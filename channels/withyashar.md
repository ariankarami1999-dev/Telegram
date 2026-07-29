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
<img src="https://cdn4.telesco.pe/file/MruG6VfXXKXN0vG0PKWya-0nhOpeCxgj2sXwYKm1pBksL6wc2hZ1naB2eQEhqBNn5zZj-1u313WjFkmNn1ndW_QaNYXUbsYd5di-LNAF6IJy56BS-IfO0hlYCb_WMP9Lp1tvpdmxHtd9yz63BULUsRSYS3KxvD4QNQwy7rc3XH8xH0mmYJ3yod9KfVFzVYnqwlCDDSUYgX3fk_pCxnIvoXWD1TqsCY-v161r4UfcIF3PblaVp0NKbtXdCLOX1BYd2o5MqxwIsbKWlqrQa3ojjMPOqT5vTy7Datw9GG9KMF9pa7P20s-U20OfOjrvA9QUS--8MBrf2zb7BkriMVB2Iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 431K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 00:13:06</div>
<hr>

<div class="tg-post" id="msg-20029">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/withyashar/20029" target="_blank">📅 00:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20028">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">از دایرکت مشخصه امشب هیجان به اوج رسیده</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/withyashar/20028" target="_blank">📅 00:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20027">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مقام ارشد اسرائیلی به الجزیره : پاسخ گسترده آمریکا به ایران محتمل‌تر از فقط یک حمله تلافی‌جویانه است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/20027" target="_blank">📅 23:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20025">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ در مورد ایران:
من دوست دارم تعرفه‌هایی علیه ایران اعمال شود.
لیندسی این را می‌خواست.
خبرنگار: آیا می‌خواهید مجلس نمایندگان قبل از ۳۱ آگوست برای بررسی لایحه تحریم‌های روسیه و ایران بازگردد؟
ترامپ: راستش را بخواهید، نباید لازم باشد، اما اگر لازم باشد، دوست دارم ایران را به عنوان تعرفه اضافه کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/20025" target="_blank">📅 23:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20024">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=uma6w4tzcZvBsiybspTSYE0RP-At42wwsbKClAsnT__lhgXYPtm9uXf83_6wZ59C6CdnHPd2qa_9CPDWjhxIBh7R1KSUsr5K4dJ0XQ_mLuDt0NMZKFzacVPTK_dvuGZHm71gG8Vsuu50aL1NRETeutJQvnUPZYWa3uZE9RAemwVGLKYDgNn_qZR9FJ1ruZTW-9VG9Rjxq2SsIfXRnd4-oMt-ySmlGMpr81n4CaKxaj6LJTVyk1Sp_9hxKTrxhD8Uf4vEygmXXBlXzhfy4iw3x_YDfueR4vNKzQ6ZUEKmNtOBZuhV6Zeiw_9HW-3UdVJxqjBib4Md-9xFiDQxpCikEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4981a0c73.mp4?token=uma6w4tzcZvBsiybspTSYE0RP-At42wwsbKClAsnT__lhgXYPtm9uXf83_6wZ59C6CdnHPd2qa_9CPDWjhxIBh7R1KSUsr5K4dJ0XQ_mLuDt0NMZKFzacVPTK_dvuGZHm71gG8Vsuu50aL1NRETeutJQvnUPZYWa3uZE9RAemwVGLKYDgNn_qZR9FJ1ruZTW-9VG9Rjxq2SsIfXRnd4-oMt-ySmlGMpr81n4CaKxaj6LJTVyk1Sp_9hxKTrxhD8Uf4vEygmXXBlXzhfy4iw3x_YDfueR4vNKzQ6ZUEKmNtOBZuhV6Zeiw_9HW-3UdVJxqjBib4Md-9xFiDQxpCikEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد حملات ایران:
این گروه با گروهی که ما با آن سر و کار داریم متفاوت بود.
آنها قبلاً عذرخواهی کرده‌اند، اما، می‌دانید، ما باید کمی آنها را تنبیه کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/20024" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20023">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=VTcCX9U2nrmbWPnpH49kf7j1CYyig1DCBa5Bs3JEyg8LgEN_-qJM6vCGTmgnaHj7tHJwoxKNFesYiEUTZuihGIoXquBMiPIbmGYMi67zV-pfjxUqZlkgYlDoFvmMSckyCa4SWj_Lm9_4Bn1Lsbu7DfVHRWrzsEc6uh81_c-GlSPBhkH0vqsGJ52Cv6O__rA584iVqvWxuKOXBO6GoC-6atQRIRRxtic91nsY-C4DywMDLJLXIQB2DyE0ZV9l-J3tBey0rFdNUhngLO5RXzLldd0af-AcGTbuvuheHDa84kz4XfvGNQIkKfkxI-p80LD8SEvDRXsqPT4Mhf4gslGKgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364b88f4c7.mp4?token=VTcCX9U2nrmbWPnpH49kf7j1CYyig1DCBa5Bs3JEyg8LgEN_-qJM6vCGTmgnaHj7tHJwoxKNFesYiEUTZuihGIoXquBMiPIbmGYMi67zV-pfjxUqZlkgYlDoFvmMSckyCa4SWj_Lm9_4Bn1Lsbu7DfVHRWrzsEc6uh81_c-GlSPBhkH0vqsGJ52Cv6O__rA584iVqvWxuKOXBO6GoC-6atQRIRRxtic91nsY-C4DywMDLJLXIQB2DyE0ZV9l-J3tBey0rFdNUhngLO5RXzLldd0af-AcGTbuvuheHDa84kz4XfvGNQIkKfkxI-p80LD8SEvDRXsqPT4Mhf4gslGKgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: چه چیزی می‌توانید درباره حمله به نفتکش در مصر به ما بگویید؟ آیا این موضوع به ایران مربوط است؟
ترامپ: من در جریان قرار گرفته‌ام. این کمی بیشتر از همان چیزهای تکراری است.
@WarRoom</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/20023" target="_blank">📅 23:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20022">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=i3_xKIF9n2dZ3emfbHEC90mlch7hio20VGsLc06cYwWGv23MLR5g-ITK5bDqGLaLBq8X1vaNZio-_Z1pwXY8TYmxzSISVahjthyzAh1S4-NRzvdNtBrfsuz_YgB0xF_hutOk4mX2qJTxfjJYIo3SjycbsT506QamDySXi8cVQvR7_bVCIdJ6CvH0TUa-PK0nmYLYZ5jYRugxP69HSSbFEymheFS6dtiJx_7ndCZ3-BFM3CgW6qrgSKnoddc1Fz7qAHEs5G0RnhU9OjVFM7wVL3fwE6zs3oOmkiwZ47nj0CQWS23oWVxBnpUYbchxEcqmgfUUxPC5QkCpKCHmpZNZ7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b410c8b1ad.mp4?token=i3_xKIF9n2dZ3emfbHEC90mlch7hio20VGsLc06cYwWGv23MLR5g-ITK5bDqGLaLBq8X1vaNZio-_Z1pwXY8TYmxzSISVahjthyzAh1S4-NRzvdNtBrfsuz_YgB0xF_hutOk4mX2qJTxfjJYIo3SjycbsT506QamDySXi8cVQvR7_bVCIdJ6CvH0TUa-PK0nmYLYZ5jYRugxP69HSSbFEymheFS6dtiJx_7ndCZ3-BFM3CgW6qrgSKnoddc1Fz7qAHEs5G0RnhU9OjVFM7wVL3fwE6zs3oOmkiwZ47nj0CQWS23oWVxBnpUYbchxEcqmgfUUxPC5QkCpKCHmpZNZ7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:ما می‌خواهیم آن‌ها را بسیار سخت بزنیم زیرا نوبت ماست که آن‌ها را بزنیم.
آن‌ها می‌دانند که این در راه است. آن‌ها از ما می‌خواهند که این کار را نکنیم.
آن‌ها دیشب سعی کردند با ۵ موشک به ما شلیک کنند. ما همه آن‌ها را رهگیری کردیم.
@WarRoom</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/withyashar/20022" target="_blank">📅 23:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20021">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اکسیوس دربار دیدار ترامپ و نتانیاهو :
نتانیاهو در دیدار با ترامپ نسبت به احتمال دستیابی به توافق با ایران ابراز تردید کرد و گفت‌وگوی ۹۰ دقیقه‌ای دو طرف عمدتاً بر ایران متمرکز بود. به گفته یک مقام اسرائیلی، سه گزینه برای ادامه مسیر بررسی شد: دستیابی به توافق با ایران، ادامه محاصره دریایی و تشدید فشار اقتصادی، یا ازسرگیری و گسترش حملات نظامی. این مقام گفت ترامپ درباره پیامدهای جنگ بر بازار انرژی و اقتصاد جهانی ابراز نگرانی کرد، اما نتانیاهو تأکید داشت جمهوری اسلامی در تلاش است با استفاده از تنگه هرمز آمریکا را وادار به امتیازدهی کند و باید فشار اقتصادی از طریق ابزارهای نظامی و غیرنظامی افزایش یابد. او همچنین مدعی شد ایران با کمبود سوخت، صف‌های طولانی بنزین، کمبود گازوئیل و نارضایتی عمومی روبه‌رو است و حکومت از احتمال گسترش اعتراضات مردمی نگران است. این مقام اسرائیلی همچنین ادعا کرد که اگر ایران به اسرائیل حمله کند، پاسخ اسرائیل فوری
و بسیار شدید خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/20021" target="_blank">📅 22:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20020">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند. @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20020" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20019" target="_blank">📅 21:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارشات از‌ پرتاب موشک از شازند اراک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20018" target="_blank">📅 21:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">به گزارش واشنگتن تایمز، وزارت خزانه‌داری آمریکا اعلام کرد دو نهادی را که به گفته این وزارتخانه از سوی ایران برای کنترل تردد در تنگه هرمز مورد استفاده قرار می‌گیرند، تحریم کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20017" target="_blank">📅 20:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به گزارش وای نت عبری به نقل از یک منبع ارشد سیاسی، گفت‌وگوی میان بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و دونالد ترامپ، رئیس‌جمهور آمریکا، عمدتاً بر موضوع جمهوری اسلامی متمرکز بوده و به عنوان «یک رایزنی واقعی و تبادل نظر» توصیف شده است.
این منبع اعلام کرد که رئیس‌جمهور آمریکا با سه گزینه راهبردی روبه‌رو است:  دستیابی به یک توافق، ادامه محاصره دریایی، یا «از سرگیری و تشدید حملات». همچنین تأیید کرد که مجتبی خامنه‌ای، زنده است و افزود: با اطمینان این را می‌گویم
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20016" target="_blank">📅 20:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارشات اولیه: صدای انفجارهای شدیدی در اردن شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20015" target="_blank">📅 20:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=ROCIRzAGVoE6mAtkHSm7exNJNWegNoReJJ_wOSrY68-mFzB_q66eNlOhAixA60QhNybpBqKxcICeQTRKeOYF8uSdDLWYvOG4p8P7-mWmYGbJ6Pm3oi_M4kD3Df5_zwQksz7T8xQ2gwe37Qzop5ifaPVOLBtg_jOATkdPZuj5UIjU4FV0sr0lJRagDoLfIulq99_fQxiK1L5749Vr-qf_ACv0KztSaHQwlffe4XT6VfCx39juwfAtDNGVZaay_LmB00ElIOO3DGjFobVVUp3pwHQdxGmBg1AbhKJDxaWfCPloEW7bD_P5rsSw6OAG_mmuPd9Lfg74UF8yekA_uXDnxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cee18be9c.mp4?token=ROCIRzAGVoE6mAtkHSm7exNJNWegNoReJJ_wOSrY68-mFzB_q66eNlOhAixA60QhNybpBqKxcICeQTRKeOYF8uSdDLWYvOG4p8P7-mWmYGbJ6Pm3oi_M4kD3Df5_zwQksz7T8xQ2gwe37Qzop5ifaPVOLBtg_jOATkdPZuj5UIjU4FV0sr0lJRagDoLfIulq99_fQxiK1L5749Vr-qf_ACv0KztSaHQwlffe4XT6VfCx39juwfAtDNGVZaay_LmB00ElIOO3DGjFobVVUp3pwHQdxGmBg1AbhKJDxaWfCPloEW7bD_P5rsSw6OAG_mmuPd9Lfg74UF8yekA_uXDnxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:من همین الان گفتگویی را با وزیر دفاع، پیت هگست، به پایان رساندم.
او چیز جالبی به من گفت. او به من گفت: "ما به جهان نگاه می‌کنیم، کشورهایی هستند که اراده جنگیدن در کنار ایالات متحده را دارند، اما فاقد توانایی هستند. و کشورهایی هستند که توانایی دارند، اما اراده ندارند."
او گفت: "فقط در اسرائیل است که هم اراده و هم توانایی را می‌بینیم."
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20014" target="_blank">📅 20:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الجزیره: شرکت امنیت دریایی امبری گفت که حداقل یک حمله پهپادی به یک تأسیسات ذخیره‌سازی گاز طبیعی مایع ایالات متحده در دمیاط، مصر اتفاق افتاد
تأسیسات ذخیره‌سازی شناور مورد هدف قرار گرفته متعلق به یک شرکت آمریکایی در دمیاط مصر است و توسط آن اداره می‌شود.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20013" target="_blank">📅 19:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سنتکام : تنگه هرمز یک آبراه بین‌المللی است.  سپاه پاسداران انقلاب اسلامی هیچ اختیاری برای تعیین مسیرهای تردد برای جریان آزاد و باز ندارد. کشتی‌های تجاری همچنان از این تنگه با حمایت نظامی ایالات متحده استفاده می‌کنند.  از اوایل ماه مه، نیروهای سنتکام به عبور تقریباً ۱۰۰۰ کشتی و ۵۰۰ میلیون بشکه نفت خام از این آبراه باریک کمک کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20012" target="_blank">📅 19:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">آسوشیتدپرس : ۶ نیروی مشاور سپاه قدس در حمله مشترک آمریکا و عربستان سعودی کشته شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20011" target="_blank">📅 19:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=RMPtDEpvRhpkVSaYQhHx2Usvzys18qD8E-Ik3ZgiscVT0-BPh0uAyPrD3HJ7Yb9RdsaxsOXwzcVscrnu7NPsouki1dkIM3r0P3VbhTwsja5JvcacNSLAVSdpj1GGZ_Xs5amIPdyZCX_6IZl3UVYGcNm9EQ1VISnXZ2PVne4gRVs-F-OF_WVaXgM3Lete25NPNBGnZPIqPWJrQh0Tf9QScOOHKqQyJo9cjPWeiBI3NVHrLJnthQviFOBFmn3Bhz7U4VrZR0V8hpJggXNh0k0cwyIcsw-HwzQr4P1X8Wm7G_CmUE4Y7_Zl6W1QUT1F7a72b4f-0i3bbB3pRCOn8rqeow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea64fcfef1.mp4?token=RMPtDEpvRhpkVSaYQhHx2Usvzys18qD8E-Ik3ZgiscVT0-BPh0uAyPrD3HJ7Yb9RdsaxsOXwzcVscrnu7NPsouki1dkIM3r0P3VbhTwsja5JvcacNSLAVSdpj1GGZ_Xs5amIPdyZCX_6IZl3UVYGcNm9EQ1VISnXZ2PVne4gRVs-F-OF_WVaXgM3Lete25NPNBGnZPIqPWJrQh0Tf9QScOOHKqQyJo9cjPWeiBI3NVHrLJnthQviFOBFmn3Bhz7U4VrZR0V8hpJggXNh0k0cwyIcsw-HwzQr4P1X8Wm7G_CmUE4Y7_Zl6W1QUT1F7a72b4f-0i3bbB3pRCOn8rqeow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو، با پیتر هگست، وزیر جنگ، در واشنگتن دیدار کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20010" target="_blank">📅 18:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو : جمهوری اسلامی، فرایند غنی‌سازی اورانیوم را در کوه کلنگ اصفهان آغاز کرده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20009" target="_blank">📅 18:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=bkz5VZ8-Au-WVyFJrdbsR1RaQ4WaVedhDob_z3_xPHAFGcJ99BkS82IbmlWvXfXXsvy1oWUA_hRsSLI2PpaZ4tM1vYIFN3ge6YSBPCggK6C645L4hRiwt0zPuwatKNZMVnxA7yq_jPaXzsbcSM4tWLbajyHIPKppWZRiLf68_o_O7aZGkwKDcpTlVfwWfHrT-EGUDYws0-w9s4SOpUjPb9xW158lMYishw6JjiB2lVvx9zc2KalXxap2jGv1sUwQH8VETe6iUZS1b7qsjKHGRUkZlpnzsGnfddPNbIV_jEhHUhjKFn4QcSRioCjJ1JOaJAeewyPhVvUVpjNLMB4vng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641e67f8eb.mp4?token=bkz5VZ8-Au-WVyFJrdbsR1RaQ4WaVedhDob_z3_xPHAFGcJ99BkS82IbmlWvXfXXsvy1oWUA_hRsSLI2PpaZ4tM1vYIFN3ge6YSBPCggK6C645L4hRiwt0zPuwatKNZMVnxA7yq_jPaXzsbcSM4tWLbajyHIPKppWZRiLf68_o_O7aZGkwKDcpTlVfwWfHrT-EGUDYws0-w9s4SOpUjPb9xW158lMYishw6JjiB2lVvx9zc2KalXxap2jGv1sUwQH8VETe6iUZS1b7qsjKHGRUkZlpnzsGnfddPNbIV_jEhHUhjKFn4QcSRioCjJ1JOaJAeewyPhVvUVpjNLMB4vng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20008" target="_blank">📅 18:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">زلنسکی:از ترامپ درخواست کردم که یک «بسته اضطراری زمستانی»، شامل ۳۰۰ موشک رهگیر پاتریوت را در اختیار اوکراین قرار دهد
اگر مشکل کمبود این موشک‌ها برطرف نشود، حملات روسیه نیروگاه‌های برق ما را نابود و یک بحران انسانی ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20007" target="_blank">📅 18:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه‌های حقوق بشری: اجرای حکم علیرضا سپاهی(فرد سوم در اصفهان)بعد از سکته قلبی متوقف شد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20006" target="_blank">📅 18:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پس از تهدید ترامپ علیه ایران: قیمت نفت هم اکنون به 90 دلار به ازای هر بشکه افزایش یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20005" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20004">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد نیروهای این کشور در جریان عملیات در روستای حداثا، واقع در منطقه حائل جنوب لبنان، تونلی به طول ۵۵ متر را کشف و نابود کردند که زیر یک کارخانه تولید مصالح ساختمانی و در نزدیکی یکی از مواضع نیروهای حافظ صلح سازمان ملل (یونیفل) در جنوب لبنان ساخته شده بود به گفته ارتش این تونل شامل سه اتاق بوده و حزب‌الله از آن به عنوان مرکز فرماندهی استفاده می‌کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20004" target="_blank">📅 16:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20003">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20003" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20002">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۴ : ترامپ درباره حمله ایران:  «قراره به باسن‌شان لگد بزنیم»
رئیس‌جمهور ترامپ پس از آنکه ایران موشک‌های بالستیک به سوی اردن شلیک کرد، وعده داد که پاسخی گسترده و سخت خواهد داد. این در حالی است که ایالات متحده و عربستان سعودی، در پی بیش از ۳۰ حمله پهپادی به نیروهای آمریکایی و تأسیسات نفتی عربستان، حملات مشترکی را علیه شبه‌نظامیان مورد حمایت ایران در عراق آغاز کردند
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20002" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20001">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دونالد ترامپ اعلام کرد حملات علیه مواضع شبه‌نظامیان وابسته به ایران با هماهنگی دولت عراق صورت گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20001" target="_blank">📅 16:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20000">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو شامگاه گذشته در اقامتگاه بلر هاوس با معاون رئیس‌جمهور آمریکا، ونس، دیدار کرد همچنین نخست‌وزیر نتانیاهو امروز با وزیر جنگ آمریکا، هگست، دیدار خواهد کرد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20000" target="_blank">📅 16:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19999">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک سرطان جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نفوذی جمهوری اسلامی هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19999" target="_blank">📅 16:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19998">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره ایران :
ما به آنها اجازه می‌دهیم که به وراجی ادامه بدهند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19998" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19997">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره ملاقاتش با نتانیاهو:
این یک ملاقات عالی بود. او اکنون متوجه شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19997" target="_blank">📅 16:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19996">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e251708c59.mp4?token=csGPLvq3POHFJ9ImkCBGAOGreBIQRPA9dG6vSfaLwhPHU9bPI-grEqVnyvwwzq5H7rYFkjfYuro9nxd2tsk932Vq8X1NL0RdDhokr3CAQqNlX6sGV3XRxKdZ1u9j1tT8-mhSDKAG3Ooio7ru3lRAxQBU-ipoaw2koL8YLFEEgQtlnsPYw95RPcGhnFRfl1RcwDriM8N_AEUx0iJ6WZiJoV3L2yIc5ZRgXX9G210WU82AaqZnacVonJ7hp02HQjKu9e_3XT955q60B1pRv3sB6vy0DaBaKk88HJ8Jib-XDEqJ9HSIaEiq4hpbKscisqg-algK39xIUgaUnuQICwaatx7FH_kI-HxuvU3dmgA3HD34XjKb42-zPPJ8vy4L-9Imoh5uywwvH_Wf4YtAutVY_uWB76UezE9HyHxNlS-i_3bwdOgKx9fl6MQ5BoXesuFpq-YJti0mdfBwJfzklq_58EsH4TJTSQX8ZJIL6e8pPRUSDiuZ8qPqonSevS4D7hFF7575NFboy8JySmlXPx0Zghf55yLPpQOCHfxfGLdzq1SaKFAeYrPd-byrmm3fskEmWy3CU2zFcv7vZPsCIfM2BZ7KrwY_CPSSeXXRLuG8qYSqPOaWeKgNE_NH0UkAHaT6NVAIWBI3EmhR-6tT-IAztg0uvaojdtp31fyy45Bg2yk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e251708c59.mp4?token=csGPLvq3POHFJ9ImkCBGAOGreBIQRPA9dG6vSfaLwhPHU9bPI-grEqVnyvwwzq5H7rYFkjfYuro9nxd2tsk932Vq8X1NL0RdDhokr3CAQqNlX6sGV3XRxKdZ1u9j1tT8-mhSDKAG3Ooio7ru3lRAxQBU-ipoaw2koL8YLFEEgQtlnsPYw95RPcGhnFRfl1RcwDriM8N_AEUx0iJ6WZiJoV3L2yIc5ZRgXX9G210WU82AaqZnacVonJ7hp02HQjKu9e_3XT955q60B1pRv3sB6vy0DaBaKk88HJ8Jib-XDEqJ9HSIaEiq4hpbKscisqg-algK39xIUgaUnuQICwaatx7FH_kI-HxuvU3dmgA3HD34XjKb42-zPPJ8vy4L-9Imoh5uywwvH_Wf4YtAutVY_uWB76UezE9HyHxNlS-i_3bwdOgKx9fl6MQ5BoXesuFpq-YJti0mdfBwJfzklq_58EsH4TJTSQX8ZJIL6e8pPRUSDiuZ8qPqonSevS4D7hFF7575NFboy8JySmlXPx0Zghf55yLPpQOCHfxfGLdzq1SaKFAeYrPd-byrmm3fskEmWy3CU2zFcv7vZPsCIfM2BZ7KrwY_CPSSeXXRLuG8qYSqPOaWeKgNE_NH0UkAHaT6NVAIWBI3EmhR-6tT-IAztg0uvaojdtp31fyy45Bg2yk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : بعد از حملات غافلگیرانه به نیروهای آمریکا در اردن، حسابی جوابشون رو می‌دیم
محکم بهشون ضربه می‌زنیم، حسابی تنبیه می‌شن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19996" target="_blank">📅 15:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19995">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">amme kojai(IG @yashar)</div>
  <div class="tg-doc-extra">TaTaloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/19995" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19995" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19994">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ:
