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
<img src="https://cdn4.telesco.pe/file/YI0GtSt8hTVbTAqnttD0ozQm4pszOccuYQS7N5l55qH5Px_ViJ04Kn5PvRar7_yLyWxoWPM-Mm2pcaZ-dJXiicUEct6eh0D8_jzHi2NJzBs7Ss9QATfHfdbXStRwaC5XPLaOmvToElmZMI3WHPyXGxWmJtxAjiKp3XVawBmRVcRFCUbboR3akn0YKTpFH1j1VqUqUSewsPwLACHUi23iRMI-04tuxwwQdzzW3QWOzPzQyAMoSuNyyq6ufeeB8rdWFqvS2-g-U-UIJgUEyv3uZBCJQ5dqS8428KLi6UsuP5sM0rl0aAB-GFxoUmLLOoj7qsy3LyS8wWDje21pTCWDrg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 942K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 13:10:54</div>
<hr>

<div class="tg-post" id="msg-131416">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دلار هم اکنون 176,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/131416" target="_blank">📅 13:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131415">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c41d4e2cd.mp4?token=KZMj15YyejJLXn7fMOeUnP5EWMjhLVOiKlR2IiitUct7qe3KTB3Bfp0h6rX03CxUPQMibjs7-YI-0ncsxbZoOh_Hai130Qs3BFNkblU3W91UQCrRUORmOpYNB-vAXaowlZ1oR8gy50PXZApkdlsfJNit4FZBa25ETCSha-GV7-IVwRM8gGSbLiGjXEZ8st-_GmSlYD6cAWQ9hQQVPiPvPEOimhZZbClaIlZytJSscuJvPLwXUklM-Oc2jAD7m86cFQ3onafy4IfcsNRBIjJEA7yC-FVfT02VzOmF9piN-FGiaGcx-1i-bAOK5dzcZSwGGGrAVpZc-PZBXdildAZ5V1s4JtVFcXz-XwtByqI6l5CWQpG7N_XfYg288hTbiRMP233lz8Q62Cd8aBHWbor0fWc3zm-LgDXaa64iBswePGZT7wY7lZUGRCQZDEvROfzHwKqpve9VGToJ6bZHXQDlN0VIU5iCrH_yfDJSqRteVYvb34mRFlXJSI3ZNSIslaZ0lriZw5bt8JEw6HjnWQ3Uj6H4e-AJKs88PpGmcyP1B7hJ6HiMKIcuPsyz8u0o6SNhveip7G0vXIgu8IWTxyPM6chMsqIRvxVmeuJEiCVqzAC8NL5OceId9jmEqO7dXzAnyG3jhKU7kuvWTgV12hRi286D9xSEkFYeMDaRdYj4shc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c41d4e2cd.mp4?token=KZMj15YyejJLXn7fMOeUnP5EWMjhLVOiKlR2IiitUct7qe3KTB3Bfp0h6rX03CxUPQMibjs7-YI-0ncsxbZoOh_Hai130Qs3BFNkblU3W91UQCrRUORmOpYNB-vAXaowlZ1oR8gy50PXZApkdlsfJNit4FZBa25ETCSha-GV7-IVwRM8gGSbLiGjXEZ8st-_GmSlYD6cAWQ9hQQVPiPvPEOimhZZbClaIlZytJSscuJvPLwXUklM-Oc2jAD7m86cFQ3onafy4IfcsNRBIjJEA7yC-FVfT02VzOmF9piN-FGiaGcx-1i-bAOK5dzcZSwGGGrAVpZc-PZBXdildAZ5V1s4JtVFcXz-XwtByqI6l5CWQpG7N_XfYg288hTbiRMP233lz8Q62Cd8aBHWbor0fWc3zm-LgDXaa64iBswePGZT7wY7lZUGRCQZDEvROfzHwKqpve9VGToJ6bZHXQDlN0VIU5iCrH_yfDJSqRteVYvb34mRFlXJSI3ZNSIslaZ0lriZw5bt8JEw6HjnWQ3Uj6H4e-AJKs88PpGmcyP1B7hJ6HiMKIcuPsyz8u0o6SNhveip7G0vXIgu8IWTxyPM6chMsqIRvxVmeuJEiCVqzAC8NL5OceId9jmEqO7dXzAnyG3jhKU7kuvWTgV12hRi286D9xSEkFYeMDaRdYj4shc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غضنفری نماینده مجلس : یک کودتا علیه رهبر مجتبی خامنه ای در جریان هست
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/alonews/131415" target="_blank">📅 12:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131414">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
شاخص کیفی هوای اصفهان با رسیدن به عدد ۵۰۰، در وضعیت «خطرناک» قرار گرفت
🔴
برخی مناطق این کلان‌شهر، در وضعیت «بنفش» و «بسیار ناسالم» هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/131414" target="_blank">📅 12:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131413">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بلومبرگ:جمهوری اسلامی کنترل مؤثر خود بر تنگه هرمز را از دست داده است.مقام آمریکایی اعلام کرد حمایت نظامی آمریکا و کمک به احیای جریان نفت و تجارت از تنگه هرمز در هفته‌های اخیر به بیش از ۱۰ میلیون بشکه در روز افزایش یافته است.
🔴
این افزایش ایران را غافلگیر کرده، توانایی آن برای کنترل ترافیک را محدود و به حملات اخیر اطراف تنگه کمک کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/131413" target="_blank">📅 12:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131412">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نیویورک پست: تنش در روابط عربستان و آمریکا بر سر ایران و نگرانی از جنگ و تهدید منافع نفتی با احتمال بسته شدن تنگه هرمز افزایش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/131412" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131411">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kiGRzAHiWE6QRsRHRp8G9vimR2b7yOjonx8nY5anUk7oG9w3hNYBQhHxo-s1qRrBbVUW12jyt86br0-fXlPPEQTQ6_j2PItuVCvvwKoa5IxgoGxX0FxlWBlQ3PMFuKH_Z4CQojKqgw5vlCYJBQmc6zoQ0ERA6uGV-jiEnwlcJGPcSaA_4qFKPnKLcJpPhXDcyIidsRnwTzae1VSDe7NsGIacXipnNBfS-p-F6A8fIfnzzpUCMhjYG6XYgO1EFQvXf52JBluVE3je4ByQLFybnDM_OWO-6FqBdMZ5d2Nhz3TnXnTGShRlJ4uCm8dNJUF-ajJnm7s0DfBtOMbYLu_66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دکل ارتباطی در سیریک که آمریکا در جریان اتفاقات هفته پیش سه مرتبه بهش حمله کرده بود، امروز دوباره سرپا شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/131411" target="_blank">📅 12:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131410">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
رئیس مجلس ونزوئلا: در پی افزایش شمار قربانیان زلزله که تاکنون دست‌کم دو هزار و ۲۹۵ کشته و ۱۱ هزار و ۲۶۷ زخمی بر جای گذاشته است، هفت روز عزای عمومی اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/131410" target="_blank">📅 12:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131409">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
الحدث به نقل از منبع آگاه از مذاکرات دوحه: آمریکا به ایران گفته که پیشرفت در پرونده دارایی‌های مسدود شده، منوط به پایبندی کامل تهران به یادداشت تفاهم است و تغییر در وضعیت تنگه هرمز، نقض تفاهمات تلقی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/131409" target="_blank">📅 12:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131408">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
رئیس اتحادیه کشوری کسب‌وکارهای مجازی: امکان صدور مجوز فروش آنلاین مصنوعات طلا در درگاه ملی مجوزها فراهم شده است و متقاضیان طی روزهای اخیر می‌توانند درخواست خود را ثبت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/131408" target="_blank">📅 12:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131407">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم الانبیا: حضور جنگنده‌های آمریکا بر فراز تنگه هرمز امنیت منطقه را به خطر خواهد انداخت
🔴
استمرار حضور جنگنده‌های آمریکا، اعم از با سرنشین و بدون سرنشین، بر فراز تنگه هرمز، موجبات ناامنی این آبراه گردیده و امنیت منطقه را به خطر خواهد انداخت.
🔴
ایران در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن، دریغ نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/131407" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131406">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8ff9a7ef.mp4?token=tw4zY5y5ZUdjdnK04w7tpnMQKjUTDOfBq6T1Sth87MyPWbLcfFcCp7wuD4i3SK4Sva9zfvmvY4tjRHlMbFWVxUEEYawYOyWV_5m5i_v7RnFdDPPDCMzHz-LcFyNsPyWZHrfnjfJnAC_ZP1GGfs14jG3EbH_TGxZBgnp8FJVk3-QjHnls7zGEATpzqPbFR9EhU-agKn8FPbmPGnkzPogTjj6_1H0F47cVrS6DYLThl-CTacxSvaIMDm6rMOSq_51rFBLJ2dwsdNg8uU18DzXQ_tc_MOr3pi2KF9QI0OM2mymnOP45Gd1coKlJGprTGpBqQvI7XEfQvZ1Gwy9G2SeoYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8ff9a7ef.mp4?token=tw4zY5y5ZUdjdnK04w7tpnMQKjUTDOfBq6T1Sth87MyPWbLcfFcCp7wuD4i3SK4Sva9zfvmvY4tjRHlMbFWVxUEEYawYOyWV_5m5i_v7RnFdDPPDCMzHz-LcFyNsPyWZHrfnjfJnAC_ZP1GGfs14jG3EbH_TGxZBgnp8FJVk3-QjHnls7zGEATpzqPbFR9EhU-agKn8FPbmPGnkzPogTjj6_1H0F47cVrS6DYLThl-CTacxSvaIMDm6rMOSq_51rFBLJ2dwsdNg8uU18DzXQ_tc_MOr3pi2KF9QI0OM2mymnOP45Gd1coKlJGprTGpBqQvI7XEfQvZ1Gwy9G2SeoYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرواز F-35 های آمریکایی برفراز ورزشگاه لیوایز کالیفرنیا قبل‌ از شروع بازیشون مقابل بوسنی هرزگوین
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131406" target="_blank">📅 12:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131405">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d4fc7f4a.mp4?token=iW5JpdzvV9btOMOQ9wROvw0V1zxdZ4M5KYwq2l50zhuJy4pdbxgmB1ILxP165bRRO-_XBiR8o9SBWloBn1Ipx4tinL-U0jJcWeXrmV5xE3vPTqamgGu8RHEVZ4YGaflHnEnGJscPemjhUWRiAdSdhd0-zDxbUk7XTfD1l-Am0CFlXxczdW-RcycCCw7qj8g7Li-zc6TEK5UdlF2ANmvD1VfjZaAvRNiBSnCq3SwVgqjuXc1tEPYoh-3A6f9J4Aagb-DM6lY6-74VJrl0RMegtvjQNPIvO8vZekUiJOBqQGadoFtj2sJkGokyJu3TQNmscWqMK567sdQClYwT7BFsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d4fc7f4a.mp4?token=iW5JpdzvV9btOMOQ9wROvw0V1zxdZ4M5KYwq2l50zhuJy4pdbxgmB1ILxP165bRRO-_XBiR8o9SBWloBn1Ipx4tinL-U0jJcWeXrmV5xE3vPTqamgGu8RHEVZ4YGaflHnEnGJscPemjhUWRiAdSdhd0-zDxbUk7XTfD1l-Am0CFlXxczdW-RcycCCw7qj8g7Li-zc6TEK5UdlF2ANmvD1VfjZaAvRNiBSnCq3SwVgqjuXc1tEPYoh-3A6f9J4Aagb-DM6lY6-74VJrl0RMegtvjQNPIvO8vZekUiJOBqQGadoFtj2sJkGokyJu3TQNmscWqMK567sdQClYwT7BFsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قائم‌پناه، معاون پزشکیان: اگر قرار باشد نظر رهبری هر آنچه که می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد، دیگر مجلس و شعام معنا ندارد.
🔴
رهبر نظر می‌دهد و نظرش کارشناسی می‌ شود؛ دوباره بر میگردد یا می پذیرند یا نمی پذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/131405" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131404">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1b5f1dc8.mp4?token=A13bc789g6IzEN7QRPIZnPfE22JuaCuJWhFdvp3OdgBJRN6XSw49SYTdDJxpiwwgsyLXNFI09Whm5k4WKhvn_ZKbJAucEj9OkbY6A_YJ2JGw6jBE22vX22bY_8cmptWxfHTO-QcXWakySOi_m9RlZa6QzTJY1WZa3IJZT9pB6N8H9jF6RHql_K6DKduf00MPUNWSVvDGVaA0NdBwtk6H2Z32BfPX8SCSwOTLto4wfvSBKkBZVYBqqKtv7i1Oysrbqrd04Rv2dk3OvtjCtzqDpbUDhY1bSWFrvAS0Dv_ieQfuVAlRB7zp635AbWS8gMejklCG25Ob-m09pxhFcP0y0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1b5f1dc8.mp4?token=A13bc789g6IzEN7QRPIZnPfE22JuaCuJWhFdvp3OdgBJRN6XSw49SYTdDJxpiwwgsyLXNFI09Whm5k4WKhvn_ZKbJAucEj9OkbY6A_YJ2JGw6jBE22vX22bY_8cmptWxfHTO-QcXWakySOi_m9RlZa6QzTJY1WZa3IJZT9pB6N8H9jF6RHql_K6DKduf00MPUNWSVvDGVaA0NdBwtk6H2Z32BfPX8SCSwOTLto4wfvSBKkBZVYBqqKtv7i1Oysrbqrd04Rv2dk3OvtjCtzqDpbUDhY1bSWFrvAS0Dv_ieQfuVAlRB7zp635AbWS8gMejklCG25Ob-m09pxhFcP0y0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اتفاقی جالب در تجمعات شبانه
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/131404" target="_blank">📅 11:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131403">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
خنده لیونل مسی از بازرسی بدنی او توسط آمریکایی‌ها روی باند فرودگاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/131403" target="_blank">📅 11:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131402">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
الجزیره: حمله روسیه با موشک‌های بالستیک و پهپاد به کی‌یف و دیگر مناطق اوکراین
🔴
۱۳ نفر کشته و ۵۶ تن دیگر زخمی شدند
🔴
مسکو: تأسیسات نظامی و انرژی و فرودگاه‌های نظامی در چندین منطقه را هدف قرار دادیم
🔴
زلنسکی: پوتین مدت‌ها است که خود را برای این حمله گسترده آماده می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/131402" target="_blank">📅 11:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131401">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/143916ad31.mp4?token=lyKUcrIPdqOscxlbVKIKlOlftokXCJKIegBT2eWPJcF7HpC3MZ5LhuGdz12WdgteuusBuA1T4-a_tbxS4uuT9dtlUMO09bLFZBZsmjWyvrhgVn9FlXN90fYdi-K5Kwse6UCGplPP6QrOKElUF2WvQbcvbZY4Roh_SDuVp0bIyK1yo6msMPyqT94qzoNKiaUELtVO6-BwfPUJVQnW9DfSBJnK0J5scdapd4wGDbhiZ9ohhBDYS2WJ6Fw0dU0LMQxOehXEDqLUldeONvlsUOzAwq5GsUAIF3wEj74efYCAiM_XnMofhKekiobU3DlHzOowrVCwoxdMqFSF7VpNiRrwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/143916ad31.mp4?token=lyKUcrIPdqOscxlbVKIKlOlftokXCJKIegBT2eWPJcF7HpC3MZ5LhuGdz12WdgteuusBuA1T4-a_tbxS4uuT9dtlUMO09bLFZBZsmjWyvrhgVn9FlXN90fYdi-K5Kwse6UCGplPP6QrOKElUF2WvQbcvbZY4Roh_SDuVp0bIyK1yo6msMPyqT94qzoNKiaUELtVO6-BwfPUJVQnW9DfSBJnK0J5scdapd4wGDbhiZ9ohhBDYS2WJ6Fw0dU0LMQxOehXEDqLUldeONvlsUOzAwq5GsUAIF3wEj74efYCAiM_XnMofhKekiobU3DlHzOowrVCwoxdMqFSF7VpNiRrwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روضه یک مداح نریمانی برای جنوب لبنان: ۱۱هزار خونه صاف شده؛ آقایان چرا نمیزنید زیر میز مذاکره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131401" target="_blank">📅 11:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131400">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-c7PyPd_IZLx_wqIwytSWyac9l-8EP-hMsX-FalBRaN9Ype-pUzy4RttMH5pDjF69JatDB8z0O1hpfbca1zHWIObAb1-zuWijaow58qnlIjOpdb7gTHtCggbMbltUSDm04wEtiYrxs3nDuNcJHrWlizizO_ItLMIs-6099R6GYUTWCefXXFP-xXsbqi-v2HcqGAvJwPckBdTc6ktudi_7kA7QXkwAyqmDu9xhF4CtyJUl28zaMfbjTP6mlIpXHGVht7ScNed2otNMwohDYNKMA77CfLX0_DWCBUrHnG2H9QC1ErFv_yq_adXZENnbfR3iX87UDKBiXlw2XqeBA6Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبور تتر از ۱۷۷ هزار تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131400" target="_blank">📅 11:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131399">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0_r7IsEl2iHHDBF7ESFa04gUBOZQQ2bUr9pE4sizZ2gw4KwRccLGipHl5lNNPbsjLZc0C9znGByU1Hf2wJD5W-GvwHVY38py-9ElzRbb1V0ucoOedhjJE_je6YfwVGFZwn0DQB24MWvVv5KBc4BMsfw2slkkESSNdsC0KWsKa7BzFdtZ31wpXcXA3nloZxGcKQ5lFFX4VBIHrhF1724o6F0Oys9WEXrQbdwsnbot8Lo_wu4Zq66Fbb0uT4IA2U7zqQyG1ArijGtkG7iM-O350womt_Tg-g4ZjMQLlgrkQDhcb2_R639gWb3ybhLxC6tgVwR0c3C7OSGEExd-ilTGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت
🔴
وزارت امور خارجه پاکستان اعلام کرد ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
🔴
طبق اعلام اسلام‌آباد، زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر سابق ایران تعیین خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/131399" target="_blank">📅 11:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131398">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQSScnDmzD0U9Bl3O7YyobI9QN9JxlyI5Gko82JgMyGzEPtpgbgDDyckaMIvY6FcjrnO-DvLCOhDwr84DNLbXY_gcNLAjuR-IoLGmketm9LLDbgf5otY0uHPDatEUQ0Akb3Dfd3aMMoleCdSpmnrStmbDX4sNOutSu8_QoRemLmlShBRTPNKRpA1BzVaPaLklaMkiCioPy8zmoMT2NWvwMJofNvX_okLJHgyFXpu60oHBXE2b9dY_zQcJy6f6OFJdFR1ReHFlak-T22jOQMFVb8C5RxxFlfNmwdYqK7jYACwhOnMBTptCe-LTWr6MKsEaeCSbINwKglewB0pEVJzDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تیتر عجیب ایسنا درباره مذاکرات دیروز در قطر
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/131398" target="_blank">📅 11:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131397">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ایران و مصر رکورددار شد
🔴
طبق اعلام فیفا دیدار ایران و مصر، پربیننده‌ترین مسابقه جام جهانی با ۱۰۷.۴ میلیون بیننده بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131397" target="_blank">📅 11:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131396">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
منبعی بلندپایه به العربیه: توافق شده است که امکان استفاده از بخشی از دارایی‌های مسدودشده ایران فراهم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/131396" target="_blank">📅 11:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131395">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / توی تجمعات شبانه، برای کشتن ترامپ و نتانیاهو، صد کیلو جایزه تعیین شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131395" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131394">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
عراقچی : هر تهدیدی علیه مردم یا رهبری ایران، با یه پاسخ فوری و خیلی قوی روبه‌رو می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/alonews/131394" target="_blank">📅 10:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131393">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سقوط قیمت نفت برنت به کانال ۷۰ دلار
🔴
بعد از افزایش عبور از تنگه هرمز، قیمت هر بشکه نفت WTI به ۶۷ و هر بشکه نفت برنت نیز به ۷۰ دلار کاهش پیدا کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131393" target="_blank">📅 10:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131392">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: مذاکرات آمریکا و ایران پس از تشییع جنازه رهبر سابق ایران ادامه خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131392" target="_blank">📅 10:29 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131391">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce007c4843.mp4?token=URR9fD-KCCilgeHEhP0yA5V9J41hJSc5M9seCYJ5V5tyOnN4V-6CcJueqz6GcV7t9yhyh9BjFagrT5iL8NUPVkXvQER5Vp5fudpCMXwTmZsNAa50l82QiefR0A56LGQijjgB7PmxYI79ZfV5EMLS8sRxRbtOg2lhvsT8JxSR6q60CpuvOIcqM3Gt6HFtGl0zWwjy2w7a2snfFb9XgwuzLai6rIw9XCV8VHCWfx-BXeddv9_qm6ZypUW2ekO-hjv0YD8g_IYWx-bawhTgR3YvzU20S8AsIu-_t436XA1cqX7ir3rupX_9rHOfREZEBCW5BxQPe-6uT2FTs6Nje4mNqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce007c4843.mp4?token=URR9fD-KCCilgeHEhP0yA5V9J41hJSc5M9seCYJ5V5tyOnN4V-6CcJueqz6GcV7t9yhyh9BjFagrT5iL8NUPVkXvQER5Vp5fudpCMXwTmZsNAa50l82QiefR0A56LGQijjgB7PmxYI79ZfV5EMLS8sRxRbtOg2lhvsT8JxSR6q60CpuvOIcqM3Gt6HFtGl0zWwjy2w7a2snfFb9XgwuzLai6rIw9XCV8VHCWfx-BXeddv9_qm6ZypUW2ekO-hjv0YD8g_IYWx-bawhTgR3YvzU20S8AsIu-_t436XA1cqX7ir3rupX_9rHOfREZEBCW5BxQPe-6uT2FTs6Nje4mNqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه پیشین آمریکا: نباید انتظار داشته باشیم که ایران به شرایط تفاهم‌نامه پایبند باشد، زیرا جمهوری اسلامی هرگز به وعده‌های خود عمل نمی‌کند. آنها فکر می‌کنند اهرم فشاری برای مقابله با ایالات متحده دارند؛ بر عهده ماست که خلاف آن را ثابت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/alonews/131391" target="_blank">📅 10:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131390">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
کی‌یف ایندپندنت: حداقل ۱۱ کشته و ده‌ها زخمی، پس از حمله روسیه  به کیف . روسیه یکی از بزرگ‌ترین حملات ترکیبی موشکی و پهپادی خود را در طول شب به کی‌یف و دیگر شهرهای اوکراین انجام داد.
🔴
این حمله به ساختمان‌های مسکونی، یک هتل در مرکز کی‌یف و زیرساخت‌های غیرنظامی آسیب رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131390" target="_blank">📅 10:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131389">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رئیس سازمان وظیفه عمومی فراجا: مشمولان دارای سه فرزند و بیشتر تا پایان سال ۱۴۰۷ فرصت دارند از معافیت سربازی بهره‌مند شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131389" target="_blank">📅 09:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131388">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آمریکا: در پی فرود اضطراری یک فروند بالگرد «ام اچ-۶۰ اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه تن دیگر زخمی شدند
🔴
تحقیقات درباره چگونگی وقوع این اتفاق ادامه دارد
🔴
هیچ دلیلی در دست نیست که نشان دهد این حادثه، ناشی از اقدام خصمانه بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131388" target="_blank">📅 09:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131387">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
واژگونی قایق گردشگری در پاکستان با ۷ کشته و یک مفقودی
🔴
پلیس پاکستان اعلام کرد که روز گذشته (چهارشنبه)، پس از واژگونی یک قایق گردشگری در ایالت «خیبر پختونخوا» در این کشور، هفت نفر جان باختند و یک نفر دیگر نیز مفقود شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131387" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131386">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
بلومبرگ: عبور نفت از تنگه هرمز، ۱۰ میلیون بشکه را رد کرد
🔴
یک مقام آمریکایی شامگاه چهارشنبه مدعی شد که حمل و نقل روزانه نفت از طریق تنگه هرمز، از ۱۰ میلیون بشکه فراتر رفته و ۵ میلیون بشکه نفت دیگر هم از طریق مسیرهای جایگزین منتقل می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/131386" target="_blank">📅 09:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131385">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
انتقام روسیه از حملات کی‌یف
🔴
روسیا الیوم با اشاره به حملات روسیه به اوکراین اعلام کرد: حملات شبانه روسیه به کی‌یف یکی از شدیدترین عملیات‌های اخیر مسکو بوده و در واکنش به حملات کی‌یف علیه زیرساخت‌های غیرنظامی روسیه صورت گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/131385" target="_blank">📅 09:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131384">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
سایت The War Zone با استناد به گزارش‌های محلی اعلام کرده است که هر شش بمب‌افکن استراتژیک B-52H Stratofortress حاضر در پایگاه RAF Fairford در بریتانیا، پایگاه را ترک کرده‌اند و احتمالاً به ایالات متحده بازگشته‌اند.
🔴
دوازده بمب‌افکن استراتژیک B-1B Lancer همچنان در پایگاه باقی مانده‌اند که این تعداد نسبت به هجده بمب‌افکن استراتژیک قبلی کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131384" target="_blank">📅 09:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131383">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KeVTa6l2K-TQxLZtxVZIf33FV-lQEpeY1wmaIt9fUsTIWQnmz2sI4vUJIvIcGjPr-_8gL3uKJ3iqsL6gIjUdM-tPVGj_nlJ7L2fxBrH7ZcZZ3VSg7mFaZNWh7bFd8pHrsFqAHD92TJrc7muTvGRawDHHfQ3RVk4NBlg5k4z3RVu9jqD2JiGWxvKjSuCMzEzATlY-QEsVU4DwlJIR_UFJUSahuJ_tZfSwwWBNJngUfvU4wypB6gVavXVDWhBePVUAW7JfYfPmSeSeaHeEmq1Ezk7xD8Yc6ExJ_IFmNCrFLNzQtB9poLhBMWOtAByTIcGp2GYZ6IIdIiMXXCxVgp2GcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی خطاب به قالیباف: هوچی‌گری هم حدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131383" target="_blank">📅 09:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سی‌ان‌بی‌سی: ایران از زمان لغو محاصره دریایی توسط آمریکا در ۲ هفته پیش، بیش از ۴۰ میلیون بشکه نفت خام صادر کرده است.
🔴
‌تهران اکنون نفت را با ۲۰ درصد حق بیمه می‌فروشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131382" target="_blank">📅 09:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131380">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3197e89311.mp4?token=Cnw15RSRjUP8AIAX7sGlTmOKq-Elv59sPa0KG_Tj2PfnTE-TBDQ8L8miku2WxlRNyd_DRXK1SKAydIYJTqfyVhi4Wawk9qPVL9CDEjX1SsboY9Pj416zmH07_JrbYW9F87CpeXxdhVOoLxyfjAKJmZihnFPspNfYIYvPeH0Ppcsdvuk-LT5Ai2eb8oqCkqPwAuRg0hBa2fPTOIh7oN6zeBQ0Wg0nubQwMI6mHNfxmpsKyB-jZD1jURbMnM89d9OoxczN0LhXpy0TAPVJ0k2d6q134-qWWuwBeTZlE5FuxpA1dUm-Dy2YdaemlGON75ZPrtT0nfjBiiZ1v1sG0X77Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3197e89311.mp4?token=Cnw15RSRjUP8AIAX7sGlTmOKq-Elv59sPa0KG_Tj2PfnTE-TBDQ8L8miku2WxlRNyd_DRXK1SKAydIYJTqfyVhi4Wawk9qPVL9CDEjX1SsboY9Pj416zmH07_JrbYW9F87CpeXxdhVOoLxyfjAKJmZihnFPspNfYIYvPeH0Ppcsdvuk-LT5Ai2eb8oqCkqPwAuRg0hBa2fPTOIh7oN6zeBQ0Wg0nubQwMI6mHNfxmpsKyB-jZD1jURbMnM89d9OoxczN0LhXpy0TAPVJ0k2d6q134-qWWuwBeTZlE5FuxpA1dUm-Dy2YdaemlGON75ZPrtT0nfjBiiZ1v1sG0X77Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراینی‌ها پیش از حمله گسترده موشکی و پهپادی ترکیبی روسیه، در متروی زیرزمینی کی‌یف پناه گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/131380" target="_blank">📅 08:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131379">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رسانه‌های محلی فلسطین گزارش دادند : قایق‌های جنگی اسرائیل به سوی سواحل «خان‌یونس» در جنوب نوار غزه تیراندازی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/131379" target="_blank">📅 08:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیویورک‌تایمز به نقل از دستیاران نخست‌وزیر عراق مدعی شد: ایالات متحده انتقال دلار به عراق را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/131378" target="_blank">📅 08:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سازمان امنیت دولتی یمن در سازمان ملل: حوثی‌ها با حمایت ایران بیش از ۱۸۰ حمله به کشتی‌ها انجام داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/131377" target="_blank">📅 08:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lObHzGpiZY8s-Do_SUFGeU1EgjHPIsrobJrqrYxUvizIoKIyZlkXfDWsoXvhyhmacW6BFxaApbsuKsM7z-HFL0iOKoVf9LGF5JowJ4KIJDATQTUPbzFWX5KrxOj-_0xExavg4YUd3GLagjaNyT1-nskwAkDPPD716J2kZHBWJIhiIboNQlARX0n0Iw1bPeSoBFo9vCOrZq6O9nbvJut2l3JWA_QL5BHDq0K19gIKmOGBTdA5n2_NBFYl2GEbwDVTVbNIz4Zv0SL02chlpclQ6CaJIubAVjabSlFt3jg8awidMdKEPLXveutPkJ57w912C4ylVoMkVLvY5bpKUQv01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی: تنگه هرمز زیر فرمان ایران تعریف می‌شود نه سنتکام
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/131376" target="_blank">📅 08:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
الجزیره: ایران پس از مذاکرات دوحه، کانال ارتباطی برای نظارت بر تفاهم‌نامه با آمریکا ایجاد می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/131375" target="_blank">📅 08:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131374">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
یک منبع ارشد به العربیه: به ایران اجازه داده خواهد شد تا محصولات کشاورزی آمریکایی را با بخشی از پول‌های مسدود شده‌اش خریداری کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/131374" target="_blank">📅 08:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131373">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
بخشایش اردستانی،نماینده مجلس: تجمعات شبانه باید فورا جمع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/131373" target="_blank">📅 02:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131372">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_ZbgHv2lHsMpyX3vlm5JpROd0m9EVg7Gs1weVg6Ion3yv25rhU75HVE8PCZeafK2rGN9PbzJHoB2OyWrcXS_9z6tgUn6v4myI1Hja7eQfAxr4tL3ucIimW7RdkfcDEG50ME9Oop2ljnhj4E-Vjk3NdxsHEuYu7PhrCR6eF5AQiwJ0xzSLpKSt6GYnd9Uiv4JYJYJ6WjZ0MUaTZAhMJ0IA-eZD64W9J4LstRy14VTiYb96Pev-WyoXBXjAMtY25q_7hKtKucs0CKODBXfLmahXZoYNES1APDQfhHhKjOBxciuclpLcPOVd5_lzh4HSmLRgAutIbOVEeGE2A4tRF9fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش ایالات متحده آمریکا اعلام کرد که در پی فرود اضطراری یک فروند بالگرد از نوع «ام اچ-60 اس سی هاوک» در دریای عرب، یک نظامی آمریکایی مفقود شده و سه نظامی دیگر خدمه این بالگرد نیز زخمی شده اند که وضعیت جسمانی آن ها پایدار گزارش شده است.
خبرگزاری «رویترز» به نقل از ارتش آمریکا همچنین تاکید کرد که هیچ دلیلی در دست نیست که نشان دهد این حادثه ناشی از اقدام خصمانه بوده است.
در بیانیه ناوگان پنجم نیروی دریایی آمریکا آمده است: «شناورهای نیروی دریایی هم اکنون در حال انجام عملیات جست وجو در منطقه برای یافتن یکی دیگر از اعضای خدمه پروازی هستند که همچنان مفقود است. همچنین تحقیقات درباره چگونگی وقوع این حادثه ادامه دارد.»
در این بیانیه همچنین آمده است که این بالگرد در منطقه بر روی ناو هواپیمابر «یواس اس جورج اچ. دبلیو. بوش» مستقر و به مأموریت اعزام شده بود.
فرود اضطراری بالگردها روی آب می تواند حتی برای خلبانان با تجربه نیز بسیار خطرناک باشد؛ زیرا بالگردهایی که بخش فوقانی آن ها سنگین تر است، هنگام برخورد با آب معمولاً به واژگون شدن متمایل می شوند و ممکن است به حالت وارونه در آب قرار گیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/131372" target="_blank">📅 02:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131371">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
حادثه امنیتی در ناو هواپیمابر جورج اچ دبلیو بوش در نزدیکی ایران و دریای عرب.
🔴
نیروهای نیروی دریایی آمریکا در جستجوی یک عضو خدمه مفقود شده از هلیکوپتری هستند که از ناو هواپیمابر جورج بوش برخاسته و در دریای عرب به صورت اضطراری فرود آمده است.
🔴
سه نفر از چهار عضو خدمه هلیکوپتر با موفقیت نجات یافته‌اند و در عرشه ناو هواپیمابر در حال بهبودی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131371" target="_blank">📅 02:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131370">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzSsbHmXGVBdL-OuwLdzyCiWCLGXVKnVjUWNGg_pflJktJMXS88y1YEU93ShR_nSdVS_GRBOcGn5sY8YvPky5gZy34VTtqvtJiscr55TQJpHBuY1cQvTO9nVRzCttuYyeLbzyumJlBFI0LfUCWiNMmhwOcHiVX1OifAZWdUwCMdXi8s-jbpWoyKBq95kjXG44zBnMHB80lPNRcSXHX3pXd0JSyuykiyUujmdhfDdP-YvvExQ2kflver3JaLgiFa7fN8oxwLDsW-3UNDnv2_DApA7JrU6OKQbeivVYA-GwCDTEtZZjUdlKB-OrsSIO9Lk9Kz6Pcc8LeGhBCwZRGv63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: برای مراسم‌ تشییع، همه مردم بیان
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/131370" target="_blank">📅 02:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131369">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromm.m</strong></div>
<div class="tg-text">کشور ایران از بیخ فاسده
میترسن یکیو برکنار کنن اونیکیارو لو بده
پس نتیجه میگیرن داخل ی سفره بشینن و بدزدنو بخورن
فوتبال هم اینطور شده</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/131369" target="_blank">📅 01:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131368">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
وزیر ورزش عربستان سعودی پس از حذف تیم ملی این کشور از جام جهانی، رئیس فدراسیون و چند مدیر ورزشی این کشور را عزل کرد، همچنین سرمربی تیم هم اخراج شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/131368" target="_blank">📅 01:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131367">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: مرکز فرماندهی منتسب به سپاه پاسداران در لبنان توسط ارتش اسرائیل (IDF) تصرف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/131367" target="_blank">📅 01:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131366">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbuJ6P6Qz9A0rSC4YAugnorBL2aKfW4akEz1B0BIbOJ9VS-fvMbnfhZh0zYA9PiiWakWlUDM3gtmpOCqN_dHd0bhoFS48fmZDb1Gh03Cl49x2btrfZ0jfavFlb3araqpwVnOsoEKMIMhR_WWWUqD4ub_Ax7P0LQwwyrSMry7940OPjEf_E5OnUAoBQCilvTr3RVDvx6skg1Kv4rDzkZTy1-R5_53ztd7dczXZdHgd-XS6YE8Vw-7MZjhDgEiX0-0gw9moyGKxxFugcM4NPst4FvMhWuxCf6dgJrR6-aDYU6LulvYPYNswCs9IWy8XgdMmwU8Wz8yl7MmO_4QNshNVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به تاج و اعضای فدراسیون که رفتن به جام جهانی مجموعا بیش از 50میلیارد تومان حق ماموریت داده شده
🔴
فک کن بری جام جهانی و بهترین هتل مفت بخوری و تیمت هم برینه و ۵۰میلیارد هم بگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/131366" target="_blank">📅 01:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131365">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/131365" target="_blank">📅 01:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131364">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Il8Az0nSsXyAE-QrZ6Xw6Obilu2mO9QRVGqbFPWmycB6T9JJEMalCWulI-c94PFg8xx5plPthHkjMhtWheKBrrEZxVdZqpcAeWf5KBNRT3f1tRySrZKcYDtfYODNb_k0hgHNVm-yxP2HyJo-VhsBbgqXjSCGGAw9MEOCoeVOmho7EzWyVK0DPq4WN44Pz1MXk1m_jcBbNdT5aQxkqkg0aDS3CZOdQ1jec-AqMUAfRkhmLJJqW6nuYvL-V4afV-EbtxnLpRULdrvDTnbVWsjKLrg2fUhsEJF0iSEfjz_HpK6wcM3V6YS_4OedBedelagry4UIbIFCbuVwXw0ylErPqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تاچ: پیگیر هستیم تا به افتخار آفرینان تیم ملی خودرو یا ویلا به عنوان پاداش داده بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/131364" target="_blank">📅 01:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131363">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🎙
فردوسی پور:
نکنه پس‌فردا صبح با سوییس بازی داریم ما خبر نداریم اینا خبر دارن که مراسم استقبال گذاشتن!
@AloSport</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131363" target="_blank">📅 01:22 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131362">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3740efe365.mp4?token=QA-4ArkTyivfDjQoioRcpjkSd5BB7f4lUVZUDwNM4MkdOATp37tgLbmjC33M0fuuZRXOrMrVTjK6lbT2sa2G8N2rKDbGO16hY0B1IaaqvWxfT9jSdGqPvPSxmuywRBS4ZSanH1HV9B9rpLJ2vBp7GbAODn0DFKqbMIzRFZ9cFYNakFlVVptGfh1LqlaR4WDm9ewljXxyt9UQPsOeRCjWt7xy_gr0_cG8FTmQwou_bSNlq3UKz6zX5g--bGaOByOlE2ftYfFjFxhCbztVcQY7pL5dWZDqfdFXhcwsLqcCtGgGvwPKB4puIV5-uOQIAHdA9a8srUF8It2VLpJTtY0FoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3740efe365.mp4?token=QA-4ArkTyivfDjQoioRcpjkSd5BB7f4lUVZUDwNM4MkdOATp37tgLbmjC33M0fuuZRXOrMrVTjK6lbT2sa2G8N2rKDbGO16hY0B1IaaqvWxfT9jSdGqPvPSxmuywRBS4ZSanH1HV9B9rpLJ2vBp7GbAODn0DFKqbMIzRFZ9cFYNakFlVVptGfh1LqlaR4WDm9ewljXxyt9UQPsOeRCjWt7xy_gr0_cG8FTmQwou_bSNlq3UKz6zX5g--bGaOByOlE2ftYfFjFxhCbztVcQY7pL5dWZDqfdFXhcwsLqcCtGgGvwPKB4puIV5-uOQIAHdA9a8srUF8It2VLpJTtY0FoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری صداوسیما جوری داره از قلعه‌نویی تعریف میکنه که خود قلعه‌ هم تعجب کرده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/131362" target="_blank">📅 01:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131361">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=sjdOGFYygPTdqgNIeCvoZUlaBfFj8cpQldwIqhetd-uSbPuccSXkE8c1SOEwAT_D4HLHw21h95pRO_jOYh2Zd7KnY27xDDtFfZ1ourZfgtL1qUBRGSyEA8kH-Z4ssW1Eua8JAafXlSFDKMVT__9z-iliQNm_6734MgPyYkJrqUFul8uUiZu-xXwK4EQAbLFxJvV6lYLSARI_gy71xO0UlKcAHCb-XdUuaOSAB5mUfyJWCPjfve6J2BVRA7jusSEk5yJ6qNCQnC2tv2Uawkycx_k-INm26ZySp-VcVcVwVBo0hiI5y3_YtbmbC-W768U38qC94C9ZBO_mKV9S5HahFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=sjdOGFYygPTdqgNIeCvoZUlaBfFj8cpQldwIqhetd-uSbPuccSXkE8c1SOEwAT_D4HLHw21h95pRO_jOYh2Zd7KnY27xDDtFfZ1ourZfgtL1qUBRGSyEA8kH-Z4ssW1Eua8JAafXlSFDKMVT__9z-iliQNm_6734MgPyYkJrqUFul8uUiZu-xXwK4EQAbLFxJvV6lYLSARI_gy71xO0UlKcAHCb-XdUuaOSAB5mUfyJWCPjfve6J2BVRA7jusSEk5yJ6qNCQnC2tv2Uawkycx_k-INm26ZySp-VcVcVwVBo0hiI5y3_YtbmbC-W768U38qC94C9ZBO_mKV9S5HahFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
@AloSport</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/131361" target="_blank">📅 01:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131360">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLjsyMHsXi00sW6WNi36AbN8gKhvktrcLQV81gCnA0c7DIFvyzbuChlIJzArcelqUrcrT8O5C7JR35Ly5ZAKzMqCV_v1WGYRkq_uXCEVyqZouXnHk8q2eM-BlBbKGLLhfvHXeAxlyB_mHagqyjQZWi3_T3dmKDcedOemAsa_dTpyTMUdsex5JSM5NVqEI7CN__p3YlI9Fs0O5jAELbsoZc8pPbR1Y0zu0436RMlxlzzN85DWdO5FhIdELVb8Jf5Cw-ECGLBxUJ0n_q3cgC2jm1A61ipKh2wGHMWlN8wBtWOIpzKoy508385LL2jkafE8MgZ9RB4yj0bF-EQT_jvbIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع رسانه‌ای گزارش دادند: مقر احزاب تجزیه‌طلب در منطقة «ديكلة» واقع در شمال عراق هدف دو حمله پهپادی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/131360" target="_blank">📅 00:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131359">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی به سمت اقلیم کردستان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/131359" target="_blank">📅 00:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ:  در مورد کوبا، پس از دهه‌ها و دهه‌ها، به سمت ما می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/131358" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/386c345efc.mp4?token=mi9fNEtJ-2bYay-SpLfUUwvhSx90fDZEMnXShQfsTuE-U5WkHIlWlt4IpEZ2vrRb1ctiFryW_xbOGHYwyLAmjVHXr1QGwP57r85-8REyWppNjE21J0rac8pY3YWwtQEBloEplUOrgjVN4xtmk9Bm-8BxcyjjyxthulQ8l1W3dW1fyOUwiMH3cenJLzOL47UhBLyVuunH07i1UmBrIYQW47yYpoegNEXdGpDR3h4jFg8Lknx9K4SzPTFZZd-Hb9dph5ECx0V4mxXaUw392yGMZBlfrlfVLl_qBkt0hDWd7wI-2NZOCa4T6IyEjgTqKrbF0dJqqq4KUUZaSzZYv0s9rgf_iASfgxfpXnrIl9PgYv0W8fYc4NXBViiqxfxVmO0vF-a9WirRSsWiTLys_gwsIlnOCZIQpKWRzuMsUT2hbDm8HHBIHPkB_m6SD24ejcdv2web_p3jMN4_V--fszkvRsjXv-CIyQnV0TmI86H9v2eJn4hz-1cHSLK4ims_56POUu4N-63fAdpIdtSACcBxno99QkmpLUBRlsIRZL-yWfU8291Q8egWJnKldeYwRYfyPPOuRhxcjx7xXkIc3jCmHTB4GfK2nfhWiVVRoeVmwJC7DeGtFyPOBpjN26q4z7I1aIRX35gpSpaqclq32lPfO1SI2el0nsNVbPQ_aKKJTgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/386c345efc.mp4?token=mi9fNEtJ-2bYay-SpLfUUwvhSx90fDZEMnXShQfsTuE-U5WkHIlWlt4IpEZ2vrRb1ctiFryW_xbOGHYwyLAmjVHXr1QGwP57r85-8REyWppNjE21J0rac8pY3YWwtQEBloEplUOrgjVN4xtmk9Bm-8BxcyjjyxthulQ8l1W3dW1fyOUwiMH3cenJLzOL47UhBLyVuunH07i1UmBrIYQW47yYpoegNEXdGpDR3h4jFg8Lknx9K4SzPTFZZd-Hb9dph5ECx0V4mxXaUw392yGMZBlfrlfVLl_qBkt0hDWd7wI-2NZOCa4T6IyEjgTqKrbF0dJqqq4KUUZaSzZYv0s9rgf_iASfgxfpXnrIl9PgYv0W8fYc4NXBViiqxfxVmO0vF-a9WirRSsWiTLys_gwsIlnOCZIQpKWRzuMsUT2hbDm8HHBIHPkB_m6SD24ejcdv2web_p3jMN4_V--fszkvRsjXv-CIyQnV0TmI86H9v2eJn4hz-1cHSLK4ims_56POUu4N-63fAdpIdtSACcBxno99QkmpLUBRlsIRZL-yWfU8291Q8egWJnKldeYwRYfyPPOuRhxcjx7xXkIc3jCmHTB4GfK2nfhWiVVRoeVmwJC7DeGtFyPOBpjN26q4z7I1aIRX35gpSpaqclq32lPfO1SI2el0nsNVbPQ_aKKJTgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره مدال افتخار
:
من پسران زیبایم را می‌بینم. فکر می‌کنم می‌خواهم یکی را به خودم و یکی را به آن‌ها بدهم و یک سه‌نفره خواهیم داشت.
🔴
من به آن‌ها مدال افتخار کنگره را برای چیزی می‌دهم... برای نبوغ آن‌ها در شکار.
🔴
و من یکی را برای پذیرش «روسیه روسیه روسیه» یا چیزی شبیه به آن دریافت خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/131357" target="_blank">📅 00:19 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ: کشتی‌ها با تعداد بی‌سابقه‌ای که تا به حال کسی ندیده است از تنگه هرمز خارج می‌شوند، ما در حال ثبت آمارهای بی‌سابقه هستیم و قیمت نفت در حال کاهش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/131356" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=n8sg-MLRy1pTJFTv8NelyyOvHf1TLTeFTI0p5Eog8t-JKd-vb0mUCtP0nveJebYz6pPNvGzEPr16Lx2_kzHT2rsdX7CvSrinV5k_El31INT9VzhhGinO7YV4pxvuxN6YJXI1Zg-z_4hcety9qDWfSlEFmIsP8QI3m6ciJJ-azzhlvTyuC_snuoGCcI1EnTunJDpLyk8o9r4_EuD54qL3DlpsujlmsQ5UuLbw3P34-yu-wBb54QBr-sxDgqj6wCTjEEvbvqh9_hoGth7yHu23_u9Or4ATH3nfw363GzfBZiZFQM94dDMnHx0YhnnAeV6_TLaVfVHSrpK3q1_CAhkZi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ce1f21322.mp4?token=n8sg-MLRy1pTJFTv8NelyyOvHf1TLTeFTI0p5Eog8t-JKd-vb0mUCtP0nveJebYz6pPNvGzEPr16Lx2_kzHT2rsdX7CvSrinV5k_El31INT9VzhhGinO7YV4pxvuxN6YJXI1Zg-z_4hcety9qDWfSlEFmIsP8QI3m6ciJJ-azzhlvTyuC_snuoGCcI1EnTunJDpLyk8o9r4_EuD54qL3DlpsujlmsQ5UuLbw3P34-yu-wBb54QBr-sxDgqj6wCTjEEvbvqh9_hoGth7yHu23_u9Or4ATH3nfw363GzfBZiZFQM94dDMnHx0YhnnAeV6_TLaVfVHSrpK3q1_CAhkZi4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : کنترل کامل. ما کنترل کامل همه چیز را داریم.
🔴
این فقط آغاز دوران طلایی آمریکا است.
🔴
بهترین‌ها هنوز در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/131355" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=ZtbzlRBiShOYqk2cFeKfdgkl2_dpmm6I2t6CO0CXDCloIp966LAFz55b2rCg4zeJVZmlY--uSYi4AkY0g3UQmBP6U4mg54bd5r0a6X1JZZZWlCJaDCzptNc6vbRyuNU6HEz88EBNNjkdSyTgIFQGLrDb0xfv10ngv5NZJa3Ohs91oE5duuiD-S_kStqR0F0_g_RaQ3SiREWNnO_aXLkPyWtlNNEGSz-jjuZvG5HZVyCJO6ADKFjhi0NPaz7_pyPjpCL5G1XSQTP485jKF7pwnzVpyIuWrVVCDspNUY4zVcuwFSOK-GLim5EFuugnP2FgFcCRjW6hgZB0HTQtqmdi0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a937d249f5.mp4?token=ZtbzlRBiShOYqk2cFeKfdgkl2_dpmm6I2t6CO0CXDCloIp966LAFz55b2rCg4zeJVZmlY--uSYi4AkY0g3UQmBP6U4mg54bd5r0a6X1JZZZWlCJaDCzptNc6vbRyuNU6HEz88EBNNjkdSyTgIFQGLrDb0xfv10ngv5NZJa3Ohs91oE5duuiD-S_kStqR0F0_g_RaQ3SiREWNnO_aXLkPyWtlNNEGSz-jjuZvG5HZVyCJO6ADKFjhi0NPaz7_pyPjpCL5G1XSQTP485jKF7pwnzVpyIuWrVVCDspNUY4zVcuwFSOK-GLim5EFuugnP2FgFcCRjW6hgZB0HTQtqmdi0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما بزرگ‌ترین زیردریایی‌های جهان را می‌سازیم.
🔴
ما در زمینه زیردریایی‌ها و دیگر موارد ۱۵ سال جلوتر هستیم
🔴
ما دوباره با کشتی‌ها شروع خواهیم کرد. قبلاً روزی یک کشتی می‌ساختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/131354" target="_blank">📅 00:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
اکسیوس: آمریکا تلاش دارد ایران را از دریافت عوارض از تنگه هرمز منصرف کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/131353" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=fn9OpLVPtPHqiWWsVNOsPP1OJ9yd_w4TGB0S2lw-xj9Dg9i4oX-YXpT8MLmvSfzgv2fSXv-IpqoCJcFUj5vJu2QqiTLAxg6iaaAY5LlHLCDVH3p2P6JXj5Yh2N2p68YOWWdBQM56tjbfZ0S6VfCSCCulQ5TZZoWL1ojkU3NFtRnRrV4GinyBi-b-X86H7vb0AjzPfESSM8BEnhQigwO9Izn-bKK5wyRXPdXqaIo6MJfUKpaF-RiY-xTw3REXacy35vY0j4h2FldU0gGniuHiBOWCq2TCtjwqXaYCAqlSUrlAykYDS4vf5E2OggJjVNOCAoY0uTAfd0Ynx5tVu3C_dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66ae0f5149.mp4?token=fn9OpLVPtPHqiWWsVNOsPP1OJ9yd_w4TGB0S2lw-xj9Dg9i4oX-YXpT8MLmvSfzgv2fSXv-IpqoCJcFUj5vJu2QqiTLAxg6iaaAY5LlHLCDVH3p2P6JXj5Yh2N2p68YOWWdBQM56tjbfZ0S6VfCSCCulQ5TZZoWL1ojkU3NFtRnRrV4GinyBi-b-X86H7vb0AjzPfESSM8BEnhQigwO9Izn-bKK5wyRXPdXqaIo6MJfUKpaF-RiY-xTw3REXacy35vY0j4h2FldU0gGniuHiBOWCq2TCtjwqXaYCAqlSUrlAykYDS4vf5E2OggJjVNOCAoY0uTAfd0Ynx5tVu3C_dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: اسپانیایی‌ها — اعضای ناتو اما نه اعضای خیلی خوبی از ناتو.
🔴
آن‌ها به خوبی رفتار نمی‌کنند، اما یاد خواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/131352" target="_blank">📅 23:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
جی دی ونس: در حال حاضر، مذاکرات به خوبی پیش می‌رود
🔴
کسانی که به دولت به‌خاطر مذاکره حمله می‌کنند، همان افرادی هستند که ما را تشویق می‌کردند چند بمب دیگر هم روی جاهایی مثل افغانستان بیندازیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131351" target="_blank">📅 23:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ
:
عربستان سعودی و دیگران در حال نگاه کردن به چین و سایر کشورها برای محافظت از آن‌ها در طول دوره مدیریت بایدن بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/131350" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=Vlesie7pJCvh2c9A0XxPbCLXVA4sh9-JAjBVjKzR5FSHAGnipFNEtOzU1s4gawzhO45sXRolPpKoSSKCzbqSxAZdBFaOlhnp2Zz2KjDkWl5CIskaRG852W-cm51KRgyW2rAxGCCpvcqVz4LX_bPxOhb8o1jqb7_Jk-b61EoalRxubMXEp6vBzIi3vLl6LnnXbkKzwmcGq0PO3EdtxGggzNKO3UI0i6eZC8SpZ7Dm67lGwQwjkUdTgv0p-wwo9BXzDM-63oSWRFdWEAiKOiFtg-zN-KAeKWw0613lkTzvZ0zXUaVo8fxRaivx5_-fEOrwzL_U30KP88tCxd87uk9X8nSyTE5djgsEV-nLXDBgw2vapVyQqVT4Zs4o2y7pAldtad27RyR05rZzGRtMQMMPkyXCVr5FgN1ESwVFML7MGeTFQKD1HpC3wnccoaN_nVKoLryUXxH3gGHOGCVbgVX1fj6D-gTNdbxKvRCFUUPLnadUfFwVe0co1HBMYn1Pdcox3yGUgX9iUVUdrukUCRlt9Y6A0xePERlRIotGOKa5Ng-CfA8U-mRAy_JVbV7DR-s7HgwXkcuBCe6t9fa22LKX5ZO6zc9V9z9iYHCOA-FS9yMuj-1DniGxBtsPxP1oLra8AJW6onVVIqkF2m9-vw6NngT89GqcLSeqG2dnVtt8UG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cca332fee.mp4?token=Vlesie7pJCvh2c9A0XxPbCLXVA4sh9-JAjBVjKzR5FSHAGnipFNEtOzU1s4gawzhO45sXRolPpKoSSKCzbqSxAZdBFaOlhnp2Zz2KjDkWl5CIskaRG852W-cm51KRgyW2rAxGCCpvcqVz4LX_bPxOhb8o1jqb7_Jk-b61EoalRxubMXEp6vBzIi3vLl6LnnXbkKzwmcGq0PO3EdtxGggzNKO3UI0i6eZC8SpZ7Dm67lGwQwjkUdTgv0p-wwo9BXzDM-63oSWRFdWEAiKOiFtg-zN-KAeKWw0613lkTzvZ0zXUaVo8fxRaivx5_-fEOrwzL_U30KP88tCxd87uk9X8nSyTE5djgsEV-nLXDBgw2vapVyQqVT4Zs4o2y7pAldtad27RyR05rZzGRtMQMMPkyXCVr5FgN1ESwVFML7MGeTFQKD1HpC3wnccoaN_nVKoLryUXxH3gGHOGCVbgVX1fj6D-gTNdbxKvRCFUUPLnadUfFwVe0co1HBMYn1Pdcox3yGUgX9iUVUdrukUCRlt9Y6A0xePERlRIotGOKa5Ng-CfA8U-mRAy_JVbV7DR-s7HgwXkcuBCe6t9fa22LKX5ZO6zc9V9z9iYHCOA-FS9yMuj-1DniGxBtsPxP1oLra8AJW6onVVIqkF2m9-vw6NngT89GqcLSeqG2dnVtt8UG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما اجازه نمی‌دهیم کمونیست‌ها راهمان را ببندند.
🔴
آن مردم، کاری که انجام می‌دهند، واقعاً احمقانه است. آن‌ها واقعاً احمق هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/131349" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=GyJIyzYhw5rzacb27yE05py7ZXMuULbpw7ZLw5dRiBmlPMlhYq8liXjw27SHfGnJl2bz5fLJHjq6FBhi1_ZjHjbayL6qjw8VbCqLBAf-5s446i0_-eSDJLSpULbwhjm9oHm1STx2-tFRDW9cFOVij6INNh8qp4CebLA5BUWEqU5a-kMHVM3sG2s0RLkYstLW59QHQMdHr7pc3c95wf5VEbqtzdZFIoIXaxXcoSubfW257QRX9PiOHTSVrHoAcGymG1sjdFH6JUHnWNpKFKabmRbhIuFJ_kUXuahL3oXk5DPpwAjwK3ogtf_62-tv5sWCSIJK1-wxa_uMCoe21zNsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709087d4a8.mp4?token=GyJIyzYhw5rzacb27yE05py7ZXMuULbpw7ZLw5dRiBmlPMlhYq8liXjw27SHfGnJl2bz5fLJHjq6FBhi1_ZjHjbayL6qjw8VbCqLBAf-5s446i0_-eSDJLSpULbwhjm9oHm1STx2-tFRDW9cFOVij6INNh8qp4CebLA5BUWEqU5a-kMHVM3sG2s0RLkYstLW59QHQMdHr7pc3c95wf5VEbqtzdZFIoIXaxXcoSubfW257QRX9PiOHTSVrHoAcGymG1sjdFH6JUHnWNpKFKabmRbhIuFJ_kUXuahL3oXk5DPpwAjwK3ogtf_62-tv5sWCSIJK1-wxa_uMCoe21zNsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
در 4 جولای، دمای هوا تقریباً 107 درجه خواهد بود.
🔴
و من می روم، و یک سخنرانی واقعا طولانی دارم فقط برای اینکه نشان دهم که می توانم هر کاری انجام دهم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/131348" target="_blank">📅 23:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=T4aqwWhtpA5pM0c9YgZ9Fb8bLv0lrPCjaed4uJ3PS0JhPgOaoGQiKfHZiGPY473H0DvERAeFQXzW-1E3_C8w_mKMHjfBETtJ8eXbcqBu3Seeo_dRPnUlTm_zPaTuOedSzC1paaY87OfOXjZ-30eQJvcOeELpMnhVe4wrq9raMirG5gHPOIyQbvCyeD3xvcdrqHuqpWUptX1xrT8dOwaM-xajcA2NYS5j7XcR6HyNMSPJhAm3z7vnzJ1Nn5sBM3UX6OJeKmLzU2k4HiW5EEwI756kBp9AFb0AgB5L9PmCzJGfybaQ00MVp3dJ5H2rbzoAcabj9sET3Mk-QJMW8aKnFH-HNWahwLA3bIBjfnfHCeQPAa2qPmTgKz1VhkioUUibx_5Ln5VuAkBjUQPqxNq6fOaGWZscM-Q-kH_DVARqJn9Iphudobu0SjfiDz-4EhrNQlU6UuoTIkPO0LEAb7YN2xickOzT4igi1Wv5vD_uMSvIAlyxmGhbJpBfuUE6B8pkudra2QAdSeDtmbvGsavl5_er2GpFDJshALQHd18zU9Kobe0B7kIeDmaXtTG6zLz8d4xyxoK7Q8xBmhsgPZ5TkKjnTnOEdGRQQmB3EZEjlrcBm2BJteaXin3vDtqXoUztnI-3CXiIElbUDcQX-RiUXy4G77T_ctaiM66TgkGUklk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/600b8e0075.mp4?token=T4aqwWhtpA5pM0c9YgZ9Fb8bLv0lrPCjaed4uJ3PS0JhPgOaoGQiKfHZiGPY473H0DvERAeFQXzW-1E3_C8w_mKMHjfBETtJ8eXbcqBu3Seeo_dRPnUlTm_zPaTuOedSzC1paaY87OfOXjZ-30eQJvcOeELpMnhVe4wrq9raMirG5gHPOIyQbvCyeD3xvcdrqHuqpWUptX1xrT8dOwaM-xajcA2NYS5j7XcR6HyNMSPJhAm3z7vnzJ1Nn5sBM3UX6OJeKmLzU2k4HiW5EEwI756kBp9AFb0AgB5L9PmCzJGfybaQ00MVp3dJ5H2rbzoAcabj9sET3Mk-QJMW8aKnFH-HNWahwLA3bIBjfnfHCeQPAa2qPmTgKz1VhkioUUibx_5Ln5VuAkBjUQPqxNq6fOaGWZscM-Q-kH_DVARqJn9Iphudobu0SjfiDz-4EhrNQlU6UuoTIkPO0LEAb7YN2xickOzT4igi1Wv5vD_uMSvIAlyxmGhbJpBfuUE6B8pkudra2QAdSeDtmbvGsavl5_er2GpFDJshALQHd18zU9Kobe0B7kIeDmaXtTG6zLz8d4xyxoK7Q8xBmhsgPZ5TkKjnTnOEdGRQQmB3EZEjlrcBm2BJteaXin3vDtqXoUztnI-3CXiIElbUDcQX-RiUXy4G77T_ctaiM66TgkGUklk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: کانال پاناما گران‌ترین چیزی بود که تا به حال ساختیم و همچنین سودآورترین چیزی بود که تا به حال ساختیم. این ترکیب خوبی است.
🔴
کمی شبیه ونزوئلا. ما در واقع با جمهوری اسلامی ایران هم به همان اندازه خوب پیش می‌رویم. شاید شنیده باشید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131347" target="_blank">📅 23:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: اخبار جعلی اخیراً نسبت به من بسیار مهربان بوده‌اند.
🔴
وقتی شما همان کاری را انجام می‌دهید که ما انجام می‌دهیم، آن‌ها باید مهربان باشند، حدس می‌زنم.
🔴
من حتی با تئودور روزولت صحبت کردم.
گفت: «نظر شما درباره کانال پاناما چیست؟ آیا آن را بزرگترین دستاورد خود می‌دانید و در مورد این واقعیت که دموکرات‌ها کانال پاناما را به قیمت ۱ دلار به پاناما دادند، چه حسی دارید؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/131346" target="_blank">📅 23:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: اجازه نمی‌دهیم چین آبراه پاناما را تصاحب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/131345" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=SRJ0dDGlDeK0kKeOmUe5h3ZAhJcDMr6h9S3_QgCDBfjHiccPfkvTzKZI-srdRDIDBHy0j7F4lg1V0uikaGrrZpvhpkfpP92AqKQDyaj80DqEQdwiw8R3rSu0rmSaMLSXo1Hpamw4stg8YZNzKZAhielFiZdSS4pm__3nMSXNVzpPGJemgLC7Jc4xuheS1XJOS-24M0mKV39Vo4Uelz7X4Cq4UICLLhas_aSvIwyn44l3pXXZN2-R5gnKLoEhB34dxafjaISbrl0lUDSZGrY13fMBg0HdVr5HfWTVd8oB7WRzv2s8BkRmVdFFSiDGzUqnhkUKbNyO37KmttNr9dCiokxwzFXL9CH-tiTTtR7vDY-G1ayksKpfoamWqEFsm79QsEXxPeeuDFB_IeGC4f_f74oahOIQj8kMPsqiaW8CfeBbW4_KGgT8wehIqoTzKBLJ7Jp830LHyCqstAvRU03qaDh5ZjWqh8qFDL-BbIty98wXX0DI3HnN2w7DNFrJeGkF25R7cMDp8SEulA3mLztdzi141-MESq49ZRvaL4nl_3X6eQu885LTvLn_-ADTG7XEYxOJbnODt3LbPJ1hUNx9cBCsPzG3jsAOzOits223KeenfpGiOtxbjgMSOzjXXrHWkBBqKTOzh9MX8iktDC4-6-FcLZ7UpU1d23bF1nvuRhc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8648b6f7.mp4?token=SRJ0dDGlDeK0kKeOmUe5h3ZAhJcDMr6h9S3_QgCDBfjHiccPfkvTzKZI-srdRDIDBHy0j7F4lg1V0uikaGrrZpvhpkfpP92AqKQDyaj80DqEQdwiw8R3rSu0rmSaMLSXo1Hpamw4stg8YZNzKZAhielFiZdSS4pm__3nMSXNVzpPGJemgLC7Jc4xuheS1XJOS-24M0mKV39Vo4Uelz7X4Cq4UICLLhas_aSvIwyn44l3pXXZN2-R5gnKLoEhB34dxafjaISbrl0lUDSZGrY13fMBg0HdVr5HfWTVd8oB7WRzv2s8BkRmVdFFSiDGzUqnhkUKbNyO37KmttNr9dCiokxwzFXL9CH-tiTTtR7vDY-G1ayksKpfoamWqEFsm79QsEXxPeeuDFB_IeGC4f_f74oahOIQj8kMPsqiaW8CfeBbW4_KGgT8wehIqoTzKBLJ7Jp830LHyCqstAvRU03qaDh5ZjWqh8qFDL-BbIty98wXX0DI3HnN2w7DNFrJeGkF25R7cMDp8SEulA3mLztdzi141-MESq49ZRvaL4nl_3X6eQu885LTvLn_-ADTG7XEYxOJbnODt3LbPJ1hUNx9cBCsPzG3jsAOzOits223KeenfpGiOtxbjgMSOzjXXrHWkBBqKTOzh9MX8iktDC4-6-FcLZ7UpU1d23bF1nvuRhc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره داگ برگام، وزیر داخله:
فکر می‌کردم بسیار تأثیرگذار باشد. راستش را بخواهید، فکر می‌کردم همسرش کاترین حتی تأثیرگذارتر باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/131344" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641158562d.mp4?token=rTgQdwIfbYp1NNHI1x9pvzkEtrH_PTb0LcH2zeNfwsIkIU37cSD3LDHAkfCYeGrXwuK_D33tkLJPVR8dQXMZ83EzRTrwx3N_3vmPi_3sJzUCYOSOl5kTBRJgexNDHnvPCJdFtDi--JRP7RBHfn5Q2AKDD6YWzoay-vOd40psg_Gd1hen6Qgtb_16vFCztv4ufa69N-i2AJqIam5pd3rB4jQ-kGAOUzoFWU7YgJJuHcvuBFrSBbepwTnpqZ_eo6rKK0GqcfAva8-lL8bsAss4iUzgUQmWfU_cWOXFinEcWeve9MgRcmsTju6c4OaIgYcm-YVf7adZTj-vVQD0mEr1cYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641158562d.mp4?token=rTgQdwIfbYp1NNHI1x9pvzkEtrH_PTb0LcH2zeNfwsIkIU37cSD3LDHAkfCYeGrXwuK_D33tkLJPVR8dQXMZ83EzRTrwx3N_3vmPi_3sJzUCYOSOl5kTBRJgexNDHnvPCJdFtDi--JRP7RBHfn5Q2AKDD6YWzoay-vOd40psg_Gd1hen6Qgtb_16vFCztv4ufa69N-i2AJqIam5pd3rB4jQ-kGAOUzoFWU7YgJJuHcvuBFrSBbepwTnpqZ_eo6rKK0GqcfAva8-lL8bsAss4iUzgUQmWfU_cWOXFinEcWeve9MgRcmsTju6c4OaIgYcm-YVf7adZTj-vVQD0mEr1cYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من دو تله‌پرامپتر (دستگاه نمایش متن سخنرانی) دارم که کار نمی‌کنند، و اینجا ایستاده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/131343" target="_blank">📅 23:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
قالیباف علنا به تندروها گفت خفه بشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/131342" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید.
🔴
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/131341" target="_blank">📅 23:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Yfo6DQVRr2L_Gsn2TQdGBkm1tb9Z_RCh1xzWqE_bMwVKN8-co-gqFOcv-Esr2z-IbzMwZfouLCW8yetYXoJR3C42LQTGBObdLReO4jYWOCLH6ME5ZON_RAoqbECGwismm0jWdKniffy7iPmDaeDQwuibNgiX0oJXvtXYdhltLH8t8v5R_sJN6NegqdeAT7sAvDrJm9VV8aw-4qC8CjV-NyICp0wpCsmWeOGcSoOs4G7TmEo1fDy4mPe5tqMEYDJpAJlsjn8mZkenLBxPAQ5zjyK5rHEVN-x7WnRD0XZF224PurKHZV6Lky4Bw7r6ILFZ97tRtxRYwB4RicIWTpqFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ab4d62a.mp4?token=Yfo6DQVRr2L_Gsn2TQdGBkm1tb9Z_RCh1xzWqE_bMwVKN8-co-gqFOcv-Esr2z-IbzMwZfouLCW8yetYXoJR3C42LQTGBObdLReO4jYWOCLH6ME5ZON_RAoqbECGwismm0jWdKniffy7iPmDaeDQwuibNgiX0oJXvtXYdhltLH8t8v5R_sJN6NegqdeAT7sAvDrJm9VV8aw-4qC8CjV-NyICp0wpCsmWeOGcSoOs4G7TmEo1fDy4mPe5tqMEYDJpAJlsjn8mZkenLBxPAQ5zjyK5rHEVN-x7WnRD0XZF224PurKHZV6Lky4Bw7r6ILFZ97tRtxRYwB4RicIWTpqFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: «باید به شما بگویم این پرواز افتتاحیه‌ی هواپیمایی به نام ایر فورس وان پس از ۳۷ سال بود. این یک هواپیمای عالی است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/131340" target="_blank">📅 23:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
قالیباف: ما خودمان در مجلس قانون تصویب کردیم؛ شورای عالی امنیت ملی هم مصوبه دارد. بر اساس این قانون، به هیچ عنوان به سایت‌هایی که بمباران شده و آسیب دیده‌اند، دسترسی داده نمی‌شود. این قانون است.
🔴
ما هیچ امتیازی بیشتر از دسترسی‌هایی که شورای عالی امنیت ملی تعیین کرده، نمی‌دهیم. طبق قانون، تعیین سطح دسترسی‌ها بر عهده شورای عالی امنیت ملی است و آن هم چارچوب آن را مشخص کرده است.
🔴
در حال حاضر، آن‌ها فقط در دو مورد حق دسترسی دارند؛ یکی نیروگاه بوشهر و دیگری راکتور تهران. دسترسی‌ها فقط در همین حد بوده است و ما نسبت آن متعهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/131339" target="_blank">📅 23:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
قالیباف: ۶ میلیارد دلار ما در قطر بود و ۶ میلیارد دلار بعدی را آن‌ها تقبل کردند
🔴
می‌گویند چرا سوئیس رفتید؟ خب من رفتم آن‌جا اوفک را ونس امضا کرد تا پول‌ها آزاد شود‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/131338" target="_blank">📅 23:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
قالیباف : می‌خوام تو سفر به چین
روابط تهران و پکن رو قوی‌تر کنیم و به سطح یه شراکت راهبردی برسونیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/131337" target="_blank">📅 23:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
قالیباف: مذاکره‌ای بین ایران و آمریکا وجود نداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/131336" target="_blank">📅 23:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تا کنون رسانه های خبری گزارش داده اند رشاف در نزدیکی بنت جبیل و بیت یاحون در نزدیکی صور توسط ارتش اسرائیل مورد هدف قرار گرفته اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/131335" target="_blank">📅 22:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ترامپ از هوش مصنوعی تئودور روزولت می‌پرسد: آیا کانال پاناما را بزرگترین دستاورد خود می‌دانید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/131334" target="_blank">📅 22:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHrMp8883_1tHqohfmMLpsobNWecpUBYA_FLsXzLrkqhB7FeIKozuOWq5UI4nWhJ0D2eUJ8EQatR96jPbxzFMp7EDXJPzaprCXCRGTNlp-pYvVHNKXm6b8SqrAed_PgzVzkI3nDccsvy-hIMemlh1rRkRLRl_6ZYJ01zV8o0wcSY0RSFQ-cTEYm-a7Jciy6YXpEqriQJiP2cwMdxo9Sr1uR2OIclI6Re4eiaXKFFAXoINBtuD3_kqg7rv-xreC1ayojVx8_7xvgThjR4qpmQOZPrG4UByCLKpR-Tdl0BuNP9Nej3aEk7iQU7j-LOoeLBJsMimfpzsZIqJL3ypQeAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/131333" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131332">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نخست‌وزیر لبنان: به‌دنبال تعیین جدول زمانی برای خروج اسرائیل از لبنان هستیم
🔴
نخست‌وزیر لبنان گفت اولویت بیروت در دورهای بعدی مذاکرات، تعیین جدول زمانی برای خروج اسرائیل از لبنان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/131332" target="_blank">📅 22:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131331">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نخست وزیر ایتالیا: من ضد آمریکایی نیستم اما در مقابل ترامپ زانو نمیزنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/131331" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131330">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قالیباف: مذاکره‌ای بین ایران و آمریکا وجود نداره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/131330" target="_blank">📅 22:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131329">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❤️
دیدار رضا پهلوی با گروهی از قربانیان سازمان مجاهدین خلق، جوانانی که دوران کودکی و نوجوانی خود را در «کمپ اشرف» در عراق گذراندند.</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131329" target="_blank">📅 22:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131328">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVNgQSnWxYlLQNJnMokpryixriRhqxPl62k94kvnEulNfjM7XJNy9fwKpJm61qNrxIWJ6jH27eE1dvME9kolefaK2blrG1MBjKMilbGFbjLLNz9nX3z3aSmu6pVDGPyrfQ4rrfMGB0vZb_kdL95fytbcNw_hqpNkja_MZC8elAMedVIRBKRR2e6ezTMPoj_GrP3muskzvTJIDByiXXYTSqEq6wT970asRN8RAL_rGe9XZSSvevDjsiWMtbgll7PIcxdNMfdpIq_Vs5PH6YeqIXvChZpnP4QWeKVjHhA_yGxxifLejhdZnE-P67vB8d_eYNf1fMGhzbY5vH5MEGWT4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران اسفند ۵۷ وقتی دیدن براشون قبض آب و برق اومده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/131328" target="_blank">📅 22:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131327">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✨
یکی از با کیفیت ترین و پایدار ترین اشتراک های بازار با قیمت خیلی مناسب حتما یک بار تست کنید
➕
قبل از خرید، کانال رضایت رو ببینید خیالتون راحت باشه
🌱
@vpn_express_supp
🔄
در صورت بروز مشکل یا نارضایتی، موضوع از طریق پشتیبانی بررسی و در صورت احراز مشکل، مطابق شرایط سرویس رسیدگی خواهد شد.
🤖
خرید سریع
:
🤖
@Team_express_bot
🤖
@vpn_express_sup_bot</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/131327" target="_blank">📅 22:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131326">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚀
سرویس VPN (V2Ray) تیم اکسپرس
✅
اتصال پایدار و پرسرعت
✅
پنل اختصاصی (مشاهده حجم و تاریخ انقضا)
✅
سازگار با تمام دستگاه‌ها و اینترنت‌ها
✅
مناسب استریم، بازی و استفاده روزمره
✅
تمدید و خرید مجدد بدون تغییر کانفیگ
✅
بدون محدودیت تغییر دستگاه و IP
🛠
پشتیبانی تا پایان اشتراک
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
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/131326" target="_blank">📅 22:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131325">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پزشکیان: اگر لازم باشد نه 20 میلیون بلکه 100 میلیون بشکه نفت به نیروهای نظامی می‌دهیم، این وظیفه من است و به آن افتخار میکنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/131325" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131324">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=ldwMHoWWyY60G4vdY4ENhCtPYuUCXMU5ycI8pMTzAHftBF5B6HTbZhu2m1XOAVHWWB1kPHXrWPwziS5BacUKKA4b9RRjLL0pssuRsK1WMT59hX3tjawihTHflZdFM3BOXbV-6_vukaFflImrK7jz6j0cqWmL86ADL5eVAf38dKYRgt2itxFnGlXlCsfNENQVntz6yWrKVlkKKFyW2sBVocnKgtUr1FZqcIC8tMp7jq2AHM75FegZ5Pev6MdNvwE1sMNdgMXV9T3dorxAShcJKQ0c2puu_J-2Rmq21DJoIQp_I21ZYkKve1H8ouNkLEHCU3jOErOZk9oPz7KAsvxP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f1501b9d.mp4?token=ldwMHoWWyY60G4vdY4ENhCtPYuUCXMU5ycI8pMTzAHftBF5B6HTbZhu2m1XOAVHWWB1kPHXrWPwziS5BacUKKA4b9RRjLL0pssuRsK1WMT59hX3tjawihTHflZdFM3BOXbV-6_vukaFflImrK7jz6j0cqWmL86ADL5eVAf38dKYRgt2itxFnGlXlCsfNENQVntz6yWrKVlkKKFyW2sBVocnKgtUr1FZqcIC8tMp7jq2AHM75FegZ5Pev6MdNvwE1sMNdgMXV9T3dorxAShcJKQ0c2puu_J-2Rmq21DJoIQp_I21ZYkKve1H8ouNkLEHCU3jOErOZk9oPz7KAsvxP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خورخه رودریگز، رئیس مجلس ملی ونزوئلا، گفت که تعداد کشته‌شدگان در نتیجه زمین‌لرزه‌های هفته گذشته به ۲۲۹۵ نفر رسیده است.
🔴
او افزود که ۱۱۲۶۷ نفر زخمی شده‌اند، ۱۲۸۴۱ نفر آواره شده‌اند و ۶۴۶۱ نفر نجات یافته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/131324" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131323">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=u9K4NHVx92_2mkkzHQT0eMXwkPcoRjC_qN0t3h58KUHMtC3GPM7FWSS-hkDeWKFTVUaU7Ch9DYI54iXXL4Bbju--w4Etjt6j8sGdvq6TsFfdCVnEbZt9YcxoNzSTnmQm7aP5Z29evXjpoL_Zjg6Rq1RYH1uBbOyIyGOT264PhYXSMmmypEme9i3z3ClObGZxxfguEMGzZrDKkOD6ypD4ycM1q79UK8rNVht3aCHF6O8nQOdURBaiFO0dXpTcz2Y4jQiWs9vViWiyvEahOPp5nNRBV6s9lPH1wWDlpx4imhRo1eAG6EH_hucHvgKVL_YCV1nFdcFgLaI7II2cSZ6gkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dece196b7d.mp4?token=u9K4NHVx92_2mkkzHQT0eMXwkPcoRjC_qN0t3h58KUHMtC3GPM7FWSS-hkDeWKFTVUaU7Ch9DYI54iXXL4Bbju--w4Etjt6j8sGdvq6TsFfdCVnEbZt9YcxoNzSTnmQm7aP5Z29evXjpoL_Zjg6Rq1RYH1uBbOyIyGOT264PhYXSMmmypEme9i3z3ClObGZxxfguEMGzZrDKkOD6ypD4ycM1q79UK8rNVht3aCHF6O8nQOdURBaiFO0dXpTcz2Y4jQiWs9vViWiyvEahOPp5nNRBV6s9lPH1wWDlpx4imhRo1eAG6EH_hucHvgKVL_YCV1nFdcFgLaI7II2cSZ6gkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ با قطار آزادی وارد داکوتای شمالی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/131323" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131322">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سفیر آمریکا: «رابطه واشنگتن و تل‌آویو شبیه یک ازدواج ایده‌آل است که در آن جایی برای طلاق وجود ندارد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/131322" target="_blank">📅 22:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131321">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
رویترز گزارش داد که مقامات فرانسه تجمع منافقین در پاریس را بخاطر تهدیدهای سلطنت طلبان لغو کردند.
🔴
خبرگزاری رویترز گزارشی از طرف نهادهای اطلاعاتی فرانسه را رویت کرده که در آن به تهدیدهای فعالان سلطنت طلب به بر هم زدن گردهمایی مجاهدین و حتی تهدید به بمب گذاری اشاره شده است. ظاهرا بر اساس این تهدیدها بود که دولت فرانسه تصمیم به لغو تجمع مجاهدین گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/131321" target="_blank">📅 22:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131320">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=QQWplehrt55l-lWYXX-85V_dGdp7Dwd9W3eHPFNqJUvlo8vpzT-Toh9QTawqmtFCh5tQPFOJ__KU1JmSDGr0dIupj1auvvsn5exsEFgVYRDBf3WmTnlZe0cYGSC-DqngAt-07R1d84jLaA25gVsVsAvtbDGOSXXxftNAXIVPcVy5RSu6Ijo9Q4dkUIz15FLrh7yY74qDFD886mt9abDBahfUxhDBoqO4FtyypuWPgQOZ2PNgSl7YtZwoJB_BRcxNRVX-Ws4umm_8bi-r9RyFU3Bbj-Dca-Je7VGm3AzTZGLpxhlbnd8hPqTlQR_rb17PS8o_g85UufTMTyfnWdHCtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b73eec92a.mp4?token=QQWplehrt55l-lWYXX-85V_dGdp7Dwd9W3eHPFNqJUvlo8vpzT-Toh9QTawqmtFCh5tQPFOJ__KU1JmSDGr0dIupj1auvvsn5exsEFgVYRDBf3WmTnlZe0cYGSC-DqngAt-07R1d84jLaA25gVsVsAvtbDGOSXXxftNAXIVPcVy5RSu6Ijo9Q4dkUIz15FLrh7yY74qDFD886mt9abDBahfUxhDBoqO4FtyypuWPgQOZ2PNgSl7YtZwoJB_BRcxNRVX-Ws4umm_8bi-r9RyFU3Bbj-Dca-Je7VGm3AzTZGLpxhlbnd8hPqTlQR_rb17PS8o_g85UufTMTyfnWdHCtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، نتانیاهو، درباره تیمی که در جام جهانی فیفا طرفدار آن است:
تیمی که من به‌ویژه دوست دارم، تیمی است که امروز در جنوب لبنان دیدم.
🔴
فرماندهان ما، سربازان ما، این ذخیره‌ها — آن‌ها قهرمانان جهان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/131320" target="_blank">📅 21:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131319">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=EGROriWErYdekDorgjZezexB0OoRnwTRQqB2PJRUiQ-_gK-7pI9RfU2Zi3uwhRbNVUTfmppsYFvtgf8sVPgCXQK3xmsYy2cqXC7aYxXJYworZvEoaxyu-taGYGxrRYvbzF1y8NLvwWjm6AK2nDJA2A7J7OBT6JQ9I9PVKcwaki_XkdOv3zcvK8-jtZiSwe1rWhfqrqpnBTe_tR0zJE-z3lzgaRTwXgHeEx5gWRhhla9BgNHOXHn-5KALUVcB1WkDsK1-MJZAS9e5HY4kGhZtAoOenTUoCV2lgTqcyoom24isA4SB2DgTiUjheLccPLDDiInLkhO3N1JvEDV1mQ6Ctg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8845591e.mp4?token=EGROriWErYdekDorgjZezexB0OoRnwTRQqB2PJRUiQ-_gK-7pI9RfU2Zi3uwhRbNVUTfmppsYFvtgf8sVPgCXQK3xmsYy2cqXC7aYxXJYworZvEoaxyu-taGYGxrRYvbzF1y8NLvwWjm6AK2nDJA2A7J7OBT6JQ9I9PVKcwaki_XkdOv3zcvK8-jtZiSwe1rWhfqrqpnBTe_tR0zJE-z3lzgaRTwXgHeEx5gWRhhla9BgNHOXHn-5KALUVcB1WkDsK1-MJZAS9e5HY4kGhZtAoOenTUoCV2lgTqcyoom24isA4SB2DgTiUjheLccPLDDiInLkhO3N1JvEDV1mQ6Ctg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: ممکن است روسیه امروز صلح را در اولویت خود نبیند.
🔴
ما آنها را وادار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/131319" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
عضو هیأت رئیسه مجلس: حتی اگه آمریکا گندم رو به ما ارزون‌تر هم بفروشه، نباید از این کشور خرید کنیم.
🔴
نباید پول به جیب قاتلان رهبر بریزیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/131318" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پزشکیان: اگر رهبری دستور می‌دادند مذاکره نشود قطعاً اطاعت می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/131317" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-131316">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی:
پیام آمریکا در دوحه به ایران این بود که «بزرگ‌تر فکر کنید؛ رفع تحریم‌ها در چارچوب یک توافق گسترده‌تر ۱۰۰ برابر ارزشمندتر از اخذ عوارض از کشتیرانی است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/131316" target="_blank">📅 21:22 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
