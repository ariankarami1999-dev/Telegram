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
<img src="https://cdn4.telesco.pe/file/R-Gx3Mz_-1VjddNgHpdHQYlLi50S90lyzFtJoT9VcsHiidNeojEi7Kja1faHJacZt63hd-dLI-JnWxoG2Q9lTETruhOCxHMEKzyF7WpPHgpU9gQNbSy2FcxtsaYvRRc2xFyojbHkHZLZvJ25l92iYaPrVoBD981nMoYXhtDPmOLXkDX1DzZrbNV9iiK9sosTd5rv2VMSSOk1hkwOhvQdhRg_qE1qQBtKaLXmV0UKeWUeCqrNnVz348Nge5nco1Ait1EdAR4a_LtYvJ5mFyufSUfl8V5iwUIpSgE_BpKAtG3bHyV7Le6IggbrTHNLlKFBVB1XUdr3GBUBp86EMUhAfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 929K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-131122">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
در پی شکایت ایران‌ خودرو، تردد خودروهای پلاک منطقه آزاد انزلی در خارج از محدوده تعیین‌ شده، لغو شد
🔴
تفاهم‌نامه‌ای که به امضای ۵ استاندار رسیده بود، با یک شکایت و یک ابلاغیه، به تاریخ پیوست؛ حالا پلاک انزلی در جاده‌های همجوار، «خارج از محدوده» محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/alonews/131122" target="_blank">📅 20:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131121">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بر اساس اعلام رئیس کارگروه آرد و نان اتاق اصناف کلیه نانوایی‌های بربری و سنگک مناطق ۱ تا ۳ تهران آزادپز شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/131121" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=YGW9KX6xyNKhEzFL0XXf1cX8p3Ho9Zp_ezaMtSZ7WINEUWdovrLYpmEaJVIwARcG5xVVm9LCJ-sIWP9Tt_fvjpXk8OqmG_Obt65JyvLP3NFNHAhIp1eliEu7V7Jeuvqj8dPxbcq3D1KRoIqyIsq8UVB4RvG1NPTYi24d900F_j-CiSptzkQF455CHt8XeVdnUHemw6lz9Foq5JS9rtDotwt7DoOXoo_WuJ_T1Y60ZA0ty1U30RRGlZGqZnbIw6Nn9W4sc2IUQGlyEF1TVsm2vzC-ei1aO0CjtLxiOInYD8dEl9A0srLNkGR65EgMv3aTJO8lV2RaBnyGXX3WeVbdnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=YGW9KX6xyNKhEzFL0XXf1cX8p3Ho9Zp_ezaMtSZ7WINEUWdovrLYpmEaJVIwARcG5xVVm9LCJ-sIWP9Tt_fvjpXk8OqmG_Obt65JyvLP3NFNHAhIp1eliEu7V7Jeuvqj8dPxbcq3D1KRoIqyIsq8UVB4RvG1NPTYi24d900F_j-CiSptzkQF455CHt8XeVdnUHemw6lz9Foq5JS9rtDotwt7DoOXoo_WuJ_T1Y60ZA0ty1U30RRGlZGqZnbIw6Nn9W4sc2IUQGlyEF1TVsm2vzC-ei1aO0CjtLxiOInYD8dEl9A0srLNkGR65EgMv3aTJO8lV2RaBnyGXX3WeVbdnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحات سازی روسیه در منطقه ولگوگراد اصابت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131120" target="_blank">📅 20:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/131119" target="_blank">📅 20:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmQw_GrbywlTOnG-Td1QKhr1ha_qGnXZ4BgO-9h--jTFJH5vujl74r_q3khGpzd21kYZEPWPDjHrAV9CoV_KOYC0SkJ3iCPXOlVcImPKOuBs41s__W7bLETrudw1kWPOSvY0pJXxEQ9Pmoeihfuc2c1L6VpV6X6lucKSPx3ZfweGj8mQlDMJcU9F31vspyHzBEAXi9K1nOvYMiEfumshXSZPdKQHMriSMDTyhdMp7ct_EdrVNfly8M9TuOuVANH3u92e8RNAcALtJJ5dfHxEyBeg9oPVc20yaM3nKM41sB1F5Lt7dgxQgowVfbW_QtaS80IuvdFZNjBFhGxzj_Cmig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: دیوان عالی کشور حق تابعیت از طریق تولد را تأیید کرد که برای کشور ما بسیار بد است، اما ما می‌توانیم به راحتی آن را از طریق قانون‌گذاری در کنگره جبران کنیم، با حمایت رئیس‌جمهور که اکنون در این فرآیند تعیین شده است.
🔴
هیچ اصلاحیه طولانی و غیرقابل مدیریت در قانون اساسی لازم نیست! کنگره باید از امروز شروع به کار کند برای پایان دادن به حق تابعیت از طریق تولد که پرهزینه و ناعادلانه برای کشور ما است.
🔴
آن‌ها حمایت کامل و مطلق من را خواهند داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/131118" target="_blank">📅 20:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔴
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔴
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است.
🔴
‌ سخنگوی وزارت خارجه: تاکید داریم که توقف جنگ باید محقق شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131117" target="_blank">📅 20:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131116">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/131116" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131115">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtqw0jLcmRd3PF47eYbim4PAYhDhPdYKnx_kOTC1rKIROturMDwwPVOL6faqq9Uc2gG29Q37wBj8TIILwLgWRfvBy1KNoB1c4aWhT9fCmQTnoKYRjNzcn28j6qqu3sUu84RxcseM7S973G4_4eA5_m6NDNNZpQkWttRWBC7lDCdtU-t_CwRmtuyoV1prqC26Xr5GqXXWFdMo0QOOosQWagIVDbvR3FYEdsm-DXnRKAVWmP8HdsZvrQY3qvAG7cYjQGGH8y1j6Cds3DtQz8hVYnFq909GD7cWT8BW7dkEYw4gntEHuOAJoqTpWaUhYzkQ7aQtJimGGl4XB0n65YoIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131115" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/egsfGvL4grXNUxHSq9XAvmTjff-27MgtysKmrTwGlHYEhK5oIps9yACjIObr6ZONR_uBMIm3oE30iDj-Y5g7iSeY1PikC6528tp3BQoWt9lDbmXjbWEu4Vwn3PqLUKUTLjN8hSvTpYbhRKncYCzJdsnfE-xK2_oMYxN00QPFt0Ri73BxUfiAkWCDQSemy5QfLmF8VQRU7LopV-XgWYzS03M9cHQdhGoPw_yF7fjm-sV-Q16kd1XejO48lW5J1h5_i6M6ct7BKzEROwXdl0AljuY56nUHtEsn2qDZPtFQaOTC758tY8viPNgDItOgwYoCikiDzcgberDYQiBQpwdIlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BR_7Hii8lRzGp6fs_yZ2aNajOOXWeunB-gcB2nerznr_WgX07CY2BATFJpfV7SHVC-nM1UFBUaSGppFhPZIA7r8TE9Kcz8vONqEIesYIbwecfa2ZXd2y56GIMROjhv6gEnSJADYvhGnmzdlHVEEL_IosctffBVyNghv2y68FspP6FyE6y1Ex0sk5ni3y7GAEckBC8vLASpNIECzOxXOoSEn1DpjGwhoDNeu_20czCbDO_Vy_dR5lFXOx98MR-3Gbs8ct9PMvdw8Hq1PsDmnDHvnERgaqwV1Yld2s7XMY_f-1n3tIDexQD_mjQngsAcXs3PGt1pnSdTGfXvxPEboMrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان امروز پیش از ظهر در مجتمع ریاست جمهوری در آنکارا با رئیس سیاست خارجی اتحادیه اروپا کایا کالاس و هیئت همراهش دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131113" target="_blank">📅 19:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
بر اساس مصوبه شورای‌عالی بورس و اوراق بهادار و در اجرای تصمیم هیئت دولت درباره تعطیلات سه‌روزه ابتدای هفته آینده، بازار سرمایه ایران در روزهای ۱۳، ۱۴ و ۱۵ تیرماه فعالیتی نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131112" target="_blank">📅 19:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رئیس پارلمان عراق: پارلمان، دولت و وزارت خارجه عراق با هرگونه حمله از اراضی عراق به کشورهای همجوار مخالفت کرده‌اند.
🔴
عراق منافع مشترکی با آمریکا و ایران دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131111" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdKCY5EgPZqHZ0P1jjzr_izVZ4BUou2zmwmSKZUhh5Fn1iP_U09fcv9580Ivj-ipx7RkZdsU_5S_Tx7pcOM8dhBSz683gMbR2ieWi-I1wjTzjcBjLGdthOsUD592yaU40UDfgicKfSc2JrxquhqchpkSKAKnUSQ7UoS45uR14NCWsh2gQ5aGQKo4TgXbku3Hy0aruVHEPMbLQUlqx_5gMVTXbQ9c4o_Xh2vyBZtETJp0CpMHlv_S-qwm35HVZZ6xXcEc7bnq0TCX2QAd9Y11xaaOzxGhFvSzvvf0HVGid-yCLsUMudnnqmX7dZfRuzABptE0QE1xDTzNSshNbyncPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، جرد کوشنر و استیو ویتکاف در چارچوب مذاکرات جاری میان ایران و آمریکا وارد دوحه شده‌اند. با این حال، قرار است دیدارها به‌صورت غیرمستقیم برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131110" target="_blank">📅 19:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=CZ20-7JzBepBTJOxCQQ65uBLoWFrFS8u8VPlmsmekgCjN80zApMm1cNi0hb_qqD3evmhODqJTb1lywH-dimIKl1PbBEF-9PDijG7cc32I6fLRmnjzeMS2FYyKK9zrwIkaIw8FTL4brKrxXAh1IkJnk_3Yi1I6p_X72MMSVui2foJyvXaAqsFJRHtdeRHJ02k-J7GO4uK5zQ8AV2ebGNy8i9auA91tdmKM5InNgrm2RSWfOz35eYmHJqA59g6lsxUkEYwkKUufy_AWkqVbsGOMkUVH40fo1rvp7zOSIAyFLJua-sSMjQGG5qjzpF_-ZU4f2tdqM42EhJzYwP3IkNtOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e31aae45.mp4?token=CZ20-7JzBepBTJOxCQQ65uBLoWFrFS8u8VPlmsmekgCjN80zApMm1cNi0hb_qqD3evmhODqJTb1lywH-dimIKl1PbBEF-9PDijG7cc32I6fLRmnjzeMS2FYyKK9zrwIkaIw8FTL4brKrxXAh1IkJnk_3Yi1I6p_X72MMSVui2foJyvXaAqsFJRHtdeRHJ02k-J7GO4uK5zQ8AV2ebGNy8i9auA91tdmKM5InNgrm2RSWfOz35eYmHJqA59g6lsxUkEYwkKUufy_AWkqVbsGOMkUVH40fo1rvp7zOSIAyFLJua-sSMjQGG5qjzpF_-ZU4f2tdqM42EhJzYwP3IkNtOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات حق استاد محمود سریع‌القلم، مشاور سابق روحانی:دوستان هر کشوری باعث توسعه یا عدم توسعه می‌شوند.
🔴
مثلا اردوغان با ایلان ماسک و بیل گیتس معاشرت میکنه ولی ایران با حوثی‌ها و حشد الشعبی.
🔴
اینکه ما با کی معاشرت می‌کنیم، نشان دهنده سطح فکر ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131109" target="_blank">📅 19:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131106">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhfnwumjoWkckZCNrXtDxik893lz2opYjPuCfBIS-RGZFu1erW3TjlEmoBuruX0btTTeiNfa0iBnTGvm0gVIaUhO_iUZS4cN7C80uhxuNR0Px1KDXu-oPrbHUlVwH518COqzMXSMOFoZp-Kj6J5AGA1FGap77e1xRRhZevnePTDG6nC-RUYQEGPobvqZya3Kbi4hIYYkkY4tY2_UB0fdylQoMq5L9GUFtII1N99NylmaeMMbHYSqblhHszu3BqopaF445bztDjeSs86yQBv1UQgWPglUQGV5dCJ17ViDnmW6ZuUSmWZENidw3DJAxL_2We_NDStZyNrcvRv5cGFtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UEtCpFIu5ID1m2sENckPEnnh4rqQzxjU84H9_28QEMcrY3EQiyrNt_yyto9gUA268vgc-baXVfTlT330OwhsL0HZvZIur5bY8d4VVbTY08NXyB3GaxAme1t8vZPmUD4XfjJwSq0l8unwIJ_v29M7ZfGZFSPaGnG87FZoxPZ6I3L7A6BsYFFGWUtWfYbTaWaQg1gKoEfzaDsiOEEe_EBTBVZGvqWoH5kjeH5GSEUc7CJTaTGicMNM8eadD2crfjwgQ3lAHQCaXCSv5CTeKYsIKZLu63sVpBmRbHk95m8dCXM3Z2etMdz8eF7QXIAiScVenjxbe8IGaN3hzXprw6tbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jEcfFh2PP_ygbrCESG_DhAUTSy3Y7LAB_C5wPR11WKTsbxADKYR7Q77fl7F7WH2cBH0K3uOekpH511r1-uqpjQJCFuC6BGEj-Cru8A4DREbdoFIAcQILWFFYrsMYnyUQ-2sj3T638nJrVGkJXvuxCozZ7XfyIrunh-kkVkoGZA1nU7JgY1bEj4mRadPiy_mkL9hK8LZpxH9aMeXF1KkXoOe03hFIS5M1mKxftdZuLQ2MZFYnA1mRwz2Nr4scg1t_khvBihA4g5J8w069XEaiQjoPchbLEz_jft9LK-UIawXMsknuXjiuVyAaf2E0cD6796xe--VC48CXcb9YY2bEZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سنتکام عکس‌هایی از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/131106" target="_blank">📅 19:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bsbiLntHcFs1r_vLdhGe-1auKQrrLvvMAEvqj9sXSpd8DmIlFfry9B0rDTjny3CW-fkbXXwNvm4m423EFI6wS2XGuLhKsgJ4Sy-gSeCKcLEEa-KBA_UqyHwHcmuyq0zGyfKQXkSYIv2XiFUrxouORGkG-xDbFawqFJ08Kl1Bn3DxPzDynOs7F5GW_kgHqSrrBOq8RYcsM1-iZz9qQvq_eFbVs1DL1sazbNZU9jyRQt50mY0dN0cmirqix2HC4dxaYQGj1UDq6aMFbxlpeIrn7F9QpmiWrSJ0hbq6sdN9gqiNirIoFKai0BH7XmEgCdgUXa71Sh3LF6-dRSwD73IkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5UPjRpEm9EhvFEgqE_nBsifidbneXpAaWsc09YnFovYZa3UJjeqW2EnKP6mufbt_peKo4iP3MGpg1vRsJ88jnJPvgqNkSUgVNsJob_1g1XbavVimIqoiFJB_cgrgQAf1sOlKQWYVQnMQson1vXss0T7ILq7nmQoJPBLTtUHQio8cQOiEf40z8GhHFlD9lZdhNLiTYygn_Ar2fsvGAgQ63c2O1XVm7IvDjs38DOTq9nYh4eEyNqRm_FzhYf_xTcfvvrwSIQ_kaapIPZeE_-gF27X9WoewogPzmR1TpxIM962tNvjU2NZemlOMw9JjsAMBju4pRZSti7KWP07LCk8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnG99bJ0NfV1lRdqeUOgWN8I-CxPYgkwdKPvfBdsXw95KtzjPOddaK2e80wK4_xBWpVOPKzu9vThU2UzqDmbog7YUoK0Wedr3Q6hMCwZbJxmdYA-kkhn_fMsHAp_AV8TjY4Wa1RueA9acnXMqNYzSSWgv1QeEtav05NQzoBKXiIU4DkyR2dd0SvpXRBgmJLJEZjn7cgp78BKujDvpzoYWY28bCTWLCu0U00vvPx7mxv0UfoAij-Kn4R5t0iL6d2yy-0j8bDvU-Ng23whxejNZf1AdkCzQShEBcXCDUzJv84HE8V_7MuFgLTt123uk_0-fSTvO2SUOwzopHlgCQ0nxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیروهای امنیتی عراق همچنان به منازل نمایندگان عراقی میریزن و کیلو کیلو پول از خونه‌ها درمیاران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/131103" target="_blank">📅 19:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131102">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e16fea3ee.mp4?token=mkt12uzz4rX7AX52utdoOSCDq2zeqCgzi136Azvacx41WhPtuaZjngtBwj8A3ereowmsPMiZOTeensScWzyVZkzRL3IrkjrfGcVitZmF0XJmDtxucbRkaNhaVsfsjOHtus-JFknEuZ8q8faqwi0X5AJDaBZ6oGvZenF5_lxV5B-eH-QLUMG_rUsa1VWLKUp98VI20nJFG-vIrNfWmco7ugp3dpsVFcjQWtMW2i-wK93YXPR1XDG_ui0Kxj1XEhEj8x89-uPyY5p0g8Z5tdkFh3UIxxey3n-IpLHWgWcMwH_1IWCY6c5Ii09ev59n5QDPtRBjv3qWENCnPqkN9th2Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e16fea3ee.mp4?token=mkt12uzz4rX7AX52utdoOSCDq2zeqCgzi136Azvacx41WhPtuaZjngtBwj8A3ereowmsPMiZOTeensScWzyVZkzRL3IrkjrfGcVitZmF0XJmDtxucbRkaNhaVsfsjOHtus-JFknEuZ8q8faqwi0X5AJDaBZ6oGvZenF5_lxV5B-eH-QLUMG_rUsa1VWLKUp98VI20nJFG-vIrNfWmco7ugp3dpsVFcjQWtMW2i-wK93YXPR1XDG_ui0Kxj1XEhEj8x89-uPyY5p0g8Z5tdkFh3UIxxey3n-IpLHWgWcMwH_1IWCY6c5Ii09ev59n5QDPtRBjv3qWENCnPqkN9th2Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهد که شهر مجدل زون در جنوب لبنان در اثر اقدامات ارتش اسرائیل تقریبا به طور کامل ویران شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/131102" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131101">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7XV7lcY1y67kI_Mm4A4wcA5525Ujf2av0Jz4AGKh0wOzRo0Yrzqd1THGse1xhR1RbRx6LCJmGFXcXYGfcLCrxDEfTvJ3L5pzSp3mLifbO-wCuwwwWvI1xG_LmMzJGrilqW_9_hJOCIauFzPgGBxI0gzESZFJLLFyCSTziSFq4X_WPuY5FqytuVRIj-Jy_Bq8puKVyHGbQpDUzmLv3lXkFcbfAhAhmUxNXWjzYVUDM9m7y1oHTfcWQwadcX82v97kZAh_01q-MBHU-2R4T6S4zsteSX_Gwpr1yaAhOr5vZt8FW49-D2Lf4L_OBT3rnewpMJXF6goMQlKTMl2CXKErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل و شین بت اعلام کردند که حمله‌ای اسرائیلی در غزه دیروز محمد فتحی عبدالحی ابو فخر، فرمانده گردان یابنا در تیپ رفح حماس را کشت.
🔴
طبق اعلام نظامی، ابو فخر اخیراً در حال جذب نیروهای جدید و تلاش برای بازسازی توانایی‌های گردان برای حمله به نیروهای اسرائیلی بود.
🔴
ارتش اسرائیل همچنین گفت که او فرمانده‌ای باتجربه در حماس بود که دو دهه به عنوان چهره کلیدی در شبکه قاچاق سلاح گروه فعالیت داشت و بر تلاش‌ها برای وارد کردن سلاح به نوار غزه نظارت می‌کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131101" target="_blank">📅 19:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا: موسسات مالی وابسته به حزب الله از جمله بنیاد القرض الحسن و مقامات ارشد آن را  به لیست تروریستی افزوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131100" target="_blank">📅 19:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131099">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab2996fef.mp4?token=ILSrXVX5-2qFVKNnHecJUho-6aKny_PrMv5DYUmLlVhuxOhDw3tUYNOcX0h2AJ2_0dk_j-5G5Dz7zeVXHMaMa8TZAwRksCmgdPCEjhFrW_XXCcrqqhQXKzUTB0IuCjvj5fUh0DNsF4GSyk10Q1OofQUb-Lyh2PFfA4tEf8VEZRCq9gmCdXDnrDVKQEB_jVZIMbQ7iYlYWw7AfPz7Z8-2gyt4Er4NDtepAbxxA6OeQC-3HgE8u_IzPj0JrxEj2q4Rzn3aDtCpzIiK8ddRAbT30QuK2Gqcu6Bk8BsFLf91cd2ohlxubfbI7bjcyaYxXZYzNgikAjkv-B7ircbmfHE5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab2996fef.mp4?token=ILSrXVX5-2qFVKNnHecJUho-6aKny_PrMv5DYUmLlVhuxOhDw3tUYNOcX0h2AJ2_0dk_j-5G5Dz7zeVXHMaMa8TZAwRksCmgdPCEjhFrW_XXCcrqqhQXKzUTB0IuCjvj5fUh0DNsF4GSyk10Q1OofQUb-Lyh2PFfA4tEf8VEZRCq9gmCdXDnrDVKQEB_jVZIMbQ7iYlYWw7AfPz7Z8-2gyt4Er4NDtepAbxxA6OeQC-3HgE8u_IzPj0JrxEj2q4Rzn3aDtCpzIiK8ddRAbT30QuK2Gqcu6Bk8BsFLf91cd2ohlxubfbI7bjcyaYxXZYzNgikAjkv-B7ircbmfHE5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اصابت 6 بمب FAB-250 و FAB-500 شلیک شده توسط جنگنده‌های روسی به سمت مواضع ارتش اوکراین در جبهه خارکف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/131099" target="_blank">📅 19:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131098">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر امور خارجه عراق: ما مخالف گسترش جنگ هستیم و هدف قرار دادن کشورهای خلیج فارس را رد می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/131098" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
نتانیاهو: لبنان اسرائیل را به رسمیت میشناسد و اسرائیل نیز لبنان را به رسمیت میشناسد، به ایران و حزب‌الله میگوییم از اینجا خارج شوید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131097" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131096">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzCC9uqf_c7xOu2ZeC6BO1DFy33B9tQIf-HNM92MtIY1emIT5kaBR2xeNAUCW1uR2cOw5pJzt9ZM8lP4wdwS0w4Ltg2gkoro2a1QcGbiSHSCkA1QXyn8g5mM4fBh8K4MzlQ89bkiA3vRTML8rWbF-8jjiSVAiHL1LcCCsaGWtdUy6NwXalL4sVxB-tdjH6DbmXV4VAdfHmmwWxy7vJ55qg5g3L3C6lsZLxDRlsvfQUG4BY3yYBNDs1mRIdvkwxU2TZYOPHjvsHVYKva6cBMPLCZDkKaPfvxmV1rA-fn2TNrAw51xMIdtYPwIo4rQRpgn9gXjTDQa-uliPxp0b12Tmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق تروث سوشال: دیوان عالی کشور همین حالا محدودیت‌های هزینه‌های سیاسی را برداشت! یک پیروزی بزرگ برای جمهوری‌خواهان و، مهم‌تر از آن، برای متمم اول قانون اساسی!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131096" target="_blank">📅 19:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW1kOhMlkpy1WZoMBdSN6RWlB6WFcf4xtttYVcMUL8rgw31EkFvv9JuU8rCnJk7Zx3XZdv59XPlX71Xm0tQRmOr979_OdbOLiamask6xP7GLySFbAvdsOtwdpD-TPvyx4RvXy7LP6B8GSoockPc3Ccx67SAnN4onyJThGBaQrhY_RB6FoYg87w7-pENj3rwY6499D107LMjzzUP4MbBwUMsuaF3ZrcM3qh4_fTi-0_pSRXFfkrMIMRxCcpTSGt6f-j-ctzRsfjej6TN6kKRZlwFgJpCtn-WhGrQZzpweSEFLDu3dPjkq30AYCT8jp7w0mSxZgrx654ymVVXFyvp-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عالی ایالات متحده حکم داده است که ایالت‌ها اکنون می‌توانند از حضور دختران و زنان ترنس‌جندر در ورزش‌های زنان جلوگیری کنند و احکام دادگاه‌های پایین‌تر را در موارد ایالت‌های آیداهو و وست ویرجینیا نقض می‌کند
🔴
انتظار می‌رود این تصمیم بر قوانین مشابه در حداقل ۲۵ ایالت دیگر تأثیر بگذارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131095" target="_blank">📅 18:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5XphorDXzBYVtXVzMtqWytEF-8bB0z_XcC8smJoTggPmvCsiSfvS8hDINZjNHA7STWMrtQ6xA1Vundp19ojbusQbTosrf3yxm3LittcYArgfRDR8IhnQM-vnEpUruMOYS24mbGoINATB45i9QLVx7btP6LDQFnu0zE2mP1fRGkrHyOKNG-Lc8sSPZR5KjCALb_0QkmkMN0Pibyuck8ByA35JgLxqqVInQ5J96zpAaxIaYz4Gd7CahKlFI6Sze7DLtOqun3uo-uO5rpXFU4lmL0zR1OTuuXIBBszOVyamSCKusrYZd1QkIuqP6dB4hmSt2nIXCVM3KmkD4i7udGvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیو: تفاهم‌نامه با ایران فقط یک تکه کاغذ است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131094" target="_blank">📅 18:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131093">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81d0469c5f.mp4?token=cDxaTQUfDTs0doTvaPw2JyyA4iQeLcKbQbXDqghUpOuvbgtLGd4cjV5xQOlSwrZ_zsE9_p9cXIYsawHp8EVMcRWV5eshTAekZnqRt8fj3ceTgyVyw9y-6lhJkI1bqZeAg3D_Q__ix9Ai1u3CMPOx0AOqA02SC5gm8aPXhorC8xEBRVHsal88wiCiNFs5BitCO2w9zFWTTJSd-98WKWb-azUtRX-MuZXplakfjXxbzi8KaE8ZXOWM20gTCj3WgOEAlsofwgjZD-r7fAzb6uqmnoDpQ-sJdCV02FJlUJGEEdBDwSQ1tIG6UqVqYR7jX-XQ49dE4tr378djcy9ksz6XE0fZU4GQSHnPBiSuelnEZFU6Vv8P2uROiZyNxNOcr8SzAv8eCSMymwYByVUIVTa25qqDB8SjkeTtbzZ3extNqJhEof4-03uBIltNdwWnnqLc9R_Y5G7jHk5ZHYaa3ntcTs5spjFBpvQws3GjkT8lvTd1S2Xyh1A_8N0Qvbd8IF01jit61FTfII3qhGDFQ_qQ888zfxHGv09lWHcAg-4H_sOCQYL3k6RhwVm48T0HuRzttf9szIl5rEVq-jn31fdxGBnNKPsauuqZHDahyWFRapnFZkGYMNqFvHVoTfzXVECHYDf61avF1CQBl-AC3hbH3lGO0PAcuw0n_HmxVAb1Z2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81d0469c5f.mp4?token=cDxaTQUfDTs0doTvaPw2JyyA4iQeLcKbQbXDqghUpOuvbgtLGd4cjV5xQOlSwrZ_zsE9_p9cXIYsawHp8EVMcRWV5eshTAekZnqRt8fj3ceTgyVyw9y-6lhJkI1bqZeAg3D_Q__ix9Ai1u3CMPOx0AOqA02SC5gm8aPXhorC8xEBRVHsal88wiCiNFs5BitCO2w9zFWTTJSd-98WKWb-azUtRX-MuZXplakfjXxbzi8KaE8ZXOWM20gTCj3WgOEAlsofwgjZD-r7fAzb6uqmnoDpQ-sJdCV02FJlUJGEEdBDwSQ1tIG6UqVqYR7jX-XQ49dE4tr378djcy9ksz6XE0fZU4GQSHnPBiSuelnEZFU6Vv8P2uROiZyNxNOcr8SzAv8eCSMymwYByVUIVTa25qqDB8SjkeTtbzZ3extNqJhEof4-03uBIltNdwWnnqLc9R_Y5G7jHk5ZHYaa3ntcTs5spjFBpvQws3GjkT8lvTd1S2Xyh1A_8N0Qvbd8IF01jit61FTfII3qhGDFQ_qQ888zfxHGv09lWHcAg-4H_sOCQYL3k6RhwVm48T0HuRzttf9szIl5rEVq-jn31fdxGBnNKPsauuqZHDahyWFRapnFZkGYMNqFvHVoTfzXVECHYDf61avF1CQBl-AC3hbH3lGO0PAcuw0n_HmxVAb1Z2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو تو منطقه‌ی حائل لبنان : تا وقتی حزب‌الله اینجاست و ما رو تهدید می‌کنه
🔴
نیروهای ما هم اونجا می‌مونن، به نیروها هم گفتیم هر تهدیدی دیدید، همون لحظه اقدام کنید
🔴
به کاری که با شجاعت انجام دادید افتخار می‌کنیم و بهتون خیلی افتخار داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131093" target="_blank">📅 18:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131092">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
امارات ممنوعیت سفر شهروندانش به لبنان را لغو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/131092" target="_blank">📅 18:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131091">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=fmuhda9nlGoAqKAt3f8_utKj-6RmZuoTaPx-_Cq6EZybAD86lu4d2Km5v4x_BSsxGDwhTurMt29dpwaNnVzR6CC5OvjY6_4mhI-Xq84mmvVIOS9yXQNaBKl-6neMOhdEto6voeQHO_aTZRL78Hbavo7K5ZYbRrl9QQ9gduAuBPdf4M95wBMPKkwcOXPUCBJQ9dxOPt2D5zQK_Mobi96_Wup7lwOUge4jpIs3Q925U-RaV9gBDg7v6UPNfbDoj5EyYBAB9wh0CjCdpdEpIdu6gFclBh4kt6lO43xlVJiZRC9bu-6_YGfFU3XX98yMxyfa8r0BzZ0Yf-7N8oKsdo42Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d5133c623.mp4?token=fmuhda9nlGoAqKAt3f8_utKj-6RmZuoTaPx-_Cq6EZybAD86lu4d2Km5v4x_BSsxGDwhTurMt29dpwaNnVzR6CC5OvjY6_4mhI-Xq84mmvVIOS9yXQNaBKl-6neMOhdEto6voeQHO_aTZRL78Hbavo7K5ZYbRrl9QQ9gduAuBPdf4M95wBMPKkwcOXPUCBJQ9dxOPt2D5zQK_Mobi96_Wup7lwOUge4jpIs3Q925U-RaV9gBDg7v6UPNfbDoj5EyYBAB9wh0CjCdpdEpIdu6gFclBh4kt6lO43xlVJiZRC9bu-6_YGfFU3XX98yMxyfa8r0BzZ0Yf-7N8oKsdo42Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در شهر حیفا با صدای انفجاری بسیار قدرتمند منفجر شد که موج آن در سراسر منطقه «کریوت» احساس گردید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131091" target="_blank">📅 18:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131090">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVfZVvXm9Pgu_5nVkVCzyrPrh-KEpPt0tz2-octraEU_eD0ybhl9SxKVQ3pmHhjhphgXjgZZsdtgJHO0q5m69QC2hR0HTHXk0Id5hr9wWZlujXjUmXQ8TvvHPHawjH9C4BEaowOMJ4hlo1L9zRFk19uhN7A2puczgmlSObXmt9YFWjnVVyHGjqji2j15OoCl3FdNYK4oSsCb1J83eydl5wF_UlJw7D7fPfFybs2wUeJuusD1zr-PgfkDpTnQCpXSQ_gu1ySv9zYPkuterNYTTXZ6QsCP516owJYpPz0ntb5yZDpRUbxqX1Wi6FQCcOSnEhNDnjQKLlkdtxjvpSYNpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ در تروث سوشال:
"پیروزی بزرگ: دیوان عالی ایالات متحده همین حالا علیه حضور مردان در ورزش زنان رای داد و این رای، آن وضعیت مضحک را کلاً منتفی میکند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131090" target="_blank">📅 18:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131089">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نیویورک‌تایمز: ایران و عمان، علی‌رغم مخالفت آمریکا، در حال پیشبرد طرحی برای وضع کارمزد خدماتی برای کشتی‌های عبوری از تنگه هرمز هستند
🔴
عمان این طرح را رسماً به واشنگتن و سایر متحدان غربی ارائه کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131089" target="_blank">📅 18:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131088">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=oI7XWnYNUEEC6wu2yrxK61SVIVUMg_g-43OrjTMLNgNpXpqX792QLsa3mxbpfjF_dP1mgDKTn7e-k9zuBOX7k1xevrV1uRXjWQoab-zqWo2AreBsuwAgjMJCxdIQCFqthJjCZN7Or97uwhU8wOcN7UE3gBhJa7G2SSapwP2W6Q6FSgjSYXgavSZ2COECJVZsPPxhl87FyOD_9g-lawS6ksrzRHjgDVQ7_LZKVZJCGz0Wo2TBfZDiSvgG2WsrnaST6fOyd_78QN892bacJwv43HjCwIfMYKBaSElUcH8-Wai68DHy13OpmW7lMljN5ekCNVom_VEQQG8ecfRHap2ed4eyBA8ub1RkRHhdXTzZWB_Ldbnk1Kkhp6rd_rLpF9MLQQqd7HY6_1HpSiGhngHfZAPrTNyf1hsjQ_8az66-lRc1oPeDQdLEByMz-QBMIOCWzSH3oTtpMSRa13wWd6ElZMSjTER-vEGhhEGzM_B9KkwraFFRmgGUiN_rN-K5kVJvJ53WDh2JrfBZ4l79dX7yC_rj9ribgoIg3kin5_WreV7EOW80-Ry9NWh_DhqDO1vSIR8KGnmOY5ZiRpmPU3uKDBq3v8J0v4NFnZp_Z0bjPdkXTXZl8zET8rlPb4PdxZGFqt2L4YKBFuEhwSw7HL55CA5vi7yBJ5Rl-UQ6oRFOBWM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f02b732e9.mp4?token=oI7XWnYNUEEC6wu2yrxK61SVIVUMg_g-43OrjTMLNgNpXpqX792QLsa3mxbpfjF_dP1mgDKTn7e-k9zuBOX7k1xevrV1uRXjWQoab-zqWo2AreBsuwAgjMJCxdIQCFqthJjCZN7Or97uwhU8wOcN7UE3gBhJa7G2SSapwP2W6Q6FSgjSYXgavSZ2COECJVZsPPxhl87FyOD_9g-lawS6ksrzRHjgDVQ7_LZKVZJCGz0Wo2TBfZDiSvgG2WsrnaST6fOyd_78QN892bacJwv43HjCwIfMYKBaSElUcH8-Wai68DHy13OpmW7lMljN5ekCNVom_VEQQG8ecfRHap2ed4eyBA8ub1RkRHhdXTzZWB_Ldbnk1Kkhp6rd_rLpF9MLQQqd7HY6_1HpSiGhngHfZAPrTNyf1hsjQ_8az66-lRc1oPeDQdLEByMz-QBMIOCWzSH3oTtpMSRa13wWd6ElZMSjTER-vEGhhEGzM_B9KkwraFFRmgGUiN_rN-K5kVJvJ53WDh2JrfBZ4l79dX7yC_rj9ribgoIg3kin5_WreV7EOW80-Ry9NWh_DhqDO1vSIR8KGnmOY5ZiRpmPU3uKDBq3v8J0v4NFnZp_Z0bjPdkXTXZl8zET8rlPb4PdxZGFqt2L4YKBFuEhwSw7HL55CA5vi7yBJ5Rl-UQ6oRFOBWM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوباما در مورد ایران
:
ما تمایل داریم فراموش کنیم که هر جنگی - بار آن بر دوش مردم عادی است، مردمی که فقط سعی در زندگی کردن و مراقبت از خانواده‌هایشان دارند.
و بنابراین اگر بتوانیم از جنگیدن در منطقه جلوگیری کنیم، این برای مردمی که آنجا زندگی می‌کنند خوب است.
اگر تنگه هرمز دوباره باز شود، امیدوارم که به مرور زمان این موضوع به مردم عادی کمی تسکین از قیمت‌های بالای بنزین و قیمت‌های انرژی بدهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131088" target="_blank">📅 18:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131087">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=c_HZfUP0zJqKU1s35bMg0JTNA7D83Ek7O0hmrQhqSTOQRdy9YI-Z1hafABnQffeIomtSUAxYUcthz_2Fc8ElQbduOVegrhpiYA617jex1Oc6xStob9g8F3qsG5c6w1iOLexnyzKo5pCtyyLoRFgR1IrMA6MfnRZyM7HuxTylH-en4AHwPOHR7mSp8I6n-hue7uAQAxhXeYBbL1IkjWY3ubjfUBkMyMFfahvJyBwLR_7vPUtQvF6088d4zx09xR2QhTSZ2aF1aG1qFReu5PUZ7TATG_0Mhzi0hgHTbZl441CXVENgT20kv7_9jw1V8FVONkRkBS4Vek2zamoQiHzf-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18bdf673ab.mp4?token=c_HZfUP0zJqKU1s35bMg0JTNA7D83Ek7O0hmrQhqSTOQRdy9YI-Z1hafABnQffeIomtSUAxYUcthz_2Fc8ElQbduOVegrhpiYA617jex1Oc6xStob9g8F3qsG5c6w1iOLexnyzKo5pCtyyLoRFgR1IrMA6MfnRZyM7HuxTylH-en4AHwPOHR7mSp8I6n-hue7uAQAxhXeYBbL1IkjWY3ubjfUBkMyMFfahvJyBwLR_7vPUtQvF6088d4zx09xR2QhTSZ2aF1aG1qFReu5PUZ7TATG_0Mhzi0hgHTbZl441CXVENgT20kv7_9jw1V8FVONkRkBS4Vek2zamoQiHzf-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
در طول درگیری ایران، اقتصاد آمریکا به پیشرفت خود ادامه داد. اقتصاد بسیار قوی بوده است.
ما حدود ۱۷۰٬۰۰۰ شغل در ماه ایجاد کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131087" target="_blank">📅 18:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131086">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=J3P6kk8eTZOwyLMKO51YgLxrV6Oq-TOWdSWepwyBASIGMl5UWohvelqwcb0Lr17QlgQStGEE-Ox0IElqP-af3NTf-j5GRlid99WYit6xfc0IL8PeBchhWRO6_ANk8pO0g45yesMQCY1M7dCU6WdailVJkpHg8Wp947Z88UzMiUt0ut4bJ10ZZeaxetX5YZm2RyFsc5_FXq5Eu1phE3PMaPfdvnJxXtVsGHvI2-kxBZIa0yR9v166NbsFuQzDgCcmjSnzAZzUsQkom_RcEakiad7xAnXHMGNeJdb10OFDCSwvKhzgy6X8VF_49JxpLHACtrM8xhDV9FgXa5cj791Ofg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44dac01f78.mp4?token=J3P6kk8eTZOwyLMKO51YgLxrV6Oq-TOWdSWepwyBASIGMl5UWohvelqwcb0Lr17QlgQStGEE-Ox0IElqP-af3NTf-j5GRlid99WYit6xfc0IL8PeBchhWRO6_ANk8pO0g45yesMQCY1M7dCU6WdailVJkpHg8Wp947Z88UzMiUt0ut4bJ10ZZeaxetX5YZm2RyFsc5_FXq5Eu1phE3PMaPfdvnJxXtVsGHvI2-kxBZIa0yR9v166NbsFuQzDgCcmjSnzAZzUsQkom_RcEakiad7xAnXHMGNeJdb10OFDCSwvKhzgy6X8VF_49JxpLHACtrM8xhDV9FgXa5cj791Ofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی:باید طی روزهای آینده روند جاری را ارزیابی بکنیم و بر اساس آن تصمیم بگیریم که به چه شکلی و در چه زمانی مذاکره برای توافق نهایی را شروع بکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131086" target="_blank">📅 17:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131085">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
العربیه: ایران تا پایان هفته 3 میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131085" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131084">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi2HnI7MxQke_uFNlYZjO2e1LTO9_b46QdZUZ_cUjwixbG8lbRPsWk3eto1bRIgB64rGVxBo9FCE9ZBEAE71Tq4THnS2FH-9XmUkwGR0f8pdx42LUqQI7WI88yyv54yZIkgupPRWCpj1iSeUF5CokPqjlRDJhTwpVYHjVaT36BVmN64ll7BXqox11i-M47vIC2jUkB73af8F02J4GIjVYPWrUf8KJNM02ct3NHWBlwT7ilZa4rQ7MctTTIk5FJrMbdlBRIPuWJgIb3w3RYKstTRRKMSV25EWaDGqjM0-dm9hsC-daLIe0NZg3y7lSAjHx2dYd8G7h9Y1xoGfTM5qFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: مجلس رو باز کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131084" target="_blank">📅 17:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131083">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-3ZW_8LdSzYqvnxUO3tETLph09Z7dfeywzFof9C0sHaQTQtnZrIHXZxO4GLI8SJBcGR6L_0HFXZYCNRcumWV5ripdDlyUkv3JsDqPh5uuHSH_6sqt2LYtJoBMRVXVDAdVUwTSZY7AX2vlPKdrHIp1QptEHwBfcRbxZVu3Dh12muikYQLfBi361mYYYF2RsiNZ4hBt9iRfHGgqKvaheR6xnhv27-LB8-Ps94Rzd4T4tYyH9YBeV9mb90Ls2ZAr2ixH2bBh43oP3xczv0437C41hv9PBxvgsIlQtxlyYZBp_CclJOl_zOo2MKrc3PtQQ9d9X3ACZmACdm-ID2lU9oEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: با وجود معافیت تحریمی کشوری جز چین نفت ایران را نمی خرد و از بازگشت تحریم های ما می ترسند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131083" target="_blank">📅 17:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131082">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6KdplXqAbvKIMC2qvcrITUkt1wNk4cqbqv176AJl9B1R_fkfuSvhe-ubBOXjgDaZOmK72S6U7fRIZIxQFzBMxYemxCVaxbZRm8-akXfmkO7M838h939pFR_SBvKJJmRkSowNNtsLaS43Uj83m1SqH8NVUOJx4mrQMeLdF5tjffMLIBSN_bX5vxTuJMuqbie03cIQJwcE2m6wzjXZSVu47SeGB4A1AhiMb30yv2UlwlIZc3cqDCtVOlnIvIv538HRfNenDTYj1wBMLs4w9aEtSeJKCfLjlNzhPbsYV_XUTYgtj2qNw4hAeBkPTF5_FtQcrizwsgkhjcWSZpRBOC9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو مراسم قرعه کشی جام جهانی هر مربی تیم بزرگی با قلعه نویی عکس گرفته تیمش حذف شده (هلند و آلمان) حالا مونده دوتا تیم دیگه که آرژانتین و اسپانیا هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131082" target="_blank">📅 17:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131081">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=H3M163WwsQa6EBYyMh2QSim1tAaqDiYFGb7QmMh3v2pYZKNTZSo69DcQz5tyQP6MpqscmsHBniwj8rSQ7nvCITqIWYR-eZBZvIAaanhPdEwFeVzw07V-eP188KUTbmKqRS665sp1PGsc9S6NWAWysj8auH-BlQD32mFxHsaziECaYC3nbTZfumyzqFb58zSQ9RE0Ri_33H9e0Qt42Rz7NlesXmJU9yCyqZ3oCmqcfxARXP0j7BjaEGfXZPW3XjKDlDRwGvqt4XCHx-SWF7dDPDEPy-byXSUXH5xYGaPntTdklKMGGdscIBEbOqvdKgrfLtdwRdkx7FKyxZAI-2ZVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00e51d5a7c.mp4?token=H3M163WwsQa6EBYyMh2QSim1tAaqDiYFGb7QmMh3v2pYZKNTZSo69DcQz5tyQP6MpqscmsHBniwj8rSQ7nvCITqIWYR-eZBZvIAaanhPdEwFeVzw07V-eP188KUTbmKqRS665sp1PGsc9S6NWAWysj8auH-BlQD32mFxHsaziECaYC3nbTZfumyzqFb58zSQ9RE0Ri_33H9e0Qt42Rz7NlesXmJU9yCyqZ3oCmqcfxARXP0j7BjaEGfXZPW3XjKDlDRwGvqt4XCHx-SWF7dDPDEPy-byXSUXH5xYGaPntTdklKMGGdscIBEbOqvdKgrfLtdwRdkx7FKyxZAI-2ZVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توهین زشت حسن آقامیری به شاه عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131081" target="_blank">📅 16:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131080">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSNHXfAUsbwn4kxwUZ-omjug9G4ZSuGCtAz23wqoJRbaL9GbFVw2mbIYj7d6IKvpQtToFnU2Mq3D5psJ6NcAe6N3Qr3ilTcmUQca0guRIz5GZzKtdxUDYE0bRw_UP5RAg9Bz3TSq250cV-cLeVLqZD5oa9WCIzxcZYeO_XLk3XvAqxeQPuWAfd8a6JC7id2ze1ACcU4aeUPPywI3JCdhuxHwQMzPg1UQXv8fdXMIgkEOwzFDwEeRPI-1FtjXT6dFM9SYq1b_OeuAKr8mz6nvBR9D797NnV6t0IWtCkR1h91W3WU7oRV3QGYWmEiDucspPCfHWYzQA8e9Pyalu56Mig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: نتایج تیم ملی عالی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131080" target="_blank">📅 16:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131079">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=boDFwANOWIaUUIUk3RyaN_Ms5PAp_lqct95E8HzUVkfFPWaTuJUwlgc_wUCV5AMeEMh5KoemCREOQ0Y-GzwMb6HGktY6MCGiHZ7Pg-pmTNfGwlqbknnIHCW3iWRZLfQhLqLxpxyyF1B3365lSjovARdHV1yd9Nqyb4Otg88nu_c3lmCzX9eWkmC2vKcIieO6PSsEgiCTC14cq-6q6v4GqSGp9vlZrAKEyIPv0wXmIIkqWR6T7lPqjLz3QdPZJOccq2N7RebzRBUM7DadY8sg1SEP8o-zuS0HHQL7VkTJDzLyfarMLbr4vP4xV8PcwmVbgA3fiRhXogXdezeykFzPAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa861dd055.mp4?token=boDFwANOWIaUUIUk3RyaN_Ms5PAp_lqct95E8HzUVkfFPWaTuJUwlgc_wUCV5AMeEMh5KoemCREOQ0Y-GzwMb6HGktY6MCGiHZ7Pg-pmTNfGwlqbknnIHCW3iWRZLfQhLqLxpxyyF1B3365lSjovARdHV1yd9Nqyb4Otg88nu_c3lmCzX9eWkmC2vKcIieO6PSsEgiCTC14cq-6q6v4GqSGp9vlZrAKEyIPv0wXmIIkqWR6T7lPqjLz3QdPZJOccq2N7RebzRBUM7DadY8sg1SEP8o-zuS0HHQL7VkTJDzLyfarMLbr4vP4xV8PcwmVbgA3fiRhXogXdezeykFzPAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمسخر کلمه دلیل؟ تجربه، آیت الله خامنه‌ای توسط مشاور قالیباف در آنتن زنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131079" target="_blank">📅 16:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131078">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بقایی: مردم عراق برای حضور در مراسم وداع و تشییع پیکر رهبر شهید در کشورشان لحظه شماری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131078" target="_blank">📅 16:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131077">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی ۲۵۰۰
ممبر از کایی ۵۰.۰۰۰
⚡
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131077" target="_blank">📅 16:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131076">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
خبرگزاری تسنیم : روز دوشنبه بورس ایران تعطیل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131076" target="_blank">📅 16:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131075">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=rIH7qqm9EShI_jv7BZzPGXlHjoZHKZSVH59i8nOhjfw8ew8IACNAUtfMsTcDiQr1ieie4S5efRhj6ud3VxR8d4zFAnZMoFSMMTvqGkolq0FQflQpn784fVehtvywy8399ofUsb8nv4tl2iSpW5bfUMDxLNnDoIxqXcFa3nDBVp37g9fZnPQEGPy8sw42G8fP9hJpkaETk67poVrRLWMG3nNIro-D10MgwRRfSha8uo_uHEMxHlJCVOklaPkWSpW4dZ2t4DhRefJgnQZwF4kffS3WJQuWUPyfaBvrxwEwhNvSQE97aMMi_4CUw9Jbt1fNp_fktXRhq8jpXZUEHnqF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c7de37440.mp4?token=rIH7qqm9EShI_jv7BZzPGXlHjoZHKZSVH59i8nOhjfw8ew8IACNAUtfMsTcDiQr1ieie4S5efRhj6ud3VxR8d4zFAnZMoFSMMTvqGkolq0FQflQpn784fVehtvywy8399ofUsb8nv4tl2iSpW5bfUMDxLNnDoIxqXcFa3nDBVp37g9fZnPQEGPy8sw42G8fP9hJpkaETk67poVrRLWMG3nNIro-D10MgwRRfSha8uo_uHEMxHlJCVOklaPkWSpW4dZ2t4DhRefJgnQZwF4kffS3WJQuWUPyfaBvrxwEwhNvSQE97aMMi_4CUw9Jbt1fNp_fktXRhq8jpXZUEHnqF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای نظامی اوکراین امروز صبح مرکز ارتباطات ماهواره‌ای دوبنا در منطقه مسکو روسیه را هدف قرار دادند.
🔴
این سایت که بیش از ۵۰۰ کیلومتر از مرز اوکراین فاصله دارد، برای شناسایی و هماهنگی فعالیت‌های نیروهای روسیه در اوکراین استفاده می‌شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131075" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131074">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: آقای قالیباف به‌عنوان نمایندهٔ ویژهٔ ایران به چین سفر می‌کند و ترکیب هیئت همراه و جزئیات سفر به‌زودی اعلام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131074" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131073">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا به فاکس نیوز: پس از رفع تحریم‌ها، هیچ‌کس به جز چین نفت ایران را نخریده است. ایرانی‌ها نتوانستند نفت خود را به دلیل ترس خریداران بفروشند
🔴
ایران تلاش می‌کند نفت را با قیمت‌های پایین‌تر بفروشد و سود آن اندک است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131073" target="_blank">📅 16:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131072">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=po04wefwYZH53rIOGy-ZDQyIgLEtWCrl9Eo5UjgEHFDGgwrtUU2p10IzHQQwdOiuGpsr7gdc0XgkImuZ-6DET4yhiCuNQeRBXD6_LZVG86BjWPi1DIHNfcBkF6rgOnuHwyW_5NrILKeNd1_uVKpGtDX4jkOlxlL3-X5VTGMg0yoK8Y3HE_4IOJFWi6viXMD9i9CghtlIf4KxY0Ba47e_pHONxpCdJ9-6EXDTuWzF8JjXGRe6fPfvTa70bCmcIbNOCcOQbaat15VN2LRs5z_jz4qMdERk0BDNIarWbNAVahCIDfBr33sSkA_UWSx54fIiAR55ZdqbIdeEMJOPm6EoSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcd78855cd.mp4?token=po04wefwYZH53rIOGy-ZDQyIgLEtWCrl9Eo5UjgEHFDGgwrtUU2p10IzHQQwdOiuGpsr7gdc0XgkImuZ-6DET4yhiCuNQeRBXD6_LZVG86BjWPi1DIHNfcBkF6rgOnuHwyW_5NrILKeNd1_uVKpGtDX4jkOlxlL3-X5VTGMg0yoK8Y3HE_4IOJFWi6viXMD9i9CghtlIf4KxY0Ba47e_pHONxpCdJ9-6EXDTuWzF8JjXGRe6fPfvTa70bCmcIbNOCcOQbaat15VN2LRs5z_jz4qMdERk0BDNIarWbNAVahCIDfBr33sSkA_UWSx54fIiAR55ZdqbIdeEMJOPm6EoSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: ما هیچ درخواست رسمی در خصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم.
🔴
اگر درخواستی دریافت کنیم، آن را بررسی خواهیم کرد، اما تاکنون چیزی دریافت نکرده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131072" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131071">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=ExwlPpYgCnTl9x9zC4WwFU5yd_Um1XvnDZ2HZtojFWr-WLYj0bSqkq1MJQTpOAWAqIERXLv7uo6hazdsf26A-veLrbcEoEIEP3yPWvuwHTq9fx9YNVr12FnzQgjirxLgOYq1hFhr80J36DmviAGPIqU44fJWQ1d9RQr-TnOsaf49ER4A5YusjIpUEjiJLi7yMuKybuOUOuQSmxLumefnD4fU4Qgv-tBiUwMX83s9olx0li10RafM79344JB4abH26DXiP3_eiUHNXfuywqZeSSl-bmvXQEjwhtFuyOJ28WJLFgO042ibwZP3kxkE3hvYdEscfq8R_08HKOu_OMBe-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3834c581a9.mp4?token=ExwlPpYgCnTl9x9zC4WwFU5yd_Um1XvnDZ2HZtojFWr-WLYj0bSqkq1MJQTpOAWAqIERXLv7uo6hazdsf26A-veLrbcEoEIEP3yPWvuwHTq9fx9YNVr12FnzQgjirxLgOYq1hFhr80J36DmviAGPIqU44fJWQ1d9RQr-TnOsaf49ER4A5YusjIpUEjiJLi7yMuKybuOUOuQSmxLumefnD4fU4Qgv-tBiUwMX83s9olx0li10RafM79344JB4abH26DXiP3_eiUHNXfuywqZeSSl-bmvXQEjwhtFuyOJ28WJLFgO042ibwZP3kxkE3hvYdEscfq8R_08HKOu_OMBe-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: رقص و جشن مقامات آمریکایی به خاطر عدم صعود ایران به مرحله بعدی جام جهانی، تمام استانداردها و هنجارهای پذیرفته شده میزبانی را نقض می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131071" target="_blank">📅 16:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131070">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با تنگه هرمز، تکلیف کاملاً روشن است. بند ۵ یادداشت تفاهم، مسئولیت جمهوری اسلامی ایران را به‌صراحت بیان کرده است.
🔴
بنابراین، روندی است که آغاز شده، تداوم خواهد داشت و قطعاً جمهوری اسلامی ایران به‌خوبی می‌تواند این روند را بدون نیاز به مداخله هر طرف دیگری انجام دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/131070" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131069">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
قیمت کولر ۳ برابر شد !!
🔴
مهدی بستانچی، رئیس انجمن تولیدکنندگان سیستم‌های تهویه مطبوع ایران: کولر آبی ۷۰۰۰ از حدود ۴۰ تا ۴۵ میلیون تومان آغاز و در برخی مدل‌ها و برندها تا ۸۰ میلیون تومان نیز افزایش پیدا می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131069" target="_blank">📅 16:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131065">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hr-Ua-BRznyvRzGTC6pZeaCzgYjvzwMqE0K-fhRXPnhbJrvlY7zYMNh015eV5OrgTiV1GTRy4yjeFZKYee8YSyWcSHHMLgUWZaUGlF2BY4eXzgkjV28vv60qzOWU8EbuM7qGc_NxLP4D-nGzq-YYqpXcZ1gZ-pbl_ru9W2B8u7BcZGPNRTdlHSuBrwoKGFJnyrz2C5FyMTzBTs2KGvZvfwwWebvADmPlc2T6yhhh_5jZQQ34kH8MXvehF3YV9aW04jo31vjd7N3wrm_5iUZJey7btl-__qvgrT3OVHYm0tNm6gm4G9yitFB1S5P7qBRJKbcpirSzHqaQXsDf-eeyDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fdmw6BvGTVQWRpsfBhTUR80Q6JQE_QPZUqRTrs3xng-UvuOtLr9yIlBbnHEYGGMb8X1wDi_AQOnU4_6zLsghLej0SgSKPMNcUSa99o38GSStKsb6_BtYoTxMWcaz4ZCKqtjqAB7HiDWaGWXavbrXf5NXZ7dK5InfHrDI6muKrUGg7aQ33YEJmFbkn2_QQFJMjJxRwn3SAdkHrPajT22fLGtPznQopb5ZItiAspwoiOwT2GnWwfZ6-zcpOHXsLnQ8bhadT7F1R3WjtnKQbJVtNfq7bSLDpjDd2Q7j050r2vtdhXuZpSaf7U_uYSIotoE_YzxETH3JtYBcD3P_0axMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwpHwHow7Jm28SEf0UaqcC_FGIj1ylSAWWDdW-x3a4KmhNdxZBatanv85wIcZA2gHnFQTCNlXYCKfY6SWFpTBspdz4WSy8WBXnq_PgnA4lFJjeiOxiO3LqWC2pdsRM3Za9hBHeSNpWXJGZ3OOBU2UPWtnZREw7PdhicOazdI5mWlbXGTEgpwmTF0A0MxY1VppUwMDhJhfax1PjPN6eF_9EUg9v6v96M3AOaS1iTeFZYzEEdjD-tZshGVYeBuTzDyPw6jTgrulDG9J_k_s8bYiYMcwWUu2Ld81WWPc6JrOs-hzZ0__eFcsRICXnjsdfOD2NoXUCR3OtMl6Uk_0oLiVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcQWafCeKFDa__BZhld1fVg-2czsJPFQPgtr_Dsj9mc2BX6bjEqRlEPru8wmJiS0LxzG7FdkRjkxqSuyVlQTBBeOu57I55CTr1m8j3DbG_VKTxeolk-0yjj0lQNKcy14OjfODNbf1sYl4IDlWL5J1MdVX-8h7XxMj5BUffkPhbXP5yo9zYLZW1quWDkzB52ysLpiCisfwHX0tTr5YTsI7UQ8UTsGC8WRrBBPlDOEXH4jOxDuWnYI5y4b057qIg9yKcwIm4zgci5D_TwSG0PYPxUijF3KYRQE1TwNlu9jw8G_oAEgAtc7EA4QaORgQMKd4hcvtDXmDN6hJBF4RtK7hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در ادامه دستگیری ها در عراق موقع بررسی پرونده معاون وزیر نفت این کشور، ۱۱ میلیون دلار و ۴ میلیارد دینار پول نقد تو خونشِ پیدا شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/131065" target="_blank">📅 16:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131064">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7907cf315e.mp4?token=HQrrD5JjVuAvE4mrZl01TNYkQPWZ15kKj0CUr0J3fhPgw72yTCn0iz-OrAjOz-7gduo8P12jyxW5MGCIIwsBtMA0k1pvGqhSDKOfocIbVq8XUB26MeTdhzrt9rwklPfr4SeWPDRKeF7H8wBxfxxhBzyD263mzkNjfz26_IsvXv6pYnhk0I5Q8pNb4PSZk6BBXWhH2NDPrc5HX8UcV1Fy0tE_C49-dXGZgYm7WF81If85DA70GRo9bPPNslwzPZ96zxIgsYutwNhbTmb1m2lTY0hQNhRxVqF6fgPyFc6kKd0s9pKNFglCLsSK26aFTMPir-Fq6flnFc-l4M9qVlzhlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7907cf315e.mp4?token=HQrrD5JjVuAvE4mrZl01TNYkQPWZ15kKj0CUr0J3fhPgw72yTCn0iz-OrAjOz-7gduo8P12jyxW5MGCIIwsBtMA0k1pvGqhSDKOfocIbVq8XUB26MeTdhzrt9rwklPfr4SeWPDRKeF7H8wBxfxxhBzyD263mzkNjfz26_IsvXv6pYnhk0I5Q8pNb4PSZk6BBXWhH2NDPrc5HX8UcV1Fy0tE_C49-dXGZgYm7WF81If85DA70GRo9bPPNslwzPZ96zxIgsYutwNhbTmb1m2lTY0hQNhRxVqF6fgPyFc6kKd0s9pKNFglCLsSK26aFTMPir-Fq6flnFc-l4M9qVlzhlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسماعیل بقایی: احتمالاً آنچه فردا در دوحه اتفاق می‌افتد، بحث درباره اجرای بندهای یادداشت تفاهم است، از جمله بندی که مربوط به آزادسازی دارایی‌های مسدود شده ایران با طرف‌های قطری می‌باشد.
🔴
بنابراین، تأکید می‌کنم که هیچ جلسه‌ای در هیچ سطحی با طرف آمریکایی برای چند روز آینده برنامه‌ریزی نشده است
🔴
تمام آمادگی‌های لازم انجام شده است و امیدواریم کار به‌درستی پیش برود و به نتیجه رضایت‌بخشی برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131064" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131063">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEAiybIERrGGDp9eTF2oG8K8xLejZGfFbt8UkG7IZlEbBM_p1B_bRDG71WdOSif2cCeny5uj8dr5rclwq14QKQGj3dTIOLbltOD0jR9VIwZgsOzGzFWtJenWxX4GPUH4P-jbd7usSZP43KT8gET6GSCydxYjaCgpKXtbITFC3NXLJlpSsWhC4WN2GEQ-WRRBWFmRoBts8MVI-I6hkglqkAgBqrKa6ux4SKH5QX6Y41pV5J4-V3d60_4fUPD82awV5lkGDC6lUMQ6mZydCK2V6jXe76u9MiGThABSEe8DdirZegFJBQJookyULpWV_qFYWjRwZLO5iia5dndiYVEeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع العربیه: ایران تا پایان هفته ۳ میلیارد دلار از دارایی‌های مسدود شده خود را دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131063" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131062">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بقایی وزارت امور خارجه ایران: خط ارتباط با واشینگتن میان این وزارتخانه و یکی از نهادهای سیاسی آمریکا است.
🔴
در روزهای آینده در مورد زمان و شکل شروع مذاکرات توافق نهایی تصمیم‌گیری خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131062" target="_blank">📅 15:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131061">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=BbyDh23ductZhPCSlIqBTEdFBvPflRFEfDUdYmV8oyXCTqzAsjzW_nYdLfsJBXUiVh9TK0ayXEcqiY5V9pQDEEm6mSC7cOUDTA83fyM10NwjejnL4EJYbGtbwQXXrdFpnyb6SG3rHpyDD3HDfcSt6rdyWAJqIx63yzTJCiEjUChQ0gZ-eecEQXYlJCTMsvLf00eeK1BG4vVK1rm1FdqTVzDAbOhp4W6wd8qX1RuoxwrNRx86QgUeN-lzKkLYJnvZVqa29cefct72ZaGNT8_5_7Rqt2_-1bG5jLj-yU6hJU1-FP7J180tmuLWxg7MLy_GdQH7zpP53mnV4NQrF-rnXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a081ef12.mp4?token=BbyDh23ductZhPCSlIqBTEdFBvPflRFEfDUdYmV8oyXCTqzAsjzW_nYdLfsJBXUiVh9TK0ayXEcqiY5V9pQDEEm6mSC7cOUDTA83fyM10NwjejnL4EJYbGtbwQXXrdFpnyb6SG3rHpyDD3HDfcSt6rdyWAJqIx63yzTJCiEjUChQ0gZ-eecEQXYlJCTMsvLf00eeK1BG4vVK1rm1FdqTVzDAbOhp4W6wd8qX1RuoxwrNRx86QgUeN-lzKkLYJnvZVqa29cefct72ZaGNT8_5_7Rqt2_-1bG5jLj-yU6hJU1-FP7J180tmuLWxg7MLy_GdQH7zpP53mnV4NQrF-rnXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: روند فروش نفت و محصولات نفتی ایران خیلی تسهیل شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131061" target="_blank">📅 15:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131060">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری/ منابع العربیه: مذاکرات غیرمستقیم فردا بین هیئت‌های آمریکایی و ایرانی در قطر با حضور میانجیگران برگزار خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/131060" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131059">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران ممکن است هر لحظه شروع بشود و ما برای آن آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/131059" target="_blank">📅 15:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131058">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بقایی: هیچ درخواست رسمی درخصوص بازگشایی سفارت کانادا دریافت نکرده‌ایم/ در صورت دریافت بررسی خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131058" target="_blank">📅 15:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131057">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی هیئت مذاکره کننده ایران:
در رابطه با مسئله لبنان، موضع ما روشن است
🔴
تعهد ایالات متحده آمریکا برای خاتمه دادن به جنگ در تمامی جبهه‌ها، از جمله جبهه لبنان، یک تعهد صریح و آشکار است که وفق بند اول یادداشت تفاهم بر آن تأکید شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131057" target="_blank">📅 15:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: اساساً برنامه‌ای برای دیدار با آمریکایی‌ها در هیچ سطحی نداشته‌ایم که بخواهیم از آن منصرف بشویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131056" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی:
با قبول کردن آتش بس، به آمریکا فرصت تنفس دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131055" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131054">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f440c5937f.mp4?token=aHAnITO5INptmFUanuWZ3nqcrWnFh4ea5wiXjUeLXdseQW_-gxGIOSJgrriy_GO9s4nmEnQU2E7luKVbweK2zj7QOHTlaeeHX82KKPtj8TGgrIhmOZt2dxrOQ9Ibxbpc6jkiOZht7JcnTj8rdjs8hDw7G-muUmK6LqULNKNu3xIhoVB6ljqshKm2xW2FWGLUHzB98uX93yVV_Sjxa_3ICpKt1p4vkrCtR56jVBYp8IIj8mSvA1XFV46FtA_j7RWqH5w4lw_Ty5VCRFd8u11r8ObZRqpbFCdUBVUhuB-yMG_XaxLANIH1Iur6mBoCkw7115l9p54GtnJke74X0sRGeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f440c5937f.mp4?token=aHAnITO5INptmFUanuWZ3nqcrWnFh4ea5wiXjUeLXdseQW_-gxGIOSJgrriy_GO9s4nmEnQU2E7luKVbweK2zj7QOHTlaeeHX82KKPtj8TGgrIhmOZt2dxrOQ9Ibxbpc6jkiOZht7JcnTj8rdjs8hDw7G-muUmK6LqULNKNu3xIhoVB6ljqshKm2xW2FWGLUHzB98uX93yVV_Sjxa_3ICpKt1p4vkrCtR56jVBYp8IIj8mSvA1XFV46FtA_j7RWqH5w4lw_Ty5VCRFd8u11r8ObZRqpbFCdUBVUhuB-yMG_XaxLANIH1Iur6mBoCkw7115l9p54GtnJke74X0sRGeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برج ایفل ۱۰ سانتی‌متر بلندتر شد!
🔴
در گرمای شدید، سازه آهنی این برج به ازای هر ۱۰ درجه سانتیگراد افزایش دما، حدود ۲ سانتیمتر منبسط می‌شود. وقتی دما کاهش یابد، ارتفاع آن به حالت عادی بازمی‌گردد.
🔴
تابستان امسال برای این نماد مشهور پاریس روزهای سختی داشته؛ یک روز دمای هوا به ۴۰ درجه می‌رسد و روز دیگر صاعقه به آن برخورد می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131054" target="_blank">📅 15:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131053">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
سخنگوی وزارت خارجهٔ قطر: اموال مسدودشدهٔ ایران آزاد نشده و آزادی آن به پیشرفت مذاکرات ایران و آمریکا بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131053" target="_blank">📅 14:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131052">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f60302362c.mp4?token=cYSi9HisPNUWBpm08UmEu5NaFCx0brQM86DnJMaRADqpfAQiX9umIJiPeyGovv_e-WE4pi9i4tnYFi0yNw1nbU44aLHPRgApLPR_uG3kfuvhmUDgfNtQRA6YUH7OWvSdPEl1K0ndy0IQbgnbE45jyLTt91LBNuh5SVKsRYD7HEl8EddrOH8Lc0lwbElqs2eiMgn9iSk32nV-cL7Xp-9KwpgME93PC-b_ByMUzz4Z74_OMouyqeZZnBw8YPwBRVqRhPn96ni7yuqaz-mWwKNrpoO0gVi4YUydt_Sq-9vHw2vQqPqF0D22iNKObkfanGSI6OZxdH-E2taOI8X86ETe0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f60302362c.mp4?token=cYSi9HisPNUWBpm08UmEu5NaFCx0brQM86DnJMaRADqpfAQiX9umIJiPeyGovv_e-WE4pi9i4tnYFi0yNw1nbU44aLHPRgApLPR_uG3kfuvhmUDgfNtQRA6YUH7OWvSdPEl1K0ndy0IQbgnbE45jyLTt91LBNuh5SVKsRYD7HEl8EddrOH8Lc0lwbElqs2eiMgn9iSk32nV-cL7Xp-9KwpgME93PC-b_ByMUzz4Z74_OMouyqeZZnBw8YPwBRVqRhPn96ni7yuqaz-mWwKNrpoO0gVi4YUydt_Sq-9vHw2vQqPqF0D22iNKObkfanGSI6OZxdH-E2taOI8X86ETe0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل یک تونل حماس به طول ۱۶ کیلومتر در غزه را با بیش از ۳۰,۰۰۰ متر مکعب بتن مسدود کرد.
🔴
این همان تونلی است که جسد اسرائیلی، سرهنگ هدار گلدین را به مدت بیش از ۱۰ سال در آن نگهداری می‌کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131052" target="_blank">📅 14:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131051">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffe136f3fc.mp4?token=elzkc2T5HhqD0wNmtotrwG6od0W6ixJJdu3jBteC2s8_InIUO1_oYvf5Kl3LaKqNIeK8Kg4RgS5dQnQXcmddw7TiiJKPpKH0PaXblJX37U7-ePhfrtW7EJqgEcALPkSkdBNgJQ5ttE49xljFWU2CXtCkjVVMSh4-OmjO-6Dj4Ou8ho801ibDp-B48kcdLb7fuqU3n9ICYB2oMXA59au3uA2lhHtNh12XQ7tK-_I5RH92zDVvEhzM-UYBCHtYW2IndksevKDDmZBVDToXE_VED7OZLQiiJvyN0ki7gWaS_TMFRA0O61J_sojvHrPH76p2BpIluCWhb_Ia_qS6OERxvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffe136f3fc.mp4?token=elzkc2T5HhqD0wNmtotrwG6od0W6ixJJdu3jBteC2s8_InIUO1_oYvf5Kl3LaKqNIeK8Kg4RgS5dQnQXcmddw7TiiJKPpKH0PaXblJX37U7-ePhfrtW7EJqgEcALPkSkdBNgJQ5ttE49xljFWU2CXtCkjVVMSh4-OmjO-6Dj4Ou8ho801ibDp-B48kcdLb7fuqU3n9ICYB2oMXA59au3uA2lhHtNh12XQ7tK-_I5RH92zDVvEhzM-UYBCHtYW2IndksevKDDmZBVDToXE_VED7OZLQiiJvyN0ki7gWaS_TMFRA0O61J_sojvHrPH76p2BpIluCWhb_Ia_qS6OERxvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر بریتانیا کیر استارمر:
۶۴ میلیارد پوند برای نوسازی بازدارندگی هسته‌ای بریتانیا سرمایه‌گذاری خواهد شد.
🔴
این پول صرف ساخت زیردریایی‌های جدید، توسعه یک کلاهک جنگی مستقل جدید و خرید ۱۲ فروند جنگنده F-35A خواهد شد تا نقش ما در تضمین امنیت بریتانیا و اروپا حفظ شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131051" target="_blank">📅 14:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131050">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از سخنگوی وزارت امور خارجه قطر: اموال مسدودشده ایران مشمول توافق سال ۲۰۲۳ است و به‌طور مشخص برای خرید کالاهای بشردوستانه اختصاص داده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131050" target="_blank">📅 14:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131049">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه قطر ادعا کرد: جلسات فنی بین واشنگتن و تهران متوقف نشده است و میانجیگران برای تسهیل آنها تلاش می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131049" target="_blank">📅 14:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131048">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزیر ارشاد: دیدگاه‌های مطرح شده توسط مراجع عظام، علما و فضلای حوزه علمیه قم در دیدار با رئیس‌جمهور، نشان داد که بخش اصلی و تاثیرگذار نهاد دین از دیپلماسی عقلانی حمایت می‌کند
🔴
در دام تبلیغات جنجال‌سازان قرار نگیریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131048" target="_blank">📅 14:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131047">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:  ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131047" target="_blank">📅 14:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131046">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: ۶ میلیارد دلار از دارایی‌های مسدود شده ایران هنوز به تهران منتقل نشده است
🔴
حاکمیت و سیاست جدید ایران در تنگه هرمز اعمال خواهد شد؛ چه با عمان، چه بدون عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/131046" target="_blank">📅 13:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131045">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / سخنگوی وزارت خارجه قطر:
ایرانی ها از دیدار با تیم آمریکایی منصرف شدند. ویتکوف و کوشنر در دوحه حضور دارند اما با مقامات ایرانی دیدار نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131045" target="_blank">📅 13:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131044">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=mmSixXCIPLm260XGZSGbXAlBFdr_uyUdpfKth3wyllSO-OriQIS6uSGBVDZdxcNbW4ftH9eE8L68zzjSeCmy3w76wjDVd6cEHfoSSDkPGBCCGsEfiilyMZvJSeyoUMuT9vI5ZYjtg726YmMGX4PzWEUACV0Oj4xStKK57oZ3OuvnD_Zgs7HbEU4otn7AdzCREKdH1jH9XKl4BGwPxfEBLlPJsMk9gyI_reG_qDev63zmToq2dVajm2gIvKeWYHYAj9rooZoGGdre-f_98zOBYnjsVj_r4IQzLexkjUf0Fe4M3JaFlEnZFcZFJCgbKtHyMK3WJODhzKeq93nEme3rZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7204ae52a8.mp4?token=mmSixXCIPLm260XGZSGbXAlBFdr_uyUdpfKth3wyllSO-OriQIS6uSGBVDZdxcNbW4ftH9eE8L68zzjSeCmy3w76wjDVd6cEHfoSSDkPGBCCGsEfiilyMZvJSeyoUMuT9vI5ZYjtg726YmMGX4PzWEUACV0Oj4xStKK57oZ3OuvnD_Zgs7HbEU4otn7AdzCREKdH1jH9XKl4BGwPxfEBLlPJsMk9gyI_reG_qDev63zmToq2dVajm2gIvKeWYHYAj9rooZoGGdre-f_98zOBYnjsVj_r4IQzLexkjUf0Fe4M3JaFlEnZFcZFJCgbKtHyMK3WJODhzKeq93nEme3rZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : توافق ایران با ترامپ و کنگره آمریکا نیست توافق با نتانیاهو هست
🔴
باید ببینیم نتانیاهو متن رو می‌پذیره یا نه چون تصمیم‌گیری نهایی با اونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131044" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131043">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=GSX1kmXr0D6ljDK1aANyES4mkZXIV3TtU0SfccsuRQ_UznUpO8RRaNy-kIkVgS6eNijAPpR3cKVneDNJx60c5mWMBdQpT4VXW5wFNlIzXl2wEJJTmQHfGeSnFQrffAj_UDB0jMSIDlw32bo128WjFYVw6UViQpOwTGL3XT3Gvb4PyCMt18L1309RvZrd682rzbbOPVV8GD7Ie2Des_woscvv6mxndS3uFZ8cRdF0srpfsTPR10aOPNo7-TSYRxdXlNYlMVjc5mhIdxUS_oUm-S6TaHrf3JNo4M-4Q1InMdkZ79YyHDMD9zQ4pXZEanh7X-T2RkNG-O_Ee6h4VJWbuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d66c8103ea.mp4?token=GSX1kmXr0D6ljDK1aANyES4mkZXIV3TtU0SfccsuRQ_UznUpO8RRaNy-kIkVgS6eNijAPpR3cKVneDNJx60c5mWMBdQpT4VXW5wFNlIzXl2wEJJTmQHfGeSnFQrffAj_UDB0jMSIDlw32bo128WjFYVw6UViQpOwTGL3XT3Gvb4PyCMt18L1309RvZrd682rzbbOPVV8GD7Ie2Des_woscvv6mxndS3uFZ8cRdF0srpfsTPR10aOPNo7-TSYRxdXlNYlMVjc5mhIdxUS_oUm-S6TaHrf3JNo4M-4Q1InMdkZ79YyHDMD9zQ4pXZEanh7X-T2RkNG-O_Ee6h4VJWbuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایزدی : جای تعجبه که عراقچی می‌گه گرفتن عوارض از کشتی‌ها در تنگه هرمز خلاف قانونه؛
🔴
سؤال اینه، کدوم قانون؟
🔴
اگه حتی رئیس خلیج فارس هم باشیم ولی نتونیم از این موقعیت استفاده کنیم، این اسم و عنوان چه فایده‌ای داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131043" target="_blank">📅 13:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131042">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055600096f.mp4?token=k43YEEPVLq_GBRZ9jc4xfIDK0_pITWUXwDL1egP4UDZe72sdZHRXfxSqTXpJ_GqMG-YBRMdpt29ntWTgyagRhStHqKgRRQjNoYF6EQTdQQgUfECTcpeAKbrWnwghwp7YAcNs6QhCX9aDE5e0lQnwcro20Ye98HUqF5-pCil4EihPRrk3Z2hXr_EYDGqORKLLynQ1lifwdSZtEOoYv2gwkLywFFs7q2bHSBy4CIsFl0JFrfDiSSg9-mf6kvPBBKqjvLQDtCunzBiZNyMvJyLaxU3_-A9HfvNSv84rsU9iEu6giCxW9Ubw9fva-bLBd9z6k0ik8cRJKEJqeOS3NTuxSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055600096f.mp4?token=k43YEEPVLq_GBRZ9jc4xfIDK0_pITWUXwDL1egP4UDZe72sdZHRXfxSqTXpJ_GqMG-YBRMdpt29ntWTgyagRhStHqKgRRQjNoYF6EQTdQQgUfECTcpeAKbrWnwghwp7YAcNs6QhCX9aDE5e0lQnwcro20Ye98HUqF5-pCil4EihPRrk3Z2hXr_EYDGqORKLLynQ1lifwdSZtEOoYv2gwkLywFFs7q2bHSBy4CIsFl0JFrfDiSSg9-mf6kvPBBKqjvLQDtCunzBiZNyMvJyLaxU3_-A9HfvNSv84rsU9iEu6giCxW9Ubw9fva-bLBd9z6k0ik8cRJKEJqeOS3NTuxSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فواد ایزدی، کارشناس مسائل آمریکا : ما
هی از آمریکا می‌خوایم تحریم‌ها رو برداره
🔴
در حالی که تصمیم اصلی برای برداشتن تحریم‌ها فقط دست ترامپ نیست؛
🔴
بخش زیادی ازش دست کنگره آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/131042" target="_blank">📅 13:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131041">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-Ge2oOtD0Y7Kk25lXbDhyGGwjWgY-IvJ6FtYj0x5VxH6Zug17KKVSBS9LzYC0Gscpo-JfvyzvrceF21PcxeeKoY2xrRlcHI2jo7A3vthxGxboHadyYFkanCfhhcHi1mDwQfY6lf3rmLtwHPFGebScQkM5eEE-v3Gi86qpXeOr96u_tejpbUR8MBYNaAkf-EG4ZUblWTqvy4m49_EiYzNcA1mEzn5Yx13vAvr3v5LDhmIauDgWU8ZuWKhZQOGwYwEq-_cZnitdbqDbXvChu50fU4DDSoWouR9jqY4i06hgBvm-gPrEoxHsTsammPC64ZByOFF07YdCFwVhC7b1i4EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه همشهری با این تیتر ترامپ رو تهدید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131041" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131040">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
پزشکیان: اگر آمریکا به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/131040" target="_blank">📅 13:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131039">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نیویورک تایمز :  بیشتر سربازان تازه‌نفس روسیه در خطوط مقدم اوکراین تنها ۲۰ دقیقه عمر مفید دارند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131039" target="_blank">📅 13:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131038">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزارت دفاع روسیه گزارش داد، شهرک‌های لسنویه و رونویه در منطقه زاپروژیا و شهرک مالینوفکا در دونتسک  توسط نیروهای مسلح روسیه آزاد شده است.
🔴
این وزارتخانه همچنین از انهدام هفت بمب هوایی هدایت شونده و ۸۰۶ پهپاد اوکراین طی شبانه روز گذشته خبر داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131038" target="_blank">📅 13:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131037">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: چرا اعراب پس از جنگ اخیر دنبال رابطه با تهران هستند؟
🔴
پای یک چارچوب امنیتی جدید منطقه‌ای در میان است
🔴
کشورهای خلیج‌فارس در حال فاصله گرفتن از اسرائیل هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131037" target="_blank">📅 13:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131036">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIRMQmTYnzYgqmZoWGgRyqAaUY2UPrtc5lV_-rIxFWJZV6kcfSPyAZ4sCEj3PIfba9kwz1ScYnNU-qeOJRtwT3vpH9kSmZSp9-v3mW0Jspdcr8v3puqhhw4jpq8b00hqfezGcxGf6jYRZuAkMiW2O00Sk0lyK3x-CdnRtyJc0FEskUofVNl-Dj3aEWT9K7PRbOZi9x2eSPQxTZZNrcEIvwnuqTVVzRSzFW3jnGZkRAUBhdWULK8-10ayohuJzAX-IgbgTF7ZBqxKzVNSETe2vQmTNceg4yjRPD8uLY5NBudu3DZjtk3VxKnciaA4P7LqdQ4tXAAvLGCY6AzOlTGgyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون اجرایی رئیس‌جمهور: جلیلی به امضای تفاهم‌نامه میان ایران و آمریکا رای مثبت داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131036" target="_blank">📅 12:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131035">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibb9ca94pttDDcmYUOFFgVIhdsoSKDJBPLVfy5dmKIVEqg5q5F2VjnsZE9dAIWJfMyg9BMn06WT9aGCFlWOQYTxpJLYFmfon5l4gkxN_ATRI5Xf2JCT2wYNB2C6JxmSMQeTj9KIcpYirfXrqAuzG6sLQI4YNjhgT9w-_Rm_cGlxUtjEVuze6PwXBn0p8XSUwvyNikyw-O4GdnmKDUZZF0I8lcK_VsQGczPow6hzRktJGsPGwCAy4Dxy3HJqEYUXQiIfpBvj60hSteoPmpIBeF5sYER_TBISMXxsHKEmGT8XL360y1xPDDyOTx3PY-yf35d-D6MN2waFVjbqNwqfbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخزن ۳۰ میلیون بشکه‌ای هند و امارات برای دور زدن تنگه هرمز
🔴
بلومبرگ: هند در پی اختلال‌های ناشی از جنگ و انسداد تنگه هرمز، با امارات برای ذخیره‌سازی تا ۳۰ میلیون بشکه نفت در ذخایر راهبردی به توافق رسیده و قصد دارد برای نخستین‌بار ظرفیت ذخیره‌سازی گاز طبیعی و LPG را نیز توسعه دهد.
🔴
حدود ۴۰ درصد نفت خام وارداتی هند از تنگه هرمز عبور می‌کند و این کشور تقریبا ۸۵ درصد نیاز نفتی خود را از طریق واردات تامین می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131035" target="_blank">📅 12:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131034">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxlz_Q5D-Z6e5dV84Bs40nldw4nTXpVCkvq5JjiGcUuC10iYE38_EYdDfz8ejDdm4eYaH9q5FQaAWaVL5pYNHMEo86nqcopUzWHK76diQmuzvR0h10jTHiDUkScqH7P3vXCKCRPfDjDYBXTRT0mwplVc9wLG3e5KLAuKAIcoUqzLRJbmQT8Pr6Of5HWSTXCOGX5vcNu6X4D_tT-LcE5LmUuVfRc-pGaFkmE5MFuVEIur04nDePNJ-4TK9keJtazsRJ20sZOnIloGLS8-Pzx8myZe0s2B9hRqVk-bh7N3RehnbPcnkr_HUMfjQg5XhpLEy_UcqSyw1lV6ycsziNynCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با جهش ۶۸ هزار واحدی به ۵ میلیون و ۱۲۸ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/131034" target="_blank">📅 12:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131033">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فارس: بیش از ۳۰ کشور برای حضور در مراسم تشییع رهبر اعلام آمادگی کردن و نمایندگان و بزرگان ادیان از ۹۰ کشور به تهران میان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131033" target="_blank">📅 12:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131031">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s-hgyvUXPCFr6D5H75DUZunUYK3T3lEM-ISdpaCA6tMofipJxDiwXqkaFW-55I1qAzcXy3HpRYta4G63U-sV7UaiEd-CG0AS8KOIh4_rsPUY43FQw60M50RnDjrJfJ-6dDQ5axObcGM7nwCU4-6q8R_YnwtSjKMOzulxEVF_3QJGkUXvu5S2IK4QLf3oI4YXm_Z-VNXSTn8-jd1BwuajTkib_LuXWtYZB3kFmYB-t20X6RCL3TkR8B1rLsK6hI1huA-ZI5nrcWhOMR8A7LzR76TXzaIBg-u_EavSJj70ru7RTXIBorsdQxHTN0m8zTOAhlbNZZ4F0UjE_VzSMZqAXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dIbXOf8Bf7wpazndxh_zL5B8xbTmf1qC7ikYIQNhA3CXAcjr-BjWA5nm4agaGWChDQdWp_2Z7jVkPohsqlhxF-pUR2At0Ru1LJHt6Zx6frZJpAah99_DoAfopqu2joVm-yoaQQmj3rhW2N7NI_X_6RO-BEeYtlUhozLhCmORedrq3Vj-4mCPlkhRIEv9taYYwXVbEQ6TW7zq3o6_evMiYuWv3LMhTBZW7zOk5V2waBx3AEsCU0RMI0w85T1tT0LcQq33j-nl4mvKvhW2_ezIHukbAeczoNa4CmpsgHfsiK-TQ_op0HwXV9Gd9vuqPLNOG1ssUFzE02cebdEgHRFphA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به یک پست مرزی ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/131031" target="_blank">📅 12:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131030">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
اژه ای: در حملات موشکی به زندان اوین، افراد زیادی می‌توانستند فرار کنند اما فرار نکردند؛ بعضی هم رفتند اما خودشان برگشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131030" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131029">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
منابع خبری از پرواز گسترده پهپادهای اسرائیلی بر فراز بیروت، و ضاحیه خبر دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131029" target="_blank">📅 12:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131028">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=SjAsSdMyxUC3UaT54pSGNabDHhxLfu09D-7j-9sfPuc_vslVa_9iAtOQwXgNronicfLq5s9WslzymrUQvau52q0l5jSd5SgM0aRC1eaZD9njUkryc1WMWWfd01cMaDS-uEoA346bLtYa4IrIwHjNYQC6IK5UHmfyBBKhw7LB5z-JziIquMMrAH_exnxd3Ni_ozdQKOFSNNIe0VYIW8J1JY8nBWEmYJ_86It361WIbW1eV4vG7QE9uS22MYiX-eExMg45uPJgwA9-4V7krjFzMYHjED36lUvi_u4ZJF-t9ERha4SphyGHver0C9a8TF4hR373y_axgMtidG4bQDYKDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeafe2956.mp4?token=SjAsSdMyxUC3UaT54pSGNabDHhxLfu09D-7j-9sfPuc_vslVa_9iAtOQwXgNronicfLq5s9WslzymrUQvau52q0l5jSd5SgM0aRC1eaZD9njUkryc1WMWWfd01cMaDS-uEoA346bLtYa4IrIwHjNYQC6IK5UHmfyBBKhw7LB5z-JziIquMMrAH_exnxd3Ni_ozdQKOFSNNIe0VYIW8J1JY8nBWEmYJ_86It361WIbW1eV4vG7QE9uS22MYiX-eExMg45uPJgwA9-4V7krjFzMYHjED36lUvi_u4ZJF-t9ERha4SphyGHver0C9a8TF4hR373y_axgMtidG4bQDYKDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو:تفاوت اصلی این تفاهم‌نامه با برجام اینه که برجام یک توافق واقعی با تعهدات و چارچوب مشخص بود، اما این یکی عملاً چیزی جز یک کاغذ امضاشده نیست؛ متنی که فقط می‌گه طرفین قرار است درباره ادامه گفت‌وگوها، باز هم گفت‌وگو کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131028" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131027">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAinuTbda53GnQnCKAJ0V2OgM9Nz_rwaM3YCDi_QJIhaJqbJ74OBX2BJQCcRvZcaL61MEfsTBZecWhQJWJ5KFe-K1EJ0kvR_XI9AYFtLucwkubcoNDzfVDPdpc3Jo-ZOUXOHthJ3iPDnFlC0mkrZYQ0NXq0tILLtfIwdq_OcuLEUut5P1qDQ9pMRDmsEZxR6h7RtBh4JxxtUA_L2xBZrQ12T3m-_EG4DeKma_mSYy-6FNt_93ubkmd5TjEVmFovOdLRhFhIgxHjBkKGU37AFC_d64JRl8P8-Cljs_FA307YA3oHkSnlisOlUeM3-BFEyNa8ai5s0SmNAxIy-4venfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه نیویورک تایمز گزارش داد، مارک‌وین مولین، وزیر امنیت داخلی ایالات متحده اعلام کرد که پس از حذف تیم ملی ایران از مرحله گروهی جام جهانی ۲۰۲۶، «رقص شادی» کرده و حتی «چند آهنگ» خوانده است
🔴
مولین روز دوشنبه در نشست خبری مربوط به جام جهانی گفت: خوشحالم که کارشان تمام شد و برنمی‌گردند. وقتی ویزاهایشان را گرفتیم و گفتیم باید خاک آمریکا را ترک کنند، خیلی خوشحال شدم و ممکن است رقص شادی کرده باشم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131027" target="_blank">📅 12:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131026">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
میخائیل اولیانوف و رافائل گروسی درباره چشم‌انداز حل مناقشه بین آمریکا و ایران و نقش آژانس در این فرآیند گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131026" target="_blank">📅 12:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131025">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
یک هواپیمای دولتی آمریکا از میامی به مقصد قطر در حال پرواز است و احتمالا فرستاده ویژه ترامپ، استیو ویتکاف را برای انجام گفت‌وگوهایی با ایران حمل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/131025" target="_blank">📅 12:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131024">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بلومبرگ به نقل از داده‌های شرکت کپلر: حدود ۲۴ کشتی باری، از جمله کشتی‌های حمل نفت و گاز، روز دوشنبه از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131024" target="_blank">📅 12:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131023">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_S03CuxsyK-a0Lw30nFMVtGkMROjCR-Wse2H9ceXLeW51cBocMInGH83wD3ryQH0X2QPjDtZj_VFBSZvY8g926ZKMwkaFmqjPNtrVNHZneFz9kL4WN16r8tN-ZxieBgVEu5kajZ4sO3hhqdfrXWwf4PdYFUDClsUtuudW0UbMFIMKYGOEQ9WARb78x1lziOG_8Y6YbYBlESw5irZIvTvgAE1825wyaZct-BDTGs_DvUHV17zh_FvlP2f_eIipCFQLIOqCPgD7B6BTUzI17vV4SHsI1D-H9snb8G9zdaYPdBXxIARP03NRvhv2QDbFzULBWzc9qOMTMgqmNHBxuf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: فرزاد جمشیدی درگذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/131023" target="_blank">📅 11:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131021">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cXrNe_wiUBLzabasoJWIVMuHxh9Mss2BULABS6HtEN7DW_tTailWcmGR4XSU6ukZ1iCuo8V8fvbpgE8FshKDLim2mAikg2_Sdwbc2NL1tL5A0qLH5QgLzlR1oSQFTjcm1ZpFKc4X3uJmcL81xLM235ripDoR2JijcfnIbOOXZVfgpxZMipSgkshcH2QVHb0pnU7SgxBznV1VeY4D0_lgaKbZftECg7tY-AiynaVHLHbMk8dL1D_irKU-NJg9BtQVY6MbvHR1ch33y1xcsSRgFmlQXcduZmmBoDxZsYGcRsAjTtZMurQ4qi6dkPO5g_omTJDjn2kbtwgSzv06y0F5Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/brEdgieIaxUFmsd9MDGadnofD0yU1YY6dfOZZ7I7r4rnRjGkmRwwEn2AMtSaPG1xU7tVJbVRAo1XRKvVgNpNKqfeAmN56dl3Qvvdh98V-WpMVcMDilsPinUv-elLP3eK7igEKQXaJlpVapzVgttXUvywkMkxenzOnjIV6NOkdDl2zbHkCufFGAaOPfeS1cenB2cJoiONtZPOa5CEGUwbK-qgnqvsMt3DFsQEJU7Q2AVrnYZDRvw14b0QPNhTEf3wU2DaEI-Lna_ARE0qGr1Evt8enZtHdd4uM36DmNLr0ptCeIwx-xXUetUf75rLb5D_YSt0nN_xTavpvYUOMTMGxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
آتش‌سوزی در پالایشگاه شرکت هالدیا در ایالت بنگال غربی هند به دلایل نامعلوم، ده‌ها زخمی به‌جا گذاشت و حال برخی از مجروحان وخیم است.
🔴
شرکت پتروشیمی هالدیا یک واحد اتیلن با ظرفیت ۷۰۰ هزار تن در سال را در ایالت بنگال غربی هند اداره می‌کند که بخش عمدهٔ سهام شرکت متعلق به شرکت خصوصی در آمریکا به نام «گروه چاترجی» (TCG) است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131021" target="_blank">📅 11:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131020">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
واتس‌اپ به‌زودی قابلیتی جدید ارائه می‌کند که کاربران را از اشتراک‌گذاری شماره تلفن برای آغاز گفت‌وگو بی‌نیاز می‌سازد.
🔴
بر اساس این قابلیت، کاربران از همین هفته می‌توانند یک نام کاربری منحصربه‌فرد برای خود رزرو کنند تا پس از عرضه رسمی این ویژگی در ادامه سال، از طریق آن و بدون تبادل شماره تلفن با دیگران پیام‌رسانی کنند.
🔴
این قابلیت که از سوی شرکت متا، مالک واتس‌اپ، ارائه می‌شود، با هدف افزایش حریم خصوصی کاربران طراحی شده و یکی از مهم‌ترین تغییرات این پیام‌رسان در سال‌های اخیر به شمار می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131020" target="_blank">📅 11:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131019">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: من به ارتش اسرائیل دستور دادم تا خود را برای عملیات «آبی و سفید» در ایران آماده کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/131019" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131018">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وال استریت ژورنال: وزیر امور خارجه آمریکا، مارکو روبیو، موفق شد ترامپ را به دیدگاه خود قانع کند که اسرائیل باید در لبنان بماند و به ایران حمله کند.
🔴
معاون رئیس‌جمهور، جی دی ونس، مجبور شد عقب‌نشینی کند و او نیز حمایت خود را از توافق اسرائیل و نه آمریکا اعلام کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131018" target="_blank">📅 11:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131017">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
وزیر امور خارجه عمان اعلام کرد که ما طرفدار اعمال عوارض ترانزیت در تنگه هرمز نیستیم، این امر طبق قوانین بین‌المللی ممنوع است و ما به آن قوانین متعهد هستیم
🔴
این مسئولیت ایران است که مطمئن شود خطوط کشتیرانی عاری از هرگونه خطر مرتبط با مین هستند.
🔴
وزیر امور خارجه عمان با این حال، اخذ هزینه خدمات را به بهانه افزایش ایمنی ناوبری، آمادگی برای حوادث اضطراری و مبارزه با آلودگی رد نکرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131017" target="_blank">📅 11:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131016">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
الحدث: در آخرین تحولات مربوط به مذاکرات تهران و واشنگتن، قرار است تیم‌های مذاکره‌کننده ایران و آمریکا روز سه‌شنبه وارد دوحه شوند، هرچند تهران تعیین تاریخ برای دیدار دو طرف را تکذیب کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131016" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131015">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQ6PKGI85r54mRmziPRqpTsroOU_elU2j1AD5rHM8h44TW-TwTaq2vWrSBb8JhOzshQCjLghqo7ExWXKTAoksCGyWAtg7BPipz5mKXzEZP7BpQQ6qP5FW3p8c3f6YjgpfkW9s_oy7v7_E3co_WlPLHDoawUOpJl2OmdJXBvAK1a-ourPbgHO7w15MKpDQk4DcgpB7zqVez9bz1beltNxBd4ZZHrXQKlAG2SM0s2h8oswI6KJcIQ4L4prT5lB4vO2ELfNKDjlgXnb-sf7VgjX38NU3OW8KFnm7ri3xsn0eeCo3S82OHKboSBMKeHy2WDOX2CBum0Wbyypz71FQdSwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دخانیات صدرنشین مجموع تورم ماهانه ۱۴۰۴ و بهار ۱۴۰۵
🔴
تورم ماهانه گروه دخانیات در فروردین، اردیبهشت و خرداد سال جاری به ترتیب ۳۰.۷، ۱۷ و ۳.۷ درصد بوده که در مجموع به۵۱.۴ درصد رسیده و این گروه را در صدر جدول تورم سه‌ماهه قرار داده است.
🔴
نکته قابل توجه آن است که الگوی تورمی سال جاری، مشابه روند سال گذشته است. بر اساس همین آمار، مجموع تورم ماهانه گروه دخانیات در سال ۱۴۰۴ نیز با رقم ۷۲.۶درصد، بالاترین میزان افزایش قیمت را در میان تمامی گروه‌های اصلی به ثبت رسانده بود و این گروه برای دومین سال متوالی در صدر جدول تورم ماهانه قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/131015" target="_blank">📅 11:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131014">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENf3SokveGjdFEfO6hnmE17LP6GpQJuP7Z1VaF5rlcXZyn0CS306d5mYViSYjzA8u0KI942wEO5LVjrN-F-mmyZ8AH-FsciMbDxtAW55jd4m3vd9nPREpxOwARXCLtCb20VqDBYFwztmpHlx9lMbCIcbmweO6JhPyRKI1pRUdpJjHwfEHb7Bq4fmwQ4RiZ3o0DjAl_fJZm-UIZoNp6F-Q3_3JkFG0LPuebX2k5dAAZvdEnwM8dRMk2_tRjHaF4ClK9vgmueihpP4aSg9ZzFgmfBe8KtUTjJLL58shpke9tIbhtISkt4h8jS6ZPjq2Daind2de-nmD_8dbmpO4oY36g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ سپتامبر ۱۹۴۴ عملیات مارکت گاردن و فرود چتربازهای بریتانیایی و امریکایی در هلند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/131014" target="_blank">📅 11:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131013">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1gTWCZqaPqk8alR3nDmrvPJoEI53SSBpfGcsLH8EHcHC9pf43W6D-NA-B0cd9RT3Xk7lWtaoQAEJkvQdbmwvDKTgkulHiXhZZZdiefXOqPAqohpXEUBKaXZRgsOHILKhSbmI1RP5_uGCgYhEoNMwOiSvsbwf919dl8q-fAJvfTltmFZldgjOcSJCVvF825zeunWjR4dtoNw9yG0WcPrRCh89dVXGc3voSlyW4yMDHLGxYySXtoBN71CRYjp9tdCdfXt5GKiFTZx8Zvtj1Rxe1BDnFUljr812rIBHwzKHkzOZN5fjcGkKYSCLUF9HvtwJSUO1vEf5-hSwL2VxTdxQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ونزوئلا: شمار قربانیان دو زمین‌لرزه به ۱۷۱۹ کشته و ۵۰۳۴ مصدوم افزایش یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131013" target="_blank">📅 11:06 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
