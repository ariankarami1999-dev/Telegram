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
<img src="https://cdn4.telesco.pe/file/egtXoEcx_tpF_EV1eNkOsitnkL3agkPHRyhQJTemD09G8VGWhNYUHeWRq2i4E3HUK-0tjs_A9GAQ6f0CK71AvBIVXEchSB5Dg_nJNcXp_UVbrPzMpOnVCTsMQOq7mv2JFKrw-sYhjg3CUew2iAyu8jw7COmsrPBs1kZHHmya6qMki8W8S7N8mZhPr0OveA55PPuuVxln2fcpOWjMYtrScdKaZFgRmhdk_t9aCpzIjLfBsV3hlJLv_C9dwJCaGaQ-4Aqv0rjyTBAwNW1RfOQfdndQtsHDGPvgPiDRYJgdR1X1Dl12dZlVV_-sM0wAdbiDeF46BycOCZOP3wKyPRzqjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.9K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 03:12:00</div>
<hr>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2637" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔻
بچه ها میگن انقدر پهنای باند دیتاسنتر ها پایین هستش که اکثر روش های تانل که اجرا میکنن سرعت بدی داره یا دچار قطع و وصلی و اختلال زیاد هستش.
خیلی به روش تانل بستگی نداره بیشتر مشکل پهنای باند ضعیف دیتاسنتر ها مربوط هست.
امیدوارم در روزهای آینده وضعیت بهتر بشه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/iaghapour/2636" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEternal</strong></div>
<div class="tg-text">🔔
🔔
🔔
💥
😳
☄️
اینترنت بدون محدودیت رو تجربه کن
⚡️
⚡️
🛜
تجربه‌ای نزدیک به
استارلینک
🚀
⚡️
⚡️
🛜
با هزینه‌ای نزدیک به خرید مودم
💵
💵
😳
😱
کلی امکانات فقط و فقط با خریـــــــــد یک روتر
😱
🤔
❗️
تاحالا فکر کردی بشه کل خونه‌ت همیشه به اینترنت آزاد وصل باشه،
بدون نیاز به روشن کردن فیلترشکن؟!!؟؟!
❗️
😳
❌
✔️
دیگه لازم نیست برای هر دستگاه جدا فیلترشکن روشن کنی
👍
👌
استفاده همزمان چندین نفر با یک اکانت
🔋
کاهش مصرف باتری گوشی و …  (افزایش عمر باتری)
🔥
مورد استفاده برای
تریدرها
_
گیمرها
_
دفاتر و شرکتها
_
کارخانه
و
مصرف حرفه ای خانگی
💥
🚀
✨
اینترنت آزاد رو برای کل خونه یا محل کارت همیشه روشن داشته باش
💥
💥
☄️
قیمتهای ما اصلا قابل مقایسه با جاهای دیگه نیست ،امتحانش مجانیه و هزینه نمیخواد
😉
👨‍💻
👨‍💻
ادمیـــ‌ـــــن
:
Eternal
🛒
📱
کانـــــــال ما :
Router iran
✔️</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/iaghapour/2635" target="_blank">📅 21:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میبینم که رو فیلترشکن ها تخفیف زدن :)
هر گیگ رو 10 و 20 هزار تومن دارن میفروشن :)
پولی که بعضی از افراد به جیب زدن تاجر ها نزدن. طرف داخل سرور ایران سایت فروش فیلترشکن داشت! قعطی نداشت. بالای 10 هزار ممبر داشت. اوایل حتی درگاه ریالی داشت. بعد بعضی ها انتظار دارن ما باور کنیم اینا به جایی وصل نبودن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/iaghapour/2634" target="_blank">📅 21:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭕️
چند خبر کوتاه از رسانه ها
🔸
معاون وزیر ارتباطات در پاسخ به زومیت در خصوص زمان بازگشایی اینترنت سیار نیز گفت: «امروز اینترنت همراه نیز وصل خواهد شد.»
با توجه به این اظهارنظر باید منتظر بازگشایی اینترنت همراه تا پایان امروز، سه‌شنبه ۵ خردادماه، در دسترس کاربران قرار بگیرد. هم‌چنین، طبق اعلام‌های قبلی، تا فردا روند بازگشایی اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴ تکمیل خواهد شد.
🔹
نت‌بلاکس بازگشت بخشی از اینترنت ایران را تایید کرد؛ سطح اتصال به ۳۴ درصد رسید
🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/iaghapour/2633" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/iaghapour/2632" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینترنت بین‌الملل وصل بشه یجوری از اینترنت استفاده میکنم اختلال بخوره دوباره قطع بشه.
🫠
گوشی باید آپدیت بشه.
ویندوز باید آپدیت بشه.
لینوکس باید آپدیت بشه.
برنامه ها باید آپدیت بشه.
و...
حس میکنم شما هم با من هم نظر هستید
🫣
😁</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/iaghapour/2631" target="_blank">📅 10:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔻
این روزا انقدر شایعه و خبر بی‌خود درباره وصل شدن اینترنت پیچیده که واقعاً حس و حال خبر زدن در موردش رو ندارم.
با این حال، سعی می‌کنم اسکریپت‌هایی که زحمت کشیدید فرستادید رو حتماً بررسی کنم، به هر حال از دست رو دست گذاشتن که بهتره. راستش با این وضع زندگی، اصلاً هیچ انرژی و انگیزه‌ای برای آدم باقی نمونده.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/iaghapour/2630" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF6Tb0YCZuI6rGJuHoHV-qZ-nakJGIiz1S_4Gsskq8rtEUk8ICT4aqhCKcyoZjjeqrS7VUgKubo2SAe0A7O0cArROoCyRLSLfb15zv2MAM07kNIHyT_oGRbpDWJsOTMopygUKhdzQWX9t0RvSQSwh6i53Cu9i4F61wzD591KjG0BKkftw3mAIPg1dac_bYwwGUEeK9GrujpKwSlkbmAMgc7gn03hc5jQk73RdKMYMb8EH7NMjXBLG5YChXF1DIG_ZnNaalXWk6M2R2cN0k_hxqnNbOyNP1GxlttWtJzubgdqug_4FUQTwEnjikeZmQVea6HQtmT2x-jqSJ-3OpMKxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید کلاینت اندروید GooseRelayVPN
🔹
این مخزن، کلاینت اندروید GooseRelayVPN است که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد.
🛠
پایداری و رفع کرش
‏
🌐
رفع کامل لو رفتن آی‌پی (IPv6 Leak) با موتور جدید tun2socks gVisor FakeDNS.
‏
🎛
پیاده‌سازی کامل Quick Settings Tile.
‏
📊
نمایش کاملاً دقیق سرعت و حجم مصرفی.
‏
🗂
اضافه شدن حالت Bypass به بخش Split-Tunneling.
‏
❄️
رفع فریز شدن برنامه در پس‌زمینه.
‏
📜
اصلاح پرش ناگهانی اسکرول لاگ‌ها و بازطراحی کارت وضعیت اتصال در صفحه Home
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/iaghapour/2628" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
رکورددار تاریکی دیجیتال: ایران طولانی‌ترین قطعی اینترنت جهان را تجربه می‌کند!
روزنامه معتبر اسپانیایی «ال‌پایس» در گزارشی تکان‌دهنده اعلام کرده است که ایران با گذشت حدود ۸۰ روز خاموشی دیجیتال، رکورد طولانی‌ترین قطعی سراسری اینترنت در تاریخ یک جامعه دیجیتال را به نام خود ثبت کرده است. این محدودیت‌ها که ابتدا با توجیه شرایط امنیتی و جنگی آغاز شد، همچنان ادامه دارد.
طبق گزارش این رسانه و به نقل از نت‌بلاکس، این وضعیت حالا حتی از قطعی طولانی‌مدت اینترنت میانمار در سال ۲۰۲۱ نیز فراتر رفته و زندگی میلیون‌ها ایرانی را در بن‌بست قرار داده است:
🔹
آوارگی برای یک اتصال پایدار:
ال‌پایس داستان تلخ افرادی را روایت می‌کند که برای حفظ شغل خود مجبور به مهاجرت موقت شده‌اند. مانند معلم زبانی که برای رهایی از اضطراب قطعی اینترنت، با هزینه ۴۰۰ دلار در ماه به زیرزمینی تاریک در ارمنستان پناه برده است.
🔸
ضربه مهلک به کسب‌وکارهای زنان:
تداوم این اختلالات، آسیب‌های ویرانگری به مشاغل کوچک وارد کرده است؛ به‌ویژه کسب‌وکارهایی که توسط زنان اداره می‌شوند و حیات آن‌ها کاملاً به پلتفرم‌های آنلاین و شبکه‌های اجتماعی گره خورده بود.
🔹
فلج شدن زندگی روزمره:
از کار از راه دور و تبادلات مالی گرفته تا ساده‌ترین ارتباطات انسانی و دسترسی به اطلاعات، همگی تحت تأثیر این محدودیت‌های بی‌سابقه مختل شده‌اند.
گزارش این روزنامه نشان می‌دهد که جهان در حال تماشای انزوای دیجیتال جامعه‌ای است که شهروندانش برای دسترسی به ابتدایی‌ترین حق ارتباطی خود، ناچارند هزینه‌های سنگین روانی، مالی و حتی مهاجرتی بپردازند./ دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/iaghapour/2627" target="_blank">📅 16:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpHTstF_auCoeT1p5vkYtpkg9hzjD3P0vJjABwnlbct1xmXnGqlkXlv55qg5LmJHoqSlQ2jdFOD3sEdjCeTwgy4Kb4-067PLWirPpSQIDeq9QCh2Hb3phNxdC24R-21cCcGn5pa2xbooDhd4L0mmCpGuVy4cpuch0UmJewvtyljBTA0voIa--E9BBiQDk8OrW-wqyUW4rCb9RSqgov4_RaMeiu2vi3ZXDc8OLosINQantJ51J5t-ZXApUfWUWpLNkg6H88GslIzfUuWx0OAkB7NXmX0La0nqIG19Me-ru1vbS3otiM5z1yL1bSvbc2z2Z1UbY4t1c0OB-Z1aFNKLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پروژه XPlex؛ راه‌حل هوشمندانه برای جلوگیری از قطعی و پکت‌لاس کانفیگ
اگر از کانفیگ‌های v2ray استفاده می‌کنید و پایداری اینترنت در کارهای حساسی مثل آزمون‌های آنلاین، جلسات ویدیویی یا ریموت‌ورک برای شما حیاتی است، پروژه جدید XPlex یک راه‌حل فنی و کاربردی برای شما دارد.
منطق این اسکریپت ساده اما بسیار کارآمد است و به شما کمک می‌کند تا یک اتصال بدون قطعی را تجربه کنید:
🔹
استفاده هم‌زمان از چند کانفیگ:
منطق کلیدی این پروژه این است که اگر چند کانفیگ v2ray داشته باشید، اسکریپت به صورت هم‌زمان از آن‌ها استفاده می‌کند و ترافیک شما را روی کانفیگی می‌اندازد که کمترین پینگ ممکن را دارد.
🔸
خداحافظی با پکت‌لاس و تایم‌اوت:
این ابزار برای افرادی که کارهای حساسی دارند و ثانیه‌ها برایشان مهم است طراحی شده؛ مثل شرکت‌کنندگان در آزمون‌های آیلتس آنلاین، جلسات کاری با خارج از کشور و...
🔹
هزینه مصرف حجم:
باید توجه داشته باشید که به دلیل ماهیت کارکرد این ابزار، مصرف ترافیک و حجم v2ray شما تقریباً دو برابر خواهد شد که بهای به دست آوردن یک اینترنت کاملاً پایدار است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/iaghapour/2625" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⭕️
نماینده مجلس: ۹۰ درصد مردم با قطعی اینترنت مشکلی ندارند!
علی یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس صراحتاً اعلام کرد که اینترنت جهانی فعلاً بازگشایی نخواهد شد و مسئولان به این نتیجه رسیده‌اند که اتصال مجدد آن به صلاح نیست. او مدعی شده که با پلتفرم‌های داخلی، احتیاجات اکثریت جامعه برآورده شده است!
این اظهارات نشان‌دهنده اصرار بر ادامه سیاست اینترنت طبقاتی و نادیده گرفتن نارضایتی‌های عمومی است:
🔹
انکار نارضایتی‌ها:
این نماینده مدعی است به عنوان نماینده مردم، مراجعات مکرری برای اعتراض به قطع اینترنت نداشته و ۹۰ درصد مردم هیچ مشکل عمده‌ای با این وضعیت ندارند!
🔸
رسمیت یافتن اینترنت پرو:
به گفته او، تا کنون به بالغ بر یک میلیون نفر از افرادِ واجد صلاحیت (مثل تجار و دانشگاهیان) دسترسی به «اینترنت پرو» داده شده و هر قشری که نیاز داشته باشد هم می‌تواند آن را پیگیری کند.
🔹
کوچ اجباری به پلتفرم‌های داخلی:
او مدعی شد که ترافیک شبکه‌ها نشان می‌دهد بیشتر کسب‌وکارها به پلتفرم‌هایی مثل روبیکا و سروش کوچ کرده‌اند و تنها یک «اقلیت ناچیز» باقی مانده‌اند که آن‌ها هم بستر مشخصی برای پیگیری دارند.
در حالی که مسئولان از پایداری وضعیت فعلی و رضایت مردم سخن می‌گویند، بخش بزرگی از جامعه، کسب‌وکارها و متخصصان، اینترنت طبقاتی و محدودیت‌های فراگیر را تلاشی برای حذف کامل دسترسی آزاد به دنیای دیجیتال می‌دانند. / زومیت
پ.ن: اینا نماینده کدوم مردم هستن؟ 90 درصد مشکل ندارن؟ عجب!
حالا فارق از اینکه این ادعا از اول تا آخر دروغ هستش ولی من قبلا هم خواهش کردم اگه مجبور نیستید وارد شبکه های داخلی نشید! اگه مجبور نیستید لطفا سیم‌کارت پرو نخرید! اینا واقعا فکر میکنن مردم به ایتا و بله علاقه دارن! متوجه نیستن خیلی ها به اجبار مهاجرت کردن! در غیر اینصورت کی این اپلیکیشن ها رو به تلگرام و اینستا ترجیح میده؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/iaghapour/2623" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔻
دوستان عزیزی که درخواست معرفی افراد معتبر برای خرید فیلترشکن دارید؛ طبق بررسی و نظرسنجی که در
این پست
قرار دادیم، با چندین نفری که از سال‌های قبل همکاری داشتیم صحبت کردیم و ازشون یکسری درخواست‌ها داشتیم؛ از جمله ضمانت بازگشت پول و اینکه مبلغی رو به عنوان ضمانت پیش ما بگذارند.
به همین دلیل ۹۰ درصدشون قبول نکردن و فقط تعداد محدودی پذیرفتن که هفته پیش یکی از اون‌ها رو بهتون معرفی کردیم. بازم اگه کسی از افراد قدیمی شرایط ما رو قبول کنه حتماً معرفی می‌کنیم.
افرادی که به ما تبلیغ می‌دن می‌دونن چقدر تو تبلیغات سخت‌گیر هستیم حالا در هر موضوعی باشه. بیش از ۳۰ درصد کسانی که پیام می‌دن، چون کانال قدیمی یا کاربر زیادی ندارن یا سایت معتبری ندارن، با نهایت احترام تبلیغشون رو اصلاً قبول نمی‌کنیم.
🔹
با این حال بازم سعی می‌کنیم همین یکی دو تا فردی که می‌شناسیم و شرایطمون رو قبول کردن بهتون معرفی کنیم؛ البته اگه خودشون دوباره قبول کنن تبلیغ بدن :)
ممنون میشم افراد جدید برای تبلیغات در زمینه فیلترشکن فعلاً پیام ندن. شرایط رو کامل در
این پست
براشون توضیح دادیم.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/iaghapour/2622" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭕️
اعتراف رسمی دولت: ۷۰ درصد مطالبات مردم، رفع محدودیت‌های اینترنت است
معاون اجرایی رئیس‌جمهور صراحتاً اعلام کرد که طبق نظرسنجی‌های نهاد ریاست‌جمهوری، بیش از ۷۰ درصد گلایه‌ها و خواسته‌های مردم به محدودیت‌های اینترنت مربوط می‌شود. او تأکید کرد که سیاست پایدار کشور نباید بر مبنای فیلترینگ باشد.
نکات کلیدی سخنان معاون رئیس‌جمهور درباره وضعیت اینترنت:
🔹
تصمیمات اضطراری باید تمام شوند:
محدودیت‌های اخیر به دلیل شرایط خاص امنیتی و جنگی بوده، اما تصمیمات دوران اضطرار نباید دائمی شوند و سیاست پایدار کشور نمی‌تواند بر محدودسازی بنا شود.
🔸
اعتراف به شکست فیلترینگ:
تجربه عملی نشان داد محدودیت‌های فراگیر ارتباطی به نتایج مورد انتظار منجر نشده و استفاده گسترده از فیلترشکن‌ها اثربخشی این محدودیت‌ها را از بین برده است.
🔹
حق آگاهی مردم:
اعتماد عمومی مهم‌ترین سرمایه است و مردم حق دارند بدانند محدودیت‌ها بر چه مبنایی اعمال می‌شود، چه دامنه‌ای دارد و تا چه زمانی ادامه خواهد داشت.
به گفته قائم‌پناه، کشور به یک تفاهم ملی در حوزه ارتباطات نیاز دارد؛ چرا که آینده ایران متصل و فناورانه است و دسترسی پایدار به اینترنت، پیش‌شرط تحقق این آینده خواهد بود./ زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/iaghapour/2621" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOiAaexsgTpk5URGs2JuHJ2_nKBgbaT1IylikBOfGIVLgVM6jT3l8RvCZLeK3ruSTO8vhIQEwuPsFS1be_ja9pd2xl22AcJMePz1CHh7oIWdH1fp58vM1fxXbGUzh1k5KAdTuXmZqcCUeQQ7OTdc4_mqx6e-BZcmPmY4-kweY9rU7ExQRIF7jsmggzQSGVpjxF01UD3N41S7bkUd3Buko9_rDfJ5OCCFu-TixQnoDVaXRBZ8PpcL16HocsGkLe_BzkdD5SqSUGf-pp4l6M3vjeecZW5GMY3r2bLyDbGhyJROWg0a7cJdE1RVEwGD4o2XN7hyJGBEm9NWQw1-U7_veQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
بحران خاموشی دیجیتال؛ ضربه‌ای جبران‌ناپذیر بر پیکر اقتصاد و جامعه
🔻
بیش از ۱۹۴۴ ساعت خاموشی دیجیتال، تنها قطع یک ابزار ارتباطی روزمره نیست، بلکه یک «بحران تمام‌عیار اقتصادی و اجتماعی» است. در زمانه‌ای که در سراسر جهان حتی چند دقیقه اختلال در اینترنت زیان‌های هنگفتی به بار می‌آورد، تداوم ۸۲ روزه این وضعیت در ایران، آسیبی عمیق به شریان‌های حیاتی کسب‌وکارها و زندگی عادی مردم وارد کرده است.
در واقع، تداوم این قطعی طولانی‌مدت نشان می‌دهد که حفظ حیات اقتصادی مشاغلِ وابسته به فضای مجازی و نیازهای ارتباطی جامعه، در اولویت تصمیم‌گیری‌ها قرار ندارد؛ رویکردی که پیامدی جز نابودی معیشت هزاران نفر، فرسایش سرمایه اجتماعی و آسیب جدی به بدنه نوپای اقتصاد دیجیتال کشور نخواهد داشت.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/iaghapour/2620" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjSIsna021tJGe7coH5I9f2_EMcvtyByj8vXPEP8poJDz6iWffX0FbxHcowz9uHlbFhT_-Af7nLnXpd6bI7btZGm15VXTHavJZ4qhFVxmirBFZMTiosh-NkSlgYgayd5C_6e0vqkUKJQN8dIrC8t1FaFEpwl2kOTdDNZKiEi0azr6boBHpXa7B7EQxHeB5ESk4JOQuzGJ0-WGyMh3e64G-MtwxeG8XPXsJ74s5SQPrVxzQhdK6IXpYfOtNi_Dh-5NyCkS1FYfxDrGOCV18INvbUeJLix64jQuEHu1mv6mt_kofitWmJ-jckbqYgmhX-oLTo0j5yVOq651AFYQwRuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شگفتی گوگل در Google I/O 2026؛ معرفی جمینای ۳.۵ فلش با سرعتی باورنکردنی!
در گام نخست، مدل جمینای ۳.۵ فلش عرضه شده است؛ مدلی که با وجود طراحی شدن برای سرعت بالا و هزینه کم، در کمال شگفتی توانسته مدل‌های پرچمدار و پرو نسل‌های قبل را در بنچمارک‌های تخصصی شکست دهد.
🔹
پادشاهی در بخش ایجنت‌ها:
این مدل با توانایی برنامه‌ریزی بالا، می‌تواند چندین ایجنت را به صورت موازی برای پیشبرد پروژه‌های پیچیده و کدنویسی مستقر کند.
🔸
سرعت خیره‌کننده و کاهش هزینه‌ها:
ساندار پیچای اعلام کرد این مدل با سرعت پردازش ۲۸۹ توکن در ثانیه، حدود ۴ برابر سریع‌تر از رقباست.
🔹
شکست رقبای سرسخت:
جمینای ۳.۵ فلش در آزمون‌های تخصصیِ مربوط به کارهای ایجنتی، امتیاز بی‌نظیر ۱۶۵۶ را کسب کرده و عملاً رقیب سرسختی مثل کلود سونیت ۴.۶ آنتروپیک را پشت سر گذاشته است.
🔸
همچنین نسخه قدرتمندتر یعنی جمینای ۳.۵ پرو در ماه ژوئن ۲۰۲۶ رسماً عرضه خواهد شد.
جمینای ۳.۵ فلش هم‌اکنون به عنوان مدل پیش‌فرض در اپلیکیشن جمینای و بخش سرچ گوگل فعال شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/iaghapour/2619" target="_blank">📅 09:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pN3yPWZ-daro5ScIOb7f4XOzUbg6MadlUqnFkWhToQEh5km0lYiKLc9gECxfdqPM1eYZk2vO1KeSGRoFuRa_UzuZcKrO7h2wDZPuixpK-Ev4AdwvUL9YArP3WZTCvgKAMophBEFwIt-iQyWRuzvtNxCzCpAhTTIUEq2skHviAQhCi2uBu4tpjUVj319idEeqTOkrf3NM-S78UB1w2iyJAhaX2VKhWMCtcm7hR56A6zBrZCPBK8NXer2S6SOODKYy4dJb-tsUbwlFRJ-NC4JCUb7DoEF9-qRV-rKTilRnDORA39F9lDjfW-sVXAFhS5OpeLHQkwaxjwqq6il99k6MzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دیگه پول فیلترشکن نده! آموزش ساخت فیلترشکن شخصی و رایگان با سرعت بالا
😎
🔹
در این آموزش قدم‌به‌قدم بهت یاد می‌دم که چطور بدون نیاز به دانش خاصی، یک فیلترشکن (VPN) شخصی، امن و کاملاً رایگان برای خودت بسازی. این روش روی تمام اینترنت‌ها جواب می‌ده و سرعت خوبی برای تماشای یوتیوب، وب‌گردی و … داره.
🔗
تماشا ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#رایگان
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/iaghapour/2618" target="_blank">📅 16:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">از هر 10 نفری که که تو اینستاگرام وصل هستن 8 تاش دختره, 2 تاش هم پسر کانفیگ فروش
🥸</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/iaghapour/2617" target="_blank">📅 17:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzRWFkuqUCt9ubuvs9drck7jcMYYXO557T4DYTsEGEnedeudhpQ1cpoxA7sUFgz0NhwQqW_0wNnYBBiPcHvZ37PdwI9bOv8HcPWOm6ODpH_VBOCBKPU2FdVzja0UEHE4mbu0gmVyeQwA3DwqFME7Vu2hpZ5hTp2qG6wD8Bccl-e0-QDDrH66VgVehj34b_YN0iMHdjd-cEx2v361x2aph0PJPd5g3PXYmidG1M4P8gx81W2Q7udFp960a8dX1BM-JTRShu1OwjvImwaDlXKEe3-wYxOWWxQwNXa-TGYRrw5PjM1HI4yQ0qahTMLUuzkJourmjyCTEOhLuMo4kf-_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش نصب ساده و آفلاین 3X-UI روی سرور ایران + SSL (+ معرفی قابلیت های جدید)
🔹
در این ویدیو به سراغ یکی از بزرگترین چالش‌های این روزها رفتیم: نصب پنل 3X-UI روی سرورهای ایران همراه با سرتیفیکیت به صورت کاملاً آفلاین و بدون نیاز به اینترنت آزاد! همینطور سعی کردیم یک معرفی ساده از قابلیت های جدید این پنل داشته باشیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#پنل
#xui
#3xui
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/iaghapour/2615" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">⭕️
بحران در زیرساخت فناوری؛ سقوط درآمدها و خطر عقب‌ماندگی ۱۰ ساله!
اختلالات اینترنتی دیگر فقط یک مشکل ساده برای کاربران عادی نیست؛ بلکه به گفته رئیس کمیسیون شبکه سازمان نصر، تیشه به ریشه‌ی زیرساخت‌های فناوری کشور زده است. این وضعیت نه تنها درآمد شرکت‌ها را تا ۷۰ درصد کاهش داده، بلکه باعث فرار متخصصان کلیدی و فرسودگی شدید تجهیزات شده است.
🔹
سقوط درآمد و انفجار هزینه‌ها: شرکت‌های حوزه شبکه با کاهش درآمد ۳۰ تا ۷۰ درصدی روبرو هستند. از سوی دیگر، به دلیل اختلال در مسیریابی و افت کیفیت، این شرکت‌ها مجبور به پرداخت جریمه‌های سنگین ناشی از نقض توافق‌نامه سطح خدمات (SLA) شده‌اند.
🔸
تهدید امنیت سایبری: محدودیت دسترسی به مخازن اصلی و سرورهای به‌روزرسانی جهانی، ریسک نفوذ و حملات سایبری را تا ۴۰ درصد افزایش داده است. در واقع، امنیت سایبری قربانی ناپایداری شبکه شده است.
🔹
تخلیه ژنتیکی تخصص: صنعت شبکه با بحران خروج نیروهای کلیدی مواجه است. تربیت یک متخصص ارشد سال‌ها زمان و هزینه‌ی ارزی سنگین می‌طلبد که با مهاجرت این افراد، سرمایه‌های انسانی چند میلیاردی کشور به راحتی از دست می‌رود.
🔸
عقب‌ماندگی ۱۰ ساله: ادامه این وضعیت، ایران را با شکاف تکنولوژیک ۱۰ ساله نسبت به کشورهای منطقه مواجه می‌کند؛ شکافی که در فضای پرشتاب فناوری، جبران آن تقریباً غیرممکن خواهد بود.
زیرساخت شبکه کشور به جای اتصال طبیعی به اینترنت جهانی، در حال حرکت به سمت یک ساختار جزیره‌ای و فرسوده است. اگر ثبات پیش‌بینی‌پذیر به این فضا بازنگردد، شرکت‌های بزرگ فناوری به اپراتورهای ساده تجهیزات قدیمی تنزل پیدا خواهند کرد. / دیجیاتو
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/iaghapour/2614" target="_blank">📅 10:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwK_gMGobPOsI1mtitTJH_7P6vabbrO8AtHfnGP1hkS5ovljX5J__byh88hz172sUn6AmzUVjxzJtw-0TI64lSGbiSi51SQ8yta-E1EetWLSQmuoyb3zzopuT99MR1i2C87LGqcklrpAen_pKre0-NLO_CY3fwVZEfdah80RmnQSHK8FGvBtXHp_oPU6BJSNA1TUofAr7jLRQ93GyHJk1HGa51SSY58KGh7wKFAo3IRWyr6yuQzAVu3InVVlKLJatGYNUE2X1WOp0cEBREk26IsI9iRS-bd5Smdpqhm1Jaw7fGlkcIaYC8zTvoVoSOf1xvTwIk8E7OTWOy_Nmug_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
حرف‌زدن درباره‌ی قطعی
#اینترنت
شاید فوری اینترنت را برنگرداند؛ اما
#سکوت
دقیقاً همان چیزی است که ادامه‌ی این وضعیت به آن نیاز دارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/iaghapour/2613" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2612" target="_blank">📅 17:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/iaghapour/2609" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است!
کاش تلگرام بیاد از شما یاد بگیره :)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/iaghapour/2608" target="_blank">📅 12:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">✍🏻
دوستان عزیز، همون‌طور که احتمالاً متوجه شدید، در یک هفته گذشته به دلایل مختلفی فعالیت ما کمتر شده.
🔹
در این مدت پیام‌های زیادی داشتیم که درخواست آموزش «روش جدید سنایی» رو داشتن. وقتی بررسی کردیم، متوجه شدیم خود ایشون زحمت تهیه ویدیوی آموزشی رو کشیدن؛ بنابراین نیازی به آموزش مجدد  نبود.
🔸
برای اطمینان بیشتر، این آموزش رو به چند نفر از دوستان دادیم تا تست کنن. بیشتر افراد موفق به اجرا نشدن، اما یکی از کاربران تونست متصل بشه. طبق بررسی‌های ایشون، این روش به‌شدت به رنج آی‌پی‌ها (هم سرور ایران و هم خارج) وابسته است. مشکل اصلی اینجاست که بعد از اتصال و مصرف حجم کمی از اینترنت، ارتباط قطع می‌شه و باید آی‌پی رو عوض کرد؛ هرچند آی‌پی قبلی بعد از ۱ تا ۲ ساعت دوباره قابل استفاده می‌شه.
🔻
متأسفانه در این بین، عده‌ای بدون این‌که تست درستی از پایداری تانل بگیرن، شروع به آموزش کردن که نتیجه‌اش فقط ضرر مالی برای کاربران بوده. چون کاربرا رفتن سرورهای گرون قیمت رو خریداری کردن که البته تعداد این افراد اصلا کم نبوده. (نمونه‌اش رو در عکس ضمیمه می‌بینید).
🟢
در مجموع، به نظر می‌رسه این روش هنوز پایدار نیست، اما از بچه‌های تیم خواستیم تست‌های بیشتری روش انجام بدن. اگر خودتون هم مایلید آموزش رو ببینید، می‌تونید مستقیماً به کانال یا گروه سنایی مراجعه کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/iaghapour/2607" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">⭕️
خلاصه اخبار چند روز گذشته
🔸
اینترنت بین‌الملل به گیمرها ارائه می‌شود؛
ثبت درخواست در سامانه همگرا (اینترنت طبقاتی)
🔹
دولت و مجلس به دنبال حمایت تازه از پیام‌رسان‌های داخلی (رانت و فساد جدید)
🔸
نماینده مردم تهران در مجلس:
درباره خسارت‌های قطعی اینترنت جوسازی می‌شود. (حرف بیخود)
🔹
معاون رئیس‌جمهور:
اینترنت بین‌الملل حتما وصل می‌شود؛ دولت قصد دائمی‌کردن محدودیت‌ها را ندارد. (حرف الکی)
🔸
برآورد انجمن بلاکچین: خسارت ۳۰۰ تا ۷۰۰ هزار میلیاردی از قطعی اینترنت.
🔹
معاون رئیس جمهور: محدودیت حجم و گرانی اینترنت پرو برای جلوگیری از استفاده غیرضروری است. (عجب بابا عجب)
🔸
قطع اینترنت به هفتاد و پنجمین روز خود رسید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/iaghapour/2606" target="_blank">📅 18:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdwW4t3UfPTq1k1qDSkqb0fw1BtKVWwRZTfpDhmljuCmfafpakFph7Wz1kmKn_FMVR5Y5Q19RDB2zzsBwmUgegzIJbtfpUjbMldkUcXwFHFX5vPexL2I0C5yYg_-kmiRJ8mcFKCF823i7QFSuPmIsa6FAgOexTFOcCsafcR1J0Um5AdYXWkOvT4wL7d2ZmubN-6xN8D33BQq1vHZ5paZ2dI3Af8MzJg8Ti-qZE8lrtwkg7fH4ZLkpQqP-8hQNQzVcED3wZu_Fvj7WYvsztufQwio_8QsfH6jYDdE1S4fUATcTwoQxDEZ6y7zY2kAgCe_BIsV0kvaMgQ3jIdPQoEB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
با اپ TunnelX در ویندوز از قابلیت Split Tunneling استفاده کنید.
🔹
اپ TunnelX برای زمانی ساخته شده که کاربر نمی‌خواهد تمام ترافیک سیستم از وی‌پی‌ان عبور کند. با این برنامه می‌توان فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگر را وارد تونل کرد و بقیه ترافیک سیستم را روی اینترنت عادی نگه داشت. همچنین در صورت نیاز، حالت Full-route برای عبور کل سیستم از تونل در دسترس است.
🔗
دانلود اپ از گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/iaghapour/2605" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✍
آدم راننده شوتی باشه به مراتب اضطرابش كمتر از کسیه كه شغلش تو ايران به اينترنت وابسته هستش...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/iaghapour/2603" target="_blank">📅 21:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚀
آپدیت بزرگ و انقلابی پنل 3x-ui (نسخه‌های 3.0.0 و 3.0.1)
بالاخره یکی از مهم‌ترین آپدیت‌های پنل محبوب 3x-ui منتشر شد! در این نسخه‌ها شاهد بازنویسی کامل رابط کاربری، اضافه شدن قابلیت‌های مدیریتی کلان و بهبودهای چشمگیر امنیتی هستیم.
🌐
۱. بازنویسی کامل و سریع‌تر شدن پنل (مهاجرت به Vue 3)
رابط کاربری از پایه بازنویسی شده است! این یعنی سرعت لود بسیار بالاتر، طراحی مدرن‌تر، صفحه لاگین جدید و بهبود چشمگیر تم دارک.
⚡️
۲. آمار زنده و در لحظه
: با جایگزینی سیستم قدیمی با
WebSocket
، از این پس تمام آمارهای داشبورد، مصرف حجم کلاینت‌ها و وضعیت سرور به صورت «زنده» آپدیت می‌شوند و دیگر نیازی به رفرش کردن صفحه نیست!
🌍
۳. مدیریت چند سروره (Multi-Node Deployment) -
🌟
ویژگی طلایی
یکی از مورد انتظارترین قابلیت‌ها اضافه شد! حالا می‌توانید از طریق یک پنل مرکزی (Manager)، کانفیگ‌ها و اینباندها را روی چندین سرور دیگر (Remote Nodes) مستقر و مدیریت کنید.
📱
۴. رابط کاربری کاملاً سازگار با موبایل
: داشبورد، لیست کلاینت‌ها و بخش لاگ‌ها حالا به صورت "کارتی" و کاملاً بهینه برای نمایشگرهای موبایل طراحی شده‌اند تا مدیریت پنل با گوشی بسیار راحت‌تر شود.
⚙️
۵. خداحافظی با کدهای JSON و تنظیمات آسان‌تر
فرم‌های ساخت کانفیگ (Inbounds) کاملاً ساختاریافته و گرافیکی شده‌اند. دیگر برای تنظیمات پایه نیازی به دستکاری JSON خام نیست (البته تب Advanced برای حرفه‌ای‌ها همچنان وجود دارد). همچنین مدیریت DNSها بسیار پیشرفته‌تر شده است.
👥
۶. مدیریت گروهی کلاینت‌ها (Bulk Actions)
امکان انتخاب گروهی  کلاینت‌ها برای حذف یا اعمال تغییرات اضافه شده که کار ادمین‌ها را بسیار راحت می‌کند.
🛠
۷. امکانات جدید Xray و Outboundها
اضافه شدن پروتکل Loopback، دکمه
Test All
برای تست همزمان همه Outboundها و ارائه گزارش دقیق از تایم‌اوت‌ها، و همچنین خاموش شدن امن هسته Xray.
🔒
۸. ارتقاء امنیت و نصب راحت‌تر
➖
اضافه شدن سیستم امنیتی CSRF Protection برای جلوگیری از حملات.
➖
اضافه شدن گزینه
skip-SSL
در اسکریپت نصب (بسیار کاربردی برای کسانی که از ریورس‌پروکسی یا تانل استفاده می‌کنند و نیازی به سرتیفیکیت روی خود سرور ندارند).
➖
اضافه شدن صفحه مستندات API (API Docs) در داخل خود پنل برای برنامه‌نویسان.
و بسیاری از تغییرات دیگه که میتونید در
این لینک
مطالعه کنید.
💡
نکته:
برای تجربه این تغییرات فوق‌العاده، پیشنهاد می‌شود هرچه سریع‌تر پنل خود را آپدیت کنید. (توصیه همیشگی: قبل از آپدیت بکاپ فراموش نشود!)
✍🏻
با تشکر از ثنایی عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/iaghapour/2602" target="_blank">📅 18:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">⭕️
عصبانیت سخنگوی دولت از انتقاد خبرنگاران از قطع اینترنت
فاطمه مهاجرانی در نشست خبری امروز خود به اعتراض خبرنگاران بابت ادامه قطعی اینترنت واکنش نشان داد.
سخنگوی دولت گفت: «در شرایطی که رئیس جمهور آمریکا اعلام می‌کند آتش بس به دستگاه تنفس مصنوعی وصل است، پاسخ شما چیست؟ کشور در جنگ است. بپذیریم که ویژگی جنگ، امنیت مردم است.»
✍🏻
پ.ن:  خانم مهاجرانی اگه دوباره عصبی نمیشید خواستم بگم کاش به فکر امنیت اقتصادی مردم هم بودید! کاش به فکر امنیت ذهنی و روانی مردم هم بودید! کاش یه فکری برای چند میلیون آدمی که با قطعی اینترنت بیکار و ناامید کردین هم بودید!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/iaghapour/2601" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
نمیتونم خبر رو تایید کنم ولی میگن:
— افغانستان اینترنت 5G آورده.
— عراق تلگرام رو رفع فیلتر کرده.
— سوریه هم که ویزا و مستر کارت و...
این که ما درگیر فیلترینگ مسخره هستیم واقعا گریه داره...</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/iaghapour/2600" target="_blank">📅 09:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سلام خواستم یه نکته کوچولو بگم
فقط بحث کسب و کارهای کوچیک نبود
فقط بحث آنلاین شاپ ها نبود
ماهایی که ۴ سال تو دیجیتال مارکتینگ بودیم توی طراحی سایت و سئو و اتوماسیون کار میکردیم هم کاملا ورشکست شدیم
نه از ۹ اسفند
ما یه بار جنگ خرداد زمین خوردیم تا اومدیم بلند شیم از جامون و داشتیم اوکی میشدیم دلار دی ماه سر به فلک کشید و بعد یه قطعی دیگه داشتیم که خیلی ها بهانه کردن و پول ندادن آخر دی ما هیچی پروژه نداشتیم حتی بهترین کارفرماها اومدن گفتن کار شما خیلی خوبه ولی ما واقعا پول پرسنل رو هم به زور میدیم نمیرسه به سئو
بهمن اومدیم خودمون رو جمع کنیم تیر آخر رو اول اسفند بهمون زدن
دفترمون رو تحویل دادیم
نیروهامونو از بهمن تعدیل کرده بودیم
و الان چه جوون ها و چه پدرانی که بیکار شدن
منی که تمام تخصصم همیناست
یک متخصص بیکار محسوب میشم.
©️
پیام ارسالی از کاربر shafikhany</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/iaghapour/2599" target="_blank">📅 01:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✍
حدودا 500 پیام بررسی نشده از 2 روز پیش داریم که پشتیبانی تا فردا همه رو بررسی میکنه.
جدا از بحث بالا، از ته دل آرزو میکنم تو این روزهای عجیب و غریبی که داریم می‌گذرونیم، حال دلتون خوب باشه. می‌بینیم و حس میکنم که زندگی چقدر برای خیلی‌ها سخت شده و دغدغه‌ها چقدر زیادن.
امیدواریم هرچه زودتر این روزهای سخت جاشون رو به روزهای روشن‌تری بدن. هوای خودتون و دلتون رو داشته باشید.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/iaghapour/2598" target="_blank">📅 03:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRdPhWUKQDrqLTTBkrQhD8ApW7VVUjJO2_6lSdKkPeCvcc8Rk3XY82m_sZUh8kTIeB8ZbLZhepf0AOZHO_ezGlakC4OIAw28DAuc2CkQGmGP3KB4i6aULfuH5A_cxqO_lzDy9QwMMu8qduLvnE33R94Dr4jlzspCEHBcql3VvA2Sm-Osl1XKaKTZy-lcYfuTznoDUtJUbnmHdFMJOvs4wG4uooFDRjm_kerrzG4296y3nZIfHGNxEwUrSsGMWc6FieIyq9epAJ0y6IgJAgpSFt1MvZnfajIod3xZovTVv8_ekMQhV9RoZ8IyY7IawdDmeRWphELkvu7Up2HgQJ8myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت ورژن 0.10.0 سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور ایران خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
توی آپدیت جدید سانگبرد با فعال کردن قابلیت Remote channel، میتونید پست هایی که تو یک چنل تلگرام ارسال میشه رو، به یک چنل توی سرور سانگبرد خودتون استریم کنید.
-
📡
قابلیت Remote channel
-
🔗
ساده سازی سیستم Invite link
-
🎨
بازطراحی بخش ساخت/تغییر کانال و گروه در UI
-
✨
انیمیشن build-up پیام ها در چت ها
-
🔔
بهبود عملکرد push notifications
- تغییرات گرافیکی اسکریپت نصب آسان
-
🐳
پشتیانی از TLS با سرتیفیکیت self-signed در Docker
-
🔧
رفع باگ های گزارش شده
-
📄
اضافه شدن نسخه فارسی فایل readme
🔘
اگه به هر مشکلی خوردین، حتما تو گیت هاب یک issue باز کنید و گزارش بدید.
⭐️
اگه از پروژه راضی بودین، با ستاره دادن تو گیت هاب از پروژه حمایت کنید.
🔹
چنل پروژه
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/iaghapour/2597" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
ساده‌ترین راه برای دور زدن فیلترینگ با تانل DNS
اگه خانواده‌ شما هم داخل ایران برای اتصال به اینترنت مشکل دارند، این پیام ممکن است به شما کمک کند.
این برنامه یک برنامه‌ی  گرافیکیست که کار با آن بسیار ساده است و برای اتصال به اینترنت هر دو روش MasterDNS و VayDNS را پشتیبانی می‌کند.
👈
لینک گیت‌هاب
👈
دانلود
اپ
📖
آموزش کامل MasterDNS و VayDNS
▶️
آموزش روی یوتیوب
📱
آموزش KevinNet DNS
▶️
آموزش روی یوتیوب
🔄
آپدیت‌های جدید برنامه
در صورت وجود هرگونه مشکل یا سوالات مرتبط با KevinNetDNS میتوانید با آدرس ایمیل زیر در تماس باشید:
©️
متن تهیه شده توسط نویسنده اسکریپت KevinDNS
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/iaghapour/2596" target="_blank">📅 23:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">⭕️
ادعای عجیب نماینده مجلس: با ۴ هزار میلیارد تومان ایتا را به سطح واتس‌اپ می‌رسانیم!
رئیس کمیته ICT مجلس در اظهارنظری جنجالی مدعی شده است که فاصله میان پیام‌رسان‌های داخلی مثل ایتا با نمونه‌های جهانی مانند واتس‌اپ، تنها در کمبود بودجه برای خرید سرور خلاصه می‌شود. به گفته او، ارتقای این پلتفرم‌ها هزینه چندانی برای کشور ندارد.
این نماینده مجلس معتقد است که پلتفرم‌های داخلی از نظر فنی کمبودی ندارند و تنها زیرساخت‌های سخت‌افزاری آن‌ها باید تقویت شود:
🔹
بودجه برای رقابت:
مصطفی طاهری مدعی است با صرف ۳ تا ۴ هزار میلیارد تومان برای خرید سرور، می‌توان کیفیت ایتا را به سطح واتس‌اپ رساند تا توانایی پذیرش بدون مشکل بیش از ۲۰ میلیون کاربر را داشته باشد.
🔸
هشدار درباره جاسوسی سخت‌افزاری:
این مقام مسئول همچنین به موضوع استفاده از بیگ‌دیتا (داده‌های بزرگ) اشاره کرده و مدعی شده که آمریکا قوانینی برای جاسوسی در لایه‌های سخت‌افزاری و تراشه‌ها (حتی پایین‌تر از سطح سیستم‌عامل) دارد.
این اظهارات در حالی مطرح می‌شود که کارشناسان حوزه تکنولوژی، موفقیت پلتفرم‌های جهانی را فراتر از صرفا تعداد سرور می‌دانند و مواردی چون امنیت، پروتکل‌های رمزنگاری، حریم خصوصی و نوآوری‌های مداوم نرم‌افزاری را از عوامل اصلی برتری آن‌ها به حساب می‌آورند.
یکی از کاربرا زیر همین پست در دیجیاتو کامنت جالبی گذاشته بود:
مامان‌بزرگ منم با چند میلیارد نیکی میناژ میشه!
پ.ن: حالا فارق از این حرفا داره میگه اینا دارن از کاربراشون جاسوسی میکنن برای همین ما باید اپ های خودمون رو داشته باشیم... من حرفی ندارم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/iaghapour/2595" target="_blank">📅 18:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiKETZ191dbXqhhvTFSdtmiBMC5UdsD0VWZPFfhLfRbdPUeWWMBKTNZr8dMfwKuC5xQ8Q9nzxDyN4-Aa8-cjgDn_Kl44o44Ufw2jrCvE0Dh11rM2eZQnKnuNm5XEz4qZLr2RoI1M0KmEba8ATNKwPyh0Edzr18Giy8h6n3O3ggvqCiNuhBqHcqN_PrHwBJEu1hGT6I8m3yHz5WBWUmdCRcwtk_F8yW_l1OL1LVOASUpR0-VrxU0OIlOWdA6yP3iK-FnAxWkFsyDYuhY_yROJq4QMllhW3Y2EU30hHzW8Ft-GuK3IS_I5taT1N4COg7em5vr038RBJ8Qz58WkMWgljw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ایران 11 هفته در خاموشی دیجیتال!
هیچ‌وقت تو زندگیم فکر نمی‌کردم یه روزی برسه که این‌جوری تلخ، شاهد از بین رفتن زحمت‌ آدما باشم. ۱۱ هفته قطعی اینترنت واسه خیلی‌ها فقط یه اختلال ساده نبود؛ قصه پدر مادرا و جووناییه که با هزار امید یه کسب‌وکار کوچیک راه انداخته بودن تا خرج زندگیشونو دربیارن و الان دستشون به هیچ‌جا بند نیست.
تا همین چند وقت پیش با کلی استرس می‌گفتیم کسب‌وکارهای نوپا و خونگی تو «مرز نابودی» هستن و همه‌مون چشم‌انتظار بودیم زودتر اینترنت وصل بشه؛ ولی الان دیگه حرف از مرز نیست. خیلی‌ها کل سرمایه، جوونی و حاصل سال‌ها تلاششون جلوی چشماشون دود شد و رفت رو هوا. کاش دردی که افتاده رو دوش این مردم، میافتاد رو دوش مسئولین...
🆔
@NetProPlus</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2594" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">#فیلترینگ
به ما تحمیل شد,
ولی
#اینترنت_طبقاتی
رو شما باید درخواست بدی تا بهت بدن...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/iaghapour/2592" target="_blank">📅 18:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFy_QUx7yp2T9NpxRpo3J4E9odQk4oD6uZL0hjk860WKlRTF0OF4SCoPIeUnMlXmrSNh11YTz_52fYhz6572zd5rlPD-lcAqaQ6lvbj_Vw1HJwn_K1NyQ5sqsBViK_4LK3hl0h77HOxm54kNW2FJ90amXpqfQ0con4eTTESH44WestCbxIOq15-CF_xKnWUYETOzPraxxsVbw4pw_3UK4Srq8UHvzcdXCU3RqNQVsyq757kRklNCDT4wFbixaHmVbs_z6c9Cx-jeV8DKMROcxMhpA-ZsqLQvZOYm5ZCHC2KV1wFONuu-7XkBSpdNTo1mGueKDi4jTuWtNAwI4ay6OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ تلگرام: ورود دستیار هوشمند به پروفایل شخصی!
تلگرام در آپدیت جدید تمرکز ویژه‌ای روی هوش مصنوعی داشته است. در ادامه مهم‌ترین تغییرات این نسخه را مرور می‌کنیم:
🔹
ربات‌های مهمان:
فراخوانی ربات‌ها در هر چت یا گروهی، تنها با تگ کردن آیدی و بدون نیاز به افزودن آن‌ها.
🔸
منشی شخصی هوشمند:
قابلیت اتصال مستقیم یک ربات به پروفایل شخصی تا در غیاب شما به پیام‌ها پاسخ دهد!
🔹
تعاملات زنده هوش مصنوعی:
تایپ و نمایش لحظه‌ای پاسخ ربات‌ها، به همراه قابلیت جدید ارتباط ربات با ربات برای انجام وظایف پیچیده‌تر.
🔸
امکانات جدید برای کانال‌ها و تولید محتوا:
قابلیت محدود کردن نظرسنجی‌ها (بر اساس کشور یا عضویت در کانال)، مشاهده نمودار آرا، و همچنین ساخت استایل‌های متنی سفارشی.
🔹
اضافه شدن قابلیت انتخاب فونت از سیستم خودتون (میتونید فونت وزیر رو نصب کنید و استفاده کنید).
با این به‌روزرسانی که شامل جستجوی هوشمند ایموجی‌ها، ارسال بی‌صدای پیام زمان‌بندی‌شده و رفع ۲۰۰ باگ فنی است، تلگرام قدم بزرگی برای ادغام کامل پیام‌رسانی انسان و هوش مصنوعی برداشته است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/iaghapour/2591" target="_blank">📅 14:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔻
مومن‌نسب: فضای مجازی به هیچ وجه نباید به حالت قبل برگردد
حالا این آدم انقدر مهم نیست که دربارش صحبت کنیم ولی خواستم بگم این همون آدمیه که چندسال پیش تو صداوسیما میگفت من خطرات اینترنت رو میدونم و اطلاع دارم یک نفر با 2 گیگ اینترنت حامله شده و پدر دختره با گریه اینو برای من تعریف می‌کرد...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/iaghapour/2590" target="_blank">📅 11:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
اطلاعیه مهم: معرفی فروشندگان کانفیگ
طبق نتایج
نظرسنجی اخیر،
قصد داریم فروشندگان قدیمی و معتبری که از قبل می‌شناسیم را یکی‌یکی برای خرید به شما معرفی کنیم.
📌
قوانین و شرایط مربوط به فروشندگان:
—
عدم پذیرش فروشنده جدید:
در حال حاضر شخص جدیدی معرفی نمی‌شود؛ بنابراین لطفاً در قسمت
«تماس با ما»
برای معرفی خود پیام ندهید. افرادی که معرفی می‌شوند، همگی پیش‌تر در کانال ما سابقه تبلیغ داشته‌اند.
—
تضمین خرید شما:
مبلغی از پول این افراد نزد ما به عنوان امانت می‌ماند تا در صورت بروز هرگونه مشکل، بتوانیم مطالبات شما کاربران عزیز را پیگیری کنیم.
—
ضمانت بازگشت وجه:
این فروشندگان موظف‌اند در صورت لزوم (بسته به شرایطی که خودشان به شما اعلام می‌کنند)، بین ۴۸ تا ۷۲ ساعت امکان عودت وجه را فراهم کنند.
—
قیمت منصفانه:
تمامی این افراد تعهد داده‌اند که نسبت به شرایط بازار، قیمت‌های منصفانه‌تری برای کاربران کانال ما در نظر بگیرند.
— معرفی فروشندگان صرفاً در زمینه
فروش کانفیگ
انجام می‌شود. هیچ‌یک از فروشندگان معرفی‌شده مجاز نیستند پس از معرفی، در کانال شخصی خود تبلیغات مربوط به "
اوتباند
" قرار دهند و یا به کاربران پیشنهاد خرید آن را بدهند.
⚠️
نکات مهم برای کاربران عزیز:
—
انتظارات از کیفیت:
کانفیگ‌ها باید بتوانند تلگرام، اینستاگرام و یوتیوب را به راحتی باز کنند. با توجه به شرایط فعلی اینترنت، داشتن سرعت‌های بسیار بالایِ گذشته کمی دور از انتظار است (هرچند ممکن است کیفیت سرویس‌ها عالی باشد)، پس لطفاً واقع‌بین باشید.
—
اختلال و پشتیبانی:
ممکن است در طول هفته، گاهی با اختلال مواجه شوید. پشتیبان‌ها موظف‌اند در سریع‌ترین زمان ممکن مشکل را حل کنند؛ اما لطفاً صبور باشید، حداقل یک ساعت به آن‌ها فرصت دهید و از ایجاد فشار زودهنگام به پشتیبانی کانال‌ها خودداری کنید.
— در ضمن، توجه داشته باشید که
ما ذی‌نفع این کانال‌ها نیستیم
و فقط به دلیل درخواست‌های زیاد شما این دوستان را معرفی می‌کنیم.</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/iaghapour/2589" target="_blank">📅 23:36 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ra8T6JLcFlglIuti4sKB7k6TpagiuN66gysEtU9QvRaKqpxMzjCH4BBNj85DCW0C7dQ9EisqkRaGybSygUmMfX9-Dmn19gLoadZFv63FQvL1K05WqkQ37a-0FrxUQE-ybs1VgLYuh3PiEw1o6Qc3fXh0kTVzCv1364JJ6bNMfjE9xAyw2Y6Kg4eoIqsskvJjAu4TbztNm7HhqgBfVzr2XDmYuF_cBBoqH7XsUKiCRTYQdsy_2kP8mdnSLmX1qQGQlC_d4n1QUzm7rJVj0-bvBnbYAjK_8VZDt2crXJnlVCJwJpkIUi6Sck-ZBx_ZRtPH_63c_IAcOODH4BEGZ-rp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
سخنگو وزارت خارجه حذف تیک آبی خود در شبکه X را (سرکوب حقیقت) خواند.
68 روزه اینترنت مردم ایران رو قطع کردن، بعد یه تیک آبی‌شو گرفتن میگه حقیقت سرکوب شد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/iaghapour/2588" target="_blank">📅 20:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔻
تسنیم: درآمد طرح اینترنت «پرو» در سال به ۹۶ هزار میلیارد تومن می‌رسه!
🔹
خب با این رقم‌های نجومی و پول هنگفتی که درمیاد، معلومه که از این تبعیضی که راه انداختن حسابی راضی‌ان. وقتی محدودیت و فیلترینگ این‌قدر براشون سود داره، چرا نباید اینترنت داخلی و بسته رو بیشتر تحویل بگیرن؟
🔸
این وسط یه تشکر ویژه و خسته نباشید هم باید بگیم به اون دسته از دوستانی که رفتن تو صف اینترنت پرو و این سیستم طبقاتی رو خیلی راحت پذیرفتن. از رئیس فلان اتحادیه و مدیر فلان اداره بگیر تا نماینده صنف لاستیک‌فروش‌ها و یه سری کسب‌وکارهایی که واقعاً بدون اینترنت آزاد هم کارشون لنگ نمی‌موند. تو شرایطی که ۹۹ درصد مردم هیچ دسترسیِ عادی به اینترنت آزاد ندارن، مرسی از شماها که رفتین این اینترنت رو گرفتین و با این کارتون، قشنگ به این تبعیض و نابرابری رسمیت دادین!
پ.ن: البته به این نکته هم توجه کنید که خبرگذاری داخلی اینو گفته و ممکنه دقیقا مقصودشون از این حرف هم همین باشه که بگن چقدر این طرح خوب و سودآور هستش و...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/iaghapour/2587" target="_blank">📅 14:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
وعده بازگشت به وضعیت عادی؛ توجیه محدودیت‌ها یا امید به بهبود اینترنت؟
معاون ارتباطات دفتر رئیس‌جمهور به تازگی اعلام کرده که وضعیت فعلی اینترنت مورد تایید دولت نیست و رئیس‌جمهور، محمدرضا عارف را مامور ساماندهی این شرایط کرده است. به گفته او، این محدودیت‌های شدید و قطعی‌ها صرفا تصمیماتی از سوی شورای عالی امنیت ملی و به دلیل شرایط خاص امنیتی و جنگی بوده‌اند.
🔹
وعده روزهای بهتر:
این مقام مسئول قول داده که با عبور از این شرایط ویژه، اینترنت نه تنها به حالت قبل برمی‌گردد، بلکه وضعیتی بهتر از گذشته پیدا خواهد کرد و وعده‌های انتخاباتی رئیس‌جمهور در این زمینه همچنان پیگیری می‌شوند.
🔸
دفاع از اینترنت پرو:
در واکنش به انتقادات، دولت ادعا می‌کند طرح «اینترنت پرو» صرفا برای نجات کسب‌وکارها در روزهای محدودیت ایجاد شده و نباید به آن برچسب اینترنت طبقاتی زد؛ چرا که به گفته آن‌ها، در شرایط عادی اصلا نیازی به چنین طرحی نخواهد بود.
🔹
کاهش محدودیت‌های عمومی:
خبر دیگر این است که قرار شده تدابیر جدیدی برای دسترسی بهتر سایر شهروندان به اینترنت اتخاذ شود تا فشار محدودیت‌های فعلی روی مردم کاهش یابد.
در حالی که دولت تلاش می‌کند قطعی‌ها و طرح‌های بحث‌برانگیزی مثل اینترنت پرو را صرفا به شرایط اضطراری گره بزند، کاربران و کسب‌وکارها همچنان منتظرند تا ببینند آیا این وعده‌ها در عمل به یک اینترنت آزاد و بدون محدودیت ختم می‌شود یا صرفا وعده‌ای برای کنترل نارضایتی‌های فعلی است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/iaghapour/2585" target="_blank">📅 21:12 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">⭕️
ایده عجیب در مجلس: تاسیس «اینستاگرام دولتی» و مدیریت کامل اینترنت!
نمایندگان مجلس در تازه‌ترین نشست خود با وزیر ارتباطات، از طرح‌ها و نگاه‌های جدیدی برای کنترل بیشتر فضای مجازی پرده برداشتند. در این جلسه، پیشنهاد ایجاد یک پلتفرم کاملا دولتی مشابه اینستاگرام مطرح شد تا به زعم آن‌ها، نیاز کشور برطرف شود.
🔹
اینستاگرام دولتی:
یکی از نمایندگان با اشاره به بازار سیاه و چند میلیونی فیلترشکن‌ها، رسما پیشنهاد ساخت یک سکوی دولتی شبیه اینستاگرام را برای پر کردن جای خالی این پلتفرم ارائه داده است.
🔸
رویای مدیریت اینترنت:
نایب رئیس مجلس تاکید کرده که مشکل آن‌ها اصل اینترنت نیست، بلکه می‌خواهند در صحنه بین‌المللی، مدیریت اینترنت کاملا در دست خودشان باشد و این فضا را به یک جبهه تقابل تشبیه کرده است.
🔹
فرصت‌سازی از بحران:
بخش قابل توجهی از صحبت‌های نمایندگان، حسرت خوردن برای از دست رفتن فرصت در شرایط ملتهب و جنگی است؛ آن‌ها معتقدند باید از این شرایط استفاده می‌کردند تا مردم و کسب‌وکارها به اجبار به سمت سکوهای داخلی کوچ کنند.
این صحبت‌ها به وضوح نشان می‌دهد که دغدغه اصلی، کاهش نارضایتی مردم از قیمت و کیفیت اینترنت نیست؛ بلکه تلاش برای بومی‌سازی اجباری، قطع ارتباط با شبکه‌های اجتماعی بین‌المللی و کشاندن کاربران به پلتفرم‌های تحت کنترل و نظارت است. / زومیت
✍🏻
پ.ن: از سوپر اپلیکیشن های ایتا و سروش و گپ و بله که از تلگرام کپی کردین مشخصه توانایی اینکار رو دارید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/iaghapour/2584" target="_blank">📅 19:36 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">⭕️
مرگ خاموش اقتصاد خرد: نابودی ۴۰ درصد از کسب‌وکارهای اینستاگرامی!
قطعی‌ها و محدودیت‌های اینترنتی فقط حق دسترسی آزاد ما به شبکه‌های اجتماعی را سلب نکرده، بلکه تیشه به ریشه‌ی اقتصاد خرد و معیشت مردم زده است. طبق اعلام پشوتن پورپزشک، عضو هیئت‌مدیره اتحادیه کسب‌وکارهای مجازی، فیلترینگ و اختلالات باعث نابودی بخش عظیمی از مشاغل آنلاین شده است.
🔹
فاجعه‌ی آماری: نزدیک به ۴۰ درصد از کسب‌وکارهای اینستاگرامی برای همیشه از بین رفته‌اند؛ این یعنی مرگ مستقیم بیش از ۴۰۰ هزار شغل!
🔸
دومینوی ویرانی: وقتی شوکی مثل محدودیت اینترنت وارد می‌شود، ابتدا کسب‌وکارهای کوچک و آسیب‌پذیر می‌میرند، اما این نابودی با کمی تاخیر گریبان شرکت‌های بزرگ اقتصادی را هم خواهد گرفت.
🔹
زنجیره‌ی به هم پیوسته: کسب‌وکارهای بزرگ در تولید، تامین و توزیع به شدت به همین کسب‌وکارهای خرد وابسته‌اند. توهم مصونیت برای شرکت‌های بزرگ، در نهایت منجر به فروپاشی خود آن‌ها می‌شود. منبع: زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/iaghapour/2583" target="_blank">📅 19:29 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسم این زندگــــــی نبود
یک مبارزه تمام عیار بود...
#جوانی
#زندگی
#جنگ
#اینترنت</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/iaghapour/2581" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭕️
حل مشکل دانلود از ریلیز گیت‌هاب با LatestReleaseMirror
اگر در دانلود فایل‌ها از بخش ریلیزهای (Releases) گیت‌هاب به دلیل محدودیت‌های اینترنت مشکل دارید، این اسکریپت کاربردی دقیقاً برای شما ساخته شده است!
ابزار
LatestReleaseMirror
به صورت خودکار فایل‌های آخرین آپدیتِ ریپازیتوری‌های دلخواه شما را دریافت کرده و آن‌ها را به عنوان فایل‌های عادی در ساختار پوشه‌های گیت‌هاب ذخیره می‌کند؛ در نتیجه می‌توانید آن‌ها را به راحتی و حتی با اینترنت داخلی دانلود کنید.
🔹
دریافت و آپدیت خودکار آخرین نسخه با استفاده از GitHub Actions.
🔸
امکان فیلتر کردن فایل‌های مورد نیاز (مثلاً فقط نسخه‌های ویندوز یا اندروید)
🔹
دسته‌بندی تمیز فایل‌های خروجی در مسیرهای مشخص.
🔗
لینک ریپازیتوری و راهنمای استفاده
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/iaghapour/2580" target="_blank">📅 16:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ركورد جديد سرعت اينترنت ژاپن:
با سرعت 1.02 پتابيت بر ثانيه، كل نتفليكس را در 1 ثانيه دانلود مى‌كند.
✍
ما هم اینجا باید با DNStt وصل بشیم تا بزور بتونیم فقط این خبر رو بخونیم...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/iaghapour/2579" target="_blank">📅 13:56 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
اسکریپت بهینه شده XHTTP Relay ECO برای Vercel Pro
🔹
نسخه ECO طوری تیون شده که علاوه بر امنیت سفت‌وسخت v1.3، کم‌هزینه‌ترین رفتار ممکن روی Vercel Pro رو داشته باشه؛ یعنی با کنترل هوشمند Timeout، Inflight، Throttle و Logها، مصرف منابع و هزینه نهایی تا جای ممکن پایین نگه داشته میشه.
🔸
فقط با GET، HEAD و POST کار می‌کنه تا امنیت بالاتر بره.
🔹
احراز هویت فقط از طریق هدر x-relay-key انجام میشه
🔸
هدرهای اضافی پلتفرم و hop-by-hop رو بی‌رحمانه فیلتر می‌کنیم.
🔹
روی آپلود و دانلود محدودیت سرعت (Throttling) واقعی گذاشتیم.
🔸
بردیمش روی Node runtime با لیمیت ۱۲۸ مگابایت رم و مدیریت کانکشن‌های همزمان.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/iaghapour/2578" target="_blank">📅 22:28 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭕️
ورژن جدید کلاینت اندروید GooseRelayVPN منتشر شد
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
هسته پروژه به ورژن 1.5.0 آپدیت شد.
🔸
قابلیت fake dns اضافه شد.
🔹
باگ ها در این نسخه برطرف شدن.
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/iaghapour/2577" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ueu4ejr_wH0l6OicJsqXOwdcgdeWnN2U4M7RSU4cHTK8ifLySLK99egeb11l8_z5wVBeRM7eoLgEtIsU9Lo40ly3uXOJnzXYfXsbHf5LnIGrujnk3iKZYDBdqpivifu4DSi5qZIFAERBVyVtscCr1A2BNs4pQndVCfPstW0qrCjlSKPWbg5VNz6_uiLfQBGrI3z_T3ewuFbPBWbKx99T1k7uc1DGD_ZKaS0ou8R-p6i-_erY3Vk48e5AplSPsh1tEKVBwyB7ZsZoauOvhhfqvZsLsUGplG5WxtkWErhJBQ_ZLQMCwwMuSVQmNawA-EgbPNu-hO3hYNOw4GFkhj-Znw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن رایگان و شخصی به 2 روش با نت ملی
🔹
با استفاده از دو ابزار قدرتمند MHRV و Nova-Proxy، دیگه نیازی به خرید کانفیگ‌ها و سرورهای گرون‌قیمت ندارید. تو این آموزش قدم‌به‌قدم به ۲ روش مختلف پیش میریم تا بتونید یه اتصال پایدار و بدون قطعی داشته باشید. حتماً تا آخر ویدیو همراه من باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔹
دانلود کلاینت ویندوز
🔸
دانلود کلاینت اندروید
#آموزش
#فیلترشکن
#mhrv
#novaproxy
#رایگان
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/iaghapour/2576" target="_blank">📅 19:53 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gtn2UBrr_6vRyru-U5dCju_KTbmalAJfx5gzMpIEFdcbjJFGcfWRX791vFTpR7WuoxWBYSC152SPmxo8kd37nSI5lk838_Zw0GqhEDMn2HTu-v3cC9maXLlhnGRdDnEwzkeAL-M5ElzxDYwYU3gWGj1u71PvIIf2F-Mo3yYZKjgsZdWNk1GHyapKfbAjQD_43GIiRR0aiGWrugLvXYZ4LjTck8dcy6zAa2WsJbdkxGpUspeCmmsEN5iY24iI83aUL5c2Akfykcn_tQxkALSd4S_C7z85VQx7pnqO9EQn7JFL4LNFLiqhOJ3e0FEYOEFzdus1GutARZYOw47864n2ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پشت‌پرده‌ی «اینترنت پرو»؛ امتیاز ویژه یا تله‌ی نظارتی؟
این روزها سیم‌کارت‌های بدون فیلتر با نام «اینترنت پرو» در ازای دریافت هزینه و ثبت کامل مشخصات هویتی به فروش می‌رسند. اما هدف اصلی این طرح، دلسوزی برای نیاز اینترنتی اقشار مختلف نیست.
هدف اصلی و پنهان این ماجرا، چیزی جز «تشخیص هویت دقیق و رصد لحظه‌ایِ کاربر» نیست.
👁‍🗨
وقتی اینترنت آزاد را مستقیماً با نام و کد ملی خودتان دریافت می‌کنید دقیقاً چه اتفاقی می‌افتد؟
🔹
پایان گمنامی:
تمام سایت‌هایی که سر می‌زنید و محتوایی که می‌بینید، مستقیماً و شفاف روی نام خودتان ثبت و مانیتور می‌شود.
🔸
تزریق خودسانسوری:
وقتی می‌دانید هر کلیک شما رصد می‌شود، ناخودآگاه وارد یک «زندان شیشه‌ای» می‌شوید که خودتان هزینه‌اش را داده‌اید!
🔹
تجارت با حقوق اولیه:
حق بدیهی دسترسی به اینترنت آزاد را مسدود کرده‌اند و حالا همان را به قیمت نقض حریم خصوصی، به عنوان یک «آپشن ویژه» به خودمان می‌فروشند.
«اینترنت پرو» یک امکان رفاهی نیست؛ ابزاری برای کنترل نقطه‌ای و عادی‌سازیِ اینترنت طبقاتی است. بهای اصلی این سیم‌کارت‌ها پول نیست؛ حریم خصوصی ماست.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/iaghapour/2575" target="_blank">📅 15:30 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJjGChGAffAxXTjfTz2mSYsfhkVxzAhfFowD1fVPyjhFGQNNUdFl7lhseVeIWtrqdpn5Fe7ma7k4ECt2QeC0HBSHtgkR9c3qXvQ3qiUyYBuyMt91zuQfCRzsWUKgblYdTzPAkndfNDfIuVJBa_g80WEbOVxQomNPFedB2uiew6g1tpvbxHeI4Ko-7UfSbkaYqHCTCeENW3DRTXA1vHXSpeUR3yQpxXhWuiYgh-a9-mR17ZLuwDInZA8LsT_0pORFnrqbk_F34-YKCEBlfYq-uGJtRto3SXTcFPqWyqZ9Jav2FBJvPyKRXsoo-1cO99UAZBcPRFBIBOk4PJA5ribHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کلاینت اندروید GooseRelayVPN
🔹
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
پیکربندی مبتنی بر پروفایل
🔸
وضعیت و تله‌متری در صفحه Home
🔹
تب Logs برای عیب‌یابی Android/Core
🔸
قابلیت Split Tunneling و Internet Sharing
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/iaghapour/2573" target="_blank">📅 20:06 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💢
رئیس اتحادیه کسب‌وکارهای مجازی
:
به شرکت‌ها زنگ می‌زنند و پیشنهاد فروش اینترنت بدون فیلتر(پرو) برای کارمندانشان را می‌دهند.
⁉️
اگر موضوع واقعاً امنیت ملی است، چطور با پرداخت پول، امنیت تأمین می‌شود؟!
منبع: کانال خبری
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/iaghapour/2572" target="_blank">📅 13:23 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-poll">
<h4>📊 ⁉️نظرسنجی درباره سوال بالا (اگه واقعا نیاز دارید بله رو بزنید).</h4>
<ul>
<li>✓ بله معرفی بشه.</li>
<li>✓ خیر نیازی نیست.</li>
</ul>
</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/iaghapour/2571" target="_blank">📅 00:25 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✍🏻
دوستان، همان‌طور که خودتون در جریان هستید، من در این چند ماه حتی یک مورد
تبلیغ فیلترشکن، اوتباند
و موارد مشابه
قرار ندادم.
الان هم واقعاً تمایلی به این کار ندارم، چون شرایط اصلاً به‌گونه‌ای نیست که بشه کسی را معرفی کرد.
با این حال، در همین چند ماه پیام‌های بسیار زیادی داشتیم که درخواست می‌کردند حتماً یک شخص معتبر را معرفی کنیم؛ چرا که خیلی‌ها از کلاهبرداری‌های پیاپی خسته شدن و ارسال این دست پیام‌ها تا به همین امروز هم ادامه داره.
به همین دلیل، اگه خودتون موافق باشید،
افرادی رو که
از قبل با ما همکاری می‌کردند
و تا حدودی قابل‌اطمینان هستند، یکی‌یکی به شما معرفی کنیم. در این مورد ذکر چند نکته ضروری هستش:
🔸
عدم تضمین صددرصدی:
ناگفته نماند ما واقعاً نمیتونیم کسی را با اطمینان ۱۰۰ درصدی تأیید کنیم، اما افرادی که معرفی میشن همگی سابقه همکاری با ما را دارن.
🔹
عدم پذیرش تبلیغ جدید و اوتباند:
تا زمانی که شرایط استیبل و پایدار نشود، تبلیغ
هیچ فرد جدیدی را قبول نمی‌کنیم.
در ضمن،
تبلیغ فروش اوتباند هم به‌هیچ‌وجه پذیرفته نمی‌شود.
🔸
قیمت‌های منصفانه:
تمام سعی ما بر اینه افرادی را معرفی کنیم که در این زمینه منصف باشند و قیمت‌های بالایی ارائه ندهند. ولی خب، طبیعتاً نمیشه انتظار قیمت‌های قدیمی را داشت؛ چون همان‌طور که خودتون میدونید در حال حاضر هیچ‌کس با اون قیمت‌های قبلی فروشی نداره.
اگه تمایل دارید، لطفاً در نظرسنجی زیر شرکت کنید.
البته نظر شخصی خودم اینه که اگه در حال حاضر واقعاً مشکل خاصی ندارید، در نظرسنجی همان گزینه
(خیر) را انتخاب کنید
.</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/iaghapour/2570" target="_blank">📅 00:24 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">⚠️
هشدار مهم درباره اسکریپت VPN Over GitHub
▪️
لطفاً از این ابزار به عنوان
فیلترشکن
استفاده نکنید!
🚫
بن شدن اکانت:
تبدیل گیت‌هاب به تونل ترافیک، خلاف قوانین این سایت است و خیلی زود باعث مسدود شدن حساب شما می‌شود.
🐢
سرعت بسیار پایین:
برای هر ارتباط به یک بار
push
و
pull
نیاز دارد که آن را عملاً غیرقابل استفاده می‌کند.
🔻
خطر برای برنامه‌نویس‌ها:
گیت‌هاب یک سایت حیاتی برای توسعه‌دهندگان است؛ سوءاستفاده از آن ممکن است باعث حساسیت شده و دسترسی به این پلتفرم مهم را دوباره از کار بیندازد. (خارج شدن از لیست سفید و...)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/iaghapour/2569" target="_blank">📅 19:21 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ای بابا روش Vercel چرا بسته شد؟ هنوز آموزش نداده بودم که.
😁
سازمان فیلترینگ زرنگ شده ها. فک کنم خودشون رو آپدیت کردن دیگه به کانال من نگاه نمیکنن :)</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/iaghapour/2567" target="_blank">📅 16:34 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
دلار 177 و طلا 19,400,000
شب میخوابی صبح بلند میشی یه پله بدبخت تر میشی!</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/iaghapour/2566" target="_blank">📅 11:10 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا نیاز نیست پول بدین ری اکشن فیک بزنید.
😁</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/iaghapour/2565" target="_blank">📅 20:52 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GooseRelayVPN Guid -- @iAghapour.txt</div>
  <div class="tg-doc-extra">1.2 KB</div>
