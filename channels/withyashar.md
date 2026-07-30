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
<img src="https://cdn4.telesco.pe/file/qGMXDaoF75qI9a-zqKD5k1Yk2Gncm4-ShobwB9pMgJz8dR9sR3eSf3Tr-0cRkU8622HrG5LLsjevrEzRR0fcmjfFPDkz8aLJWyYJCO_vw5UeXTaSVu7vnSE2RWzYDpRnwlQQ11zFJBuCz_VPUTynaOjegf2ul_6YOz6bLe7dqXGRm6zNiTzQhWrlAoS702TCM2n1fhN3NkS2xtRaWIkNotNpgymCN1ACIO_HIdvqpAsOp5fJcjSSBLHhopgHark9uKDA_NFUj0x6yQvaS_yERx2khFnTkflznojm-wukjpjfoD8FjnEfWsGNqEbwi9Vyb-GajYXgE-F7J6Pf9vUZ0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 435K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 23:41:06</div>
<hr>

<div class="tg-post" id="msg-20113">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K27Y0uxZvbp_rLwJFfpAP9Hepjuot_CrWRX7NCKXnj3BV_xvQRK-Ithi_ORGUSJ-poIpagLGA7dQrMOvwlL5-y-TY6yGYSMDdmPFUF6t01MmjpIZQ79QqqZC_x2qoiyaJ3V4NavWVlaEiiZJ98iwOlccANQSN9XCCwmECY1VctD2s9HIGKZhvbE48lQi8URXqzVzgrCeg_hHk1oEfBYDAJgJJhWv-vCCW_BpthqHaVsSd0zvQZptNSZfglQUtXB59NBaMbo76usTYvpadU679PcC-A932826L51fIuu-_SKDrts2rsLhnjXwOnSmJPkmPjv071TCR6bdQPwfS9gZYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : حوادث ۲۴ ساعت گذشته:
حملات آمریکا به ایران: آبادان، اهواز، شادگان و اروندکنار: شلیک موشک‌های HIMARS؛ کازرون و پراش‌بند در فارس: حمله هوایی بدون گزارش تلفات؛ بوشهر و کیش: گزارش انفجار؛ قشم: حمله به یک خانه و کشته شدن دو ۳ نفر
حملات ایران به پایگاه‌های آمریکایی: پایگاه موافق‌السلتی در اردن: طبق ادعای ایران که آکریکا تکذیب کرده، ۳ فروند F-35 نابود و ۳ فروند دیگر آسیب دیدند و تعدادی از نیروهای آمریکایی کشته شدند؛ پایگاه علی‌السلام در کویت: دو انبار پهپاد و مخازن سوخت هواپیما و هلیکوپترها آسیب دیدند.
در عرصه دریایی: در تنگه هرمز، دو کشتی هنگام عبور با حادثه روبه‌رو شدند؛ در یکی آتش‌سوزی بزرگی رخ داد و هر دو بازگشتند. همچنین یک تانکر LNG قطری برای نخستین بار در سه هفته گذشته از مسیر تأییدشده ایران عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/20113" target="_blank">📅 23:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20112">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">جمهوری اسلامی یک موج جدید از حملات موشک/پهپاد را به بحرین آغاز کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/20112" target="_blank">📅 22:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20111">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا نام یک فرد و ۵ شرکت مرتبط با شرکت هواپیمایی ماهان را در فهرست تحریم‌ها قرار داده است.
بسنت، وزیر خزانه‌داری آمریکا :
هر کسی به سپاه یا ماهان‌ایر خدمات مالی، لجستیکی یا تجاری بده، به حفظ یک سازمان تروریستی کمک کرده
ما این افراد و شرکت‌ها رو شناسایی می‌کنیم، معرفی می‌کنیم و دسترسی‌شان رو به سیستم مالی آمریکا قطع می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/20111" target="_blank">📅 21:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20110">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش رژیم جمهوری اسلامی :
پایگاه شیخ عیسی در بحرین را با پهپاد هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/20110" target="_blank">📅 21:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20109">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لیست کشورهایی که اعلام کرده‌اند از ائتلاف دریایی عربستان برای حفاظت از کشتیرانی در دریای سرخ حمایت می‌کنند، به گفته عربستان  آن‌ها به این ائتلاف پیوسته‌اند :
کویت، بحرین، قطر، اردن، مصر، یمن، ترکیه، پاکستان، بنگلادش، سودان، جیبوتی، سومالی و نیجریه.
@WarRoom</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/20109" target="_blank">📅 21:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20108">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روند خلع سلاح حماس : ایالات متحده تمایل دارد پیشنهاد حماس مبنی بر تفکیک سلاح‌های سنگین و سبک در فرآیند "غیر مسلح کردن" این سازمان تروریستی را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/20108" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20107">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبکه i24 پیام اسرائیل به آمریکا:
بدون یک اقدام نظامی "معنادار" در ایران، تغییری حاصل نخواهد شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/20107" target="_blank">📅 21:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20106">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=Ik5fmdVipf4E56Tz4mTRgCDc5pabCnKP3vd26GEFhg6sAcYyFh_JflXkg1d66JoATgt9fTp_mZM3w74ZwdaMCv-gBIVXB_2HmbWIdoQqLZmV-cSL10gIsDbBln6j8FEBBUIF8G5sDDOgdQowoeB2Y_37Ec_jdzlfnLi_vgFwc-KN_usTxjVYuG-Oq3F5c1YGIY2tjVVRmXOOgyYGE2LcaBel1oLyUa75LV6Yz8sHZi5Gv-L3ZUx-5YAlcEgPmzpzmld2OXdtz6-xgBskafk_YN2ZAkZrWB305v31FuLX_-SIAy8chKxGsF0JVJkLs25rQ1YvVrcFVVg2TsLowZrg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8772ccba1.mp4?token=Ik5fmdVipf4E56Tz4mTRgCDc5pabCnKP3vd26GEFhg6sAcYyFh_JflXkg1d66JoATgt9fTp_mZM3w74ZwdaMCv-gBIVXB_2HmbWIdoQqLZmV-cSL10gIsDbBln6j8FEBBUIF8G5sDDOgdQowoeB2Y_37Ec_jdzlfnLi_vgFwc-KN_usTxjVYuG-Oq3F5c1YGIY2tjVVRmXOOgyYGE2LcaBel1oLyUa75LV6Yz8sHZi5Gv-L3ZUx-5YAlcEgPmzpzmld2OXdtz6-xgBskafk_YN2ZAkZrWB305v31FuLX_-SIAy8chKxGsF0JVJkLs25rQ1YvVrcFVVg2TsLowZrg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنای آمریکا با
۵۰ رأی مخالف
در برابر ۴۹ رأی موافق
طرح محدود کردن اختیارات ترامپ برای اقدام نظامی علیه ایران رو رد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/20106" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20105">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز به نقل از مقام‌های فدرال و ایالتی آمریکا گزارش داد که بازرسان در حال حاضر احتمال می‌دهند هکرهای مرتبط با ایران مسئول حمله سایبری هماهنگ به سامانه‌های آب شهری در ایالت مینه‌سوتا باشند، اما تأکید کرده‌اند که هنوز به نتیجه‌گیری قطعی نرسیده‌اند و تحقیقات ادامه دارد. به گفته این مقام‌ها، این احتمال نیز وجود دارد که مهاجمان برای افزایش تنش‌ها، خود را به جای هکرهای ایرانی معرفی کرده باشند. در این حمله بیش از ۳۰ سامانه آب شهری هدف قرار گرفت، دست‌کم یک چاه و یک تأسیسات تصفیه آب به‌طور موقت از مدار خارج شد و چندین سامانه نیز به کنترل دستی منتقل شدند، اما مقام‌ها اعلام کردند که کیفیت آب آشامیدنی تحت تأثیر قرار نگرفته و هیچ موردی از آلودگی آب گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20105" target="_blank">📅 20:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20104">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو : ممدانی، شهردار نیویورک، ایران و حزب الله و حماس رو حمایت می کنه!
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20104" target="_blank">📅 19:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20103">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رویترز، با استناد به دو مقام در غرب آسیا، گزارش داد که انصارالله این هفته از خاک عراق و با هماهنگی گروه‌های مسلح عراقی و نظارت از سوی سپاه ، به عربستان سعودی حمله کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20103" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20102">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سنتکام ادعای ایران مبنی بر انهدام سه فروند جنگنده رادارگریز اف-۳۵ لایتنینگ ۲ در پایگاه هوایی موفق سالتی، اردن را تکذیب کرد؛ و ادعای رسانه‌های ایرانی مبنی بر اینکه نفتکش ام/تی نورا محاصره آمریکا را شکسته است را نیز رد کرد.
سنتکام همچنین بار دیگر ادعا کرده است که تهدید اصلی برای کشتیرانی تجاری در تنگه هرمز، رژیم ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20102" target="_blank">📅 19:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20101">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش وقوع چندین انفجار در صنعا ، یمن
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20101" target="_blank">📅 18:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20100">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">«فاکس نیوز»: همکنون دولت آمریکا گزینه‌های انجام عملیات نظامی گسترده علیه ایران را به ترامپ ارائه داد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20100" target="_blank">📅 17:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20099">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">Bitcoin : 65000$
Tether : 193000T
Brent oil :91.5$
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20099" target="_blank">📅 17:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20098">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اواخر شب گذشته، دو فروند بمب‌افکن B-1B Lancer با شناسه‌های LANE90/91 از پایگاه RAF Fairford برای یک مأموریت آموزشی کوتاه بر فراز سواحل جنوب‌غربی بریتانیا به پرواز درآمدند و با پشتیبانی هواپیمای سوخت‌رسان CLEAN71 عملیات را آغاز کردند. این بمب‌افکن‌ها سپس برای تعویض خدمه به فرفورد بازگشتند و حدود ساعت ۰۱:۴۵ بامداد با شناسه‌های HARPO40/41 دوباره به پرواز درآمدند تا با سه فروند هواپیمای سوخت‌رسان CLEAN91، CLEAN92 و CLEAN93 از پایگاه Lajes تمرین سوخت‌گیری هوایی انجام دهند. به نظر می‌رسد این تمرین، شبیه‌سازی سناریوی عدم دسترسی به حریم هوایی فرانسه و پرواز به سمت ایران از مسیر جبل‌الطارق بوده؛ مسیری که پیش‌تر در عملیات Operation Epic Fury نیز استفاده شده بود. این مأموریت حدود ساعت ۰۴:۱۵ بامداد با بازگشت بمب‌افکن‌ها به RAF Fairford و هواپیماهای سوخت‌رسان به Lajes پایان یافت
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20098" target="_blank">📅 16:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20097">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfpUjydJSryPcLB5z7TPuI4x4CnP665E6sB2MsXcIgCHCbC34YurdjS1qRQl0p16Tf9cWwzQCbjWF-0AxhvM7-F5aeF7ikYeofZ11k2JONxkxhvr4chIrFUyHs4f5QZn3IYcGUUSl_-f0azbT1_gB6xpskvZLzQQYDuUWfEkgKDot6xPqksqseggK-Y8yHeKSxe4DUUz_5wgVwQaTZFNifOWckMfA12eQ3l3sanETwtusDsmIfapuQ53vi9mwEsqWvoDsj5EvYMdoP4KLmrzBRc5QKcdPANBRZ0T6_r_ib_3LqCqMZnkk2QghjdpkgnOyqkhCtoTJhckvzJ_JItd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی) همین افراد دی ماه در ایران قتلعام کردند. @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20097" target="_blank">📅 16:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20096">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گزارش کانال ۱۴ : درون کوه کلنگ گزلا - مستحکم‌ترین سایت هسته‌ای ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20096" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20095">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اکسیوس : چین با ۴۰ درصد کاهش خرید نفت موجب
جلوگیری از جهش شدید قیمت‌ها در پی جنگ و بسته شدن تنگه هرمز شد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20095" target="_blank">📅 15:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20094">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سپاه زنجان: در حمله موشکی دیشب آمریکا، 3 پاسدار کشته شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20094" target="_blank">📅 15:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20093">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">وزیر دارایی اسرائیل، بزالئل اسموتریچ:
«غزه بزرگترین زندان جهان است. مردم به زور و برخلاف میلشان در آنجا نگهداری می‌شوند و اجازه خروج ندارند. این یک چیز وحشتناک است. فقط دروازه‌ها را باز کنید و بگذارید غزه‌ای‌ها بروند.»
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20093" target="_blank">📅 15:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20092" target="_blank">📅 14:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند و داخلش کنترل پهپاد انجام میدن... هیچکدام از مردم روستا اطلاع…</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20091" target="_blank">📅 14:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خانه ای که در محله مينابي در قشم موشک خورد گزارشات بومی میگن که محله مينابي ها همشون جز بسيج و سپاهن و عادی نیستند ، ویدیو خبرنگار رژیم این گزارش رو تایید میکنه و نشون میده عکس قاسم کتلت هم بر دیوار بوده @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20090" target="_blank">📅 14:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20088">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اطلاعیه شماره ۵۵ گروه تروریستی سپاه: تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در در پاسخ به حملات آمریکایی در قشم
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20088" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20087">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9ea42418.mp4?token=dKQRnRVio882kOGbNgV_qfZ7ouO7iDQ7Xl-EAWQshgDn5ZojJli5qEFzUDlBaM1rgndHUF7xAWQLAsJjf6IOr3GyRvFq_Xj6ICcX4Wv_XS2hA1xGVCyu3CeDCy1UFbiQbo71EgdGJTJ31mr9Ej_gQV433VXSRCs5SQisMm4iMcG61LcV3KijjGs4PVWRgX3vKJiGzuRnhGQiRNUf295gHoT9W2IlFOmnIauHRbjx_idXf6607tEGuH8r65fbukxYIOxvKMN6FWIL6y8eoSzdZqMuPR6VuKYwD6RHQIF2fFJKXhjEtXEpzxIahHGbxmZXwVxot4jJ5RbGw-rJNRavckHEUV7fROT0mnLPbz4QwbtBhqn0iLOxflPjoGZ590rstWmvQsCT8zly23XQiN4S22mU14TBAvTMcxFzGzvKhsgzV5eMu4cHG_do2JCF9yO0VwbU3dMpZxtq0kY1UHUeY4URhiHnLUxhwGsrRPYvaotDm-Mbn5ke2RuTRTpuiZBrznq8o7tiHLPM-Z4MTFQ3uzPGP71g9Eh5FHE38Jor1hrt_nTElNlFvSFZk0PhyM438O0selnZTDyu51ZRcHCqYBTH-3apIyu4NamfmMN0Ynq7kjknKFj2wbVlV3x0hLnIcyqsqWRw3T2ZcRXlLrmzqEn5q5H8f6IZcFtyDReAeFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9ea42418.mp4?token=dKQRnRVio882kOGbNgV_qfZ7ouO7iDQ7Xl-EAWQshgDn5ZojJli5qEFzUDlBaM1rgndHUF7xAWQLAsJjf6IOr3GyRvFq_Xj6ICcX4Wv_XS2hA1xGVCyu3CeDCy1UFbiQbo71EgdGJTJ31mr9Ej_gQV433VXSRCs5SQisMm4iMcG61LcV3KijjGs4PVWRgX3vKJiGzuRnhGQiRNUf295gHoT9W2IlFOmnIauHRbjx_idXf6607tEGuH8r65fbukxYIOxvKMN6FWIL6y8eoSzdZqMuPR6VuKYwD6RHQIF2fFJKXhjEtXEpzxIahHGbxmZXwVxot4jJ5RbGw-rJNRavckHEUV7fROT0mnLPbz4QwbtBhqn0iLOxflPjoGZ590rstWmvQsCT8zly23XQiN4S22mU14TBAvTMcxFzGzvKhsgzV5eMu4cHG_do2JCF9yO0VwbU3dMpZxtq0kY1UHUeY4URhiHnLUxhwGsrRPYvaotDm-Mbn5ke2RuTRTpuiZBrznq8o7tiHLPM-Z4MTFQ3uzPGP71g9Eh5FHE38Jor1hrt_nTElNlFvSFZk0PhyM438O0selnZTDyu51ZRcHCqYBTH-3apIyu4NamfmMN0Ynq7kjknKFj2wbVlV3x0hLnIcyqsqWRw3T2ZcRXlLrmzqEn5q5H8f6IZcFtyDReAeFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند و داخلش کنترل پهپاد انجام میدن... هیچکدام از مردم روستا اطلاع…</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20087" target="_blank">📅 14:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20086">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارشات از آغاز موج جدید حملات پهپادی / موشکی سپاه
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20086" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20085">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دادستانی اسرائیل علیه یک راننده آمبولانس به نام فارس ابو‌الهیجا کیفرخواست صادر کرده و او را متهم کرده است که به دستور یک عامل اطلاعاتی ایران، اقدام به جمع‌آوری اطلاعات و عکس درباره مقامات بلندپایه اسرائیل کرده است.
بر اساس کیفرخواست:او از محل حضور و تردد اسحاق هرتزوگ فیلم و عکس تهیه کرده است. همچنین مأمور شده بود رفت‌وآمد و محل حضور یوآو گالانت را زیر نظر بگیرد و اطلاعات مربوط به او را جمع‌آوری کند.دادستانی اسرائیل مدعی است که این اطلاعات برای یک رابط یا مأمور وابسته به ایران ارسال می‌شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20085" target="_blank">📅 13:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20084">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری رویترز در گزارشی ادعا کرد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل طرحی را شامل پیشنهاد ترور هدفمند فرماندهان ارشد سپاه پاسداران و ارتش جمهوری اسلامی ایران به دونالد ترامپ ارائه کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20084" target="_blank">📅 12:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20083">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی:
آخرین خواسته امیرحسین صفری از مادرش پیش از اجرای حکم اعدام این بود که به همه بگه ویدیویی که جمهوری اسلامی از اون منتشر کرده، اعتراف اجباری بوده و اون کسی رو نکشته.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20083" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20082">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبرگزاری رژیم : نتانیاهو به ترامپ پیشنهاد داده یه لایه دیگه از رهبران و‌ فرماندهان جمهوری اسلامی رو بزنند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20082" target="_blank">📅 11:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20081">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx9mhQEwrIDg00-pK0sJF9e80OQX3HnkgGbMmu0-L67_s5ZMl381PcPpAMhO-WPssPta2_Z1D-HUOzZsvbx3GkA2CrRAR5EF_dyrWDge36-r8gBglml98zuOAoo8Np068DWuEvGWPqEtLXBPm8fyHBbSCGoRvdZEMNWKUHfzOc2YSc1MYZ3Leftq7px47nq12shMA6gYl1VpODcEDzyy-XyZgGrg8pWx1ckgr_4ugUHiUkCFPJjuTikYEocjojii9vl0wxdiFhu-ZkcN29eMV-XhF61Df88QfO_hkls2H_9G8U-CJ2SPwd7YYbfF8XLBhsfyjjyNxhqaNeJ7e3D1eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏۳ تا از کثافتهای رسما گی حشدالشعبی که در حمله عربستان کشته شدند (عکس رسمی)
همین افراد دی ماه در ایران قتلعام کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20081" target="_blank">📅 11:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20080">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو به شبکه ABC:
حماس باید منحل شود و غزه باید از سلاح‌ها پاکسازی شود.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20080" target="_blank">📅 11:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20079">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سپاه: متجاوز همین امروز تنبیه خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20079" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20078">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وزارت دفاع کویت : یک ساختمان متعلق به یک شرکت چینی در شمال کویت مورد حمله موشکی ایران قرار گرفته و منجر به کشته شدن یک کارگر و وارد شدن خسارات قابل توجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20078" target="_blank">📅 11:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20077">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنتکام : در ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند. دارایی‌ها و تجهیزات سنتکام…</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20077" target="_blank">📅 10:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20076">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">نتانیاهو به ای‌بی‌سی: «رژیم ایران همیشه دروغ می‌گوید، تقلب می‌کند و با زمان بازی می‌کند»
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20076" target="_blank">📅 10:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20075">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5647d258de.mp4?token=V9CIRCM_SjxHOrDmyns3Ge1UXXzcEMYvepNjuwHrpTA8i_VrwHCZ9VcI547-3VtS4htJImmpfOU0t_w02CncnDLGojnv6M-XnROx5BcoIXeFxYenMEq1SGpVX8Z1VXNzQmUFWkVjjfAzNxQnrgv-OmaxIvG6rEtHJRWIsaGETF6Rrwf_OznsKzjYwm_s3fpE1g4gq4vti5yb4nitEIurNoq83-YDDWGJsP-DbB8z7nFKlUc_DdQbg72p3zrd_VL-8IYYwFRsjn6ol4x2HS9ZEy5xk62zE8hpEK3TK0Zz1HuFFG9jarBRRQBPi7Fwrh8lqICI1AiuWLDWbdTz3elmBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5647d258de.mp4?token=V9CIRCM_SjxHOrDmyns3Ge1UXXzcEMYvepNjuwHrpTA8i_VrwHCZ9VcI547-3VtS4htJImmpfOU0t_w02CncnDLGojnv6M-XnROx5BcoIXeFxYenMEq1SGpVX8Z1VXNzQmUFWkVjjfAzNxQnrgv-OmaxIvG6rEtHJRWIsaGETF6Rrwf_OznsKzjYwm_s3fpE1g4gq4vti5yb4nitEIurNoq83-YDDWGJsP-DbB8z7nFKlUc_DdQbg72p3zrd_VL-8IYYwFRsjn6ol4x2HS9ZEy5xk62zE8hpEK3TK0Zz1HuFFG9jarBRRQBPi7Fwrh8lqICI1AiuWLDWbdTz3elmBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به ای بی سی: بعد از پایان این جنگ، فکر نمی‌کنم تنگه هرمز اهرم قدرتمندی باشد، زیرا خطوط لوله انرژی را از تنگه به ​​دریای سرخ و از آنجا به اسرائیل و مدیترانه منتقل خواهند کرد.
ما می‌توانیم این گلوگاه را باز کنیم و این کار را خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20075" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20074">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=tqBLxAuGaSabQBjdEcO741Y6aLO-7T2svYqFTwyx4IBF_0sVH2TCNuJxUHOy0asFmWX7lw_m9TZNswPHW3MVcY3QrH0SrNo4PprrADVdFbqb8PkjiMg1nLFCBA2pRaSBPGZzLNFwF3Cqs3zv_spDcSVO8937bniUog3uwnH7ctfXv-jG1pSUI95mH_X-OzlEOByQHr4nuQ3eirM00GRwB7p-OF3-uy00KpdsqWFum2THNO4DrpyXC36ah1dDGo9DDxIQncpn2deiGryXwIJG0DqWUDXi9tDtNSMer9ZP-81TCj7rkwyQcj1NcSVr5xcMBpIh5UqLyMkVYfdB3n1ZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3061f41fa2.mp4?token=tqBLxAuGaSabQBjdEcO741Y6aLO-7T2svYqFTwyx4IBF_0sVH2TCNuJxUHOy0asFmWX7lw_m9TZNswPHW3MVcY3QrH0SrNo4PprrADVdFbqb8PkjiMg1nLFCBA2pRaSBPGZzLNFwF3Cqs3zv_spDcSVO8937bniUog3uwnH7ctfXv-jG1pSUI95mH_X-OzlEOByQHr4nuQ3eirM00GRwB7p-OF3-uy00KpdsqWFum2THNO4DrpyXC36ah1dDGo9DDxIQncpn2deiGryXwIJG0DqWUDXi9tDtNSMer9ZP-81TCj7rkwyQcj1NcSVr5xcMBpIh5UqLyMkVYfdB3n1ZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری ای‌بی‌سی نیوز: وقتی در کاخ سفید با ترامپ ملاقات کردید، آیا سعی کردید او را متقاعد کنید که حملات به ایران را از سر بگیرد؟
نتانیاهو: در واقع نه. این یک کاریکاتور یا تصویر کارتونی است. این درست نیست.
ما در واقع هر سه احتمال را بررسی کردیم و فکر می‌کنم این کار را به صورت علنی بین دوستان و متحدان انجام دادیم.
و این تصمیم اوست. این تصمیم اوست.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20074" target="_blank">📅 10:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDnpRloS4Iqbqda4tgVA-wM3XM0B8oCm6s6R-r0Dhlwtd8eELQnZYkvfLyUaoKI-aL2MWrJA1t_tiEelWfFR9ROiY9_va1XPUz7rqs0yBuy4Bvz2MdOGDAIBxud8zAsUAKE3107FGOX5idVK2b9lGwkCOP-Lff9QOAP4qchh4q2dmT2kDWjLKRswmji0eNkQ9nSA_mNYwxL_89_eY1Ecb8KgUOZgxI8t-gYkSHbi1SHBr7zie8sSLyHJ7pw1EJFMUGPwT0_quVJ7MEZMqnsQEqbCP8NkETtm9hkdrosEO5sNzt2u-sgEdyuJaFnEPMEiQIYdUMgDbHTlhfUfzb5kIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه حملات بامداد ۵شنبه ۸ مرداد
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20073" target="_blank">📅 09:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ارسالی : در قشم گروه پهپادی نیرو دریایی سپاه و هوافضا سپاهاز طریق آنتن مخابراتی شهری پهپاد کنترل میکنند خود اتاق کنترل پهپاد رو توسط شبکه به خونه‌های مردم منتقل کردن بین روستاها خونه کرایه کردند
و داخلش کنترل پهپاد انجام میدن...
هیچکدام از مردم روستا اطلاع ندارن که خونه بغلیشون چه خبره فقط میبینن تردد میشه در صورتیکه داخلش سیستم‌های کنترل پهپاد قرار داره
لطفا اگر هم قراره اطلاع رسانی بشه
فوروارد مستقیم نکن یاشار جان
آیدیم به فنا نره
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20072" target="_blank">📅 09:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">معاون سیاسی امنیتی و اجتماعی استاندار بوشهر از حمله هوایی به اطراف شهرهای بوشهر، جم و خورموج در شب گذشته خبر داد.
در این خصوص تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20071" target="_blank">📅 09:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=BKYmREcCcjQcVjpqGeNgTvE1giC9Urro7ZnF4fu--UFm6jDd41D9AQgPbyKON8LdOVF2n5vPB0B4MD--iDjSm9EjYeWi1G4b7kYGza58Gk-HXp12QID4j42eO6Xfp_Mpnx6s2ggq5QfVsEuLbfBww1K-y8VkadMetU7BXCU3vPVyjdzZ8BA-sTEK2tM_tvv5JL6uLBxWNb_k-oLynUQ3xhaQ6E2TXCucUh_TXkYb3Ep2sYGmIgpwOkC6pWPl1NEonoLCOC_gCwLPY2u3usOQdz6aTmYoHFjR91qGnTY_8aro8HvksxgKpNgnbqp8F85jOX8ADHyUaVT4xZ3Xydf4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe63b4dfd0.mp4?token=BKYmREcCcjQcVjpqGeNgTvE1giC9Urro7ZnF4fu--UFm6jDd41D9AQgPbyKON8LdOVF2n5vPB0B4MD--iDjSm9EjYeWi1G4b7kYGza58Gk-HXp12QID4j42eO6Xfp_Mpnx6s2ggq5QfVsEuLbfBww1K-y8VkadMetU7BXCU3vPVyjdzZ8BA-sTEK2tM_tvv5JL6uLBxWNb_k-oLynUQ3xhaQ6E2TXCucUh_TXkYb3Ep2sYGmIgpwOkC6pWPl1NEonoLCOC_gCwLPY2u3usOQdz6aTmYoHFjR91qGnTY_8aro8HvksxgKpNgnbqp8F85jOX8ADHyUaVT4xZ3Xydf4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خمین
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20070" target="_blank">📅 07:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20067">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GztC7bPfib2MLvshS0RuJrd4MqGZ2U25S0IOKwbkH-6HEAXqQOmPscjy4E2bnWWu1XDNf7UCV7_Er6wnoBbP7o-GAgaprUgAnmi6GchEOzDtGB8hz6FK-5QsQIpJmB7CDrYRRvCYR9bJS19WVxB4TDBIID8ELCrrM-9GYPO3lL4k6UtiqtCeIQAkukNBmDZ0xv-ZvbORzHjBNBpUd_20Th2mq3FwdR1_XU4lYJhAWie_Przfvc-7KU5F39Mo2-qCBaSrdLowgsQXdpLFHvs6XyQzyazclnOlyNv5f_ysnZSq0fwQLVjk5-W51nn96ggHNiV4ZAOjad-YjKdZBU3wDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-QnTzhp5WftTStjucpU-4heNWWJkX2gnL4pqCpWrCiwDxjlCz_HjfXiO_qZbOCvsknsioOpnfvXaLC5gQdcZK1jI938OFXIxPOBwxdRgDjVknqDk-HS9KQ3p0cskjqdtteEQJzPkz7rqdxQDOhJoxchljAge7B9XKybv-g9ji29Y4OqGxy3anO0OmiexXBtXQZ5HaEq3Z3vqJA_GGPUJzkFU8WgpZLMCtmNRKqaoFYJUY9WZ-6C0vd_PAVoC8cXbjxwUMc7qUGgZ9RUCsy8M33XiZ3nZctLqjK7Fk9SYHnic_7XLZPkxtSfE0YCY2qWi8ZUm2J-j1nbMtWArBXVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tg_4-c2f_1fLuvwjp0OokiF-QFU4G-e76mvrg4fOUVGqr6VNwQvuoMj5fTmEQYcB5T8XIMe1FgSG7YfQwTsXFkejRY0TnlelikVsfavolkpeVbYNA-vBdD8nAQVX05vUt9nDbOAMUzkWj6ENHhFcWUjrRmiHOFgY3QP6NlIEFbw6LHaf7uvlO2S8838X9jA-W5Zsrw2s_0ddat505I7Qntgz8D-vYRO2epa2775QklAbz7rJkQHwFDiH4KsglSsE6wWPWZs3FV-Qdb-HlAPqE8IiKZTwJN4KFlth7dtIY3Cguw2eNB_gY9UB8-Wwcdky_Or9vARHNgpbcltioLsPaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قشم ( از پارچه های یا حسین به نظر میاد یک پایگاه بوده )
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20067" target="_blank">📅 07:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20066">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Q1FKVpYgV3H0Rr8TK1KRFTMvCdBZYe19q8RgQqoyzSYdOUiAIg7AOp1jpMFGbLRAzr8ERaNqQZsy-lZsKd6E9mZFEsdCnKQncfxqE0xEwyyUSQ4MrYp5ZOyS6H67lZrLs73y0OGei6yVLAh1HUwDYf6Cmbpm2Qkh5SLozCBuhscthAIo_GVdzZnWit5VcoOeJgNS9SwPZxCY5-mRj6D6ydzfi5S2hN4X6fO2ua7oZEPzExXe7-9cLpsoGrYAZA1PBGki-BMg_PdJSnknFLQJtssUY0NcX-_O9QTNwZg021GxYV_ojf06oSoKVUT4rwpYAt9Sg6ckbsFjQZ0GAVRK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739655b0d2.mp4?token=Q1FKVpYgV3H0Rr8TK1KRFTMvCdBZYe19q8RgQqoyzSYdOUiAIg7AOp1jpMFGbLRAzr8ERaNqQZsy-lZsKd6E9mZFEsdCnKQncfxqE0xEwyyUSQ4MrYp5ZOyS6H67lZrLs73y0OGei6yVLAh1HUwDYf6Cmbpm2Qkh5SLozCBuhscthAIo_GVdzZnWit5VcoOeJgNS9SwPZxCY5-mRj6D6ydzfi5S2hN4X6fO2ua7oZEPzExXe7-9cLpsoGrYAZA1PBGki-BMg_PdJSnknFLQJtssUY0NcX-_O9QTNwZg021GxYV_ojf06oSoKVUT4rwpYAt9Sg6ckbsFjQZ0GAVRK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قشم
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20066" target="_blank">📅 07:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20062">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sqok3UdWnwFpk-W32QCvUOgrsuonZd7fX2YoM38T4OiX59crEBVaJR39zB4VuwlHuvaD1ZFEeXIbp1BHDT7AELW0jrhsKLhwQQSIX0JhM2rFqeSuUlikTmXRALQ_H5V_wYBzLQQ6WUc5Lx5_aSyxNz8rYxD8wxE2xuBxWfurRw0Tew6XbMvWQLbik-Y0iEavQtGnRpKgQvaLZXOwwctZwD8orKPby-9LEqp0dlSaraiV1-sF7gLpPGQLqjHhStH4D4pPCABPVyOOOZl4HORFiQKS4ESqfzxuMpxhy8Aaso32BlJ1xW2cQ8MC1tnbYfYrGLrr6GS9NqrNl6caVobdPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuU7W3BvcqVSCCk6imaId_muvgDCqTokHzuGqRDpSvyAanfpY5DxJ1E4FfiuIUKHCBM6BKD6ChpyA2KbnCFsmt2yDl9a6rbeeda_6fYJZgCFP56opCvtmLfGvEhnpKdi9ci3hutQBpb3LwshV4jpacZjXeR-CeS3hNH2rgWpZqrYvC8ZI9OfrqkqV34b1gbbl6Ht2nI4eUkyujxgUvJeaC7PN4VSVVFz-L8Tl9UDQM6I8aR15CVvuU6OvXgF_XFQX-DBd1RDoXNTrIiEslBK3m-yfqBOh3zmBlh3oddtJj3PbUqXoO_TQbGA6gHpM7XsTt8H-yGjxFVjg6iITuu2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_BS190uWczjeCdVBFPoQuAMpucN6k7FXsI8WFJktgQv_oWtCEP3gNTJ7uk_a95TEq6UWby-Sv_5fTDTbzZF74BTE-22p7WouL-cWWnJumJoA1Wpqts-396mw3Nv8X29KCaltbXo1cGI2QkOy_psLXihzbFIrkVbFrDfhM0Gx8vqCogzq3IZGy88X__yxoDws4EljuMBwzubTFFz60A3RoYcjcjVliD0wWlmzhjTSo2CBaWjmvow6HNuk1kpPFY27wM_FZlrCMPeEZWVnMZMsDSKC3OGfXFx8TnYa4fY5lx7DhM2c_Gum0nu2W-1z6x0g1_13XCt2BB7aJme7PcpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sXszVk36zJnRbe2M7b1_BnLzY3arkoEQuSYXiuK5a_mt1S6T6bwgy2bBsJT5r6ak74vx4tgkl623Isw8Tnrdf0TvDhhOKSf7Kxu5SKBcbpDtPL0FkX-R4Lq9WXyqnL8-CNi8UVV2Zv1-eLS4oEfQXJpdsGIidVAG3WMUR9NsJflmAiqwO3J1esp5hEKIv8vWVt9F4Y8fSXGKo5hnDDLuozNn_VSx2rnALe7oNExk4KAhAb5wTxl-s02E-fh06jNiXRmMLA786eP_83bS4v22upzTC4TmmJ-c6rWUmUkkp7amCcu95en3uHZbnkMYl2dlxyu8khF53TM2j_wpf784aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از یزد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20062" target="_blank">📅 07:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20061">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=sYGWgtce7uAxSq-D95DelzITvhdMw4mxH6SV_wDaY3hgBS1YwuKIZ-6JtUDzQL3qQDCLWr6g0OFLQ95ZqikQ5pI0BtI2fWMZ-JUigwEKUXSEET3r92ShnRHWB0uWDJzD9adaG6x_FxfXTxgBAA2TDWB0ZqdK_fYXxwHlsQY9YnRlCwAHD9kYCAHrTnYQbYWzXNd4s_00T1c88Ca5rku1MGiohyu7Zz0ZBcZG_HCdeOOBz0RK7ucM1xyVdbNt0JZqHF19yRbnFMcjXrpAZgdJxa8ulPxTE_0q088emG01boCB0pePYJfVUeL0OI2_I_fNwy-GWw7qnB-elpDDCobdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c918aabbfc.mp4?token=sYGWgtce7uAxSq-D95DelzITvhdMw4mxH6SV_wDaY3hgBS1YwuKIZ-6JtUDzQL3qQDCLWr6g0OFLQ95ZqikQ5pI0BtI2fWMZ-JUigwEKUXSEET3r92ShnRHWB0uWDJzD9adaG6x_FxfXTxgBAA2TDWB0ZqdK_fYXxwHlsQY9YnRlCwAHD9kYCAHrTnYQbYWzXNd4s_00T1c88Ca5rku1MGiohyu7Zz0ZBcZG_HCdeOOBz0RK7ucM1xyVdbNt0JZqHF19yRbnFMcjXrpAZgdJxa8ulPxTE_0q088emG01boCB0pePYJfVUeL0OI2_I_fNwy-GWw7qnB-elpDDCobdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز شبستر دو تا موشک رفت
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20061" target="_blank">📅 07:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20060">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2NCNA-OqmLnO1vjoJNzYuGszANjHQTijIIcoA6P3UQqEaD2XZq-an_TZ9gtfZfo4IUrirqQ5MrT0F2nVA4bix8IBfOeR8huw3qITk4OWLkVKwkPnWyjLw55zzu-tAnjrNOmNddnMaSzCu6Gq72aTX_CwifhWBHbrAo2_FOQF-SaYCykbHDzFPHpHbWJWhV8WSDQzSCU49nwUJdv3bMqZI3vi0Q2Q908sy8hwfglwKIXcnSoXG1e5Mv_Si4UMAJhr-FA0GvZCQNwJXC_z8aP2vi-8VC0PN-iTag3SGy0qX2NKt60f2DVsqVtVIwxHYo_JWD_J2vuhSBIhmFdnCSU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان پرتاب موشک از خمین
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20060" target="_blank">📅 07:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20059">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=R-wm9zMEb1d0NHMBX9I3Act5vowzqWCD0gSK1jMYZZa4pWV6wn84S-pCc43kf-MnptvskP-xLTHdbtil6XDe4y7Qv3zCRynucVfOFWqdkio_xxnNshPcBRRIseiGChOe42xgxMEX8IlQEGucycWbxmCpBFf5RF3ibihQ0mrhQcOuKzUcXMbxGmOmvYiVgOgA8CauajnQRMyhaf1REy1KOVNwgClmvDbrhPYGPB4dzjm4SEy_EFpJkElciEaQDNDGm1jeGGBCENB_y-jfQDeAH47Bp3vuKWK-et6bLWVDXgfhum2BcjTO6hRswVT314PHaJywKnEHMQPELSgug6YosQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a4989fd2.mp4?token=R-wm9zMEb1d0NHMBX9I3Act5vowzqWCD0gSK1jMYZZa4pWV6wn84S-pCc43kf-MnptvskP-xLTHdbtil6XDe4y7Qv3zCRynucVfOFWqdkio_xxnNshPcBRRIseiGChOe42xgxMEX8IlQEGucycWbxmCpBFf5RF3ibihQ0mrhQcOuKzUcXMbxGmOmvYiVgOgA8CauajnQRMyhaf1REy1KOVNwgClmvDbrhPYGPB4dzjm4SEy_EFpJkElciEaQDNDGm1jeGGBCENB_y-jfQDeAH47Bp3vuKWK-et6bLWVDXgfhum2BcjTO6hRswVT314PHaJywKnEHMQPELSgug6YosQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اهواز حدود ۴ صبح
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20059" target="_blank">📅 07:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20058">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=cznPpT5Ejtqwee--F4Qi4aUr4sT9OOv3bXnmMIh66cqpdCJ18AyEBcukb_1b7MW0OXpNwfZCH0XHCLLNcg6UsscjoSFG5zxOoFKE8njVfRmnjI2Aw887I4-Z2OEKmWqqZHFTaJg3iQTljfYF3bRFwm5jkGbMdbNtPo15MHwpKhCHn6qZDw31ygvxk7iki_xAMphsxirsbLJq0sp6ZEzFBadtmPzZCxEDhz6AioaGPrdRWvrvXbZETH2xLHaAjJ03zvOKAak_Fw27o3B_ia2W7dYHbl_fQNtSpipxzXmIWHu4VK2TC2to5BSvlbPVb8wS1lPCivOIK_m91IYtDq1Sag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc7049e361.mp4?token=cznPpT5Ejtqwee--F4Qi4aUr4sT9OOv3bXnmMIh66cqpdCJ18AyEBcukb_1b7MW0OXpNwfZCH0XHCLLNcg6UsscjoSFG5zxOoFKE8njVfRmnjI2Aw887I4-Z2OEKmWqqZHFTaJg3iQTljfYF3bRFwm5jkGbMdbNtPo15MHwpKhCHn6qZDw31ygvxk7iki_xAMphsxirsbLJq0sp6ZEzFBadtmPzZCxEDhz6AioaGPrdRWvrvXbZETH2xLHaAjJ03zvOKAak_Fw27o3B_ia2W7dYHbl_fQNtSpipxzXmIWHu4VK2TC2to5BSvlbPVb8wS1lPCivOIK_m91IYtDq1Sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندرعباس ۳:۴۵ بامداد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20058" target="_blank">📅 07:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20057">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=Tay46GBXChgMKh0lCEkU0IlxgnWo-kC5kww8qpOaFKU4k4jLPOs5LK4ZnETD5eYi5lqyUTQ0ArcCPdhZa33CMz6Xv1wVQlI16fX-HagPJCLEA_nky5ICLChcOqJbnydLPVEqFptJlWLYmztnA9mrZ3MJyO0-RZbYHLP8q5ktbv7nn2GUVXf1bEz404_1mJ-6qOk26pK9il6D0poIh2ElC0QGknkGYPTq9K9TZD_JzRVOckF_JTt-zB1zCDFC59Qc_QlQ1wY93hfDAHfu9uFK1ZTFRNXGuz02M1Ma-aGSzSqvX41GXNY-nc5ZZZ1Y7BKW6v8GFDrHqFd2H4Ux2SRNxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b11a9cf.mp4?token=Tay46GBXChgMKh0lCEkU0IlxgnWo-kC5kww8qpOaFKU4k4jLPOs5LK4ZnETD5eYi5lqyUTQ0ArcCPdhZa33CMz6Xv1wVQlI16fX-HagPJCLEA_nky5ICLChcOqJbnydLPVEqFptJlWLYmztnA9mrZ3MJyO0-RZbYHLP8q5ktbv7nn2GUVXf1bEz404_1mJ-6qOk26pK9il6D0poIh2ElC0QGknkGYPTq9K9TZD_JzRVOckF_JTt-zB1zCDFC59Qc_QlQ1wY93hfDAHfu9uFK1ZTFRNXGuz02M1Ma-aGSzSqvX41GXNY-nc5ZZZ1Y7BKW6v8GFDrHqFd2H4Ux2SRNxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">4 صبح آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20057" target="_blank">📅 07:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20056">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فاکس نیوز : هدف سفر نتانیاهو به امریکا تکرار 9 اسفند و بمباران تمام سایت های هسته ای و موشکی و نیروگاه های رژیم تروریست اسلامی ایران بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20056" target="_blank">📅 06:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20055">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNKFrWbGJ8x03mb4deIxYYED0auOLAIJVn_WLaFW0v8s2wfhe8h2CdECEX9svY4HhXBDuyJC8FxIUMSn-TWn5SuZhuSSMJ2L10jwmv8u2NB7C9i2ZdCoEV8QnlxrMAAHbJx-fZ1lpNyi6YljpVowZry94xxcKH9gCXZ4mhEaBxRprWkjBUUH3CuCpVXBfTlQe4TX7eTpLIYU5_44C9s3A4yD0KFHWQCJ7q76w3f5LiqDHxedXGkVCjNvmzldL6C_poIWV7FhiBaOchYnEAisiwj9CaSgjf0xQEz0gzP7acAT4IbIlDo5xsajiUrjo-ue6v-N2zHHGfesp6NhZZ2ZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ : ده‌ها موشک ATACMS برد بلند آمریکا از کویت به سمت تأسیسات نظامی در داخل ایران شلیک شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20055" target="_blank">📅 06:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20054">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=eF7ucFDlgHaMP484QRo1A1PZpThl4JCjfR3GDj_uapcqK47TbIEbB1nnmMsME1Qz7qm62IwkytrTfInz2rxcbMXDcFsJK0apZr1wcMXS5Ef6yjPAyMLz8VdCtdII6Ty70NnIt70xHQL7zbwAN0uQYhD6wfepRLKG4QXNwOQi44ehjA1LNEPUoErBiCFp6Nob6dolaxDQ1Z9qDuIt4IhDcjG_LBTUvsa7fRFEXBvSt4u9rK0aD2ooYXQu-lnaFUpw2fvINgWl2yDsTtiVZ4ZkRKGGNRXfxi6B-YKKB8x5yZAFP-x-CoHmUz90xNDKlKizlr60ALO59APe3TGuz_BaKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdc88dc378.mp4?token=eF7ucFDlgHaMP484QRo1A1PZpThl4JCjfR3GDj_uapcqK47TbIEbB1nnmMsME1Qz7qm62IwkytrTfInz2rxcbMXDcFsJK0apZr1wcMXS5Ef6yjPAyMLz8VdCtdII6Ty70NnIt70xHQL7zbwAN0uQYhD6wfepRLKG4QXNwOQi44ehjA1LNEPUoErBiCFp6Nob6dolaxDQ1Z9qDuIt4IhDcjG_LBTUvsa7fRFEXBvSt4u9rK0aD2ooYXQu-lnaFUpw2fvINgWl2yDsTtiVZ4ZkRKGGNRXfxi6B-YKKB8x5yZAFP-x-CoHmUz90xNDKlKizlr60ALO59APe3TGuz_BaKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت اطلاعات سپاه گلستان اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20054" target="_blank">📅 06:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20053">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=Y64RUoWxCzYQv_Y5yBTHS8PgpSvdmSbzRw92E0gayJiTrlzRAsR3yF6mQqVUUo9p7Li_Gfykc_ytljKB1G3S1LXktn4e6tQkAzQBVTIn1b43_hiu70GQyHAXbCOhhaWgo1WT1eIVyxH5vRI6gj1upLnfMCvAYJGg2X--0u9vDilPBp7cCKQYlekgd57MxnppFHqDsmNftD7-3VUYNov5z4HQDiGPn0tWxBvRMfk3NGvoG-IAbmJYToMxxA1sJZFb6gtZLMCVnlWcmcSgF-kUxXzaxDm2QxCImXLWypIwkE_Zmr1hLSpsHsHJXTzEzNd1occTTmoHeNi6QszUIG5x3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aabd75843.mp4?token=Y64RUoWxCzYQv_Y5yBTHS8PgpSvdmSbzRw92E0gayJiTrlzRAsR3yF6mQqVUUo9p7Li_Gfykc_ytljKB1G3S1LXktn4e6tQkAzQBVTIn1b43_hiu70GQyHAXbCOhhaWgo1WT1eIVyxH5vRI6gj1upLnfMCvAYJGg2X--0u9vDilPBp7cCKQYlekgd57MxnppFHqDsmNftD7-3VUYNov5z4HQDiGPn0tWxBvRMfk3NGvoG-IAbmJYToMxxA1sJZFb6gtZLMCVnlWcmcSgF-kUxXzaxDm2QxCImXLWypIwkE_Zmr1hLSpsHsHJXTzEzNd1occTTmoHeNi6QszUIG5x3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : در
ساعت ۵:۳۰ صبح پنج‌شنبه ۳۰ ژوئیه به وقت تهران
، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) با موفقیت یک موج سنگین از حملات را علیه ایران، در پاسخ به تلاش روز گذشته برای حمله موشکی به نیروهای آمریکایی، به پایان رساندند.
دارایی‌ها و تجهیزات سنتکام ده‌ها هدف متعلق به سپاه را در ایران هدف قرار دادند؛ از جمله مراکز فرماندهی نظامی، تأسیسات موشکی و پهپادی، سایت‌های دیده‌بانی و دفاع ساحلی، و توانمندی‌های دریایی. هدف از این حملات، کاهش بیشتر تهدیدهای ناشی از ایران و نیروهای نیابتی آن علیه نیروهای آمریکایی، کشتیرانی تجاری و کشورهای همسایه حوزه خلیج فارس عنوان شده است
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20053" target="_blank">📅 06:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20052">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">باراک راوید خبرنگار آکسیوس به نقل از مقام ارشد آمریکایی :
آمریکا هم اکنون در حال انجام حملاتی در ایران هست.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20052" target="_blank">📅 02:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20051">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بوست کم شده داریم لول میایم پایین یه کمک کنیدد بریم بالا استیکر شاه برگرده به دوستاتون که پرکیوم دارن هم بگین
https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20051" target="_blank">📅 02:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20050">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش‌ها از شنیده شدن چند انفجار سنگین در نورآباد ممسنی فارس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20050" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20049">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وال استریت ژورنال گزارش می‌دهد که دریاسالار برد کوپر، فرمانده سنتکام، در ماه فوریه تخمین زده بود که کمپین علیه ایران برای دستیابی به اهدافش ممکن است شش هفته یا بیشتر زمان نیاز داشته باشد.
کوپر در ۳۱ مارس ارزیابی کرد که هنوز حدود ۲۰ روز دیگر برای تکمیل عملیات نیاز دارد.
با این حال، سرنگونی یک فروند جنگنده F-15E Strike Eagle آمریکایی در ۳ آوریل بر فراز جنوب غربی ایران، علیرغم نجات موفقیت‌آمیز هر دو خدمه در تصمیم ترامپ برای پیگیری آتش‌بس تنها در چند روز بعد نقش داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20049" target="_blank">📅 02:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20048">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش صدای انفجار سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20048" target="_blank">📅 02:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رویترز: انفجارهای شدید و پیاپی، کیف پایتخت اوکراین را به لرزه درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20047" target="_blank">📅 01:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20046">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به گفته روزنامه وال‌استریت ژورنال ، ارتش ایالات متحده قراردادی به ارزش ۵۸.۶ میلیارد دلار با شرکت لاکهید مارتین برای افزایش تولید موشک‌های دفاع هوایی پاتریوت امضا کرده است؛ بزرگ‌ترین قرارداد تاریخ برای موشک‌های پاتریوت.
این قرارداد بر تولید موشک‌های پیشرفته
PAC-3 MSE
تمرکز دارد؛ موشک‌هایی که برای رهگیری موشک‌های بالستیک، موشک‌های کروز، هواپیماها و پهپادها استفاده می‌شوند. هدف این برنامه، افزایش ذخایر موشکی آمریکا و متحدانش و بالا بردن ظرفیت مقابله با حملات گسترده موشکی پس از تجربه جنگ اوکراین و افزایش تهدیدهای موشکی در جهان است
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20046" target="_blank">📅 01:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20045">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آسوشیتدپرس : ایالات متحده تمام مذاکرات را رد کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20045" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20044">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b45ec100a.mp4?token=q22ZcWP6i242xT2Auf8Ho9HJ46iNwXWThv9maF3mnxG2qL8nvIVasgADyTeae3PG6sTvlmQbHz8SjOw46IYcXN6tsSVEq8NJFlDjcJcFWHqIPbfK-y337Q3xhqqO_UiCE3mb5a8Kgvr25qhmDcgpxJ5oQrcTpBNb6VJIwHsI9qasHk9jw99qfUk4NKwMqlkurPhl7Kf3ahrp9tdaZnRJqgIAdkWD3i2FnwqKMJ-dpj-WuqS74dIaKFt13uQTEO7laRJ9LCSru7wSN-_5Ol69PCGhTKIXk3KZ6efBASs3w9B021Zn2WGOcgdDH0zjz7TA0KMXV648ZmlCpNq0AZf6kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b45ec100a.mp4?token=q22ZcWP6i242xT2Auf8Ho9HJ46iNwXWThv9maF3mnxG2qL8nvIVasgADyTeae3PG6sTvlmQbHz8SjOw46IYcXN6tsSVEq8NJFlDjcJcFWHqIPbfK-y337Q3xhqqO_UiCE3mb5a8Kgvr25qhmDcgpxJ5oQrcTpBNb6VJIwHsI9qasHk9jw99qfUk4NKwMqlkurPhl7Kf3ahrp9tdaZnRJqgIAdkWD3i2FnwqKMJ-dpj-WuqS74dIaKFt13uQTEO7laRJ9LCSru7wSN-_5Ol69PCGhTKIXk3KZ6efBASs3w9B021Zn2WGOcgdDH0zjz7TA0KMXV648ZmlCpNq0AZf6kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش خوردن عنبه
😁
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20044" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20039">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20039" target="_blank">📅 01:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20038">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">گزارش تایید نشده صدای انفجار در تبریز و بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20038" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20037">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خبرگزاری صدا و سیما : شنیده‌شدن صدای انفجار در پایتخت عربستان
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20037" target="_blank">📅 01:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20036">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تیک تاک ، تیک تاک ، تیک تاک
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20036" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20035">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">همان طور که دیروز گفتم، اینستاگرام و چنل تلگرام رو میخوام پرایوت کنم. این آخرین فرصت برای کسایی هست که ممکنه دیروز این پیام رو ندیده باشن !سریع عضو بشین تا پشت در پیش عرزشیه ها نمونین
🌐
instagram.com/yashar
🌐
t.me/WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20035" target="_blank">📅 00:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20034">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم‌اکنون ۵ هواپیمای سوخت‌رسان از اسرائیل و ۵ هواپیمای سوخت‌رسان از عربستان سعودی، به سمت خلیج فارس بلند شدند، دو سوخت‌رسان هم‌ در آسمان خلیج فارس با فرستنده روشن مشغول عملیات هستند. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20034" target="_blank">📅 00:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20033">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaCFt_A9Dh8hi6qSxrXjzKhAh0-_Y1oxr6gYQHIsATjPJXBgkb7Nz-dnta8_ePjHwmzv3t_KS5vJknQB4IVG0MATAPGelj4-70pu9CR0l1t3os5fOEDzTGsSMXH4zCD5EAlaBhPn_gC1sn3vYBadIGHrcOWJFqJtLIMXWP9r1pN4NnwwIxx_HDjyQHG9HKjWkNmteqgbm7BxNK5pUXx2e8kTy4tf1YTOuEKqPW8_FDSgDTklFZdY140O5s2RA4_YqjX_VyBArIKudy04sppgD7y_l7ytxl524qgw8URjmMGMg-oTUhspISBdESx0AHKIAuGi9BLetMkvFwseIgDlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌اکنون ۵ هواپیمای سوخت‌رسان از اسرائیل و ۵ هواپیمای سوخت‌رسان از عربستان سعودی، به سمت خلیج فارس بلند شدند، دو سوخت‌رسان هم‌ در آسمان خلیج فارس با فرستنده روشن مشغول عملیات هستند.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20033" target="_blank">📅 00:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20032">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وال استریت جورنال:
ترامپ با وعده انتقام از ایران، از یک دور جدید از حملات "بسیار شدید" خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20032" target="_blank">📅 00:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20031">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ارتش اسرائیل آماده حمله سراسری و بزرگ به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20031" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20030">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش شلیک موشک بالستیک از ایران
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20030" target="_blank">📅 00:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">تا آخر گوش کن</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20029" target="_blank">📅 00:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از دایرکت مشخصه امشب هیجان به اوج رسیده</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20028" target="_blank">📅 00:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مقام ارشد اسرائیلی به الجزیره : پاسخ گسترده آمریکا به ایران محتمل‌تر از فقط یک حمله تلافی‌جویانه است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20027" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ در مورد ایران:
من دوست دارم تعرفه‌هایی علیه ایران اعمال شود.
لیندسی این را می‌خواست.
خبرنگار: آیا می‌خواهید مجلس نمایندگان قبل از ۳۱ آگوست برای بررسی لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: راستش را بخواهید، نباید لازم باشد، اما اگر لازم باشد، دوست دارم ایران را به عنوان تعرفه اضافه کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20025" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=rrirbkm1BV3W5_ZzLMpdmKNP1CoeIywJb00vkHhQ6n4Ipd2EbAEH04n7Co4zzh8q1DMCQMGncezNj1H1S0jG5wDYkZ5FaPLa2k9UO0_SOz2FZcqxlUad_iWEiXN9cc-XlypkxU0UUKCWSttO4Br9cCkfetwx2II4-t5mW4uTNcFWIwMKioePU5T7-u95GD9z-ZaIkhKg9RW_BoDOkcXPPRhVcUual02SOu_R0X-Ojkti2Nyz6teb8ktw9s6rUd9R_jti-TtKVvzBHw9j1so5zb-WSfzQVGq7aT-hVbW9jHpEZraBIBQu-iqWK1Z5oYmjiX_Nxp25alWca48XjLKt2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=rrirbkm1BV3W5_ZzLMpdmKNP1CoeIywJb00vkHhQ6n4Ipd2EbAEH04n7Co4zzh8q1DMCQMGncezNj1H1S0jG5wDYkZ5FaPLa2k9UO0_SOz2FZcqxlUad_iWEiXN9cc-XlypkxU0UUKCWSttO4Br9cCkfetwx2II4-t5mW4uTNcFWIwMKioePU5T7-u95GD9z-ZaIkhKg9RW_BoDOkcXPPRhVcUual02SOu_R0X-Ojkti2Nyz6teb8ktw9s6rUd9R_jti-TtKVvzBHw9j1so5zb-WSfzQVGq7aT-hVbW9jHpEZraBIBQu-iqWK1Z5oYmjiX_Nxp25alWca48XjLKt2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد حملات ایران:
این گروه با گروهی که ما با آن سر و کار داریم متفاوت بود.
آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، ما باید کمی آنها را تنبیه کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20024" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=eaD2YdJy9OM6HhscBrh-3gVK0vXVb7TBeGYWyBO3MXVXqwoc-6JPGI_CtMC0n3GWCBmqmMQops6LXJKydn49rGEEh9hYOZ3zDnEkiW3NHkpJ2KXjAiJ29F5bNEFDJ3is84-n3MQ43xHl43ui02W_02lNN5RPCJ8odHzsX5oQmxXFrrBZAC3_5aj6OVzNQorZ30z1F9Z9uG6C62nK-ldRHq1MUkkxsZYANpHQsNZBBRoHwtIdngJRF1jp6iPjN_zMzM2AiBijmV6lFc5P3B8k1Eidq3QLC2zjciuAS5nyjggkQ_L5r8xF3ZcMx4oLaVeMKtY-l-fI-efo5EI2JTBFQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=eaD2YdJy9OM6HhscBrh-3gVK0vXVb7TBeGYWyBO3MXVXqwoc-6JPGI_CtMC0n3GWCBmqmMQops6LXJKydn49rGEEh9hYOZ3zDnEkiW3NHkpJ2KXjAiJ29F5bNEFDJ3is84-n3MQ43xHl43ui02W_02lNN5RPCJ8odHzsX5oQmxXFrrBZAC3_5aj6OVzNQorZ30z1F9Z9uG6C62nK-ldRHq1MUkkxsZYANpHQsNZBBRoHwtIdngJRF1jp6iPjN_zMzM2AiBijmV6lFc5P3B8k1Eidq3QLC2zjciuAS5nyjggkQ_L5r8xF3ZcMx4oLaVeMKtY-l-fI-efo5EI2JTBFQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: چه چیزی می‌توانید درباره حمله به نفتکش در مصر به ما بگویید؟ آیا این موضوع به ایران مربوط است؟
ترامپ: من در جریان قرار گرفته‌ام. این کمی بیشتر از همان چیزهای تکراری است.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20023" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=HMqfSfLOoNksNaqqjJoRD4BZWoh9q9jQgvHQbJRtD1hv8dL4GxvIK3B3IO4HwjEjHyNETeVUYOYYl_zZXLbWGg_57N3hDopC4UbFADIYpVY80Dpup9ahjBM9xhR6s2mbFPMeB_3am3f1G2cH503j6DMCCMtFh_gQRDWvYFa81j8jqDezqadx5tDOCmXHbe6UnlGHB3-e8ByTJu3_R47ET4KEr3VZ-j3Ooi8_1a4vJrpSLqbeW7S_f-9i9fmKWVMLMOa9-3DUrppKQwvXS0p4eksPp1P41-eU4G-y18rxVSBZ_6LesqSUYjs4gliz8IhHWmC_Ga9TSnwvuY3xUGG3WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=HMqfSfLOoNksNaqqjJoRD4BZWoh9q9jQgvHQbJRtD1hv8dL4GxvIK3B3IO4HwjEjHyNETeVUYOYYl_zZXLbWGg_57N3hDopC4UbFADIYpVY80Dpup9ahjBM9xhR6s2mbFPMeB_3am3f1G2cH503j6DMCCMtFh_gQRDWvYFa81j8jqDezqadx5tDOCmXHbe6UnlGHB3-e8ByTJu3_R47ET4KEr3VZ-j3Ooi8_1a4vJrpSLqbeW7S_f-9i9fmKWVMLMOa9-3DUrppKQwvXS0p4eksPp1P41-eU4G-y18rxVSBZ_6LesqSUYjs4gliz8IhHWmC_Ga9TSnwvuY3xUGG3WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:ما می‌خواهیم آن‌ها را بسیار سخت بزنیم زیرا نوبت ماست که آن‌ها را بزنیم.
آن‌ها می‌دانند که این در راه است. آن‌ها از ما می‌خواهند که این کار را نکنیم.
آن‌ها دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20022" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اکسیوس دربار دیدار ترامپ و نتانیاهو :
نتانیاهو در دیدار با ترامپ نسبت به احتمال دستیابی به توافق با ایران ابراز تردید کرد و گفت‌وگوی ۹۰ دقیقه‌ای دو طرف عمدتاً بر ایران متمرکز بود. به گفته یک مقام اسرائیلی، سه گزینه برای ادامه مسیر بررسی شد: دستیابی به توافق با ایران، ادامه محاصره دریایی و تشدید فشار اقتصادی، یا ازسرگیری و گسترش حملات نظامی. این مقام گفت ترامپ درباره پیامدهای جنگ بر بازار انرژی و اقتصاد جهانی ابراز نگرانی کرد، اما نتانیاهو تأکید داشت جمهوری اسلامی در تلاش است با استفاده از تنگه هرمز آمریکا را وادار به امتیازدهی کند و باید فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی افزایش یابد. او همچنین مدعی شد ایران با کمبود سوخت، صف‌های طولانی بنزین، کمبود گازوئیل و نارضایتی عمومی روبه‌رو است و حکومت از احتمال گسترش اعتراضات مردمی نگران است. این مقام اسرائیلی همچنین ادعا کرد که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری
و بسیار شدید خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20021" target="_blank">📅 22:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند. @WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20020" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20019" target="_blank">📅 21:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20018" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به گزارش واشنگتن تایمز، وزارت خزانه‌داری آمریکا اعلام کرد دو نهادی را که به گفته این وزارتخانه از سوی ایران برای کنترل تردد در تنگه هرمز مورد استفاده قرار می‌گیرند، تحریم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20017" target="_blank">📅 20:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">به گزارش وای نت عبری به نقل از یک منبع ارشد سیاسی، گفت‌وگوی میان بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و دونالد ترامپ، رئیس‌جمهور آمریکا، عمدتاً بر موضوع جمهوری اسلامی متمرکز بوده و به عنوان «یک رایزنی واقعی و تبادل نظر» توصیف شده است.
این منبع اعلام کرد که رئیس‌جمهور آمریکا با سه گزینه راهبردی روبه‌رو است:  دستیابی به یک توافق، ادامه محاصره دریایی، یا «از سرگیری و تشدید حملات». همچنین تأیید کرد که مجتبی خامنه‌ای، زنده است و افزود: با اطمینان این را می‌گویم
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20016" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارشات اولیه: صدای انفجارهای شدیدی در اردن شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20015" target="_blank">📅 20:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=S-M_jJ1un4mqrnxpW2q_MJgbPiqZ-_I4-ieGM30RTOyyAcPRf_9RCjv771M0Nly4Izspkti76WQaU9B1YC4oPiaGzyu6mFDqqdwwaq2RN2rkAFPlcIkBFCo7Z0GGdWqyeWLnOzMAna46f6x60WpPmWTDZkNwDTgT1VTv-ho1xrMkdcdEvA-NAYP8SnA6btvzssT4L2w_pBepBwFIDr-keJDPrwHXKu7nQaIYMl8mszX4rSE6K_dHM9hYiMn5cix6FqjM06xdrS3N2urpmWZm6Ufqraq5NTBMz1eBwVnQ_t6IWeUnLitFYkrETGbSjFDVMoAJ6o5g2U6yudGw7l8h9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=S-M_jJ1un4mqrnxpW2q_MJgbPiqZ-_I4-ieGM30RTOyyAcPRf_9RCjv771M0Nly4Izspkti76WQaU9B1YC4oPiaGzyu6mFDqqdwwaq2RN2rkAFPlcIkBFCo7Z0GGdWqyeWLnOzMAna46f6x60WpPmWTDZkNwDTgT1VTv-ho1xrMkdcdEvA-NAYP8SnA6btvzssT4L2w_pBepBwFIDr-keJDPrwHXKu7nQaIYMl8mszX4rSE6K_dHM9hYiMn5cix6FqjM06xdrS3N2urpmWZm6Ufqraq5NTBMz1eBwVnQ_t6IWeUnLitFYkrETGbSjFDVMoAJ6o5g2U6yudGw7l8h9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:من همین الان گفتگویی را با وزیر دفاع، پیت هگست، به پایان رساندم.
او چیز جالبی به من گفت. او به من گفت: "ما به جهان نگاه می‌کنیم، کشورهایی هستند که اراده جنگیدن در کنار ایالات متحده را دارند، اما فاقد توانایی هستند. و کشورهایی هستند که توانایی دارند، اما اراده ندارند."
او گفت: "فقط در اسرائیل است که هم اراده و هم توانایی را می‌بینیم."
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20014" target="_blank">📅 20:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الجزیره: شرکت امنیت دریایی امبری گفت که حداقل یک حمله پهپادی به یک تأسیسات ذخیره‌سازی گاز طبیعی مایع ایالات متحده در دمیاط، مصر اتفاق افتاد
تأسیسات ذخیره‌سازی شناور مورد هدف قرار گرفته متعلق به یک شرکت آمریکایی در دمیاط مصر است و توسط آن اداره می‌شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20013" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سنتکام : تنگه هرمز یک آبراه بین‌المللی است.  سپاه پاسداران انقلاب اسلامی هیچ اختیاری برای تعیین مسیرهای تردد برای جریان آزاد و باز ندارد. کشتی‌های تجاری همچنان از این تنگه با حمایت نظامی ایالات متحده استفاده می‌کنند.  از اوایل ماه مه، نیروهای سنتکام به عبور تقریباً ۱۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20012" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20011" target="_blank">📅 19:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=cLCGVQLNIMXRi99M0VacD0oc_tRQVm1RBiijIvFmvKBzebymPN9wnjsZZAkHrn-DDXLdVPMV8yoeUBFq78qmE3O5z_WfDMG2hDqx2XwP3PTMj050gJlJi-r9F1hi1bes_xtPyuZQwrKzMXZqkPC9lJtTLB-9Amj5PxCnje1GDtPV-lTUnL5AvwxNeapSHwI-doV0y5B-BV-0TNVA-8HsPfEdBsoD31lEHGmlFGOKBfxBiCJRA6zGe5qEzuvR0G-bB-W9yijhjIk5am3jPfTGOhWFNOevNLIRq9HKHsGEme9vmJSrj_yUPaRUs6DC8ack3nABRGZ8ptNuLX4w1g_MnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=cLCGVQLNIMXRi99M0VacD0oc_tRQVm1RBiijIvFmvKBzebymPN9wnjsZZAkHrn-DDXLdVPMV8yoeUBFq78qmE3O5z_WfDMG2hDqx2XwP3PTMj050gJlJi-r9F1hi1bes_xtPyuZQwrKzMXZqkPC9lJtTLB-9Amj5PxCnje1GDtPV-lTUnL5AvwxNeapSHwI-doV0y5B-BV-0TNVA-8HsPfEdBsoD31lEHGmlFGOKBfxBiCJRA6zGe5qEzuvR0G-bB-W9yijhjIk5am3jPfTGOhWFNOevNLIRq9HKHsGEme9vmJSrj_yUPaRUs6DC8ack3nABRGZ8ptNuLX4w1g_MnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، وزیر جنگ، در واشنگتن دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20010" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو : جمهوری اسلامی، فرایند غنی‌سازی اورانیوم را در کوه کلنگ اصفهان آغاز کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20009" target="_blank">📅 18:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=k7w6_A61h4cEQSs7VzOfkpaRbfu9wcolM4QMqDKanrE71E-TuMbxFFoR0Ws1a3I8461_ej7mahMD6cNtgLa2V0OcP1CSnLjLGDLdHx7u7faI00O1cNqXXFGw2yBtun89Ci7PYdXlTowbVQTbDtAnib38Vu_SZk7sTutfgetQCYIEIseId7JiVokC-5YlFrDkj50slfoXoyOF4LTXeEq-1YTtsKzTqw0WNtD4T4fp2K--tpCSS2lN98fZO9mI9p6-QlquazgeM8_ICbQIfoqrlKqUA-fVJ4eCg5oaI4bXe3uOmAg7rK9JkH0RAOo_6YajxJVXdYWM5VbQqRIqumr9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=k7w6_A61h4cEQSs7VzOfkpaRbfu9wcolM4QMqDKanrE71E-TuMbxFFoR0Ws1a3I8461_ej7mahMD6cNtgLa2V0OcP1CSnLjLGDLdHx7u7faI00O1cNqXXFGw2yBtun89Ci7PYdXlTowbVQTbDtAnib38Vu_SZk7sTutfgetQCYIEIseId7JiVokC-5YlFrDkj50slfoXoyOF4LTXeEq-1YTtsKzTqw0WNtD4T4fp2K--tpCSS2lN98fZO9mI9p6-QlquazgeM8_ICbQIfoqrlKqUA-fVJ4eCg5oaI4bXe3uOmAg7rK9JkH0RAOo_6YajxJVXdYWM5VbQqRIqumr9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20008" target="_blank">📅 18:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زلنسکی:از ترامپ درخواست کردم که یک «بسته اضطراری زمستانی»، شامل ۳۰۰ موشک رهگیر پاتریوت را در اختیار اوکراین قرار دهد
اگر مشکل کمبود این موشک‌ها برطرف نشود، حملات روسیه نیروگاه‌های برق ما را نابود و یک بحران انسانی ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20007" target="_blank">📅 18:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رسانه‌های حقوق بشری: اجرای حکم علیرضا سپاهی(فرد سوم در اصفهان)بعد از سکته قلبی متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20006" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پس از تهدید ترامپ علیه ایران: قیمت نفت هم اکنون به 90 دلار به ازای هر بشکه افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20005" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد نیروهای این کشور در جریان عملیات در روستای حداثا، واقع در منطقه حائل جنوب لبنان، تونلی به طول ۵۵ متر را کشف و نابود کردند که زیر یک کارخانه تولید مصالح ساختمانی و در نزدیکی یکی از مواضع نیروهای حافظ صلح سازمان ملل (یونیفل) در جنوب لبنان ساخته شده بود به گفته ارتش این تونل شامل سه اتاق بوده و حزب‌الله از آن به عنوان مرکز فرماندهی استفاده می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20004" target="_blank">📅 16:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20003" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
