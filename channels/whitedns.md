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
<img src="https://cdn4.telesco.pe/file/jOvxlopzgeiq7bNOXxckQFV_h5ziF14FNC5aROcJ1AFUewLvhK7iAfnDoO2X_DtGXOuv5i7y0e57s77e6ljNPP6H1aasB8CnJK3jW9UuVKZr-pkU9ZwBXxabDIG70w-Sbw9XDezKAGMHPKVhZjJMF3brBQiAsBDeKk8eH0dmW2_RIoYyXzntjoIkuXwVyxGdU70FHf-s3-CW4Hf6Q01M-5WPfqiXppBu5DAvtlrNruM4cAZAo-iNi3xTDC9-sEhm2Q5YZNjPfeoooNcrZL27L0vL9zyjG5XriE4uxJjHB2lOkfZtAEFcLrQnMTsAA6j7eudEiWuXxxFt9iMHrwWvJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 109K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 گروه :t.me/whitedns_groupادمين :@WhiteDnsChatBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 23:27:51</div>
<hr>

<div class="tg-post" id="msg-1355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">3 سرور اهدای CottenDNS
لطفا تست کنید و نتیجه رو بهمون بگید ( کلیک کنید روش کپی میشه )
Server #1 thx to Araskhatare
♥️
Location: Germany
🇩🇪
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #2 thx to Araskhatare
♥️
Location: France
🇫🇷
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HqfCfh6ogdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imdlcm1hbnkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI5ODQ0NDhjZDRkZTYxZjgiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
Server #3 thx to Araskhatare
♥️
Location: Israel
🇮🇱
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgQ290dGVuRE5T8J-HrvCfh7EgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyMjRiOWU4MjVlMzFkNWY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
@whitedns</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/whitedns/1355" target="_blank">📅 18:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS   cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcn…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/whitedns/1354" target="_blank">📅 13:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
👆
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
❤️
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/whitedns/1353" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.6.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">8.8 MB</div>
</div>
<a href="https://t.me/whitedns/1348" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/whitedns/1348" target="_blank">📅 10:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1347">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvU2p5a5yPJlkPHLg34t280S9_i178atDJsj-_VLT7EbUQoud4yBTH5kvY9BcH3lcV-PqNL1frUZXlw0poqOPC6nEURhmbN80LL5ICwpeQGGomgq5SKjYVBu3SrtH0QyutNWhVo0zO6rfe09uCq-8OIpMPbIhpASJ2OHQQWX8iK-h_GIeks4O_pXLiWaonjUMty9sZjCNkusk0CI6Etu8-TpB42w_OMr4cc7SdKz_dzCii4jQjIGB5zTNf93IZubtUeE87IHTINqda-MPWfoZuNwVYDHpinXV4e6PODVTdXgQ_pK8lDkzyrgr3tVpy1J7PvieA4iOfGS85qMRmjYvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار WhiteDNS نسخه 1.6.0
در این نسخه، پشتیبانی رسمی از موتور
CottenDNS
به WhiteDNS اضافه شده است.
CottenDNS برای اتصال پایدارتر در شبکه‌های دارای فیلترینگ، پکت‌لاس، DNS Poisoning و اختلال شدید طراحی شده و در هر دو حالت
Proxy
و
Full VPN
قابل استفاده است.
مهم‌ترین تغییرات
* اضافه‌شدن موتور CottenDNS
* پشتیبانی از چند دامنه در هر پروفایل
* تنظیم مستقل MTU، FEC، Duplication، رمزنگاری و روش انتقال
* بهبود Import و Export پروفایل‌ها
* بهبود رابط کاربری و دسترس‌پذیری
* سازگاری بهتر با Android 15
* ادامه پشتیبانی از پروفایل‌های StormDNS و MasterDNS
این نسخه انتخاب و مدیریت روش اتصال را متناسب با شرایط مختلف شبکه ساده‌تر و انعطاف‌پذیرتر می‌کند.
📱
دانلود WhiteDNS ورژن ۱.۶.۰
https://github.com/WhiteDNS/WhiteDNS-Android/releases/tag/1.6.0
⚠️
⚠️
⚠️
لطفا تست بکنید و نتیجه رو به ما بگید
سرور تست CottenDNS
cottendns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQ290dGVuRE5TIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYmFtYWsueHl6IiwiZW5jcnlwdGlvbl9rZXkiOiIyZGRlYjlkZjJjMmJhNGQzIiwiZW5jcnlwdGlvbl9tZXRob2QiOjN9fX0
@WhiteDNS</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/whitedns/1347" target="_blank">📅 10:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1346">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌎
دوستانی که با جزئیات فنی پروژه آشنا نیستند، به زبان ساده
CottenDNS نسخه‌ای کامل‌تر و پیشرفته‌تر از پروژه‌های MasterDNS و StormDNS
است.
تیم ما طی چند ماه گذشته، با استفاده از تجربه‌هایی که از قطعی و اختلال گسترده اینترنت به دست آوردیم، روی توسعه و بهبود این پروژه کار کرده است تا اتصال پایدارتر و سازگاری بیشتری با شرایط مختلف شبکه داشته باشد.
نسخه جدید اپلیکیشن
WhiteDNS
که تا ساعاتی دیگر منتشر می‌شود، از سرورهای CottenDNS پشتیبانی خواهد کرد.
هم‌زمان با انتشار نسخه جدید، یک سرور عمومی CottenDNS نیز در اختیار شما قرار می‌دهیم تا بتوانید بدون نیاز به راه‌اندازی سرور شخصی از آن استفاده کنید.</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/whitedns/1346" target="_blank">📅 10:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1345">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
معرفی پروژه CottenDNS
https://github.com/WhiteDNS/CottenDNS
نسخه پایدار CottenDNS با تمرکز بر اتصال بهتر و پایدارتر در شبکه‌های دارای فیلترینگ، اختلال DNS، پکت‌لاس و تأخیر بالا منتشر شد.
در معماری جدید، سرور به‌صورت پویا با تنظیمات هر کاربر هماهنگ می‌شود. یعنی کاربران می‌توانند بدون تغییر کانفیگ سرور، روش انتقال داده، نوع رمزنگاری، MTU، فشرده‌سازی و قابلیت‌های بازیابی بسته‌های ازدست‌رفته را متناسب با کیفیت اینترنت خود انتخاب کنند.
مهم‌ترین قابلیت‌ها
🔹
سازگاری با شرایط مختلف شبکه
اتصال می‌تواند از طریق UDP و TCP روی پورت 53 و همچنین DoT و DoH انجام شود. اگر یک مسیر مسدود یا دچار اختلال شود، کلاینت می‌تواند از مسیر جایگزین استفاده کند.
🔹
مقاومت بیشتر در برابر پکت‌لاس
CottenDNS با استفاده از ارسال مجدد هوشمند بسته‌ها، Duplication و فناوری FEC تلاش می‌کند اطلاعات ازدست‌رفته را بازیابی کند. این قابلیت‌ها بر اساس وضعیت شبکه به‌صورت خودکار فعال یا غیرفعال می‌شوند تا سربار اضافی ایجاد نشود.
🔹
مدیریت هوشمند Resolverها
Resolverها از نظر سرعت، تأخیر، پکت‌لاس و سلامت بررسی می‌شوند. Resolverهای خراب به‌صورت خودکار کنار گذاشته شده و پس از بهبود دوباره وارد چرخه می‌شوند.
🔹
تنظیم خودکار MTU
کلاینت اندازه مناسب بسته‌ها را برای آپلود و دانلود پیدا می‌کند تا احتمال شکسته‌شدن یا ازدست‌رفتن بسته‌ها کاهش پیدا کند.
🔹
مقابله با DNS Poisoning
با استفاده از روش‌هایی مانند Transaction ID تصادفی، EDNS Cookie، تغییر شکل درخواست‌های DNS و ارسال از چند دامنه مختلف، مقاومت اتصال در برابر پاسخ‌های جعلی و دست‌کاری‌شده افزایش یافته است.
🔹
انتقال داده با فرمت‌های مختلف DNS
داده‌ها می‌توانند با رکوردهای TXT، CNAME، A، NULL و HTTPS/SVCB منتقل شوند. کلاینت می‌تواند بسته به محدودیت شبکه بین این روش‌ها جابه‌جا شود.
🔹
امنیت و رمزنگاری
روش‌های AES-GCM، ChaCha20، XOR و الگوریتم‌های قابل تنظیم پشتیبانی می‌شوند. نوع رمزنگاری هر کلاینت به‌صورت امن و مستقل شناسایی می‌شود.
🔹
سازگاری با نسخه‌های قبلی
کلاینت‌های جدید CottenDNS و کلاینت‌های قدیمی MasterDNS و StormDNS می‌توانند هم‌زمان به یک سرور متصل شوند. بنابراین کاربران قدیمی برای ادامه استفاده نیازی به تغییر فوری ندارند.
در مجموع، سرور CottenDNS امکانات مختلف را فراهم می‌کند و هر کلاینت بر اساس شرایط اینترنت خود، بهترین ترکیب اتصال را انتخاب می‌کند.
❤️
Thanks to
@masterdnsvpn
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/whitedns/1345" target="_blank">📅 10:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1344">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ciTdS373YPlEdmPGggQFB_-4jTY3_Dr4J5Gb9MUjQonl7_4ehCydTWoF8lOowdhHPRCLSiAayLYmDMSIuyGbbUq0tSIJ7upNPU6qiq0Chp9AWbnA-ymjfnw74QpOs5b1rHLOAafRq1nevDvISKzeWQjzB-Sx1o-0wgvD6tPxdTEcVErDauMKVH7HViqWgprWi5jJS6z9X77qHKfhKSYN40zre03UnJPfxEns-mYfTh2rWa-ClJSn44gw8lxUDGWc5_s2uVEsR08Hf5xhx2FBwLP7XMwjNfrbAT3GizUE6u_47con3V7tBZqp02-KxmdTOhVOQMus5X69B55u1_MR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/whitedns/1344" target="_blank">📅 09:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1339">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1339" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/whitedns/1339" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1338">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4W5US9u0Vx4S4FXixTQDpQPLSrbTJ2xbdiQBKBkOusq2rA4oqlKib8hMp3JYt9uhNrgJUXXg8N6j7jFr7t9xQde0oR6owYCIqRQ5MSP8o8AUdSYR-cusnNtFJsl42d5XV8Wvm8RKYQtgx6dg3HbmtWw7wYUyyNUgNxKoGDen0-RaIGFA83x0zptTDX0GieqTgBR3cawiowP_qeuOXIq4Yvo240SALzDcogsErVnv-a3TgsPD5siT_KOcRByewoRROjKIvxlBglzzePkOwKScp8F5TWSNXjOTj6tJX6sH0q6o0pkAXQTGMDDFpR7REs1V2tlCy7c2JIYEAfDSamsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 957 · <a href="https://t.me/whitedns/1338" target="_blank">📅 09:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1337">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/SI_4HQ_ISxDvF2gOxAYFTma0LvN6U--gcU5E04n6v5f3N369tNxxeKalmPPu6N50jb09Rszb5rpF2Nasf9Su811lTyTZEhjIW6b-rbwlVwddbp7YN1PEs4Fg8BlK9bK7yJUxk5TYy3GEw7w7XpHaC4z25-OGggxojDJaMl9_WshGXD0ybUoG2XMwJZSpmX5KdBkaAa59WqF-x9mberou08prIIXX2jHwFbvEJhKhuRC2oX5ybN4Py-28CVsy121oThByBE4hpm1Chf18NghFnwtU_BFz18nHuarLIxQSfOUJ61jL0R0SrVMABfecJ6BTeNY5PVLa7HMnsieBbK2KRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
👋
:
حالا همیشه هم پست برنامه و توضیح نگذاریم، بعضی وقتها یکم حرف بزنیم با هم، اینجا همه با هم داریم کار را جلو می‌بریم
🤝
✨
برای اینکه یک پروژه درست بشه ساعت‌ها وقت و هزینه صرف میشه تا به دست تو برسه
💸
⏳
، وقت و هزینه‌ای که میشد گذاشته نشه، زمانی که میشد در کنار دوست و خانواده بود و یا اصلاً رفت عشق و حال کرد
😔
💔
. اغلب دولوپرهای این تیم کلاً نیازی به بودن اینجا ندارند، فقط احساس دین می‌کنند
🙏
.
شما میتونی با لایک
👍
و دیس‌لایک
👎
، پروژه را تایید کنید یا ردش کنی و یا با قلب
❤️
حمایت کنی و ....
خطاب به اون چند نفر :
اینکه تو اینقدر بی‌شخصیت هستی که آیکن
🤮
می‌گذاری این فقط یک چیز را می‌رسونه، تو لیاقت این را نداری که کوچکترین خدماتی حتی با دریافت هزینه بهت داده بشه
🚫
🛠️
. تو همون کسی که اصلاً برات مهم نیست چی به مردمت می‌گذره، برات هیچی مهم نیست
🤷‍♂️
.
متاسفانه تو جرات نداری بیای توی گروه‌ها خودت را نشون بدی و بحث فنی کنی
💻
🛑
، والا تکلیف مشخص میشه.
یک تعداد زیادی از شماها که همراه ما هستند یکی از یکی خوب‌تر و مایه انرژی ما و بقیه هستید
🔥
⭐
، دلیل اینکه ادامه می‌دیم شماها هستید، والا کار ما خیلی وقت هست که تمام شد
🏁
.
ارادتمند
👋
ویسپر
🎤
تیم whitedns
🛡️</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/whitedns/1337" target="_blank">📅 08:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gTlkKIlY1mMx1qzGX8D2Mv5yGKoQuMcUyNG0kYqjF4-xAs6ghY-B4kHxb0jChD4hbd6CkgsSIpjv7PUkSf-7EHudt4Ksb_vUzAtmQ6dqO0w35erN9nqz8IuDm0gxWNtJbKd-sq8Pi0aZJ4tQzrPxb8eLCnqC21w6JY-V8wfrqNu45Vk6J4kaIO3COWA4G2pANt6xSwwCksyr4nIRnu95izM21eUbVSnoWGH4mnLfwqLn5DMkh2X0B363sG5hYkTJwFg8dylKCsZJk2Dz0jEXCyzjJfSv-NSOnMgBjXo9sjhN1Z1RqpZDLQkGeMB-G2kqoJDvngB9Yt7kKkizet0odw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Aether Desktop اومد! — آزادی، با یک لمس
🔥
بالاخره نسخهٔ ویندوزی Aether رسید!
🎉
همون اپ محبوب اندرویدی، حالا روی ویندوز — با همون ظاهر، همون آیکون و همون هستهٔ قدرتمند. نسخهٔ 1.0.0 اولین انتشار دسکتاپه و هیچی از نسخهٔ اندروید کم نداره!
✨
چی داره؟
🔌
اتصال قدرتمند:
▫️
۴ پروتکل: Smart (انتخاب خودکار) · MASQUE · WireGuard · WARP×2
▫️
۵ حالت اسکن: از Turbo تا Ironclad
▫️
اتصال مجدد خودکار تا ۵ بار + انتخاب هوشمند پروتکل اگه یکی جواب نداد
▫️
پشتیبانی IPv4، IPv6 یا هر دو باهم
▫️
نمایش زندهٔ سرعت، پینگ، سرور و IP با پرچم کشور
🏳️
🎨
رابط کاربری خیره کننده و زیبا :
▫️
کاملاً دوزبانه (فارسی و انگلیسی) با پشتیبانی کامل راست‌به‌چپ
▫️
تم تیره با طراحی دقیقاً مثل موبایل، بهینه برای مانیتورهای بزرگ
▫️
نوار عنوان به سبک ویندوز ۱۱
⚙️
تنظیمات پیشرفته:
▫️
نویز (از سبک تا تهاجمی و GFW) · MTU دلخواه · Fragment · ECH
▫️
تونل تفکیکی (Split Tunneling) — انتخاب کن کدوم برنامه‌ها از تونل رد بشن
📡
اشتراک با بقیه دستگاه‌ها:
▫️
SOCKS5 روی پورت 10810 و HTTP روی 10811
▫️
هر دو پورت خودکار پروتکل رو تشخیص می‌دن — هر کدومو هرجا بزنی کار می‌کنه!
🛠
عیب‌یابی حرفه‌ای:
▫️
تست زندهٔ اتصال + بررسی ۶ موردی محیط سیستم
▫️
کنسول لاگ زنده و رنگی با دکمهٔ کپی
🪟
مخصوص ویندوز:
▫️
تونل واقعی سطح سیستم با درایور رسمی و امضاشدهٔ مایکروسافت (Wintun)
▫️
پروکسی سیستمی خودکار تنظیم می‌شه و موقع قطع، برمی‌گرده سر جاش
▫️
نیازی به Visual C++ نداره؛ WebView2 هم نبود، خودش نصبش می‌کنه
📦
دانلود:
▫️
نصب‌کنندهٔ گرافیکی برای ویندوز ۶۴ و ۳۲ بیتی
▫️
نسخهٔ پرتابل بدون نصب — هیچ ردی روی سیستم نمی‌ذاره!
👌
▫️
فایل SHA256 برای راستی‌آزمایی سلامت فایل‌ها
⚡️
ساخته‌شده با Rust + Tauri 2 — یعنی حجم نصب فقط چند مگابایته، نه ۱۰۰ مگ مثل اپ‌های Electron! کل بیلد و انتشار هم صددرصد خودکار با GitHub Actions انجام می‌شه، بدون هیچ دخالت دستی.
📋
پیش‌نیاز: ویندوز ۱۰ (نسخهٔ ۱۸۰۹ به بالا) + دسترسی Administrator برای ساخت آداپتور شبکه
📄
لایسنس: MIT — کاملاً متن‌باز و رایگان
💙
⬇️
همین الان از بخش Releases گیت‌هاب دانلود کن و آزادی رو با یک کلیک تجربه کن!
📥
دانلود مستقیم از گیت هاب
https://github.com/QW-AI-Code/Aether_Desktop/releases/
سلام دوستان عزیز
✋
یه یادآوری مهم که حتماً بخونیدش
👇
برای اینکه اپ (چه نسخه اندروید چه ویندوز) براتون وصل شه، این چند تا نکته رو رعایت کنید تا بهترین نتیجه رو بگیرید:
⏳
رو هر پروتکل ۱ تا ۳ دقیقه صبر کنید تا وصل شه. بسته به اپراتور و منطقه‌تون این زمان فرق می‌کنه، عجله نکنید.
🔄
پروتکل‌ها و تنظیمات مختلف رو تست کنید. چرا؟ چون DPI هر سیم‌کارت با سیم‌کارت دیگه، هر منطقه با منطقه دیگه و هر شهر با شهر دیگه فرق داره.
📱
اگه با موبایل وصل نشدید: چند بار گوشی رو ببرید رو حالت هواپیما و برگردونید تا رنج آی‌پی‌تون عوض شه، بعد دوباره پروتکل‌های مختلف رو تست کنید. خلاصه باید قلق DPI اپراتور و منطقه خودتون دستتون بیاد
😉
📶
اگه با وای‌فای هستید: مودم رو ۱ تا ۲ دقیقه خاموش کنید تا رنج آی‌پی عوض شه، بعد دوباره با پروتکل‌ها و تنظیمات مختلف امتحان کنید.
❌
اگه بازم وصل نشد، یعنی این وی‌پی‌ان با نت شما جواب نمی‌ده و باید برید سراغ وی‌پی‌انی که با نت شما سازگاره.
⚠️
و نکته آخر: بعضی از کاربرا میگن این اپ مشکل داره و واسشون کار نمیکنه.
اگه مشکل از خود اپ بود، نباید برای هیچ‌کس کار می‌کرد! همونطور که می‌دونید برای خیلی‌ها داره کار می‌کنه و هر کسی تجربه متفاوتی داره.
پس اگه برای شما وصل نمی‌شه، مشکل از Aether نیست؛ مشکل از DPIایه که رو اپراتور شماست و جلوی کار کردن اپ رو می‌گیره.
#VPN
#فیلترشکن
#Aether
#ویندوز
#متن_باز</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/whitedns/1335" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=vv-Cnjsy6dqUbi2mGzfNXw-i5q6G9R13Va6vjHgAx3MafaBE95XjkmqqP64HbjodYcA1W926SsMS6tRFvRdSmFEjqOt_W6uamugLCWek8yodvouB6iPQHVwkKmGuudAiW2E1HXf8tA_MRgl-qiPI_YBgKQmCIeleBNWf8VJ3J065oPX8LH9WAd2995zrETmvI-kGCUju_m8bYe9Tsjm0LrL8yMsexGXKoPkAQaasMT3285v5sbTjVLtJoCj1IkQ1Hu5bf8Mv1Khf3RvwJ3TDi1fKFJBe1UGQv8fvTsyoOR1_W3sfPqokEF3hn-6w0pPfu0sMeOFDThtLbx76HfyIcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc8d366d7.mp4?token=vv-Cnjsy6dqUbi2mGzfNXw-i5q6G9R13Va6vjHgAx3MafaBE95XjkmqqP64HbjodYcA1W926SsMS6tRFvRdSmFEjqOt_W6uamugLCWek8yodvouB6iPQHVwkKmGuudAiW2E1HXf8tA_MRgl-qiPI_YBgKQmCIeleBNWf8VJ3J065oPX8LH9WAd2995zrETmvI-kGCUju_m8bYe9Tsjm0LrL8yMsexGXKoPkAQaasMT3285v5sbTjVLtJoCj1IkQ1Hu5bf8Mv1Khf3RvwJ3TDi1fKFJBe1UGQv8fvTsyoOR1_W3sfPqokEF3hn-6w0pPfu0sMeOFDThtLbx76HfyIcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">UAC SNI Spoofer Desktop
نسخه 1.0.6
━━━━━━━━━━━━━━━━━━
تغییرات جدید نسخه 1.0.6
• قابلیت Mobile Gateway اضافه شد. دستگاه‌های متصل به شبکه وای‌فای مشترک می‌توانند بدون تغییر تنظیمات Proxy، IP یا DHCP از VPN کامپیوتر استفاده کنند.
• امکان پینگ‌گرفتن از کانفیگ‌های موجود در تب Configs و مرتب‌سازی آن‌ها براساس کمترین پینگ یا کشور اضافه شد.
• باگ‌های جزئی بخش SNI Config Maker برطرف شدند. اکنون کانفیگ‌های بیشتری از مخازن شناسایی، دریافت و پردازش می‌شوند.
• مشکل فعال‌نشدن دستی کانفیگ‌ها، به‌خصوص هنگام استفاده از Auto Mode، برطرف شد.
━━━━━━━━━━━━━━━━━━
لینک دریافت نسخه 1.0.6:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows/releases/tag/1.0.6
لینک گیت‌هاب پروژه:
https://github.com/Floxu1/UAC-SNI-Spoofer-Windows
t.me/UacSniSpoofer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/whitedns/1334" target="_blank">📅 00:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🌎
نسخه جدید WhiteVPN 1.1.0 منتشر شد!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/whitedns/1333" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1328">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">whitevpn-v1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">20.1 MB</div>
</div>
<a href="https://t.me/whitedns/1328" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/whitedns/1328" target="_blank">📅 17:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1327">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxw5z4dpqm3CvOFMVuKBmcZxD17CqwZ8HQoq2xzPUanO1uXAQGnIPEwyuSyN9fCaTLuakzPNATIzjnxNgfrZ6iMBuMNMyG0jkcbHD7VK5Y9cAeVZGeeCmFASEqIvILuT13VYM8eTN99tMB42bMEcRsFPkYze2ZOr2QW7oB4IZAEzJcL7TdHm3WDIQkctIGodA4gXmdt8Q2jCWb2aidIMLI9hkP0yeQiQ0AAgKFSCSZpZLj9kxfCdC99mf7waOtalSwqfQtjUIVD0wvyve92MQDN9LdRivrL4TFg77FAfrmKsBYRQP2lmxSmyyhYqzZJAOjL5ye8hlXzKXdOrTyAtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه جدید WhiteVPN 1.1.0 منتشر شد!
در این نسخه چند قابلیت کاربردی اضافه کردیم تا اتصال راحت‌تر، سریع‌تر و امن‌تر باشه:
🛡
اتصال همیشگی VPN
می‌تونید WhiteVPN رو طوری تنظیم کنید که همیشه فعال بمونه و در صورت قطع شدن، دوباره متصل بشه.
🔒
امکان Kill Switch
اگر VPN قطع بشه، اینترنت هم موقتاً متوقف می‌شه تا اطلاعات شما بدون محافظت منتقل نشه.
⚡️
قابلیت Real Delay Test
حالا می‌تونید تأخیر اتصال‌ها رو بررسی کنید، نتیجه‌ها رو ببینید و سریع‌ترین گزینه رو راحت‌تر انتخاب کنید.
✨
طراحی جدید صفحه اشتراک‌ها
صفحه اشتراک‌ها ساده‌تر، مرتب‌تر و خوش‌دست‌تر شده تا مدیریت و انتخاب اشتراک‌ها راحت‌تر باشه.
همین حالا WhiteVPN رو به نسخه 1.1.0 به‌روزرسانی کنید
🤍</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1327" target="_blank">📅 17:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1326">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tegxRq6gPARFAxfbZAL_fe0zH4PPvTTGI1UikQiBzipyoOgU81llk0HDlLdYfZFY3aGtmd1FEN7zzV8oztzpienObJfC0uOUTQ3LhUuE0Cyk8VubMJcTRW7MIUoFL_-oJINGBv46RCQ8llK-0e4t0_EgiusJsa4EneaMvzWfgCwnxzzUXYdltweYn8biCwN-B0ivQP8GHT2JGyySWyOI63UebI6eIfftRbzpk8t_QNtx6qlzscQbhSC9f401gsApcAi6ou0o_bFIO65a-VPSameKKv8K3JxF1wQLPBIB5BLzyRl8EUAaqNYgokPHe7BoKZLiL37MLM-Ay0WD0Adwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1326" target="_blank">📅 10:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1325">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-poll">
<h4>📊 از چه دستگاهی استفاده میکنید ؟</h4>
<ul>
<li>✓ اندروید</li>
<li>✓ اپل</li>
<li>✓ مک</li>
<li>✓ ویندوز</li>
<li>✓ لینوکس</li>
</ul>
</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/whitedns/1325" target="_blank">📅 13:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1324">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qdlsR4pwdllhx-zs59DdtUtV02EaHjAlQn1IfIFlI-FRj2TXm993aCyh10ewOWtKaMzjcns87VwVJC8yVUqgK4zSUmwCD6Xe2bx0acpru_eHW_exNvOIpNQKFhaD6yW2I1dlBVQdl-rcXcN5FoRaa0BlKZc98bE81PgiX1ItxTRaCTTuahm7zNi8cSI-eA4k_4-Zz0CGbcSIp4J9FZObAE61jcqFWGmTjwIOLsJwxwApPKiZq-kKvocmrXTgClnZOqRRjgLJOn7b7GwnEfBq6FM-MhcJm6G8PzUXHvd9MxZgmx-EsDJZSQAXnw5J6WbOYOtxOrDX5KONdwxIvdVDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/whitedns/1324" target="_blank">📅 13:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1323">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دوستان عزیز، اونایی که Aether واسشون وصل نمیشه، یه زحمت کوچیک بکشید:
📱
✈️
چند بار گوشی رو بگذارید روی حالت هواپیما و بردارید تا رنج IP‌تون عوض بشه.
🔄
اونایی هم که با وای‌فای و مودم متصلن، مودم رو ۱ تا ۲ دقیقه خاموش‌روشن کنن تا آی‌پیشون تغییر کنه.
🔌
⏳
اینم یادتون نره که ما تو ایرانیم؛ سیستم DPI و محدودیت‌ها روی هر سیم‌کارت با اون یکی فرق داره، چه برسه به منطقه به منطقه و شهر به شهر!
🇮🇷
🚫
اینجا خبری از اینترنت استیبلِ خارج نیست.
📉
اگه این کارا رو کردید و پروتکل‌های مختلف رو هم تست زدید و باز هم وصل نشد، یعنی اون کانفیگ کلاً روی خط و منطقه شما جواب نمیده.
🛑
یکی دو ساعت بعد دوباره امتحان کنید یا برید سراغ VPN‌های دیگه که با اپراتور و منطقه‌تون سازگارترن.
🚀
🌐</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/1323" target="_blank">📅 12:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-poll">
<h4>📊 با این لینک موفق شدید عضو بشید ؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ خیر</li>
</ul>
</div>
<div class="tg-text">عضویت در گروه whitedns  در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1322" target="_blank">📅 12:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1321" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gzv7xWzi_eM5Sa4G_IJ-tOBYvVEdG_XXx7iZzOB5MEWuILMtG2df38D7BItGquNoL-a00kfHyo6gbmVeQGByhr8Kom15E5Z9kR8XMVDK7ejvhnZPAkva8bK4HAEZ9ZcivwsVehzXFgEUQDIF2-A6x3V-hrtjQ4ao3vhvsf_IkBlFzwDt87uhjSR1mj0LOSEe3rBkBsoBMSkYvkpoEkG_0rXxd2yjYX27-yQnl6VnxPsPhlSgqI5MTZTFSK_HkdSuGGRdbt38E7p4B1fFi2vMAFnnnDEOq3SYE9SsacF3xgxdzHmKXEcRczG64TQGHLuVVPgjTpKcxSZIGnGcLt_4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضویت
در گروه whitedns
در گروه اختصاصی ما عضو شوید لطفا
🤝
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1320" target="_blank">📅 11:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.2-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1317" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Aether 1.2.2</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/whitedns/1317" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سلام دوستان عزیز.
راستش ما قبل از اینکه بخواهیم نسخهٔ جدید ۱.۲.۲ پروژه اِتر (Aether) را منتشر کنیم، ۱ روز گذشته را کاملاً درگیر تست، آزمون و خطا و چالش‌های فنی بودیم. خیلی از کاربران از ما خواسته بودند که قابلیت انتخاب کشور را اضافه کنیم و خودمان هم خیلی دوست داشتیم این کار را بکنیم؛ اما بعد از کلی کلنجار رفتن و تست‌های مختلف روی اپراتورهای مختلف، متوجه شدیم که با توجه به ماهیت فنی این کار، عملاً چنین چیزی نشدنی است.
برای همین تصمیم گرفتیم خیلی روراست و خودمانی با شما صحبت کنیم و بگوییم توی این مسیر آزمون و خطا به چه چیزهایی رسیدیم:
### ۱. چرا در پروژه اِتر (Aether) نمی‌شود کشور خاصی را انتخاب کرد؟
پروژه اِتر (Aether) سرور شخصی و اختصاصی ندارد و کارش این است که شما را به شبکهٔ عظیم WARP کلاودفلر (همان شبکهٔ معروف
1.1.1.1
) وصل کند.
بزرگ‌ترین مانع ما در تست‌ها یک مسئلهٔ فنی بود: آدرس‌های کلاودفلر از نوع Anycast هستند. انی‌کست یعنی چه؟ یعنی یک آدرس مشخص، هم‌زمان در صدها دیتاسنتر در سراسر دنیا فعال است.
یک مثال ساده بزنم؛ شمارهٔ ۱۲۵ آتش‌نشانی را در نظر بگیرید. شما هر جای ایران که باشید این شماره را بگیرید، به آتش‌نشانی شهر خودتان وصل می‌شوید، نه تهران یا یک شهر دیگر! حتی اگر عمداً بخواهید به آتش‌نشانی شیراز زنگ بزنید، باز هم شمارهٔ ۱۲۵ شما را به نزدیک‌ترین ایستگاهِ خودتان وصل می‌کند.
آدرس‌های WARP هم دقیقاً همین‌طور کار می‌کنند. پروژه اِتر (Aether) به هر آدرسی که وصل شود، در نهایت این سیستمِ مسیریابیِ اینترنتِ اپراتور شماست که تصمیم می‌گیرد ترافیک به کدام دیتاسنتر برود.
*   وقتی اوضاع اینترنت خوب باشد، معمولاً نزدیک‌ترین نقطه جواب می‌دهد.
*   وقتی مسیرهای بین‌المللی شلوغ یا خراب باشد، سیستم شما را می‌فرستد سمت آلمان (فرانکفورت)، آذربایجان (باکو)، ایتالیا (میلان) یا هر جای دیگر.
توی بررسی‌هایی که قبل از انتشار نسخهٔ جدید داشتیم، دیدیم وقتی مثلاً لوکیشن روی «اتریش» تنظیم می‌شد، پرچم اتریش نشان داده می‌شد، اما خروجی واقعی اینترنت کاربر یک کشور دیگر بود! در واقع آن منوی کشورها فقط یک برچسب تزیینی و قشنگ بود، نه یک انتخاب واقعی. ما هم چون دوست نداشتیم توی پروژه اِتر (Aether) ظاهرنمایی کنیم یا آمار دروغین به کاربر نشان بدهیم، کلاً حذفش کردیم تا همه‌چیز واقعی و شفاف باشد.
---
### ۲. چرا ویژگی «اتصال فقط به لوکیشن‌های غیر از ایران» را اضافه نکردیم؟
شاید باورتان نشود ولی ما این قابلیت را واقعاً کدنویسی کردیم و قبل از نهایی کردن نسخهٔ جدید، آن را زیر تست بردیم. اما خروجی کار روی اینترنت ایران اصلاً خوب نبود!
منطق کار این بود: پروژه اِتر (Aether) وصل شود، آی‌پی خروجی را چک کند، اگر ایران بود قطع کند و برود سراغ آدرس بعدی. اما مشکل بزرگ کجا بود؟
وقتی اپراتور شما مسیرهای خارجی را محدود یا فیلتر می‌کند، تقریباً تمام آدرس‌های کلاودفلر به دیتاسنترهای داخل ایران هدایت می‌شوند. در این حالت، پروژه اِتر (Aether) یکی‌یکی آدرس‌ها را تست می‌کرد، چون خروجی‌شان ایران بود قطع می‌کرد، سراغ بعدی می‌رفت و در نهایت بعد از کلی معطلی می‌گفت: «اتصال ناموفق». یعنی عملاً به‌جای یک اینترنتِ وصل‌شده (ولو با آی‌پی ایران)، شما کلاً قطع می‌شدید! درست مثل کسی که چون فقط سوار تاکسی سفید می‌شود، تا صبح گوشهٔ خیابان در سرما می‌ماند!
تازه یک مشکل دیگر هم هست؛ سرویس‌های تشخیص لوکیشنِ آی‌پی همیشه دقیق نیستند. خیلی وقت‌ها یک اتصال کاملاً سالم و خارجی را به اشتباه «ایران» تشخیص می‌دادند و پروژه بی‌دلیل آن را قطع می‌کرد. به همین خاطر در آزمون و خطاهای قبل از انتشار متوجه شدیم وجود این گزینه فقط باعث خرابی اتصال و اعصاب‌خردکنی کاربران می‌شود.
---
### ۳. پس الان پروژه اِتر (Aether) دقیقاً چه‌کار می‌کند؟
ما در این نسخه همه‌چیز را هوشمند کردیم. حالا هستهٔ پروژه اِتر (Aether) در چند ثانیه کل رنج‌های WARP را اسکن و پینگ می‌کند و به بهترین، سریع‌ترین و پایدارترین نقطه‌ای که در آن لحظه روی خط شما جواب بدهد وصل می‌شود؛ بدون قطع و وصلی‌های الکی.
البته اگر کاربر حرفه‌ای هستید و دوست دارید خودتان دستی همه‌چیز را تنظیم کنید، هنوز هم می‌توانید از بخش تنظیمات، اندپوینت دستی یا رنج آی‌پی دلخواه خودتان را وارد کنید.
یک نکتهٔ بسیار مهم برای آرامش خیال شما:
خیلی از کاربرها نگران هستند که اگر آی‌پی خروجی ایران باشد، امنیتشان به خطر می‌افتد. اصلاً این‌طور نیست! حتی وقتی نقطهٔ اتصال شما داخل ایران باشد، تمام ترافیک و داده‌های شما کاملاً رمزنگاری‌شده است. مقصد نهایی این ترافیک، شبکهٔ جهانی کلاودفلر است و هیچ‌کس در این مسیر نمی‌تواند اطلاعات شما را بخواند یا ببیند چه کار می‌کنید.
آن نقطهٔ ایران، فقط و فقط مثل یک «درِ ورودیِ» امن به اتوبانِ کلاودفلر است، نه جایی که اطلاعات شما در آن تخلیه شود. پس اصلاً نگران امنیت خود نباشید.
---
###
💡
حالا چطور آی‌پی خود را به خارج از ایران تغییر دهیم؟ (دو راهکار عملی)
اگر به هر دلیلی نیاز دارید که آی‌پی خروجی شما حتماً روی کشوری غیر از ایران قرار بگیرد، در حال حاضر دو تا راهکار کاملاً واقعی و تست‌شده برایتان داریم که می‌توانید از آن‌ها استفاده کنید:
*   راهکار اول (سوئیچ بین پروتکل‌ها): تنها راه طبیعی برای تغییر آی‌پی این است که داخل تنظیمات پروژه اِتر (Aether)، بین پروتکل‌های مختلف سوئیچ کنید. در این میان، پروتکل وارپ (WARP) بیشترین احتمال را دارد که شما را به یک سرور غیر از ایران متصل کند. این تغییر پروتکل باعث می‌شود روتینگ اینترنت شما عوض شده و در نهایت به یک دیتاسنتر خارجی هدایت شوید.
*   راهکار دوم (ترکیب با سایفون): شما می‌توانید از قابلیت «حالت پروکسی» (Proxy Mode) در پروژه اِتر (Aether) استفاده کنید و آن را با برنامه سایفون (Psiphon) زنجیره یا ترکیب کنید. با این روش، ترافیک شما از تونل پروژه اِتر (Aether) رد شده و در نهایت با آی‌پی خارجی سایفون خارج می‌شود که تضمین می‌کند آی‌پی شما به غیر از ایران تغییر خواهد کرد.
@whitedns</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/whitedns/1316" target="_blank">📅 10:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1315">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/c0mFaOcZuB3yk9AWpnuaNsG0lgrhtWKTiEu6-5boJW8TjeILl0vBHQgftFZvmJto9PP6mwu5jS9QL95-1ypPSLkmLsCW7F_hpP59o9XSsmXS7xmH_Y4v5yNK-kcvn3vfUYi6F7ATfG9rWg3uBrA8Ft8WT1Lf8fwhnEThgcNM2oT2eALzaAbbQeNSm3Ti9Dkiqdb30PGfJ95CXQGkOIEuA9qKZRy9yejTp_YnfHs9ayzIo4aUiliWqeOs5Q1UDyCRmFLgJxt-KnM3JuGYLshGPw-cQS_SxcW9psvZfM6fDW7awwUWS2c21BvmdQz6luzbgTB8ssMEYwG_s5ru6YPiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
تازه‌های نسخهٔ ۱.۲.۲ کلاینت موبایل Aether
🚀
یک به‌روزرسانی بزرگ و بنیادین با تمرکز بر امنیت حداکثری، کاهش شدید مصرف منابع سخت‌افزاری و ثبات اتصال منتشر شد! در ادامه خلاصه تغییرات این نسخه را برای شما آماده کرده‌ایم:
🔄
۱. مدیریت خودکار و ارتقای هسته (Core)
ارتقا به نسخه پایدار ۱.۴: هسته تانل داخلی برنامه به آخرین نسخه پایدار ارتقا یافت.
خودکارسازی در CI/CD: فرآیند همگام‌سازی و اعمال پچ‌های اختصاصی اسکن رنج به صورت کاملاً خودکار و هوشمند در خط‌لوله بیلد گیت‌هاب پیاده‌سازی شد تا از بروز کوچک‌ترین ناسازگاری یا خرابی در فایل‌های نهایی جلوگیری شود.
🗑
۲. حذف کامل سیستم به‌روزرسانی درون‌برنامه‌ای (ارتقای امنیت)
افزایش شفافیت و امنیت: بخش دانلود خودکار درون‌برنامه‌ای به همراه دسترسی‌های پرخطری مانند REQUEST_INSTALL_PACKAGES کاملاً حذف شد.
دلیل فنی: برای اطمینان از اصالت کدها و عدم نصب ناخواسته فایل از منابع ناشناس، از این پس تمامی آپدیت‌ها صرفاً به صورت رسمی و امضاشده فقط از صفحه ریلیس گیت‌هاب پروژه قابل دریافت خواهند بود.
🌐
۳. حذف لوکیشن‌های فیک و واگذاری اتصال به هسته هوشمند
حذف منوی انتخاب کشور: از آنجا که شبکه WARP کلاودفلر از آدرس‌های Anycast استفاده می‌کند، انتخاب لوکیشن در کلاینت عملاً تزئینی بود.
اتصال هوشمند واقعی: در این نسخه منوی لوکیشن حذف شده و وظیفه اسکن رنج‌ها و انتخاب بهترین و نزدیک‌ترین لبه ارتباطی (با کمترین پینگ و پایدارترین حالت) به صورت پویا به خود هسته برنامه واگذار شده است.
⚡️
۴. کاهش مصرف رم، پردازنده و بهینه‌سازی رابط کاربری (UI)
کاهش مصرف CPU در حالت آماده‌باش (Idle): تغییر ساختار مانیتورینگ اتصال از حالت Polling به حالت Blocking روی پروسه هسته که باعث می‌شود پردازنده گوشی در زمان اتصال بدون ترافیک، به خواب عمیق برود.
حل نشت حافظه (Memory Leak): محدود شدن حجم لاگ‌های ارتباطی به یک بافر حلقوی ۸۰۰ خطی (حداکثر ۵۱۲ کیلوبایت) جهت جلوگیری از مصرف بی‌رویه رم در اتصال‌های طولانی.
رابط کاربری روان‌تر و سریع‌تر: حذف انیمیشن سنگین شفق قطبی (Aurora) در پس‌زمینه و جایگزینی با رنگ ساده ساکن که بار پردازش گرافیکی گوشی را به صفر می‌رساند. همچنین منوی تنظیمات پیشرفته اکنون بدون کوچک‌ترین لگی فوراً باز می‌شود.
🔌
۵. رفع تداخل با v2rayNG و حل مشکل نصب (Over-Install)
تغییر پورت‌های پیش‌فرض: پورت‌های اشتراک‌گذاری شبکه محلی Aether به 10810/10811 تغییر یافت تا با پورت‌های پیش‌فرض v2rayNG تداخل نداشته باشند. همچنین سیستم شناسایی هوشمند ابزارهای موازی اضافه شده است.
حل دائمی مشکل امضای دیجیتال: گواهی امضای اندروید در بخش بیلد تثبیت شد؛ کاربران نسخه ۱.۲.۱ می‌توانند بدون نیاز به حذف برنامه قبلی، نسخه جدید ۱.۲.۲ را مستقیماً روی گوشی خود نصب کنند و تمام تنظیماتشان حفظ خواهد شد.
🔒
۶. ممیزی امنیتی ۱۰۰ درصدی خط‌به‌خط
کد منبع برنامه تحت ممیزی سخت‌گیرانه قرار گرفت و از نظر مواردی همچون اطلاعات هاردکدشده، نشت DNS/IPv6، ذخیره‌سازی محلی ناامن و ترافیک رمزنگاری‌نشده کاملاً پاک‌سازی شد.
📥
هم‌اکنون نسخه ۱.۲.۲ را به صورت رسمی و امضاشده دانلود کنید:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/1315" target="_blank">📅 10:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1314">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hermes-railway.txt</div>
  <div class="tg-doc-extra">168 B</div>