حملاتی علیه ایران انجام خواهد شد و ما با قدرت به آنها ضربه خواهیم زد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19994" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19993">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19993" target="_blank">📅 15:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19992">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسپانیا پخش اذان از بلندگو رو در بعضی از شهرها مجاز اعلام کرد
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19992" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19991">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرگزاری رژیم فارس: تنگه هرمز بسته بسته است، دیگه از این بسته‌تر نمیشه.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19991" target="_blank">📅 14:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19990">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">هم اکنون هشدار های حمله موشکی/پهپادی در تلفن های شهروندان اردن نمایش داده می شود
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19990" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19989">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رویترز: فرماندهان سنتکام در حال بررسی امکان توقیف تلفن همراه سربازان آمریکایی جهت عدم انتشار تصاویر خسارات ها هستند
ژنرال براد کوپر، فرمانده ستاد مرکزی فرماندهی ایالات متحده (CENTCOM)، به نیروهای آمریکایی مستقر در خاورمیانه هشدار داده است که ویدیوهای ضبط شده با تلفن همراه و منتشر شده در اینترنت، به ایران کمک می‌کند تا میزان اثربخشی حملات خود را ارزیابی کرده و موقعیت‌های نظامی آمریکا را شناسایی کند.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19989" target="_blank">📅 14:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19987">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ed6y7I2P-gSsrdPShtHAQBmB3aZbfD4t1ET_3ubcVh_PUcceUHpiydK_KBLdJAJ26j4z90lqklcEEhmZktLw6HyMOWBMxyf73QPbPF7l23zZ-AqKMlhJtT0s46_0-D6cfiAQLkXEgiNZYOOFgU8svAE7qY_RVVrmyL5qdcEoHvbQIZ-2nXSzIFj1Cjdj9bdrqUqs-9WqK3xh97m8ZYr6C7-D6saW0PZ-3ZeA2RW7U-n6_QL_WdeVd-iQ4B5cGcvVxkamKa2RJCoYS3Ek5abtIk9cDg2hPSl7-q3caIJ5LFE4fxYtrYxgnIrf-J0-G_s6XTBytV--ZAyDvLx9o1yhhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gzzbRyjCB3Bu75JNzzr_Kr-Rm6yf07El4vCB2utcjKGVTWCCCkwlVSTEADp45ZBQ4-DTK87eepexG15DsJnjPfux8CwmB6rydRWBOkBhLP40vWUM3f_TCocDjLy2v1aHBjWltPf1pSwd2I2y480FqShVjLHbY_CfGZcv-iXHe5RaqidCYf47DhlO_DF3kFOZx0A3Q3JEUXWIBVeuNps2v1tTA7x6qBBEIjBMW5kQQZLLU3BhriNv3tTyTq7xlh3nM6HdZEBho31fHQamiOtgAtEYSPVBJUNUJQQJiihJ7uOOdxL2QNYRHdYQIR9tU8cPBqVcULyEUgOruYZonw3Jdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمله به شمال ایران ساحل خزر شهر
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19987" target="_blank">📅 14:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19986">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19986" target="_blank">📅 14:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19985">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تصمیم‌گیری در مورد ایران
کاخ سفید اعلام کرد که ترامپ امروز ساعت 18:30 به وقت تهران یک جلسه اطلاعاتی مهم خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19985" target="_blank">📅 14:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19984">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">زلنسکی به اکسیوس :  رابطه‌ام با ترامپ خیلی بهتر و سازنده‌تره ، مثل قبل دیگه این‌قدر احساسی نیست
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19984" target="_blank">📅 13:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19983">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش های تایید نشده رسانه های بومی و مردمی در خصوص حمله هوای به نوار مرزی پیرانشهر در ایران
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19983" target="_blank">📅 13:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19982">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش انفجار در عراق و اردن
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19982" target="_blank">📅 13:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19981">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19981" target="_blank">📅 13:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19980">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مشاور ارشد ترامپ: "ایران می‌خواهد حزب‌الله در لبنان فعال بماند، ما اجازه این کار را نخواهیم داد."
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19980" target="_blank">📅 13:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19979">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSpXAm_V6GL8Oem9F_hf6NWZYOLhHysUIU0cMzs3l5AUCHHiQjZoXrlw2z6tXTRGMoVb04QuNElHslw_E5oFC9avngvnkAmWOLXt7h0ONvV0fPYkYdfBRT3IihJ3MqXVsdoG_MrC715tQVZUL5D6StyL50gGnmnTuuzi7Tosj9UQbxaJQbSX6hMkzadzpJlLqtY7O1h7v0ntcZqafW6433PUBCyo_RdpZPBIKDI4pLXYQiVLMbNCLPUXJX4iwPaPzdZ7b2N37vY0hMoP0cgNx25xoe4aep4DtIorY58IAHywYeRfCTGrgB-fDvqOWVppvu5XLXh-Z5UqMwWoznjhbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل با انتشار این عکس نوشت : شاهزاده رضا پهلوی، ولیعهد ایران، با شرکت در مراسم یادبود سناتور لیندسی گراهام، به نمایندگی از ده‌ها میلیون ایرانی که برای آینده‌ای آزاد و دموکراتیک مبارزه می‌کنند، ادای احترام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19979" target="_blank">📅 13:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19978">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xaz2BgnGJ1ekb35HJ8TBQxMDqFSekNSNpcfqRw6mfss_qMUVzVdeAGAPoytFnUFQdLXksGjLgBIxJmuljo4fuwfkvvXWK2wUfBY5ttLbYfkjMqygOcaadTUvikRijRSNY-gruUFaCGRmPG03xDf3AH3AxVxkotpm3qOgdt35GFIdkXylAjrqletgsU7ArqnY_Vm18YfqkE8zB5t_tU7IcB2uEYAGkvdz5xPly5OAzf4kRTX4iMuOcROICC9ni-GIZy3dyCBYTVDRkdqvxYHy-kNhI81sTV46cDa_iyN7xwF0XDvlTCDb6kDt6IiORNqJNiI34x9E3HZguJbHatS2Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ حضور شاهنشاه آریامهر، ریچارد نیکسون، شارل دوگل و بودوئن، پادشاه بلژیک، در مراسم خاکسپاری رئیس‌جمهور ایالات متحده، دوایت آیزنهاور، که در تاریخ ۳۱ مارس ۱۹۶۹ در کلیسای جامع ملی واشنگتن برگزار شد…
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19978" target="_blank">📅 13:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19977">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی @WarRoom وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط…</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19977" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19975">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏استیو استکلو، خبرنگار ارشد رویترز و برنده سه جایزه معتبر پولیتزر در گفتگو با شاهزاده رضا پهلوی و گفتگو دیگر تکمیلی او با بی بی سی فارسی
@WarRoom
وی در این مصاحبه به نکات بسیار ریزی اشاره و خودش همچنان اذعان میکند که شاهزاده را به چالش کشیده و وی خیلی مسلط و با تجربه به او پاسخ داده.</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19975" target="_blank">📅 12:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19974">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الحشد الشعبی: بر اساس آمار اولیه، دست کم ۲۰ مجاهد کشته و ۳۲ نفر دیگر زخمی شدند. این آمار مربوط به حملاتی است که توسط ائتلاف آمریکا و عربستان سعودی انجام شد و تعدادی از مقر‌های رسمی الحشد الشعبی را در چندین استان عراق هدف قرار دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19974" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19973">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش‌ تایید نشده شنیده شدن صدای پرتاب موشک از ‌کرمانشاه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19973" target="_blank">📅 11:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19972">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromElahe</strong></div>
<div class="tg-text">سلام وقتتون بخیر
شما که انتقاد میزارین تو چنل
لطفا لطفا قدردانی ماهم بزارین از این همه تلاش ها و اخبار کامل درستتون خسته نباشید به امید دیدار در میدان آزادی عمو یاشار
🙏
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19972" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19971">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff38dea688.mp4?token=rdIfehEyVj66yyP3vz-XnsJ2XqUc7qfJbWR9j5_Kv_qNElN4qfb49xqITMQpeFG1H_OF7pYrj9afVh45QOoGhg-r7Q0XqS5DGN7mZAb8tKxxmMZiw61aLyyY_RDQtalma36dC0vKM-NqWdEOTC_WvnJaAnQ6JRe-OOoQNMFTB0jhGDBulgbsIhm517KNOKZLAzrbsz949HbcbPsE08J9bDh7w-2zDImD9h_Ar9wbtH4kY_vlKgi_4CBEdaCQKd_QtXIKoFNpvSz0N5rBjijKQ-rV-g4YY2hL9NS08a65md_YCAfi7iUCfTGLjyLyk6nFyueC9OU_0N8bdKwI1BDBrDfciRoF69aaJcCZRFlcAgDNOZwFAguPkHBG7GXlYHUZQyknKizB6-P9xkY358wDOeLF0kyp5WABn7Px1V6D6DhNyd24wrMM4U4kl7XIXNFy9VIoimRON6dikhCHyH6VuB4RyTsO_lMQBivIg7fcJHFirNnccwT8odcUkDaO17N40VJ3G-jhB2QzTqJmu_3s5hMwo4wY_Z6zprGreV7PkuAcRcjpMKocgzfVUFITPjkNrOkc6pAZ1_V2520GBAgaQ7s5Qbh8FoRf1X9oppZ8jXFtYwPFS24fkDza_HPU7VBf24wzMdNT5YJtQJObEVGYdpabHh88l1rIpUVZJX21QM0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff38dea688.mp4?token=rdIfehEyVj66yyP3vz-XnsJ2XqUc7qfJbWR9j5_Kv_qNElN4qfb49xqITMQpeFG1H_OF7pYrj9afVh45QOoGhg-r7Q0XqS5DGN7mZAb8tKxxmMZiw61aLyyY_RDQtalma36dC0vKM-NqWdEOTC_WvnJaAnQ6JRe-OOoQNMFTB0jhGDBulgbsIhm517KNOKZLAzrbsz949HbcbPsE08J9bDh7w-2zDImD9h_Ar9wbtH4kY_vlKgi_4CBEdaCQKd_QtXIKoFNpvSz0N5rBjijKQ-rV-g4YY2hL9NS08a65md_YCAfi7iUCfTGLjyLyk6nFyueC9OU_0N8bdKwI1BDBrDfciRoF69aaJcCZRFlcAgDNOZwFAguPkHBG7GXlYHUZQyknKizB6-P9xkY358wDOeLF0kyp5WABn7Px1V6D6DhNyd24wrMM4U4kl7XIXNFy9VIoimRON6dikhCHyH6VuB4RyTsO_lMQBivIg7fcJHFirNnccwT8odcUkDaO17N40VJ3G-jhB2QzTqJmu_3s5hMwo4wY_Z6zprGreV7PkuAcRcjpMKocgzfVUFITPjkNrOkc6pAZ1_V2520GBAgaQ7s5Qbh8FoRf1X9oppZ8jXFtYwPFS24fkDza_HPU7VBf24wzMdNT5YJtQJObEVGYdpabHh88l1rIpUVZJX21QM0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به فاکس نیوز:
"به این رژیم نگاه کنید. به عربستان سعودی، کویت، بحرین و امارات متحده عربی حمله می‌کند.
ده‌ها هزار نفر از شهروندان خود را به قتل رسانده و معلول کرده است.
این کاری است که وقتی سلاح هسته‌ای ندارد انجام می‌دهد.
حالا تصور کنید که اگر سلاح هسته‌ای داشتند، با جهان چه می‌کردند."
مشکل عمیق‌تر این است که همین منطق هرگز پایانی را مجاز نمی‌داند.
رفتار بد ایران ثابت می‌کند که نمی‌تواند بمب داشته باشد؛ امضای توافق توسط ایران ثابت می‌کند که در حال خرید زمان است.هر نتیجه‌ای فقط به فشار بیشتر منجر می‌شود. من در مورد توافق با ایران شک دارم و این را آشکارا می‌گویم
‏هر بار که توافق نزدیک است، تندروها می‌آیند و به کشتی‌ها در تنگه هرمز حمله می‌کنند.موضع ترامپ بسیار واضح است و ما تعهد مشترکی داریم. ما نمی‌خواهیم ایران سلاح هسته‌ای داشته باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19971" target="_blank">📅 10:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19970">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fe5166c98.mp4?token=Qe8dwgGgGoMOuOUBn6L1p-djT76LycxSINcpI2LZ9pt3_P1WlPh-LsQOO1oti4jstGgTnL0To8bVu2fvDsfsWX1eByg7Ss3QQP9sENIbDGR5u5R_chHBCQ-hnYuTb4-zKHfa-7VtReP86Pyny-HcQQ41kSNZ9bOTYGQoJlhWl-HGNDh9--9_kobnQ-8l4D62NTszwTBWIEuCmk767i0efCFvhSSBTWFwnEwuzh-aqXZszUAe9XXiMUZrtjYweNkGc2r7C3Rx7ZLJeMN5y1v7-276tvLdzZ7aXY-uCj-Cyfc66E9tt6XurR8EhhBbJwioqu-y7JJkcdPNZX3EmPgcnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fe5166c98.mp4?token=Qe8dwgGgGoMOuOUBn6L1p-djT76LycxSINcpI2LZ9pt3_P1WlPh-LsQOO1oti4jstGgTnL0To8bVu2fvDsfsWX1eByg7Ss3QQP9sENIbDGR5u5R_chHBCQ-hnYuTb4-zKHfa-7VtReP86Pyny-HcQQ41kSNZ9bOTYGQoJlhWl-HGNDh9--9_kobnQ-8l4D62NTszwTBWIEuCmk767i0efCFvhSSBTWFwnEwuzh-aqXZszUAe9XXiMUZrtjYweNkGc2r7C3Rx7ZLJeMN5y1v7-276tvLdzZ7aXY-uCj-Cyfc66E9tt6XurR8EhhBbJwioqu-y7JJkcdPNZX3EmPgcnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنا با ۸۶ رأی موافق در مقابل ۱۲ رأی مخالف، لایحه تحریم‌های دو حزبی روسیه و ایران را که توسط سناتور فقید لیندسی گراهام مطرح شده بود، تصویب کرد.
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19970" target="_blank">📅 10:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19969">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">رویترز: انتظار می‌رود ایران در چند هفته آینده، اولین محموله از تا ۴۰۰ سیستم دفاع هوایی قابل حمل چینی (MANPADS) را دریافت کند. ارزش این معامله حدود ۶۰ تا ۷۰ میلیون دلار تخمین زده می‌شود. طبق گزارش‌ها، این سیستم‌ها شامل مدل‌های QW-12 و FN-16 هستند و هدف از آن‌ها بهبود توانایی ایران در مقابله با هواپیماها، هلیکوپترها و پهپادها در ارتفاع پایین است.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19969" target="_blank">📅 10:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19968">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نیویورک تایمز: ایران به این فکر کرده بود که یک حمله موشکی نمادین به یک بندر اوکراینی در دریای سیاه انجام دهد، پس از آنکه گزارش‌هایی منتشر شد مبنی بر اینکه اوکراین یک کشتی باری ایرانی را در دریای خزر مورد اصابت قرار داده است.‏
به گفته مقامات ایرانی و غربی، تلاش‌های دیپلماتیک تاکنون از تشدید تنش‌ها جلوگیری کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19968" target="_blank">📅 09:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حکومت ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19967" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAgFWJuHGq1-wUETQ28Cuw5J3jzLInvR0jQLRr6SiVgdIqLLf426rb9iG3w1Upbr_oPjUNhILp1PYWg1wBfsqGRILtKZhJFbwyWnAFibloCrGHY0NvQJEUY7gOxogJBs05n2huhQNX102ajzpBGB3cofz9-2JGHZ1_fQ3lJDYQ2AONeBXWFgjx2q1Pz20J4EIPTTsWHc980bMn4MSfbvY6EDY2cquG7aBiTiljLqve2Am-iH9zPbcwVd7HFg_iphqSVtpaV5WZiKQrsM9JFuRzBMzYgJtcwGvR-_WpbFWmT30cWhi_-i5bgJ6z2swh_78haQmDMZD32InlV34JhpuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی هوایی جمهوری اسلامی اعلام می‌کند که پیکر سرتیپ خلبان مجید کاظمی، خلبان یکی از بمب‌افکن‌های تاکتیکی Su-24MK که در تاریخ ۲ مارس توسط جنگنده‌های ابابیل F-15QA نیروی هوایی قطر در حین تلاش برای حمله به پایگاه هوایی العدید سرنگون شد، پیدا شده و ظرف چند ساعت آینده به ایران بازگردانده خواهد شد.
نیروی هوایی جمهوری اسلامی افزود که مقامات ایرانی همچنان در تلاش برای تعیین محل سه خلبان دیگر Su-24MK سرنگون شده هستند و جزئیات مراسم تشییع جنازه مجید کاظمی متعاقباً اعلام خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19966" target="_blank">📅 09:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b466899a00.mp4?token=Rqy_cmegj98U6d_HTJiS0ba74uuGvOHyO35L_csN2Q9YBBnRcnG_sY32QIXx5FVPFGYUBbBcYFzqKiCOMUm1KSUTB3DyC2AazDL_caaamiVQwO175V5A2zMhiUN898e_6JvnxD_qAYJuggK3extTk2guYzE1YcAYxfcku9zYMRRi9Nb9IYaVhgGO-Jl4_a8JcPdAw_s943vXgqXOrQB27ybmgXl-8NFhSBc6O6fEL6XJYSBV7eYA_4bEfyGau1xo2rYuIHIVCgeu4xIk2dSEhJAIC2jFuBCTFYN-1t8CRY0RLgMBwoQeQbyjmJXte-45ajDNzL83UiCUybViKtdobif0Sm7HODhNtqFYDxn3Seiyl9rf3acfhCNs8_SPlijbTBW9iVxr71IjXWbUxlKY9xc-kKzUYO3SGYPZudoZQMQI6yHHtxLlHy_NaD0fRFpvFIFDAoF6aua_YJGZUjXxpJbZ0t92uTjYqYE3R2w1RDJW5Y9L7ETq_xYkzSXGdvOdDo8rlkBld4qvirpu6mlFvOECs_uR_iOZI-z5uxMQ98ublYJSyy_TRhK9Dka-V5wUmq1GGqbfZxTqZjKf0cswxK0oOq_EvYWyvTxshK-S0HSSOvqt6JD9nwDGWDZYqFHEyMgvD3C9o5pveuiTTFk8Q95SilejZ0VKhLDwE0QX7DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b466899a00.mp4?token=Rqy_cmegj98U6d_HTJiS0ba74uuGvOHyO35L_csN2Q9YBBnRcnG_sY32QIXx5FVPFGYUBbBcYFzqKiCOMUm1KSUTB3DyC2AazDL_caaamiVQwO175V5A2zMhiUN898e_6JvnxD_qAYJuggK3extTk2guYzE1YcAYxfcku9zYMRRi9Nb9IYaVhgGO-Jl4_a8JcPdAw_s943vXgqXOrQB27ybmgXl-8NFhSBc6O6fEL6XJYSBV7eYA_4bEfyGau1xo2rYuIHIVCgeu4xIk2dSEhJAIC2jFuBCTFYN-1t8CRY0RLgMBwoQeQbyjmJXte-45ajDNzL83UiCUybViKtdobif0Sm7HODhNtqFYDxn3Seiyl9rf3acfhCNs8_SPlijbTBW9iVxr71IjXWbUxlKY9xc-kKzUYO3SGYPZudoZQMQI6yHHtxLlHy_NaD0fRFpvFIFDAoF6aua_YJGZUjXxpJbZ0t92uTjYqYE3R2w1RDJW5Y9L7ETq_xYkzSXGdvOdDo8rlkBld4qvirpu6mlFvOECs_uR_iOZI-z5uxMQ98ublYJSyy_TRhK9Dka-V5wUmq1GGqbfZxTqZjKf0cswxK0oOq_EvYWyvTxshK-S0HSSOvqt6JD9nwDGWDZYqFHEyMgvD3C9o5pveuiTTFk8Q95SilejZ0VKhLDwE0QX7DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید و پر معنی کاخ سفید
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19965" target="_blank">📅 09:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bf785ac3.mp4?token=QBzLrB8WNtmjHhnAG9uRXRN59NGaGMpES3ZuioeIIHLFZVzM5q8HeBwsxHUIM1j4lcLj0p3FPnujWGYwBBF89uJG0RUshxz1oYNUh2I9Y-eMP-7iAEICKuvckO-T8rB2M3sjAPmdyXI9JNfDJXm5J9eGXUDLO5ZDWivdZUlg5IxK7kcxQh3JrNXqk2f4gaJEkDDDCXqgKdEkLpM641abUqmwmN2_otiS7HoCR2xI6iFUCgPnzaw3Wo_QdwaigzrIYzIEJ1T_wKRvv8tyWju1qXtokOKNwe1D2ZPtQjfvIj4lIRZ4zSEOtCN2JztTFu6OkJPAU_Nh5pFNsqr8S_x_Ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bf785ac3.mp4?token=QBzLrB8WNtmjHhnAG9uRXRN59NGaGMpES3ZuioeIIHLFZVzM5q8HeBwsxHUIM1j4lcLj0p3FPnujWGYwBBF89uJG0RUshxz1oYNUh2I9Y-eMP-7iAEICKuvckO-T8rB2M3sjAPmdyXI9JNfDJXm5J9eGXUDLO5ZDWivdZUlg5IxK7kcxQh3JrNXqk2f4gaJEkDDDCXqgKdEkLpM641abUqmwmN2_otiS7HoCR2xI6iFUCgPnzaw3Wo_QdwaigzrIYzIEJ1T_wKRvv8tyWju1qXtokOKNwe1D2ZPtQjfvIj4lIRZ4zSEOtCN2JztTFu6OkJPAU_Nh5pFNsqr8S_x_Ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به فاکس درباره ایران گفت:
آن‌ها باید بدانند که اگر به ما حمله کنند، ما با قدرتی بسیار شدید پاسخ خواهیم داد. آن‌ها در درگیری‌های اخیر به ما حمله نکردند، به خاطر همان چیزی که همین الان گفتم.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19964" target="_blank">📅 09:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19963">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏گروه تروریستی سپاه پاسداران مدعی شد که در ادامه تشدید درگیری‌ها، سه نفتکش را در تنگه هرمز با حملات موشکی و پهپادی هدف قرار داده است. بر اساس این ادعا، نفتکش‌ها پس از اصابت متوقف شده‌اند. این ادعا تاکنون از سوی منابع مستقل، شرکت‌های کشتیرانی یا مقامات بین‌المللی تأیید نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19963" target="_blank">📅 09:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19962">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سنتکام : ما و نیروهای مسلح عربستان سعودی در ۲۸ ژوئیه حملات دقیقی را در عراق علیه تروریست‌های همسو با ایران انجام دادند که سپاه پاسداران انقلاب اسلامی (IRGC) آنها را برای حمله به نیروهای آمریکایی و زیرساخت‌های انرژی عربستان سعودی هدایت کرده بود.
جنگنده‌های ایالات متحده و عربستان سعودی در پاسخی قوی به بیش از ۳۰ حمله پهپادی هوایی به رهبری سپاه پاسداران در ۷۲ ساعت گذشته، چندین سایت لجستیکی و تسلیحاتی تروریست‌ها را در سراسر شرق عراق هدف قرار دادند.
این حملات بی‌دلیل علیه نیروهای آمریکایی موفقیت‌آمیز نبود.
از فوریه تا آوریل ۲۰۲۶، بیش از ۶۰۰ حمله ناموفق به شهروندان و تأسیسات آمریکایی توسط شبه‌نظامیان تروریست همسو با ایران در عراق صورت گرفته است. سپاه پاسداران و گروه‌های تروریستی نیابتی آن باید این حملات را متوقف کنند تا از واکنش نظامی بیشتر ایالات متحده جلوگیری شود.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19962" target="_blank">📅 09:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19961">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عربستان : عملیات ریاض علیه عراق با هماهنگی سنتکام انجام شد
این حملات در پاسخ به حملات پهپادی گروه‌های وابسته به ایران در عراق علیه تأسیسات نفتی عربستان صورت گرفته
ریاض برای کاهش تنش‌ها در منطقه تلاش می‌کرد، اما این گروه‌ها ادامه اقدامات خود، مسیر تشدید تنش را برگزیدند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19961" target="_blank">📅 09:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19960">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بصره عراق مورد حمله نظامی از سوی عربستان سعودی قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19960" target="_blank">📅 03:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19959">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجار انبار مهمات در مقر فرماندهی عملیات حشد شعبی، بصره
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19959" target="_blank">📅 02:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19958">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ایرنا:
سنتکام دروغگوعه، تمام موشک‌های ما اصابت داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19958" target="_blank">📅 02:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19957">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدای جنگنده از کیش به سمت جنوب ایران
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19957" target="_blank">📅 02:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19956">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رسانه های داخلی : به اربیل عراق حمله پهپادی شده و جنگنده‌های آمریکایی بلند شدن.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19956" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19955">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اخبار حاکی از فعال‌سازی سیستم دفاعی "پتریوت" در آسمان جمهوری آذربایجان، کشور همسایه ایران، است.(تایید نشده هست)
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19955" target="_blank">📅 02:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19954">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gseemSDRxK0MOc20vbLm7JJCRyCs72WnXJHgQu1DFp7YDFupOGM8sKKE7GMPHEDeiFefra9vMA-CTVpUKzHjRfQTqcpGAh4rEokmHNsc0SUz04vueGr7UaVRjN-H7GWj7Akq4tr_kSc63NnMsWQSlXQKU9_KSAs4Y5bPpnzeegg0W6Xh7kcWARnHq3vK3MDPts3ZK9-Qc1blQ3i_vIwBUGV60Ragh-sHUQzqQ1JSIfqS2CIUwKhFHBL7nzSBn4qDSl_RLUTdYMzMOLp15XbVB3_oicBHOMZ9YivzI43VhaOjgY1nlNk_TuYZ8P0nVqqUxJF4DTcZH8VXbmGmgrRHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگاهی به برد موشک های سپاه به اکراین
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19954" target="_blank">📅 02:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19953">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سپاه به اربیل عراق حملات سنگین موشکی/پهپادی کرد و چندین انفجار تو اربیل شنیده شده
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19953" target="_blank">📅 02:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19952">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار : دربون جهنم سابقه نداشت خبر از حمله سپاه بزنه! بدجور برد کوپر بد خواب شده ، مادر بگرید
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19952" target="_blank">📅 02:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19951">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19951" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19950">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">منبع آمریکایی به شبکه i24NEWS گفت که جمهوری اسلامی حداقل 4 موشک بالستیک به سمت یک پایگاه آمریکایی در اردن شلیک کرده است و این اقدام را یک "حمله بزرگ" توصیف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19950" target="_blank">📅 01:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19949">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">چنل و اینستاگرام رو فردا پرایویت میکنم یه مدت ، اگه فالو ندارید فالو کنید نمونین پشت در پیش عرزشی ها
t.me/WarRoom
instagram.com/yashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19949" target="_blank">📅 01:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19948">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">من نمیدونم رسانه ها برای اینکه جو بدن چرا اطلاعات غلط میدن مردم اصلا آتش بسی نبود که بخواد نقض بشه. یه حمله شد، یه جوابی داده نشد. یه طرف کوتاه اومد، ادامه نداد! الان جواب اومده جواب داده
😁
چون نفت داشت میومد پایین فشاری شدن
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19948" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19947">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مقام ارشد آمریکایی: ایران موشک‌هایی را به سمت پایگاه آمریکایی در اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19947" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19946">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمانده سنتکام بردلی کوپر رو از خواب بیدار کردند
👺</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19946" target="_blank">📅 01:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پرتاب موشک جدید از غرب ایران
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19945" target="_blank">📅 01:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">گزارش‌های تایید نشده از اصابت یک موشک به مرز اردن و اسرائیل و پایگاه آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19944" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=qtxU46KNJdkEqIWDaTeaO-r29WlWab-sGb4VGti5YdG9wW-Cu8q2_KJ67FpwW-L8NS3meTfBpZXZOxsbJ7fo1WlezgjyQEUxKpVFngGqSsx_GPN5Wa0Rjd8vuuqW_KINfiWY8yT6Vfi7FtZZSqPk8RzZ1jt6aXqcyuEFCqE0OLaKoeSU74dM7hBS8fWuKvznomRZE1zNWC2TRg1yiSU4rgbIGjFT7sCXINKb01GieAmABBO4FQKdnJgzPbJni3jckj1xvDzaZIkg7pu_X0KZmEQLNfjYd5NJkohSltyPOsGit_Z_7k3sGE-ZtvGRZEm-r2-YvdKCnPex_oV42G7QxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87354e52d8.mp4?token=qtxU46KNJdkEqIWDaTeaO-r29WlWab-sGb4VGti5YdG9wW-Cu8q2_KJ67FpwW-L8NS3meTfBpZXZOxsbJ7fo1WlezgjyQEUxKpVFngGqSsx_GPN5Wa0Rjd8vuuqW_KINfiWY8yT6Vfi7FtZZSqPk8RzZ1jt6aXqcyuEFCqE0OLaKoeSU74dM7hBS8fWuKvznomRZE1zNWC2TRg1yiSU4rgbIGjFT7sCXINKb01GieAmABBO4FQKdnJgzPbJni3jckj1xvDzaZIkg7pu_X0KZmEQLNfjYd5NJkohSltyPOsGit_Z_7k3sGE-ZtvGRZEm-r2-YvdKCnPex_oV42G7QxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان اردن ، پدافند درگیر شده
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19943" target="_blank">📅 01:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNxLC1UlKcZs6HFMQYGX8gvyOQVrxS3OX1aHx2MQ2leFto8js1L3SP_IM9I8U6Izq7Nao4FihVUzQQyvbGpgFmrAwQxneBmjc6utAwxMk0nWigljTzN8oOYdgU7gBnY2NHDQ9B386yw4smvxzSfPTuQIF46kIVkXzDz1WtHmGW-fwJGkPakWVp33rDF37l2-2LYffY7hMTWdN7jajBAmZWspeLSUIpv7iQfr2oYn_A8UgqkpCEpwgzz0JF2bPhUPelwqG7kWCwXPF2ywCNmypaZ-tXjuSy9cu1bMmZscNJit5f-lJdR-8KXGwyMrPysxLjz40bfRxdQEmosvSjCULQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر موشک ها
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19942" target="_blank">📅 01:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فک کنم نتانیاهو با گوشی ترامپ به مم باقر فحش ناموسی داد</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19941" target="_blank">📅 01:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19940">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGiaHStLS_gthrKy3zS9JyFu_MMVUq9LU9YeHdEUo6rWBVVkSeWf8-u3CPbsJEZFKIGpfFzi6Kq0RHCgo_4M2NJttPxcy4RP3lH92FmTYErB_KnHQ99vcN2cajOh5QZejv11zzNA1eurNsin_IKQlxUIiQbJBOqkYdY86Mu-UwJjDE2lbwZ7A8tuE-uPMnkp0yRpBGbdYkwRLx4sZVyW1lhOIukWQ7I1IXdyjlHB37yaZPAW1d2STSvJOB3CU4ANgG-xc4MddxbzWtyfodt_aLOFtuPsbB-7pseh1SZVXV-P9MEE_kt94ywxczYSLaO4oo4dqVnHzacUjMbTApSCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک ها در آسمان خرم آباد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19940" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19939">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آلارم اردن فعال شد
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19939" target="_blank">📅 01:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19937">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/caVgWQvyY6OeJwrQj_LHSvT_ho-3bmIXzENz6xXzgS4KPsQe4MmmrsA3DpF_ExtRu_lFbAk6AoNpPMHvQqFLvCuBiECtceQv2yt2xlgsrMbGRzkzhaEjOgdCAg-ToRigsqrf8NjDJdixl5faNQ_o-00faxU-mBeNDbdPIE5dTAFfMFWcdwLHmD2vyxoNFJopSf_6fe6RnEiyWtCtlYkfWhgCntI_LbOpypxIjhu8BGfHAQXaHISPhvqMxug7tQUZ-daDXwts4rJX1waMTK-HoYze_y9-NeIJ7imWvveFyp5Q87ClNpv1a4fECWA7L7MtJmKzXUSreJM4gJ7sx5K76g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpsRO4hMqGX5lf8xeKDi-DhV_MbAPGvjhHcwxgJsiXE04SCn2InLgJpRdsJ1xAFfW71SrjnlGt1EADCXMNxKK_C0tSfj55oPG28E310K-JsBDNVrMf-9EB9GBRPI_VHh_CKktlW6V0_Nk-_i4FjGamJb1PN9a3_sQIoFHRx1-MEmYwY2w40gYV6fQe6gZNg_Ffuv_XocxCApH8fZCUS1c3WsRv7vAy7yanIIoa0gzqby2cNLrueUdLcXdsskj6_ETd5tuntl2DGLIDJbx-J3nyOK7sAbSTkkSUW5v7m77bqEfGfuCviw4u9vBL0fsD0p_h7g1jn1nmYNox7smUycww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شلیک ۳ موشک از خمین به اردن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19937" target="_blank">📅 01:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19936">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کانال i24 عبری : تنها چیزی که ترامپ را به سمت امضای توافق با ایران سوق داد، قیمت نفت بود.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19936" target="_blank">📅 01:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19935">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=nfQda9uRSK-hvuahMoFI7d1WlOtGr3KtxvcCfvVzdgJ_bszUOfcRABzN-QJNyi-XnIXiRUyZJ7domkyysXs2LQxoWf0PK0kIB1cIynExyDVDDLIiS4T5IJ7apFEMWgeOf6bX-oOkw4LoMny_TtqMu0y9AmbifZTX-4eehIIVIwd_wOAa1IqM_3WrQIQ-MMWFqayp2mOo9wWXSmaE9VeCeBmj7cXBH0AwJgnzb9oP92-Dv1uo2r-D5jFtJKTRGV0e-BRXVvCA8mRBtMXwF9ibZzHwm1sMF5UyPPuvdLUiKlRNtUZ-cioMdId03Hb8dLfsfvMKr6QQaHu6tGr5qm0_m2JEsZzRQcUAn22E1k9rRzCVPjLIbhfJyHlIHVhvngeI1uw4a6WMgnowpyeuVvw3YtMKUqhiGKVho7sHHPiZ05hf0QURU7Ft_XQ-zrWeoDDHskv0XXLdQspX-k_zoDuXEY_W2fT0LB04-aUCpzytD5IeNfBjcWDcc4XtNtEu_fm_yDunKCoXp1Xowh2dMsDdjVEHcVobJP5kRKJZJRctni156MMmstdnKCSUXJMl7syRF1aayB80la1Mazf8vXh30AT95g9uqUUEWWgdjbpOYt6JS34ywxNVRq1xbbACl9A6nNQA2Yp7K50qo9yZ3gMIVY3xhLSijFpOv2P1wmcI01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49ddcbdc52.mp4?token=nfQda9uRSK-hvuahMoFI7d1WlOtGr3KtxvcCfvVzdgJ_bszUOfcRABzN-QJNyi-XnIXiRUyZJ7domkyysXs2LQxoWf0PK0kIB1cIynExyDVDDLIiS4T5IJ7apFEMWgeOf6bX-oOkw4LoMny_TtqMu0y9AmbifZTX-4eehIIVIwd_wOAa1IqM_3WrQIQ-MMWFqayp2mOo9wWXSmaE9VeCeBmj7cXBH0AwJgnzb9oP92-Dv1uo2r-D5jFtJKTRGV0e-BRXVvCA8mRBtMXwF9ibZzHwm1sMF5UyPPuvdLUiKlRNtUZ-cioMdId03Hb8dLfsfvMKr6QQaHu6tGr5qm0_m2JEsZzRQcUAn22E1k9rRzCVPjLIbhfJyHlIHVhvngeI1uw4a6WMgnowpyeuVvw3YtMKUqhiGKVho7sHHPiZ05hf0QURU7Ft_XQ-zrWeoDDHskv0XXLdQspX-k_zoDuXEY_W2fT0LB04-aUCpzytD5IeNfBjcWDcc4XtNtEu_fm_yDunKCoXp1Xowh2dMsDdjVEHcVobJP5kRKJZJRctni156MMmstdnKCSUXJMl7syRF1aayB80la1Mazf8vXh30AT95g9uqUUEWWgdjbpOYt6JS34ywxNVRq1xbbACl9A6nNQA2Yp7K50qo9yZ3gMIVY3xhLSijFpOv2P1wmcI01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: به نظر شما چه صلاحیت‌هایی برای رهبری یک دولت انتقالی در ایران دارید؟
شاهزاده رضا پهلوی: اگر یک وکیل تصمیم بگیرد پرونده‌ای را به صورت رایگان بپذیرد، آیا این به معنای آن است که او شغلی ندارد؟ من چهار دهه است که این کار را داوطلبانه و رایگان انجام می‌دهم، درست است؟ به عنوان فداکاری من برای کشورم.
من می‌توانستم به راحتی در قاهره، زمانی که پدرم فوت کرد، تصمیم بگیرم: "می‌دانی چیست؟ به جهنم." من می‌توانم مانند بسیاری دیگر، زندگی، تجارت یا چیزهای دیگر را دنبال کنم... اما تصمیم گرفتم به خاطر کشورم در آن بمانم.
این یک فداکاری شخصی برای یک عمر بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19935" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19934">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=RQ5zHy1LnVn3iAY7F6bwq2rkgvFxdP3-2jcW6IN04xJ-IpNCHP_rGMqw9lg_OnXW8kfxl0jEPs17FXpM24lrONpClU6v3ty1Bx-VqRlNkE96f_J6e2HvFfT6w8fadXd6gleTvDXr2qHsgcFTlLx_z5mCDTjkhzZz6BFg5GadZCFIwWC_xOxaxHqnp8GGBAGZSdWwbkVh2N7xX8WIB-FauVLuvF3kfPUBXH6_WzrOBeOyxMkAiybT6ijNHAThDfQ45slUtglU7cN0zg12duUAHhsfV24yztxlwNAR_3ytGBZgACeXj2Bj8evTQf3aqD4L95Pj-UZkQkQtogijJgSRpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba487c3af7.mp4?token=RQ5zHy1LnVn3iAY7F6bwq2rkgvFxdP3-2jcW6IN04xJ-IpNCHP_rGMqw9lg_OnXW8kfxl0jEPs17FXpM24lrONpClU6v3ty1Bx-VqRlNkE96f_J6e2HvFfT6w8fadXd6gleTvDXr2qHsgcFTlLx_z5mCDTjkhzZz6BFg5GadZCFIwWC_xOxaxHqnp8GGBAGZSdWwbkVh2N7xX8WIB-FauVLuvF3kfPUBXH6_WzrOBeOyxMkAiybT6ijNHAThDfQ45slUtglU7cN0zg12duUAHhsfV24yztxlwNAR_3ytGBZgACeXj2Bj8evTQf3aqD4L95Pj-UZkQkQtogijJgSRpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: گزارش‌هایی، تقریباً ناشناس، مبنی بر دریافت بودجه از اسرائیل و عربستان سعودی توسط شما وجود دارد. آیا این درست است؟
شاهزاده رضا پهلوی: کاملاً نادرست. من هیچ بودجه دولتی یا عمومی از خارج دریافت نکرده‌ام.
هر ریالی که به کمپین من می‌رسد از کمک‌های خصوصی حامیان است. امیدوارم خیرین بیشتری داشته باشیم که چک‌های بزرگتری به ما بدهند.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/19934" target="_blank">📅 00:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19932">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز به نقل از یک مسئول آمریکایی: توافقی که در حال بررسی است و مربوط به تنگه هرمز، مربوط به هماهنگی است و شامل هیچ‌گونه عوارض عبوری یا هزینه‌های دیگری نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19932" target="_blank">📅 00:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19931">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=Why5w9IVST4aR5j0RTJHkT8Bl2JJCiL1haOOJTsTxHMwbE6Gdmn8_EQHeKuxZ2dBzSlXp8KkR5CD_RJpnjdZfmX1s59jbWuPGdRSUpCl45lP8sbmmVF9cRIbnctPb0fvCtspCxYUbr9nBN3IRIVzct84GwkK_T0nPELkYEnMrBAv4s9JX19KdoZ_JkpRu5UB_LC3gy93aYa1FB6cmgwXmaPG2_jSKdUitqR43nAzFN-t5AV9tfOvsNmnYYTEHAELQZUs0A6UnLsysTDB-ltOBlXpyHCCGDghRruw5HqFJLmGHRaR3VFqR5fel85puQR6T0ZmDzj3UV1ptI4Qj6CutIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4dee73717.mp4?token=Why5w9IVST4aR5j0RTJHkT8Bl2JJCiL1haOOJTsTxHMwbE6Gdmn8_EQHeKuxZ2dBzSlXp8KkR5CD_RJpnjdZfmX1s59jbWuPGdRSUpCl45lP8sbmmVF9cRIbnctPb0fvCtspCxYUbr9nBN3IRIVzct84GwkK_T0nPELkYEnMrBAv4s9JX19KdoZ_JkpRu5UB_LC3gy93aYa1FB6cmgwXmaPG2_jSKdUitqR43nAzFN-t5AV9tfOvsNmnYYTEHAELQZUs0A6UnLsysTDB-ltOBlXpyHCCGDghRruw5HqFJLmGHRaR3VFqR5fel85puQR6T0ZmDzj3UV1ptI4Qj6CutIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی درباره ایران:
فکر می‌کنم ما به تغییر رژیم بسیار نزدیک هستیم.
رژیم در ضعیف‌ترین وضعیت خود در ۴۷ سال گذشته قرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/19931" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19930">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=ML7G27R6CSTmDM361HdxBdQkDiViL75OtnmXZlg4-Deo7hDcmoD9aHjfmKPG8MYZM3UrD6-z2qEuMylBjFV85GuelBNNEVHuKz2xoC51_iBHE4rG0P2KLgxM2LQ0YjKl8gNdlyarmeISfAY_XTtQwtY8BOh7bDVUGwUaKzq-acDT6wRohF0BmA78OmbA2LnYGKtJk-Xi3fLaOy6iHM35mA96p3brd3mvSrQDlMh4HR6Eds1O_28zxCotqcMPLOwUd38E-Q1is6YYDwJu6NNrX36EXYXmEa4fpM-iRbfTU75MsowvkBX7vvXQM_nsvTUg-YiNfhseYSmH4bCNgN89oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2dacc78c5.mp4?token=ML7G27R6CSTmDM361HdxBdQkDiViL75OtnmXZlg4-Deo7hDcmoD9aHjfmKPG8MYZM3UrD6-z2qEuMylBjFV85GuelBNNEVHuKz2xoC51_iBHE4rG0P2KLgxM2LQ0YjKl8gNdlyarmeISfAY_XTtQwtY8BOh7bDVUGwUaKzq-acDT6wRohF0BmA78OmbA2LnYGKtJk-Xi3fLaOy6iHM35mA96p3brd3mvSrQDlMh4HR6Eds1O_28zxCotqcMPLOwUd38E-Q1is6YYDwJu6NNrX36EXYXmEa4fpM-iRbfTU75MsowvkBX7vvXQM_nsvTUg-YiNfhseYSmH4bCNgN89oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر واضح از حظور شاهزاده رضا پهلوی در مراسم
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19930" target="_blank">📅 00:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19929">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ooa1J4ei7Gm2mtrhej4VXtR_bzdnxGq6LkiEAZNCA2ne-YLEiodNpbueJoOSZ4aId9UHMH2Q1WJmE_hRraY3w_m4XLwaO_WGng82SqKoIgZm81bdpaC7HGMV2vFKsxjnBp1wJ1btq453WXi1wCSjiSk9Z5NxPsDwUqM4vn1WhwX1FWx64qJWnuJBN9id_HuATREFLNf30YHI7ZSrSMoXoXAcTZR6xB-4GgtEtM01fxtENFnLRqlswX10vY53nt8miHaMscuDre2tdJoSZKei9eTDS7I42cqpnhif2FKp1zDx5DBwbg1lA2kreWHkGmRJSAirptGESiDB1RmhLd8FDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز: در حالی که ترامپ مدام از مذاکره با ایران حرف میزنه، طی چند روز اخیر گسترده‌ترین تحرکات نظامی و لجستیکی آمریکا تو منطقه گزارش شده.
به گفته برخی منابع نظامی، آمریکا در حال آماده‌سازی خودش برای یک جنگ تمام‌عیاره!
@WarRoom
اتاق جنگ با یاشار: هم اکنون، در هنگامی که همه در مراسم سناتور فقید لیندسی گراهام هستند، یکی از سنگین‌ترین ترابری های نظامی آمریکا در منطقه انجام می‌شود.</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19929" target="_blank">📅 23:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19928">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تقدیم به نگاه زیباتون ، بشوره ببره
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19928" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19927">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/19927" target="_blank">📅 23:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19926">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19926" target="_blank">📅 23:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19925">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فاکس‌نیوز:محور اصلی گفت‌وگوهای آمریکا و اسرائیل، تصمیم‌گیری درباره گام‌های بعدی پس از حملات اخیر به ایران بوده.
همچنین نتانیاهو احتمالا اسناد و اطلاعات تازه‌ای ارائه کرده که نشون میده جمهوری اسلامی با وجود صحبت از دیپلماسی، همچنان برنامه هسته‌ای خودش رو پیش می‌بره.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19925" target="_blank">📅 23:34 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
