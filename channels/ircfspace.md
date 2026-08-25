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
<img src="https://cdn1.telesco.pe/file/g2UosGblRzEnnRTiUVVxC_u_TlZB8mVBbYE7RqC1dUqALspYotsJOmcI15gYSDYDkgGLZQey30AZdW9TxcsH-4knggg0EUyfXUmfyccPT13xK_G958iJskWxjRCZIJtWWTO2KhTndDcjlCoj3vbHcY-F5Yz2wZ7V6dF0MV8_PeCM2nEJQV0nqLFNQqj2w2t7XpqaeJv8c9NNeVSo9_0eQtiKkxMNXgHhn6ATFpCtHxABkiZFQRLaT1pQgye72bblcFPes79etwxUfM5ZAFDmHcq1xzzJitLiAXNo9ZtXiIHSasgSTxH78ui_ww6-qy6k-In0uvMDRG7JoL9lyELgdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 IRCF | اینترنت آزاد برای همه</h1>
<p>@ircfspace • 👥 96.7K عضو</p>
<a href="https://t.me/ircfspace" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 این‌کانال با هدف دسترسی آزاد به اینترنت «به‌عنوان یک حق شهروندی»، به‌دور از هرگونه وابستگی حزبی، سیاسی، تشکیلاتی و ... فعالیت میکنه!https://ircf.space/contactshttps://x.com/ircfspace</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-03 19:36:14</div>
<hr>

