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
<img src="https://cdn1.telesco.pe/file/hyiTWxMs7SANLLSPGxjAtdlbglQEM8D7RuYWzs3Nmrj8Rxjl_LRJeon2_jTQWyc3GJIbmWnH8H8gzoT_KphCOWS9WpxztK1B8lesnHNvpY2_yl98KOnZfZ1xsmCBK2tbjZDnagjI4fDGPzI0P9cZ23dp0SzQOieOcJZXKCUNnGGY8kORSAS2KM8fL7L8S7w0yw-CxkHCDBynto406cDwZX5dRvMCo_s_zUwg_nUTgSN6HW2PJT-fsaHbpW7qLFAvWN88YirAmBZmK4ge2-LjPncH-NSxTW-jm9Gxl8SVw79EVuC4eVUjQzjYEpBr-SAsN08OXlcSmWkbEpRptoWyTQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-78062">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aUm4WwSzoOkIvWUuhJukpyDhUzPwPZ0zy9xItZsKXeQtqZq_wnwYWSw4DMxs3VlVB6YkfEg5FOXJNOZzaVF4OUOWbQAXqX1JzE70gPPgstyOZLftyPnw8ZpS-9t_EyemxuUZInP_nUiulu0ZyE1dQ08NI2KNSHwVZfyFRWHQLHl7CXyDCvlcoay3UvbznLDKNITJ5tCldUeqTulqkwhu738mSd2_svnbOTuWGGNYbckjfFbcmC5XoHyhCpYPN4jDcPW2CehL74OOzh8Yu_dloo0jgsOEWnpDAfc8G8PMSG_XgTutsgkwuWWtR3p_-N2dOZzSvqnMn7djYsEtilueIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.
به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم خواند، و در توضیح دلیل آن گفت: «توزیع بنزین عادلانه نیست و تداوم این مسیر غیرممکن است. ضمن این‌که تولید بنزین کفایت نمی‌کند و با محاصرهٔ دریایی آمریکا نمی‌توانیم بنزین وارد کنیم.»
این مقام دولت ایران در عین حال گفت مشخص نیست این تغییرات به چه میزان و چه زمانی انجام می‌شود.
در روزهای اخیر، هم‌زمان با افزایش اظهارنظرهای مقام‌های جمهوری اسلامی دربارهٔ لزوم افزایش قیمت بنزین، گزارش‌های مختلفی از تعطیلی برخی جایگاه‌های عرضهٔ سوخت در تهران و تشکیل صف‌های طولانی مقابل آن‌ها منتشر شده است.
بر اساس آخرین آمار اعلام‌شده، تولید روزانهٔ بنزین در کشور حدود ۱۱۵ میلیون لیتر و مصرف آن حدود ۱۲۹ میلیون لیتر است. به این ترتیب، میزان تولید روزانه روزانه حدود ۱۴ میلیون لیتر کمتر از میزان مصرف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/VahidOnline/78062" target="_blank">📅 19:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78060">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SgJ_4JX1Z1XTWjH5JvZjSzaxsR2pKgkyPb_LDgbPnJeTTV4QztmKQDeoC0i7qJ6bWHAi6Xm8cxlzVH2LU1SDOlaMzLvvhaX22QJOG6sq2CiB3CM6vCwTGgWeJUZzhfTwijfocyeOjwJbPkAr4Si5Kf9lXz27QGUoHp1iV8g-lznSe9zUY393Zo4isqN9X0oGa2H0lBeC-VwLIiTeYpBhrPJ18uSDijjjhiuyM7O1tFrNGf-4n5UFdHnqtHZ6Uw_YcUaWtcvhHzahfqi2wr6nZYs-72EBxcO_rBkagywKKd0O27_ZYUHQLL1ealwDOj0hmVRJoGaCtEfsLatsTyLdKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/brMneZ2xCLMnsQoVk7zajV7sP59OcUt76ro1nqjPfWqRqThcv8r0Rjgp_1w4tM-rlq_qaQU2NEWUGKUKlm3PI80TxXi-ulJYZ0LIMU419dqymJ2rdXbvsrC406J0U0-_tW_F43ZOJA8mPfuHJa1fCOtuwJcGnNG6Hi0JNz_f2fNgGAdq770B0yrdaZ7z_XOtsg8WvJHGCUm6cyMT6zyggx9GtHlMLxPC5qUuePpe7KxmTOjWYsG5IvG6nUI6hW9HZ54fT5J3QIEnCdXjo0ndcXfktWy01RWErA2UuFUBK0WyN0WVgaLJF2ADMWXFlUOUF6np5nfU0kRWXSwJ--TpIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، در سفر به تهران با مسعود پزشکیان دیدار کرد.
وزیر خارجه قطر در این سفر با محمدباقر قالیباف، رییس مجلس شورای اسلامی نیز دیدار کرده و درباره راه‌حل برای از سرگیری مذاکرات میان واشینگتن و تهران گفت‌وگو کرده بود.
@
VahidOOnLine
وزیر خارجه قطر همچنین به قالیباف گفته است که گفت‌وگو بهترین راه برای حل اختلافات و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/VahidOnline/78060" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78059">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j5y8SBwt8MM7MyYNeQEXs0iJjLxskZTRxhbqQwzK_397zci28mbfk_ORsYeWuCZMCCFOiNLxUdQK4FjPPfj4frD-UadM-lXU3FjWc1t2J3oAioYQcKCvNpq4nEV1QW2pQuRq3-W6e7eKPpeZoSISkJxBxXaxkOfuOR0tEwCk3CY21L7kZX6nYrDX6DszQrndI04lbJRdwM4rsqfyu_JFJrLjwj9IjVUu_G8roUakTEyire-WS5rpgkCs3lYeZvpQ388sCeCm1ckduQE3tSvg7p36ZKHH_qykcr9M2rFz1BkIUYRX0ItbGFqFzG6vUbV5DlI0iR-b_GpCzEdiMV7FzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیه رمضانی، زن ۳۹ ساله و مادر دو فرزند، در جریان سرکوب اعتراضات دی‌ماه ۱۴۰۴ در تهران با شلیک مستقیم نیروهای جمهوری اسلامی کشته شد.
ماموران بامداد جمعه ۱۹ دی ۱۴۰۴، از فاصله‌ای نزدیک و از پشت به رمضانی شلیک کردند. گلوله پس از عبور از پشت و قفسه سینه، به قلب او رسید و جانش را گرفت.
آسیه رمضانی مادر یک دختر نوجوان و یک پسر دبستانی بود.
خانواده‌اش می‌گویند پس از تیراندازی، او را به یک درمانگاه منتقل کردند؛ اما بدون رسیدگی پزشکی موثر، برای حدود پنج ساعت در حال خون‌ریزی رها شد.
خانواده رمضانی پس از بی‌خبر ماندن از سرنوشت او، سه روز میان پزشکی قانونی کهریزک و بهشت زهرا در جست‌وجویش بودند تا سرانجام پیکرش را پیدا کردند.
خانواده، زمانی که پیکر رمضانی را یافتند، گونه‌اش کبود بود و از زیر کاوری که پیکر را در آن قرار داده بودند، همچنان خون دیده می‌شد. آن‌ها گفته‌اند پیکر او در شرایطی «ناشایست و دردناک» نگهداری شده بود.
خانواده رمضانی همچنین می‌گویند لباس‌ها، کفش‌ها و دیگر وسایل شخصی او برداشته شده و به آن‌ها تحویل داده نشده است.
آن‌ها پس از تحویل پیکر متوجه شدند قلب رمضانی که با گلوله شکافته شده بود، بدون اطلاعشان بخیه زده شده است. خانواده آسیه رمضانی در روایت خود نوشته‌اند: «ما آن سه روز را فراموش نمی‌کنیم. آن پنج ساعت، آن خون، آن کاور، آن قلب شکافته‌شده و وسایلی را که باید به خانواده‌اش بازگردانده می‌شدند، فراموش نمی‌کنیم.»
آن‌ها تاکید کرده‌اند که همه واقعیت‌های مربوط به کشته‌شدن او هنوز روشن نشده است و افزوده‌اند: «هزار سال هم که بگذرد، خون عزیزانمان پاک نمی‌شود. نامشان را تکرار می‌کنیم، روایتشان‌ را زنده نگه می‌داریم و دادخواه می‌مانیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/VahidOnline/78059" target="_blank">📅 17:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78058">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V94LQAgpAYqeEpxF7T3WCKbSYooREQpzsQMCFSt7db_3y_V4H6mbkpggCZH1B4jxF7UadTLMWZ-VzkMtk-hn_7lLJL6wTOqXY0EsZTf38UWCHt_9CSshYt6poTIWdqO8rvNCuDXwRB4kwBlQygodJqd0SsbiX8u4EqYcIuttiE7TbrDvFOqtA2jjKa_DkzF2FI2yIJwXmnvLNiMLZVdwMN8WIMgOXfwlkRPtMIvygVA7Pf06kREAcGDWU65F90-bdRLXoH25CgS3XWnyH5g3XXaCJ-t8WDKclO01G_k2H88JtVs5i4pxOfGSbGG_uDODK-m1i4keYW7wUh1MvOydhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با انتشار پیامی در شبکه اجتماعی ایکس، با انتقاد از سیاست‌های مالی جمهوری اسلامی، خواستار اختصاص منابع مالی کشور به مردم ایران شد.
بسنت در پیام خود نوشت: «در حالی که مردم ایران برای تامین نیازهای اولیه خود با مشکلات معیشتی دست‌وپنجه نرم می‌کنند، حکومت فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.»
وزیر خزانه‌داری آمریکا در ادامه افزود: «حکومت ایران به جای تزریق میلیاردها دلار به گروه‌های نیابتی تروریستی خود، باید این پول را صرف مردم کشورش کند.»
این اظهارات هم‌زمان با تشدید کارزار تحریم‌های مالی ایالات متحده برای محدود کردن دسترسی حکومت ایران به منابع ارز خارجی مطرح می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/VahidOnline/78058" target="_blank">📅 17:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78057">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/phEwqolq3asebMp4ko8AQvAvE1CO1fE4TLKBl8x2bWv8pald6pEAd9h6i-F5MLXHqnqjHuYv95moWYgBhNgVNlJgu3j5PWTE8cDqapXIyHYOB0Szu-Z20wdAn-T8FkTSazL3nX6DJ923-VTo6dwfZ_krgLbLvSnggZalMPS7JubtLOaHEKdbUnMfOEZuk2dcgWxFZ4Uwr_VLVUtoT7k-NIl7WXYdbRHssKP7eF9eaqwcbmiVXmzlrqgwrrRvzDBS6TrfXOlL1gbW_ElrwiO6aMo3GURBeFJxf40ZUuNG_xONSgEJzBzEKLKojktbaDonbM1kyohfmy8MCeXQfo-iAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت شاخص برنت در پی بهبود وضعیت تردد کشتی‌ها از تنگه هرمز و انتظارها درباره مذاکرات مثبت میان ایران و قطر روند نزولی خود را ادامه داد و روز پنج‌شنبه به ۸۶ دلار و ۷۵ سنت رسید.
قیمت نفت طی روز جاری نسب به روز چهارشنبه بیش از یک دلار و نسبت به هفته گذشته حدود هشت دلار افت کرده است.
در پی سفر وزیر خارجه عمان و فرمانده ارتش پاکستان به تهران طی روزهای گذشته، اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، روز چهارشنبه اعلام کرد نخست‌وزیر قطر نیز قرار است به زودی به تهران سفر کند.
هم‌زمان وزیر خارجه قطر در تماس با همتای ایرانی خود بر حمایت دوحه از تمام تلاش‌های دیپلماتیک و اقداماتی تاکید کرد که هدف آن دستیابی به راه‌حلی برای تضمین آزادی کشتیرانی و فراهم کردن زمینه توافقی جامع برای برقراری صلح پایدار در منطقه باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/VahidOnline/78057" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78056">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W1LPJbQuXjo9D-inU6XHBCQ4RY7zQm3L-pmcgI7fFD9bC9quKPtq5tHe5W5eSexV-op5LpQb6X1Z_ePlqV22bXjcXtPuYK5H0VaErP2qE-5-J2yHlvri1FigGcsJFKYCmSv1jCmfu2uR0pBHbPeXz6itX5a-kfXRbVIDblGTktqbRCs1KtzA8DRlBe0CyTyAhY4v9krdEZ-tREcVO6uzJK3u2rHc5woRTwZcNTU8bdKyakFxlIPVI0RxGpXf9GvKQZb0F6NSJv_S2j1EqjFl99N5WFTpUkyGd9pRqdnnbyxkE1j-GeRuQBZKiY6WKdCIGTt1CTmLDL_H2CaeanKgqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه مدنی، پژوهشگر و متخصص ایرانی حوزه آب و مدیر مؤسسه «آب، محیط‌زیست و سلامت» دانشگاه سازمان ملل در کانادا روز چهارشنبه چهارم شهریور جایزه آب استکهلم ۲۰۲۶، معروف به «نوبل آب»، را از کارل گوستاف شانزدهم، پادشاه سوئد، دریافت کرد.
این جایزه در مراسم رسمی هفته جهانی آب در استکهلم به پاس پژوهش‌ها و فعالیت‌های کاوه مدنی در زمینه مدیریت منابع آب، حکمرانی آب و ارائه دیدگاه‌های نوین برای مواجهه با بحران آب به او اهدا شده است.
کاوه مدنی پیش‌تر در ماه مارس به‌عنوان برنده این جایزه معرفی شده بود و کمیته جایزه، از پژوهش‌های او در مدیریت منابع آب و پیوند دادن علم با سیاست‌گذاری، دیپلماسی و ارتباطات عمومی تقدیر کرده بود.
جایزه آب استکهلم از سال ۱۹۹۱ به صورت سالانه اعطا می‌شود و مراسم آن را بنیاد آب استکهلم با همکاری آکادمی سلطنتی علوم سوئد برگزار می‌کند.
این جایزه که شامل یک میلیون کرون سوئد و یک تندیس کریستالی است به افراد یا سازمان‌هایی اهدا می‌شود که دستاوردهای برجسته‌ای در حفاظت، مدیریت و استفاده پایدار از منابع آب داشته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/VahidOnline/78056" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78055">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rVGYkX3exlZpeDPy6DzI4ym3ToX1MVpiykeG7_FnEXGs6GmDUVTt9jAWHceG_h3VCFR-Ke6rXf7ZZHRentb4smwpG4xqGlmRZOINw9mdvqsG_0nxVBZ9FaHZ1rePvhPoMr_9FXI0tgUq4RZ24IBxwiqZUOqrmsFM9j6ZRLWGo2YaUzHT2tqtKAHpSv3LQBtJ4Ccfv6Oxj9YvpnMCcBhAVxkVR0fGYbgtsVTPPhitM130wGj-JjwkBEzwjMJazrk3sUtqm1x8SA51N1BHfidobk6w-EYlFhgPzLm1cXlpCLC61158RaJCivp2u7Wa_3u-3b_RXxfWGNUcvdQAgv-5NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلا ابوالحسنی، از بازداشت‌شدگان اعتراضات دی۱۴۰۴، به اتهام «محاربه» به اعدام محکوم شده و پرونده او پس از اعتراض به حکم، اکنون در دیوان عالی کشور در حال بررسی است.
لیلا ابوالحسنی، حدودا ۴۳ ساله و مادر دو نوجوان، از ۱۸دی۱۴۰۴ در زندان دولت‌آباد اصفهان نگهداری می‌شود.
یک منبع گفته است که ابوالحسنی روز ۱۸دی در شاهین‌شهر و هنگامی بازداشت شد که در حال عکس گرفتن از آتش‌سوزی یکی از فروشگاه‌های «افق کوروش» بود.
به گفته این منبع، دستگاه قضایی او را به دست داشتن در آتش‌زدن این فروشگاه متهم کرده است؛ اتهامی که به صدور حکم اعدام علیه او منجر شده است.
در حال حاضر، دیوان عالی درباره اعتراض او به حکم اعدام در حال بررسی پرونده است.
لیلا ابوالحسنی از زمان بازداشت تاکنون، بیش از هفت ماه را در زندان دولت‌آباد اصفهان سپری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/VahidOnline/78055" target="_blank">📅 17:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ukW1WfKgAiYCAKW-pCqn6lIGw7ASokSxfxnFZvVcoXb0Yspo-pJW63f0uFJzx0aIcTdy3YixMgPlO9Jj9trTHR7yf52MnXNcHJdgooosB_zic7_azEHQwiLzyHXplqD5IbUDEPC-1XA92jVKQuvMwWfKoQ-BgUecQfOB9JvUqCoFNtPb4hbPEXFAgZiGmyv3g5EEPz4O-QZn4gCf_2Ce-whPLeSyu6GP14Pzk_E7GGKnr93CBjm9zEm4GQaCrLeWqUlpIS7TxNpXJrLwOtu8rC8Pz0U4J1s8SVsIJxBZHMpYZtolnHeqPSNyLMn9yk4zHEEcutT-VgZKRuPZqHpE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
مقامات محلی گزارش داده‌اند که یک نفتکش با پرتابه‌ای ناشناس هدف قرار گرفته و در پی آن کشتی دچار آتش‌سوزی شده است؛ آتش‌سوزی از آن زمان مهار شده است.
گزارش شده که همه اعضای خدمه سالم هستند و حضور همه آن‌ها تأیید شده و هیچ گزارشی از پیامدهای زیست‌محیطی دریافت نشده است.
مقامات در حال تحقیق درباره این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78054" target="_blank">📅 05:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=eXwzhXttQg0GIAjOaR8bHP-_ijCy-iGDePHiDfXDXC-nPGJLkM0ruE62ugV2gkS6yqANHf8Ms2iaQ-VQi8y32CqjdOma7rbG2qk8T13CK2-0CY8eglqwdj-ZZd8a9PQ3MCId7-ctzdJv6kTfDAt5GQkGxx0E4E3RnA4svwro1aBsUn_wO26Vsbf38i72vRUF_GB75Qlk8gb1BYKGOFTrIJfYApMQh_Uf9B4anasynf_LXcc5n0b5vhsLN_XecaTDp2IPWXHb5YFg1N88npo7AFrOFgcTZgav1ERsC_fCC74WmAK1ao46lkGFLVfty2b_GMDSjMDuaY8PPtfmTC_uSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=eXwzhXttQg0GIAjOaR8bHP-_ijCy-iGDePHiDfXDXC-nPGJLkM0ruE62ugV2gkS6yqANHf8Ms2iaQ-VQi8y32CqjdOma7rbG2qk8T13CK2-0CY8eglqwdj-ZZd8a9PQ3MCId7-ctzdJv6kTfDAt5GQkGxx0E4E3RnA4svwro1aBsUn_wO26Vsbf38i72vRUF_GB75Qlk8gb1BYKGOFTrIJfYApMQh_Uf9B4anasynf_LXcc5n0b5vhsLN_XecaTDp2IPWXHb5YFg1N88npo7AFrOFgcTZgav1ERsC_fCC74WmAK1ao46lkGFLVfty2b_GMDSjMDuaY8PPtfmTC_uSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح: رسانه‌های فارسی‌زبان در بانک اهداف نظامی ما جای می‌گیرند
1:11
سخنگوی ارشد نیروهای مسلح جمهوری اسلامی،  در مصاحبهٔ تلویزیونی با خبرگزاری «دفاع مقدس» مدعی شد رسانه‌های فارسی‌زبان خارج از کشور مستقیماً به «موساد»، «سی‌آی‌ای» و «سازمان‌های اطلاعاتی دشمن متصل هستند».
به گفته ابوالفضل شکارچی  «نیرو‌های مسلح جمهوری اسلامی به این بنگاه‌های خبرپراکنی به‌عنوان رسانه نگاه نمی‌کنند» و کسانی که در این رسانه‌ها کار می‌کنند را به عنوان «سربازان صهیونیست و آمریکا می‌بینیم و حتی می‌شود آن‌ها را در بانک اهداف نظامی خود پیش‌بینی کنیم».
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78053" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ozs40f7nLgMOeurEet79QO4Yzn7HlrhZgc-VlUWtJFY5fVbEYUaBIQEJ3V_lbrX_WUjv4f2i7YJtv6Utw5DQi9sWXGN85HzmRPxtHaFIFGs5xvBtwDnEjyTJFVJhpbybEWfIJfOYFR46xouDzdNxaCLKOsmE85jZvOrhLSF_a3iNDrHQ57HqGHIaQt7yoq_Q1J1g3-t8Fm1YKH_6ZZDKVBQ7p1UxvkfLSV0KvRGQOWFE5LoVDUyN3AOK8iMtF33Oul6oOdoU3RtoxZuuSDPS2hBeqeJb5DNsbqX7Ek5EAMyBrp_T-DL-SkcViMId0gRaSKFkUjPEbXGsTnB1UmHJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MuNl-avn299Y_PO8LKivpDDpnYCuePqMjo2n47rD4kBQtC9ApHuR4vpb65UnOZs9kilooelYlefBCov56zw9T1DkdUS6CNTQ5j-IjiQhaxLitBuKJYAB-EO9-u15RS4i-URKKS_BffMesXFEQOhkahLOlDRqSvDbBv628M1fCHlv-_Vf4mCFTk69mSO9dG0tRoSrvFiXvDnbzjxZvcWpSY7sUmGb9bwkQwzUut2q8Bl6_yANVHBj8vMM2PreciZy7l8j7I4JliVYhxX033J0rhhhu4tuA-EcSo-oWU1_8rud0Vfrrufs4ufgsdV7ohTIk9RfW2SGJDYu_gdl9CQPuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ درباره اعتراضات در ایران اعلام کرد «فکر نمی‌کنم وقتی یک مسلسل روبه‌روی شما باشد، آنجا بایستید؛ تک‌تیراندازهایی واقعا بالای ساختمان‌ها هستند.»
او گفت: «مردم هنگام اعتراض هدف گلوله قرار می‌گیرند و جمهوری اسلامی برای ایجاد ترس در میان جمعیت، لزوما نیاز ندارد تعداد زیادی را هدف قرار دهد.»
او افزود: «وقتی می‌بینید پنج، شش یا ۱۰ نفر در میان جمعیت ۱۰۰ هزار یا ۲۰۰ هزار نفری به زمین می‌افتند، مردم محل را ترک می‌کنند. فرقی نمی‌کند چه کسی باشید، می‌روید. وقتی افرادی آماده‌اند به شما شلیک کنند و شما را بکشند، اعتراض کردن بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.»
ترامپ گفت: «نیروی دریایی‌شان همان‌طور که می‌دانید، کاملا از بین رفته است. نیروی هوایی‌شان کاملا از بین رفته است. بسیاری از سربازانشان حقوق دریافت نمی‌کنند. فکر می‌کنم تورمشان ۳۹۰ درصد است و پولشان تقریبا بی‌ارزش شده است؛ منظورم این است که وضعیت خوبی ندارند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه چهارم شهریورماه، در مصاحبه رادیویی با گلن بک اعلام کرد که وضعیت حمل و نقل انرژی در تنگه هرمز به حالت عملیاتی بازگشته و حجم بالایی از نفت از این آبراه در حال عبور است.
ترامپ با اشاره به اقدامات انجام‌شده برای پاک‌سازی مسیر گفت: «ما از شر مین‌ها خلاص شدیم و این تنگه اکنون فعال و در حال کار است.»
او با اذعان به وجود برخی تهدیدهای پراکنده افزود: «بله، هر از گاهی پهپاد، راکت یا چیزی شلیک می‌شود، اما تنگه کاملا فعال است و نفت زیادی از آن خارج می‌شود؛ به‌طوری که همین دیروز ۱۰ میلیون بشکه نفت از این آبراه عبور کرد.»
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، چهارشنبه چهارم شهریور در مصاحبه با برنامه رادیویی گلن بک گفت فکر نمی‌کند مجتبی خامنه‌ای، رهبر جمهوری اسلامی، کشته شده باشد.
رییس‌جمهوری آمریکا اعلام کرد: «او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دستش، پایش، همه این قسمت‌ها به‌شدت آسیب دیده بود.»
ترامپ همچنین افزود حتی اگر مجتبی خامنه‌ای مرده باشد، جمهوری اسلامی «نمایش خوبی» اجرا می‌کند.
ترامپ گفت: «جمهوری اسلامی همچنان درباره مراجعه به رهبرشان برای گرفتن تایید نهایی در امور مختلف صحبت می‌کند.»
رییس‌جمهوری آمریکا همچنین افزود توافق با جمهوری اسلامی آسان نیست و آن‌ها «چندان پایبند به اصول» نیستند.
@
VahidOOnLine
دونالد ترامپ روز چهارشنبه چهارم شهریورماه، در گفتگو با شبکه الجزیره اعلام کرد که هم اقدامات اقتصادی و هم گزینه‌های نظامی «اثربخش» هستند و او در رابطه با مذاکرات با ایران «عجله‌ای ندارد».
او در پاسخ به پرسش‌های تانیا نوری، خبرنگار این شبکه، افزود: «من هیچ جدول زمانی ندارم؛ هیچ عجله‌ای در کار نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78051" target="_blank">📅 17:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WHDIC9TM9_15Fl241t5mehrS2EAV-4lgaY1KQnnznWu0vora961BA70MRorVvSI34xbQ7IWIWCxIahYH5qnGnGj9YcNG65PfEs0dZwVfuZUhzPu_wCWfb3VLIvNUZpu_yoYxRUWrHjSFoCTdproCF2WXFNVLQ2_wofeTEgv5MNiePt37FcEMWy4NU10faP1QDNTixdplg47vQDoejuU92aT71rx69rjWYbZQD_d-Gp_EHYre0wociCSq1nzxwT7kIqa9dZu8IE9nuksgbFH_IH3YzmiFk8ZlpZwMIOV49PocQUigqcWnpVTyTxCoqaf70mgDcmDfPJApSSYbhU9Ulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، بار دیگر موضع قبلی خود دربارهٔ ضرورت پایان دادن به جنگ با آمریکا را تکرار کرد و گفت: «جنگ همیشه راه‌حل نیست. گرهی را که می‌توان با دست باز کرد، نباید با دندان باز کرد.»
پزشکیان روز چهارشنبه چهارم شهریور در یک مراسم عمومی بار دیگر ایران را «پیروز میدان» خواند و در عین حال افزود می‌توان با «تدبیر و اندیشه» از این مسیر عبور کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78050" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VjsSFV4aulep69u49yL7IL-xP9YJIyJblcwPg2VWYL9AVhaICzH36zCIRoEG3dnues1LcIXfEFcG7GRcbRzsYul0KKUb1YfaTUGnnRb9ZIwGCbPNMDWq9CgqjsjZui_-tY2Jo-Jw-nNWubBlLYBDQx5QkNwS52rnxVopSGnWWANs7TsOUeyyim_se9WCvvUiZPF5r3uaCpxOwUeANNdUTLu27WYY57FYjnXj7K1fD4WbCxInp5UPv9HC7e2cO045YS0HJDOhMvzzYA13yiq1JCOUu5jnqbZ66f1Prxa2380l4f8rTuoVtoqbS6pmA1JiBpHbFZjYDGGrzOObJS11rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری هرانا گزارش داده است که حسین نظری، شهروند ۲۵ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه اول دادگاه انقلاب مشهد به اعدام محکوم شده است.
بر پایه این گزارش، دستگاه قضایی جمهوری اسلامی آقای نظری را با اتهام‌هایی همچون «ارتباط با دول و گروه‌های متخاصم» و «اجتماع و تبانی برای ارتکاب جرم علیه امنیت کشور» محاکمه و حکم اعدام او در تیرماه سال جاری صادر شده است.
نظری، متولد ۱۳۸۰، در جریان اعتراضات دی‌ماه توسط نیروهای امنیتی بازداشت و پس از طی مراحل بازجویی و قضایی به زندان وکیل‌آباد مشهد منتقل شد. او همچنان در این زندان نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78049" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q4ibTG2pmdw44CwT7b55-_-In1YoXyxTN70_W7oGCtxlYBj1t2hXmF_gvkU-Nh90Kvk7f04zdZ8OoBUYMEX9DUPx-HGZWsyiJhbH7ecjqlvc3DBCQhOXf8tPbW4k6GFNxlo80XGSpc-hBvDvwi34lweYVnqFnY4gqwjj9I5cM0aT58M_bHz7wSE2Q-cv5MjS6UttdMn8TQwGYrtY5-3t_TT1CqSwChRSZbJ2arotJwFa8r1rKK5j0uOcI_QXhWIIX1yZ3Fvl9x2M9-6MSVi7BOOW3EBfsWMkBSzEBPMECJMUUYXiiK7lE8U1DR-YMoZZlZ9pYu1UglnOQQwsV2giJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش وب‌سایت‌های اعلام نرخ ارز و طلا در ایران نشان می‌‌دهد که قیمت دلار آمریکا روز چهارشنبه چهارم شهریور کاهش یافت و به زیر ۲۰۰ هزار تومان بازگشت.
در لحظه انتشار این خبر، قیمت دلار ۱۹۸ هزار و ۵۰۰ تومان و قیمت سکه طلای موسوم به «امامی» هم ۲۱۰ میلیون تومان گزارش شد.
این اتفاق پس از چند روز افزایش قابل توجه قیمت ارزهای خارجی و طلا در ایران رخ می‌دهد. قیمت دلار آمریکا در این روزها تا ۲۰۵ هزار تومان افزایش یافته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78048" target="_blank">📅 17:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=rHJkn8zaVnQRk95fvdjLTAjehgcPC-xzMjZOBhwhgNvw_ZrGdQwYDJ53HP32TrAISgKSVabDWB82r3tZX9qTGF2HZ7x50ylaqNJIGZhg6KxUTkUVZz0hDJTJ0u7D986SXc_CWIWtFoKTBlK1tJeAy3O-B5wReFPCKTc_Gm3JAGH3EpuToDxE6Ub4iWTNDFJ3WFvYir4LRKYCuKLXpNgsriIj9XLddRHc7htW7GAgXJ9MrubLnOpxr8_7FDCt6RSQ5HB_7jhK5eMC4fNqXFE50RVeV8HioydVVN2qxw3-mk027F-4SkNjhdbYQd9ONa1_UdGo6oA_gASu-iUGt88fnw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/66d56a19f2.mp4?token=rHJkn8zaVnQRk95fvdjLTAjehgcPC-xzMjZOBhwhgNvw_ZrGdQwYDJ53HP32TrAISgKSVabDWB82r3tZX9qTGF2HZ7x50ylaqNJIGZhg6KxUTkUVZz0hDJTJ0u7D986SXc_CWIWtFoKTBlK1tJeAy3O-B5wReFPCKTc_Gm3JAGH3EpuToDxE6Ub4iWTNDFJ3WFvYir4LRKYCuKLXpNgsriIj9XLddRHc7htW7GAgXJ9MrubLnOpxr8_7FDCt6RSQ5HB_7jhK5eMC4fNqXFE50RVeV8HioydVVN2qxw3-mk027F-4SkNjhdbYQd9ONa1_UdGo6oA_gASu-iUGt88fnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: با «وحشی‌های» حاکم بر ایران نمی‌توان به توافق دیپلماتیک رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل شامگاه سه‌شنبه سوم شهریورماه درباره احتمال دستیابی آمریکا به توافق دیپلماتیک با جمهوری اسلامی گفت اسرائیل در اصل مخالفتی با یک «توافق خوب» ندارد، اما نسبت به امکان رسیدن به چنین توافقی با حاکمان تهران تردید جدی دارد.
نتانیاهو در جریان یک سخنرانی با اشاره به گفتگو با دونالد ترامپ گفت: «به او گفتم یک گزینه، البته، رسیدن به یک توافق است؛ یک توافق خوب. ما مخالفتی با آن نداریم.» او سپس با لحنی تند افزود: «اما تردید دارم بتوان با آن گروه، با آن وحشی‌ها، به توافق رسید. به شما می‌گویم: نمی‌توان به توافق رسید.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 211K · <a href="https://t.me/VahidOnline/78047" target="_blank">📅 17:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Aqp-AyYXPIIEcYFQ4lK3ejMarbyUhXOLAl8m_GC-i7PlOIHv7lLlFZylr2uJh1X1nooWwVbN2nWyg9Taga0cYnKHMA-apgOlYXaklf3TFWVvmsMWW7px_LjjrA2SIZ8kUAl3m40gBUmeLiFgW1PfeD4_dmbb1YOzi1DiSKM0fse03o4PeEpb_8p_DGgsGsW8BZlkNzLMsfDSKQ8_xQHMI9snix-MD56yhksUkg_y_PE67WMhixLuA2xuztSuQBAcU9fspHCax0bPZfTabGKRwqm21Wxcru4v16kpk6V9wi4Swhp-1-t6zveTBYpIXLVCe0UJqn4jEiLeGKxJRq6BZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیح شاهوردی، بازیکن پیشین تیم‌های پایه باشگاه سپاهان، در جریان اعتراضات ۱۸دی۱۴۰۴ در منطقه «خانه اصفهان» هدف گلوله جنگی نیروهای حکومتی قرار گرفت و جان باخت.
او ۱۹ سال داشت و تنها دو ماه به پایان دوران سربازی‌اش باقی مانده بود.
مسیح شاهوردی شامگاه ۱۸دی در منطقه خانه اصفهان از ناحیه پهلوی راست و کلیه هدف گلوله قرار گرفت.
اصابت گلوله باعث خون‌ریزی شدید داخلی او شد.
به گفته یک منبع مطلع، فضای امنیتی حاکم بر منطقه و شرایط آن شب امکان انتقال فوری مسیح به مرکز درمانی را از دوستانش گرفت. آن‌ها پس از گذشت چند ساعت، او را با پای پیاده به منزل رساندند.
مسیح شاهوردی حدود ساعت یک بامداد در آغوش برادرش جان باخت.
خانواده او با وجود جان‌باختنش، مسیح را به بیمارستان منتقل کردند؛ چراکه هنوز امیدوار بودند بتوان او را نجات داد. براساس اطلاعات دریافتی، کادر درمان پس از معاینه اعلام کرد که هنگام انتقال به بیمارستان، خون‌ریزی فعالی وجود نداشته و مرگ او پیش‌تر رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/78046" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uXIju-TX7Hszi08YQy3z4stskl_wlA-lctFcncFVuk2GO14_Ouy1k8OPPmJZKynYwFnug0uRNVHm8pk5sthTonja2rcS34K6LU462vXDX1yw2AG7lYHq1tdz28v2rul27U1iXTTF7M_zj-7o_WhiX8HoubG8WZ-1k_8qK7N7uo_asRGeM3rEABeXyBBf8WMc7eCq3LZ_PHhzYHqGb-UjZ0VF0Xh7Kf_FLweCy6RVsx17seieiYtU-bGx-p5QtycCQLIsfJdK6x_KeZnV4J0UZyF-vscndVTucKN9RGdq9JgsHxnoFzoYIPKh5KnL9KMQwmNhoiKE7TSTDFjVOAz0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ با بررسی واردات گاز ترکیه، ارزیابی کرد که هشدار جدید واشنگتن مبنی بر مجازات اقتصادی کشورهای طرف معامله با تهران، این کشور را که متحد کلیدی آمریکا و سومین شریک تجاری بزرگ ایران است، در برابر چالش قطع واردات گاز از ایران قرار داده است.
ترکیه در سال گذشته ۱۳ درصد از گاز وارداتی خود (۷.۷ میلیارد متر مکعب) را از ایران تامین کرد و ایران پس از روسیه، آذربایجان و آمریکا، چهارمین تامین‌کننده بزرگ انرژی آن بوده است. با وجود انقضای قرارداد ۲۵ ساله در پایان ژوئیه، دریافت گاز ایران همچنان ادامه داشته است.
اسکات بسنت، وزیر خزانه‌داری آمریکا، اعلام کرده است هر کشوری که به روابط اقتصادی با جمهوری اسلامی ایران ادامه دهد هدف تحریم قرار می‌گیرد و دونالد ترامپ در حال رایزنی مستقیم با رهبران جهان است. این موضوع احتمالا شامل تماس واشنگتن با رجب طیب اردوغان نیز خواهد بود.
بلومبرگ ارزیابی کرد اردوغان که ماه آینده عازم واشنگتن است و برای خریدهای نظامی بزرگ از جمله جنگنده‌های F-35 و F-16 به چراغ سبز آمریکا نیاز دارد، بعید است به دنبال خشمگین کردن ترامپ باشد. به گفته کارشناسان، در صورت قطع گاز ایران، آنکارا می‌تواند این کمبود را با افزایش واردات گاز مایع (LNG) گران‌تر— به‌ویژه از مبدا آمریکا — و اتکا به ذخایر پر شده خود جبران کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78045" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rDbu03l6zkWveB4xZOQVDxR2k26QYEmxQt2exzDTiC9fquAA8aacGNLPAiU_b1EEsCtu6cL-LzMDRtYaJDou9ZLE5pr1b4gspv3xd-5yCxzxR3wFEuPb8lpbBsXzlyCfpgtbpD8_sk9Af3FtdB1tZMpgQ5uHqMfjnvVdiCSet_bD7izJzbBCBRvbkNitXTLTjYP2JuE4Skxl3FWRIxHxb3Tbggdl0sdqMTl7pcHOJW7tr25DqVCWobblswesNJzYuw8smWO9qi3EIFHA7EiNabou7fQgrDArUZsLZvOMPP6BulOdfSqX42HXSY7Wb8VZamC7fsKiAgHHmSADIhej5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان هیلی، وزیر خزانه‌داری بریتانیا، اعلام کرد دولت این کشور در کنار آمریکا و دیگر شرکای خود به اعمال فشار اقتصادی بر جمهوری اسلامی ایران ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با «فعالیت‌های خطرناک ایران»، اقدام خواهد کرد.
هیلی، روز سوم شهریور ۱۴۰۵، در بیانیه‌ای گفت دولت بریتانیا از زمان آغاز به کار خود تاکنون بیش از ۲۴۰ تحریم علیه ایران وضع کرده است؛ تحریم‌هایی که به گفته او در واکنش به اقداماتی اعمال شده‌اند که امنیت مردم و بریتانیا را تهدید می‌کنند.
وزیر خزانه‌داری بریتانیا افزود لندن مصمم است مانع از آن شود که جمهوری اسلامی از اقتصاد جهانی یا نظام مالی بریتانیا برای پیشبرد برنامه هسته‌ای و فعالیت‌های بی‌ثبات‌کننده خود استفاده کند.
او همچنین از تلاش‌های آمریکا برای دستیابی به راه‌حل دیپلماتیک حمایت کرد و گفت بریتانیا از افزایش فشار بر جمهوری اسلامی، از جمله در قالب عملیات «طرد اقتصادی» آمریکا، استقبال می‌کند.
هیلی تاکید کرد بریتانیا به همکاری با شرکای خود برای حفاظت از منافعش ادامه خواهد داد و برای بازگشایی تنگه هرمز و مقابله با آنچه فعالیت‌های خطرناک ایران در منطقه خوانده شده، اقدامات لازم را انجام خواهد داد.
وزیر خزانه‌داری بریتانیا از جمهوری اسلامی خواست فعالیت‌های بی‌ثبات‌کننده خود در منطقه، از جمله در تنگه هرمز، را متوقف کند و وارد گفت‌وگوهای دیپلماتیک شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78044" target="_blank">📅 00:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aGARl5Lun_pbOBeiitQadKAHtKR7jg4NI4YXFxaX5ZjIv-kxjzA-k7iKbsNZ5gq8e1OAar1UnfErufzdCn5XuE_D2QDvpFS4DKCBGiG-4d9Y-SfKdO8IZ5VvKHcmfpS3aafOZsvodNxSzv3kHRFAhD4143n9YaQMYBqyOFIUdq18N0smfTqIyN3TfSp-yfgE3isVhMc1oZFS4LAHWC1cPFHqiQH6ugejp3BAV_bs-lUT2KsnoACl8iy7IgLrrqxF5W4_wzKERTC8yRJyDlH4pPbq9u_6ihTPDL196kB3kMEn3MqGASxDURnh3g_K8gi_IqXmTfxKLGIqsYYI0ehuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمود نبویان، عضو کمیسیون امنیت ملی مجلس، سه‌شنبه سوم شهریور در شبکه ایکس با انتقاد از عملکرد وزیر خارجه جمهوری اسلامی نوشت عراقچی بر اساس کدام مجوز از دستور مجتبی خامنه‌ای مبنی بر «انحصار» مدیریت جمهوری اسلامی بر تنگه هرمز تخلف کرده است.
او افزود چرا وزیر خارجه بدون ملاحظات امنیتی اسباب محکومیت و اجماع سازی علیه جمهوری اسلامی، به سبب «اعمال مدیریت لازم و درست ایران در کریدور جنوبی» را فراهم می‌کند؟
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78043" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSfWGQk09edfxohxh8r98W15bRHm1M97lA_ZI4pSVcsHc9oLrvYs1IlhajZoWNPJijAPH9J7I9KWPWo-Y_B2xDoWNN4W9FQfJLO8-5IZ9dPAQpjxPVY-YWEougaI3K-uzwpTDIi54J1XEOjKwqMnSnNRU5tMPvLwPbtZxwDRyKfnejeWXUbFuv9a2tWrMAcl9yctM8fIvpzkCY92YAr5t51mmp8tjrogDgTPJkGIxcgJ3hg7azXkLuO1Fvd2hmT0TlSeiG9woeYk8wp0gMD2gTW6IvfpdPwue9pCpqigzXVFnHgQP-ZqXvW3K2k8Lb6c3XfS033qlJ6-e7CN2f4Pzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با انتشار بخشی از ویدیوی نشست خبری اسکات بسنت، وزیر خزانه‌داری آمریکا، در شبکه اجتماعی ایکس، با کنایه از اظهارات او درباره تحریم‌های جدید علیه ایران انتقاد کرد.
در این ویدیو، خبرنگار با اشاره به ادعای بسنت مبنی بر آغاز «روز دی (D-Day) اقتصادی»، از او می‌پرسد چرا تحریم‌ها بلافاصله اعمال نمی‌شوند، و بسنت در پاسخ می‌گوید: «چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟»
قالیباف با طعنه به این تناقض در سخنان وزیر خزانه‌داری آمریکا نوشت: «او ابتدا می‌گوید روز دی اقتصادی! اما پنج ثانیه بعد می‌گوید چرا باید بخواهم سیستم مالی جهانی را منفجر کنم؟ جناب، اینجا ساحل نورماندی نیست؛ این یک نمایش کمدی است و شما فیلم‌نامه خودتان را هم فراموش کرده‌اید!»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/78042" target="_blank">📅 23:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/F6Vyt9PX3iBaFz3rwrBsAlxNr_dHUlwRjqCh1umIKDPaKtZDcovRZSGA5xIqifDwt_ROQur2HoD1onKac5UjOLdeSGNjx9QfNmpW8ZOHPJV4SphNqrdAIKodW8apT1O_W0_LA5ZA6QBGWayyOxVtwnLHBR3QBzbKXXp65ayK7torUWBsXLvDSvrk8C0aY41Dj70Kg4xJcRokzEixt53aIQjes5ucsfiHBM8KP2Lq21oakdEfbZORkIZ8xPfi-_FW7uN0IKoGjzNL1fuAJQchIbJrAv_NkQ9NSvDTt492goh18FmdHKXbzE7mWEZesqSNAyIxY7oECZ4HxySUIqDSJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WwmugkPSA49SJbkGPpCBaydk42Q82HK2pTShAby0f3uUd1yKuUKndGd_Z6UjpAGnjO5FR4ItKX7HkkhaXkgN4LTKBneumke-FMITGnsvPbXVozi0W-ftronuq7eqB5R0GK4CPeYhgfdTU4zJkwIq8CiTIJ6u2M4esarI_y5bB1uKUP0GcQZhDeBb-qW35k-4k9I8Z-ElF6pv-_OfrDF_V1lJmyTWuhmdkFAYXf3cL_LEkJir6IXkX4X9ng928BIwBwUZ5nlIQihourQaw-DtsmUJ9hy8XGxnFgpCN9zwSklBorix9M_2stJ6mxXPo-hkyGkArIOsxb23LleB2a3tYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو منبع آگاه به گفت‌وگوهای مارکو روبیو، وزیر خارجه آمریکا، با مقام‌های کشورهای مختلف، به کانال ۱۲ اسراییل گفته‌اند واشنگتن در حال حاضر انتظار ندارد حملات تهاجمی جدیدی علیه ایران انجام دهد و تمرکز دولت دونالد ترامپ به افزایش فشار اقتصادی بر تهران و تامین امنیت کشتیرانی در تنگه هرمز معطوف شده است.
به گفته این منابع، روبیو احتمال اقدام نظامی آمریکا را در صورت آغاز دوباره درگیری از سوی ایران رد نکرده است.
این تغییر رویکرد همزمان با اعمال تحریم‌های جدید علیه جمهوری اسلامی و ادعای دونالد ترامپ درباره پاک‌سازی تنگه هرمز از مین‌های دریایی صورت گرفته است.
بر اساس این گزارش، دولت ترامپ قصد دارد در مرحله کنونی فشارهای اقتصادی بر ایران را افزایش دهد و شرایط را برای عادی‌شدن عبور و مرور کشتی‌ها از تنگه هرمز فراهم کند.
منابع آگاه به کانال ۱۲ گفته‌اند انتظار می‌رود این رویکرد دست‌کم تا انتخابات میان‌دوره‌ای آمریکا در اوایل نوامبر ادامه داشته باشد و پس از آن، احتمال بررسی گزینه یک کارزار نظامی گسترده‌تر دوباره مطرح شود.
@
VahidHeadline
پیش‌تر:
پایگاه خبری اکسیوس به نقل از مقام‌های دولت آمریکا گزارش داد انتظار می‌رود تحریم‌های ثانویه گسترش‌یافته، دست‌کم تا پس از انتخابات میان‌دوره‌ای آبان‌ماه مسیر اصلی اقدام واشینگتن علیه جمهوری اسلامی باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/78040" target="_blank">📅 22:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ud5twHbvi6UfhFjD34PEHYkeQzIcH5j4pesruj9NFtepkdDOlduiPwtuz1Kbp58kxdPnu79rAF-Gy5V16QjgG30XshxUl2ARfjWYuwBs0vgMcQvCRMUoBWPmHImMhf27M4Ex_ibTUo_WWQ8sCHOhnvcn89b4WJwYX3DZjOGV3KXxOdVkvdkMv7jLx-X4WXEn9b1-ZIlUfxgXGUSRA7JJk8y4jUpx1Vh7DGhw-q8YlVh3IsHoMBHXYVkkhd9ip3fvLSsClpRYZFgPaSZKuskk1ycedijRIcQG4ixPIZLawHEqVyoK8vOKInR0igFM4qQkilTXsXWOPBPKh6AdAkP1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی نیکزاد، نایب رئیس مجلس شورای اسلامی، در گفتگویی با خبرگزاری ایسنا از کاهش دو سهمیه بنزین بر اساس آخرین تصمیمات مجلس، سخن گفته است.
به گفته او سهمیه ۶۰ لیتری بنزین با نرخ ۱۵۰۰ تومان محفوظ خواهد ماند اما سهمیه ۷۰ لیتر با نرخ ۳ هزار تومان به ۵۰ لیتر کاهش پیدا خواهد کرد.
همچنین سهمیه ۳۰ لیتر با نرخ ۵ هزار تومان هم قرار است به ۱۵ لیتر برسد.
او البته گفته است: «براساس آخرین تصمیمی که درباره بنزین گرفته شد، مقرر شد که قیمت بنزین افزایش پیدا نکند.»
اشاره او به بنزین ۱۵۰۰ تومانی است.
آقای نیکزاد تعیین نرخ چهارم بنزین را رد کرده است.
دیروز رئیس دفتر مسعود پزشکیان، رئیس‌جمهور ایران، هم گفته بود سهمیه بنزین حتما کاهش پیدا می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78039" target="_blank">📅 22:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tGI0SLeGF0aYLJr585BJGI2G-HM0jiQiTOoFc-0t39TX9H8obia1kK66jpTU-5VC3HRxSdvUQbRTGzI87uXZhRUMIpmiQcw0-0mwcBMSIT7AnVJCjJgOuihHJ19A97ycW8wX82Sb_wBG5pcrBjJnETgZc0nZKhGrxmxKIZ113i8A40fu3YXUkgYoBLv2HRA9RhDhXXgmdKwoPGMu-Nm_zeydg-LDS_ibCEGLlBqe16CYBK43i52TXOKvtIt-2FnPoPyej0LAsaM5jrQIIpo2ISU6Wy-bSobK84gmvV-qYMh-HHG2QFtrJ57S4K7U2sc7rts71wqCbOX0HBHgLiNywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AfbdvZQAm2lk2s1vOpGeW6pIxBmuULGh3lntO1rpPrKspI-vpDS-N7Dmr0OQvMi9HGy-26hT1C-MlEMIqnlJYcOpMBQ1bIq8lhudKa8Hrrm17-DpnR26rW0juIZGq8JsawOY4igUxlFZsUnfiK7iGXQ3HaC_2j_FQnxvHg3ICom-aGgMmNWR-GJoxJO3-ocml9QsDkS54YSxSrj5d8mzyt8wx5iSRDjSsu4e8A81hacsy1YEh50Wx6FIJNNsjWTIpO8DfEV8uAQgJnGYYxUFqFK_QKe6xd_vY-eIOOt-oZXGm-Bn3obbaBV7wLwU48BN7HrBSPdshHsTxKXV0q9gvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/B0c3DurCc4Y83tUi66e8P3D7-p1macqXCRi6DUCK3H_0a9U6jsYhumGVnqUXQ-nHAEjaT33GbOzdiqZzvfVlCdK5rFKmtbWaDoxGKMAPtznINdBu_Ny0bPtO6NxMJOAc8XWwVNDrME7Qdd2Wp_Lt5C7GHZGjxRVtzYNDt8sc2eqIC0R06hyDUXP_OwsYqWtg6GUNTQ9bU8KAhlkVSD10VzmlQahJzBL6gsvC_gfquqRXM9ucr-WXXnTbXtVFAdabMUfwj0iDBLVOcmfM_wmJjFu_qvBUtSRs1fj5ULksDkUC1lhz_WVDuiDXLC0WBF_SFzs1c1JgOqXReVdw8A7NZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست اسکات بسنت، وزیر خزانه‌داری آمریکا،
ترجمه ماشین:
رهبران ایران دارند به چیزی اعتراف می‌کنند که حالا جهان می‌تواند ببیند: فشارها مؤثر واقع شده‌اند.
مسعود پزشکیان، رئیس‌جمهور ایران، با اذعان به کمبودهای اقتصادی کشور گفت: «جنگ بالاخره باید در مقطعی به پایان برسد.»
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر گفت: «هرچقدر هم قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید داخلی نداشته باشیم، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری به قطع هر شریان اقتصادی که این رژیم را سرپا نگه می‌دارد ادامه خواهد داد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78036" target="_blank">📅 20:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MbKKp6CnGCo6nDfXiSptT2iaF9JD9VJSurctCKPCI3bJkEh37qNNtnKVTPPsbAsCzp0j14_tjhHC0iUJ9EQgIaZJjrVnCZnkL5FX4NI66U62-kbHVeoFADcPeT5ZEjtNAR1r0ETRNDVLqbZBa2wQofFV0gxWDUmBvVVK1myrQ__4JxPylfq0jrAGcpmZ5-eGkLGM9Awncn1LojE2CE7usP7_OlV8iUIn78fHu7dreqbO0oTrtMS33ipaOV7k_qo5OlvJhEsi5UeziuNHIY8OdIzvDi16SIQy9oF7lqGSmDh0yAsACgiDY_sH2qSwTULe-s47O-hBBO_MiDwgLNuiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاصه
بیانیه
: گفت‌وگو کردیم که مذاکرات ادامه داشته باشد
در پی سفر بدر بن حمد البوسعیدی، وزیر امور خارجه عمان به تهران و رایزنی با عباس عراقچی، همتای ایرانی خود، دو کشور بیانیه مطبوعاتی مشترکی در خصوص از سرگیری دریانوردی ایمن از طریق تنگه هرمز منتشر کردند.
بر اساس این بیانیه، وزرای خارجه دو کشور با تاکید بر حفظ حاکمیت و حقوق حاکمیتی خود، درباره چارچوبی مرحله‌بندی‌شده و قابل اجرا برای مواجهه با وضعیت کنونی تنگه هرمز و پیامدهای ناشی از جنگ اخیر گفتگو کردند.
چارچوب پیشنهادی شامل ایجاد یک گذرگاه دریانوردی موقت مشترک از طریق تنگه هرمز و اجرای پروژه‌ای مشترک برای پاک‌سازی تنگه از مین است. طبق این توافق، مذاکرات فنی میان تهران و مسقط برای دست‌یابی به کریدور دائمی، مدیریت ترافیک، تبادل اطلاعات و ارائه خدمات دریانوردی و امنیتی ادامه خواهد داشت.
همچنین دو طرف بر اهمیت گفتگوهای مشترک با کشورهای هم‌مرز با خلیج فارس، رعایت حقوق بین‌الملل و احترام به حقوق حاکمیتی کشورهای ساحلی تأکید ورزیدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78035" target="_blank">📅 20:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mFGHui8Lj8cQY_WpfHUjSH4EAFvo6j-F3EGaBjxH-beZw_p7JDE5FE05i7HL-05b4ONNwX-Mxs7SAwYNsthGvahBw-VAYBuiZzN8MJM96xT-jOT2OA1vp1eVLsdZX1tYkKjlrKBv3VVgHBIaZ7nlZ4R980gdeYh7cLlIG8mAi9739UOsBoVMur6bL3LjlBzxbS57Uvk_hBF7Gmu42khKObDOSetlArGkNZkL9EpswRcoSocVip50VnqdBIPamGMOZ-uIX78DON3G-MPLVgDFej8jaIS4LnqOzk52bQ4YmGklw8-qjs5Wux41CMfbuHhb2WaG1WeLhHAtpSPOlDLcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها و ویدئوهای مختلفی در شبکه‌های اجتماعی از «تعطیلی» تعدادی از جایگاه‌های عرضه سوخت در تهران و تشکیل صف‌های طولانی در مقابل پمپ بنزین‌ها منتشر شده است.
برخی رسانه‌های داخلی از جمله خبرآنلاین، خبرگزاری دانشجو و عصر ایران نیز تعطیلی چند پمپ بنزین در تهران را تأیید کرده‌اند.
در همین حال فریدون یاسمی، مدیر منطقه تهران شرکت ملی پخش فرآورده‌های نفتی با تأیید تعطیلی چند پمپ بنزین در تهران، «افزایش ناگهانی تقاضا و ترافیک مسیرهای مواصلاتی» را «منجر به تأخیر در ارسال محمولات و اتمام بنزین در تعداد محدودی جایگاه و بسته شدن چند ساعته آنها» عنوان کرد.
به گفته او، در روزهای اخیر توزیع بنزین در تهران «۳۰ درصد» افزایش داشت. یاسمی مدعی شد «تأمین سوخت تهران به‌صورت پایدار در حال انجام است.»
خبرگزاری فرانسه نیز روز سه‌شنبه، سوم شهریور در گزارشی از تهران، از تشکیل صف‌های طولانی مقابل پمپ‌بنزین‌ها خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78034" target="_blank">📅 19:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfZRgmXu_tjCIQN_-ouIbkv2QDiQh5Wm5EXkGsxZK7uaFhN7g_NGqD-NMDrVXOXMjkWwrsF7F_vMJaYLTHuDGoOgkxr52s69ZmYBeU3sIKespm737mvv1jleIcDcN6LpXVassfLNiv1y67mPuOLi-e6vw_K7rHg9iQJyyxsrfhBVELN_Ov3QxTQ878F8SyTKCWVw52LVQdEo_x3thw9ef3wzUWlli5NENnvXkCrX5tQXU2eRSqlbLOyIlp7OGv5BuEXj5EwSrn8OJa7OnVJq0DhHFQreqst03Qt4Aw_Yn3sYITygdaWDDonXebKS5jkN6D8ZMOMnE5sC_wl-ppFCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، چند دقیقه پیش:
همین الان نیروی دریایی ایالات متحده به من اطلاع داد که همه مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدید کار بگذارد، فوراً و به‌طور نظام‌مند نابود خواهد شد.
از طریق نیروی فضایی، ما تک‌تک وجب‌های تنگه را زیر نظر داریم؛ همان‌طور که کوه پیک‌اکس و سه سایت هسته‌ای دیگر را که پیش‌تر نابود شده‌اند نیز زیر نظر داریم.
سیاست «تحمل صفر» در قبال مین‌گذاری به‌طور کامل برقرار و لازم‌الاجراست.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78033" target="_blank">📅 18:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdSEg8hgQOwMsHqRduBXquBbuzNd0-SrUAuKH2boQO3HJZp0ny1P09ONX-4ul0u50hlpV14mH28aNnYUPSBAHYCpft5McIndrLTb7pHfM9UbfOqnqrRJt3imW8uWg_j-o5WJyZsm0yJ21epc8n9qnDg3e5h9tSP0cfQh6dUyEUq2jooDvcUg7kKFx44ToH_rV9vGw8UMV6u2CAPe6k0QG9WXwdGfWGY7V6j5r-XBMnF-zQX1wtwtKhxM1kjL8m5X4ndFS2CHkORBZeQEvR08BvaFAhFq6fyQjMUNaIgkhLHjPDxW5TkLPvgZPe587aD-xAReYgUhCEuuOaeoZl5-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ چند ساعت پیش:
جمهوری اسلامیِ رو به زوال ایران، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را ــ حتی زمانی که در حال اعتراض نیستند ــ در ابعادی بی‌سابقه می‌کشد.
این یک بحران انسانی در ابعادی عظیم است و باید همین حالا متوقف شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/78032" target="_blank">📅 18:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mF7U2hP21120A8gmf7Y-mVlISPqZZRpnsmqA5KTgZo_rhp7SJhTSF3PylJFJXB-uQB9TIOHviIMZxTDfnjh9jaMW1aCbBBDTe7mYoO9KYMdmXFad6eFvfAa46Dd7YPtyGT34OE5uBrZpgtv4hi8xbndc2_pNqbG2jkjJqSfezmqKoEBwHx96pyPjVLiSas872ZWo_nxNPntoalLjjClLG9167Nn1PtPh8QnYnTYRvjSU4IGQmsP1r-DrVxSWZZNIWlgbrm-PFphMK9INBToDIQQJmGz3dHVyj0huUNmw7ulXNO8uvpkkkEnl_Wwp37qyga-wpewCTl3V2X0sKU_ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز سه‌شنبه سوم شهریور ۱۴۰۵ به ۲۰۵ هزار تومان رسید و سکه امامی نیز با قیمت ۲۲۴ میلیون تومان معامله شد؛ رکوردهایی تازه که ادامه سقوط ارزش ریال و افزایش التهاب در بازارهای مالی ایران را نشان می‌دهند.
براساس قیمت‌های اعلام‌ شده، هر پوند بریتانیا نیز به ۲۷۹ هزار تومان رسیده است.
دلار در آغاز هفته حدود ۱۸۶ هزار و ۵۰۰ تومان قیمت داشت و روز یکشنبه برای نخستین بار از مرز ۲۰۰ هزار تومان عبور کرد. بر این اساس، بهای دلار طی چند روز نزدیک به ۱۰ درصد افزایش یافته است.
سکه امامی نیز که در ابتدای هفته حدود ۱۹۱ میلیون تومان معامله می‌شد، با افزایشی بیش از ۱۷ درصدی به ۲۲۴ میلیون تومان رسیده است.
جهش قیمت ارز و طلا یک روز پس از اعلام بسته تحریمی تازه ایالات متحده علیه جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/78031" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/svQ1s8pduGfrk1ADkN7mEgX6k71Rb2gYEE2v7kivRK4jm3cI63ZHPvyAe_VWOtUz39dmhcj3oOnCD_ZIeK9HbG4dS0puHaaBrkQoJYiDt05gxqNXbAX-8juKlrGd_VOB0Dy-_4I4sEUJ30uPL8WgPyNwrP1sAwY90l_rV1H5N0EFCZVlyl_4NUHdJ25wUZvZvg2ZS0aWYkD3rSuxp582j2L9SVQxQRPQV8_H6LMX6_BtYUlhoz8FuKHkL0fL_atrVc9-A0f_piCiogJUW0vahdw3CJnxCdWXEfyoH_1GOutLBItT5msgnJcnxKORFiE7kiba-K8fJki4lSEBqzJYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتایون ریاحی، بازیگر پیشین سینما و تلویزیون ایران، از تشکیل پرونده‌ای برای خود و ارجاع آن به بازپرسی دادسرای فرهنگ و رسانه خبر داده است.
این بازیگر با انتشار تصویری در اکانت کاربری‌اش در شبکه اجتماعی اینستاگرام اعلام کرد که پرونده‌اش به شعبه بازپرسی دادسرای فرهنگ و رسانه ارجاع شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/78030" target="_blank">📅 18:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uMdRf7FLBH6-EnLNCMvsa7dy-UWAr1r2G6X6EnT6E9OfLwHO2bkbzVF9u0KcbV0ej8scg44h7-N8lekuV5GhIRTz-_62QD-npBijO8KlTp12wSu45QjrALuZbLrRALrW-OnxI6D4KZrA_gVACwic3AZMbaMORSd-qiW5TkV-TiKwHEfk6iFc6iCo2fjUso1CxJlTdEeud1ndrJb-L2rhx9SAdA7k01G-vmmwsjJHp_Z9XFyNS5wuegzzxXm4Bz512_YPMQ4AHLuEgCCpi_PM8ncdOx-IWPbuY9hYGN4R1K1rvHtPPAPMb4zXQfHg599K6mR5wM5VBTVToODsSkKCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ade157391.mp4?token=b2KGAHY484Xv3KhGCrzgFgqYyBcWtKT59qmeJKFP1nTFFhBJ6hafz3FTsVKrppbjhqRQguC2OqSHMMqo51xVZQn8mSB0UDHd7iXIyTGKN-T-Sor30xwzyheMhOp1PhA3oENYfJ__RAByAarcS6UPOOqiCxNL7HQAnltkfbySZcrcI1T7aUUPIe-IDYS-gbCxIVYmnxfP_7oqnk1TLXQHZS8pG-svrmlvuunkjQiFMEdiTPNY9EIjifOF0FoA2y0nnr9xXTdv2Eq8EUXJoIgaQSp_YS4hlAy7ZSZ2WTEmW15HTx9bjTveoTznUYDWrNMV2n1jRF2EVP8olsZcpPh9Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ade157391.mp4?token=b2KGAHY484Xv3KhGCrzgFgqYyBcWtKT59qmeJKFP1nTFFhBJ6hafz3FTsVKrppbjhqRQguC2OqSHMMqo51xVZQn8mSB0UDHd7iXIyTGKN-T-Sor30xwzyheMhOp1PhA3oENYfJ__RAByAarcS6UPOOqiCxNL7HQAnltkfbySZcrcI1T7aUUPIe-IDYS-gbCxIVYmnxfP_7oqnk1TLXQHZS8pG-svrmlvuunkjQiFMEdiTPNY9EIjifOF0FoA2y0nnr9xXTdv2Eq8EUXJoIgaQSp_YS4hlAy7ZSZ2WTEmW15HTx9bjTveoTznUYDWrNMV2n1jRF2EVP8olsZcpPh9Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرویس پلیس مخفی ایالات متحده که وظیفه حفاظت از شخصیت‌های سیاسی در این کشور را بر عهده دارد در بیانیه‌ای که روز سه‌شنبه منتشر شد اعلام کرد از وجود ویدئویی «که به نظر می‌رسد بارون ترامپ را تهدید می‌کند» آگاه است.
اشاره این بیانیه به ویدئویی است که گفته می‌شود در شبکه سه تلویزیونی حکومتی ایران نمایش داده شده و حاوی اطلاعاتی از محل اقامت و رفت‌وآمد بارون ترامپ، کوچک‌ترین پسر رئیس جمهور آمریکا، در شهر نیویورک است.
سخنگوی پلیس مخفی آمریکا در بیانیه‌ای که به شبکه سی‌ان‌ان ارائه کرده تأکید کرده است که این سرویس درباره هر تهدیدی علیه افراد تحت حفاظت خود تحقیق می‌کند.
شبکه خبری سی‌ان‌ان در خبری در این مورد نوشته است که از زمان کشته شدن علی خامنه‌ای، رهبر سابق جمهوری اسلامی، رسانه‌های حکومتی در ایران بارها مطالب و ویدئوهایی درباره طرح سوء قصد به جان ترامپ و خانواده‌اش منتشر کرده‌اند.
حدود یک ماه پیش نیز خبرگزاری تسنیم، نزدیک به سپاه، ویدئویی منتشر کرده بود که در آن شکاف‌های امنیتی پیرامون ملانیا ترامپ، همسر رئیس جمهور آمریکا، بررسی و درباره راه‌های هدف قرار دادن بانوی اول آمریکا بحث شده بود.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز دوشنبه دوم شهریور ماه، در جریان یک تماس تلفنی با برنامه زنده تلویزیونی در شبکه ۱۴ اسرائیل، در پاسخ به پرسشی درباره تدابیر امنیتی برای حفاظت از پسرانش گفت جمهوری اسلامی یکی از پسران او را هدف قرار داده و تلاش کرده است او را ترور کند.
به گزارش تایمز اسرائیل، نتانیاهو بدون ارائه جزئیات بیشتر گفت: «ایران یکی از پسرانم را هدف قرار داد. ایران سعی کرد یکی از پسرانم را بکشد، به قتل برساند.»
نخست‌وزیر اسرائیل در دفاع از توافق خود با شین‌بت برای تامین امنیت اعضای خانواده‌اش گفت: «بنابراین، امنیتی که آنها دریافت می‌کنند یک کالای لوکس نیست.»
تایمز اسرائیل نوشت، نتانیاهو با اشاره به توافقی که بر اساس آن امنیت پسرانش و همسرش، سارا، دست‌کم به مدت پنج سال، حتی در صورت شکست او در انتخابات آینده، تامین خواهد شد، از این تصمیم دفاع کرده است.
او با اشاره به مهاجمان احتمالی افزود: «بدون این امنیت، آنها موفق می‌شدند.»
مشخص نیست کدام‌یک از پسران نتانیاهو، یائیر یا آونر، هدف این سوءقصد بوده‌اند و این تلاش چه زمانی و چگونه انجام شده است.
آونر در اسرائیل زندگی می‌کند و یائیر که از برادرش شناخته‌شده‌تر است، بیشتر سال‌های گذشته را در میامی گذرانده و به اظهارنظرهای تندروانه شهرت دارد.
بر اساس گزارش تایمز اسرائیل این تلاش در زمانی رخ داده که یائیر نتانیاهو در اسرائیل حضور نداشته است، اما مشخص نیست که آیا او هدف این سوءقصد بوده است یا خیر.
در این گزارش تلویزیونی همچنین آمده است که طرح ترور ادعایی چندین ماه است که برای نهادهای امنیتی اسرائیل شناخته شده، اما مسائل امنیتی مانع از انتشار جزئیات آن شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 214K · <a href="https://t.me/VahidOnline/78028" target="_blank">📅 18:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mwRSWfZamD1yaeRbgEh9T_-WIf5ZkLn_fgW2tjbNh1Tqsr-CWWjscLeE4SOnbxoR0cROjHC4WkqijuSfzrrImwHxDBO7FW-0Vz27law-x5P9CtB11UenULVmqARDcIeSxZqAZ1RQguNuD2R61ncwXDuI0JYQkeUBpLrTSgcEnhG1iaUwxWb5kmc7udWM4lDYj-ffthpQpqs_HlIsf19sF0viv5VkF1QrcLP5gC9KrJcLXwv6GQJ2rhgk2vBxJgIunVqOPZ9w7z0ZLe4UDWUJP_Hsu6AuWF4zcDXAPQLseWFhZ2-8YuIEOMBpjO9gHKR71dPjecRj8cH084SytOn2MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه چین در واکنش به تحریم‌های تازه آمریکا علیه ایران اعلام کرد همکاری پکن و تهران در چارچوب قوانین بین‌المللی انجام می‌شود و «نباید با دخالت یا اختلال روبه‌رو شود.»
لین جیان، سخنگوی این وزارتخانه، روز سه‌شنبه سوم شهریور گفت چین تحولات را از نزدیک دنبال می‌کند و برای دفاع از حقوق و منافع خود «تمام اقدامات لازم» را انجام خواهد داد.
او در ادامه تأکید کرد که چین همواره مخالفت خود با تحریم‌های یک‌جانبه آمریکا را ابراز کرده و آنها را غیرقانونی دانسته است. به گفته او، جنگ اقتصادی و فشار حداکثری «تنها به تنش و درگیری بیشتر دامن می‌زند».
آمریکا روز دوشنبه تحریم‌هایی علیه ۶۰ فرد، نهاد و کشتی مرتبط با ایران وضع کرد و هدف آن را قطع «راه نجات اقتصادی» جمهوری اسلامی خواند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی را که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
چین خریدار اصلی نفت ایران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78027" target="_blank">📅 17:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I5RtiLQO23iXQKavxlS4XO8sJJ2_v3JxC0g_YA-3zc3ko3AVjCZjdw4XibRl67a0RXRLE3StX4Qx0K9nXD484frKzGuCR80stajWl1QMb1adeY19JK4j9GlaCxIRUMIBu3oQc7g1_Twy7W2dvjTzewoQsonEqW-YH-rd0pd5I4ytHEWLpTXD84osp51nEZlCQlyHLbIF9w2CCRG7Zom1hT2Jjatfya8iX6BOds_DTTfgtr7D8-02F2ObzK6qVCYXgB1zTTJBavx2NRjJyZkEST9Z7B3UG8NFonhopcRu_OxmWsSqlNMJDIM-zCBAWEtpVwzhB8gpP0VZHaCwZtnZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی پیشه‌ورزاده، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در رشت، از سوی دادگاه انقلاب این شهر به اعدام محکوم شده است.
کمیته پیگیری وضعیت بازداشت‌شدگان
خبر داد که شعبه دوم دادگاه انقلاب رشت به ریاست قاضی محمد‌علی درویش‌گفتار این حکم را در مرحله بدوی صادر کرده است. پیشه‌ورزاده در جریان اعتراضات روزهای ۱۸ و ۱۹ دی‌ماه بازداشت شد و اکنون در زندان لاکان رشت نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78026" target="_blank">📅 17:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=JPAtL2Sow_A0vCupPStHpk2gT93BkDJd_fQoiUkGRbS-DYYCGnRV49ZDP4Loi0eGPO4CXRhn4UgyaV1HYkfNA3UadjpBbgtIto0fXhZteSajIt1ZBaLPELELQusUnTTUxrH7vHPykb-38hnZpV0tC6NM67XNnxqaLp6xJ8L7JfVkAHVwyZmGYLlEhYUMCCTjBpBbwOwWdzDlphZL0zugAm01eWye3irejnAWQOEukccWyGCnp3Vo1ecYrWg-Hg6lZeWAiajEtEu2U7lHV4AmMAmNl6LLq5MYw3DaMtjg3phULCaRlCZbgN4zrGvlSNgHv2Xlpd4T6rFM9czYTTQ40w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aaccb368d5.mp4?token=JPAtL2Sow_A0vCupPStHpk2gT93BkDJd_fQoiUkGRbS-DYYCGnRV49ZDP4Loi0eGPO4CXRhn4UgyaV1HYkfNA3UadjpBbgtIto0fXhZteSajIt1ZBaLPELELQusUnTTUxrH7vHPykb-38hnZpV0tC6NM67XNnxqaLp6xJ8L7JfVkAHVwyZmGYLlEhYUMCCTjBpBbwOwWdzDlphZL0zugAm01eWye3irejnAWQOEukccWyGCnp3Vo1ecYrWg-Hg6lZeWAiajEtEu2U7lHV4AmMAmNl6LLq5MYw3DaMtjg3phULCaRlCZbgN4zrGvlSNgHv2Xlpd4T6rFM9czYTTQ40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر دفاع آمریکا می‌گوید اعلام کارزار تازۀ اقتصادی علیه ایران، به‌ معنای حذف گزینۀ نظامی نیست.
پیت‌ هگست که شامگاه دوشنبه و پس از نشست خبری اسکات بسنت وزیر خزانه‌داری ایالات متحده صحبت می‌کرد، تأکید کرد که «به‌هیچ وجه گزینۀ استفاده از حملات نظامی در تنگۀ هرمز یا اطراف ایران را کنار نمی‌گذاریم».
وزیر دفاع ایالات متحده در عین حال ابراز نظر کرد که ایران نمی‌تواند فشار اقتصادی تازه را تحمل کند.
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/78025" target="_blank">📅 09:12 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bvlaeHU5os_lq2xljizYPlp1isCaCdrJBm1gzBrN16KXfygjNp6cdvBjeraCPRig7x1HuJSOhBxzUZiD2000zNJz-xXRXFtTkBaOXRSJC-O5UXFHLW5OCPt5yHFNkfiIPeStZh8bqar7oP6FA85pPILoTLQpKMlwl0z9uypcyBZtyuAHUzfqQw1i8-SmINTaCBd9NFoInOd_JN9uOmxVOyS5B-4rvnZdSyYdeBgc1Q5NlqGDC6AVLdzhqf6DHL1lQ1KQUBCJ7TXcZtAcG1SqHpNb-rlZxG_2v0hZCzGfzj7mdecsZAi1v_zSm-8AfGK5OnJpYKCTuIQd6maeDcpjEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در ۹ مایل دریایی شمال‌شرق «اش شیشه» (Ash Shishah) در عمان دریافت کرده است.
ناخدای یک نفتکش گزارش داده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته که باعث آسیب به موتورخانه و از کار افتادن شناور شده است.
گزارش شده که خدمه در سلامت هستند. در زمان دریافت گزارش، تأثیرات زیست‌محیطی حادثه مشخص نیست.
...
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78024" target="_blank">📅 01:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">(۱۸ دقیقه، ۳۰ مگابایت)
متن کامل سخنرانی و پرسش  و پاسخ:
telegra.ph/bessent-08-24
اعلام کارزار اقتصادی آمریکا علیه ایران؛ بسنت: همه شریان‌های حیاتی آن‌ها را قطع می‌کنیم
🔸
وزیر خزانه‌داری آمریکا روز دوشنبه دوم شهریور در یک نشست خبری درباره کارزار جدید فشار علیه ایران، متعهد شد که اقتصاد جمهوری اسلامی را از منابع حیاتی خود محروم کند.
🔸
اسکات بسنت گفت: «در سراسر جهان، هدف ما این است که تمامی شریان‌های اقتصادی که این حکومت استبدادی را سرپا نگه می‌دارند، قطع کنیم تا زمانی که تهران کاملاً تنها بماند.»
🔸
وزیر خزانه‌داری آمریکا این اظهارات را در جریان تشریح راهبرد جدید واشینگتن برای افزایش فشار اقتصادی بر ایران مطرح کرد؛ راهبردی که بر تشدید تحریم‌ها و محدود کردن روابط اقتصادی و مالی تهران با سایر کشورها متمرکز است.
🔸
او هشدار داد که هر کشوری برای متوقف کردن فعالیت‌هایی که واشینگتن آن‌ها را مرتبط با ایران تشخیص می‌دهد، مهلت مشخصی خواهد داشت؛ در غیر این صورت با اقدامات وزارت خزانه‌داری آمریکا مواجه خواهد شد.
🔸
بسنت گفت دونالد ترامپ، رئیس‌جمهور آمریکا، در حال تماس تلفنی با رهبران کشورهای مختلف است و از آن‌ها به‌طور مشخص می‌خواهد تعاملات خود با ایران را متوقف کنند.
🔸
هم‌زمان وزارت خزانه‌داری آمریکا با انتشار بیانیه‌ای گفت دامنه تهدیدهای خود برای اعمال تحریم‌های ثانویه مرتبط با ایران را به پنج بخش عمده اقتصادی گسترش داده است؛ اقدامی که به گفته وزارت خزانه‌داری آمریکا، در راستای تلاش واشینگتن برای تحمیل یک «روز سرنوشت اقتصادی» بر تهران انجام می‌شود.
🔸
در این بیانیه آمده است: «خزانه‌داری علیه پنج بخش حیاتی شامل دارایی‌های دیجیتال، فناوری، طلا، هوانوردی و کشتیرانی تصمیمات جدیدی اتخاذ کرده است؛ بخش‌هایی که رژیم ایران برای تلاش جهت سرپا نگه داشتن اقتصاد در حال فروپاشی خود از آن‌ها استفاده می‌کند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/78023" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BhsLgOj6IRfFjUHAwODoRgXEPvso289aMaLUBixvFQcKnH6P5H32EhkEpGBHUcj3YZ2HApdn3CYln_g6f240ck8IQ7Y-5qB5MF03E6_uHdP1QA94BggYwU69tySxtNyO9rtIyfECXa0PaT1yonasVeJ-GAxRM0TJN_l5gCOLcddPMtjUgY-toh-bF7pTQmltcs9hWnlnD0cC1t9A5kz7sepFOmCkiz-Nq7Shz6zj2q_85ZsU1kgENakT1tFj7UGLSjDzkT4qQfvbfVZpgxijTV71qaT_llj_qkqy3a9KZAaJYGiXMS78fY9Ntp5zao3WGcHqe4M7Dk8bxsR7LDaXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران روز دوشنبه دوم شهریور بار دیگر روندی صعودی در پیش گرفت و در معاملات صبح از ۲۰۲ هزار تومان عبور کرد.
همزمان قیمت سکه امامی به ۲۲۲ میلیون تومان رسید و بهای طلا نیز در سطوح بی‌سابقه‌ای معامله شد.
بر اساس آخرین نرخ‌های ثبت‌شده، دلار آمریکا در بازار تهران به ۲۰۲ هزار و ۶۰۰ تومان رسید. سکه طرح امامی نیز ۲۲۲ میلیون تومان قیمت خورد.
در همین زمان، قیمت یک مثقال طلای آب‌شده به ۹۶ میلیون و ۲۰۰ هزار تومان و قیمت یک گرم طلای ۱۸ عیار به ۲۳ میلیون و ۲۰۷ هزار و ۸۶۰ تومان رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/78022" target="_blank">📅 18:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mZ_vsZAhYB11UX1YBVpAfiFKtptln-BdktAfxpUyPSRRpHsql4TXs2EhaoZTnOF58482tu7jNnRnSbE3VfBlE6FiTCK0hwu2WyWjhwdETa-x_ODrXFT6Ge8uKbA5HfpxvItUebXFt_Wc-cjlsDvk4HQl1ha7nVBlRJYrsqQTbj_xGt-AdlGHhkPDRhjwKfsN8YFMSEBfDwRa2650DhiwNrbElVbn3-hYyHpppamhAAsh1yzqP_gBAjThpiuixNkTEMqmHSes4xQ6bdqHEJi5YtwLba2ENSHikxP5kubbtYDtm1RMAgfD_L70jj0IQ2ub7mVD7Zn5LkOfEZwha-5d7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
ایران کاملاً در حال فروپاشی است!!!
رئیس‌جمهور DJT
realDonaldTrump
اشاره به ایران در پستی دیگر:
دموکرات‌های چپ رادیکال با نظرسنجی‌های جعلی دارند دیوانه‌بازی درمی‌آورند. آن‌ها این نظرسنجی‌ها را در سطحی منتشر می‌کنند که هرگز پیش از این دیده نشده است. به این‌ها «عملیات تضعیف روحیه» می‌گویند؛ جایی که تلاش می‌کنند روحیه جمهوری‌خواهان را تضعیف کنند تا آن‌ها برای رأی دادن بیرون نروند — اما نظرسنجی‌های واقعی فوق‌العاده‌اند و روحیه در کشور ما هرگز تا این اندازه بالا نبوده است.
ما در برابر همه در حال پیروزی هستیم، از جمله ایران که کشورشان در یک مارپیچ مرگ اقتصادی و نظامی قرار دارد.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/78021" target="_blank">📅 16:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H8HZbf3lThVLs36jWJqdfTTz7ku3xrjZICbrEN32577MDwlWTAo_W6DM5yVmahg-9p4jp5Z3BjChBG06XXnYVwafKgFBSxMU-DiSL0glkCWJcRQZC5ftwEdFudsDOnhmixEpWvZJ0sf6dzcWj3xxPaMtWCjeJy08wI1y7J8nUrsF0PI1JfuTdum7Bj6wPX7ArxkC3j7cnoJQaR1hZZPx_51nmFYeshbVaL1J7DLW9vBtVgbGH79Y-xL6OMC9Y0FvsBX7ce4Em16HuSbiiB97DsiG-fwa7HQaiT3ObRQ_vpk5TYCxItp1rqfsTLiJWpI8D-5Ens7fxan-2PFnems62A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jarLiey0hqC1jQf2udKruf6stlGit2EOkHsGwRexzjq_Xg1GQDU_JVv1YETL-JhNhb9zVpJCuEd6n9utdmrbQoGcraGYh71sF7POO4rAqX2_6t0XuBNY65mAhu_p9t0Cott1pttSkQQaea2JgGlN74ML2KiKM3WOgX2C7-D28GKFDQYrN644up87ejntt16-KTVBHm-HoB-ltfhXQBkO9KGrkgN9xhIPe5DWOyPKAA7ckERL08QEYNW23qZH3NI-ZnOyH2RdDFt1eAqCL8fCTpCJkqsiFjpZ9b2KsPRh4zJ31mY9KkEak2BRoXPbjQRLjCd0gxm9OmtTdmln-lrewQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری ایالات متحده روز دوشنبه دوم شهریور مقاله نیوز مکس درباره سخنان هفته گذشته محمدباقر قالیباف در عراق را بازنشر کرد.
رئیس مجلس و عضو ارشد هیات مذاکره‌کننده جمهوری اسلامی ایران، هفته گذشته در جریان سخنرانی در جمع فعالان اقتصادی ایرانی و عراقی گفته بود آمریکا در جنگ نظامی شکست خورده است و حالا به سراغ جنگ اقتصادی و شناختی رفته است. اگر در میدان اقتصادی قوی نباشیم، شکست خواهیم خورد.
ترامپ این مقاله را در آستانه اعمال تحریم‌های بی‌سابقه علیه ایران بازنشر کرده است.
@
VahidOOnLine
محمدباقر قالیباف، رئیس مجلس شورا و عضو ارشد هیات مذاکرات جمهوری اسلامی، روز دوشنبه دوم شهریورماه با انتشار پیامی در اکس، شعار انتخاباتی «آمریکا را بار دیگر باعظمت کنیم» دونالد ترامپ را به «آمریکا را دوباره گرسنه کنیم» تغییر داد.
قالیباف در این پیام احتمالا با استناد به داده‌های سازمان غیردولتی «تغذیه آمریکا/feedingamerica» و ادعای ۴۷ میلیون گرسنه در آمریکا نوشت: «آمریکا را بار دیگر گرسنه کنیم. با ادعاهای واهی نمی‌توان شکست‌ها را لاپوشانی کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78019" target="_blank">📅 16:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C8SfrpKOcTXHeOlUUg2UT6ak5WMPK22mQ8ILbg3-8DYFIgb37Q9q_ff8wQxHeYLH3DcvbdBQ0OnzQck6IUStE9RNVPQJApQbFwMAYXCGnbisp_FuNKa37m_8iovJ3qo3QIqMPceSVIdRF7AogaYljDclT23yX8PX6jRDwaMMoUKNqBgtY1jZok5jhcmjwk3acjqYj4F9u_oEruitjV2E04Bog0sR_T46x1H2FQYVaYdGg5UGUOglIJOZMKx5v2NLYs9O3Vk-jyUDmM4foSB4hZT8i-qxGSM8R5w_UB6iaJjx_joxjbl9_VesdQ-rcuL3-SP28B0ll3VhtAHqPi-ijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Dyz4BHh3QsS34bKcbWx8r0ymnalHnWF389zdEz5nhEqNQw2AmDEoJMWvWS-S5RBhcOgpU5-mZ-g2rAd1TelrXRSpmRBLqaWX_7uzAlE7BY6Uzd4AtQnSlo9z84oiAtavr_1w-aGXLmlsrr0gkw-JF1Z3Vysem9q1TqIptjFCnjr1eAi4voyoV4X9SnB_szAy_sPzPLQuGCbcIc2AJuVPoHMrs4NPreFP62-slzhMXucMb_wPs5ZTL5Sbshu0s1ZJL6KMg8v09qR0QHjHkf2Wsz_Vs0_GxA74WJffAn6P02SvUnHu0ceKcmDhdBGoH3xiqAm47dyQxWuY4js-lTh-oA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فیلدمارشال عاصم منیر، فرمانده ارتش پاکستان روز دوشنبه دوم شهریور ماه وارد تهران شد.
محسن رضا نقوی، وزیر کشور پاکستان او را در سفر به پایتخت ایران همراهی می‌کند.
ارتش پاکستان با صدور بیانیه‌ای اعلام کرد سفر این فرمانده ارشد نظامی به تهران «در راستای تلاش‌های اسلام‌آباد برای ارتقای صلح و ثبات منطقه‌ای و مذاکره با مقام‌های ایرانی بر تقویت تلاش‌های صلح و یافتن راهکاری مسالمت‌آمیز، پایدار و جامع برای حل درگیری‌های خاورمیانه متمرکز خواهد بود.»
خبرگزاری صدا و سیما گزارش کرد عاصم منیر با مقام‌های ارشد جمهوری اسلامی دیدار خواهد کرد.
@
VahidOOnLine
خبرگزاری رویترز به نقل از چند مقام پاکستانی اعلام کرد عاصم منیر، فرمانده ارتش پاکستان، هفته گذشته و پیش از سفر به تهران، با دونالد ترامپ تلفنی گفت‌وگو کرده است.
سه منبع پاکستانی در گفت‌وگو با رویترز تاکید کردند این تماس چند روز پیش از آن انجام شد که انتظار می‌رفت منیر دوشنبه برای گفت‌وگو با مقام‌های جمهوری اسلامی به تهران سفر کند.
به گزارش رویترز، این تماس که پیش از این گزارش نشده بود، در شرایطی انجام شد که آمریکا اعلام کرده است تحریم‌های اقتصادی گسترده‌ای را علیه جمهوری اسلامی و شرکای تجاری آن اعمال خواهد کرد.
در این گزارش همچنین آمده است انتظار می‌رود فرمانده ارتش پاکستان، دوشنبه با افرادی نزدیک به مجتبی خامنه‌ای، دیدار کند.
رویترز نوشت تنش‌های میان آمریکا و جمهوری اسلامی یکی از محورهای مورد انتظار در این سفر عنوان شده است.
یک منبع دیگر در دولت پاکستان نیز گفت: «منیر همچنین قرار است درباره حملات اخیر حوثی‌های وابسته به جمهوری اسلامی به عربستان سعودی، متحد پاکستان، گفت‌وگو کند.»
@
VahidOOnLine
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی روز دوشنبه دوم شهریور ماه اعلام کرد بدر البوسعیدی، وزیر امور خارجه عمان روز سه‌شنبه به تهران سفر می‌کند.
به گزارش خبرگزاری صداوسیما، بقایی به خبرنگاران گفت بوسعیدی در تهران با عباس عراقچی، وزیر امور خارجه جمهوری اسلامی دیدار می کند.
در پی حمله آمریکا و اسرائیل و بسته شدن تنگه هرمز، جمهوری اسلامی مذاکراتی را با عمان برای تعریف نظام حقوقی جدید تنگه هرمز، آغاز کرده است.
تهران، مسقط و دوحه از پیشرفت این مذاکرات خبر می‌دهند، با این حال دونالد ترامپ، رئیس جمهوری آمریکا هفته گذشته تهدید کرد که اگر عمان در مسیر «توافق» تهران و واشنگتن مانع ایجاد کند، این کشور را بمباران خواهد کرد.
البوسعیدی، سال گذشته میانجی دو دور مذاکرات میان جمهوری اسلامی و ایالات متحده بود. هر دو دور مذاکرات بدون نتیجه و با حملات آمریکا و اسرائیل به ایران پایان یافت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78017" target="_blank">📅 16:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=ur8j4FUrXdCONs_voQTCAaskbYG0pVA3iHTmQ526NBDNaXfkBRgkLRJiQuVobim-qrQQtt4ceUImGYXQB1otSwe0QBOdFcJeAbWmUkFhWZEVzdrK1_C7M8_Tbkw7NQ7xU3S48V4zr_uuMTLFczqftSIXLZajqrfScjnB85gGHV9quW-Cy3WReWWQ5wXWIf203U46BXkcbiEwbskg_C_YPixbx7bItgkGRC9t0DDUn8nyw70K_BT2nl49Qa7wjrWxxmjhsaSjr2tekg2tPoA87vtEKtj36561TW-1TjwBCTWgkFl1oBql7kVjZsiILHHJXwTEhgVRnpjBywuc4g0zmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b9437ec72.mp4?token=ur8j4FUrXdCONs_voQTCAaskbYG0pVA3iHTmQ526NBDNaXfkBRgkLRJiQuVobim-qrQQtt4ceUImGYXQB1otSwe0QBOdFcJeAbWmUkFhWZEVzdrK1_C7M8_Tbkw7NQ7xU3S48V4zr_uuMTLFczqftSIXLZajqrfScjnB85gGHV9quW-Cy3WReWWQ5wXWIf203U46BXkcbiEwbskg_C_YPixbx7bItgkGRC9t0DDUn8nyw70K_BT2nl49Qa7wjrWxxmjhsaSjr2tekg2tPoA87vtEKtj36561TW-1TjwBCTWgkFl1oBql7kVjZsiILHHJXwTEhgVRnpjBywuc4g0zmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@
VahidHeadline
این عدد ۲ از کجا پیش‌فرض گرفته میشه برای تعداد جناح؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/78016" target="_blank">📅 15:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U8a3r7SmChEYoK9VDmR5DCu5hnBbtvjUy_5Gzs4tw41ukwHwNqchgd61Jk16v1acccuyAjrPatd4-zWjwNWO-mLqGg33sdIp8xUuzXxkT29v-LCnjhJ0oHQG3RP5zP8l4E-TrHlVoIGIKfEqETmJq8jnu5l_SblNNwtre4mKhka9lMhF5CVhqeVHuB-KmLkAzveMqUmMI6Js-3Zv_Wzr_DpxJKwAjy4o0qxCG0-zRGiF9qCHiudB-Jt3BIToFg-p-Zbz0PcNzz-_xZbJP8uFiLxLX2jlR07YqsGjFaoOU4pnv5tcVja8uDqFouhtXCgLaacVBzLxhO-Kuvv8N2sMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت روز دوشنبه دوم شهریور، در آستانه اعلام جزئیات طرح تازه آمریکا برای افزایش فشار اقتصادی بر ایران، بیش از دو درصد کاهش یافت.
دونالد ترامپ، رئیس‌جمهور آمریکا، این طرح را «کوبنده‌ترین» عملیات مالی علیه جمهوری اسلامی توصیف کرده و از متحدان واشینگتن و همچنین چین خواسته است به آن بپیوندند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، قرار است روز دوشنبه در یک نشست خبری جزئیات بیشتری از این طرح ارائه کند.
در معاملات روز دوشنبه، بهای نفت برنت و نفت خام آمریکا هر دو ۲٫۳ درصد کاهش یافت و قیمت نفت برنت به حدود ۹۲ دلار در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78015" target="_blank">📅 15:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQQ2ijVRzsNhtgs6axx22wDDJUE5wJGqVtm8cbaZdTt0wUPnP78O2cKgefWcpVSJZBm1_Yl8wplWR2_OMeZ9bxQjBl50JcCrcdzjNAWujJnE5x9MdFMNWnqch5JBKDQ-FPJiSh20fbROgLjZT4w_v2RI1jy928Gn7gWUJpJRbSyQh37LNvKS1rpDH4yp99jQ7noVUWGsheUMXRjr7HujHqoyI0q3Gz0ocKj8LGMIVyTbvTXVTOnfUdn3roVv-mhd8689wGE4hXSGicx8FaCOBOqJ2bMP4CdynSx0T1yucwrZlZKfD8K3wyvzFg-13cjiLTTqhhDoj4GSCvDzaQWRTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی تجاری بریتانیا اعلام کرد: یک نفتکش در ۶۳ مایلی شهر بندری ینبع عربستان سعودی، هدف پرتابه ناشناس قرار گرفت.
این سازمان زمان حادثه فوق را روز دوشنبه دوم شهریورماه اعلام کرد و یادآور شد:‌ بر اثر اصابت پرتابه ناشناس، قسمتی از عرشه کشتی دچار آتش‌ سوزی شد، اما خدمه در سلامت کامل هستند.
سازمان دریانوردی تجاری بریتانیا همچنین اعلام کرد که تاکنون خسارات زیست محیطی بر اثر این حادثه گزارش نشده است.
نام و پرچم نفتکش اعلام نشده و تاکنون هیچ گروهی مسئولیت حمله را بر عهده نگرفته است.
ینبع پایانه اصلی صادرات انرژی عربستان در دریای سرخ است. حوثی‌های یمن ۲۰ جولای ممنوعیت دریانوردی برای کشتی‌های سعودی و مرتبط با عربستان اعلام کردند و از آن زمان حملات متعددی به نفتکش‌ها را بر عهده گرفته‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/78014" target="_blank">📅 15:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j3MRHExG742cQox6TWwTZdKaf11uRg77YfowW34YviM-6qSvsYNpKhasUSgWs9xHabdJo0xpqY4boJbnDBuwUOk5n1qX07Bc7rxR87aPrCSZgziNsAqArVWV33QIucIfeUt1hlclBoX-_U_WitwU_ebFZCVQWhvCRFGxyLAtOIs9Z2oxzGK82DPg8EGsmssMwHNUP9rpOgZjYWurYnfeDS0VRsipcbE7BAImk5mfpjKzEKCFTIZlEvJ2vLNFiMEt-GR-f_ZRu0NH1OEHl2FZ9wBE6sK8zUu3Of5kSUmA2SgnsQhB5N6qwGXxqwF8JMgAGBD_tuo821Pdu8UTnV9dkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آتوسا جعفری»، زن ۲۷ ساله اهل سنندج، یکشنبه ۱شهریور۱۴۰۵ مقابل منزل خانوادگی خود با ضربات چاقو به قتل رسید.
رسانه‌های محلی و شبکه حقوق بشر کردستان گزارش داده‌اند که آتوسا جعفری هنگام خروج از خانه و پیش از سوار شدن به خودرو برای رفتن به محل کار، هدف حمله قرار گرفت و با ضربات متعدد چاقو کشته شد.
براساس این گزارش‌ها، عامل قتل همسر یا همسر سابق آتوسا جعفری بوده است. منابع محلی گزارش داده‌اند که او با هشت ضربه چاقو به قتل رسیده است.
درباره وضعیت تاهل آتوسا جعفری در زمان قتل روایت‌های متفاوتی منتشر شده است. شبکه حقوق بشر کردستان گزارش داده که او دو سال پیش از همسرش جدا شده و با مادرش زندگی می‌کرد، اما رسانه‌های محلی نوشته‌اند که آتوسا طی سه سال گذشته برای جدایی از همسرش به دادگاه مراجعه کرده بود و درخواست طلاق او پذیرفته نمی‌شد.
براساس روایت منابع محلی، آتوسا جعفری در این مدت بارها از سوی همسرش مورد خشونت، ضرب‌وشتم و تهدید قرار گرفته بود. یک‌بار نیز در نتیجه ضرب‌وشتم، دست او شکست.
شبکه حقوق بشر کردستان نوشته آتوسا جعفری کارمند اداره پست، دارای مدرک کارشناسی ارشد حقوق کیفری و مربی و داور رشته «کنگ‌فو توآ» بود.
این دومین مورد گزارش‌شده از زن‌کشی در کردستان طی چند روز است. روز ۲۹مرداد۱۴۰۵ نیز «لطیفه محمدزاده»، زن ۴۹ ساله اهل سقز، در یکی از جاده‌های روستایی این شهرستان توسط همسر سابقش با ضربات چاقو به قتل رسیده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/78013" target="_blank">📅 15:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MqlUcpUhkYAp8pLSOA0hHwISKjdM1jqPACM9gAxC0FmJN4Mxuq1Hj0K_A9hx11Bw3wvBfJFLKPnKgxvLo4qx-6biglO9dLC9QrTtMzb9HDf4qW85vja6eDfS1M44AMBkGEJX-PAl0S3xMpZFTSaFk-WlWilULNJYU46-I2XALobSf-0e1hDCU4MTT2v8TpcDKx9EWNzuwB8p8yjd-3MzHJJyShUGroajS6HK88CXzj9z94FovKywIpZMrZTuSaV9uoyu8ajc_jyM4Jk1IRaa9zeK5AMpV_L_p54MDvQ_I2ik-z30nYSkyUB0bZ5RqDihn8dQkT6t6PMly4uOIMm6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ شهروند بهائی از سوی دادگاه انقلاب ساری مجموعاً به ۲۶ سال و ۱۶۵ روز حبس تعزیری و ۷۶ سال محرومیت از حقوق اجتماعی محکوم شدند.
بر اساس دادنامه صادرشده در تاریخ ۲۹ مرداد ۱۴۰۵، راکوئل عطائیان، کیومرث اکبری، سهراب لقایی، زهرا گلابیان، بنفشه اسدیان عربی، فؤاد لقایی، آناهیتا کوشکباغی، نسیم صمیمی، حسین فنائیان، امیلیا فنائیان، ملودی صمیمی و سهیل حقدوست، شهروندان بهائی، توسط شعبه اول دادگاه انقلاب ساری به ریاست عمار رمضانی محکوم شدند.
در این رای خانم عطاییان به تحمل چهار سال حبس تعزیرى و ۱۰ سال محرومیت از حقوق اجتماعى محکوم شده و دیگر متهمان پرونده هر کدام به تحمل دو سال و ۱۵ روز حبس تعزیرى و شش سال محرومیت از حقوق اجتماعى محکوم شدند.
در دادنامه صادره، اتهام مطروحه علیه این شهروندان «انجام فعالیت‌های آموزشی و تبلیغی مغایر و مخل به شرع مقدس اسلام در راستای ترویج و ترغیت فرقه بهائیت» عنوان شده است. جلسات رسیدگی به اتهامات این شهروندان در تاریخ‌های ۱۰، ۱۱ و ۱۲ مردادماه ۱۴۰۵ در شعبه مذکور برگزار شده بود.
یک منبع نزدیک به یکی از این شهروندان بهائی در گفت‌وگو با هرانا ضمن تأیید این خبر، درباره روند رسیدگی به این پرونده اظهار داشت: «اولین جلسه رسیدگی به اتهامات این شهروندان در اردیبهشت‌ماه ۱۴۰۳ در شعبه اول دادگاه انقلاب ساری به ریاست شجاع ذوقی برگزار شد.
این شعبه به دلیل وجود نواقص در تحقیقات، پرونده را سه مرتبه به شعبه بازپرسی بازگرداند، اما به دلیل عدم رفع نواقص، پرونده از دستور کار این شعبه خارج شد. در ادامه، پرونده به شعبه ۱۰۴ دادگاه کیفری قائم‌شهر به ریاست رضا مجازی ارجاع شد و جلسات رسیدگی در تاریخ‌های ۲۱ و ۲۲ تیرماه ۱۴۰۴ برگزار شد.»
این منبع افزود: «در جریان این روند، سهیل حقدوست و همسرش راکوئل عطائیان بازداشت شدند و امکان حضور در جلسات رسیدگی را نیافتند. این دو پس از آزادی موقت، به‌صورت جداگانه از سایر متهمان مورد محاکمه قرار گرفتند. شعبه کیفری در ادامه با صدور قرار عدم صلاحیت، پرونده را مجدداً به شعبه اول دادگاه انقلاب ساری ارجاع داد و این شعبه پس از برگزاری سه جلسه رسیدگی، نهایتا اقدام به صدور رأی کرده است.»
وی همچنین گفت: «راکوئل عطائیان در جریان بازداشت سال گذشته با پرونده قضایی جدیدی مواجه شده بود که بنا بر تصمیم شعبه ۱۰۴ دادگاه کیفری قائم‌شهر، روند رسیدگی به آن با این پرونده ادغام شد و در نهایت هر دو پرونده به صدور رأی در شعبه اول دادگاه انقلاب ساری منتهی شدند.»
پیشتر، جلسات آخرین دفاع این ۱۲ شهروند بهائی در اسفندماه ۱۴۰۲، به‌صورت جداگانه در شعبه ششم بازپرسی دادسرای قائم‌شهر به ریاست رضا مجازی برگزار شده بود. همچنین پیش از آن، منازل این افراد توسط نیروهای امنیتی مورد تفتیش قرار گرفته و آنها با دریافت پیامک‌های جداگانه از تشکیل پرونده قضایی علیه خود در دادسرای قائم‌شهر مطلع شده بودند.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/78012" target="_blank">📅 15:47 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TD2s9g2ba8yHrIO11CqHSC9psN872qNDrmahqHlOjQjcSnAb0lAO1TmrEYWlLNex0TZNBcVSFjfJHuFvcX4xEc8u7vWL9FB5FpPf-Z4x4s2TF5jvi7gWrtwUD5IhjjB26P_5H0EPZ5o-i94j8UaRI8pRCo4UQupCFQhdxHPHyPte_8o2KZIxLpWbQPji75sJHxNLSvZ0EHKTX85CxbAdc2Rhd7wWsD-BZfYzELeRxuc8TLC-bHTTNoWA7IwWy2DT_WVmph57uogoxWHqm42WAM7JqXFs5lYgELSZKb74AQpk6XmS04F95lSkuU3L1J_HpLCfARAVvBDlETdPRXLTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگو با نیوزمکس گفت با وجود تلاش‌های جمهوری اسلامی برای بستن تنگه هرمز، آمریکا موفق شده است روزانه بین هفت تا ۱۵ میلیون بشکه نفت را از این مسیر خارج کند.
ونس گفت واشینگتن در تلاش است مانع وقوع بحران انرژی شود که به گفته او جمهوری اسلامی در پی ایجاد آن است. او افزود یکی از قدرتمندترین ابزارهای آمریکا، «وادار کردن تهران به پرداخت هزینه تلاش برای خفه کردن تجارت نفت و گاز» است. معاون رییس‌جمهوری آمریکا تاکید کرد جمهوری اسلامی توانایی قطع مسیرهای تجارت بین‌المللی را ندارد و این مسئله اهرم‌های فشار تهران را کاهش می‌دهد.
معاون رییس‌جمهوری آمریکا گفت واشینگتن ابزارهای متعددی برای مقابله با جمهوری اسلامی در اختیار دارد که به گفته او برخی «قاطع» و برخی دیگر اقتصادی هستند.
ونس همچنین تاکید کرد هدف نخست و اساسی حضور آمریکا در خاورمیانه جلوگیری از دستیابی جمهوری اسلامی به سلاح هسته‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78011" target="_blank">📅 04:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78010">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVSRaSMgECnLE4mQ54QDwplBzBJCGIoIqx3vd0Zbo-PrViqOfFZebCK6SbODIq0sdskRpS4XmvAwOohpvhbbg_Zs8IAnhK2-juNwVtjsaoPjZB60inlEjX2k3cKPDl5IYzIPpZlnEKKXtVVEv8Y53oYjsvT41Qger5UWMuvocDhkVOe3Cp0Bl3xcR8jR0wZNY0f2Gyc37wZe8VTNbjbW8NsgL4EzQ385TmBOy7NUG97B9H-xSwVcD3RNfx5pgm7i-8hm8EzKhe8Ryd6Kw0PG5I3KXIwkXpgp-b1wFl_hH7JrCqvQsmShmjESoincilAChu_cvq5gto35zsThJcYcyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اسکات بسنت، ترجمه ماشین:
رئیس‌جمهور ترامپ توانمندی‌های نظامی ایران را در هم شکسته، نزدیک به ۱۰۰ درصد کارخانه‌های نظامی آن را نابود کرده و برنامه هسته‌ای‌اش را مدفون کرده است. اکنون وارد مرحله نهایی می‌شویم. با سپیده‌دم، یک «D-Day اقتصادی» آغاز می‌شود — بزرگ‌ترین تهاجم مالی واحدی که تاکنون علیه یک دشمن بسیج شده است.
جمهوری اسلامی با جا زدن اخاذی به‌عنوان تضمین‌های امنیتی، به حیات خود ادامه داده است. این رژیم از محاسبه‌ای قدرت گرفته که در آن، تلافی ایران قطعی و اجرای اقدامات از سوی آمریکا قابل مذاکره تلقی می‌شود. تحت ریاست‌جمهوری ترامپ، آن دوران به پایان رسیده است. و کسانی که از خطر سرپیچی از تهران می‌ترسند، نباید هزینه آزمودن واشنگتن را دست‌کم بگیرند.
رئیس‌جمهور شرایطی را فراهم کرده است تا از هر نهاد، هر اختیار و هر اقدامی که بسیاری تصور می‌کردند هرگز به آن متوسل نخواهیم شد، استفاده شود. هدف ما قطع کردن هر شریان اقتصادی‌ای است که این رژیم استبدادی را سرپا نگه می‌دارد، تا زمانی که تهران تنها بماند.
SecScottBessent
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/78010" target="_blank">📅 03:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، به کشورهایی که به روابط مالی و تجاری خود با جمهوری اسلامی ادامه می‌دهند هشدار داد که باید میان همکاری با تهران و حفظ دسترسی به ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
اسکات بسنت، وزیر خزانه‌داری آمریکا با انتشار مقاله‌ای در روزنامه فایننشال تایمز تاکید کرد دولت ترامپ قصد دارد با قطع همه شریان‌های مالی و تجاری جمهوری اسلامی، تهران و کشورها و نهادهای همکار با آن را در انزوای کامل اقتصادی قرار دهد.
او که قرار است دوشنبه دوم شهریور در کنفرانسی مطبوعاتی جزییات اقدامات تازه دولت آمریکا علیه جمهوری اسلامی را اعلام کند، هشدار داده است که ادامه همکاری با حکومت ایران، دسترسی این کشورها به سرمایه و بازارهای جهانی را به خطر خواهد انداخت.
وزیر خزانه‌داری ایالات متحده از آغاز مرحله‌ای تازه و گسترده در فشار اقتصادی علیه جمهوری اسلامی خبر داده و آن را «روز سرنوشت‌ساز اقتصادی» و بزرگ‌ترین تهاجم مالی سازمان‌یافته علیه یک دشمن توصیف کرده است.
بسنت در این یادداشت با اشاره به کنفرانس تهران در سال ۱۹۴۳ نوشت رهبران متفقین در آن زمان در پی یافتن راهی برای وارد‌کردن «بیشترین فشار ممکن بر دشمن» بودند. به گفته او، تاریخ اکنون همان پرسش را بار دیگر پیش روی تهران قرار داده و زمان آن رسیده است که ایالات متحده با تمام توان به آن پاسخ دهد.
او تاکید کرد دونالد ترامپ، رییس‌جمهوری آمریکا، با استفاده از قدرت نظامی ایالات متحده بخش قابل‌توجهی از توانایی‌های نظامی حکومت ایران را از میان برده و برنامه هسته‌ای این کشور را تضعیف کرده است. بسنت افزود واشینگتن اکنون وارد «مرحله نهایی» شده و می‌خواهد فشار نظامی را با حمله‌ای گسترده به منابع مالی و تجاری جمهوری اسلامی تکمیل کند.
وزیر خزانه‌داری آمریکا در ادامه، جمهوری اسلامی را حکومتی خواند که طی ۴۷ سال گذشته هم در داخل ایران و هم در خارج از مرزهای آن نقشی مخرب داشته است. او گفت فساد و سیاست‌های حکومت، اقتصادی را که می‌توانست یکی از قدرتمندترین اقتصادهای جهان باشد به ویرانی کشانده و مردم مبتکر و کارآفرین ایران را با سرکوب روبه‌رو کرده است.
بسنت همچنین جمهوری اسلامی را متهم کرد که در خارج از ایران، شبکه‌ای از گروه‌های نیابتی را برای ادامه فعالیت‌های خشونت‌آمیز و تروریستی حفظ کرده است. او گفت ایالات متحده بهای سنگینی در رویارویی با این شبکه پرداخته، هرچند تنها کشوری نیست که با پیامدهای فعالیت‌های آن مواجه شده است.
به گفته وزیر خزانه‌داری آمریکا، با وجود گستردگی تهدیدهای ناشی از سیاست‌های تهران، واشینگتن در بسیاری از موارد در عزم خود برای مقابله با جمهوری اسلامی تنها مانده است.
بسنت کاهش شدید ارزش ریال و نرخ بالای تورم در ایران را نتیجه سیاست‌های دولت ترامپ دانست. او گفت اقتصاد ایران چنان تضعیف شده که ارزش پول ملی این کشور به پایین‌ترین سطح خود رسیده و تورم نیز به یکی از بالاترین سطوح تاریخی نزدیک شده است.
او یادآور شد آخرین امید جمهوری اسلامی، ادامه همکاری کشورهایی است که از روی ترس یا ملاحظات اقتصادی تصور می‌کنند سازش با تهران می‌تواند امنیت یا صلحی پایدار برای آنها به همراه آورد.
وزیر خزانه‌داری آمریکا بدون نام‌بردن از کشور مشخصی گفت برخی دولت‌ها و نهادهای خارجی همچنان نفت ایران را خریداری و حمل می‌کنند و انتقال منابع مالی این کشور را از طریق صرافی‌ها و مناطق آزاد تجاری تسهیل می‌کنند.
به گفته او، برخی کشورها همچنین به پروازهای ایران اجازه فعالیت می‌دهند، کشتی‌ها را به نمایندگی از تهران در دفاتر خود ثبت می‌کنند و بر انتقال سوخت میان کشتی‌ها در دریا و استفاده غیرقانونی از نظام بانکی‌شان چشم می‌بندند. بسنت این کشورها را متهم کرد که هم‌زمان می‌کوشند میزان همکاری خود با جمهوری اسلامی را پنهان کنند.
او گفت این کشورها بر اساس این محاسبه عمل می‌کنند که مماشات با تهران، در مقایسه با ایستادگی در برابر آن، گزینه‌ای امن‌تر است؛ اما باید پیامدهای کمک به بقای جمهوری اسلامی را نیز در نظر بگیرند.
بسنت برای توضیح این دوراهی به دیدگاه بلز پاسکال، فیلسوف فرانسوی قرن هفدهم، اشاره کرد. به گفته او، پاسکال معتقد بود عدم قطعیت، انسان‌ها یا ملت‌ها را از داوری معاف نمی‌کند، بلکه آنها را ملزم می‌کند خطرها را دقیق‌تر ارزیابی کنند؛ زیرا در چنین شرایطی بهای یک محاسبه اشتباه می‌تواند سنگین‌تر باشد.
وزیر خزانه‌داری آمریکا گفت «شرط‌بندی پاسکال» اکنون درباره شریان‌های حیاتی اقتصاد ایران مصداق پیدا کرده است. به گفته او، کشورهایی که برای در امان ماندن از واکنش تهران همچنان منابع مالی حکومت ایران را تامین می‌کنند، در عمل همان حکومتی را تقویت می‌کنند که از آن هراس دارند.
بسنت هشدار داد که این کشورها از مرز تحمل آمریکا عبور کرده‌اند و باید میان ادامه همکاری با جمهوری اسلامی و حفظ روابط اقتصادی خود با ایالات متحده و نظام مالی جهانی یکی را انتخاب کنند.
او گفت ترامپ در حال انجام کاری است که روسای‌جمهوری پیشین آمریکا از آن خودداری کردند: پایان‌دادن به تهدیدی که دولت‌های قبلی به مدیریت و مهار آن رضایت داده بودند.
به گفته بسنت، طبقه سیاسی آمریکا برای چند دهه چرخه‌ای بی‌پایان از اقدامات تحریک‌آمیز جمهوری اسلامی را پذیرفت، در حالی که باید منافع ایالات متحده را با قاطعیت بیشتری پیش می‌برد. او گفت نسل دیگری نباید زیر سایه تهدید نیروهایی زندگی کند که شعار «مرگ بر آمریکا» سر می‌دهند و در پی تحقق اهداف هسته‌ای جمهوری اسلامی هستند.
وزیر خزانه‌داری آمریکا استدلال کرد که انزوای کامل مالی تهران می‌تواند نیاز به استفاده مستقیم از نیروی نظامی ایالات متحده را کاهش دهد و هم‌زمان امنیت و آزادی عمل متحدان واشینگتن را افزایش دهد.
او همچنین برای کشورهایی که روابط مالی و تجاری خود را با ایران قطع کنند، مشوق‌هایی در نظر گرفت. بسنت گفت قطع همکاری با تهران می‌تواند دسترسی این کشورها به سرمایه جهانی را افزایش دهد، اعتماد به بازارهایشان را تقویت کند و جایگاه مورد نظر آنها را در اقتصاد بین‌المللی بهبود بخشد.
در مقابل، او هشدار داد کشورهایی که روابط خود را با تهران حفظ کنند، ممکن است مسیر دستیابی به رفاه پایدار را از دست بدهند. به گفته او، در کشورهایی که اعتماد سرمایه‌گذاران و بازارهای جهانی به آنها کاهش می‌یابد، فعالیت‌های مالی غیرقانونی معمولا گسترش پیدا می‌کند.
بسنت گفت هر کشوری که به‌عنوان شریان مالی یک حکومت رو به زوال عمل کند، باید انتظار داشته باشد در انزوای آن نیز سهیم شود. او افزود کشوری که به پناهگاهی برای فعالیت‌های تروریستی تبدیل شود، از دید ایالات متحده به بازیگری مطرود در جهان بدل خواهد شد.
وزیر خزانه‌داری آمریکا جمهوری اسلامی را متهم کرد که طی سال‌های گذشته، اخاذی را در قالب تضمین‌های امنیتی عرضه کرده و از ترس کشورهای دیگر نسبت به اقدامات تلافی‌جویانه تهران بهره برده است.
به گفته او، قدرت جمهوری اسلامی بر محاسبه‌ای استوار بوده که واکنش [حکومت] ایران را قطعی، اما اجرای تهدیدهای آمریکا را قابل‌مذاکره می‌دانسته است. بسنت گفت با بازگشت ترامپ به قدرت، این دوره به پایان رسیده و کشورهایی که از ایستادگی در برابر تهران هراس دارند، نباید هزینه آزمودن اراده واشینگتن را دست‌کم بگیرند.
او افزود ترامپ شرایطی فراهم کرده است که دولت آمریکا بتواند از همه نهادها، اختیارات قانونی و ابزارهایی استفاده کند که بسیاری تصور می‌کردند واشینگتن هرگز به آنها متوسل نخواهد شد.
بسنت هشدار داد هرگونه ارتباط باقی‌مانده با تهران می‌تواند انزوای اقتصادی کشورها و نهادهای مرتبط را تسریع کند؛ خواه این ارتباط آگاهانه ایجاد شده باشد و خواه دولت‌ها و شرکت‌ها عمدا آن را نادیده گرفته باشند.
وزیر خزانه‌داری آمریکا همچنین درباره احتمال واکنش نظامی جمهوری اسلامی هشدار داد. او گفت اگر هم‌زمان با تضعیف اقتصاد ایران و کاهش تسلط حکومت بر قدرت، تهران علیه نیروهای آمریکایی یا کشورهای همسایه در خلیج فارس اقدام نظامی انجام دهد، ترامپ «به‌سرعت و قاطعانه» پاسخ خواهد داد.
بسنت در پایان هدف دولت آمریکا را قطع همه شریان‌های اقتصادی توصیف کرد که به بقای جمهوری اسلامی کمک می‌کنند. او گفت فشارها تا زمانی ادامه خواهد یافت که تهران در انزوای کامل قرار گیرد.
او بار دیگر با اشاره به پاسکال، تصمیم کشورهای همکار با حکومت ایران را نوعی انتخاب درباره آینده آنها دانست و پرسید آیا این کشورها حاضرند در برابر موج تازه فشارهای آمریکا، آینده خود را به خطر بیندازند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78009" target="_blank">📅 03:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtN0lNicDXMPreUX_L5Kd8fEfsFhYNzpQtbk-p1XfnsjkatXjQ4We0E_VovhCGWZq86-DHgiWRx5h6R7P_Z7D18u1hRp3mT-_X30b9ywjQgp_7b4bk--6HWPNyVC9OgFOuN48-v-UzDVmfNoTfvgRkkXLeFfz6uZy2HLOLyh-4fU9kwXdeiIFcSZQyza6rN1oi4bDRcW3f2AsXuyfd-24iC39NSKtIKHTsEWTTogRSLCU1ZWe8GF2OTTschKd703sFV-KpEjpCUGQiqPIabeeCim2vE7K6QwpJL8EhqBLRfdFHGGsKrEp0l6c_bi_UJEQ--l--vj20_R4-uTaJyEgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهای دلار آمریکا در بازار آزاد ایران روز یک‌شنبه اول شهریور از مرز ۲۰۰ هزار تومان عبور کرد و رکورد تازه‌ای به جا گذاشت؛
همزمان پوند بریتانیا از ۲۷۲ هزار تومان گذشت و یورو نیز به محدوده ۲۳۴ هزار تومان نزدیک شد.
قیمت سکه امامی نیز از ۲۱۸ میلیون تومان فراتر رفت.
این جهش قیمت‌ها در ادامه روند کاهش ارزش ریال و همزمان با تشدید فشارهای سیاسی و اقتصادی بر جمهوری اسلامی رخ داده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78008" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UjJDMz71LWcHtlLD5ZUjQBk-oCO0WMIsGGD5VeKsurxZfQum3Wbf9wHL1Ezv4MiRhd7a4qT7KsiuP2OXdBOzK2SRKlJn-aFFrMmNCcqmoRQwQz1_hIlc5BSyepq4SEMoEBwbjFzSFJfOoc_KF55pMNkO33AsZrt3dOX-x94yLfXZOq9CpiLrZJlAmYxpT0H79KU8j6g3FTnI4Cszsnn5S9OBlhfG2Z01o1cXkPsiUdVLklilzwTWyMv1wWN3h6_IIbwv0CRj050GCdPBPsgC2ZNO4mGE_eSRQDAVN-I17ve9YNp1WnCNIoFwNGvMyQxH2FD1MiNUY_XiOo8uO8W-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیر رئیسیان، وکیل حسین شنبه‌زاده، از صدور حکم بدوی موکلش در پرونده‌ای جدید خبر داده است.
بر اساس این حکم، شنبه‌زاده به اتهام «نشر اکاذیب به قصد تشویش اذهان عمومی» به یک سال حبس تعزیری محکوم شده است.
رئیسیان در حساب کاربری خود در شبکه اجتماعی ایکس نوشته است که این پرونده مربوط به پیامی است که شنبه‌زاده از زندان و به مناسبت روز تولدش برای دوستانش فرستاده بود.
او با انتقاد از حکم صادرشده نوشته است: «فقط تصور کنید یک زندانی با استناد به "نحوه انتشار در رسانه معاند فضای مجازی" به حبس محکوم شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78007" target="_blank">📅 16:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YcQ2WEUeeJhpdVQXklEKK12fIUh-M_e9OkAmiebNg_-9zTfl78UD_I62_LjlpRtgcrMfDDXuP4ivXUfYDvmx1x8QqUEFyc10b57Klnri5FF_1qSB_1cd6y30IHhpmiX6if54IvPprTxiAGm30AVn0ObtljxtSvbhJ-9v3zJ-KLsSDzZ3s6MSsDmTEIxpwzVSuXkytVWM-DKaKSDZjCoYPXojnr9xF3Ge0BaHUnUqS3M0PBK62dBXP1jf6CfT7Uk4akTexo807QlUYFyg-v2AdkS9B4BhLb5z1YOA6xh50KA-mVX-DSfxPXJRqIMn9pH7AkZ72u5vYm59CbIXBezPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی از اجرای حکم اعدام «مجید آدینه»، یکی دیگر از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴ در کرج، خبر داده است.
براساس گزارش تسنیم به نقل از قوه قضاییه، این حکم صبح یکشنبه اول شهریور ۱۴۰۵ اجرا شد.
مجید آدینه روز ۱۹ دی‌ماه ۱۴۰۴ در محدوده محمدشهر کرج بازداشت شده بود.
مقام‌های قضایی مدعی شده‌اند که هنگام بازداشت او یک قبضه کلت کمری، سه خشاب، ۳۰ فشنگ، دو شوکر برقی، دو افشانه گاز اشک‌آور، یک اره برقی شارژی و یک بطری بنزین همراه داشته.
قوه قضائیه اعتراضات دی‌ماه را مطابق روایت رسمی جمهوری اسلامی «کودتا» خوانده و آدینه را به همکاری با آمریکا، اسرائیل و آنچه «گروه‌های متخاصم» نامیده، متهم کرده است.
دادگاه انقلاب کرج او را با اتهام «محاربه از طریق تحریق عمدی» و براساس قانون موسوم به «تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی و کشورهای متخاصم» به اعدام و مصادره اموال محکوم کرده بود.
اطلاعاتی درباره دسترسی آدینه به وکیل انتخابی، روند دادرسی، زمان برگزاری دادگاه و نحوه اخذ اظهارات او منتشر نشده است.
اعدام مجید آدینه در ادامه اجرای احکام اعدام علیه بازداشت‌شدگان اعتراضات دی‌ماه انجام شده است. بیش از ۳۰ کشور روز ۲۱ مرداد ۱۴۰۵ با انتشار بیانیه‌ای مشترک، ادامه صدور و اجرای احکام اعدام برای معترضان ایرانی را ابزاری برای «ساکت‌کردن صدای مخالفان» خواندند و محکوم کردند.
عفو بین‌الملل نیز گزارش داده است که جمهوری اسلامی در سال ۲۰۲۵ دست‌کم دو هزار و ۱۵۹ نفر را اعدام کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78006" target="_blank">📅 16:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4d23144315.mp4?token=O5iXlppfYMGwqIloNbCfWXuDRScX2CW3lZmmZcaYj65fOnlZKEDuKjZYVIElBkT1CKH5rykWu5LGqJDz9WKrsCZVeUbIenctdHo5K4urDt6pTAX5ONIe_OmYsG-O7SOmBhkI2AWTJ5O6Fo_sstbGdxN0684SCuVraTdhxhLzl0KLf1OE0hHGbqA6-L27fNQCDN8OQvpEi0tS0QUb5hKrjnnQ8g6Mua8bWi6wfJF5nzSVdDd1P-YW6xtOgN1AyLA6ic1fTOfKNNTVo_S_tyQaxeIuZ8kU4PCDojKWc-4-anjYwjeOZUEbYoX49KmX0mvEhsaFMJ7AlG3TqUHgV13ItA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4d23144315.mp4?token=O5iXlppfYMGwqIloNbCfWXuDRScX2CW3lZmmZcaYj65fOnlZKEDuKjZYVIElBkT1CKH5rykWu5LGqJDz9WKrsCZVeUbIenctdHo5K4urDt6pTAX5ONIe_OmYsG-O7SOmBhkI2AWTJ5O6Fo_sstbGdxN0684SCuVraTdhxhLzl0KLf1OE0hHGbqA6-L27fNQCDN8OQvpEi0tS0QUb5hKrjnnQ8g6Mua8bWi6wfJF5nzSVdDd1P-YW6xtOgN1AyLA6ic1fTOfKNNTVo_S_tyQaxeIuZ8kU4PCDojKWc-4-anjYwjeOZUEbYoX49KmX0mvEhsaFMJ7AlG3TqUHgV13ItA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی، می‌گوید از نظر حکومت ایران هر کشوری که با آمریکا در ایجاد محدودیت اقتصادی بیشتر علیه ایران مشارکت کند، «دشمن» تلقی می‌شود و تهدید کرد در چنین صورتی این کشورها هدف حمله قرار خواهند گرفت.
محسن رضایی در یک گفت‌وگو تلویزیونی که شامگاه شنبه ۳۱ مرداد از صداوسیما پخش شد، همچنین تهدید کرد اگر طرح جدید آمریکا علیه ایران برای ایجاد محدودیت اقتصادی بیشتر اعمال شود، جمهوری اسلامی اجازه نخواهد داد «یک قطره نفت نه تنها از تنگه هرمز که از کل خلیج فارس» خارج شود.
این اظهارات تازه‌ترین واکنش مقامات تهران به تحریم‌هایی است که دولت آمریکا قرار است روز دوشنبه آتی جزئیات آن را اعلام کند و اسکات بسنت، وزیر خزانه‌داری آمریکا، پیشاپیش آن را «سخت‌ترین تحریم‌های تاریخ» علیه ایران خوانده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78005" target="_blank">📅 04:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pwMGRJhPIBUrZR_iuLdT-ONzbCzyLsRdHSTP4TWty5kYpsul_iXof0l-pChBGIhGQQZEBYzS2E5k7prikeCmx3KNXqfASFYNmGVH_gXOh4QyBFXLjXIbZbQUR8pJLVocXV3Sqp7C_YmN2B8Qz6WUSprBfAisWJguH4RIImKC6xZ-GYJ0hnndsi5ziww1wDI0DapN5HoR3gME-bU03uvAkG_C3vum89RS-8M13SJAO191pvdHYnN-smh_WIEG7IIg2Jv2qFZSOwvz1VEEiFxzxtpshfsRHyDVOq3vh1iPl4evzoBUFOwWK8vNe8O4lgAWbahD2DQ5ShUU8DQ4FRFEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، با انتشار پستی در شبکه اجتماعی تروت‌سوشال بر عبور کشتی‌ها از تنگه هرمز با اسکورت نیروهای‌ آمریکایی تاکید کرد. ترامپ مطلبی از مارک تیسین، مفسر آمریکایی را بازنشر کرد که در آن، تیسین به آمار خروج بیش از ۱۰۰۰ کشتی از تنگه هرمز با اسکورت نیروهای آمریکایی اشاره دارد.
@
VahidHeadline
دونالد ترامپ، رییس‌جمهوری آمریکا، بار دیگر تصویری از نقشه تنگه هرمز را در تروت سوشال منتشر کرد که در بالای آن عبارت «قلمرو جدید آمریکا» دیده می‌شود.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/78004" target="_blank">📅 02:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHUJe82LNPMaikvw-08w0VXr8nplbnAV0RDihWpYozw8Nvu5zXmi7Q-20usuRIiU8l0GQMVpyX1fI3xsVMUNURe58t-yVz8KSqs1Tx-5UYidb9PaGMHD5_oWSLeDfYmZFQEdDSLrdH2paVtEa46r2TYSgspf6eu3OmrNNw5Eo4bM3qwux_h6PN3bk6pzfIyVeUq19lgpJ5ckIXA7yKdlTXMjQBacQw5TqNKxc8nYV9yj_ho0DsFcgeEL8PpCgRKqta6ynpyuKRFCQ-ZbFrhhwX5GJ2cQV1RXs3cmVR5TYpO0tKpKAAEfYviqHnHKgx57yazJcrQ8mcvQ2Pl6cMmW0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باراک راوید، خبرنگار وبسایت اکسیوس، روز شنبه ۳۱ مرداد ۱۴۰۵ در شبکه ایکس به نقل از سه مقام آمریکایی گزارش داد که حدود ۴۰ نفتکش شامگاه جمعه از مسیر عمیق جنوبی تنگه هرمز وارد یا خارج شده‌اند و حدود ۱۶ میلیون بشکه نفت از این مسیر به خارج از تنگه منتقل شده است.
همزمان، رسانه‌های دولتی ایران مدعی شدند، تهران پس از درخواست‌های مکرر بغداد، به شماری از نفتکش‌های عراقی اجازه عبور از تنگه هرمز را داده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78003" target="_blank">📅 18:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HGgw2c05Qt8WkoKDMWG2xdl_a0_nLGgVd2qkbYD6vsHjXlUxqWsBSZB9GD-D7ltGKkyHza6QRLELrd2JUUM3en358IdmsY-PfW3autieqsg9Uadwy1vNhmgX1sOpNyGCaWD2buZLJfN6KgFH9SiPPbZgiKoC2s9dMBeMxUBMyBuPiKtanZKeRYXs_6I1clC6reEdwpRf9j6kW8QNPEjcRubPvsTDP6Yx_hn0zCSZCXtatW2CvX_Q-c-Fx9r9tY6PhRO_cJQTBG-KJ5_-XhmQszPVajy1sVT57IoOQ-fuRNRcCTafYxMjS3o3aB7_R94g186LCUDRbafifRe-bmjQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به پیمان جبلی، رییس سازمان صدا و سیما، ضمن حمایت از رویکرد این سازمان، نوشت که صدا و سیما در دوره جنگ اخیر، «در ثبت و ماندگار ساختن این حماسه، سهمی ارزشمند در تقویت جبهه رسانه‌ای انقلاب اسلامی بر عهده گرفت.»
وحیدی همچنین عملکرد صدا و سیما را «مجاهدت ارزشمند و نقش‌آفرینی موثر» توصیف کرد.
این در حالی است که در روزهای اخیر، محمدباقر قالیباف و مسعود پزشکیان صراحتا از عملکرد صدا و سیما انتقاد کرده بودند.
محمدباقر قالیباف ۲۷ مردادماه گفته بود که صدا و سیما در زمینه «جنگ شناختی» تاکنون موفقیت‌های لازم را نداشته است. رییس مجلس همچنین گفته بود: «تبیین ناکارآمدی‌های ساختاری، رویکردی و عملکردی صدا و سیما فرصتی مبسوط می‌طلبد.»
مسعود پزشکیان نیز در چند نوبت از عملکرد این سازمان انتقاد کرده است. پزشکیان ۱۰ خردادماه گفته بود روایت‌های صدا و سیما از شرایط کشور غیرواقعی است و این رسانه نیازمند بازنگری جدی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78002" target="_blank">📅 17:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B9aXg9rSb7bVV1G9UuXVXKs7OBryzH4lxpZMMFXhVcTOL3aw1xsH4Nn1exHlLabB4L3G3DMlFHt-x7T7vsTS5aE-ObLCxvgx6dv1EFRLShao-6t-Y9zgCntA8wUl8nwDLTjlWUUFaG-5AaqHYrl9Qm0tFoHHFAzlGBd2mgKyjXUBfRl4M4OcBzM-3s-8nWgKry5U37XVL6JjGZsBHXvXkz3YnhnfAcIviNjoD5BFg8m_dj0IwRfjhdoSzEXO_gWrOdjgxP0wP95ArEfXf-UA_-nOgCyQNxKVMp-V3xGHmLKP4oLPm5NHsCIO1dNhaFUlKdO1NapfJf71RtPPKDrfOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا عارف، معاون اول رییس دولت در ایران، با تاکید بر ضرورت آنچه «اصلاح الگوی مصرف انرژی» خواند، گفت: «باید مردم را توجیه کنیم تا بدانند که اکنون بخشی از درآمدهای کشور صرف تامین بنزین می‌شود و این موضوع هزینه و فشارهایی را به بخش‌های دیگر تحمیل می‌کند.»
isna.ir
عارف شنبه ۳۱ مرداد در «همایش ملی صنعت، معدن و خدمات سبز» با اشاره به تفاوت مصرف سوخت میان گروه‌های درآمدی گفت میزان مصرف دهک دهم، ثروتمندترین دهک جامعه، حدود ۲۳ تا ۲۴ برابر دهک اول است.
عارف در ادامه، مخالفت با گران شدن بنزین را به واکنش اقشار کم‌درآمد به تغییر سیاست‌های مرتبط با مصرف انرژی مرتبط دانست و گفت: «وقتی قرار است اصلاحی در این زمینه انجام شود، اتفاقا بخش‌هایی از اقشار آسیب‌پذیر و کسانی که به هر حال در زندگی با مشکلاتی روبه‌رو هستند، تحریک می‌شوند که بگویند بنزین نباید گران شود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/78001" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UrEfChAGaE-BZZ8NRmB1GhHALa87vKg97RZk64ILv1Sno2rtNGw-iV1_h3rlPiY3k-6C24i3-_0i6NCqhkiWvluB3d5jxbHp_dNEy94BCAI4R5bTVyrJ8EHl5xmfKf6XmCMbmNcurlPBDpbSmvwgZS3i5WH_C9Q7UUy9O1fXtwYP0si_wle_Ly4fmS4ni6isLw4I497TxnpfKRNa7NTLgUPvpm-6E88Xk2-bn5YbpRsNvYIlY2_QtCb4JFYbkje2tZY6MZ_AG7dPlqcUdkah1BpRNF0x4AtFDGlHvv110LWV2IVRtYgCpwT7EGdsfr2rkQBedqsply6wYCWIr7FMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، گفته است پس از اعتراض به کشتار معترضان در دی‌ماه ۱۴۰۴ تهدید شده و مسئولان مانع حضور او در مسابقات قهرمانی جهان شده‌اند.
فصیحی در
صفحه اینستاگرام
خود نوشت که در این مدت بارها به او هشدار داده‌اند: «مراقب رفتارت باش، می‌دانی که قهرمانی جهان و بازی‌های آسیایی در پیش است.»
او در ادامه نوشت: «همان شد. قهرمانی جهان را که بزرگ‌ترین رویا و آرزوی هر ورزشکاری است، از من گرفتند؛ بازی‌های آسیایی را هم خودم تقدیم‌تان می‌کنم.»
این دونده ایرانی گفته است تنها ورزشکار ایران بوده که سهمیه حضور در مسابقات جهانی را به دست آورده و فصل را در جایگاه نخست رده‌بندی آسیا به پایان رسانده، اما مسئولان از ثبت‌نام او در این رقابت‌ها خودداری کرده‌اند.
فصیحی درباره سکوت خود در ماه‌های گذشته نوشت: «صدها بار نوشتم و پاک کردم. هیچ جمله‌ای نمی‌توانست عمق ظلم، بی‌عدالتی و خیانتی را که در حق من شد، توصیف کند.»
او بدون اشاره به هویت افراد یا نهادهایی که تهدیدش کرده‌اند، گفته است پیگیری حقوق خود را از مسیرهای قانونی آغاز کرده و اجازه نخواهد داد حقش «به‌عنوان یک ورزشکار زن ایرانی» پایمال شود.
این ورزشکار در پایان نوشت: «من همچنان می‌دوم؛ برای مردمم، برای رویاهایم.» او همچنین ابراز امیدواری کرد که «عدالت جای ظلم، شایستگی جای رانت و پاکی جای فساد را بگیرد.»
فرزانه فصیحی پیش‌تر در بهمن‌ماه ۱۴۰۴ و پس از سرکوب اعتراضات سراسری دی‌ماه، با انتشار متنی در اینستاگرام از خشم و اندوه خود نسبت به کشته‌شدن معترضان نوشته بود.
فصیحی از چهره‌های مطرح دوومیدانی زنان ایران و دارنده رکورد دوی ۶۰ متر داخل سالن ایران است. او در بازی‌های المپیک توکیو و پاریس نیز حضور داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/78000" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rxtT1g1C8lsJlxxS8ZwRbtTy4Ujs6WsWow822crVmZWWxqIFDqlIG1MqIuMeYShi27hcLw3Yyzs30gaGwTdjBaObBzE642J_7ssdxgFOxIaCwLDVtWH4wUbPm8GQgrUzPhqPdNLnIFuAAuLp3kLEv6ydwYCN-qgKNdgy-TMu_epTh-lutpxCXYJaUtpVx_e5-CTnm8xN0VMfaUBwltcS0ClKmPZy0Fxlw1hgHA7BrpHX0b_fGcnDhsgYLMxkC3XWW9yVC6a2VSkrgFZHCY3v7s5uQ_3EQehtM2TrCNup2iGFNL5E1ciA62ErBaEmSJm8W5NYcqus4G2m4pEurgot8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف در شبکه اجتماعی «ایکس»، بدون نام بردن از کشوری نوشت: «پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی جدید و همکاری‌های اقتصادی در منطقه دریافت کرده‌ایم.»
او مدعی شد آمریکا با «قلدری» و نادیده گرفتن منافع متحدان خود به سود اسرائیل، امنیت آنها را به خطر انداخته است و افزود یک «نظم بومی و مستقل» می‌تواند صلح و امنیت واقعی را برای منطقه به همراه بیاورد. رسانه‌های حکومتی ایران این اظهارات را واکنشی به تهدیدهای دولت دونالد ترامپ علیه کشورهایی دانسته‌اند که به همکاری اقتصادی با تهران ادامه می‌دهند.
اظهارات قالیباف در شرایطی مطرح می‌شود که روابط جمهوری اسلامی با برخی کشورهای عربی خلیج فارس در روزهای اخیر با تنش‌های تازه‌ای روبه‌رو شده است.
علی عبداللهی، رییس ستاد کل نیروهای مسلح جمهوری اسلامی، روز چهارشنبه به کشورهای حاشیه جنوبی خلیج فارس درباره «هرگونه کمک یا تسهیل» برای نیروهای آمریکایی هشدار داده بود.
عبداللهی گفت جمهوری اسلامی فعالیت هواپیماهای نظامی آمریکا، از جمله هواپیماهای سوخت‌رسان مستقر در پایگاه‌های منطقه را زیر نظر دارد و هرگونه کمک به ارتش آمریکا را به منزله مشارکت در عملیات نظامی این کشور تلقی خواهد کرد. او خطاب به کشورهای منطقه گفت: «هیچ‌چیز از دید ما پنهان نیست.» کشورهای عربی منطقه پیش‌تر مشارکت در حملات آمریکا به ایران یا اجازه استفاده از خاک خود برای این حملات را رد کرده‌اند.
همزمان، امارات متحده عربی تمام فعالیت‌ها و مبادلات تجاری و تراکنش‌های مالی خود با ایران را تا اطلاع ثانوی متوقف کرده است؛ اقدامی که برای جمهوری اسلامی، با توجه به نقش امارات به‌عنوان یکی از مهم‌ترین شرکای تجاری ایران، اهمیت ویژه‌ای دارد.
این تصمیم پس از آن اعلام شد که مقام‌های اماراتی گفتند دو موشک بالستیک شلیک‌شده از ایران را شناسایی کرده‌اند. بر اساس اعلام ابوظبی، یکی از موشک‌ها خارج از آب‌های سرزمینی امارات و دیگری در داخل این محدوده به دریا سقوط کرده است. تهران این اتهام را رد کرده است.
ادعای قالیباف درباره درخواست کشورهای همسایه برای ایجاد ترتیبات امنیتی تازه در حالی مطرح شده که او نام این کشورها، محتوای پیام‌های ادعایی یا جزییات طرح مورد نظر تهران برای «نظم بومی و مستقل» را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/77999" target="_blank">📅 17:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L_5F9_2MgegVpuZ8y6Ba7Y4mWgAua_jysWX5eiauXSjA5i942cSnnPy7Wuj1hW8Mt-Lc03RESDvynsoOEs0NlOJ4qzsNraoPtgr4NasewETXk4nNLT5LDrXhNNOsMMXvaeZykLfkvcmYKhZ9fI2MW10LcTeDsKIfTeP6sO4CU04mZJ4aJ_8D2ghzbTmd9osrZIP41nM_0QUzvsvmr4xaPxPozuXDZFliGgodWwlf0OT_HWcEWp7hfuykEno_BSihIy6-3YPPbTUdSdBSCWZxwDgIBssXY5gtu5_nyPRu7liA7WNnkF2QJtFDrfvgGJ1QtWQySatgJfIv024ikTdmzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«آرزو کشور» مالک و مدیر یک سالن زیبایی در اصفهان به اتهام «ارتباط با دول متخاصم» به ۱۲سال حبس محکوم شده است.
آرزو کشور از بهمن‌ماه سال گذشته، در زندان «دولت‌آباد» اصفهان نگهداری می‌شود.
آرزو کشور پس از بازداشت در بهمن‌ماه گذشته، در سلول انفرادی نگهداری شده و تحت بازجویی‌های طولانی قرار داشته است. مواردی که به‌تنهایی مصادیق «شکنجه» محسوب می‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77998" target="_blank">📅 17:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MIIh02v6Tx0SvGGoxWAZ8yFdcGOBQLq-YodWNRuPJfnXTvfWWp0TSVs5RvSvEsKxRQZhjLTCNDOv2-uSa-qYWDWioAhBuigkwKO49Tdt4P7msSv4pQRc7IG6oMpgfNKgMDoHXUWdJ6xeVnpxMcItB2JV1R9g_g3o8lV2DQR0WoOaSnBGC_XtCNURd-fZm4UTVY04BxhvKIAIj1ahWrU7rxly--nej296vdvkX3tNeAqPTnxJkPw3BfWJSlENeahweLmAK9ZKXmd2Kl3ojJEhDhDwtuPAQ550r2XKIATiIMWdM66V8ediF5r1hzhk0sFLyXuK57UbyzHNXsL5-8GOxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NHqI1i4fhRi4DxJGAzdhQj-7bhzqNVgaLewH8YHD5bcoTS-RL1w3zAH8L0WUpjPe-f2-I7Itwi6q-4c9aiTVJIlZl7W7TuL9piuQiwrnQl46AVTeC9WPAClEablAg6ry4_zwqClhCHnzPsy3TTfat1k8LOLUKtElRFuGveNVHc7PgYqOyxSbE5t1NElM2VGmQ6UL3AWBJFQ2jpkZoNFpfowcwcIaQCD2wjWWxR379x5GAEy1sGX_ZMW3GcZHeRGh7K1vxsq_ZPkC1G4_Mla7RKFylPaYs1jErM3Ul36ViUyvALz7decW2UeyMrb3gjjVdpvyewtVmssO6_JVKNv8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Bh4Rfb-z65wwJz_WWljm-8ds6JsCwaw6yq81n8zG9UfqoWT84gJ02VetjslD9tpUH2TRojzD_lrSOHVezRbWe1xvslw4wy7l70CtMvxcTOT8LeEeOh1SOQCvOT3J6aqK8wyjXfq0PqSoNz521Jcnj0jVpAOsJlr_-haSoAl3ZVGejyEeqqR_lvBuUHAyANXBH8IG70XKdOdAUfPkssGY3kZoEwfp0_4hHjdBH0HS7PIFJVDrPi53z7b4IptfTwpLtutIMJGROGG_J0Q8Dec-6tBUPPK9kNmndI0k-xlLL-Jj4IdCilMSV9FjkvX9d3wFeHPJ9Q1Kc9zkX65fxxHVtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nxSiKomtuOVj3WgLkkoekSH7r9C7nusnMx8PKjpDwc0PlUzSsTZPBpXMBb5u1kX--VMqCsrv0mu-4QdZaYZPyU57erSOLQmCMluLSWXI56EXerBCi8a505LtUy8dB5cjQ9mpumNud6OxZ2NmLYBzGmthe-4QFx_kb581QfQ7ZnAHFtwPwRLPnU0T0Vj2TyunCOWlhb6biQigO5DmvNCvjRot32cuDmcfZdExaW9naePKYp6SdwgM0Fl_9KqarKGT3KqavcIL6kh-5F3awxOdYf_GejBSX0lMLANgWmlqt6l8-b4CLDzqlRZ27MzR4uxUZlhNaI6yKTmLg8QJVWwNWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=dUBVirUHKLNP10esJ4u37wQjV4AcKINgzHrNwze6THvMQL5tXPT0RF7zBMRt50cSI-6bdkc0cc08N7MaY9GE0R776eEhp9zpMecS3axX4oEbVxFDt1LmR96AkTDAMTOgCZgGCxMRd7FSXma_GkmhIdI4QFZFQwxWUftEAmBUm5W_Xp9BQ8Nf5dGJJ-bBY1Q0sOlONgLZFY0nD_DqVlns25kyalq1sgy0lgvF3HrfvorP66ym4yvUJ0zccW3o0WKn7K62vZbuqAucaR4N4KS-ODMkR5-lxS7Eoh54Rn32VMGQ6hfvBsvj5fAjHboEfdrnZN__MLIGwmIGVHELck15yw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b28f575c7.mp4?token=dUBVirUHKLNP10esJ4u37wQjV4AcKINgzHrNwze6THvMQL5tXPT0RF7zBMRt50cSI-6bdkc0cc08N7MaY9GE0R776eEhp9zpMecS3axX4oEbVxFDt1LmR96AkTDAMTOgCZgGCxMRd7FSXma_GkmhIdI4QFZFQwxWUftEAmBUm5W_Xp9BQ8Nf5dGJJ-bBY1Q0sOlONgLZFY0nD_DqVlns25kyalq1sgy0lgvF3HrfvorP66ym4yvUJ0zccW3o0WKn7K62vZbuqAucaR4N4KS-ODMkR5-lxS7Eoh54Rn32VMGQ6hfvBsvj5fAjHboEfdrnZN__MLIGwmIGVHELck15yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش‌های مرتبط با ایران در سخنرانی دونالد ترامپ در ایالت کارولینای جنوبی، جایی که رقابت‌ها برای کرسی سنای آمریکا در جریان است، با تشخیص و ترجمه ماشین:
🔻
و به‌محض اینکه کارمان با جمهوری اسلامی ایران تمام شود، قیمت نفت پایین‌تر از چیزی خواهد بود که حتی همین مدت کوتاه پیش بود.
🔻
اما با وجود همه این خبرهای خوب، گفتم از گفتن این خوشم نمی‌آید، اما باید کمی مسیرمان را عوض کنیم و برویم سراغ جمهوری اسلامی ایران و باید ماجرای سلاح هسته‌ای را جمع کنیم، چون آن‌ها دارند به سلاح هسته‌ای می‌رسند و ما نمی‌توانیم اجازه بدهیم سلاح هسته‌ای داشته باشند.
نمی‌توانیم اجازه بدهیم ایران سلاح هسته‌ای داشته باشد؛ خب، چیزهای بسیار بدی خواهید دید. پس رفتیم آنجا و جلویشان را گرفتیم. آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
آن‌ها به‌شدت می‌خواهند توافق کنند. ما حتی نمی‌دانیم خودمان می‌خواهیم یا نه، چون من در حال حاضر تنگه هرمز را قلمرو آمریکا می‌دانم. این قلمرو آمریکاست.
🔻
در مورد ایران هم به همان اندازه [ونزوئلا] خوب عمل می‌کنیم. رسانه‌های جعلی فقط نمی‌خواهند آن را این‌طور گزارش کنند، اما حالا دارند کم‌کم می‌پذیرند، چون چیز زیادی برای گفتن ندارند.
وقتی کشوری دیگر نیروی دریایی، نیروی هوایی، رادار، تجهیزات فنی یا تولید ندارد، رهبرانش هم دیگر نیستند. دسته دوم رهبرانش هم دیگر نیستند.
بخش‌هایی از دسته سوم رهبرانش هم دیگر نیستند. در واقع، این یکی از بزرگ‌ترین مشکلات من است. نمی‌دانم اصلاً باید با چه کسی طرف شوم. این یک مشکل است.
تنها کشور دنیاست که هیچ‌کس نمی‌خواهد رئیس‌جمهورش باشد.  می‌گویند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» «نه، نه، من نمی‌خواهم رئیس‌جمهور شوم.» پس کمی مشکل است.
🔻
او [لیندزی گراهام]  واقعاً دغدغه‌اش این بود که کشورهای خارجی به کشور ما آسیب نزنند. دغدغه‌اش این بود که ایران سلاح هسته‌ای نداشته باشد. خیلی شدید روی این موضوع حساس بود. ببینید، اگر چنین اتفاقی می‌افتاد، اگر آن‌ها به آن دست پیدا می‌کردند، از آن استفاده می‌کردند. اسرائیل را فوراً نابود می‌کردند. خاورمیانه را نابود می‌کردند. و فکر نمی‌کنید سراغ اینجا هم می‌آمدند؟ می‌گفتید: «شهر بعدی کدام است؟» ما اجازه نمی‌دهیم چنین اتفاقی بیفتد. ما قبلاً... آن بمب‌افکن‌های B-2 را داشتیم؛ یک سال پیش، آن‌ها به آن امید پایان دادند.
🔻
ببینید، جمعه‌شب است. وقت زیاد داریم، درست است؟ اصلاً چه کار دیگری دارم بکنم؟ برگردم، ایران را یک کم بیشتر بمباران کنم؟ دیگه چه؟
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 362K · <a href="https://t.me/VahidOnline/77993" target="_blank">📅 05:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77992">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=WcUVgdo5lGDJp9wlVLakOwfVspyg2kFHndwkEGljrxIhdNH2yJyz8-fGu1pStursMn_5vB9MpxkYlFpO6Qt9hQdZ5RFwu12-wFlM2Bysk88iiqFTQwDioQKSG9y2oMGQ4k3f4ArGAbx0WUAjnhhFWLxlsLzFwsf2HQUwftB6nI7iZa3wmJRBFYFLsii7bcoOpYXtQO_6Hy5N6OkfSF0fl08K8U1C86F6xnPBRpKrHKJdmnOsZX77q9GrVTUy9ye05kn2mVmE8nNboELpT5nv7WvRQdz8UIWJ_B11xZWFATp73a6_oFXLsQ9GZdbOFWmXA2BgvYv2Qvt8qY6sPqfMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edb3c61b37.mp4?token=WcUVgdo5lGDJp9wlVLakOwfVspyg2kFHndwkEGljrxIhdNH2yJyz8-fGu1pStursMn_5vB9MpxkYlFpO6Qt9hQdZ5RFwu12-wFlM2Bysk88iiqFTQwDioQKSG9y2oMGQ4k3f4ArGAbx0WUAjnhhFWLxlsLzFwsf2HQUwftB6nI7iZa3wmJRBFYFLsii7bcoOpYXtQO_6Hy5N6OkfSF0fl08K8U1C86F6xnPBRpKrHKJdmnOsZX77q9GrVTUy9ye05kn2mVmE8nNboELpT5nv7WvRQdz8UIWJ_B11xZWFATp73a6_oFXLsQ9GZdbOFWmXA2BgvYv2Qvt8qY6sPqfMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: آیا حرکت به سمت جنگ اقتصادی علیه ایران نشان می‌دهد که گزینه‌های نظامی آمریکا در منطقه محدود است؟
🔻
ترامپ: نه، اصلاً. فقط یعنی اینکه داریم می‌بینیم چه اتفاقی می‌افتد. آن‌ها هیچ پولی ندارند. نیروی دریایی ندارند. نیروی هوایی ندارند. به سربازانشان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند. تورمشان ۳۵۰ درصد است. بنابراین فقط می‌خواهیم تا حدی ببینیم چه اتفاقی می‌افتد.
و همان‌طور که می‌دانید، کنترل کامل داریم. اگر به محاصره نگاه کنید، کنترل کامل آن را در اختیار داریم. تمام آن منطقه‌ای که مربوط به تنگه هرمز است، و این یعنی تا عمق آن، مناطق خشکی را هم.
پس آن‌ها خیلی دوست دارند توافق کنند، اما از نظر من هنوز آماده نیستند که توافق درست را انجام دهند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/77992" target="_blank">📅 01:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بنا بر پیام‌های دریافتی حوالی یوسف‌آباد و امیرآباد و فاطمی و... صدای شلیک پدافند شنیده شده.
ساعت ۲۳:۰۸
🔄
پیام‌ها همچنان ادامه دارند.
کسانی هم معتقدند تیراندازیه ولی خیلی‌ها هم پیام دادند که صدای آتش‌بازی و ترقه‌بازی این وقت شب در کشور جنگ‌زده مربوط به یک مناسبت تازه‌ساز و "عید" جدیده!
دو روز پیش:
اجتماع "عید بیعت با امام زمان(عج) " برگزار می‌شود
به گزارش ایسنا، این مراسم با هدف تجدید پیمان با امام زمان(عج) و همچنین تجدید بیعت با مقام معظم رهبری، حضرت آیت‌الله سید مجتبی خامنه‌ای، از ساعت ۲۰:۳۰ تا ۲۳:۰۰ در میدان ولیعصر(عج) تهران برگزار می‌شود.
در این اجتماع علی‌اکبر رائفی‌پور و شیخ اسماعیل رمضانی به ایراد سخنرانی خواهند پرداخت. "
isna
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/77991" target="_blank">📅 23:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g3zJwCyx_o6428piDu20lrTNuqyL6k2Ap0rmOEBZ87Qd9qBkfGqywTjvCTi6E_sZy93tJOgYgUhwMxUJrGEbyY6f4V18DD8ytyeIyza7KdMiAUlwkP38yBB2WZP3Oj7woGeRCDa9zRIMKE-HCGf3q0-lWhIALFMXd7c77cKKoJidd5HD5l-iSVJxSe7RRKabTgO0Uj59Xm_VSY88uTsFPW6JlgSSon2r70J_ry0hsiXZ3jrLdLYywPqUpLz9cCyGxCcmlR-DYpfMlvTaGeF8UCRrsLPk-0XP_kImVdMOmdyjikV00h-Z5ZFNTAdH60Ch3-xHV3FnM5uFbRS-5iAfYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر عکس من در آوتار اینجا جزو تبلیغ بود کلاهبرداری خطرناک‌تریه.
این تبلیغات به خود تلگرام سفارش داده میشن و کانال‌ها امکان جلوگیری از نمایش اون‌ها رو ندارند.
هر روز صدها نفر برای اولین بار با این تبلیغات مواجه میشن و به درستی احساس مسئولیت می‌کنند که باید این چیز خطرناک رو اطلاع بدن.
هر روز خیلی‌ها هم لطف می‌کنند و راهکارهای مختلفی مثل درخواست برای ریپورت کردن تبلیغات و بوست کردن کانال و حتی سفارش تبلیغ برای خودم و... رو پیشنهاد می‌کنند.
یک مشکل بزرگ الان حجم پیام‌هاییه که درباره این موضوع دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/77989" target="_blank">📅 20:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kTUql5U19nr8LPZ52lHtDe-diAk6WCmIYI4mn0D3u_NGDgUtan-NTY7gLPXTzM8mFJAt5mRN3aDNPpNfiuSFmX0IVI26Y1YtdrAmfMIY5_A4yW0caDQDcDE22sbjKkKLBqR3jEt0rbcEM34oYO3HGJYrxMFIV8xAKezv6fz1rKW_ytGvxuMctlFALE0pua4jl7u6vxkY364-iCtCj33xwWVr8Jj5ssF0Xc6mni3z8bSahem19kp6Odft8ejR4keGmfffJZWzx189YToU7CI-gnHP9NwdBE2tYarF_2flohrcTXlcG-JyR-NnYg9EUJWV3KYiNQvx63qqLD3pIuNBGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«هرانا» روز جمعه ۳۰مرداد۱۴۰۵ خبر داد که دیوان عالی کشور، حکم اعدام «ارغوان فلاحی»، زندانی سیاسی ۲۴ساله محبوس در زندان اوین، را تایید کرده است.
حکم اعدام برای این زن جوان در شعبه ۱۵دادگاه انقلاب تهران به ریاست «ابوالقاسم صلواتی» در تیرماه ال جاری صادر شد.
ارغوان فلاحی که اوایل بهمن۱۴۰۳ به دست نیروهای امنیتی بازداشت و به بند ۲۰۹ زندان اوین منتقل شده به «بغی» متهم است.
هرانا به نقل از یک منبع مطلع نوشته است که ارغوان فلاحی مدتی در بندهای ۲۰۹ و ۲۴۱ زندان اوین نگهداری شد و برای گرفتن اعتراف اجباری از او درباره کشته شدن «محمد مقیسه» و «علی رازینی»، دو قاضی جمهوری اسلامی، تحت فشار قرار گرفت.
فلاحی پیش‌تر نیز در آبان ۱۴۰۱بازداشت و به اتهام‌های «اجتماع و تبانی» و «تبلیغ علیه نظام» به دو سال زندان محکوم شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77988" target="_blank">📅 19:05 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WqxRmstLoC5i_qK13xWnrd6bVpFlGePDg1LtvQXqEkxchW5JV3Xe6X6Gz96yoWvnITscXWC2V_Vpa8x2BRzMMWmg10PpVpLmR3OrmtJ9nFYhfAYnT6p4j_Juw_d9ipO6QzcTBDJo0JrR9SZ2Y3kR74uOXOwdGYhlBGl14Z-NfAKANmjb_HL-P9EPEVbvkfPY2v1TIBr7eFP2Qk7ZEleLLaWijuS3oIJLO_gOy05rvC3kNfAmcSyWkwQyWXI9mqrEVCS1OLiBejqBela9IXbbam7vtv_BvFgc9df3SjNuwCON17A3oSW2AvWhfwRrf6Lf0dcvSHtOSpzHyWOms0zh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی، ترجمه ماشین:
۱۴ سال پیش: «فلج‌کننده‌ترین تحریم‌های تاریخ.» شکست خورد.
۸ سال پیش: «فشار حداکثری.» شکست خورد.
۵ ماه پیش: «تسلیم بی‌قیدوشرط.» شکست خورد.
امروز: «کوبنده‌ترین عملیات اقتصادی تاریخ.» محکوم به شکست است.
این فیلم را قبلاً دیده‌ایم. همان مزخرفات. قلدرها عوض شده‌اند.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/77987" target="_blank">📅 18:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=FjBJr-RdOlvAyrCZwUfNivikoioezeGGnewdnHzb3EqHmM-ZO7HofgkYDfgwtABytIxbhG8DbKAXI4rLirt3ApYbMgUh6FO9Zn2tApC4cGi2OxgNTHJAs6roO-_nvZD3BaFhuCfIjyZCQcWX8rS4zTTLGf7oHqU3mo5nQ2A9Z3MyYKEUJBwBmPckFTW56SYirtGUUkpYXzBXDqR4yR862ULMIaJGK7BvjtGJ6fdNnHVtwwNZCcpp9WsPpklvkRf0LdbzvggVTKpX_ISNOiiybmsMu6v2RN7wfyOkqizw2fUG9zqnbfWp5QoJPY8P-5zlQe5II6R2-fW4sWApnTZD4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd72c517e9.mp4?token=FjBJr-RdOlvAyrCZwUfNivikoioezeGGnewdnHzb3EqHmM-ZO7HofgkYDfgwtABytIxbhG8DbKAXI4rLirt3ApYbMgUh6FO9Zn2tApC4cGi2OxgNTHJAs6roO-_nvZD3BaFhuCfIjyZCQcWX8rS4zTTLGf7oHqU3mo5nQ2A9Z3MyYKEUJBwBmPckFTW56SYirtGUUkpYXzBXDqR4yR862ULMIaJGK7BvjtGJ6fdNnHVtwwNZCcpp9WsPpklvkRf0LdbzvggVTKpX_ISNOiiybmsMu6v2RN7wfyOkqizw2fUG9zqnbfWp5QoJPY8P-5zlQe5II6R2-fW4sWApnTZD4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمیدرضا حاجی‌بابایی، نایب‌رئیس دوم مجلس، روز پنجشنبه ۲۹ مردادماه در گفت‌وگو با خبرگزاری فارس با اشاره به تحولات مرتبط با تنگه هرمز و تلاش برخی کشورها برای ایجاد مسیرهای جایگزین انتقال نفت، گفت: «کسی که امروز خط لوله می‌کشد تا تنگه هرمز را تضعیف کند، در واقع به ما موشک می‌زند. نباید اجازه دهیم خطوط لوله جدید ایجاد شود.»
او با تاکید بر اینکه احداث این مسیرها در راستای منافع ایالات متحده است، افزود: «هر کشوری که در زمینه فناوری یا اطلاعات به آمریکا کمک کند، عملا وارد جنگ با ما شده است. احداث خطوط لوله‌ای نظیر فجیره و ینبع برای کاستن از اهمیت راهبردی تنگه هرمز، مصداق بارز جنگ و حمله موشکی علیه کشور است و پاسخ ما باید ممانعت از ایجاد چنین خطوطی باشد.»
این اظهارات در حالی مطرح می‌شود که شبه‌نظامیان حوثی یمن، وابسته به جمهوری اسلامی، در هفته‌های اخیر با حمله به کشتی‌های حاضر تنگه باب‌المندب تلاش کرده‌اند صادرات انرژی از این آبراه را مختل کنند.
از سوی دیگر، مرکز مشترک اطلاعات دریایی (JMIC)نیز، روز پنجشنبه، از عریض‌تر شدن گذرگاه جنوبی تنگه هرمز خبر داده و اعلام کرده بود این تغییر امکان تردد هم‌زمان کشتی‌های ورودی و خروجی را فراهم می‌کند.
مدیرعامل آرامکو نیز روز ۱۳ مرداد ماه، اعلام کرده بود این غول نفتی با تکیه بر خط لوله شرق به غرب عربستان سعودی، کانال سوئر و تنگه باب‌المندب، به صادرات نفت خود ادامه می‌دهد.
@
VahidOOnLine
مصطفی خوش‌چشم، کارشناس صداوسیما در مصاحبه‌ای پیشنهاد داد، «نیروهای محور مقاومت» با استفاده از «مین‌های دریایی هوشمند» خلیج فلوریدا را مین‌گذاری کنند.
خوش چشم، در تیرماه گذشته در تلویزیون به شدت از عباس عراقچی، وزیر امور خارجه، انتقاد کرده و تحلیل‌های او را به «رانندگان تاکسی» تشبیه کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/77985" target="_blank">📅 18:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DYqWOdiYGpcW7cUcxHQCly7RqIX5G9c3tnKifP2dkFlzaD2gpi19piCWySGDBeYLl0f0YhG5J-FjIpCR9s2kx4ISDxusfQwzp6PPlAR4XInQvfixAHrSvRc200i6GSYfdRqxf32sdINbC-67QnZQ6EqzG8FZoFSWyt6HJbIxgjDoEAWfDWMr-i2uEnBlGDj5fv5Jo0N1lcgX3IXqQyQoz8cd3wUdxqUvSFYxMWx8ipDuTjfNekloBRh00RavGe62cVE79g3cv0ov0i3AO_0YezC5QzYN4AxaDHdMQNIspvtt5-vlOdp82fTkx7Gbx_T7Rji3yGpHDArb1ixCSEElPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GqII9XBNwLHb-RyDxDYobG0OlWPus0lCNY2nbhIv6utNivtNXyyGyMycmlk0Pb1j0D_8W8fXSbcp1WNnowtV13UTcpib8uzIEathwDPLwcdW8FcIxx2wwegIBSw9jKgEvdKNUjdTIoq1jnbPWzwWenr6LbUYeQ1BrpqR5bCMrECgUUg7hRzeum9IF6cU5tBi7IUdk2HXaBglSaOq_vGJqkWhMf82_ll5y_KfxxBvgTpDpVGhngEhPAGD84c2OoN6Ix9nyl-3uM3myrTv1efMZS46T7dfi7mwkaOQss0YsUyk9qlgLjSFCOsGft29eGeTr2W0hpzWp5mjC3ILmDMlug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس پازوکی، معاون ارتباطات و اطلاع‌رسانی دفتر محمدرضا عارف، معاون اول مسعود پزشکیان، اظهارات منتشرشده عارف درباره تعیین نرخ ۸۷ هزار تومانی در دولت را تکذیب کرد. این در حالی است که رسانه‌های ایران پیش‌تر اظهاراتی از عارف درباره تعیین این نرخ منتشر کرده بودند.
به گزارش رسانه‌های ایران، عارف دوشنبه ۲۶ مرداد در جمع خبرنگاران گفته بود پس از تعیین نرخ چهارم بنزین با بررسی کارشناسی و تعامل با نهادهای امنیتی و سایر قوا، قرار بود این طرح به‌صورت آزمایشی در کرمان اجرا شود، اما بدون هماهنگی با دولت متوقف شد. نرخ چهارم مورد اشاره ۸۷ هزار و ۲۰۰ تومان است.
با این حال، پازوکی در ایکس مطالب منتشرشده درباره اظهارات عارف را «ادعای ساختگی برخی کانال‌های غیررسمی» خواند و گفت: «معاون اول رییس‌جمهور هیچ‌گونه موضع‌گیری یا گمانه‌زنی عددی درباره نرخ‌های جدید بنزین نداشته‌اند.»
او افزود: «موضوع مدیریت مصرف سوخت در مرحله کارشناسی قرار دارد و هنوز هیچ رقم یا تصمیمی به جمع‌بندی نهایی نرسیده است.»
@
VahidOOnLine
فاطمه مهاجرانی، سخنگوی دولت، روز جمعه ۳۰ مرداد ماه اعلام کرد مطالب منتشرشده به نقل از محمدرضا عارف، معاون پزشکیان درباره تعیین قیمت ۸۰ هزار تومانی برای بنزین صحت ندارد.
مهاجرانی گفت چنین عددی نه از سوی معاون اول رئیس‌جمهوری مطرح شده و نه مبنای تصمیم‌گیری دولت قرار گرفته است.
او تاکید کرد در صورت نهایی شدن نحوه «مدیریت مصرف سوخت»، جزئیات از مسیرهای رسمی و مستقیم به اطلاع مردم خواهد رسید.
@
VahidOOnLine
مسعود پزشکیان، در مجمع عمومی «انجمن اسلامی جامعه پزشکی ایران»، گفت: «جدا از بحث محدودیت‌های مالی و محاصره دریایی دشمن که کار صادرات و واردات ما را با مشکل مواجه کرده است، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومانی بخرد و بعد آن را ۱۵۰۰ تومان بفروشد؟»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/77983" target="_blank">📅 18:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tK4v2uxaOf6KVTdMVEuEa5Jp-kdzi3-8k2nsY0eGTcQ-wUiRJ5f95TzAigr7CEuI08IT-XHcXpvGNKcil7j_yV2IGyPdqZcuGT0-HxGpL1w32V0QyfxDg-UMaW4iNgfJG2bQ-eHZPRvH0UK1qQDxX1V5UJdnnF6dqnW3y-nUcvpsiWborKwn-V8BIGkQiCbSZWhHo6TLmkFmekioyqXI3-T1lnCF38iHe_-VCn8TH4HkltgUlBhuLO3OMln94fYLJ-3u55rOeuL7OWXI1g57c25I1ikm9kFW-Zy0YovGm_pVONQiHQfVPcbGdDnZXq1SROq8Y9essKQ205DzE-NLvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس دولت در ایران، می‌گوید اکنون زمان آن است که به جنگ با آمریکا پایان داده شود چرا که تهران در مقابل واشنگتن در موضع «قدرت» قرار دارد.
آقای پزشکیان گفت: «بهتر است امروز که در قدرت و عزت هستیم و تمام دنیا به پیروزی ما اذعان دارند و تأکید می‌کنند که آمریکا برخلاف تمام مقررات، به مدارس، بیمارستان‌ها و زیرساخت‌های ما حمله کرده و در دنیا منفور است، جنگ را پایان دهیم.»
رئیس دولت در ایران همچنین نتیجه مذاکرات ایران و آمریکا را که به امضای تفاهم‌نامه اسلام‌آباد منجر شد، «دستاوردی بزرگ» توصیف کرد که «با وحدت و همدلی در شورای عالی امنیت ملی به تصویب رسید و همه کسانی که در این شورا هستند و دستی در آتش داشتند، با قاطعیت از آن دفاع کردند.»
آقای پزشکیان در ادامه از کسانی انتقاد کرد که «خارج از گود نشسته‌اند» و «نمی‌دانند دولت در چه شرایطی است، مجلس در چه شرایطی است و فرماندهان در چه شرایطی هستند، بی‌محابا اظهارنظر و تحلیل می‌کنند، هیچ رنج و سختی هم به آنها نرسیده و بعد هم دم از گرانی می‌زنند.»
مسعود پزشکیان در عین حال تاکید کرد که اظهاراتش به معنای تسلیم شدن در برابر تعرض احتمالی نیست: «ما به هیچ عنوان در برابر قلدری سر خم نخواهیم کرد و هیچ تردیدی در آن وجود ندارد. تا آخرین نفس مقابل آنها خواهیم ایستاد و پاسخ کوبنده به آنها خواهیم داد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 231K · <a href="https://t.me/VahidOnline/77982" target="_blank">📅 18:01 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=egPFlLH63GlI56z-p4O14KOR63qWdqmWgfZW8R-5akdUg_QBlI_2Yvnlsq0vd-WnBO-pXTJJkjAcukduNnm6OduF_INHqGKYxRhOxF0B8C4j8gyTBJmP9m_RUsVgQlFhl736GaMffEcufYqa-oqaifC-6PCWy0KBcJ3RnMmfTZUQZx5h7dHUNIMqXZEGUFge3Wr8xofiAb6wZsM0mszULsBJ3wIk1_GATSYqw4DD_Opqh-6XUbIlYVDVT1W2ITKA7Oo2qpE1_6dFUM9EyXt6Vh68s8r-zIaK9RaUhLtYKGxA0UMWc06ZBSlNQcPfdVHhAuvdv1Wpz-_TAkjtrJUP6w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9359b0410.mp4?token=egPFlLH63GlI56z-p4O14KOR63qWdqmWgfZW8R-5akdUg_QBlI_2Yvnlsq0vd-WnBO-pXTJJkjAcukduNnm6OduF_INHqGKYxRhOxF0B8C4j8gyTBJmP9m_RUsVgQlFhl736GaMffEcufYqa-oqaifC-6PCWy0KBcJ3RnMmfTZUQZx5h7dHUNIMqXZEGUFge3Wr8xofiAb6wZsM0mszULsBJ3wIk1_GATSYqw4DD_Opqh-6XUbIlYVDVT1W2ITKA7Oo2qpE1_6dFUM9EyXt6Vh68s8r-zIaK9RaUhLtYKGxA0UMWc06ZBSlNQcPfdVHhAuvdv1Wpz-_TAkjtrJUP6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک هاکبی، سفیر آمریکا در اسرائیل، گفت جمهوری اسلامی بیش از ۴۷ سال است که شعار مرگ علیه آمریکا و اسرائیل سر می‌دهد و تاکید کرد که این تهدیدها را نباید صرفا حرف یا شعارهای توخالی تلقی کرد.
هاکبی روز پنجشنبه ۲۹ مردادماه در گفتگو با شبکه ملی اسرائیل (آروتز شیوا) گفت: «۴۷ سال و نیم است که می‌گویند ما را خواهند کشت، اسرائیل را خواهند کشت.» او افزود: «این‌ها صرفا تهدیدهای توخالی و شمشیر تکان دادن در هوا نیست. این‌ها کسانی هستند که واقعا می‌خواهند ما را بکشند.»
سفیر آمریکا در اسرائیل گفت آمریکایی‌ها باید این تهدیدها را جدی بگیرند و برای اثبات سخنانش به حمایت مالی و تسلیحاتی جمهوری اسلامی از حزب‌الله، حماس و حوثی‌ها اشاره کرد.
هاکبی افزود جمهوری اسلامی علاوه بر صرف منابع برای تسلیحات خود، حزب‌الله، حماس و حوثی‌ها را نیز تامین مالی و تجهیز کرده است. او در ادامه گفت: «اگر در جهان اقدامات تروریستی در جریان باشد، معمولا می‌توان رد آن را تا تهران دنبال کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/77981" target="_blank">📅 17:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UHNc_sXyQrNEHxX3XDrORzTwqsVSBbUfbB1_SshblPDU4boXSymJ1rJ2pkpPxUXOkC7n6PZv1I14u5yxzYGiJdUI23TZTvrcQUun9m-OUas817SNV_gN45b4mgOgMsUfQEYBCDjvIaINPFyl_Acydf1mrvhwVdb1h69Ge45QOQffp0a76DDf8Q-19pOJWSS-rRuYQ7Fm3J1ulTbjeqZj-wfQKSmccHt6x-erLPDOLeTtBDOqKqckVybdL0IKQhhrz-FM6fTv0HgiKahaY1dwIYi_otp1LycqEddFDAJhL9OfXrd7XlU4K39FYc0YRfQaK7mDypBJv5A2UrSEy2rt-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس شورای اسلامی با هشدار تلویحی نسبت به شرایط اقتصادی جامعه ایران گفت: «ما هر چقدر قدرت نظامی داشته باشیم ولی اگر مردم گرسنه باشند و گردش مالی، رشد اقتصادی و تولید ملی نداشته باشیم، دوام نمی‌آوریم».
محمدباقر قالیباف روز جمعه ۳۰ مرداد در اظهاراتی در عراق برای افرادی که «فعالان اقتصادی ایران و عراق» معرفی شده‌اند، با «ظالمانه» خواندن تصمیمات جدید دولت آمریکا برای اعمال تحریم‌های اقتصادی شدید علیه ایران گفت: «باید برای غلبه بر آن‌ها برنامه‌ریزی کنیم تا بتوانیم بر آن‌ها فائق آییم».
قالیباف که رئیس گروه مذاکره‌کننده ایران با آمریکا پس از جنگ اخیر بود، در اظهارات خود خواستار استفاده از پول ملی ایران وعراق در مبادلات تجاری بین دو کشور شد و گفت: «می‌شود به دهان ارز آمریکایی زد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/77980" target="_blank">📅 17:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JDMDu_UyfMO-4ot7_WHW8Rj5IIiTsJGxC6G2b2c5AZwg4Mf1xChUlT_BZQq8fYSse1s5L_BXpxZjOD9ywGLC1pktNoyjsvMJ1Lk2nqsF5l4u1zGFGTaH-Zh4s8W45zWRPzBfKPn8B2wgJHl1mIgSxuYqUTzctMVcG8X1jRTFWlK-BSiOyrJtlM2av7BcjtM-B_VqOGXtF-P0Zkx6A6xW1iiIRYBwEZ92qmvqYBFODPUIzh2vJm2B2qThMITn1TUeq11dSGeXZiwdTlMhSV9FPEWk2g0et4me2aG8Z4iIBKhvzzrF4k7MsSudnZJmtFH8YuIzQ50JAjow3ohDoO5fqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه لبنان می‌گوید روابط عادی با نمایندگی ایران در لبنان تنها زمانی می‌تواند از سر گرفته شود که تهران مطابق با رویه‌های دیپلماتیک تعیین‌شده، از تصمیم دولت این کشور پیروی کند.
یوسف رجی در گفت‌وگو با روزنامه «النهار» با پافشاری بر تصمیم قبلی‌اش در «عنصر نامطلوب» خواندن سفیر جمهوری اسلامی در لبنان و اخراج او گفت: «ادامه حضور سفیر ایران نقض یک تصمیم حاکمیتی است. این تصمیم باید رعایت شود و هیچ تفسیر، استثنا یا مصالحه‌ای را نمی‌پذیرد».
دولت لبنان چهارم فروردین امسال با رد استوارنامه محمدرضا رئوف شیبانی، سفیر ایران در لبنان، او را «عنصر نامطلوب» خواند و چند روز فرصت داد تا خاک این کشور را ترک کند.
با این حال، وزارت خارجه ایران این تصمیم را نپذیرفت و سخنگوی این وزارتخانه اعلام کرد که سفیر همچنان در بیروت به فعالیت خود ادامه می‌دهد.
اسماعیل بقایی آن زمان گفت: «سفیر ایران با توجه به مباحثی که توسط جهات ذی‌ربط لبنانی مطرح شد و جمع‌بندی که صورت گرفت، به کار خود به عنوان سفیر در بیروت ادامه خواهد داد و کماکان در آن‌جا حضور دارد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/77979" target="_blank">📅 17:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/282709f91d.mp4?token=mCwKz2y00aZcCOY-aYDGxx0Y6Dl4MrwtYujbTcGpMr4t-JxQcTLm58zkj61pJW40CUwdgWtQ9z_dTyHAEmzwCY9nO1lTUkDvYaDdVJjwm0r_0h4csdgqfplRfTAmmL4enZDvmldhYy7O8XzQYru42wBAl0WnE44Os2zZjuMyWt-IbCnekqv-XyLRo5SZAml5ar8obql-qAxhuyXqD2o2okPEJLhAPLDcERC964ydsTaLlrYuCMeI7J1WYvEa4GQb-MJFaYzOQeUOrTvsgoZJ1zcgcHXzJDMPT8i50_ppsfMyY7j8R-5_N6M28d4ymK63v5CTiiWJ-zhrjHvQU4MO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/282709f91d.mp4?token=mCwKz2y00aZcCOY-aYDGxx0Y6Dl4MrwtYujbTcGpMr4t-JxQcTLm58zkj61pJW40CUwdgWtQ9z_dTyHAEmzwCY9nO1lTUkDvYaDdVJjwm0r_0h4csdgqfplRfTAmmL4enZDvmldhYy7O8XzQYru42wBAl0WnE44Os2zZjuMyWt-IbCnekqv-XyLRo5SZAml5ar8obql-qAxhuyXqD2o2okPEJLhAPLDcERC964ydsTaLlrYuCMeI7J1WYvEa4GQb-MJFaYzOQeUOrTvsgoZJ1zcgcHXzJDMPT8i50_ppsfMyY7j8R-5_N6M28d4ymK63v5CTiiWJ-zhrjHvQU4MO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"حمید مهدوی، متولد ۱۳۶۶، آتش‌نشان ساکن شهر مشهد شامگاه ۱۸ دی ۱۴۰۴ و در جریان اعتراضات کشته شد.
ویدئوی کوتاهی از او در حال حمل یک معترض مجروح بازتاب گسترده‌ای در رسانه‌های اجتماعی ایران و جهان داشت.
پیکر او در آرامستان روستای تویه دروار در شهرستان دامغان، زادگاه مادری‌اش به خاک سپرده شد."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/77978" target="_blank">📅 17:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nYST0-B0WlatOv9-ICWen9paVyCHY6y7W0zacC7t5Msd0zx0UkBjnJAou911UnJ-2UviO2SgIrun1e6lcRo6ZuIhevz0dg7iaLcT9ZZrwqveHs1NWzi9Y-hROUQx49V8Vt-yv5186ldu4dh7XY4Tb1k8E8tQk4-YsuYcqnfcClio_APVb1rWcFJEdfGv-M-sgShjOgqxJppougs0CXNquLKK2b2imtBHm4GAEGLRgZc52ZEQ_tURvCjt855jYbTwC4jzXloQe3bmP3Bk5vKXjgKACTxJtadMIKOEKDm0tqNachhrPIaet7jNf_icbidNRMTfb5l_vgyTvOK24XKdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حقوق بشر کارون از افزایش شمار زندانیان سیاسی و عقیدتی در زندان شیبان اهواز خبر داده و گفته است بیش از ۶۰۰ نفر در بندهای مختلف این زندان نگهداری می‌شوند. بسیاری از این زندانیان، هستند که در موج بازداشت‌های پس از جنگ ۴۰ روزه ایران و آمریکا و اسرائیل بازداشت شده‌اند.
تعداد قابل‌توجهی از بازداشت‌شدگان جدید را جوانان تشکیل می‌دهند و سن بیشتر آنها بین ۱۸ تا ۲۵ سال است و اکثرا از اهالی اهواز، فلاحیه (شادگان)، ایذه، بهبهان و مسجدسلیمان هستند. در این زندان بیش از ۳۱۰ نفر در قرنطینه محبوس هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/77977" target="_blank">📅 17:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H2nUCLPziE1AcOshTuT5r0XB3f9tkuxHIuUYPpriteyeIbwl1OxxwjBqZyN2cceosT-S9DLpVsLQ1HKhYVmatEZTOHTnXXcb4AMhi7_8ninJvbsGitzBHx7m7AD8NlayF2My2q0xx7q3zKdMAmOulTgmmjkBJFQxtNJR2FSmQCI0ZwKCkoqxBvA9pkI0hoD5v82ufP99vPhhETPMHvWIlHcmhqkLZmsyeQwGR9iBWZTfCvF2yfId50FQYPMbXjXwvMdfkZ6wK5OmD4V2nJKJ2xmxGl8gq3sssFOa3FDgYrmfmadsC-zXLomRme2pizWP0hTpn_NLSzHX81YL4DB15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از «دونالد ترامپ» رییس‌جمهور ایالات متحده و «اسکات بسنت» وزیر خرانه‌داری آمریکا، «جی‌دی ونس» معاون اول ریس‌جمهور آمریکا از آغاز «مرحله جدیدی» از جنگ ایالات متحده و ایران خبر داد و گفت: «موثرترین ابزاری که برای اعمال بر حکومت ایران داریم، فشار اقتصادی است.»
جی‌دی ونس که در پادکست  «کلی تراویس اند باک سکستون» صحبت می‌کرد به «تعامل ظریف» بین دو کشور اشاره کرد و گفت: «ما به آنها فشار اقتصادی وارد می‌کنیم، آنها نیز سعی می‌کنند به ما فشار اقتصادی وارد کنند. اما آنچه در چند هفته گذشته واقعیت داشته این است که آنها فشار بسیار بیشتری نسبت به ما متحمل شده‌اند.»
به گفته معاون دونالد ترامپ آمریکا این روند را ادامه خواهد داد چرا که بر این باور است «این بهترین راه برای دستیابی نهایی به هدف نهایی» این کشور است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/77976" target="_blank">📅 01:47 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KUca5MXhPAd4Sq0pWj0qjrrBkGv_jSw8pS6wVmV0-Ff4JKdhWQKr1m2qdVWtwhsr4xLH0zvmPH8I1jsIWAT3zuG3V5qNadg6ibmaibTJ3AiLg-dL0g5S2j9rrmA3h51KJzHGj2OXYim4poc7sSJ5iLp5MDLW1_hJpGFinuBeatpkvam7mPxdhGb84SECgFWUVsoTYIGD8SYLol-hKTNYQUHLF38gGMoTC_OahkHnecx3pMfTQgcaFYROInLqlWGMAUwZNTVR0uW4O1SzysNPKQxj5QQ_fN5O6znU26BJyTVewmGCMovMMLMudJDz4cMSHQjWhwDZxXac7m0N5O1aPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NZvTASdkaD95Ft66HWk7Jm7ERYaTg7XwGpu8RrHdFs0m_aOEHjic1x8YlOaZ1UHmI6-GLWXqV2w2PzwHXVUwmmjOfM-8hOLRkpbS_XVPB0dr11O61Pg5Xx6s-Vbhb14sYlw17pVT4X9vPYWyxITBV_izyhmSKYCQzVgpoFUAMpQuWe8FWiZckKbJ8za7alqzMPNb8YjuCDAiR0Bn1Ks1Qt85zXA_We_5UW-3qMLWZXiVq9suaWcG1bB5OBwEl36HLQ5-3AfXtonCbbIdOmp7JjWCiSrRxHmWNZ_qTMw17Yl9_kgtmViLH-MkOVtRevLlEM2V9KuczVU1L7yLXAhk1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار تصویری از محمدباقر قالیباف، رئیس مجلس ایران، در جریان سفرش به عراق که در پس‌زمینه آن عبارت «خلیج فارس» دیده می‌شد، واکنش همتای عراقی او را در پی داشته است. هیبت حلبوسی چند ساعت بعد تصویری مشابه از خود منتشر کرد که در پس‌زمینه آن عبارت دیگری دیده می‌شد.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/77974" target="_blank">📅 01:46 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkVKjXAI-Z0XrUK2FTpXwbXMQc-yBHBJxFJSev0VtuLlaN_785NlXir5BepsjRhE4phr8_zLq94-hkG58q7f5JeQa2KBGx8dQvRQ6s2cvFe0YCR2qxntG2Jv8rcWRZfIADdG2QGZORYw3bCK51uogMjVJD_jY7LmQO-SD0tIDXE6pf-5HVtKPS7kcIQXrmbCEHjSSlR6P_CtTKZQVMzphgtvkWkpnr__uDyjwbU0t2atopDrk_ADg49UISis1K2jL2K0f7889UrJEV7geTqrbdks6j0Acg40unOSVlRU8Dgpz0XgZvZG5bkh0RUFZMgTpQOxI_jIwV23mS65tRqSHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه ۲۹ مرداد گفت طرح واشینگتن برای افزایش شدید تحریم‌های اقتصادی علیه ایران با هدف «سرنگونی» حکومت جمهوری اسلامی دنبال می‌شود.
بسنت در گفت‌وگو با شبکه سی‌ان‌بی‌سی گفت: «این طرح در ایران جواب خواهد داد و ما این رژیم را سرنگون خواهیم کرد.»
او افزود: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود.»
وزیر خزانه‌داری آمریکا روز ۲۳ مرداد نیز خبر داده بود دولت دونالد ترامپ قصد دارد اقداماتی در مقابل ایران انجام دهد که به گفته او «در تاریخ انزوای اقتصادی یک کشور بی‌سابقه بوده است».
او گفت: «اگر ما حداکثر فشار اقتصادی را اعمال کنیم، به احتمال زیاد دیگر شاهد ازسرگیری یک عملیات نظامی گسترده نخواهیم بود؛ اما تأکید می‌کنم که این وضعیت مربوط به حالا است.»
اسکات بسنت همچنین خبر داد که روز دوشنبه هفته آینده یک نشست خبری برگزار خواهد کرد تا «دقیقاً درباره اقداماتی که قرار است انجام دهیم» در قبال ایران توضیح دهد.
هشدار به متحدان آمریکا
وزیر خزانه‌داری آمریکا همچنین در پی اعلام طرح جدید دونالد ترامپ، رئیس‌جمهور آمریکا، برای تشدید فشار اقتصادی بر ایران، به متحدان واشینگتن هشدار داد که در موضوع انزوای اقتصادی ایران باید میان «همراهی با آمریکا یا قرار گرفتن در برابر آن» یکی را انتخاب کنند.
او دربارهٔ پیام خود به متحدان آمریکا گفت: «این بزرگ‌ترین انزوای اقتصادی هماهنگ‌شده در تاریخ جهان خواهد بود. ما به آنها می‌گوییم که یا با ما هستید یا علیه ما.»
وزیر خزانه‌داری آمریکا در پاسخ به پرسشی دربارهٔ احتمال اعمال فشار واشینگتن بر چین نیز گفت: «بسیاری از گفت‌وگوها بهتر است در خفا انجام شوند»، اما همزمان از پکن خواست «با این برنامه همراه شود.»
او گفت: «ما اطمینان داریم که همه خواهان بازگشایی تنگه هرمز و کاهش دوباره قیمت انرژی هستند.»
بسنت در ادامه با اشاره به وابستگی چین به نفت خلیج فارس افزود: «در نظر داشته باشید که ۵۰ درصد انرژی چین از داخل خلیج فارس تأمین می‌شود. بنابراین، همراه شدن با این برنامه می‌تواند خدمت بزرگی به خود آنها باشد.»
این اعلام موضع وزیر خزانه‌داری آمریکا یک روز پس از آن است که رئیس‌جمهور ایالات متحده اعلام کرد که کارزار جدید و بزرگی را برای هدف قرار دادن اقتصاد ایران به راه انداخته است.
دونالد ترامپ شامگاه چهارشنبه در شبکه اجتماعی خود، تروث سوشال، نوشت: «امروز، من کوبنده‌ترین عملیات اقتصادی‌ را که تاکنون علیه کشوری انجام شده است، اعلام می‌کنم! این یک جنگ و انزوای اقتصادی در مقیاسی بی‌سابقه خواهد بود».
او افزود: «همچنین اعلام می‌کنم که هر کشوری که به نهادهای مالی، کسب‌وکارها، فرودگاه‌ها یا ارگان‌های دولتی خود اجازه دهد هرگونه راه نجاتی برای ایران فراهم کنند، خود با عواقب اقتصادی بسیار سنگینی روبه‌رو خواهد شد».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/77973" target="_blank">📅 20:18 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbpOh9petDchrWKHqL8c5bqef0RHdcyKhwd0DftLLazCtl5BR5r49Lfcqr17fAAdQYrBvYy-n_r8yHUd-UdeR67FT1zXx6NZIYjJDX593VWg0W-wVcfLyGUxNsGIIutN4Ixv68w8FBi6WwXNs31SE7e-dgvjKp7zNp2E49rrKU88CAYisaKieG4-4lFKZk4DtY_MnTMDVfMS1QGiLK7d42Ds6h3r0_352iNL62M_NrJZ8wMGkxXbdboJ016Ol64gywPj5Cjs27V7_MYo04hRoljNLkLivjwNvXGw8y9A37_kZT14RGlIaYCumJdOvDksfEBVQqD9eOX1cOyqEvKwCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OPtV6IGRgxKSQ22ODi8Q3vEcZO6JhIBRmHcEM-av8eNWoZ4SWL0gSBp2hs8DvVhOl2j5uMJ3YHDjpz4oC1pOtlmhn_Mgb576UuAmq_hVj6jWoamiRQNY7cxlje8t43ERe4bd4F3lDNQGTQpT6Mev83TgHlU2T-DvfwfjAMuTUfwwSQhJR7UaRjaOA1it2EeGK3RkbkKFLIfcA8ZDJztOmsTn5FHi3NYlkllECpbEWLxVi_xVPvVzfswAeLvUBMcUZSsJ_7TWs1S5Q26Ygc4fqD1PUcBGnhY5dDkTCeKW3T6WkrMBw2ahSH3mxWQ4z8VZY7WRuBMEB3s_8qsEVzrEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oYQ1C6epErDxqVksb900eRY5JZBQyjQYYfkfy90T7D_gQnFwM5OcuZKOYp-g1uonuyOy9zUuOBeS9_nZLgZl8ZXON4ZdbYXwJhXeJM-MTToQn0-7hxQP3ai1h7uYWfD3Ob1z3aC0NOC7YaGCHo-ufZeFbzAzoQPNDbiaQvmJf6w_utEAYA1kHvAHbUcFllptbjiQWuSERAwzhlY31j0AthJ-DdDfE4QFRihGMATljmUNVOUt5N_nmBSamYa--yFKmy6nGTo7dDyWyMArfo15RO3S6m7RhTv6i0oloxwbXVNcgysWQ7p4dZlIxKiW7Hw8vPuhG85_uY2BvIRjHMB9Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=is8ba0Y2iEadfF5krglo_mKse19yUE1z08mKdmDnx70D6nLcnCd57BZ-rUaAgaZo_7LNFsthwKovWZKAG2nT26mBdGLDDppow11LqIjQfnEXnqxpSlDYPLLHe0nj4aZfiv8q_D1ca8cJE_Lqb7I0bswfJQlR6vrPemky0uFTvcHbuWEEbE6_IG3v6HW83Sd2zF149nVIWAHNv2trPJQcLijK9njMjWWITIXzSUYqlU3gmAcpVrktQfRjd8yL35R_xs3VtEEMneI3hMCsP7NYWZfqGYoSc0AnFtvUhRN9VH82WeSP1-lHc8dRcM44KhQ-x5pgGF2CE54zDRskBcZQZiy33vmd5xwnes1PMvNSZSSziLzDy2W4unyFlWvAcJSms0O9KbC475ZFKBRKpa63eFGMi11xYa3Q6CQZk7ItV3e-vonL7xGfuXM4f3y62TlQKvX6yI21163NFuFGKPGVSCzm_EBNszZMtngTxX85SnCupyZAFoiXbx5YySJk9WW0wNZtoMKaDcToeiz-r5TfaXUMeklOBCM-u3WExgWz8vuriMiDju7o9bIFven8U7xCfXau3WFO6J8Eq6E0nElyYnZFFJ4Zy-_ArrZQFkZ-YLxklwpj72uASMfl3wvUwg1v7FiWT49oty6qQW0tJMIYJr1uDwEGsk_ewHzMZVUjyaU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e50a342f2.mp4?token=is8ba0Y2iEadfF5krglo_mKse19yUE1z08mKdmDnx70D6nLcnCd57BZ-rUaAgaZo_7LNFsthwKovWZKAG2nT26mBdGLDDppow11LqIjQfnEXnqxpSlDYPLLHe0nj4aZfiv8q_D1ca8cJE_Lqb7I0bswfJQlR6vrPemky0uFTvcHbuWEEbE6_IG3v6HW83Sd2zF149nVIWAHNv2trPJQcLijK9njMjWWITIXzSUYqlU3gmAcpVrktQfRjd8yL35R_xs3VtEEMneI3hMCsP7NYWZfqGYoSc0AnFtvUhRN9VH82WeSP1-lHc8dRcM44KhQ-x5pgGF2CE54zDRskBcZQZiy33vmd5xwnes1PMvNSZSSziLzDy2W4unyFlWvAcJSms0O9KbC475ZFKBRKpa63eFGMi11xYa3Q6CQZk7ItV3e-vonL7xGfuXM4f3y62TlQKvX6yI21163NFuFGKPGVSCzm_EBNszZMtngTxX85SnCupyZAFoiXbx5YySJk9WW0wNZtoMKaDcToeiz-r5TfaXUMeklOBCM-u3WExgWz8vuriMiDju7o9bIFven8U7xCfXau3WFO6J8Eq6E0nElyYnZFFJ4Zy-_ArrZQFkZ-YLxklwpj72uASMfl3wvUwg1v7FiWT49oty6qQW0tJMIYJr1uDwEGsk_ewHzMZVUjyaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مادر پرنیان دبیری با انتشار ویدیویی گفت دختر ۱۶ ساله‌اش پس از اصابت گلوله به کهریزک منتقل شد و پیکرش در محوطه این مرکز روی سطح آسفالت قرار داشت.
او همچنین گفت هنگام پیگیری تحویل پیکر دخترش، یکی از ماموران با قنداق تفنگ به او ضربه زد و تهدید شد که در صورت ادامه اعتراض، پیکر پرنیان تحویل داده نخواهد شد.
او خواستار پاسخگویی عاملان کشته‌شدن دخترش شد.
این جاویدنام ۱۹ دی ۱۴۰۴ همراه پدر و مادرش در خیابان بود و از پشت سر با گلوله جنگی سرکوبگران هدف گرفته شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/77968" target="_blank">📅 16:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I-i6J53Iz8TS30mu-HMB2--3FD_8U5x7ohi19oJkqxmeZql9owdpKFnjqG-yy46PnwvugqJR3M6lHTOZoSogqtH1l5WL20-44PsQKy86mz1IkWIbnjAQFU84UTyYaA3GHmqB1mI7-ofJ6POiPl0nmNGGsh-HNtktRN_3ikDrOKe3zvDuvrX59gNPYhcouqUk7Tr86A5sgiB-BHh7FiqsFsTH3bE36DFJFMYrgG3vQkhL77Dxqsiqn8k79ZEUX-QIAhlC7BKwDzuzngNQSejBOwoPiJitCfOspkbmKVjFYvV8omMk7EGzuoPsHRZ1AfqLy0w4kNnWu6jSNrnkg6EJrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WGOFm0ETGGmGi9F0TsE491ugGt6-0OpyNNcK34al3_NylfvPRuNJgFRifkH2PyodGIdaEyqgh1A6_dt15bAdkJ4QqQnqWUMOkUEjcdcbhruakSjQncWJBWSMXwAdGE-VGAn3CymVm32azguyEMYaIpY_qRJIA0YUpfLXfLTQSYqLCxpTxEE812JWPhJqytzwdqbrCv35N-mvjecK8h6h2rJZuFAnyjf9SYNQEIUwuFtDLxmvAIdGsVxL5jShfn3XntFIYYhip1RamnScAw81L_Y-pwuP3CLOtj_UztbPn_Zyd9ekXpTJf3Ju89BvI9TMHGtdu95Px4Xv8Io_wQP91g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، تهدید دونالد ترامپ مبنی بر آغاز کارزار اقتصادی گسترده موسوم به «روز دی اقتصادی» علیه ایران را تلاش برای سرپوش گذاشتن بر «بحران‌های داخلی آمریکاست» توصیف کرد و از «بدهی‌های بی‌سابقه و هزینه‌های فزاینده نرخ بهره» به عنوان نمونه‌هایی از این بحران‌ها نام برد.
@
VahidOOnLine
معاون وزیر امور خارجه جمهوری اسلامی ایران سخنان ترامپ در مورد کارزار «روز دی اقتصادی» علیه ایران را تلاش «محاسبات غلطی» خواند که برای پوشاندن «شکست‌ بزرگتری» ساخته شده است.
کاظم غریب‌آبادی نوشت: «ادعا می‌کنند ایران در آستانه شکست است و به یک نخ بند است، اما به همه متحدانشان التماس می‌کنند که کمکشان کنند.»
معاون وزیر امور خارجه ایران در ادامه افزود: «جنگ نظامی نتیجه نداد، حالا اسم شکست بعدی را جنگ اقتصادی گذاشته‌اند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/77966" target="_blank">📅 15:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=HLJ8KISmVGSZACS4fcqY24uMF3udGzrgLn78d35aCE7zsdF6oN4GIwctRjS4FaUMPdL8-aY0DqGf_jQ0I_JXKiCUUxwTIjM1gLHyHNd4lD_SIAI-f1GXVXZIF8g1Pwb_DPLYFBTXpmiV1qkKzkcHXifKc4QeHEGeXYpcRtJixeSVXKWj4XoLHNjg_8_qpWcyz1N322fjArICTBVFRToWUiwD-6llBs2WDuoa8qkE6K05MlGLTHd8reCQPr1aUG9F7sA5Kl1MaCWD3NCl9KOBob4C30zcDg1v6f-nyoFkYeWkDzPgNzO39Qkhvw22mJXfhzfmaCtX1umOEQY1g-zaSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ab9ff1cf5.mp4?token=HLJ8KISmVGSZACS4fcqY24uMF3udGzrgLn78d35aCE7zsdF6oN4GIwctRjS4FaUMPdL8-aY0DqGf_jQ0I_JXKiCUUxwTIjM1gLHyHNd4lD_SIAI-f1GXVXZIF8g1Pwb_DPLYFBTXpmiV1qkKzkcHXifKc4QeHEGeXYpcRtJixeSVXKWj4XoLHNjg_8_qpWcyz1N322fjArICTBVFRToWUiwD-6llBs2WDuoa8qkE6K05MlGLTHd8reCQPr1aUG9F7sA5Kl1MaCWD3NCl9KOBob4C30zcDg1v6f-nyoFkYeWkDzPgNzO39Qkhvw22mJXfhzfmaCtX1umOEQY1g-zaSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالناصر همتی، رئیس بانک مرکزی ایران، در یک گفت‌وگوی تلویزیونی تأیید کرد که صادرات نفت ایران در حال حاضر متوقف شده است.
او شامگاه چهارشنبه ۲۸ مرداد اظهار امیدواری کرد که تفاهم‌نامهٔ ایران و آمریکا احیا و مذاکرات از سر گرفته شود.
این نخستین بار است که یک مقام رسمی جمهوری اسلامی به شکل رسمی از «توقف» صادرات نفت ایران خبر می‌دهد.
در هفته‌های اخیر برخی مقام‌های جمهوری اسلامی با اشاره به تشدید بحران اقتصادی و معیشتی، نسبت به دور تازه اعتراض‌ها هشدار داده و از آمادگی برای برخورد با آن خبر داده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/77963" target="_blank">📅 15:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HVgZe9pgcsQIBhfVPWWU_lZCqZCrY75PAet4JEnslt5sbAQy-Z789j8xsgwdFrEy3Anit8B0o6E4JegIlcAq4K1dbBu9XDKqqlKZ0FCU8L9O51I8IBeJPvI8veCAg2r98rlzb28d6BddeLIgs7y9IjB8l8CJi189gyn78vXj_Tdt6vSXCoJjfp0GZIKPKhgqfka9-8dIHZY_nCqQPh_yds7eYDLLRyEnbdZZtjg9xqa9VGB8AXYn9ILdqSXF7C9LQzR6XfS0mgNlt-_Mu_Tqk-VMCzrAL1DvwsjVeMuXF1XllsUq3t9JlvBthD8K81Vagltu1sYQ2YfuqAc61OVcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی صبح پنج‌شنبه ۲۹ مرداد ۱۴۰۵ «قائم حسینی»، معروف به «آرین»، را در ارتباط با اعتراضات دی‌ماه اصفهان اعدام کرد. او پنجمین فردی است که در پرونده موسوم به «میدان علیخانی» اعدام می‌شود.
خبرگزاری میزان، ارگان رسانه‌ای قوه قضاییه، حسینی را «تبعه خارجی» معرفی کرده، اما تابعیت او را اعلام نکرده است. در این گزارش همچنین اطلاعاتی درباره زمان بازداشت و محل نگهداری منتشر نشده است.
قوه قضاییه حسینی را به «دخالت در وقایع میدان علیخانی اصفهان»، کشیدن سلاح، ایجاد رعب‌ووحشت و ناامنی گسترده و اقدام علیه امنیت ملی متهم کرده بود. براساس گزارش رسانه‌های حکومتی، حکم اعدام او پس از بررسی فرجام‌خواهی در دیوان عالی کشور عینا تایید و اجرا شده است.
قوه قضاییه پیش‌تر «ابوالفضل سپاهی»، «امیرحسین صفری»، «عرفان اسفندیاری» و «گل‌محمد محمدی» [پسرعمه قائم حسینی] را در ارتباط با همین پرونده اعدام کرده بود. همچنین میزان اعلام کرده بود که برای ۱۶ نفر در این پرونده کیفرخواست صادر شده است.
شروین باقریان، امیرحسین ملکی و علیرضا سپاهی، سه محکوم دیگر این پرونده‌اند که درباره احکام نهایی و وضعیت کنونی آن‌ها اطلاعات شفافی منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/77962" target="_blank">📅 15:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJ4BPyGNWIi40Opl3h1HTepdyvrpbckm9suGRyxKr6sj8R88X7f8zeemyz_YD0MMjYQW3mlOPX7QQFqYhFInqcZhIJyPVd7XWgqmcHfXR7oPoXvefm6xw12ieTAZLcYadS25IEcXo_D44sWtsKf1W0f9B0ohPQWcC1FkqRE0rzSSS3dsqVat__08W9eApm7ypKjbh8gCJEJATbnYIL6mOwZEgpZEHin4KHBwW3XTExot-XXkMMZXuXhg4Kt1Vqt9bgrN8pstvz-jT4_PiTuuIKB2OIPXjaURIep1v2JgoxIknLQBpOE3ctUvvhSEMwTJPZ216F2FvO7SOvCtGLgExQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
ترامپ:
هیچ‌کس بیش از من به جمهوری اسلامی ایران فرصت بزرگی برای رسیدن به یک توافق نداده است. به‌طرزی فاجعه‌بار برای خودشان، نتوانستند از آن استفاده کنند.
بنابراین، امروز اعلام می‌کنم که
کوبنده‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد!
این، جنگ اقتصادی و انزوا در مقیاسی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از بین رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان اکنون به تلی از آوار تبدیل شده، پولشان بی‌ارزش است و کشورشان به مویی بند است.
امروز همچنین اعلام می‌کنم که
هر کشوری
که به مؤسسات مالی، کسب‌وکارها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با
پیامدهای اقتصادی عظیمی
روبه‌رو خواهد شد.
قاچاق نفت، خطوط سوآپ، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها، شرکت‌های پوششی — همه این‌ها باید
همین حالا
متوقف شوند. خودتان می‌دانید چه کسانی هستید.
این یک
D-Day  اقتصادی (ECONOMIC D-DAY)
خواهد بود و ما به همه متحدانمان نیاز داریم که در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و شکست دهند.
این دیوانه‌ها به آخر خط رسیده‌اند و این اقدامات تاریخی آنها و توانایی‌شان برای گسترش ترور در سراسر جهان را فلج خواهد کرد.
ایران هرگز سلاح هسته‌ای نخواهد داشت.
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور
دونالد جی. ترامپ
realDonaldTrump
توضیح چت‌جی‌پی‌تی: D-Day در اصل اصطلاح نظامی برای «روز آغاز یک عملیات بزرگ» است، اما در کاربرد عمومی تقریباً بلافاصله عملیات نرماندی در ۶ ژوئن ۱۹۴۴ و آغاز تهاجم گسترده متفقین در اروپا را تداعی می‌کند. بنابراین ترامپ با گفتن ECONOMIC D-DAY می‌خواهد بگوید این اقدامات اقتصادی قرار است چیزی شبیه یک حمله بزرگ، تعیین‌کننده و همه‌جانبه در جنگ اقتصادی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/77961" target="_blank">📅 02:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">Vahid Online وحید آنلاین
pinned «
⚠️
تبلیغات خطرناک فیلترشکن
⚠️
من  فیلترشکن و VPN تبلیغ نمی‌کنم. کلا هیچ تبلیغاتی انجام نمی‌دم. تبلیغاتی که اینجا دیده میشن به خود تلگرام سفارش داده میشن و من ازشون بی‌خبر هستم.  به نظر میاد همه تبلیغات هم کلاهبرداری باشند به ویژه اگر درباره فیلترشکن و فعالیت…
»</div>
<div class="tg-footer"><a href="https://t.me/VahidOnline/77960" target="_blank">📅 01:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MS5PWflXc5j_UAViOIR4_xJ-eOKY44p8T1soCFY13XVxis7BTBERoygVyPIzOKAyLXQNNDl8SR-JNs8XlcRHR7au6dcs4Ab-_BIK2QHqw6f3AX09ukEHue77wQNBsvSNBqrsCKzc3jBPaeJbIvpDW4M4JT12kR9b_0PQbj1KiWHA3R3WwtCbz3ZXa8DymZEimueC0V3hWJOsC_mWuwlGWFa9iejqXA74grmKWcCH3nxd0cU-g4IJKzbaHeC3qDX_CGi7JPVDNOAuFurwU6c2Kx49vCvX6xAqrGD4ewt_IdkydphZMygm_VH8LxX-thmJiZgeCyPO8BhHg2D_9va_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت اکسیوس، روز چهارشنبه ۲۸مرداد ۱۴۰۵، گزارش داد، ارتش آمریکا طی هفته‌های گذشته یک مسیر کشتیرانی تحت کنترل خود در بخش جنوبی تنگه هرمز ایجاد کرده که امکان انتقال روزانه میلیون‌ها بشکه نفت به بازار جهانی را فراهم کرده است؛ اقدامی که به گفته دو مقام آمریکایی، بخشی از اختلال ایجاد شده در صادرات نفت در جریان جنگ را کاهش داده است.
این دو مقام آمریکایی به اکسیوس گفتند در چارچوب این عملیات، هر شب حدود ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز و در امتداد ساحل عمان وارد یا خارج می‌شوند. به گفته آنها، اکنون حدود ۱۰ میلیون بشکه نفت در روز از طریق این مسیر از تنگه خارج و وارد بازار جهانی می‌شود؛ رقمی که تقریبا نیمی از حجم انتقال نفت پیش از جنگ است.
به نوشته اکسیوس، عملیات آمریکا تنها به اسکورت نفتکش‌های حامل نفت محدود نمی‌شود. نیروهای آمریکایی نفتکش‌های خالی را نیز از دریای عرب از مسیر تنگه هرمز وارد خلیج می‌کنند تا این نفتکش‌ها پس از بارگیری نفت در بنادر کشورهای منطقه، دوباره از مسیر جنوبی تنگه خارج شوند.
یکی از مقام‌های آمریکایی که از نزدیک در جریان این عملیات قرار دارد، گفت آمریکا حدود دو ماه است مسیر جنوبی تنگه هرمز را تحت کنترل دارد. او افزود سپاه پاسداران ممکن است برای کشتی‌ها «مزاحمت» ایجاد کند، اما کنترل تنگه را در اختیار ندارد.
بر اساس این گزارش، عملیات انتقال نفت از سوی یک گروه ویژه مستقر در مقر ارتش آمریکا در فورت براگ در ایالت کارولینای شمالی هماهنگ می‌شود. این گروه با کشورهای عرب منطقه همکاری دارد و هر روز فهرستی از کشتی‌هایی که قرار است از خلیج فارس وارد دریای عرب شوند و همچنین نفتکش‌های خالی که برای بارگیری نفت وارد خلیج می‌شوند، تهیه می‌کند.
کشتی‌ها هر شب در دو بازه زمانی مشخص، در قالب دو کاروان جداگانه برای ورود و خروج از تنگه حرکت می‌کنند و با هدایت نیروهای آمریکایی از مسیر جنوبی عبور می‌کنند. جنگنده‌های نیروی هوایی آمریکا نیز برای مقابله با موشک‌های کروز و پهپادهای ایران از این عملیات محافظت می‌کنند.
به گفته مقام‌های آمریکایی، ایجاد این مسیر پس از یک عملیات دو هفته‌ای فرماندهی مرکزی آمریکا، سنتکام، علیه سامانه‌های راداری و نظارت دریایی ایران امکان‌پذیر شد. در نتیجه این عملیات، توان ایران برای رصد تردد کشتی‌ها در مسیر جنوبی تنگه هرمز کاهش یافته است.
مقام‌های آمریکایی می‌گویند ایران اکنون برای نظارت بر این مسیر عمدتا به چند رادار بازسازی‌شده و نیروهای مستقر در قایق‌های تندروی سپاه متکی است. به گفته آنها، کاهش توان رصد باعث شده است حملات پهپادی و موشک‌های کروز ایران بیشتر به سمت مناطقی انجام شود که احتمال می‌رود کشتی‌ها در آن تردد داشته باشند.
اکسیوس گزارش داده است که شماری از کشتی‌ها در حملات ایران آسیب دیده‌اند، اما نیروهای آمریکایی نیز تعدادی از حملات را رهگیری کرده‌اند. به گفته یکی از مقام‌های آمریکایی، نیروهای این کشور در اوایل هفته جاری هشت پهپاد و دو موشک کروز ایرانی را سرنگون کردند.
بر اساس این گزارش، طی دو هفته گذشته هر شب ۱۵ تا ۲۰ نفتکش از مسیر جنوبی تنگه هرمز عبور کرده‌اند و میانگین انتقال روزانه نفت اکنون به نزدیک ۱۰ میلیون بشکه رسیده است. مقام‌های آمریکایی می‌گویند در برخی شب‌های هفته‌های اخیر، حجم نفت خارج‌شده از خلیج فارس به ۱۵ تا ۲۰ میلیون بشکه نیز رسیده است.
به گفته یکی از این مقام‌ها، در یکی از شب‌های این هفته بیش از ۲۰ کشتی برای عبور از مسیر جنوبی تنگه برنامه‌ریزی شده بود و در صورت اجرای کامل برنامه، حدود ۱۵ میلیون بشکه نفت از خلیج خارج می‌شد.
دونالد ترامپ، رییس‌جمهوری آمریکا، نیز در گفت‌وگو با اکسیوس گفت «حجم بسیار زیادی نفت» از تنگه هرمز خارج می‌شود. او در عین حال گفت آمریکا در حال حاضر با ایران مذاکره نمی‌کند و افزود جمهوری اسلامی در مذاکرات «وقت تلف می‌کند».
ترامپ همچنین گفت ایران هنوز توان مقاومت دارد، اما در مجموع «بسیار ضعیف‌تر از گذشته» شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/77959" target="_blank">📅 01:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=odk8Yvnaa9GNTauIb8Dy94CN13ebrBduOJJj5njEbzOcibElXtqwAq3ShB8ZT-MXyW_5PFG3Xb-6X2xDrmT4m5oSyXkZGgHXsLC5pmfuxRJFwNODoPJgnvQjenri3zrYPIqiSHRkQkQrec1CLlAjMavvJeUjJ5KCcMrIftVxB3Xul74yiR6toIj_hFMdaJpG1G9LR0oXZdZzCjlEpH6ASo2v7_dmbSTZGnpeEcyRISdBXoTpby7SRr_ExC5b999f3UY29bYihtWrqtgH9qxgA9MKfeFFhmefcIUQPkl09bEHN-PK86i600-mObUCjQmqNhhJhgeXaZmNGDAV3ZJb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1a65b09283.mp4?token=odk8Yvnaa9GNTauIb8Dy94CN13ebrBduOJJj5njEbzOcibElXtqwAq3ShB8ZT-MXyW_5PFG3Xb-6X2xDrmT4m5oSyXkZGgHXsLC5pmfuxRJFwNODoPJgnvQjenri3zrYPIqiSHRkQkQrec1CLlAjMavvJeUjJ5KCcMrIftVxB3Xul74yiR6toIj_hFMdaJpG1G9LR0oXZdZzCjlEpH6ASo2v7_dmbSTZGnpeEcyRISdBXoTpby7SRr_ExC5b999f3UY29bYihtWrqtgH9qxgA9MKfeFFhmefcIUQPkl09bEHN-PK86i600-mObUCjQmqNhhJhgeXaZmNGDAV3ZJb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
خبرنگار: وزیر خزانه‌داری می‌گوید ممکن است همین هفته شاهد اثرگذارترین تحریم‌ها علیه ایران باشیم. این تحریم‌ها چه زمانی اعمال می‌شوند و چه چیز دیگری ممکن است در ایران تحریم شود؟
🔻
ترامپ:
خب، چیزهایی داریم که می‌توانیم تحریم کنیم. ما تحریم‌های بسیار سختگیرانه‌ای داریم و خواهیم دید چه می‌شود.
در حال حاضر، تنگه باز است. کشتی‌های زیادی در حال عبورند. این را گزارش نمی‌کنند و ممکن است در مقطعی کمی کند شود، اما همین حالا تعداد زیادی از کشتی‌ها در حال عبورند.
محاصره دریایی بسیار مؤثر بوده است. صفر. یعنی واقعاً، تا وقتی برقرار بوده — و مدت زیادی هم هست که برقرار است — به‌جز یکی دو وقفه کوتاه که عمداً آن را بر اساس یک توافق باز کردیم. اما آن توافق به نتیجه نرسید. می‌دانید، توافق آن‌طور که آنها گفته بودند از آب درنیامد؛ وقتی یک چیز به ما می‌گویند و کار دیگری می‌کنند.
اما محاصره ۱۰۰ درصد موفق بوده است. هیچ کشتی‌ای وارد ایران نشده، اما کشتی‌ها برای جاهای دیگر وارد می‌شوند. خواهیم دید. خواهیم دید چه می‌شود.
یا اوضاع بسیار خوب خواهد شد و قیمت نفت مثل سنگ سقوط خواهد کرد، یا دقیقاً همان کاری را که داریم می‌کنیم ادامه می‌دهیم. می‌دانید، از ۳۵۰ دلار برای هر بشکه حرف می‌زدند و امروز ۸۴، ۸۵ دلار است و ما داریم نفت زیادی استخراج می‌کنیم.
اما اتفاق دیگری که افتاده این است که مردم گزینه‌های جایگزین دیگری پیدا کرده‌اند که هرگز به آنها فکر نمی‌کردند: تگزاس، آلاسکا، لوئیزیانا و جاهای دیگر. علاوه بر این، تعداد بی‌سابقه‌ای خط لوله در حال ساخت است. بنابراین فکر می‌کنم تنگه هرمز دیگر به آن اندازه که در گذشته اهمیت داشت، مهم نخواهد بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/77958" target="_blank">📅 01:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I9MtNZ9KeVKAk3_UJvYD4VG6okhhjBdIuspOgDkgKK-eJfbR3OO38AGHHjo9IqJDpowfNHfvRnNOavwtJkG3lZmIJAZOVvEJGlDOlmAJcH6-3JpUqewelC-1ML6t04ZZbGXYKnQzK7ELk6NJjeyVGfKlnY26WuoFWcUg_qjv1JjdF8IUDJokSWunCkoxftjc7BmjNZz3sof2HK_i9JqlED3X8I4-PqpD9s0NTdnM9-afxV0bS0ckctmaCZpYQdXezwDQA8k_wmuP5o0wlJ7__xJo3qnaKln5qcsZekRgDrmYKdGn5lcGwclXkNdYhURXoMKIFIEsKUIz2CCV_yFVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت فرانسه روز چهارشنبه نیلوفر شادمهری، رایزن فرهنگی سفارت ایران، در این کشور را اخراج کرد.
ساعاتی پیشتر وزیر امور خارجه فرانسه رسما خبر داده بود که به عنوان اقدام متقابل دو وابسته سفارت ایران را از فرانسه اخراج خواهد کرد.
هنوز نام و سمت فرد دوم که از فرانسه اخراج خواهد شد اعلام نشده است.
پس از آن که وزارت خارجۀ ایران در بیانیه‌ای دو تن از کارکنان پیشین سفارت فرانسه در تهران را عنصر نامطلوب اعلام کرد، فرانسه نیز از اقدام متقابل درباره دو دیپلمات ایرانی خبر داد.
در بیانیه وزارت خارجه ایران آمده بود که با توجه به «فعالیت‌های خلاف حقوق بین‌الملل، به‌ویژه کنوانسیون روابط دیپلماتیک ۱۹۶۱» از سوی دو مامور شاغل در سفارت فرانسه، این دو فرد عنصر نامطلوب شناخته شده و حق بازگشت به ایران را نخواهند داشت.
طی روزهای اخیر مشخص شده که این دو فرد، از کارکنان بخش فرهنگی سفارت فرانسه بوده‌اند و ظاهراً در ارتباط با پروژه‌ای فرهنگی، با دو گرافیست ایرانی دیدار کرده بودند.
این دو گرافیست هم از همان زمان در بازداشت هستند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/77957" target="_blank">📅 23:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=HdOdPc3ve6o0x9l-iTnvJl0LJ8LkfAx-KBe9hFDNIsVNTqWzDl1n0SujLnRfyk8-JAZgjQxDOh9QxeJ4cflmKyQ6oPG9y4LHIYX42QBJdSLVYvNN6-zxWAB2xleSZg1AdaZFYniDyMKY0TLYxPl24h_dy4TEu6-j-5m93A7q7ix_o8pv-KSKWt7naXAOIxhyo1Idqz1y0cT7ny3VH0BL-AA8CdNMtEeTJiqslqvl22K4foeCR0aVl8I5TvbWI6GlBeTBSOSw-GNe6Y1q6Jw-lc1SmGDg7AQBtgDD4gFtO7lq4YFmSkksAUKvm2vuXFrc63ghi_3QdbgPFUBq6ViU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/168f12d8a1.mp4?token=HdOdPc3ve6o0x9l-iTnvJl0LJ8LkfAx-KBe9hFDNIsVNTqWzDl1n0SujLnRfyk8-JAZgjQxDOh9QxeJ4cflmKyQ6oPG9y4LHIYX42QBJdSLVYvNN6-zxWAB2xleSZg1AdaZFYniDyMKY0TLYxPl24h_dy4TEu6-j-5m93A7q7ix_o8pv-KSKWt7naXAOIxhyo1Idqz1y0cT7ny3VH0BL-AA8CdNMtEeTJiqslqvl22K4foeCR0aVl8I5TvbWI6GlBeTBSOSw-GNe6Y1q6Jw-lc1SmGDg7AQBtgDD4gFtO7lq4YFmSkksAUKvm2vuXFrc63ghi_3QdbgPFUBq6ViU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ هنگام بازدید از محل احداث بالگردگاه جدید در کاخ سفید، در پاسخ به پرسش خبرنگاران درباره احتمال گفتگو با تهران اعلام کرد که در حال حاضر شرایط مطلوب است، اما امکان مذاکره در آینده وجود دارد.
ترامپ با تاکید بر موضع واشنگتن در قبال برنامه هسته‌ای ایران گفت: «موضوع بسیار ساده است؛ آن‌ها باید به‌طور کامل سلاح هسته‌ای را کنار بگذارند. ایران نمی‌تواند سلاح هسته‌ای داشته باشد، چرا که از آن استفاده خواهد کرد و ما اجازه چنین کاری را نخواهیم داد.»
رئیس‌جمهوری آمریکا در نهایت تصریح کرد که ایران نباید به سلاح هسته‌ای دست یابد و دست نخواهد یافت.
@
VahidOOnLine
ترامپ افزایش عبور کشتی‌ها از تنگه هرمز خبر داد و گفت آمریکا کنترل کامل این آبراه را در اختیار دارد. به گفته او، شب گذشته تعداد زیادی کشتی از تنگه هرمز عبور کردند و اقدامات ایران، از جمله شلیک گاه‌به‌گاه به پهپادها را «مزاحمت» توصیف کرد.
رئیس‌جمهوری آمریکا همچنین گفت قرار نیست همه کشتی‌ها از تنگه هرمز عبور کنند، اما تردد در این آبراه ادامه دارد. ترامپ پیشتر نیز از کنترل کامل آمریکا بر تنگه هرمز سخن گفته بود و مقام‌های ایران این اظهارات را رد کرده‌اند.
@
VahidOOnLine
ترامپ می‌گوید مردم در حال یافتن جایگزین‌هایی برای تامین نفت به‌جای تنگه هرمز هستند و تگزاس، آلاسکا و لوئیزیانا را از جمله این گزینه‌ها معرفی کرد. او گفت خریداران برای تامین نفت به ایالات متحده روی آورده‌اند.
او گفت یکی از دلایلی که قیمت نفت به ۳۰۰ یا ۳۵۰ دلار در هر بشکه نرسیده، افزایش عرضه و روی آوردن خریداران به منابع جایگزین است. او افزود قیمت نفت اکنون حدود ۸۳ تا ۸۵ دلار است و پس از پایان شرایط کنونی، بسیار پایین‌تر خواهد آمد.
رئیس‌جمهوری آمریکا با تاکید بر اینکه این کشور نفت کافی در اختیار دارد، گفت: «مردم دارند جایگزین‌هایی پیدا می‌کنند. یکی از این جایگزین‌ها تگزاس است. یکی دیگر آلاسکا و دیگری لوئیزیانا است. آن‌ها برای تهیه نفت به ایالات متحده می‌آیند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/77956" target="_blank">📅 20:07 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jMIBxZPCqgaabU6bzeK3zoNddsVe5GxF2EhumAOT-KRJ48LpN6sgjfWOEm2SgfUA_LmmZPDSW75KNYamJkOf0S8fVfpzEsp7XuKvEyz8roJXnTV-SxF7H24C0SU26lAh-ceGzvSze7Do-_gKrht7Ubf_kMvzh0ivzC1reWnroHsAJVEBxvzisOTc_3hduDrmxgOlj9oe54vVBgUIk6jM1AMTu9lsEfzIikRRLH7TNipaLqXUFPoDPmrkCb5LbEZ4tWMPyteFFlAYEIr7GSH9VDL7Eqyzv008m-iA9SrbuemNOqvCOEh9yJntVaVwoYR_MYUo1Xtz19iP7-9MyXRK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aQhejQQR2ZB6vB4aL3Jz0CVy-soHxVLyYewSbh7kYH3JKD30oUVknGs2FriqOn7wM2nZsVb_bfTBeuDt_Cgo7SwXq_jkD84dlQTzwuB2maHbd1u-n9WqN-gZ7UidSUkcOt1eAxOuMJF0ygCg7d8F1jwWyZfjF3lYXoxCh2BPBw7aMwVOi4NRb-CtsbT_x67NVLh94Nly4of4LNFCmvv0TdWi9Ykh-j8UNfLmvzJXQv9PMyfrZFAxhloerzyfD2ahAqCAAKXzKpBroHtXrkwbr8HJxvJrnPtjBcmuX4Y3qRasNkfjbGBkNumKFfSKFarMreQEB-FfRRavaojIGUCokw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فاینشنال تایمز روز چهارشنبه ۲۸ مردادماه با انتشار گزارشی به نقل از دو مقام ارشد جمهوری اسلامی گزارش کرد که اگر دونالد ترامپ تصمیم به گسترش جنگ بگیرد، هدف قرار دادن پایگاه‌های نظامی در جنوب شرقی اروپا را بررسی خواهد کرد.
براساس این گزارش، یک پایگاه نظامی در بلغارستان و یک پایگاه نظامی ناتو در قبرس از جمله اهداف احتمالی جدید ایران در صورت تشدید درگیری‌ها خواهند بود.
مجلس بلغارستان ماه گذشته با استفاده آمریکا از یکی از پایگاه‌های نظامی این کشور موافقت کرد.
همین دو مقام که نام آن‌ها اعلام نشده می‌گویند نیروهای مسلح جمهوری اسلامی به‌طور جداگانه حمله به کابل‌های فیبر نوری زیر دریایی در تنگه هرمز را در صورت تشدید تنش‌ها، بررسی کرده‌اند.
@
VahidOOnLine
یک مقام سازمان پیمان آتلانتیک شمالی، ناتو، به خبرگزاری آنادولو گفت: «ناتو برای مقابله با هر تهدیدی آماده است و همواره هر کاری را که برای دفاع از همه متحدان لازم باشد، انجام خواهد داد.» این اظهارات پس از انتشار گزارش‌هایی مطرح شد که بر اساس آن‌ها، ایران در صورت تشدید بیشتر جنگ از سوی دونالد ترامپ، حمله به اهداف نظامی آمریکا در اروپا را بررسی کرده است.
این مقام ناتو همچنین به رهگیری موشک‌های بالستیک ایران در اوایل سال جاری اشاره کرد و گفت پدافند هوایی ناتو در چهار مورد جداگانه، موشک‌هایی را که به سمت ترکیه در حرکت بودند، رهگیری کرده است. او این اقدام را نشانه قدرت و موثر بودن وضعیت بازدارندگی و دفاعی ناتو دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/77954" target="_blank">📅 16:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GUzfk1RBZAibHDkeJlzjF-CkPmGoFTMKMKDlRTuf73RdFO07jr81ZQXrKIx55ex1MimDBT_o0FcfwyjAtFK0KmUcSsdya_5_k-yrYGzNE_F65Qnv2wPJ8IgUUURq6qTuUrAw7UD2PTYIF_hTGn5S3VGVbjblW0QkqS7V3K1zhIxyNWgaolSxFbzCk7xb-V9i4nn3dStvmGJ59xArSDl1gOyaxrB-eoojXcpaU904H3fPjU7lzljEBOKXPlQlum6jablh26Gmx3MUIMy4fGVSp5tYQjOl1s455C1vvSO21f4I-eFdfNXaWInXuLwzZ2thztskQ3882PTt5IswjkRtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mLkzxWTWBR4Bbxj5v8aNBsrOYhLUzUn18CZeIFO7ykeTEoDaz4NgZHtqhkGUdAfI03YdYwHQktl1BXIiMttgxGWOPqfnlICFPfAZQ1eJNFEHaIAGe7w7c4699xHvKF0Zw0gMQeU9eJCqQ9izS9RfaYjRLYDaem0KaLhBhvv8KYeoCgB8ih8sJiakx4sG5dhsDSg63AbhQGN9sBamW7ZvxCQrOsjhk_22728SYckSGnXyUioL5Xrm6Kp6dyVbTVFD-t2QmgRFavIiJe-c52NSVwB079Z-MR1zahtrdxtNbw2lGWknnuSqdTzTIiwcvqz8QrRYVd3U1BkLYT4y4ben8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روند افزایشی قیمت جهانی نفت، همزمان با مبهم‌تر شدن سرنوشت مذاکرات مربوط به بازگشایی تنگه هرمز، ادامه یافت و قیمت هر بشکه نفت خام برنت روز چهارشنبه ۲۸ مرداد با یک درصد افزایش نسبت به روز قبل به ۹۲ دلار رسید.
روز سه‌شنبه دونالد ترامپ گفت «هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است».
@
VahidHeadline
قیمت ارزهای خارجی در بازار آزاد ایران روز چهارشنبه ۲۸ مرداد بار دیگر افزایش قابل‌توجهی پیدا کرد و قیمت دلار آمریکا به ۱۹۱ هزار تومان رسید.
این بالاترین میزان برابری دلار آمریکا با ریال ایران در سه هفتهٔ اخیر محسوب می‌شود.
گزارش وب‌سایت‌های اعلام نرخ ارز و طلا نشان می‌دهد که قیمت یورو نیز بار دیگر از ۲۲۰ هزار تومان فراتر رفته و هر قیمت درهم امارات نیز از ۵۲ هزار تومان عبور کرده است.
روز چهارشنبه هر سکه طلا هم ۱۹۴ میلیون تومان معامله شد.
افزایش قیمت ارزهای خارجی و طلا به دنبال اعلام امارات متحده عربی در توقف هرگونه مبادله تجاری و مالی با ایران رخ می‌دهد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/77952" target="_blank">📅 16:43 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gzS_kikFEI9-RmfkFOIL2IKXvwJU0O0ocXWIZ-PJHPj-ia6Mf33mZq9sNL5Q8spvKKz3OYKRj1RF5_migIJWyG3_l8jKPMehQ0i1trl6YL3d-7SiNwSxvj2nQYLItmn7jg6f6nzwYoQSZFvCT3amYy3ICyznNP8Kd2Ns1FRTTP8zCJxub9qtWNBefqN3iDXIXHvZkuqAkpl0eqdq1IUVoxgIRwTfziDqqhb1oet02IPkPxf4my8wUI7ujvQLaD4dNoHDM-958RjQTlm29coqTvWaDV1j4zHRCwYx-4MHW4XNZFinxRUdSZzhPHzVn2xJbzqGjQh0N28NXAVxBv5V7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وای‌نت، نفتالی بنت، نخست‌وزیر پیشین اسرائیل، گفت که در صورت بازگشت به قدرت، معادله بازدارندگی را تغییر خواهد داد و هر حمله حزب‌الله باعث خواهد شد ما ایران را هدف قرار دهیم.
نفتالی بنت همچنین وعده داد قطر را «کشور دشمن» اعلام کند.
نخست‌وزیر پیشین اسرائیل ادامه داد: «ترکیه و قطر را از غزه خارج خواهیم کرد و به جای آن‌ها مصر را وارد می‌کنیم و در عین حال آزادی عمل اسرائیل در غزه را حفظ خواهیم کرد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/77951" target="_blank">📅 16:41 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZrFMaKSqGkDhiu_MoCYh2h6WKiW76yYBTyiMexl3TkcUvF0JwLmBg3vn_xONC9jiEJAaxzcuNl4dpYQe5oXdbaQtr5hOF-ITK0bV2tucTUR5dNs7hRoHdu-NQG7M-L0GjbCudpDtNTEorOA7Xw2pFGZnCJDK0-XTV9-Gx2dwBvNR_9Kpm-ykYamqsy5TeMCwMZtTUtlp8Z5a_D8b8H4CPGB4HbDnodFQXp7CUOo-ZHhl_sALwFoqoiap87iZ1rPF1AALsBdGUK8VfqRZbHTLMUKVgKv1ey9AA82tLs2QtMsKC7RzkRvK5Kut5pCMNKGUTcHvX5yVxjPEWFcCcogmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد کل نیروهای مسلح جمهوری اسلامی ایران بار دیگر به کشورهای حاشیه جنوبی خلیج فارس نسبت به «هرگونه کمک» به ارتش آمریکا هشدار داد.
در پیامی که روز چهارشنبه ۲۸ مرداد به‌نقل از علی عبداللهی در رسانه‌های ایران منتشر شد، رئیس ستاد کل نیروهای مسلح ایران به کشورهای حاشیه جنوبی خلیج فارس گفته است که «چیزی از چشم ما پنهان نمی‌ماند» و افزوده «این میزان هواپیمای نظامی، به‌ویژه هواپیمای سوخت‌رسان، در پایگاه‌های منطقه‌ای بدون اطلاع کشورهای میزبان بعید به نظر می‌رسد.»
فرمانده قرارگاه خاتم‌الانبیاء در هشدار خود توضیح بیشتری در این باره نداد. شب گذشته امارات متحده عربی اعلام کرد تمام مبادلات مالی و تجاری با ایران را تا اطلاع ثانوی متوقف کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/77950" target="_blank">📅 16:40 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/E_FRj4ApgwaakVsp1Djp9V2DP_9b4SNDbFHZ68gIiPIHvwsnt-786g90aNCVB9mM4zoDSosbwxHbU8OQSktTt16Aws3DlRRsmgqwbVGvrvu3QlDhPXp1C9od_UFSIdvA2HCaD9QJlbV2iMUfguewSYax8qAYatThGeHQIytx_pbZRgBZxk7Y4Lf2-oAUYBKr-N2FVTyQgrPJx2S-QSHYS5D3kDIBZ7nsSYJndfJ0MIj0xwIHw21Lz9DSwLaw6wJdCuKByhhDwy8OPUFrLCazGNhjn6xfjeBBu5NbZ6gLzkcyzygQr9QNgM1xG2n6hFeHQlLRHwHKoZ6xH1lBCMOjIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس، وابسته به سپاه پاسداران، صبح چهارشنبه گزارش داد نفتکش اماراتی که در کریدور شمالی تنگه هرمز توقیف شده بود، مسیر خود را تغییر داده و به‌سمت بندرعباس در حرکت است. بر اساس این گزارش، مقصد اولیه این نفتکش بندر جبل‌علی در امارات بود، اما پس از توقیف، مسیر آن به‌سمت آب‌های ایران تغییر کرده است.
فارس نام این نفتکش، شرکت مالک، پرچم کشتی، محموله و دلیل رسمی توقیف را اعلام نکرده است؛ موضوعی که ابهام‌ها درباره ماهیت این اقدام را افزایش می‌دهد. گزارش‌های بازنشرشده از خبرگزاری فارس نیز می‌گویند این نفتکش هنگام عبور از تنگه هرمز و در محدوده کریدور تعیین‌شده از سوی ایران متوقف شده بود.
این خبر یک روز پس از آن منتشر می‌شود که امارات متحده عربی، ایران را به شلیک دو موشک به این کشور متهم کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/77949" target="_blank">📅 16:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ONJwKgvvyqDuU6ektVnZYUtak00LIGJiqHYqULZFAxcMT4LUJsVuCNiFwi5sehFKZY3GDnco9gYeSWkHVPrBQgJw7RkO6gjon0-TBVgTmhtHJxwwfzs45-JDgIl45OCYr5W1pZcz_FQCsvdOARYvFWwVFCzDPZNhQHps4IMJoffGa5P6Wz36z2OT_MfdweYzvEffLeOjoA8qTuMzHFPnxfk1QLg5pwNR0Z-lJmbMHjrROux_zeRPXEnEoQ37eBLEAhtN2gOAwWnW667ovgdOQT93tUWT0ux_Ewxtgcvj6LXJ8LqRs3-4DQuAVc2pQ9sy1Gy8bn7XmqguvbFxmLoUZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب مشروطه ایران (لیبرال دموکرات) اعلام کرد فؤاد پاشایی، دبیرکل این حزب، هدف «سوءقصد» قرار گرفته و در بخش مراقبت‌های ویژه بستری شده است.
بر اساس بیانیه این حزب، این حادثه ساعت ۷:۴۵ عصر ۱۷ اوت (۲۶ مرداد) به وقت لس‌آنجلس رخ داده است.
حزب مشروطه ایران همچنین می‌گوید پلیس لس‌آنجلس در حال تحقیق دربارهٔ این حادثه است و اطلاعات تکمیلی و «تأییدشده» دربارهٔ این حادثه بعداً از سوی حزب منتشر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/77948" target="_blank">📅 16:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=WqmhLgjcTgqzDFOGxfA-O4g-2urRp0vlpb4qWBmOB-KQQpb9tKE_hBwrQv45rkDod99ZqB6S2rkB-JfT6WCinlf1NSQHnm_Vq7UvW6SVZq4E7FMtnuCBXTyBxRYt58MWzJCdQ7WtQC7jxXJdXapfkxILQtjX7JbrS94vVPlPRGSjVe5kZLwmK_-r00NAaPxWiJmk6dET7MyEwkCJePldifdOGZFyYvlogSYlKic3iEZuCp7Woo8HUw7r7ItuqjPxyzr_u_PPXe0MLXwKQlIQ_CbpEAsIyPRqZJZ2103CdqUayzvNHT0qez5zVfu1QA-MsgilgFW00KjkTZiIrgtyfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/edef31ced2.mp4?token=WqmhLgjcTgqzDFOGxfA-O4g-2urRp0vlpb4qWBmOB-KQQpb9tKE_hBwrQv45rkDod99ZqB6S2rkB-JfT6WCinlf1NSQHnm_Vq7UvW6SVZq4E7FMtnuCBXTyBxRYt58MWzJCdQ7WtQC7jxXJdXapfkxILQtjX7JbrS94vVPlPRGSjVe5kZLwmK_-r00NAaPxWiJmk6dET7MyEwkCJePldifdOGZFyYvlogSYlKic3iEZuCp7Woo8HUw7r7ItuqjPxyzr_u_PPXe0MLXwKQlIQ_CbpEAsIyPRqZJZ2103CdqUayzvNHT0qez5zVfu1QA-MsgilgFW00KjkTZiIrgtyfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیوا سیفی‌زاده، خواننده ایرانی که در جریان تک‌خوانی در «عمارت روبرو» در اسفند ۱۴۰۳ بازداشت شد، روز چهارشنبه ۲۸ مرداد با انتشار ویدئویی اعلام کرد که دادگاه او را به اتهام «تشویق به فساد و فحشا» به چهار سال حبس تعزیری محکوم کرده است.
خانم سیفی‌زاده در این ویدئو به رای بدوی دادگاه اعتراض کرده و می‌گوید: خواندن شعر سعدی و آواز ایرانی چطور می‌تواند مصداق «تشویق به فساد و فحشا» باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/77947" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77946">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kS2PmQOE5M4TKN-vEsX6mfu6I0g5fqk0qHVPLrr-fkXTB61gwsieanNhMKx6J4UBjNRSqsAWUC8u4x3Q_iGcjtaP1vLfNPeVq_58xPPovBQdmR7cY-JCZ5RaFrVMaeIYHeVel49J0zr_GZTG_6dsdWuuutoLBs-AFyuDrivVO4IfN83TdO5dwu4O1ivduxgnejJD48cZl8wyOkrzvNzjbQqUNgFUM3k8S8hCxt3jf-eu6SB7FS0xndDGGM6U-8iIMqVP8fqfuoNiwvmB90XZWZzxMTbQHCDd-kJ9Yb_LsJlljx0uKWt2tdE7TK7FcROo0nB1VCTNdUJdZ1X3PH-vqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرانا: آرمین نورانی، خواننده موسیقی سبک رپ که با نام «خجسته» شناخته می‌شود، بازداشت و پس از مدتی با اخذ تعهد آزاد شد.
در پی بازداشت این خواننده، ویدئویی از اعترافات اجباری وی منتشر شده است.
در این ویدئو که مشخص نیست تحت چه شرایطی ضبط شده، آقای نورانی نسبت به شماری از اظهارات و مواضع پیشین خود در ارتباط با اعتراضات و حمایت از معترضان ابراز پشیمانی می‌کند.
لازم به یادآوری است علاوه بر نقض کرامت انسانی که در سایه ضبط و پخش اعترافات اجباری صورت می گیرد، اساسا تا زمانی که فردی در محکمه محکومیت نهایی دریافت نکند، از منظر قانون بی‌گناه محسوب می شود و هرگونه اعمال مجازاتی پیش از محکومیت نقض حقوق شهروندی و انسانی او محسوب می شود.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/77946" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77945">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d2M-potJ20jq9_AX1Sp8ENDcsi7t5ZXTFqELz8LMdrYZWkA-NdMDuWEJ6mqs02cRL_jt5FPU3JKfcrUc4CBo1LtTlgLbCAzORtW8t4ui-Yvqmw24JSOVxfYwrHjtBP_nUJMhh749nfVoNcvkfFbnyXbQgOLAWCQvPk19uMrnxFB9sjpNOf3kgXwIVNOE1AlwS-6RWGfP-A_qQ9UnHExNWZvnqq_Yi0bTmGawcBXcNfFlN1Js6mD_NKDBhp_rRIh7fbwSuvkpBoeZUCo9OF4y-5rCIkDGkIOC-oty1Q4VFvqs405jZufDfgGVr3ShZU-E3dWry0t8GeAps8yzzGrcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات:  تمام مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شد
مدیر اداره ارتباطات راهبردی وزارت امور خارجه:
افرا الحاملی، مدیر اداره ارتباطات راهبردی وزارت امور خارجه، همه ادعاها درباره وضعیت روابط اقتصادی میان امارات متحده عربی و جمهوری اسلامی ایران را رد کرد.
الحاملی بار دیگر بر تعهد راسخ امارات به گفت‌وگو، همکاری و همگرایی منطقه‌ای به‌عنوان ابزارهای اساسی برای پیشبرد صلح، ثبات و رفاه در منطقه تأکید کرد.
الحاملی تصریح کرد که با توجه به تشدید تنش‌های منطقه‌ای که صلح و امنیت منطقه‌ای و بین‌المللی را تضعیف می‌کند، تمام تجارت، مبادلات تجاری و تراکنش‌های مالی با ایران تا اطلاع ثانوی متوقف شده است.
الحاملی تأکید کرد که امارات همچنان قویاً به حفظ سلامت نظام مالی بین‌المللی، مطابق با حقوق بین‌الملل و بالاترین استانداردهای جهانی، متعهد است.
mofauae
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/77945" target="_blank">📅 23:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77944">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BtSDilnrj1PLGUdeGkhgf1_7xTZ5sV_ea19zf2oucESUIXRIwqMXw391IIk-tQ7uDdRTQeZy10j92L4nNaYxFR2NKVjbPqoKabp2inYmPwim8tnr7uZN0gGKBJ5XFE7xd0PX4cMofMs9Lz-ijlP6u7KZp5Ujw8g_mYm5PFeIf0QF8coHl79DTtv4gxY_BkcBTZ9zJAQpJ30uoXY4vX4_XmecvswH8kQaRU09TE5bfL1Yr8gJ1JhigIMuetOduLhMbWlpgBekkXqwXJCmFxgtEsaGSH1djFNU1YkQl9FLU1KkdbLhzyS58nbsyZdd_aIpMkUi1R5HSTZVwomY4MihXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه فرانسه: دو دپیلمات ایرانی اخراج می‌شوند
ژان نوئل بارو:
مردم ایران، مردمی بزرگ، قربانی اصلی این دوره از تنش شدید در خاورمیانه‌اند؛ مردمی که میان سرکوب خونین اعتراضات ژانویه ۲۰۲۶ و بمباران‌ها در تنگنا گرفتار شده‌اند.
دقیقاً به این دلیل که فرانسه در کنار مردم ایران ایستاده و از هنرمندان، دانشمندان و پژوهشگران آن حمایت می‌کند، دو دیپلمات فرانسوی در ۱۹ ژوئیه گذشته به‌طرزی رسوایی‌آمیز و عامدانه مورد حمله قرار گرفتند.
من اعلام کرده بودم که این اقدام غیرقابل‌تحمل پیامدهایی خواهد داشت. این کار انجام شده است. دو دیپلمات ایرانی در فرانسه در همین چند روز آینده اخراج خواهند شد.
jnbarrot
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/77944" target="_blank">📅 22:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77943">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nf4fw-9HWzOz5pNPd0FNSsPF8lJwxWSaH8qSJ-u-unMM1N5qD-9ajxCvZdFuxZkONcbAWaoJwNxjVfzzOyoraOr6QKTDzE7_sVOARyHyQkNr7KIkzsVfv7GrctjHFeTBPl4VeCW4xT2C6MjCpY3h2t3JWxIN4pWYVvTzUparD0Zj_8DqbhTMXVV-B33oCsQr3DA1bxW3_YRRVtrR0uoh3puWgVlUF2Yt4DVgXeSkBcd1mubALguIRSSxx_TGBriXBY8BjoVgPSPOMvcfwjJI5mmvkPMVkcqEtJtgMjysokrnzkMCFSTqQEOV47ED_OaR1N_BnKnhPAbzbYhxaA33CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف:
آمریکایی‌ها فکر می‌کنند اگر فشار بیشتری بر ایران وارد کنند، می‌توانند امتیازهایی بگیرند که اصلاً جزو توافق نبود. بسنت و هگست واقعاً در حد و اندازه این کار نیستند. دیگر منتظر نباشید این دارودسته دلقک‌ها از کلاهشان خرگوش بیرون بیاورند؛ خودتان افتضاحی را که به بار آورده‌اید جمع کنید.
mb_ghalibaf
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/77943" target="_blank">📅 21:03 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77942">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahid OnLive وحید آن‌لایو</strong></div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/77942" target="_blank">📅 20:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77941">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BksGSXadtME5bH8kXpns7SLckQ7BvpM9TnE0bCJQH0Dhp_U7fLmUd06K3bHgHyaEcDtWrmtE6P8z3deQNImKf8TkUM3IbW-FysfgyzS7nETBBbMhRm8UAnqQ5tQZ2cASqg2HoSYjMJeKUpoWCOcd0ytOuwbHsbUW3E-B1bx1R1HAkOF_2aIDYdVE8jQMKyF3fXEwir6lcuzijhOgLvhLcVVF85INyGba4DMkdIUjQY1aZIaq4TQwtWtqv0atk5xxcZ94bmbkBiF2Ac7gedK3JIj0-n0Gda4nz2RaQm5QUsHEAqEbxgbSf3_w8t078pTZgo0_XaYUYQYN4N6IJF0gfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملی مدیریت شرایط اضطراری، بحران‌ها و بلایای امارات:
سامانه‌های پدافند هوایی امارات متحده عربی یک تهدید موشکی را که این کشور را هدف قرار داده بود، شناسایی کردند. لطفاً در مکانی امن بمانید و هشدارها و به‌روزرسانی‌های منتشرشده از طریق کانال‌های رسمی را دنبال کنید.
NCEMAUAE
آپدیت:
پایان وضعیت اضطراری
پیامک جدیدی که برای شهروندان در دبی ارسال شده:
از همکاری شما سپاسگزاریم. به شما اطمینان می‌دهیم که وضعیت در حال حاضر امن است. می‌توانید فعالیت‌های عادی خود را از سر بگیرید، اما همچنان احتیاط کنید، اقدامات پیشگیرانه لازم را رعایت کنید و دستورالعمل‌های رسمی را دنبال کنید.
-وزارت کشور [امارات]
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/77941" target="_blank">📅 18:30 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77940">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfSuN2zZVLiJ5wuICAEKqeqR9Fg7bGh6mpgUF6tNafbxVii5imr1YZy-Y3Cy76M1LFrnExoKgVsh0bS3HP3ALZmeHxuclTynDETKF4wb795HZwkaJgMoMbzbi778B8JUlx-0xdcTACGDwl_68CrjfYlrArxbGrLGJyqthRisCepUKfgKs3G4VWieRFbwHX1cEPo_5CudbGtx13XQRZSnEaoYrj9HdKJW1dFy7yFZFlcjO30OrAHnoQ5BoCm5Dqi3M_tctwGfsOEk7a4JT55rNiAF3ItcYegr2iW_s6QXRAv0XftktgXmQUHLEgf_VhwnpErIzUFT-x4sUrrWnDG8tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحید همین الان دبی آلرت موشک ۱۸:۵۲ وقت محلی
پیام و تصویر از دو شهروند مختلف
آپدیت: پیام‌ها و تصویرهای مشابه دیگری هم دریافت کردم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/77940" target="_blank">📅 18:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77939">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PUyZjq-6EwZPA3aroukxrdv-lTO8ETFvGsCq6HJT78dzXm1hrIXivQ4jFfQHtwrroOW5ruHxlonwesmY_XwsQRxYwV4PycUSw27YDlgNnMIo9wuRD0XiO-j1lURey3P7yHvbvDE1C8lkGpNl0xssmEL5R0U6BDJC4wHwxVgP9-UEOJbInJhTtjff4q6dITHKueR4Z56YBeKFJ-v39ayNBA90cwUF-yZXiWWEPPUsroQT4kiT6uxlGkXNRaxHCjism4Vp6TQa-bQTiXE6mKV8lD6bYnECj9EerqANvq9sy7PGJgXa-qMr9szWJt7I8-PS5TX7GCJ9LFEYFiJCLqHw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا با تأخیر گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
یک طرف ثالث گزارش داده که یک کشتی فله‌بر هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته است.
این اصابت به سمت راست کشتی آسیب وارد کرده و موجب آسیب‌دیدگی یکی از خدمه شده است.
گزارشی از پیامد زیست‌محیطی این حادثه وجود ندارد.
مقام‌ها در حال تحقیق هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 290K · <a href="https://t.me/VahidOnline/77939" target="_blank">📅 18:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77937">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugY7BAmeaJKTbFKMGKAFLwpN2xOQzacv63Rtn8b8Na_RIWcRjFbMEgFzFC6clzFKZKb3a-RvSNgAmgb1sc6-z69DbluxLTdM5VzrmhUHcR9kU2gytpeFNHrG_1QqVWzr4ZO7tLh4tnQFdJtHgaZUX5duUV5p-QHF81tjmXn8a6ukrk35re_yqTj8oStNuJM05SJ_GlK7S8UKtsedRwV7FSY2AOmsOYZqSZvQ36dEP9eWNqIyKI9PazBBLm2CupzyWjhecnO61aJFzwprhUA0_y7LHXwaqQBGzPBKkLGQyeYkWzYKs765teLFjKhu0G0MabY1NvDkScUmzuwvjVCBqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/77937" target="_blank">📅 17:03 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
