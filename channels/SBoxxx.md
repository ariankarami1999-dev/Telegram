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
<img src="https://cdn4.telesco.pe/file/EEYd5NW1G8miKwObW-FhR-PWt4cD3XvgYjEsGP3akvV8E28A39xM9wcSEhdLfIOVdbAZXj-lhTEwLIO7kW7fbqISQOVxUqtnDpfFNaFYrC6TsKGSTo_ropdtclJ0732rH7OqztYCs-7qB1974zdgHUHMe32Xep5rUHGOAFmp50ldMEiX8xvG5jwqLFurKYCZBbNJyTqcNd0UrE4f_0UIq8TYCKDlEP-Mio8Gq5ioCKmbIvO8kwSKbDhFRPYbQdYqCFEzKcFqyEPaioJ5nRFMw2Q_mHyrdvSwGPvGtRK3XHBNpJq1MNzmEDS7x1iUZqi3-mhBQ4GRzOlyF5EfTJjn6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-21271">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">عملاً همه دارند نفت صادر می کنند جز خودمان!</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/SBoxxx/21271" target="_blank">📅 11:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21270">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت…</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SBoxxx/21270" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21269">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط انرژی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYmwoyPK1ffpdKgypyCFZ67bgRS65Oi3Hv-j-KvF7vwDp7fMjvzNo3n5AxWrsHvvqU_SHONJTirVOgYzUYbsKJd3fyUEcLCz0p2tcjlD89O2W6j-W89oUtFL1rsYV01QygV_sq0rHv7tIBzsrJEQD0LPYVK0Q7O3Cp_9nG_DO0YqDH7pYLjmr8Str4G-5FkXha2FIM9Zqtsp1uLV6dtNiES8dfQoajPAxV9uRHVnejHgICIvbZFcBLg5CjzRm-uAHhMp5_kbjh72FTt39yeRrGU0DGnhffpU2R0wfrkxx8II5OtFgMpOs9IcH9K4CEL2kaz86FsUcal3kLMHi1Pstw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
جریان ۱۲ میلیون بشکه‌ای نفت در کریدور عمانی
🔹
موسسه HFI: افزایش صادرات نفت عربستان از مسیر شرق می‌تواند جریان نفت در کریدور عمان را به ۱۲ میلیون بشکه در روز برساند که در نگاه اول می‌تواند نشانه عادی‌شدن تردد نفت در منطقه تلقی شود.
🔹
بخش قابل‌توجهی از نفت عربستان در این جریان راهی چین می‌شود.
@khate_energy</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/SBoxxx/21269" target="_blank">📅 11:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21268">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سراج، نماینده مجلس: حرف‌های عراقچی و پزشکیان درباره هسته ای و کوتاه آمدن از قصاص قاتلان رهبری بی‌اساس است و ربطی به سیاست جمهوری اسلامی ندارد
آمریکا می‌داند پزشکیان و عراقچی تصمیم‌گیر نیستند و محلی از اعراب ندارند
سخنان عراقچی صرفا اظهارنظرات خود اوست و هیچ اعتباری ندارد
اجرای انتقام و قصاص ربطی به دولت ندارد که نظر مثبت داشته باشد یا منفی
محمد سراج، نماینده تهران با اشاره به موضع گیری های مکرر پزشکیان و عراقچی درباره شرط ۷ روزه و باز کردن تنگه هرمز و رقیق سازی اورانیوم به دیده بان ایران گفت: « صحبت های آقایان عراقچی و پزشکیان در خصوص کوتاه آمدن از سیاست های نظام نظر شخصی بوده و نظر جمهوری اسلامی نیست. نظر جمهوری اسلامی ساز و کار خود را دارد و در سیاست کلان خارجی رهبری تعیین‌کننده هستند و در سایر موارد نیز مجلس و قانون مجلس مبنا قرار دارد. در حال حاضر محسن رضایی، دبیر شورای عالی‌ امنیت ملی سیاست کلان خارجی جمهوری اسلامی را بیان کرده است.»</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/SBoxxx/21268" target="_blank">📅 11:36 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21267">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">طلا تارگت روز جمعه را زد (ما زودتر کلوز کرده بودیم)  امروز اما اندک اندک وقت خرید است و کل این مسیر ریزش را برخواهدگشت.  بازار جنگ را کامل دارد پیشخور می‌کند اما ناوهای هواپیمابر آمریکا هنوز نرسیده اند و آرایش جنگی تکمیل نشده و عباس آقا سعد اکبر هم هنوز برنگشته!…</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/21267" target="_blank">📅 10:11 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kizhm3pkW_MNB8iilvrMjYNNhJkYJqSHBM6ySw2SFv_tFJ1f5IjDVe52xQ3m5rIBKqLMRtp2Zd7eLVCujPfLqUKp-ns4CBm0b082Iq96rfC3VpTiTgEIeygheDE4iys9xi1nXUlNzzRhzCIkt_Y0dSB8uOzcAZ5y9_lsV13Hza9iOyvfMDfzzPg1e7xBYtIh2ezf39rSf11ynPYTbLq1MYExH9JDm1tRXyw_cHlT3156XK5NuecABviJMAOJG1CoDNpuy3uuseADWq1qntuHncINMcMC4w4YgRd_JcSqB-_VSOyE34GXbl1fgfMMiDiFRyXE2zHU-IzZZuqJwpB01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/21266" target="_blank">📅 09:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVw5sHF1gFFqOKy4_0-szWSB22FeuFReLvny6x8hDw6lE16wmqQzeWXfJvlV9hNwv958YNYFHv130ij90BCXSWs91hcZaKKStzrWfNWsZJqwyAn09F5W7iugG7s43qX1yc0pCt86R8YDgAt6XzxTyfHNSmOztC_SbdSQenLphbJm6T6GSYiuuZcumvCouo9UW5mI9LaXUBgqFkNg1o185Y_b9aB6ClJ-tvx3cgGPXJgWQJNNdXaI0jKeW7XvIb7urLCfoGlxuyZWWO4PHKJ18c6st5acAkqsAsW_U5zmFOccoVUnPlUGyhM3PKJKGK7bsCfnPs6kP7E0xj7DuRejsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC نیز به کف محدوده بیش—فروش رسیده و خرید توصیه می کند.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/21265" target="_blank">📅 09:29 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21264">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdRDRcQxsh-d19c1dsWW0sVVP5uO4dKt2yi-g2ZZrV7_NX7tB8sqhlaLoUEe-IfT9QpKGWwhBWCp7wBdCaASzhY5TWwatmPaclrWQpfZn6dWbbtld7YgY8Md0j-xsAZbAuhsbYo6kMltJMB1n_maJTeVjRb9mOO1qIOWlpWosOj_3ZIZcek8Y8Obiu3jNBBR5F4ha-pIw8y-cO77z0N-6SovaOkF7UAHrEmesdcGhV04jmvA8J0ET0KkAIuocQresIqY0pEoGz5l3QnrquFSdok0cGB9Y2Ug9skWnG3Ffi0SJKzaC2EehfssuU9WbSHo0eUokSjCZam7-wmwUeQY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح پایینی است و از دید این شاخص، واکنش بازار به تنشهای هرمز مقداری افراطی بوده است.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/21264" target="_blank">📅 09:28 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21263">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3PI4_RSX40-u5zsF4vq4GK3UMUXS05ISw5ax6ixuUR6aJlSCUIOqL3XjmJ9uIKIEbqL993YgsNEKk74sED4paQvc2Mou0vZVTeDNx4CovO_rCcVaO21uhHkB_UMGF7GRxaq0ZsPrD528scKs2Mzn8aafIQ4xmHdqt_6pdw238JcSQYwk_e7EIypviaCHVs1ZUALTOmmDOuttGTJGX3bHS_k50mCg8_tdFKgG10FTiJCeXhqfaH4z07fVzwg3WsPi0rBv7wgVlNCMNhGws0DZcwTO75mZBHNzCBE8uUKLe6dJ_hpqTWNP-MRl6nyjd8wOJvlAk_xTkxiRcyi5UPnHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ژاپن بزودی بدجور موی دماغ چین خواهدشد.</div>
<div class="tg-footer">👁️ 3.24K · <a href="https://t.me/SBoxxx/21263" target="_blank">📅 08:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21262">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">جنگ ایران و بن‌بست فزاینده آمریکا؛ از بحران انرژی تا تغییر موازنه خلیج فارس
بر اساس دیدگاه‌های مطرح‌شده توسط جان مرشایمر نویسنده پرآوازه کتابها و مقالات ژئوپولیتیک، جنگ ایران و آمریکا وارد مرحله‌ای از بن‌بست شده است. از نگاه او، آمریکا تاکنون به اهداف اولیه خود دست نیافته و در عین حال ایران نیز حاضر نیست بدون دریافت امتیازات قابل‌توجه از جنگ خارج شود. تهران به‌جای تلاش برای شکست نظامی آمریکا، به دنبال افزایش هزینه‌های جنگ و فرسایش توان اقتصادی و سیاسی واشنگتن است؛ به بیان ساده‌تر، راهبرد ایران «دوام آوردن تا فرسوده شدن طرف مقابل» است.
یکی از مهم‌ترین اهرم‌های ایران، موقعیت آن در تنگه هرمز و پیوند آن با تحولات دریای سرخ و باب‌المندب است. اختلال در مسیرهای اصلی انرژی باعث افزایش قیمت نفت، سوخت، حمل‌ونقل و مواد غذایی شده و فشار تورمی را به اقتصاد جهانی منتقل کرده است. هم‌زمان، جنگ میان حوثی‌ها و عربستان نیز جریان صادرات نفت عربستان از مسیر دریای سرخ را با اختلال مواجه کرده است. مرشایمر می‌گوید ظرفیت عملی خط لوله عربستان به دریای سرخ پیش از حملات حدود ۴ میلیون بشکه در روز بود، اما پس از آسیب به ایستگاه‌های پمپاژ، جریان آن به حدود ۱.۶ میلیون بشکه در روز کاهش یافته است.
این وضعیت برای اروپا اهمیت ویژه‌ای دارد، زیرا هم‌زمان با کاهش عرضه نفت، بازار جهانی گازوییل نیز تحت فشار قرار گرفته است. روسیه صادرات گازوییل خود را محدود کرده و آمریکا نیز درباره محدود کردن صادرات گازوییل بحث می‌کند. از دید مرشایمر، تداوم این روند می‌تواند فشار قابل‌توجهی بر اقتصاد اروپا و اقتصاد جهانی وارد کند.
محدودیت گزینه‌های نظامی آمریکا
مرشایمر معتقد است آمریکا گزینه نظامی مؤثری برای دستیابی به پیروزی در ایران در اختیار ندارد. به گفته او، جنگ هوایی اولیه که از ۲۸ فوریه تا ۸ آوریل ادامه داشت نتوانست اهداف آمریکا را محقق کند و یکی از محدودیت‌های مهم واشنگتن، کاهش ذخایر تسلیحات پیشرفته و گران‌قیمت است. بنابراین، تهدید به حمله گسترده پس از انتخابات میان‌دوره‌ای لزوماً به معنای وجود یک راهبرد جدید برای پیروزی نیست.
همین محدودیت درباره حوثی‌ها نیز مطرح است. عربستان چند بار از ترامپ درخواست کمک کرده، اما آمریکا از ورود مجدد به جنگ با حوثی‌ها خودداری کرده است. استدلال اصلی این است که چنین جنگی می‌تواند منابع تسلیحاتی محدود آمریکا را مصرف کند، بدون آنکه تضمینی برای دستیابی به یک پیروزی پایدار وجود داشته باشد.
فشار اقتصادی و راهبرد تحریم‌ها
راهبرد اقتصادی آمریکا برای تحت فشار قرار دادن ایران نیز، از نگاه مرشایمر، با محدودیت روبه‌رو شده است. طرح وزیر خزانه‌داری آمریکا، اسکات بسنت، بر تشدید فشار اقتصادی و اعمال تحریم‌های ثانویه علیه کشورهایی استوار است که با ایران تجارت می‌کنند. اما چین، روسیه، ترکیه و امارات حاضر نیستند به‌طور کامل از تجارت با ایران خارج شوند. بنابراین، ایجاد یک محاصره اقتصادی کامل بسیار دشوار است.
چین در این میان نقش کلیدی دارد. طبق ادعاهای مطرح‌شده در مصاحبه مرشمایر، چین بخش بزرگی از نفت ایران را خریداری می‌کند و از طریق شبکه‌های تجاری و مالی به تهران کمک می‌کند فشار تحریم‌ها را دور بزند. همچنین ادعا شده است که چین در زمینه تجهیزات نظامی و ارتقای توان پهپادی و موشکی ایران نیز کمک‌هایی ارائه کرده است.
در نتیجه، فشار آمریکا علیه ایران صرفاً یک رویارویی دوجانبه نیست و به رقابت گسترده‌تری میان آمریکا، از یک سو، و ایران، چین و روسیه از سوی دیگر تبدیل شده است.
نفت و خطر تشدید بحران جهانی
یکی از نگرانی‌های اصلی، کاهش توان اقتصاد جهانی برای جذب شوک نفتی است. ذخایر استراتژیک نفت آمریکا در این مصاحبه حدود ۲۸۵ میلیون بشکه عنوان شده و کاهش بیشتر آن می‌تواند توان واشنگتن برای مقابله با شوک‌های بعدی را محدود کند. چین نیز که در آغاز جنگ واردات نفت خود را به‌شدت کاهش داده بود، اکنون دوباره واردات خود را افزایش داده است؛ بنابراین یکی از مکانیسم‌های اولیه برای کاهش فشار بازار نفت در حال ضعیف شدن است.
اگر صادرات عربستان نیز همچنان مختل شود، فشار بر بازار جهانی نفت می‌تواند بیشتر شود. در چنین شرایطی، اثرات جنگ دیگر محدود به ایران و آمریکا نخواهد بود و می‌تواند از طریق انرژی، تورم، زنجیره تأمین و هزینه حمل‌ونقل به اقتصادهای مختلف منتقل شود.
مرشایمر هشدار می‌دهد که در صورت ادامه جنگ، خطر رکود شدید جهانی افزایش می‌یابد؛ هرچند خودش تأکید می‌کند که نمی‌تواند با قطعیت پیش‌بینی کند بحران تا چه اندازه عمیق خواهد شد یا آیا به یک رکود جهانی بسیار طولانی منجر خواهد شد.
تغییر محاسبات کشورهای خلیج فارس
یکی از پیامدهای مهم جنگ می‌تواند تغییر محاسبات امنیتی کشورهای عربی خلیج فارس باشد. اگر این کشورها به این نتیجه برسند که آمریکا در شرایط بحرانی حاضر نیست مستقیماً از آنها دفاع کند، ممکن است به دنبال ترتیبات امنیتی مستقل‌تر بروند.
مرشایمر معتقد است عربستان و سایر کشورهای خلیج فارس ممکن است به سمت نوعی تفاهم با ایران حرکت کنند، زیرا اتکا به آمریکا، پاکستان یا ترکیه الزاماً نمی‌تواند یک چتر امنیتی پایدار ایجاد کند. در این چارچوب، کاهش تنش مستقیم میان ایران و کشورهای عربی می‌تواند به یکی از گزینه‌های مهم آینده تبدیل شود.
خطر مسابقه هسته‌ای منطقه‌ای
یکی از مهم‌ترین پیامدهای بلندمدت جنگ، از دید مرشایمر، افزایش انگیزه کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای است.
در این تحلیل، اگر ایران به این نتیجه برسد که سلاح هسته‌ای تنها راه تضمین بقای حکومت و جلوگیری از حملات آینده است، فشار برای حرکت در این مسیر افزایش می‌یابد. همین منطق می‌تواند عربستان را نیز به دنبال کردن یک گزینه هسته‌ای سوق دهد و در مرحله بعد کشورهای دیگری مانند ترکیه، مصر و عراق را نیز تحت تأثیر قرار دهد.
این مسئله یک تناقض مهم ایجاد می‌کند: جنگی که هدف یکی از طرف‌های آن جلوگیری از دستیابی ایران به توانمندی هسته‌ای بوده، ممکن است در صورت شکست مذاکرات، انگیزه ایران و حتی سایر کشورهای منطقه برای دستیابی به بازدارندگی هسته‌ای را افزایش دهد.
پیامدها برای اسرائیل
در این روایت، جنگ الزاماً به تحقق اهداف اسرائیل نیز منجر نشده است. یکی از نگرانی‌های اصلی اسرائیل، جلوگیری از دستیابی ایران به سلاح هسته‌ای بوده است؛ اما ادامه جنگ و فروپاشی مسیر مذاکرات هسته‌ای می‌تواند احتمال دستیابی ایران به چنین ظرفیتی را افزایش دهد.
هم‌زمان، توان موشکی و پهپادی ایران به‌عنوان یک تهدید مهم برای اسرائیل و کشورهای خلیج فارس مطرح شده است. همچنین جنگ نتوانسته پیوند ایران با گروه‌های متحد منطقه‌ای خود را از بین ببرد و حتی از دید مرشایمر ممکن است این پیوندها را تقویت کرده باشد.
جمع‌بندی
تصویر کلی ارائه‌شده در این مصاحبه، جنگ ایران را نبردی می‌داند که در آن مسئله اصلی دیگر صرفاً توان نظامی نیست؛ بلکه زمان، انرژی، اقتصاد، ذخایر تسلیحاتی، انسجام ائتلاف‌ها و تحمل سیاسی به عناصر اصلی قدرت تبدیل شده‌اند.
در این چارچوب، آمریکا با سه مشکل هم‌زمان مواجه است: دشواری دستیابی به پیروزی نظامی، محدودیت در ایجاد محاصره اقتصادی مؤثر و افزایش هزینه‌های جهانی جنگ. در مقابل، ایران می‌تواند از موقعیت جغرافیایی خود، به‌ویژه در ارتباط با هرمز، و از حمایت یا همکاری چین و روسیه برای افزایش قدرت چانه‌زنی خود استفاده کند.
اگر جنگ ادامه پیدا کند، مسئله فقط آینده ایران و آمریکا نخواهد بود. بازار جهانی انرژی، اقتصاد اروپا و آسیا، امنیت کشورهای خلیج فارس، روابط آمریکا با متحدانش و حتی آینده رژیم منع اشاعه هسته‌ای در خاورمیانه می‌تواند تحت تأثیر قرار گیرد.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/21262" target="_blank">📅 08:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21261">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتجارت کشاورزی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_7Hr6og970N2By6FARGav-WATvRr-j2kGpRUDzRV9OJmtfuCp1xd9HS4AdhKO-mEQm2q9-KXvUIW2ryctT7H4b_RxoD23fIBzEOl6ffGuwqc39gqluOsvNEuBiMynaSgrf_JjpDOMY4WWDdn6qNLQA80abD7qqRZUNNLQL3QlqO97JMmA8pjjkNJ5bQwTqoLtakWF6AJhUD11dgPkqVjt9x-w9u0f6jvMoqdAhCmS9Fy71Uxrh2JmHWQ7IIP9AaUSLHxxMBxsHxTGhKlIfhmYYeetwR9eGZRBrwf7yCr-e3wo-meCQvk1ZeHig38oW3TXP0-i2T_BvFUIgPYPsDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابلاغیه دولتی
به اطلاع کلیه بازرگانان محترم می رساند
دولت الزیدی تا پایان هفته آینده مهلت داده است تا کالاهای وارداتی جمهوری اسلامی ایران به بازار عراق انتقال یابند.
پس از انقضای این مهلت صرفاً دو گزینه در دسترس خواهد بود ۱-پرداخت مالیات مضاعف بر کالاهای مذکور
۲- منع كامل ورود کالاهای ایرانی به خاک عراق
⚠️
این تصمیم در راستای اجرای مفاد مشارکت جمهوری عراق در تحریمهای ایالات متحده آمریکا علیه جمهوری اسلامی ایران اتخاذ گردیده است.</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SBoxxx/21261" target="_blank">📅 08:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21260">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SBoxxx/21260" target="_blank">📅 07:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21259">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پنتاگون مصدوم شدن ۸ تفنگدار دریایی آمریکا در حمله موشکی ایران را پنهان کرد
به گزارش NBC News به نقل از ۳ مقام آمریکایی، ۲ هفته پیش زمانی که یک موشک کروز ایرانی به شناوری که تفنگداران دریایی آمریکا در تنگه هرمز در آن مشغول به کار بودند اصابت کرد، ۸ تفنگدار دریایی مجروح شدند.
وزارت دفاع هیچ حمله‌ای در تاریخ ۱۴ سپتامبر علیه نیروهای آمریکایی در منطقه را فاش نکرده بود.
موشک کروز ضدکشتی ایران به شناور دریایی که تفنگداران دریایی در آن مستقر بودند اصابت کرد
🔴
تفنگداران دریایی — ۷ سرباز و ۱ افسر — دچار استنشاق دود و احتمالاً آسیب‌های تروماتیک مغزی شدند که علائم ضربه مغزی از جمله سردرد را شامل می‌شد. آن‌ها بخشی از یک تیم پیاده‌سازی گردانی بودند
مقامات از تعریف نوع کشتی خودداری کرده و آن را تنها یک «شناور دریایی» نامیدند
در حالی که ایالات متحده در حال خارج کردن دارایی‌های خود است و ذخایرش بیشتر تخلیه می‌شود، گزارش‌های مربوط به تلفات آمریکایی‌ها همچنان ظاهر می‌شوند — و همچنان کمتر از مقدار واقعی گزارش می‌گردند.</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SBoxxx/21259" target="_blank">📅 07:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21258">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دلار دوباره نزدیک ۲۴۰</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21258" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21257">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">خبرنگار CBS:   مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد  مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21257" target="_blank">📅 00:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21256">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار CBS:
مذاکرات روز دوشنبه بین ایران و آمریکا لغو شد
مارگارت برنان، خبرنگار سی‌بی‌اس نوشت: یک دیپلمات که در جریان مذاکرات قرار دارد به من گفت آمریکا روز پنجشنبه پیش‌نویس ایران را بررسی و آن را همراه با بازخورد و ملاحظات خود بازگردانده است.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21256" target="_blank">📅 22:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21255">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بنیامین نتانیاهو دستور داده است که یک تیم بین‌وزارتی و مقامات حقوقی پرونده‌ای علیه رجب طیب اردوغان، رئیس‌جمهور ترکیه، در دادگاه کیفری بین‌المللی (ICC) آماده کنند.
پرونده پیشنهادی عمدتاً بر «رفتار ترکیه با جمعیت کرد خود» و ادعاها مبنی بر اینکه دولت اردوغان حماس را تأمین مالی کرده، تمرکز خواهد داشت.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21255" target="_blank">📅 21:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21254">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">به نظر من جمهوری اسلامی بزودی گزینه آخرالزمانی حمله به چاههای نفت و تاسیسات انرژی منطقه را فعال خواهدکرد که در پی آن نفت به بالای ۱۳۰ دلار و طلا به زیر ۴۰۰۰ دلار خواهندرفت.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21254" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21253">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">عراقچی:  ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21253" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21252">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عراقچی:
ما برای جنگ آخرالزمانی آماده هستیم</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21252" target="_blank">📅 20:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21251">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا ایران با طرح ناکام‌مانده حمله به پایگاه هوایی در پایگاه نیروی هوایی سلطنتی فیرفورد (RAF Fairford) ارتباط دارد یا نه.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21251" target="_blank">📅 19:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21250">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=HVfhI9w2D_5IxtieLCXXU67LGk1jP_H2mSouoTK1FGBPQMhdB7QFcXE5nlCFKJmXVFIrkURGxvX6nl4UIlR46Zd9xURwtyc-SOvfpYFe9EP8cfFaHKocH19hJ4olczRCsUIvyuaNbL9W5KyH6Ks6GkP7tDooB8-E-R_bQIVsk-zaLoPrh3s0zxZ1Kt9TfFmrRBXUNEUrTA7_t_YFMvEMPPc0WS6pq_lGUFgPB6D4Iz5D1enLD2iCteb47rHYfgc7TttXVqE3hs1gRBwSIVX5HAP1JtpOQR9jrgZ_eDzlb3AIpp5QEsf975PdcvJQDR0a-GofutegwC8ysKCI1lny1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904c5f3c14.mp4?token=HVfhI9w2D_5IxtieLCXXU67LGk1jP_H2mSouoTK1FGBPQMhdB7QFcXE5nlCFKJmXVFIrkURGxvX6nl4UIlR46Zd9xURwtyc-SOvfpYFe9EP8cfFaHKocH19hJ4olczRCsUIvyuaNbL9W5KyH6Ks6GkP7tDooB8-E-R_bQIVsk-zaLoPrh3s0zxZ1Kt9TfFmrRBXUNEUrTA7_t_YFMvEMPPc0WS6pq_lGUFgPB6D4Iz5D1enLD2iCteb47rHYfgc7TttXVqE3hs1gRBwSIVX5HAP1JtpOQR9jrgZ_eDzlb3AIpp5QEsf975PdcvJQDR0a-GofutegwC8ysKCI1lny1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21250" target="_blank">📅 19:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21249">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVgWFQ1DrS4PT3SaUs0N_l-NVsjnYcdKJ5STIhGPhUxJLnMXXiZmhewkzQEhJZ3arWFo81j-grA2oVh7L2Z5bLI-Ij1GSxAw2wnZxOdZVBqc2jNfENdXpHo1YHv7GZ7cghvdk1DO6sj8A54vL-tkNy7oZliEN1DIt7PDDMd_EnRdHNsHk4Lz6yfD_g8IcZKelOf-kfwInl9KeTRbnkZ_v3foBIy9tkezotu22L8oqtseXBH7bFEuLSL0HVeVgRLxaeUPdhBC06rmrKPymYKgiHWs3yBriSaVchRwdOk0abTiQ-egDHDcEvxLAZqZu0JwuCOjbkPdx4cr51wxIdlX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21249" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21248">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد.</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/21248" target="_blank">📅 19:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21247">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حرف درستی است. به این پفیوزها گاز و برق ندهید دستکم خودمان اینقدر قطعی نداشته باشیم.
زیبنده ابرقدرت چهارم دنیا نیست.</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/21247" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21246">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAavkaRflUzB_LufEr-SFWegQmqPEwfiGCEWGUWlQzRSQ4wd7B2lrGY5f_NsNV12QqByjrNoWU4iIoEqGCeo3UaPgX7o-dQoEQf8UaAinvS2XrsyVE0_iqAKhlL-D31QRpiDClBMQWQA9bpImGUiGBpBsGZQ4I6yOTsLSpgVZFLZM2c3azzY4KYJL2Kupe_tz3XY3tQW1JIvpEeKOeFx21rIY1sLu8TmTRKoabuCSAeh_hfTHQBB_lr9qTzAWmpWIMBPcua0fLc5CQKzY3YN4clavb8oPcyYB_qDePZbJ7R5z14Hd7qx7bnvj0nAA5zqog6nTJigCbCyO4Q5zB7LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران انقلاب اسلامی ایران امروز مدعی شد که یک پهپاد زیرآبی خودکار ساخت آمریکا به نام Remus 600 را در نزدیکی تنگه هرمز به دست آورده است. نام‌گذاری نظامی این وسیله توسط ارتش آمریکا، Mk 18 Mod 2 Kingfish است.</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/21246" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21245">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رابرت کیوساکی (Robert Kiyosaki)، نویسنده کتاب «پدر پولدار، پدر بی‌پول»، به دارندگان حساب‌های بازنشستگی هشدار داد که ممکن است فروپاشی‌ای در مقیاس سال ۱۹۲۹ در راه باشد، و بیش از یک سال بعد، این فروپاشی رخ نداده است.
کیوساکی در ژوئیه ۲۰۲۵ در ایکس نوشت: «آیا حساب 401(k) یا IRA دارید که پر از سهام است؟» او به وارن بافت (Warren Buffett)، رئیس برکشایر هاتاوی (Berkshire Hathaway)، و جیم راجرز (Jim Rogers)، هم‌بنیان‌گذار صندوق کوانتوم (Quantum Fund)، اشاره کرد و مدعی شد آن‌ها بیشتر یا همه سهام و اوراق قرضه خود را فروخته‌اند و پول نقد یا نقره نگه می‌دارند. او افزود: «اگر نمی‌دانید چرا بافت و راجرز سهام و اوراق قرضه‌شان را فروخته‌اند، ممکن است بخواهید علتش را بفهمید.»
او جایگاه خود را متفاوت توصیف کرد. کیوساکی نوشت: «من محکم روی طلا، نقره و بیت‌کوین می‌نشینم» و سپس افزود: «ممکن است در آستانه فروپاشی دیگری مانند ۱۹۲۹ و رکود بزرگ دیگری باشیم.» او همچنین هشدار داد که بدهی آمریکا از کنترل خارج شده است و این کشور فقط «تا مدت محدودی» می‌تواند به چاپ پول ادامه دهد.
البته این پیش‌بینی محقق نشده است. شاخص S&P 500 به صعود خود ادامه داده و در سال ۲۰۲۶ به بالاترین سطح تاریخی رسیده است، نه اینکه فرو بپاشد.
کیوساکی همچنان درباره سهام، صندوق‌های قابل معامله در بورس (ETF)، صندوق‌های سرمایه‌گذاری مشترک، حساب‌های 401(k) و IRA هشدار می‌دهد و در همان حال طلا، نقره و بیت‌کوین را تبلیغ می‌کند. استدلال اصلی او ثابت مانده است: سرمایه‌گذاران نباید صرفاً به این دلیل که دارایی‌های سنتی آشنا هستند، فرض کنند که امن‌اند.
تمایز مهم، میان آماده شدن برای یک رکود و تلاش برای زمان‌بندی دقیق وقوع آن است.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21245" target="_blank">📅 19:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21244">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHV-r2tvwe-sL6eB5kenkfdG6Ki_urNBKyDNDdP9WSTdiojFQWgwsjq_MNirbg1Okrt437tIsKUJvuq4go_bNO9BkW0pNN1kmUJlC1q4libA84KTe2WI33XxCdce6517tqzKXP6pMs4RX3aGUPdb0GMDwTPiGJ9r96_krE2PeTQQrbQJ_JHE0OdHsao2Q6_ryWtzKCy0m0pRVZ21HADMdkR3SCpdP3YLIYeFs-gkRhvIFJZybPRRx900g3vK34KeFeACciXAIVxQ8GXJUjgdWsPRRBTFivzHuV_UQAV68HT16z4AyQuQ5Aem0VvwBXNNhfLTS32e6v_v88O5VuWSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21244" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21243">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:  ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس  نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21243" target="_blank">📅 13:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21242">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حاجی‌بابایی، نماینده مجلس:
ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
نایب رییس مجلس با بیان اینکه امروز مقاومت با محوریت ملت بزرگ ایران تازیانه الهی بر فرق ترامپ جنایتکار است، گفت: تنگه هرمز همان دریا و همان رودی است که فرعون در آن غرق شد؟ آیا آمریکا در منطقه و در تنگه هرمز در نبرد با ملتی که خدایی فکر می‌کند و توحیدی فکر می‌کند غرق نخواهد شد؟ دیپلماسی با قدرت امکان‌پذیر است و ما باید حرفمان را از قدرت و اقتدار و جایگاه قدرت اقتدار بزنیم.</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21242" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21241">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">باز هم تاکید میکنم خواهرمیانه جای مبتدی ها نیست :
حکم ۱۰ ماه زندان حمید رسایی اجرا می‌شود</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21241" target="_blank">📅 12:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21240">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScUms17CSfnYbcTltKbAh8Pk2Jjzqffki50Am8cAwj6I5OBGbzmh4gankdP8-eRGSNXIVEnDqE1MBXk5kzsnoBTTQQYyboRFcxVxTJutEnBLCvtNZ_R52K-sxWwen7IcV46WczxsYIXxNmOjHBrl13oJbBZr5ouZrjtAnDxPHC67Gw-s5lK52k9yydRlqxYr5SpV_F_JfoUw4anSjWlNnBiS_qs6_gLa1anYEPPIpXdbL5dlzEMyMZHdsoPNfK82VerlDxVzwQyb7h6tAZXBF5fNvaO8EaqEiMGlE96QwL-_79jX_5ksQUaULSUveDTgOrMfbFcqMK30HCHQGxqdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خواهرمیانه برای مبتدی ها نیست!</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/21240" target="_blank">📅 12:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21239">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وقتی برخی سرمایه گذاران به امانتداری بانک انگلستان با ۴۰۰ سال سابقه برای طلایشان شک می‌کنند؛ در عجبم از ملتی که در پلتفرم های آنلاین ایرانی طلا میخرند!  راستی میدانستید آلمان چند سال است از آمریکا درخواست انتقال طلاهایش از فدرال رزرو به انبار بوندس بانک در…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21239" target="_blank">📅 10:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21238">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سپاه
پاسداران:
در یکی از بزرگترین عملیات‌ها  دقایقی پیش 7 نفتکش اماراتی در تنگه هرمز مورد هدف قرار گرفتند</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SBoxxx/21238" target="_blank">📅 09:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21237">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یک نفر دایرکت داده خب استاد ما که به قله رسیده و سرش نشسته ایم، حالا اگر پنبه نایاب شد بیاییم خود قله را آغشته به روغن بنفشه کنیم!</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SBoxxx/21237" target="_blank">📅 09:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21236">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترسم این است که پنبه هم نایاب شود؛ آن وقت با چی روغن بنفشه را داخل آنجایمان قرار بدهیم؟!  اصلاً آدم یک جوری می شود!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21236" target="_blank">📅 09:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21235">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شیوه درست استفاده از روغن بنفشه</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21235" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21234">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=asUqXOmyts0ve87i7jyOUbuZT3g9NSAuJIcbGHZkBfBRO0SaWXsWgbYag99WXrYVFVJ2FTO5VFOe15lVA6UjXkljN9LmJ89nq7zcKHkMktrT8A9GseZQrpG_0FGoIkdPEvQIyzYBmpTHkf3mdlCcH5CRKCDvSJImEsm3wEmMChT7VDqNhRCkwZ4E3AqqHg0t-ZqG3-tMKak-sP8INL8SPcveXXE6RWoRoiugOIgEZDiUKTG6AL2WKRditGzI2HxhwV2ce_WUX8ZLQKu7p2uYw8K35nFV7bxXncu1OupSYX1G9659sTrlqdndNjC6t87ByrZKnP23UZOYvbEgEOPNOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/134b1ed686.mp4?token=asUqXOmyts0ve87i7jyOUbuZT3g9NSAuJIcbGHZkBfBRO0SaWXsWgbYag99WXrYVFVJ2FTO5VFOe15lVA6UjXkljN9LmJ89nq7zcKHkMktrT8A9GseZQrpG_0FGoIkdPEvQIyzYBmpTHkf3mdlCcH5CRKCDvSJImEsm3wEmMChT7VDqNhRCkwZ4E3AqqHg0t-ZqG3-tMKak-sP8INL8SPcveXXE6RWoRoiugOIgEZDiUKTG6AL2WKRditGzI2HxhwV2ce_WUX8ZLQKu7p2uYw8K35nFV7bxXncu1OupSYX1G9659sTrlqdndNjC6t87ByrZKnP23UZOYvbEgEOPNOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.  در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21234" target="_blank">📅 08:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21233">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFNeWLjuUd94qcz_wa8z1FNqU9Cth2zFHffkhLuAFZPvqyvy5oZqv_CHLAHdPYkFa73BGE2irV0XMmKEn6Uzw-GoZEgmnEH6uJdMsUGaTkkPxyJNmo8UGYfekIhj4tSzKPq6ytFU7Hs_lTQ4Dlz3-qa47dcOEhscEdfWzW-Ni8iP9SwK8UzfhYCOLwocVF0-OPqQPRw3qN1ChdvmPVhLLd7oHSSFjoTgwmiUJOIgg-QBLM96qIhoFbDX3GshhJOIFdvKiEhOOjEF4k87B6eQKniwJ7xthTN06CVJTndnSElFTpzT4d8bO4xJRKhX3W8OU4QmjwF24bRqIwZ_ZZyZQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان پنبه و روغن بنفشه به همراه داشته باشید که داروهای مدرن نایاب می شود.
در ضمن انجام سرویس تعویض روغن به صورت رایگان انجام می شود.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21233" target="_blank">📅 08:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21232">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بوی محاصره زمینی می آید…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21232" target="_blank">📅 08:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21231">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">حملات موشکی گسترده سپاه در تنگه هرمز</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21231" target="_blank">📅 07:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21230">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TkzUdFJTQ0LGezg1l69eJrBGCoKy5LAqwg_20XYIRQHr4UsBgUtAkduJXCK95I52SDkmanM4M5V_b_HeZlouCrYjKb3fTAAdCCFL7t6uG6Kg5cbKtTm19cCJWRW_N51_Lu82BhNDXliW3o8qLKkL5sEq-WEoMPLLV8RQX4DTu61qrTsncq3R-c3_94hG6DAiBHINfTKw7fzLbOqN1Hbp2JpD7l-4nR-jYT6zjLLkJT-EJg5vB3G0IEuIqPpv4MINGPhs6arIKbgKGHIjN62jw35Im5dZRA8rcYb6S2gVft-_V8ijXx_L5aw_QTAGR_TDbzQLIWrbT4WHGwS7hlA3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاید براتون جالب باشه
فرودگاه نجف عراق که اجازه پرواز به هواپیماهای ایرانی رو نمیده ،
توسط جمهوری اسلامی ساخته شده
😄
شب خوش!
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21230" target="_blank">📅 01:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21229">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">واشنگتن و پکن؛ پیام مشترک درباره ایران و تنگه هرمز
در یکی از قابل‌توجه‌ترین بخش‌های دیدار اخیر دونالد ترامپ و شی جین‌پینگ، موضوع ایران نیز در گفت‌وگوهای دو رهبر مطرح شد؛ موضوعی که می‌تواند برای تهران و به‌ویژه آینده تنگه هرمز اهمیت ژئوپلیتیکی قابل‌توجهی داشته باشد.
بر اساس فکت‌شیت منتشرشده از سوی کاخ سفید، ترامپ و شی درباره نگرانی‌های جهانی از جمله ایران گفت‌وگو کردند و بر دو اصل تأکید داشتند: ایران نباید به سلاح هسته‌ای دست پیدا کند و هیچ کشور یا نهادی نباید برای عبور از آبراه‌های بین‌المللی عوارض تعیین کند.
اگرچه در متن جدید نام «تنگه هرمز» به‌طور مستقیم ذکر نشده، اما این بند در شرایط کنونی به‌وضوح با مناقشه هرمز ارتباط پیدا می‌کند. اهمیت موضوع زمانی بیشتر می‌شود که بدانیم در مواضع قبلی واشنگتن و پکن، مسئله بازگشایی هرمز و مخالفت با دریافت عوارض برای عبور کشتی‌ها صراحتاً مطرح شده بود.
از منظر تهران، نکته مهم صرفاً محتوای این دو موضع نیست؛ بلکه هم‌زمانی مواضع واشنگتن و پکن اهمیت بیشتری دارد. چین بزرگ‌ترین خریدار نفت ایران و یکی از مهم‌ترین شرکای اقتصادی تهران است و در بسیاری از پرونده‌های ژئوپلیتیکی در برابر فشارهای آمریکا موضع متفاوتی داشته است. بنابراین هم‌صدایی آمریکا و چین درباره اصول مرتبط با هرمز می‌تواند فضای مانور دیپلماتیک ایران را محدودتر کند.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21229" target="_blank">📅 20:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21228">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uehq9DD57eZfowb8boCHhilA-HH09EbmMYyX64aT8zC2EX8qryOp1SA32M7COQVOdgs0zeZn6L3HGe6Cf9lYvrZEW12TzTkJOvsUGA22PHciON8Fgnt7yOJN3KZFLyV2O3ZHhTJfGQZvRZTleUIGMdqRX9iD4Bu6Lg_SGsdXGbYd5l4YOWRMdCsBHXkxkQG3IL7PTBkMI1XuFLFtYhW0y1P9FlstWBRRBLKIxcG_LjKkWvoAHJmDvm1pSFjlQ_ULK78lcuwVaCNywmMS5J2H01mJC3G-mwhoBbVd2IQ8ILMNLNoVW_NUJlDkyqHiQLhTufbGRdmtAIWf7pXqj9NREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم عملیات انتقال کشتی‌به‌کشتی (STS) در دریای عمان نسبت به سطح ماه فوریه، ده برابر شده است.
تولیدکنندگان نفت را بارگیری کرده و با عبور از تنگه هرمز از طریق مسیری جایگزین که امنیت آن توسط ارتش آمریکا در نزدیکی سواحل عمان تأمین می‌شود، محموله‌ها را برای تحویل به خریداران نهایی به کشتی‌های بزرگ‌تر منتقل می‌کنند.</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SBoxxx/21228" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21227">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شورای عالی امنیت ملی:  «ادعاهایی مبنی بر اینکه ایران به محدودیت‌های اخیر هوایی با اقدام نظامی پاسخ خواهد داد، نادرست است.  مذاکرات با کشورهای ذی‌ربط برای لغو ممنوعیت‌های غیرقانونی پرواز به‌طور فعال در جریان است.  در صورت لزوم، اقدامات متقابل غیرنظامی برای…</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/21227" target="_blank">📅 18:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21226">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:  پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس  اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SBoxxx/21226" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21225">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پسری ۹ ساله ارمنی‌تبار مسیحی در اورشلیم، پس از آنکه به دلیل دوچرخه‌سواری و استفاده از هدفون در روز عید یوم کیپور مورد اعتراض قرار گرفت، توسط شهرک نشینان یهودی با اسپری فلفل مورد حمله قرار گرفت.
تصاویری که از
کانال ۱۳
اسرائیل پخش شد، نشان می‌داد که این کودک که نامش ویلیام است، پس از این حمله در حال دریافت درمان پزشکی از سوی تکنسین‌های اورژانس در یک آمبولانس است. این درگیری در نزدیکی شهر قدیم رخ داد، زمانی که ویلیام در حال دوچرخه‌سواری و گوش دادن به موسیقی بود.
گزارش‌ها حاکی است که مهاجمان از پسر خواستند هدفون خود را در بیاورد. پس از آنکه او این کار را انجام داد و به زبان انگلیسی صحبت کرد، فریاد زدند: «انگلیسی نه، یهودی‌ها» و سپس مستقیماً اسپری فلفل را به سمت او پاشیدند.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/21225" target="_blank">📅 15:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21224">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وزیر امور خارجه آذربایجان، بایراموف:
اگرچه دهه‌ها درگیری با ارمنستان تراژدی عظیمی بر مردم ما تحمیل کرد و زخم‌های عمیقی بر سرزمین ما باقی گذاشت، آذربایجان انتخاب کرده است که به آینده نگاه کند و صفحه دشمنی را ورق بزند.
ما صلح را به ارمنستان پیشنهاد دادیم که کاملاً مطابق با هنجارها و اصول حقوق بین‌الملل و مبتنی بر شناخت متقابل و احترام به حاکمیت و یکپارچگی قلمرو یکدیگر است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/21224" target="_blank">📅 14:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21223">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!  از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!  سبحان الله!</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21223" target="_blank">📅 14:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21222">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPbW4KI26zQGsSuJCy2ajtPC5MCJlt3z77slcQdGB0C95YmcgaVvCGqHWsyJIIhuL6X9_eZUtTMc5kDfqGo7D5zkb13Sj8XeMUIrYI5k7qpBCe4PDGti7DYIIiTdkzamd5Gnm9L-qFylce8DGLXuGFTxX1oc56dku9xNxR01J4z9FL8hrBNjyokqFsZzAsij6kM77XYvwohZCsjRtsUOXHZUA6qelLfnwizR0MPux8V0KtBryZtIYW134HuYXxkG00TWD5fDyl4CCA9F_7eQUwJvNkVhthqRnvM3wSUsIG_sibUPzF2ueDZV2FjFl0g1f-K70Gjao99f2buLTkRcJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برآورد درصد مسلمانان نسبت به جمعیت هر کشور در اروپا در سال ۲۰۵۰</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SBoxxx/21222" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21221">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biLCifcRw4u8kQrr7vdmeTx0Wfows0RoyN0oNMX1jOS2yfb1OZLpPA3FNmgQt1rnIBCIKx4crdKr_wO8BxGuYIyCo0kycJhdIB-TLHKXFl2zCMo7TRKxyQ3anqWr7ximbAZsMZtGITaKb5ZPdm-kMvwGX35VVyaK-QQrfqZLwH9lwNkzbymNJZPdwOmngPk1K-fBv2yluumPqRd7OpO2DnwOciIZuWw3NV_R9-DCnhy-mixOH-dEvcGHRYuhlklEFeUAnK6CfEwZ4Y7pO7aUQuZ4NEov03N1g4hrjm6rRZ13s1pGL7yEyb0ECGnat92hyQiD-_oF-otECdN73pfyDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشاره دوباره ترامپ به تنگه هرمز به عنوان تنگه ترامپ !</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SBoxxx/21221" target="_blank">📅 13:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21220">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.  طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21220" target="_blank">📅 08:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21219">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=q5zCoEoUTfbOecsSx6vfa8LOq-baQl6MwnI0u3hyKI_lwjj4OIAiUaq_BoPe1I2oLQB4y7NifJvcRxYdm_PyVbo4UBxKXfBgNEmp3X8BJJ7OxiptNpC_YE-AFakbE8EwJV2iFDmo1Ao5-501bnTljwiUPCzpWQi4T0E8kBc77lzG33vZt1HfTCu993OOb9Oe5A0ZuGFiRFbnLRPa6fNrTFsJ_gCcHqFQ0WPojf2g7xd-ABheCanNcwxdI3SZxAhUMhrZFGrYV1MUmk8Ts3s1sTaSYuTp2-tkuP_3K2QrvH5uRh2vbrR1L3OiwJZrAeEFfNbmX6HNMANrcR3_4Id-nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07644aa8e4.mp4?token=q5zCoEoUTfbOecsSx6vfa8LOq-baQl6MwnI0u3hyKI_lwjj4OIAiUaq_BoPe1I2oLQB4y7NifJvcRxYdm_PyVbo4UBxKXfBgNEmp3X8BJJ7OxiptNpC_YE-AFakbE8EwJV2iFDmo1Ao5-501bnTljwiUPCzpWQi4T0E8kBc77lzG33vZt1HfTCu993OOb9Oe5A0ZuGFiRFbnLRPa6fNrTFsJ_gCcHqFQ0WPojf2g7xd-ABheCanNcwxdI3SZxAhUMhrZFGrYV1MUmk8Ts3s1sTaSYuTp2-tkuP_3K2QrvH5uRh2vbrR1L3OiwJZrAeEFfNbmX6HNMANrcR3_4Id-nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21219" target="_blank">📅 08:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21218">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ، رئیس‌جمهور ایالات متحده، پیشنهاد ایران برای آتش‌بس هفت‌روزه را رد کرد و به دستیاران خود گفته است که انتظار دارد بمباران‌های آمریکا علیه ایران پس از انتخابات میان‌دوره‌ای نوامبر از سر گرفته شود.
طبق پیشنهاد ایران قرار بود تنگه هرمز بازگشایی و مذاکرات هسته‌ای در ازای رفع محاصره بنادر ایران توسط ایالات متحده و کاهش فشارهای اقتصادی بر تهران، از سر گرفته شود.
— وال استریت ژورنال</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/21218" target="_blank">📅 07:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21217">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سفیر ایالات متحده در چین، گفت که رئیس‌جمهور ترامپ در مذاکرات خود در کاخ سفید، از رئیس‌جمهور چین، شی جین‌پینگ، خواسته است تا هرگونه کمک چین به ایران را متوقف کند.
او اظهار داشت که واشنگتن به وضوح اعلام کرده است که «هرگونه کمکی که چین به ایران ارائه می‌دهد، کاملاً غیرقابل قبول است».
او افزود: «ما از قبل حرکتی در این زمینه مشاهده کرده‌ایم. این همان تعهدی است که داده شده است. آن‌ها به ما اطمینان دادند که چنین کاری انجام نمی‌دهند.»</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/21217" target="_blank">📅 02:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21216">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فیلم کامل مستند BBC درباره نسل کشی ترکیه ضد کردها در عراق</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21216" target="_blank">📅 00:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21215">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=a5tIIJWgV4qdhB2KAm4QllyZt1UbsWJxFuPkUxjHMSsm8cOhaJ__s-tnQb5x4sR3IXcx96UuUjUp5DYthBJW_I5d3ztluvatOwJn-NUZNPlxjyFbMeP98yhFkJSZtHG1m8JyBI82tp6_wL-h5b7_9cY6_aQI6eJZQBha4bWGS1lpbc9e4Kj9_svq7aHxHb_9fNfMNKMPXqcwMkqcOVcrTqbZJx1IgcS3dRNiKJQK4T3k4G1IClLh53Qfrkp8oWsUbnm6F3uBcZvMa1BwgOeYWqsvlZS3nlStLTM1r4V7F3b21AeOVtvlcSJNYsnC5RqX4dOFCCvc8bh6wBH_xSo5NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ada5e22fc.mp4?token=a5tIIJWgV4qdhB2KAm4QllyZt1UbsWJxFuPkUxjHMSsm8cOhaJ__s-tnQb5x4sR3IXcx96UuUjUp5DYthBJW_I5d3ztluvatOwJn-NUZNPlxjyFbMeP98yhFkJSZtHG1m8JyBI82tp6_wL-h5b7_9cY6_aQI6eJZQBha4bWGS1lpbc9e4Kj9_svq7aHxHb_9fNfMNKMPXqcwMkqcOVcrTqbZJx1IgcS3dRNiKJQK4T3k4G1IClLh53Qfrkp8oWsUbnm6F3uBcZvMa1BwgOeYWqsvlZS3nlStLTM1r4V7F3b21AeOVtvlcSJNYsnC5RqX4dOFCCvc8bh6wBH_xSo5NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثرات خانمانسوز جهش دلار روی مغز مردان سرزمینم!
گفته می شود ایشان قبلاً پرایس اکشن کار بوده که بعد از 36 بار کال کردن اکنون وارد مباحث تشکیل سبد و تخمگذاری در آن شده است و گرنه این حجم از آشنایی و تسلط بر مفاهیم بازاری نمیتواند از دهان یک اسکل معمولی بیرون بیاید!</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/21215" target="_blank">📅 23:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21214">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد…</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21214" target="_blank">📅 23:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21213">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">— تًن ماهی — گوشگیر سیلیکونی — آب معدنی — چسب زدن شیشه ها</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21213" target="_blank">📅 23:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21212">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">علی عبدی برنامه آمریکا و اسرائیل برای جنگ بعدی علیه ایران را نفوذ آبی و خاکی و هلی برن از سمت خلیج فارس، غرب(عراق)، جمهوری باکو، آسیای مرکزی و جنوب شرق (پاکستان) دانست و تصریح کرد حملات هوایی، تلاش برای شکار شاه مهره و استفاده از بمب اتمی تاکتیکال نیز رخ خواهد داد، ولی پیروزی از آن ملت ایران خواهد بود.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21212" target="_blank">📅 23:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21211">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21211" target="_blank">📅 23:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21210">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">به پزشکیان رای دادیم که جنگ نشود، هر هفته 15 بار جنگ می شود!</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21210" target="_blank">📅 23:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21209">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خداوکیلی راست می گوید ؛ این بار دیگر غافلگیر نشویم!</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21209" target="_blank">📅 23:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21208">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNMgnboRzDdI9tVkqctWQvgTPpE3GUW3IN-d2cOhcW1p1AbNpbyBz6Xd4aVAPHKO5a16xjUhenH4psn07QAlKvfGukWAzwg04TTHvDUWmXc-y1Wzo_AYET-KH5ZB1wXLB1Xiulf4OGwBeSGm_3IJ35sqUugKYWQ9eH2CFWb_cje8H5dto28nEgensYAkwQOy77X8eY-Y6vNZAe_63aYQkJrx6_5RDPffUgWOpdP7EPz2ghoXxU69gEcSY27uQ98w3aTZwrojH1jdi9fm3dTJq744vAIJXTPm3Gxgb7VdxCpls_f36nebT4LVpIORJ092XRPfXBvwjW41q3BAx2N88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من شخصاً هیچ وقت به نزدیک بودن توافق ایران و آمریکا توجه نمی کنم ولی اعتقاد دارم نزدیکی ایران و آمریکا نزدیک است.</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21208" target="_blank">📅 23:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21207">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">چرا می خند؟!</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/21207" target="_blank">📅 22:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21206">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVwk-pvKCv_Ydcq8chwXByyvVytQMVFDfkGIZqPfXQLmCa3jngu5eYeiohitZy0AD1ABjwTaXVD5SofsRDHbNEYnSxDTGM3n2h5LbAOjBdaMC9BBJjzGBb3o5zTVxlB8HqtTdPkAjDBWMUlZDnCr3sOKL2l2uoQ3fGSGOkrM8R-hsI6Zaf5Zgg1zeZx-Znh-_5DoTnwUFTE91qKQqnheRAqGdGv_G3nf7YjLdPJAV2w0NDKBHvwGwE-BKpYpH0ZoIfESJUUUhhtUkSmXB-u1fmCnygXTUfxWClqbRv7bzeOsF35O7E3oDuWXPSRHNe8BrvnWB0ZP4bPr0x8RyAaK9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21206" target="_blank">📅 22:54 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21205">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مرندی ذوالاکتاف:
هیچ پیشرفتی در مذاکرات غیرمستقیم با رژیم ترامپ حاصل نشده است. منطقه به سوی تشدید تنش پیش می‌رود، چرا که دیکتاتوری‌های حوزه خلیج فارس که در جنگ علیه ایران همدست بوده‌اند، به توطئه ترامپ و بسنت علیه ملت ایران می‌پیوندند.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21205" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21204">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgJdPXDHFWss8zBqccPr3genRi02dKaSjhUszgDV5aa6iaHhJIesUFOOmif53anCFqA_lzf0yP4DetPwIOIqEImlAmPPMK6VkKVSPC5I17Ta0vz2HnQjlnMFAY7gdmApkh3ZDRmGx90B5xLiaHHzlnqwuP8KgwK6eUAVwkqUiDlhT46cNhX764c7I6U45uCh8LGWfESecph17YDUfPcOVEUiuHNL_sRU8FpMp0k3mt4xdnvfpgMscIt3MQs2PgsmlwxCdl3wF4Syx199bsj-VYHF0OeuM1E-YFAeynt4WatuRB7AT5Yhtj-8t8FphPqGhpt4nTt46GIISAw5LyHaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21204" target="_blank">📅 22:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21203">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvX5EqV97iJtDOamd15-3CUKBcYj47ycxwe-xUCHIbmPCdULjhoGliuXc4YcE9DLGV8hCgR4ckD7B1AczrtqnMz9-UxeJkR2c63ZezoZhrIhR2Or5LU6_2LHXf1gqXGAsyZqi1BPkLbjmI_JC7udO_IYDzj97tWi56L4NCGv_TvBs4FFREH3GIjXauPcv3nRfh6MxAeaCiRJnV71C8f0-RYEl6iMqYFthAnhdM8GVSsqLiSw6YN2n_56pw5vGJfdc1TaT_-qVqQXIhMLM0OitLeJES-wMJa7VFCWhTtzkAv-U8UTdz48LzBcVOBy1xC7kDYVFN6xIsSGva5BPb8h4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقتا خواهرمیانه جای مبتدی ها نیست!
از ۶ ماه پیش بلایی نبوده که جمهوری اسلامی و نیروهای نیابتی اش سر این سعودی های فلک زده نیاورده باشند؛ بعد این هفته جشن باشکوهی به مناسب ۹۶-امین سالگرد تاسیس کشور سعودی در قلب تهران برگزار شده!
سبحان الله!</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21203" target="_blank">📅 21:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21202">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Ali SharifAzadeh – انتخابات اسرائیل</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/21202" target="_blank">📅 21:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21201">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ
:
در نوامبر در چین دوباره با شی ملاقات خواهیم کرد</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/21201" target="_blank">📅 20:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21200">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">First Time ?</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21200" target="_blank">📅 20:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21199">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏ قائم‌پناه:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگر به پایگاه‌ آمریکا در کشور شما حمله نکنیم بلکه به خود کاخ سفید موشک بزنیم.</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SBoxxx/21199" target="_blank">📅 20:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21198">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سفیر آمریکا در چین:
پکن در پی هشدار ترامپ، بخشی از حمایت‌ها از تهران را متوقف کرده است</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21198" target="_blank">📅 19:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21197">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">میانگین 200 پیپ</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21197" target="_blank">📅 18:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21196">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#FairValueCurve  نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.  در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21196" target="_blank">📅 16:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21195">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس اسبق سیا:   امکان تصرف خارک برای آمریکا وجود ندارد</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21195" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21194">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21194" target="_blank">📅 16:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21193">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
عربستان سعودی ارسال نفت به اروپا را لغو کرد!</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/21193" target="_blank">📅 16:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21192">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21192" target="_blank">📅 16:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21191">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/21191" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21190">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بی حجاب ها بیایند توی تجمعات شبانه بعد که تمام شد لطفا خودشان خودکشی کنند</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21190" target="_blank">📅 14:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21189">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/21189" target="_blank">📅 14:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21188">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مخبر، مشاور رهبر انقلاب:
پرواز در منطقه یا برای همه آزاد است یا برای هیچ‌کس
اگر ایران امکان پرواز و دریافت خدمات فرودگاهی نداشته باشد هیچ کشوری در منطقه هم این امکان را نخواهد داشت.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/21188" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21187">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خاتمی، امام جمعه تهران:   کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/21187" target="_blank">📅 14:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21186">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خاتمی، امام جمعه تهران:
کسانی که حجاب را رعایت نمی‌کنند نیز شهروند این ملت هستند و حضور آنها در تجمعات و همراهی با مردم کار خوبی است، اما دهن‌کجی به حجاب، خلاف وحدت است</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SBoxxx/21186" target="_blank">📅 14:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21185">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uznalwJx8ZtF30gjAluHjANbzT20giW4CC-CLX7UhVXiKhhEFVjXiT9kJtINw_ixuMsB4CD3SlmkfYZ59lJK9xk4boRd0oVJBekbmyswqRNVin8yNSXNqvxper40ZtKlnbuZTcRNmRcmzNezG0l2J5rY5zbfXp6W1y_BtR1KEK0wsSFo-pmyA0Lp46Pk7rZ_NDhWVVI-o_IhrmMRxmX3PB5zPiXIofSAbN0p-pi9jaWMT_p-Nq6GPS7Lt6ApzsbR4I2cWeH5M_eZE5iz9pQQ-frgnvyr-KIeLYmQeTq3AlkKardOKB4UaqG_cMLy20xjIar4Dl4h4d44clB9zDDIuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در حال نزدیک شدن به کف محدوده بیش—فروش است.
در این شرایط پرتناقض، بهترین استراتژی فروش در مقاومتهای نزدیک (4292 و 4308) با تارگت 4235 می باشد.</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21185" target="_blank">📅 11:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21184">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pELaz8bhDhdOrgWtN0BCrMiwBUmAhjBng6uUnJA72lK44lEvmaHmYtpTml-vCX8-ypmAiPe2E1gjMdi3VcuvUoD2GX0lOphgx2B_i2RMzPOiPZgQIGffwOHUSa7wdX1AOs3NK5DkPuacAVnl7-FaqDWN2UC9j-PUvf1QjexfgnEkNkaZi_Ju3l2I3H7tcTz9VWL0JXYbEdHE3H3DP-1nT2yChLeuweSFPdSWCfFKScritMEMQu16AZF2GPr52hu4_CMTBtTE_sQwKlIfRFpA2PFL9va9K8cWBgg9yttAZvEtjXgKxXedDA6_EKn1kMEDGoWEFyiMu0N_n-MZ0dtxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح بسیار بالایی است و هر بالایی فرصت فروش است.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/21184" target="_blank">📅 11:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پاکستان، ترکیه و عربستان سعودی در پی افزایش حملات حوثی‌ها به خاک عربستان، یک جلسه اضطراری رؤسای ستاد مشترک را بر اساس پیمان دفاعی مشترک مکه تشکیل می‌دهند.
این جلسه اولین گام در سطح فعال‌سازی تحت این پیمان است که مقرر می‌دارد هرگونه حمله به یکی از اعضا، حمله به هر سه کشور تلقی می‌شود.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/21183" target="_blank">📅 10:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21182">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کلمبیا تمام روابط دیپلماتیک خودش با ایران را قطع کرد
دلایل اجازه ندادن به بازرس ها آژانس  بستن تنگه هرمز رعایت نکردن حقوق بشر و .... بود
یکی از دلایل جالبش رابطه ایران با گروه های مواد مخدر  بود</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SBoxxx/21182" target="_blank">📅 01:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو:
«آن‌ها اسرائیل را — اسرائیل کوچک — متهم به استعمار می‌کنند. و چه کسی ما را متهم می‌کند؟ در میان آن‌ها، گروهی در بریتانیا و فرانسه هستند.
به نام خدا، آن‌ها این اصطلاح را اختراع کردند — مستعمرات آن‌ها کل کره زمین را در آغوش گرفت.
استعمار؟ لطفاً دست بردارید».</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SBoxxx/21180" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=q3dpepLSXdCR-Qyx3voTDMJkSvCF8XzmlFnBbtMgCH-nmoWXhQcRJRSVPBW0U99FSvWg-cu_oYvLzqculIV-q4YS8jRhboIL_C1mh7H3ekP1Q0r6H976ZGWTkEw_xasfJvyg-IxbrKMtfqFBiBCmE1LXLxnm_8Q2aNAYo1yLaZsM3VhLsi9fJTAQCzzbV3c6O3yJf4G8cwGrdxNWTsRI6EhiEr86tq7rKq1Ql5R5Ft8VCGeY3kfzNRIU429JGj1lq0JMML5ZrdtEglJ5OdzoVIeWvSGXlSnv9Bl-ver0VE5uaarHm0gnsEbOKMkQVxshM-5b5NMv4YP-UFtxOnjjm4Y0ha6s2YVM7qQqfMpVHruOjaZVYQQQpmRns6yIwJ2m3zEgw5fsjXih8lkx9Q2McAMNqbSe6T3kZOyOEPB-IBv-aRzSXwgkefWVGevM-1JW1K0GCas8IBtKwX5btIljw7KbLA7Uc7-lIuTxb2R5qGgJpRCgeZHVU-XSR4Juu4XH2k_ESMj1fIenuF2_7uj5uMoEM1NEshF3t1vs80G31caJmB4BUEdSZ1L7-ZSqtqzfABg5pb8_DgzV8L19lvBeHGt9WJ4Y1JSUD-vQaFlClq4yVhBlMbqNPPJ9Y74qYx1a83I7n_AVux7eLQ_G6YMx5mXmTec87F1J5yVjtojEfT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dad7c5c99.mp4?token=q3dpepLSXdCR-Qyx3voTDMJkSvCF8XzmlFnBbtMgCH-nmoWXhQcRJRSVPBW0U99FSvWg-cu_oYvLzqculIV-q4YS8jRhboIL_C1mh7H3ekP1Q0r6H976ZGWTkEw_xasfJvyg-IxbrKMtfqFBiBCmE1LXLxnm_8Q2aNAYo1yLaZsM3VhLsi9fJTAQCzzbV3c6O3yJf4G8cwGrdxNWTsRI6EhiEr86tq7rKq1Ql5R5Ft8VCGeY3kfzNRIU429JGj1lq0JMML5ZrdtEglJ5OdzoVIeWvSGXlSnv9Bl-ver0VE5uaarHm0gnsEbOKMkQVxshM-5b5NMv4YP-UFtxOnjjm4Y0ha6s2YVM7qQqfMpVHruOjaZVYQQQpmRns6yIwJ2m3zEgw5fsjXih8lkx9Q2McAMNqbSe6T3kZOyOEPB-IBv-aRzSXwgkefWVGevM-1JW1K0GCas8IBtKwX5btIljw7KbLA7Uc7-lIuTxb2R5qGgJpRCgeZHVU-XSR4Juu4XH2k_ESMj1fIenuF2_7uj5uMoEM1NEshF3t1vs80G31caJmB4BUEdSZ1L7-ZSqtqzfABg5pb8_DgzV8L19lvBeHGt9WJ4Y1JSUD-vQaFlClq4yVhBlMbqNPPJ9Y74qYx1a83I7n_AVux7eLQ_G6YMx5mXmTec87F1J5yVjtojEfT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک موزیک ویدیوی Erotic از اتحاد عربستان و فاکستان ببینید شب جمعه ای دلتان باز شود!</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/21179" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز:   آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21178" target="_blank">📅 20:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز:
آمریکا و ایران درباره توافق مرحله‌ای برای پایان دادن به درگیری‌ها مذاکره می‌کنند</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/21177" target="_blank">📅 20:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسرائیل می‌گوید حملات جدید علیه ایران «مسئله‌ای زمان» است و تأسیسات هسته‌ای ممکن است مجدداً هدف قرار گیرند.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21176" target="_blank">📅 19:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">محدوده 4255 بسیار مهم است.</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SBoxxx/21175" target="_blank">📅 15:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFE0pHEhImQOauHIh3IAaTgeU68JYg3TkL0gQki3gCb2Qwl2BQK23ba9WhKrA5-D66Q0mYJiBQsSfgDk9R2IdPG2QicjwYeglS1URGsUV8KHANzJ7vtI9pz4sTS6wQw2FdLm2JHpr9KKDyu5UmuvECl69fLFwy0_13-9GfwvVaJu2bcwTm_DR2JQ8Zz1GBIIREI5dQDqJjfzNpxi8WkUYMLpbCzpR9Q3zGUceL-iqwegrKu-1KFddmei14ilYv7Tm3Grc3zvyfi2l0ALsocxOtuWKxj3jG06F8LKQ7Sg7aq2aB4iUyCv21rBdB4idypYCcAutkpYShBiyvBqGqZhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس صداوسیما اشاره نکرد که اگر ما توان تصرف بحرین را که میزبان نیروهای آمریکایی است داریم، چطور توان حفظ خارک را که مال خودمان است در برابر نیمی از همان آمریکایی‌ها نداریم؟!</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SBoxxx/21174" target="_blank">📅 15:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21173">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارشناس صداوسیما:   در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SBoxxx/21173" target="_blank">📅 15:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21172">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کارشناس صداوسیما:
در صورت اشغال جزیره خارک توسط آمریکا، خاک بحرین را پس می‌گیربم</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SBoxxx/21172" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-21171">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مرندی ذوالاکتاف:  اگر کشورهای خلیج فارس جلوی پروازهای ایران را بگیرند، ایران فرودگاه‌هایشان را با موشک باران تعطیل می‌کند</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/21171" target="_blank">📅 14:28 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