</div>
<a href="https://t.me/whitedns/1314" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">لینک‌های استفاده شده در ویدئوی بالا</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/whitedns/1314" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1313">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6g5T3lbaic9sHCND4bIeMxLf_s0iarJezCgyaLBpNlYB21a3fb6QRTSEswK4-UKlvBhodKME8g7a8UI4NGWs03YZoHMNftJ6xn23bW4MMI1dTJnqUw-xqMuHM77EYPdO1cwkytysPYeY_knnQLX9D6WYlsO7zy8FC8djit0ewEtN8By5ZYTIT5X4TWI-ncylJV-Z7y6ju8BEj1j9iQ1yYmo1kqPJfCYmRrACCkuktgmDA4T9UP504OTd1lipW5D2Ogivq-XeZfoHBRQ-Q74WEYu0nnATpY5KK83YQspDC8e4Bm421DxG7AYrITKqPt9ied8NmEPtLkoI0DGMCQONg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
هرمس رو با گوشی موبایل روی VPS رایگان و تلگرام اجرا کن! + آموزش بکاپ کامل از Hermes
⚡️
دستورات نصب استفاده شده در این ویدئو:
https://t.me/MatinSenPaii/4683
⭐️
توی این ویدئو:
1- بهتون یاد میدم چه شکلی با گوشی آیفون/اندروید/لپ‌تاپ، هم Hermes و هم 9Router رو به رایگان روی سرورهای Railway بالا بیارید.
2- وصلش می‌کنیم به تلگرام و از مدل Mimo رایگان روی OpenCode استفاده می‌کنیم و API 9Router رو ست می‌کنیم.
3- به طور کامل بهتون یاد میدم که چه شکلی می‌تونید از اکانت گیتهابتون استفاده کنید تا Hermes رو بهش وصل کنید و به راحتی، هر چند ساعت یک بار از تمام داده‌هاش برای شما بکاپ بگیره.
4- به علاوه روش ایرانیزه شده‌ی استفاده نامحدود از کردیت رایگان 5 دلاری Railway
😂
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره. از api و سرور رایگان هم استفاده شده توی کل ویدئو
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/whitedns/1313" target="_blank">📅 04:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1312">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سرور های اهدایی و فعال WhiteDNS پارت ۲ داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #11 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqIDIgICB0aHggdG8gQXJhc2toYXRhcmUiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiZGUuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjI0OWUzNDlhNDc2NjQyYTg4ZTQ2NDVmYTJiZjgwZjhjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #12 thx to Araskhatare
♥️
Location: Israel
🇮🇱
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4exICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlzLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI2MmIyNjQ0NzU5MjU4OWE0NmQ1MzdlY2M5NDc3MzY2NiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1312" target="_blank">📅 23:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1311">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">10 سرور اهدایی و فعال WhiteDNS داشته باشید برای زمان قطعی (کلیک کنید روش کپی میشه)
Server #1 thx to Coreforge
♥️
Location: Turkey
🇹🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7nwn4e3ICAgdGh4IHRvIENvcmVmb3JnZSIsInNlcnZlciI6eyJkb21haW4iOiJ2LmFub255bW91cy5vYnNlcnZlciIsImVuY3J5cHRpb25fa2V5IjoiYjI3NTAzOTE5OWIxYzhjOSIsImVuY3J5cHRpb25fbWV0aG9kIjozfX19
Server #2 thx to Araskhatare
♥️
Location: Germany
🇩🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6nwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiI5ZGIxNjYwMmM4Yzc3NjcxOWJhZDE3ZWZjOWQxM2E0NCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #3 thx to Araskhatare
♥️
Location: USA
🇺🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InYuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6ImVkMGNlZjE2YjcxNTNiOGQ4MzVhMzI3ODYxNTk3YzY0IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #4 thx to Araskhatare
♥️
Location: France
🇫🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6vwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImIuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiIyZjAyZTNiN2NiNTg3ZjM4M2U0MWM0MmU4ZWYzYWY2MSIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #5 thx to Araskhatare
♥️
Location: UK
🇬🇧
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6zwn4enICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImMuYXJhc2toYXRhcmUxLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkYmYwMmYyYWVmZmQzM2QyNDY0M2ViODM4OGY2N2Y0ZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #6 thx to Araskhatare
♥️
Location: Ireland
🇮🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImkuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjY0MTVlYjhmOTBmMWQ0NjY1N2JjZTljYjc5MTg2NDY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #7 thx to Araskhatare
♥️
Location: Sweden
🇸🇪
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh7jwn4eqICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6InEuYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjFkYjFiMWIyNGM2N2IxNzYwOTAzMmNjNDdhZmRhMzZlIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #8 thx to Araskhatare
♥️
Location: Spain
🇪🇸
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6rwn4e4ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Im4uYXJhc2toYXRhcmUuZ2dmZi5uZXQiLCJlbmNyeXB0aW9uX2tleSI6IjU4MTcyOTA4ZGFhNTAxZTk0MjUzNWU2NTY3NzkwM2ZkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
Server #9 thx to Araskhatare
♥️
Location: Italy
🇮🇹
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh67wn4e5ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6Imx5LmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJkMzM4NmM1MzkxZmRmOTJjMmNkODM3YmFkZTBhNGVjYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
Server #10 thx to Araskhatare
♥️
Location: Brazil
🇧🇷
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidC5tZVwvV2hpdGVETlMgIPCfh6fwn4e3ICAgdGh4IHRvIEFyYXNraGF0YXJlIiwic2VydmVyIjp7ImRvbWFpbiI6ImlsLmFyYXNraGF0YXJlLmdnZmYubmV0IiwiZW5jcnlwdGlvbl9rZXkiOiJmNzk4MDAyYzlkMTkxMTg4M2MzOTE2YTQ4ZTkzNTVkMiIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
آموزش استفاده از برنامه اندروید
👇
https://www.youtube.com/watch?v=tz8cj7HzHVI
آموزش استفاده از برنامه ios
👇
https://www.youtube.com/watch?v=filwdiPKN90
آموزش استفاده از برنامه ویندوز
👇
https://youtu.be/Mc--GlKw2wg
@whitedns</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/whitedns/1311" target="_blank">📅 22:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1307">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162866f874.mp4?token=c1pqteCld0h_RTLhDGcN_lblZslY_VBHVPPddPrl2bsjOT7mR4cRfvvgbznMAd4FfsIvn5OH-c6z-AbgqWT9N5kljjNLYPRwCBFl4hdZq4fSBJtrZjI_1_FN68shq-WPMvQ5dzyhzPJy-6QFVgTR1HpYpd6fqFGS5Z7XYClaD0qkeVmdbax-7bkiIPPLQi8mB4VAZSAH8HWzhYEDwFEZl5g8WuXPPXFytDRTEuGRYjgOQMb_yIum2WbREIAVyiwYBR_y8XT6_Y3LANHybb467Z7w4XMSPa8cEC1ZxL48g4pj2bCMcGveVMDy2xgik67Rhamwv6XNWUo29-sGNAUYlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162866f874.mp4?token=c1pqteCld0h_RTLhDGcN_lblZslY_VBHVPPddPrl2bsjOT7mR4cRfvvgbznMAd4FfsIvn5OH-c6z-AbgqWT9N5kljjNLYPRwCBFl4hdZq4fSBJtrZjI_1_FN68shq-WPMvQ5dzyhzPJy-6QFVgTR1HpYpd6fqFGS5Z7XYClaD0qkeVmdbax-7bkiIPPLQi8mB4VAZSAH8HWzhYEDwFEZl5g8WuXPPXFytDRTEuGRYjgOQMb_yIum2WbREIAVyiwYBR_y8XT6_Y3LANHybb467Z7w4XMSPa8cEC1ZxL48g4pj2bCMcGveVMDy2xgik67Rhamwv6XNWUo29-sGNAUYlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
آموزش وصل شدن به این روش شیر و خورشید در Mahsang دوستانی که بلد نیستند.
1-اول به داخل mahsang برید
2-سه خط سمت چپ رو بزنید
3-قسمت تنظیمات سایفون رو پیدا کنید
4-پروتوکل روی cdn fronting قرار بدید(دکمه ذخیره یا سیو رو بزنید حتما)
5-برگرید صفحه اصلی گزینه F رو بزنید
6-حالت فقط سایفون/only pisphon رو بزنید و دکمه کانکت و تمام
حالا شما رایگان و با سرعت بدون نیاز به پیدا کردن ip به اینترنت آزاد متصل میشید
🔛
لینک دانلود نسخه جدید
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/whitedns/1307" target="_blank">📅 07:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1304">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tEn1HqfaVeDgwbhHWdK6EzPirjcvv4hB5XcQbhalwB5urVDgPi_Isd79AUfG7I1vCBhjnHkBUlMmOX_wVRba45fnOG_R-VVpdi4iQtEzqpX2f1UZoOEuu6tdbcyU45MQh2pZN5Ll4-ul5PaTO_HvvMwgr6MLzqPZy4lYiqGV7o4uwR4_OFZH3YQ8vGEMBiwVMunuuR1eme3HuK0V8p2GIvSyXW5YGkEqEyVXN3b0U2SW8Jk-cPpWPxejA0MXVYmbuVSpbCo4YGOTTelXKFr8FvLwHwBlyeZdvS8uI5cBvyuZgkaES_noOCYI4JTyRdPAz_U9t7iyd9v4LTA7DJM6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!
هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده.
منم یه مشارکت کوچولویی روی خود هسته داشتم.
تغییرات اصلی این آپدیت:
1-
امنیت در پروتکل MASQUE:
قبلاً وقتی وصل می‌شدید، کلاینت هیچ تاییدیه‌ای از سرور نمی‌گرفت و اگر کسی وسط راه سعی می‌کرد با یه سرتیفیکیت فیک گولتون بزنه، برنامه متوجه نمی‌شد. اما الان اتصالات MASQUE سرتیفیکیت سرورهای کلادفلر رو به صورت دقیق (از طریق هش‌های SPKI) بررسی می‌کنن تا دیگه کسی نتونه ترافیک رو شنود کنه.
2-
پایداری WireGuard و Gool:
قبلاً بعضی وقتا برنامه بهتون می‌گفت متصل شدید، در حالی که دیتا اصلاً ردوبدل نمی‌شد و فقط روی یه پروکسی SOCKS5 گیر کرده بود. اما الان یه سیستم بررسی سلامت (Health Check) مداوم داره که اگر دیتایی از سمت سرور برنگرده، خودش به صورت اتوماتیک اتصال رو قطع و دوباره وصل می‌کنه.
3-
اتصال مجدد خودکار در Gool:
تو نسخه‌های قبل اگه تونل بیرونی Gool قطع می‌شد، کل فرآیند کِرَش می‌کرد و خارج می‌شد. الان Gool هم مثل بقیه پروتکل‌ها خودش هوشمندانه دوباره ریکانکت می‌کنه.
4-
فیکس شدن نشت مموری (Memory Leak):
یه باگ رو اعصاب بود که وقتی اتصالتون زیاد قطع و وصل می‌شد، تسک‌های قدیمی تو بک‌گراند باز می‌موندن و آروم‌آروم رمِ سیستم پر می‌شد. این مشکل تو تمام پروتکل‌ها کامل برطرف شد.
5-
هوشمندی در مصرف منابع:
از این به بعد Aether همون اول کار، تعداد هسته‌های CPU و مقدار رم سیستمتون رو می‌خونه و میزان اسکن همزمان (Concurrency)، بافرهای شبکه و صف‌های داخلیش رو بر همون اساس تنظیم می‌کنه. این قابلیت برای کسایی که می‌خوان ابزار رو روی روترها و بردهای ضعیف‌تر بالا بیارن فوق‌العاده‌ست.
لینک گیت‌هاب برای دانلود(نسخه‌های مک، لینوکس و ویندوز):
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.6.0
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/whitedns/1304" target="_blank">📅 05:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📱
آموزش کامل اپلیکیشن WhiteDNS منتشر شد
سلام به همه دوستان عزیز
یک ویدیوی آموزشی کامل برای استفاده از اپلیکیشن WhiteDNS آماده کرده‌ایم. در این ویدیو، تمام مراحل از نصب و راه‌اندازی اولیه تا اتصال و استفاده صحیح از برنامه، قدم‌به‌قدم توضیح داده شده است.
در این آموزش با موارد زیر آشنا می‌شوید:
• نصب و راه‌اندازی اولیه WhiteDNS
• اضافه‌کردن و مدیریت Resolverها
• اسکن و پیدا کردن Resolverهای معتبر
• تفاوت حالت پروکسی با VPN کامل
• نحوه اتصال از طریق DNS Tunnel
• مشاهده وضعیت اتصال و میزان مصرف ترافیک
• مدیریت پروفایل‌ها و تنظیمات برنامه
• نکات مهم برای داشتن اتصال پایدارتر
https://www.youtube.com/watch?v=tz8cj7HzHVI</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/whitedns/1299" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/fedn4QIJFdnEQkKzGfaqBE3tfN03PO6N5F83y2l7CKH_yRC0vHN6-Lj0uGUelaJEww3qcCOhmyKDZLR4-GBuDh-TwhkbVEZ_Fz3eyn8YWpdb6G2tfq9cjceBQAdu2wxf5MxF5ObSCPQB-hY1T7lldy9iBmGpCkNfVySinU3IMabWEgIIvOrwzA9kLaJtYkGSaLvvW7N2W3MniYDNFWeNbPqqkroaZwU0iLWbg8cziCV7T4wUt7AU4CyZ_xPmpvfwimrBVrpMd7n3I7m0jOYSZKudh9s9udQ0j3UVoZo936qXkfn-xfoeGF_JsETTIo_1_OExSCunuo8VEiv_Ubkx2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/whitedns/1298" target="_blank">📅 18:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Ws6mieYMJ3uRO0j5-Obtbw8ZZpcFBPKbOzBlyInESm8XgDK3vHAsXYDt9Mv8cAH9vTEpDOON1iReThtC1xT2vNaqTErKTS9BMLTC2oI4AVZw0mdsmakGbYnCKuAbv5xUBNnCj-vnvBNjY4k96ZLUVkbm8qzZn1USEkpwb3KkTPiCgwXDNE53R-TzBBCl3auEfocXv4AFOr-DllVrhtTXqmj1bmMLfxGdxRQ4TUVgkHuwUVAjH9eFQEPDyZrW3OxhEaLTr5V-RbuA4Iq5HNc_EEnrf1KsfPJ8j05VyvII7lGKez--32kf1gJa90TiTFRfoIsJ8VcIniZnb98cTxu1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/whitedns/1297" target="_blank">📅 18:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1294">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.1-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
نسخه قبلی رو حذف کنید بعد نسخه جدید نصب کنید
⚠️
⚠️
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/whitedns/1294" target="_blank">📅 16:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1293">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/m-JhSk3kWWO7wo0OuKzphnFcfhv_EHvXEYYDXP3MPGYnxpvvVmnLYluT6xxmY-8ICL77UugHJfrRpdZZJDyPoDNYKuoq0mfZqC9R8SWRi5_oD71BQJopi_vuB54ODFFkzA-X8_OwBfGMqc54mj7BjWZB7t82NDdPO_Jym3e5wQlQSqzW8CpzOcYNy7UGPfWIVcwQuzFOEDongaFBpUo22AoIOx0zCQMtfvRsIWr611Prp_oF1Wo5awaYRCxCsJPkVnQHTp2keEmAcZ98U2_TzVyDp4WfFC39LLAUwZK9xWhI2p6spf2ih7GSol5ltsgqb4rCIdZ432tHjv6h_o2b6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
نسخهٔ جدید Aether منتشر شد! (v1.2.1)
🎉
اگر به دنبال یک اتصال واقعاً پایدار، فوق‌العاده سریع و بدون نیاز به برنامه‌های جانبی (مثل v2rayNG) هستید، نسخهٔ جدید اِتِر موبایل با قابلیت‌های شگفت‌انگیز برای عبور از سخت‌ترین فیلترینگ‌ها آماده شده است!
🔥
تازه‌های بی‌نظیر در نسخهٔ ۱.۲.۱:
⚡️
موتور هوشمند واقعی (Smart Auto):
برنامه مانند یک مهندس شبکهٔ حرفه‌ای، ابتدا DPI شبکه و وضعیت اختلال‌ها (مانند فیلترینگ SNI یا خفه‌کردن UDP) را تحلیل می‌کند و سپس بهترین چیدمانِ اولویت‌بندی شده از پروتکل‌ها، سطح مبهم‌سازی (Noize)، فرگمنت و رنج‌های آی‌پی را برای اتصال گام‌به‌گام و کاملاً پایدار اعمال می‌کند.
🟢
«متصل» یعنی اتصال واقعی!
دیگر خبری از کلمهٔ «متصل» فیک که هیچ سایتی را باز نمی‌کند نیست! برنامه تا زمان دریافت هر ۴ تیک سبز سلامت (پورت، هندشیک، اینترنت و آی‌پی) در وضعیت بررسی می‌ماند تا از اینترنت واقعی مطمئن شود.
🛰
نمایش آنی آی‌پی و پرچم:
با موازی‌سازی سرویس‌های تست سلامت و تشخیص IP، این فرآیند با سرعت بسیار بیشتری انجام شده و بلافاصله وضعیت موقعیت جدید شما نمایش داده می‌شود.
🔄
آپدیت آسان و مستقیم (مشابه تلگرام - آزمایشی):
از این پس برای دریافت آپدیت‌ها نیازی به سر زدن به گیت‌هاب ندارید؛ نسخهٔ جدید مستقیماً درون برنامه به شما اطلاع داده شده و با یک کلیک دانلود و نصب می‌شود.
🛠
رفع ریشه‌ای تداخل‌های متنی زبان فارسی:
به‌هم‌ریختگی ظاهری و راست‌به‌چپ اعداد در فیلدهای حساسی مانند ip:port و اندپوینت‌های دستی کاملاً برطرف شده است.
🔒
امنیت بسیار سخت‌گیرانه‌تر:
تأیید نام هاست در اتصال‌های TLS (بستن راه حملات MitM)، حذف لاگ‌های موتور در نسخهٔ نهایی و مسدودسازی ترافیک ناامن HTTP برای محافظت حداکثری از اطلاعات شما.
🧹
دکمهٔ بازنشانی سریع تنظیمات:
با تنها یک لمس، تمام تنظیمات پیشرفته را به مقادیر پیش‌فرض بازگردانید.
لینک ریپو :
🔥
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/1293" target="_blank">📅 16:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1291">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdqlIGzwWKET7S1vBVUb13j0jmXeBE_WebNWdsnrzrZ1v3HXQtDZKxaj5JR7Y_OVmn5xSQsvvqI1MVdpdp0Ec0OaCP5MVHumh3W1XfeBD0eR9ZWmN5hVLMKkZylXtb2I55_rCcoLUOSy8HrDplbLrDKWHkvYl7SFLpr1XMztQDuTgV349L58pRgS_TIQbhAeLv4uwnEh5JUVyNdArR09i7IWsBG0O6oCtm3CMwAEh86o3SGQgTiZBe4LqhJb6Um9mOWHCQ4cG9LLi7T3fRGUoO-nMAYDE6lUVUjjDnmFa0TW2N3Qc_g5xIXlK-GSfDii97lubNf7hEwQbSL5bUV7dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/whitedns/1291" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1289">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنوا | Nova</strong></div>
<div class="tg-text">🤖
ساخت پنل نوا پروکسی فقط با ربات تلگرام!
دیگه لازم نیست مراحل نصب رو دستی انجام بدین.
😎
فقط وارد ربات نوا پروکسی بشین، اکانت Cloudflare بسازین، توکن رو دریافت کنین و چند ثانیه بعد پنل اختصاصی خودتون آماده‌ست.
🚀
بعد از ورود به پنل هم فقط کافیه رمز ادمین رو تنظیم کنین، کانفیگ رو داخل کلاینت Import کنین و از اینترنت آزاد استفاده کنین.
📺
آموزش کامل مراحل داخل ویدیو گفته شده.
💬
اگر سوالی داشتین، داخل کامنت‌ها بپرسین.
🔹
ربات تلگرام:
@IRNovaProxy_Bot
🔹
وب‌سایت:
https://novaproxy.online</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/whitedns/1289" target="_blank">📅 09:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1288">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard  https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1288" target="_blank">📅 04:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1287">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1287" target="_blank">📅 04:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1285">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYaego66N5LwEugiam0BNM62eetXeXMtsJVlmslqyJtPnh07ayN1QwsqYBYHK36jEj_mAeOd2WJ5nLJvajU9Z_Vr1z5Nax-MI2x4tbzlB_-pkcCWvo8yVNRKeX_q_ajYCv2xOr27C04i_dJyXB3cVc3MFTVDHhiXCaShru8YHaVHpNSzXB2l7nyWlJxySmXUEBhO2WIEDcP1A7qpEXnHVOxp8Iqi_Ke-SaY2UZ61SDyYzLJCCecord5qd6uMHShj0KSOYFBhPFWN23k6oW0HPNr31wPfrK45AbS0u_2BZ8bRueCQxss_abwkL_N1euClCakXvkc4HeyUvtOcopdGhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/whitedns/1285" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1283">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یک ظرفیت جدید برای تست فلایت داریم که میتونید از لینک زیر استفاده کنید
🚀
📱
اپ  CoreForge  یک فیلترشکن ساده و قدرتمند برای iOS / آیفون که مخصوص استفاده در شرایط سخت، اختلال شدید اینترنت، اینترنت ملی و حتی دوران قطعی کامل طراحی شده.
https://testflight.apple.com/join/3htm1Whc
آموزش
🎥
📹
:
https://www.youtube.com/watch?v=filwdiPKN90
@whitedns
📢
🔗</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1283" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1282">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/prT7d0q0-GE0tPcLlZWDq1iUnk0619jukIMWPfI5Sz16m3OeYFxVebZ2Rs72oShKv5ewHGlakGJeN-TJz3LBmLGaH5duU0MCa_-NPxT2IXg6LO3bVxkEMmra4MHzrrFTMaQPXN-mJsuHn7npG0C8MvkPnXhjoL42zf3hg-uNHG4aEVZ7agP4zvjaVbm2Menei3epDmximmh4IQb1i-vYKlrIheTqQnX-CLszlpFZE5rjO8L9AhM9lfKdD9Ayembt1uIuQfOowlcXXrntrWou0JyLUPddERubWrsRtMfuVmqmeNt2b7AYy0X6OXvX1QJZ4sID_dio3jnyAYPzc-3zsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/whitedns/1282" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1281">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jUNXtFBYKPz7JEFBvt5U2m9AdvZgWsVpKcg-62GOv4AE6oyJ24ke8_PKUTmSABKpZ9nOwSfq5pQfcRcwoMzQ9ekH1GuGcegmeCLlZNeVS8hBhVKN9U5NlnglWYnlw-mI3H-ebzFZejtlN58YdULxj1Y4B1MIFqsrlZLhBGvQnkPKTRIAQ4UiwONy-JZAWDh2y21EWDNqcKPGKvRILske7_C-A7p8CVoCaB9SHaWDI7hBxo34ZFwWUAR13Vugc8nmdDtB7IuERBTFalScbzNVvQ2SfAt0pTkzMNZtnpQvOXDbkXFLaDB6ea0qj7hKZSkvK4NOLhPp4qkK1y3kBUBBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/whitedns/1281" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1280">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Klpst6xHSO1on-AUuWjuCUu7GfQ8NzONnp83mMmUrf2mzRvjlRCYGeMfPJuIpcUoxbuZGl5pDegKfrAP7Pj5wVj6jxWtJo6UyItJdy2xvVXM_u9t27O9zD2OZfRz_FM612sAWkGa5ccNANeeJn1ZprauJDS6Fi0GuiVw9OXFwOTxch1b7F8RXVQX2LwzYpgqda7OH6nTTrtOKIhYPyd0cpOAs-GyeMdlpiAMzeOTqYTKOgn2cIXsh9Z6lUK1Z-6VMZWkvgj8akZFMJG8mk9ko7Fj5ZohFfjUBBojeOEsbgLsKADSBZv-Mo1pzT4wdNlJcTLo3_pjZXcPDD9x5FxxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1280" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1278" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/whitedns/1278" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/WRCI6os3DBKpMW265ejOS57BR0ZMSS9Oh2izz_OWknr2Ib3VLXcN5N72m9eTjvQNMJP-sFTwM4M9jVirkSdA-Z7mgMfyKJUzJOOFmugxGmVPLNRCuz56uwN9-QDxhXgaBepA7y_ucHqWLrYQ-tWXaKF2twXU50ihOQ3Fm5YAyvSgnFC128rhhzIkX_Z7JyHqPcdldi415o9DyBtoXrWm1f7J5oFDyB7bz_5wUxophtoZAsFCsklzPymjwhlmmthq881wqIyIIHDWsBMnlKyHTYEz6-gpRvnBABtbUOUkL70CFlc5oHje_33zvLlaEFBBzDPh1r7-DLuTOwET0uJecw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/whitedns/1277" target="_blank">📅 12:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📌
چند نکته مهم برای عملکرد درست برنامه‌:
1️⃣
حتماً فایل PDF راهنما رو بخونید
تا برنامه بدون مشکل براتون کار کنه.
2️⃣
وقتی متصل میشید، صبور باشید تا
آی‌پی و پرچم کشور
روی صفحه ظاهر بشه.
3️⃣
دوستانی که میگن آی‌پی ایران می‌گیرن و سایت‌های هوش مصنوعی باز نمیشه:
• یا چند بار قطع و وصل کنید تا آی‌پی غیرایران بیفته؛
• یا از قابلیت جدید
حالت پروکسی (Proxy Mode)
استفاده کنید و اون رو با سایفون ترکیب کنید. این‌طوری هم سرعتتون عالی میشه و هم مشکل هوش مصنوعی کلاً حل میشه.
💡
*نکته:* ترجیحاً نسخه
مودشده سایفون
رو نصب کنید تا محدودیت سرعت نداشته باشید.
https://t.me/whitedns/1261</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1276" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcdW-UWgRJ5cZmKD2kbQRXDIbl3l-hdg6NUT8gQZXoygHBYgFIf0EeyE2D9smgHx3TKDIXgIFOaaI_G9Ijy8FFK-dlrR8NYvToMtv_KK1eeMf9taLz5Ps991chEnVSdrCQPuWnbtHrSFV_k7t_M9Heq3xi-yCN9Cdr7O-rCFTn1hhPV3cD1KVN2bSHIhRE_fu7QyOc1cO8WVqH1pL9FVkUTHwwfgQHs3u4V6Ft3JdlBtmjE4sggh5iXG_52SvLYh_zfMV2gJoygq563z6HFs0yYsde8-RUycGFWlT3VB6Ayt1ntCw-z8uYYjYNO3LebWh_-ykGuw-a7lPSHvnqv_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/whitedns/1275" target="_blank">📅 06:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/whitedns/1274" target="_blank">📅 05:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1273" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1268">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1268" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/whitedns/1268" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1267">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCO_Ae2JPQeet2r-Fk9viCDTNDTGsWC8lMESHp5GZ9NoNeNO7gGXHWKmfySQinjjayrle8WvZS7Sd6OYius9Ydj4iDRlNBNW6A2asGijKJf2d7UqTW2ls-mA166VCYVYzg-0uIIFqZ0sY1ox4wWxLqW4KNBxN333Ge-kCyWhA1Kizl4HThcimWXmB7xxnIQiWtYaDQMnIvqUqBsnIG1CmShwHIjpP6KOKoew7Ow5BNDbhC8j9AGYTozfEpMUHQFj-Z6sqa3UrTRQjyh-RHaYh79uhecbMw016ydELbLRdvpGiuHpH5XTzG54hxILkZbEIRUg_WvmJ0Y9qVMFx13mAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/whitedns/1267" target="_blank">📅 05:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1266">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اگر توی نصب مشکل دارید نسخه قبل را پاک کنید و این نسخه را نصب کنید</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/whitedns/1266" target="_blank">📅 05:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.3 MB</div>
</div>
<a href="https://t.me/whitedns/1262" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/1262" target="_blank">📅 05:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1261">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ma08Hyu7j-zOxoztejhOwFry2G_1B2prVbeRWyR0pGr3xZWHY0Oj6nuzuC_LpeLy7I9ThgziU6Px-VGZnsMgpUwY6l-Iv6Kg_ogpbfDRHBq8CIm5jX3k6gOxxMyloOduWl9c31fwgEonEPciyR7L8HSucW1GnuvPPJKKLCBfgrbHbzlnRIszslyJTCf4pnX1Fm-kHQ_N7HzrnU-cw6NplYTiD3XBajl5Ox-59LsA7nQ3NnOst1OCTe6SSZtL_VT0v7Jh3M-E0iRfE00mKXvwI2Zlb63eIRk8PBRBuWW_6TJfSyGFq4_8LW3x5eAqrncCafvesrPkKYDP7F1Kkuna7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Aether
1.2.0
🌐
✨
(فقط برای اندروید )
آتر یک ابزار ساده برای اتصال امن و عبور از محدودیت‌های اینترنت است. برنامه به‌صورت خودکار سرورهای سالم WARP را پیدا کرده و یک اتصال رمزنگاری‌شده ایجاد می‌کند؛ بدون نیاز به خرید یا واردکردن کانفیگ.
🔒
🚀
📱
روش استفاده:
1️⃣
اینترنت را روشن و برنامه را باز کنید.
2️⃣
تنظیمات را روی حالت خودکار بگذارید.
⚙️
3️⃣
دکمه بزرگ وسط صفحه را بزنید و درخواست VPN را تأیید کنید.
📲
✅
تمام! بعد از نمایش
Connected
می‌توانید از اینترنت استفاده کنید.
🌍
🎉
مهم :
⚠️
برنامه روی حالت اتوماتیک اول اسکن میکنه و ممکن هست بسته به وضعیت اپراتور شما و فیلترینگ حتی تا چند دقیقه طول بکشه. پس صبور باشید و به برنامه وقت بدید.
⏳
💤
یک فایل PDF با توضیحات دقیق در مورد کارکرد و نحوه راه اندازی براتون گذاشتیم . کامل بخونید لطفا
⚠️
https://t.me/whitedns/1265
کد پروژه :
https://github.com/QW-AI-Code/Aether/
@whitedns</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/whitedns/1261" target="_blank">📅 05:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfQEHPUuE1fm5X1I7YFTFYCuZSCUUH8EkkffiDnR30eB68vurnh8htKnfqoW-ZXY74VMHRkz-g12n80VXHTZrAKhwP7U0qz_Z3RiR8MMrwAFgZu_vFgF4XCGECMLAKr3fgKBfmewqHmQs97yGEyw3ygs3dAuG4UMmwu1m4t0xfJ3Z2EL5t46ZNQbl8wvtdLuedeVjyZJYl0AmudlCtKjE4nJras-Bbtu2wcWJGw_Aon3DVNvWZdV46R9s7FbPyEkHZrhTiR0raNIBnLs4O3NUZYU9RzkmZ-ftIZtp52jQacOsBKmMOs9jWikwhdjOYBH8Hbbp9iseERGOx9ZV05BqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین سرور اختصاصی برای اپ WhiteDNS
🌐
Tunnel domain:
v.anonymous.observer
🖥
IP:
78.135.93.50
🔐
Encryption method: 3
روش رمزنگاری را روی AES-128-GCM تنظیم کنید.
🔑
Encryption key:
b275039199b1c8c9
➖
➖
➖
➖
➖
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/whitedns/1259" target="_blank">📅 01:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-1258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📹
آموزش ساخت فیلترشکن رایگان با BPB Wizard
https://youtu.be/vmazT67nRs0</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/whitedns/1258" target="_blank">📅 15:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👆
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/whitedns/1257" target="_blank">📅 14:04 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1252">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">20 MB</div>
</div>
<a href="https://t.me/whitedns/1252" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/whitedns/1252" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1251">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHSHPhIC15jldaD3PL3UYnt1chjguApk-Dv0sAfQR6-lUJ9D3NDW7eYkPed6y2QaB90CxxqQ99kwAS5zufkugWQWk6f9AnHdsQSkPhuWzmVLZDUriUTBUTzu7z5yeKWIuWn9FjEaBKbPO_FgA0fnhEqGVT27zqgpI5bdIblFV94gCGjVCTKorWXcUZyWaW3A-qr8SdPKmvsBXCD1VVVbUTZlTrdjT4-CYyXd3UCFh0wDLQZmpUmsskhI0NSwWkAlV3JxZCDQDJ0DWGfsVtaZ6bIaTOjAxvTY0BV5KC7i-jLavkOl7LtCpZHZ4um7A1Lwo45rghHhJ0rIpkqdLI3O4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍️
انتشار نسخه ۱.۰.۰ اپلیکیشن WhiteVPN
• پشتیبانی از فارسی و انگلیسی
• انتخاب پوسته روشن، تاریک یا هماهنگ با دستگاه
• ارتقای هسته Mihomo به نسخه v1.19.29
• مدیریت بهتر سابسکریپشن‌ها و کانفیگ‌های دستی
• پشتیبانی بهتر از WireGuard، WARP Pro و Amnezia Noise
• بهبود اتصال روی Wi‑Fi و شبکه‌های محدود
• بررسی واقعی سلامت اتصال و استفاده خودکار از Clean IP
• تنظیمات پیشرفته شامل TLS Integrity، DNS رمزنگاری‌شده، Split Tunneling و IP Fronting
این بهینه شده تا با ورژن جدید BPB  به خوبی کار کنه.
برای استفاده از اپ، سابسکریپشن های Mihomo را از پلن BPB داخل اپ وارد کنید.</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/whitedns/1251" target="_blank">📅 14:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1250">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آموزش آماده شد اما تا ادیت میکنیم، ورژن جدید WhiteVPN رو ریلیز کنیم چون آموزش رو با کمک اون ساختیم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/whitedns/1250" target="_blank">📅 13:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1249">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">همراه با فیلم آموزشی، درحال آپدیت کردن هسته WhiteVPN و اضافه کردن بهترین پشتیبانی ممکن از آپدیت جدید BPB  هستیم تا اتصال شما ساده تر و پایدار تر بشه.
نامگذازی اپ هامون هم داره کم کم تغییر میکنه تا کمتر گیج کننده باشه براتون
به مرور زمان همه اپ ها تغییر میکنند به نام های زیر:
WhiteDNS
WhiteVPN
WhiteScanner
WhiteBPB</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/whitedns/1249" target="_blank">📅 08:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1246">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">White DNS
pinned «
جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟
🔥
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1246" target="_blank">📅 16:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1245">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-poll">
<h4>📊 جلسه پرسش و پاسخ توی همین تلگرام به صورت انلاین بگذاریم  ؟🔥</h4>
<ul>
<li>✓ بله❤️</li>
<li>✓ خیر🫤</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/whitedns/1245" target="_blank">📅 16:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1244">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/We8RtpGp9J3LPfedFbcCxUiRPJN3Fp5HiakrBdDWjSE6fpSsE9hq8d6x7w1AFJg6GN4qkSy9a_-Y_9fz5WyB_RheKSJTfTCf5QOKMf_FdZIGd6KIizEylLy8hlrs4P-eU_MVm-RTShKKULJY_ePfm_Y9Ce9U9GHbav14KpLdo1fvUB4qFqft4wWtnmXqH6aXPEx2dxIGMpKLAm2WMRzeT8XZ2zNjjkxHUTZxY3y3IcA5pfsKfYucgu-hDsVpUaKjzSTX8uZPa0fqex0nGJ5wrnFooYCMtr5OVkwSXAitengc5X7eS6QgPVsB_G2kOBVOAgkSaxmIn8_DytAX9t9tdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ و انقلابی BPB Worker Panel (نسل جدید - نسخه 5.1.1)
🎉
نسخه جدید و کاملاً بازطراحی‌شده پنل BPB با امکانات بی‌نظیر و تغییرات ساختاری عظیم منتشر شد! در این آپدیت، مدیریت پنل و سرورها بسیار یکپارچه‌تر، امن‌تر و بی‌نیاز از درگیری با داشبورد کلودفلر شده است.
✨
مهم‌ترین ویژگی‌ها و تغییرات این نسخه:
🔹
نصب سریع با One-Click Wizard:
دیپلوی پنل حالا فقط از طریق ویزارد آنلاین و اختصاصی انجام می‌شود و پس از نصب، یک لینک کاملاً پرایوت به شما می‌دهد (روش‌های نصب دستی روی این نسخه کار نمی‌کنند).
🔹
داشبورد مدیریت داخلی (Admin Dashboard):
امکان آپدیت پنل به نسخه‌های جدید، حذف کامل پنل، و ریست پسورد مستقیماً از داخل خود پنل اضافه شده است.
🔹
راه‌اندازی ربات تلگرام:
مدیریت کانفیگ‌های تکی، دریافت لینک‌های سابسکریپشن و مانیتورینگ مصرف (همراه با هشدار مصرف بالای ۸۰٪) از طریق ربات تلگرام.
🔹
حذف کامل Environment Variableها:
تمام متغیرهای ثابت (مثل VLESS UUID، Trojan Pass، Proxy IPs و...) از داشبورد کلودفلر حذف شده و مستقیماً داخل پنل قابل آپدیت و مدیریت هستند.
🔹
ارتقای چشمگیر امنیت:
لاگین به پنل حالا نیازمند ایمیل کلودفلر شماست.
مسیر ورود به پنل به یک آدرس تصادفی و امن (Secure Path) تغییر یافته (دیگر با زدن
/panel
وارد نخواهید شد).
🔹
تنظیم سریع Custom Domain:
دامنه‌های سفارشی خود را می‌توانید مستقیماً از بخش Common settings وارد کنید تا کانفیگ‌های مربوطه با تگ
D
به سابسکریپشن شما اضافه شوند.
🔹
قابلیت‌های جدید شبکه و پروکسی:
پشتیبانی از Xhttp و VLESS Encryption برای Chain Proxy در هسته‌های Xray و Clash.
🔹
انتقال آسان تنظیمات:
اضافه شدن قابلیت جذاب به‌روزرسانی و همگام‌سازی تنظیمات از یک پنل ریموت BPB دیگر.
⚠️
نکات بسیار مهم برای اتصال کلاینت‌ها:
حتماً کلاینت‌های خود را به آخرین نسخه آپدیت کنید (حداقل Sing-box نسخه 1.12.0 و v2rayNG نسخه 2.2.3 به بالا).
برای اتصال پایدار در v2rayNG، حتماً گزینه
Hev TUN
را فعال کنید.
در صورت مشکل با فرگمنت در برخی ISPها، حالت
Packet
را روی
1-1
تنظیم کنید.
لینک ریپو :
https://github.com/bia-pain-bache/BPB-Worker-Panel/releases
لینک ویزارد :
https://wizard.bpb-panel.workers.dev/
@whitedns</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/whitedns/1244" target="_blank">📅 12:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1239" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/whitedns/1239" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnW0goX8lKOYqvvvbOwlWPj81vVuQP39i4lsAGIcqCF8d2sxZSNgWMx2VgjfDUpGr3rPj18iWgSnHKPSLAFQeNsfwuZDGraIx8RNKKRGYihg1S10h27r4DbJDXx99SeLRiz27WX4eHyePa9wxUQaPnIxoskIUOnj57J3mrgmQ016uKgobNWpI3IhfLz3mKvVbAQv53-MByGzsFc1M4Ft09x59yRZ1XVf-K0xexw-KNaDgt99qFIEEiEJGOzeLYzr-Y6N45GPngIvENrQf6GlnRaKwKUUKvBZM23-N5wN0wq8jA22Ns3vZYrZ8u_loJjZ34xluxTa7D2DspCx_zaKlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/whitedns/1238" target="_blank">📅 12:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1235">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Aether-1.1.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">14.2 MB</div>
</div>
<a href="https://t.me/whitedns/1235" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تازه‌های نسخه ۱.۱.۰
🆕
اِتِر (Aether)
تایل تنظیمات سریع (Quick Settings)
— روشن/خاموش کردن VPN مستقیم از منوی بالای گوشی، بدون باز کردن برنامه. یک بار اضافه‌اش کنید: منو را پایین بکشید ← دکمه مداد/ویرایش ← تایل
اِتِر
را بکشید داخل.
اشتراک‌گذاری VPN با لپ‌تاپ یا گوشی دیگر
📱
💻
— از منوی کناری ←
اشتراک‌گذاری VPN
. گوشی شما یک پراکسی
HTTP (پورت 8118)
و یک پراکسی
SOCKS5 (پورت 1080)
روی وای‌فای/هات‌اسپات باز می‌کند. آدرس دقیق
ip:port
قابل کپی است و کافی‌است در تنظیمات پراکسی سیستم دستگاه دیگر وارد شود.
تنظیمات پیشرفته در صفحه اصلی
⚙️
— دکمه جدید بالا–راست صفحه، پروتکل، حالت اسکن، نسخه IP و بقیه تنظیمات را در یک پنل پایینی باز می‌کند.
آپدیت بدون حذف برنامه از این به بعد
🔄
— همه بیلدها از این نسخه با یک کلید ثابت امضا می‌شوند، پس نسخه‌های بعدی مستقیم روی نسخه قبلی نصب می‌شوند. نکته: برای آپدیت
از نسخه 1.0.0
فقط یک بار باید برنامه قبلی حذف شود، چون آن نسخه با کلید موقت امضا شده بود.
رفع اشکال:
پنل اشتراک‌گذاری VPN حالا بلافاصله بعد از روشن کردن سوییچ، آدرس
ip:port
قابل کپی را نشان می‌دهد.
✅
عنوان ریلیزها تمیزتر شد (دیگر پسوند "(build N)" ندارد).
📝
Downloads
📥
https://github.com/QW-AI-Code/Aether/releases/tag/v1.1.0-build.2</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/whitedns/1235" target="_blank">📅 11:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1234">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید   درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/whitedns/1234" target="_blank">📅 11:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1233">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/IeP4OMLGC3Xg0WJspWz1hd_QWZ3mMzFe49WPushlnh27u_jcy5UT0qnCvmN4Z5ThidJ7y4H8fz8w10Fd5FmXSsjOujiAJqxtw2KRD04310g7Iot4g54lnKplFC1cA9nZnmctSitikv-YqH_h8Tc8A1M3Dp9dCgr6UwINVtuj8bFPP40D3gxd-Qg5mT1zaTijMAuMOUmIG38exYltiC0Q1j4_27tUTrZ3D11NXzbcGS3NVmVB0I5aB9zPRRH979SIgBFMrWV96l4lmaJz5kiMXSFhWccMMd5Rwm3EJRG8RZflA7lYPNZZtK7AmQeibBWLYcwpoxRL4SGgjFZsBxCd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/whitedns/1233" target="_blank">📅 05:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1232">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⚡️
اِتِر (Aether) — آزادی، با یک لمس!
⚡️
نسخه اندروید
درویدِ قدرتمند و رایگانِ اِتِر؛ اینترنت بدون محدودیت، بدون ثبت‌نام، بدون سرور شخصی!
🚀
🔥
چرا اِتِر؟
🖱
اتصال با یک لمس — VPN کامل سیستمی؛ همه اپ‌ها و مرورگرها بدون هیچ تنظیمی از تونل عبور می‌کنند
🛡
موتور پیشرفت
ه WARP با تکنیک‌های ضدفیلترروز:
✅
پروتکل MASQUE (HTTP/3 و HTTP/2)
✅
تونل تو در تو WAR P-in-WARP (حالت gool) برای سخت‌ترین شرایط
✅
قطعه‌قطعه‌سازی ClientHello و مبهم‌سازی ترافیک
✅
اسکن هوشمند و خودکار بهترین endpoint
⚙️
۴ حالت اسکن برای هر شرایطی: Turbo
⚡️
/ Balanced
⚖️
/ Stealth
🥷
/ Thorough
🔍
📊
نمایش زنده ترافیک — سرعت لحظه‌ای و مجموع دانلود و آپلود، درست مثل VPNهای حرفه‌ای
🌍
نمایش IP سرور با پرچم کشور + تایمر مدت اتصال
🧪
تست خودکار سلامت اتصال — بعد از هر اتصال، خودش بررسی می‌کند ترافیک واقعاً جریان دارد یا نه و دقیقاً می‌گوید مشکل کجاست.
🔁
اتصال مجدد خودکار — اگر ارتباط قطع شود، خودش دوباره وصل می‌شود
🔒
امنیت کامل، بدون نشت:
✅
بدون نشت IPv6 و DNS
✅
بدون بکاپ اطلاعات حساس
🎨
رابط کاربری زیبای Material 3 — دوزبانه فارسی و انگلیسی، با منوی مرتب و مینیمال
📱
سبک و بهینه — نسخه مجزا برای هر معماری (arm64 و arm32)
📥
دانلود مستقیم از گیت‌هاب:
https://github.com/QW-AI-Code/Aether
@whitedns</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/1232" target="_blank">📅 03:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1231">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سلام دوستان عزیز
👋
🌸
اپ CoreForge یک قابلیت جدید برای کاربران iOS اضافه کرده
📱
✨
این اپ شبیه WhiteDNS است که برای iOS و شرایط قطعی اینترنت طراحی شده
🚀
🌐
🔗
لینک:
https://testflight.apple.com/join/3htm1Whc
🎥
آموزش استفاده:
🔗
https://youtu.be/filwdiPKN90?si=O-hvgeNw43t4BUmR
📲
کانال تلگرام:
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/whitedns/1231" target="_blank">📅 17:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1230">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromامیرپارسا گودمن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=GJbvRKaGuVX0bXWeXPR1nmeAO2lMPXDBoXRaUfbavFPgoSOE4jYoRQeODTWNU8Q1LrmjkdCSRKTZLryQ6R4daeifiB6ceFbPJo8nwRpEtXQUE9zyLHYhbC86OkiSAGTLV1t52rnUGDzwgh1yuLgTjmB_fx5UaF97wMvwyo-dXKwARkMWKkNKI5qdWvuZI6cj0wx_50RkhpjHNmZQW5PEh4T51kLk6bHXjlQZ-Y4HIVmO_DsXCOS1EqJnE635Gf_yIxglnURLNJoDXVzfJ-umaXVst62LXlgLTe5119uSbLkhBgscuxFGEa59ldBxYVKc1_sSscPOb9PS_ADdZpzvt5tQ-IvBhwG3IcTB8cMXG4AJSsUDIC0L9xBMZ4aKAzXaL2jUPdUm5_niRYF5SW9k9NTF_OXtN0-V5m5sZVnSQdIxkdNYwBWNgjLhxcdYgO8uMpQcGxIn814By25grsQEYUdGdthjyRcqy6EtBjTC4Y0_L7iSNXm3L5elVv7luLCeu_aBYzA5JYI2tT3lVx5a4rT_jQmEK8BtfIFLBxSgAEX1IK1XCbHlp3dyFSNEyi4Fb7Res--s_6Dhnw08SOimM77Fj_4DwXvDxie3aDlfqHDMlxJ0qpN3WqdGZ9BrMglvqu_2mYQZ_Dv5bwWpQ5AzrtLDt10DxLXIjDxAOC53ZyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6b89a933.mp4?token=GJbvRKaGuVX0bXWeXPR1nmeAO2lMPXDBoXRaUfbavFPgoSOE4jYoRQeODTWNU8Q1LrmjkdCSRKTZLryQ6R4daeifiB6ceFbPJo8nwRpEtXQUE9zyLHYhbC86OkiSAGTLV1t52rnUGDzwgh1yuLgTjmB_fx5UaF97wMvwyo-dXKwARkMWKkNKI5qdWvuZI6cj0wx_50RkhpjHNmZQW5PEh4T51kLk6bHXjlQZ-Y4HIVmO_DsXCOS1EqJnE635Gf_yIxglnURLNJoDXVzfJ-umaXVst62LXlgLTe5119uSbLkhBgscuxFGEa59ldBxYVKc1_sSscPOb9PS_ADdZpzvt5tQ-IvBhwG3IcTB8cMXG4AJSsUDIC0L9xBMZ4aKAzXaL2jUPdUm5_niRYF5SW9k9NTF_OXtN0-V5m5sZVnSQdIxkdNYwBWNgjLhxcdYgO8uMpQcGxIn814By25grsQEYUdGdthjyRcqy6EtBjTC4Y0_L7iSNXm3L5elVv7luLCeu_aBYzA5JYI2tT3lVx5a4rT_jQmEK8BtfIFLBxSgAEX1IK1XCbHlp3dyFSNEyi4Fb7Res--s_6Dhnw08SOimM77Fj_4DwXvDxie3aDlfqHDMlxJ0qpN3WqdGZ9BrMglvqu_2mYQZ_Dv5bwWpQ5AzrtLDt10DxLXIjDxAOC53ZyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">https://t.me/xsfilterrnet/3623</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/whitedns/1230" target="_blank">📅 00:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1229">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OoFFv3RZGE6vWnqMvsrU64skarNuWpyVRa03kRNprmMQXn7XUDOV1qV-AZ_xS21BZiFSD119wh27olQcYYFiSzsgi9q-Gsmn9E_Qpi1aUWFA-a7YQjTmO7IxqNNnV0mIHVLmToQTUmEaYokO5dNw2vpYhKuV1NRPbnDoEq5u1u6nidAQ6z-nrLiqvsJoXVLeC7KGpnf7THZjyTTXM7zSAj8NtKNJPGLTMG5aiKheNscq1tZxzXxDB-jO85dyu-VtHbaNYnwS2aON_FwCZomhvMO5wu6IlDYkPcx0F4YAdlAA9CC5_tlFM6dMFIi7_ptXslYyZNgDGXOSPTJnPEwQEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی کانال یوتوب WhiteDNS
🌐
اگر به دنبال آموزش‌های تخصصی و کاربردی برای دور زدن فیلترینگ، پیدا کردن آی‌پی‌های تمیز و ساخت سرورهای شخصی هستید، این کانال یکی از بهترین مراجع آموزشی است!
🎓
در این کانال می‌آموزید:
🔹
آموزش صفر تا صد V2Ray
و راه‌اندازی پنل‌های ثنایی (3x-ui)
🔹
پیدا کردن آی‌پی تمیز با
WhiteDNS Scanner
🔹
راه‌اندازی
پروکسی MTProto
برای اتصال بدون قطعی تلگرام
🔹
معرفی ابزارها و کلاینت‌های مختلف (مثل CoreForge برای iOS و FlClash برای اندروید)
🔹
راهکارهای ارتباطی برای زمان قطعی کامل اینترنت
📡
و .................................
برای یادگیری ساخت فیلترشکن‌های امن و پرسرعت، همین الان به این کانال سر بزنید و سابسکرایب کنید.
👇
🔗
https://www.youtube.com/@WhiteDNS</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/whitedns/1229" target="_blank">📅 17:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1228">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/1228" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1227">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1227" target="_blank">📅 12:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1226">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/whitedns/1226" target="_blank">📅 12:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1225">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Dz2mDt02w-bd2nkBXbfJrRI5mrJ5xQ6ZVQnUTX5Rq_93tw-AkZY8fKOKUJXmf0eEZbG-RwGqMW43c72eMSQsAFg9LuBRfE0VMnkcPzpHxinZIzuXVDAQOx6yJUa6TGNe4k1-X3gFFBEZ9Fle9mOvnozcEZ0Qi-fwZJWMT1_mOrJ-Qm20aV3D4ParKdX3T4dJB9rfyomWxzDkpQ4b3FomlsfdJQHcALUESDChlM2fPyXDSw7oGmXjNmU6j7F15QfqRVVr0MaP5p-QptdUN5Dy_6xttwMhEiq2ndGu2gbb_JAux9b8EF5T0568rz6G9L_yY23ceIKTubhqrX-8IOTuug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/whitedns/1225" target="_blank">📅 06:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1224">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/O42y6OfvhbVUuZdvOxkLx1Vq_3Bk-xn8CrFpY9vpUpuFXG8JLLMR7GAR4VLtFaRNXS_wc846MTeRNCAZjt7CaEFEoHdWdTUSA9ZBSlyWMpLyTBf_oeHGmlIwM270fuOgTRYKVEfUrNKWEi68oRcEmHAcieJa_GjJ5rMq8zCqGZH_0yoTFAYyFLsCyHFqYSUuakO_-J53jzXSJCWmL4yEQJYBUMHqAVwPKuVwxfoZYkozFx3SkCIkJgJ3pEDo-ZcKAOQNjmaCjNi4hPq8Y6Xt9JZBMo44DELqIYyvhCHA_5cQ3Itx0LLfDXT-rgDTcEDjtCBjMtT_87AgYfbhETpo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :
ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.
پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است همیشه کامل یا دقیق نباشند. این ربات به اینترنت زنده دسترسی ندارد، جایگزین پشتیبانی انسانی نیست و اگر اطلاعات کافی نداشته باشد قادر به پاسخگویی نیست. لطفاً اطلاعات حساس یا شخصی خود را برای ربات ارسال نکنید.
برای مدیریت بهتر منابع و کنترل هزینه‌ها، محدودیت استفاده از ربات به شکل زیر تنظیم شده است:
- هر کاربر می‌تواند در هر ۵ دقیقه حداکثر ۳ سؤال بپرسد.
🕒
- سقف استفاده روزانه برای هر کاربر ۵۰ سؤال است.
📊
- در صورت رسیدن به محدودیت، ربات زمان تقریبی انتظار را نمایش می‌دهد.
⏳
- دستور /search و سایر دستورات عمومی شامل این محدودیت نیستند.
🚫
- محدودیت‌ها پس از راه‌اندازی مجدد ربات نیز حفظ می‌شوند.
🔄
این تغییر باعث پایداری بیشتر ربات و دسترسی منصفانه‌تر برای همه کاربران می‌شود. سپاس از همراهی شما
🌱
لازم به ذکر است در صورت سواستفاده این محدودیت بیشتر خواهد شد - پس خواهشمندیم با استفاده درست جلوی به ادامه این خدمات کمک کنید
لینک ربات :
@WhiteDnsResponder_bot
🔗
@whitedns</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/whitedns/1224" target="_blank">📅 20:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1219" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/whitedns/1219" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ow11ZRC60DOEqHR3s7z0bRJKqLl59KpuihKMiSvdKL4BR7O7YVqrT4SeaMplzCAgYW0FVRiIGPc_NDngN4vUQsZNs2h2_ycJOOFTu2wEowS4EYQC5pbDbHVsZDSn9LUBB9dtjYdePbcqGtJb-SGgTYD8oNoic_YhGEhvh57geSAotzCPKD2XFeKD53Rz6uNCUswuZZWrMl3saKN4xmkn-5k7abtznNO2yqusVLWBwCkhIZlqrdcIV_KIYGQJLH_5WLG8AWafcHLkN8Qxmn0w9rDeuuaAFIcweDwMfxMzMwHaEcJs-AKgsaBFNFNau4qmmYz9sAAtM7eEY5iQwy5mXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/whitedns/1218" target="_blank">📅 17:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1217">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/whitedns/1217" target="_blank">📅 17:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1216">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⚠️
⚠️
⚠️
⚠️
اطلاعیه مهم
با بالا گرفتن تنش‌ها و با توجه به تجربه‌ای که از قطعی سراسری اینترنت داشتیم، پیشنهاد می‌کنم دوستانی که تازه به جمع ما اضافه شده‌اند، مطالب زیر را با دقت مطالعه کنند.
در دوره‌ی قطعی اینترنت، تیم WhiteDNS چند اپلیکیشن برای دسترسی به اینترنت طراحی کرده که هدف آن‌ها این است در صورت تکرار قطعی سراسری، همچنان قابل استفاده باشند.
این اپ ها با WhiteDNS VPN کع این روز ها استفاده میکنید متفاوت هستند.
امیدواریم هیچ‌وقت دوباره چنین شرایطی پیش نیاید، اما بهتر است آماده باشیم. اگر قطعی سراسری اینترنت تکرار شد، هدف ما این است که شما بتوانید خودتان و عزیزانتان را تا حد ممکن به اینترنت وصل نگه دارید.
✍️
اگر هیچ اطلاعی از این اپ ها ندارید، و نمیدونید چطوری کار میکنند، پیشنهاد مطالب این تاپیک رو مطالعه کنید.
https://t.me/whitedns_group/32380/38590
WhiteDNS
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
WhiteDNS Desktop
یک اپلیکیشن بر پایه MasterDNS برای کانکت شده به اینترنت برای ویندوز، مک و لینوکس.
✍️
آموزش ویدیویی استفاده از اپ
✍️
دانلود آخرین نسخه
@WhiteDNS_Installer_Bot
اگر سرور شخصی دارید، میتونید سرور MasterDNS خودتون رو راه اندازی کنید. با کمک بات ما، اتوماتیک سرور مستر خودتون رو نصب و مدیریت کنید.
ما و تمام اهدا کننده هایی که همیشه همراه ما بودند سعی میکنیم سرور های عمومی جدید برای شما داخل چنل قرار دهیم.
⚠️
باقی لینک های مفید
👥
لینک گروه اصلی
👾
دانلود آخرین نسخه اندروید
💻
دانلود آخرین نسخه برای مک‌ و ویندوز
📱
تست فلایت آخرین نسخه آیفون
📱
آموزش استفاده از نسخه موبایل
🌐
آموزش راه اندازی سرور شخصی
🔥
آموزش مفاهیم و اولین شروع استفاده از WhiteDNS
🖥
آموزش استفاده از نسخه ویندوز
🔑
لیست سرور های رایگان برای V2Ray و MasterDNS
🤖
ربات ساخت سرور و مدیریت MasterDNS
🤖
ربات دریافت رایگان کانفیگ V2Ray
🤖
ربات دریافت ریزالور</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/whitedns/1216" target="_blank">📅 14:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1215">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">White DNS
pinned «
دوستان برای همه اینها اموزش هم گذاشتیم که الان لینک را اضافه کردیم .  لطفا بدون دیدن این اموزش ها سوال نکنید
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1215" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1214">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">درود به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/whitedns/1214" target="_blank">📅 13:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1213">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1213" target="_blank">📅 12:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oexSjoBnDSUnPNUcnWBF8weyFXZNaXxHTk7YmbhepkVlX94E5F7JShMebVdy-59GSFqOkE9GK_KxGVuOlq0ko1WNW0HIha7Li5lm3CQEbuXLLIach1LJBgWwAXYoARvIZ5fw2vwrrlmsOVPgQNfVvcVuWxI-RFy-Tq3TgKUXY7VP0eZK7pC88SfL3DRMsYbDXaHeWQ5DL64WQESJ0OSnToPlL8Xk2nuTqIS8himk1im5RipRTo7JPEEILkOg7zCCXveaTSKmeZXWbJ9uUK6gOgylyXqIL8S-gp42HObqp57kFFxdI-LD1cXzR3EZyScfMddSWLBktLz67UXPEnpShg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود
به همه‌ی همراهان عزیز چنل؛ امیدوارم حال دلتون اگر هم که عالی نبود حداقل بد نباشه.
🌟
با توجه به شرایط کنونی خاورمیانه، ترجیحاً هم اپلیکیشن WhiteDNS را نصب/آپدیت کنید و هم اپلیکیشن TheFeed را نصب/آپدیت کنید تا در صورت قطعی مجدد اینترنت بتوانید به اینترنت جهانی دست یابید.
🌐
📱
لینک‌های مورد نیاز:
دانلود ورژن آخر اپلیکیشن WhiteDNS اندروید | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
🛡
آموزش
دانلود ورژن آخر اپلیکیشن WhiteDNS ویندوز | وی‌پی‌ان بر پایه‌ی دی‌ان‌اس برای شرایط سخت و محدودیت شدید اینترنت
💻
آموزش
دانلود ورژن آخر اپلیکیشن TheFeed اندروید | جایگزین تلگرام در شرایط سخت و محدودیت شدید اینترنت
🔄
آموزش
لینک‌ها با توجه به نیاز کاربران آپدیت میشن.
🔄
@whitedns</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/whitedns/1211" target="_blank">📅 12:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/oCJOSnFYZ94YCcz1PLgNsBnbFZr3sIgsc-mhyjihbqYH_A4uKAVesurBv7jzMAd4avKcX19CeCHh8dQ4rptHVNyemzBL3NsrUgCsGqYtJuyI5NlTKrvYysrFL53qMmM6mOKsWnrO-C4BRlG_rq1_cpARdLOQT1EmLzYKLl1a5IhGz8RteJ5Eo_hNPvv2I05Ug42XdEIO5Y_MCD2ZiuO2YEXTAB4nDAAoH1pBsZcSpP2S_uq10Vg6OuFyE-3meg3acrba6jg787tj8uLVbDyLJ6UbOTONpMj3z1gszFYMOQJsGrE2NYV01qgnIE2AbC-mgsaajGnrAcUzSOgv5fMkrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در whitedns android</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/whitedns/1210" target="_blank">📅 12:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vrm7rhHwtBtdFrcJn3qxnsLYYEhjm1bKDfDJRL1cwSWBAA8L0AQWS4e7_mUY1DaXICFE_GZnxrw6fRgq61I2GCLfujzAzF5ZVnjob-fcZYykDoG9rdmZ5tIWPFLwC6kdm0pZ_vOZHbnc7PNmSJhUOccwIa76SEI1Id0OgdlB62h2AHuSbr1ViKieQmy81aYzXEeTBp4uj3HNmIggAVkiLXPV3z9g1OATFHkG0t8x1nKvLjOxbc2OTFpGajEj95ofxLhp2tZtH4zGMxJ74muuweK4Q6Tb206BaMfwswJcqs2eoAX1QsSqCJDRJd6t8RVCHSj6Xsvvwg-_qrpN_gAg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وارد کردن تنظیمات بهینه در Whitedns windows</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/whitedns/1208" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1206">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Android.zip</div>
  <div class="tg-doc-extra">2.5 KB</div>
