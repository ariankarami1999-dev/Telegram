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
<img src="https://cdn4.telesco.pe/file/PFF_fqcfT7S9ZitWt0ouashaK2auqZLOOfUf9RaFpWbiA4ZZelNs-Uy1IkR6oPsC-1DfU7dvaBhf0fuL6InidoOn-SA8Fj2hfCC1xfE4XzNkC2jrKW27Fk3klM42R5Uq3pBEdBXGxC4fu1axG9gW_whGOe7ZUmouKVo5pRAAHOSCo2rdfmNn6s-m3roMeQ0ulDkd43URpfhMpvEtEDe5t_ObLIfdFfRuOwjN2T3lyClNslRjMm1ske3caU1OgnAolMwJiiNTNFb_Q26Swe-a3er0oiUmW770rie2taGRseeUtyDfjxWZ37c3at7rROnUzaGvBTdNq1NOAPPw4lB3CQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 10:30:24</div>
<hr>

<div class="tg-post" id="msg-5049">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BB7nxT2BVsuKQrRsYOAEjZCdn0nTXXohY1afTJUFHov2tn9Esb0UXvG9H9cPBUrzn7WSzwhMnk_Nw9nZSHL5HIo1N9bKHE8uylxdZc1_uvZEQ9U00cmRv6wMP812twnMYMCrTdcjQEUe4IWHZIxwChmvX1ZQNfTQErvSc8iiauM1ZldpwU_7KSQB4v_I_DPP9A1cqSc-IZtpcTpOFC4jPiTQQ4UAfjBuSVCDz8Nu9mov61TfqZ6hqCF3RKw0S68fE2LP2Lj1Q0DGNGGkcUQNUDFtpa0dBQHJ6_AbHhBVplrbTOK3sUbxk-hP-C6CRqkLMtoxvfmMk3rRxegruGFMng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاثیر توییت ترامپ که میخواستم حمله کنم به خاطر کشورهای عربی حمله نکردم و…. بر بهای نفت در بازارهای جهانی.
کاهش حدود ۷ دلاری بهای نفت</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5049" target="_blank">📅 06:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5048">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=Hab7rxLjKBW_c-g6GVDqzjAY0oIK0zQyGUjJC-0OqiLxVScmJLXmoydUAgQ4pNIDnS4NW3_-puMwMJfgsE8dBhMRoTjUZm0garwHvWM1bD87l0JTnXnCxp7H8JhkmMpx6OA7Xu739TWT-g65eboRZFBlaMPkOWxwBNH3PZiukn6fke423yKSxKwyYXyrTWc24fn_u1DW4ilrW7Aym6tJRUSqInDFglcb-jAe6JRzsAStVowxz0gUwM69lP5JbuE6IqSx0TYvWAQ2u0xxKsM3ytr_im0cGE1NcVv-UiMVhE49ipIbkeqtJdpYTEcoI2R82PplkIyAqMvtop4pyscgUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b8eb45098.mp4?token=Hab7rxLjKBW_c-g6GVDqzjAY0oIK0zQyGUjJC-0OqiLxVScmJLXmoydUAgQ4pNIDnS4NW3_-puMwMJfgsE8dBhMRoTjUZm0garwHvWM1bD87l0JTnXnCxp7H8JhkmMpx6OA7Xu739TWT-g65eboRZFBlaMPkOWxwBNH3PZiukn6fke423yKSxKwyYXyrTWc24fn_u1DW4ilrW7Aym6tJRUSqInDFglcb-jAe6JRzsAStVowxz0gUwM69lP5JbuE6IqSx0TYvWAQ2u0xxKsM3ytr_im0cGE1NcVv-UiMVhE49ipIbkeqtJdpYTEcoI2R82PplkIyAqMvtop4pyscgUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعال شدن پدافند در اصفهان</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5048" target="_blank">📅 00:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5047">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5047" target="_blank">📅 00:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5046">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
رسانه‌های داخلی : فعال شدن پدافند در جزیره قشم و درگیری با «پهپادهای متخاصم.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5046" target="_blank">📅 23:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5045">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ :  از طرف امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس امارات متحده عربی، محمد بن زاید آل نهیان، درخواست شده که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی ایران را که قرار بود فردا انجام شود، به تعویق بیندازیم.
آن‌ها اعلام کردند که مذاکرات جدی در حال انجام است و به نظر آن‌ها، به عنوان رهبران بزرگ و متحدان ما، توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق مهم‌ترین بخشش این است که
ایران هرگز سلاح هسته‌ای نخواهد داشت!
با احترامی که برای این رهبران قائل هستم، به وزیر جنگ، پیت هگسث، رئیس ستاد مشترک ارتش، ژنرال دنیل کین، و نیروهای مسلح ایالات متحده دستور دادم که حمله برنامه‌ریزی‌شده فردا به ایران انجام نشود.
اما همزمان به آن‌ها دستور دادم که برای انجام یک حمله تمام‌عیار و گسترده به ایران، در هر لحظه‌ای که لازم باشد، کاملاً آماده باشند، در صورتی که توافقی قابل قبول حاصل نشود.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5045" target="_blank">📅 22:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5044">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مقامات پاکستانی هر ۱۰-۱۵ دقیقه یکبار میگن به دستیابی به توافق بین ایران و آمریکا خوش‌بین هستن.
موضوعی که نشون میده وضعیت برخلاف حرفهای مقامات پاکستانی اصلا خوب نیست.
🔺
یک : پاکستان در کنار بنگلادش یکی از متضررترین کشورها از بسته شدن تنگه هرمز بوده. اقتصادش دچار ضربه بسیار سنگینی شده و باز شدن این تنگه برای پاکستان و اقتصادش، به یک «ضرورت» تبدیل شده.
پاکستان فقط برای یک ژست در سطح جهانی در پی رسیدن ایران و آمریکا به توافق نیست!  بلکه برای نجات اقتصاد کشورش دست و پا می‌زنه.
🔺
دو : پاکستان قرارداد امنیتی دوجانبه با عربستان داره و در صورتی که جنگی بین ایران و عربستان رخ بده، وضعیت پاکستان بسیار دشوار خواهد شد چون بر اساس این قرارداد باید مشارکت پیدا کنه در دفاع از عربستان، همین امروز هم ۸ هزار سرباز و یک اسکادران جنگنده در عربستان مستقر کرد و البته سیستم‌های دفاع موشکی،
پیامی به عربستان که در کنارت هستیم و پیامی به ایران!
اما وقوع جنگ بین ایران و عربستان، برای پاکستان یک کابوسه! خصوصا اینکه جمهوری اسلامی در پاکستان نفوذ زیادی داره، اما ارتش، دولت و نهادهای امینتی همه با عربستان رابطه بسیار گرم دارند.
🔺
در روزهای اخیر خبرهایی منتشر شده بود که پاکستان مواضع ایران را به طور مثبت‌تری به آمریکا منتقل می‌کند و همین باعث سوتفاهم‌هایی شده بود.
بهرصورت اینکه پاکستان امروز دائم تاکید میکنه که همه چی خوبه، میشه حدس زد، وضعیت وخیمه.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5044" target="_blank">📅 20:39 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5042">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=XD5xZqUvgRkK1pE8xj_b0YoD6f71n2v9Y0W8Xymb2inyRHzFZ0iHEMlMoijcYNBw62NQK2AKMNHcmgSLjb9RVDZlKSyRjEFobHYDEt58euIRm8r5Nykc_ckC4TTX3GCpUaqaiEL2diCYdwFysSmY2BscNV1888fJc3cPYT_GvuOBRKMAbdh0MsJo0Rp7O5DVeW66U_DD7z6UqVp3k99hyBVDz9-52IrLTbgyH-GD1DDdT6G3evBVPqP_o-rxYfywVOrU-85FUZw1D3gRufQt_qwEDWcs7mMlYruIVgtxE6Xx6hv8CvVeGShS7fYUefI57x7wOxdTXzEy3PNa_AljzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a11f2baf.mp4?token=XD5xZqUvgRkK1pE8xj_b0YoD6f71n2v9Y0W8Xymb2inyRHzFZ0iHEMlMoijcYNBw62NQK2AKMNHcmgSLjb9RVDZlKSyRjEFobHYDEt58euIRm8r5Nykc_ckC4TTX3GCpUaqaiEL2diCYdwFysSmY2BscNV1888fJc3cPYT_GvuOBRKMAbdh0MsJo0Rp7O5DVeW66U_DD7z6UqVp3k99hyBVDz9-52IrLTbgyH-GD1DDdT6G3evBVPqP_o-rxYfywVOrU-85FUZw1D3gRufQt_qwEDWcs7mMlYruIVgtxE6Xx6hv8CvVeGShS7fYUefI57x7wOxdTXzEy3PNa_AljzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏رویترز: پاکستان [کشور میانجی‌گر میان ایران و آمریکا]  در چارچوب پیمان دفاعی، یک اسکادران جنگنده، ۸۰۰۰ نیرو و سامانه پدافند هوایی به عربستان سعودی اعزام کرده است!
سامانه پدافند هوایی برای مقابله با موشک‌های جمهوری اسلامی است لابد!
پیش از این
مصر هم یک اسکادران جنگنده و خلبان در امارات
مستقر کرده بود و به ایران هشدار داره بود.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5042" target="_blank">📅 16:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5041">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5041" target="_blank">📅 13:44 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5040">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‏
🚨
رویترز: پاکستان دیشب پیشنهاد اصلاح‌شده ایران برای پایان دادن به جنگ با آمریکا را ارسال کرده است.
🔺
دیروز مارکو روبیو وزیر خارجه آمریکا  گفته بود که «پروژه آزادی» (عملیات آزادی تنگه هرمز) به درخواست پاکستان متوقف شده بود زیرا که پاکستان گفته بود که توقف این عملیات می‌تواند به دستیابی به توافق با ایران کمک کند.
موضوعی که در نهایت رخ نداد و هیچ‌گونه توافقی حاصل نشد.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5040" target="_blank">📅 12:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5039">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ve1t-OI_HZm5G3EVaBeezMQ24iR5Nd0qw0vbsHCvfmWTZRHCrDaMImIspzhSk28ijOc4nNKXzdTmQ6OlEse1PSN74-YdIUpqwdMH-QLh-MvUFgZRb_i86H6tqawRfObE0puD_kEjG8ysIvNPEX2oKYEVRTQLGBkE0W0_z_B9xLXxE8RE1r8L0-5vpX5DcxOILeZkNZoBml8s7vmvFvTgk4TUw4X1xIIAQuVbjq5-KVi3u4B9YCpqsw6XL-ZY2NHrMXuOF6NRrw1l1xMaAxHT3OkRknyJxLxuDZYwuAiIVutOVdgPFyVPUyJXxDo3H_GHZLwp_Y-y9Kur5UsZ5n-ZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخبه و مغز متفکرشون، فواد ایزدی می‌گفت، سالی ۱۲۵ میلیارد دلار! ۴ سال، ۵۰۰ میلیارد دلار!  هی «غنائم احد » رو افزایش میدادن!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5039" target="_blank">📅 11:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5038">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mn4pUQAh_qhz1yRM13i_qVdoaTkJxBoUJw057gC7YUmLCfjv6_PHFKNIhIoXA7riFwDtlQoEPdrenuZxa6srSbgyBtHqaVeort49dNn-de-MNnbe_Ww_1jg-TaemTeiUw8nh7dXXk_sprOXHvlaVuPj8fs2SAfc-8_NeoHPbqdjkktgU0eMxCYjLFZor1qauRKScsHwrpApfQ695HNyeMrKD_lSNfksW7GaGth-bc-R8MRa1mLa-TnIM3sF4viraOTkMTMofhxcL4XGSMwTzu2SuSbbIVpq68dBNcXmRb-eXVcZP1RqXWeTZvocINaMrAOAFd7FgyTY08g4dqZD7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی ۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!  توی ایستگاه مترو هم از زبان رویترز  نوشتن که قراره ۱۰۰ میلیارد دلار درآمد داشته باشیم!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5038" target="_blank">📅 11:16 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5036">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YW9SuNGfEb0Nz04W31WoC4GM6gQP43LokDjHtEMD-zSJ3xAYeNs-G41tqt5XnfRzGWL9AwxTge2uuVUWf7AZ0hIczIYOgb362HdOtNetw3WRWkRh6CsAXrDYx-lEk4haBb_bz8t1OBa8Sz7-9mV20Y7O28kD78ErFtIgn_Kc437MJOCyD27TIfskHDca3PdMhjf-YP3c0Rf4tBLcDcpNPWhjiLAom4j42IsC9y-82LENWUSkc5oqDo0Rbaqnb7BnFmAh6maRDaSZAtujHJN6nDMmYPG9VtB3U3_CxNAAQjGqB6WKDMVAiTWvrfUCFdrIofrIloE-xkewqsKbXQm19w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NcVnPfCf8AoeTkqs-Cj0yyvXKUaSKlmvmGINZoxkj2T1vDjuIOI7gdkjShkJQp50hV4lM477HZiF22vKjy2qa6Vmy_zlKKeiuF4CA28tv5gWVz7gCNzmvydfVp1qOvl2OUnI0FBO0sXlfRHHNXHJ2k2wr3wxoyuOe-KFlrJDYgpDIlRuEPY4iGNo5fHKvnCv6YIV7z-ruf8YW0mIYsPSCYC3FUsjJXn7ckFQ4Qa58YFePdof5xVd8Hpr_l9F5anT10c1UBgl0CJoxwRNEVE-o-n9i2aXz-0jeD76aLI03AYpLnE2pSl1zOf-QS9VvuhhWJ3X96PV74fsQDifhHTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اول تبلیغ میکردن که قراره سالی
۱۰۰ تا ۱۲۰ میلیارد دلار درآمد از تنگه هرمز داشته باشیم! ۳ برابر درآمد نفتی!
توی ایستگاه مترو هم از زبان رویترز
نوشتن که قراره ۱۰۰ میلیارد دلار درآمد
داشته باشیم!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5036" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5035">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=ZKTS8IZmm0bMEGax88dF-3t8QBnOjqy0s6DbBaSrdUsmhSh6mZ_ua5BmhgF5SKWeDhlizrOlDc-cPPjTFXRdjoR52UUhO64SEQ2Ao-9912SspFTaT23RU_Y_RHwo3psaqKO0idKmzwhTkxxo7eR4dGGrCs0fIFcs9pfg_gA3W-hZCfP4L_o8DX_bL8DSx5FHSCOKnNDNWlQmbxUf8pYnqst-lYL7x_GQyMnJtKb9Q9pkLlZDeaV5amLLExz6es3fsnMFQDE2S_fhuwP2Ymb_e4MuZH5xM3UWXPaZ_5YO3D011RJhxGVMxBpXJIEvYiuj_CaT-v0iiI-Y8bhwf8OloA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818d63bca0.mp4?token=ZKTS8IZmm0bMEGax88dF-3t8QBnOjqy0s6DbBaSrdUsmhSh6mZ_ua5BmhgF5SKWeDhlizrOlDc-cPPjTFXRdjoR52UUhO64SEQ2Ao-9912SspFTaT23RU_Y_RHwo3psaqKO0idKmzwhTkxxo7eR4dGGrCs0fIFcs9pfg_gA3W-hZCfP4L_o8DX_bL8DSx5FHSCOKnNDNWlQmbxUf8pYnqst-lYL7x_GQyMnJtKb9Q9pkLlZDeaV5amLLExz6es3fsnMFQDE2S_fhuwP2Ymb_e4MuZH5xM3UWXPaZ_5YO3D011RJhxGVMxBpXJIEvYiuj_CaT-v0iiI-Y8bhwf8OloA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسلسل بردن تلویزیون و آموزش رگبار میدن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5035" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5034">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=VNbEWbtrAZbGWNDjT8f29cPSAanDxgRfP30qXcUDZrk6kK9rxcl0_IreypDGMCm7mlS2IMSqeFBEZ3eD8Zpi6RGrK_ff4ptO57PtGg7J5DJ6KzwjycUMqDjPAN28f38mqkMYcNqIGzKgdziN6rAPCIfc37MPpqjlMxkQeP-Kt5zYBlKdnc1evV7qpwOpMBGYcUnKUstA0En_sa4X-lr-M2wnwyI0Wl_1eiEo7CrMNuf87aUNbwYvyWPO5OYvBcJx4aRy_SFdW6UIpVoj8ol9LdoQCSPsxKj4SW8L8VBEe8whdJBgaDcfREUmAWlqIPKzfvLlfOG6dhhY4fMg1dlRLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4d9867bbb.mp4?token=VNbEWbtrAZbGWNDjT8f29cPSAanDxgRfP30qXcUDZrk6kK9rxcl0_IreypDGMCm7mlS2IMSqeFBEZ3eD8Zpi6RGrK_ff4ptO57PtGg7J5DJ6KzwjycUMqDjPAN28f38mqkMYcNqIGzKgdziN6rAPCIfc37MPpqjlMxkQeP-Kt5zYBlKdnc1evV7qpwOpMBGYcUnKUstA0En_sa4X-lr-M2wnwyI0Wl_1eiEo7CrMNuf87aUNbwYvyWPO5OYvBcJx4aRy_SFdW6UIpVoj8ol9LdoQCSPsxKj4SW8L8VBEe8whdJBgaDcfREUmAWlqIPKzfvLlfOG6dhhY4fMg1dlRLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما :
آماده‌ترین برای حمله به ایران اسرائیله.
اسرائیل نه خسته شده، نه پشیمانه
نه به آتش‌بس مقیده ، نه کم آورده</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5034" target="_blank">📅 07:22 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5033">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Khkf3M1O24e_PZd1zJ-VTI71FlKOR1VUi5YMF35K088OjmfKwMJN_MBO1JuqZ3eQe3R3cBXZMqxBLmv-RVaZLdu2x_5o17MXjfyAv6w26CQSGrQtNYeupJid0kVE-SVfeBOF6T-Jzgz9i3OSfv-vQKQoUg1Jg-BVbQPJ0GVgjfVKDYHgXSYXG3ybO8LGPRHFWWlhTMsPJNWHZvoX0fPiqB9koxHoqgjTfbc40Wog3p8yHU5bFGy-HF1V9FLueLIDLmGOFAlt94StZRC7GUF-PAhLRt2QnwztVfR8sQ7TCO06crk2jnfLA8Rmheo0Bs4QRbueTni7YsQSk8eJVER44g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5033" target="_blank">📅 01:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5032">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏سی‌ان‌ان به نقل از یک منبع آگاه : ترامپ روز شنبه با اعضای ارشد تیم امنیت ملی خود دیدار کرد تا درباره مسیر پیشِ روی جنگ با ایران گفتگو کند.
‏این جلسه یک روز قبل از آن برگزار شد که ترامپ گفت جمهوری اسلامی «بهتر است سریع حرکت کند، وگرنه چیزی از آنها باقی نخواهد ماند».
‏به گفته این منبع، معاون رئیس‌جمهور، جی‌دی ونس، وزیر خارجه، مارکو روبیو، رئیس سیا، جان رتکلیف، و استیو ویتکاف، فرستاده ویژه، همگی در این نشست در باشگاه گلف ترامپ در ویرجینیا حضور داشتند.
‏این جلسه تنها ساعاتی پس از بازگشت ترامپ از سفر به چین، کشوری با روابط نزدیک با ایران، برگزار شد.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5032" target="_blank">📅 00:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5031">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سخنگوی وزارت دفاع عربستان:
۳ فروند پهپاد که از حریم هوایی عراق به سمت عربستان می‌رفتند، رهگیری و نابود شدند.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5031" target="_blank">📅 23:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5030">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c29FgNEEwStb010_tbunBZCOBGONLKaJF-VvprqQyLZCqTuLqN1O9ohRB8RIJkT04ZY0ZVwX7GLum9Ts3y4iNCy_xU1oDKtR_k4Q4IgNpbgc5TmD7pF19Ah3BOm8MeQTYebJoQ8CpDZzyqXZNvbRGoFDJ4aBAatEKYFQ2WOutKtQ19unQHI7tuCs_pupWxEE57ca2PQJrBqeNlUqFwC0OEeHX675653s9ou4cV_3XgbukOhy1GZnURxSvDnM2x-ABTcrn43woHpgb9UlQOfjC8JaOVv7Yvpvyv0-XvrbInBKgbv6deTVjdFiQsek0uNzqQPV4GO_8ooYXhHJuC94Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5030" target="_blank">📅 23:23 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5029">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m366r1NED6MTjSbQlAMVSW1T2Pur-lGcRouTY_PNtMHMIIPzW2fElEPzuh83BQiMeSpo-Fhcoe-zbBiD0FlrNKUM_I-srehp9A-O0BJB5q0XT_9l9or1p9x2gOQ4ZE4bsMKSX5DorNw2D2skPVkZufjavp18In9Q8DNQR1ci_LQMotahUDQcs6bLxlaGe68J0l0Z9PFEwIXKwy5JjUuORbA5NgTnrJn78eGIhRmu--wsvG_K2ifLkFXdbJNUGFFmGwtqUwGxWvY99Ag54760ctP71KKoe99HtBvuynIhiekIhwcF-riFe0zdxGh0PzKJ9hWMabv8FIkENYgvtvoSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادبیات سخنگوی کمیسیون امنیت ملی مجلس.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5029" target="_blank">📅 23:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5028">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟  در پایان جنگ ۸ ساله  ۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و  شما «جام زهر» نوشیدید!  خود صدام حسین در سال ۱۹۹۰ به خاطر حمله…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5028" target="_blank">📅 23:08 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5027">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/re28VZaYmjtvu3ZYvEGMRZqZ8lQhRlzsWuyhI3gFKM_Vzoqd20R2xnRShVq6Rmiq_B6gOwP6uzzc_4nwOB7aG3M8gjBCBx0fos3MAzhXnR2LxmxBHKBv06V6wXiwP_QYaQF9AgVv0tz-t7MSwy-HLtOR3eDek483legYOc8gWdfwfZW1DZGdv_7aalQ3XhWUteIWMkWG5TGugyHtdQF8Lmv2JfMtCiEk9xmjRgaOxw5PdOE45Ay-3suGimUY9re83DVyc1GCS7TsV873lBJtDFNOMwIZzxuLRPD4YeBIAdsh2PAiWk1AEpwaj4rBaaKqUpeXk7orFXYRCORPLfBrfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۰ سانتیمتر؟؟ شوخی میکنی؟
در پایان جنگ ۸ ساله
۲۶۰۰ کیلومتر مربع از خاک ایران،  یعنی بخش‌هایی از: شلمچه، طلائیه، فکه، مهران، میمک، سومار، نفت‌شهر و خسروی و دشت‌ ذهاب، در دست ارتش عراق ماند و
شما «جام زهر» نوشیدید!
خود صدام حسین در سال ۱۹۹۰ به خاطر حمله به کویت این سرزمین‌ها رو آزاد کرد! خودش به اراده خودش! نه به زور شما! شماها که جام زهر رو نوشیده بودید و تموم شده بود! اصلا خمینی بازگشت این سرزمین‌ها رو ندید!
چون یکسال قبلش مرده بود!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5027" target="_blank">📅 23:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5026">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/344237687c.mp4?token=juUT5v2qbT6Hv-Yvh4GSrMEkrsK2nP1O3jw4uddSN-CHf8zOFIuD7X1s4cAWomRhbvTlY9JaHLbVtU1ixBrDDaNDFQurvaO8qpmKUhE9pCOf_Fs_fNMZQnpD6aXMwzqp_4xYN9x60kNKhwQIR4tjA1QBweC9qZPI0wYG4y6ySlphraxIYmO_gUpT0Fktd6eOJEaaYiqxhGHWvNC5gtn9FfdtYP4wE2OnGX_IpMrhR5AvG_7v9kZ4fCpHUBYe1GH0GwEAu1SsI70s0XsVYr3koW9aqx3QLazuGmm4zL5lAfqSO7P-MUYBvRN0ehFiJPHRM_hmqyCTwmMAm1y0iLKIGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/344237687c.mp4?token=juUT5v2qbT6Hv-Yvh4GSrMEkrsK2nP1O3jw4uddSN-CHf8zOFIuD7X1s4cAWomRhbvTlY9JaHLbVtU1ixBrDDaNDFQurvaO8qpmKUhE9pCOf_Fs_fNMZQnpD6aXMwzqp_4xYN9x60kNKhwQIR4tjA1QBweC9qZPI0wYG4y6ySlphraxIYmO_gUpT0Fktd6eOJEaaYiqxhGHWvNC5gtn9FfdtYP4wE2OnGX_IpMrhR5AvG_7v9kZ4fCpHUBYe1GH0GwEAu1SsI70s0XsVYr3koW9aqx3QLazuGmm4zL5lAfqSO7P-MUYBvRN0ehFiJPHRM_hmqyCTwmMAm1y0iLKIGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶۵۰۰ ایرانی رو به اتهام‌های ساختگی - که سنت همیشگی این نظامه - در سه ماه اخیر دستگیر کردن!
هر روز هم آشکار و در خفا اعدام میکنن.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5026" target="_blank">📅 22:55 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5025">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLBbRKRx-XlH1B7Ofg_eAVuQuPyV_GPCzMiVstaDlPGheg-J_3fQGJpMfKvFEj13Cxl-jojP35CqaS8dRqLRY-3Qnn1d66jMY62IZXRn0wF9kKCppVst6K1GDIa2l3QZfQDYnvkyFGae-QlC4sjODzEYMdR3SGnssTe4eZrFJ_0iviLA-BZ4tVNDsZnJo8WyHcEpNDzssqy3oUAi76jrLq5o7yQeNIr1r4Z2_qHByzsD5DtuqTspPQWI1OmkqqUnvfMyujY6BAuZY-kukmM6b_XBXmAZRUJ_0d3-o-RDpRDSWEmYdyfOBOo2DXDhQoMrJxA0E9hfc595RnKqheNs4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدصالح جوکار، رییس کمیسیون امور داخلی مجلس : «در این مدت پیشنهاداتی از سوی آمریکا مطرح شده اما جمهوری اسلامی همچنان بر همان بندهای اولیه تاکید دارد. شروط ده‌گانه خامنه‌ای خط قرمز هر مذاکره‌ای است.»
🔺
ده شرط جمهوری اسلامی که میگن خط قرمز هستن:</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5025" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5024">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ابراهیم رضایی سخنگوی کمیسیون امنیت ملی مجلس: آمریکا یا باید شرایط جمهوری اسلامی را بپذیرد و تسلیم دیپلمات‌های ما شود یا تسلیم موشک‌های ما</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5024" target="_blank">📅 22:37 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5023">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‏ترامپ به اکسیوس: من هنوز معتقدم که ایران خواهان توافق است و منتظر ارسال پیشنهاد به‌روز شده از سوی آنها هستم.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5023" target="_blank">📅 21:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5022">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
ترامپ روز سه‌شنبه جلسه‌ای در «اتاق وضعیت» با تیم ارشد امنیتی - نظامی خود برگزار کند تا گزینه‌های اقدام نظامی علیه جمهوری اسلامی را بررسی کند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5022" target="_blank">📅 20:53 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfuWyn1M5jFRTUSCwNsvyezcHuR0O9RHfQcPeelVdmo4KghY8n2ljTVKELQfG0u2LUuIKYQny8TD8v8hYcW3b-ej8LyWYyG2THy4SlZcAv3adBp2OnQDHa3XH3-xUs8qIT3ZEaG8O4PZx7yHC4gXLFiJeR2Cxe341ICjnQidptcbJsNfj0ZQK9ewz82tOtQ4JGtorMH-MPzIEJcChUubD9Occj946fv9NpWAARpmLsdS5dnibpRtNW77jfNBlxejEF26qlgLp0Shlq02chpmMXFantwBHLkaDm6YgL12j3dVKLJfEgtIYnaot52BK5Xc7JlHwnnqOuJvn_wGs0FYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ :«برای ایران، ساعت در حال تیک‌تاک است و آن‌ها بهتر است خیلی سریع بجنبند، وگرنه چیزی از آن‌ها باقی نخواهد ماند. زمان بسیار حیاتی است!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5021" target="_blank">📅 20:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=ECniRetc-JOuKk62Q0HRPUmRyF3IErmZjx3JWfr48ECGp0NxJZDWlNX8DP7ECMa4kmohm2ejbsT5xJOrsuR2ypXX7lRmh2kSL75bdpuwgz6eNXrfj_8SarNxGfc3QJ4X6A9ZMDqNsQJFTWsDVs-tZamNPdFznNT89ukoh7Kg8D14wXIjQ3kPRzutPQ7Q3KZTW5Iai0oGLhdZmo8DA7ND_0phIhXVydXXWSo0XX84GyH8oLWdxelBoqVTCgmHfa-Lq34DQ81qEWiPiMj5okn1GHsf2kxfvmigxYaO-KGdGzwW6HF87su9U6wlCQgTHbgi0A_fnEVucbx0S479FB6whg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c03a8265db.mp4?token=ECniRetc-JOuKk62Q0HRPUmRyF3IErmZjx3JWfr48ECGp0NxJZDWlNX8DP7ECMa4kmohm2ejbsT5xJOrsuR2ypXX7lRmh2kSL75bdpuwgz6eNXrfj_8SarNxGfc3QJ4X6A9ZMDqNsQJFTWsDVs-tZamNPdFznNT89ukoh7Kg8D14wXIjQ3kPRzutPQ7Q3KZTW5Iai0oGLhdZmo8DA7ND_0phIhXVydXXWSo0XX84GyH8oLWdxelBoqVTCgmHfa-Lq34DQ81qEWiPiMj5okn1GHsf2kxfvmigxYaO-KGdGzwW6HF87su9U6wlCQgTHbgi0A_fnEVucbx0S479FB6whg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطیب نماز جمعه دره سن‌گابریل - کالیفرنیا:
تغییرات بزرگی در آمریکا در حال رخ دادن است،
و اسلام و مسلمین نقش مهمی خواهد داشت
وقت دعوت به اسلام فرا رسیده.
مردم آمریکا «باید» به سمت ما بیایند!
باید بیایند!  باید، چرا؟  چون ما «راه حل »
را داریم! خدا راه حل‌ها را به ما داده!
قرآن و سنت داریم!  اینهاست  که
آمریکا را نجات خواهند داد.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5020" target="_blank">📅 20:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5019" target="_blank">📅 19:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scu-nzTkc0akLq-Wz8zx1cARd9agYVZs-1PnBwZLrLi7n-tMVbCWOaADrK14g9NLn1ozlErGcT7MfcO4mfHTw1nO8Hb84u0IHZoi0A1PXq40t-yDFDnVU9Zvth4aV_iCa617QA-wC4tCH5xV2OPPZQ5hda64YmRdhZS3eCn_tLaTXL00eolObsMyK4xGM8ev2Mc61TkFxJYp2MMFSY9JxrlFnORnaYmsOd3knFC136LuAXQmu-gCgh70zoTtMEyGh4CapNYh1R8-_bm-tuE771C7tlNKTHprXe89b8NaqcoeHUuH9DMmINxD2UFTIuVA4IWFrv9Iby2Gdcv17dsD8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله پهپادی به ژنراتور برق نیروگاه هسته‌ای امارات!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5018" target="_blank">📅 15:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5017">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !   ‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا ‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا ‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای ‏۴️.…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5017" target="_blank">📅 15:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5016">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
خبرگزاری فارس پاسخ آمریکا به شروط جمهوری اسلامی رو داده، ۵ شرطی که قاطعانه حکایت از انسداد مجدد کامل مسیر دیپلماسی داره !
‏۱. عدم پرداخت هرگونه غرامت از سوی آمریکا
‏۲️. تحویل ۴۰۰ کیلوگرم اورانیوم به آمریکا
‏۳️. فعال‌ماندن تنها یک تاسیسات هسته‌ای
‏۴️. عدم آزادسازی حتی ۲۵٪ از دارایی‌های بلوکه‌شده
‏۵️. توقف جنگ در همه جبهه‌ها [لبنان] فقط منوط به مذاکره است ‌‌دست یابی به توافق!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5016" target="_blank">📅 14:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5015">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b64429192.mp4?token=FO7IeKhr5XL0eQ3-6kj-h6Jb1jGruz2rsVxOmDVauD0zL6pZpLNsOfcZlV3cMr6Z4YxeZ4BLQzqsuK9t8R_7odP610mlb0bq9IK-HXck6GtGeDyehwqGDZupzAn7tKDbDLTP71mEz1h-ZMUXSHHs9Tff-LLMoOwziu_A0dWHpZ1Hctw6-fZ6nVMNWwegEBXsgzm_OQKPtXrI-uunnW1wbhbMpUZGcMWoTV1ILWRluYJSnauv4IeZLzdK3aDsULYLf_cbCRqbu2AKaYMR1CnhLguBMsd3YxajiX1K4MhXud2fMCa2e-gxC6C0Znnu2UQRI1pAZHaEwmZlEZ8rSw20ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b64429192.mp4?token=FO7IeKhr5XL0eQ3-6kj-h6Jb1jGruz2rsVxOmDVauD0zL6pZpLNsOfcZlV3cMr6Z4YxeZ4BLQzqsuK9t8R_7odP610mlb0bq9IK-HXck6GtGeDyehwqGDZupzAn7tKDbDLTP71mEz1h-ZMUXSHHs9Tff-LLMoOwziu_A0dWHpZ1Hctw6-fZ6nVMNWwegEBXsgzm_OQKPtXrI-uunnW1wbhbMpUZGcMWoTV1ILWRluYJSnauv4IeZLzdK3aDsULYLf_cbCRqbu2AKaYMR1CnhLguBMsd3YxajiX1K4MhXud2fMCa2e-gxC6C0Znnu2UQRI1pAZHaEwmZlEZ8rSw20ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشه عنبر خانم!
ولی روی این حرف‌هاتون بمونید
فردا که به خاطر ۴۰۰ کیلو اورانیوم
نیروگاه برق و پتروشیمی و پالایشگاه و… رو زد، نیایید بگیم ما مظلوم دو عالمیم و نیت اینها تجزیه خاک ایرانه و… !
اون وقت برو پوست پرتغال بخور و عنبر نسا دود کن .
تا می‌تونید از این ویدئوها پر کنید و یادآور بشید جنگی که بر ایران تحمیل کردید بر سر هوا و هوس‌های هسته‌ای تون بود و دشمنی‌تون با جهان!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5015" target="_blank">📅 10:20 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5014">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=GD3AWTJfrVV5Rh8yw09lSuQU4vGHNm6dXeo2yKk3IUTKqbbaQfWbfKwZuAel6hXEtI-IFL2puZI4kQtzofVaEgHVIaIsvUgXpsz0zfGVuOHP3Rc4RYiB2usgSXbVRsoilyY0XLN4wCkRW8r0oXTDigRBZ32nIK1Tb_9mL3CnAXQ72TmP5AUrAHcJMy6O19BOnaXz0wna0sm80Cit206Vd8LRLEIW4uCj7n0SxKPdF8xGQ5YnCXPqVRv1wCihT-0s-MxrIMBtRESZ3NWWx5847c1UguvoYByWRP2vMC_IPm4_48-JxNJGJKDn_pdjMYtAJcQQmx_oMGIEqhnF5mqCnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ad919fa2.mp4?token=GD3AWTJfrVV5Rh8yw09lSuQU4vGHNm6dXeo2yKk3IUTKqbbaQfWbfKwZuAel6hXEtI-IFL2puZI4kQtzofVaEgHVIaIsvUgXpsz0zfGVuOHP3Rc4RYiB2usgSXbVRsoilyY0XLN4wCkRW8r0oXTDigRBZ32nIK1Tb_9mL3CnAXQ72TmP5AUrAHcJMy6O19BOnaXz0wna0sm80Cit206Vd8LRLEIW4uCj7n0SxKPdF8xGQ5YnCXPqVRv1wCihT-0s-MxrIMBtRESZ3NWWx5847c1UguvoYByWRP2vMC_IPm4_48-JxNJGJKDn_pdjMYtAJcQQmx_oMGIEqhnF5mqCnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهزاد فراهانی، بازیگر (پدر گلشیفته فراهانی)
میگه ما … داشتیم و انقلاب کردیم ، شماها هم داشته باشید و انقلاب کنید!
چه افتخاری که جمهوری اسلامی رو برپا کردید!
چطور روتون میشه اینطور وقاحتتون رو نمایش بدید، در دفاع از رژیمی که فقط در سال گذشته میلادی، مسئول ۸۲٪ مجموع اعدام‌های جهان بود!
که ظرف دو شب ۴۰ هزار ایرانی رو قتل عام کرد!
ضحاک روزی ۲ جوان رو قربانی می‌کرد.
در یکسال میشه ۷۱۴ جوان!
در چهل سال میشه ۲۸.۵۶۰ جوان.
کاری که حاکمان شما در دو شب کردن فراتر از افسانه ضخاکه! این نوع از حکومت افتخار داره؟ تباه‌تر از این در تاریخ وجود داشته؟</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5014" target="_blank">📅 09:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=izxRrvLPeJnNUsRFv-CHwOtDLPQOL1xflccWdQbTV3XXQOk0OMdG4QbKE28sn0QbxZ2ov9oDJWWFSo7PJzln5LbPSnip4JFoDaLc8cAsPhjyi_827Zw8lNfHrKLAdXni3ZSSsU8xvUiIgDLYBFHuKtMIqghmzZa7cR_5y4S6KdOqWmCZCOCe6Am5gwb49n9HCyH9vbqtjeaiepOrUDC5B7CLhf22hTr4Kez8SynBHlMbWGmq77JOGGpB-YWFG_jRpvn37by4zfcYpGF97LdUpT8ryeNa-_Fqk_GR25Bqy1lkcr1a4XivWLfwEAFv24I8bzi_G7NBTxDy5FOu_jHP1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=izxRrvLPeJnNUsRFv-CHwOtDLPQOL1xflccWdQbTV3XXQOk0OMdG4QbKE28sn0QbxZ2ov9oDJWWFSo7PJzln5LbPSnip4JFoDaLc8cAsPhjyi_827Zw8lNfHrKLAdXni3ZSSsU8xvUiIgDLYBFHuKtMIqghmzZa7cR_5y4S6KdOqWmCZCOCe6Am5gwb49n9HCyH9vbqtjeaiepOrUDC5B7CLhf22hTr4Kez8SynBHlMbWGmq77JOGGpB-YWFG_jRpvn37by4zfcYpGF97LdUpT8ryeNa-_Fqk_GR25Bqy1lkcr1a4XivWLfwEAFv24I8bzi_G7NBTxDy5FOu_jHP1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=PL2bInOXR1bAK-webbG3DXk9QdI2uJ3SLYQVTJRQvpCSn2iSs-brIZBwHMOCg1J72XM7Q3sgFm3_Lhp4xqjO7-NLbuwkoPNNMNWJZE3H_zes_qSWtgBsD1DbdxDq8FzggFJqvBR1PMmLG_U9qFsEKFa_gzA0Tf61_u9-ZgKOwhnyN5uxY_fT1UX2kxvoDadYbVDBH8i3vSeBZvK5YkF3841e_0wWHzJWteuDzU57pJ9gJ_b9pF8EysUkOo3rkWArjq2bKQ2Y3iyIZt5mNFja9kE8I3bvMrQAqiyYKX0IIZFEMJEEUH71fs35nRGj6oWvVmXmWj4GdeqJl7un3AIqGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=PL2bInOXR1bAK-webbG3DXk9QdI2uJ3SLYQVTJRQvpCSn2iSs-brIZBwHMOCg1J72XM7Q3sgFm3_Lhp4xqjO7-NLbuwkoPNNMNWJZE3H_zes_qSWtgBsD1DbdxDq8FzggFJqvBR1PMmLG_U9qFsEKFa_gzA0Tf61_u9-ZgKOwhnyN5uxY_fT1UX2kxvoDadYbVDBH8i3vSeBZvK5YkF3841e_0wWHzJWteuDzU57pJ9gJ_b9pF8EysUkOo3rkWArjq2bKQ2Y3iyIZt5mNFja9kE8I3bvMrQAqiyYKX0IIZFEMJEEUH71fs35nRGj6oWvVmXmWj4GdeqJl7un3AIqGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=VWQG6izZIdnqi4sMsOkI0xlXR1O-ViUM-WkTSc5mhg8Ul6Sg7HiFCPDGa9s5Tpn0bOwjo1slXeGov_PhyTnk49UfPJR9c8kSy1x4hKK3UClt4SBp95vRXSteqvlQD6Xp7HP5pNrjSTHm3iYC0Spbt0oE5x8T4jYu59FSf07653aL7TbVqGI7F1sVue9y8wcvkamqFVrNxgaGwBHMr4n-TT54mablYVrPBdvC1rMABmWUHX4D5eU1pJC5EP7Y4ARpkmIj4fUFQ5aK6BKcLlTfHyFNMRHx-HfYtaDOis92x4sGq2K2ddN6li3N2nOzmE_iLEUOR4fRuXPNK5ziY2Medg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=VWQG6izZIdnqi4sMsOkI0xlXR1O-ViUM-WkTSc5mhg8Ul6Sg7HiFCPDGa9s5Tpn0bOwjo1slXeGov_PhyTnk49UfPJR9c8kSy1x4hKK3UClt4SBp95vRXSteqvlQD6Xp7HP5pNrjSTHm3iYC0Spbt0oE5x8T4jYu59FSf07653aL7TbVqGI7F1sVue9y8wcvkamqFVrNxgaGwBHMr4n-TT54mablYVrPBdvC1rMABmWUHX4D5eU1pJC5EP7Y4ARpkmIj4fUFQ5aK6BKcLlTfHyFNMRHx-HfYtaDOis92x4sGq2K2ddN6li3N2nOzmE_iLEUOR4fRuXPNK5ziY2Medg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FhFoFvSxJqEoT-1KE3auTog1Pt-ynxIVjUF9OSDtyN4W0ErHyu4Y12jqWMAUaSlonvwwyxZcwL0Rz8SCGruML3R-tE90JwujMaYgFfqzC4dC7TDBhqZ5ylrn8nBggJqqWvRuq9MDqfhFmNBLXYh_wQzARXzMmAiDrAulIMXXCuJYh6mAJubjVFinIUAVkoWpoDKU6Qaup-UE4TMpWNyhInZ7qKixMGfoP9bfrQqdDguWQonqjUkt9nafQNd_blEmYwkGjGQDDVricp8qVrianfCHsS1VU4rL7fBNrAFuV-ZRUdhAG02PalVw-XAztPN_7auE3NrBaRpsz3hGPvN7JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX5NxXw9PgL-Ae9Rm-52XlTUNQGDgXg2TtuaMnJXUBBLvjjqURl6FFY0xMfKvT0hrOhdqoFzgtzWPWxaej7mkKiEcXcqDA6B1D8OkZYcpnef6hVriMzVxQ9yFt6LiQJOtWuAi3wvWxGAN22ySd5Bv_U0LQx_5_7UfcUxfVqg8y5IAzcB0bxsaH908Op9PgMz8KZW7Zasq1PQRMA0inTdgdx6zfDH1ApuSF1krbKaJa8gsmU_AkKY4XVHWcG64--I7irBhZkHrdl_1pCgMmkwmNLxN4BfzjHXwl-7OocoXNdzjGvkZmAgfFeWRBfPPRw96vXmMf1nH5zfMU5pV1y3rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nfz1-7V0FhzF04VUd9Fj34wsP5uqT_rGu2E8EJ2eqa_8CB1alyPXamxmHl5AbbweErSovZ4tmVsNseMvGZ601S7rL0AV3IkCESMzatScOAn3u4Y8UiiZyxHuq-v-DusWT62z16wkU3DsGFg2tnQRzirWWgw-_nyn8Nw9trjBUyeZ86t98BM-EA9fMJmDwa3gfyDw_RD3f9iKpRNl3eMwuk1sghblrsGAXu5I4fYuaOhQb1Vhw7op8F86sLjrxBBQq6K8opkzR7NftspL7pt_rT_re1QH0AxxY5hL27vIWhPSL7Czl65uOYTnxTwd-T-CKZyR08ggN7vdI4GpTRuhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjU09ZcCPMEgPGAi0AQOa_fkT-Zp4KmWgElnMcRGe7oebXDBSwPjM_nZyfbJGPNufhHqdxVSB5V0YdoS2TMpg88wcKmeLhMnBYqo4lXm6w9hp82M920wmyHSaD-oukw-3_D1uto2URBpo_g-DgtBbxyFyWnQl89p_T6YepTrJJ_9SX5pw9Qd1Mh6ymNhbkG_0RP4yAT-qHzmzgZ-_YxoXkBrpr9wBLqpne3zPSMYFdzj-vdC2xcex7P2YEFHQ7ZmSA3BVTiUctRa36odMf46ZcFWD51riYnAsibt65e3gbZ4eGVaLl0G3a7Gv-3GKzWOTxn5DZKk-y1RhgL9VJUJtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=DjvoI8unaCle39K5pq__9CGSkqt5GK0oh-2qEhzq8bsPv1BjF0R69PK9suRAj1IhaCwZjkLtBqyvFIv2Hz1pWKiUkqJLh_ncnW_jSBUNHj4W-VTo6_tlrD9rZiCnPzPGWalifR_Yd7JhTbeS28hXyNdKfd447i3pKxIg0YCsQHNuJXn-5txsdeqVGA0v0TqDjHvQ3Yn_pULexuYOwwT10gYOmhoy3CuymfCtk13zJyKCNFT1p7sFNj-KoxyJjBBTJ4zB2eS8ZVSi7xLM1b3GpdfkfrrZGYw3OICM_3kDaLjyld3rCMbbuAzstRAwdN3kixPr-800zAd9KCn-pPIGJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=DjvoI8unaCle39K5pq__9CGSkqt5GK0oh-2qEhzq8bsPv1BjF0R69PK9suRAj1IhaCwZjkLtBqyvFIv2Hz1pWKiUkqJLh_ncnW_jSBUNHj4W-VTo6_tlrD9rZiCnPzPGWalifR_Yd7JhTbeS28hXyNdKfd447i3pKxIg0YCsQHNuJXn-5txsdeqVGA0v0TqDjHvQ3Yn_pULexuYOwwT10gYOmhoy3CuymfCtk13zJyKCNFT1p7sFNj-KoxyJjBBTJ4zB2eS8ZVSi7xLM1b3GpdfkfrrZGYw3OICM_3kDaLjyld3rCMbbuAzstRAwdN3kixPr-800zAd9KCn-pPIGJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aNAMfuIG8Tti40xlLwIxOgpGJfzQd5CLsWkY9eLQqHiN0c6rfljzArF51wlbnQz5vvzs4B7qwmKNCElep35xrQIb1wiLAGRNhj1hOKFhgm0hqJauRM_EV3Ks3BOjK4YMDQ__MGdrSyAwcysEo5y61u4nqU6z2ZVBeN8xCxg6a1k5fjLAthDOI2qL0bElrcVOSlgIIDtfrMeMf5kHRYGQT521hr4ymL3h4y8JabU8AyioS6Kd8BEfvrXM5k4wvIg-Bh88sfCOUuPkROp00ZnUvWz3EZxMDhrh8JcCSnZP6A-Gc0dq3sdjLKPlk0mJVeeMWJo6Vy0qNKe8cLtW8N8W4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aNAMfuIG8Tti40xlLwIxOgpGJfzQd5CLsWkY9eLQqHiN0c6rfljzArF51wlbnQz5vvzs4B7qwmKNCElep35xrQIb1wiLAGRNhj1hOKFhgm0hqJauRM_EV3Ks3BOjK4YMDQ__MGdrSyAwcysEo5y61u4nqU6z2ZVBeN8xCxg6a1k5fjLAthDOI2qL0bElrcVOSlgIIDtfrMeMf5kHRYGQT521hr4ymL3h4y8JabU8AyioS6Kd8BEfvrXM5k4wvIg-Bh88sfCOUuPkROp00ZnUvWz3EZxMDhrh8JcCSnZP6A-Gc0dq3sdjLKPlk0mJVeeMWJo6Vy0qNKe8cLtW8N8W4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=GvYMR8yaROsQk0Hob9XMvMOo6C-gJ8iO-t2uFgBBs2AncK_toKAsHQM4rIICWBuT2ZpNjvBh2bGOy_cYHMjj-Xu_TNiZg4xV4R1ZwdbqyCEsBj7CJS9OmMLNUU8zxVo-90lx52gzn8_nY0BgeCu5seDQBWD2Unu2IUyXnvormeMMVnBCgkS2Vv3QQufp5RaTQ4GwQkC3q1JLOJ_pewkuU67sL6rY_yjG_O69IuKYQjb6bT0KYufyzyP2JS4u4fHiARKWnRlb6v8lMBpF7XeYIdad2hFMOcdi4nFo4A-LwwDT_Cc0s5A_lZC-8yBwC5Lg3oJFRMF2Mp5NWeYrAVgznA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=GvYMR8yaROsQk0Hob9XMvMOo6C-gJ8iO-t2uFgBBs2AncK_toKAsHQM4rIICWBuT2ZpNjvBh2bGOy_cYHMjj-Xu_TNiZg4xV4R1ZwdbqyCEsBj7CJS9OmMLNUU8zxVo-90lx52gzn8_nY0BgeCu5seDQBWD2Unu2IUyXnvormeMMVnBCgkS2Vv3QQufp5RaTQ4GwQkC3q1JLOJ_pewkuU67sL6rY_yjG_O69IuKYQjb6bT0KYufyzyP2JS4u4fHiARKWnRlb6v8lMBpF7XeYIdad2hFMOcdi4nFo4A-LwwDT_Cc0s5A_lZC-8yBwC5Lg3oJFRMF2Mp5NWeYrAVgznA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdOETJCgDI-zTWjLkTVPAZBzmaVVQ9wW9k9fg1-z257tpL2UiHYvSAy4tuM9Z2OiHr-hZHlxEWFxn8CpyR8c3vE78GmrV6U9jsjHTp_p5IcsIrhfSgv5DGabhwxj5aE3y2P6hslukdnFG88VepBOn3Dck45QZivEMQHTzbga7sCy3VADd5SssLs3Mw1eby-ePl9aCdmyoyVaWoQxqpbzyCRflbmloddQmvtm-iQbiTbBwyR2Y7mzbD0OflcYHAxjC2WTKaGfmp5OxJQm8FHyU_B22oeYRainGRpgwTwrlK-RC9XEdWVbNYn2CS6TH9Ib0Pv7HGJRAJ1XN2-B8hMi3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=QAQXO3I0PNb3-hdl_fQ0kC5g7zphC0Udn2h-23Nx7-tOJQnOBuV8d2qJHq2PAEtpdFqWb6-rM9-20CKOHGA3GhFMjf6kYvR65ha1_2iWe6iqNzVI3iiKrbX3lVdhRU78Gl2e4hPVdC0piIASRf0uTeIkO6JHzXO3kO6fzfx40-GG3CXAy4nLKPD7kms0njq_2ZsQtSGAGHbGPnbxDV_LEOko2t75ihyyARSqhhmfsZ72p6lztTaOfvlfIzwH4MVoEr8v1Q4iwXXEOwYOPPoHecAGoWLo71SFzJd1tRFOd9PRyWOdUvY1-sHMivsXtxQ7lakl7Uh0-i6xujwBoDiwyqGqpWZHrJ0xsiS4SvCEQvewuNFsGajl3B0mrPFPXYTQW1R88xtjAA_79kJPTMvN4lj9D7QUltkJ8uJMUhFYGzkgX3EeiGKe9rDAAkuJwPtmS6T5Hk5fvJLKh1Ke2-5GIih4KORVXD_lQ92mm9EDexhCHdKjnm6T7TbtOVnzR640x6gVufgeSKzD0c4YPZVxloHk5q6bxs5sh0blUN3InGxMlNgtxpKDUDByDJF5rEdWX6HJ5wmUbHgVjueNrOjaA49bmgHJpsY_2rBPLqO5T9c9Jr8PDNcTExm29ESlk26nnwIn0eL3rWxESQcivyBMz4dagm9Bm3QNY3Lr4Odc9kI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=QAQXO3I0PNb3-hdl_fQ0kC5g7zphC0Udn2h-23Nx7-tOJQnOBuV8d2qJHq2PAEtpdFqWb6-rM9-20CKOHGA3GhFMjf6kYvR65ha1_2iWe6iqNzVI3iiKrbX3lVdhRU78Gl2e4hPVdC0piIASRf0uTeIkO6JHzXO3kO6fzfx40-GG3CXAy4nLKPD7kms0njq_2ZsQtSGAGHbGPnbxDV_LEOko2t75ihyyARSqhhmfsZ72p6lztTaOfvlfIzwH4MVoEr8v1Q4iwXXEOwYOPPoHecAGoWLo71SFzJd1tRFOd9PRyWOdUvY1-sHMivsXtxQ7lakl7Uh0-i6xujwBoDiwyqGqpWZHrJ0xsiS4SvCEQvewuNFsGajl3B0mrPFPXYTQW1R88xtjAA_79kJPTMvN4lj9D7QUltkJ8uJMUhFYGzkgX3EeiGKe9rDAAkuJwPtmS6T5Hk5fvJLKh1Ke2-5GIih4KORVXD_lQ92mm9EDexhCHdKjnm6T7TbtOVnzR640x6gVufgeSKzD0c4YPZVxloHk5q6bxs5sh0blUN3InGxMlNgtxpKDUDByDJF5rEdWX6HJ5wmUbHgVjueNrOjaA49bmgHJpsY_2rBPLqO5T9c9Jr8PDNcTExm29ESlk26nnwIn0eL3rWxESQcivyBMz4dagm9Bm3QNY3Lr4Odc9kI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS55l_3LqPaazcrbHXvIGVtFTp6jx57Jlym-KCGSRoFKOAbQzjN_dtrd9fm3EKKhAOci8zznTwvL4p5wPINoq4uslcDBE213P_d7VbwwLlkIHx8-a_HT6DnFfgMy3kP6iePQn1SgDE7LQKlOgs68E3YOA6kcbYNzFZiB3FmuG9HqL01dFNFwgeWaQwBShLix4eNEj4YIazKsky30r-jGWNk0LYNNegEXdIFaeRnHSYzOAwjiW9YQoTrYWQzVLYbYkGEguA7bSwBIAGcf00T3Ub-qH9tq1sdEVSDxHuVX4QIOZZFfl1VjJGB691Z2WSHhvFBpuIvdxBtHBW3GzMGOlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=HHGanatGxSmOll84DgOzEGsYukbhe3OcdS7q_4hSZ6KZvSxpMAEWjkU4zDOBl96xM4fSaQd70YHg-SmMAjy8r_Yl3_sns5cg5mMhorCTEjEKAyvx_zfTOaPL6rvzmKh6i52SN4Bb0z71i0AvvIbtVHRllCSAnIduOVQc92AqY5DNTGWVBeeB1W2LDTs5vzK-l7sT8WrDpWzz0ttRwcocslu54skAzVNVR1iroNwOhJMEubtNiGq-ToTRi0KGi9zu1jnlcLlfcJyzN6JZRO1kC8NJd9cERBzUb9OWjUYZd2_InABo6FvhVYOie1xpAPSogFt0OGF4GALsxz_z0KL3lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=HHGanatGxSmOll84DgOzEGsYukbhe3OcdS7q_4hSZ6KZvSxpMAEWjkU4zDOBl96xM4fSaQd70YHg-SmMAjy8r_Yl3_sns5cg5mMhorCTEjEKAyvx_zfTOaPL6rvzmKh6i52SN4Bb0z71i0AvvIbtVHRllCSAnIduOVQc92AqY5DNTGWVBeeB1W2LDTs5vzK-l7sT8WrDpWzz0ttRwcocslu54skAzVNVR1iroNwOhJMEubtNiGq-ToTRi0KGi9zu1jnlcLlfcJyzN6JZRO1kC8NJd9cERBzUb9OWjUYZd2_InABo6FvhVYOie1xpAPSogFt0OGF4GALsxz_z0KL3lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fr8O6SO1I1R2LuUgPYxlssrRt_HwqpLBUgUg1iDB2ft_2PYd-vA5KGIemDY7IRR5VSDD8ptpRDwNZY3JOIyGiDDv6gmxkUbTl2T9miprdaBfTqgYU5IuHf4VtvG0Sf47WTYIYg_Wqwun4cvU8teD02URr0ViaT7kUBXIVbHm6kpVy9Ap5vw1eLYtmP3ny21FoG_xUp-ksJm30CdOyajJtR0fItvyzNJIJounPoaHwEVEW73PX6Qfyj9RLezyrTY6TvyHKsryQveu420AtrS232zI4BtDhUT5FQtIrB0oXs_IHja7tbhykzTGkx4vJGPosHycGOW99Xbv1jR4_Tm7ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzkcsPJVjbARdzYbJ10GrTWqqjGXfRTIHzEDHVkQBRIYw468P_YEufEVYf-_I2zzPxoZ-W5iPmIPgGZn1VJG8Ib--drNYynaywldeVDndPSy7TRMbjji65DqZJU_hHnqhxHid9zbj15l2kN3JAfkKoGsGCemm0s2WlWChVWBIdU99ZRP6v-c1sptfGmqizzG7G_eUKvVSNXkTqd9qDhfOB3YbWbOwI9s-Iu04MEom2wUOiaTgA1P4xh-06vY8AhbC4GIafS8ulwGH63Ze_HVKHfQAKXefBimrzAWetnZO2mfwuHIm6CdtJxIXuHI_aPVx2ZEDXcV2rqjpLoooCploQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_YUg5OBzAeK0wK5VZMyU1silFGY49lQol7-hmIgda-VaG9sXm17uAnNMrMz6BSQiyOa7o2CrgmJbQp3_9SjzQ6bLDuPvVEbbqYdES-gsYlqX5bxLA83nRFehh27mPwFsQADe86XWmm-7tRLnkvsVOHipldrGGW69Unc2dhI0c8RUTeypzOYHqI3YqptKNtNIukq4KZi7qUB4d_7oPxCZeoS-BnzmyjXa-VnY5q0fZaF4SccbGBYAZnK4jxpuS6c6heaPGPp68B_JCOtLpqAgMDRI7r2nY-Syjr5Ecd730i6RmkVLqk-dOK6EHnnkStXJz6escv3sW2lYRP9-mxUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEvcSb8dDLyJWP58u9gHHulWWrpZP8A6QXe6obCgQcOgrHOyp5mFXc8WcOmM-AqWhzSIY3YXYhNuyT6Dl6kaD_RfBKPep9TlsDcGsBZriiWIJkKT5MM5hrRtaaN_0-X_wR7LnCr7agej_HdVpBdgenuHK3N0zyrO14AoP0iGbPU5tHXzOygS4ODoqxq6baHkcV8eCu7RHHYzuJlbxuCF_OLdLlEKiZR3EsvLvMiR8f6XL5yLZfeHmyHFYu97Osox3MTxZ_NjcmNNLFu9y_Vln51_F2ZFipGPQhDlc5d-gEDS6Jup_wLOY5zumNLpA9P8Fc1RqLX_EHBj1e3jIb0rOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkJzVP2PbWKTJfz9N1Doen53ZY1tvhz6h3GUjhaR3ypFbRx4qOnbXWSfBwppbYwwTubZ1LPXmVGeiq-QvVy1W_IY7UO6REkxEsOPi-E0V7t8mTob0lI7iIKy6yAWDO6UxzUi_VSvoh9BRh7CKOEggC1pK0rpkzMHiB4XyA_tnNlvkLyS42BodY2bjIFKN-DYOrOzkSEGQsn_hsm7J_v3uYp-7Bx7Q2KUD2qNE8hyQj2X2kZATo8KS8x8oTY-FRhuI_Eb9VUNb1aL7yoC2BVly7KQuL_8qfKfl_UagwZ2F7TF6D6oAg20ryF1CFDoirZn3FugtWbTiE2VqNUxOB3EIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4NXmAtEmmDugh6Pf23_ttgXEVW0rpRST36_XfYycX_JAIt-HCUyMF-uPCT-QPIBUsYa-NGYnrUKzaIKqsAm-YzkFDWPwW-JSeEuHY4LgF5ZJV7N9Gb3-fH8NmV6jeg0sUuGHNm9vkenW21koYVxHyD6dA3QCQshqWXnq2ZsB6FW9syVCtWOgIJNZigAlX58x-W-ZGNck7M7e3qoc3xnrpiRiuFotFvZO2OfQt9RLkJhGRwgN8dhPbcNr46m1vVg4NuZ42URQq5okoGsWvZafQVIOstr8SvToNZANLxat3MSRl6chGbnbZPRDy3VYvbinqVS0K1LbIRLHVwyWU1AMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQaWdGT57Bzi0rHzKflYQku6r04NFAUhrVug7y2q9yiXeBAyAiFs7J2JUZmWGgi_LrqfjrEDK0DJwNZvvl9OVe0ebHc00rGVivrduiIgH4Hmh-5ixRp8_l7ozOwzSkBA1EnI5LzMwLCg4r-rWv1BhT2m0gj0ngQJj84oO2_rl7-RRDK8_mQ-zQiVhO_JCIyuOfr_-f2KYdNSi5qNJwbiuzH7Vb9FGIYkfVWRqJeJh_HfjggAePM-DijJTrWuZ5S9iwO-C_CysOELUKAO-T5faEal9S0kB72ZSPLerocayc452CWvJl3_p2FnBx-TJ1zKNozNRCkXg3mVapYvdcU2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=q2m1wGd-qzxZ9OJe6WqI7SpbKBPnGD4t3pdzXemuNLcPkVvDLF6z5pqOZCuj4xffFeRbctKWdjBPyMN-KT72aWzE0TbFqxiLzWDJoGiQrSCk82CorvAwMPF_eGgr9Vvg3ioh6Riv-MbSsHOyXt9wkNFoV8mLWEZbIWuFXK9N2ZXjYlSPvlEG19VJ1ABueyz45en7RposjwuOUAvPdW8HWDUF9J_ojZIlkxdYYvIPBbvaQL00Y7u6qNw5uVhD-cVeubMS972xsE8MpLKl7xuC0E4Su9Fw3b4zGBBd4jK4J_5GbzreFmnHhfZ3gKDGCzsDBn-RPhXQ5ppskW-q3XpJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=q2m1wGd-qzxZ9OJe6WqI7SpbKBPnGD4t3pdzXemuNLcPkVvDLF6z5pqOZCuj4xffFeRbctKWdjBPyMN-KT72aWzE0TbFqxiLzWDJoGiQrSCk82CorvAwMPF_eGgr9Vvg3ioh6Riv-MbSsHOyXt9wkNFoV8mLWEZbIWuFXK9N2ZXjYlSPvlEG19VJ1ABueyz45en7RposjwuOUAvPdW8HWDUF9J_ojZIlkxdYYvIPBbvaQL00Y7u6qNw5uVhD-cVeubMS972xsE8MpLKl7xuC0E4Su9Fw3b4zGBBd4jK4J_5GbzreFmnHhfZ3gKDGCzsDBn-RPhXQ5ppskW-q3XpJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWUuFb1SiGsd6QhdvoWcLSZ-KQL-LHTKYMeHL6zpxeE3mhBGw2U2VSC1784pHBba93Ap2IzcbxbEha2fJ6ddlV9O1zzLtStHgpJi5knAf7FFSlbVb99VbnU16zWslh2AoDacfQEcLrqlUyVfI3qTB68y2T2PwvKtfEDGOkxKba9HheWCcEY2Izb7kHGTpTmC03oCWSbOETtoNuDG6RGGNKRieIKPE92KNF-bCFjF4aWcI9lahlOqtuKozKb2AVLp4HmkqD2c07KedBlz4wszCQK_eb5rCNswKPDp9Qc_nGUypoqCv59VYz3-EiRri33NNf9mVETbu8ilpY2tAM6A2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5UJUZD9Bd6lJdLIXsmAdmywcKfsYLJWtKpx_ZuxDXxG38rgy6aYOMYa2VOj4FcCNcuCxEqfFl3CL3YhF8EytTunIojw5i2-lwHNSxg6iEzCxjU4q5ARuhCYgUp_PnpMrjJYJaI2qhOg5Jq28OUfRHaP9Sb5yAfibadtIvMX1x7QgM2X8GJ_3ah37Qil--40IVlPSrFM-WMXo9kQOhl9AD1H2srxPCCXav8nqnqzgWyxMjqHzvcYfxTTXyo8FJTcbCJQUgPI7WL2pminKAhysX4s-5s1VhTPaf-1jXeNmCnDRO_35JSnI5Z3OQdBW4C8HSnfd1c7AgUiS4hSvx4sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=cx6-MotcllCrlDH8472sW5q9jGqKjFJL1efqqcVNhlPGRzS570--_HpHF-czqtcZAN2wC7pnZyTrBGFbItFvPPSMjSyPWhzH1h6WqCH_DLluY_u3MUE5IcBCHk1thTkduW3MzIIumWaX_oSEmuHvm1q2KoBT4oulreAa5yjSHMX1ySu3n8-iZX60QDyQCaX5a53oHbTZ-6UtYoTLSH0sGBOh5pNW2qdEdb0-nQB1iHIEzZiibXm100tfOHoqt_YhBAT6AsER2Wr_4QI0XoNqa1kbzgHkRJIN2XXRRi6Y1ylTtZqwxwTlSgOU6Qs8uOzOI-K7ht4D6Z-wFikWogl8yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=cx6-MotcllCrlDH8472sW5q9jGqKjFJL1efqqcVNhlPGRzS570--_HpHF-czqtcZAN2wC7pnZyTrBGFbItFvPPSMjSyPWhzH1h6WqCH_DLluY_u3MUE5IcBCHk1thTkduW3MzIIumWaX_oSEmuHvm1q2KoBT4oulreAa5yjSHMX1ySu3n8-iZX60QDyQCaX5a53oHbTZ-6UtYoTLSH0sGBOh5pNW2qdEdb0-nQB1iHIEzZiibXm100tfOHoqt_YhBAT6AsER2Wr_4QI0XoNqa1kbzgHkRJIN2XXRRi6Y1ylTtZqwxwTlSgOU6Qs8uOzOI-K7ht4D6Z-wFikWogl8yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=pkWK8gVpyRioif6Lj6yCBw8C_fPf1zVHrl8mi0_m6MeWMHZMG1p--TN4eVQFvjqysrUa_S_WbkFT30DFS-lML60MGAxpBW552oSuWeTnCLTJfU12wzLQaTxQXgKmRbiBYgazlwvB3e2CSgLfUMt_xAhvfdtcRamvykqqQPtZv7GEqyI0Z4-86-Hz9NOvpUT63HT7ZTOuTY5n_h4yjGKLkxLV3R_JNUOENu_LMZ4sARvfsF1n-vz9qWTvkndc5OYz_iCTVtqNqzjoDqEnaVtEBNOot-kHAUIQxmhtynZkXq6NANSl-6xMLsIA5XaAe9SEwKshXHrL3a25DD4pHAZXeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=pkWK8gVpyRioif6Lj6yCBw8C_fPf1zVHrl8mi0_m6MeWMHZMG1p--TN4eVQFvjqysrUa_S_WbkFT30DFS-lML60MGAxpBW552oSuWeTnCLTJfU12wzLQaTxQXgKmRbiBYgazlwvB3e2CSgLfUMt_xAhvfdtcRamvykqqQPtZv7GEqyI0Z4-86-Hz9NOvpUT63HT7ZTOuTY5n_h4yjGKLkxLV3R_JNUOENu_LMZ4sARvfsF1n-vz9qWTvkndc5OYz_iCTVtqNqzjoDqEnaVtEBNOot-kHAUIQxmhtynZkXq6NANSl-6xMLsIA5XaAe9SEwKshXHrL3a25DD4pHAZXeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulzDRiR7y2oOc2IzG0UdrMCm8LoPvXXArKWvWjbubSCZYdm6stFbQrKyJrr6gIedfH9pWN6PLJEHdRKcouBe-TsUi7ODy0CjGV-rihDVcgeg4BYvjXXkIDyVUA8p9BXf4mF4Al1GU60mgcxP5kYCpRWpXgfOBEtzcH5HIP2GImBDUBXSwMwxTwfkge0oMbGgXo_Fe_AA34a9_SYebPFMUtQqVDQLQiFeW67xRJHqV_FGcg5jqDOOb8zU8osbXG4UM4YlgeH5xTc6C-XcYnjeyu-lx_68hPHeNXZbTu4qXuwOD0QAk-RoE_s8TAAwudJMtreCpBOUd8DrTBOjCljGhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=GowNdF9voDwonKSdSh6UgogXsJ2PsksggAzzVIjPaNTw1wh6GArMFxB1dJa3FvnKZKzPXtalbwuclaXO2_Z-G9sz-Jy0L3P-4NU2-cK3Rios_5c1Aaa604AxuHOSZevkIEEWawERcWHQXUoNsy2iPN1SLXJobfoQseHZLhEn6TaGhPZBJHROCO5LpyQwItBuy9MBdQ-Ig_C9DElDEpMMzoC_tlzc1ah6-etSgH-Qs0ykBrfjDvVsRjlAMH-jJ_geW5yQTbm3_5bIuoh5RGFg8pcOcaGFrwgVLyde2YziP5B4xdkMnNEGNMDxXWsGuSI-XD1SvvKzAYdNotSk7uH-Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=GowNdF9voDwonKSdSh6UgogXsJ2PsksggAzzVIjPaNTw1wh6GArMFxB1dJa3FvnKZKzPXtalbwuclaXO2_Z-G9sz-Jy0L3P-4NU2-cK3Rios_5c1Aaa604AxuHOSZevkIEEWawERcWHQXUoNsy2iPN1SLXJobfoQseHZLhEn6TaGhPZBJHROCO5LpyQwItBuy9MBdQ-Ig_C9DElDEpMMzoC_tlzc1ah6-etSgH-Qs0ykBrfjDvVsRjlAMH-jJ_geW5yQTbm3_5bIuoh5RGFg8pcOcaGFrwgVLyde2YziP5B4xdkMnNEGNMDxXWsGuSI-XD1SvvKzAYdNotSk7uH-Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=kM7GWvdfE3oUmA8NAdIaYJENAavOKEUs_8WUSPrcrk9cQojvtkAoxZsD3wv196h2dK1B8fV4d9dxPLdoSMMLDRahOn7Zn0QqQUbkZzpRq_-vdbDi3YE5cwNAK0WTNq2OvIqfNtj0cKhp5DoHavDa0Icbsycdx3SVK_GRLgi1ZdldoqUZ_uJVWULVvbriCGBvjDCavlgUVAi5RSsIqdvNWqhMh8IlymOiUsaobQMsZOjESKxvgFghyVni3x09OxIHE7_CQ9velhj_Mku_eSmzng3AcOp695ET6u0-nYKpXkaYL44HaB86suMYniiJQ1nbM9_8nbTBUhp0kjgJ1-xYQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=kM7GWvdfE3oUmA8NAdIaYJENAavOKEUs_8WUSPrcrk9cQojvtkAoxZsD3wv196h2dK1B8fV4d9dxPLdoSMMLDRahOn7Zn0QqQUbkZzpRq_-vdbDi3YE5cwNAK0WTNq2OvIqfNtj0cKhp5DoHavDa0Icbsycdx3SVK_GRLgi1ZdldoqUZ_uJVWULVvbriCGBvjDCavlgUVAi5RSsIqdvNWqhMh8IlymOiUsaobQMsZOjESKxvgFghyVni3x09OxIHE7_CQ9velhj_Mku_eSmzng3AcOp695ET6u0-nYKpXkaYL44HaB86suMYniiJQ1nbM9_8nbTBUhp0kjgJ1-xYQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vqxjxdhk6wT8rZWzfUYHhFXVKOU5pWFmeyfL_k0uZQYCe7cRwonrTr16B-l52PaAcx9k5WA4bHdjwxT9MVcKzYS5BL1JrQPxE3aIm2o8g9NuEMbQ2GB6UBpqCxwdZsZrifzMLbBewfnh7Gjn8Nkks_kom0bNHEGNBkFln-wmZkEP8BddLlUfvhpBM1Udj1YRyBYm8E5dkjs32ECSMKe2jJ4oR48cHESnuJNxv5I23Gz-VFrXKxstGIt_3A0pRF_3Tiw1HV75OUH23tQTG6c3CiTfZk2cQO1_LA-QsG8_jU1U6sl8-kdgFiTDPn_0lNp_YgbvOBmx89zySINruGdvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XX1ubjHcnGAQOf_U-izCT7UCsbyOZ_Ir51i34Jki_Vzomp9DY14gR6kWXVKZOM9SKrNSQ2-yRFbml0fkZQ_YXPWgiLg9KHvirxwoMPUBPsT825vHX5aiHm1pQCOPp8080fOUIxgUPi0VD8vKrWXcgBhE78PUGiXj_-lzFVkLduPDotBgWwfQIlag6ftg4B9Tguq2SCUsLoSrTpyHGDOJaNuQbG9aZvvDrnu4_W7ai5v-QC_f7BWnWHlujMlG9gF6NwYx2zZrv-hOB2uSQgzRIjaqyzPV8esMx2g66anICpEnjlXW6HpFz7ACLVlX0yp67nEBfTGc0_-N6X8cLXfq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_C6MEQzJiaWRf4JOXr3b-29Ks6gyYjahTCrfmYb0XUF9efg_kipa0xdSKPcRoOYFrDu2z7ApWHcVFDnuJul1qVErPL0buyXP0_6F_zS-yIz9u9C0BPpM2gxRyp-Gn2RNvGPf7gN4-GNRn7PTlVPfI0xdxSbUg8QFXASnkqXxdj0KNL9oE8cw-NRUc_zKJxPE2MudQmayyD_Dw6q2FwWwQLeic4ZBZiRGFF3epwJDBczDwCKs-E2Jn6WRVZ9-5QUUKzHZ0F2L6Sr-u1Ts2_Bpb6TGF4NT6wtqhOLMvYajgVQTrSTaNK3ad8T_WvaPiV3b4CBfr6iQ0oneYBCJf9vtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eodvtK_9AQE0O1kL8-55J83k1lqLisx9VmLlMSc6s5_sGCJg_xZPoX8rARCNKWB_ThigzejeT71fLqCzU7tzqjEW8hKzXpleV1RXw7MlHxOXFJBc7VU-7_-fkloE_PY765yiHaiywc-V5ebQ4CCDaZNBb0ltxRNe2WuQ7JRXAM_tZEvHu6b3et17l3B8Fo2lZf84ND9KG9drezshG-HV_QoRA3Ere08Bq5B63jjkxL3p20vLuSGOFU1m5b3KtZ0WBsLJz3VWAkxFvXFwjVmjg03Sn0XZxjytynGckSJg5Mpf6BiNpMft59DjVzXq8WnjPDIiKMVbsgZ3seRTcUTQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=n8XLLTVGcj2eBN-M_McJ4ATLcMnC_HWmmM8shafUWR-VTTYrr7VNge9nltD3uLikTjrYpucmIpm2AyQr3lCpi5nB3uchKZED9MNQTfM6ttbYcyq_2Bl9qWVkX1vyi30_NZJ4LvhM1kpxkFJK2REK7ZQXJXPxgKbOVo2yUhYXN0DGgdjXTFaFKzl9sYOEiQ-TnHbqQmkiY-hlhRG_qBGDq39cuiQoImjEbJHdPkV8wzQOQLWvdSN3mTbcxSsHkydg5hhXvS84EcKouH1ErxeqheEXX-7EAgHoTmloClCLlNfsl1xoss63gYJEuWL0OUjwxdK0pOPCwXoZqOeyXwsejQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=n8XLLTVGcj2eBN-M_McJ4ATLcMnC_HWmmM8shafUWR-VTTYrr7VNge9nltD3uLikTjrYpucmIpm2AyQr3lCpi5nB3uchKZED9MNQTfM6ttbYcyq_2Bl9qWVkX1vyi30_NZJ4LvhM1kpxkFJK2REK7ZQXJXPxgKbOVo2yUhYXN0DGgdjXTFaFKzl9sYOEiQ-TnHbqQmkiY-hlhRG_qBGDq39cuiQoImjEbJHdPkV8wzQOQLWvdSN3mTbcxSsHkydg5hhXvS84EcKouH1ErxeqheEXX-7EAgHoTmloClCLlNfsl1xoss63gYJEuWL0OUjwxdK0pOPCwXoZqOeyXwsejQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NdsUxIGZK3oO3CKIsV_mTq1MVHlAurgvw0KFxGPRfAhKibNLkPLJF_P8BJ2KEDrwyMWnq1kNw5yPqbCX9m0-f96h2Y68Kk0cLciuUlI6yjSxXI6IqZcNUnlhbb82-oHByN5ozqhaDf9DYbNIsAXTKG-3wcyOtYdp6DjQqjviRdxZRuYktz7ClpO9rUonVR4wXAYdEG6ex2RuWw-kqCB837tTQkCbYlO0CSMjNjpYKRsEwmCVJ4UAzA3HVNNwSQ30bmsPklwBGSklHGAr5D21Pz7cpviYVNyJwOqQvfhygUuKdfUmSzi78o0rYlFkvBplQTG_w50ueg5aZ0wckr9jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DIGu3d2_ZTn4m-cQqnxDXWF-B-GutwkjH8LDeYxLyZidbQ3kr0CZ35pn2N71nCjFg5pcuv6vrORh4wYWlUjch1XYMHvMjFI_OaJvD3351Ru8uCEPKcxxsMZb5RR8xybRZsAmVpz551W0yojYQnBFcEMQAf5nOFIiF9Ct1H5EOXJGchy5t72UldYmE99Vv6r698UhfelzQO_RP3n7mg5Bx1x8b37sQdmhi-p0bDP1qAlUcZWVEFoTHlFG8if-fAqw48_y32T5R-0PqczdDzIYGslbRGA5EXX1zThFExlMqNy5xDDxzwL968yaWuKBwGR1uUauNNKPXAnWj6cSRxiwDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnsS1UVbgZAg6upueJkdyUkcE6TqcLU2DnnbGKYmyxaU1zCn8KISIXQj0mtwvh68VC_najEv8m8iQlyTxFSU3bxaNmNvOubOUHlDn9_A6FqygFit2Hdh0ndFqcmYaZ8vAXYHm1g_GkWUC7pQed1UPFLJtGt2aiG8txW04166QRykTbwW_uoTGZz9RY_4j3nBjlx_gf4Z0YU4sWU9HE1r8tOrA8r8mcJtTYtYo5P3zlA91lTd_ezB7Y35S28ocIXlkGTlHBtjzKtfFFVoL_T638EQ5C92QNn8W1XWWWZbRFbuNOdW3kYQJfkZURzJr9FjWZC7lsWIDxf4fnfN2TyZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=ZpmSXaCVr_t2xpG191ylskLHc4HfU1O_ZVZ2nAem_zlwdMDuwf4NMCCfqDN0iRpn4_vrJHGK_hzIs0CwNIn9q6EwF1YpbUdE_7InsIhVZ8dcV4AlF7GckPZyyyz1MRonWuDQkOuWuwdQCuLU3DJXlWUpljILqCiPxPnXScJRUKn9ZfmcjXK8W7vfEUql9nfWulpGZ8iezBp7q82p7wkiLUkQf2Ly_NoaO6N1tBv-A0igSVNSRlEHtB68Iejgn5A_mce-g1XUHdcYkzhGz8ujMW5FOFjxxNvbLYDZqKRIH-gQyHkrE9sDwYklSanhM8_HEvenSTMIbp3rEUWsOLupdw_Dtx8N4qRhJP9spVJeKM0ZDrB-tU5HucL46yTS_fJDKlkCYHlEBKwOZRW3AGldIeun-XaX0HMiznZkGAYlcfSmRhbjBAEA3min53Dw7zjqCUV0xbKKSiXnvluvgh5Q5DYGfbw0zW8nTX6atXD0KHtKovkvOEiF8wEgEx8ki5V7_xJ7ZnHa1UJNSNDdbQvvvikzrQiiszwKF3fgxdc7vAmlol45Un6jms5syVDLMhDFhQOf_vH7vdgIc9t7vSxFVwn6pfX6bJ_t_ky4Snyyk8Vh6ipgsvpEugfeArCouU0eUQkx4E9yILPTP01aKvEmU7tGVr4akmB0kAmp9Ak3cz0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=ZpmSXaCVr_t2xpG191ylskLHc4HfU1O_ZVZ2nAem_zlwdMDuwf4NMCCfqDN0iRpn4_vrJHGK_hzIs0CwNIn9q6EwF1YpbUdE_7InsIhVZ8dcV4AlF7GckPZyyyz1MRonWuDQkOuWuwdQCuLU3DJXlWUpljILqCiPxPnXScJRUKn9ZfmcjXK8W7vfEUql9nfWulpGZ8iezBp7q82p7wkiLUkQf2Ly_NoaO6N1tBv-A0igSVNSRlEHtB68Iejgn5A_mce-g1XUHdcYkzhGz8ujMW5FOFjxxNvbLYDZqKRIH-gQyHkrE9sDwYklSanhM8_HEvenSTMIbp3rEUWsOLupdw_Dtx8N4qRhJP9spVJeKM0ZDrB-tU5HucL46yTS_fJDKlkCYHlEBKwOZRW3AGldIeun-XaX0HMiznZkGAYlcfSmRhbjBAEA3min53Dw7zjqCUV0xbKKSiXnvluvgh5Q5DYGfbw0zW8nTX6atXD0KHtKovkvOEiF8wEgEx8ki5V7_xJ7ZnHa1UJNSNDdbQvvvikzrQiiszwKF3fgxdc7vAmlol45Un6jms5syVDLMhDFhQOf_vH7vdgIc9t7vSxFVwn6pfX6bJ_t_ky4Snyyk8Vh6ipgsvpEugfeArCouU0eUQkx4E9yILPTP01aKvEmU7tGVr4akmB0kAmp9Ak3cz0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=vzel7vK2feIvL_Pv9juvP_xZnjTT8zV_bT-kLMXVg2M1n1KUQBrCdWy1oT2wzvlNZ4R6gR6udEr7edemCrchzGg9jtDr7dDqNbLG-WNZvVxnYOpVpt_C-syx1rLciJT8jCFbGPDD2Enyjb5qWmvZy9S0OFcqF5gdio1mgrEll53bCe_YkvU86jAZXtKzvCMu-57fFhhj7HFod9ZMvpnGoSHOYOA5AxC3brlKpAvRk7yUKSmmm_0S7LK7vlrnYO-MreUS7qlw9G87fR9Fc_k6p6mH3hyWo1QPvWXjqflF6hJiMSs6Ckybvp4bdZeRCCgeWv-5Eu_BLYF9LDjoi7yW5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=vzel7vK2feIvL_Pv9juvP_xZnjTT8zV_bT-kLMXVg2M1n1KUQBrCdWy1oT2wzvlNZ4R6gR6udEr7edemCrchzGg9jtDr7dDqNbLG-WNZvVxnYOpVpt_C-syx1rLciJT8jCFbGPDD2Enyjb5qWmvZy9S0OFcqF5gdio1mgrEll53bCe_YkvU86jAZXtKzvCMu-57fFhhj7HFod9ZMvpnGoSHOYOA5AxC3brlKpAvRk7yUKSmmm_0S7LK7vlrnYO-MreUS7qlw9G87fR9Fc_k6p6mH3hyWo1QPvWXjqflF6hJiMSs6Ckybvp4bdZeRCCgeWv-5Eu_BLYF9LDjoi7yW5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=E-MIrYUSkaiodH8Za0dg9c8AY4OsURAAvuLnF5xHzBy-uUI3NhdPROlf1kQwp8vBt28M3wtm9yW2kM1CgcMtzvJuExcLrGPe-3xNYh_81Mj43CWD45tTWKaR7D3QGhAUu4P_5F8A06dkFb0hLDTaNPdf-R_kWBu3ll1VKGfPcQ0mn3J7hm4uhwuYI5KU2VPzV6-RNOFsX5CbUUfYqSgoSMnpdv1dPirFFuF7d9s2xOuhUFMlFNl6Fjl2EQi9JFgvPhOZ_wBUSuq634Tm5dxJOL8I3Qka_kYBkB8zBZIllY4qid7Ak5QzZZ7X6DoPdiDE9rUbHbBcB6ykaaBKeU7AKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=E-MIrYUSkaiodH8Za0dg9c8AY4OsURAAvuLnF5xHzBy-uUI3NhdPROlf1kQwp8vBt28M3wtm9yW2kM1CgcMtzvJuExcLrGPe-3xNYh_81Mj43CWD45tTWKaR7D3QGhAUu4P_5F8A06dkFb0hLDTaNPdf-R_kWBu3ll1VKGfPcQ0mn3J7hm4uhwuYI5KU2VPzV6-RNOFsX5CbUUfYqSgoSMnpdv1dPirFFuF7d9s2xOuhUFMlFNl6Fjl2EQi9JFgvPhOZ_wBUSuq634Tm5dxJOL8I3Qka_kYBkB8zBZIllY4qid7Ak5QzZZ7X6DoPdiDE9rUbHbBcB6ykaaBKeU7AKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=r9zw39iukUK-lOybcrvQo8_MXw4v4NabnW92Fuk4z23xYQxAoiYetMzFoshlgVWLfEu16DgaJLeh30leIwuMRg89TIl3srwkSlPJinS_TYG038Zh4J06mrE7OYUu0GS3v5Gk1IbL-A03tFOMxKK4fKGoRr0HvBDw18iKu6aoIR2NHlNS69kNXKwra9s60XpVsj9-a_vN04_jYNwOGEF0waUfKhPcX2ptUhYnqPld9WF-A9lgN2HovBt2-sK8L_QI_rVk8i_9mRbTB72YABg3ganhAAmk2gOTBXAwK_PzYaTqQO4fOPipIdamQZVFVDB5S43KnOCIYNsWnzJOEoJWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=r9zw39iukUK-lOybcrvQo8_MXw4v4NabnW92Fuk4z23xYQxAoiYetMzFoshlgVWLfEu16DgaJLeh30leIwuMRg89TIl3srwkSlPJinS_TYG038Zh4J06mrE7OYUu0GS3v5Gk1IbL-A03tFOMxKK4fKGoRr0HvBDw18iKu6aoIR2NHlNS69kNXKwra9s60XpVsj9-a_vN04_jYNwOGEF0waUfKhPcX2ptUhYnqPld9WF-A9lgN2HovBt2-sK8L_QI_rVk8i_9mRbTB72YABg3ganhAAmk2gOTBXAwK_PzYaTqQO4fOPipIdamQZVFVDB5S43KnOCIYNsWnzJOEoJWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=dj2WxuTWmH-HkTjvLxcdkOxSytAMTyJ2tDUzrF7dbMVu6Pz_FKxtR5aGyy5mhW8gZyYhcjRx98LOO2v4cYj5Us7O0sQBOdMQoZwxDi4OWd4vhuD-KEo87mEst2ery5qcOpkXbH83URTbxYQtB5dXWkFXWiwpvBt2_MmjmekEle-BPd8rsh9VB6LFtwP-0RA6giDAk5Sz4z8Z2pKswxHS8FO9NEsJrRZVVA6WWDEgQaRx6OZ8Ct1UXDWoILdAu6KR0fGZpls_6FyRM0HwY34IE6Pt3dVcnCJhmb2tRc4u5vljzl2UFMeZRgzx9riyX9MxeZ3V_doXfsGSpzqLCJMOlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=dj2WxuTWmH-HkTjvLxcdkOxSytAMTyJ2tDUzrF7dbMVu6Pz_FKxtR5aGyy5mhW8gZyYhcjRx98LOO2v4cYj5Us7O0sQBOdMQoZwxDi4OWd4vhuD-KEo87mEst2ery5qcOpkXbH83URTbxYQtB5dXWkFXWiwpvBt2_MmjmekEle-BPd8rsh9VB6LFtwP-0RA6giDAk5Sz4z8Z2pKswxHS8FO9NEsJrRZVVA6WWDEgQaRx6OZ8Ct1UXDWoILdAu6KR0fGZpls_6FyRM0HwY34IE6Pt3dVcnCJhmb2tRc4u5vljzl2UFMeZRgzx9riyX9MxeZ3V_doXfsGSpzqLCJMOlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P52xcKDQ0LFQBX-CUOxwXTsE8Vf5-9dm0nuHla1c2XTx63WYtGFnSSQIBcIUenY8-HDaaB6NFKVZPUU2l6l0NjsyurZfxXQsJP_KkIuW6ER969MuKQvzn0UjVHG6hE9VeiVcuCVRKyqgLouHnnhefFymicEmwN85bjqKa5ptLMBAlKiM3wRPEtEZWRjgbX2PmEaHhK5kkZ__2speUalM7UDwjvX702Rme5kOk7NeZhyTCOxOAuvo9QKPQFwxU4tK0BORKnl2-ea9khYqNpgdd-1UfkbMPjfm0CFrTXiK6UCv3kGGFLbrZbSGhRaAfWvl5KyXkMeiZd_l2rHNmyJ1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmfYmGpxV4dKYyfuWvgZfqx1aAXKDvfX5AexIqXXWo7R0DVbQZ01d7qtoJYx6c8EFQwn_WXvSbLtlpbMnMiVvQJtwhdcYImBPl7Q3lQQcaYqmryfwAQPR2jbI_bhvd9a-A2i6CRlU2cwEDCGvR3iuFrQME5ta-o6uVpkdtToIZWzqsGI2NMDwtLBPXa4QV1V8Rvqb9QcNej8hsBefigeBEm0I6CM1ZCQ3UdQyxlaxUgRrO3Ir25Ads2jJjZ8TXzH-iWhvm3TF-RYGlm6tD03GMAZydfdu9JYL7eMFHjLho5vW-ZPfsYPLk-I9YEcCtwvjtdsXORzWzZoLwsasQG75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvRceJNPH4A0j1jGU82C07pX59mGyuqUpUioUDCg5lFVtkh3aorrZBEECGpQozvPJmaRfKz-yJuKh9pxrJtbXYKq6rfqQrhQym57eS2BdEmOHdMbMTg8ghjC8rcvnUnJqlyZhfKSgVNkMM4rDNtY5m0WTkr6XJMSGQg_gIhsGXHulLqmfraO3owT6uKwQHQmaVXUN0Dr2lG00H0_lnIimLpzucY0q0NCdBplpWM_GjQmasNojeQU1jalsT4oobSiB_xtVcIANJBTStlvEfPrXflvcY6o7aWfiW2eqnf6FPkHFgocBcF3rrhyyu7rr3ZDxwHIH5UX4lc8OTlDUx3dgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4SEDzw438EwVpHvudh5BAkg3gf-8yutEPJjJYCUEl5XMbmi5Dl0fo-xoyw-7dAUppsQAhTzmYh-ehyK0zZpqBTK0cilJftILG42I-GwLeCw1qbxYzU6cWwV0IKvYr6C1TEGRRilzfygYNGkfdqiYD-eAJePrjA-fMhcE1YHLXn6J-PCjim_LWJZ7q2dP7wzbUoI9S7Q74Syfszf3W_fEGFmjyRx8evqv0OhREOw0kLXqHBeFgNnV2msowZhjBGIZanaXmg4XvQU2oq1I5206T7xtWhfBq-QJ6-v4-YwjheI6L26XrAqPWI5cZ7QblSZf3k7s7NwRONW-MEehxQq0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_cH3qocNvXx9Z6b5gi8hF36HQzvqU9CtgW0wr9gqv35ZTSoFpkcItDyh4eYor2NckyWleIZVjqf4z4v3_qrLlGGL3j8ctNh0ks3kfoSxyR-4KCzZ2gi_b8JeNzN177I9g6h8uPNniC-em1qXWvWF7vMnDlECYpRrYCL9gGe3GQkjad7CMCE1BWNzuBPKljPvsulmRswHGdyMYFwJuKPyl4qpPUsIHlyyltlDoW0BWesjdJngNZudaCSDL0z5gVuCOvxhZn0SQyT3UpcDZ_JXEIZKVFQNAGO2O2WGIrzOz-peUkhvebtjBnGrpYy7S7yoZd9kOliNA3MN6E28zhx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rGd-ajFBIhDJe4T8UCFJjOw1HLh7TC9BeE7mzZms2BYW5ORbC9-q8wDolk4ZdwfNdnAlsxtmkdaTax6wYoMXKsBcNyddtz_8AIQ9Be-vRocZ432tsqZoUY_yDCyCoyi_RhISgHctloBI0bjmhofUEjIPknmIWh3uzsQJHnCX7jXXA_HxDjZVTRogPxkTFVVnsMC9SBIg2tBeodQVqxnIl9cej-FUr5wrrHzcdJIRrWmp-RImgkwTlRLFCrqjK4gQgyrfaHWkE0wS00sb0pidlvF0x-uCGDBrwbzWDh8Z7FCt2TfkSOygNegy0qx-Ay1PRQGBSFvq830fgTWSxg3zYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rGd-ajFBIhDJe4T8UCFJjOw1HLh7TC9BeE7mzZms2BYW5ORbC9-q8wDolk4ZdwfNdnAlsxtmkdaTax6wYoMXKsBcNyddtz_8AIQ9Be-vRocZ432tsqZoUY_yDCyCoyi_RhISgHctloBI0bjmhofUEjIPknmIWh3uzsQJHnCX7jXXA_HxDjZVTRogPxkTFVVnsMC9SBIg2tBeodQVqxnIl9cej-FUr5wrrHzcdJIRrWmp-RImgkwTlRLFCrqjK4gQgyrfaHWkE0wS00sb0pidlvF0x-uCGDBrwbzWDh8Z7FCt2TfkSOygNegy0qx-Ay1PRQGBSFvq830fgTWSxg3zYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=luHVWi8Ud9DeN_OTjcfRu5QU81OQ0p1YON3FQV2cjsh2FZ5NHg8hPAPzXt-h91_4cNVWv2zceuHoh_YjstFnJQzTtLznNVMrGKJNXucA6TM0k6DCEZAPFxCipfhV5HfhD8_Er02suZwQDmIFAzE0H5XQKXnxxqb9RUMICzfi8eOUpc10_Vq9PwtO2X3MIhjB9O7IeCPLb0JNEB7zCrGFSrJMFhCJd4mxt6txxua5W4m7dEO51ws-4_inmTQ0NoOgmal8_qWTaF7N_Zd60w-r8hJNcB2LH-oRxXgTHZ4Wr3dgpwOrWqvZ9S2YvgGJ4_EcnhO9jOC1fQ20FK0HlA37GkvMinM827sLGpJ7XjbR6EAR52zkBrWnMotqK4DAF4rE6SL7sX_HJwtp6o4Pawb0JxalREI7oOWNCmd9eWZwxNn36A6ytJFraVa1nWqId2iyzJyNJEkS703-IHQgbMd6I-6kk-rf4pQesVsrywMpRTbfFX6AGuebdZRb47zSsXY6_aQ05OtTdt3j9UVZFaSGVwHxgeG10BVpD_X9XPoiu1__TuxlcgXGJ64J4eKKrFbDyt_q7SlhLAURYAw2tXO-iHUUSSZE_KdJXB1SK-CxxdSyNbd8cNvdXd5Wsz0DXikFwWFZoDc_p8oLtyni6CxT4wwU1V1T7gL9vx3VdaNhVgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=luHVWi8Ud9DeN_OTjcfRu5QU81OQ0p1YON3FQV2cjsh2FZ5NHg8hPAPzXt-h91_4cNVWv2zceuHoh_YjstFnJQzTtLznNVMrGKJNXucA6TM0k6DCEZAPFxCipfhV5HfhD8_Er02suZwQDmIFAzE0H5XQKXnxxqb9RUMICzfi8eOUpc10_Vq9PwtO2X3MIhjB9O7IeCPLb0JNEB7zCrGFSrJMFhCJd4mxt6txxua5W4m7dEO51ws-4_inmTQ0NoOgmal8_qWTaF7N_Zd60w-r8hJNcB2LH-oRxXgTHZ4Wr3dgpwOrWqvZ9S2YvgGJ4_EcnhO9jOC1fQ20FK0HlA37GkvMinM827sLGpJ7XjbR6EAR52zkBrWnMotqK4DAF4rE6SL7sX_HJwtp6o4Pawb0JxalREI7oOWNCmd9eWZwxNn36A6ytJFraVa1nWqId2iyzJyNJEkS703-IHQgbMd6I-6kk-rf4pQesVsrywMpRTbfFX6AGuebdZRb47zSsXY6_aQ05OtTdt3j9UVZFaSGVwHxgeG10BVpD_X9XPoiu1__TuxlcgXGJ64J4eKKrFbDyt_q7SlhLAURYAw2tXO-iHUUSSZE_KdJXB1SK-CxxdSyNbd8cNvdXd5Wsz0DXikFwWFZoDc_p8oLtyni6CxT4wwU1V1T7gL9vx3VdaNhVgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btj1R2S08GB-eb-_MC6m6trDcwJtgjlRr2GXXC2WqcjMihnDVre269HLUVlwyuNHf5MTRd4vJSFa_QHosoiX6PAgz8JT84yLjpmG-iMlgoihpZhTDXVxEe56x-C00m_o3dtUoLMSNt1l3OXSO4_JSZk8Co7FeVF5zxuSnNlI-9kMhb8K1waci9ceI79tHq_VmGGLMNrdF9a9TH-mmyUdaGCQbIeHubOjlm0YvyEWXmN4QsXBqR60D5_ltfDWN-tANoMzp4t82B7FtcwiGl_NMx_GuKAspKT4DisgRsGLXS4nGd4uc0kc8O-s_8QL2M1eDZau9bEBh9AUwukOXd1d-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T07fO3q9g1BMuFYOg9EZh6LbOHSQKZ_BOdunW7mB1-hiu7_2C1l8XKA12XZQjlZ86JB24zG79l7TKfDZU2czmX8FI9Cl2dCqbUQtesCzyY9nRDv7qPqulsUPJlaGG43q5ZMfJCaPrx4LXAaJleSUG2AoO6v2vuNxdPEWKK5cv1utrmeF7RMuENYI68ep6DR1dRd_xy51GIJ5kLl1FkqaZV5DmaBx-B47uvkQY60ed8KlPm9uQ_Pc-bxEYonikaSxAeP0NK1wtnudEMBQWQnbD1fjcqFni8EwvvETodSAzTqGWF7zn2plguNd8jAVdRJIG3ZHr9g17GQufdkS2SNDLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EidVIR8dJYu-hsyHMLDvpXva4cjXRXhP0-MSKJjdgAiMdxojLVBoBGsQqG5Oy4rEMqoBOJp-CQV-GkqPWvVN3MWbH_Js7orkWfEmQ24zYExdzul8L6oEnj3LEKJXn00EqgLOP1PJIQRDPOrtdW-oYrxzikewrTThjs8w-o29HIisTsfd18v29Fp0t6srxHzZlr9sgegAVCVatv1gBpM3awbmUqUWxMuCEUK6xR-5yZMo2cG4KPOE_F7HqTACqGxikrYiOeGD-m5bFZy_G9fsrrbYSXx14I1nIehMBOA0gCjS30ngO-di8zFz3u9e13PMsQY8yEM6V9B7aiF_Fc2sNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKd8-An5BDyztZHFjF-z27_Dy2RhnNWsWpdHuLDy54mpXBPy0wPwJJDuotGcARbkB501vE0QVp1PHUJ_oQdBMrgtW-_O0vd8TxbWj_XpERGhjtFHOjHXuQaKyYt_6vsYFlYydfVBP_7OGtRKT8zuTOHKIUQi_gnNZS4LLdGGDa28ajFhf1XhZrMOCv9mnOpG_IreiyYr98Uoy_mC1bz-DuzVxIBVRmLB0oEjCRgyo2OepyvQCJXJwSumwb71ItoCZq0jccX7yy3bpj3YYvo4iNez9d21F11Wwfn5DbD6DBub0xSUWWCmn4O-IL_r6d98f1uZN_RYV3RABX13rQFbHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
