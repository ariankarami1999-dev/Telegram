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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 22:39:44</div>
<hr>

<div class="tg-post" id="msg-5469">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/MatinSenPaii/5469" target="_blank">📅 21:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5468">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/MatinSenPaii/5468" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5467">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بزرگترین مزیتی که ایجنت‌های شرکتی(Muse, Grokbot و Dots) دارن اینه که با مدل خود کمپانی یکپارچه هستن
برای هرمس، یه کم چون دستمون توی انتخاب مدل بازه ممکنه گاهی اوقات گیج بزنه یا دو نفر با کار یکسان، تجربه‌ی متفاوتی داشته باشن
اما همچنان هرمس رو ترجیحش میدم</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/MatinSenPaii/5467" target="_blank">📅 19:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5466">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قراره با هم یه اپلیکیشن تمرین زبان با روش Shadowing بسازیم.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/MatinSenPaii/5466" target="_blank">📅 18:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5465">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tFDlzDtYWvDtTPhLVTtuIkAAz66_u7QDZYBSkYsLhhYzsqNk0-fzzLV_IHlnRzMF3jsMr3qjQXljvrbgPMxBh7RE_akynaEIY4RCpKn3cKmzT9B1GW2C0A8kbq06AMBAUWqOUURPX3Jn8I17qoXfIzXxGkk5rBoYcWHq7GGNBL3uf82u0a7_TC3fUgUkX5EpiovDkRaUMhQkV-Q-db6skuAx3usCKV4B0X-bJ-ITTVxoN2CcDvKVx8arPO0FPfuXc0Vm4RH19FKeYtH1n3k3BXxmHu9QAao4kRVWchCcHeAdr5j_Nz9bTWsxzfaF-Vs_s0sN7yrqHUdmhCvFGeJjiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ردیت فیدهای RSS را متوقف و دسترسی عمومی به API را مسدود می‌کند
ردیت اعلام کرد که به دلیل اسکرپ گسترده داده‌ها توسط بات‌های هوش مصنوعی، پشتیبانی از تمامی فیدهای RSS را از ۱۳ نوامبر به پایان می‌رساند. این شرکت همچنین تاریخ توقف کامل دسترسی به API عمومی را مارس ۲۰۲۷ تعیین کرده است. این تصمیم در شرایطی گرفته می‌شود که فروش داده‌های کاربران به غول‌های هوش مصنوعی به بخش پرسودی از درآمدهای ردیت تبدیل شده و این پلتفرم دسترسی رایگان را کاملا محدود می‌کند.
که خبر بدیه برای ما
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/5465" target="_blank">📅 18:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5464">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">امروز زیاد ازش استفاده کردم
گفتم یه توضیحی راجبش بدم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/MatinSenPaii/5464" target="_blank">📅 18:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5463">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یکی از قابلیت‌های بامزه‌ی یوتوب، Hide user from channel هست
این شکلی که وقتی کسی کامنت دری‌وری می‌ذاره، زمانی که هاید میشه، هنوز می‌تونه کامنت بذاره، اما کامنت‌هاش رو فقط خودش می‌بینه
نه من می‌بینم
نه بقیه
اصلا هم متوجه نمیشه که هاید شده
😂</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/MatinSenPaii/5463" target="_blank">📅 18:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5462">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ektvRyoDwmQq38R-RAYS4gZ7vpp2KxenNfjIFcW-eYbZjMjKkowct2TJYdmswC_rMNqa_97OcH2yyjZRyOBbG89i1o6ALVsAYCLGreKL4zH-Z9Y2_UKJGz-na9swCkc61cccwAPFR81ASWr-lKcCj2_uOnxJ06gyT-ydQf4_UCkH26OLOS6hR2j7Qsde1dRNlLCALjN9QfXJtxmL1GoDDvHavYNiURPkovi-l-gi0MfYBapEjIKGxLIJyUh3mQ3tcMjDiUdtDdoVHWg1HmznD1oKFUSL7wUCpRmeuUu1bfM8CitOqSn0yY0fWZMhhOIPjHAHq42WGRk1bUQBN9brbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate  توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب: https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/MatinSenPaii/5462" target="_blank">📅 18:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5461">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IlL1mIbZxoDbp7jrCFzAyY662tzLzUkFAEv4NstSss61So80bY4PEC4XLvkpcT3GkQMTMMF19tS-37f9s7EbbXl45IerVElu-8XBeHxZ_kHgkEikUkCNs-3npELkJwJpB0DidBXQVorTfSMdcpCYg1J8rYGgYt1ry5VhGhQVaFsBt1HOpTa3LFiWsJFqAyNKMVLevCKRnETZ417B-mEpYXC_sM5wy22ZrN48EK9SczNb3AuDo211_wSuwx0O59wjLNBKaQzIXTQbvbs60sZS2-5iIziKqXOXumyCZelc51qQiB6_FhRIRrPIIBNeNyhWEeAYN-OxCIUvTdN4PY_1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Decisions API توسط OpenAI برای اتوماسیون فوق‌سریع تصمیم‌گیری در ایجنت‌ها
سم آلتمن از عرضه قابلیت جدیدی به نام Decisions API خبر داد که ساختاری مشابه مدل سریع Jev از استارتاپ TypeSafe دارد. این رابط برنامه‌نویسی به توسعه‌دهندگان اجازه می‌دهد مجموعه‌ای مشخص از گزینه‌ها را به مدل Luna بدهند تا با سرعت بسیار بالا و هزینه بسیار ناچیز، به صورت احتمالی بهترین تصمیم یا اکشن را انتخاب کند. این رویکرد به ویژه برای کنترل ازدحام ایجنت‌ها و اتوماسیون لحظه‌ای نرم‌افزارها کاربرد دارد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/MatinSenPaii/5461" target="_blank">📅 17:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5460">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slH0EinZ3VyQf9kbGdBG3i8Uf3VItr7Bs-ic4ZMFfC_6JYTQXltCWGSuuTZR_NNusnD1F6Swgkp6YGGGUnkLCYnBtWuY8xT3kLZTgQdFa6EwIhSyZ1ooKlVfSsNDrt0Njy8m4ptJKxohnULDX8oCBTPUuVkE_DnRuAwFc7UrHg3_wfLVCNPVKJ2TCcbnA-B18JsBFIHUod69K0_psn76Uu3XSt7zmnstgi0uB4QHb2r1WDfzvVF-Euqty2A9hkluSzKMOnxANEOGJIhvMYurDxAXWEJe9e7I8XC-GQM983XGyHicPPSzHfI-hS4O42pLBBmyRmN-pN7kc2DqUuadYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به قول Theo، چرا واقعا OpenAI هنوز داره از GPT-5.6 Sol استفاده میکنه توی چتش:))
نه تنها 6 sol اومد، بلکه 6.1 sol رو هم دادن و چت هنوز روی 5.6 گیر کرده
اولین باریه همچین چیزی رو میبینم حقیقتا بین کمپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/MatinSenPaii/5460" target="_blank">📅 14:07 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5459">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jpyRVqtOrCixdrqsDfDEGQj5ujFkhsA7BVB0P_fDGk9XrmXSDuPReGqfXEf9AsF7QtE4zgYW_ZwjpM0sMhIe8yKAxMnFDJd66tGIjXZsvsLa28wlDm1ETdxVrBwkyP93mEVsYFVIA4TlmD0wrkh_eswcAia3jkUhYA_ugfpv6Xza8CPlrnqLwRBSw5NgkO-4cSrIx1N3sPuqT3eGbjwObl56gFWREYTCV0Ie-cb3GgOJTKT4kTgGzqcnGomcDqLZp7ad8RhtRJtH7c8KKLI441Nyp8ZU2btAyzA2JhrhtqM_wAXmAeK43OMd8DwOOdBJvsS46sOF5Q_tBLF8_ikQfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بله ما نسل Z هستیم
😂</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/MatinSenPaii/5459" target="_blank">📅 12:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5458">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TT5pQLBJyUKDcSrsb8xlwxIemxzA3DfKeMZJF-BkCKS5F3mvI_6dqTSa-sWGyECtM_Da7ekkoKg8ienSKrLyn554AKbhvRptz_wafbZlOQfxf78dgtk3YQh6yocgWoWuFlqEerYFz3ZX47dQA7Riu-HO79og2u2ZdS9GA21YlvuMYC4TGNpaAyXUmlfAvD-xUKwPM10fqyZ47oKGbbN779uK0_1jswhzjxvMcuEnETcXbMU262dfkTqcCapzjo8V3QLsYA_AqeZbigWFtAxdXxIEdgrikPG90bNExAuodLRpuY5VceYKXeD70YW48Jcv-jJGdLeyHx9MAyNrN0YE2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر ویدئویی رو رایگان به فارسی دوبله کن! آموزش Gemini 3.5 Live Translate
توی این ویدئو بهتون یاد میدم که چه شکلی، هر ویدئویی رو از هر زبان به یه زبان دیگه، دوبله کنید!
📹
تماشا در یوتوب:
https://youtu.be/dPKSMUR5cQE</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/MatinSenPaii/5458" target="_blank">📅 12:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5457">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شدیدا حس میکنم مدلهای چینی اوایل که اومدن غول بودن، بعد از عرضه یهو ضعیف شدن
مثلا هممون به Ox Alpha دسترسی داشتیم، بعدش که glm 5.3 flash معرفی شد اصلا اون هوش رو نداشت.
یا من به Qwen 3.8 preview دسترسی داشتم و خارق‌العاده بود. سرچ کنید توی چنل نوشتم از تجربیاتم. اما الان Qwen 3.8 max وقتی ریلیز شد هم از مدلهای Frontier خیلی عقبت‌تره هم توی بنچمارک و هم توی عمل</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/MatinSenPaii/5457" target="_blank">📅 11:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5456">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bWU5lIZzVq2_sydpkfCbh8IoveaJ-sVNhod-a6mIuCEAHINT_dMEAoRkVf40Sl6YCxxp-llJPVrB5c-DQ136X-DCee12NB2uM859jM26zbGItJmbTwXwxTY4wYv3JrHbDwhVTRx2FUyrf_AO1KpAOhbDJJ0H6H2U-Xf7_uzl5VMXoY85dXYYTArwCjLaz7Eb4NzVu1of4tr2izgmOlEqijiJDFL09xd9L6onTvztwpNF-JeazLvgWo7EBoqoG_bThoweav28C1MQoeU2dIp9VgnSBLA1Jupc2BHCltabxpbI4a_LE3o8vs3GWj6oV2m_iSDWLQi1NVVb2Vw-_lMvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم به نوبه‌ی خودش عالیه
Hallucination یعنی توهم زدن ai
که این یعنی جمنای 4 به ندرت از خودش یه چیزی رو در میاره</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/5456" target="_blank">📅 08:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5455">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کلا هر مدلی که میاد
این قضیه‌ی Benchmaxxing پیش میاد
نگران نباشید
میگن توی کدنویسی اونقدر هم خوب نیست انگار و باید منتظر موند و دید تا فردا پس‌فردا که شایعات و تست‌ها به کجا می‌بره ما رو</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5455" target="_blank">📅 07:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5451">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NJR4SZyajLQgLfhSncVwiAtaj5tXQAe3gV3cktaRvthVjBmmB0EZLBHqrDUUSGBzVD9RvkseoCDND74mYSso_a1z0nnIA01gbbEfKrJ3yotnaIP4KkFmZtpzrf91IalnrmJ5ZO2GDUzINRQt7S29RthKNof2KFdUP0FlWJ92ryl7nyUGPvlAzccz-3cqKVQ7KCOCJsGDmBaKcsU5T-teT9kmH29j50LxNcQvehyIvDzlhNNrBLtsBSsOmFXFKLlQA0s9x6_RDSqcbtLOxrfDTF7EcN25aUQIt0jBv-w-5s2BlF27s0taavC63yLpl8C2nUj9lg7HoUm4FKY3Ke95xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uqMy5pK2Do2A-4AmNqPHrvR9BVwCmD85b8x7deWCaXUhRp7tEdgV9YpnzEmnoPgmtMpRta3pgXwlTUfE_bxH7SSX9_UrIyCGxL2lNGLrC2IxjeIBiLe-NKF274EhWQ8iwWmAwVXqL1OtkUGzGWL6ipvNae44c3cpXeWxoSRJ-bGUIpYwBAhfGGfqDIY5a02o1Mxo58L9Kq4AUbowJ5CC6GmUVy91jpoqKb6w8IRWfH3TWXfJj-cgbpUVjoXC3LM2wNO-8xpf8LDlitj6KMx8WqPm7gAQFkax_Gg8uv43LMEXnthFZgBZByB9fhumsjynkJoZhIcapRMpDIkyHcDaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CDFew6PSAqBvCh8-f02Q-aIW5D_3Xsyl3WSqaHZPTKAnn_YBbnKWVhgRmKvpFwr2y1ZGHxsrcdC2ok8Pv4vOQ0pTf3-s9kG6VJhlNv4sKCABF9SejYm8zASxW8cJi8xNcNUX--Y-ZGdKxg7cCFkg46urEi9ODG32fBhkvi1px31dwMbyzNOn_jvupzYWPiVGvwOej7qY3HLUtPkdaNXhG3u2aJvXFWfh5EzHyafa8_DObi9P-Iit1kdKhUFd0-E8iUyvyXbfCaE4c0G8zp6ijkqv7-w9gH5UrpEuhJRQ65Bnw1vbcV-3FtTA_ZUMDf37zXUV1IWe6SQFKTAUwtHvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GiIjkJK8Dgjv2vAJx0BKrTNs6zHStXo4bbS9zJ8NAHg4dnRNUQQfe1KaImT0QZlqhs5l7gGAsVTNuQOhwqfs43g8NsjAsWiE0RPFlMuQxNg_vpBN9kwxfkZzER0qaYnxOxB_NVsTjIvuUqBg-s8pTY-phIup-39NEW3uAnXBKn-oEbfhIhY9qHMi6YMmLYyq4I636ZlwkhLjd88_z_gtBvBe8pvEBLQbCHPSLu05ynrWccsPxAsNOx-GowODEsj_pLhJlAf24R4ZAcDCIqtK1JLkztaTZ7sdbaZMlXtp6bn-_xsxH_wRhaOmpaN8l0HCGpXMSEouAEn0riOYmQ1H8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگل از Gemini 4 Argon رونمایی کرد: تمرکز ویژه روی مهندسی نرم‌افزار و امنیت سایبری  گوگل دیپ‌مایند نسل جدید مدل‌های پیشروی خودش رو با نام Gemini 4 Argon معرفی کرد. این مدل خروجی وحشتناک تا سقف ۱ میلیون توکن(پنجره Context نه ها. Outputای که همیشه 128K بود برای…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5451" target="_blank">📅 01:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5450">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yr5yiPsw7-Cx_By4yHnpMBe89UWp3b8TeKGHYnOg-Eaw_0yufSrjW_USTcY5GCg1T1SsteM0a41Wp4TExEmeKSe4-h9kkl80yDsQlRutkMRj3f7Bs2bNJJRbkYQVm2m49edBrTecFW7zWudqCGq5i6aswEcRpHM-kgc9mojRCfWRIur6KPP_74Uvc3E_OpyNgBPCjp5WJO7V_5ghJh8LGQ2DIow7tuy2E5veC-gFJhcEVGFC57BB7u7fzLAI2FTe6563rDhSA06PgL9VT4gOT0j-DMYBndDsmvJ_3BwxfLZQ5VVbso77VJqJ94A5JX49J_Ov0g9j-bHu8t4u-GVSOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb66b496c.mp4?token=Yr5yiPsw7-Cx_By4yHnpMBe89UWp3b8TeKGHYnOg-Eaw_0yufSrjW_USTcY5GCg1T1SsteM0a41Wp4TExEmeKSe4-h9kkl80yDsQlRutkMRj3f7Bs2bNJJRbkYQVm2m49edBrTecFW7zWudqCGq5i6aswEcRpHM-kgc9mojRCfWRIur6KPP_74Uvc3E_OpyNgBPCjp5WJO7V_5ghJh8LGQ2DIow7tuy2E5veC-gFJhcEVGFC57BB7u7fzLAI2FTe6563rDhSA06PgL9VT4gOT0j-DMYBndDsmvJ_3BwxfLZQ5VVbso77VJqJ94A5JX49J_Ov0g9j-bHu8t4u-GVSOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوگل اون پشت در حال آپدیت دادنای مرموزانه و کار کردن روی مدل‌های Aiاش و بیرون دادن شایعه‌های مختلف:</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/MatinSenPaii/5450" target="_blank">📅 01:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5449">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rezNiVpAwsKjSNkSS0Ijp5vvkc7DVX3YdEyEHvYlwzvxzD1uSr-NCQdI6KWxalALEK9GU3jjdCxpzk2UWzeE4pmKM2n0Sv7wUQnB_H7XjWAAGhFvusxoOfNQdTm4DuDVHtVYHm0oyOgGzCO2bxWaPZ67YatVuFkHrY8SsUzFgAODgMXFCbt34zfeQVOCjplsOqCxUR_xUSQJy7VcFLOVwSZaccr6-Ookomc4F_PY8hiJhHWhkJyYmOnk8HJPsbdYS4jWLgEoef_UqALbejP-KbdADWLhqm1P28CFiy_mLO0thmyWB6Skkaw519ig7uFn06mw5gIDvNxdPdS9geACwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5449" target="_blank">📅 01:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5448">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بیدار شید بیدار شید
جمنای 4 اومدد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/MatinSenPaii/5448" target="_blank">📅 00:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5447">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kx-0bLitRiZ95J11isgggArG_qcmb7pNf6KnqVh3rCYpVza_fqlMzAwKQ1KJ0yql8UQ3W8Gzg8W7sFGkqlrnQepVSX0uCGT2wtlI4L5JRo5aQBOpuj76RPc6m6CQvq6-xjEXnoCg5DBKJ_ORGFqWUrIWeSsWYWINR4-q1elTdc7ifHkVEPgFkoxotcIST45Dr-ckRjg9cKTuKLL__dD2FgBZxlAPfTfkQKnqj1hUbQJ-rpPt48lHoJ8oWPMoQjK0OvSwFzJoBZi7cuqE5jZWOT_mWDHEi8KzkCQer8hpyhdoZmy3HC4bfgPrU24kaYDdo9LaiftzINn2kIWDOyTOWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش هزینه‌های هوش‌مصنوعی با Auto Router در Cloudflare
کلودفلر قابلیت جدید Auto Router رو به سرویس AI Gateway اضافه کرده. این سیستم توی لبه شبکه (Edge) پیچیدگی هر درخواست رو می‌سنجه و به‌صورت خودکار بهینه‌ترین مدل رو انتخاب می‌کنه؛ یعنی برای پرامپت‌های ساده مدل‌های سبک و ارزون‌تر رو صدا می‌زنه و فقط کارهای پیچیده رو به مدل‌های گرون می‌سپاره تا بدون افت کیفیت، هزینه‌های پردازش به‌شدت کم بشه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5447" target="_blank">📅 23:17 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5446">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">من معتقدم با مدلهای رایگان، مدلهای چینی و ابزارهای رایگان هم میشه به خوبی کد نوشت و ابزار ساخت
و به زودی برای اثباتش، یه سری کار انجام میدم
چون میبینم دور و اطرافم کسایی رو که هیچ کاری نمی‌کنن، تلاشی نمی‌کنن، به بهونه‌ی اینکه من اشتراک Claude یا GPT plus ندارم و...
و این کارو انجام خواهم داد که شاید انگیزه‌ای بشه، و شاید ترغیب بشن یه سری افراد که شروع کنن ایده‌هاشون رو بسازن</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/MatinSenPaii/5446" target="_blank">📅 21:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5445">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ویژگی‌ای که Dots و Cues و Grok Bot دارن نسبت به هرمس اینه که اومدن قابلیت‌ها رو محدود کردن!
بله درست شنیدین
همین محدود کردن قابلیت‌ها خودش فیچر خوبی بوده(برای اکثر مردم و برای مارکتینگ خودشون) و باعث شده کارهایی که میشه باهاش انجام داد ساده‌تر به نظر بیاد و سرراست تر بشه. از اون طرف، چون با LLM خودشون سازگاری صد درصد داره، به 99 درصد ارورهای مدل‌ها و api و... بر نمی‌خورید. VPS هم که نیاز ندارید دیگه
اونور قضیه، هرمس به شما "کنترل" و "هزینه صفر(روی لوکال)" میده که اون هم ارزشمنده برای قشر عظیمی</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5445" target="_blank">📅 16:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5444">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بچه‌ها ما قراره استریم داشته باشیم راجب دانشگاه و انتخاب رشته
اگر سؤالی دارید، می‌تونید به ایمیل matinsdungeon@gmail.com سؤالتون رو بفرستید با Subject استریم
روی استریم می‌خونیم سؤالاتتون و جواب می‌دیم با مهمونای گل</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5444" target="_blank">📅 14:54 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5443">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ld5T6BoqroThFIEuibERMm1cJnarQpUhFDe_0FELV_5BSYgiDjqFsJwIvraeoc62m-O8fx0lbOJbtXj2uyL3h34jmjyJsJ5z2oI3isc1Q2Cz41AOLRtUcTjYG7e2kB0VRqAICtuhpQjkvRp2GN-6OFQx41sXq4R2MUN8RVxcMrAFRl5pRksj65jIyB7ELMhpOIn8xpm42ZgJm0jT2cqP2qpqivJHjh5XFXyZPoSwvO-9sg4Ll9XMcbCurfaxa-9s1ade96zBhXqQf2IDPCmbH1aI5bGj0_ruPMCYzBup-a9qi5kKVqzWsh2vmA4R7GHMZvUm2o7Pgf2H2cNncC1rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکاری رسمی OpenAI با پلتفرم Hermes
در اعلامیه‌ای جدید، همکاری رسمی OpenAI با اکوسیستم ایجنت هوشمند Hermes(Nous Research) تأیید شده است تا قابلیت‌های مدل‌های جدید و ابزارهای کدکس به شکلی منسجم‌تر در اختیار کاربران و توسعه‌دهندگان این پلتفرم قرار گیرد.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5443" target="_blank">📅 14:44 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5442">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بچه‌ها پدی 2500 دلار کردیت OpenAI داره که میخواد باهاش یه اپ بنویسه به انتخاب شما
رأی من زمین بازی سیستم دیزاینه
😂
❤️</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/MatinSenPaii/5442" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5441">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/5441" target="_blank">📅 14:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5439">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s4YtyFVdpHKGq1p3lNR09XoWyd7n9F1oDEQbv6sBmLIKqHvpNyuyyJkw4lYQkvLs4O3SCr6AQ2rb5Nwi8KWaYhMu-AnN9x-fRV6CzE9dCtnoI8KEFiqtLl03_900eAifDwsMTYPcin5cIor6pDxRxcN9XC7_IOkSs5fz8R3gZq2dGkr9MOvM7lYLYImBJ5-HYJSIBioVN8-AkTQsJylfwkyrnjsU1V44qGMj5Zlg5hkk4bQkH33RT-PgZGtyHnlusIq2OwwzvBztbBb7tL2_Kt5mZlTFxlVIDkkBlYz4D8f-HpdkMIsJAbveVKzqWmGkY2qwSYikWyhm_lHMYkqgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qqYC6NDIYYwZwF5GUcvTbelcoLUlqa70U84yHD-2sPshMljsWBOlxV37E3-oahqVr1zK05umA6lgDbalaiiiR3Qnp9BoPKfcJpJvD9xXwAT5aVSnPPi2oXyE0deo_QORYqM9b_sbhf-N83xc07L4xicYSnpboS6AYGt2xbRdUOgxlWiV85pOQ2uk_8B2XNMsx2bzrjJthqZUhhmlLr6bHF2ycHKvHIrJzpNLNwwXJBGMOsLc_Z-Wo3hWNCCjh9YF5MPMHyy92r1skK3lMB4WniUjZLM3_GbyMnUhCLSwypWVN-cgIUP8oI45V_R-jFVQpzkAzcfF7hdcdL1LdkWSqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبلا برای این کار شاید 20 دقیقه زمان می‌ذاشتیم.
پیشرفت ai واقعا عالیه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5439" target="_blank">📅 14:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ll7qMLMfG-pZNKeTMwNttYY_52HLZrmuepSB4S3YCCQSmtyFEM_LF07ohDf5J7LrIGUcbWNzkriafmdkT4T6lB_Wwb2k3O6pXNVURX_loPGdUxCQnUeUk8ATftvxhaMXYIhlmUqBm0VKCfBlnGizwZ_x-QiaTQoKsmAoR95zR16trWpUjJAXtbddHUEnxBkPqNBIIRhnCIHGE8nkyHy3Ow3EdOPGI4aqBKaULCp77B5RprK1DBk_CXXVrt4xPI1a59CDRNv7BfBRh_kNZ9H-0R6ZUh4Ws-aIa7_WuJPg0Eq32sw8sWliu-2HgszvzFr14NGoSulo3k3MwW7z7rcX-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mP3J0rvr7-pMaD8AHBPs6dD3TjunkJmx3F8bSfFomkkyyDCy7LQaw50D8OCq0BX9oAhRiE_bNrp1mqfM_v95MgCwSJ1XGme38Jn9bT0dQ14b3vjiitAHHIzg1-BfM9kSjB5_BMBAr75ei7d4FNnwNl__zEZy9Tvc8C0rkwc-ILwc_LghUPwPE5MV00XdajoCGYCZ5eXbZvlt8YNJ70bIe3miVZqIa3jOxFSw3ioMw6-OwzrCUj4jZIHOzLv-wnMFXtQSm-9BPIV8Hpa-VZisnCE7L1mAKCT-wYlLGxJmiB7zAGx2Y-Lv3rWPW0GNrjqYrTRv_vCcpYxlgF6domQ88Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز Manus پلتفرم Cues رو رونمایی کرد
چند ساعت بعدش، OpenAI از Dots
و طراحی بصری ساب ایجنت‌های بامزشون خیلی شبیه هم دیگه‌ست
😂
نمیدونم چه توطئه‌ای در کاره</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/MatinSenPaii/5437" target="_blank">📅 12:41 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5436">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گویا همه روی GPT 6.1 Sol مصرف توکن کمتر + قدرت بیشتر تجربه کردن</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/MatinSenPaii/5436" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5435">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عرضه نسخه ابری OpenAI Codex در رویداد DevDay
اوپن‌ای‌آی بالاخره بعد از شیشصد سال که رقیبش آنتروپیک این قابلیت رو آورده بود، توی رویداد DevDay بالاخره مدل Codex رو به فضای ابری آورد تا توسعه‌دهنده‌ها محدود به اجرای محلی روی سیستم خودشون نباشن و بتونن از راه دور با گوشی یا هر دستگاه دیگه‌ای ازش استفاده کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5435" target="_blank">📅 10:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5434">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=PNkqBLz39rNtRP8uL1F0e3_ztdbfad-LEgsOQtkknX7EcnCg5tXCjrOYUlzdD5-N9rVyM1u04WZgtwduFUvzPyNxNqyieq98kV8tZKa6wZmba2YVOGjoVgBIpPb3iqJlJ_MoeTGkNvmSK-nX_ETkLd4JxL544Sf00--kzHIYzqXEi6mFL-tN3x9l_AZZ2_jng6KCRAErpTjucfETxwCoDnyl1h140mKNViN8n6glZzmqP5NE6sutUVaj_TEPAPNvFRgGHmeVzg61T88XVznr6RqqF8hfaC19qcqCvDvsEyBDH3f_qyTjuytGNlTKvqNARXVP6QLfFDVEwGmagrhrCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd71a513a3.webm?token=PNkqBLz39rNtRP8uL1F0e3_ztdbfad-LEgsOQtkknX7EcnCg5tXCjrOYUlzdD5-N9rVyM1u04WZgtwduFUvzPyNxNqyieq98kV8tZKa6wZmba2YVOGjoVgBIpPb3iqJlJ_MoeTGkNvmSK-nX_ETkLd4JxL544Sf00--kzHIYzqXEi6mFL-tN3x9l_AZZ2_jng6KCRAErpTjucfETxwCoDnyl1h140mKNViN8n6glZzmqP5NE6sutUVaj_TEPAPNvFRgGHmeVzg61T88XVznr6RqqF8hfaC19qcqCvDvsEyBDH3f_qyTjuytGNlTKvqNARXVP6QLfFDVEwGmagrhrCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5434" target="_blank">📅 08:12 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5433">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">حس می‌کنم یه رقابت خیلی سخت بین سرعت ریلیز مدلهای جدید AI و بالا رفتن قیمت دلار شکل گرفته</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5433" target="_blank">📅 08:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5432">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5432" target="_blank">📅 00:49 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5431">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مدل Ember-1 از Fireworks: کارایی Kimi K3 با 40% توکن کمتر
تیم تحقیقاتی Fireworks مدل استدلالی Ember-1 رو بر پایه‌ی Kimi K3 منتشر کرد. تمرکز اصلی روی حل مشکل بزرگ مدل‌های reasoning بوده: تکرار بیش‌ازحد مسیر فکر توی خروجی که گاهی بخش اعظم هزینه‌ی توکن‌ها رو می‌بلعید.
چیزی که من خودمم توی ویدئوی کلاد رایگان، سر اون بازی سه بعدی تجربه‌اش کردم و واقعا افتضاح بود. مدل توی thinking خودش گیر میکرد ده‌ها دقیقه.
امبر با بیش از ۵۰ آزمایش و ۲۰۰ ارزیابی جوری آموزش دیده که شاخه‌های غیرضروری استدلال رو حذف کنه و بدون افت کیفیت و دقت کدنویسی، همون نتایج بنچمارک‌ها رو با حدود ۴۰ درصد توکن کمتر تحویل بده.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5431" target="_blank">📅 00:43 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5430">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن به اسم Dots تقریبا شبیه Muse، یا Grok Bot https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5430" target="_blank">📅 22:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5429">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خب انگار یه چیز دیگه هم دادن
به اسم Dots
تقریبا شبیه Muse، یا Grok Bot
https://x.com/OpenAI/status/2104984504133918973</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5429" target="_blank">📅 22:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5428">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5428" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5426">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GIE5tttoLLx1ruToxti6rYbS4HOkiRFJTM0YKsVZfnbkMTLmED4XJY8RVtuzz6xtmJk_Jq3vZFqf1y-_3kQDg0McDtsD1QCsFZDjlfTxL5E4DJ4GErKyqovvZZ0-tAYncmA4s1qvtn_gQeCdEpX927h7ALPJ_NWgR-DHLrP7kz4QVmvg_mK_dG28m33T6P3jPep7H4aj5plFD3H_cWHuVbJVMQY2nO9VAGvwABdPt0ENrkG9y7Uiw3TgzjAqtC8pw46CPmsA4AmIWWjp7eHK3_4h8SF3FpzGJXPcYRH2mMzh4fPeOTD-MqHrJFGzJoCA3xy2-u8UoSVbdfo10x9BJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vqrmE8AtgFJl8xfRfYCgYQZhw5rQpr-sGHABL5zP-QOoZnP18OzFa250rwxqMaVOsQwKdiC2gcCdEI6nY7AWp9W89XiQrVEWKeTKocRZK7zvWcIGBvgl7H4J8bRZnrvuq6oI3rnl_4yQkhDJaaDAnNlv1jksc_WYkvCxqIt8wH51nbJ4mAJXjbkyXejg_8sdQfxxurOLuVCLVfvzjqq-vRXHjuoDrM4Yrw7skehFyNTriYGQiBI-Rq4wTdel84bnkXVJvl-WbWyfZAywrqAgqarTgMRKuSrB3aIXaCZQzjzrXwleYMVyvp5iEA5RaJFeo0tmIpQyPWFr5OhKVoZkiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلی ارتقاش دادم از دیروز که الان داره با یه مدل خیلی ارزون، کارایی انجام میده که Astra نتونسته بود. یه پنل تحت وب نوشتم براش که اینونتوری رو ببینم، یه مدل سوپروایزر براش گذاشتم که بالای سر پلنر باشه و تصمیماتش رو هدایت کنه، بهش حمله کردن و دفاع کردن مقابل…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5426" target="_blank">📅 19:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5425">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5425" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5424">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ایده بیزنس: یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال" قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط بعدش از…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5424" target="_blank">📅 17:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5423">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ایده بیزنس:
یه سایت بزن و یه ارز الکی بیار به اسم "طلای دیجیتال"
قیمتش رو با طلا بالا پایین کن، خالی فروشی کن، و از کارمزدا پول در بیار
هروقت هم سودت کم شد یا قیمت زیاد نوسان داشت، برداشت رو ببند و با تاخیر برداشتا رو تایید کن و خودت سود کن این وسط
بعدش از سودت برای تبلیغات توی کل شهر استفاده کن و دوباره پول در بیار
سرمایه‌ات که رفت بالا و بالاتر و مردم اعتماد کردن، یهو پول رو بردار و دفترات رو هم جمع کن و فرار کن، همه چیز رو هم بنداز گردن بانک مرکزی و فرار کن د برو که رفتیم</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5423" target="_blank">📅 17:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5422">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در مورد آزمون تورینگ و مقاله‌ی Computing Machinery and Intelligence سرچ کنید و بخونید. جالبه. با اینکه انتقادهای بسیاری بهش وارده که دوست دارم یه روز بشینیم با هم صحبت کنیم راجبش
و دقیقا پرسشیه که اوایل سریال West world مطرح میشه.
"If you can't say I'm human or robot, does it even matter anymore to ask this?"</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5422" target="_blank">📅 15:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5421">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یه جورایی حس مور مور میده ویدئو
از شدت پیشرفت علم کامپیوتر، اینترنت، ai و...</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5421" target="_blank">📅 14:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5420">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5420" target="_blank">📅 13:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5419">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5419" target="_blank">📅 12:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/imPP1zV2Sz5bcckYUw_8873ae6flMk-C70sqLLU4bpO0biqPDzlMF-EgMHOIAVoxAc_pNqTJZtIfKipKDAW8xsXMpDfIGi4TDmxTU5DcYajiya8kn3SrGsqc3z6X78V4Nw8uKgtXFupej83ILgn9khEQBnq6XyigAC2wTyGyf62je1u0ib9o6NFJG6hHJ1hjm651xJLuFDrZU4BKTxnDUXUYd_h0aaKWXO0pJosSgLkt6T139fqzBjPHjDxQM-Bf8Oz_PaOFASD2MNXux0poihDlfFIHUMI1OJEoDGM0CMjqlgfItSitIYAmxuooQgrXNlVajbrKvvF4imdSPvIaPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GGJz99B1oYjHaVShZfaesHtbDpgGei3fsnmN3zn5zUIpw26EdDHRpEryPrBrCgp2QYc9uO2h2foPqH47tyrwSavrT1PGQIORZk814ZcJcHr2WrpgD48IBnM_CwYgNzpnP9hxEq0AWZy1Fv8UBQD2bRTKXB86GFS0eOCGPHmlo095R-POnqPfax29VuYQTmluw66JAj4iUU_s9E7wQk_69YWHu-tn-igt3ZD_pC7Pdzr5hiVuEm9qGEOcxPXTYgcYVUCNUxYT5aL8TfKKuJ9IImzYwxWRP1ugyOgMx2ob2grvBDf-wHgkKUYPZ2o9HhDetl3Yz9ttKPjH2VQOi-s36A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با این نسخه از WhiteVPN می‌تونید مشکل فیلترینگ ورکر رو دور بزنید</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/MatinSenPaii/5417" target="_blank">📅 10:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.10-arm64-v8a.apk</div>
  <div class="tg-doc-extra">38.9 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5414" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/MatinSenPaii/5414" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5413">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/MatinSenPaii/5413" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AFfQJrLVwx7fYRwK-m35SzIqAmBV19R_cXsqCqELqQft18xEFmJFP3T8302x3e8lklPuJI6HmSvapf6KAO56HFX7FxcD2RKsWKopn_xZZS5DVAqdKsNhysIc_v-HU9jmmh0ELaUGQ46bJ2g_EbMtveu43sR-NWNLg47z9d37_Z01jZnJBE_nUh94rJF5fxGfNMkhaNhXXOIGCE00Dov0u3FYzy5S7NdLGRIqvMNdtMYdy6bVlB9l8ocyPodfw4xXWSbgLyReZLDyaiHMcCj8v-_R9Sg_QiwnBUr7MiqMez0sZ9kDf0rORN_qd5oXzPu4zEKhVxGHCbNfftob5l2d2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10
اسکیل برتر OpenCode
جامعه کاربری OpenCode فهرستی از ۱۰ ریپوی برتر Skillها برای ایجنت‌های کدنویسی جمع کردن که شامل پکیج‌های اتوماسیون تست، دیباگ خودکار و سینک شدن با دیتابیس که کار روزمره دولوپرها رو خیلی سریع‌تر و روون‌تر می‌کنه.
(حواستون به SuperPowers باشه که خیلی توکن می‌بره)
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/MatinSenPaii/5412" target="_blank">📅 07:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">Matin SenPai
pinned «
اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید: https://youtu.be/dQKfkXnThCE  به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/5411" target="_blank">📅 03:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5410">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OozN1wJP9gGfcfLMGwufd_u8ZjBS5q7fkQZWiqLhHEvHcwHIyzrBs6a7zGHUkRPk_xXusdlP2HQM0E4qcQKZtVgDeQvDZCkKYkpUivoimyPvLmwHZbU6zyGltXlK13TidrioEv6pKklCGLbuQA3VPpFAYNyOXbK_RnAiIbY05EevkeqyRziFO8UfhUJGyTXFgrbR15QrYUBhqO5gBA1r8dIcoZd73ZWlcl6Iya5eHyM2iTqG4fxdYHZ3vKHLtKNjAIuU_duTLzOqB-FFVTS3c6ZvUGf-8PnKQ9ZvgiHJfhUPiB3F3nW_frZdfAfJ-DyRhXBEBl5cNRQ7DQkagKR3FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5410" target="_blank">📅 03:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5409">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H1OcSSZyF0P3HrZpO7LgZR8C8Jxs3A5LQ6kXY51saLFZ3pmou7jD--meqAw951s1s8LcMvBQugXCIblgUP-TjH2TPscqMbWoin4IkYHiGd_HV0y06lWNrkgz1CY28R9itpIPARI8xaZr0VHMyDTUvC-zTgFkaPKgG6k_fZRU8rrZwX-cALbr90NGT2dz0uxHuCd5VFNWEtD41yxwgJoXhGnWMn9MTaWLRBerWLF_n9xbe1DflHK0IvnV--a7-SADLHDnep4KIfWrp1y3JzCabBO67o6dWptzeT-rnYN6-5t9yt48W8gsVzMMwezRvfONRkLYaAk3mh7BZ-fcBog7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قسمت ویم واقعا بامزست
https://v1m.ir/compare</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/5409" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5408">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هرمس خوبیش اینه که سمجه. اگر از ترکیب هرمس + مدل رایگان(مثل mimo) استفاده کنید، واقعا غصه‌ی توکن سوزی یا انجام کارهای سختتون رو ندارید</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5408" target="_blank">📅 23:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5407">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مدل Claude Sonnet 5.5 معرفی شد. هم قیمت با GPT-6 Sol، اما به شدت قدرتمندتر! نزدیک به Opus 5.5  • $2/M input • $10/M output • $0.20/M cache reads 1M context + 128K max output
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5407" target="_blank">📅 23:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5405">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oviXf7maqdBU4l3Ep2oMPzdLADVWpVVvcN6oOh5oAnX5DMQtyeBAoSCH6y8bXXVbbe5I_bAHNf_8bt4rT5VfFVsLFPMIX-iyFih89I0HXT8jRoc4Ie9uSmBhPUfzBoIL0lQNbztQ9_YiVwvRVZh5rF2J_V9qIwYezFucxKP89Y1zQOT5YrsNlprxGx-Xmmh-BctX80sFZeG7Ckl3N_SAHhiISccqTuLDH9ZqrR45RYPV6f6uvYi_4N0Na2nnzucK_Y8sLx7GfIQ62UR4rT0jm7fUDCgi2dGe9QgwhZPaeMh4pzBawaosxfFYqpm3b8eL-A2bDX6iGwE-1jWT17e8VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ufvpDydQCG7TRp3QrFnNcY9SJWTPEzmS49F3o1JXlCUShoVBbbpkF1FMJ9yYCB5mmKVj1KKUb2pJHe4QjQEtF_FYYF87UW_Ny6PyDkwGaeT8rOauqLENeJSbEhN1yPfuMJ1cz5NAaCN5ftYLWNOOlmvbBefwaTYnySeBj4xFwXU_4h-kB9PNmzXEg0Vg1jAo_HJEL43h4l5I2fKIgZMgbXQ1xPtGFtuTFCgsJyLQyphQxuPkJdjab_pWHrJriLbzKAk5MN5X3v_S26EFJKtETr38y2PUE3Kz4e9i1R0H0bkEOHDssDtsgM3OtjljysIRPuFxluZe2rASOIUCwPU9pQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5405" target="_blank">📅 22:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5404">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5  از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.  هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید. https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5404" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5403">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82410567b8.mp4?token=qVO7e7JopGR3m1vX2zkEs3S5yE_MKtv-qjWAMXDZzyXfeyzqDbVb-W0ZNue178f8yyYbewnkWWi9bO9_uQaKAkvSleZDV49wyvVnfDRX-AiWsC2DkhCoExMRmcRVzrADpgUxXa0hpwFbfQ-vjKSZ-FNMZyDQstT5riUwY_pG-UefOVseAwvF5mTyY6C1zbM0FfNrznwulDoWCarZ7fw_M6tMHuUUruk4fKuYoRd7MFnyLd4IyrLCTvNBKaYPGc-5g9FOK4oWYZD49qYD6fBBq0QGh_6gFYdSHs37QpJGl7tg2cTvPSHX5St_GyD7QZj3wxY7v0IjlaO1BeNmdWGREw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82410567b8.mp4?token=qVO7e7JopGR3m1vX2zkEs3S5yE_MKtv-qjWAMXDZzyXfeyzqDbVb-W0ZNue178f8yyYbewnkWWi9bO9_uQaKAkvSleZDV49wyvVnfDRX-AiWsC2DkhCoExMRmcRVzrADpgUxXa0hpwFbfQ-vjKSZ-FNMZyDQstT5riUwY_pG-UefOVseAwvF5mTyY6C1zbM0FfNrznwulDoWCarZ7fw_M6tMHuUUruk4fKuYoRd7MFnyLd4IyrLCTvNBKaYPGc-5g9FOK4oWYZD49qYD6fBBq0QGh_6gFYdSHs37QpJGl7tg2cTvPSHX5St_GyD7QZj3wxY7v0IjlaO1BeNmdWGREw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">389 تا ویدئوی ساخته‌شده با Opus 5.5
از موشن‌گرافیک و ویدیوهای توضیحی گرفته تا صحنه‌های ۳D و بازی.
هم ویدیو اصلی و هم ریمیک رو می‌تونید کنار هم ببینید، پرامپت‌ها رو هم مستقیم کپی کنید.
https://skillry.dev/ai-videos/opus-5-5
✍️
ai_ba_reza</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5403" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5402">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اگر کانفیگ‌های کلودفلرتون از کار افتاده، با این روش می‌تونید دوباره زنده‌اش کنید:
https://youtu.be/dQKfkXnThCE
به زودی یه ویدئوی آپدیت سعی میکنم واسه اش ضبط کنم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5402" target="_blank">📅 19:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5401">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRXu_KBNBepXZOHk5diJeM9ta94QM5KlE_wXowEXGU4f8wl2S-Wvxh42sCALqyPLJO0MiEJT-NqqfMMwRMaUqtMMzHGH29IiaXZAwbHX1aQbgbFi2IX_zg6E-zjjgwxwzR0mUmRSL4dgeAxUSjWcD4bPZ2_eL9m5vIlLRFKHVlt4Xdl3nDPuDVRYAcg6BdZQU7bBhvNqcDBJvEbMToizBYeNASQ9ZLs0d9ohWmTM-n6L7MeKTe8BR8gam83piebyMuo--eCYcvYjx2A7byHUbKqa6Kh02FcrM5YgvFQfjoW_OgEU5d61AXdjIT3EwpfuvfQF0rv-Yghn3Rlt1ccruw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5401" target="_blank">📅 19:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5400">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yr6wqoYI8oJOGQcWx3ErshTyEA776RHiFJbkrOSObXo24JIrz0ZmulygohHYcXp3d8lwFiBPQuX1DRsXCx61m2lcaHJhyWFzlaBUfjyX3CNojj1yTdBRm3WzzBFVlZioHcVN8Q7K6wjcAnpXxHoP5IA98I-gyoxRQ153kcoskPieq2J2pd5zQCGq7-5utxvzPN1D0bBQZqa0bOMAxFJGWgg_h8_KUU_tkkgueo1Or-PzWNmLurIlgUTlmGcSWc0s7YRgkWvNohXoH374zoPjPAFO3t5K6VOdd5x8aKKJpyHpSqffUBQEFL0uToAp4sVCxVlQ8qYMVQ3XI7xp1zYGqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر کنم گوگل چند صد میلیارد توکن از نسخه 4.6 ساننت و اوپوس خریده برای Antigravity و نمیدونه باید باهاش چیکار کنه
😂
مشتی 5.5 اومد 6 هم به زودی میاد ولمون کن دیگه</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/MatinSenPaii/5400" target="_blank">📅 18:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5399">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ik6IDVFwQc-7qZ_3XhtOhJ_iJ6a-XnGQsH2rTxjfVIXNz6gx5LmaC-IG0Att_oh5bwd-sSREXAWJd7EpVaEG996VFwyTvEoH_B5gpRE4VwPGe_6k_GW31d47FnaAxNlznmnEi85HK4hGNsaTfyiwLSRVbynFb2FJsdmKcY_EDb2ljfzanGZsT6dYHEHYNxmZNhGFqrVhUbOfzSbSgiLc1nmYsApPzA0FWYzeL9l9SZFf32tcHPhxh5ZL4EdQ-RMJ_y08zdjzLhznm5LCCyLrNmKyYRFlrZ_gAvi8LH5PFqaVmuY2WEd1m8J4raev6uk85_QmuhycDA2KbhGtq4BIhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی ساخت نرم‌افزار رو آسون کرد، دیده شدن رو سخت‌تر
قبل از AI برای ساختن به توسعه‌دهنده نیاز بود؛ حالا آدم‌های بیشتری همون چیز رو راحت می‌سازن. ولی تعداد کسایی که حاضرن پول بدن، یهو چند برابر نشده. نتیجه: وقتی ساختن برای همه ارزون می‌شه، مزیت واقعی از ساختن می‌ره سمت توزیع، ایده و شناخت مشتری.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5399" target="_blank">📅 17:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5397">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GW_F8P3NnIQalrrI_3XHiTJcv9TG_MYwNHM_MnuwC5HNOzUSw7vX3hxpbw3aGegob3znaAYqQAzbNGFNjk2zsB_KE3USWX7gnuCeLt7Ml30jCpMB0U_qOgg72PBYIkdxGi_dz5EA9cWv7tybxw0vFUPumIDen7Q_T5QazuxF6KZurJJ23lu1Ksa-1yalK0Vlsu22CWEJ218B_9ch6nykDk9a6k8t980xlvgIzlbjL8Bvs31eEvDNXaJY3_B3IWGq_F0mzofcRNsSF4YOTaYwmo6C1j7w91p5Z-ID_jkiNJyCYuRrtB7QOjJsxz6Y4gJstOqwncZ1gf6rewKyMLme2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/MatinSenPaii/5397" target="_blank">📅 17:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5396">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">طبق لیک‌ها و یه آیدی تست، امروز و فردا قراره Sonnet 5.5 منتشر بشه و گفتن که از GPT 6 Sol که سر تره، و نزدیک به GPT 6 Astra هست
با همون قیمت Sonnet
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5396" target="_blank">📅 16:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5395">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/MatinSenPaii/5395" target="_blank">📅 16:04 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5394">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/erl1mMwmkV3fRt69r8KImXT2FQkd-ZMODYpyozqGGxRiiDqRcyBjt0Xxx3RgYub5MkaEidOrkwr1TatjS1hsxUqRF9afGUKHLzhnfcSF-zeVwg8aZO5cnKqu_JCWhGyVO0g13DX485gS0NXQkkhPD-TFDvq-algHynzvXADaBhbpm9L0SMeX0tY9zUePR2AcSEeDxd1gKppLYdmBYUKVw1Eq7yYADKfZvNGq7_5-A5Egz9UlJzS_Q67r6JFJk9oIyUu9VZYrka7x-XNh5m9E5ms22s5N1EjQcViGqEmI-QNPvqEm9emFTnc2PrbiaiKuLumXFuay6B3uxSU9-jwEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتیم توی ویت لیست اپ Muse متا ببینم این چیه که همه ازش تعریف می‌کنن</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5394" target="_blank">📅 15:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5393">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqiozol0Zp2hONKgL1EMHedsTs9CvK-iz4SOW4p8jAqjcaQVis6_mKwnWxPGNcwBrURaf9DU5eAyDElySNbqaSlNRf4o6cnDHRKNpFg27gw2cZjnWqjrZLBaPbQGkkmTyafsiD418ZfWM-W8Jd5yfuj__oaxuOMg89dXNL1963D8guBY6HXDgcWenD1Y_rCrNAv96eO8vNl7djmXZPSvRFtW8fVnooBqr8r1V_ExE5CINq85gPMY7S1Fj484vf2vHRX8WaAkLCtjgylcrqQEt5uaTOSSDMi5FPWVq7iPo_iUbis2969JmwWOsLC4EDXtSCkbJ-7hlPWhkVYqzmTzIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنچمارک خسته‌کننده نمی‌خواید؟ بشینید جنگ مدلها رو ببینید
🤣
سایت TinyAIArena یه صفحه‌ی ۸×۸ هست که چهار مدل توش دارن واقعی با هم می‌جنگن؛ نه یه جدول امتیاز خشک و خالی. روی هر مچ کلیک کنی می‌تونی تماشاشون کنی و ببینی بالاخره کدوم‌شون باهوش‌تره. کل پروژه هم روی GitHub عمومیه. البته این صرفا سرگرمیه و جدی نیست، اما همچنان برای دیدن اینکه مدل‌ها توی یه محیط محدود چیکار می‌کنن بامزست.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5393" target="_blank">📅 07:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5392">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">قضیه‌ی «انسان در حلقه» خودش داره از دور خارج میشه
مارگارت مچل و همکاراش توی یه مقاله استدلال می‌کنن که راه‌حل «انسان رو نگه داریم وسط کار» توی عصر AI، اون‌قدرها هم ساده نیست:
هم طراحی فعلی ایجنت‌ها نظارت مؤثر رو سخت می‌کنه، هم استفاده‌ی طولانی مدت از همین ابزارها، توانایی‌های شناختی خودِ ناظر انسانی رو هم کم‌کم از کار می‌اندازه. پیشنهادشون اینه که نیازهای ناظر رو به‌اندازه‌ی توانایی خودِ ایجنت جدی بگیریم؛ تا هم توی طراحی محصول و هم قضاوت انتقادی تمرین کنه، و هم توی سازمان‌ها با پروتکل‌هایی که اثر اتوماسیون رو جبران کنن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5392" target="_blank">📅 23:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5391">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">بعد از ماه‌ها که برای کلاینتم آپدیتی ندادم این مدت روش کار کردم و کاملا بهینه و بهبود یافته. UI/UX  کاملا بازنویسی شده با متریال گوگل. و خیلی فیچر های شخصی سازی داره بخش "رابط کاربری" از تمام هسته های حال حاضر پشتیبانی می‌کنه راحت میتونید کانفیگ هاشو اد کنید،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/MatinSenPaii/5391" target="_blank">📅 23:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5390">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سندباکس‌های ابری Docker برای ایجنت‌های کدنویسی
داکر سرویس Cloud Sandboxes رو منتشر کرده: محیط‌های اجرای امن و میزبانی‌شده روی زیرساخت خودش، با ایزوله‌سازی microVM توی سطح سخت‌افزار. با یه دستور میشه سندباکس رو بین لپ‌تاپ و سرور جابه‌جا کنیم طوری که فایل‌سیستمش هم منتقل بشه؛ یعنی کار رو محلی شروع کنیم و قبل از خاموش کردن لپ‌تاپ بسپاریمش به کلود. هدف، ایجنت‌هاییه که ساعت‌ها کار می‌کنن و می‌خوایم چندتاشون موازی پیش برن.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/5390" target="_blank">📅 22:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5389">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5389" target="_blank">📅 16:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5388">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvOknRaGVGHAnq6ev3sV74gjWewqIrjaGk-HFTT7OM2bJBCNa4lJVtzMNVIVDYXqlKiqAp-DFxfdFAoT0heM__Q_IbG4tM4s6XWQyJypPTfluM3WULd35dFiRIKem6XeLh2mOiByg8AGYnprKS_og_zpl1lNLcOKg5wH0bsfcMgTsdhF9jPGbQdEjE70AnrsDPBYFbpk-U9mOijejndMRv2I6DqyGPoJk4S6_-EMDYfY4K5HTNnc7ev_xGTzE9bAoqK_bDobYWAxs_tGdxqR9dqV_OKsSfOonDFt4gnwiRHPp4trpjsMqQD9DAs-OUJil28dU7cDkGCyfcj1-Nxbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر بلاگش رو از WordPress کوچ داد به EmDash
کلودفلر جزئیات کوچ دادن بلاگ اصلی‌ش از WordPress به EmDash — سیستم مدیریت محتوای متن‌بازی که خودش داخلی ساخته — رو منتشر کرده. EmDash با TypeScript نوشته شده، روی Worker خود کلودفلر اجرا می‌شه و تا ۷۰۰۰ درخواست در ثانیه تست شده، در حالی که بلاگ معمولا ۷۵ درخواست در ثانیه داره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5388" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5387">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dNWP3hkqVvc1icx6boRPmRupZ3LAXIz6-KU7X7UjDzw1xjRTAp-CKBUfU3iuUu7dyAk4kMMoDauESPRHnfykWGVybwkUvF3npXvs0mYKWCeZF1w9wre4N5sWaMcHgn4gYSu2Vz54DD2XdbzVy_tz79OQA527r6poiYAQjMHFwh31Bs6d1ya7thH6R2Two7YLSWBLd5Ew0A6ZuS9ZpwvuyQrqtxGOlJPM5NmbgM5U5V7CmXPcjr9Muc3EzcugwYDJc5yvTsFWDh2o-khlSOnHv0OPtekYxYgP08TvweTIIfnU6evZaBEQZq-prHVeLCRS_pTeIZ-CGNO69v2rgfH36Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/MatinSenPaii/5387" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5386">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8eFHrCZklQ2gFSfMdh-zlPv1tP3NModAuujXZeGbWhX4Z6CGMVQxMsoXYg9WlG8FzhqD6QngKJll6joogh76r7AWAZTlgiQx7flwNDHRYKTpwRQqwsG-4AJZbDWf0ieF9n3ROLGx0VoRTVTCGNW2JCL_52Etp8XbOYsABsrLQg-_v6JPZdq_3DZCSOQcMxgp0lSbvEShgL3hR3ABBu8krpY1gI7jOaP7AtdEvbhiqivXAUedsBSmqW6BcUg7lp7m6BiDVhE7jSR3MirX43AZaqL2aTq5F3J_0rVIUfk8WIjNsPgzZdGHeeOcgWb0I75n3SpdzFZy5XL0gyAduCyBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ هزار دیتابیس Supabase داده‌های مردم رو لو داده
پژوهش شرکت UpGuard نشون داده حدود ۱۶ هزار دیتابیس میزبانی‌شده روی Supabase بخشی از داده‌های شخصی‌شون رو عمومی کرده: اسم، آدرس، شماره تلفن و گاهی پسورد و توکن.
و بین اینها دیتابیس یه کنسولگری دولتی توی فرانسه هست، پلاک هزاران خودروی یه پارکینگ، و دیتابیسی که برای دریافت رمز یک‌بارمصرف کلاهبرداری استفاده می‌شده. Supabase که امسال به ارزش ۱۰ میلیارد دلار رسیده می‌گه پروژه‌ها پیش‌فرض امنن و امنیت یه مسئولیت مشترکه.
بخشی از ماجرا هم کدهای Vibe Code شده هستن که بدون پیکربندی درست، داده‌های کاربر رو  لو دادن(شبیه یه بنده خدایی که یه بار پروژه اوپن سورس گذاشته بود با به به و چه چه و بعد دیدیم apiهاش توی کد فلاترش هاردکد شده. (طرف مخالف سرسخت ai بود و میگفت به کد ai نمیشه اعتماد کرد)).
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/5386" target="_blank">📅 11:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5385">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=AoHsb_qduVI-AwIzVaUhrMqEWk83zQj6c-Yx1HNNE1rZPPOai-QthQuSp1URDbPNqR62V-lDLgh1kAMopJWJuXCIxQdifDtRgym-iqpZzARv8lQz-0hjO6ujUM1UhWd5455kSAclmclIxoWHafOlxDcVOYQTjX6AcdMebZtFxId9all_YVET5XKuTVgVlohZA5x8UoorufWSiPhWLFY56FoLZVryfC6bc0sIyvNfvcrZITTWChD5O6l9fSSWf71NEc9ipk-q73p54GlA2N1qlxVzMz-jJv_oHxXiH4A180otuRptQNENBt8POmyZv7ovnmOWi-UdJq11uMvMQhYhiQFCLnkyjmuKf6hD4EK8nXjt3X0gczzVpn-W3k_YQYzWg1IbOPy27Fb59NNVhQCNzCiEh-Et4Hjgamm7kRNp3n8h4JtsRyq4Uztg2XaIP4YJEGK-RSsEPlc4rnSwtkomJz3BqnSJ6UregHcpKbVkeOQP966q-gltP5McdeI_QoScIkdWn-Y327l9rtc4O9KG-z8tQWfC68vmMsPufEOoVFOSsrqcPgB5ABaySiRsceRfCMaDbnVvXkBt0JWoJ-ifR4zpXAu-c0WF_DwBfYJVUN5hBAme32_MdwgnE6ghaLYH4JFbnjRu1xfe0gM3_mJ5YJ6pFm-RG9L7afO8rCjRxM4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e71f3ca5cb.mp4?token=AoHsb_qduVI-AwIzVaUhrMqEWk83zQj6c-Yx1HNNE1rZPPOai-QthQuSp1URDbPNqR62V-lDLgh1kAMopJWJuXCIxQdifDtRgym-iqpZzARv8lQz-0hjO6ujUM1UhWd5455kSAclmclIxoWHafOlxDcVOYQTjX6AcdMebZtFxId9all_YVET5XKuTVgVlohZA5x8UoorufWSiPhWLFY56FoLZVryfC6bc0sIyvNfvcrZITTWChD5O6l9fSSWf71NEc9ipk-q73p54GlA2N1qlxVzMz-jJv_oHxXiH4A180otuRptQNENBt8POmyZv7ovnmOWi-UdJq11uMvMQhYhiQFCLnkyjmuKf6hD4EK8nXjt3X0gczzVpn-W3k_YQYzWg1IbOPy27Fb59NNVhQCNzCiEh-Et4Hjgamm7kRNp3n8h4JtsRyq4Uztg2XaIP4YJEGK-RSsEPlc4rnSwtkomJz3BqnSJ6UregHcpKbVkeOQP966q-gltP5McdeI_QoScIkdWn-Y327l9rtc4O9KG-z8tQWfC68vmMsPufEOoVFOSsrqcPgB5ABaySiRsceRfCMaDbnVvXkBt0JWoJ-ifR4zpXAu-c0WF_DwBfYJVUN5hBAme32_MdwgnE6ghaLYH4JFbnjRu1xfe0gM3_mJ5YJ6pFm-RG9L7afO8rCjRxM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه. - عاااااشقش شدممم. با کدوم ابزار ساختیش؟ + الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/5385" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3y9yj6iCq9AVEb6ducggcHkcV4tmjDD3ACoBy6iPBD4Latlv3VXwq8Un7F2GIkkkYGSshX0vNV83Y2Ls9rTSyfo4CMY_wu9O2-F2w7N-j9zt_Ct0-cYiBXhluBxOs9B6KDllJ3TvVsAJ1A5gy4EjNbt_H5RPsrb04QfHC1OY_L0s91_Mf01vB7t6gNkHi5iE-gAafdP6I1Bupzf2pGGi3ogK8yeLU8eODoLUIiz5ftlREoYhGJBNbUmiCGJdsbbMEzEH6PdSZL1fHOPd3hPRTk49j2avQfo7NRBCkN5QU9xtVK3R_ZQ8uu2GrTcBQobkRMV2bef0VupVy4X7bZM1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+ متأسفم اما AI هیچوقت نمی‌تونه همچین چیزی بسازه.
- عاااااشقش شدممم. با کدوم ابزار ساختیش؟
+ الکی گفتم. با Opus 5.5 ساختمش
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5384" target="_blank">📅 09:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5383">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZx1tzoc3iiXW-WAEzpbhX_k1cUADatGwI6uHaJsiRhdX7TKpyo57BFzqtpjkrx8R9UWYEwAOjz8FVYGUNagEN2C66noIoC4o_QHNfjSdZxExgjgpYc0rpz0AjGdGY8CRkU1bBLZbMkS1E4awXYC9Tw5miTNH3QmPUlTB0o6oHJR0ygYZAEomLqztTifc1Ul3pqSDXXZBWSEuCF09gi3OgEiTHYpwMXJmcZmUR_Jc5kzYQap_DSNMZA7D_0ZKTQDnsWqAW-Psty-5cLhWFlqtJ8-3uj7XEGsQKIyRcOEBaTRQ6Tgsr50CIra5IFvjttKYPge7IlJZ1hwLM0IRhNcEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولایا (Ollaya)؛ مثل Ollama ولی برای مدل‌های تصمیم‌گیری
خود Ollama، اپلیکیشنیه برای اجرای مدل‌های Open Weight روی سیستم خودتون. حالا Ollaya، همون Decision Models که Jev ساخته رو می‌خواد لوکال و متن‌باز اجرا کنه: سوال تایپ‌شده از هر متن یا JSON میدی و جواب کالیبره‌شده رو توی چند میلی‌ثانیه می‌گیری. جواب از یه پاس روبه‌جلو میاد، نه از تولید توکن‌به‌توکن: حدود ۸ تا ۱۰ میلی‌ثانیه برای ۵ تا سؤال روی RTX 4090، در برابر ۲۳۶ تا ۲۷۶ میلی‌ثانیه‌ی API عمومی Jev. با API سازگار با TypeSafe کار می‌کنه، پس SDK رسمیش بدون تغییر وصل می‌شه و مدل‌ها هم همونطور که گفتم، open-weight هستن.
اما یه بحثی که وجود داره، API خود Jev انقدر ارزونه که فعلا من با اینهمه کار باهاش 5 دلارمو هنوز تموم نکردم. لوکال اجرا کردن لایا هم خوبه اما شاید بهترین گزینه نباشه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5383" target="_blank">📅 07:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5382">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UPpIqsOdo-M8Lf2kPtLE3XnZKlC2YrxDPxcEVV3YnJ261XrB3rgXSEcRmja1wXAlXVEF6Qa-ZuY55o6TWerJmIrnq-IUOdODjB6ayMzszONtliBnueCwfJlBYF0JunTI723ponDDvv6GUDjp-NeGEksHHDeu_vIfD1Pl3pe6uEVD3ALI_oacO4M9QGksncW3DDoV8Vj0kQJRYEtheQRJ1BtE2EZ8xVfStPZJ3ZRvIiCHX9vUT0GiGjOupKEFqIedDRhN7D55nT2wdBN2aQdBt0YnfH-JpnnL0J7OMfWrFK2u8XD0ws8LHgOTeIsJh0qSser0a9o5M1R8DWpfdZAcuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیک هست دوستان.
گوگل یهو ایران رو تحریم نکرد. سالهاست ما تحریمیم
گوگل امروز صرفا ۶۰ تا اکانت مرتبط با صداوسیما رو به دلیل فعالیت‌های فیشینگ سیاسی و پنهان کردن هویت مسدود کرده
این خبر هم اشتباهه
می‌تونید ایمیل بسازید همین الان با گوشیتون و نگران نباشید</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/MatinSenPaii/5382" target="_blank">📅 00:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5381">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تانل با دو سه تا یوزر و سرور قوی هر 40 ثانیه یه بار ریست میشه
معلوم نیست دارن چیکار میکنن
کلودفلر هم اکثرا کار نمیکنه واسم آیپیا با نت همراه. فیبر وضعیتش بهتره</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/5381" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5380">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وضعیت اینترنت خیلی افتضاح شده
هم نت هم VPNهای تانل</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5380" target="_blank">📅 00:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5379">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZQcBS3wy49Hn4_NzKuw37sD3SDeB3TU4A3fDc8E9qwhJaGFBdULhdTNIVvQIIPrAjkilpVf2TaBCtQZjha-FkCIhrBDTeQ24CJA9PG9PlCgYZfnle3XoSboagqRhCEGa7-w_p4E37VOyzoo3MAvQmli7_srsiWPdQedV3cUDgGjEk5czAyCDKOfiGqw9Oy7-JSziMxxlqe4LUdi-VnMaaMZGRHMxKqSVMUHOr2prMtwMNt7Zmwp8CcGG2mfeB5-eH_p-_NpSt6zQXnMaBGH-hc_kXN0TI56WIJCnMc_Ig7UkbPyNzLGOsg6zEwVb7QunpINoydhgUc_lfMlbz9Rgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رابطی رو که توصیف می‌کنید، ایجنت براتون می‌سازتش
گیت‌هاب توی اپ Copilot یه قابلیت به اسم canvases گذاشته: به زبان ساده توصیف می‌کنی چه رابطی می‌خوای و ایجنت یه سطح زنده برات می‌سازه که هم خودت می‌تونی استفاده‌اش کنی و آپدیتش کنی، هم خود ایجنت. هدفش اینه که وقت کمتری رو صرف تطبیق‌دادن با ابزارها بکنی و بیشتر کارت رو پیش ببری.
این کارا فایده نداره گیتهاب جان. پلن‌هات گرون و به درد نخورن
برو این دام بر مرغی دگر نِه
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/MatinSenPaii/5379" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5378">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dzx_9ZJo_vbPH7nnkwDm5cxckQPGLaasOEOsDvc2uDSe7rijzZz8zxiEClO0TgKJPJtj5R7bD-eBu07yw8kBMxSeJf1DL7XxVhf_hSGnsTSc5jaIhQKMDMPpWu2-Q18fLBWEjgP2RyPyqEaLBniMpsP5BHK65wbCKkcATAqBX2WgvvH2CCJzK06JSgs4W_Y3iv_jWK3mYr36AYzQKCjgLKQYGyWb4f9vfcSfMMBGsdc1p-d0UqFRqNbf5Wtd2Rae5EN8x8jkXTRyUd1qcfuALjc2s_gsm0iBAD5MX6t3-pkLkKW8mViYxyu6qcWX8YxL8h1pdciPCW8YEAhOy_F46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">(باید برم ببینم کپچا فارمش چطوری کار میکنه)</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5378" target="_blank">📅 23:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5377">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XNipRbN7C3fF3rWZwfVOXnuIIvYn-a-9bgDlriOm_mYa7cOQCqud2nmgySX4kLyQxP1sPU7m2hTEdMnqaND8rZsgnPL_N0IvLKsdZjln_zYuIylreIc-77O-gMDbkz7Butce0ZDPmRLzNDmyg2us9tl14HuuskcqrPjvMyfleVDT--DqZqXo6qQP5GLFjWmqfmZcMcv_Q8f1HqVSsuYh6PRufhT5UzjoQ6TGRz6H96gnU9PN0dvigegtRth3vHvdODuEAjhScjy_pcIrJeRCUgqcKIlsQO7yKYZaVZQgcEMTmT3P7ogwFGcOo8VAlWJp1PLxivdqzyj54oR92aofyQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5377" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5376">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این ویدیوی موشن‌گرافیک رو با مدل Opus 5.5 برای یکی از دوستان ساختم. و باید بگم با ۲ خط پرامپت و یه ویدیوی مرجع برای گرفتن اطلاعات و متن ویدیو عالی عمل کرد. عالی  حدود ۴۰ دقیقه زمان برد و دقیق ۲ خط پرامپت با چندتا فایل فونت.
✍️
Saeiid</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5376" target="_blank">📅 21:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5375">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=grC8mPRuvsxGbSplD7gAPwWmRVkOjkZi72J8htFjKjjiLmYQBSXPhczOHlMwCoQ6ZQtxWSW39hksSnSQQ3SjIP_a-kx8PDv9NXWoQInfs5i0UH1GgquUeI0YahCFmXfGqUMz-mb_UJY21XjNV9tmo_3oYy27OrxT_6YfgfOBAUgtVAXXfTX5ilQxfPggA25RUSEAb_eXARLWOOpNY2ZoGbVXoa4VBNLnmaoD84AHutvMMm91YKh05a2olKLWBE5bj9eoKdt5ZhQtDuuNTYtddZ1e3nsCcONLPA43WSzNXoproOOpD0RHxOsjfbhRSWBzQgOmAuW3b5EY9kaoiMFtxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6a18edb9ea.mp4?token=grC8mPRuvsxGbSplD7gAPwWmRVkOjkZi72J8htFjKjjiLmYQBSXPhczOHlMwCoQ6ZQtxWSW39hksSnSQQ3SjIP_a-kx8PDv9NXWoQInfs5i0UH1GgquUeI0YahCFmXfGqUMz-mb_UJY21XjNV9tmo_3oYy27OrxT_6YfgfOBAUgtVAXXfTX5ilQxfPggA25RUSEAb_eXARLWOOpNY2ZoGbVXoa4VBNLnmaoD84AHutvMMm91YKh05a2olKLWBE5bj9eoKdt5ZhQtDuuNTYtddZ1e3nsCcONLPA43WSzNXoproOOpD0RHxOsjfbhRSWBzQgOmAuW3b5EY9kaoiMFtxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/5375" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5371">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NF7TQxPJyH6ys90dOQo9ADlWWW117WWCmCz6Tx31SG1-RVq7lffitgWAimN3ZGadjsY5fzvacDAsTuehItdefEJORic2dcrepWEiVw_pBLSAGAs-XynpDugBYCTkdlF2T20oP8J1Almgf1T9ik5hTvA8Mvh_in2ByNlzEKBsKjZfEYfFHWeLpVVYZBtUEDo6XlWbrRqNEX9l2Czn29g4gfkbTwHukljlm9LBRaTANHxW4HgP68UQVf-KDibsaY-idzIc8BSBTS-eHhnX-285s5FNBQttEastf_vpxXaSA8_fUcYbeVq8bFHQ7DdF0huksfCNaI4G8V7fWykOeFZ2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lHCDVrwqtx42iIwLtl_frdyOSF4FiHX93ubgtxu_0y-8k6b6qW3ZeRWKondBUGWDsqN1PEk4RoMc-Y2_d6U1MRIXIcxVftDTEtgDd3POmttI6ziPCh7Upqv-SU_bTz-6AEFeDUSsjFpVc5KXL-IB-5nerhfvfwgpjFoXV001zXmTLpp4Cim7OcuYw5PL3L4OQxrJSGfQDvWKdrE4Kob9Lv1EOKOZx3KJXAmd3LfUO1pz-CuBB8Sq4_-AscS6_dJRCBsv0Ul8IGBucWPNuUcq-oX1mn3QySaaKFF-zG7L0HpBd7xVH3Srowe6K5cSCF3N3R10oVnzOjJAZ7vaohl4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GA_FHGQjMhBA6hxANC0Ruf8ohX6lj9_bGPllHMCX4-Xy5HooiH4qs9GeCeJXnHsg8GTC2qWcLnx0hUBSr3RiWSXr_k3hQqCkCrgi0Lpqku6fzUeSmVI0v_OKY4uZn-ajxd1RA3-JbhGc-LnIkKiRTh53rShS2o8GM6Q_GdZaBY8homrHLR6mEqK2c-sIxTTzVuBbP6hWfayS4eLLHbY_8ffIOINIj5QIlqHIdhk5bmbljQ4qjgiw0UV7DvyBrKqggzpL4Lg8BHDztHA3cX8fSadJhrU5MPGwHAI15xqd4oFAonXwdIEXd74ew28KtkG7ERlN50NtROXY7ZabRfHmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vnjUaSad3cCm_eOc6LMPVTBnUoQDunqaNw_RP4rIdn9Fqp-bvIrC37sIMqQAvkh-SR0sg9GX4Zi1wy-fIScpTB1ZuVRCMdJfnPyiCwh6mGxJAMZGRerGa3oB-U8uAw4U8zBW_k6qDc3U_JQExVGYQg7I8m6SSQdWW7f2t3yXZLqGczmDBhVO1TRiF3CwY209dtBqdMm_64pABWZTMu8T9yux1e6MKtdC-Svbv7ErYRXP_KkvBFjfYQI-_cRbofWSs1RNP13fWSVlgxSgZtkEgDWXLXFIRShD9iaEfd9CvYogkvVQbeXLZjzp1xL0HnmvOjzL1smiDYDOaLFf3XERvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5371" target="_blank">📅 19:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5370">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxzxU9RK6RxrP2ca0qjr0xlu2-4FNT6CWcXLEhF_5AdQP9pj3Nt85x3sWDMsQsPXScpcSS0quSaqATZ2pVxBiMZuheUQpexiHuC9aeXz02u_M3ts_IK_FdRr0m6aOHol7qk4vCyPwL5pJvDNREN_sYi2zxAtm97zkLaD6fnjBONTSldElAUTsew_NgA1tag4w0udWrNEf-2kxEgnaYGYf0mq4GeUcbqS6yLjtJw27U2p_BBkHI3NrECWy9op0zfXfTybD5X2yIqY1P1ypvN_gcvxiDi1C1uYBDJ9rBa1eBEXZmr4fCtLZTrKdtupw4yuB3t5G1Mi3n4Vtob3V9ryuj-I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d63885ad.mp4?token=ik_6wffYPWaU67CYG_ALEEJlAyPSgCpZRFTkPjeOs1U_3Y-Vp4zVC-Mfto8uTYhb6NpK-hDvXM0Xv2iPqItcdENeeJ4DqCO3MTmHWJt556ZWTguzloHyomuG_nCkDvCYoJwF5rtXo9vDMYuowLdis8t4T-5Tk9lvlfz-W-x1NYtyrZ0Rol-QCu4VmKHAOJnOEVYXhUZbUk1sWQmthgbAp7YVnz-SWwe0RM4WBx2w6-knjKrmOr6LK5T7kZi5PzbW7fXJtHeak7eHPc78TwFMIQKGuDxX8tOhJQNgHaCL6YPXBjFZhaqDwucgCmDfxjsaE2cm1yl6umZT9x50lzCZxzxU9RK6RxrP2ca0qjr0xlu2-4FNT6CWcXLEhF_5AdQP9pj3Nt85x3sWDMsQsPXScpcSS0quSaqATZ2pVxBiMZuheUQpexiHuC9aeXz02u_M3ts_IK_FdRr0m6aOHol7qk4vCyPwL5pJvDNREN_sYi2zxAtm97zkLaD6fnjBONTSldElAUTsew_NgA1tag4w0udWrNEf-2kxEgnaYGYf0mq4GeUcbqS6yLjtJw27U2p_BBkHI3NrECWy9op0zfXfTybD5X2yIqY1P1ypvN_gcvxiDi1C1uYBDJ9rBa1eBEXZmr4fCtLZTrKdtupw4yuB3t5G1Mi3n4Vtob3V9ryuj-I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یه ویدئوی جدید از مقایسه‌ی این مدلی که فکر می‌کنن Gemini 4 هست با GPT 5.6 Astra توی یه انیمیشن ساده(هرچند بنچمارک‌های این شکلی اعتباری بهشون نیست کلا ولی خیلی وقتا درست از آب در اومده این مقایسه‌ها توی قدرت دیزاین و درک سه بعدی)</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5370" target="_blank">📅 18:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5367">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=bLiL2rHVbhk4g0H3ii9kbwZ9DXJxWAdTMpfGIhCohQhtNklbgd-IcyvgUvazuOvgcetz8Cq7zw3hgSRBawlBPQHJzEp_vFtMl5zkZmB6IsyXBNrwN2P3XM31q-C1QJI53dxOnACrGQgk1lttE9NO_TgJmR6ZlmhtlwN3cVXtwiziPB6pmqsK9Eg4CJizw4JHWMjfI0a1qvxbFyGBz-_KQgduqUht9TFKBFI7h3lW9hrI7dOkGnQqscmttwXdXIMl6wYb4ToiLNM89-qI2nx74VWAb19LUq13Y1vUTNRoebuvJba0rNHsN0dFV48qYeTjSmnCO_y6My28WjQwh4tWQw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ad410f0702.mp4?token=bLiL2rHVbhk4g0H3ii9kbwZ9DXJxWAdTMpfGIhCohQhtNklbgd-IcyvgUvazuOvgcetz8Cq7zw3hgSRBawlBPQHJzEp_vFtMl5zkZmB6IsyXBNrwN2P3XM31q-C1QJI53dxOnACrGQgk1lttE9NO_TgJmR6ZlmhtlwN3cVXtwiziPB6pmqsK9Eg4CJizw4JHWMjfI0a1qvxbFyGBz-_KQgduqUht9TFKBFI7h3lW9hrI7dOkGnQqscmttwXdXIMl6wYb4ToiLNM89-qI2nx74VWAb19LUq13Y1vUTNRoebuvJba0rNHsN0dFV48qYeTjSmnCO_y6My28WjQwh4tWQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/MatinSenPaii/5367" target="_blank">📅 18:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5366">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خب، انگار توی Arena همه جا دارن تست‌های این مدل اخیر رو به جمنای 4 پرو ربط می‌دن و شایعه شده از Opus 5.5 هم بهتره</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5366" target="_blank">📅 17:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5365">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تیم Tokio نسخه‌ی ۰.۹ فریم‌ورک Topcoat (یه فریم‌ورک فول استک برای Rust) رو منتشر کرده که می‌خواد ساختن اپ وب با Rust رو به اندازه‌ی Ruby on Rails راحت کنه.
توی این نسخه ری‌اکتیوی سمت کلاینت جدی‌تر شده: توی macro مربوط به view سیگنال‌ها و عبارت‌های تایپ‌چک‌شده می‌نویسید که به جاوااسکریپت ترنسپایل می‌شن و توی مرورگر اجرا می‌شن، ولی بقیه‌ی رندر و منطق می‌مونه سمت سرور. نکته‌ی جالب‌تر اینکه نویسنده میگه راست بهترین زبان general-purpose برای دنیای توسعه‌ی مبتنی بر AI هست، چون قراردادهای مشخص به مدل کمک می‌کنه با توکن و خطای کمتری کار کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5365" target="_blank">📅 17:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5364">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kcIGglk3R7-w4e4JV7XJ4r2thuNMYGY5m29u2tL5bESARJ6GhVrz8d8-T9SKCSw18V-CvGeny2XEr4FQIQJDvQ8u2Uqej9ogyV_YozN-C8W4LKNgS9HYqig6XJ-vOjjmbA1wPFLMh0M3lFLpg5voUGvETxRU4idLykGy17JxxBn4cxhulOmZwmq9_pqvqu4CTFoeOc_W-uyurO9ZOmBiQN4vKs0w0zYADiwZSfqmGHAVB0ke1LgpcJvoWlWeAxXD6uacFfWyY85ndvBjKecL9B33nUMhGzuylx5IUYTd6kgZv7VFJKU3m_YkTRJc7yqdcbGhIlkRqJOHmv_S3GFvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با توجه به علاقه گوگل به اسم قناری، خیلی طول کشیدنِ Gemini 4 pro، و چیزای دیگه حدسم اینه که ممکنه گوگل پشتش باشه
کاربرا فعلا گزارش دادن که به شدت کنده...</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/MatinSenPaii/5364" target="_blank">📅 13:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5363">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ACnle35xJf7mp_Q59-RpXImPN536QfKN0yS9D57a4lwDl7L7XBljZR45wbHAq3eG5l6iMNAT8n_45c-STEBOQKcr7Vx2O0dGvJ2AWcH2mRBvT7gIhrfoe76gtLzcYDgdeCeNO2gprMbjWs7DUm5SiHrTzM_OjLMmFQti8Zd2Hrv8Ua9Gvpo7ieW4wJEpwN5Mj-q1zTPO_r-HNJ6vjiBZSy0rXgHcB9AkZlh72QP71E7SVjt_8KAjMb693XHEXnl8CCAT1E_rmQ-LZdqqQpAjsaaT0b8eL03nm3lR7pB3evaEFDaUk13118N8DmA9jZUEsOK_Bv1HCAnjWzQx26_m9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Gemini 3.8 Flash روی Cline رایگان شده آموزش استفاده ازش: https://t.me/MatinSenPaii/5099</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/MatinSenPaii/5363" target="_blank">📅 13:13 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5362">
<div class="tg-post-header">📌 پیام #9</div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/MatinSenPaii/5362" target="_blank">📅 12:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5361">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">AI
فقط یه ابزار نیست
نویسنده‌ی brettcodes از این جمله‌ی تکراری خسته شده که «AI فقط یه ابزاره، مهم نحوه‌ی استفاده‌شه».
استدلالش هم ساده‌ست: ابزار یعنی دریل‌برقی که کسی ادعا نمی‌کنه ده درصد شانس نابودی بشر داره و اگه برعکس بچرخه خرابه.
اما AI یه صنعته، یه محصول اشتراکیه که قیمتش بالا می‌ره و مدلش بازنشسته می‌شه، رهبرهاش مدام حرف‌های عجیب می‌زنن و پشتش مراکز داده و منابع عظیمه. به گفته‌ی اون، تکرار این شعار فقط داره مسئولیت استفاده از یه فناوری خطرناک رو از بین می‌بره.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/5361" target="_blank">📅 10:37 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5360">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjDxyXEfxti_w0SaQPDoN9SkETlmtEf9ywSG6e4AOpzG9B-XvK7JEaXF5bJSsfe-l7C0hBY6OUE4P5Jv67nv7qQwm7zEsSErRszw-VM09dUjgyWiHP01Eyo4syg2FBYvDEf29yPtRK1FC02BuzL3dOVK2FusnmN8FNJKCVjpgABhYDFsppSrt5Ch0sz9Q6ZaFXR5yKEzcmccsq3gEwPsccfw3TrBTdgzfumWYU5fERo5VI8zMTZRZ9tZ9LeWO6_muvYSQWCfqlTOVboX6ZWBD_Gk6dq2NZnw24m42qyiRF18O5fHXpZNNzuHEz3WwwbAjhvmykJsYGBvx7k7ciPJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر وارد بازی میشه تا ایجنت‌ها امنیت سایت‌ها رو به درستی تأمین کنن
مشکلی که کلودفلر دیده اینه: خیلی‌ها ویجت Turnstile رو نصب می‌کنن ولی اعتبارسنجیِ سمت سرور رو جا می‌اندازن و عملا سایتشون برای بات‌ها باز می‌مونه. Turnstile Spin یه جریان کامله که به ایجنتِ کدنویسیِ شما اجازه میده هر دو طرف ماجرا (ویجت و فراخوانی Siteverify) رو پیدا کنه، برنامه‌ش رو بده، منتظر تأییدتون بمونه و بعد انجامشون بده. از داشبورد، Wrangler یا یه URL مهارت شروع می‌شه و اتصال‌های ناقص قبلی رو هم تعمیر می‌کنه.
🔗
منبع
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5360" target="_blank">📅 07:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5359">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5359" target="_blank">📅 23:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5358">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">واوووو چه باحال
😲</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/5358" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5357">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هولی شـ... گفتم برای وبسایت MatinSenPai.com هم یه Showreel بسازه با فونتای فارسی و اطلاعاتی که ازم داره.  جداٌ از کارش راضیم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5357" target="_blank">📅 22:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5356">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت توی 18 دقیقه هیچ ابزار خاصی هم نصب نبود جز ffmpeg و اینم پرامپتش: make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/5356" target="_blank">📅 22:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5355">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اینم موشن گرافیکی که Claude Opus 5.5 ساخت
توی 18 دقیقه
هیچ ابزار خاصی هم نصب نبود جز ffmpeg
و اینم پرامپتش:
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
که یه کم بالاتر داده بودم.
روشی هم که ساختتش اینه:
۱. هر فریم فقط تابعی از زمانه
کل ویدیو یک فایل HTML به اسم showreel.html هست که یک تابع renderFrame(t) داره. این تابع زمان رو به ثانیه می‌گیره و همون لحظه رو می‌کشه. هیچ حالتی بین فریم‌ها ذخیره نمیشه و حتی موقعیت ذرات هم مستقیم با فرمول از t حساب میشه. به خاطر همین میشه هر فریمی رو با هر ترتیبی دقیق رندر کرد. تیکهٔ «Rewind» هم ساده بود: فقط renderFrame رو با زمان‌های قبلی صدا زدم.
۲. حرکت‌ها از چند اصل کلاسیک انیمیشن میان
- Easing: فرمول‌هایی مثل outExpo برای ورود تند، outBack برای کمی رد شدن از مقصد و outElastic برای حالت فنری.
- Squash & stretch: نقطه موقع افتادن کشیده میشه و وقتی به زمین می‌خوره پهن میشه.
- Anticipation: قبل از جمع شدن شکل، اول یک لحظه بزرگ‌تر میشه (inBack).
- Stagger: حروف و ذرات هرکدوم با کمی تأخیر نسبت به قبلی حرکت می‌کنن.
- Motion blur ارزون: به جای نقطه، برای هر ذره یک خط از موقعیتش در t - 0.02 تا t کشیدم.
۳. تکنیک هر صحنه
- ذرات: کلمهٔ «FLOW» رو روی یک canvas مخفی نوشتم، پیکسل‌هاش رو نمونه‌برداری کردم و هر پیکسل مقصد یک ذره شد.
- سه‌بعدی: بدون هیچ کتابخونه‌ای. چرخش و projection پرسپکتیو رو خودم با فرمول ریاضی نوشتم.
- مایع: با metaball ساخته شده و داخل یک WebGL shader اجرا میشه. هر حباب یک میدان r²/d² داره و جایی که مجموع میدان‌ها از ۱ بیشتر بشه، سطح مایعه. نورپردازی براقش از روی گرادیان همین میدان حساب میشه.
- جلوه‌های نهایی: یک shader دیگه chromatic aberration، grain فیلم، vignette و فلش رو روی تصویر اضافه می‌کنه. شدتشون به ضرب‌آهنگ‌ها وصله.
۴. صدا هم کامل با ریاضی ساخته شده (audio.mjs)
هیچ فایل صوتی آماده‌ای استفاده نشد:
- Kick: یک موج سینوسی که فرکانسش سریع پایین میاد.
- Clap و hi-hat: نویز سفید که فیلتر شده.
- Reverb: با چند delay که بازخورد دارن ساخته شده.
- Sidechain: صدای بیس موقع هر kick کم میشه تا ضربه‌ها گم نشن.
- زمان‌بندی صدا با تصویر یکیه (۱۲۰ BPM، هر بیت نیم ثانیه)، برای همین همه‌چیز روی ضرب می‌شینه.
۵. رندر نهایی (render.mjs)
اسکریپت Chrome رو بدون پنجره (headless) باز می‌کنه و برای ۹۰۰ فریم (۱۵ ثانیه × ۶۰ فریم) renderFrame رو صدا می‌زنه. هر فریم به صورت PNG مستقیم به ffmpeg فرستاده میشه و ffmpeg اون‌ها رو با صدا به MP4 تبدیل می‌کنه.
۶. کنترل کیفیت
وسط کار فریم‌هایی از هر صحنه رو رندر کردم و کنار هم گذاشتم تا ببینم. صحنهٔ سه‌بعدی زیادی کشیده و شلوغ شده بود، برای همین طول ردّ حرکت و زمان‌بندی تبدیل شکل‌ها رو کم کردم تا واضح بشن.
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5355" target="_blank">📅 21:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-5354">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بعد از Opus 5.5 واقعا دردناکه به هر چیزی که GPT 6 Astra طراحی می‌کنه نگاه کنی.  به هر دو مدل دقیقاً همون پرامپت رو دادم: "make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé.…</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5354" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