</div>
<a href="https://t.me/whitedns/1206" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/1206" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1205">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ebU2lfoIxCYPZB_BHtpmoujFQpFkx4zEsSKnilpLC_ZfV0BxDppI8Q2brep2DctAhfcZZiMIsJtX1C7QgTlWb6LA5f90IJys3cmRvzV3X9eJihutzz8wOOvIOdP_7sc62wcgx1FZXntvKzJfHfqzFngg6zbkDPij6yqGroQl2AbtjiDIf08gC5sGxfgoDP2X78d9pwW7pr0eELk7ZO-sz2dvr8h8C11huXalXzBPXWrSvg2NDNLZWCXkva39EKotmwwbel1HcQlMGWkPvMfVyJJgiPCSfx5keynBzds0o7EJYiaFBF9PGL5mLF9FdX6lKcHlvT19isqjsLMBc7sDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
افزایش سرعت اتصال WhiteDNS
تنظیمات اختصاصی whitedns
یکی از مشکلاتی که بسیاری از کاربران با اون مواجه هستن، اتصال موفق
WhiteDNS
با سرعت پایین یا ناپایداره.
✅
یکی از مؤثرترین راه‌ها برای افزایش سرعت و پایداری اتصال، استفاده از تنظیمات بهینه میباشد (البته استفاده از سرور و کانفیگ اختصاصی هم تأثیر قابل توجهی روی کیفیت اتصال داره).
📦
به همین منظور، ۳ تنظیمات پرسرعت برای
اندروید
و
ویندوز
آماده کردیم که می‌تونید از اون‌ها استفاده کنید.
🍏
کاربران آیفون:
اپلیکیشن
CoreForge
به‌صورت پیش‌فرض تنظیمات بسیار مناسبی داره و در اکثر مواقع نیازی به استفاده از تنظیمات اضافی نخواهید داشت.
📥
نحوه استفاده:
• فایل تنظیمات رو مستقیماً داخل اپلیکیشن
Import
کنید.
• یا فایل رو باز کرده و محتوای اون رو
Copy/Paste
کنید.
⚠️
توجه
:
این تنظیمات فقط
مخصوص اپلیکیشن WhiteDNS
(مناسب اینترنت ملی) هستن و به درد استفاده در
WhiteDNS VPN
نمیخورن ؛ لطفاً این دو مورد رو با هم اشتباه نگیرید.
💡
نکته مهم
:
ممکنه این تنظیمات باعث افزایش مصرف اینترنت بشن. بنابراین بعد از اضافه کردنشون ، مقادیر Download Dup و Upload Dup رو متناسب با نیاز خودتون تنظیم کنید:
🔹
مقادیر
بالاتر
👈
مصرف اینترنت بیشتر
✅
اتصال پایدارتر
🔹
مقادیر
پایین‌تر
👈
مصرف اینترنت کمتر
✅
اتصال حساس‌تر و شکننده‌تر
❤️
امیدواریم این تنظیمات تجربه‌ای سریع‌تر و پایدارتر از WhiteDNS براتون فراهم کنه.
@whitedns</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/whitedns/1205" target="_blank">📅 12:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1204">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1204" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1199">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-arm64-v8a-release.apk</div>
  <div class="tg-doc-extra">19.2 MB</div>
