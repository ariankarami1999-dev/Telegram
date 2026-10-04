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
<img src="https://cdn1.telesco.pe/file/ZAb6z4v4ZUkistZL6sKigunHswpYXFiilNZo9srQ2SUhjogc3X2s04ZyJMquGbeVSYqkt4mGC9BUy4MV-FApTi-FqoyULwP5Xxr0IVgKJ5VZb6pRyf6Ubja3eMnmFVk9hTd_QOChCz717iI54a3G1q-Iic1NvB3HtIgZngx_LnXMPQ1RK1IueAWdZflhJwlgpWj5T__vVNQLOo6wSIc5EZu-cIGxDGDYM-Yv6JzQAlscKgSY3ED85LA_YiB-0t9LT_p9JRsUEb3l4m0ORpLoWPCTtfYgoqguBPJq1CGOAi-hE9fixTpisSj_w9HQJhGhWCzu3PfmH4f2NXrZgXeoVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.39M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-12 03:45:05</div>
<hr>

<div class="tg-post" id="msg-78614">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YSo8wXgmiD_DKHHppD84Jt0HrsUdTwtP9XeL-b_KJeSV0eF8SMMjuASyp1Qs2hnWa0zPhFyz13ZQX7u5e0O6RhcArKBnDrhWekk8l289Njvjqxy3zhh-iLLNI1_7b4Ndg_JWUFkLN8Qr0AnDSRn_AhTlDQi0YsBhX7SDGs9CtQaDxJkdev3UEk9BsouSwt0a614F56pTADMntrpDDqDJecaz2uLH84lKhk2paHWBah2AZ-lEidO_5pQUZZKQnike0hKQKBxtMysNt0yekwGuYUH8wdjDqGpaennRlRLH2HG-iowKHbfuzgkpUxGgrhodvJRUHa5c2OlOw1cG1_4SLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس روز شنبه یازدهم مهر از شنیده شدن صدای انفجار در تنگه هرمز و هدف گرفته شدن یک کشتی تجاری در مسیر عمان خبر داد.
فارس مدعی شد، نفتکش «اور وینست» که تحت اسکورت آمریکا قرار دارد، هنگام ورود به تنگه هرمز سامانه رهگیری خود را خاموش کرده بود. این خبرگزاری دولتی نوشت، این دومین هدف‌گیری یک نفتکش در تنگه هرمز در روز شنبه است.
این خبر پس از آن منتشر شد که خبرگزاری مهر ساعتی پیش از شنیده شدن صدای انفجارهایی از سمت دریا در جزیره قشم خبر داده بود و احتمال ارتباط این صداها با شلیک به «کشتی‌های متخلف در تنگه هرمز» را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78614" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78613">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dttyhy1WW86Vvqo3snbp6RR1JBmHKXN9gLJykcgRhjvKdEDZjJOt4irKVixua7XzhQVcGRBauouX3ztXKymb95iMLuVZdAU4qHnOp7yFrqurAydIkqab9anG6ZXuFRv2aEj5SL6ySfaWd_MPF8Q8udRnBobHPxUrlLxZUvLLoTMUHzqHyZ9bqojU70yaS5mN2A-gACoMM5h-fluHf6a78tGHJbRCM2TTQDI5tWlwabtw5oW3pEwMhezOXfkhyuIR4JkAbfDDs6jtFaAAxAmbHwFC-DP3CgXo5DcCSO3swEilys5DgP3BiQScouqNP4q8eQxgHQRn6gPo3XH02z7nkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی انتشار گزارش‌هایی از شنیده‌شدن صدای چند انفجار در جزیره قشم در عصر شنبه ۱۱ مهرماه، خبرگزاری مهر نوشت این صداها مرتبط با اقداماتی در خلیج فارس و تنگه هرمز است.
این خبرگزاری بدون استناد به منابع رسمی نوشت «هیچ اصابت یا حادثه امنیتی در پهنه سرزمینی جزیره» رخ نداده است.
خبرگزاری مهر در عین حال این «احتمال» را مطرح کرد که صداهای انفجار شاید به «شلیک به کشتی‌ها» در تنگه هرمز مرتبط باشد.
این در حالی است که همزمان، تصاویر متعدد و گزارش‌هایی در شبکه‌های اجتماعی منتشر شده که یک قطعه بزرگ و استوانه‌ای‌شکل را در محدوده‌ای شهری در قشم نشان می‌دهد که ظاهر آن به بخشی از یک پرتابه نظامی-دفاعی شبیه است.
گزارش‌های تأییدنشدهٔ دیگری در شبکه‌های اجتماعی نیز حاکی است که پیش از سقوط این قطعه، صدای عملیات پدافندی و چند انفجار در قشم به گوش رسیده است.
مقام‌های رسمی تاکنون توضیحی دربارهٔ تصاویر منتشرشده و این حادثه در قشم ارائه نکرده‌اند و رادیوفردا نمی‌تواند جزئیات گزارش‌های منتشرشده را به‌طور مستقل تأیید کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 212K · <a href="https://t.me/VahidOnline/78613" target="_blank">📅 20:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78612">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HBJy0zuyk-V3zr6tiXY2K5OSrNb8tFiF4WyCexE4WXwh3JPxWDkEkg3prNGijkWUheKXpjB_BEoinzadhvAdx7tG0i64Fgo_eRYzxPknVG-0qbxUlT0cXJB3dtcs3X8GDqr72CzjX2X00QDTTUhGnvzRWMszhpimLDjOmnin60fyq5i5yXniO8DMU5xR8mlh-Z8JSLB9GFaGWQPgPh26xnmfUMWGlUrIXsiKwb6kJwQYetNpj6o1J76_pJwmWsMmiAJ66HkIX44WRYa8ZsnY_snWCXmo-tlSlYpxSgaMCzve_iHSYsS04wMrwL08dmyqF51Bv1TnVjj4FZH5aKCGNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی از قشم  حدود ساعت ۱۶:۳۰:  صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم  همین الان قشم موشک شلیک کردن  16:34 دقیقه   وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن صداش خیلی وحشتناک بود معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد…</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78612" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78611">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oewGvFJswtZ2peG75QoB4P79MohA8PxBBG4HPMuZLKcsmG10R46tsvdNbVcW50rsUR4loKca-6mVK0U19jTPmdC0czzz21ysAAIP3peDDSHsgYZMXvbbRpPTcs1iwkDNPpN_xHRepxnEw63VVId7lt04xuuWOHWBhruRMaqTygNtrHi_EcRUjGTchrRViMaOP1Iol864fOYor7HppauznqaAvtCrMq9AWto12PXx3zHp6B1z2kawWnmE0alOhRRTHC6hQDRrattQp3eS7-QgCQ0fF8hnnqPzHAUPbdWqhBcswdcBSiAbIAiehyw50LpTDAfBTZctmGWRuI43KnSMVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند کاهش ارزش پول ملی ایران روز شنبه ۱۱ مهر ادامه یافت و بهای دلار آمریکا در بازار آزاد برای نخستین بار از مرز ۲۷۰ هزار تومان عبور کرد.
بر اساس نرخ‌های اعلام‌شده در ظهر شنبه، قیمت فروش دلار به حدود ۲۷۱ هزار تومان و یورو به بیش از ۳۰۵ هزار تومان رسید.
این در حالی است که روز پنج‌شنبه قیمت دلار در بازار آزاد حدود ۲۵۸ هزار تومان گزارش شده بود؛ به این ترتیب بهای دلار در فاصله دو روز بیش از ۱۳ هزار تومان، معادل حدود پنج درصد، افزایش یافته است.
افزایش قیمت ارزهای خارجی در حالی ادامه دارد که بانک مرکزی جمهوری اسلامی روز چهارشنبه از برنامه‌ریزی برای عرضهٔ دو میلیارد دلار اسکناس به بازار خبر داده بود.
قوه قضاییه نیز از برخورد با کانال‌ها و صفحاتی که آن‌ها را عامل «قیمت‌گذاری کاذب ارز» می‌خواند، خبر داده است.
اقتصاد ایران همزمان زیر فشار جنگ با آمریکا، تحریم‌ها و محدودیت‌های فزاینده بر تجارت خارجی ناشی از محاصره دریایی قرار دارد.
ارزش پول ملی ایران، از ۲۳ تیر، زمان آغاز محاصره دریایی آمریکا علیه ایران، تاکنون بیش از ۳۱ درصد کاهش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78611" target="_blank">📅 17:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYdNW93GrLt6YQNzJJOk7YohwJEAkvQoz9oejofSrqMv-8LqzWis5LtRYvx7FZKb-PfbxoVIIFTVR_tYk8gmoO5OJPAEGRCB_mMv5RYkuWqXTncATskSeQPAxfa-PhFX85SD5QBgcSMWjzCANgmd95KlJXeX0TzQAzUp0mrC01veL4F9J-aPpDrjzT9jh3A0FIJW4bQkcfyzJNTj6vmGMm6GJnZi275dilEeKgNrZ_XHByHLZCgf_Wd2LLP6UhkwxGaEL-sQzw-y2h8Li_6x3e8GPLGok8ZZ_08WGCcUVGYPNcdPcymo7vE7kt_S3oQYliyKVqgRlMQrt4GaJ3mTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا در گفتگو با رسانه آکسیوس،‌ با تاکید بر تاثیربخشی محاصره دریایی ایران اعلام کرد، ایران برای نخستین بار از زمان آغاز صادرات نفت، در هفته جاری هیچ نفتی برای بارگیری و انتقال از طریق دریا نخواهد داشت.
او همچنین با اشاره به کم اثر شدن نفود نیروهای مسلح جمهوری اسلامی در تنگه هرمز افزود، آمریکا عبور ۱.۱ میلیارد بشکه نفت از را از این آبراهه تسهیل کرده است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال منزوی کردن ایران «به شکلی بی‌سابقه» است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 221K · <a href="https://t.me/VahidOnline/78610" target="_blank">📅 17:44 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY68-b_WMzTMlF5LKWOSOM3yzXh9mc5gf2gXIPqAVOv6Ofr8dsmQHTr9nWF3k2LZ5_r8a6Z48aEWu9lEcaKIl8qlKauPbNJKZhBR6r7Nu2Ntj8iM-g5GFaVjDUogIoK7InhJoxXKYazrmjwdew5VE4mlHdjjPE91xfgd6wG1pLd5iHPbWRaTPTFyBOjqGv59qYlfFYfq8jY7UeO9PxrWgu3mJYj7PEeu5VN_S8LZJQu50ZurqUqT68tTwZUPy1sLPG6Im1vNA9FtxrUt12EPIOeBhiEXafI4J0Bpuk7fGz5aQfuoriZ4bGtqmw9b_no5zSbvpaROHhCSUNelAwt5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس مبارزه با تروریسم بریتانیا دو تبعه ایران را به برنامه‌ریزی برای حمله‌ای تروریستی علیه جامعه یهودیان منچستر متهم کرده است.
پلیس بریتانیا روز جمعه ۱۰ مهر ۱۴۰۵ این دو نفر را «سلام احمدیان»، ۳۶ ساله و ساکن لیورپول، و «رحمان صالحی»، ۳۴ ساله و ساکن سالفورد، معرفی کرد.
این دو نفر روز یکشنبه ۲۹ شهریور در منچستر بازداشت شدند و روز جمعه به اتهام انجام اقداماتی در راستای تدارک عملیات تروریستی تفهیم اتهام شدند.
قرار است احمدیان و صالحی روز شنبه ۱۱ مهر ۱۴۰۵ در دادگاه حاضر شوند.
پلیس می‌گوید این دو نفر برای پیشبرد توطئه ادعایی خود با فرد سومی در خارج از بریتانیا، که احتمالا در ایران حضور دارد، در تماس بوده‌اند.
به گفته پلیس، احمدیان و صالحی از طریق پیام‌رسان‌های رمزگذاری‌شده با این فرد درباره تهیه قطعات لازم برای ساخت یک بمب دست‌ساز گفت‌وگو کرده‌اند.
این دو نفر همچنین متهم شده‌اند که فایل‌های ویدیویی آموزش ساخت و مونتاژ بمب دریافت کرده، مایعات و تجهیزات مورد نیاز را تهیه کرده و برای شناسایی و بررسی اهداف احتمالی حمله از اینترنت استفاده کرده‌اند.
«ویکی ایوانز»، معاون دستیار کمیسر و هماهنگ‌کننده ارشد پلیس مبارزه با تروریسم بریتانیا، گفت این بازداشت‌ها نتیجه تحقیقات مشترک پلیس مبارزه با تروریسم و نهادهای امنیتی بوده و به خنثی‌شدن توطئه‌ای علیه جامعه یهودیان منچستر منجر شده است.
او اتهام‌های مطرح‌شده در این پرونده را «بسیار جدی» توصیف کرد.
این توطئه ادعایی هم‌زمان با اعیاد مقدس یهودیان، سالگرد حمله تروریستی سال گذشته به کنیسه «هیتون‌ پارک» و افزایش گزارش‌ها درباره حوادث یهو‌دستیزانه در سراسر بریتانیا خنثی شده است.
دولت بریتانیا دو روز پیش از اعلام این اتهام‌ها، جمهوری اسلامی را به دست داشتن در تلاش برای خرابکاری در پایگاه نیروی هوایی سلطنتی «فیرفورد» متهم کرده بود.
«دونالد ترامپ»، رییس‌جمهوری آمریکا، روز چهارشنبه ۸ مهر ۱۴۰۵ در پاسخ به پرسشی درباره نقش ادعایی جمهوری اسلامی در حادثه امنیتی اطراف این پایگاه گفت واشینگتن در حال بررسی موضوع است.
پایگاه فیرفورد پیشتر در اختیار نیروهای آمریکایی برای انجام حملات علیه مواضع جمهوری اسلامی قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 208K · <a href="https://t.me/VahidOnline/78609" target="_blank">📅 17:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78607">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JHEPPSPPSCzeUpZnE1i691Rf07_38i_QA4wuI-CakXyfgx2Hkp73RIOvieUxO63Ufx69bO2NFw3qJBK0sGedhDBlBM65iIGWraJyH0BH14I4dqvUkO8rpjeRsp-IsU3L7qIF75O4UHQI0EIryLhh-v4UiZ6dj3N0OUo5uUxnJ7Osy09bp-UsR7_ncWoC3CdHt7yocWtzzj1EC1kDH7yU5uks7YWKC41hqjKM3-b_M72AUyCsjC0b0yM56ZW3n5VaZ1VTEslZv8TqOKAt6GxG4pmfvAm1x60BkYmVKWDd1OBumLFvLQwhh_qT6snTw2YL82G-MY6SgyqTAVuJPx2BQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XdUmT4MNNGJvMgT_IyyaP8dG4lNSJU5FSeO3gCuI3XoJpMj7DPrRTm9-XwVdk9EK8NY-1dJRjZmMysD27qxhuQJrb-6ozUVhc3IgAvxJXM7I_40WQ19Ij7mSWaihOrL4dQBJka2Qc4SjNSxvDYjRVxE9sasHs9AhkopVTvY6AkA1TGVKuDAZ8wA_K8DdZBK_Fu74Y5JH892GQAfsdvrTXF-yXti81L_-pMuWguEBL8TUHVAtFlWUOpe_OuzTIMvEGK0oDBLLJ1lW2uJgLVtiaIx8fsQXHOozhkAS8SZBf0m8rkCDepPI9iWUnco2DQ_dFgf5aQR8Gs0iE-n4a0bOug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو: جمهوری اسلامی سقوط خواهد کرد و «روز آزادی» مردم ایران فرا خواهد رسید
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مصاحبه‌ای اختصاصی با روزنامه دیلی‌میل که روز شنبه ۱۱ مهر منتشر شد، گفت که به اعتقاد او جمهوری اسلامی «سقوط خواهد کرد» و خطاب به مخالفان حکومت ایران گفت: «ایمان خود را از دست ندهید، روز آزادی شما فرا خواهد رسید.»
نتانیاهو در این گفتگو مدعی شد حکومت جمهوری اسلامی ایران در شرایط کنونی «بسیار ضعیف» شده و گفت محاصره آمریکا به رهبری دونالد ترامپ، سپاه پاسداران را به‌شدت تضعیف کرده است. او در عین حال تاکید کرد که سقوط حکومت ممکن است زمان ببرد.
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت اسرائیل با همکاری آمریکا، مانع دستیابی ایران به سلاح هسته‌ای شده است. نتانیاهو گفت: «اگر ایران اکنون سلاح هسته‌ای داشت، چه اتفاقی می‌افتاد؟» و افزود که جمهوری اسلامی همزمان در حال توسعه موشک‌های دوربرد است.
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، با انتقاد از سیاست دولت‌های غربی و به‌ویژه بریتانیا گفت آنها انتقادهای خود را بر اسرائیل متمرکز کرده‌اند، در حالی که به گفته او، تهدید جمهوری اسلامی و نیروهای نیابتی آن را نادیده می‌گیرند.
او خطاب به معترضان در بریتانیا پرسید چرا به جای اسرائیل، مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنند.
نتانیاهو گفت: «چیزی که به مردم بریتانیا می‌گویم این است: کجا هستید؟ کسانی که علیه ما اعتراض می‌کنند، چرا مقابل سفارت جمهوری اسلامی اعتراض نمی‌کنید؟ چرا تمام زهر دولت بریتانیا متوجه آنها نمی‌شود؟»
او افزود: «چرا علیه جمهوری اسلامی جهت‌گیری نمی‌شود؟ چرا علیه نیروهای نیابتی آن نیست؟»
نخست‌وزیر اسرائیل همچنین دولت‌های غربی را متهم کرد که تهدید جمهوری اسلامی را به رسمیت نمی‌شناسند و گفت: «این حکومتی در ایران است که ده‌ها هزار نفر از شهروندان خود را کشته یا مجروح کرده است.»
او افزود جمهوری اسلامی اقتصاد غرب، منابع انرژی و آبراه‌های بین‌المللی را «خفه» می‌کند اما موج خشمی را که علیه اسرائیل وجود دارد، متوجه جمهوری اسلامی نمی‌بیند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/78607" target="_blank">📅 17:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78606">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLrh-GYkbvOtOMd7KeP1Mn5FSao7QR60yxDPkCAWiWE-ORygHaVwEFtv7Fnz_WQ7c5kCW-kps_-k0lekPXLUtlthVS-JKQ7jTTslpHqClQNKOyVA3WH5KU3hhthVWX5md3JJiNX8zAIT_RmpzS7AxmCWlgJOjXNdORQlLkoiArUT4K4pbAD2XGcX8so5f8BOjQgGmjmdFm_OIcLrvlo0HzdSuK9Fcz7FgjP4_EVrZbqb3WkEQjgbkVpH2Qu-pRYqdx1x3u5hfiLzaiqegWSrUBNmDooyTTcZae0ufZq8LvzzhT66aVWXXuWp6KeqOaOzTnF6nVEh5AKIdhbyzrQPFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تیراندازی مقابل ساختمان دادگستری مهاباد در روز شنبه ۱۱ مهر، یک نفر کشته و چهار نفر زخمی شدند.
امیررضا رسولیان، فرمانده انتظامی مهاباد، اعلام کردە  این تیراندازی مقابل در دادگستری این شهرستان رخ داده و در جریان آن یک نفر کشتە  و چهار نفر زخمی شده‌اند.
یک منبع مطلع به ایران‌وایر گفت فرد مهاجم که چند سال پیش فرزندش را از دست داده اعضای خانواده فردی را که او مسئول قتل فرزندش می‌دانسته و در حال حاضر به عنوان متهم در زندان تحمل حبس می‌کند هدف تیراندازی قرار داده است.
به گفته این منبع، مهاجم پس از تیراندازی توسط مأموران انتظامی در محل بازداشت شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/78606" target="_blank">📅 17:38 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78605">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1v2HQdzeGA5-j_KT2eyx_q9B78cIgNRZVcdLCs6woemq9qAiHlxjywXPolvqnYSOMsWMSBQ5HDGufbbICnHzZTw3I-wNddF1VTjJN7-Mt0UXZ-zkT4v-biZY4pYcPJOH_hSk2NpFN2AOBeXwLwtwBJbKDM7KDwf1yj9kQcRTHDTHkiLa-P3dcm6-iywjCx0CTxZJanDIgbrFLvBap8E4MvG2L7D9dr1ybSmONRX-czlGsWAoK3L1b_s1MisT66vZNhs-VclzFtu6sZ8T6l7wcl-Dg5y_Q2aAl-sm6l77D8S1iWh34Cda8kfcjjS3NOkEeMxuGwUwRwyFSc8QFhvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی روز شنبه ۱۱ مهر از بازداشت ۳۱ نفر در شهرستان سیرجان در استان کرمان خبر داد و آنها را اعضای چهار «شبکه سازمان‌یافته خرابکاری خیابانی» معرفی کرد.
این وزارتخانه مدتی شد افراد بازداشت‌شده برای شرکت در «فراخوان‌های سراسری» سازماندهی شده و در حال تهیه کوکتل مولوتف و ابزار تخریب دوربین‌های شهری بوده‌اند.
وزارت اطلاعات همچنین این افراد را به دست داشتن در «آتش‌زدن فرمانداری، تخریب بانک‌ها و ساختمان‌های دولتی و حمله به مقر پلیس» در جریان رویدادهای دی‌ماه ۱۴۰۴ متهم کرد؛ رویدادهایی که در اطلاعیه این وزارتخانه از آنها با عنوان «کودتا» یاد شده است.
در این اطلاعیه جزئیاتی درباره هویت بازداشت‌شدگان یا مستندات مربوط به اتهام‌های مطرح‌شده ارائه نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/78605" target="_blank">📅 17:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78604">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HX4EF61WE1CxMPAiBce0x0hfwJE-QtrV1PZdWdyErOF8soe_LUbOTUjNImdAVg1bS30o1lNo3FyfJWhKbQsGfIpzOo7qwEXD0FeJUR7AtniUny2Kt7GsC3mOmVIjgUAjMtvQiZ-g9kkLgMP29_EczzKhw18sKkblYxsCDscVh04ctAO-TipGR19dxjaFQA18FlL3i9G794t1dt8U-u_5eGkmkfsdAtYOkGm_xJyjPIDM-cIZ10JbfgWf2A5s29K2Pd9pL7jQyMtWh8xmSI1DTwzlHLpWfhlfYwkUOgLIgOT0B4MNVVVG6sZf51zFRBuwW6RSE9PAP5jn-ITh7IhWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه جمهوری اسلامی از اجرای حکم اعدام «سیاوش جمشیدی خیرآبادی»، از بازداشت‌شدگان اعتراضات سراسری دی۱۴۰۴، در بامداد شنبه ۱۱مهر۱۴۰۵ خبر داد.
قوه قضاییه همچنین ادعا کرده است که جمشیدی خیرآبادی شامگاه ۱۸ دی ۱۴۰۴ در خیابان ناصرخسرو شهرکرد به‌سوی ماموران تیراندازی کرده و سپس از محل گریخته است. براساس این روایت، او دو روز بعد، ۲۰ دی ۱۴۰۴، درحالی‌که یک قبضه سلاح کمری همراه داشت، بازداشت شد.
در اطلاعیه قوه قضاییه آمده است که حکم اعدام این معترض پس از تایید در دیوان عالی کشور اجرا شد. بااین‌حال، در این اطلاعیه توضیحی درباره زمان برگزاری دادگاه، روند دادرسی و دسترسی او به وکیل منتخب ارایه نشده است.
مقامات جمهوری اسلامی معترضان دی‌ماه ۱۴۰۴ را «کودتاگر» خوانده و آن‌ها را به ارتباط با آمریکا و اسراییل و تلاش برای ایجاد ناامنی متهم می‌کنند.
«مسعود پزشکیان»، رییس‌ دولت جمهوری اسلامی، نیز در سخنرانی اخیر خود در مجمع عمومی سازمان ملل مدعی شد که مردم ایران طی هفت ماه گذشته برای «دفاع از ایران» در خیابان‌ها حضور داشته‌اند.
او معترضان را افرادی توصیف کرد که به ادعای او، آمریکا و اسرائیل آن‌ها را «تهییج» و مسلح کرده بودند تا در داخل کشور ناامنی ایجاد کنند.
صدور و اجرای بسیاری از احکام سنگین علیه معترضان دی ماه از جمله احکام اعدام ذیل قوانین «تشدید مجازات جاسوسی» صورت می‌گیرد که از منظر حقوق‌دانان و فعالان حقوق بشر شامل موارد جدی‌ نقض حقوق متهم است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 193K · <a href="https://t.me/VahidOnline/78604" target="_blank">📅 17:32 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78603">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">پیام‌های دریافتی از قشم
حدود ساعت ۱۶:۳۰:
صدای جنگنده خیلی نزدیک اومد صدا زیاد قشم
همین الان قشم موشک شلیک کردن
16:34 دقیقه
وحید جان از قشم سمت اسکله بهمن موشک شلیک کردن
صداش خیلی وحشتناک بود
معلوم نیست شلیک کردن یا جنگنده بود ولی هرچی بود صداش خیلی زیاد بوددددد
قشم همین الان یه صدایی شد
سلام وحید جان چند دقیقه پیش یک موشک به سمت تنگه شلیک شد.
سلام وحید
دور و ور ساعت ۴:۳۰ جنگنده رد شد
سلام ساعت چهارو نیم بعداز ظهر امروز قشم  صدای جنگنده امد خیلی وحشتناک بود
[این پیام متفاوت هم بود که نمی‌د.ونم چقدر درسته. بعد از یک ساعت معلوم نشد صدای چی بود.]
قشم پدافند بالا نریمان و زدن
وحید
خیلی شدید بود صدا ها
معلوم نبود چی بود
رادار تازه ۳ روز بود درست کرده بودن
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/78603" target="_blank">📅 17:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78602">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=ZtjBqCKhP0cE_VOTrTGrqNtHxTCW6QEiJyhZZMRpUuWsz3tq-jISJSawSKC2t6uVMjvCmyjRg8rzcxaDecQJb0AT69vlKhPJahobrFcsSr91sD17feRBhRjIkIYS-qIrktgrQUdo5aR5uTaLmaEssWip4P6GK8wwYJhQG7AJNWr2yglX_gSprMjSoMPUbMXUkAdA2t9WRROwZAjSVapUv3jGHitW1b0DNxRU78ZSHVgJike2tQnRV-0eaRUn8z5TlGCy9YTUebAasPURxw0iXLh9Yhe3CLTGc7p-9nfHx_9TPbPT9FpXYRsUyXRE0Ix60PFxjxCI4kPUhbxtDXfBZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/742b2ddd5c.mp4?token=ZtjBqCKhP0cE_VOTrTGrqNtHxTCW6QEiJyhZZMRpUuWsz3tq-jISJSawSKC2t6uVMjvCmyjRg8rzcxaDecQJb0AT69vlKhPJahobrFcsSr91sD17feRBhRjIkIYS-qIrktgrQUdo5aR5uTaLmaEssWip4P6GK8wwYJhQG7AJNWr2yglX_gSprMjSoMPUbMXUkAdA2t9WRROwZAjSVapUv3jGHitW1b0DNxRU78ZSHVgJike2tQnRV-0eaRUn8z5TlGCy9YTUebAasPURxw0iXLh9Yhe3CLTGc7p-9nfHx_9TPbPT9FpXYRsUyXRE0Ix60PFxjxCI4kPUhbxtDXfBZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، روز جمعه، در سخنرانی خود در آلاباما با اشاره به ضربات نظامی به ایران و انتقاد از برخی رسانه‌ها گفت:  آنها نمی‌خواهند موفقیت ما را ببینند. وقتی نیروی دریایی‌شان را منهدم کردیم، نیروی هوایی‌شان را از بین بردیم و چند ماه پیش ضربه‌ای مهلک به ایران زدیم، نیویورک‌تایمز و رسانه‌های جعلی می‌‌گفتند اوضاع ایران فوق‌العاده است. آنها همه‌چیزشان را از دست داده‌اند، از جمله رهبرانشان را.
او با تاکید بر خلأ رهبری در جمهوری اسلامی افزود: آن‌ها یک دور از رهبرانشان را از دست دادند، بعد دور دیگری را، و سپس نیمی از دسته سوم را. حتی یک دور رقابت راه انداختند که ببینند چه کسی حاضر است رهبر شود، اما هیچ شرکت‌کننده‌ای نبود و همه می‌گفتند من نمی‌خواهم.
بخشی از مشکل ما اکنون این است که اصلا نمی‌دانم باید با چه کسی طرف شوم. هیچ‌کس حاضر نیست رهبر باشد.
می‌گویم در ایران با چه کسی باید حرف بزنم؟ اما هیچ‌کس آن اطراف نیست.
در می‌زنیم، تق‌تق، ولی کسی در خانه نیست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/78602" target="_blank">📅 05:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78600">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IP6xvuQnz6NTGoWA7K9S_SVw5TX2NltOoQ6QFXeXBj4HMf46-XFErgIHAnueC-CcMDrHon0vAoU4Rm7HHp3ZVb57pK6CNwJo74APMILfqYwptVnRrVxMujgcR2P7filDTIerATnNrMadWOLOWw8R811ADxe4wrWyufujbHOVmEGgFVaapfgXsUlBVwiGocCO5WlTXHFyM2lljzB2KpTleLQXgGyawm2AuzZ2JFlejO7--OIV3Sx0Y1S7DX16NF_cgsfW3Q3y605WU1RY9hnx8NyYiXTJNIxH1e3lc7oPELZMGf9SC0Ue4ciOfFTB8RyTgKpVUV97W91ea3Zlph0K2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dtu1xyszdG8fNfzDRKHTXvFd0MgHwqtUXqqRaPosaXa8zPPQXHHDqGr07pyr6SKt9QyypX_MBGgJjqOSCG1BpNvAv_iD2KqCoS_3AFL9oN5RlD5ATtPCbnwKlfK6LGE2qTSkS3fRBWh54v4TEARaJNAoejNpP6qMZW6R2bm7vfCsH4Oduv2N6Nb2FgrY3iqU3vYMIPitQi_V7_f6BQeDWReWJyVxXFHGgewJWqR56YV6uYNlwCK1_SryFkbYdJCK6FZg7woMpZhoZGq87X8Nhdj8g8w6Zu3ECKuYnc48w4FqzL6dvcU5rLSSxi64mAH1Uws0W291dRD5W6LrHsLH0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وکیل «الناز شاکردوست» اعلام کرد دادگاه تجدیدنظر استان تهران، حکم بدوی یک سال حبس تعزیری و دو سال محرومیت از فعالیت‌های سیاسی، مجازی و هنری علیه موکلش را تایید کرده است.
الناز شاکردوست، بازیگر سینما، به دلیل انتشار یک استوری مرتبط با اعتراضات دی ماه ۱۴۰۴ به دادگاه انقلاب احضار و به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس تعزیزی و دوسال محرومیت از فعالیت‌های سیاسی، مجازی و هنری محکوم شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/78600" target="_blank">📅 18:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78599">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=LKcgwiogh4GIdoo_O4D4gIyfY4aZGtqM1C1H0GR6fYcvtTgEcEL5TmE-qZDcViuet1U2_30ST_uB8GZ-urbTNSZnz1AJ2RHbFh_dGby_0pQD9d1bzKvlTxIprFTUqH973ZDiCd1tRnvA0lsHoB2CeYMWmPHiqJbWNE7yLzH-4EiE8iMCKS8nwEO0GW-XAN0zHkjfzvmdZ7nmiu_Z4E-MAmGaBF7jIJXt9mg79AkbrkyeV3zkdvPUzM-kAVSfZVoXvjMNoN0LI64GmSxpUN4zggL0O3mMoSED6Q9peZoce9NJCWWxShqXoTZqF5iifUy5hAPfMb1f8Jb_DVr1tbXJHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/84b4ce621c.mp4?token=LKcgwiogh4GIdoo_O4D4gIyfY4aZGtqM1C1H0GR6fYcvtTgEcEL5TmE-qZDcViuet1U2_30ST_uB8GZ-urbTNSZnz1AJ2RHbFh_dGby_0pQD9d1bzKvlTxIprFTUqH973ZDiCd1tRnvA0lsHoB2CeYMWmPHiqJbWNE7yLzH-4EiE8iMCKS8nwEO0GW-XAN0zHkjfzvmdZ7nmiu_Z4E-MAmGaBF7jIJXt9mg79AkbrkyeV3zkdvPUzM-kAVSfZVoXvjMNoN0LI64GmSxpUN4zggL0O3mMoSED6Q9peZoce9NJCWWxShqXoTZqF5iifUy5hAPfMb1f8Jb_DVr1tbXJHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه پنجشنبه نهم مهر ماه، ویدیویی در شبکه اجتماعی تروث سوشال منتشر کرد که حضور گسترده معترضان در جریان اعتراضات سراسری
دی ماه
در ایران را نشان می‌دهد.
در این ویدیو، معترضان شعار می‌دهند: «امسال سال خونه، سیدعلی سرنگونه»
realDonaldTrump
این ویدیو رو ۳۱ دسامبر ۲۰۲۵ ده‌ها اکانت عربی و اکانت‌های مرتبط به یک سازمان سیاسی خارج از کشور منتشر کرده بودند و گویا بیشترین توجه رو هم در اکانت این مسئول اسرائیلی گرفته بود که بارها ویدیوهایی با شرح اشتباه هم منتشر کرده:
GadbanWaleed
اون روزها خودم هم کلی ویدیوی مهم از شهرهای مختلف ایران منتشر کرده بودم ولی به درستی تاریخ این یکی شک داشتم که مربوط به اعتراض‌های ۱۴۰۱ باشه و نگذاشته بودمش. به ویژه اینکه منبع اولیه‌اش اکانت‌هایی بودند که همیشه کلی ویدیوی قدیمی رو هم با شرح نادرست بین ویدیوهای روز منتشر می‌کنند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78599" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78598">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحسین باستانی Hossein Bastani</strong></div>
<div class="tg-text">🔻
معمای «تیم شش‌نفره» در حکومت ایران
مسعود پزشکیان اخیرا به «تیمی شش‌نفره» در حکومت ایران اشاره کرد که در مورد بحران جاری با آمریکا «اختیار دارند تصمیم بگیرند و تصمیمات با هماهنگی آنها اجرا می‌شود». به دنبال انتشار این اظهارات در مصاحبه با سی‌بی‌اس، رسانه‌های رسمی ایران روایت‌هایی را از ترکیب تیم شش‌نفره منتشر کرده‌اند که عمدتا در مورد پنج نفر مشابه و در مورد نفر ششم متفاوت بوده‌اند. بخش ثابت روایت‌ها اغلب بر رئیس‌جمهور، رئیس مجلس، دبیر شورای عالی امنیت ملی، رئیس ستاد کل نیروهای مسلح و فرمانده کل سپاه تمرکز داشته، هرچند نفر ششم را برخی رئیس قوه قضاییه و برخی وزیر خارجه دانسته‌اند.
اشاره مسعود پزشکیان به وجود این تیم، البته اهمیت داشت، ولی این اشاره نه اولین بار بود که صورت می‌گرفت و نه نشانه تحولی کلیدی در ساختار تصمیم‌گیری کلان، یا مثلا ایجاد نهادی با اهمیتی مشابه شورای عالی امنیت ملی بود.
در تیرماه گذشته، عباس عراقچی در مصاحبه‌ای با برنامه یوتیوبی «ماجرای جنگ» گفته بود چارچوب مذاکرات با آمریکا در شورایی تعیین می‌شود که به «کمیته شش‌نفره» معروف است. توضیحات او اما نشان می‌داد که جایگاه این کمیته پایین‌تر از شعام ـ شورای عالی امنیت ملی ـ و در حد یکی از کارگروه‌های داخلی آن است. عباس عراقچی در گفتگوی خود، مشخصا از کمیته‌ای «در داخل دبیرخانه» شعام سخن گفت که ابتدا «کمیته هسته‌ای» و سپس «کمیته مذاکره» نام گرفته و در نهایت به «کمیته شش‌نفره» معروف شده است. مطابق اظهارات او، این کمیته از مدت‌ها قبل از جنگ چهل‌روزه فعال بوده و در زمان‌های دبیری علی شمخانی و سپس علی لاریجانی در شعام، به‌ترتیب تحت مسئولیت این دو نفر فعالیت می‌کرده است.
البته روایت عباس عراقچی از قرار داشتن این کمیته زیر مسئولیت دبیر شورا، این ابهام را ایجاد می‌کرد که آیا ریاست آن، مانند شعام، با رئیس‌جمهور است یا اینکه سخن از جمعی شش‌نفره است که رئیس‌جمهور را شامل نمی‌شود، ولی جمع‌بندی‌های خود را به رئیس دولت ارائه می‌کند.
در هر صورت، عباس عراقچی تاکید داشت که تصمیم‌های کمیته باید «عینا مانند مصوبات شورای عالی می‌رفت، تایید می‌شد و بعد ابلاغ می‌شد»، که اشاره‌ای به لزوم تایید مصوبات از سوی رهبر جمهوری اسلامی به نظر می‌رسید. او همچنین، به این سوال که آیا تصویب آتش‌بس (موقت) در پایان جنگ چهل‌روزه «با نظر آقا مجتبی» بود یا نه، پاسخ مثبت داد، هرچند در مورد شیوه تصویب گفت: «ارتباط ما با کسانی بود که رابط بودند و مسائل از آن طریق منتقل شد.»
قابل تامل است که مسعود پزشکیان، که در مرداد ماه از دو نوبت دیدار با رهبر جدید جمهوری اسلامی خبر داده بود، در مصاحبه‌هایش در سفر آمریکا هم به همان دو مرتبه ملاقات خود با رهبر اشاره کرد، که نشان می‌داد دیدار جدیدی با مقام اول حکومت نداشته است.
به عبارت دیگر، با گذشت هفت ماه از رهبری مجتبی خامنه‌ای، ارتباط تیم‌های حکومتی با رهبر کماکان به حلقه «رابط» اتکا دارد که، در مورد آن حدس‌های متنوعی مطرح شده است. از جمله، گمانه‌زنی‌هایی که حسین طائب رئیس جدید سازمان بسیج را از افراد موثر این حلقه می‌دانند.
🔹
ادامه  مقاله در لینک زیر در دسترس است:
https://www.bbc.com/persian/articles/cr9dw7dvjxj1o
@HosseinBastaniChannel</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78598" target="_blank">📅 16:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78597">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vGxJYvnc1AoOpuGIKvKvRwIZZG9ghLRQTzKIRI7fI3cVg3ydn1kkQInfkt8Okm_31If8lchJfTdaDV_S-Gqmw7Vv798frz7rNeir1OsDLh8OgsqQNBGkNE-0knuIY7hqUoJ3_fgVWqLhSfm2d5M1KRw82uAKOCZ5eRNOGQV2lE5TbTa5lsdvL_qD7u0-fc7xOoYnVa6d7WliPA89SpJiVvTS6i3i516gudk8rXEeJ0nAOxqh8SsSP6s5tW2ru1hA1dZlc7CPfJ0WqEQztOPQcrPm9-pReESugfasv9_zmnaKCijeY9PmUV3jZ7VTMuypZBcpkNqXFruBRltouYyEaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری آمریکا می‌گوید ایران در ماه سپتامبر حتی یک محمولهٔ نفت خام هم بارگیری نکرده است. داده‌های شرکت‌های ردیابی نفتکش‌ها نیز نشان می‌دهد در این ماه هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
اسکات بسنت شامگاه پنج‌شنبه، نهم مهر، در شبکهٔ اجتماعی ایکس نوشت: «ایران در ماه سپتامبر صفر بشکه نفت خام روی نفتکش‌ها بارگیری کرد» و افزود دولت دونالد ترامپ در حال قطع «حیاتی‌ترین منبع درآمدی» جمهوری اسلامی است.
داده‌های اولیهٔ ردیابی نفتکش‌ها که بلومبرگ منتشر کرده و همچنین اطلاعات شرکت‌های کپلر و ورتکسا نشان می‌دهد در سراسر ماه سپتامبر هیچ بارگیری نفت خامی از بنادر ایران ثبت نشده است.
این در حالی است که برآورد کپلر و ورتکسا از بارگیری نفت خام و میعانات ایران در ماه اوت حدود ۲۲۰ تا ۲۵۵ هزار بشکه در روز بود.
ایران همچنان مقداری نفت را که پیشتر بارگیری و در آب‌های آسیا ذخیره شده بود به خریداران چینی تحویل می‌دهد، اما این ذخایر بدون خروج محموله‌های تازه از ایران رو به کاهش است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78597" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78596">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbtWsZ4EtiloeyOUGscNaH2iz8YTNfmc27p9EmYfkevV5EICGbHyttd6Eh8UkWJEN15tDtGDhJ5Lm_n6YeI0RvXYXENILL7lZc4Hz7X9buB_FuwNvQTl7qee3IxlwgsM3nf1NcsFYDhgqJBsNwUvFo_XLBd8r-bd0TTJsVgLB7jbjubXGIQuRfZnXZQMdB2LMdpQ8oNo67EQo-nCf_Dh8QMMhV25PI5yv_9mLHV24tCiCTmfYKbgarE4_Q2pLjpdji82rCd1hHO9prFozFtIWjuy0YoxVuX-dvnxpSOfXgDfs0Sf018CvDQW9buz3l1BsE0NrKC1Z4ISz-XO3FVwjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، روز جمعه دهم مهر ماه، از وقوع درگیری مسلحانه میان سپاه پاسداران و اعضای «یک گروه تروریستی» در یکی از روستاهای شهرستان راسک در جنوب سیستان و بلوچستان خبر داد.
تسنیم با اعلام این خبر افزود نیروهای سپاه «در حال پاکسازی منطقه و بررسی وضعیت» هستند.
همزمان خبرگزاری حکومتی فارس نیز از آغاز «اقدام عملیاتی» سپاه پاسداران از صبح جمعه در راسک خبر داده است.
این خبر در حالی منتشر می‌شود که روز پنجشنبه نیز قرارگاه قدس نیروی زمینی سپاه با انتشار ویدیویی از یک درگیری مسلحانه، از کشته شدن ۶ عضو یک «گروهک تروریستی تکفیری» در منطقه منزل‌آب زاهدان خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78596" target="_blank">📅 16:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78595">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV0LcNgbG7oi4VpnvXMJRvQr3QNxs82VAHOCY1ZLPS6d8DrdlerEMB-dCwBcGLxBOI7Xj_6ZCXtW-VrRfPeeypZmg8jA0G4cC_qcAKPzV_tDFAP79WrNS6FaGuwQmL8tXT8Jh9K32uIjmHoS3jcEetSuTtdTJw_zFFb_oMOmGVd-53dN3t65Iy9O7UKh8YqXjsmrxotCpLP1OilA5N9gN8KU5TLAFcWMwKX1aehpfaY1UoizBhB3NkM9lZIPKqqC10rYI2NTEPiAswUIbk82V-NarIJ6z0_Ikp4VG4M9G3VKrJBWBHYcXwShAfvUcL0uwIHnKEa-2-Pk96fBlI5HGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ در دو اظهارنظر تازه دربارهٔ ایران هشدار داد اگر مشخص شود تهران در حادثهٔ پرواز فلای‌دبی به مقصد اسرائیل دست داشته، «به‌شدت هدف قرار خواهد گرفت» و ساعاتی بعد بار دیگر گفت به اعتقاد او ایران «در آستانهٔ تسلیم‌شدن» است.
این اظهارات همزمان با ادامهٔ تحقیقات امارات متحده عربی دربارهٔ احتمال تروریستی بودن حادثهٔ پرواز فلای‌دبی و گزارش‌ها دربارهٔ تقویت حضور نظامی آمریکا در منطقه مطرح شده است.
رئیس‌جمهور آمریکا شامگاه پنج‌شنبه، نهم مهر، به وقت ایران، در پاسخ به پرسش خبرنگاران در کاخ سفید دربارهٔ احتمال ارتباط ایران با کمک‌خلبانی که به خلبان پرواز دبی به تل‌آویو حمله کرد، گفت: «بر اساس آن‌چه می‌شنوم، می‌گویم پاسخ مثبت است، اما همین حالا در حال بررسی آن هستیم.»
تاکنون هیچ مدرک علنی دربارهٔ ارتباط ایران با این حادثه منتشر نشده و تحقیقات دربارهٔ انگیزهٔ کمک‌خلبان ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78595" target="_blank">📅 16:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78594">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLSmnP-fySCJQY-Ylb-A7u3FLLZB8o2RvWtxR6_qjCZUHIyhaA4F-ecxmq7c-i-aWiBukN9b3QutRPpr-Ywm0iKg1Fi76ue1u3fpZcdicMhmzRpWaRTNUQXJlb7tb0jLMXpUDYPm63ddbUf9beH68BM8EmgTjPXZlTIFJ5uDYmA4JVgo2BiOzYy1D7KQvF43wmo8uD6OE-2ttqVbCqXKVchHNMdqYp3lm0o6IertfjbHzdCXjQ8lqwr-4IQ0aNFSpnwqCrV1do7NzgsbgTohcHLwyc9BNpkgrUHzYrR7tUhdwnE1SJWoE_Nl-tAWynajnu7d8rh7BltwQ1y2s1_4kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه شهروند اهل کرمانشاه، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، در شعبه ۲۳ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌اند.
بر اساس اطلاعاتی که به سازمان حقوق بشر هانا رسیده، سیروان شعبانی، ۲۵ ساله، هنرمند و نوازنده و سرپرست یک ارکستر پاپ و سنتی، خسرو محمدی‌نیا و مسعود توشمالانی هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شوند.
هانا گزارش داده است که این سه نفر روز ۱۹ دی ۱۴۰۴، هم‌زمان با اعتراضات در اسلامشهر، از سوی نیروهای امنیتی بازداشت شدند و پس از آن مدتی در سلول انفرادی نگهداری شدند. بر اساس این گزارش، آنها پس از ماه‌ها نگهداری در شرایط انفرادی و آنچه هانا «اخذ اعترافات اجباری» خوانده، به زندان قزلحصار منتقل شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78594" target="_blank">📅 16:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78593">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IRgzqhtwmBVPE08PJtIhf0MqqjZ0dviZglcZVINgL2iZnEzhTbaA2phKWTi9HaI3JQKNfr9E2ikoVlVVMrznk-FcS45Qqizi-U9nMN00QGsE3jje4GyONv2cbH6VUa4PZ9ya5Hz9HiIQyEqTCB0a-AtGwwP0TvE38mDDxcB7nFjMCA8QJbLWO9bp569zbtX4N3fglHgCLxytL1-jZ7CsYWIGYi3cR1xkoyjTir6TLrEyl-91YMg2Mid2i8rLAJ3wtpnOhUH2_jaTbTobgMIc_lN01RYTkfOrqWICTAn1qM_SC92eGqF77FE00neDlylRT8ewzBif4XFeirf03Hcpug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
«عملیات تجارت دریایی بریتانیا» (UKMTO) گزارشی از یک منبع ثالث دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز با یک پرتابه ناشناس مورد اصابت قرار گرفته و در پی آن آتش‌سوزی رخ داده است.
گزارش شده که خدمه در سلامت هستند. میزان خسارت و تأثیرات زیست‌محیطی در زمان انتشار این گزارش مشخص نیست.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78593" target="_blank">📅 23:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78592">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTGWJVEbZbh0IZ0ZBJkOELyVj35O0aCW1mRFQ2Fk7qS9HzOuwGLj9jPRw6x3_vKXku0Ls_MYQTufDN5g5JY4krXPKboDFgrbN61_yTv2MpMnT5RNcwfouxmTuuSmt6zN9z9Pspmt6jy3yvBkyoBZhJYwjZIeSSF8An5Nx9Kq2RcSFLvell5nAPhzDSIoboyaVoEPQ2FiyIp7aI2ga7_v6hLHPyzM8-PyG8s6w_Dkpq3CRgcduQqU8wQdlIxL-oJPI-gdBtOYbtYXGXypnXvZBUjA4zo5JWU1j9sdfgKZlmg79e5nolUIbdRGSNC4Q0Nx9cT8K8erCDEEjLkekoPvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
من بارها گفته بودم که برای از بین بردن «تهدید هسته‌ای ایران» ۴ تا ۶ هفته زمان لازم است، اما من این کار را در یک شب انجام دادم! باقی آن زمان فقط برای این است که مطمئن شویم اوضاع همین‌طور باقی می‌ماند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78592" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78591">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GDvY_xfxC9x7RgEMG1gvcZIjJx_bDP63pPJ-lxLZD_8zuRNp5KbTx5HEJgDOMp33q7uPmMiRtDSPN96u_1-IfifrrK7e6iqh6RE4rE13jqZd6yscx-QajqZol9MaoyavMnB8mG2EvTKLKkZySb8abfrr6kd1rTsJe2T1BlmzOad52aAc7OOavMPhVkJjq2xYEminWeb2EFroKONwbc5Or2ujtuHIaBssgXPKQqSc9P0zZKxazFXj5Hk9GBETqScoSrIwvnOkFY9mcVO_bPAhpgzDPoMtTJMIbn4_HYHKZMdSXkSGEjZ2nqYy-YLcP0SzR1bIOyHGiFvDF9p82BjHSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس جمهوری آمریکا، در مصاحبه‌ای مفصل با مجله تایم گفت پیشنهاد اخیر جمهوری اسلامی برای پایان دادن به درگیری‌ها و بازگشایی تنگه هرمز را به دلیل «ناکافی» بودن آن رد کرده است، و افزود احتمال تشدید حملات نظامی آمریکا علیه جمهوری اسلامی را منتفی نمی‌داند. این مصاحبه ۶ مهر در کاخ سفید انجام و روز پنجشنبه ۹ مهر منتشر شد.
دونالد ترامپ در پاسخ به این پرسش که چرا درگیری نظامی با جمهوری اسلامی بر خلاف برآورد اولیه او وارد هفتمین ماه شده است، گفت پس از حمله بمب‌افکن‌های بی-۲ به تاسیسات هسته‌ای می‌توانست عملیات را متوقف کند، اما تصمیم گرفت «فراتر» برود تا حکومت ایران نتواند توانایی‌های خود را «به شکلی متفاوت» بازسازی کند.
او گفت: «توانایی هسته‌ای آنها را نابود کرده‌ام. نیروی دریایی‌شان را نابود کرده‌ام؛ ۱۵۹ کشتی در کف دریا هستند. نیروی هوایی‌شان را نابود کرده‌ام. همه هواپیماهایشان از بین رفته‌اند. رادارشان را نابود کرده‌ام.» رئیس جمهوری آمریکا همچنین گفت اقتصاد جمهوری اسلامی از بین رفته و تورم آن حدود ۳۰۰ درصد است.
ترامپ گفت آمریکا عملا کنترل تنگه هرمز را از جمهوری اسلامی گرفته است، و تاکید کرد شب پیش از مصاحبه حجم عبور نفت از این آبراه به بالاترین میزان تاریخی رسیده بود. داده‌های جدید نشان می‌دهد صادرات نفت خلیج فارس در روزهای اخیر به‌ شدت بهبود یافته و به سطوح متوسط سال ۲۰۲۵ بازگشته است.
در بخش دیگری از مصاحبه، خبرنگار تایم به اظهارات اخیر ترامپ درباره احتمال «نابودی ایران» اشاره کرد و پرسید آیا چنین اقدامی واقعا ممکن است. او پاسخ داد: «بله، این کار را خواهم کرد. ممکن است.»
هنگامی که خبرنگار درباره مردم غیرنظامی ایران پرسید، رئیس جمهوری به سرکوب اعتراضات اشاره کرد و گفت حکومت ایران طی ماه‌های اخیر بین ۷۲ هزار تا ۷۵ هزار نفر را کشته است.
ترامپ همچنین گفت از تصمیم خود برای مداخله نکردن مستقیم در جریان اعتراضات دی‌ماه پشیمان نیست، و عملکرد دولتش در قبال جمهوری اسلامی را «باورنکردنی» توصیف کرد.
او گفت ایران کشوری بسیار بزرگ‌تر و دورتر از ونزوئلا است، اما «نتیجه همان خواهد بود» و افزود: «آنها می‌خواهند توافق کنند.»
در پاسخ به پرسشی درباره علت رد پیشنهاد اخیر جمهوری اسلامی برای آتش‌بس، ترامپ گفت رژیم ایران پیشنهاد بازگشایی تنگه هرمز را مطرح کرد، اما شرایط آن «حتی نزدیک به کافی هم نبود.»
رویترز گزارش داده است پیشنهاد ارائه‌شده از طریق میانجی‌های قطری شامل پایان درگیری‌ها و بازگشایی تنگه هرمز در برابر رفع برخی فشارهای اقتصادی آمریکا و دسترسی رژیم ایران به دارایی‌های مسدودشده بود. مذاکرات غیرمستقیم همچنان ادامه دارد.
خبرنگار تایم سپس پرسید آیا دولت آمریکا پس از انتخابات میان‌دوره‌ای حملات به جمهوری اسلامی را افزایش خواهد داد. ترامپ پاسخ داد: «ممکن است.»
او از ارائه جزئیات خودداری کرد، اما گفت آمریکا طی شش ماه گذشته ذخایر تسلیحاتی خود را افزایش داده و شرکت‌های دفاعی با فعالیت شبانه‌روزی در حال گسترش تولید هستند.
رئیس جمهوری آمریکا در پایان مصاحبه هدف اصلی سیاست خود در قبال جمهوری اسلامی را جلوگیری از دستیابی آن به سلاح هسته‌ای دانست و گفت: «موضوع اصلی که همیشه مطرح می‌کنم این است که ایران نمی‌تواند یک قدرت هسته‌ای باشد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78591" target="_blank">📅 17:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78590">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJyJyAOHFo7kwTtxtGrmWQydh5NqGwTSAoC9gqObPQKa9egCd1sEFmuPSqXP7DqvUiv6iZ6e-k9jKk1ei8p9KhrAlg311R5ysFGNtXvGY1wVPcc2QNBSOdQie8M_BlvdZvWl1Y79mjwhFfqgRO98B5-L_7SXHnOETkFD4GdhtJ77oEecMC6pMOgWpoav3yEMwuhyrw9RgYG7XnSRbQUhxg0zbhJgopgzX5qlO0uJvIbKdDwDMpVyoFK-N_ZnGFVn9OmFdDckedoDH0WhItgz9syZOQ-91d5-Az6nK2jmSrSSKtZz8v_xPdHM6TjuB4zK7hvFz0D-_lM0yjuKX4E0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد ایران روز پنج‌شنبه با افزایشی حدود ۱.۵ درصدی نسبت به روز گذشته به ۲۵۸ هزار و ۹۰۰ تومان اوج گرفت.
دلار آمریکا در مقابل ریال ایران طی یک هفته گذشته بیش از ۱۰ درصد، طی یک ماه گذشته بیش از ۲۰ درصد و از زمان آغاز جنگ حدود ۶۴ درصد جهش داشته است.
در بازه یک‌ساله نیز نرخ برابری دلار در مقابل ریال ایران تقریبا ۱۲۵ درصد رشد داشته است.
قیمت سکه امامی نیز در لحظه تنظیم این گزارش در بعد از ظهر پنج‌شنبه از ۲۶۰ میلیون تومان فراتر رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/78590" target="_blank">📅 17:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78589">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ft8O1_V0BqGvfCO3b8iemZWrAbjF9edqDRMu2aKOmN5yP5R2rPTx7tHLksPtt-9ro-pc7kmydS1yChEWlnKBGIBm0dO3gEtA6PaFZaw2a0eSxNMymes3JWWy8gDHtVTlSoHvsllTpFXRhDPA5v8DSlz5ETM5nnVEE51A_ZEBPmqiV3ue985n35TlQqoLUJI1J6r136xWy7nuIWCgzoRIdhIQaGv-kgoGrQGV_XJscNAOu8qK-mg0pYI8nXCAIHmBxc46gy53Ftla9QdtT15IMk2HWDjoFMf9vsLDzL6Z3IXcBsE-8Lbo-KEVp9kuPS2jDeDeNZcm1qanhqpem7Kd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«فرزانه فصیحی»، دونده المپیکی ایران، در واکنش به اظهارات تازه «احسان حدادی»، رییس فدراسیون دوومیدانی جمهوری اسلامی، او را «بدنام‌ترین ورزشکار تاریخ ایران» خواند و نوشت که ورزشکاران جوان باید او را «عبرت» قرار دهند، نه الگو.
فرزانه فصیحی در متنی که در صفحه اینستاگرام خود منتشر کرد، خطاب به احسان حدادی نوشت: «در جهان موازی تو باید پشت میله‌های زندان می‌بودی و از هیچ حق شهروندی برخوردار نمی‌شدی، ولی چه کنیم که اینجا سرنوشت صدها و هزاران جوان پاک و معصوم رو هم سپردن دستت و حالا فاز نصیحت برداشتی.»
این واکنش پس از آن منتشر شد که احسان حدادی، چهارشنبه ۸مهر۱۴۰۵، در گفت‌وگو با وب‌سایت حکومتی «ورزش سه»، درباره ورزشکاران زن گفته بود: «با زنان دونده جلسه می‌گذارم و به آن‌ها می‌گویم تو می‌توانی مثل خیلی از ورزشکاران زن، مجازی شوی با ۳۰ هزار، ۵۰ هزار، ۳۰۰ هزار فالوئر، یا می‌توانی قهرمان شوی.»
فرزانه فصیحی همچنین با اشاره به «ریحانه مبینی»، «زهرا زارعی» و «فاطمه محیطی‌زاده»، از ورزشکاران زن دوومیدانی ایران، نوشت تصور این‌که آنها بخواهند از آموزش‌های احسان حدادی پیروی کنند، برای او «مثل کابوس» است.
او در ادامه خطاب به رییس فدراسیون دوومیدانی نوشته است: «شریف بودن ربطی به مدال و قهرمانی نداره. تو ثابت کردی با خورجینی از مدال هم می‌شه به قهقرا رفت و منفور یک ملت شد.»
اشاره فرزانه فصیحی به «پشت میله‌های زندان»، به پرونده قضایی احسان حدادی در دهه ۱۳۹۰ بازمی‌گردد. در آن پرونده اتهام تعرض و تجاوز جنسی علیه احسان حدادی مطرح شده بود و دادگاه نیز رای به زندان، تحمل شلاق و جزای نقدی داد. با این حال پرونده با دخالت نهادهای امنیتی مختومه شد.
در سال‌های اخیر برخی از زنان شاخص دوومیدانی ایران نیز کشور را ترک کرده‌اند. «الناز کمپانی»، رکورددار دوی ۶۰ متر با مانع ایران، از مهاجرت خود به آمریکا خبر داد و پیش از او «مریم طوسی»، رکورددار دوی ۲۰۰ متر داخل سالن زنان ایران، به آمریکا مهاجرت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78589" target="_blank">📅 17:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78588">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kvy25vS0vPdJ-APiRLaoLYLM3WO6VJ9Hxo_WKuSJ1U_bpclGafv-69KqqQopAQMY3_GBTWHvaxbpX36obgwf6P0ZTJNeHvWvZ-Y1A2-jnxtW1hlzaXZn0tbKlR99VEXjp4iW1vroSOUhfQD4tVP9cuRR5kMw2b6lYeXvTws3JobB2O_l7waoH4yM4uRDTLAPcv2NYuByAfZ3Hz943K9qs6VQYapTua8Vc4gopHHJByapHneMJQUXRPpwvpVqglZz3vecCOfOj4ldTyWDs0RE-cxRMoHgN1NWalbQ3bW_YPbO70K0lS5hp-Zy7w3ItW8Gm7XaJHzkJmX7xUxeM0QfjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایمان صادقی، بلاگر ۲۰ ساله و از بازداشت‌شدگان [اعتراضات دی ماه] در کاشان، به بیش از ۱۳ سال حبس تعزیری محکوم شده است.
او بابت اتهام «تبلیغ علیه نظام» به هفت ماه و ۱۶ روز حبس و بابت اتهام «انتشار محتوای مجرمانه برخلاف امنیت کشور» به ۱۲ سال و شش ماه و یک روز حبس تعزیری محکوم شده است.
«انتشار محتوای مجرمانه در رسانه‌ها و مطبوعات منتهی به هتک حرمت اشخاص» نیز از دیگر اتهام‌های مطرح‌شده در پرونده اوست.
ایمان صادقی ۱۱ بهمن‌ماه ۱۴۰۴ بازداشت و پس از آن به زندان کاشان منتقل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/78588" target="_blank">📅 17:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78587">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bYfe7_TwHPSoqmLjrtBqIBV4_ozVLBwVVa1vIB7GFHIQ7r9GGQPT5-kXPcczJo_SHTj8LQPBeOfnGyCYdidFToUVszNsbF0cKD5IKQ0v23xMpUkKB0bCjE5dIHTVbmja9pDMPECu6ynH9xzeYe-vP-hYUUhBeJN8sphzlFRSsZYFW-ASfcNR6Ixwicp8umxi6lJNnpv3fnqQU3aeaBhy05sHj_Sjhw5IqtFsWMK3TEasJPXis4rrooVssP1NGadKhnaYDjfDXmu2RTSvPlzB0flVcmUD7iWc4a7vzWI9mzDD2KrkGd7PaxbvtTP5YWolDbCun2Xmzmy3rTzhhzzNKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، چهارشنبه شب، گزارش نیویورک‌پست از اظهارات اسکات بسنت، وزیر خزانه‌داری آمریکا را منتشر کرد که گفته است اقتصاد جمهوری اسلامی ایران، «ظرف دو هفته» هیچ‌چیزی برای تجارت نخواهد داشت.
محاصره دریایی بنادر ایران مانع آن شده است که جمهوری اسلامی از طریق دریا بتواند نفتی صادر کند. دلار آمریکا نیز در روزهای اخیر با سقوط خیره کننده ریال جمهوری اسلامی، رکوردهای تازه‌ای زده است.
آقای بسنت به فاکس‌نیوز گفت اقتصاد تحت محاصره جمهوری اسلامی ایران به‌زودی و پس از تحویل آخرین محموله‌های نفتی خود، در حدود دو هفته دیگر «چیزی برای مبادله» نخواهد داشت.
به نوشته نیویورک پست، بسنت در مصاحبه با فاکس‌نیوز ارزیابی کرد که جمهوری اسلامی به دلیل فروپاشی اقتصاد خود که با اجرای «عملیات طرد اقتصادی» شتاب گرفته، از روی درماندگی به‌شدت مشتاق توافق است و هشدار داد که مشکلات آن طی دو هفته آینده به شکل چشمگیری وخیم‌تر خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78587" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78586">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz8d7FvY46uit3yd9csTPjo2zv2kPvoYTOwMrbnGhTeMJfwYIxYthwpm_t9Ux9wuT57WUI6WHVctHlpJNVRUkugwYNo4JInKddrp3lYBLnogQbVSKQoCtw2_rleCr8BB2sGhmZAE6m_qi6MR0jIUt-FT52NAOvnI0v1lzVlf5zRGeB7Ywhf4tcOXoC9_cZP73DaKYF0nqkjjh-mb2RpNriTideKnKzh5S7dxovgvCS1o0MwESlcFPRR8btcMXdCnQ6g7-fXWDp_6fn89hnP8ku37KHpUZ_rN9kdWUW4jlON1qgfdOnn7hXo1FwlY-HbO7MlT20e55fAoOh1EVACT3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش آکسیوس به نقل از یک مقام آگاه، مارکو روبیو، وزیر امور خارجه ایالات متحده، روز دوشنبه ششم مهر پس از به بن‌بست رسیدن مذاکرات با جمهوری اسلامی ایران، دستور داد هیات ایرانی حاضر در مجمع عمومی سازمان ملل، از جمله عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، فورا آمریکا را ترک کند.
یکی از مقام‌های آمریکایی به آکسیوس گفت: «روبیو هیات ایرانی را که بیش از حد مهمان مانده بود، بیرون کرد. مجمع عمومی سازمان ملل تمام شده بود و وقت آن بود که بروند.» بر اساس این گزارش، نمایندگی آمریکا در سازمان ملل دوشنبه شب به نمایندگی جمهوری اسلامی ایران اطلاع داد که هیات ایرانی باید فورا نیویورک را ترک کند.
آکسیوس نوشت عراقچی و اعضای هیات چند ساعت بعد راهی فرودگاه شدند و بامداد سه‌شنبه با پروازی از نیویورک به دوحه رفتند. منبع دوم نیز درخواست آمریکا برای خروج هیات را تایید کرد، اما گفت عراقچی از پیش قرار بود دوشنبه‌شب برای بازگشت به تهران حرکت کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78586" target="_blank">📅 06:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78585">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DtA1nuAzc17AW3fZf1jHMPpvplw3CDMfyq7JB5XRtC3TkI4R_WMWqpt-GrFljLnddRb1SETExTBxY5UOw8SSBeGnTHYZOqsV4hFn0oowG9mPPFnBoEWrCRRQACCvQiIV_G7a7SJVqRVp9ytQ-Ua2Ti1dYu6Dwd-B4IVTWGPmsd7hKN4th98_Izs6GWRq0sylTf38juu3G0JlWWFtC2_B_2yEomJA0mbMkY1ZOCv37YCWZSJbO3GXCMLUJTZs16z5BADJzmpD3o6fydCwmmUAGpQ1w59SdDs8bsd6L3hvGIuA99FhiSq7iPt-z2VnICeMZ2OZR7ZSX-DM4UVAAw_5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، در پاسخ به سوال خبرنگاری که از او پرسید اگر رهبران جمهوری اسلامی به گفته او «دیوانه» و «غیرمنطقی» هستند، چگونه می‌خواهید با این افراد توافق کنید؟ رئیس‌جمهوری آمریکا پاسخ داد: «شاید آن‌ها را منفجر کنیم. باید تصمیم بگیریم. منفجرشان کنیم، توافق کنیم، وقتش دارد می‌رسد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78585" target="_blank">📅 00:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78584">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=Nx8fSryYx-Kkut93QO9_5S2bUAEzIX1-c9Lfm59i6CWhG0McmvjLq6LKpfo0K2dptbUWjRCzZ60nJdobieC7LeF_XiH56ROIQyiEu995f6_nGX_DyeM1SN8LXoWA95qZuFu9rQoCtEhZY0B0qgjw3SN9hg2CuvXP7e0gi1NnwNvIGYGR7Ngrz_f4GfNL7JiM0aib_TII0fhDJoIu8kmeRUdVrMLS6d1dQat5uVUXfTQ9ipu6KFE0F0aDkBo9U_VRcVXweE-JpSPEIu2TgtBcVGl3Lk_6W7bPJ9OzC4cQ-BH6SKUk_24qEHiPtiTW8WuJzcuyReryjq-hPHutON5inA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e8aa88a9b.mp4?token=Nx8fSryYx-Kkut93QO9_5S2bUAEzIX1-c9Lfm59i6CWhG0McmvjLq6LKpfo0K2dptbUWjRCzZ60nJdobieC7LeF_XiH56ROIQyiEu995f6_nGX_DyeM1SN8LXoWA95qZuFu9rQoCtEhZY0B0qgjw3SN9hg2CuvXP7e0gi1NnwNvIGYGR7Ngrz_f4GfNL7JiM0aib_TII0fhDJoIu8kmeRUdVrMLS6d1dQat5uVUXfTQ9ipu6KFE0F0aDkBo9U_VRcVXweE-JpSPEIu2TgtBcVGl3Lk_6W7bPJ9OzC4cQ-BH6SKUk_24qEHiPtiTW8WuJzcuyReryjq-hPHutON5inA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در تازه‌ترین اظهارات خود درباره ایران گفت تحولات جدیدی «بسیار زود» رخ خواهد داد.
ترامپ گفت: «خیلی زود» خواهید دید که اتفاقاتی رخ خواهد داد. او در ادامه گفت ایران «عملا ویران شده» و با تورم بیش از ۳۰۰ درصدی و وضعیت نامناسب اقتصادی روبه‌رو است. رئیس‌جمهوری آمریکا همچنین بار دیگر گفت که در جریان جنگ، نیروی دریایی و نیروی هوایی ایران از بین رفته و تجهیزات پدافند هوایی این کشور نیز نابود شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/78584" target="_blank">📅 22:48 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78583">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pub8L5KM2zzUqMFli5XkujWBV-AR7R9L87WNOB7lh7X_gJNIxGvrCwii1a1rbuv01tpnUQ4c6PC8q6fOYycPsZC8yYKNInxk3WHoNGtS2pKm7Xk378IKnEOBA6E1sB-EQcaFmg-1_haaNRMHwNiViCd-49dkosMB-0eU8SjbvOR1_RLvUp_wve4KS3QIy423c7q-JUnW3sZ4g-CCB4fuL7wgE34uLO2_z5BLS--uLv5krLUXw1ivMv8DAizr8bB68rz1VyJWKPsgIpKwmdQf1teJmo5ftW_lx8j5G80EBKBLfdeNL8Hf46vS8nGWbD3BVo9s4VDhzYl2VIa-xTIapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندی برنهام، نخست‌وزیر بریتانیا، روز چهارشنبه هشتم مهر، اعلام کرد که قرائن و شواهد قوی نشان می‌دهد جمهوری اسلامی ایران در حادثه امنیتی اخیر در نزدیکی پایگاه هوایی «فیرفورد» (RAF Fairford) تحت مدیریت آمریکا نقش داشته است.
پلیس ضدتروریسم بریتانیا روز یکشنبه پنج جوان ۲۳ تا ۲۵ ساله — که همگی اتباع بریتانیا و ساکن لندن هستند — را به اتهام آماده‌سازی برای اقدام تروریستی دستگیر کرد، اما آنان روز بعد با وثیقه آزاد شدند.
پایگاه هوایی فیرفورد در گلوستشر بریتانیا که پیشینه‌ای طولانی در استفاده توسط نیروهای آمریکایی و ناتو دارد، از ماه مارس به عنوان نقطه‌ای برای پشتیبانی لوجستیکی حملات ایالات متحده علیه ایران مورد استفاده قرار گرفته است. بریتانیا مجوز بهره‌برداری از بمب‌افکن‌های آمریکایی مستقر در این پایگاه را برای هدف قرار دادن سایت‌های موشکی ایران — که کشتی‌های عبوری در تنگه هرمز را تهدید می‌کنند — صادر کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78583" target="_blank">📅 20:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78582">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMqPml8r9QF-KarZ7GA0sBwdGhutLYiIS_5pfkRn4_PWZNb5qR9mXwuGF1YI8hSgduizmettXlSCZXK5kH5scS9hcYJxM42q_RgwbMDq4UFnYfvhHRPVKGgYZS_HFJLcuCcIY6_5-Gc1YhQ-cDdVX703bfOpzvcYyRLQSfmE9bOyh243EhVyQysnQeq1n27gBUlVCRz3tr1GkoBjWNd6TUPoFNeYYOWIBGvDDmsy7KaJayscoAbCejs2l5U3Jdh332H6rTX4TFqLgUemyUpY2CuHODo6qoV39I9ns7CFmMErjmBuchPJlHfUBnke7hy83FEYWkk0u_eHNzNTsSECbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه، چهارشنبه هشتم مهر گزارش داد صرافی‌های رمزارز معاملات تتر را از ساعت ۲۱ هر شب تا ۹ صبح روز بعد متوقف کرده‌اند.
بر اساس این گزارش، این محدودیت از امروز ساعت ۲۱ تا یکشنبه ۱۲ مهرماه اعمال می‌شود و سقف خرید روزانه برای هر کاربر دو هزار تتر تعیین شده است.
این اقدام در پی افزایش پرشتاب قیمت ارزهای خارجی و سقوط ارزش ریال انجام شده است.
عصر چهارشنبه قیمت دلار در بازار آزاد ایران از ۲۵۵ هزار تومان عبور کرد و هر تتر نیز حدود ۲۵۵ هزار تومان معامله شد.
پیش از این بانک مرکزی جمهوری اسلامی نیز اعلام کرده بود اعطای وام برای خرید طلا، ارز و رمزارز ممنوع است و این ممنوعیت شامل تسهیلات مستقیم و غیرمستقیم بانک‌ها و واحدهای دیجیتال نیز می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/78582" target="_blank">📅 20:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78581">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc36ad6QNhvuusnN21bydqm-nVB2YjPDxdCHmiLVCIgTmnxhMgj9b-Cjm5pXj514HpCxk3ux8jXUuLoZp_Ef_ad11rQM53r6J_EjCPvYc6kE-UEfMH6RZcF8hTHvr14Dm4_ZzLYRoovLM7kihCap4Eh3e2z8nTPjJ1eoYPfFQA8sLrLCA-_2lxwn7tR8Iig6Mkzjcb7KraVFWsAeW55z2X-tiH5eGrib2mKfqcYC__GWS4hyOsZqrsOxgi-kY4GB2GzYjJ3FBxdZoNrEUdzonSQJ3oSWO9F-OdiUqeeaYDv9r0kydp7b53ZaoFxIwBkuoIQ0sShG7dPbvYAbCVn0VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۶ هزار تومان گذشت و دادستان تهران به ضابطان قضایی دستور داد با «عوامل اخلال در بازار ارز» برخورد کنند.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار ۲۵۶ هزار و ۵۰۰ تومان، یورو ۲۹۰ هزار و ۵۰۰ تومان و پوند بریتانیا ۳۳۹ هزار تومان معامله شد.
دلار صبح امروز ۲۵۵ هزار تومان بود و دیروز ۲۵۳ هزار و ۱۰۰ تومان، یعنی در دو روز سه هزار و ۴۰۰ تومان بالا رفته است.
همزمان دادستان تهران از برخورد با فعالان بازار خبر داد و گفت ضابطان قضایی مأموریت یافته‌اند با بررسی میدانی و رصد فضای مجازی، عوامل اخلال را شناسایی و به دستگاه قضایی معرفی کنند و گزارش اقدام‌هایشان را روزانه بفرستند.
نیروی انتظامی جمهوری اسلامی دوشنبه ۱۱ نفر از فعالان بازار ارز را بازداشت کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78581" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jK_MeXWa5sFHohiaakKnqK17rq_H07x4uT3BEXRh552Cekw2g9mDy5gQlvxGzn6UbkA0LcbUiDMvebzQNU4F4IuycqtH68fDv0f99WcZY5qYTHtkr_38DPtKl-Pn1hxD8FvXwZvym9Onf3Kb-fsyFb5IpuByOwCGNgwfw9HMaZH4v8RG9761PhChr5cX3rlgYMgJlRvNFAxCbSfZb8FgXGITd7-McY6IIMT2Cuun6rHRZfjb2hB4lOgjwuw3mwaqaIHhIQGilsDfX_QrRkHwO3XL0v9AvOsMy-2d_RCyay8Dc-aRVWah8LT2OBasm6N1pO4lkgd8L4WyRpW-h764fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=jSxWAs-iCojbUhuXJhmHrqve0Jdt8eaEbAPNJ3ZXeF6M-yS26J6j4wvwaoTaBl27V-IeNYn3SjQaIllLBXYgC8I-2QUCTUZ_e77aBB7HHNcpdNoURUDBT9eQvn1OUP38VaMxeuVCxsS_Twub7YBuzt0OrkCMQ5wrfmdGiSEp6kXT9mJS9Vx65zXz-bMk3NtF_aC6xzNz96Jwh-qQzURtb9EEaeuhyQBL3IZsQcU0ZkO4MpGVCFNiW_Upffr3amLB-qA_Lis0MT9FkP-4PyojhAZZwMO5rt4jMiPaRjmACzQfp86ow0jcTEPSXRZgUhSgaS-b2qYAexJoPV88e4ngdA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0e653b47a5.mp4?token=jSxWAs-iCojbUhuXJhmHrqve0Jdt8eaEbAPNJ3ZXeF6M-yS26J6j4wvwaoTaBl27V-IeNYn3SjQaIllLBXYgC8I-2QUCTUZ_e77aBB7HHNcpdNoURUDBT9eQvn1OUP38VaMxeuVCxsS_Twub7YBuzt0OrkCMQ5wrfmdGiSEp6kXT9mJS9Vx65zXz-bMk3NtF_aC6xzNz96Jwh-qQzURtb9EEaeuhyQBL3IZsQcU0ZkO4MpGVCFNiW_Upffr3amLB-qA_Lis0MT9FkP-4PyojhAZZwMO5rt4jMiPaRjmACzQfp86ow0jcTEPSXRZgUhSgaS-b2qYAexJoPV88e4ngdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی فرود اضطراری یک هواپیمای خطوط هوایی «فلای دوبی» از مبدأ دوبی به مقصد تل‌آویو در عربستان سعودی، نخست‌وزیر اسرائیل گفت کمک‌خلبان این هواپیما پس از حمله با چاقو به خلبان دیگر، ظاهراً تلاش کرده بود هواپیما را با سرنشینانش سرنگون کند.
بنیامین نتانیاهو، در پیامی ویدیویی که روز چهارشنبه هشتم مهر منتشر شد، گفت: «در جریان پرواز، هنگامی که هواپیما به کشور نزدیک می‌شد، یکی از خلبانان به خلبان دیگر حمله کرد و ظاهراً تلاش کرد هواپیما را با همه سرنشینانش سرنگون کند.»
او مسافران هواپیما را «قهرمان» خواند و گفت آنها با اقدامات خود «از وقوع یک فاجعه بزرگ جلوگیری کردند».
نتانیاهو همچنین گفت عربستان سعودی کمک‌خلبان این پرواز را که به ادعای او به خلبان دیگر حمله کرده و تلاش کرده بود هواپیما را سرنگون کند، بازداشت کرده است.
او افزود: «خلبانی که دست به حمله زده بود بازداشت شده و اکنون از سوی مقام‌های سعودی تحت بازجویی قرار دارد.»
نتانیاهو همچنین دستور آماده‌سازی برای مقابله با تهدیدهای احتمالی بیشتر را صادر کرد.
یسرائیل کاتز، وزیر دفاع اسرائیل، نیز روز چهارشنبه این حادثه را «تلاش برای یک حملۀ تروریستی» خواند.
او در بیانیه‌ای گفت: «حادثه جدی در پرواز فلای‌دبی یک تلاش برای حملۀ تروریستی جهادی بود که تنها به لطف شجاعت چند مسافر اسرائیلی خنثی شد؛ آنها وارد کابین خلبان شدند، تروریست را مهار کردند و با دستان خود کنترل هواپیما را به یک خدمه پروازی دیگر که در آنجا حضور داشت، بازگرداندند.»
رسانه‌های اسرائیلی روز چهارشنبه از احتمال ربوده شدن این هواپیما خبر دادند اما بعداً گزارش دادند که «بروز درگیری فیزیکی بین خلبانان» در هواپیما باعث تغییر مسیر و فرود اضطراری آن شد.
بر اساس این گزارش‌ها، این هواپیما از نوع بوئینگ ۷۳۷-مکس کد اضطراری مربوط به ربوده شدن را ارسال کرده و پس از آن ارتباطش با اسرائیل قطع شده بود.
به دنبال این اتفاق جنگنده‌های اسرائیلی به پرواز درآمدند و فعالیت فرودگاه بن‌گوریون نیز متوقف شد.
ویدیوهای منتشرشده در شبکه‌های اجتماعی که رویترز محل ضبط آنها را پرواز FZ1073 تأیید کرده، مسافران را در حال رسیدگی به دو مرد مجروح در کف هواپیما نشان می‌دهد که دست‌کم یکی از آنها لباس خلبانی بر تن دارد.
در یکی از ویدیوها، یک مسافر اسرائیلی درخواست کمک می‌کند و می‌گوید مسافران «تروریست‌ها را مهار کرده‌اند». با این حال، مقام‌های فرودگاه تبوک و این مسافر هویت فرد یا افراد مهاجم را مشخص نکرده‌اند و جزئیات دقیق چگونگی درگیری هنوز روشن نیست.
بر اساس اطلاعات وب‌سایت فلایت‌رادار۲۴، این پرواز ابتدا یک پیام اضطراری عمومی ارسال کرد و سپس پیام اضطراری دیگری فرستاد که احتمال «مداخله غیرقانونی» را نشان می‌داد. هواپیما پیش از نخستین هشدار اضطراری، در کمتر از ۳۰ ثانیه نزدیک به ۱۴ هزار پا کاهش ارتفاع داشته است.
به گزارش این وب‌سایت، هواپیمای بوئینگ ۷۳۷ که رسانه‌های اسرائیلی اعلام کردند حدود ۱۵۰ مسافر اسرائیلی را در خود جای داده بود، بار دیگر پیام اضطراری اولیه را مخابره کرد و سپس در فرودگاه تبوک در شمال‌غرب عربستان سعودی به زمین نشست.
از سوی دیگر، شرکت هواپیمایی فلای‌دبی، مستقر در امارات متحده عربی، اعلام کرد علت درگیری‌ای که «در کابین خلبان پرواز FZ1073» رخ داده، همچنان مشخص نیست و موضوع تحت بررسی رسمی قرار دارد.
سخنگوی فلای‌دبی در بیانیه‌ای گفت: «در این مرحله، دلایل و انگیزه‌های اصلی این رویداد مشخص نیست و همچنان در چارچوب یک تحقیقات رسمی در حال بررسی است. از همه طرف‌ها می‌خواهیم تا زمانی که مقام‌های مسئول در حال جمع‌آوری اطلاعات و روشن کردن ابعاد ماجرا هستند، از گمانه‌زنی زودهنگام خودداری کنند.»
خبرگزاری رویترز به نقل از مقام‌های اسرائیلی اعلام کرد کمک‌خلبانی که این حادثه را رقم زده است، شهروند عمانی است. دولت عمان هنوز درباره این موضوع اظهارنظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/78575" target="_blank">📅 19:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEoKJAUb4aIOu-UGhe8zGpKpRhQRzrNztVQixRq4bQcZ21kNar3iO3uVs6ahZdrN9VByQnR54srhEfHK5Mv3mc6YbKopo9RYQyZE2F21cwxL9qmOXEf_niF171fkEoUlukC-Cbslhus7Bygxn2xF188tR9Mv5hZw9iX7tHehFSUeG2NBoDOMKn-9peSVC94ui77_ixX9EuDCTlW8Qqjxg-ceWSKnVdPDS5D2s2NjsOhqXISMru5BWzVDZ1XkobyVyszjmcvVlGqwHmRoGRBpOtArIpT1Qn6UM_c0W1gXmgJAQJ1_PD5hGLB5PMgdwX0-gfAnXGu8HQryvLVe487jhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KcEb9rDFQ9K3CUctQNiR4Df9D-NSpvM90J9tjaZuHzppNt1GAB1GDv8uQ883FeBRRIAWj7wvsq_vGRJNC-ML32BnMJoDd7mYK6_W1xhRX54dfe7AJLVdGWDt4AEiOzaz9ZCTbHig7oPclNs-4jmxlim9FZO_PC2Cm5yuDRf1s3Efclg7Pa7W6YjtbVg5puM39H60f7exr8FN0W64GOtAnJVFQ0YFacxYeo_j-ilTIHOkIDfL-0EM7tE61PPM2mphNlJ-c6fcqGVCtFjJOtnGu-AyzCibLRu9ioc6WhcnNpUXb_sCFd0_taMzycgLWOcLtJmw8WN_MYizsuXgiSXobA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XSFdmAOYbkjT4_EN9Lw19cpEl6wgsjNEM1km5-BtiYqgukbzK6R-ewjcl1pZrocS72hba09n8guZO-28gC-KPGvAwauh7SUlhddlmvez9SM8O4-TQxbB6xdmm1mxhkjhET4TU0xWSJC8JXYCT_RhG7Trd06K4KxZRgaSKfxxqoqjAwEqLqNfL0Ff6CxwWjP4viAcP5WRMLwrw7OAIo3zWudcJISUwEz0qeZpTMZjVaYNnjdZTecL7ay59cm8gQW5CcuwnNsJ3xYwnMh2QooSP6NtlbY4_g2GPJ7TqGbzkFSOl0ANig-eEK_q_rAKmZMDpON0H9MpXCvLtBAVWNlScg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5lyM4fZzZx9U_eYXik09mZaQL1E0wTflCAkxo6HKZmJ-U9tQUKsS24rVFMbhFbigHhhlqXJWKlewZ6voj4dlruqO2a9hNob6MtPtTx4bBRkrW3qH6Yj6_Lv0SbYHvT4uqIXCcXx0tGkUW6dGOux9cfB4Nfqs8y07uUajnlCRan0f0pyGeRMI74tLe1Ef_O5EEpBA7M4JfK06ce_NlGkn_tG6Ozt65koIsjoXyn_iaWA7ZyNmKxY3Y05tzlY2t3WGhdlBVkK8D_jP_WVmj4rybBK-rLMQeBYmyDWBrghTBCozYrKHVFEBMjJhhy6Frg3oY0O1odS4Eb2qUW2fB42NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
«برای کمک به پدر مجروحش رفت که  هدف گلوله قرار گرفت»
🔸
هفت روز طول کشید تا خانواده محمد عباس‌زاده بتوانند پیکر تنها فرزندشان را تحویل بگیرند. در این مدت، بارها به مراجع قضایی و نظامی مراجعه کردند، اما پاسخ روشنی دریافت نکردند و تنها به آنها گفته می‌شد منتظر پیامک بمانند.
🔸
فشارها پس از آن نیز ادامه یافت. برخی از بستگان احضار شدند، از اعضای خانواده تعهد کتبی گرفته شد و مقام‌های امنیتی برای نحوه برگزاری مراسم و حتی روایت چگونگی کشته‌شدن محمد برای آنها محدودیت تعیین کردند.
🔸
خانواده با وجود این فشارها، پیکر محمد را در زادگاهش اهواز به خاک سپرد؛ در حالی که پدر مجروحش هنوز در بیمارستان بستری بود و نتوانست در مراسم خاکسپاری تنها فرزندش حضور داشته باشد.
🔸
سرگذشت کامل محمد عباس‌زاده را در یادبود امید بخوانید.
https://www.iranrights.org/fa/memorial/story/-9241/mohammad-abbaszadeh
@IranRights</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78571" target="_blank">📅 19:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU83mBP3JyLYn-lzZze6RWLvymP9Dh8D0PP1a_epD2R_j4lZtE4-ARYx1fD3pwAeiGX8amGJBA3esMEuVV7U1YsX2LxiotqG4diuZ2hsuIHEspCZAvKIbFiVXHhg5ufRuIC1ZlewX0_mcBGzPh18AKFdSwzf5QlVFPg7pyi3ZOn6RGQrj5DC7WU2u8_jNVJwQ-6Az_F6vE0rzOuwj-v0PjzP-_3wFNZVg8VJyJ3ZEoaEzv8PA4j-mHaQ9mLP0Io7oPFauRS-6p7WA54tjpd5yLqEKQp0KALchpIq4wsPCmYvQTE3SmwhBdB72RY8nQOmZ3pD6-eJ2CiJ1xT9ea3-wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد دو نفر را که در اعتراض‌های دی‌ماه سال گذشته در مشهد بازداشت شده بودند، بامداد چهارشنبه اعدام کرده است.
بر پایه اعلام مرکز رسانه قوه قضائیه، علی همتی سیستانیان و مجید نیک‌اندیش پس از تأیید حکم در دیوان عالی کشور اعدام شدند. قوه قضائیه آنان را به دست داشتن در کشته شدن چهار نفر از نیروهای امنیتی در منطقه‌ای در مشهد متهم کرده بود.
در ادعای قوه قضائیه آمده است دو متهم در بازجویی و در دادگاه به حمله به یک فروشگاه زنجیره‌ای، آتش زدن آن با کوکتل مولوتف، آتش زدن یک بانک و تخریب اموال عمومی اعتراف کرده‌اند.
هیچ اطلاعاتی درباره روند دادرسی، دسترسی متهمان به وکیل انتخابی یا شرایط اخذ اعترافات منتشر نشده است. اعترافات تلویزیونی در پرونده‌های امنیتی جمهوری اسلامی بارها از سوی نهادهای حقوق بشری به اخذ تحت فشار متهم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78570" target="_blank">📅 09:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qrYMglmUGBH94H18Iqaqat74gcj532MRdlXGMl77q8UqdrGGVSsRNILPmbBTjK9IvV44jDvxDTwSEnw0_lWsRcIw5OXiIyqkQM1hTeho6a_UAu5FGlF8Dw0MfztxTNBIpzeyIbFQ43Kfln8SxmziulVO7nX32uHaF0UTo-dEzluAtNy29ALubCmF21N3geefqgodWjheEihNKvCe4qVnwX_kh3Kfe6Fn2wdBsUmUFBWPnXXgn4NJ_Xqvta4KEXFPyxtBhQuOA9fjxGzRdKK_txGvlddxqtaD7qp0IxsLRI9nw-u-ks9HCDWJA3Vv25_b_nu4mjybZD79du0JwGIMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/utg5ByFwkFyyzuMC677FlBDL2vhS7Izi3B1Mvk3wjAUV0-Wr7PPfgVVDi4hk88Ho3Rqa_2pXC6YO4I606YEzPbEk6qDWgngwQD7kBXdK74eeR2pJ32DUad_UII-vGGJERitA2Ar0z58dxoQ9m9qlKUVzu3xlwulV9e630sjv9o-D_j67YjAxyfyvKO-jpVbwMjavUHNxAAO4cIdW3qxs81uRvcjKgKW8ix1FHJ6T1BhWgmA1rQwZJVEYibv75kStjnXfMPPbSDUxrFiUcg7nUjwojpYHXDkMuwgzwOUTcdHYPWgWWFO_9EMIhbIiCrdEiuRY5hwFSOMH8CvzFs4xww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن رضایی، دبیر "شورای عالی امنیت ملی"، در دیدار با شاهین مصطفی‌اف، معاون نخست‌وزیر جمهوری آذربایجان، با تکرار مواضع دیگر مقام‌های جمهوری اسلامی گفت: «ترامپ در باتلاقی گرفتار شده که نه می‌تواند مذاکره کند و نه می‌تواند بجنگد.»
او افزود: «شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است.»
رضایی ادامه داد: «آمریکا آینده‌ای در منطقه ندارد و ایران با قدرت در مقابل آن ایستاده است.»
@
VahidOOnLine
ساعاتی پیش از این عباس عراقچی در آستانه بازگشت از نیویورک به تهران گفته بود که ماموریتش در این سفر این بود که شروط ایران از جمله درباره بازگشایی تنگه هرمز را به اطلاع ایالات متحده برساند.
وزیر خارجه در جمهوری اسلامی گفته بود که «ایران در این خصوص طرح دارد، شروطش، کاملا عادلانه و منطقی است و اگر آمریکایی‌ها ادعا دارند که دنبال توافق هستند یا دنبال یک راه حل مسالمت‌آمیز هستند، ما این راه حل را معرفی کردیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78568" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f601498008.mp4?token=fGUlGfj1L4MbQVNfMasVt0yiNY7t5SSJQo_X1HH74EayD7q_7pyhFDT94UwKPZbnI7N5_Xl2jFmBtRF27_7kSYIAHOQDoghkJR8jkDQ0-6AarFawJGb5eCF6MHVav71woFF_pYVIppg0Lemw5n2cMbiMj43FKKroGvmhpFij2faw9Nk6dk0-kUFQi9U9BdooLQyUZ9l_6BLBTt6FcL696zVcpkXUWu-aNJfZf49Nr-RHo-3wXU9twR_BE9XRpz5V8vpYnRrbK7uwxoMHGsinraz781R-m0pVX01NgGc5mZXR-6fEoz9czKmcAfKMMSj3LpsXqHKIYN94BDskfWSCrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f601498008.mp4?token=fGUlGfj1L4MbQVNfMasVt0yiNY7t5SSJQo_X1HH74EayD7q_7pyhFDT94UwKPZbnI7N5_Xl2jFmBtRF27_7kSYIAHOQDoghkJR8jkDQ0-6AarFawJGb5eCF6MHVav71woFF_pYVIppg0Lemw5n2cMbiMj43FKKroGvmhpFij2faw9Nk6dk0-kUFQi9U9BdooLQyUZ9l_6BLBTt6FcL696zVcpkXUWu-aNJfZf49Nr-RHo-3wXU9twR_BE9XRpz5V8vpYnRrbK7uwxoMHGsinraz781R-m0pVX01NgGc5mZXR-6fEoz9czKmcAfKMMSj3LpsXqHKIYN94BDskfWSCrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، ترجمه ماشین:
و ایران سلاح هسته‌ای نخواهد داشت. آنها به‌شدت در حال شکست خوردن هستند؛ خیلی بد، خیلی بد. این وضعیت خیلی زود تمام خواهد شد؛ خیلی، خیلی زود. آنها سلاح هسته‌ای نخواهند داشت و قیمت نفت هم به‌شدت پایین خواهد آمد، درست مثل قبل.
من مجبور شدم آن سفر کوتاه را به جمهوری اسلامی ایران انجام بدهم؛ سفر بسیار خوبی بود.
فکر می‌کنم در سال‌های آینده درباره این موضوع کتاب خواهند نوشت و تاریخ کشورمان را خواهند نوشت و خواهند گفت که این یکی از مهم‌ترین کارهایی بود که انجام دادیم. در واقع، این یکی از مهم‌ترین کارهایی است که در دوره دولت من انجام داده‌ایم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 368K · <a href="https://t.me/VahidOnline/78567" target="_blank">📅 19:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78566">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oLgURfMQEqHzBeIi4za03p1P4AIeTJGAnnQJyx0hRs1TiEPVoO0ck1GRg1sPSX52VFp1LhJA0_Y0m7Z9pU9eonxD1iz5HEZI7I_dBNWaCdGG7V1Ws5kn2GtjR8pq7ulpSEvNoxyGkS3hXZdXGfyEWIX9yP7hTsP_Dp-JiC3Kb53RdMBlsX_eW0-OVIXgCfEQm935VskC10yEBZH82hp9Yvcfzaf6TYMSkizUHIpPiFvfo_jI_00pzqbfur-me9PMjfDtbmrBxY2sW0LKAkuG3sB_R8zEKOEB9SOd765bU_cf_MxGMbqox3IbGtkVoebid8nUyPyfHZKG3ESiuP3MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ونس: ایران با نقض تفاهم‌نامه اسلام‌آباد مرتکب اشتباه شد
جی‌دی ونس، معاون رییس‌جمهوری ایالات متحده، در مصاحبه با وینسنت کُگلیانیز، پادکست‌ساز و روزنامه‌نگار محافظه‌کار آمریکایی، مقام‌های جمهوری اسلامی را مسئول فروپاشی تفاهم‌نامه اسلام‌آباد معرفی کرد و گفت آن‌ها با هدف قرار دادن کشتی‌های تجاری در آب‌های منطقه مرتکب اشتباه شدند.
ونس افزود: «فکر می‌کنم ایرانی‌ها متوجه شده‌اند که اشتباه کردند. آن‌ها با ما توافقی امضا کردند، آتش‌بس برقرار شد، قیمت انرژی کاهش یافت و این امکان وجود داشت که اگر ایرانی‌ها به تعهدات خود عمل می‌کردند، از بهبود روابط با آمریکا منافع زیادی به دست آورند.»
او همچنین به ابهام‌ها درباره وضعیت مجتبی خامنه‌ای، رهبر جمهوری اسلامی، اشاره کرد و گفت واشینگتن با قطعیت نمی‌داند که او زنده است یا نه، اما شواهد موجود نشان می‌دهد که همچنان در قید حیات است.
ونس ادامه داد: «ما فکر می‌کنیم او زنده است. البته با قطعیت نمی‌دانیم. من هرگز او را ندیده‌ام. اخیرا هم تصویری از او در مقابل دوربین ندیده‌ام.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78566" target="_blank">📅 19:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UZaLkiEEmKRWvwRMD60Jlovs2nB7raEgiynX-cpErCS-iuQT4wElMCF0FBsegO2Cf1jkvqBe2B_veVMP4Wo5TRmbdrfZOXptkfyfMbTnj-PB5meaYDvBxNyOhtK_GL6NzW4dOVuqO88sgBpaXKaM2tynwMaIBXWLtqcHAhMFaynzOau87mQkFqYovyNrs7Q1En2KR6-pNi6QDO39sV1sBr3T0gFQBf5setbUxHHIlwrhb7N8tzxeZVA_FWF5hfE_kzQiS0hH3uH9-HZHCyY7vuscEW_lo2FtADZsPaUjO83psw6CRZNQax99_wXboVoWueBpJY9DiSPGTLY80ZiDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ دلار در بازار آزاد تهران امروز از ۲۵۳ هزار تومان گذشت و رکورد تازه‌ای ثبت کرد.
بر پایه داده‌های پایگاه‌های اطلاع‌رسانی طلا و ارز، دلار در ساعت ۱۴ و ۳۰ دقیقه به وقت تهران ۲۵۳ هزار و ۱۰۰ تومان، پوند بریتانیا ۳۳۵ هزار تومان و یورو ۲۸۷ هزار و ۵۰۰ تومان معامله شد. سکه تمام امامی ۲۴۹ میلیون و ۵۰۰ هزار تومان، نیم‌سکه ۱۲۸ میلیون تومان و ربع‌سکه ۶۸ میلیون و ۵۰۰ هزار تومان قیمت خورد.
دلار دیروز ۲۴۴ هزار تومان بود، یعنی در یک روز بیش از ۹ هزار تومان گران شده است. نرخ ارز سه‌شنبه گذشته حدود ۲۳۳ هزار تومان بود و در یک هفته ۲۰ هزار تومان بالا رفته است.
دلار در ششم مهر سال گذشته ۱۱۱ هزار تومان بود. بهای ارز آمریکا در یک سال ۱۲۸ درصد بالا رفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78565" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnF5ty8QRcvKE0e_Js6D88EsJDQuLTLxL9l3zsudOItZ5kIXZpUPEvNrOeGa3DchBv_-yle-0UdiS7q_d6CExWgkzrum7rmOYcb49jN8CO432YBobP2jqRQ3ABXZL8cceCyN_hmMDxCxNNXLns_t5ndvBMz83n_EDO3l2N3s0Gjjhu5nJVMenx0fB9K6LFPGyFogAHCQdr546LODhrXzoHy4egDOoVb3GWQ7lmsl-9dYLH3XNxHoBmqXkmcPl4umC3w-37CybX49g-QQVZk58-XIHFtIcJ1k3eoMxvD1SBqPBJXkFJ0XJlMhCWcTtn4N_rWee9-2B_eQtYqIROss9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم از توقیف یک فروند هواپیمای مسافربری شرکت هواپیمایی کاسپین ایران در ترکیه خبر داد و دلیل آن بدهی سه میلیون دلاری عنوان شد.
بر اساس این گزارش هواپیمای توقیف شده بوئینگ ۵۰۰-۷۳۷ بوده است.
این هواپیما زمانی که برای پرواز از استانبول به تهران آماده می‌شد با حکم قضائی متوقف شد و مسافران مجبور شدند پیاده شوند.
شرکت خدمات هوانوردی «تمسیل گزتیم» می‌گوید کاسپین حدود سه میلیون یورو به این شرکت بدهکار است.
بر اساس این گزارش، این شرکت حکم توقیف را از دادگاه گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78564" target="_blank">📅 17:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W6cwWQYXyIj5fWFoeHu5ANHKojqoE0X2H2D6iqfECMBiPiBc5VkjXLg6Cxk3iPHMYWphX1SsZexHkthCinBtoUtLdftjcjpvFcL2Tb9HiyheE3caqkjOjdbOi0Q4V_pzAtfD4kiUkxJ6ZbxDWl8WbJMl1w81RvFGg1Sy3al4C0aFlg8IGEqAgFd-fT7xlKangbTN5E3w_riHJ0rj8R9XfkG9LqQOvLWqXfE0WOrBAbeJTXL-_ppui2pWqdSOwskseLUIyUtbYSo0YmKcPJnapyjKqP93ZiWsAt7xUHW-clh_NL4J9IlStma6bBPPFSeerhSyqojz46WTADRmudvM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/cLd8Nm8D6JlrYMh4MGP7mxHQcH8BoeEdC83Ghznm_WecMgC_31ce2vO9NWvbtgTEy4-G56Csr0R1xzEZfVuO-fXUi4jyP266VjUs51Q7Z5udsdakVDjboAOZDitCJmHmhp3pJzD3CcDj9eJbZ1tBGsiHFYkfwOT_jpSeCb0iwHKamXfmKtDsmijG5NiCMMpSOw7sOCm3APo0u89cytrV72wTN-mzHvJ6gzBtSliclcYly7ciSDGO7IjfTkoDAnfPujY8Y2LSwFnDXYVUSyVnQU9gqLOvg7TNr1LV9Pq87oYyDaWIIQGn7CCVo6Zb1WHF5mF4pPnTlHybL7Udve4TZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی روز سه‌شنبه ۷ مهر متن نامه‌ای خطاب به مردم آمریکا، دانشمندان، دانشجویان و اصحاب رسانه این کشور منتشر کرد.
در بخشی از این نامه که به زبان انگلیسی نوشته شده، آمده است: «حساب خودتان را از اشغالگران فلسطین که خواه‌ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید! ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.»
سپاه که در دوره اول ریاست جمهوری ترامپ در فهرست سازمان‌های تروریستی آمریکا قرار گرفت، در این نامه از آمریکایی‌ها خواسته است «در برابر سیاست‌های دولت خود موضع بگیرند» و «امور خود را به جای اراذل به اندیشمندان بسپارند.»
@
VahidOOnLine
حسین محبی، سخنگوی سپاه پاسداران، در نشستی خبری با خبرنگاران خارجی درباره نامه سپاه پاسداران به مردم آمریکا گفت در این نامه درباره «میزان محبوبیت» سپاه پاسداران در ایران و خدماتی که به گفته او به مردم ایران و منطقه ارائه کرده، توضیح داده شده است.
محبی گفت: در نامه خود حقایق ژئوپولیتیکی را برای مردم آمریکا روشن کردیم.» او افزود: «از مردم آمریکا خواسته‌ایم که نامه ما را حداقل یک بار مطالعه کنند.
سخنگوی سپاه پاسداران گفت: هیات حاکمه آمریکا به مردم خودشان دروغ‌های بسیاری می‌گویند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78562" target="_blank">📅 17:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GFLmV7KvF0TiA6d5JMUHKw8OKgLx5wojz-LPMaBhGNbiJ3lhbkQ50bXkOOISGjW-yFop_BbrGD2VEDz0U2XwIrnz7M11mai-dgGGpB_jyCKtl7YxKInlksiZBRORLUtGwA_ATySbfMVWbjJxPpG0UALjjKu6rABqyEu1MwSXtKrPOvPW-xo9mCpAJ67BSvLTZakNgNqO9e8QSMBHB9qlHq88zTNrgq6CGld-9e-yFnh6FmXqBjIIEsbIke20WYT8sDS_t63EkSOaxk92bLUsyhhxFgHqPzvLNfZkznVCy9kBSWuK7SsQHFiRVK30r0rxLU6u-wgNxanr8ry3pJV8KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/krS8sYY2VDAgcOGj40rI2AnCvH75BdjPWPyM2_PstPA9yGHgAeh615RrG6jMnBJOq3gBYQMatOLbM1b6AC6oywBzPptNMgv8D-Rv8aDHEu24G-GNVYL5ff5eRys856lc7NXgEUfL8mC34sbyIpA2WPNd6RChyiAAuZ7VPwrEWDIRKGF-jokhJQHqS7CINdp0L24EJkbdxC36sn2g-QyTxsWkdrjBHda3jcRz8n7Q6awfjRCV26JO9BiJN2m2WLyztzwzdHTS-BzdljMWxXMU-C-89Re0ZRyIpULrQDM8Nd3asHNregpDmHFNglMBAvts8BwwWK4yVDd0kBlnlyDsgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمدباقر قالیباف، رئیس مجلس شورای اسلامی، سه‌شنبه هفتم مهر در جلسه علنی وبیناری مجلس، آمریکا و کشورهای منطقه را به حمله به زیرساخت‌ها و نفتکش‌ها تهدید کرد.
این در حالی است که روز سه‌شنبه جمهوری اسلامی در انتظار پاسخ رسمی آمریکا به پیشنهادات تهران است که دونالد ترامپ قبلاً گفته آنها را رد کرده است.
قالیباف گفت: «در منطقه‌ای که ما نفت نفروشیم، کسی نفت نخواهد فروخت و اگر امنیت ما تامین نشود، هیچ زیرساختی ایمن نخواهد بود.»
رئیس مجلس شورای اسلامی در عین حال مواضع دونالد ترامپ علیه جمهوری اسلامی در جریان مجمع عمومی سازمان ملل را «سبک‌سرانه» خواند و به او گفت: «بچرخ تا بچرخیم.»
روزنامه خراسان، نزدیک به محمدباقر قالیباف، هم نوشت: «اگر مذاکرات به دلیل اختلافات هسته‌ای به نتیجه نرسد، جمهوری اسلامی فرصت استفاده از نقشه دومش را خواهد داشت تا به انجام حملات پیش‌دستانه روی بیاورد و یک دوره جنگ پرفشار را قبل از پایان انتخابات میاندوره‌ای به ترامپ تحمیل کند.»
شماری از نمایندگان مجلس شورای اسلامی نیز دیگر کشورهای منطقه را به حملات جمهوری اسلامی تهدید کرده‌اند.
از جمله علیرضا سلیمی، عضو هیئت‌ رئیسه مجلس، در گفت‌وگو با خبرگزاری خانه ملت گفت: «باید پذیرفت که امنیت در منطقه یا برای همه خواهد بود یا برای هیچ‌کس».
او افزود که جمهوری اسلامی در برابر هرگونه اقدام تخریبی در منطقه «تماشاچی نخواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/78560" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=mAH72XXf_ZOdSBZTO3rmFcZEnKTu1WQZVIH3plHzaiagQA55HuposSpGsV5WV1Y0PYqhBf_eWHQC1uPeXfZDo38ZH7ht3K9dzb7xQsWqsKO6gysea8EM1FOO_P9Ishwyv0L5_CDASMpdtgIb4VYiK30cxSfb9vH4I5cWthUUiQsdwbBz5vpM8EjM7E3KQyn0j1rGNlxJ3gx-8AxTqcEplWedsilk8zrZfPHWXeaCYR1CBGqgd1zRyo2PNxjrsMC940jGME9-QTh4RjDbQ51S7_nYQN43OgMri54Si9AhBXBzptyl0pkPp9m4NVsBCcHyX2NZAq-lS6OHNye4DOdeiLlBKFIOgzY8ZZ8MFQLmtFjV-ka0pxDMH9vmx-7mzCUpg2SyZzwxncubs3o6rR6mBO2h8yxxghXVZkeKlqYWNKrvl40aAU6fcoskGuTM_3FU1MvW1QEZD_ju7byNgG8vRf2jWfdBAqOXmeqs7zCSUDMlFr10CnMkPLMyd1c47kLECuZMVGdkxCVNoQOjmFeyZ6RxaUf3sFLMWdrYc5zRoHozLXySvZlCnzySuAXiKDuzXewol_N6Jhb5i16GwB3jpAHaVy7JSds7HlEtkIXn8U-LMsBnbPWzxVpdWA0fxM2VkRAreqWg2B1oqUhvYzKpRGdyFeW2bXufUGIW-flsm2E" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1d7707475e.mp4?token=mAH72XXf_ZOdSBZTO3rmFcZEnKTu1WQZVIH3plHzaiagQA55HuposSpGsV5WV1Y0PYqhBf_eWHQC1uPeXfZDo38ZH7ht3K9dzb7xQsWqsKO6gysea8EM1FOO_P9Ishwyv0L5_CDASMpdtgIb4VYiK30cxSfb9vH4I5cWthUUiQsdwbBz5vpM8EjM7E3KQyn0j1rGNlxJ3gx-8AxTqcEplWedsilk8zrZfPHWXeaCYR1CBGqgd1zRyo2PNxjrsMC940jGME9-QTh4RjDbQ51S7_nYQN43OgMri54Si9AhBXBzptyl0pkPp9m4NVsBCcHyX2NZAq-lS6OHNye4DOdeiLlBKFIOgzY8ZZ8MFQLmtFjV-ka0pxDMH9vmx-7mzCUpg2SyZzwxncubs3o6rR6mBO2h8yxxghXVZkeKlqYWNKrvl40aAU6fcoskGuTM_3FU1MvW1QEZD_ju7byNgG8vRf2jWfdBAqOXmeqs7zCSUDMlFr10CnMkPLMyd1c47kLECuZMVGdkxCVNoQOjmFeyZ6RxaUf3sFLMWdrYc5zRoHozLXySvZlCnzySuAXiKDuzXewol_N6Jhb5i16GwB3jpAHaVy7JSds7HlEtkIXn8U-LMsBnbPWzxVpdWA0fxM2VkRAreqWg2B1oqUhvYzKpRGdyFeW2bXufUGIW-flsm2E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"#سپهر_بابا کجایی؟"
⚠️
۱۲ دقیقه ویدیوی دلخراش از مرکز پزشکی قانونی کهریزک تهران پدر «سپهر شکری» به دنبال پیکر پسرش Vahid نسخه ۴۰۰ مگابایتی: twimg  آپدیت دو روز بعد: #سپهر_شکری در پی گزارش دروغ صدا و سیما درباره این ویدیو و انتساب این ویدیو به خانواده داغداری…</div>
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/78559" target="_blank">📅 17:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uC66hSQfHOBYRElqui2UDWpnroT-mn_MAwOMzvxbRhpBZIF-gJzhMdSOmoDLcWxuDMvRt1MZThuF_zxIz5QCiF3rgbeiVbgg8Jb6vb31esNtpR977xal7mfzozrydbcHnIADYYnazdcUmMrODlnDJ87bBNGjKwnFNe8BlmFSEPowjUsqo0lEhKAqH5hvuVotVY5MNNs5OwY7YlD2ZZ39D2MVtDUH1LS-W3h3Ce4B8oRlXDS4O8IgKGsiCuO8PPb8nI721VqDJGN8EFFoYBlZA27fweqNc2mEk_5Qh37772yzcxHLiLC3VrboBUzzkRFf1ZBmXorj4vindkomfGq9NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CcFc3N71_pUjFjwQvvBQ-9ue_gVgjbUPthSqwqlnkFq-TcVlHgu-GquaoGQ5ShidWS27AlXdZkGj1oeZRlTmolOVK3tobVHQYMQ_-qmjnF4tupwitJMGdJgawEbaQS6-vnx2Xq3bAu8in7I_WbxBdlYPSb9WK4m9rUcbIHyCVQ17oQkXG2Oqd0qgXWtN73ZqBog2VfUfFiaNph6GVcnrT8Li3P0XJupH9sHNiQ-PrNEEMxitxh8g82i-ph51SSf_Mvs6Z3Tqb4IAkJv3idomue5ABdQew1j_4MTm9Y0SactodQaX6O52Qob3Jzbx_aPOauFlIiwAlJNrqCZNdtWC4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، روز سه‌شنبه هفتم مهر در گفتگو با شبکه فاکس‌نیوز گفت رژیم ایران پولی را که به دستش می‌رسد خرج مردم نمی‌کند، بلکه آن را صرف ساخت تسلیحات و صدور انقلاب می‌کند.
او با اشاره به عملکرد تهران طی سه دهه گذشته افزود: «مسئله صرفا تحمیل هزینه‌های اقتصادی بر این رژیم نیست. پای هر دلاری که ایران در اختیار دارد در میان است. آنچه آن‌ها در ۳۰ سال گذشته انجام داده‌اند این است که هر زمان پولی به دستشان رسیده، چه در چارچوب رفع تحریم‌ها در دوره اوباما و چه از مسیر فروش نفت و گاز، آن را برای ساخت بیمارستان، جاده یا بهبود زندگی مردم ایران خرج نکرده‌اند.»
روبیو در ادامه گفت: «آن‌ها این پول را تنها برای دو هدف استفاده می‌کنند: ساخت تسلیحات برای خودشان و صدور انقلاب. آن‌ها این منابع مالی را برای تامین مالی حزب‌الله، حماس و شبه‌نظامیان شیعه در عراق به کار می‌گیرند. آن‌ها این پول را برای حمایت مالی از تروریسم و طرح‌های ترور در سراسر جهان خرج می‌کنند و بنابراین هر پنی که به دستشان می‌رسد، پولی است که برای مقاصد این فعالیت‌های مخرب استفاده می‌شود.»
@
VahidOOnLine
مارکو روبیو، در گفتگو با شبکه «فاکس نیوز» با تاکید بر اینکه نباید ایران را با حکومت فعلی آن یکی دانست، گفت: «مردم اغلب این اشتباه را می‌کنند که ایران را معادل یک کشور عادی می‌دانند. بله، ایران یک کشور است، اما مشکل ما کشور ایران نیست؛ مشکل، انقلاب و سیستمی است که بر آن کشور حکومت می‌کند.»
او با اشاره به مقامات جمهوری اسلامی که با پوشش‌های دیپلماتیک در رسانه‌ها ظاهر می‌شوند، افزود: «کسانی که در ایران تصمیم‌گیرنده هستند، روحانیون تندرویی با دیدگاه‌های آخرالزمانی‌اند که باور دارند رسالت دینی‌شان رقم زدن روزهای پایانی جهان است.»
روبیو همچنین هشدار داد که دستیابی چنین رژیمی به سلاح هسته‌ای، یک خطر غیرقابل‌قبول برای جهان خواهد بود، چرا که از آن برای باج‌گیری و کشتار استفاده خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78557" target="_blank">📅 09:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZkhNPuCg5BE-Fvcm3nDOBqf0BlNq7bcZ6qHUDhdQ27bUnaEd8q1frPfQbIBd2HqKGqWTrvxNig9gWViC9x1JAhmhEKg2D3Vbe4iJeDXGjTkiDXaDsINEV3sP7UVKAwiJEmPj7Da_IcrFAhS-ur1vr4VKiEUU1Vc9P5uMbqjo7w1BADkGyIP0bWhlWDRzuT_sJTq33n1KTvaXvAWuMtlozdEPZBTIDaDy1WeOh-7M-k0vuCe0luTvPM-TdWgpxxXSjTr1vQ2LeaX55kYHW2WC9BlvR28S4C6TtFKN6KnOeFZ5VAqdzr8yTc5WXqRbGI_a_4Mk5fs0ebUlNXI1qGHaiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ، ترجمه ماشین:
اکسیوس همین الان
گزارشی
منتشر کرده که مدعی است «ترامپ» به ایران پیشنهاد کاهش تحریم‌ها و آزادسازی منابع مالی مسدودشده را داده است. این حقیقت ندارد. من به آن‌ها هیچ‌چیز پیشنهاد نکردم!
گزارش اکسیوس، مثل بیشتر گزارش‌های دیگر، یک حقه و دروغ است که فقط برای ارضای «سندروم جنون ترامپ» آن‌ها منتشر شده است. آن‌ها باید این گزارش جعلی را فوراً پس بگیرند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 393K · <a href="https://t.me/VahidOnline/78556" target="_blank">📅 01:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=BCv2GHB-oNRwNtks_P4hJjgfJC4odQcRC5PYsCSSo3113hqOHaoL-FJZLbtg-kZAL3iCemOKyv8eJd79Yzct8YJn-5krKN8hMmPU5sh_wZG911AyIXUrNCMYebrTvS63e9VmGNTFy1mxH7BfiIOZALjVcItGuJSEC8GTzCZtHkoyfyv_OZZeEaZyh26GsN0yPq5BHb0J7heEZeCYlk9j4hHekD08mMY2tb7IMz3oaQMwGOZok7CEQvTL_CZoshP-LWGvDXv933Vk5heZ6_ZDCUfUoePQily8B697oUAnOdTMX1M_rm84borvSkDQb0vcWseeA1HO9C4GzfyENzXSnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e65799ad06.mp4?token=BCv2GHB-oNRwNtks_P4hJjgfJC4odQcRC5PYsCSSo3113hqOHaoL-FJZLbtg-kZAL3iCemOKyv8eJd79Yzct8YJn-5krKN8hMmPU5sh_wZG911AyIXUrNCMYebrTvS63e9VmGNTFy1mxH7BfiIOZALjVcItGuJSEC8GTzCZtHkoyfyv_OZZeEaZyh26GsN0yPq5BHb0J7heEZeCYlk9j4hHekD08mMY2tb7IMz3oaQMwGOZok7CEQvTL_CZoshP-LWGvDXv933Vk5heZ6_ZDCUfUoePQily8B697oUAnOdTMX1M_rm84borvSkDQb0vcWseeA1HO9C4GzfyENzXSnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، روز دوشنبه ۶ مهر ۱۴۰۵، در کاخ سفید گفت آمریکا «خیلی زود» در جنگ با جمهوری اسلامی پیروز خواهد شد و پس از پایان جنگ، قیمت بنزین به‌شدت کاهش خواهد یافت.
ترامپ گفت: «این جنگ تمام خواهد شد و ما در این جنگ پیروز می‌شویم و قیمت بنزین با سرعت زیادی پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست چنین کاری را انجام دهد.»
او درباره برنامه هسته‌ای جمهوری اسلامی نیز گفت آمریکا مانع دستیابی تهران به سلاح هسته‌ای شده است و افزود جمهوری اسلامی این موضوع را می‌داند و حاضر است به آن اذعان کند.
@
VahidHeadline
متن زیرنویس، ترجمه ماشین:
ایران هرگز سلاح هسته‌ای نخواهد داشت. ما خیلی زود در آن جنگ پیروز خواهیم شد. آن جنگ تمام می‌شود و قیمت بنزین به‌شدت پایین خواهد آمد. هیچ‌کس دیگری نمی‌توانست این کار را انجام دهد. هیچ‌کس دیگری.
اگر دموکرات‌ها سر کار بیایند، مرز فوراً باز خواهد شد و میلیون‌ها نفر درست مثل قبل سرازیر خواهند شد. این وحشتناک‌ترین چیزی است که در عمرم دیده‌ام.
بله، آنها حاضر نبودند جلوی ایران را بگیرند که سلاح هسته‌ای داشته باشد. گفتند: «بگذارید یک نفر دیگر این کار را بکند.» البته این را درباره خیلی‌های دیگر هم می‌توانم بگویم. ما جلوی دستیابی آنها به سلاح هسته‌ای را گرفته‌ایم. آنها هرگز سلاح هسته‌ای نداشته‌اند و این را می‌فهمند و حاضرند آن را بگویند.
وقتی جنگ تمام شود، دو اتفاق خواهد افتاد. اتفاق اول در واقع همین حالا هم افتاده است: ایران هرگز سلاح هسته‌ای نخواهد داشت. این موضوع بسیار بزرگی است، چون اگر می‌خواهید آشوب و فاجعه ببینید، بگذارید آنها یک شهر را با سلاح هسته‌ای نابود کنند.
فقط درباره اسرائیل و بخش‌های بزرگی از خاورمیانه صحبت نمی‌کنم. نباید بگذاریم با سلاح هسته‌ای به ما حمله کنند. برای همه آن آدم‌های احمقی که فکر می‌کنند اشکالی ندارد، من با آنها سروکار دارم و آنها دیوانه‌اند. هیچ تردیدی در این نیست. آنها آدم‌های بسیار دیوانه‌ای هستند. همیشه این را به خودشان می‌گویم. می‌گویم: «مرد، تو دیوانه‌ای.» اما آنها نمی‌توانند سلاح هسته‌ای داشته باشند و ندارند.
پس این موضوع بسیار بسیار مهم است که ما در چنین وضعیتی قرار داریم. این کاری است که سال‌ها پیش باید توسط رؤسای جمهور مختلف یا کشورهای دیگر انجام می‌شد. لازم نبود حتماً ما باشیم، اما ما با فاصله قدرتمندترین کشور جهان هستیم. بهترین تجهیزات نظامی جهان را داریم.
و ضمناً، اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات نظامی تولید می‌کنیم. چاره‌ای جز این نداریم. شرکت‌های بزرگ دفاعی در حال گسترش فعالیتشان هستند. مثلاً لاکهید پنج تا می‌سازد. ریتیان هم تعداد زیادی می‌سازد. همه‌شان دارند مقدار زیادی تولید می‌کنند. اکنون بیش از هر زمان دیگری در تاریخ کشورمان تجهیزات در راه داریم و به‌زودی واقعاً تولیدشان شروع می‌شود، چون این کارخانه‌ها قرار است شروع به کار کنند.
قیمت بنزین خیلی پایین خواهد آمد و همین حالا هم، می‌دانید، اگر نگاه کنید، فکر می‌کنم پیتر، این صددرصد است.
پس ما ارتش ایران را از بین بردیم. تقریباً هرچه داشتند را از بین بردیم و هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ایران هرگز سلاح هسته‌ای نخواهد داشت. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که ما بدترین تورم تاریخ را داشتیم. هیچ‌کس درباره این واقعیت صحبت نمی‌کند که در دوره بایدن شما برای بنزین خیلی بیشتر پول می‌دادید.
بیایید درباره همه این چیزها، می‌دانید، همه‌چیز صحبت نکنیم. در دوره بایدن، شما خیلی بیشتر برای بنزین پول می‌دادید تا الان.
و کاری که من کردم این بود که وارد جنگ شدم تا جلوی چیزی را بگیرم که می‌توانست یکی از بدترین اتفاق‌ها برای جهان، برای ما و برای بقیه جهان باشد. اسرائیل الان نابود شده بود. دیگر اسرائیلی وجود نداشت. دیگر خاورمیانه‌ای وجود نداشت. و بعد موشک‌ها و بمب‌ها به سمت ما و اروپا می‌آمدند. و من جلویش را گرفتم.
و این آقا داشت ۱۸ میلیارد دلار در آیووا سرمایه‌گذاری می‌کرد. او می‌گفت: «من می‌خواهم از آمریکا صرف‌نظر کنم. قرار نیست ۱۸ میلیارد دلار خرج کنم»، چون ما یک دیوانه و یک کشور دیوانه داشتیم که با سلاح‌های هسته‌ای این طرف و آن طرف می‌گشتند، چون قدرت بسیار زیاد است.
اما هیچ‌کس درباره‌اش حرف نمی‌زند؛ هیچ‌کس درباره همه آن کارهای باورنکردنی حرف نمی‌زند.
باز هم، خیلی از شما... نمی‌خواهم بپرسم، چون می‌گویید: «اوه، ما قرار نیست این را گزارش کنیم. ما رسانه اخبار جعلی هستیم. اجازه نداریم گزارشش کنیم.»
همه شما حساب 401(k) دارید. لازم نیست چیز دیگری درباره شما بدانم. حساب 401(k) شما در مدت کوتاهی دو برابر شده است. دو برابر شده. ثروت شما دو برابر چیزی است که مدت کوتاهی پیش بود؛ تک‌تک شما، و این به خاطر من است.
خوش بگذرد، همه. خیلی ممنون.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78555" target="_blank">📅 23:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">"ترامپ در ازای امتیازهای مشخص هسته‌ای، به ایران پیشنهاد گشایش اقتصادی می‌دهد"
اکسیوس، ترجمه ماشین:
دونالد ترامپ، رئیس‌جمهور آمریکا، آماده است در ازای برداشتن گام‌های مشخص از سوی ایران در ارتباط با برنامه هسته‌ای، به ایران تخفیف تحریمی بدهد و دارایی‌های مسدودشده ایران را آزاد کند؛ مقام‌های آمریکایی این موضوع را اعلام کرده‌اند.
🔻
چرا مهم است:
پیام آمریکا به ایران در حالی مطرح می‌شود که میانجی‌های قطری و پاکستانی این هفته بار دیگر تلاش می‌کنند میان دو کشور در حال جنگ به توافقی دست پیدا کنند.
▪️
در حال حاضر، دو طرف بر سر مسائل کلیدی فاصله زیادی با یکدیگر دارند. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار آن است که ایران با امتیازدهی در زمینه هسته‌ای موافقت کند.
▪️
با این حال، این پیشنهاد پس از آنکه ترامپ آخرین پیشنهاد ایران را رد کرد، روزنه‌ای از امید برای دستیابی به یک گشایش دیپلماتیک ایجاد می‌کند.
🔻
تحولات اصلی:
میانجی‌ها امروز در نیویورک با عباس عراقچی، وزیر امور خارجه ایران، دیدار می‌کنند تا درباره پیشنهادی از سوی قطر گفت‌وگو کنند که طرف‌ها طی چند روز گذشته مشغول مذاکره درباره آن بوده‌اند.
▪️
انتظار می‌رود میانجی‌های قطری اواخر روز دوشنبه یا روز سه‌شنبه با مقام‌های دولت ترامپ دیدار کنند تا برای دستیابی به یک گشایش تلاش کنند.
▪️
یک مقام آمریکایی مطلع از مذاکرات غیرمستقیم، این گفت‌وگوها را «مثبت و سازنده» توصیف کرد و گفت ایران «نشان داده است که در مسائل هسته‌ای انعطاف‌پذیر است.»
▪️
اما این مقام همچنین گفت هنوز اختلاف‌هایی وجود دارد و تأکید کرد «تا زمانی که به مسائل هسته‌ای پرداخته نشود»، توافقی در کار نخواهد بود.
▪️
این مقام گفت: «طرف‌ها همچنان درباره زمان‌بندی تعهدات و اینکه چه کسی باید ابتدا کدام گام را بردارد، اختلاف دارند.»
🔻
آنچه می‌گویند:
این مقام گفت: «تردد در تنگه هرمز همچنان در حال افزایش است و محاصره و تحریم‌ها همچنان موقعیت ایران را تضعیف می‌کنند. موضع آمریکا هر روز قوی‌تر می‌شود و رئیس‌جمهور ترامپ همچنان صبور است و کاملاً به هدف خود مبنی بر اینکه ایران هرگز به سلاح هسته‌ای دست پیدا نکند، متعهد است.»
▪️
این مقام افزود که کاخ سفید نسبت به وعده‌های ایران بدبین است و ایرانی‌ها را متهم کرد که با شلیک به کشتی‌های تجاری در تنگه هرمز در ماه ژوئیه، آخرین تفاهم‌نامه را نقض کرده‌اند.
▪️
این مقام گفت: «آمریکا این بار به تضمین‌هایی نیاز دارد که نشان دهد ایران جدی است و صرفاً تلاش نمی‌کند از شرایط دشواری که در آن گرفتار شده، خارج شود.»
axios
🔄
آپدیت:
ترامپ تکذیب کرد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 404K · <a href="https://t.me/VahidOnline/78554" target="_blank">📅 20:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3aba301950.mp4?token=WFNmXaNeIRmsVtf6MjIvb860sI1LWe-z69e8oTtXdfK-1-goreM163sL1Vabyo2ao4P8uSdOqM3w7YJeIkR7zj64lQmLthkxQzNomBmYtxfwCuQncyTkqGDh83z5JljssyZEppNJYv5Ebjqfp2UQrNSlOtMmrlzpPXMeUPpB0EPi5fbtlvTswh32oUYWAepiy5gFGEYyH-yRqSgj0DrVoUHeR_qzaDVKiSug5VqmxXWTfzIAvWtp2s6Piq9PuEC8os2qgp8dab1sR9ihAFq6192DA5lhRMuWIQm8VxuQmCAbshckqCeDUQQxbak87ZbruLEzhPDBl-iJZRUTHeux6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3aba301950.mp4?token=WFNmXaNeIRmsVtf6MjIvb860sI1LWe-z69e8oTtXdfK-1-goreM163sL1Vabyo2ao4P8uSdOqM3w7YJeIkR7zj64lQmLthkxQzNomBmYtxfwCuQncyTkqGDh83z5JljssyZEppNJYv5Ebjqfp2UQrNSlOtMmrlzpPXMeUPpB0EPi5fbtlvTswh32oUYWAepiy5gFGEYyH-yRqSgj0DrVoUHeR_qzaDVKiSug5VqmxXWTfzIAvWtp2s6Piq9PuEC8os2qgp8dab1sR9ihAFq6192DA5lhRMuWIQm8VxuQmCAbshckqCeDUQQxbak87ZbruLEzhPDBl-iJZRUTHeux6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غلامحسین محسنی اژه‌ای، رئیس قوه قضائیه جمهوری اسلامی، روز دوشنبه ششم مهرماه از دادستان کل کشور و مقام‌های قضائی خواست تا با آنچه او «وضعیت برهنگی» توصیف کرد، «قاطعانه و با برنامه‌ریزی» مقابله کنند.
اژه‌ای خطاب به مدیران قضایی گفت: «نباید از هیاهوها ترسید... رئیس جمهوری هم با مقابله بابرهنگی موافق است. مجلس هم قطعا موافق است که این بساط برهنگی جمع شود.»
جمهوری اسلامی در زمان اوج جنگ تصاویر زنان بدون حجاب حاضر در تجمعات شبانه حکومتی را به‌عنوان حضور ایرانیان از اقشار و افکار مختلف، پخش می‌کرد و در اختیار رسانه‌های بین‌المللی قرار می‌داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78553" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUB6vCzgh3U_mGlEX8hhhCMMmq3F9EJGjtXERt6OSZvPV-FwOk3aVQjA0j6RgJNHnK_geyYr9hqzHETCyVWdiJKm9djXktuftVf6Uym6IlQBPTCnUwgd0xJ4q2LH83V8Ub1SIjbwRgW-LD7kdG0ybHRuxtf3SZqe_DNBYB6qPgStl6YUoLdI4duy5WXDTjkjnfaB7Lr3U0ar340TCCMVad4K62rJUtqDRAGbzzIqUyuzHEwXnN3bUVCXRPpbzhLCZMZUAzukoYSsjXUHPYVwYYthdV32rIxDkYQezGV9i3lZreHfhquv7xzlNio7onjYEMUKVCv5-0_ADj-AqlwoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مایک والتز»، نماینده آمریکا در سازمان ملل متحد، گفته است واشینگتن پیشنهاد هفت‌روزه ایران برای آتش‌بس و بازگشایی «تنگه هرمز» را به دلیل شروط تهران، از جمله «دسترسی به میلیاردها دلار دارایی مسدود شده» و «لغو تحریم‌ها»، نپذیرفت.
والتز روز یکشنبه ۵مهر۱۴۰۵ در گفت‌وگو با شبکه «ان‌بی‌سی نیوز» درباره دلایل مخالفت دولت «دونالد ترامپ» با پیشنهاد ایران گفت: «آنها میلیاردها دلار پول مسدود شده می‌خواهند و خواهان لغو تحریم‌ها هستند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78552" target="_blank">📅 16:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bt3yzBgA0dDQHGRVN92CYNUJUggUggVba74jjUJgz5kq6RyqPGNDSNPCFSp4wdz3_K9UFGKYPbjXfnHT9o5ygXzoI37argtlEI0FGGM2rhNqonTAlBDMyy1otaXEajaXhZQxJftEdDql5yBsBqkvf-ZWJNrQi_uabTmqySOzDUWZmNjqd1bl0N8L9ycl0Nn_RcJBx11SDaOkKSRNN8K2tLYAOXQ1UqpNa2Ix9Exa9S-Qa-48IN8Mn2UKJWRrRjVI4BSA2rX8_6sCEkzQX6KO5RyIhxRm1RzJcNh5_wxir56NSYvDtqEAqT_q_IYVP3L8RXeA2paIi7ui7yRDv9FGKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت ارز در بازار آزاد ایران روز دوشنبه ششم مهرماه تنها در چند ساعت بیش از ۶ هزار تومان افزایش یافت و دلار از ۲۳۶هزار تومان به ۲۴۲ هزار و ۵۰۰ تومان رسید.
سقوط آزاد ارزش پول ملی ایران، همزمان با تشدید تنش میان تهران و واشنگتن و در حالی که تحریم‌های همه‌جانبه و بی‌سابقه آمریکا علیه جمهوری اسلامی ایران ادامه دارد، وارد مرحله جدیدی شده است.
سایت‌ها و کانال‌های اعلام قیمت ارزهای خارجی گزارش می‌کنند که روز دوشنبه، یورو به مرز ۲۷۶ هزار تومان رسید و پوند بریتانیا هم رکورد ۳۱۸ هزار و ۶۰۰ تومان را شکست.
@
VahidOOnLine
قیمت دلار در بازار آزاد ایران ظهر امروز دوشنبه ۶مهر۱۴۰۵ از مرز ۲۴۳ هزار تومان عبور کرد و رکورد تازه‌ای بر جای گذاشت.
اما خبرگزاری «فارس»، وابسته به سپاه پاسداران، افزایش نرخ ارز را به اظهارات وزیر خزانه‌داری آمریکا، کانال‌های تلگرامی و فعالیت دلالان نسبت داده است.
دلار صبح دوشنبه از مرز ۲۴۰ هزار تومان گذشته و تا ۲۴۰ هزار و ۵۰۰ تومان افزایش یافته بود، اما تنها چند ساعت بعد قیمت آن از ۲۴۳ هزار تومان نیز فراتر رفت.
@
VahidHeadline
به نوشته هم‌میهن، قیمت سکه معروف به امامی نیز روز دوشنبه در کانال ۲۴۳ میلیون تومان قرار گرفته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78551" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWhuNrnqeUAYCdqXJ6DP-udDO0sp2LDiJ4x2wClIYXUyLFHdjXzVYzAVjitVFGbtQC7MU03vr2VDGEGmtHWROi5TE8PebhS2sGOYk_H2vV1v69RHWNFEscNB6wo0V-L02HbtHNjEKKPGyIq3ptK5jMDaQNczVzVTT62WDcQdOruvF6DY_9uNC63n4qNI-Zb0-OXeIWCc16HCoHuXvKUgZQfUztXPzIyh95u2M85lZ_-HUVwGPjcom2MfBQK-fEFKLeoHgGYLdCuaXHfwYKbbDSwYN0Ew3tZZlRRAfDptjyq9NCmYb2XdGx0-WkPACK_8S7OftT5daAuKZP-js8_F8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ که به‌تازگی به اعدام محکوم شده، امروز دوشنبه ۶مهر۱۴۰۵ به سلول انفرادی زندان «وکیل‌آباد» مشهد منتقل شده است.
خبرگزاری «هرانا» گزارش داده مسوولان زندان با اعمال خشونت، محبوبه شعبانی را از بند «آرامش» خارج و به سلول انفرادی منتقل کرده‌اند. دلیل این اقدام تاکنون مشخص نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 327K · <a href="https://t.me/VahidOnline/78550" target="_blank">📅 16:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=oPdKxDEhTf7y7R-MOuyNIJwKT_lCs__f7ity_A7Okw7YAf3QzAsCXQTMAuWMQDYS5nj0CaCMDQGeNq0UMuLeGVCJsk6TqJn8qWJ1I9CEIyppAUXC6QPTIYBDgOKYRKi9xulMf0-oRp59Kro5FkwsYh1_UriLDbEfQki_Y72S7in54w0sCnVPTWRehHh0f2pHlWr2FCCRqc7-wDjZPDFbkkJpUW3Ubi-r3ZxKaqlxIkd_4pZusi1Nf7QSgKUvW2EzjeLoFvf8NFzvXNU47Q6Kdn5x7BxD-ceaSHNyVWYxc_B9Fo-IOvknMPPOEv9kvg2Nf4L_9tfYBX7NH2oytSG4Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16f966f0d3.mp4?token=oPdKxDEhTf7y7R-MOuyNIJwKT_lCs__f7ity_A7Okw7YAf3QzAsCXQTMAuWMQDYS5nj0CaCMDQGeNq0UMuLeGVCJsk6TqJn8qWJ1I9CEIyppAUXC6QPTIYBDgOKYRKi9xulMf0-oRp59Kro5FkwsYh1_UriLDbEfQki_Y72S7in54w0sCnVPTWRehHh0f2pHlWr2FCCRqc7-wDjZPDFbkkJpUW3Ubi-r3ZxKaqlxIkd_4pZusi1Nf7QSgKUvW2EzjeLoFvf8NFzvXNU47Q6Kdn5x7BxD-ceaSHNyVWYxc_B9Fo-IOvknMPPOEv9kvg2Nf4L_9tfYBX7NH2oytSG4Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"از او بگو به دنیا.. از او که قصه ای داشت
او جشنِ زندگی بود.. سروی که قد برافراشت
از اُجرتِ گلوله .. از شر که می‌هراسد
از مادری که او را از خال می‌شناسد
از او بگو به دنیا.. ای شاهدِ غروبان!
این رقصِ بی‌سران است، این داغِ پایکوبان..
یاد آر اگر رگت را با مرگ می‌خراشی
تو بازمانده‌ای تا او را گواه باشی!
دیدی که بر مزارش، رقصِ پدر کدام است؟
این هلهله عزا نیست.. آئینِ انتقام است
از او بگو به دنیا.. از نغمه‌ای که سر داد
از او که نیمه جان بود در کیسه‌های اجساد…
از او بگو به دنیاااا"
monaborzouei
Lyrics: Mona Borzouei
Music & Arrangement: Reza Sadeghi
Producer & Concept: Sia Davarnia
Executive Producers: Mahshid Hamedi Boromand & Farshid Rafe Rafahi
Director: Carlito Brigante
Video Producer & Director of Photography: Avid Eghbali
Ebihamedi
📱
youtube
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 390K · <a href="https://t.me/VahidOnline/78549" target="_blank">📅 18:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Uzgbe4qKDHETNdV0doVRD5y4EjVYZKEeHCNGtkvfue0P3MOevh6FuZIX3H7A3tat_xoGcAzAnXz6_PuHV_yDn9jwb-PT5ExZ58RdK3qb_LuOvYRGzTj6ejI_kJeXHmoKOQczFAMj7bLWnluJUBc7cGqGkB2zvoIkWki2fXUNKduuOIOG_xEqbecDZAD3IB3dsBDz_DhdI0YHxabQgwvjInVbnFoc-swXJOlc_JC-aJrEwKl_gASsMznqgCSgk84nChEYKatRu7JW6KwJinzE5nOYY8Wy4PgAxhsrMcHTCt_jEpaqZmdhjJ5XHqxTlrWYJ3y0QVpUvrPGZWJTYb8q0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا، روز یکشنبه پنجم مهر ماه و یک روز پس از آنکه اعلام کرد پیشنهاد ایران برای پایان دادن به جنگ را رد کرده است، در گفتگویی تلفنی با آکسیوس گفت انتظار دارد مذاکره‌کنندگان آمریکایی این هفته مذاکرات بیشتری با ایران داشته باشند.
ترامپ گفت: «انتظار دارم این هفته مذاکرات بیشتری با ایران داشته باشیم. آنها می‌خواهند به توافق برسند، اما این توافقی نیست که من بخواهم به آن برسم. این همان چیزی است که شاید یک سال پیش با آن موافقت می‌کردیم. آنها بیش از حد روی مواضع خود پافشاری کردند.»
به گزارش آکسیوس دو منبع منطقه‌ای نیز اظهارات ترامپ درباره برگزاری مذاکرات بیشتر در این هفته را تایید کردند و گفتند انتظار دارند دور دیگری از گفتگوهای غیرمستقیم میان آمریکا و ایران از روز دوشنبه برگزار شود.
با این حال، آکسیوس گزارش داد مشخص نیست اختلافات میان دو طرف بر سر مسائل اصلی قابل حل باشد. ایران می‌خواهد مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا متمرکز باشد، در حالی که دولت ترامپ خواستار تعهد ایران به امتیازهایی در پرونده هسته‌ای است.
@
VahidOOnLine
پیش‌‌تر:
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز یکشنبه پنجم مهر در حاشیه حضو در مسابقات گلف جام رؤسای جمهوری در شیکاگو، از رکوردشکنی انتقال نفت از تنگه هرمز خبر داد و تاکید کرد به محض «تسلیم ایران» و پایان جنگ، قیمت نفت به‌شدت کاهش خواهد یافت.
ترامپ با اعلام آنکه شنبه شب «مقدار بی‌سابقه‌ای» نفت از تنگه هرمز منتقل شده، افزود این میزان حتی از مقدار نفت منتقل‌شده پیش از آغاز جنگ نیز بیشتر بوده است. او همچنین گفت قیمت نفت اکنون از دوران دولت جو بایدن پایین‌تر است.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/78548" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h6O3_KstxM_5vJHouP-H6fpkvL88QX6YxGe8lMOzSLUdpoAbggHN8SPuSzuaJip-fgFoLqAdXG_BscArYAnZ87RX95-etwsD_Jh9NYFElAHgLwotYpDZefvtfy12qs035XUxL-4x0OustZnRAZHzDvZT1G_mhrYwrcbXXYwxaiqithRVF3XOqzt6JAzzf6dkHXZ9nsWYDVZiupC7S6EAsu8btm9dyCTi-LOXHkSaBIYb_2QSrkhLLs-bu6DDS0mZddCqzg3tpK7B5_seJDbDrNGshDyMkzaaHFV2l5H9BHa-DGqZz054JjBF3Z9Q-Bb3lLF2ChEarSwgbR4j9gCVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vHUYKfZxS9YwuuPEr-b_plqpEF8-jUnpxD7RvWlu1hd36sBEwhpZz9Zznx_12hnpNf_uCRKcHoO9TxuNDwQjjL65cdcEou8q-lF2XVvHerCx7nXPENiZbv35meOD0M1eXBff0e9rrttfjh5B0PBd4NZ0RTJtzMbRH6TvFPTeB8bkBESP9CtYlGjQtPjJzGYWMo-CvmrKf8V1Z7eazdj97NVT7vMhKl87fxnxvsoXYhvExxdBsUeueViUe5x3X-JlUF4depxc7QjNm-wcirdZNEiTnLvfMpCNkMbyGv8AHnN0m7EOgl_3Lpc3r8CaPRNYieHX2pDXzTcLTjbmWL1k0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، می‌گوید با وجود اعلام علنی دونالد ترامپ درباره رد پیشنهاد هفت‌روزه تهران، هنوز پاسخ رسمی واشنگتن از طریق میانجی‌ها به جمهوری اسلامی منتقل نشده است.
او با اشاره به اظهارات متفاوت دونالد ترامپ در روزهای گذشته افزود: «متاسفانه از رییس‌جمهوری آمریکا حرف‌های ضدونقیض زیاد شنیده می‌شود.» عراقچی گفت تهران منتظر خواهد ماند تا واسطه‌ها «نظر قطعی» واشنگتن را اعلام کنند و سپس درباره گام‌های بعدی تصمیم خواهد گرفت.
@
VahidHeadline
عراقچی روز یکشنبه ۵مهر ۱۴۰۵، در گفت‌وگو با برنامه «میت دِ پرس» شبکه ان‌بی‌سی نیوز، در پاسخ به گزارشی درباره احتمال ازسرگیری حملات آمریکا پس از انتخابات میان‌دوره‌ای این کشور گفت: «ما کاملا برای ازسرگیری جنگ آماده‌ایم. در برابر هرگونه تجاوز جدید ایستادگی می‌کنیم، حتی اگر به جنگ آخرالزمانی منجر شود.»
او در عین حال افزود: «هم‌زمان آماده دیپلماسی هستیم. انتخاب با رییس‌جمهور ترامپ است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78546" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/125cba9619.mp4?token=vV8jDi-2IJ_k1kaUaV7c6wXPeaLsqUvpc6SV-nXOUrZgDUG_9YYIbxTLMLEAqMoqVNmdzZvTgj-DsgT-mklLeZF0aLqHOALDc1-6dwB1rOKA-uf6bOvLD8N37KnHUoHVHSvMAy9yqBpCv6ieLEt-qoGVLZafptluCauM9B3bUsbdjd66_gnSe8lzg_4ZevAQCnkpoR_TGWaECq7ylWnZ_owuYmPD9E6aQtBLXeJ6yKVxfZZ9hxvGD8dDtdrAfasvbzwvH_D593uwa-gz__udP67r-BCEoVfBGGtT3CtltNjqIlJ9i53tt3eGOXk2d3Ai4mjkDf6mqA-kG3uxwAXALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/125cba9619.mp4?token=vV8jDi-2IJ_k1kaUaV7c6wXPeaLsqUvpc6SV-nXOUrZgDUG_9YYIbxTLMLEAqMoqVNmdzZvTgj-DsgT-mklLeZF0aLqHOALDc1-6dwB1rOKA-uf6bOvLD8N37KnHUoHVHSvMAy9yqBpCv6ieLEt-qoGVLZafptluCauM9B3bUsbdjd66_gnSe8lzg_4ZevAQCnkpoR_TGWaECq7ylWnZ_owuYmPD9E6aQtBLXeJ6yKVxfZZ9hxvGD8dDtdrAfasvbzwvH_D593uwa-gz__udP67r-BCEoVfBGGtT3CtltNjqIlJ9i53tt3eGOXk2d3Ai4mjkDf6mqA-kG3uxwAXALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: دومین زیردریایی بدون‌سرنشین آمریکا را در تنگه هرمز به غنیمت گرفتیم
نیروی دریایی سپاه پاسداران انقلاب اسلامی روز یکشنبه پنجم مهرماه با انتشار بیانیه‌ای مدعی شد که یک زیردریایی هدایت‌پذیر از راه دور بدون‌سرنشین (زهپاد) آمریکایی را در تنگه هرمز شناسایی و به غنیمت گرفته است.
در بیانیه سپاه آمده است که نیروهای نیروی دریایی این نهاد در یک «اقدام هماهنگ و پیچیده» و با استفاده از اشراف اطلاعاتی و جنگ الکترونیک، این وسیله زیرسطحی را که  «برای جاسوسی در تنگه هرمز» فعالیت می‌کرد، به دام انداخته‌اند.
سپاه این زیردریایی را REMUS 600 معرفی کرده و گفته است که آن را به غنیمت گرفته و اکنون در اختیار متخصصان نیروی دریایی سپاه قرار دارد تا اطلاعات آن بازیابی و بررسی شود.
رسانه‌های وابسته به جمهوری اسلامی نیز هم‌زمان ویدیویی از این وسیله زیرسطحی منتشر کرده‌اند و آن را به‌عنوان «دومین» زهپاد یا زیردریایی بدون‌سرنشین آمریکایی که در جریان درگیری‌های اخیر در تنگه هرمز به دست ایران افتاده است، معرفی کرده‌اند.
براساس گزارش رسانه‌های دولتی ایران، این زیردریایی یک وسیله نقلیه زیرسطحی خودران (UUV/AUV) است و برخلاف یک زیردریایی سرنشین‌دار، خدمه‌ای داخل آن حضور ندارند.
این خانواده از سامانه‌ها برای ماموریت‌هایی از جمله شناسایی و مقابله با مین‌های دریایی، نقشه‌برداری از بستر دریا، شناسایی و پایش زیرسطحی و جمع‌آوری اطلاعات دریایی استفاده می‌شود.
ادعای امروز سپاه در حالی مطرح می‌شود که پیش از این، در ۱۷ شهریورماه نیروی دریایی سپاه از توقیف یک وسیله زیرسطحی آمریکایی دیگر در نزدیکی ورودی تنگه هرمز خبر داده بود.
سنتکام در آن زمان اعلام کرد که آن زیردریایی به‌دلیل نقص فنی متوقف شده و «حاوی اطلاعات حساسی» نبوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78545" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/egRUCzQMWhKx3pPhm5mBAukU0AUb46rUaxSNQN7aOrhTVYgBTDbzs7XOcMhZZaO7_wPXt0ykqJT78qpoNCfsmxJ8aQVHg89Ef3r9_uX1P8AvU92afB5fayW21oM7nEP_bOBGcFbf0HpVHtTVN5-Eq5nOmmdrSYWr-VK1bOjGyzlIVySquZvaoZspsAaC9DaUhdW_LgyC98HAshKkWjJJ4hId384vzsXErjgnUsL2GyDJBB6ek_ziq6v-1vlFd7RrZ1ERafyVF3ou1D6y0DJXTQ46TB2YUtuq1Baqk79xkb1A4IknyHzFVT8KOaMmYrB9_dP6kLkbhDGReV25ClOhOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد اکرمی‌نیا، سخنگوی ارتش جمهوری اسلامی، در گفت‌وگو با خبرگزاری دانشجو گفت: آمریکایی‌ها در منطقه در وضعیت مناسبی قرار ندارند، اگر وضع آمریکا خوب بود تلاش برای تغییر وضعیت نمی‌کرد. آمریکا ممکن است دست به یک تعرض بزند اما ما از گذشته آماده‌تر هستیم.
اکرمی‌نیا گفت: آمادگی انگیزشی و روانی داریم و تلاش کردیم تجهیزاتمان را بهینه کنیم و تجهیزات جدید وارد سازمان رزم کنیم.
سخنگوی ارتش جمهوری اسلامی افزود: اگر دشمن دست به تعرض بزند منطقه بیش از گذشته درگیر جنگ و ناآرامی و خشونت خواهد شد و کشورهای منطقه آسیب بیشتری خواهند دید.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78544" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RGqATk3uZiEhGJ-h5Iy2x2hUWJ2Mb1_PfmV-A2KyQb2RrrBITKtDt_9aO5vSg94OYr3AI5Vl1rnRaYBL4SZqF3mK52aJNZApN7GnuJk-EmaH_84pZ844VNDzIpiBvxp28zGdHPHxq1g0cpYpf-7a4oRgkYW1CCfL3CHeJ5ucW2ZYfff7XsRofZs0FA-Rass9I2pOr5Q470s-fMokIR5RyqJuf8k7Awu3sjf4SN-_nVwPjJhwimRyg8C2DS0q4O2JLPLVFXId9LMYfh6ryIOmcf9O8YnluVFlM5Qy2opG5DTbbZZX51Q9z4qX1KCvyAreryclRP08s4XknhwueY-NKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aQzpnNC6_UtcFnKHlL24BoPhCHT8gA-3Hu03Amf2Z2Dy1gIrOWbv9xQmMj7uy7jQoCrymEAmeSENX_bjDqVJazTvMJWbIgZWh6mER6W663FVve6R5OriFsjtiOz_GdYVYYFxyZY_0P5raGlJQ6E1ixMDkMBASWeCHBE2bUYg2uFP61VqanfUXaNOpayIi2KTq6dz3c9GYGT1H6H2gPAoIY3aiZwMRwUM1fC0oa4Z1ZYe1iTmazUAjF0izF3s8QPNRDPkg9DvCLwLrvkYbkEvQudoL9Qt_3Y3U8k-w0R1DYeOPlxFfnQpFW-aCeremQBpxp6f8law0qxUSxE-I1YLnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمید رسایی در پرونده شکایت محمدباقر قالیباف به ۱۰ ماه حبس محکوم شد.
این نماینده مجلس شورای اسلامی گفته است که برای اجرای حکم خود را معرفی می‌کند.
دادگاه به استناد ماده ۶۹۸ قانون مجازات اسلامی، حمید رسایی را به «اعاده حیثیت و رفع اثر از ادعای نادرست از طریق انتشار تکذیبیه در صفحه اول نشریه ۹ دی» و ۱۰ ماه حبس تعزیری محکوم کرده است.
گفته شده است با توجه به اینکه این جرم قبل از دوره نمایندگی رخ داده، حمید رسایی مشمول مصونیت پارلمانی نیست و دادگاه او را برای اجرای احکام احضار کرده است.
@
VahidHeadline
عباس عبدی، روزنامه نگار و فعال سیاسی، به دلیل انتشار یادداشتی در روزنامه اعتماد به یک سال حبس تعزیری محکوم شد.
روزنامه اعتماد هم در این پرونده به دو ماه توقف فعالیت و انتشار محکوم شده است.
آقای عبدی در بخشی از این یادداشت که ۱۶ اردیبهشت ماه در روزنامه اعتماد چاپ شده بود نسبت به انتشار «اخبار جعلی» از سوی برخی از نمایندگان تندرو هشدار داده و گفته بود: «این افراد تحت نام نمایندگی هر چه بخواهند می‌گویند و کسی هم در مقام اصلاح آن‌ها برنمی‌آید.»
در پی انتشار این یادداشت، دادستانی تهران او و روزنامه اعتماد را به چند اتهام‌، از جمله «ایجاد دوقطبی کاذب و اختلاف میان اقشار جامعه» و «نشر اکاذیب و مطالب خلاف واقع» تحت پیگرد قرار داد.
@
VahidHeadline
صادق زیباکلام نیز در پی مصاحبه‌ای با خبرگزاری آنا به یک سال حبس تعزیری و از باب مجازات تکمیلی به منع هرگونه فعالیت رسانه‌ای، مصاحبه، یادداشت‌نویسی و انجام مصاحبه به مدت دو سال محکوم شده است.
@
VahidHeadline
حکم یک سال حبس در پرونده حشمت‌الله فلاحت‌پیشه نیز در دادگاه تجدیدنظر تأیید شده،‌ اما به مدت پنج سال به حال تعلیق درآمده است.
سیامک رحمانی، روزنامه‌نگار، نیز پس از تفهیم اتهام و صدور کیفرخواست با اتهام «فعالیت تبلیغی علیه نظام» به پرداخت جزای نقدی درجه شش به میزان ۸۰ میلیون تومان محکوم شده که این رأی قابل تجدیدنظر خواهی است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78542" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_kaq68ch-ttmls5g57woGGZclM8fs2P5Ol1FEwdFKA6R1FJRSHkZG_g5hrosWJmC_h_4KQESPid4O0kM8ph5iT_3Nr4haRVu0Ao-Obs-9qYAdXd4_qushDdSdxWGAVL8RfHuEhmPwq983IOL1v7o4KVljQJwpzU1T3_vvdyRonkZLetm2qqWEQuF0gjLDS65nzch0mz_JsG8LirnTG5zHlS-y_PC2X-XDaJlL80Jj_aG_BFgQbgv5Dz0y2PsJGpH_T1GRacgMlJ3-mtE2Gbf9jsdR2FqOiF97s8ZLvUpEssATXylumoSA7NsAWSHscAKqfykIKb8ZCSZHZGpMoyIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم پنج سال حبس دیگر برای علی یونسی، دانشجوی مهندسی کامپیوتر و دارنده مدال‌های المپیاد نجوم، در دادگاه تجدیدنظر تأیید شد. این حکم پیش‌تر از سوی شعبه ۲۹ دادگاه انقلاب صادر شده بود.
یونسی و امیرحسین مرادی، دانشجوی فیزیک دانشگاه صنعتی شریف، قرار بود با پایان محکومیت قابل اجرای خود در آذرماه ۱۴۰۵ آزاد شوند، اما با تأیید حکم جدید، علی یونسی همچنان در زندان خواهد ماند.
تابستان ۱۴۰۴، این دو دانشجو هر کدام به اتهام «فعالیت تبلیغی علیه نظام» به ۱۵ ماه حبس محکوم شدند و علی یونسی نیز علاوه بر آن، به پنج سال حبس دیگر محکوم شد.
یونسی و مرادی از فروردین ۱۳۹۹ در زندان هستند و بنا بر گزارش‌های منتشرشده، در مجموع ۸۰۸ روز را در سلول انفرادی و بندهای بسته سپری کرده‌اند.
این دو دانشجو در پرونده اولیه در سال ۱۴۰۱ هر کدام به ۱۶ سال حبس محکوم شده بودند که در مراحل بعدی، میزان حبس قابل اجرای آنان کاهش یافت. با تأیید احکام جدید، هر دو همچنان از ادامه تحصیل و حضور در دانشگاه محروم خواهند بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/78541" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیام‌های دریافتی:
سلام وحید جان قشم صدای انفجار از روی دریا اومد
قشم۱۲/۳۲ انفجار
وحید جان صدای انفجار از سمت تنگه میاد خیلی فاصله داره تا ساحل جزیره قشم تا حالا ۵ تا۶ شنیدم
از ساعت ۱۲  تا ۱۲۳۰
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/78540" target="_blank">📅 00:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIIc6GG2GU8PiI9Qz-o5vCfqk1y1G6vqZznPIq5STmttqD7i60rQD-Y7EzpKTc8vt4FNtDmELUOefZdKNe_LpBiqt6C36luEmyG0FNOuF3nnki8pzZj71yX1oAds6w3XK3oNpt3zEDbtQgP_f--QZIclBCug69l0lKK-W3ReRjEJJrpXxLKKEviwqRVbnIGD3WgHVnrgQFctBEnODtH_QjaL9JLYktO2aJwDA16YXpRFx_G9fet8PN70C7ndcpxMlMiN3Kwq0hqGiQYH3KJxc_GjX7o-Fc7o9x_nlb0--PWN8gdzcg7qGqJYB9xeqKZSL9LZofezrmvXtf89zuykjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وبسایت آکسیوس، روز ۴ مهر ۱۴۰۵، به نقل از یک منبع آگاه گزارش داد مذاکره‌کنندگان آمریکایی در جریان مذاکرات غیرمستقیم با عباس عراقچی، وزیر خارجه جمهوری اسلامی، به او اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند برای بازگشایی این آبراه شرط تعیین کند.
عراقچی در این مذاکرات شروط تهران برای بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای را به طرف آمریکایی ارایه کرده بود.
بر اساس پیشنهاد جمهوری اسلامی، تهران حاضر بود تنگه هرمز را بازگشایی و مذاکرات هسته‌ای را ظرف یک هفته از سر بگیرد، به شرط آنکه آمریکا محاصره دریایی بنادر ایران را لغو، تحریم‌های فروش نفت را رفع و آتش‌بس در سراسر منطقه را دوباره برقرار کند.
بر اساس گزارش آکسیوس، مذاکره‌کنندگان آمریکایی روز سه‌شنبه در جریان این گفت‌وگوها به طرف ایرانی اعلام کردند که جمهوری اسلامی کنترل تنگه هرمز را در اختیار ندارد و در نتیجه نمی‌تواند درباره بازگشایی آن شرط تعیین کند.
در حال حاضر ده‌ها نفتکش روزانه تحت حفاظت آمریکا از تنگه هرمز عبور می‌کنند و میلیون‌ها بشکه نفت را به بازارهای جهانی منتقل می‌کنند. با این حال، حجم انتقال نفت همچنان به‌مراتب کمتر از سطح پیش از جنگ است.
مسوولان آمریکایی می‌گویند طی ۷۲ ساعت گذشته حدود ۶۰ میلیون بشکه نفت از طریق تنگه هرمز منتقل شده است.
در همین حال، قطر و دیگر میانجی‌های منطقه‌ای برای ازسرگیری مذاکرات میان تهران و واشینگتن تلاش می‌کنند، اما اختلاف دو طرف بر سر موضوعات اصلی همچنان گسترده است.
جمهوری اسلامی خواهان تمرکز مذاکرات بر تنگه هرمز و محاصره دریایی آمریکا است، در حالی که دولت ترامپ بر دریافت امتیازهای هسته‌ای از تهران تاکید دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 456K · <a href="https://t.me/VahidOnline/78539" target="_blank">📅 22:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=pHbX4Igk4IG8ysD5r_P6pyidxvA6AJ4Bzg6YTCLsi5_3S5arl_O_WziWMJb6taN-c4Mt2wDXCToCjBsYTYZuohjyoxJdP1MvKm8juj2y22SFmlRERmkiXWALVxE3iPyIyUrdTuA8uIyaACJ77YONpqAz2iaZweHJo_4CqVwQs_fkxyrW-gsxfLh9awZ45PYAl0bVs_E3pWczTYLkWeLrdkACa3TZXVa3v2vXCYx3F4DmdtIc60kXkCfuoICK7v2LXRzV9bA9w4SiJNBR1gbI929L0AIYh4OkugFdbKWyvKe8MKpWck2z17zDPnfVBjTx-dHonUa7rLGmpPdzAQno5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aa5e4db158.mp4?token=pHbX4Igk4IG8ysD5r_P6pyidxvA6AJ4Bzg6YTCLsi5_3S5arl_O_WziWMJb6taN-c4Mt2wDXCToCjBsYTYZuohjyoxJdP1MvKm8juj2y22SFmlRERmkiXWALVxE3iPyIyUrdTuA8uIyaACJ77YONpqAz2iaZweHJo_4CqVwQs_fkxyrW-gsxfLh9awZ45PYAl0bVs_E3pWczTYLkWeLrdkACa3TZXVa3v2vXCYx3F4DmdtIc60kXkCfuoICK7v2LXRzV9bA9w4SiJNBR1gbI929L0AIYh4OkugFdbKWyvKe8MKpWck2z17zDPnfVBjTx-dHonUa7rLGmpPdzAQno5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز شنبه چهارم مهر تأیید کرد که پیشنهاد جمهوری اسلامی ایران برای بازگشایی فوری تنگه هرمز را رد کرده است.
ترامپ پیش از ترک کاخ سفید در گفت‌وگو با خبرنگاران گفت: «من پیشنهاد آنها را رد کرده‌ام. آنها می‌خواهند توافقی انجام دهند که بر اساس آن تنگه را فوراً باز کنند، چون به‌شدت در حال شکست خوردن هستند.»
او افزود: «ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم و مقادیر عظیمی نفت از تنگه هرمز خارج می‌شود. دیشب ۲۹ کشتی از تنگه عبور کردند. آنها می‌خواهند توافق کنند و من هم با توافق مشکلی ندارم، اما آن توافق قابل قبول نخواهد بود.»
@
VahidHeadline
او بار دیگر گفت جمهوری اسلامی خواستار بازگشایی فوری تنگه هرمز است و افزود: «آنها هیچ پولی به دستشان نمی‌رسد، چون پولشان را از تنگه هرمز به دست می‌آورند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/78538" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OgmDpwyz99-Ny29duR6UPHFR8udYyAaBWotBnJWOt5EaL7EPaDZTuLaLNyqr6J3A4Hf8JFo5WeW92blr40M4UVMzPON_wqAMwDjfJb2bPVANggrhTyYIwDMojvsKlFNaDCDvPQE4OAo5hHqNd2WgWG0Pmye-astqUNOnPsLKInqDpoITYyoxM4tH6z3blOJMyIOr5oUI7GmTFmULrUaCBHHfIZfaoM7yWftZS8yag1PscWgaQYZlBEwnlVZRKUDMEUDIGifxoxWz3OJlOfDew7m5f8DedZUatdg1gE4rBQQraBv6wXl9V2EGSRTPPUCvZI7P8Xa4MQPwOCzeCEwnhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=pTVcdcCZRxBy7ZeDQyIwFCKMcum0KaHCgIj9Wz19skYMyrG1X4IKkOhSyAcqjCzbtIdvpnELBnLOVWTp2xY3MDEztSs_BbUodAPyFydy701_t9bhYjd4_O8gLv8afgkwE2gCCYSms5wud0Sc9woGzraj3cvjToOzrDbGdUla6bspaMiNuf0LsXInkvfsuXle_seH0vaKMP9perar_oE8GGY04cK5qVqkqx-OMGhdEXhpD6YueU3bp4hLljCN1nYB5XYiJ4zxk-5cu3MqH_eBH6b78MFWuGp3XEY1XiExrkH6ndtbMAZJYI9yqX9f2_Y_NrdvFws7sSyMq7_ueFfn4w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/19b541c60b.mp4?token=pTVcdcCZRxBy7ZeDQyIwFCKMcum0KaHCgIj9Wz19skYMyrG1X4IKkOhSyAcqjCzbtIdvpnELBnLOVWTp2xY3MDEztSs_BbUodAPyFydy701_t9bhYjd4_O8gLv8afgkwE2gCCYSms5wud0Sc9woGzraj3cvjToOzrDbGdUla6bspaMiNuf0LsXInkvfsuXle_seH0vaKMP9perar_oE8GGY04cK5qVqkqx-OMGhdEXhpD6YueU3bp4hLljCN1nYB5XYiJ4zxk-5cu3MqH_eBH6b78MFWuGp3XEY1XiExrkH6ndtbMAZJYI9yqX9f2_Y_NrdvFws7sSyMq7_ueFfn4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستانی تهران در پی انتشار تصاویری از اجرای نمایش «تهران پاریس تهران/ پل»، علیه عوامل این اثر اعلام جرم کرد و پرونده قضایی تشکیل داده است.
مرکز رسانه قوه قضاییه شامگاه جمعه ۳ مهر ۱۴۰۵، بدون اشاره به نام نمایش اعلام کرد «رفتار خلاف عرف و شئون دو بازیگر در یک تئاتر روی صحنه» موجب ورود دادستانی تهران شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/78536" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vzZoXT1aUOR-rQ9znaNWfeBKFsyTLiNNnGLU33E_mxdffJGb_m_aw2e2JVbwq1g5Oi60DE7JBa2rhYAOPVIin0ljkeCRKF4ATog2WZfo_rE87VgBdQin4nf6LkrFz7VdhWAsPg0HIKVRqX93zxpUyRf9cEz_y7wyO5vOJU4KBVMBBjtW8oy_tBX4p07vc6I-W4U-7ZdD1MbjuennvKcspdqcQ9Y6L2HCVpT3LOuNacrmHc6EM6cwN60az-JyuPwPKGKUn5IU0D9u2dNKwQpUkL2H9_mfr-QstzcKbwnGsvoOHAeAYsl4ck-k54clJ4LeMpsR8IUIwtyEmQww3uCv_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«محبوبه شعبانی»، از بازداشت‌شدگان اعتراضات دی۱۴۰۴ در مشهد، به اعدام محکوم شد؛ زنی ۳۳ ساله که براساس گزارش‌های منتشر شده، در جریان اعتراضات با موتورسیکلت خود به انتقال معترضان مجروح به مراکز درمانی کمک می‌کرد.
هرانا خبر داد شعبه اول دادگاه انقلاب مشهد، شعبانی را با اتهام «اقدام عملیاتی جهت تحکیم اسرائیل، آمریکا و عوامل وابسته به گروه‌های اپوزیسیون» به اعدام محکوم کرده است. به نوشته هرانا، حکم امروز به وکیل او ابلاغ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78535" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDGuH9QgubsoeHH5oRTLmSJdufiprko-5G0CJ2ap1yjw8PjTFuRxvNbW20QOBOGHmiVPFRoZO6yeqcVaKbLQTbLbnV1Wl0Ze4bXVDYxLsABuuOUMZtG0tuka8oPECL2c424oRSsABNg5WzCpSCDcsAa8BCy5rnm_5Gy7RQNww-hW3dAkuvtPfpE3mag0nszrkTya9IIaiWgR1ktDoG20vRVZXmZ2kXKO7PoI1fbqrEv67N0YVAZc9rsFUWZpDimciYEmqjXHDAV1YM20eHxyL9Z4jR9Q9kg9r6P4tzL5Omsh458PSzLY0uxPXmasHp6nugNODEpbmXCoSc3b7ledog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«امیرحسین موسوی»، زندانی سیاسی محبوس در زندان اوین، در شعبه ۱۵ دادگاه انقلاب تهران با دو اتهام «محاربه» و «افساد فی‌الارض» روبه‌رو شده است؛ اتهام‌هایی که می‌توانند به صدور حکم اعدام منجر شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 295K · <a href="https://t.me/VahidOnline/78534" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/apHf5RWSbpa6_7g_CGFuTfDCrWTitabZDJnr2UHrQ6CUM6aXOHyoV_pdOCzy0_9rR_SSOJOJG3h2-Kv6G_viKooo_2XNJyyYH6SoXjaejxUDGhbXhGIcpmVaPBj-5TeVPlUSlOib1ry23ltoFh9mF-EEDEJZM2ZhwkTAJbYBoAJJ_kiDYGNc8hRU7K4qBl1wuC7PjjnA6WhAQe9up0rDlCQyxjn3nzFQpmOqNxK3rctVNkqaC4gt_BhIuntVoLrqCECFF0yhRMYclzIKxKDslTSWMtabLheJsP9BkoNyeDCeCI9kDst25ciet7DHWUpsjTHC3jTN1hLqSHlDcscr8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=ORRzkECoOFZeSXXRlS3tSSjCH1vQqQk3fGUfLsc1_PnKycS6opb927LptvAEYrxEkSESEaXopxyBsbxwwh2IZ6zZVp5XT4pIuWq75BzageDtfaxPEcQaMKg4-brv_Tc3Ab8HpyocyrWvACr6PXezMkLRCHjD1MCNqRxX04Oa9p5gsttAPkRbWPvjYSfrai6388c658MLwvoMHqxVaKWl4ByPxk97OYxi6n8HXWAOrr2l4u-gmnKoH9eH9Vwli4zoQXareUD92kxeNAhI8whg77Tcj1PLVEZBQw0dSKYV8eMmYsDHPdrSxK_jS139ST9NxjDfTn7Nr6LftYAD1jvg4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f732caa14c.mp4?token=ORRzkECoOFZeSXXRlS3tSSjCH1vQqQk3fGUfLsc1_PnKycS6opb927LptvAEYrxEkSESEaXopxyBsbxwwh2IZ6zZVp5XT4pIuWq75BzageDtfaxPEcQaMKg4-brv_Tc3Ab8HpyocyrWvACr6PXezMkLRCHjD1MCNqRxX04Oa9p5gsttAPkRbWPvjYSfrai6388c658MLwvoMHqxVaKWl4ByPxk97OYxi6n8HXWAOrr2l4u-gmnKoH9eH9Vwli4zoQXareUD92kxeNAhI8whg77Tcj1PLVEZBQw0dSKYV8eMmYsDHPdrSxK_jS139ST9NxjDfTn7Nr6LftYAD1jvg4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در  دو واقعه جداگانه دست‌کم ۲۰ نفر کشته شدند:
یک دستگاه اتوبوس مسافربری بامداد شنبه ۴ مهرماه در آزادراه همدان ـ ساوه واژگون شد و بر اساس گزارش مقام‌های امدادی، ۱۱ نفر از سرنشینان جان باختند و ۲۴ نفر دیگر مصدوم شدند.
@
VahidOOnLine
برخورد یک اتوبوس مسافربری با تریلی حامل میلگرد در محور بیرجند ـ قاین در استان خراسان جنوبی ۹ کشته و پنج مصدوم بر جا گذاشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 293K · <a href="https://t.me/VahidOnline/78532" target="_blank">📅 17:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoPUnJJRr9SsL_iuUm97Xs_XHZ0AByrfy-bONYkTI8kHRNBu0gL8uI--XJDo9tHPbD8fTlFyCVmUR4SpGDedSz51sfupRHgw6loaGQ-oJTyiFR03BWYocQ9ILLUxl92QdTl_s0J4nMCGe8l5wid0NgNPot-PFOPPP2QDD1skbCj9ntgWON4mAMurcX4UoymWdzDmdKGK008EpmWvOnhFFHSeemMSpDuSxW6-vjwN5-NpBJo59hWhirT2PDDLI6yOYrL3Xk3j-e2OiGx8DJHFVYAyVZadBIjhWYYlbMBHXY7BvD1GtCSNIKHaC1zgkL5HNKzg9vqD7XmbRZr7bKM38Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه تجدیدنظر استان قم حکم ۷۴ ضربه شلاق پرستو احمدی و هشت نفر دیگر از نوازندگان و عوامل «کنسرت کاروانسرا» را بدون تغییر تأیید کرد.
ابوذر زمان، وکیل دادگستری، روز جمعه در شبکه اجتماعی ایکس نوشت بر اساس رأی شعبه ۱۶ دادگاه تجدیدنظر قم، پرستو احمدی، چهار نوازنده و چهار نفر دیگر علاوه بر ۷۴ ضربه شلاق به دو سال ممنوعیت از فعالیت در امور سمعی و بصری و ممنوعیت از خروج از کشور محکوم شده‌اند.
دادگاه کیفری استان قم پیشتر این ۹ نفر را به اتهام «جریحه‌دار کردن عفت عمومی از طریق تولید و انتشار محتوای مبتذل و خلاف اخلاق در بستر فضای مجازی» محکوم کرده بود.
پرستو احمدی در آذر ۱۴۰۳ ویدیوی «کنسرت کاروانسرا» را که بدون حجاب اجباری و با همراهی احسان بیرقدار، سهیل فقیه‌نصیری، امین طاهری و امیرعلی پیرنیا اجرا شده بود، در یوتیوب منتشر کرد.
قوه قضائیه پس از انتشار این اجرا علیه عوامل آن اعلام جرم کرد و احمدی و دو نوازنده همراه او نیز برای مدتی بازداشت شدند.
در رأی بدوی، دادگاه پوشش پرستو احمدی و همچنین تولید، تصویربرداری و انتشار عمومی این اجرا در فضای مجازی را از مبانی صدور حکم عنوان کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/78531" target="_blank">📅 17:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p2j_Oy6iPP79tNoogANeD1UeHVm1vg1KhZaa_S45qNWMbqrkkB3Gj21yzzwgkGUGMXpyDPt3LjxrMdgShOxoRjLXpWs41mU1fUyhg_wZ-vaOYGOVM-pyOhdPypy7lCFoGGAQ6O6boQhOfVeTBBxcaGf71B0IDuQ_HMj6cj74RJOMB0CI-IQzw-38AGqboF1BmUckMrzHcmE_9KiCurmzPT7qR5qaZvemUceABkwJaU9t9kqWl7XwqxmMK8XUyumx4cwPRFU_l85KeXEuBVye0CnAhYtgXH_bb6Q6jqT5NEZN8LitkYg5OV291MNBirVN52EWFultFAWHpcn4rzgXSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه وال‌استریت ژورنال به نقل از «مقامات آمریکایی» گزارش داد که رئیس‌جمهوری آمریکا، پیشنهاد جمهوری اسلامی برای برقراری آتش‌بس هفت‌روزه را رد کرده و به دستیاران خود گفته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران را از سر بگیرد.
دونالد ترامپ بارها هشدار داده است که در مورد تاسیسات هسته‌ای «کوه کلنگ» ممکن است دست به اقدام نظامی بزند.
وال‌استریت ژورنال می‌گوید که پیشنهاد جمهوری اسلامی شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران توسط ایالات متحده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 386K · <a href="https://t.me/VahidOnline/78530" target="_blank">📅 05:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCg3YCci7siCVQQTMaEZnbICDxx3i901rq87Oh92cp5gCQsta1lxle709a7elmxoFHRAOtn51K9xkM8Z87GRqtxSrk8dgnMVHy0dUliAGR5wS6V3D58aD7h44yqJrVpESTaEcCFllP71of3XYuGWzlRHSyXttSHwJTHwYolSMs3Mk2efqa3U2jSsII08ntzJ3tlg_og4gFb5lv6jwyJ1Eqg_mFFB-EFg-4GtuURf7YdOks_vHLtqdUIv2w-hsk8BUKQNS0kp87pGY_pmJwdwJ1GbgioUL69qoLpCj4Pq686mwHzGA1KJpJKB00kfbTFJb1IHORWEc2EnQlkjICZMJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مخبر، مشاور رهبر جمهوری اسلامی ایران، هشدار داد که در صورت تداوم محدودیت‌ها و قطع خدمات فرودگاهی برای پروازهای ایرانی، هیچ‌یک از کشورهای منطقه نیز اجازه نخواهند داشت از خدمات پروازی بهره‌مند شوند.
مخبر روز جمعه، سوم مهر در شبکه اجتماعی ایکس نوشت: «همسویی با آمریکا در اجرای سیاست‌های خصمانه در خاطر ملت ایران ماندگار خواهد بود، هر چند راهبرد ما در این مورد مشخص است: پرواز در منطقه یا برای همه آزاد است، یا برای هیچ‌کس.»
پیش از این محسن رضایی نیز تهدیدهای مشابهی را مطرح کرده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78529" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3eMs_TiD8wvg2DAILjBtW8ynLnFrzwzTDqqYjzIjZjPRDobO-SLxuq5BRZ4Gtac6RQvSpc3MMBSqpvZ8n7lG4-gZ4u8OmYz_5xdNfd3lAsblbGApOPmEr0ttzbTb6kyKjgTbbz7HdzogWE4uEXa4BhAzB4EFmafNzgQgzgchqYxuj-7NucLF2WggJmcaovKFNkrzp1wFVlsv05FC7zxS7ynwIBcdJB8wQHJfyVKoOi6kXfI7-MoLndKzRRJr-SnFNtYySp1beLBCeaJqyT0SGc_G9UMu6UAcufLnn2G9m52EAxqxkIkoqoarHrGuNBiyapfr72H5Mbvo1l-GMKxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع مطلع خبر داد که فرودگاه‌های اربیل و سلیمانیه در اقلیم کردستان عراق از روز جمعه سوم مهرماه پرواز هواپیماهای ایرانی را معلق کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/78528" target="_blank">📅 17:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-NXPS9100jh4B1Wc_PRVuBozSUhkdzSvV_PsqntNBe-bG0WpkPYAQAaWF5F7pNtjUpR4GaePgOA8LEh7mtXkp-QuOfE6d_jfWvoXnRP-yk9m8LXknVByrW1OxL2SJFSAX6tyi8iPhwGTRuw54ggun_eVYo7rWxEDKsJzl2-ukXG5GAyE57Ke33aZw95sSHq9pFScjex-VkCSpHLO3FSVOqR36EW-z73t_oDxIktqmiPUyBPlNNxEAib6xCpJyMh6obAv4XeCY_HrCQ0p7YL5vu8Ilq_2QUDVtY-LcVv7y20Dfh3puxco_q--EhJfNprhDAAwNQhXK406f6Mzxnd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی عراق از توقف تمامی پروازهای ورودی و خروجی از مبدا و به مقصد ایران، از فرودگاه بین‌المللی نجف خبر داد.
مدیریت فرودگاه نجف با صدور اطلاعیه‌‌ای اعلام کرد: بر اساس دستورالعمل‌های رسمی صادرشده از سوی نهادهای ذیربط، تصمیم گرفته شد تمامی پروازهای فوق، از ساعت دو بامداد روز جمعه سوم مهرماه تا اطلاع ثانوی متوقف شود.
پیشتر فرودگاه بین‌‌المللی بغداد نیز از توقف پروازهای ایرانی خبر داده بود. این اقدام در پی تحریم‌‌های اعمال‌شده از سوی ایالات متحده علیه خطوط هوایی جمهوری اسلامی اتخاذ شده است.
روز پنجشنبه نیز فرودگاه‌های امارات به همراه برخی از کشورها از جمله ترکمنستان و آذربایجان، از اعمال این تحریم‌ها خبر دادند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/78527" target="_blank">📅 17:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2PoKawXD7uaPsKD4HgXKtXROjXr2_Z-6Vhlzq0ruNUjtkWRrAG0Pim1u9C2ax-LJrT9BgNp6k_8bXS_E-pDOWH5qZq4df-hl183l663FU7k2Rp7afdPWH0reNUEbP7PqLKxB40wa-6dUpIqIFGmQZvBnvDNynv77Ehf5gH5cw781-cFJ9x7yljJ-IoewWokQuGOUhOjR6ZIQeQtIg-uN0YC49c8XghICvvCki8R3IDLp75vA50r_lecOjnA815zoson5-6vURG_mtyeqnL0nSZBEOUoU2TTZBreZBPB3-xU30xWcHfrSxX2oiVX3rXj1XNwl3mvhqcYdYJ16pMdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه اسکای‌نیوز می‌گوید وزیر امور خارجه بریتانیا در دیدار با همتای ایرانی‌اش به او گفته است که بریتانیا «ارعاب، تهدید یا اقدامات خصمانه در خاک خود» را از سوی گروه‌های وابسته به ایران تحمل نخواهد کرد.
اسکای‌نیوز این گزارش را روز پنج‌شنبه دوم مهر به نقل از منابعی در وزارت خارجه بریتانیا منتشر کرده اما منابع رسمی دولت هنوز آن را رد یا تأیید نکرده‌اند.
اد میلیبند و عباس عراقچی روز پنج‌شنبه در حاشیه نشست مجمع عمومی سازمان ملل متحد با یکدیگر دیدار کردند.
وزارت خارجه ایران می‌گوید عباس عراقچی در این دیدار از اقدامات آمریکا و اسرائیل انتقاد کرده و گفته است ناامنی منطقه و تنگه هرمز پیامد حملات نظامی آمریکا و اسرائیل «با حمایت برخی کشورهای اروپایی» است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78526" target="_blank">📅 17:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPDyW9rLHLBxLCk_RJqiwvCbPi20NbSHQsblhxJYhWF0pKb900CtL93kcZBagTAqOdeWCJNLSIhRrrtM9kXfyfr7y7QfuTlxKnlR7mBcc3Y8vR-dRyI_1OiM4zzc2pnZvObo_NEmfKlwfN1DfhqqcjYLTywuHGI5K0_BOfCedixAhFuKSpNpRKpudxC6xgbEBRylz0HSj-cwsAS9JREn3o-7Jx2zI2pvfGu2IEDCWR19EFISi0cdz5U9E9FpYFyLyHkGbhP1lJglVIOcDSdFP7yLhlhoXpYBXjzFur9HpJK1YAnrHWzNhIB0UjA0qw3i9nNVk80rLos5Va6IHaUSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهور فرانسه از اعزام نیروها و تجهیزات نظامی این کشور برای محافظت از یکی از تأسیسات نفتی عربستان سعودی در مقابل حملات خبر داد.
امانوئل مکرون روز پنج‌شنبه دوم مهر در یک گفت‌وگوی تلویزیونی اعلام کرد که فرانسه در پی حملات شبه‌نظامیان حوثی یمن، «تجهیزات و نیروهای نظامی» را برای کمک به حفاظت از بندر راهبردی «ینبع» در عربستان اعزام خواهد کرد.
او گفت: «ما برای حفاظت از این تأسیسات، امکانات نظامی شامل نیرو، رادار و سامانه‌های دفاعی اعزام خواهیم کرد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/78525" target="_blank">📅 17:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/im8m22XrPjgOIexae3QCH91vkVfgU8EYDU_qDTSlXhtLqYNwAe05StoVdJOfVO-Jtcc-nzjgpU4Lrj_RtI6ZDTQnHrICFNKEwqd6UYPqtcmAYPWVmPvkXL5QWDbaKpSwGNQOn0PhP9ynFlKlfdaM_MwuerDUX2ASD-yJO4xjUzOeWwj7o47B9e2IXN396ZIDMftgh1z3keS19bbz5iW3Rvbeiteehvid98iW1RR667zojtI_Sl5esMP7LiNXw2z7l4ClIb3zlfx-ppYfzdGOayxebtLj9g4Q68zWgM-FH3V0ZRLFuCU1z6cet2tXcjU6VGYyLpySwCXnIz7s8LxLVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل ناتو با اشاره به تشدید تحریم‌های اقتصادی آمریکا علیه جمهوری اسلامی اعلام کرد مردم ایران هر روز آن را احساس می‌کنند، اما برای رژیم حاکم ایران منافع مردمش اهمیتی ندارد.
مارک روته در گفت‌وگو با فاکس‌نیوز تصریح کرد دولت دونالد ترامپ با حملات خود، برنامه هسته‌ای و موشکی جمهوری اسلامی را که «تهدیدی برای اسرائیل، خاورمیانه و اروپا» است تضعیف کرده و اکنون فشار اقتصادی بر جمهوری اسلامی را تشدید کرده است.
او در پاسخ به سوالی درباره اظهارات بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل مبنی بر اینکه بزرگترین ترس جمهوری اسلامی از مردم ایران است، تصریح کرد که به نظرش این حرف درست است و مردم ایران از دست حاکمیت به ستوه آمده‌اند.
بیشتر بخوانید
.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78524" target="_blank">📅 17:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t886XSgHRInQuvuZOhlKtgOifLxJaCllxQmuDCTMpRXlsg9HUJWgY70_SR5RrgYIuqW8WYgZ2k1ONLPQDW9qx-8RPASkEYSWqlxlwvhevnd_zefHNy6P1MiIir3x3E3zOiN9oX0psxXerl3b1VrRPm5yrZN7cOrfRZhY7SiXKtJTW247fLxbCh-jsU8FHS-2tdiNdwF15sFmWDnQaPCEJT2kc3Oh_HRlw0HYYGpBvayMUZWSCQcDlDDP9kIyEXPos6ZaHAsDVi6iifuOgmfC8uJ3VAXhRDddVdpFutO46oIjNObvzBy6au1FsIAjDvtF4071MyzHj9qrKPRsjaWIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت کلمبیا روز پنج‌شنبه دوم مهر از قطع روابط دیپلماتیک این کشور با ایران خبر داد.
در بیانیه دولت کلمبیا گفته شده است این تصمیم بر اساس ملاحظات مربوط به «امنیت ملی در سطح نیم‌کره» گرفته و از روز ۱۹ سپتامبر (۲۸ شهریور) اجرایی شده است.
کلمبیا در بیانیه‌اش حکومت ایران را به داشتن ارتباط با «گروه‌های نارکو- تروریستی» متهم کرد که به‌گفتهٔ کلمبیا امنیت این کشور را تهدید می‌کنند.
دولت کلمبیا همچنین تهران را به دلیل مسدود کردن تردد در تنگه هرمز و حمله به سایر کشورهای خاورمیانه در جریان جنگ با ایالات متحده و اسرائیل، به شدت مورد انتقاد قرار داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78523" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rINn5yEVwNh4ddeQEzDFYqMpMhH4-EHydTt2Lg1m2stBzhoHNs21lyPjNM3HD2arlQlLRX3kIkqdZnPXP2Ifw9RlxaOuQRCpMd0jriTfbFurZ2NVf50diz1EY4DYsq5mWgeS9AKzyd9vU4k6ac1yJI1kh5E0WxpVqeLE_xlfLnhrpOytFY_NFWI8nh3zteZmG-_m6jqgpqYPF7CO9h5QddsfcEmMgnhgWn7iCmpNFsKYpvbZRlOlP3tlvfThCJV7yYUng313-3_5hiR2CPu_l--_doqy5QUyqXnwqK7152BY0BdZ_YV8G-LTxMyyVGMef5Or4KVAEDv70LdBzZWWIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه بریتانیایی جوییش کرونیکل در گزارشی روز پنج‌شنبه دوم مهرماه از محاکمه غیابی هفت ایرانی و یک شهروند لبنانی از جمله محسن رضایی، دبیر شورای عالی امنیت ملی و احمد وحیدی، فرمانده کنونی کل سپاه پاسداران جمهوری اسلامی در پرونده بمب‌گذاری سال ۱۹۹۴ مرکز یهودیان آمیا در بوئنوس‌آیرس خبر داد.
بر اساس این گزارش، دانیل رافکاس، قاضی فدرال آرژانتین، با صدور حکمی ۶۴۸ صفحه‌ای، اتهامات هشت متهم را به‌طور رسمی ثبت و دستور مسدود شدن دارایی‌های هر یک تا سقف ۵۰۰ میلیون دلار را صادر کرده است.
احمد وحیدی، فرمانده کل سپاه پاسداران، و محسن رضایی، دبیر شورای عالی امنیت ملی، در کنار علی فلاحیان، علی‌اکبر ولایتی و چند مقام و دیپلمات پیشین جمهوری اسلامی از جمله متهمان این پرونده هستند. قاضی اتهاماتی از جمله قتل و جراحت با انگیزه نفرت نژادی یا مذهبی را مطرح کرده و بمب‌گذاری را جنایت علیه بشریت و نسل‌کشی طبقه‌بندی کرده است.
مرکز آمیا تاکید کرد حق دانستن حقیقت، دسترسی به عدالت و تعهد بین‌المللی به تحقیق و مجازات جنایات علیه بشریت نباید به‌دلیل پناه گرفتن عامدانه متهمان در خارج از کشور بی‌اثر شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/78522" target="_blank">📅 17:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37b765df18.mp4?token=qDz_bueLRTp_eSzEQVyNe6D8FlT2fv0z2vU9XchueZ30EmQ6L1IH70jkR5mZbwLEN0YbmS0_7lB75OqEmk0E5LCXiNdzLLBRZ6m8bv0BYAFqFow3kz9ycHpOBAPyq0DkbyCv83xql2Gfzqip3LVwdUxNq3hOcv0Cb3nGjcjgzwRVaVoRuE9NqCiEwFeT73MIMVnPaK_vrdW8LsY7qJuo17g30Qgp5wwaVGLODYOIHfe8KNoBowx4SoF-npU-BdiGmjuyzKox0Oe1V0o97UTTb9yK7VwTU58mlMn3ohyzSQk1JJN_hlTI5h1DKcJ2IQdqhbYVOqf8mxd-KpdWHaxQ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37b765df18.mp4?token=qDz_bueLRTp_eSzEQVyNe6D8FlT2fv0z2vU9XchueZ30EmQ6L1IH70jkR5mZbwLEN0YbmS0_7lB75OqEmk0E5LCXiNdzLLBRZ6m8bv0BYAFqFow3kz9ycHpOBAPyq0DkbyCv83xql2Gfzqip3LVwdUxNq3hOcv0Cb3nGjcjgzwRVaVoRuE9NqCiEwFeT73MIMVnPaK_vrdW8LsY7qJuo17g30Qgp5wwaVGLODYOIHfe8KNoBowx4SoF-npU-BdiGmjuyzKox0Oe1V0o97UTTb9yK7VwTU58mlMn3ohyzSQk1JJN_hlTI5h1DKcJ2IQdqhbYVOqf8mxd-KpdWHaxQ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دنی دانون، سفیر اسرائیل در سازمان ملل، در ویدیویی که منتشر کرد، یک دستگاه استارلینک را به ناصر اسدی، نماینده جمهوری اسلامی، پیشنهاد داد و گفت: «می‌خواهید آن را بگیرید و به تهران ببرید؟ می‌تواند در ایران برایتان بسیار مفید باشد.»
دانون در این ویدیو می‌گوید: «فکر کردم مناسب است این استارلینک را به شما بدهم. اگر سخنان نخست‌وزیر را شنیده باشید، می‌تواند بسیار به کارتان بیاید تا پس از آنچه با مردم ایران کردید، اجازه دهید به آزادی برسند.» او همچنین گفت: «ما مردم ایران را دوست داریم و برای تغییر رژیم در آنجا دعا می‌کنیم. آن روز خواهد رسید.»
این همان دستگاه استارلینکی است که بنیامین نتانیاهو هنگام سخنرانی در مجمع عمومی سازمان ملل نشان داد و از رئیس جلسه خواست آن را به هیات جمهوری اسلامی بدهد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/78521" target="_blank">📅 06:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1BVOKxXF0_A6cpxqf_LSAo3Rck0YOzDFox09koubq9dwBeg5R8UHeZhj0Z-eoW14cn5VHEpLsaBn3Pm5cMDhJYhsYrgR-QET3Vg1yoceiVMDAA_f3GpiGc3oRt9OQRG486EVs5Diudf_FuWCBpvjkKK9Iefi_r2AbR7algBs_u1XKYqsQaGHe9-3WN-MQ_ph4a7iabd6BnQnCWesN3HnVQggHVH1WrE9lM2MZqYQboHhEus3-Ppkalm8Ib4_zk2lQZoL0yLYJJpH6D-ERQdqLt4h7NcAO7HkosKER9HO5q956AHCEIWnubLzPueA6OgUAqGHODRWiLVJ7q1uhS7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش سی‌ان‌ان، عباس عراقچی، وزیر امور خارجه جمهوری اسلامی ایران، پنجشنبه دوم مهر گفت تهران پیشنهادی به آمریکا ارائه کرده است که می‌تواند به بازگشایی تنگه هرمز و ازسرگیری مذاکرات برای دستیابی به یک «توافق نهایی» منجر شود.
عراقچی گفت این پیشنهاد در هفته جاری از طریق میانجی‌ها به واشنگتن ارائه شده و بر اساس آن، آمریکا باید ظرف هفت روز شروط مشخصی را اجرا کند تا مذاکرات از سر گرفته شود و تنگه هرمز بازگشایی شود. او جزئیات این شروط را بیان نکرد، اما گفت این موارد «چیزی بیشتر» از مفاد تفاهم‌نامه اسلام‌آباد نیستند.
بر اساس این گزارش، تفاهم‌نامه اسلام‌آباد که در خرداد میان ایران و آمریکا به دست آمد، شامل کاهش تحریم‌ها، آزادسازی دارایی‌های مسدودشده ایران و توقف عملیات نظامی، از جمله در لبنان، بود. یک مقام کاخ سفید نیز در واکنش به اظهارات عراقچی به سی‌ان‌ان گفت گفتگوها از طریق میانجی‌ها «مثبت و سازنده» بوده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/78520" target="_blank">📅 06:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">مسعود پزشکیان در مصاحبه با فاکس‌نیوز، از آمادگی جمهوری اسلامی برای توافق و کاهش غلظت اورانیوم غنی‌شده خبر داد، اما درباره محل نگهداری ذخایر هسته‌ای و تضمین تبعیت سپاه از توافق، پاسخ روشنی نداد.
مجری این شبکه همچنین با اشاره به کشته‌شدن معترضان و حملات نظامی برخلاف وعده‌های رییس‌ دولت جمهوری اسلامی، پرسید: «چه کسی در ایران حکومت را در کنترل دارد؟»
پزشکیان در این گفت‌وگو تاکید کرد جمهوری اسلامی خواهان جنگ نیست و مدعی شد جنگ به ایران تحمیل شده است. او گفت تهران آماده دستیابی به توافقی در چارچوب حقوق بین‌الملل است، اما فشار برای وادار کردن جمهوری اسلامی به تسلیم را نخواهد پذیرفت.
او با اشاره به توافق و تفاهم‌نامه‌ای که به گفته‌اش پیش‌تر با طرف آمریکایی امضا شده بود، از تمایل به ادامه همان مسیر سخن گفت و آمریکا و اسرائیل را مسئول حملات و کشته‌شدن رهبر پیشین جمهوری اسلامی، فرماندهان، دانشمندان و مقام‌های دولتی دانست.
بخش مهمی از مصاحبه به میزان اختیار پزشکیان بر نیروهای نظامی اختصاص یافت. مجری با کنار هم گذاشتن وعده خودداری از اعمال زور علیه معترضان، عذرخواهی از کشورهای همسایه بابت حملات و اقدام فرماندهان علیه کشتی‌ها بدون اطلاع «رییس‌جمهوری»، پرسید چرا تعهدهای او چند بار نقض شده است.
پزشکیان ابتدا به آمار کشته‌شدگان اعتراضات پرداخت. هنگامی که مجری دوباره پرسید چه کسی تضمین می‌کند سپاه از توافقی که او امضا می‌کند پیروی کند، گفت قرار بوده گروه‌هایی برای هماهنگی، رفع سوءتفاهم و ایجاد کانال ارتباطی تشکیل شوند، اما فرصت راه‌اندازی آن‌ها فراهم نشده است. او همچنین نیروهای آمریکایی را به شلیک خودسرانه در منطقه متهم کرد.
مجری در ادامه پرسید: «چرا رییس‌جمهوری ترامپ باید با شما مذاکره کند و نه با فرمانده سپاه، ژنرال وحیدی؟» پزشکیان در پاسخ، از بی‌اعتمادی عمیق میان تهران و واشینگتن و خروج ترامپ از برجام سخن گفت، اما توضیح مشخصی درباره حدود اختیار خود در برابر فرمانده سپاه ارائه نکرد.
مجری با اشاره به آمار نهادهای حقوق بشری و گزارش مجله تایم، پزشکیان را به چالش کشید و پرسید: «شما جراح قلب هستید. چند نفر از ایرانیان در ایران توسط نیروهای امنیتی کشته شدند؟»
پزشکیان بار دیگر آمار رسمی منتشر شده توسط حکومت را تنها آمار واقعی اعلام کرد. او گزارش‌های خارج از کشور را مغایر اطلاعات حکومت دانست و خواستار ارائه مدارک هویتی قربانیان شد. در عین حال، از ضعف مدیریت رویدادها ابراز تاسف کرد و گفت استفاده از سلاح در تظاهرات خیابانی پذیرفتنی نیست.
ادامه گزارش :
pezeshkian
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78519" target="_blank">📅 05:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78518">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ویدیوی کامل با ترجمه ماشین
بخش‌هایی در خبرها:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «می‌خواهم با دقت به سخنانم گوش کنید. روزی، و شاید آن روز چندان دور نباشد، مردم ایران آزاد خواهند شد.»
او افزود: «حکومت آدم‌کش آنها به‌دلیل دروغ‌هایش، فسادش و بی‌رحمی‌اش سرنگون خواهد شد. این حکومت شرور سقوط خواهد کرد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو در بخش پایانی سخنرانی خود در مجمع عمومی سازمان ملل متحد، بار دیگر به خروج نمایندگان کشورها از سالن و حضور معترضان در مقابل ساختمان سازمان ملل واکنش نشان داد. او با یادآوری سرکوب اعتراضات در ایران، خطاب به این افراد گفت: «زمانی که رژیم ایران هزاران نفر از مردم خودش را کشت، شما کجا بودید؟ شما درباره مردم ایران هیچ چیزی نگفتید.»
نتانیاهو در ادامه تاکید کرد: «اما باوجود سکوت و ریاکاری شما، نیروی مردم ایران چیره خواهد شد. فقط مساله زمان است. یک روزی که شاید خیلی دیر نباشد، مردم ایران آزاد و پیروز خواهند شد و این رژیم پلید سرنگون خواهد شد و همه ما آن روز را جشن خواهیم گرفت.»
@
VahidOOnLine
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «مستبدان تهران؛ می‌دانید از چه چیزی بیشتر از همه می‌ترسند؟ از مردم خودشان؛ مردم شجاع ایران که برای مدتی طولانی، فداکاری‌های بسیاری کرده‌اند.»
نتانیاهو افزود: «از معترضان بیرون و نمایندگان ریاکاری که این سالن را ترک کردند می‌پرسم: کجا بودید وقتی مستبدان ایران ده‌ها هزار غیرنظامی بی‌سلاح ایرانی را کشتند و مجروح کردند؟ وقتی هزاران نفر از مردم خودشان را کشتند و مجروح کردند، کجا بودید؟
آیا تجمع‌های گسترده برگزار کردید؟ اعتصاب غذا کردید؟ آیا مقابل نمایندگی ایران در سازمان ملل اعتراض کردید؟ آیا در دفاع از مسیحیانی که در ایران و سراسر خاورمیانه تحت آزار قرار دارند، سخنی گفتید؟ نه. چنین کاری نکردید، زیرا شما معترضان قلابی حقوق بشر هستید.»
@
VahidOOnLine
ده‌ها نماینده حاضر در مجمع عمومی سازمان ملل متحد روز پنج‌شنبه ۲۴ سپتامبر، همزمان با آغاز سخنرانی بنیامین نتانیاهو، نخست‌وزیر اسرائیل، سالن را ترک کردند.
نتانیاهو در واکنش، نمایندگانی را که سالن را ترک کردند «بزدلان بی‌اخلاق» خواند و از دیگر افرادی که قصد خروج داشتند خواست پیش از آغاز سخنرانی او سالن را ترک کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در مجمع عمومی سازمان ملل گفت: «قطر میزبان عاملان کشتار هفتم اکتبر حماس است. اکنون تازه‌ترین کشوری که به عامل گسترش گسترده دروغ‌های یهودستیزانه تبدیل شده، ترکیه است.»
او افزود: «اردوغان یک مستبد است. او نیز میزبان رهبران تروریستی حماس است. او هزاران غیرنظامی کرد را کشته، نسل‌کشی ارامنه را انکار می‌کند و روزنامه‌نگاران و رهبران مخالف را زندانی می‌کند. در واقع، فکر می‌کنم در این زمینه رکورددار جهان است و البته رقابت سختی هم وجود دارد. اما فکر می‌کنم او نفر اول است.»
نتانیاهو گفت: «او به‌طور غیرقانونی قبرس شمالی، بخشی از کشوری عضو اتحادیه اروپا، را اشغال کرده و به‌طور مرتب علیه یونان، عضو ناتو، دست به اقدام می‌زند. اکنون می‌خواهد سوریه را تصرف کند.»
او افزود: «البته این تعجب‌آور نیست، زیرا تقریبا هر روز خواستار نابودی اسرائیل می‌شود. او می‌گوید قرار است حاکم اورشلیم شود. نه آقا، نخواهید شد. این کشور ما، شهر ما و پایتخت ابدی ما است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 373K · <a href="https://t.me/VahidOnline/78518" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/475bcac205.mp4?token=tnPSJPAaSwdFtZ215fS19kpBBsKfoRJuyDGgxPl67y7CeGYZkP1ydbPqWZITfRKlPTTUXhpa2CZgUPlPsSFYYA1Mcwqy6pGhfW3D4fyp6fWSo4awowRd41ygGxw10jLkT2NsAYkvKAboBzr1u9NfridwpFu8fagfhWQJMMRKgsCaKTiWGKrKbupyR9k13NcbNdYxQFJXZXcFKspuXozng39TmbmNOXZQnE8Xav6drFQJVnAqaCpz-guHdkTEZ-SCHrvtzEhyPiFTpFr0IoLyUeRPLSZtAvqX_DOJaoc41HZ6-cRDLfkn5HacnYx3di_lLawYW1uYRfLSpDr-T0sUfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/475bcac205.mp4?token=tnPSJPAaSwdFtZ215fS19kpBBsKfoRJuyDGgxPl67y7CeGYZkP1ydbPqWZITfRKlPTTUXhpa2CZgUPlPsSFYYA1Mcwqy6pGhfW3D4fyp6fWSo4awowRd41ygGxw10jLkT2NsAYkvKAboBzr1u9NfridwpFu8fagfhWQJMMRKgsCaKTiWGKrKbupyR9k13NcbNdYxQFJXZXcFKspuXozng39TmbmNOXZQnE8Xav6drFQJVnAqaCpz-guHdkTEZ-SCHrvtzEhyPiFTpFr0IoLyUeRPLSZtAvqX_DOJaoc41HZ6-cRDLfkn5HacnYx3di_lLawYW1uYRfLSpDr-T0sUfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبران دو اقتصاد بزرگ جهان روز پنج‌شنبه، دوم مهر، در کاخ سفید دیدار و دربارهٔ موضوعاتی از تجارت و تعرفه‌ها گرفته تا تایوان، هوش مصنوعی و جنگ ایران گفت‌وگو کردند.
در این دیدار که در کاخ سفید برگزار شد، شی جین‌پینگ از ایران و آمریکا خواست که در اسرع وقت مشکلاتشان را با گفت‌وگو حل‌وفصل کنند. رئیس‌جمهور چین همزمان از میزبان آمریکایی‌اش خواست که به‌سرعت و از طریق مذاکره، جنگ با ایران را پایان دهد.
رویترز به‌نقل از منابع آگاه گزارش کرده بود که چین در گفت‌وگوهای پیش از سفر شی جین‌پینگ، در مقابل امتیاز احتمالی آمریکا در زمینهٔ فروش تسلیحات به تایوان، پیشنهاد همکاری در اعمال فشار بر ایران را مطرح کرده است. این پیشنهاد به‌طور رسمی از سوی پکن تأیید نشده است.
تایوان از دیگر موضوعات حساس دیدار روز پنج‌شنبه بود. چین این جزیرهٔ دارای حکومت دموکراتیک را بخشی از قلمرو خود می‌داند و بارها با فروش تسلیحات آمریکا به تایوان مخالفت کرده است.
به گزارش خبرگزاری رسمی چین، شین‌هوا، آقای شی در کاخ سفید از دونالد ترامپ خواست که در قبال موضوع «استقلال» تایوان، با «دوراندیشی و احتیاط» رفتار کند.
این دومین دیدار ترامپ و شی در سال جاری میلادی و نخستین سفر رئیس‌جمهور چین به واشینگتن در بیش از یک دهه است.
شی جین‌پینگ عصر چهارشنبه به‌وقت محلی وارد آمریکا شد و دونالد ترامپ در پای هواپیمای او در پایگاه اندروز از وی استقبال کرد.
این نخستین بار در ۱۱ سال گذشته است که یک رئیس‌جمهور آمریکا برای استقبال از یک رهبر خارجی به این پایگاه می‌رود. آخرین بار باراک اوباما در سال ۲۰۱۵ در آن‌جا از پاپ فرانسیس استقبال کرده بود. موضوعی که نشانه‌ای از احترام ویژۀ دونالد ترامپ به همتای چینی‌اش به‌شمار می‌رود.
کاخ سفید همچنین برای پنجشنبه‌شب ضیافت رسمی شامی ترتیب داده که شماری از مدیران شرکت‌های بزرگ فناوری آمریکا از جمله اپل، آمازون، آلفابت، اوپن‌ای‌آی، تسلا و انویدیا به آن دعوت شده‌اند.
شی جین‌پینگ چهارشنبه‌شب در بدو ورود به آمریکا ابراز امیدواری کرد روابط پکن و واشینگتن باثبات‌تر شود و گفت دو کشور باید «شریک باشند، نه رقیب».
پیش از دیدار دو رئیس‌جمهور، مقام‌های ارشد اقتصادی دو کشور بر سر تمدید آتش‌بس تجاری به توافق رسیده‌ بودند.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پس از گفت‌وگو با هه لی‌فنگ، معاون نخست‌وزیر چین، اعلام کرد توافقی که افزایش شدید تعرفه‌های متقابل را متوقف کرده بود، تا ۱۰ ژانویه تمدید خواهد شد. آتش‌بس تجاری فعلی قرار بود در ماه نوامبر به پایان برسد.
در جریان جنگ تجاری دو کشور، تعرفه‌های متقابل در مقطعی از ۱۰۰ درصد نیز فراتر رفته بود.
مقام‌های آمریکایی همچنین از احتمال اعلام توافق‌هایی در زمینهٔ کشاورزی و موانع غیرتعرفه‌ای خبر داده‌اند. آمریکا می‌گوید چین در اجرای تعهد خود برای خرید ۲۰۰ فروند هواپیمای بوئینگ نیز پیشرفت‌هایی داشته، هرچند هنوز سفارش تازه‌ای اعلام نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/78517" target="_blank">📅 18:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78516">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2513034044.mp4?token=bpD9Aszhi0TD3pBEcO6Fk6x7IpcOjFyqDjCes6h2Lw-hvbto2ykcO9X4oDLJP42FMJrwK72zgLjGbTO3PPPkGRMlxcdy4HZ_64voRrFU0RrJnGiHUVPnftItbtquBhnqVSGTnsqJ_DUomctw4tyfM65ZX0xYeW3SLX2EC6kHOBFLepKDzbw_lTsOcxxVO7UKbSvmY6HyqVnIKibutOEl1ddMTyWavqfWdjU7YQreu_400e4hZjR8b5RlKGjYcZidbrnk6E2fM9TaC7qwUwyECS2VXni0nJA8_G7Wr0M23Qb4Sl3T7NHR3U-raMV5id0xH7Sr_Zt2_E-WsR_tQzS5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2513034044.mp4?token=bpD9Aszhi0TD3pBEcO6Fk6x7IpcOjFyqDjCes6h2Lw-hvbto2ykcO9X4oDLJP42FMJrwK72zgLjGbTO3PPPkGRMlxcdy4HZ_64voRrFU0RrJnGiHUVPnftItbtquBhnqVSGTnsqJ_DUomctw4tyfM65ZX0xYeW3SLX2EC6kHOBFLepKDzbw_lTsOcxxVO7UKbSvmY6HyqVnIKibutOEl1ddMTyWavqfWdjU7YQreu_400e4hZjR8b5RlKGjYcZidbrnk6E2fM9TaC7qwUwyECS2VXni0nJA8_G7Wr0M23Qb4Sl3T7NHR3U-raMV5id0xH7Sr_Zt2_E-WsR_tQzS5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش ریال در مقابل دستمال کاغذی
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78516" target="_blank">📅 17:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=flQeZrQI1K63xmY6NW4YTt9RzVztXXvTQi2IGJdJPGa_NR7HLrV1BkWfBEpXkH7jSXoyvPeCVhWOXLH8zOsBB1hRuj0l8bj-7KKzILjuAPLIzalKO6O4DDvOcWJeYY343X5WY9JW37PpNAPwmyz44jEihQMvj5ko7ECADiB6zp-pmqx13gTJOAd9U6FzQiUk0McZ_ItnIKFHh7bgCOGhRzNgBJDvQqUvcCLE3N_1DxL372o9p1N66znL57nEMz56xHeO7BeHZJKW9t3T5EUMfOuqeodp2utb9GanLrEwdVDj11mHHnciw1VByMfzEtG_u9eAYGTKnKpH9AFVYbHAwYk4awUJ5JoqtyFE2NlcY3DwrUUx2cMylVaLOUh5ro1qWbdS_xPKWHEl1bC1D5og8O9KFuzp8KCEmB2WK7FSWmOxQvUJ-w7cm99mYGgmFVtZiIUGVkFLX3cq2JBP0QR9WnzlgytFvepRrVjLU5gdg0i6AvOq5EOZbKSepJceiLEiUFeFdsNjbpL8LtaPN3orX1wnbsn50H10QiugwVpk1O663QzE0GJwi9vI_QdMBDtVwahrSbkROWTdBcng_9iWc20ZtFTVyTVF3VwTAbJV7HcRp6VS05WYqndMwPs161uQKDg6M-hhDebjXJJRJmT77_Rw7IS6XDvkB6Nhosj3mcY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/29d6b98e99.mp4?token=flQeZrQI1K63xmY6NW4YTt9RzVztXXvTQi2IGJdJPGa_NR7HLrV1BkWfBEpXkH7jSXoyvPeCVhWOXLH8zOsBB1hRuj0l8bj-7KKzILjuAPLIzalKO6O4DDvOcWJeYY343X5WY9JW37PpNAPwmyz44jEihQMvj5ko7ECADiB6zp-pmqx13gTJOAd9U6FzQiUk0McZ_ItnIKFHh7bgCOGhRzNgBJDvQqUvcCLE3N_1DxL372o9p1N66znL57nEMz56xHeO7BeHZJKW9t3T5EUMfOuqeodp2utb9GanLrEwdVDj11mHHnciw1VByMfzEtG_u9eAYGTKnKpH9AFVYbHAwYk4awUJ5JoqtyFE2NlcY3DwrUUx2cMylVaLOUh5ro1qWbdS_xPKWHEl1bC1D5og8O9KFuzp8KCEmB2WK7FSWmOxQvUJ-w7cm99mYGgmFVtZiIUGVkFLX3cq2JBP0QR9WnzlgytFvepRrVjLU5gdg0i6AvOq5EOZbKSepJceiLEiUFeFdsNjbpL8LtaPN3orX1wnbsn50H10QiugwVpk1O663QzE0GJwi9vI_QdMBDtVwahrSbkROWTdBcng_9iWc20ZtFTVyTVF3VwTAbJV7HcRp6VS05WYqndMwPs161uQKDg6M-hhDebjXJJRJmT77_Rw7IS6XDvkB6Nhosj3mcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی قلهکی، از منابع "نزدیک به حکومت"، با انتشار این ویدیو نوشته:
'''
اختصاصی: «تاجیکستان» و «جمهوری آذربایجان» آسمان خود را بر روی پروازهای «ایران» بستند
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه» _پایتخت تاجیکستان_ از مرزِ هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
🔻
پی‌نوشت: مسیر پرواز هواپیمایی وارش از سمتِ ایرانوبه مقصد «دوشنبه» _پایتخت تاجیکستان_، ورود به آسمان جمهوری آذربایجان و ترکمنستان بود که پیش‌تر آذربایجان و ترکمنستان آسمان خود را بر روی پروازهای ایرانی بستند و پرواز نتوانست وارد آسمان این دو کشور شود و بالاجبار به کشور بازگشت.
'''
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 344K · <a href="https://t.me/VahidOnline/78515" target="_blank">📅 17:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9ppGkzecEUbD7sIznUItRlYRiBMkTIQVEGsMXnq6i6Z_BUBajQ-qT3PmEKkjXlcqkjN1OQS1I4SXZDYgJPC0NT1IpnHnGo8cfl-jHZq9JLYOQHdtO42QVtRag6yVyqd1HC5R0Wm65Psro4NCSlARqeXQcAYQeBsG4UFGavYMNaCCbyPBVD36ScJdi7jN9bjkIuX0n7sAUB4wSUZdRa6M-XypoAucaQuXjw11aOI0s_8lVepsdSYfwssYtibw22UzJQj2FF1nRBCplARH-UVDuRKgeMshZsWczJuvLT4kKXdyOScj9v1ljcNJKXsQCfvqgZhtUMT89MhWVx152OGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه دوم دادگاه انقلاب رشت ۹ وکیل دادگستری در استان گیلان را در یک پرونده مشترک به مجموع ۱۴ سال‌وهفت ماه‌و۱۵ روز حبس محکوم کرده است.
هرانا خبر داد «معصومه پورشهرانی»، «طاهره پوراسماعیلی»، «شادی فلاحتی»، «غلامحسین لایقی»، «حسام احمدپور»، «لادن آصفی‌راد»، «محمدرضا تاک»، «کیان طاهر‌اجارود» و یک وکیل با نام خانوادگی «دلیلی» در این پرونده محکوم شده‌اند.
هر یک از این وکلا با اتهام «تبلیغ علیه نظام» به هفت ماه‌و۱۵ روز زندان و با اتهام «توهین به رهبری و بنیان‌گذار جمهوری اسلامی» به ۱۲ ماه زندان محکوم شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/78514" target="_blank">📅 17:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3ReKm1l5QQg0X0Y0Pvv-Rvsyw1iwPb3GuQo3S9ZfUOGlWm3uj5UE6MUOvBat1orWyj5J36iZe_nPbBwSokjHgugRjgOLc2LqZA28eGQ7_wxW8O8-xvxBbe483hadtse1EBfoCYOztYvtiTW6Q3_VRmH6WO5LuV2N6OJE_OkEVISAzR-QNfmCEwKRlaJ4UKpuGu73nZh5jPKCYIiX8-EWGJuF2xUchNpjRZoeOp6aGB8rjx_hseB0XORJ6Zi3Ty0QTntW1Mrydnsipc9ZY6DjtNsjgKK2e7HuoY54foVXRHzWkLLS71q5RZzcEeSZFyzoLYmvJNApNKJ0YHoSjAQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات متحده عربی روز چهارشنبه اول مهر فعالیت بانک ملی ایران در این کشور حاشیه خلیج فارس را ممنوع اعلام کرد.
این بانک در بیانیه‌ای اعلام کرد: «این اقدامات در نتیجه تخلفاتی مرتبط با رعایت نکردن مقررات، قوانین و تصمیمات نظارتی لازم‌الاجرا در امارات متحده عربی اتخاذ شده است.»
این نهاد افزود که این تخلفات شامل رعایت نکردن الزامات قوانین مربوط به مبارزه با پول‌شویی، تأمین مالی تروریسم و تأمین مالی اشاعه تسلیحات بوده است.
بانک مرکزی امارات اعلام کرده تمامی شعب بانک ملی ایران در این کشور از انجام تراکنش‌های مالی به مقصد ایران و از ایران، از جمله تأمین مالی تجارت و انتقال وجوه، منع خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 301K · <a href="https://t.me/VahidOnline/78513" target="_blank">📅 17:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_-3chbmgpu_6T_H75PkZmF0b8agb0p50VZvSBBOGlQZnDruli9Gw7CWJiKtY2Eoekmv2Yd0CNWaIJRqwkUo2M_v5eR5h6eb-N7rUH1Ev40l3DGsPtGXoXeqPcNgR5ru7MReuWKnpxOo8SREGNGQSwuem-pMHTglnZLwPGhnhBrJmAbrNp9nZbdO5SaZlhccOpe79pxBUg-HD9doEf0DV2QbFqSyJ-2GNk8CfLZjdEKTdW4nxRe27Z8hG9o4_76oAnnLSBssttjmqfeXiWR5SlCbHvpNiMIFuTFM-vpY7HdgCpiRmCl0wfn6_gEb74pdKIsfTxfn8K2yDZCwjB5QGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تاکید رئیس‌جمهور ایران بر ادامه برنامه هسته‌ای و عزم جمهوری اسلامی برای تسلیم نشدن در مقابل فشارهای آمریکا، ارزش ریال ایران دوباره روند نزولی گرفت.
نرخ دلار در مقابل ریال ایران روز پنج‌شنبه با ۱.۴ درصد افزایش به ۲۳۵ هزار و ۴۰۰ تومان رسید.
نرخ یورو در لحظه تنظیم این گزارش در ظهر روز جاری به نزدیک ۲۶۸ هزار تومان و پوند بریتانیا به ۳۱۳ هزار تومان رسیده است.
سکه امامی با نزدیک به دو درصد افزایش هم اکنون بالای ۲۴۰ میلیون تومان و سکه بهار آزادی با ۱.۷ درصد افزایش بالای ۲۳۶ میلیون تومان معامله می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78512" target="_blank">📅 17:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCX1kvBcYn7TLYjnuZ5CX3LPXPYUbcgcfgiSAvpn89lE1azsugQGPcScIswSI0X-ImOSHv-DXcoUF0s_N49XDNRrJuKbyiBYzmKMRSBRrlL4AyXdwZa3JI8rax49KG7cOAY6B5r84B8s3RIbHV8_MSxCvU9ksxuAY5b2ILoH7qoU7SHgg9J4eMOOVxSmmT5k_3nj78gK9GIL56Oc1BcJl2WT1U0IXjDiZHcfWO25BXQDplVMxBmHC0mHKORld7EbkqzczRYSZi_oKdyxDYtBcW73eGZYIfYHg8kXfTikeLIfvGyw6hcAseX_riSeznr0uAHB5OwgtU3w6pwyxmFU5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت ردیابی نفتکش‌ها «تانکر ترکرز» می‌گوید نزدیک به شش میلیون بشکه نفت خام توقیف‌شده ایران، به ارزش تقریبی ۶۰۰ میلیون دلار، در حال عبور از اقیانوس اطلس به مقصد ایالات متحده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78511" target="_blank">📅 17:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sFzxM3N8zsQZ8tSZf1Y3sg8dzkoUCl8tQ58yV2pce6E7oP5yS2_9m89w4zHXLRgPwQdxfDdFd8eLz3mfqOetpjGUv5DTqrti8-RO3UUkKkQZc6Lykfouwnco4878uFEG7Mnp5dWfhtBfMPvSVq_TTpL7dCJPaX-5SXS5_vIXu49dYIvJ8qPCwCTmB3BQ7csXSrkoKalAWdPQdbnRNfFxbwfudW-j32iu-pCDbhKfvEH3JFb2N8vQRAGmr2BredE4KR6fR_stQC7r-DElaRYIMh2TduWx5l0_iRlXwSZ5ZcNr33TlySYQ0vUpet_3R0esRuDwaK7Ds2vAxzAJZn26ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس اطلاعات رسیده به ایران‌اینترنشنال، همه پروازهای شرکت‌های هواپیمایی ایرانی به امارات متحده عربی لغو شد.
پرواز شرکت‌های هواپیمایی ایرانی به امارات از شهرهایی از جمله تهران، کیش، مشهد و شیراز برقرار بود که اکنون لغو شده است.
لغو این پروازها پس از اجرایی شدن محدودیت‌های اعلام‌شده آمریکا علیه فعالیت خارجی شرکت‌های هواپیمایی ایران صورت می‌گیرد.
اسکات بسنت، وزیر خزانه‌داری آمریکا، پیش‌تر اعلام کرده بود از اول مهر فعالیت شرکت‌های هواپیمایی ایران در خارج از کشور متوقف خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78510" target="_blank">📅 17:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJTFlzLxrvyhe7J7ukPmxYGFA1AIjWxxuDjwsIz0QMNd9IHjUNopUmeVs2ZgdqwrImR8TsiZmRXKFe0L6JfhoBOBLOZlh4XrpWX9_uRNGAg9xDI0SYosbhkP93z8jNtb2SC2-TvwA7tRCbZz_wy2BZ_z-RHF2h_qJ0iSrWDvZLeRAUVSsDgXijzeQSdCrYxMS01hhnu5QTnSgfJzb6GHXXc4FP9fCtcWNZ9FPPsqgrOzxn1k1kykhCXG9XG29wl6gehczp4MfqSQBAViZMudNQWQUV_ymEe5tUQFceqeHBRhWqft1i7pKtQXRhrUXGmhc6T64pl1x97RQbiTRIkjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دفاع مدنی عربستان سعودی پنجشنبه دوم مهرماه، با صدور هشداری از تلاش دوباره برای حمله به مکه خبر داد.
این هشدار برای شهر مکه صادر و پس از لحظاتی لغو شد.
عربستان سعودی برای برخی از شهرهای ساحلی دریای سرخ از جمله طائف، جده و تبوک، نیز همزمان هشدارهایی صادر کرد.
در همین ارتباط ترکی المالکی، سخنگوی رسمی نیروهای ائتلاف بین‌المللی، اعلام کرد که شش فروند موشک بالستیک شلیک‌ شده از سوی شورشیان حوثی، رهگیری و منهدم شده و پدافند هوایی نیز تلاش برای هدف قرار دادن طائف و ینبع را خنثی کرده است.
هفته گذشته نیز عربستان سعودی، شورشیان حوثی را متهم به تلاش برای حمله موشکی به شهر مکه کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/78509" target="_blank">📅 17:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CF7i9eun_FgbxBcITIGS6uzJBD6DoPoeaTxleufe2Fc-ljfAq6_NZq7hNNNkApoPYZrTLE2mT5Hf8y_2GOLadzExzSmA2gaG4sJpNkADeu8y9nyboXCBjDGDH8msGQNENMvSXrV4uvVsPXWD8zndmhWrPCwEmIza0lYAEVaJMqVGDfkg-CGp-Oaw63qDQWkhwbIqKL1SpcbLlZSL-OTEn0CFf-59YvDFRgUtP66ZKAegfbxkxX0qaWm1cKQiIlVAWfeyopSHibVecTsOgydWog-pExGFVnbg2CsnQo8_06mT43aPvyMH5bdwvQbFSu91WioDsgiKTE2MMCS_p4q-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام «ارغوان فلاحی»، زندانی سیاسی محبوس در زندان اوین، پس از پذیرش اعاده دادرسی متوقف شده و پرونده او قرار است برای رسیدگی مجدد به شعبه هم‌عرض فرستاده شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/78508" target="_blank">📅 17:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a986602075.mp4?token=sDbgnb2Bwd8zS00VEpNhHH1vq0kJSk4MKUOLyf1qeeTLxoSe60gIDWGT567sCqvY_Ism7U1IAYykX46MvfDIUD9emhJgLMqOxTz2qKYSLy6Z-WsUEMOVLDuFlSUnlfJ2kWMpWLHjm7fpoJgPCSkDQQaEL1_IQEm5N1APfVh70sQgZa6qrK0grEkc8to7J-Sg3GsbxL4Si9cSSqsLgHlAG4AvlZ2cPz-IwYRcK_SYRMfyNENcxtxfP23PNQHtAO9_4Lli_dsZ0ghjPgEuxQEglY6VyOJG2cV-1G7gg9_SFOLReqTw1713TDNoIt8kNDJCGwuBe0HYsXfECtGkqCL7RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a986602075.mp4?token=sDbgnb2Bwd8zS00VEpNhHH1vq0kJSk4MKUOLyf1qeeTLxoSe60gIDWGT567sCqvY_Ism7U1IAYykX46MvfDIUD9emhJgLMqOxTz2qKYSLy6Z-WsUEMOVLDuFlSUnlfJ2kWMpWLHjm7fpoJgPCSkDQQaEL1_IQEm5N1APfVh70sQgZa6qrK0grEkc8to7J-Sg3GsbxL4Si9cSSqsLgHlAG4AvlZ2cPz-IwYRcK_SYRMfyNENcxtxfP23PNQHtAO9_4Lli_dsZ0ghjPgEuxQEglY6VyOJG2cV-1G7gg9_SFOLReqTw1713TDNoIt8kNDJCGwuBe0HYsXfECtGkqCL7RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ تن از آسیب‌دیدگان چشمی خیزش مهسا با انتشار پیامی ویدیویی، خواستار لغو حکم اعدام علی زارعی شدند.
غزل رنجکش، عرفان رمیزی‌پور، مرسده شاهین‌کار، مجید موافق، حسین نوری‌نیکو، حمیدرضا حیدری، سالار وطن‌شناس، پارسا قبادی و علی دلپسند در این پیام از مردم و نهادهای حقوق بشری خواستند در برابر جنایات جمهوری اسلامی سکوت نکنند، صدای علی زارعی باشند و برای جلوگیری از اجرای حکم اعدام او تلاش کنند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 377K · <a href="https://t.me/VahidOnline/78507" target="_blank">📅 17:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">پیام‌های دریافتی:
ساعت ۰۰:۱۳
انفجار شدید بندرعباس
همین الان بندرعباس موج انفجار حس شد
وحید قشم لرزید
انفجار دریا بود
00:24  بندرعباس، صدای خفیف انفجار از دور
سلام حدود ساعت ۱۲ یه موج شدید پنجره های ما رو تو بندرعباس لرزوند
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 448K · <a href="https://t.me/VahidOnline/78505" target="_blank">📅 00:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78504">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kBwdm27KgsInggjXo8WmzFXWQ49-zTlvzVdR8scYzJZu37VlmaZTrpvxpbhbe27TfTOq99YP8GAHsH4cspGkkrn5ZXGqTh1l1Hgvgpke0fQq9Gcn0sg2nm73JsEg9MQ-Rvm9Rw6n6yh2mGgQSxVonzGNe0xrZqsXLdhXzBVSGDpC6T-m2HQZ_fWGTG-d_GjMgGUIrvKp5fBX777yL-gw7P8Mi7IC_kLnlksdaO-Pyo-Uh6Ux_M71D-anyoIkJoEaipaNFFUlNs7SV_TrLIYYYUY7ti0EqHoqiSgwYJRW4SKgyaDproJ3CkhBFVar12B6FmC6C4_i1sb1Nn0q1mcgiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط‌عمومی قرارگاه قدس نیروی زمینی سپاه پاسداران، از کشته‌شدن سرتیپ حسین ظریفی، فرمانده عملیاتی قرارگاه سجاد شهرستان سراوان، در جریان یک درگیری مسلحانه در این منطقه خبر داد.
روابط عمومی سپاه، روز اول مهر ۱۴۰۵، در بیانیه خود نوشت ظریفی در جریان «آخرین عملیات رزمندگان این قرارگاه در منطقه سراوان» کشته شده است.
همزمان، حال‌وش گزارش داده است که احمد هراتی زراعتی، مسوول اطلاعات قرارگاه عملیاتی سجاد سراوان، نیز در جریان درگیری نیروهای نظامی با افراد مسلح در منطقه جهاد آباد سراوان کشته شده است.
بر اساس گزارش حال‌وش، این درگیری روز چهارشنبه یکم مهر رخ داده و دست‌کم ۱۳ نیروی نظامی و امنیتی دیگر نیز در جریان آن به‌شدت زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 450K · <a href="https://t.me/VahidOnline/78504" target="_blank">📅 21:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78503">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/813923332b.mp4?token=deLlMbATTwkyPs_-fh8th7QJHEzBbwqVcwXJ2BRBaMJ0zPT0htD1wpJCkuwtbFNSH2-yWiogLZCt-LL5rNFxBvUFZ0pkweAiFlKoC1bH0fxT2voJcmyQ1HI6yW3VZ6xvIH5XUiKVnwsGsGl-Mb-TkELGQvspBGsICbeZOlCT6IyZmJDngrfLtlB5nH7rvpx2wfUwLSU5H85_ipcj1oThMKcYBdFZuWiqDX0lsMtEiMqEnaEI0iz2HHRzOzQ6ob04c5hN30QgXOz9q32Q_gxhGzyRg14xDoDNYLaIh0M-7JUkX50q7omPZoDnfu8P4heVEXxNnUFRQynxb66OZRye6A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/813923332b.mp4?token=deLlMbATTwkyPs_-fh8th7QJHEzBbwqVcwXJ2BRBaMJ0zPT0htD1wpJCkuwtbFNSH2-yWiogLZCt-LL5rNFxBvUFZ0pkweAiFlKoC1bH0fxT2voJcmyQ1HI6yW3VZ6xvIH5XUiKVnwsGsGl-Mb-TkELGQvspBGsICbeZOlCT6IyZmJDngrfLtlB5nH7rvpx2wfUwLSU5H85_ipcj1oThMKcYBdFZuWiqDX0lsMtEiMqEnaEI0iz2HHRzOzQ6ob04c5hN30QgXOz9q32Q_gxhGzyRg14xDoDNYLaIh0M-7JUkX50q7omPZoDnfu8P4heVEXxNnUFRQynxb66OZRye6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا، روز چهارشنبه، اول مهرماه، در حاشیه نشست‌های مجمع عمومی سازمان ملل متحد در نیویورک، از ادامه رایزنی‌ها با میانجی‌گران درباره ایران خبر داد و جلوگیری از دستیابی تهران به سلاح هسته‌ای را مهم‌ترین موضوع در هرگونه توافق احتمالی دانست.
به گفته روبیو، دونالد ترامپ همچنان برای دستیابی به توافق با ایران آمادگی دارد، اما چنین توافقی نیازمند مذاکرات دشوار و فشرده با مشارکت میانجی‌گران خواهد بود.
وزیر خارجه آمریکا همچنین با اشاره به تنگه هرمز، از ادامه عبور نفتکش‌ها از مسیر جنوبی خبر داد و حفاظت از کشتی‌رانی و باز نگه داشتن تنگه را از ماموریت‌های ارتش آمریکا عنوان کرد.
روبیو درباره جزئیات رایزنی‌های دیپلماتیک توضیح بیشتری نداد و تاکید کرد: «اگر قرار باشد توافقی حاصل شود، این اتفاق در یک نشست خبری رخ نخواهد داد.»
@
VahidOOnLine
روبیو در واکنش به سخنان مسعود پزشکیان که ایالات متحده را به نقض قوانین بین‌المللی متهم کرده بود، به شدت از تهران انتقاد کرد.
روبیو با اشاره به کشته شدن هزاران نفر از مردم در تظاهرات، حمایت مالی از گروه‌های تروریستی برای حمله به همسایگان و تاسیسات انرژی، و سرپیچی از قطعنامه‌های هسته‌ای تاکید کرد که جمهوری اسلامی ایران بزرگ‌ترین ناقض نظام بین‌المللی در جهان است.
او تصریح کرد: «نمی‌دانم ایران چه حقی دارد که به کسی درباره حقوق بشر یا نظام بین‌المللی موعظه کند، در حالی که خود به طور مداوم آن را نقض می‌کند.» وزیر خارجه آمریکا افزود که حکومت ایران با قتل‌عام مردم خود، نقض حاکمیت کشورهای همسایه و بی‌اعتنایی به قوانین جامعه جهانی، صلاحیت اظهارنظر در این زمینه را ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/78503" target="_blank">📅 20:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78502">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=MtJEzcXt1aFIxpQqdMYfABms16mqhdWGNotg3CFfX-JAdVfQKq3ZEVt6axYkyD8GMthJLhJdx8H7G9pY-H4JZGsHa2X3az7k6imGCHoKzeZG2Euvnv99aZ-0amtlbQN673_syLvRAU-pI2MTFizM_e9A3u5Ux9bDxA2vy8CjMEZXdLHzrFsDQC38TN4p7aUOtV1NfgWYcaiYaJF4tm6RIKmHGROrwJQ8k41iihw-gF351XBgSXprCYx_52avj9MnuncpGeiXsm-V5Caxbl8l9q51V0FDE8nsStJhgPM1vvAs3J-RPq_V7ao3rEQeT6iUvzipsj3S8BYKcqzEwfgqCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f3a6c0f2e6.mp4?token=MtJEzcXt1aFIxpQqdMYfABms16mqhdWGNotg3CFfX-JAdVfQKq3ZEVt6axYkyD8GMthJLhJdx8H7G9pY-H4JZGsHa2X3az7k6imGCHoKzeZG2Euvnv99aZ-0amtlbQN673_syLvRAU-pI2MTFizM_e9A3u5Ux9bDxA2vy8CjMEZXdLHzrFsDQC38TN4p7aUOtV1NfgWYcaiYaJF4tm6RIKmHGROrwJQ8k41iihw-gF351XBgSXprCYx_52avj9MnuncpGeiXsm-V5Caxbl8l9q51V0FDE8nsStJhgPM1vvAs3J-RPq_V7ao3rEQeT6iUvzipsj3S8BYKcqzEwfgqCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی: اگر کشورهای همسایه پروازهایمان را ممنوع کنند، پروازهای آنها نیز متوقف خواهد شد
محسن رضایی، دبیر شورای‌عالی امنیت ملی جمهوری اسلامی، کشورهای همسایه ایران را در واکنش به محدودیت‌های اعمال‌شده علیه پروازهای ایرانی تهدید کرد و گفت اگر این کشورها پروازهای ایران را ممنوع کنند و وارد همکاری با آمریکا شوند، پروازهای فرودگاه‌های آنها نیز متوقف خواهد شد.
رضایی گفت: «اگر کنار آمریکا باشید، ما شما را تماشا نخواهیم کرد» و هشدار داد در صورت ممنوعیت پروازهای ایران و همکاری کشورهای همسایه با آمریکا، «فرودگاه‌هایتان پرواز نخواهد داشت».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78502" target="_blank">📅 19:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78501">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان: از مذاکره برای صلح نمی‌گریزیم
مسعود پزشکیان، رییس دولت در جمهوری اسلامی، چهارشنبه اول مهر در سخنرانی خود در هشتاد و یکمین مجمع عمومی سازمان ملل متحد گفت متن سخنرانی‌اش را از پیش آماده کرده بود، اما پس از سخنان دونالد ترامپ، رییس‌جمهوری آمریکا، و «تروریست» خواندن جمهوری اسلامی، تصمیم گرفت عکس علی خامنه‌ای، رهبر کشته‌شده جمهوری اسلامی، و دانش‌آموزان مدرسه میناب را به حاضران نشان دهد.
پزشکیان همچنین گفت: «هر کسی را که می‌خواهند تخریب کنند، نام تروریست بر آن می‌گذارند. ۲۰۰ سال است که ایران به کشوری حمله نکرده و فقط از خود دفاع کرده، اما ما را عامل ناامنی می‌خوانند.»
او در بخش دیگری از سخنانش گفت: «آمریکا و اسرائیل با آخرین تجهیزات به ما حمله کردند و ما با قدرت دفاع کردیم.»
پزشکیان گفت آمریکا و اسرائیل جنگ را به ایران تحمیل کردند، اما جمهوری اسلامی «با قدرت» دفاع کرد و در عین حال «برای صلح از مذاکره نمی‌گریزد».
او درباره برنامه هسته‌ای جمهوری اسلامی گفت: «برای دفاع از کشورمان از هیچ‌کسی اجازه نمی‌گیریم. ایران نمی‌پذیرد که دانش هسته‌ای در انحصار چند کشور باشد؛ سلاح هسته‌ای را عامل امنیت نمی‌دانیم.»
پزشکیان در ادامه درباره تنگه هرمز گفت: «نمی‌شود همه از تنگه هرمز بهره ببرند و راه کشتیرانی بر ایران بسته شود. استقرار ناوگان‌های متخاصم و گسترش جنگ باعث امنیت کشتیرانی نمی‌شود.»
او درباره شرایط منطقه نیز گفت: «در منطقه‌ای زندگی می‌کنیم که جنگ مرز نمی‌شناسد و بحران یک کشور به همسایگان سرایت می‌کند. از این رو همسایگان خود را قوی می‌دانیم.»
@
VahidOnLive
پزشکیان: یا امنیت را با هم می‌سازیم یا ناامنی را با هم تحمل می‌کنیم
مسعود پزشکیان در مجمع عمومی سازمان ملل گفت: «صلحی که برای همه نباشد، صلح نیست. یا امنیت را با هم خواهیم ساخت یا ناامنی را با یکدیگر تحمل خواهیم کرد. ما آماده گفت‌وگو هستیم، اما زبان زور را نخواهیم پذیرفت.»
او افزود: «سخنان ترامپ نزد افکار عمومی جهان و اندیشمندان، نشانه بارزی از خوی قلدری و منطق زور و مغایر با منشور صریح سازمان ملل است.»
پزشکیان گفت: «ترامپ بداند که این سخنان ملت ما را منسجم‌تر می‌کند و باید بداند که ملت ما در برابر زور سر خم نکرده و متجاوزان را پشیمان خواهد کرد.»
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/78501" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78499">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EIDFiPNkvOeGCzdJ5V5AslqOJFLRikHuBRnOS_QH6AhgkwPJZevU2Z2DYy73_eGYYQogWzGnqEBzSQtCTx0Vvv0DCEZ2n9J-AE63IR2aRR1ufsB9z3Ryk5cx4KQBIxzqC7c6pFl3pe1Qzqm0CcaY-84FfWEaa42wY31wsconvTzb8uSEbumUYLoDSTkIYhwCJcP9fBU6-NVhBtnwni2C_mPXwTdPDyPX7iwicTgig0_hKJKSyLzFXiIImlPWG0dPp0mKPUm6MGEM8EVRnh-frkBvXxyRmgM01xul58AEAJo54sfmuNKF84r0WjfkaWaFHnwswg2ijTVanYP1p9x_bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/612763335d.mp4?token=SyNTeXK1BNOUKc9h7cNfht-W0ITjD2GHPzSjQKadyG_JJ53j7wWjvNMSI_nq--tw7DxCjaxhlKpJwUeRxIgjzj9Elnc84nwPPf0lOM0EOOJQe-2vKVzwWKWn2mvG3LO49nI5TLWKcdXyxvIeXJp4WEmSK7N_LspwCTmNViNGBi0yaMRhymYUXMSo91BQIw4A0q2GhjguRQ3fJcsiWVFFt7mpGrUUxfu8FABZirEoC5bYrUQ-LQf4GATZyf3FG8_D8AjW5PlHAiul9Nl3cRzTqZ7p1W0fJVB0sc2zgRUwGo7uW53T5yg12o_f2V9-F6kqVgWIxY-gcqrDYjwqnEbeyA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/612763335d.mp4?token=SyNTeXK1BNOUKc9h7cNfht-W0ITjD2GHPzSjQKadyG_JJ53j7wWjvNMSI_nq--tw7DxCjaxhlKpJwUeRxIgjzj9Elnc84nwPPf0lOM0EOOJQe-2vKVzwWKWn2mvG3LO49nI5TLWKcdXyxvIeXJp4WEmSK7N_LspwCTmNViNGBi0yaMRhymYUXMSo91BQIw4A0q2GhjguRQ3fJcsiWVFFt7mpGrUUxfu8FABZirEoC5bYrUQ-LQf4GATZyf3FG8_D8AjW5PlHAiul9Nl3cRzTqZ7p1W0fJVB0sc2zgRUwGo7uW53T5yg12o_f2V9-F6kqVgWIxY-gcqrDYjwqnEbeyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا اعلام کرد یک کشتی باری چهارشنبه یکم مهر در تنگه هرمز با یک پرتابه ناشناس هدف قرار گرفته و پس از آن دچار آتش‌سوزی شده است.
بر اساس این گزارش، همه خدمه کشتی تخلیه شده‌اند و در این حادثه دو نفر آسیب دیده‌اند.
@
VahidOOnLine
کشتی که امروز در تنگه هرمز، هدف حمله سپاه پاسداران قرار گرفت یک کشتی فله بر هندی با نام Cape Dao بوده است. در نتیجه حمله، یک نفر کشته و یک نفر زخمی شده است و کشتی تخلیه شده و در حال سوختن است.
mhmiranusa
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/78499" target="_blank">📅 18:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouafy42PGv4QaholO4qN-_Y2rN_F8kj0d2dor-egYQpEFF2UweHYhlISu4OGPTPKXwlcnmkUKcCYJFbufOK_aqEeM-s1LjKJMcCkF0Bqpap_0V2eFj4JG_vcnb6bQZoey60g8T25ISihLRPmNLbVBgFVekC-_stYHQ7wxlztxIOIFS5XaHnJ7aqOOChXvZtciHsIjo7ncDZwahpSHw2HXTArBC2A9Q65H6hRF6YlAa0gq3zcryE-7pIoAnMtDlhs3w7AXwK06iNK3pZTRE1NHm9kZqWcjNfpDr0Pt-CCZiCQVIjcWDBmym7PHTJnxoj6R_lgZX0pDcuRwAeiteQFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پی تشدید فشار و آزار شهروندان بهایی در ایران، یک شهروند بهایی به نام رومینا گلی، از سوی دادگاه انقلاب ساری به زندان و محرومیت از حقوق اجتماعی محکوم شد.
بر اساس گزارش رسیده، شعبه دوم دادگاه انقلاب ساری، رومینا گلی را بابت اتهام «فعالیت آموزشی یا تبلیغی انحرافی مغایر یا مخل به شرع اسلام»، موضوع ماده ۵۰۰ مکرر قانون مجازات اسلامی، به پنج سال حبس و ۱۰ سال محرومیت از حقوق اجتماعی محکوم کرده است.
این شهروند بهایی همچنین بابت اتهام «تبلیغ علیه نظام»، طبق ماده ۵۰۰ قانون مجازات اسلامی، به هفت ماه و ۱۶ روز حبس محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/78498" target="_blank">📅 18:25 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=eIQz-1SzfNXwRfv5cA4qqGEQfNKoEhi1LvYa6qbRHmDRSpgS5nJiZmTHdpDiwOEuDAE_1UDsgrryYeAUsJ1HSYcQ6clh1mSNvfnj10hH1GDxNRuXfuEtJ6gpeRohp9MZMNqMwlW7t3z5biVf-JzQuu4UomREfuhQ0sVCJH_hTh2KVKrkw8CM_wX5VpalB95CBGHjJGKFpW_ScF6XRCTIdHdpAnkSOMKrZO_UByvSS3SuQKXD7YDzDJAFf7UueLwZ1WU3xInS44nBZbk54WAa1CEMQn8KYmNy9dzSWIPChYW_SF0CEYn-AxwxgYkzKbOJjluprFgLiXYz0ZgBaIhltmEgNezH1TTYD511hNCihSFQ0DjzNJkLiSNbCSfIsXtMdw_3MT0uW1nbawuUdDhGl884QjDDrjDHwmFyr1zQOurz1JTzrxFMjwb0ocVbCUxx0VhRpZkcwZPRG7_ZeLVhuWCtIQUm-8wUG0FZYSnEG25uzy2Vsr9INV-4gqkp0URgybw1BWdc6zwWr_HCiUowK_8UQuadf96nXU_5DLTtXP4Mhw_PJGkSovqZXL4RpisbKxoRPthbgx_L6G51Fyycf57RimvOIGP1_xZ_tpYW9LolKcYOGdzTA5WX_WFW0-e3s_xVK7L4o9L6OeSp81Eyr176OX-n95wpMkmppVpfezA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d50a67123d.mp4?token=eIQz-1SzfNXwRfv5cA4qqGEQfNKoEhi1LvYa6qbRHmDRSpgS5nJiZmTHdpDiwOEuDAE_1UDsgrryYeAUsJ1HSYcQ6clh1mSNvfnj10hH1GDxNRuXfuEtJ6gpeRohp9MZMNqMwlW7t3z5biVf-JzQuu4UomREfuhQ0sVCJH_hTh2KVKrkw8CM_wX5VpalB95CBGHjJGKFpW_ScF6XRCTIdHdpAnkSOMKrZO_UByvSS3SuQKXD7YDzDJAFf7UueLwZ1WU3xInS44nBZbk54WAa1CEMQn8KYmNy9dzSWIPChYW_SF0CEYn-AxwxgYkzKbOJjluprFgLiXYz0ZgBaIhltmEgNezH1TTYD511hNCihSFQ0DjzNJkLiSNbCSfIsXtMdw_3MT0uW1nbawuUdDhGl884QjDDrjDHwmFyr1zQOurz1JTzrxFMjwb0ocVbCUxx0VhRpZkcwZPRG7_ZeLVhuWCtIQUm-8wUG0FZYSnEG25uzy2Vsr9INV-4gqkp0URgybw1BWdc6zwWr_HCiUowK_8UQuadf96nXU_5DLTtXP4Mhw_PJGkSovqZXL4RpisbKxoRPthbgx_L6G51Fyycf57RimvOIGP1_xZ_tpYW9LolKcYOGdzTA5WX_WFW0-e3s_xVK7L4o9L6OeSp81Eyr176OX-n95wpMkmppVpfezA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در جریان دیدار با رهبران و نمایندگان کشورهای عربی خلیج فارس، ترکیه،‌ اردن، سوریه، مصر و لبنان، ترجمه ماشین:
فقط می‌خواهم این را اعلام کنم که استیو و جرد امروز جلسه‌ای بسیار سازنده با میانجی‌های ایران داشتند؛ عمدتاً میانجی‌ها. ببینیم چه پیش می‌آید. آنها مدتی است که میانجی‌گری می‌کنند، اما فکر می‌کنم شتاب زیادی برای رسیدن به توافق وجود دارد. این چیزی است که از همه می‌شنویم.
و سخنرانی مرا هم شنیدید. لازم نیست دوباره مرورش کنم، اما ما ضربه سختی به آنها زدیم. قصد فخرفروشی نداریم، اما اقتصادشان واقعاً در وضعیت بسیار بدی است و امیدوارم کاری بکنند که واقعاً به نفع مردمشان باشد. و فکر می‌کنم واقعاً همین کار را خواهند کرد. واقعاً همین‌طور فکر می‌کنم. گزینه دیگر برای هیچ‌کس قابل قبول نیست.
جرد کوشنر... [بخش نامفهوم] اما استیو و جرد، دو نفر بسیار باهوش هستند و دارند کارشان را انجام می‌دهند و فکر می‌کنم این ماجرا را تمام خواهند کرد. هر دو طرف احترام زیادی برایشان قائل‌اند. ایرانی‌ها برای هر دوی آنها احترام زیادی قائل‌اند و فکر می‌کنم این مهم است. اما فکر می‌کنم کار را به سرانجام می‌رسانیم.
...
می‌دانید، زمانی خواهد رسید که دیگر خیلی دیر خواهد بود و ما دیگر شاید فرصت این را نداشته باشیم که بگذاریم به‌عنوان یک کشور باقی بمانند. من مایلم بقای آنها را ببینم. می‌توانم بگویم افراد دور این میز هم دوست دارند چنین چیزی را ببینند. بعضی‌ها از شنیدن این حرف تعجب می‌کنند، اما آنها چنین چیزی را می‌خواهند.
همان‌طور که می‌دانید، نیروی دریایی آمریکا مین‌های ایرانی را از مسیر کانال‌ها در تنگه هرمز پاک کرده است و اکنون در حال تسهیل ازسرگیری جریان نفت هستیم. اخیراً اعلام کردیم که بیش از یک میلیارد بشکه نفت را از خلیج اسکورت کرده‌ایم. حالا این برای تمیم رقم زیادی نیست، اما برای بیشتر مردم هست. یک میلیارد بشکه؛ این نفت زیادی است، درست است؟ از هر طرف حساب کنید همین است.
اما اخیراً اعلام کردیم که دوباره بیش از یک میلیارد بشکه نفت را فقط در همین مدت اخیر اسکورت کرده‌ایم و هر شب ۲۵ تا ۳۰ کشتی را خارج می‌کنیم؛ گاهی روزها هم، اما بخش زیادی در شب انجام می‌شود.
محاصره قوی‌ترین چیزی است که کسی تاکنون دیده است. اسمش را «دیوار فولادی» گذاشته‌ایم و نیروی دریایی ما شگفت‌انگیز است. ارتش ما شگفت‌انگیز است. واقعاً شگفت‌انگیز است. و حالا نفت بیشتری از تنگه عبور می‌کند، نسبت به هر زمان دیگری، با فاصله زیاد، از آغاز درگیری تاکنون.
و باز هم، بخش بزرگی از کاری که کرده‌ایم، شاید ۹۹ درصدش، برای اطمینان از این بوده که ایران سلاح هسته‌ای نداشته باشد. آن سایت‌ها منفجر شده‌اند. شاید مجبور شویم یک سایت دیگر را هم منفجر کنیم؛ کوه پیک‌اکس. فعلاً فعالیت زیادی آنجا نمی‌بینیم، اما اگر ببینیم، فوراً آن را منفجر خواهیم کرد.
در حالی که همه اینها خبرهای بسیار خوبی است، حملات تروریستی ایران به کشتیرانی تجاری و کشورهای همسایه نشان داده که لازم است زیرساخت انرژی خاورمیانه را از گلوگاه‌های تحت کنترل ایران دور کنیم. به همین دلیل دولت من قویاً از کریدور اقتصادی هند–خاورمیانه–اروپا حمایت می‌کند و همچنین از راه‌های دیگر برای انتقال نفت، چه از طریق خطوط لوله یا هر راه دیگری.
و با همکاری هم، در آستانه غلبه بر چالش‌هایی هستیم که دهه‌ها این منطقه را گرفتار کرده‌اند. این وضعیت دهه‌ها ادامه داشته است.
پس آنها ایران را به مدت ۵۱ سال «قلدر خاورمیانه» می‌نامیدند. من می‌گفتم ۴۷ سال، اما چهار سال است این را می‌گویم، پس عدد واقعی ۵۱ سال است. و واقعاً دیگر قلدر نیستند. می‌توانند مشکل ایجاد کنند، اما دیگر قلدر نیستند. ولی قلدر خاورمیانه بودند و همه بسیار نگران و به نوعی ترسان بودند. شاید هم حق داشتند، اما دیگر نمی‌ترسند.
بنابراین فکر می‌کنیم که وضعیت ایران ممکن است درست بعد از انتخابات میان‌دوره‌ای پایان یابد، شاید هم قبل از آن. نمی‌دانم. هیچ‌وقت نمی‌شود مطمئن بود.
اما آنها درک نمی‌کنند. چیزی که واقعاً درک نمی‌کنند این است که من انتخابات را با اختلاف بسیار زیاد بردم. هر هفت ایالت چرخشی را بردم. در رأی مردمی، با اختلاف میلیون‌ها رأی پیروز شدم. در شهرستان‌ها ۸۶ درصد بردم، چیزی که قبلاً هرگز اتفاق نیفتاده بود. این بالاترین میزان تا آن زمان بود؛ و در کالج انتخاباتی هم با اختلاف زیاد، اختلافی بسیار بزرگ.
و من نامزد نیستم. افراد دیگری نامزد هستند. جمهوری‌خواهان دیگری نامزد هستند. آنها آدم‌های فوق‌العاده‌ای هستند و من کمک می‌کنم انتخاب شوند. اما خودم نامزد نیستم.
و اصلاً به انتخابات فکر نمی‌کنم وقتی که به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم. فقط به پایان دادن به تهدید هسته‌ای ایران فکر می‌کنم و تمام. فقط به همین فکر می‌کنم. و هیچ ارتباطی با انتخابات ندارد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/78497" target="_blank">📅 00:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/luoDgiTfHYYqSypAVM_rf7bE-8Kfk4UwCzYLoSGV0ZX4LBksEd_D5wJ5EvnK_nGbaOK_2Zbc0WIO5myfsjgmzxSoYp6Qrvfp2ouFs6ykSOHgjeYlZ9ieSahg23_1typr1Dx-Ne8Lya2KXGmyJirIpFvpBGHLDBhKpqn_dASmpvom2moQSq-7ZsQ3yvxi5pLqUzrww-tOh7xaYi0bxPgSwQ2Hx20O9sP6IFwc9zRM_FSV9OOtTHkKvzt6M0sZ2upb016wVMQvdxtkw0cUkClsHOhJ_2z3B4PpBOcI5blGHUaSZ4pSos_ekpLXUhhL4Y7d72Uq7YpgciQJ1eB_d3O5Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیما: عراقچی و ویتکاف در حاشیه مجمع عمومی سازمان ملل دیدار کردند
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 385K · <a href="https://t.me/VahidOnline/78496" target="_blank">📅 23:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78495">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=kG70apHAnMoNlLog5vd4a39Iqtyqf00F7BLsmCdySETzu1aAsAPiOJtAXarxdYFHhKgXJ--v45UIPCL9_-p2MYC6a0hRqXMw09UVWdXVF9JTRb_By1qPaDDBqjvdGbqLIKMd2g5P-GrcH_4fKD3NF8hByiglH_YR8aLAA_JOhPXq5jpMF2B2K4u3hJgTJnNp1q53HDOxeV4S4rRbhCWdFm5djd_IVtu_RPYXPbB239hBvHY2EscfDWOjE0r1P9wHsRrnUTqFk8XXpiDn-jqX2Zn_-cSDzKBYbKx1soCH751-JVINsQh44mKRpXfhzoDAoIEvJEJI7G43_8MsMheSeA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/784b28c7d4.mp4?token=kG70apHAnMoNlLog5vd4a39Iqtyqf00F7BLsmCdySETzu1aAsAPiOJtAXarxdYFHhKgXJ--v45UIPCL9_-p2MYC6a0hRqXMw09UVWdXVF9JTRb_By1qPaDDBqjvdGbqLIKMd2g5P-GrcH_4fKD3NF8hByiglH_YR8aLAA_JOhPXq5jpMF2B2K4u3hJgTJnNp1q53HDOxeV4S4rRbhCWdFm5djd_IVtu_RPYXPbB239hBvHY2EscfDWOjE0r1P9wHsRrnUTqFk8XXpiDn-jqX2Zn_-cSDzKBYbKx1soCH751-JVINsQh44mKRpXfhzoDAoIEvJEJI7G43_8MsMheSeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
در دیدار با ایران، آیا آقای کوشنر و آقای ویتکاف شرکت داشتند؟ درست متوجه شده‌ام؟
ترامپ:
می‌خواستم همین را بگویم؛ آنها دیداری بسیار خوب و بسیار سازنده داشتند و دیدار دیگری هم برای آینده بسیار نزدیک برنامه‌ریزی شده است.
استیو، اگر می‌خواهی... جرد، اگر می‌خواهی چیزی بگویید؛
آنها دیدار بسیار سازنده‌ای داشتند.
حدود یک ساعت پیش.
خیلی خوب پیش رفت. یک ساعت پیش تمام شد. دیداری بود که سه ساعت طول کشید. یک ساعت پیش تمام شد.
دیدار بسیار خوبی بود. یعنی باید بگویم، خیلی خوب بود. اصلاً نمی‌توانم تصور کنم چرا آنها نخواهند به توافق برسند.
یا عظمت است؛ عظمت بالقوه... یا نابودی کامل. دو انتخاب وجود دارد. یعنی، در یک حالت نابودی کامل است و گزینه دیگر، عظمت بالقوه است.
ایران می‌تواند کشور بزرگی باشد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 372K · <a href="https://t.me/VahidOnline/78495" target="_blank">📅 22:17 · 31 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
