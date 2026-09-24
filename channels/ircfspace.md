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
<img src="https://cdn1.telesco.pe/file/PSvS9DZSl620QqK4dGR-RX_7nxf32ydhw62-5AfxJGuhA3RIps3lfjX8YcsMLmSPODpu1_gPp5QGfI3tEaIAmczzOLYpN2xtArB6MlK0phqLHrp3-uFc5sf1XnNm2yU0Ny6xG5TnHu17Q6qDnSL468o4Jn4uQgf82VArF-imNDHIglOglZpw9ZihGtT1Qf-5CfSfo5DmEy8MKQDcyyueqGTS15-d4KTwDiF2fQq_wXwXPyKARu5U0yPjgCAHy7zy3zx0xsTIDXpLPKyN_Jrx1NdERDEM9h3FrsenL-ZDAgnV0S58CxY2hosbsyaDL5jAKRDiDzgbD3QHoRvZTvNEtg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 95.9K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 14:17:46</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/ircfspace/2616" target="_blank">📅 07:38 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/ircfspace/2615" target="_blank">📅 07:34 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/ircfspace/2614" target="_blank">📅 08:01 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2613" target="_blank">📅 07:52 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2612" target="_blank">📅 07:45 · 31 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/ircfspace/2611" target="_blank">📅 08:20 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/ircfspace/2610" target="_blank">📅 08:11 · 29 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/ircfspace/2609" target="_blank">📅 07:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fZAS3wdASHFHSMVbyORWcXiug4_JvT5GHeH4vwZH2-Psw0r90pHEQQIvpv94g5neVbuqXIRNpudiN8k3BxIhGszt3qeP0g5WW5eKoVRQj146aboBMmZK9ta22Ye_NNLwh5AHMH6Bb4J5OrjXcrqM0E57ZgWDH5N21BRG3HWJaEIEqjfkCXH8LI6NHyO3Mjt4KkXkFifqNwXKtGOSWkeBoIIYieSm0DSsmGsx1OnbP3fAGwKN5pU-KxpClsDrXIVbZ0INoED4dB0u9PGIqS1h_sUI_cxb13emy-9PIY0XKjt9nH7f7xnoLGV07v2jZYK_zIdYWBwkkfU4f_eE09TB-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2608" target="_blank">📅 17:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OCaXheaLmXqGYy1CSTepcDUeHb1GD2el_ku3zc6EEBbRq4cF1LhzfhsX2rKwcsesV5Zn7LILoOvDP78rrALv-iXgpjAF7rzukg6CJpccc2Fhs8n4OiANd2eUqaM2E47DawCUsDvQ-nro1rGrqd6PNcMpL4Y7XxZakEyWp1-dTtb2frJpxwSSBeHOqpoQhTSviAk9EvZl9YlbkE56ydGg3-8BAqZpcCxJucYE2QWUjASWW53dZq_DUY77I9W4Ixz6WZw2eXB_9FYtel8Qqd3A6q-fLGTPeqx-WibRt8oQ8EB6Ar1SIUOi865vjfZYV-mllStImjLxqTaCmFfcP99atA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/ircfspace/2607" target="_blank">📅 17:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SwD1QZnI8cgU0YZBVATsFnmbDZFYS1ScqOK7pyREnr5fc7HMSR3czJubWx8Yw43nkkD0spgOrsT84_M4mXvITw426oHiyy1nHW3XHJ6l6mPkHugktFW36_NBCGV5wME3NBBn0fx5zrV2F-Gsm6iDYZ2GAHzDYZKl5ek824OrHWmvsk3k1yZeewk3quGVgZaWVa13n_Rlcxg56aNvlg0BGqmaRSsQZWQnTo9X1FBc-ZQAHgmo_cdjdiEWAA7BhR88--9GFLR5WS9-6xdgn6ZJO4LaGYcFOxlDYdS_c-SZyHsnVmKVIDxAqM9VxRq3dnttgdgsDbJCuD_Fd1NA-znYDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2606" target="_blank">📅 17:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n9uZ-51gNTE9elNNIW4TiVbE489S92ojljBlq4fWy1Gny5YTYooa7MRJhki4zakNYFF0A60_PWbfhgtvX5K-uPJjPOKP2zvqc6n-Gact5Qq_eKzJaOKPS1B6QOMoLmj5Avf9lXox7fKuQGq3UAWd4SQ6R1_hYuGraA8Bssp7cwmDup-c809aG0lqEoG2SKZFLXM_KHTnInljhxE2cfOmsdF5kArf7i8BkbKNF_rV9QKFoGcAetHsuulNe4Pdba9nGatNh0sENr_yXDikk_VTiKTVwFaDxU9GUVbdljOfuKB6f03zvycmW_yaNDrTglw-kioy0ReO7iQDAg5w6PGWFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2605" target="_blank">📅 17:08 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/ircfspace/2604" target="_blank">📅 17:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rd-n3qb16Q2Nf_52z-0rcquxJBYvXZ29-5ksdJwvPtYAytl9J2ZOzqvUv8SQjo3HIU0Lzd2oSiW5MK7-Lnhd8rGpttK0TeuBN0WjpfDW4rf54PEtMqpmlwCbAak2kkgLMcaYHPytdZgA_tocilYxh8vUPXgktK4dVS8ZraGuWVht-MdZfbpsdTp8T3uzLsUKVj_lKRqwphlMT1QwWt1-Kyq2WdwDRfyzdcgeUOYOGVOYViMQuzRDX4UWrbrhJ3x48hIgTDPZVlVGZhQoyvyKwgBfkpk25n2p3d7ukm-S7MI_amTOd1u1RgY8LxFK8AH30pgHueu3a6_7wqgEI6xngA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صرافی رمزارز کوینکس اعلام کرده فعالیتش رو متوقف کرده و کاربران تا ۲۲ دسامبر فرصت دارن داراییشون رو برداشت کنن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/ircfspace/2603" target="_blank">📅 16:51 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2601" target="_blank">📅 08:17 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/ircfspace/2600" target="_blank">📅 08:09 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2599" target="_blank">📅 07:53 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2598" target="_blank">📅 11:15 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/ircfspace/2597" target="_blank">📅 08:00 · 19 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/ircfspace/2596" target="_blank">📅 08:14 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2594" target="_blank">📅 07:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2593">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ao8g3s-LSgAVcYCa1aCRkuINzs8LjpSf4VwTrpzgkrgLtL7fKPqxtRFtEs5EcL80ydZy5hZuuVKTP_DkgYtZevTCUzLba6vWcR49RCnET3I2BykF32pdjiDmLvPvCTOeNLUtTomOODfvN5zvMOFwdTkfDsdoIhgJ8PQ7CDvAAI7eAKAZgcoUKEd5KdO_-9VN1w5na1Src80gg1zphYS2ePap0-Sw5UG599ViIJgrWwCRdU2yk_x4RmgFDV2dY-1wkMFdxZSkx1LCQSMPmaueg_GzGp82cXYF31L_p4yGA3zT_QH_oPAn2cS4aCSxvTlxy7DUTblhTAeCx1CvJSmyiA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2593" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GgUBZuX26CCtd3FGF88qdZwvxL5TLKXUUrPlDcvNFH7FwodEkx6fkhF6RZq9P-ifz7HfxHKGAEFxc3iLuCJeEJKvx2pOVOvmH6ZOA3FJya8H4HqmLDoWdTIc2G5QsXDO0PB17j5xK3KTv8e89GaS4sxfN2PcO5XGZDnGAEo9kaHHVoYcyk06APQtzWKa7ARvGXvcTuLsCed5c6y6LKGW_SRHnRBS5i90kohvyYHcRxSSVrK4FPA4V7zbXNuLqfGSiFZsF1mzdrHKJc11fY4kw9C7APkVyS_wQnQVmtGHa47UYu3Jw8OyzeBBfA3zLfgncc24-wAf2W559E8Dc4fpug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AMIdBTdyyc5lGXOcjFEeodMwDS9ElSa1UB-ZzsZ-TzI0KHQ2_71m3COAlVo1clOJqk04vCjbUiDind7FS2hOiUI4cKKSMKRAWfPEA0z4WZPeOcyTuB3T8tY_cgP_qRZlXxzpiDlcFa0GBwZ_rbPJSjQ7AkHJ3DEubKqtiHEarOP4nzTx6DXePFmJXR386jg_oftPz5jGyb4ZP_fg_IpYGYlK-OIOKvt8NTzlY0MBJy_OovN-A6xZ9cAOokK268DZycsArxPt1kz5d4XirSh7_kPv3VZiDOs-vHtz8Jzb85gb74LV2rvT8EG_ZfqMNj3nEQzDCv0G5uY3QnI0QPfkCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FncNlmZg6kX0jfGMquynbSYzZQ72NpoktFmQhy1ST7Udy-PKwTROeGOrItFE5eRbgH4gBol8rKyxv9kWjKV1jDRsaXhkKbxmM7KFKhX9LB-R2ivgJGEAgg9D1zr5bKX-967jn7GjtGgp-bLdbvLNRmm9-OFXvESLbyxalvYVPiu2SZL-Yuqb7zIZWhfikhPI7ScazY9aoqG_b59Xc8LDloDH-WMap4nEciZfhqhuqAVVcQPH2jUXYZx-ov0gNMLd9OKHL5MArdpBjyh73vyCjFHl40eln51puuhI7z_PNsXg_OnMhxcJduhaqsXHy1dtVAZE1C-DMH6kwUOgosO9WA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/R7R8iUyDTp7GzBxlpIP7a-xjWoyF1ITiVA_wrJeFgwyDH-OmH9sbDRKYIZTdHpkEYEJeagk57ZozR1fahwY70KGws1plmI-W97EHBlL9r_z2nXHXHR-9dkCdzPHVHLf0ts0W5vLOosw5-gaOlu0r4X1ia3pfUTslqX9e_5GFDPqK2vt0VxvugUge8mTD9hX8w7kAZiZyBj6EZcPuYrVXA8N_EwhVIEFAjZlJnQkClAuiAG_TW-SxpgfAEyfmOQNUEMHeOZBLT6RZrlsMvl-rtRo_LevKSugPD1mYAL8P-mMG_387nea5hRmvdkX61Ism3arga02d5C04IktjJsrOBA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2589" target="_blank">📅 17:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mULj0MUYsVKdI8tZkndDWQ49ucqEJjRkW-62LIbeQH543mBeHbB1LaSj0Hkb3zzQjd0zLmNufF5ZS78aTxwyGVmM1JQLNC09T9u7Wbj7-SZXVvH8SoBlXe2uStXu6ItAvFy5JFrKMlSDkL6PM6fDZD58XQG3tmfk9YYe8_08Xsc-lTwdSHeXFuHJZQWd546_jSgMFxICLu5f6lKDJ-F1fxaE_jfbgfXQapfysU9nYXFB8nTlEieDfj8-YXdPgIv88egoEnbJuemCeqSb0HTatAy8NKMrRpms5T7xPSWpnjd9RiLQeXtt7DqYJwSaLDjuI7smVXw4jQd-8P4JLx9Xpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q6h3Y5Bd9q1XBhp8SI-99bkRqiiFOa6X65Bs2RI76Jk86GE9wpmSWrsZAEGqUEcXoWqOfN_13fzopFWu5IJVaHFUQfXIlsQdd2qlWcy6Oano7e7xLYICsi8RzQsgg_t5Ftznta_ZoibBOYoD4Lzj_qP_rXpf6ifWR8FmOzHDRSzmsJekQ5Cg3c4lIL506qm6goXB0pXd8V-pEYlNiNNJsPfARsNNWnigaiwXZDeVUqVbHsHwFQNoCfaDIPWlxAhNe01A90cMiS41qPDqq-0bqEy7vJjcdv2zH7krkcpwyZjLoZeLx6vGshVuutzVPmiyYTciyPEc_MfPjxPUZW10tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/ircfspace/2586" target="_blank">📅 09:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sQrSu1DH1EiN5MuaacmZxO88jwnXuUUsxnScJRnS4PHjIEDb8YXEhwUJZTAFbwBPsprVR1sDiVeNy5m7ovv5XASDKPUJuVXd9cFpQnS-F5r5YTiEPi77kFuhzxhPiZYgQ2KYBbpRFnFF6UfFFD_XspIKnV_dbI_ZmBITvdA912PJ5qkbSA58eg__0UaMHw8ijN9UdprwC-ve9bvN1xs-1sjR2OJyxKvPRXqn3uuuYRgHodVO3kTHIn95Py7KL0POTcxdNmTrQKNXP3-LIynJfK6D0Rjk_yJ_hL3X-lKInvpQM3-wb5XJiSWkQhiOheihRZ1du-6qc5z38ZIL4o7vKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2585" target="_blank">📅 09:02 · 16 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8dTP8f2YTqw4zk0pqwmkHVw7GvgDSkvK55ef9yZe1w3trry-e1bp4ZwQSv2qJJYtgS38Hxum3cHmZtCGjD5LFnw31dvs95KrcwEXaflZ3SGA5q5l8bVFxH6Rwp1tehxcTX3rY7K-C13zkYx2Wjy8O3_wSuraMNw0YWJ7dolvS21Q9VE5HwSSXbR9-m5FHO5ttvUJp49geAGhfntDW4Avhwwzo5sVt_UqYrJS-29o1ljERbCqTgBYwhpKjGHQmgsShUzgydF9kX7byU5PublUKYXtBhc8h4yS3WeXQUr9Nh5vALtM8d3hu0r8tEophWN8NtHNX1KyTewZGGZOi-Lgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/ircfspace/2580" target="_blank">📅 07:10 · 15 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hqG-tYZ0DJMEWzBf3CzKphcCEc1h1nC7rFBt5w-x4uat-hPUJBPUJvtS6Cpui3HxnK1B86I06hNnE-oWed2HRN7yulJX9kSr-7PMO8p92AEwhi8_KCF_pqpT-cfvTEG_OpWDBee7OL9niqaLk2bbBEBgNmve20wcDtFGe4Tlb5N92qfmHy7RtnlwGot9Jl8_SbxVpWLF0gOtoyUVqK8wu6mZ3nN0A376VR4e3XZk4B44xWXoU_8BHWV93wY4kU9BZohmGV6TxWwm6kT4BqXcDxBneVln3HMXSB4kGYXAgptfpJHbkqG3c01JvfyqYL5J93_FFnlI7DIQSzVkYwpe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات در مورد ۸۸ روز قطع سراسری اینترنت و بعد از اون اختلال گسترده در سیستم بانکی کشور خودش‌رو به اون‌راه زده و با سیس عقاب اعلام کرده "آماده انتقال تجربیات سایبری خودمون به کشورهای منطقه هستیم".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2577" target="_blank">📅 18:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eKcVxtJOPLW28MGZj4_jYagZ2yc-zVISFtu-VXPpFoBWAzrGMgZ_y_EHsP2k7LyJy86ULTi79TsGIlbh9Zk6WTtc3CmSbrriaycN4XNVdY0YqLOqnJHLyyAb0qP9dkf5Po20O0hALTxgyrIuD8xeIPaU2GXmn_XiQE4r6a6mRLFZ11GwVyDczjI99ZP-6e3u4eJmKPSceIUJE1_wDYR_Gs8ega6BIwaL0t2vcT_Lp3LpSyLhJqtZdLG8CG89PzKlV1G1o7yG9WoS_A_oFXq-6HwLGuMHTMhQ5p1tROK-DK0_gDwjk7FRckPE_mQanmGkZZyIGXBa-hmLBAFqHtOZ9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2576" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGJbdCaCsTbA0dEhrWAp5SYOXtHmE2QbbRo0494819-tIw797LNAGTRjuz2Xj_PtASG5F7uvN5JCl1QiuSv85oGmxehn25maOfV1rUrQryIJRpi1j_AP-gBlqhwrJo0ztw8cQ5odG8eBtGPQ8WLmMlUDPzf5IL3gVNaO9nhC2e7lw99kgdC-lvujobkwPfRQygNB6Nk7uqziQhOtriLZ5xoHBoqxfJGH1Pg_TSrTgkGrhjLYvqw3sXdlJ40scAoxo7MsJ0yKZfp3bwl5ePxBmB7KaBljBx-oQHrBJjFnqwvpUDSvy-f6H5_VSHqXAmUmijCk7VQ6QeIDIjW5dRhhew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Yri3EdXGQqiD3YqEJF6tAYMsFO5MAAxgJZEMWxz8RWfm_TdC1y8TdtTd1yTfrvxA87ABtBf886_lsM6HRlnw1vA-djEZpnn_7hT25CrA0xfXUZAV8GNh51oXZoFAL3EijuNXLavuqYNjC-hyEsGMRP0Ua1wLhB8kEh98IDhsF63lleFR3mhecXd_TQVwck13PPZdAvxJ5a25ZY_MHNLc5jtLkBkZ-tXlpRtJJuxsGDkqJ7Caxt9nVuiXzTKdq5eI9K3zNfm5owv8qNyN2hAtXCibUhFw92BOHo5WsfWLERbDFBwJVdD9RvelBf4gSduhu4gkclCBitzCIx30o3B7Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TX3M4c15RuNXzuiIAKVvMF1hQ4p87A0IXsGK8UGRWegPOCp2vpMsT7HGmOPiMiWtNZ0MTYRai7sL0WgmFMCyVnzNpHPBTPW3jFsJKThCL18z0t0DDz-u-u9sqRXfrNQBVyZPu2CRjNjKaFj60c6-BsAUJEdb5mKMuIYirI-B9w5WkQlXBpaWqG2YqGQLq-bsjcwTUuBA8mikEkmjbYLbxPFZGb4LwmMGhc_yzDjHzsUwOTj5vzLIdUYYG7LRppsBIq5tnGh_lKmU6EjZiY9RhumnC__N1gLILIRQzHffy4yiemWmG7i3QEAOOq40QmoyQ-S7xNj9ef24FgzkXXDBhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=D3E_gduSQz0YXPsos7ahi8JNFoOZm2JTQehNoDrE138P7YC4sFSb6soIB1QPl_1URY5SzSQ09csHGc1epZQZqGzuFEi25DTycpElZAenUKNvZz0JTQ4Hb9hzZSFW7Aeg3gbCw3ghw7mb7n7pu0AOnU7n0TDf45wLGZvAHoPa6v8PNkTeTvgH6HBSkZNzz3aQex4229oOoQh_E9S1EdfyeWMEOedLNLyQ87_Sh-M4dMPXCsoEXHfOJ79IDh8WJv8Ze0Q8bMAo3leIM0Yk0uxT_Up5kEUtZ4I2WtUDacNfIhyhtWPHetXRs214qEKsxOkNZS6mMX3k8ZiUhHDTS6arLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=D3E_gduSQz0YXPsos7ahi8JNFoOZm2JTQehNoDrE138P7YC4sFSb6soIB1QPl_1URY5SzSQ09csHGc1epZQZqGzuFEi25DTycpElZAenUKNvZz0JTQ4Hb9hzZSFW7Aeg3gbCw3ghw7mb7n7pu0AOnU7n0TDf45wLGZvAHoPa6v8PNkTeTvgH6HBSkZNzz3aQex4229oOoQh_E9S1EdfyeWMEOedLNLyQ87_Sh-M4dMPXCsoEXHfOJ79IDh8WJv8Ze0Q8bMAo3leIM0Yk0uxT_Up5kEUtZ4I2WtUDacNfIhyhtWPHetXRs214qEKsxOkNZS6mMX3k8ZiUhHDTS6arLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lZRqMhoJiBQCrtiLIuir-Awcmso57fO8pHkJPbywGM56sGi7QBKYq_O3sHeDcsiKMvs90iKruZ4945ChMkKEE6PNwFLd0WEI_hbnQgUQsWqalOh7D376l0vKnj24bjNyhk96ERgZKc34KA7zFYlR5M8js4hak0pOJkm95pw-9GupMYd8v3-rvNiiemTnps3pIckxFExRysfxr42cE4crAonGMpxJxMZjR6RmvNNXmtkUV0h2cj1EI4S9JuYmDIyZfWFU48KViV3xF_k1uLacWzJdbXTQvViKPu4hExzJ87YA70i5SbSpgACoSbIZJI7YDVLNySj3FjmtyViuU4HW5A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sm88bCPjFxQaO3W1oINbDYVscCsYMQN42EFzht1WHrCmhkfuYGjU2lJECC7DPmbCbvHPOFuy7NHE53kB99FgY1d446BDB56L9D8llsOeOGKIl_1Xoxcs40XlYPOmfs8BHD56taA4RLAVhY6bPDZA_hxPw-Tlb7j1w_yE9D1vq1TFAO1ikMbYUT-eAcwJomvjhBKBQPz7rYNkD7JAVyF3jGZU7iRIwCPUO9tXrVeHdNp8xy3XqiT-Eb5iqYMCCmHx8REyCe83Di2tN60_qXfIdhtTq0bxrDAMKqMq6G4PXlqMIOBFePg9iF3kSP6gMi0oD8Dmxjde4KuYbgmyG3gApw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/suGEdiDRQFWqDMX0ixDvSXOseIvgxK6v1wiLfmwzTF293TW7jPhtoKXmIkSeuxgBFFzF_pDGKveYw5S6GC8erPkOTFQFdCU87f0g-zYetvIr-GH-ZMotE86dN7KI-MEcUBub2nLIhDsH9qOGg6xa3KFWLmuHSHR2Dwp4mcho9czYUnjK4Vh70XhChc3j-bwPly3rUWfuJ2JWkRPZlpWGc8oqO3XRFbCbecFQ_MpJ09u1jly-vJKXEN8z_uLoPqyNCx8GnE3NFqfmtESzSimTEuSZJu5o38TZWdSC3KXFCWSOMF5LhuRq8W1IGn1po6H1qSpxxRwnyd93hH56s53CcA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dqk8O9Hrw2hLZXM9yB4MfkPRt73HS2LIXLf3P9inrV6j4UKHD_KcPhZBBddsvAit8BP4FlEuuHNRotD9Exi6NXcxOfwtxchMLkG6NKjSHEasqIEgfjZNyRYojGnhI8245v5kinHPvgc6Zz6gythJ7bdwoXnG3urqg3nU9ksMdMXFOEMymmmfY4fGhiHI_6rEJsbWaZw-38yXXm1QidvWfiBFvNRNl6hEXaqBO5WsBDMs6RDVfZscs_62ZlAZjC0Oh0T69X1IAO1hlqs1ox2Mf2VS14Cm2U3fAXPpL39pz2uf0QVoVY4Yr_sdaLQCTGpvMC_S9uXzxNiUUE6AOM1rPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/osMhQtTtBxe4vjn0nZHyHEEuItzvObbrgJH4QI79YRY3C4GdVTtpJnHMCeIDxLOFAuQUycLRS59ssuA1SIpuSL-1DX7G80VS5Rp9JD0IUrKo6omn8AMZtRaKMuHJgZz88hYdMvu7r-Rd4Y2XjpIWNd0ZEHSi_EEdmlPIazjgl1N0n4ca9AXTy9Z1R3xG7bqKwGpNRNXeFujYltFMUwUJaTOCTsH_2NUutkjS0VRmC019x5u2ltoNPU9hq_HBc8pSlDUifahC28Zi1bVE7RanMmalxClC04m3zGGcIQqGnyP2t8w4WahrDIWmOQLnFFQlznTpzogaLQByB9Y73g-2uQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tghtkdLFem_jQZi6jjoj548s7gD0eDANQfESVTfbtCA-P8-BMZyErCm9rEH1uF339ej7KWNMJgIiWhvl50WdiBYPWCimDPkEBQL2XAZ0E9-9x26Qegb-bxfkb1ZDmjDpwvzN-EnNXsHdJ65j8q5ghbdRyv9cq5SNGAO6rc0V7oL25ccE-xzaSyNCBnKAm2LsCiyZZJ5cH2oisfE4ORw01HF00uoOrHp2fQ_8Tl261SC1opr-U1ECzRw-YvLr9WrHrz2xGKmvxsJqFw8aypXxoqVsdJy7qpsw3woPfqTeceglD8d6mLVHkEzPC4qbhv-2R5kzUFLmjOXDDvxmx--1bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DWpoWi8W9DgQe-LQFv1XyJ1eIHz4-Yv3PEUSVwi__5mtNXEc5V88MabMeBwbgkZExw6MdEMTvaTX_Su5X6xwVQcfAtmF_D3lDcVmMMEHMBXk0weCLqedgGQFYA6GTAJSB5DPWF1WUm0UjIlPC02kWcDIXcU3ATQdPI7Fnwy2N1vCKXaNeb5yst_WWaei5QkOwWid_m2s1VA2emTu6ghRGFhmGJjnpNejRCvEKLqLOx9FSqhtfTClK-mNVmnxW6ziBDP19EODGZTlhEYi3n3XRo-vi1yombcUDceY0zxRMcDEJTq4iLcuMh6RykatONfebJv8yVbFMtzPf3F8JcNzMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AYt7UrvmGYDXRVx2bSVIy1dFEebDwnBHDfrpdFySCHVLRpRtkKi9LkUNY41-eid55eS7d6UItyuHf86ALBu3fjK_vLB88WFNhIlLEZ5jQlSnlBpuiDHsw7VNb-A-zym9za_G3hIKmIINu-pq8C-Obg2FvulT3e57MNmlbJPs-uHHYqt3INpW-i-Oe_j3tXbTOi0HUo4-UFnPb7yiAuIOKF_szZDkDTYAPQoJGM57tVFH6ZjxYxxK2vVyWQ2ttefaOdYzW9YgDjaABpYh7UH2LSS9aGNT9S0WmREajR_PFIcX4g68wx7u_5Fzf9CExTO6-CTDdEX8gj7W1xYr72dG_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b97K_I4tRS2CkWbDKVK3T67pn8zOxH_Vuo2JYjTj6jQQXY12oOu8QdpZW9BzFkw8z4O1FdVuqsSS6bedG16ac7TL2kl4nr65zuOOPcF6jLBoKc9zh5ssyBF1KDtmAMnP0W5X7oSkcvvovFKFkUeKAXsec4IjQxXx3e2c5p_x7h9HU3Nawg4k6MG7D6R7WeEOzWhA3vTrVePoRpX71kcCdCq7469qljXdzHRwpQfRi5etNusIr6c5VMsxrpU6liz7_gjNVRV8sqSzbIYfJWKigCn3QE5BDSC368LujCusZysQsl_Z6hGahX5kh3ivrVxisV0HN0ZXHqOg39SdQVlGXw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfWPkvOtBL6SOP68SuQeWnTZRuoPljz7i5O2JZOQbqflSjKEeI-oZa0sHrlaB9FeJEOFou4ihQCrZUFNASGCCUcSeUGVzpXT0jhBAVoGaK6Uy3_-eBxZt36LZiobYUx9R3RvaBchxgG56O4jl34ikFCpFJANyYRlCJcvSdGLupSs2tiCz31UBjrU5uLAugPgPl1kjij5ikNqCqEN_uMLiddQxUkHQkJTn5LFS2CVfDbLDoiQecLLC1C7BbNjf3K4RXBskFgpFs0e-YA2VbZoo6aurMndPunjODzEiaXL77s51UUWodNpkB6y84C_oCQnTmtbtdEhCWNzb9cv-z3M2Q.jpg" alt="photo" loading="lazy"/></div>
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
