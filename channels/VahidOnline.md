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
<img src="https://cdn1.telesco.pe/file/LougC4s9h1G9sL2bJwVQ0pmalBjjt89DaWJ6ci4d9HYv13iUDIvP5XcBp-rmZCPbweZ355I3bdfjeiqPvMaRzUtQz6yZ8XPGzVI0AwjDwSXbabl9ntw33FIFVYNFLC1v8_SwR2NreYJOCp-Jb1O6JVxL2JaSEBubWWD4kW5qekcmmiApvHZhQKXQXgXHfo7Fcz1UP0fuoE1GBi-4hYHSc0lnzvGDEeFKsmaH93FSYpwe55zckxx2BUMmzL3GR04-_xkBoQKXVsfonMMwRjnHhVWJ5Rz2dic5N0l2BpXKCmFNE5Vo-d9wEmZ5zNCMhD3QaVzrWGcwKNIV79I_4vfMOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 10:49:23</div>
<hr>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e49979671.mp4?token=XNpMQxp_sXBA8DAeXKQdyY3buRiPd1jHPCCcqaQyunIsc17fFJ9yMDOcp-JT4HS7zL3otkKtYMaXaNz1qIL2Ua3JQiMZXeYEyGEd2OHZTI2FoCM-7_sD-WIA3l48ry6k5GBXJ5RfXDjS9YOIEtvEaz9WNUwzOpZwTbbejUwzFODPj1fxdHnJby3SiAJIglR4zz0I-aYg-K7yRHJQmxIKjco36NlCYictPcLqMYLyXtevQHDnFaBtP3b7oyoRH5ZdE8BGKRv37CCcsuie5euXFiYdsf5f4FIfvOBWUAmDUxup_J1ds1ShL3Y_UE-l1e4jGKeo1yxk7xOJ8HaXd8gniw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e49979671.mp4?token=XNpMQxp_sXBA8DAeXKQdyY3buRiPd1jHPCCcqaQyunIsc17fFJ9yMDOcp-JT4HS7zL3otkKtYMaXaNz1qIL2Ua3JQiMZXeYEyGEd2OHZTI2FoCM-7_sD-WIA3l48ry6k5GBXJ5RfXDjS9YOIEtvEaz9WNUwzOpZwTbbejUwzFODPj1fxdHnJby3SiAJIglR4zz0I-aYg-K7yRHJQmxIKjco36NlCYictPcLqMYLyXtevQHDnFaBtP3b7oyoRH5ZdE8BGKRv37CCcsuie5euXFiYdsf5f4FIfvOBWUAmDUxup_J1ds1ShL3Y_UE-l1e4jGKeo1yxk7xOJ8HaXd8gniw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس"
خبرگزاری فارس و تسنیم با انتشار ویدیوهای بالا نوشتند:
سخنگوی سازمان آتش‌نشانی:
در ساعت ۶:۱۴ صبح امروز، وقوع یک مورد انفجار در جایگاه سوخت گاز واقع در بزرگراه یاسینی، مسیر غرب به شرق، بعد از سه‌راه تهرانپارس (نرسیده به پل ۱۲ فروردین) به سامانه ۱۲۵ اعلام شد. بلافاصله نیروهای دو ایستگاه آتش‌نشانی به محل حادثه اعزام شدند.
در بررسی‌های اولیه مشخص شد که یک دستگاه خودروی نیسان یخچال‌دار در حال سوخت‌گیری در این جایگاه بوده که به دلایل نامشخص و در حال بررسی، دچار انفجار شده است.
خوشبختانه این انفجار منجر به آتش‌سوزی نشده بود، اما شدت آن باعث وارد آمدن خسارات قابل‌توجهی به بدنه خودروی نیسان و بخش‌هایی از سقف و دیواره‌های جایگاه سوخت شده است.
در این حادثه دو نفر شامل راننده خودروی نیسان (حدوداً ۶۰ ساله) و یکی از متصدیان جایگاه (حدوداً ۴۰ ساله) دچار مصدومیت شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/75892" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پیام‌های دریافتی:
شرق تهران
تهران نو صدای انفجار شنیده شد
وحید جان ۵:۵۸ صدای تک انفجار شمال شرق تهران، سنگین بود. مثل بمب بود
سمت شرق تهران یه تک صدا اومد ۵:۵۷ وحید جان
ساعت 5:56 تهران شرق یه صدایی مثل انفجار شنیدم دقیق نمیدونم
سلام، ساعت ۵:۵۷
شرق تهرانیم و انگار صدای انفجار از جنوب غربی بود
تهرانپارس صدای انفجار اومد ساعت۶صبح
منم صدای انفجار ساعت ۶ شرق تهران بیدارم کرد ولی چون ادامه نداشت فکر کردم اشتباه کردم تا پیام بقیه رو دیدم
سلام، ساکن شرق تهرانم، تهرانپارس- با صدای انفجار ساعت حدود ۵:۵۶ بیدار شدم اول فکر کردم توهم زدم، الان که پیغام‌های شما رو خوندم گویا بقیه هم شنیدن.
الان حدود ۵ دقیقه ممتد صدای آژیر میاد حالا آمبولانس یا آتش نشانی نمیدونم.
سلام، پردیس چهارشنبه ۱۳ خرداد ۶ صبح صدای مثل بمب اومد
وحید جان من تو نارمک صدای انفجار شنیدم ولی نزدیک نبود  ۵:۵۸
شرق تهران یه صدای خیلی بلند اومد ۵:۵۷
سلام تهرانپارس فلکه اول ساعت ۶ یک صداى انفجار بلند اومد و از  ساعت ۶:۱۹  تا ۶:۲۲ صداى آژیر ماشین هاى امبولانس و اتش نشانى میاد
آپدیت:
دلیل احتمالی انفجار در پست بعدی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/75891" target="_blank">📅 06:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7aj23-UpGBW26fDdBXTKlHjQvZL7uRXHtez6s6JolJ1feOu4uDAR0AIPr6DoNaB9xOPEtgxzlpegVT663KsFCOnmSrGGrhkcBo-s8s9rvZikmxBTJzUKXRcEGpOgyco7J68DnkJmppdm3q7Dv3mdNDtGcTUL1dFEzEJ42mCkWsi8cxUJ2AiWDzg4ITHqe1HK-gFuDvZf7DP6rpubq8kpQW-vMkGgwtkE1HTbakLDYtDF2qfK6ghA_YuRjJ8kpLJO3xrvKyY1BJt6ckm7TvFyBrtnzt_as7TeE-v_DEa04FQmO2EYQ0mTq5aQRo7wHlZicvaDITsdGZ701NmUh04HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌پست می‌نویسد، بر اساس گزارشی جدید، یک خلبان جنگنده «اف-۱۵ئی استرایک ایگل» نیروی هوایی آمریکا در جریان جنگ ایران در کمتر از یک ماه دو بار در کویت (آتش خودی) و ایران سرنگون شد، اما هر دو بار زنده ماند.
هویت این خلبان هرگز به‌طور علنی اعلام نشده است. مقام‌های کنونی و سابق نظامی به نشریه «های ساید ساب‌استک» گفتند که او یکی از دشوارترین پنج هفته‌های دوران خدمت یک خلبان نیروی هوایی آمریکا را از زمان جنگ ویتنام پشت سر گذاشته است.
به نوشته نیویورک‌پست، بدبیاری او از دوم مارس آغاز شد؛ زمانی که در یک حادثه آتش خودی در کویت، نیروهای دفاعی این کشور به اشتباه به سوی سه فروند جنگنده اف-۱۵ئی آمریکایی شلیک کردند.
در این حادثه، هر شش خدمه این سه جنگنده مجبور شدند با استفاده از صندلی پران از هواپیما خارج شوند و با چتر در خاک کویت فرود آیند. همه آن‌ها سالم نجات پیدا کردند.
با وجود این حادثه، به گفته پیت هگست، وزیر جنگ آمریکا، خلبانان تنها چهار هفته بعد دوباره به ماموریت بازگشتند و در عملیات بمباران اهدافی در تهران شرکت کردند؛ اقدامی که او آن را نشانه شجاعت و فداکاری این نیروها دانست.
نیویورک‌پست می‌نویسد، اما چند روز پس از آن ماموریت، بدشانسی بار دیگر به سراغ یکی از این خلبانان آمد. یک جنگنده اف-۱۵ئی بر فراز ایران هدف قرار گرفت و دو سرنشین آن در خاک ایران سقوط کردند.
این خلبان در سوم آوریل به‌سرعت نجات داده شد، اما افسر سامانه‌های تسلیحاتی همراه او زخمی شده بود و پس از آنکه ایران برای دستگیری او جایزه تعیین کرد، ناچار شد مخفی شود. او روز بعد در عملیاتی نجات پیدا کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/75890" target="_blank">📅 04:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NNdYDGG5yg0Y_ZrkhP9vPj8G56yhEcS2WAGejfDT1Bz5SLcheKQwicLXntNfbLaMlP_Q-LPQME0dWz4hxew7te4u2JkfTSzNaMWteBVBL_8PbJ8K4scnIFkmORj9k0bvoW3meP1mFsKC2WOp86MeXlxwcps64JVLWtwb8vPWCzz52fcQ_P4gq7r6hA3kXaRJZKqa7CYGGWFUW7W8VSTPTft3yZVp_JEq10JSUT004OGxTJWilEbucuS-Y1n1Ovo1TV16HTMGHcb1R-45NyTUDb22eOyl_Sgi9y5kHh3FjJJERvrJ5K0vYY-o0vbmsL2h4Rcd_gx_6vRhNHd07rsS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی آمریکا در شبکه‌های اجتماعی اعلام کرد که سپاه پاسداران مدعی شده که در حملات امروز با موشک و پهپاد به مقر ناوگان پنجم آمریکا در بحرین و یک پایگاه هوایی آمریکا در منطقه ضربه زده است.
سنتکام گفت این ادعا نادرست است و تمام حملات جمهوری اسلامی به نیروهای آمریکایی شکست خورد.
@
VahidHeadline
آپدیت:‌
سنتکام توییت دیگری هم منتشر کرد:
ستاد فرماندهی مرکزی آمریکا (سنتکام) دقایقی پیش اعلام کرد که «موج دیگری» از حملات پهپادی جمهوری اسلامی که نیروهای آمریکایی در کویت را هدف گرفته بود، ناکام ماند و پهپادها به اهدافی که داشتند برخورد نکردند.
سنتکام افزود پدافند هوایی ستاد فرماندهی مرکزی ایالات متحده «با موفقیت چندین پهپاد را سرنگون کرد. سنتکام گفت هیچ یک از پرسنل و یا تجهیزات آمریکا آسیبی ندیده است.
@
VahidHeadline
(مثل دو روز گذشته در این ساعت، ده‌ها پیام دیگر از تهران دریافت کردم درباره صدای عجیب پرواز هواپیما که منجر به بیدار شدن خیلی‌ها شد.)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 241K · <a href="https://t.me/VahidOnline/75889" target="_blank">📅 04:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVGyW-Fp14Y4-JBLQW8YgAIkBSn84H9vYEFut-e8mXSfrWYR_9tGaiH46QZsceV4W3GyyXzCxRoOJVS6vl7YQDUGWYEjXhQOGYd-CxYYBQjAl-6vuzRUCxO7kT0agF8f6GyIy2owDPHNbTsiRpPQ9B8yu1WWekmsQKR54_LNYvvnbT3bLa0vXymGG8d5nLHQ3H1ZSrZ9WIZo_Oo2g21CzQiRoLdD3F47Dv6dtX673xmswEv58olIeJrR1zyqDdhiXTrSy_CU-IMwhL__-uY-y0VUWhhRwxvKEsJsnOAEC1TEuZpGGkCbUlAp8RumIqGN_SoKJyUu0VvGsW2hGHuYVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام از حمله به جزیره قشم پس از دفع حملات موشکی جمهوری اسلامی خبر داد
ترجمه ماشین:
نیروهای آمریکا و شرکایش در برابر رفتار تهاجمی ایران دفاع کردند
تامپا، فلوریدا — نیروهای آمریکا در تاریخ ۲ ژوئن با موفقیت چندین موشک بالستیک و پهپاد ایرانی را منهدم کردند و در پاسخ به تلاش‌های ایران برای حمله در سراسر خاورمیانه، حملات دفاع از خود را در جزیره قشم انجام دادند.
ایران چندین موشک بالستیک به سوی همسایگان منطقه‌ای شلیک کرد؛ با این حال، هیچ‌کدام به اهداف مورد نظر خود اصابت نکردند.
دو موشک ایرانی که به سوی کویت شلیک شده بودند، پیش از رسیدن به هدف سقوط کردند یا در مسیر متلاشی شدند و سه موشکی که به سوی بحرین شلیک شده بودند، بلافاصله توسط نیروهای پدافند هوایی آمریکا و بحرین رهگیری شدند.
لحظاتی پیش از آن، نیروهای فرماندهی مرکزی آمریکا، سنتکام، سه پهپاد تهاجمی یک‌طرفه را که ایران به سوی دریانوردان غیرنظامی در حال عبور قانونی از آب‌های منطقه‌ای شلیک کرده بود، سرنگون کردند.
نیروهای آمریکایی همچنین حملات دفاع از خود را علیه یک ایستگاه کنترل زمینی نظامی ایران در جزیره قشم انجام دادند.
هیچ‌یک از نیروهای آمریکایی آسیبی ندیدند. نیروهای سنتکام در جریان آتش‌بس جاری، همچنان هوشیار و آماده دفاع در برابر تجاوز بی‌دلیل ایران هستند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/75888" target="_blank">📅 03:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAmzuUZDyUxvLjMKm6mYsXzSpF01pEzxPThOUEoFahBb7F_4QoAtaNQEIptYYTlNHLvKSOS5IrAmHYsmC9ySPALG4vQwDNlpOqCzogDE6GJpOF_1V-TqUW7DfQeaaUKXSRHgTG2YtwRwwLynyMDlavjiEZeuIjzV2VQmUziJacdBt18i8TqHX-yN3ZGS-CYE7sx0x0mMiem0guvLEk5C6zxqO_jUxvWcPK87HvG7037fKIEuGNJmSWrw-axxXV9K0c5uaY_2vAzVE9dhmEOg-73HTHj7_WgR8ncQu1_6wlrbM607Njh9iYcy0gUH_msvzvSI8WKlfi_z1AZXAswgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعتی پس از مخابره گزارش‌های متعدد از حملات موشکی به نقاطی در کویت و بحرین، سپاه پاسداران با انتشار اطلاعیه‌ای رسما از حمله به پایگاه ناوگان پنجم نیروی دریایی آمریکا خبر داد.
@
VahidHeadline
بیانیه سپاه به نقل از منابع جمهوری اسلامی
"بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
در اواخر شب گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد در پاسخ به این تجاوز پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
پیش از این اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم. این پاسخ ها باید عبرت شده باشد.
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 242K · <a href="https://t.me/VahidOnline/75887" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J1oj0eICaFfQsEzzKPsx5aARGwlkPmMlq3LH8pA9M9LmuLeZ2CO6Bd23CfXY-UrE1JOoqDMCed3IvYwgQPd_x6yicbEwOgWSHwDCwwTYNAUUGQsdeYOcKiD2g63wS8xftgmkmFdhbhb8wNT04Q3Yd-64m0-74XicZM4h2WRxhcTbBUe7y8ljAVDkxDqUKuU9Egu5PKL_hm24Sz93REd78fK9iUn9HdRL80tAHXgU0qH-qWOrwg79CVEMvteJDfPWrPHzxIbTPkEkgqERQBEcYfwgbqj3pWENo4VNusZ_O8_Mwq2WXbiPButYuHnvzw06sr4d_kXyxBd4jIZuuhY5QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
عکس بالا: بندر کنگان دو تا موشک شلیک شد سمت کشور های عربی 2.19
ساعت ۲:۲۰ از جم بوشهر موشک زدن
درود همین الان از جم دو عدد موشک شلیک شد به سمت خلیج فارس
از جم ساعت ۲:۲۱
دو تا موشک پرتاب شد
از جم بوشهر هم دو تا زدن
همين الان
شلیک موشک از شهرک موشکی شهید چمران جم هم اکنون
ساعت ۲:۲۳ دقیقه صبح دو موشک همزمان
آپدیت: پرتاب سوم
سومی هم پرتاب شد
یکی دیگه هم همین الان شلیک شد
۲:۲۴ از جم یکی دیگه پرتاب شد
🔄
آپدیت:
وزارت کشور بحرین دقایقی قبل از به صدا در آمدن «آژیر خطر» خبر داد و از ساکنان این کشور خواست به نزدیکترین مکان امن بروند. این هشدار پس از آن است که کویت نیز اعلام کرد مشغول مقابله با حملات هوایی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/75886" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IooSf4neQtAPzAI7WougwwjnIASrts99XDJ_k4OK92kitlABgvfNejjc3YWOpKoQyhLvZg5j7kM9ISKhBTnFcHrnXGZHV7Mc48giW0EKw3lnwfHu-kQyRo0wi1ZFGsjNfzkyVS5ixPXsqf86gFi44iMGF71aOh2L2saxDlQTY398kybOtrS3A3P9PLmVeiszDVWJiH5jfGmz-V7XVhEQZYj-8UcKat2RGPEclfaCUQ0aGY6COSVJUmqk7PVqU2X2HMhjQ7ZiMdthzbwp6EHzt5OQtSYkVZ32x0LaMU6wsEhFKRG0_St3bn2ldIrtrnX3ylOZr7nyd8-jPa2L10YjGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی:
۲:۰۷ همین چند ثانیه پیش صدای پرتاب موشک از توی خود شهر داراب شنیده شد.
الان دوباره صدای پرتاب موشک اومد
وحید سلام
یکی دیگه هم الان زدن از داراب
۲ دقیقه پیش
۲ تای قبلی هم یکیش تو هوا ترکید
آپدیت: عکس بالا
و پیامی دیگر از کویت: دوباره صدای آژیر
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/75885" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l06wn0xL4SJDtyxhwa1ewqgDUcosz31Q1-WaebSBI5EqIY0klNQoBho_CPNHLZNKuI5KsgHcKBdP60781uyyQxeileuZtNIy8Li5miO8yytLtxlFWh53kxAyBkU0wdhnCg6tGUbAYZu7NRCR-oS-qFBMUQD92MaYCt4HyKcaJUp8zOgHGSLFKZt1abA3IXgfdPZ3TmmzoMuUjOEFStqwmUTMpGbF7TDukk0JKA58UBAofuKFtQIS3QGXGT_TwiLHBvCzLZv34LWbyS0GV_pfv46Zpnu1VEqlMYD_4q6QIhmvBIAWR2N-EYnA9gqPREXUpv6kEMycz5TSmmaWZIobGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از داراب در استان فارس پیام‌هایی درباره شلیک موشک دریافت می‌کنم. هم‌زمان اسکرین‌شات‌هایی هم از کویت دریافت می‌کنم که میگن هشدار اعلام شده.
چهارشنبه ۱۳ خرداد
Vahid
ارتش کویت
اعلام کرد
سامانه‌های دفاعی این کشور در حال مقابله با حملات موشکی و پهپادی خصمانه هستند.
VahidOOnLine
ستاد کل نیروهای مسلح کویت با انتشار بیانیه‌ای فوری اعلام کرد که سیستم‌های پدافند هوایی این کشور، بامداد چهارشنبه، ۱۳ خردادماه، مشغول مقابله با حملات موشکی و پهپادهای متخاصم در آسمان کویت هستند. ارتش کویت در این اطلاعیه تاکید کرد که صدای انفجارهای شنیده‌شده در مناطق مختلف، ناشی از عملیات موفقیت‌آمیز سامانه‌های دفاع جوی در رهگیری و انهدام این «اهداف متخاصم» است. مقامات نظامی کویت از تمامی شهروندان و ساکنان این کشور خواسته‌اند تا آرامش خود را حفظ کرده و به طور کامل به دستورالعمل‌های امنیتی و ایمنی صادر شده از سوی مراجع مربوطه پایبند باشند.
@
VahidOOnLine
پیام‌های دریافتی که پیش از اخبار بالا نقل کرده بودم:
سلام همین الان ساعت ۱:۲۳ دقیقه دوتا موشک از داراب استان فارس پرتاب شد
یکیش حین رفتن ترکید
همین الان داراب صدای انفجار شدید اومد و شیشه ها لرزید
کل همسایه ها ریختن تو کوچه ببینن چه خبره
وحيد همين الان اژير كويت فعال شد دوباره
٦ تا انفجار خيلي سنگين تا الان
توي اين ٣ ماه اينقد صداش سنگين نبود
سلام آژیر در کویت
۵ انفجار بزرگ در کویت نسبت به روزهای قبل بیشتره
آپدیت:
ما بین فسا و داراب هستیم
یه صدای انفجار وحشتناک اومد ولی نفهمیدیم چیشده
من داراب هستم
ما عروسی بودیم تقریبا ساعت ۱.۴۰ دقیقه بود که یه صدای انفجار اومد و سقف سالن لرزید
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75884" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام دریافتی تایید نشده:
صدای  انفجار روستای نخل گل قشم
سلام وحید جان
قشم صدای پایان جنگ در همه جبهه ها از جمله لبنان میاد
خبرگزاری مهر هم نوشته:
"بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 243K · <a href="https://t.me/VahidOnline/75883" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=dn1-XwFKJ-7Th8i7y6wW5ZYn5sXaDx-S4RAs_gf_uWWS324JK9nCj4be6kFDFWrzl_qNypuEPcCNbrdBmae1FC78LzGDobeXVhEgQkaM-mE8uh1oVA6ZndZJfcU5klrQrNfdnyF-rxGb9rEQwWQfnwPdCiqGYb7OVFDInP_HZtzkqdfRZT6HlSKr6_7153TCDwsWE0y1cS-QWeJKD-6HLDZPPMJUwKQm8rNonWvdgH26805hRPZ-Z8vqeM5XV_CuD8dgvef_Q-mUCAkDY4u2UAIgLsrpOx4iM_M_qSk3xXidzu0QTpZVTaW0Na-cLMQq901uIwtEPaMfMefs2wQ4yg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=dn1-XwFKJ-7Th8i7y6wW5ZYn5sXaDx-S4RAs_gf_uWWS324JK9nCj4be6kFDFWrzl_qNypuEPcCNbrdBmae1FC78LzGDobeXVhEgQkaM-mE8uh1oVA6ZndZJfcU5klrQrNfdnyF-rxGb9rEQwWQfnwPdCiqGYb7OVFDInP_HZtzkqdfRZT6HlSKr6_7153TCDwsWE0y1cS-QWeJKD-6HLDZPPMJUwKQm8rNonWvdgH26805hRPZ-Z8vqeM5XV_CuD8dgvef_Q-mUCAkDY4u2UAIgLsrpOx4iM_M_qSk3xXidzu0QTpZVTaW0Na-cLMQq901uIwtEPaMfMefs2wQ4yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا به یک کشتی دیگر شلیک کرد.
بیانه سنتکام، ترجمه ماشین:
تامپا، فلوریدا — نیروهای آمریکا [امروز] ۲ ژوئن یک نفتکش بدون بار را که قصد داشت به سوی یکی از بنادر ایران در خلیج [فارس] حرکت کند، از کار انداختند.
فرماندهی مرکزی آمریکا، سنتکام، تدابیر محاصره را علیه نفتکش M/T Lexie با پرچم بوتسوانا اجرا کرد؛ این کشتی هنگام عبور از آب‌های بین‌المللی به سوی جزیره خارک در حرکت بود. خدمه کشتی هشدارهای مکرر را نادیده گرفتند و طی یک دوره ۲۴ ساعته چندین بار از اجرای دستورهای نیروهای آمریکایی سر باز زدند.
در نهایت، یک هواپیمای آمریکایی با شلیک یک موشک هل‌فایر به موتورخانه کشتی، آن را از کار انداخت و مانع رسیدن نفتکش به ایران شد.
سنتکام از ۱۳ آوریل اجرای محاصره همه رفت‌وآمدهای دریایی به بنادر ایران و خروج از آن‌ها را آغاز کرده است. با ادامه آتش‌بس با ایران، نیروهای آمریکا تاکنون شش کشتی تجاری را از کار انداخته و مسیر ۱۲۲ کشتی را تغییر داده‌اند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75882" target="_blank">📅 00:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dmW_kn2MUtmhLrC2FeBh47JMdyr0lPhq2uV3ZA-tFKhikP-FIySq4ABHxR5MHbOBXj_F-_9TIYb-gqTPcO01URLfh8gwSHe-tPUOnSKmSCeEPmIfAkXwaQB5QbHPDrq8kh5nAB629kOnq0iGR9bTSmOb2oHzaGs7xBzHX5wOk008a3KqsdmjiZElRuLXZZqiCpRwV-liBpava8q3hhKJzOAkqokj57WmWoDAdIeQTFIm01U_9JX7waxBjHqnG_IchMNI8U3cm9QPDSWFewcqxvRlY5YCipzthmh0ss_UevBBCtdIy4G8zhR7641P_FwQuzchHml-HZ7P-4GB_eSzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: گزارش‌ها درباره توقف مذاکرات درست نیست
ترجمه ماشین:
گزارش‌های رسانه‌های اخبار جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش گفت‌وگو را متوقف کرده‌اند، نادرست و خطاست.
گفت‌وگوهای میان ما به‌طور مداوم ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش، و امروز.
اینکه این گفت‌وگوها به کجا می‌رسند، هیچ‌کس نمی‌داند؛ اما همان‌طور که به ایران گفتم: «وقت آن رسیده است، به هر شکل ممکن، توافقی انجام دهید. شما ۴۷ سال است که مشغول این کار بوده‌اید و دیگر نمی‌توان اجازه داد این وضعیت ادامه پیدا کند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75881" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j66Drd8i-fT8Fkw-ppvDr5f3wF_MuxL5bZkatrm89zCAvSXP_DLRmAbUU2uqAFgkLUkr8eoTYMxiYxrabII_v06un_Cw3Fu5Lm-NmAkWGAUWE9VMYu8cqxxmTWKRaeqhpM5rnm0IygCm3TU-WOM4HqjO3-81Oa0-hC43uean3xSfg75_2WH3F--iv31n4-eL0p6Fpv9LgiinrD6zT69jftbOD6ApEpV4-yuPXD2t8KJyAaFEaUM8NNKmavrndTZFY_AvXrMIspyLTsmmcDyMljNHbu6hQ-bGgoxa9zEY7XYUiGEyn0ZnJwj-nUVWxvg6ZOtLYhwrTSt-OrKc4tgQnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که نشانه‌هایی وجود دارد مجتبی خامنه‌ای رهبر جدید جمهوری اسلامی در سطحی به شکل فزاینده‌ای در حال مشارکت در روند مذاکرات است، «اگرچه تمام ارتباطات او به صورت مکتوب و از طریق واسطه‌ها بوده است.»
آقای روبیو افزود: با توجه به اتفاقاتی که برای رهبران متعدد در آن سیستم رخ داده است، تصور می‌کنم که حضور بسیار علنی احتمالاً چیزی نیست که در داخل برای آن‌ها توصیه شود.
او همچنین در پاسخ به سناتور دموکرات کریس مورفی، کاهش تحریم‌ها در ازای بازگشایی تنگه هرمز را رد کرد و گفت که هرگونه کاهش تحریم‌ها باید پس از امتیازات عمده در مسئله هسته‌ای و اورانیوم غنی‌شده صورت گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75880" target="_blank">📅 19:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TES0zcEcKRtecRY0rZt6eet4GxEYMUJvc0ks2PVBPDOLHe5pwp2gbBX74Df3LSvJjGvXo5K0FW0o1Pa3IsSdcltO6VxrRmp_UH8-oYfdXiUe_Vat9_FnuvL83hy0H5jlHmAYEstlXzPhn1Zsk6ZO0nbD-oAusPWQPt-5i8OTCJuzgWNI3oKENShnINZ4zayGv2N6V0pxcidx-mFYvAZzfr-fYr9v2wdVs1UE5QCOQVt1_p0bF9hjSFn2CLZApBhewhQEMd5ppQ-Y_4RRCJ2zAPXtO6FX53n5cvPyF5wVWdsDcI4vxBu-4huRNZF9r66vnqVOtLREo0Wz1l0z2nVteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BNV2F8BYcJO-0OJzQSfPkcwlPEKxYXb3WPas9ZI_bj8uklIn3ccALYgLBPNnTuYnPfpmj6FK56SDOv9A_ek7xFRZ8w7oop8-dmjwP7WSroGAat8aJmlXPdbXYL1dZPcElrZGptNA9-XAWYlKkzm3xOnkg77H8FJrsyRlc2rodkj01g-xE1hQv5cH8FPeIoe0SK_lWScKHswkWdpkQkJvqVTC4rfuB8iEmRt4dPlJPMyc3ISYEmos0QZ9YTUSM2sN59yzWoNF-wOWQWh7f_W7s10amFJ5cOyvCd3mrLnfUx8aV8mCxAUCWbCoi0NDDM9TZeFLwAwH1mL9SLkMu5n_-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو در جلسه کمیته روابط خارجی سنا گفت: «چیزی به نام نیروی دریایی جمهوری اسلامی وجود ندارد. آنچه باقی مانده تعدادی قایق کوچک است که روی آن‌ها مسلسل نصب شده و نیروی دریایی واقعی در کف اقیانوس قرار دارد.»
او افزود: جمهوری اسلامی همچنان تعداد زیادی پهپاد در اختیار دارد. توان بازدارندگی متعارف تهران به‌طور قابل توجهی تضعیف شده است.
@
VahidOOnLine
وزیر امور خارجه ایالات متحده در جلسه استماع سنا تاکید کرد که شرط اول آمریکا برای مذاکره با جمهوری اسلامی، بازگشایی کامل و بدون قید و شرط تنگه هرمز است.
او در ادامه تاکید کرد که منظور از بازگشایی، بازگشت شرایط به پیش از جنگ و عبور و مرور آزاد تمام کشتی‌ها از این آبراه راهبردی، بدون محدودیت و مانند سایر آبراه‌های جهان است.
@
VahidOOnLine
او گفت باز کردن تنگه هرمز شرط اول آمریکاست اما صرف این کار باعث برداشته شدن تحریم‌ها نخواهد شد و رفع تحریم منوط به شرایطی خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75878" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwRBPy7DbEkNzvyoK1tcDzG2xH4U_rbYg5SKyLvl6w4AYZV8gM_DwMZripgzaZRgGXdHQfHeLSz7yhKv2B3pljXtwkTzYjRGEz-Fq5k9GVUn_z-ZsmGhuIRBljTW2geQR8MA2L8OigyX1csklxoTEkYU6B4ELPlu98-v9dgicaDP4x-Ka1IfsOWgY_TeI0w2Rwo5JaBYUqsw2FzoXmcw_MAJ4zbj1wPryg7EZTKCMMZJb1SPiJ2yVyrDkgJjmZwOR9BDlCSkG_lWxr2RQYDZPe6lGNK8IE2OtRPDkdFCorn7FzAe344M-YmgwRvlPWLkbwgDzQgtKUmGjLN6Igpfag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، در مراسم تودیع دیوید بارنئا، رییس موساد، گفت جمهوری اسلامی تاکنون به دلیل توطئه‌هایش علیه اسراییل بهای سنگینی پرداخته و سرانجام این حکومت سقوط است.
بر اساس گزارش دفتر نخست‌وزیر اسراییل که روز سه‌شنبه ۱۲ خرداد ۱۴۰۵ در شبکه ایکس منتشر شد، نتانیاهو در این مراسم گفت: «هر کسی که بدخواهی علیه اسراییل در سر می‌پروراند، بداند که توطئه‌هایش شکست خواهد خورد و بهایی که خواهد پرداخت بسیار سنگین خواهد بود. بهایی که جمهوری اسلامی تا همین‌جا پرداخته است، بسیار سنگین است. پایه‌های رژیم وحشت در ایران ترک خورده و دیگر به آنچه بود باز نخواهد گشت. من به شما می‌گویم سرانجامش سقوط است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/75877" target="_blank">📅 18:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o-AAtMvWiLkPzEfWVbSAstV6i2Ib7trxJ6j5EMN-IzVF34wbJZkvA9YNP5LVNIiVEhIX8QVZ6KcCrr0kiZrmxQhCCcU4apnk1StiP5fiQKFOWPkYqpM-d-FFJMZIXaZJ9vwXnx0UFxtIOPG5inXj1Zn-PFZ_23B8Uzy3faU7_bcVr0lTe3kozf4ssZys2YfSNz63qqoUGPdofGMaDzFoTrD2_nXDc4gdAv5xvu-EaUSQ_qvgAujIFaAL9CxULUoH0iwX7UmISv7GAEUpwEwtepKitCH-hVB2YHOuNBGNoAAd58DUyzPwRryx1MpMOCgrcG_15tLbfo_Gd2Fx3fVTxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که جمهوری اسلامی در حال دستیابی به سلاح هسته‌ای بود و اگر عملیات خشم حماسی صورت نمی‌گرفت دیر می‌شد.
آقای روبیو با یادآوری این که توانایی نظامی جمهوری اسلامی به شدت تضعیف شده، افزود که جمهوری اسلامی ایران برای اولین بار در تاریخ، بسیاری از شرایط مدنظر آمریکا برای رسیدن به توافق را پذیرفته است.
به گفته او شکاف در ساختار قدرت سیاسی جمهوری اسلامی و زمان طولانی رسیدن پیام‌ها مذاکرات را طولانی کرده است. اما طبعا اگر مذاکرات به هدف دلخواه آمریکا نرسد، ایالات متحده گزینه‌های دیگری را درپیش خواهد گرفت.
@
VahidHeadline
پیش‌تر ‌خبرگزاری فارس، وابسته به سپاه، به نقل از یک منبع آگاه نوشت که تبادل پیام بین جمهوری اسلامی و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشینگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/75876" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nb0KW1sD8OqYI-866KuArRJicztK-bnBc2WwRn6xBagceO4uREi8PR9AdbO1kvUqKdE8dd0COQqflUh9WrTGf9fweqhTH2HQmZ_SJwHwejUF-BOj-WN0Psf9zWvz_vhFR0Sy9K7wd3Uo1tfbTrIpMpKU-n9lAZVi9Mg8WTyEmGth5gf2NVzhaAcwV-pkq5lTCBZP7yz8lSNrdriUEZ-d4nE9LYxVJ4KJV54VXW2YsIfXteC6dB0qjBGULsBJ5Z9p4dhipjSShMMsSpPGHTvtf1d1thJ4BQ2fP0lMt3x0hBkAjdmUWuH9K47ekhFt7iI3dQDhEx-LuGa-yZqnaNg1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=KDbBcLZOmo79BhWVXTmu_CLanSTRtqWje-nQ2SJ_65FI0ySF5SPzmQfoKZ-VhauFnlqxqrydKviwQcPcWUS_GLyO_7RMipVCbydGjvQnnjIftvMLVbhz9Koa9Zal4ShzcxlVzlCHjSqKh5tCcKtvg2264a0nLlcOs3YwewsRslPPYEHX1oWJa7-hAvNzlBTCAOTgoQ3TIwcz-9OXqbvDwF8LEe3sJfWJ0oOk723VYmKBm5udKIYdCTDRHxgWPnihtPTTld9HMSOqEP2G9AWoz0TXsEqlL06spppgQ587465ZSatGHURHYQmMX6emLwtHpl2TKvhJFWtlcXPxLAYOkg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=KDbBcLZOmo79BhWVXTmu_CLanSTRtqWje-nQ2SJ_65FI0ySF5SPzmQfoKZ-VhauFnlqxqrydKviwQcPcWUS_GLyO_7RMipVCbydGjvQnnjIftvMLVbhz9Koa9Zal4ShzcxlVzlCHjSqKh5tCcKtvg2264a0nLlcOs3YwewsRslPPYEHX1oWJa7-hAvNzlBTCAOTgoQ3TIwcz-9OXqbvDwF8LEe3sJfWJ0oOk723VYmKBm5udKIYdCTDRHxgWPnihtPTTld9HMSOqEP2G9AWoz0TXsEqlL06spppgQ587465ZSatGHURHYQmMX6emLwtHpl2TKvhJFWtlcXPxLAYOkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هما میرافشار، شاعر و ترانه‌سرای نامدار ایرانی، در ۸۹ سالگی در لس‌آنجلس درگذشت.
مرتضی برجسته اشراقی، با نام هنری مرتضی، سه‌شنبه ۱۲ خرداد، در اینستاگرام نوشت که خانم افشار هفته گذشته چشم از جهان فروبست، اما خانوادهٔ او با تأخیر این خبر را منتشر کردند.
این شاعر و ترانه‌سرا، که بر اساس گزارش‌ها، سال‌ها با بیماری آلزایمر دست‌و‌پنجه نرم می‌کرد، از پُرکارترین و محبوب‌ترین ترانه‌سرایان قبل و بعد از انقلاب ۱۳۵۷ بود.
هما افشار با بسیاری از خوانندگان برجسته ایرانی از جمله حمیرا، هایده، مهستی، ستار، ابی، داریوش، معین و عارف همکاری داشت.
او در سال ۱۳۱۵ در تهران متولد شد و در جوانی با علی میرافشار، پسرعموی حمیرا، ازدواج کرد. این پیوند، دوستی نزدیکی بین هما و حمیرا ایجاد کرد که به گفته خود او، جرقهٔ تولید بسیاری از ترانه‌ها و همکاری‌های این دو با هم شد.
@
VahidHeadline
هما میرافشار، روزنامه‌نگار، شاعر و ترانه‌سرای تصنیف‌های عاشقانه موسیقی دستگاهی و آثار به یادماندنی پاپ، در ۸۹ سالگی درگذشت؛ چهره‌های نامدار موسیقی و علاقه‌مندانش در شبکه‌های اجتماعی از مقام هنری او تجلیل کردند.
او در سه مجموعه شعری بیش از هزار سروده دارد که افزون بر ۲۵۰ شعرش در زمره ماندگارترین ترانه‌های ایرانی است و بی‌دلیل نیست که در جامعه موسیقی به «زن هزار ترانه» و یا «ملکه ترانه‌سرایی ایران» معروف شد. از همین روست که ایرج جنتی عطایی، ترانه‌سرای برجسته معاصر، هما میرافشار را پیشکسوت خود می‌‌داند که «پیش از ترانه نو و در کنار آن شهره بود.»
هما پیشگام سرودن اشعاری بود که یک زن برای معشوق می‌خواند و یا حرف‌های عاشقانه‌ یک مرد برای دلبرش، چرا که تصنیف‌سرایان آن دوران به جنسیت ترانه‌ها کمتر می‌پرداختند. او سال‌ها پیش در برنامه «یک‌ حرف و دو حرف» رادیو بی‌بی‌سی به زنده‌یاد محمود خوشنام، پژوهشگر موسیقی، در این باره گفت: «منیر طاها، سیمین بهبهانی یا لعبت والا که کار می‌کردند، من ندیدم که ترانه‌هایشان بوی زنانه بدهد مگر این که از زبان مرد بیرون آمده باشد. اگر خواننده آنها مرد بوده به ناچار باید چیزی را می‌نوشتند که یک مرد به یک زن بگوید.»
«یادم می‌آید که یکی از من پرسید که شما این حالت را چگونه می‌نویسید و من در پاسخ گفتم اگر بخواهم از زبان مرد شعر بگویم، مشتاق شنیدن همان‌هایی هستم که دوست دارم از او بشنوم. آن حرف‌ها را می‌گذاردم در کلام و اکبر گلپا می‌خواند، یا می‌دادم به محمودی خوانساری می‎‌خواند اما گاه طوری می‌نوشتم که مرد یا زن هر کدام بخوانند فرقی نکند.»
....
در ابتدای دهه پنجاه بود که اشعار هما میرافشار و ملودی‌های زیبای محمد حیدری در صدر جدول بهترین‌ ترانه‌ها قرار گرفت و نام هما درخشید؛ مثل ترانه «دیوونتم» با اجرای حمیرا: «بذار بگم دیوونه‏‌تم...آره دیوونه‏‌تم من...نشکن منو به سنگ غم... چراغ خونه‌تم من...» یا ترانه «دلم می‌خواد» با اجرای هایده: «دلم می‏‌خواد که روزی صدهزار بار... بهت بگم دوست دارم عزیزم...» و یا ترانه «میکده» با صدای اکبر گلپایگانی: «هوس میکده داره دل دیوونه‏‌ی من، نمی‌‏دونه بی‏‌تو ایام بهارو چه کنه...»
...
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 244K · <a href="https://t.me/VahidOnline/75871" target="_blank">📅 18:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zroorx49rjH6saih2sKwUMe0gO9QBW1Gq34HgFNLZ9LSL_AOymIdQ_xBkhA1MQMWHkqN5Q91B61GJwINrk58x_JQ3VPLROzUDniEnZjr-IMXNnCicwy07C4oPBGSEuml2Ytub9G8sxTj0Cil8ayY0c9QS8UsnSV6cywj1CD0SABGCTGjGDKC06zLNR3N5HS7X80gETaxC5bucLorbkchCSAhQ4faSiLypNaqLIPsufb8XPPie1YUuFQPKSyQf3SuLGM1-y-HcxMRg7-thVrpQ6N6eK-DpH3Y1qxWYlZfXpt_nZ2nkAoQnbSn3nhHeosqj55cqf7viAk6mrlK-zQEjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/75870" target="_blank">📅 17:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRJAwJoootKheDgrZR3EcoWS8GisUEM3wnSbScpDo4dLDABYE7fQMZ7xMoKH3Os1EVGQLJ5m_3ZQ859TYmooisPNgHKDZZhMkkQ9dx2FNGjscz1gEDtFQEYY8C9mt4TsPTBMqS79AlOFzTg_0zyqngTBSwCbdAGg9yGC3-E0UondnYXtDRdgOhP7tsGxFB0172IJHv32B_r-UV0pUQt_zTXkT4Sny23lovN_vkLDmjIWgnu-fK9wHdTUgKEy3dAWG0XNAbDhk2BMVEysjPh2bZN-XuuVXy8HDwRWDwZydKWwB9_NVKaSTXLPsK5eKZHan-A1wvzQ3x4-vXihv_h4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام شهرداری تهران می‌گوید که برگزاری «مراسم بدرقه» و تشییع جنازهٔ علی خامنه‌ای، رهبر کشته‌شدهٔ جمهوری اسلامی، در شهرهای قم، مشهد و تهران «قطعی شده است».
به گزارش رسانه‌های ایران، محمدامین توکلی‌زاده معاون اجتماعی شهرداری تهران روز سه‌شنبه ۱۲ خرداد گفت که این نهاد «در حال تدارک برای حضور جمعیتی بیش از ۱۵ تا ۲۰ میلیون نفر در تهران هستیم».
او به زمان دقیق برگزاری این مراسم اشاره نکرد ولی گفت که احتمالا در پایان ذی‌الحجه و اوایل محرم برگزار شود.
این زمان تقریبا مصادف با اواخر خرداد و اوایل تیرماه است.
علی خامنه‌ای از ۹ اسفند پارسال که در حملات مشترک آمریکا و اسرائیل کشته شد، هنوز دفن نشده است.
معاون اجتماعی شهرداری تهران در ادامه گفت که «مراسم بدرقه» سه روز در نظر گرفته شده و در تهران قرار است ۲۴ ساعت طول بکشد.
به گفته توکلی‌زاده، محل دفن خامنه‌ای «طبق وصیت ایشان و توصیه‌های نزدیکان‌شان» در حرم امام هشتم شیعیان تعیین شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75869" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfv8qQ0DkLYWDOEvlT2aVRix4VSEBRiipFOzVp7W2eOQpopw57O-MOj9SA1ZFi_9iXvP7CLWp-i6Y7NJdNFUefGKaVr0CShDbQcHaEW-08w97zbjwhgARlhB3xRc37Z_-lehzbmqjgjSv5urYIWFvUn4KHchbFOihK5EjNTG7dMMf3o96gv3DSbDoQmYZfYn31Zt2jGGt1noIqx5NRlFJPg6N7ZiPEYn4suBp9fsSZp5iaar81XqQJaRMh6ia7rDzh23OV0i2I1-IWNGMZprHNVoTbYT9iIFd8e2RdMlHSpxJoWmrtziKdqB6dDZVltXTuQvzBoA_kFR9pUq-4yDjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از چند روز تاخیر، بانک مرکزی و مرکز آمار ایران به‌طور همزمان گزارش‌های تورمی اردیبهشت‌ماه را منتشر کردند؛ گزارش‌هایی که با وجود تفاوت در ارقام، از تداوم روند صعودی قیمت‌ها و افزایش فشار معیشتی بر خانوارها حکایت دارد.
مرکز آمار ایران تورم ماهانه خانوارهای کشور را ۸.۸ درصد، تورم نقطه‌به‌نقطه را ۸۳.۹ درصد و تورم سالانه را ۵۷.۷ درصد اعلام کرد.
همزمان بانک مرکزی با تمرکز بر مناطق شهری، تورم ماهانه را ۸.۵ درصد، تورم نقطه‌ای را ۷۷.۲ درصد و تورم سالانه را ۵۳.۹ درصد برآورد کرد.
بر اساس گزارش بانک مرکزی، شاخص کالاها در اردیبهشت‌ماه نسبت به ماه قبل ۱۰ درصد و نسبت به مدت مشابه سال گذشته ۱۱۳.۸ درصد افزایش یافته است؛ آماری که از رشد شدید هزینه خرید اقلام روزمره حکایت دارد.
اختلاف ارقام منتشر شده از سوی دو نهاد آماری به تفاوت در جامعه آماری، سال پایه، شیوه نمونه‌گیری و وزن‌دهی کالاها و خدمات بازمی‌گردد. مرکز آمار کل خانوارهای شهری و روستایی را مبنا قرار می‌دهد، در حالی که بانک مرکزی تنها مناطق شهری را بررسی می‌کند.
مقایسه آمارها با ماه‌های گذشته نیز از شتاب گرفتن روند تورمی خبر می‌دهد. تورم نقطه‌به‌نقطه که در فروردین‌ماه ۷۳.۵ درصد اعلام شده بود، در اردیبهشت به ۸۳.۹ درصد رسید؛ افزایشی بیش از ۱۰ واحد درصدی تنها در یک ماه.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 228K · <a href="https://t.me/VahidOnline/75868" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=PK27U7wQDSwtYlenaufHv11WwrfXp62bLVtAR9YcRx5U31Nj-3ApeoRzBMeZBdiV_sOR00JkgmGQ9VYwzl4HqAFf4_zKGh6_QG0ht8UNx64qbAMbZK-7Qh_ToBdveP71rJCCphkTZwNqRjS01_mImqPXhrFh5TnqgEBUdQfBgrnaGRVkyMmGtjSe5HVZ2gsVMQpIaX9VH-j2LjF7gx3dFSql_2ixpnPNmbNM8aXZxHjIqMNijMGGEHjsSpzosptE1Fcij6e3xi4v3EKF5LnA2rj9tvweK6Wbgo5u_wIGHGw4ZlFworHgKn9bklijy72D5HYAn5zUoD-m0-w-vqdBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=PK27U7wQDSwtYlenaufHv11WwrfXp62bLVtAR9YcRx5U31Nj-3ApeoRzBMeZBdiV_sOR00JkgmGQ9VYwzl4HqAFf4_zKGh6_QG0ht8UNx64qbAMbZK-7Qh_ToBdveP71rJCCphkTZwNqRjS01_mImqPXhrFh5TnqgEBUdQfBgrnaGRVkyMmGtjSe5HVZ2gsVMQpIaX9VH-j2LjF7gx3dFSql_2ixpnPNmbNM8aXZxHjIqMNijMGGEHjsSpzosptE1Fcij6e3xi4v3EKF5LnA2rj9tvweK6Wbgo5u_wIGHGw4ZlFworHgKn9bklijy72D5HYAn5zUoD-m0-w-vqdBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها دانش‌آموز روز سه‌شنبه ۱۲ خرداد با تجمع مقابل وزارت آموزش و پرورش در تهران، به تغییر قوانین کنکور، افزایش تأثیر معدل و پیامدهای جنگ بر آمادگی برای آزمون سراسری اعتراض کردند.
در ویدئوهای منتشرشده در شبکه‌های اجتماعی، شعارهایی از جمله «دانش‌آموز بیداره، از تبعیض بیزاره»، «دانش‌آموز می‌میرد، ذلت نمی‌پذیرد»، «وعده زیاد شنیدیم، عدالت و ندیدیم» و «فشار روانی کافیه، زندگی‌مونو پس بدین» شنیده می‌شود.
سیاست‌های مرتبط با کنکور از جمله افزایش تأثیر معدل و تغییر در شیوه برگزاری و زمان‌بندی آزمون‌ها، در کنار شرایط ناشی از جنگ، در ماه‌های اخیر با تغییرات و ابهام‌هایی همراه بوده که به گفته داوطلبان، موجب سردرگمی و دشواری در برنامه‌ریزی برای امتحانات نهایی و کنکور شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75867" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k3CBvpwXoF-KMR2kNsbofpDbWFpkiJ-4NgrBXlUTU6iazdJ3PdIRrnh0IIkyvwwtxH-QfBtObOGTrHRw-WycbQ1tEmSxXdMaPBcqgIvXCZCFtf1H6Vil5rXQUO1Sh-wwh1fOSmhx360WZqV2T1IpkGr8eHBb-A9a6XpfUMn4viAFihb6OekpzWeg-Trt0xiNloPyKMHrcwjMSMRijpm7LvN6mT_yUGp8xyP1dklMZjTHrUBc5Vq78YgaPGTqbBQrtwD0n-29s60stu-PIa30PnJPYknBTLWgoCqhSH7Mb6rP_ck0Bb9xCZpTYFO58qDfqEGKUZpcrnIJfitH4mLkGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای سومین بار این متن رو علیه بعضی از رسانه‌ها پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">باز هم صدای غیرمعمول پرواز یک هواپیما خیلی‌ها رو در تهران از خواب بیدار کرد.
پیام‌های دریافتی:
صدای هواپیما سعادت آباد
سلام، تهران صدای توافق میاد فکر کنم
صدای جنگنده یا هواپیما ۰۴:۰۹ غرب تهران
دوباره همین الان دقیقا ساعت ۴:۱۰ صدای شدید تر جنگنده غرب تهران
سلام تهران صدای جنگنده میاد چخبره؟؟!
مطمئن نیستم ولی غرب تهران فکر کنم صدای هواپیما یا جنگنده اومد
تهران سمت  سعادت اباد صدای جنگنده میاد
خیلی پایین بود صداش
همین الان تهران صدای کلی جنگنده اومد ک رد شدن
خیلی بلند بودن
صدای جنگنده غرب تهران
ساعت۴:۱۰صبح صدای جنگنده سمت شمال غرب میاد
تهران جنت اباد 4 09 صدا جنگنده اومد
4 و ده دقیقه صبح بالا سر شهرک نفت پونک جنگنده اومد آنتن قطع شد و وصل شد
همین الان غرب تهران حدود ۲ دقیقه صدای جنگنده اومد
دقیقن ده ثانیه پیش ساعت ۴:۱۰ ‌صبح یک‌هواپیمای از همونایی که موقع جنگ از بالا سر خونمون رد می شد
تهران حدود ساعت ۴ یه هواپیما مسافربری رد شد صداشم زیاد بود
هیچ وقت از این مسیر رد نمیشه!
توی فلایت رادارم نیست
شهرک‌ غرب ۴:۱۰
صدای جنگنده او‌مد
سلام وحید جان . ساعت حدودا ۴ و ۵ تا ۴ و ۱۰ دقیقه صبح شمال غرب تهران صدای مهیب جنگنده اومد. کاملا مشخص بود تو ارتفاع پایین داره پرواز میکنه . البته نه پدافند عمل کرد نه بعدش انفجاری شد. احتمالا برای نیرو هوایی ایران بوده
امروز سه شنبه دوازده خرداد ساعت ۴و۱۳دقیقه صبح صدای هواپیمای باری یا مسافری اومد چون چراغهای کابین و چشمک زن روشن بودن، مسیرش رو دنبال کردم مهرآباد ننشست تا جنوب تهران ادامه مسیر داد، صداش عین هواپیمایی بود که دیروز دوشنبه ساعت ۹و۱۵دقیقه صبح ، بسیار طولانی و ممتد حرکت می کرد به سمت  شمال ،چون از  کوه های البرز رد شد
صدای جنگنده نبود غرب تهران
یه هواپیمای خیلی بزرگ بود که اونقد پایین پرواز میکرد احساس کردم الانه که بخوره به ساختمون روبرویی خیلی بزرگ بود هواپیماش و خیلی پایین
پنجره باز بود دم پنجره خوابیده بودم صداش شبیه جنگنده نبود مابین جنگنده و پهپاد بود
همچین قیرقاژ داد رفتم رو هوا
سمت پونک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن موقت خطوط تلفن همراه در بعضی از شهرهای استان‌های فارس، بوشهر و هرمزگان و...
از حدد ساعت ۲
▪️
شیراز کلا قطع شده انگار
نه میشه زنگ زد نه میشه کاری کرد
▪️
کل تلفن های همراه توی شیراز قطع شده
تمام اینترنت ها قطع شده
مشخص نیست چرا اینجوری شده
نه ایرانسل نه همراه اول نه رایتل آنتن نداره
▪️
وحید از حدود ساعت ۲:۱۰ تا همین الان انتن گوشی ها و اینترنت خانگی و هر چیز مخابراتی توی شیراز پرید
همین الان [۲:۳۰] همراه اول وصل شد با سرعت کم. ایرانسل وصل نیست
▪️
شیراز خط گوشی بیشتر از ۲۰ دقیقه رفت
از ساعتای ۲:۱۰ دقیقه تا ۲:۳۰
ایرانسل هنوز نیومده
آپدیت:
ایرانسل هم وصل شد
ولی همگی 3G  هستن
سلام وحید جان بندرخمیر هم از ساعت 2 همه چیز قطع شده الان به زور وصل شدم بهتون اطلاع بدم
اصفهان هم دقایقی خط همه رفت
تو شیراز یک دفعه همه انتن ها پرید. حتی نت مودم خونه مون هم کاملا قطع شد
الان بعد از حدود نیم ساعت دوباره انتن ها اومد
وحید فکر کردم فقط واسه من اینطوریه نت خونگی مبینت ما هم قطع شده خوزستان سربندر
از شهرستان های فارس نیم ساعت همه انتن ها رفت و اینترنت مخابرات هم کار نمیکرد الان اینترنت مخابرات اومد و انتن همراه اول هم با سرعت کم اومد ایرانسل قطعه
نت و انتن و... کامل توی بندر ماهشهر پریده
اهواز هم همینطور
سلام بندرگناوه چند دقیقه کلا همه چی قطع نه زنگ نه حتی شبکه داخلی همه چی بسته شد
بندر ساعت ۲ بامداد تقریبا آنتن ها رفت
و بعد برگشت خط 3g شده اما اینترنت کار نمیکنه
الان فقط اینترنت فیبر وصل شده
دقیقا راس ساعت ۲ کل دیتا سنتر شیراز قطع شد
تلفن همراه کاملا بدون آنتن
تقریبا ۳۰ دقیقه شد که وصل شد
همین الان حدود نیم ساعت در نورآباد ممسنی همه چی پریددد نت و آنتن و خط و همه چی
😐
شیراز از ساعت 2 تا 2:30 انتن همه اپراتور ها قطع شد
بندرعباس هم همینطور، قطع شد وحید جان تا الان
اینترنت و انتن های تلفن همراه تو قشم کلا قطع شد یهو
تقریبا ۱۰ دقیقه قطع شد
هم انتن هم اینترنت همراه
بوشهر اینترنت مخابرات و ایرانسل هی ده دقیقه ده دقیقه قطع میشه
خیلیاهم کلا قطع شدن از اشناهام
شیراز بعد از نیم ساعت وصل شد
کل سرویس های ایرانسل و همراه اول و شاتل حتی اینترنت مخابرات قطع بود
خط  ایرانسل هم برگشت
وحید سلام و خسته نباشی، اینترنت و خطا برای ده دقیقه کامل قطع شدن هم بوشهر هم بندرعباس، بوشهر وصل شده و نت همراه ضعیفه منتهی بندرعباس اینترنت ایرانسل قطع شده
وحید اصلا همه‌ی استان فارس همین شد
من فسا هستم منم قطع شدم
دقیقا از ۲:۰۲ تا ۲:۳۶ قطع شدم
وحید بوشهر هم کلا قطع شد الان وصل شده و خیلی ضعیفه یه نیم ساعتی کلا آنتن نبود
میناب هم یه ۲۰ ۲۵ دقیقه ای کلا انتن نبود
بندرعباس: ایرانسل کلا قطعه، همراه هم قطع و وصله
سلام اقا وحید داخل بندر دیلم استان بوشهر ما از ساعت ۱:۴۵ دقیقه هیچی انتن نداشتیم چه ایرانسل چه همراه الان درست شد تازه نت رو h هست
با تمام سیم‌کارت‌ها ما الان وصل شدیم
مرودشتم کامل قطع شده بود همه چی الان وصل شد
سلام وجید جان
ما برازجان هستیم
برای ما هم نت ایرانسل، همراه اول و رایتل و مخابرات کلا قطع شد
الان که برگشتن 3G هستن
سلام از جنوب استان فارس پیام میدم اینترنت خانگی و همراه و همچنین آنتن از ساعت ۲ تا حدود ۳۰ دقیقه کاملا قطع بود
بوانات برا یه نیم ساعتی انتن پرید
سلام توی یزد هم آنتن همراه اول کلا قطع شد، فکر کردم باگ گوشی خودمه، اما الان که گزارشات رو دیدم ظاهرا چیز دیگه ای بوده
درود وقت بخیر شیراز حدود ۲:۱۰ دقیقه کل خط ها انتن و اینترنتشون پرید و بعد از حدود نیم ساعت با سرعت بسیار کمی وصل شد
تشکر وحید جان
سلام وحید خط بستک و کل غرب استان هرمزگان بعد ۲۰ دقیقه وصل شد
سلام وحید جان بندرعباس الان 45 دقیقس که همه چی قطعه آنتن ایرانسل اومده ولی روشن نمیشه همه چی پریده فقط فیبر نوری وصله فعلا
سلام وحید جان :استان بوشهر :کنگان از ساعت ۲:۲۳نت ایرانسل و مخابرات پریده و هنوز وصل نشده خدا میدونه چیکار میکنن.
شهرستان
قیر و کارزین
هم ایرانسل هم همراه وصل شد اما مودم مخابرات از ساعت ۲ قطع
درود. از لاهیجان پیام میدم. اینجا هم امروز اینترنت مخابرات دو بار برای چند دقیقه رفت و بعدش با سرعت خیلی کمی وصل شد.
اصفهان هم حدود ساعت دو انتن قطع شد‌ ولی چند دقیقه بعد برگشت
سلام داخل اهواز کل آنتن ها قطع شد و سریعا به حالت قبل برگشت
مجدد همه چیز پرید توی بندر ماهشهر باز الان وصل شد
وسط بازی بودم پرید بیرون انتن رفت فکر کردم خودم اینجوری ام  از ساعت دو
الان وصل شدم دیدم بچه ها هم نیستن هیچ کدوم نوراباد ممسنی
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 375K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QRh3uMix6RUnM9O7xz-wx2N3tF4NZl5dHbQJ2cH2c_VnhTmIFI09qok-clyPt-15PRCAUULeEP8z5a2OAS2xg8oecC5o90e2zcxXn6je8ePGpAmlzQ8VVmyWwHUi8jP0JWo2MkftAoNlndtZD17OqpAybv-ynL9saqLKvFeG-M1by1luz4HxNf3e3N9p_M_jxcewrM6AQwiMvnGVIhj8WN1GB-TYzizVKCdKTW95xQKlrRs4kgIQyin_et7_ZcoPDVI7u6S6MhCSqa49SgBfSmYe0TnyLivjloj2Z_h5iubHt5jLVSDBYmRI2QpxEmH1hhfBE3bNXwde_FqBfNB2kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O_kglRaCbJO5yqKsxVVjxoTRGriLwZrpp8o8ud8WUJrtB96M5z7ahCMcG7BmHFzeWYWNlDWDinwDxw5pwPqNhRzIjmIHqYSdhFXS3Obm8yP-l0beOI4jo1i4CZBVQ08aneepl35JI8NJHLjoN0GqACktXPWzvCyLdVIgFoOcdU6zFH6ELEi-tWnBtekmekVUWGxdceWhkt3xcISY3YNuLBQ77DkDwqq2GhYjEziuyWcmLU3HIHY74JTUhfQ3XBP5LRqr-OEqIkDsnTAojb1LVjiwTGIGEygvRKP2SrHSfoJOOb4rRPsZ8iKgNbLDvTh1z8dpdXfyFx1qj11RpK1N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
امروز با بی‌بی نتانیاهو گفت‌وگویی داشتم و از او خواستم وارد یک حمله بزرگ به بیروتِ لبنان نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آن‌ها پذیرفتند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب، اسرائیل هم پذیرفت که تیراندازی به آن‌ها را متوقف کند.
ببینیم این وضعیت چقدر دوام می‌آورد — امیدوارم تا ابد ادامه داشته باشد!
رئیس‌جمهور دونالد ج. ترامپ
realDonaldTrump
خیلی شبیه به
پست چند ساعت پیش
ش به نظر می‌رسه. به نظر می‌رسه همون رو بازنویسی کرده ولی قبلی رو حذف نکرده.
نظر چت‌ جی‌پی‌تی:
در اصلِ پیام، تفاوت محتواییِ بنیادی ندارد:
هر دو می‌گویند ترامپ با نتانیاهو صحبت کرده، نیروهای اسرائیلی از رفتن به بیروت منصرف شده‌اند، و از طریق نمایندگان/واسطه‌ها با حزب‌الله هم درباره توقف درگیری صحبت شده است. گزارش‌های خبری هم نسخه اول را با همین مضمون منتشر کرده‌اند.
اما متن دوم از چند جهت مهم بازنویسی و تنظیم‌شده‌تر است:
۱. ترامپ نقش خودش را پررنگ‌تر کرده
در متن اول می‌گوید:
تماس بسیار سازنده‌ای با نتانیاهو داشتم و نیروها به بیروت نمی‌روند...
اما در متن دوم می‌گوید:
از نتانیاهو خواستم وارد یک یورش بزرگ به بیروت نشود. او نیروهایش را برگرداند. ممنون بی‌بی!
یعنی متن دوم بیشتر این برداشت را القا می‌کند که ترامپ شخصا جلوی حمله بزرگ به بیروت را گرفته و نتانیاهو به درخواست او عمل کرده است.
۲. عبارت «حمله/یورش بزرگ به بیروت» اضافه شده
در متن اول فقط می‌گوید:
نیروها به بیروت نمی‌روند.
در متن دوم می‌گوید:
وارد یک major raid of Beirut, Lebanon نشود.
این مهم است، چون متن دوم وضعیت را جدی‌تر و عملیاتی‌تر تصویر می‌کند: نه فقط «نرفتن نیروها»، بلکه جلوگیری از یک عملیات بزرگ در بیروت.
۳. تماس با حزب‌الله با احتیاط بیشتری بیان شده
متن اول می‌گوید:
I had a very good call with Hezbollah
یعنی ظاهرا «تماس خیلی خوبی با حزب‌الله داشتم».
اما متن دوم می‌گوید:
I also had a conversation with Representatives of the Leaders of Hezbollah
یعنی «با نمایندگان رهبران حزب‌الله صحبت کردم».
این تغییر احتمالا برای این است که مستقیم نگویند ترامپ با خود حزب‌الله «تماس خیلی خوب» داشته؛ متن دوم آن را رسمی‌تر و غیرمستقیم‌تر می‌کند.
۴. تعهد حزب‌الله محدودتر و دقیق‌تر بیان شده
در متن اول:
all shooting will stop — Israel will not attack them, and they will not attack Israel
یعنی «همه تیراندازی‌ها متوقف می‌شود؛ اسرائیل به آنها حمله نمی‌کند و آنها به اسرائیل حمله نمی‌کنند.»
در متن دوم:
they agreed to stop shooting at Israel, and its soldiers. Likewise, Israel agreed to stop shooting at them.
اینجا حزب‌الله مشخصا متعهد می‌شود به اسرائیل و سربازانش شلیک نکند و اسرائیل هم به آنها شلیک نکند.
تفاوت ظریف این است که متن اول از «attack» استفاده می‌کند که گسترده‌تر است؛ متن دوم بیشتر روی «shooting» تمرکز دارد که ممکن است محدودتر از «حمله» باشد.
۵. متن دوم تردید و شکنندگی توافق را اضافه می‌کند
متن اول قاطعانه تمام می‌شود. اما متن دوم اضافه می‌کند:
Let’s see how long that lasts — Hopefully it will be for ETERNITY!
یعنی: «ببینیم چقدر دوام می‌آورد؛ امیدوارم برای همیشه باشد.»
این جمله نشان می‌دهد ترامپ خودش هم دوام توافق را قطعی نمی‌داند و بیشتر حالت آرزویی/نمایشی به آن می‌دهد.
جمع‌بندی کوتاه
متن اول بیشتر شبیه اعلام رسمی یک توافق فوری است.
متن دوم بیشتر شبیه بازنویسی سیاسی‌تر و شخصی‌تر همان پیام است؛ در آن ترامپ نقش خودش را برجسته‌تر کرده، تماس با حزب‌الله را غیرمستقیم‌تر توصیف کرده، عبارت «یورش بزرگ به بیروت» را اضافه کرده، و در پایان هم درباره دوام توافق تردید نشان داده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhRzgV4u7YPd97_Zezre0d01kGr2zoFYubGZY9VtOd5xtGKXQGscZ3W42TwzlD6v5Ro-I81fHxHK4RLYXGubI2TA13YlzoeQjBYxaNkYOO_w5jkCAoAtwBUFluZf_GwPieepoALwXAkJaqnzsbviNHOTlPXbXv4ksVj39NxMiexyYrpZapRlN7YQ2a7strjhsT3CY5BHJfiDKy5lqLwWl62-LsXwiiCWmW94zSprTu-0ln4auFPMlbgtIdLP1lvS3RjxB1A7wSVyvY1SR3aHJGui67NhMZPq_nBqEa2K1kTGxfX8GEITnoQtpvu8_Aor2LEQ30wHTATuOHHo_S7RkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=RPg3J088kZZSHbsjDM_fo8eBaFEYbRy1cyTt3ujTbCjG7EWdNV9JXZHzC_95NEWsGggb3dZW-LgBWe21p5aU6popJsQg-ZCpEdwWd5hkq9QxgWX0pjD-Wa8aE1TeJn7S89QKRp7Fsz0PM7mJgWaAowcIa1ZnNoQ1OOkVVJTK7G1iIDkOcxnoigZ9icaRUYBkYIR-8w1aObu-cz6wiYpz4KYO35ByHrCOsUQmFWqPqkDX_oJS7cTdKcRarEfMhfCWzxcNdNYFlEGEXPxRRz3FKGGl4hARQNvdDlwmrPjAbyE6oJt9E3tJZ-yDhWHpVDO3eS9d5GwiX4HKbTSGwcBqdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=RPg3J088kZZSHbsjDM_fo8eBaFEYbRy1cyTt3ujTbCjG7EWdNV9JXZHzC_95NEWsGggb3dZW-LgBWe21p5aU6popJsQg-ZCpEdwWd5hkq9QxgWX0pjD-Wa8aE1TeJn7S89QKRp7Fsz0PM7mJgWaAowcIa1ZnNoQ1OOkVVJTK7G1iIDkOcxnoigZ9icaRUYBkYIR-8w1aObu-cz6wiYpz4KYO35ByHrCOsUQmFWqPqkDX_oJS7cTdKcRarEfMhfCWzxcNdNYFlEGEXPxRRz3FKGGl4hARQNvdDlwmrPjAbyE6oJt9E3tJZ-yDhWHpVDO3eS9d5GwiX4HKbTSGwcBqdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kYYcVLsin2Ah0n4ctQhPpXp1LSReNCo5yX7m8cygLFZZAcdyesqe0a0bi8B9u-kB0BmC0GPVSVCTCACUms2Oo4-FIu6HAqUyHFoCFiKSP42v1iVVfKUC5coxKUp7Kapx12ZEmxKKkxZQ9C6IGZkbE-0dyKFrYs071l6IZXp8g6zvIcyY_Bdl50Dc_3gUMHZLatSFlukqTINV714sSSMprEyhnYhMkGkRjf8dOEXvI4S6Bzapre0SjncC6Ao4AChA5JqEhuGc5zIV818hsjJ_xAIxZwWkm9WxO7jywhqDnnQJc-9zRdHN0HbtgK4DiPVQqqU-wfzTZNNMkRnCSip_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام دونالد ترامپ مبنی بر موافقت بنیامین نتانیاهو با توقف گسیل نظامیان به بیروت، در شامگاه دوشنبه ۱۱ خرداد ماه، با واکنش منفی چند چهره شاخص سیاسی در اسرائیل مواجه شد.
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، با انتقاد از این تصمیم گفت: «زمان آن رسیده که به ترامپ نه بگوییم.»
همزمان نفتالی بنت، نخست‌وزیر پیشین اسرائیل، نیز در پیامی دولت این کشور را به ناتوانی در حفظ امنیت متهم کرد. او با اشاره به حوادث امنیتی در اورشلیم، بیت‌شمش، لبنان و غزه نوشت: «مکان‌ها متفاوت هستند، اما داستان یکی است؛ دولتی که کنترل بر حاکمیت اسرائیل را از دست داده است.»
بنت همچنین گفت: «هرج‌ومرج در همه‌جا دیده می‌شود و ما امنیت را به شهروندان اسرائیل بازخواهیم گرداند.»
یائیر لاپید، رهبر مخالفان دولت اسرائیل، نیز با انتقاد از نتانیاهو، تصمیم او را «اعلام تبدیل اسرائیل به یک دولت تحت‌الحمایه کامل» توصیف کرد.
@
VahidOOnLine
دفتر نخست‌وزیر اسرائیل در بیانیه‌ای به نقل از نتانیاهو اعلام کرد: «امشب با رئیس‌جمهوری ترامپ صحبت کردم و به او گفتم اگر حزب‌الله حمله به شهرها و شهروندان ما را متوقف نکند، اسرائیل اهداف تروریستی را در بیروت هدف قرار خواهد داد.»
نتانیاهو افزود: «موضع ما در این زمینه تغییری نکرده است.»
او همچنین تاکید کرد ارتش اسرائیل به عملیات خود در جنوب لبنان طبق برنامه ادامه خواهد داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p4S3mukqJ-SC5t038mnFVg_9P-8tQhSne-opfrZ__7UK7OiWW53zB2-HgbnZ1RIa469VD1r52XFujvMAlCdOueLJa2b7DIeCMdOAw8lrIbEunnBqGW59JvZaWrT3uGU3hREm6O_hRnHNoPgyP0qjpgSz2z5yr1Q7gG2trTg6APBSfe0_-MJ9AlnLKQVXgG0qpyExEk2-BHReoj3YCg0rnz2CgL1AuQ_XQOwDRsxNPr3ZKj1gxA1XkEAuYvOC_A8uYFx4Sy8sb_hpq6czZ_yhkfa530WMapvbYDv1ZxN3mARvYFE80OuFWEewzw7PUmWRo4mxGG_wWRfBQR-R5rcwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی: ادامه حملات به لبنان و غزه، باب‌المندب را به تنگه هرمز تبدیل خواهد کرد
اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، شامگاه دوشنبه ۱۱ خرداد ماه در پیامی که رسانه‌های دولتی ایران منتشر کرده‌اند، نوشت جنگ اسرائیل در لبنان و غزه «در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعال‌سازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگه باب‌المندب با تنگه هرمز رقم خواهد زد.»
فرمانده نیروی قدس سپاه همچنین هشدار داد که ادامه عملیات اسرائیل در جنوب لبنان و غزه، این کشور را با واکنش‌های گسترده‌تری از سوی حزب‌الله و گروه‌های فلسطینی روبه‌رو خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75857" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lU43Yl0KifUi1JemGO456hh4mevJvJKVTH2DTAJeY0EpI3WRdoHfdgHPFsqDSHgkEC9Oarjfy35XcZyeAiLFvjww1ikVNlRQ6PbquANZmAYjovDxyaHBDnp0e5xpXfsOeqHmCVG5v2adwC3MNIO90KhwGw3tmeOZIAw9XmBbVWUEwTeyNCh5MQy83JqvindJQH8S-9k9gLK1rfntPEUixIFJyjMMytO4m9mLDlcN3rICdvaFw04TB0da10v3d8UfPGg_8MBKPBnO_wffS3TDXab4_NGU4kYItiFCbkL5a9CVAj6R-YTZ8A8JT9HInVog3XCUyP_r6kr-UnI9bZmmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با جمهوری اسلامی ایران با سرعتی بالا ادامه دارد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
این دفعه گفت "جمهوری اسلامی ایران"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/75856" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YjNY-OqkM51uJdkqwOmH-Gfc32P6X89mXhzjF55GRP-xRPUC9PombMgdWvXCAOpUaqh8ogP--XrVelSUxN5te6n9BE66LBbRGF_nxFYTHRM8QXbyMXTkR40AtcrUOUtuGTEfOrJ7Odfe0cN1m_M2n_XSGGycsrAQok8sz-U9CS8g8EocEQ30g-iAie4RFYwtGmHqPTfKD0yDgco_OLXaSRqYi0M9Mr700SqHVO-NMvqJJT5GS7pCSbtVl7ccRMr3ufW1gGveD69l08D3Ebw4Smx4pUb0bz4HkPBBBdICmkuHVZGhYjlHcwObg9aq4MwGtFZ6O1CRYcNw05P76tQmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و حزب‌الله پذیرفتند حمله‌ها متوقف شود
ترجمه ماشین:
من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل، بی‌بی نتانیاهو، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد؛ و هر نیرویی هم که در مسیر بوده، همین حالا بازگردانده شده است.
همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها پذیرفتند که همه تیراندازی‌ها متوقف شود — اینکه اسرائیل به آن‌ها حمله نکند و آن‌ها هم به اسرائیل حمله نکنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75855" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uvS6z5kGYKXFQMZwbamszISam2HOrQAGsGG94PF0XXguzxscHEwbeCwUuqIhP46m0XAOG03N7Zm21Iq9VEt5fU4jXauuQKCAyH0s9Q6dxr-csg4-BftkQ7LmgWPYctyiz4h91k70CYld4_UV5t9gWd4qHbCX4zg07vautPf-CE20Ohvjln7shaOQQmsV43sz_DESSiDKuGqO5mPkCtH8xczQnZB34trqDBg7AuQHjMEzMb9uCLLE4vwNnevU93s-RExqlgus4R_35MZn3rOSzP0-d2fkmgebjdj-j2yU3dT-1OALdSM3U7fVFyDX3UinSBd_muH6Arg4Hk-mRM3unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: محاصره را حفظ می‌کنیم
توییت‌های خبرنگار NBC، ترجمه ماشین:
تازه: رئیس‌جمهور ترامپ به من گفت که درباره گزارش‌ها مبنی بر تعلیق مذاکرات ایران با آمریکا، چیزی از ایران نشنیده است؛ اما اگر درست باشد، اشکالی ندارد:
«فکر می‌کنم اگر حقیقت را بخواهید، زیادی حرف زده‌ایم. به نظرم سکوت کردن خیلی خوب خواهد بود، و این می‌تواند برای مدتی طولانی باشد.»
او ادامه داد: «این به آن معنا نیست که قرار است برویم و همه‌جا آنجا بمب بریزیم. فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم. محاصره یک تکه فولاد است.»
آیا می‌تواند آن‌ها را آن‌قدر منتظر بگذارد تا کوتاه بیایند؟
«فکر می‌کنم تا هر وقت که بخواهند می‌توانم صبر کنم. آن‌ها دارند ثروت هنگفتی از دست می‌دهند...»
همچنین وقتی از نویسنده کتاب «هنر معامله» درباره گزارش‌های تعلیق مذاکرات پرسیدم به نظر می‌رسید با اکراه نوعی احترام برای مذاکره‌کنندگان ایرانی قائل است:
«این حرف مناسبی است، چون آن‌ها مذاکره‌کنندگان بهتری هستند تا جنگجو.»
GarrettHaake
الان هم:
ترامپ و نتانیاهو دارند تلفنی صحبت میکنند.
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75854" target="_blank">📅 20:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j4HkqKKv7b08N-1tGxLsvvnbugjYV4r-_F2yG4h9FhjmyUSFybUvoxg8AFPcq-GQcClvsmA0ca-GPgvVdsNyYrpxAmqgNZOK2eWjnQ5-yy3w4CMWQZpx-UeseFIPoKbs0dxXUsGrC-zkVU5rtsi7QI2_XcOILpvso9OfJU3rntfXwcNBNuJIfgwK_z2RzwyH_N573Y93vUSVkEDtDp75kfxrXFECk2GIWfWt5zD2RZGhiiIG_gC9zMD1jd6NDzCwi6NZUEjHeTY8rEDL_pznzP488BolWSn4Rs3XkqVQw8fidec_Tpy-5UxH2N0KSR9RNiY8C7pqI9Do9ftBY2qzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با صدور هشدار تخلیه از سوی ارتش اسراییل برای ساکنان حومه جنوبی بیروت، فرمانده قرارگاه مرکزی خاتم‌الانبیا به ساکنان مناطق شمالی اسراییل هشدار داد که در صورت عملی شدن تهدیدهای اسراییل علیه لبنان، برای جلوگیری از آسیب، این مناطق را ترک کنند.
علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، اعلام کرد بنیامین نتانیاهو «در ادامه شرارت‌های خود در منطقه»، ضاحیه و بیروت را به بمباران تهدید کرده و برای ساکنان این مناطق هشدار تخلیه صادر کرده است.
او افزود: «با توجه به نقض مکرر آتش‌بس توسط اسراییل، در صورت عملی شدن این تهدید، به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/75853" target="_blank">📅 19:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=XzXZVGfzsDIfNDi1wupCeK6ZoLFuec-wEtKj9H5VH0Sg3QEcupgNbojNcw0Zlaqiok8S4k8vPCHOkVQ47G0_RCok1IrD0PW6tCKrpCankaOZSk4JfhoFcLt-2BouNX0T0nbRSifm0vX1nHLu8TlB4onjBdej48q3a73LeNnt3rflI-1jEORLnwHjW2eLCViKWrqcvrCi90VRnvkAVdSbOxc76NQJqDyqQWS9AxFdJmQnceEujjnYfBz01LJD09Tc3M582P6Kf4Kpo5VJe1LNLTH8CJMHtM2jICF0HgPT4T8hdHXFHhjqiN6WYHAh9-LGTbSZXvmw43wz8aDejV6kmw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=XzXZVGfzsDIfNDi1wupCeK6ZoLFuec-wEtKj9H5VH0Sg3QEcupgNbojNcw0Zlaqiok8S4k8vPCHOkVQ47G0_RCok1IrD0PW6tCKrpCankaOZSk4JfhoFcLt-2BouNX0T0nbRSifm0vX1nHLu8TlB4onjBdej48q3a73LeNnt3rflI-1jEORLnwHjW2eLCViKWrqcvrCi90VRnvkAVdSbOxc76NQJqDyqQWS9AxFdJmQnceEujjnYfBz01LJD09Tc3M582P6Kf4Kpo5VJe1LNLTH8CJMHtM2jICF0HgPT4T8hdHXFHhjqiN6WYHAh9-LGTbSZXvmw43wz8aDejV6kmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«حمید سلیمیان» در حال نواختن تنبک
#حمید_سلیمیان
، متأهل و پدر یک پسر چهارماهه شامگاه ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در زرین‌شهر اصفهان با شلیک مستقیم گلوله جنگی جان خود را از دست داد.
حمید سلیمیان راننده یکی از شرکت‌های فولاد بود و به گفته نزدیکانش به موسیقی علاقه فراوانی داشت او  تنبک و سنتور می‌نواخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/75852" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/U7J5lw8pWOrRuitud9yU7CTIagATOYu9CchB-najEPL4IGDx_1sNTa3VjFY0KH7GjHMIdklCG7TGDB-MgzBx-a9BG_hMlhpsAIHoAgP8iNZql-kOjv8-JDEU_la3m6I0M51qDnbZ4CPUodJSbu9Td_42JzoJqM78DLuzOX7MbtWg9gx8duarzSUFqNxYsMXet2DT1SEA3dPhMcinGFKL-8EoCXoEIOdFP-kUm31EO-jt9VOBtDkr7a6mx7PRcSY5cA_GtEYzo122Dc8YYGrAMF2OHVd4IiceZbNTvREUd_BYLcrmyo08Cw_bzkFz0smL0MozvJYlxCuZlD_5lNkUag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FF11ChChWHoyjlqyZMl1ObqCpR9zdpqYUYOMUDHacbyPoUfZ3ZA5s29uqSLDZmKdRf0opTpa8osvZNO3nCP8dnW8gizbxbpddDF2YPPnET6WOP4yG6QYcoD1Rl3VKrxnY6qpx80Qz7ulhLQs7dQ5yeJ-8Ia4vSq95L8oZEmH7udDpunffn2lYWYNeeSQrbXhLqzYrbzL0zzwAoZFewhUu9FGqMQjZgqMGrNM9JucJ9k8bVaLtK54f7q9cDUmne50JELUprVkxjl5HAZoZyJ-LakllzeFy7e6rBJmpGNlEEACeIeVkovsNkmhAznoPuYRFnsJR2L0lUhkoYiPmCOEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UofhB6Zdgsx3Po9av1dBBo6CAtCjTqHXpiGm4ZwExYehCTjTqeWHNP-MdY8wL-jCbgh_KVMd6x1aYK7OiVFgNQJnBQ8maouuiYX2LMDP_Wb6ztSPQRNpeNaPjsyu88N9eakingVady2fYqsnJ6TNtr8-t1FNQfbhA33VKrBblesiqkZU6BktP7SwTFTel4rSuUEiKz2MXkOVxROvrrm1IPAnjcmj75XiVH-WRULfrwxUGzNdECl9-GMQO4ArAFMsn1kke9oibjn2Ju0yLY5IhZ7RlsWvsSvbDnw3ppV9t3bEUlKPfehWCeu2D5sIFamOvqA3ZPWeJXDpJr6zuG3BhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r2X158Q8g5nL1UDRfGTuzqCoJQmsTXZJuMSxD7bj-E3TCwLPjld4-eDfxwKIJAW6FRI_sg09Sfh9-1I6qdspID_uPcANqFo3eAa59GbQw93Fw2KPWhietbFNaqyI0D1SL6--c10OviTxbPd-CiZ2MWpDLtqYJVIla1R28WHRK8WA610tyUKle2sF_QkIJ102--AyCi-SJVNRKTEtuEQlw3O314jt5T11GAyE5H1Gpl28Pq4hdftgOPnY6Z3gPLjaQNOMeJv-HSW4IOUTmpg-QB9iUXKQVqs8_GI8g8SsHpXpCQB1sJ5WpkYz_LO60n1fPqiJ8jqNIi8Mo5BDOZCqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FJRulMM_Pv_tI1PPDX-I64XL0_t32PRpMZ6GFx-gxcG2RKgUqKrDU_vIlBzjeXKpDwll9jcIffDSkeV-4-YuIV9rT1iJGC6P9ynpHRLEG63DSL0xlEj0WaqPKzqkq4hzh99WyBChNH9EYBhhmINIAlfa_UbnVMzx0MbxoIFScvclXn4oaNRZOR2Ky6Zy73sBMcuRI4WyKj4RwEmWKbdmOa85DmJ31ssDU8y7d_JKwDOrOXoOFDdR6Alqetr8ybvEjdQcBDMvhucdkUYnRL4NPhvQWSvSUsY51wArCWjw4FQRePNrru0jX6tdce8xhVqSCEpKQa3SqC0FtebFzHEgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HbwneLDy2SFKFYP3J7hvFJPAKUMozzAma1Dc1kKRUZRDYIegKfehI5QvqB5cSKi1FqU76leDVzWeQzyy5rJ4MDoG3041bxZTGRzf6SOdNzWntdJ_9tFQuohD3-ADkQS0e7FbO9nmuo4F8487GrIQoCNn0FM2s0V9B38J8X2ZQJBtT6YmTzw3ufwFqU0YdRPzu-wlELIIBgdTOzjwOB0nKl_t7Vgv3TpHzIe7SAWW14rcdf-PmcNQW3EpiLnEFAdpFKftqOfYKAFGzPTGNmn_3uoASVeqcQmt4LSaJPN3qECuwSn2Npi4-GoIro4Ss7ugMAZf_7J42m12GwUylyaB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OoZsqXP2fKwrI99BPKA8SDOAT5oAsVJcfWUfBnNOIiodF4ujNQsPPAsexQuJuAq1K2o1hOboGLE26tMT4mowbFiX1UwhyRRMps07dqN338DdEZYwU1Jzq9VO3QovF_75vZN76GrAG4mvJ2QooUVbF4HPHytwBdt24zFCceQ6kfYdKowGett91pBvWu4U-vI1SVKQ0k-NPRSDyzlkv0v7mNFJPbNJeCcfZq-rU36PYriZT1rqmgUOPo1mW6yzMhxyaIuHTrkQ_yNmTW-lYB3_oCA5kmo1EhbYl5H3J_z5N6_GukQAzfVgfAZSI3IQHHy8DlEtO58wSvc7Lx1e5OM3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CRG7GJDSgPPYs9DSMFTx_P9BpFzk183Q5L3zjPcwVNLE9r-Iyxd7ZDXKyQCmCJQcaD5UeYZ7VoKJo3bODPM1IxZMrn2uOd8BMtK7a838VWAJ_uc07m1XhgxA2hr9bjknX9oPdT20GhGGbxcGulplBCgAy2NO781A__mBvmOqHm_almoHraJ2hoWmOwJgRf8cxEOzB9VWwHktE0GUo2p_BHi8Ge5Snv9upwvanB3IhXtrrmHIcqX5bg_WlbVLObtL_Gg7QagwbcKDx67l6BiSfnVtZX-ZXNiQ8HzL6xi8ipLUMzy_Kd8VA6iPgLuNmE-2UoIVQhUIhnpbS9LwFWbgVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xs7jNWQNHRfEx4dSw_nYo-sqSQ6vO2j6XfBo2yQv_WE0d0U6idoe6ng1e7ogigS3n2S6Rzi9tYK0eezn1RXmeaTI1mxvkZPZxa5NFdXyvkgkVfnu7JKWR77wtMgbJVk0-8KuXf2kJ_t38nPnJMJ8se4uhUshJto23nUS68jw5mg0noKIXE8e_KI7ITapI8R1pvbUKoGzaQRJVgkEvfyG_vsTnbSpyD4ulHD76x0IRal_GZHE4diLbXsUCf5GqersH-RzkgrHHPFXDzrmpGOnRWMCD9XodYkngBn3oCOjgqJRmvT9_RJJYbSFZY3s---1kxuGTM99QKtDTNrIT-IW6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هم‌زمان با تشدید حملات نظامی اسراییل به لبنان، مقام‌های جمهوری اسلامی بار دیگر تاکید کردند که هرگونه آتش‌بس میان ایران و آمریکا باید شامل همه جبهه‌های درگیری، به‌ویژه لبنان، باشد و هشدار دادند ادامه حملات به این کشور می‌تواند پیامدهایی در پی داشته باشد.
بنیامین نتانیاهو، نخست‌وزیر اسراییل، روز دوشنبه ۱۱ خرداد ۱۴۰۵، اعلام کرد که به ارتش این کشور دستور داده است اهداف متعلق به حزب‌الله در ضاحیه، حومه جنوبی بیروت، را هدف قرار دهد. او در یک پیام ویدیویی گفت: «هیچ وضعیتی وجود نخواهد داشت که حزب‌الله شهرها و شهروندان ما را هدف قرار دهد اما مقرهای تروریستی آن در ضاحیه بیروت از حمله مصون بماند.»
دفتر نخست‌وزیر اسراییل در بیانیه‌ای اعلام کرد نتانیاهو و یسراییل کاتس، وزیر دفاع این کشور، در پی آنچه «نقض مکرر آتش‌بس از سوی حزب‌الله» و «حملات علیه شهرها و شهروندان اسراییل» خوانده شده، به ارتش دستور حمله به «اهداف تروریستی» در حومه جنوبی بیروت را داده‌اند.
نتانیاهو همچنین گفت عملیات زمینی ارتش اسراییل در لبنان در حال گسترش است. اسراییل در جنوب لبنان منطقه‌ای امنیتی ایجاد کرده و می‌گوید هدف از آن جلوگیری از حملات حزب‌الله به مناطق شمالی این کشور است.
در واکنش به این تحولات، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، در شبکه ایکس نوشت: «آتش‌بس میان ایران و آمریکا، بدون هیچ ابهامی، آتش‌بسی در تمام جبهه‌ها، از جمله لبنان، است.» او افزود نقض آتش‌بس در هر جبهه‌ای «به معنای نقض آتش‌بس در تمامی جبهه‌ها» خواهد بود.
عراقچی همچنین آمریکا و اسراییل را مسوول پیامدهای هرگونه نقض این آتش‌بس دانست. جمهوری اسلامی پیش از این نیز بارها اعلام کرده بود که آتش‌بس میان ایران و آمریکا باید سایر جبهه‌های درگیری، به‌ویژه لبنان، را نیز در بر بگیرد.
ابوالفضل شکارچی، سخنگوی نیروهای مسلح جمهوری اسلامی، نیز به اسراییل هشدار داد که «تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود.»
هم‌زمان، محمدباقر قالیباف، رییس مجلس شورای اسلامی و رییس هیات مذاکره‌کننده ایران با آمریکا، با اشاره به آنچه «محاصره دریایی و تشدید جنایات جنگی در لبنان» خواند، این اقدامات را «شواهد آشکار عدم پایبندی آمریکا به آتش‌بس» توصیف کرد.
قالیباف در پیامی به زبان انگلیسی در شبکه ایکس، بدون اشاره به جزییات بیشتر، نوشت: «هر انتخابی بهایی دارد و زمان پرداخت آن فرا می‌رسد. همه‌چیز در نهایت سر جای خود قرار خواهد گرفت.»
این اظهارات در حالی مطرح می‌شود که عملیات نظامی اسراییل علیه حزب‌الله، از گروه‌های مورد حمایت جمهوری اسلامی در منطقه، شدت گرفته است. با وجود تاکید مکرر تهران بر ضرورت گنجاندن لبنان در هر توافق آتش‌بس میان ایران و آمریکا، این مطالبه تاکنون محقق نشده است.
اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، نیز روز دوشنبه در نشست خبری هفتگی خود گفت: «ما تاکید کردیم و کماکان تاکید داریم بر این نکته که آتش‌بس در لبنان بخش لاینفک هرگونه آتش‌بس و هرگونه توافق نهایی برای خاتمه جنگ است.»
او همچنین حملات اسراییل به لبنان را از عوامل ایجاد تاخیر در روند دیپلماتیک برای پایان دادن به جنگ میان ایران و آمریکا دانست و بار دیگر بر ضرورت برقراری آتش‌بس در لبنان به عنوان بخشی جدایی‌ناپذیر از هر توافق نهایی تاکید کرد.
@
VahidHeadline
تازه‌تر:
خبرگزاری تسنیم، وابسته به سپاه پاسداران، گزارش داد که جمهوری اسلامی در واکنش به ادامه حملات اسراییل به لبنان و آنچه «نقض آتش‌بس در همه جبهه‌ها» خوانده شده، روند گفت‌وگوها و تبادل پیام با آمریکا از طریق میانجی‌ها را متوقف خواهد کرد.
تسنیم همچنین مدعی شده است که ایران و گروه‌های هم‌پیمان آن در «جبهه مقاومت» در حال بررسی اقداماتی از جمله انسداد تنگه هرمز و فعال‌سازی سایر جبهه‌ها از جمله تنگه باب‌المندب هستند. این گزارش می‌گوید این اقدامات با هدف واکنش به حملات اسراییل و حامیان آن در دستور کار قرار گرفته است.
@
VahidHeadline
ارتش اسرائیل در بیانیه‌ای به ساکنان منطقه ضاحیه در جنوب بیروت هشدار داد و از آن‌ها خواست برای حفظ جان خود این منطقه را تخلیه کنند.
در این بیانیه آمده است اگر حزب‌الله به شلیک راکت به سوی شهرها و شهرک‌های اسرائیل ادامه دهد، ارتش اسرائیل اهدافی را در ضاحیه جنوبی هدف قرار خواهد داد.
در ادامه تاکید شده است دولت اسرائیل با مردم لبنان در حال جنگ نیست، بلکه با سازمان تروریستی حزب‌الله می‌جنگد.
@
VahidOOnLine
در پی اعلام خبرگزاری تسنیم مبنی بر توقف «گفتگوها و تبادل متون از طریق میانجی» میان تهران و واشنگتن، بهای جهانی نفت بیش از ۵ درصد افزایش یافت و به بالاترین سطح خود در هفته‌های اخیر رسید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/75843" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lnbek6k34lm_wDfGl7I8KgbTa6ezPBj7wtarSqCN98BsiQG2GKOke9yflN9W9h0QCXVqBSHlBlbXJR2HvHG-Xv3Za5XJdsamy1f8jMpsPo-gfNxWQB4WMaKOJv2CbQ04zlQzHd5VAPmm2Gota5lWeM_Lk_khudMS5_o_2Vd6nIipx7Hy3twBIgQ64JXdiTc4nsJbYZetVm9TVGfgSPANlQL4fNDTWPDc_qdeTd8oCnUMaFlK09L7hBh2tW4RuFS4nFSn9N3neWoKEwvLVrjnXglVEqwkEFCYiz8LW5YHRlxGGbFyeHs0ACfbYGqUmkGSso5f4-EfqdGqyyoP7VzBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از کشته شدن یک دانشجوی زن در دانشکده دندانپزشکی قزوین به ضرب گلوله خبر داده‌اند.
میزان، خبرگزاری قوه قضائیه، از قول دادستان قزوین نوشت: «بررسی‌های اولیه نشان می‌دهد این دو دانشجو که در آستانه فارغ‌التحصیلی قرار داشتند، در مرحله متارکه از یک رابطه عاطفی بوده و پیش از این نیز اختلافات خانوادگی شدیدی با یکدیگر داشتند. صبح امروز، مرد جوان با یک قبضه سلاح کلت جنگی وارد محوطه درمانگاه شده و چهار گلوله به ناحیه سینه دانشجوی دختر شلیک کرده است. شدت جراحات وارده به‌حدی بوده که متأسفانه وی در همان محل جان خود را از دست می‌دهد.
در اطلاعیه دانشگاه علوم پزشکی قزوین در این باره آمده است: «انگیزه این واقعه، مسایل شخصی و خانوادگی بوده و ارتباطی با فرآیندهای اداری یا محیط آموزشی دانشکده ندارد.»
به گفته حمیدرضا قافله باشی، رئیس دانشگاه علوم پزشکی قزوین، «این تیراندازی به دلیل خصومت‌ خانوادگی اتفاق افتاده و دو دانشجو که زن و شوهر بودند در اثر شلیک جان خود را از دست داده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75842" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پیام‌های دریافتی از تهران درباره صدای پرواز یک جنگنده یا هواپیمایی دیگر مربوط به جمهوری اسلامی:
سلام تهران صدای جنگنده اومد همین الان
غرب تهران وحشتناک صدا جنگنده میاد ۹:۱۵
صدای جنگنده داره میاد غرب تهرانم ساعت ۹.۱۴
سلام وحید همین الان تهران صدای جنگنده میومد نزدیک ۲ دقیقه
شمال شرق تهران صدای جنگنده
سلام تهران صدا جنگنده شدید
الان از بالا سر ما صدای جنگنده اومد
رد شد رفت
همین الان منطقه گیشا صدای جنگنده میاد
همین الان ساعت ۹:۱۵ دقیقه صدای جنگنده سمت غرب تهران اومد(فکر میکنم جنگنده ارتش بوده باشه)
سلام وحید از سمت لویزان تهران موشک بلند شد
وحید الان ساعت ۹:۱۵ صدا جت منطقه ۲ تهران
تهران-فرمانيه
ساعت 9;16 صداي جنگنده مياد
وحید تهران ساعت ۹:۱۷ صدا جت میاد زیاد
هروی
الو سلام تهران سمت شهرک غرب صدای نمیدونم هواپیما بود جنگنده بود چی بود خیلی نزدیک بود
الان ساعت ۹:۱۷ دقیقه در قیطریه صدای جنگنده اومد
شرق تهران صدای جنگنده شنیده شد الان
سلام تهران صدا جنگنده شدید
احتمالا جنگنده های خودشونه
ساعت۹:۱۷
سلام دوشنبه تهران ساعت ۹:۱۵ صدا جنگنده من شنیدم سمت هروی
صدای جنگنده تهران ۹:۱۷
صدای جنگنده منطقه ۳
خیلی پایین بود
تهران صدای جنگنده اومد
سلام ساعت ۹:۱۵ سمت دروس تهران صدای جنگنده اومد
صدای جنگنده شمال تهران ساعت ۹:۱۵ رقیقه
سلام ساعت ۰۹۱۵ دوشنبه صدای پرواز چند جنگنده شمال تهران
منطقه ۳ صدای جنگنده انقدر زیاد و وحشتناک بود که از خواب بیدار شدم
سلام  پاسدارانیم صدای جنگنده اومد چند دقیقه پیش
صدای جنگده نارمک
سلام وحید. صدایی که ۹:۱۵ اومد شبیه جنگنده بود ولی از پنجره نگاه کردم شبیه هواپیمای مسافربری بود فقط نمیدونم چرا از ارتفاع کم حرکت میکرد
سلام آقا وحید من خونم گیشاسصدای جنگنده نبود هواپیما بود من بالای خونه رفتم دیدم ولی هواپیما بزرگ بود ی مقدار دیگه باری بود یا سواری نمیدونم ولی از بالای گیشا رد شد
من از روستای اطراف شهریارهستم یه هواپیمای مسافربری بزرگ تو ارتفاع پایین از بالا سرمون رد شد به وضوح دیدمش صداش زیاد بود
سلام وقت بخیر نیاورانم صدای جنگنده اومد وحشتناک بود
وحید من شهرک محلاتیم
بین ۹:۱۵ تا ۹:۲۰ صدای جنگنده میومد
(با ارتفاع پایین)
سلام وحید جان صدای وحشتناک جنگنده ۳ ۴ دقیقه پیش خونرو لرزوند
-هواپیمای کارگو سپاه از تهران بلند شد
.
-صدای جنگنده برای این بود؟
-ممکنه برای اسکورتش بوده باشه
J74wabx
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 418K · <a href="https://t.me/VahidOnline/75841" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">پیام‌های دریافتی از
#بندرعباس
درباره شنیده شدن صدای سه انفجار:
بندرعباس ساعت ۹:۰۷ سه تا انفجار
الان بندرعباس ساعت 9:7 دقیقه 3انفجار قوی
یک صداهایی شبیه برخورد جسم سنگین (بمب یا هرچی) به زمین داره میاد از دوردست.
بندرعباس ساعت ۹:۰۹ صبح دوشنبه
سه تا صدای  انفجار اومد بندرعباس
ساعت ۹ و هشت دقیقه
دوشنبه، ۱۱ خرداد ۹:۰۷ صبح. بندرعباس.
صدای ۳ تا انفجار از نزدیکی پایگاه هوایی شنیده شد.
آپدیت:
خبرگزاری تسنیم وابسته به سپاه مدعی شده که مربوط به مهمات خنثی نشده بوده. البته دو روز پیش‌تر از این هم اعلام کرده بودند که طی ۷۲ ساعت آینده قراره از این صداها شنیده بشه در بندرعباس.
پیام‌های دریافتی از
#اصفهان
درباره شنیده شدن دو صدای انفجار از دور:
پیام ساعت ۹:۱۷: اصفهان صدای انفجار میاد، دو بار پشت سر هم
اصفهان همین الان صدای انفجار اومد سمت ناحیه ۶
الان اصفهان یه صدایی مثل صدای انفجار اومد
سلام وحید، اصفهان ساعت ۹:۱۸ ۲تا صدا مثل انفجار و کمی لرزش حس کردم فاصلش خیلی دور بود، بین ساعت ۸ تا ۹ هم یک صدای مشابه اومد فکر کردم توهم زدم
اصفهان صدا انفجار نزدیکای جی شیر(مطمئن نیستم)
سلام. اصفهان حدود ساعت ۹:۱۵ صدای ۲ تا انفجار به فاصله چند ثانیه.
نمی دونم چیزی زدن یا دارند مهمات خنثی می کنند. البته تقریبا هر روز صبح یه صدا میاد که به خنثی سازی میخوره.
امروز ۲ تا پشت سر هم بود.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/75840" target="_blank">📅 09:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nWrZV2_oSY4surq9JMOk0zd9yDQ1jHzutGoHkKsMCrrsQxitIe783m__LVxET93Uv4AlPz3CZsR7hly1ycyMRGdCsLyvHeDTP6KlDy3x32CBtDFVfix2fHCK0WMVW12OsKMlHRw5B6S4p37fHL-YLzPDgvT42fOG3UJ1kenwD612HmBm3i-_O2JBGBAC96MZVcsBbZAryWkLNWLWE4v9tDnVvE9iOKKven7CuIz3E5vPvgrdkhJlummnEgVOLV-XIU1XuHSrC-nDgl1M0Df7VrDmId_cW96pdiOSQJL6y3ZRwEKp_4AIx8PF9ZS5muVeKhvFF71TZOlF6LqO8AN-ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌های کودن و بعضی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند وقتی سیاسی‌کارها مدام و با شدتی بی‌سابقه غر می‌زنند که باید سریع‌تر حرکت کنم، یا کندتر، یا جنگ کنم، یا جنگ نکنم، یا هر چیز دیگری، کار درست و مذاکره برای من خیلی سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور است!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 391K · <a href="https://t.me/VahidOnline/75839" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پیام‌های دریافتی:
امیدیه خوزستان صدای انفجار شنیده میشه
از امیدیه خوزستان پیام میدم
طرفای ساعت ۸:۱۳ دقیقه صدای ترکیدن اومد
ساعت ۸:۳۱ دوباره زدن
همین چند دقیقه پیش صدای انفجار واضح ای اومد
امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75838" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد [گیشا]»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» اعدام کرده است.
نام این دو معترض که بامداد دوشنبه یازدهم خرداد اعدام شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
میزان نوشته این دو «از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران [بودند] که اقدام به تخریب و آتش‌زدن مسجد، تخریب اموال عمومی، درگیری با مأموران حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند.»
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 370K · <a href="https://t.me/VahidOnline/75836" target="_blank">📅 08:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Tc3kFVV5GidLXVSTk-jZdKbRj4ZrUf-gLRUKwoq4rH3QejAgX-ownG6niGXxr0yTkBPaA61aJng02DQyVSIEyb0ZE1XgS8ZtAFlkuWL5MAqi_t5qrYEsKGLGSvgNjV5u-l04EncRoh8QycF1wWnLxVExhfJTvyI74yEjcYkJVona7_HNVgBjpNsuAUvc2beo4OwVwUwpv4DqSS7_V-h2zyXP9GZwcGSntirdPQKwUmrpsbDCAE6vo648IJ9_k2fC7ezpBzxEMM3nHP08Im1VLhhrL17TeCZtM5yOFNa2Y-B0pZzfRMAnAbtdp274wS_vkGP6t6bkISEdII-AFln2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rF6fbeJLGOHYHUDzHo-V8DL2VkbUGAV86uglCUpDr94-Q2vsRFmcCjbJGO2XxX9KL11dXiJt5lgNjVsp-cpp7AbwVMeB69oxv6FV_7F63ZK1m2sXK_oZjXcnYG_oxYgamIBExBVLX4vOaFHt66ax4tRt0kplkOjj6cegrthuAMSSsstFYKO5N55Tva0bHCSs1esYepfM8rztvRS0z1Z9WCud5M68UOWDpKcNjptTHH-rbsck9XEvEQ5qM-HO-W73B32g79fK5HreUTO9JpTePARH-6jWcSoe8KVJyzoLH9HMZZ-QUuwiL4kupZ8YQdzNnpevMqGSymCzKHxeRo6RGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیانیه سپاه: ساعتی پیش آمریکا به دکل مخابراتی سیریک حمله کرده بود پاسخ دادیم
من اون موقع فقط از یک نفر دو پیام داشتم:
ساعت 4:00 چهار انفجار در شهرستان سیریک
پایگاه سپاه سرخور زدن
ساعت 4:26 دوباره یکی زد
هرمزگان شهرستان سیریک
و الان کسی تصویر دوم بالا رو فرستاد و نوشت:
"حدود ساعت چهار صبح، آمریکا با چند موشک به اینجا حمله کرد.
پایگاه  نیروی دریایی سپاه  شهرستان سیریک ، حوالی روستای گروک"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75834" target="_blank">📅 07:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=BRLAKWbVxl5N4WzgyOOoWpc1WuOLs_aWhqk_UEcRzwbdZe8YJYBp2z5Ji4MmvAedEwAokMW5X-uPfHawgOa3Xn21Y8uWBzxixBhdaTt2UdBnSDVJ69fbNlbgKa8wGrGfAcChvJVjZjCEAOqiElNtOZU_372rzmbQiUoTJR-a2GvLYec1iz2IdhcGmEqV2UUkMwGpvLc0KSyJZCv_DSl8oWtPWFuy3Vee9058Bka1kvuAWCHG77ZIznIiC-M64CH7_NdtVgBgr_s2OSfdSQHG35FYfvuyqhNDbgbRmwg7h0GOO2nR_u1BBayx6uFQhxbstd5Zgknmaa85bygTZbJs6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=BRLAKWbVxl5N4WzgyOOoWpc1WuOLs_aWhqk_UEcRzwbdZe8YJYBp2z5Ji4MmvAedEwAokMW5X-uPfHawgOa3Xn21Y8uWBzxixBhdaTt2UdBnSDVJ69fbNlbgKa8wGrGfAcChvJVjZjCEAOqiElNtOZU_372rzmbQiUoTJR-a2GvLYec1iz2IdhcGmEqV2UUkMwGpvLc0KSyJZCv_DSl8oWtPWFuy3Vee9058Bka1kvuAWCHG77ZIznIiC-M64CH7_NdtVgBgr_s2OSfdSQHG35FYfvuyqhNDbgbRmwg7h0GOO2nR_u1BBayx6uFQhxbstd5Zgknmaa85bygTZbJs6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
ویدیوی دریافتی دیگر از همان موشک،
دوشنبه ۱۱ خرداد ساعت ۶:۳۰
Vahid
ستاد کل
ارتش کویت
دقایقی پیش اعلام کرد سامانه‌های پدافند هوایی این کشور در حال مقابله با حملات موشکی و پهپادی دشمن هستند.
به گزارش خبرگزاری رویترز، جزییات بیشتری درباره این حمله پهپادی منتشر نشده است.
ارتش کویت در بیانیه خود تاکید کرد که صداهای احتمالی انفجار ناشی از رهگیری اهداف مهاجم از سوی سامانه‌های پدافندی است و از شهروندان خواست دستورالعمل‌های ایمنی را رعایت کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75833" target="_blank">📅 07:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g0BOIy25M533QW0k6462AZcUYl3G-oPOVCZCkpIUYQjW1m1ZD7WbY-EQoAHoZT9nj9cIu7UO0zHBTMcJf7kyWA4Tb_iU9aYtno8wQn_-kGYAsEPpimxogVLh-G8rsMitVgQC1owCw7YuwUxEZ6fR7zNBhMsYpAEJAtjqqCaoal_fr7w09vZAptD0JYzW6Ay8NytBn385L-QmU4lCvcYQc1KgwPP8ajuJDnbCdgNiqxMRKjKpN8c9FzstatfuvIkwkeKM3ymgPiesVJ7cal9je3Fg_SzMiw-6gRaLlJ-JFEMI-gIbN-CZ9nwCPCFanBo4C-0-LEV7mtRNQcT-y7RCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام درباره حملات شنبه و یکشنبه
(از جمله حمله ساعاتی پیش به سیریک هرمزگان که با توجه به
پستی پایین‌تر
گویا حدود ساعت ۴ صبح دوشنبه به وقت ایران انجام شده. در آمریکا هنوز یکشنبه است.)
ترجمه ماشین:
"آمریکا در واکنش به تجاوز ایران، از خود دفاع کرد و تهدیدها را از کار انداخت
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده آمریکا، سنتکام، این آخر هفته حملات دفاعی علیه سایت‌های راداری ایران و مراکز فرماندهی و کنترل پهپادها در گروک ایران و جزیره قشم انجام داد.
این حملات حساب‌شده و عامدانه، روزهای شنبه و یکشنبه و در پاسخ به اقدامات تهاجمی ایران انجام شد؛ اقداماتی که شامل سرنگونی یک پهپاد MQ-1 آمریکا بود که بر فراز آب‌های بین‌المللی فعالیت می‌کرد. جنگنده‌های آمریکایی به‌سرعت واکنش نشان دادند و پدافند هوایی ایران، یک ایستگاه کنترل زمینی، و دو پهپاد تهاجمی یک‌طرفه را که تهدیدی آشکار برای کشتی‌های در حال عبور از آب‌های منطقه‌ای محسوب می‌شدند، منهدم کردند.
هیچ‌یک از نیروهای نظامی آمریکا آسیب ندیدند. سنتکام در جریان آتش‌بس جاری، در واکنش به تجاوز بی‌دلیل ایران، به حفاظت از دارایی‌ها و منافع ایالات متحده ادامه خواهد داد."
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75832" target="_blank">📅 06:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GDkNG-I5gPxAM-slghzyxGAq2Q_ynFz3Y3naT4-_3bT8-vn8QoYhFa3aA0gzKvd4EF8RK8MSIr8rv9O72uVbvnkUUIpoZIIN2m9_RP5ltRkkYy8r4uMm1QaSbJrsLJKO-kVx8lMiz39UYMuLSccxa9HwQN8iOCZNLT4UGVV96IwpFGDmY0vEuVfn7hJgTcgfXPrlRP7q_r6sFlrIf91I6Mm6nR4ksPDdLjwaR69Ewb2ujZ17h1eA-lx184qo4Ph3wLRcCvdzlIepNiJ4UFqCjmoCzLzPOLE50CyJOc_QaxebbtcEMuD5h1jyztQbPKq5IRqC7oIzFYb1wkZ4MGVCIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/N44dOm8dnSstRnSQq0PTeB8PHdpI4LjNvWYn7H6HdwV53NHi5rGtIFLADPL7WrFxcAcEh24x2LktkwhWgPZY3nPQuMPmgLeP5im3PRBlZWKjUUgF-aNpG2w1He86DgdP5d3jN9ly8bCUPCtJlQ4mKeXURpTUTBJTR6BiB15AV0cv-n3WnSMCd1D-I17uGJchzL4cUay42jHDwvKbcN26KpVqxYQ0L7GxPowk0Wt9JsVT3QbtLlg8QisyTWq_jhekjL4xYzybriB_-V2k1D63WosfTkrM7gnSljSQv5i5yuDXr_ILX92CPHNadoutjVQp_o5ShaRsvaTuzrmL1t68Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jjnzc7UmtvCcpWYAPNgv-TznpRwJ26XURvjpJDafIXrICC5iUBEd8zxGlHHbydfosVUBtz10FFzMS7kgkNGpRmMpOR-TDKGEVGSQIbTUFBqX0_zb2n-CkxNxkOfDXFI6ZHq2XUW16ZUUZolWRZcfyXFsKmA8q6j0th-idHKhw_JsWUNGOdQH_4M8-ym2AXMndIvOrr2FkSOdK2skjqta9LSs5nIbhUfCyHY05ZX1PLjYEEPupoSnsd3aRYV70T47YEQqPOln-u5-GyA2DG8pNPXQzRBon1Vr6EJWiZIWBga4z2g4uMhnSfTpBfhaPmV6a_nfD27lov3fhp4AN5bPVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=n3ELHk3NrshCt_bTr-o-hgp5R4S173akkTIgqEkeREAUDrEDCBfHbztbKz4sRnsbzAmwUDgRQf7eT-XRUWd7AgPuq75Hc6Ojv-yvJew4M-aNMcjQKHnd-TyXrOPKwIP8QRvgJNOFvMUJpBK0cQyTcojg2E4TvVrUzRyGvqCkiSxSaZXsX5cBSAfqPgcMEhXmoqvbnktr3mODMHHg954Z829M9DOqBVuPj-OGwtF6kH51N5bEfAGZbi4MCxINMwOV_LXDcGn5p3evoQ1A05XZHGkycLGe-zW4dvuFpX3Rs83hBU5V_eNf1GULgOwg7DSa8GBljBtw3yaD1gLj-LB4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=n3ELHk3NrshCt_bTr-o-hgp5R4S173akkTIgqEkeREAUDrEDCBfHbztbKz4sRnsbzAmwUDgRQf7eT-XRUWd7AgPuq75Hc6Ojv-yvJew4M-aNMcjQKHnd-TyXrOPKwIP8QRvgJNOFvMUJpBK0cQyTcojg2E4TvVrUzRyGvqCkiSxSaZXsX5cBSAfqPgcMEhXmoqvbnktr3mODMHHg954Z829M9DOqBVuPj-OGwtF6kH51N5bEfAGZbi4MCxINMwOV_LXDcGn5p3evoQ1A05XZHGkycLGe-zW4dvuFpX3Rs83hBU5V_eNf1GULgOwg7DSa8GBljBtw3yaD1gLj-LB4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
تصاویر دریافتی، دوشنبه ۱۱ خرداد ساعت ۶:۳۰ به وقت
#ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 288K · <a href="https://t.me/VahidOnline/75828" target="_blank">📅 06:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lbZEJcGKucOI5CawfXCs0dqmlE9EDuj96AE54lJXDE97YeZGJkq8h0qiPaKQslhNsL75TW0-FeElXD19PSMLwpWUAZ2BWuBIMC9XI7ENwZdgtlXNsQt9VqngOprihGnbBmcMSJD3wiEt25ufyHwLJL_dwoM0al_GoUsH5_t6l1clz2MCxFM4n7GBNWhWfqzgrd8EFIkq9gcdJOYQSAIh6Cs3GlcbNzrK7AVYToSNqeIpWlznpBklvV17UgaaUNcKQUQtUCy0UfoiF1HlMZCQR-wU1B0VnMOQ70kqSXgKP0RxHwlgd3fgYmX2Hpm1ZFvp11GLB45DGGafBmF2Gg2_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به کویت
دوباره همز‌مان پیام‌هایی درباره شلیک موشک از امیدیه خوزستان و اعلام هشدار در کویت دریافت کردم.
دوشنبه ۱۱ خرداد
ساعت ۶ به وقت کویت که میشه ساعت ۶:۳۰ به وقت ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 333K · <a href="https://t.me/VahidOnline/75827" target="_blank">📅 06:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZCaBzV6IPqHNDNEokub29PESA1hdvYaVsg9271I767y_ij7-YxS7av5Y9UB0m5fF6KKDug6Ydv5hfg54jAbzlEW7bW5rl8WKsrVviPltzjGjFEzM_prnrZalqVBURyB4vo93JUe-y1xDwtwEjIt7jfB3idej2Vu_GwxmFJ6hyjplhWOfGIsL4ELnOoBXJf8I6Jj3zn9_4lcSpfgxUPwp6JRyY9IBXGVCOaGCeKx6dE2Ci558uYKBkCjv4xFUV51eyy97B4RDYIJ2u0xfLuHc9ymTgI8wsBP6HQK0p2NnrpU2vgAKsDzWA6t07UWeScTxYrI-tP-GGB27nRZJrLJyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
رسانه اخبار جعلی سی‌ان‌ان امروز طبق معمول گفت که توافق هسته‌ای ایرانِ من درباره مسائل هسته‌ای صحبت نمی‌کند؛ در حالی که در واقع، بسیار روشن تصریح می‌کند که ایران سلاح هسته‌ای نخواهد داشت.
سپس با جزئیات بسیار محکم و مفصل، به جنبه‌های مختلف دیگر موضوع هسته‌ای می‌پردازد.
در واقع، بیشترِ این توافق درباره همین موضوع است.
سی‌ان‌ان و بسیاری دیگر در رسانه‌های اخبار جعلی، فاجعه‌ای با رتبه‌های پایین هستند.
حتی با مالکیت جدید هم بعید است اوضاعشان هرگز بهتر شود!!!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75826" target="_blank">📅 03:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZrbXjL2AeRGnrbAQZ5Fcupko24rIry7rQm_NkzxtbXaI1gWxz0Ww1I8ux5MkAsDV_78pgpzF-CjgR-zQCfiPHvG9S252rZ7JFgRPrEM_PCha0Iqiup-bPxGeWaXS0lex8uC7PeqHaRG8YvCB7eHqKN5hPakepuK5edsCzOARlmQY0bnHHhGflTXuL_hYGkkEuhk2lKVAsD-jIOPk8S8M1Lkp08wKClxiYUxJnfyD2X3ySlP_CVMpIyo9gpAK1ojX7mvcG_ruFKYMSHuqvudU6ErnJZbuPZrnOeBm3kTcOVJ8cre7o5D44sh-xavP1zqccCy9jZ1c2T7FAw0nXyCsCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز هم به درخواست استعفای پزشکیان پرداخته:
FoxNews
چند مقام دولتی با تکذیب شایعه استعفای مسعود پزشکیان، آن را «خبر کذب با هدف ایجاد ناامیدی» خواندند.
فاطمه مهاجرانی، سخنگوی دولت، الیاس حضرتی و علی احمدنیا که از اعضای شورای اطلاع رسانی دولت مسعود پزشکیان هستند در پست‌های جداگانه به ادامه کار رئیس جمهوری و تلاش او برای «حل مسائل کشور» اشاره کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/75825" target="_blank">📅 00:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P4wU7XeJ_Ewt1veVJw6OKTNJsGoDfKTTNM7GPATSn-9bvrA07waNErdXr8sjsEyZ89n4xC7zLPFEkXexBjv9jxPmFlZDEd4RNsfllxFhqVUQu_KcMTk2l9HrtMUsBF-4X_cbTjEn2C8aW7BdqjX1Uc79Y1dnCGgTPcRtgk1V3sl2mueG559E_kU9h1UiMOTHtj-WRK77ALhtTy-rveMj73XpH14QSoUb_awI8C-cP1Ok5sZz99-H6yE297IpZclqDQzCfonKhxxdEAItACKUtFxSFKj2o2NePydl5eX8VSgOjx4sLAbHNt_FBu8xDmT8Dn-yB_U8RA3kYemXLJg1jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی وقوع دو انفجار را که تقریبا هم‌زمان در تهران و کرمانشاه و در ساعات پایانی یکشنبه گزارش شد به نشت گاز نسبت دادند.
سایت تسنیم، نزدیک به سپاه پاسداران اعلام کرد که در ساعات پایانی روز یکشنبه، «انفجار گاز» در محله باغ ابریشم کرمانشاه باعث مصدومیت ۲ نفر شد.
این سایت‌ همچنین [با انتشار عکس بالا] مدعی شد که انفجار در یک واحد مسکونی در «فاز یک اندیشه» در استان تهران ناشی از «نشت گاز» بوده است.
خبرگزاری ایسنا به نقل از سخنگوی اورژانس استان تهران می‌گوید این انفجار تاکنون ۶ مصدوم بر جای گذاشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 405K · <a href="https://t.me/VahidOnline/75824" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=fCd1XHdKOJR4fjTCCK4U00mkkxhnxyd7mvRraFZ1PHVyA2LxqFcaohIAKxKnZA61vDwM5jbUTK4cKAj0QYvABhBtKPOGs_fnfdvFBkVqx736vG78mO4OMuhrlwDiYHDAbwLj9hPx0Pe0yrEbaHI9bH50agDP3FZqlAEMkTBaAYDak9MeF5YbOcGVWB9UNAYT3Aju1-66sRAzJnqd0XEA96G336QJJaMI9Q-VX8Rbe_WuuNYR-JCWcHqXPrWh8CcMjeBbL19-9Dpxe0pCRT3mr272ZvZqzYjejrCX0UO5oyRMaxRHCJRvGjxWPQveO6EEaAMUvAJkBs0v-efm-CqEjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=fCd1XHdKOJR4fjTCCK4U00mkkxhnxyd7mvRraFZ1PHVyA2LxqFcaohIAKxKnZA61vDwM5jbUTK4cKAj0QYvABhBtKPOGs_fnfdvFBkVqx736vG78mO4OMuhrlwDiYHDAbwLj9hPx0Pe0yrEbaHI9bH50agDP3FZqlAEMkTBaAYDak9MeF5YbOcGVWB9UNAYT3Aju1-66sRAzJnqd0XEA96G336QJJaMI9Q-VX8Rbe_WuuNYR-JCWcHqXPrWh8CcMjeBbL19-9Dpxe0pCRT3mr272ZvZqzYjejrCX0UO5oyRMaxRHCJRvGjxWPQveO6EEaAMUvAJkBs0v-efm-CqEjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی، در واکنش به گزارش شبکه ایران اینترنشنال درباره استعفای مسعود پزشکیان، رییس دولت، این خبر را تکذیب کرد و آن را «شایعه‌سازی» خواند.
شبکه ایران اینترنشنال، ساعاتی پیش در گزارشی اعلام کرد مسعود پزشکیان در نامه‌ای رسمی به دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خواستار کناره‌گیری از سمت خود شده است. این رسانه همچنین نوشت در این نامه به وجود اختلافات ساختاری در اداره کشور و نقش نهادهای نظامی در تصمیم‌گیری‌های کلان اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 424K · <a href="https://t.me/VahidOnline/75823" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qgiqYCO1As4uPlwQ5jOuVgCB_TkZQin22eH7JVzdf1xO4AU6BUTZqumhq9KtnB0D0dOe4qoFR0n-8UUJgy8jj3xWPU-sJvhyN2SU6zs3t-5nch5kiW4eIJehxJSVYM3Nvwy7rD4TgFp-Yk5IN1HdfY_xw0xZdUVFDNTXjCwDPiun-YI9VdAEPzq9unHduYdG5sF64MbdIDaGQDW5HnKy_THPrzl2MZcdOV_j0E3fCgO-qedLGBDDMVSHiwRlwPLc19cGd3KWs-fBtYXdhR5ah_PezPACWPUr0tqLSStM8cIUQ9MSXxEW_whDUStWDlt4Y2239oB4Xg7fBFawkbm7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 425K · <a href="https://t.me/VahidOnline/75822" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzybdXsP4QYSvxKNZ2Dqqh3m0TqWVhY9FTnJblQG5uJHqt-2vcRTYxnaO7vhzbgpNz-o_UAQ1IuS33YYzhC39dVwqB3AgOEOJ3oTXgjx-oPWdY2uliBs_4YTHyva3iWJ7XmyoYjY1bQn_2AsX7uTFgfhU9Sk-YQmaqCtwepbz9j3beMNMEut4v78-7vlenVLgfVTFFQKcy_NcNbpLjmBejUEhUjo-cH4C7g8cRabGejNNwophCF1oH1bU_vGJZbjOuoqmx21HsP9_Ce2QQiiREgBW7hS5OlIvUhK9HKkL1pdrS6QUh2HsiB0mlV9SgRhWeJoTprpngJ6KEoTYxcd0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پیاهو، مردی که تصویر معترض نشسته مقابل نیروهای پلیس یگان ویژه در مقابل پاساژ علاالدین در آغاز اعتراضات دی ماه سال گذشته را منتشر کرد،
به گفته وکیلش
به ۱۰ سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 419K · <a href="https://t.me/VahidOnline/75821" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6220710705.mp4?token=mHTDAZ-FKQGQmz664IvsTffwOQ_hvEnHpv9IBXzmfqd57ndyYCtRqZLQXKAvT0SiEKdqUZs_x1aAN4-7CQq3omjhGO4mMohhCL6IK-rvF-wu8xdIIyj2zpjZ2XTC_E8B13ydityTnQMcLsGLhdeo4dt4nZ5qm9bUXQkVehANvfpx34gZGed1WOIoZ_ZdwAPmbUK3je0XyRhRxGO7OxJJJ3BjoID1QpWLIYrm0x0ue0uFQ9qnTg-_iodnwqpZuyxCetepqDI6Dok1k0k9-WnJ2bcnfJoB5HphkM4sOiHAlLFu9Bdpfwpmtxx2ymugR2Dui998GtNBRBQ9OZASEftniA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6220710705.mp4?token=mHTDAZ-FKQGQmz664IvsTffwOQ_hvEnHpv9IBXzmfqd57ndyYCtRqZLQXKAvT0SiEKdqUZs_x1aAN4-7CQq3omjhGO4mMohhCL6IK-rvF-wu8xdIIyj2zpjZ2XTC_E8B13ydityTnQMcLsGLhdeo4dt4nZ5qm9bUXQkVehANvfpx34gZGed1WOIoZ_ZdwAPmbUK3je0XyRhRxGO7OxJJJ3BjoID1QpWLIYrm0x0ue0uFQ9qnTg-_iodnwqpZuyxCetepqDI6Dok1k0k9-WnJ2bcnfJoB5HphkM4sOiHAlLFu9Bdpfwpmtxx2ymugR2Dui998GtNBRBQ9OZASEftniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با فاکس‌نیوز درباره ایران اعلام کرد: لایه اول و دوم حکومت آن‌ها از بین رفته و اکنون با لایه سوم روبه‌رو هستیم. شاید آن‌ها دیده‌اند برای بقیه چه اتفاقی افتاد و می‌بینند ترامپ آماده انجام چه اقداماتی است.
بسنت افزود: اگر ترامپ با این توافق موافقت کند، همین حالا به رهبران جمهوری اسلامی می‌گویم که او این توافق را هم از نظر نظامی و هم از نظر اقتصادی اجرا خواهد کرد. آزادی کشتیرانی در خلیج فارس از طریق تنگه هرمز باید به وضعیت پیشین بازگردد.
او درباره اینکه آیا ترامپ «کار را تمام خواهد کرد» گفت: اگر «تمام کردن کار» یعنی اطمینان از باز بودن تنگه هرمز، در اختیار گرفتن اورانیوم با غنای بالا و نداشتن سلاح هسته‌ای از سوی جمهوری اسلامی، پس کار تمام شده است.
بسنت تاکید کرد: چه از طریق مداخله نظامی، چه محاصره یا فشار اقتصادی، این نخستین بار در ۴۷ سال گذشته است که ایرانی‌ها درباره نداشتن سلاح هسته‌ای گفت‌وگو می‌کنند. این موضوع پیش‌تر ممنوعه بود و اکنون برای نخستین بار روی میز مذاکره قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75820" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75819">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهمند عليپور Farahmand Alipour</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=Hl-8RTwBuI-89cUSmgmpl-jgTjofv-sQUBQ_JTIPOI0Gjbc3LufzBsc6nkQc-tQl7YXZp1QtP5omWNe7FhxujwhvngYARE9UJIg-rKxTUU8J_wetMm3gmtg_KE-jqbmEXxJ-n_KEwWEuacrK8r8zhRvFzijC-ElY3bERDU2X4kVVQqSYPZglHXaXqbI1zQdfqQTlvYKwzc2w3-b-q6pMyDvs4gxBbpAjFkQ_u8ij4Xc8rqjZ1rDEPFMDKSrN5AjI7ZjhPesDJ6L-D7tgqoTe0VxmktwwdOMw6SHQQ1U3fcF3k0HEOQzhUvpSKPE0n2RkbOlR_zAfg78u2yZJloavLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=Hl-8RTwBuI-89cUSmgmpl-jgTjofv-sQUBQ_JTIPOI0Gjbc3LufzBsc6nkQc-tQl7YXZp1QtP5omWNe7FhxujwhvngYARE9UJIg-rKxTUU8J_wetMm3gmtg_KE-jqbmEXxJ-n_KEwWEuacrK8r8zhRvFzijC-ElY3bERDU2X4kVVQqSYPZglHXaXqbI1zQdfqQTlvYKwzc2w3-b-q6pMyDvs4gxBbpAjFkQ_u8ij4Xc8rqjZ1rDEPFMDKSrN5AjI7ZjhPesDJ6L-D7tgqoTe0VxmktwwdOMw6SHQQ1U3fcF3k0HEOQzhUvpSKPE0n2RkbOlR_zAfg78u2yZJloavLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در تاریخ ۲۹ آبان ۱۴۰۴
در تلویزیون جمهوری اسلامی میگه ترامپ به ما نامه‌ای داده و صراحتا نوشته
«دو گزینه بیشتر نیست»
یا جنگ و خونریزی یا مذاکره مستقیم
«برای از بین بردن غنی‌سازی و موشکی»
این مصاحبه چند ماه بعد از جنگ ۱۲ روزه بود! یعنی در آبان ماه، مشکلات آمریکا و جمهوری اسلامی همچنان همون چیزهایی بودند که باعث یک جنگ شد، و این مصاحبه یک ماه پیش از آن بود که دست به قتل‌عام مردم در خیابان‌ها بزنید!
الان هم محور مذاکرات کاملا مشخصه!
همون چیزهایی است که جنگ ۱۲ روزه رو رقم زد. همون چیزهایی است که در آبان ماه عراقچی در تلویزیون گفت.
خون تک‌تک ایرانیان از جمله کودکان میناب پای شماست! شما طرف مذاکره بودید، شما انتخاب کننده و تصمیم گیر بودید.
و شما بین اورانیوم و موشک، و یا جان مردم، زیرساخت‌های کشور، فولاد و پتروشیمی و…
اورانیوم و موشک و دشمنی با اسرائیل و آمریکا رو انتخاب کردید! هنوز هم طرف مذاکره و تصمیم‌گیر شما هستید! و‌ جنگ ‌از سر گرفته بشه باز تصمیم و انتخاب شماست و مقصر شما هستید!
نمی‌توانید پشت کودکان میناب قایم بشید و از کشتار دیماه فرار کنید!
هر خون و ‌هر ویرانی ، همه پای شماست.</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75819" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fXkQ_s49S-XK6F8VnEMCStqcNItgxjCXxva_u8tEevmzug3GE0tGDOg-UgyTx2R4tZ9nj1mzBt63hKkDfqHQ62yV2_W_r5SdVOe2_3u29kseALyhuPAwW9FALcTgQCVKrx9mY9xSm2If7-xUW8UJUi-gu3JZnLPz0C1FCfpQMHPp_pwPk2X37ARNk3Jioe7FCSoZvuYPVKFU2xv0RYFtUdGPztFsjeC0tv6d_JPhvne1_ZaYNrqvnyPndxTgHsysrCsF6TPYV9slIKBrcqJPjMBxEnuwzZnDibhoFDSIHb_eK3AaKtwbiU6io-5QMLbIUtlCK0jDtpDXaucxuSmroQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن و حسین امیری، دو برادر دوقلوی ۲۰ ساله محبوس در زندان قزلحصار کرج، از سوی شعبه ۲۶ دادگاه انقلاب تهران به ریاست قاضی ایمان افشاری به اعدام محکوم شدند.
بر اساس اطلاعات دریافتی هرانا، مبنای صدور این رای اتهام «جاسوسی برای اسراییل» عنوان شده است.
یک منبع مطلع در گفت‌وگو با هرانا اعلام کرد در کیفرخواست صادرشده علیه حسن و حسین امیری، مشاهده تصاویری از ساختمان‌های آسیب‌دیده به عنوان مستند اتهام «جاسوسی به نفع اسراییل» مورد استناد قرار گرفته است.
این منبع همچنین گفت: «حسن و حسین امیری به دستور بازپرس پرونده به صورت جداگانه در زندان قزلحصار نگهداری می‌شوند و از حق ملاقات با یکدیگر محروم هستند. این دو زندانی در حال حاضر در سوییت ۳۵ این زندان محبوس هستند.»
بر اساس این گزارش، این دو برادر پیشتر در یکی از ایست‌های بازرسی و پس از بررسی تلفن همراهشان بازداشت شدند.آن‌ها پس از بازداشت، به مدت دو ماه در وضعیت بلاتکلیف در زندان قزلحصار کرج نگهداری شدند.
👈
حسن و حسین امیری از دو سالگی در مراکز بهزیستی پرورش یافته‌اند و خانواده‌ای برای پیگیری وضعیت قضایی و حقوقی خود ندارند. به گفته آشنایان این دو جوان، نبود حامی خانوادگی بر نگرانی‌ها درباره روند رسیدگی به پرونده آنان افزوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/75818" target="_blank">📅 18:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OZL597fVsAut1pQdHyacr0LNA4z3e-zw5QwHufSwha3_D5DgSP78_azh0QIZx8yzKK7G8TgTLR8ndVWNwuJIUMRWArPdIuSSB7_EAbQdL3fbyMjsY3B1VKjeaPpBB7X0muOqIayNO9lGEMFFN2A2pNxNUwmCHq7s32qpZwv5YUGlSrE-N93vcGuYLdampee9Hn3j6CSplIt4WNT9TI91DfqeCumuSiWmR3Dw5o4xVoTpm_J0CVxD0SEFO60hh5RjIVu_cTultp8mR6HNhRhquZMwyRN4Qd69eZHs7YM1lqJ5XiIy742dGea6bPcU80Btav44kw0Tx-QnHB-VLsr8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: ایران چندین ورودی تأسیسات موشکی زیرزمینی خود را بازگشایی کرده است
شبکه خبری سی‌ان‌ان روز یکشنبه ۱۰ خرداد با استناد به تصاویر ماهواره‌ای اعلام کرد ایران توانسته از زمان توقف جنگ شماری از زرادخانه‌های موشکی مدفون خود بر اثر حملات هوایی آمریکا و اسرائیل را از زیر خاک بیرون بیاورد.
حملات آمریکا و اسرائیل با تخریب جاده‌ها و مسدود کردن ورودی تونل‌ها، دسترسی ایران به پایگاه‌های موشکی زیرزمینی را محدود کرده بود.
سی‌ان‌ان ادعا کرده است که ایران تاکنون ۵۰ مورد از ۶۹ ورودی تونلی را که در ۱۸ تأسیسات موشکی زیرزمینی توسط آمریکا و اسرائیل هدف قرار گرفته بودند، بازگشایی کرده است، از جمله در پایگاه‌هایی در خارج از اصفهان و در اطراف خمین.
بر اساس گزارش این شبکه خبری، ایران همچنین بخش‌های دیگری از این پایگاه‌ها را نیز ترمیم کرده است؛ از جمله جاده‌هایی که آمریکا و اسرائیل برای جلوگیری از تردد پرتابگرهای موشکی بمباران کرده بودند. تصاویر ماهواره‌ای نشان می‌دهند که تقریباً تمامی گودال‌های ناشی از بمباران اکنون پر شده‌اند و در دو پایگاه، این جاده‌ها حتی دوباره آسفالت شده‌اند.
ایران شبکه پایگاه‌های زیرزمینی خود را در عمق خاک و در مواردی زیر کوه‌ها ساخته است تا در برابر حملات هوایی مصون باشند، به همین دلیل آمریکا و اسرائیل بسیاری از ورودی‌های این تأسیسات را بمباران کردند؛ اقدامی که در کنار تلاش برای شناسایی و نابود کردن پرتابگرهای موشکی، باعث شد توان ایران برای شلیک موشک به‌طور قابل توجهی محدود شود.
این حملات خسارت سنگینی به پایگاه‌ها وارد کرد؛ به‌گونه‌ای که بیشتر ورودی‌های تونل‌ها زیر حجم عظیمی از آوار مدفون شدند و جاده‌های منتهی به این سایت‌ها نیز به‌شدت تخریب شدند.
سی‌ان‌ان می‌گوید باز کردن ورودی تأسیسات موشکی زیرزمینی می‌تواند به ایران این قابلیت را دهد که در صورت وقوع دور جدیدی از درگیری‌ها، موشک‌های بالستیک بیشتری نسبت به اواخر جنگ ۴۰ روزه به سمت اسرائیل و کشورهای دیگر شلیک کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75817" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75816">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSQrrrD4P7s50ahsISHAo5hnehyt5WlK_VxyYGUjwt6U-gtF60x24njRKkeq0tWfmKqx9Zl9T49UGrkrs3EmJtLJqJBVIV1N1_Xo7AB7StRZR5PNyqUbC8ijk6u2SUy2X7Ec_7JXEYZ3ispikfE1hMwDiOFVqlPPKa8aDXIq8yzRGxPP9vOUb6f6gR3Gu0Fsh54uRr0tVAG0GQgRma3p331AXENbq2CpO1t_wZL4EzEAONylI4AG0bRiJTlDObWtzQuo01i1Miz5pJSre-IcoA-_Djo3108AZJYGZj0y0UQq_Ppi4S2b4BoV3CW6BmxoxkHX08NmoMi-3SBYXmPxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس مصوبه جدید شورای شهر تهران، هزینه خدمات مرتبط با خاکسپاری در بهشت‌زهرا به‌طور میانگین حدود ۴۰ درصد افزایش یافته و در برخی موارد رشد تعرفه‌ها به ۵۰ درصد رسیده است.
روزنامه دنیای اقتصاد گزارش داد نرخ خدماتی از جمله حمل متوفی، تغسیل، تکفین، تدفین و برگزاری مراسم افزایش یافته است. بر اساس این مصوبه، هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری ۵۰ درصد افزایش داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75816" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75815">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CllkICPCMnd6-pzUvNGZ7T2CHO7vMCGFZnoDZ6Q2XwunPk9rozK9ne6gde-HshJIqWQdWh9Vk-Rb1HPJHKw-hbYQTnn2UuoEHxwtI5k6a2DWP0CUPhhauJtz-HwyGXtqcOfAIwia21lU9TDYO_rly8eOuhpG0E6aLJrE8vtEJaNwjUxFWhrQpjPjYAovCCfITOvGb2MYaHeg6QSW72ZJ8d5UmTax9MnZceSQIqxsKL8AGNyADXh1OINGy0i_AR7Fzfjinoz7d7xnlXX63mpf0p4cv8qmH0_gEviyhTM4wcvhGehS67E-p6YWe1hYdW5IDZYDaXvtPJD-0SYVOLiF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت هرانا گزارش داد زهرا شهباز طبری، زندانی سیاسی محبوس در زندان لاکان رشت، پس از نقض حکم پیشین در دیوان عالی کشور، بار دیگر از سوی شعبه دوم دادگاه انقلاب رشت به ریاست محمدعلی درویش‌گفتار، به اتهام «بغی از طریق عضویت و فعالیت در سازمان مجاهدین خلق» به اعدام محکوم شد.
این زندانی سیاسی ۶۸ ساله، در فروردین ۱۴۰۴ در منزل شخصی خود در رشت بازداشت شده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/75815" target="_blank">📅 15:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75814">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQxztNZfZHln8qy0XWaTUOTvx5tXZ7H9tHWqxJHFFmybyZqg7iALCWZLhOpI0i0j3yT7fc8VNScMAdWAe4q_sPpHs2eZVeSFKJLNC-nLIMvcd5mY3IvItvxBgOfja-RCxHXcTayE_qC70M8AoCNTafmEpOleVimb_LFdb27DTmI_qMaHLau3zyPpv5OiYklOXIlFbXpsoRfpIHnCqiBAEZm9WVGs1U-rGnV9_cqFn0JUqHIuhGVnmxErYoan86bQPmmurQzVepo8nfLWxmTvr0-93KR2cCXG8-j0Guef17xam2TyhWcPYXO49S4rnSbIOkbvJhpeuuWoDW1OB5lX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران روز یک‌شنبه اعلام کرد‌ «طی شبانه‌روز گذشته ۲۸ فروند کشتی اعم از نفتکش، کانتینربَر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگه هرمز عبور کردند.»
ساعتی پیشتر روزنامه اسرائیلی «اسرائیل هیوم» نوشته بود که ده‌ها نفتکش حامل نفت و گاز طبیعی مایع در هفتهٔ گذشته با اجازه آمریکا و پرداخت عوارض به ایران از تنگهٔ هرمز عبور کرده‌اند.
این در حالی است که دولت آمریکا بارها اعلام کرده است با پرداخت عوارض به ایران برای عبور از تنگه هرمز مخالف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 300K · <a href="https://t.me/VahidOnline/75814" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75812">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hh5ZZmYeaOk6YryBUgqxuIyC_TDJX3KhVowvx7r_r8P3kjQ5u72TGffHtSwsWg3pErnDRPEVZCrjAXXQELQ__mbSQ_I0fmO5t3xBRvlERr-y5IcXHEzfbx7HxaNnJP7oaWQGIFGb71iPpu7EXQt4k3UbS9FivbRWG1nvJEM9oSYYAN8lWK-qigNX8hoXMdHBfG5ghQUeJlY-pOQuXmovxBROdQIlKczqC8ANiIqdBXx9-IYEt8Lvf9kR7KnV4kdVvDAoiRhEZXeEOVWMVtc72og-uLtHMkRFzcxkGGaitCA7i-Ot6l3CEhrbP2aCzQu16ViqJeFxbcrJoi1ssjYf0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=n-kCBxYUQ3BFyaVgKEKiZl0-p5bnktgfwP5L0yn-TBKhktIQWJkS5tQYLttDbVogTzUwiki4f4pg4g6p_T0F8CIisbLF3dh163mfEQAAsRgUM5YFexWnE1IyayIZXXStkBlq-x9iHXAxZYxVXhHA-281hvQeBI8gMgvD60k9pQNRKBVbij3am3tR2MMiCbXaf4S_QkSNsa7fNVM-mcvkxS2y8wR23SlYatD9-i0f15XQi4pZrj8iPMoGNWdD79jc107MwmwEKCVMcsviTa0Lup4ll9Dn-QHZ0sJDRIQoxRBeFGO1TIV_4-tK3XfccSZsfRbkJGkUF7bWdQMaBKOMtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c9b60ac63f.mp4?token=n-kCBxYUQ3BFyaVgKEKiZl0-p5bnktgfwP5L0yn-TBKhktIQWJkS5tQYLttDbVogTzUwiki4f4pg4g6p_T0F8CIisbLF3dh163mfEQAAsRgUM5YFexWnE1IyayIZXXStkBlq-x9iHXAxZYxVXhHA-281hvQeBI8gMgvD60k9pQNRKBVbij3am3tR2MMiCbXaf4S_QkSNsa7fNVM-mcvkxS2y8wR23SlYatD9-i0f15XQi4pZrj8iPMoGNWdD79jc107MwmwEKCVMcsviTa0Lup4ll9Dn-QHZ0sJDRIQoxRBeFGO1TIV_4-tK3XfccSZsfRbkJGkUF7bWdQMaBKOMtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جلسه مجازی صحن مجلس شورای اسلامی به ریاست محمدباقر قالیباف و مشارکت آنلاین ۱۸۷ نماینده و حضور ۱۴ نماینده برگزار شد.
در این جلسه که اولین جلسه از سومین سال مجلس دوازدهم بود، اعضای جدید هیئت رئیسه مجلس سوگند یاد کردند.
جلسه روز یک‌شنبه، دهم خردادماه، همچون جلسات معدود گذشته در مکانی مخفی برگزار شد.
محمدباقر قالیباف در همین جلسه تأکید کرد که «تا اطمینان پیدا نکنیم که حقوق ملت ایران را گرفته‌ایم، هیچ توافقی تأیید نمی‌شود».
قالیباف که از او به عنوان رئیس هیئت مذاکره‌کننده ایران نیز یاد می‌شود در این جلسه بیانیه‌ای را قرائت کرد و در آن ادعا کرد که «در حال عقب نشاندن دشمن در یک جنگ تاریخ‌ساز هستیم».
@
VahidHeadline
محمدباقر قالیباف، رییس مجلس شورای اسلامی گفت: «سومین سال مجلس دوازدهم را در حالی آغاز می‌کنیم که یاد و خاطره رهبر شهید با ماست و هنوز فقدان رهبر و پدر امت را باور نمی‌کنیم.»
او ادامه داد: «رهبرمان به ما آموخت مقابل زورگویی و تهدید، ذره‌ای سر خم نکنیم و با مشت‌های گره کرده مقابل خصم تا آخرین قطره خون مبارزه کنیم.»
قالیباف اضافه کرد: «دیدن جای خالی رهبری برایمان جانکاه است، ولی دلگرم به مدیریت و رهبری جدید هستیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75812" target="_blank">📅 15:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75810">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gkID-WuOJSZlsrBL1fPKeJOQBVapONOYRbYXX0Vwwv4RURUc6vJbCVffk1Sk87ZFY-oJgYLlL6OwZCWOP28eJ6glpnrNm1jPofS94OEvcsdHjPLXpOIX2CuAP6Q0WG0-bnQccglnHGiKSuTwIrdbIlQlUAbe6AZhW4J41mrGmfSf5k_0RpLUY-2AmrZ-FtmFBBWF7glMBRSE8WnIXiZhCAfOVU1Mnuav2nsd2I0LCx0e7E9Uva2yVZooBQItSNzNOPLEIz_6GAUqoo6yk4-K_TDNzl0zAO8pZIFo4M89AlfCOEW67sr5tSzA48-jmS0N-DeDFLZnACeEEwDDXm5aqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=EYsljB7UJgpg4ZdfQN6CwrxvJdi8PMETw0sR7szKahb698rZu6xChnPBKjvP7f6_WMJV8l1M6oZjIamwfUSSPaWhMz3BtO-FKTPak2moD9pHmI-gOCxJwqdi8msmnop7p7jsP-r-ZXPfa_K07uJAouyoirs_O3XuHV4VKdQVDZGSzdq0nJFnxMDgbC2inGN0fkA9K_mEkHjeHKVad_fLSvmeDJJFa5anqQNLBLVk0_xldzUx4UX-Zep8HwY6pTfPUlTDybMiE16kavirgO1u7C_vA6y0NLvGJMju61vAsGkmOooJ_wpgQGrW8oP3wY7AnDwztABEZbBFdzFmmV3KKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8e2c9e72d6.mp4?token=EYsljB7UJgpg4ZdfQN6CwrxvJdi8PMETw0sR7szKahb698rZu6xChnPBKjvP7f6_WMJV8l1M6oZjIamwfUSSPaWhMz3BtO-FKTPak2moD9pHmI-gOCxJwqdi8msmnop7p7jsP-r-ZXPfa_K07uJAouyoirs_O3XuHV4VKdQVDZGSzdq0nJFnxMDgbC2inGN0fkA9K_mEkHjeHKVad_fLSvmeDJJFa5anqQNLBLVk0_xldzUx4UX-Zep8HwY6pTfPUlTDybMiE16kavirgO1u7C_vA6y0NLvGJMju61vAsGkmOooJ_wpgQGrW8oP3wY7AnDwztABEZbBFdzFmmV3KKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی انتظامی تهران کافه‌ای در خیابان ولیعصر را که در آن برنامه‌های موسیقی اجرا می‌شد، به بهانه آن چه «فعالیت‌های مروج فرقه‌های انحرافی» خواند، پلمب کرد.
مرکز اطلاع‌رسانی پلیس جمهوری اسلامی در اطلاعیه‌ای نوشت: «این کافه با برگزاری برنامه‌هایی با ظاهر موسیقی غربی، بستری برای حرکات نابهنجار، و آنچه که ماموران توصیف کرده‌اند "تحرکات شیطانی" فراهم آورده بود.»
نیروی انتظامی جمهوری اسلامی نام این کافه را ذکر نکرد اما ادعا کرد که «مشتریان این کافه، شامل دختران و پسران جوان، در وضعیتی غیرطبیعی و با حرکاتی عجیب و غریب، که از آن به عنوان “شیطانی” یاد شده، مشاهده گردیدند.»
پیشتر نیز بسیاری از کافه‌ها و اماکن کسب و کار به اتهام‌های مشابه پلمب شده‌ بودند اما جمهوری اسلامی سرکوب‌ شهروندان را از زمان اعتراضات دی‌ماه گذشته تاکنون شدت بیشتری داده است.
موج تازه اعدام‌ها، صدور احکام سنگین و بازداشت‌ها نگرانی فعالان و نهادهای حقوق بشری را برانگیخته است.
@
VahidHeadline
ویدیوی بالا رو هم به عنوان "تحرکات شیطانی" در اون کافه منتشر کردند!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75810" target="_blank">📅 15:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75809">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ghAr74LGkbZ8ZtEz5-SY4EX8UiArgoE58P4BG0gnlO0n5BbdT-rA16nvuEh_tjmKPTZEqT6kCiduXaf31tRVXLtMz5ATfpCWjdUZtKbGJppY8VNQtV8d8hDFxIkoUZhjWbMKfw2ALvTx3MoB5u1eEq_2mhahoI7FBOOxnur0l4L2DlptaTeomMVs5_br8rGwCjD4JVTLK_VhqxcZ76bdN8u90qH8Sm4Bl3WEbjdo0zM2s_TyAwz96d_NvZDP4Er_tgSXw5So1QPKMIwi5ACxvzkwhahz_agqq4q59Hf8bB71TWtL6NuEtbmACM6B3ns8fxwmIrNuz-aZ3ZoHHFIvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس، ترجمه ماشین:
رئیس‌جمهور ترامپ در جلسه‌ای که روز جمعه در اتاق وضعیت برگزار شد، خواستار چند اصلاح در توافقی شد که فرستادگانش با همتایان ایرانی خود به آن رسیده بودند؛ این را یک مقام ارشد دولت و منبع دومی که در جریان موضوع قرار گرفته بود، گفته‌اند.
...
مقام‌های ایرانی به رسانه‌های دولتی گفتند که آن‌ها نیز متن نهایی را تأیید نکرده‌اند؛ هرچند دو مقام آمریکایی پیش‌تر در طول هفته مدعی شده بودند که تهران آماده امضاست و همه چیز به تصمیم ترامپ بستگی دارد.
به گفته این دو منبع، ترامپ از تیم خود خواست تغییراتی در پیش‌نویس مربوط به بندهای برنامه هسته‌ای ایران ایجاد کنند.
در شکل فعلی، این تفاهم‌نامه شامل تعهد ایران به دنبال نکردن سلاح هسته‌ای است، اما امتیاز مشخص دیگری فراتر از آن در آن نیامده است.
در این متن آمده است که یک بازه ۶۰ روزه برای مذاکره درباره تعهدات هسته‌ای ایران و کاهش تحریم‌ها از سوی آمریکا وجود خواهد داشت؛ نخستین موضوعات در دستور کار نیز چگونگی تعیین تکلیف ذخایر اورانیوم غنی‌شده ایران و محدود کردن غنی‌سازی بیشتر خواهد بود.
ترامپ می‌خواهد تلاش کند این بخش را اصلاح کند.
یک مقام ارشد دولت گفت: «موضوع، جزئیات بیشتر درباره این است که آمریکا چگونه مواد را دریافت می‌کند و زمان‌بندی آن چگونه خواهد بود»؛ منظور او اورانیوم غنی‌شده بود.
منبع دوم گفت ترامپ همچنین می‌خواهد برخی از عبارت‌ها درباره بازگشایی تنگه هرمز را اصلاح کند.
این مقام آمریکایی گفت به ترامپ گفته شده است حدود سه روز طول می‌کشد تا ایرانی‌ها با پاسخ برگردند. این مقام ارشد دولت گفت: «آن‌ها عملا در غارها هستند و از ایمیل استفاده نمی‌کنند.»
این مقام ارشد دولت گفت: «توافقی در کار خواهد بود. اینکه چقدر قریب‌الوقوع است، باید دید. ما حاضریم صبر کنیم تا رئیس‌جمهور آنچه را خواسته به دست بیاورد. ممکن است یک هفته طول بکشد. ممکن است کمتر باشد. ممکن است بیشتر باشد. امیدواریم در آغاز هفته چیزی داشته باشیم.»
axios
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 403K · <a href="https://t.me/VahidOnline/75809" target="_blank">📅 05:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75808">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJmn8wT9vYeMj6rRdLzkwHXOi1MB_6_c0zEwrWRJkPHVFOBDrqtxEzYPKMRcSHfz35Qgu8YU9r3aTm50qP3iYjX3Rcw5MAwUb6D4Vg9zhBscnTkm8DTR5uKjDSJazZnOLJrWBrd2hsxRwhVFcV5M8oApCgp9N1oRwgbl8es7Sv6RDxvexjg028L0eAJw3CqBQYvLxG_silZcaBkpyi8meVq24DYpKfWSI3VuUfF3QjdKOI2grZwCxfTS98k-pC1jKaMjPbPTSXuEhKZYCB0oVuAJ7h4e1rPCMDwznpjFpnx4cqCs_V3uiB3tPFtBOssrYMb1rgm-0G2nJRWp3MmHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی سپاه بامداد یکشنبه، ۱۰ خردادماه، اعلام کرد یک پهپاد «ام‌کیو۱» (MQ1) ارتش آمریکا را منهدم کرده است.
خبرگزاری فارس نوشت: «این پهپاد با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت که بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون شد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 379K · <a href="https://t.me/VahidOnline/75808" target="_blank">📅 04:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75807">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B37IRl9KE9cLygVq1HlQTxKepZmyIGxrzWcWUwhBGmPXpXSizGQpvdnttxUrjGTjaWmNAbWYg9FmMnC8FDDrOq8Ycplnn5LUkMqbiLQg0Dh-ObNcaKpSjzuAASfkcidq4tRnYf6rg-C6ScQRY6UR2J_0gePGRNfpt5GAj_Pdzv5dy2C0KXpel6cWw8W2oGDAvSG0R0YU6TxwpRhCfITWp355GMF7tCNCl13_VR0PkyLhpIjCTR-inQbBxIXV2D6CXktoc_qqjx2FiP9yX0RN_0OYhp8cQdaAbGpiklM5PBDKY-JzkzV0FjMbOstBR02Uoy04Rg0OoYoGzENo0Zbs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستاد فرماندهی مرکزی ارتش آمریکا، سنتکام، اعلام کرد نیروهای این کشور یک کشتی تجاری با پرچم گامبیا را که به گفته واشینگتن در نقض محاصره دریایی به سمت یکی از بنادر ایران در حرکت بود، در خلیج عمان هدف قرار داده و از ادامه مسیر آن جلوگیری کرده‌اند.
سنتکام روز شنبه نهم خرداد در بیانیه‌ای گفت نیروهای آمریکایی روز هشتم خرداد کشتی «لیان استار» را هنگام حرکت در آب‌های بین‌المللی به سوی یکی از بنادر ایران شناسایی کردند و بیش از ۲۰ بار به خدمه آن هشدار دادند.
به گفته این نهاد نظامی، پس از آنکه خدمه کشتی به هشدارها توجه نکردند، یک هواپیمای آمریکایی با شلیک موشک هلفایر به اتاق موتور کشتی، آن را از کار انداخت.
سنتکام افزود این کشتی دیگر به سمت ایران در حرکت نیست.
در این بیانیه آمده است که از زمان اجرای محاصره دریایی علیه ایران، نیروهای آمریکایی پنج کشتی تجاری را از کار انداخته و ۱۱۶ کشتی دیگر را وادار به تغییر مسیر کرده‌اند.
سنتکام جزئیات بیشتری درباره محموله کشتی یا مقصد دقیق آن در ایران ارائه نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75807" target="_blank">📅 21:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75806">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnA2TPGAhiWA05xU8NffsVFi8oajYt1jtMLSQH2Gnwrem-nfFfx7PELrbFQchnXLe9egt4PWade7wNUJRgVFL_89k-Wg_utb814np7CCDZnz-j3Jk7YlxX8W_DNZ8UcV4jVb1RvBrGrJlsbhtFKs2l5-G4_6CDeWoiSyWC4DwVvLXqPIjElIvthkw6uGHObyUbNFmxGFO5fKXjVapB7JpJ5lO_jjSPz39dcU9hjfrdirPs39FV4NtuR6ZXv85OPb4D-Hw61Yg_dqjAP2yLHtJi54uUKpBPZmQfvZXnoXuxeYY3z5qdACD65nxX1Ry5nBbD8f1JVzHxjEvYC4S_A_MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی در گزارشی درباره تفاهم احتمالی بین تهران و واشینگتن با عنوان «جزئیات غیررسمی»، اعلام کرد آمریکا متعهد شده در طول ۶۰ روز امکان دسترسی جمهوری اسلامی به ۱۲ میلیارد دلار از دارایی‌ها را به‌گونه‌ای فراهم کند که این منابع قابلیت انتقال و هزینه‌کرد در بانک‌های مقصد را بدون محدودیت داشته باشد.
این گزارش افزود که بر اساس این تفاهم، جمهوری اسلامی مرجع انحصاری تشخیص ماهیت شناورهای عبوری است و هر شناوری که محموله آن تهدیدآمیز شناخته شود یا بهره‌بردار نهایی آن در «خصومت» با جمهوری اسلامی باشد، به عنوان کشتی تجاری شناخته نشده و اجازه عبور از مسیرهای تعریف‌شده را ندارد.
صدا و سیما تاکید کرد که این رونوشت هنوز در حکم یک تفاهم غیررسمی است چون مسیر آن همچنان در چرخه بررسی، مذاکره و بازبینی قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/75806" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75805">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnjTUws2lDHk0ETZIdgQxZJfi94Z0U-mqpHWPlpeGek26MZcBbMFs0IBWJxFwmIaXqdgo4LaPDpUoFAY14cYqtjhgiku9tjXVrcEiImUXVvZaTk62rIblCzLUnDVQbSfw55aPh75lZJ47YRARCbuDGJzUUfeUtGIXL0GZc68QO1UO2l2CAt4H1vX3hlAkvav8fhGvWtJBRLlSrjcRkjgKq06RZihulKcYlFkG5pe59BKB1jfIXaVFv1MsdlYLpqGZldswzbc_pTXwZRet3IyTpa27g8QehwE99D8s-Tcp7YlamGrITaRrb12JhFWAF3eL3xHDWOULGQLhHhZAPyLJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به گزارش نیویورک‌پست، در پی حمله موشکی جمهوری اسلامی به یک پایگاه هوایی در کویت، چند نفر از نیروهای نظامی و پیمانکاران آمریکایی مجروح شدند. این حمله در حالی رخ می‌دهد که دونالد ترامپ، رئیس‌جمهوری آمریکا، در حال ارزیابی پذیرش آخرین پیشنهاد صلح تهران یا بازگشت به شرایط جنگی است.
یک منبع مطلع روز شنبه نهم خرداد، اعلام کرد که در پی رهگیری یک موشک «فاتح-۱۱۰» توسط پدافند هوایی کویت طی ۲۴ ساعت گذشته، قطعات و ترکش‌های ناشی از انهدام موشک بر فراز پایگاه هوایی «علی السالم» فرود آمده و منجر به جراحت سطحی چند آمریکایی شده است. این حادثه همچنین خسارت شدیدی به دو پهپاد «ام‌کیو-۹ ریپر» (MQ-9 Reaper) به ارزش تقریبی ۳۰ میلیون دلار وارد کرده است.
این حمله در شرایطی صورت گرفته که دونالد ترامپ روز جمعه با تیم امنیتی خود تشکیل جلسه داد و اعلام کرد که قصد دارد تصمیم نهایی را درباره توافق با ایران اتخاذ کند؛ توافقی که شامل تمدید ۶۰ روزه آتش‌بس، بازگشایی تنگه هرمز و آغاز مذاکرات بیشتر درباره مواد هسته‌ای ایران در ازای لغو محاصره دریایی آمریکا می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75805" target="_blank">📅 21:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75804">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/upTGyuelmyOONEIQe2mfjJ2g2c3GgwM-CRbNtltSkEkr4XLJ-SSXmrsP7buJQcGo6_GbHVq73qsC4WYHBeCI2cZWaoeT3WANE95h3jaWtSWoWsPbyYJMnu5j8EoD3ULQAO7L1KDK1YwPJYHTdbtXETcjUErJvQnHe5G6QsSb6w2m2BStXSa0eCEeVEZxzAdm91UEjWSDFj2zI4R-N-Rey9IaD79tSGfWWeGOUWBmySZdEMduT21a9Dc0mLDBdvhXtftCqcd4eUd95_28ljKRQE8vgEBwdlWq-MMOFIV4yB9BULeV0JPW4u5bFiXau2R2CbsWRwT4zuCRXfXPPmHrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا در بیانیه‌ای اعلام کرد که هرگونه اقدام شناورهای نظامی جهت مداخله در مدیریت تنگه هرمز یا ایجاد اختلال در تردد، مورد هدف نیروهای مسلح جمهوری اسلامی قرار خواهد گرفت.
در این بیانیه آمده: «هرگونه تخلف از این ضوابط، امنیت تردد آن‌ها را با مخاطره جدی مواجه خواهد کرد.»
قرارگاه مرکزی خاتم‌الانبیا اعلام کرد کلیه کشتی‌ها، شناورهای تجاری و نفتکش‌ها صرفا ملزم به تردد از مسیرهای تعیین‌شده و اخذ مجوز از نیروی دریایی سپاه پاسداران هستند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75804" target="_blank">📅 19:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75803">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=Z5pgmJgv0J-EGaB4s2W7qGYWUjSPbTmnG5HDWSFmOwtHDwASptrvy82P4I3zCZ0MpXnM0C4ntHWGsaQH-KtJl8YZqWpxYzSTATRieVVbfuhC16Njs4xdH4u1cyNP3NXUCOlAfbdzdC_P6DuNoiy6lCeYu_sPHp_KlmacnFRCe6ja4xRNZiVaR_wiuSbt41wwWVUEbBBL0PLB-DMrGft-FaIW7V8rHWPut7yZwGYdny5Xktw-ndhx2bkRHv5Vx5PXvPLY2MoC6EEZollRVOjOBXUxTR9RorII-gNMNPVThuOFt_MqCriJPsLUfn74G1IWrrQkWsZ5IK1-Kv9fJY0fSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83c715fa8b.mp4?token=Z5pgmJgv0J-EGaB4s2W7qGYWUjSPbTmnG5HDWSFmOwtHDwASptrvy82P4I3zCZ0MpXnM0C4ntHWGsaQH-KtJl8YZqWpxYzSTATRieVVbfuhC16Njs4xdH4u1cyNP3NXUCOlAfbdzdC_P6DuNoiy6lCeYu_sPHp_KlmacnFRCe6ja4xRNZiVaR_wiuSbt41wwWVUEbBBL0PLB-DMrGft-FaIW7V8rHWPut7yZwGYdny5Xktw-ndhx2bkRHv5Vx5PXvPLY2MoC6EEZollRVOjOBXUxTR9RorII-gNMNPVThuOFt_MqCriJPsLUfn74G1IWrrQkWsZ5IK1-Kv9fJY0fSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر دفاع آمریکا، روز شنبه نهم خرداد گفت ایالات متحده در صورتی که مذاکرات با ایران به توافق منجر نشود، آماده ازسرگیری حملات علیه جمهوری اسلامی است.
هگست در جمع خبرنگاران گفت: «در حال حاضر تمرکز ما بر حفظ آمادگی و آماده بودن برای بازگشت به عملیات است، اگر لازم باشد.»
او افزود دونالد ترامپ «صبور» است و به دنبال دستیابی به «توافقی خوب» است که تضمین کند ایران هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
اظهارات وزیر دفاع آمریکا در حالی مطرح می‌شود که مذاکره‌کنندگان تهران و واشینگتن در تلاش‌اند اختلافات باقی‌مانده بر سر برنامه هسته‌ای ایران را برطرف کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75803" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75802">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mCE3xT7cnqzA6zRd5Z5ElkpOWXaBu7wQmYEezMvD_B_dsj_k7wSgHs14vOPSU9Lg8nLplymip1v63IZT6zBhQkLUQq65dM7wUOf11IPhfcV0cuau1F8FRrGqKlpbG5ebr_QxATvcl1-UxepI5xttY5jsXnunKmHxKw1KL_mtR1BXJDZn3Dv6qwR3wLn6Iv8y7bjPPRcagB0EGmDi4GkbIPSGNkC2nELAAxCCR1aKmO_nuLPbHwXArv7hmHmqWU63bpv72ObYbanv07_g-wnaBYqXVNjTajbZ_VoUzCVInu3poll3kphgvUKPGL8f5OCBKPvg9gtdxJ9PV9C_Xqoh4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصطفی نیلی، وکیل دادگستری، اعلام کرد شعبه اول دادگاه انقلاب شیراز بنیامین نقدی را با اتهام «افساد فی‌الارض» به اعدام محکوم کرده است.
نیلی در گفت‌وگو با امتداد گفت که بنیامین نقدی شامگاه ۱۳ دی‌ماه در شیراز به دلیل شعله‌ور کردن یک کپسول آتش‌نشانی به سمت ماموران نیروی انتظامی بازداشت شد.
به گفته این وکیل دادگستری، در ابتدا اتهام «شروع به قتل» به موکلش تفهیم شد، اما پس از آن اتهام وی به «محاربه» تغییر یافت.
او افزود پس از پایان تحقیقات مقدماتی، کیفرخواست بنیامین نقدی با اتهام‌های «محاربه»، «عضویت در گروه‌های برهم‌زننده امنیت کشور»، «اجتماع و تبانی به قصد ارتکاب جرم علیه امنیت کشور» و «فعالیت تبلیغی علیه نظام» صادر شد. به گفته نیلی، در خصوص اتهام‌های «ایراد صدمه جسمانی به ماموران» و «حمل سلاح سرد» قرار منع تعقیب صادر شده بود.
نیلی همچنین گفت قضات شعبه اول دادگاه انقلاب شیراز در جریان رسیدگی، مجموعه اتهام‌های مطرح‌شده را مصداق «افساد فی‌الارض» تشخیص داده و بر همین اساس حکم اعدام برای بنیامین نقدی صادر کرده‌اند.
وکیل بنیامین نقدی با اشاره به قصد خود و همکارانش برای اعتراض به این رای گفت که در مهلت قانونی درخواست فرجام‌خواهی خواهند کرد. او ابراز امیدواری کرد که با توجه به این که به گفته وی در جریان رخداد مورد اشاره هیچ فردی آسیب ندیده است و اقدامات موکلش مصداق افساد فی‌الارض نیست، حکم صادره در دیوان عالی کشور نقض شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/75802" target="_blank">📅 18:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75801">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Akbarpour🔥نیما</strong></div>
<div class="tg-text">اینترنت در ایران آزاد و عادی نشده. بیشتر مسیرهای خارجی یا بسته‌اند یا نیمه‌بازند. فقط بعضی مقاصد و مسیرهای خاص اجازه عبور دارند. همین باعث شده فیلترشکن‌های معمولی خوب کار نکنند.
در این میون بعضی از افرادی که دامنه‌ها و مسیرهای سفیدشده دارند، دسترسی می‌فروشند. نتیجه‌اش هم شده اینترنت نابرابر، رانتی و پر از راه‌حل‌های موقت.
انگاری که درِ ساختمون رو کمی باز گذاشته باشن که هوا بیاد، اما اجازه ندن کسی ازش رد بشه.
برای همینه که گوشی‌تون ممکنه نشون بده که اینترنت دارید، حتی شاید اولش سایت یا اپ مورد نظر رو باز کنه یا بهش واکنش نشون بده، اما در عمل از اینترنت خبری نیست.</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75801" target="_blank">📅 18:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75800">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iN1SrbUyF6WO15kIRuG0PwZstpazWKHgX89KLhe61ci1y54wTA9TM3zIdyhRwmBVoWN0V170mli6xyu3GlzG1K5gbwdP2Hfz3qzsjniblzxgUwzDsUmVBmwX5fswm20X66eNPPkTwWPLXH8AEbQwNpruyb-2CfGLhTsFEE4NviKltPRyqHxHkXC_qU6HJPsortReZL0jfLfwQKdUf8rCzrG0qMvD2jT2lR2ds11VXhLHBF9rVNSr3xNF7fceUfZc9ALtwxun2Q0nBj9HQ1XuXMn72OgLRhFPVBSKYzW09rKuaNHOayOUtz-s9kJADv_nhYQ40AhXw2L8Te1QHS7qaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی به نقل از سه منبع آگاه گزارش داد جنگنده اف-۱۵ای آمریکا که ماه گذشته در ایران سرنگون شد، احتمالا با یک موشک دوش‌پرتاب ساخت چین هدف قرار گرفته است.
به گفته یکی از این منابع و یک مقام آمریکایی آگاه، چین همچنین ممکن است در روزهای نخست درگیری، یک رادار هشداردهنده دوربرد را در اختیار ایران قرار داده باشد که این رادار توانایی شناسایی هواپیماهای رادارگریز را دارد.
ان‌بی‌سی نوشت مقام‌های آمریکایی همچنان در حال بررسی سرنگونی جنگنده اف-۱۵ای هستند و هنوز روشن نیست تجهیزات نظامی احتمالی چه زمانی به تهران تحویل داده شده است.
کاخ سفید به ان‌بی‌سی گفت شی جین‌پینگ به ترامپ اطمینان داده پکن تجهیزات نظامی به ایران نمی‌دهد. سخنگوی سفارت چین در واشینگتن نیز گفت پکن صادرات نظامی را «با احتیاط و مسئولیت‌پذیری» کنترل می‌کند و با «تهمت بی‌اساس» مخالف است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 440K · <a href="https://t.me/VahidOnline/75800" target="_blank">📅 07:53 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75799">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etzzI6Vn9XpZawKdUe0EvOscV1c_AyGmge6KxRbH0DA1X-N-8wDFKcdM08hCsHNZ2rPfeUJGs_3Y1VZwZVx2yl-U9nN6xpbfxlmf7aH1eirGkUJujz0Jv0u3YvmlrL8Zn9PtpGXIuVGHb-HIKJU7K-xci98LZ4DcZ2rPkbMzzhnOE1vBXttSp7qZgGWzrzqSRKySh_7vK_C9yIPMIAEmRiTC1ohuMiT0TJCR1_7mz4_Ie5zRI9sQaxX89tBf_hezAyOCGR-nohEadQmJwEpoAgWHx8cG0-XWxHDGmepgyOlm4ONk_96ZEXjc4U0n9SfWYk_fMahd4LCbkobaYWu5Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">'به جای پول نقد قطر موافقت کرده ۶ میلیارد دلار  اعتبار در اختیار تهران قرار بگیرد تا کالاها و محصولات اساسی را از قطر خریداری کند'
یک منبع آگاه از روند مذاکرات به ایران‌اینترنشنال گفت سفر قالیباف به قطر به شکستی دیپلماتیک منجر شد و با وجود درخواست تهران برای آزادسازی فوری و بی‌قید و شرط ۱۲ میلیارد دلار به صورت نقدی همزمان با امضای یک یادداشت تفاهم اولیه با آمریکا، مقام‌های قطری این درخواست را رد کردند.
به گفته این منبع، مقام‌های قطری تنها با آزادسازی نیمی از این مبلغ تحت محدودیت‌های سخت‌گیرانه موافقت کردند.
بر اساس گفته‌های یک منبع نزدیک به یک مقام قطری حاضر در این گفت‌وگوها، دوحه از انتقال مستقیم یا نقدی این منابع به ایران خودداری کرده است. در عوض، این پول تنها به صورت اعتبار در اختیار تهران قرار می‌گیرد تا کالاها و محصولات اساسی را مستقیما از قطر خریداری کند.
این محدودیت در شرایطی اعمال شده که آمریکا به شدت با اعطای دسترسی مستقیم و بدون محدودیت جمهوری اسلامی به دارایی‌های نقدی مخالفت کرده است.
آمریکا ابراز نگرانی کرده است که تزریق مستقیم پول نقد می‌تواند برای تهران فضای تنفسی اقتصادی حیاتی ایجاد کند و به آن اجازه دهد حقوق‌های معوقه بخش عمومی را پرداخت کرده و در دوره‌ای از تنش شدید منطقه‌ای، تجهیزات نظامی را از کشورهای دیگر تامین کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 429K · <a href="https://t.me/VahidOnline/75799" target="_blank">📅 03:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75798">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=k6nY7RTpsB2Zw4f0RfeoVuVub46RJnHFfoIcSZNteVac9HaitFq5tqelZAv8bYnfjPcxaELaURZnBFFKtHTYG1YSXtCeZDlQI4D_m_Kmwd5lRU2yvcnftRwOfeUN6AtbqVPnlAeujjLwA-b7o8an6664a6uQdkF0kpIr2c1c4sX_J5P9_Q5Vf6dGCtAacsvwHPs7F78Yo34VS7EmkPPPtQy_yH1Zuy_DonoODtPXJkebjYQ6_YufSXdTEvXxQmSnlw9EsP2pwqpgXdbLrQopumgpwqFr9d8k7WLlvFa6vGtLctOZXpkDItPVn73Zur8LnbGBVufu1qMGz6jWXy5oew" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/139e7f5cd8.mp4?token=k6nY7RTpsB2Zw4f0RfeoVuVub46RJnHFfoIcSZNteVac9HaitFq5tqelZAv8bYnfjPcxaELaURZnBFFKtHTYG1YSXtCeZDlQI4D_m_Kmwd5lRU2yvcnftRwOfeUN6AtbqVPnlAeujjLwA-b7o8an6664a6uQdkF0kpIr2c1c4sX_J5P9_Q5Vf6dGCtAacsvwHPs7F78Yo34VS7EmkPPPtQy_yH1Zuy_DonoODtPXJkebjYQ6_YufSXdTEvXxQmSnlw9EsP2pwqpgXdbLrQopumgpwqFr9d8k7WLlvFa6vGtLctOZXpkDItPVn73Zur8LnbGBVufu1qMGz6jWXy5oew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران، بامداد شنبه ۹ خرداد با انتشار تصاویری مدعی شد بقایای یک پهپاد متعلق به آمریکا و اسرائیل که در حوالی قشم هدف قرار گرفته، کشف شده است.
تسنیم بیان کرد این پهپاد با واکنش پدافند هوایی ارتش هدف قرار گرفت و منهدم شد.
پیش از این خبرگزاری مهر به نقل از منابع محلی گزارش داد یک ریزپرنده در حوالی قشم از سوی پدافند هوایی هدف قرار گرفته و منهدم شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 414K · <a href="https://t.me/VahidOnline/75798" target="_blank">📅 02:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75797">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UHg04oMbUZrhCNOx89VSbWrAKxhYuEZbL2d36GjgqqeXe1s3yK_qzzH6nUF8ATg2AEBOWE-fvo0hCrRCyvsvt5gB4ml_udvwJSE2Bqfi7TQL76xPc1VMNomXpJNaAknmiO8Jv_ymAS-LE4ZTmvDSyyXdhhv168K-leqhIjICmE7p3D1raWqxSoNwdPgjbThc5OayZb3WxsCwhuBBqxQZB4o5aOsOosc6IqibCCZB-DsonvaUygYMSrOhqvfraEfg-GdZ5v_oU63ySVKf0qNqxEe4obiDteQQr8WvnHltDupljyW9IPwZoNHDWiWcYG_Os-9jCRneoG3dkiTI2eUJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش نیویورک‌پست، یکی از آخرین موارد اختلاف بر سر راه توافق احتمالی میان واشینگتن و تهران، چگونگی آزادسازی مرحله‌ای دارایی‌های ایران است که در قطر نگهداری می‌شود و برای اهداف بشردوستانه در نظر گرفته شده است.
بر اساس این گزارش، منابع مالی مورد بحث مستقیما در اختیار حکومت ایران قرار نخواهد گرفت، بلکه برای خرید مواد غذایی و تجهیزات پزشکی استفاده می‌شود و سپس این اقلام به ایران ارسال خواهد شد.
نیویورک‌پست به نقل از یک مقام دولت آمریکا نوشت پرداخت تدریجی این منابع به اجرای تعهدات از سوی ایران، از جمله بازگشایی تنگه هرمز و پاکسازی مین‌ها در تنگه هرمز، وابسته خواهد بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75797" target="_blank">📅 01:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75796">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=RzT88KnLJg8v-byG6EOQS8TI7XJ-XeFJq-gCwWGHrsXcJTyquzCK3GKuWzvEY7yNckqEqfu7ukYUsrRvTMHNG955vRvT-SO2-NSWJVjw-D1Y5l9M-0DrvXu4P6g_-tdN5t9u_Ufr2cHJnu2VKEI59b_9J9E-EmJtw1JhbZDBpRIz5nlxfK6T4rJ0KMCPLtkN4ONZr-3kmw8SssAYIpkSgNria6fupnpoF_2b1XrGMZqrVe4L2Rplfid5S8oyrBEnMEml29uY0JzKXxupkyYeGWdTinLZ7qwrI-acDoEx3wzggd0GkljmEXp2UsB9No3WDP7SMBhwcMO3kW1dE99CmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3e9ce77c58.mp4?token=RzT88KnLJg8v-byG6EOQS8TI7XJ-XeFJq-gCwWGHrsXcJTyquzCK3GKuWzvEY7yNckqEqfu7ukYUsrRvTMHNG955vRvT-SO2-NSWJVjw-D1Y5l9M-0DrvXu4P6g_-tdN5t9u_Ufr2cHJnu2VKEI59b_9J9E-EmJtw1JhbZDBpRIz5nlxfK6T4rJ0KMCPLtkN4ONZr-3kmw8SssAYIpkSgNria6fupnpoF_2b1XrGMZqrVe4L2Rplfid5S8oyrBEnMEml29uY0JzKXxupkyYeGWdTinLZ7qwrI-acDoEx3wzggd0GkljmEXp2UsB9No3WDP7SMBhwcMO3kW1dE99CmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، روز جمعه هشتم خرداد در «مجمع اقتصادی ملی ریگان» اعلام کرد که واشنگتن حدود یک میلیارد دلار از دارایی‌های رمزارزی مرتبط با حکومت ایران را به طور مستقیم توقیف و کیف‌پول‌های دیجیتال آن‌ها را ضبط کرده است.
او با تاکید بر اینکه این اموال در واقع پول‌های دزدیده‌شده از مردم ایران است، اشاره کرد که بسیاری از صاحبان این حساب‌ها هنوز متوجه ضبط دارایی و کیف‌پول دیجیتال خود نشده‌اند.
وزیر خزانه‌داری آمریکا همچنین افزود واشنگتن با همکاری نزدیک متحدان اروپایی خود در حال ردیابی و توقیف املاک و مستغلات، از جمله ویلاها و خانه‌های متعلق به این افراد در سراسر اروپا است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/75796" target="_blank">📅 23:22 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75795">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KbovuE4do6wEHv4Lv1ByHAwQTwl7DyvZtF28PHOkTpQFc1b7rb-TbPN-dWCbyuDdKTFPVdedbJzw27aEKlh2Lnb1hBoeNdLlG4NzZ1i0oPtfJ_-kQpCbc9Cm-JEOm7jJTdZmJ13V75edWiPn40jlrz49YSM9vJAd1i7y3YLSwLl1w2MxGf5bk3qvxEnLdfeyOtdX32T1QfiZpz5JMTpdpfU8UmfDciYVdbwiL1hWmfaDA7feQ0dEcfHNhjoS2TCJIJqFfQGBl1ZuyYFgik_sqpqFhqMs4u8JY5LhXofkZRRvo438D0F7pRmdrL_wE43HxcZij86tNoj7728LbuRwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک‌تایمز به نقل از یک مقام ارشد آمریکایی گزارش داد نشست دونالد ترامپ در «اتاق وضعیت» کاخ سفید دو ساعت به طول انجامید، اما رییس‌جمهور آمریکا هنوز درباره هیچ توافق جدیدی با تهران به تصمیم نهایی نرسیده است.
این مقام افزود دولت آمریکا معتقد است به دستیابی به توافق نزدیک شده، اما برخی مسائل از جمله آزادسازی دارایی‌های مسدودشده همچنان محل بررسی و اختلاف‌نظر است.
@
VahidOOnLine
یک مقام ارشد به خبرگزاری آسوشیتدپرس گفت که این جلسه در حال بررسی چارچوب توافقی بود که آتش‌بس را به مدت ۶۰ روز تمدید می‌کرد و مذاکرات در مورد برنامه هسته‌ای ایران را پیش می‌برد.
این مقام رسمی در مورد اینکه آیا ترامپ پس از این جلسه تقریباً دو ساعته تصمیمی برای پذیرش این توافق اولیه گرفته است یا خیر، اظهار نظری نکرد.
sky
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/75795" target="_blank">📅 22:31 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75794">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLgQwoSS5xfw_NptI-wItnJ6pE5-5e85FJXQJ7O8YnxS-Kx9sWcUPSIwCyatNFqY0uHcXxVd25Xy--fTTKS20WpZy1IvRcSRfQP5MekDBzr7CK85G7WJ1fAowqMcEd5JeQvXOIGvfUGadNV1iuNcjRdH-7YTNy7AamcJSSEjPBl9OwWENNjqrkJxv9tt23i4gsBXBIOZWN1n4JOMuNaZwtymp3JD8lWGzlUUk0Lz6ulg2ple1cFeGhUdjgw0EwAiB04tuaBgZoy1f5acFQlp-cs0cy9EhHY4MuTS6CrFgNwATNqHAxhMec1EQ-Pn72ZiRU9a5_Pmfoefbf7jqxPM2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال روز جمعه هشتم خرداد، در گزارشی اختصاصی به نقل از منابع آگاه فاش کرد که امارات متحده عربی در طول جنگ، ده‌ها حمله هوایی را علیه مواضعی در ایران انجام داده است.
منابع وال‌استریت ژورنال می‌گویند نقش امارات در این کارزار نظامی، «بسیار عمیق‌تر» از آنچه که پیش‌تر گزارش شده، بوده است.
بر اساس این گزارش، این حملات با هماهنگی کامل واشنگتن و تل‌آویو و با اتکا به اطلاعات ارائه‌شده از سوی آن‌ها انجام شده است.
اهداف امارات شامل جزایر قشم و ابوموسی در تنگه هرمز، بندرعباس، پالایشگاه نفت جزیره لاوان و مجتمع پتروشیمی عسلویه بوده است.
حملات به عسلویه که به صورت مشترک با اسرائیل و در پاسخ به ضربات جمهوری اسلامی به زیرساخت‌های انرژی امارات انجام شد، واکنش‌های شدید بین‌المللی را برانگیخت و واشنگتن را وادار کرد از اسرائیل بخواهد حمله به تاسیسات انرژی را متوقف کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 394K · <a href="https://t.me/VahidOnline/75794" target="_blank">📅 22:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75793">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">#قشم
پیام‌های دریافتی درباره فعالیت پدافند:
سلام وحید
قشم ساعت ۲۱:۲۵ تاریخ جمعه ۸ خرداد
پدافند فعال شد من در محدوده قلعه پرتغالی‌ها شهر قشمم و شلیک پدافند کاملا قابل دیدن و شنیدن بود
21:26 هشتم خرداد جزیره
#قشم
صدای توافق خیلی بلند به گوشمون رسید. حدود یک دقیقه صدای شدید پدافند، احتمالا برخورد موفق با پهباد نفوذی.
درود همین پنج دقیقه پیش پدافند قشم داشت شلیک می کرد درگیری بود
ساعت 21:25
همین الان پدافند قشم فعال شد و یک چیزی رو زد
🔄
آپدیت:
تسنیم: "در پی رصد ریزپرنده متخاصم دشمن آمریکایی ـ صهیونی در حوالی قشم توسط پدافند هوایی ارتش، بلافاصله در عملیات موفق مورد اصابت قرار گرفت و منهدم شد."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/75793" target="_blank">📅 21:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75792">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gP9kMt4dIGH7nc6Y2KWnDXOR2o_-iG9OICyEblH05en1ktdVma46Uh1zx0dRyB2J9HrSn8lpA-3eRRAew7j7d2TtpB0GSOJSQ8eRqNPu3FGpHzcUcj6gxzG2fZ96mVnunMrhjWZo0zdUxXlUtkQ6MAs9ScYzlCvV3zyeZJePrj9H2BG-w2SrzKqkipUTN_SN1kfYsW_ghND5dlirSM4-J6EK3Igt_81cRYsptsborlT9-DH8gmvWC5hWPBgLBdQD35itHW91wg7X25FxUrmHNzLcykOGUpTybUpq7SAZYz308C8frrEEe0fIONgWzr375nI5eK2cl0BuY6oMxKQWdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ پستی از نیوت گینگریچ، رییس پیشین مجلس نمایندگان آمریکا، را در تروث سوشال بازنشر کرد که در آن نوشته شده بود: پس از بررسی جنگ ایران در این هفته، متقاعد شدم ترامپ در آستانه یک پیروزی تاریخی قرار دارد
IranIntlbrk
پستی که گینگریچ ۸ ساعت پیش نوشته بود، ترجمه ماشین:
پس از آنکه این هفته را صرف بررسی جنگ ایران کردم، اکنون متقاعد شده‌ام که رئیس‌جمهور ترامپ در آستانه یک پیروزی تاریخی قرار دارد. نقطه عطف واقعی برای من زمانی رقم خورد که تصمیم‌ها و مانورهای رئیس‌جمهور ترامپ را نه از منظر یکجانبه‌گرایی آمریکا، بلکه از منظر رهبر یک ائتلاف تاریخی چشمگیر بررسی کردم؛ بزرگ‌ترین ائتلافی که تاکنون در خاورمیانه مدرن شکل گرفته است.
همه می‌دانند که اسرائیل متحد مهمی است. اما آنچه کمتر درباره آن صحبت می‌شود، عمق حمایت امارات متحده عربی، قطر، بحرین، عربستان سعودی و دیگر کشورهای منطقه است. برای دیکتاتوری ایران باید بسیار تأمل‌برانگیز باشد که دریابد حتی یک متحد ندارد که حاضر باشد محاصره دریایی آمریکا را به چالش بکشد. آرام‌آرام، به‌تدریج و با احتیاط، متحدان اروپایی ما نیز در حال صف‌آرایی برای کمک در خلیج فارس و تنگه هرمز هستند.
بخش بزرگی از مانورهای رئیس‌جمهور ترامپ علیه ایران زمانی معنا پیدا می‌کند که او را نه صرفاً یک رئیس‌جمهور یکجانبه‌گرای آمریکایی، بلکه رهبر یک ائتلاف ببینیم. من بخش زیادی از چند هفته گذشته را صرف بررسی گزینه‌های نظامی کردم؛ از جمله پیروزی در نبرد خلیج فارس و تنگه هرمز و، در صورت لزوم، استفاده از سطحی تکان‌دهنده و خردکننده از قدرت نظامی؛ مشابه آنچه رئیس‌جمهور نیکسون و وزیر خارجه کیسینجر در کریسمس ۱۹۷۲ علیه هانوی و هایفونگ به کار گرفتند؛ اقدامی که هر دو رهبر معتقد بودند ویتنام شمالی را به پذیرش آتش‌بس و آزادی اسرای آمریکایی متقاعد کرد.
اگر این یک کارزار یکجانبه آمریکایی بود، می‌توانستم با اشتیاق از یک کارزار نظامی تهاجمی‌تر حمایت کنم. اما در عین حال روشن است که چنین اقدامی ائتلاف را از هم می‌پاشاند، زیرا متحدان عرب ما متقاعدند که ایران هنوز می‌تواند خسارت عظیمی به میدان‌های نفتی و زیرساخت‌های آنان وارد کند. ائتلاف‌ها ذاتاً کندتر از کارزارهای یکجانبه عمل می‌کنند. با این حال، ائتلاف‌ها در نهایت قدرتی به‌مراتب بیشتر را وارد میدان می‌کنند.
من نیز مانند همه دیگران از سرعت گفت‌وگوها با این دیکتاتوری سرخورده‌ام؛ اما پس از بررسی توازن قوا و گزینه‌های در دسترس ائتلاف از یک سو، و دیکتاتوری مذهبیِ ایران از سوی دیگر، آماده‌ام بگویم که رهبری ائتلافیِ رئیس‌جمهور ترامپ ــ چیزی که تقریباً هیچ‌یک از منتقدان او نمی‌خواهند به آن اذعان کنند ــ در آستانه دستیابی به یک پیروزی عظیم تاریخی است.
و اگر دیکتاتوری ایران در نهایت ثابت کند که به شکلی نومیدانه به موضعی انتحاری پایبند است، زمان کافی برای یک کارزار نظامی با قدرت و اثربخشی عظیم وجود خواهد داشت. در هر صورت، ما در آستانه یک پیروزی شگفت‌انگیز برای ارزش‌های خود و برای خاورمیانه‌ای امن‌تر قرار داریم.
NewtGingrich
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/75792" target="_blank">📅 21:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75791">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGatV-S4oIe_oZaa5JPQrzqmj85QnVVJP-nyJMQwPxeOqY-wfHsbe6_slY1FLCWyw-JBBSj1QGisn-lOtQ_2J-tyATsl6s66CfoRprmnLpQZEGl3GVpDdPu7SjoxkzX__8mpPojjTCLgPi4ck-WZa2gqHs4FHFbpNsXTwhwjbx5BgxftXhkB8DTL3dPuItA9AnLU3pWFMaRs75_6bJFKjedukQu4wlevElXVN6mHlnI7MpG5SpD7f043JU3Kz2Kb8gIYmEqJ4pp1aHC-iDBf2uPjFJ2G-7Gf97OZKZXrRRA98cUR19KgUsYSkyL40jFHWfnbkmfMKEFjl7evNpABrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی خانعلی‌زاده، عضو تیم رسانه‌ای هیات مذاکره‌کننده جمهوری اسلامی، نوشت که در متن تفاهم احتمالی هشت بند از ۱۰ بند بیانیه شورای عالی امنیت ملی که به تایید مجتبی خامنه‌ای رسیده، رعایت نشده و زیر پا گذاشته شده است.
او افزود که تفاهم‌نامه کنونی برخلاف بیانیه آتش‌بس شورای عالی امنیت ملی است و مشخص شده که اساسا مذاکرات پسااسلام‌آباد، بر مبنای شروط رهبری انجام نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/75791" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75790">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dpxvyT6Ff1Rhx4vYIBXh-68P94tQfFzhdEWwIRCgeZED5Axflog1i67G6UNe-ie_mmCNgJmhG_hxwBo_jGr0SGhz4-knk-CJ4T4HMOT2XfqrCe-Sbx351voHkLCJ6NVBPTHKWf4_SzvnHUB6jUdm8OB0iWtm7mpunVmXRweL7ipYhaOi2DOIevMNJtiGf0G_WZMlEZgIC_N5j3ov6wgXPqYtZESHQu6jFqAop9jj0dlSwaVfXbF48mitrsq-6UkyqzMRFCW45n8y1jCqBoKjCsf7oj0NNNg6edaE3MXVWhGHv1ODgHbwuxNSKk5oSOPxKwrwXrKipZFKGNDdkMr8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت خارجه ایران در مصاحبه‌ای با صدا و سیما گفت که تبادل پیام‌ها ادامه دارد ولی هنوز هیچ توافقی نهایی نشده است و افزود که مدیریت تنگه هرمز باید توسط ایران و عمان تعیین شود.
او بار دیگر گفت: «در این مرحله بر خاتمه جنگ متمرکز هستیم و در مورد پرونده هسته‌ای هیچ مذاکره‌ای نداریم.»
این اظهارات در حالی از سوی ایران مطرح شده که آقای ترامپ فهرستی از خواسته‌هایی را که می‌گوید ایران باید برآورده کند، مطرح کرد که شامل تعهد ایران به عدم دستیابی به سلاح هسته‌ای، باز کردن تنگه هرمز بدون دریافت عوارض، مین‌روبی کامل این آبراه و خارج‌سازی ذخایر اورانیوم ‌غنی‌شده ایران با همکاری آمریکا و تحت نظارت آژانس و سپس از بین بردن این مواد است.
@
VahidHeadline
پیش‌تر: خبرگزاری فارس، نزدیک به سپاه پاسداران، نیز به نقل از یک منبع ایرانی دیگر اظهارنظر رئیس‌جمهور ایالات منحده دربارهٔ توافق احتمالی با ایران، را «آمیخته‌ای از راست و دروغ» خوانده است.
این منبع گفته که در متن توافق بندی درباره باز شدن تنگه هرمز بدون دریافت عوارض وجود ندارد و تفاهم بر سر نابودی دخایر اورانیوم ایران را نیز «بی‌اساس» دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/75790" target="_blank">📅 20:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75789">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JSp3nm9bI4ZMXVKWp3NsfbZqzc4GoocT-AFuRCk3tpVuIg6eQTzKZe4YUCetr8pAmK5aW7O1DrFCDQRHflHwZaUZIuqtSfLtFVmU1WU50p_8kY-i0Far3sO09RGEHFOnnCHAPpTFOK9K3qKexVr0dXAkurwPWYHY1bnTtjdCOMOuvpIRoX951ToQvkmDqixXM4fXGfhyoS-8Q8juhCJXiWyqadw2d3X0Sl97mLXaCgmi4zr1us15MYMRyS-7Wj3xmLep0exm4FdWHM7dE96BzpoILJIQxi_CWxf9GVz_WsiUuGsWll8l_LbHnvyjIzuA_mNhBwXxbBu6rzaipWUg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
پست ترامپ، ترجمه ماشین:
ایران باید بپذیرد که هرگز سلاح یا بمب هسته‌ای نخواهد داشت.
تنگه هرمز باید فوراً، بدون عوارض، برای عبور و مرور آزادانه کشتی‌ها در هر دو جهت باز شود. همه مین‌های دریایی، اگر وجود داشته باشند، برچیده خواهند شد؛ ما با مین‌روب‌های زیرآبی فوق‌العاده خود، شمار زیادی از این مین‌ها را از طریق انفجار از بین برده‌ایم. ایران نیز باید فوراً هر مین باقی‌مانده‌ای را، که تعدادشان زیاد نخواهد بود، جمع‌آوری یا منفجر کند.
کشتی‌هایی که به‌دلیل محاصره دریایی شگفت‌انگیز و بی‌سابقه ما در تنگه گرفتار شده بودند ــ
❗️
محاصره‌ای که اکنون لغو خواهد شد ــ می‌توانند روند «بازگشت به خانه» را آغاز کنند! از طرف من، رئیس‌جمهور محبوبتان، به همسران، شوهران، پدران، مادران و خانواده‌هایتان سلام برسانید!
مواد غنی‌شده، که گاهی از آن با عنوان «غبار هسته‌ای» یاد می‌شود و در اعماق زمین دفن شده؛ در حالی که کوه‌هایی که عملاً بر اثر حمله قدرتمند بمب‌افکن‌های B-2 ما در ۱۱ ماه پیش فرو ریخته‌اند روی آن قرار دارند،
❗️
توسط ایالات متحده از زیر خاک بیرون آورده خواهد شد؛ کشوری که، طبق توافق، تنها کشور در کنار چین است که توان مکانیکی انجام چنین کاری را دارد.
این کار با هماهنگی و همکاری نزدیک با جمهوری اسلامی ایران و همچنین آژانس بین‌المللی انرژی اتمی انجام خواهد شد و سپس این مواد نابود خواهد شد.
❗️
تا اطلاع ثانوی، هیچ پولی رد و بدل نخواهد شد.
درباره موارد دیگری که اهمیت بسیار کمتری دارند نیز توافق حاصل شده است.
💥
اکنون در اتاق وضعیت جلسه خواهم داشت تا تصمیم نهایی را بگیرم.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 389K · <a href="https://t.me/VahidOnline/75789" target="_blank">📅 18:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=rBVHk62FB7WkBUqIo93XKbAf8-ZcjOPqsdJSj6Gj6V9BUDnMvtFNeiApL1RNaOQZru3VA_Ozk1zY7BwDNm-aYPKpd3j79hKYnoHlty7cv7eDWK5kXMfBQv9bFj025SUezT0_P8wiDfkhKzaSEiHF9NPfd4wLqoWAgVrc2BE7M6HTwpanhulg03MiOmu0oBGjwAmGn65MbmAh_jLEM04j-6cuRrWmARUz3eElHgxlXwCEHIfiDcmSwicnIyMeeTJcx0udfs_3OS47p_Kn0uuZhYm42hgFhQuEfJLspE8RM7agiFPmEa1leMiGQmYp_czNMDK8ibuELsABQBp0fTJnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1103555bb8.mp4?token=rBVHk62FB7WkBUqIo93XKbAf8-ZcjOPqsdJSj6Gj6V9BUDnMvtFNeiApL1RNaOQZru3VA_Ozk1zY7BwDNm-aYPKpd3j79hKYnoHlty7cv7eDWK5kXMfBQv9bFj025SUezT0_P8wiDfkhKzaSEiHF9NPfd4wLqoWAgVrc2BE7M6HTwpanhulg03MiOmu0oBGjwAmGn65MbmAh_jLEM04j-6cuRrWmARUz3eElHgxlXwCEHIfiDcmSwicnIyMeeTJcx0udfs_3OS47p_Kn0uuZhYm42hgFhQuEfJLspE8RM7agiFPmEa1leMiGQmYp_czNMDK8ibuELsABQBp0fTJnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با شرح عبور موشک‌های تاماهاک در مرز عراق و ایران در شبکه‌های اجتماعی و چند رسانه منتشر شده و گفته می‌شود مربوط به روزهای نخست جنگ است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/75788" target="_blank">📅 17:49 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=krGItHLlllMds5ZYKI34tDrjIDAT3F_jlB_0WO2JrMgcV118kRIBF05TFNKv_aWv9dabsBoeGuLL2is6YtBe_iXXAghGn7XwtsZgA7tUxbzfGkcU9ajflGHEgidVNCMe8MfM6XDleBjKoVbSNXv5Ja8DA0AE5V6E2gvLnAIrj53iMozKoSLllQZdL3m57X1HZKLXLsZkyhSNwWBhfyOJbn18rRV0kY8vFJFPbd04ENHtI1DWr2sNvofImjaHbYg6fVaUcvN2WjLutF8ZYrxeobMcjbvaktAglQYlcJbEbyTxyzC7jZ8jlPwAFZNc3k3YLL0q2gzgpUyqkRNpya9UnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5091050bbb.mp4?token=krGItHLlllMds5ZYKI34tDrjIDAT3F_jlB_0WO2JrMgcV118kRIBF05TFNKv_aWv9dabsBoeGuLL2is6YtBe_iXXAghGn7XwtsZgA7tUxbzfGkcU9ajflGHEgidVNCMe8MfM6XDleBjKoVbSNXv5Ja8DA0AE5V6E2gvLnAIrj53iMozKoSLllQZdL3m57X1HZKLXLsZkyhSNwWBhfyOJbn18rRV0kY8vFJFPbd04ENHtI1DWr2sNvofImjaHbYg6fVaUcvN2WjLutF8ZYrxeobMcjbvaktAglQYlcJbEbyTxyzC7jZ8jlPwAFZNc3k3YLL0q2gzgpUyqkRNpya9UnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنجشنبه هفتم خرداد ماه اعلام کرد عمان پس از دریافت هشدار واشنگتن درباره پیامدهای احتمالی مشارکت در طرح دریافت عوارض از کشتی‌های عبوری از تنگه هرمز، به آمریکا اطمینان داده است که برنامه‌ای برای اجرای چنین طرحی ندارد.
بسنت روز پنجشنبه در نشست خبری کاخ سفید گفت که صبح همان روز با سفیر عمان گفتگو کرده و از او شنیده است که مسقط هیچ برنامه‌ای برای دریافت عوارض در تنگه هرمز ندارد.
او افزود: «به او گفتم این موضوع از اساس غیرقابل قبول است و او نیز نمی‌خواهد افراد عمانی یا موسسات مالی عمانی را در معرض خطر تحریم قرار دهد.»
بسنت ساعاتی پیش‌تر در پیامی در شبکه اجتماعی ایکس هشدار داده بود که وزارت خزانه‌داری آمریکا هر فرد یا نهادی را که به‌صورت مستقیم یا غیرمستقیم در تسهیل دریافت عوارض در تنگه هرمز نقش داشته باشد، هدف تحریم قرار خواهد داد. او تصریح کرده بود که هر شریک احتمالی این طرح نیز با مجازات و تحریم روبه‌رو خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/75787" target="_blank">📅 17:44 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L87h4l_URCngoQCo04YAeLW19rq3hyAlg1h9axWRxtTDkThiDOJmPFXKCEL_Fyg02h0PWRZkoxBWeniO116LwluGLeM4GU62D6-yJ1eU2z0Hpsz1wCbnLCF5hE1M5Mj8L8-iyEACgvsZL5waJ44sX-u3GK9Iu7869jwfpNdfJBLBj6HXI0VdJlYGwdKYMXzfu8tulrTTMgEIoL2qHqiPToNieBoiGKzpmpXhyXCGvc2J9X2AanV2ZySzpguOiAKN4QLf1NpGG3fk5eg0O6FCbDtO7slQdhSgzjdopxccyJsE0vBPOEuzoZtaBDZ64J1AGwmn3Ma0rA65anDHSKC03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه العربیه به نقل از منابع آگاه گزارش داد جمهوری اسلامی می‌خواهد اورانیوم غنی‌سازی‌شده خود را به چین منتقل کند، مشروط بر آن‌که چین تضمین دهد این مواد را به آمریکا تحویل نخواهد داد.
به گفته این منابع، بسیاری از نکات مرتبط با برنامه هسته‌ای جمهوری اسلامی در مذاکرات جاری حل‌وفصل شده است.
بر اساس این گزارش، جمهوری اسلامی با نظارت بین‌المللی بر تاسیسات هسته‌ای خود برای جلوگیری از تعطیل‌شدن آن‌ها موافقت کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75786" target="_blank">📅 17:43 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jxe-YhJHEK7srgMl-3cj9TgU3YjXjGhwHguxQemXw2gURvJKXLNrjKPa_8ixoTXv-AAlSu45X8boe2-LvIJxrxvTcaDHob7isoS_TU3pBtBnQGWfGrBuDHqsS00VDj_gcP7Xqwm0oRHuwCgUk2C7PQjV2K5kzxtYQwhaGHPAtbPEfP0oIDyN00WUDekH4s_mc9oyyNlHPWIhaIJkd_UJl2f5BPPK-Ez23ogeSDU34MIIHXvp97Wobu1seFrGJRJhUL3gMYm0o0Lkd1Z9xlHdFuFkvlfYPIoJvHlU9uVz02TYCG32cfFf4J4IByoSJqcdwfJKuzm6cjyZ80KLb6HlSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد جمهوری اسلامی با آمریکا، روز جمعه تهدید کرد که تهران امتیازات مورد نظر خود در توافق پایان دادن به جنگ را با «موشک» می‌گیرد و پیش از اقدام واشینگتن درباره این توافق اقدامی نخواهد کرد.
او در شبکه ایکس همچنین نوشت: «هیچ اعتمادی به تضمین‌ها و حرف‌ها نداریم، فقط رفتارها معیار است.»
این موضع‌گیری یک روز پس از آن انجام شد که چند رسانه غربی خبر دادند آمریکا و ایران به تفاهمی برای تمدید آتش‌بس و رفع محدودیت عبور و مرور کشتی‌ها در تنگه هرمز رسیده‌اند، اما این توافق منتظر تصمیم و امضای نهایی دونالد ترامپ، رئیس‌جمهور ایالات متحده است.
قالیباف در پیام خود اعلام کرده که «اقدامی پیش از اقدام طرف مقابل انجام نخواهد شد».
از سوی دیگر، رسانه‌های نزدیک به سپاه پاسداران می‌گویند گزارش‌ها درباره توافق تهران و واشنگتن صحیح نیست. خبرگزاری تسنیم در این مورد به نقل از یک «منبع مطلع» نوشت: «متن توافق تا این لحظه جمع‌بندی نهایی نشده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75785" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghygsXnutQPMnI0f0yG89agnep5uTUCoT_yLP8AbLrCIiGFnIOW-5T2NiXDDGyKer9SsGeO7BPL9N30vvzkz-O6D5EygvgQatlRNEgb6jVhdMuTnKCu1XCQbChvK3K6zG3TC_r--Z2z8n6Bha1m0oJ1YY_kATE3BLax0L5xY1d-5vYxED4VxTT-dXttXrMqBNmWyj1txWqsr63kvvTI7SB1pcXWj1oVAX_gQqJ5ANfTqajcvDoEV4Z7vx3MJSfwzqbVZVoU3CHZr50UPb7iS6v9pVF747sU8c_4Zre84LT9xea9PU2n8nXWeyf-x0Ck5_JV4Lrw8CSUo_NaW5wplNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند از ابتدای سال جاری تاکنون، اجرای ۶۶۰ مورد اعدام توسط جمهوری اسلامی را مستند کرده است. با این حال، به دلیل ماهیت پنهان‌کاری و غیرشفاف بودن سیستم قضایی ایران، آمار واقعی به احتمال زیاد بسیار بیشتر از این رقم است.
‏
🔸
از زمان آغاز جنگ، آمار اعدام معترضان و افرادی که به جاسوسی و اتهامات مشابه علیه امنیت ملی متهم شده‌اند، با سرعتی نگران‌کننده افزایش یافته است. «اعترافات اجباری»  قربانیان، اصلی‌ترین «مدرک» مورد استفاده در این احکام مرگبار بوده است.
‏
🔸
این اعترافات در شرایطی کاملا مبهم و تحت فشارهای شدید جسمی و روحی اخذ می‌شوند. جمهوری اسلامی به طور مستمر این اعترافات اجباری را در رسانه‌های دولتی پخش می‌کند تا از آن به عنوان ابزاری برای توجیه اعدام‌ها و سرکوب مخالفت‌های عمومی استفاده کند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/75784" target="_blank">📅 17:41 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOhbPJ64sgwooB1NZw22iQaTcrYWsAY9Y4lPD3xfICIe0hShBGz_QQ9fmTuBfiVrD_6rbd_t10J8a_Fx3846XMYMmY6fcyuUvwnfkfU4HmKsH8rwKXfEMyiZENU0jKZ9LK58xG4eQfmUvQueDQoJNdd2ylMb3Kjp5HG6ICQ4FYycnXsauM-uLyVoWZhpJ9z9x20m5UAaEpLT_i89U-m-zxrTxrt_pa7I-pnFu7X43JUFbYWfi5luZ7eejw_HvydQwJkdAffdk9ZPmd2AwDJaWVcXurqKI13cvz1qPr-5SyBM-_G4awX81Ajfwafrnk21vE7llh6qDzW7TO-v-tuyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ‌ ‌ ‌
شیخ تمیم بن حمد آل ثانی، امیر قطر، در تماسی تلفنی با دونالد ترامپ، رئیس جمهور آمریکا، در مورد تحولات منطقه‌ای گفتگو کرد.
دفتر امیر قطر در گزارشی از این مکالمه تلفنی اعلام کرد که شیخ تمیم بر اهمیت اولویت دادن به راه‌حل‌های دیپلماتیک و گفت‌وگو بین همه طرف‌ها به امید جلوگیری از تنش‌ها و تشدید بیشتر در خاورمیانه تأکید کرد.
در این بیانیه آمده است که ترامپ نیز به نوبه خود از نقش قطر در حمایت از تلاش‌های میانجیگری پاکستان بین واشنگتن و تهران قدردانی کرد و «از تلاش‌های قطر برای رفع اختلافات و ترویج کاهش تنش در منطقه» تمجید کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/75783" target="_blank">📅 02:20 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75782">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=oPCpHE5oh6Fdd_HBaiFjb4NlK2ZJh5qpA5NjK8Vv4RiRlJ4ZNIQE5NvvcGCOAmJNKySsTRT_8B_d_cldLS2ZLKjSDYQ7Qixc9cWjESxBmNv1mJ9qzCEgOPM5WQxrD_wpN6GbXiGIOCY2E_7oPDPvhI3kbF2yati82E8Rp0U1XC93BK57_pTKQPfJIHJN34eW9egNXshvLNMMpZ1YrUUUqXnF_W0mcvuH37ie0T9_qT_aoLk7yJ8CL8t62f-OzDk76SM1VjMuHrUNjZ7xuYL_PkrXYAuN1I9H6txDY8omsnhR6hJ-NjiW-68ZnTMW8utRNyMAGmvVn9JMqlYmjolx7g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41d327c1f6.mp4?token=oPCpHE5oh6Fdd_HBaiFjb4NlK2ZJh5qpA5NjK8Vv4RiRlJ4ZNIQE5NvvcGCOAmJNKySsTRT_8B_d_cldLS2ZLKjSDYQ7Qixc9cWjESxBmNv1mJ9qzCEgOPM5WQxrD_wpN6GbXiGIOCY2E_7oPDPvhI3kbF2yati82E8Rp0U1XC93BK57_pTKQPfJIHJN34eW9egNXshvLNMMpZ1YrUUUqXnF_W0mcvuH37ie0T9_qT_aoLk7yJ8CL8t62f-OzDk76SM1VjMuHrUNjZ7xuYL_PkrXYAuN1I9H6txDY8omsnhR6hJ-NjiW-68ZnTMW8utRNyMAGmvVn9JMqlYmjolx7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز: جی‌دی ونس می‌گوید ایالات متحده در مذاکرات با ایران «پیشرفت زیادی» داشته و معتقد است تهران «حداقل تا حالا با حسن نیت در حال مذاکره است.»
جی‌دی ونس: خب، فکر می‌کنم گفتن دقیق اینکه رئیس‌جمهور دقیقاً چه زمانی یا اصلاً  تفاهم‌نامه را امضا خواهد کرد، سخت است. ما در حال رفت‌وآمد بر سر چند نکتهٔ زبانی هستیم.
کاملاً واضح است که به نظر من، ایرانی‌ها — آنها یک معامله می‌خواهند. آنها می‌خواهند تنگهٔ هرمز را باز کنند. ما هم می‌خواهیم تنگهٔ هرمز را باز کنیم.
🔸
چند مسئله در مورد موضوع هسته‌ای وجود دارد: ذخیرهٔ اورانیوم غنی‌شدهٔ بالا و همچنین مسئلهٔ غنی‌سازی.
پس می‌دانید، ما با آنها در حال چانه‌زنی و رفت‌وآمد هستیم. ما واقعاً فکر می‌کنیم آنها حداقل تا حالا با حسن نیت مذاکره می‌کنند.
داریم پیشرفت می‌کنیم و امیدواریم به این پیشرفت ادامه دهیم تا رئیس‌جمهور در موقعیتی قرار بگیرد که بتواند توافق را تأیید کند.
FoxNews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 427K · <a href="https://t.me/VahidOnline/75782" target="_blank">📅 01:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75781">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjByBsY-mYBHrWGwokYG4tWbbZsfSkx7DYIqWzddDX4sQpadz4yxa46RV68A9rhk1vLX9n8w7doMAQN0hEgleEAWRXbnrjPCKScxOWVJ8wj26gTFd7_CdQ8bC_RmchZaVkKvmFNC_eM--3xaKYm6SpkFLXMaLyZe9nGGT__x9Vk8FB798CJFLRJCr6nrdl4tTcFkV_zV8cfs50eD4itBMSzWAY7bJ940nIMmdlYjYdJKsbetN66MN8S8WsgxH2tZ4tdqSMKs1gKO2PlQjB7UP6fWMX-PIBy11jZEDdJQRTv5wSkJ6ceafBX0VDvuUBwZ71fEAMvr8hu1MxPkqIvMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران گزارش دادند که نیروی دریایی سپاه شامگاه پنج‌شنبه در نزدیکی تنگه هرمز به ۴ «شناور خاطی» که قصد عبور بدون هماهنگی از تنگه هرمز را داشتند، «شلیک اخطار» کرده است.
همزمان، گزارش‌های منتشرشده در رسانه‌های اجتماعی از شنیده‌شدن صدای انفجار در هرمزگان و بوشهر حکایت دارد.
@
VahidOOnLine
ساعتی پیش پیامی دریافت کرده بودم که در پست قبلی نقلش کرده بودم و الان به اینجا منتقلش کردم. پیامی از شهروندی که درباره یکی از اعضای خانواده‌اش نوشته بود: الان قشم بود. پلاک موقت دادن بهشون گفتند فقط از جزیره خارج شید سریع
همزمان با خبر بالا هم پیام‌هایی داشتم:
صدای انفجارهایی در بندر عباس شنیده میشه.
صدای انفجار داره سمت قشم و دریا میاد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 432K · <a href="https://t.me/VahidOnline/75781" target="_blank">📅 23:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75780">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g7jAeTh3qlAJJjnlBwd7VjHGThvtNcuzKwvtFDV8nbkplOL4nw4bdSohg2QCwhBa-JQeZUzFtqEDGbUmPzgdJON8Cls8UMSN_RW7l61x67cKj8yZFUdah7fxHMSfd32q26TDAlTMYBW_xGPnQk1VCK_sX8o8n3bLy2yzg1G_JnR06swybBEiZD8gq9Nh0ho0PgUolGDdrwyQqPFNSzN9zJm8EPsej9qry060kSyZXl8XyvloTjMN3I2F7pLhWkxL3b3BwYz0F0kQXIEraZDsRjHqlCjKAK0TDI0FpSfk5t2P8oP5RMvA7HKVWXYAGPThDES9dPmH4HlAVBVJg4UnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
#جم
در استان بوشهر
پیام‌های دریافتی درباره شنیده شدن صداهایی
:
▪️
همین االان 10/42دقیقه موشک از جم پرتاب شد
▪️
الان جم رو زدن...صدای انفجار زیاد ۲۲:۴۰
▪️
سلام آقا وحید
امشب ساعت ۱۰:۴۶ ۷ خرداد
بوشهر شهرستان جم نمیدونم صدای پرتاب موشک بود یا جنگنده ولی خونه ها لرزید
[معمولا این دو صدا با هم اشتباه گرفته میشن.]
▪️
درود بر وحید جان آنلاین از جم پیام میدم
حوالی ساعت 22:41 بود که فک کنم صدای فرستادن موشک یا رد شدن جت و این داستانا یهو اومد
صدای مهیب و خوبی بود
🔄
آپدیت:
مسعود تنگستانی، فرماندار جم، به خبرگزاری صدا و سیما گفت نیروهای مسلح جمهوری اسلامی «یک هواگرد» را در آسمان این شهرستان در استان بوشهر هدف قرار داده‌اند و اکنون وضعیت منطقه عادی است.
@
VahidOOnLine
یک مقام آمریکایی ادعای صداوسیمای جمهوری اسلامی درباره سرنگونی یک هواگرد آمریکا در استان بوشهر را رد کرد.
به گزارش رویترز، این مقام آمریکایی که نخواست نامش فاش شود، گفت هیچ هواگرد آمریکایی در نزدیکی بوشهر سرنگون نشده است.
@
VahidOOnLine
آپدیت: تصویر بالا
به صور رسمی هم از طریق
سنتکام
تکذیب کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 442K · <a href="https://t.me/VahidOnline/75780" target="_blank">📅 22:51 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75779">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGex9f20WyfbcremcsqnbEa1xlz1HF3uRqGensWkcaR3JFcjRHGyHKmFJH9qp3-HDTJVdflA4XmUmOIEd65QIe2G6iX1Oq1LdcRXW5XdiKUn2OGilEWLyGdGMcmSKEs4hNfuE1yYKuBhWkVqF4FcJJWhg5Fz11uPs59MyKiDXDznTRkY0c1eK9O1LH4HGwdQFQnLYSY29joQk5WeSyqNNbz_XnWqUlnORQYqyr8OONH0F_9hN8jjcpYfIU1eQDGqzu1ZDhHvhaZ6SAWAfPSGdC5k2aNTsAaWgSHqyJAuALPPLLpfB3upG7O-0VVsAxUeiOyiZdbon8-7oSDNKRpvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارگان خبری مجموعه فعالان حقوق بشر در ایران خبر داد که تارا و کیمیا داوودی، دو خواهر محبوس در زندان اوین، توسط شعبه ۱۵ دادگاه انقلاب تهران به ریاست قاضی ابوالقاسم صلواتی در مجموع به ۱۶ سال حبس محکوم شده‌اند.
براساس این گزارش، کیمیا داوودی به اتهاماتی از جمله «ارتباط با گروه‌ها و شبکه‌های معاند» و «اجتماع و تبانی علیه امنیت کشور» به ۱۰ سال زندان و تارا داوودی نیز به اتهاماتی شامل «اجتماع و تبانی علیه امنیت کشور» و «تبلیغ علیه نظام» به شش سال حبس محکوم شده است.
این دو خواهر در تاریخ ۲۴ دی‌ماه ۱۴۰۴ در جریان اعتراضات سراسری در تهران بازداشت شدند و هم‌اکنون در بند زنان زندان اوین نگهداری می‌شوند. به گفته منابع حقوق بشری، بازداشت آن‌ها با خشونت نیروهای امنیتی همراه بوده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 422K · <a href="https://t.me/VahidOnline/75779" target="_blank">📅 19:12 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75778">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWGdAeLz26KIVwd1SfClXkt4Wq33NZBOISjcKTSgW9lqi1LbTBU4DUAZLiDasbICofnNJ3JQMeag1GUJNRzbQsLEmNpaio0yf5lfhT9NPDh9w_mB_HpOCOViyo0IZrh8106RaptH1yX0tos_gdieI7lO2gpyQwuMUQwDOkxhdnlYRgJXrQZkg2z3DQbUZ9257uO7QBz75Q1vH5T9VQ7_GFDWDq4nihenCxkTB-o36PZh6Tao6a9nmD8Mrn4uwlX7YnvjUZ9KsOUsfDc1v9-2zst10OcfarLzBushe0evnGiw30qc7LsG5aLq-Uf6gKeGc7_a_DIoCOpQ9Y3ZcJwdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از مقامات آمریکایی گزارش داد که مذاکره‌کنندگان آمریکا و جمهوری اسلامی به یک یادداشت تفاهم با مدت ۶۰ روزه برای تمدید آتش‌بس و آغاز مذاکرات درباره برنامه هسته‌ای ایران رسیده‌اند، اما دونالد ترامپ، رییس‌جمهوری آمریکا، این متن را هنوز تایید نهایی نکرده است.
مقامات آمریکایی که نامشان فاش نشده به این رسانه گفتند که شرایط توافق تا سه‌شنبه تقریبا نهایی شده بود، اما هر دو طرف هنوز نیاز داشتند تایید مقامات ارشد خود را بگیرند.
مقامات آمریکایی افزودند که طرف ایرانی اعلام کرده که تاییدهای لازم را دریافت کرده و آماده امضا است.
تهران هنوز این موضوع را تایید نکرده است.
اکسیوس نوشت مذاکره‌کنندگان آمریکایی جزئیات توافق نهایی را به ترامپ گزارش دادند و او درخواست کرد چند روز برای فکر کردن زمان داشته باشد.
@
VahidOOnLine
بعدا
فاکس‌نیوز
هم خبر مشابهی منتشر کرد.
و گویا به همین دلیل هم می‌خواستند اینترنت را باز کنند. پیروزی جلوه دادن با اعلام جشن و پروپاگاندا در جو جام‌جهانی و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/75778" target="_blank">📅 19:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75776">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dBoUYARKJVI1Oj0IbTdERDoOxcOsTIKeHHQEtTBrmTZ7TXNFZ7GaJQlcfYC1i9FXTUhv8BfLd_LSnYg7dzHrFHae7ZmPbPAfsqu-X4dIAi_Z_pF6fdHO36XuYfcOjevkNmI-3QFFVUEeqqS6H8KgcJLTcHIDDsWS2vleDou7PQC-O5Rsx9wxhqufkJXXqeVJ-ilmdu_wg5yBEevyzRq2_1gp4c67k8OHXfHByO3r-MpZFWvpXaTgeElGh8Ktocpzo3xtMVSPRTDlg6HcmE_b_Q6ujU9pU5MBwyjC0SZVgLAfunmfUWzTCH7phAbSzIDT8_71Je2KSFjCb2AtmMTG0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xbq0TA5DWbDuNqsuZPTjojSophR_GG0nVOAUxPwoea3cCMZ3HO4q_0ePBNXF3CSlyGzAZoHg46tgNLyAZDmJYabLee99LwqECxmDIoe4GMsM0kBDvOF4tJfMPYfK6n1kDnF3ngNRY5ahTYBsA4CmVTQdQDU4l6cL1Rt5nueUHKW3w77bqk9zUehoUFQmcJPFX9K1M0A2tdp9r2MnXJNRU5vC4SB-xUdTHsMCIhN_OrwcOjkaUcvX9zp45lu2ziF2R2jDth3cRAatQcW2K9yx13lTCa3WhnJZiZLyUHN--qagxioITpUViE_-AAg4_gedAsqIcs9kDhyy-ami8XEESw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پس از انتشار پیامی منسوب به مجتبی خامنه‌ای درباره «نابودی اسرائیل تا ۱۵ سال آینده»، رسانه‌های ایران تصویری از دیوارنگاره جدید در میدان فلسطین تهران منتشر کردند که بر آن جمله «اسرائیل ۱۵ سال آینده را نخواهد دید» نوشته شده است.
در پیام منتسب به مجتبی خامنه‌ای که رسانه‌های ایران آن را منتشر کرده بودند، آمده است اسرائیل «به مراحل پایانی عمر منحوس خود نزدیک شده است.» در این پیام به سخنان علی خامنه‌ای در سال ۱۳۹۴ اشاره شده و تاکید شده است که اسرائیل «۲۵ سال بعد از آن تاریخ را نخواهد دید.»
@
VahidOOnLine
سپاه پاسداران روز پنجشنبه هفتم خردادماه با انتشار بیانیه‌ای به مناسبت کشته شدن محمد عوده  و عزالدین حداد، دو فرمانده حماس اعلام کرد منطقه جز با محو اسرائیل روی آرامش نمی‌بیند.
سپاه در این بیانیه از حمایت جمهوری اسلامی از «محور مقاومت» تاکید کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/75776" target="_blank">📅 19:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75774">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Nb5Tgn1ASMIDAFegvreHVaSfF18141ZwwpesIvJefl5ivQYOi7bERm4DYcUB3_kruMbrFMHtHv3M5VMonYQasAJkiKLLFIQOJLsh2XQPExRjXK158qmwiymBayiQ4qiKG0BIyOOHKRYadhODRjbMgZplti_ldddffv39I_S8phXI_kEd9Srol6NG-PgcAsgYE82UpO4wADYPxoORFzCRolJGpr4SZy_JFrbye0DGtLBzzkj4z9SBwfQiPsDpmixulPI-dnVUpf2NOI-AFIfQ1zwn4vDy88MALSyxIadMqlQj2cEJuk1NjD6VmbjLwrBtq64o9_Cg0YSb9zx_OteB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QdLvanc8H-KJWkWQrSCe9GJTCe167i9grVsYLgZHuyvnPYY0h9MbRy7ipmz2h8gvF-jXnT89YGrALW-BaTrPNSRhPaGUxQt2I4FPPomg4Urp2hCzYJJMqbMMMKI5fhoIsifLBUh-jSYdymdXp82zZMSyVmEVRxsDJg98KY2ViidwTUF0eyVmkDnlMkZuDA4JkJ3sEdLmpobvco1GyDzWCzUoPc0VVrHJU3rLANrcMCMotTzKwwfhJ7bCaElAs4QwfR_CfUYqvvzuBAi0-lo8KtzmQvhJbfCmqNp3BCgJpmlu9-HujGIa0Op3XT6l7hCAYHTy_cpEMELZWBmkvBQ--w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز پنج‌شنبه در پیامی در شبکه ایکس نوشت که ایالات متحده در راستای افزایش فشار بر تهران و باز نگه داشتن تنگه هرمز «دسترسی هر دو شرکت هواپیمایی ایرانی به اماکن فرود، سوخت‌گیری و فروش بلیت را متوقف خواهد کرد»، اما جزئیات بیشتری ارائه نداد و به نام دو شرکت اشاره نکرد.
@
VahidHeadline
اسکات بسنت، وزیر خزانه‌داری آمریکا، با تاکید بر اینکه این کشور به کارزار «خشم اقتصادی» علیه حکومت ایران ادامه می‌دهد، در شبکه ایکس نوشت نیروهای جمهوری اسلامی حقوق دریافت نمی‌کنند، پلیس‌ها سر کار حاضر نمی‌شوند و جزیره خارک تعطیل شده است و اقتصاد و ارزش پول ایران در سقوط آزاد قرار دارد.
او افزود سازمان مدیریت تنگه هرمز از سوی جمهوری اسلامی یک شوخی است و امروز وزارت خزانه‌داری آن را تحریم کرده است. ما به هر نهاد شرکتی یا دولتی درباره پرداخت عوارض یا پنهان کردن آن به‌عنوان کمک هشدار داده‌ایم.
بسنت اضافه کرد با تشکیل «دیوار فولادی»، محاصره دریایی آمریکا باعث شده میزان نفت خام ایران در دریا به پایین‌ترین سطح تاریخی برسد.
او تاکید کرد تنها یک نتیجه رضایت‌بخش در مذاکرات این روند نزولی را متوقف خواهد کرد.
@
VahidOOnLine
دولت دونالد ترامپ نهاد موسوم به «سازمان تنگه خلیج فارس» جمهوری اسلامی را تحریم کرد
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75774" target="_blank">📅 18:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75772">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/FhddKOABxvpZj5aBAmnIp4U5gkM3aaKJ9S0iTp8h6QZo0v-Tk9dqWE-pTsDHC1J_B4gdMSLwC5LNYpAybMsWkPynPS8iuer0l5GFX3KAPXIvXXV8UeWNhIOY6vSlgxCBmqQ5BMTf3Y5Id4QQYrE2OkZluAwJC4ncmrQzVq53qjTQEowfL7T4e97lvdVZrAU5uloLZWb7w8HApMueHk2UsS517iTP_0mhGXtYhfCaBKWEMj6jTQBVsnEtUj33xCPFsVCSlvY5pUmvks75V71DUUROfd3xCvKOQKzmVMBsnOcNHW527f4UD9QCrgulZWtCRFfwlMniEC1dqczWZAVYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DpRn_9W2ErfgP2kgims-zpzY2gcpApKcEj0uew6br883B-DAiVfFhDx35cQ3YGiKBzGlW855bacqn8Jtlmo4Gq7tn5ZK7V2h04u-TNhQ94VoG7ObZ2h6yxQoUaevZKd3u8Ne4FrgSEMJeEZtg98AXziBwKh7CKpZacyQ0dz9W0Oj9eVPaa80k_gSOvrA4Bh7HKXdD1tka-vuerhv77Vc032FExOcJ5sbIqIrnF1pwoIKPu8TodCTEAv5RpQcn0iD29aBTFgSZs7nd_ybv7DT70rJaYkTrduY_LMlPfMR4_dh_Vibi771bK9WtL9cMT1DLYROaYyY_xM1s58YEM2ZrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت خارجه کویت حملات اخیر موشکی و پهپادی رژیم ایران به خاک کویت را به عنوان یک تشدید تنش جدی و نقض آشکار حاکمیت و امنیت محکوم کرد.
این وزارتخانه روز پنج‌شنبه اعلام کرد که تهران را کاملاً مسئول حملات اخیر می‌داند و حکومت ایران خواست فوراً و بدون قید و شرط حملات را متوقف کند.
@
VahidHeadline
اسماعیل بقائی سخنگوی وزارت خارجه ایران، حمله بامداد پنج‌شنبه آمریکا به مناطقی در بندرعباس، را «تجاوز» نامید و آن را محکوم کرد.
آقای بقائی این حمله را «نقض فاحش حقوق بین‌الملل و منشور ملل متحد» دانست و افزود: «شورای امنیت سازمان ملل موظف به ایفای مسئولیت قانونی خود برای پاسخگو کردن متجاوزان آمریکایی است.»
سخنگوی وزارت خارجه ایران می‌گوید آمریکا «به‌طور مستمر»، آتش‌بس میان دو کشور را که از ۱۹ فروردین اجرایی شده، «نقض» می‌کند.
سنتکام با این حال تأکید کرده که این اقدامات «سنجیده، صرفاً دفاعی و با هدف حفظ آتش‌بس» انجام شد. این دومین بار در سه روز گذشته بود که آمریکا اهدافی را در ایران هدف حمله قرار داد.
@
VahidHeadline
فرماندهی مرکزی ارتش ایالات متحده، سنتکام، حمله موشکی ایران به کویت را «نفض فاحش» آتش‌بس خوانده است.
این نهاد در حساب رسمی خود در شبکه ایکس نوشته است: «ساعت ۱۰:۱۷ شب به وقت شرق آمریکا در تاریخ ۲۷ مه، ایران یک موشک بالستیک به سمت کویت شلیک کرد که با موفقیت توسط نیروهای کویتی رهگیری شد.»
سنتکام نوشته است «این نقض فاحش آتش‌بس توسط رژیم ایران، ساعاتی پس از آن رخ داد که نیروهای ایرانی پنج پهپاد تهاجمی یک‌طرفه را شلیک کردند که تهدیدی آشکار در تنگه هرمز و نزدیکی آن ایجاد کردند.»
فرماندهی مرکزی ارتش آمریکا می‌گوید: «تمام پهپادها با موفقیت توسط نیروهای آمریکایی رهگیری شدند و آنها همچنین از پرتاب ششمین پهپاد از یک سایت کنترل زمینی ایران در بندرعباس جلوگیری کردند.»
سنتکام در ادامه آورده است: «فرماندهی مرکزی ایالات متحده و شرکای منطقه‌ای کماکان هوشیار و محتاط هستند و ما همچنان به دفاع از نیروها و منافع خود در برابر تجاوز توجیه‌ناپذیر ایران ادامه می‌دهیم.»
@
VahidOOnLine
وزارت خارجه عربستان سعودی در بیانیه‌ای در شبکه ایکس، حملات خصمانه با موشک و پهپاد به کویت را به‌شدت محکوم و تقبیح کرد.
@
VahidOOnLine
وزارت خارجه قطر در بیانیه‌ای هدف قرار گرفتن کویت با موشک و پهپاد را به‌شدت محکوم کرد و آن را «نقض آشکار حاکمیت» این کشور و «نقض فاحش قوانین بین‌المللی» دانست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/75772" target="_blank">📅 18:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75771">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7Q56e9JoyUBmi-vjSlad4l4d1BsjKf4rsGFimSLdi82ZaK3LgNFpM-nkZ6xXfGqX8Oa22LFx-jDB7D6_OWPU4hsFQPhxJEWBfvDxbnkSSyU98KGnluG_up7wWDLpz7XrjXwtJSTvCCLB76y00LK6TSKp-QaGqGKfe_coPP6-oUJSRQEmpia0qJ9AGRGSN1_elzC6HXtpY2mQ0hocxk_5og6469zr6j-KQzxSHTK7KYetAr9GTnRc6HRDe0QKRCHDnCG_r4bHIzI9DmTv_RD3NDIe6HopivMuhNZDRG1jtLfRb-wDv6PuYcoiWMk4P7PevCeZMIKbUVirbK_jg5XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران پیامی منسوب به مجتبی خامنه‌ای، رهبر جمهوری اسلامی، را خطاب به نمایندگان مجلس شورای اسلامی منتشر کردند که در آن می‌گوید «ایجاد تفرقه و تجزیه اجتماعی»، در کنار جنگ و فشار اقتصادی و محاصره، «طرح و نقشهٔ کور دشمن» است.
مجتبی خامنه‌ای در این پیام که روز پنجشنبه هفتم خرداد منتشر شد، همچنین به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داد که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
وزارت اطلاعات جمهوری اسلامی روز گذشته در بیانیه‌ای هشدار داد که بعد از جنگ اخیر، «برخی کمبودها و گرانی‌ها» در پی فشارهای اقتصادی آمریکا می‌تواند باعث بروز ناآرامی‌های تازه در ایران شود.
وال‌استریت جورنال نیز روز پنجشنبه در گزارشی به نقل از تحلیلگران هشدار داد که ادامهٔ محاصرهٔ دریایی آمریکا علیه ایران که به کاهش ذخایر ارزی ایران انجامیده، می‌تواند احتمال بروز اعتراضات جدید در ایران را افزایش دهد.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 285K · <a href="https://t.me/VahidOnline/75771" target="_blank">📅 18:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75770">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHHaxw_mvzcItf3-AtwRY53UmR5l9bk-86g_RnC6pPzPhhSVxOEj3sEiZEUvOVr7V3QssLmX6GguCGSWw2y0hc_2DV-h3Va3_Nt3o7E3G7OwzDaPK4DYqeN1ahYod5ZLVQWBDU_FfxgWrqRV_varpZKXQsfSzievBUMeX0pwQMHAAHU8aU-NJOK5iApRHISvUhAOvHW5XKoIU66NqaYiWr3YfeM3ABJtvdsftkDfFvn0QZmNsrWwFMee00-VizUNBEYucx2Pap-gO13PnE_Fra5CNG2ZVcI4heWr4wCRatRnghnH20G9BLwRUBC0fR6pK8sKcOK-fb0pBqpWjf9xZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دادگستری آمریکا اعلام کرد «جاناتان لودهولت»، شهروند آمریکایی ساکن استاتن آیلند، به‌دلیل مشارکت در طرح «تعقیب و قتل» مسیح علی‌نژاد، فعال سیاسی ایرانی-آمریکایی، به ۱۰ سال زندان و سه سال آزادی تحت نظارت محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75770" target="_blank">📅 18:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75769">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/shsDTKQCF955VlNI6jJFNcFq8lBg2qtjuRv8uRjZLt0cvyV5iuv10wKuvkBHZrn_ct3UdFCpRhMna58Yw5X0QVf7nOhaTTEDKTQcEatB8Obpd-AM3uXd8Q8jZhoypwPJmO4lSS5FrD3kQMhXIrGI7OvpzTEbpkiVcSDHnpqwsbkxBMVxMGZZJkOkNSSbY7tnNQgzkV65unEwHgSU4UTRJrJ4naxKmGkprwe8zsGnsnvoRnwi09OXS6LkAZP_QRR2pNCtUy8UF0EQQnie1KLz7eMWKkLEL1DT3wn-HZMO9p670om_rmhvukeFlw3-Q_2k-iMDYvgD-YDv0jfGkjKGcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محمدباقر قالیباف»، رییس مجلس شورای اسلامی، در پیامی به «غلامحسین محسنی اژه‌ای»، رییس قوه قضاییه نوشت: «قوه قضاییه زیر بمباران و تهدید دشمنان دست از صیانت از حقوق مردم و برخورد با قاتلان داخلی و خائنین به ملت نکشید و خوش درخشید.»
این تمجید از عملکرد قوه قضاییه درحالی صورت گرفته که در طول روزهایی که از جنگ ایران با آمریکا و اسراییل می‌گذرد دستکم ۳۹زندانی سیاسی اعدام شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75769" target="_blank">📅 18:41 · 07 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
