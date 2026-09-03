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
<img src="https://cdn1.telesco.pe/file/lvHY29zhgXybTrGp8iHXinG4MYHwVSYYcBt9Sj8gECY4jeVftFkH_k1oddSiMP3-_QfJPvf9wuLS2MgLq4XUHNlrbk6D4cmlSL0zcBZgofCKwoJpUZ7okgg0V9mHe9ATQpTFUhPUV25zldeh3vmAghEeEHKNENID4WddL1fRQc3kvs5U3IUKHqq7Y_51zpYLitAhnOIH-MWbVos7BD3rzLE6COmSjjcRkDMRSBdmUJ_H3R0cnm6wAga7JouE68C-2yoaOUJgtBD5GjQKTL1v2FNQYZrwWI_q6O0iyugwPvqcqDgBYY0uyeHU26zqilD6mY5dFImGHiIC4ZrQQZgNsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.4K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/ircfspace/2575" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VB6YJ_glwtxeODobXpMyv8B7iJ7FlkA0N8X_SK-KgT_yheVv6AgRPZRJ-ENPWmRwn66GfLt2e7e_BSqtxYxbT_kysN982XBYJ4j7ba93slWycXO7UnZYR8JQpBMEDFkmpr1sU_YDqFgJBMO1V3xIsYsMJyVwF6RyYfgCoUu-icuXBMnJ6RL5Hw4OzSktke9TZKr9rNDO85P8LZdkCAP88uxKCIhBBrhHT0_FM9zdkBdwLbqljzrziMoqBdqQ4T4fN9LPpTXyCDTPwpA3soGNwsFRvR4ttzWEuFfjDvdcF1pEkNh188kiY_BXOCWeZKH52WsXGhe5jXJnPC_6tIExGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/ircfspace/2574" target="_blank">📅 11:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V9kiI9mbuWedUCua9YGlv8po7wI5iONoCM3OToRzqx8cUCvFQudbUrYmh0AY1LeT68WwbWOnqT8ZwX-FvMp17a-PT8SndcavYE4XL2o8JQsOr6ycHKRVY7cJKkwUcqAimAL1xXivPpRAA6C4xhiuF3FGxYHaQeuZD0ln5wN_UmWWs1UACWpVJaDDOR8OdwaoCO05pQbTkypfZjKXjo6WwnLAhbFU6uFqxw1zF5MuvZTi7FRfLlpafmTScYiCwLLPrmLpnsONLFoKwtLN0DRpyE39ZrUMNQ0CYH9XOutaRgOLhRwVsu_g6XtUhaD4cjpceDZX91QIPDO1qp6C1EJrRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/ircfspace/2573" target="_blank">📅 11:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ae47y3RmWyigyR6QtBX2vcCYe8QszTG2qqMxrvcgbFf3qH8okT52vMNPiV_0tbMN224M_F8McT7all54XXwNG0yhWqiANJULorhjbg7qf343XQNDLJG89ZqoWfhtHRV3beKzOI7kZqet0MRTENunJczYWYj2YrEEluWhXx91r9T4DgGaZdrMtZ4kQNs282jxZoa5SqRG6Y7Ps9WyD-6DpKF2a7wDNsCE_YYzoooKv1R62WcpnCQaNv-xKAA3HRiEGo0D57aa8fuT6Os2Ib44Ra_4WZXKIRN3_BT8rTMTG527aQKaXJBAserapjI7G1h8cmYT8xHQABypDHXIhEwoFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2572" target="_blank">📅 11:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C2tgcfqcO3ExWuUphnyQDxVtKByKxCOG_j8pclEIL0mNFvesFNwlJlPNjBJwDMEECIHLQf8STEFmWImiQhIMh9RG_MaPKZzq42Q1RAqazlzWF3VGeLC6M91xHOVDFyPGXzStPllrRKorIce258S4pB2p-BH24YEDV92u6dgRCAdfDOW7uwhm1LyNfjqw1367mde83VrL2olyEBhoYajPhLb4yO_KIJsQmesRfLHrzLZsFfuhIdy4maNFrX6PofCXp1k_GulmDyCNuep_kX6dJMyRZrJ1_sP4XZCNB9h0-qQgrQyGBgVQeflBLFkG8jnQ9CF20OHh8OmCX5IfnxkyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چندروز قبل وزیر گفتاردرمان (و فاقد مصرف) قطع‌ارتباطات گفته بود "اگر استفاده از فناوری‌ها به نقطه غیرقابل بازگشت برسد، بخشی از حکمرانی کشور در حوزه فضای مجازی عملاً از دست خواهد رفت". در ادامه "بستن پرونده فیلترینگ را یکی از الزامات ارتقای حکمرانی در فضای مجازی دانست".
فقط نمیدونم مخاطب این صحبت کیه! اگر مخاطب مردم هستن، بدون تعارف بگه بیایم برای پیگیری و حل مشکلات وزارتخونه آستین بالا بزنیم.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/ircfspace/2571" target="_blank">📅 11:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/ircfspace/2570" target="_blank">📅 11:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2569">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kZfJ1aql-5YlimlzpvmCWsx9Dx1iDNpDqeHt10_xpwncohB47OcO14gHkEBuwtM52nHdbr3zuiqHVPpScv083avV1zslgcT6BEo8SxQhH_ERVpTrCqh4rdqAeoq3a3sFDpmhmKBKfdkzwTrPitT2yjQC0h3810oRQEHF1aCN2VMM8jWsO1mLjUxSSL6CqAF6qa0IDIfYP_F0tojv6GJemlq2ZZ1u2AerxobvxUYb7J89-nLtn-ERq3fQPJN6CSgTeSOyOV-M_2cT60oYOn3a57d2eRFF14JSlOCugG5dbd8HgQKlTmnVNvVcaim_27epPuYlgzg39zSmjFXbeSzkEQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/ircfspace/2569" target="_blank">📅 11:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cs042MqUkkGSd5rDNKb1lQr_xOGQs1kvWhAT6gFFnobsUNt_nKvMcp2SzBPrNzRQxU5Hlay203jnDVYBCn--Up3PB0dUAczSyknnd1BEt2ukHv__3Q2_Rl7VUIbEaw63oS9QNHmzkIbh_zV27iwTiZdndclLTVkyS0qPd0SrMGa8YEvpETu07UK_VTYOf-w7c2cgU21cavZLAp8XOgo31UKgnhCR9bCYigmZuuFEktHsc3hVvQLGgXH5TC5kYQODOc5F0-AQaeVq-v3aAkcz2wtKt28AJZL7OMIpEZ2e1dkUQdZDJSjidcYPfSkPlC4lIArn4jCrhh4LcDYGjt07RA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aotBsWZC1PfoxW_l0SYzECHzk3rEETNLSUtx9IgeT05C7TIxFOlhHcdm2XhQFRxSzwUGld4fyhFe0UaqqfJ1R5-LMbLBN7tOvEkc05tOp7vfDV2qMJlM83_I0WsyC4xOHAMlmcS-4Q3soNflZ4jzni_3N3LRdqHMdHjnPGn0ZcB_j1e5yHtnXW5B0keAN6iAc1Yuaj_9CFKzbD6kYxyYS_t3pRkEGR69eDutvb_lP-fudfuz0DqQavDwG4AkgmkVwMf2C4sfz829lbDpA7vb258ROT8eU166MMO0B6KJw4QAC8xwb_iVcT-Rtek4AclyWw5c3TgXGcjiLbfV8GECbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vBGYrOQUAATxY5MwMNExNJPy60FXVE_0ybxZo1F9aNfje1Ro3E1CJpwZw2V7DXfb15jncVuNl886hYZfR1fAxHt8WatfYF9TseHfcbHiwIzxjdMw3bfPbyq1QvOX7oS9Y03UtMtcsuuce4ClP8Wcdws4XxljwOK4DQ26AdCFEPtRi9RicdErtTanx4wE3Y6wfzVvgozsQDpt0iNv__ACw0IUA1OirZ_BMaeYZxnlnwW3lipGxnGIvd23s5szhcyYCuhM4bxB7otKJdH3OPMd_eA1jCxTjE6JXG7_WhR0qsnCyOKTdapDDsfDjK3fBQZCWSMAtbffvGnn4BRQZ0tmQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OlkOQKVcU0wJrjGy5wmCu2X_0imH5LaTxiWNLuA7YaIKMT5eynYtYtprw603KvyjRTcrPtJ-M-n5eE3TSq0vmBHosXSqXnbqaqzep3maVc1kpGNEt5PeLIHXuPs0I5e3CZQ1l4KQLI_zVaYPBvBTItqm5yvYbqnYDBfqtY3UUjX3Ci8rEMNAGO1H_4fAsTGxuQNryq5b8gAUF3EnL-Ea43YXRtJco2Nh3rHBa_TtGqlvQTS5FK1WUJD40r3wb061okTpJfEtvzRPM9SXaJgrWjaYCXNMQGt7EnwFFS3FgUawEJ3llgneWU8_ImqLGyKnT1Pld8lYauiuJ1msr67f7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OQyXYYlzVLEL0PfE1q2LIYb12pjh19G0q8AcM5AhvjHFu_neAsWCYhKENim-bJYIYeUGpuGALY4YEl_34uqSahtFaARYil7HObKjs6LXwbqH_eGidh17EYxXQkcoyMOtoGxKn1C_ErvyRLLHeXfL5eBl9--ub8eOHCj_17eKZ3BiFZKwB-rjGZ0aZMayM9tRfLbg-el-1JWnX504pIr4WcZJBvc-VcZBsAzBWx-1vfEr-Q6GaMsPsN_TsB3UcexqZ65bjDoE_h-C-K1nSDrLo_rggw_WngVDjeT7Sp0goO_7n9b9JrJq7kT8EWQZ3hT8eImSF7BfOHjAn5txE7Lb1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u8KpcywDN5MMclUZxmDldE5pra2Vg8M5JglQxDCHbRknm9LwdE6VzAJNHQOKF4_Ho8VWBxFimzjSysP0ZP21Q5DT6SopLiPVC1r4eukLkJoEYKLXpuFQj_BPUZJfVObbjKx4Nnk9mWYBZzomtpo7Y5yLMBchwDzCFFjzR01anSBJCfi8Pv3uTFeO4J-EcxHROmuv3H_xxzUSChJZvv88NmHz4ge-ioCMY4ELOLhzuaFs1P4xdMFtmai9FDVZUDOElKkrzkGb329PWm2viCzlx-mSatBV7YLtLTNb6Bwc15Ns35rDmU6IBB9tAQ0oZlNrw54Bi5_poNSeATNHyDe4bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cbuTZdcWpR96o1Sp5QmDql0BCGb2DnrJv0WhlHJ3gC9u4JJPhQpMz1LLtK3x6SHw-nRPXZiih4DWK1IW6D6u8CN71z04DfgICI_qiPiFVph4Gz2PNY-c_9yPKNRLZh-hQpV9HM6ap_PqHz53mVaNOBrwblaHk_ybgpwI3G-VtcBbTECRiZjzr0zItP8cDWXQWLj8X8EGAuPftCjdh2UqaLII-wiy1Fht_VDIJFzFEbWQG23MCy2FSeegfYvjjOijUitDVVfZ8zbHkKnNBoGr6iJGAGzgIAZhFtj2vSLct3MD_g0kKkapve76c20z8Gsu_g0eH1mbGUY0L04NUEYQWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/F-gVVY6_ZxFjh-MvZ1N7qWlkBFUzkF9jmPqt4FpgsQ4speu_xbVagIQzYXg0kSXdJhpkP4pX75_t_sHK-HNrblGjJTRLzkWaW2SvCf3WLS1jClH_p2j1RWJLslTw4tkG_9p1rtQT3Eylwido9_hV6iM8UXOx9i038pti7xcMLwZ4hzOk34JIsy5hFhj1m6Ie_pQh7v6T31Xhzhwogpu8tOz-0zasM-4izIUnm9potRjYRT3bFS5gp9mX8f4Wjh6Km8qD_hIqmQFrTlZMrDxdDsImFCB_kleQePSew7AvfNOW44e_9pqTa08zzl6Y_ASUJaq8AgiLL3UnavVNBULNXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSmSxyNpp3SDflimOhg7H_hsv9Auu5sC4OCqnQM8eNs_Y4IkvBLSyGWk2Ld02WSkS7xUMfO7Cy-oSQ47DYXpNYS5xCQWBqTT5PDhvrG4tbDzVYdjQs0A6_V33wlziKCOg8z0fdf3glwiNTvEATz4tfiNOxSY3NVOVgGFjxjF1MhDxAZpkUCnuw7gIwRkx18MnlsVIdPPLaXXu4_0cMqYeVPtypicj-GTzPNo4jKiTH2NCXS5vVstNQWnJvHSFYXhgMa2v9YHoL_GEJ7QezVjd_oVpN-5glT5hGprzJiPqUp6IE194cz0_krZehYPKY-pjAG2L_EE-ge40QVzA3q6Tw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=pRN598EMU92mCYO479nA4EaAVeF09JnntT0bCZF6dIyUrw7Mmq43RR3g3B9Z2ya_J-u6QVxvkrCSiMAGA5pu7eEyL_5Fbkk8JORMuCo4Xsz-CqXIolIVLRDjTR7BXhx96YIYdeF4emIMvFJttM1tHQMQNNDNXRr5x5803LjKycih2VxUW0HrF6ItnACbmRDK51aXKEBEjMsuaSonR_9boAzXgOCF4-PhreqAo5nMgdyetE9NNDkyz5FRQtgkn0Rv5trVrG-UQ_f6t4wVGWcfMULb6TP24TPm72861rdvqDUk_wxRrMIdCAp78Xfa-jgCsLKk_7WY7WtZaRWHWZLJwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=pRN598EMU92mCYO479nA4EaAVeF09JnntT0bCZF6dIyUrw7Mmq43RR3g3B9Z2ya_J-u6QVxvkrCSiMAGA5pu7eEyL_5Fbkk8JORMuCo4Xsz-CqXIolIVLRDjTR7BXhx96YIYdeF4emIMvFJttM1tHQMQNNDNXRr5x5803LjKycih2VxUW0HrF6ItnACbmRDK51aXKEBEjMsuaSonR_9boAzXgOCF4-PhreqAo5nMgdyetE9NNDkyz5FRQtgkn0Rv5trVrG-UQ_f6t4wVGWcfMULb6TP24TPm72861rdvqDUk_wxRrMIdCAp78Xfa-jgCsLKk_7WY7WtZaRWHWZLJwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 52K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RyQvMFYRnR4RarN_HUWvz_2rhxS5AKyNZwNVLanBM1xAQWxfmNXTqFUMqYE-QO-KcoOQaDWnz4MN6bgueBZnLtRqEeJlHEQlErh3zGTJX_gkooz0wDzHPcIk4dVCtyEBee4VRSrTUoArhlZsAm0AudsM88d_8pXB3IF4-ch1HjRxOXCKoxHXP7LPKFv9_iFbU337xen2LDDi3IdwmPH5-6BtXCyaiQWcVXtsPRE4C3N-rTUWwehhC8Wyp6W1GY8UEV3hnRN__rHL8ipiTVnw0V5HqRD5WGEP5xafWZ9YWPsCM0Cct7j88UxcJ2kqUPWDkhff3Uzz54IriZzT0G7Z2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VEFQ-AHURFlBEJeAk3Mlpca-8oB0nYNmP6cUY5I8zdimCLcTS5FsfJgeJJYW-PHsCvhyBnj03vd6AuTuB9r7qK_EKInC5jE876HYqMTyoV_s2FLZTt6qQUxMpOT3UTd9KyTGwZtwj2zusk6XtlbDfwP-NEVa0l_PpWicZNJe3ZKFHevieeBbsh-zNhHyBDJHzPI4gtDtsaJH1VJWb1Tym-9P6YwW4DKoq_6b_E4fGLhWIsh1tYUHCM6bK9yjRgnOILxiSDMBOWrc7wIJXNqvYGhw9JjwGvW9tJCeB7zty0FGXgeq1Hec2S8A4Dd16n6lr3WkMegz16xGGbCMIK-f5w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RSl10tmLGWGQoqZrR11E7ASEg2Su-TIYAPYjh7cES4OMiqQQ4y3jSd_QMKHcf4szVajdgwZ1lGcNVtVlESnGeyAeRmZoz5uwrZKxgidDHQ-lBdY3aSBHAsuyMVzTFcGNWhS2baRsoz97us8axvDEvki-NHG2ZTgHNBFzi4TOZJ8MtGro5lYZ8E944nyyrlPfjuOko4PHHKdHX_Q97j5XER1rfvYWMbhYXJ1NNPzN4GUbqZ9I_FSpVZjS3xPCbRr07I7Es84DqYxyTWqO7wEmuTW8UhWasDGavXPimucWK52UFh0X1WgL5OlAs93qe1yQfRRnwYt21CFhqaRRUxFrkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KT0rHAOw5e8aQkff0b8b5CEOumS0HQUzKPEgedci3jx6iphhoCfQfrScQ7TyzEYIQtjbZytUZvopcjTLBfQdZki5dUfexG86iYt84uEVFogFwguYz32x62y1ZMiqsNlplDTvog_15FTAKltGaC9qBlZnhYmwgDuMI0g0zp-frqPPm-GbM0-nWboBoSGdStpc6ZrVs-Ac6ajad8HdHXXPV6yHBCMgQPSl3NqE57DdR-aaGJD2h2_fbwC8ORQycCALV-CXZLo8LOmXC5bUMvlyuVSU3q1JV0_9WVnZkdPRWOjjLiMCTyK6Dn1DDCbqDFLWKa_E2WryF77fGBHWJEm2Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a-Z0V9lKxWSqydK8wPl9_8CgFyOQORe5WkHzbscvOlryeVL4o5d2RHLXnIwDiUIryuV8sNlSBzEn8kTsT8L1Fn-LLJ_MAu7SDCo44BjmqV4ua2A8ELvqDb-9B3RCzePsBti2egemPkvS4KRDRSMPpqIPAxw6Lnwqf3kiaArD9nVh5NoG_ZjyW6kO99e6E4Izr9SBIXZXMkqzjJ1WbDr5_P2iQ-5lRDDZSYgLl8dwr4xUfdVcNxEHoogoxC8orU0oFO605UwbHkXqCGcgMq8hUiWpCbUjxKqvGw3qbw7-iQHyFFNN5760FVxYLoAd_d8noXLKsS5G9-iTeHBR4ToF1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iTKbZL1IQfZSltbu_6xtv5asEQ-9boxsmfcuztogm5m_1GHiwV2WuxmKO7Y9VNLIvgD9spM7V2W1alHC97vecOHBBPXYuZJUOdSygyqSB6C7mPXRVaLPkbEaJyukV4q6EPFUyi0dvxMZQXZaAAJIV-5CoQllEb2SzeeLVPdNJnjQFXH334-X-tI1ZPulEbVLmbZdRsyfZEPnUX3ig0y_BnMNs4EFQpNAtRWhg1dCXD7YQfecsjeycAIV2P-kA2OY4hQ4n7FxfAycPsox3mCEAPdSCdbCbBkMRkIMqpCJ1wrX6jqC1wY_cPqyu8k2IGcA_zyWBiK1HhWBIG8HDxskJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AdZ61rqyze-abXO66ncxx2Llv1k3vYVhboTZ0bMUGQcdiT9OEP5IPDhX77BIUWg_z6pFYYz468eAojvoq1z5Un3Cf_Efkp0CAIatywZk_2J_hC0TJTL8kbLrR2tnnNgaJiYCvJvcazMZp4qPTp25CqPD3arYmbZ_mq8nKdsN3km6www4z6mZnJjt7jYqwcNJYPQmyk26iuKHtQvbRPgqYxf-KSsIPLY7xOFRrDjNskba6T6dUYIn9zxpI1uQtUXQwAZZ_gbdhhZGMTevlgWyyv4qshqOs7erBeWQt2zew-EMxY3c1Tq3HqNKeL-Qim7T3o5UVPxL_ceHBDTZTRtN3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dFYPI6MDQI_I-P5IktpmEdozUlVRz4L__j39JhQrkjBumebPt_mbEEx-q6h7rzUNCdgBBe7-OLyYx--t5NUzdSw3P9D_V9dtfdaRH7GvBAVKZdAY9WKC2qfmag6ffqdj5HPHhRHn3RUq8OsuaDm1A7Ck-qbcqe9TtlBngFYDLTFNmQ2maX5sSihFaDVjk2lZ3ovx6lmC3Lz-vMIOQzWJcJg0GANvfgn0jPeGWdKjWx9X-rOcPWPncV0vgdFlXomRkGwAx2v-IigVfddjtE8C9FB_hQ4wzLKPe-3Bk2-nwdkRbkcL4lvOTLT4cCtehdn4ndwe0Fcr5ZYUlIzp33Pdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vXMMKXg7vOzVVKuwdSN0Jcnbxn_up7FlXHwVyQG8kGMFJlG2IGp-zD-wA3-KRbjq211RgHe5RQTBeu5IlUPl3zRnaceYdsigLuNwo7zXCu5OTP7DiXMzRwkcU3hXO1kgjYHgqgRIS2aXwacQfEb8_bdoS6tXIb4emMKmhpgBSpvKPAGRLcwlrtPKNmAHkNAwscwn8eMJUvJ9t_m7ODKajvBbjs8LCaFdsL_30gDU_Pz5cuootQlL5djUUJ_tsPSToMhI1_m_VqhlLEvsy-kCUVpfQ03BmDE0kLAK5dfyWTssC2pbtORXAw9iWAGPd8JEazJ-F6kdiBNtkf1NTATuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UmszEM47DEN1PsBgEDKBDKG85NFwKIbZBUwqHip05nnBudxHL7ZyqTXNGPmD8MQ7-ygDwD0clneeZz2sQh-12EuYQiobaSl_WFC6pT0PiYwbl6ldF6AN2X8z4n-lAWqCn-NXbJvovL3eVyyoUEAtXuVpKr_S5LqMNEazr2VJ8KIEntnq2oQfbNFLMtP6RgVEwqoCzdrl0AAKhK4wIBk-60awXot7hrOoxj8F0f9aWmapg7PENKI8n6s9VUuTGsYjydCx5Tx5rr7VO0lLfjci2ZLc84Ga_0OV1zmXpRtkCDeewRvgSxrw0yKYbhQNXDZXN961k6XNwF4Uz2M7DCiRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rRFBBAc09pn6NlF-uG5n2gOvzC29Tgy-2oCCrEgLwmm3U2r8jijbzSF1kZY9x9Yx_lbvkCt64BSQiia46PFxCsqfdRlN3uMO56haXGwnE-c23aPY6YIfdLin0HIiRD0aJ_m5Kki0Kj0uZFF9uE9s3DwGQUcPn40b4512BomG3Frb60tIFJlJ33THJI7-7UZtLZnFlGf92QI0FFdIRk1CBX8vk3RVQEPZCPTHaiW3DOMoJLtJCRuEtnP5R09rd6JpPeENLO_N4NZNG1A16eKTfe6l2YiCaPXTScOHjW6xWLBPwEo9D-eEnk5IYXpC0RZh4dNOzcIwv4FQWkS-tNSe7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lB8CMuwMviL2LnwAiHmIeXmcP3EpWmdXvJd3mCMWez2jPzukAzCqUy5-DM2suUJL__A_XLQRgLyATQe1p5eAf2PGjvEwlAYnHtLdeGyMSS_08womHCb6O7dyYmRb-kBth7Z6jBZOVh70Ssau0m4bv8giNAnPGgEY_XPqTj5otJLgzE5nGTxNlnLerBK6GT2iTZPZ19UURN9e5BbMMsgdRs7F0i6mQFAraD5s4INYhqV6iLI97s00OqUP4LlOSZxSCQJridd3IHJw-Sep3D4fDvn67ls4Ad7h3HgT-5tkvj9gwtI-uNQ6as3K3ZviBIW3WuCzjdrdhuo03tSXG9Ghzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lqa20FLaeplorAeJ40wMxuN9fDlAKvTqukkmT3YcbcIgKFTg_ofx6Blwrit1x43TOBemkBEk53vg0E8mDdijB6Pd0BOZwfXotVD1nRpcx42ufY28WinnNVVNdoIfK5q97CTb1wyXZDceXsFXE9Qtwa-_R8HTpSukmgWUN8KOyRE3A9cNMm8LaqB6HlnfCmH-HQ4eb_DfhIrhIOnDQv8kRdyBxmLKFughBvZ4q9ysG2FmGMI08BjLLFcOOZKoKLvy4HsCFqIEaNp_9L1dVD8BA7DfxfAQhuhj8qDPZRBKIRzFZvSd0iwWLCLMxwnXg7qIkUNpPbGFSOwd4dGzQdNSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NYExXT510KCpu2QG62AuXuuxiFg4fpE8H9vM1Z1gB-J4a8mwlO--XWbRTjkEJAtKEjBve3KemynOs6hiDO-hBKNdmJ7bJbAphiGwMbzgHFeDX80ytZmKPHlpUjkWW2whLggrqXfOEXcQL37_e4-uXzdKGAEq_H33ErDjwcEiZHYah8lV0DV6FFEYlLiRmtGIVlvzobGo0lUBHBT8Dur_bHlz9lKMy9B4XkR_b_Yu2FKsuHKqGAxTphG2BONCgOnFJ_CFonPa1P-8p1Z8SZ6dKV9WvF0SFmWmQgQaAlk5KtPv5hAIaQtqKDDaZ9Ca-gLshkFVD14QM4TYpq69Q86b_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XIR8ZvyuaEkhD7-M-6aCBWhGG3BhfwNLsiGS3ZjktjfWdcBBfo0d_trxQrgX4C6ohNOscACd3GWUyEfwAXT5HMH5QYz8UYh0DMTGWSKcBsjINpHIUbG1B9l2BLmypuv88tA3oVx1k9cyQ43lmVZizOPSqVQM_ej28wqx-vBIPUI-92S3BeTKcxIIhbphN93ycUb2ELsLJhFKMiSln4KJ4VlI0C2kvqqkYUMEXainyiyqk_TE_IjXVEyUp0uYU9SDkmGUukpRVNrKikt45f5lO-nzAYzckt8qIrxjLwJMG4Wg2h5MZUi9pgduGlsP7zSQoHW6tUHPYGdvU10Eum5THg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gcndB7sWMvo97rR7qdeGZhio-0weHdAWRCi4EZYV4B69y1E58en4lGlLZffjTjzx0e5KYMpNyYt1d8izAGnmP6YbMqoBrq29-HFLg5KFxDX_JrnZUUxDGbM3X9MQ1vYOfpIwEtP3TxejerwTrpxY-yg0nyg2-LbXqfwf1CQsnhguX4duXJ7ULuSP3XMLMLyZW6sZSTOe-VbHvvTyVPEAmByh-aMsw0Bfs-5sDL0n-M4-gXsPczl3tk2spuZp8fXIjq6p9dQWpm2ZeIme2k_Ad1scDyOaAjX6SzavKn3c9TBlqEDroRUnIlPIqOTOoqcqpZcUrTUSilFuUoQNKgMQxQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #57</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mR5RLWXNtMYGSzhkT3Y_Pu-mn0OHTCQTJ8thFOHkaJFf6VvLf4OII4VT6oqgJd1h4imzbP1wEEga7UmfodUt7CcebCIonhO7ZsbpAANeEW-F4dVReaQ611cW7Nd7pt1utsBcM2dY08RuNu94bt7FAu3zKyFLwUZdQOAk-R_OKFxOisJBYUo7Lz6SYF3y91AcWdTsY-RFL2xaP5q98sthizKy787BHtpz85zhkZzLvetsZya5GDW4GQYk6KWfhM553Wsg20LAbPNuSKQvcAmQSWZ8UyLQxTI09XiMFVh-teBxcjNEOEVvQWHZakheODRvBg0BN6xYCtj8yFAWCafpvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S3px-ufC8rbba0IgrQEUwmU8o-igubiUTosKvMzpA37Uj-j-RI9CTpWbbZEN3gvJIyLhaJYt8b5mW89gLCD4b8SDVGBI9UMuEH6JS8p8spNjxytgGqtkRjGrLGph80UJvLWsNyM8pvbAx9DPdhwvXyOiR2DLEF055GM4mfm6_sDkNOfOGThEtLism1_kETQK722vNScKhB2MKjEaQgFiALQPW-HEXTv2iHMbQznKmSTJlh0kpNf2L3f3cFw3Vrry0H88fiVM2_VJra46qq7FoecGW3WqWyfIIZ8S5MDwcN6hnHeLL0uGhA-05efVloGg2dXVFaCPGbyue20woLPpvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qSC7an0WgYcGDRi9MjILopyRSyY18oSh424otpnqVUNAXAxaoOAPPxGewjFY00E74EBRse0f9ccRD-s2pKmSZEzXYWak1I7ASDAHbJUr8I6wbYBdYrh-Fuuhh3s1n9r11f_Zfq0wn4H1-hXACVFPMIsHgr76_PyvfDZZ3ix0PCNLqgFopNh-B8WzoMnT1IKZ1UMZMmk-84PVt-GbhOUZefWlwSPG9xNRugrAk0cdDL0XuLYMoELhrCvSs-e_cDQ_xgYCtJ9-gA8qfWaVLCDvL9v33TbQwRc4e6DdoACZ4S1HxThMPgacde3OwtmHC1h3J72YIgGBQgoaqHL6z5LV3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hfmEhhPsI2FB6uEv5815Mr46h0MW0WrFMSWNYs_wmBns9Mh3CQDh7cDsRUXbcWcMgQZ6weIq-4_vANR6JKyeQb1_MoBnCn8BLuzCjxZ-9tyqRe9FA5ZE90QF-qvRQVxEKjW_EX-SSKLwgo3FPVDY4fY6cPSg8F2hqnMcgt_VNJO3jHEeCSH-Ja-Uk6VSEmKc_6R8KWiz7J6n5zj7KBMfQgELeRl5q-bAaNgY6pWCQmrDdfg6NL0IKT3j5k9Odcf3zRfHpaZwMx2lWwxzouzqH5N7ZIFD-4TelfPsbP5gnGZ3NpKZVMXSdIm741mPUHT0UDUXWfiNq6cavVQMFH28MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ER_P-wrExbAKkZNu0XNsPkpAIL1z-G_7YJgLHqWpB8PZTE0T83YoxKyliyLIlu9tgSXHSSLzTIuY-dVX2J760Mt6_TdqLRkb8mRUrk2KJBWiwIWhEHz_8JsRDM82vHSTeJp6cmGgYpTIG0K2t7tGhUCeh_xgrC5f3tHJd5-1EQOJ7s7FzHngZZOJuhA2F4yeNC6zBJCx9WIKGkPNcYXQdIW7uawyq-dembdSvUQqZec2Twzk0wi1oxEANSaqil2bvS7YJGwV7TqAnLF48W1lZYhDyY45ksoxftRhmt8sLLlSVOolSFh4gL4-CSZ1yZsr3yBsOgnhDKy7HqntgygI6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ucRpiM2ySbD6_YgcbUM15c8FqiGvrubBr2KORP4uspY6vh0_Ngym6QbOcxv6B77E-6LpVhWSh6AhLXzbJKXca_gzXPd6MKTDvg_5B8HNQFD8f8riQBEYmm0Wx42D0E8zBKSk8VHWLZohzpi-Fehp0QkcvLeyz2dyrXTqT2uaLrmxeNOLjR1b-36nLMlqgdHd3Ljrw9oLCw7skIQ8k3C7mvF99XpNf-hK_o_ZfaRXdFPOazvVJ6UOpPr9TyM5P4vulIeFkGE1efajvxu6oVoIfRP6Nm7538RXz5wCc6Y1WwkRXBqmXX6Zb9c3_yBImD5BYUEG4AQMwZ1gFsaVfhlodg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/q-grE6jIKrlQ-4papvCpdgevIiCjPcRM4smd3zTi6iaCuUFp5Mn3hazlGH2x4nzh7B02M45sdh_sfa6qduj_K5sIKQ00nYL5QlvkkWsz_6nmuLgNpNs2xjrDKc6NTGLhpAFBVTMVDh6EQTX-0JA035q-11uHqRs1MqxYu6fGOFHfVW2CWQ16W_edXv_OG5hS2DjBT44MPLoSk_DblHm097u3p6Ey0Js15Q7C2Mwk4sV6Da8AVkjE2JpNU54fK09OggXjSRApXPsz11ws6cPTPKVqsCG61IKX9J5R3ruwlEp6-FpI6yA8YZZ-lGgqBsNFC-YVv8Yikr8z8jQYVF4oVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/omIZJ5mMuV-7nb59UvUOfad_EtxaN7vESr3Shcret_ljVVcsb-5zPaGbOn478VnJHqexAwu_JiE6kcEvan2ovqmP93-Q1nankqIiEc_snheUYnR3HPDCPwuJPjkCbKGSfa83FoO5vGDgkwQvA_J2r_H1LwGsYmTr71McZTtaauIz20lLAMSMeYM5mU-6PDcbwLBby6_tTOyGQYm9xNJx1weV6tYgInAKp_cJMhLMTjF94nt0jd2pMa_TtG8DiXPMoOZrncnsqsYjTpE8ElSnSQpZ1AR83V4qey_EidiUIHZOhBIcNYcNiPVrknOThtG9RVi7zFTabQ-0ZdNvjs6qbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #46</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XqHcsQTRkHkTbNxbgOfHnxOtYFkbUBWkayWz6yojwdhINDjsCmgn05NlLp_Wq63dw5pAD2R1ElfjEmIJ45bKVa6Mq7F3gN0JnGrqJ_xdjp7W9LGEmql4kfLLhonRGCp_FyXhqNhTzZ4-t-P4X8mDTwEpmCzHuiZtP8yPt1z58x1ROE5NUTsx_1gP0g1OJ320Q63WnC76Bt6r18WLMIRvZ8lOtsAVDaP2UYSl7IQUJXF60Jq4DDbxbb5S-Y-X21gvUvO7FFmoYR4KXrlYyuxmv7a-ym-e1GwOCEx3pwSMmag0AWAZdzWu3lM8a2oK7C5yO4fWg-3PW8ksrCXQyLM2VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoPjS49b8zYLUxNr--VI4BTAs3Nl5pKAMgf9BW9gYm9LDNE9Uj44g_c0mX9kroxspz6sZCiCxRXtfnTUr6A2680eupPX2IfPRRfeXl_jpK_B9_Gi6arjaX12TAYKwP-cNDvuTJEu0jddAaiLyse_WbRlfOUoqUitYbnfGPpu6gJ2PFux4ZkgS92-ymuZ2u3wujOZix32itfcyDtFzgMCiTalsr0-PxIf-9QlZOeY2pWmWlBZchOXPj7cu9rl4LzcLr5DK-hsxD0ocNC4CLUuqax_Qws2KrFup4rt_8Obtujc0Ry2THYtC8iYaqbWeA25YFPeT0nHCtQ0lhXmjvCfrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pfdprKGu9Xtk7bVrKHQBVXdvzZu9PWQkRrN5N_TbQZNrsRnXh05pj2kFmaRCmv_U-upl2tSIMj3zGhxyvfV0YHeQzJvuNjzlWq_BKxaJa5I5UEar87dOkpEgXlCdp25fvU1t5oYtDyZqkkCsCPedfzBqkKV-CghTaXbr-FubA_hReUt9EGm4A6bWgUrwz9S9o5w0zA8HK5GJSTW_wD1ElkAI1TYhk4wwrXNkpXVSE3f_nWDxqwAO4LeOLS0J_KSMTko0DF2vpfJ4xsAUgKT31h_ysndD__MK3gf_Y0j_mzCybpBK2GLX0r3FfdC4ewRRFWp63mDB4Em7iVlvdM7SAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHaO0M2ZQHzFZJtM_H8aJucGc1dJiWqHhUPmyBODWp8tt6Ic6DbkdZ70d9RDAIHU_6euH6O3Dh7-NgxpcYgrDeOHUwasZzgM7-8fNPhW-o53e5VJ2okaiNqGlJlW7aZx39xT8mT4mi7Y8KgkAKj9ATXlQoyQbtGPzkU-qk7EMP2elC_540ezE2qsi_U4TYIrOnD8BpK2ZI9bdpNdWp2dPLYMWdCWJc0Ey_agxQpwANRk8-4J_oHGkL0XC22YXZ2Um0WROU3O8a4uXJ98GfX8dOLCC2mBk9ZimCcKqA0vJKSUeT3Ghr0QUnA7hIOUnzHKT9tp3IxOCOpR6vF5gcivHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gIknAU-ier5nlGqyW6cnCbp3l84XX0Md6hHqf9gn4OWs_J8188Y67Okyi_6K7e6G5Msc2MD7LuCkUsDFPCe43J3fiELcLbaACrQhzsI89bhsnQjpcsHsqS1O1uPNiobqbOwi8tkEgiQlys4TDG6FthPyTsH_HEqSl74bDBeXvDgoDzd300p4axh_1cFMt-QZqJxCj6l1f8OWYrOfysSK77Vr4NsFc9yx_uyv82vu0hrQ_21oMN0AFaT2Fmj06lK_f6HOkqDdLCpHKRayeC0cQBHGgJLJuwzjh931mnLuQQxQgBxBJ6iG50jetMJsxcaNVblncWUaDQfV_0jPVFy-VA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a8_JEyK0MyM4rGEUWMahdwzW7PLZtZgqomVyAV1nqAxLxTY1x4sCNCFxccx-4DwoRVfqKv5GIP53YGe7QO3exNGuanUpznwnJ06ZnoBFOwIqwP35YnlJp_Dk_WnbvwcbPhMdT6pSpQxPXDMkDw742SKj9oCablcBCfKOv-9f7Z2VrEyzFWJBByPycvaEA1kLHRnII4-CZKEG_GxUMTteUVkMXRlMI20CN0TnSOrCxnTA8sh5Ht0EDnnjds1-MMXk6F5MT14qBa8SlhszeT-0ff-A4mK67x6h59f1tsg0t5MWgE1kiYzw5Dt9heHg6xLWenS4ByPCnwWwMrjoZCkbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QeMz4MxMa36C2Hh58a-chvEPtBln8cNDWa3YUvv_HAT5WdB30CktDLoQkhrYYK7I40cP9-l7fgaQJ2-QKdOTa7T1b2t3jkj8sZkFvOhyoEanEAsfTmCa32WDxt5Wb9hHc6Hj7mCOfomRZ_jdQh3-vQLHrJY97GNI-hEcMplB8SJ94K-MRAnBEwIB25zvZOaNsGjNrgkBwEg064A7IBolnkp_Ajlsp0VskpmDuKzIdgHehl05BXXTjiwYUQUCAn-Hgl_y1hakUIWgSWFbfqtCokq5uqf06c4vcPqwrPvER1Uzee1nnvSu9m55H0L58Fx52jDitYSONdUk3NQ2SOzp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AJOyrQiIdlOhwGwe-PEUCG_wJ6t-pXDETKXRLFsqq5gV2iaKE7jXrBOWPxckiBbjl7Pa8f1wub5BgkA4EPwLeg2eQA1bsx7Ni-dw_BVa1SjVRSlvo-o-GgnN4oVaE7vfRir2bdy_QiKSwAJzeCt8gh2g7oJ71cPqcObUr3nj5DvPe0TNJx41DoO6SOLSbB8ajfHn3g5aMZPmg-gbrb2UXVswg_K0_dN0SAuMerWD3v0APsqOPFS4T0BYcez28AHM53hWfFrc7FLNVnjfHEv3hPzugFOMFaXV7xqTZOQ5NkHdQ_K77_V2SmSTnXf4tRELMbV8eA5kTYj3Wxo4vWihYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/anE90qiAR5GWHYwy6q-RzSL-0-fsDg2Km_wwCvAahF3RgEgCjts5Qxb_5iqB2mglGyqHsbF_F-e2y3u_j-5z4jsIdNTMSe8t_g6PNb42QpE0FgdPvBdsf5vzUMCK084UjnfKgT4sLAgQXDsAfJTYf5jhjDfXVW7W8QZJePFj3VeaM9UyRN_lezXkgpbxpsFqN9SAfKckS_zdqhma1H5y9QabXliO21P19q3Xg8Swr5viBaNt1M-CgTh2bWGnGwATfLxW7wNZNS6lYlozWA0irFp1vVzrrhINKEBozUVebN_BvXfSLEmnS0i_dCXo6RqjT06o3CZW2VDKOlOI7sTQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ ShineNET VPN یک فیلترشکن رایگان و متن‌باز برای اندروید هست، که از امکان انتخاب هوشمند سرور بر پایه هسته‌های Xray و Aether برای دورزدن محدودیت‌ها استفاده می‌کنه.
👉
github.com/shayanheidari01/ShineNETVPN/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NzTNi5noEQ7EQJq_Lrp13WHee5avDp7zJd-k2BhuiLvZWY8eEUIdVphs3-sgMnomRS4qk63sSj_az72VvvZGN0JOvMDguJxHwU03xucPyx3pOPDUXn5_HOxHMPBCuJ4FJGIbyHC8VfhJmL6Jci4X09OUt_qxooHT6DWZ1TZhH-3SMtMqQ87aQnNhI1vg_M5MnrP_qpOXYD0hOMvO_4l8d8Y9ia4THu1ORPOWmHFWNUmM5_PyMNPoe6sI6XuURyBmbtme01A2kGmJQDfMFww62pJA03cqNjr1x1s_nrA0Z5gtFVFfq6jhvtS4U0I3x4UXrZ6fc2tuGNxQe5a5DicBQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HtpRUQNDW0IthqhDhjxBWyJ3nAXK2Z2Cv0IW1u-G2SBUTKQjwI2uNvycGU-K41DEfU6Lv8iTnrTETPhsU4FFyNncx7frfeiesVGi91R1Po--QFDlwYXdUB7I3Haq9ead4C72XDT6DiYwg6pru5mwZ6JwNu4Uvy5qXN1oEO4oejlFNclo_3NZR-Qs7HYjGlpN733y2MDz_SHF70A6Y-cm7qKXB55iAC_arMN2gqKfSxqP9Tn9X8wNa1KDmdSnnt695HT2_xgxcdQpxP8xtlokjR4uxFnN1qepKb4TADlQmzUf2vDj-MYwxslxIqzQppMcOhQp1aTAznUacRvr4fsVXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن Aethery برای اندروید یکساعت قبل به ورژن جدید از هسته Aether بروزرسانی کرده. اپ Aether-GUI برای ویندوز هم کمی عقب‌تره و ۳ روز قبل بروزرسانی کردنش؛ البته احتمالا بزودی براش آپدیت جدیدی ارائه میدن.
👉
github.com/ZethRise/Aethery/releases
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J8MV6F5rNrgyvmPtOlyfqXuYhecDBzH5AS9Jhw7ZrtQzlZX6YlUwNeUL_tO6H64xG-ZGJi6wvR3WSdjmeibNR90k4ZdUiipH6vfG_XHJ-lUeB52KvYOdnT_X0OuLNWSSd1JFberqtTulukzlu2IXyPZf5X5XyCdqhqY3wK2EfFRn-uuWE6uf1B1WpNbn9tFHlo3r7MSLpT4RBxI7K2MiiXdeE5A0rYHZ9PQSj1a8YNrdKYONOXh8_KwtgRlcb6MQSc22xV_IaSBXdp34nq6QgkOZahucj3kBYNQYg7VVm_cuZAK71f-kAbO9jKKP4j6o279nbRd82d6OkG663WiEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۳ از پروژه متن‌باز و رایگان Aether منتشر شده و مهمترین تغییرش اضافه شدن حالت اسکن Ironclad هست. برخلاف حالت‌های قبلی که فقط بررسی می‌کردن یک اندپوینت در دسترسه یا نه، این حالت قبل از اینکه به یه سرور اعتماد کنه، یک تانل واقعی برقرار می‌کنه و یک درخواست HTTP از داخل اون عبور میده تا مطمئن بشه اتصال کار می‌کنه. البته این روش زمان بیشتری می‌بره، اما در عوض احتمال وصل شدن به اندپوینت‌های خراب یا ناپایدار رو تا حد زیادی از بین می‌بره.
توی این آپدیت روند اتصال مجدد هم هوشمندتر شده؛ اگر ارتباط MASQUE یا WireGuard قطع بشه، Aether دیگه برای دور زدن فیلترینگ مستقیم سراغ اسکن کامل همه اندپوینت‌ها نمیره. اول همون اندپوینتی که چند لحظه قبل روی اون متصل بوده رو دوباره امتحان می‌کنه و فقط اگر از دسترس خارج شده باشه، اسکن جدید رو شروع می‌کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پژوهشگران امنیتی Insikt Group وابسته به Recorded Future از شناسایی یک کارزار جاسوسی جدید خبر داده‌اند که با استفاده از بدافزار MarkiRAT، کاربران ایرانی را هدف قرار می‌دهد. این عملیات به گروهی با شناسه TAG-182 نسبت داده شده و طبق ارزیابی پژوهشگران، ایرانیان داخل کشور، مخالفان جمهوری اسلامی و فعالان مدنی مرتبط با جنبش‌های ضدحکومتی مقیم اروپا و آمریکای شمالی از اهداف اصلی آن هستند.
مهاجمان برای توزیع بدافزار، نسخه‌های آلوده برنامه‌هایی را منتشر کرده‌اند که برای کاربران ایرانی کاربردی یا جذاب به نظر می‌رسند. از جمله آنها می‌توان به فیلترشکن Pis2ray VPN، نسخه‌ای جعلی از Star VPN، برنامه‌های YESHICA، YEPlayer و YEMPlayer و همچنین یک وب‌سایت جعلی با هویت Starlink اشاره کرد.
بدافزار مذکور پس از اجرا می‌تواند اطلاعات سیستم، فایل‌ها و داده‌های مرورگر را جمع‌آوری کند، اسکرین‌شات بگیرد، دستورات مهاجم را اجرا کرده و ارتباط خود را با سرور فرماندهی و کنترل (C2) حفظ کند. پژوهشگران همچنین زیرساخت‌های جدیدی را شناسایی کرده‌اند که نشان می‌دهد این کارزار همچنان فعال است و احتمال ادامه فعالیت آن وجود دارد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gm0Kag4Ump9rt_lhZP66xpPKqqVo_rhMWp3GCRNsfAcqtUNCfTkL6QngR5pz4P9Cy4pmFsOW9l-u6kd8uhxY9LzKFH4N6mzM3UlX7DxQ2bYVmx_9m6T15L_lnhZweNXMPxVSMQ0pIKBDNHWRNIAouF-TVbZfORPNj44E5alCwvyIgGrvnUgG8yeTsEs3buTxDpJ3opKlWjeA7EoIjLQiOrY2bdI1JUzUwlyoJUzS7FnvBymyjEFyu5_ygQakFwE_hAISsIDF8QC9oxoc4J3x4oEPnIfmWwss2qMJCDdwgIwjwZ-GVm7TGjYK_8ywZE09hGjSFgz6_pTnQCz0lkgFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران امنیتی از شناسایی یک زنجیره آسیب‌پذیری جدید با نام wp2shell در هسته وردپرس خبر دادن، که می‌تونه به مهاجمان اجازه بده بدون نیاز به احراز هویت و حتی بدون نصب هیچ افزونه‌ای، کد دلخواهشون رو روی سرور اجرا کنن.
بدلیل شدت این آسیب‌پذیری، جزئیات فنی و کد اکسپلویت فعلاً منتشر نشده تا مدیران سایت‌ها فرصت کافی برای بروزرسانی داشته باشن. این مشکل در نسخه ۷.۰.۲ وردپرس برطرف شده و برای بسیاری از سایت‌ها بصورت خودکار در دسترس قرار گرفته.
©
slcyber
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/STkpfn8nUd67YmfNKq2svWQdvYHg3wWsfwK8fmFKc6_H4JgGtbkbJ3ihvjSWe3-TSvJ1z-K_6xh_eFkcj8UcwYpgnK7whCdvD57iRaiJOeiYeCyBXAJverI3DFIVFl9OW-bqC5bCWyAAZhrjXcC_Ql71QZDvXhbgiNV0lBI-dTnnH1vg0ZpPwxOu8_ARHkyn9rlcKMa4ZMfDPAKHtHv4WYJyeUSoDwFu1QeA_sYFB7Nmaj0wWUBX3h3-uEAOzknKKJvh2ZGpe_JBEt7260wZXLBJOX2o61jp-IBGUsmNp1ZNnOq6xyA0H6clbM7LqVdN3TZUde7V3hEOKtSYQfkCSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZaBpIWqD9XEIsA7tL85I5wLIgBo4EKoosb2lMlHzWRPTg7UqUh3WB8FZn3lScFguqCq-uFjQ6LTmAepBDqAqwANskoJB0Fb-TX0upyYVLvqqsCPlquZcm67LKFLgHcn4zcbV9wF4a-yAjYluMn6VqsTrLBIgu1CZvHIoLTA4JKFBeggLj-ZjhB5pnrIxjy2dIrLv3F7ELB3R2OfFov8EyuC_F69a3wN-1w7MBLYnL3o-2co09-tV_A3BkJeNGH4sjSmufffCusbIz8YJT1-bEBnb1JFir8H1Fukp2FQD291kekJuf2n1GQo7KI9txKieA7lmFx-ZmxJ1ycuPQ5fCDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ dicodePing یه کلاینت متن‌باز و رایگان برای اندروید و ویندوزه، که مدیریت و اتصال به کانفیگ‌های مبتنی بر ایکس‌ری رو راحت‌تر می‌کنه. این برنامه از مدیریت سابسکریپشن‌ها پشتیبانی می‌کنه، می‌تونه بصورت خودکار بهترین سرور رو بر اساس latency، jitter و سلامت اتصال انتخاب کنه، از حالت TUN/VPN پشتیبانی می‌کنه، آمار لحظه‌ای اتصال رو نمایش میده و امکان تعریف دامنه‌ها و برنامه‌های خارج از تانل رو هم در اختیارتون قرار میده.
👉
github.com/mcodersir/dicodePing/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">پژوهشگران دانشگاه میشیگان، دانشگاه نیومکزیکو و مؤسسه فناوری دهلی، ۲۸۱ وی‌پی‌ان رایگان اندرویدی با بیش از ۲.۴ میلیارد نصب رو بررسی کردن و به این نتیجه رسیدن که بخش زیادی از این برنامه‌ها برخلاف ادعاهاشون، امنیت و حریم خصوصی کاربران رو به‌خوبی حفظ نمی‌کنن. توی این بررسی مشخص شد ۶۱ اپلیکیشن بخشی از اطلاعات رو بدون رمزنگاری ارسال می‌کنن، ۲۹ مورد دچار نشت ترافیک یا DNS هستن و بیش از ۸۰ درصدشون هم با سرویس‌های تبلیغاتی و رهگیری در ارتباطن. علاوه بر این، خیلی از اونها هنوز از تنظیمات امنیتی ضعیف یا روش‌های رمزنگاری قدیمی استفاده می‌کنن.
اما نگران‌کننده‌ترین بخش گزارش مربوط به ۵ وی‌پی‌ان بود که فایل تنظیمات اتصال رو از طریق HTTP و بدون رمزنگاری دریافت می‌کردن. این ضعف میتونه به مهاجمی که روی یک شبکه عمومی مثل Wi-Fi رایگان حضور داره اجازه بده تا اتصال VPN رو به سرور خودش هدایت کنه و تمام ترافیک کاربر رو بدون اینکه متوجه بشه زیر نظر بگیره. به گفته پژوهشگران، ۲ مورد از این برنامه‌ها این مشکل رو برطرف کردن، اما BambooVPN، Free VPN و 101 VPN همچنان در برابر این حمله آسیب‌پذیرن.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fPyaq5dtfzGTHftO44uW0jkO1E5F8s46m9uaBMG7mNQMyk5_ZqiEYGbExmrw3DZltWxlwctslw2ADOohMnXr-FbuUPo_p_FcYNcBvVyJrGvuu9KLWrpMwjUcLUh4LTO_kHmi4dK1bfdOuGIVevrRVIfAlhYM7eneufH3hmbgf91Jzg7jthnpJN8qAv52t0Evg669nCvF-y9-CsD4fbbapouXTlIqadur7KV28_trwEAH9RFwnnqjFHHjR_cA7j2WWu_Xq4xdSP1wKhWZy_Z6Vweb9I6rhI9s6Cz-h2DjtU1KC8lCNKY44Ksasf6IWfejB9frGcaZA7wWENEcWqsfFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aethery یک فیلترشکن متن‌باز و رایگان برای اندروید هست، که بر پایه هسته Aether ارائه شده.
👉
github.com/ZethRise/Aethery/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSQOjnYYqEhrXrnayP7_gsuAdm0kTPMUR4PDZLDYfAwLXlEWfageniQxbCERX_ASRp0PPkyMYxWcJJaCZJTQYxTbn9dnMIBSMU_8lL3pStOJMH0kOCeuWM5V2dew9ZCmXcWGuV6cCBJ3FfGorxj3jlbzNr4unH5MtgC98LWIrxI_diznmSAVec_PM6tFMW7A0pGLPUD7GO2yeF4gl-ycSl4sXlzeXcFAVlYGtdhG3CCk8QCJTam1KRFrWXsBYEMQutmEV-gbPpPBizn_GSaGLFznjKfHbY49uAK2kpLDrIf3FEa6lB7u3CxI-9wr2OAEVPLAMqina0pu-IdR1_XzJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت رسمی Sing-box برای سیستم‌عامل ویندوز بصورت پیش‌ازانتشار عرضه شده و طبق اعلام توسعه‌دهنده‌ش، همون تجربه‌ای رو ارائه میده که پیش‌تر در نسخه macOS در دسترس بود.
👉
github.com/SagerNet/sing-box/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OjuL1objyncocDUPlUh6LT-zARGxQFrMGNqCFv1tOuvm9QrgKkzDGexckHSaoVT66DbUlo79l32SCMxy_BOZL0dkQdTFrJL6vt8rfrXH8YGlpU8q4NjNAe5bVsWGyYeVFGZLbu7t9qiODx-3uMPfjDORu5bLnO8_xIi7rFQqnxTzwGXzfOCGQXWR-SX1DjU7c1i4wK2KOpeTD2udtQDA58Cu5DGeO8qz57di23uFVm87IkFPLCp1dwuS5x2uHF9UzTsoQELyKQ9hPqY-_Ugur9SzyfeFAMQxe1_fx12rlgX_H4_NC8NLm8HJqtsZOyc07vxhvI3CXvHO7peYAfRryQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Aether-GUI یه واسط گرافیکی برای هسته Aether جهت دسترسی به اینترنت آزاد و دور زدن فیلترینگ هست، که دردسر سر و کله زدن با محیط ترمینال رو برای کاربران سیستم‌عامل ویندوز حذف میکنه.
👉
github.com/MatinSenPai/Aether-GUI/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TbL5gGc_MpCECKUj2HLV1hhDtq1tNHwl8WxjQgQD33_KYnlVOytf9T_kshMnH-3y9LfTXtlu5cVGCP6y_7McoZgvF9X39ULnVmsnIu3W2enPRmpABnKkBaExmeP4ojPJnfmKBYVDTyMVmwRYTkwggfy2BUo8iCempOxwGRp7rfLg-Pip3kOCKQO6_p7r0BXJXQgYtn9vOz6m_9rore_V1lTkL438Jcld4QzuHd2DBFxbzvOgPF_LRNCMXkRDzEElmOgWYQgTPkL5DO8XPmjq6voq5PLkY3RnIPHWrSqp2MBw8N1AxbRa9o2nb5P41HH7_dYHEJMXa7yqKQbv3W5u9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت در بروزرسانی امنیتی جولای، بزرگترین بسته اصلاحات امنیتی تاریخ خودش رو منتشر کرد؛ بسته‌ای که ۶۲۲ آسیب‌پذیری منحصربه‌فرد رو در Windows، Office، SharePoint، SQL Server، Exchange، Defender و سایر محصولات این شرکت برطرف می‌کنه.
اهمیت این بروزرسانی صرفاً در تعداد خیره‌کننده آسیب‌پذیری‌ها نیست؛ دست‌کم دو Zero-Day Vulnerability پیش از انتشار Patchها، عملاً در حملات سایبری مورد Exploit قرار گرفته بودن.
©
PingChannel
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mbu9Fr7Yt1MRG-79t_HuzeU5n1AGLZ5gxk3Q1OwBzRzmhXDuWBaQTn5trIQBh9RTEYfdDZO43gpLC2ql0LRkwbAMdeYeQLGAcdP8xFEmTO3Hp-orFoWidckW5wajrUZ2OrbglF5SIuaYXT2yu59TyLwfUfKTZ5tghIWHiiRXtGO6gdeTOmgpAG5lNJzf6JqrbZOu9eqM5tj1bG4lBhKI-DxVIEezor-UY52tkfXdryQUSUwYTIPn5ZMcx0mcQXj11Z9taaoFH2_Vi_AmVsldqnZGRBF_sU3UikkKVLmrLxamdGvOWxalhJpbujTCFG2u5UjvMjflwinms4uYIGtZJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروژه Aether یک ابزار متن‌باز و رایگان برای دسترسی به اینترنت آزاد و عبور از محدودیت‌های شبکه هست، که با تمرکز روی سرعت، پایداری و مقاومت در برابر فیلترینگ توسعه داده شده. این پروژه با ترکیب وایرگارد، MASQUE و WARP-in-WARP، ترافیک رو تا حد زیادی شبیه ارتباطات عادی نشون میده و به همین دلیل روی شبکه‌هایی که از DPI و روش‌های پیشرفته فیلترینگ استفاده می‌کنن میتونه عملکرد خوبی داشته باشه.
یکی از قابلیت‌های کاربردی Aether اینه که خودش بصورت خودکار اندپوینت‌های تمیز رو اسکن و بهترین گزینه رو انتخاب می‌کنه؛ بنابراین نیازی نیست که تنظیمات رو بصورت دستی انجام بدین. بطور پیشفرض هم از HTTP/3 استفاده می‌کنه، اما اگر شبکه‌ای QUIC یا HTTP/3 رو محدود کرده باشن، میتونه اون رو روی HTTP/2 قرار بده تا سازگاری بیشتری داشته باشه.
این پروژه روی ویندوز، لینوکس، مک و اندروید (از طریق Termux) قابل استفاده هست و توسعه‌دهنده‌ش اعلام کرده که بزودی قصد داره هسته Aether رو با زدن Pull Request در فیلترشکن‌های ابلیویون و دیفیکس ادغام کنه.
👉
github.com/CluvexStudio/Aether/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VpLHfv8mKdj9EsOgIQNRVQVYxIEPVegCfaQE3qrPmfihgfNiqvmzjGhctLUzZ2dEx7MMXE7tQ3mOPVILsNAYvvHXa9miy96oqP8P7qWGbKjiGfAp4uKIKVI6AvoBrWn0oW3Ai6JOC2rYo_bFssCCDRGI7LXZrYpauaqRhI47paDkIKUci6nAG1aCeqHlzyv_Niyopt4ayNr5qIsKFg5Gk_MlsGWEIj_GyxMQiZ5BqwOUa7e1cFpjcMOJASl3FzB8I16u8L8pXHVscMW9SiYhQpVL226O-L9by6EcT0nnuzApPyJndbtwJdoE96GwBJNmySmRVkHjap6tNDOlUVDd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دامین
t.me
که بدلیل تحریم‌های وزارت خزانه‌داری امریکا مسدود شده بود، مجدد فعال شد.
©
Linuxmaster14
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wuz9M9ck3Wm3rqYAXM1pVDNCKkXqIHRsfxTEH0vj93ixKzxcAf8uKvLp-UcJFDqZBXjVNYjPbDHBIqjNIr-hk8HY9uMuGb5Eb_GzzqXkUvf05g1hCoPYW_M_L9jjosd-lgleKI03dXHM5e69e4fWAuuvWXoU9cqVGbiuCYtKclwE7fDebneeNYE8kuY7OLXFL5Gkyhv6fJ8KCrr_9olZc9jKLBHLCMGEwwd7FWhZ37Jsz21m5FXDHiXQSrEeEnVXm3ApAWyhcT350gDU6ZfDkOPBTG5Xh14w5RzfxI7B1ALiShzdHs4M_4wX6MWo9ir3TkzdnDBzc0wZr1YZdUEipg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به یکی از شرکت‌هایی که API می‌دهند مشاوره مارکتینگ می‌دادم. چند راهکار برای کاهش هزینه جذب مشتری یا CAC گفتم، ولی تاکید داشتند که باید API‌ رایگان هم بدهند. پرسیدم چرا؟‌ خیلی راحت گفت: چون رایگان است، طبق شرایط Privacy & Policy تمام پرامپت‌ها و داده‌ها و خروجی را می‌خوانیم و ذخیره می‌کنیم. فکر کردم شوخی می‌کنند. بعدا دیدم نه. جدی است.
(...)
مواظب باشید، لااقل اطلاعات حسابداری و مالی و مارکتینگ و اکسل فروش و لیست مشتریانتان را به این API رایگان‌ها یا این سرویس‌های هوش مصنوعی حتی پولی که در ایران هست، نمی‌گویم ندهید، می‌گویم دقت کنید.
©
AdelTalebi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gDASkXyk7rLv_AhOguYJPQ-TzP7qJY_m8nEF5R1Q-JWTbXfTgcvbnVJgZbRlHw7-io1y-JyQgeLCrhuGX2tPejHK9UrpBL55tTdyT1roEnApC3n14lnmGL0tTCpFfjkcQQpQX1A6JsaY639eEefTql0dktJYJHlOlGwS8VTuElg1M85Bgaqi6TvXYo2iBVu7wb3rz1hxg2X-GDSGQHW9tT95fjxWpixPkA3l0AUE-T0yeG75QCtGfKSLmSXGqwrSh_NsXS3bc7Fp3oDpmncMFqdJuBNUrpsOp5btM8s9XJj1EcoKOCcwcVY0V_Hu27w81Twgk87uCXKp6EpJAUulNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروتون در
یک مقاله
جنجالی ادعا کرده ویندوز دارای شناسه‌ای پنهان به نام GlobalDeviceId (GDID) هست که میتونه یک نصب ویندوز رو بصورت پایدار شناسایی کنه. به گفته این شرکت، این شناسه حتی در برخی شرایط با وجود استفاده از VPN هم میتونه برای مرتبط کردن فعالیت‌های یک دستگاه به کار بره و حذف یا تغییر اون برای کاربران ساده نیست.
پروتون با استناد به یک پرونده قضایی معتقده مایکروسافت درباره وجود و نحوه استفاده از این شناسه شفافیت کافی نداره و به همین دلیل از عبارت "ویندوز یک جاسوس‌افزار است" برای انتقاد از سیاست‌های حریم خصوصیشون استفاده کرده. البته این عنوان بیشتر یک موضع انتقادیه و نه یک نتیجه‌گیری فنی قطعی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">طبق گزارش‌ها اینترنت در برخی نقاط کشور از ساعات گذشته با اختلال و کاهش سرعت همراه شده و دسترسی به برخی سرویس‌های آنلاین با مشکل مواجه است. همچنین گزارش‌هایی از قطعی‌های مقطعی و افزایش خطا در اتصال به خدمات اینترنتی به گوش می‌رسد.
©
IRRadar
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ClMkI8g1Zx6q-h32xmvFYvCMNLynzor98KvF7vIPVvDU3t6-ouHaw4NfGMBeRXECuW--numd2gn8LJOdF9Xj9sYC0mhPjlBeBadm3plRWm3stoe_ClzCDfVbWGyNT9KpJxnAt6uuln21K65a-1oVaDSVl2at06UkrmkPk0lawKuwL_8l-YCNFwm4z1W-C4CDUNNu-9ZQhCONwTZiWhPn0O7POJ5eJi3JHWwVMAVCikAmomWSBxtB6xuvUVxTSDoN4XAw8IGUN6VCgqQRri4b4o_4rFKfzPSh7PcFxCMWOepVwwqahyw7QU2fSuVySTjXY-QkkcgCRP_oLh5SIAn7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XiLHkcMG9chNTk0FVK8RCYgHMwcsZB45jrx-uzQjsAXvik7KhrSsNBl3ZgKf0AIgpw6apo8VtBh88nvwTnOUqL8LTB_IC633rBlZZ6Rxv9K5bubwhwIyLDPoCfAbjh24HQQBycHaHat7xSMH7GM9FNxNgaIpDiJ1e0IE1T9zCP3dYGnwiTnWcpNBjFjZF45KqvUVJ_ecHjs2fJMFgPrCxsUwUtiq2igf9Z0EsAM_ceEJzm7iwPos3kyXMYYD1d1Jgg11eAyigHH9G1fYNewiVsoO1dJG3HAgyOvkbNHF5japcLcfLNYxnLwM4tEZkimYeK6f02jo4hGpS3CbHQjBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنل زئوس یه ابزار متن‌باز برای ساخت فیلترشکن رایگان روی بستر ورکر کلودفلر هست، که امکاناتی مثل آیپی و لوکیشن ثابت، دریافت خودکار آی‌پی تمیز، لینک ساب و QR Code اختصاصی، فرگمنت، شبیه‌سازی فینگرپرینت، بکاپ‌گیری و ... رو بصورت یکجا در اختیارتون میذاره.
👉
github.com/IR-NETLIFY/zeus
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t6pOBDVnuLICE05NB67AOTiqgu8eHVOwteIzgcFS7j4uBb3wsT92oGBLOJwELlziRz2DvKtWRtHvneEn9rmhisa-gObzGlo_RYGHzkTctAlGjL1qrk4pM-yGxETd54caUhOX2f-nifDqzHLqg2braLsHKs3WiICuVF6Xtz8OUoTwNSH2cdQB5Tna2t4aEY63551nqf1uGSftjOSM0blwdNRzRLzOqvhP9_NdW3yBx_xYKb2uVkLA3m9mKK73bHj060NcVZGzlY-ASgSloxP_Gl3vTYK7jT_g7w-zfiwzmJsedChU03OWjjh5LUVL8vTW7IFhsY1CzfFqrPiHzeeYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکروسافت یک آسیب‌پذیری روز صفر در Microsoft Defender با نام RoguePlanet رو برطرف کرده که می‌تونست به مهاجم اجازه بده تا با سوءاستفاده از یک نقص Race Condition، سطح دسترسی خودش رو تا SYSTEM بالا ببره. این مشکل با شناسه CVE-2026-50656 ثبت شده بود و حتی روی ویندوز ۱۰ و ۱۱ کاملاً آپدیت‌شده هم قابل سوءاستفاده بود.
©
bleepingcomputer
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GrKCDx-JCUbH3KI8VaOl_0TweqAwU3mgksa9Ei91Z3b9oFOO_ArPHwDgZPt8Duq4nphhkYc8ZLWsfUABN5xLQZM2uwBoo1k_vBJmQe7KXEYlMwmg_tXQg2FqShWVD6zVN9NCTdBFM7SwaPwW9HZ16MDiw_XJWQk9K3J_9YBqUejor1zBw49GLJieWUVCfrExmaEOME_jUnLsw4YtCmwrLcbwgSzKrSbvMdWe-FRsTkCGSc-mbo4MYHR2QL8GMtH2fb8zk0PgjFCSqLMufRv7Z-N-acB4IIEYTvyLjF5Tn4qdQGxEFUUpQA7gMxLDIaFgfqO6gbV8Hn63qHEl_4a0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاینت اندروید NipoVPN که برای اتصال به هسته این پروژه و مخفی کردن درخواست‌های HTTP داخل ترافیک عادی وب طراحی شده، حالا روی گوگل‌پلی در دسترس قرار گرفته.
👉
play.google.com/store/apps/details?id=net.sudoer.nipo
💡
github.com/MortezaBashsiz/nipovpn/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YHX7S1hzbVohER1Ffj4RLaJ1KEM6JX_7zZ1j3UxNAk4a0l03pdK6UPryl7M6y8LI7HOfua67ofWMgUS9A2XRqYvIo5ema6Nj1q9TzKanVVEqVLLRD7cZblsqOQoKJIb63KO2QqMYIhFrghXwXRBbG9QjL4AY2CT2RNv8WgmG_9kIKGexYaGAWwMhIoIrYaykFO6OSegZyDaXVW1bD2X4qtp3mlrhPy8M5-zY_vk3cBl5Vok1-ccxgJv1STNcZPYV_TD9n_YtIpp1-tdECsr7ISxUyZyDMo-WAnv-hA6RycLdg_ljSbkO-IE1phTzOuju-tJrxZHJNhrMGf1_WjAvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابزار BG Scan یک اسکنر متن‌باز و رایگان برای پیدا کردن و اعتبارسنجی سرویس‌های شبکه هست، که اجازه میده چند مرحله اسکن رو به هم وصل کنین و عملاً خروجی یک مرحله رو بطور مستقیم وارد مرحله بعد کنین تا فرآیندهای پیچیده راحت‌تر انجام بشن.
این ابزار از پروتکل‌های مختلفی مثل ICMP، TCP، HTTP، TLS، DNS، DNSTT، Slipstream و Xray پشتیبانی می‌کنه و علاوه بر اسکن، امکان اعتبارسنجی و مدیریت نتایج رو در اختیارتون میذاره.
👉
github.com/MohsenBg/bgscan/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6fgahJUdqedkk3x5oeGycNdL-YKH39n4owjxuhBdAOQzDxyGxHY3LOlGLjRtHWlrKJanUZD0IndHmIltPJnQFCfl5fXqecmlinnLE_MtsJ950iPU3daUxl8Y2OOjgMKsWVPs4hySxQLwo5iOWwEk1hZwmLUCr-Wt1ea1VjmaYhGkUq9_ImA6elGXqSlcXeXhrWx9u7hIa91tqfFOAYIsQF7ZIjM6cTDe3YuDDVf-DJzUdaGTEM5buEywG8FBZo7hwv5CENDa1MTTsL-Bk7lq7MFfYh6pGQwpG4z8bjJOrPnZy2EdRHXCv1H-IrFxDEtRerp4iyEYymV4I_3cA1uBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه یه ابزار برای اسکن، استخراج و اشتراک‌گذاری کانفیگ‌های فیلترشکن هست، که کار پیدا کردن کانفیگ‌های سالم و به‌روز رو راحت‌تر می‌کنه. این وب‌اپ میتونه چندین کانال تلگرام رو همزمان اسکن کنه، کانفیگ‌هارو بصورت خودکار استخراج کنه و در نهایت یه لینک سابسکریپشن بهتون بده تا مستقیم داخل کلاینت‌هایی مثل v2rayNG، v2rayN، Hiddify, Streisand, v2box و ... وارد کنین.
توی کاوه می‌تونین کانفیگ‌های خودتون رو با بقیه به اشتراک بذارین. علاوه بر این، حذف خودکار کانفیگ‌های منقضی و امکان رأی دادن به کانفیگ‌ها و منابع از جمله قابلیت‌های این ابزار رایگان هستن.
👉
kaveh.yebekhe.workers.dev
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMtC-Mi7evhEdlipPfOG3fgQGEF35yCMX0P0IODgU9mRsLr47dJvmrShQidcfq0X-USYzE6RXsHSFANUY-CIaLpYkr0r2U8kFK_e77S2GRjepV12joD3W-1Yd7VavItGnhEhsoNnZ6njrx-sg5riEl8RbsjCPCWfykAgnRr6e_88IXADD6nlDj_WNTglvcVLzVI3BtbzXHOVlQwPaR0WzzxrkdF-ga9-rgbXlaUyYwC97kJNyt_bPx6wZJMiIjYLXjIrP0grChfS8LFFL850ksjFU206WwsOGErCpGUX8vOq2uHYSdjBAVDiaHAlxW9ot2Xbi62JHj2w-96P9hH-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ابزار MTProxyMax آپدیت جدیدی منتشر شده که توی اون از بهینه‌سازی‌هایی مثل BBRv3 استفاده شده تا عملکرد سرورها بهتر بشه و مصرف حافظه هم روی VPSهای ضعیف‌تر کاهش پیدا کنه. همینطور در این ابزار که برای مدیریت پروکسی‌های MTProto تلگرام روی سرور شخصی هست، قابلیت‌های جدیدی برای مقابله با DPI و اسکنرهای شناسایی پروکسی اضافه کردن تا شناسایی و مسدود شدن سرورها سخت‌تر بشه.
👉
github.com/SamNet-dev/MTProxyMax/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CwGx5y1_Kx5MsOTHtADa7Re1nUe9I8BNEVmvNmNsa9aiRrPVrcMoadTtfOC_1nMKvy0VMIjQ8OakkHLwGATY8dnG-t7ZLhTt5edyBdnOMOkFNJ6swk_T2AdVRofhQmRCaBhw9RDJPxAFUSIX30ShmNWiXyiw2DMPmq7h0dv4uhBkYP-oP4t_sfTmgTGNihT6BzHLhEr2oNO3JyZMDcN5Ib3ii4xMF8YElSDeEi9iAwIXb1H-UInMS508bpNuTfGECq_9IESGKF6098la7FPgl4mC0BVJJJVAskC6ujR30HrptN8J9ExoLX4VNE0NUyKalfJ9fKxpKwpxCW39AohfoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ Intra با استفاده از فناوری DNS-over-HTTPS (DoH) درخواست‌های DNS رو رمزنگاری می‌کنه تا اپراتور اینترنت یا هر واسطه‌ای نتونه آدرس سایت‌هایی که باز می‌کنید رو دستکاری، مسدود یا به مسیر اشتباه هدایت کنه.
این برنامه فیلترشکن نیست و آیپی شما رو تغییر نمیده، اما چون جلوی سانسور و دستکاری DNS رو می‌گیره، در شبکه‌هایی که فیلترینگ از این روش استفاده می‌کنن می‌تونه باعث دسترسی به سایت‌های مسدودشده بشه. علاوه بر این، رمزنگاری درخواست‌های DNS تا حدی از کاربران در برابر حملات فیشینگ و برخی بدافزارها هم محافظت می‌کنه.
اینترا توسط Jigsaw (تیم نوآوری گوگل) توسعه داده میشه و سورس اون بصورت متن‌باز روی گیت‌هاب منتشر شده. این اپ از طریق گوگل‌پلی در دسترسه و برای استفاده ازش فقط کافیه یکبار فعالش کنین، تا در پس‌زمینه کار خودش رو انجام بده.
👉
play.google.com/store/apps/details?id=app.intra
💡
github.com/Jigsaw-Code/Intra
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gW_hoXjaktQBa_BA_GeqIxDPzyzqdkjhCnIq5gNUIQwM_4kjqQ-UJnuDDOnqlyXq8THEqeSHPI9VRVa_n150CeLsVyzZS0hGyUIJR48Dj_FZo6NAPRWjMZCJvZ97mbENG_nNe-dAa6xFAWG9TvXHfYWe1VFGwd1HMwj6u5gKlIxUJ5qSxHnnsAsXDSFeiJBpXTK4dtMY-MmOO6IZO7VZjXV9pqMsK42KDgyubyBBwjpC_KR4Ia4B9GXBGsOzJqCtlSLdOhqWycIJhsFggWUPKRh_SfDsR38eE0-zD6rJxtXK21-acicHGBN1vEJSRRxEWG7eEj32mDrrvl5aBmp9iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محققان Datadog میگن مهاجمان با استفاده از بیش از ۵۰ حساب قدیمی و غیرفعال گیت‌هاب و توکن‌های دسترسی (PAT) افشاشده، از طریق API گیت‌هاب در حال جمع‌آوری اطلاعات سازمان‌ها هستن تا برای حملات بعدی آماده بشن و ساختار داخلی، اعضا و ریپازیتوری‌های اونهارو شناسایی کنن.
توی بعضی موارد هم تونستن ریپازیتوری‌های خصوصی رو کلون کنن. به گفته Datadog، چون این کارها با حساب‌های واقعی و API رسمی گیت‌هاب انجام میشه، تشخیصش از فعالیت عادی توسعه‌دهنده‌ها کار راحتی نیست.
©
thehackernews
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BKzH_2baXnuC2A8dl7056c_u3-8rrLQ7-NnFUo3Wqm8xTaWW16V5DF0Ci9FLnHtQO5wmu2jvBYoZdqdPy7Pl8zXjj2OJhccKuoLwnLNR4Bvmh8QcbWwFSpGUxScrupFKzHsq_k8VrfSldRIwJbazNYG8OIN23CD7q-UkMy2fbMxHc9m5g6iXCtMZrkxMw6rupOWa2Rb4lwGYI5O9WGRVFZykVu2zlrvSw8vZvgxcd-0pXXnGFhmf-LQaYI9hmvkmfxjA8HMCHONbdo8TSxez-SNNQvu3qfmDBAdrmnXASHL8J9N-EDjLna2fZsa4Bp4YH6WQaMRI2ErwnxYpnZl_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AIo-PQc6muvJ3qMfXOk7Mq6OdQ7zu0_W5oNkl_MXvDmmhGWpWq1kx4QRljC8nAYt8kPnOKU66M6t1vCuDdGSaAzdGf6L4_Y3BDh-f5cVGN6P8s8VqWpoevPoKUqugMI6nJ8fVFuzXfhnVt4OJDBGCVxn_BDgZuS63ZwAViaVOl1-PFNzA8aWk5OgrUq7k36gkMAaQ5zcAe-ea0qvsJpLYogj0fsE4SCngRExcJHS6IIYRK7y0b6T5ok2ZbSYavW4M9Ekex1ty1VcJ84B9om3eZHew2R3w7YQJhQBkM7jKy8Jz6kR5XnyfS1NmLtbzYGNeOJv4NKGiffxCCImmWNCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اپ GRoute یک کلاینت متن‌باز و رایگان بر پایه هسته ایکس‌ری هست، که امکان استفاده از پروتکل‌هایی مثل VLESS، VMess، Trojan و Shadowsocks رو در کنار ترنسپورت‌های مختلفی مانند REALITY، TLS، WebSocket، gRPC و XHTTP برای دیوایس‌های اندرویدی فراهم می‌کنه.
این برنامه از قابلیت‌هایی مثل اضافه‌کردن کانفیگ وارپ، مدیریت لینک‌های ساب با بروزرسانی خودکار، مسیریابی تفکیکی، پروکسی برای برنامه‌های انتخابی، فرگمنت، Sniffing، نمایش لاگ‌های Xray، اسکنر آیپی تمیز کلودفلر، امکان تست کیفیت اینترنت، بررسی پینگ واقعی، تاریخچه مصرف دیتا و ... برخورداره.
👉
github.com/SuOracle/GRoute/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
