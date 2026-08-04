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
<img src="https://cdn4.telesco.pe/file/otgiOvBZ4HN9o-Xxrq0MF9C1kq89C5IVAMMKIICQzwKGT8q5g12ljPadySjuqPmWfco5MdRTbGzYIPbPjV8V3iAMQRz7OsPJvJKfWdI0Q0sHak0rC8Eg4OlRPHTU88_vToaSLNc-_3u5MOkmepDnwa8La10umR0sp7cVNkCFYwXWMXGsrCT46dtUcdKR1C7k5_swCzpBO53th20mwTVC9izxzFnrhadP9rGG9Yl_1x2_bVTMYWObLkKEoVyRZlctGnh_sr0bkZtfRBpOBGz7-ym44gGVuXvEqZU7mCdZ_iIsNF-f8d-xlVzxV7AifllO8AC06tRtWywtlReJ0UyzEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.6K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالیhttps://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 23:36:34</div>
<hr>

<div class="tg-post" id="msg-19666">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.  به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات…</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/SBoxxx/19666" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19665">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ایران در حال بررسی طرحی برای بازگشایی تنگه هرمز از طریق ایجاد یک صندوق داوطلبانه است که توسط کشورهای خلیج فارس و کشورهای اروپایی که به این مسیر وابسته هستند، تأمین مالی می‌شود.
به جای اعمال عوارض رسمی، این صندوق هزینه‌های ناوبری، حفاظت از محیط زیست و خدمات جستجو و نجات را پوشش خواهد داد، مشابه مدل موجود در تنگه مالاکا.
این پیشنهاد که به گفته منابع از عمان حمایت می‌شود، می‌تواند یک راهکار قانونی فراهم کند، زیرا قوانین بین‌المللی اجازه دریافت عوارض عبور اجباری در گلوگاه‌های کلیدی کشتیرانی را نمی‌دهند.
منبع: تلگراف</div>
<div class="tg-footer">👁️ 714 · <a href="https://t.me/SBoxxx/19665" target="_blank">📅 23:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19664">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr9PAgspaswUQvXCVxR_qkoss2rkGF11HjDd7t8-eD1xX5Uhi5QkJJZe0dAhFeQFvt-n_JQ9xjiSbbsVX3q1HX8BoSH42bz4MxDutLxQyFgGkf5RE2ptzy5_j68lT7RQO1kUbHCyO4GWWF6stwWJEIYvBxIS4nUtrPjbkM6sR0Ip9xMlUycseep5r7oHP1iyJEasjhqv788fHJyzepGO1JMfSjTxCv5OgHyoR8aAhzk5Oh2B4-jWqCNyA_m_IqxQP_KkTfF38kJe1PzJkHhD3qaUnT5xOIok37dipqlF9LThWMmrC2zOnBM9OdqciBcbTt5k8Mqmkx3yOt5vElBikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏳
سوپر اپلیکیشن بله بعنوان اولین لژیونر اپ های داخلی وارد اپ استور شد</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/SBoxxx/19664" target="_blank">📅 22:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19663">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SBoxxx/19663" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19662">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ایران سیگنال داده است که مایل به بازگشایی تنگه هرمز است، اما در عین حال حق دریافت هزینه‌های عبور، تضمین‌های امنیتی در برابر حملات آینده، پایان محاصره دریایی ایالات متحده و تخفیف تحریم‌های نفتی ایالات متحده را مطالبه می‌کند.  منبع: WSJ</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SBoxxx/19662" target="_blank">📅 21:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19661">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.  روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ…</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/19661" target="_blank">📅 21:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19660">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">GeoMarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SBoxxx/19660" target="_blank">📅 21:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19659">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سبحان الله!</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/19659" target="_blank">📅 20:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19658">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbrIdRpwR9x82-IGNFjZKrdVckhpuws5yNu3woZVK1JBE6YzaIIodoFFzh7T_DzF8nbJKGNFxt0cagaOLTaEKcj6DX-O2OafJqvhwv0Q0GqeWsiXxfSX9FicqqcRS520u89rfvGTGgKOWWM28Z8tvjFjIA7siz4R7bDw6GMKSRiS_C-35jLt62Sujlxb5lS-4Nx-qyAotaYU1OcPm9dkRXcCy6M4JblvRyk866wW6547IPCVRsaYcLrPx8yvWTIF7MphBNPYyYQ-SNMUJLl9wp1IoH2HKYs9PP-UFJKm2b7qqeYWhpC8ajTlMh8rtUsqtV2Mjb71vqjCnxVIEJQrBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SBoxxx/19658" target="_blank">📅 20:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19657">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روبیو، وزیر امور خارجه آمریکا: پیشرفت‌هایی در مذاکرات با ایران حاصل شده، اما هنوز توافق نهایی وجود ندارد.
روبیو گفت: «ما در مذاکراتی بین عمان و ایران در مورد بازگشایی تنگه هرمز برای تردد کشتی‌های تجاری شرکت داریم» و افزود: «امیدواریم این اتفاق به زودی رخ دهد.»</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SBoxxx/19657" target="_blank">📅 20:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19656">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ایران در حال بررسی اجازه دادن به کشورهای اروپایی برای خنثی‌سازی مین‌ها در تنگه هرمز است، امتیازی که می‌تواند بخشی از یک توافق برای عادی‌سازی حمل‌ونقل دریایی در این مسیر و تسهیل مذاکرات صلح با ایالات متحده باشد.
ایران بارها به‌طور علنی اعلام کرده است که اجازه نخواهد داد کشورهای خارجی در تلاش‌های خنثی‌سازی مین در این مرکز حیاتی حمل‌ونقل نفت و گاز طبیعی مایع‌شده مشارکت کنند. با این حال، طبق گفته دیپلمات‌هایی که با این وضعیت آشنا هستند و به شرط ناشناس بودن درباره مسائل حساس صحبت کردند، تهران در جلسات خصوصی در هفته‌های اخیر موضع خود را تعدیل کرده است.
وزارت خارجه ایران بلافاصله به درخواستی برای اظهار نظر پاسخ نداد.|</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SBoxxx/19656" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19655">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">غرق شدن کشتی هندی در ساحل یمن  به‌گزارش برخی منابع یک کشتی هندی در فاصله ۱۳ مایلی جنوب حدیده، توسط نیروهای انصارالله مورد حمله قرار گرفته است. این حمله با استفاده از یک قایق انتحاری انجام شد و در نتیجه، کشتی غرق شد.</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19655" target="_blank">📅 18:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19654">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حتی وقتی کشتی طوری ش نمی‌شود، هندی ها تلفات می‌دهند</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SBoxxx/19654" target="_blank">📅 18:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19653">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">العربیه : تا ساعات آینده بیانیه بازگشایی تنگه هرمز، رفع محاصره و از سر گیری مذاکرات اعلام می‌شود</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/19653" target="_blank">📅 18:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19652">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">323.7 KB</div>
</div>
<a href="https://t.me/SBoxxx/19652" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 18</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/19652" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19651">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 18</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19651" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 18
سه شنبه 4 آگوست 2026</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/19651" target="_blank">📅 15:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19650">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گروه حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SBoxxx/19650" target="_blank">📅 14:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19648">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ij4kpBk-jjWbzjsDTYoIdS5UziEuLFxWPLzM1cluh-yze3h7l40aO9COP9rBDEGwtxbHFJX6mfabAmZIzslyG6r_dI9nT62mlbU1whxzSs0JKv9DQPnj0JJZedraxB-z4h1EJLGQ-3mcsTC3DIBdnqwh_EVqSgrbIlsc6JEm_GN3jvHooAkshYb6zXGOnvQyQpUSbtEcW9dDSkO9xALXpq3s8iN4_Jeo9XCyUr5lXi7JrKhX1iCXPZLQzSlpFqHeSaoe8Id-qqBj8-c8HulTVy5ZABAhNlYi1OquYw1ns9Mpmd5PDHJKBI85czHxkFj_wX7rTtqUtExKNhXVU9tR-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfwNEWZFcRK3zR871nh1RZy_bwoB8CEUGBj3mKITAs3ygy_UtlzIYWpO-bVVChQ40kOwz9aaRSkA8ULJUXyQzWR4V_dyKwy8d4G4O9oPQSxjQnHP4ieTGPPR3PunxIpTTqWJdCBYym8lq7JHB4ejkh8-HkLwrRVl4YzNOkgTJBhLLlT_Sp5Mu8FMbkxthkhXT-b_dlv2zkH6sLsKmbInxUakEAWg1GltNCHwBrFdOpZDjZhfeinmoBFdgh9HrMC0OVDViTgH_Fy5tdliPNnbSm8qG9KLIhP__7GEjUooEjtIMmL1o0q2V8jCfeu7W-tFEL1askjo1H96hNVwNBPs9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/19648" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19647">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI1tSsREtTwAeh8AUPlnCtLHIe15FeEDopbv6fqfTUI4GRk_XwH_RZ59aI9o0VT9VZZSuf-AYH2C9P9gqux9s10Y6x4E20hT1d47_HQ7P-zHQbeJEplZaoJCLiIonqHfZ3Mx3WLIgByB-2kRMP0Idth8p5WwdZg7SMjFC6iNLVpTaUFcO3Gk6GtgEtLGKRhdG3zdcHpvBJO9NwSSM6zTq8LuqOqrHteIU3djJDHYZNoo5Qnq8Hnl4qrwJKMyKKlCndJwip9O74T4p6BX7O-gX-gTrCg_MR5sKqoT3kHzL0JPgw7Ipcwn0HpxFtdMfu9xB1smZkNRNyy9oqvGG633Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادداشتی به قلم « احمد کوچاک»
ایران روی اخلال اقتصادی برای وادار کردن آمریکا به امتیازدهی حساب باز کرده است
ایران در حال اجرای یک راهبرد فرسایشی حساب‌شده در سراسر خاورمیانه است و با استفاده از مسیرهای کشتیرانی جهانی و زیرساخت‌های انرژی به‌عنوان ابزار فشار، تلاش می‌کند اراده واشنگتن را فرسوده کند. تهران بر این باور است که افزایش هزینه‌های اقتصادی در نهایت آمریکا را به دادن امتیازاتی درباره کنترل تنگه هرمز وادار خواهد کرد.
تهران در حال اجرای یک کارزار فرسایشی حساب‌شده علیه ایالات متحده است و کریدورهای تجاری و شبکه‌های انرژی خاورمیانه را به نقاط اصلی اعمال فشار تبدیل کرده است. این راهبرد از رویارویی مستقیم نظامی پرهیز می‌کند و در عوض بر افزایش هزینه‌های اقتصادی و لجستیکی ادامه این تقابل متمرکز است.
رهبران ایران بر این باورند که می‌توانند واشنگتن را پشت سر بگذارند؛ به این معنا که هزینه حفاظت از کشتیرانی بین‌المللی برای آمریکا و متحدانش را آن‌قدر افزایش دهند که در نهایت پذیرش خواسته‌های دیپلماتیک تهران برای واشنگتن کم‌هزینه‌تر از ادامه وضعیت موجود باشد.
گسترش نقشه تهدید
عملیات ایران دیگر به تنگه هرمز محدود نمانده و میزان تحمل آمریکا در برابر اختلال در چندین گلوگاه دریایی را هم‌زمان آزمایش می‌کند. اکنون تهدیدها دریای سرخ، تنگه باب‌المندب و زیرساخت‌های انرژی عربستان سعودی را نیز دربر گرفته‌اند.
این پراکندگی جغرافیایی، نیروهای دریایی بین‌المللی را وادار می‌کند مأموریت‌های اسکورت و حفاظت دفاعی بیشتری انجام دهند؛ اقدامی که منابع غرب را فرسوده می‌کند، بدون آنکه الزاماً توازن نظامی منطقه را تغییر دهد.
مایکل نایتس از مؤسسه واشنگتن می‌گوید:
«ایران از همان ابتدا تلاش کرده است با گسترش گزینه‌های تشدید تنش خود، آمریکا را در این زمینه پشت سر بگذارد؛ به‌گونه‌ای که همیشه بتواند هر هفته چیز جدیدی ارائه کند: جغرافیای جدید، نوع جدیدی از سلاح یا نوع جدیدی از هدف.»
بهره‌برداری از آسیب‌پذیری‌های داخلی آمریکا
محاسبات ایران تا حد زیادی انتخابات میان‌دوره‌ای آمریکا را نیز در نظر گرفته است. تهران بر این باور است که دونالد ترامپ، رئیس‌جمهور آمریکا، در شرایط افزایش قیمت سوخت و کاهش حمایت عمومی، تمایل چندانی به ادامه دادن یک جنگ نامحدود ندارد.
این درگیری شش‌ماهه تاکنون به کشته شدن ۱۸ نظامی آمریکایی از ماه فوریه منجر شده و فشار نمایندگان جمهوری‌خواه در کنگره برای ارائه یک راهبرد روشن جهت خروج از جنگ را افزایش داده است.
چرخش به سمت دیپلماسی
واشنگتن در حال حاضر برخی عملیات تهاجمی برنامه‌ریزی‌شده خود را متوقف کرده و به دنبال امکان آغاز مذاکرات با میانجیگری عمان است. این تغییر رویکرد پس از رایزنی‌های فوری با متحدان منطقه‌ای، به‌ویژه عربستان سعودی، صورت گرفته است؛ متحدانی که خواستار کاهش تنش برای حفاظت از دارایی‌های آسیب‌پذیر انرژی در خلیج فارس شده‌اند.
دولت آمریکا در این توقف تاکتیکی، دولت اسرائیل را نیز به شکل محسوسی در حاشیه قرار داده و ثبات در خلیج فارس را در اولویت قرار داده است.
با وجود گشایش دیپلماتیک، اختلاف اصلی بر سر تنگه هرمز همچنان حل‌نشده باقی مانده است. آمریکا خواستار آن است که این آبراه به‌عنوان یک مسیر بین‌المللی باز باقی بماند، در حالی که ایران بر حاکمیت مدیریتی خود و حق دریافت عوارض عبور تأکید دارد. اما تهران حاضر نیست از موضع ضعف وارد مذاکره شود و با استفاده از تهدید به گسترش اختلال اقتصادی تلاش می‌کند برای خود اهرم فشار ایجاد کند.
ری تاکیه، مشاور پیشین وزارت خارجه آمریکا، می‌گوید:
«اگر قرار باشد مذاکره‌ای انجام شود، ایران شرایط آن را تعیین خواهد کرد.»
در نهایت، رویارویی کنونی بیش از آنکه صرفاً یک تقابل نظامی باشد، آزمونی برای تاب‌آوری نهادی دو طرف است. ایران بر این باور است که ساختار داخلی آن می‌تواند تحریم‌های طولانی‌مدت را برای مدت بیشتری تحمل کند تا ائتلاف تحت رهبری آمریکا بتواند نوسان دائمی در تجارت جهانی و بازارهای انرژی را تحمل کند.
#ژئوپولیتیک</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SBoxxx/19647" target="_blank">📅 13:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19646">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای انفجاری در شهر صنعتی شمس‌آباد، واقع در جنوب تهران، خبر می‌دهند.</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SBoxxx/19646" target="_blank">📅 13:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19645">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HL_8L2XIvF1HO_BHAAljMEJ0OftdRJYf5z2eEBvAMoQ6VG6cbdzerAdjWXsAsTEwPUvZsWC4rZhiN7Xo69S_FrTNOky5vghDfQ6zFiPe-PvSgy-US1anG_MWsa2jEutPLIdiDNq1PMTNoGp40eaYAaz-f6qP8wvbFz2i02xZui6PNI8jmRvst0WSPx9W8KbbVMRVHl3SyWQ3L0BR72lFijobjfjP3DgJf_LugH5bhq5xJ1Ziw7QUDgYPmweIhaFIj88KvV-6YG2CGcFOETf08aNIaw8WB7fhm5zGFrO-GndS_m2XcVjWCgnxZQUz5aVpJi_CTUg9tQSRO6osI75uEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در حال احیای صنعت آمریکا است و این مسئله در گزارش درخشان دیروز PMI کارخانه ای آمریکا بازتاب یافت.  یادداشتی در این خصوص منتشر خواهدشد.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SBoxxx/19645" target="_blank">📅 13:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19644">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd1HANt58rQfxFAF_fBkEI8f0m8Ub-KpA3mzDRFbrXYtdEEDLASyOkg3k8YH0HZMSByZx2Oie4yUya86xIdkaj1RTERp5SQMBNODjk3g1C3VxWHqWtJrZynugHgb9oaO_JlvkExvY20nTzA8hUsJlYXVSXKHkJWrx3hkbcwp1peBt8QTd2Ia9G930vcVHDcxir2VuGFDILEeyLNzvXhS_n6FgqKPYFWpgkXxDx_DFNxWZkEVhGmS_0VXfUNRJb1t_NDKSHH1hH071L5TR62Cm5kIvXWUQfc1JNoP6WimTqf_J8iu_zd3TelSEirR88rBOff16NfCJGqpwUAq8e0jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Geomarkets Podcast Text.pdf</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SBoxxx/19644" target="_blank">📅 11:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19643">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbf3_f2vHKDt0DImDjEsMdZWn4_sDN_Ph8-3O9YeqTx1VreKD-MiephbIPRjolDUGeqvN-MmRXCqLsRuhcm8GmBcTgdK8jqnTsRN4w_1YC6cr1dwOrqARdPWk50TPndIMzvAoptmFDt_pW7fdludw5Zzr4VIjVNs6aBUPNmtDx9MqIzEE0GqqWBJSQh3pC5AeOIlQKz0wLj3b_k51zJXvyrErC_Aht_qrKqh-hHCvvHs6AO6Yhea5mL2fH425-WBkfcOkZ7Wd6sSNrWYM0GCY5hHE1k6eCOMRpUM_rkfpWTlM9xnoDWGFpjxxAtu7qEW7K_i4JF0h2mVsSRMZ2DZ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک امروز در سطح بالایی است. پس از رشد مناسبی که طلا از کف دیروز داشته، توصیه می شود امروز با احتیاط برخورد بشود و بالای 4090 اگر برود قطعاً محدوده فروش است.</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SBoxxx/19643" target="_blank">📅 11:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19642">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVLbjUXW7f2WgY6mgYerz4RIlklZpmVks_NvdE8U4p0eGTbqBYoHdrsHlAaQyvH3J7GXXKFYyrto1P2nILPxSMGTMJkCEMMfUQg5GOPPK03ZSqjl4NS3b9ent_rpFA9d2wcTttU4kyxEWii50_FJK7-4L1U29K91_NJG-8EPu_tsN_mYHP5CYwpP66WsUIVsAteIXi19GdMEnURefTT-InxC8gd_HYeZgbuAAxcy0QvMDg5QuaV2ce1Hj5G1lMnjJ66aVefx9RhHfvQKzujSf9cswXoxctRpjN_4fc50hwGj3DXl-56d2Wc3EEGncoqrQcJHrYeECM5sNeNRTspUhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا بخش تولیدی اقتصاد آمریکا در دوران ترامپ احیا شده است؟   داده‌های اخیر PMI نشان از رونق و رشد چشمگیر بخش تولیدی آمریکا در اوایل ۲۰۲۶ دارد که می‌تواند ناشی از سیاست‌های حمایتی و استراتژیک دولت ترامپ باشد.  با این حال، این بهبود به دلیل کاهش اشتغال و تغییر…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/19642" target="_blank">📅 10:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19641">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ایران و عمان به توافقی نزدیک شده‌اند تا پس از ماه‌ها اختلال، مجدداً تردد کشتی‌ها را از تنگه هرمز از سر بگیرند.
مهم‌ترین مسئله مورد اختلاف این است که این توافق پیشنهادی می‌تواند به ایران نفوذ بیشتری بر این آبراه بدهد.
مقامات ایرانی می‌گویند که کشتی‌هایی که وارد خلیج فارس می‌شوند، از یک مسیر نزدیک به ایران عبور خواهند کرد و هزینه‌ای را پرداخت می‌کنند که بین ایران و عمان تقسیم می‌شود. در مقابل، مقامات آمریکایی این ادعا را رد می‌کنند و می‌گویند که ایران هیچ اختیاری برای دریافت هزینه یا کنترل تردد نخواهد داشت.
منبع: نیویورک تایمز</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/19641" target="_blank">📅 10:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19640">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHt8aI8bPK94L5k3R7Ig8rQiz1J-ldOPhHdwHXL2CHcX-GStFSMUgiphCSRXXPYk8EQo3hyTxMd6m4rvginRzbM2tys3f4SLxLXB4rQna7mYI7329pM_csl2ORQ6zS32CgHHPIikDcQOOI1hkGlCWY0BQCstbFJ2tT6U00gcftu7CkWTMmsJyfiqEn8agsCaHh_aNg48g3YPtket6uEFlc6WFOOSEn7N2hiFQC7Zju9JSfTs9OJtbjI1yWokJBgrxltwYRtGqyDRbL5dL5vLOk7e4TwlulOG8q5vh_e11R3Q6Dz4Rv0TG-GRdTuGH5Jro83oErMXZkzcmaf-j-cNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/19640" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19639">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">#USOIL — H2  محسن رضایی: منتظر نفت ۱۵۰ دلاری طی روزهای آینده باشید.</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19639" target="_blank">📅 00:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19638">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6ah04-KedZ0zdO7G35ZMBcLT4QoJN7B5Q-RxiWoSYVb5iLG_Zx1JKy0etF3rhap_lISk_XmMwfwFHGt2WRR77w-Yjlx32TSkDoImmhh9huwvRzaoMXz0W8GlGKi8rtmsJAWkLiT3p9UpqRWLXkRK7J4F-eHOkjdnMmQVdRTUbJ85cP_DDiJZGqT6FvRJL1PqihajK6RRPj4ps0NhgWPSXM2yToA9nxJEzquc7cDg3ZL8RgcR0CLMTX8TdTzeN2Xg4b-yyFAurcmBRaFhaO0svdcUWlSqGie0O3O17aLkb17bqRvzz4TrpxiFZtXHnIJnFog-82FokGTiVU4Th1sxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#USOIL — H2  به نظر تارگت 2 را می شود دستکم 120 درنظر گرفت.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/19638" target="_blank">📅 00:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19637">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یک منبع آگاه به خبرگزاری رویترز:
ایران در 24 ساعت گذشته حداقل 3 پهپاد به سمت کشتی‌ها در هرمز شلیک کرده است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19637" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19636">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">در حال حاضر خورشیدگرفتگی روی نداده اما ماه کنار مریخ است.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/19636" target="_blank">📅 23:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19635">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ژنرال محسن رضایی:
در حال حاضر، هیچ آتش‌بسی وجود ندارد. اما تمام عملیات‌های ما هدف مشخصی دارند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19635" target="_blank">📅 23:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19634">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">برنامه داریم اسم جزیره قشم را بگذاریم آمریکا و آن را محاصره کنیم.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/19634" target="_blank">📅 22:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19633">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏ژنرال  محسن رضایی:   اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.  ‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد. ‎</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SBoxxx/19633" target="_blank">📅 22:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19632">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
ژنرال
محسن رضایی:
اگر محاصره دریایی ادامه پیدا کند حتما برای ناوهای دشمن خطرات جدی به وجود خواهد آمد.
‏درصورت عدم تغییر رفتار در آمریکا، نیروهای مسلح ایران هم دست روی دست نمی‌گذارند تا محاصره دریایی ایران ادامه یابد.
‎</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/19632" target="_blank">📅 22:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19631">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ژنرال محسن رضایی:
آمریکا در طراحی چهارم خود علیه ایران تلاش دارد از داخل شورش‌هایی انجام دهند
کشورهای دیگر را هم می‌خواهند وارد جنگ با ایران کنند!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19631" target="_blank">📅 22:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19630">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/19630" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19629">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:  من اجازه نخواهم داد که ایران این عوارض را دریافت کند.  اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.  ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/19629" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19628">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دونالد ترامپ در مورد چمن:
چمن مثل انسان‌هاست. آن هم زندگی دارد.</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/19628" target="_blank">📅 21:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19627">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اظهارات ترامپ درباره عوارض عبوری از تنگه هرمز:
من اجازه نخواهم داد که ایران این عوارض را دریافت کند.
اگر کسی قرار است این عوارض را دریافت کند، ما این کار را خواهیم کرد.
ما کنترل کامل را در اختیار داریم.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19627" target="_blank">📅 21:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19626">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منظور کله زرد از «این» چیست؟! وقتی مذاکره ای صورت نمیگیرد</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19626" target="_blank">📅 21:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19625">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19625" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19624">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین شانس آنها برای امضای یک سند خوب است.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19624" target="_blank">📅 21:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19623">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سوئیس: ما در ارتباط با ایران و ایالات متحده در مورد مذاکرات احتمالی هستیم -
خبرگزاری تسنیم</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/19623" target="_blank">📅 21:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19622">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PD4oOJ7LYUjDwvD1_3n4Mmh_7wONz9R24GaBViqIoAYa0BC6hN0VNOTMOKZR2D06wy0--Y-oqAYsdWCOeZ-NMrvXToGCm_L93iXmovkIs1mEZUxodfN2Ey3Z3l6fLVqANRrGSsQMAm5iAVjybgRz_PLYR-CNLerXtakkONN2-cSmGXMO5aTLn6jPTrqV3oKISl9E9T08I_I8jzokV_dHmNJY5zasaNLAwlGa4iwhJYKzx30LxHFVqzffTwZVxuiiVLNoQmj0WsUAfqDzne4jcwArswumZm0FtoQovfKxCAI_Ipg_FrzRZSa6bDEzJ6oYf6wbTYpWtphl9Fc97eRFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:   رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/19622" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19621">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ:
رهبران ایران به طرز باورنکردنی‌ای ریاکار هستند! آن‌ها درخواست ملاقات می‌کنند، برخی می‌گویند "تمنا می‌کنند"، مذاکرات آغاز می‌شود، و جلسات بیشتری در آینده نزدیک برنامه‌ریزی شده است، و در عین حال، به صراحت و با افتخار اعلام می‌کنند که هیچ بحثی در جریان نیست، هیچ موضوعی مورد گفتگو قرار نمی‌گیرد، و آن‌ها فقط با "عمان" در ارتباط هستند.
سپس، آن‌ها به سخنان همیشگی خود ادامه می‌دهند و ادعا می‌کنند که تنگه هرمز به طور کامل توسط آن‌ها کنترل خواهد شد، در حالی که در حال حاضر، این تنگه به طور کامل تحت کنترل نیروی دریایی ایالات متحده و "محاصره" ما، یا همانطور که برخی می‌گویند، "دیوار فولادی ایالات متحده" است.
هیچ چیز به ایران نمی‌رسد، مگر اینکه ما بخواهیم، و هیچ چیز نخواهد رسید، مگر اینکه یک توافق حاصل شود، یا ایران به طور کامل تسلیم شود. چه ایران این را بپذیرد یا نه، در واقع، ما در حال بررسی راه حلی برای مشکلی هستیم که آن‌ها برای دهه‌ها ایجاد کرده‌اند.
این موضوع بسیار ساده است: ایران هرگز سلاح هسته‌ای نخواهد داشت!</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/19621" target="_blank">📅 19:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19620">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پاکستان وجود هر گونه مذاکره ای میان ایران و آمریکا را رد کرد.</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19620" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19619">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تصویر نگران‌کننده بازار کار ایران.
بر اساس تازه‌ترین نتایج طرح آمارگیری نیروی کار مرکز آمار ایران، اقتصاد کشور در بهار امسال حدود
۴۵۰ هزار شغل
را از دست داده است. همچنین
۶۲۹ هزار فرصت شغلی در بخش صنعت
حذف شده و شمار قابل‌توجهی به جمعیت بیکاران افزوده شده‌اند؛ آماری که از تشدید بحران در بازار کار حکایت دارد.
﻿
همچنین مرکز افکارسنجی دانشجویان ایران (وابسته به جهاد دانشگاهی) اعلام کرده است که
معیشت بیش از ۳۲ میلیون ایرانی
به‌صورت مستقیم یا غیرمستقیم به پایداری اینترنت وابسته است؛ موضوعی که اهمیت دسترسی پایدار به اینترنت را در اقتصاد و اشتغال کشور نشان می‌دهد</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/19619" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19618">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نتانیاهو:
ما باید روابط خود را با متحدان بیشتری تقویت کنیم.
به همین دلیل است که من سرمایه‌گذاری زیادی در رابطه خود با هند انجام می‌دهم، با دوستم نارندرا، که یکی از بزرگترین دوستان ماست.
برخی می‌گویند اسرائیل منزوی است. اما حمایت‌هایی که اسرائیل – و من شخصاً – در هند دریافت می‌کنم، واقعاً شگفت‌انگیز است.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19618" target="_blank">📅 18:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19617">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو:
اکثریت قاطع مردم ایران، اسرائیل را تحسین می‌کنند.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SBoxxx/19617" target="_blank">📅 18:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19616">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Geomarkets Podcast Text.pdf</div>
  <div class="tg-doc-extra">324.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/19616" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - podcast 17</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/19616" target="_blank">📅 18:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19615">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">انفجار در دوبی همراه با یک کشته و 5 زخمی</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/19615" target="_blank">📅 17:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19614">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn5yG0QTyQ8IumWTlba_Z0D8cvV0hcJdJSSy1pqsz1zO9tfEZ9ixJ8Fz4M2a2qIphq_R2G1qIqc7jEVYYDTYZkRTM3jCbqnaLliguVcPUCo8EUCiLhqT6mgBVhNubl5tIN2_nMAhVHEPXXxKYYgbrBxWWPLTWfyzsOiNQsa_XB-lF-NAOK9XIw7TI7etUi7cnBmlsVra70UwOlF9jjfROoyZIM_dE_lcPhxLLrYOnPZfmZgr3CzMbuK0mJPQMANRIL6FBGJvFbtXXTp2TR274guyEVBe99Vb6shiTPm3oP8u9LsZmn-jTVGNQIHrSwaQG0MDQdv0KvIzROc0vmqriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
