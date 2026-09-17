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
<img src="https://cdn4.telesco.pe/file/CUXvXX34Qip01PgQyiaWWOFZMVIjJxM8TUwSroI0WJ_GqxklXeVJ1n5pd0_-H98EDHJsVUM4rxlWmaLLjrnw0Jala9F5pHi0nLu3n8rfXqS60HQMtSoPb5zk5VTNOEJZ3ujH3bW_OhQvc15ZDM-gVVizaQunNbcRlBBglHOhfFhLwZdGFRuSz4NtBpGWd2SC6LWMBCPHEq9DDdn0ug6hly8aWqrGjIN0NPb9P3GjWMpba0qCTh_06GUvqDr5k2lUqBLb-tmbaEWDe4D6Ct4q9h2rAPFlQvysUZdXHskswMqrQdTsoc_U1MmczONJsTWVoZumHVh0g9_zbJOWZEXi9w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 107K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-1819">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gQO9HjbfSVteh74koDGrUxNCvsv9vMNSmX1adH6PPC1oqt4_zCskIPUsLxc6hL1EHxEYhSeHZyoxotZ5ypxS0QmMdZgqjBT067ieba_AZk5gUg-FijxdHJZc5KgDO-Q2Ks1r7HTfLguYPWWTj2Q_65nmClegowBQxJXdcVi69USDWutolrojLNb1ZJjrEOdmT8RvMwdQGmYZdJis8JS5iangBYtJTu4q1DWXQaMproa7Bn4uPHFuJ_wCb9vTGZFcTofVa2AxfKZfyEYEzRMTwHfHXotop2vLLVOAIXgPsuLsa6xiCIe9YhYMSqmNSBPfEJ37q-W39h9QOStKNVmfWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whiteaesther moblie pre-release 1.8.1
⚠️
این نسخه برای کاربرانی هست که توی چند روز گذشته اختلال شدید گزارش کردند و نسخه آخر هم مشکل انها را حل نکرد
برخلاف باور غلط عمومی ورژن ها در حال بدتر شدن نیستند بلکه امکانات بیشتری در حال اضافه شدن است - اما به دلیل گستردگی کاربران ما مجبوریم حداکثر بومی سازی را انجام بدهیم که این کار گاها زمان بر خواهد بود .
اگر روی ورژن قبلی مشکلی ندارید فعلا اپدیت نکنید !!!!
⚠️
⚠️
⚠️
دو اصلاح، هر دو روی حساب زنده اندازه‌گیری شده:
MASQUE دیگر دنبال آدرس نمی‌گردد. Cloudflare در هر پاسخ ثبت‌نام آدرس اختصاصی دستگاه را می‌دهد و موتور نادیده‌اش می‌گرفت
ثبت‌نام‌های Cloudflare دیگر دور ریخته نمی‌شوند. هویت بلافاصله پس از ثبت‌نام و پیش از هر کار دیگری ذخیره می‌شود؛ مسیر مستقیم یک بار امتحان می‌شود نه پنج بار؛ و نصبی که enrolment مربوط به MASQUE کلید WireGuard‌
اش را باطل کرده بود، در اولین اتصال خودش را تعمیر می‌کند.
این نسخه به‌صورت خودکار به کسی پیشنهاد نمی‌شود.
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.8.1
@whitedns</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/whitedns/1819" target="_blank">📅 12:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1818">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">😎
دیگه لازم نیست برای آپدیت از اپ خارج بشید.
اپ اتوماتیک ورژن جدید رو دانلود و نصب میکنه.
این به کسایی که اطلاعات فنی هم ندارن کمک میکنه.</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/whitedns/1818" target="_blank">📅 11:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1817">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVWM5IWXDf2kjxYnJo66C1-ggQMC_75nnYrBBYcfmO4PgyOGChqcSOHMvjanQla1xbnzNxg0T0oGRbMPsQYpQX2ez21XNnmNVbFCYFULjE3BOF5dP3Ek-W-Xp0qHiANuWhFoxeLmw9OZ_R1ViWFnsWkHO0ruoafz_FQ8NRTr0I5JKLgWEPNfIF95JI0XANQEHXPBOKb2fnV0dI7_7cOpbDzGYD06v_h25AoJQCB38COGB8bVxx_Nq8g0IUC_M1404EdYnUnIQPHGFaPqzW_jRY1xPS78KERfJpahtBzbFjnb_kw3HSR9n-XQn7stPIPKkP8Ta6VEC1CL035m8sQTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.8
تغییرات نسخه جدید:
🟢
ویجت صفحهٔ اصلی برای اتصال، قطع اتصال و نمایش وضعیت VPN
🟢
به‌روزرسانی از داخل برنامه، با نمایش پیشرفت دانلود، امکان رد کردن یک نسخه و بررسی صحت فایل و امضا پیش از نصب
🟢
اجرای Real Delay Test و تست سرعت در پس‌زمینه و هنگام خاموش بودن صفحه
📱
دانلود از گیتهاب</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/whitedns/1817" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1815">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭐️
چطور API رایگان DeepSeek V4.1 Flash بگیریم؟
توی این ویدیو، قدم‌به‌قدم نشون می‌دم چطور به API این مدل دسترسی رایگان بگیرید؛
اگه با API آشنا نیستید، خیلی ساده یعنی به‌جای اینکه فقط توی سایت با هوش مصنوعی چت کنید، بتونید ازش داخل برنامه‌ها و ابزارهای خودتون استفاده کنید.
چه بخواید ایده‌ای رو تست کنید، چه روی یک پروژهٔ شخصی کار کنید یا تازه کار با API رو یاد بگیرید، این آموزش می‌تونه نقطهٔ شروع خوبی باشه.
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1815" target="_blank">📅 22:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1812">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✍️
موقت
دوستان هم نسخه مبایل و هم دسکتاپ برای کارایی بهتر اول ورژن قدیمی را uninstall کنید و بعد نسخه جدید را نصب کنید
در نسخه ویندوز موقع uninstall کردن حتما گزینه delete app data را بزنید
ممنون</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1812" target="_blank">📅 16:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1811">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/mcXzGGQRqHWcn0-Aw2TbWTq7MV2XUeiFdMhs3r__S2sQkmSC9hNxDR2JY1CYJz2a28Lv2XRej6K8Oy0rtPG-jdv86Ed9DdiIiSi9_5rXjb2408dAEHWSaBwLfe9XyQXTiuBvFe5RJKdFFTbd8tIZGJVLf9x_-h3nJq4sptKsfPWJkoHq3WnxqgRf6VfcD4f9aB0D_Hir7KOYuxuaHu-mQoudaQbdh8Ljl9z4RpqOLr0uiOKUrTTl64OFTGLs2Ntduh8wBAYnXH9zNcFZaczvCGezUExpmGXS9u1S8o0P0IgnxW_nsO5EKUql7kMm5fVTC1am3OYD8rJPGpt7Xt3fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
WhiteAesther Mobile ۱.۸.۰ نسخهٔ پایدار
این نسخه دو کار را با هم می‌آورد: هرچه در نسخهٔ آزمایشی ۱.۷.۰ بود، به‌علاوهٔ یک راه خروج تازه. اگر روی ۱.۶.۱ هستید، هر دو را یک‌جا می‌گیرید.
⚡️
اتصال روی شبکه‌هایی که تا حالا جواب نمی‌دادند
حالت خودکار حالا واقعاً خودکار است. از همان لحظهٔ زدن دکمه، اتر و سایفون و تور را هم‌زمان می‌فرستد و هرکدام زودتر ترافیک را رد کرد همان می‌ماند. تشخیص اینکه کدام مسیر واقعاً کار می‌کند هم دقیق‌تر شده — دیگر یک مسیر سالم را به اشتباه کنار نمی‌گذارد.
این حالت از این نسخه پیش‌فرض روشن است. اگر خودتان قبلاً حاملی انتخاب کرده‌اید، انتخابتان دست‌نخورده می‌ماند.
🧅
ماسک در ماسک — راه تازه
یک پروتکل جدید برای شبکه‌ای که یاد گرفته یک تونل ماسک تنها را بشناسد. دو پرش تودرتو: پرش داخلی از دل بیرونی دست می‌دهد، پس چیزی که شبکه می‌بیند یک تونل است که محتوای مبهم حمل می‌کند، نه الگویی که آموزش دیده دنبالش بگردد.
هم در فهرست پروتکل‌ها هست، هم آخرین چیزی که حالت خودکار امتحان می‌کند — و بخش دوم مهم‌تر است: شبکه‌ای که این برایش ساخته شده همان جایی است که بقیهٔ راه‌ها شکست خورده‌اند، و کسی سراغ تنظیمات پیشرفته نمی‌رود. پس خودکار خودش به آن می‌رسد، بعد از اینکه راه‌های سریع‌تر نوبتشان را گرفتند.
از یک پرش کندتر است و عمداً آخر است. جایی که یک پرش کار می‌کند، چیزی برای شما عوض نمی‌شود.
🧠
موتور اتر ۲.۰
هستهٔ برنامه یک نسخهٔ کامل جلو رفت: سرعت عبور ترافیک روی تونل‌های TCP بیشتر شده، یک لایهٔ تازهٔ دور زدن تشخیص پیش از دست‌دهی اضافه شده، و پایداری تونل‌های تودرتو بهتر شده است.
🌍
کشور خروج روان‌تر
فهرست کشورها بلافاصله به‌روز می‌شود، «بهترین گزینهٔ موجود» همیشه در دسترس است، و اگر کشوری که انتخاب کرده‌اید در دسترس نباشد برنامه صریح می‌گوید به‌جای اینکه بی‌صدا تلاش کند.
🛡
پایدارتر
اتصال مجدد بعد از قطعی، حفظ تنظیمات محافظتی پس از راه‌اندازی دوبارهٔ سیستم، و رفتار دقیق‌تر هنگام جابه‌جایی بین وای‌فای و دیتا.
━━━━━━━━━━
📥
دریافت
برنامه خودش این نسخه را به شما پیشنهاد می‌دهد. اگر می‌خواهید همین حالا بگیرید:
برای تقریباً همهٔ گوشی‌های امروزی:
WhiteAestherMobile-1.8.0-arm64-v8a.apk (۴۵ مگابایت)
اگر نصب نشد، فایل universal را بگیرید — روی هر گوشی کار می‌کند ولی حجمش بیشتر است.
🔗
github.com/WhiteDNS/WhiteAestherMobile/releases/latest
روی نسخهٔ فعلی نصب می‌شود و تنظیماتتان می‌ماند.
#WhiteAesther
#v1_8_0
@whitedns</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1811" target="_blank">📅 16:54 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1810">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cPloJE7sPwmGy6Mm0Cel87tRA3YRlknfDrFJCGUfYwR_8zzScI7-qTAExqY6H0M8NFU2R8YccCTkCotYRioCKZUSvNoqkcsZEtHhpkdDUi_1mXq7VeUyzMwYA5KIfPivw2S9R6_FIAbRaC8JN0x6NXFPjzwPQ7TGeJhJEmGJtcSIc7LfyFRC4Qr2Pufx-4N3GAO6E5ddw5tPDaMyocrv46nz7RJq6BJJFxZvlFE3p60itYqrfYBozMhfgNNCwja4gVepXHjuI5qdmt3o6dcvlGZ7VlUrW5k_W46F--3ajvFTuqz4jrg6WHkKIuH-HuwzUzRu3bJEUUI84j1LJCzsug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
WhiteAesther Desktop 1.9.4 — نسخهٔ پایدار
بزرگ‌ترین تغییر از زمان ۱.۹.۱، و دقیقاً همان چیزی است که بیشتر کاربرها لازم داشتند.
دیگر لازم نیست بدانید کدام راه کار می‌کند
تا امروز اگر وصل نمی‌شدید، باید می‌رفتید در تنظیمات پیشرفته و بین Aether و سایفون و تور یکی را انتخاب می‌کردید. بیشتر مردم اصلاً نمی‌دانستند این گزینه‌ها وجود دارند و فقط فکر می‌کردند برنامه کار نمی‌کند.
حالا فقط اتصال را بزنید. برنامه هر پنج راه خروج را هم‌زمان امتحان می‌کند و اولی که واقعاً ترافیک حمل کند نگه می‌دارد.
قبلاً یکی‌یکی امتحان می‌شدند: اگر Aether بیرون نمی‌رفت، باید سه دقیقه صبر می‌کردید تا نوبت سایفون برسد. حالا همه با هم شروع می‌شوند و معمولاً چند ثانیه‌ای تمام است.
🆕
یک راه خروج تازه: MASQUE در MASQUE
بعضی شبکه‌ها یاد گرفته‌اند یک تونل MASQUE را بشناسند و ببندند. این حالت دو تونل تودرتو می‌سازد که از داخل هم رد می‌شوند.
لازم نیست انتخابش کنید — جزو همان پنج راهی است که خودکار امتحان می‌شود. روی شبکه‌ای که بقیه بسته‌اند، ممکن است تنها راهی باشد که باز می‌شود.
⚡️
موتور به نسخهٔ ۲ رفت
هستهٔ Aether از ۱.۸ به ۲.۰ ارتقا یافت. محسوس‌ترین اثرش سرعت است: بسته‌های بزرگ‌تر روی MASQUE H2 و دست‌دادن سریع‌تر.
🔒
حالا مطمئن می‌شویم چه کسی جواب می‌دهد
قبلاً برنامه یک مسیر را «کارکن» حساب می‌کرد اگر چیزی از آن برمی‌گشت. ولی روی شبکه‌ای که ترافیک را شنود می‌کند، خودِ شنودکننده هم جواب می‌دهد — یعنی ممکن بود همان مسیری انتخاب شود که در حال خوانده شدن است.
حالا از سایتی که به آن وصل می‌شود می‌خواهد هویتش را با گواهی ثابت کند؛ چیزی که فقط سایت واقعی می‌تواند ارائه دهد.
🐧
و برای کاربران لینوکس
پیام خطای «تونل کامل» دیگر شما را دنبال دکمه‌ای که روی لینوکس وجود ندارد نمی‌فرستد. حالا می‌گوید واقعاً چه کاری از دستتان برمی‌آید.
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/whitedns/1810" target="_blank">📅 16:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1807">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💬
تقریبا ۵۰۰۰ هزار کاربر فعال از کشور روسیه داریم که روانه دارن از WhiteVPN استفاده میکنند.
اونا هم اندازه ما دردسر فیلتر دارن، اما با توجه به «چراغی که به خانه رواست ...» از ورژن بعدی دسترسی کشور های دیگرو به اپ میبندیم.
• از ورژن بعدی میتونید اپ رو ببندید و پشت صحنه اسکن انجام میشه.
• آپدیت داخلی و اتومیاتیک به اپ اضافه شده
• بکسری تغییرات کوچیک دیگه
💬
اگر مشکلی داشتید که به ما گزارش دادید و ما فیکس نکردیم، لطفا برامون بفرستید.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1807" target="_blank">📅 09:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">💬
دوستان ما هرشب سرور های اختصاصی رو روی WhiteVPN بروز میکنیم تا از فیلتر شدن سرور ها جلوگیری کنیم.
متاسفانه این‌چند روز سرور سنگاپور رو نداریم ، توی یک شب ۳۰ ترابایت مصرف شد و هزینه زیادی داشت. وقتی خاموشش کردیم، دیگه سرور سنگاپور ارایه نمیداد.
باید دوباره موجود بشه و براتون یکی به زودی میسازیم.
🔒
اگر براتون مستقیم وصل نمیشه، به یک سرور عمومی وصل بشید و اختصاصی رو زنجیر Chain بکنید تا آی‌پی ثابت بگیرید.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1805" target="_blank">📅 02:11 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/W1o7ww9QiMh0tEkptwwtEUxHdYDVNVctzBtxR7NmoLAql-amcx1VBYipumnlacV3EW-LXwz7JjZABlWQEW5rE-5mTMD9dOTYDrQ51R7gIIoLV9kU_fMXrwqkBWIwLC6buS1X7N__XPeqiv6KQmI0V4QKy5IgEY-LOzWEweHMIgmxAkHMlKXx51Z5rtdGuA3n2_dAOMD4BwtnD4JN0GCIL_Ck6u4GhjduOX_TN8OhpMGhWaYmJJ0IqQAl009HUEP2umMXHaQChYGNUcNX8tXGhStXA7WvpQxalvuS2N4YSrdVTe3xur9b0gfvQRptyl1fK27CRS-BhtWLu29_IvSQUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
اگر به هر دلیلی نیاز به کانفیگ (cottondns,masterdns,stromdns) برای اپ
WhiteDNS
دارید از ربات زیر میتونید با محدودیت حجم و روزانه کانفیگ بگیرید.
⚠️
این کانفیگ 1 روزه و با حجم 0.5 گیگ هست
در حال حاضر تعداد کانفیگی که میتونیم بدیم خیلی محدود است و فقط با تاییدیه ادمین برای شما ارسال میشه
⛔️
لطفا اگر اشنایی ندارید و کنکجاوید و یا میخواید ازمایش کنید و... درخواست ندید
@MasterDnsManager_bot
WhiteDNSاپلیکیشن
دانلود اندروید
•
دانلود دسکتاپ
@whitedns</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1793" target="_blank">📅 09:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1790">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JPaAsCOirtnwiGyxbVpsTXkENZYA_v3Xo0HiReGRE6NSgoB3LepUoq3bPC96mjByLZUjpIaggRPT_6o3Uu6S0UkVrT5MMI154ZXttGWsxDmaxUJCutVdlIultfcJagayUTt85zp_q3jS99r7NTAmcZojH0fj93AQ23JG7uQaVH9F2EYM72fiC-SpskeCyEcouHCu_TClaQFhS9kCAcGFBMQ4lgtQigp4gVj1nOmASSu8gAFuvbgy4vi2utSf_puy4a-x0C7cKwc4yjtwns5FG2ykQgTjqExrS7pVpxIg-XKvH9Pn0UMtbYp7IcVNpjdHV3cwJ30i94ckmlMV1h22cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
🤖
قابلیت جدید : (نسخه ازمایشی )
⚠️
⚠️
⚠️
گفت‌وگو با هوش مصنوعی در ربات
🔥
WhiteDNSResponder V.5
نسخه ازمایشی حتما باگ هایی دارد  و  دچار اشکالاتی خواهد شد که با پشنهادات و کمک شما هر روز بهبود خواهد یافت
👀
از این پس می‌توانید مستقیماً داخل ربات با هوش مصنوعی گفت‌وگو کنید، سؤال بپرسید، متن تولید یا ترجمه کنید و درباره موضوعات مختلف توضیح بگیرید.
این امکان جدید به صورت محدود و با درخواست کاربر فعال میشود.
⚠️
@WhiteDnsResponder_bot
🔐
نحوه درخواست دسترسی
1️⃣
وارد گفت‌وگوی خصوصی ربات شوید.
2️⃣
از منوی ربات گزینه /airequest را انتخاب کنید.
3️⃣
درخواست شما برای مدیر ارسال می‌شود.
4️⃣
پس از تأیید، دسترسی به‌صورت خودکار فعال شده و نتیجه از طریق ربات به شما اعلام می‌شود.
نیازی به پیدا کردن یا ارسال شناسه عددی تلگرام نیست.
🔹
روش استفاده
پس از فعال‌شدن دسترسی، سؤال خود را بعد از دستور /ai بنویسید:
/ai تفاوت DNS و VPN چیست؟
یا:
/ai یک متن رسمی برای درخواست همکاری بنویس
🔹
دستورات کاربردی
/ai سوال شما
شروع یا ادامه گفت‌وگو با هوش مصنوعی
/ainew
پاک‌کردن گفت‌وگوی قبلی و شروع مکالمه‌ای تازه
/aistatus
مشاهده سهمیه روزانه، میزان مصرف و تعداد درخواست‌های باقی‌مانده
📊
محدودیت‌های فعلی
• سهمیه روزانه براساس تأیید مدیر: ۵ یا ۱۰ پیام
• حداکثر ۳ درخواست در هر ۵ دقیقه
• حداکثر ۲۰۰۰ نویسه برای هر پیام
• نگهداری موقت چهار بخش قبلی مکالمه برای ادامه بهتر گفتگو
• قابل استفاده فقط در گفت‌وگوی خصوصی با ربات
• سهمیه روزانه در نیمه‌شب به وقت UTC تمدید می‌شود
🔒
امنیت و حریم خصوصی
• هوش مصنوعی به سرور، فایل‌ها، دستورات سیستمی یا اطلاعات خصوصی تلگرام شما دسترسی ندارد.
• متن مکالمات توسط این قابلیت در پایگاه داده ذخیره نمی‌شود.
• تنها شناسه کاربر، وضعیت دسترسی و میزان مصرف سهمیه ثبت می‌شود.
• لطفاً رمز عبور، اطلاعات بانکی، کلید API یا اطلاعات محرمانه ارسال نکنید.
⚠️
این قابلیت فعلاً به‌صورت محدود و آزمایشی ارائه می‌شود. درخواست‌های تکراری ارسال نخواهند شد و در صورت استفاده نادرست یا ارسال خودکار پیام‌ها، دسترسی کاربر ممکن است غیرفعال شود.
🤍
WhiteDNS — دسترسی ساده‌تر به ابزارهای کاربردی هوش مصنوعی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1790" target="_blank">📅 15:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1789">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✍️
موقت
اگر روی ویندوز و یا اندروید نسخه قدیمی دارید
⚠️
⚠️
ویندوز :
گزینه reset app data را بزنید و بعد uninstall کنید و جدیدترین نسخه را نصب کنید
اندروید :
حتما ورژن قدیمی را uninstall کنید و ورژن جدید را نصب کنید
@whitedns</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1789" target="_blank">📅 04:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1787">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✍️
موقت
برای جمینای و بقیه هوش مصنوعی ها بر اساس تستی که کردیم روی سایفون و تور راحت باز میشه - اگر تور و سایفون مستقیم وصل نمیشه اول با اتر وصل بشید و بعد خروجی را روی سایفون و یا تور تنظیم کنید.
در ضمن اگر روی یک اپراتور جواب نمیگیرید حتما حداقل یک اپراتور دیگه را هم تست کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/whitedns/1787" target="_blank">📅 19:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1785">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-poll">
<h4>📊 امشب ساعت 8 به وقت ایران لایو بگذاریم جواب سوالات را بدیم ؟</h4>
<ul>
<li>✓ بله😍</li>
<li>✓ خیر😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1785" target="_blank">📅 14:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1784">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ao4QLJAhNC8JcQWCPromO_rRvrbEp_p4BhzjVAEKCIWq7pvFt7tLR5CiJbI5UGRI8TWcCQn7FVJzA8vYRPNFeJWaRMCwrl68u6E1RK9NdmlL4boM9-I2fn5oQ7jPwC4mq1CSqMK_4xsqn0sSrz5AUAYk6Q6uZ9Xehxk7yfGQmt6AQYPTEFGCaVPqJtymHX62Wn9tMWOyG4a_anWhDQJHOalkR8IOM64xSLr5cnVb2D7zuo6R3fLUMA-6kChRAYDDz7SLTyqoWav4MXQ5W3nxhOFjeHivvZy7rBw-rJdCPdkYNrvaxs-Fz5io5UuPFSt6xjgIOnXaZIpCqVHnzhREqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
💬
Support Bot:
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1784" target="_blank">📅 14:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SkCiJBRVZWCtSSzII7CQlndka1R6arae7Pn8MjcRFX6OOOr-BZpdwLTXA2pU78Hojj6hCXV9ISzULBAlK-UUhyIN0sjzrc8W_3VevMIJ-uNAEowj-UToy7r59jxvg1UxPYB1SiDI3WG4_bbJuqryeNQAKyvE58idE_hQSirlN2ep65d1dODXds6W21o0aqCTHd13Ij2XcjIbn7C3XnF0rJr_W5E_D0KJ5YlxpkihKKs7BgvAFFbrMBj3W-VP26ImOJj5JhsH-ees3s6unEc4gU7sCvVwEq9-gkJ3U4AVN4dKy5Ly45aVP03d7yopfTkaRAVhPQWPU9eBODsCGegX3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
WhiteAesther mobile 1.6.1 (stable)
دوستانی که منتظر اپدیت بودند الان میتونند اپدیت کنند
⚠️
✨
چه چیزی جدید است؟
🔗
زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی. حامل اول چیزی است که شبکهٔ شما می‌بیند و حامل دوم چیزی است که سایت‌ها می‌بینند.
مسیرها ← حامل ← «خودم انتخاب می‌کنم»
⚡️
سایفون بهتر
سایفون به سرورهای بیشتری دسترسی دارد و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد، پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
🤖
حالت خودکار (آزمایشی)
اگر روشنش کنید، برنامه خودش اتر، سایفون و تور را هم‌زمان امتحان می‌کند و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود. راهی که روی هر شبکه کار کرد را هم یادش می‌ماند و دفعهٔ بعد سریع‌تر وصل می‌شود.
فعلاً پیش‌فرض خاموش است تا بیشتر امتحان شود. برای روشن کردن: مسیرها ← حامل ← «خودکار (آزمایشی)»
🛠
اگر نسخهٔ آزمایشی ۱.۶.۰ را نصب کرده بودید و وصل نمی‌شدید، این نسخه آن مشکل را برطرف می‌کند.
💡
نکته
اگر اتر روی اینترنت شما وصل نشد، سایفون را امتحان کنید:
مسیرها ← حامل ← «خودم انتخاب می‌کنم» ← سایفون
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.1
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.1-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.1-universal.apk
روی نسخهٔ فعلی به‌روزرسانی می‌شود و تنظیمات شما می‌ماند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید (همراه اول، ایرانسل، وای‌فای خانگی و…).
@whitedns</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1778" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fbKAkaoP9wXd9puC3iL3FuLx2iblw_CMe_d0T54d3qgUwDGNOLpKeZLQCbfvP1jm8oMCXN4GTMUlkdrNeBd6MwK7CO_7OyCGcBDBVFwHOhNlkS7NHSsHt-oCDF6k-OoUgU916Z_GytuolKf9BH7Qfrbo8sf1fRyeK9MZit9-W_b3ezFny-AhbDNeUTX8m_NFxTggCpUD_NhaaFIKKfOSe3g6eIEU2H4rCEMmZyKp9LfKKMRhiTFs5umZTX-whaKPCHUZjOU46rDd53RZy0HO4MfUQ0ewNggWefG6v8xQ9OcIi7kObkJmF37jQNv9JNqlHLot5Ht_ASjvTrtJEYDTVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteAesther desktop  1.9.1 (stable)
🔥
دوستانی که منتظر اپدیت بودند الان دیگه میتونند اپدیت کنند
⚠️
پنج ایراد درست شد که سه‌تایشان را فقط وقتی می‌دیدید که شبکه سخت می‌شد.
دکمهٔ «یکی که کار می‌کند را پیدا کن» حالا واقعاً می‌گردد
تا امروز، جست‌وجو روی همان گزینهٔ اول می‌ایستاد و می‌گفت وصل شد — حتی وقتی نشده بود. هیچ‌وقت به سایفون، تور و شش ترکیب زنجیره‌ای نمی‌رسید. حالا هر راه را تا آخر امتحان می‌کند، و یکی را فقط وقتی قبول می‌کند که یک درخواست واقعی از آن رد شده و برگشته باشد.
⚠️
یک نشتی در حالت زنجیره‌ای بسته شد
اگر پروتکل را روی WireGuard یا MASQUE H3 گذاشته بودید و بعد سایفون یا تور را جلویش می‌گذاشتید، Aether از کنار آن کریر بیرون می‌رفت — یعنی از همان آدرسی که زنجیره برای پنهان کردنش وجود داشت. حالا پشت هر کریری خودکار روی MASQUE H2 قفل می‌شود.
به هر کریر همان‌قدر وقت داده می‌شود که لازم دارد
جست‌وجو قبلاً هر تلاش را سر ۹۰ ثانیه می‌برید، در حالی که سایفون در اولین اتصال روی شبکهٔ سخت تا ۵ دقیقه وقت می‌خواهد. نتیجه‌اش این بود که روی سخت‌ترین شبکه‌ها — دقیقاً جایی که این دکمه برای آن ساخته شده — هیچ‌وقت جواب نمی‌داد.
و چند چیز کوچک‌تر
• جست‌وجو ساعت نشان می‌دهد و از اول می‌گوید چقدر ممکن است طول بکشد
• سایفون می‌گوید اولین اتصالش روی شبکهٔ سخت چند دقیقه است، تا فکر نکنید هنگ کرده
• عمق جست‌وجو (از turbo تا thorough)
حالا واقعاً رعایت می‌شود
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.1
ویندوز → .exe
مک (اپل سیلیکون) → macos_arm64.dmg
مک (اینتل) → macos_x86_64.dmg
لینوکس → .AppImage یا .deb / .rpm
@whitedns</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/whitedns/1777" target="_blank">📅 14:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/GpVoa_oyNqYxsgCR0ZEw3whRu5luh044Subvly9u4TnelXaYxoh9TD55VD9rcMB3a06t3cq1x6rw5x1haQn-Guimget1vrxQEvgHPdlHrRtx7PDsP5u-ExyqldGdv2DWiQ1rf54iqtni7KpSp9fzRXHBoyW1ZbW5wXs6GqkmtqBi8aZBe2q9O47ACyoS3Dt4BI6wjbsJ2NgVpF8c81cP4WKNxNPKyCWmQZGmveEJFE2uf_X6mv3pxW9lAYTlNhg8lRTTy8AjcIUwO9Xz-xz1uOHBIMEqD-_DxCtTsRlwJeaIR6bvUQ82OUXeZru2X8H73R4A-BsygMa3wbpCvqoYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه پایدار WhiteAesther به‌زودی منتشر می‌شود!
🚀
تجربه‌ای سریع‌تر، امن‌تر و مطمئن‌تر در دسکتاپ و موبایل. منتظر باشید
💚
@whiteaesther</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1776" target="_blank">📅 13:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1772">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UC9tQbxuAe7Pha0uz4zkQ-D3ebqZrq-UVfh8p-r7UChS8MfIUc2XatKUjeVrVPUEs_nz6B08SpcXBz708zgP0YqIjCBBGVm6WoOEsa_kCPiq4M8qXzKBiJu0ft6wpxKO8Mcs80RKLDO1gNOXBdzKd7BusPZEV_1IBDLczRpO-3o0m2rJV6n4xBLo3B5u9amaNQZpGrhEcNymopcLiAlvjfECYBk7JXnqfpNlw5_XpKQPa8eKlPDXtinNOlNpnNWYqu26yYpiYLT1LauZ3jTnF8KKDyJbImDVNBvVMtZDaCwj5M6KoMXfXnqLcLNuX9Qr-iCEgMnYAMOUupRMjENkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاخره تصمیم گرفتیم برای WhiteDNS یه Patreon راه بندازم.
حدود ۷ ماهه که این پروژه رو با هزینهٔ شخصی جلو می‌بریم. توی این مدت بیش از ۱۰۰ سرور ساختیم و هزینه‌شون رو خودمون دادیم. از Conduit و DNSTT شروع کردیم، WhiteDNS رو ساختیم و در روزهای قطعی اینترنت هم با MasterDNS سرورهای بیشتری بالا آوردیم.
این هزینه‌ها صرفا جنبه مالی ندارند. مهمتر اینکه با استفاده از همین زیرساخت‌، سرویس‌های رایگان و با کیفیت بهتری برای افراد بیشتری ایجاد کردیم.
امروز WhiteDNS حدود ۱۰ هزار کاربر فعال روزانه داره که در مجموع، هر ماه نزدیک ۱ میلیون اتصال به سرویس‌هامون ثبت می‌کنن. همه سرویس‌ها کاملاً رایگان‌اند.
بعد از راه‌اندازی سرورهای اختصاصی داخل اپ، فهمیدیم وقتی زیرساخت دست خودمون باشه، می‌تونیم کیفیت سرویس رو خیلی بهتر کنیم. الان حدود ۱۵ سرور رو هر چهار ساعت یک‌بار روتیت می‌کنیم تا احتمال فیلترشدن کمتر و اتصال‌ها پایدارتر بشن.
این مسیر با کمک تیم ما در ایران جلو رفته؛ از تست و پیدا کردن مشکل تا پشتیبانی از کاربران.
برای ما Patreon کمک می‌کنه این کار رو پایدارتر ادامه بدیم: سرورهای بیشتری داشته باشیم، کاربران بیشتری رو پوشش بدیم و روی WhiteDNS و محصولات بعدی‌مون وقت بیشتری بذاریم.
اگر دوست دارید از اینترنت آزاد حمایت کنید، خوشحال می‌شیم کنارمون باشید:
https://www.patreon.com/cw/WhiteDNS</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/whitedns/1772" target="_blank">📅 16:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1771">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان :
⚠️
⚠️
اگر پست ها را کامل نخوندید . لطفا توی گروه ها پیام ندید . چون کاملا مشخص هست خیلی از دوستان حتی 10 ثانیه هم وقت نگذاشتند . این مدل پیام دادن فقط باعث گمراهی بقیه میشه . لطفا کاملا پست ها را مطالعه کنید .برنامه را کاملا بررسی کنید . تنظیمات متفاوت را انجام دهید وفقط با توجه به روشی که توی پست های بالا گفته شده گزارش کنید
سپاس</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/whitedns/1771" target="_blank">📅 16:08 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1770">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IqSNs2tX0xTgXZkIluzqdiHPKK3QM6hhu8HniusJQEobxJM5J3gA8_j1CcjLzYPgHZPLriTt2JMyOlxgBRFVURvw6O4NXdG7Bkqr39TtPnXnL-gPSnw1PMeDdkEqngoYRXN9BSvSK3Up8m4jlfWZpLh8v7u8ojW6uYEHFZGxWMkuIs2s5n-ltRhm_uDHAW1zd5UdNThF64BQXZ0XNdzF70EzETERI7R4i1FSRJq0vA_MInMv0itPPTBxztCPUYfyBLdmfsxc8ScT4Y8pgxt-pb48-WM06AmryO3FqkAH-vuAuCqGukz5dLJqkd3fqcclpkWACnKNHbeXHc9c3gWHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا توی نسخه اندروید هم شما حالت اتوماتیک دارید ، خودش می‌گرده و بهترین حالت را انتخاب می‌کنه و وصل میشه
#WhiteAesther_Mobile_1
.6.0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1770" target="_blank">📅 15:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1769">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی WhiteAesther Mobile  1.6.0
حالت خودکار: فقط دکمهٔ اتصال را بزنید
🔥
🔥
🔥
🔥
⚠️
این نسخه آزمایشی است و ممکن است باگ داشته باشد. داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود.
✨
چه چیزی جدید است؟
دیگر لازم نیست بدانید اتر، سایفون یا تور کدام روی اینترنت شما کار می‌کند. در حالت «خودکار» برنامه خودش اول اتر را امتحان می‌کند و اگر نشد سایفون و تور را، و راهی را انتخاب می‌کند که واقعاً اینترنت از آن رد شود.
راهی را هم که روی هر شبکه کار کرد یادش می‌ماند؛ دفعهٔ بعد روی همان وای‌فای یا همان سیم‌کارت خیلی سریع‌تر وصل می‌شود.
📱
استفاده
برای بیشتر کاربران خودکار از قبل روشن است؛ فقط دکمهٔ اتصال را بزنید.
اگر قبلاً حامل را دستی انتخاب کرده‌اید: تب «مسیرها» ← کارت «حامل» ← «خودکار (پیشنهادی)».
⏳
اولین بار روی یک اینترنت سخت ممکن است چند دقیقه طول بکشد؛ لطفاً صبر کنید. روی صفحه نوشته می‌شود الان کدام راه را امتحان می‌کند.
🐞
اگر مشکلی دیدید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده»، و بنویسید چه اینترنتی دارید.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.6.0
• بیشتر گوشی‌ها: WhiteAestherMobile-1.6.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.6.0-universal.ap
@whitedns</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/whitedns/1769" target="_blank">📅 15:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1768">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/d0PGvh5GUO23VA6QMXKkKW4pv4SeFfu_duwxZ2ZJLluy16ouBszaDLrumxjmRdUFjT0PQMHGVyPGF7Vq8IoxIpvEB_5DZRhR78ts5vIFEEFOQgqTgLuv2wcG9FjV53RJHT-5w5emZ5n6v6rba_hg7qTZ1RabyZ5p6jl80_PgU65kdOqJUSGQrkmbAFbS_zLl-B1tjK8TfFOv4cbjGODBz1yMC7ByKC_442y_RORe_9terGSD_D9a6gBfKsi94Yg282d-fWbLN-vefN0SgRz30Oq47-fCn69vg1NFKFSLr4bAzMghOphRHrHj8oafniK5R6Yb5IqRUTwQbm4wyOok9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی نسحه دسکتاپ یک گزینه اتوماتیک ما داریم . که خودش بهترین کانکشن را براتون پیدا میکنه
#
WhiteAesther_desktop_1
.9.0</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/whitedns/1768" target="_blank">📅 14:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1767">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان :
اموزش هایی که ما توی پست های کانال میگذاریم به خدا برای شماست - والا ما خودمون بلدیم !
خواهشا وقت بگذارید مطالعه کنید</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/whitedns/1767" target="_blank">📅 14:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1766">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-poll">
<h4>📊 توی این نسخه ازمایشی whiteaesther مشکل شما برای اتصال و استفاده از هوش مصنوعی حل شد ؟</h4>
<ul>
<li>✓ 😏اتصال اوکی شد ولی هوش مصنوعی کار نمیکنه</li>
<li>✓ ❤️هوش مصنوعی و اتصال اوکی شد</li>
<li>✓ کلا نتونستم وصل بشم😢</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1766" target="_blank">📅 14:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1762">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther mobile 1.5.0
⚠️
⚠️
⚠️
⚠️
این یک نسخهٔ آزمایشی است و ممکن است باگ داشته باشد. برای همین داخل برنامه اعلان به‌روزرسانی برایش نمی‌آید و فقط از لینک پایین نصب می‌شود. اگر به اتصال پایدار نیاز دارید، فعلاً روی نسخهٔ فعلی بمانید.
━━━━━━━━━━
✨
چه چیزی جدید است؟
۱
. زنجیره کردن دو حامل
حالا می‌توانید دو حامل از بین اتر، سایفون و تور را پشت سر هم وصل کنید، به هر ترتیبی که بخواهید. حامل اول چیزی است که شبکهٔ شما (اپراتور) می‌بیند و حامل دوم چیزی است که سایت‌ها و اینترنت می‌بینند.
۲. سایفون بهتر
سایفون حالا به سرورهای بیشتری دسترسی دارد (از جمله سرورهای داوطلبانهٔ Conduit) و زمان بیشتری برای پیدا کردن راه خروج می‌گذارد؛ پس روی شبکه‌هایی که قبلاً وصل نمی‌شد شانس بیشتری دارد.
━━━━━━━━━━
📱
چطور استفاده کنم؟
۱
. به تب «مسیرها» بروید و در صفحهٔ «چطور وصل می‌شود» پایین بیایید تا به کارت «حامل» برسید.
۲. در بخش «اول — چیزی که شبکه شما می‌بیند» حامل اول را انتخاب کنید.
۳. در بخش «بعد — چیزی که اینترنت می‌بیند» حامل دوم را انتخاب کنید. اگر فقط یک حامل می‌خواهید، «هیچ‌چیز دیگر» را بزنید.
۴. با دکمهٔ «ترتیب را جابه‌جا کن» جای دو حامل با یک لمس عوض می‌شود.
۵. «پوشش» باید روی «کل دستگاه» باشد؛ سایفون و تور در حالت «فقط پروکسی» اجرا نمی‌شوند.
۶. به «خانه» برگردید و وصل شوید. آنجا مسیر کامل نوشته می‌شود، مثلاً «متصل از طریق سایفون، بعد اتر»، و وضعیت هر حامل جداگانه نشان داده می‌شود.
━━━━━━━━━━
🔀
کدام ترکیب برای چه کاری؟
🔹
اتر ← سایفون
اتر وصل می‌شود ولی می‌خواهید سایت‌ها آی‌پی خارجی سایفون را ببینند، نه کلودفلر. کشور خروجی را هم می‌توانید در کارت «کشور خروجی» انتخاب کنید.
🔹
اتر ← تور
بیشترین حریم خصوصی، ولی کند.
🔹
سایفون ← اتر
وقتی اتر روی شبکهٔ شما مستقیم وصل نمی‌شود: سایفون راه را باز می‌کند و اتر از داخل آن بیرون می‌رود.
🔹
سایفون ← تور
وقتی تور مستقیم بسته است.
🔹
تور ← اتر / تور ← سایفون
برای شبکه‌هایی که فقط تور (با پل) از آن‌ها بیرون می‌رود. این دو ترکیب کمتر از بقیه آزمایش شده‌اند و نتیجهٔ شما برای ما خیلی ارزشمند است.
اگر یک ترتیب وصل نشد، «ترتیب را جابه‌جا کن» را بزنید و دوباره امتحان کنید. اینکه کدام ترتیب جواب بدهد به شبکهٔ شما بستگی دارد.
━━━━━━━━━━
💡
نکته‌ها
• زنجیره از یک حامل تنها کندتر است. اگر یک حامل به‌تنهایی برایتان کار می‌کند، همان را نگه دارید.
• وقتی اتر حامل دوم است، خودکار از H2 استفاده می‌کند و انتخاب پروتکل اثری ندارد.
• وقتی تور حامل دوم است، اسنوفلیک کار نمی‌کند؛ تور مستقیم، با پل obfs4 یا با پل‌هایی که به شما داده شده وصل می‌شود.
• اولین اتصال سایفون ممکن است چند دقیقه طول بکشد؛ صبر کنید.
• اگر برای سایفون کشوری انتخاب کرده‌اید و وصل نمی‌شود، «بهترین گزینهٔ موجود» را انتخاب کنید.
• اگر در تنظیمات اندروید «VPN همیشه روشن» همراه با «مسدود کردن اتصال‌های بدون VPN» روشن است، ممکن است سایفون و تور وصل نشوند؛ خاموشش کنید.
━━━━━━━━━━
🐞
گزارش باگ
اگر به مشکلی خوردید: تنظیمات ← تشخیص ← «ارسال برای توسعه‌دهنده». لطفاً بنویسید کدام ترکیب را امتحان کردید و روی چه اینترنتی بودید (همراه اول، ایرانسل، وای‌فای خانگی و…).
━━━━━━━━━━
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/tag/v1.5.0
⚠️
در صورت امکان ورژن قبلی را کاملا uninstall کنید و ورژن جدید را نصب کنید تا کاملا بروز شود
⚠️
• بیشتر گوشی‌ها: WhiteAestherMobile-1.5.0-arm64-v8a.apk
• اگر مطمئن نیستید: WhiteAestherMobile-1.5.0-universal.apk
روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان حفظ می‌شود. برای برگشتن به نسخهٔ پایدار (1.4.2) باید اول این نسخه را حذف کنید.
@whitedns</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1762" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1761">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🧪
نسخهٔ آزمایشی
WhiteAesther desktop 1.9.0
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️
این نسخه «آزمایشی» (Pre-release) است و ممکن است باگ داشته باشد. بنا به درخواست تعداد زیادی از شما، آن را زودتر در اختیارتان می‌گذاریم.
✅
اگر نسخهٔ فعلی برایتان بدون مشکل کار می‌کند، فعلاً نیازی به به‌روزرسانی ندارید.
✨
چه چیزهایی جدید است؟
🔗
زنجیر کردن دو راه خروج
حالا می‌توانید Aether، سایفون و تور را دوتادوتا و به هر ترتیبی پشت هم بگذارید. اولی شما را از شبکهٔ فیلترشده بیرون می‌برد، دومی تعیین می‌کند با چه IP و از چه کشوری دیده شوید.
مثلاً Aether ← سایفون: سرعت Aether برای بیرون رفتن، و کشور خروجِ سایفون.
🔍
دکمهٔ «یکی که کار می‌کند را پیدا کن»
اگر نمی‌دانید روی شبکهٔ شما کدام راه جواب می‌دهد، اپ خودش همه را یکی‌یکی امتحان می‌کند و اولی را که وصل شد نگه می‌دارد.
🟢
سایفون خیلی بهتر وصل می‌شود
خیلی‌ها گفته بودند با اپ خود سایفون وصل می‌شوند ولی با حالت سایفونِ ما نه. علتش را پیدا کردیم: سایفونِ ما نمی‌توانست از پروکسی‌های داوطلبانهٔ خود سایفون (in-proxy) استفاده کند، یعنی همان راهی که در ایران بیشتر از همه جواب می‌دهد. فهرست سرورهایش هم به‌روز نمی‌شد. هر دو مشکل برطرف شد و سایفون حالا برای وصل شدن تا ۵ دقیقه صبر می‌کند (قبلاً ۲ دقیقه بود).
📥
دانلود:
https://github.com/WhiteDNS/WhiteAesther/releases/tag/v1.9.0
⚠️
دوستان حتما  delete cache/data را بزنید تا کاملا بروز از برنامه استفاده کنید
⚠️
🪟
ویندوز: WhiteAesther_1.9.0_windows_x86_64.exe
🍎
مک با چیپ M1 و جدیدتر: WhiteAesther_1.9.0_macos_arm64.dmg
🍎
مک اینتل: WhiteAesther_1.9.0_macos_x86_64.dmg
🐧
لینوکس: فایل AppImage یا deb یا rpm (نسخهٔ x86_64 یا arm64)
🐞
اگر به مشکلی خوردید:
دکمهٔ Advanced ← عیب‌یابی ← در بخش «گزارش»، دکمهٔ «ذخیرهٔ گزارش» یا «کپی» را بزنید و برای ما بفرستید. آدرس‌های IP به‌طور پیش‌فرض در گزارش پنهان می‌شوند.
📘
آموزش نسخهٔ 1.9.0
١) کجاست؟
بالای برنامه دکمهٔ Advanced را بزنید ← از منوی کنار، «مسیرها و پروتکل‌ها» ← کارت «راه خروج».
٢) یک راه خروج (مثل قبل)
در ردیف «خروج از این شبکه با» یکی را انتخاب کنید (Aether، سایفون یا تور) و ردیف «و سپس خروج از» را روی «هیچ‌چیز دیگر» بگذارید.
٣) زنجیر کردن دو راه خروج
در ردیف اول چیزی را بزنید که شما را از شبکه بیرون می‌برد، و در ردیف دوم چیزی که می‌خواهید IP و کشورِ خروجتان مالِ آن باشد. زیر این دو ردیف یک کادر دقیقاً می‌گوید این ترکیب چه چیزی به شما می‌دهد و چه چیزی نه.
💾
برای اینکه انتخابتان بعد از بستن برنامه هم بماند، «ذخیرهٔ پروفایل» را بالای صفحه بزنید.
چند ترکیب کاربردی:
• Aether ← سایفون: وقتی Aether وصل می‌شود ولی IP از کشور دیگری می‌خواهید. کشور را از «کشور خروج» انتخاب کنید (فهرست کشورها بعد از اولین اتصال سایفون ظاهر می‌شود).
• سایفون ← Aether: وقتی Aether به‌تنهایی وصل نمی‌شود ولی سایفون می‌شود. خروجتان همچنان نزدیک خودتان است و کشورتان عوض نمی‌شود. شرطش این است که قبلاً حداقل یک بار با خود Aether (بدون زنجیره) وصل شده باشید.
• تور ← سایفون: وقتی نه Aether و نه سایفون به‌تنهایی وصل نمی‌شوند. کندتر است، ولی یک راه دیگر است.
نکته: وقتی تور نفر دوم زنجیره است، از «پل‌ها» استفاده نمی‌کند؛ کارِ بیرون رفتن را نفر اول انجام داده.
نکته: زنجیره‌ای که سایفون یا تور در آن باشد UDP را عبور نمی‌دهد. سایت‌ها و بیشتر برنامه‌ها عادی کار می‌کنند، ولی بعضی تماس‌های صوتی و تصویری یا بازی‌های آنلاین ممکن است کار نکنند.
٤) پیدا کردن خودکار
در همان صفحه، کادر سبز «نمی‌دانید کدام کار می‌کند؟» را پیدا کنید و «یکی که کار می‌کند را پیدا کن» را بزنید.
اپ اول تک‌ها را امتحان می‌کند (Aether، سایفون، تور) و فقط اگر هیچ‌کدام وصل نشد سراغ ترکیب‌ها می‌رود. به هرکدام تا ۹۰ ثانیه فرصت می‌دهد و نتیجهٔ هر تلاش را همان‌جا نشان می‌دهد. هر وقت خواستید، «توقف جستجو» را بزنید.
٥) درباره سایفون
اولین اتصال سایفون ممکن است چند دقیقه طول بکشد، مخصوصاً وقتی از طریق پروکسی‌های داوطلبانه وصل می‌شود. عجله نکنید؛ تا ۵ دقیقه صبر می‌کند.
⚠️
مشکلات شناخته‌شده
• زنجیره‌هایی که به Aether ختم می‌شوند (مثل سایفون ← Aether) ممکن است بعد از چند ثانیه قطع و دوباره وصل شوند (وضعیت reconnecting). روی رفعش کار می‌کنیم.
• ترکیب سایفون ← تور، و قابلیت Kill switch (قطع ترافیک هنگام افتادن تونل) در حالت زنجیره، هنوز کمتر آزمایش شده‌اند.
ممنون که با ما هستید
🤍
گزارش‌های شما مستقیم به بهتر شدن نسخهٔ پایدار کمک می‌کند.
@whitedns</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1761" target="_blank">📅 11:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1759">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.   بعدش دوباره وصل بشید.   خود اپ هم…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/whitedns/1759" target="_blank">📅 15:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1758">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IHFTSLbUaGEJfxGkfBR_9opMOK9YzzatHWC2YSP3I8dmD6iGDmX0MLUfeHzIAoL3NFQuvDFQwoNL8tgfIdYa4TdObEr9tGY4SYKpDBS1tXUZ58JXTPZE-9iUck5BlDBm0FgC1VGG1GNbtjXZjtOxRUSKNomFCBQdAnZypvvY3qnSQPVKMKV0Lecsb_M-49pFZ7NQH41rG5grD1cpWM9o8CZD1_ElTU2-_LeVrRhOW-1ArJxhKwsDsCIYZJq9lD3XPyC5Y8Uj149xjgSWR4RysfAv-NEOCBBuiRH0iBE3cdgkMkjH5aVHbdcmYE9BWxcrxAzX4FWpFh8sc4mDoXHxrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه
WhiteVPN Desktop v1.0.22 منتشر شد
این نسخه چند مشکل مهم را برطرف می‌کند که می‌توانست باعث
عدم اتصال، ذخیره‌نشدن تنظیمات و ناسازگاری برخی کانفیگ‌ها
شود. همچنین از این نسخه،
سرورهای اختصاصی WhiteVPN
هم به نسخه دسکتاپ اضافه شده‌اند.
━━━━━━━━━━━━━━━━━━
در این نسخه چه مواردی اضافه شد و چه باگ هایی رفع شد :
🖥
سرورهای اختصاصی و عمومی، هر دو در دسکتاپ
تا امروز نسخه دسکتاپ فقط از سرورهای عمومی استفاده می‌کرد، در حالی که نسخه موبایل روی سرورهای اختصاصی قرار داشت.
حالا هر دو فهرست داخل برنامه در دسترس هستند و از صفحه
Subscriptions
می‌توانید مشخص کنید از کدام منبع متصل شوید.
نصب‌های جدید به‌صورت پیش‌فرض با
فهرست اختصاصی
شروع می‌شوند.
اگر یکی از فهرست‌ها در دسترس نباشد، برنامه دیگر همان‌جا متوقف نمی‌شود و به‌صورت خودکار منابع دیگر را بررسی می‌کند؛ از جمله:
• فهرست داخلی دیگر
• سابسکریپشن‌های شخصی شما
• کانفیگ‌هایی که دستی وارد کرده‌اید
برنامه همچنین اعلام می‌کند اتصال از کدام منبع انجام شده است. انتخاب اصلی شما تغییر نمی‌کند و در اتصال بعدی دوباره همان منبع امتحان خواهد شد.
━━━━━━━━━━━━━━━━━━
🛠
رفع مشکل «هیچ سروری وصل نمی‌شود»
در نسخه‌های قبلی، اگر روی فهرست داخلی فیلتر
کشور
یا
نوع اتصال
انتخاب می‌کردید و بعد به سابسکریپشن شخصی خودتان می‌رفتید، همان فیلتر روی فهرست جدید هم اعمال می‌شد.
در نتیجه ممکن بود تمام سرورهای شما رد شوند، بدون اینکه مشخص باشد مشکل از کجاست.
حالا هر فهرست تنظیمات و فیلترهای خودش را نگه می‌دارد.
وقتی وارد فهرست دیگری می‌شوید، آن فهرست از حالت
Automatic
شروع می‌شود و وقتی برمی‌گردید، انتخاب قبلی شما همچنان حفظ شده است.
━━━━━━━━━━━━━━━━━━
⚙️
رفع مشکل ذخیره‌نشدن تنظیمات
برخی گزینه‌های صفحه Settings تغییر می‌کردند، اما پس از خروج از صفحه به حالت قبلی برمی‌گشتند.
این مشکل برای گزینه‌هایی مثل:
Amnezia Noise
و
این‌ها مستقیم خارج شوند
برطرف شده است.
حالا تغییرات مثل نسخه موبایل، به‌درستی ذخیره می‌شوند.
━━━━━━━━━━━━━━━━━━
🔗
پشتیبانی بهتر از کانفیگ‌ها
پشتیبانی از موارد زیر اصلاح و کامل‌تر شده است:
anytls
socks
HTTP Proxy
قبلاً کانفیگ‌های anytls ممکن بود اصلاً در فهرست نمایش داده نشوند.
کانفیگ‌های socks و HTTP Proxy هم ذخیره و نمایش داده می‌شدند، اما هنگام اتصال به‌درستی کار نمی‌کردند.
این مشکلات در نسخه جدید برطرف شده‌اند.
━━━━━━━━━━━━━━━━━━
🐧
رفع مشکل آیکون Tray در لینوکس
در برخی نسخه‌های لینوکس، کلیک روی آیکون WhiteVPN کنار ساعت باعث بازگشت پنجره برنامه نمی‌شد.
این مشکل در نسخه 1.0.22 برطرف شده است.
━━━━━━━━━━━━━━━━━━
⚠️
کاربران لینوکس، این بخش را حتماً بخوانید
نام فایل‌های لینوکس تغییر کرده است.
فایل‌های بدون پسوند amd64 و arm64 حالا از
WebKitGTK 4.1
استفاده می‌کنند و مناسب سیستم‌های جدید هستند، از جمله:
• Ubuntu 24.04 و جدیدتر
• Debian 13
• Fedora 40 و جدیدتر
اگر از
Ubuntu 22.04
یا
Debian 12
استفاده می‌کنید، نسخه webkit40 را دانلود کنید:
WhiteVPN-Desktop-1.0.22-linux-amd64-webkit40.deb
در نسخه‌های قبلی، نام‌گذاری فایل‌های Linux بین amd64 و arm64 یکسان نبود و همین موضوع می‌توانست باعث انتخاب فایل اشتباه و خطای Dependency شود.
این نام‌گذاری حالا اصلاح شده است.
✅
برای کاربران Linux با پردازنده Intel/AMD، ساده‌ترین گزینه همچنان
AppImage
است:
WhiteVPN-Desktop-1.0.22-linux-amd64.AppImage
━━━━━━━━━━━━━━━━━━
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
📥
راهنمای سریع انتخاب فایل
🪟
Windows — Intel / AMD
windows-x64
🪟
Windows — ARM / Snapdragon
windows-arm64
🍎
Mac — Apple Silicon / M1 و جدیدتر
macos-arm64
🍎
Mac — Intel
macos-amd64
🐧
Ubuntu 24.04+ / Debian 13
linux-amd64.deb
🐧
Ubuntu 22.04 / Debian 12
linux-amd64-webkit40.deb
🐧
Fedora / RPM-based Linux
linux-amd64.rpm
━━━━━━━━━━━━━━━━━━
📢
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1758" target="_blank">📅 14:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1757">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💬
ما قرار داریم روزی ۴ بار سرور های اختصاصی رو عوض کنیم تا همیشه وصل بمونید و سرور ها فیلتر نشن.
✍️
اگر یکدفع دیدید که سرور اختصاصی قطع شد، برید با قسمت ساسکریپشن، بزنید روی ۳نقطه کنار سرور اختصاصی و تازه سازی رو بزنید.
بعدش دوباره وصل بشید.
خود اپ هم هر ۳۰دقیقه اتوماتیک ساب رو آپدیت میکنه.
کشور ها ثابت میمونه و فقط آی‌پی ها عوض میشن.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/whitedns/1757" target="_blank">📅 10:27 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1756">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
👆
دوستانی که این ورژن رو قبلا دانلود کرده بودند. دوباره نصبش کنید چون سرور های عمومی یک باگی داشت که رفع شد.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/whitedns/1756" target="_blank">📅 10:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1751">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.7-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/whitedns/1751" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/whitedns/1751" target="_blank">📅 10:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1750">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuvoqTzHHetC9haTpTypCq9pP7BcJUvz_3kKH474yCJZ4QD3LezC1B5po22zQYW4ncWw_UhkZFjgByfBdR2myLqT7OSjfcqXb_tkwZ_-Y5WjbNTNLa0p7o4SmMlOQ_rOOJofplTvaRV9ymAEsO4tMsB73eptzSh9L7xBzPSO_yYqV-nZU9-df7bkOuoVPxjwASH3WlZO48Doj9Ua3JxroDmU2bdVKAGrHrF5AfyaUm6OjyGYbJyLIy2Nb12LvRXhda3XzmRdlb43kOpyfXGHFDEveF_F0UVcChvn13iCiCXI3RdiDvSwm_-hlKWd18W3dKZg4zx-yk7eEQg8Z40yyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه WhiteVPN 1.6.7
✍️
تغییرات این نسخه
🟢
توی این نسخه، ما سرور های اختصاصی خودمون رو هر چند ساعت یکبار تازه میکنیم تا پایداری بیشتر بشه. و فیلترنشن.
🟢
۳ کشور جدید به سرور های اختصاصی اضافه کردیم
🇺🇸
🇩🇪
🇸🇬
🟢
با کمک تیم پس‌کوچه
@paskoocheh
یکسری حفره امنیتی رو رفع کردیم
🟢
حالا میتونید همزمان تست سرعت بگیرید و هرکدوم رو خواستید کنسل کنید.
پیشنهاد میکنم حتما این ورژن رو بگیرید تا آپدیت های سرور های اختصاصی براتون بیاد.
⭐️
دانلود کنید، به بقیه معرفی کنید و نتیجه تست هاتون رو برای ما بفرستید تا مارو هم خوشحال کنید.
💻
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/whitedns/1750" target="_blank">📅 10:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1749">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دوستان عزیز من مجبور به پاک کردن ورژن آخر شدم. ساب های عمومی کار نمیکردند داخل اپ. به زودی آپدیت میکنم و دوباره پست رو میفرستم براتون.
سرور های اختصاصی توی این ورژن جدید که دانلود کردید باید درست کار کنه.
شرمنده همگی
❤️</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/whitedns/1749" target="_blank">📅 09:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1746">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭐️
امروز یک آپدیت جدید برای WhiteVPN داریم
توی این ورژن، یکسری تغییرات امنیتی داشتیم به کمک بچه های تیم پسکوچه.
👨‍💻
مهمتر از همه، سرور های اختصاصی رو اپدیت میکنیم تا هر چند ساعت آپ‌پی های جدید بهتون بده.
این یکم هزینه های مارو بیشتر میکنه اما اینطوری کار فیلترچی رو سخت‌تر میکنیم و سرویس ها دیگه فیلتر نمیشن.
🥺
دیروز مادربزرگ خودم برای اولین بار از ابزار هامون استفاده می‌کرد و چنان دعای خیری برام کرد که انرژی ۲۰برابر شده.
هیچی چیزی ارزشش از این بیشتر نیست که بتونیم با عزیز هامون در ارتباط بمونیم.
هوای هم دیگرو داشته باشید
ارادت
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1746" target="_blank">📅 06:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1745">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">با WhiteAesther به Tor و Psiphon وصل شو!
🔥
https://youtu.be/WiybhJ7ylps
آخرین نسخه WhiteAesther
🦋
WhiteAesther Windows
WhiteAesther Android</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1745" target="_blank">📅 02:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1743">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚀
وایت‌اِستر موبایل نسخهٔ 1.4.2 منتشر شد
WhiteAesther Mobile v1.4.2
حالا سه راه خروج دارید، نه یکی.
از این نسخه اگر شبکه جلوی یک مسیر را گرفت، بدون نصب برنامهٔ دیگری می‌توانید مسیر بعدی را امتحان کنید.
⚡️
اِتر | Aether
همان موتور اصلی برنامه؛ سریع‌ترین مسیر و حالت پیش‌فرض.
🌐
سایفون |Psiphon
از شبکهٔ سایفون استفاده می‌کند. کمی کندتر است، اما ممکن است روی شبکه‌هایی که اِتر جواب نمی‌دهد متصل شود.
🧅
تور | Tor
عبور از سه بازپخش؛ مناسب زمانی که حریم خصوصی اهمیت بیشتری دارد. کندترین گزینه بین سه مسیر.
✅
تمام قابلیت‌های قبلی با هر سه مسیر کار می‌کنند:
• زنجیرهٔ خروج
• تقسیم ترافیک
• قوانین مسیریابی
• کلید قطع اضطراری
✨
تغییرات مهم نسخهٔ 1.4.2
• انتخاب کشور خروجی برای سایفون
• دریافت پل تور با یک دکمه
• امکان فراموش کردن نقطهٔ پایانی و جست‌وجوی دوباره
• رفع مشکل ثابت ماندن آدرس بدون تونل
• رفع نمایش اشتباه آی‌پی در حالت سایفون
• اضافه شدن سه موتور با فقط حدود ۱۴ مگابایت افزایش حجم
⬇️
دانلود نسخه موبایل
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
📖
آموزش کامل استفاده
برای مشاهده، بخش زیر را باز کنید
👇
۱️⃣ انتخاب راه خروج
وارد این بخش شوید:
پیشرفته ← مسیرها و پروتکل‌ها
در کارت
«راه خروج»
سه گزینه دارید.
اِتر
| Aether
همان حالت قبلی و سریع‌ترین مسیر.
سایفون
|Psiphon
پیدا کردن خودکار مسیر و امکان انتخاب کشور خروج.
تور
| Tor
مناسب‌تر برای ناشناس‌ماندن، اما کندتر.
مسیر موردنظر را انتخاب کنید و سپس
اتصال
را بزنید.
⚠️
در حالت سایفون و تور، تنظیمات نقطهٔ پایانی و انتخاب پروتکل اثری ندارند؛ این موارد فقط مخصوص اِتر هستند.
━━━━━━━━━━
۲️⃣ انتخاب کشور خروج در سایفون
بعد از انتخاب سایفون، گزینه
«کشور خروج»
ظاهر می‌شود.
🔸
در اولین استفاده ممکن است فقط
«بهترین گزینه موجود»
نمایش داده شود.
این طبیعی است؛ فهرست کشورها بعد از اولین اتصال موفق دریافت می‌شود.
🔸
انتخاب کشور یک ترجیح است، نه تضمین.
بعضی کشورها ظرفیت کمتری دارند و ممکن است اتصال به آن‌ها موفق نشود.
اگر یک کشور متصل نشد، گزینه
«بهترین گزینه موجود»
را انتخاب کنید تا سایفون از تمام سرورهای قابل دسترس استفاده کند.
🔄
تغییر کشور نیازمند اتصال مجدد است.
━━━━━━━━━━
۳️⃣ تور و پل‌ها
بعد از انتخاب تور، بخش
«پل‌ها»
نمایش داده می‌شود.
خاموش
اتصال مستقیم به تور.
همراه برنامه
استفاده از پل‌های داخلی.
گزینه‌های ترابرد:
obfs4
snowflake
meek
چسبانده‌شده
برای وارد کردن پل شخصی.
در این حالت می‌توانید پل را دستی وارد کنید یا گزینه
«از تور پل بگیر»
را بزنید.
🔑
هنگام دریافت پل، کشوری را وارد کنید که از آن متصل هستید.
مثال:
IR
منظور کشور فعلی شماست، نه کشوری که می‌خواهید آی‌پی خروجی آن را داشته باشید.
💡
ابتدا با اِتر یا سایفون متصل شوید و بعد پل بگیرید.
پل‌های جدید به فهرست اضافه می‌شوند و موارد قبلی حذف نمی‌شوند.
━━━━━━━━━━
۴️⃣ نکته مهم درباره تور
تور فقط ترافیک زیر را عبور می‌دهد:
TCP
برنامه درخواست‌های ناسازگار را مدیریت می‌کند تا اتصال بی‌دلیل معلق نماند.
برای بازی، تماس تصویری و استفاده‌های حساس به تأخیر، اِتر یا سایفون انتخاب مناسب‌تری هستند.
━━━━━━━━━━
۵️⃣ اگر راه خروج قطع شود
اگر پردازش سایفون یا تور متوقف شود، وایت‌اِستر آن را تشخیص می‌دهد، وضعیت را
«خطا»
نشان می‌دهد و زنجیره اتصال را می‌بندد.
اگر گزینه
«اگر تونل قطع شد، ترافیک را مسدود کن»
فعال باشد، ترافیک بسته باقی می‌ماند تا خارج از تونل ارسال نشود.
برای بازگرداندن اتصال، ابتدا
قطع اتصال
را بزنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1743" target="_blank">📅 19:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1741">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚀
وایت‌اِستر دسکتاپ نسخهٔ ۱.۸.۰ منتشر شد
WhiteAesther Desktop v1.8.0
حالا سه راه خروج دارید، نه یکی.
تا امروز ترافیک شما از مسیر کلادفلر عبور می‌کرد. این مسیر سریع است، اما معمولاً کشور خروج شما را تغییر نمی‌دهد.
از نسخهٔ ۱.۸.۰ دو مسیر جدید اضافه شده است:
⚡️
اِتر
Aether
همان حالت قبلی و سریع‌ترین گزینه برای استفاده روزمره.
🌐
سایفون
Psiphon
مسیر مناسب را پیدا می‌کند و امکان انتخاب کشور خروج را می‌دهد.
در حال حاضر
۲۵ کشور
در دسترس است.
🧅
تور
Tor
ترافیک را از چند بازپخش عبور می‌دهد؛ مناسب‌تر برای حریم خصوصی، اما کندتر.
پل نیز پشتیبانی می‌شود و امکان دریافت خودکار پل وجود دارد.
✅
هر سه مسیر با قابلیت‌های زیر کار می‌کنند:
• زنجیرهٔ خروج
• کل دستگاه
• تونل کامل
تنظیمات قبلی شما تغییری نکرده است. اگر چیزی را تغییر ندهید، برنامه مثل قبل کار خواهد کرد.
⬇️
دانلود نسخه دسکتاپ
https://github.com/WhiteDNS/WhiteAesther/releases/latest
📖
آموزش کامل مسیرهای خروج جدید
برای مشاهده، بخش زیر را باز کنید
👇
۱️⃣ انتخاب راه خروج
وارد این بخش شوید:
پیشرفته ← مسیرها و پروتکل‌ها
در کارت
«راه خروج»
سه گزینه دارید.
اِتر
Aether
همان حالت قبلی و سریع‌ترین مسیر.
سایفون
Psiphon
پیدا کردن خودکار مسیر و امکان انتخاب کشور خروج.
تور
Tor
مناسب‌تر برای ناشناس‌ماندن، اما کندتر.
مسیر موردنظر را انتخاب کنید و سپس
اتصال
را بزنید.
⚠️
در حالت سایفون و تور، تنظیمات نقطهٔ پایانی و انتخاب پروتکل اثری ندارند؛ این موارد فقط مخصوص اِتر هستند.
━━━━━━━━━━
۲️⃣ انتخاب کشور خروج در سایفون
بعد از انتخاب سایفون، گزینه
«کشور خروج»
ظاهر می‌شود.
🔸
در اولین استفاده ممکن است فقط
«بهترین گزینه موجود»
نمایش داده شود.
این طبیعی است؛ فهرست کشورها بعد از اولین اتصال موفق دریافت می‌شود.
🔸
انتخاب کشور یک ترجیح است، نه تضمین.
بعضی کشورها ظرفیت کمتری دارند و ممکن است اتصال به آن‌ها موفق نشود.
اگر یک کشور متصل نشد، گزینه
«بهترین گزینه موجود»
را انتخاب کنید تا سایفون از تمام سرورهای قابل دسترس استفاده کند.
🔄
تغییر کشور نیازمند اتصال مجدد است.
━━━━━━━━━━
۳️⃣ تور و پل‌ها
بعد از انتخاب تور، بخش
«پل‌ها»
نمایش داده می‌شود.
خاموش
اتصال مستقیم به تور.
همراه برنامه
استفاده از پل‌های داخلی.
گزینه‌های ترابرد:
obfs4
snowflake
meek
چسبانده‌شده
برای وارد کردن پل شخصی.
در این حالت می‌توانید پل را دستی وارد کنید یا گزینه
«از تور پل بگیر»
را بزنید.
🔑
هنگام دریافت پل، کشوری را وارد کنید که از آن متصل هستید.
مثال:
IR
منظور کشور فعلی شماست، نه کشوری که می‌خواهید آی‌پی خروجی آن را داشته باشید.
💡
ابتدا با اِتر یا سایفون متصل شوید و بعد پل بگیرید.
پل‌های جدید به فهرست اضافه می‌شوند و موارد قبلی حذف نمی‌شوند.
━━━━━━━━━━
۴️⃣ نکته مهم درباره تور
تور فقط ترافیک زیر را عبور می‌دهد:
TCP
برنامه درخواست‌های ناسازگار را مدیریت می‌کند تا اتصال بی‌دلیل معلق نماند.
برای بازی، تماس تصویری و استفاده‌های حساس به تأخیر، اِتر یا سایفون انتخاب مناسب‌تری هستند.
━━━━━━━━━━
۵️⃣ اگر راه خروج قطع شود
اگر پردازش سایفون یا تور متوقف شود، وایت‌اِستر آن را تشخیص می‌دهد، وضعیت را
«خطا»
نشان می‌دهد و زنجیره اتصال را می‌بندد.
اگر گزینه
«اگر تونل قطع شد، ترافیک را مسدود کن»
فعال باشد، ترافیک بسته باقی می‌ماند تا خارج از تونل ارسال نشود.
برای بازگرداندن اتصال، ابتدا
قطع اتصال
را بزنید.
❓
اگر سؤال یا مشکلی داشتید، در گروه وایت‌دی‌ان‌اس مطرح کنید.
@whitedns</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1741" target="_blank">📅 17:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1740">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Rw30McuNjLlNbrUUTfToHwYIQphKd66sciPzZpD4Xv0mGkAI-fU_Ar7Yf9LyBoF8rLvCChf2VY7AS4bTQ7CX-6UzKQI_O9yMd0cMXeJJJqcU-qlIO7EIiKx5p4BDYywRfyAJOOUZ-bxIQCra7JFKCOPSKQsbADIiRs9P3EmN-lpcuTWOh66aXsq18YpRyCm2YRsnUn4BVuM6duavY7hlb46-KQy32_prlBG-y5Srxe1ubXaWeUpjEpjXCc-CSjoYvLkEop37YxsfRxXXRY09umFSOVEQyO0_S2sVZFwUN5SLYKsLGPLyVIQ_Tbed6GdKebvn-ZNsEmNuO0AfhONIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Coming soon
🔥
@whitedns</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1740" target="_blank">📅 11:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-poll">
<h4>📊 سرور های اختصاصی براتون وصل میشن؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1738" target="_blank">📅 11:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZ7SdijCc2yUZw8e-QjMGmSb-4vFurSptQ5uLjfMJHkVSfQWQwip_l1T1vVroreEQDaY_choyb5KrFFZtd-391yStQwWVMLa8FvWzLWfmP9qtmZk9EXHYgzaIkSr5ICXYaORRv5pV_6N9B5KEjGRPBz9TKdFtoscHp_jOlQ6vaOJFRWoWfRItfDsCUmHOSxyNlT8dhEF46yZMJAN8oTDSFb_uf0zeIw8RYjNIfb8NmI5HqQ8SE3xso7g4K7i3DNQ-CSA7br8nTOTmXfq8dNG70gkyyloGs9piA_YaZ3k_kLT2vypwbBLHkwRwtMIlMvwfzWQy8NZW3sHrhiP4Hn1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
دانلود ابزارهای WhiteDNS
⛏
اپلیکیشن ها
📱
WhiteAesther
دانلود موبایل
•
دانلود دسکتاپ
🛡
WhiteVPN
دانلود موبایل
•
دانلود دسکتاپ
🌐
WhiteDNS
مناسب دوران قطعی
دانلود اندروید
•
دانلود دسکتاپ
🔎
WhiteDNS Clean IP + Resolver Finder
دانلود برای موبایل و دسکتاپ
🍎
CoreForge VPN + DNS
دریافت نسخه iOS از TestFlight
🤖
ربات‌های WhiteDNS
💬
Support Bot:
@WhiteDnsResponder_bot
🔗
WhiteDnsChain
@WhiteDnsChainbot
🎓
آموزش‌ها و راهنماها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVP
🛡
آموزش کامل WhiteVPN
📱
آموزش کامل WhiteAesther
🌐
آموزش کامل WhiteDNS
🍎
آموزش کامل CoreForge
🔎
آموزش کامل اسکنر WhiteDNS
🔗
راهنمای کامل ربات WhiteDnsChain
💬
راهنمای استفاده از ربات WhiteDNS
@whitedns</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/1737" target="_blank">📅 08:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">از دیروز تا حالا تعداد اتصال‌ها چند برابر شده؛ از کامنت‌هاتون هم معلومه که این تغییر رو حس کردید
🙌
جالبه بدونید ما با فقط ۱۰ تا سرور و ماهی ۱۵۰ دلار هزینه، داریم هر هفته به حدود ۵۰ هزار کاربر فعال داخل اپ WhiteVPN، رایگان سرویس می‌دیم!
این تازه بدون حساب کردن کاربرهای ویندوزه؛ با اون‌ها، آمار خیلی بیشتر هم می‌شه.
😑
آدم این عددها رو که می‌بینه، بیشتر حرص پول‌هایی رو می‌خوره که تا امروز به فیلترشکن‌فروش‌ها داده
واقعاً ممنون از انرژی مثبتی که بهمون می‌دین و وقتی که می‌ذارید تا تجربه‌هاتون رو زیر پست‌ها بنویسید. همین بازخوردها کمک می‌کنه بفهمیم کجا خوب پیش رفتیم و کجا هنوز باید بهتر بشیم.
به‌زودی WhiteVPN Desktop رو هم با سرورهای اختصاصی آپدیت می‌کنیم تا کاربرهای دسکتاپ هم از این اتصال‌ها استفاده کنن.
🎮
یه سورپرایز هم برای کاربرهای WhiteAesther و بچه‌هایی داریم که دنبال سرویس مخصوص گیمینگ بودن
ممنون که کنارمونید
🤍
تیم WhiteDNS</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1736" target="_blank">📅 06:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1735">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ما سعی میکنیم هر ۲
یا
۳ روز سرور هارو عوض کنیم تا تا جای ممکن از فیلتر شدن آی‌پی ها جلوگیری کنیم
.
همچنین کشور های دیگه رو هم اضافه میکنیم تا آپشن های بیشتری داشته باشید
❤️
🛡
سرور های اختصاصی رایگان، امن و مدیریت شده توسط
تیم ما هستن.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1735" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1734">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
لطفا تست کنید و نتیجه رو با ما به اشتراک بگذارید. امیدوارم همه بتونید به سرور های اختصاصی وصل بشید.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/1734" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">36.1 MB</div>
</div>
<a href="https://t.me/whitedns/1729" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/whitedns/1729" target="_blank">📅 14:49 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btuJUua901dFZv-Dj9zn8ARpFjjXugY9pQCEt-d9qghvsK9eOinm1_iPnllrE4P5ikpXEo9TLOo5fM_QwMWL3brAjos-hifLVGbSxRDiexQRiD0TSob9rRWwokTwVDGwaGySThW-y5z6j9jDBIvy1Z5J0kaSo5IV89gyrjGtKDdBswKHvDeDMEH6dGeFO7e_LWK7-n1yCB9MCxSWnUBWpdXJFIt50Gcogm8jbXOETAkA_-qz_29B2nYD3w8zWcK9J_Gdua86coJHfJ4_nUPFnHEaLMt0Q8Mz9U1CPzJYxkiZMePsiziTjkGBpId7MDLRJMYSKPSwXg-9cEP_4PJ4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
انتشار نسخه جدید WhiteVPN 1.6.6
🟢
توی این نسخه ما ۱۰سرور اختصاصی WhiteVPN گذاشتیم. همه داخل فنلاند هستند.  بعد از تست کردن سرور کشور های دیگه رو هم اضافه میکنیم.
در صورت فیلتر شدن سرویس ها، سرور هارو جایگزین میکنیم.
🟢
توی این ورژن، اپ اول سعی میکنه به سرور های اختصاصی WhiteVPN وصل بشه، در صورتی که امکان‌پذیر نبود بعد سرور های عمومی رو امتحان میکنیم.
📱
دانلود آخرین نسخه از گیتهاب
✍️
دوستانی که ورژنی که دقیقه هایی پیش فرستادیم رو گرفتن، دوباره دانلود و نصب کنید.
❤️
نتیجه اتصال رو برای ما بفرستید.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1728" target="_blank">📅 14:46 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1725">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✍️
یه زودی یک آپدیت جدید داریم برای WhiteVPN روی اندروید.
توی این ورژن سرور های اختصاصی WhiteVPN رو اضافه کردیم. برای شروع ۱۰تا سرور اختصاصی فنلاند به صورت آزمایشی اضافه کردیم.
اگر بازخورد ها خوب بود، سرور های کشور های مختلف رو اضافه میکنیم.
توی این ورژن جدید، اپ اپل سعی میکنه به سرور های اختصاصی ما وصل بشه، بعد میره روی سرور های عمومی.
خیلی زود برای دستکتاپ هم آماده میشه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1725" target="_blank">📅 13:41 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1724">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚀
نسخه جدید WhiteDNS Clean IP Finder منتشر شد — v1.4.3
این آپدیت، قابلیت‌های جدید و اصلاحات مهم نسخه‌های v1.4.1 تا v1.4.3 را یک‌جا ارائه می‌دهد.
✨
مهم‌ترین تغییرات:
⚡️
اضافه شدن حالت اسکن سریع
Fast Scan Mode
🌐
اضافه شدن انتخابگر شبکه‌های Edge
Edge Network Picker
☁️
پشتیبانی از سرویس‌های مختلف از جمله:
Cloudflare • Cloudflare Pages • Vercel • Render • Railway •
Fly.io
• Netlify • Koyeb • Glitch
🎯
اسکن هوشمند بر اساس دامنه‌های اختصاصی هر پلتفرم، برای پیدا کردن IPهای واقعاً قابل استفاده
🔐
افزایش دقت در اسکن‌های Scoped با بررسی معتبرتر Certificate و پاسخ دامنه
🌍
اصلاح تشخیص روی Port 80 و جلوگیری از نتیجه‌های اشتباه مبتنی بر CDN Header
🚂
بازگشت دامنه
railway.app
به دامنه‌های شناسایی Railway
🛠
بهبود منطق اسکن، افزایش دقت نتایج و رفع چندین باگ
📱
💻
نسخه‌های منتشرشده برای:
Android • Windows • Linux • macOS • Termux
اگر هنوز از نسخه‌های قبلی استفاده می‌کنید، پیشنهاد می‌شود مستقیماً به v1.4.3 بروید.
🔗
دانلود آخرین نسخه:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases/tag/v1.4.3
@whitedns</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1724" target="_blank">📅 21:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1723">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سلام، من پدی (پدرام) هستم!
همون‌طور که احتمالاً حدس زدید، برنامه‌نویسم و این اولین ویدیوی این کاناله.
اینجا قراره درباره‌ی دنیای نرم‌افزار، برنامه‌نویسی و ابزارهای مختلف، مخصوصاً هوش مصنوعی، حرف بزنیم؛ اما با یه تفاوت مهم:
قرار نیست با اومدن AI، هنر برنامه‌نویسی، مهندسی نرم‌افزار و طراحی درست سیستم‌ها رو فراموش کنیم.
توی این ویدیوی کوتاه، خیلی کلی درباره‌ی دیدگاهم، دلیل ساختن این کانال و مسیری که قراره با هم جلو بریم صحبت می‌کنم.
📹
تماشا ویدیو از یوتیوب
https://youtu.be/h920xIQCMP4?si=gjpsrzgky62iOy25
@whitedns</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1723" target="_blank">📅 20:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">موقت :
دوستان گرامی ، اون کانفیگ هایی که ما توی ربات
@WhiteDnsChainbot
می‌دیم خدمت شما برای
"exit chain
" هست ,
توی v2ray و بقیه آپ ها میزنید و بعد پیام میدید چرا کار نمیکنه ؟ خوب معلومه نباید کار کنه
روزی ۱۰۰ - ۲۰۰ پیام اینجوری داریم میگیریم ،و نمیشه هی تکرار کرد ، خواهش میکنم قبل از استفاده از هر چیزی مطالب کانال را مطالعه کنید ،
پست زیر را بخونید خواهشاً ،
https://t.me/whitedns/1608
اگر موردی هست که سوال دارید و جوابتون را پیدا نکردید  از ربات پاسخگو بپرسید
@WhiteDnsResponder_bot
@whitedns</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/whitedns/1721" target="_blank">📅 13:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1718">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">📦
WhiteDNS Tools — Downloads
━━━━━━━━━━━━━━━━━━
📱
WhiteAesther
• Mobile:
https://github.com/WhiteDNS/WhiteAestherMobile/releases
• Desktop:
https://github.com/WhiteDNS/WhiteAesther/releases
━━━━━━━━━━━━━━━━━━
🛡
WhiteVPN
• Mobile:
https://github.com/WhiteDNS/WhiteVPN/releases
• Desktop:
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases
━━━━━━━━━━━━━━━━━━
🌐
WhiteDNS — مناسب دوران قطعی
• Android:
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
• Desktop:
https://github.com/WhiteDNS/WhiteDNS-Desktop/releases
━━━━━━━━━━━━━━━━━━
🔎
WhiteDNS Clean IP + Resolver Finder
• Desktop & Mobile:
https://github.com/WhiteDNS/WhiteDNS-cleanip-finder/releases
━━━━━━━━━━━━━━━━━━
🍎
CoreForge VPN + DNS — iOS
• TestFlight:
https://testflight.apple.com/join/DRkT6zny
━━━━━━━━━━━━━━━━━━
🎓
آموزش‌ها
🔗
آموزش Exit Chain برای WhiteAesther و WhiteVPN
https://youtu.be/yx-jFqv9pYM
🛡
آموزش کامل WhiteVPN
https://www.youtube.com/watch?v=tm0ls3r4ppw
📱
آموزش کامل WhiteAesther
https://www.youtube.com/watch?v=cRfqxbDY1Dg&t=1s
🌐
آموزش کامل WhiteDNS
https://www.youtube.com/watch?v=tz8cj7HzHVI
🍎
آموزش کامل CoreForge
https://www.youtube.com/watch?v=filwdiPKN90
🔎
آموزش کامل اسکنر WhiteDNS
https://www.youtube.com/watch?v=N5hKuWXp37w
━━━━━━━━━━━━━━━━━━
@whitedns
·:¨༺
@BlueKnight_Net
༻¨:·</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/whitedns/1718" target="_blank">📅 20:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1712">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qF21LkpNikoavgsF5eaOJrZM5SKARrCo1SV1Xtl0GHsFlu7wFYeYgfK8yk9YJMhe1-v9SNhrrlUxP16Bazz1Qn_vHFgff_mtGG0AL0ST2c01ueyKuggFY-Hi-4q9o5Ml2-j8gnck5rPm8_XCgsYKCmVdD5UMlY-Pxcp8WXLjDeW5RTtR9edbKQyKwH8ZJrakxw7PA8PGUnetdGl4JBZ1QkFw99JNVINGXgUOkw78MKC7lzBPx-70I3L3eYGAgQN0IfLXxRy8W3Gk9LWelSugjQ3-3tC9g4qyLIwJHvnGHn016ntjk0xx0M6ZChRdbdUHTDQqDV31L3vsuGmccY8usQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/whitedns/1712" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1711">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HDT9gZ1xESOJtP2NJQKpQks3oOben6fzvpW7YmV5T2XbAIc8RZj4B-nBk6cwb3ljvnOHNhg-GtbNUDg9OvjNe7UcjTiDh9jHNbuwd6V3p8cuaY3cbDvsMa5J3RjITDi9qmiDyzKZ7crqx8N5mbw9MgH0JhaEmkUzSRJOyzBIcpCgX_taGtWDJpqrEwPbsoEH7aNjtvm6bYtEDyLFg1LamdhoE6CvkGnujFwdw52WxgtKNHktjRxa5uET5mYeepyVO8MgWiQX0_KFXnAOwIlzaY7OK9fvkki_-TlVQcjDTcSwzWNiqPE1qzDUeGDwBfrR_xFh3eh-TaYyeo8yiasvow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1711" target="_blank">📅 13:28 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1710">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">WhiteAesthe Desktop 1.7.1 — حالا کامل فارسی منتشر شد
🔥
🔥
از این نسخه، تمام برنامه فارسی است. نه فقط صفحهٔ اول — تمام تنظیمات پیشرفته، زنجیرهٔ خروج، جستجوگر دروازه و پیام‌های وضعیت.
اگر انگلیسی بلد نیستید، دیگر لازم نیست حدس بزنید کدام کلید چه کار می‌کند.
━━━━━━━━━━━━━━━━━━
🔤
چطور فارسی کنم؟
هیچ کاری لازم نیست.
اگر ویندوز یا سیستم شما فارسی است، برنامه خودش بالا می‌آید فارسی.
اگر می‌خواهید دستی عوض کنید: بالا سمت راست پنجره، کنار آیکون تنظیمات، دکمهٔ فا را بزنید. برای برگشت به انگلیسی همان‌جا EN را بزنید.
انتخاب شما ذخیره می‌شود و دفعهٔ بعد هم همان می‌ماند.
━━━━━━━━━━━━━━━━━━
📐
کل چیدمان راست‌به‌چپ شد
فقط کلمه‌ها ترجمه نشدند — منوی کناری، ردیف‌های تنظیمات، دکمه‌ها و نوارها همه به سمت راست منتقل شدند، همان‌طور که یک فارسی‌زبان انتظار دارد.
سه نکته که عمداً برعکس نشدند:
• نمودار تأخیر — زمان همیشه از چپ به راست می‌رود، هر زبانی که باشد. اگر آینه‌اش می‌کردیم، «اکنون» سر قدیمی‌ترین نقطه می‌افتاد. • اعداد لاتین ماندند — آی‌پی، پورت و میلی‌ثانیه با ارقام فارسی خواناتر نمی‌شوند، بدتر می‌شوند. ارقام فارسی فقط داخل متن‌ها استفاده شده‌اند. • اسم‌های فنی — MASQUE، WireGuard، DNS، TLS و مثل این‌ها دست‌نخورده ماندند. ترجمه‌شان فقط گیج‌کننده بود.
━━━━━━━━━━━━━━━━━━
🔍
جستجوی تنظیمات، هر دو زبان
Ctrl + K را بزنید و تایپ کنید.
فارسی تایپ کنید یا انگلیسی — هر دو کار می‌کند. اگر اسم انگلیسی یک تنظیم را از قبل بلدید یا در یک پست انجمن دیده‌اید، لازم نیست معادل فارسی‌اش را حدس بزنید.
مثال: هم «مسیرها» جواب می‌دهد، هم routes. هم «تونل کامل»، هم full tunnel.
━━━━━━━━━━━━━━━━━━
⚙️
موتور به Aether 1.8.0 ارتقا پیدا کرد
چهار مورد که مستقیماً به کار شما می‌آید:
۱. پروکسی بالادستی با یوزر و پسورد — اگر در تنظیمات «اتصال از طریق یک پروکسی محلی» را با نام کاربری و رمز پر کرده بودید، موتور در نسخهٔ قبل رمز را اصلاً نمی‌فرستاد. درست شد.
۲. تونل WireGuard بعد از یک خطای داخلی بالا نمی‌آمد و تا ری‌استارت کامل برنامه برنمی‌گشت. چون پیش‌فرض ما WireGuard است، این را احتمالاً دیده‌اید.
۳. حالت WARP in WARP کرش می‌کرد و بعدش دیگر وصل نمی‌شد.
۴. یک آسیب‌پذیری امنیتی شناخته‌شده در یکی از کتابخانه‌های رمزنگاری حذف شد.
━━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
ویندوز · لینوکس (deb / rpm / AppImage) · مک (اینتل و اپل سیلیکون)
از این نسخه به بعد، وقتی آپدیت جدید بیاید خود برنامه بالای صفحه به شما خبر می‌دهد.
━━━━━━━━━━━━━━━━━━
💬
اگر ترجمه‌ای به نظرتان نامفهوم یا اشتباه است، همین‌جا بگویید — عوضش می‌کنیم.
@whitedns</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/whitedns/1710" target="_blank">📅 18:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1709">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎉
نسخهٔ ۱٫۳٫۰ WhiteAesther android منتشر شد —
برنامه فارسی شد
بزرگ‌ترین تغییر از زمان انتشار .
🔥
رابط کاربری کامل فارسی
همهٔ برنامه، حدود ۴۵۰ عبارت — از صفحهٔ اول تا تنظیمات پیشرفته، اعلان‌ها، و کلید تنظیمات سریع.
زبان را خودتان انتخاب می‌کنید، نه گوشی. در تنظیمات ← زبان سه گزینه هست: سیستم، English، فارسی.
چرا مستقل از گوشی؟ چون این دو برای خیلی‌ها یکی نیست: گوشی‌ای که انگلیسی مانده چون همه‌جا همین‌طور فروخته می‌شود، ولی صاحبش فارسی می‌خواند — و برعکس، کسی که گوشی‌اش فارسی است ولی اصطلاحات انگلیسی را ترجیح می‌دهد.
🔤
فونت وزیر
متن فارسی با فونت وزیرمتن نمایش داده می‌شود، با فاصلهٔ سطر تنظیم‌شده برای خط فارسی.
فونت داخل خود برنامه است، نه اینکه هنگام اجرا از اینترنت گرفته شود. برنامه‌ای که کارش نفرستادن ردپا از شماست، نباید برای یک فونت درخواستی بفرستد که نام دستگاه شما را ببرد.
🔢
عددها
در متن، عدد فارسی. در مقادیر فنی — آدرس IP، پورت، سرعت، مدت اتصال — عدد لاتین.
آدرسی با رقم فارسی نه خوانا است و نه قابل کپی.
🐞
دو کرش وارپ‌در‌وارپ رفع شد
▫️
موقع قطع شدن: برنامه هنگام پایان نشست ناگهان بسته می‌شد.
▫️
موقع وصل شدن: همان موردی که در ۱٫۲٫۷ رفع شد و اینجا هم هست.
⚙️
هستهٔ Aether به ۱٫۸٫۰ رفت
کتابخانه‌های رمزنگاری به‌روز شدند و خواندن هدر پروکسی سریع‌تر شد.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
💬
اگر ترجمه‌ای به نظرتان نارسا بود یا جایی متن از کادر بیرون زد، همین‌جا بگویید. زبان چیزی است که فقط با استفادهٔ واقعی درست می‌شود.
@whitedns</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/whitedns/1709" target="_blank">📅 16:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1708">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ9FWwyaJNdv-RyCAI0KYlLOJjblCJ-fQxyS56am2cnCwqbWzEfWzyotsKOBJTOm9xI_MMRz8F92Y3-Hu7gft8-bAn3z1ah6Rk72dokfk2yNsQJqZrvLCCBMFcv14xR3nZlzhs7MCtKQlU_rHUPRYRNlAqc8IahThIngGdAtbYnhR73CXJ69IDFMphpsMuWat9id8Q3p1IgBA7wEW_efQZ1lTtVAeAFG933mJwm9J9E1UHezvWeD1uQkJzWmIBI__lT95yTIzhHd6ZJb4iUp8R377XF-H1WASjll_n_kc7RIhodkuYIBIdXYvhg-1Yb2K5rYbHWYuDWw6oOBB6h-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
این هم یکی دیگه از تست‌های موفق ما بود؛ تستی که با همراهی و بازخوردهای شما، کنار هم مشکلاتش رو برطرف کردیم.
👑
بیش از ۶ ساعت اتصال پایدار و بدون قطعی
به‌زودی ظرفیت سرورهای اختصاصی WhiteVPN رو چند برابر می‌کنیم. این سرورها فقط از طریق خود اپلیکیشن در دسترس شما قرار می‌گیرن.
تیم WhiteDNS، یک تیم کوچک و با محصولاتی کاملاً رایگانه و هیچ درآمدی از کاربرانش نداره؛ تنها پشتوانه‌ی ما، حمایت شما از کانال یوتیوب و یوتیوب WhiteDNSـه.
❤️
ممنون که کنارمون هستید و کمک می‌کنید این مسیر رو ادامه بدیم.
به امید روزی که نیاز به هیچکدوم ازین ابزار ها نداشته باشیم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1708" target="_blank">📅 16:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1697">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/whitedns/1697" target="_blank">📅 18:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1695" target="_blank">📅 17:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616b32759e.mp4?token=uhcVdR1TCnKPALXogMgP38NL_hXuDo7HamaUICQg-SdVG8uClEl7cdYzK6elFGdZ-OPw4SKRShGnHtEx0W-P-AQ7ZpFFjvGskeGX3xtxrXd4dpnWIl8dJimwH02pJxIh9qYCT6R7BKduyNNl3nyIaCId7IhWKgGSnhAGt5cr3ok2Tk_xzjzwqkp6lcKmltIlDl1uJLeH4zh-6lRMksHCiYo9NhDn3P56GJveMJHmavOOWsyrwjP_9OnBGbQ_ZgpH35XZJgOeXRDO2Hk7NWIuD-ncJ_-l7pEADYXpopYpaweSPG2sYuRx6uHjwGR3xkiMRQqT5DgoNgpM1LlGIJtzyEss5_bPNJ7dRJ_UsPswbFBhbLGhDYqmp94XBx05k4YWs1p7XojohHTQ10Uk_2Ams_-IFyN8xjIapdyws2_JSVYcd5hV9bwS-B1R1KhWqyImwEywPnnwY_pM-dLLdIHS7TuKxYQY6U3HmyZdyF3KGs3KQLD6rus4pYEKyHEUNfIQiwGC2qFJ58U-Cg48zAF-u_5FZjhgTaKezb2lNMS1rTMfSAAe9JmF2Yqm63zvSihPleumC4dlImWcOB-Dr9KwpZbMv3Gl26wCdhEfsxqRXzXaC0F4Z12zA8kTvIJmBokwyEzRs-bn-G2f7OrgLzfOFmdT6v1F7EEPeplDnPbibHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616b32759e.mp4?token=uhcVdR1TCnKPALXogMgP38NL_hXuDo7HamaUICQg-SdVG8uClEl7cdYzK6elFGdZ-OPw4SKRShGnHtEx0W-P-AQ7ZpFFjvGskeGX3xtxrXd4dpnWIl8dJimwH02pJxIh9qYCT6R7BKduyNNl3nyIaCId7IhWKgGSnhAGt5cr3ok2Tk_xzjzwqkp6lcKmltIlDl1uJLeH4zh-6lRMksHCiYo9NhDn3P56GJveMJHmavOOWsyrwjP_9OnBGbQ_ZgpH35XZJgOeXRDO2Hk7NWIuD-ncJ_-l7pEADYXpopYpaweSPG2sYuRx6uHjwGR3xkiMRQqT5DgoNgpM1LlGIJtzyEss5_bPNJ7dRJ_UsPswbFBhbLGhDYqmp94XBx05k4YWs1p7XojohHTQ10Uk_2Ams_-IFyN8xjIapdyws2_JSVYcd5hV9bwS-B1R1KhWqyImwEywPnnwY_pM-dLLdIHS7TuKxYQY6U3HmyZdyF3KGs3KQLD6rus4pYEKyHEUNfIQiwGC2qFJ58U-Cg48zAF-u_5FZjhgTaKezb2lNMS1rTMfSAAe9JmF2Yqm63zvSihPleumC4dlImWcOB-Dr9KwpZbMv3Gl26wCdhEfsxqRXzXaC0F4Z12zA8kTvIJmBokwyEzRs-bn-G2f7OrgLzfOFmdT6v1F7EEPeplDnPbibHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✍️
اگر WhiteVPN فقط با زدن دکمه 《اتصال》 براتو کار نمیکنه، میتوین کانکشن هارو دستی تست کنید و بعد وصل بشید.
⛏
این ویدیو ۱دقیقه بهتون یاد میده چطوری این کار رو انجام بدید.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/whitedns/1694" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFMDLG9NmqTCBfmWebVwRZWWQu3gJzd13XKjBk9q-1Kn5L8gOdOFL7lpjmQEmeC_1aOsbR-XC1yzH0wn0kI1hXa2WsYLlawxb5BXcthoGstWhfBcdTd6wbakibkaobFGV5y9eCgpck5ueJzEyhpBYoqImdkaMCj-8AJMyb2eV_Mn6fpRnYoHhBc0a3QjmnZ0r8hSxZn5SYaGTyNZ7VQvvLb9zJCz-VG9C-kEIiI61Uhx6QO0jNiHopBuyz86M_oGbkNsUXMZYTqdkdX2rOKJZug-xBwr2uR9-oNAvRR3Ek7UAVcxSmZXfBi3yjMXR8ocUtJGVBna8vtgblacEuq0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
ما تصمیم گرفتیم محتوی متفاوت در زمینه تکنولوژی داخل
چنل یوتیوب WhiteDNS
بذاریم
این اولین ویدیو متفاوت از موضوع هایی هست که تا  امروز داشتیم و توی این ویدیو دایانا ۵ ابزار کاربردی
و
رایگان هوش مصنوعی برای تولید محتوی در موضوع های زیر معرفی میکنه.
🎙️
Speechma — تبدیل متن به گفتار و ساخت صدای AI به‌صورت آنلاین
🎨
Leonardo AI — تولید تصویر، آثار هنری و تصاویر خلاقانه با هوش مصنوعی
🧪
Google Labs — آشنایی با پروژه‌ها، ابزارها و آزمایش‌های جدید هوش مصنوعی گوگل
📸
Clipdrop — مجموعه ابزارهای هوش مصنوعی برای ادیت و ویرایش عکس
🎶
Suno AI — ساخت آهنگ باکلام و بی‌کلام با استفاده از هوش مصنوعی
📹
تماشا ویدیو در یوتیوب</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1693" target="_blank">📅 11:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1690">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/YmiU2yiPvW6r6EB4NYIEv8xzP_AXWFbe89WJbIgW7C-HK1IWsWOXAWlLj7BCJ01LOXzjBHs8B39jIV7J9vPZMtYepE55D7PDaFxeg_hNTkJMFEzhhE7rOWV3nQUAnLQ45mnwXHL2BV6blU2C_GEB6-xPk-txMLArOU9MCFFa50LbVNH1l3zHuGJHJdMYwUs1Iyj5ySvV6PkFe0HI8ZP3RAiTJVzgdbmJdw-FEvsa8K6aopbZzBLB8MVxSkLen7P1EasYpnUsJsPD-wook-CfElq4h12VfpdCa4pafCfx9gIacGS3sfDx9AZGywRW26QFrOPWwqcC1lj6HEummyNE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/whitedns/1690" target="_blank">📅 11:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1689">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">⚠️
اصلاحیه
نسخهٔ ۱.۲.۷ منتشر شد
اگر نسخهٔ ۱.۲.۶ را نصب کرده‌اید، لطفاً به‌روزرسانی کنید.
🐞
مشکل چه بود
در نسخهٔ ۱٫۲٫۶، اگر پروتکل را روی وارپ‌در‌وارپ می‌گذاشتید و دکمهٔ اتصال را می‌زدید، برنامه بسته می‌شد.
بقیهٔ پروتکل‌ها سالم بودند. فقط وارپ‌در‌وارپ.
🔧
چرا این اتفاق افتاد
در نسخهٔ ۱٫۲٫۶ یک باگ قدیمی را رفع کردیم که باعث می‌شد روی وارپ‌در‌وارپ مرورگرها باز نشوند. برای آن رفع، اندازهٔ بسته‌ها را به عددی تغییر دادیم که این تونل واقعاً می‌تواند حمل کند.
ولی آن عدد از حداقلی که پروتکل IPv6 لازم دارد کمتر بود، و اندروید این حداقل را اجباری می‌کند. نتیجه‌اش این شد که ساختن تونل رد می‌شد و برنامه بسته می‌شد.
یعنی رفع ما مشکل بدتری ساخت: قبلش وصل می‌شد و مرورگر کار نمی‌کرد، بعدش اصلاً وصل نمی‌شد.
بابت این اشتباه عذرخواهی می‌کنیم.
✅
در نسخهٔ ۱٫۲٫۷
حالا وقتی تونل نتواند IPv6 را حمل کند، برنامه آن را روشن نمی‌کند به‌جای اینکه بسته شود.
نتیجهٔ عملی: وارپ‌در‌وارپ فقط با IPv4 کار می‌کند. این محدودیت واقعی این تونل است، نه چیزی که بشود دورش زد.
هم اتصال درست کار می‌کند و هم مرورگرها باز می‌شوند.
به‌جز این، هیچ چیز دیگری نسبت به ۱٫۲٫۶ عوض نشده. تمام قابلیت‌هایی که در پست قبلی گفتیم سر جایشان هستند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
نیازی به حذف برنامه نیست؛ روی نسخهٔ قبلی نصب می‌شود و تنظیماتتان می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/whitedns/1689" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1687">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔗
نسخه جدید اندروید whiteaesther منتشر شد -
🔥
1.2.6
این نسخه یک باگ مهم را رفع می‌کند و بخش زنجیرهٔ خروج را برای فهرست‌های بزرگ بهینه می‌کند.
پایین همه‌چیز با آموزش آمده.
🐞
رفع باگ: مرورگرها روی حالت وارپ‌در‌وارپ باز نمی‌شدند
اگر روی پروتکل وارپ‌در‌وارپ وصل می‌شدید و همه‌چیز درست به نظر می‌رسید ولی هیچ سایتی بالا نمی‌آمد، این همان مشکل بود.
چه اتفاقی می‌افتاد: اپ به گوشی می‌گفت بسته‌های بزرگ‌تری بفرست از آن‌چه این تونل می‌توانست حمل کند. درخواست‌های کوچک رد می‌شدند و هر چیز بزرگ‌تر بی‌صدا می‌افتاد.
برای همین بعضی برنامه‌ها مثل تست سرعت کار می‌کردند ولی مرورگرها نه — مرورگر بسته‌های بزرگ می‌فرستد.
این باگ از نسخهٔ ۱٫۲٫۲ بود و حالا رفع شده.
⚡️
زنجیرهٔ خروج برای اشتراک‌های بزرگ
اگر اشتراک شما صدها یا هزاران کانفیگ دارد، این بخش عملاً غیرقابل استفاده بود. چهار مشکل داشت که همه رفع شدند.
۱) باز شدن صفحه گوشی را قفل می‌کرد
اپ همهٔ ردیف‌ها را یک‌جا می‌ساخت، حتی آن‌هایی که روی صفحه دیده نمی‌شدند. حالا فقط همان‌هایی ساخته می‌شوند که می‌بینید.
۲) دکمهٔ تست همه تمام نمی‌شد
روی هزار کانفیگ حدود شانزده دقیقه طول می‌کشید و هیچ نشانه‌ای از پیشرفت نمی‌داد. حالا دکمه می‌گوید چند تا تمام شده، و همان دکمه متوقفش می‌کند.
۳) فقط چند تای اول پینگ می‌گرفتند
همهٔ تست‌ها یک‌جا فرستاده می‌شدند، یعنی صدها درخواست هم‌زمان از یک تونل. تونل اشباع می‌شد و بقیه به نتیجه نمی‌رسیدند. حالا دسته‌دسته فرستاده می‌شوند.
۴) اتصال، لحظه‌ای گوشی را قفل می‌کرد
اپ کار سنگینی را روی رشتهٔ اصلی انجام می‌داد، دقیقاً وقتی تونل بالا می‌آمد.
🆕
قابلیت‌های جدید در زنجیرهٔ خروج
مسیر: تب Routes ← گزینهٔ Exit chain
🔍
جست‌وجوی کانفیگ
بالای فهرست یک کادر جست‌وجو هست. بخشی از نام را بنویسید تا فیلتر شود. روی فهرست هزارتایی، این تنها راه پیدا کردن یک کانفیگ خاص است.
✅
انتخاب چندتایی
کنار هر کانفیگ یک تیک هست. چند تا را انتخاب کنید تا روی همه‌شان کار کنید.
⚠️
تیک با انتخاب کانفیگ فعال فرق دارد. برای عوض کردن کانفیگی که ترافیک از آن می‌رود، روی خودِ ردیف بزنید نه روی تیک.
🗑
حذف از فهرست
بعد از تیک زدن، دکمهٔ حذف ظاهر می‌شود.
⚠️
نکتهٔ مهم: کانفیگ‌های اشتراک واقعاً پاک نمی‌شوند، چون اپ دفعهٔ بعد دوباره اشتراک را می‌گیرد. اپ فقط آن‌ها را از فهرست کنار می‌گذارد.
اپ تعدادشان را نشان می‌دهد و یک دکمهٔ بازگردانی دارد، تا کانفیگی که ناپدید شده با اشتراک خراب اشتباه نشود.
🏓
دو نوع تست
هر دو دکمه حالا بالای فهرست هستند، نه پایین آن.
▫️
Test all — همه را امتحان می‌کند. روی فهرست بزرگ چند دقیقه طول می‌کشد.
▫️
Test selected — فقط آن‌هایی که تیک زده‌اید.
راه عملی برای فهرست بزرگ: با جست‌وجو چند تا را پیدا کنید، تیک بزنید، و دومی را بزنید. خیلی سریع‌تر از امتحان کردن هزار تا.
📶
مرتب‌سازی خودکار
فهرست خودش مرتب می‌شود: سریع‌ترین‌ها اول، بعد آن‌هایی که هنوز تست نشده‌اند، و آخر آن‌هایی که این نسخه نمی‌تواند به آن‌ها وصل شود.
📺
اندروید تی‌وی
تیک‌های جدید با کنترل تلویزیون و دستهٔ بازی هم کار می‌کنند و حلقهٔ فوکوس دارند.
⬇️
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— تقریباً همهٔ گوشی‌های ۲۰۱۷ به بعد. از این شروع کنید
▫️
armeabi-v7a
— گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید
اگر مشکلی داشتید، از مسیر
Settings
←
Diagnostics
گزارش بگیرید و بفرستید.
@whitedns</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/whitedns/1687" target="_blank">📅 21:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1683">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نسخه جدید
🎯
WhiteVPN Desktop  منتشر شد -v1.0.20
این نسخه بیشترین تغییرات کاربری چند وقت اخیر را دارد.
سایت‌های ایرانی دیگر از تونل رد نمی‌شوند
بزرگ‌ترین درخواست شما بود: لازم نباشد برای باز کردن بانک یا سامانه‌های دولتی، وی‌پی‌ان را قطع کنید و بعد یادتان برود دوباره روشنش کنید.
مسیر: تنظیمات ← سایت‌هایی که از تونل رد نمی‌شوند
سایت‌های انتخابی مستقیم از خود دستگاه شما خارج می‌شوند. سریع‌تر باز می‌شوند، و آن‌هایی که آدرس خارجی را قبول نمی‌کنند درست کار می‌کنند.
▪️
فهرست از قبل پر است. اولین مورد، کل دامنهٔ کشوری ایران را یکجا می‌گیرد
▪️
دیجی‌کالا، آپارات، ورزش سه، دیوار، اسنپ و شاپرک هم در فهرست هستند
▪️
هر کدام را می‌توانید حذف کنید و هرچه خواستید اضافه کنید
▪️
محدودهٔ آی‌پی هم می‌شود اضافه کرد، مثلاً برای شبکهٔ محل کار
▪️
چسباندن آدرس کامل اشکالی ندارد و بخش‌های اضافه خودکار حذف می‌شوند
پیش‌فرض خاموش است. آپدیت نباید بدون انتخاب خودتان مسیر ترافیکتان را عوض کند، پس اول سوئیچ بالای همان صفحه را روشن کنید.
⚠️
هر چیزی که در این فهرست باشد با آدرس واقعی شما خارج می‌شود، دقیقاً مثل وقتی که وی‌پی‌ان خاموش است. هدف همین است، ولی یعنی هرچه نمی‌خواهید دیده شود جایش در این فهرست نیست.
🪟
یک پنجره، هرچند بار که کلیک کنید
تا حالا هر بار اجرای برنامه یک آیکون تازه در نوار وظیفه می‌ساخت. دو بار، سه بار، و هر کدام یک موتور جداگانه که سر پورت با بقیه درگیر می‌شد.
حالا اجرای دوباره فقط همان پنجرهٔ موجود را جلو می‌آورد. مخصوصاً وقتی پنجره را بسته‌اید و برنامه کنار ساعت است، که از بیرون شبیه خاموش بودن به نظر می‌رسد.
🐧
حالت تونل روی لینوکس
تا حالا فقط روی ویندوز کار می‌کرد. حالا روی لینوکس هم هست و رمز را از طریق پولکیت می‌پرسد. اگر پولکیت نصب نباشد، گزینه اصلاً نشان داده نمی‌شود، به‌جای اینکه باشد و همیشه شکست بخورد.
🎨
رنگ آیکون کنار ساعت
حالا وضعیت اتصال را از رنگ آیکون می‌فهمید، بدون باز کردن پنجره:
🟢
متصل
🟠
در حال اتصال
🔴
ناموفق
⚪️
قطع
🔌
پورت اشتراک‌گذاری روی شبکه
وقتی اتصال را با گوشی یا تلویزیون به اشتراک می‌گذارید، حالا پورت را خودتان تعیین می‌کنید. قبلاً اگر پورت اشغال بود، برنامه بی‌صدا پورت دیگری برمی‌داشت و دستگاهی که تنظیمش کرده بودید به جای خالی وصل می‌ماند.
هر دو پروتکل روی همان یک پورت کار می‌کنند.
🧪
تست همهٔ اشتراک‌ها در یک اجرا
دانلود
ویندوز، مک و لینوکس، همه از این نشانی:
github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
@whitedns</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/whitedns/1683" target="_blank">📅 21:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NRY5eCNTGUG6P3wasDzOsY1fx6VTZ9kpcWdff1Nqj6ojAUeFsoboyVAwYOurgTI4_TFoT2s-F1T_YXh9qviGrAuvP5ndMpfxc5yKw3K-oM0WcR7Ru1xZztige4y3YrQUFTuWWqRdbp8kLipulW5TzLEdDnvM1aXcOSoBJ40BYonTkYdGkY0pvrybdLA9w1rDxTCDGC4DFVI54fdbkBgP5AurFs7k_h4RbG64kI3ZDLA9L3l8XVy-PApkC-axzavUiBW6WuNXHdY1Ct_hT9x8MAZHOrBKgg4-vtP1bRw7d1iWtq_iCEli3JMgHwDBQVHhp059Fk6NssTjDyqNuD4pvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
نسخه جدید WhiteDNS Clean IP Finder منتشر شد.
🔭
تغییرات اصلی:
🟢
پشتیبانی بهتر از IPv6
🟢
انتخاب IPv4، IPv6 یا هر دو در ASN Scanner
🟢
بهبود حالت‌های Fast و Thorough در DNS Scan
🟢
بهبود DoH / DoT و مدیریت Timeout
🟢
گزارش‌دهی و مرتب‌سازی بهتر نتایج
🟢
بهبود Nearby Discovery برای IPv4 و IPv6
🟢
بهبود نسخه‌های Android و Desktop
🟢
بدون نیاز به تغییر تنظیمات نسخه‌های قبلی
📱
دانلود آخرین نسخه از گیتهاب
📱
تماشا آموزش اسکنر WhiteDNS Clean IP Scanner
⭐️
اگر پروژه براتون مفیده، توی GitHub استارش کنید.
@whitedns</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/whitedns/1680" target="_blank">📅 09:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=BYaVkyPuOhW3DtVc0uv5JWc_BOzvwK4IY1PD8cmW0UUS0KyxeDw9_o4t2DDTGbjpZLos7mj5-tM2q-9ZxGdcnuINY18PYsDA2xNj6UykIt7Qup6WaCXmYbl9ofO4uNgeJ7QSkdXgGl7CALTUzJJzNIHKZ3yAFhXhOohSpE4adM7715ldM5x46yZUIEC-LqU3TQSnIfuWxx_mStsx9Db_FGfAIkxeh6rbfrzIEvjPclCKylTRQMacw9yXV9GdvWCQK6Ulje2AE23yENl90zxpxV9eDQlCXRXqCXjJtDAL4pyS9Ma0AIBwC-WkMpS1itpW9Wt2xko_sXCVOHR7Z0jpeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f216f892a.mp4?token=BYaVkyPuOhW3DtVc0uv5JWc_BOzvwK4IY1PD8cmW0UUS0KyxeDw9_o4t2DDTGbjpZLos7mj5-tM2q-9ZxGdcnuINY18PYsDA2xNj6UykIt7Qup6WaCXmYbl9ofO4uNgeJ7QSkdXgGl7CALTUzJJzNIHKZ3yAFhXhOohSpE4adM7715ldM5x46yZUIEC-LqU3TQSnIfuWxx_mStsx9Db_FGfAIkxeh6rbfrzIEvjPclCKylTRQMacw9yXV9GdvWCQK6Ulje2AE23yENl90zxpxV9eDQlCXRXqCXjJtDAL4pyS9Ma0AIBwC-WkMpS1itpW9Wt2xko_sXCVOHR7Z0jpeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اگر برای باز کردن اپلیکیشن های
x.com
یا اپلیکیشن های AI مشکل دارید، میتونید از داخل WhiteVPN مسیر زیر رو طی کنید
تنطیمات > اتصال ها > یکپارچگی TLS
Settings > Connections > TLS Integrity</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1679" target="_blank">📅 09:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1676">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">خرید و فروش کانفیگ در کل گروه های whitedns ممنوع است
⚠️
بلافاصله بدون اخطار = ban</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1676" target="_blank">📅 10:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1675">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
🔼</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/1675" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1670">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/whitedns/1670" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/whitedns/1670" target="_blank">📅 09:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1669">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFKkInGWQztb4ZnrAsrMQS40wIBfkl0OEmogCsW5k9kGTmTPs8L5h7ZKZTTXxlj4kOg7dOMRP0K3pJoqsL7rX0ZtcWiCJIhWyqVOUG5FV2ZsfZRKOx3NfLM5pBp91FtCfzex4pTxanNxjX1puPGyDFiNq8uMu7reVH4OWb_2ZqRlx_AC8dm74OdUO1IIUhIa70AomyEftpXCEa8-2Gyx4QygtGxP6Nrd9xmR2LyyF-FiXotSmA54grBi4wGZFcHnSznGrG9WE3hAGI54pTpGGZhbJAWCHYEIZXkEOQ4swwDMPg-BEIFxtfUeiHNOgqj3ZoA9FfkxIKYxaQNX0-t-LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/whitedns/1669" target="_blank">📅 09:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1665">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/LUp02YsIhO9QA0Dz6yJJ899xgtK8wLg-a23EJeWA5NWhc_xkqK71EO8LpHYg-eLVBYxCgYy3utCbxCiSbfb-4c3gW0BJfy4OCNX2fl8f7j0BYVTH6RcKC_s-nP3isrq2Iqrj7Ak7O_Iznho5XKwrQD_7LNeHr4HCqLSwVpMn0DM9tI97it86MaeF1SXz5ZzWM1TlfcEJxJc7Ume7cxzXu7nIxGJ8S_t02AQ4fId2Ve-V7mBc3zG9arwmrhfCsdlZbDYmjnb8WBIQN1uuVKURQ60A80udsF59XH-djZd9agwZ9hkgNayIat1D09icdhS8hWeAGDC0jH4i7q3hN5o-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه رسمی و شفاف‌سازی مجموعه WhiteDNS
دسترسی به اینترنت آزاد، پایدار و امن حق طبیعی هر کاربر است. مجموعه
WhiteDNS
با هدف تحقق این هدف و تسهیل ارتباطات، خدمات و زیرساخت‌های خود را در اختیار عموم قرار داده است.
بدین‌وسیله رسماً اعلام می‌گردد:
۱۰۰٪ رایگان بدون هیچ قید و شرط:
تمامی خدمات، سرورها، کانفیگ‌ها، دی‌ان‌اس‌ها و آموزش‌های ارائه‌شده در چنل رسمی
WhiteDNS
کاملاً رایگان بوده و خواهد بود.
عدم وجود هرگونه اشتراک پولی (VIP):
این مجموعه هیچ‌گونه اکانت ویژه، پولی، پلن VIP، یا سرویس اختصاصی فروشی ندارد.
ممنوعیت کامل خرید و فروش:
هرگونه خرید، فروش، واسطه‌گری یا سوءاستفاده مالی از نام، کانفیگ‌ها یا سرورهای
WhiteDNS
غیرقانونی، غیرانسانی و نقض صریح قوانین این پروژه است.
هشدار نسبت به کلاهبرداری:
اگر فرد یا گروهی تحت عنوان ادمین، نماینده یا پشتیبان
WhiteDNS
به شما پیشنهاد خرید سرویس، اکانت یا پرداخت هزینه داد، سریعاً او را مسدود (بلاک) کرده و موضوع را گزارش دهید.
تنها مرجع رسمی:
کلیه اطلاع‌رسانی‌ها و به‌روزرسانی‌ها صرفاً از طریق کانال تلگرامی ما منتشر می‌شود:
🔗
کانال رسمی تلگرام:
https://t.me/whitedns
❤️
حمایت شما تنها از طریق معرفی کانال به دوستانتان و اشتراک‌گذاری اینترنت آزاد با دیگران و تماشای ویدیوهای ما در
کانال یوتیوب
و دادن
⭐️
به پست های ما و همچنین boost کردن کانال و حمایت از
گبت هاب
ما  امکان پذیر است
کلیه خدمات  WhiteDNS همواره رایگان در کنار شما می‌ماند.
@whitedns</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1665" target="_blank">📅 06:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1663">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔥
درود دوستان عزیز :
با توجه به رای گیری که شد و نظر دوستان عزیز
مقدار حجم روزانه کانفیگ های ربات به
4 گیگ
تغییر کرد
❤️
اگر از این خدمت استفبال شود احتمالا به زودی سرورهای بیشتر با لوکیشن های بیشتر در اختیار شما عزیران قرار خواهد گرفت که هر چه بیشتر امکان دسترسی رایگان شما فراهم شود .
بازم تاکید میکنیم که این کانفیگ ها فقط و فقط برای استفاده در قابلیت " exit chain " در برنامه های whiteaesther و whitevpn است . متاسفانه هنوز یک تعداد زیادی پیام دریافت میکنیم که دوستان میگن چرا این کانفیگ های توی v2rayng , hiddify و .......... کار نمیکنه
.
⚠️
لطفا تمام مطالب پست زیر را با دقت کامل بخونید
https://t.me/whitedns/1608
لازم به ذکر کرد در صورت مشاهده هر گونه سواستفاده از این کانفیگ ها لطفا به ادمین ها گزارش دهید
درصورتی که مشاهده شود که کانفیگ ها توسط افراد سودجو  در حال فروش به دیگران است این خدمت به طور کل حذف خواهد شد - پس خواهشمندیم خودتون در حفظ این امکان کوشا باشید
ربات :
@WhiteDnsChainbot
ارادتمند
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/whitedns/1663" target="_blank">📅 05:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1658">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-poll">
<h4>📊 محدودیت حجم کانفیگ ربات را از 1 گیگ به چقدر تغییر بدیم که برای انجام کارهای روزمره کافی باشه ؟👀</h4>
<ul>
<li>✓ 1.5</li>
<li>✓ 2</li>
<li>✓ 3</li>
<li>✓ 4</li>
<li>✓ همین خوبه☺️</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/whitedns/1658" target="_blank">📅 13:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1656">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ua4qZZ3KyTfeSO9WdCOmoOKvKIWeYlcnRNLE6qD_uneWf6F0DaO1yBAcEcuqWDPYVxiyoX02UjKzhNmS5UYbM5msyuHJT0oeuPc6ShiOJ9zt77KPfOKZu93vRsNmvSOmgIy7ml4K89NWfQhy6ZQIHINnhEl4UFSPz-qDHjwPXpDJqwauUCAl5OS-sZWIZj2teJlIirku8f4A2xHJ0gg-wcugoqETN2G1Yw9zgtvDB8PEIcRYWD9O3rM2D7f9CQLYFU8wUr680YgnSylZfztaosjODKvM2ERVVnQx3q6o1nzrv8wnnfrTb9KUBmPWwb1miBIjHXcXRMnsv3Ke1hY2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#آموزش
اگر WhiteAesther mobile با یک بار زدن دکمه اتصال وصل نشد، یعنی هنوز باید تنظیمات درست شبکه خودت را پیدا کنی.
📡
این راهنمای کامل را قدم‌به‌قدم بخوان:
📖
https://github.com/WhiteDNS/WhiteAestherMobile/blob/main/docs/GUIDE.fa.md
@whitedns</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/1656" target="_blank">📅 09:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/kpR0NtZiuHgC0KGocxVEO5Y_r_tPKXIVi8KU7xMd1v0dIgu0e2RwpGRb_XFK8sgqUCmP4fha4VYqTo_X7KG4ehbtpCAm5NtDH2e8jFK6A04TMFot8VH_tq_RFEDJgVtrxx8bdSG67pYAY1kOtadaqD_faYegeWl1cB9dgNEMbxHDRti0Am4XjoT8u4LX1OGjoA82Bvet4z8d376hT_zml0HVxQiWz-1YaalZNuJjMUkuaV_NPY2jfenBm6Jp5BbXMn-WNdRXs4R9NgPhya7cYv3BEH8MshsxHJ8gaoPBf92Alwl-hFsWOqTljU5lG-6clSRfOunV-IBFW7IYmDCMIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان عزیز
👋
چند تا کانفیگ جدید به ربات اضافه کردیم  که شاید بهتر بتونید متصل بشید و برای سرویس های خارجی مشکلات کمتری داشته باشید . کانفیگ ها تست شده است و مشکلی نداره
✅
از حالا به بعد شما میتونید تا
3 کانفیگ
را انتخاب کنید
😃
❤️
لطفا برای اطلاعات بیشتر حتما پست زیر را مطالعه کنید
⚠️
⚠️
https://t.me/whitedns/1608
Bot
🤖
:
@WhiteDnsChainbot
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1654" target="_blank">📅 05:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZfUXgtjW6zcF6LPsaiyLfcisMy1PxsghBVrsZfn96MLdTxG2J3EQraZ482f6l1xVNiMXB10d8gFaq1udNcpuPoDDVqZoV874nYkCojjESUd20wrHPncDzGRaVKmfOQGFoUO1t8chuVQdleU8PvBsxiAbsGRZc1wpKXFvxsFV_oC1ZseX0zkTJczk1M5M5xWW1zmNMYBDN-S0mWZ0Jp7KBDoJCqt60NNCqG3SefDQNr3SVsuYiV2GI5C8mVkvtZo3nHLn1V85YRC1_fkHUyWMbwdWu7jPUTNnRQhsqxgiXsS9NWnG9g1h17eLChoSv_WJciFaZ0m-x3La6wzvZjfdkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1653" target="_blank">📅 05:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/iWEh9zhN2hKSScLwHQOPHE-dmm1lLud1mwwzcpbmCkfGCY1Wp7PSRDELVbKltrsE-yFWudWI_BsGs7k229FZ5uKoLl_VMuI4yQsXYhjk4vOFz38fQ2N71d4qqJdJ2MA0nG_IOOs-KLb8fXpOoxC3Xh2iXGR3gp1lx1mp_5v2bT8J_ZoJW5DN0WwLPwQFn1EyTjMC6_EyeHZNKf-OQ9VYBr9jEWp5aXxCgPfkPizbKUoSPmZRW5aTeSgppzuQGVWymOCqTHms7ckt4D5x7a8QUKlAU0iMSjjDDnfd1QEkkchh--gxZaiGxcUyotKQR7VMumoElnq45Yypg1Wt4W0cxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1652" target="_blank">📅 05:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XDe3Y4iH8WvpWVJl1Hj8sVg0Qso5m982l_6IuMYgjBJI4mUvjSPRX9VGpr7S_a86dwbycVFf6ltGSr7Xq1z4Q7bn5JjmoV6dGrV4FfBXqVCzbVz9MSjXhZjez9gMWxRyHt4PUoKR6jQR8TkGuWtBxUxqzeBW0MZ2LKG5W4NplIB89YX2zpTSbBksuXVgACA8dhdup4_qqqikN1TTVzsVcDs6ZObe5MZamk9wPQJNTuoBb6aSxlnggTUFC29Kt9ssyMI5gh_XDrpa6NNDsxW_uwXW_KR33YZzTg7etcqNjQNpDerGi9beI0tXyNYPdwjsYkNi4KCZRK33-ChzZ-aEXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
آپدیت WhiteAesther — نسخه 1.2.5
🔥
⚠️
⚠️
⚠️
در این ورژن رفع باگ Android TV انجام شده است و دوستانی که روی گوشی استفاده میکنند لازم نیست اپدیت کنند
⚠️
⚠️
⚠️
مشکل کنترل با ریموت در Android TV برطرف شد. پیش از این، بعد از رسیدن به بخش «Connected for»، امکان حرکت به قسمت‌های پایین‌تر صفحه وجود نداشت.
حالا با دکمه‌های بالا و پایین کنترلر می‌توانید به‌راحتی بین تمام بخش‌های صفحه Home حرکت کنید و اطلاعاتی مثل آدرس، ترافیک مصرفی و جزئیات اتصال را ببینید.
این تغییر فقط مربوط به حالت Android TV است و عملکرد نسخه موبایل تغییری نکرده.
🔗
دانلود رسمی از گیت هاب
@whitedns</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/whitedns/1651" target="_blank">📅 16:25 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFV7EhrtmJsaFI2JfI7WXBQBdg3E0QIhzePBbYWQB9Q3XrXE_jSMWEI7v1bhJo4R1e-HdAcT7nJSYQnillh0yQB5IozPjKy8t-uDpTLymNg4kFrQBxQ8i1y2itdr79y6uCkqBl3hjwia6rRL_m5n_T90E_Z4D_jBJaaFd_m8d5mpS8brihWp2j7HodwwulX5IW8D_yUoi_U6KsRNRnsYiAelTi0TbBI2dDEgEHqMvnCuXSDgMZ6EI35GsQjCC_U3t6ryjJRpvK_Q1iLvaCmijQDtsv4JkEBpG5dyadn9Dw_F84hQnz-NaD-4B-Z2zDz7Am4nubP-kh6qAhtcexYDnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
نسخه Android TV و Google TV برنامه WhiteAesther منتشر شد
از نسخه v1.2.4 به بعد می‌توانید WhiteAesther را روی تلویزیون، TV Box و دستگاه‌های Google TV فقط با ریموت یا دستهٔ بازی کنترل کنید؛ بدون نیاز به صفحهٔ لمسی.
حداقل نسخه موردنیاز: Android 8
🔗
دانلود رسمی از گیتهاب
⚠️
برنامه را فقط از لینک رسمی بالا دانلود کنید.
🦢
🦢
🦢
🦢
🦢
🦢
📥
کدام فایل WhiteAesther را برای تلویزیون دانلود کنیم؟
برای بیشتر تلویزیون‌ها و TV Boxهای جدید:
"WhiteAestherMobile-1.2.4-arm64-v8a.apk"
اگر مدل پردازنده را نمی‌دانید یا فایل بالا نصب نشد:
"WhiteAestherMobile-1.2.4-universal.apk"
نسخه Universal روی دستگاه‌های بیشتری اجرا می‌شود، اما حجم بیشتری دارد.
گزینه‌های دیگر:
• نسخه "armeabi-v7a": مخصوص دستگاه‌های قدیمی ۳۲ بیتی
• نسخه "x86_64": بیشتر برای شبیه‌سازها و بعضی دستگاه‌های خاص
• فایل "AAB": برای نصب مستقیم مناسب نیست
🦢
🦢
🦢
🦢
🦢
🦢
🛠
نصب WhiteAesther مستقیماً روی Android TV
۱. مرورگر تلویزیون یا برنامه‌ای مثل Downloader را باز کنید.
۲. وارد صفحه رسمی انتشار شوید.
۳. فایل APK مناسب دستگاه را دانلود کنید.
۴. فایل را باز کرده و Install را بزنید.
اگر اجازه نصب داده نشد، گزینه Install unknown apps را برای مرورگر یا Downloader فعال کنید.
این تنظیم معمولاً در یکی از مسیرهای زیر قرار دارد:
Settings → Apps → Special app access → Install unknown apps
یا:
Settings → Security → Unknown sources
بعد از نصب، بهتر است این دسترسی را دوباره غیرفعال کنید.
🔗
دانلود نسخه رسمی از گیتهاب</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/whitedns/1650" target="_blank">📅 10:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1649">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7BjC0lMI8eEyDLSEH6qBNAzI53yKazFMbbeju8bqCs3YM_cWMLkfnkH-07IAJFyZKjzas9d8Ds1Rlgo_RUekNEzA7MtANVJ8OuN1HQkn7zW1Sesz-clBqMq1rJNkwKEHqSxkiCmT3GTZ97X2-yqPZNbvUdX2rnSAJjA9kp7cKVO9moD-7YeDY_Agv9TH1V-XwkDHeQ7bpKZnAyJWP0HO0J545_uRoye7CQnsZhZOdxHxTuurXpoZFkapF_xxkm7Q6qlOMOSm8RM2mJZOwzDrN_hsQJ4sUVoDgnHEj7brM023oKKXlNY6K3B1lr4wQKS1HUmKqnlB4N0Ltd0mj8Omw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔭
داریم تست های نهایی رو برای WhiteAesther روی AndroidTV  انجام میدی
م</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1649" target="_blank">📅 19:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1645">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/oO3Hfmm9TMvu80XOGRuQSHpm1sigZon-8Zz-C1evZvXU5RF3oy3pzBAxp8UqFH1S-3D0ei1n-fo6YjgdYnhkCIJJL447_1gmkR0s5soYmF6l64mXGO0KzzvsWO_-AgysmMBrUjLz1iKFU3OtKnjhKUoLMfIdiPObwPv7t9mw_mm0pgzgfdxxCWftuceRGG5c2r_kBOn3CG1NbkizfPaJ2rlZceGxacQDKNnZyDcUR3BGOiIy6b8kPxISEiM2XOHSCl8CWEqftOhO6hHsdaNCoZr3dTEmG_XG8ax9OMoxwAJaiAW9VbDM5_bubHVcKkIDLAc17hUl14ZHtet2y1tONA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/j_eAmBp_loCtC6fI7Zh0bI43xG05s7hV37ilmM5eAKl4jnBLX6d5zCuuz8rhWlu6CX7ipTCvyhGtWRC1J11NTms9nt8AnvPS--DToPrn99GpJ83T0YTwtWs9jEgP-l6ahMIM0dLH3wbB5W_KTaay3sN23QMO9aA-pUrfeYDDhNDwvM3LmcORrffhqkphL6ee0N8hBxG1sTFW6N3Fr0gdblWx9Cqt78e2QTxbyldm81fMdMIFhdd3ZzIAbf88S4yYd01G9DPXk4d2Ngn14Kf25LtY5o5fz7hfadrQGWsB8_VeRbG7aSZ0ePghhQ9NeoYNAZ3Oy8Ju8ngf9VfucwUmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Ffc0nwjnHjqqNJPh4-KIuCU2L66gKghZn55vCL2fY_9-zXOl3W9VdTcfH4M4B_g1pPiIavtusp9-4EkwQYy_tLOJt1v1EScMislQZfWl_6QJyE2FUBVcWD2LIUYBMbyDnbQPFYEXFMspabWR-cI-56gn-aFRcTPQqaCu7m-BSo_a40GNrAHVEaFY9wTRMvSZzffVH3z9oZQEpE0gljVLdEP0pR23cIf7OKHIbuLp3MxXuMIxGJn1UVTuRFrPmj99lFx7CWGn_BjU5F4zjgqYEORiwT_H-qOXDn1RUItoziCGel73NbaOG2HkE6ZlC83NMnmzcDLkWauiga2FCElkJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/whitedns/1645" target="_blank">📅 15:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1644">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG/PattN کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  پروژه های خوبی وجود دارند که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1644" target="_blank">📅 06:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1641">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مطالب اموزشی نسخه 1.6.0 دسکتاپ whiteaesther
🔥
🔥
خلاصه :
🔧
تغییرات و قابلیت‌های جدید
▫️
حالت
Full Tunnel
یک کارت شبکهٔ مجازی ایجاد می‌کند تا تمام ترافیک سیستم از تونل عبور کند؛ حتی برنامه‌هایی که تنظیمات Proxy را نادیده می‌گیرند.
▫️
خروج سایت‌های ایرانی از تونل
شامل ۲۹۰۶ رنج IP و ۴۱٬۷۲۹ دامنه ایرانی است که مستقیماً داخل خود برنامه قرار گرفته‌اند و نیازی به دانلود جداگانه ندارند.
▫️
دریافت خودکار دسترسی Administrator
هر زمان دسترسی ادمین لازم باشد، برنامه خودش پیام تأیید ویندوز را نمایش می‌دهد و با سطح دسترسی لازم دوباره اجرا می‌شود. دیگر نیازی به راست‌کلیک و انتخاب
Run as administrator
نیست.
▫️
اطلاع‌رسانی نسخه‌های جدید
در صورت انتشار نسخه جدید، یک نوار اطلاع‌رسانی بالای برنامه ظاهر می‌شود که با یک کلیک شما را به صفحه دانلود می‌برد.
▫️
چهار تنظیم جدید موتور
تنظیمات بیشتری برای موارد زیر اضافه شده است:
Local Proxy
Domain Sniffing
Identity Re-registration
Keepalive
مقدار پیش‌فرض
Keepalive
نیز از ۵ ثانیه به ۲۵ ثانیه تغییر کرده است.
▫️
عبور مستقیم ترافیک شبکه محلی
ترافیک دستگاه‌های داخل شبکه مثل Printer، Router و NAS دیگر به نود خروجی فرستاده نمی‌شود و مستقیماً در شبکه محلی باقی می‌ماند.
▫️
رفع مشکل آیکون‌های مرده در Taskbar
حالا در تمام حالت‌های خروج از برنامه، آیکون آن به‌درستی از Taskbar و System Tray حذف می‌شود.
▫️
حذف اتصال خودکار
برنامه دیگر بدون اجازه کاربر به‌صورت خودکار متصل نمی‌شود. زمان اتصال کاملاً در اختیار شماست.
▫️
باز شدن صحیح پنجره با کلیک روی آیکون برنامه
مشکلی که در حالت اجرای برنامه با دسترسی Administrator باعث می‌شد ویندوز فرمان باز شدن پنجره را مسدود کند، برطرف شده است.
🛡
۱. حالت Full Tunnel — جلوگیری کامل از DNS Leak
تا الان دو حالت داشتیم:
▫️
فقط همین برنامه
▫️
کل دستگاه
مشکل حالت دوم این بود که فقط برنامه‌هایی را پوشش می‌داد که از تنظیمات Proxy ویندوز استفاده می‌کنند.
خیلی از برنامه‌ها این تنظیمات را نادیده می‌گیرند و مستقیماً به اینترنت یا DNS وصل می‌شوند. در نتیجه ممکن بود بخشی از ترافیک خارج از تونل عبور کند.
حالت جدید
Full Tunnel
یک کارت شبکه مجازی ایجاد می‌کند و
تمام ترافیک سیستم
را از تونل عبور می‌دهد؛ حتی برنامه‌هایی که Proxy سیستم را نادیده می‌گیرند.
این حالت بهترین گزینه برای جلوگیری از DNS Leak است.
🔹
روش فعال‌سازی
۱. برنامه را باز کنید و متصل شوید.
۲. پایین صفحه اصلی سه حالت وجود دارد.
۳. گزینه سوم یعنی Full Tunnel را انتخاب کنید.
۴. ویندوز برای دسترسی لازم از شما اجازه می‌خواهد. گزینه Yes را بزنید.
۵. برنامه به‌صورت خودکار بسته و دوباره با دسترسی لازم اجرا می‌شود.
دیگر لازم نیست روی برنامه راست‌کلیک کرده و Run as administrator را انتخاب کنید.
✅
برای تست
بعد از اتصال، سایت زیر را باز کنید:
dnsleaktest.com
سپس گزینه Extended Test را اجرا کنید.
سرورهای نمایش‌داده‌شده باید مربوط به کشور نودی باشند که به آن متصل شده‌اید.
━━━━━━━━━━━━━━━━━━
🇮🇷
۲. خروج خودکار سایت‌های ایرانی از تونل
دیگر لازم نیست برای باز کردن بانک‌ها، دیجی‌کالا، آپارات و سرویس‌های داخلی، هر بار VPN را خاموش کنید.
سایت‌های داخلی معمولاً نیازی به عبور از تونل ندارند. عبور آنها از تونل فقط می‌تواند سرعت را کاهش دهد و پهنای باند نود را مصرف کند.
حالا می‌توانید کاری کنید که:
سایت‌های ایرانی مستقیم باز شوند و بقیه ترافیک از تونل عبور کند.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS → Routing Rules
سپس گزینه زیر را روشن کنید:
Iranian sites bypass the tunnel
لیست موردنیاز داخل خود برنامه قرار دارد و شامل:
▫️
۲۹۰۶ رنج IP ایران
▫️
۴۱٬۷۲۹ دامنه
است.
هیچ فایلی هنگام اتصال دانلود نمی‌شود؛ بنابراین این قابلیت حتی زمانی که دسترسی آزاد به اینترنت ندارید نیز قابل استفاده است.
━━━━━━━━━━━━━━━━━━
📱
۳. اشتراک اینترنت با گوشی، تلویزیون و دستگاه‌های دیگر
حالا می‌توانید کامپیوتر خود را به یک Proxy Server تبدیل کنید و دستگاه‌های دیگر را از طریق آن به اینترنت متصل کنید.
بدون نیاز به نصب WhiteAesther روی گوشی.
🔹
روش فعال‌سازی
به مسیر زیر بروید:
Advanced → Traffic & DNS
در بخش:
Share with other devices
گزینه اشتراک‌گذاری را روشن کنید.
برنامه یک آدرس مشابه این نمایش می‌دهد:
192.168.1.24:1080
بار اول ویندوز ممکن است از شما اجازه Firewall بخواهد.
گزینه:
Allow access
را انتخاب کنید.
اگر اجازه ندهید، Proxy فقط روی همان کامپیوتر قابل استفاده خواهد بود.
📱
در Android
وارد تنظیمات Wi-Fi شوید.
شبکه متصل را باز کنید و به بخش تنظیمات Proxy بروید.
حالت Proxy را روی Manual قرار دهید.
برای مثال:
Hostname:
192.168.1.24
Port: 1080
همان IP و پورتی را وارد کنید که WhiteAesther نمایش داده است.
🍎
در iPhone
به مسیر زیر بروید:
Settings → Wi-Fi
روی علامت (i) کنار شبکه بزنید.
سپس:
Configure Proxy → Manual
را انتخاب کرده و IP و Port نمایش‌داده‌شده در WhiteAesther را وارد کنید.
🔐
نکته امنیتی مهم
اگر Username و Password تعیین نکنید،
هر دستگاهی که به همان شبکه Wi-Fi متصل باشد می‌تواند از Proxy شما استفاده کند.
در شبکه خانگی شاید این موضوع مهم نباشد، اما در محل کار، دانشگاه، هتل یا کافه حتماً هر دو فیلد زیر را پر کنید:
Username
Password
خود برنامه نیز در صورت خالی بودن آنها با یک هشدار زرد به شما اطلاع می‌دهد.
یک Port برای هر دو پروتکل استفاده می‌شود:
HTTP
و
SOCKS5
بنابراین همان شماره Port را برای هرکدام که دستگاه شما پشتیبانی می‌کند وارد کنید.
━━━━━━━━━━━━━━━━━━
⚡️
۴. پشتیبانی بهتر از Hysteria2 و TUIC
اگر در Subscription شما نودهای Hysteria2 وجود داشتند و همیشه علامت — نمایش داده می‌شد، این مشکل اکنون برطرف شده است.
مشکل از اندازه Packet بود.
این پروتکل‌ها Packetهایی با اندازه حدود ۱۲۸۰ بایت ارسال می‌کنند، در حالی که تونل قبلی فقط ۱۲۵۲ بایت ظرفیت داشت.
در نتیجه حدود
۲۸ بایت کمبود ظرفیت
باعث می‌شد Packet قبل از ارسال حذف شود.
🔹
روش استفاده
به مسیر زیر بروید:
Advanced → Routes & Transports
سپس Protocol را روی:
WireGuard
قرار دهید.
برای این نودها از MASQUE استفاده نکنید.
در حالت MASQUE این محدودیت از سمت Cloudflare وجود دارد و برنامه نیز کنار نود توضیح می‌دهد که چرا قابل استفاده نیست.
━━━━━━━━━━━━━━━━━━
🔔
۵. اطلاع‌رسانی نسخه‌های جدید
از این نسخه به بعد، وقتی نسخه جدید WhiteAesther منتشر شود، خود برنامه به شما اطلاع می‌دهد.
یک نوار اطلاع‌رسانی در بالای برنامه نمایش داده می‌شود.
با زدن گزینه:
Get it
مستقیماً وارد صفحه دانلود نسخه جدید خواهید شد.
━━━━━━━━━━━━━━━━━━
🔧
سایر تغییرات
▫️
نودهای REALITY حالا با برچسب Not Supported مشخص می‌شوند.
موتور فعلی از آنها پشتیبانی نمی‌کند، بنابراین بهتر است وضعیت آنها واضح باشد تا اینکه نودی نمایش داده شود که هیچ‌وقت متصل نمی‌شود.
▫️
Subscriptionها کامل‌تر پردازش می‌شوند و مشکل جا افتادن بعضی نودها برطرف شده است.
▫️
مشکل باقی ماندن آیکون‌های قدیمی برنامه در Taskbar برطرف شده است.
▫️
برنامه دیگر به‌صورت خودکار متصل نمی‌شود. تصمیم برای اتصال کاملاً با کاربر است.
▫️
تنظیمات بیشتری برای Local Proxy، Keepalive و گزینه‌های پیشرفته اضافه شده است.
▫️
موتور برنامه به نسخه زیر ارتقا پیدا کرده است:
Aether 1.7.0
@WhiteDNS_Laurie</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1641" target="_blank">📅 05:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1640">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ek6U0ZCQ29vfVt5TNUcrl4lZ0XC-wCoaUc-o0sYZDYifksg3gtK6n5bw6JpED3VlgTK3cc8pGsofcgrY7faD-UD1uwdk5uafXhZiBSQBTRS5MWpEHl0uRA5ykB_7U9QtBgwiJKssnZTb8DXkPiMrB8iJxKQ2dODqKXRhMEAFH1Hzcrc5my-mm0FYtdZc8Xg3v692fQH-cftwYPD9oa-QXgIKILtpnCtJOwqv193-4SheLwya7JsLpBHL--mj5545gSs5pKy8w6jsm1e1t9tkw0DliY6R0sncehay7K1KHQ_Wf1aX0hbQW8jmVua2JTW21WGpvJIXkVgU9_-iNbbAmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخه 1.6.0 دسکتاپ  WhiteAesther منتشر شد
بزرگ‌ترین آپدیت WhiteAesther تا امروز.
حالا می‌توانید:
▫️
کل کامپیوتر را تونل کنید
▫️
سایت‌های ایرانی را از تونل خارج نگه دارید
▫️
اینترنت را با گوشی، تلویزیون و دستگاه‌های دیگر به اشتراک بگذارید
━━━━━━━━━━━━━━━━━
📥
دانلود
github.com/WhiteDNS/WhiteAesther/releases
نسخه‌های موجود:
▫️
Windows
▫️
Linux —
deb / rpm / AppImage
▫️
macOS Intel
▫️
macOS Apple Silicon
━━━━━━━━━━━━━━━━━━
⚠️
نکته مهم قبل از تست
اگر برنامه رسمی
Cloudflare WARP
روی سیستم شما نصب است، قبل از استفاده از WhiteAesther حتماً آن را کاملاً
Disconnect
کنید.
اجرای همزمان دو VPN روی مسیر شبکه می‌تواند باعث تداخل، قطع اتصال یا نتایج گیج‌کننده شود.
━━━━━━━━━━━━━━━━━━
💬
اگر سؤال یا مشکلی داشتید، همین‌جا مطرح کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/1640" target="_blank">📅 05:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1636">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBlue Knight(𝑫𝒊𝒂𝒏𝒂🍓)</strong></div>
<div class="tg-text">آموزش تغییر لوکیشن با Exit Chain
داخل اپ‌های WhiteVPN و WhiteAesther
🔥
واسه gemini و بقیه AI هایی ک نیاز دارین عالیه
https://youtu.be/yx-jFqv9pYM?si=VuY0qqm5qbFUJOO6</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1636" target="_blank">📅 03:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1634">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔗
نسخه ۱.۲.۳ اندروید WhiteAesther منتشر
شد ......!
در نسخه جدید سه بخش مهم اضافه شده:
🛡
قفل ایمنی
🧭
قواعد مسیریابی
⚙️
چند تنظیم جدید برای موتور اتصال
پایین، همه موارد را همراه با آموزش توضیح داده‌ایم.
🛡
۱. قفل ایمنی — Kill Switch
چه مشکلی را حل می‌کند؟
تا الان اگر تونل بعد از چند بار تلاش وصل نمی‌شد، برنامه تسلیم می‌شد و گوشی بی‌صدا به اینترنت معمولی برمی‌گشت.
حالا می‌توانید مشخص کنید که در چنین شرایطی، به‌جای برگشت به اینترنت عادی،
تمام ترافیک اینترنت مسدود شود.
آموزش
۱) وارد بخش Traffic شوید.
۲) بخش Advanced را باز کنید.
۳) گزینه زیر را روشن کنید:
Block traffic if the tunnel fails
تمام! از این به بعد اگر تونل از کار بیفتد، هیچ ترافیکی از گوشی خارج نمی‌شود.
🔸
حالت سخت‌گیرانه‌تر
بعد از فعال کردن گزینه بالا، گزینه دیگری ظاهر می‌شود:
Keep blocking after you disconnect
اگر این گزینه را روشن کنید،
حتی زمانی که خودتان اتصال را دستی قطع می‌کنید، اینترنت همچنان مسدود می‌ماند
تا خودتان آن را آزاد کنید.
⚠️
توجه:
در این حالت گوشی واقعاً اینترنت نخواهد داشت. اگر فراموش کنید این گزینه فعال است، ممکن است فکر کنید اینترنت یا شبکه مشکل دارد.
برای برداشتن قفل دو راه دارید:
▫️
از نوتیفیکیشن Traffic is blocked
▫️
یا از صفحه اصلی برنامه و دکمه Lift the block
اگر دوباره به تونل متصل شوید، قفل به‌صورت خودکار برداشته می‌شود.
🧭
۲. قواعد مسیریابی — Routing Rules
چه مشکلی را حل می‌کند؟
بعضی سایت‌ها و اپلیکیشن‌ها با IP خارجی درست کار نمی‌کنند؛ مثل بعضی بانک‌ها، اپ‌های داخلی یا سرویس‌های ایرانی.
قبلاً برای استفاده از آنها مجبور بودید VPN را کاملاً خاموش کنید.
حالا می‌توانید مشخص کنید که
فقط بعضی سایت‌ها یا سرویس‌ها از تونل عبور نکنند
و بقیه ترافیک همچنان از تونل استفاده کند.
آموزش
۱) وارد بخش Routes شوید.
۲) در کارت اول، گزینه Routing rules را که زیر Exit chain قرار دارد انتخاب کنید.
۳) دو کادر خواهید دید:
🔹
کادر
Never connect
هر چیزی که اینجا قرار بگیرد، اصلاً اجازه اتصال نخواهد داشت.
مناسب برای مسدود کردن تبلیغات، ردیاب‌ها و دامنه‌های ناخواسته.
🔹
کادر
Skip the tunnel
هر چیزی که اینجا قرار بگیرد،
بدون تونل و با IP واقعی شما
باز می‌شود.
مناسب برای بانک‌ها، سایت‌ها و اپلیکیشن‌های داخلی.
هر قانون را در یک خط جداگانه بنویسید.
مثال:
bank.example.ir
digikala.com
snapp.ir
نوشتن یک دامنه، زیرمجموعه‌های آن را هم شامل می‌شود.
برای مثال:
digikala.com
شامل این مورد هم خواهد شد:
www.digikala.com
حالت‌های پیشرفته
▫️
فقط همان دامنه دقیق:
full:
example.com
▫️
هر آدرسی که یک کلمه خاص داخل آن باشد:
keyword:tracker
▫️
یک محدوده IP:
cidr:
10.0.0.0/8
▫️
یک پورت مشخص:
port:25
▫️
کل شبکه محلی:
private
▫️
هر خطی که با # شروع شود، به‌عنوان توضیح در نظر گرفته شده و اجرا نمی‌شود.
⚠️
مهم:
هر چیزی که داخل Skip the tunnel قرار دهید، با
IP واقعی شما
به اینترنت متصل می‌شود. بنابراین این لیست را فقط برای موارد ضروری استفاده کنید.
🔸
نکته مهم درباره دامنه‌ها
در مسیر زیر:
Traffic ← Advanced
گزینه‌ای وجود دارد با نام:
Match rules on domain names
این گزینه به‌صورت پیش‌فرض روشن است و بهتر است روشن بماند.
اگر آن را خاموش کنید، قوانینی که با نام دامنه نوشته شده‌اند ممکن است کار نکنند؛ چون برنامه در اندروید معمولاً ترافیک را در سطح IP دریافت می‌کند.
در صورت خاموش بودن این گزینه، خود صفحه Routing rules نیز هشدار خواهد داد.
⚙️
۳. تنظیمات جدید موتور
تمام این تنظیمات در مسیر زیر قرار دارند:
Traffic ← Advanced
🔹
تنظیم DNS داخل تونل
گزینه:
DNS inside the tunnel
می‌توانید DNS دلخواه خودتان را وارد کنید.
مثال:
8.8.8.8
,
1.1.1.1
اگر خالی بگذارید، DNS پیش‌فرض موتور استفاده می‌شود.
آدرس‌های نامعتبر نیز به‌صورت خودکار نادیده گرفته می‌شوند.
🔹
اتصال تونل از طریق یک پروکسی دیگر
گزینه:
Dial out through a proxy
این قابلیت یکی از مواردی بود که کاربران زیادی درخواست کرده بودند.
اگر ابزار دیگری روی گوشی شما در حالت پروکسی فعال است، مثلاً
Psiphon
، می‌توانید اتصال WhiteAesther را از داخل آن عبور دهید.
مسیر اتصال به این شکل می‌شود:
گوشی ← WhiteAesther ← Psiphon ← اینترنت
برای مثال اگر پروکسی SOCKS روی پورت ۱۰۸۰ فعال باشد، وارد کنید:
socks5://127.0.0.1:1080
پورت را باید با پورت واقعی برنامه پروکسی خودتان جایگزین کنید.
پروکسی HTTP نیز پشتیبانی می‌شود:
http://127.0.0.1:8080
🔹
تنظیم WireGuard Keepalive
این گزینه می‌تواند روی مصرف باتری تأثیر داشته باشد.
سه مقدار قابل انتخاب است:
▫️
۵ ثانیه
▫️
۱۵ ثانیه
▫️
۲۵ ثانیه
مقدار پیش‌فرض در نسخه جدید
۲۵ ثانیه
است. در نسخه‌های قبلی مقدار پیش‌فرض ۵ ثانیه بود.
هر بار که این زمان می‌گذرد، گوشی یک بسته کوچک ارسال می‌کند تا اتصال فعال بماند.
در حالت ۵ ثانیه، این کار بسیار بیشتر انجام می‌شود و مخصوصاً روی اینترنت موبایل می‌تواند باعث مصرف بیشتر باتری شود.
مقدار ۲۵ ثانیه نیز مقدار رایج استاندارد WireGuard است.
⚠️
اگر بعد از آپدیت متوجه شدید اتصال WireGuard بعد از چند دقیقه بی‌کاری قطع می‌شود، مقدار را دوباره روی
۵ ثانیه
قرار دهید.
🔹
جایگزینی هویت ردشده
گزینه:
Replace a refused identity
این گزینه به‌صورت پیش‌فرض روشن است.
اگر Cloudflare هویت ذخیره‌شده روی گوشی را دیگر قبول نکند، برنامه به‌صورت خودکار یک هویت جدید دریافت می‌کند.
بدون این قابلیت ممکن است تونل ظاهراً متصل شود، اما هیچ ترافیکی از آن عبور نکند.
📌
خلاصه محل تنظیمات
بخش
Routes
▫️
Protocol
— مثل قبل
▫️
Endpoint
— مثل قبل
▫️
Exit chain
— مثل قبل
▫️
Routing rules
—
جدید
بخش
Traffic ← Advanced
▫️
Obfuscation
— مثل قبل
▫️
Local proxy port
— مثل قبل
▫️
Share with this network
— مثل قبل
▫️
DNS inside the tunnel
—
جدید
▫️
Dial out through a proxy
—
جدید
▫️
WireGuard keepalive
—
جدید
▫️
Block traffic if the tunnel fails
—
جدید
▫️
Match rules on domain names
—
جدید
▫️
Replace a refused identity
—
جدید
⬇️
دانلود آخرین نسخه
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
— مناسب تقریباً همه گوشی‌های سال ۲۰۱۷ به بعد؛
اول این نسخه را امتحان کنید.
▫️
armeabi-v7a
— مخصوص گوشی‌های قدیمی‌تر
▫️
universal
— اگر مطمئن نیستید؛ حجم این نسخه تقریباً سه برابر است.
اگر با مشکلی مواجه شدید، از مسیر زیر گزارش بگیرید:
Settings ← Diagnostics
و برای ما ارسال کنید.
@whitedns</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1634" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ZqcfdMPmN-VpbPWFEL6JpT9K3xupB3dln0XroQwKjMMJKzFbYJzDEV-uTfbzcrILmSSYiV4YoN4IA4Q60D7Kpz9TxYm-lX37GRLimj_xF7WZ65zjwN0YfuqKZZpUawa-lmituFlBPvK6GFCkfcDhCSu_55jw_Lo1aQAWTbSMHSJEsYenwvwUTnei4lYNknwWENmszmYxxebMxgBp8IuNi06fZv-W1UTQUNmc1sP4ono7VO5hhPOjke1Qdvz-n7PHhyXowldUvX3N6kETr_UsqDtyC_VZMqRM8fqna7Jlh3eL0CfOBOw0mkYFlf9M2ciKhCcGUOyMz6rvq15cd-mQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔜
به‌زودی:  WhiteAesther  اندروید نسخه ۱.۲.۳
🔥
🔥
🔥
▫️
قفل ایمنی (Kill switch) — اگه تونل بمیره، ترافیک بی‌صدا لو نمی‌ره
▫️
قواعد مسیریابی — بگین کدوم سایت‌ها بدون تونل باز بشن (بانک، اپ‌های داخلی)
▫️
اتصال یه پروکسی دیگه (مثل سایفون)
▫️
امکان DNS دلخواه داخل تونل (برای کاهش پینگ)
▫️
بهینه‌سازی مصرف باتری روی WireGuard
@whitedns</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1632" target="_blank">📅 16:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jJ0yk9YxbfbcWOQvAGrc_fke1gv3ciFUrt8l4geuG6fzr3_eQvfxsdBVNPCSOXfZ6RZqhRrsuhlktTBVNq6N8szGpJahAZL2-o21Gt6DgqDqDb-TknkcVWRuEkngU8C7fUIgBW2riCZU8V4dGk_fzZloMVa9dLdb3o0yeXX7F_smvOiaWhuWN9pvVK3POO_pI_eAbU4XOly3ln_W7MPs9rssvdhZ-cGJR7ug4oGhdv8xPHNdSFho5pA0BoCwaO1fPBgmVDBagySDHffPGLuGOQCaYPqdctsgDUY0b8GCYyuzUCAUCjpcZS2vBzjHI6mHoFa9ZT8vo0C-lQeUCJIZdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کلاینت WhiteAesther
(دانلود همزمان برای اندروید و ویندوز / دسکتاپ)
اگر به دنبال یک اتصال فوق‌العاده پایدار، سریع و امن با پروتکل نوین MASQUE H2 هستید، نرم‌افزار WhiteAesther در دو نسخه دسکتاپ و موبایل در دسترس شماست.
✨
قابلیت‌ها و ویژگی‌های کلیدی:
🔹
مبتنی بر پروتکل پرسرعت و مدرن MASQUE H2
🔹
اتصال سریع با یک کلیک (Zero-Config)
🔹
پایداری بالا و پینگ عالی مناسب وب‌گردی، گیمینگ و استریم
🔹
سیستم محافظت از کل ترافیک دستگاه (IPv4 + IPv6)
🔹
قابلیت Reconnect خودکار و Killswitch داخلی
🔹
رابط کاربری بسیار روان، تاریک (Dark Mode) و مدرن
━━━━━━━━━━━━━━━━━━━━
📥
لینک‌های دانلود مستقیم آخرین نسخه از گیت‌هاب:
📱
دانلود نسخه اندروید (Android APK):
🔗
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
💻
دانلود نسخه دسکتاپ (Windows / PC):
🔗
https://github.com/WhiteDNS/WhiteAesther/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
پیشنهاد: این پست را برای دسترسی سریع به هر دو نسخه ذخیره (Save) یا پین کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/whitedns/1631" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SE_zRHoCGC2vA6orsmd3pP-58DRxn6aAgacI5xemFh93HG8lXllhFxTwnpf6zV3TYG5qwhBQeNRpVz5FKa6wUbKzqDYCRRS9Au3R-h5gaEGUtfDq4bJKSF7oopZFtU4uaCF92Dwomh5V5fh4gGN_ig-YCs9my3qJxn4EpmVBpJunYHFhmZJ4lDi81Mvp9APvkUyEHpdIhJGWeATTBy6h4L9ZycwPBD0nrqtSlBbAnnWCWgHFvgpJCe2ep6Th9n0tBjChmBueGYEoPJbu_v90rH8zzIWez__cmv2TIAbKkqKNbsRXN5OKdha3wmZLOv-ZVzRb-M3BXDSPElmRYbnqCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی آزاد و امن به اینترنت با WhiteVPN (نسخه موبایل و دسکتاپ)
اگر به دنبال یک کلاینت یکپارچه، سبک و حرفه‌ای هستید، WhiteVPN با رابط کاربری مدرن در دسترس شماست!
⚙️
قدرت گرفته از هسته Mihomo:
این برنامه بر پایه هسته قدرتمند Mihomo (مشابه کلش و متا) توسعه یافته است که بالاترین سطح پایداری و سرعت را در دور زدن محدودیت‌ها برای شما فراهم می‌کند.
⚠️
توجه مهم:
این اپلیکیشن کاملاً سورس‌باز (Open-Source) است و در Google Play یا App Store منتشر نشده است. تنها منبع رسمی برای دانلود، مخزن گیت‌هاب پروژه است.
✨
ویژگی‌های کلیدی:
🔹
پشتیبانی همزمان از ویندوز، مک، لینوکس و اندروید
🔹
رابط کاربری ساده و اتصال تنها با یک کلیک
🔹
سیستم پراکسی جامع و تونلینگ کل سیستم (System-wide)
🔹
مدیریت پیشرفته سرورها و پایداری بالا در اتصالات
━━━━━━━━━━━━━━━━━━━━
📥
دانلود مستقیم آخرین نسخه از گیت‌هاب (رسمی):
📱
نسخه اندروید (Mobile):
🔗
https://github.com/WhiteDNS/WhiteVPN/releases/latest
💻
نسخه دسکتاپ (Windows / macOS / Linux):
🔗
https://github.com/WhiteDNS/WhiteVPN-Desktop/releases/latest
━━━━━━━━━━━━━━━━━━━━
💡
برای دانلود، وارد لینک‌های بالا شده و از بخش "Assets" فایل متناسب با دستگاه خود (فایل apk برای اندروید و فایل‌های نصب برای ویندوز/مک) را دانلود کنید.
🆔
@whitedns</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/whitedns/1630" target="_blank">📅 10:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1627">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سابسکریپشن WhiteDNS برای اپ های WhiteVPN / Karing / Clash Mi / Clash Party / FLClash :
https://raw.githubusercontent.com/iampedii/whitedns-sub/refs/heads/main/mihomo.yaml
@whitedns</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1627" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1626">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">Live stream finished (1 hour)</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1626" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYIUAf3px4-E4eTm1RN5cAWTpCSsTiwn2cyZ5iFqJq0s8Q6xBE3lvqKp9aiXb0rxRdF_89Y9O4JEUeUVKiUJgsQ2vmc2Lvqcxk6tyckosB4_iCTE-HYoI_k8WhzgIUQ26JsvkrtVpCQ6tYGJsIwwAhjMpcBhyA5YPursaduGdCqM7w7wH7dUsULG86TaWkMsWgWK1GK9izRf3TeMzCzoQTlC4dPxIpnYRF--mWX9g0sh5Quyl2ProBIM0MJbKOyBwH4FEPHj4X36MSGqwqX9LI30k2hD4oAH4Zwb-8BIp_XNGE4s8eWHJh9ikOy5_Hq3DlRHd_-rpaHbUNB3kexILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
یک پورت برای حکومت بر همه!
آموزش نصب و راه‌اندازی CottenRouter
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
اگر روی یک سرور چند DNS Tunnel مختلف داشته باشید، خیلی زود به یک مشکل می‌خورید: همه‌شون پورت عمومی 53 رو می‌خوان.
سرویس CottenRouter دقیقاً برای حل همین مشکل ساخته شده. جلوی تمام سرویس‌ها قرار می‌گیره، دامنه هر درخواست رو تشخیص می‌ده و بدون دست‌کاری Packet، اون رو به Backend درست می‌فرسته.
یعنی می‌تونید CottenDNS، MasterDnsVPN، StormDNS، thefeed و سرویس‌های مدیریت‌شده با SlipGate رو هم‌زمان روی یک سرور و یک IP اجرا کنید؛ بدون جنگ بر سر پورت 53.
✍️
توی این ویدیو می‌بینیم:
• سرویس CottenRouter دقیقاً چه مشکلی رو حل می‌کنه
• مسیریابی درخواست‌ها بر اساس Domain چطور انجام می‌شه
• چطور چند DNS Tunnel روی یک IP اجرا می‌شن
• پشتیبانی از DNS، DoT و HTTPS
• تفاوت نصب مستقیم با Docker
• پنل مانیتورینگ، محدودسازی ترافیک و قابلیت‌های امنیتی
• نحوه نصب و اتصال Backendها
سرویس CottenRouter هیچ Label یا داده اضافه‌ای وارد Packet نمی‌کنه؛ پس فضای قابل استفاده Tunnel و MTU رو هم کاهش نمی‌ده.
🇺🇦
تماشا در یوتیوب
https://youtu.be/N725_-A_-B8
🔗
سورس‌کد و راهنمای نصب:
https://github.com/TaJirax/CottenRouter
اگر با DNS Tunnelها کار می‌کنید، این پروژه احتمالاً کلی دردسر از مدیریت سرورتون کم می‌کنه.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/1618" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔭
یک خبر خوب برای کاربران WhiteVPN
🟢
یک فیلتر جدید به سابسکریپشن
اپلیکیشن ‌های
WhiteVPN اضافه کردیم تا کانفیگ‌هایی که هنگام استفاده از ChatGPT و سرویس‌های OpenAI خطا ایجاد می‌کردند، به‌صورت خودکار از لیست حذف شوند.
🟢
از این به بعد، با تمام کانفیگ‌های موجود در سابسکریپشن باید بتوانید بدون دردسر به ChatGPT و سایر سرویس‌های OpenAI دسترسی داشته باشید.
🟢
برای دریافت لیست جدید، کافی است سابسکریپشن WhiteVPN را یک‌بار به‌روزرسانی کنید.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/whitedns/1616" target="_blank">📅 11:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1610">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NulRBdHQcpprf2Ziq8-N-PgCrx2-eHtvY7MkEDuUKm5BDZZ1kEEbpGP7T-VXijbHV84o2CYhwEkVzuNLEdomAwsAed2zyLb0UFLE272h655L9jGYzYLidKbOVgTXGLSJqcHOdrX6l9uyif_dPnlpEuvNDufz-dBK2GYv9Kw7ZN-hZDrikcGUpDdMpBqtMN2J6dDRBRXUN9q9e6T78au8J1TFx2RiGKsWQ3BB-OiVoTgb40GoyOHoNE1TlVjyj8hLNEcTVkuyW4nKENvVSwUZ7kNBm4V_0cRDMXZ4cka7H0clpQAxo72U34fZSeuKMjmsbEOPF9HypyuZ65QUMdm97A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Whitedns Chatbot V4 (جدید)
🎉
🎉
🎉
@WhiteDnsResponder_bot
راهنمای استفاده از ربات WhiteDNS
سلام!
این ربات به شما کمک می‌کند پاسخ سوال‌های مربوط به WhiteDNS، ابزارهای اتصال، DNS، نصب برنامه‌ها و رفع مشکلات رایج را از میان مطالب منتشرشده پیدا کنید.
آموزش :
⚠️
👇
### ۱. پرسیدن سوال معمولی
💬
کافی است سوالتان را مستقیماً برای ربات بنویسید.
نمونه‌ها:
- چطور WhiteDNS را روی اندروید نصب کنم؟
📱
- آخرین نسخه برنامه چیست؟
- چرا DNS وصل نمی‌شود؟
🌐
- تنظیمات ویندوز را چطور انجام بدهم؟
🖥
برای دریافت پاسخ بهتر، نام برنامه، دستگاه یا سیستم‌عامل و متن دقیق خطا را در یک پیام بنویسید.
ربات ممکن است همراه پاسخ، دکمه‌های منبع را نیز نمایش دهد. با انتخاب آن‌ها می‌توانید مطلب اصلی کانال را مشاهده کنید.
📎
### ۲. عیب‌یابی مرحله‌ای با /diagnose
🔧
اگر مشکل فنی دارید و نمی‌دانید چطور آن را توضیح دهید، دستور زیر را انتخاب کنید:
/diagnose
ربات از شما سه مورد کوتاه می‌پرسد:
1. نوع مشکل، مانند وصل نشدن، سرعت پایین، DNS یا نصب
2. دستگاه یا سیستم‌عامل
3. توضیح کوتاه مشکل یا متن دقیق خطا
پس از دریافت راه‌حل، این گزینه‌ها نمایش داده می‌شوند:
-
✅
حل شد — اگر مشکل برطرف شده است.
-
🔁
راه دیگر — دریافت یک راه‌حل جایگزین.
-
👤
ارسال برای مدیر — آماده‌کردن گزارش برای مدیران.
برای جلوگیری از طولانی‌شدن مراحل، ربات فقط یک راه‌حل جایگزین ارائه می‌دهد.
### ۳. ارسال نتیجه عیب‌یابی برای مدیر
اگر راه‌حل‌های ربات مؤثر نبودند، گزینه ارسال برای مدیر را انتخاب کنید.
قبل از ارسال، ربات پیش‌نمایشی شامل موارد زیر نشان می‌دهد:
- نوع مشکل
- دستگاه یا سیستم‌عامل
- توضیح شما
- راه‌حل‌هایی که امتحان کرده‌اید
- نام تلگرام
- نام کاربری، در صورت وجود
- شناسه عددی کاربر و گفتگو
- زبان حساب تلگرام
درخواست فقط بعد از انتخاب تأیید و ارسال برای مدیران فرستاده می‌شود.
### ۴. جستجوی مستقیم با /search
برای پیدا کردن مطالب کانال بدون ساخت پاسخ جدید، از این دستور استفاده کنید:
/search عبارت موردنظر
مثال:
/search نصب WhiteDNS اندروید
ربات نزدیک‌ترین مطالب را همراه دکمه مشاهده منبع نشان می‌دهد.
### ۵. ارسال پیام مستقیم به مدیران با /contact
اگر موضوع شما با عیب‌یابی قابل حل نیست، دستور زیر را انتخاب کنید:
/contact
سپس تمام توضیحات خود را در یک پیام کامل بفرستید. بهتر است پیام شامل این موارد باشد:
- نام برنامه
- دستگاه یا سیستم‌عامل
- نسخه برنامه
- نوع اتصال
- متن دقیق خطا
- کارهایی که قبلاً امتحان کرده‌اید
مدیران اطلاعات حساب تلگرام و پیام کامل شما را دریافت می‌کنند و می‌توانند از طریق ربات یا گفتگوی مستقیم پاسخ دهند.
شماره تلفن شما برای ربات قابل مشاهده نیست، مگر اینکه خودتان آن را داخل پیام ارسال کنید.
### ۶. ادامه سوال قبلی
ربات می‌تواند برای مدت کوتاهی ارتباط بین سوال‌های شما را تشخیص دهد.
مثال:
- پیام اول: «روش نصب WhiteDNS چیست؟»
- پیام بعدی: «برای اندروید چطور؟»
این زمینه گفت‌وگو حداکثر ۳۰ دقیقه و تا چهار نوبت نگه داشته می‌شود و به‌عنوان منبع واقعی پاسخ استفاده نمی‌شود.
### ۷. شروع گفت‌وگوی تازه با /new
اگر می‌خواهید موضوع قبلی فراموش شود، از این دستور استفاده کنید:
/new
این دستور زمینه موقت گفت‌وگو و عملیات نیمه‌تمام را پاک می‌کند.
### ۸. ثبت بازخورد
زیر پاسخ‌های ربات دو گزینه وجود دارد:
-
✅
مفید بود
-
❌
مفید نبود
بازخورد شما به مدیران کمک می‌کند پاسخ‌ها و مطالب ربات را بهتر کنند.
همچنین می‌توانید برای آخرین پاسخ از دستور زیر استفاده کنید:
/feedback
### ۹. لغو عملیات با /cancel
برای خروج از ارسال پیام، عیب‌یابی یا پاسخ‌دادن به یک درخواست فعال، بنویسید:
/cancel
فهرست دستورات
- /start — شروع کار با ربات
- /help — نمایش راهنما
- /diagnose — عیب‌یابی مرحله‌ای
- /search — جستجوی مستقیم در مطالب
- /feedback — ثبت بازخورد برای آخرین پاسخ
- /contact — ارسال پیام به مدیران
- /new — شروع گفت‌وگوی تازه
- /cancel — لغو عملیات فعال
محدودیت استفاده
برای کنترل هزینه و حفظ کیفیت سرویس:
- حداکثر ۳ درخواست هوش مصنوعی در هر ۵ دقیقه
- حداکثر ۵۰ درخواست هوش مصنوعی در روز
دستورهای ساده مانند /help، /search، /contact و بازخورد شامل این محدودیت هوش مصنوعی نمی‌شوند.
نکات مهم
- برای پاسخ دقیق‌تر، همه جزئیات مشکل را در یک پیام بنویسید.
- پاسخ‌ها بر اساس مطالب موجود WhiteDNS تولید می‌شوند و ممکن است برای مشکلات خاص کامل نباشند.
- در صورت حل‌نشدن مشکل، از مسیر عیب‌یابی و سپس ارسال گزارش برای مدیر استفاده کنید.
@whitedns</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1610" target="_blank">📅 11:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">"exit chain "
⚠️
✍️
راهنمای استفاده از
#exit_chain
در اپ whitevpn# اندروید
ساب را وارد کن - برو تنظیمات - برو زنجیره اتصال - برو افزونه بعد - اشتراکی که وارد کردی را از اون بالا انتخاب کن - یک تست اتصال بگیر - یکی از کانفیگ ها را انتخاب کن - وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# اندروید
📱
برو route - گزینه exit chain را روشن کن - یا ساب و یا کانفیگ را وارد کن - برگرد صفحه اول و وصل شو -
تمام
✅
راهنمای استفاده از
#exit_chain
در اپ whiteaesther# دسکتاپ
برو advanced - برو exit chain - ساب و یا کانفیگ را وارد کن - برگرد simple - کانکت را بزن - تمام
✅
👨‍💻
این سه پست را مطالعه کنید :
https://t.me/whitedns/1601
https://t.me/c/3869114465/152008
https://t.me/c/3869114465/151806</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1608" target="_blank">📅 10:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1605">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/D_xVNOM4VIF0AzrsOUgdg27cR0tgTuRUP0ijosiTkIEzNCVjYiDmkyfU49CR3IzacTdlVP9DD2KAOwXeZad2UNMjEELUNF5cFaL-N7A77AJDz9ADRCFdbRMEa1e-5_UrWsLfqSBMF3wORS5F9dd4CjHZhJk0Krasv0_yIIzgG4fsXOoyWSr12clSPeXtFnyIeoTRXLQEbWPIdJ0fF2eFXo1Q6-HjhtE27enH6pHpLB1xNZLLJ6zOHE5r1AAmqZJglEDHAGfsr59XpRd-RTYu1yBNhvv-_hnd2dENQ0OQUcn-B8gkA8oNrCKlRjsw5WbapsHWKxJfsD2thvKukAdrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔗
Wh
iteAesther
✍️
نسخه ۱.۲.۲  برای اندروید منتشر شد !
— موتور جدید و چند قابلیت
این آپدیت موتور تونل رو عوض می‌کنه و چند چیزی که کاربرها خواسته بودن اضافه می‌شه.
🟢
⚡️
موتور جدید (Aether 1.7.0)
▫️
مصرف حافظه محدود شد
— قبلاً هرچی اتصال طولانی‌تر می‌شد، حافظه‌ای که اپ می‌گرفت بیشتر می‌شد تا جایی که تونل می‌افتاد. حالا سقف داره.
▫️
WARP in WARP وقتی یک طرفش قطع بشه دوباره وصل می‌شه
به‌جای اینکه کلاً بمیره.
▫️
پیام خطای واقعی از Cloudflare
— اگه ثبت‌نام رد بشه، حالا می‌گه دلیلش چیه: آی‌پی علامت‌خورده، یا ثبت‌نام زیاد از این آدرس. قبلاً فقط می‌گفت شبکه مشکل داره.
✍️
نودهای hysteria2 و tuic توی Exit chain کار می‌کنن
اگه توی ساب‌تون نود hysteria2 یا tuic دارین و تا حالا هیچ‌وقت بالا نمی‌اومدن، دلیلش پیدا شد و درست شد.
✍️
ولی یک شرط داره:
باید پروتکل رو روی
WireGuard
بذارین (از
Routes ← Manual ← Protocol
).
روی MASQUE همچنان کار نمی‌کنه و این دست ما نیست — محدودیت خود Cloudflareست. اپ هم اگه ببینه روی MASQUE هستین بهتون می‌گه.
🟢
نودهای REALITY حالا مشخص می‌شن
اگه توی ساب‌تون نود REALITY دارین، قبلاً یا اصلاً نمی‌اومد یا می‌اومد و وصل نمی‌شد و معلوم نبود چرا. حالا با برچسب نارنجی
not supported
نشون داده می‌شه و قابل انتخاب نیست.
نود سالمه — موتور فعلی هنوز نمی‌تونه باهاش احراز هویت کنه. وقتی بتونه، خودبه‌خود دوباره کار می‌کنه.
🟢
اشتراک تونل با شبکه (LAN sharing)
می‌تونین تونل گوشی رو با بقیه دستگاه‌های همون وای‌فای به اشتراک بذارین — مثلاً لپ‌تاپ یا تلویزیون.
از
Traffic
حالت رو روی
Proxy
بذارین، بعد بخش Advanced رو باز کنین و
Share with this network
رو روشن کنین. اپ آدرسی که باید توی دستگاه دوم بزنین رو بهتون نشون می‌ده.
⚠️
رمز اختیاریه ولی حواستون باشه:
بدون رمز، هرکی روی اون وای‌فای باشه می‌تونه از تونل شما استفاده کنه و ترافیکش با هویت شما بیرون می‌ره. روی شبکه خونه خودتون مشکلی نیست؛ توی کافه و هتل و خوابگاه حتماً رمز بذارین.
🟢
صفحه اول: آی‌پی و مصرف
•
آی‌پی قبل و بعد از تونل
— که ببینین واقعاً عوض شده
•
سرعت لحظه‌ای دانلود و آپلود
و مجموع مصرف هر نشست
نکته: آی‌پی «بدون تونل» فقط وقتی خونده می‌شه که اپ باز باشه و وصل
نباشین
. اگه مستقیم بزنین connect، اون خونه خالی می‌مونه — این عمدیه، چون خوندنش وسط اتصال یعنی فرستادن آدرس واقعی‌تون از کنار همون تونلی که قراره مخفی‌ش کنه.
🟢
کلید روشن/خاموش توی پنل سریع
از
Settings
دکمه
Add a quick settings tile
رو بزنین. بعدش از پنل بالای گوشی بدون باز کردن اپ وصل و قطع می‌شین.
🟢
مشکل «Allow background running» که نمی‌رفت
روی بعضی گوشی‌ها (مخصوصاً شیائومی) هرچی اجازه می‌دادین، اون کارت باز هم می‌موند. دلیلش این بود که این گوشی‌ها تنظیم باتری خودشون رو دارن و اجازه رو فقط اونجا ثبت می‌کنن، ولی جواب استاندارد اندروید همچنان «نه» می‌مونه.
حالا اپ خودش می‌فهمه این اتفاق افتاده، شما رو می‌فرسته به تنظیمات درست گوشی، و یک دکمه
I've done this
داره که کارت رو ببنده.
📥
دانلود
https://github.com/WhiteDNS/WhiteAestherMobile/releases/latest
▫️
arm64-v8a
(۵۴ مگ) — تقریباً همه گوشی‌های ۲۰۱۷ به بعد. از این شروع کنین
▫️
armeabi-v7a
(۴۸ مگ) — گوشی‌های قدیمی‌تر
▫️
universal
(۱۵۷ مگ) — اگه مطمئن نیستین
اگه مشکلی خوردین، از
Settings ← Diagnostics
گزارش بگیرین و بفرستین.
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1605" target="_blank">📅 08:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/McoemQQ5ekXykc4QGG4aAn3hxMeUtWSGgS3VAlxOycxV0EL5TXIUoV6wQiY2b92LZTF_7kUwK-oJFKTxtVmPJ440KQiXxBsAVEQm5RN08SjN77t9BT3F67pAGqEXFITM0jk49iZPxJHSEIZwZO-0-MDH1GWBiAib4V-n9DyNNPsqWFrtnevksC2NfNSQC7b6BpNVjyAFKVI-jeefM66NSE27EkqFnQZaKM81Rdp0fjhBfZj3ebzfHnqqQkZbw4GU3r42jSTvwQMqj58kO4QgMG8MP_pjVj7RGVu_9WZe_nG9F9w7H7E9yIgQttBt2n8b_LKZXZjLcWo1UxCHOfy02g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
آپ
دیت جدید وایت‌استر برای دسکتاپ (WhiteAesther) منتشر شد!
نسخه:
v1.5.4
در این نسخه تغییرات بسیار جذاب و کاربردی برای راحتی بیشتر شما به برنامه اضافه شده است.
🔭
تغییرات این نسخه:
🟢
اشتراک‌گذاری اتصال در شبکه داخلی (LAN Share)
از این پس می‌توانید اتصال VPN فعال روی سیستم خود را به راحتی با سایر دستگاه‌های متصل به مودم یا شبکه (مثل گوشی موبایل، تلویزیون هوشمند یا لپ‌تاپ‌های دیگر) به اشتراک بگذارید!
🟢
نمایش هوشمند وضعیت گره‌ها (پشتیبانی بهتر از Node ها)
مشکل عدم نمایش وضعیت یا کار نکردن بی‌دلیل گره‌ها برطرف شد. حالا گره‌هایی که برنامه به هر دلیلی نمی‌تواند از آن‌ها استفاده کند (مثلاً نیاز به WireGuard دارند یا از پروتکل REALITY پشتیبانی نمی‌کنند) با
رنگ نارنجی
مشخص می‌شوند. با نگه‌داشتن نشانگر موس روی آن‌ها، می‌توانید دلیل دقیق عدم پشتیبانی را ببینید.
🟢
بهبود مسیریابی کل سیستم (Whole Machine)
(تغییرات نسخه 1.5.3)
حالت System Proxy حالا به درستی ترافیک کل سیستم را از طریق مسیر زنجیره‌ای فعال (Active Chain) شما عبور می‌دهد.
🔭
راهنمای استفاده از قابلیت LAN Share (اشتراک اینترنت با گوشی و
تلویزیون):
۱. در برنامه به بخش
Settings
(تنظیمات) بروید و تب
Traffic & DNS
را باز کنید.
۲. گزینه
"Share this connection on my network"
را فعال کنید.
۳. برنامه به شما یک
آدرس (IP)
و یک
پورت
(مثلاً 1080) نمایش می‌دهد.
۴.
امنیت اتصال:
در همین بخش می‌توانید یک
نام کاربری (Username)
و
رمز عبور (Password)
تعیین کنید تا فقط خودتان بتوانید به آن وصل شوید.
(
⚠️
توجه: اگر این دو کادر را خالی بگذارید، هر دستگاهی در شبکه وای‌فای شما می‌تواند بدون رمز از اینترنت آزاد سیستم شما استفاده کند).
۴. حالا وارد تنظیمات پروکسی (HTTP یا SOCKS5) در گوشی، تلگرام یا تلویزیون خود شوید، آی‌پی و پورت نمایش داده شده را وارد کنید و روی اتصال ضربه بزنید.
(نکته: در اولین استفاده از این قابلیت، فایروال ویندوز از شما یک تاییدیه می‌خواهد که باید روی گزینه
Allow Access
کلیک کنید تا پورت شبکه باز شود).
✍️
هم‌اکنون می‌توانید برنامه خود را به آخرین نسخه به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteAesther/releases/latest
#آپدیت
#وایت_استر
#WhiteAesther
#پروکسی
#تونل
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/whitedns/1603" target="_blank">📅 07:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tTl-rFeGkqGTMf5njz_B0j1cf1VpetlVp785bcaYCsWBRiG7cj34CuCecDNdM9h5te57uKiyET5dSYE-E5oEh05DMbpTf-OvmNOxnGvOSvlMuuzYvLXGV-xViH18xc1pIiAIiL1NV7mO6HianDoYHvL2qMbVFXHLhKIKOcWVUZf7FEqOSlopcKVH9xzJ5sxg-NzxNp9TYn5Ti6oOXUDkpLlAEPJJtB81oCUs2BIfKH6itIN2AiyXDRjgwN4Af61tn2svrJo8TTsSoYGta6v3FjrlLTfcS-11AH5Kj-gjjcUFNYnPGXCCNDDQwn1Q9gOg-R-93GNM8l7M91y4Q3uoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
نسخه جدید موبایل و دسکتاپ به زودی منتشر می‌شود!
این نسخه‌ها شامل چه مواردی است؟
🟢
بهبود عملکرد اتصال برنامه
🟢
ارتقا موتور به ۱.۷.۰
🟢
اضافه کردن امکان LAN sharing
🟢
رفع باگ
🟢
در اندروید امکان اضافه شدن به Quick setting
🟢
استفاده از wireguard و hysteria exit chain برای داشتن حداکثر سرعت
ممنون
@WhiteDNS
🔥</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1602" target="_blank">📅 19:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SSeKWclC_BZnxTh4GlOrpupzsa5y73PufhBLn8faMtDs4fyOsPP_1RTeqRqfUL0XoZReKvZIHunBrb-cfggPc4orP6zGweXrliogNkmA5FQUfVY7qafQuL7oHL8-KPixPjR-viK-lqKL5mWriDtmxS6Uauky5wLvaHoIyoXeXSuAflj4JMNtoGaSO7nDcFowNnR3ZQgzaN9Wk5K8jTTiMRGQcNjvZS_4TIJ_h3oAZjZ5gCs0ITV1Ys05G5TLOcVKGT0RbG5oV2v6EllIM6N0GPMNlptFOF0w_5XLdck6O0Dl20O78kCh2pUszauyXF_HhGV3r0hVmGdElGavPEOuBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم
⚠️
⚠️
⚠️
⚠️
⚠️
دوستان :
پست  را با دقت مطالعه کنید
https://t.me/whitedns/1568
این کانفیگ های برای قابلیت "exit chain" توی اپ whiteaester و whitevpn هست - که ip شما را ثابت میکنه و یک لایه امنیت بیشتر به شما میده چون TLS هست
چون خیلی از دوستان کانفیگ نداشتن و یا نگران امنیتشون بودند ما این امکان را فراهم کردیم .
این کانفیگ ها برای استفاده مستقیم در اپ هایی مثل v2rayng و غیره نیست، اگر قصد استفاده مستقیم دارید لطفاً درخواست ارسال نفرمایید
تشکر
@whitedns</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/whitedns/1601" target="_blank">📅 17:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-1600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/AskMT_Me0r3eGPbwc1W3vCwJ-nUzYQ7jDQJIYNaIYGc28qiCqDvwCSWACYrvHhf-y8xpvp3fF2h8ZvVrpRmOXHA8STm_hpIHK_8Q0GxmfjxxWuyRYI7zvtfbAGLhcu1EIvp1WgTvTVzRKYads3v71Y6aOjfUAvT-HFtJFH_Y6cpRBiGYx2ab_6_lwakPI3b5CXT9R32CbZmbn5QBR5DSQl1fYaxDGrcajE-udGrmH0N2bLQ3kSvtSdYweDEvxCw62fG1QzxjFWWe9jWtTqWv2WoVOuaPm1H7arKcVU3dYB7t9Ui7tMfvNsdDBHHzObzzUgnDE99j9tMHl1i6q5RXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
راهنمای کامل استفاده از ربات WhiteDnsChain
(کانفیگ هسته x-ray )
نکته : این ربات یک کانفیگ اضطراری برای شما ایجاد میکند تا در موارد خیلی خاص از ان استفاده کنید . کانفیگ های این ربات برای امکان exit chain در اپ های white ایجاد شده و هر گونه سواستفاده از آن مجاز نیست
🤖
آدرس ربات:
@WhiteDnsChainbot
برای دریافت و مدیریت اتصال اختصاصی خود مراحل زیر را انجام دهید:
1️⃣
شروع و انتخاب زبان
- وارد ربات شوید.
- دستور /start را ارسال کنید.
- گزینه «
🇮🇷
فارسی» را انتخاب کنید.
- برای تغییر زبان در آینده از گزینه «
🌐
تغییر زبان» استفاده کنید.
2️⃣
درخواست کانفیگ
- روی «
🔐
دریافت کانفیگ» بزنید یا دستور /config را ارسال کنید.
- درخواست شما برای مدیر فرستاده می‌شود.
- پس از تأیید، یک پیام اطلاع‌رسانی دریافت می‌کنید.
- دوباره /config را بزنید تا لینک اشتراک و QR اختصاصی شما نمایش داده شود.
3️⃣
اضافه‌کردن کانفیگ به برنامه
- یک برنامه سازگار با V2Ray/Xray روی دستگاه خود نصب کنید.
- لینک اشتراک را کپی کنید.
- در برنامه گزینه افزودن Subscription یا «افزودن اشتراک» را انتخاب کنید.
- لینک را وارد کرده و اشتراک را به‌روزرسانی کنید.
- یکی از سرورها را انتخاب کرده و اتصال را فعال کنید.
4️⃣
مشاهده وضعیت حساب
از گزینه «
👤
حساب من» یا دستور /account استفاده کنید تا موارد زیر را ببینید:
- وضعیت فعال یا غیرفعال
- تاریخ انقضا
- حجم مصرف‌شده
- حجم کل
- محدودیت تعداد دستگاه یا IP
5️⃣
دریافت دوباره کانفیگ
اگر پیام کانفیگ را پاک کردید، نگران نباشید. با /config همان کانفیگ اختصاصی دوباره نمایش داده می‌شود و کانفیگ جدیدی ساخته نخواهد شد.
6️⃣
پشتیبانی
- روی «
💬
پشتیبانی» بزنید یا /support را ارسال کنید.
- مشکل خود را در یک پیام کامل توضیح دهید.
- پیام مستقیماً برای مدیر ارسال می‌شود.
- پاسخ مدیر را داخل همین ربات دریافت خواهید کرد.
7️⃣
دستورات کاربردی
- /start — شروع و انتخاب زبان
- /config — دریافت کانفیگ
- /account — مشاهده وضعیت حساب
- /menu — نمایش منوی اصلی
- /support — ارتباط با پشتیبانی
- /help — نمایش راهنما
⚠️
نکات مهم
⚠️
-درخواست ها توسط ادمین دونه دونه بررسی و تایید میشود پس لطفا صبور باشید
- ادمین کاملا مختار است که به هر دلیل ممکن از ارایه کانفیگ به شما خودداری کند پس لطفا اعتراض نکنید
⚠️
-در حال حاظر کانفیگ ها با محدودیت 1 روزه و یک گیگ هست
- لینک و QR کاملاً اختصاصی است؛ آن را برای دیگران ارسال نکنید.
- هر حساب تلگرام فقط یک کانفیگ فعال دریافت می‌کند.
- ارسال چندباره /config کانفیگ تکراری ایجاد نمی‌کند.
- برای امنیت بیشتر، پس از دریافت کانفیگ می‌توانید پیام آن را با گزینه «
🗑
مخفی کردن» حذف کنید.
- در صورت پایان حجم یا اعتبار، از طریق پشتیبانی با مدیر ارتباط بگیرید.
@whitedns</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1600" target="_blank">📅 17:14 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