</div>
<a href="https://t.me/whitedns/1199" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/whitedns/1199" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1198">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKDYhD7Qb6DE7DWXRk-X2xEukVZLseVeiO5pX9iKj7V2bPKD18lCF_O-S5MkK25A_MK9wf-sRJJmLtnRnZz7a50vr4A-dCEzKITBf9dvxOQLSZTp3tv-y9mczDy_k0lOjfwZzjcg4FqRJ0LOwem-OWBtjN-3i_mF8iU9uCBPR3PxJS_ygPlPko2i8q7hGBC_-QBRi2m7vq4Mat0uyHKNpcgyqqzgjCmaMCVgDAPErY1_lDv9hnIgTFWxG9NMkNvP-c03JRgeL_OoYni1E_X9Z96GcxupPScAfbz_gPZQ8JNIeEuoGc8s6hYB9DMUn218SX9ZvxWqG4ll-F8NW3c5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نسخه 0.0.9 اپلیکیشن WhiteDNS VPN منتشر شد
در نسخه جدید، اپلیکیشن
WhiteDNS VPN به‌طور کامل فارسی‌سازی شده است
تا استفاده از بخش‌ها و تنظیمات مختلف آن برای کاربران ساده‌تر و قابل‌فهم‌تر باشد.
همچنین ظاهر اپلیکیشن به‌طور کامل به‌روزرسانی شده و قابلیت‌های جدیدی برای کنترل بهتر اتصال، DNS و کانفیگ‌های شخصی اضافه کرده‌ایم.
قابلیت‌های جدید:
• فارسی‌سازی کامل اپلیکیشن
• طراحی و ظاهر جدید اپلیکیشن
• امکان اضافه کردن DNS اختصاصی با پروتکل‌های
DoH
و
DoT
• امکان وارد کردن سابسکریپشن‌های شخصی با فرمت‌های
Mihomo، V2Ray و JSON
• امکان تعیین پورت دلخواه برای قابلیت
IP Fronting
• ارتقا و بهبود بخش
Connection
و فرایند اتصال
• اضافه شدن قابلیت
TLS Integrity Test
قابلیت
IP Fronting
به‌خصوص در دوران قطعی یا اختلالات شدید اینترنت می‌تواند بسیار کاربردی باشد. حتی در شرایط فعلی نیز کاربران می‌توانند با استفاده از IPهای تمیز Cloudflare، بعضی از کانکشن‌هایی را که به‌صورت عادی کار نمی‌کنند دوباره فعال کنند.
قابلیت
TLS Integrity Test
نیز برای کاربرانی اضافه شده که هنگام استفاده از بعضی کانفیگ‌ها، برای اتصال به سرویس‌هایی مانند
ChatGPT
با مشکل مواجه می‌شوند.
با فعال کردن این گزینه، اپلیکیشن پیش از اتصال، سلامت و یکپارچگی TLS را بررسی می‌کند. اگر TLS دست‌کاری یا جایگزین نشده باشد و تست با موفقیت انجام شود، اپلیکیشن به کانفیگ متصل خواهد شد.
در صورتی که یک کانفیگ این تست را با موفقیت پشت سر نگذارد، اپلیکیشن بررسی کانفیگ‌های دیگر را ادامه می‌دهد تا یک اتصال سالم و مناسب پیدا کند.
فعال کردن این قابلیت ممکن است زمان اتصال را کمی افزایش دهد، اما می‌تواند مشکل باز نشدن ChatGPT و سرویس‌های مشابه را برطرف کند.
پیشنهاد می‌کنیم همه کاربران از همین حالا اپلیکیشن را دانلود کرده و آن را به آخرین نسخه به‌روزرسانی کنند. این نسخه یکی از راهکارهایی است که برای شرایط قطعی و اختلالات شدید اینترنت روی آن کار کرده‌ایم و ممکن است در چنین شرایطی بتوانیم استفاده بسیار بیشتری از قابلیت‌های آن داشته باشیم.
📱
WhiteDNS VPN v0.0.9</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/whitedns/1198" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1196">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lHaieTo1DJk12yZq5EPTCbynzknAM-pzGq31vhB4UIJ-K2cas8UUOfFVGRQ-omkaLmCC7yBOSttFkQqdanNhZr7Q-53pByImvzIWi7Kp7PJQklCPHaQuMtNBxU9AzBnjbijt7eoW0lv20OBuiwxZSpqAAsocN4Jzn__162zEjyMXh4UpDUC0-4LYKz2SKYae021O3krYrvEu20LISC-BKywhXKFcTkwuDPnmYUEb3En-hmQjuX0QKm5YS20DQej9UiP6-4JsSq9GcEk09xEgbXE84UHjKnpl9uYty-UvFmbbe4xqyU41Fu_r9AJ5x0fir389c9ABB_eyE3SXXJ876w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mgFSkgcFITO3E2tZAb3JeYc_LriTAW5BojI4kghLm0mbRnYhS_0GCsN_ZnSKqER6toD_ENgh4P4CIeO_2nMiuyggK3OqJ_oS-t05nFFH-HKVsIEltxkHRrTKr1QJLSnyVFthAsw7T8GWacUqtZ96GwiUcI1CttLIhuwFms5EiS__0Uvx_Xn0M201Ps3fW8w4veMVyymAsyUMbsFXBP39XMlrgTaX4OAA7C-kZCX9pp1aotkJH_JsTt9vhgl1WnxzrKXeyd_95bpufi-LI1_sx0M_CZMNdoRV7o5yuzrgs8Mms4iTLOhjCzKzZXgdCR-yVEtno8ex3eTIygxbBG9Mmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آپدیت جدید Aether-GUI (نسخه 0.4.0) با هسته‌ی جدید!
نسخه‌ی جدید برنامه آماده‌ست. توی این آپدیت، هسته‌ی اصلی (Aether Core) به ورژن
1.2.0
ارتقا پیدا کرده و قابلیت‌های زیر به GUI اضافه شده:
🔵
رفع مشکل وضعیت Connected فیک:
قبل از این، بخش Validation ابزار با پینگ کردن
1.1.1.1
(که داخل شبکه‌ی خود کلودفلر هست) وضعیت رو متصل نشون می‌داد؛ در حالی که ممکن بود ترافیک واقعی اینترنت قطع باشه و لود نشه. حالا ابزار یک ریزالور خارجی رو هدف قرار میده و باید ۲ بار پشت هم موفق بشه. یعنی وقتی می‌نویسه Connected، واقعاً متصله.
🔵
اضافه شدن انتخاب ترنسپورت برای MASQUE:
توی بخش Advanced الان می‌تونید نوع پروتکل ارتباطی MASQUE رو تغییر بدید:
HTTP/3 (QUIC):
حالت پیش‌فرض؛ سریع‌ترین هاندشیک و بهترین کارایی (اگر شبکه شما با UDP مشکلی نداشته باشه).
HTTP/2 (TCP):
کاملاً شبیه به ترافیک عادی HTTPS؛ مناسب برای زمان‌هایی که شبکه شما UDP/QUIC رو اختلال می‌اندازه یا مسدود می‌کنه.
تنظیمات انتخابی شما به‌طور خودکار ذخیره و در استارت‌آپ بعدی اعمال میشه. (این سوییچ فقط روی پروتکل MASQUE تاثیر داره و برای WireGuard/gool غیرفعاله).
🔵
به درخواست دوستان فرانت کار لوگو هم از دیفالت عوض شد
🤠
دانلود نسخه 0.4.0:
https://github.com/MatinSenPai/Aether-GUI/releases/tag/v0.4.0</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/whitedns/1196" target="_blank">📅 04:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1195">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/q91U56UDbC27Oa2FmtKtONViWsPIDnuwX7fpjOwJy3XrHGY5cFjW3My21Vl2doJeKyPEwukds2iR6bVCZ7l4jASS8wbttETzIA0DcWfi0zlF87Tl-2C_GpnB3EpeIIz1FUsQisBWFnPoGPLfXKPnMXYNS3nDzsq-Be_v7p1BeCcTFU1UJBVoiS9bxyTTzhmtQpgY6wnc7Nnv4GApPZyosQB0HA6j1N5NlhqdiuNfWB9xaUb0vD97vWecgo-SR-C59EPFmSx7DGQaBkP9lZrx-tjwWAnsrmcHguBJ0iW2uRZ7bgWQVIyYefc8xbT0og7G0gJRlUNAFX5mHX2uJDjPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
راهنمای جامع تنظیمات APN اپراتورهای ایرانی
📱
📥
۱. مراحل تنظیم در اندروید (Android):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
اتصالات (Connections)
یا شبکه و اینترنت بروید.
3. بخش
شبکه‌های موبایل (Mobile Networks)
را باز کنید.
4. وارد گزینه
نام نقاط دسترسی (Access Point Names یا APN)
شوید.
5. روی
افزودن (Add / +)
بزنید تا APN جدید ساخته شود.
6. فیلدهای
Name
و
APN
را مطابق لیست زیر پر کنید (بقیه گزینه‌ها مثل پروکسی و پورت حتماً خالی باشند).
7. از منوی سه نقطه بالا گزینه
Save (ذخیره)
را بزنید و آن را فعال کنید.
🍏
۲. مراحل تنظیم در آیفون (iOS):
1. وارد
تنظیمات (Settings)
شوید.
2. به بخش
Cellular (تلفن همراه)
بروید.
3. گزینه
Cellular Data Network
را انتخاب کنید.
4. در بخش
Cellular Data
، روبه‌روی گزینه
APN
مقدار مربوط به اپراتور خود را (از لیست زیر) وارد کنید.
5. یک‌بار اینترنت گوشی یا حالت پرواز را خاموش و روشن کنید.
📋
لیست مقادیر APN اپراتورها (برای کپی آسان روی کلمه‌ها ضربه بزنید):
🔹
همراه اول (MCI)
* Name: MCCI Internet
* APN: mcinet
🔹
ایرانسل (Irancell)
* Name: Irancell-GPRS
* APN: mtnirancell
🔹
رایتل (RighTel)
* Name: RighTel
* APN: rightel
🔹
شاتل موبایل (Shatel Mobile)
* Name: Shatel Mobile
* APN: shatelmobile
🔹
سامانتل (Samantel)
* Name: Samantel
* APN: samantel
🔹
تالیه (Taliya)
* Name: Taliya GPRS
* APN: taliyagprs
⚠️
نکته بسیار مهم:
اگر در فیلدهای
Proxy (پروکسی)
یا
Port (پورت)
در تنظیمات گوشی شما هرگونه عدد، آدرس یا کلمه‌ای وارد شده باشد، سرعت اینترنت شما به شدت افت خواهد کرد یا کاملاً قطع می‌شود. حتماً بررسی کنید که این دو بخش کاملاً
خالی
یا روی
Not set
باشند.
@whitedns</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/1195" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1194">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/1194" target="_blank">📅 13:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-1192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">•
📢
به‌روزرسانی ربات WhiteDNS
🛠
ربات ورژن 3 :   ربات WhiteDNS یک دستیار هوشمند فارسی است که با استفاده از محتوای کانال، به سؤالات مربوط به اینترنت آزاد، DNS، VPN و ابزارهای عبور از فیلترینگ پاسخ می‌دهد.    پاسخ‌های ربات کوتاه و کاربردی هستند، اما ممکن است…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/whitedns/1192" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