</div>
<a href="https://t.me/iaghapour/2564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
دستورات
برای ویدیو
GooseRelayVPN
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/iaghapour/2564" target="_blank">📅 14:21 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjuuyNmIE_8R1qjpt3_nYeTRUdzcjZrmS5KXprZ4A3t9-pZVuluKb_Pt_rzG6aqAFYHsRf8OHFTQ02x4sxf6kkRiit5r_pHccAia4z6jVg1AxqAPoZNzgbfZIZEeKyKjYpTyTsOTU8ytI4eiSdFBVZGRMejQJ8YfrWx58QJ_KO46FrAxvVlU8aGTZzyy9YGkx8X9TORurPGVmkG3-05lkEzz95ptj1o3PHrUarEvlbUz8NPRk1ugVNxWsE9lFbJFw0LQgJXPG9N_dG5vGV2HPZ8-xJWozR_Xgfp4YwdcJHAusl0LgtW59qmlG63gpfUjtdTgPEmrMlEpr6X_RPGKoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن شخصی و تانلینگ امن با سرویس‌های ابری! (GooseRelayVPN)
🔹
در این آموزش، یک روش عالی به نام GooseRelayVPN رو بهتون معرفی می‌کنم. با استفاده از اسکریپت‌های ابری (Apps Script) به عنوان واسطه و اتصال اون به سرور لینوکسی خودمون، یک تانل امن میسازیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل کدها
#آموزش
#فیلترشکن
#گوگل
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/iaghapour/2563" target="_blank">📅 14:18 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✍🏻
از اونجایی که دیگه کسی حوصله خوندن خبر رو نداره براتون عناوین خبر رو قرار دادم :)
🔸
دو ماه قطعی اینترنت؛ تعدیل ۳۰ تا ۵۰ درصدی نیروی انسانی در شرکت‌های اینترنت اشیا
🔹
ثبت ۳۱۸ هزار درخواست کار در یک روز در جاب‌ویژن
🔸
کانون وکلای اصفهان هم اینترنت «پرو» را نپذیرفت
🔹
ارسال پیامک اینترنت «پرو» این بار برای مهندسان
🔸
خزنده‌های گوگل پس از ۶۰ روز قطعی، دوباره سایت‌های ایرانی را می‌بینند
🔹
ضربه سنگین قطعی اینترنت به اشتغال زنان
🔸
دبیر سابق شورای‌ عالی فضای مجازی: اینترنت بین‌الملل می‌تواند ظرف ۵ دقیقه وصل شود.
🔹
سخنگوی دولت: با پایان بحران وضعیت اینترنت تغییر خواهد کرد
منبع: زومیت - دیجیاتو
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/iaghapour/2562" target="_blank">📅 11:54 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسکریپت KevinNet DNS با پشتیبانی از VayDNS آپدیت شد
حدودا 1 هفته پیش یک آموزش ضبط شده به اسم
(بهینه ترین روش اتصال با پروتکل DNS)
و توی این ویدیو ما اومدیم اسکریپت
KevinNet
رو معرفی کردیم. و الان در آپدیت جدید میتونه از VayDns هم ساپورت کنه.
🔹
اضافه شدن قابلیت تغییر مقادیر در برنامه
🔸
قابلیت تست ریزالور حتی در vaydns
🔹
قابلیت ایجاد پروفایل متعدد برای دامنه
. قابلیت های دیگه ...
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/iaghapour/2559" target="_blank">📅 19:22 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmjWxeAW9mmYO7zo4gJ-ZHgilNOGTHGMiJP_DI09AwItC6fOFFNs6qU9x7l_aDdjCo4xCWV0nH0CdkWUDf-MWM-V_KPB8tsXIcTUyag1UBtwo2jz5bx4FC4K1trz3CmfNvNh0aebqy8GDfFef8hgwzxlD84kSSXRLAGux4c9kmcDPHZZvgurr8c1jUr9sGaTIhML3kBLR70QNSmUvcNLTYzVFa6I0nuHVKe9UZgEiBMdupr-bAl83Dadcn6FzRu1DJ8JnUZqzIKEJxX-NhVkI98ey9nGooEJq5d98IT0IEkbNsam-3SV6HMMeRRJns3qo9uzwhvAo-8GN0JYBE7JOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت هارد ۱۰ ترابایت بنفش (Western Digital Purple) ناقابل 108 میلیون
🫠
همینطوری ادامه داشته باشه برای خرید یک گوشی دکمه ای هم باید همین مقدار پول بدیم....
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/iaghapour/2558" target="_blank">📅 09:34 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7Bcy2tSNeL3zdgiuihy92Pkk4qs7Vix_n9I_8p6kSQVeHQvmye0E4jQ9dIk_s6dqfauDneYzW2dpGi-4QKNZ8PnHLcJ8RHt3diaU8yUQjfVhMer4MAN4x6CTwIkI2aACQT7xRQ3iZIFqUiOdJxRvovlShSODLKaXYOfv1RDAmplj0exGDp66tOF8dkf66LCkX32nctc5Wr-sdS-HQqDWPEoVr__isk4xABS4Jf4NWB9xT9nW6Y1JBzRaLTrtB7Psqv9XM-I_iRwu-75LUtPC5rPhu8eYZ7__QF5DXqVDBHac94hAYIOwQWkzfnsJEbyZBICoBHZ5G9u-b-N4YrR8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب‌کننده خودکار Parley Chat
🔻
از اونجایی که راه‌اندازی و کانفیگ کامل یک پلتفرم چت روی سرور (با تمام دردسرهای تنظیم دیتابیس، وب‌سرور و گواهینامه امنیتی) کار سخت و زمان‌بریه، این ابزار جذاب اومده تا همه چیز رو براتون ساده کنه!
🔸
راه‌اندازی کامل بکند (Backend) و فرانت‌اند (Frontend)
🔹
کانفیگ خودکار Nginx به همراه دریافت گواهینامه SSL
🔸
ایجاد سرویس‌های Systemd برای مدیریت آسان‌تر و پایداری سرویس
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/iaghapour/2557" target="_blank">📅 21:48 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWdBwL2xmDpwdqAeMayUJFmpKZxggXhEAya_BUFxzt79xEQbz3YKnPFVy8uxuJx1SoLeqfsijFITp7S2fI5SYvkw5at2fg2LXepKDHC2iEFJLEtUaBDbOuNOdOZ09lORXqyOVYVtAJe6hfkMyfwRk74OMpDLgwK7y0PfYQgKXCC4CXLSPzoGerof4Q5-eJndaCqwEItwSLCZnnvb-MBrZFGAZ4Ynjr4ROsYQLexFe7G-pbAZwg9bDz9rKQQ-273-AtLdMuaawygXclHWB7cPsVcCgXeH7G9J0ynAOO0CZFI7T8wnrcmQajcHShaeXHul_XRHU4aPg6nFxti9RH0pAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
لینک همه سایت‌های کاربردی تو این سایته!
🔹
از اونجایی که پیدا کردن لینک سایت‌های کاربردی در دسته‌بندی‌های مختلف مثل آپلودسنترها، سایت‌های دانلود فیلم و سریال، ابزارهای آنلاین و... خیلی سخت و زمان‌بر شده، سایت WebDX اومده همه این‌ها رو به صورت منظم و دسته‌بندی شده یک جا جمع‌آوری کرده.
🔗
لینک ورود به سایت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/iaghapour/2556" target="_blank">📅 21:40 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">💢
سازمان نظام پرستاری:
با وجود اینکه امکان برقراری اینترنت پرو برای اعضای خود را داریم، تا زمانی که همه مردم ایران به اینترنت متصل نشوند از این امکان استفاده نخواهیم کرد.
🔴
در اطلاعیه کامل سازمان نظام پرستاری:
«بسمه تعالی
سازمان نظام پرستاری جمهوری اسلامی ایران به اطلاع کلیه پرستاران و مردم عزیز ایران می‌رساند؛ با توجه به محدودیت‌های ایجادشده در دسترسی به اینترنت بین‌الملل به‌دلیل شرایط خاص جنگی کشور و ارائه دسترسی محدود (اینترنت پرو) به برخی اقشار، امکان اعطای این امتیاز به اعضای سازمان نظام پرستاری نیز از سوی مقامات مسئول اعلام شد، لکن سازمان نظام پرستاری جمهوری اسلامی ایران براساس بررسی جوانب مختلف تا زمان رفع محدودیت‌های دسترسی عموم مردم به اینترنت بین‌الملل، درخواست هیچ امتیاز ویژه‌ای را برای اعضای خود نخواهد داشت.
ان‌شالله زمانی که این امکان برای همه مردم ایران فراهم باشد، پرستاران نیز در کنار آحاد مردم از این امکان استفاده خواهند نمود.»
﻿
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/iaghapour/2555" target="_blank">📅 13:20 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsgdyypOaGDqFWfgbU-Ln5DgcuDSAYv54BN4G7kaMJ47ICxIYkBJdJzXrFG7_A3uUlOEqDZby6B9jBo-NtTJaxExDZlgfs_yZvKeND5i5-SNXkafTNhX10urs9bP5-_AjM9gWfIBQVaD2rzKZarnPnbngqMQEXAbvWOmt0x5uqWiMAGvreU0LxQRnloutdRUtfaYskgubsetdpJBJTxtPKY7uG1c2O03OZ49KbvPx7TzO3AGW8mebaAmBOhHbeXrUd7QkzbODYKNt6Nfu3z_Tdk9Oh0TI3Ts7o6Tb5v0vS8s5k9tFxbbiBznby1XB0B-Fil1_aJ5zUkpMEGP0hateg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات‌های کاربردی تلگرام برای شرایط اینترنت محدود
با توجه به محدودیت‌های فعلی، این ربات‌ها حکم یک اینترنت آزاد و همه‌کاره را در قلب تلگرام دارند:
🔹
@GPT4Telegrambot
دسترسی به ChatGPT، جمنای و تولید تصویر.
🔸
@WebSearchAiBot
جستجو در گوگل و خواندن محتوای سایت‌های فیلتر شده.
🔹
@apkdl_bot
دانلود مستقیم برنامه‌های گوگل‌پلی (جایگزین استور).
🔸
@SaveAsBot
دانلود ویدیو و عکس از یوتیوب، اینستاگرام و توییتر.
🔹
@reddit_download_bot
دانلود محتوای متنی و تصویری از سایت ردیت.
🔸
@UrlUploadBot
تبدیل لینک دانلود سایت‌ها به فایل مستقیم تلگرامی.
🔹
@ReadabBot
تبدیل مقالات وب به حالت مطالعه سریع در خود تلگرام.
🔸
@vtovbot
تبدیل فایل‌های صوتی پرحجم به ویس باکیفیت و کم‌حجم.
🔹
@voicybot
تبدیل ویس به متن با پشتیبانی از زبان فارسی.
🔸
@fakemailbot
ساخت ایمیل موقت برای زمان‌هایی که جیمیل در دسترس نیست.
🔹
@newfileconverterbot
تغییر فرمت انواع فایل‌ها مثل عکس، ویدیو و داکیومنت.
©️
با تشکر از ایوب عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/iaghapour/2553" target="_blank">📅 20:41 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2552">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💢
اردستانی؛ نماینده مجلس
:
حکومت تصمیم گرفته فعلا روایت خودشو بیان کنه. برای‌همین به خبرنگارها؛ دانشگاهی ها؛ نماینده های مجلس و هنرمندانی که با حکومت همراهن اینترنت داده تا برای خارجی ها تولید محتوا کنن.
پ.ن: عجب بابا عجب دیگه کار از مخفی کردن و شرمنده بودن و... گذشته. خیلی قشنگ این تبعیض رو فریاد میزنن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/iaghapour/2552" target="_blank">📅 17:38 · 05 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✍🏻
یه تناقض عجیب بین حرفای مسئولین و واقعیت اینترنت کشور هست. از یه طرف رئیس‌جمهور میگه موافق وصل شدن اینترنته، از اون طرف سخنگوی دولت میگه اصلاً اینترنت طبقاتی نداریم و وزیر ارتباطات هم کلاً وجود لیست سفید رو گردن نمی‌گیره.
ولی خب تو عمل، داریم یه جور تبعیض و آپارتاید اینترنتی رو به چشم می‌بینیم:
افراد رانتی:
اینترنت کاملاً آزاد و بدون فیلتر (همون لیست سفید).
شهروندای درجه دو:
یه اینترنتی که بدون فیلترشکن دوزار نمی‌ارزه (همون اینترنت پرو).
مردم عادی:
محدودیت کامل و حبس شدن تو شبکه داخلی.
از همه جالب‌تر مسئولینی هستن که میان میگن این محدودیتا موقتیه. یعنی ۶۰ روز قطعیِ پشت سر هم، معنی «موقت» میده؟ اصلاً می‌دونید موقت یعنی چی؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/iaghapour/2551" target="_blank">📅 19:30 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPKIgJgN4xLjuy3kC_6uJ58Y2UZKM9d7aTMq9xksgeENfeQRr8-WCc81Ks-2S3zC2fFG34T-uiLDcMcj5chvzUL3caRLo8Rx4PpJCPlWr73-n0FXgUcN11eHqRGYqsroxUzaDrAxpKyFSEmri_sOqd1auB61eXhtimy4sKwRHiv1pK1vbA45JkJW63aoNmo37kyKFz21sI6GeAceqKPA26BPEIqV5_bQTpkgHeGWuXM7R5gcjdr4lEHvCha9NWQk00jI1bA8AUgbwT4EmfxJUBuBMcBzbCLQLxsJSJ6XIilspRPGPMILJCHfhTu8B26tUczCUQuWJRPH4pwnJrI1cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
روز ۵۶ام از قطع اینترنت در
#ایران
هستش و اتصال بین‌المللی بیش از ۱۳۲۰ ساعته که قطع شده و کسی پاسخگو نیست!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/iaghapour/2550" target="_blank">📅 11:19 · 04 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚠️
یک یادآوری و هشدار خیلی مهم به دوستان عزیز
دیگه واقعاً حسابش از دستم در رفته که تا حالا چند بار این موضوع رو گفتم، اما باز هم باید تکرار کنم:
ما اصلاً هیچ گروهی نداریم!
متأسفانه بعضی‌ها با استفاده از اسم و عکس ما اقدام به ساخت گروه یا کانال می‌کنند. حتی بعضی‌ها خودشون رو به عنوان «پشتیبانی» ما معرفی می‌کنند. من قصد قضاوت در مورد هدف این افراد رو ندارم، اما این کار باعث سردرگمی شما میشه و اصلاً درست نیست.
لطفاً توجه کنید که فعالیت رسمی ما فقط و فقط در چند آدرس زیر انجام میشه و تمام:
🔸
یوتیوب:
youtube.com/@iAghapour
🔹
کانال تلگرام:
t.me/iaghapour
🤖
ربات تماس با ما:
@iaghapourbot
🐦
توییتر:
(که البته خیلی اونجا فعال نیستم)
نکته مهم: هر گروه، کانال یا شخصی که خارج از این لیستِ بالا خودش رو مرتبط با ما معرفی کرد، هیچ ارتباطی به ما نداره.
ممنون از درک و همراهی همیشگی‌تون!
🌹</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/iaghapour/2547" target="_blank">📅 15:42 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚀
معرفی پیام‌رسان دلتا چت و سرور Madmail
🔹
یک پیام‌رسان امن و غیرمتمرکز بر بستر ایمیل که حتی در زمان محدودیت‌های اینترنت هم به کارتان می‌آید! با پروژه Madmail می‌توانید به سادگی و سرعت، سرور اختصاصی خودتان را بالا بیاورید.
🔻
ویژگی‌های کلیدی:
- امنیت به شدت بالا: رمزنگاری پیشرفته و عدم نیاز به شماره موبایل.
- مقاوم در برابر قطعی‌ها: امکان راه‌اندازی آسان رله‌ها روی سرورهای داخلی.
- اجرای سرور چت‌میل تنها با یک فایل باینری (حتی روی سرورهای آپدیت‌نشده و بدون اینترنت بین‌الملل).
- پشتیبانی از تماس صوتی و تصویری.
🔗
لینک گیت‌هاب برای بررسی و نصب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/iaghapour/2545" target="_blank">📅 13:15 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✍🏻
دوستان، اگر برای باز کردن تلگرام و سایت‌های مختلف از روش
MasterHttpRelayVPN
استفاده می‌کنید، حتماً حواستون به این 2 تا نکته مهم باشه:
۱. آی‌پی شما تغییر نمی‌کنه:
برخلاف فیلترشکن‌های عادی، آی‌پی شما تو این روش همون ایران می‌مونه. در نتیجه سایت‌های تحریمی براتون باز نمیشن و حتی ممکنه سایت‌های حساس اکانتتون رو به خاطر آی‌پی ایران بن کنن.
۲. جیمیل اصلی‌تون رو استفاده نکنید:
یه سری گزارش‌ها به دستمون رسیده که گوگل ممکنه اکانت‌ها رو مسدود کنه. با اینکه هنوز مدرک زیادی وجود نداره و قطعی نشده، اما بهتره اصلاً ریسک نکنید و از جیمیل شخصی‌تون استفاده نکنید.
۳. نسخه اندروید رسید:
خبر خوب اینه که از امروز می‌تونید نسخه اندروید این روش رو هم نصب و استفاده کنید.
🔻
ممکنه مواردی رو من پوشش ندم ولی کانال
IRCF
که یکی از قدیمی ترین و بهترین کانال ها هستش میتونه راهنمای شما باشه.</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/iaghapour/2544" target="_blank">📅 13:09 · 03 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری…</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/iaghapour/2542" target="_blank">📅 17:08 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Moux1Yme10wdyuLuoCKVEfYTgPDhCppYZv5INenRUVH83dQ6yqN8wTQfm0z6mWdxrPb9g1c_Imo4CV-ZyX0KMsFQNVHa65SAw4be2htsL4WNPtBVowmBHZbHLCmyRiBprkVG48qZx9jRGY4keTq6u9DKf2E-1RDuFMJokPMfugjZxbRjR1zjBN8alo_q6TCc9VaVZJqTK33RX2NVigx0ioVD2WP_BkZ5r-eyJmoajsnTOEyGatrwwPo9WSsx8fnC3GGSGA0bHlIuCObCOae--w2VXEB0YUClRHCBqTc22Otf5GdmHIz5pE6TlNMY7m9LxaxwLbJkvy0WeQqRMm-a6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
جواب به سوالات پرتکرار شما + بهینه ترین روش اتصال با پروتکل DNS
🔹
توی این ویدیو به پرتکرارترین سوالات شما درباره ساخت فیلترشکن جواب دادم. در نیمه دوم هم یک روش فوق‌العاده و بهینه برای اتصال با پروتکل DNS رو به صورت قدم‌به‌قدم آموزش دادم تا پایداری بیشتری داشته باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔻
دانلود فایل exe اسکریپت
#آموزش
#فیلترشکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/iaghapour/2540" target="_blank">📅 16:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-rg_VAacm9qGo_ZnMtM1cB7H6eNO7DH2lBFhV8LHgiEaGX8P6YEWMg7X-GSAsaHRki6ydmAHMabDd_QPcNjE1ruh_jIUSbOdx-zYjYoJVhHiHznVu2_KSIeauNJZcwPGpFNO45sl2foR_ZXMAMFSHCT5VD7kLbLEOKhh8GBjavgJehb493mBH9WJT_cJkUK0j9T9Eh9DbzascduKX4WZ6r-crwpX8qaWPYoaAy0Bs17RAJHMY46Fq9feMfm34hZuu_lz5xQzxXZwBr4iFNF-TSGE6N0lZIjryGL3NKSiM0GB7b14FnMKEBEB21BfhXaTKQ_avmeO8fjgz7Cw5-igA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست ملی کردن کامل اینترنت فقط برای طرفداران نت ملی!
🔹
هرچی از طنز ماجرا بگم کمه :) یک
کارزار
ساختن و گفتن کد ملی طرفدارهای نت ملی رو بگیرید و اینترنت رو برای اونا برای همیشه ملی کنید :)
داداشایی که سنگ اینترنت ملی رو به سینه می‌زنن، بفرما این گوی و این میدان! لطفاً اینترنت این عزیزان رو روی کد ملی‌شون برای همیشه «ملی» کنید تا دیگه غصه ما رو نخورن. ما خودمون یه جوری با این اینترنتِ پر از فسادِ بین‌المللی کنار میایم!
🤣
🔥
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2537" target="_blank">📅 01:02 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بچه‌ها حجم پیام‌ها اون‌قدر زیاده که اون عزیزی که به عنوان پشتیبان داره همکاری میکنه با ما واقعاً نمی‌رسه همه رو سریع بخونه یا جواب بده. شرمنده‌ی روی ماهتونیم و بابت این موضوع از همگی عذر می‌خوایم.
🙏🏻
🌹</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/iaghapour/2535" target="_blank">📅 00:37 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭕️
آپدیت مسنجر سانگبرد منتشر شد
(
v0.9.0
)
🔹
با اسکریپت زیر میتونید روی سرور ایران یک مسنجر شخصی برای خودتون و خانواده بسازید.
-
📥
قابلیت آپدیت آفلاین برنامه از اسکریپت
-
🔒
رمزنگاری Client-Server
-
📃
قابلیت Context Menu اختصاصی برنامه
-
↪️
قابلیت فوروارد کردن پیام
-
🗑
قابلیت پاک کردن پیام (یک طرفه و دو طرفه)
-
✏️
قابلیت ادیت پیام
-
💬
قابلیت پاک کردن خودکار پیام های متنی
-
📜
امکان دریافت سرتیفیکیت 6 روزه برای IP در اسکریپت
-
♻️
دستور بازیابی دیتابیس از بکاپ در اسکریپت
-
🚫
دستور بن کردن یوزرها در اسکریپت
-
✨
بهبود UI/UX
-
📜
قابلیت نصب سرتیفیکیت با فایل های کلید SSL
-
👤
دستور ادیت مشخصات یوزر در اسکریپت
-
⚙️
قابلیت تنظیم پورت دلخواه برای nginx در حالت نصب با دامنه
-
🔧
به همراه رفع باگ های متعدد
اطلاعات بیشتر در گیت‌هاب
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/iaghapour/2534" target="_blank">📅 00:31 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">2 تا آموزش عمومی و خوب در پیش داریم.
👈🏻
یکی آموزش نصب و اجرا هوش مصنوعی لوکال و بدون اینترنت.
👈🏻
و یک آموزش کاربردی و پاسخ به سوالات پر تکرار شما.
فردا یکی از اینها منتشر میشه.
💚</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/iaghapour/2533" target="_blank">📅 00:26 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✍🏻
همان‌طور که احتمالاً دیده‌اید، اخیراً آموزش‌ها و اسکریپت‌هایی (مشابه Spoof SNI) برای دور زدن فیلترینگ یوتیوب و برخی سایت‌ها منتشر شده است. البته قبلاً هم شاهد موارد مشابه بوده‌ایم.
دلیل اینکه ما این روش‌ها را در کانال قرار ندادیم، درخواست بعضی از دوستان بود! درخواستشان چه بود؟
اینکه روش‌های جدید را «پابلیک» نکنیم
تا مبادا هزاران نفر از مردم عادی از آن استفاده کنند و روش بسته شود؛ در عوض، فقط یک عده محدود بتوانند با خیال راحت از آن لذت ببرند. واقعاً عجب منطق جالب و «ازخودگذشته‌ای»!
😇
ولی خب به هر حال، کانال‌های دیگه این آموزش‌ها را منتشر کردن و میتونید از اون ها استفاده کنید.
این توضیحات هم بماند برای آن دسته از دوستانی که قدرت تفکر دارند و متوجه ماجرا میشن. :)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/iaghapour/2532" target="_blank">📅 00:25 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
آتش بس تا اطلاع ثانوی تمدید شد.
🔹
ولی اینترنت باز نمیشه. چون امنیت به خطر میفته. این که 2 ماهه سیستم خودمون و حتی گوشی رو آپدیت نکردیم و آنتی ویروس خودمون رو آپدیت نکردیم و.. خیلی به امنیت آسیبی نمیزنه. حداقل به امنیت ما آسیبی نمیزنه :|</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/iaghapour/2531" target="_blank">📅 00:14 · 02 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">💢
رئیس شورای اطلاع رسانی دولت: قطعی اینترنت موقتیه و یکم دندون رو جیگر بزارید تا دشمن رو به یه شکست ذلیلانه بکشونیم بعدش حتما وصل میشه و به شرایط عادی برمیگرده.
پ.ن: کاملا از ثبت نام اینترنت پرو در رسته ها و شغل های مختلف مشخصه دارید راست میگید.
👌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/iaghapour/2529" target="_blank">📅 17:53 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
گوگل و گیت‌هاب دوباره باز شد!
بازی موش و گربه شده قشنگ!
🧐
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/iaghapour/2528" target="_blank">📅 13:31 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚠️
گیت هاب هم بسته شد
احتمال موقت بودن یا اختلال هم وجود داره!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/iaghapour/2525" target="_blank">📅 11:47 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚠️
گوگل مجدد فیلتر شد
البته وقتی سرچ میکردی سایت های توش رو نمیتونستی باز کنی پس خیلی هم فایده نداشت! مثل این میمونه که بچه رو ببری ویترین اسباب بازی رو بهش نشون بدی ولی بگی حق دست زدن نداری...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/iaghapour/2524" target="_blank">📅 11:44 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDD_EMWCktIqGLD-DsPqAiwJpUxP2GrkRuq7_-T_S8AwKcXT01YW9Ke0Q3TzPo-P4nxz5i4Fx9p1gh5gYCzkRgGdTj62Mu6CTQz-0iV1_d2M6R2LYK1RJ6IpG5B9BTYzCf2PB98kyVN-DZmlp3LSJ8deCJqMP1QBtUpxVAiJ4k8DMSlYYMkNeTnXfTAN0oaN6ygkJ7ZHkoMos19J_l7tLhFdp68VWnSZj30KOZsPrjZgywrS4_6AB1tUJM7wSNPlDEO5brCxo_ycriYaXGanahyBj1DQQ4qSQp2kNX-au2KyP6rrJ1GifRolo-7R2hI-oZk3ce-HtdFN-PGJoFomqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استارت اینترنت طبقاتی توسط همراه اول!
🔹
همراه اول رسماً از طرح اینترنت طبقاتی خود رونمایی کرد. با افزوده شدن بخش «اشتراک پرو» به منوی این اپراتور، زین‌پس تنها افراد خاصی که فرآیند احراز هویت را طی کرده باشند، امکان دسترسی به این سرویس را خواهند داشت. گفتنی است هزینه بسته ۵۰ گیگابایتی در این اشتراک، ۲ میلیون تومان تعیین شده است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/iaghapour/2523" target="_blank">📅 00:27 · 01 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9xjBglDfhdIMg0W6shK-CGoZUBqzmsrcvxv3VauIBy1MwJXvpvN4weu5SN8MohG74ACujDKIRDH-01d5UWNrOKd_JWVEakvbHCMzN3VyYzXaKSG_KgJxKcp923kqD_h-FX-5Cb6PpoMxmCxLE72vECaSlb7vXWo8pYirG2IDhjRli6y2KlaBoYHeHfncNVw3NIeeA7-PqElrwTrxBoHXQiSTvHfzmf3Xe5kyn0m9pwPcAMh5SYJGviqw8CXVAtFIJiBJk2qjvc1G_VBtlaNVd2LUncYOH3iy-zmx3bWZREQ2FBuLK4K_P0d3z7T8Llvjpiuf3ABJ9G2tE6VF5MHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
چرا جهان، زندان دیجیتال ایران را نمی‌بیند؟
بیش از دو ماه است که اینترنت در ایران قطع شده و میلیون‌ها نفر در یک «اینترانتِ» محدود و ایزوله حبس شده‌اند. کسب‌وکارها نابود شده و ارتباطات فلج شده است، اما در کمال تعجب، سازمان‌های مدعی حقوق بشر خود را به خواب زده‌اند.
🔻
چرا نهادهای بین‌المللی خفه خون گرفته‌اند؟
سازمان ملل سال‌ها پیش قطع اینترنت را نقض صریح حقوق بشر اعلام کرد. اما ظاهراً وقتی نوبت به ایران می‌رسد، این قوانین چیزی جز کاغذپاره‌های نمایشی نیستند.
اگر اینترنت در یک کشور غربی دو ساعت قطع شود، دنیا جلسه اضطراری می‌گذارد! اما ماه‌ها حبس دیجیتال در ایران، ارزش یک واکنش قاطع را برای آن‌ها ندارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/iaghapour/2522" target="_blank">📅 19:45 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArdyVt2dw8HLMJzvfsVBneLGOT046txkRM83vD6g-3n3M974UtsPK0wQw6xXxGAThkC70IER6ffCUB7DKyBHJQuU3mZsL_0ZNI5f0zKYb9xQA2e-kf6M52ViSoiTlmTMSeekRQ-jPNNVRZUK19TLzDr5jhghTfLemULT91LSU3uY9QVFg72MdP8oU2aK0zj_Ab1M31Bn_a6HzmJUzdaTq-QqW6VMMU48TkKJmFFL87VUMmqYOPqKFDbVHl4HeEO8wK7zuCDqFAEReosMB1SidZ6NumgkT1SRrY2jgdYlOj1gL8R7CUb3oYTw3EFq2JkGWJtUMH5JyEGNOnhf8QcbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کانفیگ فروش دنیا
😊</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/iaghapour/2521" target="_blank">📅 15:30 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
موج حملات در کمین سایت‌های آپدیت‌نشده!
تو این دو ماه اخیر که اینترنت ملی شده و دسترسی‌ها به شدت محدود بوده، یه خطر امنیتی پنهان اما بسیار بزرگ، خیلی از کسب‌وکارهای آنلاین رو تهدید می‌کنه:
عقب موندن از آپدیت‌ها!
فکرش رو بکنید؛ تو این مدت چقدر سایت وردپرسی و پلتفرم‌های مختلف داریم که هسته اصلی، قالب‌ها و افزونه‌هاشون رنگ آپدیت رو ندیدن؟
⚠️
خطر اصلی کی خودش رو نشون میده؟
دقیقاً همون لحظه‌ای که اینترنت دوباره به حالت عادی برگرده و دسترسی‌های بین‌المللی باز بشه. ربات‌های مخرب و هکرها منتظر همین فرصت هستن تا از باگ‌ها و آسیب‌پذیری‌های امنیتی این چند وقت (که پچ و برطرف نشدن) سوءاستفاده کنن. با وصل شدن اینترنت، باید منتظر یه موج گسترده از حملات هکری و بدافزاری به این سایت‌های بی‌دفاع باشیم.
🛡
چاره چیه؟ (همین الان دست به کار بشید)
آپدیت دستی:
منتظر آپدیت خودکار از پیشخوان نمونید. فایل‌های آپدیت‌شده افزونه‌ها و قالب‌های ضروری رو (از طریق منابع در دسترس یا شبکه‌های داخلی) دانلود کنید و از طریق هاست یا FTP به‌صورت دستی جایگزین کنید.
بک‌آپ‌گیری فوری:
همین الان یه فول‌بک‌آپ از دیتابیس و فایل‌های سایتتون بگیرید و تو یه فضای امن خارج از هاست ذخیره کنید.
محدودسازی دسترسی‌ها:
موقتاً تنظیمات افزونه‌های امنیتی (مثل Wordfence یا iThemes) رو روی حالت سخت‌گیرانه‌تری قرار بدید.
🔄
حتماً این پست رو برای دوستان وب‌مستر، طراحان سایت و صاحبان کسب‌وکار بفرستید تا اونا هم آماده باشن.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/iaghapour/2520" target="_blank">📅 14:32 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">یادتونه یه زمانی می‌گفتیم هوش مصنوعی قراره خیلی از ماها رو بیکار کنه؟
هیچکس فکرش رو نمی‌کرد یک روز سیاست فیلترینگ و نت ملی و... نزدیک به 10 میلیون آدم رو بیکار کنه!
بیش از چند ماهه که هزاران کسب و کار نابود شدن و هزاران آرزو مردن! پاسخگو اینها چه کسانی هستن؟ تا کی قراره قطعی اینترنت ادامه داشته باشه؟
#اینترنت_را_وصل_کنید
#اینترنت_ملی
#DigitalBlackOutIran‌
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/iaghapour/2519" target="_blank">📅 11:30 · 31 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTUKkNKdbELVW13T5xNouwTK3S6b6IMUDR1WuQFMFO2Sr_R4oWjBqCQjZpy91eVk54GAvAlTv9mxFn40O0pfT0GvO5wZqdEzHgbylyMaLRbR0BOw2yI4ftoClVwFl3r1s5l7H0JJ1ib5A9JzEgrPiia-rGUOz5nL-Yyfx83GKw0Bl30WQTDM7zCT08ThqxUQopsh4QAkVHCI10YkTrCOrQQ_RodOemDmsODrOxhGwT6CLdtrwfrZDPZHh8w8iKI-FpBdAHY_W2RSNznpef2uYMEWUiAjhKqJvvBkglhjmQmwBF1ieFrc0U7EKq4smad2ROsdjUorXiMllAoM63GKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
تعطیلی پلتفرم «کاموا» در سایه جنگ و قطعی اینترنت
🔹
پلتفرم فروشگاه‌ساز باسابقه «کاموا» پس از ۸ سال فعالیت، به دلیل بحران‌های سنگین ناشی از دو جنگ و ماه‌ها قطعی کامل اینترنت، از فردا برای همیشه به کار خود پایان می‌دهد.
🔸
هادی فرنود، بنیان‌گذار این مجموعه، ضمن اعلام این خبر تلخ اشاره کرد که اگرچه در سالیان گذشته توانسته بودند از سد چالش‌های اقتصادی و قوانین دست‌وپاگیر عبور کنند، اما تحمل بحران‌های اخیر غیرممکن بوده است. او این تصمیم را فراتر از یک اتفاق تجاری دانست و کاموا را بخش مهمی از زندگی خود توصیف کرد.
🔹
فرنود به مشتریان اطمینان داده است که تمامی هزینه‌های آن‌ها به صورت کامل مسترد خواهد شد. وی در نهایت تاکید کرد که رسیدن به خط پایان به معنای بی‌ارزش بودن این راه نیست و کاموا یکی از مهم‌ترین تجربه‌های زندگی او باقی خواهد ماند.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/iaghapour/2518" target="_blank">📅 23:33 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtGVm52_domXb-t0aSd4KXf3vTXsjfki4E_pec0pC8WSdzHz_H8IdI5fkESkiyfSv3EXkEwayOH1R-hY9k8BNbN0_0TaSy9Yr4CffqRewMen-pcvkSIsIuhpkJae6JtLCmvtf1Suo6ZPgeqjY5sNQudVH_l-rBX7Aqjq85xxZzILh14lV6APojuCEerAUeyiPic5DeSio3NX_DkB8T2RK5weo4aCpT73zOZEVGnH0u42AJebAY3CKaM0c0k1NO-_2ZSD5ociwoCl_yGWkWbEUF_fcPPu5qoJ6JKE-21MlnwQqrtNXsH348ky7YTZ4st5xuhQWD2EUjyDi_gxFX-v_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت بحرانی اینترنت در ایران؛ رتبه ۹۸ در میان ۱۰۰ کشور جهان!
📉
تازه‌ترین گزارش انجمن تجارت الکترونیک تهران از وضعیت اینترنت ایران (زمستان ۱۴۰۴)، تصویر بسیار نگران‌کننده‌ای را نشان می‌دهد. بر اساس این گزارش، اینترنت کشور را می‌توان با سه کلمه «کُند (رتبه ۹۲)»، «پراختلال (رتبه ۹۶)» و «محدود (رتبه ۹۸)» توصیف کرد.
📊
آمارهای کلیدی و نگران‌کننده:
🔹
سرعت پایین: میانگین پهنای باند در ایران تنها ۵.۴ مگابیت‌برثانیه است، در حالی که میانگین آسیا به ۱۳ مگابیت‌برثانیه می‌رسد.
🔹
اختلالات شدید: شاخص تأخیر (Latency) بسیار بالاست و تنها ۳ درصد از وب‌سایت‌های پرکاربرد برای کاربران ایرانی در وضعیت مطلوب و پایدار قرار دارند.
🔹
فیلترینگ گسترده: با مسدود بودن ۳۹ درصد از دامنه‌ها، اینترنت ایران از نظر میزان سانسور پس از چین و میانمار در انتهای جدول قرار دارد.
پ.ن: به نظر میاد این آمار فقط مربوط به سال قبل باشه در صورتی که تو کل سال جدید که 1 ماه ازش میگذره هم اینترنت نداشتیم!
©️
زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/iaghapour/2517" target="_blank">📅 22:45 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7xlmig83qMwBvswPCDnBymyHAVb2bLr7IvUP8GeFmDAmMW-z1kfMerN7DrwxnoK9hbWrJwCPU8d6pRH2k0EP_-02jY5fMfTd4bf3qJLQNfFRugoaoWWayCcin7oYZe5jTKhEobwdJNKwHrciCSktMmt0veggcAaa6pppx8MAgHlUS83ZEDg8fazd6hfTX9D9HNc4xBP1XQkomdl35Ec7hlx4_CuDaIWKInKtis1fSK6Lxctk1EgLWcMz_NtX1eU4mNUWtpPC2YOzhhRmsxg2U2_tQK4OTkCCvUMFBkJtGuqkhkgoSKJJv-TGPAQOW3dm0jvCOHVEBBGTfCXEwnx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
معرفی اپلیکیشن Range Scout؛ اسکنر قدرتمند DNS برای اندروید
🔹
اگر به دنبال یک ابزار حرفه‌ای و در دسترس برای اسکن و تحلیل DNS resolverها هستید، دیگر نیازی به سیستم‌های دسکتاپ ندارید! اپلیکیشن Range Scout یک ابزار کاملاً رایگان و متن‌باز برای اندروید است که این کار را مستقیماً روی گوشی موبایل شما انجام می‌دهد.
🔸
این برنامه با موتور اسکن قدرتمند خود، به شما کمک می‌کند تا بهترین و باکیفیت‌ترین Resolverها را پیدا کرده و آن‌ها را بر اساس عملکردشان بسنجید.
— اسکن منعطف:
پشتیبانی از اسکن دقیق روی IPهای تکی و همچنین رنج‌های کامل IPv4.
— پشتیبانی از پروتکل‌های اصلی:
موتور اسکن DNS با قابلیت پشتیبانی کامل از هر دو پروتکل UDP و TCP.
—
تشخیص پروکسی:
قابلیت بسیار کاربردی تشخیص DNS Proxy به‌صورت شفاف (Transparent) در اسکن‌های UDP.
📥
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/iaghapour/2516" target="_blank">📅 21:53 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT4JXjH5dpFdFYWDEHVHvu3aPiv9nQICg183Td2FZZo5RaagzqBNeCUFwgtHGaaUzRZAY4cZY0jdo2p3QC3Gd7NHjfoj4gDvhWPDKRhQzyAFuauRwifExiZik-LGylkyIb4QAb2FoHYsQMT3bLbslKXz3_sWXog7Fiq1FOh5JmO0rGMFwBf6gRByuuxXNqe0Iw01O3UhpTBkgovdTByzvJ8H5IGVhGJrLSBqw_D1LszgJaNFEda9S20g9JscC57rXOhLx9T3xagH8QfYdOa423HVbnZhA2DXkzyyBNZUu4KpcgJElvyDYkmtzc-vgLmCrGF-LtD9BZsApm2CM5snUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی ابزار MasterDnsWeb
🔸
این ابزار بدرد کسانی میخوره که، روی سرور ایران میخوان نسخه کلاینت MasterDnsVPN رو نصب کنن و از طریق وب مدیریتش کنن.
🔻
ویژگی‌های اصلی:
🔹
قابلیت ساخت چندین Instance به طور همزمان
🔸
قابلیت مدیریت و انجام تغییرات کانفیگ و ریزالور روی وب
🔹
نمایش لاگ های هر systemctl و قابلیت ریست کردن و استارت کردن.
🔗
گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/iaghapour/2515" target="_blank">📅 20:28 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-poll">
<h4>📊 به نظر میاد لیست سفید داره اجرا میشه و فقط به سایت‌هایی که خودشون باز میکنن قراره دسترسی داشته باشیم.هیچ نشونه ای از بازگشت اینترنت نیست!⁉️نظر شما در این‌باره چیه؟</h4>
<ul>
<li>✓ همینطوره و قرار نیست باز بشه.</li>
<li>✓ باز میشه بزودی.</li>
<li>✓ بعد جنگ باز میشه.</li>
<li>✓ نمیدونم :(</li>
</ul>
</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/iaghapour/2513" target="_blank">📅 01:24 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✍🏻
چندتا از کانال‌ها لطف کردن و تو چند روز گذشته کانال ما رو معرفی کردن؛ به همین خاطر افتخار این رو داریم که میزبان چند هزار عضو جدید باشیم. :)
🔻
دوستان عزیز، به کانال خودتون خیلی خوش اومدید!
💚
فقط یک خواهش کوچیک دارم، ممنون می‌شم پستی که
بالاتر
براتون قرار دادم رو حتماً مطالعه کنید.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/iaghapour/2512" target="_blank">📅 00:36 · 30 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUalQXx4h7dxStc0FTET38aTcbOvQU20YjgQNXFaKd1kDITMRkcIKk6TFzPzs9hXlFiU0IaIJ3jOBKOTFCMhZy7D1yI8CbBFI-OijrVl-zLl-j7OvvO83NwO-sAYrBiV6PuXHvttKP9ana3CvTPESYvlvBjzvFyWONfDzz633IhOCrFBf6kL91fjMOo2T2IzzS07WNheHKlhW8vlaASoDF2Nif4JZyZu8iESMuilnrBKPVVHda6hqfx2ewkaTUMFSBwI0dl74mEZgooo-juXrR7-MklDt4-g17JjV6bJ7cizRwo9DC7qIsYOMZX-UwLfW5ySeU-PrEUe05jdI3JRvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گیت‌هاب در بیشتر نت ها و دیتاسنتر ها باز شده
سایت گیت‌هاب (GitHub) به‌تازگی روی اینترنت‌های مختلف و دیتاسنترها باز شده و در دسترس قرار گرفته اما ظاهراً ماجرا به همین سادگی نیست!
🔹
طبق گزارش کانال IRCF:
ترافیک سایت‌های پرکاربرد برنامه‌نویسان مثل Github و Npmjs در حال حاضر به‌جای اینکه از مسیر عادی و بین‌المللی خارج شود، در داخل کشور به رنج‌های داخلی (شبکه زیرساخت) هدایت می‌شود.
⚠️
این یعنی چه؟
این اتفاق به این معنیه که دیتای شما در حال عبور از یک مسیر دستکاری‌شده هستش. این نوع مسیریابی غیرطبیعی (Hijacking/Routing Manipulation) میتونه خطراتی برای امنیت داده‌ها داشته باشه یا نشان‌دهنده‌ی پیاده‌سازی سیستم‌های مانیتورینگ جدید روی ترافیک باشه (یا شایدم من دارم اشتباه میکنم).
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/iaghapour/2511" target="_blank">📅 23:28 · 29 Farvardin 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