<div class="tg-post" id="msg-2568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">از بین همکارا، اولین نفری که تغییر شغل داد و رفت سراغ آهنگری، شدیدا تعجب کردم! با اینکه خودم کم آورده بودم، ازش خواستم جا نزنه. اما بعد از چند جنگ، کشتار معترضین دی‌ماه، قطع طولانی‌مدت اینترنت و حالا تداوم یک آشغال‌نت پراختلال، آدم‌های ‌کاردرست و خفن زیادی رو از نزدیک میشناسم که سال‌ها در حوزه‌های برنامه‌نویسی، طراحی، شبکه، مارکتینگ و ... فعالیت تخصصی و رزومه قوی داشتن، اما در این چندماه رفتن سراغ مشاغل غیرمرتبط مثل نجاری، دست‌فروشی، مکانیکی، واسطه‌گری و و و ...!
لعنت به جمهوری اسلامی.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/ircfspace/2568" target="_blank">📅 07:54 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JVrZJbaW6MBfSrjhNsKIYyvGtORkJglAsnitiR-_lG24BV2hdg1y3ddQphsUmXLPqiItCALENPu4RBwl5vmZvapnz9njxAP72Zhq5NAU2UcTZ4z2OxJ2DzacqCHf8MkPf5GJrRyS0-qri1SoFN3fozclsZ9h55YkkwWG8qr1-ALQdJmUIdeA8-msw5X7Uv_8RjQxjYwexHKYpwUp9oH43QPABooTH3A-8Fsal8C8B8Wuh13tuKEOPnmSEJDYwvSylt0EffO2HR-dUeXZUgTrT_DdZ6ZzU92CsjGH73p0bl_pgquElXHKamFGK5Klj0iSQmPVQ_PL4PJs0VHrVbC4fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/ircfspace/2567" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gU1Y7WjZ9wP_q9JZZHEBwayoWfd8_Fpj5zbn97OBXRmMDdBUhasFCe-3agOk_ktJWxyQBxR1KP-XVB7zKjIQbadcOBbyAFfw-y709K1G7jCYHYwn7OIzrBgclIz4h8AU3Y9JcX3zzDUfe43IEfQyEnYa4jF5FGomqWOVQbwzi_I-ieHwsHkwYj97_PYcBP2Y_319-h2Rdn5JQEzvywFo7jvVAvxvt2nQf5ztW1ZwvU4FHxwaDkJz6ZCbJZGEz1pRyjJtn8eACtYnglnuTcl9YOLvlTn8rhTELqwqCa6h1jT73Ljh0u2PxgpbfJUMmbZCz48AZfi7GX7D4MM2GHItgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس امنیت اقتصادی فراجا از کشف ۹۹۷ دستگاه ماهواره استارلینگ در ۴ ماه نخست امسال خبر داد و گفت: در این رابطه ۱۶۳ نفر دستگیر و ۱۵ دستگاه خودروی حامل تجهیزات استارلینک توقیف شده است. /ایرنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2566" target="_blank">📅 19:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2565">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eLA3qAw5ObypnH4gbOArDRgBbdg4AIOYOkjJxSkB5UQ37Ee_r2FHaiK98nMUdds2FU7daqjjASBEbTGISg2m-OQBmD5ByQrex014wqUiuQdx6miUljml4vl3-5AvVc3ZPHeMctPM_2_7KmEoz1Qm-cf6cXZJnHUTHw2ZhdsQ_OAmTbcaCqh5seCY_RA9dHP7n-qZyTz5zbNl3qHjscmVspu3hEqYdK6qVLodJZaFUokpPYxELn6MvmCM4k2Q7eBroeM_WmzyKAcCA0YSMJg9lXejxoPOI4YMI26IjG1z0xFaRlktbm-BKUgvtMXGOCE70IWfnEdvu5IHlAstS-IdwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/ircfspace/2565" target="_blank">📅 19:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2564">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gnKaW2W_w-nbDjwCRfjVgq1kfoTPKWuCJP37sL5dsZ48tO9mckoXl_tUp278bBvcqPGTRlwklDgcdzZb1cXRdHCimpAyLSrkoA0l_4riOX0PkphVB67fIMfeeDEB8pRprHW-v7XJQqGKEKYCRup3XnxCtDUCKrXeLg6EmM0DKB1C8WiGlrwPCqvO5ZcrQOUcAqpJBn1WpMIRxEYNbigogJfNP2vqD0Yp9W_z9SgJArAEMmG6DfnyZg9DUYsd980ddPcafiiFzXF4izMrPzS2szFQe_TV4433wZqyeAo1s_YHBPy1xUU5KHMbCllAWgnZbDf3SFdx_85mNqD1_PAwQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/ircfspace/2564" target="_blank">📅 08:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2563">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_dZB37_PSwiidpEgGxFnPqr8MgQv_el7_rhUcS6SmHG_ZYtS8QK3X6evcLSPowmbLIH7pAy-jTpOh0woW0KNB2wc_RdhoSxbtlJYO68r-5cdR7l_Eh7K73FZ_L81cfkiTvmn2DqyruXPBdxwiBPechkrHRmqFbZIenJyB90_NTUBUuoFwMWAI9B2ykGpm6anPquPyWzjN8OjBZPiYjRU7CAPzrv5PWaL3n_uB9Lriz8xdAWbSjoIScSXEEsexWjng-I5ADHIYe3K5RRU78gDPQQQMishloyqsSKKQ0V6XBYtb66WihfSEIxbZVNCgRF0nzzQ-XpaKu5n302Z1sM_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2563" target="_blank">📅 07:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2562">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CM9lZ1aaSN8a1asSTWECLATxnL4jr1LvZHID-qje-Li9AxPmEjQlG1_XV0yLWPEhc2cwp95DqEe6K-9qelR1Eaimha07PrgFBjOb9C4LQIZ0lOHjhT5B9b8af0gkeOuKhe1ayV8j1hf5XNs-5mAHzM9fYnWDOsJzl57pU0LVVUZ4gDD0CrNj3oOWvs8Y9jN8iWFgg_ABvl_lhZBohULdlqbASLzYlvZYXv0-AiREGPHx_xogJmcZ9KPCXPhP4MU79DSZ9O1Uudb_Lv730LKQukxjGFhLgKW2wp0ZM9aN4cw-iOnYFpf-HfAD3_rL7RC4kdkqzZK_ONHNHwj9USnhYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/ircfspace/2562" target="_blank">📅 07:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2561">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bpkLMbttXdznOHcgRxKjN9047xjZaxGn3oG2zz4LhATdUdi51zjdVa95WGOr0IyWQimIzN-7H0qfNWlgETfRNX74NqPPNN64FcSu3DKW6hTRY0r4PVpEhF3gBOXux4xprfvNukCUkw22TZGPnRyEPH9JqlPPvtdp3nOsylav3ayjAyePWbjHrK9zcYpCOcMjMKzHwuE53-TnsjlXSrPqXGLg1liaz_oXvwdcpDAyp068hkq8GyqHG07fZl2iBQLJjWuD1-13YysjBnFGsMb_BVVH1hvAqUBrHInWVQyS8D7Zlr0u313cUwOUJXR4q0-wMHPwG_OeE096--UO4iWAPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پژوهشگران مؤسسه فناوری کارلسروهه روشی توسعه داده‌اند که با تحلیل سیگنال‌های رادیویی وایفای و استفاده از هوش مصنوعی، می‌تواند افراد حاضر در یک محیط را حتی بدون داشتن گوشی یا دستگاه متصل، شناسایی کند. این روش در آزمایش روی ۱۹۷ نفر به دقتی نزدیک به ۱۰۰ درصد رسید. این پژوهشگران هشدار داده‌اند که فناوری مذکور می‌تواند در آینده برای نظارت و ردیابی افراد، به‌ویژه در حکومت‌های اقتدارگرا، مورد سوءاستفاده قرار گیرد.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/ircfspace/2561" target="_blank">📅 16:58 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2560">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/ircfspace/2560" target="_blank">📅 16:47 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2559">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 40K · <a href="https://t.me/ircfspace/2559" target="_blank">📅 16:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2558">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pGfJovwwwGwu0DNQK-vgYN6C7YdbireJPzmcPNqmZ80J4oestreiS-uMjddDSlaWvioblXTlCuKATOQBvGpbkd7qWDLwBM5GzUJ9-BYYlSilQ_Aa6bf40paBdlhfTTfpRN0OY2ljF_Nar4rRCbpTT0UcHHj6mC_nekIzMVulPrGsi3YycWbeveRxVhy9SYhhbTUWL9UzoP-KMqYpL9fjlZX19QjiIL5U1RUJyzY2Gz9keLsyrAg8XabATPlTY7PQGWz-wZInUNRci68nHKlsBiqazT8UNOybZsLmckraU68jnApyYPBMkUt4TUA4WOul49FNj1FXpC7FU5LzGgp_iw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/ircfspace/2558" target="_blank">📅 17:00 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2557">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lXh21S-rAS-aR7NLdJh2JqdCUEDgihr542KJeWBJUZZWNLCyHpFUtpyjT3FbM4lGn-I6UyQQeKO8d0zl7H8QxFedkGO_4qCzc6hxV4c40GTui1Y6jRpsZ0kMuLxy5Zcb1AZJwKWNMfgsB5OazF_UDWKoaLnSl7M20XkccI_X1riu6MqXGWgi6wLj-1ayIjSY4f8uCrg-kpNJjb984O_TFn038dxPUi-LYDt4TLbRp2Ayn-t5t2G55K7RCHSdneuElIK9Vt84V6TXjHuuHlXm6KqW8WvQ2oN85o9Zo95ZyLiF_nKpgzKkbK79n8OYveuJDtfP6-4lf5y_YuSuE346kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2557" target="_blank">📅 16:57 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2556">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/ircfspace/2556" target="_blank">📅 16:41 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2555">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/ircfspace/2555" target="_blank">📅 08:47 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2554">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2554" target="_blank">📅 16:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2553">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7887a97904.mp4?token=KIzDcDHKouWmAFA1-jVgc8yUpVtk6rXGaGQmIDnUGQIuIxl4LR5-CBZa4_3RUdtMTmrOX_P8ZmQy2_ge0mm4778JIuHkVDl94eGjRRSa4iSTMD2wJpL574AIPqBidxl1T-UaeRr2_RgLWkuHf2AofGeFyYUyMLigp-uxVql8JMdN3aYX8VEL1kU34tQA6dStsUinx-Okm4WbhTHM0TVGJl1-hAZd282XMvYNal4jJCWa3heKrTv2XBwIb-vj4tStW-ROl07tTUHY8x1jIoEXbD8Oj3MagIpurKxL6ONJpqad9_3F_NSFK6f84XqiDdidpxdG6WGbBl4k3PYPl4D6ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7887a97904.mp4?token=KIzDcDHKouWmAFA1-jVgc8yUpVtk6rXGaGQmIDnUGQIuIxl4LR5-CBZa4_3RUdtMTmrOX_P8ZmQy2_ge0mm4778JIuHkVDl94eGjRRSa4iSTMD2wJpL574AIPqBidxl1T-UaeRr2_RgLWkuHf2AofGeFyYUyMLigp-uxVql8JMdN3aYX8VEL1kU34tQA6dStsUinx-Okm4WbhTHM0TVGJl1-hAZd282XMvYNal4jJCWa3heKrTv2XBwIb-vj4tStW-ROl07tTUHY8x1jIoEXbD8Oj3MagIpurKxL6ONJpqad9_3F_NSFK6f84XqiDdidpxdG6WGbBl4k3PYPl4D6ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/ircfspace/2553" target="_blank">📅 10:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2551">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Neljmhfn6kkgu23V-NL-Az1aNuwC86k8TmU3H4GbqKplnSAe_CrJ3wYDQwzhWztvcKMbDNye9eyDIoRiNjFeRVAYqjFDelB5T4MnJSZ1OaxTFIo1ZieX8bD3yEWeqAN3C_qjL_LL1_zw5jiUX54h_yF4bk7amK5g5qAC-85ZIC7IdVgHq2Iu2XTGw9gGb1xIOGkCFpR4HF0OX0tYC5BSm5J6EE--J2EEESAsBzNa_O8xUpcb2NGMh6JjGdU0hpeL7HWN5xl6O2ga1LxgSPGkj87g9An9iwz1MB69XiXb-96LuGTZZBIHjOPiyp4xwmRG2mgsZSQK-VLehFI_GFkp0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2551" target="_blank">📅 10:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2550">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V5Rn9zTYXOiios-fjPsU03TPzu_cNjxumsGLCMHLD28pgkKUdQs5SkkETNzIgjZLxiRcYt0O2ZBaP6PHlRohfMKuplop9Z16-8OFByj18zvVjj73mY0uMzGjOF3kgvG59wlhGDjW9oZyFFyF0_pw5Dq0oMGUgl034FSggrKFUWAbSskQfyedNHLIAxey4_VPkM2zS9I_OXuIe4LNmmsYxqlVupSHTaiWMFYoPWEzed_9FNpabaybxbnQisx3yvqncQqAYyCkMSphGhnlHjAaCJwTaGlcuC7Ax3EYTD-2lAL_WQm9Q63YRSRHuy8uyOvOUG6DQUglzx5y_l-N9a1Ssw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2550" target="_blank">📅 09:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2549">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mMStpq17sN9-PXry8ymxnBD17Crd421ZNVShSVbsR9U4cSdp0PHNAv5FXBWRLa0uzwRRMDIQLHncItAscLVyxbNl5Jwope59znwJ9QypMOufmgeFfhETZKz7qetjS-OwGn129_pkCKU0qv9yzdNQTUOuhwFKILCGpmwwuHe_SO_QDoivQkXtm6PAJPDTYSPjqJPMbN_A9fdaa3QmmAJDwhE7L0ds2PAMzf2mHYk76o5mg_33GZ20Qg0cO6Ktup7WT6n_YlivoXYgwYRIPZUBvHmlA8eL2PawnmFSaiqk4uz4CJFNxRTfFcKmXCF93AmpxJ_N1FBlAHtznbnZPJEtUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فیلتر شدن فوتبال ۳۶۰ و دستور رئیس‌جمهور برای پیگیری مشکل چقدر گذشته؟
هنوز نه رفع فیلتر شده، نه کسی فیلترشدنش رو گردن گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/ircfspace/2549" target="_blank">📅 09:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2548">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CQSwDogpvUlYoYvxeisJtVhu8vOdmKJ1-wGO5GuHsOCEMeGnMnzmf8ZpZh-oGKkHBIT7ec4yrQ0XsWjsZYJw5xvBLdEFOsyRGx0HJm07GctenyzdJAD3vrsJXAi9HmPK6QMwUp520fukxrzoKaRbkNE_DBQvi-Vlvz_vOxJ19YVElF0sjrDwLkwmMOGAc_klocKqoC7ZaCLNWRjFKn10ZBfSzz6mvQKuc5UqPWFI48LGE1_ddG1PdJYkH_-1gVe_MdNuj4WjMI8WTxxFwwsEKD4hAHBMW2XISFhbaYnkTQEECzl6jLYaV164Piyw3BaIzceyfgmyLtHL8d5vou1-xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلتفرم لندین که برای ساخت لندینگ‌پیج بود، بدون اخطار قبلی فیلتر شد. بعد از یک‌روز که با تعهد در دادستانی رفع فیلترش کردن، اعلام شده دلیلش فروش آمپول لاغری در صفحه یک کلینیک زیبایی بوده!
یعنی هنوز که هنوزه نفهمیدن فیلتر کردن یه کسب و کار چه آسیب‌هایی داره. هنوز که هنوزه نفهمیدن وقتی یک صفحه محتوای خلاف قوانین داره، کل کسب و کار نباید فیلتر بشه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/ircfspace/2548" target="_blank">📅 09:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2547">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vlj94TcIiwuN1BYQp8fqFM_H8FdbkZvr-fdsHyzXPK8Kb-5kMlQJdGLiMhUecj2FV88qaSGwojCTrKeiMgD7bOChQNReL2o12zGM2zVSymkFazQ93hge3vVeXhWwkCzYHoOEBxg-MsozlaCSFpL-_Sh13-2Q8kSMycsKjvGSraGhvtpYxuSB--wTu6tUnUvG0YIaopTVYb8GGTVh7ag9iZ-m2pWESQAo7TMCGMtNJMShV_YiLKUoLzmVsuan6_EnGh6ryDCCSZg3vteukcFbsZ8bnBGiMfQk09J7wovBhyH4rTSL6nBGu-WIonhwonWKg-byBI0QTF4de74xz8SaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با قطع سراسری اینترنت و نابودی هزاران شغل، هزار میلیارد تومان به پیامرسان‌های رانتی کمک کرده بودن! همون پیامرسان‌ها در عین دریافت پول بیت‌المال، اختلال داشتن، ثبت‌نام جدید نمی‌گرفتن، محدودیت‌های تازه گذاشته بودن و چشم‌وچار مارو با تبلیغات کور میکردن!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/ircfspace/2547" target="_blank">📅 09:36 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2546">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a_lwrHPVdFn6KFMYM8ybhWJfXwP3uO_FTESlSw9EgnV-DFyOdtU_Y4KM-SBKpfo2432OqdV6XppqGSWuy8ZKf6aNOCCU2_j8Jsf1ccJanc_bVuz26iuW0SnEnGUfZKQy23ovksIqnh1X8WVvfaNQ2N6WwCfbALosucaCBdZq8PIJ_EbTpXzQcKWz1x2Q86ZWPKrPwHSsbHzAnP9KWo1fOsyTqs9gNT-e_xIyOi41VR4xyPgF5BDCsqJ-DPrHorLBlD9qH1ilVz-Xp2g2516vgxrdofaOEXAoaQPr5kXDS_4AxL_GK6XnDa0DViniWUEQB0zWELF167LEml-3MbbRlQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/ircfspace/2546" target="_blank">📅 19:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2545">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UE39nMAvvzJjEXhYILrPCmpop2dKozHCbFobP_-3oC8mdieYBn88wxdaoW10JtrYaxty0Kg16AaMCzbyNwfhjyKnkGYdvvnJCKKg4aIsMhV1_uf5gRz5XdMnNP7ieyKYm02dli2hZoN_VUgFSmz9t3rFIfXhM17jI4w2qFM0z7wHCwuL1amoujDGAxEQyrM8O0yyKcC_RaeIiDwd5MJAicQbfSrKeypROQnm2Jh53VWEPw9tco7fms2JH6NqSFVJxiQnJPMJr-KJ0QWckTFRqHdtTH4aK7OWRTelD_a9YdiszBokEQsUN5YOMK5wpn8_jfc60oaZxLw6P6WJRjWPZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگین چرا با وجود اینکه چند روزه اختلال‌ها و کندی اینترنت شدیدتر از همیشه هست، چیزی نگفتی. خب الان گفتم؛ کدوم احمقی قراره حلش کنه؟ همونو بهم نشون بده!
ده‌ها پیام داشتم که نگران بودن چرا چند روزه نیستم. غرق در گرفتاریام و گاهی حتی آب از سرم رد میشه، ولی دوباره برمیگردم سطح. نگران نباشین.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/ircfspace/2545" target="_blank">📅 10:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2544">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AGLRnkZIjL8VoybXK8_6-A2pQK6eJW0i_XEdHyfmcXbIAjxLKT9j7v10R0ysOd0YFvXa69brK1Jy69qDQxUmqergmBwR6oIHHGgvZa9YIB86OuOMrV92u4cHM1uxarGfNhzy1h3VRu1-nvmWe4ijMnE6CViIPROk_uWkNXg56vEB7-FTdGhUvLNEfX6EdsrfS5SLkWJfPyx1eJdBsa3kwTGSFANL9G2hlUzsYkNmsH-IHs8Tb5rui0X7xci1XHneg9w54lvkdXWL9VhptgX3WUvr7XTzXJe9I8UVpldeO0mCRIMSaJ9XLk3n5PeFi-egRQwxZ3GKqTf6MygEZUuugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر لو رفته از وزیر قطع‌ارتباطات هنگام رونمایی از طرح تشویقی "نسبت حجم ترافیک بین‌الملل به حجم ترافیک داخلی"
😄
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/ircfspace/2544" target="_blank">📅 11:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2543">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">این قضیه اینترنت نیم‌بها و ترافیک تشویقی برای استفاده از سایت‌ها و سرویس‌های داخلی واقعا داستان جالبیه. فقط ایرادش اونجاست که کاری می‌کنن تا سایت‌های داخلی روی ملانت باز نشن، یا به حدی کند باشن که بازم فیلترشکنت رو روشن کنی!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/ircfspace/2543" target="_blank">📅 10:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2542">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/ircfspace/2542" target="_blank">📅 10:28 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2541">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SDrmTTCNvSTW-aq_MRP7s33ouy-rx4yvSHt-njLu8_XWyub_gKsfKbrjvm3NNtoS1hrnEqk0u6n7IflItdcfjRvQRjJ0jEgEzFSR_lSp8UBMj2IL7zmU-H09Cij94j6KKh0b30_Cbx0cio36T6uEw-AaWfZrY8Dvz9ze_Ezi2i6bJ4gAt8No4bDuBPpdQ-4Hwes8-N4nn8W8AsZ7SHPrEeKIpNHo2-00lZR61SloOqzMkOd4nz5AP2emCtz6990Ddgi0aEg3dCFZtarK1w6n8vo70CwXMt4P7wqnL8SQmgZEINLUVmyEZqvmYt2RmZ-NFhmV9ysqjkR4JZ5QC4Wd2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورم نمیشد که بعد از ۸۸ روز قطع سراسری اینترنت به جای اینکه بیرون بندازنشون، به نمایندگان حکومت تریبون دادن که در اجلاس جهانی اینترنت سخنرانی کنن؛ بعد دیدم این اجلاس در چین برگزار شده!
روابط عمومی وزارت قطع‌ارتباطات گفته نمایندگان جمهوری اسلامی در پنل‌های تخصصی اجلاس جهانی اینترنت که دیروز برگزار شد، مجموعه‌ای از پیشنهادهای راهبردی برای توسعه همکاری‌های جهانی در حوزه‌های اقتصاد دیجیتال، هوش مصنوعی، امنیت سایبری، خدمات ابری و تاب‌آوری زیرساخت‌های ارتباطی ارائه کردن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/ircfspace/2541" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2540">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/ircfspace/2540" target="_blank">📅 17:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2539">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pLowD0CxZb7kDTmCDFRX4Awtn-4ZtfcsEQSR1yB350HHQ1TjNv5AHbqDa_2aLdH5xPRzyCTaG2S7_-NOPDChlhBkG0UjjrHkDiI0SYv44mJ1mcbtL-nNUoSdV-KwjrrSU7bgbe8nqRXOfCbw8vR_nft8srf6VlSHFgyPwlmMyFEFE4hg90k6SD7v8cygt5IW5ySoBRAzbm9D53BbFk22fmeECS23tbm0GBV7zSKEeZGPeqPjIvdvznxeG8JOOVkVam6rMUMoNBRbchLlIKpowlRpVAEJbxo9BC-WH7r1dAE0ybkPmTVX-Hmrx0jH3QJVBxXkIqKZqaG6Vgc2IdkPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین داده‌های مرکز آمار ایران نشون میده در بهار امسال ۶۳۰ هزار شغل صنعتی از بین رفته و سهم صنعت از اشتغال به ۳۱ درصد کاهش پیدا کرده.
حالا این آمار رسمی مربوط به مشاغل صنعتیه، ولی فکر می‌کنین آمار خسارتی که بعد از قطع ۸۸ روزه اینترنت به درآمد و مشاغل اینترنتی وارد شد چقدر بوده؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/ircfspace/2539" target="_blank">📅 17:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2538">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MHg1OGU2pJ6BOweLQ39uuiwNp91NjtPERcek-mtve2tmHxfAF2grNrkEIAZF7coCmGFdu11gcH_F5LiXFVFHarIeg4-nwvs7FNZKQfzpe2JYV2NMehDTwnmP8bIrgxXxA9FJVtnMPmE9FPm5yeunEfsPc-8Uh2WqnfJlgR9ZWlDpcmz6T2IDNBF-DfvtvhTKnFYloTHXDL5qq_qZadhd5dPnS6_HyfQj2O2fZjQPgD6ms1RbhHL8HbO9o5XI-5tctAfyibgTU4d11vehMmUaH0DpoT9TcD2dx4d0fuSaNkgMTph7RKqT5QU6gh7GjTCWB7wYujXULU6BVdaSmUNn1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/ircfspace/2538" target="_blank">📅 17:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V-XivsmvBKYOyVpwueB4YDDs7f5c0KrsKq9D2aAxzeRU5vlITqiGcsg6_4VbbMBGPfbbtfaPj-blcS1JYTTDrGLK0d7qmbejgiTGN5pUYR9w75mLKp1hOdtnOqhG9AzqNqrrKB_L33MUf6veCpkH6ATRFf2-P0ajHKUWh_qjceomNaE1OZAYeDOYfWJo7JJ2RKXUbNXrqCdfwQPqzhWLHJS5a4POWnBzCt6HpYA9NTnArn-YDrlO6ctfYbzwyIAMmyhQNHes4lOfmDisQrejyAhGu1SJK0hkArLu3VMmhV6WFMmXfdeq3bamgh225ZtolZ-Q5woN6fvraouu9crk-A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/ircfspace/2537" target="_blank">📅 20:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cusaanOTPWn3ZgItXEQ-PsQ8bjFyAtzrTVfK2z-f6kBBdnAZ5VT8J9dKMl588U89ZWiGOY2Tqz5rxhAHHRZfujnjzNIVh7AbyZZUOVBMmg8gEVsdHzEq_3ZrkWgIvgrNil4RpbcDHxzeu90V8A0ZSXEnklPpFxS40SXNLe28EOztiY6JQc7hTFNbjfBpiOvYKptz5niMbWU-YhzXqz0n6PKPl94mIZEFiUSfBfQQ0OxiY9dvjBO9mL1TGzzL4nMltXhBfIEE5K4jCwlDlmGM7VVJ1EoNtbm7bGse7pQeqImVpSycngfWhf63nu9-ZcEh7ukfp4XrMSIpsEpYJYQuUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری برنامه مثل GlassWire، NetWorx، TrafficMonitor، DU Meter، DataMan و ... برای اندروید، آیفون، ویندوز، لینوکس و مک هست که باهاشون می‌تونین مصرف اینترنت خودتون رو بصورت روزانه، هفتگی و ماهانه مانیتور کنین.
چرا میگم؟ چون صرفاً مصرف اینترنت شما اون چیزی نیست که خودتون دانلود می‌کنین و ممکنه خیلی از برنامه‌ها در پس‌زمینه مشغول رد و بدل کردن دیتا باشن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2536" target="_blank">📅 20:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ID7g2K9s5Y972EeWz5pLhZab-pPEf7Qq-aHEK3YqHqbuzeKNoHtrdBKLhF2RV2iGUMz82yH2SIEqcWRbCFoiz6hlyPkT57YcQ22P6VuPTNiD3xUR6kDGEnc6J0-WWxpDtA14uZeXiTOFbZOrDF24FnJT76wUoOw91KOtASNXzSh_LokHVa6yETL5nEBlNnrcZ3NkifOtSrvE4vGv0WAXxp7GUFDhJKCtao_fhpT-JMb4rW2-zGA9u50FjOX2N1MojUiGN6ZuOgTyLmRSPegbrQq7bfrsNBlHkHwrFa0JQrm0PO_2Im4GGqU-7yEtDjAOZufjJ059mNhU7HbMDx7EhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/ircfspace/2535" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/klZ4pD_Jl0MhhJ4U4WuSoe9lHuCHe-Pe97DE49uXT2TnixELJCJfIcNMZ5RnTNHEph5V6Aa-RLhJ86h05McRAxvMNnBOi-emOkb0I_boF_EYICM5sMPQykdstpqjRg58RlysHRcAbcB9VO840qYwQ1Yz7_IdXHRoDTDjraqWoIUvUEaTJgSFVJdrdgZHJNbCHUKTGafpJrLTkGl6F3DGbR_PkVVvLkjH33KJ5dssh_XGtlqNlJQA4iQPtA5QiBBMSTZRIbd3HcSLyTyZnHQZdzImuJ7xkdQSJW9EWHr5kyT2LE32WSkH48qqi9RVmhI1l7ueodEsKWgrWKU-P-ywcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظر میرسه این تصویر وضعیت رو برای بسته ۹۶۰۰ گیگابایت شفاف‌تر میکنه. در توضیحش نوشتن برای این بسته ضریب ۲ واسه اینترنت بین‌الملل لحاظ شده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/ircfspace/2534" target="_blank">📅 20:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/htVJdPRcPW26yBI5j_o-UMLi_yj8gY1wt9uqk7ambz98wd_qAqE7nvCiQpnoe_JqnrXoR00uIcf7x1XfVupEUxJxZpC3btcNY4U_rhaHhcgL138tDk9h0yv92ik3-V0bsaLV3M9OWQu_rV43vpJgQbQmpH757tgvRM3GNmwRXCVA0hxKjlztXxZtMXu3dO6wjT_DMjZKP9qZksSyV0I9dYe-5_4aZxTrdzkCduOLVFA1miQ5vh_9yPDmj8jDDv6KLj6GkjcC4WTt3tr3vzDTY9A0mX4cHAX2pKJ1EI07GqfCKYBwgST0oxjao6FdvgFUjfO2-83hybxIgwOHrLfLQg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/ircfspace/2533" target="_blank">📅 19:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2532">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/ircfspace/2532" target="_blank">📅 19:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2531">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/ircfspace/2531" target="_blank">📅 19:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2530">
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/ircfspace/2530" target="_blank">📅 19:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2529">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c8bG3F1ddK1fPy-sV-IDJqwWpyOECqv5_UlTqWaQTmR6W0URbRVj6-W_eyLO2ygjOQ45TVvLSCO_zvfO1DtyKTYT46nySeJtVQ1QQwwv2H_9xFwXKr2VbTkuy8sIfQrjzBW8wRpej4uN6Y6JduYCbwQ2Ih2i9b7gsJudVKfKa_SGrUqNjEGFzL7eA8pPsiprKm53mbcqFhI5A6cDg_gowPVQKqNKoCL5rG5qWE-FZPha0SbWzkO4ewbtPgGoLKIAtVKWOPDj26TwxU-kBpuYTabv487y4ljQXIdSyviBmSDyJu8HGQYaZU7fstJBUyA9iZwAU6tyLFuVoZ5PuGbjTw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/ircfspace/2529" target="_blank">📅 19:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2528">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Tk0yC7R6PZSSoQPk2xDozdx68u_V2n45rvMDnmei17PFYy_O23JX9lFf6hyteXPCYzzxknN1XKmEzuf_E-PutZ5TMYIpJURsZTfkZvSYAebKDkF_cvTMTZUWwjnUhX4n0mdoT3Fo4Ff4ysFaU_aHrqk0MSdXUPinC4eIFft9lLw4FXmfRQ--O0HBxnk3U9d_3Wpodn6s1Ja-LQwHxORrzwK0ilRlJsL_zF-xZafFI9Ke5_DSdWos62AgUna3ifyAcUgiOq0cY7vwAV0QvfsiqtvYjGzbK2MmN_VBbYQ_GRKARcsgE4TroRI1Eb0VzPyzURCBQW4OD2Z7RYqCKTH1Ow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/ircfspace/2528" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2527">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/t3gwxelwbzMxseYJdt41er1uU8R11eMAN_GlrLPm4HzZIXq-e-QiMLAXurbq-KtmEsyQbjuege3ViYJvkUKUQVNkF8sa4jSdKr5z2K8tq9MmqdQNg8JERg5TikMycKo1d5L17yKaY-HABM6vLOqasmKKoYuI6i6axKAN8xIr6bI3yPGWEyohDi43JEho_s7_cWkTLFVQ87ngY7CUygtoJFOIdAYDaxAVfjc-c8R7W-DQmnBgVpzTtVBXWDZlXiahsKljIWiKlUFcn1J6biGSBTlzbIv4-sQJ2RcfSpkkTSik1BxyFlB9VoWb-3Ds5A32QcMqyQeYwtgna6feZ3RHXg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/ircfspace/2527" target="_blank">📅 18:11 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2526">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/ircfspace/2526" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2525">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r5-F_fFdsPj4Py-wFAMl81_y8-DZLKwskdOrDVOuCtCZhoh7GeAvaOfCYWefzSy8T_rBYzve-Y2QDlM2_iUnzzHNi4iYCF6ntvwmUT_6mxgaFW85bmsBNLF7hg43iRzL7Ut-nG4HgVz3lHBSyyT4cf1htGLpQdE3PEU6h-JNZOvy-o5xc218dF2HblbvocchfDj-MDHy-fM5CU85HDBmLiPe8HsYqhjVg8YZxIZdAeV13bKk5SWSun3b-coasBSzpqClgniiKU0kM31pelc60lpCQnzZhf-09CIyEEnAMY1AqvUWKSrukaszJ5ZasSmul0PLzxevVba-Z5VoKq5szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردش مالی ماهانه بازار فیلترشکن‌ها ۱۵ هزار میلیارد تومان است؛ بیانگر حجم عظیمی از سرمایه که به جای ورود به چرخه تولید، نوآوری و اشتغال، صرف حذف یک محدودیت می‌شود.
با چنین ظرفیتی می‌توان ماهانه برای حدود ۳۵۰ هزار نفر، حقوقی معادل ۴۰ میلیون تومان پرداخت کرد؛ اما این سرمایه، به جای آنکه به موتور رشد اقتصادی تبدیل شود، در بازاری گردش می‌کند که هیچ ارزش افزوده پایداری برای اقتصاد ملی تولید نمی‌کند. /هموطن
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/ircfspace/2525" target="_blank">📅 18:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2524">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMKm5-CXNZ-YkP2Fxou8OTS4t-447KWDlemqN0uEMmJQ6c2CslA_PdVGsRhMwXV2Huke__i_cyWXx6vah0cvjxjBMZct4UlX8WdVBHjciIDCnNiGd-IIVsJE5DMaRjNiv_viRPNvuDioZniGJMD5ZHpidq0Rt8mJ3Iit690TKjhtQvELiEyYZHW-0cYIAv1rbew-R247MKkSzD1f0lqmOl7awbOCRkvJXRVwYd7-77kPqKzAAQskQwmPTZn1JiAQfSkdbsSVdPl-QKDpl3g8LHvUgCHrRyY4b5T1P9j5EK3SoTJts6VnxwVDGPe6Zhsxuyu39hcQvKpwZogzTZ9ymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز کسی مسدود شدن سایت فوتبال ۳۶۰ رو گردن نگرفته، اما سخنگوی دولت گفته "هرگونه انسداد، تعلیق، تحدید، ممنوعیت فعالیت سکوها و کسب‌وکارهای دیجیتالی پس از اخذ نظر ستاد راهبری و ساماندهی فضای مجازی و دستور رئیس جمهور شدنی است" و "این موضوع یکی از دستاوردهای رئیس‌جمهور است"!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2524" target="_blank">📅 18:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2523">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lts4do3ezq3cnmMTnpFA3jHB9bA3GBtFbYcYQeoueHHieUp9Wu7ahrYrnb3alAXv8aBhMb5VPDymIn4cGTFpQoRDs_DqNa9DCOUXIIbUfiDay1xgb8r3nOSiGv8y_NPng9T3YksoXVWg-D4mctwKJjwT2ZDtMDe7ZAwLjjQCEhzhbhISyE0wZx3EYZloGLF4yMVkHM7koJaUwLxSKqQxfgw4yn9MW9rY2dk3pt4reysJQCDtqfm9AzCC6Dx3147smdnxueB9Qs9KFjSb14MYP-nRNITX8MP8rzn7Nq77-kqIaBhudKgrcsVdczIhmCC0J63Qsr2lI8oxQ3j8yA8ZhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/ircfspace/2523" target="_blank">📅 18:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2522">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Sk1rCK2P79AGF8zTx5hANe2l6_11A8tKjaCelsOi4Q6yhDdVJrbBEVpyJAwVIhIuthx91BN3IYMN4KgGlDTBwHzSQD6-iFeEviAYjJz4I4Zx48JSKi2OSRTNAboLjKVOMkwbfiwJ2Zhzkh9ZnBSuj6yTH58vLNCZ4gkjIwzpI1tXWTFRDiQdQtDOG-eDDhESw2-SkjaTHCHq3Becw-3joyYB9Rfxzb3U3Qxcv206uOSBWPrLd93Mp9lvEEPKIl0-9dGnoPt70ZJDXMDdygIPl_-QGIXAx7p9MgfOKRwf1h7ccYYeG9IbOs3KkKQ7k4y0MwcnR8eUYwxKWag7UVMPPw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/ircfspace/2522" target="_blank">📅 18:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2521">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZH25LzAdHEnXkELA92cJLFWXqHUpJvZJ-WZmuQDYImJb_ppjg7RUXH8lPWake8RNikks6VKjNpTqmXa7DEtr4BCtcJE0zAgKrTkVJiv0wUEG6lb5a7ZSl0OvJrb2_t84lflkwq1zNkftdR-PRHDTBIz9EvdIQth2EdDzlne3kgmUN-ATSjEwyvCvopDhBPU1wz08Hclr-fF9F6KsMlZQCqxV3ZpnP9scNfRTebGuIRx2GPoSbDtIzLnDfCDebcgQF0pexesdsT7m_zwdn9Ud2cle-xG9HYiqys-5ci-N1TYJkNbxKgKRQwKZ2g8oPzvNUGSUW1tJElEd5Z0L4yh1_g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/ircfspace/2521" target="_blank">📅 18:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2520">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/ircfspace/2520" target="_blank">📅 07:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2519">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6GZqTmx9-MaAJm1ZdWL1jWJ7NPUAycr-VkuMGt3ch3nILpQLSed80pVBrVwFDffZQZpxDPVDTbLxM8suey7D8emow1MA4_COd5cSZZos5A7i2j80IbtjRXsllrFmiH-sVHibQyIqDH6sQHn9zBbVs--B26Rs6Bof5Xgy_BdJad0Pt6AsirJDz3yBsu4ixZnT55KSO5Qzhx6HIvtran8GOfm6685ASRV3WZxsqs6B0btpER_gu9jqlUpNCJbtdQCA-UFRys9qCFkd1B1MMA7ZOgiGRAegcVwl7VoOcYJDp9HG00jEaEexZdw5K4KCPcEzzVmUxFStPA3d0Ql_bzUCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/ircfspace/2519" target="_blank">📅 07:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2518">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AVR79tsHwQ1p2tqkF5dqkLpgFOo3hxC7ZHws_ouIF5TUMAVPniWMbw6kVwDSPZEyFQMWZ_i44ZzHmwhjUIm38FK2FHdDNLuv21KUii_c4vVB2SB_FKeSlxSUe2Z_GgHpilywOilj-CcBSjNge3gmPl2LvsLLmWfoyrPZZoANdpajH8APRNZkfftkxcAyZ7mvuADqd5n4TO0-xNao9FsMcW9Ahbsnh9HBd18mdNsO2YePd2F9Dkvvwya6mh1NJv_zgKSm1CY4gHZxa8rdhaY4NKNXoCKm1lNRL_Ltyr84U47zgMdgH4iTA1RejNsrJW48KNhu7Cgx548TcHHZr_QIaA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/ircfspace/2518" target="_blank">📅 18:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2517">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cDkt_ZmAIXg25rDQD6K1bb_hDqYb9zc0cd_vgJ1Kki6vjaa0REOaZCUltsQGBLTuCIJZZPrOXFM_jlGDhlkxDW7oUlUMZMF_v39LtE59-fLwrhe66U9T1U4BCmMrCw0Opjxwq6I0wjrB3JjrXIGxfJkjBUwuWpG8Bih4NilMX5nje-EB2mAzFdIba7JTftw2xPuUwemPK3ZuaOR9NPDGOJz400S9mpdyRBOpPqgUlNsA9FuJPNdZxIATCQkBHSLrOagbjvIpnKkTr3wz0L7EaMZjhBqTWmcjPEAGuOc8zgMFxOgC4X1aZS02JwwyfamkT4NKR_NfU2ZopSs4L_r5fA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/ircfspace/2517" target="_blank">📅 18:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2516">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TIlzEBM4bqOXiUhytaLkzqvUG5mgAmNiN6-lP7g_NCA3zXvnH_sU56qlc4HJcCieAAQtyWQCiv1T3FdlyAPP40oG0SPztRbb42_I7DJhXc7vlxzevBMc5-ZTKa-K_e053WCVN0hrqzD7RO-fSf3XOT6odZwqtLhGjj6ESmY7mDowS08h-uT0xKAu10KLntwdMvpeogv0Nki50NElgABcgSW_AcoIavendwT8ZLcYCEV7W5y_lEeWrin8hTjLBhH_kK0I_Qv-KsfetUj4tBtdT7B9gvKrFJb1p-TE80QC24QRDTqslfAJtPUtRXHkBUE8vvwQkKLgOale4anpnTIpKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/ircfspace/2516" target="_blank">📅 18:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2515">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i66UuUsKk6-AjC8WkIEbXFgGqWoup7hbNcimBu38kiuDGr2MxA-wtB9moebBGy8HHXREXt9zEj5SgIYzL35pCbv_9sjH-34TVnhhma-nuFR9CmzNC137s0L95kalwc8EvanvQadmJ9Y-5QTOOdKm6i8i8zZEFxu5hOwOCJ-MeEhhYlOu8Ybv1DJSBfGqp-xt7BYirId2vxAgD7ygKKWeb8bVPE-NoxINqNSEU5eV1c4KsY3mLbZNnHNzDaOG6YHVydTug0FjTOeOPXDd3uZlPi8C5IwO7HVk0Am4BAOJKU2Yie162rdoFPzdJ0NfLPyB_M3eFhe9FJ3zxofJycqQfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/ircfspace/2515" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2514">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XpqTrDt6eqAcWJLZWnhuvaJbhLPAY38NAqnqv2US1KST2dA4JjESPy5alNi8wdSyrd5vP6bu_RkZi6BLqKtsGWg_fBkZcikYxFsgfhIdbjeRxInuyTPplMDImQK0MdnLVuS2EqN2xm5aMUUSfs9XEeZwjZl_MgfAbalIaLxEOFKHRd_kTSVbwBQnsF9JZyvNJ-TkcxjGj34PxSRTnEuniFlRhI42zmoBzSoLY6T6xeCR4NjdkeVC1zI88em3fDo5ER2KRluWBC8x4v_RQ_bBPLQhPZ5H5p1glomemiCJwfHYmVftufTEfPTMsEa-A9NfuO6KjVcVCrSBgJfXryBtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قطع اینترنت در راهه؟
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/ircfspace/2514" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2513">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/is-qYVU2rbuyWeUMr5uWseDLVntAzlx9QirqKRpryGTDp9HO2IGR637qri5Rwa_mUwRGqEfrif5Rjk-MIEkX5UhIAz7CQ19CUCzmsZBmu6-92_lBw_IK4WZ-3PtpvEMMlsc0dZiLLXw8TfHhVxsIiE4LcP5tXaREpTEsM1pHBuZSHTKWA6Y3DOQ2oWBaX5jkeQrYFwa_h7lON9NmwjJ-x68YGmPGot10SVhw1ug98_QKJ9p62GEwBvRplPl0EN8ZrAyWzs7CctMqJL8heq4AfNSg1j53hDmpSXPcTUJ656eJ0cAm6Mz5V_r325Gzj1Xw86IMqLkNYpP4kEdVgFqPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغات تلگرام ابزاری شده تا بعضیا مرزهای بی‌شعوری رو جابجا کنن.
هیچکدوم از تبلیغاتی که توی کانال نمایش داده میشن توسط من ارسال نمیشن، به هیچ‌وجه مورد تایید نیستن و اگر سرتون کلاه رفت یا امنیت و حریم خصوصیتون به خطر افتاد، مسئولیتش پای خودتونه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/ircfspace/2513" target="_blank">📅 19:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2512">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ksgu_HmOiD7Za-Wuf3LdtWuKajMFfOuP7YaikJ8p9RUp27Vg19s2_7i_BcTUHFl8jFHI9PMG5tIP5aINH3NTj3ED_7vE-HT9MzSUSOt9dhNQiW2AMC-n08L7e4F0yP8OAs8KVu8h-n-OlOdSxVYMdnv9Q1eup58UDFCbz7z7yw7acH0UOQ1jvr-fSGVUyAmpq1GweXt2Tn_nx-FC1UI80U9HoKVd9VqZrukygj2Bt3qCZ7GJeS8MdY2l9ogKJh9tJpf1bmqSsVirsitND2AXsBCqUo2k9Y855k5LPFXYBgZfxVqPrzTxpLUmBwljwLUIcfc0Me6jPKkzv-a7PYzlIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انجمن تجارت الکترونیک ایران یه بیانیه داده و نسبت به تعلیق دامنه فوتبال ۳۶۰ در رجیستری ‎.ir اعتراض کرده.
اصل بیانیه قابل دفاعه، اما امیدوارم برای کسب‌وکارهای کوچکتر، استارتاپ‌های کمتر شناخته‌شده یا پروژه‌هایی که بدون پشتوانه رسانه‌ای قوی دچار مسدودی دامنه یا محدودیت میشن هم کوپن بسوزونن.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/ircfspace/2512" target="_blank">📅 19:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2511">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ساترا گفته نقشی در فیلتر شدن فوتبال ۳۶۰ نداشته و قوه قضاییه اعلام کرد مسدود شدن این سایت ارتباطی باهاشون نداره.
وزارت قطع‌ارتباطات هم طبق معمول نقشش فراتر از هویج و سیب‌زمینی نبوده!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2511" target="_blank">📅 18:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2510">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JwqBjpeYrD5VFpg4tjE39YG-qowhgoJX-O9vEdAppubz-U67JygCmg9fLGyTcqR9MujWyj53qeCGnb40jixH0iiZCwQ6y0JMX4CYE-al2GR-CnMrpcR8xsQjLhGg9OchhHIpKRvVGKCEfBVmwp6K8bjb2ElZKQojzwxEKzcMy7ymm7GOm4WE0hqAbbljSU6duC5jLjskGcp4omFOrPfoWwcvYFqJIYr-K8fqQjp-MmqpxrrGIOW0lJH7PU0DzjynsqqfACPyiUrAn1meYozc9Qe6KPA_hUn0y4G3HYMwyQ0cpZlzj2mYjzjl7jVY5hPhfboxwjgA4hyU3nnU1IHOjg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/ircfspace/2510" target="_blank">📅 18:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LmfUv0XGn5kpQRnQX7-NWUCmSx_rCjAabT-yN84kfbfiXRjj2XbHp7cqn3kDYhwUm6uG-4yWJwufXca7BHUyp8t1V1FRXGrRPxO_nlItqs66H-fnnjznYiAbVKtun9hPL8GBhaouoLOBx39DkPMYvSZ_B7Y79JxV0TYh5xphHGXjZTNxqAMqp5UuPydCnDkCUuCYr6YU-tLgyzJyBTFlq0R44SWDBugVT4JpIXwy-2iYwLeaOIznnU8JmmkeaFzfUA9344v3fahxk3ugqUAZ89ucyViVa_4sYmpih8OcsWf-Cu2wsNMiiiZbmXhUtB8lRiBwineMn3V9gZYQdycrTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فوتبال ۳۶۰ عادل فردوسی‌پور توسط قوه عاقله فیلتر و دیشب چند دقیقه قبل از شروع برنامه زنده از دسترس خارج شد.
هنوز علتش بطور رسمی اعلام نشده، اما این اتفاق پس از درخواست سرمربی پرافتخار(!) تیم فوتبال جمهوری اسلامی برای برخورد با این برنامه و یک روز پس از جوابیه به امیر قلعه‌نویی صورت گرفته!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/ircfspace/2509" target="_blank">📅 11:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FifLk4grpQzvQgrXwJTVKRrqs-g1FS1T8J4K-bmtOhv6Ncn594derShAwZ2HnJZqxh89bXwPPQPT8qndHlQ6tUBPUOGbE3Aea0KfEeO6Qz0_XAvjNOwK0NhOCmm80Wgf5fUb2WfkI2HNfH-ZGfX9Dgc3e-BWAJ72GZSj805my7ThgXLGHwpsg0OVcKsP09MdvGn3g5_wzbKrKmsim_P3c_VQ5_NEdRS-DBv-On4Zl05-eByO5LcmIyzDtyJVy_ahbffS_aEu_3Qi81-1bDnsa8Kv_3-Xd9hcKJcVqj9B-XqDuPqZByBumvx5jnT3Uu-QhPcCeU4eGoYVmrOG213c7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/ircfspace/2508" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rGHKdQKUdpHl1YPd8dwRta5IDc0XNfu9F3USe2ohx91T6KG82wiMCPnIKWJniRiSJadh3SgGdKxOWY_tGXbZ6wkquPDNSOSnnY3SvhJdzjipwXZyuEKW1UOPAA5gKjfwAZUU55b00ILSrm4F4ppyr-ImNY9qvzKMefJ2LB__wBFTDObVP2Uaoy9HDMJbioTGLXcuXyqp8gszaaT30sODcqMPw_saJDKx5V18AOiBpDXKbrPZgy3j116p1RlMg2RUa3w4amHe_XcZWxjI3v36O_gKAqWmfXLYzE04dZsPGDEmf3YsGu5sxGfySV4Eh-D5sG8Qz6_k9zTB-9rj55Q_rQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2507" target="_blank">📅 16:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2506">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/ircfspace/2506" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2505">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مدیرعامل شرکت آسیاتک با رد شایعات منتشرشده درباره کاهش ظرفیت دیتاسنترها و احتمال قطع اینترنت، اعلام کرد: تاکنون هیچ‌گونه اعلامی در این زمینه به آسیاتک ارائه نشده و خدمات ارتباطی و دیتاسنتری این شرکت مطابق روال معمول در حال ارائه است. /سیتنا
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/ircfspace/2505" target="_blank">📅 19:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2504">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گزارش‌های زیادی از کاربران در ۴۸ ساعت اخیر در رابطه با کاهش پهنای باند، اختلال یا کندی اینترنت تلفن همراه در مناطق مختلف کشور وجود داشته.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2504" target="_blank">📅 19:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2503">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RkRxFB__Gf8X5VL4ysheoTyIYCQXMIuIgu2roVw5v-IiyNa6YSqKanapODcjKF6SWqY5gWuNhAkIlkID90AD9eHLrgl4fRMrPh7tCxC1fRiQb0TPQ5EVUYqJOo_exOBy6KG0R9syPbWfCwVjZtN3S28ii3u9jgeXW01bUiE1zETarqVXQDJraNSVALbI7R5rFwuVbt1O95kmfl3HIeSK6ZAuBYyx0jQpV9ktHVtkG5vO0JNFuaIhaLBin6OJCyB26xlmixKYmSX0RunDou7X5iiOU8oTZlCKJ4qtKn9aqtm-YxC7Iie37irBF6Hc2LZ4STPApSpp2Q_Uxw_veAd2sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/ircfspace/2503" target="_blank">📅 18:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2502">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیش از ۱۱۶ دکل مخابراتی استان هرمزگان در پی حمله آمریکا دچار اختلال جدی شده و خدمات تلفن و اینترنت ثابت و همراه در شمال بندرعباس و بخش‌هایی از استان با قطعی مواجه است. /عصرایران
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/ircfspace/2502" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2501">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">زهرا مرادی، مدیر اجرایی سامانه پیشگیری از خودکشی طعم گیلاس: در روزهای قطع و اختلال شدید اینترنت، روانه حدود ۷۰۰ فرد بحران‌زده که به کمک فوری نیاز داشتند، امکان برقراری ارتباط با سامانه را از دست دادند. برای تصمیم‌گیران، شاید اینترنت تنها فشردن یک دکمه باشد، اما برای سامانه‌ای مانند ما، این شبکه تنها پل ارتباطی با انسان‌های ناامید است. قطع کردن اینترنت، فاصله میان زندگی و مرگ را کوتاه‌تر می‌کند. وقتی شبکه قطع می‌شود، افراد آسیب‌پذیر دیگر نه تریبونی برای شنیده شدن دارند و نه راهی برای دریافت کمک‌های حیاتی. /دیجیاتو
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/ircfspace/2501" target="_blank">📅 08:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2500">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C4HFV-q7EbSswcgOQfxPKYNm8UMmPWqCiE5xmz0mvzQooDrL_RcX2qaahi9qBdCOeYiilJN-Nd-JDpPnZPgb3c5cCDNdknNB9JXvq9XwLf4Cd_ZdztVubDzbgWcpwlyANj4q8YWRB7OdOUzIlkvSaG8TCWvjM2xLTWbM4xQA-zhfoTkaq2LcLtvrA6dxNVW8CPX6ivQQy-uv9sMqL4Suu4DSQCu2YK4Ihhi3ytNgH5mLS4E4hCBRHvK5C49cfrbzcDRxPJ_ye8PDEjXizYgRrqO_zIhNu1zrTtP2YKiYiNAqlrfuSky-LKXEBaZ7s5Aby4Xx-umnEbRksJUvKhz-4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگرچه قضیه ترند شدن "لغو عضویت جانفدا" در نتایج گوگل بزرگنمایی شده، اما یه نقل‌قولی هست که میگه "وقتی دیکتاتورها در حال سقوط هستند، فقط دو گروه کنارشان می‌مانند: هم‌پیمانانشان و احمق‌ها".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/ircfspace/2500" target="_blank">📅 07:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2499">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tyamoZR_vIW7jmiZXEGOPDpLyVA3eSwdnYe2I2K091a7mN5vGyBMh-FF8fxvYYnvyMKmTFQ_YSxhg37btk53YWGM3JOxTrlY4mOyIHhp3TXDoEmBKVohQloSMrqzOz6Mc6mi1cWcKo9--AMbfvNsunovJaNtr3aTNXeAXd1VhThN2nItW9nEPeeAoInYnIt3VgrWVno8XMqtpCmdlZxTtORyiGEyGVHTI57iERDJ4rgY3MFnFp2_F0fLfKgN1695bCCulVkFcSGDCUkO5s1lvrRNYPQWfk1TI7Za0zV_ZNzsiHEmn8RMvzBzQV_YvLPBooq-6n_iAOwhXJ9OM9Uodw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/ircfspace/2499" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2498">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/ircfspace/2498" target="_blank">📅 17:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2497">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RGfhskAtnftzFZEhcwc4HimyeKquMb8tC3ejdxY6I6QxIt6NfXDCbqPHtDNRJVKRCJa1axkUtFFoeLotEaLnj8J2Rg6msjVE-Y22CWt9xEJhkK_kTyHYJRikmH-hMStP_GfR7OAN9oDWVbM4CPX5Tq8ZWNOYS1VGS7SyNrj2zqV1GuZRvMeCK27YVhxEPXBHFWqRPNuXqX7V3HAb7aGt_2DfezmFQsUI9yA8_dU7DhnZaV7gK-i89S5A6INtP3jFeXIMU1YEo1BK46RCg-QUay4ChRW703k4UDUhcZSic6upwVIGqkfMT0EYchxMhUBYQW-RL97AbLPMPMhFnb5k9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/ircfspace/2497" target="_blank">📅 16:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2496">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PHV2Ek53ywqPZOcSROgReYFMm_qaFrMQUpuvST5t5Q_G6cj9ri0JrsLCHDv2CFVBDHEz-mOG_fdqj0pGU-Z5k2zRD1Ei2h42Y7u-KQMMAGphYfLhPiDKHKzwjg6RZraCtKFUBMdwqNa7r_wCdWkrzcIOpuDPIQTayIqmjri_7mXPMalA9AdP20knpvnP8Xjh2gZDrsJTRIB745N0fU6akOTTLzN3998DypNrwotl95IIpAc58apzpI_jPQ3SP-IZZIOCNwyoYFywhFOTFqziEavTGPA_zvhrP9r8iZgbTo3f9LZikO1Vvtoc9VaNoGczmY4T99bFfXfCO-WlMxidWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/ircfspace/2496" target="_blank">📅 08:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2495">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S9-_ABIFeZMvAvari1L5S7-FzVE4oBf193kDHVzcnGbIit5mwRSIsl_xfIuZG8wIFFQ1GYjIcd9DzLmD-8SSEDwQsBAfzFCr_eWvBG-bzlq0SAvjnK8TeUe6O7H9smVc8IZAY0uekagvQ62-kZh9nBCckDnh5bRNsUfKlYIsnhzUolmjZU0BJFqts0QDy1KKu3ZQ-oEl5ylagcrNnS4K-CpuZKHrqW13IbPbFpTEwiydMUqocSTJjoVS807MsSgAwHB-7P2fDGvZmp9vgAhiXftRi2kGfQFeBdCfWK6uPUPSRJ5XtCVp1JvB8yid_3Aj_ndoXwUaedSj1wt-XOjuNQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/ircfspace/2495" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2494">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WBCjv_KWTUlZ3ZVX5yHK4scRV2Buelu50mEF2TPI74ZJCRXoAKqJZjLvEOtl4eoZN72drIXKUPTzV3U8qeSqLV50g9eWxW9WhXwTbv3l1Rbh9jFzKqcPuofPy1lnCOTlEKVGUp3MEIhoBBTMxywWvissz2JyUALYh0FDFfgi0srDVax9hV7NrAML3qJI01GHaXZ-bhwR0Kbcss98Hhzmdx4dPpmpTkOkaTMEHDxS7lgZIfw4neB-cB8vf5puwzMPSN16eVWGbwkyKFlW953R4q-j34wQaQ0kEf2ti_Jbkjq4BVUo8Hi01g4_6PI8Bcdgdc42V7AMXsxPGDOV3TzlOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36K · <a href="https://t.me/ircfspace/2494" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2493">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gFRjNGg0kNMsrx8tmaT_yY3Fw5NDs0WFMMFCv32H3P6WZ60jbh6f0WVUe8CpY_GxthIphyxM8FA62eunEexAS-nxoBfn8gg-1zwWsxhVvWDyxu19_7qJinw8ptv32P76jMqx_4b65f6LPKbZb-f0dN_1fPwAgaXcgHfBiqGWn56M42hlBRDEYnDltBWewVQP0vd8oWoPXExleBdDOC94GE6ZoeHO59xG46AM7wqacW7_ghtv-53kf2OPeUYnt31DdtuwQYbmOnK2KEwRGvbCV_7NumQ04MqPm73u08PHb74cuJpLGFQgkdEP3xNdndJo-YlK57EQZXAzU8CkAQyO0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32K · <a href="https://t.me/ircfspace/2493" target="_blank">📅 19:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2492">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jEyXRvapfEpVUUgVC7j7F0oGu1QXolD_cm-TdrcZ49hqeGtu10KzgHmJofZRVEPnW8eTjgGRJbaxmDZHlgJdoPAfeeZ5aiNx9ElvBEDFICZ5m9VDFRBG4HSe8mSwkLva7OKS8mL9qPfP8sJ-7Sh2WNqKx7aiLdM6IOrlKDbLIr4yVQusLAz-7PWQoj6r8Rp7mK38d5tMp03mgmgvDgPc27ZEpdvEdmTW0ZeY2_udE7utcWOgF17-ldPn0UcgU4jd6exFb8-5xXIooupEaf8oYs7gUNj6sl6_ZWfglOf-FYL-KC023AcZPEiQy05BJpgICCffgdV3lEWHyTDgR509eQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/ircfspace/2492" target="_blank">📅 19:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2491">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نزدیک به ۵ ماه مجلس تعطیل بود، آب از آب تکون نخورد. ۱۵ ماه وزارت قطع‌ارتباطات هم تعطیل بشه، وضع اینترنت بدتر از این نمیشه!
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/ircfspace/2491" target="_blank">📅 19:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2490">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیروز کاربران گزارش دادن که IPv6 بصورت محدود روی بعضی از سرویس‌دهنده‌های موبایل باز شده. همزمان گزارش‌ها از اختلال شدیدی که روی اینترنت موبایل و ثابت بصورت منطقه‌ای اعمال شده، زیاد بوده.
در مورد اینکه آیا با از سرگیری جنگ ممکنه دشمنان داخلی اینترنت رو قطع کنن یا نه، نمی‌دونم. البته قطع مجدد اینترنت از کسایی که ده‌ها هزار نفر از مردم رو توی ۲ روز قتل‌عام کردن، بعید نیست.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/ircfspace/2490" target="_blank">📅 08:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2489">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-UCmMNtu_A6ZnIzcD8cTx7gclXbcgmbtGjn94Ep2iNq9_Knmeohxbz_ogVB-gO4FoYUbMPc6XTkovHcVFKrnyjkwpxdJmB6sW9Osz6yrwmatMcP9FybbttRiaZIhvSMK1g6LzPqreJG6IU0NG7GlJRDJY3rZJtGoYMf8jnEJKOCMnacBWC9j4hMoxJO0GZap8jJamTXu3vEax5iR_V4DHBmtsJpKzY9iJ39Blodo8VMnWFuXhBAPzO0nOffcVTT98ZqC7duRechMPSfbqHwllpnicl45vQh8cJ5PPTKdMS54vUnjBsb54msJV8eYTwEWH4fnDhCukxpGv6QV8rhtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/ircfspace/2489" target="_blank">📅 07:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2488">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RXniQdQeDLJSKV0igfEGQbzCzfrBzX93XFrtzGDgJ6-VouGPFcd-7wRnBa4Z0zwtWI6eS8BTzNxBUEOQJ0TbAkgvc4tLHmKGo40tPryJGgj5AqUbst5Rhbg1oZSkwEnGc2636yCw_V1QyXxslyyhgWSk0o4ohJ3gVgaFNL6MAg6x1BKtemLqZCf3NHVeOI-DsVopSKJD2U-SNAMUCBrBi60y9zXGX2bq3_XUhJUlqqLbX7vY135Owtg4o-8B7-m3IbW6Ws7kOPKV4M7cMGpfYzO31j0aDttDx6Loa_vIiAcCBJ2hgh_YdQfBS1xIPlfbARGgkWncvyeEKRcCtXFyMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/ircfspace/2488" target="_blank">📅 07:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2487">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بانک ملی اطلاعیه زده که "کلیه خدمات بانکی و مالی این بانک شامل همراه بانک و اینترنت بانک مجددا فعال شده"، اما ایسنا نوشته "اعلام بازگشت خدمات بانکی به شرایط عادی، لزوما به معنای پایان مشکلات برای همه مشتریان نیست و گزارش‌هایی از تراکنش‌های ناتمام، کسر وجه و اعلام زمان انتظار تا ۳۰ روز کاری برای تعیین تکلیف، نشان می‌دهد بخشی از کاربران همچنان با پیامدهای اختلالات اخیر دست‌وپنجه نرم می‌کنند".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/ircfspace/2487" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2486">
<div class="tg-post-header">📌 پیام #19</div>
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
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/ircfspace/2486" target="_blank">📅 20:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2485">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyHLJqmE6xckU_cJTqweZK_OTIxM0uwclHD94szbgMgvzyBhLZiPnVYMT7n2AV3FChTZHg-TuRlUXzW79kJ0mlRYCcfRQ8NX9VDu55ExdtJFe1hj0w02l2xwxdOPAdmC-V-5hME_jBpViLvfclCBmjoQwuXJ1EVDXvRsmeJ1dlv_yLU5ZTductceinreuD04jCvY1MdlnBNEzWvXbipLV0D65UW6JKvPYJE3rSkmEShYcnkkKaM-HpfcPaVw3rOtoJka3cy5P1admSYpm-pYPt1g3kjN1bWt88LBN5V9PyNNSW1ZpSMqJhxHa-7jqpkQ9IlU_zZQJ-2TCsF_fxfjBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که بارها نام اون در گزارش‌ها بعنوان یک اپ ناامن مطرح شده بود، حالا یک محصول پرریسک دیگه با نام SpeedTop VPN منتشر کرده!
این برنامه با وجود چند میلیون دانلود در گوگل‌پلی، طبق بررسی‌های فنی پس‌کوچه دارای موارد نگران‌کننده‌ای مثل وجود تعداد زیادی ردیاب، درخواست دسترسی‌های غیرعادی و کدهای مرتبط با شبکه P2P هست، که می‌تونه دستگاه کاربران رو به بخشی از یک شبکه انتقال ترافیک تبدیل کنه.
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/ircfspace/2485" target="_blank">📅 08:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2484">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CSpUN34zZ2Lt3ay55jaW60wGeWwVvrDsRjTx7qAi9SllIYV4ugl14z5SMrimNX_0hiLI_HqABq4O5ukPSS5J9x1xX4MJ3sxlkhlw9HlsQWrBTPscqc5w1IqKddqXvelJB3kv0rKQ-Aup1vJZD-6EVFo3BpsrDAOCX8_0SDlYXzsGib_UaIOEmCeHCyYUGgRZAXe9h66fxzTqG3cug6SFiYlhJEfdBuYt1O2EmakTzsmbwhVZEpX9D4HE7iE6kTUEo7ZVasECskxdVSYtEIcSq_qOwqYoMusn6AlfPH8vG20gMFHJ31lhYmYE11s1zWX-EVNOUgEDRc6YIx7gRp3fPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/ircfspace/2484" target="_blank">📅 08:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2483">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B03AS5Oeqxp4v23exlFeaVPVOJiwB9spvgrV6v1voVbCVqaQKxj0tpStKQ36rZeAIqOTFFFFfEM9gBYyznH30jDaciF55_XH44uciO1N0SNWFGvqRHtdytf1HjBO3ko8v8jSTc6MREYh1KzmiR0gAnafu2p71A1koN2W7FOrI451CUo9TxiIBRrD4T5m07bKn_o_dQvu_ehoz3BhnY90cslNdhkFDw_KV2hdj41eAsvxmtKH-G25y4G0PtqRdz3pv6bSkvN__DMqu0y6SKVhBX9aA7aDEvHP5FHIPiLCnQ9aYrOYyz7jCK36ny9LGpFym3tpfYAY37r55UQC-mLzGg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 33K · <a href="https://t.me/ircfspace/2483" target="_blank">📅 08:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2482">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b2ig-0rgkD3fA0qD4WlqEBwxMMI77FiNaVSXoD3DTNNqNhgrfxkGYLJrXJUsOl8xxn7DVAXOQNEryA97GJG2MynODiBeoeH30__SbZNoDe44y_2PKBb-K52O0z_-Rfxe3TLlVv-6_2V1Tpl2pvEWyNyhOlGP8chnSz5FaP1rtirhmcfso6V9Ka1_91IIxvnxOjZH9nOgKew4U1vwdmpH1SSmb94xA7FcjjHLlRd06c1wP3mwuSe8a1MUZ5zM7hMBr3LGOFWoOi3nOK8xj7twbPMV5QHHqLnE1yuJa2CVhCdlP8qOZGTG44fOMaTp0YynZd_mNYeASnh6KLj2GJ2-HA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/ircfspace/2482" target="_blank">📅 08:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2481">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dGMRjwoezdp9kQp_-MJ0WFvvTc4ceIXk304KfCijZgk8Kv2HjzPmkgXr0-a6LcLoni22gZ4Oo4Y3Fa6g2BZewmWo9aOaYlvRtXE4kyw7rGszDK9OSBRpzwYnbLyGdQd16AsVVkCNK0-1SK4kma5IL-ZZfxApbcQG_U9PgVuHykSLIL14lvw9h_Gl2bgT9TaDO65eUZe7fpt4Tc02AvZnmtMtpjNDS2JlmGm9A0_XxAS0_PsKQ-nrUKQplfkr2kS464qRdgb0n1QsSNH0enlPxLhFCzuFrVzJxvSETwGIVz6O5bfRVdo39sKVpG-6IrWwBzpGfBsN3G7pkkmoW6_VQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/ircfspace/2481" target="_blank">📅 08:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2480">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rJ1Qd73TZPLUEJogBGXBvfSVR0x2WC7ZaHo1aSMfX8NhQhIuv-PzQpoEo4Fj1AERmHdPTHdAPT6wj9ujm7gJT0kYAladIaPDmcBBk9oYMsum-5gdM5GbPZRp8z9rvNi5KO-iydZooaKJ9mOthGjlYrXXMPBwjHdEN-FTwg9_pAjee7WN8ryY1ULT8nqnzi2R45N1qCro7JPpPb2yNRAoqDtWQ6n-u3WHv3iEJTKAVaZhqDc662JDZssTBFs7jRsUbyp-i1JoOF_K_I3V7r2uoj92HHx06433xP7YAp0DS1oM3zhAmcffwElVTh9KDPx_TsOyfGK8SkrTIbHdI3vkBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/ircfspace/2480" target="_blank">📅 08:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2479">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HUrLiS4hC5ncTCcARlFkDkkK89VpKRhABQhbZk2fUmcKNsSlIaeYJcC-TO_-8N5TWTNVs5zyx7Fc3oCZkuaaxjLKjNdYmZhK8lsfE1DQFOXRl7aLYnxAtWkoKUkeYNVKjWGeK6GiTxbb6HwXQ-wUtIehoODm6GIVwAVw6N2OBWC3mc2fmYa61NzdOD6gHr5O8E6O3EBdDLsX7I9y8axwT6vp0_yWmCHQIllrI2cnxH5Zl3S-AaBnGi2kAGowZbOtZK7GM0MZ8s71QQYzuyHVaNUuCPXXkul0yQ7JG7us7u8LkjWjYSbfPlFjnh_WdBBxY5FwpSG91-rT292FV5uwOg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/ircfspace/2479" target="_blank">📅 07:49 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2478">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/moEnzsogmEF8vjhZk-Fgg5jDZzCWjWfvC-DZL7Rwiv_hpqoa04rO2cPdaD4nSOJd6aag7PYr2ijiCvEiGCYc0XbMkGXC5ZYbXmPWUwcew-TcAs5AqQLAM9alFJZu2xQQcBKc_v53oe4mUgaZz6CEQ1RDya1T-gDLpiiDXMapH5360xv03-DSK_PTx69oR7JOQdEcbBn8MeRVwN1_IQ9-x4iTVIpqD53whQQkYyVoiar_mUPj1gcqyBlPl760YCu70-Vs9MUq-U1SEdVceLHkuGbEVNHPVt7obtv_nE8Lof-GdSiQpTmXHtv5s-yTdh33urqjR8kdHhtd5We2DrmskA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/ircfspace/2478" target="_blank">📅 07:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2477">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xxukn9XbCU8W-O3pxVaCThNMkinztxFxRUbC4BB0nnymDxsu1cov5gQUKKzHHGf-DkNQKapUvRotsiwhi_Qs-fw2LKezhD31JKOPqOsqmCeUTt0u-ceUlm2oeaJQRkZ6k2AzioadVVbvkq-TPKbMjZ8m63-aw1vICYvvL92x0W4o9fJiNx05LUJxR37GsSnoiHN-UvKl-rWsbxFV4aPp5OmK4fxxhf87YwWtEC83R7T-6dK3QzzoLZ8_7HDF5ZVwqcFT764AbqW3cgpOk-_0hYHm9a3GnzJ2TTI6LhQU2WW6r1lhSEg7geH7Q6in5pu3xPRaIsRgzYvRW6JZa3S5bw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/ircfspace/2477" target="_blank">📅 07:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2476">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e8Hsi2viOQNkIPUr0IuT387dl2obN_MJ9YmhKoK3xED3aRTyCjTXRkwQ9Na5CaJ4rVnAAzqhB7N2eQ1F6cJiZcL9DvHRd8oW9HJ5RdUsAApC9_KQnlueOYchXTpr0dYPpWiJVRFEDMXywX4qMiq87qSOKyZjgfO_Fe1xtlWO-2SuPkNzu2en8lxybLZwXLeo1vRD4khlQjwgnw7AuhdsbzUAxslCQYwg4rPC8d_-ReYFhsV4Kz9gNRpng5bTOmVKq49iY0Y1MjwH77vEMmLN14cOYGYRscK7Vrdn_meSCs2CbeZ1hblcrLyLKcvpXzsdBNHIwjqJntN8s8zs9PKfqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایک سنتوناس، مدیر ارشد فناوری شرکت CrowdStrike میگه خیلی‌ها دارن روی این تمرکز می‌کنن که "کدوم مدل هوش مصنوعی خطرناک‌تره"، در حالی که تهدید اصلی جای دیگه‌ هست. مشکل واقعی اینه که هکرها حالا با کمک هوش مصنوعی می‌تونن آسیب‌پذیری‌های قدیمی و جدید رو ظرف چند ساعت، و بزودی شاید در چند دقیقه، پیدا و سوء استفاده کنن.
به گفته او، هوش مصنوعی بیشتر از اینکه باگ‌های کاملاً جدید کشف کنه، باعث شده هکرها بتونن تعداد زیادی ضعف امنیتی شناخته‌شده رو خیلی سریع به همدیگه وصل کنن و ازشون برای نفوذ استفاده کنن. یعنی اگر سازمانی هنوز وصله‌های امنیتی رو نصب نکرده باشه، حالا خیلی راحت‌تر از قبل هدف حمله قرار می‌گیره. هوش مصنوعی لزوماً حمله‌های جدید خلق نکرده، ولی سرعت و مقیاس سوء استفاده از ضعف‌های امنیتی موجود رو چند برابر کرده و همین بزرگترین تهدید امروز امنیت سایبریه. /اکسیوس
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/ircfspace/2476" target="_blank">📅 07:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2475">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jUpHTT2koQOiGElULb2sn1114t5JDbp2sdBfb9LeHidZMg8QuAw9jbH9FWFaTl7-3ki4jDHEu1s437wMwu_24V6140NMJWv6RzcfRFPjBlkAI_SDmZJ31m88AVR6YDkJ0jLmovpxFMQ7_rYepUhOh3HKcohMiwuI8s1H384OtQE6QieYluKjl32SxTLw9nA-uCK9yqIekdimR9ZpUahfmJaG5QX-0byGdcofvU_mVOyPkAmX6mkpVmCHSLwBhRXJguLPhQebU9XvmXI05tz3Gx9VACnG_gC9QS2WjgJxyNRutnneLftUBmONsDybvRA_ornWERzCVscQ06i-MHcL1A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/ircfspace/2475" target="_blank">📅 08:14 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2474">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آموزش راه‌اندازی پروکسی تلگرام بر روی سرور شخصی ...
📽
youtu.be/pyvB6VSPhwg?t=176
💡
github.com/SamNet-dev/MTProxyMax
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/ircfspace/2474" target="_blank">📅 08:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2473">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bl-2jxZp9EgCOsODH1CnQEzzP2o1RypCCK0q3lp8yKclAdhWrOHs1f8tlUdRFL4WyB2Jp4obxs_FJzA03ZTFU3OgOGOhySfXv3Y-lp2widWUdWiZZOtyuYe-K4H2XtTtZYlX4SeYFugjtcaXlwMsOGtwCTRyxNre0_zcaUer18WL_cYAZp90U-szfzxup5WmjpLEH3oOU6GBt7X70lybt_25zmjcd4riquceP0qkBeTlByg3J3kmk2khW2ti5H-skYICRqXylqnitCp1WKTRgv20Zj1D3ZZyJKKUZ5oUrSRtX93E6S0zm3ZXMRdnUO4DDVNzPc3y4usgHByqNMwhrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر سیمرغ یک ابزار متن‌باز و رایگانه که برای پیدا کردن آیپی‌های تمیز کلودفلر در اندروید و ویندوز ساخته شده. این برنامه میتونه آیپی تکی، رنج‌های CIDR، رنج‌های دستی و لیست‌های آماده ISP رو اسکن کنه و بهترین‌هارو بر اساس سرعت و تأخیر بصورت رتبه‌بندی‌شده برگردونه.
👉
https://github.com/rezakhosh78/SIMORGH-Scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/ircfspace/2473" target="_blank">📅 07:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2472">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e7626zVZjjKz8W7vc5dTvoMLCgQm-lr6PBQsLBiG0pTwteBfhXG7s8JWiOkC01yl3dJKm6FI11Gfz_ejm9VUeb0HAMouS7KWw9_WpmRU0HO6BVc692ltwQyf0segzrOKig8RaJ8NFOA6Gvkdg6YltMsifTm1M7zlC88Yf9PlJc870Zwzfn1pZTwkRzvvDtxzJTCZe7NBt-_wxImVEomNCScX1NO3WFFVFm10MJVWBlaHd81d6UkFWPGkkNPDKT_RXntPMeUnz4WcZ5PLleps-E1Y0Zi2AZ16iDDPutRkd48hv6vcy9bLdL31cnYx6P2-Hdms5y1Kxb04XJi16WPNDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکنر Asha یک اپ متن‌باز و رایگان برای اندرویده، که با تمرکز روی پیدا کردن آیپی‌های تمیز و پایدار کلودفلر ساخته شده و کمک می‌کنه سریعترین و مناسب‌ترین آیپی‌هارو متناسب با شرایط شبکه پیدا کنین.
حالت‌های مختلف اسکن، بررسی لیست دلخواه آیپی، شناسایی دیتاسنترهای قابل دسترس کلودفلر، امکان تست سرعت واقعی از طریق پروکسی و استخراج هوشمند آیپی از وبسایت‌های پشت کلودفلر، از جمله امکانات این اسکنر هستن.
👉
github.com/ashanews9776-eng/asha_scanner/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/ircfspace/2472" target="_blank">📅 07:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2471">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نسخه ۱۷ از اپ
#MahsaNG
منتشر شد و توی این نسخه هسته سایفون بصورت ویژه برای شرایط اینترنت ایران بهینه شده. همینطور امکان ساخت، وارد کردن، خروجی گرفتن و اشتراک‌گذاری کانفیگ‌های
psiphon://
هم اضافه شده و یک اسکنر IP جدید برای CDN Fronting طراحی شده تا پیدا کردن آی‌پی‌های مناسب راحت‌تر انجام بشه.
امکانات جدیدی هم به خود برنامه اضافه شده؛ مثل دریافت کانفیگ‌های ایکس‌ری از طریق نوتیفیکیشن گوگل، قابلیت زنجیره کردن دو کانفیگ و حذف کانفیگ‌هایی که موقع تست پینگ توی ساب فعلی پاسخی دریافت نمی‌کنن. رابط کاربری بطور کامل بازطراحی شده و جابجایی بین ساب‌ها با کشیدن صفحه به چپ و راست انجام میشه، مدیریت ساب‌های بزرگ بهتر شده، شماره کانفیگ در حال تست نمایش داده میشه و از این به بعد خود اپ می‌تونه اعلان‌ها، اخبار و بروزرسانی‌های پروژه رو مستقیم به کاربر نمایش بده.
توی این نسخه مشکلات مربوط به اتصال مجدد و کرش سایفون، ایرادهای ویجت، باگ‌های CDN Fronting، کرش نسخه ARMv7، بازیابی نشدن رمز عبور HTTP، وارد کردن لینک ساب در بعضی شرایط و چندین مشکل دیگه هم برطرف شده، تا تجربه استفاده از این فیلترشکن پایدارتر و روان‌تر باشه.
👉
github.com/GFW-knocker/MahsaNG/releases
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/ircfspace/2471" target="_blank">📅 07:58 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یکی از نکات جالب اختلال ادامه‌دار خدمات بانکی اینه که هنوز چک کردن موجودی از اینترنت‌بانک با مشکل مواجهه، ولی پرداخت قسط با قدرت کار میکنه. در کل هرچیزی میخوای از حسابت برداری، به خاطر هک به مشکل خورده، اما هرچیزی میخوای بذاری، میگیره
🤡
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/ircfspace/2470" target="_blank">📅 07:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2469">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مخابرات قیمت اینترنت ثابت را سوسکی بیش از ۵۰ درصد افزایش داده و آن را به بدترین شیوه در محدود کردن کاربران و تغییر ویژگی بسته‌ها انجام داده است. مثلا اینترنت ۱۶ مگابیت قیمتش ثابت مانده اما در سرویس سه ماهه، بیش از ۱۰۰ گیگ از ترافیک آن کاسته شده (۳۶۰ گیگ به ۲۵۵ گیگ).
حالا شما اگر بخواهید تقریبا ترافیک همین بسته را که تا ابتدای سال عرضه می شد بگیرید بایستی ۱۰۰ گیگ ترافیک بخرید که قیمت آن بیش از ۲۰۰ هزار تومان است و در واقع همان کلاس ۱۶ مگ سه ماهه با ۳۶۰ گیگ از ۳۰۰ هزار به ۵۰۰ هزار تومان تغییر کرده است. انتخابها هم محدودتره و برای ۱۶ مگ یا همان ۲۵۵ گیگ را باید بگیرید (و بعدا ترافیک جدا بخرید) یا انتخاب دیگر ۸۸۲ گیگ است که قیمتش بیش از ۳ برابر است!
©
alirezashirazi
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/ircfspace/2469" target="_blank">📅 07:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RPUJ0rCQVXatIxYbM802kxBb0A0vwvYqJ5-yEwVadmPIEVGTZZ43EvBV8yF9qmjCF9M52C3yw_BHLiL1hApyn3E9XCnWGyXy7eZNLcnXryxCDqNMOUJpRAj_xj0gJXS0eqlDToTiWUOSW0g-27YblT0SALUQTfUnlbqD1jJUmhusbwOsmWcJMAlYAJeUS_mBj_54SE1QyiPpEiKAoIIgUeOKH7kvGnT0xeCbD0S7Nh8fXZB-3I_zLWwQluUZ3eD-C-N3IAZwhFN-LrPiBo8YOgD_sQUz_3mG7ptWZCgnJdAQt5vMicyWIS8hAg1M0UMep0fI-PIm6tt3XsZW_-jh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر قطع‌ارتباطات (که به تازگی بابت عملکرد درخشان وزارتخونه در دوران جنگ ازش تقدیر کردن) گفته "لازم است با وزارت نیرو برای خارج شدن سایت‌های ارتباطی از اولویت قطع برق تفاهم شود".
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/ircfspace/2468" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
