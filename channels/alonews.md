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
<img src="https://cdn4.telesco.pe/file/TKzzx13pQ25N9g9POIjlcvconfMgALIcTWtwV4OBNuhGcZZYkulVB1snPIMpNaqpDdVSl_cjziMJARugr5g2AQFUGhLIU1LR6pumS5yxuqqns5K91-3mW_B8VS1chc0HKpL2Rop9gLcqnJ8zsZxtcNeJF4LMnr2o0hJpYJsnt3gzLcHBpYzncTmLSQL5wb7VVPit-HvBRzEphRNonWtF8PcOy1GIQ6z31SVn2NzFnh2QKzv_gkQZJp7Ry2tzO-g08Ck0l_cUEHv55yoAh0ehS9KW0lGPUGPLpzkdtva02R1XZTCbj0-2wNQ0aa1v9C-0cFQFfu5CLY9Y8h2OfMHCsg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 945K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-131224">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دلار هم اکنون 175,500 تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/alonews/131224" target="_blank">📅 12:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131223">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فارس: ارزیابی‌های اولیه حاکی از آلودگی نفتی بیش از ۲۵۰ کیلومتر از سواحل هرمزگان در پی حمله آمریکا به ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/alonews/131223" target="_blank">📅 11:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131222">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:  خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟ پسر بچه: آره، جونم مهم تره خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد. پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.…</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/131222" target="_blank">📅 11:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131221">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=NNYpfd-Yg30mE7H0vCYBYc6ku10gyoB4b3MMfXTHTTa8lzZ4w--9m70RvYb_SgbnhLZDc33RpEz4zZ6slrFVeVYWvOmSZDOATkKx2T-tWJEvv26P2-PG9xVMjERPG-EfBlWzh6nyU4qcIj8WOlL0SsHDbL3Gxo28skDsb2MZPc9RKNMdh1OwXJosMWApDVagV_tY5pkXITM_OzIEvxqHB0DkGohWj-VFizkKdNYTmnPABDPI0BL8-oogP9KH2i6gzWu0u1WnqjBNeCjnR7W7l0ckpoLB2MvSNR4nx71-1AEpd6c23pVclNZWro0CpR-CjKXz4TmHT87umaUx-uv4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=NNYpfd-Yg30mE7H0vCYBYc6ku10gyoB4b3MMfXTHTTa8lzZ4w--9m70RvYb_SgbnhLZDc33RpEz4zZ6slrFVeVYWvOmSZDOATkKx2T-tWJEvv26P2-PG9xVMjERPG-EfBlWzh6nyU4qcIj8WOlL0SsHDbL3Gxo28skDsb2MZPc9RKNMdh1OwXJosMWApDVagV_tY5pkXITM_OzIEvxqHB0DkGohWj-VFizkKdNYTmnPABDPI0BL8-oogP9KH2i6gzWu0u1WnqjBNeCjnR7W7l0ckpoLB2MvSNR4nx71-1AEpd6c23pVclNZWro0CpR-CjKXz4TmHT87umaUx-uv4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصاحبه حق و جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
پسر بچه: آره، جونم مهم تره
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/alonews/131221" target="_blank">📅 11:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131220">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZkzIxhsxZ5FYyRFm30sMzEQARFqOdAJIrinONBHo7OgP2G2mr6K5hLR5ae4YYM6Qi6va7GAMewDF1hQ18LTTscwvvDu6UsRpNY52PCb5t56XMSDfUOcPvi3ybSL0Ias-CGpox8WE77B21-X0F5ZH-RuMU_VZhA1C5Djw66vvmrAeVODRhgZWSB0O5czn5UxcTAJTMUMP2j5y0SohYWvH0ywY_jMFz_L22c5xHz7snPLAi4WVQe6kXTtzHmVecCjrSYKMiVjf-_B9JC5ju3R9Zdo5CltjSHsXAcBLF7IQRHktOylqxo89R9ImGAWzXmjbrjSTTqEq5ReQ591PmY_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: اگر مشاوران به پزشکیان اطلاع می‌دادند که ترامپ ادعای دروغ صفر شدن صادرات نفت ایران را مطرح کرده، رئیس‌جمهور نمی‌گفت «۴۰، ۵۰ روز است نتوانستیم یک بشکه نفت صادر کنیم» و ترامپ این سخن را به نشانه پیروزی خود توئیت نمی‌کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131220" target="_blank">📅 11:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131219">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
رسانه اسرائیلی ای ۲۴ نیوز: سیا و موساد اسرائیل نقشه‌ای محرمانه، مشترک و پیچیده برای سرنگونی دولت ایران در طول جنگ آمریکا و ایران اوایل امسال داشتند.
🔴
بخشی از این نقشه نیازمند نفوذ مسلحانه جدایی‌طلبان کرد به مرز غربی ایران بود.
🔴
معاون ترامپ، جی‌دی ونس، از این نقشه‌های محرمانه مطلع شد و بلافاصله به اردوغان ترکیه اطلاع داد، زیرا می‌دانست اردوغان سیاست‌های توسعه‌طلبانه کردها را رد خواهد کرد.
🔴
این نقشه در نهایت پس از افشای جزئیات آن توسط ونس شکست خورد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/131219" target="_blank">📅 11:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131218">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کوبا: مذاکرات با آمریکا متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/131218" target="_blank">📅 11:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131217">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
نتانیاهو:من می‌خواهم کمک‌های آمریکا را متوقف کنم. این مثل کمک‌های رفاهی است؛ من آن را نمی‌خواهم
🔴
اقتصاد ما دیگر یک اقتصاد کوچک نیست... ما می‌توانیم همین بخش کوچک از درصد تولید ناخالص داخلی‌مان که از ایالات متحده دریافت می‌کنیم را خودمان تأمین مالی کنیم.
🔴
می‌خواهم این روند امسال شروع شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131217" target="_blank">📅 11:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131216">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
خبرنگار الجزیره : تهران خواستار آزادی ۱۲ میلیارد دلار است؛ البته نه برای خرید کالای آمریکایی
🔴
عمر حواش، خبرنگار الجزیره در تهران، گزارش داد که اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، تأیید کرد که دستور کار هیئت ایرانی به ریاست کاظم غریب‌آبادی، معاون وزیر امور خارجه، محدود به مذاکرات «ایرانی-قطری» برای تسویه دارایی‌های مسدود شده است و وجود هرگونه کانال مذاکره مستقیم با هیئت آمریکایی را تکذیب کرد.
🔴
تهران خواستار آزادسازی فوری ۱۲ میلیارد دلار در دو مرحله ظرف مهلت ۶۰ روزه است که با ۶ میلیارد دلار سپرده‌گذاری شده در بانک‌های قطر آغاز می‌شود.
🔴
در پشت صحنه، یک اختلاف نظر شدید آشکار شد، زیرا تهران شرایط واشنگتن برای ایجاد یک خط اعتباری انحصاری برای خرید کالاهای کشاورزی آمریکایی (مانند گندم، سویا و ذرت) را رد می‌کند، در حالی که به حق مطلق بانک مرکزی ایران برای تعیین نیازهای خود به کالاها و داروها بدون دخالت خارجی پایبند است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/131216" target="_blank">📅 11:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131215">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtx8ttmiKF7QqpNcl-qibJKEPdlcg-KNWw4LT2HS_Xixiu0jJvvPADZSEGOogNaHP2fwCwX0n-XsXiNU6-neor_nJU1_KwQw0NI7G63doa4UBBL6UM_nzOatRiYyZIxzWP7PF9MrgqyHCzg-hbZnhnHvDu0uAS0_af6300tqg27DMxN4vPtHFgaT6UzvNj60tqzQ7xVJ2hl7NuaQD5vjJSQiF6_hSkgFG_utJi_xjSe5C1MrnR_vaAZnb2wH2xlQ4M3iAJsmZpeUOpnt9fZNCaNwuK1nJc1TR482YShXSjsqip9_r39z8e7NhB5mUZwxq03A9InB9Vfb79yCTlK95w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش جدید وارزون از نقاط استقرار ناو های هواپیمابر آمریکا
🔴
از مجموع 10 ناو هواپیمابر آمریکا ۳ ناو در حال حال تعمیر ، ۲ ناو در حال تمرین ، ۳ ناو مستقر در آمریکا ، ۱ ناو مستقر در دریای چین جنوبی و ۳ ناو نیز در منطقه خاورمیانه قرار دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/131215" target="_blank">📅 11:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131214">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLy1WZzNePsEBK_TGgQvL7bgpRe9wzIYk8Q6LCs_hcI0SKLTt4WCMfHaljcKJ0MLE5kjvr282sq-nmv2LMe-PWXM4iO7RF7kzpqtRlg_QIz3cQuokZpx57s-gBSDOGImPySQt0SnzH4JHMCrxJr4SZypsRYFg6f4Z8xjb3C7xeazBgVnQjJg1Pt1tXdggGHiC2pNhcdXwoKHnM41M0s8BoNdxdvfSChNYz9YXv9ozDLwf-HMMHhlaD-1mNC7V0pZfJgNrBqPBX5fVzzp0KitPYohJFSQj57FFwc403x1uuCzXYofcFx7ViaMaB79O0ftpXYQZSNjvbiPIdmEBFimIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی عضو تیم مذاکره کننده: ایران به سرعت درحال بازسازی زیر ساخت‌های غیر نظامی خود است.
🔴
ذخیره سازی اقلام حیاتی را انجام می‌دهد.
🔴
سیستم های تسلیحاتی جدید را پیش می‌برد.
🔴
هزاران فریب دهنده «ماکت» نابود شده را جایگزین می‌کند.
🔴
فناوری های نوظهور را مستقر می‌سازد‌.
🔴
شبکه پایگاه های زیرزمینی و مراکز فرماندهی و کنترل خود را گسترش می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131214" target="_blank">📅 11:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131213">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سی‌ان‌ان: با تعلیق موقت عملیات سازمان ملل در تنگه هرمز، تا کنون حدود ۲۵۰۰ دریانورد از تنگه تخلیه شدند و بیش از ۸۵۰۰ نفر همچنان در تنگه سرگردان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/131213" target="_blank">📅 11:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131212">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
آمریکا قصد اعزام نیروی زمینی به لبنان دارد
🔴
بر اساس گزارش واشنگتن‌‌پست وزارت جنگ آمریکا (پنتاگون) در حال آماده شدن برای اعزام نیروهای زمینی ایالات متحده به لبنان است.
🔴
این اقدام با هدف اجرای توافق‌نامه اخیر و جنجالی با میانجیگری آمریکا میان لبنان و اسرائیل صورت می‌گیرد که خواهان خلع سلاح حزب‌الله است.
🔴
روزنامه واشنگتن‌پست به نقل از مقامات آمریکایی گزارش داد که نیروهای آمریکایی برای نظارت بر پایبندی لبنان و اسرائیل به این توافق‌نامه، در خاک لبنان مستقر خواهند شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/131212" target="_blank">📅 11:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131211">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/816b9c6962.mp4?token=q9k8Yi_Z3ZjYtVgJeBlXsovHClE-R8BMx1_Jj-XEMl_oIr-YLBDFITlflUUIzvPpSKn6vSWFWNeSKy8pGPodWgSCzL6Q-9j8cDc7ulEKRN9VYZlNxsi-lZVCdUIceoBLguy3Tf-BHVNKt7Y8N0QLwQ79XGdU5eLcI93tnwqMXXCnYPP6f3Pk-G4BVCNqLcY6Fu-oWIJhsCErsEDZFDBf0cn0V-bzjywmAjGiFHp-HDkwwmOvEmBPHb5eZx4sQSUrA_To_1LK3B1M7sOVGn4pM8igFFN1Fj-17aRggEFjrnjsMcdl_PFdV_SJ21N2-v0p43MzrY_ZD772HUclPohgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/816b9c6962.mp4?token=q9k8Yi_Z3ZjYtVgJeBlXsovHClE-R8BMx1_Jj-XEMl_oIr-YLBDFITlflUUIzvPpSKn6vSWFWNeSKy8pGPodWgSCzL6Q-9j8cDc7ulEKRN9VYZlNxsi-lZVCdUIceoBLguy3Tf-BHVNKt7Y8N0QLwQ79XGdU5eLcI93tnwqMXXCnYPP6f3Pk-G4BVCNqLcY6Fu-oWIJhsCErsEDZFDBf0cn0V-bzjywmAjGiFHp-HDkwwmOvEmBPHb5eZx4sQSUrA_To_1LK3B1M7sOVGn4pM8igFFN1Fj-17aRggEFjrnjsMcdl_PFdV_SJ21N2-v0p43MzrY_ZD772HUclPohgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تریلی هانری :)
@AloSport</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/alonews/131211" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131210">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🚨
قرعه کشی پرمیوم رایگان  دیگه همتون از پرمیوم تلگرام خبر دارید که باهاش میتونید تیک ابی و استوری و ایموجی پرمیوم رو باز کنید.  فقط کافیه توی چنل های زیر جوین باشید
🔗
@CRYPTOSMART_ORG
🔗
@Proxy1y
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/131210" target="_blank">📅 11:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131209">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUGucUj3nwZ1EUG0XqSJ6md1oUAdTOA3ELV3xlqpMtX7b5vl9eswdFZR9XrjiD7hHxdOQaLb8aCHLjCUEQ9Q_u1lfcqSPMY9MBBSBOTpSZFllkwLKF2Ai_JtPArU8aSKid1_krikHxNPscVgHqvHLn0vXV9Jj80DNmz71OJQVTxvCV2LWJuivgZCiROkRhILvmVbCrlKpMe5Pot0kT7nQhjsYU87MXFCxGRA-JKWKIM33H-Li8SQ7dckOVH8WN-PN8XMHF_rarLrENS_HCW0Y9nS7KEC8DVK7tarVb2q3BlmaGz5RkOH53J6bJwKxvHRHLDcN8SA_IJ309RuSwQHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش فرانسه: ناو هواپیمابر شارل دوگل در خلیج عدن در نزدیکی تنگه هرمز مستقر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/131209" target="_blank">📅 10:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131208">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سازمان جهانی دریانوردی: دریافت عوارض اجباری از کشتی‌های عبوری از تنگه هرمز مغایر قوانین بین‌المللی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131208" target="_blank">📅 10:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131207">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
فرودگاه مهرآباد از ۵ صبح روز جمعه تعطیل می‌شود/ توقف کامل پروازهای تهران در روز دوشنبه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/131207" target="_blank">📅 10:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131206">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
وزیر خارجه چین: شتاب مذاکرات آمریکا و ایران حفظ شود
🔴
باید توافقی جامع حاصل شود که مورد پذیرش کشور‌های منطقه نیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/131206" target="_blank">📅 10:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131205">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پاکستان: دیشب طالبان بهمون حمله پهپادی کرد ولی همه رو رهگیری کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/131205" target="_blank">📅 10:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131200">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMWIXM_flBO7_wEbWEqTuFqB5Tqg7E7HgvDYtGvi9_lJNWG3oTNNdsWG6om0HNPLL7OrfcrHKDI75MQ_Kd9r4WV6Tr_QHKkqUJQkwVm4t1xC2SgAzHBLbJomnokE5m-ygNmLRnbe9iKQHMBifmsqch06IIKHKOh07b1COx7Ysgqj4YaWvReXbkVkbfuHSIB7nuXeGEx1oRz2Ljg2kOA11klEOFN5lDJI_FCuvMSAofCwKMHvgve_6v65GU77KdSsJXcAwJC-nq_7MUg7U9_GGd42QUe0I4VjrJ2bYH_L5h1jI40HRywNS5-4XSZDDEiAcH4d9GJKDd6byVHBuZ81zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m3K2Fi5IpjpNdOn_GmP_Ut_h09mgaud9A3bIXCbh7w_Y1a5tEXhKd7R2MIjqcOF0gZLfXHDwtWNL1lchRGAEyvUa1puZkgrR0EUlw08Z0wIwIVOzVNlapKTzAzH-6rQLMzg4I6VC4jfWNHGneFs23bIX9gaunEMXx1rEfLoL4WEOGg4CRMlFE3XIStd4D1bD-A4hzAkAmzLddxumfhln7mmcSGBkPOknp_YXrH6gllwL9083Qoq5Emleffuci3a3HhSS_KF5535nlyOQYMv1p4zvzh0TlkVWhZVPTS5XGoqwdD59qOcCJcxJljLiYdGCX8UQZatQuoM_JYy15ffULQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbp01Kv8P-YQX7JT9QyEmHZ3qnTjEQWPbT_ziOgdao9p1n8ldY5lQgrKSh4cjEs5VVWsRZdFbYp5yQdFgUq8u-gySLb45Y9RB7AbyP5gjwFnH6pxfZsUJoPEdwwPchOvJ15tC9_Hlhehgu1uydttomDhBY64GTr7dHgNaFLxI45mSSm_JBJlYcjup98L4gj1mdRR0BOu7Yzx-NVYizUjYlxN1y_4J4H6bgJ6B090L6x7yHNXRbBYZfGrOjSIrcIVzxeOiFaI9QLT42a2SWblwLpPbzPZn9QHPkYExdPARIwfqJtzf6gG2OZ6Tgk5e11Ywuj1UHxT_091RJu0MH6mMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MW6zz7NTLmAJXG7dml_X5ZS-HDU0PmHPpWSfeo7-I0PHGlo6A0gAqD4PnjMynOervJSnxIUHHSKWp6yIX7mnan1W1_d4q9D5Mukh7nSW_XC0pKbBDqSziztcx85kWbf-vlqqjm-7cn6H7toQcxRfqYnFryuMdqeCL3je9a5InsBVYOM7-e4M8tDvjMghSON2inCYOQqse0c4XUTqv00xWQmhNhum5nIEfHgU7OrLHQ2DpsZlDCQh5MhAelDvFDurJwD5nlxcZi0jHCskuUwPtseGxePU0KzVTi6pSM0CBx04pba0_JjWLOYmkmkvWE_Y-sZXDOh4toAzDPPZha3EIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2FDerybTrSqGdZR_ttTB833imwxQFm_nU4hUZJDd5DmrdqSp7gD4FvHzgClFHZ6yhVh5WNtCtZwKfUieo-Ai0aknnBBMZuR9_kqq2eeqyZzDbsdCzUc47W-kw73boQIHZbqOfPxH7Fp2yvpfv5phzoqFja8C0bgs4mVKnCgjr91eW0T_-fcScmCiWMmf9XMmQOb8hxALVb7nN3xTTfm27RDqqg6J-_-gI5qpM8ZEx47g8MzcQyrQrtt_6dNNMqFBvV13yocMEe0PTZIjxLDtwXZycTDtIcSk4wyCHUBMAdwYgbiLWZaRgKPIhUtnGtblRZAy6rDxsO0HCRrVBx2SA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به جنوب لبنان همچنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131200" target="_blank">📅 10:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131199">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd7mk-G2KV-316EhLCokWWdXAIsCx2b-k0ZFx1W8plXJ8BQtaakKdjT4zdpEe2vYV-GQlOdV0Qg0nC2IRcBz6ehNEYMsYB-Ws0njQTIM2TRKWNA2AgcTuAZuePLotNbADWjc8D6an7AT5iZ_SvalbfaPz4sLFx6qUD_NUu8yq2i32jfdaiD4mgFbFYvCXwriswrEhzee69nsbSTaw2bmBAlREEG12hJ7wF5gzdqvkNggx7iE5iJAfoao3wqtzmh0QHqnIY_pgOrDlceNHTPiBlUst-pY4IpSvpxX0yOyVINmKA4iEIf07OclA2ZyMHLAsZtFzjZNTEdyzGvLrcGEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ناوهای یو‌اس باکسر و یو‌اس پورتلند به خاورمیانه رسیدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/alonews/131199" target="_blank">📅 10:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131198">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار کنترل شده در بندرعباس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131198" target="_blank">📅 10:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131197">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سخنگوی دولت: سه‌شنبه ۱۶ تیر تهران تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/131197" target="_blank">📅 10:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131196">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
بی‌بی‌سی: ترامپ در سال گذشته بیش از یک میلیارد دلار از فعالیت‌های تجاری، به‌ویژه در حوزه رمزارزها، درآمد کسب کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/131196" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131195">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
خبرگزاری بلومبرگ در تازه‌ترین ادعای خود به نقل از یک مقام آمریکایی گزارش داد که استیو ویتکاف فرستاده ویژه رئیس‌جمهور آمریکا، و جرد کوشنر داماد دونالد ترامپ رئیس جمهور آمریکا و فرستادگان این کشور در روند مذاکرات با ایران، گفت‌وگوهای مثبتی با سران منطقه‌ای در دوحه داشته‌اند.
🔴
این منبع افزود که تماس‌های فنی بین آمریکا و ایران در چارچوب تلاش‌ها برای دستیابی به تفاهماتی درباره توقف درگیری‌ها همچنان ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131195" target="_blank">📅 09:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131194">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2068fce62f.mp4?token=a9Bljp48g4wg7k80OF-sMCBSm0u8WFdbmAV6d-Z24Dp2yRSV_5YDiFo6wszEPvHSnXHvRvJJI4zExPaV7WmHbIFXofhyfj4SJk__meuMBLJRrPqjuMsF2HrHcUb_Njt16ZhOWR5TK_4KMG69KWy59GEwkgJC1_nHIYznrhmrayFJCgqLSeXaE4bhABgi8lZ-QRr3U4KD-h3hQAzX9OEGtAzu76YisoQBJG1PKPKVvKRuOQnX8HZkx6agTfq0WIZMW6lbwMW5jPr1nx9s5mVfzKn3dNJnBuqOINEp6e7DtUNMI9lryC-KPjFaI1j3OoHrjWmlC2RMMRh0NLSQk-Mwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2068fce62f.mp4?token=a9Bljp48g4wg7k80OF-sMCBSm0u8WFdbmAV6d-Z24Dp2yRSV_5YDiFo6wszEPvHSnXHvRvJJI4zExPaV7WmHbIFXofhyfj4SJk__meuMBLJRrPqjuMsF2HrHcUb_Njt16ZhOWR5TK_4KMG69KWy59GEwkgJC1_nHIYznrhmrayFJCgqLSeXaE4bhABgi8lZ-QRr3U4KD-h3hQAzX9OEGtAzu76YisoQBJG1PKPKVvKRuOQnX8HZkx6agTfq0WIZMW6lbwMW5jPr1nx9s5mVfzKn3dNJnBuqOINEp6e7DtUNMI9lryC-KPjFaI1j3OoHrjWmlC2RMMRh0NLSQk-Mwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گرمای بی‌سابقه در آلمان؛ خیابان‌های برلین را با آب خنک می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/131194" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131193">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92e2ffb510.mp4?token=JdQQZuOPiSxbvio19BMHjc96mDEfqggKFvZnHZqYhsy0s7M7Xl_I_fW5E1JuJMjspSUyOgHPlFneCWpmax_DZ8C7px2lxupfY_Yg6NVFOLhSz6upqr6PhBTQIHL7JuaxOLLlolnftLVShvYFf4axwh1jItYens7ulXmqBTjeUKzfF4lGdFSXibVS6GKT2nQKdWKg4gGqHRYEl7v_BuplOutEO2kI1f-6-ZqWnWvukJnafT2u_Ls7_8UvJF4y9A44MWIqYHGo0EQ5_iWh2uIzFSNjtv2nBYjZUHwX5qGPz8FZmRZ9k6Wm31ic1CqivFMU2Ra_esMhx-mVbVhmycjgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92e2ffb510.mp4?token=JdQQZuOPiSxbvio19BMHjc96mDEfqggKFvZnHZqYhsy0s7M7Xl_I_fW5E1JuJMjspSUyOgHPlFneCWpmax_DZ8C7px2lxupfY_Yg6NVFOLhSz6upqr6PhBTQIHL7JuaxOLLlolnftLVShvYFf4axwh1jItYens7ulXmqBTjeUKzfF4lGdFSXibVS6GKT2nQKdWKg4gGqHRYEl7v_BuplOutEO2kI1f-6-ZqWnWvukJnafT2u_Ls7_8UvJF4y9A44MWIqYHGo0EQ5_iWh2uIzFSNjtv2nBYjZUHwX5qGPz8FZmRZ9k6Wm31ic1CqivFMU2Ra_esMhx-mVbVhmycjgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد.
🔴
بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131193" target="_blank">📅 09:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131192">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
الحدث: به گفته مقامات آگاه آمریکایی، دونالد ترامپ در حال بررسی بازگشت به رویارویی نظامی با ایران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/131192" target="_blank">📅 09:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131191">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
میزان خسارات وارده به زیرساخت های آموزشی در جنگ اخیر حدود ۳.۷ همت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131191" target="_blank">📅 09:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131189">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pII8155ElozOgdERPw8d2jXuSP_--RpDTb5PqwC_JdkZ1Ptn6SQIjl09apxsbMoDaRqCgvy7fFtuL7cc8N6rDFfBKRwSnIHKX7LdlnJyouw64FwLpAuryd1cATaoB7W5Z1Mjwafw4zB7IlhnZYuKwFtpM8m7NN8xtCRqHFUbl0IekK9_zAEmFDFu9Z7LrhKOxMqiwZMGSwLPwRiM_bdpz02CzIFJL4B-uB4JfOK-ozsL2vrfJXXEikjjGkzzgO7c70WX67kmpsuDbd5DhytG-h_H_4LIW6X0Ir3WJQ2T4EToHoYZYUBC2R97Tdos6unWGIn7p-cK4uG5REQvNP5-Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/P_BAZV3elYkEU-kFdWM52uLg9_jChClK87CbdxT__BPHPRY5XNRR6NPPuVmywh_g-MeaL3m-XwUySKbR2KZKr8fMBYXZaP2XYxcCtWRLC4xGy4RE_BFH-99qjRH4LWeBDyZqvGqxJb3facwsfGGnVPGG5hrS2kQYL91BTyHD0oqPLUfShCceglBC6F6-uLuvGVXEkD1FjvhKgvrIzF9ZaRkXJts5ZObbgNB4PJAuOvE3LqMIwL-DfE90AfJ5UEzFhxpc3vKKVzwIGFjxy40AXxbK9GYBJPAQZwrUdkXbmHvZBGLbASU0K5_7_zJ4rD7JK8Gyd6hMXIi_nmBWuSXDGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
اوایل دیروز، پدافند هوایی S-300/400 روسیه تلاش کرد تا پرتابه‌های ناشناس اوکراینی را بر فراز مسکو در ارتفاع بالا رهگیری کند.
🔴
با توجه به هشدار موشکی صادر شده برای منطقه و ارتفاع بالایی که رهگیری‌ها در آن انجام شده است، این احتمال وجود دارد که اوکراین برای اولین بار از موشک بالستیک آزمایشی FP-9 خود استفاده کرده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131189" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131188">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz1gvltLY18s3VuR_OMNd4zV3lbcsIjMhj0lu1T6zrx2tfyF_-qbKQCiwqoJ-PNLvX9J12scYM3bqDMxI2TfV0gNmPr06iMKvpssDJaOWvUY1AucBC_LbmjWETb8_bYvARdE90h2Jl9XIVFZXjqV32lXrgdqhsVQWpAmpdHif6CmqnZ-AqvvazequjtJu296U44uyLRPx22evVaC-wEENXYlgh2QOTx4we7reh5iF3_Zte7l0WcoI2qZwD7F85JD8b_Y3U95wHf6SVBePzti3tkbbmB2Pt9nRm1Md0aOCcL0TcfVDCxGw4mk3bJlzI4VxAc3IuOp4-k3ZRhEmorU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گفته WSJ، رئیس جمهور ترامپ اخیراً در مورد احتمال از سرگیری حملات نظامی در مقیاس بزرگ به ایران با پیت هگزت وزیر دفاع و ژنرال دن کین رئیس ستاد مشترک گفتگو کرده است، اما به گفته WSJ فعلاً ادامه مذاکرات دیپلماتیک را انتخاب کرده است.
🔴
ترامپ معتقد است که بازگشت به حملات تمام عیار می تواند مذاکرات را تضعیف کند و شانس دستیابی به توافق برای برچیدن برنامه هسته ای ایران را کاهش دهد.
🔴
او همچنین مایل است اجازه دهد مذاکرات فراتر از ضرب الاجل 18 اوت ادامه یابد و در حال حاضر از حملات تلافی جویانه محدود در صورتی که ایران یادداشت تفاهم فعلی را نقض کند، حمایت می کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131188" target="_blank">📅 08:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131187">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eky42jKYDcb_Cjv5paQHlY-7r9mydVk00eEQtCurwwOCteDGkyyabJVVYPAZGKkpsGWYGn-xtqC38mB5RSG9DtqCzi4DnmU0KniyRsl4EeUYy54Nqvi3ZTIxv8gtOjRvmRICPABfmKrYfNH8FtTmq6AM-gOBqdpiUvmbW3fEsRa3wDObE9vMH4Eu8euL2JYSk7kZjnqaLynmHL6trFSygJLqRLqjoN_t-n-BV9Nw29xP-Id8U8vvpCWnbuQ2rsVuq0OnoCe9-r4IGtesGGNJ3ZiGXjuhcM8GgArRwrdVuL7WltVT-QUyQ9o3tSaIgorVxKNiIFOJ3t8HmPfaV9EqjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش وال‌استریت ژورنال، عربستان ابتدا دسترسی نظامی آمریکا به پایگاه‌ها و حریم هوایی خود را برای عملیات امنیت تنگه هرمز محدود کرد که با تهدید واشنگتن به تعلیق تحویل سامانه‌های دفاع هوایی همراه شد.
🔴
هرچند ریاض بعداً موضع خود را تعدیل کرد، اما این اختلافات و تنش‌های دیپلماتیک اخیر باعث شده آمریکا به کاهش حضور نظامی خود در عربستان فکر کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/131187" target="_blank">📅 08:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131186">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ورود ناوهای آبی‌خاکی آمریکا به منطقه مسئولیت سنتکام؛ استقرار گروه آماده تفنگداران دریایی در خاورمیانه!
🔴
در ادامه تقویت آرایش نظامی آمریکا در منطقه، فرماندهی مرکزی ایالات متحده اعلام کرده است ناوهای یواس‌اس باکسر و یواس‌اس پورتلند اکنون در منطقه مسئولیت این فرماندهی فعالیت می‌کنند
🔴
همزمان، یازدهمین واحد اعزامی تفنگداران دریایی آمریکا که بر عرشه ناو باکسر مستقر است، به‌عنوان بخشی از گروه آماده آبی‌خاکی، همراه با ناو یواس‌اس کامستاک در این منطقه عملیاتی حضور دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131186" target="_blank">📅 08:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
آخرین وضعیت کیفیت هوای تهران
🔴
شاخص فعلی:۱۲۷
🔴
وضعیت: ناسالم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/alonews/131185" target="_blank">📅 08:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
افغانستان مدعی حمله پهپادی به پایگاه‌های داعش در خاک پاکستان شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/alonews/131184" target="_blank">📅 08:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLPAfOR4xi0Zn1xnSP5W0FsUll6_4D0L1ufQvktpNt5FeJSxCAffbhcMFroSilm22G9NhG7Q99kcYU0rsQGL8JZ3UY2xUARm067i6nDfd9Hq4S--hOWwmFkDh19VW-ZMeu5Ld22Vf-YY-74nlidVL_4736grwJkyH06GKplDSHBQSskHZX2iZnvJW5wAiRHhxubw0BLwma2UKfimRkNM172LQNPoHbI3E5U3Mz_iamXgCOmKrlMHuXVbQuM6BE20A2ml_BJ-u7TKie3Fw-j4JpvmIaj2d3_l-Vp1E0OJJbBXTn72jiJGb5GMhQ5TYJu6x1UQuypvPQgAMfb9Zo-xAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این شخص غلامرضا قاسمیان است کسی که یه مکانی درست کرده به نام پناهگاه زنان خیابانی که اونجا زنان رو جمع میکنه تا خدمات جنسی بدن! و اسمشم گذاشته شلتر
🔴
قاسمیان در این ویدیو میگه خودمم اینجا میرم و میام
🔴
صدا و سیما هم یه هفته هست اینو هی میاره تو آنتن زنده…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/131183" target="_blank">📅 07:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSbacn3FtvFHDuidAaL3iXoyHB-WkM5Now0kME8clPRnAwbGppK2m28hiQmdHxPTyBpf_1iFt4CZpYFQhKOkrmjdszMls8zvn4j6kbevDHQNPADQdQO6UP8R7zFqwaEB9dusEkVeJXrzufsHVkJ6uMgdycuqMLHLw8vHMYFLD4ae4_81WVocdXMa7ndkR1QqIAKocLwpKK0d3dYw4T7HwS7WWYUNVprTl7Hbpgy-RsJHtUUJz5kh4JL029_5J8wcmfhGTpFfx7s9CBxMHNd1u6xWyhTBYMuu2SzkQqWQXrymS7j4Mr5uI6keFmAgRfIOfEuGJJjdHy0U6R9YchkvUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده رهبر در سپاه:
آقا مجتبی رو خدا انتخاب کرده و ایشون یه پاداش الهی به مردم بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/131182" target="_blank">📅 07:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/131181" target="_blank">📅 01:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکریپتو اسمارت | Crypto Smart</strong></div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131180" target="_blank">📅 01:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131179">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skJOU6Rc8EXQmQv_TdEfyflzjzIl5v7sBjSneMdDv_UCdxfxCQd4S_8eVCAdJKMnHpnsZdIiwL5zOzSix_emb6CcbZ_XmkN5cogafCYCZ7p0AwSBWFgBX16bz58GdZ5jJAjPC25tEvP9fbbtlB2FBEqvUZ1QKAuCEwXY8m2s5_0zc_CF957YY443L4aFgSokNIya060YAIXQUN39zQKJyYANrvNLof9Rcnt-NKgYm48sYdlWqGveB3ccSQ26kt957bMIuaRS8a2b3jMIBY-8ttq_xwZYtrlA79ruxlDo6fzjlToc4Gq-s3_D8JgOQwAHDaa_2Oq_cPYMsMidMupfkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حماسه سرایی پیج تیم ملی از ریدمان قلعه نویی
تنها سرمربی بدون شکست ایران در ادوار جام جهانی، مرد خودتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/131179" target="_blank">📅 01:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131178">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfEm8lOE09nvbMPDYHSGYu1iUAhOXVJXh7DRw0YB9UYaiq34F4A8YaPwbS8V4GkaXy45czLOjVljKSPzOj1kl5yBXKsrLOMPOjhweDeFJ0MJUijjoWOFdxVKgUR9u1wy7ANjHz0CaHb67Zwf_OGoBDjPNXILB7VnxVgdIj97CSeUCS0Ay0D86FF6HB5_Wy3afaPidDg5BD8fUK95IgJRcFENF9ChRO8tyR8lSCMr6Oja92oCmdelprdnklQX2Jx8Yu2qeB1M-dUknm5hymz0QmiBACDV4aZpxCy1E65LiWK45bAwAb6p5nbySqpzij93P-1zpm5Mknz6DSLGPTAbVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون ترامپ:
ترامپ از وقوع جنگ جهانی سوم جلوگیری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/131178" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131177">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_OADxOZeg47RvVcMlLvdJntaD4NKo_u0EgQjlOVHvsO4ODFEr1esNNIg2_Zc8HnJHR8GnN_NfTAOwCD9uY87zTulSWCfN7mqcHDdl929rhdvp8Cs8smTT6D2Uhrq-9dSCt5KMR1VHK_GovNZu6xIcxJ5bJaZqrWShNRTKGIKKVjvhGiUvJ3vo9k2j5wyBTYzn9nOZ6qlc7FWysgDsdFC3-zoQSaJfFix826JrE4379hGT_zm9JRQTw9XzBQidp0v5xnLEwmgjDjwwznUv3D9pKy6FqqYIMBQBFMw2fv4pDzZ1_8e3kUHlpBtjF3GhFPI7dfIei43M0I96lvb4ca0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طوفان توئیتری طرفداران قالیباف علیه جریان خوارج، از دقایقی قبل هشتگ
#اخراج_جبلی
در توئیتر ترند شده تا این شخص منفور از ریاست صدا و سیما برکنار شود
🔴
سالهاست صدا و سیما در انحصار یک جریان طالبانی است و تقریبا مخاطب قشر خاکستری را از دست داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131177" target="_blank">📅 00:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131176">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnlH666UkMW3f-GTKawSPtzKi2AQNuznZ_XSjE_VGW7l91v5iPQvTPqF3rr3iEfQp8Qwjteb3TM423-jM-ThG765_ln1xxUi6JH4J-bnjobxigGojVvA-AIGieyGt8Dh5WGUh7CGuXUTGX9vYAw5PydC-zvEy9Eu94gGbCx83gvfL4MdrT7R93e6tix0oQoxGkSRyOeo9FgauDPl1FadVUlFajeAu7g2g8aUBUiOGRsPrNUp9afRjq35rwxAAPbf-yEjOVitpulH2ciWmliGLs1ZoTJsGmDqRrOaM1UgdbnBvOhL3slGnk5cqk0a7utecYVZe934L8ejaDVH09tTvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جبهه پایداری:قالیباف مجلس رو باز کن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/131176" target="_blank">📅 00:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131175">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=c_Z7owsqCkPIyKtrnPWkqSoc5cdhtYWksfmDLG_gnFz3DMu23JExdwo4TKfpkZImGrAfXvnFJFDyqp33igv3KQYsNAwIqdm0rRoPkRpYV5cQIFI2YlvuCWtMsvsb5q7PZSH35W1iWfmvh1LZS4nB0LuCmX8KCQHxkzSemHwN6cnoJgOGhkYoj0p8Zgih_lCuQBsOdYXd0__NogKDJgybdAs7BqDG4WNZTa4eNDECkK7k8OP9Y_ohvNe1ixfFZmq3r-yaP56KPDYbhka7J6-30d95d8XIl524VQkmq8sLhbjo7qnLxEpxXpjGGkXavPw4TUGVbENxb82qyfo3sS-XRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e95ddaa0dc.mp4?token=c_Z7owsqCkPIyKtrnPWkqSoc5cdhtYWksfmDLG_gnFz3DMu23JExdwo4TKfpkZImGrAfXvnFJFDyqp33igv3KQYsNAwIqdm0rRoPkRpYV5cQIFI2YlvuCWtMsvsb5q7PZSH35W1iWfmvh1LZS4nB0LuCmX8KCQHxkzSemHwN6cnoJgOGhkYoj0p8Zgih_lCuQBsOdYXd0__NogKDJgybdAs7BqDG4WNZTa4eNDECkK7k8OP9Y_ohvNe1ixfFZmq3r-yaP56KPDYbhka7J6-30d95d8XIl524VQkmq8sLhbjo7qnLxEpxXpjGGkXavPw4TUGVbENxb82qyfo3sS-XRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حال بچه‌های کنکوری خوب نیست...
🔴
یعنی مسئولین این صحنه‌ها رو می‌بینن و سکوت می‌کنن؟
🔴
سهمیه برای ۸ نفر المپیادی ردیف شد...
🔴
ولی برای کنکوری‌های ۴۰۵، با این همه فشار و آسیب روحی
🔴
کسی به تعویق امتحانات  توجهی نکرد.
🔴
کاش یه سهمیه اعصاب و روان هم برای کنکوری‌های ۴۰۵ وجود داشت...
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/131175" target="_blank">📅 00:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131174">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kGBbyYKcBnGi5dkoQNrY9A93fXnXIRy-vyUQaoST-DkVNUNqbLkc2Sexuz0Oug6EpxvcaR_pkh4Qx_PhjEHdbDQhghOxYqYlq7oebspHDYt4gLFWipwDGX158TUWyjeIVOellMGecfGqu4y1EFuNJRMSGaNHgVRVWI5-LAu6ghi1VgiAwyPZrG71XZOYMW6d-yEu3FJlsR-KOXEXUxy1VuFhLACK7RoLtAi-Jg6NQHxjmRP6vTRVVRwpodZ_YFCLvSbVquhUNdVm7EKCphsPEo0iepXNgbWv3Pwp6uES2uWuqaIeoT_rhxIyfL3GsNP2TK9rU2m87Jh3CDhXp62DTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صداوسیما: قالیباف امشب خیلی حرف زد، بقیه حرفاش فردا شب پخش میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/131174" target="_blank">📅 00:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c196a09733.mp4?token=ipmTeB0ZMx8TdQ37oeh2i_CL3_S782ltqomEqpylnjr9dAb7ZIgvD5m7EzgwCuGShEAu-pWH6V8Rgwb32DRtN4XJ2Ag4tKtyUa1Sy-KcPsgZ_deXqgd41nazsyY2lB4waNy4-IdUfOh0TcVddRF5ATGC6SzvD-0-F8ek5POkHqaKRS3zXOVMxSxeGpcazn-IqTYltC4bZmcznl1EOC0ASG06EYrXLXuJNAm-8yUtXt-F2GyVUHOHQ7MbAhxzoiKxPNLHSylXq0M1XKXjFgxXaC2pNzGuGII2ydCIeB8Dm4L03AHefqATv-THSavPZ_BlGdNEhJeBY0qJ-CFqzJD_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c196a09733.mp4?token=ipmTeB0ZMx8TdQ37oeh2i_CL3_S782ltqomEqpylnjr9dAb7ZIgvD5m7EzgwCuGShEAu-pWH6V8Rgwb32DRtN4XJ2Ag4tKtyUa1Sy-KcPsgZ_deXqgd41nazsyY2lB4waNy4-IdUfOh0TcVddRF5ATGC6SzvD-0-F8ek5POkHqaKRS3zXOVMxSxeGpcazn-IqTYltC4bZmcznl1EOC0ASG06EYrXLXuJNAm-8yUtXt-F2GyVUHOHQ7MbAhxzoiKxPNLHSylXq0M1XKXjFgxXaC2pNzGuGII2ydCIeB8Dm4L03AHefqATv-THSavPZ_BlGdNEhJeBY0qJ-CFqzJD_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش سانسور شده صحبت‌های قالیباف در صداوسیما: قالیباف: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوپک صادرات نفت انجام می‌شود.
🔴
۲۰دقیقه از این مصاحبه توسط صداوسیما سانسور شده است !
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/131173" target="_blank">📅 00:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
دولت ونزوئلا : یه کودک ۳ ساله رو از زیر آوار، بعد شیش روز نجات دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/131172" target="_blank">📅 00:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
روزنامه «العربی الجدید»: تلویزیون ایران به‌طور ناگهانی گفت‌وگوی زنده با محمدباقر قالیباف، رئیس مجلس شورای اسلامی، را بدون ارائه هیچ توضیحی قطع و پایان داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/131171" target="_blank">📅 23:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
ونس: ما باید از طریق بازرسی‌های مداوم، برچیده شدن برنامه هسته‌ای ایران را تأیید کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/131170" target="_blank">📅 23:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نتانیاهو درباره غزه: «مهاجرت داوطلبانه» از غزه همچنان روی میز است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/131169" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو درباره ترکیه: اردوغان درباره تمایلش به نابودی اسرائیل و کنترل دوباره اورشلیم صحبت می‌کند.
🔴
فکر می‌کنم فراموش کرده که ۴۰۰ سال حکومت عثمانی به پایان رسیده است. امروز یک دولت قدرتمند اسرائیل وجود دارد.
🔴
او باید آرام شود. ما اجازه نمی‌دهیم کسی وجود یا امنیت ما را تهدید کند، و فکر می‌کنم نشان داده‌ایم که چه توانایی‌هایی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/131168" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ونس: نتیجه مذاکرات مستقیم لبنان با اسرائیل، احترام به تمامیت ارضی لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/131167" target="_blank">📅 23:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e7b409e3.mp4?token=K3guyhMuFFtzJH-0t3UCWwEiD8IVLd2Jp0Ff5nl_gWIQjKQBSXUkpkREf0WMdE40gcIb3gBOKqQqBSsI_baW4MioKBMUfJzsiv-rwJr496o_RKvZ_1eTTFPMv-XE_lbtDNfKFhJmsdh0NmHNblL8EyrOtvCX0Z1tgZgjK5_JEaunNH-iOPhtjY2MMWte8O-Uw0KJsdNEM36QkKhQDou5nxqvoW2FXwSAOZ2A9pRhbIQ_9AvNUThL3CvUL32IjzPKi_Ep_PZF--E8sTMCzTzNbWehsUjMHhYE5VUFSONvEsOVnfrP7lTHFs_QR1Ao6ij9DsIlHfCydpQWUwJeI5IkhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e7b409e3.mp4?token=K3guyhMuFFtzJH-0t3UCWwEiD8IVLd2Jp0Ff5nl_gWIQjKQBSXUkpkREf0WMdE40gcIb3gBOKqQqBSsI_baW4MioKBMUfJzsiv-rwJr496o_RKvZ_1eTTFPMv-XE_lbtDNfKFhJmsdh0NmHNblL8EyrOtvCX0Z1tgZgjK5_JEaunNH-iOPhtjY2MMWte8O-Uw0KJsdNEM36QkKhQDou5nxqvoW2FXwSAOZ2A9pRhbIQ_9AvNUThL3CvUL32IjzPKi_Ep_PZF--E8sTMCzTzNbWehsUjMHhYE5VUFSONvEsOVnfrP7lTHFs_QR1Ao6ij9DsIlHfCydpQWUwJeI5IkhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امیر رولکس : ما نرفتیم مرحله بعدی ولی کلی دست آورد بدست آوردیم اینم عزتی بود که خدا به ما داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/131166" target="_blank">📅 23:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131158">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SVRalhrxClDDFG8vT9eBTGVHa-hX-V1Id8bxfNfY9SZhgOOqKwv0jdTR9Y1aiHBLuq60f1QrZxHn_0HBvk8K6Iav7u_Hf9nZaTZgoW7VFlnVtqZG7rJyO1Jg28HzolK64tPLGOKke4fZNNXbSeyCoDIQqCUBiW_YvXjJD5DSX75SXt9E6Arp5_W5tAvrBUgmTWmca488WMz_Dm0oJwNMDVASprVoA9quCPfhGXQKgnSK3f-fxJYXY_Z5_zTsIJ_0NjQQL2NLUUUCRusLvlH__Ug5fwnLtVjeb1wCEWzcoF493OxSPU6u7_gfKWSTxtsjlurAoFxy27BFKUR6pief-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRwItdsqMDqzKBGURvkkr1bXi8dGNOuo2_Ta5MeSJGIp_wi2S9EuoTESSaVLguiqSN1aVkNAOfvFn9n-R0Z-AV3zPohTajTz8-bXsN49zMhg_IZ16Uri-3iV4fuY6esOEFAJy8QUeEVat1yXopTsiehp4_g07csuD3hnP1pfYrMP0iUhkZRtCDuBULjF-eBE1qKd_-1wNn2ZJeZu8cao6eSw0XIIUz0oI1O4OV-L7vQOEUu-RaorZabDLwSO4-BVKE-WG2Y-5kyMJq16A6pzdtkC_gzCfQ-ogWErrHIiXIpe8eOSMyj08FMbZZhpu4YwSqk9eB7BfVnCgMXOi4Ei0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tsJ43CDNTx3o0z-Wal9utsUcPwn-o6MWCLbQl9Agvq2TIIDbGhKpu2wWZuQyqT-8cAEFG7uNoPQmrYY1jdTORsFMiQIM80BaLuXMVz2TN07aBNo-cTE2rE_nV8Wxq8MhOGk5YlISi59lQWHjw8gd8x-PH9D0onJeNq_4NpKKW3iyKC4orkuHJVD-D9cPR-lyCi7GWwVzkiZ6xpiE3Dt-FuKGQD0bI0Au8bjahdsXkkfhsiNtXtBoQHSFEyFMn6n9h7m6qdGsFw2vVcfNvDCaQhapoG_bFOkCtd5OTEh92EkTb70sxV8LTXZxtyPoHtWIgg3CDNN8mpbvlwpg9Yr04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XiNE7I_ZCAueJFj2BPjG9xiEha3VHOjoN4KklGWUdheHgpPxWBjo-NP9xWJhVT6Xr3nPVyR_OmybgwnSWXq-9jajz00dJtptlU6UG9hUplshKG5YDIup27vrBbf5axsSHhKKRCv1L1XqVvQ7yaUzoM01T14xGD55qtB4kPC0YRRoN3-xNjhgnu_Ko1YRlJ1eBHFbx2AIghdct1iNUyJ9CBO6W2mERe6hB3Pcpii1YyndCSidESLwH4rkP7CbRuRoWOeEOB4R-oPFYCRknb-WKkCe8N1JbTrkhhuDvRQ1bZRpAe-RZL4XfSZF5FL0qGFZH2FECa-XY54IxxKgCBWV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ubHUKk8UtgtfvLuhWPAJARkWCkHeNhgUiHxYRVelXnfxSSfz4dTUmUHPftxRu5zHCZB-9EI5J6sykwwUp73vKqPoj4NEQkpCehJsIQmVPh1l-Be2sf3ofBNebGcUxlyV3MWQZlbKx0rMwjcfCg2yss_WZMvuZ8YS8v7RkSQLyCu-n4sm--bIL1o5ncKBQrwhJHcjTXY62iPq8LsyBnGy-MaPk1yBzwam_iTbizFGlJpWNk8JSs1hiQYeLqdFWILDHkTwwOTtTyixi_WMMq1HfBVrVVgvWXdx4lybLkBhUCDv31QE6eX6T4QqDoCHOiuudUHCPyTjI6PsQ3Hy2uBVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nvTbuYSkkZ6tK0GuFsNS1Z8zbRIoM6LGBpBB0csQLcO3AbBFDhwlg29YSSACQWjMplB-d8nH5hcAILzM3jB0vsi1FvS31-SH-yhkrZbhA6Xjd-4c1k-b7oNZamAZNLOBaK0zB9WAjDrCWSIyJFhlDNhdRE3xKBreUMS4Z9_wAXNiDX5QZpe3diQ7Y816AyBKKBQg9drmtAW7jJQnbFzFVMS8DNxzd7VH4i5pPZL0JTWNUE8cd4a1bg7hT4O55RFSJK5cR7oubwNo8D7b9rwqy7XFn7iqBqFjyK4PCf1YF2MnAQWgXG5JACYd-lsfUhj_jBTghOPDNwK1jIy51HQcdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYFAJRqbWKqpuY-Doso0pi_SIlLaqlyci6yO_5qAPV48sEDXiG4xHT8e9HbhBM9y8QsKFIz2qnuGj-I_lJWLnN0d7xE4Fnwr4NQbPSwUErKbTgeJ2M5e0YvzejLmrdqE2K6QIZwmh8ecDjGveGI9pwSfhsOch-eEKxHmmgJa_goW1nI-eadeIFygxQWui_YnCjFngo2TfZsEVCg4Njqgl4vidMI7m0Uxm3chClyJHJhqH8GDmKas30wBLEBrwJ6UzhhOUHKaw3zRRrFA2-xV84-EwE-JOt1Y20j7YM1Q5P_NDPsSCPmS_j0ePfIh-etjQPwTPOecvAO5uBgHVYnLBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc2621eaae.mp4?token=RgX5a6J2j70EHT2VkE9r4OAlCRX30zkVxcgVngU8GOu_tgf6hwHwuilCV9m1vY2V_aP6DgIIoSIcHej0QsrWgudMAK58yx1Suo-UTMFDt6_hPNyRCbRr1Bcn9DG6I8wepoty0Bsk9zK6zNEVwHANJwzcdAGuNmXyOMrYza2INui24I3wFYDy23GtLAtV1jvYuVC-OfAiaihXcDtLE9YCx6lc3pterXqYcGsSZDyrc5Hzfky2uGF6X97XuH3zkqCV8bW2iyTkPjesbAgQuZkkUz4P60rJ-Kj3VsnuL40cqYP85qig2ss4HXIiCFpUrho7MAkZkK7hqb1rHAFILmfmf5v3ELO8IF8iXNLEuCM7uJC0uJKd5acMoexV3HDvfzle1jet8qqcr1hMmzkBzFCwXscct9aEruOwrxjkLaM6mbkvdtt3_Xkyg5qX6WKXLD6GayDCmm1TL1_zzw5Iuj1C3dKX6YzWwPCW1VKR18ECkQoPKrgEOb9LAjEYTxwf2fDNPpkOwu1ilqsJiscJsfSYpch-Pkg6vCIIljFdsEUDI7_lhNMF3udwUAFiFFoXRaNkj3k7tcFDYW7tppVds4rcN3227D5pFO3PBvQ7bDtZRKwR6HDFK7k7qb4kq_CGmuw03_Op_XWTGwmbgQbKOZrCQJYlI5iJLD3rDgZG0_hXNDs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc2621eaae.mp4?token=RgX5a6J2j70EHT2VkE9r4OAlCRX30zkVxcgVngU8GOu_tgf6hwHwuilCV9m1vY2V_aP6DgIIoSIcHej0QsrWgudMAK58yx1Suo-UTMFDt6_hPNyRCbRr1Bcn9DG6I8wepoty0Bsk9zK6zNEVwHANJwzcdAGuNmXyOMrYza2INui24I3wFYDy23GtLAtV1jvYuVC-OfAiaihXcDtLE9YCx6lc3pterXqYcGsSZDyrc5Hzfky2uGF6X97XuH3zkqCV8bW2iyTkPjesbAgQuZkkUz4P60rJ-Kj3VsnuL40cqYP85qig2ss4HXIiCFpUrho7MAkZkK7hqb1rHAFILmfmf5v3ELO8IF8iXNLEuCM7uJC0uJKd5acMoexV3HDvfzle1jet8qqcr1hMmzkBzFCwXscct9aEruOwrxjkLaM6mbkvdtt3_Xkyg5qX6WKXLD6GayDCmm1TL1_zzw5Iuj1C3dKX6YzWwPCW1VKR18ECkQoPKrgEOb9LAjEYTxwf2fDNPpkOwu1ilqsJiscJsfSYpch-Pkg6vCIIljFdsEUDI7_lhNMF3udwUAFiFFoXRaNkj3k7tcFDYW7tppVds4rcN3227D5pFO3PBvQ7bDtZRKwR6HDFK7k7qb4kq_CGmuw03_Op_XWTGwmbgQbKOZrCQJYlI5iJLD3rDgZG0_hXNDs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل اعلام کرد که سامانه دفاع هوایی گنبد آهنین پس از یک سری آزمایش‌های گسترده که با همکاری سامانه‌های دفاعی پیشرفته رافائل انجام شده و شامل درس‌های عملیاتی از جنگ و عملیات اخیر علیه ایران است، ارتقا یافته است
🔴
این سامانه ارتقا یافته در برابر تهدیدات پیشرفته از جمله راکت‌ها، موشک‌های کروز و پهپادها آزمایش شد، این آزمایش‌ها همچنین شامل سناریوهای عملیاتی مشترک با سامانه رهگیری لیزری پرتو آهنین بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/131158" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131157">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پولای بلوکه شده مال دولت سیزدهم(رئیسی) بوده است، مصاحبه اش در صداوسیما قطع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/131157" target="_blank">📅 23:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131156">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گفتگوی قالیباف نصف و نیمه در شبکه خبر قطع شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/131156" target="_blank">📅 23:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131155">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=TARDm8syvRMgaYCpIJXtNCpKkSLDTMNoNch-SqjA_B7RzHVhduVH8ulB5INAFCLD_qwxHVeKo7C3KTOikc3xd-CVGygVlzdBiqLMJFQhUSEpLaNyyurk_QMF7lygJKlV40W5wrr_GVGZLLWeJhdbR3JA9xc2v58mYhdneLKsh9tgHdUDgsfts6DNCp0j5lxsjkqfyUD52EW0NxAPqRp_w80miGbWymHc610btyXmfsa2TWZ4twrOBoLweIT3EXOYPs20WHgG59iq1Nlf5OkGbSCgMD7V5rqb5BQR-X-u7bEs4H4vp_GEZj_He1mdpDuiKvoP6rxlknbI_kf7HIq9og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=TARDm8syvRMgaYCpIJXtNCpKkSLDTMNoNch-SqjA_B7RzHVhduVH8ulB5INAFCLD_qwxHVeKo7C3KTOikc3xd-CVGygVlzdBiqLMJFQhUSEpLaNyyurk_QMF7lygJKlV40W5wrr_GVGZLLWeJhdbR3JA9xc2v58mYhdneLKsh9tgHdUDgsfts6DNCp0j5lxsjkqfyUD52EW0NxAPqRp_w80miGbWymHc610btyXmfsa2TWZ4twrOBoLweIT3EXOYPs20WHgG59iq1Nlf5OkGbSCgMD7V5rqb5BQR-X-u7bEs4H4vp_GEZj_He1mdpDuiKvoP6rxlknbI_kf7HIq9og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: رئیس‌جمهور آمریکا گفته پول‌های بلوکه‌شده صرفاً برای خرید غلات آمریکایی آزاد می‌شود. این چقدر صحت دارد؟
🔴
قالیباف: واقعاً هیچ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/131155" target="_blank">📅 23:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131154">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b26e4e44f.mp4?token=hjOfM0hyJe62rm9DJKphPbO3Qv7fJ-59ti6KDYMjl5_cnSFU1VsE1arU7lrQn6cbMkOq6Iwjv20DWdpx0P0Y4feo4rmCQaEg8pwTAfK5nzKulUqfCtO3zZqQDLRyhhgfgUl8wMKvPigvXwSU6rUfL56Uxln2BxSCPSZ2J3SOBFIVRDbBkhfIFCZA3Mjc4mxo5JoJAyNQ5bIHlksBigqCxGMBGdpH7iWI841jGB9Mm9UsH7LHw8YUkdhgwqDG-Y-5YdoD8UARAKERPIx0PiEuFPm0DR94KEyZGEygcjobqQrNccOVD3iVucNHYFUYSA8raDh0vZlkOQ8u_-vJRPaYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b26e4e44f.mp4?token=hjOfM0hyJe62rm9DJKphPbO3Qv7fJ-59ti6KDYMjl5_cnSFU1VsE1arU7lrQn6cbMkOq6Iwjv20DWdpx0P0Y4feo4rmCQaEg8pwTAfK5nzKulUqfCtO3zZqQDLRyhhgfgUl8wMKvPigvXwSU6rUfL56Uxln2BxSCPSZ2J3SOBFIVRDbBkhfIFCZA3Mjc4mxo5JoJAyNQ5bIHlksBigqCxGMBGdpH7iWI841jGB9Mm9UsH7LHw8YUkdhgwqDG-Y-5YdoD8UARAKERPIx0PiEuFPm0DR94KEyZGEygcjobqQrNccOVD3iVucNHYFUYSA8raDh0vZlkOQ8u_-vJRPaYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو : اگه لازم باشه، برای بار سوم به ایران حمله میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/131154" target="_blank">📅 23:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131153">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
گفتگوی قالیباف نصف و نیمه در شبکه خبر قطع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/131153" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131152">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f975bb897.mp4?token=d4PMU43_6ajd9d4sK4fHXC6SQKYu4zzWqJNkdZfsdM-BryXlht2A9uYMZKcJJmOKEAXVNdO6HLZrrxgWLIm9uvU0NAnBqBhcPZ9n9xR_RLvGGetN4oqB0q091ZjwDbq0xbz0lCqLKq_4xdipsyJ0HXLeMFfgGqEmBMJQr_29K1bGvmr4pModUazeXIucush6z3oF6xcDWx7EIMCPHKfNpmB0xuRLS2AlyqtH6cL8N6vn8HIqkVuhvx4okRVJfVF_lqfwG1h4BpzhmT7aeVP82ZAMl3NmaHc29678-MFDClotHbdCsqJNXF2hmLHT-23bfTzuLptl6Xxv1Ao4_16lSToNhlw7krLlfoYefw2FO2LQOYHzjm67XJO-ODADzhKnxFZNbzK9c_3VV4ullpb1kHtGyj4-FUHaoGko3V01gRSQKbNEA-eXKBf1-C2vDvG34sAK-Pdb4q8b2xS20OiJDQDJMoqDrKJa2yb0k0IOMLFfhqinGveN54GAbyIw0RfrIhqummV822bPpU0i9PHOAcshjzsOmYqGSHtnEHZNsVNKoTKeueBOtDXGvg7iKlFKvBCPawAzmxDQykRQzLKtzzhP4FbcvsHRXWOB5A2p9mTxcGjFZJ34ekofXzZDAnWcw67xC-YLRMzZr-9z8_IXfHccR0BXbCk4d1l7G0nuOtc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f975bb897.mp4?token=d4PMU43_6ajd9d4sK4fHXC6SQKYu4zzWqJNkdZfsdM-BryXlht2A9uYMZKcJJmOKEAXVNdO6HLZrrxgWLIm9uvU0NAnBqBhcPZ9n9xR_RLvGGetN4oqB0q091ZjwDbq0xbz0lCqLKq_4xdipsyJ0HXLeMFfgGqEmBMJQr_29K1bGvmr4pModUazeXIucush6z3oF6xcDWx7EIMCPHKfNpmB0xuRLS2AlyqtH6cL8N6vn8HIqkVuhvx4okRVJfVF_lqfwG1h4BpzhmT7aeVP82ZAMl3NmaHc29678-MFDClotHbdCsqJNXF2hmLHT-23bfTzuLptl6Xxv1Ao4_16lSToNhlw7krLlfoYefw2FO2LQOYHzjm67XJO-ODADzhKnxFZNbzK9c_3VV4ullpb1kHtGyj4-FUHaoGko3V01gRSQKbNEA-eXKBf1-C2vDvG34sAK-Pdb4q8b2xS20OiJDQDJMoqDrKJa2yb0k0IOMLFfhqinGveN54GAbyIw0RfrIhqummV822bPpU0i9PHOAcshjzsOmYqGSHtnEHZNsVNKoTKeueBOtDXGvg7iKlFKvBCPawAzmxDQykRQzLKtzzhP4FbcvsHRXWOB5A2p9mTxcGjFZJ34ekofXzZDAnWcw67xC-YLRMzZr-9z8_IXfHccR0BXbCk4d1l7G0nuOtc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس درباره مذاکره کنندگان جمهوری اسلامی ایران: یکی از چیزهایی که درباره ایرانیان هم شگفت‌انگیز و هم کلافه‌کننده می‌یابم این است که می‌گویند «نه، نه، مذاکرات صلح در جریان نیست»، در حالی که مذاکرات فنی بین ایالات متحده و ایران درباره توافق صلح در جریان است. این یک تاکتیک مذاکره‌ای ایرانی و یک ابزار بلاغی ایرانی است که من آن را درک نمی‌کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/131152" target="_blank">📅 23:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131151">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fd90a566a.mp4?token=q3bkiMkM3Zq_2WLGm6HPfffmuo6i8RGwXFGNbD4GVErMG_zTz11W_cnePvAmwjOE3ARblUkEj1AwrCLKqNCp0BN5WGdTO95BnMliknuWL5W_Lh2T82--i02wLA-VP8PmLTSKseVlnmpbFRKw5aPHOFUiRqDHZ58_Q8U2HsXRPxBE-os5Q8v5R-WsnOEuZipEnW0k8tTlstItjzSRxiw4ny1e_Iar4NmZqLaEIbc36FWczY3wHoEVoZxQb1nJ-ooNI9RBHkfqS-1gZlu_vUTXatkKaqj8mZ0PpesnRsW6W0i5VedioS3PNgSzE2atyO_vfSm6UNdc0e-oK9RKpcr6VB_TQMKghkrkFl2lRILB0WJqg8msUdbOsf8f_I3lBkLohCQclmQcL2KXNi9hx1WiGS-pOrZyzOnzHDLNdRoCcWX4vsALLFccd03KgT5DjbehCvAxeGWVa4S7n1F5nU85WIjuYVT46xydvlrrLxNWvzK5Sx3oXzYv4SOLTw6_pvzmwgyHkhEtUTWgMwHdAVwziq-wpREoBhnmE6qNcLl5F8YvD4sfJr26981NfAQLKdET92XFALUWsJJ__F1w7TyhOSop3ewgITA09JYJmTbL5eap_5NDI7fvVhPwDrV_EA6HmdgRJRk-DJ1sZwYvYjTYTXnIECs5LnQiT8ZI0TNTV4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fd90a566a.mp4?token=q3bkiMkM3Zq_2WLGm6HPfffmuo6i8RGwXFGNbD4GVErMG_zTz11W_cnePvAmwjOE3ARblUkEj1AwrCLKqNCp0BN5WGdTO95BnMliknuWL5W_Lh2T82--i02wLA-VP8PmLTSKseVlnmpbFRKw5aPHOFUiRqDHZ58_Q8U2HsXRPxBE-os5Q8v5R-WsnOEuZipEnW0k8tTlstItjzSRxiw4ny1e_Iar4NmZqLaEIbc36FWczY3wHoEVoZxQb1nJ-ooNI9RBHkfqS-1gZlu_vUTXatkKaqj8mZ0PpesnRsW6W0i5VedioS3PNgSzE2atyO_vfSm6UNdc0e-oK9RKpcr6VB_TQMKghkrkFl2lRILB0WJqg8msUdbOsf8f_I3lBkLohCQclmQcL2KXNi9hx1WiGS-pOrZyzOnzHDLNdRoCcWX4vsALLFccd03KgT5DjbehCvAxeGWVa4S7n1F5nU85WIjuYVT46xydvlrrLxNWvzK5Sx3oXzYv4SOLTw6_pvzmwgyHkhEtUTWgMwHdAVwziq-wpREoBhnmE6qNcLl5F8YvD4sfJr26981NfAQLKdET92XFALUWsJJ__F1w7TyhOSop3ewgITA09JYJmTbL5eap_5NDI7fvVhPwDrV_EA6HmdgRJRk-DJ1sZwYvYjTYTXnIECs5LnQiT8ZI0TNTV4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی وانس در مورد جمهوری اسلامی ایران: ترامپ مایل است بمب‌ها را رها کند، اما فقط اگر هدفی را پیش ببرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/131151" target="_blank">📅 23:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131149">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04d179f44d.mp4?token=VR7YmBb4NTOAyzgKG2NxH5juxz0LvuCFXL2MaYVn0GnUfYfgoazGWwWiimXquxhPohezcw-2fqZdAv4YnO-pgsl2THuryrvA0Sfjlvo1jQHSrVQoYjMO7B656ZllmP0H7ygRFoLR72ZlLegh3ahkXt9IhCn2KmPUyy60kvPDu35ApHl2QNxP5q_rJYuvIUOOmEUs7NGpPRRc28ZLPPK4w3Y2rPfrgcnXR1hHJVkiJCvo2rlRskBNoF_FcOTlrOEM7RMdplDh2uiD2poaKioF6nayynwegX4mi2Ls8FRgJEtqf_9zqxFcAZ87fDqt-uIUWmACIWmI2Svx8n1ttXbqQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04d179f44d.mp4?token=VR7YmBb4NTOAyzgKG2NxH5juxz0LvuCFXL2MaYVn0GnUfYfgoazGWwWiimXquxhPohezcw-2fqZdAv4YnO-pgsl2THuryrvA0Sfjlvo1jQHSrVQoYjMO7B656ZllmP0H7ygRFoLR72ZlLegh3ahkXt9IhCn2KmPUyy60kvPDu35ApHl2QNxP5q_rJYuvIUOOmEUs7NGpPRRc28ZLPPK4w3Y2rPfrgcnXR1hHJVkiJCvo2rlRskBNoF_FcOTlrOEM7RMdplDh2uiD2poaKioF6nayynwegX4mi2Ls8FRgJEtqf_9zqxFcAZ87fDqt-uIUWmACIWmI2Svx8n1ttXbqQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اظهارات جنجالی منان رئیسی، نماینده مجلس در صداوسیما درباره بندهای تفاهم‌نامه
🔴
برخی از بند های تفاهم‌نامه آنقدر ضعیف امضا شده که اصلا نیاز به نقض نداره و خودبه‌خود ایده‌آل آمریکا است/ در سند امضا شده که آمریکا باید مشخص کند پول های آزاد شده را کجا باید خرج کنیم/ آمریکا غلط کرده به ایران بگه پولشو کجا خرج کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/131149" target="_blank">📅 22:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131148">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
قالیباف: تنگه هرمز بزرگترين ابزار قدرت ماست، باید از این نعمت الهی به درستی پاسداری کنیم.
🔴
باید روز به روز رونق تنگه هرمز را بیشتر کنیم
، محدودیت را باید برای آمریکا و اسرائیل بگذاریم اما تردد باید بیشتر شود.
🔴
باید به دنیا نشان دهیم امنیت اینجا روز به روز بیشتر می‌شود و حتی هزینه بیمه کشتی‌ها کاهش یابد.
🔴
برخی می‌گفتند رفع تحریم وعده سرخرمن است، رفع تحریم‌ها انجام شده و نفت ایران ۲۰ درصد گران‌تر فروخته می‌شود و پول آن به حساب واریز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/131148" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131147">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">➕
حتما یک بار تست کنید تا سرعت و کیفیت رو متوجه بشید
✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
در هر صورت تمامی سرویس ها قابلیت مرجوعی دارن و هرموقع راضی نباشید میتونید مرجوع کنید
خرید فوری از ربات های زیر :
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/131147" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131146">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚀
سرویس Vpn(v2ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
دارای ساب برای اطلاع لحظه ای از باقیمانده
✅
متصل در تمامی دستگاه ها و اینترنت ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
پشتیبانی تا پایان سرویس
💬
تعرفه‌ها
🔸
پلن‌های یک‌ماهه
▫️
۲۰ گیگابایت — 50,000 تومان
▫️
۴۰ گیگابایت — 95,000 تومان
▫️
۶۰ گیگابایت — 140,000 تومان
▫️
۸۰ گیگابایت — 185,000 تومان
▫️
۱۰۰ گیگابایت — 230,000 تومان
▫️
۱۵۰ گیگابایت — 340,000 تومان
▫️
۲۰۰ گیگابایت — 450,000 تومان
▫️
نامحدود (مصرف منصفانه ۳۰۰ گیگ) — 560,000 تومان
🔹
پلن‌های دوماهه
♦️
۳۰ گیگابایت — 95,000 تومان
♦️
۵۰ گیگابایت — 140,000 تومان
♦️
۷۰ گیگابایت — 185,000 تومان
♦️
۱۰۰ گیگابایت — 250,000 تومان
♦️
۱۵۰ گیگابایت — 365,000 تومان
♦️
۲۰۰ گیگابایت — 475,000 تومان
♦️
نامحدود (مصرف منصفانه ۴۰۰ گیگ) — 675,000 تومان
🔸
پلن‌های سه‌ماهه
▫️
۸۰ گیگابایت — 240,000 تومان
▫️
۱۰۰ گیگابایت — 275,000 تومان
▫️
۱۵۰ گیگابایت — 390,000 تومان
▫️
۲۰۰ گیگابایت — 500,000 تومان
▫️
۳۰۰ گیگابایت — 720,000 تومان
▫️
نامحدود (مصرف منصفانه ۵۰۰ گیگ) — 820,000 تومان
خرید:
🤖
@Team_express_bot
🤝
فروش عمده و پنل نمایندگی:
📩
@expressuport
📢
کانال اطلاع‌رسانی:
🌱
@vpn_express_sup</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/131146" target="_blank">📅 22:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131145">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
قالیباف: به خاطر مشکلات سیاسی با من قالیباف حقوق ملت را از بین نبرید
🔴
کسانی که حرف ترامپ فاسق را قبول می‌کنند یک‌بار حرف برادر دینی خود را هم بشنوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/131145" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131144">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قالیباف: حاکمیت تنگه هرمز با ایران و عمان است و تردد در تنگه با ترتیباتی است که ایران مشخص می‌کند البته ما با کشورهای ساحلی خلیج فارس تبادل نظر می‌کنیم.
🔴
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید و این آب‌های سرزمینی ما است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131144" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131143">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
قالیباف: در متن تفاهم آمده است که عبور از تنگه بدون هزینه فقط برای ۶۰ روز است، این موضوع به دلیل اصرار کشورهای منطقه و کشورهای ساحلی خلیج فارس بود و عمدتا برای کشتی‌هایی است که با آغاز جنگ به دلیل بسته شدن تنگه در آن منطقه بودند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/131143" target="_blank">📅 22:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131142">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قالیباف : اگر از اجرای آنچه مورد بحث قرار گرفته است خودداری کنند، ما نیز برای جنگ آماده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/131142" target="_blank">📅 22:48 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131141">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
قالیباف: غنی سازی حق ماست، خط قرمز ما در این حوزه مشخصه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/131141" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131140">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
قالیباف: بعضا می‌خواهند مدیریت و ترتیبات ایرانی در تنگه هرمز را رعایت نکنند و طبیعتا ایران عکس‌العمل نشان می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131140" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131139">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
قالیباف: از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/131139" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131138">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قالیباف: در آمریکا روبیو موضوعات را یک‌جور دنبال می‌کند و ونس هم جور دیگر دنبال می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/131138" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131137">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔴
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها  در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131137" target="_blank">📅 22:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131136">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
قالیباف: الان هیچ مذاکره ای نداریم. سفر به سوئیس هم برای گفت و گو درباره اجرای بندهای ۵ گانه بود. در گفت و گوها ما نتایج مذاکرات قبلی را پیگیری می کنیم تا محقق شود.
🔴
پس از امضای یادداشت تفاهم اسرائیل تهاجم سنگینی به لبنان داشت و به دنبال اشغال برخی نقاط مهم بود تا تفاهم با مشکل مواجه شود.
🔴
این اتفاقات باعث شد به سوئیس برویم و در آنجا موضوع اصلی که پیگیری کردیم آتش بس لبنان بود. بعد از این پیگیری ها، حجم حملات به لبنان قابل مقایسه با قبل از آن نیست.
🔴
یک کمیته مشترک بین ایران، آمریکا و لبنان ایجاد می شود تا حاکمیت ملی لبنان را محقق کند، سفیر کشورمان نیز نماینده ما در این کمیته است.
🔴
این که تلویزیون تحولات لبنان را برجسته می کند خوب است اما گاهی به این موضوع هم اشاره کند که شرایط لبنان چطور بود و الان چطور شده است
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد. کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/131136" target="_blank">📅 22:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131135">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قالیباف: آمریکا در یادداشت تفاهم متضمن شده که در لبنان جنگ پایان یابد و لبنان بر سرزمینش حاکمیت داشته باشد و ما دنبال اجرای قطعی این موضوع هستیم.
🔴
نسبت به اجرای تفاهم‌نامه مصریم
🔴
ما هم درحال گفت‌وگو هستیم و هم اگر تفاهم را اجرا نکنند آماده جنگ هستیم و عکس‌العمل نشان می‌دهیم.
🔴
ما در سرزمین خود کمتر درگیر آن هستیم. تنش‌های ما گاهی، همان‌طور که دیده‌اید، شب‌ها اتفاقاتی رخ می‌دهد
🔴
گاهی می‌خواهند عبور و مرور در تنگه هرمز را با ترتیبات ایران نپذیرند و اقداماتی خارج از توافق انجام دهند.
🔴
طبیعتاً جمهوری اسلامی متعهد است که عبور و مرور در تنگه هرمز حتماً در راستای آن تفاهم‌نامه انجام شود.
🔴
اتفاقاتی که این شب‌ها در خلیج فارس رخ می‌دهد را نقض تفاهم پایان جنگ می‌دانیم و حتماً به آن عکس‌العمل نشان می‌دهیم. در آخرین نقض آتش‌بس، مقرهای آمریکا در بحرین و کویت هدف قرار گرفتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/131135" target="_blank">📅 22:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131134">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف: محاصره دریایی خودش جنگی غیرقابل وصف بود که با تفاهم برداشته شد./ما داریم دوران گفت‌وگو را دنبال می‌کنیم برای تحقق ماده ۱۳ یادداشت تفاهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/131134" target="_blank">📅 22:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131133">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh-_EfbslfirGroPnPLQ9gQCbP3xxP5TmtB8iFLv6bFJfGNoPLm4lyZweb6a5k12LpgXZgF3M8msAZ-HAltdOiJgDma7eK-2-pbno7VzKTxSa5taKVbgUUkyhKzCeD4Z1NIc4gd1cFQdg77XNOHQSdNFbB_Sy1xTiwsFOo0E3lDkgt3oMHkXVrmaITvdlHFbDu_9ptuR3CqMRdm3wunUdBuhjHPRH0MxDvE3u2AbzGqkvzVra3UhwY-Rz3jR9hD2W0ZPvVwakRNfSRYgfpR7GCi09PBh5b843MQ_wjFnApANlIuL407m8ORElSJpQu5Hm2fOqOOFilTRb9FtxYm27g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسخ عراقچی به سخنان وزیر امنیت داخلی آمریکا: به جهانیان ثابت کردید که شایستگی میزبانی یک تورنمنت بین‌المللی را ندارید!
🔴
مارک‌وین مولین، وزیر امنیت داخلی آمریکا، در واکنش به حذف تیم ملی ایران از جام جهانی ۲۰۲۶ مدعی شد که پس از قطعی شدن این نتیجه «از خوشحالی رقصیده است».
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/131133" target="_blank">📅 21:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131132">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: ارزیابی ارتش اسرائیل این است که حماس از نظر انسانی و لجستیکی برای نبرد بعدی در نوار غزه آماده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/131132" target="_blank">📅 21:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131131">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
دولت ونزوئلا : تعداد کشته‌‌های زلزله به "۱٬۹۴۳" نفر رسیده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131131" target="_blank">📅 21:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131130">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cv6Z64m3AOagiOvArjNQgehmcYj1eKHPzUb7ibdQ9ovW-jVYuHtr3Iebwntlk5-EQ7fL19hy05mC-ao4EcbpJG3Ng6_pwYkEHE6DB8dMqTbwIM3DLPaZpfIRUEmJ1gCOYQBWEdI2wS4PZJRe_Haxw6WY9sd5DXYVP5RjuQqFXwuMs2U3hkyFpy3jDnA_d1vwf3SWMqB-jWiO6cnrZ27oMk-P1_INlyfm8aG_aqcaMljDKCXeUyEQjlqeXlaJmstTk9uyeQmr9eo2R7TVuUJ0WoMDIAtQk3Li8FEPNnhrl9tVBcl_k-T7EoVQS-CsKrFuaKbmrpvPK-rc27eJVWV5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طعنه ترامپ  به چینی ها بعد از رای دیوان عالی کشور: من می‌خواهم رئیس‌جمهور شی و کشور بزرگ چین را به خاطر پیروزی بزرگ آن‌ها در تابعیت تولد تبریک بگویم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/131130" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131129">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
تانکر ترکرز: ایران از زمان رفع تحریم‌های آمریکا، ۵۰ میلیون بشکه نفت صادر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/131129" target="_blank">📅 21:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131128">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سی‌ان‌ان: با تعلیق موقت عملیات در تنگه هرمز، تا کنون حدود ۲۵۰۰ دریانورد از تنگه تخلیه شده‌اند و بیش از ۸۵۰۰ نفر همچنان در تنگه سرگردان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131128" target="_blank">📅 21:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvzMILsDM3MH5oUHU9yuYSTiGmer0q-mMykky-jj4y778eqYlGyi8wxoOvnj02vho7CbMVGNdGPIlg59VT_4AjDWTcBWI5Ng8rZ5EB3hfY9oPEooERDknHXPwlGyEd5GzJMEi0XuubP5-kTZ280Cbfy5pjpVojf0-RKGSi-x33N515yn3Kwj2BEFzrDfPfwoe8o6BZJfg9S5QU_D51mQwC5Lm9OJgW7gqfQrsciva_x2tV5rdGBK76lTnSXkbVskaRWZjBViimX0OweaCh7KSYLJVBDYlOIwp-hrZWNvhwcQ3htEByFFJZDj8BNI2zhpEamItdk4WVP8dUaxN2_ujw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌های 6 سال پیش یه رستوران شمال تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/131127" target="_blank">📅 21:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
پرتاب موشک کروز Kh-59/69 از جنگنده-بمب‌افکن سوخو-34 به سمت اودسا، اوکراین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/131126" target="_blank">📅 21:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
بلومبرگ: پاکستان پس از اختلال در صادرات قطر که این کشور را با کمبود فوری عرضه مواجه کرد، یک محموله اضطراری LNG خریداری کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/131125" target="_blank">📅 21:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
صدا و سیما: استعفای وزیر نفت تکذیب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/131124" target="_blank">📅 20:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: برای ازسرگیری تردد در هرمز منتظر اجازه ایران هستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/131123" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131122">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
در پی شکایت ایران‌ خودرو، تردد خودروهای پلاک منطقه آزاد انزلی در خارج از محدوده تعیین‌ شده، لغو شد
🔴
تفاهم‌نامه‌ای که به امضای ۵ استاندار رسیده بود، با یک شکایت و یک ابلاغیه، به تاریخ پیوست؛ حالا پلاک انزلی در جاده‌های همجوار، «خارج از محدوده» محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/131122" target="_blank">📅 20:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131121">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بر اساس اعلام رئیس کارگروه آرد و نان اتاق اصناف کلیه نانوایی‌های بربری و سنگک مناطق ۱ تا ۳ تهران آزادپز شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131121" target="_blank">📅 20:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131120">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=IoTXoqvOcOj6kadFnihYPmed40X-r_iGtZGEXYJi9GJMMyv8K7UjMIzrswCACucAXCrxQoxr9F5ah0N4EKfuZ115Z84X0u_sJ_bteKmtTZHtPRB42qVjJTzvO1RK3eTBGL3ur2eQcZ6gNPe5vawUcyYGS6U-VCq-4NpWW7FdyGxaPCzFHxG8uQhb2fNxu3gTLSK09H72-DPwoRf99HR1AcZrErCY-2MN_o_HPCrSYeQ1nlmuhHYdfNPAIzbzCm35HlrhgEKHDPSoGk92Yh2AkLAex9SVVHrU8OkPkDFj37VlodF_KyvvXfSdsHcp1KWvSuzfPeFJgTNTvP-jUUA8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f337fc8f1.mp4?token=IoTXoqvOcOj6kadFnihYPmed40X-r_iGtZGEXYJi9GJMMyv8K7UjMIzrswCACucAXCrxQoxr9F5ah0N4EKfuZ115Z84X0u_sJ_bteKmtTZHtPRB42qVjJTzvO1RK3eTBGL3ur2eQcZ6gNPe5vawUcyYGS6U-VCq-4NpWW7FdyGxaPCzFHxG8uQhb2fNxu3gTLSK09H72-DPwoRf99HR1AcZrErCY-2MN_o_HPCrSYeQ1nlmuhHYdfNPAIzbzCm35HlrhgEKHDPSoGk92Yh2AkLAex9SVVHrU8OkPkDFj37VlodF_KyvvXfSdsHcp1KWvSuzfPeFJgTNTvP-jUUA8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحات سازی روسیه در منطقه ولگوگراد اصابت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/131120" target="_blank">📅 20:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131119">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: در نشست فردا عمدتاً در مورد دریافت پول‌های بلوکه‌شده و آتش‌بس در لبنان بحث خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/131119" target="_blank">📅 20:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131118">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ijd9NXl4Yn8mCs5VSTMlqjJOrAdWsXbEM6CH4SFmpFdjllAaQF5UP3CpjSKBTzYdXA6JtNqtAs5ddN2AiSDkeAeJzfb-fruwK8SXZSWaejnjMR4xV1TBb-ymFM7v6GyUq-1VN7Mpo4Uvx00VwLEN1Smu5jZlFT1oj08jAIIbR2oqItje_3PMbqei0FME1lL7BHbJqvoAoE-xrz_lOkwKlNOYSucPsiMvPb4wVV6x6hCjRFcXT1yQbno08AIXDq5iwNUClKdfhv_3A_uHlmv-lRwWpiGRhQJzKLUkG5mRMiYzpg--10dsNJ5Y41lhUaBsD7QqW_0-u4Y0uGki2i4L7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث سوشال: دیوان عالی کشور حق تابعیت از طریق تولد را تأیید کرد که برای کشور ما بسیار بد است، اما ما می‌توانیم به راحتی آن را از طریق قانون‌گذاری در کنگره جبران کنیم، با حمایت رئیس‌جمهور که اکنون در این فرآیند تعیین شده است.
🔴
هیچ اصلاحیه طولانی و غیرقابل مدیریت در قانون اساسی لازم نیست! کنگره باید از امروز شروع به کار کند برای پایان دادن به حق تابعیت از طریق تولد که پرهزینه و ناعادلانه برای کشور ما است.
🔴
آن‌ها حمایت کامل و مطلق من را خواهند داشت!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/131118" target="_blank">📅 20:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131117">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131117" target="_blank">📅 20:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131116">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/131116" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131115">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyztGjM6X7d7GeH_qNBeK2vp7cyXxaCPXfpgkf4knGWbDEYuZBL8XzJRuA7vilb3rR7nqtSKl5gMR-gYyqlrSp0j457_HdvZHqcpcZY9l-lGeAu2j_znJwPiU018F-LaezpUTOZh9_GlHIWZ64xB4s6xtQWXwnTxaHOYq_qh_dO7Kvzimsa2eYEzyLMgG5MYF-jdDQzcRUHf18pwSxplMRxnd8z1X6BpKOLXbtDaHXAPGwhfIol5O4rFjflylUSlvGtCHLgaLOewnT-DPu8sp2k9fM6Yxb90PvkFy56lPbPo1WFJPe3fZOSj5auBKwNg5Egel5X5zcbHYR2R8H72lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به هر کدوم از بازیکنان تیم ملی فوتبال، حق الزحمه 100میلیارد تومانی پرداخت شده
🔴
قلعه نویی هم 170میلیارد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/131115" target="_blank">📅 20:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131113">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/om7u6ycJeo6SAN92O9DVz6AYvLmk6DBEaozS2h09ABOy6KRaDNlwuhHXN3LQPdNRDTopNRfd4ObQVR8zeSj7shsPY2CChE3arbdAVb9RGBSE9F5qTxC950ZqFSwKl9_yY0OLlJqgT7GflZia3YVH9zhz_m0jobE7fCjpaTvW5I1GV62pTkokV0xJQFcN9iGVV9KYFXhmEOl83ZS9Nl-2bPAdDxtza0SftVlm8DcITRFXxOHVt9DMj6SNXCg1xQe2vy6i7vMIOGlX4m3eKd7Clq8CDFO3sfVOVjJSOV3YdDAbKCxxCzpUuU3bGNROenfTTNLYefvbj1lwZMVKi3xTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ijyfgRpvP5WIMdCnIgNbbIJF0eKm4GzJi5KlmQg9DpMK3rsycb51GdpoO1vQ07eLsV4L92CDD93G13gMyjPO-KfijG8Kw34Wc9EBgBA1gu7gAsCTZMu46t0wbDy8oTVIQpouZCUyfL41akk1uMckt0AijBNQ_IorfnYGR3ttRGYhVn-doEy_SHyTn7eSfun15IyACKcbKd5an6yluSw24pdgRr3mIl6S0Fz_zE_jz9Fjtfgpi58XcFQR7npIyjBkhHKdLH53MOFTZpfpseffBwudj-uUUV4YR3quE3e13XVWwZED8VJ1Y7-8hpXV1Brqs3MCt1IVUOJebnxzdCDrYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه اردوغان امروز پیش از ظهر در مجتمع ریاست جمهوری در آنکارا با رئیس سیاست خارجی اتحادیه اروپا کایا کالاس و هیئت همراهش دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/131113" target="_blank">📅 19:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131112">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
بر اساس مصوبه شورای‌عالی بورس و اوراق بهادار و در اجرای تصمیم هیئت دولت درباره تعطیلات سه‌روزه ابتدای هفته آینده، بازار سرمایه ایران در روزهای ۱۳، ۱۴ و ۱۵ تیرماه فعالیتی نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/131112" target="_blank">📅 19:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131111">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رئیس پارلمان عراق: پارلمان، دولت و وزارت خارجه عراق با هرگونه حمله از اراضی عراق به کشورهای همجوار مخالفت کرده‌اند.
🔴
عراق منافع مشترکی با آمریکا و ایران دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/131111" target="_blank">📅 19:50 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
