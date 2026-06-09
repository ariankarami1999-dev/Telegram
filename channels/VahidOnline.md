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
<img src="https://cdn1.telesco.pe/file/a0ULoZ2nX5qitCgeFM3ShDqbZrxcwohOPIn5ZnCF_ByX3qZXXI8XgE_xI-hRSNp55PksLAHTcokCzbmPb9TtV314_Q7EzvQjjyWynxnUaGXERGJzk7ZxFY2tCiJ97WZVVVA45ERd_I_7cWUapW15CAliRpV97-Yvfo99_-jkLkIjEZUmewr2tp0tBJ9b2mM-NMk4d9jKjuxEaqNxgTrHCjDBQTPZQlsJQmJV6E6r5SP4rXUo2QzAhUuCGDsccPKwizYM2sYsKChQeCI_33O5xyMEhH6eQeA3I2ExMkBEX-A0D33-1LVnhBme4C0bhCZBDgEAWSYZhTBPFnpTge06Mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.34M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 01:35:45</div>
<hr>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hPORqQOxprVkgjoKxbTf0clKo3PkWsLNEpoEpmT52O8NHD58v560G5Kb2W-AdVy7sTFEICftIRGrU5RSLsN5t5Z-XvEcMHOaKCxxDaLY-galGrIFPbTSwtj-3ol-A2cMqZWxdFd7x5OOsE0pvXLFxHz19V7OBFOEctfQ_9j52I4Rvag5bE8-9VS6hha-jx-f34JJUycKdstRWEKQ0oHfkONzxSI0vThPsHFz1-HG1_wBTKJibZ7fHUvNpKrfPVOGRCWlAvFk6jGgCi_HOVxQC--gYh43SAuI03yz90aW_yB2jAHrevLFgbPPNwtCbjTUodVZ-AcapR735qIQ7rOfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، سه‌شنبه‌شب، در گفتگو با شبکه خبری «ای‌بی‌سی» (ABC) درباره آغاز عملیات نظامی واشنگتن علیه ایران گفت: «من فکر می‌کنم پاسخ دادن امر بسیار مهمی است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین حالا که صحبت می‌کنیم، در حال پاسخ دادن به آن‌ها هستیم.»
ترامپ با تاکید بر موضع قاطع خود افزود: «این اقدام پاسخی به کاری است که آن‌ها شب گذشته با هلیکوپتر ما انجام دادند و من معتقدم این واکنش باید بسیار قوی و قدرتمند باشد و حملات جاری نیز دقیقا همین‌گونه است.»
@
VahidOOnLine
"خبرگزاری صدا و سیما":
سیریک اصابت یک پرتابه تایید شده اما مکان و نحوه اصابت مشخص نشده است
برخی منابع از شنیده شدن صدای انفجار و فعالیت پدافند در بندرعباس، قشم و سیریک خبر می دهند.
"به گفته یک منبع آگاه ۶ صدای انفجار در قشم شنیده شده که بر اثر پرتابه های دشمن بوده است.
ظاهراً این پرتابه ها از جنگنده شیلک شده است."
من از جاسک هم چندین پیام داشتم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/VahidOnline/76112" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HA_cdnODD1waQ7iQ5v2dmGGyUOfoclbFYm4WIGADHUj1q9h8iRdovrDbNJ6dZSkk-DWD3-whllueewlK9AUD0OYDlAB1yg9Ilj2fuMy3yMr1ip7tFkFyCJH7XSi1LnBb-fgXEflEQt08KS2PLIJfbzw5JcGjcLqTfVohxlkxCBYs0BS7ldLT_HblTi9_PPGtLBkvCr-i5WxCpKCW9orfWappfb4qeaCPsypdOWLEGSd705djbwj9apF-V0PTuOgwIb46sNT2ctTDqZL0ZXduLLeX-HZWqpjIylGQIUabCBfMP7wzw9WvKvYGx71D-gWtJFfSg-G-uzKidY347f18vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
سنتکام: حملات در پاسخ به سرنگونی بالگرد آغاز شد
ترجمه ماشین:
فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، اعلام کرد نیروهایش امروز ساعت ۵ عصر به وقت شرق آمریکا، به دستور فرمانده کل قوا، حملات دفاع از خود علیه ایران را آغاز کردند. این اقدام در پاسخ به سرنگونی هلیکوپتر آپاچی ارتش آمریکا در روز گذشته انجام شده است. این مأموریت پاسخی متناسب به تجاوز بی‌دلیل ایران است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/VahidOnline/76111" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۰۰:۳۰
صدای چندتا انفجار بزرگ پشت سرهم شهرستان سیریک
وحید جون سیریک صدای  انفجار اومد
وحید بندرعباس صدای انفجار میاد
چهارتا انفجار سیریک هرمزگان سه تای آخری کناره های ساحل
وحید بندرعباس صدای انفجار اومد الان
صدای سه تا انفجار شدید از سیریک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/76110" target="_blank">📅 00:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ep5lf03Uy2W_3b2oKCxwe-pndW-xhTCxVDHQVRYz8J3EHy_Rz2Mw3xzGI96ld7ZubTSjjNmUnFDktrxmB_45_p6i_LJf0tST9o1MiIfEgve8rqiR0ofwUWrSVbZbf6qbDRFQ_JtSQrfbwBxHc1RvJ3_GcxwKk0zDp11HHq5IX52-X4ci5a75MThPPxQi2PnbmwiTuw5O7EQLSg4KFgarbboE3uMfqRY5kzk19TqkyiS-j1VUnafjw_uqRT9Fe7iZ0IrL_Iak95rab_CkhD3PDkp7kp74tE3diJbYwfx4mbisqJ3Us7vzbe_jgl9lrcIoElGZLX1fe-8AW1SQUksPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، به نقل از یک منبع آگاه نظامی نوشت: «در ۲۴ ساعت گذشته هیچ عملیات نظامی هجومی هوایی در تنگه هرمز انجام نشده است».
@
VahidOOnLine
پیش‌تر خبری بدون ذکر نام پخش شده بود که:
معاون وزیر خارجه جمهوری اسلامی ایران، روز سه‌شنبه، ۱۹ خردادماه، در گفتگو با «الجزیره» اعلام کرد که هلیکوپتر آپاچی ارتش ایالات متحده که روز گذشته در تنگه هرمز سقوط کرد، به طور عمدی توسط ایران هدف قرار نگرفته است.
این مقام رسمی با تاکید بر اینکه ایران پشت این حمله نبوده، در عین حال هشدار داد که به دلیل شرایط به شدت ملتهب و متشنج منطقه، ممکن است بروز چنین حوادثی در این فضا «عمدی» تلقی و تعبیر شود.
همزمان، دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با کوچک جلوه دادن حادثه سقوط هلیکوپتر آپاچی گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/VahidOnline/76109" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gJevVMV9h87aSuJ5su3CUyQZ8QyUO1-CXZsOKRrAPJKe8zVxHhSN0-YQqlMGOZe_MY73jGKubwDlubdTiIXyPHSpriwQzdI1waNJQYoZ6siixrpN3GoNmsENZpLhyEYApDIldnh6jwFuzOXMJeRdBXS_iRLr_UJt_9CtU2vAZtZL1Rr53t720UO8V9kgakQ7WeyMDixUPn_E8SIlFJwNpvpXEA5FUB7RJd2IaBgY70oTVp6tr0hKFidI_GBL-s_2ZQLSirwA8bw6Q4XG1vfP8qKKYZDmiPrKr-SwEvyU2vwyyMRfPycGuGzPtAzJZ_4zptf_95YAXYFWFp6IMDMbdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PXqqxlSGzzUXlNLr4eyJEE4AuOSUjwPXZhhRJUOvWAwn8c4dUoC26d8ONWxWdHFs27T7KM7V52ePJKSiIlvzjvasdswk0pPaprzma8hVNUqEqzdC0tSqpi3541jlGpHVDbDvoC_luqiORpbUFgQF6mLTyWhSrXa9zcdFiQ6_ksmJr3On2WBYREFEzZ32kGY_LgGNI-k_u8e9LQayxG4xonIeLyJX17ugnKLzgETQcCwtx-FrkK0JjhZ-VcLTuXscBq53kDWULP_MqAbuKQY-7hU4Hq_o4c18DQ-bsAmhhu7IK6u-8ZGTVDOkHMGfDqkH4sUkcTc20dr5imZaFlrJww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگوی تلفنی روز سه‌شنبه با روزنامه «وال‌استریت ژورنال» با اشاره به اثرات شدید تحریم‌ها اعلام کرد که محاصره دریایی بنادر ایران باعث شده این کشور «بسیار فقیر» شود و واشنگتن این محاصره را تا هر زمان که لازم باشد حفظ خواهد کرد.
ترامپ همچنین با کوچک جلوه دادن حادثه سقوط اخیر هلیکوپتر آپاچی آمریکا گفت این اتفاق «مسئله چندان مهمی نبود» و تأکید کرد که «حال خلبان خوب است».
بر اساس گزارش سنتکام، سرنشینان این آپاچی پیش از نجات، دو ساعت را در تاریکی شب روی آب سپری کردند و یک مقام ارشد آمریکایی فرار آن‌ها از این سانحه را معجزه‌ای همچون «دست خدا» توصیف کرده است.
@
VahidOOnLine
وال‌استریت ژورنال نوشت که حادثه سرنگونی بالگرد آپاچی در تنگه هرمز برای ترامپ «کم اهمیت» بوده است.
این در حالی است که پیش‌تر ترامپ در تروث سوشال تاکید کرد که «ایالات متحده ناگزیر باید به این حمله پاسخ دهد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/VahidOnline/76107" target="_blank">📅 00:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LXOkTSZDfCM5P65vBD-yRJGv4-eMONhxIuc42BdPm0w3r6-ouA2s91SQPr5PJT23Mc5-TzgAYnol8SgjVk6hqtuQrReW0FvLUcAx8tB3IU4DyZi5ykAUC-k725-7c4C6y-LBfdyqYkRmxT2PZj3xWzUPHQy3WZJb_LXE3OqE3aPzrt2cHVxfH2ZboFxmPP7JQrrOH_J9zUw7NjIFSThdqCMxxq6AZaXWZjdsUNFYlaOGXwVAtMDZ1tqXoTYuSjpXn92tfk94_W8IoMY7LkhVI8glYQiseYWEKxoi6kf7QR6PxJeEdPu3TIEaixVkteN93faA6NqeHZb2WVRn7c6iYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عراقچی، ترجمه ماشین:
نیروهای خارجی در نزدیکی قلمرو ما همواره در معرض خطرند؛ چه به‌دلیل خطاهای انسانی خودشان، چه حوادث ساده، و چه احتمال گرفتار شدن در آتش متقابل.
برای کاهش خطر، بهترین راه‌حل این است که آنجا را ترک کنند.
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگری را هم بلدیم.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76106" target="_blank">📅 22:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/spOQ1ik9CPP3wK9T3k_oQd3HrS26U0Q8hSnf26HI990kwb1ryJYQjYZl4FfSC0XbY3q9vDb0t2HNJmiWjaCZuynWdFE2W9JhJGnZvoVZjEHUn2Oc9b7On2N9YGEcesxo45QnwoThrIPCRlqcs-o49UtAxy-d4hDlzPwNdHlWXW_GAwTv9ynTM4lVgFYJrEMPoUfxP19sXCOs0pzy_wfQmPRF-sr__3JWXlOh6jtNT_weFl-EaWBrYgWpdXqgtBgLiSkY2lvhE9GCgbHHPzOEBjHjMWlLN9OKBl0YLag2DjFZVa7naGJO0IVx_jrPSLLiYzAoTSqnK9OsNnNYoy_gag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری سی‌ان‌ان به نقل از دو مقام آمریکایی گزارش داد که هلی‌کوپتر نیروی زمینی ارتش این کشور که در سواحل عمان سقوط کرد، توسط یک پهپاد ایرانی سرنگون شده است.
یک منبع آگاه دیگر  تایید کرد که یک پهپاد از نوع «شاهد» به این هلی‌کوپتر آمریکایی برخورد کرده است.
یک مقام آمریکایی به اکسیوس گفت تحقیقات هنوز مشخص نکرده که آیا این برخورد عمدی بوده است یا نه.
😱
‍
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76105" target="_blank">📅 21:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F8ARwItN2DuxoPGrYluy2y1Ehk8R_J5Ss9vuGjkFnHwvEWTYXIskoubVe0oSWGNHCHQA2QVOEv6MkxEoqNipY2xhZM5-diH6CRTeAYQo_e__B_7C6ub07BV5xA9f-2NR5qBK_6DvlzdfWLyRFCl5JPmzZrlPk-zSNEmDttzbjvh2hP9lsBvwYy5nPcWvYxjwCZPENFMWtu48MPADVrz1tkyxkDfM3SiTnGzn32CzwayH7pzaJsKPA5Ac9YYFu2L_vyZr9LAqgUWMTLbHlAXqsH79ezJV1tfWkJP4SsOPWlZCvxYBkcPazvaQh5CrRtGg7MZCyo5lyJ1fY_D7LXPj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت قالیباف، ترجمه ماشین:
ما زبان دیپلماسی را ترجیح می‌دهیم، اما به زبان‌های دیگری بسیار روان‌تر سخن می‌گوییم. تعهداتتان را زیر پا بگذارید، آن‌وقت ما به زبانی روی می‌آوریم که در آن بهترینیم.
خودتان بر اسبی سوار می‌شوید که زین کرده‌اید!
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76103" target="_blank">📅 20:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KsUj1L8t9W7rsoUv--y2F8KEqZodjmtbkSwGzO5I8mn_kKKxTF_eMDhDPp_Y9Zbpf_9vjLE19FOjKKeaj-1aPI0J1mVEWE7T9FWxgBYuzKlQ7p4Vp8q8QvyIEu8Zvy1KhzBXQ2zV83ccs07eoVbSm_R2MLiQtbRrxucXy_3FE0Sk58-X4tMUPTCIveLlHyIjYce3uhhDu1xiRrqppwU86120ibmVk-uhOm1GbeIG-VxVy7uArxGdizA8SPJgimIGnNR0Q-xewY4dVnFLZIxOSXipgZaafK6Wv--OBNCanRMggb6xqcPIzFtZBT4N2zlwszZ0WaKVEGmZovZ0ck5nFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ: ایرانی‌ها بالگرد پیشرفته ما را سرنگون کردند، ناچاریم پاسخ بدهیم
ترجمه ماشین:
به‌تازگی از سوی ارتش بزرگمان به من اطلاع داده شد که دیشب ایرانی‌ها یکی از بالگردهای آپاچی بسیار پیشرفته ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کرده‌اند. دو خلبان در این حادثه حضور داشتند که هر دو سالم و بدون آسیب هستند. با این حال، ایالات متحده ناگزیر است به این حمله پاسخ دهد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76102" target="_blank">📅 20:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXsmDhodT6bQ7pJz4mOnhnZW6JeBvZFGxgp3MsYtLEMoHv9muQSYZViMi7Hx2yKCq2lhoBUheljvpTVCVxsZGDeRF7cFB7Tc_aYJnHjPoXvsrlsjGP2yPf_g8mzOrYR7c95VWipTn_Q05c8C57wzHJwVzCD-wra88etgJ3vOnHraZMOjU0TA-k_fcJcQPlSoLtztejo-I7ZxiDS2Ny5yWB4_dnz-BVp3wQ3aELQGm0hRLQUzq5oXEoN9Nvtb92sAyRtyUeST7xDDCtcN9FFslMIuSkIw-P5v8VJztMvxgrP58Z82D_3BbdQCoB6MofeSM6fsjLjtQRSpEwr-n7DCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f396691769.mp4?token=gwZUtaSpQ-6tzxKTkHX3wr4jBO-PAgdf-yohMiFcUj7bOglXQywrMZ8xppbApAH8qKm83Pv6ubcdENKUut8_qBQv_yQNKga7lzX2wUsyPBWXh9Rd3EBj4jUOo_cLmFZBli-Ja8FYozX5TcaVEpXUYRJFVtFGgthHFGIWYTPc0bOaJx52Xfbf-mwQEcYrT1d-V935XFnEeY5Xy38Jq-6WT-YUprwyZ2ixNvPEDYVnudN9BZKSigYvCq8RXyae1fkpdJ2ppt36UJVUf6v1btQBRETk24gQlWTeDKiaHMEfmw5ivl-y7tvNhN6IpZb_iZCFRbRFrQhOTQ_YMTPDJ7sB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f396691769.mp4?token=gwZUtaSpQ-6tzxKTkHX3wr4jBO-PAgdf-yohMiFcUj7bOglXQywrMZ8xppbApAH8qKm83Pv6ubcdENKUut8_qBQv_yQNKga7lzX2wUsyPBWXh9Rd3EBj4jUOo_cLmFZBli-Ja8FYozX5TcaVEpXUYRJFVtFGgthHFGIWYTPc0bOaJx52Xfbf-mwQEcYrT1d-V935XFnEeY5Xy38Jq-6WT-YUprwyZ2ixNvPEDYVnudN9BZKSigYvCq8RXyae1fkpdJ2ppt36UJVUf6v1btQBRETk24gQlWTeDKiaHMEfmw5ivl-y7tvNhN6IpZb_iZCFRbRFrQhOTQ_YMTPDJ7sB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طالبان به تجمع مدافعان حقوق زنان و مخالفان حجاب در غرب افغانستان حمله کرد
AngelaGhayour_
مقام‌های امنیتی افغانستان روز سه‌شنبه ۱۹ خرداد تظاهراتی که در حمایت از حقوق زنان را در ولایت غربی هرات برگزار شده را متفرق کرد.
این اعتراض پس از آن آغاز شد که پلیس امر به معروف طالبان گروهی از زنان را به اتهام نقض قوانین اجباری پوشش بازداشت کرده بود.
به گزارش خبرگزاری رویترز، شاهدان گفتند که در جریان حمله طالبان یک نفر کشته شده، چندین نفر دیگر زخمی شده‌اند و ده‌ها نفر از جمله زنان و دختران بازداشت شده‌اند.
..
به گزارش رویترز، هرات که مدت‌ها به‌عنوان یکی از پویاترین شهرهای اجتماعی و فرهنگی افغانستان شناخته می‌شد، دستخوش تغییرات قابل توجهی شده است.
...
شاهدان گفتند اعتراض‌ها زمانی آغاز شد که مأموران امر به معروف تلاش کردند زنانی را که با الزامات پوشش اجباری مخالفت می‌کردند بازداشت کنند.
برخی از ساکنان گفتند مأموران حتی زنانی را هدف قرار دادند که از پیش نیز پوشش مورد نظر، شامل پوشاندن کامل صورت و بدن، را رعایت کرده بودند.
@
VahidAfLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/76100" target="_blank">📅 19:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76099">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M0hTVGzhAom7OQxwSBTnc6-D0bZJ1UD9RuQboj38Ew9EDA961NsTKyUlYCCwkKtUFz-Nmlf0pOgnIJBEuq56V3puBONbJyljjwf9ZxzUBKSXDkkgXrnocF1F7q1QdiwQo1igLo7b2n2T5G0a997q63kyW2Xo-Hm_sBs7JxCsn7w0gd0GI2QEsrUEFjf_jCH2fUt_KwbMkS8Iwmf6bwd4Sok3HPIgBWTJjlj7g_BYpCqUlBqysUigFyIuFP3uOVjFcXfqEYdPTLBeVdFVp96ou66YPeTjhrvVkQMJWvKvXayoRR1D5Mtg5m9wUyhSabi9itG-HXa5ttGTn5JkPz7vWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا پیغمبری، جوان ۲۶ ساله و از بازداشت‌شدگان اعتراضات سراسری دی‌ماه ۱۴۰۴، توسط دادگاه انقلاب تهران، بابت اتهام «محاربه» به اعدام محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/76099" target="_blank">📅 18:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/677a13e326.mp4?token=CCI-o-Lw0fXTRK5TpDMqZ50OviALaYLDkHa56tHGsyvhEG9fhL-9vJFBdevJ7B8zl7Qvb8jUcts-zuAGYCR4M-mONbMICGcKMDDxKKM8ZAEaCd8npZnCOwhxN7kDSKMcG8m2kabiS870lcnzyDb55DLVLySoei6b3ZblzykT1Y1wxwpiwFmKDWmDi8SQLlGdRW6V3vyuA7BjMvKBhDdaXgD69IBmNBdoz6aSrwx1iX71hjqxhhb6tf7ARXv4HrzYjuIcu9yhh9dKhe0ljt9kjtBLUs79cBvd4R_co9mBIxOpzjkH7FWe5dl-nU8gA_5Zn7g_yKFGcxYGY5Ql2Q0wuA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/677a13e326.mp4?token=CCI-o-Lw0fXTRK5TpDMqZ50OviALaYLDkHa56tHGsyvhEG9fhL-9vJFBdevJ7B8zl7Qvb8jUcts-zuAGYCR4M-mONbMICGcKMDDxKKM8ZAEaCd8npZnCOwhxN7kDSKMcG8m2kabiS870lcnzyDb55DLVLySoei6b3ZblzykT1Y1wxwpiwFmKDWmDi8SQLlGdRW6V3vyuA7BjMvKBhDdaXgD69IBmNBdoz6aSrwx1iX71hjqxhhb6tf7ARXv4HrzYjuIcu9yhh9dKhe0ljt9kjtBLUs79cBvd4R_co9mBIxOpzjkH7FWe5dl-nU8gA_5Zn7g_yKFGcxYGY5Ql2Q0wuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه شب هنگام بازگشت از نیویورک به واشنگتن، در گفتگو با خبرنگاران اعلام کرد که ایالات متحده به دستیابی به یک توافق بسیار خوب، محکم و قدرتمند با جمهوری اسلامی بسیار نزدیک شده است.
ترامپ با رد وجود هرگونه نقطه اختلاف بزرگ در مذاکرات، گفت: «اگر بخواهید حقیقت را بدانید، شانس خوبی داریم و باید بتوانیم ظرف یک ساعت توافق را نهایی کنیم.»
رئیس‌جمهوری آمریکا با ترجیح راهکار دیپلماتیک بر گزینه نظامی هشدار داد که بمباران ایران در مقطع کنونی، به قیمت جان انسان‌های بی‌شمار و بسته‌شدن چندماهه تنگه هرمز تمام خواهد شد و فرصت توافق را کاملا از بین می‌برد.
او با تاکید بر موفقیت راهبرد واشنگتن افزود: «سند امضاشده نهایی، کارسازتر از بمباران خواهد بود. ثابت شده که محاصره دریایی اهرم بسیار قدرتمندی است و بسیار قوی‌تر از بمباران عمل کرده است.» ترامپ در پایان اشاره کرد که ترکیب تهاجم اولیه و محاصره، ضربه سختی به اقتصاد ایران وارد کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/76098" target="_blank">📅 17:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta6C1AhFROjynFropgZs9oidjj_ho5xYptgdJw5AEveRb9tCIpPe0EU2DkymfTAwwn_69gTAvuT0TzuKw9FOLuAg5ea9bAT1tU6E2HPz7BbIiZ1vh6Hc0mRTVm_dfV0k4qXwpx99r7a4ePl3huCoijs83CU2AnllGoYXUt13oyfheoGMLG0Vacrw5dgY5BYDKUo0fVpIy6AZpva3xRUBZBVLv7kLHPMf0tS5_WhU1gzElDxw8E_R21u9qvp8ovrrhgwnRd_m93ute_SlGjYprX_IrKrOC5yqsBXZnurMgghQH1b8TrOTZIJCHeEUQS624oXtco7TNVOHMsyQ7UEp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو عضو نیروی پدافند هوایی ارتش ایران در حمله دیروز اسرائیل کشته شدند
تاکنون در حملات دوشنبه و سه‌شنبه اسرائیل کشته‌ای گزارش نشده بود و ۱۵ زخمی اعلام شده بود.
ارتش اسرائیل دیروز گفت حمله «همه‌جانبه‌ای» به سامانه‌های پدافندی راهبردی ایران کرده است.
بنابر بیانیه‌ ارتش اسرائیل، در جنگ ۱۲ روزه پدافند ایران ضعیف شد اما بعد «سامانه‌های پدافندی در نقاط مختلف ایران» مستقر شدند تا توانشان را بازسازی کنند که در این حملات این سامانه‌ها منهدم شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/76097" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oHYNSaIK4Qi7SL7U8RPx134nvMMZMI9TYQ-rFfid9o7FAWCRhy464lZGl-dVZfSsu4z3JWPXLbZqFyMnGLuc0CrtKLckgpI-nUtDjJSLjRyMBJnJfCD1XHVvrWsJk1KMSuxiwmonGRVWyDLlwtDKZMBKYKcbB0aKp-y_vhroVIr1E0ZLh_lC9j2PlNf7lJ9d6vM-IgAGr6QuFRkISYDBg0p_rAMrTlQDyoxJ7JVo6S2-Lx0LPTZflCavhL4OFJR2yHYKYFZybGD5D1EQLopSeguWST-qlefNypAjfXsMrV-eKN2Q8v8KHL7wkDZrudo1eExB6wJDxvNz3MrffPhm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا، سنتکام، در بیانیه‌ای اعلام کرد دو خدمه یک فروند بالگرد تهاجمی «ای‌اچ-۶۴ آپاچی» ارتش آمریکا که در نزدیکی سواحل عمان دچار سانحه شده بود، توسط نیروهای آمریکایی نجات یافته‌اند.
بر اساس بیانیه سنتکام، این حادثه ساعت ۷:۳۳ عصر به وقت شرق آمریکا در روز ۱۸ خرداد ۱۴۰۵ رخ داد. این بالگرد در زمان وقوع سانحه در حال گشت‌زنی بر فراز آب‌های منطقه بود.
سنتکام اعلام کرد دو نظامی حاضر در این بالگرد ظرف حدود دو ساعت نجات یافتند و در وضعیت پایدار قرار دارند. این نهاد همچنین افزود که علت وقوع حادثه همچنان تحت بررسی است.
یک مقام آمریکایی به شبکه ای‌بی‌سی گفت دو خلبان این بالگرد پس از سقوط در آب، توسط یک شناور سطحی بدون سرنشین یا پهپاد دریایی از آب گرفته شده و به خشکی منتقل شدند.
به گفته این مقام، پهپاد دریایی مورد استفاده در این عملیات طراحی مشابه یک قایق تندرو داشته است.
@
VahidHeadline
هنوز مشخص نیست که آیا این هلیکوپتر بر اثر آتش نیروهای ایرانی سرنگون شده، دچار نقص فنی شده یا با مشکل دیگری مواجه بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/76096" target="_blank">📅 17:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76092">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EgNZVczGrfeD0pGCHJgXFYtaMwvri-F9fyjY_DBzUBW6AkGnKaNCaAoh3kQEAR3QSqbxqrzKE_wQT0bsv01pn20eTrBC--hTM70EoKWtr04FzfZMIy1UDNQCqmOizcf9PdDVZZxVfjoqK1BTzQnqkrA8OhkdVeQ06Px77xoQg37gcYKS7-IUCPwPrIbOtQniAXQ4TOrZD71WQq6kldi2ifXRQp42agGkcaIXafU62SKZ9WyQjoQaA_jQ6Y70ed_4r5P9daSbPV0c9AVcR7Zl-twfVcbQoM_n_eJs-hiQAtwNAbuC64afKtXUmBTJf8nvzZzTSLX2xhnE2VHtqjFwRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJopRTIHM8loYB5NmG2fpyZsqZBPYthexAkDkBkYJc97VkHmTa3zlbjZrmeNdJ4FZe3dgAT2gVdCA0iA7NChi4EKD5uVdOQuGiFOy5TLThEOEYsdb0N5ifaKW99c-rRKpzFhH1GiIv_Kh6zKKkKetRaBVWjZ41SYFW7D1B48HFjORUjkvS6pWyOEiDW6v54Llx6HjPhAo-8kf8oC_V94Ql6Bgwh6KZjTnJqQ3mqn43VkgP5PX1DvlcIGRYeQSmXW0PS1JVTIAhDOj46TIlmOjCT9B839qImAd8mPMIysAUOah8AEqagk_9Q_fMP7qcBTWL5vl_La0mcxQTOPa3GDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NYA516Uk9VuL3_XnK-PcZzNmHr4j6zS0cH5DO87shj0Zvy6shgOPAQMOfmwJ8k8Lk2TszbenGhcXLiviNRp9samwIfs2Z1fZWVokF381oErqr4MyIpLtK6pwIp0eeDUcK3iT4xihv1Ifaucf3hSDwXGR-KkbQ9_J1yYRLzv-B_5SFXxN7p8CF29Ux-n3VPr9bePbHMyefPNMMqMj06kE5AzEslrUi_gqMuVlCk_NWNKZzbxxHe4A33kBSUw5hRyCD6r5fjHfE_cFJi6xc9EEqqUsNJFykJkZFJkJuBNY0iE4KesI2aBg91VztXV2uLRSEEIOqptLQAyMHvyNf_nMRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8642136842.mp4?token=G0tk89foMeuO5C7y6M-t8rPsNBrJZph3eZC4EoJykS1xbh4bb0Zir4OdirzJvj_JbitocxIpUsEJKgyWjh0qiHVpD8dV3G0Nmx3-etcbGtnCY260JBXIbHlEjOQvagiZZHtpmu83lKyoplXUF4xLcBXMyuWgjFfDfOtI3--1INDe0KvVdUv8rt94b8fg4htapiaRRkpYJMJKBV-784FzpA2JQA8i8Fakvf_Pl8R2jWPRcaVCKIFpcw8VqQyOgVk2i_R9ex6TNRJX1laLe84Qb9-bQpT140LBqUjKQA7YIV0O-B55AccCFAc7r6eMskjWASSs2dgZq9kpeEoE5bTIJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8642136842.mp4?token=G0tk89foMeuO5C7y6M-t8rPsNBrJZph3eZC4EoJykS1xbh4bb0Zir4OdirzJvj_JbitocxIpUsEJKgyWjh0qiHVpD8dV3G0Nmx3-etcbGtnCY260JBXIbHlEjOQvagiZZHtpmu83lKyoplXUF4xLcBXMyuWgjFfDfOtI3--1INDe0KvVdUv8rt94b8fg4htapiaRRkpYJMJKBV-784FzpA2JQA8i8Fakvf_Pl8R2jWPRcaVCKIFpcw8VqQyOgVk2i_R9ex6TNRJX1laLe84Qb9-bQpT140LBqUjKQA7YIV0O-B55AccCFAc7r6eMskjWASSs2dgZq9kpeEoE5bTIJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از برقراری تدریجی دسترسی به اینترنت در ایران، ویدیویی در شبکه‌های اجتماعی منتشر شده است که فرزند جاویدنام نسترن زارع‌منش را در حالی نشان می‌دهد که پشت پیانو نشسته و هم‌زمان با نواختن ملودی، یاد مادرش را گرامی می‌دارد.
نسترن زارع‌منش، ۳۹ ساله و مادر دو فرزند ۱۰ و ۱۵ ساله، ساکن تهران بود که ۱۸ دی ۱۴۰۴ در جریان انقلاب ملی با شلیک گلوله نیروهای سرکوبگر جمهوری اسلامی به سینه و گلو جان خود را از دست داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/76092" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76091">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PrfAT11O5ozS61N8kEYAHnvDNbIxv_-hKesRf-KQHxgAFprPI4wwllULLB9-iMCHiDMvgJ-8ndyyerbNkhPiimmYWaMUBNauiqIdbpENsh91X_8QiAoFMfFxtFIpCvr61B31pHoT_cQZUaSKuMlg6CEqJhgBE658r32FOCLL1v0c_5UceMk09MMDWVHr03UF6-Oj6jZJeR5idhLCFjodZwMzoLiS6pvFscO1Vb0dctoe4QtTDfJt5ZBHYkVa5a6yE9XQjP3e2LevNMjb5Rz9FzK0Iy8ULFMIdd0PPTQ7cpn3VVDjJkpsGgvTdjywfKpHPaAamf1ptP6ma0YBQvY5eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی دی ونس، معاون ترامپ، در مصاحبه با فاکس‌نیوز ابراز اطمینان کرد آمریکا و جمهوری اسلامی می‌توانند درباره پرونده هسته‌ای به یک توافق بلندمدت برسند.
او گفت صرف‌نظر از اینکه اسرائیل از این موضوع خوشش بیاید یا نه، چنین توافقی به نفع آمریکا است و واشینگتن به پیگیری آن ادامه می‌دهد.
ونس با اشاره به نگرانی درباره اینکه تهران ممکن است در حال بازی دادن واشینگتن باشد، گفت: یکی از مهم‌ترین عوامل موفقیت این توافق نهایی این نیست که جمهوری اسلامی چه چیزی روی کاغذ می‌نویسد، بلکه این است که آیا واقعا به برخی از الزامات توافقی که به آن می‌رسیم پایبند می‌ماند یا نه.
او با تاکید بر اینکه آمریکا تعهد جمهوری اسلامی به چنین توافقی را در بلندمدت راستی‌آزمایی خواهد کرد، گفت
:
بیایید صادق باشیم. ایرانی‌ها نمی‌خواهند این جنگ ادامه پیدا کند. ادامه جنگ به نفع آن‌ها نیست. آن‌ها پای میز مذاکره آمده‌اند و پیشنهادهای واقعی را مطرح می‌کنند. اگر به این توافق برسیم، یک موفقیت بزرگ برای مردم آمریکا خواهد بود.
@
VahidOOnLine
جی دی ونس در گفتگو با شبکه فاکس نیوز: موضع رییس‌جمهوری کاملا روشن بوده است. اسرائیل اهداف خاص خود را دارد، اما هدف اصلی آمریکا در قبال ایران این است که اطمینان حاصل شود ایران به سلاح هسته‌ای دست پیدا نمی‌کند
جی دی ونس: در ماه‌های گذشته و در واقع طی حدود یک سال و نیم اخیر، شرایطی ایجاد شده که رییس‌جمهوری معتقد است ــ و من هم فکر می‌کنم درست می‌گوید ــ می‌توان به یک راه‌حل بلندمدت برای مسئله هسته‌ای ایران دست یافت
ونس: ممکن است اسرائیل از چنین توافقی خوشش بیاید یا خوشش نیاید، اما ما معتقدیم این مسیر به نفع ایالات متحده آمریکا است.
به همین دلیل به دنبال آن خواهیم رفت، زیرا این همان چیزی است که رییس‌جمهوری آمریکا برای انجام آن انتخاب شده و همان کاری است که برای خدمت به مردم آمریکا باید انجام دهیم
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76091" target="_blank">📅 06:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76090">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZML2JARgSRvjm68olzvzzRD2wS0e5Ul8OlP5rxtpJ-ddwe73bQROOMDO7XqtDGIwMlOePG3YwRxfF3Ldjb-llFxh1xUoLRxXLd_0qTY7K6Hz3_1524UWgbECrvvu5bjcuLQ2SvW3Q-hpFcJiMVkhKubsb4I-836nklFuU1t6VCpoBHMfOYbQo2nSUnQMo7kZlJ5VE2TU7cL2IJaBuULQct6BOSGNhD0HwWME9JumvWSxOTbgI3OmCgnAIZLrxgVPU1QBxYA3YouvSP2g54q4aCTJ_iqLR9EQjIVnaUmYbuhSbliTyY_lawMWDv0LZCXo4DY9ooKXEhPm3i7OlhFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه با تاکید بر موضع سرسختانه واشنگتن در قبال برنامه‌های هسته‌ای تهران، با تقدیر از همراهی لیندزی گراهام، سناتور برجسته آمریکایی گفت:
«لیندزی در تمام این مسیر پابه‌پای من جنگیده و ما تیم بسیار سرسختی بوده‌ایم. من فکر می‌کنم در حال پیروز شدن در این نبرد هستیم، اما طی دو هفته آینده با اعلام پیروزی کامل، برنده واقعی آن خواهیم شد. این یک پیروزی کامل خواهد بود که بسیار زود رخ خواهد داد.»
رئیس‌جمهوری آمریکا در ادامه با اشاره به نابودی گسترده زیرساخت‌های نظامی ایران، این وضعیت را مصداق تحقق «صلح از طریق اقتدار» دانست و خاطرنشان کرد:
«ما در حال حاضر مشغول مذاکره هستیم و آن‌ها به شدت می‌خواهند یک توافق بسیار خوب انجام دهند. آن‌ها اکنون حاضرند همه‌چیز را به ما واگذار کنند و توافق کنند که ایران هیچ سلاح هسته‌ای نداشته باشد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/76090" target="_blank">📅 02:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sooMTPCcYTo7nTyBCvdtgC9uI0smz-3LMGAo53OQyzibkDc-4rCmLJMSzBivjsmWnounNX5TKD4PxOtoQdDC7emhPF_Cw-e1TDoGPEIy8c89YU7QU4EfB92S6dslx6las-ayaWT8xSD-l4x2W95RGHN8-rLdEpw1rGUgSucCS3rvzHZvOHOzIlGY6QoneX8y7ZWePPVBGgQBMPzFfQU8wSAOYwZqQXYqWFmxu7aVhT-NdgKDEqxaNqzGRYuVU3XWaFCLZnZ4bI1OysWDQPdc1QC78BwLWAC9atNVk_mZ3uOa95pF2EGPk5rgkriCFVgvEXj0SF4eOU1O4Z1p4b2gVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران در اظهاراتی جدید به حمله موشکی شب گذشته از خاک یمن به سوی اسرائیل واکنش نشان داده و آن را نشانه‌ای آنچه «هوشمندی جبهه مقاومت» خوانده، دانسته است.
آقای قاآنی روز دوشنبه گفت: «اقدام به موقع و با اقتدار یمن قهرمان نشان از هوشمندی جبهه مقاومت دارد اگر لازم شد دیگران نیز می‌آیند. شرارت‌های رژیم صهیونی و آمریکا در این منطقه عکس‌العمل جبهه متحد مقاومت را در پی خواهد داشت. رزمندگان بدون مرز مشرف برگلوگاههای عبور شما هستند به تعرض ادامه دهید گلوی شما را خواهند گرفت.»
یکشنبه شب ارتش اسرائیل اعلام کرد که پرتاب یک موشک از خاک یمن به سوی اسرائیل را رصد کرده و کمی بعد از رهگیری آن خبر داد.
کمی بعد حوثی‌های یمن حمله به اسرائیل را تایید کردند و گفتند که «منطقه اشغالی یافا» را هدف قرار داده‌اند.
حوثی‌ها همچنین در بیانیه‌ای «ممنوعیت کامل و مطلق» تردد دریایی اسرائیل در دریای سرخ را اعلام کردند:
«ما در قبال محاصره ناعادلانه تحمیل‌شده بر مردم خود و مردم محور جهاد و مقاومت در فلسطین، غزه، ایران، لبنان و عراق ساکت نخواهیم نشست.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/76089" target="_blank">📅 02:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76088">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=pX0q9EEHg5NjFj3ZlcFdByRN7GSiV_y8JkBnu391_lsN3uVgcUoOTFb4ia1Ia-e9Ohox6COGPbkIOujPvyrKmWZp0REJ0oQrMT14qaEiPKnE34GhDR2yzU-5awwbz7TWjatlspePFFOlVbrTpaGxmz7OnMqKgOtuEXpjM56I99iftl0s1VnKKsYnlQfQ_FsrJ9JPZ6ewkqRTkFJw7Uk_-cXCNPctonW7Gp7apRY6gGNrxPq_Gzdu85mqiIynJcA5ps76d_gK3g3Bukyo47IBblXS47d4UXDi2YQaz6wsV4to9grez1aRbehWIGxD3LLgKgsA6LjRwkUAzwVDGYekPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a40e8ba.mp4?token=pX0q9EEHg5NjFj3ZlcFdByRN7GSiV_y8JkBnu391_lsN3uVgcUoOTFb4ia1Ia-e9Ohox6COGPbkIOujPvyrKmWZp0REJ0oQrMT14qaEiPKnE34GhDR2yzU-5awwbz7TWjatlspePFFOlVbrTpaGxmz7OnMqKgOtuEXpjM56I99iftl0s1VnKKsYnlQfQ_FsrJ9JPZ6ewkqRTkFJw7Uk_-cXCNPctonW7Gp7apRY6gGNrxPq_Gzdu85mqiIynJcA5ps76d_gK3g3Bukyo47IBblXS47d4UXDi2YQaz6wsV4to9grez1aRbehWIGxD3LLgKgsA6LjRwkUAzwVDGYekPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناسی حکومتی در صداوسیمای جمهوری اسلامی مدعی شد آمریکا در جنگ ۴۰روزه بیش از ۷ تا ۸ هزار زخمی و دست‌کم هزار کشته داشته است.
او گفت: «برای ما کشته گرفتن از آمریکایی‌ها و اسرائیلی‌ها هیچ کاری ندارد» و افزود جمهوری اسلامی به درخواست «عالمانه و عاجزانه» کشورهای منطقه خویشتن‌داری کرده است.
پیش‌تر، دونالد ترامپ، ریس‌جمهوری آمریکا، چهارم خرداد در مراسم «روز یادبود»، یاد ۱۳ نظامی آمریکایی کشته‌شده در جریان جنگ ایران را گرامی داشت و گفت آن‌ها جان خود را فدا کردند تا اطمینان حاصل شود که ایران «هرگز به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
"روایت فتح"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76088" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76087">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">زمین‌لرزه در هرمزگان
پیام‌های دریافتی:
سلام وحید جان
زلزله همین الان بندر عباس ساعت ۱۲:۴۰
آقا وحید بندرعباس همین الان زلزله اومد
قشنگ زمین لرزید
00.39 بندرعباس زلزله شد
زمین لرزه نسبتا شدید ساعت ٣٩ دقیقه بامداد بندرعباس
داداش همین الان بندرعباس زلزله‌ اومد
🔄
آپدیت:
‌
خبرگزاری فارس: زلزله‌ای به بزرگی ۵ و در عمق ۲۲ کیلومتری زمین، منطقۀ سرگزی احمدی در شمال هرمزگان را لرزاند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76087" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76086">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPscJAwfqru5w-ClTr0RY1Ngdh5j0q9KVS7tvNtI-_48eH_YOz1qR53-vu8pBrUW86ZQA2Zy531TTFolNT_W4emY_rYDxC3gvTVGva2pHBPXUndCkfuaGrkpS_HLslXCWVFh-IyOB3bdVUMRDErXULnUKPoufGnftHsBEzn1m3a9OySxQw6ZV_pdqIOpTAE9ikYBsb8z-isde6IrFS57FhEvaJYvGP_UetTizHtQmQWZlL6W714YC9NgFpsGUyA9X9kmBSKVuyNEfPzPxcn4RawMLcHu2ude5gT_L1dsNrZ9AJoY1qWSWhUq5q6RUp24em_ven1rkpvLdDTZi09aiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سارا اسمیت، سردبیر بخش آمریکای شمالی بی‌بی‌سی، در یک تماس تلفنی کوتاه با دونالد ترامپ درباره گفت و گوی تلفنی روز گذشته او با بنیامین نتانیاهو، نخست وزیر اسرائیل، پرسید.
وقتی از آقای ترامپ سؤال شد که آیا نتانیاهو با حمله موشکی به ایران در روز یکشنبه از درخواست او سرپیچی کرده است، رئیس‌جمهور آمریکا این موضوع را رد کرد و گفت: «نه، نه. موشک‌ها از قبل شلیک شده بودند. آن‌ها از قبل در راه بودند.»
او سپس افزود: «اگر به او بگویم کاری انجام دهد، انجام می‌دهد.»
این تماس کمتر از یک دقیقه طول کشید.
در بخش دیگری، سارا اسمیت از آقای ترامپ پرسید که برای متوقف کردن حملات اسرائیل به ایران به نتانیاهو چه گفته است.
«تنها چیزی که گفتم این بود که باید از عقل و منطق استفاده کنیم. ما به امضای یک توافق بسیار قدرتمند و بسیار خوب نزدیک هستیم. بدون سلاح هسته‌ای، بدون هیچ چیز دیگر.»
او ادامه داد: «می‌دانید، باید از مقدار زیادی عقل سلیم استفاده کنیم. همه چیز خوب بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76086" target="_blank">📅 00:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
وحید جان گیشا یه جارو زدن یه انفجار وحشتناک بود
[از روی صدای یک انفجار چطور میشه تشخیص داد که دلیلش حمله بوده یا چی؟]
وحید جان ۱۲ و ۱ دقیقه صدای انفجار خیلی خیلیییی بزرگ
گیشا
سلام از گیشا
یه صدای خیلی بلند انفجار اومد
همین ده دقیقه پیش
همه ی همسایه ها اومدن دم پنجره
نمی‌دونم چی بود خیلی عجیب بود
همه جا لرزید
📡
@VahidOnline
۲۰ دقیقه صبر کردم ولی پیام‌های زیادی دریافت نکردم.
آپدیت:
ما وسط گیشاییم و خونه هم ساکته، کوچیکترین صدایی نیومده
وحید جان راست میگن دقیقا ۱۲ و یک دقیقه در گیشا صدای انفجار بزرگ اومد،اما فقط یکی و واقعا نمیدونم چی بود، ضمنا برخورد به زمین و یا عمیق نبود.
من گیشا زندگی میکنم ، با اینکه امروز ظهر هم گفتند یک جا یک جای گیشا را زدند متوجه نشدم
حتی الان هم که پیام گذاشتی داشتم می‌خوندم اما متوجه انفجاری نشدم
من گیشا هستم چیزی نشنیدم
آپدیت:
بعدش کلی پیام دیگر هم در تایید و تکذیب شنیده شدن صدا دریافت کردم ولی چون بعد از انتشار پست بودند نمیشه خیلی روشون حساب کرد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76085" target="_blank">📅 00:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gzsmHCTqI_E865F8mn33D19NlBtDp-xHXfhdAaEw4tPCqr9_DfMzuHRjZkZsVlm_3xGhNgrTfMMuqhXyVMlqyWY7Kqm9FDJz6g1XmiD9xh59-elC-GNLkqYZJzuzpAPTCmKCpsoQfoZ4Zm0HZ7reLaop7_Jc0B9Lft1G53ntkQSyuycu-icp_Lq9-bLk_3-NHDh5Ea5OHYLpvZqey-OKkgCDYFXQJtbSgQeEWtHLXU3SHoWCMG1_fZmQ39YK5BEyUZ9SSeTNrMkLhVqpam7iVLvG0tiZeiQklNKACN1IaIzHeMcFgM-bY221miiNBit3V-mzmlLiVXV9jFRga82U3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شبکه خبری سی‌بی‌اس، روز دوشنبه ۱۸ خرداد ماه گزارش داد، دولت دونالد ترامپ قصد دارد روند لغو تابعیت ۱۷ شهروند آمریکایی را که به تقلب در پرونده‌های مهاجرتی یا برخی جرایم متهم هستند، آغاز کند.
بر اساس این گزارش، وزارت دادگستری آمریکا این افراد را به پنهان کردن اطلاعات مهم، ارائه اطلاعات نادرست در روند دریافت تابعیت یا ارتکاب جرایم مختلف متهم کرده است.
سی‌بی‌اس نوشت این اقدام بخشی از کارزار گسترده دولت ترامپ برای استفاده از سازوکار قانونی سلب تابعیت از افرادی است که به گفته مقام‌های آمریکایی، شهروندی این کشور را از طریق تقلب یا پنهان‌کاری به دست آورده‌اند.
در میان افرادی که هدف این اقدام قرار گرفته‌اند، نام چند نفر که به جرایمی از جمله سوءاستفاده جنسی از کودکان، کلاهبرداری مالی، پولشویی، تقلب مهاجرتی و استفاده از هویت‌های جعلی متهم یا محکوم شده‌اند، دیده می‌شود.
تاد بلانش، معاون دادستان کل آمریکا، گفت دولت در برابر سوءاستفاده از روند دریافت تابعیت «هیچ‌گونه مدارا» نخواهد داشت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/76084" target="_blank">📅 23:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76083">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQ02TdcB8M8b4g5eKebKtUbHBtkk5cpO5_nSnSNd42pymJtlTWimLbauGK2wIPoHkSy16_P3IlxbPSKsBu3kUED4kw1o5aoad3cDjuAnT5IUUlarPw2jSAUxfI-wlUF7B-6FnY-eu2yjdI23Al8cgoJopqhOxP2kii_XBdiOpMQLXzQd83qpahKCl3Bm8_gh9Mb5ireOteWsNr_1sZSiIaRnZqr3bj14d7xGFHAZPkZ2FxjZfjzCJjo9HEKnvnfspNfkxsxH511XRr_rM2N5RGOsyXvLIR5rQfBklQOPz9KnC98N-7wp8s0dO6RYAnAs8_TBGVtllZBT1Jy6-3JV4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه خبری سی‌ان‌ان، شامگاه دوشنبه ۱۸ خرداد ماه، به نقل از یک منبع اسرائیلی و یک مقام آمریکایی آگاه گزارش کرد اسرائیل در حال آماده شدن برای حمله‌ای گسترده به تهران بود، اما دونالد ترامپ، رئیس‌جمهوری آمریکا، در تماس تلفنی با بنیامین نتانیاهو از او خواست از انجام حملات تلافی‌جویانه بیشتر خودداری کند.
به گفته منبع اسرائیلی، ترامپ در این تماس از نتانیاهو خواست دامنه واکنش اسرائیل را محدود کند تا از تشدید تنش‌ها جلوگیری شود.
بر اساس این گزارش، نتانیاهو در نخستین تماس که شامگاه یکشنبه به وقت آمریکا انجام شد، در برابر درخواست ترامپ مقاومت کرد و اصرار داشت اسرائیل باید به حملات ایران پاسخ دهد.
با وجود اخطار ترامپ در گفتگوی یکشنبه شب، ارتش اسرائیل برخی اهداف را در ایران، از جمله یک مجتمع مهم پتروشیمی، هدف قرار داد.
این شبکه همچنین نوشت لحن گفتگوهای اخیر ترامپ و نتانیاهو به اندازه تماس‌های هفته گذشته تند نبوده است. به گزارش سی‌ان‌ان، در تماس‌های هفته گذشته تنش میان دو طرف به حدی رسیده بود که ترامپ با الفاظ تندی با نخست‌وزیر اسرائیل صحبت کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/76083" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qttqmcMHp5CH9q2W6b36PtAB37SKQPJaG-IGwkf6HafJsIIpyP9CEJMZA02f4bWbKCxxScSsU9Ks7jah85ArTbmNYACnb3a324oTDs61zjwpLsItIW14FLL6KysbGzT-MIhfxFrj6X5ebgSuAbrJFtq1yusyA9P0Ks66h7uhkmyaavIvPAiuIca-dsDZ4bFAf9x80U1evaQ_cCI6mPXOB3TrXTpQsktdePWwwTa7hHvQINkdqiA1mIepMsLqFUdXLZCkyKYHXgKu9voJ2fhy7iSQnYF4E7Naj8EzMGBEv1EK_DlDBVyKJ43YdkPHmRnEvN72dI0zfehr0uHUvfS6Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول پزشکیان، درباره حملات موشکی اخیر جمهوری اسلامی به اسرائیل نوشت که دشمن در کوتاه‌ترین زمان ممکن ناچار به التماس مجدد برای پذیرش توقف آتش از سوی تهران شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76082" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r6Szcm9XDNJuZcaYFPalESyyltbeMEy5p7czzEEXCTo_xUVIq57hA-sqh3NNIZqmMXL-bBrCYmntLiWDzJ8-CqjaMIEgAP5GadgRoBfqHY5nO7iZEgDcknouOS0kWQYAipr_1SfmIpeum2dUKMYMUUEtAqYcHJfiZ1RJ0JvIEFTDhEh9QAVCeA5v0FSWG1LoVtOw6riNd6dq5u5A-WE6wrQTpEPRqN7esd8eVDXg-d_2nfrncdmYTf-u5F-DFxIIzPZkcvd2CdOCl_XdjRqZv6MLOWN9rLA6RU8dWYHlS6u4MMe_fVQrCYOK2Wg3tafYVzuC7cYYHLUhALK2s3NaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAiAVanRo-lOrASSmvA6DOEdLUIO1hH4Nj7I5nYNlsyanLM1PJgkO-98EMU8zZMDzSP-GpwBum4rEWLJhHODWoZ-bseKylMiHivrVsqvd_nfDPwVYn7Xp9_z2sbDvrZZ9CiT8Po8Btr_HI6-vzqqZ4Q4c5LO-OAberd8VAgc9LLT3oiBu7Hj7xR7nr761XrkzuJdBSDz8ue2X7IEWdHVZmUvGEJffuwk09fSIsmN8-eEK5rW7KV6gUOb-ttNAgGGp0AIxhBnsznV8Al0NgHiuWnpiE7pXgvq_iwPUu7tPrPxTijzSWmTrZLDIcrMKD8gbbhCIC6ZCA0cRRxG6-Ztqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ گفت: «به بی‌بی گفتم خیلی مراقب باش چه کار می‌کنی، چون ممکن است خیلی زود در برابر ایران تنها بمانی».
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز دوشنبه در گفتگو با کانال ۱۲ تلویزیون اسرائیل اعلام کرد توانسته دامنه حمله اسرائیل به ایران را محدود کند و بنیامین نتانیاهو را برای کاهش تنش‌ها تحت فشار قرار داده است.
ترامپ گفت: «من موفق شدم شدت حمله اسرائیل به ایران را کاهش دهم.»
او همچنین افزود شماری از کشورهای منطقه از او خواسته‌اند بر نتانیاهو فشار بیاورد تا از تشدید درگیری‌ها جلوگیری شود.
رئیس‌جمهوری آمریکا در ادامه گفت در مورد حمله به ایران به نخست‌وزیر اسرائیل هشدار داده است: «به نتانیاهو گفتم خودت را در برابر ایران تنها خواهی یافت.»
ترامپ همچنین گفت نتانیاهو «با تاخیر مرا در جریان حمله به ایران قرار داد، اما من موفق شدم این حمله را کاهش دهم.»
کانال ۱۲ تلویزیون اسرائیل عصر دوشنبه ۱۸ خردادماه به نقل از یک مقام رسمی دولت نتانیاهو اعلام کرده بود اسرائیل حملات به ایران را به درخواست دونالد ترامپ متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76080" target="_blank">📅 21:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XWWvh9NtvEr0rL3P4f54GmYTI4K9NKg5btGxlPb-0iBkas2bbIlIVS3VeOkRvkw4Sn6c_rtcCrva2EjYz4dv39gDIQrxYh3-StKx-r8xO1RpILOVqzivnG1_rc-ygiJYEMY483L5TRI0yYtVS2oBcEb_vcVh1c8aBkogIaoLt0ScBGJIGLrdmwd4rGQVqiSq0Qa0O26kHARkLT_wEVD093kKwQxE5pXtZqawIMYkhIBwCbMIBBaLCEi1FLwVpybUB6IRTyuRdSAF_MSo6P8DvRbmtrLc3ioHi6i8BnOXKqIFJ4QQcpBPy9UgdiWrfdWF4f9aDmp8XPqcFk7Hv5GBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: نیروهای آمریکا نفتکشِ متخلف را در خلیج عمان از حرکت بازداشتند
پست اکانت فرماندهی مرکزی ایالات متحده، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکایی روز ۸ ژوئن یک نفتکشِ بدون بار را در خلیج عمان از کار انداختند؛ پس از آن‌که این کشتی با تلاش برای حرکت به‌سوی یک بندر ایرانی، محاصره جاری علیه ایران را نقض کرد.
فرماندهی مرکزی ایالات متحده، سنتکام، نفتکش
M/T Marivex
با پرچم پالائو را هنگامی که در آب‌های بین‌المللی خلیج عمان به‌سوی ایران در حرکت بود، از کار انداخت. یک جنگنده
F/A-18 سوپر هورنت
از ناو
USS Abraham Lincoln (CVN 72)
پس از آن‌که خدمه کشتی از اجرای دستورهای نیروهای آمریکایی سر باز زدند، یک مهمات دقیق‌زن را به بخش‌های مهندسی و هدایت کشتی شلیک کرد. کشتی Marivex دیگر به‌سوی ایران حرکت نمی‌کند.
از زمان آغاز محاصره در ۱۳ آوریل، نیروهای سنتکام هفت کشتیِ متخلف را از کار انداخته‌اند، ۱۳۴ کشتیِ فرمان‌بردار را به مسیر دیگری هدایت کرده‌اند و اجازه عبور به ۴۲ کشتیِ حامل کمک‌های بشردوستانه داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/76079" target="_blank">📅 20:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgSm2lweuGNn81SikrMmbRD6PIVBrj1B_An4UvTAEkqu75KCmAr5-LR8zWkDcE68_rYtNba2oo6PC7nnqfChmSX544K0Ey6gGcIX_atiRuWWci2FwRwAl7MeNuK_YLJz1_UIaWr6Rc2sNODaRwYVeop9Q-pRBWfjRXUy_PFWj3Vt-kc5GnvfAuxH74mMqn09xEPqdwf37GoDisLiJinPOAGNxo8t3Ii2vXWpflSk7Q6g6-FhOvJqBZF4gj1_m2byAWyZ6Nr9cZqtk78IaMvd9AeV5rBoUtp8mq3WWTE_tOwEhncoRR9AJQRrrbDaxeI-l4nIotiHHVHMR5vtb4uc4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامد تیزرویان، عکاس حیات‌وحش و فعال محیط زیست، در ساری بازداشت شده است.  به گفته زینب رحیمی، روزنامه‌نگار حوزه محیط زیست، آقای تیزرویان روز ۱۴ اردیبهشت ۱۴۰۵، بازداشت شده و موبایل و دیگر وسایل الکترونیکی او ضبط شده است.   اتهام مطرح‌شده علیه آقای تیزرویان «اجتماع…</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76078" target="_blank">📅 19:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lY2i4oP1tZj91nryditD6L8LEebJkX8dnBNaMkoTeDyR6b2EHax2TAzjiq0pycayG1pI9ZqZNMFcZs8zXESsJTnjxCVPaISpGosvq8XvkTOEY5ktKbJYXc3CXRbXJNBZ3diFpJA9DWuK-NEEqR-tEtJCFM3-8MXP0cb35dUKgzjrGntF-D-iHHBguvA7eu5eQt44_QZ9f8gD6Om3JwvQCZn4r_JvbdD7C8nw8BVeA1UTkQGhZ5_ai1cp2GYANpokttCdeVDcG0oqLsOuGI9YpJQTIiH2VywErbtXn48Da6OCokGl4J6OhW6IRpHg-52KZOJWwcGLksccsE0haF7sTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران وضعیت پرواز‌ها به حالت عادی برگشته است
سازمان هواپیمایی کشوری ایران عصر دوشنبه اعلام کرد که فضای هوایی کشور به شرایط عادی بازگشته و عملیات هوانوردی مطابق با اطلاعیه‌های هوانوردی (نوتام)، از سر گرفته خواهد شد.
ایران ساعاتی پیشتر گفته بود که تمام پروازها از فرودگاه‌های کشور لغو شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76077" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oB4fN1RTXLUxlsJbiJzU6ny0UOTC3z58ExhpzT2whZD8ZuO7J5HlfkjxF0tFSDVtB5iC0ZezGzFLMUjfBSVVkBjGWWWYGnUP3X1HCO970FVX6VVgfnXTsrJjV-myDzLkU1Hw0JQfRjHDhKr5OW0tqS-76NKG_LLTSuM07unLxcdwGxn4ainZjoMA2sNbpYgCYTf3ODyhtf1D4zNlZltLl_-y8m1VEU_BTDVsVKrxsvt79MK_1m9HuygMjA6rTrnpQm7KNSDnYSPVg4s2bcc0WK8RBguXEBV8pZQD9aBW60SPAKQ_4-bd9PTcT0p4bPr302YDloIfRsrjHA-Yh9bt2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد یک موشک بالستیک که از یمن شلیک شده بود، در منطقه‌ای خالی از سکنه در نزدیکی مرزهای عربستان سعودی و یمن سقوط کرد.
به گزارش رویترز، وزارت دفاع عربستان سعودی اعلام کرد این موشک به سمت یکی از کشورهای منطقه در حرکت بود.
همزمان حوثی‌های یمن، تحت حمایت جمهوری‌ اسلامی، اعلام کردند دوشنبه یک حمله موشکی به منطقه یافا در اسرائیل انجام داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76076" target="_blank">📅 19:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYKZwl0pTk0WGwLmtdHqHYnrSmEr6sf21EOddbefU7zGpgP8BVEFOWGPpK3ssI5Y1YZRJY-dt0kqIgZ0GS3qmVTG9htmz8Ow_qWsW5OQ7iIdKNtaU9iMk9E1ejoWrBl7Z7iPvGhoXVnNnrl5f0SpPb5oP0Ni22R9W_vu5j84tCZ0Jw7oDjqW8FCstaN9xF-H9AU4tvRkBhkpQY-Gxdqd_BMoJQnRb-qQ2n4u8MlMeWIPGfYKEHRAfx3-GD2P4xYPEpswgopVaaV51xwNHA2xyzd_5XK91V7Y3bERhsAgeWz_lgvz56eAsbBsQVFycbc7TftbB4EqhNqXEK0pdjHubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام آمریکایی، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اظهارات مطرح‌شده از سوی ارتش اسراییل مبنی بر مشارکت ایالات متحده در رهگیری موشک‌های بالستیک شلیک‌شده از جمهوری اسلامی به سوی اسراییل را رد کرد.
به گزارش سی‌ان‌ان، این مقام آمریکایی گفت ارتش ایالات متحده هیچ‌یک از موشک‌های ایرانی که بامداد دوشنبه به سمت اسراییل شلیک شدند را رهگیری نکرده است.
این موضع‌گیری در حالی مطرح می‌شود که در دورهای پیشین درگیری میان ایران و اسراییل، آمریکا با استفاده از سامانه‌های دفاعی خود در رهگیری برخی موشک‌های شلیک‌شده به سوی اسراییل مشارکت داشت.
@
VahidHeadline
نباید اینجوری نگاه کرد که تعداد موشک‌ها چقدر بوده و نیاز به کمک داشتند یا نه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76075" target="_blank">📅 19:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76073">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aB3m9UE0yHfbD3vQ89rRwrNG1xGexc28Z_G3X9eGpWCkQagIvZLWXxBCn9zC8TOH3WKY3CFLQ7dm-ddrnY_1HZ6xX3brR2c2mezSAqQSNxa8BDzkkysUwy_DaHl3WOngmt_L3rHSAxJvNFrROYBqI9xyN-ieEnsYFPXd9gS8CZCahkVDpWqxhATMDmLLmaI42Vn0IJepvjG2QLX_ZfAWBi95CEU4A_U9Bv3-1Z08onY5BbKF_agIAKmPyMKmGzQSs3xBhYryJIjkIMeBAX69rObXUy_HDCfcHgmI3L4Ltv_XQ55oSbgpiAnV7dN_ni2ZzXfoC3Ho7JB2H_NYpXPU8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=k4uQO_FCz2TlUKLvUvF7KTleHDByhdbfn9wafm2HCttTyGSGnPLmcZoSWbQp6NaBO9V1ejYgaQtG_zmkgna3DMEbX9amsf4sOckp8wE-Q7ndyTcs5vHkDp83FYmer-22I8wcetZ5ZT7UVZoL-uQy3UVR1iCQHwmo5418PorB9pe_TmmOvMnEZjBN5St-fH6HlyhcOlfnVLYWJ3fENLlIFgVhoXfnKeYAWB76s-EWnscLwsqI5Rehtmo6KiYDAgWr-F6pQnDOIc6wdPCuAS3h-eU9S-EeKNfg-nouYqJ27_L2NJGMf1wyIj7hCFnlXuGNf6vd8LePtqNBc4pUO4JAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fca0bb1962.mp4?token=k4uQO_FCz2TlUKLvUvF7KTleHDByhdbfn9wafm2HCttTyGSGnPLmcZoSWbQp6NaBO9V1ejYgaQtG_zmkgna3DMEbX9amsf4sOckp8wE-Q7ndyTcs5vHkDp83FYmer-22I8wcetZ5ZT7UVZoL-uQy3UVR1iCQHwmo5418PorB9pe_TmmOvMnEZjBN5St-fH6HlyhcOlfnVLYWJ3fENLlIFgVhoXfnKeYAWB76s-EWnscLwsqI5Rehtmo6KiYDAgWr-F6pQnDOIc6wdPCuAS3h-eU9S-EeKNfg-nouYqJ27_L2NJGMf1wyIj7hCFnlXuGNf6vd8LePtqNBc4pUO4JAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل روز دوشنبه ۱۸ خرداد با اشاره به توقف حملات متقابل اسرائیل و ایران گفت «آتشباری متوقف شده اما اگر رژیم تروریستی (ایران) اشتباه کند، ما به شدت پاسخ خواهیم داد».
بنیامین نتانیاهو در اولین پیام ویدئویی خود پس از آغاز موج تازه حملات ایران و اسرائیل، افزود: «ایران و حزب‌الله از همیشه ضعیف‌تر و ما قوی‌تر از همیشه هستیم».
به گفته او، «ایران و حزب‌الله تلاش کردند معادله جدیدی را به ما تحمیل کنند که از نظر ما غیرقابل تحمل و غیرقابل قبول است. آن‌ها فکر می‌کردند که از خاک لبنان و از ایران به اسرائیل حمله می‌کنند و ما سکوت خواهیم کرد. این اتفاق نیفتاد و نخواهد افتاد، نه در زمانی که من رهبر هستم».
نخست‌وزیر اسرائیل تصریح کرد: «ما حمله خواهیم کرد، با قدرت پاسخ خواهیم داد. به نابودی تمام زیرساخت‌های تروریستی آن‌ها در جنوب لبنان ادامه می‌دهیم، و امنیت را به شمال باز خواهیم گرداند. اگر به موقع و با قدرت اقدام نکرده بودیم، امروز این‌جا نبودیم».
نتانیاهو همچنین گفت که ایران به سلاح هسته‌ای دست نخواهد یافت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76073" target="_blank">📅 19:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LosybnwIWD7SmNK4xprcUN14bjDv6NmEz-kUB3o2n-zoQbFX2no_WTCYkSF4VMkVCKrl074ygwoNOKSUEJP3dhl4r2s0QfHAbm62ygUXqsNuH4Vd0cTyx1HUkVecdYSp0C8S2w2HumvWeew56webhxKUR0XONREMTURZ7dK5oVNDq1UOSkWEyy0JTkUC1JMeXeG9gyVU0ZHmr_rEFL_6TqCa6Z8tOum2uDnf6DuP5KLQUz7mBWbJNbpDFSNgQbKeFXRvlxXUpMAt74wisSlQekJbpyKaTodBdp2D7pcgIjUz-_eumNyjXoAFP_rmLVCcY-5UsW7Y9XpqO-MVe8WDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هشدار تخلیه فوری برای مناطقی از لبنان صادر کرده.
J74wabx
ارتش اسرائیل با صدور یک «هشدار فوری» از ساکنان جنوب لبنان، به‌ویژه در منطقه «زقوق المفدی» خواست خانه‌های خود را ترک کرده و به سمت شمال حرکت کنند.
آویخای ادرعی، سخنگوی عرب‌زبان ارتش اسرائیل، در شبکه اجتماعی ایکس نوشت: «در پی نقض توافق آتش‌بس از سوی گروه تروریستی حزب‌الله، ارتش اسرائیل ناگزیر است با قدرت اقدام کند. ارتش اسرائیل قصد آسیب رساندن به شما را ندارد.»
او همچنین هشدار داد: «هر فردی که در نزدیکی نیروهای حزب‌الله، تأسیسات آن یا تجهیزات و امکانات رزمی این گروه حضور داشته باشد، جان خود را به خطر می‌اندازد.»
این در حالیست که ایران امروز گفت عملیات جنگی علیه اسرائیل را متوقف کرده است اما هشدار داد اگر حمله به لبنان ادامه پیدا کند با شدتی بیشتر از قبل پاسخ خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/76072" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/puk4m700tIVQgskTxrAtVVsx3ySTv3aGWSUrTCZLiS8d-a5AgtEXBjSc3faLvfToG1AHYqcJzvRSGqchFO60USAvqVG02fxlppNF4DBGTZAWCreybtBGRr5uGmuyJmmQENs27bbV19kQsTLm4h8O0QiIuv1HJUSkgmEzgnusEnMP-7gksATdvQ7m_KDM3Ew8sH3jRxiP-np04WNSlEtJPuvgl34xMlCVFaYQcjMfSE3rmLcdVwnIFbRgV6zwS8VT_-hBZ0UoXY_gtyr5fQDBoeeRqIEucfoNbU86iyK67OjZMemozDNuHH0Ewm-fUoJB0UMG3JIvCmRyLW2lqCzsWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranSaat25
(وطنه*)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76071" target="_blank">📅 18:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mK7YdSzm7IzXYciC98vdGFVNdrTCTP3oIB6f5ZrO09GNrKrf2EAvqjBP_OcOIGpmc28cHJhO-j6ReM-3gMqKbsu9MIuDmcbf-LwRxeJJ6oiG-fT6wMybZmFtSyqn3RC2WDc-X1EtF4Pad9JxwRSC6WA3PpqwfX02wiuoslpWGOUqzYHuvwo4VwChWz3uOG-9VOjSFjVqMh0nLvdljLglLr7dYos-xsrX69KtWqrz1TyPBEi60O32umteY8fWJRZoOFmGbCAyGt2kAd00ZAgybqQ8LbzE1DNhSWgSnnE9LbN_Ex-mqWyDk-bwuSQb6_TDCcfVn6ZDIQQI5BziO9C9Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Atlansick
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76070" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XaBYk8Cr5o2027Qb2Iz-e3iTn2XsTUFMnb-0mYhXg4d-4xiIfnzlAAf8Le2CreGcS-X8_x8trRGcgJw3QuOlM6pSTAixCfZ9Gd-KmucTxRJFcIY8yXR6NoLplxYYnefimpjsQYxtVJjlUW9fzgum3J4l5HfBXWnS4SThI7HiFGKiQbVvhhAprWkpeSOXqnfmyDs1XT8lvDAEdfsvLgE2qGuGARONvN-DV8PtZ7t1bw2KU8CDsFYBmkrYRDfqOkx_Dlr2EmWYkSJZAMvcLbG0SeRy2JTxp6SNL46p998SV7h0jNTn1kN_1VoUw4gz5e_x57Zyqzz1Om_f3FVvUqIrzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی ایران، در پیامی که روز دوشنبه ۱۸ خرداد منتشر شد، هشدار داد در صورت تکرار اقدامات آمریکا و اسرائیل، منطقه با پیامدهای گسترده‌ای روبه‌رو خواهد شد.
ذوالقدر در این پیام نوشت: «تهدید معتبر را از جایی غیر از واشنگتن و تل‌آویو جست‌وجو کنید.» او افزود: «اگر ائتلاف شیطانی صهیونی-آمریکایی دیگر بار دست از پا خطا کند، منطقه برایش جهنم خواهد شد.»
دبیر شورای عالی امنیت ملی در بخش دیگری از این پیام مدعی شد که جمهوری اسلامی طی «چهل و هفت سال و صد روز مقاومت»، از میدان جنگ تا عرصه سیاست و دیپلماسی، معادلات امنیتی جهان را تغییر داده است.
این پیام پس از آن منتشر شد که قرارگاه مرکزی خاتم‌الانبیا اعلام کرد عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل پایان یافته است. رسانه‌های رسمی اسرائیل نیز از توقف حملات این کشور به ایران به درخواست دونالد ترامپ خبر داده‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/76069" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzqsz_qR1ltcONVFJkR0LrDRCjlAkpnD-2TNm30-4FUmU-R89lkP2shqezyy85UFxjQl0aTHp7RYDfHhswOyn0iQJheihbnMnJ5e0-qmJWZGeIPXovbxtkwOQPUdIMhA34T9FN-Rp4Q98LGRXg9bpvKuRlsYtqRjO8qpgEYtYpg1-mPBoIEazYkR6IXlFVPsHtkB_DaYobczWnGE3-G3pO21NE3o44V56jq5LPXG89UzWTgP9cv4DwmzgYiXQzi0dqaDvrQyY5tQu-QrAQrGyY_flYaHK0mfHPThr0oMXQbcFtprqiEahdWCrONq1V7zqbWwDRpA9Boe9oUwKiIqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یسرائیل کاتز، وزیر دفاع اسرائیل، اعلام کرد هرگونه حمله به شهرهای شمالی این کشور با حمله به ضاحیه در جنوب بیروت پاسخ داده خواهد شد و ارتش اسرائیل به عملیات خود در لبنان علیه سازمان «تروریستی» حزب‌الله ادامه خواهد داد.
او افزود: ما تهدیدات جمهوری اسلامی را کاملا رد می‌کنیم. هرگونه تلاش تهران برای پیوند دادن لبنان و ایران و حمله به اسرائیل، همان‌طور که یک‌شنبه اتفاق افتاد، با شدت زیادی پاسخ داده خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/76068" target="_blank">📅 18:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=auFxRQXmVeFPQsWoZINJsoCuqrozGc6X-bTFi4LcFaDnhE3dvyrAryVlLbf6T3NeW-xTPj4VVOEr-EV8t1X9CDjPW8bdiDuzdhh74y2centlDAC_h2FDkFo5J1oa-K8CpN94Blyuphl24_b7Q-MrcdTf9NEP0nl3AsD-Jfzd4C_WqmE02okSsgFUAHoa6QAtp7h0Rv_K6JSlirJsVmbnl3pHLyfUoKjgH4G6plu-FsjvUk166U_pjkhdPcg5qLE790bioMy0vSepAoyDanJaTbWkMQt71T28xoStAYqirybPF1T7Cw69sskTrAgEm2V-sJsI7xg0BdPdkwZ4s1vsyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4c3ab90b1c.mp4?token=auFxRQXmVeFPQsWoZINJsoCuqrozGc6X-bTFi4LcFaDnhE3dvyrAryVlLbf6T3NeW-xTPj4VVOEr-EV8t1X9CDjPW8bdiDuzdhh74y2centlDAC_h2FDkFo5J1oa-K8CpN94Blyuphl24_b7Q-MrcdTf9NEP0nl3AsD-Jfzd4C_WqmE02okSsgFUAHoa6QAtp7h0Rv_K6JSlirJsVmbnl3pHLyfUoKjgH4G6plu-FsjvUk166U_pjkhdPcg5qLE790bioMy0vSepAoyDanJaTbWkMQt71T28xoStAYqirybPF1T7Cw69sskTrAgEm2V-sJsI7xg0BdPdkwZ4s1vsyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسراییل، روز دوشنبه ۱۸ خرداد، ویدیویی را از لحظه حمله به یک سامانه پدافندی جمهوری اسلامی منتشر کرد.
ارتش اسراییل گفته نابودی سامانه‌های پدافند هوایی ایران، آزادی عمل هوایی بیشتری برای عملیات‌های بعدی فراهم می‌کند و بخشی از تلاش این کشور برای مقابله با تهدیدهای جمهوری اسلامی به شمار می‌رود.
@
VahidHeadline
و در پستی دیگر ویدیوی دوم بالا رو درباره مجتمع پتروشیمی در ماهشهر منتشر کردند.
بدون هیچ شرحی درباره اقدام نظامی خودشون نسبت به اون مجتمع پتروشیمی
نه در متن پست نه در خود ویدیو
اگر قبلا تایید نکرده بودند که به اونجا حمله کردند این طور پست گذاشتن بیشتر شبیه به تهدید به نظر می‌رسید. شاید الان هم همینطور باشه.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76066" target="_blank">📅 18:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76065">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GnBK1F_mtJi9-CvhhBc9SNcvuaycQ8FS_49Qdn72F9hM1qq5b95FvqACYYySHaqTh0wt9etiMKW0p1RnpVPArjydVbylXj-induHayINPkIS21yO1jjU5W8lEDcajBHSBOs6_3SEaE_42hVT-rwfo63I9WQYR9hRqFyBd63skcOtgZaxqTlrdfZoczZxgFwVa_AZjEnuVfRdk2_etv_MtLBLaVtUaMMyNTX9uywj66Lm0qsnuur0WwCvhEQTdzm2pe6O8MMaiXCLET1s27MafcVheJ3I4FOBMHIiorfofcuZH8N2YlQGzsk5nCsqtLEqW98yMeT75iR-Dle0fEb8gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت محمدباقر قالیباف:
"معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را بر هم زدیم.
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود."
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76065" target="_blank">📅 18:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkr3IYWWfgbfNJLCKx46QZQ6PbADwC9i-jMrCy_kueMqMc_CG7jqnvokdujWVSPiDASBHqSIXKRHIQyRySUrjbG55uY2TgmdVeNwDaL2vSr8FKRTveksmcfFvAQ703JNFmK5LMcupX7GkM71isr7mX_b4J78xVMk1gwOd66sog26Ha5OOyfoEQQNBnPvN0Lh3boZ2w8qnvxRR9PeWbtIc4xuz_TDOxdmvZJomvJghO5Ww7CMiqkoWNLOoeBEi8-ZSHe98SEeU8VHbkYXGdOQL-ScwN3DZeB4Dco1hKoIXc4j2WC0P5Z85z2u1Svc5BlWkQHB1rD4hTmQx-uujxOLlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های دولتی لبنان گزارش دادند یک حمله هوایی اسرائیل روز دوشنبه ۱۸ خرداد یک خودرو را در شهر صور در جنوب لبنان هدف قرار داده است.
خبرگزاری ملی لبنان اعلام کرد: «یک حمله هوایی دشمن، خودرویی را با موشک در شهر صور و در نزدیکی ساختمان صلیب سرخ لبنان هدف قرار داد.» تاکنون جزئیاتی درباره تلفات احتمالی یا هویت سرنشینان این خودرو منتشر نشده است.
این حمله ساعتی پس از آن صورت گرفت که جمهوری اسلامی ایران و اسرائیل پس از ۱۶ ساعت درگیری نظامی اعلام کردند حمله به یکدیگر را متوقف می‌کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/76064" target="_blank">📅 18:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHkVvmjJZ941eXGiT8YbeV5ZC7DbyCWyb6_mlANOuSe5szmBFthOaUvQFvy6hrExuM7Z9vgfYYzuj3Lep1lVPYiB59PM8qCGhNBJqzFdgC0EX6LrsPTIKeem_vxw5sW6KWRXndwqx2NbVcPbXs64t3kBUf9J8WpSERRyhEQL3KyNVguQ90Pc3k4XDWXvDswS3TY3XdPex5sfTnAgIq1baa-TXeMAPovzVw4NQcGvZWtVYRxYx0qxa23EPuSNz6-sSNgNMLsEHaSS3PiLb7J68OpDu06Boj3eRs955ZUjPWGQxBPVnf4ndf9RQFo3gK3R-WOKHTGs2HJqUM2mvOKcqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رییس سازمان اورژانس ایران، روز دوشنبه ۱۸ خرداد ۱۴۰۵، اعلام کرد در جریان حملات اسراییل به ایران، ۱۵ نفر مجروح شده‌اند و تاکنون هیچ موردی از جان‌باختن شهروندان گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76063" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAxljtLlzVKwGiP2a_ynOLhZryNRMaWbl16Rxd4C8_lJl_YgYAZE7C2ZpQHONkREyTVR4okqAvJ3OKksjy9fQj2YXNnh0M4cvTR5hmm3tmmtR--GhI3oteArn5T4nC_wgPWKGBB1asuKKp4fELm1YEoFPajPwv8TnNHmIrADpYbZxf0JGYq6dBaIqTwOV3uNUJYRXS4FFa1i3ziHLiwzPPc3YXOHTaYKZPWHPKrG72djfddkxa0_THA5Fgc5klzyqt79kf00a-1nLnfVP3dEnK7_tufdIK3mNYtzngSi8diDeoSTBqBTXD1L730v00b5Uh1qbp2G1sD7D4-IZcsWdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ایسنا عصر روز دوشنبه، ۱۸ خردادماه، به نقل از شرکت فرودگاه‌ها و ناوبری هوایی ایران خبر داد که «همه پروازهای فرودگاه‌های کشور تا اطلاع ثانوی لغو شد».
این اداره همچنین از تمام مسافران خواست تا «جهت حفظ نظم و پیشگیری از هرگونه سردرگمی، تا زمان اعلام وضعیت عادی از سوی مراجع ذی‌صلاح به فرودگاه‌ها مراجعه نکنند».
این خبر ساعتی پس از آن منتشر شده که قرارگاه مرکزی خاتم‌الانبیاء سپاه در آغاز بعدازظهر روز دوشنبه با انتشار بیانیه‌ای از توقف عملیات نیروهای مسلح جمهوری اسلامی علیه اسرائیل خبر داد.
همزمان رئیس سازمان حج و زیارت خبر داده است که «با توجه به شرایط پروازهای بازگشت حجاج احتمال تأخیر در برخی پروازها حتی تا ۷۲ ساعت وجود دارد».
او اضافه کرد: «برای فردا (سه‌شنبه ۱۹ خرداد) ۱۰ پرواز پیش‌بینی شده که امیدواریم بخش عمده آن‌ها انجام شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76062" target="_blank">📅 18:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXJXWTBpoYFB9VyL50YGtquUDl_bj5j6JeFBqZCJnnvFCreGjUG3bNM1YOEj3E4KNKEpKJvijNLIWqVMoomI62JYlFRYpJ5AiIjbIk3tQ0mrvdTLlbJd427Vd57iyfOr_4LKsorTRmclYaEVhetEyz-pyBSt226nZVhCARL7MSLqf9a66T2PQJlSQQ3oO523uSofCIYl6vRwksAYwZZqFDFKLRNuu2eDeaR9lvw9m974vqDMItms4aAihh9Fq-A36KqGzQgx1GscCLET4HKjU0zSLWaL-Qqzppu4fWctXjentBrrAtsh9_ZJrGAsXfyvPkUUHFa5JNzeAclW2egw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایا کالاس، مسئول سیاست خارجی اتحادیه اروپا، روز دوشنبه ۱۸ خرداد اعلام کرد که اتحادیه اروپا به‌دلیل تهدید آزادی تردد دریایی توسط جمهوری اسلامی، تحریم‌هایی را علیه شماری از افراد و نهادهای ایرانی اعمال کرده است.
کالاس این اظهارات را در جمع خبرنگاران و در حاشیه نشست وزیران دفاع اتحادیه اروپا در قبرس مطرح کرد.
هنوز جزئیات بیشتری درباره این تحریم‌ها ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/76061" target="_blank">📅 15:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b31564948.mp4?token=E2TQUdogCRrnxCw2nnzS7SSSluADiP_nQzRRB9jHJBUekWP7TLEoOaL0CtD83FtQWSfrRHYppqWx0rkTSNscGmg7zFLMoShvtLdHXYGTbR-Bhw_B8DJT2cAfO9aI5Yi49m72WMxad6u0ExbyzjOHHc3pbAIsPRsdoj7kFTYR9xDDv7ZYray4JeJd5P0IK2OfFcHJj-CJlBiigJ8UaeIwu-JIIEY7arwXRRlzxBg62rtaN5jDpqClJZv01JrSFRX79RZOphVlxtDFxBmEk_6cupju798EG7ObhkJrsBXLAEOnFv5ok3OlSsSl3aS1LaKVz7l7EA8dMdyuHH9g5A7cnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b31564948.mp4?token=E2TQUdogCRrnxCw2nnzS7SSSluADiP_nQzRRB9jHJBUekWP7TLEoOaL0CtD83FtQWSfrRHYppqWx0rkTSNscGmg7zFLMoShvtLdHXYGTbR-Bhw_B8DJT2cAfO9aI5Yi49m72WMxad6u0ExbyzjOHHc3pbAIsPRsdoj7kFTYR9xDDv7ZYray4JeJd5P0IK2OfFcHJj-CJlBiigJ8UaeIwu-JIIEY7arwXRRlzxBg62rtaN5jDpqClJZv01JrSFRX79RZOphVlxtDFxBmEk_6cupju798EG7ObhkJrsBXLAEOnFv5ok3OlSsSl3aS1LaKVz7l7EA8dMdyuHH9g5A7cnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی در شبکه‌های اجتماعی از لحظه حمله‌ الهه و شهربانو منصوریان به اتاق ریاست فدراسیون ووشو و شکستن دوربین مداربسته منتشر شده است.
طی سال‌های اخیر
خواهران منصوریان
بارها به ساختمان فدراسیون یا کمپ تیم‌های ملی حمله کرده یا با مدیران درگیر شده‌اند، اما همواره از حمایت نهادهای حکومتی برخوردار بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/76060" target="_blank">📅 15:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf21K7092vzdDPbQFPg2MoMUoAeSWUmWd1_gwHuFkSuwss8uw1aMuIQmtK3Rgw12ZOMVXd3OEHN8WOXD1Ynv85cUd441BedAL-TkakTKKQgl8DGZNQCl1RxvTMwfkblE2myGS8dEH8A4tFu8Zn8aRu7plhQmFcDa0hvLZ42148kDWRotQux1n0HUVZ9Y4y6wFVVG53hVKvD1HNbdB9xDOz4GJdSVGUYRNNesoce2rWOGZUg8-5ss-CPhWELHra5ibbKiO8BnalIqwpw2CDE5u27c7vvsVYKltRnToP8GGvfERGPA87DtIz3p1PIW5PE23Gztf9A0jWSXNAe-F66Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
سپاه پاسداران از «توقف عملیات» علیه اسرائیل خبر داد
♦️
قرارگاه مرکزی خاتم‌الانبیا سپاه پاسداران، روز دوشنبه ۱۸ خرداد ماه با اعلام آنکه نیروهای مسلح جمهوری اسلامی ایران در واکنش به حملات اسرائیل به منطقه ضاحیه و جنوب لبنان «پاسخی دردناک» به این کشور داده‌اند، از «توقف عملیات» نظامی خبر داد.
بر اساس بیانیه قرارگاه خاتم‌الانبیا، پرتاب موشک به اسرائیل «در راستای حمایت از مردم مظلوم لبنان» توصیف شده است.
در این بیانیه آمده است که این پاسخ برای اسرائیل و حامیانش باید «درس عبرت» باشد.
قرارگاه خاتم‌الانبیا همچنین اعلام کرد «توقف عملیات نیروهای مسلح» در دستور کار قرار گرفته است.
با این حال، در این بیانیه هشدار داده شده که در صورت ادامه حملات و اقدامات اسرائیل، به‌ویژه در جنوب لبنان، جمهوری اسلامی ایران «اقدامات بسیار شدیدتر و کوبنده‌تر از قبل» انجام خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 451K · <a href="https://t.me/VahidOnline/76059" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76057">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PeTxH4asAwxzWmEb0KYtfjSJ7LgWCMthbEu04YaDCfit3vy-RWy7AcWyOYHMDl1WOXmpSEDO9mUIfq6gv25qgLBmxr__LpdJHNBPsnT4W_Kx2lmYJWufqv-VoUK8qNF7UNtO8wDPGO79waGeb46gtCX7I0p62c6R7ji1unSimMZJ1lZ60tRHNTmvum4Q4_sQ3Y_NKf1Jp99hTwsHAeFCCAPu7iic4TrO6jL6Yqu3MTStkqCn9H44hIl7WvmBmhiZzbKUuX1qv8sKKj8K6K1ALnWtFQ5TPDDUu1x9gXaEkTNKPpx6HONo0FiLcsyufXVjfjVbw3jsTp8AsJ9OV5oesg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tvBPqg49BwlM5Z41VWp3FDYKy_f4PYy6HkWxc9-Nvwcxbb6nftTdidJBnADMvIxh26Bn3dYjNFTruEK5a9n9ULVQyHfTGm6jlmgvmfnt9tDs52h4FHr_CNSlvYqtotxX8IRpi_y4QFFEhqR2oADT54vf3YH4eWjyts9SgKcZjmPZSiyjS56BDdbcjnR9B5NDp4TFlFNp85eX-hYmcAIOXjwe-SQKPkmSFcITDteGSihEf-btTX7ME4UtyL7qLN8P21i7KTZSyA53nK2e3KM8-0zz0YRuUbF-ZRm7yBIawPt-Ssi-lFOm4q8PuYrkG3Ss-wUb23M4K8HoQhcTZB4kmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «تیراندازی» را متوقف کنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دو طرف، اسرائیل و ایران، به دنبال برقراری فوری آتش‌بس هستند! مذاکرات نهایی درباره «صلح» در جریان است، مگر آنکه نادانی یا حماقت مانع آن شود. محاصره تا زمانی که «توافق نهایی» حاصل شود، همچنان برقرار خواهد ماند و با تمام قدرت و اثر کامل اجرا خواهد شد. امور باید به‌سرعت پیش برود. از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/76057" target="_blank">📅 15:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BMiBHXuOni0h5ePpOtvSP5C_K_KH6jpPToyi9TBjY19J9X4DWGQ1Q-pSU-BJiZXq2xiOxmmLwO17YrT0uYoe2WbznHbWIyVdiiLAhfVxTtPjRCdS6y8V5KHeu_TUwSNNQtjUIzsXAo3J0EMtQykwqukldQMMSF7rZb_8E6sI1Y4GMGcpFbMcTjicwMgBm4CWSavNQpzNjmPFSkA2PLbC-pL-f_KIBxmlcir6qwHG2ErHOSQilMj6jm43bjEyvoQP7Txm66DZ9Uq7Tcgw_F_1IpErI1ReTgCJ_L0fEGXZVZ4XjuZMnxfw-XlHRZridPi_FoCYdPkON5GVw4jx3C9j_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی گزارش داده‌اند که نیروی هوایی اسرائیل همچنان حملات خود را در نقاطی از کشور ادامه می‌دهد.
بر اساس این گزارش‌ها، فرودگاه شیراز در جنوب کشور نیز در میان اهداف حملات اخیر قرار داشته است.
هنوز جزئیات دقیقی درباره میزان خسارت، وضعیت پروازها و تلفات احتمالی منتشر نشده است.
@
VahidHeadline
در خبری دیگر:
خبرگزاری مهر وابسته به سازمان تبلیغات اسلامی نوشته:
"پهپاد متخاصم دشمن آمریکا_صهیونیستی توسط پدافند هوایی در آسمان تهران هدف قرار گرفت و منهدم شد./ مهر"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 507K · <a href="https://t.me/VahidOnline/76056" target="_blank">📅 11:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-h8toECyVXn4mwM4ren5uUVtA1gQOOxF9F7ek0l8dkmmOXdLHmfUa5iJS80Tq02qeQMPXbr3n8tBQa7BFvJPkO6AWMxs-1ORBj3_-xFCCGmus2_v1MnA5GV5l7Q5aUiQJlNVn2ECRDKvuswuQTaOZ5Y6lsl5qm3YmHjs7L-lLnAVS9KFD3l6aONCMaqy9wihO9NvLZlJFrUjSzeDyHvBFN1CtrUKrX8cQwm3ld1qkEzDp_vBd2j7p9g6crkyjgHh11s1_oE_aYj1yZARrLwEfVJXnri-5XeyOeGtLgH8bxTNqTZUErDCXNd1cHGA71cNGwK-xNhfQfQi8VFXuKWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران در بیانیه‌ای گفت در پاسخ به حمله اسرائیل به صنایع پتروشیمی ایران به صنایع پتروشیمی حیفا حمله موشکی کرده است.
بنابر این بیانیه، هدف قرار دادن اهداف غیرنظامی و تاسیسات نفتی «بازی خطرناکی» است که زیرساخت‌های انرژِی منطقه را تهدید می‌کند.
پتروشیمی کارون ماهشهر که در بیانیه سپاه نامش برده نشد، تاسیساتی است که هدف حمله اسرائیل قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 501K · <a href="https://t.me/VahidOnline/76055" target="_blank">📅 11:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پیام‌های دریافتی:
‌
وحید تهران صدای مهیب وحشتناک
ساعات 11:33 دقیقه جنوب تهرانسر صدای انفجار اومد
سلام ساعت ۱۱:۳۰ رباط کریم صدای انفجار
تهران صدا و موج شدید انفجار ۱۱:۳۲
همین الان صدای تک انفجار غرب تهران
زدن تهران صدا واضح انفجار
ساعت ۱۱:۳۳: صدای یک انفجار شنیده شد - تهران آزادی
صداش خیلی زیاد نبود حوالی غرب باید باشه احتمالا
اسلامشهر صدای انفجار ساعت ۱۱:۳۲
تهران الان صدای انفجار اومد
تهران غرب ۱۱:۳۳ تک انفجار بزرگ
سلام وحید جان.۱۱:۳۳ تهران صدا انفجار اومد.من غربم صدا دور بود ازم
۱۱:۳۳ دقیقه صدای انفجار ملارد فکر کنم زدن
ما سمت مهرآبادیم ساعت ۱۱:۳۲ صدای انفجار اومد
صدای انفجار در اسلامشهر ساعت ۱۱:۳۴
وحید ما غربیم 11.33 صدا انفجار امد
یه صدای تک انفجاری اومد الان انگار سمت یافت اباد
بهشت‌زهرام. از نزدیک اینجا صدای انفجار اومد. ساعت یازده‌و‌سی‌و‌دو.
همین الان اسلامشهر تهران ۲ تا صدای انفجار
سلام وحید جان، صدای انفجار در فردیس
غزب تهران سمت پونک همین الان صدای انفجار
تهران اطراف اتوبان نواب صدای انفجار
شهرک غرب
صدای مهیب انفجار از دور اومد
وحید قلعه حسن خان دو تا صدا انفجار قوی
سلام باقرشهر کهریزیک صدای انفجار 11:33
وحید داداش سمت دریاچه ۳ تا انفجار ولی دور بود
11:32
گرمدره صدای بمی داشت تک صدا بود ولی دلم یجوری شد
سلام وحید جان من سمت مهرشهر هستم ساعت 11:31
صدای انفجار خیلی وحشتناکی اومد
از شرق کرج یا غرب تهران
ساعت ۱۱:۳۳ سمت ملارد صدای انفجار وحشتناک اومد
سلام ۱۱:۳۳ صدای انفجار اومد از جنوب تهران از دور بود
تهران سمت شریعتی ساعت۱۱:۳۲ صدای خیلی دور انفجار اومد
از ملارد ساعت ۱۱:۳۳ یدونه صدا اومد
وحید اسلامشهر دوتا صدای خیلی وحشتناک اومد
ساعت ۱۱:۳۴ اسلامشهر ۲ انفجار با فاصله یک دقیقه
ما سمت چهارراه ولیعصریم دقیقا ۱۱:۳۳ دای انفجار از دور اومد
سلام ما عظیمیه کرج ساعت 11:33 صدا شنیدیم، دور بود
سلام من نزدیک مهرآبادم یدونه صدا اومد بنظرم بلند بود اما خیلی نزدیک نبود
بازم هم مهرشهر کرج صدای یک انفجار
ساعت ۱۱:۳۵
درود گلشهر صدای انفجار اومد همین حالا
ما تو یافت ابادیم صدایی که اومد نسبتا دور بود ولی خیلی مهیب بود
سلام وحید جان من سمت شمال تهرانم ۱۱:۳۳ دقیقه صدای انفجار دور ولی سنگین اومد
آپدیت:
پیام‌های زیادی درباره فعالیت پدافند در مناطق مختلف تهران دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 510K · <a href="https://t.me/VahidOnline/76054" target="_blank">📅 11:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tKzBdURTKuLwI0Hy_YOfkOOOc7CknKcfjGV_1NbeymxEofPs3nVUElk5evN5ESztrZ_bLGlB4bNGL0Z25juxsVCKpW7vekzdbMWBR3jZU5Id3BAtxHrXpOP_5W1dEXqDwkyuHwNIRDIAmlKSIMhwgXDikh0ulEDzmB8jTUTgB1jLDtiXQlN_ySMAx5VSN-CDyiKnaQflFF_57wEJKprVZm16t1YAusQNFXotCQfoA05LYi97PKfzFy3oCoY_Yi8eoWeZyzz2u445RYXQhFoAkfGjQi8rvY-M6mJhz8bmyY6qpyXE6yHWkJuEZeRbY0dFfjwtToviy72wJOMfbY5rQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ایلان ماسک: "تنگه هرمز به نام اهورا مزدا از آیین زرتشت نامگذاری شده است."
elonmusk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 443K · <a href="https://t.me/VahidOnline/76053" target="_blank">📅 11:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOBe4gx7ghLCFad-o7396r48TiT08IPjCz_njorYOSp8AfaMqsRVWM7T50TZ0UwDEutJAxDLOYDafMsPpL-ivFuknZ--1fy3gwFf1BiPVbusO3IR8zjiwLp9xeAX8cj_RDCIv2S9VHBsUyvNvDjM6nmKH0befetm2nJmaXa_1p3sJTpRU_U1rUvz6adcI8KKsp5h1yX5kPhiCfs77YKW4ynO5PystzQXo1XYPd4pLFH_vDFxgy2EcvtMm68myiL2iN0lEb00itVEiYmSLzxVWFP2oNgtb_-p97pyibyOtnl6xstwIciPCo50KRovyETAEIC9pYjn1lzEuznF4Ut9Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسماعیل بقایی»، سخنگوی وزارت امور خارجه جمهوری اسلامی، در نخستین کنفرانس خبری خود پس از آغاز حملات ایران به اسراییل گفت که اتفاقات ساعات‌ گذشته، به بی‌اعتمادی موجود میان تهران و واشنگتن دامن خواهد زد.
بقایی در نشست خبری خود گفت تبادل پیام میان ایران و آمریکا تاکنون در فضایی لبریز از بی‌اعتمادی انجام شده و به گفته او، آتش‌بس نیز «به طور مستمر و مکرر» از سوی طرف مقابل نقض شده است. او تاکید کرد جمهوری اسلامی هر زمان که لازم بداند برای دفاع از «امنیت کشور» اقدام خواهد کرد.
سخنگوی وزارت امور خارجه همچنین آمریکا را مسوول تحولات اخیر منطقه دانست و گفت اسراییل بدون هماهنگی با واشنگتن اقدامی انجام نمی‌دهد.
به گفته او، وزارت خارجه آمریکا حمایت از اسراییل را دلیل اصلی جنگ علیه ایران دانسته و جمهوری اسلامی از همکاری و هماهنگی کامل فرماندهی مرکزی ارتش آمریکا، سنتکام، با اسراییل در حوزه‌های دفاعی و تهاجمی اطلاع دارد.
بقایی با اشاره به تفاهم آتش‌بس ۱۹ فروردین، آمریکا را مسوول هرگونه نقض آن دانست و گفت پیامدهای تشدید تنش در منطقه متوجه واشنگتن خواهد بود.
او همچنین از «رافائل گروسی»، مدیرکل آژانس بین‌المللی انرژی اتمی، انتقاد کرد و گفت در صورت تصویب قطعنامه‌ای علیه ایران در شورای حکام آژانس، تهران «پاسخ مناسب» خواهد داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/76052" target="_blank">📅 11:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/025351cf82.mp4?token=WkekflisnLiPnKmRO1XVHG8Kb1Y4LL0VuihEbAMqgI3e_HDqp2PXv1jiYbThdF6Uh10ZRK4DsKVuUDrtv5sxiL_5dQbMzp0ydLVGpADLf5m2JN1GlaDQXb-kryyR06qKWry9CNu-CQiUUZX-YiVmtaPU6A4Ss3BDvAobHZMG-xuA-JvIq1UWHonJQLqMDsAwNNtSTy9xK6CJ17RemvuTTbDiLraL8_SCRhRyKEEsx_paJ2dvO7xeJjZ8sP2cI9qjORDflqu4CmeE8OCdWlFv4oh-yuFnbmBJgxibstRekyFrjlceIcBVpV4mOx1-QFd1yRifxnJZbFKgM77cQ8Sh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اکانت ارتش اسرائیل با انتشار ویدیوی بالا نوشت: "در دوره اخیر، سامانه‌های پدافندی در چندین منطقه مختلف در ایران مستقر شده بودند، ... این حمله منجر به انهدام این سامانه‌ها شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/76051" target="_blank">📅 11:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQxYDHLFxpLm6jMZ-X-KalExbxSeit5jcAI5dICvXs0RKPnrVZFjcK8t9CiuPKhcIbTWngYuNSsiOnT33QyMOvq5KizO9mKYzCAnrpzWufOiDlPNLBBX7UFkhf73XUcqd84m-HrzVh2eAh0z1RfveBJkNnw1suI73HKvopZ9WzD9Iz4xa1PBTRe0D_B670qBoSOopOzjea25Bxk2TFSWqs5IPxwrLdZt0IysbNslSjoXkFCiHzarmYA1mLCvMVLQyE8WpdmMrYxQMWSAdP4HCkm5j2v4qXjBAIY9xYB9EJFmx48UIItty_ys-Eg2woP1mQ5FAEbJBexX1QZrEmR0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه قطر اعلام کرد «محمد بن عبدالرحمن آل ثانی»، نخست وزیر و وزیر امور خارجه این کشور، در تماس تلفنی با «عباس عراقچی»، وزیر امور خارجه جمهوری اسلامی، درباره تلاش‌های میانجیگرانه میان ایالات متحده و ایران و همچنین تحولات لبنان گفت‌وگو کرده است.
بر اساس بیانیه وزارت امور خارجه قطر، نخست وزیر این کشور در این تماس بر حمایت دوحه از تلاش‌ها برای مهار تنش‌ها و دستیابی به توافقی جامع که به تقویت امنیت و صلح در منطقه کمک کند، تاکید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/76050" target="_blank">📅 10:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rlPPrOJ7pW6tspT17iXD0403adRYGedBJ5JyfEWALtJBvcJ_Ams06vLJLeFp4ffpAmDbWr1o8XNyu3lXEpGGsp0-Qf0-ACn4PGukMFlOakg5KFD9flQU3yjUQt0OAjWIHe07MWTeV270n4J0D4hnJvjW0GQy3dwMCod6AFt_goKjsBZE9qXu4XvrzasC4N_PubBctNxI5mEbbbliWuPuxYtKf31X6FEmsGbbu-XHY8pZ51oxUiWFkwZcrTvCMfqEpxieQGncrinb9IufIhaG1dgswdKa-IUTmSpKjy1Vw_M-7ilINo-0eYPE1bJvPZtDU2wbWE4xJ4A-xe54Fdonig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQeyd1se9fF9moXb0YVhhbrHYpYm9Wll7hzZ87jJg1WJHIxh3zpXai9nqA28BAhWqxllQCqOY3qegvBhmKla12OoyAIAO3ZjLpkNlIyYy0fiDcWc42lGBgCttondyJJU7GfWcb6PkZzTJspa-EBjyNVqDnFR9IJdD-AidAk-9gOhGOGxrVpP2zTBqSvT1DB3g7MRNlndl_pnGZIoJEtaUbGQa_b2ej8D2xhUiXr9UlPzTIc7hCcTSPlNI8W1x2_V5icVZqqM0cyHaasJI2ta91CpaXiHif2foi49tG_C9tzOvQB_-0ho2nhoIQZJsZrzOVl6ZnCyREd5bSsi5V15Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qk4s88oo_0n2C1TcUDkNGTV9P-uOcSd8CKUcbz8KqHeJLNZ4xeHbcrNXzwK76HRk_yuZ8AzHEDOabEjCRZvuUaM00HTP8miX32UxttS46rhW8Yz_42Jg-KTtkMgdMX5XdoOfOBhVz6QPi6puGzgOpLTGldsvDruXO_S1mQoVR-7cvAG8_-hfvNGZS5IWuUCtoXI3GVoVdQK9r03SidfoyMMCquiX8J2rwFvCjTQ4CUZDxRPEaNESGPuK1oydflFhcDK1nxp6eG9XVY3mCxOJMEbhEs0rJIt9DVwQSEogr7hRDTjOO8af4c1V1MYO2YJFrFglCAvaXkkmoe2zV91g-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=mdaD2rT-SevZsNIIXAxSoY0j3QHkWYXoyGIKUV2KEwzl9-dIzBV-OeYDJDGV7wn9-GGfuNRRoPPoEM-HtJI1VPPm158jVF0fxeLNvlPA9Ug3-cpOyOiwYwaFCDmFn0otA83luVkEanY2-_YFBY62qrAmSb5eHN3Z7dUFwK0Cssmv52rc9PMQ38RLVhkGwVrWKLUJWcQYzo0T90K7JQrhGFDOgyciFcIOIGzwaY8WciwzOUgOYp3QamX0jAZQprRMJRWkKGqXFd9tJXMY5ARSid_geMaQ3KFzMTOqmRBx-Gs7He3R7zNKYYTrITJs13R_xrOtQIDb3VAr3gEwkdidYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/551c6649bd.mp4?token=mdaD2rT-SevZsNIIXAxSoY0j3QHkWYXoyGIKUV2KEwzl9-dIzBV-OeYDJDGV7wn9-GGfuNRRoPPoEM-HtJI1VPPm158jVF0fxeLNvlPA9Ug3-cpOyOiwYwaFCDmFn0otA83luVkEanY2-_YFBY62qrAmSb5eHN3Z7dUFwK0Cssmv52rc9PMQ38RLVhkGwVrWKLUJWcQYzo0T90K7JQrhGFDOgyciFcIOIGzwaY8WciwzOUgOYp3QamX0jAZQprRMJRWkKGqXFd9tJXMY5ARSid_geMaQ3KFzMTOqmRBx-Gs7He3R7zNKYYTrITJs13R_xrOtQIDb3VAr3gEwkdidYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما کاشان هستیم
اینجا قشنگ صدای موشک رو حس کردیم که داره رد می‌شه
همین الان ساعت ۱۰ و ۱ دقیقه.
از خمین همین الان موشک زدن
شلیک موشک از ابهر ساعت ۱۰
خمین ۹.۵۷
وحید طرفای ابهر خرمدره ازناب زنجان موشک زدن ساعت ۱۰.۰۲
سلام شلیک موشک از استان مرکزی
وحید جان سلام ساعت ۹.۵۸ دقیقه یه موشک از ابهر زدن
سلام از کاشان هم همین الان موشک زدن
شلیک موشک از زنجان ده صبح
سلام از خوانسار صدای موشک اومد، رد موشک هم توی آسمون هست.
همین الان از زنجان دو تا موشک بلند شد
هم‌زمان پست ارتش اسرائیل:
ارتش اسرائیل شناسایی کرده است که مدتی پیش موشک‌هایی از ایران به سمت حریم کشور اسرائیل شلیک شده‌اند.
سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/76046" target="_blank">📅 10:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76045">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=HXxlvs62QzJoWnuCPNPjTBPaL1BysQt0wPoZAyKdpLU5-po5zyDfv9B71b55WUmsbnN-xl9mXnHGla3FS7YfM3yBal2JNlEf_RlZUa3QgHGITl3HtV-YANZq_dWnyk60rH6G6QteqJRcoe_CFj1L7S_wjZQbxtBTppyLqqSdrAHf4l2Kz-0efyXgJh0vKsLEIiw9i66taPlxCz9GkFFbMyHCtEq2cuVieJ1fEWpniHf4OG8OntWNktnpBpWzKgYRuh7KkoICDZjZIRAvy8_ekeiPyiwiTdydqsj8Un_RRv0KWHkgqYRN4gGBDPIgkthqvgUe1Y9AXlM2NvCkzrDc7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2e62b7f335.mp4?token=HXxlvs62QzJoWnuCPNPjTBPaL1BysQt0wPoZAyKdpLU5-po5zyDfv9B71b55WUmsbnN-xl9mXnHGla3FS7YfM3yBal2JNlEf_RlZUa3QgHGITl3HtV-YANZq_dWnyk60rH6G6QteqJRcoe_CFj1L7S_wjZQbxtBTppyLqqSdrAHf4l2Kz-0efyXgJh0vKsLEIiw9i66taPlxCz9GkFFbMyHCtEq2cuVieJ1fEWpniHf4OG8OntWNktnpBpWzKgYRuh7KkoICDZjZIRAvy8_ekeiPyiwiTdydqsj8Un_RRv0KWHkgqYRN4gGBDPIgkthqvgUe1Y9AXlM2NvCkzrDc7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اعلام خبر حمله موشکی به اسرائیل در تجمع هواداران گروه‌های مسلح شیعه در تهران
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/76045" target="_blank">📅 09:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhWHrE5PdIKQhNmHZb-pKNAIO735Q1DjjLo3H58fswwdc_Ivhg_5Xq5aKXw0pXUSXbJOSYv3zHMfe8K0EFkhn0Z1O5g67NkPdJQv2s18ZX-70dMlq4S_2Ha0viXugjSSGYAeWmXMKXYTIoUjOyJ_ZhizBy1bmZQNapPvmymkaoW-Eyb2Y80RnwvF4wX-KoWER-n78e_ljyaJGVL_803QaLjEHd5n2kUKzTIhpeROjLFqUu8GFnx3oLc0bc_nFjrpbr0TfM84y0C-eUB8XpzT_XfDr6kfYVq9BSUwlpvOFeqQ9if7y0sf0yN-lvAW9pRdlXaLwbRXZPMFzK03onc5rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که تمامی موشک‌های پرتاب‌شده از سوی جمهوری اسلامی در صبح دوشنبه به سوی اسرائیل رهگیری شدند.
ارتش اسرائیل افزود که پرتابه‌ای که به یک زمین باز در کرانه باختری اصابت کرد، احتمالاً یک قطعه بزرگ باقی‌مانده پس از عملیات رهگیری بوده است.
در همین حال، پس از آنکه هشدار اولیه در اورشلیم درباره حمله موشکی جمهوری اسلامی صادر شده بود، برای این منطقه وضعیت پایان هشدار اعلام شد، زیرا موشک جمهوری اسلامی موفق به رسیدن به خاک اسرائیل نشد.
@
VahidHeadline
به گفته نیروهای امدادی اسرائیل، اصابت یک قطعه از موشک‌های شلیک شده از ایران، به چند خانه در یکی از شهرک‌های کرانه باختری آسیب وارد کرد.
در این حادثه مجروحیت گزارش نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 458K · <a href="https://t.me/VahidOnline/76044" target="_blank">📅 09:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=B-JJVE_zBGYvUS5_21-LhMlVMmiclF72EG4DI0fVlrDNF1rXG4PiYbl7hdYCe5kSHxCZw_AXz5yN4QFkp4JjwnOGFFWJ8IqGIA3kZqrJMdvCgUdXTmgrq0p--N1cDqtzSwY6_3fshn0T8ne_7cg1xuptHDE2vXkTBnn0QV9RxsdOkqAJQn3nMo_li6aTZZQ_Vo_FOoWatCpz2XxgmeZ-KvX2h8xd0JFittJcXkfjpuBQLtw_HuyEgGSvLw_0ihhY9sdSTltBT617V0rFs-hd5Ip833nkzmLOkg53zuzdf-VhWdludNV462REDPStHRgycK1In5ERtma7lTTPl3lpwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e89e6ed06.mov?token=B-JJVE_zBGYvUS5_21-LhMlVMmiclF72EG4DI0fVlrDNF1rXG4PiYbl7hdYCe5kSHxCZw_AXz5yN4QFkp4JjwnOGFFWJ8IqGIA3kZqrJMdvCgUdXTmgrq0p--N1cDqtzSwY6_3fshn0T8ne_7cg1xuptHDE2vXkTBnn0QV9RxsdOkqAJQn3nMo_li6aTZZQ_Vo_FOoWatCpz2XxgmeZ-KvX2h8xd0JFittJcXkfjpuBQLtw_HuyEgGSvLw_0ihhY9sdSTltBT617V0rFs-hd5Ip833nkzmLOkg53zuzdf-VhWdludNV462REDPStHRgycK1In5ERtma7lTTPl3lpwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@
iliaen
ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد
به دنبال گزارش خبرگزاری فارس مبنی بر حمله به مجموعه پتروشیمی کارون در ماهشهر که خساراتی به دنبال داشته، ارتش اسرائیل حمله به سایت‌های پتروشیمی در جنوب غرب ایران را تایید کرد و گفت به اهداف متعددی در مجموعه پتروشیمی ماهشهر حمله کرده و جزئیات مربوط به این حمله را به زودی ارایه خواهد داد.
ارتش اسرائیل پیش‌تر گفته بود که مواضع حکومت ایران را در غرب و مرکز ایران هدف گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 452K · <a href="https://t.me/VahidOnline/76043" target="_blank">📅 08:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=qOe0GSMBpTxS_HdRFdESRHSMIo7Z3oJmF-VQjm22n_F125QqyqfC7gVf1wTtEgcBpMYudFPZ1Ckvet7vvD75qduF9iE8-RCxs_bHuMIsBuk6IJtC8G855O7zKfZiHIcW39vMm8fpvU-R-NcuQtLtiHuCP0fcm7cOwSRQaa_NNZLeB5ZKI4BiFkkFsV5tchpJqNxCpxRQUtpne2NoB8rQzYPqsUpig2FOfR3UPlFizBycxsF1Qfw7JH5cu1CbR2XCK7D5T1l0CSge-U85LxPJdpKT5ZXtw8zlU9_HmTEKG9G31QXR9etvYG_t35EGMvJeYF7JtrUUsfn4IqNqIPC8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ac9a29e4c7.mp4?token=qOe0GSMBpTxS_HdRFdESRHSMIo7Z3oJmF-VQjm22n_F125QqyqfC7gVf1wTtEgcBpMYudFPZ1Ckvet7vvD75qduF9iE8-RCxs_bHuMIsBuk6IJtC8G855O7zKfZiHIcW39vMm8fpvU-R-NcuQtLtiHuCP0fcm7cOwSRQaa_NNZLeB5ZKI4BiFkkFsV5tchpJqNxCpxRQUtpne2NoB8rQzYPqsUpig2FOfR3UPlFizBycxsF1Qfw7JH5cu1CbR2XCK7D5T1l0CSge-U85LxPJdpKT5ZXtw8zlU9_HmTEKG9G31QXR9etvYG_t35EGMvJeYF7JtrUUsfn4IqNqIPC8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اصابت موشک به شهرک یهودی‌نشین ایتامار نزدیک شهر نابلوس و در بخش شمالی کرانه باختری رود اردن
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/76042" target="_blank">📅 08:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76041">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBR5wayG9A9lSu0zaWjXZw1PlRbYCdJsk5l0t5XkN4zP0-6CK90GKukwxrvZwWq8UXLH4m5EKthgJgcf4dZqFmxvV_uMPEEITdpLY3sJ8xEAoU3-Z_QjGKJSg-D3dwuFlj9p2t1rchsNgmoFkw-0LdLrx-gi5FTPkMBCGZGOpt5z6CmfVZSVuIiYUldK1CV2pC4SJjm3H-4szcSDkXxUsoQHTaR0Xq5Og1Gjh3GDgLyM4515PaOXRb4o1Un87EtKeNbHuMqk4K2Fj2PxeeJDacaHPkICqP_VGplVDBUlT0sRGmuExjLABuHK5tA0ZufEqVwqWQc7Q2L91AK-ej5rAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بامداد دوشنبه از رصد موشک‌های پرتاب شده از سوی ایران به سمت اسرائیل خبر داد و اعلام کرد: سامانه‌های پدافندی در حال رهگیری این تهدید هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76041" target="_blank">📅 08:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76040">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌های دریافتی در پی گزارش‌ها از شنیده شدن صدای انفجار در ماهشهر:
وحید پتروشیمی کارون تو ماهشهر زدن
آقا وحید سلام پتروشیمی کارون منطقه ویژه ماهشهر زدن دستور دادن کارگران و پرسنل برگردن خونه هاشون
سلام ماهشهر پتروشیمی کارون ساعت ۷:۳۰ یک انفجار رخ داد
وحید جان منطقه ویژه ماهشهر صدای وحشتناکی اومد. میگن شرکت کارون رو زده
آپدیت:
پیام دریافتی: کانال ماهشهر هم اعلام کرد
پتروشیمی کارون رو زده
اما صدای انفجار مثل انفجارهای قبل نبود
همه نشنیدن
معلوم نیست با چی زده این بار
🔄
آپدیت:
خبرگزاری فارس، نزدیک به سپاه: " تهاجم هوایی دشمن صهیونیستی به شرکت پتروشیمی کارون ماهشهر
حیاتی، معاون امنیتی و انتظامی استانداری خوزستان: دقایقی پیش شرکت پتروشیمی کارون ماهشهر مورد تهاجم هوایی و اصابت پرتابه‌های دشمن صهیونیستی قرار گرفت و بخشی از آن آسیب دید.
خبر تکمیلی در خصوص خسارات و تلفات احتمالی متعاقبا اعلام خواهد شد."
‌
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 426K · <a href="https://t.me/VahidOnline/76040" target="_blank">📅 07:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eCLt7IZL77KShOuYb0l9Do389fnvgvKmrNGRCXsohyMcbsoQoVakuWPUgnX6oHqvnI33_O0gvKxP9YrcoJS3eK1yXfY3UU85FYMmnSFLEbz_ZB1drDPB0zfhYiHY-5bp6y7-1KvvA5XXnjGm-8z9w694u2BTRyo0XoKpg496g1sDTC4_gIjuO7v_y-AURRpfdMQz3j1Yc7gWqi3Q9SPc8IgdwVi5j3lzGUjZmzB4-WbBDR3rr7ac5IASJdmOKne_XnS0gMwKCDZVY7_NFZ-kP4rK92xx0ELXOesHOgXPrIujhbe-bDHFx0v9jL9A1FrRujkmUAgFbMAxNLn5XYo-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pecAYElhVz4BG_NJCVwNEHtLX7UahrrByDsHd02298htu_0JNLdwQ7Z8RJ_vJpV8r9zJJ-Ar-w0xaiD2pg2_V1MWvOHU7KBqVbvrFhRGGN4M3MCCXcW2V5UVEcgFmRK5fOxYwKvlcDWqFauuhLYsq-dQ3Wbv-A8gQeb8oL4gKq-7E5gc11y_hMAUZ4r40sMsycA5Ew8uoc5YGrH6Zf6Z8dre8VEpL1z81eKiM2v8hdyNg1GWRe9PDXVH3B5mxv-yAtvCMg73rmTN4XzL6pnfipphl4PtVqHe-YfxfOVyJlbKuOr0IKILsqCbmVX-WsSBS4HCA72vbgE1OcUxS7B4lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VI22V4Axc52GtwUo2KiOZEPaRO8Yzyqz9Ezhvr8JHaORMnLdusy-q6FYQM9c5pG-aE4tqrOdWTmiEL5qe8si7o9h3anhYSE7GtYoZ5LXTOJ0KtxSwxGkmLRzxWOiB0WRNFKpkQpNgE1g7GaHJ7kSkQrh9oZhERJBttNwynXsHzlvwMDtETDBZ6-08MDJvbN5h3j9u3B46fh3NrFBom8loT71IYOn1y-KCRsGO2lGg2_FpjR_OMt07j5amckOwo0yfe8mYO0vJR3yKCYTE0CHMqtnGzUe1pmqeOR6hKkGf76v2qIXj8e8CXoCq8SZxN7jS5BILsF382uCBsF6Vax0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KUiqLRNS-eYJP1eaGJYxcxcZdWtg9TAKnHugN1rGCtvBr07y3HMObxT6RqPxNLPC6haaHHS80YekliN5gxKHQrVHyxSiss8TE5kO907F7gducxpThZYBMUEvo9iXWwTyE6a9luTfC1iH5fjpwVpDXwI5-iCyXoavtkcweossq4Be-kmW86JWSwhKyZQvSMRu7pwxT52Bui0xQOWsb4QrIFfXHEsgas7Ugl8HFPcrVvvnIAzuIjva7qesK_d-0HPgYio948o08Pf7KLT_MbUUYVTNBYJ35dkhFbw-7n9PM5n5kwVD1QX0coqPHmD2kPr74DO5FjushHdAi0JDLOuAJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/D6jQhhMusmHau6VxoqMl8Xhj1gJr1xXUa94F7uwG3KyJ2OcrYy5iflNsokNpMfyl9sEM4tYz78SPBzLihqBmpuKVvSPVkQZv0-pRe054se11JFC6Kkj_UiB51hvTuq5k21XToTAQzqgXBR2rrkCBAjJSyD1Yl_u9SnAxe_0cSo-Hvwhv5PI5GAqlIPm5_egYz-j35pkdqXkOxaCPveRmYg4C_8ob0PnlbRfxWsmr92DxzeK59W7c4oChIC8dbchRDPyXQBtYD0aXHzU7sr1e010K41fP1KS6CJOTEWyPmbaZPPWRHTBwlZIsPrC0YG48Exh_Q_zqyeIsEBSoXpavBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=vrsA-bdIB0h45HSAxHWA9rUE1ob0E1QjlhOnj3vsQ2Jbl1HW52jCRp-ItKf-1qtUTW_DKhkRACRaDxD8qxGSS_anB7Eafbr9rvFbhez9xpLURKbyHt1nHsdn2ZWVhyUJIMwTdd1D9UdBZlpauYbyewVYmcg451LZoMPe2cP_o0AdPzdeL5Mo_GkaI1S06tNlWXZpwJ_Z22xLTiDxxjerG6f7iO_O_Sqw09jMKh7f03cFoWEq4dldnWb8HWxGNxNtx492LVv9VwaFLsTL_gVUa1KSe235D-eV5EXlWFLb1uX1EQhIvzH7NuIw8lbSPcSd8RhWv8ywrgZZhS4CHt796A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/08feac2b13.mp4?token=vrsA-bdIB0h45HSAxHWA9rUE1ob0E1QjlhOnj3vsQ2Jbl1HW52jCRp-ItKf-1qtUTW_DKhkRACRaDxD8qxGSS_anB7Eafbr9rvFbhez9xpLURKbyHt1nHsdn2ZWVhyUJIMwTdd1D9UdBZlpauYbyewVYmcg451LZoMPe2cP_o0AdPzdeL5Mo_GkaI1S06tNlWXZpwJ_Z22xLTiDxxjerG6f7iO_O_Sqw09jMKh7f03cFoWEq4dldnWb8HWxGNxNtx492LVv9VwaFLsTL_gVUa1KSe235D-eV5EXlWFLb1uX1EQhIvzH7NuIw8lbSPcSd8RhWv8ywrgZZhS4CHt796A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
۷:۴۰ پرتاب موشک از بیدگنه
بیدگنه شلیک موشک بالستیک همین الان
همین الان ۷:۴۰ موشک از بیدگنه رفت
دوباره از ویلاشهر نجف‌آباد موشک زدن
وحید جان همین الان از کرج موشک پرتاپ کردن
7:39 دقیقه از ملارد صدای پرتاب موشک
یکی دیگه همین الان اصفهان
شمال اصفهان یدونه موشک دو دقیقه پیش پرتاب شد
الان دوباره موشک زدن ٧/٤٢
اینجا،اصفهان یک بار ساعت ۷:۳۰ دقیقه یک بار هم الان،۷:۴۰ موشک پرتاب کردند.
۷:۴۰ از سمت ملارد انگار یک موشک زدن.
وحید همین الان از جهانشهر کرج صدای پرتاب موشک میاد خیلی صداش شدیده.
سلام وحید 7:40 صدایی شبیه به برخواستن موشک از نزدیکی مهرشهر کرج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/76030" target="_blank">📅 07:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VQyg2mFMkjmfyr0LXos0ZQaM9ZBv-fTXw8QD589Degt24De-wcRIg2XEJV-q5NoqVZV24MNH7EjVmCZBzhYUpfaqGJG5O2utv3BCWDqgPC84yAJ51K_aTyemqWNCgkhLcnX7W7Ax3pGpSLEfrjb3j4mXTch1R_7ygYgYKNHXOrzy-E5WOAtRIkXqOmr8kED2K7TE0ANla9DWs2Vg1_T5-oDq83WHw31Qkq0J_1k863Mi7lKg5KMeiPc3Qebem3pS6QoBzKlybEdhSktx7SjdB-QmUBaoAC5bYZPJqUkZT2wJWai5h2J1u5n1ekMf91rHPvSZy973IeRSZtGj_8j8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
۳تا موشک از کرمانشاه همین الان
وحید کرمانشاه همین الان صدای وحشتناک اومد
سلام ۷.۳۰ صدای انفجار از کرمانشاه . احتمالا پرتاب موشک
سلام وحید جان
7:28 بندرماهشهر صدای انفجار اومد
وحید 7:30 دقیقه ارومیه یه صدای سنگین اومد
الان ۷:۳۱ از ویلاشهر نجف‌آباد موشک زدن
الان کرمانشاه صدای انفجار شدید
شلیک موشک از ارومیه
خرم آباد 2 تا موشک از پایگاه امام علی انداختن
از ارومیه موشک فرستادن
پرتاب موشک از نجف آباد
اصفهان شلیک موشک
سلام وحید جان از خمینی شهر یکی زدن
آقا وحید همین الان شلیک موشک از فلاورجان اصفهان
شلیک موشک از ارومیه
با صدای انفجار زیاد
سلام وحید آنلاین همین الان ساعت ٧/٣٠ از اصفهان موشک زدن
سلام وحید جان همین الان موشک زدن سمت اسرائیل از اصفهان
موشک الان زدن از پادگان پشت ویلاشهر نجف آباد
سلام ماهشهر ۷:۲۶ دقیقه صدای یک انفجار شدید اومد
از کرمانشاه ۴ شلیک، نه ۳ تا
ماهشهر حدود ۷:۳۰ صدای انفجار اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/76029" target="_blank">📅 07:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIU14Z-_KarbrWrynZP6cykdcz-D5CnU_0ZEdlBe70TU6SdXj1ywfbyyqx3HziYC8SH20DhtukaKfcaNtGORsRb7QKBV5u32b4WqAN6BJUYw3K3WWGpkBbzOmc3uu3CuzaQPD3bLwy3qeNiKF2VhV7JDLw7LtmG--S7tmYajq0pYKQDZenmQACKZT_j9VJ_y0of4CAe2-U96JZsOXZ8tideJhgZZRT3IO0QmFuCMtU3rYRK5B7z5urOB_cCd-Erv86gnHhSmjWSL3-1ANimlWhTJbHmuwbgtWAnU9k2LCbEneJzJ_oVU8Oib4_hQblPwkVM09uEPhpuXt5fRNTXe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی بعد از موج حملات موشکی ایران به شمال اسرائیل، خبرگزاری تسنیم، نزدیک به سپاه پاسداران، در تحلیل و تفسیری درباره ابعاد نظامی این حمله گزارش کرده که در حملات موشکی و پهپادی یکشنبه شب، سپاه پاسداران از «پهپادی ناشناخته» که از موتور جت بهره می‌برد، استفاده کرده است.
کارشناس نظامی تسنیم همچنین از شلیک موشک‌های خیبرشکن با کلاهک‌های خوشه‌ای در جریان این حملات خبر داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/76028" target="_blank">📅 07:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76027">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rg1uhIcUHcirweXmiww7G4iHn-_GbZpQOY2Vn8YH4hHW_G7QmgjxFCjNxpve6yvyEHqHu9wllYgD6oNEyEldi-wda9HPl9Pj8Ph9KWI5sPqDh8q8j5RBDWzGHbWyQxb9FXItbcU7WRDD51MbO84oVamcrK5Q1GLN1voLABGZzag4xuo25ks8vD702IfSpH1GBwjvFizZh5fuWKf6zwOvj1nRL3YAW4RKeTl0x30AMl8UG4eVMVLOMuH3HBRifrhSeTuoe8ehcG5sw6gw-iG5A-c_wWdjAu-nLa5i4o9504xgj6wbitIgd0rghA7FfHNYCKLhlT5ev_35hphaUOXJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخیئل لایتر، سفیر اسرائیل در آمریکا، در پیامی در اکس نوشت: ارتش اسرائیل پس از شلیک موشک‌های بالستیک ایران به سمت اسرائیل، سایت‌های پرتاب موشک زمین‌به‌زمین و همچنین زیرساخت‌هایی را که به بخش انرژی مرتبط نبوده‌اند، هدف قرار داده است.
لایتر افزود: «ایران امروز ۱۱ موشک بالستیک به سمت اسرائیل شلیک کرد. هر یک از این موشک‌ها می‌تواند یک محله کامل را با خاک یکسان کند و صدها نفر را بکشد. هیچ کشور دارای عزت‌نفس در جهان چنین حمله‌ای را تحمل نمی‌کند و اسرائیل نیز نخواهد کرد.
سفیر اسرائیل در ادامه نوشت: «مردم لبنان، حزب‌الله به‌عنوان نیروی نیابتی ایران را رد کرده‌اند و به ایران گفته‌اند از کشورشان خارج شود. اگر حزب‌الله به اسرائیل شلیک کند، مراکز فرماندهی آن در ضاحیه به‌شدت هدف قرار خواهند گرفت. این موضوع هیچ ارتباطی با ایران ندارد. همه از این رژیم ایرانیِ دیوانه خسته شده‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/76027" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDM2neptRwqXsJlTXGI3dkJsf24Yny-YaX3wLm7t_HtoE9J_5KyQBsaksas6STg3ZqYNQiGzNcQ3Uk9zhzDp391wNZn4KleQy2GgFGJxR11hAEpAZtYMHL4u-IM8K1913Pn22xcupxdSAOe5X1bv5soFTqXVzISM7OXTqAq4U0omhV9JN2KThr-NTIaDH6SshRDr8HGiDF8F0FCDvcmAN_S2bvL7KA8ExHVlvC9LmZMCcnBfDDkWPQSIUz5wqOhpZwRcmycNHEqW04Tde_yXgHx44tg9hQcSgU2wZ4pXZNrG9jGXsULyFrcuUgevbrNwZ4MUkixUpYidaH-YVPTKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
یک مقام آمریکایی به رسانه‌های این کشور گفته است که ارتش ایالات متحده در حملات شبانه اسرائیل به ایران هیچ نقشی نداشته است.
نشریه آکسیوس به نقل از یک مقام وزارت دفاع آمریکا گزارش داده که این حملات اسرائیل «نسبتا محدود» بوده است.
این گزارش در حالی منتشر می‌شود که دونالد ترامپ، رئیس جمهور آمریکا، پیش از حملات از بنیامین نتانیاهو، نخست‌وزیر اسرائیل، خواسته بود در بحبوحه تلاش‌های دیپلماتیک جاری از اقدام تلافی جویانه علیه ایران خودداری کند.
آکسیوس پیش‌تر گزارش داده بود که آقای نتانیاهو به صورت غیررسمی یا به تعبیر این رسانه «تلویحا موافقت کرده بود» که این درخواست ترامپ را بپذیرد.
حملات شبانه اسرائیل ساعاتی پس از شلیک موشک‌های ایران به شمال اسرائیل انجام شد و در حالی صورت گرفت که واشنگتن همچنان می‌گوید در تلاش برای نهایی کردن توافقی با تهران و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76026" target="_blank">📅 07:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76025">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcfELKgvQkhDrJaepSIejYe9D8tmauxmLgPYadU3rql8uba3uTvdDcuF1E2wOnKqRpJX2bPS7BgPa-ZbRvdFqHrVHqfnpfQYjTqKBzf_IiUkMPcR9Eyn27h5AQvnQGurf7t66BGEQ2E-jdwH8Ohp0OPRueeW8GS-rhP3JecU6e7lJxXgRKCa23M9dFS6jNIyGlYxlZk-BNvFODDfx8pSZ9mRyI017YPcN1Qm5thBX6L4FWt5sQ0Xx8Yl0Nia08Zdd2iVDdPzmCOLrbzucTfELgdKCAAF_6Fad5Xzbleivqg_Uf9ibb5lGdy9F5r18JwSllQUdXOM_dxwG9fZbSusaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل پس از حمله‌های یکشنبه شب سپاه به شمال اسرائیل و حمله‌های متقابل ارتش اسرائیل به غرب و مرکز ایران در بامداد دوشنبه اعلام کرد که ارتش اسرائیل یک موشک شلیک شده از یمن را رصد کرده و سامانه‌های پدافندی در حال رهگیری آن هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/76025" target="_blank">📅 06:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76024">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vai3Os2Bg26YdQuAHO5XgNmQNZkhgL9v0_ELsx3QXGM1pTbpsv7gsaxVpkl6UcZ2wXP84-ktApTfeq0AOVkT5am_hdKXwW6zrgIT1JvgxkxlfvnMAhqKewGcNule84DkKnaFYQbyjRQKWg95j1MKTHsoyu5YzyX91Zq3BTjVl8DqNjWRneHe2PgoN4PIaVCWdytL-ZXdeR-W303t77K88t9bGV9bPpJNHcKW--6su5HE9o0cNrC6-VrvAaaIn0ciPN4_TMHzasOzc01o-RKsVUB-oRrjs17zgiiEwVA7Pcrw6ZIfwRyxoSzdfJBOKKR7sT_b0yf-2AXcIwJkq0R-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس گزارش داد که عربستان سعودی در منطقه‌ای که پایگاه هوایی شاهزاده سلطان، میزبان نیروهای آمریکایی است، آژیر خطر موشکی به صدا درآورد.
@
VahidHeadline
آپدیت:
خبرگزاری صداوسیما، وابسته به رادیو و تلویزیون جمهوری اسلامی، به نقل از «یک منبع نظامی» اعلام کرد که جمهوری اسلامی هیچ شلیکی به سوی پایگاه هوایی در الخرج در عربستان سعودی انجام نداده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 361K · <a href="https://t.me/VahidOnline/76024" target="_blank">📅 06:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76023">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBzyDgG8Ii8P74iIffBW85hLpthblHZNvYrZKhDpanen00mHEyjyrsrR9qkwoUwyHizS3DramtTV-1Z44OEWx42ylRtL6Dbv78e7LQ1BZGuIVNJbVtLgCsmjuA-g8829eVIPO06h8qmweJapW4IWX4bwDV2neg_vNCttDSQ-mH5b7fKlQl0xbVXR30LCZkRXXH_BVwxL9N65pBRuvMdu5jNYrlDLUzxEXTWLrZgVvRhBTGyHio8X_-OSmkraRS_xmJT88OXFk5NUWy7A2nSt-81ZTOJsqDph-bRgKMTaCwg5AZ-R18dudCwA0nY0Rz2kfIJ4hoORt51UHH-KwGkMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌نشانی تهران اعلام کرد: صبح دوشنبه دست کم صدای ۲ انفجار حوالی ساعت ۴:۴۳ و ۴:۴۵ در نقاط مختلفی از غرب تهران شنیده شد و ادعاهایی درباره هدف قرار گرفتن فرودگاه مهرآباد منتشر شده است. سخنگوی آتش نشانی تهران از آماده باش آتش‌نشانی خبر داد، اما اعلام کرد که نقاط شهری در تهران هدف قرار نگرفته‌اند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/76023" target="_blank">📅 05:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76022">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V3K7pvZQJ74HSIheHcOx-MLuS8SHCuLe07L8FoLxQIw9ZkEc256jGPelgVYbglJf-gonhzD_NdaESNMeihW5kqIdN92Z4GFbh9JMXlJxrmHpSXABbFfH-262roRvR8s8ceYU8X2xyMnG18QT9_vsH1FaHQJcdcLkiTdtv9J__hSUxzykUhqA-qnXRka79IMRtWwuEK_go_Nq6JLCfW82nxadPMBv-ZlG0e-p19ExleDmBSzAWReyPI4nhtI1TOUS4L6EI7c9-Ma7YZb_mxeajsBfiERVU0I_P4EF-RA685vq75cz12M-3i6l1sgjKK9PadcYycMltPEiVItQNwKuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک خبرنگار اسرائیلی حوزه دفاعی به نام امیر بوخبوط می‌گوید که نیروی هوایی اسرائیل صبح دوشنبه به ده مکان در ایران حمله کرده است که از جمله سامانه‌های پدافند هوایی و موشک‌های بالستیک در آن‌ها قرار داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76022" target="_blank">📅 05:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76021">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UoXo4XwKDxkbYKmbSyqu1RwfWNC0xf9CdadBcuT8t-P7x-6Sl7uZIEJw6I8KqPZeXfVQkGqmy-t_iZkpwc4fTI63iWQE0_D3gQ78U0XPkb-_Lj3WSsJUotbbKdFoR5i9SDxEDGLf0bz2PRnF-r9TX5vqcVYB1DMwv_od4xrBXAC7e0ei415B37qt7NSP6bBjdIBqVWs5u_g00H2OHXKg_KVbeevBr1HQuthjcACu4FSa52cOAAdg-jIkImmEDalVeWNNlBQoS9gfCQbcThHnPuBOEeKGVBccgSDRUOp46r25iY587A-a3Q_rXZuPNXF3LwRpDx6WioGfG8br1jjZkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درپی اعلام حمله هوایی ارتش اسرائیل به نقاطی در غرب و مرکز ایران، سپاه پاسداران انقلاب اسلامی بیانیه‌ای صادر کرد و نوشت که اسرائیل «با استفاده از موشک‌های بالستیک هواپرتاب اقدام به حمله به اهدافی» در خاک ایران کرده است.
ارتش اسرائیل حمله هوایی به مرکز و غرب ایران را اعلام کرده اما هنوز نوع سلاح‌های به‌کاررفته در این حملات را اعلام نکرده است.
خبر این حملات درحالی منتشر می‌شود که یک مقام آمریکایی به اکسیوس گفته بود دونالد ترامپ، رئیس‌جمهور آمریکا، روز یک‌شنبه در تماس تلفنی با بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از او خواسته بود فعلاً از حمله تلافی‌جویانه به ایران خودداری کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76021" target="_blank">📅 05:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76019">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iTbYht3G06viGWpYjwBS0EUwkCe6avrx6Hqno9EJQJiJpNQZFgzMtJZI3ZYjR58bCc0_C-3TJepuZIncOIbxBVGqB4i6QAbC5ZmhoQqkDmzPzx4SaesVJSaYkwj0pnS_Tb4ADN8LU2oMFvdLzJth__ixB_7vq_qEh23yXud81cyBl_moqyrwUHqyecbE5sDFwywr0bGWGwdNbPPHup521Jmg7-jeFca-QNuYE0mzrTJvXAuB-GxH9s7G_9gLnRPB-_16yDv5YkYzLhguoy4PBKWpb9DYG4P9LhurS4jcCC_adL_cXpyY9ZqN5X4m4zhE7QBaZBmYFHQSCwwIjOJJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/itceta9F42w9irAQbHoGRKO7VvHu5iezQs6nhZMYtTyv50GRemHevdBwVOY4HYmTeRyBvzpYt1_rfpe9vjiHejqj7qE5kGfYRzutJyO3Az5fzIXIF8NQHfTOtnGZrIUHSfuzuhHO9aazobsvsATHRGR1xg11ozHX7SIzI-jo5y-x2FiziwpamCJCsWiENX1kEsHOxmaFttBCWZQOCeIrdV2HnC0p_-eXgjIheNTOtQqFgb61mHhOCHydi_fZPh6mkvblCP3p8e_5fnEZmQiHLgckO_iRgBx3p7a4CS4v3JlEtEZ-_qIQ2uXhdJNfjmJKgRMvbrQwAUWT5cbRm2fZTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کانال ۱۲ اسرائیل از حمله نیروی هوایی این کشور به فرودگاه مهرآباد تهران خبر داد.
@
VahidOOnLine
درحالی که هنوز ارتش اسرائیل اعلام نکرده حمله‌های بامداد دوشنبه در پاسخ به حمله‌های یکشنبه شب سپاه پاسداران به شمال اسرائیل را با چه تجهیزات و تسلیحاتی انجام داده است، کانال ۱۴ تلویزیون اسرائیل گفت که جنگنده های اسرائیلی اهدافی را در ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/76019" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76018">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mo6uTOaArz4jAGbdShX6V3y-jIlPiCk6XU9RAE7XGyxPbqMDvXKLhRFFOTPSs5lCFVJxa7hGJxfZw7V4ohBSH2BoObOwUKBxt3o-dv_j7QZfJamZABaArq_It3NFrNgoPIJErMD0ewf5vW6Iz9n5NqEUud_3fx7SweCshKPl5IDFqMeuFxSZog8MbPEgEgkfx18CB9m7DMWulXNdxOgz4Y0R_yBmXaJC_RTkmcErJy14j0Dm8BazTLZPKjCb6mZSInuyIflIxeCyhFwu7nYT9XaKWII57ATgKoUNgJlmlJ97ZqCFxuKbzEROMaJCbG9cVUdsVmZ5BNPDJf92naImqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
نجف اباد ساعت ۴:۴۰ فکر کنم با پهپاد زدن
سار پیام‌های دریافتی:
کرج هستیم الان  دوشنبه ساعت ۴:۴۳ دقیقه صبح  از راه دور صدای انفجار بسیار بزرگی اومد
سلام وحید سمت شهرک غرب ۴:۴۳ دو بار تا الان صدا اومد خفیف بود
ما رباط کریم هستیم
ساعت ۴:۴۵ صبح ۴ بار صدای انفجار اوم
وحید ساعت 4:44 صدای انفجار نزدیک سمت جنوب تهران (باقرشهر)  شنیده شد طوری ک خونه لرزید
سلام،چهاردانگه دوبار صدای بلند اومد ساعت ۴:۴۳ دقیقه
سلام وحید سمت مهرآباد ساعت 4:45 دو تا صدای انفجار شبیه دوران جنگ اومد
ما شمال غرب تهران چند دقیقه پیش و دقایق قبلش صدای انفجار مهیبی شنیدیم ولی دور بود. صدای جنگنده هم نیومد
...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76018" target="_blank">📅 05:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76017">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YrgqUscBntjbBn1VdWnGyu0h9qdr1fja6W_FWMvedYzPYKHG6PgG3r1WwjY-q62oWrG8JcjXMtSXxuATIMTdOUX6iBRvFcvp8zLsQekox4hAjei-qT_U5GVPKTR6SHAReRsmB7krIHzq_njNFWiw1d_k_honHmaXXvXrDxXy0SBQLMKyzbJvFSR4meX7DCxbnBC68iXcLK13b2pzRXdJxTJO1epDA4YukEZPeYFWvYM8xXZeefTs3B1biLxYjALUD5UUTOBhnDQWDF3rUvqU4U83W5ae0tifdgv1Z89kOLh5rxzw2DEln8b6wqqjx4tHr_i7LvyuRSdaiXTs16BbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👆
دریافتی با شرح: نجف‌آباد
سایر پیام‌های دریافتی ساعت ۴:۴۵
سلام ساعت ۴:۴۵
سمت خزانه دوبار صدا انفجار اومد
صدای بمب جنوب تهران ۴:۴۵
سلام همین الان صدای دو انفجار از میدان المپیک
داره میزنننه
فردیس کرج ۴:۴۵
همین الان صدای مهیب سمت مهرآباد
ساعت ۴:۴۴ سمت غرب صدای عجیب و بلند اومد ، لرزش خفیف سعادت آباد
تهران اندیشه
دوبار صدای انفجار همین الان
سلام اصابت موشک غرب تهران تا الان دوتا انفجار 4::44
صدای دو انفجار با فاصله کرج
ساعت 4:43 دقیقه غرب تهران صدای تک انفجار
دو دقیقه بعد دوباره صدای انفجار اما دور تر
صدا انفجار داره میاد سمت غربه انگار
دوتا صدای انفجار غرب تهران
تهران زرگنده ساعت ۰۴:۴۳ صدای دو انفجار اومد
الان ساعت 4:43 دقیقه و 4: 45 دقیقه صبح غرب تهران صدای انفجار کوبنده شدید
همین الان دو تا صدای انفجار در اصفهان شنیده شد.
سلام وحید. شهرک اکباتان. صدای انقجار اومد دو بار همین الان. ساعت ۴:۴۳ و ۴:۴۵ دقیقه
صدای انفجار , کرج , ساعت ۰۴:۴۲ , ۱۸ خرداد ۱۴۰۵
صدای انفجار , کرج , ساعت ۰۴:۴۵ , ۱۸ خرداد ۱۴۰۵
کرج صدای انفجار 4:45
جنوب غرب تهران دو سه تا صدا مثل انفجار از دور اومد
صدای دو انفجار مرکز تهران ۴ و ۴۵ دقیقه صبح
یه صدای گروم مانندی اومد اما دوره مرزدارانیم ساعت ۴:۴۳ بعدی ۴:۴۵
سلام وحید جان ساعت 4:40 دقیقه رباط کریم حداقل 4 تا صدای انفجار اومد
ساعت ۴:۴۳ و ۴:۴۵
۲ تا صدای مهیبی اومد نمیدونم چی بود
سمت خیابان زنجان
زد صدا اومد شهران ۴:۴۳
دوباره زد
نزدیک نیست ولی صدا میاد
۴:۴۵ تهران شهران
وحید ۴:۴۳ صدای انفجار دریاچه چیتگر
کرج مهرشهر دو تا انفجار به همراه لرز ساعت 4:40
احتمال میدم سمت فردیس باشه
وحید تهرانم سمت شرق یه صدا هایی میاد شبیه انفجار ولی نمیتونم تشخیص بدم
۴.۴۵ دقیقه تهران سمت غرب ۲ تا صدا انفجار
سلام غرب تهران دو بار صدای انفجار اومد
سلام وحید ساعت ۴:۴۵ دقیقه شرق صدای انفجار اومد.البته دور بود.
وحید ۴:۴۲ پرند صدای انفجار مهیب حداقل دوتا
سمت م معلمم یافت اباد
همین اطراف بوده صداش همراه با لرزش بود
دوتا صدا انفجار 4.43
وحید جان ساعت ۴:۴۵ سه تا صدا شبیه انفجار سمت غرب شنیده شد.
وحید جان شهرری همین الان دوجا رو زدن شیشه ها لرزید
ساعت ۴:۴۵ ۱ انفجار دیگه شنیده شد
دومی صدای مهیب تر بود
جنوب غرب تهران سمت تهرانسر همین الان صدای دو تا انفجار اومد حس میکنم موشک بود
سلام تهران سمت شرق و غرب صدای خیلی بدی اومد
۲ تا پشت سر هم ساعت 4:43
مرکز شهر سمت ۷تیر. ۳تا صدای انفجار از دور اومد الان ساعت ۴:۴۵
وحید جان صدای دو تا انفجار به فاصله یکی دو دقیقه حدود ساعت ۴:۴۴ از نزدیک ستارخان شنیدم
سمت صادقیه تهران تا الان دو بار صدا شنیده شد
از ساعت ۴:۴۰ تا ۴:۴۵
اما بنظر دور بود معلوم نیست کجا بود
سلام مرکز شهر تهران ساعت ۴:۴۳ دوتا صدای انفجار پشت سرهم اومد ولی صدا دور بود
سلام اسلامشهر ساعت 4:42 بامداد صدای خیلی بلند اومد
صدا انفجار تهران ساعت 4:44 سمت پیامبر مرکزی
دو تا صدای انفجار مانند اطراف اصفهان چند دقیقه پیش( فکر کنم نجف آباد ۴:۴۲)
ساعت ۴:۴۵ و ۴:۴۰ دوتا صدا انفجار اومد
سمت مهراباد
سلام اقا وحید ، سمت شهرری رو فکر کنم زدن خیلیی صدای بدی اومد من از خواب پریدم
سلام وحید جان  الان
دو بار بیدگه ملارد رو زد
کرج مهرشهر
صدای دو انفجار ۴:۴۳ و ۴:۴۶
وحید حوالی ۴:۴۰ تهران صدای انفجار شنیدم
دو مرتبه بود، اولی اومد بعد از ۵ دقیقه دومی ترکید
4:45 فردیس 2 صدای انفجار از دور دست
دوتا صدای بدجور اومد ساعت ۴‌.۴۰
سمت خانی آبادم ولی صدا یکم دور بود
ولی زیاد بود مثل غرش بود
شهریار صدای چند انفجار بیشتر سمت رباط کریم می خورد باشه
درود وحید جان ساعت ۴:۴۳ دقیقه ۳تا صدای انفجار توو پرند شنیدیم
سلام ساعت4:42دقیقه صبح صدای انفجار در اشتهارد شنیده شد 2مین بعدش هم بازم صدای انفجار صدای بمی داشت
سلام اقا وحید من اسلامشهرم با صدا انفجار بیدار شدم
صدا صدای زدن بود،سه تا انفجار شنیدم
وحیدجان سمت شرق اتوبان بسیج صدای 2تا انفجار اومد ساعت 4:45
رباط کریم صدای شدید انفجار
چهار پنج تا
غرب تهران ۴ و ۴۰ صبح صدای دو تا انفجار اومد اولی شدید بود از خواب پریدم
ساعت ۴:۴۵  دو بار صدای انفجار اومد کرج
تهرانسر ساعت ۰۴:۴۳ صدای انفجار شنیدیم و از خواب پریدیم.
اصفهان چند تا انفجار شنیده شد
ساعت ۴:۴۲ دقیقه، از سمت غرب تهران دو تا صدای تک انفجار اومد. یکی دور و یکی نزدیک
درود صدای چهار انفجار شدید اومد ما سمت نسیم شهر هستیم جوری بود از خواب بیدار شدیم
ما نزدیکی اکباتان زندگی می‌کنیم و توی پنج دقیقه ی اخیر سه تا صدای انفجار شنیدیم
کرج صدای انفجار میاد
قطعا حمله شده
رعد و برق و غیره نیست
اصفهان دوبار صدای انفجار 4:42صبح
هیچ صدای جنگنده یا موشکی نیومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76017" target="_blank">📅 05:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76016">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی از ساعت ۴:۴۰
سلام وحید جان
4:40 دقیقه انفجار از سمت سپاه تبریز طرف متظریه اومد
۴:۴۰: وحید ارومیه یه صدایی اومد نمیدونم چی بود
صدای انفجار شدید در ار‌ومیه
مشخص نیست صدای چیه
سلام آقا یک صدای مهیبی همین الان از ارومیه اومد ساعت ۴:۳۹. شب هم البته چندین تا موشک از اینجا فرستاده شده بود.
سلام وحید ارومیه ساعت 3:39 صبح صدا اومد و انگار زدن چون خونمون لرزید و دقیقا مثل موقع جنگ بود
وحیدجان نجف‌ آباد صدای چند انفجار شدید. ۴:۴۲
وحیددد
دارنن  اصفهانو میزنن
نجف اباددد  سمت ویلا شهر
دوتا زدن همه جا ترکید
لرزید داریم سکته میکنیم
شاباد موج انفجار شدید
سلام وحید غرب تهران صدای انفجار شدید اومد همین الان ۴:۴۳
وحید اینجا صدا انفجار اومد ۳ بار
خیلی بلند و نزدیک. ما کامل از خواب پریدیم
بدون صدای جنگنده بود.
نجف آباد اصفهان
خمینی شهر دوبار صداری انفجار اومد
وحید زد الان تهران رو
یوسف آباد ۴:۴٣ صدای انفجار از دور شنیدیم.
مجدد ۴:۴۵ صدا اومد.
۴:۴۲دقیقه همین الان دو انفجار پی در پی اسلامشهر
انفجار مرکز تهران ساعت ۴:۴۳
وحید زدددددددد
بالاخره زد
همین الان ۴:۴۳
غرب تهران سمت جنت آباد صدای وحشتناک اصابت موشک یا بمب
صدای جنگنده نیومد
دوباره الان ۴:۴۵ دومی  رو زد
توضیحات اینکه چند دقیقه قبلش برق نوسان شدید کرد
صدای دو تا انفجار همین الان نجف آباد اصفهان
انفجار لرزش شیشه صادقیه تهران
غرب تهرانسر یدونه صدا
اسلامشهر همین الان صدای انفجار مهیب شنیده شد
سلام ساعت ۴:۴۱ صبح، صدای انفجار شدید تو تبریز اومد، جوری که از خواب پریدم، قطعا پدافند و اینا نبود...
وحید جان از سمت قروه کردستان صدای سه انفجار شنیدیم با فاصله ۱۵ دقیقه، به نظرم موشک خوردیم چون لرزشش زیاد بود
سلام وحید جان
ساعت ۴:۴۴ صبح اسلامشهر مرجان آباد
۲ انفجار شدید پشت سر هم
جنت آباد جنوبی صدای انفجار - ساعت ۴:۴۴ صبح - ادامه دار نبود در حد دو سه تا بود
۴:۴۵ مجدد زدن
ساعت ۴:۴۴ دوشنبه صدای ٢ انفجار با فاصله ١ دقیقه از هم غرب تهران
الان صدای دو تا انفجار شدید اومد . اصفهان
سلام از انديشه
وحيدجان فكر كنم ٢تا صداي انفجار بمبي اومد اينجا
صدای انفجار از دور
غرب تهران ۴:۴۳ حدودا
ساعت ۴:۴۲ دو تا صدای انفجار توی قائمیه اسلامشهر  اومد
پشت سر هم
آنقدر شدید بود شیشه ها به شدت لرزید
ساعت ۴:۴۲ صدای انفجار خیلی خفیف شمال اصفهان
انگار خیلی دور بود از ما
فکر کنم ۳ تا بود
اسلامشهر ساعت ۴.۴۴ دقیقه صدای  سه تا انفجار اومد
وحید حان مرکز تهرانیم، ساعت ۰۴:۴۴ صدای ۳ تا انفجار شنیدیم.
وحید سلام. صدا دوتا انقجار ۴/۴۱ نجف اباد
صدای انفجار فردیس
وحید نجف اباد صدای انفجار بلند  چند تا شیشه های خونمون لرزید مثل چی
بیدار شدیم ۴.۴۳
یه جارو زدن داره مثل چی ازش دود میره سمت همین نیرو انتظامیو اینا که توی جنگم زدن
الان صدای دوتا انفجار اومد
شیشه ها لرزید
مثل صدای لانچ موشک بود
شاید جای رو زدن ولی صدای جنگنده نیومد
خمینی شهر
سلام نجف آباد الان صدای ۱۰ تا انفجار اومده و جنگنده
سلام نجف اباد ساعت ۴:۴۲ دو تا انفجار خیلی بزرگ کامل مثل وقتایی که میزدند بود. صدای زیاد و بعدم موجش اومد
سلام وحید همین الان صدا انفجار اومد سمت تهرانسر در حدی که شیشه لرزید
دوباره الانم اومد ولی دور بود
4:41 صدای انفجار اومد
04:44یکی دیگه.
فکر کنم بیدگنه رو زدن
چند دقیقه پیش تو استان کردستان شهرستان قروه سه تا صدا اومد آسمون صافه ولی اطراف رو زدن احتمالا
غرب تهران صدای انفجار
مجدد
وحید داداش صدا انفجار کردستان
سلام كرج ٤:٤٣ صدا انفجار طوري از دور اومد. رعدو برق نبود
بازم الان صدا اومد
ساعت 4:42 صدای انفجار خفیف و لرزش زمین سمت صادقیه تهران
4:44 صدای دوم شدید تر بود. صادقیه
توهم زدم یا صدا اومد؟ سمت ملارد
زدن وحییید زدنننن
انلاین شو وحید بد دارن میزنن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76016" target="_blank">📅 05:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76015">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YYETQt0dDP0fALoCWTVr3sYA8Gp7F3SqWS8JJq5uwkuNe4B2BD-IxD2ouZQ9GhuMCgtIcb5kPamLCqrVCmXEjTpDVcFOYz2LRylyAnReagXdtE_S_MGsgqcB_KQhmFP4jqRcnTiThCckXx1UGg_GAilRMqMtmYeacRgMohzmQOcaZshZ8jET5ZNLK78WzZqqxL8ylDPeV4NkW5oqT6OQs-qjFNSpOQyaoKcKKfA_3TLuLDle9Jb4nP2yyvmrYjdcw8EpTmtHSzzYEaFjPACaP1btH7vnc40YPvqyV7UA2yFI4ZQsKKlXWWu4QLHaxJweCp8RfLVfKLN0jU7eIG4PKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل با انتشار بیانیه‌ای از حملات هوایی به چند نقطه ایران خبر داده و گفته است: «نیروی هوایی اسرائیل، تحت هدایت رکن اطلاعات ارتش، اندکی قبل به اهداف نظامی رژیم تروریستی ایران در غرب و مرکز ایران حمله کرد.»
پیش از این سپاه پاسداران هشدار داده بود که در صورت اقدام متقابل اسرائیل با شدت بیشتری واکنش نشان خواهد داد.
جزئیات بیشتری درباره ماهیت اهداف مورد حمله، میزان خسارات یا تلفات احتمالی منتشر نشده است.
این حملات پس از آن انجام می شود که ایران ساعاتی پیش چندین موج حمله موشکی به شمال اسرائیل انجام داد و سپاه پاسداران اعلام کرد این حملات آغاز یک هفته عملیات مستمر خواهد بود. همزمان، مقام‌های اسرائیلی هشدار داده بودند که در برابر حملات ایران واکنش نشان خواهند داد.
این تحول در حالی رخ می دهد که دونالد ترامپ، رئیس جمهور آمریکا، در ساعات گذشته از بنیامین نتانیاهو خواسته بود از اقدام تلافی‌جویانه خودداری کند تا روند مذاکرات و توافق احتمالی با ایران آسیب نبیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76015" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76014">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRP8Sv77-LYRmeDBLX2xKT4XxGB_JoArKyesRKK4KyiGZzYD6TFQbcSjJA-05xDr9kYf-A2QPk5FQfroLAdeHNncuXl3WUy3T8iXE_u7UtNy756yLcpIMjmxJLihM1tJWAFj5thSoKr-80X1rSFJZJeI0DEWJEFPb0ENP0sFiGYcx78NCH1Au-eTlKZNgJ7RbAZoV7RVl6WmhPHpVD2W9Xlw6UjoMIdpB9TNP-GeHxBK2SbwzxradO4bSYVDDmqW_8LmH7uynF4nLty3of6S_wYWboZE_4xR14CVon-SO3H0MQSaMxk0sy3QpxE0fKPkN6yA2il8cX-uRxNFJ0LAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رسانه‌های رسمی ایران از شنیدن انفجار و حمله هوایی به چند شهر ایران از جمله تهران، اصفهان، تبریز و نزدیک به کرج خبر می‌دهند.
bbc.in
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76014" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76013">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVFp78cIvq-Pdi91lu0zRm3zzclp6TZ7IKrvRi_ayf28PgIfvVlYMiV6PCNe7dLOL94GJV8Op_Y_Spj_U7jyYwKc_Qd_StibL93_4TS5OmaSruIawlw-0vOzkgPiYjyrE2uw3DnPEzwciGIfl-WmBp_Mt6aRxoTxVqRpgzXP-XtthpOYl6b4aRZuSMPT8ntf2rjrfyrzcmuLVsMKftV5sBDqD1xFETWVzJZTIbXquUo0xDphhnSudsnxZbG4cKY5TtjXebrPcG8lOvzVQPtrTS4jdWAE0iuXeNx5DrS4apTYk5KCAJIxn4tmfaAtfv1pWX9vJEN7ozZadYmt1Y1adQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از وقوع انفجار در تهران، اصفهان و تبریز در بامداد دوشنبه خبر داد. خبرگزاری تسنیم از وقوع انفجار در کرج در بامداد دوشنبه خبر داد. ارتش اسرائیل نیز اعلام کرد نیروی هوایی این کشور «مدتی پیش» اهداف نظامی متعلق به «حکومت ایران» را در غرب و مرکز ایران هدف قرار داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/76013" target="_blank">📅 05:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76012">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AAUvJltQym-WEVY3mcJEmVXgKOD9kSKK99cGVmykCPpJ3UOzAaAR_xmFHBB6dY_NaaDlH43ZDjPWZovuBLNR6jbf0_09b6Sj3gV2cJ3MvnwVrsdFKCScyH_xwYCjgYH6a5lDC1_8mKHSy3hludhlQULwU0YD7E6ne6TcN3x-I4lBUATUQoHaq-mFY93HLCC6bTBLHgyCARGtCTw8dbimOkuzDJqWQj2oNLKY2tqPaXR4Hx9GL_d4jb_HomcE01GDApz_g2nm7K2APUpa6tAwuCvJeisKHk5KPb-th1S9ueKBuBUK1CbhDNjP5oDAuNjwGuBfTLTzHezxQPB8Pz36Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش اکسیوس، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با درخواست دونالد ترامپ، رئیس‌جمهوری آمریکا، برای به تعویق انداختن پاسخ به حملات موشکی بالستیک ایران موافقت کرده  تا به واشنگتن چند روز دیگر فرصت داده شود تلاش‌های دیپلماتیک برای دستیابی به توافق با تهران ادامه یابد.
بر اساس این گزارش به نقل از یک مقام ارشد آمریکایی و یک مقام ارشد اسرائیلی، ترامپ در تماس تلفنی یکشنبه شب از نتانیاهو خواسته از انجام حمله تلافی‌جویانه خودداری کند، زیرا به گفته مقام آمریکایی، او معتقد بوده «ما به انجام یک توافق خوب نزدیک هستیم».
طبق این گزارش، نتانیاهو تلاش کرده با این درخواست مخالفت کند و ترامپ را متقاعد کند که اجازه حمله به ایران را بدهد، اما در نهایت «تا حدی به‌طور غیررسمی» با درخواست رئیس‌جمهور موافقت کرده است.
این مقام آمریکایی گفته است که این گفت‌وگو بسیار آرام‌تر از تماس پرتنش هفته گذشته درباره طرح‌های اسرائیل برای حمله به بیروت بوده است؛ زمانی که ترامپ به‌طور علنی اعتراف کرده بود بر سر نتانیاهو فریاد زده و الفاظ تندی به کار برده بود.
پس از این تماس، این مقام گفته است: «فکر می‌کنیم رئیس‌جمهور کمی زمان خریده است. او بسیار قاطع است که ما به توافق با ایران نزدیک شده‌ایم. فکر نمی‌کنم در حال حاضر حمله اسرائیل قریب‌الوقوع باشد.»
او همچنین گفته است: «ما در یک لحظه حساس هستیم — چرا باید وقتی در راند چهارم هستید، یک توافق احتمالی را به خطر بیندازید؟ رئیس‌جمهور فکر می‌کند سه ماه است درگیر این موضوع هستیم و اکنون زمان پایان دادن به آن است.»
با این حال، هنوز تصمیم رسمی در اسرائیل گرفته نشده و طبق گزارش شبکه ۱۲، نتانیاهو تا نیم ساعت پیش همچنان در حال برگزاری نشست با مقامات ارشد امنیتی درباره این موضوع بوده است.
@
‌VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/76012" target="_blank">📅 02:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76011">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uc_0aAMwKIopFKTIvmrkYsxaInEQYNw5eqAEUyxduWEmDmxNbzFqJIBuupAw1OY_rfw9xlfzXR0v6Y87OZ2mia8ZBLFmarvX84gNNTfd-HGSc6GM0Kzu0AecJs2fmIF50PlwU-vRHnwDS0zpsxBs4-gwrji7vxnYd7Clyjfh0SI0RaY-7EPNBK-1lWbGPl_fg4qajrXy5dx1xH8_oaYIVCjuLK8ZJSZPFUBhMkbbtMwyKVY13ve9ERTcv-Zs3qSrDSK6PGucv3orQ_m_umsLfLv67hlmPu76EUE9AiI7JAlA2UZ68iESCVZacl6BgZC5jBrB-DzTsl05z_ohvjaJ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید هر توافقی که او با حکومت ایران کند نخست وزیر اسرائيل خواهد پذیرفت
رئیس‌جمهوری آمریکا در گفت‌وگویی تلفنی با فایننشال تایمز گفت که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، چاره‌ای جز پذیرش هر توافقی که آمریکا در مورد آن با رژیم ایران مذاکره و نهایی کند نخواهد داشت.
دونالد ترامپ گفت زیرا «تصمیم‌گیرنده اصلی رئیس‌جمهوری ایالات متحده» است.
دونالد ترامپ به فایننشال تایمز گفت: «او (بنیامین نتانیاهو) هیچ انتخابی نخواهد داشت. این من هستم که تصمیم می‌گیرم. همه تصمیم‌ها را من می‌گیرم. او (نتانیاهو) تصمیم‌گیرنده نیست.»
به گزارش فایننشال تایمز، آقای ترامپ این اظهارات را اندکی پس از آن مطرح کرد که جمهوری اسلامی در جدی‌ترین نقض آتش‌بس از زمان توافق آتش‌بس در اوایل آوریل، چندین موشک بالستیک به سوی اسرائیل شلیک کرد.
آقای ترامپ تأکید کرد که حملات موشکی جمهوری اسلامی تغییری در تمایل او برای به نتیجه رساندن مذاکرات میان آمریکا و حکومت ایارن ایجاد نکرده است.
او به فایننشال تایمز گفت: «این موضوع هیچ تأثیری بر توافق نخواهد داشت.»
ارتش اسرائيل به صدای آمریکا گفت که جمهوری اسلامی یازده موشک به اسرائيل شلیک کرد. ارتش اسرائيل پیشتر گفت که حملات موشکی جمهوری اسلامی را دفع کرده است.
در همین حال در واکنش به حملات موشکی جمهوری اسلامی، ارتش اسرائیل در بیانیه‌ای به صدای آمریکا گفت که رئیس ستاد کل ارتش اسرائیل، ایال زمیر، در حال ارزیابی وضعیت در مجمع ستاد کل است. ارتش اسرائيل به صدای آمریکا گفت: «نیروی دفاعی اسرائیل به محض صدور دستور، با قاطعیت به دشمن حمله خواهد کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/76011" target="_blank">📅 02:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76010">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرگزاری تسنیم: "صدایی که دقایقی پیش در تهران شنیده شد مربوط به رعد و برق است و این صدا ارتباطی با پدافند یا موضوع نظامی نداشته است."
من هم پیام‌هایی گرفته بودم که بعدش با «ببخشید انگار رعد و برق بود» آپدیت شدند
.
زیاد پیش میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/76010" target="_blank">📅 01:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76009">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NeEOa4mBluq8Mwty44sQMOOEfYQQf7EOrao3R2rx5gSxcsCTIk-6VaSqtT_hdF2FaPVJK9e9VEtqFOZc_PQ_La2_FNq5nEXwrjiW8UUTjn3EXAgpInvIJkUvo9gjM9eEowV8oABuQet-XTW_GwwCn0OW7Q81583PO4WYQsxB40HiLRTsqEDOOZbK2pHE9hi7dPve_RkUv07DtkvMuOmXB7GVkeRsIp5Ur5q4o7p0p20sAJ4lJz5SGF0n_fLeL-IPQT7yGCNaUGcH5kyb3qFeF9FMzcnf1-YSgOF88_7Jyj__yQdOLnJhlkIJxoepR1V_4fC8oretlbbYaLh_GzPWaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">shamidartii
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76009" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76008">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qli-5Edgp6gF9KC7yQnHskLqGtEtDYEIavdgZqfpUaAjH3SXHbnc1gQYE5Jk_LtX7Hym3QdM7U5FaLXfFCfgDZp2ANnnwn8jmVAphbWmrXhqf0p6dCDj0RAefyQFVGusoYqCxQEhNvavUcv6B2UfxjqaL_6sxOgucDaiqoOq8XFzoLtV-rEPbqN9BCrzWByIfzT3UhUk5L27WMRuJYZtA18AJIiIUYCyhrSmC-J22VgFnKRdhZFJauhDDSGmUQbbIKzKlibJrPAwXcVcWDQ3JODds5lfn082xV4tdVChSUGI3KxRIRwgko4HB5q_YrpiM7ReJEstnHqZTSOqTm_WAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با به اوج رسیدن نگرانی از آغاز درگیری مجدد نظامی میان ایران و اسرائیل، سازمان هواپیمایی ایران اعلام کرد تمامی پروازهای شهر فرودگاهی امام خمینی از بامداد دوشنبه ۱۸ خرداد تا اطلاع ثانوی متوقف خواهد شد.
در اطلاعیه این سازمان آمده است: «مسافران از مراجعه به فرودگاه خودداری کرده و اخبار بعدی را از مراجع رسمی پیگیری کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/76008" target="_blank">📅 00:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76007">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O8KpB0f3SLXMSfRWfJB3OeedabKe9jblocMqDbIsjA7HQubkBJNLEgHsw15BskAyj7LZ0ZOQkXoQw7l2yzhZdGVg0NEOALmcF7XoH3iYKNwgUi5rsTsRtTGergQ5wEhkkmaGpCyHj-pYCGRSZefYBvFqReo_bmIH_s8dg121bCQMTH0wY_BVMittfzTo6mj80FX6L5OznxjbfmUIEsahOv0KeUlbNPpFM_Mtgpk9XxzbYGNVDqMYh10H8mAdPC61VupiO_SYCPdf3QzC8P1BuBQ-o0JnW3leRUBIXF7HQdtAwgQk2Zwn20sbgcsR3qF4U2RgnJfENRA0X1kZiGbIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایتامار بن گویر، وزیر امنیت ملی راست‌گرای تندرو اسرائیل، پس از حملات جدید موشکی ایران به شمال اسرائیل، خواستار واکنشی شدید شده است.
او عصر یکشنبه در پیامی کوتاه به زبان عبری در شبکه اجتماعی ایکس نوشت: «امشب تهران باید بسوزد!»
اظهارات ایتامار بن گویر در حالی مطرح شده که ایران ساعاتی پس از حمله اسرائیل به حومه جنوبی بیروت، موجی از موشک‌ها را به سوی اسرائیل شلیک کرد. ارتش اسرائیل اعلام کرده است که این موشک‌ها رهگیری شده‌اند و گزارشی از تلفات فوری منتشر نشده است.
ایتامار بن گویر از چهره‌های تندرو کابینه بنیامین نتانیاهو به شمار می‌رود و در روزهای اخیر نیز از توافق آتش‌بس میان اسرائیل و لبنان انتقاد کرده بود.
@
VahidHeadline
نفتالی بنت، نخست‌وزیر پیشین اسرائیل، در واکنش به حملات موشکی جمهوری اسلامی به اسرائیل، در شبکه ایکس نوشت: «خویشتنداری یا واکنشی نمادین، این پیام را به دشمنان ما منتقل خواهد کرد که ریختن خون شهروندانمان بی‌هزینه است؛ از این‌رو اسرائیل باید با قدرت و به‌طور موثر عمل کند.»
بنت نوشت: «این یک لحظه آزمون است: «آیا اسرائیل کشوری دارای حاکمیت است که توانایی دفاع از خود را دارد؟»
نخست‌وزیر پیشین اسرائیل نوشت: «در این موضوع، همه ما، تمامی شهروندان اسرائیل، در کنار یکدیگر ایستاده‌ایم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/76007" target="_blank">📅 00:46 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76006">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F1krysEEgKZjyhm6HP3i2R3sOXhYadu_CEWgcq7Im-M3MHwkgwj4wYZoCgxMfJVm1Gy_FG7oEBKuOz0iiEp_vWwiVmylf44FgLdQPuF7qTJ_-Q8xzN_4Q-q3gzHAnvWyA_FIql8FZGHJTE9VqRsbRNU5FAz5IBUMTcFYCRSN5toxLY9Endg6Lu8tTuVZaXNpAP70xMp_cjiB6A_e5C6c-Di1aDJMFdS9is1SGcgavRTZL6un5txrAyc_PNqUnjqkX0evsBbCPqjElhRiS0JSCEN4nH1amyIqCVKSEGBztQHL7i-2rBIA1nhRI8taQrcmpD49WElZC8rekZpw7BNL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با حملات موشکی ایران به اسرائیل، تسنیم، خبرگزاری وابسته به سپاه، یکشنبه‌شب، در پی شنیده شدن صدای انفجار در تبریز، گزارش داد: «براساس پیگیری‌ها، صدای شنیده شده در‌ فرودگاه تبریز تست پدافند بوده و هیچ‌گونه حمله‌ای به این فرودگاه اتفاق نیفتاده است».
@
VahidOOnLine
پیام‌هایی که من دریافت کرده بودم:
سلام وحید جان
الان ۲۳:۵۵ سه صدای انفجار بزرگ آمد تو تبریز
پیام بعدی در ۱۹ دقیقه بامداد: همین الان باز زدن تبریز رو
سلام وحید جان
تبریز ساعت ۱۲:۱۵ نزدیک لشکر عاشورا صدای انفحار اومد.
البته شدتش مثل انفجار های جنگ ۴۰ روزه نبود.
تبریز نیم ساعته صداهای عجیبی میاد
مطمعنا صدای پدافند نیست انفجاره
هم اکنون صدای چند انفجار شدید در تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 421K · <a href="https://t.me/VahidOnline/76006" target="_blank">📅 00:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76005">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eHLUmY69VAHUcKzpGa-a79-wmrkbisFdtkaj1_z-Z0JTWIJPNQhVbmKNqxznneHT2i1oLDM-QZJA3yOlXDq6_RoJy6dcsTF8YPxY2JCqUjAPeaZwlmMnxE9dl7ijufea9gwwzj6FCzx-sx8CIANtKtbNC6BBXUJHwHXEmgMurFtQ7x78hFuZGooH0lQd8-Q7WDlbmGqfFBbw7XdVKAMBOJ-qPQ32ny9apkMAMo5_UboCHzdVhthNPJhG1n33vJUGSD4MLK-aZ9qdKJnf7toIeBB8yf3M8e7hbExbgDjTbM5rhKBcCWSzx29h4GCAHwyG7_wpomDhegML1itngn0PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارتش اسرائیل، افی دفرین، می‌گوید پس از حمله موشکی بالستیک جمهوری اسلامی ایران به اسرائیل، ایال زمیر، رئیس ستاد ارتش اسرائیل، در حال انجام ارزیابی و تصویب برنامه‌های آینده است.
سخنگوی ارتش اسرائیل گفت: «رژیم تروریستی ایران اشتباه بزرگی مرتکب شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/76005" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76003">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dzZuEOmpHDqmrf5x4dSlzopHK5tb0Dd1q2rGHYxV-cwRpiVvoScKfvVYP11l6Fl7TvuSHrcstI7kGtFYbQfWM1O1JmgiNWSgMdN6Dj9bSB8jL-aM8SbKS4YXRf-UY06Ml5tWgo-MoRm8IKuAPILaCaoourRCdr6LWfvZVy5H4HKV_V_YQaFVU3E9q5wAoIUVeBFOzOumZSdU40ogHltXyuozEDGi4hutcO9-tDVWxIJZPOMglEXhDC68CjklEUbHnR8EjctOy9ezA31m2vUMsRsgnuYH-hd5KSPcedJdxqwYxqIwiI0jUoxsN9UCAV6V-nYtIFo4Alt2p3bBiZyHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uwOP7enTomUFQj0uAe9xdCQY7BLXQiY9W5_1Sl3syCnEQ4ErEGROd-E5w1a21fmpyKJtUbGo2PPyYXrQAYRmPM6Tk8OOFXS4I8TGR5Lqq0hpD3V4a4q2Ldj2sJJmcnAaZtN_e0tYvxlXg1EE9sN1WM-5KGppSurejEMzaNRvLF4QbuG1Gl-BPcZk955UaFJoFGed4CIeXLGA3ApNoTzWy9eU7c5tUKJ-qG_jE5T8QtYUkSfeCrmH9V9t6Dy6cu_E25f2hjpxge_cetTGdiHz8hAIzNLqnGnoe7wxiY_6yuBePkXaVX-kpEwXqpoHl875fBbyyKxuuVa7rEkM0I8m7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
ما تهرانسریم
تو این 1ساعت اخیر که اینا اسرائیل رو زدن
نزدیک به 8تا هواپیما مسافربری از مهرآباد بلند شد
نهمی هم الان رفت
انگار دارن فرودگاه رو خالی میکنن
سلام از تهران داره همینجور هواپیما بلند میشه همشونم تو ارتفاع کم پرواز میکنن
همین الان از بالا سر مهرآباد یه هواپیما با چراغ روشن از غرب به شرق رفت
مسیر خیلی غیرعادی با ارتفاع خیلی کم ۰۰:۰۸
آپدیت:
بعدش کلی پیام مشابه دیگر دریافت کردم.
آپدیت:
وحید جان همچنان پروازها از فرودگاه مهراباد به سمت شرق ابران ادامه داره احتمالا هر ۴/۵دقیقه یک پرواز بوده لاینقطع
شاید ۳۰/۴۰هواپیمای مسافربری پریدن تو این دو ساعت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 430K · <a href="https://t.me/VahidOnline/76003" target="_blank">📅 00:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76002">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CXutfmz3x9QZM4YwkaDNzlzCklgZdoJTokIF9CKKHN5ZthJn3dONd6EGl1zxGD61UPTCW1nqNLl7X9w-XwhgttfQpaOJRPgpmzSVxOcxw7ClOJqxs4B3uIU0Fh6UeBFp1_6K6ldRfV1FFIeVNGCEaZILZlwhYrlLDjc8mhGNEn7j81NioWUCBn-6cdikHHNmRFcVOGc7Yvn4WTe3ObAGwVb9tGG3E_h20i7XgaXWVBf08Yjr93NRBNtdMA_T5KggaYx5Dbgja9YFt2ibJ0Cruxkz9chiQIc9y1p_YkCSk_aQrhD67_rZivXGmRX3YkGqH4bWRvz8poXVIy9B5cqLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: حملات ایران به کسی آسیبی نرساند، امیدوارم اسرائیل تلافی نکند
درپی اعلام خبر حمله موشکی ایران به اسرائیل در شامگاه یک‌شنبه، دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگویی تلفنی با خبرنگار اکسیوس گفت: «همین حالا با بی‌بی (بنیامین نتانیاهو) تماس می‌گیرم و به او می‌گویم تلافی نکند. هر دو طرف کار خودشان را کرده‌اند. اسرائیل حمله خود را انجام داد و ایران هم حمله خود را انجام داد. دیگر نیازی به حمله دیگری نیست.»
دونالد ترامپ در این گفت‌وگو افزود: «حملات ایران به کسی آسیبی نرساند. امیدوارم اسرائیل تلافی نکند. اگر بی‌بی (بنیامین نتانیاهو) پاسخ بدهد، این ماجرا همان‌طور که در ۴۷ سال گذشته، یا حتی در ۳۰۰۰ سال گذشته، ادامه داشته، باز هم ادامه پیدا خواهد کرد.»
ترامپ افزود: «ما به یک توافق نهایی با ایران بسیار نزدیک هستیم. این توافق، توافق خوبی خواهد بود. نمی‌خواهم به خاطر اتفاقاتی که اکنون در حال رخ دادن است، این روند از بین برود.»
این اتفاق چند ساعت بعد از آن رخ داد که ارتش اسرائیل منطقه ضاحیه در جنوب بیروت را هدف قرار داد و ایران تهدید کرد به این حمله پاسخ خواهد داد.
یک منبع ارشد ایرانی هم به خبرگزاری رویترز گفته است که «ایران به هر حمله اسرائیل با نیرویی شدیدتر پاسخ خواهد داد.»
ارتش اسرائیل اعلام کرده است همه موشک‌هایی را که تاکنون از سوی ایران شلیک شده‌اند رهگیری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 455K · <a href="https://t.me/VahidOnline/76002" target="_blank">📅 23:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76001">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/td7xKnpCyt4-PmitzbCDlJhzqcnHOQebaIEVzBJ_3gSsp8kTagMC-Y_gVoHVpAhzazpRbjVXJsAwklLPKM17uwfHaT7-ntJP8Ipjb28El8yABTRrt7V6qGRi8uaMKHh539Ml8bcqNzC2R-fOHqT89CoMvQBAYbR-045JjhrRE6cmlfwnZtjnH4_sGEEtjeJATaqNXbi8LEC2D5JWSA4bk8MFPfHkYJ_FaG0xVFlaMYBP7bq0o2vRCukMUymqA_f4pjmi-k-L4AHK9zsfN4_6YBW1I8P9QeLdffcETw5D-hr_AlJJTsLn5delhclN4-LWRlXzjRkM2U5wn5Y8e7KlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">mohsenreyhani01
سپاه پاسداران پس از حملات موشکی به اسرائیل در بیانیه‌ای اعلام کرد عملیات شامگاه یک‌شنبه صرفا یک اعلام اخطار بود و در صورت تکرار حملات، پاسخ‌ها گسترده‌تر خواهد بود و تمام اهداف آمریکایی-اسرائیلی را در منطقه در بر خواهد گرفت.
در این بیانیه آمده است: پذیرش آتش‌بس از سوی ما در ۱۹ فروردین ماه مشروط به توقف آتش در تمام جبهه‌ها بود اما مثل همیشه آمریکا و اسرائیل به تعهد خود پایبند نبودند، هم حملات را در لبنان ادامه دادند و هم با تعرض مکرر به سواحل و شناورهای ایرانی در تنگه هرمز، دریای عمان و اقیانوس هند آتش‌بس را نقض کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 468K · <a href="https://t.me/VahidOnline/76001" target="_blank">📅 23:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76000">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sC3ubgn3VPlV3ZJMx7uZ1Nw0dnzg29m37qj6kHQ4dz1Ut-qlNqIgiwX9xq5LOvRsatRzXYgdO5tb3RAU6-rljTfXHxlQ8ccy9kMtwUgwlyOc5j51b9HKc9SmqPjmQ4uOYnNKHujPBfhgBKLo7XJaXzBWnEyaMaMxrzZW3Xy7_9Tgi_Z8pE_SYdmARBRk1cX5j0-ikdsyHprErKDaTfv3dzkz-Z5y0d1K4dQBCdKwtNczl7Dp8JBYuh7wPl_SdVApxnhAPNGvNIMoEX3JEJF4xAslO5ZaV-_K5c4Lr6qqnp1VoyCqxjviXWAMbEDDdyWaj7Li5sgTd0VEG-2Y4GMjWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز گفت: پیشنهادی که به ایران دارم این است: موشک‌های خود را شلیک کرده‌اید، همین کافی است.
او افزود: به میز مذاکره بازگردید و توافق کنید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 481K · <a href="https://t.me/VahidOnline/76000" target="_blank">📅 23:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75999">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MuS_s5MshzoeMEJr2SY3tnvnWfylWVHXPFP6vezf81_sfgJsvSjDAd2nEwQitfe35LwxEEITp8nWrtGFWFfrkdjnQ3lDPiaAwweEzQOK_JUOz45MIqIG0A_NIgATs5Hbi6vNUcDyZl1NSMQb5FcRakDx0jUHIBDd1k88Ma1DBZbaNqwn59jM5NsCnNM_Jka1_FbZVPyZeYXsBJ5FDv521-Hiigj8xpce4uou-dVY6Yqqarw2aI9YrP_b7bRZZUs-xtHSJW7fM_UoIPN-KDKiZRK2t3Skn7VCFpZAnJajVDJFnNl4NXCyUS01WL60jevqd827OSppYuwLojhOWOlMeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی اسرائیل در بیانیه‌ای دقایقی قبل اعلام کرد که این نیرو تاکنون تمامی موشک‌های شلیک‌شده از سوی جمهوری اسلامی ایران را رهگیری و منهدم کرده است. این نیرو گفت ارتش اسرائیل اکنون پرتاب‌های بیشتری را که به سمت اسرائیل شلیک شده‌اند شناسایی کرده است.
@
VahidHeadline
ارتش اسرائیل به صدای آمریکا گفت که جمهوری اسلامی تاکنون یازده موشک به سمت اسرائیل شلیک کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/75999" target="_blank">📅 23:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75998">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">توییت باراک راوید، خبرنگار آکسیوس:
یک مقام اسرائیلی به من گفت که اسرائیل قصد دارد به حمله ایران تلافی کند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 466K · <a href="https://t.me/VahidOnline/75998" target="_blank">📅 22:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75997">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EHFsQYuw18RT3fUpnWnQeKpLd6d2r6gR5F0jzsiUtl2ZZ4DUx4KkmCl75VN8CFGJguuOJT5W1hyY7pFJoJmwBh5c6VwkAUcb1mdIa6SxL-SbSdG5Pv1RdWle1I0hAQU3ZO_BU45RduG336pGEGgH_lsFlkLGIbEsMGuFwH0OPApFjPf9OjRXnk8dpwJemPZ3_5Wj5RMR-bmuCs4zeDSQGPnZyWblgfbjcsXF3C6nC__ZJHs7kMjajw6u4xChy_Vc1jH3v20tYHZMONxe-Cbsly7pSa0XpIxeL96Gvx2kpWfAiJtKa_mLRDA8joKsIK8_-16i0Wmxc8y1jYMny57mng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: در صورت گسترش حملات پاسخ ما کوبنده‌تر خواهد بود
به نقل از تسنیم، خبرگزاری وابسته به سپاه:
"فرمانده قرارگاه حضرت خاتم‌الانبیا(ص):
رژیم متجاوز صهیونیستی با نقض مکرر آتش‌بس شرارت های خود علیه مردم مظلوم لبنان با چراغ سبز و حمایت آمریکای جنایتکار و سکوت مجامع بین المللی را روز به روز افزایش داده و با استفاده از سلاح های ممنوعه از جمله بمب های فسفری مرتکب جنایات جنگی می گردد.
با وجود هشدارهای قبلی جمهوری اسلامی ایران، رژیم کودک کش صهیونیستی با عبور از همه خطوط قرمز و افزایش حملات در جنوب لبنان، ضاحیه بیروت را هدف قرار داده است.
قبلا اخطار داده بودیم در صورت گسترش جنایت در ضاحیه بیروت، اهدافی را در سرزمین های اشغالی مورد هجوم قرار می دهیم.
ارتش صهیونیستی باید حملات خود به جنوب لبنان و ضاحیه را متوقف نماید و در صورت گسترش حملات خود به آن منطقه و یا پاسخ به اقدام ایران با ضربات کوبنده تر و پشیمان کننده روبرو و حملات ویرانگری علیه رژیم و حامیان آن آغاز خواهد شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 480K · <a href="https://t.me/VahidOnline/75997" target="_blank">📅 22:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75996">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">☄️
موج بعدی شلیک موشک به سمت اسرائیل
پیام‌های دریافتی:
دوباره شلیک از کرمانشاه
دوباره یکی دیگه زدن الان
یکی بود
10:44 دوباره صدای انفجار اومد کرمانشاه
صدای انفجار مجدد
بازم زدن
همین الان صدا اومد از روانسر کرمانشاه
22:47 شلیک موشک از تبریز
آذرشهر [نزدیک تبریز] صدای موشک ۳ تا
سلام وحید
ساعت ۲۲:۴۰ ۴ تا شلیک از تبریز به فاصله هر یک دقیقه
نور خیلییی زیادی داره و صدای زیاد
🔄
آپدیت:
منابع حکومتی نوشتند از اصفهان و ارومیه هم موشک شلیک شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 470K · <a href="https://t.me/VahidOnline/75996" target="_blank">📅 22:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75995">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">☄️
'شلیک موشک از کرمانشاه'
‌
بعضی از پیام‌های دریافتی:
سلام همین الان صدای موشک از کرمانشاه اومد
سلام صدای جنگنده در کرمانشاه
سلام وحید جان.
همین الان ساعت ده و نیم دو تا موشک از کرمانشاه شلیک شد
صدای غرش  شدید ترسناک ساعت 10.31 شب کرمانشاه میاد
وحید همین الان از کرمانشاه موشک پرتاب شد
از کرمامشاه الان دوتا موشک شلیک کردن
صدای پرتاب موشک از کرمانشاه الان
سلام وحید جان
من کرمانشاهم
الان ۱۰:۳۰ یه صدایی شبیه شلیک موشک اومد
مطمئن نیستم، ولی دقیقا شبیه صدایی بود که زمان جنگ میومد.
🔄
توییت ارتش اسرائیل:
ارتش اسرائیل موشک‌هایی را که از ایران به سمت اسرائیل شلیک شده بود، شناسایی کرد. سیستم‌های دفاعی برای رهگیری این تهدید در حال فعالیت هستند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 493K · <a href="https://t.me/VahidOnline/75995" target="_blank">📅 22:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75994">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پیام‌های دریافتی از شنیده شدن صدای جنگنده در تهران که لابد داخلی است:
سلام وحید جان ۲۱:۳۲ شمال غرب تهران صدای شدید جنگنده
درود وحید جان
صدای جنگنده (؟) غرب تهران
۲۱:۳۲
صدای جنگنده غرب تهران ساعت ۹:۳۲
بازهم مرکز تهران صدای جنگنده یا هواپیما رو نمیدونم ولی خیلی پایینه ساعت ۲۱:۳۳
شهرک غرب
صدا جنگنده
صدای جنگنده ساعت ۲۱:۳۵ دقیقه، شمالغرب تهران
مرکز تهران صدای جنگنده میاد شدییید
صدای نامتعارف جنگنده در مرکز تهران از ساعت ۲۱:۳۳
غرب تهران صدا جنگنده داریم 9.32
۹:۳۱ شهرآرا صدای جنگنده میاد وحشتناک خیلی پایینه
سلام الان نیروهوایی صدای خیلی عجیب میاد صدای جنگنده ست انگار خیلی بلنده
سلام وحید . ساعت ۹ و ۳۳ دقیقه شب مرکز تهران صدای جنگنده میومد واضح . ۱۷ خرداد .
سلام ساعت ۲۱ و ۳۳ دقیقه شنیده شدن صدای جنگنده زیاد ، امیرآباد تهران
صدای جنگنده میاد سمت مرکز شهر
آپدیت: کلی پیام مشابه میاد که دیگه نقل نمی‌کنم. درباره صدای هواپیما اهمیتی نداره که در کدوم محله شنیده شده.
بین پیام‌های اولیه دو تا پیام هم بودند که نادرست به نظر می‌رسند:
سلام وحید، اینجا شهریار صدای موشک میاد. احتمالا از بیدگنه جمهوری اسلامی داره موشک میزنه
وحید از بیدگنه موشک زدن ۲۱:۲۸
صداش تا فردیس اومد قشنگ
آپدیت:
در پیام‌های بعدی روی این تاکید می‌کنند که صدا طولانی بود و چند دقیقه طول کشید.
بعضی‌ها هم نوشتند این بار هم هواپیمای مسافربری بوده با رفتاری عجیب و پرواز با ارتفاع کم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/75994" target="_blank">📅 21:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75993">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MZsYP-yt-QnorfdqNR1FhKKdvt4OdoLgMLU3nehG_hkAFsF4mdqzDdyWERYFZYDMba8-_hI68lq4dlSfcFLesEqLgJK8lgietaXrM96qrteNlTOdNdVaaVsRP4MMM8m0NuPa5DIjlUImqo0cgONbDjkCPD6hvl5VYg8gnAmb_242rmWoA7Ts5Ew1Uc1gWOfIRXU4ZVUllePGnOWzb6We6CgMzn_XAkAJvMTeSEoPv3Glx8wmal55q1Ae2xG-kbNYiRArWGbs0Lc_ymlBYOK0VyA5zCzihCESgSkHMHPMlkFbo-fUXr3nDZkyomvtom6yHzuHGPKq_99Jb_JUE0NM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان علیه صدا و سیما
رئیس دولت در جمهوری اسلامی، تلویزیون حکومتی را در شبکه فیلترشده ایکس تهدید کرد:
drpezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/75993" target="_blank">📅 20:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75991">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K7gxwoyg_QwjzoeY6OYEyaCZ_VaN3reE1PojkcCX7JSSvk0fB_OcOWRMxtzWrbXrJcjDA4eoWl8z95OeHiO_YMOUAbG3nT6A1nCUTgdxNxHN09IyzDeR2UE7dkNO6NCpamIv-9E31CGVU2a47BRijPUP5sUpUiY3bAgYU0YXMtxeJDqGaDbE-w_gt9sGwzr3NuW6g4Pn3u_Bl0qcWaUqvK-4jkOKrKIhejI6kqDVW17jpqlxLDc4KwOVPizIvVSqm0IBNBI4Grv3nOKBblMaGFbj-DcYuAeqBuw5MR6PSBaCemSTA-M8nylZHEGhaEstuhkre09bY7rxImt8n3TN4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FrphRqxJN5av7l9gKw-3TwoHj7Zmz9WBF5nlrQfpsnqAwXvYh1hGBbrTzkYwl2sj0ikMhoqke8rvar0ujb7CEL9jg7LnpXLaPatnIEHv0HJupZR5pmEnwwEcqfKlE3pVIDwolBTLEtNU1AGlQBo4LddoAdtyZeBYoqHCoEpWF2rfc4f33nkRiMOBBoZGvtzahedmhUQkBhUf4g72XrXPCXlS4z_Xt39ZVnpfzmr288a11yGxDc8TRn2R5ghYMK6ITgN2gU2146wuscrj0SjVCZrF1SpPUldeVFCv-Nt0uWqzexz2cD7SBCAslcnN50_Cif56xWw4NUXRJp5kk6oTUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قالیباف در واکنش به حمله اسرائیل به بیروت تهدید کرد پایگاه‌های آمریکا هدف قرار می‌گیرند
:
mb_ghalibaf
رئیس مجلس شورای اسلامی که مذاکره‌کننده ارشد جمهوری اسلامی در گفت‌وگوها با ایالات متحده است، در شبکه ایکس نوشت که محاصره دریایی علیه ایران و «چراغ سبز امروز آمریکا» به اسرائیل برای حمله به ضاحیه «پایگاه‌ها و دارایی‌های آمریکا و رژیم در منطقه را به اهداف مشروع تبدیل می‌کند».
اسرائیل ساعاتی پیش اعلام کرد در واکنش به حملات حزب‌الله به خاک خود، مواضع حزب‌الله در حومه جنوبی بیروت را هدف قرار داده است. از سوی دیگر دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد که قصد دارد نیروهای آمریکایی را تا زمان «تکمیل» روند توافق با ایران در منطقه نگه دارد.
قالیباف در بیانیه خود ایالات متحده و ‏اسرائیل را متهم کرد که «نه به آتش‌بس پایبندند نه به گفتگو باور دارند» و افزود که این کشورها «با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/75991" target="_blank">📅 20:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75990">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MhTMGdPFT0G-i-3S309B8jbrXSKqqWv5Y9VVXUjBEQdQ4FCoMRhN8ENiWIUBdoEN_STtbjUIMQ_vCwqIUpdl4o611VijkQGHa9QU_oPQ9uOXAJeiJBATizK9MnJqlH6hFeWSfqAJruHOVcW1-nY8bDpcglPto518HkzNWXdOMtkk-pLntup-0uF-IpfWNRv8oSbA3MAm_a9dc0uhgxLkWZYQrDJGAIj2SVCGgWUsO5iEB4wWZC6Z2BH3X8xgCOVyjLxQorSHv7eN0CqpZQWQLZD8OJXIj3n2iJRTn-WrNnund0hCto460ss-lTG3BOBzi-gcf_N3n_HuIv9JrH6jcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابراهیم رضایی: امشب به اسرائیل پاسخ دردآور خواهیم داد
توییت سخنگوی کمیسیون امنیت ملی مجلس شورای اسلامی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 423K · <a href="https://t.me/VahidOnline/75990" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75989">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AejbjIxiJJnSiRoka7aB04dJNYUPhTiotvVkHiDbK3jB4geig9fDm8S0tTBlAyzJjUKTtYAXXPPLw3cFjWQEOGco2kZIo2_giqO9ohVF6YR2pNDgaXHHuZ9QfGdOr5KmEYw4Je3asqXs4N-9JjJ7fOVsAZIpo6oMDG1L-3IjM-fVEoDpnfJjpXm8OnGsfMECx1GIFlbnKrAhh-dlAVHb_3EHObs7xXziEQw1r2cWAKsPxeoYhDsyuwS3OpWQuTPlCMsF6ELe_JQmmX9GvErChQZGn0wOumz5NAjM9gIYxMh6uASOqu1izUxdUZn6B7XQ0d4DLmH8fm43y5wcjFafaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«وحید هاشمی» ۲۶ ساله و تبعه افغانستان، شامگاه ۱۸ دی‌ماه ۱۴۰۴ در خیابان ۲۰۲ فلکه تهرانپارس هدف شلیک گلوله جنگی قرار گرفت و ساعاتی بعد بر اثر شدت جراحات جان خود را از دست داد.
به گفته نزدیکان، گلوله جنگی به ران پای چپ او اصابت کرده بود. وحید هاشمی حدود دو ساعت پس از تیراندازی به بیمارستان تهرانپارس منتقل شد، اما به دلیل خونریزی شدید جان باخت.
خانواده وحید هاشمی پس از ناپدید شدن او به جست‌وجوی او پرداختند و سرانجام پس از شش روز موفق شدند پیکر او را پیدا کنند.
پیکر وحید هاشمی در تاریخ ۲۴ دی‌ماه در قطعه ۹۶ بهشت زهرا به خاک سپرده شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 388K · <a href="https://t.me/VahidOnline/75989" target="_blank">📅 18:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75984">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mUelOopF888lbw4-hh-q-QsU00v9sXfgxRRVu2JJkuZx9RNW6ib46Dkwi7ky-0w0gKNGgRxKgZlUccdci5kfdRLe8Ye7lmbTqPkZQrS5ORSZtum8u8F7VMcvEWqjtdnOS4_gnRDe0Tk8Me7kVgqsJ0KiU22zg7kfgiNlNvfF2o0cHN6e2O8BVp6lADCP4SG9IFpjD1s9puFkOnwj0DXaA6KbE96rmt_2H8CGZ5rgk6rAtSnCu-2eB1BkDPgjgAsGHPSxAb2jiJknZEUf_0UBkynda_vjEcRWhOCw_GSWWhFi1EaeQPJ85voZlH1DZWYJ3Sr1x8o_68B2JXAheJbcgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GC5awepKuPIQikKgBp2a16beqql4I8Iz-thWgKbv7xmKshZxAT1VVU1n4G5Zm5m2OguXnBjxWbTLBVBYhuNQjP--rzX9zTe7PG_rkTU_guzQ7ujp3j_Ul0oTu6mJ2RdhdHtLQOfJ6SrN1e20fVwb_Ra7m-6VH8SZnA1Dhsqqu8Dac3Fl7chdFplGaCKNg3CNPQmubx-irHEP-Vp24pUHY0rZQRpncMg1ihYm6Nbis03ErxAwMaPKS0DrBjMstotHrQMnFaKRGZUBMTpD2rF45Ji8ZE1UII7vILAeD2LRctN0Xv6IszAbIjsF3VtsKR1h1X1e8YZ_PBgSJg3dlWRAcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SMof02B2Pkf4Y1_mMyAVC6JNGzaP2TfZGp4ylB9fG8n5bp3d1JnHteQpHPUFHo9r8duOKsK01fU4mL3-iMeTMgMPAz6zUC2QuhlZiR27rVuSrcPUyWUyuThYyg3z7fVZ-e_M30a0it0X2tZs4k2RTiNVerQuArK7w4V7wauEoNN3DNMdJfuCr2tnDrdnBmAI-T4qLMDBObDzoF9iqXbXCLE5Jd9yTGeaL_W_kiZ_qTQwn7nm0uOOigMLPZOBTO-Li7QcvaCOTTRHnAo_b5fTxGyL5lmilp-gk-jZKPV9Z3eHeFeW7iunFjNpgMraGnkzFBXgDN0G8_vRvmd8BJQ-QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ai2-XVujOOBJVujaotZtJTSeWstG0URD-N5Y6CakU6wvAzbLVYdAdRYROmBDZx9a0qXugOIkc1DunnAt-5JgEqmrEswcR9oCMxHyg98lcifd_wJmYc35bM6DekZpr8i0AwZzOFibS_TyDlCCApLUgRHJeF5TokrfsE3GybgikEWwKZIAhnE6OS2mV0d4O-VhJYVyp5kY7yOuctwl3wG1C-PXk5kyjkCJKyUD_M_EgbzZyG0C4DhPUphVbnS6y7CX4ji_VvOotPIcmk1mLgIyc72X02oD8IcLMQ9J1JpxMzRfF_hVm9AQsTDKdTBswJex6qQCcku3AsKAOSJ6nR_Mcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S91b-6vMXazBxhk1pDh_nqHOLLN4lJyqO-l9ubTCttq5WnEN_8EW-rsWAkjBqhZugp3kO4CzYVBPFu79B7KR4QR184mX1fcT1ksOtlOjQnC4yBoZr9wy7mJNmUInV-wsW0IWmKg3Sf80agaVNUlVbTrgOHTl9wjsHN795S1rEOfCARV0vTWxUdyynbGfM89SfejaPcqNUvBBEys69aM5sVS_iqxDks4ma8tLkG2OGfu-kbMhqt2TZ09JyHmZbO808uuWlALSYENhS6Qb-vnjmAXvCStl1Qr1gN3u8slAT25hUEreNQdPTSDdVOxWW9z8OSvFng4s_-ldzMx4-EE-eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ: پیش از نهایی شدن توافق، دارایی‌های ایران آزاد نخواهد شد
دونالد ترامپ، رییس‌جمهوری آمریکا، در گفت‌وگو با شبکه ان‌بی‌سی نیوز گفت که به‌عنوان بخشی از هرگونه توافق، دارایی‌های مسدودشده ایران را از ابتدا آزاد نخواهد کرد و هیچ تحریمی را نیز پیشاپیش لغو نخواهد کرد.
او افزود که اصراری ندارد لبنان در توافق کوتاه‌مدت میان واشینگتن و تهران گنجانده شود.
ترامپ در پاسخ به این پرسش که آیا این اقدامات پس از توافق انجام خواهد شد، گفت: «بله، بعد از آن. اگر رفتار مناسبی داشته باشند و به تعهدات خود عمل کنند، آن وقت گفت‌وگو را آغاز می‌کنیم.»
رییس‌جمهور آمریکا اضافه کرد اگر بتواند با تهران برای پایان دادن به جنگ سه‌ماهه میان دو کشور به توافق برسد، آمریکا با ایران برای جمع‌آوری و نابودی ذخایر اورانیوم با غنای بالای این کشور همکاری خواهد کرد.
او افزود در صورت عدم دستیابی به توافق، واشینگتن توان نظامی جمهوری اسلامی را بیش از پیش تضعیف خواهد کرد تا نیروهای آمریکایی بتوانند با امنیت کامل این مواد را خودشان جمع‌آوری کنند.
ترامپ افزود که خواهان اضافه شدن بندی جدید به توافق است تا ایران نتواند با خرید سلاح هسته‌ای یا تجهیزات مرتبط، محدودیت‌های توافق را دور بزند.
او گفت: «پرسیدم اگر آنها خودشان سلاح هسته‌ای تولید نکنند اما آن را خریداری یا به هر شکلی به دست آورند چه؟ من می‌خواهم در متن توافق عبارت خرید، تهیه یا کسب سلاح نیز گنجانده شود. آنها نه حق تولید سلاح هسته‌ای را دارند و نه حق خرید یا دستیابی به آن را. تهران در ابتدا کمی با این درخواست مخالفت کرد اما از موضع خود عقب نشست.»
دونالد ترامپ، رییس‌جمهور آمریکا، درباره مجتبی خامنه‌ای و محل اقامت او گفت: «او به‌شدت زخمی شده است. نمی‌خواهم بگویم می‌دانم کجاست یا نه، اما احتمال زیادی وجود دارد که از محل اقامت مجتبی خامنه‌ای مطلع باشم.»
ترامپ همچنین اعلام کرد فعلا قصد خروج نیروهای آمریکایی از منطقه را ندارد؛ حتی با وجود آتش‌بس شکننده و ارزیابی او مبنی بر اینکه توان تهاجمی و دفاعی جمهوری اسلامی به‌شدت آسیب دیده است.
او افزود: «هزینه نگه داشتن حدود ۵۰ هزار نیروی آمریکایی در منطقه بسیار ناچیز است و ممکن است برای اعمال فشار در مذاکرات به آنها نیاز داشته باشیم».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75984" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
