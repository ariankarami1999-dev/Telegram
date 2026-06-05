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
<img src="https://cdn1.telesco.pe/file/pXiWUYCsxoWqaTIipfJKKcfVGdKrwT2vzF2ruRTL6HjSZgKwzrKfoTAHCkyVGwUo8AKxjwd0w0YjotjHgdx1imYaLO3UZBgwb47tCtQf55Y-pz1NFbApah9EYvczDdQzhlMxOAgWLy7bxD3msyqODiIaSpY1Zri0abX0-j2QHyoVvTcp_R-4xAolSzjjYL4xrt-wwIgs6TYz3NbwgNmjPNGW_XOwyXpYbnoa18uVVldrgDQ4pD96x9QSYKcOv0xfWOCtfSEj7dNjh67q7WuVu3u8w1-0GlZV8eUE5li9GWI9KyqYmh4YeCgcPeD86Oe_rJ_xygJLeZIfDXfixXualQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.33M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 03:13:42</div>
<hr>

<div class="tg-post" id="msg-75958">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C67yUJTaaG9XHFqiKOpHMqHmOT9FHtBKsbBvIHtNZCzbydxEs6oQ8hxhYIBocI7GMsx1HQJ3QSmlVuth3Z_HI6Ree9MSnERURg6ZGhsK5oTzY2AU4udKcbQd13t1ZmISZ-92rRBzB42ZM1jsBrwtvGqL2NjgOw_xBqLZ6ErpQLoUOJqx8E5uS_CGquKi2VAIONvdh7DXdg6tFbcHlD4A3g7m0rmEneCYz0atLCHnX7-5ODC36tHYPAT6Xx2ODafCZ9q4_Mu3E32ElLYlzKyrhxXPaRfHC35jwPOCwaaaFsjgf-EUONqGtyT7P1riPsZoQGgwIqYdaLWkYChqOpR00w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرماندهی مرکزی ایالات متحده (سنتکام)، بامداد شنبه، ۱۶ خردادماه، با انتشار بیانیه‌ای رسمی اعلام کرد که نیروهای ارتش آمریکا چهار فروند پهپاد انتحاری (یک‌طرفه) ایران را که به سمت تنگه هرمز پرتاب شده و تهدیدی فوری برای تردد دریایی منطقه به شمار می‌رفتند، سرنگون کرده‌اند. بر اساس این بیانیه، نیروهای آمریکایی متعاقب و با هدف دفاع از خود در برابر حملات بیشتر، سایت‌های راداری نظارت ساحلی ایران را در منطقه «گروک» و «جزیره قشم» هدف حمله قرار دادند. سنتکام در پایان با تاکید بر حفظ آمادگی کامل نیروهای آمریکایی افزود که واشنگتن برای دفاع از خود و پاسخ به «تجاوزات توجیه‌ناپذیر ایران»، در حالت آماده‌باش قرار دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/VahidOnline/75958" target="_blank">📅 02:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75957">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سیریک در هرمزگان
پیام‌های دریافتی:
پایگاه نیروی دریایی سپاه بندر سیریک  رو همین الان دوباره زدند. همون
لوکیشن چند روز پیش.
شهرستان سیریک صدای لانچ موشک ساعت  ۲:۱۴
سلام ساعت دو ده دیقه
پنج تا انفجار نیرو دریای سپاه سیرک هرمزگان
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/VahidOnline/75957" target="_blank">📅 02:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75956">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzjxAOe5kcLRgl7YNvrKwTo9V6ICcLpx7tlzxwdEtBAZOzi62rbChgsRDZaMAjqifUv8pmfSX7fiiTSVnmT-ElKUgBON78eIR9typDPUBiz-fmQgrYc--4V-dRPpmheMzPZ1YlConTePviY23xN1Th1simr90vaNFwQd2qbAIRx8_TJt17y0UDemCB-WiePDi-acCLMp1i1Bx9py8bh7AlMvxugzOjGMyaYPxAA9y0FpgakTAt57itsMXSQpfnMUySXAL1aQY0ipdHqbkSshb8aywcbWsZCWitl8xi3jp0ddQ4e5R1JjHRDmOONcY7L6WWC7OxIqohFztxLwQLINag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
وب‌سایت آکسیوس گزارش داده است که استیو ویتکاف و جرد کوشنر، فرستادگان دونالد ترامپ، روز پنجشنبه برای رایزنی با گروهی از کارشناسان فنی به آزمایشگاه ملی اوک‌ریج در ایالت تنسی سفر کردند.
به نوشته آکسیوس، کاخ سفید در تلاش است با ایران بر سر یک تفاهم‌نامه برای پایان دادن به جنگ و آغاز مذاکرات تفصیلی هسته‌ای «به توافق برسد» و می‌خواهد در صورت آغاز این مذاکرات، تیم کارشناسی لازم را آماده داشته باشد.
به گفته منابع آمریکایی و منطقه‌ای، تهران و واشنگتن همچنان بر سر برخی جزئیات این تفاهم‌نامه اختلاف دارند، اما مذاکرات وارد مراحل پایانی شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/VahidOnline/75956" target="_blank">📅 02:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75955">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XlWwuzeBH_ss6hPggUaomIqnXvrLuXfWX6cu-D7RB1cocNCSkAUpmIMNmG7zKnubXMd7168ysEBAog52XA6g_G_O9904Q1jVuAOHho5gt5LUoU2YIo4Epr_-WDvBbuJd_XcQv6h_mnaQkzh4Q3vnc8ShNKono4ALEELhuI_ZE8_r3_s1HzXaywbTobVeZ2jy6wgYzVbmY94KmK39pp93RfvNPxS9RwEORTkaW94CmPQb99Tq3R2Vjy_oG3J_bO63knx6_E-7ZrgxuODVCypyyWpF-dtQ9jIX2eK18c3vKOrllX5zUrIgT3FvpsdsBJ8aBwhfzyH4pz9qBcfhjBTCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مقام آمریکایی گزارش داد جمهوری اسلامی چندین پهپاد انتحاری را به سمت تنگه هرمز پرتاب کرد که هواپیماهای آمریکا دست‌کم چهار پهپاد را سرنگون کردند.
این مقام گفت مقام‌های آمریکایی گمان می‌کنند این پهپادها کشتی‌های تجاری در حال عبور از آب‌های منطقه یا نیروهای آمریکایی فعال در نزدیکی آن منطقه را هدف قرار داده بودند.
@
VahidOOnLine
ساعتی پیش‌تر اخباری درباره خارک و بندرعباس در بعضی منابع منتشر شده بود، خبرگزاری مهر میگه صحت ندارند:
جمعه شب خبرهایی مبنی بر شنیده شدن صدای انفجار و پدافند در جزیره خارگ منتشر شده است.
پیگیری های خبرنگار مهر مستقر در جزیره خارگ نشان می دهد، چنین خبری صحت ندارد.
بامداد شنبه برخی فعالین فضای مجازی مدعی وقوع درگیری‌ها و حملاتی به شهر بندرعباس شدند که بررسی‌های خبرنگار مهر نشان می‌دهد هیچ‌گونه درگیری در این شهر اتفاق نیفتاده است.
شلیک‌هایی در این منطقه صورت گرفته که جنبه اخطار داشته و کانون تحرکات در دریا و فراتر از جزیره لارک بوده است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/VahidOnline/75955" target="_blank">📅 01:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75954">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=jDCWJGN61j9GcrXbeF0O542RUSsqzvsnppBiDDrASmyoLm3FgejU0y9Hgp6MVbC2usf64zSscnn4UwVWIzYPwtEkw3FMHmRHkOf0qnEYihHoM3cA472NjDot8eycUSVqCt4sgZn1ms7fA--WA2tr6cbSUoAFlyKTKHLoLPN2N6WYfqQPUaJWzbDjxDIzn8iMKfLhVQomBsFjqZBaBJs45hdhh24dYSaHlGe_1MTGmDtgXSyVMXm_v-tQjYlTU3-ZBF79GcePnW2XyajvbHlDNCiIGK1DNd1dtuhzf3pidawwKQwf8GlnB7PRHGp982cit0VYmgwf2V3-m4DRpU-9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e4d85c72c6.mp4?token=jDCWJGN61j9GcrXbeF0O542RUSsqzvsnppBiDDrASmyoLm3FgejU0y9Hgp6MVbC2usf64zSscnn4UwVWIzYPwtEkw3FMHmRHkOf0qnEYihHoM3cA472NjDot8eycUSVqCt4sgZn1ms7fA--WA2tr6cbSUoAFlyKTKHLoLPN2N6WYfqQPUaJWzbDjxDIzn8iMKfLhVQomBsFjqZBaBJs45hdhh24dYSaHlGe_1MTGmDtgXSyVMXm_v-tQjYlTU3-ZBF79GcePnW2XyajvbHlDNCiIGK1DNd1dtuhzf3pidawwKQwf8GlnB7PRHGp982cit0VYmgwf2V3-m4DRpU-9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش امشب برنامه «خیابان انقلاب» به خاطر این حرف‌ها لغو شد
beehnam
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/75954" target="_blank">📅 23:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75953">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArHPvBajPoQQwxYi7NIuu37FISpe-3Fd42n2_kYoPRkwy7nQ8oydYoAq1XdCgfgf9hWIZ9oj4u9Dt_92EJbQBCCkruS7XxYEZktG2OJPodBvpzp0KG8smryzjvHE7jdGnKpJbbyj6a7SX39kMtV-dJ9qf3dx2v-W-V8ieIBIhoZyUDogU57A5rZrZZHxy39Hdei4dScbijPN-XRmzkfQRst3eW68dv2MAHXk12K8tyHuRkMchwaiXPMqY3dzWlpakUJw-O70JCBLGMNR-dof-auEZ-mJ1ZJK-SfdQ5qfmDCCsKAG9V7-Qj8LJJXnu_gnRhxk7kiWU92U2AMoXIpWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام کاخ سفید روز جمعه به خبرگزاری رویترز گفت که بازیکنان تیم ملی فوتبال ایران برای ورود به ایالات متحده و شرکت در جام جهانی فوتبال ویزا دریافت کرده‌اند.
تیم ایران قرار است نخستین دیدار خود در جام جهانی را روز ۲۵ خرداد برابر نیوزیلند در لس‌آنجلس برگزار کند. این تیم سپس در همان شهر به مصاف بلژیک خواهد رفت. بازی سوم در سیاتل مقابل مصر انجام خواهد شد.
@
VahidHeadline
آپدیت:
فارس، خبرگزاری وابسته به سپاه گزارش داد که ویزای برخی «اعضای کادر فنی و اجرایی» تیم ملی هنوز صادر نشده و سفارت آمریکا تاکنون از صدور آن «خودداری» کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75953" target="_blank">📅 21:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75952">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WShDeSZ9xQ2Ra5en6F_-se3g6SErpcmXUlyI5m-HeFXyINCQ6CXO1zswiZvfcLMuzSkAqTh5yoLnhsqbEATlGOS0hiZkb5ogOTD5ozZfDpPPoXUfo2lfceimzEMVPxDWnDyXdCkAnniuSUGq984KYixJQ3vY756O9aM1SbZuCyrS_WPVyJIYxTITZ4Y60F1VT1skx8_9YMMcUrRGLfcpZH2RCLgrF5kczgGwfEtqmiy8MhP-qdky_56S99aplCRQaralk9tzZqfoLiLDVUv964ZNVMXAW-TPLjQPpfaYtHIAU1KYPCVEDTDyLFGEwmgwqju6qxBDTwI4nPrIrkk5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسعود نبی‌دوست» خبرنگار خراسانی فعال در حوزه میراث فرهنگی با انتشار تصاویری خبر داد که کلیسای تاریخی انجیلی مشهد، از آثار ثبت‌شده در فهرست میراث ملی ایران، بامداد پنج‌شنبه ۱۴خردادماه۱۴۰۵ به‌طور کامل تخریب شده است.
رسانه‌های ایران از جمله «جماران» نوشته‌اند که تخریب این کلیسا «توسط عوامل ناشناس» و با استفاده از بولدوزر صورت گرفته است.
فعالان میراث فرهنگی می‌گویند این اقدام در سایه غفلت مسوولان میراث فرهنگی رخ داده، عملیاتی که حدود دو ساعت طول کشیده و صبح روز ۱۴خرداد نیز با بستن اطراف این کلیسا از ورود افراد و خبرنگاران جهت عکاسی ممانعت به عمل آمده است.
انگیزه، هویت افراد یا نهاد تخریب‌ کننده، مشخص نیست اما این نخستین بار نیست که یک بنای ثبت ملی شده تاریخی در ایران بدون اینکه نهادی مسوولیت آن را بپذیرد شبانه تخریب می‌شود.
کلیسای تاریخی انجیلی مربوط به دورهٔ پهلوی اول است و در خیابان جنت، کوچهٔ گلستان شهر مشهد واقع شده است. این اثر در تاریخ ۲۵ مرداد ۱۳۸۴ با شمارهٔ ثبت ۱۳۳۷۵ به‌عنوان یکی از آثار ملی ایران به ثبت رسیده‌ است.
پیش از این بارها بناهایی همچون کلیساها، آرامگاه‌ها و بناهای متعلق به اقلیت‌های مذهبی از جمله بهاییان، مسیحیان و یهودیان
تخریب‎ شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75952" target="_blank">📅 21:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75951">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امروز ۵ ژوئن ۲۰۲۶
قاضی فدرال آمریکا امروز حکم داد که تمام سیاست‌های تعلیقی USCIS غیرقانونی هستند و باید فوراً لغو شوند!
leeleehozak
چه خبر خوشحال کننده‌ای برای دانشجوهای ایرانی آمریکا، امیدوارم بزودی روند بررسی پرونده‌های USCIS شروع بشه و استرس و نگرانی همه تموم بشه
21aban
بلاخرررررره خبری که ماه‌ها منتظرش بودیم، اعلام شد.
طبق حکم دادگاه فدرال، پاز برای همه‌ی‌ افراد در داخل خاک آمریکا برداشته شد، از این لحظه به بعد دیگه
#USCISpause
وجود خارجی نداره، چون این بخشنامه از نظر دادگاه غیرقانونیه.
درود بر استقلال قوه قضاییه که زد کل بخشنامه اداره مهاجرت رو لغو کرد.
درود بر دموکراسی که در اون قدرت، چک سفید امضایی دست دولت نیست.
پی‌نوشت: احتمالا دولت درخواست تجدیدنظر بده و اعتراض کنه به این حکم اما خب دیر یا زود پرونده با پیروزی ما بسته میشه.
BrmTheGreat
این
لینک اصلی و رسمی حکم دادگاه
ه
اینم
لینک جزئیات بیشتر این شکایت خاص
ولی از یه منبع غیر رسمی
mozfang
جزییات تکمیلی:
دادگاه تمامی استدلال‌های دولت را که سعی داشت سیاست‌های جدید USCIS را از شمول بررسی قضایی خارج کند، رد کرد و رأی داد که:
واژه‌ی «امنیت ملی» نمی‌تواند سیاست‌های مهاجرتی قوه مجریه را به‌طور کامل از نظارت و بررسی دادگاه‌ها مصون کند.
قاضی رأی داده که هر چهار سیاست جدید چالش‌برانگیز، ناقض قانون تشریفات اداری (APA) هستند و به دو دلیل عمده غیرقانونی اعلام می‌شوند:
۱. مغایرت با‌ قانون (Contrary to Law): اداره‌ی USCIS از حدود اختیارات قانونی خود فراتر رفته است. دادگاه اشاره کرد که اختیارات مربوط به محدودیت ورود (موضوع بند 212(f) قانون INA) منحصراً متعلق به رئیس‌جمهور و مربوط به مرزهاست، نه مربوط به فرآیند پردازش مزایای داخلی برای غیرشهروندانی که قبلاً وارد خاک ایالات متحده شده‌اند. علاوه‌بر این، سیاست اعمال «عوامل منفی بر اساس کشور مبدا»، به وضوح ناقض اصل منع تبعیض بر اساس ملیت در قانون مهاجرت (موضوع بخش 1152(a)(1)(A)) است.
۲. خودسرانه و دمدمی‌مزاجانه بودن (Arbitrary and Capricious): این آژانس نتوانسته است استدلال منطقی برای اقدامات خود ارائه کند، منافع و انتظارات به‌حق مهاجرانی را که طبق قانون عمل کرده بودند کاملاً نادیده گرفته، و به دلایل ساختگی و بهانه‌جویانه (Pretextual) متوسل شده است. دادگاه به یک «عدم تطابق جدی» میان اهداف اعلام‌شده امنیت ملی و آنچه در واقعیت رخ داده اشاره کرد؛ از جمله اظهارات بیگانه‌ستیزانه همزمان رئیس‌جمهور و کریستی نوم (Kristi Noem) وزیر وقت امنیت میهن در شبکه‌های اجتماعی، و همچنین استثنائات خودسرانه‌ای که آژانس برای ورزشکاران جام جهانی/المپیک و پزشکان در نظر گرفته بود.
🟣
دادگاه رسماً هر چهار سیاست را غیرقانونی اعلام کرد و آن‌ها را به‌طور کامل ابطال و ملغی اثر نمود. از آنجا که این حکم یک دستورالعمل دولتی را ابطال می‌کند، عملاً اثری سراسری و ملی در کل کشور خواهد داشت.
🟣
دادگاه درخواست شاکیان برای صدور دستور منع دائمی را رد کرد و استدلال نمود که حکم ابطال و اعلام غیرقانونی بودن سیاست‌ها به خودی خود برای جبران خسارت شاکیان کافی است و نیازی به این ابزار فوق‌العاده نیست.
🟣
درخواست دولت برای رد ادعاهای اساسی شاکیان (مبنی بر نقض متمم پنجم قانون اساسی در خصوص رفتار برابر و رویه عادلانه) رد شد. دادگاه بر اساس اصل «اجتناب از ورود به مسائل قانون اساسی در صورت امکان»، اعلام کرد که چون پرونده بر اساس دلایل اداری (قانون APA) به‌طور کامل حل شده، نیازی به صدور رای در خصوص بندهای قانون اساسی در حال حاضر نیست.
این حکم به امضای قاضی ارشد، جان جی. مک‌کانل، رسیده و لازم‌الاجرا است.
منبع‌:
کانال مهاجرت به آمریکا
BrmTheGreat
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 273K · <a href="https://t.me/VahidOnline/75951" target="_blank">📅 19:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75949">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X2OvuP2w2rTGwreIXbF6VtTv6YtceiPKOyXarTHlqw5sXTSfOetW4npdaJpktyTBpczqsPZP_ljlq-YXtdbJ1Dvxi0s7w_lKylr_5YHOX_c8qBPm_kWCJYvh5-Ftj_JtpbQvLHE6aVNfT8J0oKKXCMUV0jdYCKsp4YHjVFWQQNgaX6oJrcgfnmSRe-DcAedYGBnI_e7xOjIv1_NPTDQVa15bpHrW6uj42Hfd11DJXmfIec3mVhSVF5aNYYho0X14i5hgCdSliSIMEeYlXB9OSTMF1i5UILI13FqoMG8MnB8nqMEVeVkXMrECyRzZxFzwGTW3YtipCwvoR6Z_XKoviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VJe2dW0iQoH-ZL6CaduwNkSiOzJoRmmOZrVUAhQGipSdx38275tKut_D_UjdLrQkg7qlnH-RhMFX0DDaqJaQXigmjpkRE1E6R1F2za8Gje06ljUXb1aFBvKtDpH-cbDcQcRfjVAwuOL0-cNcHq6oOrrEXAYNe7OwkX11knAhz4mZjBEwMrztT5Q5_7N8sq6J-7sshXC0drC_XgdE5WRmuCnn6DMJ28efuJlOhK3k3VzPHQkncMPF_B9KLF5cYnb5zxti0y7EOizJwj4iYxHLoXnVHxhCOhQXC-hJVmwqgDxtA2s5sVpyAcgwPBdBGt9sgon6Gywsz3Wc1wiot16jWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شبکه خبری الحدث، روز جمعه ۱۵ خرداد ماه به نقل از «منابعی آگاه» گزارش کرد تهران موافقتش با انتقال بخشی از ذخایر اورانیوم خود به یک کشور ثالث را به اسلام‌آباد اعلام کرده است.
بر اساس این گزارش، اصلی‌ترین اختلاف باقی‌مانده در مذاکرات میان تهران و واشنگتن به موضوع آزادسازی دارایی‌های بلوکه‌شده ایران مربوط می‌شود و نحوه و سازوکار آزادسازی این اموال همچنان یکی از شکاف‌های مهم میان طرفین به شمار می‌رود.
@
VahidOOnLine
خبرگزاری فارس، وابسته به سپاه پاسداران،‌ روز جمعه ۱۵ خرداد ماه به نقل از «یک منبع آگاه نزدیک به تیم مذاکره‌کننده ایران»، گزارش شبکه العربیه درباره موافقت تهران با انتقال بخشی از ذخایر اورانیوم غنی‌شده به کشور ثالث را تکذیب کرد.
خبرگزاری فارس به نقل از این منبع گزارش داد ادعای مطرح‌شده از سوی العربیه «نادرست» است و موضوع انتقال ذخایر اورانیوم در دستور کار فعلی مذاکرات قرار ندارد.
به گفته این منبع آگاه، موضوعات مرتبط با پرونده هسته‌ای در مرحله کنونی گفتگوها مطرح نیست و بررسی آنها به مراحل بعدی مذاکرات موکول شده است: «ابتدا باید طرف آمریکایی اقدامات مشخص و قطعی خود را انجام دهد و درباره برخی مسائل اساسی به توافق‌های روشن و نهایی دست یابیم.»
شبکه العربیه پیش‌تر گزارش کرده بود تهران موافقتش با انتقال بخشی از ذخایر اورانیوم غنی‌شده به یک کشور ثالث را به اسلام‌آباد اعلام کرده است و این کشور ثالث با توافق طرف‌های مذاکره‌کننده انتخاب خواهد شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75949" target="_blank">📅 18:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75948">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAeVWz8TnZAv5aTw00H3pBVCX18SXRhKIpTRzdJz4PUbHT4G6ve00WWGQo780DOEkL0fkF1j8rzQDtuMvu0p0CMu64_aJoHwJtZxT0OU_dFRzIg7K4f-Elm8cy1FRtUT9lbJtsdQv8CE-bl7KR1u1W7R77HExSpE1ZpVEfXqEIBViP-RVV4M9A0M5mrCKnKS14Yu4AEg99slN3Twtrg-UrqbnaIo2FGJw905Rx008SZ6tMrfCHCzcqXgDAXkSqHZNZrwqX09QksrTvAiaTAk0SqPfjkaZhu6i1IEWC-wEexbJt4ij35UcmlEpUF6o-TjcYWDWV9B0Pov51BaWix-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جوزف عون، رئیس‌جمهور لبنان، در مصاحبه‌ای که روز جمعه منتشر شد، از ایران خواست در امور لبنان دخالت نکند. او همچنین به گروه حزب‌الله، متحد مورد حمایت تهران، گفت که تنها راه‌حل درگیری با اسرائیل، دیپلماسی است.
او در این گفت‌وگو با شبکه خبری سی‌ان‌ان خطاب به ایران گفت: «این کشور شما نیست، کشورِ ماست... دخالت در کشور ما وظیفه شما نیست.»
آقای عون افزود: «آنها از لبنان به‌عنوان یک اهرم چانه‌زنی در مذاکرات خود با ایالات متحده استفاده می‌کنند. این غیرقابل قبول است.»
رئیس‌جمهور لبنان همچنین گفت: «حزب‌الله باید درک کند که هیچ راهی جز نشستن و گفت‌وگو وجود ندارد؛ هیچ راه دیگری برای حل این مشکل و نجات آنچه باقی مانده است، جز از طریق مذاکره و دیپلماسی وجود ندارد.»
حزب‌الله از سوی آمریکا به عنوان سازمان تروریستی شناخته می‌شود اما اتحادیه اروپا تنها شاخه نظامی آن را تروریستی می‌داند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/75948" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75946">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tTSuELwa5YXjA4qxabEuc-HdUYZ_ZRwmSfLHi_mRfhymdxHfANFzx2C_vLYnO1KcnXChMU4eHjnvoJcXFEzHIYbXpJyj4-uZn-SaFV3GPsmP8VviBVbOsrtMGOHysk1Su3CZA_ILoAvRLD13io_lO3Nxx1k7ejktqIvqFEYGIWga8bnsFCVl--XtqhdhLB36wM9H6hN1aMI-Q_vZx1GsavzE_PJPHj1_zCyiXGhF7xQKhIBNym_gAqoVfGs4nT8Uuh5aeQ8CY6LT9H0RV_4wz4IIusYk84kIc7Kaj59-rwCdPtVXgz7RJNv0JMK7Ln0zkx00SMvlMxBByS39_f5y-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=SyRps47ddL1lD5h3sdybkECDN8vGB1B48u_xVosNt1019Z8h9s8KYpJZfgKQKJbFPNfFJUAqb5RhNWQzK_R5W8fjPZ83QokmC6MmMX_bMVKWpZVareFuqJsYix6P0uNttej9Pk9VWK5UyQR9B9kMgxpWwHaf0xl4c3g_i2KSulzHbYmJ0MWbtzC8uvLHKBj4tQ0fS7SYAt6aqS4BTsIgb0JOJv4dqTMl_HHN2krJU8tAr37OpbaxnXLHRm90Qups49dDCMVV1k8zfwT9rhIZES-SJf0qJXb_LAuKPwg3fF-pTRKPQ0U0kVvxpueNzHEMybPJBe-cxm1X1XogvJ75hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03b8183b03.mp4?token=SyRps47ddL1lD5h3sdybkECDN8vGB1B48u_xVosNt1019Z8h9s8KYpJZfgKQKJbFPNfFJUAqb5RhNWQzK_R5W8fjPZ83QokmC6MmMX_bMVKWpZVareFuqJsYix6P0uNttej9Pk9VWK5UyQR9B9kMgxpWwHaf0xl4c3g_i2KSulzHbYmJ0MWbtzC8uvLHKBj4tQ0fS7SYAt6aqS4BTsIgb0JOJv4dqTMl_HHN2krJU8tAr37OpbaxnXLHRm90Qups49dDCMVV1k8zfwT9rhIZES-SJf0qJXb_LAuKPwg3fF-pTRKPQ0U0kVvxpueNzHEMybPJBe-cxm1X1XogvJ75hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستاد فرماندهی مرکزی ایالات متحده، سنتکام، ادعای ارتش جمهوری اسلامی درباره شلیک موشک و پهپاد به سمت ناوشکن‌های آمریکایی در دریای عمان را تکذیب کرد.
رسانه‌های ایران روز جمعه به نقل از ارتش اعلام کردند که نیروی دریایی آن به عنوان «اخطار» به سمت دو ناوشکن آمریکایی «موشک قدیر و پهپادهای تهاجمی جدید» شلیک کرده و این دو ناوشکن دریای عمان را به سمت اقیانوس هند ترک کردند.
سنتکام که فرماندهی نیروهای نظامی آمریکا در خاورمیانه را برعهده دارد، ساعتی بعد در شبکه ایکس اعلام کرد: «نیروهای ایرانی به ناوهای جنگی نیروی دریایی آمریکا حمله نکرده‌اند و به سوی آنها آتش نگشوده‌اند. انجام چنین اقدامی نقض آشکار و فاحش آتش‌بس محسوب می‌شد.
در این اطلاعیه بر ادامه محاصره دریایی ایران که از اواخر فرودین آغاز شد، تأکید شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/75946" target="_blank">📅 18:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75945">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTehDdxnMln3etsx70yxebAyPwVHWlX59vxhv3-U-zR6yJ2cb3imIaBX5l21UPG1JKeAZf07FbLWHTw5j4MjO87gFauvzHqxSGcCTtvGPj0wcYUB7dZ1UdxR1m3m1NiE4QSAdR3Qu_h3uSQ8Nvam5SMHq2eLInXQvxBAtS1cVqYXNl6UxktNzA3hzVyrcD8N7aYc1lJ3KN2QZ_DVJyuh5l151bR4UJmaephuarsidShYXOpSTCF-IkdYv3LPG8y4uD5G1jmbThjX53BL4IFARKi9YTCR1cAOuLl0kDryn1WCHzMT8hvnhNEh9_erhsYES7DmyiTB_DIu8QL1gXLv8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کمالی، از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه ۲۶ دادگاه انقلاب تهران به اتهام «محاربه» به اعدام محکوم شده‌است.
رسانه‌ حقوق بشری هرانابا اعلام محکومیت علی کمالی به اعدام، نوشت این حکم در حال حاضر در دیوان عالی کشور تحت بررسی قرار دارد.
به‌گفته هرانا شعبه ۲۶ به ریاست ایمان افشاری در اواسط اردیبهشت سال جاری حکم را صادر کرد. کمالی که دارای اقامت مالزی است، ۲۲ دی‌ماه ۱۴۰۴ در تهران بازداشت
شد و اکنون در زندان تهران بزرگ نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 250K · <a href="https://t.me/VahidOnline/75945" target="_blank">📅 18:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75944">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G8EvJ3Mz-A5wzFmQxWXib8lBioQSqht3_ZcAUpBv5oacVYGyvcpa8WwcHK09tZdnUnUK4XPb3f567uPHYQB30Lef8MtZyfZWkM2gamqibcJShR67mUZm3BP7dxMm2zcFl4XdP7cellpzty4jVDpanN8YCdya9FUMw0IPv9Qb8Gl8MsoH2bT_AvF2V2Ht4UuzBOg1DrwCwMJ34VYUvjSls3tImTQAAwM9XaZ-w1Tqws1JnczCXSwlAmRDMrGqhr8cFQloTtvdhzlS3-yLAhuGa41XFMHxkC8bHZiSJ401oZEmW_5rv-ffs5GzMhjoz8FMLrpe7pAsrhgWDF_hNK6Fjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رویترز به نقل از دو منبع در روز جمعه گزارش داد که پایانه نفتی مینا الفحل در عمان پس از وقوع یک انفجار در نزدیکی اسکله‌ها، عملیات بارگیری نفت را متوقف کرده است. به گفته این منابع، انفجار ظاهراً در پی یک حمله پهپادی رخ داده است.
@
VahidHeadline
AJENews
هنوز مشخص نیست این حمله دقیقا چه زمانی روی داده است.
بر اساس داده‌های کشتیرانی ال‌اس‌ای‌جی، روز جمعه چند نفتکش بسیار بزرگ در نزدیکی این بندر لنگر انداخته بودند.
رویترز در ادامه
نوشته
:‌ رسانه‌های دولتی ایران روز چهارشنبه گزارش دادند جمهوری اسلامی یک کشتی نظامی آمریکا را که «مرکز کنترل و فرماندهی» توصیف شده بود، هنگام نزدیک شدن به آب‌های سرزمینی ایران در دریای عمان هدف قرار داده است، اما ستاد فرماندهی مرکزی آمریکا، سنتکام، این گزارش‌ها را رد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 352K · <a href="https://t.me/VahidOnline/75944" target="_blank">📅 06:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75943">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hvM6Xxd4RmNdYQId4DRMkwMxw26L4iLxY59PZHm3ynNnfNY4CcI-mTg_2Jf-Dn53Le3HiFjQV0q_Kl4pi-9_eXEv0PFLbTkfgu2N2A6GC4vGY9UHCJDQmGlvm3E6wgROjWRqje7vjmpWkrSKr1UnjBCUYkQ_RazXe5lzZGaYWUSNfmIIhA2S-rWRHUmbVzdEo3QdyqhFLbJgGNTj9WxO1ku0yl3DTOk34nKHABA1KYt40-1De9Lhwk4ogxfNzDzg4QPHKpCR_NAIU4xq9BJuyBVpuzcqEbVQ5u6Y04cPbigiZ90ATQl7j72LGNQGfwPl0iNAJQu_qEK3-dMmdsQnJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: ایران نباید سلاح اتمی داشته باشد
دونالد ترامپ، رییس‌جمهوری آمریکا، در کاخ سفید در پاسخ به این که اگر حکومت ایران نیروهای آمریکایی را بکشد، آیا جنگ با جمهوری اسلامی را از سر خواهد گرفت، گفت: «این دلیل خوبی برای چنین کاری خواهد بود. اگر آن‌ها نیروهای آمریکایی را بکشند، فکر می‌کنم خیلی سریع دست به این کار بزنم.»
ترامپ درباره جمهوری اسلامی تاکید کرد: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند.»
رییس‌جمهوری آمریکا گفت: «ما برای به‌دست آوردن اورانیوم غنی‌شده آن‌ها به توافقی با ایران نیاز نداریم.»
او درباره کمک ناتو به بازگشایی تنگه هرمز نیز گفت: «ما به آن‌ها فرصت دادیم که کمک کنند، اما نخواستند کمک کنند. این موضوع برای آن‌ها بسیار پرهزینه خواهد شد، چون نباید چنین کاری می‌کردند. باید کمک می‌کردند.»
🔻
ترامپ درباره جنگ: چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد
دونالد ترامپ، رییس‌جمهوری آمریکا درباره جنگ ایران گفت: «چه از نظر نظامی و چه روی کاغذ، ما پیروز خواهیم شد. بخش اصلی این است که تنگه فورا باز خواهد شد.»
ترامپ افزود: «آن‌ها (جمهوری اسلامی) هیچ نیروی دریایی ندارند، هیچ نیروی هوایی ندارند. ما آن‌ها را نابود کرده‌ایم.»
او ادامه داد: «رهبری‌شان را از بین برده‌ایم و تقریبا همه آن‌ها را نابود کرده‌ایم. بعد در رسانه‌های جعلی می‌خوانید که آن‌ها در جنگ خیلی خوب عمل می‌کنند. واقعا باورنکردنی است. ما هر چیزی را که می‌شد نابود کرد، از بین بردیم.»
🔻
ترامپ: حکومت ایران درباره توان و اراده آمریکا دچار اشتباه محاسباتی شده است
دونالد ترامپ، رئیس‌جمهوری آمریکا، در نشست کابینه در کاخ سفید با اشاره به مذاکرات جاری و وضعیت تنگه هرمز گفت یکی از محورهای اصلی توافق، بازگشایی فوری تنگه هرمز برای عبور و مرور کشتی‌ها است و تأکید کرد آمریکا «هم در میدان نبرد و هم در عرصه دیپلماسی» پیروز خواهد شد.
رئیس‌جمهوری آمریکا مدعی شد توان نظامی جمهوری اسلامی به‌شدت تضعیف شده و گفت: «آن‌ها دیگر نیروی دریایی و نیروی هوایی مؤثری ندارند. ما تقریباً همه توان نظامی و ساختار رهبری آن‌ها را نابود کرده‌ایم.»
او در پاسخ به پرسشی درباره احتمال ازسرگیری جنگ در صورت کشته شدن نیروهای آمریکایی توسط حکومت ایران گفت چنین اقدامی می‌تواند دلیل کافی برای اقدام نظامی جدید باشد و در آن صورت آمریکا «بسیار سریع» واکنش نشان خواهد داد.
ترامپ همچنین درباره ذخایر اورانیوم غنی‌شده ایران گفت آمریکا در مقطعی گزینه خارج کردن این مواد را بررسی کرده بود، اما به دلیل نیاز به حضور طولانی‌تر نیروهای آمریکایی از این طرح صرف‌نظر شد. به گفته او، واشینگتن همچنان توانایی دسترسی به این مواد را دارد.
وی افزود آمریکا با استفاده از سامانه‌های پیشرفته نظارتی و امکانات فضایی، تمامی مناطق مورد نظر را به‌طور کامل زیر نظر دارد و هرگونه تحرک را رصد می‌کند.
ترامپ درباره احتمال دیدار با مجتبی خامنه‌ای نیز گفت شخصاً تمایلی ندارد و چنین پیشنهادی را هم مطرح نکرده است، اما اگر چنین دیداری انجام شود، با احترام برخورد خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/75943" target="_blank">📅 00:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75942">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OpODWKC5etyBGk0b5BKhE0MGccAG396tRP7-oHmppWudBtfXwImMWQpRPRt_8PTRa8De6SueENrAGOMmdXRtnoW6Fq6VVoGYtWgrwLxbgV_nBq0gG92Hx_15wYUeuFucgk9H-AeAESV9gk1ApoZgcQjIUavHTv2OUFfMuXuVEmw5XD3phABvQpd8qmkOdQ3R0UtkIwoGWd3IEV_qogajfk5xK6lvqLD1vwrGo0CSEM97Z7qsFDCmYVZPgBLXS4_yFflQ8IWa1mAELiO3bSDLhHcgPTzKjnqG3QdNG03tRuWIxcKfskaQ_gvuV-P4iwD_vuE7ly9BVzXrM9sQ-aRU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العربیه پنجشنبه شب ۱۴ خردادماه، به نقل از منابع اختصاصی گزارش داد محسن نقوی، وزیر کشور پاکستان، برای پیشبرد مذاکرات میان جمهوری اسلامی ایران و آمریکا به تهران سفر می‌کند.
به گفته این منابع، سفر نقوی در چارچوب تلاش‌های میانجی‌گرانه اسلام‌آباد میان تهران و واشنگتن انجام می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75942" target="_blank">📅 00:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75941">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g1SxIzXmuysQ59FiJLpi74i7w6lyYno0jEahyojyxZ1Spww2L4LBBOE3oiquV5cExyFNGurFgvU_CipRLbHesRTXB7eSFQIqgdnhtkBJxVXbP9Cf4NfHneJfvo1LUXOq9y2ACVjvOIfx18zpV9jmsS8HjZF3U8ueR7XZ6rcjZ4yy34ynwcK9RHLIfC-dTMVQ9o_aIrLdPDjeFiv6qWoBMTR6KX3u_oXytIdLJADEXwGrBKKYwFTPgx3rocSSBicDlZ_qnzoZ-5X-WG2HO3VzvjPtN09TrVGAauWBO20rYcSAK3SIOcnIZY5EYTRU66uVnZkX_Ge5JHR5A0bo84ryzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، روز پنج‌شنبه گفت ایالات متحده بر جمهوری اسلامی غلبه می‌کند، یا با توافق یا با عملیات نظامی.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75941" target="_blank">📅 00:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75940">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnZJOllE-XRPsTwckgltPsZb-kIKXQgWOlnqb2xIwSaY2tCByrkyxLS2S8djAI_SpsGrvDWPL3Pg9M_dToquKB-P2HrMg74a2aXxeaUMK21Xcv7R4v9j7jy0PzWCytCQl_OL6M7eaZx1QGj1QUw14bnJ0Sq22i_TtWkCAdBdY4S8XSJMDQ8g_FvU5RDqkgS6ZRmV9qhbIYTr92lNZnLl5U1VzDz5fmuu6Xb8r7saOT6B6SB-bhEit4KDt-EfHbKZfMSrYe1o6CmFecJlPe5aB3mLqMIbEZTVRND2to-zAsA-J6PdHxfr5puYf_4GzEM1JOWVrals3KrUVc9LaTra5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پنج‌شنبه ۱۴خرداد۱۴۰۵ در گزارشی به کشورهای عضو، بار دیگر از جمهوری اسلامی خواست «به‌طور فوری» درباره سرنوشت ذخایر اورانیوم غنی‌شده خود پس از حملات سال گذشته آمریکا و اسراییل به تاسیسات هسته‌ای این کشور توضیح دهد.
در این گزارش همچنین از مقامات جمهوری اسلامی خواسته شده تا زمینه ازسرگیری کامل بازرسی‌ها را فراهم کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75940" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75939">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qn9Z1SHVuqqXlSHUEZNutWii2LWJov9p7sp6eP9rNtcayGwbzORPiQf6_n2zD6qiXqJ-lyVjCCyobrkyBNAbU5p8vCAJ--ViriwPHmL6y0tHjQBuWJ7gIBIvY6dPjvyE39WUoVtmAlUKvhBD91Fi_dJU83lfdSlG3p0Lf8kFrxXvSLlDD0lyQs5mhGPZTQEeSQS2ve_8-ECm03pwThOqliFLsy-RFjmlOQL5s2sFFp27bcXC8j9WO2Ywwk1nkbWN23TnkZ6fhOAmL4_4Sw8wEpXX-dhWg6tRD6EOSMBGv7uf7pw_BGuNgliLCE1jZ0WbBPycNosO2oaRd4wIDHbE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل گروه حزب‌الله طرح آتش‌بسی را که دولت‌های لبنان و اسرائیل در مذاکراتی با میانجی‌گری آمریکا بر سر آن توافق کرده بودند، رد کرد.
ایالات متحده روز چهارشنبه اعلام کرده بود که لبنان و اسرائیل بر سر اجرای یک آتش‌بس به توافق رسیده‌اند؛ توافقی که مشروط به توقف حملات حزب‌الله و خروج نیروهای این گروه از مناطق مرزی جنوب لبنان است.
@
VahidHeadline
نعیم قاسم، دبیرکل حزب‌الله لبنان، توافق دولت لبنان با اسرائیل که با میانجی‌گری آمریکا تدوین شده است را «تسلیم و شکست تمام‌عیار» توصیف کرد و گفت حزب‌الله تنها به توقف کامل حملات، آتش‌بس و خروج اسرائیل از خاک لبنان متعهد است.
او همچنین خلع سلاح حزب‌الله را به معنای از بین رفتن قدرت لبنان دانست و تاکید کرد این موضوع برای حزب‌الله قابل پذیرش نیست.
پس از توافق آتش‌بس میان اسرائیل و حزب‌الله لبنان، آمریکا برای حل‌وفصل اختلافات مرزی و مسائل امنیتی میان دو طرف نقش میانجی را بر عهده گرفته است. در همین حال، موضوع خلع سلاح حزب‌الله و نحوه اجرای آتش‌بس همچنان از مهم‌ترین محورهای اختلاف میان دولت لبنان، حزب‌الله و اسرائیل به شمار می‌رود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75939" target="_blank">📅 16:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oNexD75gO0JmwXApD-uqdu25HDIF2OU_uYoT4BzmrRX568KN1F7RK_qcHiXZTWboLS95QDy1ZbXW8bAynF6-CF6rZH-BBSoFkFBW-JGc39IULNliTjGlTMEbNkNhBufy0yqcevGco5UdIsX-ky5wq9wrU85qLN5Q4v0L0hQlbcgva9SuNngw_jrdcRDSK9gzB-iRW3m2aNtohVidgf_hkOKRwJNfcvpAeDcqXYDN1jD7xqtUaeCc87i5Owh_c2xAbZGHYcqNE99IY1qt8PCbV4uuVG136t4WqF17RqpUDFWbcEwRF5hGIt8DhEAUnfHXx5IZZzEJDVnWTknnU3sw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران روز پنجشنبه ۱۴ خردادماه و ساعاتی پس از انتشار ویدیوها و تصاویری از برخورد پهپاد سپاه به فرودگاه بین‌المللی کویت، به نقل از یک منبع نظامی، آن‌ها را «تصویرسازی دروغین دشمن» خواند.
این منبع نظامی به تسنیم گفت:‌«پرتاب پهپادهای هوافضای سپاه به سوی اهداف آمریکایی در کویت، در نیمه شب و اصابت هم در نیمه شب (و در تاریکی هوا) صورت گرفته است درحالی که در فیلم و عکسهای ادعایی که از پهپاد در فرودگاه منتشر شده، هوا کاملاً روشن و مربوط به روز است.»
سپاه پاسداران پیش از انتشار تصاویر برخورد پهپاد با پایانه مسافربری شماره ۱ فرودگاه کویت ادعا کرده بود که موشک‌های سامانه ضدهوایی آمریکا به این محل برخورد کرده بودند.
این منبع نظامی که نامش فاش نشده به تسنیم گفت:‌ «فاصله «هدف» پهپادهای هوافضای سپاه تا فرودگاه کویت بیش از ۴۰ کیلومتر است و این نیز نشان می‌دهد که اصابت به فرودگاه کویت ارتباطی به پهپادهای ایران ندارد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 314K · <a href="https://t.me/VahidOnline/75938" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q2bSnfElviYkNDWDY0lPA0zH5zfgpKYHypw6nBh1fYM4SDnXomFUoQk9EiCmBij3VNmUF4UAnVKBpQeNaM82AHBhJcfH_lD8g2ndXbKh48vfWIOV8g2M6FjAZVs1TlShK1tgqvFLTmHIx3xUOzjLg2zx_Vc3too7PK96afgEy1zq_gOxczPzAuxhRJyUQDs5L1A0iEvRZbL6ZQ_nhOmAhBarmso10tz-HG_nul6CYUgKQoAr823qSYEQHZJZpbEIGM0OSyrfr42wBAA6fZValQDt7SeAT7taeBdSSSJ92ONr0WajJKCMFZ7fO8e_Ue-MzW6CPPGvdyZMOiZwvjd_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام مکتوب و منسوب به مجتبی خامنه‌ای، سومین رهبر جمهوری اسلامی، در مراسم سالگرد مرگ روح‌الله خمینی در تهران، خوانده شد.
در این پیام که محمدجواد حاج‌علی‌اکبری، امام جمعه تهران، روز پنجشنبه ۱۴خرداد خواند، رهبر جمهوری اسلامی‌ آمریکا و اسرائیل را به «جنگ ترکیبی» با ایران متهم کرد و گفت این جنگ «بر دو نقطه متمرکز است؛ یکی تاب‌آوری مردم و دیگری ایجاد اخلال در دستگاه محاسباتی مسئولان کشور».
مجتبی خامنه‌ای همچنین هرگونه اقدامی که به‌گفتهٔ او «موجب بدبینی و سرخوردگی» شود را «کمک به دشمن» خواند و خواستار «حفظ وحدت و انسجام و اعتماد متقابل» مردم و مسئولان نظام شد.
مجتبی خامنه‌ای هفتهٔ گذشته نیز به تمام کسانی که آن‌ها را «جان‌فدایانی که دل‌شان برای اسلام و انقلاب یا استقلال و سربلندی ایران می‌تپد» نامیده، هشدار داده بود که «اختلافات غیرموجه و حتی موجه را به تنازع و تفرقه تبدیل نکنند».
در بخش دیگری از این پیام، اسرائیل «پادگانی متعلق به نظام سلطه» توصیف شده و تاکید شده است این کشور از هر اقدامی برای جلوگیری از پیشرفت ایران کوتاهی نمی‌کند.
این پیام همچنین اعلام کرده است: «دشمن خبیث در مصاف با فرزندان دلاور شما در نیروهای مسلح دچار شکست شده است» و افزوده است دشمن پس از آنچه «تحقیری پرمعنا و عمیق» خوانده شده، تمرکز خود را بر تضعیف تاب‌آوری مردم و ایجاد خطا در دستگاه محاسباتی مسئولان قرار داده است.
در پایان، در این پیام از همگان خواسته شده است با ایستادگی، روشن‌بینی، حفظ وحدت و انسجام و همصدایی نکردن با دشمن، «نقشه شوم» او را خنثی کنند.
از زمان اعلام نام مجتبی خامنه‌ای، به عنوان سومین رهبر جمهوری اسلامی، تصویر یا صدایی از او منتشر نشده و رسانه‌های ایران فقط پیام‌های کتبی از او منتشر می‌کنند.
مراسم سالگرد مرگ روح‌الله خمینی که هر سال ۱۴ خرداد با سخنرانی رهبر جمهوری اسلامی و با حضور پرشمار مقامات و فرماندهان ارشد نظامی برگزار می‌شد، امسال به‌صورت خیلی محدود و بدون حضور مقامات نظام برگزار شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75937" target="_blank">📅 16:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqGWvOe_lrsW3fe79E4w46YrHvhEDohkEDZaO9bZkAUht8Y8BLgKlNKrEalHxxwNpz8060nHc9U8pwh4U_NK2CRBywCV04jJmxXQwhA-cGpQhhS40jeAEd-1CCZRQSM9A_X0mtx4o6f8iNe3kJOCMjNyk7SYKYSkYDzkmLHXB6NbhhVzr89TuAm5ByJ81qFktSF2w-W-b82JQ_WPtsD6hxF6gO3SZBJOSE3_xN0J7TW3K4-gINgB0VSM4vvciTEbSts-kd10rj5d7k3yr5KT6Dl-dfBq0qN99Vlf4H-aiacR22791Rvyhqg00R2hp8bAeVk2SyRf0VB21UoYSUrFow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ، رئیس جمهوری آمریکای روز پنجشنبه ۱۴ خردادماه از تصویب قطعنامه «پایان جنگ ترامپ با ایران» به‌شدت انتقاد کرد.
رئیس جمهوری آمریکا در این پیام نوشت:‌ «دیروز، در یک رای‌گیری بی‌معنی، مجلس نمایندگان، چهار جمهوریخواه بد و تمام دموکرات‌ها، درست در میانه مذاکرات نهایی من برای پایان دادن به جنگ با جمهوری اسلامی ایران، به محدود کردن اختیارات جنگی من رای دادند. چه کسی چنین کار غیرمیهن‌پرستانه‌ای انجام می‌دهد؟ آنها می‌دانند مذاکرات در چه مرحله‌ای است.»
ترامپ با انتقاد تند از نمایندگان حامی این طرح نوشت: «دموکرات‌ها از سندرم اختلال روانی [بیماری مخالفت] ترامپ تغذیه می‌شوند. آنها ترجیح می‌دهند کشورمان شکست بخورد تا اینکه به من یک پیروزی دیگر، از پیروزی‌های بسیار، بدهند. چهار نماینده جمهوریخواه، داستان آن‌ها کاملا متفاوت است. آن‌ها خودنما هستند! آن‌ها باید از خودشان خجالت بکشند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75936" target="_blank">📅 16:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75935">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r4sfUf0xpdiknj12bHoZPXAafFL74MhgizviYBx_YqVeuvsZIbnh6IZyugzqfPztjg3IxR5nx9rFJSIDcio0_6E8Rx19SN0iuatvQBme7H7q8vJoIqHy7p7Aek5BiZHrLQKonA1c-vFgR6iJZgpLTry_FMiFrHyPUJkCf13xKPfGoV5H4IseUD1hKxKQGgFiUlEyGwt7VukbaGV40TCZmotDsJXo7AFy3kN7LHXRWw-91KGqrE-rWu70qCk7_O6waFKfmj_wjy6vZ1idYzE8Tw_ugpkLDZ3SQDqi0L3DubjdTck0m0vZ9-oFD8-PDCk0T6-Fm7XOMsKvfXL6rmURIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرجان ساتراپی، نویسنده، تصویرگر و فیلمساز ایرانی-فرانسوی و خالق کتاب مصور «پرسپولیس»، در ۵۶ سالگی درگذشت.
به گزارش خبرگزاری فرانسه، نزدیکان ساتراپی اعلام کردند او «کمی بیش از یک سال پس از درگذشت ماتیاس ریپا، همسرش و عشق زندگی‌اش، از غم درگذشت.»
ساتراپی سال گذشته نشان لژیون دونور دولت فرانسه را در اعتراض به ریاکاری دولت فرانسه در قبال مردم ایران و جمهوری اسلامی رد کرد.
مرجان ساتراپی با انتشار «پرسپولیس»، کتابی مصور درباره زندگی خود در ایران و مهاجرت، به شهرت جهانی رسید. این اثر با استقبال گسترده مخاطبان روبه‌رو شد و به یکی از آثار شاخص ادبیات مصور معاصر تبدیل شد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 311K · <a href="https://t.me/VahidOnline/75935" target="_blank">📅 16:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75934">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9sI81GaBoC01qb_6I5ySgpCsIgFeSoPw2BlzmEGOsKHwyFX4YVQMY6gXnuDAw0WdVWFQRaaOMuxw-t6Si1-nbUgtY8z_jngn-d7jen3jBy6p6ksJvoL-DZwXkO21oPk5UdwbQierRX5ZObyXsmPVd4BCeGzLS3t5MIidNN85fJhPuaoWrtQ3lhrNdRuafh0gDK3lmtscSkBp-_2scnfuBtBm1cdO1S01gTEd3PLSqZpOFFScPfM86QspgcsnTOdTCq_k9TZQAD6MRdDC0hHcQ0H5cFs30s_S2P68BAKHUfaDuHD8KAC1GHBotV8j4H6dI9x_BgfQ8Lq3zJFRi3BJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان هه‌نگاو و سازمان کوییرهای ایرانی سیمرغ با انتشار اطلاعیه‌هایی خبر کشته‌شدن مهشید فلاحی، زن ترنس، در سنندج را تکذیب کردند.
این سازمان‌ها ضمن عذرخواهی درباره انتشار این خبر نادرست، با وجود راستی‌آزمایی‌های قبلی، گفتند اسناد جدید نشان می‌دهد این شهروند زنده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75934" target="_blank">📅 16:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75933">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPLgCBVp5bGdFVUegmhshEehhkams5sz4McWhEDjPE7W0WGb-XUJPehias-uRveh8VHodn1IWxQfEwtggJlCwu8io7iVoV865s8h_p9T0fgNWxTbXERzxXpq0r2tHFvmOHy5Qe_9y2PVf3Mlh49q_PDkQcJzKfteV8PLx4FV0Bq9LgkI_JpQqqMa9yxVsThvumEAsbkNwzeor_Xr5K87Meum8UyqOmGBGZ7i51g71eqrEYTajutbzbeokfhO6-SSeu0Conzah9TP-DXs81xIyoofxqs19i-BHHwyzq19N5PpqJ-tsUtRc0KvfouteHEvzbj1Ok42Ixl_Uw_4x4u9FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحدث گزارش داد آمریکا و جمهوری اسلامی به توافقی چهار مرحله‌ای نزدیک شده‌اند که با کاهش تنش‌ها آغاز می‌شود و به پرونده هسته‌ای و ترتیبات امنیتی منطقه ختم خواهد شد و انتقال از هر مرحله به مرحله بعدی، پس از «اجرای تعهدات» انجام می‌شود.
طبق این گزارش، مرحله نخست توافق شامل توقف عملیات نظامی مستقیم و پرهیز از هرگونه تشدید تنش یا گشودن جبهه‌های جدید در منطقه است. مرحله دوم نیز بر امنیت کشتیرانی، بازگشایی تنگه هرمز و ترتیبات امنیتی ویژه گذرگاه‌های دریایی و خطوط انرژی متمرکز است.
به نوشته الحدث، مرحله سوم این توافق شامل اعتمادسازی اقتصادی، کاهش محدود برخی تحریم‌های جمهوری اسلامی، آزادسازی بخشی از اموال مسدودشده ایران و ارائه تسهیلات مرتبط با صادرات نفت است.
بر اساس این گزارش، مرحله چهارم توافق پیچیده‌ترین مرحله به شمار می‌رود و ممکن است ماه‌ها طول بکشد. این مرحله شامل بررسی برنامه هسته‌ای ایران، سطح غنی‌سازی اورانیوم و سازوکارهای نظارتی و ترتیبات امنیتی منطقه‌ای است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75933" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75932">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFIYVMDh58Uw_XozRN-G2DH5W61JcMFNa12-sAGoyg0d8CA1sxQEIRoV5clsj-xfiClNNjriwqy96nP-bl-ItzSz5d4yacsb85UzC9ZhqgOwO3kTeUHaAzugNai2S1oUSrWHhFfbyb6DNd5yAeZ9WsjCmCShoPrynlCUngoQ35Wgl-o2Ro7yy1oBELAKOqfBykW9gdFKqTwCkQ_bPb6PPmUdGwA6aaLa5nuVXXhOPm2Tfckr_S_XX5a3jED_kv337nqBXNyrCa8lyXDV--iYwiFPTozGZUD0656hDNMP3FF1J1cSiDY1abQR_wfIlilovEtn5Sb2mAm8b_IlFnxafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا اعلام کرد اسرائیل و لبنان بر سر اجرای یک آتش‌بس به توافق رسیده‌اند.
بر اساس بیانیه منتشر شده، اجرای این توافق «منوط به توقف کامل» حملات حزب‌الله و همچنین تحقق چند شرط دیگر است.
این توافق پس از آن اعلام شد که حملات اسرائیل به جنوب لبنان در روز چهارشنبه دست کم ۹ کشته بر جای گذاشت و حزب‌الله نیز راکت هایی را به سوی شمال اسرائیل شلیک کرد.
در بیانیه چهارشنبه شب وزارت خارجه آمریکا آمده است: «همه طرف‌ها بار دیگر تاکید کردند که آینده روابط میان اسرائیل و لبنان باید توسط دو دولت مستقل و حاکم تعیین شود. آنها هرگونه تلاش از سوی دولت‌ها یا بازیگران غیردولتی برای گروگان گرفتن آینده لبنان را رد کردند.»
حزب‌الله تاکنون به صورت رسمی درباره این توافق اظهار نظر نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/75932" target="_blank">📅 02:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75931">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=hwbPccQF1RHofU7R5Hp_lOgDo5ImoIstKF3iK68mv0sPkiF9Zl-u63Ea2ob_73Ok5Y-NXYP-DdvuI2EEhhFDVqPOGlS94DFEz6HGlJNHF_JEO_Y3SCGZhpelUgEusgLzx_CrZ6LbNl2agQHkAIWn5Awp4rjsPtKkn4eSBYLCJ7_0My4JKuh9WJZtg_5NYWjylxMKhini7oea9rVz5DP0PojwNx6erwVqiRxaITnMqr7BbbazNQ1E5HY5vvcCEwDCAyOdtF0qpLFQXnEx0YoCI6LWDqZ_ugdXKNeB0-LYEKkQxAUGzHXPGKphKPn92LmI2mruqqMnEOQg8BQ3fs2guw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a5b9c36ab1.mp4?token=hwbPccQF1RHofU7R5Hp_lOgDo5ImoIstKF3iK68mv0sPkiF9Zl-u63Ea2ob_73Ok5Y-NXYP-DdvuI2EEhhFDVqPOGlS94DFEz6HGlJNHF_JEO_Y3SCGZhpelUgEusgLzx_CrZ6LbNl2agQHkAIWn5Awp4rjsPtKkn4eSBYLCJ7_0My4JKuh9WJZtg_5NYWjylxMKhini7oea9rVz5DP0PojwNx6erwVqiRxaITnMqr7BbbazNQ1E5HY5vvcCEwDCAyOdtF0qpLFQXnEx0YoCI6LWDqZ_ugdXKNeB0-LYEKkQxAUGzHXPGKphKPn92LmI2mruqqMnEOQg8BQ3fs2guw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه اصابت پهپاد انتحاری شاهد 136 به ترمینال فرودگاه کویت از دید دوربین مدار بسته.
mohsenreyhani01
سازمان هواپیمایی کشوری کویت با انتشار ویدیویی گزارش کرده که «نخستین تصاویر» حمله پهپادی به فرودگاه بین‌المللی این کشور که از طریق دوربین‌های مداربسته بیرون و داخل فرودگاه ثبت شده را علنی می‌کند.
در این تصاویر که از چند زاویه بیرون و داخل فرودگاه دیده می‌شود یک پرتابه مشابه پهپادهای انتحاری به سقف ترمینال فرودگاه برخورد و موجب انفجاری بزرگ می‌شود.
در ویدیویی دیگر، وزارت کشور کویت با انتشار ویدیویی اعلام کرد که شیخ فهد یوسف سعود الصباح، معاون اول نخست‌وزیر و وزیر کشور نیز ضمن بازدید از ساختمان ترمینال ۱ فرودگاه بین‌المللی کویت، این حمله را «تجاوز فجیع ایران» خواند.
کویت اعلام کرده در جریان این حمله یک نفر کشته و بیش از ۶۰ نفر مجروح شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر این کشور نیز در این حمله زخمی شده‌اند.
سپاه پاسداران که شب گذشته از حملات موشکی و پهپادی خود به پایگاه‌های آمریکایی در کویت و بحرین خبر داده بود، روز چهارشنبه گفت «هیچ شلیکی به سوی فرودگاه کویت» انجام نداده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/75931" target="_blank">📅 01:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75930">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l-u6xPeoIiJ64Fod6Y0CkqV-3u6fW5-XkHBHHHssVGu-Yuv5vGnZ7N609h6MLgt3vTt-YrEMx3OHFvzqzYROtV2mw6oCgRiisJPiy6gJcpmOcjkhM_Uhzvlx1pzoUimbtrp0PATjPo5-AtqDZGvVm2sZfOA2DAsLFB4helBAsnCcQ-iRpzG6AxRPRkJo2cWMsUlsNUQPTDPE9Ik8S7GJKKd1a7GDPvezINi2SwaswhwnlyI3UOczgyAhRN4uraxmPGcB0OpKzUJWpckxso8X9n1UFfPvGmxvoISM0DvOFfbj8JbsgkrXOS7t7PlsIl8T8W6a38Q-kvOtQGatIjZ99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلس نمایندگان آمریکا روز چهارشنبه از قطعنامه‌ای به رهبری دموکرات‌ها حمایت کرد که هدف آن متوقف کردن جنگ با حکومت ایران تا زمان صدور مجوز از سوی کنگره است.
به گزارش رویترز این قطعنامه با ۲۱۵ رای موافق در برابر ۲۰۸ رای مخالف تصویب شد و چهار نماینده جمهوری‌خواه نیز به دموکرات‌ها پیوستند.
این رای‌گیری تازه‌ترین شکست سیاسی دونالد ترامپ در کنگره به شمار می‌رود؛ با وجود آنکه جمهوری‌خواهان در هر دو مجلس اکثریت شکننده‌ای دارند.
بنا به این گزارش، این اقدام عمدتا جنبه نمادین دارد، زیرا برای اجرایی شدن باید در سنا نیز تصویب شود و همچنین برای عبور از وتوی احتمالی دونالد ترامپ به حمایت دو سوم اعضای هر دو مجلس نیاز دارد.
با این حال، این رای‌گیری نشان‌دهنده افزایش نگرانی در کنگره درباره جنگ با حکومت ایران است.
سه قطعنامه مشابه پیشین در مجلس نمایندگان شکست خورده بودند، اما با اختلاف آرای کمتر از دفعات قبل.
همچنین سنا ماه گذشته یک قطعنامه مشابه را در یک رای‌گیری رویه‌ای به پیش برد؛ اتفاقی که پس از هفت تلاش ناموفق قبلی رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75930" target="_blank">📅 01:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75929">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JdJXZR7bJTinTQ5Au4idrTxkk9Zx0PX9p28Tn_vYKr4w7_EY7IxLCXFcZ7lrLB06-4YYqawiXP1EnZJw7vX3_uB-ID_X73bdG0TJB2ShAoDuMQeVFKHiaKLpoyeofothlPzSw_AzmSF4P0rtwA_-Atm-fKPQo_2lOk-gDzJ3omR3vb4yg5NoZHrn5A3f9-HWhd5MY6KFwfD225ESJJZziFJjKPEP9TVOOIHBu74Ye-e9DV_60Rj5wKODUa2Qty8MpZ-y6hm4OtNAddHa-ZXnP0weke8Ao8CcEkSbAZCXFmnKoXr78gCuBou9G3PQpDClJ4X_5_TabNO33LobVqXu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامپ: می‌توانیم همه را نابود کنیم، اما ترجیح می‌دهم به توافق مکتوبی برسیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۱۳ خرداد در کاخ سفید درباره حمله جمهوری اسلامی به کویت و شکستن آتش‌بس گفت: «ما سه‌شنبه شب حسابی به آن‌ها (جمهوری اسلامی) ضربه زدیم، و در واقع دیشب هم همین‌طور. و وقتی موضوع را برای من توضیح دادند، گفتم بسیار خب، پس همین کار را می‌کنیم، اما ما هم کمی داشتیم شدید به آن‌ها ضربه می‌زدیم.
ترامپ گفت: «بنابراین برای بعضی چیزها دلیلی وجود دارد، و معمولا دلیلی هست که گاهی منطقی به نظر می‌رسد. و خب، آن‌ها کاری انجام دادند که خیلی… مسئلهٔ بزرگی نبود. ما خیلی سریع جلویش را گرفتیم، همان‌طور که با بزرگ‌ترین ارتش جهان این کار را می‌کنیم. اما بعضی‌ها ممکن است بگویند که آن‌ها تا حدی تحریک شده بودند، چون ما به دلیلی دیگر اقدام قاطعی انجام داده بودیم. بنابراین آن‌ها در حال تلافی بودند.»
او در ادامه گفت: «خود مذاکرات بسیار خوب پیش می‌رود. بسیار خوب. اگر اتفاق بیفتد؛ ممکن است اتفاق بیفتد، ممکن هم هست نیفتد، چه کسی می‌داند. اما اگر اتفاق بیفتد، ممکن است همین آخر هفته رخ دهد. تقریبا اوضاع به همین شکل است.
آنجا بخش متفاوتی از جهان است، می‌دانید. من می‌گویم در آن بخش از جهان، آتش‌بس یعنی این‌که به شکلی ملایم‌تر به تیراندازی ادامه بدهید.»
ترامپ افزود: «تحت هیچ‌ شرایطی نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست پیدا کند، هر اتفاقی ممکن است بیفتد وقتی با ایران طرف هستید، اما وقتی با کشورهای دیگر هم طرف هستید، این یک بخش بسیار بی‌ثبات از جهان است، احتمالا بی‌ثبات‌ترین بخش جهان.
رییس‌جمهوری آمریکا تاکید کرد:
«ما از سه تیم رهبری عبور کرده‌ایم. این یک وضعیت نظامی است، و واقعا هیچ ارتشی مثل ارتش ما وجود ندارد. ما می‌توانیم دو، سه هفته دیگر ادامه بدهیم و همه را کاملا نابود کنیم. ترجیح می‌دهم این کار را نکنم. انجامش خیلی آسان است. آن‌ها آماده‌اند که این کار را انجام دهند. می‌خواهند انجام دهند.»
ترامپ گفت: «اما اگر بتوانیم چیزی را مکتوب به دست بیاوریم که همان نتیجه را بدون کشتن همه به‌دست بدهد، من آن را ترجیح می‌دهم. فکر می‌کنم بیشتر افراد من هم همین را می‌خواهند. بعضی‌ها نه، اما بیشترشان بله. یعنی ما بالاترین بازار سهام تاریخ را داریم، با وجود یک درگیری نظامی یا جنگ. بعضی‌ها اسمش را جنگ می‌گذارند، بعضی‌ها درگیری نظامی. برای ما چیز بزرگی نیست.»
🔻
ترامپ: اورانیوم غنی‌شده زیر کوه دفن شده و می‌خواهیم آن را خارج کنیم
دونالد ترامپ، رییس‌جمهوری آمریکا چهارشنبه ۳ خرداد درباره خروج اورانیوم غنی‌شده از ایران گفت جمهوری اسلامی در مقاطع مختلف با این موضوع موافقت کرده، اما چند بار نیز نظر خود را تغییر داده است و این مسئله بیش از حد بزرگ‌نمایی شده است.
او گفت: آن‌ها [با خروج اورانیوم غنی‌شده از ایران] موافقت کردند و بعد گاهی هم مخالفت کردند. این یکی از چیزهایی است که درباره‌اش صحبت کردیم. خیلی هم بیش از حد بزرگ‌نمایی شده است. من خودم آن را بیش از حد بزرگ‌نمایی کردم.
ترامپ با اشاره به گزارش آژانس بین‌المللی انرژی اتمی گفت این مواد «نابود شده» و زیر کوهی دفن شده‌اند که تقریبا فروریخته است.
او افزود بیرون آوردن این مواد بسیار دشوار است، اما تاکید کرد: «من می‌خواهم آن را به دست بیاوریم.» به گفته او، آمریکا و احتمالا چین تنها کشورهایی هستند که تجهیزات لازم برای چنین عملیاتی را دارند.
رییس‌جمهوری آمریکا همچنین گفت سه سایت مورد نظر به طور دائمی زیر نظر هستند و در صورت هرگونه تحرک، آمریکا از آن مطلع خواهد شد.
او افزود: «اگر کسی به آنجا برود، دقیقا می‌بینیم چه اتفاقی می‌افتد و کمی هم بیشتر آن را منفجر می‌کنیم.»
رییس‌جمهوری آمریکا درباره مین‌روبی در تنگه هرمز گفت ایالات متحده از مین‌روب‌های زیرآبی استفاده کرده و مین‌ها را پاکسازی کرده است.
او افزود: «تنگه هرمز بلافاصله پس از امضا باز خواهد شد.»
🔻
ترامپ: ایران یک مشکل بزرگ جهانی بود و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند
دونالد ترامپ، رییس‌جمهوری آمریکا درباره گفت‌وگو با حزب‌الله گفت آمریکا برای نخستین بار با این گروه صحبت کرده و سه‌شنبه توافق شده که شلیک انجام نشود.
او افزود اسرائیل نیز قرار نیست شلیک کند و تاکید کرد موضوع‌های مرتبط با تنگه هرمز، برنامه هسته‌ای و لبنان باید از یکدیگر جدا بررسی شوند.
ترامپ گفت بنیامین نتانیاهو، نخست‌وزیر اسرائیل، برای او «شریک بسیار خوبی» بوده است.
او همچنین با اشاره به نقش آمریکا در تحولات منطقه گفت بدون کمک واشینگتن، اسرائیل قادر به انجام عملیات اخیر نبود.
ترامپ افزود ایران «یک مشکل بزرگ جهانی» بوده و اگر مهار نمی‌شد، می‌توانست خاورمیانه را نابود کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/75929" target="_blank">📅 23:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75928">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC48oWUdiJuozOQq_J8nyhiWo2BY-pQ7cK1wELB9S3_tjCVmWP1TjtzhzwjJ2TNTe5NSAFsZB7deGw723AFTxqc0-g_WpmaIBhYyV7ebr-bbM2gagNGnremdONuXA_gdahLd26u6pLCnsP-ji1LSKArq778xwnKha62VKLBFPpHpl67xheynFN5Kt5M3TqybCq23odoCehCWwCSKBHNh6OBLAE__-M_-IP9cNvn-9Zf-hfubZI954Asi8KFsGi_8dIHa9K8lg24dhjB9AYPiT2VwaORIXPNO6i2DOUuban7CNzlQsalXAkaI7zO5x3iIHmhm8T4Py7gXUQHo1Di7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقجی، وزیر خارجه جمهوری اسلامی، روز چهارشنبه تهدید کرد که حمله احتمالی اسرائیل به بیروت، پایتخت لبنان، باعث «ازسرگیری کامل جنگ» ایران با آمریکا و اسرائیل خواهد شد.
او در گفت‌وگو با شبکه المیادین، نزدیک به حزب‌الله لبنان، همچنین ادعا کرد که بعد از تهدید اسرائیل برای حمله به ضاجیه، حومه جنوبی بیروت و مقر اصلی حزب‌الله، نیروهای نظامی ایران در «وضعیت آماده‌باش کامل» قرار گرفتند.
عباس عراقچی در گفت‌وگوی روز چهارشنبه خود همجنین اعلام کرد که ارتباط با دولت آمریکا «قطع» نشده است، اما افزود که «هیچ پیشرفت ملموسی در روند مذاکرات حاصل نشده است».
ساعتی پیش مارکو روبیو، وزیر خارجه آمریکا، اعلام کرد که ایران هنوز تصمیم نهایی خود برای پایان دادن به جنگ را اعلام نکرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75928" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75927">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y3D2aIymZ6GpCHtxHKVSoY5tnkLjtxY4lkT2XxZuNcj-HTQUJ1CxeZLG5Mz8C8S1gxcdiSikjM1yRX5NHBkyNsvNk1elFDFXH1LWviemI5B9sGZrJ1nc2Dt3Ce_fWupSV9jVAtp6U9LmrC7uEvt02UovYTZFEqTN7ehclDR_MTnwjTVvhHgWtlWbSMyzdVr-YIBwZw_MBVmwuhKQL2ttEKRcmMDu3ATW5zoHW115J8-Xnm2jhwVJizzwajkegNaenxzZ5EoPUaofNIDuR3tcY5dD21qfEIs5BDKylNTtjlAoXCCxkY6cnBU1W30u-uExRk0nCFoF5nwbPYldt6Nxmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
ادعای جمهوری اسلامی
درباره شلیک به یک ناوشکن آمریکایی رو دروغ خوند.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/75927" target="_blank">📅 23:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75926">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=dtCHLpPwvnINM4_GbnzHSPc46n4fY0vRfi8gCZh-Q2JyPleT_CR89uAiVwtjmezixsod6zUCmh5M9zET6PAdh6zWEuQAmfQsTUS46i8F18TpWbDwGT6ho9MAHnpcGIhvK9Qg9k_wmBFyBr1RfaijdxhEnJkw0akmkmriMdVv6LX6Wvs8GlrAUwGJ3HrnF2YgQmcJiZ-mSe49B8zQVNlyQm4FvQNgCetP_wHhUkD4vet4vXn0kNd6lYPymmN0kEqFbe4jHi6rs0aZjOSgW-QfSRK3opTWVQq0adO172WPd2E4JYVN3di8ACWnG961gKneCiuYO5EhBiwWf3VZiodJzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/993ece4c51.mp4?token=dtCHLpPwvnINM4_GbnzHSPc46n4fY0vRfi8gCZh-Q2JyPleT_CR89uAiVwtjmezixsod6zUCmh5M9zET6PAdh6zWEuQAmfQsTUS46i8F18TpWbDwGT6ho9MAHnpcGIhvK9Qg9k_wmBFyBr1RfaijdxhEnJkw0akmkmriMdVv6LX6Wvs8GlrAUwGJ3HrnF2YgQmcJiZ-mSe49B8zQVNlyQm4FvQNgCetP_wHhUkD4vet4vXn0kNd6lYPymmN0kEqFbe4jHi6rs0aZjOSgW-QfSRK3opTWVQq0adO172WPd2E4JYVN3di8ACWnG961gKneCiuYO5EhBiwWf3VZiodJzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک‌های ارتش به ناوچه آمریکا در دریای عمان
شامگاه چهارشنبه، خبرگزاری فارس نزدیک به سپاه پاسداران به نقل از نیروی دریایی ارتش جمهوری اسلامی از هدف قرار دادن «مرکز فرماندهی و کنترل ارتش آمریکا» خبر داد.
فارس نوشت: «ساعاتی قبل و درپی نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی از سوی ارتش آمریکا، نیروی دریایی ارتش جمهوری اسلامی، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی را هدف قرار داد.»
در رسانه‌های جمهوری اسلامی ویدیوی کوتاهی از لحظه شلیک موشک‌های ارتش به اهداف مورد نظر در دریای عمان منتشر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/75926" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75924">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H21ytyvsw0Ywn0BO9nxxRlWUPpf5Z7mF7U-34qGEyYm5ZnXj_FxOVp5uW-CE5sjQv9yKmOeFWInXN3eeMQtkuaff3DKDoTsniD1E6AT-vJjbD_BJ-UDnoBLME0Elp1lBYtjyEmvun9mo-sFWfkO6bOF9dLRJSeKlHKTKtBDHxtjCTY7Hbn5wkFYZSlJXQjRt1nSWScI7xLmKDb950pFYc2fDoASr0mE9ga3rhql7qXVTbD6D8vL3T-IRygF72uOKAer-yZcS3lSVRQBAMbuvncCpuqzuaDhq4tnQps2cZNYriQr8_kmd04HTwiti3ji0AqhaT0tmMkhdIlhRq_3gxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hrYFoNXybOZ6GAJivEbBYaOvKPozZR8wNNIcYWxSneIn63HjFXdaa5IKECezwlIkK8xhXOhJOVLak432ZP5gsjZBp9RcBo9_rC-M4N-2j2RfvucZHxWwtW4wNkBpsWaADV1nTuekw4k3Fs8oIz4P3joSW7hmAMy7SegQtfeqqj_dYUmsG1Jb8sIJBryev5Glt7yqEX5SHW4Q6x81jG4WYc4itd2Av8XpMXJ5w-hKom3DOtD3xVoqMx86PYPiwPSll1aNmcfiX_8x1w7i7U5-C1M6umWXTCEjTgbbQ4D8nKtNP6fym5Zb7EB5pcT6D5cpKD45zRITKVUrad7tSpMVpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده اعلام کرد ادعای جمهوری اسلامی مبنی بر اینکه به ترمینال مسافری فرودگاه بین‌المللی کویت حمله نکرده و خسارت ناشی از یک موشک رهگیر آمریکایی بوده، «کاملا نادرست» است.
سنتکام اعلام کرد جمهوری اسلامی با پهپاد به این فرودگاه غیرنظامی حمله کرده و این اقدام را «عامدانه، محاسبه‌شده و بی‌دلیل» توصیف کرد.
@
VahidOOnLine
پیش‌تر:
حسین محبی، سخنگوی سپاه پاسداران، گفته است که تخریب ترمینال فرودگاه بین‌المللی کویت «ناشی از خطای سامانه‌های پاترویت آمریکایی بوده است.»
به گزارش رسانه‌های داخلی ایران آقای محبی اضافه کرده است که سپاه «هیچ شلیکی» به سمت این فرودگاه نداشته است.
او مدعی شد که بنا به تحقیقات سپاه: « تخریب ترمینال مسافربری فرودگاه کویت ناشی از خطای سامانه‌های پاتریوت آمریکایی بوده است، که پس از شکست در رهگیری موشک‌های ایرانی بر این ترمینال فرود آمده‌اند.»
در نتیجه فرود آمدن یک موشک در فرودگاه بین‌المللی کویت، دست‌کم یک نفر کشته و چند نفر زخمی شدند. فرد کشته شده تبعه هندی بوده و وزارت خارجه هند گفته چند شهروند دیگر هند نیز در این حمله زخمی شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/75924" target="_blank">📅 22:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fluShidjQe1opMNOGAh2dsvA9SuMU__5dgJfRfydIOnzycmuK3dl7YCK0akXb_UJVaQcxTs-Bcx5QG3yN3K6YQ1sYIvg-gSybaDLnKwY-2su9FKCReZdCqo0IKrq_Gx5PLo3XwzXVWut78Bd6pQyFzbNDTDlw4ReC3lBIrGe6-YXKHXNLUzRGXl7IIPn3R57oCwkn-gOUXQ2L1FXjAVEkwzBKZnGPnVcuZlgNlBCAINTCARCNuMSqHBPc9JQpuXCjZ9HsyxCADQ89nMBCpPntVXTTSUuKDk6PL01tU1MXAEj1lRqv7fLHv9-MCuNEScjXo4JhB7IjKR866iIEZhJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/MNGXLrWblQkGHQKq6nNw1FgR3LBFRabjJEw1cImiHJLhPzFTychzTRgr3rpze-RnvT5EuxnTMPYfJfXOBLfmoz7I7MJTXOPFDASBYs4UmQNAIX3zRi3aox4Z2ax6DUnAZf9zOLd57TYiRnrXL-iwctAiCJ8IvXildmzWA7Z6CUrEihzoowuV88h8iFisScuxbFpvnUjDIyvjpR-RM4Tiruhi9Yjn_o1eziSfCrF4VTXP2vVEncMuRdRUznKiKGgRHI8ZwYNrduNyxHHFmhY99F_ztu-uOPlxhvpoDGdkY-S90L9xdkmNn9gMv5I76NsNJqbSplYEl1D9n0u-gbAmdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lxKZ78myh51xR0kMtnqp2eTNjgMfTQVqSrgPfBn24wFjHytUKyXWB7j4aXbZviQUUu15arGg0N0qB3pGQpywcS2HvzVoF7GJIxirMRPxbJAs1ChyvyIaIEo8j7pkrQh_stxO7wmF7uUayYHKd_rjRMmmv4iNCphVJcuvc0bT0hGj9I2G8gxqrpC2SdtsOUNh8JqN6VOtqXrbhGqcQEigOUTXcE9EC82nw0Yv7U6RK9FOXN23uBU33RVqKe3zGwxSJrc7tisrm34FcNIDoas2lLb1_8NuVWDYP_suuZjT1Z8cln8TXDMQKxCm1I_EbGdZLCxX99lHfpP-puaQDLy4hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZYm09sd8Ko1bwa4Q8bmF7SI6zGi8xwTsa2hFq11Gv4sDJuNNRQ4D_TU2aZLSHN3LPiuzuI1uN-3yVRiAaJL6sdJ-KZ6bfQprBJ4gaMwd-7j17fU2r80QHOWuyrlV3lBi1gYiFaxOgbYiFzznVra3vgs5tI6sOuG6GKmlO6jXlfd0fgV9mcqjqd9teNcXm6G_1ZfpmeSxX6s3IirI3jgmve8hl3fk_Wft0pz8VOXR5fwQfsWpbwCd26ZbdoICOEIaK9QNyAZng4SDH5qlSsM9iVURZkCNtVGemoirq_hoyiv0ahx4Y5u8siET2YZQt0pnjkW2iw7l1I9NFzeFKUZujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KT2PcHCjD7qOxdPDMx06fGgOmOcTX0yjibvd6DfvEHke_7bReaAEjGqVb0dq8LqHlrUmnBEeybHXtew_bVeT3tZrCzrxoDsVvarZcimxwjKVMWDB5ygEix4_KIKa3jJGAsHOEhTciezJfSg_mwNyQiVahJ7HNYVUr85hQGT_YWarwnNEY79hXDZORj9ifke0p7BEUo_rJka8IYqNvqI06eAUM4GtPVML_KPobbjclcDxkBivHn67Rb1MN3s9INIKED-jNzkRdxFUMuEsneMRtne3RF5-AQh2YX9QFtQhJXwL0RoNQKTeBiuS0iyix34ltNhTTelQhAj1ZKjV9nsxuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qurJB5u6D2SBLX6o5uNvzOpCdOoPze8b7MRRkzMKkG4FCygEDYSI_okjWKfiYuPrEdtHttenETp7SxiHfUIsssIM-tjrV5GJ5O20u48BPhA0P3xhb1IifZCKTCkkCNA08jOgP0Hb9dDmmMLM2WCwdGF1BGGsH6LBcj69g-ZwMGFktA9hFfO6s-cDxhz9Rx4K4A80sL60CPOYLyT5lkpxvKEWmskd6EuqF1-fDbEXTZC4z-FrLFpxZUWPQU1xMVpuGIP15hn1DjNsN5Iib00tMzioOaiKV7jJXsUk5Lspg_9tT40XWSHJMZyklln1mj_A7L6V0sZXWkooejRKU7iRyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T4A6KCJ4Nzfl4FDyUBFQleYpQoco_b_cESgjBQBk_-zRsRDrjWpcCmDFjj2EY7aZ575C13-dYNy1jbB2vOXkqO980hQdbG2vL8fLyCH2dB1jaM7Wo0CCVogSmZ2Ibuqwe3KD0bGiG3COGv92hoz04_W8gox97-bGTzHP2T-BmbBNlQ2DCs089hmAkc_VJvyk0w35Z_9CZmZGZJT99_oLqrL485ttG0_7moI_HYHuTuHm3oQ6sTph6f2D4wHaINEhjfD8M1iKJaATJXBROLSUaenIRjlysI7kQ5IaGNXgJQYazU5yPCuR4y-VNmI2wXZKrE2_WVCHzJIhG6NDcWuj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iN_BkDmnxIG0vkU-PBK-sr8IWRu5MnmyFIpnZYs4ThZwVvCYcmqXwDnseVYVzZ7PpVlpmNc9j6zw7pbr1eRRgdgUFHyc9Twgx2pYjgdsnV_-KALmmj2Etxu0pNJS20PGFRusm7dX3XHjJo3zvsbfyuVNLObUUQh_6a0mRgLaGxvGsRy_EQwwNZouL7yXeft6G2b2nVjiCwOoXHkd5PVY8OeFKk4mu1F91VWkCpwAGuHQhRaEqOYLEZmm7buP9vKoLLJafF4FB4dLcJ4RlYTdbsGtTbprIbqvDODUSf93D4P6tmy_CHC_LL0JUeHOONxe1nQ0ouQ6GMLofDTFEIjvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Jmfovh_iWr0TOReyAMkvezL8FPyvpIfabha6UvdV0MLaMokoq36kJLgjwFpXry46RfzFBcpUqfo7MS_l5-VXN5FlsOO_q3fGL9Ef8MWIbe24OmBIzkVpg53nRQQKeaZii4SJNdnlNoa7SZ7pFADC83HV4FbL5cBE_rq5DNhSgEagqUaNBPMWo05dG4AYmcZLa-oHeCQ4JWNY0xCknzAzTpkCFtEttQNvyGxWZ0CZQqLZ0Kwbv2BkmVVCV7Srr3nS_K1cIKEF1Wj4tm24IJh1RywnLvbRu13auFc5JR-oa_OSbH56YXWN1z75O8jmGiiJ13Zw8Uzx3ySIw5j6N2W8DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XG6Eu8nyonsulK6g1QMVqkW9B2AOmc9F_1VwG4LVlGL7Z4E4tty10d7CXmIV9jpEe8OvwqRTiwo6YN2DuBBeT64F2K_wNiPcFXHtz82rrtQWtnZyhKp2iACH7F5ZN2ad4RNfUd3t5QdjClD3WJjt6Ta7tKrhvLnoV4MB4sBHRfGxXrJ4ap-bJeWmYbjgVL5cjRm6_DvJAZVmuVsUkXkKqPk2-CqcCsR91fWJbTbksUW8S5QqT1841UGtljGzfmIgoNnHU3H-0dgsjjEAH06IlHB9osz6LezVBdS0uFCn9M9btEuRYB5rQZTrh15dNaU17uqnjlf1RYYjvXvNwNmYew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دادگستری آمریکا روز چهارشنبه اعلام کرد مدیرعامل یک شرکت فناوری در کالیفرنیا به اتهام تأمین تجهیزات آمریکایی برای نهادهای هسته‌ای و نظامی ایران بازداشت شد.
بر اساس بیانیه این وزارتخانه، جمشید قُمی، ۶۳ ساله، شهروند دو تابعیتی ایران و آمریکا و ساکن نیوپورت کوست در ایالت کالیفرنیا، به «تبانی برای نقض قانون اختیارات اقتصادی در شرایط اضطراری بین‌المللی» متهم شده است.
او متهم است که «تجهیزات پیشرفته شبکه، امنیتی و رمزنگاری ساخت آمریکا را برای مشتریان ایرانی، از جمله نهادهای هسته‌ای و نظامی حکومت ایران تهیه کرده است.»
وزارت دادگستری آمریکا همچنین اعلام کرد که جمشید قمی از «شرکت‌های پوششی» در امارات متحده عربی برای پنهان کردن محموله‌های تجهیزات شبکه و رایانه‌ای که مقصد نهایی آنها ایران بود، استفاده می‌کرد و این شرکت‌های واسطه برای مخفی نگه داشتن مقصد واقعی کالاها و دور زدن تحریم‌های ایالات متحده به کار گرفته شده بودند.
جان آیزنبرگ، معاون دادستان کل آمریکا در امور امنیت ملی، در این بیانیه گفت: «طبق آنچه در کیفرخواست آمده، قمی با تأمین فناوری آمریکایی برای سازمان انرژی اتمی ایران و سایر نهادهای تحریم‌شده مرتبط با برنامه هسته‌ای ایران، به ثروت دست یافته است.»
او افزود: «بخش امنیت ملی وزارت دادگستری افرادی را که برای پیشبرد اهداف هسته‌ای ایران قوانین ما را نقض می‌کنند، پاسخگو خواهد کرد.»
به گفته وزارت دادگستری ایالات متحده، متهم بیش از ۱۵ میلیون دلار از ایران به حساب‌های بانکی خود در آمریکا و یک حساب امانی منتقل کرده و به‌دروغ این پول را به سازمان مالیات آمریکا به‌عنوان ارث خارجی اعلام کرده است.
بر اساس این اتهامات، اظهارنامه‌های مالیاتی فدرال او تقریباً هیچ درآمدی را نشان نمی‌داد و بالاترین درآمدی که در هر سال گزارش کرده بود تنها ۲۰٬۶۸۴ دلار بوده است.
وزارت دادگستری آمریکا همچنین مدعی است که او از درآمد حاصل از «طرح دور زدن تحریم‌ها» برای تأمین هزینه ساخت یک عمارت چند میلیون دلاری در اورنج کانتی کالیفرنیا استفاده کرده است.
@
VahidHeadline
دادستانی علاوه بر درخواست مجازات حبس، به دنبال مصادره اموال وی از جمله عمارت گران‌قیمت اوست.
بازپرسان معتقدند او به مدت بیش از یک دهه از طریق شرکت خود در تهران به نام «فراز پرداز رایانه»، بیش از ۲۵۰ تن تجهیزات کنترل‌شده تکنولوژی را به‌صورت مخفیانه خریداری کرده است.
او متهم است که با استفاده از حساب‌های شخصی در eBay و PayPal و از طریق شرکت‌های صوری در امارات کالاها را تهیه و به ایران ارسال می‌کرد.
@
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/75913" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C2OhiGFK9gWnrtfOoLY4gD0U9cZtk3dQmbRPZbPbniyN4gur-IiEl7HP1cuH0D71VDJAL9brPV2eszOL2QJXX3pdnBPStqqybJvyXeWeLv754O3-6I3OjQcydQZaKH3IJx3iZdDMeRQJapWEbMkTIy_TcGWOTJXql3dxuBX0sEPVWKQ7mJV7m5aZtTHfrSPaqSYdX20_umZK9NsYex5LVCnNq0N7Xj2c7Mdtcux4_1FHpbygAI2SC5R40kXzHBOv9ZzNJzQqSpfeiy48WHCxJbhYEkO4gyesjNCVoNXnSypHSIy4ysvL84CBidbuzQ3x3If_hqZGC8EHHpHaFZgLVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VqpcnWm9VWfGceCarUqOnO3DrB7MiJs43crmdhwFqzjnWB5kOm_vEDOTK818QN_3L8lwR_BZei8AD6XCqtZT5K_EA9ZUWoQNDygu86Xo5ZzI_fK7KuJLJSeQDrERmwGmlkSqdV1YcEIPP9ud3v_T4xpZBT7gyY4RQ4-9P1Iyabhlm_D6eRq9U-JxNcnexMIeGsbC5e8wC5UZjtGpUcy4nBPLJEiIAXnqsF_lSZdPCgvk0zfRy1PJSlqL9hqWPtEw7LgckPN7pSRrDFyG_Ix0YspAuOJoPf7iYoiiofs5gmaqlFWvtOTorrnKWbbjd_eRcvwPCGH_SNkG0rAoRmzXHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سی‌ان‌بی‌سی، ترجمه ماشین:
▪️
نتانیاهو از پاسخ به سوالی در مورد اینکه ترامپ در تماس تلفنی این هفته به او فحاشی رکیک کرده و رئیس جمهور آمریکا گفته است اگر او نبود، نتانیاهو الان زندانی بود، طفره رفت.
نتانیاهو در پاسخ به سوالی در مورد اینکه ترامپ ظاهراً او را «دیوانه» خطاب کرده است، گفت: «وارد جزئیات نمی‌شوم.»
[ولی ترامپ در
مصاحبه با NBC
گزارش آکسیوس رو تایید کرد که بهش گفت دیوانه]
▪️
نتانیاهو می‌گوید او و ترامپ «اختلافات تاکتیکی» دارند اما «در مورد مسائل اصلی اتفاق نظر دارند»
نتانیاهو هرگونه اشاره‌ای به اختلاف با ترامپ را کم‌اهمیت جلوه داد و گفت اگرچه آنها گاهی اوقات «اختلافات تاکتیکی» دارند، اما «در مورد مسائل اصلی اتفاق نظر دارند».
او گفت که این موارد شامل جلوگیری از دستیابی ایران به سلاح هسته‌ای و تهدید اسرائیل با آن می‌شود.
او گفت: «گاهی اوقات، مثل بهترین خانواده‌ها، این اختلافات تاکتیکی را داریم. اما ما همیشه راهی برای حل آنها پیدا می‌کنیم و این کار را به عنوان دوستان خوب انجام می‌دهیم.»
او گفت: «ما می‌توانیم صبح اختلاف نظر داشته باشیم» و تا بعد از ظهر به زمینه مشترک برسیم.
▪️
نتانیاهو در پاسخ به این سوال که آیا واقعاً آتش‌بس با ایران برقرار شده است، گفت: «فکر می‌کنم یک بازی تاکتیکی در حال انجام است.»
نتانیاهو گفت: «و ایران مطمئناً می‌داند [ترامپ] چه گفته است، اینکه در صورت لزوم، بازگشت کامل به اقدام نظامی وجود خواهد داشت. این تصمیم رئیس جمهور است، اسرائیل آماده است، و نیروهای آمریکایی نیز آماده هستند.»
او گفت: «فکر می‌کنم ایران باید این را در نظر بگیرد. فکر می‌کنم آنها دارند این را در نظر می‌گیرند که دارند با آتش بازی می‌کنند، این واضح است.»
▪️
نتانیاهو از اقدام تلافی‌جویانه ترامپ در محاصره بنادر ایران در تنگه هرمز تمجید کرد و آن را «بسیار مؤثر» خواند.
او گفت: «محاصره معکوس، یک حرکت هوشمندانه بوده است.»
▪️
نتانیاهو گفت که «هر دو روز یک بار» با ترامپ صحبت می‌کند.
او گفت که دو رهبر «اهداف مشترکی دارند... ما می‌خواهیم به آنها دست یابیم.»
اما در پاسخ به این سوال که از توافق آتش‌بس احتمالی چه انتظاری دارد، نتانیاهو اذعان کرد که «این یک سوال بی‌پاسخ است که جنگ چگونه باید پایان یابد.»
▪️
نتانیاهو گفت نهادهایی که به نفت ارسالی از طریق تنگه هرمز متکی هستند، در حال حاضر «در حال توسعه مسیرهای جایگزین» هستند که کمبود عرضه انرژی ناشی از بسته شدن مؤثر این آبراه کلیدی در طول جنگ را جبران خواهد کرد.
▪️
نتانیاهو انتظار دارد که تغییر رژیم در ایران رخ دهد زیرا رهبری فعلی «به شدت» تضعیف شده است - اما پیش‌بینی نکرد که این اتفاق چه زمانی رخ خواهد داد.
نتانیاهو گفت: «شما نمی‌توانید دقیقاً پیش‌بینی کنید که چنین رژیمی چه زمانی سقوط می‌کند. شما در بسیاری از موارد آن را پیش‌بینی نکردید: نه در رومانی، و نه در سقوط دیوار برلین، و هیچ‌کس آن را پیش‌بینی نکرد، اما این اتفاق افتاد. چرا؟ چون ترک‌ها از زیر در حال گسترش بودند.»
او گفت: «در واقع، شما همین الان در ایران شکاف‌های عظیمی دارید و نمی‌توانید پیش‌بینی کنید که چه زمانی این اتفاق خواهد افتاد.»
«اما من دیروز در یک نشست عمومی اینجا گفتم... ببینید، من معتقدم که در نهایت این شکاف‌ها گسترش پیدا می‌کنند و رژیم سقوط خواهد کرد و ما تمام تلاشمان را خواهیم کرد.»
نتانیاهو گفت: «من فکر می‌کنم که ما باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تغییر نکرده است، اما دقیقاً در لحظه‌ای که ما انتخاب می‌کنیم، این اتفاق نخواهد افتاد.»
او گفت: «فکر می‌کنم آنها به شدت تضعیف شده‌اند.»
nbcnews
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 342K · <a href="https://t.me/VahidOnline/75911" target="_blank">📅 19:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vOXW_IB5-IMODHsMx3XwvIR5x6BYU8dcYjGlIg0b4HjukWFyUbcF0Clz8ey1QkLwO_DfOAdUgSOKiq7KCeXn3Bmn02SMCOOjHyz3QpofL33vIhgPNoNUr0tff4DvZZYRe5X5_w7axsc2w8xX0mnQyweweZI6K9LymeI5NMdIlMZ7VRTs0h87VS0_m-xBnyL9ab4KA9WCxmPhigQSotvqSH_pcwcYjQ60hP2TjqryCorC6jXqHDvOWWQu_NBiUkVXBU13C4u7f2gW1u0DI3R8JkqeuYFcjIj0b935M5JaNqOugJ925kdc2TKlbYnFHT5dE9DXSb6fXhXvpWczS8V4Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه گفت که سرنوشت ذخایر اورانیوم ۶۰ درصدی ایران در مرکز مذاکرات با واشینگتن قرار دارد و تهران هنوز با یک توافق صلح موافقت نکرده است.
روبیو در جلسه کمیته روابط خارجی مجلس نمایندگان آمریکا گفت: «فکر می‌کنم اکنون در برخی از اسنادی که میان دو طرف رد و بدل شده، این موضوع به‌طور واضح مورد توجه قرار گرفته است، اما تا صبح امروز هنوز تأیید نهایی از سوی نظام تصمیم‌گیری آن‌ها را دریافت نکرده‌ایم.»
روبیو در مجلس نمایندگان آمریکا بار دیگر بر اظهارات پیشین خود مبنی بر پایان جنگ با ایران تأکید کرد و گفت: «ما دیگر حملات مستمر در داخل ایران برای تضعیف توان نظامی آن کشور انجام نمی‌دهیم، زیرا عملیات "خشم حماسی" به پایان رسیده است.»
روبیو با تأکید بر اینکه آمریکا به اهداف خود دست یافته، افزود: «ما پیروزی را این‌گونه تعریف می‌کنیم: نابودی زیرساخت‌های صنایع دفاعی ایران، کاهش قابل توجه تعداد پرتابگرهای موشکی که در اختیار دارند و کاهش چشمگیر ذخایر پهپادی آن‌ها.»
او ادامه داد: «ما به همه این اهداف دست یافتیم. علاوه بر آن، آنچه از نیروی هوایی ایران باقی مانده بود را نابود کردیم و کل نیروی دریایی متعارف آن را از بین بردیم.»
با این حال قانونگذاران حزب دموکرات در این نشست موضع آقای روبیو درباره پیروزی آمریکا را به چالش کشیدند.
از سوی دیگر ایران بامداد چهارشنبه کویت را هدف حملات پهپادی و موشکی قرار داد که به گفته مقام‌های کویتی باعث کشته شدن یک نفر و زخمی شدن دست‌کم ۶۳ تن دیگر شد.
@
VahidHeadline
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75910" target="_blank">📅 17:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پیام‌های دریافتی ساعت ۱۳:۴۵
سلام وحید همین الان بندرو زدن فکر کنم فرودگاه یا پایگاه هوایی بود صداش زیاد بود جوری که تا شهر نمایشو لرزوند
بندرعباس سمت اسلکه صدای انفجار یا بمب
وحید جان بندرعباس صدا انفجار خیلی بلند 13:45
بندرعباس رو زدن خیلی بد بود این دفعه صداش از همیشه بیشتر بود خونه لرزید
سلام ساعت 13:46 بندرعباس صدای انفجار اومد.
غرب بندرعباس
بندرعباس صدای چندین انفجار سنگین همین الان شنیده شد
همین الان بندر رو زد
سلام ، ۱۳:۴۵ صدای ی انفجار با لرزش شدید بندرعباس
سلام 13:46 صدای انفجار بندرعباس
وحید بندرو فکر کنم زدن صدا انفجار اومد
سلام همین الان قشم صدای انفجار شدید اومد
هرمزگان صدا اومد
بعدش این خبر منتشر شد:
"معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان گفت: صدا‌های شنیده شده در شهر بندرعباس ناشی از انفجار‌های کنترل‌شده مهمات دشمن است."
(گزارش درست اینه که: صدا شنیدم.
از روی شنیدن صدا نمیشه گفت "زدند"، "حمله شده" و...)
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/75909" target="_blank">📅 17:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75908">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omCqMI-iMXt0yWhTaOJM-qnTC5erndX0jjCaE3DgQE851Zxw4m7FtKGDMvke7StQXpSa5lxRojtFT9L8VsPsvbDUpzeuoBGjT76NhM7aOXUNpsO4mkbTvag1oEn5r8fzxGtSvXAaT5rfkqWvAAtARXWhz5Pem2srKzLUzRo-hDkfq7DqX3zwsX_aOQ-PvuWXEmABaWkNMfEKeLmIUczmyTAn9XZ7qCbX9svCJ3iFongby1SCIMlfvvbmLVTI4gt8-BFcIgksyfe2CMyGrNjvAWp2nwXtbYyRdx4na7rVzDFPyLWMepkwYfOPphmYxQ2Ap2RkJxSRnWpYJar_gtWOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم جلالی، سفیر جمهوری اسلامی در روسیه با اشاره به سفرهای علی لاریجانی دبیر سابق شورای عالی امنیت ملی به مسکو گفت: سفرهای او، به جز دو مورد که خبری کردیم، بقیه محرمانه بود. یعنی هم ما و هم طرف روس، سفرها را رسانه‌ای نکردیم. فقط دو سفر اعلام شد.
جلالی به خبرآنلاین گفت، لاریجانی سفرهای محرمانه زیادی به روسیه داشت و در یک سال‌و‌نیم اخبر، هفت بار به روسیه سفر کرد. جلالی بدون اشاره به دلیل این سفرها و موضوعات مورد مذاکره گفت: «در یکی از این سفرها، طرف روس با من تماس گرفت و ابراز علاقه کرد که سفر رسانه‌ای شود و آقای لاریجانی هم مخالفتی نکردند و خبر آن منتشر شد. اما سفر آخری که در ۱۰ بهمن‌ماه ۱۴۰۴ صورت گرفت، به شکل دیگری رسانه‌ای شد.»
جلالی افزود: «ما دیدیم وقتی هواپیمای ایشان حرکت کرد، سه یا چهار هزار نفر در فلایت‌رادار آن را تماشا می‌کنند. زمانی که هواپیما در مسکو نشست، این رقم به ۳۴ هزار نفر رسیده بود. برای فلایت‌رادار، این عدد بسیار بالایی است. بعد هم یک‌سری شایعات شکل گرفته بود. در ماشینی که ایشان سوار شدند، به ایشان گفتم که این سفر را باید رسانه‌ای کنیم. پرسیدند چرا؟ گفتم با توجه به حوادث ۱۸ و ۱۹ دی، الآن عده‌ای از ضدانقلاب‌ها تلاش می‌کنند این خبر را به شکل دیگری جلوه دهند. برخی نوشته بودند که رهبر نظام به روسیه رفته یا برخی گفتند که پول‌ها را به روسیه برده‌اند و این خبرهای عجیب زیاد شده بود.»
جلالی در ادامه گفت: در ۱۰ بهمن، زمانی که علی لاریجانی با پوتین ملاقات داشت، در پایان جلسه من گفتم اگر اجازه دهید ما یک خبر کوتاه، با هماهنگی، منتشر کنیم. به این ترتیب همان دو سفر رسانه‌ای شد.
سفیر جمهوری اسلامی در روسیه همچنین گفت: پس از کشته شدن علی لاریجانی، پوتین متن پیام تسلیت خود را آماده کرده بود اما گفتیم منتشر نکند تا اول رسانه‌های داخلی خبر مرگ را اعلام کنند. [چون فعلا به مردم کشور خودمون دروغ گفتیم و ضایع میشه!]
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/75908" target="_blank">📅 17:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4rn_qmd8B1rvJAWyBsd6Amkrw1v0DtOq6m4XJryHU3-h_YUp58rAYJF1P5x3c1gJOpGG5pT_KSlU2jByAn8g9tVyWcgtpVVTim2_f98TPwYyYHFA61Em9yrAowEVDoMvGgwBCM2ehd2ydwVC6LbgN_4TQJXFZbFpRSbZ9NESifDo8zHgTJ28pJGfV8o92lC1nGuapr0BkMnIWaostYjhGz7pui9ySFyjWC5mfEKf1JtrFxpYTrZpZy9axfqkW70y6yImWBHWqEyKmpEE0-8qKYTbRvNywsINe0p0Y0DHrgqHicNDhC5AIMkD-7Cm_BzBUaU-IGF_FU4grIeFg4c2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در گفت‌وگو با پادکست «پاد فورس وان» متعلق به نیویورک‌پست گفت که جمهوری اسلامی موافقت کرده که سلاح هسته‌ای نداشته باشد، اما همزمان یادآور شد که تهران همچنان می‌تواند «نظر خود را تغییر دهد.»
او در این مصاحبه که روز چهارشنبه منتشر شد، گفت: «ما باید کاری در قبال ایران انجام می‌دادیم، زیرا صرف‌نظر از اینکه وضعیت ما [از نظر اقتصادی] چقدر خوب است، نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.» پرزیدنت ترامپ اما اضافه کرد که «آن‌ها از قبل موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند.»
وقتی در این گفت‌وگو از پرزیدنت ترامپ سؤال شد که آیا رژیم ایران با این شرط موافقت کرده یا خیر، او تصریح کرد که «بله، آن‌ها با این موضوع موافقت کرده‌اند.»
او اضافه کرد: «منظورم این است که آن‌ها اکنون می‌توانند نظر خود را تغییر دهند، اما این یکی از چیزهایی بود که باید با آن موافقت می‌کردند و موافقت کردند، این موضوع اصلی و بزرگ بود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/75907" target="_blank">📅 17:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1XAsTyril5vz33tiCN4NP4vrwdpjJcaA2dsvUQLiKoQ1NMBJUdFwUPTJ1Zxh_McR4bAkCoz73w-9v-Rv6Z-3JmAFpI_sD4Xnchlx6XM6y3yOtDu9-p2C6MbBbl5YeEIEHpNhjUIA1dt38iAtqt2OFMPJhRVIFzsf_34WZzcs_vBcWUHkSuKHGeCWZ7ZkJQkIoTWr7lCRx3hr_2kPavVuDUHScfho9NqNoV586763l-wB_sMqkfw4xeKKJEuEgtWIMMKl1O4EmKIUjxmV4iTfP2n2MjAJKQGVuu-zUPBFYERQfbrwCcFFK7x5DcuZdTpfmUKawKy577juVlkGalGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ ایالات متحده می‌گوید این کشور مصمم است مانع از تلاش ایران برای «جا زدن» افراد مرتبط با سپاه پاسداران در کاروان تیم ملی فوتبال برای شرکت در جام جهانی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/75906" target="_blank">📅 17:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mLr_7h30pXBDGUjw8o6mbNw_ek5HBIafvFvRxKfHYxfT5WCpl_M0-7AbMmhbctTXQo1uwuwiWmL2uLZCEW8MimbV0i6GbdV9gHrmCZqn72-iDxTUzlbwLjnYytk1EW8ul1MNw54GaSF9_DbO0kF6xpoUzNEP1YWfhC-AROV1O6tp2sdVo37bOMVivcj5EDMXJnvpXiRfZ1wfDBtDjTl-QTyQuuyJ4sd29eHO-xkbHt56-dCJPUBH7CWy7YdPaDxkiQhD0v8aycuadAZlx-cfyIvsqQ4Vfym0urlxFE6EKiD-yi05GiB_gG-vaE-2kfctu-PCi31Hhb1f5jRdvi3mog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/c66MhuxKlXDUfc4CaEjBaMUy6QG3ve4iEM_YF1r7RFv3hFg_zQucg27njvY_XTcyJaa-XATLKu5LQUpAsCVYxwyxx0ZsDkqp22VsrGIGIOCCN0t7YGvK9eqH94YYXqPzCyx0saKWXalyD2aC7PAy-MJS4bhrxvh1rb_S3zQRNU0Amz1Ek4M-SmtD9vFfnkkm4YO6nUWNQ16DZ4fWgZ-9P_6OKG6WqXhyVD5ymurrP-bitbZUZgHaoMuMWW0vXISMtvbzvE3LhxlPtEqc1LIFWMyIzBL08eARkhKcfKR6bY9gCSdja3oKDYgPF7Ec4gR9JI5kR5dANfWRDd1vkiKUAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Fqyuwf7i3ACqoD1PI-qduRlvimShPE8UY6kKv4tlLM0BDqnUKAxBNR_07xnVBCHIPIjX9rv7vwTvy5JIgS2TQo4ttOfOIdnMBpTT-uWjWCQiyo2Me3UQzF9U2OekhKXTrGCWqHo46jKXiLoDfHnNsb-s380wB-Kqn8ral05nAp9ETBSIztEfFGxJ_Yki4tzr1Ce0A9n_sjhjoPYMwS5FH1b2P5TdsYA3e45AOygPXxabLx3NYYFghiSyd1RvenZkW-0sOZKwV5scgMmO4XM0ZC_rVPqlO0DgqLkOURE48lQJhDI8NKtNxaekl2iStJc575HRAu8luTwVA1J7SyEgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Iku4fUbzy6-bLdHRqf_26Lv124NFT2J0ZwCrghAmozVnN4OdKOX5vpYlXV_x3zjzveMzYIMBHykqHswkja0VoZ_OF31OKbGxCTOV8aybfbfrLhDDeqxBIZhzbnsYpbLF3Zj0C-VWtPY9aPNEghxS1cF3aKudQan4_FftwcG6fKydfYcD1V6Q4J69PjCNoYO-x25S1KZp9iN-sq9aXrfqol9-86PHBkon4AFX-wr_9jS-9tc-drX_G7LWB1xwVW5rkO30Efd37OPAp8Y85hoNzG-rn_s8_7W4UCtcXV4vsCTLn9XGq1G_pPhXKNHzWMq7Ueulopf31PJt25enTaF24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EuzE4Vn9FlDehN15dWgFqEYZsiEipuqEpDg3UmMe3E4IgzqK-viRfQFlcDoNXBTPT0UA5_RWNh1hAXV1H5kbEfs3kZg6wE_yKAhaFloxzMu6Dm3bgaYyLmeq0bfY6TDbbSzS9XXYuBVNrrIF73wUtcfTDLsfJA60GNQ4QYXwZkO8vhviSrx9oGc2FHrnHSlUTzjHxGyulp5t8VCp5sltIX5i7p_XcKhCZvRgednOTwO29yxu8hslNuu4k0z6GMI8EobywfXUYPLV8N_O3vYle6tdTavKBIaCvOz7a0uh2exmXWqelJPGki1U48eF4QRKGYH6tkbkGpSleAWYOsnWTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lc5LBPzfCmxAar-C9a6XqvZFybSK7yNAXZyAM6lHsJzd0xEpAwo2kv8OCe61iJNFR08_DFQaGn7UITY0eduUcQ_hKq9o8iEjNQ5eEmhRhySw0zrOdrHB8vvWy6Y-HVcYGftzGvWKNl-BIr32HmdirVZjp0gSI9zYBZqxG_JkCGNvzgm16_ofwjsHLvqx-yiJwYyPL8kMrdcyRB9v8iwpeBvZaonJotU0rTWfvYNuBrIsjrZJSb2Vu6Bkp4SQl6Y0pDcb10LzrHrOHOVxa-RZALaz9ytktqu5jGTAi3f2fU95wYSPODvFSpFy_eagpSPmKMu0xjSJTGO3FZQyu-EzsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uOVWchcc71ici4cojsKVd2hgTB-L9EUoL3n30K4yymvcsnrXT_whYL1CPTZP7bsE-5jLt6AO9FTRXEwphwrQHP7ftEx4mLvzvh2uUv6yWRqkUmtEIJbg1nebjcWJWAbv-yhCwFIkuYeBLJBID2TVDCPQnpi9lkUEf6WYefmC3BrYPNAwmD9V77Pg2yVG60Bso_uvsG4krqc2AFhAjUIjn-FgMPfqAglxWTgq-mU2SASlZjf-ncaPqbMCZWR-5XI9kVZHw0xhDPc3an3UP4spKiLFlhGeKEnSWW7LnTB7Pw7LUI9v9AjW9qhn4u0HFg9SYMpRl8qoqajBt8ZX6mFOhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nI6gGvhKevVSLhFIjmpCRks7RHg_YMtxDyMRqq918UQdCgQeBuySPjuczrADDZbL8XKj-pe34z2PHINyPopa-N-Q54GjOJHF_I5tUXbEJGEN4Ct4Vab_AZZjZsw4hdGsVrfuQ3yrs45UG6RAE8kzd7AYeH7hA6ygQVNfO-by4cpEsm4pdVFX4eYRATq-4i4FmguCfIp2mrsr7meifjA4Ke5CIO_v2MG5bihphUvhRQPGhr--GLethG2c9azJElDbBWCvCg_vpUXNggAX0kAPgA1PK-3bSWy534bXl16hwhCK_OndciSnEEbQwHVOkb4k2onsmS-THOxBLXymKOuLkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=n1roTnddPKSuVksmCbhXQb6_FZvkWgEuHYYQ4tDX53exfbvgYyYlyBhIvzECLqBLJz_8Uj83AKPsmX9q6ME6NeOdrMv_TKg33BuWwTDorsLjJyOrfjATyzephef6nf-s3Iir6OIbDZSFyR3GfFgUqlJUlY1P2ErjdMbeDQr6KEnv1YASXEc5jI6g9x4JjCPc6WTthO3v5Jxl3DUlj9g7Nj6YWc71SRlBejH9lDp8VYPlig6QlL3w5nNs-G0FsbZStBZo5InWS4MJ5tce-2nAyck-hEaH8JCiIIzi2yyrWoFZeEx3t5j7r75ccPYWBph3u7cFBsUeNEHgUVv5pml32A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1acb519b46.mp4?token=n1roTnddPKSuVksmCbhXQb6_FZvkWgEuHYYQ4tDX53exfbvgYyYlyBhIvzECLqBLJz_8Uj83AKPsmX9q6ME6NeOdrMv_TKg33BuWwTDorsLjJyOrfjATyzephef6nf-s3Iir6OIbDZSFyR3GfFgUqlJUlY1P2ErjdMbeDQr6KEnv1YASXEc5jI6g9x4JjCPc6WTthO3v5Jxl3DUlj9g7Nj6YWc71SRlBejH9lDp8VYPlig6QlL3w5nNs-G0FsbZStBZo5InWS4MJ5tce-2nAyck-hEaH8JCiIIzi2yyrWoFZeEx3t5j7r75ccPYWBph3u7cFBsUeNEHgUVv5pml32A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارت خارجه کویت روز چهارشنبه ۱۳ خرداد اعلام کرد در حملهٔ پهپادی ایران به «تأسیسات غیرنظامی» این کشور، از جمله فرودگاه بین‌المللی کویت و برخی نمایندگی‌های دیپلماتیک، یک نفر کشته شده است.
وزارت بهداشت این کشور نیز اعلام کرد در این حمله دست‌کم ۶۳ نفر زخمی شده‌اند.
وزارت خارجه کویت در بیانیه‌ای که ساعاتی پس از گزارش‌های اولیه از حمله منتشر شد، مشخص نکرد که کدام نمایندگی‌های دیپلماتیک در این حمله آسیب دیده‌اند.
ساعتی بعد وزارت دفاع این کشور اعلام کرد که روز چهارشنبه ۳۰ موشک بالستیک و پهپاد را که ایران شلیک کرده بود، شناسایی کرده است.
سعود عبدالعزیز العطوان، سخنگوی این وزارتخانه، گفت: «از بامداد امروز، نیروهای مسلح ۱۳ موشک بالستیک متخاصم را در حریم هوایی کویت شناسایی و با آنها درگیر شدند. این موشک‌ها بر فراز چندین منطقه مسکونی رهگیری شدند که در نتیجه آن، بخشی از بقایای آنها سقوط کرد.»
او خبر داد نیروهای مسلح کویت ۱۷ پهپاد متخاصم را شناسایی و با آنها مقابله کردند و افزود: «این تجاوز شنیع ایران، تأسیسات غیرنظامی و حیاتی را هدف قرار داده بود.»
وزارت امور خارجه هند اعلام کرد که یکی از شهروندان این کشور در فرودگاه کویت کشته شده است و این حمله را محکوم کرد.
این وزارتخانه در بیانیه‌ای اعلام کرد: «ما بار دیگر از همه طرف‌ها می‌خواهیم که به چنین حملاتی علیه اهداف غیرنظامی پایان دهند.»
پیش‌تر، خبرگزاری دولتی کویت گزارش داده بود که حمله بامداد چهارشنبه به فرودگاه بین‌المللی این کشور چندین زخمی بر جا گذاشت، فعالیت فرودگاه را به حالت تعلیق درآورد و برخی پروازها به فرودگاه‌های دیگر هدایت شدند.
اداره کل هوانوردی غیرنظامی کویت هم اعلام کرد ساختمان ترمینال شماره یک فرودگاه در این حمله «به شدت آسیب دیده است».
شرکت هواپیمایی کویت نیز اعلام کرد پروازهای روز چهارشنبه خود را تغییر زمان‌بندی خواهد داد. با این حال، اداره هوانوردی غیرنظامی این کشور ساعاتی بعد خبر داد که پس از ارزیابی خسارت‌ها و اجرای تدابیر ایمنی، پروازهای شرکت هواپیمایی کویت از ترمینال شماره چهار از سر گرفته شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/75897" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8H8H0ceN6URlwOo9Wx04hEYwVHpbotdik6T2NARpEm3Varh8SgBTyOFucEGqy-wqYFUF_Hz1kbaPZz2x1KqKB84pqu-o0FHrZjX1giMx0_AhTgyODiTPt8QIOHVJb1_Awt6oh_PXXOS-kn2fgq96kmG9oNiGP-os0xG5pMn9agemshiOKxRWv4XXz79ufRU9F39FcHYp4MnewNfYZGwR6RASRMb-ukgF5fD4qHwXzMBRZsXnS5FsphA46HZQzKO5h96KVLPcjcb7fpnF5I4VTVkyVbVOjaUaYZ2IgvekCWiYnWUcZBXPzAgO_ujha5Kiti21QMKZ7SQgxej0Yr_yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان وابسته به دستگاه قضایی جمهوری اسلامی، از اجرای حکم اعدام فتح‌الله آوری، به اتهام قتل محمدجواد بخشیان، از نیروهای انتظامی در جریان اعتراضات دی ماه ۱۴۰۴ در همدان خبر داد.
خبرگزاری میزان مدعی است که در زمان دستگیری، «آلت قتاله (چاقو)، هودی مشکی و همچنین همان کتانی سفیدرنگی که در تصاویر دوربین‌های مداربسته محل حادثه مشاهده شده بود»، کشف شده است.
خبرگزاری میزان مدعی شد که آقای «آوری» دارای سوابقی چون «آدم‌ربایی»، «ضرب و جرح عمدی»، «تهدید با چاقو» و «شرکت در سرقت مقرون به آزار» بوده است.
اما خبرگزاری مهر در ۲۹ دی ماه ۱۴۰۴ و زمانی که خبر از دستگیری وی در غرب تهران داد،‌ او را «دارای سوابق کیفری و امنیتی» معرفی کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 267K · <a href="https://t.me/VahidOnline/75896" target="_blank">📅 16:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75894">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TUQ7HK6dUbVEdt_XzeBMix76xqhzuqsGD0gXx7chS-C2EZr9Qeok0oD9REjvD1bnmeqpMhc7pe5XDcZ1XbnVtJVrL7s4zP21ljwAkkc6cHkuOeTstzZMaUibuFtVR1Fn7Jikb1cmqstP5tUayZnToYwIBaD88w2BWmwLmJgU1yiMTpsBBo_DmtkA9b8c14HrarngUQ4VbfcGdh3dv5M8c17x4A9k9fdanfL_qiF_xWJ1WpgQ45kfPh6TG57cCyHafatOCsv35edGZ7bSO52HEBu7_xoOqtXAiom5OefHHTeJaN35JUr0souPRiSzLiE3P8KqxoE20RafSnq1LEno_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/TUQ7HK6dUbVEdt_XzeBMix76xqhzuqsGD0gXx7chS-C2EZr9Qeok0oD9REjvD1bnmeqpMhc7pe5XDcZ1XbnVtJVrL7s4zP21ljwAkkc6cHkuOeTstzZMaUibuFtVR1Fn7Jikb1cmqstP5tUayZnToYwIBaD88w2BWmwLmJgU1yiMTpsBBo_DmtkA9b8c14HrarngUQ4VbfcGdh3dv5M8c17x4A9k9fdanfL_qiF_xWJ1WpgQ45kfPh6TG57cCyHafatOCsv35edGZ7bSO52HEBu7_xoOqtXAiom5OefHHTeJaN35JUr0souPRiSzLiE3P8KqxoE20RafSnq1LEno_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">.</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75894" target="_blank">📅 16:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5e49979671.mp4?token=gt9Ox-apQomx8TgaxwMbAR3M35Y7gf_thJfNs3gLmeF6t3QbupBPUa-8on-SRiVik8zp8U_DyjO4dzaua1JS94xjuEdLlGnkpJ61Gg7Fiwyff_rpAx8zsObV4KwjUbvgVILXy9VR9MxH-9RUQoY3vtI_ZhTeywy5UYC2UYLy6UmOrkzVsqmCWswXB5TGJDgpDStsRV0PVdNY_KkjYpGinjUnTmhkXXYv-E0JXygkro4U3jqI6VIf4WJm-qCfT9EMePN5ED4EIHl7c1Flxgxe-1PmZZw3-vI7qnKvZGNCnEXxd00aV09vqLBYaDdITZGWQWWvf6lDK-x-dKMcmw3f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5e49979671.mp4?token=gt9Ox-apQomx8TgaxwMbAR3M35Y7gf_thJfNs3gLmeF6t3QbupBPUa-8on-SRiVik8zp8U_DyjO4dzaua1JS94xjuEdLlGnkpJ61Gg7Fiwyff_rpAx8zsObV4KwjUbvgVILXy9VR9MxH-9RUQoY3vtI_ZhTeywy5UYC2UYLy6UmOrkzVsqmCWswXB5TGJDgpDStsRV0PVdNY_KkjYpGinjUnTmhkXXYv-E0JXygkro4U3jqI6VIf4WJm-qCfT9EMePN5ED4EIHl7c1Flxgxe-1PmZZw3-vI7qnKvZGNCnEXxd00aV09vqLBYaDdITZGWQWWvf6lDK-x-dKMcmw3f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 398K · <a href="https://t.me/VahidOnline/75892" target="_blank">📅 08:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75891">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 407K · <a href="https://t.me/VahidOnline/75891" target="_blank">📅 06:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJCjOysG0wOQFPJOCki9USQFdqNEOPvlrMUVEic_-qZO_ser5k_p0qvGe_rQLvhfC2riUV9axBpzgXjvawSk6edC65d3JL5oT1KcU7Zsr6vJMFlRrq8tVjAXrbvEYtcNyWYKzxV5CkzKkbb-NwJGMVmkVU3Ef3YQTnqWpO1cu85KVuf0HBQ87D371HbcK_6c3FPyXdwqMBMN0ukvLSARNJH2EvW0WLIDtIw9VpYrHkbuGmDCEU77DrOIEYvDkfpg3aBNz7rFjNeUeEyxNEMyR2de2dVQOkBYJJatDFp6IKF6PlvnFkdvhcFfdkIjrMzd7dbgi4w_XT-eIvvPr6MROw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/75890" target="_blank">📅 04:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DAvUisn6xvOKF_LwrB_tcRNRvsHzvIr5FJw427XaLWuKTHNyr_UAt8cXSjFCTveF63rKfBjeNMyDg82W-gT5AFgAhSM62U7y5CVhuNjnhBQXMTS9Kov8_m4w99FU9qclXQNSjEOJgjyQcBMSl7N4Dql8PvtUHssJnR-nJ3n2PB1_KeE7uM39vXntMtCXs60jakH9mEpKnKnTtLyOqz0wDUGDfAXR1K6lgq2NLvWY68g-DzEOj_NvFaTJ6OBNm-HE8eDpy39js8TwV-eYt5kqswyWuv2h8L6eKlmImnvE73i8XrpU-Fg_lC0NvD4PLPj5b1bFVDOxXpwNWJWYs5ngJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 350K · <a href="https://t.me/VahidOnline/75889" target="_blank">📅 04:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75888">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rgk81NQ-UN1PyQ4JupgDO4Jd0E1Ie7SrAGqEIqLGYgmAkJMPh4vjzV61X6LCghH6vWn38lM54MmYolreo-XJOUuorb_QR53lbRPF3NuuTEDE-STJie7BrTAQ_Z2EGnYP01mu5n4Jk-XDbRpix9BDavQfFii9Dg9uKSPb1WvLPqyNWRRqcVRyG29F0IcuZD4gI3OX6n0wAoGHUZkWDmrdehdmkMbYJBCdabLOG_r5EnDfLXid2awISxGwfQnioU2IXWihkyxu3Ew7x1-hrI5lusxp91phn1xLQzHm63VRvJ_Tp1B06rRB4GVd4dsrCJzLHOasoVZ-UgNB1dYN-QkzWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75888" target="_blank">📅 03:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75887">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-hfAkQIoVgp4gjNlYxzj7yh_m2p41Xx2cbJ0U6jzOXLCLFkOEOgYyWxyEUekp97MpF3-LSIIpJbobPm_TQBaeSBfoJmfWS8mrzHBD-yqfhVSSOwMW7gCO2z-RZa6mmFWpbcSM-uJD_QDgAvh4ZIcjodc-JGend1l8UIa7LOZ8-6F5vYmQciiLxFIlqXeE2kCoLeWj5gdW-eRTwNBRaiDgJcx-Hle2fU7EtCEjuM0yh49IMqi3BRIPfVKHwE-yqjo7XkAQdJvWigo7g2v1hWxta8SbMBsEzkTsd6QxthRij_NyfPr4hCQE8OiLfiR11mrr7a46tOH7t659xi77UbDA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75887" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75886">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KJmGMf1VKaV3YVfORRH2TJI-z5ThdnRLeg34KZ3VvXG9N-SREc1LzL7Z3rAcupnUPiEmRt8aTNCPnhqV1qMyxRgfgvaCiLbH7AyLMgJu7pDDIeNLhQKAOcMhfbjtIsde5lxt650mjAuI7DQjJ145RY9kXYuma7zEalhoxsqkgkJ3aj58PQMVANm--gkuvcqnaVhK-jlr3upLJ4-6ssPnoSHsS6bH7EKBhKT0ie5XPEB3p1icUY_1Wr6b18KOiG9II2cByPCRhC1Kw_576RvjLp5Q2dSgbFhZXRbyos58JxN9zVLjzgFKKgO0pRuQGrxXHCzjOLMd2eUpiuJl329qIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 309K · <a href="https://t.me/VahidOnline/75886" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75885">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyaVj4zDc2qwYfXvviZKuL176aDUlhnClgayXC3nNl668Po99Ez1s3d4nPAVlcSwUa5nXJkqu6B_MrPZOnVV8J313Hoc9vEIalGW1y9CFrNEuZNAdXUNmhjLugeIokXPOnt7-jZ4dcrFPa46SUfBE8zUjxOln4JBUmQDopnCJIHmZRvBLYOe8uV5FpDxYj7kBbAdznSJuQpEjHKe-grUp_78vc5Bl2yTjOqBh0sxzP4pK0x0X16a49xY2YDacf9u5Jm1FwOQEsDrUX25Iv1KfJhdwtk6qMRnp1T6P0w_rcvOyztnyJg_dQ2vSoIYXjnP6IgngUJcV1pBri9VDq2qyg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75885" target="_blank">📅 02:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75884">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o4TTCD_dddOqZlPRRQ7nrDDa_-cOY3icphAZ3CYHiDBgE_AtOmikRLogcB5jPSfwSx9hnzfNUhN4bcOxaO741YODo1Y1lVrlEHQ79I5hSGZxNyXc5gg1HJ8U-R5gIUtZxghv3rTGr-_CXfHZfPkNHIRFNMyQ_ygXStFOLuua-f-xRWTwEQz8zDYR_jQSOxjqwbDczEoi93IWNLTvqejj6fMiq45YN7oan800b8qtA-2XQsVHTmbAxnwt6q5Dk8wI05pyNl0cFz6tlt3m0wLlT1qF7PUJ9SEr6j4-dsIom9H-I8-035oUdve5YA0jKmeiW4oQIp2PodsfpYY_6SI3_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 348K · <a href="https://t.me/VahidOnline/75884" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پیام دریافتی تایید نشده:
صدای  انفجار روستای نخل گل قشم
سلام وحید جان
قشم صدای پایان جنگ در همه جبهه ها از جمله لبنان میاد
خبرگزاری مهر هم نوشته:
"بامداد چهارشنبه صدای انفجار‌هایی در محدوده شهرستان قشم از سوی منابع محلی و ساکنان این جزیره گزارش شده است."
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75883" target="_blank">📅 01:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=IB4_pgliMr3qPq-dKvlCu88NSRKFGYQYkCnguTJVPUeeUzFNNS3K2r6f4Hte6kOxTcqCG775P1rSek4AwEQ-aDaSnjVmnb9vQyFjXfVy35rlpCghftk1n8MkFJ1RWz6JsI9HwjfW2KKHVHT1RJedXdKklZAgWvkFb_SnWAN4EKVnBy1vvq9WFsbPZkBZMiD9YadgRekDjWy1LZBHpUXC1wUbL36MHe-01vd6MGX5OYDqs1on3SPGRrTVjO8MEYLwM5Sv_HSQZg2BYW5PVlwu3ZbfhZx5emBrqN8xRBuY4_SARhOJQ5IP_fsMdrZjBgMFzqIxgAcH4DjOfCDFtkcZ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f311feab7d.mp4?token=IB4_pgliMr3qPq-dKvlCu88NSRKFGYQYkCnguTJVPUeeUzFNNS3K2r6f4Hte6kOxTcqCG775P1rSek4AwEQ-aDaSnjVmnb9vQyFjXfVy35rlpCghftk1n8MkFJ1RWz6JsI9HwjfW2KKHVHT1RJedXdKklZAgWvkFb_SnWAN4EKVnBy1vvq9WFsbPZkBZMiD9YadgRekDjWy1LZBHpUXC1wUbL36MHe-01vd6MGX5OYDqs1on3SPGRrTVjO8MEYLwM5Sv_HSQZg2BYW5PVlwu3ZbfhZx5emBrqN8xRBuY4_SARhOJQ5IP_fsMdrZjBgMFzqIxgAcH4DjOfCDFtkcZ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75882" target="_blank">📅 00:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75881">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q0GaQnf64dDVqW6QbB2zgpsSp7nQkGj7cEqWeRKUws9ejp6uyD5g5RjYWAwxLtjKblMR7Z45YjglftctFOjYl0UrTgVbLQOxPCjHx9AU_C-Mj89lneBh511waUniKGu7UgnzDC3n9wCVoL1nq71YOwb7O7gfX0kxeF9XeV9uznYz5dxG58eNntGOjbOPANFpXr_Ut079SPAVRvgHiiHhTErVfi5wfBPHRIUsV_lnxKDUpXX-iUUw8Smhkhab_RzVEMu42VyAyqI6bwlvSTL9_xf3mEkVpzdgVAMNJUekvRGUOaloQX7SvQv_S-_GDFGX8BTsSi1wyYDemkOF1Kl7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: گزارش‌ها درباره توقف مذاکرات درست نیست
ترجمه ماشین:
گزارش‌های رسانه‌های اخبار جعلی مبنی بر اینکه جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز پیش گفت‌وگو را متوقف کرده‌اند، نادرست و خطاست.
گفت‌وگوهای میان ما به‌طور مداوم ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش، و امروز.
اینکه این گفت‌وگوها به کجا می‌رسند، هیچ‌کس نمی‌داند؛ اما همان‌طور که به ایران گفتم: «وقت آن رسیده است، به هر شکل ممکن، توافقی انجام دهید. شما ۴۷ سال است که مشغول این کار بوده‌اید و دیگر نمی‌توان اجازه داد این وضعیت ادامه پیدا کند!»
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/75881" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75880">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Jb4CkBNqHTMtI_bo137xHNKzTQwu0lw-Cas5o5OyRRej3fmhzVsKuO-JNiSZY4qs5jEw7sudUh0hU3YgOU4LIMpfogSU2gKzkizOQZnkthf_ZPCxVn9b2b3Ueh8ZYqTLwvO7bMbKp_p6Q4wjsUeWfsw6maEBoxe0iDgDz5h_UygmNRoCIoWRfGy8zKzD9BZX2yQ0tmJVi8YF5mGkhlU89grMNc619PC0VvAR3W4k5vxGGjD0bvq2_dIrABJflGlji0G4sizDEsf0wrIO-qH-JOyhmtdJF0ppUJsHObrRHD0miibEDcLGj3HZFHo-fR9ve6kIS_vlk-6rnXn9hYUs9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا در جلسه کمیته روابط خارجی سنا گفت که نشانه‌هایی وجود دارد مجتبی خامنه‌ای رهبر جدید جمهوری اسلامی در سطحی به شکل فزاینده‌ای در حال مشارکت در روند مذاکرات است، «اگرچه تمام ارتباطات او به صورت مکتوب و از طریق واسطه‌ها بوده است.»
آقای روبیو افزود: با توجه به اتفاقاتی که برای رهبران متعدد در آن سیستم رخ داده است، تصور می‌کنم که حضور بسیار علنی احتمالاً چیزی نیست که در داخل برای آن‌ها توصیه شود.
او همچنین در پاسخ به سناتور دموکرات کریس مورفی، کاهش تحریم‌ها در ازای بازگشایی تنگه هرمز را رد کرد و گفت که هرگونه کاهش تحریم‌ها باید پس از امتیازات عمده در مسئله هسته‌ای و اورانیوم غنی‌شده صورت گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/75880" target="_blank">📅 19:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uvKYOEyfkdxebi0fZoPTuOlMBZOqDa1-GodcGE1bF6pYU3dL_cD77eGHQJKgsaQWWZhF3Q0OsP_RClFiMZgUx2FE1c6Z60Nhog4_KAHK7gkogMWX2MSsmDcEXruqiM3VoAPb3KT7QIK52w0FUw1yDJPXHx9kdqyIXhlQGJBfI14mfIMPMUMIYxd97UbA5aBbffMW5ckmSI6bTJPK_SuJmUY7POtcEaeuOVxo-YkTv604gvnVjaZ7JIaCFBTUTGP6z5xjkoUcyULe9axka6-Z3gSaEapZj02OlDgq4W-9cbC6tdIKmeKWRYc8rrgbya8pbhOorITtUkPHNkrho4Nu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eFg2-x4w_GxP_B7wbghLxR3P41dXf_Bqqp8X6SQ9SJd69JWfRSKJcyM_IJDkQIaCxWxueWS0HH4vdCz9n-3twqFe9rzDqDPFwONWfE9u8tFJJGrSXXDvYJvXRQtjHy7sdTDLfywXfk0XhNiJthyR8zS-BkeW9fQcUc4X_CifPLA1eihN_KE9AAZDos1m2LecKSWD6tEtHRC2PYLkg1mldIspc9xmHQYLuLoUa2BWGGB3Jff7Mb2ChVHHrPGFJBQuQHv1UvvXvFbgIQQ2DnirkblMEHm8xv22B_9U66ae-KDpHK75_4cBO9v20mS4NjI5qCrgNbHT5hb0LSuaYFEhNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 346K · <a href="https://t.me/VahidOnline/75878" target="_blank">📅 19:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgmvz72aYz5_OyfYDXH-fGTOLd5UpVMfXcGGFrhFFiqTBL_hfpFr4MLXJMmMOB85dtky3fV39o5xA5oAkvUgdy2SIBCeQPULXY9FzindwFrdcKB4RbEq_eh3B_3Ja2ehnK3maeSTGT2z6ww4XNJ7y6fUNpksmjJ0eoJF4Y3G4JNhCGeTQuHfAKp2NHWDHoXFZkP4FS9cVgQGFjZ4auVtsVGS4HErznbpdMR3J8L5RdQD_EfYLQdJxVQKmsUc1lXyC2NEgtH6zM2xGwwbV_MlDnnmyI7mvy148aQyZfLvz6ob8QhzJoiOz9x_gV9PXrbrl1Up34r4QYxdHhS4xwNszw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسراییل، در مراسم تودیع دیوید بارنئا، رییس موساد، گفت جمهوری اسلامی تاکنون به دلیل توطئه‌هایش علیه اسراییل بهای سنگینی پرداخته و سرانجام این حکومت سقوط است.
بر اساس گزارش دفتر نخست‌وزیر اسراییل که روز سه‌شنبه ۱۲ خرداد ۱۴۰۵ در شبکه ایکس منتشر شد، نتانیاهو در این مراسم گفت: «هر کسی که بدخواهی علیه اسراییل در سر می‌پروراند، بداند که توطئه‌هایش شکست خواهد خورد و بهایی که خواهد پرداخت بسیار سنگین خواهد بود. بهایی که جمهوری اسلامی تا همین‌جا پرداخته است، بسیار سنگین است. پایه‌های رژیم وحشت در ایران ترک خورده و دیگر به آنچه بود باز نخواهد گشت. من به شما می‌گویم سرانجامش سقوط است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 317K · <a href="https://t.me/VahidOnline/75877" target="_blank">📅 18:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UtJfM_HTZemyY_U1F2dPUYJd-FM0fRs4aCNW3GVAyjg3P87ikkuGL62mOgb52Z56EWfRRaMLvy9IG4-HS9nWaDnKFidyV8F3j9pJF48FmZtuF47mWk8YIT66Z0yazZs_S9C2We40vB-2KllurIvGmzGXJMC9TBkDDtVLJ3PJ4W1-Qi7Wg1OR28DU0o1zVQX-2ZWDX45dz94Q3Z_mcktBlpb6jx8HLDbO0ytplMLxw7VE6tFNOkUr18-SZBtb_CjoJnhhEeVsqfJ4vM5iBOk73C1K36F3DThlzRAC4aQFNSwHzpYGvR0LsOP-U03D7MVC869AWL4m3ROjhOv8v9Z0sA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/75876" target="_blank">📅 18:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75871">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTXoaPBGt0BqSFvyYODBLQzhc9A02yhLGFrjietJ9VZ26m8nK-RKPrcVKf4EZ8XP7WlQVxIJyuvGDen40OHUN4ct7MdN-VGvzUPOLC086fQdtR4be0qKCPV6ZR8IXw8oUnATTRMv-sdm_pV3U0m-pnclwkQlRIIlS-ONPWJhKc5S59SuixVxRC-HqMw9J4diFpLgAyr7GNoaNukFbrVpIpCZ4QcmgekhHQK7NhOStF3USYkn-RHOXIsqCoMzmTDn6vaO_TQVhd9l-rOnDXVjHFP57zAtUOv9MSGn4D6i58fPpBanUFe-bwr8y_RwgX3xB7ouEEUSNrRjwVC9Eb21HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=Pv_btrtIGWOXHi6nbXlFgrHNZKosZN_AmK_OKNRxIHe5XUx6E0_mD7fO9kps8Aa12lJcTZ41LPPjHhYxE6RgGT9xmhu0WjcA7YIxITk9gh50NGMBVx8bfN-oeNw-InzSV_Qqt9JeQtDkFRFFqBIpvTIErLUlzA7U_GX2WIQjRYq6rXwIcdcy89eLOA0dwJFHsj6fmEDO4Cq6pndXTv0dcvPX3sUqNrSm9S1FSmldjxCzpoDrabx9YdztbEHOoP29j5k2nfHJT5fM0RkJ3pfFa0ThcAg5wGZsOlTEphPEzrqOYHrbcblegbkyf1-cCCn8417QFAPEtNt8rMEpyHzZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/92446ed5db.mp4?token=Pv_btrtIGWOXHi6nbXlFgrHNZKosZN_AmK_OKNRxIHe5XUx6E0_mD7fO9kps8Aa12lJcTZ41LPPjHhYxE6RgGT9xmhu0WjcA7YIxITk9gh50NGMBVx8bfN-oeNw-InzSV_Qqt9JeQtDkFRFFqBIpvTIErLUlzA7U_GX2WIQjRYq6rXwIcdcy89eLOA0dwJFHsj6fmEDO4Cq6pndXTv0dcvPX3sUqNrSm9S1FSmldjxCzpoDrabx9YdztbEHOoP29j5k2nfHJT5fM0RkJ3pfFa0ThcAg5wGZsOlTEphPEzrqOYHrbcblegbkyf1-cCCn8417QFAPEtNt8rMEpyHzZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 280K · <a href="https://t.me/VahidOnline/75871" target="_blank">📅 18:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75870">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bxTjnoUxC8727hrFL6-K6pT0-c_nBoIWj-oD5wi6C0rXVb9mTqHNlgav2xRTepogFJf7CObrQX0nER-9Stxcg33DAgMsYMy6O7kyoii8Awy5s4mPmUYEGwa1c1QfgVVLaIeYMJielyYptET-u3pVwqSd7_T4bL0rFZoXGznKFu3HATwGMBC-MaCIEgf_jKwsbnUdJgVtwonKeqOixV9XcpDUc0XN2oTL-C7Ursh12qrclzEopQM-iYkQYhdz6NaIpMZXphG9ILaaTfKSM0L-7VeUEl8AYs8JkiwHjaFaaEWhooVhkwnWmQ00uruSjvbs6dmwSzDq2ZhbiiTgcm12Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 272K · <a href="https://t.me/VahidOnline/75870" target="_blank">📅 17:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75869">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjHWyPNgQ9yh42Mah_4CRBXDONPW6R_Efs5u4okgJqvK0R-XCWF7ciFaK_caRzdEkSLiQbmD14c-r9OaVyvV5m_nSTrdS1rSp00ydW81gzhR7UsdyiOUjQguzINPJL_spMWL1Wc7fHlTHb3cX4e6J8l7qR9FQUOC506DUi3TjgXEoZU1TK0J9Ai8AbbFQNwV9Fra6noRCjykIHCcalck0hWNNKT_1xko625EEiuHullsKPEvQJ2gpp5DaO5hRPXO_f2LV6UZp7eZWPo0NfDGQG2I_KSFh3ww0xWB2a8GnxqYTkwsuXrnjXCNa-8zTM43E6Z1LgIGZeyzaFjZvjbqcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/75869" target="_blank">📅 17:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75868">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwjP8Xus2hV5AjCh_5Z1lseA4G4qwODRWH5JQTt-VhraBQxC0yf_COdG2uWlarIyxUPO4XHkw_g18EkT94iLXC8ePbV-cK3GzO33pqqRz3d5pKM9WJLbUgZmQHafyPw9ytz190rGc8YNsENwRb_Qm3kCYXYFzGwHa0pTVqZBJnhW0vOPj4M0aV1m2qBavZIzsPRu6ZWcCZE66rb4uQCHD1wuLUmj5VizZYYPQi2sCkXbBLgnhG7-BKoTkqGY7-3xUph6Gcyg5GrpK2n_Ar2O07sESyczCyNI-Qch6TZ3sDF8hrO6CyPSL4KMM7BFmS1S2xaujvCFKfHMDRU9Vvp1mg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/75868" target="_blank">📅 17:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75867">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=OjmbH5-kcDAw5eMLudYYGymtsy80XNYo25JxbdvxaOB09clEqGXix1I05J1IKZFn-6oOZR3KFXPyWIeo1C_oRiecpPyl0W6rpaoAf3KqJ8cfUGSd_mE9RRZyi8hZQfmOLE7sHmRCAEFi6nu9qYb1l1nwGv-6HE7GUGeIgpZeKAFCwvJFv1ouUDLKRO0DU-gmR1GaHzvGux3xYQkYI-uJn9JF5V4i9o_OoRQ_cC6MxRNf1uRKq7YmozDE1-KS1jBDUvRRUf7ScLQeyl0cTSDkMMQzU1pUDXf0OfDEfaY9b1fMjDwytL1hGAojMT3PvdIcxUYiKeSF7ZovfRHwULJr2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/695f2e3957.mp4?token=OjmbH5-kcDAw5eMLudYYGymtsy80XNYo25JxbdvxaOB09clEqGXix1I05J1IKZFn-6oOZR3KFXPyWIeo1C_oRiecpPyl0W6rpaoAf3KqJ8cfUGSd_mE9RRZyi8hZQfmOLE7sHmRCAEFi6nu9qYb1l1nwGv-6HE7GUGeIgpZeKAFCwvJFv1ouUDLKRO0DU-gmR1GaHzvGux3xYQkYI-uJn9JF5V4i9o_OoRQ_cC6MxRNf1uRKq7YmozDE1-KS1jBDUvRRUf7ScLQeyl0cTSDkMMQzU1pUDXf0OfDEfaY9b1fMjDwytL1hGAojMT3PvdIcxUYiKeSF7ZovfRHwULJr2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها دانش‌آموز روز سه‌شنبه ۱۲ خرداد با تجمع مقابل وزارت آموزش و پرورش در تهران، به تغییر قوانین کنکور، افزایش تأثیر معدل و پیامدهای جنگ بر آمادگی برای آزمون سراسری اعتراض کردند.
در ویدئوهای منتشرشده در شبکه‌های اجتماعی، شعارهایی از جمله «دانش‌آموز بیداره، از تبعیض بیزاره»، «دانش‌آموز می‌میرد، ذلت نمی‌پذیرد»، «وعده زیاد شنیدیم، عدالت و ندیدیم» و «فشار روانی کافیه، زندگی‌مونو پس بدین» شنیده می‌شود.
سیاست‌های مرتبط با کنکور از جمله افزایش تأثیر معدل و تغییر در شیوه برگزاری و زمان‌بندی آزمون‌ها، در کنار شرایط ناشی از جنگ، در ماه‌های اخیر با تغییرات و ابهام‌هایی همراه بوده که به گفته داوطلبان، موجب سردرگمی و دشواری در برنامه‌ریزی برای امتحانات نهایی و کنکور شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/75867" target="_blank">📅 17:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75866">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gAlAQ_hTmUQ575JnS1MwZdpv6gj8sdq3BPfzrK4vHv76sFohy4mg9GjUBhG1HMG6ABRHf1qnq3rjD1o7e7ZZARmLNTsNObwGS4z4RmU8z5pDKj2mkCsW6_yanTexLd51sguqDqT9Gdl0J3Hb5RLHPnyDOjqyHKiheQCir5Xo_f2Pxh6kWCavcJWc4WRCJdJwvZve91xgw0KRm5KL7trcmQOBONV1skniNFQIX8h8nqdcnqPrYvZYEbVuUeZuBjDoXlJi6DClU0trj2n6WeYhSYsErmKxEOVkwKMOh30KabTxPmjcDtJcYIwFpfCz0HaS8WYkpO0Fam45BBeutHvp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای سومین بار این متن رو علیه بعضی از رسانه‌ها پست کرد.
ترجمه ماشین:
اگر ایران تسلیم شود، اعتراف کند که نیروی دریایی‌اش از بین رفته و در کف دریا آرام گرفته، و نیروی هوایی‌اش دیگر در میان ما نیست؛ و اگر تمام ارتشش از تهران بیرون بیاید، سلاح‌ها را زمین بیندازد و دست‌ها را بالا ببرد، در حالی که هرکدام فریاد می‌زنند «تسلیمم، تسلیمم» و دیوانه‌وار پرچم سفیدِ نمادین را تکان می‌دهند؛ و اگر همه رهبران باقی‌مانده‌اش تمام «اسناد تسلیم» لازم را امضا کنند و شکست خود را در برابر قدرت و نیروی عظیم ایالات متحده باشکوه آمریکا بپذیرند، نیویورک تایمزِ رو به افول، چاینا استریت ژورنال — یعنی وال‌استریت ژورنال! — سی‌ان‌انِ فاسد و حالا بی‌اهمیت، و همه اعضای دیگر رسانه‌های اخبار جعلی، تیتر خواهند زد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا به دست آورد؛ اصلا هم رقابت نزدیکی نبود. دموکرات‌های احمق و رسانه‌ها کاملا راهشان را گم کرده‌اند. آن‌ها کاملا دیوانه شده‌اند!!!
رئیس‌جمهور دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 406K · <a href="https://t.me/VahidOnline/75866" target="_blank">📅 05:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75865">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 376K · <a href="https://t.me/VahidOnline/75865" target="_blank">📅 04:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75864">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/75864" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75863">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5RQ-5xcNxOYwPAWMWenPQlhGHjDYvNov2K0ay4VHXFW-252jkej8Dv5YVLXAFQ8CX5j1HEkVSMPnKmlTtCZWBK0m0QVizgmMkt5E-XeU0-MHbxlS6aRSKD0S10Vy73k1MjLLof8GOK73TdKvZ1RFJOH8YLxLmaQSDLTVS44WRd5ER9ctXDr2fCUl_TzWauKy2tRqmex9gV3e3kWtcbqKaWmE5octCCzBpzHVKUqhubGASKTo6YpaNNSeJT-Mg-iYVwKDwzD5MUifEPFvbkjp9TPlOyWXg_m79ZMKacu-OQVkZ6dHcSnIyOtPz6vIt7fzPTMb2aJvAg97KlV8Sokww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفتگوی تلفنی با شبکه خبری «ای‌بی‌سی نیوز» اعلام کرد که به نظر او، توافق با تهران برای تمدید آتش‌بس و بازگشایی تنگه هرمز «طی هفته آینده» حاصل خواهد شد.
ترامپ روز دوشنبه در گفتگو با جاناتان کارل، خبرنگار ارشد این شبکه در واشنگتن، با ابراز خوش‌بینی گفت: «اوضاع خوب به نظر می‌رسد.»
رئیس‌جمهوری آمریکا با اشاره به تنش‌های اخیر افزود: «امروز مشکل کوچکی پیش آمد، اما همان‌طور که احتمالا پیش‌تر متوجه شدید، من خیلی سریع آن را برطرف کردم.»
او توضیح داد که این مشکل ناشی از ناراحتی و عصبانیت مقام‌های ایران از حملات اسرائیل به لبنان بوده است؛ ترامپ در تشریح نحوه حل این بحران گفت: «من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید؛ با بنیامین نتانیاهو، نخست‌وزیر اسرائیل هم صحبت کردم و گفتم تیراندازی نکنید، و هر دو طرف شلیک به یکدیگر را متوقف کردند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 360K · <a href="https://t.me/VahidOnline/75863" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75862">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTq4Y1avJkm71wqEPPuz6zFATPhuyv3AFE7bxgBwe-aEx9luzfo2WPnMAcPYToj4a-fXwOc69OTcLhNoB5ByycKqbVCR3_W3msqJQZ5iBc4aG8QsI8SnPThgKDbDUCOq6QQmcnoIxa4HjrhKh5wo75GZYPrCdp1MPh-68Bre8xXAT2eUtIiJ6cetmxOVCyxaUhhz_S7ekxGoNHFzG6xUiTat4Uuwo-ovAAOG21ntmS4-fI-mckUMLtUpj3VI0N8kDc_It46sKuWyaTd2XvKWQZuPIP-9EpzrVhudVLNpkIXS4icON3DRC3Rc_hg9YTnz1-db65t6rxI2gjMxqihDEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75862" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75861">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lJ_vf3n7Cxoj9yaySqp2HJWEX0Ttzkj1SwhMvXKwYTa1q6NS8reOFuBdUxnHbApgBZ-FPv_7xbsFoVWbuf2aYgoIszSZ5nd28t6sQsnael4WgaMBUeZRhOsybusq-f8euNPsAusQ7LAukmD6GSjan5jb0jyRRgQAZq6I1JEm1pEqWWcasZekcjE_WmO3YJeYfTCrMvIEitvuVADja0WvLh_EnI3dgAMhpA2a0a827wkKkUgP6F3NybEOSqb2n56aJFI_mqOOFP8DJDpZf26zWWG3xLx81guRhCjhuGc54k3AhQERCROz_FYSH2c0yOMCA-uHTh33e5x76i18hqI7gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری جمهوری اسلامی، ایرنا، روز دوشنبه ۱۱ خرداد از کشته‌شدن دو سپاهی در قم خبر داد.
این خبرگزاری ادعا کرد که این دو بر اثر «انفجار پرتابه‌های باقی‌مانده از جنگ اخیر» کشته شده‌اند.
طبق این گزارش، سپاه این دو نفر را حسین رمضانیان فردویی و محمد اویسی معرفی و محل کشته شدن آن‌ها را منطقه فردو، در استان قم اعلام کرد.
با این آمار تعداد تلفات سپاه در دوره آتش‌بس جاری میان جمهوری اسلامی با آمریکا و اسرائیل، و در خارج از درگیری‌های اخیر، دستکم به ۱۶ نفر افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75861" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75859">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=e8RM7c0F_g09jAchskTkemN9kJNo1n7dZYKPK86yyKJuYuQlnAuj20Tx2JecMoq9qVIUYpvE02t220eo_uBqQAnvFZO5wHUmlWkfayoFd-ooHcUPgC3HZTIk44d0yxD9aPIi5mkZxMjhcFnXz_ePSZAIKFWicPfp0NCEZzJcvOMkRPvc7bA44Ksn23mL03BK2Edxq5b7N_WTzKO5aEtfx_cqpQWBpjF4oKsWvQ1dII9pN7gp04q4LS7dphiGQb7CdcDb04uqaQkvzBmWI7DCmlGDiyXtDG2lHQHcU6JCYOQHlKMqap25rjxSmHHDjEhkYBDljaL7Rfy3fc4ZFWRJUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2d24e12abc.mp4?token=e8RM7c0F_g09jAchskTkemN9kJNo1n7dZYKPK86yyKJuYuQlnAuj20Tx2JecMoq9qVIUYpvE02t220eo_uBqQAnvFZO5wHUmlWkfayoFd-ooHcUPgC3HZTIk44d0yxD9aPIi5mkZxMjhcFnXz_ePSZAIKFWicPfp0NCEZzJcvOMkRPvc7bA44Ksn23mL03BK2Edxq5b7N_WTzKO5aEtfx_cqpQWBpjF4oKsWvQ1dII9pN7gp04q4LS7dphiGQb7CdcDb04uqaQkvzBmWI7DCmlGDiyXtDG2lHQHcU6JCYOQHlKMqap25rjxSmHHDjEhkYBDljaL7Rfy3fc4ZFWRJUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روابط عمومی سپاه اعلام کرد که در پی حمله ارتش آمریکا به کشتی ایرانی «لیان استار» در محدوده دریای عمان، نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی «ام‌اس‌سی. ساریسکا» با مالکیت «دشمن آمریکایی-اسرائیلی» را با موشک کروز مورد هدف قرار داد
IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/75859" target="_blank">📅 23:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75858">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0RCQ9TwnOtkU9m8993jR_snSEGry4hafKf7Y_Qfj-6bm7_QuFLLp1TdVvqhw02ZxvVLufcj8Wax6XKxyL-0Ssof1MGpfH9uEmk-x5aT52iHacAJoZdok99-4Zng3sTVOEq4Ty4ti-T1eAfwOvoS6llxcuvW7yrfMuyPZAw_Py5Qcm5oAWecleu9VtFF1bIe4nfV4QVtBdpHv-69yeDrWP-nyXL7hovyGJIYrsBaDkooHYZD6Ylt5BpHqh0YiNqJRjZLSS6UX6NY8QWhisnGCP47hGhbz-lNgcGvvnAreBtrDfcY-Grc10O7Cw-cc2YJfVEbWaqFjNOc6pKV4nvQAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75858" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z4au43nxpJb-0xxjK2IjSvYVC-ehmd51OGbl7peT_nQxXSZ-3AiOoXeddbD-hl_vkCVDZmygm_C4ixuCQSqmlGleL0YOehzsXp_uwYQosjvF7u3jcJJ3MnwA1Qi9E_irFT47KH12gbd6ztn6n8z3nqukSnyQPuTSlCxBBbZbxjGX2R21EaDIINtH7KKa_vb5IaVKm1gtobIIPRHkGZzGfkc7UXNvGvgcsnESao2Bd3ns0n49D6WLny7ColVGv_Bt9sTlddWR9B_29T_BBVqxIXqEHAezgJGeLxQpj824ya7wFoPxmXK0dQNdLtgny7LA-OIL_rxOepgXT8sqeK-qqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی: ادامه حملات به لبنان و غزه، باب‌المندب را به تنگه هرمز تبدیل خواهد کرد
اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، شامگاه دوشنبه ۱۱ خرداد ماه در پیامی که رسانه‌های دولتی ایران منتشر کرده‌اند، نوشت جنگ اسرائیل در لبنان و غزه «در سایه حمایت‌های وقیحانه آمریکا، عزم محور مقاومت را برای توسعه پشتیبانی‌ها از هر دو جبهه، اقدام برای فعال‌سازی سایر جبهه‌ها و همسان‌سازی وضعیت ترافیکی تنگه باب‌المندب با تنگه هرمز رقم خواهد زد.»
فرمانده نیروی قدس سپاه همچنین هشدار داد که ادامه عملیات اسرائیل در جنوب لبنان و غزه، این کشور را با واکنش‌های گسترده‌تری از سوی حزب‌الله و گروه‌های فلسطینی روبه‌رو خواهد کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/75857" target="_blank">📅 23:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qcvs-nf5slBAJkL6KQwybVx6aDPveOUuz-qX9ajPTRx0saIHPV9KPOqCs7_VPSDtOoESne4qPyVzgx2nChGL7b4EKUGUE9ZNpfCPgP6fiW-jQL5W0qzEO0QOUeBHKKEYhnvRwTzPafJKJF66CI1tgNaSJ67fe22CU1dOWB1BSsi35bQjDQXbxaU9LWanYYgdKFqWM8tMqRIvyCXXRI33cyUBfVBZVZxQ2YjMpMjjtW7GK2Z_dwppQYDrJT36YYU1DsTWIpFx6976C24Z4sD7TjVTqaLxBYz1Qj7kg273mszXAWAZYpXiJCnrion161wHNzdyTPUR1dGrnl7xbbPGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با جمهوری اسلامی ایران با سرعتی بالا ادامه دارد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
این دفعه گفت "جمهوری اسلامی ایران"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/75856" target="_blank">📅 21:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OsN_0HOLZYLGoKYpDdSWymmnnn8Sphe2gNErwAkU98ne43C7oMy4B0yCaVWG10DYwURb32qV7rzH9jijmzIc8QpDIOp0P74KEGQBjVYDgRD2Nx79SvgBVkfkYxFqbOtztYluHj7B_iIT2B2o9HguPiPusuILeX_LTMd5IlUhqRoY_JsY0OoryuvWMEljwKs8TX_smSjJPfjkwjvuwOpoErrVOpkVc48gwwTct3x_YOrZUQ0rHBUHAkR4YgOrFHq98U3VBDFrS4GsK2ps5duCC9r9pLUrTp9khJ5EsKLaUzAV3SMTa58IBJtf8rPJoDzoF9zh-va5J8162C4XoO7obQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اسرائیل و حزب‌الله پذیرفتند حمله‌ها متوقف شود
ترجمه ماشین:
من تماس بسیار سازنده‌ای با نخست‌وزیر اسرائیل، بی‌بی نتانیاهو، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد؛ و هر نیرویی هم که در مسیر بوده، همین حالا بازگردانده شده است.
همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آن‌ها پذیرفتند که همه تیراندازی‌ها متوقف شود — اینکه اسرائیل به آن‌ها حمله نکند و آن‌ها هم به اسرائیل حمله نکنند.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/75855" target="_blank">📅 21:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V8Bmy-NkbYTPI3qdMaCJ8Yy6Z09suNig5l6kcudFbe-ePxTdg7Bfl2XhZB80_6x0ZAPzaZoLn2WFfwTuYHO4KoDxZPpySeg0auWwtM1YtXha2n1DotIxkIOsdnVncEri_leCtgn0zHV925GcLFxGh2TuIQJx4csmX3BBb32I0ACttWMDEj8NeyiwGyX1pFohwlSoMrnCycMESucj0qbWs_yoUcRPAazvk-D74y4H02nGaMYya3DqVDb5KO1v7VZtQ5b37jypNLSn-34-fjHJzXUmQA9gLTJs32X_vnz9Ntcj5RzDO5kMLS_CtBKelW4YKrONn1OuNRk3d4I4uuuY3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/75854" target="_blank">📅 20:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XKyl7-cXCtTEM2LxPWMJ7xBjJxHHqZ9huENTQGNxuUf7UQuHmbTKtqL6nXlXuw29m9qvjoRaBjOG4bIfdruxC34w7IHKM453m1UpaptREHv5htUXhx6ixsGgGmuRWqxwI6we0JPHY7c209yGDu10o5rDsd6FvpGTvnExCkPeCadx5PRkFBT2O_qjburCLS4MKlgkSWwyj8q1zVnA8d0Msw83DtNRi3Vvnhnp98MBV92kWelSz-OoOGkrFtbGbsa0IKf34gr2pBjY_NNEfT7ju5lt_47dxvq1nhIa5FHgFSIPJadrKd6rMVyijEh-69QOQWBUUBZ4VT3zfmQR6qe04A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم‌زمان با صدور هشدار تخلیه از سوی ارتش اسراییل برای ساکنان حومه جنوبی بیروت، فرمانده قرارگاه مرکزی خاتم‌الانبیا به ساکنان مناطق شمالی اسراییل هشدار داد که در صورت عملی شدن تهدیدهای اسراییل علیه لبنان، برای جلوگیری از آسیب، این مناطق را ترک کنند.
علی عبداللهی، فرمانده قرارگاه مرکزی خاتم‌الانبیا، اعلام کرد بنیامین نتانیاهو «در ادامه شرارت‌های خود در منطقه»، ضاحیه و بیروت را به بمباران تهدید کرده و برای ساکنان این مناطق هشدار تخلیه صادر کرده است.
او افزود: «با توجه به نقض مکرر آتش‌بس توسط اسراییل، در صورت عملی شدن این تهدید، به ساکنان بخش‌های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک کنند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/75853" target="_blank">📅 19:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75852">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=WUg5CJStxiqMvAZlDdr3U3z2guhHN4b2kamx6V7_uPnCK8jbflwH9IXsAqidtG_vq6UyRuB8K3sY9NkCSEERt4I9Ek2sbj0dbEWeAIOF1XcY0QOmYamoGJxK8WoYAqgveH8itwoSTJODv4pMJ2_aChxtrBu6CfjQNwJwNGdNfpGL4xTgix9aDS_rq4sgND2vWJQy7EEQ6GjRIRIIbe8rRayvjy3EpJRZ0KsgHhrydtAp4OXnoL3l6r0Rq7j_g1puSyjBaStpHhpcL_v0XISAwqzoVg7ImvDJT67HFrO2QV1dSKhok9jxChR4UPKEhrF-ZgvhG2ujPeix0B-97b4aEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89a4fe09bd.mp4?token=WUg5CJStxiqMvAZlDdr3U3z2guhHN4b2kamx6V7_uPnCK8jbflwH9IXsAqidtG_vq6UyRuB8K3sY9NkCSEERt4I9Ek2sbj0dbEWeAIOF1XcY0QOmYamoGJxK8WoYAqgveH8itwoSTJODv4pMJ2_aChxtrBu6CfjQNwJwNGdNfpGL4xTgix9aDS_rq4sgND2vWJQy7EEQ6GjRIRIIbe8rRayvjy3EpJRZ0KsgHhrydtAp4OXnoL3l6r0Rq7j_g1puSyjBaStpHhpcL_v0XISAwqzoVg7ImvDJT67HFrO2QV1dSKhok9jxChR4UPKEhrF-ZgvhG2ujPeix0B-97b4aEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«حمید سلیمیان» در حال نواختن تنبک
#حمید_سلیمیان
، متأهل و پدر یک پسر چهارماهه شامگاه ۱۸ دی‌ماه ۱۴۰۴ در جریان اعتراضات در زرین‌شهر اصفهان با شلیک مستقیم گلوله جنگی جان خود را از دست داد.
حمید سلیمیان راننده یکی از شرکت‌های فولاد بود و به گفته نزدیکانش به موسیقی علاقه فراوانی داشت او  تنبک و سنتور می‌نواخت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/75852" target="_blank">📅 19:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75843">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbCCNcUXQzmozbR_cEcpM_tph0MgDMVUYeNgO9kYNnWDZQVdIDJULCZlmhSbhIQzeC9kqtDbbdSz7eLaUA642Z_GBYCGkTUEws4RGfnq0MIOqLLol-7lg8NYLRoB995iNjLB22ic5AqhXpG_sm7ZLWsHeK94IFNXzrvPqg1r84xx6OnvUTzBA1DpFJ-lGxjzYMILU9rKVtHBIdy5BwkEwQyW3tWmyrp8DlKcIW6NDmtPHsjqtX9SD83Ziz7uD8_OzhmGZlsSqpNAoUEcJgZUArIMdwhxh6Lv8NEX0N0ddQ3MmL_J5RXwreEaPWgGAZGk4SSQaD8d0hMDcDmGIxG9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aqO75EbXO30_ibB2K5vG64l8QuOaMFXLS-XeSjN94gGwJZF2HQ5mvHsALDRgMlqHoWS09l6IzDKprSltDRUyhR7F9POA0Mkc-jLSlEH4rEw617XEdGAhk3t8kCFe-UQSwSb2rqtOpxUimfK95Y7YrN3LjqTgX_jZckhxthO9Y8WtVSDLnmZGZidouooF42r59WgPH80WvtdXYd7H_J-YDiatURDRgqA6uiJXS_mTRvuk4FitUko9EkAXk3WbyX4dD5tGJ1kjCSJvfv5ATELwI9e8ifYIv9gBmNpn01AXrh13WVm6fcmU0JYxJnMCgXDDkOSsoxCPqTovsWRsqw3KfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dRI91VDVaQqOHyOBA1K-ShvAiLc74dtfpCeMtFb7mGCrXNdltBS6B2bZbFhpckReonmaH6WCCud7n70SqDw6qPRmj2oKdtOo7dlSVUHhQU1jHOGSWXOAkdplEhaQruY-ATaNTDRBDLlJVGbBAUQ9WYKA-Fhy7FgXLGn-RSLQ1HeR9PJKkoFybahxgofDrZ_JVZLZg1-Kzy7krhnZkgyKvV_wXuzaV4eWmnIPfsKj1pv5SV5mD25ymkRp9OwaWorts72f_Ni8s3D1OS_HxVuVx-bOoMWSJS5TCyuM997ODYlcnCdmyM8rG2DMvmGaQqQL637j3lLiOZ886zJp79sUzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tkQNm_Hh7yUfHfLfdW3HI09Ef94C23ndki-sitjwEkncLdwtw9rQWLiA5MCsEoYFI_cHlhVcAt42--0lUoUBrlfi0_GsHvX4PuQRSpt2VpqyTmKdeAxVDdynT0SX72FsMnR4E_xdD2bhA9tCZDQI7JDXdt1EJDauSoP_lF1mW-htkJQ4Gr3JpkLQv93dRvkkOReweHY9eiuN0clQ4mE-JycTds5nYr6WbtW0Hg3-zKUWac7iLYANdyEknZxTmSb4VEkntNrSGTlDp1KzNRSHCOo5K3aFPbiih-40xYWvwbzzUHme8_fE5daJk4eivo5P_jaKeg4ymZEsJD8ldBfwfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rhMu6HrP4rYJ3iaiaOhs4fsOQnktbzo0aBecmFa8dwE-XsYhS0WW145LiSjdc87uH54N9qckooVZQjPPQDbLXjjFYpXKYNhGZnW-jcdHqNcsZKbzOsAwLofnr5Oop9rOWXLhVlnKPvKTIjDsHPyd2J3E7_-3-16shxtsi_JiQRXwsjd-ChHjYknYfd_exHiJ2z_jnKnAI4b4Z2c8fDXiCGfuia0VY6wwc0SpKw35tiXOuG5alUWIr2M83sxi7Yfih9BU2HkxGoMZrVpSZwrxCfnBsW_TCTpWHOxXNqHFPxU_EWzyP8DxecRlbGA0Wu-QvyhxK1LqLG2W03DUyxrqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XoB9ZWLy_ura_JPteSJ0D5N5n_AX3kkmpV6HaGP6c1G5SIS036GJEillfvbkUESNp7Nsrk33hmbJC_XeBuoNBdD-UvivUucHgDO88rVlenhre9MRsou_3t-6xKqC9ef-0Fv1h48-Ge-NWOHX-V92HeIQV2Njo4hJajzGYGzjlxSg66T5a_XIQgZR_yNz0RF75y4pTa_bZ6PqGmYf4wDwDxx6J9u5aFay0L13nf8xHpjYzJkfP3oqFtVTO6teiekYTjjeCLRyMOQl5R4Nld4atGdJoyRCThbC3p8djgWZNTxrGdAOJhuA54LF_QUvfXTBsrqEniXXEScS6sWOgLqnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/m37gUQPPB__XUvGhKh3zfA1GylZhpd2G-JzOOvo1cfxRje_5UpVtRHAQJlljGk6tpRc25hqg6ZIrO5KF5-9SLITxXKCKfSK9LqMCcSQIJnuJCiFIr9mXGWbjhEfoMdLQ2DnFHaF5ytL1jRoYlwmgiCC8s-_e-wi8nWLY0v2ousl4O6lJEquFOo62ywwXD-OS5k3mowi3ViYz-GtJ9n7QOZBaHIDu3ehweaDaaDckBweYZqR_bANrOBgMmtSSrTxFcGM9OdACg66NnVLHu3zzvw1TMLdCdBvNPYvhE3n1SMhKEoctwAbIfJ4kL8B0ZzfAzx4ZZg0CMQLQnyfnMYrxYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DhJCAIV1RclOAJREVNsMd9IeMsmznknkVZ49vusTprm-QKzGYS0f0M0sR_S00J1o5XgpASioXsEY_Gh2k91cP4_qma9sixFLIYZXg2_4b3m52P6TP4MqvthVo_GONRoavytNtgudF6Y6AWskad9n2rZAGLxIWBQFecQlVYShFA8tJKnsDVtm0vyxX9ViAy-CtpN_e-ffa-1kEWe0nfFjJbqBIdbNfTZ_ryW5xXz2Zf9XM9IekJKvDVn5DCGsvJVA6OF2Id_7hjE9mptN8ogrBl8itnrnsgjM-9GeolDZcjQv2MtaMlojWKa9_cE0zY0eUHN9fx4E93l_oSYQokHn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nlhnfwfQ80x2g-jwkH-GAI5rV9FV3V-7dbhctgslkM3HGdq8xb6eqU-plkoK359rqc3zv5N8JY_jBAjZF_lBr5gXCDtiRO14Fo-pz2N_AOaDGOtlShGMYDNDI3vKVCLXYSoPVnsb8hdW_P33Jlvjt6VEdHuVWjtze_HnZBxXaiV_MM6oJmqHbu-WvOAqBqKAHu4Z7CL8WfF9dDr5HnZ1BaIqTUiyJgH2PmuFXIeTkzjDBVH4YmpPmv2rtdzxfLiUEjlPF3XHHmMZeuW3-ecSKEgWA0-H6mfGjlZlK-CX-VwkJKIpeI5s6K9NpoSDVa9_X2ORk3bI8AqkN_pyPLs7uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 318K · <a href="https://t.me/VahidOnline/75843" target="_blank">📅 19:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75842">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1l0DRcW8RYsfiMlg1gLyMUQV_edfZP5VsDLaBdH4cWOQ0-DKap1Yj4musUh7xH_s2ViA89TWNO2HwJgyBD0c8jobTy8K6k5pC3CSTr9OkkFVQ5_VlHUrR2D-9dtieHTJIcjaGm7ZXpdKmsW1fYkCGUFx1L-iKHnpZn7D55G-SQ_G_0ecRroo2kIORMM7SYTAnbQ5JU1BQBj0Y96PY6yZTn-S_Hf87CCRkialomnhjzzGLKrMYSJALJmYphBK5EJLaTmUOiUKuyxrZOLT-QfuC4EB5mzRiTMpvwvtvYk2Ep_nyq_j1pPz4GCyTH1CEyRN3zAKG503estykb70K8nJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های ایران از کشته شدن یک دانشجوی زن در دانشکده دندانپزشکی قزوین به ضرب گلوله خبر داده‌اند.
میزان، خبرگزاری قوه قضائیه، از قول دادستان قزوین نوشت: «بررسی‌های اولیه نشان می‌دهد این دو دانشجو که در آستانه فارغ‌التحصیلی قرار داشتند، در مرحله متارکه از یک رابطه عاطفی بوده و پیش از این نیز اختلافات خانوادگی شدیدی با یکدیگر داشتند. صبح امروز، مرد جوان با یک قبضه سلاح کلت جنگی وارد محوطه درمانگاه شده و چهار گلوله به ناحیه سینه دانشجوی دختر شلیک کرده است. شدت جراحات وارده به‌حدی بوده که متأسفانه وی در همان محل جان خود را از دست می‌دهد.
در اطلاعیه دانشگاه علوم پزشکی قزوین در این باره آمده است: «انگیزه این واقعه، مسایل شخصی و خانوادگی بوده و ارتباطی با فرآیندهای اداری یا محیط آموزشی دانشکده ندارد.»
به گفته حمیدرضا قافله باشی، رئیس دانشگاه علوم پزشکی قزوین، «این تیراندازی به دلیل خصومت‌ خانوادگی اتفاق افتاده و دو دانشجو که زن و شوهر بودند در اثر شلیک جان خود را از دست داده‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/75842" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75841">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 431K · <a href="https://t.me/VahidOnline/75841" target="_blank">📅 09:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75840">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 409K · <a href="https://t.me/VahidOnline/75840" target="_blank">📅 09:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75839">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZHwRUSd_CXMu4p54R7SG6JjbkdQZHCyCIX5B41IleMhJLYueB_Zy2xpmvHl9YaOyqgFal0Op1_M2931H_wBWXB5cQa8OoA3WcUIkBXsjdgGGvFDPIAmDwXtCvoNsj4fckH1HtcyFA9KytXUQ-dqx0qrJhx7guhKXmgLBqTIx0SuQ2l6qt_fJsbvk2vouMTumwp2UWO-z5tMvtB4mbaVykAXfJB6B-OM2nfvsUyXWN1X4WMZ8ngckyOk_yfmDTr1QFyFVKbE62TKe9Gugn5ykMC5y0Wmwz0J_sEcPEZBix-rT2bP2F3V4VBXMmTtMbBJiEpgBGqB-pUwDdo0tBNOBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود.
اما آیا دموکرات‌های کودن و بعضی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند وقتی سیاسی‌کارها مدام و با شدتی بی‌سابقه غر می‌زنند که باید سریع‌تر حرکت کنم، یا کندتر، یا جنگ کنم، یا جنگ نکنم، یا هر چیز دیگری، کار درست و مذاکره برای من خیلی سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور است!
رئیس‌جمهور، دی‌جی‌تی
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 401K · <a href="https://t.me/VahidOnline/75839" target="_blank">📅 08:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75838">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های دریافتی:
امیدیه خوزستان صدای انفجار شنیده میشه
از امیدیه خوزستان پیام میدم
طرفای ساعت ۸:۱۳ دقیقه صدای ترکیدن اومد
ساعت ۸:۳۱ دوباره زدن
همین چند دقیقه پیش صدای انفجار واضح ای اومد
امیدیه هستم و صدای دوتا انفجار شدید ساعت 8:33 اومدش.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 365K · <a href="https://t.me/VahidOnline/75838" target="_blank">📅 08:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75836">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">قوه قضائیه جمهوری اسلامی اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد [گیشا]»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» اعدام کرده است.
نام این دو معترض که بامداد دوشنبه یازدهم خرداد اعدام شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
میزان نوشته این دو «از عوامل اصلی آتش‌زدن مسجد جعفری در محله کوی نصر تهران [بودند] که اقدام به تخریب و آتش‌زدن مسجد، تخریب اموال عمومی، درگیری با مأموران حافظان امنیت، انسداد خیابان‌ها و ممانعت از عبور و مرور مردم کرده بودند.»
دستگاه قضایی جمهوری اسلامی در ماه‌های اخیر به شکل تقریباً روزانه اقدام به اجرای احکام اعدام معترضان و یا افرادی می‌کند که آن‌ها را به همکاری با آمریکا و اسرائیل متهم می‌کند. برخی نهادهای حقوق‌بشری می‌گویند جمهوری اسلامی از اعدام برای ایجاد فضای ترس و به‌عنوان عامل سرکوب استفاده می‌کند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/75836" target="_blank">📅 08:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75834">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aRataeBDGPy3fQMCOqZJ0IG6HN5wfkbuCyz5ejg6DfQH7waiTLx4oXit3VzpqNEJ0Z8epYNVmm2irrElrttRNhrUjkFrs5dXlvZ21q80uZkl2TIZR2_2UDWqUKypbbv5cdnFgQ7p_Wykgy4dzaGHI677z9ORn_lxQQF-WrJh0FeHu8OIEqaqvnnbwBR3ffWMbqdKgSeobHJeEDFoBfy_0qRCpbkflF_rdAtr0RBt5iUIvWkmYKH7Xe4Eb9UpivJ1N-HPx34znWqqtuljjEMlFZIxU5mPD6_LB_iosbyjh_BzUaJscIh0M8N708-N-ViO9MbaRSOnTVvSZll3Wt_0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J4qf9D_Uk67CV50BfDkxVtMdx3A--AScxF_eh6VECTtSEqmHN6GVHoUVdmz_O7dTmaiGjXZKJDyBVFm5kciqndf73ZaFCLeNP7RxjJS6f1kwpKZp1io_ZVX_0QD3cgp-OR95Nq30iPc5h8mgtt-9fc6bHzEzWMRcsVTMFN_w4Iw2B-bEpim9FBWubC4I5s1UAeOyMfs8XQO4ye98a9O8Eulerp35qTz6LItWmCoeaddp_DeJF4A0KVrsE1017dHJm3uvdy1ixIXlEsZ2W6VbD10lqaaZzETv_efyJkXy0uqZWwhYXpLuYCHd4SP1VwUxJ_CmA_RKkLRsq1Kgq-7vgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 356K · <a href="https://t.me/VahidOnline/75834" target="_blank">📅 07:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75833">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=Ss3Kemh36g34e1cV1GmYIEvMX1o9mloRXvk6jl2VkDey5G96PdYRgh8sP89YXcKmKj_c3Exj1m9GTF6PN9MO5-XX7Cfk3Mc1rJtTCpDuvk1jA7f4IPgPwgbuT28pp_L5y3qoXFDnl25g1Us1Pnrq1uWkPCmsrmuXle9nfUSUTIuwfg8mssVHtjC_QxVu-aPRYKeOT4-T6T3plzKJ37_rOms-sWLnalDAzY76YM7Wf1ko6qRLxSGpux5hVn6KsVKEcwezrMjHfkz8unaj6ixmcNjHFZzIhNiopp81mlOqQLGARhXp_s2dpyM3IzQZl9gTzUpCWi0f4Co3dF7383Uwlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a89b39dc76.mp4?token=Ss3Kemh36g34e1cV1GmYIEvMX1o9mloRXvk6jl2VkDey5G96PdYRgh8sP89YXcKmKj_c3Exj1m9GTF6PN9MO5-XX7Cfk3Mc1rJtTCpDuvk1jA7f4IPgPwgbuT28pp_L5y3qoXFDnl25g1Us1Pnrq1uWkPCmsrmuXle9nfUSUTIuwfg8mssVHtjC_QxVu-aPRYKeOT4-T6T3plzKJ37_rOms-sWLnalDAzY76YM7Wf1ko6qRLxSGpux5hVn6KsVKEcwezrMjHfkz8unaj6ixmcNjHFZzIhNiopp81mlOqQLGARhXp_s2dpyM3IzQZl9gTzUpCWi0f4Co3dF7383Uwlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 326K · <a href="https://t.me/VahidOnline/75833" target="_blank">📅 07:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75832">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YXlC0Ngfllr4XbWdFsLFW7M4HiZCz8XWNK74xKUMC-ESAbtVYrx3-R-aLXqdPETrYVa-EYysWr9JpbaSRZDfWbbE46xbtjSyICHIiqaTYWDpG53BkIphcoJ1V5bMZdMhEi_R_QjHHJzWOp_tRHi7pTljUNFqiLkTlgCxkurgJf781FjyfnD57smiOi3lysr0JgGvGL9nnf349F2LHhscl5-aBgX5BypFNH6WjsF98HmvTssaKBfMubwNY6c8deOyDAgkGA2HB8GgvkjJ0QCD-fviXWCdaKkWwB2gJH2a7gQKmBPQICNnNUWWmT8hSdhVE-04fBuDFeTOL6-3zEg9fQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/75832" target="_blank">📅 06:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75828">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HwHOqRN8G-3IraUPA2oCgAYAkegruQhVwIORSJMt-xzDGH1E-2bg4LHq-qjcXds0IyWIjRQfHEy65UqarY8jtPlpJzxS_6ydcVpOW0zKP_rCTq0GzTPIeNvwHQY-S5IGNbjWDemsSxLmjlWdvCeFebl57iuUEZ3UcryyOynblIO_Az1WIxU8E4SB08I3ZrECiBGatkfbIkLcSJT4ZggmiiLZ3chw3YqhYx248vCvpors6EFtgxo_udsTNqrHCSV4EXo37o99IPU99WG0ipiK3zw-WA7Q6YqOBQXms4zhPS4P1173frXN80Qd2xqfM4AE4SGHszyILUKsBnHg0YUUAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sXILDRmX0NxWo2u6bB49AsSGXi2lGDuYT-bLB1zwRVEN0Jq5JGS0dBw14C-NMk88tmXYyxun4bbbdfgNcI9bNGgFmHruiKvPt_hbBqZBTqkYVTYvfLtTszs5K8wIYeCvd6Sm5BS_rjD-oWRjoOIhAm0QoF7N-lUpXgmHevxby4HYxgn-pjgrzTYOONgeXE4fjUaGMbool8HU4onBLGpqqzHS5S_Ti0n9aRw1uBBoCOLm2ONedfPTKB-FCIar6S1kOhyYnAWwzfzf4JDa4Q3rClX2wBkvpJXYReOYUgBlvHWAUkCo0LtO0-UStCRRW2DhxymQ18wRF0bWwo2iDpvUOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/arIgYu2klw9l-l1x__gUl_iEn41ocoFv1TO_J-xf6GzP9yHT0CTkdifJu8R0IRaQUHTFcHcxc9l5SXS2gDNgElgZDMF6WlaUdENHjnDzUB9BN7TuJsist3pbbFfPQQxQlrQhd8pMLOU72MYLnjMhizdNpsU8x5Uw-o8tQmE2l0hdU9hl_MH-IDatJJ3dVvdqM_YN5O_rr-xVdGLpTnS0kOmdk7CrbNy4v7lnqj-HU7Wr1v4ebS3S-hz7RV5j__RWxXZDMWosGcJe1qlDRXyUkjPE97n8UU4JAuSX30_s_FVXwoocqArnfPpicyroUwtj9GbSFV9VJqx6Ta9jn96HPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=B99Az9uuoN-t2A13AhJuI1-txJ7k8mvLn-fU01_w0z_-g5fleATP7UKui2w0cWp5cz5mYHz4KAS2Y4_9k1ifOXZl9v3UQzHogzF9tQcErWqgoD1SamSBkHHWhTTspp222kd5srG2hRQj7XyWKX1llpPs1aKPCy7Mdie1mK3nC0lIc_ylKQ1kXz8oNjfYd_dbMa4vAnteHiMR8D95KnBEhEh9uZK5KZVAUdunE0BYFvfoKp5zYmZh8mepmuWUX2MRpfyYwA3FhLbFJkZ2vnqPhAuKgBr77YhgxMMLk7CxKWhzD5r8KYamOJsiLGolrLsz7DnBpJUqlOidJ_2e6bhsNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1affc9bf27.mp4?token=B99Az9uuoN-t2A13AhJuI1-txJ7k8mvLn-fU01_w0z_-g5fleATP7UKui2w0cWp5cz5mYHz4KAS2Y4_9k1ifOXZl9v3UQzHogzF9tQcErWqgoD1SamSBkHHWhTTspp222kd5srG2hRQj7XyWKX1llpPs1aKPCy7Mdie1mK3nC0lIc_ylKQ1kXz8oNjfYd_dbMa4vAnteHiMR8D95KnBEhEh9uZK5KZVAUdunE0BYFvfoKp5zYmZh8mepmuWUX2MRpfyYwA3FhLbFJkZ2vnqPhAuKgBr77YhgxMMLk7CxKWhzD5r8KYamOJsiLGolrLsz7DnBpJUqlOidJ_2e6bhsNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">'شلیک موشک از
#امیدیه
در خوزستان'
تصاویر دریافتی، دوشنبه ۱۱ خرداد ساعت ۶:۳۰ به وقت
#ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/75828" target="_blank">📅 06:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75827">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhA21-v9Y1afCDhr74kVIPkgvCuMs5no6wwVRH426KJzTLPNbs4yxnxY2cU8ceyghTuSgyqs-P4yvvVkLgAat-M12GYbBLtJC9hYsYqTy3_t_lSgrYqGmafs_keIWbqmEWxVah2xQDLCBm32Pj3dFEK7tq6bithl5bLB1Po4P9GrEvciIsh9t3mDpdVylBUt-QNdywYfomgAF1pH421L0Wu9lejP71xApEua4cIH3k9MG-g8wFlpimk_fhKeI2GV0Do1RceJRpJZTRDz0EKQgphrxq5zRXQCVyY9-jSFeApcL_K6WkDmWIo-XJ-VLc8KJ7LURxgSG1KMiA4stwqTLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به کویت
دوباره همز‌مان پیام‌هایی درباره شلیک موشک از امیدیه خوزستان و اعلام هشدار در کویت دریافت کردم.
دوشنبه ۱۱ خرداد
ساعت ۶ به وقت کویت که میشه ساعت ۶:۳۰ به وقت ایران
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 345K · <a href="https://t.me/VahidOnline/75827" target="_blank">📅 06:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uun3e38MEzC8nZVjA-dCl_gVpne9PmdpfEzMuB85E4zMKb1H0hmnDGOUahXJtArSnIuN-Arw9lV6UCNGD5omf36bEWiz9Cumyr58gb-iiBaKGriGylgNOCAkwDCZHQaIxoV2qccSe5m6RWo6pJDJJzUkliCr16XgBILeDx4Nzu0JPGfFIKVGR0eFAh77JhNRGXAZt8N3ZOCt0a3ab4TwuVm9EeXu_wJ5MzqNmnigeeku9WrQu3hbCD6N_0O6q5OWGVMZPequcW7HymXuxH1zAtp2zH9DOnYLxgooiknYiWVZ3VygBS42FHWcSVenDLd_sLr99IiCNXuJN4Fidiokmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 359K · <a href="https://t.me/VahidOnline/75826" target="_blank">📅 03:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/goSSL2ZBhhQo_O2Q9t1dzhQWI8uZ6M-ntPo3j9BzHr3pubTlpXXym4_CiRx9btxS0t8bdW91mRgYkAaIzD51PzxfFmHAnvlIpx6eHLyp8G23OffrG6Gejg_QYTYR3yztLlIzXVrsjP8WzRc4mRzilMDjP4hOAk3tZQGCYBN1L7r7sDKJGKGq-8pXF_3eG53iU9bsetnCR9MPLPAOT6rq8kWF7sTvJkH3JFdDX6gb0WEJWrc3RKlSfd3voUOvEhH8kWuzSBE6FrdRFD5YYxO_zZ9fwNn7uisaXFSqWdUPhNa1nHnXyG-kk6u9Qst9Lkp2cqGxJulN3wcHR8xch0JPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز هم به درخواست استعفای پزشکیان پرداخته:
FoxNews
چند مقام دولتی با تکذیب شایعه استعفای مسعود پزشکیان، آن را «خبر کذب با هدف ایجاد ناامیدی» خواندند.
فاطمه مهاجرانی، سخنگوی دولت، الیاس حضرتی و علی احمدنیا که از اعضای شورای اطلاع رسانی دولت مسعود پزشکیان هستند در پست‌های جداگانه به ادامه کار رئیس جمهوری و تلاش او برای «حل مسائل کشور» اشاره کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/75825" target="_blank">📅 00:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pgdhfBBuxez8EILrAwBMVd-0bxq1pWq-1sSO99JiblCLSZxmlbgzpL0YCLJpEp3bkYdNHsJCpIL_vdPp8cQ2m2eSTexQeH9YFru94MRXQLyQOHdL46la0p7qJh-nog5MtgAC4kx5NhpMMFadNpJPF4-diAH3b7BKI8RrPCYMFz6btMR2jymyji6gT4J4_YBhSGNx3zFKetahGSibdCc52pVju5WEveSgfp6mPhgSDAe38RXZu-UpoVuHUXNxv_glxInsNRcvIwIlznkLI8bpNMOWXf03PXRXLzwybhqtR8N8WunVDny1pRWnjUTcXRBLKgFBA806lgwSLjSh8ZcYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های جمهوری اسلامی وقوع دو انفجار را که تقریبا هم‌زمان در تهران و کرمانشاه و در ساعات پایانی یکشنبه گزارش شد به نشت گاز نسبت دادند.
سایت تسنیم، نزدیک به سپاه پاسداران اعلام کرد که در ساعات پایانی روز یکشنبه، «انفجار گاز» در محله باغ ابریشم کرمانشاه باعث مصدومیت ۲ نفر شد.
این سایت‌ همچنین [با انتشار عکس بالا] مدعی شد که انفجار در یک واحد مسکونی در «فاز یک اندیشه» در استان تهران ناشی از «نشت گاز» بوده است.
خبرگزاری ایسنا به نقل از سخنگوی اورژانس استان تهران می‌گوید این انفجار تاکنون ۶ مصدوم بر جای گذاشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 420K · <a href="https://t.me/VahidOnline/75824" target="_blank">📅 23:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=ZiXQZHfPsQKm-92eEWmI2EqXPgAzKOyeY9v9lRcrc7n2RV6XecOwFhsSOJ83LP_plre35Iggx3kq7NLVlKSDEEraewsx8z_lfpZMB00JJnJpqmDfg9xyp3_71d9D3l1gKePnperai3SiK2FU1ceFkCnIqnplIxxnwhUBdFGMZjxWg3ByIWyouw2cZ6NBxjKU5tWzK6QLTPv0ivzfi4_Ec8bC-0uFqZ-R7B8etFY4mtGwgPrrUCOjX5I6UZFalqu2gmMcRCb4hPSntdDBOD2dvE2DBpnn7A9VK-pPyTEdusZtFhrszqmcEOlxOYQqwKXctPWyzq9pISfJL50apKdrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c3fc33b86.mp4?token=ZiXQZHfPsQKm-92eEWmI2EqXPgAzKOyeY9v9lRcrc7n2RV6XecOwFhsSOJ83LP_plre35Iggx3kq7NLVlKSDEEraewsx8z_lfpZMB00JJnJpqmDfg9xyp3_71d9D3l1gKePnperai3SiK2FU1ceFkCnIqnplIxxnwhUBdFGMZjxWg3ByIWyouw2cZ6NBxjKU5tWzK6QLTPv0ivzfi4_Ec8bC-0uFqZ-R7B8etFY4mtGwgPrrUCOjX5I6UZFalqu2gmMcRCb4hPSntdDBOD2dvE2DBpnn7A9VK-pPyTEdusZtFhrszqmcEOlxOYQqwKXctPWyzq9pISfJL50apKdrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری تسنیم، وابسته به سپاه پاسداران انقلاب اسلامی، در واکنش به گزارش شبکه ایران اینترنشنال درباره استعفای مسعود پزشکیان، رییس دولت، این خبر را تکذیب کرد و آن را «شایعه‌سازی» خواند.
شبکه ایران اینترنشنال، ساعاتی پیش در گزارشی اعلام کرد مسعود پزشکیان در نامه‌ای رسمی به دفتر مجتبی خامنه‌ای، رهبر جمهوری اسلامی، خواستار کناره‌گیری از سمت خود شده است. این رسانه همچنین نوشت در این نامه به وجود اختلافات ساختاری در اداره کشور و نقش نهادهای نظامی در تصمیم‌گیری‌های کلان اشاره شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 434K · <a href="https://t.me/VahidOnline/75823" target="_blank">📅 21:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UCoOvGujhev_FMylIpiNgZKC9Onh0TvZksr5whGuL-OLDdyrZZwpUXry8_7sXxjRpE_bbvsFY0Q1FmgFUtUe7QnXuYMqGZrq3ni8aF4urIJq9FXU_51MZDtbH2b644MRYcpjmzaO4-r5c7tsfQ9qrTRP_cgbqmvG619y8_Sqp5CV22zJ-4C8vmnT3EZjx1F3_yxnULocWql5-Hmnlt10381QbX-gV8PVbfvSA83UuoQ6fYk3goOUiAAUKDM2ETT1gn7QDGnXCVtQMkgCWACioPI_nBWYnkB0qo3qopc6Gm2Zc_gEn6Rw5T4FGwWACqjl9Bkv98D0ZtI3Dw7ARYShEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">IranIntlbrk
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 435K · <a href="https://t.me/VahidOnline/75822" target="_blank">📅 20:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9A-bcNoi3j8tFCc-kBoRHHM8ZFYIIVUeKIXAMqr7rkr2R33skwmEVP287MHAgRIVSvDXbTqwro3yuNaXLw7xzDIqSv37LqwMHrwoHcGiZwIQXUbUkjN4TlsB3NZJsvgPE3xqrzYZJwa6Uh6ImgFOODTeVkevxs0whadVLOyfjpNWWdCcoLANxW_ybSsaVEtprS3ygexR34W-wwxACA_k9qGS9PpfJcZbraeCNYuiM56rUX_diUgOkYmaucsy20p-ZZCZhGVFWS_L0r9pTeR6YtSadx7Odzaw-lYNEtgPyLW2kd8fZEOzpSa8aa_jQ48ius-CK_qpnhaRbsiR0duEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پیاهو، مردی که تصویر معترض نشسته مقابل نیروهای پلیس یگان ویژه در مقابل پاساژ علاالدین در آغاز اعتراضات دی ماه سال گذشته را منتشر کرد،
به گفته وکیلش
به ۱۰ سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 428K · <a href="https://t.me/VahidOnline/75821" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6220710705.mp4?token=U9MrQ84cJf8k_Mp8tEcgqLygjiiQzrkoSC4lG2hnQp1SUSDxq8TuHt6F5gW_grK0XC04dx0DQW7BsrSl-CD_ryFtZCLv8_MS7QhAd9nVuUUqVkvT2r3bxBRDU9hdXIeUeAuqqf_3pkNBcsPcuBDfmgn5i3pWfE4eCmdUpt6FyTzSIWj6d9wJlbVCsSH9liSC3kCA2bkqeZMU5XRx6WlyozVJY1JNDeoRq9VzWWrz4HQglISSiKe-uzSioJkm4kqQ88ZTkmslnv5gtDk66V22oliiIcr1D1eXpzf38uASaELQsprhvMN_ZJ0LOP-1A-UgOil18R3U8lQMeKMmm3Jt3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6220710705.mp4?token=U9MrQ84cJf8k_Mp8tEcgqLygjiiQzrkoSC4lG2hnQp1SUSDxq8TuHt6F5gW_grK0XC04dx0DQW7BsrSl-CD_ryFtZCLv8_MS7QhAd9nVuUUqVkvT2r3bxBRDU9hdXIeUeAuqqf_3pkNBcsPcuBDfmgn5i3pWfE4eCmdUpt6FyTzSIWj6d9wJlbVCsSH9liSC3kCA2bkqeZMU5XRx6WlyozVJY1JNDeoRq9VzWWrz4HQglISSiKe-uzSioJkm4kqQ88ZTkmslnv5gtDk66V22oliiIcr1D1eXpzf38uASaELQsprhvMN_ZJ0LOP-1A-UgOil18R3U8lQMeKMmm3Jt3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با فاکس‌نیوز درباره ایران اعلام کرد: لایه اول و دوم حکومت آن‌ها از بین رفته و اکنون با لایه سوم روبه‌رو هستیم. شاید آن‌ها دیده‌اند برای بقیه چه اتفاقی افتاد و می‌بینند ترامپ آماده انجام چه اقداماتی است.
بسنت افزود: اگر ترامپ با این توافق موافقت کند، همین حالا به رهبران جمهوری اسلامی می‌گویم که او این توافق را هم از نظر نظامی و هم از نظر اقتصادی اجرا خواهد کرد. آزادی کشتیرانی در خلیج فارس از طریق تنگه هرمز باید به وضعیت پیشین بازگردد.
او درباره اینکه آیا ترامپ «کار را تمام خواهد کرد» گفت: اگر «تمام کردن کار» یعنی اطمینان از باز بودن تنگه هرمز، در اختیار گرفتن اورانیوم با غنای بالا و نداشتن سلاح هسته‌ای از سوی جمهوری اسلامی، پس کار تمام شده است.
بسنت تاکید کرد: چه از طریق مداخله نظامی، چه محاصره یا فشار اقتصادی، این نخستین بار در ۴۷ سال گذشته است که ایرانی‌ها درباره نداشتن سلاح هسته‌ای گفت‌وگو می‌کنند. این موضوع پیش‌تر ممنوعه بود و اکنون برای نخستین بار روی میز مذاکره قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/75820" target="_blank">📅 19:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفرهمند عليپور Farahmand Alipour</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=lfjIE7t6q1bafCMuRfWJvBpbh5uqy0HKw7l4ulUYJqA6R5sBVUnqbrjjp84E_a41jZ3hnpjM9A4XCV_cZrN-Lxw48XOW5vAL2vj6ku6oyCU-5W5kK0k3MpjchYvKyb_6Dco0ufdOTJoVwYQ4_RwaUBmuCP7Jn52Wl0niqtM5lnqfSpr1rgxFUEYzm279eY8oaVHpu6z-4JqdtD6o-s1pIZfhHi2NlBN9phF2UQIa3VtmlyFFhVTwcJnOIl4FeTb0sAEdWXTWAKx-Q5pAoWnatZo78dWe2YArdRWp1v2pWsKC2k4mPJtDuefoQ4B--IUDbaidQUFYWHHIOkmHkb_J7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65778ca5eb.mp4?token=lfjIE7t6q1bafCMuRfWJvBpbh5uqy0HKw7l4ulUYJqA6R5sBVUnqbrjjp84E_a41jZ3hnpjM9A4XCV_cZrN-Lxw48XOW5vAL2vj6ku6oyCU-5W5kK0k3MpjchYvKyb_6Dco0ufdOTJoVwYQ4_RwaUBmuCP7Jn52Wl0niqtM5lnqfSpr1rgxFUEYzm279eY8oaVHpu6z-4JqdtD6o-s1pIZfhHi2NlBN9phF2UQIa3VtmlyFFhVTwcJnOIl4FeTb0sAEdWXTWAKx-Q5pAoWnatZo78dWe2YArdRWp1v2pWsKC2k4mPJtDuefoQ4B--IUDbaidQUFYWHHIOkmHkb_J7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/75819" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75818">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGmxaIW5oKkWIOan2-Jy7KIt1Cl2_gszc6c9Vbfpk_yAoJ2D4uxkMiTJPYKTUmxQIHEc7N_h90DluZSr0cceaDGzYZGu2rHcBh_Yt5oHP4G_27UVY_mn-jQIV-1xMDDjXK7uR2LJQo0azOLMC_q9dx7mT_q9iXNMAuiX1BpvNo8Ga59BTZqEZFb0TDQSOYRakdkkjBKUp9uIDYf_hJXSCrN9AHzSOAoK0hme96X0xxej473S4qSI3ZhIc2vRvLC8wB76VWhlohzRIiOtOfNEVAXNzv8UgRodY_JF6FM9boccgwHAJqO7t7S0W5oxniHb8lFKeZtcem5SWOU-F_qa2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 312K · <a href="https://t.me/VahidOnline/75818" target="_blank">📅 18:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75817">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QDRSQQEiosEkG2JHgBgR_foYIZFPAu-YiTZIukY4ohmgIW9e3JZuLbVe6E7iBB9xYCwGnKN-cPrh9142jRTFXFMzKUWqvQ_mwC5J5RNcRPBGzOJtUnq8elffaY4PnkZP52VbF3EVtOEfy5OHr5HLNwxS9HBxs7RO8O8h2eVxgJEmkoX46xMOKTvQOWGObXP66LrsrhPlrz4ONlQORAex17vfCCmPJVb08erp7hnxuMYkv0Msg3a3at2R4-anSIcj_IeyAxeKYCpSwAdLYZAG84cABj3d3qZM1eTXW_fLGKwzeaEGWVhMup9BbTdmRoMQz8-8kmL3Be0cwF1yvm_dqA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 322K · <a href="https://t.me/VahidOnline/75817" target="_blank">📅 18:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-75816">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJgtZeYtKb-LFz9y8iJO9pmamLj6v2FdMyyNqJHTnrY8UYU6oMm7F07ZLQK7qEuhQEL2BGGMKCnXrSSR_0oqwjNrhHo5_pbC9v5b7-ivvgnFasYtHC4lTe5-ck9qFfvVQyUcPcsyBjrMplCD_HWFV15KQAOEr6lySeVMpuB_mHJ11M49RLNeq0G6LtbbPNCYf28vLccn_yfbldD-7nkduytLjYzfqbDXgDT0vdTQwUEJsRMUlSOJPh4ZceSak_Fcz7YKMjh3DqVnN3mCGVt2ZITNp8RvnPHOboM_xpt-Mt2a4CxLicNWgR48-lEuE7Xh2Dslgskrso6zDwyx5twxyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس مصوبه جدید شورای شهر تهران، هزینه خدمات مرتبط با خاکسپاری در بهشت‌زهرا به‌طور میانگین حدود ۴۰ درصد افزایش یافته و در برخی موارد رشد تعرفه‌ها به ۵۰ درصد رسیده است.
روزنامه دنیای اقتصاد گزارش داد نرخ خدماتی از جمله حمل متوفی، تغسیل، تکفین، تدفین و برگزاری مراسم افزایش یافته است. بر اساس این مصوبه، هزینه انتقال هر متوفی از سطح شهر تهران تا شعاع ۱۰ کیلومتری ۵۰ درصد افزایش داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/75816" target="_blank">📅 15:59 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
