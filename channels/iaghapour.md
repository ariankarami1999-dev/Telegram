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
<img src="https://cdn4.telesco.pe/file/vIpfBCE142Wb3dR7L1QMUp5ZXL6V1McFwPMOG8u5K-nKYQgJoOusVUG28zDqlhfbGZrEGbiOWYXFeDEAFshz3fx8DZTaRDeLXMjfuWCPlrrUApX4Ou7a7m_1tNPgM58NC_f8jD2C-BffW8MaEair1N5roZj18uwoGHkRzsasgv-o_IDjx6qiydS1Rw-ZLK4064fpIuk6BamZjaUVBhimJ1PSIY-sf6Y1TgMnxNPtirmhnDlTnW9V0mI6r-NVdaPD7DS_a9Lq6BbFqykpmWtXWJw-khRNtVDGRvgCRrXVHayQrJX8umxqQtyK1dU5iFeEPNGWpgDE_v-W4Ljo4ulctA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.4K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-3096">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐓𝐞𝐜𝐡𝐉𝐮𝐧𝐤𝐢𝐞(𝐓𝐉)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFzvXieo3pVsZ8tovmlNAE2YyReD7jnSWNS8Na4a4TTsOfErjt9dUcGWLeLR1JTYiYpdgcHTYwsTvnfdAp2FjKzzQpqNK3wP0a36g6B8s-jQI0yLsCz3oNOtziw90q_MmCPSngnEmL5jQwdNeI-VlOMJQKYUrNYIo5JwBrQrfS4ydsvowAWW1Qf7aNgYNoQUdrf0vW_oqQoUcAPI6B29JaoFa-UQiaU4H4t_iAxGYHw2dczoyG3Cx4iq05KLHEwPyA8-owd-jk5CymvGWqVbKIJK7Wn06sSpSeYG2G_DznncQ_C2NEvNLnoHCjLbb3TSdnOgfn1gJAQ5BEh2QK-pDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اکانت 18 ماهه Gemini Pro رو می‌تونید فقط به قیمت 390 هزار تومن تهیه کنید
✴️
📝
​توضیحات:
✅
اکانت اصلی و امکان دعوت تا ۵ نفر
✅
📱
آنتی گراویتی،عالی برای کد نویسی
✅
برای طراحی عکس و فیلم هم خیلی خوبه
✅
فعال سازی روی جیمیل شما
✅
تولید عکس با Nano banana پرو
✅
تولید ویدیو  با Veoپرو
✅
استفاده از Notebook LMپرو
✅
۵ ترابایت  فضای ذخیره سازی شخصی
✅
شما فمیلی اونر خواهید بود
✅
امکان فعال سازی بر روی تمامی ریجن ها
🛒
جهت خرید :
🔻
🔻
✴️
✴️
@proTJshop_bot</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/iaghapour/3096" target="_blank">📅 21:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3095">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/du46xi3be45EpN92_sYj7FoteuaVPUiB3N7pHws5LeerYJte1oj0MWbtPqDTvfuvoXSkL1ygtGrRHiXapZuL2RuSSbAnGUuudsdEl5Uzl6aqhgzIlw3JyiyWBRZIfbNcv9_3_Pd1eSKGP9KIsZBzUYycf0MoZb51aQsVCJ16lZu620m7VCilI2SZA0c5jbykHTdkn_VSCr4Wy4kOAsj6r_bFz6pk0jjaGtsugE3I7ksaG2TpGD80aeAOs30d4S9N0MJjIIz9AQuJC24D7pJl3MdzmuDiz1F49EcItj4HacqQEgJAOWycQgrm4HEbj9tzXvdxiyoKWXK5ZNhDRJdZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کلادفلر تأیید کرد: ناهنجاری بزرگ و افت غیرعادی در ترافیک اینترنت ایران
داده‌های رسمی رادار کلادفلر نشان می‌دهد ترافیک اینترنت کشور از صبح یکشنبه ۱۲ مهر با افتی ادامه‌دار و تغییرات ساختاری بی‌سابقه روبه‌رو شده است.
⚙️
شاخص‌های کلیدی گزارش کلادفلر:
🔹
افت ترافیک کلی:
کاهش محسوس در ریکوئست‌های HTTP و داده‌های جریان شبکه (NetFlows) از ساعت ۷:۱۵ صبح ۱۲ مهر که همچنان پابرجاست.
🔹
تغییر سهم پروتکل‌های وب:
سهم ترافیک انسانی HTTP/1.x از ۵.۳٪ به ۱۵.۲٪ جهش یافته و سهم HTTP/2 از ۹۴.۷٪ به ۸۴.۷٪ افت کرده است (ترافیک HTTP/3 و پروتکل QUIC پیش‌تر نیز بسیار ناچیز بوده و عامل اصلی این تغییر نیست).
🔹
افزایش سهم درصدی IPv6:
سهم IPv6 از ۴.۳٪ به حدود ۱۵٪ رسیده است؛ این افزایش به دلیل افت شدید حجم کل ترافیک IPv4 بوده، نه لزوماً رشد فیزیکی دیتای IPv6.
🔹
اثر ملموس روی کاربران:
افزایش شدید پینگ، اختلال گسترده در اتصال تانل‌ها و کانفیگ‌ها، و لگ سنگین در بازی‌های آنلاین.
هنوز منشأ این وضعیت میان محدودیت‌های هدفمند زیرساختی یا اختلالات فنی مسیرهای بین‌المللی رسماً تأیید نشده است.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/iaghapour/3095" target="_blank">📅 20:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3094">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaKB16OkmzysT6uPW_3Wl-vRiVikoz79f_0eW-gUQy20oBiVhbxIS9CBEh6R-sy_gZwdaiRRytE4akNffSkBD53vUXaSwre8pE4xW1QNwXmFhC7vcqZVSoK3RBe5gOioduIwm5IX8zcBSG2KXKGolXkD99LBFoApcFdU_CQ5Bw0tYO7aeGGlYRo5JBE3HEtSFwcM7vD38k2m5BK_-6NlEC4_gOWtACxIoVieL8CYBwGVHabwXx4gyaF19R-BDi3VOVOARXmHM9vmlF3wNY5xwVlFFhxDv6HBiYTYIBVB9_CkVtHtKMj9zPgUvwaYHs1AfubGqnFau0FgkBWmyAcJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
پرونده جنجالی فیلترشکن جامپ‌جامپ (JumpJump)؛ شایعه هک فیک بود، اما بدافزار واقعی است!
اسکرین‌شات فروش اطلاعات کاربران جامپ‌جامپ در دارک‌وب ساختگی از آب درآمد، اما بررسی‌های فنی نشان می‌دهد خود این برنامه یک تهدید امنیتی بسیار خطرناک است.
🔹
نسخه‌های تلگرامی دستکاری‌شده:
نسخه‌های غیررسمی پخش‌شده در کانال‌های تلگرامی با سوءاستفاده از آسیب‌پذیری‌های اندروید تلاش می‌کنند دسترسی ریشه (Root) بگیرند؛ دسترسی که به مهاجم اجازه کنترل کامل دستگاه (دوربین، پیام‌ها و فایل‌ها) را می‌دهد.
🔹
رفتار مشابه گروه‌های سایبری APT:
تغییر سیستم آپدیت به کانال‌های تلگرامی و جعل امضای دیجیتال برای نصب بدافزار سیستمی.
🔹
مجوزهای خطرناک نسخه اصلی گوگل‌پلی:
حتی نسخه رسمی نیز ۳۷ دسترسی غیرضروری از جمله IMEI، فایل‌های شخصی، سیم‌کارت و دیتای رفتاری را ثبت می‌کند.
🛡
اقدام فوری:
اگر این برنامه را نصب دارید، فوراً آن را حذف کرده و دستگاه را اسکن امنیتی کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/iaghapour/3094" target="_blank">📅 16:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3092">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m57D84zkMLTEvN0C2Ss3QkoHySC0EEJepWq4LnQFZ520lXfEjKZ72p8uBpUZ1_g_YjjoTl2gSAqH0P1MhxtdJgCEcV91VlEtYT4BtctMsFk19pdguwaofVP4bwofHO-5mr43cr48-MI1KRww01hl2N-y2CaqZvvln5mZ7pL0BuxHqE-s-dGtQkhabzVV_Ylxj6Lq0HRsO1Rd28og2W9xB47o3yhmQGdzROfaalTEpC57S_abpkS1OApjCsmWNiJErWCTsINX5j2Qp_TkslC1w0BcOim3ul_957BuzvxXYqpulN0N4_qh1i7HgDJmaLGB6Uear4rB-VeWOFmR6ri6yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مذاکره‌کننده گروه باج‌افزاری «کیل‌‌سک» بازداشت شد؛ مدیرعامل ۱۶ ساله یک استارتاپ هوش مصنوعی!
مذاکره‌کننده مظنون گروه باج‌افزاری بدنام
KillSec
شناسایی و دستگیر شد؛ فردی که در پوشش زندگی حرفه‌ای خود، مدیرعامل یک استارتاپ حوزه هوش مصنوعی و تحول دیجیتال بوده است!
⚙️
جزئیات ماجرا:
🔹
هویت دوگانه متهم ۱۶ ساله:
وی در معرفی رسمی خود مدعی شده بود که هدفش کمک به کسب‌وکارهای کشور عمان و منطقه خلیج فارس برای پیاده‌سازی راهکارهای هوش مصنوعی و ورود به دنیای دیجیتال است.
🔹
نقش در حملات سایبری:
شواهد نشان می‌دهد این نوجوان به‌عنوان مذاکره‌کننده و نماینده گروه KillSec با قربانیان حملات باج‌افزاری تماس تلفنی برقرار می‌کرده است.
🔹
سرنوشت قضایی:
متهم اکنون با احتمال استرداد به پورتوریکو روبه‌رو بوده و مجازاتی تا ۱۰ سال حبس در انتظار اوست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/iaghapour/3092" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3091">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG4Oa-pmTmfn2eHiRHDNk9OixbaW9FL3Fx6zZl_m944J2G3lpDmRw7LRNjq4Hls6NbLxN-zbJ2k3Z78HC5CRd565qVtiJ6q91wrsHDeMApSciQaYwXTxW2yZOv5Tf7X_3ukvpR3KgQyZEJwlB-OnWqck4Z4Za4DXuwQsKbTqGKObFv_lSohHlO-nyIeaE8upURzmZfMGW5xWxLMmWbj69EqHD2zYMUGA9m5R7rqCmg6rFBchC_5UaV8gNYgJMKinB3I0_Qx74CU5A_s0FbSl9tCqlZRb0lpx-8QxBDNvFIiYVF8fYIsacoIf4wkivW_SDadRUQTzluhZzosSYUVS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
️
پایان دسترسی رایگان به جمینای پرو و فلش
گوگل با به‌روزرسانی اسناد پشتیبانی خود سیاست‌های جدید دسترسی به مدل‌های جمینای را اعلام کرد که بر اساس آن، دسترسی آزاد به مدل‌های پیشرفته محدودتر می‌شود.
⚙️
جزئیات تغییرات و سطح دسترسی پلن‌ها:
🔹
کاربران رایگان (از ۱۷ مهر / ۹ اکتبر):
قطع کامل دسترسی به مدل‌های Pro و Flash؛ تنها مدل فوق‌سبک
Flash-Lite
در دسترس خواهد بود.
🔹
پلن AI Plus (ماهانه ۴.۹۹ دلار):
حذف دسترسی به مدل Pro؛ دسترسی فقط به مدل‌های Flash-Lite و Flash محدود می‌شود.
🔹
پلن‌های AI Pro (ماهانه ۱۹.۹۹ دلار) و AI Ultra:
دسترسی کامل به هر سه مدل Flash-Lite ،Flash و Pro حفظ می‌شود. همچنین قابلیت پردازش عمیق
Deep Think
بدون هزینه اضافه برای مشترکان AI Pro فعال خواهد شد.
📊
قابلیت‌های جدید و سیستم محدودیت مصرف:
• امکان تنظیم سطح پردازش و تفکر مدل‌ها در سه حالت کم، متوسط و زیاد (تحلیل دقیق‌تر به قیمت مصرف بیشتر سهمیه).
• ریست شدن سهمیه مصرف مبتنی بر توان پردازشی هر ۵ ساعت یک‌بار تا سقف مجاز هفتگی.//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/iaghapour/3091" target="_blank">📅 17:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlzUn8dWh4gYXWhzH4q00XnDNNv1NoyJ36jbJMXxW-VF6CTBMOR4oxK0qdmryilGSXm0lgtjicnq-voO3PKhgE5csrM4tbbSORD_W_-FBkjOz3P3xr_u6Z07AlZzs9juoLZ3nrZse2vIb5gk0sl7RbN2Q8WbManCUnhNaTK_EtfURXf8pAKCC36ntEp8BHESChd9kQk4reClmIrSzxGmG5yYPvflEEDiPAvxvpcfq0XXHiuBMkln1m10oSHyR66Cw2B5i6sJ9FNQ5rxpQk987YrLPPLItXlzpI_10ulyds0iaDeuXer1-HqYCoY_E7sr64NGsPRcLSxraNGo4dx94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
معرفی FleetPanel؛ کنترل‌پنل امن برای میزبانی هم‌زمان چند ربات تلگرام روی یک سرور
اگر چند ربات تلگرامی را مدیریت می‌کنید، اسکریپت و پنل
FleetPanel
به شما اجازه می‌دهد همه آن‌ها را به‌صورت کاملاً ایزوله روی یک سرور لینوکس بالا بیاورید.
🔹
ایزوله‌سازی کامل هر ربات:
هر ربات دارای یوزر مجزای لینوکس، استخر PHP-FPM اختصاصی، دیتابیس MySQL جداگانه، کانفیگ اختصاصی انجین‌ایکس و گواهی SSL مستقل است تا مشکل یکی به بقیه آسیب نزند.
🔹
پنل وب و CLI:
داشبورد مانیتورینگ مصرف CPU و رم، نصب خودکار ربات از طریق وب‌هوک و دریافت توکن، تهیه بکاپ و بازگردانی خودکار.
🔹
امنیت سخت‌گیرانه:
رمزنگاری توکن‌ها و پسورد دیتابیس با استاندارد AES-256-GCM، هش ایمن رمزها با Argon2id، فعال‌سازی CSP سخت‌گیرانه، محافظت در برابر حملات CSRF و مسدودسازی وب‌هوک‌های بدون Secret.
🔹
عدم تداخل با سرور:
اسکریپت به سایت‌ها، گواهی‌ها و دیتابیس‌های موجود سرور دست نمی‌زند و فقط فایل‌های اختصاصی خود را اضافه می‌کند.
🔗
سورس پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/iaghapour/3089" target="_blank">📅 20:50 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3082">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام بچه‌ها، وقتتون بخیر.
به دلایلی حساب‌های توییتر (X)، اینستاگرام و چند تا از پلتفرم‌های دیگه‌مون رو خودم موقتاً غیرفعال کردم. از طرفی طی روزهای آینده رویکرد و مسیر کانال هم یه سری تغییرات داره و از مباحث فیلترشکن و... فاصله بیشتری میگیریم.
فعلاً نیازی به توضیح بیشتر نیست؛ سر وقتش کامل براتون توضیح میدم. ممنون از همراهی همیشگی‌تون.
💚</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3082" target="_blank">📅 20:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3081">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmcfcJiuExQiR2e0-Cpp38dmG3yF9nCbcQMKqfexgPRKHHdeR7P7wUuBAGUPeMVeCsKCKN7bva8qCbGQPMEK9gPotJFA-yOVyZAfOxIKC16bE8kUymmMaAhJAURIzxadK-Pbtm7-RUSK5pHtS6nEljivuQuc8pZ1Ts22tWRhTQQUvUQzCOPXzeJDfnMBpgPWoagT0STYx7OGzO1VXqX_OICgteZVTMSonKsWeSXcbTT9HnBNPQnOlYYwKEu_KofQBACyLpvqUxckzgZgKct4LJo6vHA349SSjHh3dnWy6efzD86qvnVRB0GNBaQa476-wonl-4NdJbaQmtGSKXVTzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
درخواست اپراتورها از وزیر ارتباطات: فیلترینگ اینترنت ثابت و فیبر نوری را بردارید!
در جلسه کنترل پروژه فیبر نوری، مدیران اپراتورهای اینترنتی با اشاره به هزینه‌های سنگین توسعه و عدم استقبال مردم، پیشنهاد رفع فیلترینگ اختصاصی روی شبکه ثابت را مطرح کردند.
🔹
پیشنهاد رفع فیلتر برای جذب کاربر:
نماینده صبانت اعلام کرد برای ایجاد انگیزه در کاربران و افزایش فروش ترافیک جهت جبران هزینه‌ها، مسدودیت پلتفرم‌ها حداقل روی اینترنت ثابت برداشته شود؛ چرا که کنترل امنیت در شبکه ثابت ساده‌تر است.
🔸
اقتصاد در حال احتضار اپراتورها:
نمایندگان شاتل و پیشگامان از خسارت‌های چندصد میلیاردی ناشی از قطعی‌های اینترنت، هزینه‌های استهلاک باتری‌ها در خاموشی‌های برق تابستان و عدم اصلاح تعرفه‌ها گلایه کردند.
🔹
کیفیت پایین اینترنت ثابت فعلی:
به گفته مدیرعامل زیرساخت، کیفیت ADSL کشور به شدت افت کرده (سرعت آپلینک ۶۰٪ مشترکان زیر ۸ مگابیت است) و همین امر بار مصرف را به شکل نامتعادلی روی شبکه موبایل انداخته است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3081" target="_blank">📅 19:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3078">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_9Yk2E9bXrDSXz20LOyGpSmy2gC0xefWAREuXZLGSQVXynWwR6gr16vQ88wBwLjbEb8GlifFZXx2xua0K_-L_j0SpdGHnZfklAmRvaNwOj0cA1JpjhAKuHT-Ym4JZlY0hFdTEzqIo5zEr_J2umv5XvBjSS00f-55aek7cc25btfhyFT4b5Py7UlX8oR-XfrXUJNPZ3f_9nrO1lWROEJryFjCOtFfM_YlWs8BHQAeMlqP4Vp5WG-8-5DxIqspGSM22lBe3QqM5NkfSxPGYXVTmQJt_VLi2JeDT6GjaLllQ6otQq43OYblJx249TobCwAnzP17gHbUJjGomSbqbz-BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعضی‌ها واقعاً فکر می‌کنن ما همین الان از پشت کوه اومدیم!
🏔
😅
ماجرا از این قراره که وقتی ما بین کامنت‌های یوتیوب قرعه‌کشی می‌کنیم، تو ویدیوی اعلام نتایج، اسم، عکس و آیدی دقیق برنده مشخصه. حالا اتفاقی که میفته اینه که یه عده از دوستانِ فوق‌تخصصِ جعل هویت، تو سه‌سوت میرن تو یوتیوب اسم چنل و عکسشون رو دقیقاً شبیه برنده می‌کنن، یه آیدی مشابه هم میسازن و میان میگن: "سلام، من همون برنده‌ام، هدیه‌م رو رد کن بیاد!"
🥸
🎁
رفقای زرنگِ من! فارغ از اینکه این هدیه واقعاً ناقابله و فدای سرتون، ولی یوتیوب یه چیزی داره به اسم Handle (همون آیدی با @) که تو کل دنیا یکتاست! یعنی هیچ‌کس نمی‌تونه آیدی تکراری داشته باشه. ما هم موقع تحویل جایزه، فقط همون آیدیِ اورجینال رو چک می‌کنیم، نه یه اسم و عکسِ فیک!
🕵️‍♂️
خلاصه که سرعت عمل و خلاقیتتون قابل ستایشه، اما متأسفانه جواب نمیده!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3078" target="_blank">📅 20:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3076">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtw2bdecJVLSu5oQ0Pjx_WsD3-K2xTM9WoR0ngcw3ZZIPy3bQzdd4hGFbO4LcxNWW-vplyM-DQuAugP43FJS6ZIwPZfvQJeu4Y5nrg51MvRTrSRVPNPIZbnnNI7wZ88eHVlNiki4WGp9FSoStB5G6cJL75xKjUgog2LjeSiLNSKiANGK1w0NJS3AiYe1c3Zojnh9Dz3oYNdpZK4hEChgNEa87GiRwd1E79lsCoCL5ehIFl68Yt3IskL_cYAwErNEV8u7b__pt3sdRfhJ-sZvET_48bKTAEws8jlVgIIaML6BFR2_wnK_-eFQo4f5rEIftEyuxqqLdH9vYv-hL5cqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
مدیرعامل مخابرات: اختلال اینترنت برطرف شد / وضعیت IPv6 بررسی می‌شود
محمد جعفرپور، مدیرعامل شرکت مخابرات ایران، در گفت‌وگو با رسانه‌ها از برطرف شدن اختلال چند روز اخیر اینترنت و فیبر نوری خبر داد.
🔹
علت اختلال چندروزه:
قطعی اینترنت، سایت شرکت و سامانه ۲۰۲۰ به دلیل ارتقا و به‌روزرسانی زیرساخت‌های سامانه‌ای مخابرات رخ داده و اکنون اتصال کاربران بازیابی شده است.
🔹
وضعیت پروتکل IPv6:
جعفرپور تأکید کرد از سمت اپراتورها منعی برای ارائه IPv6 وجود ندارد، اما سیاست‌های بالادستی شبکه در اختیار آن‌ها نیست.
🔹
احتمال تأثیر تغییرات دوران جنگ:
وی اشاره کرد که تغییرات فنی اعمال‌شده روی شبکه در شرایط جنگی ممکن است همچنان بر وضعیت دسترسی به IPv6 اثر گذاشته باشد و این موضوع نیازمند بررسی فنی دقیق برای شناسایی منشأ اشکال است.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3076" target="_blank">📅 14:06 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3074" target="_blank">📅 20:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3073">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQl2_60TUbCbrrGr30N0CXcbvYkrMt-L8jt9dyP60GnTEkONbt1aGq7owqgJKrYnYJMoxre2QyZNmGR7F9xhs069crSAGsTCK-hIZ3dIMRQcABezOP-hjnHSSmFbWuugtb6Rq73V0wY452KOTQfdSFnVuxAH3e9xl2IdowZu1ORWZADWPEbT0RVCsu8WhemBeSr_ibvw3hEJXHwT8ZUfmCjCnMQ_Mf8injg3Ou8hgIQrIzCvV2gymYxocTHL63VUmnG-vBsTOfK0_SSjjUO806LFujILJY1NRXWk0Xu6JKTMUVv5DP8mvLmuG7kVL3py2u2wISnjnmvjeEOod_Ctiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
تولید ویدیوهای 1080p با هوش مصنوعی برای تمام کاربران گوگل فعال شد!
گوگل قابلیت تولید ویدیو با کیفیت
1080p
را در ابزار
Google Vids
برای تمام کاربران عادی و مشترکان Google Workspace در دسترس قرار داد. این ویژگی با بهره‌گیری از مدل پیشرفته
Gemini Omni 1.1 Flash
کار می‌کند و ورودی‌های متنی، تصویر، صدا یا کلیپ‌های موجود را به ویدیوی خروجی تبدیل می‌کند.
⚙️
قابلیت‌های کاربردی و کلیدی:
🔹
توسعه هوشمند صحنه‌ها:
امکان افزایش طول زمانی کلیپ‌ها با حفظ ثبات کامل در نورپردازی، چهره کاراکترها و زاویه دوربین.
🔹
هماهنگ‌سازی و افزایش رزولوشن:
تنظیم دقیق مدت‌زمان هر فریم برای تطبیق با صدای گوینده، به همراه ابزار ارتقای وضوح (Upscale) کلیپ‌های قدیمی به 1080p.
🔹
سرعت بالا در تولید:
رندر هر صحنه ویدیویی در این پلتفرم در کمتر از ۳۰ ثانیه انجام می‌شود.
سهمیه استاندارد به تمامی حساب‌های رایگان گوگل اختصاص یافته و کاربران طرح‌های تجاری و پولی سهمیه ساخت بیشتری دریافت می‌کنند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/3073" target="_blank">📅 18:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
اجرای مستقیم و بی‌دردسر پروژه‌های داکر با Docker Compose در دوپراکس!
🔹
دوستان عزیز، یکی دیگه از قابلیت‌های فوق‌العاده دوپراکس بخش App Space و پشتیبانی مستقیم از کدهای داکر کامپوز هست!
🔸
اگر پروژه‌ای دارید (مثل ربات‌های تلگرامی، پنل‌های خاص یا وب‌اپلیکیشن‌ها) که با فایل
docker-compose.yml
اجرا میشه، دیگه نیازی به سرور لینوکسی خام، نصب دستی داکر و درگیری با کدهای ترمینال ندارید. دوپراکس یک محیط کانتینری کاملاً آماده در اختیارتون میذاره.
📝
مراحل اجرای پروژه‌های داکری:
1️⃣
ساخت فضا: از منو وارد بخش Container Platform بشید و یک App Space با منابع دلخواهتون بسازید.
2️⃣
تب Compose: وارد فضای ساخته شده بشید و در بخش Topology، روی تب Compose کلیک کنید.
3️⃣
وارد کردن کدها: کدهای فایل داکر کامپوز خودتون رو مستقیماً در ویرایشگر پیست کنید، یا اینکه خیلی راحت با دکمه Upload YAML فایلتون رو آپلود کنید.
4️⃣
اجرای نهایی: در نهایت دکمه Apply changes رو بزنید. (حتی گزینه‌ای برای جایگزین کردن امن منابع قبلی یا Override existing resources هم وجود داره).
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کانتینرها، شبکه‌ها و والیوم‌های (Volumes) تعریف شده در فایل شما رو در لحظه می‌سازه و پروژه رو ران می‌کنه. یک مدیریت کاملاً گرافیکی، سریع و حرفه‌ای!
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3071" target="_blank">📅 20:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3069">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iS4FVbwa8bao7mGogYcBNFXPe_kefurg8HSLA7gruWSeli6IBqWRuKV4bqbdrapD3QPP08KEzAfmQ4_Ms_-SbKFxHEbja4at7mvgikQEolMu-ld8A3Nxna5sLJI4nTjCN3y_1DWWMSCnCZc_C5z1o693IPs-poiTEqC9YbSy2oHq6YwB4n5IlOcpembmuo4PnKuVuSrZKvtaXSVCMFPF7aqQapJlquQ_xCIwY__BPU792uOGcqyoH0m4Jv-LOxok8d5v89k9tLYLPzwEdcmekbatDY_J6Mms1kVlNvZ9zWEEmw4Yg1QGTI4puPc4GeEzJaL3wXYzDEBcICEOEV2C_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDjAZVDmDXibL5OZBMVAN0_RILCm3Py8uwCk9Ry7WnlRmzwBKBUS9wGCj_EZ3N1TSD6IJ8jIt4NgCVQJhnYkpWRp4eTlMiLgfTDDzyOd_cLh5hbydJBvqgEvADQdj4gCw5DT28Ib9Fqj--NbyMGJl9zdsG429xC6UzXWJnR-8ZhbTUkX2sj8Y3Li_ohm0WRTr6pltOy2dApUsjtOM5WchS0pLDYltS6r2-O7N9OvVH3mdfyjilquyZU-Neur-lvpM39TCjQEDAIO3NicVBJZk1Occ4rRt2-kAJRDDpkCth622VKFgKq1-lZFzRQQ6PIwBvhuuYR8UhpoZ2s6bWdB2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سلام به همه همراهان عزیز کانال!
💚
به لطف و حمایت‌های گرم شما، تونستیم
8 عدد کیف
مدرسه و تعدادی دفتر و... رو برای چند تا دختر کوچولوی دبستانی تهیه کنیم. (همشون تو عکس جا نشدن)
این هدیه ناقابل، نتیجه
مهربونی
و
همراهی
تک‌تک
شماست
و از طرف همه‌مون به این بچه‌ها تقدیم می‌شه. سال قبل هم اگه یادتون باشه اینکار انجام شد.
اطلاعات بیشتر
ازتون ممنونم که باعث و بانی این اتفاق قشنگ شدید. دلتون همیشه شاد و لبتون خندون.
🌹
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3069" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3066">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=CTihWeigQV4myNad8Da5h23DVvRsl2H4BGR3scrZz3ZI3zf462v9pBKOQ5xUWfGwe0kHrnMKMOesJmJ4UiFxWhovbazqAS3z9b-dkPVjqUA8xClhoNhwAL4wwOU3S_XvaIKs6xtQnmzQ-vXVbuavH_-HUT2Dumei6yrDV40uZvN8Amry7_CDgzi87Ol6cIlltrM7cHenuDfNJV_45jDphfTub5_Kw3v5SynKHFuFJVMF0m2LJnxcSLiwXuJi6rto1MTs1Xwi4C4DZDHf6vOyilE9owDH39brooBpHdRGIVRk7qpQfg31dX_iHvwGiOmZtaT5fA4cme9XlrLisCwI_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a941f5d680.mp4?token=CTihWeigQV4myNad8Da5h23DVvRsl2H4BGR3scrZz3ZI3zf462v9pBKOQ5xUWfGwe0kHrnMKMOesJmJ4UiFxWhovbazqAS3z9b-dkPVjqUA8xClhoNhwAL4wwOU3S_XvaIKs6xtQnmzQ-vXVbuavH_-HUT2Dumei6yrDV40uZvN8Amry7_CDgzi87Ol6cIlltrM7cHenuDfNJV_45jDphfTub5_Kw3v5SynKHFuFJVMF0m2LJnxcSLiwXuJi6rto1MTs1Xwi4C4DZDHf6vOyilE9owDH39brooBpHdRGIVRk7qpQfg31dX_iHvwGiOmZtaT5fA4cme9XlrLisCwI_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی (دوره سیزدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده  اکانت هوش مصنوعی مشخص شد:
👤
برنده عزیز با آیدی SattarBayat، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3066" target="_blank">📅 16:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3063">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsRZHIikKUXj3fqSC1VCvKC7PNezLk7Q4QuQGnyZ9-LTnZMHtZ0bvcMJ15bVAbSjXVyO-Jf_YG2liLmYYKuccmQ-ljjPH6tFnOZxGkSaoxA4Y_1regUj-qOpuTIyzHOfNdTzSBDxNcU74hfw8mPifNMhZoaKvnvM8DQ8mS5Xs_d1boDak-IeNDS6UQ_IgjXBzZAN8Huh6WvB_KcBit0RN-UcAyhgiWhtSFB6lHnNtnHIL8Yxvg42XkViJAaWmm0i3fMnIBeF1bVv9KEuRundEcFJl25DMOKeh_egMMFL8cOSK2ukbkROTwcYdMPXnO9l7VB0uvGuWHHnnfxS9cWgqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نشت اطلاعاتی چیست و بعد از لو رفتن اطلاعات چه باید کرد؟
رخنه‌ی اطلاعاتی زمانی رخ می‌دهد که هکرها با نفوذ به سرورها و دیتابیس شرکت‌ها، داده‌های هویتی، تماس، رمزها و اطلاعات بانکی کاربران را سرقت یا در دارک‌وب منتشر می‌کنند.
⚙️
۵ اقدام فوری و حیاتی پس از افشای داده‌ها:
🔹
تغییر فوری پسوردها:
تغییر رمز حساب هدف و تمام سرویس‌هایی که رمز مشترک داشتند (با کمک Password Managerها).
🔸
فعال‌سازی تایید دومرحله‌ای (2FA):
فعال کردن کدسازهای معتبر مانند Google Authenticator روی ایمیل و تمام شبکه‌های اجتماعی.
🔹
امن‌سازی حساب‌های بانکی:
مسدود کردن آنی کارت مشکوک، تغییر پسورد اینترنت‌بانک و فعال نگه‌داشتن رمز پویا.
🔸
استعلام سیم‌کارت‌های به‌نام:
ارسال کد ملی به سرشماره
۳۰۰۰۱۵۰
یا سامانه
cra.ir
برای بررسی عدم ثبت سیم‌کارت مخفیانه با هویت شما.
🔹
هوشیاری در برابر فیشینگ ثانویه:
عدم کلیک روی پیامک‌ها یا ایمیل‌های مشکوک.
⚖️
در صورت بروز سوءاستفاده‌های قضایی یا مالی، فوراً از طریق مرکز فوریت‌های سایبری پلیس فتا (
cyberpolice.gov.ir
) موضوع را ثبت و پیگیری کنید.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3063" target="_blank">📅 20:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP81chaUoDVAwqa96ig9Biwkqb17Pm5ociZmhMInVWJu_yQna9MKMLFLjOp_ze4mMcVRaf9_rbWTeSH3XaxWKiUdR8q3LMT9mql6g9x8Kbtq19paGDwIZJNaPfvgfDtjHNF9yImKn3FDVb-Tlzo8Q_DIhphZ0HMVPbSNhwVwmLqpG7-XEShCzF3jdc0TQNh6ScFtI4hgRTYio2es7f0m51zEYhl9DbaQshvsSk10PyQswofx4N4CV48i9y28knvDMapyM2AzrrQO4hfYLZvbD3ZeaexXp8tHrz4oKw-r4IdN0zBcND5pla8t53xvMszxIHI8Ed8sq23GC_-H3q3fgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎒
حرکت جالب WinRAR؛ فروش کیف به قیمت ۵ لایسنس نرم‌افزار!
شرکت
WinRAR
از یک کیف جذاب با طراحی آیکون نوستالژیک و معروف کتاب‌های خود به قیمت
۱۵۰ دلار
رونمایی کرد.
اکانت رسمی WinRAR در توییتر (X) با لحن طنز همیشگی‌اش نوشته:
«حالا که هیچ‌کدومتون پول لایسنس برنامه رو نمی‌دید، حداقل بیاید این کیف رو بخرید!»
😂
قیمت ۱۵۰ دلاری این کیف معادل خرید حدود ۵ لایسنس رسمی نرم‌افزار است و یک راه جالب برای حمایت از سازندگان این ابزار نوستالژیک به حساب می‌آید.
©️
Behrad Javed
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3057" target="_blank">📅 20:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3055">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdPcqYThlX9o5cjNAdJrRKxAeI320nvp3yAxQQ5FCfOnb20MRFoniHkXfDpEnZHzZScgHBsAfq1TJYP7Zop2sP5xmcVMDVsjnHlc3UNnZWyoUzPor1zGcS7gG8qZsf4E-lkadmjNA-xlrAQCNvNlp_BDgu_0FUn4gxr6RSFIFkkQXiMPfo_wu9VzBQ10NuNT8D56NjKHjE2haqhAJbJpWVpBW2lVlD9x_r9RbCwc8wi5zWVIX6IQTndgjpBuawr6dxbISlflHPX2jpU8U1x-YtL7U3-qLADA4Ld2AbdXSYVmMZ8JRDgRwRGlEGEbW_1WYQSwdU4H4_dVw_5RknT_Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
رئیس جدید گوگل دیپ‌مایند: جمینای 4 تقریباً برای عرضه آماده است!
پس از مدتی فاصله گرفتن از رقابت پرچمداران، گوگل در آستانه رونمایی از مدل قدرتمند و مورد انتظار
Gemini 4
قرار دارد. «کورای کاووک‌چوغلو» رهبر جدید بخش دیپ‌مایند گوگل اعلام کرد این مدل در مراحل پایانی ارزیابی قرار دارد و بسیار زودتر از پایان سال جاری میلادی عرضه خواهد شد.
🔹
عرضه زودهنگام نسخه پس‌آموزش:
کاووک‌چوغلو اعلام کرد با توجه به نتایج فوق‌العاده و هیجان‌انگیز تست‌ها، گوگل قصد دارد در اولین فرصت نسخه‌ای از فاز Post-training را منتشر کند و سرعت ارتقای مدل‌ها را بالا نگه دارد.
🔸
بازگشت به رقابت با GPT-6 و Mythos:
در حالی که رقبایی مثل OpenAI با معرفی مدل‌های سری GPT-6 و آنتروپیک با خانواده Mythos پیشتازی می‌کردند و عرضه وعده‌داده‌شده‌ی Gemini 3.5 Pro لغو شده بود، دیپ‌مایند هدف خود را مستقیماً روی جهش به نسل ۴ گذاشته است.
🔹
تغییر استراتژی فنی:
کاووک‌چوغلو علت تأخیر در عرضه پرچمدار را تمرکز موقت روی بهینه‌سازی مدل‌های سبک و سریع Flash دانست و تأکید کرد گوگل همچنان جایگاه خود در خط مقدم هوش مصنوعی را حفظ خواهد کرد.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/3055" target="_blank">📅 16:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTVs1w3Te6ca1LPyJVa9mNc65PYhx-0M643eWdjRKwet0KymeDB8RI9CmeheEPGUzv2JmZNhfOZEbtWsSNqq3q4bgcK1fTCMK5BDiB_dnYkOPhZ9GKn7_6L9zPuGraoa_DH-MEtK-CkGUtqDxsGIaF7usI7jWZRphQImYJFxl_1k68lzTTJ_C28SSnvUVxkGLL-c_qEAz8ugHAKTB6VBuWA0g8y6Hpw85gf5abgLJGJD0IIKissHDuo7wW8T9lCnZ64Xn81zviukj7olS2AV5M-OXb46lBQ5Y6A5BedghZJq0JJGRJecFmRObUXizTmiHqrQXbQnU1xCQ9QKMnHRzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAATaNGlYfCW-dv16POgtW11aRvp1YRaRDC_RVay0rT1XZRdMpHk8vSbdXgO6F4OsCWh3aD_hfQXy1Yvk10yz8X4an-O0RrISOtWy0amxZgGSN047wDfEhcpVCx6oaTB0an7qcKKXKkQL9No_3EcWg5z8_wCZyFzlqJeAb_Q3uMlNdFXlozwL6rsRDm7Ox4QAlyrDZI7Ne5OmhSFLg5Kt6W1iN-yc1SaXNQFrD-zLEt1g8G0JWSTH4hzWKe3ZqXx0X40RMc_pEZsrb3kg0sGBwIuWPlvA6tDzXvajEjDXFnbgA7PzzgTMx_vwOWPYWv9Er4t1rkn0ae24WxHBDoj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
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
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/js2yQRb5cxRGkvJHftsVR34nRaMrqOEy_ZA3hYo5ABZ3kU9lk2ghQPXmfyIIJZsq6LAILPKW65YCpa5_bL_mWYF-bvfkzW1gO5ZtrIDVx-0zo3aTB-N18znu-e2nGwlV5T7qP9jp6dgpL20KTHWMJChis9vHHGcGq82HhSAdapNs3YMbfZ9GCwEVAVHOxTtPYZdULP7GxShHRJq3STnoi10Qdi2zVEduprnPPU0WiXGPAZyCVQPTE6ShOFMHTORbkxg9u4Yf469h2gswVhLY-_2pK0LYEqrE4aNjH3kEPj1Ner3KGX26SDL6BGa0WNFb5vG-4OvfE6jl_6psGwN1Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=ijcC2w6xuXKKAbyDGKXG-MhTNJNfqD3Jc3zaqQLwSB_Z6GAZKnLafbIFbl89ywCGU9Nv8efZzVdBfUQaScS6dT35kreWpR8OuQq7ARzfhogWG71S4JHKncelRmFvcT2GtiFypO359bfXiMlQU2RY5qEACnbL-aEbXuEe2eIhAMmf5QLSVy8PQUwWFgIl3_sJ1_6AcHZ6ZzQ0Q8fPUYc0_Nt2Dyba8xQCfShRWNQrnw4ri9pFTxej13izukoCU7paQrWizDqWfjeguv4-GyAzSoZgzh8Cg5m2-EVweBAiLTj-lAfurVVU8WJtInTF08sNRUizuOhku5CboNGZGYvGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=ijcC2w6xuXKKAbyDGKXG-MhTNJNfqD3Jc3zaqQLwSB_Z6GAZKnLafbIFbl89ywCGU9Nv8efZzVdBfUQaScS6dT35kreWpR8OuQq7ARzfhogWG71S4JHKncelRmFvcT2GtiFypO359bfXiMlQU2RY5qEACnbL-aEbXuEe2eIhAMmf5QLSVy8PQUwWFgIl3_sJ1_6AcHZ6ZzQ0Q8fPUYc0_Nt2Dyba8xQCfShRWNQrnw4ri9pFTxej13izukoCU7paQrWizDqWfjeguv4-GyAzSoZgzh8Cg5m2-EVweBAiLTj-lAfurVVU8WJtInTF08sNRUizuOhku5CboNGZGYvGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGzrGZzk3QrQqnO6PKZwLVl5J1u2lN3WycS3ZrLYGODtH6MaDSWEIPdSN5BxUuURYMyWuA_U3F_Q8z2vIqxQlRXWY-MTh20vCS7x5U12FcucRqYu9BpxgiReQDa5Z24fseXgc3ZcduoCWtypwl1qo9jLQUTkLrbIzgxgzbzd43uOx2VMAFhk1zYFpIUTZdeS4wGN0CnzBoCo0K9CPVhcf5zIGjdEX_an7zjGRggQkTEC1nexx1E-rPHpslHZUFgS9ZZgdSEDCii5p7JFjcCzgsHck_SH0khAl_rViQ7nRrvBA7z1Tko3UkzCvAi3f4pKcVhw_mDrV96Qpb2TKcDXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfcCehuRFXO5POdAhBup6WCYghExfTxASubgcs7mIU2Jy94tuF-OAUCNgxWtNuuZvtlhTYDU6FEOm_JZagqAWJ3JHfoMVhNhsriAcyxczUgslwzwppQxF1OsCzqsuOhVqzb9iq9ET7RDx6iTp_cgDyNMYVFGU5EoZM7N2Ca8u2wSDFSLOYvNOAhOFZRyd3el-f_yxC6bHD_4FnupnDCvzNxYwGvuG4KMZEXmcdQ3DVaZ5UnHZq2i66RrBamDLiS8pURW3jBrx_VIJDir0mvdW6VEmGJidJSHPtCiG_lsGyw9dfRrRDqLMgrLpeS0lWryjj9J7lnwkePxV5vVlF9g5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsZwaqI68cJMs9RwHilz8wsW5kse2W9SAf17Fl2TosbKUPQnw7zZ-dXZ15t3Lxr3kMUypvY3ewhSs2KiDEcm44Oj5k-ZDUmEb7nFbllhB_9led386TA7dLuL5nOBbR1J1PtYVK9INCQVKoPm6HO9d5lcn90v_Pk2oQozQ3XicFC4AbT-D_oaWKYd3CDeMmHsl_gV04Cj1zf0u8BnjXA8XX_3EVfekF7juspsO-uriM59vRoWGox2ILsloB-Lf_pdUJYj2hAAwbbPkHlIE8665tpcMJIqblCab4xq8NLfCaJP96HUOB-MPpYOAkX7bEGJoADC3oOTmQkB9Nd9mrmw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaAGhqe5aNR9ngkBWBUXlYzp9XqWVDVMBHZhiHAbrKTcXfuPyRdXnle-MNqUWEGfFwQbda02DFObYNuNoBeWeKOGNHJOS0_NyZ6OtKyZZY8s5gY7UXP9_k0yqVacNHEq9T7R5EyeYk30A73cFY7FGFpwCeVegDBRn1Cc2gh0py8B6MMUzaL3sV8rDcv50BFfAi5tzDzquRslVsyvVYwXzGiZ47jmP80WXhjHCZqlg81IVvIZWy6PLecV-h06IhZwARf9YPSKA4JjMAYVatZDEgoiuyu-HWqIpp_oETeXQ3_eUQ60DqUmwa2Qo-2Uah25PK8rKQll5I0b0D5VSE_v0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghwZMHMRlNekuz88VOoSQvOzbk1SiWfzBMstkatdkIW9KXBhmWz1p9OzxmIRyzW2ZXkwhbiRz6XW6X_J3KBGZu120zogkTogDMn4DKzutldhkTuZlPjvVphM3KG7o3U1k2jYTde1CnTZOaehIIyPNOcjeUOS-tVS6q-PA2ak0VDmUF_BXqdhZEnaGdCtac1cLlHiGuYeKAitcNUQBfyx6-TiCkTbEEqZD9h-W410VHsH97QLftjjiXqDC3pPwtPJ8KWWwng6R8dDyStgSQkDvcjgBxnBoKb_x6UfPuWgZALvZg_4BD4yIXOqYalfcdGUv25B5HkAgr0w9HAi575xdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-AxmqQrVLRy8IP9uNbUQc_7yPHbSVBYvtJl5EN9zOM-MUzvZa6Ll2VtF5V64Xg66P-34CLpovci40fyI0u4wrFlZOIYP9Me8XI6DuPb9b3dUJprxFeXcZVud-pu4aTRpOumwJQQiEiUDpgffT4KB2XQ4ANNVzggj3MD94d9xY2MTGwH5COyf0vPKI-xNQILZ9h5XessyoGWwGYT8Y7fZiE_DpFM6dMdaJHFP_vvK3gERyez4EFBckUxfnqzR2JPI35yoR7ib-w-3yt_OhaDDkq1cLn37kB49baho_d-9rmvOuSl_OIcRcGSlwGIPoyyGgXRc6OTesvdu2yacAol4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8wIdehaobjO-g9scrXKftoHihtL8md5iDpBbNcTwTAK-wvQni1e2EpsjVbNF-56WjrZ3GG_T6cAzq1QYLD3_66TTzAHw5klE36HZQ9hQzZvvLqHt0DT-3tmktvnbWmWHkfafodQ-eUkZwGoerSXEhEba4-v7Sm-WimjEivntfiLV5Ar3mepGf9cQlj8CIfCrQLo2EKwUSXiUsm5IAeflGUeGtJTM4E5MxxhRaGpQ82cO0wuDPbrAEqPuf1pXA4o5GPQoTX4h7u622njmlHWNLC9PPhhuiRqC7zb2qrLQokgJffliPCN13utP2UrSojYQpnu95hnsnVWlxwiEPfo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYn51DowB5mE3pXsunwqDMlizARMEHwY8mmuzqyUzYskc5x-SX0XCcZcuF0Mgfpsmhqt7bxRnuiVPQmV4e0crnPF202iKRuNVr5VoXwp4jCENRcMYMseNDpXh3Kz0v3-sA0DLM-bc3oEIggxbWGINP2HNMPvBi3IRrNsjyiuSyQdfzWolQlRseTnh6Nkn3QHQ3sg-fgABXhVLy89_DHs6P6vJRF4JFWHD3JdxLRpXR4_CyKdUdMk7QzCIN-tDFvAhCGtUik8v2hCFPOsMccHyS0Yrps1b-TRTM4pfQEEjYJPa6Z1_KhSugr4vnojKok4arLfS9ceQ8AqgF6eA34dsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzB4ioJhgN-uCzmwpuSXZnyJyQ1VsdiwHCiWk7-Y2QCruOqn0RDuwWcXQBsFrGChdmCc7q0nVStQB1lWKx2KmqrECpWyh_M43jRZqqABvwluAO5fbrXQ-lPNCuGu1AQ1gnw3PmQ-_fAe8baE-aZJQpFokElAhjmVTM1bedwpqMhbZ1-QOpiX61bs5P5r-H-yV3oi5ewAWciuEPai-LdvD6NS2vj963Ti29Q8nOES_mCIRgHKNEbCgBlGWHy-j45oZ6mA3vRXITmw2aldq0WqXqI620TjvXtvp2HmNjOjINyLPKp92MzwYxZzlwZlWvuRoI5bYv6m2WeogONX792mYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UAQCS_voGLjoLNMPIzJJQqZbCOaynMhUi-vo_pd0G7O6o3dq7WvOjFvbwMBRbdg4YPByWtdEq5dbTsF4m9XDVwG7kTWHrZQzNcbAXXQ1p_PoxDTOkn4sD6jrt-05NrNHScyKhjIqxtsV08gdt0btwSLIjhcXFKnoQ4dGjh_ek_2wUNJyzs6XaA9tXIyOPfgN9ZfSkqMP1HJvFZ4hJNGuE0vL0KDgBx2oRrO62AG5SZp_7SDk86ass71BeauL8Ra23jGFsU1pyI9YpJArxfEA5-xgEh-65NVMrhlSS3r0XoCvSVNGEJWMwdre7U-l0YDargNLrljQx4y3U5dYOuYFcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=kQkrZUOm5OeS8lmX5STZYX4P0FfgkILDyS1Xc9a0bSn2nDAe3nIC0Rl1ZWpd1bC1iLvLeorgerNk7NEEXzsWOXZEGreGP0GjS9lVhYF_cNEMMHey82oMH_Xp0Vjrv_fHUC-ESD4REYvjo7pE3BVCRiBETctqE6a8-BVXI3pbFYU8n38pujggrKZHaQWbAYgPnISp3xPy25HGr-lygnCgomuhhKgxKPV0ECQAL9UPEbXf6qsaG3RXyxfcYs5x1Qy2WTOAj2IlOXdsZkEn2N_lP1hfEDxBHdkNJKHEID0TPnspXQz9cfcmvG1A3yuZW7PKunTYNSO4JN0UndXAQDDz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=kQkrZUOm5OeS8lmX5STZYX4P0FfgkILDyS1Xc9a0bSn2nDAe3nIC0Rl1ZWpd1bC1iLvLeorgerNk7NEEXzsWOXZEGreGP0GjS9lVhYF_cNEMMHey82oMH_Xp0Vjrv_fHUC-ESD4REYvjo7pE3BVCRiBETctqE6a8-BVXI3pbFYU8n38pujggrKZHaQWbAYgPnISp3xPy25HGr-lygnCgomuhhKgxKPV0ECQAL9UPEbXf6qsaG3RXyxfcYs5x1Qy2WTOAj2IlOXdsZkEn2N_lP1hfEDxBHdkNJKHEID0TPnspXQz9cfcmvG1A3yuZW7PKunTYNSO4JN0UndXAQDDz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzNHuyfWjgOzj2hbGqCQa4McelTV7MhjYT-RHrMAnzeIG1Hf6244jqwQebXi6aRg7CCf4xX4xATgIjLou7Fr-yn99lJagIyLNcVAQ-VeIAjeUQcR_caDPlVXm-JBwKs2afk7GZSl3KbaoTg1lBTGOwDj4w-jItCob5R2M6bL-6SnMtQDbUI43IHrcI6P2NPhwZTu2xjqj0lEiToWRDZO6vHpXG4UEEVL7605cJYwvetH84jmDz0F8BFdyiYTtHo1Vi00dg8iVdNR0YOt6YuNa9zTle-RK0D-exgoViubU0kyg5RWRz3S5gyfhxuPA6wC8-Nd9K8igUJ05GUDFRjA3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_gcXTU_A_55qi1ixR1M-jNex3EAGqEbroncqQ9I90HNFLME9pHTTgDzrw5yth8PCrIbU3tm5vamWovdic1FDWvVT-UEtGBgP91VS6XAqe8SisHPEHtX9lUDlhWQGQbLGKygsIiQvPCU6erAKon7HyoBHpnvc7AbXjxqYPUU4ihnZgBoi4L2UGO3W7ovFKZi7Uaxf2cul3Kb16NChcunM7nsZ3Jihs6Lmf5Q0Cx5kYrP5m9GOu4uCWf6RP8D3vzSTR_S-FvLgp5qE5S9Z63VKWPObdJPVM1vXT9xTLztrnZq84SNxlKkvyhFVg5JSBDPbvWLXzQeEe-tUyGQA0u8jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU2oWurknCCHtVcbJ3y29YY9meYJkwXWSCjBgv7-CwpXnY6gDz-r8S21SSWCE7CLoDBwRSONpsaWihJhPUFZLALzUqExC4_9gz46U1vINj3DWDHxxCnpPuFpfFYdyugCctOWC3-G-f2ruTm8qlVcMf6QvAOOQxeEAubAK4FmTpV337P0vi8CCGsz4y453q8x7Z-0yU37g_8Rre_eE2K0cNPMHK5wuYcQEU9GoMwzboc3df0mrwMp4Jk2GeuRPd-93xd2hJ6NN4wyp47oLbWMuIvV7JHB0-pDkFGaHCGWWSH1Y36-7wfc5yYLuM5WnQM7qmbcV5IRc1ciiG7xdByevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wpf0fvmMVWFAoGx-jQ4yy8BmcndlZRFqN4XGCA4YdUKTM49wENwSn-xulPbtNCoj4zSMoPKgZgQXpN2DJNvkc-gWNJnrtq8kKUE28sTpG8yrWzJMlHAfA8fAYeUG4GdKc8YHi-5-yJacvBp2xumMjahfa_FkHzYZ8qd0dTqoYfPadrukdGslioLYuS2Mug1wLPGWzLg9fB0BY775Wez5Im56sP-R6xFk-oOHb_47y4AZGeECPu8aWfh55oD1LI2m_DOH-icwWjicFZNO0hZNbsw5KZI5HIEaamGkC8mHulzDazYDmf9bGHlfJRgMJcMO-Sm16dFZEYMoQs4EVKGQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWaet9mfF7XODkzieRxYz0yYpw9IjDv1PCb8DXdKuIIBPniK3jSoJP9etShRyEqG-nwiWHWILekF4FPwKVYjkZstcijdu6WMyl79MMLA5qsmOZhnzaIQexF3hbU9l2Jw8kw1RSXOuCxbkISKShBujwnLmFfKdnVIMPBXXjadFAQ1yDkg-is8V4jutpjo3kOg_FEronTyW4gF7RyP8YewXgB_2smVJjOLi1SvhLEcsSS6OtUKnVxxm7kbLJTV-wvmTVrAUT0rQoI1qkPDXWc75t7Y-KsR3nonP8PVNIoAizG2QX1h6r5kdE24hJZdsED6Nfqwjvh9OSJph2ZoHG0Jug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5OwFsmb-H1LpglTSWgO8ZXtv8qIpP8OFKO_z_vYJXXCIZP0tdvhVEUSZPGgXaL5gHEt4ibztc_ZVwSkQS_dNClYwSyO9s1fQ3PqtuaGGzfCopMLj7N09j8vN2Q4GCqlxmNXeOyZRQLUB933nrCHQFw3hT-28mvjMhW5l0dKZyUNRWDKsMkkxxO5SxIleM3TMa-vtQpAR3VAvYsZnN59APVW46AL1Kn6cFqxpLNetsDnlZVNXqpFIxjO3XA-xSGKeZkBHVVXE_C-9ETOm1a-l8y2OZxh6w2fKhEhIkpIZFqCP32kvTbkAyqaazPrJu4SKQNWwzOQzBC1bUZPvC8YrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=HWdu1sP0t4NEyaRXH2EJeIHxbxAqZNF0aMphF1SYv-wiX6IwNMekWOlUsJjGg2b-eN4F4W1vU9mGvwVvza6GUmc-SBD4mYe0E_1qQknsX8L6i50wbAjpL2EKOMYIxLydNIkkbg1oU8pn4fV8-pl-nLFvB1rXLJTRdm0hz1FXch5wJ11IJPfMEZ2Wvlk2HlJxA8lHxeitttnxnSnTEAOdvN8OQCLZ-C_jRxCm7Tx2gAWJk1sRF2sU-7H_BbYBgf4krmTWqYC_bI82Mze4-WPMGcP6Um7JZPGvtRGAwXzcj39RCTAkX4Zg-LvGxPnWVOKJj69jL1Hrq0DaQsEDyy-lng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=HWdu1sP0t4NEyaRXH2EJeIHxbxAqZNF0aMphF1SYv-wiX6IwNMekWOlUsJjGg2b-eN4F4W1vU9mGvwVvza6GUmc-SBD4mYe0E_1qQknsX8L6i50wbAjpL2EKOMYIxLydNIkkbg1oU8pn4fV8-pl-nLFvB1rXLJTRdm0hz1FXch5wJ11IJPfMEZ2Wvlk2HlJxA8lHxeitttnxnSnTEAOdvN8OQCLZ-C_jRxCm7Tx2gAWJk1sRF2sU-7H_BbYBgf4krmTWqYC_bI82Mze4-WPMGcP6Um7JZPGvtRGAwXzcj39RCTAkX4Zg-LvGxPnWVOKJj69jL1Hrq0DaQsEDyy-lng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbjFiGx1gcSBlIATBeOcDS8LYw9x_k1VOxkWRg-rrx0renheGxWTtagzJs6jRbp4r1shRmT9hxEuCSn1vdc83fpuQok01QScbcseo-bYGGRT-gqvqa2w0rwziy6aZwYusRXac9Nlj8z3Jxb02eYouIwIsH-i6W9o0FZP6mDpg4DPbpuNiH0p-_I8TBkpTI6pWUL1wmzGkA-3wZkGN4qyzAElYcnC4EE-a9IbiMiExKsajR_wrh7j6zKJ1e02lEZd7826F1MoPgdIuKGXhmyjiLIu3heDvwiYB8onsA00vxupLJh769ZDs7JbwPz-T_5NoSeV2vmzEbPgbmg4rebPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOT4rMIb4eyUWhEXdtD1XoUSVWPw1ElA5sjXl1Z3-RQZoCjDhjhXadxrK0EfYG1GKkvg62TSxgJOw6GDU51r828uExAG0n5X92XuNl-KtMH2WHk9qYWfCsXziopFZtEf02NjRwLHuJMbKjgtoVw6xYrT2904wBWOgcyozlxAcMWCRHQ0h0rWru8k5Z-5CJ36k8rd8AF_wjro1bTkaHsnaV5eLU77PVMeO8HebOD_hipvUGx1tvEJTkVwkNpI6JFW6A_f0bDgkw0XMvrYaSMpB_rceLDTlzJSUbKpc367MQ2jk7TB9Jw3N5nUt1TRlPRhO_J8VU_Br3b_HnJo3Bz-6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJsXyMiHBg_o51fMyONdd5_-nGk_EXrXeBa5HL07uFTYp9WgmVywsjrFqzUwCvb7b09RP6_CFV2KAvYAyTi_Zi4xK4OkRNS3beMZUUyXrUfnaSLHIyFiJ2b-k1myce3gBvmLFfPgx3RjYffy4ruiyQ64oYPXfhhwB2aZbX4lWgfNZ2_Tw32k5-LOqp6qylvKdGRZJ9WXhqCsXHUqMN2fN22MdmyaYPmLFAvsPly4C6BRok6sMtknJTvmTuGZ2bkYeoi-LhkcDCcaBECdhnWiWgwninPjqgMcloJezVcVReFdcyZErSNP-MQ53iyYos5ORRgRimhjG6qX7nPmZQBsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZjPvbqaYCUTbxrKreLKCehitbuj_asSehsCUfU9uKKN0lIU5MJU8-j5V3z0X3NVEZ9RU-GkitQgXGcKAP0LcnSrIkp9OqBwqX1uHCC3rcAqe1OdnmQqAcA64_5EAwa4RMducUiVIsWmPmEO6tG9k8ASHZTXoL2GJnhZR3WiCN2O3gPwwH0xM4jxfdHz2MG8uYII_QD-0_Aj2QwbcZu_H2ARp2oHCadpkujD25Qy1N74BF3Q6SlytkWQKduCl8cQ-w4mHsDJGvvGF6HLGTHlUHUsTk8VYrQyuFpv_QID007JcoLtw34EMUwQdi0VsFzPVSsN9Ndk9-WkttROeQzr0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/embQW3zJa6I5X6_M1gQ4jc8QhdF3cyKW7DM_TULCYv0Xjt0fSbQicnGo_Qt3ymRRjmIkpNWlsEqs0mWpRe4c7Is7t1Ws2Cw93IYtJxINtxOiJ0j6w4VV9Zs3F92kgXw31PkwlPjrkCHr1gs4EJ_AF4zGSE6y5iIhXZWMCAOYeIrQHUs0-HCuvO-iYAndO88BotB5342X1OB-yii0DSms2HDsACQfn3VBFs8iJEwpCMTsyAWgkXX5Pj-6ve_mqSA6g6PCfirh-VE59XB5k9BKsGmmCBlt4yD_Llqq3T-bDUDV3Rs3ecwVGoWI2YFFdf_I_a1JvXZYNLBw29pIrp-pdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
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
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در روزهای آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBDY4VC_n-ZRyYyuNINpQUcf-12cIgc_BKkiKxi1k80GgxiT0dajdNYAvCHGMVe3HCk1J-5wcOjlNVhWWc1O9q6cmMPpM6PWFYsj_FHHs281tq6BUX5dTJWGVjhUttX_Rm76y5G_lOmrynRy1T5zlpp1Kgz5UACNNgT4C5wGaMaVZhNAjIon8fWlTLRAPkxBhnV-RUlzBRI9S8WrfXzF9EN9Lyv1T5QCwqn0VrfNzFi2o8eFrk5mgUNHEoVl46vqagfW8sDJVELHMpL6twr3W6f6V_2aPk5Puqh8y705tWEI8p_BlTYhmi8mtffD0o5e5j9USnvpOTkW10hGdNOeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0yk6t59K0VRp540fJ6K5NYTnHFtxS5Bs2JuZaMn9VEckAVK9lg9f_tN9tWZykZko5n31K9-YjhgfRqiC3J2yR8F3KH83Q7n_Fh78f20KVUNdQRwUYoy85YRLi8FWBgxJH6AffW9-ctwBcXqVfDYHzOc5y7aY9-SZyVXsdPk0GEi2PdwY2CFAtwk6_mgV0ixy8XzS_jyloS0s4nKeF5jWgt9dLky8KKLPwk0RtSk0Dn7i_g_HrjvndpMqtBxSTU48jXunPpHu7p-XsZPmWbVdktw15MJJHFnmVfSvBv5c6gMp9MAaSrLQ_dbIvstX6MnpbPPfILZvzKmhi767-92Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=t2tCsb-0qocPqiJ4zhLYz8zg3FszvzuZU7B6hJEIktSUByGC0wqP-OfRCsWozbihcJs6q3QFhmVKXM1p_wsfa4xI72dplyC2Edo30V577K_9d5CxuvK0G2Ih5Y90MYMAQbL9FPKjyjbpSb5XwriGk2xnqec3wB5GGquJHc4DopxKqsPTE1Wtd5nVpDmAatmLcmb1YrsbCOkp-A5GpvL_-8YXKdo_4CJNbm_zZ4F7NWcK7vq4hxDTx6qqmXC5skU_vC58iMN8GDakaZjuBp2Y1zw_bZ0t7e6dWV4S1UHZahNe7ylA1wuTIozeKNU4WbytFAtOHXQu5rlrDRH91F2rFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=t2tCsb-0qocPqiJ4zhLYz8zg3FszvzuZU7B6hJEIktSUByGC0wqP-OfRCsWozbihcJs6q3QFhmVKXM1p_wsfa4xI72dplyC2Edo30V577K_9d5CxuvK0G2Ih5Y90MYMAQbL9FPKjyjbpSb5XwriGk2xnqec3wB5GGquJHc4DopxKqsPTE1Wtd5nVpDmAatmLcmb1YrsbCOkp-A5GpvL_-8YXKdo_4CJNbm_zZ4F7NWcK7vq4hxDTx6qqmXC5skU_vC58iMN8GDakaZjuBp2Y1zw_bZ0t7e6dWV4S1UHZahNe7ylA1wuTIozeKNU4WbytFAtOHXQu5rlrDRH91F2rFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fzz1PxHSmYsmChltDS-vom85GcoMPbvVFJhVQv7DK7XsWFCPfQh0EUc-QFy3vVAU7mUh47HVfxmbjPB_TvkfyXwuvY5kHl8hhjNYzVI1-ehq3S-ySTaTLKYC5NzDXAtw7o8d-RSJGSNy6GGs-YeJGuMjNpllb_jIk4AK-QucMn-QPhGCJogAY41XGI8kkpfc_xJvv8SfHD3lbzlYAj38OVaQu2Ku13wvGjzX-g3Jgk5bGNIyltIJbsJ6ZFuekCo6YqmFQElJZh_pEPQMFcH2xDNtOI1dr0HNtMIcCdvsBkJW5-fqdj-Sbpe5_iuFMlZD_gL8ExS4amxhaBopjj0v1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=bFmxDHVy5yFVTd0DmArulOIGyM_ftGRSxDWxMpsnaa03kM8vULPwRH8_uvJVaUq7pKL4rMhEu7cOrEcXSQ6RioI7X76TyCU7_7O-IiiZgKwTKOKkxBgqXwvopZRqrFlVnnUk0vS2Siflb-BPA5w8ncJ6p8NfwO3DMGRn2c4aKvn10wo3n3EJTcYPNu5vWE4DzJvunTMc7-9uVYKbOdHuO2QIHrBmcNBO456ie5ukS-ISJMHqLPH_yWLpQd69gRw2STRmvHnTro5FqN99JBQoNTqEBOQkJnGyZZfCKssCisPAA3BL5YA7LaW2XLtbDKAKtpH8EhE4H66BSj0P8uvN1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=bFmxDHVy5yFVTd0DmArulOIGyM_ftGRSxDWxMpsnaa03kM8vULPwRH8_uvJVaUq7pKL4rMhEu7cOrEcXSQ6RioI7X76TyCU7_7O-IiiZgKwTKOKkxBgqXwvopZRqrFlVnnUk0vS2Siflb-BPA5w8ncJ6p8NfwO3DMGRn2c4aKvn10wo3n3EJTcYPNu5vWE4DzJvunTMc7-9uVYKbOdHuO2QIHrBmcNBO456ie5ukS-ISJMHqLPH_yWLpQd69gRw2STRmvHnTro5FqN99JBQoNTqEBOQkJnGyZZfCKssCisPAA3BL5YA7LaW2XLtbDKAKtpH8EhE4H66BSj0P8uvN1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGmfBmvw6KBEx0ScGxpQ4fK6ZVf1Fr2Mh0CwqQcXOxrt3w0nrWQDm9t_aEMBheo2LO9Ql2cOHg341JxyJX491pzzyf21CalivvUxwDz-JDPBcpRwP7yfo1mM78hg9tRih-wu1y_ipIDdwTxNrdnQP4SrJLjKIjDh-mQTkch2-CyzdJtAF4EUpK-B1yszzPX2Y9V_zZZY3BE57PZStvcDLOQsM6W1LB2ZgU0iUPMPFlakL9KRwjOOHu9Lad2oqyNZEa9_Rt4FvKBTAn3m3kk0H7czhRliX4DatSAS_6fqgRKFmNeHwOOuqzB0aJlhGVj5eAPOcbVDdZli2jq3WeELhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl7kc0lw0dmNPt3LDwRu7vwm8wvipl3sYqp5alMbpx7ajXbrbiHTIDOd8auje00ANARvOE0uMdGOf6KmU_0md1wt3hLojT1wWzakMusDOT7sKarfP3YLKJiHUs1XzbcGJqHA6YSTuOpxlqV7Da_f3Csmm0_br5BRILxKkDcowB4tlSnkqZKVQtFmDrWn2r-VvoBoBA4ZOmlwfFT_WlO23Xd6Ar_3PTrS67oDZyvtnuvIyooD6Vq2WB7_XRIwUNkid-nJnmIG1OVS4Oou66VCmGRDRnaGA9S5shK9cNIOdwDNtbz89A8Hrr2Ue1IXkZRoGUKXG9V7_KqW611gQ3nI9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gqp-BK0OM7w_4Lm1mBNueCM1BSS6jnOOZarSqzJ5ya_rykQCcd_YG3ZBT9lWVTLDLlbBOdk3GnX931v42fv4SUhkjCWcz4HyEo51itGHfpnaCA0ze9X1T0LDoWflpy2A1oJrhECX5OOvi3PzusybFGr5dtSR-30oKvOBgbQ2sHbrwf1RF9q0XDma130aT0g9nYu7jiLJ0kI9rQUaWGYE0tyHdEp48NuAhT7tanJuwsIXt-8BUvKGngmBg067mLa5epKnifUIEj2fc_zcN4M-xRciF_nH1mjuevMMVYXKP9GTd5SAdxgHLuHPAFK3KUJoh7XcjpUsK-rKrpKLNlpD3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcrneQgvXOCtWEkTfHw-M-vovV6U41FdJYdWoGVnSajEZsfRkNkYHYnjFRcaR6PwZrk7_0w00pzJPvJO4k3vjFHe6jYu9fgyrxfGOtM8q7XcELXE9V2Dsi0TtGKIahkNPzx97I2lOkBST572AOZb0yCLopBlZ9K7bMtHjX7wYVWI2YJNde1TO4utqPLBJXxoql2OG8qTgKDhMqincAel3lTcuCgZl4k__GVqu70y5v1_enTJqv-bRxrG35jlpTghfUR2_W4gGGVsarYygNRjEo_1S5ARt2vXnIo_fAF9G8951mjVGqP6CsaPN0UxesyYUZomNvGR7LQ-AENUTrvG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWnF0dg0SYzhdkasAwsoVdL0hJeEmwU8xjqsNtbm8QlMuOVkVGsKO7ceMh1Hn5GQlzvYE0Mj6TqG8gJtStsFByCtxXwQ9JrIOf3lZ-yvLTx2UeYqZQHGUuDbGcvCYgEbqWHyir8d8Vtu5rQ_z5xowhYJ_srzp4v9wmbiW2LTa_PrbcY0bNChJLmLOX9JkmJN8CR2CP1TzH6d_1Sq4_7_JbDOhT6x-VTuIUNjeODDufuWGP_nc-hLN7BXe-XIK7i_kMYjMt3GG0GeABDfEfsLJUophW66JMmRWkztU-iCptaCTziB2G9sXCZWMZ5OhUMNMDlBspVXe2XwrxhlqE_EhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhKyl5vzUVePaqCj3wg4to6-0-9ZcTOrHmKAdB4j-xG-FkzzXDD9fk6tSHfe8RUIrS6UmXuUYrubTXJftMZFLWTlICIn0C1-bprNvTWIIjTp7mzNxgDUsTNZC-xoBI66Z-9PVHlRPlY9N-rSG2IJpOrxmXzgBIdoER3iOgwfS5pFqoAPLDVFNgk5b6nHJpbNetpK3u8eVMNGfLfIhE_hzw8XJs1TLxAqgn2SizHIpfwNZmR4cV38GFyD4gOwWxLewmJnlqMmnozkVDMtefvPXAJnVwpwtxeKCJwDX_wbT7qrSstWBsNiivq8wvJciQgLbR9g0gKNpPbMNIBb4lD9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raIYrWuRkHCNvR83EXyAf1e6EDNlNygOmzVVbuMlat5XqK0G5Jos5DzOqmF5wdDkUuTAi31RCKlrcKE-mnD2yd2JdfOLHJxC6anRGbSdeltvtN2R-cSaLeO4fSR22vjT0ocYYT_kBA0izSJ3enBp4SziBDMKxIJ6bmI69eQoh9rdUyuqyNxDiev0qAiPPkgs7d1ckAv1rjGKBNv3xsOYjUPzOA0_tXweCzwkgwIUbP_4Rjkn3XQsww9j_dv_Lji2bdYtbaah04QFrlyBM6DETU4GtFVK6zdqiEoiOamSIr2qNY-_6Slmqw9bmynhE_xwhHVDapF6qeCzQhujFM7tLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEFHYxGiQ4QUOf5p3TIYIlvIszmhVRlFidZg5Lzo3GgpO1LVs_MKBxjecSxxdz9ClB6IMrcmJOt-9JJxGWfiCQ-JPNiLn30uDebgMQNubh8h3GPNap59om-njHuDGBcMUPotXS2Qb6OV4wOPTKNGqESGThgHu5LYms4xuLoaMsoZ7byqqdeHZ7FLsHPfvRG3o5jOcElwDPXG62Q5ruAR-RFLwjoP7kDPQnM-kvgPzpriAP7ZvT0n-7RJmVOsb3Uf0FGn2PjSeWPQ09wnRAm6G3XlWtVlKWTDhScPRlcXyUDagCTEKwiz7JcpCAe3fh7pRPapbOfyuG76krOEbvplcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=Mi-pTYxEXzFx6NeKMWRlXF6DLne9s0jST47Ox6MB8c59uKQp6gAQ1gKAeupRuArD-5y96rOKrwhfZ-aVwya65-9vFt3ELptzOYPsSaV8hEiC-mZ-g7w_5nZIMRk2L6sqs_s7N_kJlSk7fepQ_I7PrNnhr2mGAd4W7ieMBeAtI1rfCQ-OoDs5-Bzz_JCweewyRV2s65M6sxYDW8JH5PoO7Tun804QlDVR7D-i8qgwFZq-cECQbTOtOMvtQeR3m145dKONcV_Ic8fuGP6wghicHUYnZ2Z8TxpdPzut9XjbevqDM8143ZoLWw3n4dZCSHllxK7uA0_6l-sz73laFhY5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=Mi-pTYxEXzFx6NeKMWRlXF6DLne9s0jST47Ox6MB8c59uKQp6gAQ1gKAeupRuArD-5y96rOKrwhfZ-aVwya65-9vFt3ELptzOYPsSaV8hEiC-mZ-g7w_5nZIMRk2L6sqs_s7N_kJlSk7fepQ_I7PrNnhr2mGAd4W7ieMBeAtI1rfCQ-OoDs5-Bzz_JCweewyRV2s65M6sxYDW8JH5PoO7Tun804QlDVR7D-i8qgwFZq-cECQbTOtOMvtQeR3m145dKONcV_Ic8fuGP6wghicHUYnZ2Z8TxpdPzut9XjbevqDM8143ZoLWw3n4dZCSHllxK7uA0_6l-sz73laFhY5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXEbytqfb10yVxYzAit184lgstUhZethxtCMXgOCVPVoVTAchH1bVBDnDRjoJeET_53CwtQLumlj5wuvepdVepWovko3uWdgfR94dDr1G39lenRrzfpBIIzQnJ0WyNBucEJvW1VGJoTgXYqzKYWDkVMk7P9MUmp0xvN8lVyUK30zIXv-xFUMCpawpMsIjs8T1sapcM-mN0vW5_j4aINC2-gH3g47v4nGktIkJAW5YBJgHvZau-D5gLMXAYggxWjgS6wiJ0omE7GhvUksBOuRaPOwpP08vvC1t6V25b_S71FKK3ZrS7uwAw6bUoZjJRQXOdon-7xmJWi_xcg12A-hJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQUcfGZ8b0GJUT5fkDFPCWGdqjtmm3yfgDdOQca0dHz9r_Op37HoTwKEfeafo8MWxMPfpoec2m3S6R3pTx0Ql4QsZsTlA6-e6Fei3U8Dn7qzdAXtjqXZxE1wKoVRA8PsftpZ6ll5sFcz_gbt8_Boefgh2peKEQP0u-smTHWhnEthvQ4lj5zxVm0qfonpj2ZgK7jdpVpkmgkcTqHS51bTLsJo_gGyy_z47mZXegCl7IPMCae_QWPFoYPX-_P9arLD1EyE1jcf1zSV0w7ST9VuhhYO_ZYh7Idad5R7TQxt5ypEabp5gVMZDgJgUo6M5fx7Ifx2_VvtII3-smGi1YW7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVZUc1m51S3gGds9MwAsoHbQ3D5T6vec_pYMtMwGMSSdKs5LGDRuj4VWHm8DFA1UTnMhGZIR6NcvuMm_6_hWVx094LSF0X8U7_uusBd2yQSHmtx2zKZKX-J_5DmRu0qTw7Xam2UyUVAYVzOJFe8UG_Ty51P_KMMlKzH6OUZWCFh6L0Z8pqI3HHpow1ZDpzk9MCImqEBjvBu_DLqT9OcC8EYblGjiO_AguLWZdwD8Y3OP1qWmOYK4ehV9FfxJeSlPrPVBsVTrAn-Xru8QBTnNaNxq1ScaD8Ao4L6YyRUEbqzvxEe5F3v2fik3K3P52cF9Cbaj4AusMsrNi3pPoApeeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EbFtQkAu48h2lndGgInHjv9LWbX73IIlb6tqVUOanmt5uYq9PcwxWp2pzhK7t5rH4afjONpNTY7RELClIFJtfGTdy25kesC9szONoqUSpqTRMV8Lcl66kHIR7bGbppE5OBpJdXmhzRxbT2zSadQkw7PwismEAGR32sgD6lei7IzO7h4tzK3mfnHABObQZZ6n390ZsA6x9Ef8vDEX662i1U2pXufh5rKt124nW3gQ3caTR0dgqKeFFairsZTgez_3VYaxU4Vc-BJYwB8LZItOFEi8tPCe0e93lu28hPxO5RyAYnECorvkJsJFy8YixKEerA9gihvUFaDKm-BeOpw5rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=fB3FHizWyweNTNB5dU68xyjBLQ8ytOE33OdCpAZbPv45lMvYL13vGWUvx1ekNpj0vp672UN-jn6WN-BOZIj6ZcC7UYL6WwX09tATlJr9TAtVFDXyEl9Yew7ekP_TXTPUCImvV89w4hoGxCoItOf3j0qlZCIDQMmV-xtRnv_sN_Co-3PAUzdHnO6AGrX-lFCxwqYgTKTvahfCMjOuTj3_ceuvkI7XDZTjac5AeJ3RDr0amDTf5i1O7uZt_4uPMKmWXATkQDcrQwitOldIL6GU670bUuDQcqjwoteDU3LjoQYOtFjkdteUSvo7sVlkMUDsGOf1YuTPet8uJdA7BYunaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=fB3FHizWyweNTNB5dU68xyjBLQ8ytOE33OdCpAZbPv45lMvYL13vGWUvx1ekNpj0vp672UN-jn6WN-BOZIj6ZcC7UYL6WwX09tATlJr9TAtVFDXyEl9Yew7ekP_TXTPUCImvV89w4hoGxCoItOf3j0qlZCIDQMmV-xtRnv_sN_Co-3PAUzdHnO6AGrX-lFCxwqYgTKTvahfCMjOuTj3_ceuvkI7XDZTjac5AeJ3RDr0amDTf5i1O7uZt_4uPMKmWXATkQDcrQwitOldIL6GU670bUuDQcqjwoteDU3LjoQYOtFjkdteUSvo7sVlkMUDsGOf1YuTPet8uJdA7BYunaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8C0NnL3Y3vuoflTKPZDSuqyXD70G7sbhTsfDm33MfbebijLs3dXXxJkUSECIBIf139spz2tB_CMcrsj1UUnzvylh79JX3PHBGIQAQ4AMdB9TQp82RHP9g1P7jAds3NvtsJ6YZuNN0Kh-JGFfqoS-9VARxo81lkNkOsdAEhN8eCycCUCgAmgZG8rD1wk7U0BER7XpOC2E93Ict-H2PGTt4_ak6fobtTYemj12DeYXsLZTdjttHQaUy9t6M3PAXx_r_eG6Q1QxWGUuyE-976qFsTI-17roFq8z0PggeR9ak7_d7i91OPDIm3QXh6UWDVjcZIyYG7mKWOtTt7qRFGLmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOwO1D70Ifn6OhzAUdckbcTjd9qT67-42jWVuKGtVgGU6EGtZGBhOThJJMFdUHMuKLdq6gE42i1xVMc8YsVVd0GR69cZ7GZOTGlX8lDtKCdNQCE98XG3ScDnqSEWrCCs2k1Mgj3ErBq7_pgD8DWCRh8RiSxmRGFTT6FeeQkNV29iqLecQlcgpcNuXVFdHW16-7hoWPtkpqz21URKpoy24W8D3boSqkPqx7EgtevGHpsLkddo0x7ROvQeCAcawqY1vcVmVmJMM0oGjoOSkh0ozQByGy5bvwoGCohusBwwB1pf4EZ8xsjRnvqcY6pki5FHCzkJ7MVKpItHYdWfdNdAQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElE8kbh2RbY917MeOCUtUz70ToZe0ODBtPVNjVBqk1y7PxySyngOlq9W6zyGYhDAc8tYAuUmkFaeknmjQsSqaCncZngicm5wEp4wfl6naS0CEjxlKeuCaMYeeV42JoqcHmzvCWYdk4xicKj1K_sh0FCTLms2SCGkvCGvwLjfOnpez0_xlX2FtzgdMkcy2jmQx5Eg6jiSFOaCdZHdfkJ-v8dywYJYFAzuhqBa3PoVCH4EkpLsmatbuSRwdSjahrUOPwM_yJsMi6MdN0mPUIbKrS20MKo8js7eX9zKfCsgaJpynnZe4sml-Bq9VlvufvKbw24bros8x4FNugooXVvsJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ-Ng0P6shSirzyUBS-6l0sldd0ALVWk9R105QPIc2IrJ6lwpxJ33jYujO0VDVMgP9xcoQ2d_0o8wG-SKKc2A15ExotsIlmzmgGLJ0PuK9uumKwrc6mfbKnch8w0VFHIO8CFK-L5X7SMUMj2sb3Vz6G-PdEvhAoPgG9Z7biCsCnjyZvebYM2kkqVfWw9cGAZPXwFl6F995C1BWpVkgx-KAwS3IIf5HCWBWvRmFtR6dc9RnPqAJJv9fAw6QDytllMI3RbzqlfZf931L0-QA9JB2Mb-QqLJH0gMn2ObyhSCPl_W3LIYrdkP0ebY53v5m_qcSCfggSMHxuW1WLx7yboHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZ5dMdr44OQLlQskgJrcF-eJawwABxp4eBsnS54SnRWfajpKqkkw7ctQZ41qxyRa4EggO_-0wli9bjKhyYKQEsDnjTNq_00kSCBz-6hLPsz1-dFjC9K-zycnSJ8jUx1bI51uEkK8BqVeMIaxLi4LxmtPX7tVa0OwCmQ1XPyb6R8AO5fgKhohwdJaY_LWUVh4mSwQSbTGxlrEWMGeDnWNy4X4U9gDR1QcDf7xdo8LpbtjjjYqDzmbaRtoqTEQMyo7b1g770FuFbogNSeHWCS2_URCNebFSYAQkGCbw-HjRyMBtQEZlVFD8vP67AznrL_H9A0udstYEPt0xT52Kf8iAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8S1NXtuc87rJ1Ed5AKUw4RfkOfJoJWzATZJh-6360tj3gDxnq9vQgZ7Fk7cW-wb6Sof8VD7NygObS1RU-iT86X4LkGtcuDrlY1CzajWofQP9oSN5REw_cr4Y9oJR04ss7azovY9kr__OWC5hyZxa8rugSoMxUPuZQKhBaT8qek-IAPS6SGrxAVg1oVpQvWi6brO9q3fVb-YFtLZOV_ef9OVg4e2hvbhs2j4BHL5-od_jjXluyAe6uYrpKIKiJHlBg-CDC4N57UbptM74U5EKhbov1OUuF4nfvWZgJkrIviz0yTn_wNjme7CIzO__V70JH1_ESUeUprqaUEyspfASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=DTEiA6UH3HfSflNJvKpNLOiEGQSiZh33oMhL505EYlodlcAtuhI1nxyyewaKYqndzfwzZjUkrREsm8za9FOS42qRKidYkabyssmqBUYu58A8cUqCczT1dNWGu8CxHsehMAnnd3uYRaPWmt5HJv8u5oXWQ_1jd2YPP9bP5RZeG56JN7MnL3defx3Q2E0K4ZGnKnKCMLUEJS2l91C-1-DJZQ0Er79k6g5nh-QJHj96tgkSdWQDbpoccm8wLIqBNFoHZf_RpR36mj9nIuIFqlrgychr5IKJ6OagzxeQKCy79QrPJijP4M_utL1JMaVmpci9cK1tJnl6tKceKOrpTG1MQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=DTEiA6UH3HfSflNJvKpNLOiEGQSiZh33oMhL505EYlodlcAtuhI1nxyyewaKYqndzfwzZjUkrREsm8za9FOS42qRKidYkabyssmqBUYu58A8cUqCczT1dNWGu8CxHsehMAnnd3uYRaPWmt5HJv8u5oXWQ_1jd2YPP9bP5RZeG56JN7MnL3defx3Q2E0K4ZGnKnKCMLUEJS2l91C-1-DJZQ0Er79k6g5nh-QJHj96tgkSdWQDbpoccm8wLIqBNFoHZf_RpR36mj9nIuIFqlrgychr5IKJ6OagzxeQKCy79QrPJijP4M_utL1JMaVmpci9cK1tJnl6tKceKOrpTG1MQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎮
ویدیو مقایسه جذاب GTA 6 با GTA 5؛ جهش خیره‌کننده گرافیک و گیم‌پلی بعد از ۱۳ سال
با نمایش گیم‌پلی بازی موردانتظار
GTA 6
، مقایسه‌های فنی میان این نسخه و بازی محبوب GTA 5 نشان‌دهنده یک ارتقای نسلی و عمیق در استانداردهای بازی‌های جهان‌باز راک‌استار است.
🔹
جهش چشمگیر گرافیک و جزئیات بصری:
بهبود محسوس در طراحی چهره، فیزیک و انیمیشن موی کاراکترها، سیستم نورپردازی پیشرفته، ارتقای کیفیت بافت‌ها (Textures) و ارائه پوشش گیاهی و محیط‌های شهری فوق‌العاده زنده و واقع‌گرایانه.
🔹
انیمیشن‌های طبیعی و گیم‌پلی واقع‌گرایانه:
طبیعی‌تر شدن فیزیک حرکات شخصیت‌ها و تعریف استانداردی نوین در زمینه تعامل با محیط، اکوسیستم شهری و واکنش‌های هوش مصنوعی NPCها (شخصیت‌های غیرقابل‌بازی).
🔹
پلتفرم‌های مقصد و قیمت‌گذاری:
نسخه استاندارد با قیمت ۸۰ دلار و نسخه آلتیمیت با قیمت ۱۰۰ دلار در دسترس پیش‌خرید قرار دارند.
📅
تاریخ انتشار رسمی:
۱۹ نوامبر ۲۰۲۶ (۲۸ آبان ۱۴۰۵)
برای کنسول‌های پلی‌استیشن ۵، ایکس‌باکس سری ایکس و ایکس‌باکس سری اس. /منبع:sargarme
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecX0TjOYI0zu1jKkK3GRdpryCtXt9323iL4UbH7ZkpYJ6Z0h8boqgXsf3XUZ_ZFHFenBuzXBBgzj__NEJMnby77tcVopXTvaSlRDwFw7SKs_6p1X8YQEXDkuj84XAUfi5_QKF6FB6yKxcRRuVKP68AOse6ciHSWypEHFCEJl1xRdr8rSjSu6KBKPRX3_3JGId2MJ-Sb3KrNmkPxcaAIAUaI0-yM4yWx50eMRv3A2OgmvcIk_5CHhLXaCN9LMO8Evy1uFtBub4-jycWrVF3IqBfYaY7NXoLU32ICAYGchjsDxpbEQhkmOfrH13r51dcyE9mnIjSPAUut4xPuer8s2Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی PingTunnel VPN Client؛ کلاینت ویندوز برای پروتکل ICMP
پروژه
PingTunnel-VPN-Client
یک کلاینت مدرن تحت ویندوز (WPF) است که با ترکیب
pingtunnel
،
tun2socks
و آداپتور
Wintun
، امکان عبور دادن کل ترافیک سیستم از بستر پکت‌های ICMP (پینگ) را فراهم می‌کند.
🔹
مانیتورینگ و نمایش زنده ترافیک:
نمایش لحظه‌ای سرعت دانلود و آپلود تانل به همراه مصرف کارت شبکه فیزیکی و سیستم لایو لاگ (Live Logs).
🔹
امنیت DNS و بهینه‌سازی ترافیک:
مجهز به فورواردر و کش داخلی DNS جهت جلوگیری از نشت DNS (DNS Leak Protection) و مسدودسازی UDP روی اینترفیس TUN جهت جلوگیری از خطاهای ناشی از ترافیک QUIC.
🔹
پایش سلامت و اتصال پایدار:
بررسی مداوم تاخیر (Latency) با قابلیت ری‌استارت خودکار در صورت افت کیفیت، به همراه سیستم بازیابی پس از کرش و پاک‌سازی رول‌های فایروال.
🔹
قابلیت Split-Tunneling:
امکان مستثنی‌کردن ساب‌نت‌ها و رنج‌های آی‌پی مشخص جهت عبور مستقیم ترافیک بدون رفتن به داخل تانل.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUczQ2CcS2ht4ullI0d4flwllYLyeVD-aMyw8Vsn4rZSEashqxBT0yQCAbf20M1EEfDP_zESkoqon25SzDlA3giZp_NiaYa9ibmAG43L3yIPOsCWKON4qNIsvOk-NDJ5zupFxHJJhdafYk4bnhCp7M5mTtBxh701UASocFuZmiSJkp8vK75RMlq_H3Z4fWSIZRvnMZDGDvW2aEsrqfZq4Qujpz2IPW_GKS9W4Lf-QPZzZ1d_d0IgzvvL-76227QIXgWZEhE23pHdLtrCW1iLUiUWZdBNNJjFmBRMDxYFBhQeaAkM3M2GORKdc6DixrHGejTSIf-cN-6MzudHDD-vbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مقایسه WiFi 6 در برابر WiFi 7؛ کدام نسل در سال ۲۰۲۶ ارزش خرید دارد؟
با گسترش روترهای
وای‌فای ۷
انتخاب میان خرید یک روتر جدید نسل ۷ یا یک مدل مقرون‌به‌صرفه نسل ۶ به یکی از دغدغه‌های اصلی کاربران شبکه تبدیل شده است.
⚙️
تفاوت‌ها و مزایای اصلی WiFi 7
:
🔹
پشتیبانی از فناوری (Multi-Link Operation):
ارسال و دریافت همزمان داده‌ها روی سه باند ۲.۴، ۵ و ۶ گیگاهرتز که پایداری ارتباط و سرعت را به‌ویژه در محیط‌های شلوغ به اوج می‌رساند.
🔹
افزایش پهنای باند کانال تا ۳۲۰ مگاهرتز:
دو برابر پهنای‌باند WiFi 6E که برای استریم محتوای 4K/8K و کاهش تاخیر ایده‌آل است (در مدل‌های پیشرفته سه‌بانده).
🔹
سرعت تئوری و برد بالاتر
و
سازگاری کامل با نسل‌های قبلی
دستگاه‌ها و تجهیزات قدیمی.
🤔
آیا خرید WiFi 6 هنوز منطقی است؟
🔹
بخش زیادی از لپ‌تاپ‌ها و گوشی‌های فعلی هنوز از پهنای‌باند ۳۲۰ مگاهرتزی یا سه باند همزمان پشتیبانی نمی‌کنند.
🔹
برای کاربردهای روزمره، استریم و سرعت‌های معمول اینترنت، یک روتر باکیفیت WiFi 6 کافیه./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtzfqMLl-B0g_Zg4ASRqqByniBeGyR-YHtftgzcC5cNb28ogGds0YKHy3tOMfasYqCIx1eOMgyGMD4CSkAKC2onG812KysLople9OapP1hRC6A0VEl1GgagEfYzBDUjgu8pCfwwAJktjqbXGBPIB9kLNQ1ZkYha1rFWffJDpXkNDgqfXSkyDLfTNUXVHFB7lEeiok1EBbecEmrNfH4rKzWNc5TL28jjtdeWOf7KDTUiFzoc1iCYtVY6gtQJp8t8MItbRkX4Ai2c4sjeV7qLYXNUAj8-W6B-7jQvzSgbG8HJWV3rZf24Siz-xqzRagFq6Hy_DkWSamnif9ESV9PhkVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
گوگل در حال آزمایش هوش مصنوعی Gemini 3.8 Flash
بر اساس گزارش‌های فاش‌شده، شرکت گوگل فاز آزمایش داخلی نسخه پیش‌نمایش مدل جدید
Gemini 3.8 Flash Preview
را روی پلتفرم کدنویسی اختصاصی خود موسوم به
Jetski
کلید زده است؛ اقدامی که از احتمال انتشار عمومی آن در آینده بسیار نزدیک خبر می‌دهد.
🔹
پیشرفت چشمگیر نسبت به نسل قبل:
طبق ارزیابی‌های اولیه کارکنان، نسخه ۳.۸ فلش عملکردی به‌مراتب بهتر و ملموس‌تر نسبت به ۳.۷ فلش در سناریوهای مختلف ارائه می‌دهد.
🔹
تمرکز ویژه روی مدل‌های اقتصادی و پرسرعت (Flash):
در حالی که مدل‌های سنگین پرو در دست توسعه هستند، گوگل تمرکز اصلی خود را روی بهینه‌سازی مدل‌های ارزان، سبک و پرسرعت سری فلش برای کدنویسی و توسعه دستیارهای هوشمند (Agents) گذاشته است.
🔹
سرعت سرسام‌آور چرخه انتشار:
پس از عرضه نسخه ۳.۶ در اوایل تابستان و معرفی نسخه ۳.۷ تنها با فاصله ۳ هفته، اکنون نسخه ۳.۸ وارد فاز تست شده است.
🔹
رؤیت در بنچمارک‌های جهانی:
شواهد نشان می‌دهد که ردپای تست‌های آزمایشی این مدل به‌تازگی در وب‌سایت معتبر ارزیابی هوش مصنوعی
Arena AI
نیز مشاهده شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6CPOWwz_XdNjcALmyUovsH8owikH-5vpsdATLkg7OrIc54WmX63lTVUCOrvEWqd8XCr5HmJhRwrgX7a77THcTU1J3gjCDbX6opKvl2OaxyWPaAc267WeHdw80FFGTj6bKLfrdOLmMk1oNQ207Q4lGkMpBVYIs6_1U7n4FoG3ru5-TjJ8yAyhyB1rZr152H_XGzBJCv51JPZRLfAf7jcj7tc4iULvyoAYqhAF5_pFnhXHzKsZ8kiMifNGdAT4wen9dL-gVIclebRrAa_VGxFHrX2Tf_3Ez3J6bVPNcArZSJKaczELSmAF2MtXf_uURV0x_J_wEmy9thT1tOInaLhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pEUzA9GF_-rivs7mrZA4aOJUBfFKKCrMRqxav10NpdfBB3jwjJaJ4OQVzoT5wxSlHoHw0N8nFrZXNf02dprxXIEbffXaRcN0li9di6UK39MCkFDjqtkfkKJCMa8UbYVrwt8knWT8leUkxnauR2OJsTlf8weG4gTdW3rM7aWkwlc3kH0In1d_Dyu1ZOYQSnkHiAiUVULOu2XvACYkAP8klRqSYOeotzz2lYH2zkA1ZXalIuqGFBHyrWIbJX-mHkKmtrxgR-jqxdNtRDQwK107FG8kjPFEdIDC4mccDFi4LPCxrvSHcMb2V5mEWH6Nl2ZvaPmn4ZuyeSGxvfbFS0N3gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
فناوری DLSS 5 انویدیا پیش از عرضه رسمی لو رفت
تصاویر فاش‌شده از نسخه آزمایشی و اولیه
DLSS 5
انویدیا روی بازی‌های کامپیوتری نشان می‌دهد که این فناوری رندر عصبی هنوز تا رسیدن به استانداردهای مطلوب فاصله زیادی دارد.
🔹
تغییر رویکرد در آپ‌اسکیل:
برخلاف نسل‌های پیشین که تمرکز روی افزایش شفافیت تصویر بود، DLSS 5 با بازتولید هوش مصنوعی تلاش می‌کند متریال‌ها و نورپردازی را بازسازی و فوتورئالیستی کند.
🔹
نتایج عجیب و غیرطبیعی روی چهره‌ها:
در تست‌های اولیه روی کاراکترها چهره شخصیت‌ها دستخوش تغییرات سنی نامتعارف شده و ترکیب این چهره‌های تغییریافته با انیمیشن‌های حرکتی ثابت بازی، حس غیرطبیعی و ناهماهنگی ایجاد کرده است.
🔹
افت FPS:
فعال‌سازی قابلیت رندر عصبی در بازی Control روی کارت گرافیک
RTX 5070 Ti
در رزولوشن 4K، فریم‌ریت را از
۷۱ فریم‌برثانیه به ۳۵ فریم‌برثانیه
کاهش داده است.
🔹
نسخه رسمی DLSS 5 برای پاییز برنامه‌ریزی شده و باید دید انویدیا تا چه حد می‌تواند با بهینه‌سازی نسخه نهایی، مشکلات افت پرفورمنس و رندر غیرواقعی را برطرف کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIIR5gmrwoiVGe0r26Nl1zU3RMritNwgtCp72_SHuDv3b5pxfuCLDPlkbSiEXNbMB6jg74SC1HYpe3zixRLL75npfYbkid1fdr0Gu7jumb58NsespOceue70NQvubZr1BQ0GJSs8TMUuj2XjshQ4FLC_eEZWF1oh6fzAvcrzZxxwO2C7OmwY6nkfxUuqhcQv-7dziXVsmeKcg-xHAUBpOWsFs_AxpGtIfASrohgPMlBDLPEzbMjT_Lm9IZssNao-m0uRDUlu3yPXmEdTRi5CcYoilj7kbd072gvDJ8ctm-HT2Fsft-1BSeGrzxi6LxCmh2Vf75WuCEBd256kTG523Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
توقف کامل آزمون زبان دولینگو (DET) برای تمام دارندگان مدارک ایرانی از اول سپتامبر
بر اساس اعلام رسمی پلتفرم
Duolingo English Test
، از تاریخ
۱ سپتامبر ۲۰۲۶ (۱۰ شهریور)
، دسترسی به این آزمون برای تمام متقاضیان داخل ایران و همچنین افراد دارای مدارک هویتی ایرانی متوقف خواهد شد.
⚙️
نکات و جزئیات مهم این تصمیم:
🔹
محدودیت فراتر از موقعیت جغرافیایی:
این تصمیم صرفاً مسدودسازی IP یا موقعیت مکانی ایران نیست؛ بلکه تمام افراد دارای مدارک هویتی و پاسپورت ایرانی (حتی در صورت سکونت در خارج از کشور) امکان احراز هویت و شرکت در آزمون را نخواهند داشت.
🔹
تاثیر بر مهاجرت تحصیلی و اپلای:
با توجه به پذیرش مدرک دولینگو در بسیاری از دانشگاه‌های معتبر بین‌المللی، این تصمیم فرآیند اپلای متقاضیان ایرانی را دچار چالش جدی می‌کند.
🔹
پیشنهاد به متقاضیان:
متقاضیان ادامه تحصیل باید پیش از هرگونه اقدام، فهرست مدارک زبان مورد تایید دانشگاه مقصد را بازبینی کرده و آزمون‌های جایگزین (مانند آیلتس یا تافل) را در برنامه خود قرار دهند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjlJ7rlnIoFxFO-HtsZDd1efs2ct_3YPij6AxxaSYu7Mwbjkj3tg5728eualGpwPo6yR291rZ0mbIg4__7x_bktbW92--66L1NdN3KZMXJLgMTTI-VSv3-oHx6tzFNfpQo88r5Jl2oVV5ZCItYVRWY8GrGNWZxgerSSPezMhWxMKcwOD2qnv94ndfxDNSC9DhgWB6QVpBhbGZ1N_nugdR1xR9YBsY-_luyNfRLC2Nx0l1qLRXwyb2iOUXxgLVmUCXwC7LUbRlPUpNhC2srKLheJG5mM_fKEHj7CuqHgDBGuRohka6JqUN8cYiwQSNesaJuB_EAdygTsLSF9LBv3JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل مدیریت نمایندگی و ادمین برای 3X-UI
پروژه
x-ui-reseller-panel
یک واسط تحت وب مدرن است که به مالکان سرور اجازه می‌دهد بدون دادن دسترسی مستقیم به پنل اصلی، دسترسی‌های مدیریت‌شده و تفکیک‌شده به نمایندگان بدهند.
🔻
امکانات اختصاصی ادمین:
🔹
ایجاد، ویرایش و حذف اکانت‌های نماینده
🔹
تخصیص سقف ترافیک اختصاصی برای هر نماینده
🔹
محدودسازی دسترسی هر نماینده به اینباندهای مشخص
🔹
مانیتورینگ کاربران آنلاین و آمار مصرف ترافیک زنده
🔹
پشتیبان‌گیری از دیتابیس پنل و پشتیبانی از تم تاریک و روشن
🔻
امکانات پنل نماینده
:
🔹
صفحه ورود مستقل برای هر نماینده
🔹
ساخت، ویرایش، حذف کاربر و ریست حجم مصرفی
🔹
باطل کردن لینک اشتراک (Revoke Subscription)
🔹
مشاهده کاربران آنلاین و حجم باقی‌مانده
🔹
همگام‌سازی خودکار ترافیک با پنل اصلی X-UI
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljs-tF-oVfZpcfmYPZlzRpJq_9lMcnlUUy8igEaV3tfufWLkUkJ19jG-y8I_UblqXabVQv7airW4tuoxRSJ4xmSL1ir37NK5ou7UTXbbfznVnLQmy610NhdF_-ewObbfjry-gG-AqOtoHbymkokC09KDgDS_vK3kXtIi5Laf_jIsg5dtugMyjo1TnoceqUPfmjjlDZ67KloXzMwFgWmE9k-qbeo5CERrwmhD4d-IU5TKV1YF3hmKy1b3u4K6oh2dnZ2UYBlzhSaXeOqLRq-XxAyHbnJ-ABRn0G4-Zf3mw5smO9sHaJsn0T-eFvMALpC47_5lYKU4kc62S9JW-T1Xgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات فروش خودکار کانفیگ تلگرام (جایگزین ربات میرزا) + آموزش راه‌اندازی
🔹
اگه دنبال یک راه بی‌دردسر برای اتوماتیک کردن فروشتون هستید، این ویدیو دقیقاً همون چیزیه که بهش نیاز دارید. تو این آموزش یک ربات تلگرامی فوق‌العاده رو بررسی می‌کنیم که تمام مراحل تحویل و مدیریت رو براتون به صورت خودکار انجام میده و از تمام پنل ها پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#ربات
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idxHCHA9sKp-HV4ChyjSAejSCGPadx7dHw40LZKjikArVdEvj0DJ6B6Y29yniwjkycWxXqy3UW4uFiNBvT2z-1io4xB676U1cQWGln9G_xt6CDQM4EvI2Zxgh_BlTuZECRho97FZ1A-Kd22fzJ5qPC9c-h52nrKeXYXoGDnRU-5xIrhSNsO3y68ZqfD3b45-rhfmEpVbQ7M--wZo6D8q3cA3lDBdQIII6eIENJbOzMg5kBWiUWYRxV5fYam393MxyKQUAHym3TKuLNkvXcxdUpuNQ-UPwLeBrtU6FT7lHL5Wn4AIcwCbSpC5MUx_n6i-pmnp41nsDr-Bc1vK_zFCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شناسایی شبکه گسترده افزونه‌های جعلی فایرفاکس برای سرقت رمزارزها
محققان امنیتی شرکت
Socket
شبکه‌ای سازمان‌یافته شامل ده‌ها افزونه مخرب را در مرورگر فایرفاکس شناسایی کرده‌اند که با هدف سرقت کلیدهای خصوصی و عبارت‌های بازیابی (Seed Phrase) کاربران وب ۳ طراحی شده‌اند.
⚙️
روش کار و جزئیات این حمله:
🔹
جعل هویت کیف‌پول‌های معروف:
این افزونه‌ها نام و رابط کاربری ولت‌های معتبری مانند
OKX
،
Rabby Wallet
و
TronLink
را شبیه‌سازی کرده و بلافاصله پس از ورود اطلاعات توسط کاربر، کلید خصوصی را به سرورهای مهاجم ارسال می‌کنند.
🔹
تغییر ماهیت بعد از جلب اعتماد:
تعدادی از این افزونه‌ها ابتدا ماه‌ها در قالب ابزارهای نمایش نتایج زنده فوتبال و بسکتبال، تم تاریک، پسورد منیجر یا وی‌پی‌ان فعالیت می‌کردند و پس از جذب نصب بالا و امتیاز مثبت، با یک آپدیت مخرب به بدافزار سرقت دارایی تبدیل شدند.
🔹
ابعاد کمپین:
کارشناسان موفق به ردگیری ۷۷ شناسه مرتبط شده‌اند که مخرب بودن حداقل ۴۰ مورد آن‌ها به‌طور قطعی تأیید شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eld1TnncimanCVxiTt8PEfsdUzEQuf4f2rdoxIcC__tNNfF74mgMTE48COa-6eRld3Zf-RJKZbZqfnTWn-vQPEdL8kNePV7O5RV0D6gw7YRq3i8qPMHPRMiTucfgOaiwqpPG2fABz_Shg0usv7eL7zEXkQgTNYQC9zSIoQ_q39jsbRfo_nBa198QCBckIO2z2wtqVdzfslpaEpVG3YRaWv3bium4eQaK7gRH6u902LSYfkhHNVIH7HfuRIYguNoFu4DOp17JnYcS3cclQXvBA9iZmiAvtKUZBHSIO12PwudaovOgwKye3u_oNJwwrdMU6Zsx8xiRS2VnyoGGORiQuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
لطفاً برای هر ایده ساده، اسکریپت جدید نزنید!
✍🏻
دم همه‌ی دوستانی که توی این یک سال اخیر با کمک AI اسکریپت‌های کاربردی نوشتن و به بقیه کمک کردن گرم. ولی یکی دو تا نکته هست که باید بهش دقت کنیم:
۱.
فورک‌های بی‌مورد:
لازم نیست هر فیچری که حس می‌کنید یه پروژه کم داره رو سریع فورک کنید، بهش اضافه کنید و با یه اسم جدید بدید بیرون! با این کار فقط کامیونیتی تیکه تیکه میشه و کلی ریپوی نیمه‌کاره و بدون پشتیبانی روی گیت‌هاب رها میشه. اگه واقعاً ایده‌تون کاربردی و درسته، بهتره همون رو به صورت Pull Request برای نویسنده‌ی اصلی بفرستید تا روی سورس اصلی مرج بشه.
۲.
تمرکز روی نیاز واقعی، نه هر ایده‌ای:
لازم نیست هر چیزی که به ذهن می‌رسه رو با عجله کد بزنیم و فکر کنیم حتماً به درد همه می‌خوره! مثلاً واقعاً نیازی نیست برای یه دستور ساده‌ی Iptables بیایم اسکریپت نصب آسان بنویسیم.
۳.
مسئولیت نگهداری و امنیت:
ساختن اسکریپت با هوش مصنوعی شاید با چندتا پرامپت ۵ دقیقه زمان ببره، ولی پشتیبانی، رفع باگ‌ها و حفظ امنیتش کار راحتی نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⭕️
طرح جدید «نظام‌بخشی فضای مجازی»؛ از جریمه ۱۰ درصدی درآمد تا لغو مجوز پلتفرم‌ها
پیش‌نویس سند «طرح نظام‌بخشی فضای مجازی» با هدف تفکیک وظایف تنظیم‌گری، تعیین مجازات برای پلتفرم‌ها و تعریف حقوق کاربران نهایی شده است.
🔹
تفکیک وظایف تنظیم‌گری میان نهادها:
مدیریت اینترنت، کلاود و دیتاسنترها به وزارت ارتباطات؛ پرداخت‌ها به بانک مرکزی؛ ضد انحصار به شورای رقابت؛ صوت و تصویر فراگیر به ساترا؛ و اخلاق و ایمنی الگوریتم‌ها به سازمان ملی هوش مصنوعی سپرده می‌شود.
🔹
ضمانت اجراها و مجازات‌های سنگین:
شامل اخطار، انتشار عمومی تخلف، محرومیت ۱ تا ۳ ساله از تسهیلات،
جریمه نقدی ۱ تا ۱۰ درصد از درآمد سالانه
، تعلیق و در نهایت لغو کامل مجوز فعالیت.
🔹
مهم‌ترین مصادیق تخلف پلتفرم‌ها:
نقض حقوق کاربران، رفتارهای ضد رقابتی، عدم احراز هویت معتبر کاربران پیش از ارائه خدمات، خودداری از ارائه اطلاعات به تنظیم‌گر و عدم رعایت مصوبات قانونی.
🔹
به‌رسمیت شناختن حقوق کاربران:
تاکید بر «حق دسترسی به شبکه»، ممنوعیت قطع یا دستکاری ترافیک بر اساس اصل «بی‌طرفی شبکه (Net Neutrality)» و رعایت رده‌بندی سنی و حقوق کودکان.
🔹
سامانه حکمرانی مشارکتی:
الزام به انتشار پیش‌نویس مصوبات ۲ هفته پیش از تصویب جهت نظرخواهی عمومی از مردم و کارشناسان در یک سامانه هوشمند./
مقاله کامل
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nvn95OQ2r6ef2ezivpJ9BaugUQMvc1nMvy1vQVlThxfsvLnQJqDy4xgG-ur7L5dgdWXXvVCb88VBTeiOTIVBGap7rcgtaScWwNLA69UNcSyvV4z55Fn4gEXYghetpIxGo4ckW9m3VknRWZv0V-tBwoeXoGakyaGIaYwjllsY7wbJ4OKbcxMS7so29TT9GybOOr_Gz4UYmKmyATi_qV8TTdDfZ68vYDiHKRFanCET60zDLcxRFuTps7CXPxXDW9v_8h0CjJwH5wjVj8povxfQj1XjK60NnVn4-eFY9-mmMUMoEVlPtmq1FPq-g7WlirsYa6kFKGS6cMAi_RCBgxHViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی تانل سبک و بهینه Netlink Tunnel
پروژه
Netlink Tunnel
یک ابزار تانلینگ سبک، بهینه و کاربردی است که امکان مدیریت کامل و سریع تمام اتصالات را از طریق خط فرمان (CLI) فراهم می‌کند.
🔹
تشخیص قطعی و پایداری بالاتر:
واکنش سریع‌تر سیستم در شناسایی قطع ارتباط و اعمال Reconnect خودکار.
🔹
مانیتورینگ و آمار ترافیک Live:
نمایش لحظه‌ای حجم دانلود، آپلود و مجموع ترافیک مصرفی.
🔹
گزینه Optimize:
ابزار اختصاصی بهینه‌سازی پارامترها و تنظیمات شبکه.
🔹
پشتیبانی از پروتکل‌های متنوع شامل TCP، TCP Mux، حالت‌های مخفی‌ساز TCP Stealth و TCP PCK
🔹
پشتیبانی از اتصالات وب‌سوکت WS / WS Mux و WSS / WSS Mux
🔹
انتقال پایدار روی بستر UDP + FEC (تصحیح خطای رو به جلو)
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qitv6qMP54vfIlvfAnQ22Jot030F4UA6bU4nlS1Go-aSqEyW9gH5oWU3gYYL1kF8wN2rEtEKhPHUW8Vx_EZ-l6rML-Z-qzHtZzh_3HyM9AHEQIihenuDhJGTH4WRgpxFuHrAVhpaf71FyrezBSFD5Uu3zg7mSR7B5tUICyoLVN96amWBl038YsaRRRuuoSffwQQhL5QYqB588ja3X51J1ToW4fkHyXBSIzHeF4bknhzhRRV_m5Mw0tNb1GROyC8JuFQZzQlFUvBXZs77ZX6T9z4asPD02uHVtJZLKLH3_9P0H2sKglvUmu4KU_wzuT04-4xyzFyUfpDBwzB8v6aG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
معرفی DayLock؛ گاوصندوق دیجیتال و ‌امن
پروژه متن‌باز DayLock یک سرویس اشتراک‌گذاری پیام و فایل بر پایه معماری «دانش صفر» (Zero-Knowledge) است؛ یعنی سرور هیچ دسترسی یا کلیدی برای خواندن اطلاعات شما ندارد!
🔹
رمزنگاری سمت کاربر:
تمام داده‌ها مستقیماً در مرورگر شما رمزنگاری می‌شوند و سرور فقط کدهای نامفهوم را ذخیره می‌کند.
🔹
پنهان‌نگاری پیشرفته:
مخفی کردن امن فایل‌ها و متن‌های حساس داخل تصاویر (PNG) یا فایل‌های صوتی.
🔹
رمز فریب‌دهنده (Decoy):
امکان ایجاد یک گاوصندوق جعلی برای مواقعی که تحت فشار مجبور به باز کردن فایل‌هایتان می‌شوید.
🔹
قفل‌های هوشمند:
محدود کردن دسترسی بر اساس کشور (Geo-Lock)، شبکه اینترنت (ASN) یا تنظیم زمان مشخص برای باز شدن پیام (Time-Lock).
🔹
تخریب خودکار:
قابلیت حذف برای همیشه پس از اولین بازدید (Burn-on-Read) یا پاک‌سازی خودکار در صورت عدم فعالیت (سوئیچ مرد مرده).
🔗
لینک بررسی و نصب در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxhCJLPC1QMnXLTXDD5mxAHDFlrNOX5kO0693JBqDHTWhwXoFxzfubPWOkbxuM392QI2gIK300wWYplL51BOgzvp48zF_nuxFIa6kdTuBBLwSo0px0NhaLCc7x1h1x0fafBiRoPvo5qrD7reQXy_A2nspkHinTU8dr_5cle6Yv2-0LquZFruId3EldhGVp2wsY3nhw45h-DZxpxxeAVEKEAajSNLFRE5a4SMeXTV_7TD9yeGMwKg4bqs0rgKzlsb4rmvOm6OWvyL9_pDBGcHQjtM12LagmacmdsQe9P2ZMB_KuvdLGSZdF34ImPb95mHqrYcvSH5KDx6DJfzOub0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pr-fhIW_8iJCue-tcjd-GIdS63hL3zuqNt9zwlrNmn9JC7ocBPIP7Gat_QR4hUe4oaYW69grFmAFDaHZCYUrOc9pNbTbqY_5oTZYdm_YCdPW82oJE9pzESZZH9Ysdaf945w6AC6EhUiEl9pQJEOC5gw1u1z3AaQrt4xR_MKod0ZkHyAeuF_yYQ6AVqIbIiYbzWfjaZh-nS5AUUe3Q8B_cASLX37qhnrUi8Wuw5N5TGrVY0ne9K-m_q0vrJ9qSB2nWnvz53B93seiYh89kZgR6ONSz5Tg80_2gd_BPVejhrRUto05UcBJDzxyNIfThkfK8UB0_Sb3Vz7M8BJR-uNBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آپدیت بزرگ ۱۳ سالگی تلگرام منتشر شد؛ از فایل‌های درون‌متنی تا پیام‌های خوشامدگویی اختصاصی
تلگرام هم‌زمان با سیزدهمین سالگرد فعالیت خود، آپدیت جدیدی را همراه با قابلیت‌های کاربردی برای کاربران، مدیران کانال‌ها و توسعه‌دهندگان بات‌ها معرفی کرد.
🔹
پیام‌های خوشامدگویی:
مدیران گروه‌ها و کانال‌ها اکنون می‌توانند بسته‌های خوشامدگویی شامل متن، عکس، ویدیو و جداول بسازند که تنها برای کاربر تازه‌وارد نمایش داده می‌شود.
🔹
دکمه‌های تعاملی درون پیام‌ها:
با به‌روزرسانی
Bot API 10.3
، توسعه‌دهندگان می‌توانند دکمه‌های کنترلی تعاملی را مستقیماً داخل پیام‌ها قرار دهند و امکان اجرای بازی‌ها (مانند شطرنج)، آزمون‌ها، نظرسنجی‌ها و سفارش کالا را به‌صورت زنده فراهم کنند.
🔹
قراردادن فایل داخل متن:
ویرایشگر پیشرفته متن اکنون امکان گنجاندن فایل‌ها و آهنگ‌ها را درون بخش‌های مختلف نوشته فراهم کرده است (با نوشتن بیش از سه خط متن فعال می‌شود).
🔹
افزودن امضا و پیام به هدایا (Gifts):
هنگام خرید هدایای کمیاب (Collectible) با استفاده از Telegram Stars، می‌توان امضا و متن شخصی دلخواه را به هدیه پیوست کرد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🛑
یه اشتباه خیلی رایج و خطرناک: «هر اسکریپتی که اوپن‌سورسه امنه!»
سلام دوستان عزیز
✋
همون‌طور که می‌دونید، هدف اصلی این کانال معرفی اسکریپت‌ها و ابزارهای اوپن‌سورس برای دور زدن فیلترینگه. اما یه سوءتفاهم خیلی بزرگ و خطرناک بین کاربرا وجود داره که وظیفه خودم دونستم حتماً در موردش باهاتون صحبت کنم.
خیلیا فکر می‌کنن چون یه برنامه «اوپن‌سورس» هست، پس قطعاً هیچ بدافزاری توش نیست و ۱۰۰٪ امنه. اما واقعیت اصلاً این نیست!
متن‌باز بودن فقط معنیش اینه که کدهای اون برنامه برای همه قابل دیدنه.
این ویژگی به خودیِ خود امنیت رو تضمین نمی‌کنه؛
بلکه امنیت زمانی وجود داره که متخصص‌ها، اون کدها رو خط‌به‌خط بررسی کنن. اگر کسی کدها رو نخونه، یه بدافزار خیلی راحت می‌تونه جلوی چشم همه تو همون کدهای اوپن‌سورس قایم بشه.
من خودم همیشه قبل از اینکه اسکریپتی رو معرفی کنم، تمام تلاشم رو می‌کنم تا در حد توانم و با کمک هوش مصنوعی، کدها رو بررسی کنم تا مورد مخربی توشون نباشه. اما یه مشکل بزرگ وجود داره:
👈🏻
اسکریپت‌ها مدام آپدیت میشن!
🔹
یه اسکریپت ممکنه بعد از اینکه تو کانال معرفی شد، تو همون چند هفته اول ده‌ها آپدیت جدید بده. بررسی تک‌تک این آپدیت‌ها برای منِ نوعی واقعاً غیرممکنه. این یعنی ممکنه اسکریپتی که ماه پیش کاملاً امن بوده، تو آپدیت امروزش حاوی کدهای مخرب باشه (حالا یا عمدی توسط خود سازنده یا به خاطر هک شدن اکانتش و...).
💡
خب راه‌حل چیه؟ چطور امن بمونیم؟
۱.
هیجانی آپدیت نکنید:
هیچ‌وقت به محض اینکه سازنده یه آپدیت جدید داد، سریع نرید اسکریپتتون رو آپدیت کنید! حداقل چند روزی صبر کنید. اگر تو آپدیت جدید بدافزاری باشه، معمولاً بقیه برنامه‌نویس‌ها زود متوجه میشن و گزارش میدن.
۲.
استفاده از نسخه‌های تست‌شده:
سعی کنید از همون نسخه‌ای (Release) استفاده کنید که روز اول تو کانال معرفی کردم و داره کار می‌کنه. تا وقتی اسکریپت فعلی‌تون بدون مشکل وصل میشه، لزومی به آپدیت کردن مداوم نیست.
۳.
به اعتبار پروژه دقت کنید:
پروژه‌هایی که تو گیت‌هاب ستاره (Star) بالایی دارن و افراد زیادی اون‌ها رو فورک (Fork) کردن، معمولاً بیشتر زیر ذره‌بین متخصص‌ها هستن و امنیتشون از اسکریپت‌های ناشناس بیشتره.
۴.
گزارش موارد مشکوک:
اگر خودتون برنامه‌نویسی بلدین و کدهای آپدیت‌های جدید رو نگاه می‌کنید، اگر مورد مشکوکی تو آپدیتی دیدید، ممنون میشم به ربات ما پیام بدید.
در نهایت فراموش نکنید همیشه حواستون جمع باشه و به هیچ ابزاری، حتی اوپن‌سورس، چشم‌بسته اعتماد نکنید.
🛡
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