چرا بسته‌شدن 20 درصد صادرات نفت جهانی منجر به افزایش 80 درصدی درصدی قیمت شد؟
بسته شدن تنگه هرمز فقط به معنای حذف ۲۰ درصد از عرضه نفت نیست؛ بلکه ظرفیت مازاد تولید جهان را نیز از بین می‌برد و با از بین رفتن انعطاف‌پذیری بازار، حتی یک شوک محدود می‌تواند جهش بزرگی در قیمت نفت ایجاد کند.
علاوه بر این، بازار نفت ریسک‌های آینده مانند گسترش جنگ، اختلال در تأمین نفت جایگزین، محدودیت اوپک‌پلاس، مشکلات پالایش نفت سنگین و معاملات اهرمی را نیز پیش‌خور می‌کند؛ عواملی که مجموعاً جهش شدید قیمت‌ها را رقم می‌زنند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/19614" target="_blank">📅 17:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19613">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ:
مایک ویرث، رئیس هیئت مدیره و مدیر عامل شرکت شرون، همین‌اکنون در مصاحبه‌ای با ماریا بارتیرومو که فوق‌العاده است، تمام دلایل موفقیت شرکتش را بیان کرد.
تنها چیزی که او به‌طور مصلحت‌آمیز فراموش کرد ذکر کند این است که بدون نبوغ، دوراندیشی، قدرت و ثبات دولت ترامپ، صنعت نفت و خود کشور ما مرده بود!
به عنوان مثال، آن‌ها مایک و شرون را از ونزوئلا بیرون انداختند، اما اکنون آن‌ها بازگشته‌اند، بسیار بزرگتر و قدرتمندتر از هر زمان پیشین، و انتظار دارند ثروتی عظیم کسب کنند!
این موضوع برای سایر شرکت‌های نفتی نیز صدق می‌کند... و همین حالا قیمت‌های مصرفی (خرده‌فروشی) نفت را پایین بیاورید!
بابت توجه شما به این موضوع سپاسگزارم.</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SBoxxx/19613" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19612">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">المیادین:
ایران پیشنهاد بازگشایی تنگه هرمز تا پایان کامل جنگ را رد کرد.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SBoxxx/19612" target="_blank">📅 17:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19611">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گادی آیزنکوت در مورد ایران:  در مورد ایران، یک هدف برتر و دو هدف بسیار مهم دیگر وجود دارد. هدف برتر، حذف حدود ۴۴۰ کیلوگرم اورانیوم غنی‌شده از ایران است.  اگر این کار انجام نشود، ایرانیان می‌توانند با تصمیم خود، به سمت سلاح هسته‌ای پیش بروند. این چه معنایی…</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/19611" target="_blank">📅 16:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19610">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=gswtdVwsQjXppA6kkQcSHCcxsMO3N7bfXo4LrEJmgvvwUVBa-b4OtI4mwoPioF4pKJmCAtIAe8R1tyokltK5KRYb5ycNL2viAViDxEezYpPn_ZUm_t0i81Zg1KOxVD3K6yrXr_lB231mGHVZKdHGrqfNJ0w6u9pNdmnbqL4fkcSqrX4Wcj8Y_RtutW0HV81144EVhzMll601dP7dd1Zdj1NIJC28KWDA791XIAEB--12zkX1jFk1D16cJayXKGgV3nDyPhdqxMNILUP4S-B_8QiDgenZxRnLx5NDgrTUmZOIGa6Gi80IVLwJTUkjD0Eh-efuWt7E6FyCfRCQjdb0_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f6c5fe91f.mp4?token=gswtdVwsQjXppA6kkQcSHCcxsMO3N7bfXo4LrEJmgvvwUVBa-b4OtI4mwoPioF4pKJmCAtIAe8R1tyokltK5KRYb5ycNL2viAViDxEezYpPn_ZUm_t0i81Zg1KOxVD3K6yrXr_lB231mGHVZKdHGrqfNJ0w6u9pNdmnbqL4fkcSqrX4Wcj8Y_RtutW0HV81144EVhzMll601dP7dd1Zdj1NIJC28KWDA791XIAEB--12zkX1jFk1D16cJayXKGgV3nDyPhdqxMNILUP4S-B_8QiDgenZxRnLx5NDgrTUmZOIGa6Gi80IVLwJTUkjD0Eh-efuWt7E6FyCfRCQjdb0_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:  «ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/19610" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19609">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWQojgkSUxfcpMHFy3oOZSCr_B5__EltRp7wL8R6QKoJlYMtOonspKoIILqjX-UTsYi6gdiHzjh4jK9QejJz0T1HVG3GlJ6gc29hLaL7v9xP74VNDAiS_uRla8tyMfBOZF3PY3PZk6DZXsUvVNwyg2y5lQf3ilKiVDUVQeaEkDyIkrR3wCTlJK1bv0PcisHC_RO7W6wwU6xpNs8_Bh1q43tACcQk6QH1-crKaZ4kngBwa2wFtB_NdE-Lj2JZxbju_76OmKZvFHNsJjGpomqnxRzZNnBj1jSxg9nSU7YRQHi5FceUU77Ft4_p5e4vN1y7H35C_sPw4L9MV4T-mt95xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسناد فاش‌شده نشان می‌دهند که شرکت اسرائیلی "ال بیت سیستمز" (Elbit Systems)، فعال در زمینه تسلیحات، به دنبال انعقاد قراردادهای تسلیحاتی به ارزش تا 1.3 میلیارد دلار با امارات متحده عربی بوده است، که شامل پهپادهای پیشرفته "هرمس" و سیستم‌های اطلاعاتی می‌باشد.
منبع: هارتز (Haaretz)</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/19609" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19608">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:  در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.  گزینه‌های نظامی واقع‌بینانه در نظر گرفته…</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/19608" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19607">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">احمد الشرع (جولانی سابق) ، درباره محیط سیاسی پیش از عملیات ضد اسد:
در آن زمان، مردم تا حد زیادی امید خود را به شانس موفقیت انقلاب از دست داده بودند. ترکیه به دلیل مسئله پناهندگان سوری تحت فشار داخلی شدیدی قرار داشت.
گزینه‌های نظامی واقع‌بینانه در نظر گرفته نمی‌شدند. رویکرد غالب، آشتی با رژیم بود. اگرچه بسیاری از سیاستمداران ترکیه در کارآمدی آشتی تردید داشتند، اما این مسیر در حال پیگیری بود.
ترکها همچنین می‌ترسیدند که اگر یک تهاجم نظامی شکست بخورد، روسیه با حملات هوایی گسترده به مناطق تحت کنترل مخالفان پاسخ دهد و موج دیگری از پناهندگان را به ترکیه که خود با بحران پناهندگی روبرو بود، وارد کند.
حتی کشورهای عربی - به جز قطر - در حال پیگیری عادی‌سازی روابط با رژیم بودند. هدف تأیید آنچه اسد انجام داده بود نبود، بلکه دور کردن سوریه از نفوذ ایران و کاهش خسارتی بود که به منطقه وارد می‌کرد.
عملیات نظامی با وجود آن نگرانی‌ها آغاز شد. این کاملاً تصمیم خودمان بود.
منبع: الجزیره</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/19607" target="_blank">📅 15:14 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19606">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - podcast 17</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/19606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 17
دوشنبه 3 آگوست 2026</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/19606" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19605">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMnaZe9zz9KuyKVFDvMScQEDjapm1buLdsdIBz_HB8ae9A-CpySBHXTzVFN3sMiYoNRAy6XQID-b1Ccw7Dm0V20qoyHSXX7jP6eBZNa6iijoG67i0r-MMRO4UefNEPcypNgbNkabvtfTgCnqjTfMkWsj_NajSNWxHUE65PLqbOOJbCDF6CxRVribnKf4fLWojqm6RiThoZ0WG3y6RM_tfqGR2QZCkIKSTw4n6p3Y3CPc6GA7R_sfXZ3fdo2CeTpckZh-ouy2NtmL27zBf1rwpwcY-qCXB8ygdlxY3Xv4H3OZvHF-BLmkOHEEc0-f5FtB3oZiNR0a38_pYlUSfA1dBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رنکینگ مسخره ضریب هوشی کشورهای جهان را ناموسا رها کنید!
اگر میانگین ضریب هوشی ما واقعا چهارم دنیا بود باید سطح رفاه و توسعه اقتصادی ما هم دستکم در ۱۰ کشور برتر جهان قرار میگرفت (کشورهای دیگر صدر جدول را بییینید) نه اینکه رییس جمهوری مثل پزشکیان داشته باشیم که سطح ادراکش از توسعه برق این است که برود آستین کوتاه بپوشد و یک لامپ خاموش کند!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/19605" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19604">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هر وقت پاکستان میانجیگری میکند یک جایی ازشان منفجر می شود</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/19604" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19603">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">توضیحاتی درباره روند تکامل صنعت دفاعی اوکراین و پیآمدهای خطرناک درگیری با این کشور برای ایران  #ژئوپولیتیک   لینک مقاله مرتبط</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/19603" target="_blank">📅 12:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19601">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه‌های خارجی گزارش می‌دهند که یک مقام ارشد فرماندهی مرکزی ایالات متحده (سنتکام) هفته گذشته ایمیلی را برای گروه بزرگی از تحلیلگران ارسال کرد و در آن نوشت:
«ما به دنبال راه‌های جدید، نوآورانه و غیرمتعارف برای تحت فشار قرار دادن ایران و مجازات آن هستیم.»
این اقدام نشان‌دهنده درک این موضوع است که گزینه‌های موجود در حال حاضر برای دولت ترامپ محدود هستند و ممکن است از نظر سیاسی یا نظامی قابل قبول نباشند، که این امر ضرورت بررسی راهبردهای جایگزین را ایجاد می‌کند.
— کانال ۱۲ اسرائیل</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19601" target="_blank">📅 12:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19600">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_0CY7dLp5AWKp6d4fKE5HZI0PtDlk_ZQILqLAH9UvY8LOQQKn3vDOZpGCEsBSmO8_eoWiqWh1CrpIiM-A1wxXVH-CedgOr4H8545jeEjdWOHyTfdw-ze1uHziNNT-X9pNQ6ITHgc2Vosv58axOnQlrl2T6sLL7aQl8zSMLgUGjRYqqiMlCOQDSNWG5MOBVC6GdUD2IFNeWJxOWzBm8saQtAI9krg7VepAhr3dPiNzqQsemHL7zwC0laAFl-jqm9UoTDvPEpNDanzZ9fFKv_k-N-2H-2mxtBHNhrsFBjZyOu8XV9FQfn14bMxxEwZjGZ8ZfxEqb0roB46t8T1e2Uag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح بسیار پایینی قرار دارد و پیش بینی می شود که طلا رشد مناسبی (دستکم در حد 400 پیپ) را تجربه کند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/19600" target="_blank">📅 10:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19599">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.  این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19599" target="_blank">📅 10:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19598">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یک دادگاه اسرائیلی به طور موقت طرح وزیر امنیت ملی، ایتامار بن گویر، مبنی بر احاطه یک زندان را با تمساح‌ها را متوقف کرد. در این زندان عموماً اسرای فلسطینی نگهداری می شدند.
این تصمیم پس از آن اتخاذ شد که یک گروه مدافع حقوق حیوانات، این طرح را به چالش کشید.
منبع: i24</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/19598" target="_blank">📅 10:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19597">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ ادعا می‌کند مذاکرات آمریکا-ایران روز دوشنبه آغاز می‌شود
او‌ گفت:
«خب، کاری که الان انجام می‌دهیم این است که در قالب مذاکره با آن‌ها صحبت می‌کنیم. این کار فردا بعدازظهر آغاز می‌شود و خواهیم دید که آیا این واقعیت دارد یا خیر. من عاشق انجام این کار هستم،»
ایران این ادعاها را رسماً تأیید نکرده است.</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/19597" target="_blank">📅 02:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19596">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19596" target="_blank">📅 01:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19595">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا UKMTO از احتمال وقوع یک حادثه در آب های عمان خبر داد. گفته شده یک ناخدای یک نفت کش صدای انفجار شنیده است اما خود تانکر سالم و سلامت است.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/19595" target="_blank">📅 01:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19594">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ درباره ایران:
نمی‌دانید این حملات به کجا منجر می‌شوند. منظورم این است که آیا همسایگان ایران با هجوم مردم (ایران) به کشورهایشان غرق خواهند شد؟
یک فاجعه. اتفاقات بد زیادی می‌تواند رخ دهد.
من ترجیح می‌دهم توافق کنم. به دنبال کشتن مردم نیستم. مردم می‌میرند. بسیاری از مردم می‌میرند. ما نمی‌خواهیم این اتفاق بیفتد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19594" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19593">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ می‌گوید عربستان سعودی، امارات متحده عربی، قطر و ایران همگی از او خواسته‌اند حملات را لغو کند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19593" target="_blank">📅 01:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19592">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">محاصره اقتصادی | فعال شدن گروه های جدایی خواه</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19592" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19591">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کشته شدن مامور پلیس در درگیری با اشرار مسلح شادگان  ستوان‌سوم شهید «سینا سیاه‌نژاد»، از نیروهای حافظ نظم و امنیت، هشتم مرداد در جریان درگیری با اشرار مسلح و حادثه تروریستی در شهرستان شادگان استان خوزستان، حین انجام ماموریت به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/19591" target="_blank">📅 22:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19590">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سنتکام:
تا تاریخ 2 آگوست (و در راستای اعمال محاصره دریایی ایران)، فرماندهی مرکزی ایالات متحده (CENTCOM) مسیر 35 کشتی تجاری را تغییر داده است، 2 کشتی را غیرفعال کرده و 2 کشتی را بازرسی کرده است.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19590" target="_blank">📅 22:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19589">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترکیه با پیش‌بینی تشدید تنش‌ها، اقدامات کنترل مرزی را تشدید کرده و  مرز خود با ایران را با دیوار فولادی تقویت می‌کند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19589" target="_blank">📅 21:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19588">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:  مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.  در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است،…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/19588" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19587">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک دیپلمات ایرانی به روزنامه وال استریت ژورنال گفت:
مقامات ایرانی از آسیب‌پذیری‌های سیاسی ترامپ آگاه هستند و در صورت لزوم، به دنبال بهره‌برداری از آن هستند.
در صورتی که دیپلماسی به نتیجه نرسد، سپاه پاسداران انقلاب اسلامی در حال بررسی حملات پیش‌دستانه است، حتی اگر ایالات متحده حمله نکند.</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/19587" target="_blank">📅 20:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19586">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/SBoxxx/19586" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فردا یک صوتی مفصل درباره این داستان قدرت نظامی اوکراین و بحث زیرساخت ها خواهم داد.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/19586" target="_blank">📅 19:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19585">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.  بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19585" target="_blank">📅 18:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19584">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یک حمله انتحاری به ایستگاه پلیس کابال در منطقه سوات، ایالت خیبر پختونخواه، پاکستان، انجام شده است.
بر اساس گزارش‌های اولیه، چندین نفر از نیروهای انتظامی و غیرنظامی در این انفجار کشته یا مجروح شده‌اند.</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/19584" target="_blank">📅 18:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19583">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">با گند زدن عبدالصمد ونساوی در حوزه برخورد با جمهوری اسلامی، اکنون شانس روبیو برای پیروزی در رقابت های درونی نامزدی حزب جمهوریخواه برای انتخابات 2028 به 31% رسیده که بالاترین میزان تاریخی خود است.  در سوی مقابل شانس ونس ترنس به 39% سقوط کرده است.</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/19583" target="_blank">📅 17:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19582">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیروهای اسرائیلی در حال هدف قرار دادن ارتفاعات علی الطاهر در جنوب لبنان با بمب‌های آتش‌زا هستند.</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/19582" target="_blank">📅 17:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19581">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEFqX2uc0owmHS0Lq2Pb9SL5Vajbf-UKeWlHuqNvqRkhlOD3ZpYcHe1Y5iELgwBHL-TtJyWVdpm4fjMyWYWH_HA8oBtr9SiC8UmAomjEeZXPleE2zOABvrIpC1wzWTUkVdJUSTV4MnpfnNR9apr1Q47qXfva3J-mXapHFXDnWD82P7hvig61xItYWzeWI2SJLKyeQzY-yJIRDYqf3WreqkWJhWTZujH7IjSZWQTZJ2epVSo6qR1EUPfazQ-Ug6lzlkB4n5MnTjrWcHgBmAApk7baS5kuj4NhQDOz0m6siCOdZTL52BVmofAh-qud_7tXt49pjrroeqnYX0DXAZYrFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب پولیتیکی زده اند.  به نظرم مراکش — که بشدت در خط اسرائیل و آمریکا است — عامل اجرایی است. آمریکا و اسرائیل که هر دو با دولت چپگرای سانچز مشکل دارند به مراکش گفته اند این وحوش و و طیور را بفرست سمت اسپانیا؛   حالا 2 حالت پیش می آید:  — یا دولت سانچز با بی…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/19581" target="_blank">📅 15:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19580">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بسیار بعید میدانم جمهوری اسلامی بدون لغو محاصره دریایی، تنگه هرمز را باز کند، حتی اگر ورودی تنگه هم در اختیارش باشد.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19580" target="_blank">📅 13:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19579">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19579" target="_blank">📅 13:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19578">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:
حکومت ایران در طول جنگ سقوط نخواهد کرد.
مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.
تأکید باید بر این باشد: اقتصاد، اقتصاد، اقتصاد، اقتصاد. این چیزی است که در نهایت حکومت را سرنگون خواهد کرد.
به نظر من حکومت می‌تواند به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی این اتفاق بیفتد، ترس دیگر مانعی نخواهد بود. آن‌ها بیرون خواهند آمد، قیام خواهند کرد و حکومت را سرنگون خواهند کرد.</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SBoxxx/19578" target="_blank">📅 13:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19577">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxrZYNOn41E36AvzOKsm6kmk4cVOLdIt1DSQ6ZBS492wE6nDtlutyy9hfkrRpz2TQyzeZUhheuEWk6WG5yHXcQkZuuPOZ_9GQuhdATCK-gS7DNhylMkApihOHiasX1Snhru5dAC9CtUk4eG_-7pZSM2opaXhorovQvUBFepMToacG8Bbe4JbJ36IKqbHIfWeiJa-jgIYJ3pf5YikN9-WEsxLWvPyg5BbXBwMI9j0l9fR3ncUYc-2_0Z3sAI9lp1Cp7-FQ2y0YqjaCdUnNUISUzcav8pRKgoz8PqFkeLbAw9XBPRdBiPgcIo_W4ErvVWOJwAwjg7ZTcblJC6kx8iMrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">GeoMarket Podcast Text.pdf</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/19577" target="_blank">📅 13:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19576">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آکسیوس :    ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/19576" target="_blank">📅 11:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19575">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یعنی موج 2 اینقدر کوتاه بود؟!  سبحان الله!   همه 5 سانت و 10 سانت و ....</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/19575" target="_blank">📅 11:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19574">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نیروهای مقاومت بعد از اربعین پاسخ آمریکا را خواهند داد
علاءالدین بروجردی، عضو کمیسیون امنیت ملی و سیاست خارجی مجلس، با محکومیت شدید حملات بزدلانه ایالات متحده و عربستان سعودی به مواضع حشدالشعبی و موکب‌های عزاداری امام حسین(ع)، این اقدام را نشان از استیصال و ناتوانی نظامی دشمن دانست و گفت:
با وجود احترام به قداست ایام اربعین حسینی(ع)، پاسخ قاطع و متقابل به این جنایات در زمان مناسب و پس از پایان این مراسم مقدس، توسط نیروهای مقاومت انجام خواهد شد.</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/19574" target="_blank">📅 11:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19573">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">آکسیوس
:
ایران با طرح بازگشایی تنگه هرمز موافقت کرده است و قرار شده مسیر ورود از طرف ایران و مسیر خروج از طرف عمان باشد</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/19573" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19572">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/19572" target="_blank">📅 09:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19571">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ گفت که حمله دیگری به ایران را به تعویق انداخته تا مذاکرات به سرعت ادامه یابند.</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/19571" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19570">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">باراک راید از آکسیوس، با استناد به دو مقام آمریکایی و یک منبع دیگر، گزارش می‌دهد که محمد بن سلمان، ولیعهد عربستان سعودی، نگرانی‌های خود را نسبت به طرح دونالد ترامپ، رئیس‌جمهور ایالات متحده، برای انجام حملات گسترده علیه ایران ابراز کرده است.
بن سلمان در یک تماس تلفنی با ترامپ، درخواست جزئیات بیشتری درباره عملیات کرد و از او خواست که حملات را آغاز نکند.</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/19570" target="_blank">📅 03:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19569">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">حمله ایران به سلیمانیه و اربیل</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/19569" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19568">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این شرکت Fire Point، بجز موشکهای دوربرد فلامینگو، پهپادهای انتحاری دوربرد FP-1 را هم تولید می‌کند که اخیرا در حمله به تاسیسات نفتی روسیه عملکرد درخشانی داشته است.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/19568" target="_blank">📅 02:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19567">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دنیس اشتایلرمن، رئیس شرکت فایر پوینت، تولیدکننده موشک‌های «فلامینگو»، پیامی با تهدید علیه ایران منتشر کرد.  این تصویر، فلامینگوهای صورتی را نشان می‌دهد که در امتداد مسیری که اوکراین و ایران را به هم متصل می‌کند، پرواز می‌کنند و لوگوی شرکت و عنوان زیر آن آمده…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/19567" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19566">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تهدید یک نظامی اوکراینی به حمله به ایران با موشک های کروز فلامینگو</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/19566" target="_blank">📅 01:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19565">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">این بستن تنگه هرمز نهایتا باعث:  — ایجاد مسیرهای جایگزین  — تقویت تقاضا برای نفت آمریکا، کانادا و روسیه — تسریع در انقلاب انرژی سبز  خواهدشد</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/19565" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
