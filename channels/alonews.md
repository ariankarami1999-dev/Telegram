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
<img src="https://cdn4.telesco.pe/file/Vcl_DXfJZACJRC5jQ6xLhznzx1jK7veoIfzVbTYvnpOze2Ha_x0NulLIftYAaZRgK0BVOMAjuaoKd_TQWPek1usBELzMhqt7QsU3xcFPRTv4rIeiRw6AcUQWmRiftMrA6gPMCwV_B7s-21gM5z7tc6yvhWd8AYk1s8yxSekhYdKxW-2f1oP1nNDx1WwaofvCs71dZWbO4SIxFaX4pO7Oi-sXadCGaTpo3r-gO9Nd_t2L1P97r6L5Sa4-QpsEGyCfeDxGpr73N7uCshRstMgkC981RMl4fdQ8szJp9ZM3c3kXZzJsHbl0FY1UkLAlvItK8pbwflfBWx8gu1kB1XF0Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 936K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-04 22:27:12</div>
<hr>

<div class="tg-post" id="msg-122644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxLTW73JMXUu0xHgyaR4i49q4z11zg2K4Ivgfxf6LK1yXjup9aqeLsws9HMaRcTh9doIZMbCqxcjGuMzZ42wDPpKYJP3uvvP3SOhUtxdZ0N7o1KHR960CD1TtNGPLKGDhD9NZRI2FjzCC7nS-uCfoVvAxtbvD4i5oeRm0g7rm4Y-soS_eP3_fzOihTdVFXUxX02FQbgz7mvWz7EYrYbnLM8zT7__R4yXfGDVUTvC2S_ACeY1OC8zsGf8VvB-UcNp4zVwrfSTgPM4UsNBE0HCUiwcc6C5f0U3DiBRctIUDIGHP_KS4ygx9vl0jUj9QIYl7pxKgBD9YC0ggtMy9mB9Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/alonews/122644" target="_blank">📅 22:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
وزیر امور خارجه روسیه، سرگئی لاوروف، در تماس تلفنی با مارکو روبیو، وزیر امور خارجه آمریکا، اعلام کرد که نیروهای روسی حملات سیستماتیکی به اهداف نظامی در کی‌یف انجام خواهند داد.
🔴
لاوروف همچنین از آمریکا خواست تا کارکنان دیپلماتیک آمریکایی را از پایتخت اوکراین تخلیه کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/122643" target="_blank">📅 22:16 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری /  نتانیاهو: دستور دادم حزب‌الله نابود شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/alonews/122642" target="_blank">📅 22:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ارتش اسرائیل شروع حملات به چند شهر لبنان را تایید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/alonews/122641" target="_blank">📅 22:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره: احتمال دارد اسرائیل پیش از هر توافق ایران و آمریکا، دست به یک عملیات نظامی بزرگ در لبنان بزند
🔴
با هدف استفاده از فرصت زمانی باقی‌مانده تا توافق ایران و آمریکا.
🔴
یا برای به شکست کشاندن توافقی که بر توقف جنگ در جبهه لبنان نیز تأکید دارد. و احتمالاً ممکن است شاهد بازگشت جنگ به منطقه باشیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/alonews/122640" target="_blank">📅 22:04 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آمریکا هیچ تصویری از پیروزی ندارد و هیچ یک از اهداف اعلام‌شده‌اش را محقق نکرده است، در حالی که ایران بقای خود را تضمین کرده و با بستن تنگه هرمز قدرت خود را نشان داده است، به نوشته اسرائیل هیوم.
🔴
تنها نتیجه ملموس تاکنون بازگشایی متقابل تنگه است؛ همه مسائل دیگر — از جمله برنامه هسته‌ای ایران، موشک‌ها و نیابتی‌ها — به مذاکراتی با تاریخ مشخص موکول شده‌اند.
🔴
این توافق حتی حزب‌الله را به آتش‌بس ملزم می‌کند و عملاً ایران را به عنوان یک بازیگر نظامی و سیاسی در لبنان به رسمیت می‌شناسد، که کاملاً در تضاد با اهداف اولیه جنگ است.
🔴
تمام مسائلی که برای اسرائیل حیاتی هستند به مذاکرات آینده موکول شده‌اند و هیچ‌کس نمی‌داند آیا این مذاکرات اصلاً برگزار خواهند شد یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/alonews/122639" target="_blank">📅 22:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نبویان، نماینده مجلس: رها کردن مدیریت و حاکمیت بر تنگه هرمز در هر توافقی با دشمن، خسارت بزرگ و شکست برای ملت ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/alonews/122638" target="_blank">📅 21:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VegbmYz-TWZQdfRvKO6zDV01nyxZjsolbtoAGxZu0G98rXPa4gYZ03Se7nPcI6xwo07M0XLeYy7NWhC8WYU0rBwnfP9h_C1UNrphRTHg-1sA-PxCeflW2BjTz5SQpouwC1sWrmftAVAsCVbdNN5OoahTYLjyZ0xsUAr8HbmhKEbHZiH0ot5eFGCEKdxS7tdGPb_3I-xy3tg502uNuW5IZ2uOkZ2wdpXOcz_D2m_Hla8VJ9RWokfwV9FTw6_xOrLJetlffnbwJ3e1E4gHGm5GTSVZ3UsiOdZjlKJHEts7S5xD0mU__yk6ymvBS_PP-wiso8p5B_qQ7NJlSTfzf3zaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکونومیست: نزدیکی ایران و آمریکا به توافق؛ توافقی موقت برای خرید زمان، نه پایان قطعی درگیری‌ها
🔴
ایران و ایالات متحده به یک توافق نزدیک‌تر شده‌اند، اما این تفاهم از جنس توافق‌های پایان‌دهنده به جنگ—آن‌طور که دونالد ترامپ ادعا می‌کند—نخواهد بود. این توافق در بهترین حالت، صرفاً زمان بیشتری را برای پیشبرد مذاکرات بعدی و به مراتب پیچیده‌تر خریداری می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/alonews/122637" target="_blank">📅 21:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
بنیامین نتانیاهو: «ما در جنگ با حزب‌الله هستیم و حملات علیه آن را تشدید و قوی‌تر خواهیم کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/alonews/122636" target="_blank">📅 21:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CWlPpYVhrUvV8Og7dKf7alJ_v10658EpbqtD9GcZ0OzGbZ-XI_z6VwBrkjI4tWI98aVfGTXJVfwKt9aaaJ9s04S7HPEigM-iF-wf5xaqk4jeMz17h56YzI7KvNk58xWUAeurLJfI5U9Ahbl8KPc0CoFdj_Fc2gs_8KSfuDsaZIthqI3ZSdoQ28XOAiiqVGkllQ8M0jG1fcaodwLZ4c3GXke_OIJ0BRnqQIJlG_D8PrQa2mY0tozKa26rKdYApgzmTkj1DjIi56LHkdxJp3MBY6flsx-7YVXQlGT6lhSVyzpZfKaljRDg7_eSwLortCIEj2HF5pDqu3aSgs_niFMfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت آمیت سگال، خبرنگار شبکه 12 اسرائیل از اختلافات ایران و آمریکا در مذاکرات:
🔴
ایران در حال حاضر فقط حاضر است به عدم توسعه سلاح‌های هسته‌ای متعهد شود، در حالی که ایالات متحده چندین گزینه برای ذخایر اورانیوم غنی‌شده ایران پیشنهاد می‌دهد، از جمله فروش آن به ایالات متحده، انتقال آن به یک کشور ثالث یا رقیق‌سازی مواد.
🔴
اختلافات همچنین بر سر تنگه هرمز باقی مانده است، ایران بر مدیریت بر این آبراه اصرار دارد در حالی که ایالات متحده خواستار کشتیرانی آزاد و بدون محدودیت است.
🔴
هنوز هیچ توافقی در مورد دارایی‌های مسدود شده ایران حاصل نشده است، اگرچه قطر پیشنهاد داده است که ۱۲ میلیارد دلار وام بشردوستانه به ایران بدهد.
🔴
لبنان نیز به عنوان بخشی از چارچوب توافق گسترده‌تر مورد بحث گنجانده شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/122635" target="_blank">📅 21:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RggUmjE27uTwYzu9Y5YAfJ8qQWEH27rrs7RLPbeUimxIOGCiNXiptxdZ4yoLP3F4Iffw8v7RyVdO2RSAVNIgTixhCjsXrKN5AeHx-ECkMfh4EdoeESPoo-Skk8y_36u82VaUhBDfou9w-peh_xieGZxxXt5KpklliPbHcodrwXT_dkRNTVQRK7n0L-eju8Ff9mQcaHPoqZpqI9zAprVDhcfSdZ8s23JOUSd_pMoRaNRIFAyS4HRpoor6YfR4TtCXgDwN6jH3aoXJHX7JoKhe5yqDVUPSNS1aAa9diycMj0ZJZd_jd8ZC5wDoGsGt7aTOws5_o6VB13rMNJktHFjW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی، از رهبران بولشویک‌ها:
پزشکیان خودشم میدونه نمیتونه اینترنت رو وصل کنه. این خبرای جدید بازی رسانه‌ایه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/alonews/122634" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/122633" target="_blank">📅 21:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-uOsa1z8bYvoSKoSG2h9SNwEcwsxYeYdRx3qOwoxCKyf5lcYEtWBBk_L-MnzJvULCPsw23JJ7-fILXYngfF9rkHnTK8GUTE7WutBxA9wQGafIxuUqQPpWKP-WFAnXhw5mDYrh4YqQFf4ksG3uZSn7RJ9Oc5dKvyKiBstsoXV4PyO8A7YPdU1D2jPJB5txpPwy0n7zxMHj4wCSjsvOjsO5h6C3ioJjerXOjYG-_CVtpMMbMjIAz6mNio4sCxDX14CWz5E9dE71SbRENM-n4LDg3vLA2W8vmH9WTpRxA-Na1IteYLU9ooO5dcqkoRRtsWmp05OjxqYEcGss9A53GMHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به اکسیوس گفت: دولت ترامپ از تشدید اقدام نظامی اسرائیل در لبنان حمایت خواهد کرد
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122632" target="_blank">📅 21:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
اسرائیل آماده حمله گسترده به لبنان است
🔴
کانال ۱۴ اسرائیل: نتانیاهو و کاتز (وزیر جنگ) درباره گسترش چشمگیر عملیات در لبنان و تصویب هدف قرار دادن ساختمان‌ها گفت‌وگو کردند.
🔴
کانال ۱۳ تلویزیون اسرائیل: اسرائیل در حال مذاکره با ایالات متحده در مورد گسترش عملیات نظامی در لبنان است.
🔴
خبرگزاری رسمی اسرائیل هم گزارش داد که ارتش طرح حمله آتشین قدرتمندی را علیه لبنان آماده کرده و منتظر تایید سیاسی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/122631" target="_blank">📅 21:08 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caYBfFJHH4TVBJU2dWKtlOVAM-v6KIwboCpX1OHfkfF4h9WxFioVmGHpkz4f6IfEaElbWEbwMsHhRSnlnnpLvHTGUlo1xx2c2BNyK-YtdBYCG12TnSVNpiKvo0ur-lc28i8oGGrDU4OJGt4DY5JV5FsIOtVLyyV5TxnYrE3jHPKBoWKwkvJbWMzl-cLlD3m9miKyzyIPlgde1TF4s1zfjhqIqS9r45MOvZW55Mg3JSStSCfw59RM4sLP0GtdiUQm_H3nDnIxcyioiHJ_NIViMFa9ukhgRAoxjiXYguk4hBBzo0j0GC3PU4DVv8_MvFsimydhfjsjFRVn3KCuoiJGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اشتراک v2ray
🗯
گیگی
120,000
تومان
🔗
لینک ساب برا چک کردن مصرف و حجمتون
🔥
سرعت و کیفیت بالا
✅
پشتیبانی دائم
📱
جهت خرید :
@v2safeBot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122630" target="_blank">📅 21:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122628">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
قیمت نفت امریکا برای اولین بار از ۷ می به زیر ۹۰ دلار در هر بشکه سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/alonews/122628" target="_blank">📅 20:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122627">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فووووووووووری/فارس: اینترنت باید با دستور شعام باز بشه و فعلا خبری نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122627" target="_blank">📅 20:56 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122626">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
مدیر روابط‌عمومی وزارت قطع ارتباطات خبر داد: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/122626" target="_blank">📅 20:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122625">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb1084d3e.mp4?token=jAXE9ViHV5neLZCcjHFtAZICKjJ_UHwRRENTFzpZPzgPfcUafMR9KDYrUpZVf0hZgh2WNLaJu3OLc9fGs0I1qd39XszUoeoztpfeU08HvmrNHguyeVWW6dQq_WedeM9FX4Dr3ktdyp130kCCfFICkqhks8xKpYQQTwdb1WTCxm0VuQt1v2ETtSuaci6pwM5E9Dbsnjp7HyQXz6b5gqrLHFI4T0CKOtG-gwIjXv6Bn-WUVkDzVYP-3O0DH1Oi5d45LDDD6Vf6bcP6iT0pM8WL7NQ-J4x5RPNwuPSoWNWK-eMTR6Q4NWnPXOwwU8bk6raeguPdHL_kIq9TbfcmJONFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb1084d3e.mp4?token=jAXE9ViHV5neLZCcjHFtAZICKjJ_UHwRRENTFzpZPzgPfcUafMR9KDYrUpZVf0hZgh2WNLaJu3OLc9fGs0I1qd39XszUoeoztpfeU08HvmrNHguyeVWW6dQq_WedeM9FX4Dr3ktdyp130kCCfFICkqhks8xKpYQQTwdb1WTCxm0VuQt1v2ETtSuaci6pwM5E9Dbsnjp7HyQXz6b5gqrLHFI4T0CKOtG-gwIjXv6Bn-WUVkDzVYP-3O0DH1Oi5d45LDDD6Vf6bcP6iT0pM8WL7NQ-J4x5RPNwuPSoWNWK-eMTR6Q4NWnPXOwwU8bk6raeguPdHL_kIq9TbfcmJONFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ایران هرگز نباید سلاح هسته ای داشته باشه
تو دو درگیری اخیر مجموعاً ۱۳ نفر از نیروهای مسلح رو از دست دادیم
- تو ونزوئلا که یه پیروزی کامل بود هیچ تلفاتی نداشتیم و اونجا رو در یک روز گرفتیم
- اما تو عملیات خشم حماسی ۱۳ نفر جانشون رو از دست دادن
- این افراد فوق‌العاده برای جلوگیری از دسترسی بزرگ‌ترین حامی تروریسم دولتی به سلاح هسته‌ای جان خودشون رو فدا کردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122625" target="_blank">📅 20:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122624">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری/روزنامه هم‌میهن: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122624" target="_blank">📅 20:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122623">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
فوری/روزنامه هم‌میهن: رئیس‌جمهور دستور بازگشایی اینترنت بین‌الملل را ابلاغ کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122623" target="_blank">📅 20:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122622">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رئیس شورای هماهنگی تبلیغات اسلامی: فعلا تصمیم نگرفتیم چه زمانی رهبر سابق رو تشییع کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/alonews/122622" target="_blank">📅 20:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122621">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کانال ۱۲ عبری:
برخلاف ارزیابی‌های قبلی، ایران تولید موشک‌های بالستیک را به سرعت از سر گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122621" target="_blank">📅 20:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122620">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ادعای العربیه:
پیش‌نویس توافق تأکید می‌کند که کاهش تحریم‌های نفت ایران مشروط به اجرای تعهدات آن است.
🔴
پیش‌نویس توافق آمریکا و ایران بر دوره ۳۰ روزه برای بازگشت کشتیرانی در تنگه هرمز تأکید دارد.
🔴
پیش‌نویس توافق آمریکا و ایران بر دوره ۶۰ روزه برای مذاکرات هسته‌ای تأکید دارد.
🔴
توافق بر آزادسازی بخشی از دارایی‌های مسدود شده ایران طبق سازوکاری مشخص تأکید دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122620" target="_blank">📅 20:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122619">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/فارس: باز شدن اینترنت دست شورای عالی امنیت ملی هست و فعلا تصمیمی گرفته نشده و گمانه زنی‌ها الکیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122619" target="_blank">📅 20:22 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122618">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JL1ePzXO0ZTSPPILYeqIHubMqF5E_xX-2cTrWFV3iIhLmDEl_XTdIyEKF3xL8XqqUWPgKAj1hyhj-2B-oM9ouzh9m8cjOtaU54IOU2Z4LdR24NhJHutPpD2ueCcKOn01XYzNnSusb7kuaroMDBUOwW07H9xUEesrIhscqkIEUeoDKLkoHqm5cSXu-oPLXwQ98yZWeQecrm06Jl0k_6hAafqLnkozCqpIbfCc3eDyXy2kif5O4AI7G1EU0Uoo8ihWim6OEc_IiA37IBvv1qSCOw7NIOlXCyHwU60SRcg4huOpmR6ZnlrfhUmM2_Gx_usovV7N8lCFvNVV7xDhLgTCFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه: پیش‌نویس توافق میان آمریکا و ایران، برقراری آتش‌بس جامع در تمامی جبهه‌ها، از جمله لبنان را تضمین می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122618" target="_blank">📅 20:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122617">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
منابع خبری الحدث:
پیش‌نویس توافق آمریکا و ایران بر گشایش تنگه هرمز بدون عوارض و خنثی‌سازی مین‌ها تأکید دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122617" target="_blank">📅 20:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122616">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797c664227.mp4?token=GEcxwRFkTpWXNRRinpv-jmV8as0uI2BDvYROtWsapyq6UUJTZHMOMj1oXctPYvrh4WEhp1uwyLBekQ3Tt2zyGo5LHn72EBanL2lMz7N940YbrRNyJ0mqSwD_VgtOr0PcMZ9g9qd0qd4RpCaKwHJnaLxZwPXyNYCBdEcGSNdUwCP8L4gxAkqXK6CWDLBcbwTICpv4y31fiSVafvCuE1DFlgg1hFJ2gpMGoJFA0fJjYDQXu2lXGLfIdKjAmGmi94YhUZNRgjL7dpzMXMaj7RLaq5_BjfV8uZ6aVLx8U2Ead0NmdiX41JT1gFXWo8Meoc3Vq7LRoFSfSxyfWu-tIKUo1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797c664227.mp4?token=GEcxwRFkTpWXNRRinpv-jmV8as0uI2BDvYROtWsapyq6UUJTZHMOMj1oXctPYvrh4WEhp1uwyLBekQ3Tt2zyGo5LHn72EBanL2lMz7N940YbrRNyJ0mqSwD_VgtOr0PcMZ9g9qd0qd4RpCaKwHJnaLxZwPXyNYCBdEcGSNdUwCP8L4gxAkqXK6CWDLBcbwTICpv4y31fiSVafvCuE1DFlgg1hFJ2gpMGoJFA0fJjYDQXu2lXGLfIdKjAmGmi94YhUZNRgjL7dpzMXMaj7RLaq5_BjfV8uZ6aVLx8U2Ead0NmdiX41JT1gFXWo8Meoc3Vq7LRoFSfSxyfWu-tIKUo1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ به احترام روز یادبود تاج گلی بر سر مقبره سرباز گمنام در گورستان ملی آرلینگتون می گذارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122616" target="_blank">📅 20:14 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122615">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سی ان ان:
مذاکرات به خوبی درحال پیش رفتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122615" target="_blank">📅 20:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122614">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olRvZrJP_QdV_j2yXwjIh9de1mUwca4dRZNkCuDo_qmjGJhkOwOkxIs78s7t6-lWOALvtmPf0LV0CBdtsBy0WiKnNUP8DNqGwhDYEBsQD5EFtQZpEj-8PkCBSliz8910_mlUpw9Cf_y_Jq_SfHTjJm10bEZY1XHj4j60VZKiyNJiTumASomCOV59S0aDmxtyzYemNdWZXTf9CLreJY3UpQ2pL4bP7HKci8GoiJkXkL-9LS1kbznrfNJQPhacLgwkexa_iU7tOGfVcbKEN99mFZMP7izp9sYOXXx_QfMCzB_j1VrkuJht_3KA4r6xrMloWVK5sbyON-roRnO5FYo_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از واسطه‌ها
:
واشنگتن و تهران به مواضع خود در مورد مسائل هسته‌ای و دارایی‌های مسدود شده پایبند هستند..
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122614" target="_blank">📅 19:57 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122613">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
‏سی‌ان‌ان از مسئولان آمریکایی:
اختلافاتی درباره نگارش مربوط به برنامه هسته‌ای ایران و رفع تحریم‌ها مانع از نهایی شدن توافق شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122613" target="_blank">📅 19:50 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل به نقل از یک منبع:
اسرائیل در پی تشدید حملات پهپادی حزب‌الله، در حال بررسی تغییر رویکرد نظامی خود در لبنان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/122612" target="_blank">📅 19:36 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
یک منبع مطلع به i24NEWS: مذاکرات بین ایران و آمریکا پیشرفت دارد اما مشکلاتی وجود دارد، تغییرات و "ارتقاءهایی" که هر طرف در زبان یادداشت درخواست می‌کند.
🔴
هیئت ایرانی که به قطر آمده است، تلاشی برای پر کردن شکاف‌های جدی است - مانند مسئله آزادسازی وجوهی که ایرانی‌ها درخواست می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/alonews/122611" target="_blank">📅 19:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
محمدباقر ذوالقدر، دبیر شورای عالی امنیت ملی: هیچ عقب‌نشینی وجود نخواهد داشت. این موضوع در میدان نظامی، میدان دیپلماتیک و مردم حاضر در خیابان‌ها با مقاومت شجاعانه‌شان که دشمن را ناتوان کرده است، به اثبات رسیده است.
🔴
اکنون بیش از هر زمان دیگری، کشور به وحدت و انسجام نیاز دارد تا آمریکایی‌ها و اسرائیلی ها نیز در این زمینه ناامید شوند. میدان وحدت و انسجام، عرصه‌ای دیگر در مبارزه است.
🔴
تلاش جمعی برای جلوگیری از هرگونه سخنان و اقدامات تفرقه‌انگیز، ایران عزیز را به پیروزی نهایی خواهد رساند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122610" target="_blank">📅 19:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: به نظر می‌رسد گره مذاکرات ایران و آمریکا در مسیر حل شدن قرار دارد و ابتکار قطر برای حل اختلاف میان تهران و واشنگتن نقش اساسی در این روند ایفا کرده است؛ به‌طوری که دوحه عملاً یک میانجی بوده، نه صرفاً کمک‌کننده به روند میانجی‌گری.
‌
🔴
تنها چند ساعت باقی مانده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122609" target="_blank">📅 19:27 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
فایننشال تایمز: دو نفتکش حامل گاز طبیعی مایع (LNG) از تنگه هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/122608" target="_blank">📅 19:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شبکه CNN: توافق احتمالی ترامپ با ایران می‌تواند تقریباً به اندازه تصمیم او برای آغاز جنگ اختلاف‌برانگیز شود
🔴
طرح کلی توافق پیشنهادی، بسیار کمتر از «تسلیم بی‌قید و شرط» است که ترامپ در مارس از ایران مطالبه می‌کرد. برخی از جمهوری‌خواهان می‌ترسند که بالعکس این ترامپ باشد که تسلیم ایران می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/122607" target="_blank">📅 19:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122605">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eVHQ2Fywg1qUbxtHsgpgZh5H89PKpNY69rDEM9mS2QdL6uYc-aagSdt8TOipuwJv5MIpkaO3axDc4guf1SjFx5bDt4GrgnAD5nUp1vPUPY_7GC5qjQYNlbO5coHycKwitw_azdNdwR5K-L2C0db1JX_0SaCLYkvC_SA80WoJdThTNE8Gg3H8xdLhv0PMXBj1wH9t99jfUiQMgsSiJM5QxDaX2Hw76MN_qzQutaHC5Kj1TK_9xhz7l6FAMdqV7oUp2n1CZpHbtYXshYvWTWS8HWHbbtzlYzA-2jTUmDp6A1qpgCPeEbWIh9w7X4N3g3F-eN_iX9ryZqgnhHtz9zzS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/guhP6vwNPSA7ZVaz2p8l7WAwq-Zl2euYjn5JN5zkMsL6kV569tsE_Q7i9DtMaghS5rz9gd_GgUppxGagO0yYN564iFadwDw36gZ6HAjAYkkJN-5j0TLla8RjX9xA5dySCSEpKdM-bRSl0UMvq0meE2GF1h7XLlFRFQcsAYXqEL4H_YqwlsHEiIAELV4PAQd_bZhj8wwMf-MbNQWmVov-QmkrSO5eBkKQ3KJjTfWj4rW0Ls5LO7k5Vd7G5bSPhr7FBxVqCtBLVWXpXq4SP_Ozx9gxvM72_BgKbiWHX6z9gFzWLX7ZnHIVELtkpHoFG7DsGo6pVXf9gqAbG2TTbJg-KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ عکس‌هایی را که به جو بایدن و باراک اوباما درباره ایران تمسخر می‌کند، دوباره منتشر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122605" target="_blank">📅 19:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122604">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5540723a.mp4?token=Oy8L7OfUWfZT2TYreP6nvt2t3WvI6r9_dJkfB3-Uhlq87452Hl2B-9q8NZUsnDv91oRi_TNHb1z8obiYh1Vnga5cBt4DDSMpNHN-UwnrqAgmcvjKhOYf5rtIZ_MYykxH8UnoXGEyt3RmKV1rkbS5ixtvL_fPfGaE8AAtTgtMdLKEgdllbqw__binOY33JQW8bByAI02u4riqPksZRcUBrRl3CG97zwSkO_UaUyUFmxQNt3Ryr27W1plwywKIDHhpsTBioNFc5Ir4RMwnLCQTwuZkQpqcw_tnj29N_cKR1J5Sbc5qe6hXP-o-0zvT8BVKWZu5bwwFp-M7L0bCdWkoCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5540723a.mp4?token=Oy8L7OfUWfZT2TYreP6nvt2t3WvI6r9_dJkfB3-Uhlq87452Hl2B-9q8NZUsnDv91oRi_TNHb1z8obiYh1Vnga5cBt4DDSMpNHN-UwnrqAgmcvjKhOYf5rtIZ_MYykxH8UnoXGEyt3RmKV1rkbS5ixtvL_fPfGaE8AAtTgtMdLKEgdllbqw__binOY33JQW8bByAI02u4riqPksZRcUBrRl3CG97zwSkO_UaUyUFmxQNt3Ryr27W1plwywKIDHhpsTBioNFc5Ir4RMwnLCQTwuZkQpqcw_tnj29N_cKR1J5Sbc5qe6hXP-o-0zvT8BVKWZu5bwwFp-M7L0bCdWkoCzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پاپ لئو چهاردهم : هوش مصنوعی باید خلع سلاح شه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/alonews/122604" target="_blank">📅 19:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122603">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5ZOkqJP8d1QzAULq5uMTZ5Cm5eYCCkyj6cD_QzfflMR0lHtUCQmN0han2ASJ7_Qgnnpc-r2vAI9NDjpeoBiiHo0OEe0s1c3SAuq8xsYWA0ZeCajpFq4kcTvmvVAm3nWFqJYDZxFCSnkVwTSdrqKE09v9nbi4iKfa7WQdCWfVaq7N-N91o7GXkoqAe3RvF3ZHBX1KSMNUqttiALJaov-Jc2syOmRGokrd3qieDLTAa--hjV1XJ2ppEn1ctJWjfavE8wxeK1paSfVhBW4jUf4lAN8nfPRzoV09m7GwxAxOV9mO8Tk8JwczdiVd5Z0icoggrlMadBr3OhLkpIYXex03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / الحدث : منابع نزدیک میگن ایران آماده‌ست اورانیوم با غنای بالا رو از کشور خارج کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/122603" target="_blank">📅 19:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122602">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الحدث به نقل از منابع عالی‌رتبه:
به احتمال زیاد فرمانده ارتش پاکستان به دوحه سفر خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122602" target="_blank">📅 19:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122601">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی در آسمان جنوب لبنان دیوار صوتی را شکستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122601" target="_blank">📅 18:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122600">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF): نیروهای دفاعی اسرائیل آغاز به حمله به سایت‌های زیرساختی حزب‌الله در منطقه صور و مناطق اضافی در جنوب لبنان کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122600" target="_blank">📅 18:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122597">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JM4bzzdlS4m12f0IMJvsAxV7oPQ2Mbj-Uq1n0GMt506yH40bUzu_RmwzbZghLB2f3W2_KYGXf91xW5fb3sN3RW02kTmFffyH4XyQ_Lvx1A_Y3OwOXXGRQL16B6mlE-RjEaNTbyjQXM1H_vgLeNBiMVpK7iTHknNvzZuPp335TbwXi0ujmgbZTsgYsSmP5unvh6Jl1-NfY1kBjCT4gIyp0AEm1Wz-Gr9PoW1-Qk8xRrjIbQsQT-_cqDxJcSlaHiT547aQFnoR73pPhT-kOqJ0aKv9jhLb1reNE1UAHHK7zOYn7u5diMafEGCfGeF0bH2y013KqJMpe9b-UzsuyranIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af0f9ce0e5.mp4?token=ORMEQEG8pykIGGi05teDaZ_SHxsKFFdVJXW8rlh4gwyb13SCCdsMzhGd_nEKKO9HnYppRxQMhBThtxAWTBUfiX-h9XXEQm5Sq2e9rl6xOeKCp7614lAIMbBrwYY5lxTEk9gzfasQcsg8Q-VMvidjs6K38h0Gvs2bCfzOSZJpIhSDCFJQi47tlnDm6BV3PYPRb8GQaosB0Oi_DL9kDa2wk2oJji0xRQKQrwXkjh_qpTTh9ZqXSdaihfFpYt2hqV5-pxeNvpHRmGyKPdoz0SPM6bRbeucs7B7alr_5_1e75xllKgLZRw8zZscm7cBHzfc7GRLTAxN3525DYDTMRTMy-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af0f9ce0e5.mp4?token=ORMEQEG8pykIGGi05teDaZ_SHxsKFFdVJXW8rlh4gwyb13SCCdsMzhGd_nEKKO9HnYppRxQMhBThtxAWTBUfiX-h9XXEQm5Sq2e9rl6xOeKCp7614lAIMbBrwYY5lxTEk9gzfasQcsg8Q-VMvidjs6K38h0Gvs2bCfzOSZJpIhSDCFJQi47tlnDm6BV3PYPRb8GQaosB0Oi_DL9kDa2wk2oJji0xRQKQrwXkjh_qpTTh9ZqXSdaihfFpYt2hqV5-pxeNvpHRmGyKPdoz0SPM6bRbeucs7B7alr_5_1e75xllKgLZRw8zZscm7cBHzfc7GRLTAxN3525DYDTMRTMy-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از حملات اسرائیل به صور در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/alonews/122597" target="_blank">📅 18:33 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122596">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSfA5MBVxIoKI4FHtJHmXsny6bez-TBZVPoQ20hZfeb4QGSX_05gL1DxmZophtvs5RXCqItl6jYkE16bBfO6yh4xjx7mWgqzcqu91CZT2qiy8c1rKYuRw4_aYR8dMc7j4nDuiq1dQuLehXKV2VaRbwS6NXCn03A3yHrKjzHWG7mofEzSFShumEIqTEpl2Bvl06D6x59jM25x5zCSn8RjHJ7uTKWWV6MN5Kvs4GxQI29Zsk4yC6YDAdenl3PKuLbmGWezK_-cAnvBEwcLU84A7zZKqA8VgBHR0At1piDlbF4KlyWZucmATbW_OTFDiwJO6fNJBZkFjh7uQ_9pp_x2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال تلگرامی Fighterbomber که وابسته به نیروهای هوافضای روسیه است، قول می‌دهد که روسیه «کی‌یف را تمام خواهد کرد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122596" target="_blank">📅 18:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122595">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
یک منبع سعودی به سی‌ان‌ان گفت که عربستان سعودی تنها زمانی روابط خود را با اسرائیل عادی خواهد کرد که «مسیر غیرقابل بازگشتی» به سوی تشکیل دولت فلسطین وجود داشته باشد و تأکید کرد که موضع ریاض «همانند همیشه» باقی می‌ماند، با وجود پیشنهاد ترامپ درباره به رسمیت شناختن منطقه‌ای اسرائیل پس از احتمال توافق با ایران.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/122595" target="_blank">📅 18:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122594">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
الجزیره: هیئت ایرانی در قطر برای گفتگو درباره «حساس‌ترین مسائل حل نشده»
🔴
مذاکره‌کنندگان ارشد ایران در حال سفر به قطر هستند؛ کشوری که نقشی محوری‌تر در گفتگوهای ایران و آمریکا ایفا می‌کند.
🔴
عباس عراقچی، وزیر امور خارجه و محمدباقر قالیباف، رئیس مجلس، در حال گفتگو درباره حساس‌ترین مسائل حل‌نشده برای دستیابی به یک تفاهمنامه هستند.
🔴
رئیس کل بانک مرکزی نیز در این هیئت حضور دارد که نشان می‌دهد تحرکی در جریان است و بحث‌هایی درباره رفع انسداد دارایی‌ها (که یکی از خواسته‌های اصلی ایران است) صورت می‌گیرد.
🔴
منابعی به الجزیره گفته‌اند که بحث درباره سایر موضوعات از جمله ذخایر اورانیوم با غنای بالا باید به زمان دیگری موکول شود و تمرکز فعلی بر گام‌های اعتمادساز است.
🔴
نقطه اختلاف دیگر، تنگه هرمز است. اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، پیشتر گفته بود که این موضوع بین ایران و عمان است و تهران خدمات امنیتی برای کشتیهای عبوری از این تنگه را ارائه میدهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/122594" target="_blank">📅 18:25 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122593">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) : پس از به صدا درآمدن آژیرهای خطر در ساعت ۱۶:۰۳ مبنی بر نفوذ هواپیمای متخاصم به چندین منطقه در شمال اسرائیل، یک پهپاد انفجاری که توسط حزب‌الله شلیک شده بود، در خاک اسرائیل، نزدیک مرز اسرائیل و لبنان سقوط کرد. هیچ تلفاتی گزارش نشده است.
🔴
علاوه بر این، اندکی پیش، نیروی هوایی اسرائیل یک موشک شلیک شده توسط حزب‌الله به سمت خاک اسرائیل را رهگیری کرد.
🔴
در حادثه‌ای دیگر، اندکی پیش، یک پهپاد انفجاری در خاک اسرائیل، نزدیک مرز اسرائیل و لبنان سقوط کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122593" target="_blank">📅 18:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122592">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2ONgmIpeCDLiC7RPig-KXQKCuCfUIKEAhAt9lHz1gHVsASlDK5v6AulD9OoLEn1ihULzK8DJOuxgzOAB9n3naYJ-Rn-5FkNmG82ldT0N1vs6jDd63Vk3X4z-eTwpzr18JAtwagbiIEcqB8DUbKezpb_sB7_Mi8lkGfQ780YBLOUFXZRS41Bj0HrrNP51edK0rKgYIYkqa6a-eAMb3PVlljGj3qaznAHX0zKEarf7RHOjuQznPDC0DtFhN2O_jxjJul-gjpIkgVAh6CJNEp_YuIzZeiCq0HXPuMWaY6vBTc2R3ua-9ofwzCosnNIm57C4-D5G23qePsGpzDwL7ShXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سناتور جمهوری‌خواه لیندسی گراهام:
پیشنهاد اخیر رئیس‌جمهور ترامپ که گسترش توافقنامه‌های ابراهیم را به عنوان بخشی از یک توافق مذاکره‌شده در مورد مناقشه ایران الزامی می‌کند، به سادگی درخشان است و منجر به مهم‌ترین تغییر در خاورمیانه در هزاران سال خواهد شد.
🔴
با صلح عربستان سعودی و دیگر کشورهایی مانند پاکستان با اسرائیل، منطقه شاهد سطحی از ثبات خواهد بود که پیش از رئیس‌جمهور ترامپ هرگز تصور نمی‌شد و در نهایت به یکپارچگی منطقه‌ای منجر خواهد شد که خاورمیانه را به یک قدرت اقتصادی و منبع فرصت‌های خوب تبدیل می‌کند، به جای اینکه یک انبار باروت باشد.
🔴
انتظار دارم متحدان عرب ما این را بپذیرند، همچنین دوستان ما در اسرائیل، با تمرکز بر این وظیفه، زیرا شکست گزینه‌ای نیست - که تحلیلی درست خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122592" target="_blank">📅 18:17 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122591">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqy_PCL8Uo8P9eIpflUqzMaHX-0_7lv5-1UFnKiQageARX5wnuL-pazsqy_0B2ho81RhQX1pqewE-c7doKRggzOeqFMJxfrblwkf8DGj5wqBFXmZaQALGS9lSwX3BDNnOaIMlwxa_yGFe5In-ZGKzGTOHdTwsBC0MBW14AGuBHgHMzoKOLX7e-9GPE0q9CsWp7VVz3BSh5CVDVJr8X1igXF5XXkzW35ZMtHkQXTtcF4kGC9eHfnFEFVgQFmb6OXRcDzT9L8-UWkZO1XUSNE0uC9BT-2ubzvyH2MnGNLRFQcvxs1fS5xMFD22k97Qh0fDkNa0K8F8MGttBy75H_iFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش مکو اسرائیل، ایران در طول آتش‌بس، بازسازی بخش‌هایی از صنعت موشکی و پهپادی خود را سریع‌تر از حد انتظار از سر گرفته است.
🔴
بر اساس برآوردهای اسرائیل، ایران در حال بازسازی موشک‌ها، پرتابگرها، پهپادها و سامانه‌های دفاع هوایی در تأسیسات زیرزمینی موقت با استفاده از قطعات باقی‌مانده، حمایت روسیه و قطعات قاچاق شده چینی است.
🔴
مقامات دفاعی اسرائیل معتقدند ایران می‌تواند تولید پهپاد را ظرف چند ماه از سر بگیرد و تولید موشک را ظرف یک سال به طور قابل توجهی گسترش دهد.
🔴
فرمانده سنتکام، دریاسالار برد کوپر، شهادت داد که ۹۰٪ از پایه صنعتی دفاعی ایران نابود شده است، اما اطلاعات به‌روزشده نشان می‌دهد حدود دو سوم پرتابگرهای موشکی ایران سالم مانده و از تونل‌های زیرزمینی مجدداً مستقر شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122591" target="_blank">📅 18:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122590">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
قیمت جدید لبنیات:
🔴
شیر نایلونی: ۸۴ هزار تومان
🔴
شیر بطری: ۹۸ هزار تومان
🔴
پنیر یواف ۴۰۰ گرمی: ۲۰۳ هزار تومان
🔴
ماست دبه‌ای ۲ کیلویی: ۲۲۸ هزار و ۷۰۰ تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122590" target="_blank">📅 18:05 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122589">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5HxAD9Vljk8Ncus3pwsriU28g91UH6o0ooQgAvvQj09fF2YBLkLKnHJAJxYU_xW0TSn42IooLoTfZR7GmTyejfme2YTu4UxpHRb8c4gCWSerIC-UhgHV4N0hC4YTiXLBmEbQA0YYnxIsL7ftJUzdqcWPQdoIIhCOStlHPjxhRFjr0GnuwKIwB_M9CVQsr9pFVW1OJ6K8GqiPUx7eGKv_4BNCFLW_sLmaqYVdeKEh2-RwWlhduoAprhLHGwln7yRzEf12XSLjNQmJNUqtaKN7FoRTDvzlclOJl2a0yLxfEVWTJcjTXoYnSgvr0IsCAJjKz9ECrWB1UtGoGoKxG8ESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال: مذاکرات ایران رو بحث برنامه هسته‌ای و رفع تحریم‌ها به بن بست رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122589" target="_blank">📅 17:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122588">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
المیادین: هیئت ایرانی به ریاست قالیباف امشب به تهران باز می‌گردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122588" target="_blank">📅 17:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122584">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d7c408a3d.mp4?token=mIGe2bDkW1541Xai9-GOfn36LAHO7coMvmuI5VMlFnbJ0MAoiFZMdHLOMVePOS-fvm_VlTt_syF0wKiqvmfPmOQHAOrUP1m0qaPDbOrgm3D1zhywGhSRQ3MvzGNshbgnVVS8ElwU6WDr5vxRbUHU97KRGhg9Hl803Ia9zMffs26bBZmug1a1vtXNYbt8EjbIkQij7jGejHuoR3rZl268t8fRQixZgEfWwQ85Ta8RuqGVKT-sqV118xj-Cp4Kns85gXnl8fpVFLj2o_LfZ2J6x14YW7zucZasimT6h2BQ0YP7fBKK5j5tbqz8Wll8FM-4lc8smczZ-_Jyhx9ZOIrYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d7c408a3d.mp4?token=mIGe2bDkW1541Xai9-GOfn36LAHO7coMvmuI5VMlFnbJ0MAoiFZMdHLOMVePOS-fvm_VlTt_syF0wKiqvmfPmOQHAOrUP1m0qaPDbOrgm3D1zhywGhSRQ3MvzGNshbgnVVS8ElwU6WDr5vxRbUHU97KRGhg9Hl803Ia9zMffs26bBZmug1a1vtXNYbt8EjbIkQij7jGejHuoR3rZl268t8fRQixZgEfWwQ85Ta8RuqGVKT-sqV118xj-Cp4Kns85gXnl8fpVFLj2o_LfZ2J6x14YW7zucZasimT6h2BQ0YP7fBKK5j5tbqz8Wll8FM-4lc8smczZ-_Jyhx9ZOIrYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز - حمله‌های شدیدِ ارتش اسرائیل به جنوب لبنان انجام شد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/122584" target="_blank">📅 17:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122583">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
رویترز همچنین گزارش می‌دهد که بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در گفتگوهای خصوصی با نزدیکان خود گفته است که اسرائیل توانایی کمی برای تأثیرگذاری بر تصمیم‌گیری‌های رئیس‌جمهور ترامپ در مورد ایران دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/alonews/122583" target="_blank">📅 17:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122582">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf973f0a89.mp4?token=BwFcwwpmTsCHWUHMn5mFP6-LmJR3x8PHGDYhBn5LxkPIPi8rhIZ0Sh7BAuwtG8PGL0kBGiY92BpXlnaX-_qWdDg52bUazFo091Lr2Bh_MW_ZhlQ8KkM0gatTJDqA7r_CQyH9KCzbajQpk4LonF7nmTXIu-KC5mzZixkFGnO7ppUSvP3-z1nefxqhRPapLbaFy6HLmrW4GcnmE8fc67mYQw0P3JTBIlvJydJF1z5mp0tZ4YWnMTEsfVRsElgJILmWZ8SEbU9YIrLZ_mHJjuhBiAjsmM8r0zlGu9uWq_Ri4zUnt4I1-FmmU7Xphd_OyQULBdIj4D5wb3ka8fsz4Bm1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf973f0a89.mp4?token=BwFcwwpmTsCHWUHMn5mFP6-LmJR3x8PHGDYhBn5LxkPIPi8rhIZ0Sh7BAuwtG8PGL0kBGiY92BpXlnaX-_qWdDg52bUazFo091Lr2Bh_MW_ZhlQ8KkM0gatTJDqA7r_CQyH9KCzbajQpk4LonF7nmTXIu-KC5mzZixkFGnO7ppUSvP3-z1nefxqhRPapLbaFy6HLmrW4GcnmE8fc67mYQw0P3JTBIlvJydJF1z5mp0tZ4YWnMTEsfVRsElgJILmWZ8SEbU9YIrLZ_mHJjuhBiAjsmM8r0zlGu9uWq_Ri4zUnt4I1-FmmU7Xphd_OyQULBdIj4D5wb3ka8fsz4Bm1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیماهای باری نظامی آمریکایی در راه غرب آسیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/122582" target="_blank">📅 17:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عاصم منیر، فرمانده ارتش پاکستان، روز دوشنبه به وانگ یی، وزیر امور خارجه چین گفت که توافقی بین آمریکا و ایران در مورد تنش‌های جاری نزدیک به حصول است.
🔴
در دیدارشان در پکن، منیر آخرین تحولات را به وانگ گزارش داد.
🔴
منیر گفت که پاکستان حاضر است به تمام تلاش خود ادامه دهد و امیدوار است که چین نیز به ایفای نقش خود در این روند ادامه دهد.
🔴
وانگ یی با اشاره به اینکه پاکستان میانجی‌گری واجد شرایط و مورد اعتماد همه طرف‌ها است، گفت که چین از تلاش‌های این کشور قدردانی کرده و از آنها حمایت می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122581" target="_blank">📅 17:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122580">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbBG7Cx9eoeXZcSM0POQbFRRzPZ6vlCnzW-bew0ooY5f-iwiOSZjQ7CtjciMJdTgZX68Mb94plKiRZPdyz2cs6_dAHMYBZBdWHxF5nqS5NofVtPZJho9LUcWdZZAMjBQIWTiJSh0qjwjfCVmlWSvDvwnlXd2VvCcsz48u8s1-44eoT-0kYPL6To3rodT_i1g8wnfMlBA-C7Iy-EHU2JEeBvD_yGK13jftW3-LjIg-ABVnZdN_O1hvmkih9CYcjbriqbIkaRN5epdFZitOc-jLE9F5KKUvnBxOkzg8XQJw9oYB2PWnZxLC4dr7-zCJkA8qdWYGjJxh6VRkQswtIu1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل هشدار تخلیه برای دو ساختمان در منطقه عباسیه صور، جنوب لبنان صادر کرده و ادعا می‌کند که این‌ها «تاسیسات وابسته به حزب‌الله» هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/122580" target="_blank">📅 17:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر نفت: باید عرضه بنزین کشور را بطور خاص مدیریت کنیم و در تلاشیم تا تاسیسات آسیب‌دیده به سرعت به مدار تولید بازگردد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122579" target="_blank">📅 17:28 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122578">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل لحظاتی پیش موجی از حملات هوایی شدیدی را در نبطیه در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122578" target="_blank">📅 17:24 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
فوری / هشدار  روسیه: اتباع خارجی خاک کی‌یف را ترک کنند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122577" target="_blank">📅 17:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122576">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پزشکیان: ما آماده‌ایم به دنیا این اطمینان را بدهیم که بدنبال سلاح هسته‌ای و ناآرامی در منطقه نیستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/122576" target="_blank">📅 17:21 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122575">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAumzpED9sAsge1uIwy55Jw19m-bpZRSF0M2MYk1u6cYZqPgB_Cpkm45ezEVr6g-um8NTxGl3cq5jnHHwRWQTRIjxsfUSCTmTLBDNPVY5Q1jvmSDjvCIhXeITrgVb7bepXKjdyw9zy5IA96sdgCYzBG7S073JDKtlXmPtLFx7bz6_831qIwTWDUknQqnFVI2XxwHAKuuyj7zx-IHWluSyCr252M0CHqQOzM3r2j3uGa_wiFdJCrwqq8Kz_W8O6qoHNjAW7gWG_k-pGAk1wkb4-kwrb2zs1ifTfDLxDnNrkrsTgAX-wN_D50DSj6aEElNjVBKC8C6bCAHuAqQ2nQN3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
امروز فقط با گیگی
159
تومن کانفیگ اختصاصی خودت رو بخر
❤️
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
🤩
ساب
✅
ضریب
❌
ضمانت بازگشت وجه
✅
پشتیبانی مادام
✅
پس دیگه معطل هیچی نباش و بدون واسطه خرید کن
😁
خرید مستقیم از ربات:
@manageuser_robot
پرداخت ریالی فعال هست
‼️
پشتیبانی درصورت بروز هرگونه مشکل:
@Niiiiiimaaaaa
عضو کانال بشید کد تخفیف ده درصدی هم بردارید
😁
✈️
https://t.me/+iDE5AfsFulQ1YTg0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122575" target="_blank">📅 17:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPTjQyUNhufZS2t2irBSdoEUgq5nV-M10jp-S4ziKYU27-PIYoPhBirNDHBmYqsj6tiLPaB8KhQ1_qWJASJ8Ug-wK80sGj2wLR6d1OhnhT8BbW7sLZgoFRElZl9x9NqrWjeug1GzTUczTtwSrPDbggBGXy8OKelSI9YcUKuHcpRpZqu8TpzlCBkwWzKWizQWjH-57bZ_Yc9YGkWxFvHE4pL3a58qgok3y_PsGR71709dVl_Cns-X-NTY07iVSj_utOhbQp-OVx2BJEq_uoaG0RLp9bZRTTXo13ms4eSiTEmlrBrRvjrAYNScjHu38i_HUxyGuO1K2S0mfP3FRb1TCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو شارل دوگل فرانسه، و یه اسکورتش، ۵۰ مایلی شرق بندر
Salalah
عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/alonews/122574" target="_blank">📅 17:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت خارجه ایران اعلام کرد که جمهوری اسلامی، اسرائیل را «یک موجودیت اشغالگر و غیرقانونی» میداند و هرگز آن را به رسمیت نخواهد شناخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122573" target="_blank">📅 17:03 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122572">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
عصر دوشنبه، صدای فعالیت پدافند در جزیره قشم  از سوی ساکنان محلی گزارش شده است.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها مشخص نیست و هنوز هیچ‌یک از نهادهای رسمی درباره علت وقوع این صداها اظهارنظر نکرده‌اند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122572" target="_blank">📅 16:59 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122571">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeaQRy8ectr8ARHre9BHy5geAXjG3qjxoZ-es5xR7sNjE3e1XqPU1YzODG_nTqHak14D06PKAvmX9N_cCIPiSreJgMycbsGAj1Nf0O9L0vbxhNqR7zuYyikkUFZ5swqFM3_Thz3DrNxX48m4nac_TVsSmNI47PFY7UjsH14VAI0iipbw7XvojyoIErcwWPyze1dSn6mjiuRhaQFBXiC8b5MA7LhALak485-INM6QjcHEDAS0AaBN6r3ua-hT7upO79Kt_K-fm-lfTqzbXNROHHnTydP2cIQqh9iR_25fuT1S3ctD-ARdbM7adDixkRsLwUnxegC80DQMLV2Sx8HPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز /  انتخابات هیئت‌رئیسۀ مجلس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122571" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122570">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNqOo_YmPpqVeQp3_jxaaXqdbZ-heP79VAw8D6ryldnk01bLUeO3SIZ-vU52ykWVvdK3t9RRkmEAx9E1D5WaC07pjf4wFBE8d96LrLEWCxpfKD0WgzzQEcAWMWrfjO5bIKEVIt5pNCK7nCsI8Oa39Q3QFzOPx2mUdi2uENipAW3aq5BijdtIXnfIkoVqCkdeA8Xrc8ZKwRSz4Gyk0VQOdiHcltkaonTwWoLF-Gt6ESLw177zMqnC6U3Y7LF3p4OOQaWb9gLjVqc3YoBS5Me5sV3HX-wAMhXN9oh6nePmrGYQR8Ywa5ELzvcq7Tgl9ayccgbH8Y8TFz53vKZ28cWwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دمای هوای تهران برای جمعه به ۴۰ درجه خواهد رسید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/alonews/122570" target="_blank">📅 16:46 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122569">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نماینده حزب‌الله: لبنان بخشی از هرگونه توافق احتمالی بین ایران و آمریکاست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122569" target="_blank">📅 16:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122568">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
به گفته شمس الواعظین عضو شورای اطلاع‌رسانی دولت، اختلاف در رقم و زمان آزادی اموال بلوکه‌شده ایران وجود دارد که با حل آن، امشب یا فردا شب تحول امیدوارکننده رخ می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/alonews/122568" target="_blank">📅 16:41 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122566">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JS64sYOHn23Hqxr5RGDCV4b2BUEpuco75UxLAwgJzuEHdQYWjOsKMSwKErbdEgeksmt0o9zv7yo9ozUtcfqI6y4hAjEYyeblUsV73kznZjTKvpEhLXOpdIRXhDxGkkxgAHeJnxWymX8-WpAUcVF3JKrOACNumBqt8gRApVzzg2zaclC6VtYUGKmgTLsgN0J2NBVRa3XpNJDMBzPhJzU2YPKCv2a9qNXCvkhTXnJmPx3uHuav4n2L1Xvmb804VavC6k7D3dclxZwzXsS_IMhtCj5cpaA5h0yO1GCNqnxfydvpSsCDSGoeWa0No6Ry7ykCAsRqClBskdOGvecPdxbJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qOQtyR91Zs7EU14da7NTThDW7-kNcceLKOL-3aNEuhKqqxMg8TNO6KkRxFFLd-rxtcViMZZkLbOSY_e7Mvq8vowdE3t2VUHGht5_XLbXVkM5VYKJ1RYyNNPDY1KFmTjV-iZTGATCt-ZP-N8FvWPUXjPChsK4_ipPHEwM6qtZ_LUDyzNOZrDyU7-Taqzs6t4_3ooBKmxAogUeO8vBlzKB9I66ii_l48b-rrXctIQfv0IyhIhC0dYYIaOEFJ5ISsBlEockUXxDjHUdXWPuO5ZyNQi_TwkK6n_dgjBe3nRiurfGPWIArT83E9A7OLDGRWXSsz3ea1ywSaRQa-nH9VFDow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شهر سلطانیه در جنوب لبنان پس از حملات هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122566" target="_blank">📅 16:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122565">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
عصر دوشنبه، صدای فعالیت پدافند در جزیره قشم  از سوی ساکنان محلی گزارش شده است.
🔴
بر اساس این گزارش، هنوز ماهیت این صداها مشخص نیست و هنوز هیچ‌یک از نهادهای رسمی درباره علت وقوع این صداها اظهارنظر نکرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122565" target="_blank">📅 16:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122564">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk5FNd5tNqWQjKRudNYKnXP9KpLe2YBy5GwfkC8ixyU7bJNSN-92HyATOGloU6DQerGaPj9W6D7RvrJvUp3aN14Dwu4mV1spwMC5HgGD2nTukPfX3AeB5nQ8w7JvD8Zd5BjdIUGV8JKxGALiIG0Bt8HPD5rWNk2HzaF8yljBuVMloHdIRZ4O94y4afTztLXZ3pEkTCXd78FqyEC-Vn6CQeezfQWUXYekfodoPzg0YRtirU7PMUN3YTB2kpiS8hY-xaqnvuvMj0uHJWHvnoEpIlyx-tcSEmcCi-WQOpPJY8PWxrB-yJnL64dx1zDvEZbm-m2r00KVMRgC5b_4-QnEbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست:  ترامپ از تأثیرگذاران راست‌گرا و چهره‌های رسانه‌ای مرتبط با اردوگاه MAGA برای توضیح کلیات توافق با تهران و جلوگیری از شورش سیاسی در پایه محافظه‌کار رئیس‌جمهور استفاده می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122564" target="_blank">📅 16:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122563">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpFhEhsSoVowVBacyYK1WAHQGstUAm8yuwyB-5NxYwMN-QAyfB0Z0xMb5ck_iP7QpbJbFQai54OZNvhmIoJ9uf3PVbyRaeI-imIfQPXj9oGczakSwst1VTiHaww2879FPi_FBZWNjceQLV6hGsErfmKn_5QYKk0Y1NrYTI5zw_riL9xgxPGQ50kxJ6DGGB_D2rOWamG_AAbWKc8ib0Q-EZvmB9-72XgwU00gKkGOPhGqeZG6829BdLYoyMTqEGTzDt5H6vWDKWca3f1OoqXMC_OfBYxpvqgtRdIff1msydutPGG_GjJxmNLXsO676cyBkn4DHqtXJ2wYUpXSTQDHng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : مذاکرات با جمهوری اسلامی ایران به خوبی در حال پیشرفت است!
🔴
این فقط یک توافق بزرگ برای همه خواهد بود یا اصلاً توافقی نخواهد بود — بازگشت به جبهه نبرد و تیراندازی، اما بزرگ‌تر و قوی‌تر از هر زمان قبل — و هیچ‌کس آن را نمی‌خواهد!
🔴
من اعلام کردم که پس از تمام کارهایی که ایالات متحده انجام داده تا سعی کند این پازل بسیار پیچیده را کنار هم بچیند، باید الزامی باشد که تمام این کشورها، حداقل، همزمان به توافق‌نامه‌های ابراهیم بپیوندند.
🔴
ممکن است یکی یا دو کشور دلیل داشته باشند که این کار را نکنند و این پذیرفته خواهد شد، اما اکثریت باید آماده، مایل و قادر باشند که این تسویه حساب با ایران را به رویدادی بسیار تاریخی‌تر تبدیل کنند تا آن چیزی که در غیر این صورت خواهد بود.
🔴
در صحبت با بسیاری از رهبران بزرگ ذکر شده در بالا، آن‌ها افتخار خواهند کرد، به محض اینکه سند ما امضا شود، که جمهوری اسلامی ایران به عنوان بخشی از توافق‌نامه‌های ابراهیم حضور داشته باشد. وای، این واقعاً چیزی خاص خواهد بود!
🔴
من به صورت الزامی درخواست می‌کنم که تمام کشورها فوراً توافق‌نامه‌های ابراهیم را امضا کنند و اگر ایران توافق‌نامه خود را با من، به عنوان رئیس‌جمهور ایالات متحده آمریکا، امضا کند، افتخاری خواهد بود که آن‌ها نیز بخشی از این ائتلاف بی‌نظیر جهانی باشند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/alonews/122563" target="_blank">📅 16:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122562">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e73ffdc524.mp4?token=PV4ReXSdx-p6JibcH43M8VeAX6J5vCBNDy5KayoS_DROCEZWY-0tjITfo1mY0CDqfeLsn8NOvw69UHpzoQHUn5lVyq6priSHTJSArvWO9WiLxA1-beD_brELrJRgy9umtWNAIZ8CPM7rTCJCfzNPzDgzOw6BckptP-A68R61aIvGn43lmMXnNTtw1TjH84cob0g8nhdVqUVFCgTgOwLduQT_Udb5FtxKf4LTehBAZA28A1t7SgZlYn6OSQZilktOkf6vy07YtsE7GFSei8szAiEQhTQzqp5BXowQ1_Z_-c5TOKVHzax6XpNNCfdQZ07fE92NSirlgB4acVnUiHWpbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e73ffdc524.mp4?token=PV4ReXSdx-p6JibcH43M8VeAX6J5vCBNDy5KayoS_DROCEZWY-0tjITfo1mY0CDqfeLsn8NOvw69UHpzoQHUn5lVyq6priSHTJSArvWO9WiLxA1-beD_brELrJRgy9umtWNAIZ8CPM7rTCJCfzNPzDgzOw6BckptP-A68R61aIvGn43lmMXnNTtw1TjH84cob0g8nhdVqUVFCgTgOwLduQT_Udb5FtxKf4LTehBAZA28A1t7SgZlYn6OSQZilktOkf6vy07YtsE7GFSei8szAiEQhTQzqp5BXowQ1_Z_-c5TOKVHzax6XpNNCfdQZ07fE92NSirlgB4acVnUiHWpbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور چین شی جین‌پینگ به نخست‌وزیر پاکستان شریف: از زمان برقراری روابط دیپلماتیک ۷۵ سال پیش، چین و پاکستان یکدیگر را درک کرده‌اند، به یکدیگر اعتماد کرده‌اند و از یکدیگر حمایت کرده‌اند و دوستی سنتی شکست‌ناپذیری را شکل داده‌اند.
🔴
علی‌رغم تغییرات بین‌المللی، چین همواره روابط با پاکستان را در دیپلماسی همسایگی خود در اولویت قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/122562" target="_blank">📅 16:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122561">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/933f4064df.mp4?token=fuU3k6UIU_zHDDpibLkQws31ya9Ox3_6znHPk0k3OvL8i7yRpQSjrG7j0drnuHsFFuZmOH9hNOb_ll-yDrEmGT8WEou2EE-D6ZnEInlpIZP8v87xRvbaOMBq4lsWZV6HkeAvPGS-qWDfq1-fXL7lIacVcC0-_5G7B8bRi6i5K9w2ZfLEwuMJbWRJuEAeP9hrHLz4jCiZiompV-Nk1fdfetU2y2kb3eE5wwHWQbJQ29f9rrVHi-844wxrX9gvGPhatjjc2Igv8lCwcpfqnmlDHihzc7vtDDN553VXbLcyvw1Sf2St1_O-C4mQ4H5g8ks-ayIhyCe7R3rt991okOteiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/933f4064df.mp4?token=fuU3k6UIU_zHDDpibLkQws31ya9Ox3_6znHPk0k3OvL8i7yRpQSjrG7j0drnuHsFFuZmOH9hNOb_ll-yDrEmGT8WEou2EE-D6ZnEInlpIZP8v87xRvbaOMBq4lsWZV6HkeAvPGS-qWDfq1-fXL7lIacVcC0-_5G7B8bRi6i5K9w2ZfLEwuMJbWRJuEAeP9hrHLz4jCiZiompV-Nk1fdfetU2y2kb3eE5wwHWQbJQ29f9rrVHi-844wxrX9gvGPhatjjc2Igv8lCwcpfqnmlDHihzc7vtDDN553VXbLcyvw1Sf2St1_O-C4mQ4H5g8ks-ayIhyCe7R3rt991okOteiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شی جین‌پینگ، رئیس‌جمهور چین
:
فیلد مارشال منیر، می‌دانم که شما تازه برای تلاش‌های مثبت در میانجی‌گری برای صلح از ایران بازگشته‌اید.
🔴
ما نقش سازنده پاکستان را تقدیر می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122561" target="_blank">📅 16:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N6Mm1rhSk3hmd8sIPXodZXkG9bxIaiZOwEsXMU8wJYXjgwxdD0BrKF5Cw4mlU5_JZNAZic7lrrarPlyPvc9sqtKThmf6pwaenfm6zbxownDCtqzAR5UQ_lbHBxdkJeJ-YMZUhIVJwDsFGWC-UDWQmW-0rnFJfcFoOnGWGLQobYR2mcKK3slpRbVEzk-MnA0z80Ro6J_v9pgQQ0GOSTZwOM73wBgYMlJSmolQjr6ZxcjMWmLoewZ8K88McORUHc811RHdfZrdbUdbfLaSl2qdwsxBdj7K0wwKmnFEKEdkfXiocX3NfcGbOnEe_1S4CoI6xW0K0y1qaiAkolvlaAu3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srkXPAK7lwC2_V8gVj0z1pqfJVXji6UI_2dvm5_lPL9IfrHwsElvzP0h7Yq_BWTOMzX8GmtgfwmlGRoKbmJSth5ehNmaNvRdd3YlnOvJkfJihMb2L7BnH4YL-1UiY1aE8oH-B_PDcIEVYehmizwS7zoeOb9MZJT8Npu4UeF9eHd42WjHyNO3X2nNsxUfLaMsmUTKb5m09oVp_J1HBovUyR1U1wpmvoqRms_wPJeougOY3WywmCigNroqIalc9k2VHzvaFiro49CMTdzLp6LVEc99Zi8QPp9RRYmNAfuue3rVZVJsuwOLlAgasphfSW0xcuTC8Io2ZonF_hYVCWhODQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل دو هشدار تخلیه برای ساختمان‌هایی در برج الشمالی، منطقه صور، جنوب لبنان صادر کرده است.
🔴
ارتش اسرائیل ادعا می‌کند که این ساختمان‌ها توسط حزب‌الله استفاده می‌شوند..
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/122559" target="_blank">📅 15:55 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
خبرگزاری مهر: محمد باقر قالیباف با امیر قطر دیدار خواهد کرد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122558" target="_blank">📅 15:54 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ به مجری فاکس‌نیوز: هرگز پول نقد به ایران نمی‌دهم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/alonews/122557" target="_blank">📅 15:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRmMk64Le2Z1NNwNxFWa0X5W7l_FsfXd1LFwbK5mJBSlouueQqpvlW1l-NOWTTqZgtkw3yJpMIg4h97PSm-pL61QFDo8tEcylUoeE5bFP7Baq-X5gScbPAEZpQ-OMBybcYIhvJr7A1xTh-8yU_fMCQ8Ws59Gw5i-fKFDdyXTUUyuYByVbfNO6K6Nm1kHEd-leNJrNzen8XOlu1oFoD3FcgT7mSj9jXIexsHsB6VE40_PRrjytdNSU9GESX6kxSnQHW0YPp7kOTK3SMjpsgXkKnbrDh5kPenL3r66GW2aykVV814r1FwBWR_jwLWJlgDbls28xMoILGT3JmddfkXk6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جروزالم پست:  رهبری چین ممکن است محاسبه کند که همکاری معنادار با واشنگتن در مورد ایران، انعطاف‌پذیری متقابل آمریکایی را در مورد هدف ملی اصلی پکن شایسته می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/alonews/122556" target="_blank">📅 15:49 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
«اتاق بازرگانی ایران و پاکستان، یک نهاد تجاری خصوصی دوجانبه که منافع تجاری ایران و پاکستان را نمایندگی می کند، امارات متحده عربی را متهم کرده است که فعالانه مانع ادغام ایران در کریدور اقتصادی چین-پاکستان از تبدیل شدن به یک کریدور اقتصادی پورتدارو پاکستان (CPEC) در دو کشور است دبی." - فارس نیوز.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122555" target="_blank">📅 15:45 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
تسنیم خبر سفر قالیباف و عراقچی به قطر را تأیید کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/alonews/122554" target="_blank">📅 15:40 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCjyn1EDTa8IBbuNF_0_0hQLdAQnFY3UMas4jcs-AU12RAZ2vQiuv-xZ3FsXlK0mg7zaU48wUegh4ZJ8-NBkbgoiXyHzzVbbFSejcfSEqjbKWbOtTOtpTPwc-TilBIfzPpmC1pyKHdMNim0hWmWA8BJMkLotTDBIYRjFEhbD56RXot2pVxFLkYVxgh7OzIKTdEVjcm5-xeYxodUrpMM__5PDESOV6rNtf8jFN3EVpOf48EvPXHQfa5sXJpto4Pq72tUxKoIDiUQ-SdODIoHZ9ASfAaLLkYOgwUhe8POOsEn3oe3gREjTeEETAJZHMvIp98E9pO0UgyyHOzaHJnbLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل هشدار تخلیه برای ساختمانی در اردوگاه پناهندگان فلسطینی رشدیه در نزدیکی شهر صور در جنوب لبنان صادر کرده است و ادعا می‌کند که این ساختمان توسط حزب‌الله استفاده می‌شود.
🔴
از ساکنان خواسته شده حداقل ۳۰۰ متر از این ساختمان فاصله بگیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/122553" target="_blank">📅 15:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122552">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رئیس مجلس ایران، قالیباف، و وزیر امور خارجه عراقچی امروز زودتر به دوحه، قطر، رسیدند برای گفتگو درباره تلاش‌های دیپلماتیک جاری برای پایان دادن به درگیری، طبق گزارش فاکس نیوز
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122552" target="_blank">📅 15:38 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122551">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIVYoik9Ql-2T4XH9k_vvxcfvJAG0EYQ0QJ-5XTDg3wik53d1pKAkRsH28SSB7lgN93pwKtWBLhzQwvPWW-76Dt6YdJnx-7qxEtamtm_gU6ZOA0cVFtROmE0hmA3NGyafBsZLtedDOCgXuelOmNI0LIrVRTCilGSx-pTnc9PTpUFvib43DcSR7XCzU2AruW3u2QthoHT47-Uw1sCY2irWX9rDr8LccofEMnmJnESRfx65tx3XybGn6Rb1RD2w4mO14lyDwlVGm_9XkUmqkH0IrNULvdSN5_jegVY0D9LlmmMJSMXVRiKDrTfwjaQBeB4TQD2GKKM-7UgATxbh2E-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مسجد ابوذر در بلوار ابوذر ،اتوبان محلاتی؛
آموزش کار با اسلحه.
🤔
جمهوری اسلامی از چه خطری این روزها وحشت کرده ؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/122551" target="_blank">📅 15:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122550">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwUlhMBs4tQAvQIoM-_vpqpqRaAJ3WgUA_AatQarqd1upkPBLFgoHgyEyp3JJ856w6-tYR7TSnr5CC-imrldAQfeq-U9PV6XbyEuHJWAsiiRFEkERpO_WeDL2IllZs9fzXGzZobhFpVXjk19SEfMkI1nW_Q1egRV6BAroBwbW_4WvWRl6qCHmTX4odotzce5yWFS7LAH1N3pQutpNg0IzeZZ97FwDD04XL7RZHOnn8f7rgPjnZe-YZ5xrYrmJXRbl0Wr4q3j3W1G69EXtW2gp-J6zh-pHmZQ5kwCw4JLuRIavkoZ4H8ZANS0X_OQelX7pg9-SRZeYdcStpRbBnr1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همچنان حمله‌های ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122550" target="_blank">📅 15:29 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122549">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
دو مقام اسرائیلی به رویترز: نتانیاهو به نزدیکان خود می‌گوید که هیچ تأثیری بر تصمیمات ترامپ ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/122549" target="_blank">📅 15:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEeq8B4f-YNTxV_jIw07x7azVL3oJqtWBnIVuZIZd7NIRVWMEi2KeV01JNxR9dSjpYXt9pGD9qeGumMQ30NB6ToAt3fFztEaj25h-HqcowAL6AFBIMmtnOMiXN7uqeOZTVyCFIJuxlIZ7btpdZS9F2GxFLSI9gqw3aH1s1UN2mFiDBmF8eQpXtQ3LqLnjdzVsVC-aQ6vqztf5sloFt45BUI15exFAdrnLRtcNGNS3UhBVFFzEGQnlIVfVbZVv4AGkKFyzv1WT_g_XOwm21M_wa8rqhEndhMdSDYPiqr5ISJznIOdK0IcmfRn9HWdJBmMUTaSJfYx-P71n2gBS3PIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527cd39d33.mp4?token=lO5srp13qyvIpzIFokVfwfgExazcFw8uhGRGDCGDioPfrD4qK8tcwW-uMHLCTzcX8iFyooieUkRO7nIPW94QYS2IPn4KaWz2wJuPC02G8KnbqlIrUlLgZaPjCb-YGwvatV1UZiELAblv1_1Fp2visGgx6MfVgcfIKmkFODoQYs6J8gQqvCIgKMNfp3fl0rqHpWirn0yjShggHc-8dhZOwW1-ACcYvHWOtNv6vFMM9fk4On9C4boCHN_fdRs1UV629eUQ0E_x-wwJhit1lJp7pYxHMhrJqrFfcvBPkRMZbUXeA8h-P0iblrIGWZ8I2CHmlQNeankJ_lAE10S21wxaWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527cd39d33.mp4?token=lO5srp13qyvIpzIFokVfwfgExazcFw8uhGRGDCGDioPfrD4qK8tcwW-uMHLCTzcX8iFyooieUkRO7nIPW94QYS2IPn4KaWz2wJuPC02G8KnbqlIrUlLgZaPjCb-YGwvatV1UZiELAblv1_1Fp2visGgx6MfVgcfIKmkFODoQYs6J8gQqvCIgKMNfp3fl0rqHpWirn0yjShggHc-8dhZOwW1-ACcYvHWOtNv6vFMM9fk4On9C4boCHN_fdRs1UV629eUQ0E_x-wwJhit1lJp7pYxHMhrJqrFfcvBPkRMZbUXeA8h-P0iblrIGWZ8I2CHmlQNeankJ_lAE10S21wxaWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریب در قانا و نبطیه در جنوب لبنان پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122547" target="_blank">📅 15:23 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در شبانه‌روز گذشته ۳۲ کشتی اعم از نفتکش، کانتینربر و سایر کشتی‌های تجاری پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122546" target="_blank">📅 15:20 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رئیس مجلس ایران، قالیباف، و وزیر امور خارجه عراقچی امروز زودتر به دوحه، قطر، رسیدند برای گفتگو درباره تلاش‌های دیپلماتیک جاری برای پایان دادن به درگیری، طبق گزارش فاکس نیوز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/alonews/122545" target="_blank">📅 15:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عوستاد خوش‌چشم: علت منصرف‌شدن ترامپ از حملهٔ دوباره به ایران، ۲ عملیات پیش‌دستانهٔ منتسب به ایران بود نه درخواست عرب‌ها!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122544" target="_blank">📅 15:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ادعای واشنگتن پست به نقل از یک منبع:
بازگشایی تنگه به صورت مرحله‌ای خواهد بود.
🔴
در مرحله اول، آمریکا ۱۲ میلیارد دلار از دارایی‌های بلوکه‌شده ایران را آزاد می‌کند، مین‌روبی در تنگه آغاز می‌شود و محاصره آمریکا برداشته می‌شود.
🔴
تفاهم‌نامه شامل توافق هسته‌ای نیست، فقط تعهدی برای مذاکره بعدی درباره مسئله هسته‌ای است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/122543" target="_blank">📅 14:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122540">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2b6f9bc3.mp4?token=ERYrENRTSQk9KEQfN8s20NyiVRlR_eFwTjB22gZNATblDnB7uM5H-nKFXswFAxHvyCQkLFuUhDqSQKVVF24UOuJbHC_TLWXB5aCoTu3auWQsJ6-fB7gAukb0BYpeFu3Yb5lVe2gD_cL468-qthH88iRvsY4-_JbcXlaudGuwx67hrvH3pdq19DeBVNvEqx65mGrD7G0UiCBommojCjtbPOuQ-fJIV78lPWcdENK14flvEwj2LfIQpNmXeDu5Jx_-RGloKq_8UorJHgpREDoYjZR2svlqYNIRJ2ZXansV_hpXECs1f6kDgudRR1qfij71r0INyD8Ve1TUpn4-ZADqmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2b6f9bc3.mp4?token=ERYrENRTSQk9KEQfN8s20NyiVRlR_eFwTjB22gZNATblDnB7uM5H-nKFXswFAxHvyCQkLFuUhDqSQKVVF24UOuJbHC_TLWXB5aCoTu3auWQsJ6-fB7gAukb0BYpeFu3Yb5lVe2gD_cL468-qthH88iRvsY4-_JbcXlaudGuwx67hrvH3pdq19DeBVNvEqx65mGrD7G0UiCBommojCjtbPOuQ-fJIV78lPWcdENK14flvEwj2LfIQpNmXeDu5Jx_-RGloKq_8UorJHgpREDoYjZR2svlqYNIRJ2ZXansV_hpXECs1f6kDgudRR1qfij71r0INyD8Ve1TUpn4-ZADqmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک پهپاد حزب‌الله امروز صبح به سقف ساختمانی در متولا، شمال اسرائیل، حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/122540" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122539">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLt1fGi8kkwjwYJ59OSVxDgBNU_bOJWnuv2IYC8NE-xGx-0Yx1qRnm4Wo2IhjuIqOffg7B6_SECuVeN-StG0Iqrtka2O5GPXRI-7d2TkzCaXFudN-UeG4iVooJSqJzpyKbscqq47wZia43cvrK-XrdeE76Dy4gz01hFGwS8DubtkUiv7OeCysL5Geda9czhoCdbirBku2dFYkLNzVKx5N0FxHPlcOG-dw2ttHItEaDU8VXp3CIqYFh2mNjodrbb99EyxRHxGr5O8N0dzaUDdbHc6rC6Z9dFV_0CAivWJJ6k7jXbaJL4MZCc0PegubeAw8Vs7IDSyqr0yxAcqg85Vpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۷.۸۰ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122539" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122538">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaG86VCOcVhWJmKpOkWe9Oh8MS3iZU_S-_7MLxbX83vS1m-dCPqYkkAlKoocVAP9p9pG8Q3W9mSYji1HAxejlNzwFA-du45js5jedSC0U7EGO67od9QvDKo1qW6G857TT9zkmlmIsiD9b8l1pUjU1m3QetBXN6_yMqdJsMeW8FdgiNjAafSw6dNufrVl0zddBnfMNvC_T6WZBibq-BGm1N9FIQXJ9pgo-yvvvDoe57dNYmmX0docnhf3WJh1Lw_00Vp2Xw94qjlC3rjnUdGA8uqc9zrj0yo_93A2GliyhiF9n4vhD5Hx5buVnfUc2df3I7wlgxleUBcAFzwca2lX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیئت‌های چینی و پاکستانی در تالار بزرگ خلق در پکن دیدار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/alonews/122538" target="_blank">📅 14:44 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122537">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZeRmNXyMa9Lej5CZKiDre2fKQ6BXhwXXPXNbbamFb0yz9zJ_uW0uZAoJCC754QtKcgFn_qNZ3mVpLtF0U6SbNKeDTtWEX3Veg3wLXUOn-3GO7dwLB_1_RS1DrFZrjdj04L07OXqmJBsq5O7cJ9V9w5entX-E-u83uew38MA75Uex2DWiyUvMtNN2bIwzvcbmuYSs3DyVDzLnY_VTQ7vsxZK6wVNcoYf9od68FndtCid1yAukkN5odb3X25PasAvW34n4u4dlBdqa4HlkwsEDNlrX_UbAfMirZSxWVc-S3BcPg4dkuTiaR_YipStqQAC2pYNEjfxcOXEMaercT2CWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social: دموکرات‌ها سیاست‌های بد و نامزدهای بدی دارند. غیر از این، آن‌ها عملکرد نسبتاً خوبی دارند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/122537" target="_blank">📅 14:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122536">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDA8WROzE2agn7xvO5nHo-rcsTyGEWjDD2OS9SYMZv9ae6Y5JdAkC-vznkXkJoA_kTdfLtXhTvOq9vtfG4wKcB5tC35Zf_jVT2pDnfPwq6k7VltfB4vSwylRPOKJgaeQsi4LbW3v4U7EzuCEhxAlSpvYrhH4FD7bW1v7IQNFpIpWndWEqU1g3lf9bjrGl6duS34sRb0JZcndp3YcPC8kP_vhj5o9UO19J9vwzhAYD0y2MeYBXv7_dibGTVhHapkjJZmUpcPHl8FA-8z1LkVygrVGgKDOPe2n90YMlN9sAJW9V6nXTTbU9HiEqfrwWlKuS8uu1N9bG6MNYNCQLBnB5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
روز یادبود مبارک به همه، از جمله دموکرات‌هایی که به ارتش ما و تمام موفقیت‌های عظیمی که در سال گذشته داشته است بی‌احترامی می‌کنند.
🔴
خداوند کسانی را که بالاترین فداکاری را کرده‌اند، برکت دهد. من همه شما را دوست دارم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/122536" target="_blank">📅 14:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122535">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
شهباز شریف، نخست‌وزیر پاکستان در دیدار با رئیس جمهور چین گفت: پیشرفت قابل توجهی در مذاکرات ایران و آمریکا حاصل شده و اوضاع در مسیر درست پیش می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122535" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122534">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دبیر کنگره موبایل ایران: برآورد خسارت روزانه ۵۰۰ میلیون دلاری به اقتصاد دیجیتال ایران در پی قطعی اینترنت و اختلال در زنجیره تأمین موبایل، با خطر لغو ۶۰ هزار شغل و توقف واردات در فروردین و اردیبهشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/alonews/122534" target="_blank">📅 14:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122533">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری / منابع پاکستانی به خبرگزاری آناتولی گفتند که آمریکا و ایران می‌توانند طی همین هفته، «یک پیمان موقت برای پایان دادن به جنگ امضا کنند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/alonews/122533" target="_blank">📅 14:29 · 04 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
