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
<img src="https://cdn1.telesco.pe/file/d5xL_KcNlfnLLwCzMzt0oml1CB6Hz-c2Q37JGauiIf-VlHBk_k73XUUBhl9LAcQzvamfcdfF3kf1Z057Y2oSFXeEBE-Nmf6zR-Uc4ZkOBOW8arb0jr_QP5a7cynyuwWUn9hJHMm9_7ftOWgjokCXV9E9oRKpodIpHzfgV9cn7v7-ltjXk-I6XaJVyFJPW_KR7xFhPOtXOY_vfN16ilTrsMJiwyykUqa4x86HQw6hc88JXSdUDE4C_sE9z1K1iBNXrc4P1pD8vrAnfk4vaeBUeljNcmOo-L5Z50PGrpOXudvsV-uqFBkoS92V5ahR_lMsjeqbuVVWFTTsqQ8LioASHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 13:46:06</div>
<hr>

<div class="tg-post" id="msg-77352">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پیام‌های زیادی از اصفهان دریافت می‌کنم درباره شنیدن شدن صدای انفجار و لرزش شیشه‌ها
پیش‌تر اعلام شده که:
صدا وسیما: صدای انفجارهای کنترل شده مرتبط با مهمات عمل‌نکرده از ساعت ۹تا ۱۶ بعدازظهر امروز در جنوب و غرب شهر اصفهان، بهارستان و محدوده‌های صفه و شهر ابریشم شنیده می شود
مردم نگران نباشند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/77352" target="_blank">📅 09:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77351">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oUDb2EKz0cIHP20RXtARKCCufGM70J5dxqPJP_yB8fg--eIsITgFLFc_OgP7UsJvcfV5wGYsaCI3b7rpixbSlEiEShRRN8i4cLAuFFe5UBt_9DfcuaEXoVgavqPRjbf9E00636n2x82bO9LPOyBfFA9mZrYoZWokKhn-4VExEha20B4I_h2Lu-S_Kl-o-FXI9Ez0vY10M06pP4y3jmyNg26DsgjLAyCO0VU7fblVt1n7gZg3Gcui39cVNgFuSYUxHzv_EbYMCIEMuO-7Zn64BteH8kv_ixA46vLnHVT3TowsoPVA5CAck18NRNshhZqhzGToBPDSHG-XY6aU4Etj1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای سپاه: سامانهٔ راداری دفاع موشکی و یک هواپیمای اف ۱۵ در آشیانه دشمن در اردن منهدم شد
خبرگزاری فارس:
🔹
روابط‌عمومی سپاه: ملت عظیم الشأن ایران اسلامی! با استعانت از خدای متعال، در ادامهٔ عملیات پاکسازی منطقه از رادارها و سامانه‌های پدافندی و هموارکردن مسیر حملات موشکی و پهپادی گسترده‌تر و تکمیل شب سیاه راداری دشمن آمریکایی، رزمندگان غیرتمند نیروی هوافضای سپاه در ادامهٔ موج ۲۴ عملیات نصر ۲ در حملهٔ موشکی به پایگاه آمریکایی در اردن یک سامانهٔ راداری دفاع موشکی را تخریب و یک فروند هواپیمای اف ۱۵ را در داخل آشیانه منهدم کردند.
🔹
این منطقه جای متجاوزان آمریکایی نیست، ارتش کودک کش آمریکا برای پیشگیری از تلفات بیشتر باید منطقه ما را ترک کنند.
📝
گزارش تکمیلی این عملیات تنبیهی به استحضار ملت شریف ایران خواهد رسید.
ادعای سپاه: زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون در بحرین ویران شد
خبرگزاری فارس:
روابط عمومی سپاه: با توکل به خدای قادر متعال و در هم کوبنده ستمگران، رزمندگان هوافضای سپاه در ادامه موج ۲۴ عملیات نصر ۲ در پاسخ به تجاوز و تعرض روز گذشته ارتش کودک‌کش آمریکا به تاسیسات در دست احداث و غیرنظامی دارخوئین، زیرساخت مرکزی داده‌های شرکت آمریکایی آمازون را در بحرین با چند فروند موشک کروز مورد هجوم قرار دادند و آن را ویران نمودند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 254K · <a href="https://t.me/VahidOnline/77351" target="_blank">📅 09:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77350">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرماندار آبدانان: آمریکا با موشک به نقطه‌ای در کوه‌های اطراف آبدانان حمله کرد
خبرگزاری جمهوری اسلامی، ایرنا:
🔹
به گفته فرماندار آبدانان، ساعتی پیش دشمن متجاوز آمریکایی با چند پرتابه مناطقی در بیرون از این شهر استان ایلام را هدف گرفت.
🔹
بهزاد نورمحمدی صبح سه‌شنبه در گفت‌وگو با خبرنگار ایرنا اظهار کرد: دشمن آمریکایی با پرتاب موشک، به نقطه‌ای غیرنظامی در کوه‌های اطراف آبدانان حمله کرد.
🔹
وی افزود: خوشبختانه این حادثه هیچ‌گونه تلفات جانی در پی نداشته و دستگاه‌های مسئول در حال بررسی ابعاد موضوع هستند.
🔹
نورمحمدی یادآور شد: دستگاه‌های امدادی به محل حادثه اعزام شده و مشغول بررسی دقیق ابعاد تجاوز دشمن هستند.
پیام‌هایی که من از یک شهروند دریافت کرده بودم از ساعت ۲:۴۱:
سلام وحید جان صدای دو انفجار اومد چند دقیقه پیش
ما آبدانان هستیم ولی صدا خیلی دور بود بیرون شهر بود.
ظهر هم رد موشک تو آسمون دیده میشد
الآنم یکی دیگه
2:49 دوباره
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77350" target="_blank">📅 06:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77349">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=td0112gzcJC079DD_ZEhcMTqQNEY3V84N6Zy2Fa0NWYxCHCOS-rFFE49cYzGD5-5Z0qdttjHx1xTV4U7L7dLg5WfnhOuAt8o61wrVmg82fT4lW2kO_0wVRF8rDaYyqwRhPMXtNiWwIWZkCMXG2O5yIVU2MWmJOYNCriidCBOS1ovSXFhk93WMFRa_5a-IENpR8nCNeNKxtg2bkYMRh5JVAvB7xq-IQJffclpbp4vo4VAsGLw1-SIYDs70_C12R_za8XpMq-EyLHp-HiUK0PNNWvoZKueWsTaKwtu6ZdjK3TWOD6PzLlsL7QXx51bHK5GnZvdb2K9caJx75Q8lTSLPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e6445e1dc2.mp4?token=td0112gzcJC079DD_ZEhcMTqQNEY3V84N6Zy2Fa0NWYxCHCOS-rFFE49cYzGD5-5Z0qdttjHx1xTV4U7L7dLg5WfnhOuAt8o61wrVmg82fT4lW2kO_0wVRF8rDaYyqwRhPMXtNiWwIWZkCMXG2O5yIVU2MWmJOYNCriidCBOS1ovSXFhk93WMFRa_5a-IENpR8nCNeNKxtg2bkYMRh5JVAvB7xq-IQJffclpbp4vo4VAsGLw1-SIYDs70_C12R_za8XpMq-EyLHp-HiUK0PNNWvoZKueWsTaKwtu6ZdjK3TWOD6PzLlsL7QXx51bHK5GnZvdb2K9caJx75Q8lTSLPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی با انتشار ویدیوی بالا: سه پایگاه مهم آمریکا در کویت، هدف حملات پهپادهای انهدامی ارتش قرار گرفت
مرحله نوزدهم عملیات صاعقه ارتش
روابط عمومی ارتش:
🔹
در پاسخ به شرارت‌ها و نقض عهدهای مکرر شیطان بزرگ، بامداد امروز و در مرحله نوزدهم عملیات صاعقه، ارتش جمهوری اسلامی ایران، ساختمان‌های اداری  و آنتن‌های جهت‌یاب در پایگاه عریفجان، پارکینگ گروهی بالگردها در اردوگاه العدیری و ساختمان اسقرار نیروهای ارتش تروریستی در پایگاه احمدالجابر کویت را هدف حملات پهپادهای انهدامی خود قرار داد.
🔹
پایگاه عریفجان از بزرگ‌ترین مراکز استقرار نیروها و ستاد فرماندهی نیروی زمینی آمریکا در جنوب غرب آسیا و پایگاه العدیری محل استقرار بالگردهای آپاچی، شنوک و بلک هاوک نیروهای دریایی و هوایی  آمریکا است.
🔹
پایگاه احمدالجابر نیز نقش محوری در آماد و پشتیبانی ارتش متجاوز آمریکا در غرب آسیا دارد و تاثیر عمده‌ای در عملیات‌های هوایی و نظارتی این کشور ایفا کرده است.
🔹
ارتش جمهوری اسلامی ایران اعلام کرد، امنیت منطقه در پی شرارت های نیروهای تروریستی آمریکا مختل شده و  نیروهای مسلح جمهوری اسلامی تلاش می‌کنند در نبرد با آمریکا، امنیت و آرامش را به منطقه بازگردانند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77349" target="_blank">📅 06:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77348">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/841c527612.mp4?token=DaX6zGhjXbJNWA4iqsiLjC7xrbx5c0MRhQRsL6vmoocXOUuhLr658X_iwSmRTD0Isxidy_QrAuOpeVpwKFMu7HDiyOZDwmRl5h9hwSktvymb4ROMmD8vMVLHE_f7Ocvr4Fg5RIsDGbC_11flO4qiXCvsXHEU5cNgpr9j2zpn0eQoMY9yIw2e-WXf6LVOlh-8_ql4qarLoyY37tX6mitugzeivTRppdDepArHMDXqfHVKsuTvzFeA-8LrA_psHIpCtz-7g20hnCFVyzR7sMtxMccOzkj4G8Rdh4xF32zs836XHKDY_Z1utWCrIuephyS3GoyGhg6cC24_8JQ4_AOwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/841c527612.mp4?token=DaX6zGhjXbJNWA4iqsiLjC7xrbx5c0MRhQRsL6vmoocXOUuhLr658X_iwSmRTD0Isxidy_QrAuOpeVpwKFMu7HDiyOZDwmRl5h9hwSktvymb4ROMmD8vMVLHE_f7Ocvr4Fg5RIsDGbC_11flO4qiXCvsXHEU5cNgpr9j2zpn0eQoMY9yIw2e-WXf6LVOlh-8_ql4qarLoyY37tX6mitugzeivTRppdDepArHMDXqfHVKsuTvzFeA-8LrA_psHIpCtz-7g20hnCFVyzR7sMtxMccOzkj4G8Rdh4xF32zs836XHKDY_Z1utWCrIuephyS3GoyGhg6cC24_8JQ4_AOwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند.
ترجمه ماشین:
پایان تازه‌ترین حملات آمریکا علیه ایران
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دور دیگری از حملات علیه ایران را در ساعت ۹ شب ۲۰ ژوئیه به وقت شرق آمریکا به پایان رساند.
نیروهای آمریکایی مراکز فرماندهی نظامی ایران، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد و سامانه‌های پدافند هوایی را هدف قرار دادند تا توانایی ایران برای ادامه حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز را کاهش دهند.
عبور کشتی‌های تجاری از این گذرگاه حیاتی دریایی بین‌المللی همچنان ادامه دارد. از اوایل ماه مه تاکنون، نیروهای سنتکام به تسهیل عبور حدود ۹۰۰ کشتی تجاری و ۴۵۰ میلیون بشکه نفت خام کمک کرده‌اند.
نیروهای آمریکایی همچنان در موقعیت و آمادگی لازم برای پاسخگو کردن ایران به‌دلیل تجاوز بی‌دلیل علیه دریانوردان غیرنظامی که در پی عبور آزادانه و بدون مانع از این تنگه هستند، قرار دارند.
CENTCOM
اطلاعیه شماره ۳۵ سپاه:
شب سیاه رادارها و سامانه های پدافند هوایی آمریکا در منطقه
روابط عمومی سپاه:
🔹
ملت عظیم الشان و مجاهد ایران اسلامی؛ حماسه حضور در میدان و ۱۴۰ شبانه روز ایستادگی بی‌نظیر و پرشور شما چنان روحیه ای به رزمندگان اسلام و مدافعان از جان گذشته وطن بخشیده است که با لطف و امداد الهی هر روز حماسه‌ای نو خلق می کنند.
🔹
ساعاتی پیش عملیات بزرگ رزمندگان اسلام برای تنبیه ارتش کودک کش آمریکا به خاطر برهم زدن امنیت تنگه هرمز و تجاوز به نقاطی از میهن عزیزمان آغاز شد.
🔹
فرزندان شما در نیروی هوا فضای سپاه شب سیاهی برای رادارها و سامانه های پدافند هوایی آمریکا در منطقه رقم زدند و در موج ۲۴ عملیات نصر۲ با رمز مبارک یا رقیه (س)، به منظور هموار کردن راه عملیات گسترده آینده و از میان برداشتن موانع اصابت دقیق اهداف یک سامانه پدافندی و یک رادار آمریکایی در المحرق بحرین به طور کامل تخریب شد و از مدار عملیاتی خارج گردید و همچنین یک سامانه پدافند هوایی پاتریوت آمریکا در اَلرفاع بحرین هدف حمله همزمان موشکی و پهپادی قرار گرفت و نابود شد.
🔹
تنبیه متجاوز ادامه دارد و گزارش آن به استحضار شما ملت عزیز و قهرمان خواهد رسید
و ماالنصر اِلا من عند الله العزیز الحکیم
اطلاعیه شماره ۳۶ سپاه:
یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی و یک سوله آشیانه پهپادهای MQ9 منهدم شدند
روابط عمومی سپاه:
🔹
ملت عظیم الشان و قهرمان ایران اسلامی؛ در ادامه عملیات تنبیهی رزمندگان هوافضای سپاه و در راستای هموارسازی مسیر، برای دفع موانع عملیات هوایی و موشکی گسترده در مرحله دوم موج ۲۴ عملیات نصر۲،  امشب یک سایت راداری برد بلند، یک مرکز مخابراتی و سامانه های دریافت ماهواره ای، یک رادار دفاع موشکی ارتش کودک کش آمریکا مستقر در کویت مورد اصابت موشکی و پهپادی قرار گرفت و منهدم شد.
🔹
همچنین یک سوله آشیانه پهپادهای MQ9 نیز در پایگاه علی السالم مورد اصابت واقع و تعدادی پهپاد منهدم شده یا آسیب کلی دیدند.
🔹
عملیات تنبیهی فرزندان شما ادامه دارد. التماس دعا.
و ما النصر الا من عند الله العزیز الحکیم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/77348" target="_blank">📅 04:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77347">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LmX7HzVKFKYzQCPB69SNetSeEIsPxRgJ71KAlchBPo2-RE_tlFtaJN_LlwxGi2DKFUp0B5bSML7ecifaFfn0ZlBSkOOCzc434Jk_DFty4UGVWgfVGAbpquL7xJuqTpJ5Hdg1FQmkTLqLagdV0C2YxSw6CqM5gEvdHYS8ElNanvnjqpDT0bqqewaYKBUFiVUCZaUOj05_9D2-ST3sJjT5Z94-lkqydSGaOvtqSplNulqKJxxOfJZoP0diRdrbqmxN4mGfIpb5SON6PH7VpOaXf8vhTXFyGuS-q5JzZ0Ovh_M2vW2-eGjfm9q2JB-wxYRky8r_22pNWD_1aMZl0yFUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
خبرنگار صداوسیما: حوالی ساعت یک بامداد در برخی نقاط شیراز صدای انفجار شنیده شد که بر اساس گزارش‌ها یک نقطه در شرق و دیگری در غرب شیراز مورد هجوم دشمن قرار گرفته است.
چند پیامی که من دریافت کرده بودم:
شیراز رو باز زدن
یجوری شیراز رو زدن که شیشه ما بدجور لرزید
سلام صدای دوباره انفجار در شیراز
شیراز دوباره زدن
خیلی بد زد
شیراز 1:21 صدای دوتا انفجار خفیف دیگه اومد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77347" target="_blank">📅 03:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77346">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvyl_Ji8l2ZwxzDqTCA4yA8Uus7sYq4GVnv9MqT7vs0ASW-pGx9aHA1LmNQdxhsNa7R9iY5whThSMGMWkinVrzwki-K0TcZrwKSvId_hAr0kuB5tmyJyZUVWfuAVJ47LyNACP4UFW-xJgrGP0T06KHvPpAZnoECSLQHBr7sHEXjEgZD6EEfBOmXRWertgOJVd985jOCOqpsTrbDVCZjShfeMsdqiGYkdNf_KeDs0b6hwWPiA_ZEonYQVwPbnUFX5JemXIgW2I4W5DfzLMb0pNoxauXV3H9vbQFA7yjC8L4E2QbKaO5bZKMQsdzXrKqVAUzYmC1CAmg-8aV-BprRV8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درباره تماس با نخست‌وزیر تازه بریتانیا: درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
ترجمه ماشین:
گفت‌وگوی بسیار خوبی با نخست‌وزیر جدید بریتانیا، اندی برنهام، داشتم. درباره موضوعات بسیاری گفت‌وگو کردیم، از جمله روابط فوق‌العاده‌ای که با بریتانیا داشته‌ایم.
در آینده‌ای نه‌چندان دور برای گفت‌وگو درباره موضوعات مورد علاقه مشترک دیدار خواهیم کرد. نخست‌وزیر کار بزرگی پیش رو دارد، اما قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا نیز برای کمک در کنار او خواهد بود!
درباره نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌روبی تنگه هرمز و بسیاری موضوعات دیگر گفت‌وگو کردیم.
این تماس جالب بود و بسیار خوب پیش رفت. برای نخست‌وزیر برنهام آرزوی موفقیت کردم: موفق باشید و خدا به همراهتان!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/77346" target="_blank">📅 02:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77345">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDniHT-m3hebZbgn5eBkYDnJYRCatX04LngpAHe05pLc2UV-0eYs8zNOO8JYQNkQbnGE6483HJVoLJnHPS8YO7fTmP1TLG-4zWReCi_yf2awRl--1EhrHshp08_DkdnN4Sw95p4vIIbvkT7EOHYwPOp-DA_vSOB9E0ATg9MJJgamqIDDNT_BzCJkdxfKq9kk9QJi2G7bzws5s3GqA53q8Y22VXshQiKIzn7SU5UFixh6J4WoITmicYCcPtQguvT8_CqtE5LukbiWgP1MwfJJ5bSipzpTdtyyyFXMGcXvl54Qt0tkh09F2vQwzbaBGFPTqbs2pzaFfo7Q9qjkDQiqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از یک حادثه در فاصله ۸ مایل دریایی شمال شرقی لیما در عمان دریافت کرده است.
این سازمان افزود گزارش‌های متعددی دریافت کرده که بر اساس آنها، یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده در تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77345" target="_blank">📅 02:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس پایگاه هوایی ۲ انفجار ۰۱:۴۷
بندر ٢ تا شنيدم ٣٠ ثانيه پيش
1:47 دو انفجار به شدت قوی در پایگاه هوایی خیلی شدتش زیاد بود بندرعباس
بندرعباس ۱:۴۷ دو صدای انفجار شنیدم
درود آقا وحید دوتا انفجار وحشتناک ساعت ۱:۴۷ دقیقه بندرعباس
همین الان ساعت ۱۱:۴۶ انفجار فوق شدید بندرعباس
۲ تا انفجار وحشتناک بندرعباس ۱:۴۷
صدای ماشین‌ها درومد
صدای دو انفجار الان بندرعباس ۱:۴۷
بندرعباس ۱:۴۷ صدای دو انفجار
تک انفجار شدید بندر
سلام الان صدای دوتا انفجار بندرعباس اومد
سلام وحید جان صدای دوتا انفجار پشت سر هم اومد بندرعباس
ساعت 1:48 بامداد
بندرعباس ۳ تا انفجار شدید
صدای ۲ تا انفجار سمت پایگاه هوایی بندرعباس
سلام صدای دو انفجار بسیار شدید بندرعباس ساعت ۱:۴۷
درود وحید جان وقتتون‌ بخیر
بندرعباس ساعت ۱:۴۸ دو صدای انفجار بلند.
بندرعباس ساعت 1:47، دو سه بار سنگین زد
سلام وحید جان الان دو تا انفجار سنگین سمت فرودگاه بندرعباس آمد که شیش ها لزیدند 1:48
سلام وحید خان بندرعباس ساعت 1:46 چندتا انفجار پشت سر هم
سلام وحید بندرعباس همین الان صدای 2 انفجار خیلی وحشتناک
اقا وحید  ۳تا انفجار شدید قشم ساعت ۱:۴۶
وحید‌ داداش
حوالی۱.۴۷ اینا دو انفجار مهیب. اومد
فک کنم پایگاه هوایی بود
ثانیه پیش هم زدن
حدودا ۴ انفجار شد
تعداشو دقیق شمردم کمی با هم فاصله داشت
در حد هر کدوم ۳۰ ثانیه
ولی همش از یه سمت بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77344" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی:
۱:۴۵ قشم صدای انفجار همراه با لرزش
قشم من چهارتا صدا شنیدم، نمیدونم توهم زدم یا واقعی یود چون خیلی خفیف صدا اومد ۱:۴۵
چهار انفجار فعلا بندرعباس
وحید جان
قشم چهار تا انفجار ۱:۴۵ دقیقه
صدای انفجار بندرعباس ۱:۴۵
سلام وحید جان ستا انفجار همین الان بندر عباس ساعت ۱:۴۵
بندرعباس الان دو تا صدا آمد ولی صدا دور بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 289K · <a href="https://t.me/VahidOnline/77343" target="_blank">📅 01:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77342">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع حکومتی
منابع محلی لحظاتی پیش گزارش دادند برای دومین بار طی بامداد امروز صدای انفجار در بندرلنگه شنیده شد.
چند پیامی که من دریافت کرده بودم:
سلام وحید جان بندر لنگه دو بار زدن
صدا و لرزش زیاد
ساعت ۱۲ و ۴۰ دیقه
ساعت ۰:۴۰   صدای انفجار در بندرلنگه شنیده شد
درود وحید جان
صدای انفجار در ساعت ۱۲:۴۰ بامداد از بندرلنگه اومد ۲ بار
گویا هدف، نیروی دریایی سپاه بوده
صدای انفجار ۲ بار در خونه لرزید بندر لنگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/77342" target="_blank">📅 01:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77341">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پیام‌های دریافتی:
۳ انفجار در کنارک همین الان
۵تا انفجار سنگین چابهار ۱.۲۷
مجدد چابهار صدای چندین انفجار میاد
چابهار ۱:۲۷ دقیقه صدای ۲ تا انفجار اومد
ساعت 1:27 چهار انفجار پشت سر هم دیگه چابهار
کنارک 1:28 دو انفجار
۱:۲۸ دیقه کنارک دو بار صدای انفجار اومد
🔄
کنارک 4 انفجار دیگه
خیلی سنگین بودن این چهار تا انگار خونه رو سرمون خراب شد
۴تا دیگه چابهار همین الان ۱.۳۰
۱:۳۰دقیقه ۴ بار چابهار زد
نمیدونم کجاست اما از سمت دریا بزرگ دورتر
۱:۲۹ چابهار ۲ تا انفجار دیگه اتفاق افتاد
دوتا پشت سر هم و باز 3تا پشت سر هم 1:30 چابهار
صداهای شنیده شده در چابهار و کنارک: ۵ انفجار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77341" target="_blank">📅 01:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77340">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcyZt4oSPzKnCh4gxWfkGALSFDTFZXIe2kEvm4AT-L1Kihf3B9JHbE8UIemv-tHvoL-AWxNrLw1atXFq24u-oVaWwmdFoj6CV2Z5aFiyThYgNz4s3lHKpfADvmvhLi932uqLxurlz12E115c3I5DXdoMek9DAgXQWTgx5wMRHVS4LvlFJ6x0qZObUSVHomAAcKa887PVLMdFIJvplQ2z8lhI0ZOL27-trYXqVRVSjy5G7UlOX5RRhqcdQBJxha0acabp26_Qg_HBAxtCShsBFjI2djIajKTjnw1ScRBe7qPvY2wCJyjeKdsFggxN2QmokQt0xpfWbeRrH1TECumKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر از شنیده شدن صدای دو انفجار در شهر اصفهان خبر داد.
دقایقی بعد، استاندار اصفهان اعلام کرد که امشب حمله‌ای به شهر اصفهان صورت نگرفته است.
@
VahidOOnLine
فارس:
استاندار اصفهان گفت: امشب حمله‌ای به اصفهان صورت نگرفته است.
وی ادامه داد: در حال بررسی علت شنیده شدن صدای انفجار اعلام شده از سوی شهروندان هستیم.
تسنیم:
معاون استانداری اصفهان: هیچ گونه تجاوز دشمن یا انفجار در سطح شهر اصفهان و سایر نقاط استان نداشته‌ایم
من هم چند پیام مردد داشتم و از این رو فکر می‌کنم صدایی شنیده شده ولی مطمئن نیستم که دلیلی نظامی داشته یا نه.
منابع زیادی هم هستند که هر روز کلی خبر دروغ تولید می‌کنند و از این رو اعتنا کردن به پیام‌هایی که بعد از چرندیات تولیدی اون کانال‌ها ارسال میشن هم خیلی سخته.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77340" target="_blank">📅 01:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77335">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fj9-HXlVRZ4uET2fMpUpx_WaJK98DWp1wSzBObPni73U44_GKT4MqvciNmeLz6Q0RGeqruenwu1FnIDHGNC3641D0vBkaPPwH9-JitQosPBVOtwd-UlNo64ftEy0xhxA2MMTXhI1JTD5V5VQHv3KluouFi0Xp3I10zzEAyx4bc8ZmEkkxP4dsqn7flqzuWzdMOvy396EvnmE5Nzm-vZmxyLvXHJbT9O1d0DIIttzU6KtBffVjgTV9K4cDDkg8cel8XdqqVEyzDc1ILbEdzyjcpOw1Gc9IjphQZseGu8N0Vfu-pHUo9-LzCXOOZJMd1gY-vp-0azyBOdAqRVLLaajGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qTyfJB50HQGaG_xGAb8Q1Io-4k8z3OpFJG9Oj6LpdLDXuJ_ZwKCPXLh_F9flwwUi93RFY_BStLsHBO4cSInIXevkxRxlmPT5RFUFWEVWp-dgnLnwBWamv4fqNqWDWvv8NirtXK8e16O_-S97X06T-oN36FyrU3-qLjMVa2yrSw3yWqkgwn4oXQYuExYtV3Jf4A9F974QWDq08HoCSED62CiIbWcponenBX9scAJL8zhb3gG7yNyyf6752noraKqkZ_V_U7qWfnhSLIwl5qhgbIgnNANegbPebc-zgEzT6VH0afbLj-siz0n2hgyolNxyzhf8SAYnUJ5Vcj8B4xG23Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YNxqCYNT33bQb5kIjlTa5kUhg7Nd5zOYvBOOWSQvSvnTWZ04OIjbNz8qQz015U5XxfwmXfOEu_Jh0OYFm-DXs2_homcKFx5QxKSgbIeykaFJ-r_qRK91JRoaR1zP6g5inGbm09Pq43HRIvFh6Eve5OcKWb9nKznFHY-Q_Lf1e-UOe6uVJQp3fHT4eApXydlAO4S2HoojG2G6-r6kdrPrsh6Zc2cQ1UVgT90QYy23Z7B7weCDdH8UDoXEWSnCAA28QYZawUWgm0en4zuDc7PhoXPU3kvpLq602bp-57kvrEfrxCycRMnuInU7igmPcF6Mx4dZ_-2snqzQ2km_MPmc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hSYAj-GkygHG8oL_60GhUBz4sy7TFs42OdecpSXhB5CBztSTZZOZ5BiE1ozTvXxRsQFB9ybIskbALzyH08mAGBxwqyrGV3ariER6RZ2nZfjHvih3btkC8WWcwhzlPFPUwQ204ZZNKzvqbI7iZbtDI7Jz4uBWPcQRMYByspi4PdQsPHzAmIGKbpDlXJJO7KXK6xudB1qr6YvYaRiHDR9whup1Nf6zluVGLfklaM7IcRQV9eVWSzO9amNC3ZBQgc6GtaFVvzl3U2twSlQ3QDOKPMdeeXEjIUUkxQJV_ZHzePoP4MJSOsT3NVP5a3MCqg7KvlM4qy01DTVP1sAKB5EuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XxNtdTEx6gNlK-GKxQE9QEIRRElcdFFnoD8VVxr2NZrujSjIZdikJC2RjjWPZIgCzcOIpPYXyQMDqzEOW0K4zC8v4rCW0WLhGbuCupUQFjkJba0mqOY1CGjRTOjmPQzanbTTGVj27gwSMtA9JVP8jWDqwv1OPqMtt157uEAlS_0sBDQkmJMBs-FY5pZV8XHN97oUUu2dp8S8YySCPwFDIhuZIci5CuMYjh25AnxKQlsieGvqsQY38z-um6ItgUtkXNfCvVkgl445hkt8WUyRJXM-PzPQIeV5ogwQ5ADnfboEH4sWYyKSVxZalULxNklQJtcfTgB6anLTYI7raO9iQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Vahid
'هدف قرار گرفتن نقطه‌ای در کوه دراک شیراز'
تصاویر دریافتی از شهروندان با شرح بالا، سه‌شنبه ۳۰ تیر حدود ساعت ۰۰:۴۰ بامداد
Vahid
📍
میگن
اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/77335" target="_blank">📅 01:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77329">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N6iRSAvjQ19wzHOn4RZFGvWP7ZPkfNSF6QSDuufnKckFigCy30_VF7twLPHzvSXoQ_71p0QSHkSADCjYIALy3y8n9YYZ6_vn2ssLSV9ycOld5n-QRmG2x9HDdBOFs3OgXF469y_eX0JJuJirGrk-4oy_J7UmzKCnnif4AGSYhagCwc4zQ8ZZd5NwjN1Inmh7IdVz2IB85QxpgWt-Nj5APmCgp1FcGkM_UyLUkNA-mJJ1lxlPSRNAmx6F-v_zHJ_YxXvvlkXTBsbhdkrxTXgmrDUVBsJq4ENsTCck4UaeHIAEYhr80mnm-PLqbPVSsAh0i_Yl-xByMRBVKRIPC1osJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dCqWINznRfW8fTo3jwdVVOi0iS2ec8ykUbwh80qTFep70SNqoNbfzJKcgc8vh5bSv7fCZqvSmHvEjudz3ICPX7Ac9i0HpsaeYOVI5Y_7lr3KiLDtLQ_cQyeAin4gPZQDDbORxdeUGkso6iz1BQWGUcLnj4TzM44cBAJSSMSDMkAemRb2g0E2vS8FnE7bnf-VQ3BMLCEZcAiO5SiPLu9u07nCoC7xU3jlCd1oy2iKv7d2wIoGA8oNPiPMciMwN_51Q1xai7YsGkMYfHjKcMZMa99tia1UAx8MHPnSmUHSUDAkq1NlCOL8AQnVz9-mbojodFSQUDMDmy5ehm7otUs4zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی درباره صدور هشدار در کویت
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77329" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77328">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده ده دقیقه پیش:
سلام شیراز همین الان صدای انفجار اومد12.37
شیراز همین الان صدای انفجار اومد
شیراز همین الان صدای انفجار مهیب اومد
🔄
پیام‌های رگباری الان:
همین الان شیراز و زد کلفت
همین الان صنایع صدای انفجار اومد
سلام وحید جان
شیراز سمت صنایع رو زدن ساعت 00:45
00:45 شیراز صدای انفجار
فکنم صنایع الکترونیک رو زدن
همین الان شیراز صنایع رو زدن
شیرازو زدن همین الان
سلام وقتتون بخیر
ساعت ۱۲ و ۴۵ دقیقه بامداده
شیراز همین الان صدای انفجار اومد
شیراز صدای انفجار
همین الان شیرازو زدن رکن آباد خونه لرزید
فرهنگ شهر شیراز صدای انفجار مهیب  ۰۰:۴۵
شیراز صدا اومد
سلام یدونه تک انفجار صنایع شیراز ساعت 0:45
شیشه ها لرزید
ساعت ۰۰:۴۵ صدای انفجار از شیراز
شیراز ۱۲:۴۴
احتمالا صنایع صدای انفجار
درود وحید جان
الان صنایع الکترونیک شیراز رو زدن
این دومین انفجار امروز تو صنایع هست
شیراز الان 00.46 زدن
12:45 معالی آباد صدای بلندی شنیده شد ( انفجار یا بمب نمیدونم)
چهل و شش دقیقهٔ بامداد صدای جنگنده و انفجار در شیراز
سلام وحید. ساعت 00:46 محدوده صنایع الکترونیک، صدای انفجار شنیدیم.
شیراز صدرا همین الان صدای شدید انفجار اومد
شیراز صدای جنگنده اومد روی کوه دراکو زد انفجارشو دیدم
همه فکر میکنن صنایع رو زد ولی بالای کوه دراک بود
امروز ساعت ۵ هم از بقیه شنیدم که صنایع الکترونیک شیراز رو زده بودن
سلام شنیده شدن صدای انفجار صدرا ۱۲:۴۷
همین الان صدرای شیرازو زدن
شیراز صدای وحشتناک بلند همه جای شهر شنیدن یا صنایع بوده یا کوه دراک
وحید ساعت ۱۲:۴۵ بعد نیمه شب صنایع الکترونیک شیراز رو زدند صدای انفجار اومد
۰۰:۴۵ صدای مهیبی اومد، ما ابیوردی هستیم ولی صدای انفجار تا اینجا اومد
سلام همین الان حدود ساعت ۱۲:۴۵ شیراز صدای انفجار شدید اومد
سلام الان شیراز صدرا هستم صدای انفجار اومد
شیراز  0:45 صدای انفجار اومد
سمت فرهنگ شهریم ما
سلام ۰:۴۵ شیراز سمت شهرک گلستان صدا انفجار اومد
شیراز زدن نمیدونم کجا بود ولی من از فرهنگشهر شنیدم صداشو
سلام وحید جان  دکل مخابراتی کوه دراک شیراز رو با جنگده زدن ۰۰:۴۰
من رو پشت بام بودم دکل کوه دراک رو زدن
صدای جنگده اومد بعد زدن
خونه ما معمولا وقتی صنایع رو میزنه صداش نمیاد، این انفجار مشخص بود خیلی عمیق  و بزرگ بود که انقد واضح صداشو شنیدم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77328" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77327">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پیام‌های دریافتی:
چابهار صدای جنگنده سطح پایین میاد الان
سلام صدای انفجار شدید در چابهار ۰۰:۰۲
۰۰:۰۶ دیقه صدای انفجار اومد کنارک انگار دور بود
چابهار ساعت 12 شب دوتا سنگین زد
🔄
چابهار دوباره صدا جنگنده :۶
انفجار سنگین :۰۷
الان زدن چابهار 12:07
چابهار الان صدای انفجار شدید
درود چابهار الان زدن خونه لرزید 00:07
دوتا دیگه هم زد
چابهار همین الان دوباره زد
انفجار خعلی سنگین ۱۲:۰۸
وحید ۰۰:۰۷ انفجار شدیدتر
کنارک همین الان صدای سه انفجار
سلام چابهار الان ۳ تا صدای انفجار اومد۰۰:۰۸
چابهار همین الان دوباره زد
۳ بار شد
🔄
صدای ۲ انفجار دیگه در کنارک
همین الان یکی دیکه چابهار
صدای انفجار دوباره در چابهار
صدا جت امام علی زد یکی ۱۲:۱۱
باز یکی دیگه زد همین دقیقه
پشت هم داره میزنه
جنگنده ها در ارتفاع پایین در حال پرواز هستند
داداش امامعلی چابهار رو مثل اینکه زدن
سلام آقا وحید طرف های امام علی نه خود [پایگاه] امام علی رو زد
دو تا چیز شبیه فلر از سمت دریا اومد چابهار
نمی‌دونم چی بودن
منابع حکومتی:
فرماندار ویژه چابهار از حمله هوایی دشمن به شهرهای کنارک و چابهار در بامداد سه‌شنبه خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77327" target="_blank">📅 00:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77326">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dWVlCrXrLrgk5AS7IQZWdkeFE2aqteJ2y1i2mXsnsrmXbgMdAlJKyD2HrFynqv0FrtkyE2RUO1A0Nb3rhJW0k02WF6oVdpZoVj7bqb8qZ1MAhOzFJEfKald6OaJWK0YMm-Wt8jtgsZg7vkYLd00wcBPb0gaKfKgtGnsb1Dhak-s3ky9tpxrQTBDtXHZdEVR1tsovumguTnnnW-9KzlvYfUoJko6LN5g88P6giVA9QSpiJKOoOJV3er1KJmPTMNNTBxLvmXpVzC-sJE8F1u4QbdL8FuSm8OQg3vIazwIGmLWPkQSaNGhl2xewfVg21WM4wweOXn8JhRT0Wdh59_JjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۴ بعدازظهر به وقت شرق آمریکا [۲۳:۳۰ به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور جدیدی از حملات علیه ایران را آغاز کردند. هدف از این حملات، تضعیف بیشتر توانمندی‌های نظامی ایران است که برای حمله به کشتیرانی تجاری در تنگه هرمز به کار گرفته می‌شوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/77326" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77325">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار الان بندرعباس
صدای انفجار مهیب بندرعباس ساعت 22:33
همین الان ۱۱:۳۴ بندرعباس صدای انفجار شنیدم فکر کنم
سلام وحید جان ، بندرعباس صدا اومد الان
بندرعباس انفجار همین الان
سلام ساعت یازده ۲۳:۴۳ بندرعباس موج انفجار
انفجار در بندرعباس
بندر انفجار ۱۱.۳۴
ساعت ٢٣:٣۴ صدای انفجار نسبتا شدید بندرعباس
انفجار شدید بندرعباس ۲۳:۳۴
بندرعباس الان یدونه صدای انفجار اومد
بندرعباس ساعت ۲۳:۳۴ صدای انفجار شنیده شد
۱۱:۳۴ صدای انفجار بندرعباس
وحید سلام ساعت ۱۱:۳۵ بندرعباس یه انفجار خیلی شدید امد
بندرعباس صدای شدید انفجار همین الان 11:35 الهیه جنوبی
سلام صدای انفجار بندرعباس ۲۳:۳۵
بندرعباس الان صدا اومد تقریبا شدید بود
بندرعباس صدایییی وحشتنام ۲۳:۳۴ دقیقه دو تا انفجار
بندرعباس ۲۳و۳۵صدای انفجار اومد خیلی سنگین بود
سلام آقا وحید ساعت ۲۳:۳۴ دقیقه صدای انفجار اومد بندرعباس
ساعت ۲۳:۳۷ دقیقه یه صدای انفجار دیگه از سمت دریا اومد
یک ربع پیش از پیام‌های بندرعباس خبرگزاری فارس نوشته بود:
دقایقی پیش صدای چند انفجار از حوالی سیریک در شرق استان هرمزگان شنیده شد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77325" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77324">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u7ioZ2MeiQY638YqGBf50Fteuc17Sb9AdLjZVcT-2A3z3l8crymHJt0UoA1zgtAFX2SluBVj4oU4Vrst0sApNw04ZyBKMBW7XSoUGD6ZwTnFE8xBhTGCfhKV6NyPobOft4jg-XfEDV6Vpi37e4yydkqcpECftqvoQ0Y9UThs4-tVUdbJSHHZd0UY21i_sIiVxgv8-KA3HsSzqKS10tHkN8XwHQ-PnUxTyb3ZeqUWVzziYlE0HdVYT0mj4w08WcYcb_a-BfIvrDH1UuTL4Za6PUuAMwrFY5WAfdK97zd85sOntD3gbrSVYAr73kMlpMQN8Yc_JN4C0TZtxSJNzs9sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب فارسی وزارت خارجه آمریکا شامگاه دوشنبه ۲۹ تیر با انتشار یک هشدار امنیتی از شهروندان آمریکایی خواست در پی افزایش تنش‌ها در خاورمیانه، هرچه سریع‌تر ایران را ترک کنند.
در این هشدار آمده است که وضعیت امنیتی منطقه همچنان پیچیده است و احتمال تشدید غیرمنتظره تنش‌ها وجود دارد.
@
VahidHeadline
خبرنگار اکسیوس، ترجمه ماشین:
یک مقام آمریکایی درباره گفت‌وگوهای احتمالی آتش‌بس با ایران به من می‌گوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را به‌دلیل نقض تفاهم‌نامه و ادامه اقدامات تروریستی‌اش در تنگه هرمز مجازات کند. علاوه بر این، رئیس‌جمهور ایران را به‌دلیل کشته‌شدن اخیر سربازان آمریکایی مجازات خواهد کرد. این ضربات ویرانگر تا زمانی که رئیس‌جمهور صلاح بداند ادامه خواهد یافت، اما گفت‌وگوها میان دو کشورمان همچنان در جریان است.»
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/77324" target="_blank">📅 23:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77323">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=O5jlRlFD87SmNx8vaqoyQlvOY-IU_-n4e466Cc0VIk2UjLvmONWttqdFF397Klg5o0vRjQ2m38zIRTKzQaojEipguSmkCu2rEmshmtSd_wG1S-foiDpPsxlcKir_xCWZTTdC4GnheCNP5KNYQqdbffoKADZMnGGLM_v8R0tXagsmy-Nr8-mtV61X0iARiueA-h_peEWL19vs-uCuAGZMf17kziRgVhf2z7fPB5AcHY8OJcGVpPnXOcfEUxzKDDnixqsyFZ3xHNJJc9_Atik5u0pRiIyVuDQ2gtqw0LZ9ry_BvQj7t-fKZafwt6NscYxka5C6PamNC51OjkDeuCQ_jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b98202fb7b.mp4?token=O5jlRlFD87SmNx8vaqoyQlvOY-IU_-n4e466Cc0VIk2UjLvmONWttqdFF397Klg5o0vRjQ2m38zIRTKzQaojEipguSmkCu2rEmshmtSd_wG1S-foiDpPsxlcKir_xCWZTTdC4GnheCNP5KNYQqdbffoKADZMnGGLM_v8R0tXagsmy-Nr8-mtV61X0iARiueA-h_peEWL19vs-uCuAGZMf17kziRgVhf2z7fPB5AcHY8OJcGVpPnXOcfEUxzKDDnixqsyFZ3xHNJJc9_Atik5u0pRiIyVuDQ2gtqw0LZ9ry_BvQj7t-fKZafwt6NscYxka5C6PamNC51OjkDeuCQ_jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد گودرزوند چگینی‌، نماینده شهرستان رودبار در مجلس شورای اسلامی می‌گوید که در تحولات اخیر، این ایران بوده که ابتدا توافق آتش‌بس میان ایران و آمریکا را نقض کرده است.
او در پاسخ به سوالی درباره توقف مذاکرات به دلیل نقض آتش‌بس گفت: نمی‌دانم گفتنش درست است یا نه اما اول ما حمله کردیم و بعد آنها سیریک را هدف قراردادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/77323" target="_blank">📅 21:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77322">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82071ea2df.mov?token=StXfaiAxhDxxeFIBXpjoDn-VQTmIS4p2490ippR1aO3X3rXwsmdj4P4X36g8k0bjy_Y1egnXSgSWgEHpEnOzuvEw4P89XL_aK9O9UKiX00h7OhZHqAErClHGdgonH6Aanril2B6hOp-1FXAGAjFrWLRfpzGAqXJ7O2UZLJ3SbbpG4xXyhyFVynyKzgJyWsTMbqWg37MhFFcvUP7livsGNn0fZ7CTmhO0E4Pux77C-UCdu8yawaoTIOgRUbyMQkOptTILVzb7Ij5lzBTfjOqiOS-2Tp-xenvxMIc7A0ROTz9EydmT4-m_KxSjA2xQnuFPmmTZRXmEbZPEyE5RN16xkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82071ea2df.mov?token=StXfaiAxhDxxeFIBXpjoDn-VQTmIS4p2490ippR1aO3X3rXwsmdj4P4X36g8k0bjy_Y1egnXSgSWgEHpEnOzuvEw4P89XL_aK9O9UKiX00h7OhZHqAErClHGdgonH6Aanril2B6hOp-1FXAGAjFrWLRfpzGAqXJ7O2UZLJ3SbbpG4xXyhyFVynyKzgJyWsTMbqWg37MhFFcvUP7livsGNn0fZ7CTmhO0E4Pux77C-UCdu8yawaoTIOgRUbyMQkOptTILVzb7Ij5lzBTfjOqiOS-2Tp-xenvxMIc7A0ROTz9EydmT4-m_KxSjA2xQnuFPmmTZRXmEbZPEyE5RN16xkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی: موشک‌هایی در آسمان ارومیه
آپدیت:
ارتش اردن شامگاه دوشنبه ۲۹ تیر حمله موشکی به این کشور را تایید و از رهگیری موشک‌های شلیک شده به سوی این کشور خبر داد و اعلام کرد که سه موشک از مبدا ایران که پادشاهی اردن را هدف قرار داده بودند، سرنگون کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77322" target="_blank">📅 21:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77321">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=bKrko_OyT1V9ni3MsEdBzyQRKCr6BjjLLc4U6YaVF2PCxsg1nf3QnSAPhN-015AMs8yriJfP0L84LUl030oG5DXczWACzFoUftHigfA3m8Cy5SHOLfSxLEcZMeJuxKqlVDnPTTugW8LCGjX5Xfnrp_mFovb3tAOLhTLNy-d944-SL18oHSuvVrI-YhNfRmKfn3UGKAjP9UCfcioGqEdNK3_Tpos5i6aVc-2yFr84Yv4aqp2_8Wi5M-1LL7XwH1TnGfjsDblzgxYRu__i1tEJBxg0LvGAJdJ2ZR6nNNecuIeZelDVB8FVwIZOMuYpltKfiplKQzHczfMST0jUPgZmPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb11afb901.mp4?token=bKrko_OyT1V9ni3MsEdBzyQRKCr6BjjLLc4U6YaVF2PCxsg1nf3QnSAPhN-015AMs8yriJfP0L84LUl030oG5DXczWACzFoUftHigfA3m8Cy5SHOLfSxLEcZMeJuxKqlVDnPTTugW8LCGjX5Xfnrp_mFovb3tAOLhTLNy-d944-SL18oHSuvVrI-YhNfRmKfn3UGKAjP9UCfcioGqEdNK3_Tpos5i6aVc-2yFr84Yv4aqp2_8Wi5M-1LL7XwH1TnGfjsDblzgxYRu__i1tEJBxg0LvGAJdJ2ZR6nNNecuIeZelDVB8FVwIZOMuYpltKfiplKQzHczfMST0jUPgZmPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی درباره پرتاب موشک از تبریز
ویدیوی بالا: شلیک موشک از [...] تبریز ساعت ۲۱:۲۴
صداشنیدم تبریز موشک زدن 9:25
میگن از [...] بلند شده
همین الان از [...] تبریز ۲ تا موشک فرستادن. ۲۱.۲۵
همین الان دوتا موشک از تبریز فرستادن  21:24
از تبریز دو تا موشک شلیک شد الان
صدای شلیک موشک ساعت ۲۱:۲۵ از تبریز
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/77321" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77320">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=WWcb_x3rEGtcXZ4QQ4JSkMW2og7Nqyanp0c5eBnd1KcueJK9AVoQasBtMKmctXZ6P7fRooqBmVQMxgMytJAZFZAqy_xa_T9Vdih1jaJRI_iK0a2HAfaWNjJyZA3JlWyImWghKmEda1-x_BX7Alk7NX97sd4E9hgNk1KcK0uvZERHDVjZqhcs1_sNqXlDk4eED6gjp92XVpzd_Qne5dlSmcPXxPPY_HyRwOvq6WKNksp1tA3zbXmkDR8MrZ7xxLa35G1Yr76dQPJcaGa2U3AviGHXr07G03E35j0YNv-0I4VzoqzklxGV4Q6QEqlCCRFLjoiaQMq3cBB2f3fUs5cQ6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3c8221ff7b.mp4?token=WWcb_x3rEGtcXZ4QQ4JSkMW2og7Nqyanp0c5eBnd1KcueJK9AVoQasBtMKmctXZ6P7fRooqBmVQMxgMytJAZFZAqy_xa_T9Vdih1jaJRI_iK0a2HAfaWNjJyZA3JlWyImWghKmEda1-x_BX7Alk7NX97sd4E9hgNk1KcK0uvZERHDVjZqhcs1_sNqXlDk4eED6gjp92XVpzd_Qne5dlSmcPXxPPY_HyRwOvq6WKNksp1tA3zbXmkDR8MrZ7xxLa35G1Yr76dQPJcaGa2U3AviGHXr07G03E35j0YNv-0I4VzoqzklxGV4Q6QEqlCCRFLjoiaQMq3cBB2f3fUs5cQ6jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تونل‌ها و پل‌های تخریب شده در حملات آمریکا، روی نقشه
در جریان حملات اخیر آمریکا که عمدتا بر جنوب ایران متمرکز شده، چند پل و یک تونل و یک ایستگاه انشعاب راه‌آهن در استان هرمزگان هدف قرار گرفت که خسارات جدی وارد کرد.
این پل‌ها و تونل در مسیرهای دسترسی استان هرمزگان به استان‌های فارس و کرمان قرار دارد و تخریب آنها باعث توقف تردد در مسیرهای بندرعباس به سمت شیراز و همچنین استان کرمان شد.
تونل شهید میرزایی در محدوده گلوگاه در مسیر بندرعباس به سمت حاجی آباد یک روز بعد از تخریب هر دو دهانه رفت و برگشت باز شد. در مسیرهای دیگر که پل‌ها هدف قرار گرفت، مسیرهای جانبی پل‌ها به طور موقت مورد استفاده قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/77320" target="_blank">📅 21:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77319">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Evk7K2Up29I3I2qaWA_cZKdePOaO6ELYUhXOD6OwYaaTxZ2P4GocmN-nF5P1hzT7lYfcImsAka3clpNF8pM7ID9PAa24en1XgZLIlt___ak8O3fVKmqU2d1bkGmlxbvWJA2cYL92AJDoyFrVPdBSd1W4kIzI0gVyQLLrCjYNlntSYivs49S86503azcNjvb1_6ABs7l1xmTD-HJ6u1ISx0YiNGO1LWOlyMawKKVp5sJUFFA7crmZeRQhrRX5m5TZwHqVPm9ZokLD_7rdHXLIjMutb4cqvNsIh9P_XNioaL_XsSfN4EzdNiKaMrzb-4K9Ap-kHAM0ZHYserO7sDAlsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت! این دستور به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک ارتش، و تمامی فرماندهان نظامی ابلاغ شده است.
رئیس‌جمهور دونالد جی. ترامپ
Every time Iran kills an American Soldier they will pay for that killing many times over! This directive has been passed on to Secretary of War, Pete Hegseth, Chairman of the Joint Chiefs of Staff, Daniel Caine, and every Leader in the Military. President DONALD J. TRUMP
realDonaldTrump
ترامپ در پستی دیگر نوشت:
بنیامین نتانیاهو تحت هیچ شرایطی، به هیچ شکل و طریقی، در ایالات متحده آمریکا بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را کشته و طی ۴۷ سال گذشته سربازان آمریکایی و دیگران را به قتل رسانده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که رؤسای‌جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!
رئیس‌جمهور دونالد جی. ترامپ
Benjamin Netanyahu will not be arrested, in any way, shape, or form, while in the United States of America. He is fighting against the Islamic Republic of Iran, which recently killed 52,000 innocent protestors, and has spent the last 47 years killing American Soldiers, and others. The only ones that should be arrested are the people that led Iran into this unprecedented SPIRAL OF DEATH AND DESTRUCTION, something that should have been dealt with years ago, by previous Presidents! President DONALD J. TRUMP
realDonaldTrump
پیش‌تر:
زهران ممدانی، شهردار نیویورک، اعلام کرد در حال بررسی امکان بازداشت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در صورت سفر به این شهر برای شرکت در مجمع عمومی سازمان ملل متحد در پاییز امسال است. ... @
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/77319" target="_blank">📅 20:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77318">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j8hIeU7rzukU6sc4mdsZAgn9TAcFSX_boiY0r8HKhvcuVL3Vr65rYXsDGiFL0Fq1eOxBVLnXGYyt6ityIorkaEEMKd461sVxRhHyLTVwWTm5WihV3048q3-CqXgghaO4AEhu0fEkmLExoWrPcf38MKwc50CbYZUFwq0HyKdUI_dMpff4b6hK-ZvgyEY9E0cYxwe7S2KUrk5Yx7uF6axW3gHyepP_Mw3JDW81IbNIu-GXHxRE7qu85CFjKi-ULpZqsuqEPUz7e5C2TGzoSXoCGJwf4HC-uMWVmnVxfoKYqNH_JKIM5tYvRvsgFhOMSmGqnTOjWTG9vzLYzs6lyc3QDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند پیام دریافتی تاییدنشده با مضمون: کارخانه نخ شهرستان خمین رو هدف قرار دادند.
هم‌زمان منابع حکومتی:
یک واحد صنعتی در حومه شهر خمین هدف حمله دشمن قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی در گفتگو با خبرگزاری صداوسیما: این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 364K · <a href="https://t.me/VahidOnline/77318" target="_blank">📅 19:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77317">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoYe4h7e8F0JUvYfMxh75nkDb0T-aUM-W6MMRzOFkZ6lKP1ZzAJ0X-YdrLcGyCuX9bvrR63OYyPK6QIdqak0bcqubi-xkNBHKyOTjbZJoUpyvZcndMnh7hrsbV9ggff4FlrqGHMG29xoAEI79VhpTuAvaLmce8ghBWh0lchM8iSMX8y6ucerWUYPYHDNFmoe5XfCGaQDaYBGd_E3mIssgm6WBe6mvMBV-6LfB52dH7EdiywmeffR73hji57qEc3fvRSME85estut1_7uEHOgdLOIYdtY17Rl-ijT1CKkDfWRHc9YbdtGEAHZ2bkgY9O2jmXY6aJb54Nd-pSP0BfZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژان نوئل بارو، وزیر خارجه فرانسه، در شبکه ایکس اعلام کرد که دو نفر از کارکنان سفارت این کشور یک‌شنبه از سوی نیروهای امنیتی جمهوری اسلامی مورد «تهدید و رفتار ارعاب‌آمیز شدید» قرار گرفتند.
بارو گفت این اقدام نقض آشکار مصونیت‌های دیپلماتیکی است که این افراد از آن برخوردارند.
وزیر خارجه فرانسه افزود: «آن‌ها بدون هیچ دلیلی برای چندین ساعت بازداشت بودند و مورد بازجویی قرار گرفتند و یکی از آن‌ها نیز مورد ضرب‌وشتم قرار گرفت.»
او گفت: «آنها سرانجام توانستند به سفارت برگردند و اکنون در آنجا در امنیت به سر می‌برند تا در ساعات آینده به فرانسه بازگردند.»
بارو تاکید کرد به عباس عراقچی، وزیر خارجه جمهوری اسلامی، اطلاع داده‌ که «این تعرض غیرقابل‌قبول به سلامت و امنیت کارکنان ما، بدون پیامد نخواهد ماند».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77317" target="_blank">📅 19:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77316">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZzjOA4BXCf6zsAMH19M7YYRvrWi-wvDm1Grw0p9FmVcLuGooGXp6nhTFWQbrgWdGHk8w6ZSDrHvaZpllZ8mIRTf7283bZsUpWQCw_82jrA9sNyaXrhxxOoliiCpqRv0hBPDfsshIoyreHltjX2wkKx_Ya_Itg6gz8lA3x8AetHM5k4whV-OXST6PaIMKET3qfFn7G0fJD8LCy2SdlRWMqdGeFMm2gSO58iVL0vM11Sv1DA6jk-gjueL45VcfbYdzvJPOswgF_6GFKapoKb3Pv5vtDCPia7aVkTDel0aEVaxgHxnzAALg2iJSA88GCyDCMwrSqnBZ_PNN7_EDBw6vjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس‌نیوز، ترجمه ماشین:
خبر فوری: پنتاگون تصویری از سرباز ایزابلا گونزالس، نظامی ۱۹ ساله آمریکایی اهل کارولتونِ تگزاس، منتشر کرده است که در حملات موشک‌های بالستیک و پهپادی ایران در آخر هفته کشته شد.
گونزالس در حال پشتیبانی از مأموریت آمریکا علیه گروه «دولت اسلامی» بود که هنگام کمک به دفاع در برابر حملات ورودی ایران کشته شد.
مرگ او در حالی رخ می‌دهد که درگیری‌ها در سراسر خاورمیانه همچنان شدت می‌گیرد.
نیروهای آمریکایی نهمین شب متوالی حملات تلافی‌جویانه علیه اهداف ایرانی را آغاز کردند؛ در حالی که دو کشور همچنان برای کنترل تنگه هرمز با یکدیگر می‌جنگند.
FoxNews
آپدیت:
خبر فوری: رئیس‌جمهور ترامپ در مراسم انتقال رسمی و با احترام پیکر دو سربازی که در حملات ایران در اردن کشته شدند، شرکت خواهد کرد. این مراسم فردا شب در پایگاه نیروی هوایی دوور برگزار می‌شود.
کارولین لیویت، سخنگوی کاخ سفید، در پستی در شبکه ایکس نوشت: «رئیس‌جمهور و تمامی اعضای کاخ سفید برای خانواده‌های آنان دعا می‌کنند.»
رئیس‌جمهور نیز در پستی در تروث سوشال نوشت: «هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین برابر خواهد پرداخت»؛ در حالی که آمریکا به کارزار نظامی خود در خاورمیانه ادامه می‌دهد.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/77316" target="_blank">📅 19:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77315">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6cac939191.mp4?token=vPPpkFhRPVBa4jm6GP_X33HhMSjHGfmt1NV44_GNhoo-DRnC97e_hyj_WprDtWDMqhQwl7m5M0j67XUAOlpSExs1Kk7xz004vbe2fJ4DWwS4xghRMpFiQCKh16iL_LIzieBsUqttooHAizzV431Nci35IyIPE_dpIxvoA_CN5v5HmvP1N63m0h5b1HhnyXNmJsJ29A_tjZr5mw7G4EgtumgEqer5oVpEJSi3BYdI8bkISLpOOxklVDxRM6a-Ck272djhQ8oHg8T6rngKyfUwRLCaUeHRWTucH0tpqIYwAzMzMV-_h-6od03S5dyqsPZNf7RcfWGAFQNnCdR9OLLECw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6cac939191.mp4?token=vPPpkFhRPVBa4jm6GP_X33HhMSjHGfmt1NV44_GNhoo-DRnC97e_hyj_WprDtWDMqhQwl7m5M0j67XUAOlpSExs1Kk7xz004vbe2fJ4DWwS4xghRMpFiQCKh16iL_LIzieBsUqttooHAizzV431Nci35IyIPE_dpIxvoA_CN5v5HmvP1N63m0h5b1HhnyXNmJsJ29A_tjZr5mw7G4EgtumgEqer5oVpEJSi3BYdI8bkISLpOOxklVDxRM6a-Ck272djhQ8oHg8T6rngKyfUwRLCaUeHRWTucH0tpqIYwAzMzMV-_h-6od03S5dyqsPZNf7RcfWGAFQNnCdR9OLLECw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پیام‌ها و تصاویر دریافتی: پرتاب موشک از حوالی لار در استان فارس، دوشنبه ۲۹ تیر حدود ساعت ۱۹'
هم‌زمان: پیام‌های دریافتی از صدور هشدار در بحرین
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/77315" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه‌های داخل ایران از پلمب چند کافه و رستوران در مرکز شهر تهران خبر داده‌اند.
براساس این گزارش‌ها جو کافه، ۱۴۰۱، سام‌کافه، دو بار، نووک و تئوری در خیابان‌های سنایی و ایرانشهر پلمب‌ شده‌اند.
وبسایت امتداد نوشت که به هریک از این کافه‌ها دلیل متفاوتی ارائه شده است از جمله «حجاب، داشتن ساندویچ در منو و صندلی در پیاده‌رو».
پلمب کافه‌ها و رستوران‌ها به دلایلی مثل حجاب یا موسیقی زنده سابقه طولانی دارد.
@
VahidHeadline
پیام دریافتی به همراه تصویر یک حکم:
چهارشنبه (چندروز پیش) به ۹ تا کافه داخل اکباتان فاز یک حکم پلمب دادند بدون هیچ توجیهی (فقط گفتن حجاب رعایت نشد) و همه کافه ها رو پلمب کردن.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/77313" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzz_wjuJsnbPhujg4EfNgN7JQxR0Ao9KIcgXqwYEuktWuzc4Gro2BfM7t0pgad9EYndbZGvHPeS95ODjg6oSFWVbu_3iI6hipZlIf0x_hyXpltzv30hnWftnssNB5802Qg78RXfd0AXmyywEh0JWiPFn_2n136GZJmc9dfkd0g8YGmeI_UhT6Cax_SgBwWRZ1i8WOEORmY2hFwZhgZlj344ABo7oZF8DnDmwtvIXsaJRU-RHVlwhSaIRX9i5FJsa1jXStey_iczwM1sP-_VlxQ9b6olqarQAzbflJ1mWCKrjm-bDhy129GrC0kq3v_yBGrOkn6y-k3_tgwHl7AixTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اسکندر مومنی»، وزیر کشور جمهوری اسلامی، در راس هیاتی از نمایندگان دستگاه‌های اجرایی، به دعوت همتای پاکستانی خود عازم اسلام‌آباد شد.
رسانه‌های ایران روز دوشنبه ۲۹تیر۱۴۰۵ گزارش دادند که هدف از این سفر، بررسی راه‌های توسعه همکاری‌های دوجانبه میان ایران و پاکستان است. جزییات بیشتری درباره برنامه دیدارها و محورهای مذاکرات وزیر کشور جمهوری اسلامی منتشر نشده است.
سفر مومنی به اسلام‌آباد در حالی انجام می‌شود که وزارت خارجه جمهوری اسلامی ساعاتی پیش دریافت پیشنهادهایی از سوی کشورهای میانجی برای توقف درگیری‌ها را تایید کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/77312" target="_blank">📅 18:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77311">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzjZhfw-1wg1dvHr94zAkDZNA-dM6fRHK68AiLIliNN-vsORFHvqfWlULY7eVLUrxz4Pqs8E1PgKwtNIJP3y_94oHhQOfXhrStHzlz9Ezfj1Wj-IGursCl1zIh3G5D2A5ISS1e_QJLKrZM71Szubs3xjgdCr8wjrLPlWySOR5lCS2VNFOYpyCYYEihCX0E9iOflyrPbLf1ZOBSpC1lxrOJPeD6eTRnY3CqeWJyCvQsARLBozZBvuw8r9DnYgcUydklYoeT3BkPSu3uozdfcUgtXDKHNjVS93rT094fzfzaajjekgMv7q-kDH1Asx7N_BjiHywRyxY2m6Evvjj5Gzlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، با انتقاد از سیاست‌های آمریکا در منطقه، با انتشار پستی در حساب «ایکس» خود نوشته است که واشینگتن هم‌زمان با ادعای تلاش برای توقف جنگ، به انتقال تجهیزات نظامی جدید به منطقه ادامه می‌دهد.
قالیباف در پیامی که دوشنبه ۲۹تیر۱۴۰۵ منتشر کرده، نوشته است: «آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگ‌اند.»
رییس مجلس شورای اسلامی همچنین با اشاره به آنچه «آمریکایی‌بازی‌ها» خواند، نوشته است: «آمریکایی‌ها روی هوش ما اندازه آی‌کیوی مختصر خودشان حساب کرده‌اند. جمهوری اسلامی در شناخت این رفتارها «به مرحله استاد تمامی رسیده و بر همین اساس برای مواجهه با آن آماده شده است.»
قالیباف در پایان نوشته که اقدامات باید موید ادعاها باشد، نه ناقض آن‌ها.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77311" target="_blank">📅 18:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77310">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCwh2GCZYIExJlWYpF051r3LSEZLJAUi4hj_2ngCrPEXMdtJaesXeOo9-SOLOtmLip0oU5kelMK6YKvlbSJPl2JEs77vrpl8pN4JLG_ql27xy26Lo1Ye3yGZR6ebuAh0MVWQ8V8PGmA-LYDjl6XNvoDtuP19xOguRR3Lx4Ju1tPXXtkQVAWFipjJAx3_TBnTS0kTyPT3dp5kiPPmpBd07seTJ-3oggrNUJdJuPPhU2pzYv3YMkimLhd23GdbIrgwe5MlgWTDrs2quM83cWAyCO1-TF6vhRtm1zpJ8kSJOfdVaISSFYtbNAtAy-cHYJoufM6nG_n-mMh5I7N0HdYAJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت کشتیرانی یونانی «دایناکام تنکرز» همزمان با بالا گرفتن درگیری‌ها میان ایران و آمریکا در منطقه اعلام کرد که دو نفتکش تحت مدیریت این شرکت روز دوشنبه هنگام عبور در آب‌های ساحلی عمان، هدف پرتابه‌هایی با منشأ نامشخص قرار گرفتند.
شرکت دایناکام اعلام کرد نفتکش «کاوومیلیز» با پرچم مالت هدف دو پرتابه قرار گرفت که باعث آتش‌سوزی در اتاق موتور آن شد و خدمه را ناچار به ترک کشتی کرد.
این شرکت در بیانیه‌ای گفت: «پس از فعال شدن سامانه اطفای حریق کشتی، ناخدا تصمیم گرفت کشتی را تخلیه کند.»
دایناکام افزود که تمامی خدمه توسط مقام‌های عمانی به سلامت پیدا شده و به ساحل منتقل شدند و این شرکت در تماس نزدیک با همه مقام‌های ذی‌ربط منطقه‌ای قرار دارد.
شرکت بریتانیایی مدیریت ریسک دریایی ونگارد اعلام کرد این حادثه زمانی رخ داد که کشتی در فاصله حدود هشت مایل دریایی در شمال‌غربی کُمزار عمان در حال عبور بود.
سازمان عملیات تجارت دریایی بریتانیا که پیش‌تر گزارش داده بود این کشتی دچار آتش‌سوزی شده است، اعلام کرد هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77310" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77308">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UewixnjbB1HFKYWr_gkWk_Fv4UFLdXgm6m3KudezKgdV6NsY_CgPPq80iBlxLIaQ27VUoXHi4y6vY6bzAMBxzDDpZzKI1rgj1sYdm3AXyAKAcB_iRK1p-SALR7qkgfJsmpVrCQM0lMwf-VdxkkOY93ihibOItMZCLnej3GrRBpuy2J6RZilsu4itnpdOasvSdmd1Oa9RaqAgi6DieIlU_6j_VxRG22FxmkBaEJcmR1pPQh7GNUmxmbiL2QS_MftBIYHxuI0fow1jfuChaXtNGuW6an2Wthvk_shVoV7S9g82bvOevilLnwy7PANtDTgKNlUiH4ZeZrIjK_WrQnpCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RLOErEZu8-AXluxyVbncO4aYtSGhnSlhi0fACFUtB-udzmyhNCqG1aXd5bQnIlek82cYDBKP8QP2hL-JFc5kq753QFVWnndaoYH6PMBDemAC3ZKXhZ16s-qA9L1jmkgQHISHhPQ_hpd2gBsvFXC_KDmFlXoXx_7jKSj-241NrDDBZn457CExbMLGJFG1czPjdBHaBePDl9CgUkq1VXw_h4Z4yj-Ohy_281zacW-0loqs3ma0Jq5dJLMX3I33isxScI9nPXoxDY1v9U22kOe9tO0-17-fPZ4P3eqBlEenLXhh_PC1ZreE_l8ItyZ6uTfPl5HFn0lPoooZgOIjAEp69Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرگزاری رویترز به نقل از یک مقام ارشد جمهوری اسلامی گزارش داد که میانجی‌ها پیشنهادی را به جمهوری اسلامی ارائه کرده‌اند که هدف آن کاهش تنش در جنگ با آمریکا است.
بر اساس این گزارش، این پیشنهاد شامل یک آتش‌بس ۱۰ روزه برای یافتن راه‌هایی جهت احیای تفاهم‌نامه میان جمهوری اسلامی و آمریکاست که ماه گذشته حاصل شده بود.
پیشتر سخنگوی وزارت خارجه جمهوری اسلامی اعلام کرد که پیشنهادهایی از طریق میانجی‌ها دریافت کرده است. این اظهارات در بحبوحه تنش‌های نظامی میان آمریکا و جمهوری اسلامی مطرح شده است.
اسماعیل بقائی روز دوشنبه در یک نشست خبری بدون ارائه جزئیات افزود: «اصل موضوع که در این روزها ایده‌هایی از سوی برخی میانجی‌ها به جمهوری اسلامی واصل شده، تأیید می‌شود.»
تنش‌های اخیر پس از حملات جمهوری اسلامی به کشتی‌های تجاری در تنگه هرمز آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77308" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77307">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چند پست بعدی مربوط به ساعت‌های گذشته هستند.</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/77307" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77305">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nWM-YNOuyWKnBCuhqHWXeuHT_XmJBb6gqsmWofWm_A68gtVG6e9FFXQvr9yr4U8HYUb_b1_2zNNYqf9WIpZ2r0mV_BjGz30Wnui2WtLeoeiy6Dak5zcwcQJdaxr6iAoTGmsDz1u1Nu2ExwH6dpK3h1XFZPaRJXQKsNv65wsYs0-uHf09c4BS6xJYF1CFruMK8tgkg4u0PADy6ThLEFFRDtIBZYA9qU2vzfJjWEjokXLKvfHbGN-EYf8BIFbVhBpRb9nb-Psc8GQCqqDuj0JrogOWQQq7fVeSaMcdlfh2m6ne_VGQIbC03wujxEzy0x6G0_jX8OUY9l55BwedgJXsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FxD-FWs5hGVh7eUQMztY7vR4-xWtiBXLUVhamyENUjiX1mHhO-fMcdYIO1P0y3zEHDd-IVdsxxYBoJRs5_iGfokr_aEFxl4L7vzuFvPbBYzD3EEka8udMKgieGXjthYt0j9X9KdWSqxmUXZATM1F5qNTEnlg74dOTgR294aB--F_LiQfgYuE2HRf42l_VgJP08HuTsi3SWyxZZV4lBcBuUrqjZWQ2sYiOsAwdmlT-zqtVyMfR2QtVdnoYQ3tOZuXOaIIy4q4PCBeyz9B5brxMOdz3HLJ-9kucs1X0CwFmNOFF_saXnaKO7x2fq0LsC5O9VVAzNrFSeLoH2Uv_WBjBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
اسمون شیراز الان
ساعت ۱۸:۲۵ از شیراز موشک شلیک شد
سلام وجید جان شلیک موشک از شیراز 18:17
درود وحید جان
۵دقیقه پیش از شیراز موشک زدن
[بعدش کلی تصویر مشابه دیگه اومد که دیگه پست نمی‌کنم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77305" target="_blank">📅 18:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CxBcdvgNtsGqsk433GdZx7H0dLBbwYRDqAyTz-EjcqRFhI_I-f1i4qyGceZP9tg-C15-hfEwSkYbTPi3tB3Q8eJ9DEeDcAWcy1O9L6EO6b9TDBZiSnOUvs9iqBKiZYWbjJbZ_3M0h_Vys79xHu6bbKG4EPvoG4GosffgIOlZ-JaODJZW5HTmJNuBr9JPtEuBhHamt2zGN4_49fNpkEpu9RP3vqj1ZC6JOscHRDgRDEKmw3KrnFJdD4fo5lkRlHYTFkfknH94YFQtWSrj1DmIu9XMkT6690yB5HR3wJcXUypT4lHybNpF1w6CiVIBOcLadWaua6hMMyjyrKcGIe-94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gl8WTlQ1FD0DkiRZLgrbg5JP3nqQBLG1ar-t66E0rO5FrqWvleRx9Q_FKXmJt6TWVTrYd9378vmqT_ZG6vXJVJD7aaMWcRyGF1Z9HyMakl84C_GrCO51KkRXeESwjZ25HOE-91aLEaQPlRs5RszsAbtyM_OeUHPEHahDlIpE7LUuI0loYDJrBeOkXBwV2PyMhhFY7BEjGA5qH9QaCpqRFN_NoZd871O11RDqkU33x5umEBgzO87E4eCYKhy7npZKT207L2CswGylMvhwhfwM9e8aIzj2VEp1ScIlCMonbQOl35ED5HB3gHz5HvxkUHytnJSDwqZoiWj77DoMGdt35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UJZKxXY4-jmtHWhmDA8DT2zXFysNQaCkz5hr44X8kj22SJ8V9MsHIpu_h7gWoK8a3XIuhR8DitiaJJ25uXR80J7RzB6vf7Vu1MDN_FZKd6aEwWAik8ckKEFLFNBbPznitFB8WFPW21Tewb1opxUdM1I0eKCSEMJ_5DJDlQOBoQNLoJnv3TonUCzSFBCDMpRhreQVTCNdo76xmKhG-E7VSXCoJH3hpmThoNr4vC9jIgEyb68gIcF1-c5LucmvraH9Da8LJ9CfkGG40uAkIJxcShCep2I4VA3WQtkhvd27gt3EpJIJyDgLskZNOtzqBYrvyvzYBV0nQdSuIdYZwfa5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/px10GieUcP1RTdGH8WTOW3EryAbeO3orqdVhTw9ymmBMKBOo2l7q2yplFTbS4hFqOU7_DzoZDK16olplfcKV4hpulhgil1iULiKl0Hg2huvGbD-ENa1mKiXZmv0A5C3x3lCCuhKaqFGsvYzjiEbFy-nAyF_x_QHrAv7ThRL1JkcTUpMPPpWFjC1j59464NEdFmHqYTnYVDvQi5_I-tgZiw6imtKgVZVft12aNEi-fUgTrLQeEyYkpl-Sw96E6RrT_qfEDX9boxkuTzuK4h7JrNnMsEimLyOBi3syJFdiiW6Ucx588yPPEvb-sOyW5e0wblLISZg7CA__NH0JcX2QTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر دریافتی از شیراز پس از دریافت پیام‌ها درباره 'شنیده شدن صدای انفجار سمت صنایع الکترونیک'
دوشنبه ۲۹ تیر حدود ساعت ۱۷:۱۰
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/77301" target="_blank">📅 18:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شیراز، پیام‌های دریافتی از ساعت ۱۷:۰۶
سلام ساعت ۱۷:۰۶ شیراز ،صنایع الکترونیک زدن صدا انفجار لرزوند
صاایران شیراز رو زد پنج دقیقه پیش
صدای انفجار و دود
صنایع شیراز
ساعت پنج
سلام وحید جان من شیراز هستم همین الان سمت تاچارا و معالی اباد صدای انفجار شدید اومد فکنم صنايع الکترونیک بود
سلام وحید جان. شیراز ما خونه‌مون نزدیک محدوده صنایع هست. ساعت ۵ صدای انفجار اومد. نمی‌دونم زدن یا موشک پرتاب کردن، ولی صدای انفجار بود.
سلام وحید جان ساعت ۱۷:۰۷ شیراز سمت صنایع صدا اومد
مطمئن نیستم افنجار بود یا دقیقا از کجا بود
ولی صدای بلندی بود
شیراز صنایع رو زدن  ۱۷.۱۶ دقیقه
وحید ساعت حدودا ۵:۱۵ عصر صنایع الکتریک شیراز صدای انفجار اومد دود بلند شد
شیراز صنایع رو زدن انفجار
صنایع الکترونیک شیراز و زدن
سلام شیراز صدای انفجار حدودای ۵وربع سمت صنایع
آپدیت:‌ منابع حکومتی
شنیده‌شدن صدای انفجار در شیراز
دقایقی پیش اهالی بخش‌هایی از شهر شیراز صدای انفجار از محدوده شمال غرب این شهر شنیدند.
خبرهای اولیه از حمله به یک نقطه در شهر در جریان این حملۀ هوایی دشمن حکایت دارد.
به گفته استانداری فارس، این حادثه هیچ گونه خسارت جانی درپی نداشته و تیم‌های ارزیاب در محل حادثه حضور یافته‌اند.
📍
میگن اینجاهاست:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/77300" target="_blank">📅 17:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wl9plXqufw2mPlfBFMPITDKOXQx537PuZFzMXMtU5uoviGwBuZCt8BshKyVlsH7HLRNX0s4JOMW-I52rtZjgTDFKvY6GoKAEFlTZEkZNlBD9GpwDEn5Bvs_pymiCvmsbCrvzWLlTKcH6KlT-6ci74t8Ctm2qRrXkXJcESNsMkX8p7UpKrgatdzdRZFszZ4XXvVR0GKJyW1IOFrB5EcIAK2rbROyvlUUAUEgonFgG6PZrn12rSbVzF8JEIeDrqA4dzx3yNlMUZbV7FVMda58tigtWMeUSeOev68kXPpP6fSSoo_1rF_-EHo4s6MwEg1WZY3BNj_1mfq-Fdk92FcQMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ها در کرمانشاه!
آپدیت: دو زلزله به بزرگی ۵٫۲ و ۵٫۷
📍
در عمق ۸ تا ۱۳ کیلومتری
کوزران
پیام‌های دریافتی:
الان کرمانشاه هستیم
کل خونه لرزید
زلزله بود
سلام وحید همین الان زلزله اومد تو ایلام
کامیاران سنندج زلزله هنوزم پس لرزه میاد
خیلی بد زلزله اومد
کرمانشاه
کل خونه لرزید
اینجا جوانرودزلزلە اومد شدید بود
سلام ایلام حدود ۱۰ ثانیه خیلی بد لرزید
سلام وحید، زلزله سنندجم حس شد
سلام وحید همین الان ایوان غرب زلزله آمد خیلی شدید بود
کرمانشاه زلزله اومد
درود کرمانشاه چند ثانیه به شدت لرزید کاملا حس شد
سلام وقتتون بخیر همین الان زلزله اومد استان همدان ملایر ۷:۱۵
زلزله نسبتاً شدیدی سمت کرمانشاه اومد
همدان هم ۳ الی ۴ ثانیه لرزید
سلام همین الان زمین لرزه اومد جوانرود استان کرمانشاه
سلام اقا وحید، ما پاوه هستیم تو کرمانشاه خیلی بد لرزیدیم معلوم نبود زلزله‌ بود یا چی. از شدت لرزش زیاد از خواب پریدیم. ساعت تقریبا ۷:۱۴ صبح
کرمانشاه اسلام اباد غرب زلزله شدید
سلام کرمانشاه خیلی شدید لرزید حدود ۶. ۷ ثانیه
سلام من کرمانشاهم حدود ۱۰ ثانیه شایدم کمی بیشتر کل خونه لرزید
آقا وحید ما مرز مهران هستیم، استان ایلام اینجا هم لرزید ساعت 7:15دقیقه
🔄
دوباره لرزیدددد
یا خداا بازم
دوباره اومد
دوباره ایوان داره می‌لرزه
وحید خیلی شدیده
وحید بازم داره زلزله میاد، ایلام
همین الان سروآباد استان کردستان لرزید
همین الان ۷:۱۹ هم پس لرزه‌ش اومد
پشت سر هم زلزله بالای 10 دیقه کامیاران داره پس لرزه
سلام وحید جان
مریوان دوبار اومد ۷:۱۴ و ۷:۱۹
وای دوباره اومد اینقد شدید بود
سلام وحید دوباره کرمانشاه لرزید خیلی شدید تر و طولانی تر
سلام ایلام دوباره لرزید
۳ ۴ دقیقه پیش پاوه لرزید
یه دقیقه پیشم لرزید و قوی‌تر بود
درود دو مرتبه پشت سر هم داره زلزله میاد هنوزم ادامه داره
خرم اباد ساعت 7/20
همدان دوباره بدتر لرزید
کرمانشاه زلزله بود
همین الان کرمانشاه زلزله خیلی قویی امد
کرمانشاه بازم زلزله شدید و طولانی
سلام آقا وحید کرمانشاه زلزله قبلی حس نکردیم الان ۷:۲۰ خیلی شدید و طولانی لرزید
ساعت ۷:۲۰ همدان لرزید
زلزله بود
اراک همین الان ۷:۲۰
چنننند ثانیه لرزید
سلام 7:20 اراک خونه لرزید در حد تکون شدید
همدان الان کاملا لرزید برای زلزله
قوی بود
وای ایلام بد لرزید
عجبيه اين زلزله خرم آباد حس شد
جالب اينه چقد ادامه داشت
سلام وحید خرم اباد لرزید خیلی کم لرزید
سلام،همین الان پشت سرهم دو بار زلزله اومد همه مون از خواب بیدار شدیم،جوانرود
نهاوندم لرزید خیلی عجیب بود
دوباره کرمانشاه زلزله،
از دفعه اول طولانی‌تر بود
۷:۱۸
زلزله شدید دوباره کرمانشاه
سلام وحیدجان همین الان اراک لرزید چهار پنج ثانیه شدید بود مثل گعواره خونه میلرزید چه خبره همه جای ایران میلرزه...
سلام وحید ..زلزله خفیف ساعت ۷:۲۰ همدان
همدان شدید لرزید چند سال بود چنین زلزله ایی نیومده بود
وحید جان سلام
اینجا الشتر، لرستان، ساعت 7:19صبح لرزید و قشنگ حس کردم لرزش زمین رو
سلام وحید جان ۷و۱۷دقیقه ب مدت۶ثانیه زلزله خیلی شدید از کرمانشاه همه رو از خواب بیدار کرد
کرمانشاه با زلزله بیدارشدیم
سلام وحید جان زلزله خیلی شدید همین الان کرمانشاه
سلام داداش کرمانشاه برای چند ثانیه وحشتناک لرزید
سلام بروجرد هفت و بیست دقیقه لرزید
سلام ساعت ۷:۲۱ همدان شهر همدان یه زلزله خفیف اومد
سلام بروجرد هم زلزله اومد
زلزله یا چیزی شبیه به آن در خرم آباد احساس شد
کرمانشاه زلزله وحشتناک اومد خیلی شدید بود
کرمانشاه زلزله آمد
منم قروه کردستانم
خونه یه ذره لرزید
آپدیت:
گزارش مقدماتی زمین‌لرزه
زلزله به بزرگی ۵.۲ در استان کرمانشاه
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی:
۰۷:۱۳:۱۷ ۱۴۰۵/۰۴/۲۹
طول جغرافیایی: ۴۶.۴۳
عرض جغرافیایی: ۳۴.۵۶
عمق زمین‌لرزه: ۸ کیلومتر
نزدیک‌ترین شهرها:
۱۷ کیلومتری كوزران (كرمانشاه)
۲۳ کیلومتری گهواره (كرمانشاه)
۲۶ کیلومتری روانسر (كرمانشاه)
نزدیکترین مراکز استان:
۶۵ کیلومتری كرمانشاه
۹۸ کیلومتری سنندج
كوزران کرمانشاه دوباره لرزید/ اینبار زلزله به بزرگی ۵.۷
مرکز لرزه‌نگاری کشوری مؤسسۀ ژئوفیزیک دانشگاه تهران:
محل وقوع: استان كرمانشاه - حوالی كوزران
تاریخ و زمان وقوع به وقت محلی: 1405/04/29 07:18:49
طول جغرافیایی: 46.48
عرض جغرافیایی: 34.57
عمق زمین‌لرزه: 13 کیلومتر
نزدیک‌ترین شهرها:
13 کیلومتری كوزران (كرمانشاه)
22 کیلومتری روانسر (كرمانشاه)
25 کیلومتری گهواره (كرمانشاه)
نزدیکترین مراکز استان:
61 کیلومتری كرمانشاه
94 کیلومتری سنندج
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 464K · <a href="https://t.me/VahidOnline/77299" target="_blank">📅 07:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aLM-HVWEhmZLw-j2Ta42ZGEHGqkRVL81r_edClUV3EZ5DyqQtH4LM-hnSKUr9v3ERA9fkcxpPKKYDEBIb2feAm9phAz7QcNZmc5hJF9kbz-4ntzBGt8GIyDsjZTd1ZT2glElfkwNoztIYi_TTKVUJbaUUSBaLubCeKwUD_eKJaiHPjWJYZ_YrvkotwWCO7DgcIH-xcQvn8KwRWWTHdAu0bMgs8xbm0pCHXbdRTfl_lBdqaU7wYh9lh8rNakqmIWIu1lTnMJ_PvFQPFK2UCqhV3IEXF7uKj-CxsQCNtif2evEd3YChUqasi6T7GLVe-qjyorhKeyLzpTwiLMUafKv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترجمه ماشین:
مارکو روبیو، وزیر خارجه آمریکا، روز یکشنبه گفت ایالات متحده آماده دیپلماسی با ایران است؛ هم‌زمان ارتش آمریکا نهمین شب پیاپی حملات خود را آغاز کرد.
روبیو پیش از عزیمت به مانیل، جایی که قرار است در اجلاس اتحادیه کشورهای جنوب شرق آسیا شرکت کند، به خبرنگاران گفت: «ایالات متحده همیشه برای رسیدن به یک راه‌حل دیپلماتیک آماده است. ما چندین بار با ایران تلاش کرده‌ایم و به تلاش خود ادامه خواهیم داد. اگر آن در باز شود، از دیدن آن خوشحال خواهیم شد.»
روبیو از ایران به‌دلیل حمله به کشتی‌ها و ایجاد مانع در تنگه هرمز انتقاد کرد. تفاهم‌نامه‌ای که آمریکا و ایران در ماه ژوئن به آن دست یافتند، با هدف گسترش آتش‌بس و ازسرگیری تردد در این آبراه کلیدی تنظیم شده بود.
روبیو گفت: «اگر آن‌ها مفاد این تفاهم‌نامه را نقض کنند، نمی‌توانند انتظار داشته باشند که این تفاهم‌نامه همچنان پابرجا بماند.» او افزود: «آن‌ها همچنان پیام می‌فرستند که می‌خواهند گفت‌وگو کنند و مذاکره کنند، اما آنچه ما به آن پاسخ می‌دهیم رفتارشان است، و رفتارشان این است که موشک‌ها و پهپادهایی را علیه کشتی‌ها، از جمله همین امشب، پرتاب می‌کنند.»
کیت ماهر، خبرنگار سی‌ان‌ان، از روبیو پرسید اگر تلاش‌های دیپلماتیک شکست بخورد چه خواهد شد. روبیو پاسخ داد: «فکر نمی‌کنم برای ایران خوب باشد. منظورم این است که اقتصاد ایران از هم پاشیده است.»
CNN
مارکو روبیو، وزیر خارجه آمریکا، گفت حادثه‌ای که روز شنبه در شمال عراق به کشته‌شدن یک نظامی آمریکایی انجامید، یک «سانحه» بود و این نظامی هنگام خنثی‌سازی یک پهپاد سرنگون‌شده ایرانی آسیب دید.
روبیو روز یکشنبه به خبرنگاران گفت: «هیچ کاری که ارتش انجام می‌دهد بی‌خطر نیست. همه این کارها ذاتاً خطرناک‌اند و ما فقط سپاسگزاریم که چنین آمریکایی‌های قهرمانی با پوشیدن یونیفرم، در خدمت کشورمان هستند.»
روبیو درباره حمله ایران در روز جمعه در اردن که به کشته‌شدن دو نظامی آمریکایی انجامید، گفت: «یک موشک عبور کرد. تقریباً همه موشک‌ها را سرنگون کردیم. یکی از آن‌ها رد شد... این دلخراش است.»
روبیو گفت که «برای خانواده‌هایشان و آمرزش روحشان دعا می‌کند.»
تعداد نظامیان آمریکایی که در جنگ نزدیک به پنج‌ماهه با ایران کشته شده‌اند، اکنون به ۱۷ نفر رسیده است.
CNN
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/77298" target="_blank">📅 07:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌های دریافتی:
همین الان چابهار 5 بار زد 5:50
باز داره چابهار رو میزنه  لرزش ها وحشتناکه
الان دوبار صدا اومد ساعت ۵:۴۸
5:49 دیقه کنارک صدای انفجار اومد
هنوزم صدای هواپیما میاد
به عنوان آخرین مقصد اینجا رو میزنه
کنارک صدای جنگنده و انفجار هم اکنون
۲انفجا کنارک نیروی هوایی ۵.۴۹
صدای هواپیما بازم شنیده میشهه چابهار
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77297" target="_blank">📅 05:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=NNZrbtqW5nfmswMC7vM12s21nyQ8peO6yD7z9a3Ea6TKUoIGKLHOF4UlBt6p_RalNBWvCQ0kIiuo54SVUpW9bG3NEgQYQ1DIKO9_Q9VEv_51HFvLFyLbBV2GYNV_YDsOm4u9mHZywyeluemz1aavsN9RDN-HBENe3GStcTzkpZ6DBa4Ts2W0qtAn61UNR1NvAFlOz-TEsJBkcWP5B6gp85ma-kgNugGX8quZnLlF2Z8RyfnxNGbqm1L0fB5FCOd9-vpaCqQ5Np9yPXdD5e2zb4HCfmFvQxF2zfuUOnUrkVuhb8c6qRx_jJ2ZkaoQSbQo1EfNG8mU7YAyR2phG6HjKA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f2ddbd450c.mp4?token=NNZrbtqW5nfmswMC7vM12s21nyQ8peO6yD7z9a3Ea6TKUoIGKLHOF4UlBt6p_RalNBWvCQ0kIiuo54SVUpW9bG3NEgQYQ1DIKO9_Q9VEv_51HFvLFyLbBV2GYNV_YDsOm4u9mHZywyeluemz1aavsN9RDN-HBENe3GStcTzkpZ6DBa4Ts2W0qtAn61UNR1NvAFlOz-TEsJBkcWP5B6gp85ma-kgNugGX8quZnLlF2Z8RyfnxNGbqm1L0fB5FCOd9-vpaCqQ5Np9yPXdD5e2zb4HCfmFvQxF2zfuUOnUrkVuhb8c6qRx_jJ2ZkaoQSbQo1EfNG8mU7YAyR2phG6HjKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام موج حملات آخر هفته علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) نهمین شب پیاپی حملات علیه ایران را روز ۱۹ ژوئیه، ساعت ۱۰ شب به وقت شرق آمریکا، با موفقیت به پایان رساند.
تجهیزات و نیروهای سنتکام مراکز فرماندهی نظامی ایران، مواضع پدافند هوایی و نظارت ساحلی، توانمندی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و شبکه‌های ارتباطی را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی عبوری از تنگه هرمز بیش از پیش کاهش یابد.
ارتش آمریکا به دستور فرمانده کل قوا، ایران را پاسخ‌گو می‌کند. نیروهای سنتکام همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده باقی می‌مانند.
CENTCOM
منابع حکومتی:
اطلاعیه شماره ۳۰/ دو نفتکش که قصد تردد در مسیر ناایمن تنگه هرمز را داشتند منفجر شدند
روابط عمومی سپاه:
🔹
ملت قهرمان و بپاخاسته ایران اسلامی؛ اواخر شب گذشته دو فروند نفتکش متخلف که به تحریک و اجبار ارتش کودک کوش آمریکا قصد ورود و خروج از مسیر ناایمن و حادثه‌ساز جنوب تنگه هرمز را داشتند منفجر شده و از حرکت باز ماندند.
🔹
اینجا سرزمین ماست و دخالت ارتش تروریستی آمریکا از هزاران کیلومتر آن طرف‌تر هیچ وجاهت قانونی ندارد و با قطعیت با آن برخورد خواهد شد و تا زمانی که شرارت های آمریکا در منطقه ادامه یابد این معبر برای عبور کود شیمیایی و حتی یک قطر نفت و گاز امنیت ندارد.
🔹
ارتش متجاوز، آماده عملیات تنبیه ما به خاطر این تخلف غیرقانونی باشد.
قدردانی سپاه از اطلاعات مردم اردن؛ هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه هدف موشک بالستیک قرار گرفتند
روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
إِنْ نَکَثُوا أَیْمانَهُمْ مِنْ بَعْدِ عَهْدِهِمْ وَ طَعَنُوا فی دینِکُمْ فَقاتِلُوا أَئِمَّةَ الْکُفْرِ إِنَّهُمْ لا أَیْمانَ لَهُمْ لَعَلَّهُمْ یَنْتَهُونَ
🔺
مردم شریف و ارتشیان مجاهد اردن، با تشکر از همکاری صمیمانه و اطلاعات دقیق شما که موجب هدفگیری دقیق رزمندگان اسلام و انهدام ۲۰ سوله محل استقرار نیروهای ارتش کودک کش آمریکا در منطقه الازرق و کشته شدن ده‌ها نیروی تروریست آمریکایی شد.
🔺
رزمندگان نیروی هوافضای سپاه در موج ۲۱ عملیات نصر ۲ با رمز مبارک یا رقیه (س) و تقدیم به دختر بچه های شهید جنگ تحمیلی سوم، با کمک شما، هواپیماهای بزرگ ترابری C17 و هواپیماهای فرمانده کنترل P8 ارتش متجاوز امریکا در فرودگاه عقبه را هدف حمله موشک های بالستیک قرار داده و به تعدادی از آنهاخسارت سنگین وارد کردند.
🔺
نظامیان متجاوز آمریکا که طی چند دهه اخیر به بیش از ده کشور اسلامی حمله کرده و میلیون ها مسلمان را کشته اند و حامی اصلی رژیم کودکش صهیونیستی در کشتار عظیم مردم غزه و ویران کردن کرانه باختری هستند، از لحاظ شرعی مهدور الدم هستند و هر مسلمانی، هرجا دستش رسید باید این قاتلان وحشی را بکشد.
🔺
با تشکر مجدد از تلاش‌ها و همکاری‌های شما که با انجام تکلیف شرعی راه را برای آزادی قدس شریف هموار می‌کنید.
«إِنْ تَنْصُرُوا اللَّهَ یَنْصُرْکُمْ وَ یُثَبِّتْ أَقْدَامَکُمْ»
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/77296" target="_blank">📅 05:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=L2FNY0DlCVmmO6jKd8GPKbccjbIH3rtyjcOjLUfDNm4_rSKp5_Ed8-u3_ur-lfPwxWi2orsQf5hwHTnMET-SQ04ojiBnvvm3So1mRI2u66Y5EH0aZGYhUOSa9RLC5xOO28PoOrpVvzPFyQbs8hJ7jiCT_r2CZKYkRhKUDb0wk2VBfjEBI85a5nW11uChasNQU5BpF6Zx6bLVWbjDEJ0Rx_-LPcE1oH8AE3SwSi2zrJ3PeNJ7TnPuD92n4Ezc8Od0hr53ddhVaglmVEq6Sibbsm_81jF3R5w0tcJuCeTgwruEh828k0bjpexBcguM5H16528RbFXWp9FXLEvsTW8pNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/94bb518d25.mp4?token=L2FNY0DlCVmmO6jKd8GPKbccjbIH3rtyjcOjLUfDNm4_rSKp5_Ed8-u3_ur-lfPwxWi2orsQf5hwHTnMET-SQ04ojiBnvvm3So1mRI2u66Y5EH0aZGYhUOSa9RLC5xOO28PoOrpVvzPFyQbs8hJ7jiCT_r2CZKYkRhKUDb0wk2VBfjEBI85a5nW11uChasNQU5BpF6Zx6bLVWbjDEJ0Rx_-LPcE1oH8AE3SwSi2zrJ3PeNJ7TnPuD92n4Ezc8Od0hr53ddhVaglmVEq6Sibbsm_81jF3R5w0tcJuCeTgwruEh828k0bjpexBcguM5H16528RbFXWp9FXLEvsTW8pNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم
مصاحبه ترامپ بعد از مراسم فینال جام جهانی، ترجمه ماشین:
ترامپ:
به کشورمان افتخار می‌کنیم. به کاری که همه انجام دادند بسیار افتخار می‌کنیم. به جیانی اینفانتینو و تمام کارکنانش برای کار باورنکردنی‌شان تبریک می‌گوییم.
این یکی از بزرگ‌ترین رویدادها از هر نوعی بود که تاکنون برگزار شده است. بنابراین خیلی خوشحالیم که این‌قدر موفق بود. مردم از سراسر جهان آمدند و کشورمان را دوست داشتند.
می‌دانید، این رویداد کشورمان را از زاویه‌ای متفاوت به نمایش گذاشت.
اتفاق فوق‌العاده‌ای بود؛ یک رویداد عالی بود و خوشحالم که همه شما از آن لذت بردید.
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
این را شما می‌گویید؟
خبرنگار:
شما گفتید آرژانتین باخت.
ترامپ:
نه، چنین چیزی نگفتم. فکر می‌کنم هر دو خوب بازی کردند. من می‌گویم اسپانیا واقعاً بهتر بازی کرد.
هر دو خوب بازی کردند. منظورم این است که به فینال رسیدند و واقعاً بسیار هیجان‌انگیز بود. به نظر می‌رسید اسپانیا مسلط بود، اما مسابقه بسیار نزدیک بود. بنابراین عالی بود؛ یک رویداد عالی بود، بله.
خبرنگار:
[پرسش خبرنگار نامفهوم است.]
ترامپ:
خب، احساس بسیار بدی داریم. اما می‌دانید، آن افراد بزرگ، آن میهن‌پرستان بزرگ، در تمام این مدت جنگیدند تا ایران نتواند سلاح هسته‌ای داشته باشد.
ایران به‌شدت، به‌شدت آسیب دیده است. تقریباً همه توان نظامی‌اش را از دست داده است. چیز بسیار کمی برای آن‌ها باقی مانده. تعدادی موشک و پهپاد دارند. مقداری توان تولید هم دارند، اما زیاد نیست.
ما تنگه هرمز را در کنترل داریم. آن‌ها هیچ‌چیز را کنترل نمی‌کنند. پس خواهیم دید چه اتفاقی می‌افتد.
امشب دوباره ضربه بسیار سختی به آن‌ها زدیم و این کار را به احترام آن میهن‌پرستان بزرگی انجام دادیم که احتمالاً سه نفرند، نه دو نفر.
خبرنگار:
پیامدهای دخالت چین در انتخابات آمریکا چه خواهد بود؟
ترامپ:
بعداً درباره‌اش صحبت خواهیم کرد. با آن‌ها گفت‌وگو می‌کنیم، مطمئنم.
خبرنگار:
می‌توانم بپرسم آیا با کارنی، نخست‌وزیر کانادا، گفت‌وگو کردید؟
ترامپ:
بله، کردم. بله، صحبت کردم.
خبرنگار:
گفت‌وگو چطور پیش رفت؟
ترامپ:
خوب پیش رفت. اما به او گفتم باید جلوی ورود دود این آتش‌سوزی‌ها را بگیرید، چون هوای ما را مسموم می‌کند. هوای ما مسموم شده است.
من رابطه خوبی با مارک کارنی دارم. اما می‌دانید، باید آتش‌سوزی‌های آنجا را متوقف کنیم. اگر بتوانیم به آن‌ها کمک کنیم، کمک می‌کنیم. اما شاید باید بابت خسارت‌ها چیزی به ما بپردازند، یا شاید ما باید تعرفه‌ای وضع کنیم.
وضعیت وحشتناک بود. کسب‌وکارها تعطیل می‌شدند؛ به‌ویژه در میشیگان. اگر به دیترویت در میشیگان نگاه کنید، مجبور شدند همه‌چیز را تعطیل کنند. مجبور شدند کارخانه‌های خودروسازی و بسیاری مراکز دیگر را ببندند.
من هرگز به یاد ندارم چنین اتفاقی افتاده باشد. در چهار یا پنج سال گذشته این وضعیت کم‌کم آغاز شد. پیش از آن هرگز به یاد ندارم چنین اتفاقی افتاده باشد.
خبرنگار:
آیا فرصت کردید با نخست‌وزیر اسپانیا هم صحبت کنید؟
ترامپ:
بله. با مقام‌های اسپانیا صحبت کردم و بابت داشتن چنین تیم بزرگی به آن‌ها تبریک گفتم. با افراد زیادی صحبت کردم.
خبرنگار:
پیش‌تر با اسپانیا تنش داشتید.
ترامپ:
نه، هیچ تنشی ندارم. با هیچ‌کس تنشی ندارم.
خبرنگار:
[پرسش خبرنگار درباره اسپانیا نامفهوم است.]
ترامپ:
خب، [نامفهوم]. می‌دانید، توانایی زیادی دارد. اما تا جایی که می‌دانم، ظرف حدود یک ماه [نامفهوم] تا آن را به حداکثر برسانند. بنابراین قرار است آن را بفرستند و به حداکثر برسانند. فکر می‌کنم حدود یک ماه دیگر.
خبرنگار:
آقای رئیس‌جمهور، آیا با نخست‌وزیر کانادا صحبت کردید؟
ترامپ:
بله. همین حالا داشتم پاسخ می‌دادم. درباره‌اش با او صحبت کردم. گفتم: «باید جلویش را بگیرید.»
مسئله در اصل مدیریت جنگل‌هاست و آن‌ها باید بدانند چگونه این کار را انجام دهند. اگر چهار یا پنج سال به عقب برگردید، به یاد ندارم هرگز چنین مشکلی داشته باشیم. اما حالا این مشکل را داریم.
فردی در محل:
از این طرف بیایید، آقای رئیس‌جمهور.
خبرنگار:
شما گفتید جنگ را ظرف چهار یا پنج هفته پایان می‌دهید.
ترامپ:
[آغاز پاسخ نامفهوم است.] کاری که اکنون انجام می‌دهیم بسیار بزرگ‌تر است. قبلاً کار محدودتری انجام می‌دادیم؛ می‌خواستیم مانع دستیابی آن‌ها به توانایی خاصی شویم. حالا داریم کار را تمام می‌کنیم.
بنابراین واقعاً همان موضوع قبلی نیست. کاری که اکنون می‌کنیم این است که هرگونه امکان دستیابی آن‌ها به موشک هسته‌ای را از بین می‌بریم.
اگر نگاه کنید، پس از یک هفته و نیم ــ نه چهار هفته؛ یک هفته و نیم یا دو هفته ــ جلویشان را گرفتیم؛ احتمالاً... اما نمی‌خواهم از واژهٔ «احتمالاً» استفاده کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77295" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vmbMbbEYyDSt8tuDcS-Ve7JzrRswaoEwrYflPz73D83Ry_Bq-eLQPVSOGGkrQR0oZxnqXwdU5Kc4WbU3obhweoMB37X8rHRojnxwQpGfPBF40Epfg6UaLk0RDQgkyPBaTdpAjbB-0iRXS27V6IdBo7T-7_iRN50JPIx1ohbTKDUeNu9XFI0BphcKCqLqElMwLtQ8cN60gg3CIrd7ErqVG1ify8DoCl9EOqnQSxEq2VKdeV4u6CjC4tD6dNYb0-0BwXBPBv7NjY5muJ-HJAywCaVToYcIfT9NE2g7Mr-wnB9Rsudk0nW08L8hseQy15OXFUu5RT-LeRw-aiDaIvVAdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: تصویر منتشرشده با شرح کنارک
پیام‌های دریافتی:
بازم یه انفجار چابهار ۳:۵۱
کنارک صدای انفجار(دور بود)
و همینطور صدای جنگنده
نیم ساعته از بعد جام جهانی داره چابهار و کنارک رو سنگین می زنه. جاهای مختلفه و نمی دونم کجاها بوده فعلا
دوباره خیلی سنگین زد
چابهار ۳:۵۱ صدا اومد
همین الان چابهار دوبار زد 3:51
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/77294" target="_blank">📅 03:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFsSUUiW-wY4NkDWBjQKtmUMnjBBWt5h1El_JzEnP5w1xQijLAxtl8Doii74ICgQoW_OGTHgkYt88m-4j0VK9HSTFZezgTCieTIxdLSv_2tSLMPGSa1IYccRxvfDkV7KYL27PZ_mXc62fVoYVntZv0118Nu2hSK6WfZ2_0Lwp6LKAey8--6aBIqB7GmAVhZMuGIlv-vYqP0PaWImoAW4HCiJXt1fUY61aX4oeGahZ5BFd5XbZgTYdCGPzqHA8kuVhqy0JvoO-c6lqnLO2gH5kLlbOFnIwvHPp5WdZOAYwoMVLtlWI893WLFpXOWP92BhbUs-XVn0m0PMa4ODlH0E1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با آغاز نهمین شب حملات متوالی آمریکا به مواضع نظامی در ایران، بامداد یکشنبه، فارس از اصابت چند موشک و شنیده‌شدن صدای انفجارها در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر و بندر خمینی در خوزستان خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/77293" target="_blank">📅 03:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیام‌های دریافتی:
سپاه خورموج توی استان بوشهر رو زدن برق ی منطقه هم رفته
سلام وحید  ساعت ۳:۰۷ دقیقه
خورموج پنج انفجار شدید
همین الان خورموج پادگان سپاه زدن برق هم قطع شد
همین الان سپاه خورموج زدن ساختمانش کلا صااف زمین شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77292" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پیام‌های دریافتی:
چندین صدای انفجار پیاپی، سیریک.
ساعت سه و پنج دقیقه بامداد شهر سیریک ده ها انفجار بسیار سنگین
سه تا آخری خیلی بد زد موجش زیاد بود
احتمالا اسکله بوده باشه
۳:۰۵ تا ۳:۱۰ چند انفجار سمت سیریک (طاهرویی) خیلی شدید
سیریک صدای انفجار پشت سرهم خیلی بلند، صدای جنگنده‌ها هم میاد
بندر عباس ساعت 3:11 دقیقه چند انفجار پشت سر هم و طولانی رخ داد و تا دو دقیقه ادامه داشت
بندر جاسک همین الان دوتا صدا اومد
بندر جاسک دوباره صدا اومد صدا خیلی وحشتناک بود
سیریک حدود ۸ انفجار شدید شایدم بیشتر  شیشه های اتاقم نزدیک بود بشکنن
جاسک جنگنده بالا سرمونه
۳تا انفجار تا الان
بیشتر از ۳تا شده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77291" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SehRc8Ge4ZPoDpnp3NHeRf_4mEXvAFlzbjYgl5SmYEmHnOBr-sV7T9fliiSAsIRKLWYlAjZKujfDohJfajuoFtaau50Z2mbUkbwn-0s47SPXcw-KOw8qUnnK4zoNR2GOi228Zjkr8IbN_WcNQjRLwPB-dpBsg62W2BZDjjVpPJtc1_pxdN7NBajIbiKTxKPLhN_OB7MHyAtKbtVc7nCPIu_0Wxw8Yw0fX8f9dI8MP0_XgFEBlZoGHcrv1TmFKKUTwT20wV-l7NTwWVUOyCiPtuSJwJcd-smqG6mESzCk3gWg3TLuqo2KlHJPQkftb1h6m9y7GqYLFlUOHAmLDLR-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی با شرح: 'سربندر ("بندر امام خمینی") ساعت ۲:۴۰ دوشنبه ۲۹ تیر'
Vahid
دوباره زد
سربندر خوزستان 3:08 دو صدای انفجار و لرزش شدید خونه
وحید جان دوباره سربندر دوبار محکم زدن
وحید سربندر رو باز هم زد
تک انفجار، ولی خیلی سنگین ۳:۰۹
۳.۰۸ دقیقه سربندرو بازم زدن
اقا وحید ماهشهر دوباره زد
شیشه اتاقم لرزید این بار
صدای انفجار قبلی رو فقط شنیدم
خود ماهشهرم، سربندر نیستم ۳:۰۹
وحید ماهشهر یکی سنگین زد
سربندر دوباره زد صداش بیشتر از قبلی بودد
ماهشهر دوباره شدید ۳:۸ دقیقه
ماهشهر رو دوباره زد ۳:۰۸
همین الان باز ماهشهر دو انفجار شدید
سربندر ساعت ٣:٠٩ دقیقه دوباره انفجار شدید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/77290" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=Yj-iVRs99e4NiKT5WzOTf0a5Dx1PyTXowtlTVynWA4jJV8HTuoE-UynbO9ta3phRE11JHBDJ9xyFm4crs1bHsnKGLku_by2mR-hEIhi0hpes_dNH_yYv-GCARFGcTF_llv71HSx7G01cDdQoa84WDDAp2x4Sva38WDAQ9MZa8kgqyZApk00aXjAEjWm6KNOyGpPWtMTC4VIRoZJrjNMXbjWJ5QEFGcFG7x65QRS8PyNjVElWcdZHQXko7PnoZnleDEsTZtgyNNat7p_h018Bdl0oi_qWbL2O5MZavANl8xqiuYTJx_ziWgXKqOM0xtGNXrWSL4R2TcAQo6BdMEnkdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/baefb3737a.mp4?token=Yj-iVRs99e4NiKT5WzOTf0a5Dx1PyTXowtlTVynWA4jJV8HTuoE-UynbO9ta3phRE11JHBDJ9xyFm4crs1bHsnKGLku_by2mR-hEIhi0hpes_dNH_yYv-GCARFGcTF_llv71HSx7G01cDdQoa84WDDAp2x4Sva38WDAQ9MZa8kgqyZApk00aXjAEjWm6KNOyGpPWtMTC4VIRoZJrjNMXbjWJ5QEFGcFG7x65QRS8PyNjVElWcdZHQXko7PnoZnleDEsTZtgyNNat7p_h018Bdl0oi_qWbL2O5MZavANl8xqiuYTJx_ziWgXKqOM0xtGNXrWSL4R2TcAQo6BdMEnkdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'سایت موشکی تبریز'
دوشنبه ۲۹ تیر
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/77289" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77288">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=W1Msy-Ydd_yqOICgVTLzXwXFCREOhthvVaCT48rOh2G0CHThWZWkQccX39GJV7RYEGF8tIydBjcBI4Py0AoG9u-pA53L58lH9dsQnbX5RN4nmGYIv65-AniWXf2Ung02rGs_6pjEFOTJRixwpjPDlW9ResUsi27nWxGPy-OQSgNOvQPdWUEEoCcpiFPyxDMc-394mBKQLkF1KspM9cQRmGMTZDgeEe4OvjKGX_h4FQyLP6llnV7Gg6v1gXuHO9RE93aP8KiR3MVPvbROfw3xdrWikwa4pbcyaVgJgoI8l2zCmMo3A1yVotRnzDaCNJX6zfybRf10B7U_6IkkQDTOqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/028b9087f7.mp4?token=W1Msy-Ydd_yqOICgVTLzXwXFCREOhthvVaCT48rOh2G0CHThWZWkQccX39GJV7RYEGF8tIydBjcBI4Py0AoG9u-pA53L58lH9dsQnbX5RN4nmGYIv65-AniWXf2Ung02rGs_6pjEFOTJRixwpjPDlW9ResUsi27nWxGPy-OQSgNOvQPdWUEEoCcpiFPyxDMc-394mBKQLkF1KspM9cQRmGMTZDgeEe4OvjKGX_h4FQyLP6llnV7Gg6v1gXuHO9RE93aP8KiR3MVPvbROfw3xdrWikwa4pbcyaVgJgoI8l2zCmMo3A1yVotRnzDaCNJX6zfybRf10B7U_6IkkQDTOqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی با شرح: 'انفجار در
#تبریز
'
بنا بر پیام‌های دریافتی از شهروندان حدود ساعت ۲:۳۷ دوشنبه ۲۹ تیر صدای چند انفجار در تبریز شنیده شده.
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/77288" target="_blank">📅 03:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77287">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LCcm_h8Aph90prE_VDS_lCm6Lovu7OaGKvTxS5ssTtMz5SaK-laWNkZVOWlsbdoGQvZ5xeE2R7WWacu1Xz727Tb2rp35Ye3c0D3Sk8k6icq16pbmbmX4xm_YqZukgND7k1z_51xOdRxPqg-C1yPTWDzyyauS3QhDa4NRwzR2QCBfLDXmSPx7-ncyDkz3ScUwsX0Wc70df_qBNJqimCNy7wXdPJuBp4rhlXdNah9z28hDnsJvAWwRv58EvA4Af2cDN-TVP9XcJOpxXf2epK784zm96CHm6sCNiElxFYb14N0GlxUEsAWS7gfB2HZRgoWaYQ0kAhI-bxxrH-6de6qcbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
سنتکام امروز ساعت ۷ عصر به وقت شرق آمریکا، برای نهمین شب متوالی موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات به تضعیف بیشتر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز به کار می‌روند، ادامه خواهد داد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77287" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77286">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام‌های دریافتی:
۵ ۶ تا همین الان کنارک
خیلی خیلی شدید بود هنوز داریم میلرزیم
۳ تا دیگه همین الان
چابهار الان صدا انفجار پی در پی اومد
2.43
چابهار 4تا صدای انفجار شنیده شد دور بودن
چابهارو الان زدن ۲:۴۴
چابهار صدای انفجار اومد
کنارک 2:42 سه انفجار پشت سرهم
کنارک ۳ تا انفجار
سلام بازم دوتا قدای انفجار ساعت ۲.۴۵ در کنارک
خیلی بد داره میزنه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/77286" target="_blank">📅 02:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77285">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پیام‌های دریافتی:
ماهشهر صدای انفجار اومد میگن سربندره
سلام وحید جان
ساعت 02:40 سربندر صدای وحشتناکی اومد.
آقا وحید ماهشهر همین الان چندتا صدای مهیب و لرزش شیشه ها رو داشتیم
همین الان ماهشهر رو زدن
سربندر ۲:۴۱ انفجار شدید
سربندر دو سه تا پشت سرهم یکیش خیلی نزدیک بود یعنی پدافند رو زدن
چون تازه دود دیدم از سمت سایت پدافندی  نزدیک خونمونه
وحید جان همین الان سربندر خوزستان  شدید زد
وحید جان 2:40 سربندر انفجار بسیار قوی
بندر امام خمینی، خوزستان
من ماهشرم، هیچ صدایی نشنیدم، شاید سربندر رو زده باشن، اما ماهشهر هیچ خبری نبوده
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/77285" target="_blank">📅 02:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77284">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z8knS3aIe7nw-m2boDlDuGghLtdRKRUnuvzGbDTYyMcnJeVgKvpfmF7TV4c-B4g9ZXlC1SQHmLD-K4vtawBI2FNtljKKJt7zkvW5BWAmweTOuAxnEVgtpBIuNr9JPwafyfbpnWnDGzLPPK47MxmAr8UbWAeD_Jdeayx3ixzFQwtdNy4_R7Pd6ILbkOuvV1t0g4qYe5Pky2rCYxccPz8gAnm_0vM9D8KdomkCP3xx0ebHjW5Vp9CEzCFrZWslfuWRl0021FJNm--u_p-v4Q-JOtxE7Qg1pCHfFOoKmN4e_sUkozezH0iEpkk2tLQIqLXye0eiszPsBT9QRRDVOmhs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
وحید همین الان صدا اومد از تبریز ، ۳ تا
تبریز همین الان ساعت ۲.۳۸ صدای انفجار شدید اومد
صدای چند انفجار وحشتناک از تبریز همین الان
تبریز سه چهار تا صدای انفجار ا‌مد
سلام تبریز الان صدای ۳ تا انفجار اومد
صدای چند انفجار پیاپی - تبریز ساعت ۲:۳۷ بامداد
وحید جان تبریز 3 باز زدن شدید
سلام آقا وحید 2:37 صدای ۳ انفجار اطراف تبریز
سلام وحید. ۲:۳۷ انفجار در تبریز
ساعت ۲:۳۸ تبریز
چندین صدای مهیب انفجار
وحید تبریز یه صدای مهیب اومد نمی‌دونیم چی بود ولی انفجار بزرگی بود
همین الان تبریز پشت سرهم ۴ تا صدای انفجار اومد
سلام تبریز زدن ساعت ۲.۳۷ دقیقه
مکانی که ما بودیم قشنگ لرزید صدای انفجار هم اومد اما سمتش نمیدونم دقیق کجاست
سلام آقا وحید. الان ۲:۳۸ تبریزو زدن.
سلام وحید جان چند انفجار پشت سرهم در تبریز ۲:۳۷
خیلی شدید بودن
سلام تبریز صدای ۲ تا انفجار اومد
سلام صدای ۳ ۴ تا انفجار پشت سرهم  اومد تبریز
وحید  ۴ انفجار پیاپی تبریز
همین الان صدای انفجار تبریز ۰۲/۳۷
تبریز صدای ۳ انفجار پشت سر هم،ساعت ۲:۳۷
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/77284" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77283">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/668363f045.mp4?token=L6Q8BA30ZhjUsmFuOKHYFQoU7KnWbgMFPM4moD_uTBM4QJbjy1OPVEVCGdMMWg7iSyBGNPIt4ZEWJmhqW9KH8l0WH3TgaGWxefEvp74cYJGsBru8K5Kk9vOLUCIXKVn7oS7Ovj5y8TH8P2cPGjk7QQB3TJoVQW8_12-VB2_lZBt_pM0b8VE39ZZJmwrrSdY78MolB_K84sonkPGpzNnZ27uXk-M31uuLIhDR54fiUpD_vAhu8k4s1MZHRKukjRUnZNJASB_WDnsZPJv0qlO5fpi6jMm9pbj2Z-oluqZ64mRA6WISBGaKWsANaGFv9_IBTzcIHSlPJ5xonLvWT9P9qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/668363f045.mp4?token=L6Q8BA30ZhjUsmFuOKHYFQoU7KnWbgMFPM4moD_uTBM4QJbjy1OPVEVCGdMMWg7iSyBGNPIt4ZEWJmhqW9KH8l0WH3TgaGWxefEvp74cYJGsBru8K5Kk9vOLUCIXKVn7oS7Ovj5y8TH8P2cPGjk7QQB3TJoVQW8_12-VB2_lZBt_pM0b8VE39ZZJmwrrSdY78MolB_K84sonkPGpzNnZ27uXk-M31uuLIhDR54fiUpD_vAhu8k4s1MZHRKukjRUnZNJASB_WDnsZPJv0qlO5fpi6jMm9pbj2Z-oluqZ64mRA6WISBGaKWsANaGFv9_IBTzcIHSlPJ5xonLvWT9P9qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیم فوتبال اسپانیا با تک گل فران تورس در وقت‌های اضافی آرژانتین را شکست داد و قهرمان جام جهانی ۲۰۲۶ شد.
این دومین قهرمانی اسپانیا در جام جهانی است که این بار با پیروزی مقابل مدافع عنوان قهرمانی به دست آمد.
@
VahidHeadline
تلویزیون سراسری در ایران مراسم اهدای جام جهانی فوتبال رو به خاطر حضور ترامپ پخش نکرد.
ترامپی که حتی موقع ثبت لحظه تاریخی بالا بردن جام هم حاضر نشد از کادر دوربین‌ها بیرون بره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/77283" target="_blank">📅 02:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77282">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=WqnSrjReRokfMrVyvECka9JQA4ZB2RAJHQIRXdOWkMhC8YXTmKQbgBW56wdV34QU_Q1czIIhj5rg3EMFPCWQJ4wPSZAvJ02LXhwmup6kWd7GCGqpFU1twPZxqT0iMRFmggsPVYu0jx5ZgmciGBtNFMixzk07DsAf4p8f-lIS9jIuiD6M1ght6rBU17-eGRJzOyCK56BJEi7atcu2IJnThZniQeCPawkBCsEuPJAcZ9D2obXDqKAvd4ugWJvJbd_aThYB4-E5Zlk75xIdt7DbzZvZYgcDZhhi3gcmIrMI6P3q4e2X26rXlzljBEv1r6KKgbUfYWGILrCWDm9xnVTZVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5c82cf41e.mp4?token=WqnSrjReRokfMrVyvECka9JQA4ZB2RAJHQIRXdOWkMhC8YXTmKQbgBW56wdV34QU_Q1czIIhj5rg3EMFPCWQJ4wPSZAvJ02LXhwmup6kWd7GCGqpFU1twPZxqT0iMRFmggsPVYu0jx5ZgmciGBtNFMixzk07DsAf4p8f-lIS9jIuiD6M1ght6rBU17-eGRJzOyCK56BJEi7atcu2IJnThZniQeCPawkBCsEuPJAcZ9D2obXDqKAvd4ugWJvJbd_aThYB4-E5Zlk75xIdt7DbzZvZYgcDZhhi3gcmIrMI6P3q4e2X26rXlzljBEv1r6KKgbUfYWGILrCWDm9xnVTZVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دریافتی از قم با شرح پرتاب موشک
سایر پیام‌های دریافتی که شاید درباره پرتاب موشک باشند:
وحید شهرستان محلات صدای انفجار مهیب اومد . همه جا لرزید
23/44 صدا انفجار از دور ساوه
ساوه ۱۱:۴۵ دقیقه
صدای انفجار
سلام وحید جان صدای انفجار ساعت ۲۳:۴۰ ساوه
نزدیک قم یه صدای انفجار اومد
سلام وحید  الان صدای جنگنده خیلی نزدیک  دلیجان
صدای دو یا سه تا انفجار شنیدم اما خیلی فاصله بود. فکر کنم خمین با اراک بود.
ما خنداب هستیم.
قزوین صدای جنگنده [که معمولا با صدای پرتاب موشک اشتباه گرفته میشه.]
از دلیجان موشک پرتاب شد
ساوه صدایی اومد. مثل انفجار. ولی انگار از دور بود
اراک هم صدای یه انفجار از دور شنیده شد
وحید جان ما اراکیم یک ربع پیش سه بار صدای انفجار اومد اما بار اول صداش خیلی خیلی بلند بود
🔄
منابع حکومتی:
فرماندار اراک اعلام کرد که صدای شنیده شده مربوط به اقدامات آفندی در یکی از استان‌های مجاور است و جای نگرانی نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77282" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77281">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esDlMsBnx3s9hrb7Ml2GxNqG7XmYsEcqOaAgw5E-Q1sU_UNkBH7ES-CHtT8iUHAP0WhzXV3Mcjb4GHNI77l7PMnF2wDEJY8T_Zqn_QKLfs0MrJ66lq4N4Rzc8Yn4EAD9xZj4QAAK7ZGsy1eOaNm8oHFsjT3U4cOMwHEBzBSw0dxPNglfSufrWmHNZczjy5DbJSAqbRVWSE6XAiQAQdYVjR7jJo2XmYewIxpWYYuXaMpgKZoXFr09l2Zv6rkWoAFvSuXRiOdWcKxRc2MOdXioWkEMPbGkHITF86nPS-8NtCX8UKJqdTqu9cwTIQXibyRpH35xPoe6KPeP2qtTKQHShA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
به‌روزرسانی سنتکام درباره نظامیان آمریکایی جان‌باخته اخیر
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) دیروز اعلام کرد که در پی حمله ایران در ۱۷ ژوئیه در اردن، دو نظامی آمریکایی جان باخته‌اند و یک نفر نیز مفقود شده است. پس از جست‌وجویی گسترده، نیروهای نظامی آمریکا اوایل امروز بقایای انسانی ناشناسی را در محل پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.
در رویدادی جداگانه، یک نظامی آمریکایی در شمال عراق روز ۱۸ ژوئیه هنگام انفجار کنترل‌شده مهمات منفجرنشده متعلق به یک پهپاد انتحاری سرنگون‌شده ایرانی، در جریان عملیات کشته شد. یک نظامی دیگر نیز زخمی شد و همچنان برای جراحت جزئی خود تحت درمان پزشکی قرار دارد.
سنتکام به احترام خانواده‌ها در جریان روند اطلاع‌رسانی، از انتشار اطلاعات بیشتر، از جمله هویت نظامیان مفقود و جان‌باخته، خودداری می‌کند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77281" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77280">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSxMA7E5XREDBpkFPjSQPELUAFPU7MVzrN9naHWa1n808PKjuP1dAZ328TGPZypKcyHhojnd8etiw_q9k0Wxa53jOEiwcAwly5cWFbTvUumtOVAhKnfiJyRe0Oxs0-ZB-C4CwLtOzYjhHQNGpTVJtnogDI_oEVJ5-yzdawGlxetTEWymanL317bE5UwxKOXRWw0Xp4Gt67uViAwNTJWdyQgAr-ggux_Wntxgb_rDIzna3ju_v_Cx7Iezl27PmqHXqaN7IhobC3hlp-R6_lAk13J9sEMQ_LKz_2vUNajWOvjz8db9_5DMJGRR0SQE5UUjziBG8L9B6FyJzM6oCrlXpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران گفته است آمریکا بامداد یکشنبه با «تعدادی پرتابه» به سایت در حال ساخت نیروگاه دارخوین حمله کرد. دارخوین شهری در بخش دارخوین شهرستان شادگان در استان خوزستان ایران است.
آژانس بین‌المللی انرژی اتمی اعلام کرد که در حال بررسی این گزارش‌هاست و یادآور شد که این نیروگاه «در مراحل بسیار ابتدایی ساخت قرار دارد و در آخرین بازدید آژانس، هیچ ماده هسته‌ای در آن وجود نداشت.»
آژانس افزود که این حادثه «احتمالاً هیچ خطر پرتوی ایجاد نمی‌کند»، اما رافائل گروسی، مدیرکل آژانس، با انتشار پیامی در شبکه ایکس «خواستار خویشتنداری نظامی در اطراف همه سایت‌های مرتبط با فعالیت‌های هسته‌ای» شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/77280" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77279">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U4puusnp9hP0dVjy4PBa21lQzLxLMBYqUVZXzzEmRoUPc9p8BoS83Q_aZWxqw8dh3FSIcs2_hs2i_dq08yOj7kKqLEJnYZiM-diHD2AzJmQij_y9zhpze4j4aGRai8abbiCJhrdfXQ5ESJnd3kRz6lUQYMOXDxC5TxOysCwVpNPZmJ5aIFb8CaNEB3P1_C4hHhNZTrg1f3PxeknSZM-WN2lGKig0CqVcKZ_oESADxqXieoZorju9O2c5U3Cg8diN8P4O06yNSRv7Ea7I0Tv0l1ZfxgK44p8BbOE2w5J64LgOpdTjFZTEQsLNVFFojOnyVNfV5hsyPN4-TjTrtAOwUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون امنیتی و انتظامی استانداری خوزستان عصر روز یکشنبه از «حمله موشکی آمریکا» به نقطه‌ای در اطراف شهر آبادان خبر داد.
ولی‌الله حیاتی اضافه کرد که این حمله کشته و مجروحی به جا نگذاشته است.
سنتکام، ستاد فرماندهی ارتش آمریکا در منطقه خاورمیانه، [هنوز] درباره این ادعا بیانیه‌ای منتشر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 411K · <a href="https://t.me/VahidOnline/77279" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77278">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H548TzGGHdn7obbFmgCKR2ohcKj050j_rapj_5RryRxEUBmqtPtGjZwo1RStZmWA3yxMVINH7CrypuG9t22Wy-m_VQt6bQddTd0fpmC4zPU73mILoxe4zqhiFBstYuqS_833lFCdnYMJQS3ZyTxZnomyYDCfEZmHl4NryeDAdrfY5T7JvNrLj_xCJFHBqm0JgL8zPxqVfQYnSe6NEEJw1Ni6CdhgUkpsFebi1ZeFKFnBKABgGMI7I3JVwhbNAaGi3-jmvMET8_cFKVNkc48RhfG7TgzHloNks2lGyV_55svG9CZfmicLXuEutTkEqUmoIoKViHL28GmLryxT40mU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل روز یکشنبه اعلام کرد که نیروهای اسرائیلی و اردنی یک موشک ایرانی را که به سمت شهر عقبه در اردن شلیک شده بود، رهگیری کرده‌اند.
دقایقی پیش از این رهگیری، ارتش اسرائیل اعلام کرده بود که موشک‌هایی را که از ایران به سمت عقبه شلیک شده‌اند، شناسایی کرده و نسبت به احتمال «سرایت» حملات به خاک اسرائیل هشدار داده بود.
سخنگوی ارتش اسرائیل در پاسخ به پرسش خبرگزاری فرانسه دربارهٔ گزارش‌های مربوط به شنیده شدن صدای انفجار در نزدیکی شهر ایلات در جنوب اسرائیل گفت که نیروهای اسرائیلی و اردنی به‌طور مشترک یک پرتابه را رهگیری کرده‌اند.
در همین حال، ارتش اردن اعلام کرد که «سه موشک ایرانی را که خاک این کشور را هدف قرار داده بودند» ساقط کرده است و یک موشک دیگر نیز در منطقه‌ای بیابانی فرود آمده است، بدون آنکه محل دقیق آن را اعلام کند.
ایران در دور تازه درگیری‌ها با آمریکا که در هشت روز گذشته ادامه داشته است، اردن را در چند نوبت هدف قرار داده است. ارتش ایالات متحده اعلام کرده که در جریان حمله روز جمعه ایران به اردن، دو نیروی نظامی آمریکایی کشته شدند.
@
VahidHeadline
آپدیت:
اکانت ارتش اسرائیل، ترجمه ماشین:
⭕️
ارتش اسرائیل شلیک موشک‌هایی از ایران به سوی شهر عقبه در اردن، در مجاورت اسرائیل، را شناسایی کرد. چندین موشک رهگیر به سوی بقایای موشک‌ها شلیک شد تا از اصابت این بقایا به داخل اسرائیل جلوگیری شود.
هیچ خسارت یا جراحتی گزارش نشد. مطابق دستورالعمل‌ها، آژیرهای هشدار به صدا درنیامدند. این رویداد پایان یافته است.
آپدیت:
صفحه رسمی وزارت خارجه اردن در ایکس، از احضار کاردار سفارت جمهوری اسلامی در امان در اعتراض به حملات تهران به خاک اردن و اظهارات تحریک‌آمیز مقامات جمهوری اسلامی خبر داد.
در این بیانیه آمده سخنگوی این وزارت‌خانه به کاردار جمهوری اسلامی اعلام کرده است تا پیام روشن اردن مبنی بر توقف فوری حملات را به تهران منتقل کند. ...
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/77278" target="_blank">📅 18:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=cpTUgVaAOHe87DwUy_c2ew-vNyT-EsLyDMrGcbAEchnE3r19v6YQR4PoQGIFbR0ZXrzTNgYR0uqQeh0TGLEpGFP26okuGOQNoUU75zrmxQcTQXoCVVYxWD0ipr-usnaZ4zlKVKAiiyyiug90t5CwSenQGg_E-QgvYgvSkI4nM9aUS8PYRCPH3S_EmTK4q3zG4ZaRrZQJLKZO_0ZM2fUfz2emrQ9G6c8M_e0Go0-SHDPmHdejAKc37RYaEf08OVSPOxvIhSz7SPfDPSHyw-W4cosV8B2I5fezv4bh89pUOIIILZDVwUicveP7UmTcpSix2K9HEjgCf99Am13zrPAh4pTL9ZL83LrUBDpOLEIbFcjoH7dqwGVGBwvy2bGmY7NC3XbK0jv7B3APREZRXqQWUg9TkYHaPtIIJHCeLyIka0eoCXA6qy6aOg4SpcPESVXCyG3I6PaKgeMiqRwxK9cAHZx2shvf-mhXqMwYYvaVSNU_blgJIxj5jsVhBk-dS9ub4tNg0m2NITGyRdNstBBcXjNOnFgp_Jjwv3faqni7LusuK7DQ5-m98lgnsLmruRNBp2rLGO-DmqJ9wSQE60w0yTlyXICHAEwQ3RjKLFx71FJ42KRNEgHfPsDomvZgTk7adjQJbZpTxrXwm5oaGeHTtSQ6U6J0oaThtO9LIC8JeT8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/224ff6e0b2.mp4?token=cpTUgVaAOHe87DwUy_c2ew-vNyT-EsLyDMrGcbAEchnE3r19v6YQR4PoQGIFbR0ZXrzTNgYR0uqQeh0TGLEpGFP26okuGOQNoUU75zrmxQcTQXoCVVYxWD0ipr-usnaZ4zlKVKAiiyyiug90t5CwSenQGg_E-QgvYgvSkI4nM9aUS8PYRCPH3S_EmTK4q3zG4ZaRrZQJLKZO_0ZM2fUfz2emrQ9G6c8M_e0Go0-SHDPmHdejAKc37RYaEf08OVSPOxvIhSz7SPfDPSHyw-W4cosV8B2I5fezv4bh89pUOIIILZDVwUicveP7UmTcpSix2K9HEjgCf99Am13zrPAh4pTL9ZL83LrUBDpOLEIbFcjoH7dqwGVGBwvy2bGmY7NC3XbK0jv7B3APREZRXqQWUg9TkYHaPtIIJHCeLyIka0eoCXA6qy6aOg4SpcPESVXCyG3I6PaKgeMiqRwxK9cAHZx2shvf-mhXqMwYYvaVSNU_blgJIxj5jsVhBk-dS9ub4tNg0m2NITGyRdNstBBcXjNOnFgp_Jjwv3faqni7LusuK7DQ5-m98lgnsLmruRNBp2rLGO-DmqJ9wSQE60w0yTlyXICHAEwQ3RjKLFx71FJ42KRNEgHfPsDomvZgTk7adjQJbZpTxrXwm5oaGeHTtSQ6U6J0oaThtO9LIC8JeT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی در یک مصاحبه ویدیویی اعلام کرد که از زمان آغاز دوره جدید رهبری، شخصا با مجتبی خامنه‌ای دیدار نکرده و تنها افراد محدودی موفق به ملاقات با او شده‌اند.
@
VahidOOnLine
عباس عراقچی، وزیر خارجه جمهوری اسلامی، با اشاره به دلیل کشته شدن رهبر سابق جمهوری اسلامی می‌گوید هنوز این احتمال هست که در رده‌های بالای حکومت «حفره امنیتی» وجود داشته باشد.
او در گفت‌‌وگو با یک مستندساز حکومتی در تهران که بخش‌هایی از آن روز یکشنبه ۲۸ تیر منتشر شده است، با اشاره به «وجود عوامل نفوذی در بالاترین سطح نظام» گفت:‌ «نفوذ فقط در گرفتن اطلاعات نیست، بلکه در تصمیم‌سازی هم هست، در جهت‌دهی به فضای روانی هم هست.»
او تأکید کرد بمباران «بیت رهبری» که در جریان آن علی خامنه‌ای و شماری از فرماندهان ارشد نظامی ایران کشته شدند، از طریق یک «حفره امنیتی» صورت گرفت و افزود که این حفره همچنان وجود دارد.
به گفته عراقچی، در روز ۹ اسفند ۱۴۰۴ که حمله مشترک اسرائیل و‌ آمریکا به ایران آغاز شد، علاوه بر دفتر علی خامنه‌ای، دفاتر علی شمخانی و محمد شیرازی، دو مقام نظامی، و علی‌اصغر حجازی، مقام امنیتی بسیار نزدیک به خامنه‌ای، هم هدف قرار گرفت. از این میان، فقط حجازی زنده ماند.
جواد موگویی که با عراقچی مصاحبه کرده است، در جریان این گفت‌وگو توضیح می‌دهد که علاوه بر جلسه خامنه‌ای با مقام‌های دفاعی کشور، در آن روز یک جلسه بسیار مهم دیگر هم برقرار بود: جلسه شورای معاونین وزارت اطلاعات در نقطه دیگری از تهران.
به نظر می‌رسد اشاره او به جلسه‌ای است که اسرائیل اعلام کرد در نخستین ساعات حملات مشترک با آمریکا، آن را هدف قرار داد و چند تن از اعضای بلندپایه وزارت اطلاعات جمهوری اسلامی را کشت.
ارتش اسرائیل روز ۱۱ اسفند پارسال اعلام کرد سید یحیی حمیدی، معاون وزیر اطلاعات در امور «اسرائیل»، که به گفته آن «فعالیت‌های تروریستی علیه یهودیان، بازیگران غربی و مخالفان رژیم در داخل ایران و خارج از کشور را هدایت می‌کرد»، جزو کشته‌شدگان است.
جلال پورحسین که از او به عنوان «رئیس بخش جاسوسی» وزارت اطلاعات نام برده شده، نیز بر اساس اطلاعیه ارتش اسرائیل ازجمله کشته‌شدگان است.
رسانه‌های ایران پیشتر خبر کشته شدن محمد باصری، از مقام‌های ارشد وزارت اطلاعات، را در حملهٔ روز ۹ اسفند اسرائیل تأیید کرده‌ بودند.
@
VahidHeadline
عراقچی همچنین ادعای منتقدان مبنی بر اینکه مذاکرات زمینه‌ساز جنگ شده است را رد کرد و گفت جمهوری اسلامی در مذاکرات بر موضع خود درباره غنی‌سازی ایستادگی کرده و پس از ناکامی مذاکرات، طرف مقابل گزینه نظامی را انتخاب کرده است.
عراقچی همچنین گفت برای احتمال کشته شدن رهبر جمهوری اسلامی نیز سناریوهایی طراحی شده بود و «این سناریوها حتی کد مشخص داشتند»، هرچند به گفته او در جلسات تصمیم‌گیری کسی تمایلی به طرح آن‌ها نداشت.
@
VahidHeadline
عباس عراقچی درباره فرایند تصمیم‌گیری درباره مذاکره با آمریکا گفت: «آن زمان [بین دو جنگ] کمیته هسته‌ای را در داخل دبیرخانه شورای عالی امنیت ملی تشکیل دادیم که اکنون به کمیته مذاکرات تبدیل شده است و به کمیته شش نفره معروف است.»
«تمام بحث‌های مربوط به مذاکرات، در این کمیته صورت می‌گرفت و مصوبات آن، عینا همان روال مصوبات شورای عالی امنیت ملی را طی می‌کرد.»
به گفته عباس عراقچی، ریاست این کمیته ابتدا بر عهده علی شمخانی و سپس علی لاریجانی بود که هر دو در حملات آمریکا و اسرائیل کشته شدند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/77274" target="_blank">📅 18:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XwHjyliCEDLtqllrx3F-kJwuIcaYT9TuQroWITfEOQvJE-1na4HUmlg8LSH4_hgKqOhkuchzAtGPFDIot1sghHZVainJ5lYJgTys6sBodtsYADZHdWWQVui9TgNeKx-4k6--UKm7xQ2caUUrI-2qAO997L1n-Sbg_Rm0pLAdkcf5vctG52N3wtmiffFJ0ZUvYLleDSr8owmyJvXNnwa3H90efYOvr3qoeqD_d9d0ho_zzmvcVj4hIXSuuqIOvlryQob_K-3N-MIBIWU6Z19rez5scj2xbHPYnwfA5XNWejd1jlDkOIHcCDmRH3GW1Gdly7Yy-Yn_FJ-J5nASY4UA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=vSZuaYgDQBz91EZFMIadD-DYoBCodN-q4C3IKzfygvJUmHYlC68JZA3w0-nqz4c1rwZi4oZ9JH9P0VoeDvjuuH1wgpzWgkQNdPTF7DHom1a4Qrp9XIZhHVCd2b-QRbXRh14slMHUTv_4o1tMpmcc_IKOw3svxGmXi6uCkFR7hkzQBh1lKoN0Zo9niQP6_x678nG9sGxB8f8LAjaMNs6Mjdcp5t6b1rHETsIXSfrmtPYMoKE_8ep8Wqg-_Z1QHbGKjpq71XbwpAY-JoFrldRu6gNAL3LQC8qO3j3s8IO4tN-yXW0b7eL_Wmcjvkxh45CX1GGjYthx2HdqKv0tYPhr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d80bc4cf46.mp4?token=vSZuaYgDQBz91EZFMIadD-DYoBCodN-q4C3IKzfygvJUmHYlC68JZA3w0-nqz4c1rwZi4oZ9JH9P0VoeDvjuuH1wgpzWgkQNdPTF7DHom1a4Qrp9XIZhHVCd2b-QRbXRh14slMHUTv_4o1tMpmcc_IKOw3svxGmXi6uCkFR7hkzQBh1lKoN0Zo9niQP6_x678nG9sGxB8f8LAjaMNs6Mjdcp5t6b1rHETsIXSfrmtPYMoKE_8ep8Wqg-_Z1QHbGKjpq71XbwpAY-JoFrldRu6gNAL3LQC8qO3j3s8IO4tN-yXW0b7eL_Wmcjvkxh45CX1GGjYthx2HdqKv0tYPhr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خواننده زیرزمینی زن که با نام «آنیتا پاپیست» در ایران فعالیت می‌کند روز شنبه با انتشار حکم قضایی‌اش خبر داد که در دادگاه به ۷۴ ضربه شلاق محکوم شده است.
آنیتا که ویدئوهای آوازخوانی خود را در شبکه‌های اجتماعی منتشر می‌کند، طبق آن چه در این حکم آمده، به دلیل «جریحه‌دار نمودن عفت عمومی» به این مجازات محکوم شده است.
این خواننده همچنین تصویری از رسید توقیف پاسپورتش در فرودگاه را منتشر کرده و خبر داده است که خط موبایلش هم مسدود شده است.
یک ماه پیش دادگاه کیفری استان قم پرستو احمدی، خواننده، و هشت نفر دیگر از دست‌اندرکاران و نوازندگان «کنسرت کاروانسرا» را به‌ طور جداگانه به ۷۴ ضربه شلاق تعزیری، دو سال ممنوع‌الخروجی و دو سال ممنوعیت از فعالیت هنری محکوم کرد.
این خبر به‌سرعت در صدر اخبار قرار گرفت و واکنش سازمان عفو بین‌الملل را نیز به دنبال داشت، اما خبر حکم شلاق برای دو خواننده زن دیگر و اخبار این‌چنینی این روزها به دلیل اخبار جنگ و حملات بی‌وقفه به جنوب کشور مورد توجه قرار نمی‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/77270" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DUi6u5mwVrbTt97gVn9oRkqa13Bs1PTfgEI6vqe85TGPWutQn0XjH1WhpM1Rmvo44rD7liOzVRCqiiLyUCkfni5tdl3cqXpe7r519tpInpDLegvEw0IYgIgSHJG_CpPlmnIOqT64hT7iaO16nuEtPlqlnWElhuvq0R9KUzqWOyKabxIYCtLiUpFpamZJhnufRC3cb8T4EA9NDek3rFHy2KvoJqaSsd9-1PqwOzkWbfd5ybpo2Tc_CeX7ICqWnE_7172dsXLKiB2qYNDOVIdiAY13IodMvMT6XIjYTUrTdvPQA8eKhT2-4okLjkkGK5Q-ln5hUI2zuG5aHbDkEu1U3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنا کراری، شهروند دو تابعیتی ایرانی-آمریکایی که پس از حدود ۱۹ ماه ممنوع‌الخروجی و محدودیت‌های امنیتی سرانجام ایران را ترک کرده بود، به ایالات متحده رسید. هم‌زمان، مقام‌های جمهوری اسلامی همچنان روایت منتشر شده درباره آزادی او را رد می‌کنند.
جرد گنسر، وکیل دنا کراری، با اشاره به «۵۶۶ روز بازداشت ناعادلانه دنا کراری توسط حکومت ایران» از همه افرادی که در آزادی او نقش داشتند قدردانی کرد و افزود: «اکنون باید تلاش‌های خود را برای آزادی سایر شهروندان آمریکایی که همچنان در ایران هستند، دوچندان کنیم.»
خبر خروج دنا کراری از ایران نخستین بار روز ۲۴ تیر از سوی دونالد ترامپ، رییس‌جمهوری آمریکا، اعلام شد. ترامپ در شبکه اجتماعی «تروث سوشال» نوشت ایران به یک شهروند آمریکایی که به گفته او از دسامبر ۲۰۲۴ «به ناحق» بازداشت شده بود، اجازه خروج داده و این اقدام را «نشانه‌ای از حسن نیت» جمهوری اسلامی توصیف کرد.
اندکی بعد، جرد گنسر هویت این شهروند را تأیید کرد و گفت دنا کراری پس از ماه‌ها محدودیت امنیتی، در مسیر بازگشت به ایالات متحده قرار گرفته است.
با این حال، خبرگزاری میزان، وابسته به قوه قضاییه، گزارش‌های منتشر شده درباره آزادی یا مبادله یک شهروند آمریکایی را تکذیب کرد و مدعی شد هیچ «زندانی محکوم یا جاسوس آمریکایی» از زندان‌های ایران آزاد یا مبادله نشده است.
با وجود این تکذیب، میزان به اصل خروج دنا کراری از ایران یا لغو ممنوع‌الخروجی او اشاره‌ای نکرد و توضیحی درباره چگونگی ترک ایران از سوی این شهروند دوتابعیتی ارائه نداد.
دنا کراری، ۵۳ ساله و ساکن کالیفرنیا، سال ۲۰۲۴ برای دیدار با اعضای خانواده خود به شیراز سفر کرده بود. به گفته وکیلش، گذرنامه او در ایران ضبط شد و اجازه خروج از کشور را از دست داد. هرچند او هرگز به‌طور رسمی زندانی نشد، اما طی ماه‌های بعد بارها از سوی نهادهای امنیتی بازجویی شد و تحت محدودیت‌های شدید قرار داشت.
بر اساس گفته‌های وکیلش، مقام‌های جمهوری اسلامی او را با اتهام‌هایی از جمله «همکاری با دولت متخاصم» و «جاسوسی» مواجه کرده بودند؛ اتهام‌هایی که کراری و وکلایش آن‌ها را بی‌اساس دانسته‌اند.
گنسر همچنین گفته است حساسیت نهادهای امنیتی نسبت به موکلش به فعالیت او در «بنیاد کودکان مهر» بازمی‌گردد؛ یک سازمان غیرانتفاعی ثبت‌شده در آمریکا که با مجوز دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) و با کمک‌های مالی خصوصی، از کودکان کم‌برخوردار در ایران حمایت می‌کرد.
برخی رسانه‌های بین‌المللی نیز گزارش داده‌اند که کراری علاوه بر فعالیت در یک شرکت فناوری آمریکایی، مدیریت این موسسه خیریه را برعهده داشته؛ موضوعی که به گفته نزدیکانش، به افزایش حساسیت نهادهای امنیتی جمهوری اسلامی نسبت به او انجامیده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/77269" target="_blank">📅 17:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G_N6OXc3whisZELv8x7WeSCFmns01hEfPtt5zqNl8jhKWPr4JUvBWZVsfdPRnhM97LuuJ9NJHiL3ZTVGDudc7-edDo0BOAmHMYUwV0nHdvpPsMMyvPUPETHhhfG1_Eu07ZO3xUlRpHGjiMfgellDm8mW27bp8x-r0LGgeamnLaIudcdtJQfpWFKDNGLjbB63rfg2IpbRuz3Tzp_eQ8RykFIf3x_yrTlB5pg1LnlrMNVQSXvZyCYH-HewQjZ6bomIYbB1-U9FtLx3KJoUb4ZBsZTFvDVW_1qX-viL9w-DDx18dLaExKySXB6rNeckvb3gnO42N8FwcdxSgs_T4LjijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، وابسته به قوه قضاییه، روز یک‌شنبه خبر داد که حکم اعدام عرفان اسفندیاری و گل‌محمد محمدی، دو تن از جوانان معترض دی‌ماه ۱۴۰۴ متهم در پرونده موسوم به میدان علیخانی اصفهان، در بامداد همین روز اجرا شده است.
هفته گذشته کمیته پیگیری وضعیت بازداشت‌شدگان در ایران هشدار داده بود که حکم اعدام ۱۲ نفر از معترضان دی‌ماه در اصفهان در پرونده موسوم به «میدان علیخانی» این شهر، در دیوان عالی کشور «تأیید شده» است.
در میان این ۱۲ نفر که برخی از آن‌ها به دو، سه و حتی چهار بار اعدام محکوم شده‌اند، چندین نوجوان و یک شهروند افغانستان نیز دیده می‌شود. بنا بر گزارش‌ها، گل‌محمد محمدی شهروند افغانستان بود.
این پرونده به وقایع ۱۸ دی‌ماه ۱۴۰۴ در محدوده میدان علیخانی، بین ملک‌شهر و کاوه اصفهان بازمی‌گردد، جایی که مقام‌های جمهوری اسلامی اعلام کردند چهار نیروی بسیج و یگان ویژه به نام‌های حسین رمضانی، محمد همتی، سید علی خشوعی و ولی‌الله صفری کشته‌ شده‌اند.
در پی کشته‌ شدن آنها، ۵۹ نفر در اصفهان بازداشت شدند و برای آنها پرونده‌ای گسترده تشکیل شد.
@
VahidHeadline
این رسانه حکومتی معترضان را به «آتش زدن ساختمان‌ها، تخریب تابلوهای شهری، دوربین‌ها و چراغ‌های راهنمایی و رانندگی، تخریب پاسگاه و کلانتری، آتش زدن لاستیک، مسدود کردن خیابان، حمله به مردم در حال تردد در خیابان و تخریب مسجد» در جریان تجمعات ۱۸ دی در میدان علیخانی متهم کرد.
بر اساس این گزارش، «عوامل دشمن» در اعتراضات ۱۸ دی به «انواع سلاح گرم، چاقو، قمه، قداره و کوکتل مولوتوف» مجهز بودند و در جریان درگیری آن‌ها با نیروهای جمهوری اسلامی در میدان علیخانی، چهار مامور انتظامی کشته شدند.
در پرونده میدان علیخانی ۱۲ نفر به اعدام محکوم شده‌اند.
در زمان اجرای حکم اعدام، اسفندیاری ۱۹ سال و محمدی ۲۴ سال سن داشتند.
۱۰ متهم دیگر این پرونده که زیر حکم اعدام قرار دارند، به سلول انفرادی منتقل شده‌اند و نگرانی‌ها درباره احتمال اجرای قریب‌الوقوع حکم آن‌ها بالا گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/77268" target="_blank">📅 17:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اگر صدایی شنیدید و خواستید به من هم اطلاع بدید لطفا فقط بگید صدا شنیدم. یا نور دیدم، زمین لرزید... یعنی لطفا تفسیر نکنید که: زدند!
آبادان تک صدای انفجار از دور ۱۶:۳۸
سلام همین الان ابادان رو زدن برق هم نداریم
صدای انفجار آبادان همین الان
همین الان صدای انفجار یا شلیک موشک از آبادان
نمیدونم دقیقا کجای شهر بود
سلام ابادان همین الان ۱۶:۴۰ صدا شنیدیم
سلام وحیدجان همین الان صدای مهیب انفجار از آبادان
همین الان آبادان رو زد نمیدونم کجا بود ۱۶:۴۰
آبادان صدا انفجار
صدای انفجار ۱۶:۳۹ آبادان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/77267" target="_blank">📅 16:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پیام‌های دریافتی الان درباره شنیده شدن صدای انفجار که می‌تونه انفجار پرتاب موشک باشه، انفجار شلیک پدافند باشه و...
سلام وحید جان
الان ۴:۳۱ صدای انفجار اومد، کرمانشاهم
کرمانشاه صدای انفجار اومدددد
وحید جان (۱۶:۳۲)  کرمانشاه دو انفجار مهیب. احتمالا داخل شهر یا بسیار نزدیک به شهر
سلام وحید جان
کرمانشاه 4:31، دو تا انفجار بزرگ صدای جنگنده خیلی نزدیک و زیاد
همین الان کرمانشاه صدای وحشتناکی اومد
صدای پدافند نبود
الان 2 صدا انفجار آمد کرمانشاه
سلام همین الان کرمانشاه صدای وحشتناکی امد
ما شریعتی هستیم
وحید الان کرمانشاه ساعت ۴:۳۲ زدن
سلام وحید جان الان صدای ۱ انفجار از کرمانشاه اومد
صدای شلیک موشک آسمان کرمانشاه ساعت 16:30
دو تا موشک کرمانشاه خیلی نزدیک بود.
انگار تو شهر بود
صدای سوت موشک کامل پیچید
کرمانشاه ارسال موشک ساعت 16 و 32
دو پرتاپ موشک
[هنوز از اخبار ساعت‌های گذشته بی‌خبرم]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/77266" target="_blank">📅 16:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77265">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a4gRINCYL9mVNwS50zYINwtl5BHl_AhCCDwtiLRWjtnslwD-yYphHt45Ek7nO4LATB_Mp1g3QGTGdXJxDBJuByP5KR_tVrFfQz0mcML4fyalCJxeL0d2mJADJ3Wp5pnjscnZQiagOSG4jVEO3vFDchLu__hF6IXD2vUIniBtbMOe7IXVA1sgWRJzaVgh3mEc5hWpZtRiTEn51ZqSFZLQ_qWgWnFbRdl4_DPQ9nG_U5W5IVKpYEYFRIdZPBPTutvVGPd_nFJSHywJVxKr_0pfzsdiJPOC4sT_wzbqbLoiRE7zAmFIQ7y1KtXiLsd76siPYHvIXIjq8i155TDpDvPppQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار در کویت هم‌زمان با پیام‌ها درباره پرتاب موشک از خوزستان
آپدیت:
ستاد کل نیروهای مسلح کویت در بیانیه‌ای رسمی اعلام کرد پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی «متخاصم» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77265" target="_blank">📅 10:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77264">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیام‌های دریافتی:
صدای یک انفجار چابهار اومد دور بود فقط موجش بود
09:42 بدجور زد الان چابهار رو نمیدونم کجا بود
چابهار یهو صدای انفجار اومد شیشه هامون لرزید
🥲
قبلا تو روز روشن نمیزد
چابهار یچی زدن همه ریختن بیرون ولی نه سمت اسکله نه پایگاه امام علی اصلا هیچ دودی هم نیست به شدت لرزوند
آپدیت: منابع حکومتی
فرمانداری شهرستان چابهار: صدای انفجار شنیده‌ شده در روز جاری (۲۸ تیر) در حوالی شهر چابهار، ناشی از عملیات امحا و انهدام کنترل‌شده مهمات عمل‌نکرده بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/77264" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77263">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hZQK_MZCIUz25Ch6pbARAViKd5pGVQLrIvFOEUb_mVwYfoyWb617NtqGJXP5dzsN6BUvJwUq4s0GFb9Xfcmmf0HsAbAg-9eLz16jR7_0lJnsJCKSQKfI9NUBSJ1c8vlRQBDMiwLrew-5pm23Tam1_7tozW5GN0GTAvl-8D-vHk7JwAo31yf_MRDCJo9fHeXgWNn6qaSixK4AO2F2pc7Tuw2plUUu7BGsbM9DMSFNe2vOt1j-NajTk4Q8EslaNUY5NwUfjsh5BZzFd3J1PSl7Dr6IIFgY1xi4dcB1iFoN12HFL-jOV8TGmzHmf3eXwQHpFmIPJkmg6cBRf8Pj17_Z0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های ساعت ۹:۰۹
سلام وحید همین الان گرگان زلزله اومد نسبتا شدید بود
آقا وحید گرگان گلستان الان ساعت 9:09 صبح هم لرزید، زلزله بود
سلام گرگان الان زلزله اومد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/77263" target="_blank">📅 09:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77262">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HbHsC-tu1YGtXJWSHFOGAqrt_CpwMxD-VnhViEuX5-HWlMv9zvITM0z7pzTaK0ulYB9rTlg36KoJdd1GvW4f1p7rbHVe-vN-VWi_moE5vRKdAhPsnNC0p9_04ChGBU6kSBsZl1NhulVV1dK4M9RjTN--6LNpFv7Ia4kk8_kcRXhaTD6ObrddcAdCSZ3sRTwNbk64lC57hSPDBgXV7Hwrx7qon9c1WQtxpzJAFf9751ZGf8hp8xsoUsXP3DTcXAMOLNuns4fyHvAAeBkUgKTMFyygRdXD7wQ4fa1DQLn0-OAN-4yRWlk9jRwkJ1KObnT8GyMAKpgF-mx_NBhvCLfSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت: زمین‌لرزه به بزرگی ۴
دوباره
در سالند خوزستان
پیام‌های دریافتی:
۷:۵۷ اندیمشک دوباره زلزله اومد
دزفول لرزید دوباره
اهواز دوباره زلزله اومد
دزفول لرزید بازم فقط شدتش خیلی کمتر بود
زلزله ۷ و ۵۷  دقیقه باز هم دزفول با شدت کمتر از قبلی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/77262" target="_blank">📅 07:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77261">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIe7oz_vTzlGt6-kM_z6FA92gRZXtpEXITiT5a6IxjYR01EjCQ_i5F6npX4OtUUkkI71uoZcNwrl2s0pY5gQSS-Qfmf3TlqcPofledprb-25fdE7IfseYFqPaLTdMbg20r4tXAj43qP5vsZPlLCFKCJn3P7uvwjgxTkaK4prmFlr4t1GSuCpy185uH0i5TmdAcOnWQy0Gw5aP692-GqNYxjaBX-QiBHz67rqVFsLxqVPDD-cFqhjwjFYNnHDWqN3rjNAg6ucCqXuoGFMch0ikZmRNj2VFuWINi4GIoTBkpxPf__XEgKtXQA5kyPw5v5AZOm7Qv9VbZ89rQrdfL8Ymg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با ادامه سقوط ارزش ریال، قیمت ارز، طلا و سکه در بازار ایران به سطوح تازه‌ای رسیده است.
براساس نرخ‌های ثبت‌شده در روز ۲۷ تیر، قیمت هر دلار در بازار آزاد به حدود یک میلیون و ۹۴۵ هزار ریال، معادل ۱۹۴ هزار و ۵۰۰ تومان رسیده است. یورو نیز حدود ۲۲۳ هزار تومان و پوند بریتانیا بیش از ۲۶۲ هزار تومان قیمت‌گذاری شده‌اند.
در بازار طلا، قیمت هر گرم طلای ۱۸ عیار به حدود ۱۹ میلیون و ۱۳۸ هزار تومان و هر مثقال طلا به حدود ۸۲ میلیون و ۸۹۵ هزار تومان رسیده است.
قیمت سکه نیز یک میلیارد و ۹۰۰ میلیون و ۵۰ هزار ریال ثبت شده که معادل بیش از ۱۹۰ میلیون تومان است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/77261" target="_blank">📅 07:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77260">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b791da5472.mp4?token=peNUCzosifTa-Evf7iaIs4mzSbKC-D29pnIWFdEmnohAL_JW7DIXZ0vaWPGHEzAmAEnfclO3FAwOQF8Ke6eWOeESqZx7Z2YVuON-b25svwOggo_EN_w4avwu-kV7dc8dXdeDfILUqGZ_pseVC4-WiTL3uvly3jaUB_vN1HZD455Ymhtx9xuSf0D9oZkebaqyNZtOwnLRlIdiRaHzSMjq-WYf6c9FLoj72pTdnc1Yu6fUgS6WoRZMgQYICEg5KI7KOQcxajPOVYz3Oc4N209yEjec6gjIisSGbfr0mQUG4rZrvknoo7xdIEJ9mYvIxflF2mxDN1iClB1xbt-W1RLbQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b791da5472.mp4?token=peNUCzosifTa-Evf7iaIs4mzSbKC-D29pnIWFdEmnohAL_JW7DIXZ0vaWPGHEzAmAEnfclO3FAwOQF8Ke6eWOeESqZx7Z2YVuON-b25svwOggo_EN_w4avwu-kV7dc8dXdeDfILUqGZ_pseVC4-WiTL3uvly3jaUB_vN1HZD455Ymhtx9xuSf0D9oZkebaqyNZtOwnLRlIdiRaHzSMjq-WYf6c9FLoj72pTdnc1Yu6fUgS6WoRZMgQYICEg5KI7KOQcxajPOVYz3Oc4N209yEjec6gjIisSGbfr0mQUG4rZrvknoo7xdIEJ9mYvIxflF2mxDN1iClB1xbt-W1RLbQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
آمریکا هشتمین شب متوالی حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) به دستور فرمانده کل قوا، دور دیگری از حملات علیه ایران را در ۱۸ ژوئیه ساعت ۱۱:۳۰ شب به وقت شرق آمریکا به پایان رساند.
در هشتمین شب متوالی حملات آمریکا، نیروهای سنتکام با موفقیت تأسیسات نظارت ساحلی و پدافند هوایی ارتش ایران، توانمندی‌های دریایی و محل‌های ذخیره موشک و پهپاد را هدف قرار دادند تا تضعیف توانمندی‌های نظامی ایران ادامه یابد. تجهیزات نظامی آمریکا همچنین نیروهای سپاه پاسداران انقلاب اسلامی را که در ۱۷ ژوئیه به نیروهای آمریکایی در اردن حمله کرده بودند، هدف قرار دادند.
بیش از ۵۰ هزار زن و مرد نظامی آمریکایی در سراسر خاورمیانه مشغول عملیات هستند. آن‌ها همچنان در بالاترین سطح هوشیاری، متمرکز، مرگبار و آماده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77260" target="_blank">📅 07:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77259">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">منابع حکومتی:
‌معاون امنیتی ‌استانداری خوزستان: ‌جنگنده‌های‌ آمریکا ساعت ۰۵:۵۵ دقیقه یک نقطه در اطراف شهر شادگان را مورد اصابت موشک قرار دادند.
ساعت ۶:۱۰ صبح امروز جنگنده‌های آمریکایی بار دیگر مناطقی در جزیره قشم را هدف حمله قرار دادند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/77259" target="_blank">📅 06:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77258">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پیام‌های دریافتی:
الان دو تا افنجار بندرعباس ۶:۹
اصلا تا حالا این ساعت حمله نمیکردن!
وحید جان ساعت ۶ و ۹ دقیقه قشم صدای چند انفجار اومد باز
وحید ساعت ۶:۰۷ دقیقه دو بار قشم صدای انفجار و لرزش
دو سه ثانیه قبل از زلزله،صدای بمب سنگرشکن اومد،قشنگ از دوران جنگ تو گوشم صداش هست
بندر عباس ساعت 6:09 دقیقه مورد اصابت قرار گرفت دوباره
سمت پایگاه هوایی دو انفجار بلند
یکی دیگه هم الان زدن ساعت ۶:۱۰
سلام بندرعباس رو زدن ۳صدای انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 402K · <a href="https://t.me/VahidOnline/77258" target="_blank">📅 06:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77257">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lvFQ93Vni0_Jcm1lTLckf7rqQB1JH5nwEZ503bgrtO4AO6mnhlvbWtBHLQYX2dS3JbGIx3dAn4Sq_i8yhJA2FWmeoL6Yn2JzqQLDr5F6Z1qkKqqNbgqDggwt2c1yAYydorUb9Z7Cc-Lust-4Z2g233iqOqQfD53rf27gbctupP92tm_tFWPw2ml4u8H6vd8jYqwybFH1jYr_im055B3JMWc5KyLUbXyUf83HQKXxwFYsE3AtRFI-LnU7KfInRhuKElzj3Ca8YSUUI_SURcUgKhzgpiPOx-sV-yaLrx8WzivwaAvhtBPiJfQBcePldq-Ce74rI-bFYuk_mvVTi3fKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
زمین‌لرزه به بزرگی ۵ در عمق ۱۲ کیلومتری زمین در سالند خوزستان
پیش از آپدیت:
پیام‌های دریافتی درباره لرزش زمین:
وحید جان همین الان زمین لرزه شدید شهرستان شوش
خیلی بد بود
دزفول  رو زدند
همین الان تکون خورد همه جا مثل زلزله بود
زلزله اهواز
خونه لرزید بد جور دزفول چ خبرههه
همین الان اهواز زلزله اومد
5:55 دزفول
از توی خواب پاشدم،تخت و خونه و تمامی وسایل داشتن با شدت بالا میلرزیدن
اصلا نمی‌دونم زلزله بود یا جایی رو زدن
اقا وحید اهواز همین الان زلزله اومد 5:56
اهواز ۲ بار پشت سر هم زلزله اومد
ساعت ۵:۵۵
یکم ترسناک بود
اهواز زمین لرزه اومد
خیلییی شدیدددد تمام خونه لرزید
سلام اهواز زلزله شدید ۶ صبح
همین الان اهواز خیلیی بد لرزید
زلزله اهواز ساعت ۵ و ۵۵
اندیمشک هم زلزله شدید امد
ماهشهر زلزله نسبتا خفیفی اومد
سلام زلزله اهواز شدید مثل اینکه از دزفول بود
سلام آقا وحید اهواز الان زمین لرزه حساس کردیم،ساعت ۵ و ۵۷ دقیقه صبح
وحید جان دزفول همین الان زمین لرزه شدددد
زلزله اهواااز
از خواب پریدم کامل تخت تکون میخورد
زلزله اهواز اومد وحید کل خونه لرزید
ساعت ۰۵:۵۵
از خواب پریدم از شدت زلزله
اهواز چندبار لرزید بدون صدا
وحید جان الان اهواز زلزله ساعت ۵.۵۵
سلام زلزه اومد اهواز‌
وحید از خواب بیدارم کرد
و طولانییی بود
سلام وحید جان ساعت 5:56 دقیقه زمین لرزید ویه تکون خیلی شدید خورد خونه دزفول
سلام وحید جان ساعت ۵:۵۶ صبح زلزله فوق شدید اهواز همه چی داشت تمون میخورد
همین الان اهواز زلزله ، وحشتناک بود
سلام اهواز زمین لرزه بزرگی اومده حدود 10 15 ثانیه خونه داشت میلرزید
زلزله خیلی شدید اهواز ، ۲ بار تقریبا پشت سرهم ساعت ۵:۵۷
اهواز ساعت ۵:۵۵ خونه بد لرزید انفجار نبود انگار زلزله اومد
اهواز ساعت 5:55 دوبار زلزله اومد
آقا وحید زمین لرزه شدید اهواز در حدی که مبلا از جاشون تکون خوردن
سلام زمین لرزه اندیمشک هم حس شده
سلام شوش دانیال همین الان لرزید. انگار زلزله بود
دزفول  ساعت ۵:۵۶ صبح چند دقیقه ناجور لرزید
اهواز زلزله اومد هنوز لوسترها تکون میخوره
سلام وحید خوزستان لالی خیلی شدید زلزله اومد۵:۵۵
مسجدسلیمان هم زلزله حس شد ۵:۵۶
درود ایذه دو بار لرزید الان‌
سلام ساعت 6.55 شوش بدجور لرزید اما خیلی کوتاه ولی خیلی ترسناک بود
سلام ساعات 5:55 گتوند خوزستان زلزله احساس شد لوسترا تکون میخوردن
سلام زلزله سمت دزفول خیلیییی شدید بود یکم دیگه ادامه میداشت من خودمو از تراس پرت میدادم
اینقد طولانی بود که موقعی که بیدار شدم رفتم توی تراس هنوز قطع نشده بود توس عمرم اولین بارم بود همچین چیزی حس کرده بودم
🔄
پیام دریافتی به نقل از مرکز لرزه‌نگاری کشوری:
گزارش مقدماتی زمین‌لرزه
بزرگی: 5
محل وقوع: استان خوزستان - حوالی سالند
تاریخ و زمان وقوع به وقت محلی: 1405/04/28 05:55:21
طول جغرافیایی: 48.61
عرض جغرافیایی: 32.58
عمق زمین‌لرزه: 12 کیلومتر
نزدیک‌ترین شهرها:
23 کیلومتری سالند (خوزستان)
27 کیلومتری اندیمشک (خوزستان)
29 کیلومتری دزفول (خوزستان)
نزدیکترین مراکز استان:
103 کیلومتری خرم آباد
140 کیلومتری اهواز
📍
آمریکا هم
میگه
بزرگی زلزله ۴٬۹ بوده در عمق ۱۰ کیلومتری همونجاها:
GoogleMaps
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 415K · <a href="https://t.me/VahidOnline/77257" target="_blank">📅 05:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77256">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پیام‌های دریافتی:
بندرعباس همین الان صدای چهارتا انفجار اومد
03:33 سه تا پشت هم صدا اومد بندرعباس ولی فکر میکنم دور بود
همین الان بندر عباس صدای 4 انفجار
الان وحید جان ۳:۳۳ چهاتا انفجار شدید بندرعباس
همین الان قشم
صدای ۶ تا افجار پشت سر هم
خیلی بلندو قوی بود
کل پنجره ها لرزید
سلام ساعت۳:۳۴ صدای سه تا انفجار قوی اومد بندرعباس
سلام بندرعباس ساعت ۳ نیم صدای ۴ انفجار شنیده شد
بندرعباس ۴ تا الان زدن
#بندرعباس
28 تیر ساعت 03:33
صدای 4 انفجار سریالی،محدوده پایگاه هوایی
۴ تا انفجار سنگین در بندرعباس
بندرعباس 3:33 تقریبا سه تا صدا اومد
🔄
سه تای دیگم زد 03:35
مجدد انفجار ۳ تا در بندرعباس
دوباره زد ، شدید داره میزنه
یه صدای خیلی وحشتناک تر الان اومد۳.۳۵ بندرعباس
دوتا دیگه هم الان زد
سلام صدای ۴ انفجار به همراه لرزش از قشم
بندرعباس وحشتناک صدا انفجار میاد مشت سر هم داره میزنه
بندرعباس صدای انفجار 3.35 شدید بود
وحید قشم رو الان ساعت ۳ و ۳۴ دقیقه دو بار زدن
بندرعباس همین الان 3 انفجار جدید3:35
#بندرعباس
28 تیر ساعت 03:35
صدای 3 انفجار سریالی دوباره ،محدوده پایگاه هوایی
وحيد جان قشم هم صدا مياد
٤،٥ بار پشت سر هم
همین الان ساعت ۳:۳۶ چندتا صدای انفجار شدید در قشم
الان ۳تا افنجار دیگه اومد، کل خونه لرزید، خیلی بد بود ۳:۳۶
تسنیم ساعت ۴:۴۵
گزارش ‌خبرنگار تسنیم از بندرعباس:
🔹
براساس اعلام استانداری هرمزگان، تا این لحظه ‌بر‌اساس گزارش‌های دریافتی، هیچ‌گونه اصابت موشک یا پرتابه‌ای در بندرعباس ثبت نشده است.
🔹
در حال حاضر آرامش در منطقه برقرار بوده ‌و با وجود شنیده شدن برخی صداهای نامشخص، طبق آخرین گزارش‌ها تاکنون هیچ موردی از اصابت موشک در بندرعباس تأیید نشده است.
🔄
ساعت ۵:۳۰
صدای انفجار اومد همین الان
4 تا پشت هم
وحید الان ساعت ۵ و ۳۰ دقیقه قشم دو بار صدا انفجار شدید اومد خونه لرزید
بندرعباس الان دوتا صدای انفجار اومد ۵:۳۰
ساعت ۵:۳۱ دوتا صدا انفجار اومد بندرعباس
دو انفجار الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77256" target="_blank">📅 03:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77255">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پیام‌های دریافتی ۲:۱۷
درود وحید جان همین الان بهبهان اگر اشتباه نکنم سمت پالایشگاه بیدبلند رو زدن ما تو حیاط بودیم  که اون سمت آسمون سرخ شد
سلام بهبهان صدای سه تا انفجار اومد
سلام بهبهان چندین صدا اومد
صدای عبور جنگنده در بهبهان شنیده شد ولی تا این لحظه هیچ  صدای انفجاری من که ساکن شهرم نشنیده‌ام.
خبرگزاری مهر:
برخلاف فضاسازی رسانه‌های ضدانقلاب، تاکنون هیچگونه حمله و بمبارانی‌ در بهبهان صورت نگرفته است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77255" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77254">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fahG8MVQVYkM7iYdOy-7wom3FJDhK4-JarTp4kLFn18KLlrZ98wUjaaf3N_uUI7CP40kooU23oEISxP0wpEjozT1Gt7ZfjCqk-7Vk9UU9zEyFZvwSGjQeJxYJHdE3xLYIj67u8aQ86Zr0OhGCQpfwjfSvDsv2UWHwIaeYOd7h7IM6NO2MN1e7UlmQ8DQ_aW8L213BZKPx949KrmVQoINL6Wuu4odlQwOJOo5WowTEWHMqjIAP9EYn6Gpj4acOBnXBtC2JjXCCKxsF7UYqBB0GYSMWJZu42_ASsECTsfcnWtpsU4F2gGpbyukBrLuYT1LRFR5D26dqOLfWC2nGExE-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
امروز ساعت ۶ عصر به وقت شرق آمریکا [۱:۳۰ بامداد یکشنبه به وقت تهران]، نیروهای ایالات متحده به دستور فرمانده کل قوا دور تازه‌ای از حملات هوایی علیه ایران را آغاز کردند.
این حملات با هدف تضعیف بیشتر توانایی ایران برای تهدید کشتیرانی تجاری در تنگه هرمز و مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی انجام می‌شود که شب گذشته به نظامیان آمریکایی در اردن حمله کردند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/77254" target="_blank">📅 01:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77252">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ErfI8D4_xXso0Om37onR14VAYPoM86LnHn0evpJOxBHH84RjTPk970Yi4gMqUUpaxQkyOoCgzqQbs2D8wcPytVna2DK2iXuSard13ZN9NPynfQo9ZTNOWLMinmPhzTUvySBEOAwGNpswxsnngRPWaBoGooMiVkf4X_5DawlRDOa0d5Ue3YC_EPtu7E3pp59RKXauQRX1EKmc2OLx8mH8VLvjJ_LzJE1igYO8NSy2K_fL-1M3d8Snn9GK3GrgQGxLXoPMg1LRSAa_U8O70eubIv7612VrJxklqBJ7BEH_fWUD0vQVQ5ZhkgGJ3TDhmtBzQOY1xbW4khJY1W-Zkv4sFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aca24TxBwCdqm878-HLut_LTiI02XkZhNnPmrFLzZtM1uzj6H0yRqKxvHlzpLMsjpokfk1QU6tm-cYpbm777mtL7osQuL0XopfUhTnB448b-LTHqharOZe0BoC4MyiWC6KI3P25ntIpNkJQnyrBLnlkAFwZF_GSXp-LkjWjtgDcINnVzTM5h_LocvW1SsPTMAji-n0jb43n-z4xRwzLZ8nCWGqowJ4ktkecEV_oiC66cQU8eu1LAivQ0rs0SV91okJNEoVfBe6IOdMZoKklIGpFM9YgMKUS4jCOS99qklrLRfXoso9mfFHOHlszr-WK07Mdx6OoGwZJ9YyrlMXnrow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری ایالات متحده، در واکنش به کشته شدن دو سرباز آمریکایی در اردن به شبکه «نیوزنیشن» گفت: «بسیار غم‌انگیز است، واقعا رویداد بسیار غم‌انگیزی است. ما از دیدن چنین چیزی متنفر هستیم. آنها در راه خدمت به کشورمان جان خود را از دست دادند.»
@
VahidOOnLine
ترامپ در بخش دیگری از این مصاحبه با مواضعی قاطع، بار دیگر تأکید کرد که «ایران نمی‌تواند و نباید سلاح هسته‌ای داشته باشد.»
او همچنین در واکنش به اظهارات مقامات جمهوری اسلامی مبنی بر تعلیق تعهدات تهران در قبال توافق موقت یک ماه پیش، با بی‌اعتنایی کامل اعلام کرد که اهمیتی به این تصمیم ایران نمی‌دهد.
پیش از این، کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزارت امور خارجه جمهوری اسلامی، شنبه ۲۷ تیر، گفت آمریکا همه تعهدات خود ذیل تفاهمنامه اسلام‌آباد را نقض کرده و ایران نیز اجرای تعهداتش را متوقف کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/77252" target="_blank">📅 01:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77251">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nS-9nyG2cEQQ4v9V0ShQ4zPQnzAO63So9NxPzfSn2QOavyEvOSChmpqDkjslv4cXwdXvOgiMjenL9IMrv1Q5QnJIv2oGyOhEIr2rbonEtEjG-dyaxQdWiSYvk1H4J0mCrnLgeDmDZS-5bwvvwWtyhqfzaa-3vJf_w2lCWrBScSKigOWdjeVlOrBBRMVIyGNm2x_RvrVsR6kynWQGoHZCAEBHr8WxnlhGgu0z2Bz3rjGceeTXVMIMytC2Z5570ZW-Ny2Luf6aodf2KxltFfKriwZmZiLLwfGULJbyCawXCuJEbsjVgql9iq0In31c7L5vYoJzweGUylshTen29ZdGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه نیویورک تایمز به نقل از چند مقام آمریکایی نوشت حمله جمهوری اسلامی به اردن که جمعه به کشته شدن دو سرباز آمریکایی و مفقود شدن یک سرباز انجامید، چهارمین حمله به نیروهای آمریکایی در این کشور طی پنج روز گذشته بود.
به گفته این مقام‌ها، این حملات در مجموع ده‌ها سرباز آمریکایی را زخمی کرده و به تعدادی بالگرد بلک هاوک آسیب رسانده است.
این مقام‌ها گفتند حملات و خسارات ناشی از آنها نشان می‌دهد نیروهای جمهوری اسلامی همچنان ذخایر موشکی قابل توجهی دارند و در عبور از سامانه‌های دفاع هوایی آمریکا نیز ماهرتر شده‌اند.
نیویورک تایمز نوشت اهمیت اردن برای عملیات آمریکا افزایش یافته است، زیرا پنتاگون پیش و در روزهای نخست جنگ، بخشی از نیروهای خود را از بحرین، امارات متحده عربی و قطر به اردن و اسرائیل منتقل کرد.
به گفته مقام‌های آمریکایی، محدودیت‌های اعمال‌شده از سوی برخی متحدان منطقه‌ای آمریکا برای استقرار نیروها و پرواز هواپیماهای آمریکایی بر فراز خاکشان نیز نقش اردن در عملیات واشینگتن را افزایش داده است.
پنتاگون از اظهارنظر در این‌باره خودداری کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 463K · <a href="https://t.me/VahidOnline/77251" target="_blank">📅 01:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77250">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9VWdyaz2vXmnUjPmJhUdltWHc44A2VKLuRPh30veUhTKYk9w5FAzwQQuM3eiJo8Xnv74LEMroLB-l3PX9Rq-Otf5SO5BU35gYsXjLp02XgshKVrktEW6znGuUovAHV7QjoBoL18spHyJXkF1bL0qibdLPHzttpSGQmHzGHcEOxIjFA0CojIg3UzufnSvmnXF-ovCn51OzBUDBY9lPlWgWLsOfInlhCGjwMnVHpnAhc23AOcvC99Ra_CLlFT_k7RDBAgBMrnF3gurba68rPx4fm3k0kGQByuW2A5V_b6pfUGK7xBPtqv3B86ztaW26dd-cRPr0fQ8UAjyOVZlzFyKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری مهر، بامداد یکشنبه، ۲۸ تیرماه، زمین‌لرزه‌ای به بزرگی ۳.۷ حوالی سرگز در هرمزگان را لرزاند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 461K · <a href="https://t.me/VahidOnline/77250" target="_blank">📅 00:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77249">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">چند پیام دریافتی در ساعت ۲۲:۱۳
بندرعباس ۳ انفجار
اقا بندرعباس رو زد
۴ الی ۵ تا
زدن داداااا
بندرعباس
اقا وحید الان بندرعباس زد صدا اومد معلونم نبود کجاس
[ولی فقط همین‌ها بودند و انقدر هم صبر کردم که دیگه پیام‌های دریافتی بعد از انتشار این پست فاقد اعتبار محسوب می‌شن.]
آپدیت:
گزارش خبرنگار تسنیم از بندرعباس:
🔹
از دقایقی پیش اخباری مبنی بر صدای انفجار در بندرعباس منتشر شد، اما مسئولان استانداری هرمزگان ضمن تایید این صداها می‌گویند هنوز گزارشی از اصابت موشک یا حمله جنگنده‌های آمریکایی نداشته‌ایم.
🔹
از سوی دیگر برخی منابع خبری به خبرنگار تسنیم تاکید کردند احتمالا این صداها مربوط به هشدار نیروی دریایی سپاه به کشتی‌های متخلف در تنگه هرمزگان باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 494K · <a href="https://t.me/VahidOnline/77249" target="_blank">📅 22:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77248">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/77727bb200.mp4?token=AsBj6Dqp__eL-Cf6TAnVIxJSnWljqHmonCBEZVDG300GZr0mKsRueXQ-mG8p_b_W22p9xMgbNgmSh5mslvXplaoZDgYw1z4IryGqV3OeXN3D4wX1k2BR6gJOETq8zGygIswMfnYUiJbY_eDqTtGISJwGLnLfiD9QQKt-zYHFLm8jrZhGDTWvpxXY8AVIlhTS7d-dLTZbnVrF1YuRfPbCTnBYz4dTnJCikSDFJ5pPpW_u8h_3WC4toObh7BBTY9jegHgSVv11taRwWoLz2jtnknpIvVGUs8Z_nXiMFpyljzX5PfsBpYzRfxrUSJTIXeQhDGFGGY5EFdLCRszA3DV4qg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/77727bb200.mp4?token=AsBj6Dqp__eL-Cf6TAnVIxJSnWljqHmonCBEZVDG300GZr0mKsRueXQ-mG8p_b_W22p9xMgbNgmSh5mslvXplaoZDgYw1z4IryGqV3OeXN3D4wX1k2BR6gJOETq8zGygIswMfnYUiJbY_eDqTtGISJwGLnLfiD9QQKt-zYHFLm8jrZhGDTWvpxXY8AVIlhTS7d-dLTZbnVrF1YuRfPbCTnBYz4dTnJCikSDFJ5pPpW_u8h_3WC4toObh7BBTY9jegHgSVv11taRwWoLz2jtnknpIvVGUs8Z_nXiMFpyljzX5PfsBpYzRfxrUSJTIXeQhDGFGGY5EFdLCRszA3DV4qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توییت، ترجمه ماشین:
این ویدیو لحظه اصابت چند موشک بالستیک ایرانی با برد متوسط تا میان‌برد به پایگاه هوایی موفق‌السلطی در اردن در طول شب را ثبت کرده است؛ حمله‌ای که دست‌کم دو نظامی آمریکایی را کشت و چند نظامی دیگر را مجروح کرد.
sentdefender
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/77248" target="_blank">📅 21:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77247">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T8tKKTxXM5RDnmyVbwbrvEXHePS7tzHR249eN0EWIz3MQnl5se-xVaCG9mAGxihxsLbeHK3PkCC9UrhNxs7P9QU_4I8ZXTgMC-hDrsTmKnnrPk0I_iAI55u-15lt7xf2d89Oys9dfdk0EBWIupwcBeeOXNnC3o7I0NS4pJcDmrNCP70tkLhwlgrF-XRsp4yYl8TQpoaVwT8tghU799XyCaXe0QVVzn9JPTkMYPkiJft0CbsO1lY2eNrbz6CCtMrcamSCupCLuX9Jv6cEGafdpTMpiwEh-tHXHmIEj6C7ONbktD-3pG7bGhY_Qu2KYfnWugrzlwBKjbaxwhgfqmNthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: دو نظامی آمریکایی کشته شدند و یک نفر مفقود است
پست سنتکام، ترجمه ماشین:
بیانیه سنتکام درباره نظامیان آمریکایی جان‌باخته و مفقودشده
تامپا، فلوریدا — در ۱۷ ژوئیه، در حالی که فرماندهی مرکزی ایالات متحده (سنتکام) و نیروهای شریک در برابر حملات موشکی بالستیک و پهپادی ایران دفاع می‌کردند، دو نظامی آمریکایی در اردن در جریان عملیات کشته شدند. همچنین، یک نظامی در حال حاضر مفقود است.
چهار نظامی آمریکایی برای دریافت خدمات پزشکی به بیمارستان‌هایی در اردن منتقل شدند. آن‌ها از آن زمان مرخص شده‌اند. سایر نیروهایی که به‌دلیل جراحات جزئی تحت معاینه قرار گرفته بودند، به خدمت بازگشته‌اند.
سنتکام از سر احترام به خانواده‌ها، تا ۲۴ ساعت پس از اطلاع‌رسانی به نزدیک‌ترین بستگان، از انتشار اطلاعات بیشتر، از جمله هویت رزمندگان جان‌باخته، خودداری خواهد کرد.
CENTCOM
پیت هگست، وزیر جنگ آمریکا، در واکنش به کشته شدن دو نظامی آمریکایی در حملات جمهوری اسلامی در اردن در شبکه ایکس نوشت: «خدا نگهدارتان، قهرمانان. فداکاری شما فقط عزم ما را راسخ‌تر می‌کند.»
پیش‌تر سنتکام خبر داد دو نظامی آمریکایی روز جمعه ۲۶ تیر در جریان مقابله با حملات موشکی و پهپادی جمهوری اسلامی در اردن کشته شدند و یک نظامی دیگر همچنان مفقود است.
سنتکام افزود چهار نظامی مجروح پس از درمان از بیمارستان مرخص شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 469K · <a href="https://t.me/VahidOnline/77247" target="_blank">📅 21:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77246">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/863eecb938.mp4?token=khJkHuEHHYaju5Qp578gpO5IUdirinY-hkcyLQQ-GySkG2nhyyRq9tvMXpGqRvAB744WH0YyiaLPmPlm0PrPMnoLKWTw-B07nULqcoyUIYLs3uN4Sor7PtUDXq_mzgFPaE0vCfLjaDepOdMzHHh6pqlPWAInD6jWYqYc6pl2avcrmgA7pdQuts7oWii30Kwxl60BP_iQ2KPd9mJZCl2bdTG8VsxkMufxcYuDlGRpq2bv5rpnpUQ7gnfJcb08mswHesdAJQY2I3AZJ7YSWO8Nlttpk04T5waEHVOiSRm5eSZPe7cP54fL7Mx6eLfFCT4CVLRjEc50m8YAqy9BH0A2xrhYEcMiwmqEaNxgvs-LzP08q_qUL6JXerCt6sOAVSiBviI69pYZX0TzJyhD5GPWHJKtPl-Dn3krk5T0yvEOJdkSPP6HrZ-sulJGeI7I7k4IQ2ak09i4FDSrOsPiwD9LTM0t7PXmU49SlYyk-ftGbsSdJDQp2vFfNLJW318FsO_lw9HsyUS4BBWhiUKGvbN6OYZdG1_54_hFgq9EsstryXbevb9jZohZAOnh3GyzV86oYAvP3wdY16X-UuDlbESDAHVKX14FkauVvyNNp-xyFIx31H9WitX_jwRF3-TxB7IFqAHp9eK6cvoxwuv9vg_3e-IzV-m3OJtD2g5N3990rDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/863eecb938.mp4?token=khJkHuEHHYaju5Qp578gpO5IUdirinY-hkcyLQQ-GySkG2nhyyRq9tvMXpGqRvAB744WH0YyiaLPmPlm0PrPMnoLKWTw-B07nULqcoyUIYLs3uN4Sor7PtUDXq_mzgFPaE0vCfLjaDepOdMzHHh6pqlPWAInD6jWYqYc6pl2avcrmgA7pdQuts7oWii30Kwxl60BP_iQ2KPd9mJZCl2bdTG8VsxkMufxcYuDlGRpq2bv5rpnpUQ7gnfJcb08mswHesdAJQY2I3AZJ7YSWO8Nlttpk04T5waEHVOiSRm5eSZPe7cP54fL7Mx6eLfFCT4CVLRjEc50m8YAqy9BH0A2xrhYEcMiwmqEaNxgvs-LzP08q_qUL6JXerCt6sOAVSiBviI69pYZX0TzJyhD5GPWHJKtPl-Dn3krk5T0yvEOJdkSPP6HrZ-sulJGeI7I7k4IQ2ak09i4FDSrOsPiwD9LTM0t7PXmU49SlYyk-ftGbsSdJDQp2vFfNLJW318FsO_lw9HsyUS4BBWhiUKGvbN6OYZdG1_54_hFgq9EsstryXbevb9jZohZAOnh3GyzV86oYAvP3wdY16X-UuDlbESDAHVKX14FkauVvyNNp-xyFIx31H9WitX_jwRF3-TxB7IFqAHp9eK6cvoxwuv9vg_3e-IzV-m3OJtD2g5N3990rDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پیامی منتسب به مجتبی خامنه‌ای، سومین رهبر اعلام شده جمهوری اسلامی، او با اشاره به نقض تفاهم‌نامه میان ایران و آمریکا تاکید کرد که این اقدام بار دیگر «بی‌ارزشی و نامعتبر بودن امضای رئیس‌جمهور آمریکا» را نشان داده است.
مجتبی خامنه‌ای همچنین، آمریکا را به «جنگ‌افروزی» متهم کرد و نوشت: «اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبروئی بیشتر است، بداند که ملت عزیز ایران و جبهه مقاومت، درس‌های فراموش‌نشدنی برای او دارد.»
@
VahidOOnLine
متن پیام بنا بر فایل PDF منتشرشده در منابع حکومتی:
پیام رهبر معظم انقلاب درباره‌ی حماسه عظیم بدرقه آقای شهید ایران و تبیین مسائل مهم کشور
بسم الله الرحمن الرحیم
ملت عظیم‌الشأن و شگفتی‌ساز ایران!
سلام و درود و سپاس بر شما که با حماسه‌ی بی‌نظیر و تاریخی خود در رستاخیز بی‌سابقه‌ی بدرقه‌ی آقای شهید ایران، نصاب تازه‌ای از جلوه‌ی بعثت و اراده‌ی مستحکم هویت اسلامی ـ ایرانی را در قدرشناسی، وفاداری، بصیرت، و ابراز محبت فوق‌العاده به زعیم امت اسلامی و رهبر شهید انقلاب ثابت کردید.
گرمای دل‌های گداخته، چشمان اشکبار و عزم‌های استوار جمعیت ده‌ها میلیونی و ده‌ها کیلومتری در تهران، قم، مشهد، و سایر شهرها و روستاها، دوستان ملت ایران و مردم آزاده‌ی جهان را به تحسین و دشمنان مستکبر ملت ایران را به حیرت و سرگردانی و خشم و وحشت انداخت.
همزمان با این حماسه، نقض عهدهای مکرر شیطان بزرگ نسبت به تفاهم‌نامه امضاشده بین رئیس‌جمهوران ایران و امریکا بار دیگر این حقیقت را به همگان ثابت کرد که امضای رئیس‌جمهور امریکا چقدر بی‌ارزش و نامعتبر است و زورگویی، تمامیت‌خواهی و وحشی‌گری، اجزاء لاینفک مرام و مسلک امریکایی می‌باشد. امروز شیطان بزرگ بار دیگر چهره‌ی واقعی و بدون نقاب خود را آشکار کرده تا این تجربه‌ی تاریک از جنایت و بدعهدی، سند محکم دیگری بر دروغگویی، غیرمنطقی و غیرقابل‌اعتماد و پلید بودن امریکا باشد.
اکنون که دشمن امریکایی به دنبال جنگ‌افروزی و تحمل هزینه‌های سنگین‌تر و بی‌آبرویی بیشتر است، بداند که ملت عزیز ایران و جبهه‌ی مقاومت، درس‌های فراموش‌نشدنی برای او دارد که رشادت‌های رزمندگان اسلام و غیرت مردمان شجاع خطه‌ی جنوب در این روزها نمونه‌هایی از آن را نشان داده است.
لازم است به شما مردم باوفا و سرافراز ایران عرض شود که از جمله اصولی‌ترین امور در این برهه، اصرار بر وحدت کلمه و اتحاد مقدس در همه‌ی سطوح مردم و مسئولان و در تمام عرصه‌ها برای تحقق آرمان‌های بلند انقلاب اسلامی و تأمین عزت و استقلال ایران عزیز خصوصاً در برابر دشمن جنایتکار و حیله‌گر امریکایی است. همان‌گونه که پیش از این مکرراً و مؤکداً تذکر داده شد، صیانت از وحدت و پرهیز از تفرقه و تنازع، اختلافات سیاسی و برجسته کردن تفاوت‌های اجتماعی وظیفه‌ی همگانی است و البته نقش مسئولان و عناصر دلسوز و دلباخته‌ی انقلاب و امام و رهبر شهید در انسجام و یکپارچگی کشور، مهم‌تر و حساس‌تر است.
بر این اساس ملت عزیز، با تداوم بر اعتماد به مسئولان دلسوز در هر سه قوه که تلاش ایشان برای رفاه و سعادت ملت، مشهود می‌باشد، همچنان برای تضمین صیانت از منافع ایران اسلامی، هوشیار و فعال در میدان خواهد بود. ممکن است کسانی با اخلاص تمام و از سر خیرخواهی، انتقاداتی نسبت به عملکرد بعضی از مسئولین داشته باشند. به نظر بنده، در عین اینکه این اهتمام و نگرانی ایشان برای نظام همچون اشخاص خودشان، سرمایه‌ی ارزشمندی به شمار می‌آید و فی‌نفسه امری مطلوب قلمداد می‌شود، این عزیزان که بعضی از ایشان از زمره‌ی پیشروان بصیرت هستند باید مراقب باشند تا این رویکرد، اولاً ظلمی را بر بی‌گناهی روا ندارد که آن خود منشأ محرومیت از برکات و عنایات می‌گردد. و ثانیاً موجب شکست در وحدت و انسجام اجتماعی نگردد؛ که با حفظ این جهات، انتقادها موجب رونق و شکوفایی امور خواهد شد.
دشمن نباید هیچ علامت ضعفی و از جمله این ضعف را از ما دریافت کند؛ که هرگاه ما این مراقبت‌ها را به طور کامل مراعات نماییم، او به ناچار رو به هزیمت خواهد گزارد.
بار دیگر از یکایک مردم عزیز که خود، صاحب عزای پدر شهید امت هستند و با وجود دشواری‌ها و برخی محدودیت‌ها و ناملایمات در رویداد عظیم بدرقه‌ی آقای شهید ایران، حماسه‌ای تاریخی خلق کردند صمیمانه قدردانی می‌کنم.
همچنین از مراجع معزز تقلید، علما، اندیشمندان و نخبگان، فعالان فرهنگی، اجتماعی و سیاسی و از اقدامات و تلاش‌های نهادهای کشوری و لشکری و نیز حضور مقامات و نمایندگان جبهه‌ی سرافراز مقاومت و نهضت‌های پرافتخار اسلامی تشکر می‌کنم. امید است همه‌ی کسانی که در این حماسه‌ی تاریخی به هر نحوی حضور و همراهی و همدلی داشته‌اند، مشمول عنایت و دعای خاص سرورمان عجل الله تعالی فرجه الشریف باشند.
سیدمجتبی حسینی خامنه‌ای
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 445K · <a href="https://t.me/VahidOnline/77246" target="_blank">📅 20:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77245">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/su5PV49B4jj--WEo4A0-SLKW5jmumGK5_Iozw_9_J505pG37vahbE3ViR0afPqCVfJbT-5oZ6jUzt5i-9ouWrp-nW3hR8vafoSsg6xkGT0K8Tr_m9uh3-PqrPU5SpTfEabDFaAh-QYY9EfJObzqOAyLiKE27EJMy3UfPSPrVHpYA4ZRJCviRpBTGSuyG1f7e-Ic2ckBEboDEiiubBJDZu3Y5Pd82hVqvf_adShrlVDjhIp83MfUSvg8Cdisi6N5wqMp93n2EYWC3ZOZD-g3mncOsmxhLni8NUcVn97tf2UWvwpLCFmcftnuUv5ky5XeBo1snJDEqb1HWxE_7RWcF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران به نقل از استانداری هرمزگان خبر دادند طی ظهر تا عصر روز شنبه چند حمله موشکی به حوالی شهر سیریک در نزدیکی تنگه هرمز انجام شده است.
استانداری هرمزگان اعلام کرد: «در ساعت ۱۲:۳۰ و ۱۶:۳۰ و ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله نظامی دشمن آمریکایی قرار گرفت.»
در این بیانیه آمده که «هیچ مصدوم غیرنظامی» بر اثر این حملات گزارش نشده است.
سنتکام، ستاد فرماندهی ارتش آمریکا در خاورمیانه، درباره چنین حملاتی به ایران گزارشی اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 441K · <a href="https://t.me/VahidOnline/77245" target="_blank">📅 19:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77239">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S3tiAhM2JPaGBPwlqiQm6Y9WDjFRJdnVkz1Bj9j-H8tgERlR0S5smyyQQqr58zqnM4qBD6Op_S92ktErsZqhrcPAPV8pR05pWMLRSFMlY073PNxX_ULQLcImKaIbeYc0EqAUdaBiMPAYdWGf_zuKFqMwY_mCEO7g8i3wJMIUJ7k2Iav9iwR12zfCq1KDxFWQwjXCl8woUWZuVET1luPR5Ggwd_dr9-Ql2CXpVnHqiisJBAEpZYJt0_VA0qEQzIucQbfbi5naurUBzK8LO7GI48kQmhNq7kfe023Y377jhDC6biCaDRf0EKhhxGNf3vIDG21bFSDuLxEXSSShAy1IwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PC9krbI23OCt2FW4Y8YS8Lykkb9natRHaGd0h6HAH2xT9hHDNx33GF8zmvvBFGKcAaFSCk30LnityZTt7mHDOuXxKgP49hJc1L4shdZqEhWNdqGdV2XPCHUIhdyN_un1DWOZOhhBwBDfQkdNgGg1dlxJJI7v7ULa_pEXvsviVzPDc3wHSfJsvdlfo4WROBQ9H_Pgnu5AS3OCzgv3vB-eBgkW4GYuOC2a2AZPMFp93nn2N02ZAWaf-Yh2cZRTIJ1pSLm4vQqokirI6HctJUEACWECeU90xowSxN7_pVHDLXlyNafKWlfGGS9l3vLiMTUKYwZJorR3I3iNv6TZjKm2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/d16AyIk2BVft111PxdITFwJrm9_sg7zXOaL60oMdEDZa9zNOKhf7cwzIQfuVvXb2008cEKFx-HVSQAvCiJNNObfz5qXV6-iEwT2IFRV8ql0zagsBkLzqoZhDGHszPIdx-2KjsSVOMxpZvZyBt39XmDKgZlBBnJSs0X2grsNUoBGZuKLwEPRqGqNYTupKjWjqrHgZEjvK-q2xyHHSMiiIuqO0UOmso6T5957wbRWnteQeIt-qEbBSMCqUirhhmOg7Tmy51ZjvylyOKZkftDJhbkulAFMHtHLMvRx4DIc-EAnjbRRuwfH2aO5QeacgXPNfWK0caP_RcKmO7fhxM-fAog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VYpu-OkxjTj2A2aMZ4r0tYA1PAMMLaqbQ-o6G0ZrOBhnDkVfBFTdqdddTyUG8cmhhM09-YTV5ss0kvjn2v_KqsAZoUbZex8slf_9Z12soy6sbJspbdL1g3aOEsBwrB4K6YlWQW0W7TEqCr8HXOlpZ52HTAx71r0wJupUfhxlGy5-n6qx2zesB5rvvlK_2hf_I4nUOmPKn7jPj6bvrcE5KhQqCx0RDNbi1knbXJokYbpot-3P0mk4QQxcQF3cCm_ZHFqi4zTnTHX7u0B5mT2q5U9VMlxq-UfuDwEARPmsLiAlBMrnOc9sZ9Sr9eVRwmNO3Dvx3nBEsusDaQA7B0nr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/thHCZLZ7V_bcppox6uaXWADuH-HTglYFcbibHTo8etO7yerQPc6kOkFfzKt7iaxKkUB5HYQ3U2H6F9ut0Oxq37Qe4H1ImggKD74WEKa3DVVZbywHNW9QAzVSPVVmSmjgkg2hcZwd9cFsKBAyVOJtGJdyufE59Fr4Z_LShiNf9R9f4wFHbUYYypOLgmegGpdkfTj7z_l-E4K5pMPgIq3GaCphyVp7-WB5DAT3WFIIR8kcqTlvuR2IkTTm7Zmmf8n9Fi-htb1VS4Zwax0aHMwmVcJG-4OIkbkbTdpFIWUGAkkkrJnGw8liBqLn4nNYMqf78uoa4OslpWHiqTvJTGlihw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lfrZ6MiYVUTWIdNsMfxSuY3lg4sk1eWIrJwCgYUuJQi626l03usXAMTR1RLKCrNSiHnggTNb06uuPM4kN72xU9Eetui7SZ60m3kABKvsptErOS84Y5dVBbwzPKbVU-IcrWoQbEjRGq0Nc4Q8j1FJwJIS8pSKJPwesVGxLgVNRe-d2xPlvlAuzmcpZ7zkq8mUsMDrNyTVlhWS8Zey_au7URwPs5KarcH1Sdo58WBDz6KJ30yEZNq8SDEuEujBxUt0sFagqk8O5Ng4zku2LCGCAnfLyeYNwIAMwsNeP__1v81ovApVU42PRgI1zDCFBs96GbYb8VMjlUR4iEqUYtbYWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ارتش جمهوری اسلامی ایران اعلام کرد در ادامه عملیات موسوم به «صاعقه»، پایگاه‌ها و تاسیسات نظامی مرتبط با آمریکا در بحرین، کویت و اردن را با پهپادهای انتحاری هدف قرار داده است.
روابط عمومی ارتش در بیانیه‌ای مدعی شد در مرحله پانزدهم عملیات «صاعقه»، پهپادهای انتحاری «آشیانه هواپیماها، محل استقرار جنگنده‌ها و مخازن سوخت» در پایگاه شیخ عیسی بحرین را هدف قرار داده‌اند. این بیانیه همچنین از حمله به چند پل ارتباطی در بحرین خبر داده است.
ارتش جمهوری اسلامی ایران پیش‌تر نیز در بیانیه‌ای درباره مرحله چهاردهم این عملیات اعلام کرده بود که «چند پایگاه و تاسیسات نظامی آمریکا در کویت و اردن» هدف حملات پهپادی قرار گرفته‌اند.
بر اساس این ادعا، انبار مهمات نیروهای آمریکایی در اردوگاه العدیری، ساختمان‌های ستادی و انبارهای مهمات پایگاه علی‌السالم در کویت و همچنین مخازن سوخت پایگاه الازرق در اردن هدف قرار گرفته‌اند.
ارتش کویت حمله به چند مرکز نظامی و تاسیسات حیاتی این کشور را تایید کرده است.
ارتش اردن اعلام کرد سامانه‌های پدافند هوایی این کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده بودند، رهگیری و منهدم کرده‌اند. به [ادعای] مقام‌های اردنی، این حملات هیچ تلفات جانی یا خسارت مادی به دنبال نداشته است.
@
VahidHeadline
روابط عمومی سپاه پاسداران انقلاب اسلامی، روز شنبه ۲۶ تیر ماه، با صدور بیانیه‌ای اعلام کرد «اسکله پشتیبانی سوخت ناوگان آمریکا در بندر الاحمدی کویت» را هدف حملات پهپادی و موشکی قرار داده است.
بر اساس این بیانیه، در این عملیات «محل تجمع پرنده‌های جنگی» آمریکا در پایگاه شیخ عیسی و «مرکز داده‌های اطلاعاتی در بحرین با عنوان باتلکو» نیز مورد اصابت قرار گرفته‌اند.
در بخش دیگری از این اطلاعیه آمده است در جریان این حملات، «یک مرکز سیگنالی و مخابراتی آمریکا در کویت» نیز منهدم شده است. سپاه پاسداران در این گزارش بر «کنترل قدرتمندانه تنگه هرمز» تاکید کرد.
پیش از این، نیروی زمینی سپاه پاسداران در بیانیه‌ای ادعا کرده بود، مرکز پشتیبانی نیروهای زمینی آمریکا در منطقه عریفجان کویت را هدف قرار داده و این حمله منجر به کشته شدن چند نظامی در این مرکز شده است.
@
VahidOOnLine
وزارت برق، آب و انرژی‌های تجدیدپذیر کویت، روز شنبه ۲۷ تیرماه، اعلام کرد پس از حمله نیروهای مسلح جمهوری اسلامی به یک نیروگاه تولید برق و آب‌شیرین‌کن در این کشور، آتش‌سوزی در این تاسیسات رخ داده و چند واحد تولید برق در پی این حادثه از مدار خارج شده‌اند.
وزارت برق کویت روز جمعه نیز از خسارت و از کارافتادن یکی دیگر از تاسیسات تولید برق و آب این کشور در اثر حملات جمهوری اسلامی خبر داده بود.
@
VahidOOnLine
ارتش کویت در بیاینیه‌ای اعلام کرد از ساعات اولیه روز شنبه ۲۷ تیرماه، موشک‌های بالستیک و پهپادهای «متخاصم» را در حریم هوایی این کشور شناسایی کرده و آنها را رهگیری و منهدم کرده است.
سرلشکر سعود عبدالعزیز العطوان، سخنگوی وزارت دفاع کویت، در بیانیه‌ای که نیم‌روز شنبه در ایکس منتشر شد اعلام کرد «تجاوز» جمهوری اسلامی همچنان ادامه دارد و شماری از تاسیسات نظامی و امنیتی، همچنین زیرساخت‌های حیاتی و غیرنظامی این کشور را هدف قرار داده است.
به گفته این مقام کویتی، این حملات تاسیسات مربوط به بخش‌های نفت، برق و آب را هدف قرار داده و موجب آتش‌سوزی و وارد آمدن خسارت‌های گسترده به شماری از زیرساخت‌ها شده است.
ارتش کویت افزود نهادهای مسئول عملیات اطفای حریق و تعمیرات را آغاز کرده‌اند و در جریان این عملیات، شماری از نیروهای آتش‌نشانی و کارکنان بخش نفت هنگام انجام وظیفه مجروح شده‌اند و تحت درمان قرار دارند.
در این بیانیه همچنین آمده است رهگیری موشک‌ها و پهپادها باعث سقوط بقایای آنها در چند نقطه و مناطق مسکونی شده و خساراتی به اموال وارد کرده است، اما هیچ تلفات انسانی در این مناطق گزارش نشده است.
ارتش کویت در پایان تاکید کرد نیروهای مسلح این کشور با آمادگی کامل به انجام ماموریت‌های خود ادامه می‌دهند و تمامی اقدامات لازم را برای حفاظت از حاکمیت، امنیت و ثبات کشور در دستور کار دارند.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران، به نقل از یک مقام امنیتی جمهوری اسلامی نوشت اگر آمریکا به زیرساخت‌های غیرنظامی ایران حمله کند، فرودگاه‌های دبی و ابوظبی و بنادر فجیره و جبل‌علی باید فورا تخلیه شوند.
این مقام امنیتی گفت این هشدار با هدف حفظ جان شهروندان در برابر حملات متقابل جمهوری اسلامی، صادر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/77239" target="_blank">📅 19:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77232">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KkSXp717LD-QrKEW6aPvEd9_oTkn4wSbElv6dyXzf6YyiVEvKjEw37IjUpgy8cCSClYrOQgjVXpOgSTzEW5Fi07KuP1qM_RYDlwsviWho3-glQ4_pegQE9C0xMUvGbnqMv4r5KR46xdY1ZCOMyXYrvb6zdIHrvYrZnMhceVyFuF0Cpf4jc_003_RsOl-YRPEmuwTDloISUKkZ2QYtv1lPBOnT7pWyb3cUZ7tvUJPcnJYyhjganMEHzybxsqwfRdqSQDhIGaWWZ1zlYc9UoCUK3qsYNG7isxMYIj_5Yx2r40xv_4Nr7vGC5briiFmkdRRh2yg5LEfXQdlnX4vc4jLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lgbvc_z68Fn0TtEc5CixjnWprPPlm7hzpvNSTOkoh3t_sHC5_CEdujwg1uq22XAeXbahoEgQt5M4phikc8TpoYJKbVaotITpujdgB78uApMfcSF4tm44aKrySbX7O552GYIoucGgbzaM1el0fJqDSK2uNyRgQo_K7xAJf6wqWR_NvqJbkR7gHgVRQSiAtWe9VakTDTc2B0VZ_qSyNqvE3J8sMG4d3LBwgNYLBzLbDJ0bABii6jc-vUgra07nkpIhnavxd3PHpG_JVT19Ogq_CA00R4x3GKlCA-BXSvpQYXm51i6U6j4eg9_fi5V6DYnYTy-Wu472Sot20Pisze3b4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ahu9pZoakKZGnkpQMfX10RD-kzL9Nv7mVaZ8IYDRpN_Ilhl1HWdXWWVEsSarLzk4cbHDrA7Sdcr-vUYUnerzIYkJq4AYF2oHHtFHXGlg5Jhi9zAkCnU-QBa7E293ESdk2PXw_WsmlHUnKxod-mneZBmOUnpdL3hg36F8Btavo8lLhQ0Y2Mcgs9t1SiYSP6xq-AnQt-iikB6vMjNY2z00lXsGXan6aWlwmV-dmSb7L1OYh0BW4JVJUWjHHoEqnI211oCVxZfd3l5sUWgBXOobTCFCqrE1riLwcAXLYb7n0YilkIYMUOXZWBcYQ-TqEqpvGfVEfHXoAXS_oU_zzruUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XQ0qSOgwTc4FEoSBqGpxdKEFwkUFoH_RUVQ06zcAAzK4wUrgBAX7okwHjZXQBUEHUH0LniHiyqiItp23O3tPV_1BpI-n916ukUQ4qYA6YaWGLI0ozZyPFerA8afRIc8wZpKS609wRdcwR8byZssafyUP7vsMkEfDdwHR0ong7ENCvxMPTp3ixYup2yXpZRYWsGfediwv4zFxNS8vFWK-f7IPkWAU7f1rzQaE3IW-WD6s4D6Z4cc5AmObeyl7JSlZ89DPGhSU-fYPPFuPcz86PKgVSU-U9usu3VFCjbZbwYiZx03rIowElFMKTfSfk4NLDGwq_PVd_qHeJDxuspVOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iqry-Qet5A8g0M1mJi7Qx2P7qf1-3SQeNPfjbJMyMoi5jvKkuK69sQLTFyXBxaihJWUPjexsr7a1vpVUT1k2VIPRJhj8ViWEndAfAD1hrfHpI3B8tz7A6fjlvo0LTxtJKXzjp7P7QRbOxl7EbjRTVxN9so1gm9Wzs8MvMh_boodFbNi1QuX3v00hLZPSWf8q_vfR6sBJ4N-WDQY8WSF1hJfbYX4oj36Z-jPpNKGkJK-s8X5X5wXFinu3MofpQ8RoJ1McashktOqU7DG1nRwS0muTkPXDxPYqtJIc6BxxlKeXJznyF6Qt6zm38Jc26wuNHtuNJCsZQ7E5X_LmKdw3hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/i6KRPZdLGdglewNn9jcwBpTp6gMIm-b_6tWcV73lWnnhQIeneDDoHYHFhK8_iFcwrNfIa7xkru19_8BKIGyTDzr6oGG8aFAUztEzIvMG_XFks5DN4hO_j_yBQEAM3FvyS3v5wF_2alhsEzjdyZt2B9ozW3-r48-ygsA_sAbJioWBEv6Wm8qIgvM07UOZtSOlxwMhGLiBeDrsEpguOVfrILrVdgjBzjoalSLXgZ6ySyKVJehhO5qqHiI1wAH7YHa6cCMemhsfzIG7aDJMN22tv8V3bHvvSq9sHtmKlHz2Cghy7In9rSt7-wQFAZVfo-twB347TzbRds7o09CC9M3MVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با پایان هفتمین شب حملات آمریکا به ایران، مقام‌های جمهوری اسلامی از وارد شدن خسارت به بخشی از زیرساخت‌های حمل‌ونقل، آب و برق استان هرمزگان خبر دادند؛ حملاتی که به گفته مقام‌های محلی، باعث انسداد موقت برخی مسیرهای ارتباطی و اختلال در خدمات‌رسانی شده است.
احمد کرمی‌اسد، رئیس پلیس راهور فراجا، اعلام کرد در پی حملات بامداد شنبه ۲۷ تیر و همچنین حملات چند روز گذشته، بخشی از مسیرهای خروجی استان هرمزگان به سمت استان‌های فارس و کرمان به‌طور موقت مسدود شده است.
به گفته او، پلیس راه و سازمان راهداری در حال تلاش برای بازگشایی دست‌کم یک مسیر عبوری هستند. کرمی‌اسد افزود در حال حاضر تنها یک مسیر فرعی برای تردد خودروهای سواری از بندرعباس به سمت فارس و کرمان فعال است، اما تردد ناوگان سنگین تا اطلاع ثانوی امکان‌پذیر نیست و بازگشایی کامل مسیرها به پایان عملیات ایمن‌سازی و ترمیم زیرساخت‌های آسیب‌دیده بستگی دارد.
استانداری هرمزگان نیز اعلام کرد حملات شب گذشته به چهار نقطه از محورهای ارتباطی این استان خسارت وارد کرده است. بر اساس این اطلاعیه، تونل شهید میرزایی در مسیر رفت و برگشت، پل رودخانه شور در محور بندرعباس–سیرجان و دو پل در محور سه‌راه میناب به سمت رودان هدف حمله قرار گرفته‌اند. استانداری از شهروندان خواسته است تا اطلاع ثانوی از تردد در این مسیر‌ها خودداری کنند.
هم‌زمان، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان از اصابت چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در شهرستان جاسک خبر داد و گفت در پی این حمله، آب چندین روستا قطع شده است. تاکنون گزارشی رسمی درباره میزان خسارت یا تلفات احتمالی این حمله منتشر نشده است.
خبرگزاری تسنیم، نزدیک به سپاه پاسداران، نیز از آسیب دیدن دو پل در محور بندرعباس–رودان و همچنین هدف قرار گرفتن دکل مراقبت دریایی جزیره لارک خبر داده و نوشته است که در این حملات چند نفر کشته یا زخمی شده‌اند، هرچند آمار دقیقی از تلفات ارائه نکرده است.
@
VahidHeadline
مدیرکل ارتباطات هرمزگان اعلام کرد در پی حملات دیشب آمریکا «۱۱۶ دکل مخابراتی» در این استان از مدار خارج شده و ارتباطات مخابراتی در بخش‌هایی از شمال بندرعباس و شهرستان حاجی‌آباد دچار اختلال شده است.
احد قویدل روز شنبه ۲۷ تیر با اعلام این خبر افزود در حال حاضر تلفن ثابت، تلفن همراه و اینترنت در برخی مناطق شمال استان با قطعی مواجه است که علت آن آسیب واردشده به مسیرهای انتقال ارتباطات در محدوده تونل میرزایی است.
بر اساس این گزارش، «مسیر انتقال دیتا که با کمک فیبر نوری از بندرعباس به سمت حاجی‌آباد می‌رود، شب گذشته زمانی که به تونل میرزایی و پل رودخانه شور حمله شد، دچار مشکل شد».
@
VahidHeadline
سخنگوی وزارت بهداشت جمهوری اسلامی اعلام کرد در حملات هوایی آمریکا از ششم تا ۲۷ تیر، دست‌کم ۵۰ نفر کشته و بیش از ۵۰۰ نفر مجروح شده‌اند.
حسین کرمانپور، سخنگوی وزارت بهداشت گفت پنج زن و دو کودک و نوجوان زیر ۱۸ سال در میان جان‌باختگان این حملات قرار دارند.
به گفته او، ۳۲ زن و ۱۸ نوجوان نیز در جریان حملات مجروح شده‌اند.
سخنگوی وزارت بهداشت افزود ۳۷ نفر از مجروحان همچنان در بیمارستان‌ها بستری هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 439K · <a href="https://t.me/VahidOnline/77232" target="_blank">📅 19:06 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77231">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iHTw3nhxUQdWR1NPXOZuY4pm2620IMciAfIOJ1QaNZQGrm-yOglP55InHsWjOBuhy6N-F4wyY9Et8qIsDK5gwZcBmhoV4KPt9uB_5F7JNrcEwPP7razcuxtwvC0AYHovpCU0kCRWqlNRiIu0mN3zrE3cbghUS3KOMNesrBUDvjtuO0Mv99dEqAzKn3pcPpi6HWDZF2PmVrAeREuCQZ7TLADYaI8uBxpM7pyn6UBpgs7IrZ_RWB0pGV0AHkwykCFFQkfDlJQA_Pu_7ws6MjICcuF35Xg5sMVfFw_EaSK_hMd04kQJwnVoSrOUkvL_r7s8mghBGE6zl2WKZPkmmEZUtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت آموزش و پرورش اعلام کرد آزمون‌های نهایی پایه‌های یازدهم و دوازدهم در روزهای یکشنبه و دوشنبه، ۲۸ و ۲۹ تیر، در استان‌های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان برگزار نخواهد شد.
این وزارتخانه روز شنبه ۲۷ تیر دلیل این تصمیم را «استمرار شرایط ناپایدار در جنوب کشور» عنوان کرد و گفت زمان جدید برگزاری این آزمون‌ها متعاقباً اعلام خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77231" target="_blank">📅 19:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77230">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q-Pot97Imd45IeBe69nYGaE8Rw2nKYF8uiBpfwZg0lIc5hwMfriLsls1J8ByCtIrCfe9JC3ynKfA55TKRIcmx0GqGvm46JfiIEQ0z_9338UgDyBmoeEcDp3BjeTIRcOtXwT3v2RppTYvkFhk9jMz6XkQ-G4A6BzeC_fptDSyZWghNDljyvXhzLcTypfC_BBHc07AVhYNSwqnxPbjw9ZtYH8fc240b9QUotg3au_XWSRM1t7bwWq7Bu2mngw3ywuJtDzjY5vy6SZPARLOgPL23VX84IVRCT6K4GCz6qP_wzqz0dfmIlhNlduwTyT1_S6en7HH2stBeSA5-4luUpUHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس دریافتی: پرتاب چند موشک از استان بوشهر
شنبه ۲۷ تیر حدود ساعت ۶:۳۵
Vahid
آپدیت: ساعتی بعد هم کلی پیام و تصویر از امیدیه اومده بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 489K · <a href="https://t.me/VahidOnline/77230" target="_blank">📅 06:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77229">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=hz1lKV4l5avWcLDVhaGJJFxyJsbQVVUanTCsCe9NmMInyFods4N1LsR2nGc2d5srHmZITZwoYLteS3_qlU7qjHzgOFfno9Bu4HdODD_imisNPF0-cwLXe215fLqbxNtxsYPXQxaGN1WeDlQFAgMw1yz_X3mxlb54wge8wieLYv66bEAgDg_89TPPG7Dy9oGU8ayQmwJieI2nSRyyBu58q8nb6r2yO0e0n9fuB_0PY2J3vdfOlzI_zCJWVNCI5SXtcMeR20LXwCRv9e0dWKDEKJdMbVJbXVhdYi8rQfvilC8f0AC0PRydpypqQWRnHWkiKk2qHNjJ8Gn4VfVawQTNNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4f9ac6ccc3.mp4?token=hz1lKV4l5avWcLDVhaGJJFxyJsbQVVUanTCsCe9NmMInyFods4N1LsR2nGc2d5srHmZITZwoYLteS3_qlU7qjHzgOFfno9Bu4HdODD_imisNPF0-cwLXe215fLqbxNtxsYPXQxaGN1WeDlQFAgMw1yz_X3mxlb54wge8wieLYv66bEAgDg_89TPPG7Dy9oGU8ayQmwJieI2nSRyyBu58q8nb6r2yO0e0n9fuB_0PY2J3vdfOlzI_zCJWVNCI5SXtcMeR20LXwCRv9e0dWKDEKJdMbVJbXVhdYi8rQfvilC8f0AC0PRydpypqQWRnHWkiKk2qHNjJ8Gn4VfVawQTNNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم با انتشار ویدیویی از محل حادثه گزارش داده است که دو پل در محور بندرعباس–رودان هدف حمله آمریکا قرار گرفته و این مسیر آسیب دیده است.
این خبرگزاری می‌گوید که در این حمله شماری کشته و تعدادی نیز زخمی شده‌اند، اما آمار دقیق تلفات و میزان خسارت هنوز اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 483K · <a href="https://t.me/VahidOnline/77229" target="_blank">📅 06:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77228">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lpy67r5hkyJhD2VQk59mGIlhOJm1SA4p-SE1DlCGLvxpuaIF1QV506bD4c57--OWmlAX_USSUedlQIm2S-_RIK1ClHdM98ExFX30lVDBap4AL2QigaDeY4lu3pZDoZczZX3Ah_9pDTzGB6f_Vz26uYX7T67fee87KnwOpuiKieB_y2WqtBbWc9Dvr5BCkBak3irm7aHn9gMV0zNvYb0xdDA28rKpUFfT47ZOlnH9iWaaGHxdEv3PT1duwqS5W6ARYGG8Y4efa0EhMeuSF2ud8P7yagmli6HaOE8sdy1t8-wsCvICgK-uS2OwU4dWTD7jbj9JsgUeqrugUWVOeWhaVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت: نقشه «راه‌های مسدودشده» در نزدیکی تنگه هرمز
شامل دو پل و خروجی تونلی که در حملات هوایی امشب آمریکا هدف قرار گرفتند.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 472K · <a href="https://t.me/VahidOnline/77228" target="_blank">📅 06:28 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77227">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=t7jB1-hD1IsIKE4INSMyGfbybSIC2-QEwcRz0onWDOFam75Pp8KpUUx9xD-iqmfDGWFaaOMG06A33KCTRlTME_p716MDM574nxHrDz1geT5YC_vT82mR49DWvOw1FRXvGOq6WALu5KC7Q7oPoVjQ17fN-Fthq3VyJWGZDMHESgiePEmt26g9hwI3SleAc028_W1lJhbMrQvqS8C6gBdMIG9wSDiNz9-7kW5CHLzS3NhLAQS3QW235RWlYmSmj3SGNfpnPNykmn2kcojDlcfOhsCNeJS8nt_toDBKIj7zEx33dqyI1gOvzYixY4Ei9IhW7cFbkQPysaMoLYB3ZYZHqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c159c5a2e1.mp4?token=t7jB1-hD1IsIKE4INSMyGfbybSIC2-QEwcRz0onWDOFam75Pp8KpUUx9xD-iqmfDGWFaaOMG06A33KCTRlTME_p716MDM574nxHrDz1geT5YC_vT82mR49DWvOw1FRXvGOq6WALu5KC7Q7oPoVjQ17fN-Fthq3VyJWGZDMHESgiePEmt26g9hwI3SleAc028_W1lJhbMrQvqS8C6gBdMIG9wSDiNz9-7kW5CHLzS3NhLAQS3QW235RWlYmSmj3SGNfpnPNykmn2kcojDlcfOhsCNeJS8nt_toDBKIj7zEx33dqyI1gOvzYixY4Ei9IhW7cFbkQPysaMoLYB3ZYZHqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
سنتکام تازه‌ترین موج حملات علیه ایران را به پایان رساند
تامپا، فلوریدا — نیروهای آمریکایی در ۱۷ ژوئیه، ساعت ۹:۳۰ شب به وقت شرق آمریکا [۵ صبح به وقت تهران]، به هفتمین شب متوالی حملات علیه ایران پایان دادند.
فرماندهی مرکزی ایالات متحده (سنتکام) تأسیسات نظارتی، زیرساخت‌های لجستیکی نظامی، انبارهای زیرزمینی تسلیحات و توانمندی‌های دریایی را مورد حمله قرار داد. نیروهای آمریکایی علاوه بر دیگر تجهیزات، از جنگنده‌ها، پهپادهای هوایی و ناوهای جنگی استفاده کردند.
سنتکام به دستور فرمانده کل قوا، همچنان ایران را پاسخ‌گو می‌کند و هم‌زمان محاصره دریایی بنادر ایران را به‌طور کامل به اجرا می‌گذارد.
بیش از ۵۰ هزار نیروی نظامی آمریکایی در سراسر خاورمیانه در حال فعالیت‌اند و همچنان هوشیار، مرگبار و آماده باقی مانده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 473K · <a href="https://t.me/VahidOnline/77227" target="_blank">📅 05:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77226">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پیام‌های دریافتی:
انفجار شدید همین الان خرم آباد
خرم آباد لرستان ۴:۵۷ بامداد صدای دو انفجار شدید
سلام وحید انفجار در خرم آباد لرستان خونه لرزید
خرم اباد دوباره صدا اومد ۴:۵۷
خرم آباد دو صداي انفجار پشت سر هم
همین الان دوتا انفجار  شدید خرم اباد
درود وحید جان خرم آباد همین الان دوتا صدای انفجار خیلی زیاد بعید میدونم اینا شلیک موشک باشه
خرم آباد دوتا صدای انفجار
سلام
داداش خرم آباد انفجار نبود
دو مرتبه صدای شلیک موشیک بود
[پیش‌تر پیام‌هایی درباره شلیک از استان بوشهر دریافت کرده بودم.
آپدیت: پس‌تر هم ساعت ۶ از داراب]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/77226" target="_blank">📅 05:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77225">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U_eLt845DX5ZlNSfLYrHU2rhJHDVSELP08Dw4oGmWGAgpAXAqG3di5Q7bgnLWXUFfKpSq2pkUSifDT_0tz0kwIe5sG5ENfeYo2zOyp1QQcOeFFBizSzNgrsmy4H63xe7UOFB8eT0BOEMwAX5oVbZI54chF_bpwN7rltk2NCUZ9iwEVzsnGtmzdELivur-2-EQdxEpGEn6kUnlkgESR-4TzuiExQaUtoWt8KI_RXAgwhsaLVrHJRdoQPYi4E2dfMCoo4LU_sfGB4Cf1uQevzTNtLhDAgMv4HwkxCP1LTn6ZQCMhVv_VTt7UJYbMeit9M7FS7-uYhJjybhbzyoWgneUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش تسنیم، خبرگزاری وابسته به سپاه، بامداد شنبه، در جریان حملات موشکی آمریکا به جزیره لارک، دکل مرکز کنترل ترافیک دریایی اداره بنادر و دریانوردی این جزیره هدف اصابت قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 417K · <a href="https://t.me/VahidOnline/77225" target="_blank">📅 04:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77224">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mYFiPdLJqC_fMNUT56ZHIuPnOeH3dikUBKwQydXWSgPI3bD6dgr5zbkxspoF60BDfpMG-jOPZddxuGq6ZFetVY9wefBxwAVyPrw0WpLywX71DxOkcokEO2nRLwEDq8G5fJ2VX1oFqf9jP3qduc4SflsjQIfTuj8P4vaEKPGqyCfiy53QgmlqPa2u6F6VzskvFZjYRdsYC_uktKDeh5WeAGIl-rTuFeT2mHInjcWquOn1mQSbeSMjIP3vT0QeFNX2isb6UFaNHGzrc7-W3E6sqVDeLnqadTKAhQKjkhkpLSUup3lIEtRgfvFi5shHY_SCMfzitoAuOCSapXQWvHn8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران مدعی است دو نفتکش پس از برخورد با مین در آبراه بین‌المللی تنگه هرمز منفجر شده‌اند.
✅
واقعیت: این ادعا نیز مانند بیشتر ادعاهای سپاه پاسداران نادرست است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/77224" target="_blank">📅 04:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77223">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پیام‌های دریافتی از ۳:۵۰:
بندرعباس دوباره چهارتا انفجار شدید بود
باز داره بندرو میزنه
۴تا انفجار پشت هم
هفت تا بندر
بندرعباس کلی صدای انفجار داره میاد
سلام بندرعباس
از ۳:۴۸ تا ۳:۵۰ حدود هفت بار زدن
همین الان انفجار در قشم 3 انفجار پشت سرهم
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/77223" target="_blank">📅 03:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77222">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرنگار اکسیوس، ترجمه ماشین
:
🚨
مقام آمریکایی: ایران یک موشک بالستیک به‌سوی یک پایگاه آمریکا در عربستان سعودی شلیک کرد
🚨
چرا اهمیت دارد: این نخستین حمله مستقیم ایران به عربستان سعودی در نزدیک به چهار ماه گذشته است.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/77222" target="_blank">📅 02:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77221">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RKZMeSNjWI7Oxy11Zw2xcjARoo1vmjJ_ZMJyUW9VY_We6AtIW8L5XR9uPqYiDfwBrUilRFSV34nB-y2izDIPJk_FeULhVSg3uw7_GvAfqcYgd-2M6Fibzr3bNLaBp2SqOQ0DWlpgHkgF75fzQraeGzGNBCo1t7ZNQs-G1-nCfKkTJ0870d2BL9hdl-2plZxJsfVQZ-Y_Yy5J6eNi69ylsS3mR_Ir0Mvx013xprJ5d13mGY0gysbHxwM_t4H_6iCRQSHiBUVYG0yt_K2pDGG7uj1Y2Lt5e8ZW-kqw2Wyzjwz_M4kep9qSlTvxn44yCu74H4gGJJqCWUIRvHBdPLjJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر دریافتی با شرح: پل جاده رودان به بندرعباس
شنبه ۲۷ تیر
Vahid
منابع حکومتی:
حملۀ دشمن به ۳ پل و تونل دیگر در هرمزگان
🔹
استانداری هرمزگان: تونل شهید میرزایی در مسیر رفت و برگشت به دلیل حملات دشمن مسدود است.
🔹
پل رودخانۀ شور هم در مسیر بندرعباس به سیرجان مورد حمله هوایی دشمن آمریکا قرار گرفته است.
🔹
همچنین پل محور رفت سه راه‌میناب به‌سمت رودان بعد از دو راهی سرزه مورد حملۀ دشمن واقع شده است.
🔸
مردم از تردد در این مسیرها خودداری کنند. تلاش ها برای ایجاد راه کنار گذر و راه‌های جایگزین در جریان است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/77221" target="_blank">📅 02:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77220">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daa140a498.mp4?token=eSR51wTuONGFfLqI_OZR0yczEtdkKPR65t3a5V-Pp5sBccf56w3lgPWFN-3mGtD3Fykao5tf8tzaUyO_821aDo19OlibM_D6K8U6rTEexnFl54LQArNaZEKkqqH79GSfWJaUt6eclNS8Wxdw3r7inop0aiXlF5phGoYE8RfPQaSTqs-4lJ1F0eDChythmrsc-4XOmLs3iGS6xAFQSyAy6zuRTgFrNKopW4Dxid_7Rc8vSGybKm1EAcuTP1m4WX1q-Z7m6Vs-uoH5ikkSZKm8g3Kfy_o9hOr9qvcXkDA9-mctQqwMuU4B4wZUv2MivSOFGymZZWEWud107bvumXED2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daa140a498.mp4?token=eSR51wTuONGFfLqI_OZR0yczEtdkKPR65t3a5V-Pp5sBccf56w3lgPWFN-3mGtD3Fykao5tf8tzaUyO_821aDo19OlibM_D6K8U6rTEexnFl54LQArNaZEKkqqH79GSfWJaUt6eclNS8Wxdw3r7inop0aiXlF5phGoYE8RfPQaSTqs-4lJ1F0eDChythmrsc-4XOmLs3iGS6xAFQSyAy6zuRTgFrNKopW4Dxid_7Rc8vSGybKm1EAcuTP1m4WX1q-Z7m6Vs-uoH5ikkSZKm8g3Kfy_o9hOr9qvcXkDA9-mctQqwMuU4B4wZUv2MivSOFGymZZWEWud107bvumXED2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
شلیک از خرم‌آباد و زیر ۵ دقیقه بعدش ۲ تا انفجار
وحید جان صدای دو انفجار در خرم‌آباد
زمین کامل لرزید صداش هم مثل ترکیدن بود
تو کانال استان زدن شلیک موشک نمیدونم صحت داره یا نه
خرم آباد زدن
دوتا شد دوبار انفجار ساعت ۲:۱۵ دقیقه خرم آباد
وحید جان خرم آباد ساعت 2:15 وحشتناک زدن
سلام وحید همین الان خرم اباد۲ صدای انفجار اومد
همین الان ساعت 2:15 خرم آباد دوبار صدای انفجار اومد
خرم آباد۲.۱۶دقیقه انفجار
۲ و ۱۵ خرم آباد صدا انفجار اومد
خرم اباد چند بار صدا انفجار اومد
سلام آقا ما خرم آبادیم مارو همین الان دو بار زدن صدا انفجار اومد
سلام همین الان خرم آباد صدای انفجار
سلام ساعت دو پانزده دقیقه خرم آباد صدای دو انفجار
۲:۱۶ صدای انفجار خرم آباد
خرم آباد ساعت ۲:۱۷  دوتای صدای انفجار  اومد
خرم آباد دوتا انفجار پشت سر هم ساعت ۲:۱۴ صبح
همین الان سه بار خرم اباد صدای انفجار اومد
دوتا زدن تو خرم آباد لرستان خیلی سنگین بود
سلام خرم اباد ۳تا انفجار داد ساعت ۲:۱۵صدا خیلی دور احتمالا پادگان امام علی
[ساعت ۳ هم چند پیام دیگر دریافت کردم.]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77220" target="_blank">📅 02:22 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
