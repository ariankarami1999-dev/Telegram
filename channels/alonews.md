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
<img src="https://cdn4.telesco.pe/file/NRcG1nHmLvSRZ06H0EvY-TIVHVVxUU0Pozw3pu5oYSiQsfevKNE2OBVNSUyMy2mi2A870O77_Z8_tWL6QlzRlxdmvZe4YqPR0OLQdKW3GyzwF9wbYTpgYtCcFQIrlXycgscYqRvu9KiJx0kp9R_sUoDr9MDNRiNTx13-veqMito807GYQUAxc4TfaOXpb1tkEgP5ungTV5g34jnJp6DjHaSc_JvMAsuruHUcrWY9V9-6i8wE8-KoLSGdiUx9CUJMzeHW-njyWbnjjIZa-0SbN7fS8L-_tQNRvlhQdBXW6ZPaokZblfYsSptyJwPyG2ibPUpNiuIsapyuGvrYxHWuFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 986K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 19:37:34</div>
<hr>

<div class="tg-post" id="msg-139870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فارس: از زمان اعلام آتش بس در غزه، اسرائیل ۴۰۰۰ بار آتش بس رو نقض کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/alonews/139870" target="_blank">📅 19:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139869">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بلومبرگ: ایران بارها به طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در عملیات پاکسازی مین در این منطقه حیاتی که مرکز حمل و نقل نفت و گاز مایع است، شرکت کنند.
🔴
با این حال، در جلسات خصوصی در هفته‌های اخیر، تهران موضع خود را تعدیل کرده است. این موضوع توسط دیپلمات‌هایی که با شرایط این گفتگوها آشنا هستند و به شرط ناشناس ماندن صحبت کرده‌اند، فاش شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/139869" target="_blank">📅 19:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139868">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دو زمین‌لرزه ۳.۹ و ۳.۵ ریشتری هرمزگان را لرزاند
🔴
نخستین زمین‌لرزه ساعت ۱۶:۱۰:۱۴ امروز حوالی سردشت و دومین زمین‌لرزه نیز ساعت ۱۶:۲۲:۱۶ در مرز جزیره قشم، خلیج فارس و جنگل‌های حرا، حوالی لافت در استان هرمزگان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/139868" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
فرماندار ری: آتش‌سوزی در شهرک صنعتی شمس‌آباد اطفا شده و آتش‌نشانان در حال لکه‌گیری هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/139867" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
یک مقام ارشد ایرانی:
رسیدن به توافقی با عمان در مورد تنگه هرمز، در صورت توقف دخالت‌های آمریکا، امکان‌پذیر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139866" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139865">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
انتشار گفت‌وگوی مهم پزشکیان با مردم عقب افتاد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/139865" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139864">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
یک نفتکش هندی در جنوب یمن هدف شهپاد قرار گرفت و در اثر انفجار غرق شد.
خدمه کشتی توسط گشت دریایی یمن ( مخالف حوثی ها ) بدون جراحت نجات یافتند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/139864" target="_blank">📅 19:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139863">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6wWO974Pry9q7BszH10DrGqNJT3aaxtf9pVFHwowYPS4IKjCfy50yAMqIEv2DCPd__de2EGA7-DkyslreQoYp-hmhmLvg6Igj5IpA-EpplltFOU_0a6eylbYrqyBWv25o8Zwu9DcYZbyehzJHHKFO036MDI_JwfzhqdonWI3b93QDqkmMODYT4c7WIqjxeDnMV0RI3HUm5XDvYO19_Ndeo3F6RGfC4MgLXwDvj_y9r57ufV-gklbbDS_6mP4NncL7euSkVsAUZymiE77BUJnz5Hf3E5tZOe2NBYCIRBRbJN1DX21WyVw2_-83EfASGynBc4wMHZ-U6yA-FqK2tkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاتریک وینتور، دبیر دیپلماسی گاردین:
‏ به نظر می‌رسد عمان، تحت فشار آمریکا، اروپا و عربستان سعودی، در حال پذیرش مسیری برای بازگشایی تنگه هرمز است که تا حد زیادی با ابتکار ایران طراحی شده است.
🔴
‏ بر اساس این پیشنهاد، مسیر عبور کشتی‌ها به گونه‌ای خواهد بود که ایران همچنان کنترل غالب را بر آن داشته باشد و کشتی‌ها هنگام ورود به تنگه از آب‌های تحت کنترل ایران عبور کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/139863" target="_blank">📅 19:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139862">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLgZypHaugXaEG6xUKi0V2C64kvXDSd5hmsSX8VmYk_211YF8U-g7arpzAEiFBUp6tVqTvTZs9WculUxOgsqXaSHI6RXdapW5-mZMKhJU2WEOmTZN9y0ERYkduyLz25SR5qP4QiH6Bm0f55fY8rFMcw4rVk6CWsYAhldcCq9A2LeG8F1m-MtElpF55YQBV0lvTJ2KpVmKSdCQcD8U9O-F0AEQL6eUdDUhpXKetqHMgzGdS721z8UqZp_X__zJfnzUj9LTwXg9lrrQYgEnk3RkewB0pARbZHAvzecFqOaZq5wEvbPnq8fLljyt5N7ByqIXQdlk1ynp5g6LLb-vTfb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کشور رو هواست همزمان عباس تو کربلا:
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139862" target="_blank">📅 18:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139861">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش عربی سوریه دستور تجهیز کامل تمام نیروها با مهمات جنگی و افزایش آمادگی رزمی به بالاترین سطح را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/139861" target="_blank">📅 18:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D54dOlYS6hMLlWK-KjYTUCXFGVC_uADCWcVY2GBdoNgFdoXIIeJVaghdJHGwa_aqrPbfJHisjm0WGBDbc6f10L94FJt2dG30xzaScyB23WbQiSGL9saxtdCYOJPlEEiG4NVVokCIlMsve2wGfZpqMPU557v1aQozHd1cSsSSyl829_BuyTRfW88Rt33J0rdG1U8wm1EiPpy7SeB1Ehlyt3Tu_AC1C977mUVl9yAypXiYNSNx75c-sKdozx96PTuh0yzOIho3mG2ZSf-hQaIi9CmhfilPqXIDFzWdT_7nRsQEx1Zo3hf2wQn7W6MUr8Y4DVoMP2SLnfpzJtvaZ3mMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: "توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران در مورد خلع سلاح هسته‌ای و تنگه هرمز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/139860" target="_blank">📅 18:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: افتخار من بود که از سناتور دارلین گراهام نوردونه (خواهر لیندزی گراهام بزرگ و فقید!)، از ایالت فوق‌العاده کارولینای جنوبی، در دفتر بیضی شکل استقبال کنم.
🔴
ما مدت‌هاست که یکدیگر را می‌شناسیم - او فردی فوق‌العاده و یک وطن‌پرست واقعی آمریکایی است. لیندزی یکی از بزرگترین انسان‌ها و سناتورهایی بود که من تا به حال شناخته‌ام، و خواهرش عشق عمیق او به کشورمان و ایالت کارولینای جنوبی را به ارث برده است.
🔴
در جریان دیدارش، از دارلین خواستم، به خاطر کشورمان، در انتخابات مقدماتی ویژه جمهوری‌خواهان در روز سه‌شنبه، ۱۱ اوت ۲۰۲۶ نامزد شود. او پذیرفت، چرا که هیچ‌کس بهتر از او برای گرامیداشت میراث برادر عزیزش، لیندزی، وجود ندارد.
🔴
دارلین، که از خانواده‌ای کاملاً فوق‌العاده می‌آید، در تمام زندگی‌اش یک برنده بوده است، و از حمایت کامل و تمام من در انتخابات ویژه سنای آمریکا در کارولینای جنوبی برخوردار است - او هرگز شما را ناامید نخواهد کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/139859" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139858">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بسنت: همین حالا تعداد زیادی کشتی درحال عبور از تنگه هرمز هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/139858" target="_blank">📅 18:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139857">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqTCrNhvkd9-exFaUdrHT_svDpS-HiJUfFx9NMFA_ccPZYqGnzU1jytnN1FLFni_9tvyf_dNdwHgbhONl8_jrnUA8pyBAYfObKVdmpn-36PqXDq8Uj-3oVxKB4OUsidaQwvdkGuQ5BHgZ6CPO0pUf8ybHGY5gjLoD5864oEj__KoTfwd5mYy3mzkihhZzi6GQEC1AgJaqZ3UScogzZicdYqMvIqtsHePUS4wD0msTCRFBTf7JW-dx-j7KMFBK9sXxKEvgLQ003sNBsfpcgeuXumNJE8ZqmF4u9UTxG5EbtwN6WQG2nFVTAGFvuTHVep37OunH0BA-B9LyXTzq4cmcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووووووری
/
بهرام یوسفی فعال اقتصادی نزدیک به دولت مدعی شد توافق ایران و عمان برای  بازگشایی  تنگه هرمز حاصل شده و احتمالا ساعات آتی خبر بازگشایی تنگه هرمز از سمت مقامات  ای عمانی اعلام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/139857" target="_blank">📅 18:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: فرماندهی ارتش طی ۴۸ ساعت گذشته سیاست حمله به غزه را به شدت تشدید کرده و اکنون هر عملیات هدف‌گیری نیازمند تأیید شخص رئیس ستاد، زمیر، است.
🔴
سخنگوی ارتش اسرائیل هنوز در این باره اظهارنظری نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/139856" target="_blank">📅 18:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139853">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KMjspa2OZkILfe0dqIKCmT9JTL6Zh0M4fss9qTtAEALa-qj6XIQYzMV3KWnB0Uv8RSuirGZfcbRMby2Tj5Y5RVIWRS7Z-0ankvB_QEtz1hTZ72lH0PDMMbP50xNZQlvMIopPKWvZf2hww4oX9f0WLVLXvFHNl5ejH9AYvNaw8oJ5jknbOeDezzhYMiUQ_fzoefoXUZuysA112Kl74LqZEufv1D-KY43QxaFqK3qt9-qUSqFzsF6ALQAoOUF0gb2zJIk7hJr_3UJ42f0JqgpilgE3sFD0DcpnSlJQDfnnfM6YwXQE7l2uS8RtIefCKsYh-CUYKsDUMOXRJ7JcyDMbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K1vNuK547ohzTmXJWRNK2wzFi_yNHHZrPheZcSShxKjlOjYmdSiPKOEWr98zNpWhO8dZRkQp8A1WzstR9eBE0SREtumhG5UtWizrr7ewb-kTkLnuVAAURvGOY8RmyUauCVx52Xpmly_4jIAK52HxWKJQn4i_HRVndtxbzZSXx7exogBDVfUHuvArasFWLrSDpKl5ewKo9h6upZpZCdzJ0sxXdB14fJYHtifgrZZUNLgvHuOmmWeoik1xohxeCANzcILaebqroZZXmt_CZ74gszTk0ejiuCjR6LlGzgrPORy1CvXGA1_U3QQVURFT4YcheNP5eDjiUWIZJOc6OWq4dg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b73abb732.mp4?token=UjZoQ68veQwhzPSdRTPb7EtA1R2ieh7Kyvlc6ZZhTCPj677OcAaMg_i1H4o3shr9kwYUg0TXm-mS-T5Ng2Zo31-QGP9VkI8y1j2hKcRbxU-XIj-vfHHfsT1wN02Mpsb4YS_nbRw2xblLtE_7VhIddDOMnO-tKBIQ1REGsSEwai5bC4pD6UHy2XMbpuzfB3gNfuB7UB9eBxZL80IxpbniCXGsOjaHRVCBMDTaXSh65ElYoo4XgnvuOGa6UIJ-rXtC4SAqOgHYQuQrwc5Vma1JivAwWKRWC4tT5ob4g36aHjTbrsSU99PhtnixB4kATGdDsIlgz0jHep3ltA7hU6VsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b73abb732.mp4?token=UjZoQ68veQwhzPSdRTPb7EtA1R2ieh7Kyvlc6ZZhTCPj677OcAaMg_i1H4o3shr9kwYUg0TXm-mS-T5Ng2Zo31-QGP9VkI8y1j2hKcRbxU-XIj-vfHHfsT1wN02Mpsb4YS_nbRw2xblLtE_7VhIddDOMnO-tKBIQ1REGsSEwai5bC4pD6UHy2XMbpuzfB3gNfuB7UB9eBxZL80IxpbniCXGsOjaHRVCBMDTaXSh65ElYoo4XgnvuOGa6UIJ-rXtC4SAqOgHYQuQrwc5Vma1JivAwWKRWC4tT5ob4g36aHjTbrsSU99PhtnixB4kATGdDsIlgz0jHep3ltA7hU6VsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز 13 ام مرداد، تولد جهان پهلوان، جاویدنام مسعود ذات پروره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139853" target="_blank">📅 18:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139852">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نشریه بلومبرگ گزارش داد عربستان سعودی از طریق میانجی‌های عمانی در حال گفتگو با انصارالله یمن درباره برقراری آتش‌بس و کاهش تنش‌ها است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/139852" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139851">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptQKZ_82uXNaxHRVTW5L6qw_I9GgrgcAYxvQ5yce9n-uWXWeao8uqlkb7PcZWzPCi3QJQ82ZQG3GIAU7_Q4AZFiGw60F-e5rUIZVC-EGTecy6Hu63YSQui4x1b9b85MvP6EKMuUqr-_4kbL2P_DUvTuWPegrgbpYjGodspmR41esSa5bJtA8TV0S5JP3K1aDHI4pG77iXWXyMLQxgI0XQEISMZOfFZWYsmjrvm2E90hL0-8lPxY4biFxg9Vo8RMaCRi-iwb_BoFOhC6Ida2UsubmIdFuFRrTaTnYa5ueGQUX9L08wcRgSIRgYdf1iYcust3xbLl7EYTkHHsqKcycJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
توییت ضرغامی درباره جنتی
🔴
خودت استعفا بده و به نظام خدمت کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/139851" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139850">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
به گزارش فارن پالیسی، گسترش سریع تولیدات صنایع دفاعی در روسیه باعث شده است شمار زیادی از نیروهای کار از بخش‌های غیرنظامی به صنایع نظامی منتقل شوند.
🔴
این روند رقابت برای جذب نیروی کار را در شرایطی که روسیه از پیش نیز با کمبود نیروی انسانی مواجه بود، تشدید کرده و فشار بیشتری بر بخش‌های غیرنظامی اقتصاد وارد آورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/139850" target="_blank">📅 17:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139849">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
روبیو : روابط آمریکا و پاراگوئه هر روز قوی‌تر می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139849" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139848">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
روبیو : تو مذاکرات برای بازگشایی تنگه پیشرفت‌هایی داشتیم، اما هنوز به توافق نهایی نرسیدیم
🔴
امیدواریم خیلی زود به توافق برسیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139848" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139847">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
روبیو: اعلام توافق با ایران در مورد تنگه هرمز می‌تواند خیلی زود انجام شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/139847" target="_blank">📅 17:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139846">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
العربیه: بیانیه مشترک عمان و ایران درباره هرمز، طی چند ساعت آینده اعلام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139846" target="_blank">📅 17:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139844">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f3aBfOEISWOO4CncoEDWEHEdrDzViXwD1X8ntXMUhr17JipbE3HEBcLfzb6DIlPHZdaIfT4Mtd1QQcUBq6UUST1cPzzkKc-lxfBJdMtHcVYSp4-dleo-k-HqoeRIOiP2zryggxJm2bQad20yXhpfl_xMqPJ-YklmNej9fziaW2fEjXSPvma6i2jtO3EoYSFr-7JrWnDuD_J_fEj9cO3INcefPXmBdcEhwGDzRw9jeC7Yhl3Tpo6FW13kSyJsAZuLM6sPooUMd6PW-MhOgm8x8mPHvBA2iRdDha4dC_7Nalabm7IA4zv4XkGv3wf-P6M5KBzXwoQPqyryKZjHYpaVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QFxzx5MKGLaHX468am9pHm6_8Lye_RQJKis90o_sPvYahRnCh0-H7QNsHasZJnN2JJY6I7-XsCBau8lJqJ8dKU5ywj9U-DaSpk8504__cdve1D-vWy5KDRLVIM1KxOy58a7c22x9vPJm42SzkGQy9VY9uZQKyWAH9-nlbChYU3aHGcQ57by1zk9fngW3WZppei50D3oorQ2bLF2GrWZXwTnSpgsoj_3yE8eKm8jsCKjWOGY-YjCgzNdRiaEuUlrI_w3BrhoDnNtaGR3VEjaMZHh40WKVs_Nm-t5WrFDEhyZ48F3hpy4Og2LaNusZrKntIw_JzcIbUfFjHLun8O2mPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یک هواپیمای آمریکایی امروز از پایگاه هوایی اوسان در کره جنوبی به سمت پایگاه هوایی عیسی در بحرین به پرواز درآمد که احتمالاً به دلیل کمبود موشک‌های پدافند هوایی در بحرین، محموله‌ای از این موشک‌ها را حمل می‌کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/139844" target="_blank">📅 17:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139843">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
الجزیره : اعلام توافق برای بازگشایی کامل تنگه، ممکنه تا چند ساعت دیگه یا نهایتاً فردا انجام بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/139843" target="_blank">📅 17:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139842">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
یک منبع مطلع به العربیه: احتمالاً طی ساعات آینده یا فردا، جزئیات مربوط به بازگشایی کامل تنگه هرمز اعلام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139842" target="_blank">📅 17:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139841">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شرکت تسلیحاتی «فایر پوینت» اوکراین با بیش از ۱۲ شرکت دفاعی اروپایی برای تأمین رادار، سامانه‌های هدایت و دیگر تجهیزات مورد نیاز پروژه دفاع موشکی «فریا» توافق‌نامه امضا کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139841" target="_blank">📅 17:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139840">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_exWetlnRXFBDs7HIPkWQymQsCnYXrPcuWN9idWlPUx94wfN9Xi8uT1AelS-rBUilzzFzONCQP89nq3H1AxfuyKB2WsLPFX-huwXqQcsVTm1XYUW63uRgQbeVSu57ey7PBoF7LtikOmpzmD9t-w_5I9Yslm1PUOd7OmagitrReFGfcSp-5neiE2T0Pe8ET8L5R3oOdN3146et6UaEBwyjPzTBBUy_E33OFCiUCTNDBU8BQRn6fULq7LM07IvOhHtVjuPf2bOA2V8u_uIVWw8IeFH8ug0-HvGnJOC8b5An3RWIhFlMa3m-F0GTZpSf9L6cQ-8bbQ9CC7Qgou374wuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تایوان: همکاری نظامی با آمریکا فراتر از تصور است!
🔴
مقام‌های تایوانی از گسترش همکاری‌های دفاعی با ایالات متحده خبر داده‌اند؛ همکاری‌هایی که علاوه بر فروش تسلیحات، آموزش‌ها و تبادلات نظامی گسترده‌ای را نیز در بر می‌گیرد و بخش زیادی از آن تاکنون به‌صورت علنی مطرح نشده بود. این موضع‌گیری در عین حال پیامی به چین تلقی می‌شود که نشان می‌دهد روابط نظامی میان واشنگتن و تایپه همچنان در حال تقویت است.
🔴
به نوشته وال‌استریت ژورنال، «ولینگتون کو» وزیر دفاع تایوان تأکید کرده است که سطح همکاری با آمریکا «بسیار نزدیک‌تر از آن چیزی است که تصور می‌کنید». به گفته او، این همکاری‌ها تنها به تأمین تجهیزات نظامی محدود نیست و نیروهای تایوانی از طریق تعامل با ارتش آمریکا، تجربیات عملیاتی و رزمی ارزشمندی نیز کسب می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139840" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139839">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUX2S9Y9qnAylkEeVcwTz9KQF5P1GeAVUYNt7dmY9lXsy_4ROCF4qiFaycf73E8wKrfIguNb3E34PsVIDv4clC6LlV7aG5aitxdi5R7W0my6jk00ymihz4bnx8Kji3udyT0kQz1OWD3EPut_kHXo5YzMyaeIbQEqNlMvRPy3zqEfPQQSytHVD3n0kppnzk24l_sdyjlGJg0RL2GvJ2ifUufyjRcIygCbem4GFKbWcld_3bOMm0qNJbvjsI9DFuB630ZVtFLXmgsMFUI0gi6iezZaOuuUplkbtaVfKIn0VDpEad9R5aY4FxEnmh_LYQPWkbi8vBOOyLusITWEQ_7KQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط نفت برنت به ۸۰ دلار پس از مصاحبه تلویزیونی وزیر خزانه‌داری آمریکا و اعلام احتمال دستیابی به توافقی جدید برای بازگشایی تنگه هرمز تا فردا
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/139839" target="_blank">📅 16:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
شش نفتکش غول‌پیکر سعودی، خالی از محموله، مسیر باب‌المندب را تغییر داده و از جنوب اقیانوس هند به سمت آفریقا حرکت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/139837" target="_blank">📅 16:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
رسانه‌های انگلیس: آتش گرفتن قایق حامل ۱۶۰ مهاجر در کانال «مانش»
🔴
رسانه‌های انگلیس امروز (سه‌شنبه) اعلام کردند یک قایق حامل ۱۶۰ مهاجر هنگام تلاش برای عبور از کانال مانش دچار آتش‌سوزی شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/139836" target="_blank">📅 16:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ویدئویی از عملیات جنگنده F-22 همراه سوخت‌رسان آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/139835" target="_blank">📅 16:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
روزنامه Izvestia: آمریکا داره با سردر‌گم کردن تهران زمینه رو برای یک حمله غافلگیرانه فراهم میکنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/139834" target="_blank">📅 16:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139833">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
امارات متحده عربی ورود همه شناورهای ایرانی، از جمله کشتی‌ها و لنج‌ها، را به بنادر خود ممنوع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/139833" target="_blank">📅 16:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139832">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA8wYEzk3EQGA4dM0iXUqhhvd8UC67UulAqD09KAXxJUb3h-2EN1M39rWMHjRLFO5SN2XtfRli-0hz3alHqjGvpgQXcKpgxB03hCu_kyXQKJjU_lST6IPJu3bJ5FW838Yh3Mkozzr_BmoUAZBCm3JqH0PzqG-07qypmDHLBl81uGd1Ib3HyDKUjDKatB1b-_orXs_fc9nVP2Ry6lhGQdZugMq8vEEJpY8hS9UpIi9hOV-dvLa8UhqX_7FRCa2yUP7s8LTE3HhGrZDnYJl6xAzKanvujw2OFm3konuKTFyZTbUWqtNSqVkuyPIMxP_H4FsLtC5qqpXZ-d2reDSPluIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حسن عباسی:
سال 73 با امکانات متروی تهران، در جزایر و سواحل جنوب تونل زدیم
🔴
زیرِ جزایر و سواحل، تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139832" target="_blank">📅 16:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139831">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EguU5f4xO3oA2CR96wrFjprjK8inu5HWMTHW3vO4w0Tbs13tDqg19geZ-tElnho0S_mD5DqpBuz3jduU1HfEzYYUgTvEI5-lpdXI4D5RgWhX8PSrZE9Ue8AImHQCUWl7q04m9i_oQBuGAvqiGz4NDi90Fkepe_l8VXohEbw2z0jY4UuMrjVpDMnJc6YVGpvYzGpvDw7LBrlpJPfvUj4-K9PZ2mWtXy6fmQu7-ZjX5Kq3Gw_3XWeUm0uj99et80noH62JYLNGHkISksqyBP8nKHn-Q1DXyRwgcDfEBOJBdqn9RN_1Iz5eBFuVJbXgG1kbdgs_EXwKiAvVOE4xG47Isw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : وقتی با رضا پهلوی حرف میزنی، میفهمی بیشتر از سیاست به فوتبال، غذا و عکاسی علاقه داره
کاملاً مشخصه که او ویژگی‌ های لازم برای رهبری را ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/139831" target="_blank">📅 16:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139830">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7UsZ-JJj7gRlXCxtr09rt3KRMaekVE9uPkJtMDF4apY8q52HjPeSW1nULtHx_n81r8IoWJrNzdxco4CwZrBkW5ofnnL_WmXjt4ykXFoGBoDkkK5Yqbb7bkVKWPMRU9387Zv9lbaNGFpIKoEY-M5seAWW7ZqiwDpyk1_m-SjD8mEZUUVKFZEPDtbXbObnmPjma0A-qqTin0NQfOCPL5rUkIGIOyQCZwv8dXez8slQKB2Uuqt8-rQjbFLGa5OXDmhVLNVjV2hv4EIAtjsSSuNMfb3eq0Jx-2XSIqqIqUK4yxcrJn9iLPE5uy7dEU_LE8rangQaN5mV01exO6ENbHdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۸ نفر بر اثر انفجار در شهرک شمس آباد مصدوم شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/139830" target="_blank">📅 16:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139828">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=R6mmVgszfTcz0hHzCmxGKUmNTzelwx59K2P7Tf3svMqhqkiD8CClcUTFH4PLJ22cMV11h-QgAzHPb6AuB2dQK0NDhnPC47K0Hp-eruDQtHzH7pu9h9bgkr5RNXokjAE_VSNNZ28Fdc98Ql2P1lZLVfVkuoNsBNU1LAc-h3NCVZYFqdUaVL_uuzuuCOoqeaWOjxBZ0aoJkubz3nXaKbW5QIDq8wvd_vn2xu2-DApAkZnCxylDMhUxTAHab1N-xhirEqtjWrME_aHIQC7BtX2kFW6x6k6Tzifs1lX0sQZva4Ck82uLSYEgB_iKO_uK9xWXFM2ydMb7RkccEyI46xLNfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df5d5b7fb.mp4?token=R6mmVgszfTcz0hHzCmxGKUmNTzelwx59K2P7Tf3svMqhqkiD8CClcUTFH4PLJ22cMV11h-QgAzHPb6AuB2dQK0NDhnPC47K0Hp-eruDQtHzH7pu9h9bgkr5RNXokjAE_VSNNZ28Fdc98Ql2P1lZLVfVkuoNsBNU1LAc-h3NCVZYFqdUaVL_uuzuuCOoqeaWOjxBZ0aoJkubz3nXaKbW5QIDq8wvd_vn2xu2-DApAkZnCxylDMhUxTAHab1N-xhirEqtjWrME_aHIQC7BtX2kFW6x6k6Tzifs1lX0sQZva4Ck82uLSYEgB_iKO_uK9xWXFM2ydMb7RkccEyI46xLNfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
توریست ایرانی پاشده رفته کوبا و زیبایی های کمونیسم رو به عینه تجربه کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139828" target="_blank">📅 15:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139827">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
کاهش نفت و افزایش اونس طلا بعد از مصاحبه وزیر خزانه داری آمریکا
🔴
ریزش 5 درصدی نفت برنت به زیر 80 دلار.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/139827" target="_blank">📅 15:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139826">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا، در مصاحبه با شبکه CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/139826" target="_blank">📅 15:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139825">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139825" target="_blank">📅 15:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139824">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-C1o7NS2DGod1JnlyMuX2Zl2pTvIIqh0fdcVB5CornlIFSNrrPKofL7v5iHD86XZK44sZ1MVT11qw1YcoPhsPCOIC-CHG1BSC8OPvpCfSWW-WrDE7Zs0sbuZFpJ82HC6F8x3LhXRH9D7WiaL9VigKqOFaZzZ0T2s35fucrmMit7TUJEZ-1H1ZEzUbvRYRywMQk-gP6o4gnQm48e9JaTMNFzXuER3SbX9KImmHraqsHEAHNLHaw63XP5oSGr07px_N-8KcxsTyEbKkvEN2-0wlLF8vEyy2W6kfS5R11D3pfluMuHAe32P3gdudON9x-x49LGekUNNAUwQ3VTCaOhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
العربیه تصویری از کشتی هدف قرار گرفته در تنگه هرمز منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139824" target="_blank">📅 15:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139823">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vi29nO7snJmg4p-r6ffXnXPNLU532RKfuMfjsGo__Ik3vCuSN-Vm6_yyS6TAYOD2m8jd6V3vW_38_5a08ryoanMoyq5dq2ymwrd_tmWnkrC3k_6fTUohAOnGpC0AWkCeHnKBdbeaUbcyTUgMAygQnKnrvhYIgW_szf06Xe2o1i_8MgBXl1V7cOB6Ii8GF5gkqeZ0WqzKFCoqbOhMapfI4BEM7WcIg7O3RXGWe8b9f4GE6cowB143NAGC5V5G5wHPEKSxxc3Ri5vVvbjAjcVgZs8nNQzL7aU070-4T1Ldk-_prbaEkNgxreEdau7mDpwgpV4EYyoBmoD3QLz_r5Oy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: ترامپ تا سه شنبه به جمهوری اسلامی فرصت مذاکره داده و باید تنگه هرمز رو باز بکنن
در صورت باز نشدن تنگه هرمز ایران با حملاتی ویرانگر مواجه خواهد شد
✅
‎
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139823" target="_blank">📅 15:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139822">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpFgpi42Y7bsdpfMrOkMfJOqSnmDYiff10Nzfi-JxAlHj-Q57UAxSoW6hAQigMqQ0yBeahpupQBD_KvCEoOK-GI08DtZjSK1vEDn6yYbBUWwWdaUXhVYnjox84ebguKSdhoXOyEA3JzVT8ACOYnNWRURG2J7agP_VCuLqofHZrFWceMAjCB8EJrpoMcdrCR3k0XjzydACVVEGOfatEtRr6IerTh2BrQwDEfO3fF10jkbNn1uoTLBl_jkzyxFpdOQd9FEaY3i7V5O5ZmCjjYIog6a3enVpDCU3cA1geK0ilQKbesbwIdn9c3wulmaHQBeVhAI5o9LIDS2qZEEdBvFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پراید در سال ۱۳۸۵: ۶ میلیون تومن.
Vs
چرخ فرغون در سال ۱۴۰۵: ۶ میلیون تومن.
همین برای توصیف اقتصاد ایران کفایت میکنه.
فقط طی ۲۰ سال.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/139822" target="_blank">📅 14:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139821">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
قطر: متن اولیه برای یک توافق  آمریکا–ایران تدوین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139821" target="_blank">📅 14:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139820">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
قطر: متن اولیه برای یک توافق  آمریکا–ایران تدوین شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139820" target="_blank">📅 14:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139819">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
امام جمعه ساری: بی حجابی سبک زندگی یزیده، سرباز یزید نباشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/139819" target="_blank">📅 14:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139818">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
جمهوری‌خواهان کنگره آمریکا برای ایجاد اجماع میان اکثریت شکننده خود بر سر «قانون SAVE»، بودجه دفاعی و چندین طرح مهم دیگر با چالش روبه‌رو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139818" target="_blank">📅 14:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139817">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
زمین‎لرزه‌ای به بزرگی ۴.۱ ریشتر در عمق ۲۶ کیلومتری زمین، کهنوج در استان کرمان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139817" target="_blank">📅 14:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139815">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zng8-TX71e0HDAMgWRxEIOkcu33IdxFJMTWGMaxlcIP4FHJ0sSNLoS-cAsyvM_yrUqiEpY2JjJnkPuEvcXBkh7L-PZXIltepXh8pVpev7-gPHOYDpaF5IFZCEq80VVICB4bPT6ekBpOP49hLog3h85Im-uc7ljDs2kVy85k4FhDv2RpUENndTvGeeIpF92_7EGLx5v5tu5k5waHUs3L_cUs0t651MJLt88aXDjNyr-wnVGe8zev-9dCkrSsOvNzDwG2L4kk65c5kcCZIJqMvP1LXR2dLY2Ggt8ISzqL0ZKXC7dAxi1UIe7QKvmkTEIb_4u9l03PlGRx3uNMQbyb9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری دیگر منتسب به انفجار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139815" target="_blank">📅 14:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139814">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
گویا یه مخزن گاز ترکیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139814" target="_blank">📅 13:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139813">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
رویترز:ایالات متحده تقریباً تمام مهمات پرای‌اس‌ام (PrSM) و اِتِی‌سی‌اِم (ATACMS) را در طول جنگ با ایران مصرف کرد. همچنین، کمی کمتر از نیمی از ذخایر جهانی موشک‌های تام‌هاوک (Tomahawk) نیز به کار رفت. برخی از مقامات نگران هستند که کاهش ذخایر، آمادگی ایالات متحده را در صورت بروز درگیری‌های بعدی تحت تأثیر قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139813" target="_blank">📅 13:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139812">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
حوثی‌های یمن : با پهپاد، یه حمله دقیق به یک «هدف حساس» تو فرودگاه نجران عربستان انجام دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139812" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139811">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
گویا یه مخزن گاز ترکیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139811" target="_blank">📅 13:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139810">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / صدای انفجار در شهرک صنعتی شمس آباد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139810" target="_blank">📅 13:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139809">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
حوثی‌های یمن: یک هدف حساس از عربستان سعودی را در فرودگاه نجران با پهپاد هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139809" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139807">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qUiMVkmTkIT53QF5dGf7-mD8o22ddlYGkO-85o5qgtAzLkLQCOx7oekR4b7wdDGB97oTkaFJMl0OySrTcK5IK_b_ljF6IK9Akw3HE_6Ac0OSKcJ_mxyOfhJgO6hhvowQC_7zpGe7EbkJ62C2tmQo3lCmwVKqs3MXBBdAvXUx1Ik2GOQdppAJ680TertEzlWBwDMdG962-qvP5nagaG1v-QA59nKgD__sKi_zZH_EtPzpIH0s9Ezxr1ghPsMeQldOkIECkFxPKVwTIbj9_z8BM18iVs6I207Jm8vhTkZUx-S9ChSZ0FhdlUe3AoJbgKqNeAilIs-El_VpFZD6U3-tTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez7HNQu9EoFHGFy7RyDDc0ZBpZZhGIjHfzPesbaNqT5tesnBR-dkkXVcz89Ij2ZPXYNyDvNpHjtRHT4Yaqgo1NkLcxnMgIPC9kyFmQH6yyGpjQ8i3h36YQzHKVFAeh0_ddUiEdYT9b_Q9MJn_IWHqr_7Xx4dHmJyaS8bAo3LV6-J7NZNfBz_Zo2Lj-jnB-IQ19lpxhupONakzl6dwqGebp380MupZ7Z5sU1ks8PRfAH-CdGBOiUH_io2BsCB2e6E7vvswKUVdAjXZ9W8frGc7vQPPk6O6Jz-z-zUFiGfYqvpYNwUHQQJa0h0xs8_bRxDYWiKg-B5e9AjljPrWl6hoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی یونانی که مورد هدف قرار گرفت، در حال حرکت در نزدیکی عمان بود و سیستم شناسایی خودکار آن فعال نبود. این کشتی پیش از این، در تاریخ ۲۹ جولای، با خیال راحت از مسیری عبور کرده بود که توسط ایران تعیین شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139807" target="_blank">📅 13:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139806">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4tMBlQrw3-RlDC9z9K5WPjBByk-cheSsPLAuY94rg3urFU9cNbX-kUx_61P2VkS23o6uGHLVfvkBUM3RnPjWshqYjoxx8vXyg32keyX0YDEvzQuzn-UnXsdadgnTVvxajQNXFgS1Ubn7ZRrn7hq4uy8IKD67sDffnaVOgEYFsvfs7zuCvu46FGrqyvDE_G3XcokJKMdN2dlB_R5VRWZnCakFNNA5UCeFuTAyg7mT4s0sYSF0aOcNiV-3_M2RaIJaGOFuh7QtjdiqU6hpxOqoyDBvrEUMWWpWwnGrD8NzcojrVIxIdyGWdotG2deXEdTpYJDM5lrQkGOSVKCs_mEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعار علیه اسرائیل می داد اما جاسوس بود.
🔴
این مرد ‎إیلی‌ کوهین بود. مردی ‎تندرو و مخالف اسرائیل!
🔴
اما در اصل مأمور مخفی ‎اسرائیل که تا یک قدمی نخست وزیری سوریه رفت. در مجلس ملی سوریه فریاد می‌زد و اسرائیل را به هزار کار کرده و نکرده متهم می‌کرد، اما شب‌ها، برای اسرائیل اطلاعات ارسال می‌کرد.
🔴
شباهت نداره به بعضیا؟
#الی_کوهن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139806" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139805">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dArVkYrTauud3NcgkgzHwwrWcPQJrsSxS0Z9C8iYSGqvobHVzjvrwFW6VmKqVCNFDQcWWWBvaiWCFB9qJ7dCoCQw6uql5Xxt48ozHvcNn_cgT5XRZUNAz2O7QER2-xGAalRszkRs9WyAuKf-pK2uJTdtgCbisXq2XSDS0juJbP97wHPnzPzClKUJSZ9vdsJGUQX2KGMHNU7WiOAanX0gUpDCNISf9C5VS4eiMbJASWTPKpBYhYVuOet3ytca_VCM5ioY07xGEwyAcyMZ9kS2tmDmMDDnn5o_EnBGy7jzoneSuBLUROH4bSCtvo8jtxg1q72ZtGktqmMcHG1KbtEUdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اظهارات عجیب محمد باقر خرازی: تنها راه نجات ایران ساختن بمب اتم و زدن بمب اتم تو دریای اطلس و اقیانوس آرامه طوری که تو آمریکا سونامی بیاد، هرکس با ساخت بمب اتم مخالفه با اطلاع بهتون میگم اون دنیا باید جواب پس بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139805" target="_blank">📅 13:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139804">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
دونالد ترامپ از ایران خواسته است حداکثر تا روز سه‌شنبه بر سر تنگه هرمز با میانجی‌گری عمان به توافق برسد.
🔴
بر اساس گزارش بلومبرگ، ترامپ هشدار داده است که در صورت عدم دستیابی به توافق، ایران با حملات هوایی ویرانگر مواجه خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/139804" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139803">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIwMUoG7cLTmb0fziypH6-wHZjmRh2iq9WBem1KtnRCpbWSYW2BJdKasQkzJ7tJGoITjvMW_38S05BbgAfX-DGpmMGzq-rCoj8TjsmuYWr9WjxK0aye1_1Tog30GAqSRcl9Om5n87szDMKbNDgcEGZRK5I2R2iw8qXu-B4ZVi5xjtmP-nvHe6M7zvir0fUXczS3SQ6GM3TooaK028VHbD3ebUmzN0zqsEHpoLJL9b93wsNOhruc84Sq-oYjTTTEc7VsvZaFW_HUgCMWB_ErnGvY7UaTbt93PkwjNqoKC2X5isfv7honLdqEWNg1AoWaY2WdvXMMTKw1RKlmz67X2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / صدای انفجار در شهرک صنعتی شمس آباد تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139803" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139802">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
رویترز به نقل از منابع امنیتی دریایی:
یک کشتی باری در نزدیکی تنگه هرمز مورد اصابت موشک قرار گرفت؛ خدمه آن کشتی را ترک کردند و یک ملوان نیز مفقود شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/139802" target="_blank">📅 13:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139801">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نعیم قاسم: رهبری آقای جدید(مجتبی خامنه‌ای) یعنی پیروزی‌های بیشتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139801" target="_blank">📅 12:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139800">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نعیم قاسم، رهبر حزب الله لبنان:
دیدار بین حزب الله و دولت سوریه هیچ مانعی ندارد و این دیدار در زمان درستش بر اساس روابط دو طرفه انجام خواهد شد.
🔴
یک سوریه پایدار منبع حمایت برای لبنان است و یک لبنان پایدار هم می تواند به ستپن استراتژیک سوریه تبدیل شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139800" target="_blank">📅 12:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139799">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7yEYJm0fhlBGJVX-hnvOk3dtZWTYVoTMwFSyGEeCCkQUrPLVaKkAHo3xNODL3pvkuXb72jLbFSauX5ELn79fsABrOsvbmNXqKE9uDgmitQygWMjq0v5-p2xBZz8f-BdjDmlK3pQnZwjpo-o9eFtvjm5K0yTmbn32EbsmhS14NlInTdMKRxQmw6Ycj9UNdJgP81IEO8D9mqVlo-6xobILwNVti8HHo5Q9nIvMHmD8v-UW7fCcvHOJqD1ETAsxa80ex7CMMv1AsHYdP5JKwbK1gBC_YZKpCACOLNbmdQkRJmm32s61F0usuIdv6wp96lNzMwnch5gm312LRouNTMD2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اگه‌ توی گوگل سرچ کنید «پدر استعفای ایران»؛ با همچین شاهکاری مواجه میشید.
✅
@AloSport</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/139799" target="_blank">📅 12:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139798">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a783e28.mp4?token=jKEZhGHt9pjpUtIZ9hC_WplXEr9OQfQoboNviQ55s_NYc3PXhFngqtgnsKIcdBhy1uxgpZwOfNoELRIhua0Jt5FtFwxhM0xYwZMg33BgFHJC_S110p-hUjZ4xHSkhaRAluZ6NJJw-e-tEuizByCvHFUOUlf7QfoO8yiwBjmGYKVx8jCITdc1QC3_VX3e2vAPMTzQXllcOBqE22ZgYGDx2jmLfHxDr4Gcf-x63W1RZVRddX4a0fyt9VnjtNzuAEXw-0hfJjSV0SmjFxJbOtL-rZ3PidOLpGZnH_M2Q4q70ULaOa8fCmJYxoE_knv4srmuVwsZPLobGgF3qZeoRLB6_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a783e28.mp4?token=jKEZhGHt9pjpUtIZ9hC_WplXEr9OQfQoboNviQ55s_NYc3PXhFngqtgnsKIcdBhy1uxgpZwOfNoELRIhua0Jt5FtFwxhM0xYwZMg33BgFHJC_S110p-hUjZ4xHSkhaRAluZ6NJJw-e-tEuizByCvHFUOUlf7QfoO8yiwBjmGYKVx8jCITdc1QC3_VX3e2vAPMTzQXllcOBqE22ZgYGDx2jmLfHxDr4Gcf-x63W1RZVRddX4a0fyt9VnjtNzuAEXw-0hfJjSV0SmjFxJbOtL-rZ3PidOLpGZnH_M2Q4q70ULaOa8fCmJYxoE_knv4srmuVwsZPLobGgF3qZeoRLB6_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به گزارش رسانه‌های ترکیه یک کشتی باری این کشور در حمله‌ای که ظاهراً با پهپادهای اوکراینی انجام شده، در نزدیکی بندر نووروسیسک روسیه در دریای سیاه هدف قرار گرفت و دچار آتش‌سوزی شد.
🔴
بر اساس اعلام اداره کل امور دریایی ترکیه، ۲۲ خدمه سرنشین کشتی بودند که ۱۳ نفر آن‌ها شهروند ترکیه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139798" target="_blank">📅 12:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139797">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
جروزالم پست به نقل از یک منبع آگاه مدعی شد امروز سپاه پاسداران ایران به یک پایگاه نظامی آمریکا در کویت حمله کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139797" target="_blank">📅 12:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دور جدید مذاکرات لبنان و اسرائیل در رم آغاز شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139796" target="_blank">📅 12:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139795">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
حاجی دلیگانی، نایب رئیس کمیسیون اصل نود: هر نوع توافق با عمان درباره تنگه هرمز باید به تصویب مجلس برسد
🔴
افکار تیم وزارت امورخارجه در دوران قاجار گیر کرده و از روی ترس و وادادگی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139795" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139794">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
زلنسکی: جنگ با روسیه باید قبل از آغاز زمستان پایان یابد
🔴
رئیس‌جمهور اوکراین، در دیدار با سفرای این کشور، اعلام کرد مقامات اوکراینی تلاش خواهند کرد تا درگیری نظامی با روسیه قبل از آغاز فصل زمستان پایان یافته باشد.
🔴
او گفت: ما بسیار تلاش خواهیم کرد تا این اتفاق پیش از زمستان و در پاییز امسال رخ دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139794" target="_blank">📅 12:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
یک منبع بلندپایه به العربیه: سفر وزیر امور خارجه ایران به اسلام‌آباد به‌زودی انجام خواهد شد
🔴
درباره دستیابی به گشایشی در مذاکرات میان آمریکا و اسرائیل، خوش‌بینی محتاطانه‌ای وجود دارد.
🔴
فضای مثبتی درباره توقف عملیات نظامی و همچنین ترتیبات مربوط به بازگشایی کامل تنگه هرمز وجود دارد.
🔴
میانجی‌ها برای دستیابی به اعلام رسمی و قریب‌الوقوع آتش‌بس، به زمان بیشتری نیاز دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139793" target="_blank">📅 12:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر دفاع یونان، دندیاس : ما می‌خوایم شرکت‌های دفاعی اسرائیلی رو تشویق کنیم
🔴
تا کارخانه‌ها و واحدهای تولیدی خودشون رو در یونان راه‌اندازی کنند
🔴
این کار باعث تقویت صنایع دفاعی یونان، انتقال فناوری، تولید مشترک و افزایش توان صادراتی کشور میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139792" target="_blank">📅 12:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: رویکرد سخت‌گیرانه احمد وحیدی(فرمانده کل سپاه) به سیاست رسمی جمهوری اسلامی  تبدیل شده  و سید مجتبی خامنه‌ای تصمیم‌گیری درباره پرونده آمریکا را به او واگذار کرده است.
‏
🔴
مذاکره رسمی بین تهران و واشنگتن در جریان نیست و تماس‌ها فقط از طریق پیام و میانجی‌ها ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/139791" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
روزنامه روسی ایزوستیا: آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139789" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139788">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بلومبرگ: حجم تردد کشتی‌ها در تنگه هرمز همچنان بسیار کم بوده است، زیرا حملات به کشتی‌ها و تهدیدهای ایران، نگرانی‌های امنیتی را برای صاحبان کشتی‌ها و خدمه‌های آن‌ها که قصد عبور از این آبراه را دارند، افزایش داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139788" target="_blank">📅 11:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139787">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c173297d17.mp4?token=Q6hTTulfn8zV5ImZ6ByU820RPEl598W_GDtQyVNg1SqYyrjwBnoLr_PCvsC47ikQPmFFd-IkA2VwPnr0f1egRqA9HTnxVTMLcZUipywIMAE_v4vPmgpQIJyvlcSSnfpTq5VMFKWnP71K37nwRVuTTYLyumdpd2eteQV8D4fk0qI9TL-hfktDywCCq-z56EFDq6YyLSWMyRKR36qSELNwdCoP5WkFijrYfGkfTM9q014YjnwXyopOTbZ6rcoCYwVESuhO4xiozhJICuGu3OoR_l-vHdoibbSQfTdGZ0bUPoYmo_CYsx59Jsg_ZfTYFIrGXcAcpxAiJhRYdydjLtZxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c173297d17.mp4?token=Q6hTTulfn8zV5ImZ6ByU820RPEl598W_GDtQyVNg1SqYyrjwBnoLr_PCvsC47ikQPmFFd-IkA2VwPnr0f1egRqA9HTnxVTMLcZUipywIMAE_v4vPmgpQIJyvlcSSnfpTq5VMFKWnP71K37nwRVuTTYLyumdpd2eteQV8D4fk0qI9TL-hfktDywCCq-z56EFDq6YyLSWMyRKR36qSELNwdCoP5WkFijrYfGkfTM9q014YjnwXyopOTbZ6rcoCYwVESuhO4xiozhJICuGu3OoR_l-vHdoibbSQfTdGZ0bUPoYmo_CYsx59Jsg_ZfTYFIrGXcAcpxAiJhRYdydjLtZxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراینی به یک انبار بزرگ شرکت ویلبریز در منطقه کراسنی بور واقع در استان لنینگراد حمله کردند که این حمله منجر به آتش‌سوزی گسترده‌ای شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139787" target="_blank">📅 11:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139786">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyaqLfT6Ru8wfGD0Mg5hGxrezDOH9z7zmw_ZPkNZjkVRySoE4Q4i-Ervj0JoovMFbEnLiQMVh5wvQ1JKVfYgPqdu3hPqeiFBeHrrLcLM_21fkJ5vXlX51wH5ijcDbH1ituD5uaoPxRD2WPopDPcN9OqmZqcmdvjV28Lei4w6K4uMueHE1UquUFIMUh2qoDiAJzVHbwAGCRePDWT_aUHCO4IduLayF1bKforAEP2Homtt7ADw-txIrqVrvX3IIxdDjmX0ur6_G6KZUXsC3fVGw3b9vdKmjwRXlawi6BaXIjO8rzT6wC4ShDETCbfWy0-g4RHlcnBmelWFy3-6AV7jMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه پیشین آمریکا: محور روسیه، ایران و چین، اکنون به واقعیتی تبدیل شده که تهدیدی برای جان آمریکایی‌ها به شمار می‌رود
‏
🔴
ان‌بی‌سی مدعی است روسیه در جریان رویارویی نظامی میان آمریکا و ایران، اطلاعات الکترونیکی پیشرفته‌ای شامل داده‌های شناسایی ماهواره‌ای و اطلاعات سیگنالی در اختیار تهران قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139786" target="_blank">📅 11:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139785">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
دبیر کل حزب الله، نعیم قاسم: تفاهم ایران و آمریکا، اسرائیل را مهار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/139785" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139784">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1aa3d91bc.mp4?token=fuXVJ4QlEhhphDyZc77b_EHK7YWZ3cFieuafo9lEOV6Rx1xLN3lxAilE4Ch8A2_C1x9qBs4121JJZ_H_JJksAtF_zlNn6byvLD3yq6B-LHNv76axslHoMbeW4stbGnUSxYdEYqpi14AO11PlVqyCfSdVk1RZfqrzO3tnkWK4CgNMRvOLtg03-vGzVK5BKRFRUYrRJcMR0a7X_rPdywEVT_GTSkWVoejWz3Q0sqolTB8b3ieAiwNau5PFNadGmL1duLB70gJf1rfYxeS9O3mXH0MLXCFbgMnkt0ebGn4oee6ThpJFr2tqV_w2eZpgVZeeJ5HAJAeVV9fLhPj3_J9FqA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1aa3d91bc.mp4?token=fuXVJ4QlEhhphDyZc77b_EHK7YWZ3cFieuafo9lEOV6Rx1xLN3lxAilE4Ch8A2_C1x9qBs4121JJZ_H_JJksAtF_zlNn6byvLD3yq6B-LHNv76axslHoMbeW4stbGnUSxYdEYqpi14AO11PlVqyCfSdVk1RZfqrzO3tnkWK4CgNMRvOLtg03-vGzVK5BKRFRUYrRJcMR0a7X_rPdywEVT_GTSkWVoejWz3Q0sqolTB8b3ieAiwNau5PFNadGmL1duLB70gJf1rfYxeS9O3mXH0MLXCFbgMnkt0ebGn4oee6ThpJFr2tqV_w2eZpgVZeeJ5HAJAeVV9fLhPj3_J9FqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشر شده از فرودگاه رامون اسرائیل حاکی از حضور بیش از 40 هواپیمای سوخت‌رسان KC-135 و KC-46 در این فرودگاه است
‏
🔴
ده‌ها سوخت‌رسان دیگر آمریکایی در فرودگاه بن‌گوریون،حیفا و… هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139784" target="_blank">📅 11:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139783">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
اسرائیل به شهر کونین در جنوب لبنان حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139783" target="_blank">📅 11:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139782">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adlxQ_pxGbtzgMgM-HkDAKPL7M2aIeVtr9-JU7I3GYKu1LunsdvEOf9Km_s3O8DvoWkr98mO-d_r46ric64iMgI95IfQ5SQqZJg5TZ9AbWDKaAyh6u4e3HdcQ0xVTmNsqs0dYv7pZ6tOVw87P5A5U6tMNUTm7Av47gqxJSg5V1Km2xaEcxZp92shCXR7nG6a_JnLOzp_h_9JA6FP8FTmKhsoTKllRs8Rtxud4fGvO2sGAmlKRKY6kz8Jn3MM30l_En15STLp28lFD6uunLkiJ2j_KUmn5zpLZrT4z5SoL73--nLaLjZEyRyA4_S8sgkhtQIKK91rwT5XDWC3cs5ipQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت ۸۴.۴ دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139782" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139781">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7ZshA-X1TLs3LP3f6mJDJ45e9YeLC6D4NakYPlBcLDXNtRdqZzWh95nmSec_LUL1cK4_MCdy17KY8TSVqk4znq7B8c3iP_keJr4m9-CtRaI3KEneZTAqAzgvL-pQTmQTPQRdsVK3SBF0mXC40IGEpMHIjaSj1Wii0SDoTKS81yV8Aklm2WJX4vy3hirA_VMeP5lPZprpeGOCiJUXhNc5jZO1Nv-HSHoBBzxu0On1MwpVQ807evjYKSuuzjXEnQkL1d6Ub4fAwDkdrmWoy9zFGZvoOwF5YIIy3no2rTC-rVHwwg_bp_EXwaETPKy3hndemXh-macOsF2xoHj0zOxbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/139781" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139780">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfbXCPA68jefEhFiZrWmlW0QzN00sRhnCkGJKedz2PBsLA7nhfVVml29eJPFfs5W0Ysv06ox51I4LoZ_4ARtf6HTgzgYu8h8zqElUoAGjsGrCsWjgaWR2pEbbx2Dpribu3eqpZlYE_6cnOtAd5IBnoce8HYN3ZbtiEM35ggxGWhmKxFcu4cnFVJBZbbINh4IKCDCBeVOAU7H3twlPm_0i7BN00wgmPLC2WAiQe03yeTHq2koK_CvlQD__nzKDg5xqZtj5xvNOrB1g7uGop2N_WUD2nGACkli00VxI3p81O-BzsTPI7jI0hmaWAKOlPryIrR2fMwaIw1bfKGF5KvE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مدیرکل حفاظت محیط زیست مازندران:
یک فقره حریق جدید در محدوده پناهگاه حیات وحش و ذخیره‌گاه زیست‌کره میانکاله رخ داد.
🔴
از ۲۶ تیر تاکنون در مجموع ۱۰ فقره حریق در میانکاله رخ داده است و تداوم این وضعیت، فشار سنگینی بر نیروهای عملیاتی و ماشین‌آلات موجود وارد کرده و بخشی از تجهیزات را از چرخه عملیات خارج کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/139780" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139779">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb-8Jz7Homo5O0hZju0nEXscZh9Ykuz1cxHrQP8j3EcWHKfGOfHiKYWtuwFIXoFGdV_oSt1bvdBeayqZ5sAPDkfWkBF0rNouhTGDP_BfdMSSOftF5a_YlBdXxt_AS6ncMmietJHcmNn8fkpLNqMasUl1Dm2VJhFLO4RgLEyc3PeHlZ3DkZqHgmZ--9ehPqDDX1PX624E1-0fn_3_7XDNxoMdaeFBxETIN7HZTnmMcsqDQMALKTpCEWjqHiYgZmI1q7eC5asO4ZUBC-RWWSXXa4hPEtGgvyYxKaATVl-nw7y75E7zeiTJLH0WFRV9eNVxL-EZ1WKmEaW0BqLutsLm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پهپادهای اوکراینی بامداد امروز به پالایشگاه نفت سیژران در روسیه حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/139779" target="_blank">📅 10:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d32c2045.mp4?token=LXA0iBwwF65XyV7etwa301HLrjPtyi_lIP_cskLIGr_GeQEU_aEwOYZPpExxaK3wY0n2zaHm5HEroXpT8ulUKwMl3tgzo98UlDxsaop34Fegt-t_pVDZ9yAfIz2WVcbkL6J2spktTJ3qtBbJhJVhPFie4JF9utj1gBRUy00DDK_uo0nkeVMtpLyervi8DpDkoARcEeZeJa4SEmhA37EByVNT9kVhCkwqAljVxtM5GPb7IudkEZP38OGoQ2-uLfQZZ3kzp1zJ_AVsOkniMybmqD8o9HQ1w1rnRLipYSuhed_Mi871OUM4jCBJdsSTaBUqqYDswq6UWQz6LTWquw_Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d32c2045.mp4?token=LXA0iBwwF65XyV7etwa301HLrjPtyi_lIP_cskLIGr_GeQEU_aEwOYZPpExxaK3wY0n2zaHm5HEroXpT8ulUKwMl3tgzo98UlDxsaop34Fegt-t_pVDZ9yAfIz2WVcbkL6J2spktTJ3qtBbJhJVhPFie4JF9utj1gBRUy00DDK_uo0nkeVMtpLyervi8DpDkoARcEeZeJa4SEmhA37EByVNT9kVhCkwqAljVxtM5GPb7IudkEZP38OGoQ2-uLfQZZ3kzp1zJ_AVsOkniMybmqD8o9HQ1w1rnRLipYSuhed_Mi871OUM4jCBJdsSTaBUqqYDswq6UWQz6LTWquw_Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حجم آب پشت سد کرج در مرداد سال گذشته و امسال
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139778" target="_blank">📅 09:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139777">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ngLG6HNMMj8lIWVmVinP-TCUOeI9LHXSRP-7C1-Ad1EN9_tz_-6DeqbZ090yeEIZHpLuFDNReMIsRjR1UCKozUZmz4foX7jZOhDsHMJyzwIX2LNdmPyAWIo9mNUzrYKd5vRxAo7xOIXURs6JFMac7dWcfphCG7ZoVNOX-9wm_NSPBVGOjCDRtrqawNLJPb2H3vZOofmgcaEMYBkVBLvUi0qeXPHNqWtaXjwKl0r9_RFxoQgTEckLHazSjgoSzQUEtGS6MqfmXIZNob8FOMsO5Mn__OFl3C7YAyWqUFqYJmJFLy1IOKwHRkKvw_Wo53mYCbW43M4LLtxQbO8pwaz_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شرکت اپل اعلام کرد پس از آنکه در یک بررسی مشخص شد محتوایی مغایر با قوانین این شرکت در رابطه با «ممنوعیت سوءاستفاده جنسی از کودکان» در تلگرام قرار گرفته، این پیام‌رسان را به‌طور موقت از «اپ‌استور»، فروشگاه نرم‌افزاری اپل حذف کرده است.
🔴
به گفته اپل، پس از آنکه تلگرام «محتوای متخلف را به‌سرعت حذف و حساب کاربری منتشرکننده را مسدود کرد»،  دوباره به اپ‌استور بازگردانده شد.
تلگرام نیز در واکنش به گزارش‌ها درباره حذف این پیام‌رسان، در شبکه‌ اجتماعی ایکس نوشت: «گزارش‌های مرگ من بسیار اغراق‌آمیز است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139777" target="_blank">📅 09:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139775">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
پزشکیان: استعفا نخواهم داد و خواهم ایستاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139775" target="_blank">📅 09:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139774">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764948ea9.mp4?token=YU-dkKUYJXPNocULSifA9flWBp63MGqm1YakTLLb-0R4t82HIiy2flQytSEG6cb0CZpqguxhe3hyAWEGTLJ2bUoxRZNDawb3au3azsxLDkFE1-GDNqDeIAFzdAbNceymNgCateMsmnvoJsuIaCI8NcfPYqeqK0oXoCn1dbg06x1yw0O0FYFPBLH89vhoh8H1cZy98qzE0jlwXUE2W9taWvH3khdx1B5vAEkZS2zwYfDQd90OludyD3lBKlp3nMkEZN9JhqfoEOWFjUdh8CyLwWFddsoO2gNYh4v8L2Ki5pzuxi2TJkqUtaVFUPzizRpqZEypu2Lz9ce2ASGwVIHeww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764948ea9.mp4?token=YU-dkKUYJXPNocULSifA9flWBp63MGqm1YakTLLb-0R4t82HIiy2flQytSEG6cb0CZpqguxhe3hyAWEGTLJ2bUoxRZNDawb3au3azsxLDkFE1-GDNqDeIAFzdAbNceymNgCateMsmnvoJsuIaCI8NcfPYqeqK0oXoCn1dbg06x1yw0O0FYFPBLH89vhoh8H1cZy98qzE0jlwXUE2W9taWvH3khdx1B5vAEkZS2zwYfDQd90OludyD3lBKlp3nMkEZN9JhqfoEOWFjUdh8CyLwWFddsoO2gNYh4v8L2Ki5pzuxi2TJkqUtaVFUPzizRpqZEypu2Lz9ce2ASGwVIHeww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک خودرو در غرب غزه هدف قرار گرفت که منجر به کشته شدن دو نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139774" target="_blank">📅 09:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139773">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: ایران و عمان به توافقی در مورد تنگه هرمز نزدیک شده‌اند که بر اساس آن کشتی‌هایی که وارد تنگه هرمز می‌شوند از مسیر ایران عبور می‌کنند و کشتی‌هایی که از تنگه خارج می‌شوند از نزدیکی عمان
‏
🔴
این توافق شامل هزینه خدمات (نوعی کمیسیون) برای ایران می‌شود.
‏
🔴
طبیعتاً تا این گزارش‌ها توسط مقامات ایرانی بیان نشود، مورد تأیید نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/139773" target="_blank">📅 09:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139772">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fae3de193b.mp4?token=lo1F9ORjgU2LoBGmu0pkSBMUzidnpFRD_MaDTsiRfGzRYOtMOIYy8W2xPxysTlO7QwTJSc0MFTsAYm93VVufP_Ebz6cfwRURsCz_GhKXc8dTKmS-iQrcLkvHkk59goybkp4iTNmuaBvq0hsPlIWJa7QxWP-H1yt3NjSX4Z2shiULcjG_uFeTlRQqMoznMsoVirGLi4pgYcqAZO9_LB1DvzIYjbQBA1VG2Bn39XJIr-zbPFxAKBuFa1zsihTOXRjj_npztFbB6sDmWRtiZL3ftEfDNLg_SQhWV9a30oV8rPjqeNiHiFZ5qnWcwSZF5w0y4PfZgKkH2Z-rsjnpalBXew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fae3de193b.mp4?token=lo1F9ORjgU2LoBGmu0pkSBMUzidnpFRD_MaDTsiRfGzRYOtMOIYy8W2xPxysTlO7QwTJSc0MFTsAYm93VVufP_Ebz6cfwRURsCz_GhKXc8dTKmS-iQrcLkvHkk59goybkp4iTNmuaBvq0hsPlIWJa7QxWP-H1yt3NjSX4Z2shiULcjG_uFeTlRQqMoznMsoVirGLi4pgYcqAZO9_LB1DvzIYjbQBA1VG2Bn39XJIr-zbPFxAKBuFa1zsihTOXRjj_npztFbB6sDmWRtiZL3ftEfDNLg_SQhWV9a30oV8rPjqeNiHiFZ5qnWcwSZF5w0y4PfZgKkH2Z-rsjnpalBXew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طراحی پرچم‌ های لبنان، عراق و ایران با استفاده از گوجه، خیار و... در موکب‌ های عراقی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/139772" target="_blank">📅 09:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139771">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزارت دفاع روسیه: 4 کشتی باری را در بنادر نیکلایف و یوژنی و همچنین در دریای سیاه هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/139771" target="_blank">📅 09:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139770">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بر اساس گزارش تاس به نقل از استاندار مسکو نیز در پی حمله پهپادی اوکراین به منطقه مسکو، 5 نفر کشته و 6 نفر زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/139770" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139769">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c5f722d89.mp4?token=n2sVEU20yRylFSzY9SSmazH9Figzr3FIKZ8NAGlVFoiTckJmR57sDfhjuueS9WuVnhtz4I0yv4WOIVY9FUxZjnFfcrgMHWDctg91Uco_J4OKny4xrj8Kb3qWH3LCwZU5A3Zj6z9sIkqnPf8uYeKuTDWO_DpjDC1y9DWGd3e2oe_V_yP5RrGhCvJ-br4h1Ni77xlI4ZlUQ7xJc_iH_AQcuWXkncfEiNZlKWvFfQje7lL4-iV827SGsTsL2Qj31Req9nhCfuuthCsOQXOwA0U0KyVva4Wwe6PiO1f2hr81ug6a_zDUAozB2R1ubros9IMyRD07rdGoHiTst19cdSYIWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c5f722d89.mp4?token=n2sVEU20yRylFSzY9SSmazH9Figzr3FIKZ8NAGlVFoiTckJmR57sDfhjuueS9WuVnhtz4I0yv4WOIVY9FUxZjnFfcrgMHWDctg91Uco_J4OKny4xrj8Kb3qWH3LCwZU5A3Zj6z9sIkqnPf8uYeKuTDWO_DpjDC1y9DWGd3e2oe_V_yP5RrGhCvJ-br4h1Ni77xlI4ZlUQ7xJc_iH_AQcuWXkncfEiNZlKWvFfQje7lL4-iV827SGsTsL2Qj31Req9nhCfuuthCsOQXOwA0U0KyVva4Wwe6PiO1f2hr81ug6a_zDUAozB2R1ubros9IMyRD07rdGoHiTst19cdSYIWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از سیلاب در شهرستان راز خراسان شمالی که موجب قطع کامل دسترسی مسیر ورودی و خسارت به زیرساخت ها شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/139769" target="_blank">📅 09:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
رویترز گزارش داد صادرات نفت خام آمریکا پس از توافق صلح با ایران به ۳.۶۶ میلیون بشکه در روز کاهش یافته است. به نوشته این خبرگزاری، افزایش عرضه نفت خاورمیانه به بازارهای جهانی پس از این توافق، از عوامل اصلی افت صادرات نفت آمریکا بوده است.
🔴
بر اساس این گزارش، سهم صادرات نفت خام آمریکا به بازار آسیا نیز کاهش یافته و از ۵۲ درصد در خردادماه به ۴۰ درصد در تیرماه رسیده است؛ موضوعی که نشان‌دهنده افزایش رقابت نفت خاورمیانه در بازارهای آسیایی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/139768" target="_blank">📅 09:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سنتکام شمالی یک سامانه موشکی هیمارس را در ۳۱ جولای به نوم، آلاسکا، در چارچوب عملیات توندرا مرلین مستقر کرد.
🔴
این استقرار که با پشتیبانی یک هواپیمای ترابری C-17 نیروی هوایی سلطنتی کانادا انجام شد، با هدف تقویت توانایی‌های حمله دقیق دوربرد و نمایش قابلیت استقرار سریع نیروهای آمریکایی و کانادایی در سراسر منطقه شمالگان صورت گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/139767" target="_blank">📅 09:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139766">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
سیلاب‌های اخیر در افغانستان ۲۹ کشته و ۱۲۹ زخمی برجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/139766" target="_blank">📅 08:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTsCDQL-oRHzloHOCXuxGt2io_jfe6pIpPY6IGn9kJalkRLwKs1QTuTPuKIz4J-E9AiNaBTrWvSPYCEHES1aPTS_-My0smLfwI7mi-fgrtwtUK0tz6Li5lUvNGDz7fMS4JRSDjX0t_7Sz2vKqkoBQy1ixJLwuPV122eQXkAQTxiEGf9l-8FqYUjrXFYbsMdI8HRVqUwRIVBKouhdjKRpbINDLbKyzDBzf1AuFnNN-rbaUr_aNeZEXdD-I8AK_suDGAQgFs5-r2NT2pQq1RmGhcazsgVVrrgIJRYI4rcvZIU88K9jyhALK8CuEWuYug9nNYNzAdhgg6ybwIFd9rqitA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیدآبادی، روزنامه‌نگار:
اسماعیل بقایی اگه سخنگوی یک نهاد نظامی بشه به نظرم براش زیبنده‌تره
🔴
اجازه نمیده آب از گلوی یه خبر معطوف به حل مشکل جنگ پایین بره؛ درجا میاد اونو تکذیب می‌کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/139765" target="_blank">📅 08:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45090a2b37.mp4?token=kosPC6sd1hqtjAsKzQeOCLonyWQwCVW-A6Yae-30oHiEwa7Yo4hnRtrPpEo0iKc8FadTVooM5N0SHq79QjBvjFwwRFuaTmInSqy7-SpgdE3fIPUuUu9YvohwCr5tjJOllKcIspTdFUVwY3DX0O5TwbsYjsKFYYrah_P5DEAlRpzJPHUE5lZUt4mZiBon04ICFTp_ujiHmu-7yGOx1vxb7cWPX1JV03vIf2zHf8OxHGWXe_Ia44Ldm6rhWfI7rEfhROSDb5B-_PMMvNuLTHTksGgwLgg3cJjG_56wFGK9OObPdGA-5T1kVngzR5tInX-0NrdJ5FPOH51nedFbElaQ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45090a2b37.mp4?token=kosPC6sd1hqtjAsKzQeOCLonyWQwCVW-A6Yae-30oHiEwa7Yo4hnRtrPpEo0iKc8FadTVooM5N0SHq79QjBvjFwwRFuaTmInSqy7-SpgdE3fIPUuUu9YvohwCr5tjJOllKcIspTdFUVwY3DX0O5TwbsYjsKFYYrah_P5DEAlRpzJPHUE5lZUt4mZiBon04ICFTp_ujiHmu-7yGOx1vxb7cWPX1JV03vIf2zHf8OxHGWXe_Ia44Ldm6rhWfI7rEfhROSDb5B-_PMMvNuLTHTksGgwLgg3cJjG_56wFGK9OObPdGA-5T1kVngzR5tInX-0NrdJ5FPOH51nedFbElaQ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: ما از حد و حدود خودمان دفاع می‌کنیم، اما به‌دنبال گسترش جنگ نیستیم
🔴
باید تلاش کنیم در این اوضاع و احوال، جامعه‌ای بسازیم که دشمن در آن طمع نکند، وارد آن نشود و نتواند این مجموعه اجتماعی را تکه‌تکه کرده و از بین ببرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/139764" target="_blank">📅 08:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
👈
منابع عربی:
چندین پهپاد انتحاری به سمت شرق و شمال کویت شلیک شده است و سامانه های پدافندی درحال مقابله هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/139763" target="_blank">📅 02:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-139762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
روزنامه روسی ایزوستیا:
آمریکا می‌خواهد با سردر‌گم کردن تهران زمینه را برای یک حمله غافلگیرانه فراهم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/alonews/139762" target="_blank">📅 02:35 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
