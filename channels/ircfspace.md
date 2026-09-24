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
<img src="https://cdn1.telesco.pe/file/rEsDVCpPDIIRNLx2MaB0b0GNiDDZ48gk1nOUORX94SmnhYbdmMpxdMXzTjlRdbrUdJEMx12zuF99GKU5fefwOQD1rd0-pN5_Ox7MWT-PlSAyxyxk8EKAnnpQKeIwtpCgdXTvQhvAJCDixdlU8QPXxD_sZv5RdwzcQuSn76g_5mKMIRY074uH7b7-Ncwm5FGj4NMgsIiCmfmihJKi3JAc9keDZuJnOF9kptVhcaHTPQM7n-HNnXphrB3u425WGyo9A9OZLaEfI3rUsD5JA4EzURwinDmFg09jeS3J4RHDqTvS1FIxyaVjv3_PaYxcVtyccX_8KUK8NlFRVnZz8hbMdQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 19:06:26</div>
<hr>

<div class="tg-post" id="msg-2616">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGCoACjvnBv-RgiX62J4oPUpgQeOOjwYGF2Lkw8IkDhgbp1zTG9B7AV795ZO81GtYrSfiypMI-AhY3-5vqnmv7-OnyBNke6gCVIblN_Istd0uKUNyLUGaur1m_OujMdZWWng-E49IQ5zTzW2IvNXXWwoKKQ50m90wr4extRKEPOrjEz2koIsPM59IhQLx5osJyZC-e2NV5d_PtxZK4LSWu_Cqj_ON-CJQgMOXyII5D21aAE6YycpmMNWvvehPFWRqfOOcu9vBZgefMWdhIf50QGmU9PZCUCOKW1zcN1bb2A9QJMCeGsax8Wj1qQGmoUamMRJoHgz65dakcRFpnDNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی فقط دسترسی به شبکه‌های اجتماعی را محدود نمی‌کند؛ محتوای حساب‌های شخصی را هم زیر کنترل می‌برد.
شماری از کاربران با انتشار پرچم حکومت نوشته‌اند که درباره فعالیت‌های «غیرمجاز» توجیه شده و تعهد داده‌اند در چارچوب قوانین جمهوری اسلامی فعالیت کنند. پیش‌تر، انتشار لوگوی پلیس فتا در صفحات اینفلوئنسرها و کسب‌وکارها نشانه توقیف یا محدودسازی آن‌ها بود. حالا انتشار این تعهدنامه‌ها، نگرانی از تبدیل حساب‌های شخصی به محل نمایش اطاعت را بیشتر می‌کند؛ جایی که مخاطب نمی‌داند آنچه می‌خواند، انتخاب صاحب حساب است یا حاصل فشار بر او.
©
filterbaan
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">معاون سازمان تنظیم مقررات و ارتباطات رادیویی گفته "حجم‌خوری نداریم و بخشی از ابهامات و برداشت‌های کاربران درباره نحوه محاسبه میزان مصرف ترافیک اینترنت، به وضعیت ثبت اطلاعات محتوای داخلی در سامانه تعرفه ترجیحی مربوط می‌شود".
خلاصه: حجم خوری ندارن، ولی باقی چیزارو قول نمیدن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJfR0EOM2XMiI5TTlpRocv9Pke0mxOrtZqkQuILYa64JBNQ0VYk1gyQbaQFiGkID-KnnmPS7aM0u6gveAK9yMgbJ3pXywNFjKOCYx3ts3aJDljOWB9v2Dtwx7yuI7ZMvoDllhSYeJk4l393DVY9PTAsOEsJPjJqhAHRo6pKj9qLysw6jlCgXsUvk3Smy6ENpTeYtDeDI2P3oCMPwpwfrUH3NkYjsC0K-lHbJntl9OMwShwu183wQDYwnlZqZ9ei8k2r8p-sQlqfuyEU7K5Q8Dna0YDRQHiasOpOwEaGI8c8q62SKSU-QaVTNEAYZFndXPZNbRmvhjKBxfir1kKmwLg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lnpFNFCWMOstKWA43mIN54ASqdvCn0p9AgqvgWIMsh0SQgXhfk5tol6EHb8XCv99xGYWGSZIjDl02EQU_b9rOToD8_IQdUtdmj5FeZSgLnkKXxnaUx8d_WmuK4Qyi5OGIe1ZtAkm8z30KTgvygi5Uob95r9IzDx3OhAd9XWfu2OgsvKwGZcnozo1NjPHsdTokPYUi0vZcTN8-vnLhI0MaYoE4ighA0cI6-xgzdIkhe9YFtYW9eENHwTCLV7j8lZHXwbj_4evPaOGsMPCXjONrX6fiCuQVEsopih6lxk6y4eVPq5NwJ_kxQumUMJR6PyO27fjNWR1uCoOXIukuk7JuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2611">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kqf7sVj9SHFPRPHSPbbLclNyetGbqr0Lo66XlmP01thYZTwZUmi9th-sd-1ihkIFLHz6dnBpK5k510sXA5y1pqGApujAzSMAX3MGYmxYMdLr8h1OtX50yNwgcqlWkxRr0ccmXibDXuZxt3PU4sTsGn_yiK62U2L6-wWZI0HnSO9MRsvkKHd-Gf-GQQayDN6djEtnSv_QQ0T4mcgaziT2Z1MIi0kl1GaB7W2v0OQcJ69j1dD0F8yQStCLaQPx5z3BkN1Eg7SVGIy8Y-LNef3vxktIbb5PIZU8O6L1PlVsl_M7cMqGlJdVh9pY3x4lwgX5c8LY1lTUkN16c5rOn8x0GQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2610">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eSUmMOysfvPRnbq-7ioCtNMNJVXrgyyOsw9JdxJLpR8omln8qR3stZRkvQ5Peo0s-PNzKbEZ-viNtNXe5KF34og58PifnQw0OFGOQ87Yqre53a-XNbpgkQKG1yJzyfgz7ta_d1SIC3mXFHpKOY4be5nT_xQcBWxntwwEHqR5agDtLVb5IJQKftqXuxHTxSN_m3CJGHsxRihEmQzKdCShrMswubcJkuRUR41V84OxRpj55VJzoQqjZbfuzmBWe1zQs2Z1PCnjNyYG9tlcuwA6mn7K2aAhrlPA4bWxpbbl9vPKBBuM15Ve6U30qGQmQj63NkpM1f2Ahe94bcYE08cP5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lpwFh6RLmXExZGDsVAp2O9QHzD5WvmYcRU0i-XivoYsY1CDfc_rV_cxFrztHAvxbx_M-FlCgIKhPmOf6vZc3ZAyA5BcEsMumVZklN_OV93BKoSX32l3GsGe9tYQYjXXh9d1xeDmJXnQ60MAW95CVQePfbOTHpp57i0hF1GdTLz-160MkrTIFC51VGN87xX3hmTlhcNXXFrG8hYVEf3_oQ3yl6aMelnGMvx4lLQvqjoOPfo5JuEAQdKXcBghGUKCosemqZUGHw_F1g_nEBUJC93JXk5M_929zJp_wYw8BM8b-fZgf10UUBBnhcOLlRfi1tY3MyWqunw5CLjicUlzTeQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qqwXZI5oVCPZuh4HKiweRFXYSltT_5K7w1iNg8K-Xl10Z7Jzht8SuhqmM0wk_PuKsG2PeP6iQN0Naz9QO1V9qF69x4aWRTKWGDIte73xc1Omzd_llI-ajKMkJJOaROySWZ-QkGht_VMBPyuG1X3TEP-TaiqL0Xjv1gp6hr-2GdccfhyLqIHUTIkCgk3WHbcP2Il1BZP2oVDqS5KeLA6yaz8gKU2WFVaYj0s4R7JD2OjxDphGcZGuIrSYDHNKyKaz-pRTlugMIyAvR1yN09YVLhom95t-5n9_Yaw2DpqUbDzbp3JPfABuRAsbBXBA2-PegmJu1e6IJNwHN6DLC_Gl5g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HfyYNDnJT4YU5j-otk9dLcDl6S9VgYekM9sBeIt_QUgusmdvAm2XKjC5C_ETjs7C9Qxrb7-gf5RKYBpKzyHzFD0vfKjtdh2w-5UX31wjExe0AGuedLhjx_i74VvyZDz4knGWjqE8kIIl4ozbfYKfyFljpfa-OgOZylzd6Pkeox6Bsn9D0kFGptPPSavd1jwIPxf2xZNtWg-I4gRzXetTSbJ8szUNTzMi9v8dYwv9gs4F3JVeT7MD_eNrTX0i6676IsvPOtZtnFDlbq6UlttVHD4HWNgdKVt8BLieZxDxOjVkG_Rb0o_68Q2PHlwL7uEa-e637fxDIUtsAAis27NIEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/G1MpEcfVVo_y86nqaL8bhKKnpBqPYvqxV5RupsyH6Fo5AG-djn9YpylpTgCcbrIrEsIGQWOnDUhViGrPhwKolv3asgF6y5ZyP6Fn3dsrv9MZO5ft1v9PymqUT8LizjZP3LgHVUwoCpR1lShlxsV2Jx6LhvWQp6io1abq6cq_2-PbFOUi1Y5WlJ8Ro8HLuarqCTKO2dk4wm7clU2RAXuExP1Cd_h2ljo_87EVgkCkKRsYjuY4szBI11RN62_ymLMbfabS8bn-1rTUpaQC0ORlcIRVQTBkcSRLFmI0fCo38YN9fzKdvb4JRTQJ_fNeRHpIyOhIox4UCPiGVYmMZkkScA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AulTgFVdq2zroFgTRXKhQSSAXo1nMzxgs03oC6C1rJxhHSOs2gir0Obz0uDyfavPY4NoiehEdK5AXkfzBXbLR7sapQjGN9aT7rzDTiuHumdz8sVCB8bOxkN0ALPkwS9bmGVSL5E9zH6D67K_BJ8CJ-QEigPkKWzKEruu60nU8SuJKsMXKiogQt4ml-RghseMkPuem9HLgJFYAFdgRFEoizZmbypFofc9cpuZFM8e165aUHZ4R_QhJOElXJv4O0fcozchOGbl--0T6oB_SnaaqpNqfs-NR8fIA0rcjEQ7sz1d-Gc0oe7RDJU2HGLWL1ajtHiEb3xmUFNKNNk2QNyMkA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2604">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nlDU0cNPXRku9y7A-7nxTUAZWr44m_c3G7qZVC8Ih4KcOPTgkmJGwbtK9eIGBkZ-PazTtdAgr380hCA-B3ponrGxBsHWj8J8tmbo-JTYbtpYpKS6L6J-zWJvXVdr-5pfPF2rGW_XAgXqgA2VehES51FjbqvC02L3phZrMfcL-9SKBWyG-uk-wPyjLG69fj_XfmlHZ1spOpVedYKaxDaqS3fAdR0Oc2VPQodCEuT--nA4LrbBqe0AhAkNxFqmYOsvji4JU1yCjO6-d6NFGKYxWE_zuUprc4by9UZ040QQ5H_lx03jzQzc6siJETNPaxE8geQ0RqJzN2-FVFwjhwNqKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nRRmd_tc3SXnq0cOoZF-_uTJ2p2lSiO9RIDhdM0Esve_Z0ii8D0knlVLLIBjVAbMDxa1ZqO4X12ycS3d6IX1uEIwZ7Bp7BncSHiaFjK8yR9GAcXP58F2MBnGqs8Pn7OtRpN3l3HGJFlqORZIzwkzJKIfv9CjbwMG6a9AQ0Mceys8oUwqSNT50tNp8szToL6t6cdSDgqVdu5evUZSMMpJupfv7q-Ix3KoAWCaq-SIVYbwBqeEx7_Negq5wS5J4IO958ZN9p3ZQ_arvuZFf2ptXE9puyDZ8HvCYukza7hbzNaVs7bfRHRsd9jj0EhhgVIdLJ-MyHaD7iW_7oiMYoL3bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bdFLjJ0fSRN0vOEPnCNIf7DrteMU5C16rMbbb8WeqWcUR8qM2p7eIgg2VK7jKDjojBqnlcbKBp0wtujIaJxipPyudO6x8VZoHflmmnRFLoN0bRdLFFQNvxCRVxSPq4FF78duUijy9NEC04qGhDEDxEfubWGDaQr1N9vGn6XB-OuZrvYtpeYLUNndhR8cWcYxXNDwWjpI5aXdx8s51B_HAdXAb71UB0aqzsMPIm7RsMmrZTMxYgPdy62vr1f_6mbYNN6LDt8r_4wYq8_ctl42BlP_QBQe7ntZlSwpZplnOWDl1Imk043nMFNoQpDqMj8HT9o7m0VW_Czh6UipTwULlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات سرشو از برف بیرون آورده و گفته "اگر درباره محدودیت استفاده از IPv6 مصوبه قانونی وجود ندارد، دلیلی برای اعمال محدودیت در این زمینه وجود ندارد و موضوع باید با سرعت پیگیری و تعیین تکلیف شود".
به مناسبت همین دستور سریع، فوری و قاطع، از تصویر پیوستی اکلیل باریده.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NgAzQhMSu6o3CKoaSGGnRZpK_k2GcoswDNnQIwEG1oZElIG2i9GSbPnuD3NUT7ZynzM9cSP5fqZaxdzizDsD85V1FxGbkRS9om0Rx0NjcZzykYMDX3khsNVHga4Efs5TMGxnmG3hyXEZ1Umzwav5zTzdTDaQ0e2yz-5flYGabqkK-n4Bj0lIZH50fPw12BMqyyE384fwY6gmhWJVdvc-rawNtkDBKk-u2I-tKGfh7xnUX6H0xptpiQL6vuVYeTLBbKHJ74bbSz30arxeUfJayrzh92clIfZhGmT2HBXe6CYeMTR2JfgxBGUWYNgO9OnehvDb6xQMLBG2xqSusxfFUA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dhYzjiNm9vVKwanFEY7zHyWiTddezdKJAfunFJ3R1oCUCEXrWpXRZJOHNVVDyWaB4B8-YQJeOlWIcVFkrTdTJISyLNbToC-ySEJ9P8ynCsyYhd9tjr4CJTtNWdPBrTPC3bY70K9a6W0lXCy1NOOXUgx-VhJaLdna8GqBy53cd0En_ny7gVsBtjB4d-H8bNVACJjR4k3j1wnvmBqCGqPMQCSY3ft5knmbwZIAL_APGAU8HQDtxyRA37Bfj-rfUfAvQBsqVFMNdI0dbacZfNrD8qq5_2t9dD-RUhTsl8dAjpIdnAZfXM0hNd2FCV_0ZfzyYssOJbsK_AZkzVwKADA9SQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oygftG8SP-2PrjipLTgCZcvOhLeUFUrSEfI236F4kS22FimxN5Fv9_rQDYLrnX8bphLaXiZP3yz0WHpzOz6Y6LuQTN-Ud4kI5p2d3e8vkC3R_xvn1UKhdchZR5AhRYHPv15sl660NSSTOJxhLC4ETghrgy9H-mljKSSRmg9Wq_oif2UaqYTgRpppnEdFGyZtLiHsLSe7QEwWq-XKmeqX3XyzBBi8LYQB2hg4FaLSZQsLIP5sXuUb9CCqVnMkgtX8lu96Ph8Aml6CDpHoeNdOVUb4xqhGQh2xASU4hSEDt6Y2HpkXbDVM6NuROnwiWpPwBXiGaFVeIaxcfRcNcE3CrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eX8qDEo5cPfF3MrUsz18yw1ESqWsKBQ-FbBg3lSkeu8J74D4H9_8ujr2cRhdF-yUKJJSI3_WOeHyfSjf128YjpEp1zgo-RX2AhQHwz5Ssyf6izeT2zOLdPSQ3WsBNqPTPaSXvV5GBmODqJgfbvXGdSlWpD3XGbNrwJkCN1uVQreEmaqRvR5PZlgJgJUfYVohUFGqGlhAlpdlbLFNGz7AhOFTaBdpmc0odgz4iDE-QCqWfn-57WDxcwKjbgHLdpl-XaTEqUR98TLPixUN8x6_rwt18nULPa6P6ec6BhLGOj-I4SHf9J1WzbUqiKy0ofS1mVKesiNRBepdc5kSZdcXcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FX8utEOD_Kp5j7_oHDVdR9jIteaXIY9YnzlfO31f7qO1mshdsfDP40kKdHuZ9Ik_l6Q6NP9TdB3uURdvk6hRuA1nqjxlN-3BMbEG5LxnWSONwuujzmtVb7TPXlXFt-Fna43oOTZEjhcBkxHjBwBEQp-nWBInOMT-e6LX9fG80qDI5iKKusq9AHMhJystuAlgOrfZrHX0STVi7MRUZyv9K85iNIZ66ZHHWSdAY9Axc2C5HBk5xJR9_EkuE9p7Pv1_6J0uMrYgbxCEKhvhUqJ2ZWxh4IeDda7nDkEWV2vkydKb2WbgLSf3msAWA4satGiEoHmc054HXmlMWxJODYL2JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه پایدار است، یعنی به همون آشغال‌نت قبل از قطع فیبر نوری در ارمنستان برگشتیم!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2595" target="_blank">📅 07:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BfulVrqQTxxw6Kp7BuAyJN_YiKwEub45sUi4LAw2Muyf0R410zzawM-bUeggMh8JfYFrmn0WQPPCvzh1GytoXe_frxZRzFSI7uFTOwwFOYCv5VhdWH-6po7NkAdyHajQ11G2efvr-Ho0TLPtreyoZSRQE11vz84tCJAMfC2NJMHJYeWkZ98iBxYHMvTeWNuMVSNB8KeQnqvy-VSmQiLKs0iiGJ_HEFCQCYcB403_q7Puh3StZT35-J05wZOdG0d4rF81uJlhI0Nu9KsArIuqvAk6TX966nfjqD2DtkSgcJ5b3mt5vIB440flpNHu2ZwTGpr_b_sF2QDDTI0mcvrnIw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QyCqmD-WkpM_9B0vAmifUypfQ50MAOWKPCyyqtABDyRzs6BfnzlIApGdiGrPKbEZ7OD80Sbx_LD6qlP0JL0hubD8tK87QJKJxii2jarhyQhXgH4EGtdBfTvSc5pdvQr7ijYaCn11PlXYbRtltTYIsLi74pTXWZVsyuRwVHu8lG17fSZL9CFBxy1qyLjBgpqRDAzCpMUPBkLYZ1dcLdzPcI8XHhRNf96H_PyPqpaO6o0JjCytbUCF-ACoFAMmfm8gdjUcNgRMHbk0k0__efaLNKqNiunaWFuXdGexichFG1NwAOflrsPDhFSlbkrvLMLJa1WlwQ1WgTEaZNXOj49eoA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hEggpImaCn25LntdPqoXItw0WmPEU40x67AgyOIjAUlOvSa9xTtW4gdmSAwn92a3UyOavz38WIG5qpt0il79b5GXhfugZwdMQZ0eWsvswgREoToMfgFVI-ZL2wPE3RYadf8VI1d4r9Cmq8SUu_BolpaAEowodrcRc4d8uTRUkpuKb9gI01RL_FFjjwdd1wOReZcL44zBbI2AuFQyHFtt7n1oMJGdDyOzbWwzW38yh_Te_5NWOgST7z-XjMfrh1yNtDCMkD2MSmoUg8e1U0oC_V81Xo-eCHJ0IZlB1kwIbEIJHnUFSWrC90Jy8KMw12hBje20AxVKZBN9qMjn5AXs0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/ircfspace/2592" target="_blank">📅 18:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tJ9xUD2dTkUwrRHICn2X0Y_377HPpVhphduZ0ik3CmwTYmfOfzPYQIwV6Bft9NKOvKWXi4w6t6jdmjWO3cFMXRsCQMKldWNcRYxrUOPip_BZhq6hAXGeSlw3qkwrFtCLPqaCXkF1qRu3fHsGGlNj3f0nHYC08I9j-LDcOLU0YeF052e5BQezV3gaKXfEKTqFXmzRyVIOXjAn1DpVeB26mqbM7_9lLTkJlLr5FGqGxEHEZG0IE62C2XyGsZQaRrU643x9gUDnRdi-PN_x5vwnwz9U68Rl1kDQwSFFjXoNHuv92YErDMpTt2dlUS5SZbU05Ou8klaeqXy67lBUyX8i3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه کد QR حساسی رو می‌خواین مخفی یا مخدوش کنین، نصفه‌نیمه رهاش نکنین. ممکنه اطلاعاتش همچنان قابل استخراج باشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2591" target="_blank">📅 18:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/izB3mxnNmC9lb1CAjAUKe9H9lYSwqkwlrROHr4vq5AzGBrTcio8kSIXU_bequnFbcFm7a3uLvt-qpCmQBbA3En5Eck0rEJ50AOq2E1FUXcu5fUuvxxzcWN8LboVhchkI_XH5sauuJ3vY-WcEE5CcnV1vdCHnfBy2h6BtiepjrUlT3sFU_2YjMxCtFJVIxpo1Jjq8bxgJkL1rxCgwcumaQ2HBCAXvklxL-kBH4EGHmiF9oefkbe4qYmyTaGB7jl0WY6McI8dTrBy_Bm8wdoOvrSeDPYFb0ALlfVz6Po0Fku7gI-T6oab8jn89n9Lw8wXhU5w7tc0qYMSIkdG7nvfT0A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/ircfspace/2590" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AS00hd_KyY0Pj18VMZMerjPV7Gd96AYYYnx4PARsHV8wDd8goANvsCi2Edd-eD659PuYEp_J5IA9w3rlWbcRjT50Oikz4ytvQWRhOUNQZKLtM8kvT3oSy726IPooqgbjx4sdeJz7zMLlOknPprJq5PW5x4xAEU8LFzfxDONSgo6NXNeHYyDxoq4c4Wvpwtkc2X9V9a_irk28aXAoBCYryczsWirf_eK6b2OWBjTTVI57JexT04VpPqqwxqIeavVgABPovAzY3PhRng0JRfFbY3I5xiVQGiNZzSCrWXMuYhHfe3ctdCj8-AqeDy4X-Vvmi6FxTKBs8frnaSLBqeKSxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VqCLST_rwCggMNm-kF6wNU4U6Lj0zMN_GpqWNxtuKCQWYMm9XtzqMjnzxh9y52LiKsIyLVPh0QgDLjwRHK89TRAnL-2OtlYb0_p48JZ85N6P7erBZgZNZD4SGXz5WYMaMbLtZt4NdBgDDtJX9lj36gjhtFvv5JO2OH_Oy-cytlcYAQ8S3chDRaazoA_7R1Ibzjlbnaec7BRYWnSFW59tcmhBI7yX9wtpsSnzes6KJrQ0GugVdZrQ_b3otuizR5zANml8FoHVRGePIKl0XEopFhlzo8396WnPZCBe5X2vlKMOU9Im1ryAWlxTke84wfs6ywzR7m-i62H_mxChORNxuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/ircfspace/2588" target="_blank">📅 17:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M-TEZF8dgES6Ldotn-hXMRjMsXc4ERS5kHcCKIlKZMMsyElFgoWLL-YL5iekMNmN4HmgOuSUoKctS6eqt3sSo1DZopGrj4U9-HeY93Hir2bUIwEcRrlZ-cMjGWPUNsfbClayuagKkL-PQ_CRBrWI0chUM6efoQEFiDUU7tH2OHqLey-3Ty6_1GHlddTvamet2MOgiMdlpWmKW7KlyURpqOZ2GLEO8okmwgDaBUyw6GHkcFdTa64RWxzHrZtcPpHudoHFTY6HH11DQ3JTnyMPZvdKcBEmw4TUHpY46CMbr089ThetyJlwSLzLKdFxAQw4YQmQDBYq35v1yBOV5BrqbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجلسی که خودش کارت قرمز داره، به وزیر قطع‌ارتباطات کارت زرد داده
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/ircfspace/2587" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2586">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TXQQhGZ799L6fLp_CfO15Pe4EvL6hlGum-dpz98cqCD0pOLhFBHs_eAtXuCsSqHWOfV-0nho7zD3yUTPYJDVDGl8JlIAPJmzkbuilZlMzK3fEFf45TLG4CckHqktFzXIzJSQr012G8UnrAP49vK0ctB3bCI-7pyx8b95IVYmWyI6TO-T9MEHwXtf7skpbBQFj-uSr3Ry6Qxzbi7oZxINUuTsIdm7GyOjASq_RRU80gKzlzVcsc8XJ6dAYCVJSo8EOaAXaTjnFH0nEbDyctzotOUtFOM315tkmAlx7XSZ_zgHf53-fESrPWlBAr8ZLv55j_JZeQk-jzo_a1dDLwx85g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور: طی ساعات اخیر اخباری کذب به نقل از اینجانب درباره رفع فیلتر اینستاگرام منتشر شده، که کاملاً ساختگی است.
/اقتصادآنلاین
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dS7ckh8c-7vhoXbHAd4oX-XjeBrpKLt3hXinNVPjjGJEZuMDx4dBRBooplnyv19ujAtKjMJz7iMPp_dxjOk25ogu3VrIhYFBabPyLHIZqnK98g-jI7zouVQFOudcKLkbzrTwAsbHVN7B5vsEZ_vkANeXXWbBj9jpvX0-d5FC5TeSe0KWH59jBBomfHTsHygoebLtlmRpqNBwAiOvK9s1kgWQWqhQLNjpoEhM6Pi1gnOHdR5bcxLLxu6YZ7HbyV6ZQ0svRuM1MpK2zh7I98f5Hkdrhjr9zzwZHYSxj03Sz6yHonKA_0J6LnYCsDGQ_6h57EQ8izvUftCLQVYFlrca5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t70KRdluFSa0h5fBCt2xkCtaU5V_SxJbquzY1dxTbBK9X0wK0t6SG9VDC18996tHnHNHDR539NaNeZLL4Q0jWoO7n5ARMQN4ZyR8HJDtJl-pSC2YK6tCnMMB6HaP2VaKGjICGHv5kTMT2wJdKgCw_RU4sgiDw6FJcUwRH4hmQtKdAjVcnY4XJNhD8DjPX5JRQgIXGnP0S58RNOVV-UW8zEfRnH2OtMmlLvQ8jfAH0C3_XXIxoPUcVkMbw8RKCL9H7fR9IhSnS5a3yRZ_1lknpaHKVk1yC6PNrpdCP8_ZNcXQthFo5JL1_W974Rje-fpuAfP83jlgyv6NwPjsC0n2nw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2584" target="_blank">📅 08:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H6bWtkZMWOZ1LxGyz8a0cQS_RANtEOGYDb1c3cjoD5fJSiU0PSjqfRwYiVZkqZl5UMLc79HFZYxTUETYI9XojKZX-RA0dXoosMnvuq_XtmqHnYEUSc4DmNZ6Nk-54Psea7j3E0e_fcZYhpWGXPTwu5dlEp7H4jIayiT0_EidpODhvTenQ57KUDl9lS2gSLO-IE3sf5OmNRoQmIJXwxngCB1t3hWPNKpWKfMnDvOcFKimB7ZtBrHNqaACZjrtdRA6YRyq2N8eYmeNgJiG0h4TaLDHxDUcms-F5LwbSJ_5nbZSI8lufnPWTbEFb3-nQd0fMfxbGMYnMTT7VoRkIBKy0Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/ircfspace/2583" target="_blank">📅 08:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2582">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BfawemwEcKucNSl7oGgQT-zp1-ScGrGm9wyGUw31QMXfAmm5LPQW8nMvcPefsSFLT7DjkUj_o_UnBfEEUNSYFY88HVvVtA8hyRdgYUp7Tew0BEhgWz7jKrl6UgsBJDTxnfMWVB6gLfAxyiF6YK_ojW1Z1qDfkBTx3-eotYrEgnrWCnaZbwGyVxOX__k-0VFvVDDS3sIKbU8UDNSHJhc9yaymUvW8AkYhDDIeiVpcanqnZSJk9JO_RMquXgcLlsdbAGdo_LnbpuEtm8nuEAm7swH19nppyFOlRaQr3sbfH1UGBUC1MalSFOoM2WrXGyZ01GlfbwHfcCkO7AoSy1MRhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/ircfspace/2582" target="_blank">📅 07:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C1z0cwMwsM3Uq4tuZnkfgt0MEtw1FsdOBoEq7mHahBhHmcxwBigsXIMIxQmkRikymb5d_AFz9_iG1WqG02lHgyrmvuk7Q9f2mmKweqbLY8AWkTIEpGm3ztEO0_wEZSqJBD_zFe8WG8O6eDsF63nId4oq1CnucksdXxBZrPBDeBgDgbuEqGbh2HtPO-OCHmWOsUGhazzX2by3d9MMLq7Va-X5-HVoBYRp3dXHBBnHUBcNxSoMJPiEVtvuSyBfYw5qEgyz0GTH9LGXNrgX8y8BDrM6SVuQHh-QzSMdn5P7O10t0gZrwCVwEpCHlxIDaIWKZgoRgR4tVWXtH1_w8ZDR6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2581" target="_blank">📅 07:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2579" target="_blank">📅 06:59 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PRqQnk_HlE7C8a2HMvOORoM2bceRJ0df9n8wOhwyE1MNP2w--OckD5SDTpRCLYFfnwgxaPX_0ID9fy7VBbmXaC1QiuUGkhqW3ak4h3HtHMQzZoYGkFBj3P05LAJxZVn8IZTnuVX2ciL2aPirzt1dIYaLSmXziuZ0O1CgitXz4hFwL17Rw7CwsRDwI5leoPebLHOc1d_U9Na6WdniBQ3nALEfpgDmE2CzK0CYMM418LYyQ4hyJQNiMBH6DLoRSwNAsBt4JNPSgD4jJTY1InYQzcD-BGeP6ofFdjB78B7210fJIrQXurWUYiGiZVVnBeICtdByAEl7az7_IyRBCPNGTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/ircfspace/2578" target="_blank">📅 09:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JZTEMTGEDMgLNAKrHDxtskk0evl_u735c3QIr-rHIYKYKjDdPir74ignJuCVON9ht13zqJ66niyTY58zUrtyEt-tPTgLM8eGbwWH3quTzB0AEqyWKm6Pm-YoXz0XkoTRn74xzhJjjPgJvaGTOkTIMwXRQZ8eu67Ct2-5Sgk90HLCl0LuRaTrrq7HtTyBazd0srPi_tdDIfyb1nIrKaqjlsa4XvVThFw84N7IpeiyQoxnoPn2kK7csLEe2MWYxFAEpxDpKOdIwTu1ev8JDisvvCQr2HRQI9Wqg0cRoCgHneKyEg9Db15tQfxs3t1RBLNRKH7YPjgId5c6TMKX0-T_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kLIY2Sio4bDVZ0qQw1W04poUuYuJ7niuwkAQGeftivgXRoZCMEep5kLZXUPvLdyEbcDhX9YdXhDTGcdj4tza30mg5Ha1mHxKiDBmlc9N4hbaO1UpyDZYTxxa3K1ihSuu1uURQ3W0w7rz1oOTr45eRKaW9tJbWTwDvahBCS4LLyilATnRSqsbW0YjvqWY-WdLfkMqhErrDawCKStMonVHm3RjlBwGhARuoV6-KJTAokbyuVV2VXgOAEk1mTUA5Bo98wgISBSKXZCULDLhG0NxeM5L0NYH7L13zq8l0U8dDl3po054ZOZVDy3rDZjG72alvmnvF3uYKE3CS8a8jacQWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #60</div>
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
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vw8iGIj5SJoh7uWFXhQ2e_g2_Mu2MSjK36TDW00RJbv3aeB-Np-azZL7Rk03TK-qSw6h2AavASVrIK0D4_DU9dYoYWG9gL2V7rbMcFtYiYDvsmcfHaL0bYoGnxNWNe6O8lVfwa1P95Xcxu8ro3u1kGkA83PC77cA5rtjOSQkQ3xyO6-MtX-OAj3mODLje0_Ot__Oj5lg_VwS3xm0G8yrvesXrALtrLQJARmvfQawd6TAqBgOod9SYacagnsGTg1Mo7pBgk8MuC9xNYeC8TCJXqa7YgAB1itMjBLMGLeyibbVXn9YViLP_arIkDzbquHB6ZeLXYyhc3c9u6VySX21Ww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ezl-HInQVqdVfRZEIrL_Qu5OgSAr28v3F4M4rWh0JHAn5XJydQNdZo2u3NpdFtIuOKK6s59FMhQPZ3MDEIa_E7yIcEWropRiROamNhI4PaHri4BiiTalRS2dLqkdp32ywY3Z4yo_iCx-qFfQMRNauKqieASOMVGwPL5CKqvpWRx7jEDN96qzfRbpDqQgkKJN47n-62DHa3fBM4oBuE3t6kQIvgNvilbp7lxHBWw8cd-_1H1XGxatAcIkNKpCb5nE0UICQS8NxmTuU25z5QeM7NoFLs4pCAzB2DUZHPy64kOK-04Nc9OJ5mGydoJ76PYTozvk9huSf2rStI7FMNNR4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OemFtg7vYqThHDvABDz9vOQMKCw7uSwVonrWQ2ySclHDUBpvmeDzYIhy7FZqjbP9z_p23ilg7OnkfpiHUPCI-rSaLum6gqF9p9DHxiwTovuxCPNxlyyDH-7SGSKiaVNMLL0LjoESlawA6oxA-jaoQ3yCPwxmCZqcrhzN5aqbJEv9RejE6nD_AeGbcnbvrTWwaLg6Nc60JIEskuyKK_wfHHqwSfTFNbABD2vAQ3aNyoBUd-wr95wuUgRf1odkctrCkmhJJ5d856ZeW1HZ5g942xxocb3O2CaDmqpX2b5m90zNBInEbQM1UvUPet4rCray-SkRV7WCBgf7wunBeWrC8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LtXrl2RackOdOYjvrgmTibNNLssmg0lnSpb19uyvyGkwYOQwPKhP_ahAg1Dwg8MdHk1ihRcXw3qZEPlfO3QhPJyKYN6N9e6yC4WtPVjM6wHFndqRlByfOrA5JSrx0shxg1nooZRZoXJKYnYEiGfllFzmULOCRJz8bPw6DxtH98KtpueB_sUYTnOsvg43htOGnR0arc8a2eFRFRy2Ml3OdFckYG6dd8VZ8EyDU0X_g_eb5Uuap6GdLqtiiUTvRUMHCWVssqKjtGRb_UmQbx95s-s8rvlYMH0Aq6Cbh6xRKIU3bs3bbNXRdpuULj10oxoxlGXCPnC6e7vVR49HCIcrKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #55</div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u84qbQsXywzGfPU1tQxFgwav1lSBBFhMn6ckQfrD-bupVE-nuOO7fbPWf-bNcU_w_T7pIST2j-ZOllfSmX5EDgYr4-Yn9ZGZxcH5bul5_wyvSEDu1jkOdg57JUUIjJRXdIIRJEW5Xn2K-S5-VLMNiyZpJW50gVvdj4sYL1hAS5Msxa_InUvRPp372krAiqWt-IUfxwEIqWHPTRThpfm_KoRnlh1O1sMftg6HynygDUJopBpUWiviRtF7qFxWprRT6BeVooc4X6gq22gruiz89c7gkao9xyCxgO2atdXXfhzanLxWeQrAFf3Hxc6FWeuPa01tTXcMGTI8TJrydWegxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZvzmF9luerlNSDAl2wfVSjThP2NbDklpLXjcKcjFfJ9_MFt4EMPTwFe5F1clKwmoYqKUcHhslDApcoPdQO7LPqqGWN4yd-lpb6It2Ol5MqT6YHQKB7wmue_KqPQDA3CsNpxyYlNAsGi5BOOOHXU-N1lmCCocdDgzYXjDvky1TdyNQz4lwo3mNg54MJBwISMJx_OCDb7QFaw2wFoMGRmq9VTmOK8ihRQue7tV225dSKtTWyego0RRl8AsrfgZ4Ru2U_UA-UM1CaDOCjEwqUNJvJaaXYK3Flx1LbYE_UdNI4zk7PqLxsA3csm_TkcVAtVRmYwb4or34gnjLywu2plhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FNZo9e90IESZ5fmXT1oMDXluZ9MBnglGRQlXVvwqvR_C4sxwP3-8b2KXZ8Yce0ZHGHqNaobi6wPOpfoCHBKzCr527neUO8rP48-0i4VNlkiCNi5x4zIWzgg6rTu0Y4L7nP5R1I-a9CmX3kID0YjRqYpALjvExRpraSxPCBqFkvRn0mmQvpaETr7BQCskkhyD3090vIaB1sl-b2L5f2PMFFOpx8tTXRvMVvKL_c3b9p0xfD1IHilG7sN0w-MO7JK1lAZMHx7TnXwGtMGk89x_XyklIDjtQ97ikNpcSlrY3ApoQgkEFdlxQEWhaktwX7DQds8NG1JgcEdX9gkOg1s1eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L2i7UuadWFYWYlTo16hRgyGnFy9RK2C3cxoHGvM8HqN30XAOEFDhZCgK6wrgzNacIPVo_vsAyN2vlAyXiRFqXw-InylneRl_UyPQlDY-7EYo3R8Ei5qbmlXTaBCuSGKyDn4wyDHJi9PmUcrZRMsIwjbUSliO5wgzyWWvAbfQvbL_4uvGjvShR1Hv_hetQdnmbKtqLJqiqvfxWnGnD34-zlIJboKRzCP_1fKDMFZreoTYg6t0dKmM17GaJeFxgIVdOW-bEtYhsy7lRrMFYpCtC7Hds4dx9QL7lCFjDTgdckK7El531rwB30DHXnoF3Wh_d-zL4TdJOapFvLMgeu6tTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H4MmmuwS9IZ2OtnA4KneNE-0drhYyAyCPdH398OhaVe9TDwEI0CuB6pJF4aAxh9BkEy96sKOofXOlWo3UFasFRbvCs8mpJVCOqZzVAFVb3r76xVkDxAf_1Y01tS3C8ORmrl2gz74Te85Ysw8aIcs9mHcKxYzAvEq7FEhYnzsI5Nm_1y9gTe0hjuc0Whb8jY7Zom78zYMCkpI1f_KYvUcTOLVjZ1Y1NrsNX_9uTKOyPgAEsi98_MjtsCjuLHOtm-1Uzy_Lio_SPf3KOkCdCRI4l6b2AmtlgdTzxB0KGpnXoSAT41Fkny9barziONuyora5CdO-eRfBqtQQyw1rXujlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FunwgwGs1QKixHcspMpaQpIZEyLT4L_B2TAmdiYq1G1U7NntdSawDEWUMF3Di-FwFDRf_HKXmhQJZcF_jfrEMYLRbokLS8l06fKZ_yU02EiV1U1K28FhNjhsLMMgK1Kg9WJ3E1O2XYzwQP4MqwvspmtvG4SRArXxYxsA_0Oxl3WkbFyN_I8lxsYymaloW4z82yWBNYnS7bs6WiWktXuI-h5uL0SbeMKV2j7-Y-GZTeWqa7CSxfLQgFbI9JwuV4_4OOKl2nuwV6-pTOsM56tOfscWnKxUqN5ElUiHBA4XtReVyeu2rOojOrL59LNvaWUVkIcR_D7CfCobvpBN6HLWxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hvy5nFFmpy26dSxk97Jd6kRTz9g4hmAoSIJre5aMNwgH5NQFJwdBMa7TmgE3KHVavx6n-AP12vIaK9dhKokHgueQ8h9eTjT6HAskpTkF3bSeFqz_OFmEHOGtrIZLnavdYcYQDfzTGWjNeVowb_SN9LwaapiUh_zZNpBYrOmAlWgiOHd2EYIdsddhHOBRIWmRrjSxOk0m9ixP7byXzbbq6rlOttbnXAgm3wItatO5OpZS8qyZef5t7T1zL3JzvvyvmwfABssFDoPAX0wF94VRlvruLM4rzGm05EC_tbYrMeuiSuttXZKN8bRASBCBaYirge9C5vg4vKfwtD5GxDVIWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfPG2SVQrLb3o7bVyMPVAwaWeiD4stWsem5FSQHdcgX4ghtx0XAyZQEKCdC_6unaWkuxe3E8YESIGlHaIxguRbiPCdoQPA-YlBlAsAQFMjlSnCyzI-UEDHPZY7g0NF5dU1YGC0vkywloaOSjzJKEjcUQVN71qH6lp96xM-z87beQ_wfbsbIsVVCrKDjYcZ2YtsNwRVlQoYNZyuJCjzKb3tMI94csNlXx0bS48Rv4RJpz4sMMGrNEiTSi40b2931FWQDv2S5429Chd8idaPCcokvD5hZ6immBpofHJ7MhXdFCVm0gK6CBAVZuZG6N6lQpnXIEZ2tLIfO7LLcw045-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 37K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qu8883aj9QEoUE_7dgGiHPRca-P8WXG_1VoI5UJ15j6erhEoM7V7aLdMsASpmkrA0zozlEy1uA98l0rYL3tYc5MUquDq30OebcoFY6SERBjuJwtYWvrTd0tN3OvNfNc2LIDdhA8vCUyP6VUt_KCJoO2TFXx_YnB5RrOsk2si19UFcwWvvfWB7_46ZTFuVG_qjBAImk6X_KXdNji5RJkCuud6F_injevhIrYsYqzblPBc0HEXu-2jorhG3edvC_vaOxBs01rJ5EN2LA2UdW-wt5SP9nrlr56hi39ur47bGC8G1dSps4yhHmDxUenbHTG245d3DQ6UqkuBOZzW_sggxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J9HM6E17SQuCgYO5CMiPTd46Bbmxc1U7vOjburWU7yRvXDbuyZjpiaSb3A1g3k67gbVbGre_aZhCsfVVA1swzq17GRFQy9D69fUnHfV8l1TvTumW-OhnGMxW2no86h9zH8nZTah6CGgrPe0Jfy45LItuernza78F6nd_oSXc5gD-xFnLHodBI79g5tDNx30fHFhOFelEE38ifGm8gnMAu56mSskp_8l5ZXL-OeDyRpBWo6WKAG4vX25En7JVNEID65qm9mZYJ3Aa7Yl_7UR9kki4_lFZuDF8ghYBYZQkjU2BcyW-DytgQ40JUSiQgr-GqIlSS8bNP0VKhbUGM2MZsg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #40</div>
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
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=TkbF4ZvrGGMxXqPFunO710FuLHFzkahnUnH-ISBrmLrdKAc4cr3NS-2lGdFGi9Q0K5JUhD76fF4kuhbTS3-L31sKl2EPKaq64UxkFFwnV6I-OJVa3rZd131XgvppRljM6N7JgQ6gWGXnd1AXx63RWd15EnBq-09xosrueAg9RYprjSUfK0ty7PUkuakzsVW0mYrI62h-xMfuiAyBWnuna77LorBP28aACNmbABzN3bN2JN7QizBQ-aLDUDlNAdSdtmTMaxqbxIL2p5kpTbdLkQyS3We9mx6Q3txLIJFVYd_GcErRD6fJSyVdC9oy1RahVmtolWGsQqWqBpvcBR0l_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=TkbF4ZvrGGMxXqPFunO710FuLHFzkahnUnH-ISBrmLrdKAc4cr3NS-2lGdFGi9Q0K5JUhD76fF4kuhbTS3-L31sKl2EPKaq64UxkFFwnV6I-OJVa3rZd131XgvppRljM6N7JgQ6gWGXnd1AXx63RWd15EnBq-09xosrueAg9RYprjSUfK0ty7PUkuakzsVW0mYrI62h-xMfuiAyBWnuna77LorBP28aACNmbABzN3bN2JN7QizBQ-aLDUDlNAdSdtmTMaxqbxIL2p5kpTbdLkQyS3We9mx6Q3txLIJFVYd_GcErRD6fJSyVdC9oy1RahVmtolWGsQqWqBpvcBR0l_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kdlwVJrKZnnVO-NNZ_u28-fcQt2W2ttKaSBPetaHPp2DsqbRHZWdBureKhFXkwd2qwNULFkbSiWfe4oNcxdLms1xKhB-EJxLcrsmLmVt0WlhMqkDO_Ab0Gauvfp9iCqUXJFT9BXjaLFkZpf2NQ3J6-rykq0w0QlTVk7XfxyzuUrKbaPnkfsCEsH7h0cibSeT3i14-0kGDIWJTQh-HmhPjN09-dg0YS-d6xJbCVt8R6jHR6_FqyyxGbVcKGOpt2cndRbW7v2O0Atdfq9D2jQypM4AwGFqMHeoiyITgeHkz7yl6MPmQeu83kwriIdmGeU-prC4gzdLY4B6GId9onJovQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MaFbF9SHF2Xg3RtHJlLreG1ZznKiOBWMjkbkkg0cNYo1hKAqmXn06eck6aizbCFj_-zY0P4pK5HwOARaHI_VbobyrvjUZk_XIxAgKG4CaQTW3g_e3mKYiahLG8Qk0HFCOMZFAO31q373StXK_BS2gRqs87wtwDN5s998FnLRUSMt0VS0oMj4X5Qt7IRRQDFEOB7DZHWndKVUz7Gh4qnb0qIrL3JlVh6_LcVHaP5tbaC7lY1lKv9lSZ2_wCf58rgF8GhbhxlwWQCaIl2DL6nn-TIYgm7pNI0Pfqf3hTJDkoBhuVrJTHGOV0nbAMnjjrkEboJ4jkLe7UAcRRIpgYhcfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e04OuNVeQi5IWJo7Z5q6Me8lGHWg5oGx17wQGYDzkmmTaa2UuGXw_uPhLgg03ly9ad6sjTuQ6swBnIkvO-1BLKwV1mHWs-wMcMh74nRCenRvKWiSXFJ0kxPLwz3WlKlFt-Ug9cK5otDcHmOW38xjboUMj7CnTB0kMRvkqEx8_lkeLvzTICPfxuIYIYvZzc8Iwyh-X9OVHKhkCDxJP0sDjgQf0-nuh9IYD8HL0WXooGdL_FcSoIi5Nt9B_KVgSke1mNfWAOkytF7VvlILuDgBXX1E5-ZC_kA-x6EKh2mEhtlLYdL0jXSK-7cBHm5GVcGzF0XmQyc48gbcTkyisAc4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rPlJiPghtnaFVqpRSD9jhjvdo91OlyDfM3XSt1KHDSZC_h1eakC0vxz3mpDORKtnowuN1awvEHZbBr0Ari4MFGBkhIgErtrhytP4G0rFB2nenGO44j0XmW2iBMZcio4lhub27GvthvQBHJAW4e8V-a4iCJzShPwZqev3DIvG0zfyC59t0NO4dzkdn2EeMrMxE5ew0O73idWpXkCTxiA3OvU56vR2Kb2R1bHtKEuzNiSzS9CBT47QH7ymBSg-avRFo_w9iG16A_JRmUcnzNZ3My0rZRnGsyiz5CgarCWI3DiBDh0WM4796E-u_Qt4csBzja7vhV8sJKxToKncH435RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrMLXPFWRJAQBtwvotTbESg0OroCW3si6t6d07ncKUwfsD9oRiEWs5dxEH-YnIFc0bjJznLmZqQSdLaXCopROU6hZ9iLOrwhYJreDbn_H7gT7x6F0YylHhBAT715jPD1kA8TztUnUwhV6UXTGr10ll23-696MCJPm8SDZ91gXG605VKR9yHZVWBW29FRGaXJa3QCL1h2IqHkXxbn5CwAhfsqnzcIlnCuvkjf4wvgS_jRgjQNeDD6bv6UkThUos0eGETGBU4J4kcfZJjtuKI4Ouw2vbb2VfgHEpeYNZEmQKwVU2oFlHLl5KeqCSyy3PwMnN1ApVokZfYPAYIkk-xGMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gH2Y_iK0lu4z0YkXx0PGIuiEo40U4u_vOfOZeKQp-B1dWP2z7epQJsN4IQqAM3ZM-NLYIh1qUWjKeD_SmYuz8c3jk_3zpLjPkFkewwyDjo3iDvLcMccG4N2-nyhNqftdYBRjqXxYxjbu1oeLf-XqSsMvDJ1Sz34-zzAmRtS5Z0vN5NARyhEoMe8V4nI9YSZyL8WgqK-RDZz9Ks1nLkA3_wUnbBbRpobp33VQ4zg8JvUDOgdUU7SLZUcHQZYAQtqBj3vqiyxl-MFOQEU0LW35f8t89rAGp6rvA0zUM9PcNqB00KRbUXSdKDxEq4-4DWkcQOqAEwVU8FpxoEDWY6i-XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aTkQq4kI7TmgfpF_hA4dnrlssp2yozeVzZ4nPWzZGytwx1RPaI9m0mj2uJKaAkIgAllu6-YacGwWdr2qdMg6dYFVYPf-mWNO1YtUJleZFcQ35Vz11nWe2cYMUFpE1ITpbNCqrAPEtGuEL9o43bez_tbshe6THkXcdbM29lc7Bgz8MGQ07pFCMlK2SrFc3xwSyl1mlQVzlTqoRPi12yeYbUSl551U1Nam1TuVYWzmYc0mliVm8A3QFRurEOnH2uHU66PSqJ9IYuv68gN9o7AIdToIApXBx8Q0JDZAuRlJUjCT_ug5FVAfpkFtcRtOYj7GWLt6ly7J7dqVruZHKMWifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZL3EtfKcDPQ1vpRg3l73UMtY1o8P4Jb0gMrDMg28mTlJf_9eOsM5999J_fg4cI-ddziD2fRaaD9THZyE3tFpE-9WjAS7Pcs57laQE2u64jbWkkrxvAMDKoak1vaRFbeDea_UCuyDdZecXVlbzNBjhmGjUpbXvNrcnEDRiuUC58-45BnIYk4zZvQaOJpHUwwgY0FiWVE6T-T1d-OBINh7lvecDYd79BzYtrbs-iMVYqXhLEb4rTs-WzlviM-MV2MOn8ftjHyLCZ1Elq8JicO8ej2BvIv8k2I9WV_HrE_Kc36ZKh2va9SioWi30U1s4VD1YXWiCdSOgZh1ySRHunUhGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d25_-lQ4f2w7rstXLS2R3kA5MOL_x3_cbbqbV88WUxV1IE7MjZ-ubkpoJ3BDBfXcqncqCgDzBHYFccMIn6i98tI68elxHuXIeT52OKdIpXhw8gHC6vl6sAHlPDYKApkAdI7etyAytGl40i_0HlOwS9nPcFOvkBX8izHXWu_hqtI_MFMuGf2rgE7xumBBbLlhzlEetUKsclSyn2efXnao7yGvuVEbifacSETIxZZRsjNXJyM00ePJWuPUsdj686gD2yX3OOYMG7GgECw9qVeyQqde719ZxKbEZBJkR8hNp1Gc10a2gfTeZSt87otRt-q1MW4BCNjDJUPI78DoWMJ6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DuA7AUu7N_ebUx188_Sm5zzHb0jyxNCIxfSF5WBq3vFalS957tV4C3dhKX0TyS6Xhf3LjkLVc9Z6kTpgJIgjRiqV2LRCEoVXKfNAmSKT469n31i3gXxE6y39FbPdRJ-Rg1xg4rH8J5k6uH9N7P3hhzchzs28Jh7opZflIkm8xpEwviEDvvCXmVwn76xhl7k-8q-WDCkwoS1Nc0zl5c-xSuAElDKp2s5qgYxJfH6g8i0XZqEWTI005vDL7NHscwfQBkLOgF2_YFcckX0_ucoc0rJ1BAUSKDgtEPx7P8PCNjEko1XkJxWc3soCsIipTjHtwCqUf9Tuf79T7bU6xhnsxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vfMI63-3e6P-jYEJO9VbSrsuXpYzJ1y0gtG6vM5gyMUdKBkCGMiKrZVESOO69UI79l4xG1vPYNffL_J5B4H3UXJVYrHoDGCzS7QUdzrDOu1ej4tRUIFeNxcGGOxeayMf4e9MHPd5yKRGsPc8nUeS1CDtDmf_HAp1cxMC6vZvQDjGjxLFSu0NKrFWOAP1QfMiCC7fH5wgB-240EtJBlwmyLo9jPQ1pfqNW1_laejPlRMkolCvMLP89G54P0PAe8Ha3DzgAOdvbq7qe8imZGqsNIhsm0MYG6gvq541-_RJWb_8wxo0I8CqhmVVn48ihGTrkjV-3Wz0PYqkwqS4PSpyQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lGYbzteevNHWm4R7WPJMEX4szFhqiNjUJ4TL_SrMr_6tN8wnMUyHDG86XxtL--KhM0UAHVflNsbuOakqbvGXf7tBONIEKKt-ixCXrhd2urPKJUI3qN8hchNRUE04NPdsPEGg6zuWALFqmnUZAfh09_cBkK0gjOuzZNUjqMe8RYQrQ6G30yUUKYEQkMrtQuleuaDiHyC0a-Kr9VODdR43AxAoFnRvk1j64k3FRYId8ltm9TP0tYpcHNQ2PmAV6k_HfTIm9m5j-6P7Qr1yPHyrZatT10HYX2_e-HKC0oTsMt9WhU6FtmBaQqSBt1ZNJyXhC2j9sQxC4BqPE2uEC2cYcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VV944Q0jQndyJfTjJX9pgP_k9Ep6NUpXt_ls0vnPDrbHm6nG_CSwPPkdUuQzAUJ6XbOX19wCEMBcuoIcVtqpxcFXLFYe0fbkIv7IAeCu5ZaIFXhL2ul-wJQqTMKhj8cmpb53CuYYnl3dbks1cML9JfCFv62xE0bLn1cGJJf197CGSrcdaz3jHlKIF_l7HBHQ339ertB2lQz7yybUNx4rVe-Bz0fEjvoH_R-exIeg5ERHDxHhyrsRpwvAbfNGgoZWgdfITazNaND89VvAGHHB3VSoTrLcWDcTLsiAvj877GE6utXJODnXv8POUPUjq11fBSdakJRYGIbwmNsKOghFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u_0OhaYIDVZ2WIjNVzTW_D31DcJgShmYcfnc6cJUoYl1nw8CCh1RQbaxaCcP6tfnITFr0AYvdtET7fyR55FYzK_aeiPGHuIv9yjTlHdPpAsa7si-lwNIymNuVsmVDlQ_vk50NbR9Rv8CTGT7XnAr2cL82wo--gnP_XxhmGrL7ItrDSukNUi993WttfelHU4ni6sYN-GSxxAPmNein9A2fdIjRPub_MQDfgtF4eYPQS7__O54fHPPRjUuu8o6o1AIl_elwuibkO4xEcQbDvwR1PC6zHwbAOhIA8f1GmVrVvuzZXH1pCWZFboMceRZE2EO_GOLmNFoddx17q2M-2Mltg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NM1nkMYaklHKcol1N98M1ujM4GOacnsz4X5x9xyqbjy--jhCZprCKd4C5rGJ6AQt5vSvBzoMdlZ7_kseFIsJiKHMFiGR2YkNcjPclKPjGiU_9Umr2HItccbVMzMrGPT2coPGL69bciqea67UP4HnAzobHjyunKE1e6hPEU9Aiu5IJlzTmj47cwJyFbM67kXmQBA-w08-6EUF-FZGM9tdq7WwzmW7coT04v9KEsnCBg9pYOExhxIneWy_3JRGiYwkKu5XMsMMuQjUGeZ0296kNocQw9UmOWl8Z3Hq0XQExNZ3psT63k-QVSHO_xA0_yBDbXTd1WAA88sV1WxmKvjA-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KvvZ5QNBdoXNpZyGA-7DXDzEy8oWIV90jBSgpKpnVUdJ6AVWi-YGLz85nMkOe0y-ZCyLgpvnVFtpKrimIXIRueRy2IqrinwSHjdahGv8OZkSSlzbh0P8R-c-4F7t5fNk4VVZO2ep7sfYCrUreNj2oH7QLJJj7xi2e1DpsDLFyyIFNRU_yDYWc0iTucMkp5_xF6BxiDbiUPtk7H1Jj2T5l6KRc73MHpT7I6PYcxoDc8ec_niDedVLoLzDDvA0JPgjVyrVWA7lg0T-ruj1H9eZ9O9Mum8SLT3_fJ__d_r12h36nKjvycm1-AiOJQbeb_qSxfpbQ2z8-DCR2KHDeUJcrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #17</div>
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
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jD8nQeSUfgLFAygLjIp0dTSgU6DpmFiOESQnKelif8qJN1a5IMaTQISfdcIilc5zo9lqxKkRm7TmA0nxBGtfWoZlu2gB7Wua1_VJ3Z3Sm1qABNZnIB1uVOwUL83AXMEEJ-U54Ak3FINuze7udCpfet2i1zp00hvoJYIqhGsWahSqcfH3NirbVawkHWrZVdnoclnI8Nfbi10IcmKyZ7R0U7XmKnW50U2_5QtTAKZY0GsPgD4eSDbdbRfyFJ0hBFWqJwcjWGkBz-talusMyybmiLDxKlVJekk4RpVNqgHlg96vyQLFkF1n82D8jNuHGnE2sAQAug0NuAvbvqot9AZuqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FZZ_2KoYp3R0WfTeT53iuGvyj3QKozMe0PdTlmkHJUUUdCMnL03gZ3JQqO9GTGk5MJNWxJ2G4w3d5J5SIJHwbiGr12OpJzH7DzefFkU3Q23i5Ft3ZT_yGwsmStziVC9cdKcw4S6lAPglpXE_Iu35wkvRJU1u6cZvHCvvUuOLsONpFVJ9Ersx8auK-Y6VIm2-JjiqlUaRqBymkC89lNtRvapJcwURw7iQBCeQ6Fvjwz2eYEk87pBIE60WjOZAGFaNQ3GkzRLH0JcDOkad5VzUBAkLD18jJXw-9KaM9Poj2FinFCillj1zgzArcaNWygZa26hOlxW911hQSZIJKjIP8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kg-4wuMusn7Fa-R_O5iUCeU52ncmTgQ1GYkc0gztnmKSfoVI5ji-Yg4BQ76B93hcI8JMXhUKMS-AJks9yuuOi900gvSj9-NSa1cJZwFbKd-n06CpdP6ekfYHvWKv9rt2dWTQ8jgcZYChUCwdVSiTYN8aqJ-Io9w4iGNMfmfR2_cZwuIlbTENyyiW0braNkGKKVE0dGzdA8O0tyusebZN3-SdOLPcaJqRLWN86p_uGDxooW2lWsBYMQvg8SifxWbBdVm0uwK8LiVJeZ_nwxDx5_lJnt8ck0ubMgiZmaJJR2PUxIlRHqeRtbzCv186fl2empPA9AuTVfUT4gZPeBLBlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #12</div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NAryzvYAlqB4B-rmDZN1H8WO_IWXJeLbNGLDVJKhQ7isie0N3b2UEF193PJblP5-Kv8MGaGqfdNJNAqTKkXhlIyZgOZHNStB5cyzygD_7G7xpRUtrADK0uH3kG6txwPhphbndwyMBi6xVNUYoSfH2jl6SNAymqpTmEmaW1yi38Y4aw-kX7JQWQ4gPvD_M9Rb8xUnt3BJ7B0em6Mq46W4tFNxDHfl_PODLY5HCbcpG6CdS_uOjaFatm4ALgd0RuuIAbiAV9mT9BbGCaAZGhXAS2rPFuu-aNayfLqMDpqmc7VlSaRvbg70A66Y10K8uolpmbQPId_d6YBudPkUIwmYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nGqDgUfHHy2tT5ZymjPZ9tU59Rcv4yDPvgPL29c9gYZbKHvR-y6b3k76JTAyZCGthwZlQjZtmXIFfk_oSaibacGxkoysqWKICmfJOEuMx_LSIzsGjcjwZ4qPp3wApIgujvJzSCUXghk0wzD2cvpLP5T7ETnJpixfpdAclySQ0gwJQ_1hN5ohaXS0IBacww02Z3EyvJUsPt7J-7s5eOdVlY8Lr46pYOl4ze4KZSSz53CA8b2TruWQCz6330RD4oScnkLhcw9pzN2YQBygPeCmt1oawAWXyjXpKHJtcxV3VGtAUpB5VxiTEK7MQwNOT_B7p1uymQfrgVfnG5USD9ezvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fRFZckDIJv3DaW6HhYthDMz0erdPhQqm3fuTvUNYE1zIbkqu2_Q7S5sjDJcFjjii8DO_qxfaacpox13rpyne5O7hw1EYS7Rh-dfV2A96o8TOLlNinNGwWVVP6QXgMQiN7NaArhih-ZhAeZQwldZoLp-1J4CqPdd5f2U8_rjBK_U9p5Th05RKWjuUdsDHIrEdkid62eXoP4QqsJG8JdoEY4KHsb8jyubo7sH60RQYlCtrGGsJhtTADycFjNqS4XGBjOoBMpSCFhgs8iGHX0ucO4uhvEVL74kNFCUQBJMjOEwKyLaS6k2sR9u9ATMRVF5mk6QkOyLEGv7qvy4h9iqXtA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IOydFhGdxQyPGTGhtsc5t-sHQ-VO0Vf4LF2ZYvLxH_Cc7IA-jJrEHp0cMovGjRQxD0lOSD0hNMYOeyScSbbtQSuEkRPXH5jctqQCCi2pQapcOPYVQlfXyqdjOl5Yz2-HLdVifboUiT_uu2Ylt2WlF8bJVPcwe9Z5am0so2Knwe0W66tZsWnK92yGBO2j6u-JeXUv_iQmTRvlH1IySRGdWEe8hPqFppQ-QNVXg8Ye10u3ih_6dNk-aRLYN7f5om90L9Qlh4TP4ZdXkkCsIBRGR0JnZWl8vR7_t2v-Onsdh4xoFiCt9b6IQEzp6MV49fysoHrffSMENp6J4KPKcDb3hw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T-M7iKCeHYlFICuChkiw0TUH20eQzY9kIf64Qanucndpr75axSZNkjrJs8gHbUcUhy9awquC2sDxxKRZXTjo9h1J_amJTmlldk2BHhVNHBMHmoszJflFZBBpykhcPtgpdh_dD7DUY-P-sfE9v7h0_vMK-hLNdARdfVYer5YlLIfU6sPQldXFvY2ouhs19PEOhFlcKxhBwEdDStsvYTtwKV1ka_u5oXwo-PA_tAWqJiIlwt1A_uqWOYCdIT0wk0-U8jF7BKRn_-mfN9mFTh59RVtKrkLTeoiFHEI7p9K7Fa7UY1MAMgzjBEm0NuZeGAo9Lywjo4k0O885tabkbAN4Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/P89wlWvQMHWhmje-qrIRoWRq0u3sodxLwbkO8nxTb5cF1WfLj_zxMYGwkelqSWMw1gaa-kwijXXe8KQQNb8PCS4Da9pZogQxZtzyvHRmmVyv3hsSqr0qqZeIWE1UZO5vf-vuU-dZq5gpF2s2SEeGwosNvncXR-ZP3Sl5zOKrA8DzwyoLZSnjRLxgHFMOV8uMul_ZiyoWfbHn8rWjZJc2t0SdqbAdE62HO7kcPzG9L02wVpsS4AzT3dFTI7_laGC23P5W54lLGy_fEptEg5hm3xtWq8fnfZD_Ygptk2nqkLrMSSYRBjtNOMttZ1b9ZFv8JA_ZlhtEXmww1ciV89E0MQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K6HHrHkA5CQwJ1QE5rJ6vBupu1TLKidq_yAoZPAbIe545TBQkEPRfLkHdlZWDUe1iW9gd8uSGgp3NAsbKq-Wz2cJvuDj2nXRaxSGIyGXUwN9synhqaJ0m2UA-0rd9-k12BWG3JnZLE2pvH9aDDxmva78JCEnZquSdX5Pzx-T2xjT2F4681aU0W_ZdklDDJSltedlp4NXCo5h4-9NwUbN3EZ1xbNNY7fdDkbGxsBblnXMKLVhdDZNJaUkthwjMJFlj7tfh-7FS5Kt21qFhJYpM9RRpClFXy82BuXfBO0NFghPWbdWe9Lm2BEl8NmId56cMe6ABbpmBNw0KlZ1nNWCRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WepkX6gMjUmyc3HxowldsSybdDK2u54D7ZbuAcxirbLSR8gzO-WNNQM1xZz-Dji1IQRTDe0CkCh2ysiGbnxPmu9Gdl3bvDMwrcVTMdU5Pjxk5l1FCqj8xm3rBJ6tsjNr9LzEltG3mrp0_NTCeAlaMdGU_l_n9Q9RzKxSs5XYJ8s_raaGR8YNlqdA7GS4o6alBrlGPpB-bvIxIhH1giZy3Edc3KYFwgnV1mpe-Bh20cMhfAz_VFQZun9f1RoxfDsn_u85nbOOQkjajJs5tgC-pxrwzG6sMzcP8oLKYw5Lljaokz1_thzeAp75oAdDxdU8z_gfKvymkRcnaF_oN2wcFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TZuOBCSfm2VlSXQAN1R2cRQhB73DOUuP4GtYUOSX4sIMQrp-NSe52ptOhGITivYz7Ubp-JObZEleol1TYh-j4iJu33-2oDp_gCl16r3fUjqGSWwzMddSU-g7qpKswr9PkKtw8ToCckch-fSRdXK3DefrljRcAnyoeyjBu6VuGbmT0t5jkTXHYQJG__D0cOtwVOhpdUKdrXor0Znr2WApaeVZsCeLzPlduKjA2ZTc5F6G9l-aErJtHQRxMuaeckG0qP2nSwrQ9qjZ_gUh6YM4wVXpnDy1Q-Xy_RuUNyuayAejZe4p9fr4CNhJo2w89kTOKdmp7lPyGPDSQE8y9Yg0mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ifXcIJUK4gfBuE45yiBQxvsZmiZPuDosOuXrVhXn6OyUfM4NrVtNNuROW_T0wNCqNVIfwN-zU3keGcgOM4GZzW5MeZe5ffin2jSB5BF5se09astv38ICDd4xXaEe4FVN2aDMZX9F9UaYJRp0HluW02kMpssDrzB1OHLWhDiIM_apQSOdxvVzrBrpU8awyZBKrN2-nGhO1GOR01fINE7-FEL0fkrUYKcpLCjvsd_92_txQHgx_skCve8IEFzJCdFslaVcMztr2vnWtlLaXGzEIH4rDUT2EuiAMFdZO8YG6wHmbBkEkaQUcYcsHNijPGAmYzRz_A6fu_ZO22Wf8NghBw.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
