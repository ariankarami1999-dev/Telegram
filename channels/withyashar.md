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
<img src="https://cdn4.telesco.pe/file/qtnyVtT-yZbSj8UOWWyqf0Lz7I9tsG6ykdHA0RcW0_Rf6setvcYAh-WuGxmaFvu806PtWtjDzIJpXWsNppDojqwX0njv3XcP1qdvziljo6XJdP0MQLw99_oJm3sekGxUtVtfUmEupov0iJ9pNaxoHCuOdu-M6ViGcrYPQNYEuWFcfA_0TL743xWje5V5A_G1CuGqRC9JILknkdm0NgPHRnkcRURxIPUCfYL7nb0SoVWK9cGlAvG1hZ_niOqkOXVSJvPNZBiPwhKudiKy8HPN0WPL7bU5M36eLg2eV4lSrRlbDFnp5SZi9fBhcHVAg7yBD1qYZQZXY1bxDdpJpiB29A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-28 01:15:23</div>
<hr>

<div class="tg-post" id="msg-23484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ برای گذراندن آخر هفته راهی کمپ دیوید شده است؛ طبق برنامه رسمی، او شنبه و یکشنبه در این اقامتگاه خواهد بود و برنامه‌های این دو روز با عنوان «زمان اجرایی» و بدون حضور رسانه‌ها ثبت شده است.  هم‌زمانی این سفر با تحولات جنگ ایران مورد توجه قرار گرفته
@WarRoom</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/withyashar/23484" target="_blank">📅 00:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش ها از
هدف قرار گرفتن نزدیکی اقامتگاه بن سلمان
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/23483" target="_blank">📅 00:00 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=g2KPaCWfgPkGusIa_mKnX7Tkn4PelQqlkilu43rhCtTDwMsho6524NXy_OQfR0M6OfBc79KcBU7Cl-tzDKk3ovD_aJIw1TkuPWVa10abBpr5xjNRgz5fwzr6cflZLli5vo4UtCa7NryDyr_VM_8k3WNYei1SVn49dxnwyH_SLkXwOPZJDujDKvVQFrtPFVGpT4RqGsVZ03hdr-x039kSAT0SE_Jhww8kIxKBOB4GO8qkz3c5Raq6kab38MR10nCkYC5ahEotq3X6DJBUPFGRI8cR1R6Qi_RJ6ohC2DXMOMMNKSQp5EbWTsRUZZoXiGTwLB0eTJmFhsqgacvoRy1rsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8fa371e84.mp4?token=g2KPaCWfgPkGusIa_mKnX7Tkn4PelQqlkilu43rhCtTDwMsho6524NXy_OQfR0M6OfBc79KcBU7Cl-tzDKk3ovD_aJIw1TkuPWVa10abBpr5xjNRgz5fwzr6cflZLli5vo4UtCa7NryDyr_VM_8k3WNYei1SVn49dxnwyH_SLkXwOPZJDujDKvVQFrtPFVGpT4RqGsVZ03hdr-x039kSAT0SE_Jhww8kIxKBOB4GO8qkz3c5Raq6kab38MR10nCkYC5ahEotq3X6DJBUPFGRI8cR1R6Qi_RJ6ohC2DXMOMMNKSQp5EbWTsRUZZoXiGTwLB0eTJmFhsqgacvoRy1rsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: جنگ به زودی به پایان خواهد رسید و وقتی این اتفاق بیفتد، قیمت بنزین شما به سطحی که قبل از آن داشت، کاهش خواهد یافت، شاید حتی کمتر از آن.
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/23482" target="_blank">📅 23:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">العربیه: وزیر خارجه پاکستان محسن نقوی در ساعات آتی به ایران عزیمت می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23481" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">المانیتور: یک منبع ارشد اطلاعاتی اسرائیل می‌گوید نهادهای امنیتی اسرائیل در حال حاضر با
حمله پیش‌دستانه علیه حوثی‌ها مخالف‌اند
. به گفته او، حوثی‌ها اکنون هیچ بازدارندگی مؤثری از سوی آمریکا، اسرائیل یا عربستان ندارند و به «اسب تیره» منطقه تبدیل شده‌اند؛ تهدیدی غیرقابل‌پیش‌بینی که می‌تواند عربستان و متحدانش را به اسرائیل نزدیک‌تر و وابسته‌تر به توانمندی‌ها و اطلاعات اسرائیل کند
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23480" target="_blank">📅 21:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">آسوشیتدپرس:
سقوط بقایای یک پهپاد حوثی پس از رهگیری در عربستان باعث کشته‌شدن یک نفر شد.
پدافند عربستان پهپاد را منهدم کرد اما بقایای آن روی منطقه مسکونی سقوط کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23479" target="_blank">📅 21:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الجزیره: یک منبع مطلع آمریکایی اعلام کرده حدود
۶۰ میلیون بشکه نفت ایران، یا نفتی که مشکوک به منشأ ایرانی است،
روی نفتکش‌های تحت تحریم سرگردان مانده است. به گفته این منبع، نفتکش‌هایی که خارج از محدوده محاصره دریایی قرار دارند نیز در معرض رهگیری هستند و به همین دلیل با سرعت کمتری محموله‌های خود را تخلیه می‌کنند. همزمان، واردات نفت چین از ایران یا محموله‌های مشکوک به ایرانی بودن به حدود
۴۴۰ هزار بشکه در روز
کاهش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23478" target="_blank">📅 21:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJvuwr6fF69GynC9bqoBUo1H-1FwKMGXfWusKAPS-N2RBYorPzCNGS_VjZT_GJj4mf7NIIICJ3zSqfshaqPQhVJ6IsNEiqOwV9YFw4H5e__sW3ZHGz0tdBpdsoBzBhwaLH23DrSYeaqBJZqwDlE8A98NHV15noPyxi7qMG4lEQ_30f5c8CumqRSenM5mk-moqkpr-8S8yrSyPsYUS5sbGkIgRLUAveLuyfDtsWpLRde1_O1wrQOvXOF9cB_shP-PEUCaq1qr9Fdh-zZwR3gfxBrdZ__TVoi-_KLB0Jvlw8QWzDg7bsIhxbfO8YK03kh1Z6jdqG7ziwkZgJ20MZphqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف
:
دوره‌ای که در آن F-35ها و F-15های شما شکار می‌شوند و مجبورید گزارش دهید که آسیب دیده‌اند
🤏
از قبل آغاز شده است.
آنچه زمانی سوخت خالص کابوس بود، اکنون واقعیت روزانه است. با آن زندگی کنید.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/23477" target="_blank">📅 21:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الجزیره: وزارت خزانه‌داری آمریکا اعلام کرده اقدامات سختگیرانه‌ای علیه بانک‌ها و مؤسسات مالی در امارات و ترکیه که به گفته واشینگتن از ماهان‌ایر و شبکه‌های مرتبط با آن حمایت می‌کنند، آغاز کرده است. این اقدامات با هدف قطع مسیرهای مالی و خدماتی مرتبط با جمهوری اسلامی و ماهان‌ایر انجام می‌شود. آمریکا پیش‌تر نیز چند شرکت در امارات و ترکیه را به اتهام ارائه خدمات به ماهان‌ایر تحریم کرده بود. هنوز نام بانک‌های هدف، نوع دقیق محدودیت‌ها و زمان اجرای کامل این اقدامات اعلام نشده است. همزمان، ماهان‌ایر اعلام کرده از ۳۰ شهریور پروازهای خود به استانبول و آنکارا را متوقف می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/23476" target="_blank">📅 20:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بر اساس گزارش رسانه‌های تحلیلی مستقل، دولت ترکیه ابلاغیه جدیدی به سنتکام ارسال کرده و هرگونه بهره‌برداری از پایگاه هوایی اینجرلیک برای سوخت‌رسانی یا هدایت پروازهای رزمی علیه هدف‌های منطقه‌ای را اکیداً ممنوع اعلام کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23475" target="_blank">📅 20:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23474">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ به نیوزنیشن : باید ببینیم که آیا ایران نابود خواهد شد یا خیر
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/23474" target="_blank">📅 20:20 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23473">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ در پاسخ به سئوال نیوزنیشن درمورد گزارش روز پنجشنبهِ اکسیوس درباره «تصمیم بزرگ» او: «آنها حالا می‌خواهند به توافق برسند. اگر این توافق، توافقِ درستی نباشد، حتی به آن فکر هم نمی‌کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/23473" target="_blank">📅 20:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23472">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: ممکن است به سمت جنگی تمام‌عیار با ایران پیش برویم.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/23472" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23471">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: ایالات متحده در حال مذاکره با حوثی‌هاست و آن‌ها نیز به دستیابی به توافق با آمریکا تمایل دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/23471" target="_blank">📅 20:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23470">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">برنامه «پاداش برای عدالت» وزارت خارجه آمریکا برای اطلاعاتی که به مختل کردن سازوکارهای مالی سپاه پاسداران، از جمله حساب‌های رمزارزی، متولیان نگهداری دارایی‌ها و شرکت‌های پوششی، کمک کند، تا سقف ۱۵ میلیون دلار جایزه تعیین کرد. و همچنین اعلام کرد سپاه پاسداران…</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/23470" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23469">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/23469" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز: آمریکا به هیات اصلی جمهوری اسلامی، از جمله مسعود پزشکیان و عباس عراقچی، اجازه داده است هفته آینده برای شرکت در مجمع عمومی سازمان ملل به نیویورک سفر کنند. این هیات کوچک‌تر از سال گذشته خواهد بود، اما اعضای آن با محدودیت تردد در مناطق مشخص نیویورک و ممنوعیت خرید کالاهای لوکس و برخی کالاهای دیگر، از جمله عضویت در فروشگاه‌های عمده‌فروشی، مواجه خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23468" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">وال‌استریت ژورنال: تلاش جمهوری اسلامی برای دور زدن محاصره دریایی آمریکا از طریق انتقال تجارت به مسیرهای زمینی با مشکل جدی روبه‌رو شده است. صدها کامیون در مرز پاکستان و هزاران کامیون در مرزهای ترکیه، ترکمنستان و افغانستان گرفتار شده‌اند و تأخیرهای گمرکی و افزایش هزینه‌ها روند انتقال کالا را مختل کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23467" target="_blank">📅 18:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23466">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حکم اعدام امید گودرزوند چگینی، ۳۷ ساله و از بازداشت‌شدگان اعتراضات ۱۸ دی در قزوین، در دیوان تایید شده است. او در زندان چوبیندر قزوین محبوس است و پس از ۴۰ روز نگهداری در سلول انفرادی بازداشتگاه اطلاعات سپاه، بدون دسترسی به وکیل محاکمه شد. به گفته این منابع،
این زندانی پیشتر از کارکنان نیروی انتظامی بوده و استعفا داده بود
.
@WarRiom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23466" target="_blank">📅 18:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنگه صدای زوزه ابومهدی المهندس میاد
@WarRoom
😂</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23465" target="_blank">📅 17:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ادعای رسانه های رژیم :  شلیک ۴ فروند موشک کروز «ابومهدی المهندس» از جزایر ایران به سوی اهداف متخاصم در دریای عمان
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23464" target="_blank">📅 17:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بیانیه نیروی انتظامی‌ ، فرد دستگیر شده در ماجرای تبریز دارای چه سوابقی بوده؟
نوامیس مردمو تو تاریکی با قمه خفت کرده! با چاقو زده لب و شکم یکیو پاره کرده
با قمه زده شُش یه نفرو سوراخ کرده، یکی از آنها با شیلنگ نفس می‌کشه!‌
مواد فروش هم بوده و
….
نیروی انتظامی همچنین اعلام کرد این سوابق به هیچ عنوان رفتار خارج از قانون مأموران را توجیه نمی‌کند. مأموران خاطی تنبیه انضباطی شده و پیگیری‌های قضایی ادامه دارد.
@WarRoom
یاشار : من انقدر به این مامورای نیروی انتظامی پول دادم که تمام رفتارشون رو توی شرایط خاص می‌دونم. از لحظه اولی که ویدیو رو دیدم کاملاً متوجه شدم که این قضیه ناموسی هست. در نتیجه با این‌که پیام های بسیار برای انتشار این ویدیو فرستادین ، از انتشار اون خودداری کردم. مثال خیلی ساده‌ای از طرز فکر و نگاه من و کسانی که این ویدیو رو فرستادن و بارها اصرار کردن تا منتشر کنم.</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23463" target="_blank">📅 16:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گزارش فاکس‌نیوز : دونالد ترامپ، رئیس‌جمهور آمریکا، در حالی وارد
هفته‌ای سرنوشت‌ساز در سازمان ملل
می‌شود که موضوعات ایران، چین و هوش مصنوعی هم‌زمان در کانون توجه قرار گرفته‌اند. نتایج یک نظرسنجی جدید «فاکس‌نیوز» نشان می‌دهد که ۷۱ درصد از رأی‌دهندگان معتقدند دولت ترامپ فاقد راهبردی روشن برای پایان دادن به جنگ با ایران است؛ این در حالی است که ترامپ در حال بررسی احتمال انجام حملات بیشتر علیه تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23462" target="_blank">📅 15:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23461">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فایننشال‌تایمز: ایران برای دور زدن محاصره دریایی آمریکا، انتقال بخشی از تجارت خود از مسیر دریا به مسیرهای زمینی، به‌ویژه مرز ترکیه، را افزایش داده است؛ ترافیک واردات از این مسیر در اوایل سال ۲۰۲۶ حدود ۲۵۰ درصد رشد کرده، اما تأخیرهای گمرکی و هزینه حمل‌ونقل افزایش یافته است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23461" target="_blank">📅 15:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23460">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آسوشیتدپرس: چندین هزار نفر روز جمعه ۱۸ سپتامبر در تهران در تجمعی حکومتی علیه آمریکا و اسرائیل شرکت کردند؛ مقام‌های جمهوری اسلامی از ثبت‌نام بیش از ۶۰۰ هزار نفر برای آموزش نظامی خبر داده‌اند، اما این آمار مستقلانه تأیید نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23460" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23459">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شرکت آرامکو سعودی به پالایشگاه‌های نفت اروپایی اطلاع داده است که در ماه آینده نیز هیچ محموله‌ای از نفت دریافت نخواهند کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23459" target="_blank">📅 14:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23458">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست. @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23458" target="_blank">📅 14:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23457">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رویترز:
کره جنوبی اعلام کرد هیچ نیروی نظامی را برای ورود به درگیری خاورمیانه اعزام نخواهد کرد. سئول در عین حال در حال بررسی راه‌هایی برای حفاظت از کشتی‌های تجاری، مسیرهای انرژی و شهروندان خود در منطقه است
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23457" target="_blank">📅 14:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23456">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ایلان ماسک: «یا باید ویدیوگیم بازی کنید یا احمق بمانید؛ فقط همین دو انتخاب را دارید.» این اظهارنظر در واکنش به پژوهشی روی ۹۲۳ نفر مطرح شد که نشان می‌دهد گیمرها در عملکردهای شناختی، مشابه افراد حدود ۱۳.۷ سال جوان‌تر عمل می‌کنند. این مطالعه همچنین ارتباط بازی منظم با عملکرد بهتر حافظه، استدلال و سرعت پردازش اطلاعات را نشان داده، اما ثابت نمی‌کند که بازی‌کردن مستقیماً باعث جوان‌تر شدن مغز می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23456" target="_blank">📅 13:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23455">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E39BeoMu6ifcpcl1KY0-bqkWIii0LGM5Evrbq0xxNOT_unLaix2c8kezOPsMb0-PbGbswtJlzqgTwN65C68ekVROf5KyIMCIRMcbY02IUg7Hs-LpZUTtbNMTSWv-BPQiahd7dkHbDpXSDliVdaPOFwaStY2DDqNrQAEdA8KL2xfTSipE_91s6QujCB3FanJQPKtm0ZAlHkfprT1tVYRKH3RnN8hfjowSSISJTqMCc_S0WYrK9AVLRKr5pwq4oy1NIPo__RLkeXq1zUHIBar1y-xfj7VZFxTdR65y60RB78dSwBl6pbOzZikt2Pr4EzBFBZM3dMDoLm_zi3OMRFWo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ستون دود شرق تهران
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23455" target="_blank">📅 12:46 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23454">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جی‌پی مورگان: بیت‌کوین می‌تواند از طلا جلو بزند؛ تحلیلگران این بانک می‌گویند اگر سرمایه‌گذاران از مواضع دفاعی خود در
صندوق‌های قابل معامله در بورس (ETF)
بیت‌کوین خارج شوند، احتمال افزایش تقاضا برای بیت‌کوین و عملکرد بهتر آن نسبت به طلا وجود دارد. این بانک همچنین اعلام کرده صندوق‌های طلا بخش عمده خروج سرمایه‌های سال ۲۰۲۶ را جبران کرده‌اند، در حالی که صندوق‌های بیت‌کوین تنها حدود نیمی از خروجی‌های قبلی را بازیابی کرده‌اند.
بیتکین در این لحظه از 78,000$ عبور کرد
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23454" target="_blank">📅 12:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23453">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOxWL8I5S_QJ1RovUCMqGBBI1bloW6bRJ6Z_NZisPdESPegMvTc8sr6bn-z0nJt6HbDUTGC4Hh9d_GdnRQQiowp4Rhvr3S3pMEnIpwVOuAyzRtdeYTQXQb31MxsEhSUkaJkJNZZzgEqn3oG2crn8gOd7Z9Hyx35_ZZb9Ke9mf5_m6dJb5Pe1trBDDVMiqPzhtlDhakvgBOfgg93njPTFJvUVVdSXOkKRKovQs80vRiTmbV8O6tBzTIBeXjlPMKI3xnkatoRAbg1Azd9NiJmHFr2of2OQUoMqvZFRTG-eRn3RjTVkQyvuyIxBs_eaxixl3jHkapuax4RRgg3T4Zf41g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز جان فدا ریختن بیرون، رژه میرن. این وسط هم دوتاشون مزدوج شدن. قیافه داماد شبیه کندفیله(یه مار حشره خوار) نمیدونم بشناسینش یا نه
@WarRoom
😂</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23453" target="_blank">📅 12:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YmBx5veCML_XFPl-oQ9AvGs3AavfGBQyc9LjyyK-4pg6dboj1_IqSNRfp0blOlBqXneJ3_j7I8CpMGRl0aiqvV-Vn9k_Yp8N69_hV9r0b4pRcRwK0NpHJ_XlbOcFMFYAQgcOMSJGpKJtlZp-OEc05g2wIIItkjYpO23vG-oIglJto7EcanHyQtu-l5zavXwbNYK7uuMIoJwj5a1B9tG1Ql4GCcoTnLo8KNndxAjppiY9BSen_Fb28147iTDEbexiD_FfF-I_N03nPN5KQQLkXMfuhcwbZxqV5-ZiRbTxPpjIvPbRL7yaDMLyFD-xr046RP2n88W-8897pUyY0xtRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSIMcxE06CHJAv6ta2ZzYeUtMERGQt4tAj9VaPd63r8nqL0tBngDs-T4yV8KAlzt2djcikwWY4ouIgaQDTPPyOGnq8X76t-CLy97XxpmLVevbIFMLranZ3UvQDhsiy1DaW74tO6Mh4U17guk0VnmwiUEtO6zKBRMnhYD5zXIYtMIVqUO2KUxSKAI1Cn8fUGZhRnGCxKs5izWm1wNhSZKuZn_FmcksSwMh2zbvz6GgtH1QQckNBMYuyqYF5S-TWkWl0FT28WrWGiT6ppD1z68DUeWnbgIcMpIq4qB6U05G9PC0nMQCqiqfp8kkay8yfM5e64mLr45v7qTV8BtME6b5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به سه نفتکش در حوالی تنگه هرمز
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از دو حادثه جداگانه علیه نفتکش‌ها در منطقه تنگه هرمز خبر داد.
حادثه اول: طبق هشدار شماره ۱۳۸-۲۶، یک نفتکش در تنگه هرمز هدف پرتابه‌ای ناشناس قرار گرفت. اصابت پرتابه باعث آتش‌سوزی در کشتی شد، اما آتش بعداً مهار شد. خدمه سالم گزارش شده‌اند و میزان خسارت هنوز اعلام نشده است.
حادثه دوم: طبق هشدار شماره ۱۳۹-۲۶، یک نفتکش در هنگام حرکت به سمت خروج از تنگه هرمز، هدف پرتابه‌ای ناشناس قرار گرفت. در این گزارش، آتش‌سوزی اعلام نشده و جزئیاتی از میزان خسارت نیز منتشر نشده است. خدمه کشتی سالم هستند.
حادثه سوم : تایید نشده دیدبان های اتاق جنگ به من از حمله به کشتی سوم هم خبر میدهند
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23451" target="_blank">📅 11:59 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZo8_IXePw5IwmVyrYWUYV5fYiPn4UjlDQuEDJnNn-2zJgX_68cunGfzHw6flqgG6fbiwE5HQ0J1uHgukZqctm4ui6CatvjfzBpobn-CcQnORfQHAoGSJ7lwKyUsVxkPd-GPJFcbuRk9V5BQ4mPyMzYaf7w6gGLLNxgGCqwAGDjed5pG0zifFAGzFU56ZGZ3r1bCw4uRqo7W3D_58OgAal7o9iFXD-cgsYTVxqNVU2gw3d7lIiYy9Ikpkq0J9EB0YOxNlMtDaX4X1NcBut_9EmWaIZuWo00QFFQTj5Wj6R6_uTfggPOoh8gGaAkSwyex1jBw85ST6mltrc4rvC0OiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث‌ با بازنشر مقاله‌ای از واشنگتن‌پست درباره افشاگری‌های داخلی پیرامون جنگ ایران نوشت: «خیلی جالب است. حتماً بخوانید! به افشاگری ادامه دهید،
سگ‌های کثیف
!
وقتی شما را پیدا کنیم، بهای سنگینی خواهید پرداخت!!!
» مقاله مارک تیسن، ستون‌نویس واشنگتن‌پست، استدلال می‌کند افشاگری‌ها درباره هشدارهای تولسی گبرد، مقام‌های ارشد نظامی و جی‌دی ونس درباره خطرات حمله به ایران، به‌جای اثبات اشتباه ترامپ، نشان می‌دهد او برخلاف توصیه‌های مخالفان جنگ عمل کرده و تهدیدهای حکومت ایران را جدی گرفته است. تیسن همچنین اقدامات ترامپ علیه ایران را یکی از جسورانه‌ترین تصمیم‌های سیاست خارجی یک رئیس‌جمهور در دوران زندگی خود توصیف کرده است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23450" target="_blank">📅 11:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیویورک‌تایمز به نقل از مقامات آمریکایی:
ترامپ در حال تقویت رویکرد متفاوت برای پایان جنگ اوکراین است؛ پیشنهاد قرارداد تجاری با روسیه
کاخ سفید در حال بررسی امضای قراردادهای تجاری با روسیه، حتی پیش از توقف درگیری‌ها ست
ترامپ می‌خواهد انگیزه‌های بیشتری برای نخبگان روسیه ایجاد کند تا برای صلح فشار بیاورند
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23449" target="_blank">📅 11:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد ایالات متحده رسماً از
شورای حقوق بشر سازمان ملل متحد
خارج شده است. واشنگتن این شورا را به ترویج «ادبیات ضدآمریکایی» و اتخاذ رویکردی مماشات‌گرانه در قبال حکومت‌هایی که به سرکوب مردم متهم هستند، متهم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23448" target="_blank">📅 10:47 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rP9uko7PXFoXZaVaDMhr220GArqw2gtzQl-RRt_Nkcn2RdK2YBacNaK5SmGMAJ89rpmUEBULKvvWuTAWBZC6ip7R2x7P4BHx8MPv05RFJfJ2K4HZXM77oeSRGHjiO6tmI-JjOkKEv_eb1eYtMUlOIVAFBw5aYLVysbi6jLcRARV036ZuhQBM9J_0KuXMpRuet00u832YtQOlRo4ryt7n6d2k-AFHJfhIIj4AuwP9Oc9MYl4NfUgf3ioOToXNxjL7JeIByUmIgpHxl5UrPorFIhCTvTeAeixPY55QoaCRxuDces99aW8wmB11CpqmbO5DXwE8VppUThaVzi_meR9P4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoUslWiFeXUD2PjI06PR0NRPKRS8sMKT5eSwYJzOvICqniIf_daCBBErrggmhiR-S_O_gWNJbojwFqrKiZLOeZx6bltNQt8SIO5Im-oFb5dpUl8oa2uY9fhj_YaJmcREFLgKXkOJErCdsc3S6O9nd3VrWQwHqMBpRdeIh9SaBSk5Te8MWpuNP3rHKouzPUYFFqydCtGGyffxde1mr2J5uvFE29pJ8ttWTglLuui8fpnweL325vjGFSVGy3HknDETBVq5PhyjQa5_OiySjDczNmXjxz0cMqr5LnC4GOn-BwaqqPOuQIrBvwXzLGT8NbhY72kQHgZe0CXPdajlvdpAPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANvILlCG3HC0nsJe2VoJMF9RifBoYLZS2WlT412-YkU1SMKxQkeCFWXrlp8WgxmwKMAjXgtoaWHrWa98xEtqIZpLF1TVNWlRvOvne9CTQ2-Ihg9Ya5jpIf57ybbysl79zbQ18fRS0EWQtmGc_1dZrJppdQ8NQS1FYjOBhEgNtA5vRa4SdU_9f0PGoY718hiW1ouefNyK6SPtF6B654afYceKrCThPhY0e_OGLBpRsp22pDU7yG-2snodgI90FSmZiLpXkCxEarhltIEOHAG3OVLYHrD2AdvXb_qYUj01faSCG0ZbG-Fj611fh1y-kiT0cB7lYJL8z-GNMfaSN5Jfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NO25xhoOtUkJ-5GD30v3_sOqZl4cKgkp7096RBFmK2XtiYsbbVJK6_4_pQSrFdYdKpez8p7w1YwMbt6FJtfRrIHnw_hEGOqk_MU1e47SugN45S_YQFqVSXHQfsr-TRrIbsr3B7lTqinYEwSRtn4LhAx0ae6Wtw6y86am_0Vwvq84ojp1fQw-ZbqJ7vkt29SLtgDcoW631cw0CsuF4jBHFAWGyj4-e8O6HP3oGoi11H_BoQlgfdSZGcwrljD5L6o0RsgPME9c5f8LV28PSK7wXg4PhHvslvueoU7W74XBIZChnVROqLRP1z9D1N8Eu0vh52n9RNmQv-3iIVCOdD9xkA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آسوشیتدپرس: آمریکا در حال تکمیل خروج نیروهایش از عراق تا ۳۰ سپتامبر است و یک مقام نظامی آمریکایی گفته صدها نیروی باقی‌مانده در شمال عراق عمدتاً به اردن و دیگر کشورهای منطقه منتقل خواهند شد. تجهیزات نظامی، از جمله سامانه‌های پدافند هوایی نیز از عراق خارج می‌شوند. روز گذشته گزارش داد یک کاروان تجهیزات سنگین آمریکایی شامل خودروهای زرهی و کامیون‌های نظامی در غرب عراق مشاهده شده که در حال انتقال به سمت اردن بوده است. جزئیات دقیق نوع تجهیزات و مقصد نهایی آن‌ها هنوز به‌صورت مستقل تأیید نشده است.
یک مقام نظامی آمریکایی گفته خروج از شمال عراق «ریسک ما را برای عملیات‌های پیشرو کاهش می‌دهد».
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23444" target="_blank">📅 10:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">مجلس نمایندگان آمریکا با رأی ۲۵۲ موافق در برابر ۱۵۴ مخالف، اصلاحات سنا در طرح «قانون تحریم روسیه و ایرانِ لیندسی اُ. گراهام در سال ۲۰۲۶» را تصویب کرد. در این رأی‌گیری، ۱۹۷ جمهوری‌خواه، ۵۴ دموکرات و یک نماینده مستقل رأی موافق دادند. در مقابل، ۶ جمهوری‌خواه…</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23443" target="_blank">📅 10:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک مقام سعودی در قبال تحولات یمن در گفت‌وگو با شبکه ۱۲ تلویزیون اسرائیل: «از سوی پاکستان یا ترکیه چیزی جز اظهارات نرسیده و هیچ همکاری‌ای صورت نگرفته است. آنها فقط می‌خواهند سلاح بفروشند.»
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23442" target="_blank">📅 09:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a920abf92.mp4?token=N2b9PQn3oL6eBh3aKVBZJ47iOzWUFw9jCgcXQRHYHmnQvBYoZoinlvEFNT5HVhUtjMKQnjb9P5oMpxsriy5i-iF2CG21ZtKc08DULaktQ9gKznpK_QGUalAI4uWABr8d4OG0HjP9Nv5PHQz6CLVueG6aSdxZAbupv-tn1biVbThy-B8NOb8ZFiNC_wln87piY1SHxSTVY19hYgorw5IKfx7y0KWOlBsUJ9QeLBe10o9LsDwRiZmFWfvZ7X3zlyQzmeUlJV5n4ppR4_0gvTwVh5Rd3XwRXj2Q5Ezm0I7WTyjQFXdHjTg_87r6pzczEOuL_-EFWUeciDr4BFZD3hQ8pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a920abf92.mp4?token=N2b9PQn3oL6eBh3aKVBZJ47iOzWUFw9jCgcXQRHYHmnQvBYoZoinlvEFNT5HVhUtjMKQnjb9P5oMpxsriy5i-iF2CG21ZtKc08DULaktQ9gKznpK_QGUalAI4uWABr8d4OG0HjP9Nv5PHQz6CLVueG6aSdxZAbupv-tn1biVbThy-B8NOb8ZFiNC_wln87piY1SHxSTVY19hYgorw5IKfx7y0KWOlBsUJ9QeLBe10o9LsDwRiZmFWfvZ7X3zlyQzmeUlJV5n4ppR4_0gvTwVh5Rd3XwRXj2Q5Ezm0I7WTyjQFXdHjTg_87r6pzczEOuL_-EFWUeciDr4BFZD3hQ8pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي:
فکر می‌کنم در نهایت پیروز خواهیم شد.
نمی‌دانم آیا از طریق یک توافق‌نامه باشد یا نه، اما ما از همین حالا در حال پیروزی هستیم. اما فکر می‌کنم در نهایت پیروز خواهیم شد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23441" target="_blank">📅 09:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a3d694c10.mp4?token=OKOKrRKcw_sbI5HSItOCIjHHUr2pzalchJ5ob3hy3gaebLf6NLrfKD7yt9WYifZN0osr8suVWJh2TDljP2_t0yzRRPrf2tqrWfPXTn-2AVjY4m6Tah7iRtvY_cKeoGiWLGiIhPV8k8Wz7_0xoKNhUzunj6bZnEFTG3aMz7H4WxQOvrBBAWYdJr-AkR-lmy5JgPr30OvPTB26kxNm_PJTjSpu0veo3OSScH4H-9bk_ZeGnk2pefotcDFeszgIf6Azyj_tgNizHfqwS7CQ6cAUv5dOQ3lrtgK5boB5fjzOVif4TZuvTpQXKU5Lq6Q_YKe4yVT8IIgqquWI1aQ3UKB1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a3d694c10.mp4?token=OKOKrRKcw_sbI5HSItOCIjHHUr2pzalchJ5ob3hy3gaebLf6NLrfKD7yt9WYifZN0osr8suVWJh2TDljP2_t0yzRRPrf2tqrWfPXTn-2AVjY4m6Tah7iRtvY_cKeoGiWLGiIhPV8k8Wz7_0xoKNhUzunj6bZnEFTG3aMz7H4WxQOvrBBAWYdJr-AkR-lmy5JgPr30OvPTB26kxNm_PJTjSpu0veo3OSScH4H-9bk_ZeGnk2pefotcDFeszgIf6Azyj_tgNizHfqwS7CQ6cAUv5dOQ3lrtgK5boB5fjzOVif4TZuvTpQXKU5Lq6Q_YKe4yVT8IIgqquWI1aQ3UKB1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي:
هر جا را در جهان نگاه کنید، ایران به عنوان بدترین کشور جهان شناخته می‌شود و مدت طولانی است که این‌گونه بوده است.
ما کار را انجام خواهیم داد. آن‌ها در وضعیت بسیار ضعیفی قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23440" target="_blank">📅 08:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f45e1be2.mp4?token=lCdA-X-ZEG0fAFUzA7VH82EnN_0tpbV1RshMv8PZVzSMxi-HbWD_9BGmpeANnU9LgBoKW-HR83yN1LtJYOvH9h23tMXpsU43Tt9mftQ61g6f4DtpQTloT-o1S2OdkpilCF6svuO1EJxKJlHKwQy26iV5GC6ntz0sBPRGjEmUSki80J2uke4OFO6UCLcto2CogQocJGfOKFI2OGO6aTk4OUnGA24WrrhSeHuQPagbLY6JaCcTtKfpc7sDJn8vw9AKjDrfLDJki1nbV1_U78XgzU6i6gWGnpKILneV4LTYw6RDYU4L6tM5i1qTkw87ydHUbhOvjxJLNA3UZTQCDLwZjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f45e1be2.mp4?token=lCdA-X-ZEG0fAFUzA7VH82EnN_0tpbV1RshMv8PZVzSMxi-HbWD_9BGmpeANnU9LgBoKW-HR83yN1LtJYOvH9h23tMXpsU43Tt9mftQ61g6f4DtpQTloT-o1S2OdkpilCF6svuO1EJxKJlHKwQy26iV5GC6ntz0sBPRGjEmUSki80J2uke4OFO6UCLcto2CogQocJGfOKFI2OGO6aTk4OUnGA24WrrhSeHuQPagbLY6JaCcTtKfpc7sDJn8vw9AKjDrfLDJki1nbV1_U78XgzU6i6gWGnpKILneV4LTYw6RDYU4L6tM5i1qTkw87ydHUbhOvjxJLNA3UZTQCDLwZjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره جمهوري اسلامي ایران:
فکر می‌کنم در حال فروپاشی هستند.
می‌دانید، اقتصادشان در حال حاضر در سطحی است که هرگز پیش از این ندیده‌اند. بدترین اقتصاد تاریخشان است.
تورم آن‌ها بیش از ۳۰۰ درصد است. به سربازانشان حقوق نمی‌دهند. به ارتششان حقوق نمی‌دهند. به پلیسشان حقوق نمی‌دهند.آن‌ها در آشفتگی هستند. خواهیم دید چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23439" target="_blank">📅 08:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رویترز:
قیمت نفت برای سومین روز متوالی کاهش یافت؛ برنت حدود
۱۰۴ دلار
و WTI حدود
۱۰۱.۲۰ دلار
معامله شد. کاهش نگرانی‌ها درباره اختلال طولانی‌مدت در صادرات عربستان، از جمله تلاش برای بازگرداندن بخشی از ظرفیت خط لوله شرق-غرب، عامل اصلی کاهش قیمت عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23438" target="_blank">📅 08:10 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با یاشار: اگر پرونده ایران در شورای امنیت به رأی‌گیری برسد، باید بین دو حالت فرق بگذاریم: اگر رأی‌گیری درباره یک قطعنامه معمولی و الزام‌آور باشد، روسیه یا چین می‌توانند با وتو جلوی تصویب آن را بگیرند. اما اگر رأی‌گیری از نوع رویه‌ای باشد، روسیه و…</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23437" target="_blank">📅 07:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=uIb5do5CBNrTD1S4hDPnq9Jz3cKWJfBO-UKTl2fI7MOBHywSkeZ4-C5dltnJM_NBAUJbWHgH2A0L4CAzMZjExZDuxR4su_sYIHyFAIyE6Zpzam2OwJIPnRk6E4Rbf_4BhnF-OrZq0euGYRQupy8zMKOJnBFYzSpA_VVe2sZ1DD0deYCQmVtENdqZwtgygmOiNC9kiS2ASI25pOsqcSGPr700hcwNrp-_GfFom2_H93dp0q4RzIzYtSfEmi2vAYp0iIUbs_MmV0NGyBdHM7HNaJMZXF1QwF53wG-Y8NAdhvTw5vn8IYoQGQ6gA9jrt_Ic0nTj43rkRcfKVvlwxI9VpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6a10ce6c.mp4?token=uIb5do5CBNrTD1S4hDPnq9Jz3cKWJfBO-UKTl2fI7MOBHywSkeZ4-C5dltnJM_NBAUJbWHgH2A0L4CAzMZjExZDuxR4su_sYIHyFAIyE6Zpzam2OwJIPnRk6E4Rbf_4BhnF-OrZq0euGYRQupy8zMKOJnBFYzSpA_VVe2sZ1DD0deYCQmVtENdqZwtgygmOiNC9kiS2ASI25pOsqcSGPr700hcwNrp-_GfFom2_H93dp0q4RzIzYtSfEmi2vAYp0iIUbs_MmV0NGyBdHM7HNaJMZXF1QwF53wG-Y8NAdhvTw5vn8IYoQGQ6gA9jrt_Ic0nTj43rkRcfKVvlwxI9VpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام یاشار جان زاهدان حدود ساعت 12 نیم بامداد امشب درگیری افراد مسلح شروع شد تا همین الان درگیرن صدا تیر میاد بین خیابون دانشگاه و دانشجو خیلی کشته دادن حدود 9 تا امبولانس فقط امده بود سر صحنه
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23436" target="_blank">📅 02:29 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر دفاع ایتالیا: ما کشتی‌های جنگی خود را مستقر خواهیم کرد تا از عبور ایمن در تنگه باب‌المندب اطمینان حاصل کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23435" target="_blank">📅 01:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است. بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23434" target="_blank">📅 01:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش حمله پهپادی رژیم به کمپ های کرد های عراق اطراف اربیل
شبکه المیادین از شنیده شدن صدای انفجار در منطقه «مصیف» واقع در حومه اربیل، مرکز اقلیم کردستان عراق خبر داد.
همزمان منابع غیر رسمی از به پرواز در آمدن هواپیماهای جنگی آمریکایی در اطراف این شهر خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/23433" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23432" target="_blank">📅 01:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23431" target="_blank">📅 01:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23430" target="_blank">📅 01:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MP_zSncOHJ00XsY2Xdpdb52I_fO0tKqgsmspCPpBCqeky0lz7Okb0Hm_O9oZcFNRakkRQ2d2b7lx2533tx4gbUOUjLn3mWEnKO3KKhYnXlwhBLWSxtQpWXYepEmrC1KyEtWAnkjR7wK90J0z9SsGyhem1mHtDSJBEKfc3yX6jUKS4eu1weoTZRm44MVRkUTuMCeufEHq1qULlDWplN2hNYJn_s4hYoLWUj-xkoMoHta9BnQBH7HPvMy43AWT6bB4oeet8BqwHmkMN4QXIZHP8FAAdi1iQpMNYwLddmBxt3v1Bo5aSC4-ccTTo-zV61DrcfcjaijKoeHoJWKh4gUE0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار: آیا حلقه اطلاعاتی آمریکا درباره شبکه‌های جمهوری اسلامی در حال گسترش است؟!   یکی از احتمالاتی که می‌توان درباره بازگشت برخی چهره‌ها و افراد ایرانی به کشور مطرح کرد، گسترش دامنه دستگیری‌ها و تحقیقات آمریکا درباره افرادی است که با جمهوری اسلامی،…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23429" target="_blank">📅 01:11 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23428" target="_blank">📅 01:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23427" target="_blank">📅 00:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">میدل ایست آی: دونالد ترامپ «وسلی هانت»، نماینده جمهوری‌خواه تگزاس، حامی سرسخت اسرائیل و از منتقدان شریعت اسلامی را به عنوان سفیر بعدی آمریکا در عربستان سعودی معرفی کرده است. هانت، افسر سابق ارتش آمریکا، پیش‌تر دو سال به عنوان افسر رابط دیپلماتیک در عربستان خدمت کرده بود. این انتخاب در شرایطی حساس برای روابط آمریکا و کشورهای خلیج فارس و همزمان با جنگ ایران و آمریکا و تشدید درگیری‌ها در یمن انجام شده است. انتصاب هانت برای نهایی شدن به تأیید سنای آمریکا نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23426" target="_blank">📅 00:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23425" target="_blank">📅 00:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پدافند شرق تهران درگیر شد ، اگه ادامه دار بود گزارش بدید</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/23424" target="_blank">📅 00:39 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSina</strong></div>
<div class="tg-text">داداش فکر کنم دارن تهران و میزنن
هم صدای جنگنده اومد هم صدای انفجار شیشه‌های خونه ما لرزید مادرم از ترس رفت پایین
شرق تهرانم</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/23423" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSemiramis</strong></div>
<div class="tg-text">پدافند پاسداران داذه همینجور میزنه</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23422" target="_blank">📅 00:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پدافند تهران فعال شده و صدا ناله های شاش قاسم میده همه ترسیدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23421" target="_blank">📅 00:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23420" target="_blank">📅 00:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23419" target="_blank">📅 00:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/23418" target="_blank">📅 00:22 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23417" target="_blank">📅 00:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23416" target="_blank">📅 00:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23415" target="_blank">📅 00:08 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">صدای ناله های تنگسیری از قشم شنیده میشه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23414" target="_blank">📅 00:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نه دیگه بهمن پنجاه و هفته
نه حرف برق مفت و پول نفته
نمی‌ذارم سر من هم بذارن
کلاهی که سر بابام رفته
شاهرخ
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23413" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23412" target="_blank">📅 23:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23411" target="_blank">📅 23:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/385ac22afd.mp4?token=qfwkeeQcau2KCb_6YAg8rnBXcAw9Ogti677R2gjogbEq_wpJ41_ID7Zh2FDWZQuTv72Brj3OMeKnaOj4y6066QXhmSk2JsskDiDzgaxyqsqXptUYIwslZ_FGsUKax32tlFzixVlLcjW-SAyYYuNslDChfiAjbfJyqUAlEfy3oedsl-7iopmvjCXAeb2BzgHG5DlNicCoK5hdAIPEEZ3peJ8lYmZ19K4kTNPUydx9RR7zxW2U0hf7OiHISBQ72W2OoAoPWY9-CHGCv378n6NeGHfXmbGW3dyROuzqY3Tn1JkOH-8SiQTHJqB-Vu_LRAYspUtpF-zQGOPlzMZrMGeYaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/385ac22afd.mp4?token=qfwkeeQcau2KCb_6YAg8rnBXcAw9Ogti677R2gjogbEq_wpJ41_ID7Zh2FDWZQuTv72Brj3OMeKnaOj4y6066QXhmSk2JsskDiDzgaxyqsqXptUYIwslZ_FGsUKax32tlFzixVlLcjW-SAyYYuNslDChfiAjbfJyqUAlEfy3oedsl-7iopmvjCXAeb2BzgHG5DlNicCoK5hdAIPEEZ3peJ8lYmZ19K4kTNPUydx9RR7zxW2U0hf7OiHISBQ72W2OoAoPWY9-CHGCv378n6NeGHfXmbGW3dyROuzqY3Tn1JkOH-8SiQTHJqB-Vu_LRAYspUtpF-zQGOPlzMZrMGeYaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نِتانیاهو درباره ایران: ما تومور را از بین بردیم و اکنون زنده هستیم. این بدان معنا نیست که تومورهای دیگری برای مقابله وجود نخواهند داشت!
@WarRoom
💥</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23410" target="_blank">📅 23:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23409" target="_blank">📅 23:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23408" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23407">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMMAJI_Ry4nM6BzvO8XoZtwcvIwokCiLPM-heWh_MAawCE_0Hd137MHs-COFqdmL5yzSEqqMjdscjURhcux3IQ764_k0UGluOa3h3dpg1KG6ZgltNVF4oKn5_0YvVI2_C8Sgy2nZ8j2k5ZaOw3dejHDeKfAhQFP_XEYj4A18o3xoR7GDYMGOruBP938zVHc-01O3zWgAnCoHP8TfsFnjEIaUJ7iaCm9fsrpRM_Y-l7AQuUOKRTqRI8dISGDiYjagE63ELuMXeUhUZZ8PR8dEyZCAM2ka7B_3wa21BW3ILIElW0d7H-mggQlkYa6x9zGkO8Skv-7tJO016_wdMYlomQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23407" target="_blank">📅 23:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23405" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">page2 :
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23404" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شبکه کان اسرائیل : کویت و اسرائیل در حال انجام مذاکراتی سری به دلیل حملات ایران به کشورهای منطقه، از جمله خود کویت هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23403" target="_blank">📅 23:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23402">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5129cb70.mp4?token=cgmK_Gdm7gn1EZmZgdTcMkhDG9rXbAQtmkqtdqZ-MQ0ENTDzpJufbc7FC-xyQRruHgjV-BpOovCKTqOuWsJ96xrC8G7eweKkb5X9l8O179Qeh3-A7rdPFxl1B1xg_4oDMt-aHMn2N58GGD5sHC-YKKpsdfNzbDh3FrN9fMLviOSIAX9_Hmdv3-krAA0tsq_BkYnmT_cSInU3vn5BwoTZ_qD5u7cqKa1DoI7nzFxyt6IV15-TosRxKJwXTPaWkj2aYmslqqXHTbVQQT3vMo4yLdlZkBvhElolQ-TDnhx6EJAI1RsEBIfZ1_V-jAGHiKyCsyH6LXHbCzheD26LooECtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5129cb70.mp4?token=cgmK_Gdm7gn1EZmZgdTcMkhDG9rXbAQtmkqtdqZ-MQ0ENTDzpJufbc7FC-xyQRruHgjV-BpOovCKTqOuWsJ96xrC8G7eweKkb5X9l8O179Qeh3-A7rdPFxl1B1xg_4oDMt-aHMn2N58GGD5sHC-YKKpsdfNzbDh3FrN9fMLviOSIAX9_Hmdv3-krAA0tsq_BkYnmT_cSInU3vn5BwoTZ_qD5u7cqKa1DoI7nzFxyt6IV15-TosRxKJwXTPaWkj2aYmslqqXHTbVQQT3vMo4yLdlZkBvhElolQ-TDnhx6EJAI1RsEBIfZ1_V-jAGHiKyCsyH6LXHbCzheD26LooECtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد بزرگ شطرنج ، نتانیاهو: من مسیح نیستم و(کینگ) پادشاه هم نیستم. پادشاه نیازی به انتخابات ندارد؛ من باید انتخاب شوم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23402" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e1019a561.mp4?token=GmCF6AmsltUKJdvU0LESnAxmxJg5SBYA5cguKwAKZVdLz_a8ori7kKEdeQCIhSHgO5--60FMrEZXc4Q7XLQOujYx7l37Jfwy-oDiZAY36WTZJ34K64-Gs_xrmINlfURY9irb1l9hI6HJqn3DgQMrVSHjAUKWth55w3cACxpfk20nmtY-Vas6xqMnLMABc7LXOuco1AAI9Sp_UeZyP9reaLFHA--qafC7l2gfA9t2PK2lg4eqSSfd1k_JkFRWeAkTfwwH-GF34yFhKhwHBa2sn0xQC71aaxx2MvAYj5P0JqUPasCUUJk2M9857Aeyl4jWvs0LqkcHktU9tg2dL5LLZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e1019a561.mp4?token=GmCF6AmsltUKJdvU0LESnAxmxJg5SBYA5cguKwAKZVdLz_a8ori7kKEdeQCIhSHgO5--60FMrEZXc4Q7XLQOujYx7l37Jfwy-oDiZAY36WTZJ34K64-Gs_xrmINlfURY9irb1l9hI6HJqn3DgQMrVSHjAUKWth55w3cACxpfk20nmtY-Vas6xqMnLMABc7LXOuco1AAI9Sp_UeZyP9reaLFHA--qafC7l2gfA9t2PK2lg4eqSSfd1k_JkFRWeAkTfwwH-GF34yFhKhwHBa2sn0xQC71aaxx2MvAYj5P0JqUPasCUUJk2M9857Aeyl4jWvs0LqkcHktU9tg2dL5LLZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره ایران: اول از همه، ما باید رژیم ایران را سرنگون کنیم. این مأموریت من است و این مأموریت اصلی ماست.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23401" target="_blank">📅 23:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDMfqzwFwOZF3OViHhOLZ9lNStKj1PxPL71-N64AvY3JGPqPkNZYqt4uYRvQvEpCJk4mqROgyMXs7N-oONwMqNkZABMKxs8m3l4L2GkgoyYHjVB7baSveqFT5cSdMQSuX5HqlJtjFWninsRF-o6Or0IAeWUSEj0XU2DQubWftroFs-Z0t49RQ0v89c3ApzshuoB1t6y24DEUhgCmgPW2po0mbzmmzrxHD0nhYZOFAQyWZTUH7PGJNLfbuOJ0IX25PNiegiPpBM95fwaNr3lekTQvj_1FoSPgwbnhtt6vG1v15ON3JJjNSoBXeU1EHpmmImZ97TP293A0sgN_u58rKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: گزارشی از یک حادثه امنیتی در تنگه هرمز، در ۱۶ مایلی دریایی شمال شرقی خصب در عمان دریافت شده است.
بر اساس این گزارش، هیچ خسارتی به کشتی وارد نشده و هیچ‌یک از خدمه نیز زخمی نشده‌اند.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23400" target="_blank">📅 23:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش پرتاب موشک‌‌ از لارک به سمت تنگه.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23399" target="_blank">📅 23:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تنگه صدای ناله های مرحوم تنگسیری ‌میاد
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23398" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا اعلام کرد صرافی رمزارزی «بیت‌بانک» متعلق به شبکه مالی بابک زنجانی است. بر اساس اعلام خزانه‌داری آمریکا، بیت‌بانک تحت کنترل بابک زنجانی قرار دارد و شرکت «پیشتاز سیمرغ تجارت الکترونیک» نیز به‌عنوان توسعه‌دهنده نرم‌افزار این صرافی معرفی شده است. آمریکا در همین ارتباط بیت‌بانک و افراد و شرکت‌های مرتبط با شبکه زنجانی را تحریم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23397" target="_blank">📅 22:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یک مقام آمریکایی: برای ایران ویزاهایی جهت حضور در نشست‌های سازمان ملل صادر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23396" target="_blank">📅 22:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نتانیاهو: ما کار این رژیم را تمام خواهیم کرد ، به‌زودی غافلگیری‌ای در انتظار ایران است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/23395" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نتانیاهو در کنفرانس حزب لیکود، روایت ترامپ را تکرار کرد: ما اسرائیل را از نابودی نجات دادیم، و اگر این اتفاق نمی‌افتاد، احتمالاً کشور اسرائیل وجود نداشت.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23394" target="_blank">📅 21:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تایمز اسرائیل
: سه میلیارد دلار بمب تخریب گر در راه اسراییل برای دور جدید حملات.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/23392" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تحریم‌های تازه آمریکا علیه یک صرافی رمزارز و کوبا
آمریکا پلتفرم ارز دیجیتال «بیت‌بانک» را به اتهام همکاری با ایران تحریم کرد.
واشنگتن همچنین تحریم‌های جدیدی را علیه کوبا اعمال کرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23391" target="_blank">📅 21:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ :تصمیمات آتی را با 6 کشور عربی خلیج فارس و اعضای شورای امنیت سازمان ملل بررسی خواهیم کرد.امیدوارم ناتو از فاز بی مصرف بودن خارج شود وگرنه دیگر برای آنان هیچ هزینه‌ای نمیکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23390" target="_blank">📅 21:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">واشنگتن با فروش احتمالی ۴۸ فروند جنگنده از نوع F-35 به عربستان سعودی موافقت کرده است. ارزش این قرارداد حدود ۲۴.۳ میلیارد دلار تخمین زده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/23389" target="_blank">📅 21:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سی‌بی‌اس
: سپاه پاسداران انقلاب اسلامی در روزهای اخیر، حداقل دو فروند از هواپیماهای بدون سرنشین مدل MQ-1 متعلق به آمریکا را سرنگون کرده‌اند، اگرچه هنوز مشخص نیست این حوادث در کجا رخ داده‌اند و کدام مدل خاص از این هواپیما درگیر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23388" target="_blank">📅 21:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ به آکسیوس : می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم @WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23387" target="_blank">📅 21:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed20696f0.mp4?token=dWIJkvfEbYh55oJejorQ8mXuBxtLw_54OtmaU_Xv2Me_HW4sZ2FguSprGhYkOtiLH3PABnQjFSX1ZnJhc5IEcCLigb0EpwSlSOEmSBH8G1EF3ixsuepvUktTtrxLn2QP3jlMhR1rJftGmorqPZZMaz64jGJ4hZsANEC99MAKHlBWIiygwBMFrvEAd8PHhIUh1rZvQDYRrV9qScsQFcu418INRNVaEjYyQieqI958Ath-zQJiQWIugZRMF8_62usp5nt_53BKthL-ZQlN8-6wpSrxZzPzOXgjd76ZGvvo4aXILvb5OjhUhaSuCI0YxTFiGIGjRPM2hGHn_fVUr99ARw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed20696f0.mp4?token=dWIJkvfEbYh55oJejorQ8mXuBxtLw_54OtmaU_Xv2Me_HW4sZ2FguSprGhYkOtiLH3PABnQjFSX1ZnJhc5IEcCLigb0EpwSlSOEmSBH8G1EF3ixsuepvUktTtrxLn2QP3jlMhR1rJftGmorqPZZMaz64jGJ4hZsANEC99MAKHlBWIiygwBMFrvEAd8PHhIUh1rZvQDYRrV9qScsQFcu418INRNVaEjYyQieqI958Ath-zQJiQWIugZRMF8_62usp5nt_53BKthL-ZQlN8-6wpSrxZzPzOXgjd76ZGvvo4aXILvb5OjhUhaSuCI0YxTFiGIGjRPM2hGHn_fVUr99ARw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر شبکه فاکس‌نیوز از بمب‌های سنگرشکن و ۲۰۰۰ پوندی آمریکایی داخل ناو جورج واشنگتن تا دندان مسلح برای حمله به ایران
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23386" target="_blank">📅 20:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس به نقل از مقام آمریکایی: نیروهای آمریکایی مستقر در خاورمیانه برای احتمال یک درگیری تمام‌عیار با ایران در آماده‌باش هستند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23385" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23384">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامپ به آکسیوس : «آیا وارد شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»  @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23384" target="_blank">📅 20:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت: من در آستانه اتخاذ یک تصمیم مهم در مورد ایران هستم. @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23383" target="_blank">📅 20:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت:
من در آستانه اتخاذ یک تصمیم مهم در مورد ایران هستم.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23382" target="_blank">📅 20:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نماینده ویژه سازمان ملل متحد در سوریه: اسرائیل، تقریباً به صورت روزانه، در جنوب سوریه نفوذ می‌کند، موانع مرزی ایجاد می‌کند و با توپخانه شلیک می‌کند، همچنین بازدید نتانیاهو از نیروهای اسرائیلی در کوه شیخ، یک نقض دیگر از حاکمیت سوریه است.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/23381" target="_blank">📅 20:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23380">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نیروی دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در فاصله ۷۵ مایل دریایی شرق عدن در یمن دریافت کرده است.بر اساس این گزارش، یک قایق اقدام به تعقیب یک نفتکش کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23380" target="_blank">📅 19:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23379">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سنتکام: فرماندهی مرکزی ایالات متحده اعلام کرد که ارتش آمریکا در راستای اجرای محاصره دریایی و تضمین رعایت قوانین، تا امروز در مجموع به ۱۰۴ کشتی که در تلاش برای نقض این محاصره بودند، دستور تغییر مسیر داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/23379" target="_blank">📅 19:52 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
