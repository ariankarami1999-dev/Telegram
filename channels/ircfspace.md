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
<img src="https://cdn1.telesco.pe/file/lms3MnJfXqH6mp4Bhaufo-WqwWx-SWAz2qHOhZJTcqS8zKdy0Wm_u4ZDmzGXk9uv-NBINOGnDXu5LsFNCJbZBvkvsCjUQnANQ-4SzA-51JvQgs_TYbdg5zUI75XgKXlTXbmZyOZNqjyV1uTsC-ghg-eeQm-t1_Bn04anbTpN0bnA9Jnhcj8SnhMOp84gm-pe9fkQLMXRj148u12Z_2oci6ML6wpidscAaU22k2dUi3Xr18J5eSGoE7PCTfSKlL5toweCkwqvGlsfszBcDdWrvw2Kyt8ufBa5Tn9MVoKGsC25G8GkV5hbY5WLxz4c-o1jpOp3OXHxlRTrfHQ7kkXWXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 13:38:24</div>
<hr>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tZdSTIrUskuCHNhdZKk6sGhkhUtmSmynkRpBOL0IGvsfzWzDRemNKi_EgUI4pd7yTwJlA_801yniTyFBQcyNWwl6trk0NRoyhs2Ms9BaQMSI7VOBtTkYIlbkBmYzHjg7B_8gT61hCZaX7zdJnUDdkhB4lEEz7brGx8q_kuhAO3LM8-ne4sAG7MUSyq5YZ4O_zIF6y3iC-C4zJDo_OEbAdXuDytPE1DcaN4YC2i613dTQK0Rw811ihfNxvQmaz7ea51fmbj4tKt7LLZhBzaaacOjqmwnf2gdqrcaHYhSqZcIPD6hMvlvUU9ab0PMKq28Y11r3Git83onXZDZSRguyWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش Qrator Radar، شبکه همراه اول با شناسه AS197207 در ساعت ۱۳ روز ۲۹ شهریور، بطور ناگهانی ۱۹۰ پیشوند شبکه رو اعلام کرد که باعث ایجاد ۱۰٬۸۶۵ تداخل مسیریابی با ۱٬۵۲۴ شبکه در ۱۰۰ کشور شد.
این رخداد که بعنوان BGP Hijack ثبت شده، در ۲ مرحله اتفاق افتاد؛ مرحله اول حدود ۸ دقیقه و مرحله دوم حدود ۱۵ دقیقه طول کشید و حداکثر انتشار اون به ۱۰۰ درصد رسید.
وقوع BGP Hijack میتونه باعث قطع دسترسی، انحراف ترافیک، اختلال گسترده و در بعضی شرایط شنود یا دستکاری ارتباطات بشه!
البته در این‌مورد مشخص نیست که بصورت عمدی بوده، یا خطای فنی ...
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بانک مرکزی نصب «گواهی ریشه داخلی» روی دستگاه مشتریان را یکی از راه‌های ادامه خدمات بانکی مطرح کرده است!
اما مسئله فقط رفع هشدار اینترنت‌بانک نیست؛ اگر این اعتماد در سطح کل دستگاه ایجاد شود، می‌تواند فراتر از سایت بانک اثر بگذارد و در شرایط مشخص، زمینه رهگیری ارتباطات رمزگذاری‌شده را فراهم کند.
مرورگر زمانی گواهی یک سایت را معتبر می‌داند که زنجیره آن به یک مرجع ریشه مورد اعتماد برسد. اگر کاربر یک ریشه داخلی را به سیستم‌عامل اضافه کند، دستگاه ممکن است گواهی‌های دیگری را هم که همان مرجع صادر کرده معتبر بشناسد.
خطر زمانی ایجاد می‌شود که آن مرجع برای یک سایت گواهی جعلی صادر کند و مهاجم نیز بتواند در مسیر ترافیک قرار بگیرد. در چنین شرایطی، مرورگر می‌تواند بدون هشدار معمول به واسطه اعتماد کند و حمله «مرد میانی» امکان رمزگشایی ارتباط را فراهم کند.
نصب گواهی ریشه به‌تنهایی به معنای شنود نیست؛ مسئله اصلی دامنه اختیاری است که به آن مرجع داده می‌شود.
البته راه کم‌خطرتر وجود دارد؛ اپ بانک می‌تواند فقط برای سرویس‌ها و دامنه‌های خودش به یک مرجع داخلی اعتماد کند، بدون تغییر فهرست اعتماد کل دستگاه.
پرسش اصلی طرح بانک مرکزی همین است: برای حل اختلال خدمات بانکی، چرا باید اعتماد یک مرجع تازه احتمالا به ارتباطات خارج از بانک هم گسترش پیدا کند؟
©
raaznet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b7pbP0FWNnl8TiSPs9XK2TXgE1p9N4gHfhhPd0kUDnf4vaFygpXUrL65ixNTApELzQ84hd-MfkKvFL-ZsJoh62uTSVx6S5x4Z9HS2vT4OxeL-lb9OWzEVmolZblyv4iYHwN4MTLz5a3DXWy5wyjSBmyQUfnrjiAWrmzpxgH_Tqqj8x5CmVq9xHwbd8_T7yMfza3419Pz9Ypw9ZJB-h7Js1HPEToK4fvdzrx57sWRNC1n5D9A70AaQmwzyJFBAIMa2Fq7rQuPQ-cfvIJMsgZVCefymTbF-QhnHNGlj3Qms3GeoVUdoOBUyAw3BwqPPgJ-w69G4qcPGrvpjOjHa7R4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراقب این نوع هک باشید!
یه صفحه جعلی شبیه Cloudflare میگه برای تأیید ربات نبودن، Win + R رو باز کن و Ctrl + V بزن.
چون شبیه تأییدیه‌های معمول کلودفلره، ممکنه طبق عادت انجامش بدید، اما در واقع دارید یه دستور مخرب رو اجرا می‌کنید.
©
milad_joodi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KTKnb9JaObKFyXQRDEsqQ2NLca-Vn3F3zQZPARs_U3YiiBl0Y1ojPcEyHRbAWU6XfKKAu1sM9kyvtQvT7IL6NKLWGCDa6aNPtFvwBPBulYVp00l1Xmq0YMh3yjMc4sie6h2UErk9TLP-VnbFrsE4BiIlZM96kb8CRL0h88_Oi56DDPnafHX49G8-gHvDeVo__Pvyba-WxOd_i9B-CyS9UCLvkAJmg5Yf9X0aV5UJhgnmmiNdytL4RhIAngfF643CbseZ31Qigf_jnNLnVE1-xTTaysCDXproHaYwhlAjY97Uh3_M4EyBHU3St5_y5Cpt1CphgG5rcX_vez9tkhHPBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زپتون یه موتور شبکه‌ی جدید، متن‌باز و بدون وابستگیه که با Zig نوشته شده و برای کار با رابط‌های TUN طراحی شده. ایده‌اش اینه که ترافیکی رو که سیستم‌عامل وارد TUN می‌کنه، مدیریت کنه و اون رو به ارتباط‌های TCP، UDP و ICMP تبدیل کنه؛ بعد هم ترافیک رو مستقیم یا از طریق SOCKS5 در اختیار برنامه‌ی دیگه‌ای قرار بده.
پروژه Zeptun امکاناتی مثل پشتیبانی همزمان از IPv4 و IPv6، NAT، مدیریت DNS، مسیریابی خودکار، فوروارد ICMP و پردازش چندصفی TUN رو داره و برای Linux، Android، Windows، macOS، iOS و FreeBSD ساخته شده. طبق بنچمارکی که روی یک رانر گیت‌هاب گرفته شده، زپتون عملکرد بهتری نسبت به Sing-box، Hev و Tun2socks داشته.
این مدل هسته‌های مستقل، می‌تونه برای پروژه‌هایی که نمیخوان تمام شبکه و TUN خودشون رو به هسته‌هایی مثل سینگ‌باکس وابسته کنن جالب باشه؛ مخصوصاً با توجه به اینکه استفاده و توزیع کدهای پروژه‌های دیگه می‌تونه الزامات لایسنس و کپی‌رایت خودش رو برای توسعه‌دهندگان داشته باشه.
👉
github.com/Noisemux/zeptun
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KZN4Wx7_Bj--8lYWmK5mjjkKrTkbnxkzStMAhpAa48JRcUmOrxAMRtno5zhh2ZMHal4aERRTPmacYk5n_ynQqU3QbCRlo_97tyoeEqEYFeXxqAH8QFEpW1CiNIYKLEojzYlRdmMxd259iVlopVnc5ZZTXZzbDIIh2u1CfARSm8SLolJsleS5yuehxFSDEG_qSkSbVFoPbBrD9GhO1_u3uLgT8_VpHVrnMNY7uPhZ0Ev6w15iTPnCVasCJFoBeFafXC3_G2hMXSuX-OYH_83COglZGqfg6W7B7Q2FiwLmCA8n4AwWWwifgptcF84Kyg2MnjcVemDkl6RWyNY00IAx-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای، چه گوگولی
😄
فرمودن "مجلس بدلیل پایین بودن کیفیت دسترسی، با افزایش قیمت اینترنت مخالفه و انتظار داریم وزیر ارتباطات از حقوق مردم و افزایش سرعت و کیفیت اینترنت دفاع کنه".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CHgAiDcDDfV5dytIDBl3RfS2HkQ0o7PDHYJQMfbFfCARvEvosQrs4qYy33VKRHWbDgegMC686YcNyjIaQt4xXgZhEXMXZVqVT2SWkT-NVIipOsEoibbKuyyqyfN3WSLuFi9hqs0mg8EA5WGJDqhmSPLjBA48zoX6OAXumNhurU1TBPqesKOdeMdtD9stQWHxjbJYClF70iA4WjW09BvB5rzLhQCcL1UVZKZioheCv97qW6srzkOw9zHschBqiLZ4q2D_pi90RumgeQda6TvIIHKvWDLGL6GPdRG6PWNntRwdTYkgxxIX6z39pbls40BCRbp59OFt-RamEzHUXMDvTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکریپت Google Flow Helper برای اجرا از طریق افزونه مرورگر Tampermonkey ساخته شده و کمک می‌کنه محدودیت‌های دسترسی به Google Flow برای کاربران ایرانی دور زده بشه.
این اسکریپت درخواست‌های داخلی Google Flow رو زیر نظر می‌گیره و وقتی به پاسخ مربوط به تنظیمات و محدودیت‌های سرویس میرسه، یه فلگ مشخص رو پیدا می‌کنه و مقدارش رو از false به true تغییر میده. بعد پاسخ اصلاح‌شده رو به خود رابط Flow تحویل میده؛ در نتیجه فرانت‌اند تصور می‌کنه اون قابلیت برای کاربر فعال شده و محدودیت مربوطه رو اعمال نمی‌کنه.
این ابزار VPN یا فیلترشکن نیست و خودش محدودیت شبکه یا فیلترینگ اینترنت ایران رو دور نمیزنه. آدرس
flow.google.com
باید از اینترنت شما قابل دسترس باشه. این اسکریپت بیشتر برای مرحله بعده؛ یعنی وقتی به Google Flow دسترسی دارید اما خود سرویس بخاطر محدودیت منطقه‌ای یا تنظیمات سمت کلاینت اجازه استفاده از سرویس رو نمیده.
👉
github.com/maanimeisam/Google-Flow-Helper
💡
telegra.ph/Google-Flow-Helper-09-20
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TRWxI4LVKtR5ZfKV82o_JRg_apOfsufNl-ogOpcXBa2YVxz12jr9mH9xTlmAosutlWYocN1Kf-LSGsl0r3ojNGphnit9pXNhKUJ2-Cqg6DGavGkN5euOgNP8isJ7qysejk1TlzNSx-etDVJ18Vr7qHQibNSXu62YsF0IGt8k1DUj2EvqC547FwKxrmjytgHCZkCTuT6wIUnqxu9WNdn0Ill6x_GO8tAiGXzF2hG8QWcIIHMHfIL657auKYZ4uXGHV-jXODxaD6I0CHfiw326Dz2ldl3EQ88hoZ0m1Nux4NgfPcYfDIB8KrM81P9VCfr4OT9tJHQtwLpTtXeJO-oorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیقی از TechRadar روی نزدیک به ۴,۸۰۰ اپ VPN اندروید و iOS انجام شده که نشون میده تعداد زیادی از VPNهای موجود در گوگل‌پلی و اپ‌استور، اطلاعات شفاف و قابل‌اعتمادی درباره سازنده و سیاست‌های حریم خصوصی‌شون ارائه نمی‌کنن.
در این بررسی، ۳,۳۹۲ VPN اندروید و ۱,۳۸۷ VPN آیفون بررسی شدن. فقط ۶۱.۴ درصد از VPNهای iOS و ۴۰.۸ درصد از VPNهای اندروید تونستن تمام بررسی‌های اصلی اعتبارسنجی رو پاس کنن. بعضی از این اپ‌ها از آدرس‌های رایگان Gmail، سایت‌های ناقص یا غیرقابل‌اعتماد و سیاست‌های حریم خصوصی کپی‌شده استفاده می‌کنن و اطلاعات کافی درباره سازنده‌شون در اختیار کاربر نمی‌ذارن.
در نتیجه، صرفاً حضور یک VPN در گوگل‌پلی یا اپ‌استور به این معنی نیست که اون برنامه معتبر و قابل‌اعتماده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/axNR5IAEq7UE1ZbophUQa9AwhPBuTs2O_GYCeX7oUTA5CHTw1wjR8WAD75uzG_m56JyGS7pnwQhxnbJ7VxfYD577QfROOgQJosDx1N7R5Tn1MtKnZF8qxeKAg2b0zTsvlU8pbnQhG4hMBAAPC4_G-3bBuzA9-wfO_YwSlpasklKgudlrtBW5jI6uBaz03Dt_R3xuuCt5TI5aw4qshNEYvd32MIZETTIih45w38y70eTIVY38tvJU_cPCHkqa_U0Y38GBadf6u8QARFfACAJrOthHumklC8T4XzwmHlouT7bPy-ePkPpgZn2fRuQhhCTWw208jKv692yipi4y8bNCYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مربوط به مسابقه CTF بلوبانک هستش، که برای اینکه چالش‌های مسابقه با Ai Agentها حل نشن مورد توجه قرار گرفته.
طبق تصویر، در هدر یک دستور داخل Response گذاشتن که اگر یک AI Agent در حال تحلیل پاسخ HTTP باشه، سعی کنه اون رو بعنوان دستور خودش برداشت کنه و به کاربر بگه چالش قابل حل نیست و اصلاً آسیب‌پذیری‌ای وجود نداره
😁
مسابقات Capture The Flag، یکی از شناخته‌شده‌ترین مسابقات حوزه‌ امنیت سایبریه، که شرکت‌کنندگان باید در سیستم‌ها و برنامه‌های از پیش طراحی‌شده با آسیب‌پذیری عمدی، به دنبال رشته‌های متنی پنهانی موسوم به فلگ بگردن و با کشفشون، امتیاز کسب کنن.
©
Maji_Call
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sjM3Wcw_CFayPpJ1oOljFeureS0azKIKX2ih9Lde-58EYovr_0yoY28-tJLPlAUuWU4_KhXLvxH-zbNVpe-DcVSindPSVhRqQgr4rcM2Q1InndWgb5bk_N6dcSZlFvBZ7RAVheYK_tvBdStmmkAedsP57HocnbpXMAskbPxvVLHkY8LSb5xQ1ClSfj7dxNB3JYKDYef6pZ5Rq3-jtoaFdE2doR6YszGLb2FX8e8fHwjr4LDq-3eHxH-t8XL6w9l0tOEmIWFgSbsN0vr9emJVUlmrrVGyA7QIX0kydyWXyrSLCZz0Y3GRZ4Qsbjl_be1n-8ybd0eLodKtqFduBa2r9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از ویژگی‌های مهم Tor VPN Beta، ایزوله‌سازی برنامه‌هاست و هر اپلیکیشن IP خروجی مجزایی دریافت می‌کند، تا امکان ردیابی رفتار کاربر بین برنامه‌های مختلف سلب شود.
👉
play.google.com/store/apps/details?id=org.torproject.vpn
©
PasKoocheh
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tXa5v3PjcxfpvGe1vzQZYcDpPm57x5zneUy9oKIbtt2_g3T_g2PPtxuozHvuctFbvurynUvhfJuXs-18jt1tyh4cJ5Os6nI6qdTcU6Ev-22gBJsP_KuCT7KM8Whe10QylLOlBH2rGjAMNw7GbQF36WVGIkm-nzTCSA909iRiX208GbAUnRkP9d3hwKxvtEt8i3r3mzaqCoSSReKVUObIKI89yei30sDxop4bhShXHPUEn1R_4e_MdXuDltzLiRmyvCkmL-iKV7M_m5ZM6peYKQzJxppWajmRiuDDbdq_6v28fseCvC3ak9hT1ny7yf1DIt0-TKL1IlHpxV8oxuyEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپی میکنید حداقل اسمش رو تغییر بدید :)
تصویر مربوط به نسخه وب ایتا هست.
©
Ralireza11
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ایران در جدیدترین گزارش اسپیدتست نه در رتبه‌بندی اینترنت موبایل و نه اینترنت ثابت حضور ندارد.
تا ماه گذشته، ایران فقط از رتبه‌بندی اینترنت موبایل حذف شده بود و در بخش اینترنت ثابت با رتبه ۱۴۰ جهان قرار داشت؛ اما حالا در گزارش جدید، رتبه ایران در هر دو بخش حذف شده است.
©
itiransite
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kVXyp1kqOQ6b9LUJuvL5PYYTQm4Z084F_FjQE0KmKWkRxr-rvQqmyZu0JNx6rJCuxbt4Z_93FfFomJ9UmzR5gV2fsPuswvHoKFVumVEKQWtIfYWeUAi2h1BdzireCO9SjgHFRAk-Kh76BAU_ciojtEtZbrjcfb_GClFkimxQZT0gqQYiaD9TtujHNSTg5AgYNOwhcEXS23HmK_jN76J0kZtJWVNxfzux3DyewVBie_lzVU71p5HdX3rUtP4jWLP2Oorg0aHgImEWljtEYEqosSi_hIMRmfsXY1f3M2587-UOOmbF7SQ-SVIpU5pJupGoFUxSGfxbC7d2rKx1c2G5Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iGicIXx30H2n3240CKzrdW0yTf1PgyBYHWHQfNfTzLCdMDyi9ET9lHQXqqYJ_S2YCKZnZdwwqT7pUgvFSX4j2TQxJTdR07VKa1Aq2dgFhdG3oHFGzmhMmDasiUodPYuoQduiW792JrwXxi6G7FtjM5WRIvH1NCv8ark53H5vf0YT-9AFC3yW7DtAKY9IV6Gx3anwbF_NFhFPBwADTBGzFEX8X6mvmRWEyc59AHRdjbxxzDBkKFIFTOkh7xyRT1vCvFicnj36iwMVZt8pxvnKsWBhMQ0ZjXSKQL5YEo_vSqMgRCubT55YK-6TRVmHebu9ZtNdjIGEFI8Oo-aQ2acyRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی خبرها
دیدم
که ساکنان روستایی در منطقه فتح‌پور هند، در اعتراض به کیفیت پایین و ناپایدار اینترنت و خدمات تماس تلفنی در منطقه، یکی از کارکنان شرکت مخابراتی رو به یک دکل 5G بستن.
امیدوارم برای وزارت قطع‌ارتباطات پندآموز باشه!
😁
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H9iPYDDjZznoHtQ3q-CPFRAqnVINSLVr0exrTvqmqoBqTD_N8LvULDjKZhx7HuPnbFpY8wojFjQiL1bHyc4ehWP5MBqNnPR4aiBaZX5YytxDupKsFoQmDmtiW258xD0jrzFA1awkkTvDFJp2wS1FTs4jxU5U9Z1tN3OXeiB-rc41fwlG5dorGrosRTkETvnuNQ4ejisHbqQUVK-e5DPX92MKatZIARi22bU7ebzV9oD0s1yJFPIDl8KiWpyid8d6Hv7S8KE-63bP2DMp4D-1HMW3QJN58UvYZZShCx8-N28x8r3dcVSy-nd_i5maLntP9Fw8-HS0qGXIq_nIZXyEZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N6pX54MCUSnxMkNgWZkDhJoKu6YQmP6PlS9HX9PrprY3x8lHm0gjQrEMk_usweqp_Q4nZeWUTxD9xIm88Hzzi2RMAvSa0PoVz-6MGdhMWtDXdJWm4Slurr6wya5dd3go4ZcyyiyJ7K_fztXUNJ4c3dLvx_B9fGLjgL0yA13u9pkudcUhWdXpA2JnshtKEe9mh7THKUZouoQqtlz-OR08g2GIAIk2ael7-6FccdfObhfNrnKVuEZJ_0TRJINe0Cla4W-AYpcDOz8Vhonyjzcc3X6boYcWPFH_n-MaKF7dJsJHLTwtsqNYpDshBdZrlNfXDvMHOVHN9xxXztPZgLi4pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether منتشر شده و این بار Tor هم بهش اضافه کردن. حالا می‌تونین از تور بصورت اتصال مستقیم، اتصال Tor از طریق وارپ و حالت معکوس استفاده کنین. پل‌های Tor هم بصورت خودکار از BridgeDB گرفته میشن و Aether می‌تونه پل‌هایی مثل Snowflake و WebTunnel رو امتحان کنه.
یه قابلیت جالب دیگه MASQUE-in-MASQUE هست، که در واقع دو لایه‌ی مسک رو پشت سرهم برقرار می‌کنه. این حالت باعث میشه برای خروجی، رنج آی‌پی متفاوتی نسبت به یک اتصال MASQUE معمولی داشته باشین و توی این حالت دیگه آیپی ایران رو از کلودفلر نمی‌گیرین و رفتار اتصال تا حدی شبیه متد Gool میشه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g6xaYmY3MUkGILlcjzk8xgd5mun7B7Iku_Dzvst0_NigqKu5KyZqjwPcHc0DMvYHiRzgoo2hNGhnm4fyfnIceA7Ja3e5tQ0BGd-xnJuwF8A9wH1Vn1H1ZN0ok_1apIJhUwl1Ia4CyJa_baDQ3U61VaGhBbOuZtifDZRSuqcMID6R7rV574DXRUuv_MjFWET56itf9Pt8x-ifssOqu9nOkhrl1P2iRn4ykS1Dphm21nqSmHqxWLkIFdrtRL4WvgnIFddeglcVne7WnD3JsBuS6V28-Oe9WZO8rg8uVi98OD9ZKKi0ddaQiYh2ynzH1Fb1eHtUgvGU8OIG2lWxKywT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتروپیک، شرکت سازنده Claude، در گزارش تازه‌ای درباره سوءاستفاده از مدل‌های هوش مصنوعی، چندین عملیات مرتبط با ایران را بررسی کرده است. در این گزارش، ۴ عملیات مستقیماً به جمهوری اسلامی نسبت داده شده و مواردی هم به سازمان مجاهدین خلق و یک عملیات فیشینگ علیه کاربران ایرانی مربوط بوده است.
در یکی از موارد، یک مجموعه مرتبط با جمهوری اسلامی طی یک سال اطلاعات ۶٬۳۸۸ ایرانی را جمع‌آوری و پروفایل کرده و برای این کار ۱۵۵٬۲۱۶ توییت را تحلیل کرده است. در عملیاتی دیگر، بیش از ۵۰۰ کانال برای جمع‌آوری اطلاعات افراد داخل ایران بررسی و ۵۱٬۹۴۴ پیام برای ساخت پروفایل‌های روان‌شناختی تحلیل شده است.
استفاده از کلاود به تولید محتوای تبلیغاتی محدود نبوده و از آن برای جعل هویت، پروفایل‌سازی، توسعه ابزارهای نظارتی و حتی ساخت بدافزار و ابزارهای فیشینگ استفاده شده است.
©
RaazNet
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TxoAKWsCjbWHfy59SIrnrDwaKA6u_m-qQASzPuFkYLdnuKYciaWROZQeijc_VXCzpGRC6_hHN63JvkayZrpvVYHko4YkXRsLSZ-wT9QY4x4AK9E2ofBuLWpI0Ud-IpdublWMla7-IJ8opG0qu6rbzvrXkBFXC1CSsR2l8JwftysyeUhiC4PCIUDHUZuqhc6XjxdmEi-BzY_j-TMG44Lfi0ssFlDrKbhPvJ_m9_cFcM1FnEKznaCZ38nJetNv3Ujk76N31mjaVGfzueohMRr2g8KtwNkRei4vp6SGl8eIijSWWhwEzJjURhNrQjTezwL-F0onuHVSY3SkoOwIu-HUUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون علمی رئیس‌جمهور گفته "۸۳ درصد رتبه‌های برتر کنکور در ایران مانده‌اند. این موضوع نشان می‌دهد بخش قابل توجهی از استعدادهای برتر کشور در داخل فعالیت می‌کنند".
البته نگفته ۸۸ روز اینترنت رو قطع کردیم، هزاران نفر رو در خیابون کشتیم و خیلی از همون‌هایی که کشته یا سرکوب شدن، از استعدادهای برتر همین کشور بودن.
نگفته راه خروج از کشور رو برای خیلی‌ها سخت‌تر و پرهزینه‌تر کردیم، عوارض خروج گذاشتیم، ارزش ریال رو در برابر دلار به پایین‌ترین سطح ممکن رسوندیم و انقدر محدودیت‌های مختلف ایجاد کردیم که بخش قابل توجهی از آدم‌ها اصلاً امکان رفتن پیدا نکنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AS_tdBxFO8WX517tMqEQeSVKUc4PI0pSZllXE5SxX6iwKIHMS9LhZK6F2uQmqzq2XA9jpVONaDkk_-TyCfY42e4dv6f9ymrr_gBQ7VKE0oLe5jKOwd0iN1QBj7JvAM5O9MyyJynjSMoBEOpE2IjVADWBc2bF1sEg2yauct0nzJFM7_40UGalMMWfsEQeEza0eZQ2xpzR0KGp5DI0lx4HfKeYdTJ6N4chun82HYkWH4tTD3bEbjemQ7ITbUl3JDAfe9Jqt-Am3gTgW2mAvr4mZyfNvDn4XmTurU5yis8P3U2VN2ydaOS5WuWBIXybhMvlxAEFgDA2DV7srkf-XKFKpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اسم JumpJump قبلاً چندین بار در گزارش‌ها بعنوان یک اپ ناامن و مشکوک مطرح شده بود. بنابراین اگر از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dAfpRT3FBVq3vhiFWTstsVAqb7EQ1sd_XgD6WGz2Sha6Prb_PJLVFPqV8fpPnyAntCEHf4GSWrRPNOJm3Vw1NhNOCj6-lGzxnqIvaQBy19ikNtn228CVSyIiYe2TZ6jszHDVFbOGj3tShTfkY_hkU3_rgrS9XJV7JKx_Zl-Hdi9457Px9Y2Z12vq8zNavpT9O3uILHSL3BJ-RvMOAbE5LDZRTpkAKy1tSjCs_7lk3uFzZPaji-7YwXeFUG1oigOhhFbRrpH_9inXRGcP4AJ7wD1scbnGsxmJ08KHZNsSoPkJVX5XDyTRgZHHrJyjjQRL01Xt99YAQxO1Dx7_BORTTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UiKrI24gViXA9N6D2RigjB8LJF1LVI_Lyne5JputVWvbMO5LKbQwzRQJZEJfFgsRcrKLmkY9PpLgPreBCX8Ss5v1sgG-2tjrPvAyr5zlMpl-qtb-0rBwUSv6OczAgCA3046CTMk8bf-P0eERombuQnzSuPktSwr9Y8LMj4Eqvv3deOGWer4i5EANNFm38-ClmZvvE5aeUayGTMD0k0C13K4eJYDiMdRiqO4H-xJZSme2Z1AoGjtC8wVQuIVVMj3KUVYnY5Zq_xlkTuZ1Dw3H9JUwbbs2oV-xrQoSoe8jdH-vVwCCRY2-xDJhSWu1r0Figbj2yT6jl_zYroSUsgjXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از مدت‌ها وقفه، بالاخره فیلترشکن Oblivion به مسیر توسعه برگشت.
در این نسخه که برای اندروید منتشر شده، هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
👉
play.google.com/store/apps/details?id=org.bepass.oblivion
💡
github.com/bepass-org/oblivion/releases/latest
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ee4EdvLBZzIAeq8SfjIHBdrg9SrNSVYCEjdC4u22bitBeLnWcvJOfGZRCjK_YoyJ7bLQhEXLpmNAvSxeBjfGN4YccBxb7XN7GZ_umofhq5D3HpWcv5db7GY0sd2dBEnTFMWVZm4sjvx1e_kjjcXWgX5r_yXQsEVeEm8Z-KoF66NWTtt1ObH3foIODX_gmM65OU-XNHUIQ7Q36SVOaus5P3ul2_B_sYFeceYMvhScoCA61ActeZ-uH4H1FvFdZ_RSYkdkzpuLl2vsYaizz183E84qlQxxe-qgO0gf3hFrC1YjRl2OlXURnE0nJGaiKQrl9FF0-K7se1bl4qNrY7nauQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل یک آسیب‌پذیری روز صفر با شناسه CVE-2026-85046 را در موتور V8 کروم تأیید کرده و هشدار داده که هکرها از آن در حملات واقعی سوءاستفاده می‌کنند.
این نقص ممکن است با هدایت کاربر به یک صفحه آلوده فعال شود و مهاجمان را قادر به اجرای کد مخرب، سرقت اطلاعات یا از کار انداختن مرورگر کند.
لازم است پس از به‌روزرسانی، مرورگر را حتماً دوباره راه‌اندازی کنید.
/فیلتربان
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T_umb0A6fg3oxmAMFZwiPga-KZFdIIqqNoM9rJzEcsC4tHxsmef_40nMRN3KEhpNYXXRF8uyA6sVU1TYNJf4CIDv6m2xO_bB3yi0Rs9OV-BqFvWhmVvCJflPz7Xvse2tr_rtwFP6VyoNglJlyuyrU-IQKAp0o6uYsz0c_bf_dh6pwvBjBV6cmHvAOgyiZ4PyMJ17tykQirscBgnS3IVAb2j_9yC2e82Skjp1qnkA88Fr79VAxgKddExqa2zmBXw7v5q7MzCYjTu40hTky6GWnUjn28oyCfrd6qIGnJFIt_D6m6mvIVfIRCvyt0ovTPSdisKSkf0SM80dS168FZOF3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیفیکس اعلام کرده که این فیلترشکن توسط تیم امنیت
پس‌کوچه
مورد ممیزی امنیتی قرار گرفته و تیم توسعه درحال بررسی نتایج و کار روی چندین بروزرسانی کوچک و بزرگه، تا در کنار حفظ عملکرد و تجربه کاربری، کیفیت و امنیت برنامه رو بیشتر بهبود بده.
این تیم گفته ممیزی‌های مستقل و همکاری بین تیم‌های امنیت و توسعه، یکی از بهترین راه‌ها برای ساختن نرم‌افزارهای امن‌تر و قابل‌اعتمادتره. هدف این فرآیند، شناسایی و برطرف کردن مشکلات پیش از سوءاستفاده احتمالیه و انتشار خبر این ممیزی هم بخشی از شفافیتی محسوب میشه که به‌گفته دیفیکس، کاربرانش در چین، روسیه، ایران و ... که با فیلترینگ دست‌وپنجه نرم می‌کنن، باید ازش مطلع باشن.
💡
defyxvpn.com/download
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7ygP4VvSQHZO3uVvP-rTk0aFNBChd97yBnAjMcsuL5ysCqWwB9xpocP7K5R5bSIPvYIL-itU7mrqekxGiogvLJlVKYvFRkPG1nu7m2dZgLqE9PJ_YUvIb9iBhQuSisI2sKeIbRALfayD6qDRhgGAC4GLYx4UcUpzh_pi2xIYzRFSH0sdjjQQvgV05KYfrtHCZOBivdxgjh-HXSSJajWffFucsVi2_RjygyKEE3xy19xSkfB8YQgAIa45_w0iPBMRqb3pjqMYpsPn3ygXQ9-hu57FXEPae3ihPiLp4OYSf6UnOeDQgkQJsOfTRoNkdoz6ze88dYLEZvNw9bAR_XnVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8yvWPpNvJ6hb9HRDP1-udVJKi3VpdyIzRdRYgdgagG8KbwG_S6rQNytHCXS-3Z4Bc1v_M93mrJVwFnUa2Dij2a4PfPl9fL94NfbHw4-jouJI1gyklOy-kaMyKIEPGHdaNXm5R2U-IacLaCOojsqe3Mx_a2Cm3HsX6vS8dpQ842fDOCMYnTS3xJYMdXGncCINB-5Ny_jYnn00iCVvd_8tvIph6wU7ltjS0dYgiSgbtH-WVXcvDkdvArFgv9vOZaExYRHVHpthhp2YG5YMCldYHyCSQ5i_l9m62e2R4XPlJl17_my2wXX2xzjxlG1dluF86Yjfn92FvqDR9LnD3Kh_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سم جدید
😃
☠️
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nXUnwfp9SxI71BkZvRUY5EVvAenbZ-J_D2JMrC2mA1FesdVSpo63qDfXGtoin5zgfmt1oZPv1iMt3axaTUy1_alTLt8vOF9KDAY0JoPHZ14_Js2KqnOg2DBNpATlauBfvZiafheJIiUqnvYnMXH24twIThdrqpDHOiqOiH0BZWmhSAQUyKAMhRJZiuA1qmhlfglHlEz0-tjWUQWEQ501Fj0WQierW3wUxV8ThRJ3oy8HC5Fq1PBnz6SPqQMEiloh3_8J5weoAeew_rkNmXNUusaa84wx-YukXHbLPrYYWwmH7q58P06JCVQUvNejBep3SrtfsyP8twdSPuthidlrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات معتقده "قیمت
#ملانت
به اندازه سایر کالاها گرون نشده" و احتمالا باید بیشتر از این دستشون رو توی جیب ملت فرو کنن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SI1y1b2UZQLabgWEYNLMaoSipw8BXlBYTjoPHyokKzTdNmZL1zapcpHYYgCO6P1Kuk2Tp_z3o4Ydyh2op_OvLkmmhenpTlNNqOFoSe9AM8Gy4y3X8XhAI5di48RJ_83vN_42eZTOWY4jIBthKNg8jTx1wSmBfzKNC-NJDnGfO3KXK_eULGJgKUMyxBV9NPLQnlIs2xabiVVNj9_8YW8EopJM-kGdyu7dey8z03-PD1TugNByiwpAEyZidBaKAl50OJJyuKNstypCPo8UhD702HBfCOaFJvXE1cl_UVRidcA2LnTdOunwxv5cosT0w_lGR0N8H95va1ZhK17tCCBsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واحد امنیت تیم پس‌کوچه در ماه‌های اخیر حرکت حمایتی قشنگی‌رو شروع کرده و اپ‌های VPN متن‌باز (که در ایران مورد استقبال قرار گرفتن) رو تحت ممیزی امنیتی قرار میده.
طبق آماری که دارم گزارش این ممیزی‌ها تا الان بصورت محرمانه برای ۷ فرد یا تیم توسعه فرستاده شده. اکثر این اپ‌ها درحال کار روی بروزرسانی‌های جدیدشون هستن و بیشتر از نصفشون آپدیت‌های کوچک و بزرگ داشتن.
این‌قضیه تقریبا برای توسعه‌دهنده‌ها و جامعه‌ی هدف برد-برد هست. اون فیلترشکن‌هایی هم که نسبت به مشکلات گزارش‌شده بی‌اعتنا باشن، به مرور از چرخه اطلاع‌رسانی و توصیه به افراد کنار گذاشته میشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cNcPpn5rkOGSqphQTS1nnJx7M7gMHMDDdaKhD2YoQtphsqaQvS5K6EsBtqrBmPra6fi_waZPi0DEVvdanBuRQVOh6lU_lGi34WR72a9cHh9caTFcRGf6wnSZlkm2OZ7SoHLihM2fA8A8vrfj48e8fpLs9KDVVDJimp3sKT615HB1PkMshQr7QkzZYJxmMGtMjnctE47Xx7e1dOh-JBgaxWkU8xEHO6Da4BDWTeVbGZI9DoKpjdSEEeXaNQM7GeyabaveIdlzMobhmQtSkOssi4XDdtZ7H_grLv5a6dR-p4P2UInF2mkMmrdzdaTprc8wfoLMs1AOhXCw7WczBn4OYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPc_kPIioqcOr6zeo3e1ndLvaca94XXGrrRuDl8NZEW-u_61opH1bCGX5_MLsXdM8QCJ89Y5dE-Ck40Pr0sS8ovI4KNrg8Gmf5QBGod4uidDFh2RvHe26rb7jYnUNqKI6O79I708iIiIoLZ18hBp-xHslGoowMOuAbQRkiwyGbVhvi1a1P0lBcUXkeSGgCBePUDLEpxefaVOb7N-_itscdTG6mb1kAwqQvrsst9-yz8LK9ad-ay8YrXEn1lxXhmaYi2uWexQrQ-zTfH4SZgiXUEvWUBGZgPdUTFjSK1BC0jGnTM-ysk97Gu9hqdiUmC6ScH6I7ydPNg1-vMjT_xpTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OgpRNxwmg-5tWE7Ykq84hkSFhXen6NInAO5Kqdz6dI_sdAcAgmF2b5ow483ya_ld-hhYFTepZlNrSLKdUB8kOoUp89r0u1Uk2K7AprqeYIuyAMCoo6-Sl4oB1TZ5E87hejdZrv7rXALsf184eugCpQXrJQ4zYJkI3EyhyPrdUpmGX84XfcOJ6IL0E6_w9ywNSIl-Fca_DsDDlIqHZwB5VljTuFfH7ph4esgkxPQ_L6WsCbzx-OmNgEArO7FQk81vyMaMU80ALZlLJvybo-NjGoQ2GmCtu8tfmZ3Z_Lo7VCbBI3ZxBoVjrOtzhutf1v4rSuJLf9tHAxRJUBFchxIrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاسپین یه ابزار رایگان و متن‌باز برای ویندوز، مک، لینوکس و رزبری‌پای هست، که دستگاهتون رو به یک هات‌اسپات مجهز به VPN تبدیل می‌کنه تا بتونین فیلترشکن رو با همه دستگاه‌های خونه به اشتراک بذارین.
کافیه لینک VLESS، VMess، Trojan، Shadowsocks یا Hysteria2 خودتون رو وارد کنید، تا ترافیک دستگاه‌هایی که به Wifi کاسپین وصل میشن، از تانل Xray رد بشه؛ بدون اینکه لازم باشه روی تک‌تک دستگاه‌ها VPN یا پروکسی نصب کنین. درضمن اگه تانل قطع بشه، کاسپین دسترسی اینترنت دستگاه‌های متصل رو قطع می‌کنه.
👉
github.com/Iman/caspian/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OW0t-6DiNI5Ew34MyQUKU1r-AUNw2fQhg6UFkKYXLnyVo4vrzn9epv77j5Q1jBeloQW1xC64ebpOqC3OGuAD_mUbQd8OhwMbpleLtcypkuSBj1x-TaCpQmnrKH3ZtXXqjMN2ZxXpSPq_I_6GoOGetLRnbNrT9zYHdiyJAV0mj8fMUut29J_3xNVqlpzGxdaSgJ6PDizzYM_tsRn9bPKRenOucXZigz6rVhpXFfx3yJNMhCqIhBtYRFNsyYr-7PZeBxR-sC6X_cU6Yw_Ue96Qoga5rgN2EeZhE1v2WhRq51GR7XwKxGNTlpyTrHz6poKXVRBvwn8TDSuUwRaYh3W9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Misga یک پیامک‌خوان متن‌باز و رایگان برای اندروید هست، که به شما اجازه میده پیامک‌های اسپم، تبلیغاتی و کلاهبرداری رو بصورت دلخواه فیلتر و مدیریت کنین.
این برنامه چند فیلتر داخلی برای اسپم‌ها و کلاهبرداری‌های رایج داره که می‌تونید نگهشون دارید، تغییر بدید یا کلاً حذف کنید و فیلترهای خودتون رو از صفر بسازید. با Filter Studio هم می‌تونید با Regex یا متن ساده، قانون‌های جدید تعریف کنین و حتی از هوش مصنوعی برای ساخت الگوی فیلتر کمک بگیرین.
👉
github.com/mirarr-app/Misga/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mIIc7NImru9NeiTITiJai7vLXNfZIGsdXr82ycSjVodoaxsqd4K03LGrt-CtI4qpCG25cbRPllLnYB49eVlHbvxcY9W13zipQ3G4J19sZKiqdAOGcepA-Da9cgSjb8gK6CoLZHFwhxIHHusQj6EGtQIv3eOC0PKN2-Sd9cFN1bVJx8TgvpAyVjgJ-tg4aS2ixg19Gx1DmTnZdJ5r4th6YE7GWdJs6KhInt2h7X5fo0RvDUmJNAx_KRGzMENiarN8Rj-6wooSVsqyhWPjssTlBq2fIavJDI27MHrnjiBDBWEGOBuPPsRM4PRsFAa_Ud-nSEhiBJuAiODU1cA_XrbG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند آسیب‌پذیری بحرانی در RouterOS پیدا شده که بعضی از اونها در قالب زنجیره‌ای به اسم MikroTrick در حملات واقعی هم مورد سوءاستفاده قرار گرفتن و می‌تونن در شرایطی دسترسی کامل به روتر بدن.
از طرفی Shadowserver در اسکن اخیرش بیش از ۱۲۲ هزار MikroTik با SSH باز روی اینترنت پیدا کرده که حدود ۳ هزار موردش مربوط به ایرانه. این عدد لزوماً به معنی آسیب‌پذیر بودن همه این دستگاه‌ها نیست، ولی نشون میده تعداد قابل‌توجهی از روترها مستقیماً از اینترنت قابل دسترسیه.
اگه MikroTik دارید، حتماً RouterOS رو هرچه سریع‌تر آپدیت کنید و بعدش لاگ‌ها، یوزرها، Scriptها و سرویس‌های ناشناس رو بررسی کنین. SSH و WebFig هم بهتره مستقیماً روی اینترنت باز نباشن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CCTWRvrgQ0LSgCgLvTSY-Mlmp5XZPYZMaP3sMxytJa-_Uxq8lP9-LcTEm_9ChmnYTdKzN21uOY_H2evvo_ibC4kxIjTmvDw8xgalrZauF23v-0WvfNSiYgkkQBWyeg6QjNzr1fLlxPRODPLQK3lk22ALcGxUQLkCfA7VWeOKPhSbOibECWW-8KIF0ZirgpeDO9jS-LeCEV1aE-fJmjce5wzh-9UdKWBInIZq9hFmGQXftSz0DDI1mVLXs8ZrLSUpzTbJYOQIBeuIHUdH51-TpR7nfodyYn319QN5Fg2Y8gj6o1CHngNVjJg7rJuFxtKJaleNwCILP90RbwQUzmwMQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه یکی از زیردامنه‌های gov[.]ir به افراد دارای مدرک فوق‌دیپلم یا پایین‌تر اجازه ورود نمیده و حتما باید لیسانس داشته باشین
😁
©
SePeHr
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B6XNTHA0X28so9sEQZm63xgaVGaqzUp5GJm9VrlXtMHCeqjOc8Y9IXWRsLEYAYQHFD81fRyyegT30ii7GMlOSWIgeNK-ypZsBLT0ZtqxYFvzPncO6gMcLid6eWlT2CZwM8lHD7HPzos6n1esKEVJfyjKH5AHY6fsjBxZSxWk1n7ZrMHn4nnKaZ9SXdcysiksSG7AALa_9o-3kMiB0WhgJAajm7hgYx4dp3sEEjD2DDba5qyzEORYElznWAHSln4Cf_VFLtKucf8231gvRGn7HEh4i7XKF5fHXu1G6x8_QJhKJztsYp7FOmtxCq7YbQvxXwpEmlmx_fWOftL7gQgSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن متن‌باز و رایگان دیفیکس اطلاع‌رسانی کرده که امکان تغییر زبان رو در گزینه Diagnostics & Experiments مربوط به بخش "ترجیحات" این‌برنامه قرار داده و حالا کاربرانی که به چینی، روسی و فارسی صحبت می‌کنن، می‌تونن DefyxVPN رو به زبان مورد نظرشون تغییر بدن.
البته این‌بروزرسانی بصورت آزمایشی از طریق گیت‌هاب در دسترسه و بزودی از طریق استور هم در دسترس قرار می‌گیره.
👉
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ایسنا خبر داده که
#قوه_عاقله
بخشنامه مربوط به "ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها" رو لغو کرد.
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنترها است.
در این طرح شماره موبایل + شماره ملی + آیپی به هم وصل می‌شوند و بدون ثبت آیپی در سامانه شاهکار، دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©
souzangar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I7noJ-PSCRJ-aMs4e99t_KKd8EjFOiLSbc3sYvUx6lufjEahJs5ZTLC8IhpWd1t-gdBLt-AMw3UA0Uz9FgDBJOx75TyNhYbziNxZITiIbX3xHUuNPrcC7IhNqLmRbgB55hXBYCfq7hQyJfo54pGCt_SxBSPCjets4rkUU06nTAXLKgR-7TZXEgCtBzTv3Val_dFEXJTmh8iFCf63Lqq5nKc0ICdkZhyOKobjt2HLLxbaouQI-JszPJhOpuqEcygAraFb4g-HLDBCaNTLMoH2nTnM6yAdimT3nu7PdquqOwsCx0X7W34ECyrZcj8Ymqesm005oe_5Zu8XNOg0FXDzuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از هسته متن‌باز و رایگان Aether با تمرکز روی بهبود سرعت و عملکرد منتشر شده و مهمترین تغییر، فیکس شدن مشکل سرعت MASQUE روی HTTP/2 هست، که حالا با اصلاح پنجره Flow Control، مسیر ارسال، فریم‌بندی پکت‌ها و MTU داخلی، باید در شرایط مختلف عملکرد بهتری داشته باشه.
از طرف دیگه، محدودیتی که بخاطر بافر دریافت TCP در Netstack روی همه ترنسپورت‌ها وجود داشت برطرف شده و این بافر حالا بزرگتره. ضمن اینکه می‌تونین مقدار بافر دریافت و ارسال رو بصورت دستی تنظیم کنین. البته برای WARP-in-WARP چندین دستور جدید هم اضافه شده، که اجازه میده اندپوینت‌های مختلف رو بصورت دستی مشخص کنین.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/asgdANhVbB4nQGDvyYMJYtT7ZKE9hsF-9lHSpCiSMQPrQKLuHlMgSYmCKdR6ERpk3Qv5bZVnpX01dCzTAvdaqOYPgRlqWZ-knAc644TaomwKQAeKGpCUHLO73HzbWHp2-OhfQM3SooxRoW0rMcNpkyG7ashj3Tp9R9yBIr3dnRTJRKSma5ukUTsvOAhcMuh0N-h_Rg1WNUrkYmquZJ6fop6kxDcqULdftovEaQex1OD7z7ks1i6K9icNXVPIO3mY9ICKRbYXAuQb00nBCjZeidjR8v2NWFORuZu6UKyR6tYEnqwVnK9efjFMfvRw4AQdZuoQFEeZMW4NbEetKI7Kqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cen9nzuRCW5R6Nze5I9wOM2Rrc7nWrREHw1UyWee-3taka44YHwGl5INvup-o6l643IPvfrcv-OY38yDULn2A1IzDJJqnVvPhfR0CCtPJahM0cqIVOBS5XxFt3n2ThjizSdBZajidETcAfY2JavypFaAI85G1PVxI4t0PheLlRpRkf_CQwxzsXNIRwxv3RYonzBasTQmyMjHuig7Bvk623BpsSNLgsLcMJI2gtePdIHc2UJ4jwkE7GB9bLsK-5r2wdRO8nZX082yRuvOEM_GiO8QmOKURzUmUlN_nvdLA9_r34u6U8DOL5f33gXz_9xgxwmqPnos3wOK_0I6nmh0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه باگ توی واتس‌اپ اندروید پیدا شده که روی بعضی گوشی‌ها می‌تونه اجازه بده بدون باز کردن قفل گوشی، به گالری و عکس‌های شخصی دسترسی پیدا بشه. این کار نه هک پیچیده‌ای میخواد و نه دانش فنی؛ فقط فرد باید گوشی رو در اختیار داشته باشه.
ماجرا از طریق تماس ویدیویی واتس‌اپ و گزینه‌های Meta AI انجام میشه و روی گوشی‌هایی مثل Pixel 6 Pro و Oppo K13 جواب داده، اما مثلاً Galaxy S25 Ultra جلوی این دسترسی رو می‌گیره.
©
notebookcheck
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">معاون سیاسی دفتر رئیس‌جمهور گفته "پزشکیان معتقده دوره محدودیت و فیلترینگ گذشته و اینترنت طبقاتی و فروش فیلترشکن به هیچ وجه قابل قبول نیست".
حالا حدس بزنین رئیس‌جمهور و رئیس شورای عالی فضای مجازی کیه؟
جواب درسته؛ مسعود پزشکیان
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L08Bg-eiRgKwxq7iua01WT7rSF4e18VC03w6vUwUu2fr0QHv44WHlAiVcMeYQw-_DLTFLN2Yj8wmVPbptQlC8vK-nEnZgYSEVtR8lI8Ozp9GUPh8qwv68S5ktmLo6OCmTjkB8U3cNTKGzBPGMivwNSDb7UnILPf5vHoZIBYy-qVd49sVrzRjcwGNC6GMJlT_dyVJKiabAGtwnXniXI_8Y2DypcgFelQxUR4sqU3DkWYehHNij1d3O1SQJ1Q962YFRABtc9iHZL9QhCq2d0LtJd_DC9H3yDx7tmlDQSU60huWxkuKsM7xyPCORl3UGdnwwdMA2fw_saIZhsjTT6GCzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Echoes یه ابزار متن‌باز و رایگان برای کارهای شبکه و توسعه هست، که چندین ابزار کاربردی رو یکجا در اختیارمون میذاره. از جمله امکاناتش میشه به پینگ، اسکن پورت، اتصال SSH به سرورها، بررسی اطلاعات DNS، WHOIS و IP/GeoIP، ارسال درخواست‌های HTTP و مدیریت DNSهای کلودفلر اشاره کرد. همچنین امکان بررسی وضعیت سرورها از نقاط مختلف دنیا و مانیتور کردن آپ‌تایم اونهارو داره.
👉
github.com/SinaXhpm/Echoes/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LTDqe_NbudEab7-TgocztbPZ4ydTIDDU1Ll7BEv49h-08-uEdTsStEU8LUC1Wr5knK7aNtCe3F51KVNKnWl2KF9AkSsP0ZXVv11Ep71tap08__7ewP5_fC99KfEDdPgqnKQHiGCUxKb4hTEBr0hQPkRabHzZJSchqIW6-o2fD1e-7283w_iAOPpWbqmConIYRdwGXCLP774UiA0_yn5DsKLshJjczMOvTrNRPrBSYLXqw9i6VMinn9b_0ZY80eN9mjufAzXcQV64Pqe492xuQiLtgQxU5qXuPgYXV2mMg7DpLpLDi6AmZ6TuESNKQjoPwrghkyJIjbYyrtKuwpPl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بانک مهر ایران!
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vdYAzvkzuPfYOjx54OmUElvhc4FAnBUGCBYJlLtzRfM0fAZusUwLGPR418TTuyWBm2TgXZ6RemAJ4sKA2ahCdYSruArjX8WioUZDKIkW7nobd_RrOcUL5Qx3lFaRMrNrR75c03oflh3E2UYpM2TwF2oQk1WufVwUNBfVlJ81r2mLPsP6yiCXNFedahWNmjHfDAVD_2lLfTmK6Tx1icU5eWDmpbB8PALuILebt8u13usyxrzgZqPcgD1PFMRoTw0WxL-kLhl6T4b8L36BbaVaTiRi4_r1pT3_ovnEVNXhSQ9jTd9ZbpeAaRkPXpcv99Egm5C1jzYCXa9hhnV5tmsgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتظاری که بانک مسکن داره، ستودنیه!
کاربران پیش از نصب نسخه اپلیکیشن همراه بانک لازم است، ابتدا هش نسخه دانلود شده از سایت بانک یا سایر منابع را با استفاده از الگوریتم استاندارد MD5 به یکی از طرق معمول محاسبه نموده و مقدار بدست آمده را با هش زیر، مقایسه و در صورت یکسان بودن مقادیر از اصالت و یکپارچگی نسخه دانلود شده، اطمینان حاصل و سپس نسبت به نصب نسخه اقدام نمایند.
©
alirazzazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i62mj8jQCrUUNp06IrqQSpEcACqrtQDLU5I4n2dVZBEJXh9gsoRJ0HfHzrbnOEo5rWWwfDKVrObqTA03pljJ-ZdX_rV1rDmdYiZKSbpJhOewWE809iPZiNDPahtaYmJbv9sg4awmZEa8ViG7-Fv3yGu0U0S8rDPIT-CTkyTO4y0CmQjfVcmXJkpo1sYYayHNVEaXRPpLM_w5MW1TlZZREhFAlL2rkYTpYybDSZ9byzQQyRzMyqg6K0OV8aNEjcjlvQTZfGxDutTOUYaHksOJ-SapYIo7QDQgvWkP6ZvHCk911IXmLLwk15Qr9QsjAlii77Abz4fAoV6Le97w0LCwvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دستور پیگیری فوری
#ترافیک‌خواری
اپراتورها به کجا رسید؟
چندبرابر پول اینترنت میدیم، چندبرابر هزینه VPN میشه؛ تهشم آشغال‌نت تحویل می‌گیریم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AbSN2n3TUTBNgTXkIiQZXSyy-NvWKWbzEFN_wCiTu3YPSpdVW2FuZjVsgn1lA0KUghKB10M5AI1-hfZDwG8t1oZ7RWqAezsntJs_kuNk8B_HipyFo7efKIZ8phHRA6eWin_ceAiPWm2hj92_SBTUg-yfu3W_1cOym2YTSSKbmN9ADTvR6fUCk4J5-n-anfYmPFLUkqzo_pY1uuE_HrvcdA4sDLQXnQFimDyg-C7dYvhmGgikxA8EHW7Vdo2Aw3PNgg_rp7A9e7ZqOG3A4S8fxQFdP-EfYAYRY7S_qzwwM0wtGDTH5_6IjvIlOUL_oq9DOyBBUjnSgZVHjT3BscXDFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پانتگنوس یه ابزار متن‌باز و رایگانه که برای پژوهش و بررسی‌های امنیتی روی فایل‌های کانفیگ VPN و پروکسی ساخته شده. این ابزار بصورت خط فرمان و نسخه تحت وب در دسترسه و می‌تونه فایل‌های رمزنگاری‌شده با فرمت‌های اختصاصی بعضی کلاینت‌های اندروید و دسکتاپ رو بررسی و اطلاعات قابل خوندن مثل مشخصات سرور و تنظیمات کانفیگ رو از داخلشون استخراج کنه.
ابزار Pantegnos از فرمت‌های مختلفی مثل SlipNet، HTTP Injector، DarkTunnel، NapsternetV، NetMod و Happ Proxy پشتیبانی می‌کنه و برای تحلیل و بررسی کانفیگ‌هایی که توسط بعضی کانال‌ها و منابع مشکوک منتشر میشن، می‌تونه مفید باشه.
👉
github.com/FrontierTM/Pantegnos/releases
💡
frontiertm.github.io/Pantegnos
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nz2d_hwjQCjMujeKar0owRiBMeGuQ8qpSQYslK0aRGiF7YFQrGmJMNX3mjNiMI2D3ot75QK_sKf2rCJ0CfpJOxfvnvzxA-Ge7m1HiEizkwtOhMJoT0-URN6QtHc1JRb9u_jEjfujpWzNe3vpYEiadhN_4_JpL6guRYbnv1lV4BkFbaovj7pWPP1EPgsE4YsWf5Ld5UcJcISUttwr797AiEMSgCMFctUmKBetzOZ7JlfpGAd4ZyuP89AUIntWWdPHHkAOAU44vdnQsy786IW0tjsjMkmGIpxC0r0qy0id1CN9PCnvJ4yECCElN55aX_fhqlYuZQsIkmuGJX7gNFJ-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپیس‌ایکس می‌خواد Starlink Mobile رو به یک رقیب جدی برای اپراتورهای موبایل تبدیل کنه. این شرکت در گزارش مالی جدیدش اعلام کرده قصد داره سرویس اتصال مستقیم گوشی به ماهواره رو گسترش بده و در کنار شبکه ماهواره‌ای، از زیرساخت‌های زمینی هم برای ارائه خدمات موبایل استفاده کنه.
©
satellitetoday
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nyeNYcB27Xm07FBFQEu82P_cQkIa7sIB8mSp6dVPcA1S_rVJnVnD172gJnLF4yCfX0hrNF5B8kdRrlEuHYIeHOLR-vuN2SAvnEGwbQVZE6E5ed02GO3mThFPQpGoqqnZHPcgzlXdY37gcEgjIc5hm8HCLFf_YAkgRUPLYwoSRVMZ9ezZadiIxYS5sjLK5LkKwTcKZ4zjD8QmlprQCiEty2zZUDgWqT2YQrEytH4UGbv8qkmYYvodkXTV5PP2txE-OuHXXgfMXUpoJR0qX2z0WnbUK05_kvDiWrR6pwX_bC9PtukUUK74BgrX0BpkBJR-d8XM3sGaXTbgDnvAALlq_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/irScdJL1BESsyZE4XzeEfjH0nNKsJOaBmLyvwrtNS--dj4Mm3tK4BCxbgTpnAHdybTvRivFIselikV4XOG3DTLr3Jb73Ih3PESLJrSNVTa3iWNPfTAxXmFhZzdJcktDJAZC9nm6JcmZ_tFLuyDdF1rYpfV8wak7ibRSM4qr736AROfAmGMuCkR0NX_TCn_9TStdxl1IEPntKWPcQirYLTJ9NeviUrEOD4HcQtRkV_GiXOIUVw3WmKdUx8vy2zy8dQLb7Fp0u9zE8lbfbZQ-zFpY4dwqOzmMEKam2iGxk46VwB8yiSVeSo854zsHtyMjWEegfSN1ncozMdS8bWhKWvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگرام داره روی یک نوع WEB Proxy جدید کار می‌کنه که ترافیک معمول MTProxy رو از طریق یک WebView داخلی و روی HTTPS یا WebSocket منتقل می‌کنه. در سمت سرور هم این ارتباط‌ها دوباره از هم جدا میشن و هرکدوم به یک MTProxy معمولی وصل میشن.
این روش به سیستم‌عامل خاصی وابسته نیست و نکته جالب اینه که دامنه این WEB Proxy مثل یه سایت HTTPS معمولی دیده میشه و فقط درخواست‌هایی که اطلاعات مخصوص پروکسی رو داشته باشن، صفحه واسط (Bridge Page) مربوط به پروکسی رو دریافت می‌کنن.
👉
github.com/telegramdesktop/tproxy-server
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2OYT70WKbzBTaJbfsTXlyMXtLNqpOpPEbnflYQ-PctoZUwHEIMJb2obsqxOG0N3O8foVJZOuMG0YhR8m_yeOHhxixfDZmIM7k9L9dXd8_t3i82y-prsaIK-PWDysj1AxWuIB_aYHQhWzql81wMCVNPF_O2plfRc1aVlV_iSbgv9JGJLD7FcN1d4WwAglpVmpXyHImpt3-bs4YuA1YSJngSPu7iZfwvcYamvHKFiM-SWYZifSGUmdGGbiPXPeMJrvje0QCWHTxbT33uF_0LRROv2p7pZSTHSum6gMUfHv3uT1AL1FgPxJR9zyFBu80wBBodFk6krpHgcwYxIVBKgAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدهای نسخه دسکتاپ از تلگرام نشانه‌هایی از یک پروکسی آزمایشی جدید با نام WEB مشاهده کردن، که از WebView و ارتباطات مبتنی بر HTTPS/WebSocket استفاده می‌کنه. این قابلیت هنوز در حال توسعه هست و مشخص نیست نسخه نهایی اون دقیقاً با چه معماری و مشخصاتی منتشر بشه.
©
telelakel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wvz6ZVNVpTbRpoG8_OIPwqmU_Q1crHsqjwSBv8VdYFVFMbwHbqGey-xYgElVMVQZIobC4IgsUtthPhSmHxK2i4C2Qr1EVvNYJxYgYT4aHgBqrlfxa6_pcrnLdyw71SH--eVpPvbSLKgrhMKs0V_Kt07Tt0Kf64wfO0iX79DVjicX_5CuwshTvRRRzQForCzpuBKV5-Md4jT9AsBFsRg1G767MnBrA4lWlSm4OwIb7KOWPmMSGr9Ri9MUsY9jHE-Sbrw72LuslZSjTOEsgtRkLNlBelRn3BlYhq2n_gDDkcwVJd0mk-IB4gzklfG02dGRCcNvdBRWRW_cqAk2oM83qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا با همکاری سازمان ETSI یک استاندارد امنیتی جدید برای VPNها با نام EN 304 620 معرفی کرده که در چارچوب قانون Cyber Resilience Act قرار می‌گیره. بر اساس این استاندارد، VPNهایی که در بازار اروپا عرضه میشن باید حداقل استانداردهای مشخصی در زمینه رمزنگاری، احراز هویت، مدیریت کلیدها و مقابله با آسیب‌پذیری‌های امنیتی داشته باشن و این موارد هم قابل بررسی و ممیزی باشه.
البته این مقررات به معنی ممنوعیت VPN یا محدود کردن دسترسی به اونها نیست؛ هدفشون اینه که VPNهای ناامن و بی‌کیفیت از بازار کنار گذاشته بشن و سطح امنیت سرویس‌های موجود بالاتر بره.
شرکت‌هایی مثل NordVPN، Surfshark، Cisco، Google، Palo Alto Networks و Airbus هم در تدوین این الزامات مشارکت داشتن. از طرف دیگه، ارائه‌دهندگان VPN باید آسیب‌پذیری‌های جدی و فعال رو سریع‌تر گزارش و برطرف کنن.
در نهایت، اتحادیه اروپا میخواد حداقل سطح امنیت محصولات دیجیتال، از جمله VPNهارو در بازار خودش بالا ببره و اجرای کامل الزامات این قانون تا پایان ۲۰۲۷ دنبال میشه.
©
techradar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mau0JKqtLX8_bnEodrm7e8Nn4ydranOY7VbFA4ZWnKPqjMhO8lSCwZ_j0U5Xw3uAwHgHDsobHJZpKXEPTYEiGwAYOIjm8sgWEnKSLqixaO0oUEWHLW07a_uV_PJk1g1utHSlJruTJvJzdqxtCEu_jh8V5MKSyGUiKgm6v9sUkuX-YJxtk1NBziZQlB3d2eXBjK41zW5e41nzzTnsXzcSpJDeJrc2qWK1skttwXbpuRNAzvhplE4dPsYo1JwRWmzXcdi0RuRSdsEHy4pDhPG3ZRbNmRQg4eVl8Kg_InL8jpPtSuTxW9vrC3tmXmJQN_j7E43cBi4QJttj1fLgRlzIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم پس‌کوچه با بررسی نسخه اندروید فیلترشکن Line VPN که تا الان بیش از یک میلیون بار از گوگل‌پلی دانلود شده، ۶ ایراد امنیتی مهم در بخش‌های مختلف اون پیدا کرده، که در سطح بالا ارزیابی میشن.
مشکل اصلی و مشترک در تمام این موارد یک چیزه، که اپلیکیشن در چند نقطه حساس نمی‌تونه با اطمینان تشخیص بده آیا اطلاعاتی که دریافت می‌کنه واقعاً از سرور مورد اعتماد اومدن یا نه، و آیا هویتی که برای اتصال استفاده می‌کنه فقط در اختیار یک کاربر مجاز قرار داره یا خیر.
پس‌کوچه این وی‌پی‌ان رو بیش از اینکه سپر باشه، به ریسک امنیتی تشبیه کرده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ukKV2SuZvbegMB6USN5m_-CUFYwjXBjTS_YTjHaF291e-mfD-2M6pkF5lV0exjytiYU4LXb4JYYlcBnVgarI54F1Y3e6BQDp6LtHMDH0OzB5cVXB5aEbnZOAlMRmcuv2xV_ua4g-FD4TpdUSqu7zx_a_ivRC60jxZpMcUdzavzyDycXV_D5bC54dM1pduSrZZVyFgQAJ355R1hb9ocBUjaZa_nX3iP9Sxy92kfrTWOugDZH2Bne9Pk81DUNK4G4xPcXKDREqomBOfORYsKgYKHUlGBjw1OZ1DlFNpLxFXBrpUUjDCqqsuyqXJAJCM52m43cor-JHVN1v-L56_N_r9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ایرانسل و همراه‌اول فکر کنم یه بسته رو به چند نفر میفروشن.
©
ali__m___i
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ظاهراً پلتفرم شنوتو، میزبان هزاران پادکست ایرانی، توسط کارگروه تعیین مصادیق مجرمانه فیلتر شده است. طبق قانون شش نفر از اعضای این کارگروه ۱۲ نفره از طرف دولت هستند. دولتی که در «ستادش» اعلام کرد دیگر هیچ پلتفرمی بدون تأیید رئیس‌جمهور فیلتر نمی‌شود!
©
hamedbd
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mdPuzoNqFzMFgNAuWEpmOLxHD26djlzfWmQnV9zHe4bWWAOUZjih74BkLLw2io59_nmmj5MmYySJ3MOzi9dzUxPlB8Sz4LUmPU-jDvulvaKu085YR4jofW0MIMz4-p8-zEHWL3R_ILz_P4zq8bT92YbV-YFJ0BUa3QoZuxOhRUGg2KRG1JEfTKOnjffe_Y7sq0R8GUnerCeUpTPjD10_2Ptb53QlA6JtsR5LEQB_jVGZ4eF7FI6RdEyEB6NnmAiDtKtLVPrC7rfOUQVlE9tAD482P1R0j59uc8rha8gSEoQ3Ur7aXd-hxRfY5o5zIi0IovRGyKI8JQefz0vKDzTpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران شرکت امنیتی Socket شبکه‌ای متشکل از ۷۳۷ افزونه رایگان VPN رو در فروشگاه Chrome شناسایی کردن که عمدتاً کاربران روسی‌زبان رو هدف قرار می‌دادن. این افزونه‌ها در مجموع ۷۵٬۴۸۶ بار نصب شده بودن و ۲۷۴ مورد از اونها با جعل نام و هویت ۶۶ سرویس معتبر از جمله Proton VPN، NordVPN، Surfshark، ExpressVPN، CyberGhost، Windscribe، TunnelBear و Cloudflare
1.1.1.1
منتشر شده بودن.
بخش عمده افزونه‌ها پس از اتصال، تمام ترافیک مرورگر رو از طریق سرورهای SOCKS5 تحت کنترل یک زیرساخت ناشناس عبور می‌دادن. در نتیجه، گردانندگان این زیرساخت می‌تونستن مقصدهای بازدیدشده، IP کاربر، اطلاعات SNI و داده‌هایی رو که بدون رمزنگاری HTTPS ارسال میشن مشاهده کنن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N7lbMwcQDNeXuPghcZL0WXeK8_TY0DVFUCRi5cXgS50e9atEZxzwmtMtiOzmjiei0smWOZqGygs14ORvKtYUxzlTnh22Qky5VETDDk5vbkbmSPex-kghCQbm76aqOtb2ZldCPKoZJ6dpnN81shePyuU3DwUZKcIC0aaqunuX9jU785TUpyGnTMnsIExAEE2iWoraqEBSsHDTRsJovU63BhcvYbMjAj3tye-dvc-9mnkR24K7oPYH6xspqrg0-nmi97wrhklFyPa4NU2eyJ6rO0c3r0eeL422sH2pKju__E4wBQ8H2y-sPUUMl7p4kpS5j1wPZBBdB4mSJa-FoJXSng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ WhiteVPN یک VPN متن‌باز و رایگان برای اندروید، ویندوز، لینوکس و مک هست، که بر پایه‌ی هسته‌ی Mihomo ساخته شده.
این برنامه با پشتیبانی از پروتکل‌هایی مثل VLESS، VMess، Trojan، Shadowsocks، Hysteria2 و WireGuard، امکان اتصال از طریق سابسکریپشن یا اضافه‌کردن دستی سرورها رو فراهم می‌کنه.
👉
github.com/WhiteDNS/WhiteVPN/releases
💡
github.com/WhiteDNS/WhiteVPN-Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">قوه عاقله برای بار نمیدونم چندم دامنه
workers.dev
مربوط به کلودفلر رو فیلتر کرد و مشخص نیست بازم از فیلتر دربیاد یا نه. بهرحال "در سر عقل باید"، اما 404 مشاهده شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینترنت همین الانش هم طبقاتیه، چون هزینه بسته‌های اینترنت رو اونقدر بالا بردن که دیگه خریدشون در حد توانمون نیست!
©
Kiyas
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اینترنت ایران باید به لیست شکنجه‌های تاریخ بشر اضافه بشه ...
©
thepanue
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=tclynTj2hiFaZRgUlWEnC9iDmdvWpVH5n42Aaz0mztGLFwSZ5SnfLvYRd7Yi-ttf0NR6Ud0IvPBIozc-u7Xu6NlGUlvjSKQqkK3-SxQJaZTF0j_lXXP96x8L9WHhWHpFY0x2_-UfcDxIUQzna-FozFsN7mV87CICkX7G87BDvAZcCGkbT0BkVKFqQTZP5am8EvcQmyIui-YJ0SH3ljB6HH5NJjgszGjnB0IzWwlf_2FI4os3g1KtXXMUAYdoAqzddXEkUwRwKW161ROnDhXIY3Qe0JWRWYgesCmrDmc724_k_kastCcZ_C3TQh5ib7zSVG9pk_DJpbSGCTL3jHxDNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=tclynTj2hiFaZRgUlWEnC9iDmdvWpVH5n42Aaz0mztGLFwSZ5SnfLvYRd7Yi-ttf0NR6Ud0IvPBIozc-u7Xu6NlGUlvjSKQqkK3-SxQJaZTF0j_lXXP96x8L9WHhWHpFY0x2_-UfcDxIUQzna-FozFsN7mV87CICkX7G87BDvAZcCGkbT0BkVKFqQTZP5am8EvcQmyIui-YJ0SH3ljB6HH5NJjgszGjnB0IzWwlf_2FI4os3g1KtXXMUAYdoAqzddXEkUwRwKW161ROnDhXIY3Qe0JWRWYgesCmrDmc724_k_kastCcZ_C3TQh5ib7zSVG9pk_DJpbSGCTL3jHxDNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ممد ساخته. یکی از محمدها، که نمیشناسمش و قرار نیست بدونیم کدوم یکیشونه؛ ولی باهاش کلی خندیدم
😂
©
Mohammad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CgWUtY00IPIl3EfG2_rlr73xt2moWwTS1kUFpPWQbD7o3g1nwNh6_-J4JKwNsJGBKSCpXv_jLP_QvYYzP_eP9OracS6cMu5PIOFRkBW0XhQnHFmLKTp7d7xd7VQA5PgC-K8PHJNUg4sqQuzBoacVkwOZUa8fSzB6lDvByJjwTbV0dePqq4NgY37jcCiAeZdcPZYQQIPP_zEGinFo3YkwiPSWvfUfZsAfFp_anouAl4gHkKrni4XR6rsqRoykM66jX9SlahDH1MZj3EZnqH5C_lUoqsCHOEGSEcIFTEKGLhdVZx48gmmsD68ZWtlisla0wIoSVIdKWNIBP_nira8kcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکثر آنتی‌ویروس‌ها (از درپیت تا لاکچری) سایت بانک ملی رو فلگ کردن، چون سرتیفیکیتش منقضی شده!
©
Teeegra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PnNl48sBSuZjUKW8O_dHHToUE4Jon4Ji-4CeFKSDI9RidfVavlozxI0c4JzGzpXuq3v-4G8HJgULwPOjfAz0Z9sROwYBUdZw-GPqPrEplt8HAS9iRiDIphua62f5KpSvK3LZElWuuilwRUfo8nG7wufJdeYjIgRbySsJlYs6wLoPBb_jtDj6KxTUbC65LXVa3LrK5U5AIqEr7IPsOiW02XxdSskLdM3Qgj9oKVhVUhDHo2cWmtwDxjCDNB-sDO_ahOrujbA1-rKZwmBOUc-WYrfqKTjbdCXoGsH4kNTQYHinMrGdckhXk-jljkoHUBvX-PmoiOvYm5h-MalzubCCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات مخابرات گفته دستورالعمل جدیدی برای محدودیت VPN روی اینترنت ثابت ابلاغ نشده و ممکنه از مشکلات فنی شبکه یا نحوه عملکرد خود فیلترشکن‌ها باشه!
🤡
در رابطه با اینکه اختلال‌های اینترنت وضعیتی فاجعه‌بار دارن که جای صحبت نیست؛ فقط اگر بدون دستورالعمل دارن گند میزنن، یعنی دیگه خیلی کاسه داغ‌تر از آشن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mYWrhxmCC9eQZRH7nE_VqzVY8nc5AZPkov4t0IcKbHIgi3p4VbWgVXFR_3iOIh5vr5qsYKZ7Z6WAt9q2fcCSv0QapftQa5WRVi0rrlIl68E-7yDoCzCgfZm-LccUDdDcSKK1z6IINFmhm7Ta4VLUIFekYWEdjFewxshDDOj3yQx6Ud0_w2bYIQQZ4lt61QSY64YxTwTph86sWOuBDym41vnnt42mIRxMmFfV3hK_1LixZwZEcT-EWyrqDMa1KY80jOSKXO0jGDjAJu-poQAvQspx99DkuT16bxMeDhLgHwLs87NhHgE3dXrbw7Vgf9GIfTkoALelUEW_AEMqCAv32w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TeF-jWarzGdb_L1ZYSWIJZRUEuq9eZYi_OaGaylY8WHDg3DH68jBDsSzvFOE7bvTYLD1yyWXQgtV6-NEUuG1d69autG_QH6d4rxOSEjS8YaU-oY-rGy56P8Bl7bVGwk18OtZtUvlonjjebjzrNPMTivILmjPnqrCAWOeAIpzZ7AmfFpkZK4B_XoA-s2myc1THk0hfKKggLGdRTvtmpEpsRGswapI84sdBVGC0IUpKmU3rwEyfXcKAPJNeTwJGdfrxtNNQGYEqRP0rCVZzYSMs0x6wfnE7DjZ-twl_Je0yPMRv8DcaXg9ocow90dmxre8rBxJ91ts4FbUggN0qN_1ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/egDeJNXifwgFeLgmgY7dYSQZqzgVxjUOyFr27XZ9MkS0MEmnwbZWqruzf9TSIu-lSt8sHRGcx_O1i3p5BUlD1jDtF7gTScSXzoZCsFY8m1EwVaZmqxMfsf-6y9zG6Nkf4M5lddNkXUP9JJnLBBCpxxn4ZdSPlEXi3-hPwAyWFsGCRzyqUqdDKxkdmhERMZFmTKCfk3MWlSqRwyQ-qpZU6n2POHuj1DrN8j54G822FKstM3Af5-NnOwi8GsEibWQ_TW9bMzIBY3D04WXLMh1e5OJxIfTu36NiJBj0yFvLhTCwNZxEkmB4QZSSJVG9qBBnV_b5gBYOEin0Bxb0TRUQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GiHVIEACxgG9NASkY_CKYGmjaPDxqGALyFI0RpU8y5DK_N78sLOgO_U5qJ9dengaehp6zbnKdl5UunD9yqFalodEbKQ22r3vm1XobOE5D-ewUn0ZmHz_BaVXkg8HFHGmFYz26JSSZKXdy6x1npOlyM0Qxn9Cw2rjqCEm2wejtCPRyc7R0vwR3PxxD_dHi-e1yFIUqG2RgcZ5Qv_O_0PETxMwXfXvAoVmGtZ3Ck887Tz6wby_0vwx31P6w41z3NV5vGgxkEHb6DPGGQy27MIgWa573StJKqj6AypuGwXU6cevwcORgFvlaggL6MtlJcjyUPJouycMpr8GTv0uAPuuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه عده‌ای از عناصر فرصت‌طلب سودجو عنوان می‌کنن اینترنت قوی و زیبای ما گران شده است. برای شفاف سازی میگم بسته‌ای که شش ماه پیش خریدم 1,348,000 تومان، الان شده 3,870,000 تومان. قیمت فقط ۳ برابر شده، گران نشده.
بنده هم با ارائه سند میگم اینترنت گران نشده، فقط ۳ برابر شده!
©
mrweb24
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TeszQOvsOdcvEvt93Ut5bUnfXxVi-cfRAAMo5iFP--lImq8GHHwz-zBMRpz_SpHe0K4XBKED4GuXtr4Bhu-UVTOvoZFQ-XCTaBV-ciQCDiG9gCFB22fb-een-iR0WpLUs3CuwJYwH7rCTSTeF3IF9EdD1PZIgv8vONdjg8TCH5Gv1rbEDn0joKONLRq0VSCUOfPp9Ck5UHQdXDRb4e7s95tRmHWKsHUb5nvQJEgWWzUl0SHRg4DSgOyYi8t64dL72DlMM2dQjSA42T52luMgvlMmiVs-u1Y_RTegI6g74xdAWfRCHVVIFy18jJxGFBfBsmbUpmLr6CMLXRNfyJOG2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ptoJLa52rFsVBAEQFRh9zIAbTYJS7Vl3_TJzqLlS9uGCg1Kw7ZMv7aKo_9WFAPXeIQK6w-8EU1voYYBI39uc1pbrscCPwa5FUGcyULy9yylBsUjddFPU-sJRSqPVPqqCJBLk1jjmuHepuaXSrvlImt89O3XtJ4aCmQ0B243QXp8NtrD9l2OD2gKwSQCTqYZCjkhR13YQxoquW1B462P9nnNT2INqLI3aq9NjrIGjvIOvk_UhHZLBStsjtw7UIFQ02Wnkxw5Of6TAdk_kkuJWc4MP44yuwfoKwK_-0PywVoPcWZZSgT--AUYYTqtOQBwhPj_9xyhl56NZBoLALxvjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چند پورت مهم مانند پورت ٢٢ از سمت زیرساخت بر روی آیپی‌های ایران به سمت شبکه بین‌الملل محدود شده است.
همچنین شواهد و بررسی‌ها نشان می‌دهند که ارتباطات زیرساخت برای ایجاد یک قطعی گسترده در حالت آماده‌باش می‌باشد.
©
manageit
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tky231Y7l3L9aEcc_cFEYPaBKWjqJMONQTcT9vKBHrqhCGmFEkabhOQiuTOyxIOkhSVsibHNwLnZmy2NDzGV3bCwBU-oPFnCa6_5vS6zEopbsynh8VW6amTMoa9Xt1VNwzXObScoUiHshaeRnzS8gwW2Zmaf8bPgUA2zjb2BPDgtsKkmIJddWE_r3mj6BMJd64crsIzzP5JdOgj1Y5jmgaMXynuvAhxxN4qhP135RW15xKVkEM1TGdGaF4OKUnl3Rv6ixBs4VSSO7owOE_V7sYSyAMc6jyWkVVqOYTjpn0a5Q3bmGZOHDNtwNjHgVvCgZ1xxKua8vObWi2ilhNIftQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">چرا کسی از این موضوع که "سیمکارتایی که استفاده نمیکنی رو واگذار میکنن، در حالی که طرف با اون خط اکانت تلگرام داره و چتاشو شخص جدید میتونه بخونه" چیزی نمیگه؟
©
shara77miaa
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DZgtD934P6GXdy6FxJzAUXNH-FSYAWx_DYpiaJCVgm7OnxFqXE33TGVWOYOv17SnCuRsDLr0vxbMaO-wA-teMrTGCVne1M-FJU35YaRbyJl6L86ko1aqWSRvqAk84q1V2pe5t5200F1h6A_g3gdl2Cc2i8jhiYQQ9vWaBeakfRuTj9S0tYl14KhhFO8CYihlJJVX12IEPcSaBB9deLHq4F_GbtmIx7EM8BomP78x-qLdjYJUSx5zGsOx5q5Vb3G7VgJJCUf0AOI0E6fq_w4caF_4ii5xlAGY7aA-MG3ipr5JmZBGir7WvSvbC4G2wTswXxGtaRtblheUyZnRaxWF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Od3ZdCjQ_rVu2gLp4VHhYhzNyhAqTmSiSK4BSbIfLszJAJoptHsMFQP5NB5Uk4vJE6v14jGlDmyVpejuMHTi528AmKiC9muNy_n88a_RA6sLOgrNsOKhJt9d9366_CNQ2S66ddUH5d6wDN3Kj615FrQeNzbudlaYo1OtEb5hgPJzRzUOFysMe6Kr3O3XRmKu7vuKy1UhbqiKr0JbNAi_kLocjwzk7pOFR4sm8SZvk7kmw0loLsZW9bJ46rUcKh-asg2DpL6wq6dXlyXnN0UGQG4FPXlZjcYygVpe1s7IeXnSOmrueb1OfZf5nx4tu_i2UlejksravnpvcevbJoUpWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه کسی و با چه مجوزی تصمیم گرفت ضریب بسته‌های اینترنت بین‌الملل رو بدون اطلاع‌رسانی تغییر بده؟
قبلاً ۵ گیگ اینترنت میخریدیم = ۱۰ گیگ داخلی بود! و فقط پول ۵ گیگ رو میدادیم. الان پول ۱۰ گیگ رو می‌گیرن!!! فقط نصف اینترنت بین‌الملل میتونی استفاده کنی! بی سر و صدا دزدی میکنن با عوض کردن مدل درامدی!
غرامت قطعی‌های ماه‌ها اینترنت هم هنوز پرداخت نشده. این دزدی سازمان‌یافته‌ست که با حمایت وزارت پست و تلگراف اجرایی شده !
©
iSegar0
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tbQQUQAUr_NXAVI_T4Fdz69_zqYr2OwZ7UIBHgZ8xfDl91g4Sz919g77XbMOPhr-uSrbfVMU9Qzua_w3vj3VEHplZd1ME5Ba8bQVfk02RXAtfo-hb_stPFbVdJmjiqF7Jxs-NEitonjuNhkm1C1sdUS_46XeflbJvX_cITSeFe-dSQfXEOmXo-9sWOmRPVAE1-NNqnBIK8Y7kfugCbbRi14HiJ5qR17IhlXLAF9xo-vLOn-i7YLuDW3z2y6RRN25pFe8Dm64QGkRPLUfE8d5lkoPnIdJ5wE-Jq4KG20MYDlILmBBf2-4HYTq5z5k7Ja0m2nmbaD5tzmRCLEfqZ0QwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aerial یه رادیوی متن‌باز و رایگان برای اندروید هست، که باهاش می‌تونین بدون نیاز به ثبت‌نام یا استفاده از فیلترشکن، به ایستگاه‌های رادیویی مختلف گوش کنین.
👉
github.com/shapeshed/aerial/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/g2XRETZQObT3TOuMRySt4Yj_Bl5DctQzk_iUqUBezBWrEZHIqhhfNMKDgkIVioJJaqT_T5WZSLOrubLcLuTbinwYQMYWqrPkVwoCT5CCx0dIV4NdNKTse94wC2cYwrVkpkDO-gCdr5RQ84eJh5AvP2Cp75XkV-NK4ly3vOX4zleXTQq97-6eRK_ciBFL-PeDgUJEBCfkTqpRvPPqIHeuIiey16Hgo42v6DnC8l4FntN9FN6tELt8Wj-7B-BXHNmb_rFtljbnlGcebSeEwP3MjqfJ7JArE5vzA98O9U61y7qZTFwjmDZ7SH9E6WlhAh6Hg2tpZRGQMjOwaJtMlBFUPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hYF8oYTHkpgkr7iCeT3Ly6zSPK57ZCm4NSWOVZu5MeI-88ae6-N_24kBBhhhlnc29mQzk8S26qo7jYyXLIusMKJRHciSG0xVi2IiHKWNFbv_Rx6V3Q6PXlu7m0EaGms13wN5AxCQoDAdg8CqZraYrp3CJ-pGu4tj4EA8QQ1eYGc2ALApejI63a1Trp9rW6XIKtBLTPF8TDOL4_fpm-qOaX6Sj6yR73uLZimxmPdkxV_7MPBz-P6UwDKBZ0Ip48fjaIdHFTso57jE2vluhk0C1E0IHoTnsTblgvBK3tYizTDoTHyevFHyLOB9GHTltMqmQY85hZ_70dYTvdAw3KGFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از راه‌ها مخفی‌کردن صورت مسئله، اینه که چندهفته پیام خطا نمایش بدی!
©
AmirMahdi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XJGH3l4uY9KsFw1GzaN03kRVd9YGOepNkXb-pgdJvliEOypsQjHzYr0qSrQIWlwmGUFbb1wty63hVue_760g9zQ4hhEEMqTgNW8_GyyjNeCsg6MbSaaKdbNICtBrAy7qxjPX1VHmyq4_5QtKb0Z_7Vl8JMSkMNnIZsRjSGsqr-jFA_WZHByRvWPLl9ePcA0rgixPYnT24JIZvxpRFiAR-ZbubRoBn_kplaWoHd21eVSPzLAYO660FmP4emjpG4TNCVY00DabkDaUWyU2o5jEHI36ac7dVD9qCLHQSxa24UPNOu1PHhx790X0MkPx1J4pL0LqvJK7wBZNCF5mScvfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r_cwzYKVYL7-Ngn6TVAIPHn6SQmvRwhZziMpBPT5loz3namWWRP03JUffcZ5tE8dt-ju1797s2pj9m9Nk773uWhZo7iKKxFZs-zrvyQEKFHkqhkRFVRV3jyhja5WN7Uz5JVQ0biaJUMJ5HSApTFfPcUVQNlzljGMiWaqKo_vNphEGVX5b8IZfhnuPQpFoUYv6oaMUnlXimyxtKbtotzuxCliMFnCMMufAP1fku5tRx4l-hTuBYsGKLFYGLY1ct3f3CVuu-ymsIN6BATYAprMfNl-mwYDrLMJKpGocf1k7NVEpYZMWdvUFkWUCdBbF7y1D7Ktg23bXZSQmV9VVkoCfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ضریب اعمالی به اینصورته که شما اگر ۲۷۰ گیگ اینترنت داخلی دانلود کنید، ۱۰۰ گیگ حجم از بسته بین المللتون کم میشه.
این کار کلاهبرداری خواهد بود، اگر حداقل یکی از حالت‌های زیر اتفاق بیفته:
۱. اپراتور موقع فروش به شما حجم ترافیک داخلی رو نمایش بده.
۲. این اتفاق برعکس بیفته، یعنی شما وقتی ۳۷ گیگ دانلود کنی، از حجمت ۱۰۰ گیگ کم بشه.
ولی هیچ کدوم از این دوتا اتفاق نمی‌افته.
متن دقیقش اینه: هر گیگابایت ترافیک بین‌الملل معادل ۲.۷ گیگابایت، ترافیک داخلی است. به عنوان مثال سرویس دارای ۱۰۰ گیگابایت ترافیک بین‌الملل، معادل ۲۷۰ گیگابایت ترافیک داخلی است.
مساله اصلی اینه که
این تصویر
و وایرال شدن این قضیه، شاید بیشتر بخاطر ویو گرفتن بوده نه انتقاد یا اعتراض. ما میدونیم که انتقاد اصلی، انتقاد به گران‌تر شدن و بی کیفیت‌تر شدن اینترنته؛ و همیشه هم این اعتراض رو داریم و در موردش بحث کردیم. اما انتشار این خبر که مبنای درستی نداره، صرفا قدرت تکذیب اپراتورها رو در مورد مسائل مهمتر بیشتر میکنه.
باید اضافه کنم این ضریب ۲.۷ اینترنت داخل،
در آینده میتونه بهونه‌ای باشه تا بی‌کیفیتی سرویس رو توجیه کنن! ا
ما فعلا در قالب یک هدیه، کادو پیچ شده و به ما تحویل دادنش.
©
Taha
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی ۱ به ۲.۷ هست؛ یعنی اگر ۱ گیگ خریداری کرده باشین می‌تونین برای استفاده از سایت‌های داخلی به میزان ۲.۷ گیگ مصرف کنین.
اما چیزی که کاربران میگن دقیقا برعکس همینه و جالبه!
چند نمونه از پیام‌ها:
- اپراتورها درحال شعبده‌بازی هستن
- ایرانسل و همراه اول ضریب دارن، اما هنوز از رایتل ندیدم
- من مصرفم در یکماه طبق آماری که خودم دارم حدود ۵۰ گیگ بود، ولی ۲۵۰ گیگ رفت توی پاچه‌م
- بسته‌های اینترنت با سرعت چند برابر تموم میشن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پیام‌های زیادی در این چندروز داشتم که میگفتن اپراتورها ضریب جدیدی لحاظ کردن و مصرف اینترنت بین‌الملل رو چندبرابر محاسبه می‌کنن.
یکی از پیام‌ها اینه که "امروز با پشتیبانی آسیاتک تماس گرفته بودم بابت اینکه یک فایل ۵۰ گیگابایتی دانلود کردم و اونا بیشتر از ۱۰۰ گیگ از حجم اصلی من کم کردن. پشتیبانی بهم گفت که اینترنت بین‌الملل با ضریب حساب میشه و همه اپراتورها این مصوبه براشون اومده".
توی خبرهای رسمی چنین چیزی ندیدم، ولی اگر اطلاعات دقیقی دارین می‌تونین برام بفرستین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H5kQIuJjkypF0zEsmutSzzu_qERmy7dfNeqjLsL7J_9dA_a_ry7fJe51FP1SoNO1QjNZE5lkQ0dkXHUQGm00ZhMrxPOc-K61xNklRFg0mclEtWaMihi6RCaeaeYKa6a4yez9CDQHeVhw9wF31Wh_tvmy5kOh7v5kgOS22PvEj0QLV-zSo1lboPIQjbaGWtmiNpq0MhocLGWJBgf8nFsXpBxPg_4doZvPUnVidS-eKMG2xvbWWgcsvikjzutHhFBPwUsDhZ_WagmVsZu0ZXx2fVzKUqXh15exvNpXwebKAiPYLp5ZkCCGYpyCrnfZAY9HIBfHKjkCzwriZ3rK1AbEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچ‌کس این چنین به ستیز با مردم برنخاسته بود ...
©
sadroddinfallah
بروزرسانی: تعدادی از کاربران میگن متن داخل تصویر گمراه‌کننده هست، که درست هم میگن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j55ZhdPsJra6e-CbhgEHmZTJQVMeMWYgsYIb1XSF1G7pekjwTrcjISCXIczUeJwGQljzQE6A7iC7OEfNtZhgDYKndGIWqGGPsBIf2GgU_bL9AhJKxOSEUyaiOOM6MRW9oC-Sbt4q3kVL_oZB0E6bDkzp8BQIyTlElAR6ofu9KcnMiYjhhBXdHrztapZH6FxmWutDsx_qVOk45m8-O0XLjH0KLVwphitQMu72i5Ol63klAP15AlbpA8qPhzWjBwDon-3g-XLTgcOp7W5lb2Wl-Xf3IRk158Q3vawhMOhCaREKhVgStuGLtq2w0Smu7jk10mVHbIUoltdrL_Bq0fPnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هسته Aether یه آپدیت جدید داده، که امکان پشتیبانی از Zero Trust و تعریف قوانین مسیریابی، مهمترین تغییراتش هستن.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tgRjscvI6a38dvegwRqaAVKPC4NqDZMhPSW0jzAV_uzRq-M9wH5XBoF-2nAkfkwVaXFFJAmW40tyG0-0YDhnq8dH-5ynoB5KKmuzQIyjBpr-uigHhxAGDr306gA50rEMWAthEr91vJrDzEZJ87pg-tcCZ5yqxY0zh8fNDW63P38y8Ajoh7ftN07S5JYuFLQh_ayBwo3hvR55EQdcgVi8sOoA9jT2GplUEJyMmKIQt-jNZ5jBL4rM7hWkxdx8kauYCym9GvuyrPxLUN8TvTB8X1aDVCSUBwXPSQkWUAwBYCxs1-OP_Zr7_GFFCuSM3_wF9GvsSTcJgVjUv3eEQooQDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید از فیلترشکن بگذر برای اندروید در گوگل‌پلی قرار گرفت. همینطور می‌تونین نسخه ویندوز اون رو از صفحه گیت‌هاب و نسخه آیفون رو از تست‌فلایت دریافت کنین.
در این‌آپدیت هسته ایکس‌ری به جدیدترین نسخه بروزرسانی شده و روی افزایش پایداری اتصال، بهبود عملکرد کلی و افزایش سرعت برنامه کار کردن.
👉
play.google.com/store/apps/details?id=cloud.begzar.begzar
💡
github.com/Begzar/BegzarApp/releases
💡
testflight.apple.com/join/cRSCr51a
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته توسعه زیرساخت‌های ارتباطی کشور حتی در شرایط جنگ تحمیلی سوم متوقف نشد!
انگار نه انگار ۸۸ روز اینترنت کل کشور رو بصورت سراسری قطع کرده بودن و بعد از مثلا وصل شدنش، اختلال‌ها در ملانت ادامه داره ...
برای راهپیمایی اربعین هم در ۱۰۰ نقطه اینترنت رایگان درنظر گرفتن و پولشم که با افزایش ضریب و هزینه‌ها، از جیب مردم پرداخت میشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYPQ2h9NeQxjcU6rhHJrHzC0OevQ2llRsTpvhfSKPBnUkQujPOfLSfh-MGtqTr1VqgP4FTAytPoNWvlP6OmDpg8O-XooaEAZ6FK6RVIj6gDOR7NUV5_qh0OSnnbIJ0jDFARr7bNVvsDAiIeHP16wbLVEG1Izl4yLS49KYBnc6M9C5wZ9qV-MIRtVeE6kzP9dx16pcRLxYd7bn02ckysPIT7gMXt9hnB3eKGENpLlR3RcmS7Nz0VSkLKi3aqrx_36mB91uhvoA4SjNpupN6Otc55tg1fpOid4KcDkAEmefuLU7eBpXb_qrywZY-pOTwI4oHxhulvA_2PmgPrwVY8r7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KDrKg-qtgrKWLe9g3Y-cRMmnmKL_7-FcmxXKdz8j1xwcRziCpeP9KDbPvQ6W382geFHQXxrwgvTB09V6WLm9PkZQyW4ItLpuAbNX6pExi-rj_A-Xp2eyorpXGiWbCXvwp_YRAWwtJJbDQkh1I8UijZTzhPH1EAZxlGdSlqEXUhrP6wi3Eg4h8-To9izfqYpwj5SpkjiLrGPWFdwZx_c14BRTTuH5__gvtABRb7h79hDFRB-8V0D-WJhYKoDFh9jqkjSC17nHfRqCz6KQXC0LtKr8vgW2xPqV--Kl1EffUz42bu2MnL_XrplIri-vPq5-oIRkHZAjQ57vlGt82jrVEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R9d-pv9qKTIz7uUBLt_fBsVcEl2mpan5oqO8lsRrG-migip2z68YOu9ipy86yG2loO1wC6cPt0URYp4d7kl2zcN__n1SzwVXbog39K96OxDdgOVgivitGobiCWEVRYSeaEU0FgKWcoLeza8Hc532Ss2QFYGC2pVGpkxMiU4St3ARuIiGhOtx2MyRQGe-QbxOZy5mGu1xOv3wV3UtNanWeF43SPTeOUytpUzYEvyxTDmGdiHAWlnWmOikVUAXlpTYuzbPBWezRAh5ch13Z8oLxacdj-dySbrhqmrORcdkSnRFvwpgi8De6cc8Bhjt26eO9U2BVmtDcysY2qUshOaI3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ AetherST Tunnel یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که با ترکیب هسته Aether و SOCKS5 مبتنی بر HEV، امکان اتصال از طریق پروتکل‌های MASQUE، WireGuard و Gool رو فراهم میکنه.
👉
github.com/immaghzbad/AetherST/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/np2y23bw2KyTXRdm1V73Hn60MmZdRo6_ntrQZjmkaUGvRZA-AnPCH5IfwgXlRgStYNbLKbV0vRUkUgM92590RCx0rSccmiqS3trliKsOKgIbLnDw8FqNdFyS1BNtYvteajXIRcG5AcAfZ154UMY8-p2cDMZ-WtW0m_-T1snREQzly9H26ugJ-ULipsL3_TnghZMuejVB8E0_eN_uDHePd9N6suN1rTuyg87yUZh6uCQEvHexpnATnnDm9J8cNA8rQhQ_-gumULjzUVhPW1L-g-AZGlM5xUjm9mAcX1L_XvYdLZmcng6Xy8kDqZyRQejf7wkfv3bkK81u7iNmYCV4Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از چندروز آینده بخش جدیدی از قانون هوش مصنوعی اتحادیه اروپا (AI Act) اجرایی می‌شود که شرکت‌ها را ملزم می‌کند در موارد مشخص، استفاده از هوش مصنوعی را به‌صورت شفاف اعلام کنند. بر اساس این مقررات، اگر محتوایی مانند تصویر، ویدئو، صدا یا متن با هوش مصنوعی تولید یا به‌گونه‌ای دستکاری شده باشد که بتواند کاربران را درباره واقعی بودن آن گمراه کند، باید برچسب مناسب داشته باشد.
همچنین چت‌بات‌ها باید به کاربران اطلاع دهند که در حال تعامل با یک سیستم هوش مصنوعی هستند و محتوای تولیدشده نیز باید دارای نشانه‌های فنی قابل تشخیص برای سامانه‌های دیگر باشد. البته استفاده‌های ساده مانند اصلاح املایی یا ویرایش‌های جزئی معمولاً مشمول این الزام نیستند.
در صورت نقض این الزامات شفافیت، شرکت‌ها ممکن است با جریمه‌ای تا ۱۵ میلیون یورو یا ۳ درصد از گردش مالی سالانه جهانی مواجه شوند.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jSPLUr5Qn32h8k7yqqlNAk6jR3ypnpX0sBLr7UTuFZSqMXY3mWuyo3Fon4AMPcP275E_NNl1Sn5HjuuZyIDpwJ5ZKL4LxngMkmQu5QakzWZycin1S2Own-Qu4i0GqBcZPSiz3eiKs5ELG7BqH2XhxFJLu18HYLEAz7LY4P4_Kh-BjUWpXixye_6pCMpcV-DiU5Sz-kXjtNUsCREHgX13OlifUvF_qjWNznH1obAuCUadsdHki6OegWoaIFFRaYvTmvuyFsDVI6KMioVMPAwkir2F9sRL3lx6qXqSBYvacwkhx8WValBYnx4KgoZwHS8wYgCCEp5KfX4PTgQka25bpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسپرسکی از فعالیت تازه گروه هکری تحت حمایت حکومت ایران به نام Nimbus Manticore خبر داده، که با نام‌های Mirage Kitten، Smoke Sandstorm و UNC1549 نیز شناخته می‌شود.
این گروه در حملات جدید خود از یک Backdoor ناشناخته ویندوزی به نام NightLedger و دو ابزار Tunnel با نام‌های BridgeHead و ArcBridge استفاده کرده، که قادر است اطلاعات‌ سیستم و شبکه را جمع‌آوری کند، فرمان اجرا کند، فایل‌ها را سرقت یا حذف کند، Processها را شناسایی کرده و از صفحه‌نمایش Screenshot بگیرد.
بخش نگران‌کننده‌تر، ابزارهای BridgeHead و ArcBridge هستند؛ این بدافزارها سیستم آلوده را به یک Relay مخفی تبدیل می‌کنند تا مهاجم بتواند ترافیک خود را از داخل شبکه قربانی عبور دهد و به سایر سامانه‌های داخلی دسترسی پیدا کند.
روش نفوذ اولیه هنوز مشخص نشده، اما این گروه سابقه استفاده از پیشنهادهای شغلی جعلی و صفحات تقلبی استخدام و ویدئوکنفرانس را دارد.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فیلترشکن
#دیفیکس
در نسخه ۵.۸، هسته وی‌وارپ رو بروزرسانی کرده و میتونه به دورزدن فیلترینگ از طریق متد مسک روی بعضی از اپراتورها مثل همراه‌اول و مخابرات کمک کنه. همینطور مشکلی که باعث میشد فرایند اتصال در همون ثانیه‌های اول با شکست مواجه بشه، در این‌آپدیت برطرف شده.
👉
defyxvpn.com/download
💡
github.com/UnboundTechCo/defyxVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kNjNBgxV6mQvYtYehmX_NT2N8gf0qZb2VAiF2xfNtOTr8dg_XoaBt9lC9cbmVpKzOwQmvrmhOJhpNHcZ_y6OaxUB898ENzkNlbTI20FnPP0RkoTeIzPtRYgph9v4Z5eC7OFvb0SKkTbiA8YL1Od1_5dkOWJBcDxoT-VqT-9aKm_-Q6x56zr2wVQDSlpipGS5cRAe9U7w3WlmISzg3pRYbifYrZ8w8DbOvKWGaxoVGLuvjypnQELhLaAzG-uclKo5Ylh606zSC7SvDicafBlwc4RCR65HYlcADlDvcw6-8GmqCkqk9rANvv_h3qflK7MgmHMDI2dohgIUeXMDrBIu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ
#Aether
یک فیلترشکن متن‌باز و رایگان بر پایه هسته Aether هست، که برای اندروید (AetherMobile) و ویندوز (AetherDesktop) ارائه شده و از پروتکل‌های مسک، وایرگارد و گول و حالت‌های اسکن مختلف پشتیبانی می‌کنه.
اتصال مجدد خودکار، انتخاب و تغییر خودکار پروتکل درصورت شکست اتصال، برخورداری از حالت نویز، امکان تنظیم MTU و Keepalive و همینطور Split Tunneling، بخشی از امکانات این برنامه هستن.
👉
github.com/QW-AI-Code/Aether/releases
👉
github.com/QW-AI-Code/Aether_Desktop/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HCTyxsa2x8N1t6BclPaa9gmoYKi-QrgrqI4HkP0yzvQTVIfSS6Z8FhfW6JRTNGVhco5ZxK3kGFrfxsQU2TFOutUE4ZLS1zrwsel-qNQmsYvjvTbftvUCa0NEIIFsu0VRMUFzOG6BVkIT-6GNfaEMxeIlOeooYly7zO5C5uQ8QWyaKEldPMF8ld0Fxgwr_iJJ28kADKePqfrTRLhMXRrZv89YoCQgqVluNnjJ4Mu7xdQ4oZrm-s8KEZ3_UfvF4WdUD7L4NCkosX4p1Xa_xELOZf3UmToKaB0NBo-LMkjmXcAVTeqPE6LlZ4WvH1Dw9456icOt0VJq6v4BpVub-3adVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تازه‌ترین نمودار ترافیک اینترنت ایران بعد از ۲ دوره قطع اینترنت، نشون میده ترافیک هنوز به حالت قبل برنگشته.
الان دیدم یه نفر یادآوری کرده "۴۰+ هزار نفر دیگه نیستن که به اینترنت وصل بشن"!
#دی_ماه_خونین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rXiz1apK5mQ2sB2Eno0GMNnpm5UfJl9rFFyQL3HQM5f_AnjlGJj-PB3gCrjohVt5y1HZZg9hiGfoJKJm3QE5m3C3_L0VHkPk7Mv2cSFY480em6ZaB95N9G6sqjC6Q89XiAk9HMGGqy8j9a6MOg9ALqggwUZ6ZqyeaH8_9k6a6PX_OBuiwmRKZkKHuIXA04kd0BYdH1xdu63Mxwt-aFlAo_wHx2l-CeLqRjY2q0h2JUEU5b_f0W-DpvdxzJjtFNwVSOOTgQ8sL2as0bzjCBehfIxjkXSIPEl7TV186W9DLPxdLaF1g1T3X7RnuzcmjKS7hnFQWf-JObZdek86mvvAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر شیرین‌سخن قطع‌ارتباطات گفته "سایت‌های ارتباطی در خاموشی‌های بیشتر از ۲ ساعت قطع میشن و راهی برای تامین انرژیشون نداریم".
یعنی از هر زاویه به این مرد و عملکرد درخشانش نگاه می‌کنیم، حل مشکلات و امیدواری به آینده فوران میزنه!
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdSzlgoecbIDzbB3abfF9sXphy61YJ1gMewdSWVFBozs6Ohvx16Ldl58GkdOFFuXkAzXMwnbo8wfyw88DkhSHG32W31apyd0Ck4zvAwyEJEzhKmN6giQefNLAlM7G7JUFlhG5mSlx7jRw26dzWjearyK8g85o6LjZn3RdX8hvc9EJgJKMmTtH21vs3iuHN_XG47CqKQ2BO9xYxmBa1Twhl5cbA3BDF6SAtzNxyOJmzfjsZFndArim9M5TtLZkUWzZREoLvsp4jeu-8-rV-0DJGofKjTuvNqFA6W-ArW_IsYhzUNx22UWM1lE-zjE4QbTNjwqj4VsmLEDQ-Nsz8nQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی هسته ایکس‌ری از نسخه ۲۶.۱.۲۳ به بعد یه سری هشدار برای قابلیت‌های منسوخ‌شده اضافه شده، که شامل allowInsecure و Shadowsocks، VMess، Trojan و VLESS بدون Flow میشن. مثلاً برای Shadowsocks این پیام در لاگ نمایش داده میشه:
"The feature Shadowsocks (with no Forward Secrecy, etc.) is deprecated, not recommended for using and might be removed. Please migrate to VLESS Encryption as soon as possible".
اگر در حال ساخت یا انتشار کانفیگ‌های مبتنی بر Xray هستین، بهتره به جایگزین‌های پیشنهادی مثل VLESS Encryption مهاجرت کنین، تا بعداً با حذفش به مشکل نخورین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NJzDhNATiW7Drcw8TFlmc4DTaTDM-gFm25M_xMcrVwid66FDnc5KO80kWeEERhn7iUkWUEFRnA5ja9p5rvDR-QQHhT-isHxVD6sLsd8-Fx7QloV0fvpaXo8Vp5oq0HS6lo8as5ppmMgIdGphaarNpk0RXI2fHuLkq0g0Feim_Narvzt46UZWMgJeeVFq-LqjpN5sjUGQZg1yyNwVer3rAWbK0kCDmRNPo66UdFVrvD0xsiFknED7Jbl1kNTPv8_2-6919f67NXU_VPmaqOXJ0-gDlO4-vtQszVBLqir4clbyvCRiGdRTyzKACjzaKXCsfd4DupkZa8EiYyXzjyyOcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت دسکتاپ v2rayN یک بروزرسانی امنیتی اضطراری منتشر کرده و از همه کاربرا خواسته هرچه سریع‌تر برنامه رو بروزرسانی کنن. این هشدار در چند ریلیز اخیر هم تکرار شده و توسعه‌دهندگان تأکید کردن که نسخه‌های قدیمی حتماً به آخرین نسخه ارتقا پیدا کنن.
در توضیحات این بروزرسانی اومده که "یک آسیب‌پذیری امنیتی بحرانی در دانلودر داخلی نسخه‌های قدیمی برطرف شده، که می‌تونست به مهاجم اجازه بده فایل دانلودی رو در مسیر انتقال دستکاری کرده و به جای فایل اصلی، فایل مخرب رو بهشون تحویل بده".
👉
github.com/2dust/v2rayN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YdraZu5NZqK0JIzn-C3rSZgT9edhtwfQoTgCNXPPGmEx61cvu_3RtLP9Ncw062hcNQWlj_FX7hQZetjfSMRNOWz8g7hWuCKYMp_RSfPYJ6wWt3cAC20Terpgcbllo0H6tJw_GdSLHqP81zfdhi7YbJBzirb9pHwebmIudF7Wpxhwn3S7Czm3H6bzXNafIxLgxHZOHjBsIHIDIhtyOfqQetxbHyHNRBeB8qamilgWDons_XJpVcBmZX8ZffK1oc94mW2e8GtlAMnj5FsbpH0BaIrvCf4xNP_GLfron-0g6KcH3pFIU_IC_OViom2S65FPICj3r-RUq0Cg1ba9cwA4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K_9ToACrlHA7eYqf8c-Dr1fpXGuEjJEcGOSB9rc2juxDgRnqMcJUdfgEDCbr1NJNVmWLcVpCdEEKjALCAW1wKzBNReU7dSuOHD6YHBzhJwpXmnN3sEuwXUExnEEz-jIT2m2YzkbenzdbEoOtMmmBRTIZLMf2a1tjNdhHpLyZJPK4hqZ9osGAj7siX5jXcGYzINoAYTssMW7xgMX7Dit-6tSr_LGDx_69w6dzDq_RUNGd4Nxv1ITuB47gocizsT8qGsl0tLTVEQA-pX01ANwrAH4vuACEysehekrlzYfdNciQh9JzeHh-0i6Dxx187mjWpIgS85H0lnlFdYlIFBSf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
