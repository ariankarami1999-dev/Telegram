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
<img src="https://cdn1.telesco.pe/file/UXHvCyYVEqK9w1B_QInm_AHQqv0RboWYqord_kjszSu_RjiweDqCOK5ZbeErM_KxRxPOkx-2EFbsruk8wFFcxo9a6PRlzsrM9mJzlDBlaSKH7shBxvDqNhUcnl_905b8DkDPYt1iIc6uSWD1pC5nW2Y-ASjE9LkhtfY8YnI6UTtzkItA911IuH5_ojD_ncX5zD_ISEawl3_x0EdX0zqFN6GZWyMFMJ0Ck1f662dQlULjEtiARfK1S1lZQeG5eyqBsrho9dZdBDiIs_PqckHfhGd3MFHZKzNaR7S0DoMVT0iuS7jhiSFIrHGOmsIVerqQNHEpL2-RoAGFAR4uQxxsgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 154K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)ارتباط با من:https://linktr.ee/matinsenpai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-5474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)  1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا https://github.com/patterniha/PattNG/releases) یا نرم‌افزار PattN(برای ویندوز از اینجا https://github.com/patterniha/PattN/releases)…</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/MatinSenPaii/5474" target="_blank">📅 10:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">چطور فاصله‌ی بین Hermes و دستیارهای اختصاصی Dots و Grok رو پر کنیم؟
یکی از کاربرا توی یه راهنمای کاربردی از اکوسیستم هرمس توی ردیت، بررسی کرده که چطور می‌شه بدون نیاز به پلتفرم‌های بسته(مثل grok bot و dots و muse و...)، قابلیت‌های پیشرفته Dots و بات‌های گروک رو توی ستاپ Hermes پیاده کرد. راهکارهاش شامل لایه‌ی مسئولیت‌های موندگار (persistent responsibilities)، سیستم دیده‌بان پرواکتیو (Scout) برای وب و دیتا، مدیریت وضعیت تسک‌ها با SQLite، و تعیین سیاست‌های دسترسی قبل از اجرای ابزارهاست.
که البته خیلی از ۱۱-۱۲ تا قابلیتی که گفته همین الانش هم هست، صرفا دسترسی باید راحتتر بشه توی UX خود هرمس و به نظرم کم کم به اون سمت هم میره
👍
پستش رو توی ردیت بخونید، بد نیست:
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/MatinSenPaii/5473" target="_blank">📅 09:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5472">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مهار دزدی و Distillation Attack مدل‌ها توسط OpenAI
شرکت OpenAI اعلام کرد یه کمپین گسترده و سازمان‌یافته برای استخراج و تقطیر (یا همون Distillation خودمون) قابلیت‌های استدلالی مدل‌های پیشرفته خودش رو متوقف کرده. گویا مهاجم‌ها با کوئری‌های پیچیده در صدد کپی‌برداری غیرمجاز از متدولوژی استدلال منطقی مدل‌ها بودن. اوپن‌ای‌آی دفاعیات و سپرهای نظارتی جدیدی رو برای شناسایی و خنثی‌سازی تریک‌های Adversarial Distillation مستقر کرده.
(ببخشید برادران چینی. راههای جدیدی پیدا کنید
😭
)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/MatinSenPaii/5472" target="_blank">📅 01:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5471">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5471" target="_blank">📅 23:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5470">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آرنا توی این ویدئو، قدرت Gemini-4 Argon رو بیشتر توی زمینه‌ی 3D و قدرت پیاده‌سازی گیم‌ها و محیط‌های مختلف بررسی کرده
که خب کامل نیست و باید توی تسک‌های ایجنتیک و کدنویسی و بکند و... ببینیم
انگار که کلا قدرتش کمی پایینتر از GPT 6 sol هست که خب، ازم بپذیرید که قابل قبول نیست برای گوگل، اونم بعد از اینهمه غیبت کبری
توی دیزاینایی که نشون میده، قدرت Sonnet 5.5 هم می‌بینید
😂
خداست این مدل
https://www.youtube.com/watch?v=h5EL5zThKaI</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/MatinSenPaii/5470" target="_blank">📅 23:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U2R4AK6EvmdMKnETOyyj90J1-6edk0OUqneYyxWue_KeAV-ZuW5fCaJoRTSPAsuC7qW3ehHnd2sUg0gsPEUnfkOmvxuLztWgKwPeQaExiqUsn75WtWKpj7FsGfghk2Wpq-86Ps1knyEBv8qVUMSoDVoFd_LTxZj0TRifYwcXLXOj9PfTOezIwamYHPJQotNAtV2iQlsEifW-SmEkvyIEpeLezc2ZK3oe4lJKsnM6GBw9FKXOTFwOzwaflDvXO8PtYgFIVoQmsiNkxa0d-4l8eTtGll1RyKNUzyoWkaD9ot1VhRwTxry85GudPsq85KgNzppbce1-sKXnTjXBgoEx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش دور زدن فیلترینگ کانفیگ‌های کلودفلر با PattN و PattNG (نسخه آپدیت شده)
1- ابتدا اپلیکیشن PattNG(برای اندروید از اینجا
https://github.com/patterniha/PattNG/releases
)
یا نرم‌افزار PattN(برای ویندوز از اینجا
https://github.com/patterniha/PattN/releases
)
دانلود کنید.
2- کانفیگ V2ray خودتون که با Worker کلودفلر ساختید(آموزش ساخت کانفیگ رایگانش اینجاست:
https://youtu.be/iAbYpjXyLpY
) رو وارد اپلیکیشن(PattNG یا PattN) کنید
3- توی اپلیکیشن اندروید، روی مداد سمت راست کانفیگ و توی اپلیکیشن ویندوز، دوبار روی کانفیگِ وارد شده کلیک کنید تا پنجره‌ی تغییر تنظیماتش باز بشه
4- توی بخش Finalmask raw json، این مقدار رو وارد کنید:
{"tcp": [{"type": "fragment", "settings": {"packets": "tlshello", "lengths": ["0", "104", "1"], "delays": ["0"], "maxSplit": "0"}},{"type": "fragment", "settings": {"packets": "1-1", "lengths": ["114", "1"], "delays": ["1"], "maxSplit": "11"}}]}
5- توی بخش Fingerprint، مقدار رو روی
Unsafe
تنظیم کنید.
6- مقدار Alpn رو روی http/1.1 تنظیم کنید
7- توی بخش Cipher Suits، این مقدار رو کپی پیست کنید:
TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
8- کانفیگ رو ذخیره کنید و پینگ بگیرید. دقت کنید تمام موارد رو انجام بدید. آیپی تمیز
188.114.97.6
عموما کار می‌کنه. اگر کار نکرد، از اسکنر
https://github.com/MatinSenPai/SenPaiScanner/releases
که هم نسخه اندروید داره هم ویندوز و مک و لینوکس، استفاده کنید و آیپی تمیز پیدا کنید.
مقادیر ممکنه عوض بشن، مقادیر جدید رو می‌ذارم خدمتتون.
موفق باشید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq0u41-1mU4zAHqHeeVM57UF2YCSqvD5wtG3biiRdqp--xjATKv_XGxFU0V0-alSADGHHcYfkRdTUz7C3NHI2tQBan1GkkkvVzju8XbSq3e8B6OojUVTzrF5lh_jz9ZfMVr3NX8M7Wk5SFvwSLrzUhRBELnomWwiQc9Qvk15oiFz_aWD3TsoW_JGx6RBeOrRcR_xeZp75npmCBrt0t9tf56DVWFV7tPuFRGVn0thEBrzCSUwQH9XmO6PE5MTDEjfp7Wm2bOFB-P96gwHRUntCoBkoUMDRWFzV3CpIiEcNpxexheMr_EsPQsVvzddcsBwkDsJok2C2Ap-eyjejA6puQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل Airbnb: ایجنت‌های هوش مصنوعی به سیستم‌عامل اختصاصی نیاز دارن
برایان چسکی، مدیرعامل Airbnb، توی گفتگوی جدیدش تأکید کرده که
پارادایم اپلیکیشن‌های فعلی پاسخگوی نیاز ایجنت‌های خودمختار نیست و دنیای هوش مصنوعی نیازمند سیستم‌عاملی مستقل و AI-Native هست تا هماهنگی بین ایجنت‌ها و خدمات به شکلی پایدار صورت بگیره.
خب مشتی یه کاری بکن. ما هم میدونیم
😂
طرح نیاز که خیلی وقته شده
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tFDlzDtYWvDtTPhLVTtuIkAAz66_u7QDZYBSkYsLhhYzsqNk0-fzzLV_IHlnRzMF3jsMr3qjQXljvrbgPMxBh7RE_akynaEIY4RCpKn3cKmzT9B1GW2C0A8kbq06AMBAUWqOUURPX3Jn8I17qoXfIzXxGkk5rBoYcWHq7GGNBL3uf82u0a7_TC3fUgUkX5EpiovDkRaUMhQkV-Q-db6skuAx3usCKV4B0X-bJ-ITTVxoN2CcDvKVx8arPO0FPfuXc0Vm4RH19FKeYtH1n3k3BXxmHu9QAao4kRVWchCcHeAdr5j_Nz9bTWsxzfaF-Vs_s0sN7yrqHUdmhCvFGeJjiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ektvRyoDwmQq38R-RAYS4gZ7vpp2KxenNfjIFcW-eYbZjMjKkowct2TJYdmswC_rMNqa_97OcH2yyjZRyOBbG89i1o6ALVsAYCLGreKL4zH-Z9Y2_UKJGz-na9swCkc61cccwAPFR81ASWr-lKcCj2_uOnxJ06gyT-ydQf4_UCkH26OLOS6hR2j7Qsde1dRNlLCALjN9QfXJtxmL1GoDDvHavYNiURPkovi-l-gi0MfYBapEjIKGxLIJyUh3mQ3tcMjDiUdtDdoVHWg1HmznD1oKFUSL7wUCpRmeuUu1bfM8CitOqSn0yY0fWZMhhOIPjHAHq42WGRk1bUQBN9brbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IlL1mIbZxoDbp7jrCFzAyY662tzLzUkFAEv4NstSss61So80bY4PEC4XLvkpcT3GkQMTMMF19tS-37f9s7EbbXl45IerVElu-8XBeHxZ_kHgkEikUkCNs-3npELkJwJpB0DidBXQVorTfSMdcpCYg1J8rYGgYt1ry5VhGhQVaFsBt1HOpTa3LFiWsJFqAyNKMVLevCKRnETZ417B-mEpYXC_sM5wy22ZrN48EK9SczNb3AuDo211_wSuwx0O59wjLNBKaQzIXTQbvbs60sZS2-5iIziKqXOXumyCZelc51qQiB6_FhRIRrPIIBNeNyhWEeAYN-OxCIUvTdN4PY_1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slH0EinZ3VyQf9kbGdBG3i8Uf3VItr7Bs-ic4ZMFfC_6JYTQXltCWGSuuTZR_NNusnD1F6Swgkp6YGGGUnkLCYnBtWuY8xT3kLZTgQdFa6EwIhSyZ1ooKlVfSsNDrt0Njy8m4ptJKxohnULDX8oCBTPUuVkE_DnRuAwFc7UrHg3_wfLVCNPVKJ2TCcbnA-B18JsBFIHUod69K0_psn76Uu3XSt7zmnstgi0uB4QHb2r1WDfzvVF-Euqty2A9hkluSzKMOnxANEOGJIhvMYurDxAXWEJe9e7I8XC-GQM983XGyHicPPSzHfI-hS4O42pLBBmyRmN-pN7kc2DqUuadYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpyRVqtOrCixdrqsDfDEGQj5ujFkhsA7BVB0P_fDGk9XrmXSDuPReGqfXEf9AsF7QtE4zgYW_ZwjpM0sMhIe8yKAxMnFDJd66tGIjXZsvsLa28wlDm1ETdxVrBwkyP93mEVsYFVIA4TlmD0wrkh_eswcAia3jkUhYA_ugfpv6Xza8CPlrnqLwRBSw5NgkO-4cSrIx1N3sPuqT3eGbjwObl56gFWREYTCV0Ie-cb3GgOJTKT4kTgGzqcnGomcDqLZp7ad8RhtRJtH7c8KKLI441Nyp8ZU2btAyzA2JhrhtqM_wAXmAeK43OMd8DwOOdBJvsS46sOF5Q_tBLF8_ikQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k-0PAwTpofDbGE656yhnYq1PE57tTlM27xqre2PKGBiFottezdR8ddj9PRChKj6LOVDme5muliDYAbJM3cdeRhi-OJjZPTX4i0_I25Mdf36PHhl6kuoJ7gjeNtZPwzttyAH18QF57qCgkvzb8cNbEQDdnnaxzaTkkAGZUL68U81LSqdc8rN8lAiyihrPGNI5oE9hLM0kMHAejpFiAwVIBVuvrEUn7vCa03UFz2JpbC7G_TqDTEOU1raQkMU7v2ZSeTrNor_enGHU5UlItF-AJh-j1ADCGQEpyHRJjShppdPBSDO1U8mIp3ek7lyqPXG6AoqE2runV0RS7O9CIMMMaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nZtNghpgQiH42VyhFNIrw_YEwZ52VkidU8rEptsFT89qKrbcaG3N10G8FQQqfnt8Bm5tsGiRsNJ1RwKC-weLmcPfHHmf8FkO-5fV1XYAXyAy-ONL0tDxmdqKv9ds8sLyIPouXcrhGUe_qjYiUnPDRwp8x4bGqwQmpgAu0apBd1Qb1v2MC-cbwWXtBEyKpmEhTp058LeICHKfi0VKmh5MOZfaiU-aMX_gRhFBwOf0J5rjjOVABlAT2pEEMmpzodBNKBarKRPobZR_ro_D0vf54txgKS6KGDPy9t4QxQcWL_r-4RrYYjI8khxqCM3_SPKzHdNfXV4Dx9dClzYPP6bumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rQVGxr2y0jSAOlwHSeu-MbhwzZJtSvR6Y95kqtPbdu-LHhYHDvtvNSzf9v8oO_fReEwr0sk9yjlJm0YKbp9zYkkaHdB54ylaw-eHDaokXNYXT9rwhvc5cRSOyfHWeEeP9k-7aNMaN7dOY5YcHKdSdvSyrJR94tgttc74DD1XZlO7JTpNK9I0YyWyVE_xUzTm5eadSHT-0fDfT1WDAzvaA6cjH6DhLVD3JQ5lRmipU9acnQ83bumiwhvd2fQq4_gL1h5qD4fXtliCZo8VpzdV6N5cTXX9a5ovt2sLoYx37o5ESvJa_ObZozFWu7Jzr7wOcGCuxP4tx9DU7MGIBZj-VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/THy5ADHb1_ZcbUi_2PZbHOabq0RhU4DeHtja9lwrXlHEbdpZ5sCbssl0EkXXqWQwGCiUijz0p3ycaWDUUbu5wGsrvpLvDkz9H7Gh0ouLDDcDGG6fD9VSrdLd5F9ZQ5_FIYSngswbZRb9ppX0kaT7P1cGOJ5peFhwS7VQ3Y09vNeV7Z9b43vC9cQz-VTCFTHpK4B2UlygxQK4CqjwnWawqasQzVRjY6aJ6zd39ZXbK1eXuH0FTrdYuoVWK-wbWrbAr9h-ZXE9ysTsD6KRENix72I5Xu9M8ThINLqLjSwMwsZ7W7kYZNr8UTBJkIbQJj0OofyjmbgdHE8Ent9L-pLMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Q7BpARCsn-iN68M7QINKxjBnzjQWq4msg-GYAEX9lrKDfiKsDy77tJH2RWdTpBnW7WBjcJdyYHjvQGHBKCp0Lmi2yIXSHSK9ahSCB8Jr2HuN4Hwe-g1zGRiWuYZtG9nPrAVFSmlhvp7QOxgT4vOJ0P9Hu4pIDoB0I3fVpEm5o7N3_445PIaP1wEBbw8KDEFTuRrY1ruFm60TVyySONI1MwiKwXgOhVFhdMef59E62VvVTmUmSLAj543Sj_zkioOZGuMYaSaplDoEIXNYeZIDQID-RYdOG5pphGlM9DdzYGI6GHyaAzN7zvGUdU7RVfoAk-gFbvaObD0kgqAYJxFS2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/u1Q9qJ1AQtKoSCrPahnkOca4EsFu9_6Y7QwOhMe4Z4-h8B9WHxM8xY0ammotSbLKD3h3AbR3skQIMiFEg1kKyLdTxcegr4Eo1sRfn_wM0uFdlBn6uo1e0WAn_w8e8fU_ZkB3kNb-ebo_bw0zWRJC8AYcqRXeL1Q19GNJkGG-dm69mekBCbG6NOOgTd7aIlkjrVeIhQeNyLYem4szrPtUJKI_dhhfqBWfMNxRplZT48lr8x7Ss_kKVwhW9oAt4FsuB4kOzYXrWVAQluzaASwDENUKXXCI-sI1BDHY6CXTgV2fmfc_gnMO_u8VWOyoy4ohrZJM-VZFoL6eR9oMorRLww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=c-J1MgHGA5zuA1Y1fqTXRbOv9EFzJpgHMxiGREy-F2Mervbk5_8M06AgIj6mEvZWKT40BpVW3CcLc9n8q3OyC2XSyemI_GoAlKc9E2R9F-TgyKaM2OIpmB09QGyaoGjwWvlEIpMPtpC-1o7V7lsWH12ipH94x1FAhLINgno5py-7vSRb_y6N6W4GvdcrM1Hzz0-yFuKEGwF368_S2pl_YlydhnrCWQQZf5XgbD8O0hyNNZPTLgy-8TCHTF39Oudcz62Pz59Un5Z45wiMBpKWgMekViFYC_8-X30Lrc_qHnVPu3mWe-FhGsfEJft_LjHZRWoYGBArp7vAEBMXJ9G-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=c-J1MgHGA5zuA1Y1fqTXRbOv9EFzJpgHMxiGREy-F2Mervbk5_8M06AgIj6mEvZWKT40BpVW3CcLc9n8q3OyC2XSyemI_GoAlKc9E2R9F-TgyKaM2OIpmB09QGyaoGjwWvlEIpMPtpC-1o7V7lsWH12ipH94x1FAhLINgno5py-7vSRb_y6N6W4GvdcrM1Hzz0-yFuKEGwF368_S2pl_YlydhnrCWQQZf5XgbD8O0hyNNZPTLgy-8TCHTF39Oudcz62Pz59Un5Z45wiMBpKWgMekViFYC_8-X30Lrc_qHnVPu3mWe-FhGsfEJft_LjHZRWoYGBArp7vAEBMXJ9G-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAz9cdAxCXVxlYO73d6cAtWVrSS4BJLGMuFmXe0FXoim-8eC1ydQRWMBylYkFYxkvE2_2aMgyzbvXvYcuJri3k2xsn81OLQLum5rwRH3-K1CguolDNNxTBd30qLhlYmpp_0zjCuJ70OxeaX03elAMoLgGKE-FGPoAa0qwVF_3tagcGJX_YtXARW1lMTMPqNdX_4FxciY6VLHThG1X96puUyDnYMZAV_ds2RZtBH41hcy-jFa3H0emCOCDR5EvFQIRc74-CEiuDp50kGB70pd5nzHo4TMcNQ7D31w1pgmVxZDxFYon7K0ns3K9H1HSjvnE22-8Dbh6I3M1Hl4utgANg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری
گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای اکثر مدلا) تولید می‌کنه و توی بنچمارک‌های مهندسی نرم‌افزار (امتیاز ۷۷.۹٪ در DeepSWE v1.1) و امنیت سایبری پیشتاز شده که به زودی می‌ذارمش. آرگون با هدف کارهای سنگین کدنویسی، تحلیل دیتابیس‌های حجیم و کشف خودکار آسیب‌پذیری‌های امنیتی طراحی شده.
هزینه‌اش برای دوره معرفی، قیمت خیره‌کننده‌ی
2$/10$
و بعد از اون،
4$/20$
اعلام شده. با 0.1$(بعدش 0.2$) برای هر یک میلیون Cache ورودی
دقیقا هم‌قیمت با Opus 5.5
باید فردا ببرمش زیر تست ببینم گوگل واقعا پرقدرت برگشت یا هایپ الکیه:)
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SeFq8c3ZtqQIXcI6xA6-0Vr2x6NqSHkrUbfT6sMMlTm9HJZbdtH3FQVCVjzigTAm8zKi0vVjf6O9WAZHjh513rTE1OnlKO5cuE66ZrnJUNo_GZOzbYoNqrp_ilu08NoYDcvOnWSmynEEnLHmyCzIPw_laNmlM4z_w0YYxyJ12qpDNGLWKSuZLdrtS4huEJWj2doWey_0-47JYYYMR1Z-hjaEM1Xb33MYGYD2vazk_xx04HeUMphNmV7B83gkBa_HtgD7Wr6Q4jQc4bNk3CCZx3jE3mYSgzy-NXmJLDcQTdF5cLVwte5U1nocWwW4GAy7rm798A3jBB969Xj9TzMyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ld5T6BoqroThFIEuibERMm1cJnarQpUhFDe_0FELV_5BSYgiDjqFsJwIvraeoc62m-O8fx0lbOJbtXj2uyL3h34jmjyJsJ5z2oI3isc1Q2Cz41AOLRtUcTjYG7e2kB0VRqAICtuhpQjkvRp2GN-6OFQx41sXq4R2MUN8RVxcMrAFRl5pRksj65jIyB7ELMhpOIn8xpm42ZgJm0jT2cqP2qpqivJHjh5XFXyZPoSwvO-9sg4Ll9XMcbCurfaxa-9s1ade96zBhXqQf2IDPCmbH1aI5bGj0_ruPMCYzBup-a9qi5kKVqzWsh2vmA4R7GHMZvUm2o7Pgf2H2cNncC1rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPedi | پِدی</strong></div>
<div class="tg-poll">
<h4>📊 کدوم ایده رو با هم بسازیم؟</h4>
<ul>
<li>✓ تمرین انگلیسی با Shadowing</li>
<li>✓ زمین بازی سیستم‌دیزاین</li>
<li>✓ تبدیل کانال تلگرام به وب‌سایت</li>
<li>✓ ایده‌ی خودت رو بگو💡</li>
</ul>
</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s4YtyFVdpHKGq1p3lNR09XoWyd7n9F1oDEQbv6sBmLIKqHvpNyuyyJkw4lYQkvLs4O3SCr6AQ2rb5Nwi8KWaYhMu-AnN9x-fRV6CzE9dCtnoI8KEFiqtLl03_900eAifDwsMTYPcin5cIor6pDxRxcN9XC7_IOkSs5fz8R3gZq2dGkr9MOvM7lYLYImBJ5-HYJSIBioVN8-AkTQsJylfwkyrnjsU1V44qGMj5Zlg5hkk4bQkH33RT-PgZGtyHnlusIq2OwwzvBztbBb7tL2_Kt5mZlTFxlVIDkkBlYz4D8f-HpdkMIsJAbveVKzqWmGkY2qwSYikWyhm_lHMYkqgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qqYC6NDIYYwZwF5GUcvTbelcoLUlqa70U84yHD-2sPshMljsWBOlxV37E3-oahqVr1zK05umA6lgDbalaiiiR3Qnp9BoPKfcJpJvD9xXwAT5aVSnPPi2oXyE0deo_QORYqM9b_sbhf-N83xc07L4xicYSnpboS6AYGt2xbRdUOgxlWiV85pOQ2uk_8B2XNMsx2bzrjJthqZUhhmlLr6bHF2ycHKvHIrJzpNLNwwXJBGMOsLc_Z-Wo3hWNCCjh9YF5MPMHyy92r1skK3lMB4WniUjZLM3_GbyMnUhCLSwypWVN-cgIUP8oI45V_R-jFVQpzkAzcfF7hdcdL1LdkWSqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pEK8IuSoH7VrhY3lGYHPZgzCEy6XR-GVblyDejn0gWm0MGLLk4zD5WxCQr0pSihF_yCC_jMK-eEMIiHBhfSKp6C9qqeQ7b4LD7mUCUUZkId1mBZj7BwFnirrORDT88pz9klA3Gx-EdbQ7WwArZeqZXYry2kVC0ZRJPg44e_saLaj7aT2eDTgLYyM4C2CmIwUQECR7mh3BITAIPIM-9Eb8zpTspcbWA29m3hJIhY6T9ILtcwmGiC4wr1fHkoTOnhmXU-I4vSBLw-pzDTt8jnPWtHzAA-Jn7sn5ZN64O4tkMtThr9xFx4Fh-tBngdrWksQ8GhmsFjwZX-SbgMma_56jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/io59bvSy7V-oEjF3dw94Ee600BlRkQLAKwL0tiQ8NyvPx6nuJQrQFQKB7jdDO70tpp4vP9G39r1vSeeTOsVhujsdlNBndJLTbaX6VSwsMyI1VyejbWj8SFt-wUy5ZffqZPEM_1FBs74UQiV_RVBUTl9F9JpY9qLc6u__CF-hV1b2gsts-2GpoqCc9OulOCXAX5uPTdZEeBUd3wTTIWq3SSXkth249POQligSo1U3chQnF51lQgAYpyACcbeKO8iUE9PNW0XxSJPDWemcCTFTbhzlpTvJhPUq2egDLkoVE6SKZ275NNJUsfNMSs_o4e2TRdAp_ApY9vKlsVz3MkquHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=Y6OYi8mkKwZTMCZu_x8iYf4sZ67pW9r6BRkHTajcj0cEPsMhpVGwmmQb7-Lr7dYgPnuvwf69yzURckm7y-25YYNZSCWjwFrNwqCW4P-FDNgx4yglWzBIO0DZBmhia6cjtAFhttsfRdUmHCRnCgtxBRENhzWd4pzfSbx6NKsHzypo8hsHfFpSKFwzbKAM4azlqFQbnN8B64X3QpOURiK4M4fTcmXII6x8plot18t4ZrcxlClkfRh9CC6bAZ_hpCsGAszfiW2gcG2AScwaZgwlZA4RXYL74VMi3jEiHVDlbyr5oXT2GW7yF0n-cEGQV3RziSJcC1bz_dbfrJJtHVr1jA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=Y6OYi8mkKwZTMCZu_x8iYf4sZ67pW9r6BRkHTajcj0cEPsMhpVGwmmQb7-Lr7dYgPnuvwf69yzURckm7y-25YYNZSCWjwFrNwqCW4P-FDNgx4yglWzBIO0DZBmhia6cjtAFhttsfRdUmHCRnCgtxBRENhzWd4pzfSbx6NKsHzypo8hsHfFpSKFwzbKAM4azlqFQbnN8B64X3QpOURiK4M4fTcmXII6x8plot18t4ZrcxlClkfRh9CC6bAZ_hpCsGAszfiW2gcG2AScwaZgwlZA4RXYL74VMi3jEiHVDlbyr5oXT2GW7yF0n-cEGQV3RziSJcC1bz_dbfrJJtHVr1jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nn7QvipOViGoMrQM2fOiL4ZkV9TQwhO1UKlQWJUsdNGc0wCMgPGr0c316-hg0538ZuUOBysF0t7ZBmmq8dZhi1Ahb9uTwiGLH7iDjfSKHu9frJcG4rNx17wbp9pVSRoP_laDW5FAe2Zk0ESJUaQRa94HciqwnFT0mJCUkk9hiUekF5o25Bv4NktA74CZBXKqhd4YorkEzPG0e_c7MWiN7GY3SntmohZGK9V0TsHlRN-uq1HIMcwqC26nBj8-OAdweMPM1iTdkCFAxg8A3E2BxtJmFAausygQj9bDEmngJFHOj6vY9JqsrbTlc7A3WS2hNytRnYX75NYvCOf17et4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خندیدم
توییتر OpenAI کلی گفته بود که امروز به مناسبت Dev Day قراره یه چیز خیلیییی خفن بیاد.
کلی توییت زده بودن
هایپ کرده بودن
حالا حدس بزنین چی دادن؟
GPT 6.1 Sol
😂
😂
😂</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IUHXOwrUlVQPcdDi9xfWLFC6AGEYNVZagOAk7TNXB0dmJ79AniZ-y9kqeGui9RgEZkuwLC-UH7-aCXN3tyDp3Au8KzLfGpfEr8_Tua8cHrhrY243SI8IKmd2UxlnLXpNu0lNza5-KHp8LKVoyu9YJd--0J1r7BVYB81omYUQgNTt5wtpKjbLHDOWkme2TA91uv1u14_DIsZskeHtrW9Hi7AAIDTJX3sGP9yQtg3TNc-Pit9xKrzUebEyWd3Df_bUq5DLrrxcN8uhbTWTcgtmZOquN08gJfbEUHTQftM_x1TaVT2Jh07VxANeEHCJ1QKGmmjFPXeUSceLOrK6CS2Uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vqrmE8AtgFJl8xfRfYCgYQZhw5rQpr-sGHABL5zP-QOoZnP18OzFa250rwxqMaVOsQwKdiC2gcCdEI6nY7AWp9W89XiQrVEWKeTKocRZK7zvWcIGBvgl7H4J8bRZnrvuq6oI3rnl_4yQkhDJaaDAnNlv1jksc_WYkvCxqIt8wH51nbJ4mAJXjbkyXejg_8sdQfxxurOLuVCLVfvzjqq-vRXHjuoDrM4Yrw7skehFyNTriYGQiBI-Rq4wTdel84bnkXVJvl-WbWyfZAywrqAgqarTgMRKuSrB3aIXaCZQzjzrXwleYMVyvp5iEA5RaJFeo0tmIpQyPWFr5OhKVoZkiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IdRScJND86xt5VPCEWh5XOHFFIql-x9jJRVYF6C1D9XMCdcExVPHkUfz4OsOpGD_lTYOmm-mLC-u7wRAinWvS3ffRIFoZwJPFxHc-Lm9oJ04552mJjpVMw1_stTVWeiz9dTdOpz4fpMfuXVYZVVtEM85gh0_D8pu150Ga-6VMuEy3K9rThU43ddvPduD9HCw1XWX_IYGhRZwyrJpQQMCWly6l-qSj6qtZS7ji5xVOfNvhY9KUU23YCn0jRnamu_riONti5XbN-mXhhabdsjp59EOfq3rNPw8XrCwThFst2cnmShEKjzPsL_d12WFU5xgkyfrYl1W6e3mLKVA_-Is7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیار جدید ماریسا مایر فقط از روی عکس‌های گوشیت می‌فهمه کی هستی
ماریسا مایر، مدیرعامل سابق یاهو، بعد از راند ۸ میلیون دلاریِ seed بالاخره Dazzle رو معرفی کرد:
یه دستیار AI که برخلاف Muse و Instinct، نه خبرنامه‌ات رو می‌خونه نه تقویمت رو؛ کل context از Camera Roll می‌آد. از روی عکس‌ها می‌فهمه چی دوست داری، آخرین سفرت کجا بوده و بچه‌هات به چی علاقه‌مندن.
مثلاً از عکس‌های خود مایر فهمیده خانواده‌اش escape room دوست دارن و چند جایی که نمی‌شناخته پیشنهاد داده
😂
😂
کمی ترسناکه حقیقتا
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=A6d4Sk20T41O-C1QLAV5Twm8txaVk-ZPYO5n17urdJTZr0pcNEpbcmz9fUpuxtzNmgpVWp4L_F2CQd_l6PMjSdqG8pGVt1MuApi_EUuX4CtsHR9wF37ywQbew4-VbpY0loQTqI2PyXqS9JbM7cM5Kw_2GnHNDXusbLf1n9Kovgilx3LUVJAfs_UXL0qKWeNhEo1DI3oBcnf5nDDn2U-hIm-oqFryTKstGA6-2omLPF0--rghOOON3tQ_KWPkuJqmaSHrJgHTjDAqFMdXOhI-jm5ihy1s3EfUwpSlaYtmU53D22h6hacSnsURfNmrjGzWQvdhmMQmtTBIMG27tWSWsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b452f6f520.mp4?token=A6d4Sk20T41O-C1QLAV5Twm8txaVk-ZPYO5n17urdJTZr0pcNEpbcmz9fUpuxtzNmgpVWp4L_F2CQd_l6PMjSdqG8pGVt1MuApi_EUuX4CtsHR9wF37ywQbew4-VbpY0loQTqI2PyXqS9JbM7cM5Kw_2GnHNDXusbLf1n9Kovgilx3LUVJAfs_UXL0qKWeNhEo1DI3oBcnf5nDDn2U-hIm-oqFryTKstGA6-2omLPF0--rghOOON3tQ_KWPkuJqmaSHrJgHTjDAqFMdXOhI-jm5ihy1s3EfUwpSlaYtmU53D22h6hacSnsURfNmrjGzWQvdhmMQmtTBIMG27tWSWsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«کلاد ساننت 5.5 این رو ساخت. فقط با کد»
این داداشمون
این ویدئو رو توییت کرده و اینطور گفته
ویدئو در مورد پرسشیه که آلن تورینگ، پدر علوم کامپیوتر مدرن و هوش مصنوعی چهار سال قبل از مرگش مطرح کرد:
- آیا ماشین‌ها می‌تونن «فکر» کنن؟
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=GBT758ts88oCTe-mR0eraj0qR2M--hYWE6wgWAEy-0usbCP1V2jXu_8q4meIESUKoSGsOD4lsR7n6P2rCWvSp7M4ercoE8TOb7AAWU8eE0KvQnSVj0C2Qxw8xefWgdpsV7wmlET-a7igjcMC05mV5g9kTaOogxAGT1jv2Uap0EPyX8QHxazOjBGuwO85f8e74RrkNhf9Blov0H-dFluyAkZExu2wSv9HZItNSMfthPpHuUop8q5mRvq6cqss9OHxHskJ-MArSJVK0bJel-4qYSqZpH7peboQkzHdt1B4EBpcZNRDIBOi_LYkpyZ0V51o4dyFxKMFyOowmLTw7Q7zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3a3bcc7a3f.mp4?token=GBT758ts88oCTe-mR0eraj0qR2M--hYWE6wgWAEy-0usbCP1V2jXu_8q4meIESUKoSGsOD4lsR7n6P2rCWvSp7M4ercoE8TOb7AAWU8eE0KvQnSVj0C2Qxw8xefWgdpsV7wmlET-a7igjcMC05mV5g9kTaOogxAGT1jv2Uap0EPyX8QHxazOjBGuwO85f8e74RrkNhf9Blov0H-dFluyAkZExu2wSv9HZItNSMfthPpHuUop8q5mRvq6cqss9OHxHskJ-MArSJVK0bJel-4qYSqZpH7peboQkzHdt1B4EBpcZNRDIBOi_LYkpyZ0V51o4dyFxKMFyOowmLTw7Q7zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل Claude sonnet ۵.۵ توی بنچمارک Terminal-Bench 4.0 نمره‌ی ۷۰.۶٪ گرفت.
بعد این پرامپت معروف بهش داده شد:
«یه کد به HTML بنویس که یه انیمیشن دوبعدی از یه پلیکان سوار دوچرخه رو با گرافیک SVG نمایش بده. نیازی به تست اضافی نیست.»
توی حالت xhigh: یه SVG سالم توی ۴۱ ثانیه، به قیمت ۰.۰۵۷ دلار.
اما توی حالت max: تمام ۱۲۸ هزار توکن خروجی کاملا خرجِ فکر کردن شد، ۱.۲۸ دلار سوخت، و SVG‌ای هم در نیومد.
گاهی سطح Effort/Reasoning بیشتر، فقط یعنی «شکست» با هزینه‌ی بیشتر.
پس الکی درجه‌ی Effort رو بالا نذارید. برای مدلهایی مثل sonnet، همون High-medium کافیه واقعا
🔗
‌
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fIkPOIIxeTWn9TuoP0Rc1h9gB3Vn8PY55-JMvUqyBl-Rxk0v2OWHgyjg721W3WOK7LiyILWfp91HSRKEnosSGVchu8IZDJhRuE0w29Lo5oKQ6U_zkPFNX3Rw5u9wLDS1yeT4pm7QLzdd_N6gMWR9pRxf_8fCbhL4_Tr2Z6mjpo5-MpsAD8Kf9tuGd2nGNem2nYNqhMZBTz2Ty8ANQ8o9LUFXqWBLcIQmAPYI0Hf1i8hsnRaqmhBwyoH8JUGDPFcHuqNe0q015250LWoPAyIZinVa3rwS1A6ABOThL-ug8oxy_fUPLpgpbKmIXNZ-CGCqNRa-wIYfZX8y_17u5tGMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LMRXLHrZsHNLkN2rLC2gV96PNV4uLZCWY48TgozlYxlvM2jZRI_6wx4a9x6T7TravogDpADrhicpOtZvjHfTJJzSmcI4FDM-TzfBAuMTGOdtByHZOg3U8RqxaaeY63FUCVbyTIdcBYVSJn5CLrQ9F6O2MGJimJD2mCUntajRHaVf2eAnZbRVqpaFB7t2XRmXU1Po09s_vYrWf2xhjm3Z3kQx-j6eJwSLDHaQq3QbrhyauZU_r9GHbiMS2ZWTK2adY4zoKh1pXg6_BKRNxdLui4gsaZnRnQPbdEwN3x5YshRA7LHQV9Deaqldidogc2OizFyPrKAissljSPM3zbWchg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/MSO5HfyJmDUCGOkWGHlV7wNOi7ev6Cj3uWbT66KbJrIjYnpkVR7KSQdPrOSKwhD0KrTYBYBhlVJgd9ev8p7vjBrFwallEUHdMA1nCAX9OkWHEuizTxV6lLKWKMYnZZ04N0yQ3i3YXWOL0NjLzA8rBP54mSg44a9-mMJ0eTlC-qVAFTecOjJHr7kXytuutTVCSN5MZ2REGXXsQJloxzj07O7Soj1x67M998lRx9EhFooDQgyBkk1Nzbjh5zO9tokCuf3SyvgylX76qVpO4r7NB3w8S3qEcm2F9XRtVkwVhZx6uPOol3MGUjaA8agsYTLE-DumRVIjen0UpqJ7vsRDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت جدید WhiteVPN منتشر شد (نسخه 1.6.10)
در این نسخه، مشکل نمایش وضعیت «متصل» در شرایطی که ترافیک در شبکه‌های دارای فیلترینگ شدید از تونل عبور نمی‌کرد، به‌طور کامل برطرف شده است.
تغییرات و بهبودهای این نسخه:
تأیید واقعی اتصال:
وضعیت اتصال تنها پس از تأیید نهایی دسترسی به اینترنت آزاد و پایدار ثبت می‌شود.
سوئیچ خودکار هوشمند:
در صورتی که سرور تنها پراکسی محلی ایجاد کند اما دسترسی واقعی به اینترنت نداشته باشد، برنامه بدون وقفه به سرور پایدار بعدی سوئیچ می‌کند.
بازیابی خودکار اتصال:
بررسی‌های ناموفق مداوم پس از اتصال، مستقیماً وارد چرخه بازیابی و اتصال مجدد خودکار می‌شوند.
ثبات سیستم امنیتی:
حفظ و پایداری رفتارهای قبلی در بازیابی آفلاین و مدیریت خطاهای گواهی (Certificate).
افزایش امنیت اشتراک:
الزام و اعتبارسنجی دقیق لینک‌های اشتراک خصوصی در بیلد‌های رسمی برنامه.
📥
هم‌اکنون می‌توانید نسخه 1.6.10 را دانلود یا به‌روزرسانی کنید.
https://github.com/WhiteDNS/WhiteVPN/releases/tag/v1.6.10
🆔
@Whitedns</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JKOJCQjyQLUgMRnuIA-20BeVBp_eXwYcmBlFaxN0XhbqVqg03YefwHKE1R5x7YmUVtPjBMd0vldm7VGbrWDWny8scQwlM9kb0FH32Tqn_zd7MQL6CHpNAe2391Xug44RC-KzAYwEXyJIiz7SF_079-0LMaBCQ4Fs4L9qQnRXRn8pyy87K42FdxXJVQJb0_z4awGcBpcT_Es7xIYdGFK27TT2RqhbusLcLMeojZF4nC4DEhT-pd8DRg6RR7EtRxht_qVsbJP18E25xCcBpgMY_okerBqEVcJadKei3rSoNzOJkN_99JqKCho9J_xHDNjVjdKturBeUYnIzn42CRDvwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L0dGgA2zakjxOwgNKDEuiJdGuL9GOPv3cLHW-Xqdm4nomSGj4wXM_uqMK0L_K8WO1wYdnXdeeWG73TqlcPCL8sNpKORb_lg2CJ0YlU5a4V-jboJR7B9rq_Xb1RFa3lBrGXT0112vcgmvu9qyMb3aBb7VRMGKzJLvDELKW9A-kzijAQf6UiQSKuK-pw0okY4k9xOB61-1UpUK4I4Ul4ZC9Bh5CkYH9ixPfXR2xWPZuoVtIrGAYpIiAOFgRJOT-r1oZ_gkbgv6-Y9q-LzxWfsqNe29AWvy45d7n_8hbyvqRmnwBm8QpUzFAU2udv9VtxeM1L7o_G3smmeigzUYq-xXvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DBU_aMRvNo74Nr7PgZpfLlQW2GMvB-H3MYhuyD1pOrIn8GAUCy0Tcun0_n3V0ZC40z2K5bR5McxG6OQX85Wn4TGDDeDnznXJJt9vrt7YZXNstyl3Sn9ehrx6jT_DWiVhgNk76etv5tl6gwBn_h9qBO91xRVNUoYb1PzQEx_fY6fOGRDHsFPTKlWwo8D-m7Mn3E5Ells1pCXz8V-z2wpfuKbn3GbPD9mVswvvhGQtrI3b7t1fQgFpyaxDS3baMxJNlUz96JLShpakUYiv7EugP0HOtR-noUWembl72WGE-8mTJNZUDJtE8l9nFQ50PDi54u5kGi8G-bLj0fChNITH8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gVTOq_jihHv4YKxh1wSWXvyI4fYZIVYfJ9-ByKBDP4xAC6Ug4cddV3CI4dtEdcEHiG2NNPeQIrK4SEx-TcAW907M3TrkWfCWNWRWQHxUtNFglQDDCZaSGR6reQWeVnZQFIVlaPFGgk_gRjPDslj49d2HjQqU13tXn49wixu5YoRGE-nh5GBbIU_iMOHpp-HK0RGI4KCrhzyLHPSRglcw-vqh3fA-EaqnNNh7rzWEOEX2bKxYkzhX7IhAn2Y0YX550LCLFpZm7Nw_i42IPl9PJWGRpBGnR-BcHh2TXW7RhTQXvqe4GCm2Wi5m6KJ7CFiE8hO3RSViRcWAmRONVaHQ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NQZ0onuloOxmNjOMz6fThhBFqh09wuIrcZ79iEckLRgNjSFIcGOJ89VvHoYUj78lNx-fv1VmgcKXEdKRJkfiItxQ3hFEjU5CIR53oqXIJdKaSEUTM3fKtfvrwTgxeMeP9j6WlpuTw7UpgAZ-VJx_Kc2P7ek4OoRYK2KpoRyg6iBbde-ezHeECymsgtKhGSuAYnViS_pagb2Wh1GqD09FmICz9FCtACui4BqbsozTiJ1AGzIyF9fiCeHsJHpJWp6AhGc7tblP37yuycSpKnCVW1kGx20Nz9_aXKcDNBqPKzi4QqjBC3z25My8w4kbUOL_NeJCqDzNsMjfsmmICHOQ-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=CVxWtvmN-ACKc-h-JCX4b0uDrgxFiB7fmKCwotRTnqMhTD1wljFuuuiYtcWJwa6CV5YR1mSBRTTdcH_EvYbHT3XChbOE7L5B7daBYfnM8olkYocN6xi_WBqpjbcAGxfxo4lN8a5BuFw34sepmg7nwobt9oqK2YOh3TAErTmOi8_nFzOBf6gPFiYVuKMHRq9vJLH7a7U5Etc8K2va2E1vwVKL8bFi31Lj4gqw5OsFIa_q4hlCjdbYkuMYsodPgoqljwCF7lUHBhy_nSkzxwsXYmdKA2dYlsOmt15NfpLU9ehQQXLRDN9bb-LqolC0D4uzDJM8ncomQXA3W3v9-yOHnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=CVxWtvmN-ACKc-h-JCX4b0uDrgxFiB7fmKCwotRTnqMhTD1wljFuuuiYtcWJwa6CV5YR1mSBRTTdcH_EvYbHT3XChbOE7L5B7daBYfnM8olkYocN6xi_WBqpjbcAGxfxo4lN8a5BuFw34sepmg7nwobt9oqK2YOh3TAErTmOi8_nFzOBf6gPFiYVuKMHRq9vJLH7a7U5Etc8K2va2E1vwVKL8bFi31Lj4gqw5OsFIa_q4hlCjdbYkuMYsodPgoqljwCF7lUHBhy_nSkzxwsXYmdKA2dYlsOmt15NfpLU9ehQQXLRDN9bb-LqolC0D4uzDJM8ncomQXA3W3v9-yOHnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TaajW-TM6Ivrpp2E6EFgD-n_-QBr1Z6-8rpd9J7XZx3RJe1K9w3hbj_ygP1_umT4-d8caKSjnUQEUbP8JITxxy5959e15aoVSGdqqqEHEH9KiQjqdIp-gI-CmQAI8cthWD6BOSv49X0Lp2kfXsvNPERY2FqwpuXVXpOeGYe7Rb6CUxvaWkx6Ybh98Ujd9vDqGl-3pkoX6bWFX-7vHosgtoU9jaTInhMROR58TMBLTMoUpFo2-z_wvmvecD1W9Zsh0kGp4gpnB2ADmp3z0ttXRCbzINURDI3d3fspOLCI_tQy5qvsQWoEp5wDebINoHzn3xLv__Ka1IQhEH1zc48FSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه‌ی Hermes: از
MEMORY.md
متنی تا گراف دانش
نویسنده این پست ردیت گفته بودش که مثل خیلی‌ها به دیوار
MEMORY.md
دو هزار و دویست کاراکتری خورده بود (۹۹٪ پر و مدام درگیر نوشته‌های کهنه‌ی توی کانتکست). پس برای همین تصمیم گرفت plugin مربوط به ارائه‌دهنده‌ی حافظه‌ی Hindsight رو توی یه کانتینر Docker جدا راه بندازه؛ بعد از کلی تنظیمات مختلف، اولین اجرا و تجمیع گراف تموم شد.
که این باعث میشه:
1- دیگه محدودیت
Memory.md
رو نداشته باشیم
2- سرعت خوندن از حافظه وحشتناک بالا بره
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dkhJdF97I8wjKq6TC-jJbSEKhDtpl7TbeRnb58NdYpzRr5tbrYM-HLNrFtlDmvle-RorJxty1GccOF9R2zo2eVA_exT725GS3pH-58fqt1m_Lr4Dl8RRUYcZuy3UtdilcwooKuCunpuIQPg-Mzea2EvR8Y8Ni5K_PBYqYUzPhPcifm6Wv-mdmJylJ3GUYoJaleb9fax0nI6otLAjmErOtxafqaSRMua6GXTxWC9jjq-PJge_6agG1CN6sYkktPWC7boYodVld_l1n0ubOp3PNtyeFDjItrd1uAJtVc5-gmqAIZrdHDmh_NuYPFlXxxuNOKjT3T9kwM_hfRngRhNZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xf6ca7xQmOHmX4DcJw3_zN3mHgoZYIjrZsJ9m4u6hRYt3xzikIZcOGW1rSJG_ZAQTDhgoaokT3qO7NpfxHMetkpzCJkwwKzkAxQb61NfW4nwszFcuw5jOHLrWCQDJqEnU-KC2snA_hmwy1ZWyoS0MaDryzbsCm5gPdbBDhj4yKDZOPHAFgWbNHKjdh7yVS2FriYZv1v2xCgUyN2Q1YQJiTGBBlCyn8KSEUELqaVt9euHYEVIzkcCXKfFgdyx_KNUaAzMVagdoNoMDWpphGPvYprFM8DXf0eQl85Z8p9xeaHVLPj32w_wcrN6cyjv3XJT9v-5WT_7Eofg9JR1Uj9Mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VmyJBqbh3clx-wFLDvD4XJDzxXAntvVn8RzKTqjoWbufWPNAnO37jKA4JeWCGR4mMU3hNSJgaB5I2lzNHZECpqZluJDiZYyRF1AUwDYfLzYnXgJ_XJxLaBbloQQMyai96k_3rprohpNG_efgeGGZFBt4sPu5Yc81JwrkWid0uLBAJSn71WwPPCb1uz7xVr6bPQNzCDp11zuuCZlXDzPjoBjNNwOyxDPI8cm3neTyi5etdjnYBbz1iFQ7viomhhr2CkrD_kKh7uu46dFYEj3Z71164IP4Xg8Lb17WrSGXfBx0Jl6Zj0wUMFXr5v2_yYmpAYRXb7s67ShN-qgj2c4OOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HkCLUc7aaWb75ZCexjXpWvhOcVe0v-aBMRKG5_B5bLXdJRkKUOqJx9C3KGBeozREMUPnrOaVIPLLhJH15HRHO5kO9BgJQ51RjXRcJ0T18lixyEcDccxakKkUrKTUVEY8ickjhzZoe1vofMJYnmwo-XEP66kTGgiSsUl6LWA9-jadW_MN4uMYLyP9Kc_EjZxquJO4yJfSOiHGTZQ4_BQAqb6TzPCWamlCnNQi8qUOkms-Ys_JphqKBebvXPSKLCEJoILlrqNcCocCSTZePoJNyUxu-bKF-u2rDeqLync4vabWEo4QB-2Uv6RNwvLhSVutXEy9eDMg2cJpAblPavYaNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این فتوشاپ اوپن سورس که مسخره‌اش کردن یه دوره، سازندش اومد توی ردیت درآمدشو از دونیت‌هاش گذاشت و گفت محصولم خیلی پرطرفدار شده
😂
لینک این فتوشاپ اوپن سورس که اسمش Photon هست:
https://tenzen.studio/photon
لینک پست ردیت:
https://www.reddit.com/r/SaaS/comments/1wsac6d/i_replaced_adobe_photoshop_with_a_free_better/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPatt's Channel</strong></div>
<div class="tg-text">محدودیت آپلود
۶
پکت رو دوباره دارن اعمال میکنن.
از چند روز پیش برخی سرورهای شخصی دچار این محدودیت شدن.
از دیشب وبسوکتِ (alpn/1.1) کلودفلر هم برای برخی دامنه ها مثل
workers.dev
.* دچار همین محدودیت ۶ پکت شده.
در نتیجه کانفیگ‌های ورکر کلودفلر به صورت عادی در دسترس نیستند.
با ech ,
fragment+fingerprint
و چندین روش دیگه میشه این محدودیت رو بر روی کلودفلر دور زد.
فعلا تغییری در وضعیت warp هم مشاهده نشده.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHUiw3S8CnZxotIIcIDaL92gOqzHF8IaoZbU47sV99tabh9Q_7EEAkOIFNKMUZX3hyr5sR9ipxmr0sBvyZH18Th2FJmf46-IpQztcs7xUYjw5dybZxsYWjRDG2dS69RM3Eb0mxHpkVZ-M-B3xJWartWl218Qrqmjc2RuHm9h1ckNA1pexQk20w8nkYwVP0F_sczg-7QgNkpaI92lAhjE_qmZwnpn8XnuN4qmffsXwVnurrvRJEmpyY9ZlCNWNV8qxv_5NyNo-gmGdJGpr-RZbBN4d5HzrDCCsw6mKcQczyMxaOGl-oxlvUhHQ3_Q2Qu87328jeRCnTM56LNOiZJqFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cArcdSD2U1JJHC85F-_N7bqjrCSZBERDsvucN-yEWxPBVypAtyetr0GnQT3ZAv1k9OOIEtXBjOIyegvF5HSJg7x85xyIINwAgYwweoqnG70iX2j7xggHHEXNZfm_9qKKzBJUXQNPVa5XK8pOiphSV_UREQTKovPVg8y8xZNCxx208wyb-S9WyU564UzFPIgcE4prOSA3dzJz_yHvf444z6jHe__cLqLZNcvDdzCRwZ2sAd6pDqDASZNFglkyd4joy1PK4GhVJlyxKsAnmAf-UAVAVDeqsCCTKcgVTgLen246h8CH_ffvHuWtW0jfvfNzZpgA2H59pmszxlcTpOqgBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvOknRaGVGHAnq6ev3sV74gjWewqIrjaGk-HFTT7OM2bJBCNa4lJVtzMNVIVDYXqlKiqAp-DFxfdFAoT0heM__Q_IbG4tM4s6XWQyJypPTfluM3WULd35dFiRIKem6XeLh2mOiByg8AGYnprKS_og_zpl1lNLcOKg5wH0bsfcMgTsdhF9jPGbQdEjE70AnrsDPBYFbpk-U9mOijejndMRv2I6DqyGPoJk4S6_-EMDYfY4K5HTNnc7ev_xGTzE9bAoqK_bDobYWAxs_tGdxqR9dqV_OKsSfOonDFt4gnwiRHPp4trpjsMqQD9DAs-OUJil28dU7cDkGCyfcj1-Nxbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dziYcTtFPbbVN08oBKD7WiMw704DJgTMHXSY3VwMPo-XkeU3o7yb7pYTTeawfSYQsudiV6p3Vz16oyyyVUnMyDoT_rCVEIdydY8UrP4qjZLo1w8LN7cUCo6KOFG8vOaZDuWTZXdrj2vsr2uJPDu7zCeAcIDwMJ1B2lHSesYP92csKm1jJ-D0cKd1TkS35VgGgfduUbuk-J7iH0GVwilrJ1vs8R6rRgfBd09DgFzXtRPIw4AZkm6asBLqHFelB1qiJLOHKH-ailk40waLBi-PeveGAw7XrzKddCkQcGq28igM85vl8UyTcNFzvLTuPBNcu0ySzYDE2SuPqMAn6UArAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا حس می‌کنیم هر مدل جدیدی که میاد، انقدر از مدل‌های قدیمی قدرتمندتره؟
باید بگم که این بیشتر از منطقی بودن، «کلک» شرکت‌هاست برای مارکتینگ
اگه یادتون باشه، 2 هفته پیش همه‌ی این بنچمارک‌ها(خصوصا سه بعدی) جوری از GPT Astra تعریف می‌کردن و چیزای خفن می‌ساختن که انگار خدای همه‌ی مدل‌هاست.
بعد که Claude Opus 5.5 اومد، خروجی‌هاش رو جوری نشون دادن انگار اون مقابلش پیامبره.
حالا این قضیه برای هر دوی اونا در مورد Gemini 4 Pro داره تکرار می‌شه
به این کار اکانت‌های بنچمارک و Ai Enthusiast ، قضیه‌ی Strawman Fallacy می‌گن. یعنی مغالطه‌ی آدمکِ پوشالی
توی فلسفه، Strawman fallacy یعنی از رقیب قدرتمندت، یه فرض پوشالی بسازی جلوی مخاطب، شکستش بدی، و بعد خودت رو پیروز جلوه بدی
هم خود کمپانی‌ها، هزینه می‌کنن که اکانت‌های توییتری/ردیتی این کار رو انجام بدن؛ هم خود آدما خیلی وقتا این کارو سر هایپ و ... انجام می‌دن.
چه شکلی انجام می‌شه؟
1- مدل رقیب با پرامپت ساده یا بد تست می‌شه، ولی مدل خودشون با پرامپت بهینه‌شده.
2- قابلیت‌های رقیب مثل reasoning، ابزارها یا context بلند خاموش می‌شه.
3- هایپرپارامترهای رقیب به درستی تنظیم نمی‌شه ولی مال خودشون با دقت tune می‌شه.
این شکلیه که می‌گم هیچوقت به بنچمارک‌های این شکلی توییتری، نمی‌شه اعتماد کرد.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXCxU05q2zDFz-XszV_agAHx3oK8K0WVFLxG9TqDYyz3EUhtFXM5YQ5urUzp-pCe9cRcl-tsP3qm23sOzo5hh6pqkWQiSXAcuHW5am4fqYmb2Avqnkk3Lq8hMtTzl5RSdXTNVaJCop_3PkGu3D_20IBU2qvJ0wR7QqBAiJoAgVjQ46RkWwreA0JD2RmbKPm7w5glHFZGPy_pObi7qxCcDN6vGES2thAHlLR5eMg4OAdGS-wPXvW5PliOJ50X6DDGivsQKwO0lNA-JEB2E0lMdtOj9InuBvp0i2J9l97gNRiOns-6YMq8zlS617O3iws79IYAcZtL9pofPzt7HOh0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=drilcBUdM9m3WolDt7GnZP-0ELRvkd_YhbeU7IRzOMQ2TnOECocdVSMxT0dMwojFOugC3r8FgHHX8m6zWHiYZPbM9Ujy0ILdRFXZO6FmhuyWkRIwx31qbZLKN6aKy9duAonOwgTZDXX65CE-_ICAPcXFAijO9l1rQI898Msy-nw394WSAZqAqJ1Ri8JzLcXDfXLB9DxxUYQZAWydCfZ7vqzeOfqaQfjic58gdsMvKF-_VLjigOOFV36_oym1_g7djk2Is1TNfdui_Fg1i3RdYQqnHuyK-kQPcbYGczvmA7-6lz16gN9D9S1e_vhhBwflfVfo8WRsncQiQG-7tYgxUqWRSRWs8477DGBxk3rUfgXp8K7CKVcwwIZyIFTOsCQKMXiB0wrMeYGjle1xKNwZgpdimo8-ZWv_nEKGIUr3Zxqcl43zQzJSgl2SBKOjzH5be3dMhsNk-6dJwHjJxsaXA477XBAbiJq5LUM6ivBQ2qIcAAHIKFrCEu06QZ4F-DA2pPZvwl9p_CjkWrCdxBZPX5e6UJ3XnXCyW-B4mUQaofhGyxn1eU7PqtOcakl1lqgslNvneg1XOCQGdiMK5bSMuLzNPzx86RKCf9FXrkD6nSjC8r3HOu-7zjH9HW6AgRjOZeyXadZmbDIKpt3qyUGc-iXqD4xG4KLtKOXPp12sQU4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=drilcBUdM9m3WolDt7GnZP-0ELRvkd_YhbeU7IRzOMQ2TnOECocdVSMxT0dMwojFOugC3r8FgHHX8m6zWHiYZPbM9Ujy0ILdRFXZO6FmhuyWkRIwx31qbZLKN6aKy9duAonOwgTZDXX65CE-_ICAPcXFAijO9l1rQI898Msy-nw394WSAZqAqJ1Ri8JzLcXDfXLB9DxxUYQZAWydCfZ7vqzeOfqaQfjic58gdsMvKF-_VLjigOOFV36_oym1_g7djk2Is1TNfdui_Fg1i3RdYQqnHuyK-kQPcbYGczvmA7-6lz16gN9D9S1e_vhhBwflfVfo8WRsncQiQG-7tYgxUqWRSRWs8477DGBxk3rUfgXp8K7CKVcwwIZyIFTOsCQKMXiB0wrMeYGjle1xKNwZgpdimo8-ZWv_nEKGIUr3Zxqcl43zQzJSgl2SBKOjzH5be3dMhsNk-6dJwHjJxsaXA477XBAbiJq5LUM6ivBQ2qIcAAHIKFrCEu06QZ4F-DA2pPZvwl9p_CjkWrCdxBZPX5e6UJ3XnXCyW-B4mUQaofhGyxn1eU7PqtOcakl1lqgslNvneg1XOCQGdiMK5bSMuLzNPzx86RKCf9FXrkD6nSjC8r3HOu-7zjH9HW6AgRjOZeyXadZmbDIKpt3qyUGc-iXqD4xG4KLtKOXPp12sQU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k7oYU4MiMwOz0q5pRlZpNcJgsfUmMC2f_0f3p8k7TiSrlvzMCe8esrG1Xf8_R9uRJCVjwWy7CZD8IN9Unk7prXUpeFZAPPMg2R83X1aK1CiKq7-JvYL4n6HBya3DDCAC12JxFCH5_7dbCQ8_Pneyd_uAE1K4KlEtinutwPrjrGFUV3bNivJTuwhkECn5VwZo5PGchdS3sceTsg16m7sjnljHjTEZb-1cuqUGDz4ta-h13yua18vax68EhxOz3fR1BJQ3bfdZxF9bSXHcjfGPQAbad2TBjzy6tGZ6nUVtiUFkEPsFPQLaqkykEggxiKN7PXM_j91tKVkKJMIHre9-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZx1tzoc3iiXW-WAEzpbhX_k1cUADatGwI6uHaJsiRhdX7TKpyo57BFzqtpjkrx8R9UWYEwAOjz8FVYGUNagEN2C66noIoC4o_QHNfjSdZxExgjgpYc0rpz0AjGdGY8CRkU1bBLZbMkS1E4awXYC9Tw5miTNH3QmPUlTB0o6oHJR0ygYZAEomLqztTifc1Ul3pqSDXXZBWSEuCF09gi3OgEiTHYpwMXJmcZmUR_Jc5kzYQap_DSNMZA7D_0ZKTQDnsWqAW-Psty-5cLhWFlqtJ8-3uj7XEGsQKIyRcOEBaTRQ6Tgsr50CIra5IFvjttKYPge7IlJZ1hwLM0IRhNcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qP0oNVJh09Znttf6xEiaRLaLzTBkFSMW58eGHGLt0rjliQHfFrjx3g6fz9fhmRIQaW_7sORGtWKcc2MR6DW8KKsTW6mRU4JXHQ4lyz5riVThToGGnWYpGqUrxsfLi6ca6o3HerISAEpFf8O59kMgVnndX8bO0raq3F1MlgWXFdC6cmIVnRZrOT0cQLmbv80wcOL6BFr8YVwzLkCI68M4oB4mdaNJSN1GtC99zclljFdjp8YRKj6uKjbf9uj-0UpIU9dBRtr2KMNJLqDKFEekKJAWP36tuUtB_yRIfwhdLiyQuTmwuckDTq_0OSATEAv4PoUbw8FhBaFas3206iBIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSlvOVoeXwAuJoaQWP3fh_Z6UPQJEXAD0yf_d-BbN4PcVt834jUZpV8Ue4nuWj0tJNs7T2JND6wvGliZ58saADLHRMVp6c4WH70Xvd7OJjon76pdxR6pGfOKm3Fmh6s4ExYRlsuUMX6HWbtTwlEqtzm6Awmj6RLnkRE12rPEGV-xWRHH352i2AL7aDK8gbMHUve8uWb0T3fqSbYlMoux_-oav8gzblZh6ndtb9yYHkgZYy2EzWhOIWMXX6BQtTBqd2n9jBrkmkMefKw_7XP4vQzFCImOc7fIiAMCgeKlAqmPVXs6VWSu9vbyExFL6VuFb6D_DutHvk3QvFqyPUZxyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-d-2MsuCptQgM3diAsLttc1wbY4zl7TN1JzsIBqvPw0RDvdmlfdMT0UuefBdhQiXXiVm7uGb1TSVyGDvNfMR-GSVUB2dlApRVQNE4VYjce7thCVrKKjtRyBxwbTpz_9Xn28eDAosQ362l2HQ0OateoGuPIcS_KJ9AsZY4dtCC8l0U48YH7cwkbsDmCMd-tyXIiTJszsePc0wocYFG70UjwZ5YoPycomxMd4VWkrCW2YOsCbRC79PQx1IFoT_tp-eSh4NPGTt-s7FCky3QLVVUvAia7j6U6T4ANZykOk_9OeI5mHqCJIM_FyU_3TMi2KLopj-ACUc4DwGjrj0ABkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rsTNj98AStWaJi2f89Q3ToB0cl_htGS9QhxEU34ft40UsyWYJD8k3LZGPggU50zjsPGyoCwnfgjVISkg4PxriVl6KuPCIowDJ4dTywXnMECamcEdXd-dL5Ky1zXjvL4aU6D0VRGw_Yqv2YgwJmOQiebm7Plog0kO0FwKQRfHjvLxLhToCOsAk17IXvMEksT7V1FlaC9sdMqTSdeNXN2g93B5UZUzOPc_p1cyLz7c5zK6wQwaw21awBloHsD_krKw4DHFWGENv0fwt-_B9VS-88VMFWxB9ZvTI4v8Yr8-JGrYdBhLp__JJMrvtoU_UyFueMJs9MfJUAzRTxagUXaujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر سایتی رو برای ایجنت‌ها به API تبدیل کن، بدون Browser Automation
💪
یکی از توسعه‌دهنده‌ها توی ساب ردیت هرمس ابزاری به اسم
agent-data.dev
معرفی کرده که ایده‌ی جالبی پشتشه.
حرف اصلیش اینه که برای خیلی از کارهای تکراری وب، مثل چک کردن قیمت پرواز هر روز صبح، دنبال کردن آگهی‌های شغلی جدید یا سرچ توی یوتیوب، browser automation رابط مناسبی نیست. ایجنت باید سایت رو باز کنه، بفهمه چی روی صفحه‌ست، هی کلیک و اسکرول و اسکرین‌شات بگیره، و هر بار که لازم شد کل این چرخه رو از اول تکرار کنه. وقتی کار در اصل «این سایت رو با این پارامترها سرچ کن و نتیجه رو بده» هست، خیلی منطقی‌تره ایجنت یه API call بزنه و JSON ساختاریافته بگیره.
حالا این agent-data چیکار می‌کنه؟
1- یه کاتالوگ از APIهای آماده برای سایت‌هایی مثل X، Reddit، Zillow و کلی سایت دیگه داره
2- اگه API مورد نظرت نبود، URL رو می‌دی و توضیح می‌دی چه دیتا یا عملیاتی می‌خوای؛ خودش API رو می‌سازه و نگهداری می‌کنه
3- از طریق HTTP، MCP یا CLI قابل استفاده‌ست، پس برای ایجنت شبیه یه tool call معمولی می‌شه
نکات فنی:
😟
به‌جای HTML selector، endpointها رو روی همون network requestهایی می‌سازه که خود سایت برای لود دیتا استفاده می‌کنه؛ برای همین با تغییر layout کمتر می‌شکنه
📱
خود APIها مرتب تست می‌شن و خرابی‌ها خودکار شناسایی و برای تعمیر صف می‌شن
💰
زیرساخت proxy و CAPTCHA رو خودش هندل می‌کنه(باید برم ببینم کپچا فارمش چطوری کار میکنه)
سازنده‌ش گفته قراره نشون بده این روش در مقایسه با browser automation چقدر سریع‌تر، قابل‌اعتمادتر و از نظر مصرف توکن بهینه‌تره.
🔗
وبسایتش:
agent-data.dev
📌
ردیت
اصلی پست
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=c73xb3yyEnq7NolU93BOtjmocHFkyskdCrblXq_cS2BJutbTfXLdevC9GArLAReRMRHjlv2t-pCy_UMOHwm9Q4H0R-dhBW-hvF5n8O62hw2-ifYSIbI4z9c4xS480iN4OKcgAstz9IltK1NkR8DEYuXbgP3qKk8NvWwnNCwcvCpPQgQuBV0ydADMavPlIjcDCyZJlfkVU84-MsTJz-r8DLwsb029Ec8dukPzas7w14p-oYwWc5bcgmgqipjDgiKfQGTCOptn2_MQmggojThFPIJKdhIpy437qYxLGQ7Kz13GgfItfvsD4a5cytnA1CQiByVVICzu_k2JBhMgguEwvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=c73xb3yyEnq7NolU93BOtjmocHFkyskdCrblXq_cS2BJutbTfXLdevC9GArLAReRMRHjlv2t-pCy_UMOHwm9Q4H0R-dhBW-hvF5n8O62hw2-ifYSIbI4z9c4xS480iN4OKcgAstz9IltK1NkR8DEYuXbgP3qKk8NvWwnNCwcvCpPQgQuBV0ydADMavPlIjcDCyZJlfkVU84-MsTJz-r8DLwsb029Ec8dukPzas7w14p-oYwWc5bcgmgqipjDgiKfQGTCOptn2_MQmggojThFPIJKdhIpy437qYxLGQ7Kz13GgfItfvsD4a5cytnA1CQiByVVICzu_k2JBhMgguEwvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OxSqTA2pdFV4IORa-eH8oNJfG2qPhJrpHeZMeddVm2h8dDmHWgCmM_uBPh0sgSG7rAG6Re8oMpllRLUQ9ryfjLG1gKHU_dEJeXc0rIjUlFg6O7vYhdyojIwiu4XATYtyJzbumQDJOUTVPsQhqJr6ea59N1H2AoCHkzPHTwbYF_vKzlCNl6DJAaKNCSReExp1Zzye3azyjc9ENXYRwPuDfjZS1hY-X7KDlJ_-Lp5dmky1cPaAjzphvUF2RSbbunir8ZRL6EN8ZmoYuvJpPrUkoed6UpeB1RBSYfLydxH7LVDyJBGVpN6J3vNkAe5l6r08sqsOGVhF-w1nf_9y0EPR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lHCDVrwqtx42iIwLtl_frdyOSF4FiHX93ubgtxu_0y-8k6b6qW3ZeRWKondBUGWDsqN1PEk4RoMc-Y2_d6U1MRIXIcxVftDTEtgDd3POmttI6ziPCh7Upqv-SU_bTz-6AEFeDUSsjFpVc5KXL-IB-5nerhfvfwgpjFoXV001zXmTLpp4Cim7OcuYw5PL3L4OQxrJSGfQDvWKdrE4Kob9Lv1EOKOZx3KJXAmd3LfUO1pz-CuBB8Sq4_-AscS6_dJRCBsv0Ul8IGBucWPNuUcq-oX1mn3QySaaKFF-zG7L0HpBd7xVH3Srowe6K5cSCF3N3R10oVnzOjJAZ7vaohl4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V9rdxcd385-brZzqfUrWtUkl_DIsNeMrzygY-QhJKP9wOM3qorSlpYZ2E6qdGz13dAtpglBYRt1j-XeKrDeGfOrUIPRgvhiACappOMTAOBfnwfmWdOvH2XySNdO-w6qEEEmpdPkAWK3hnSb4k2FyE9EpzFkDMC57k41_gm7oVSx9PqSGnf1255_Rr3PIUesFzPUCTuVOAPBeruRZ2nosZrPufMtBJ-CC2Vge5hWlQAzqbFg98oV8Gw4ZJuEsqHM0BgQSNxJ6csNj0RTrSYFYqEaAodkP9W426jY3exi3efGpQcm0qoX4WJLvhbobGCR3kiRoeD5CUV5bRxbQtDXTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kr5Qs2XgeAH2feVM50fKiN8-IOxq3tjGbxleLE6LavS9eloVWCJcVTUNHThScqIuu95hn3F3oLFXlNTInJxmTV24P8y1kQPJ44mYfv1eNkx8oqCEZgCwVmgPYR0NrNwrtGLgYdByKuc3icE3AdWOjw6UZ1XuywmlJ-fBSfhJgrZ1ST53J6rVZTxzvcj0pa_qYrCSdVl5oygCijmJ5nt2ZEUUcyoZqU7qtcHHWNaGVcpw0QgQGA4RPsQdo2l-_uv0q1IDN0QJxuu1ugefetGGZyznVr4EoFd_TfS3IuNRrw98pJV8b2etxxJGh-MuHueCIRjKcC4o_6SOjEboac9Kzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اروین از توییتر
یه سایت بهم معرفی کرد شبیه به Mpay، اما بیشتر برای بیزنس‌ها یا کسایی که تراکنش نسبتا بالا دارن؛ با قابلیت برداشت مستقیم از کارت و کارت‌های تبلیغاتی برای کارهای حساس مثل تبلیغات گوگل ادز یا تراکنش‌های سنگین و گرون
از اینجا می‌تونید ثبت نام کنید:
https://finup.io/?code=MATINSENPAI
لینک، رفرال هست. اگر دوست نداشتید میتونید کد آخرش رو پاک کنید. برای شما سود یا ضرری نداره
نقاط قوت:
1- برای ساخت کارت، MasterCard داره به جای Visa(شانس قبول شدن آفرهای رایگان معمولا بیشتره)
2- قابلیت برداشت ازش وجود داره به ولت کریپتو(هنوز تست نکردم که KYC می‌خواد یا نه اما توی مستنداتش چیزی ننوشته بود که احراز می‌خواد یا...)
3- آدرس BIN آمریکا داره
4- از ارزهای مختلف برای واریز پشتیبانی میکنه برخلاف mpay که فقط تتر داشت
5- دو نوع کارت بیزنس و تبلیغاتی(هزینه‌شون یکیه) که کارت Advertising شانس پذیرش بالایی برای کارهایی مثل تبلیغات Adsense گوگل و تیک‌تاک و متا و... داره
6- کارمزد رایگان روی برداشت و تراکنش کارت‌ها
نقاط ضعف:
1- هزینه اولیه ساخت کارت 10 دلار هستش
2- برای KYC شرایط ثابتی نداره اما توی تراست‌پایلت نمره‌ی خوبی داره
3- حداقل هزینه واریز به خود کارت(نه ولت)، 50 دلاره
و اروین گفتش زمان واریز مراقب باشید از صرافی‌هایی که امریکا تحریم کرده نزنید. ترجیحا بریزید توی تراست ولتی، جایی و بعد بزنید به ولت این سایت
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=Ix6Sox6_GvBQk_yiMMCQsDB7HKC171xcLBmfwhwzcZwnYfdZWkGXJbGnzDqQvYn6KxcLpAydEWGdKwm1u0l8SMdMk4571zL5lGgtD4AdG-qCnXlm2rnaVcHPpy2-iYcYhm6mgFuimj5we-3wJ6ugz8txj04P2BuAUm5DluMUf5l6n-3rT9dqdNuS2jF-x8mW_qaHo1e-KDon1gtR3tXDIW4OpZnW5XbvfIVWVWjfC61-LcNnuXThBC1bE8q2dY-3NP3zz7_ijZxJoI5AAA77fjWxyZBh4sqIfC3oQKIed_NbHhBDHvjhlXVD3YJCj4N0D6shEhqOOixX3a0QuNPPWUAGVWuc0Og4nnPKvL39J4iS4SHtNUWXuK0KGdweq316w06eMio1C48fnQe_tRe_sVva9c7OQljwbswximIlQfY3DnEHiiXCPGTxrad_dC9kSmwhM0rRBiJdgpm-IagYHPaiUoOJALKhXijRcUfzQgz91ganpvMz90cPf7szX_tDgbgUFRRVyzbrj34euFWQ5yX93e_146GfZF8ZSdWOBCc48v0fR7kVZY53XnXNBkAfONJuA7o1qe4Oe_V1l8xTHQ8bE_UsymI98aMYR9dTqBStUwYLl_AqTTU_osfLUgJmd86xs7GzuhSQ2coY4ISFSsEQBO_Bbe9jj0PiSpNzxLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=Ix6Sox6_GvBQk_yiMMCQsDB7HKC171xcLBmfwhwzcZwnYfdZWkGXJbGnzDqQvYn6KxcLpAydEWGdKwm1u0l8SMdMk4571zL5lGgtD4AdG-qCnXlm2rnaVcHPpy2-iYcYhm6mgFuimj5we-3wJ6ugz8txj04P2BuAUm5DluMUf5l6n-3rT9dqdNuS2jF-x8mW_qaHo1e-KDon1gtR3tXDIW4OpZnW5XbvfIVWVWjfC61-LcNnuXThBC1bE8q2dY-3NP3zz7_ijZxJoI5AAA77fjWxyZBh4sqIfC3oQKIed_NbHhBDHvjhlXVD3YJCj4N0D6shEhqOOixX3a0QuNPPWUAGVWuc0Og4nnPKvL39J4iS4SHtNUWXuK0KGdweq316w06eMio1C48fnQe_tRe_sVva9c7OQljwbswximIlQfY3DnEHiiXCPGTxrad_dC9kSmwhM0rRBiJdgpm-IagYHPaiUoOJALKhXijRcUfzQgz91ganpvMz90cPf7szX_tDgbgUFRRVyzbrj34euFWQ5yX93e_146GfZF8ZSdWOBCc48v0fR7kVZY53XnXNBkAfONJuA7o1qe4Oe_V1l8xTHQ8bE_UsymI98aMYR9dTqBStUwYLl_AqTTU_osfLUgJmd86xs7GzuhSQ2coY4ISFSsEQBO_Bbe9jj0PiSpNzxLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=eTQ8Anc7Rym7bq51PKmmg_aWw8gm7iVNMJ-ZZJeXObSUawbjjOWIogPNrJqEbAMTkWnwUInOLujCW_yE6wAvL-P6kb3N7RIO44Z_g7Ln6xc99lp-Z28QToszxvxBn2EEtJ1GpYSAhS67MRflspDk3hi0mMSTxJpRSS128eJnL1pyi8WY20nBTTHXCSxeQRMVZuqbu0_k23WdnVN4VDDzzuKfhaZUadI3eVqfXELHlt_bA_snET0oicq0PuOYp7HyjMy2EyDthG7PifTRqmKRWV5LlTiFOoRockN4ddowcoHrapiepuyk4zZwc4v46co6VLWZsoiLUNFkzrCq8KOIXg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=eTQ8Anc7Rym7bq51PKmmg_aWw8gm7iVNMJ-ZZJeXObSUawbjjOWIogPNrJqEbAMTkWnwUInOLujCW_yE6wAvL-P6kb3N7RIO44Z_g7Ln6xc99lp-Z28QToszxvxBn2EEtJ1GpYSAhS67MRflspDk3hi0mMSTxJpRSS128eJnL1pyi8WY20nBTTHXCSxeQRMVZuqbu0_k23WdnVN4VDDzzuKfhaZUadI3eVqfXELHlt_bA_snET0oicq0PuOYp7HyjMy2EyDthG7PifTRqmKRWV5LlTiFOoRockN4ddowcoHrapiepuyk4zZwc4v46co6VLWZsoiLUNFkzrCq8KOIXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uTA-R5FWNSveXgex0f9Zcc-cepMwVAR7Eq3EPOXuzmPu9P672d5lex6cn6fMV_Gu7AvvJwcQiA3Neky1Cska0cV-iWM8iAI2WYBVOcBBk4u9jHCWXwkHsdTfbSpOz0CrTvCG0WLLsSZqt-zT2MmO1vLBhpszM8z306h_x-VdiehGc5JSz-duTNR0fCtIENRE2FrM_0b3jxVvYulBHjv3Jp70pxyjiIcTjhIKomGvzu50RfX7vuKAHaSLeFsmdkYO6TwuDX19KlPW2KN0xZdtL6-Ya8AXDxQozcbmffJWwj_MzYum3C5tXGepDV3iaba9BNf0UT7RG3f2muuwCqjHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uhGtZSO5gF4THl-KlhkrKD3igSpV3CEK7uZx2HbTWQy1kiG8JpO6ASlZOZRllZUW_mgnEs5NxOsgjxqDKYvZxbInMo48afuNz50_PeH_COughA5IcxJFuCzrGMIPFx6PUGyWTP7iPNYX5y36VHnRuMyDuwVAhScqw_CRZzpXOJ894xk01LMtmyvFkq9tUmK9qmIhrvPVPri2nIk8JCHtgUcCkopkxOh_SScbQHTSNAIemQ9DfBH8JmwJQJfIx3q7QrVPHd7Qeet-6uK1-TG7khQdyIGIRZ5WyJrDQ5le9GL8HPZMsN0ny_5seZ4SgXYgqkkYAzqTY1Q9L19zOJVIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زبان‌های برنامه‌نویسی توی عصر AI چی می‌شن و چه بلایی سرشون میاد؟
خوزه والیم، خالق زبان زیبای Elixir، یه مقاله‌ی فکری نوشته درباره‌ی اینکه وقتی ایجنت‌ها بیشتر کد رو می‌نویسن، سر زبان‌ها، ابزارها و کامیونیتی‌هاشون چی میاد.
چند تا نکته‌ی خلاصه از صحبت‌هاش:
۱-
کامیونیتی:
هر زبانی دور یه سری سلیقه‌ی مشترک شکل گرفته؛ پایتون «یه راه واضح برای هر کار»، روبی «خوشحالی برنامه‌نویس»، لیسپ «تغییر خود زبان». وقتی دیگه خودمون کد نمی‌نویسیم، حس تعلق به این کامیونیتی‌ها چی می‌شه؟
۲-
اکوسیستم:
فاصله‌ی اکوسیستم‌ها کم می‌شه، چون پورت کردن کتابخونه‌ها یا پیاده‌سازی الگوریتم‌های یه مقاله با ایجنت خیلی ارزون‌تر شده و زبان‌های کوچیک‌تر سریع‌تر به بزرگ‌ترها می‌رسن. ولی از اون طرف، وقتی ساختن یه کتابخونه ارزون باشه، چرا کسی بیاد روی یه کتابخونه‌ی مشترک همکاری کنه؟ خودش به ایجنت می‌گه دقیقاً همونی که لازم داره رو بسازه.
۳-
سینتکس:
سینتکس‌های خوشگل (مثل optional chaining به‌جای چند تا null check) دیگه اولویت نیست، چون ایجنت از boilerplate خسته نمی‌شه و از دیدش همه‌چیز توکن ورودی و توکن خروجیه. به نظرش زبانی که ادعا کنه «برای ایجنت‌ها ساخته شده» و تمرکزش روی سینتکس باشه، داره حول محدودیت‌های امروز مدل‌ها طراحی می‌شه.
۴-
کامپایلرها از بین نمی‌رن:
اینکه ایجنت مستقیم اسمبلی بنویسه منطقی نیست؛ کسی نمی‌خواد برای هر معماری یه نسخه‌ی جدا نگه داره. تازه هیچ زبونی توی همه‌چیز خوب نیست؛ Rust، زبان‌های اثبات قضیه مثل Lean، Erlang/Elixir برای سیستم‌های توزیع‌شده، SQL، هر کدوم تضمین‌ها و سطح انتزاع خودشون رو دارن.
۵-
تضمین‌های قوی‌تر:
اگه ایجنت کد می‌نویسه، می‌شه trade-offهای زبان رو بازنگری کرد. مثلاً type inference برای آدم‌ها خوبه چون نوشتن تایپ حوصله‌سربره، ولی ایجنت حوصله‌اش سر نمی‌ره. نوشتن صریح تایپ‌ها اطلاعات بیشتری به کامپایلر می‌ده و دست زبان رو برای تایپ‌سیستم قوی‌تر باز می‌ذاره. به نظرش زبان‌ها در آینده با این متمایز می‌شن که چقدر تضمین می‌دن: از طراحی‌ای که حالت نامعتبر رو غیرممکن کنه، تا تایپ و اثبات، تضمین‌های runtime، و تست و fuzzing.
۶-
دیتابیس برنامه به‌جای LSP:
پروتکل LSP برای IDE و آدم‌ها طراحی شده و با فایل و خط و ستون کار می‌کنه، که ایجنت‌ها دقیق دنبالش نمی‌کنن. پیشنهادش اینه که اطلاعاتی مثل سیمبل‌ها، رفرنس‌ها و call graph به شکل یه دیتابیس با زبان کوئری در دسترس باشه. آدم حال نداره برای پیدا کردن رفرنس یه تابع کوئری بنویسه، ولی ایجنت راحت می‌نویسه، حتی کوئری‌هایی مثل «همه‌ی مسیرهایی که یه مقدار می‌تونه nil بشه». برای همین هم جادوهایی مثل monkey-patching که کد رو غیرمحلی می‌کنن، بیشتر مشکل‌ساز می‌شن.
۷- در نهایت
Observability به‌جای دیباگر:
breakpoint گذاشتن و خط‌به‌خط جلو رفتن کار آدمه. ایجنت می‌تونه سریع کد رو instrument کنه، trace جمع کنه و اطلاعات رو کنار هم بذاره. پس باید runtime و state سیستم رو جوری در اختیارش بذاریم که بتونه برنامه‌نویسانه کوئری بزنه، حتی روی پروداکشن. اینجا هم طبیعتاً یه اشاره به Erlang VM می‌کنه که این قابلیت‌ها رو از اول داشته.
جمع‌بندی خودش: زبان‌ها قرار نیست از بین برن، ولی سؤال اصلی عوض می‌شه. اگه دیگه برای «آدمی که کد می‌نویسه» بهینه‌شون نکنیم، برای چی بهینه‌شون کنیم؟
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkFsktHI6JyMLdjc28wfnMGn4BFdXyjNLWumNswLIPulAzx3PRV_2S6h8Tu9406DrQxSeHjXO_ZUucZCLl3FSy3wdDgqvwmKfYTINxkpEAGJ0wKaspCYwBI5uaClMmF1KbIFPgv23t4ld3OmO7dfHNEpF0Iv2u6ozki58VwTExTVSvPuSD7Vsymei7rFQJfvan_fC_VNnFOQ76-07zTu9ccsZn1jThWK6zI_MVUdHOWcPiDRlUNF3zkTinT_dYWUmLclJVf77DdHQOwwvTeo1flR_qDkb_FNNz0w2k7JImDmFpUpSr8l_Pm4P8mE4jXY9ZREQkliXGFsp4uqX0OvpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
