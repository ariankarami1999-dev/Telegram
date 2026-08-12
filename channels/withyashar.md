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
<img src="https://cdn4.telesco.pe/file/ewP945oEBOYeKUAhNfcsOMd8nYrUfVyNu3u5EhS9kJ636mmYKnbQHLFLz-on_798KPPVTM7V_s-G9zkBbqUP-o4k8GkgsusH4EnVVOow8Vm7dmEUXPJzdL55n9pKVw7GzEwRYeJhg_Dj1tPmKp0Avu9sT5Zwd3VDbPMbw9ky6f3KIu7XvR7BnAcIwRvMP6fi6W-edi8LmwYyj3udBPRBRB3op2YJP5-BJ8K_PIPQA8uxxWuz1kI_PaOdilx7TaM56oT0w9dsblRnjaRispo8zSVULcebacXx5zye5-VpyEaoSierZeNYiM3LTQqasMqAuiSUskzrF0wuiRW0J8e_qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 445K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 20:55:21</div>
<hr>

<div class="tg-post" id="msg-20898">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد. ‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند. @WarRoom</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/withyashar/20898" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20897">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مشاور ارشد قالیباف :آ مریکا و اسرائیل برای یک حمله نظامی پیش از انتخابات سراسری در اسرائیل و انتخابات کنگره آمریکا در آبان ماه،آماده می‌شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/20897" target="_blank">📅 19:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20896">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">وزیر کشور پاکستان در ایران به عراقچی، وزیر امور خارجه، اطمینان داد که "توافق دفاعی مکه" به عنوان یک ائتلاف علیه رژیم ایران طراحی نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/20896" target="_blank">📅 19:03 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20895">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=mXaH_SHNDWS6A15pJtrC600xf2lqjDsiUBafHevyDQHGgHVXQRj9CDj_ICY4wRR_oy7V0Belp-p4uGwl1SVp8VdhAeZQ26uK0rn3avZawD2H4ndp-GSNvaDBoJFMXjRDlFsJGordEzrEj7lXygW6jbmZ4zaZA0_cAGf8ruJyjQEAlba-pIOLAeq1brNZSQShOyE2aybevRGfqodLzjLTsyO0fHRI8Jr4_XgPbYYlBoxBNzE5VnyTcdHIBGs4vOebIqrKdl-GDfBCYva8bqzrDmsa7UVSrKhx3J3jq_044pAxAyFDQTJacaUybFhSCQdeG3xf_CxcJ7F_nr1M79Jjui6Q6mHubdZWiHCZCgJyEuhINK6qq3Q_1GHFMG1MMHOn9YArDaNEMA1aBz3SqwJX2jGfzZ3tPkYH_e-pV68-xm2YqqE7StaWYtfenR_0JdJKY4AG8UbK99__nEP4-aRhq6mWqkQtzX521v8FxeTxNN-lY9t4HM4ngdaLLyiJNLOfHlrW8v7vrMQ9Bzh51DCA2rwZgJ8mLG0mdiOk7n2mXIkk4TGlO3XZYT9ms-2qCTLpGQvyyrGhzJrVhcCFYcI4XaEDOZ7sT-XdbHFA4r4lvKpOvXYqg_PtJNZ2kFl7azPGRJ0UcwnW0lp7roQdGEHdjaF9GMBacMqlB78GTUC6dfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42557aaa83.mp4?token=mXaH_SHNDWS6A15pJtrC600xf2lqjDsiUBafHevyDQHGgHVXQRj9CDj_ICY4wRR_oy7V0Belp-p4uGwl1SVp8VdhAeZQ26uK0rn3avZawD2H4ndp-GSNvaDBoJFMXjRDlFsJGordEzrEj7lXygW6jbmZ4zaZA0_cAGf8ruJyjQEAlba-pIOLAeq1brNZSQShOyE2aybevRGfqodLzjLTsyO0fHRI8Jr4_XgPbYYlBoxBNzE5VnyTcdHIBGs4vOebIqrKdl-GDfBCYva8bqzrDmsa7UVSrKhx3J3jq_044pAxAyFDQTJacaUybFhSCQdeG3xf_CxcJ7F_nr1M79Jjui6Q6mHubdZWiHCZCgJyEuhINK6qq3Q_1GHFMG1MMHOn9YArDaNEMA1aBz3SqwJX2jGfzZ3tPkYH_e-pV68-xm2YqqE7StaWYtfenR_0JdJKY4AG8UbK99__nEP4-aRhq6mWqkQtzX521v8FxeTxNN-lY9t4HM4ngdaLLyiJNLOfHlrW8v7vrMQ9Bzh51DCA2rwZgJ8mLG0mdiOk7n2mXIkk4TGlO3XZYT9ms-2qCTLpGQvyyrGhzJrVhcCFYcI4XaEDOZ7sT-XdbHFA4r4lvKpOvXYqg_PtJNZ2kFl7azPGRJ0UcwnW0lp7roQdGEHdjaF9GMBacMqlB78GTUC6dfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏وزیر دفاع اسرائیل: من به ارتش اسرائیل دستور داده‌ام که تمام اقدامات لازم را برای حضور طولانی مدت در منطقه امنیتی لبنان، سوریه و غزه انجام دهد.
‏ارتش در منطقه امنیتی لبنان، سوریه و غزه برای دفاع از تمام اسرائیل باقی خواهد ماند.
@WarRoom</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/20895" target="_blank">📅 18:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20894">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">امروز،
۱۲ اوت ۲۰۲۶
، آسمان شاهد هم‌زمانی
چهار پدیده نجومی
است:
صف‌آرایی شش سیاره
شامل مشتری، عطارد، مریخ، زحل، اورانوس و نپتون که پیش از طلوع خورشید در امتداد بخشی از آسمان دیده می‌شوند؛
خورشیدگرفتگی کامل
که اوج آن حدود
۲۱:۱۷ به وقت تهران
خواهد بود و در ایران دیده نمی‌شود؛
اوج بارش شهابی برساوشی
که از امشب تا بامداد ۱۳ اوت ادامه دارد و در شرایط مناسب می‌تواند ده‌ها شهاب در ساعت ایجاد کند؛ و در نهایت
ماه نو
که یعنی ماه تقریباً بین زمین و خورشید قرار می‌گیرد و از زمین دیده نمی‌شود. نبود نور ماه باعث می‌شود آسمان تاریک‌تر شده و شرایط برای تماشای برساوشی‌ها بسیار مناسب باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/20894" target="_blank">📅 18:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_N7Kv2T7h9wPEPGRs0eiudqz_VoKJZTzSVGANiZZGHSYskS5NHZOKRV7eZq4kRjm1x28SVg3wbDwzz9NjzBkb5DJc8zdwTmgCYGgUkX9rT-53vq29PUbuTJz53ur6sSwnC5DNq6GGkLpfCUaYeR-Z9VF51QCz1gvJfoLwAXHFqQa7QWk9F3Cg28GN1tkyh1OWIaeoQzDBjX6gHnYRyC0UN7qZnIrhctPwzJ2NItRij8G97EzbzTPsPvhuH-aQKdDdguSbIGWGGU8Y703uSo68ZDlLGV4DyIEV61n-3ZRnjgoyi7P_3G3VG40DhY50iITBA-gccYh-994ec7VeVZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:ایالات متحده کنترل کامل تنگه هرمز را در اختیار دارد. فکر می‌کنم آن را حفظ خواهیم کرد! محاصره دریایی ما از سوی همه «دیوار فولادی» نامیده می‌شود و ایران هیچ کاری از دستش برای مقابله با آن برنمی‌آید. آنها نیروی دریایی ندارند، نیروی هوایی ندارند، سربازان باقی‌مانده‌شان حقوق دریافت نمی‌کنند، سپاه پاسداران به‌شدت تضعیف شده و در حال فرار است و «رهبری» آنها، در بهترین حالت، نامطمئن است! آنها پولی ندارند؛ کشورشان «ویران» شده است. تنها چیزی که دارند اخبار جعلی و تورم ۳۰۰ درصدی است که روزبه‌روز بدتر می‌شود! ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند؛ دیگر قلدر خاورمیانه نیست. ستایش از آنِ الله باد!
@WarRoom</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/20891" target="_blank">📅 18:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20890">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=V_Y922Dsr4PJDmmGuej_ujBEnitnbHEGAmE4B-yUomOMPBaPpFmiW3RE1EUZk9nb_luvsqGn__oaHK3ZcnQdiMNJkw3GKeSgmoDi4aUyQwrPGxPfNW1PQFoJPPMNa74vNDi3EL8E_bMX746YneSxWT5GrlH0CIMsa508pEEF-Wun4EaQoEDqd7wfWYTeNQPhVvdsooxlBGTCAkUxWaEXoCJfbTzXVBF1nkU0rE2Pt7PHRlYbSEVK91YP1WZ9_WGnfuW1xK-ENz6-dnu2dPGHLfzRfhxGx0mnYPUf5gnsYtxvmp5Z5BH4eqDq8t-Iv6JzzX-6VX4u-MQihT8MAZb93w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7908fd3c.mp4?token=V_Y922Dsr4PJDmmGuej_ujBEnitnbHEGAmE4B-yUomOMPBaPpFmiW3RE1EUZk9nb_luvsqGn__oaHK3ZcnQdiMNJkw3GKeSgmoDi4aUyQwrPGxPfNW1PQFoJPPMNa74vNDi3EL8E_bMX746YneSxWT5GrlH0CIMsa508pEEF-Wun4EaQoEDqd7wfWYTeNQPhVvdsooxlBGTCAkUxWaEXoCJfbTzXVBF1nkU0rE2Pt7PHRlYbSEVK91YP1WZ9_WGnfuW1xK-ENz6-dnu2dPGHLfzRfhxGx0mnYPUf5gnsYtxvmp5Z5BH4eqDq8t-Iv6JzzX-6VX4u-MQihT8MAZb93w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منم مشکلات زیادی دارم ولی برای شما شاد هستم
😍
🙌🏾
@WarRoom</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/20890" target="_blank">📅 18:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20889">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/20889" target="_blank">📅 18:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20888">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش CNN: وزارت امور خارجه آمریکا به دلیل تنش های احتمالی به سفارت‌های این کشور در خاورمیانه دستور داده است تا برنامه‌هایی را آماده کنند که به آن‌ها اجازه دهد با تعداد محدودی از کارکنان به فعالیت خود ادامه دهند
@WarRoom</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/20888" target="_blank">📅 17:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20887">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=fE6wGH81y2CoFh9AQpMqdKTIMtzqkuzSiIgjEbX8bQc4nNf0SYeMBpBFNVKPbLO1k9_9ETAMm1mizMfcRukbmTjKQoLy_G--tKAMTYonRk5AD9UkYuJixCez4-RW0F_6lSSuSh4TKcXzSclrf-HrXrp2KuJ5X8CaDl8KHofCirWTrP9n-B7INNit3eejTX06gsiCXtSGXN0-B1XgtzlFhworgmdJR2VSNYn3poBj9bAUtXHwgM7mEjhN_9QKguI1JeifLYtZL7tSVMB8iCCHG0lZ_nemhbPYbHl7gdeXBKG41-XFxDcg_n7U5cG14ldsc9rEP5OwQYCeu9yEYus3jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6ab93f52.mp4?token=fE6wGH81y2CoFh9AQpMqdKTIMtzqkuzSiIgjEbX8bQc4nNf0SYeMBpBFNVKPbLO1k9_9ETAMm1mizMfcRukbmTjKQoLy_G--tKAMTYonRk5AD9UkYuJixCez4-RW0F_6lSSuSh4TKcXzSclrf-HrXrp2KuJ5X8CaDl8KHofCirWTrP9n-B7INNit3eejTX06gsiCXtSGXN0-B1XgtzlFhworgmdJR2VSNYn3poBj9bAUtXHwgM7mEjhN_9QKguI1JeifLYtZL7tSVMB8iCCHG0lZ_nemhbPYbHl7gdeXBKG41-XFxDcg_n7U5cG14ldsc9rEP5OwQYCeu9yEYus3jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری پی بی اس: چرا مجتبی خامنه‌ای در طول این جنگ هرگز در ملاء عام دیده نشده است؟
محمدرضا نقدی: استراتژی متعل به اوست. دشمن ما جنایتکار است و به هیچ قانونی پایبند نیست.
مجری: آیا این به دلایل امنیتی است؟
نقدی: طبیعتاً به دلیل امنیت است. مطمئناً دلیل دیگری وجود ندارد.
مجری: آیا او را دیده‌اید؟
مجری: بیایید این موضوع را کنار بگذاریم.
@WarRoom</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/20887" target="_blank">📅 17:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20886">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=Aen7UrR1Gtnv_O2v2VDZ3g0VuW3nkMd4oepyJDDgeeh-sMwbN0_xwQlFMnSYcZuyA7wVLG_ovOEL4oLFpnziQkr0f0px7YaSsX3RLsQsqpsB4aQ88SUSGo2Eo3oIK_vVTGOUz9wZvU2ew39x3eo-FT0IerTFlKyW5BMPQ9oVKvkWtymuH-7t58LaiJqlrGPqaYGSAZ1jJFCd6zPkPBidSQOsXzIR3CUYwQFkbtQz39OtAVleWyXBPCbFFlkWxLyNrcpIbkq2S8ZuaYGFaWX7MxsGOwDtQ6YfKQDprECLuu9_IofxwbL0DnGYDjF76O0VKMmVuPrxwNxczhnCYKnM_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7137b6f963.mp4?token=Aen7UrR1Gtnv_O2v2VDZ3g0VuW3nkMd4oepyJDDgeeh-sMwbN0_xwQlFMnSYcZuyA7wVLG_ovOEL4oLFpnziQkr0f0px7YaSsX3RLsQsqpsB4aQ88SUSGo2Eo3oIK_vVTGOUz9wZvU2ew39x3eo-FT0IerTFlKyW5BMPQ9oVKvkWtymuH-7t58LaiJqlrGPqaYGSAZ1jJFCd6zPkPBidSQOsXzIR3CUYwQFkbtQz39OtAVleWyXBPCbFFlkWxLyNrcpIbkq2S8ZuaYGFaWX7MxsGOwDtQ6YfKQDprECLuu9_IofxwbL0DnGYDjF76O0VKMmVuPrxwNxczhnCYKnM_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری آمریکایی پی‌بی‌اس : آیا هدف ایران این است که این جنگ را طولانی‌تر کند، شاید تا زمانی که آقای ترامپ از قدرت کنار برود؟
نقدی، فرمانده سپاه: ببینید، ما باید به بازدارندگی برسیم تا دشمن هرگز جرات حمله به ما را نداشته باشد تا بتوانیم با امنیت زندگی کنیم.
یک راه این است که این جنگ را تا رسیدن به دوره بعدی ریاست جمهوری ادامه دهیم و فرسایش ایجاد کنیم تا اگر کسی بخواهد به ایران حمله کند، بداند که هزینه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/withyashar/20886" target="_blank">📅 16:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20885">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKrdbYYeCKkyVKbpeUAv_-0KGLipff9s84bX1w7tA46_bE5Asbldxn3Gp2N8AYNJ825Fo_b7mrag2sXvMNWJGCHVhPUMQCxC_ReANZVzoX597uWu93ndagYKI_NgoDxIfMrGuF4IrC1P8ikyFKvQMS58fnefEhguXOeNcSfBZDynu2jvfkygrre1wjGcRVUzvH43goKFbrv8S-QsicmVivvvKJj27K9KGeESes2Hb0i6oOThS2l4DVivVD8_-5yRULzkg_Bk7U-KRK6AwRkmKx4rWj3IOvsxuSK1N3et0J7sTntX_36dwKSCtUuOs8EPwdIxK7p0Kggx3e7QOchgSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پهلوان آواز ، «ایرج» خواجه امیری،  خواننده قدیمی در ۹۴سالگی درگذشت
بخش بزرگی از ماندگاری صدای ایرج در سینمای پیش از انقلاب، به ترانه‌هایی برمی‌گردد که صدای او روی تصویر
محمدعلی فردین
است. ایرج خودش گفته بود در
۲۶ فیلم
به جای فردین آواز خوانده است. در مجموع هم گفته بود برای
۱۳۵ فیلم
خوانندگی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/20885" target="_blank">📅 16:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20884">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجار های جاسک رو اعلام کردن کنترل شدست ، هم اکنون باز‌ داره گزارش‌ میشه
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/20884" target="_blank">📅 16:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20883">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">«الحدث» به نقل از منابع آگاه گزارش داد که اسماعیل قاآنی، فرمانده نیروی قدس سپاه، در سفر غیرعلنی اخیر خود به بغداد با رهبران حشدالشعبی، گروه‌های مسلح و چهره‌هایی از ائتلاف‌های سیاسی عراق دیدار کرده و
پرونده حصر سلاح در دست دولت
را بررسی کرده است. طبق گزارش‌های تکمیلی، قاآنی از گروه‌ها خواسته از هرگونه درگیری با نیروهای دولتی جلوگیری کنند، اما هم‌زمان با
تحویل کامل سلاح به دولت عراق موافقت نکرده
و بر حفظ توان نظامی این گروه‌ها در برابر آنچه «تهدیدهای آمریکا» خوانده شده تأکید کرده است. دولت عراق برای تعیین تکلیف سلاح گروه‌های مسلح خارج از نهادهای دولتی،
۳۰ سپتامبر ۲۰۲۶
را مهلت نهایی تعیین کرده و پس از آن قرار است با فعالیت مسلحانه خارج از چارچوب دولت برخورد شود.
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/20883" target="_blank">📅 15:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20882">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پزشکیان: جنگ کنونی از قبلی بسیار پیچیده تر است و دشمن قصد فروپاشی نظام از داخل کشور را دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/20882" target="_blank">📅 15:34 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20881">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در ۱۷ اوت منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته…</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/20881" target="_blank">📅 15:31 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20880">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">خبرگزاری آناتولی به نقل از منابع دولتی پاکستان گزارش داد تفاهم‌نامه قرار است در
۱۷ اوت
منقضی شود. به گفته یک منبع نزدیک به روند میانجیگری، دو طرف موافقت خود را با اصل تمدید مهلت به میانجی‌ها اعلام کرده‌اند، اما
هنوز درباره مدت دقیق تمدید تصمیم نهایی گرفته نشده و تهران و واشنگتن در حال تبادل پیام برای تعیین بازه تمدید هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/20880" target="_blank">📅 15:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20879">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک منبع ارشد ایرانی به رویترز گفت:
هیچ بحثی برای تمدید آتش‌بس بین آمریکا و ایران وجود ندارد و در عوض، مذاکرات بر بازگشت احتمالی آمریکا به توافق‌نامه تفاهم (MOU) و یک جدول زمانی برای اجرای تعهدات متمرکز است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/20879" target="_blank">📅 14:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20878">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش صدای انفجار‌ در‌ جاسک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/20878" target="_blank">📅 14:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20877">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سخنگوی وزارت امور خارجه پاکستان:
فرایند صلح گسترده‌تر بین آمریکا و ایران با مشکلاتی روبرو شده است و ما امیدواریم که دو طرف به گفت‌وگو بازگردند. ما می‌توانیم توافق‌نامه همکاری را قبل از پایان مدت اعتبار آن تمدید کنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20877" target="_blank">📅 13:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20876">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بلومبرگ : ایران در دور بعدی جنگ، به سمت یک وضعیت نظامی "تهاجمی" پیش می‌رود. این کشور در حال بازسازی ارتش خود است تا آن را انعطاف‌پذیرتر و تهاجمی‌تر در برابر تهدیدات خارجی کند. این اقدام، در سایه جنگ با ایالات متحده و اسرائیل، نشان‌دهنده آمادگی ایران برای یک رویارویی طولانی‌مدت است، حتی اگر درگیری فعلی به پایان برسد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20876" target="_blank">📅 13:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20875">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک تایمز: در نزدیکی اجلاس ناتو در ترکیه شخصی با موشک دوش پرتاب شناسایی شد!
نیویورک تایمز گزارش می‌دهد که تهدید ایران که ماه گذشته باعث تبادل مخفیانه هواپیمای رئیس جمهور ترامپ شد، در حالی آشکار شد که او در آخرین روز حضورش در اجلاس ناتو در آنکارا، ترکیه، در 8 ژوئیه حضور داشت.
سازمان اطلاعات ایالات متحده چندی  جریان اطلاعاتی دریافت کرد که نشان دهنده یک تهدید موشکی زمین به هوا علیه هواپیمای رئیس جمهور بود، صرف نظر از اینکه کدام هواپیما حامل رئیس جمهور بود.
همچنین شخصی در نزدیکی اجلاس ناتو با یک موشک دوش پرتاب مشاهده شد، در حالی که عوامل ایرانی دقیقاً می‌دانستند ترامپ در آنکارا کجا اقامت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20875" target="_blank">📅 13:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20874">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سازمان بین‌المللی دریانوردی:
نشت نفت از نفتکشی که در شمال شرق جزیره قبلیه عمان به گل نشسته است.
انتظار می‌رود نشت نفت از نفتکش کارولین بیزینجی به عمان برسد.
بادها دسترسی به نفتکش به گل نشسته در نزدیکی عمان را محدود کرده و عملیات نجات را به تأخیر می‌اندازند
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/20874" target="_blank">📅 12:49 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20873">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ
:
سامانه دفاع موشکی «گنبد طلایی» آمریکا نخستین آزمایش‌های اولیه خود را با موفقیت پشت سر گذاشته است.
به گزارش بلومبرگ به نقل از یک مقام ارشد نظامی آمریکا، این مرحله از آزمایش‌ها شامل انتقال داده از حسگرها به رهگیر و همچنین ارزیابی سامانه پیشران فضاپیمای رهگیر بوده است. به گفته این مقام، آزمایش عملیاتی گسترده این سامانه برای اواخر سال ۲۰۲۸ برنامه‌ریزی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20873" target="_blank">📅 11:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20872">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">تحریم‌های آمریکا، صادرات نفت ایران را محدود کرده و باعث شده بخشی از
مشتقات نفتی، از جمله قیر،
به‌جای صادرات در پروژه‌های آسفالت‌سازی مصرف شود؛ تا جایی که علاوه بر خیابان‌ها، بسیاری از کوچه‌ها و جاده‌های خاکی نیز آسفالت شده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20872" target="_blank">📅 11:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20871">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مذاکرات ایران و آمریکا درباره تنگه هرمز به نقطه اول برگشت
خبرنگار الجزیره در تهران:
مذاکرات ظاهراً به نقطه آغاز بازگشته و توپ در زمین واشنگتن است؛ تهران ممکن است به این نتیجه رسیده باشد که نحوه عبور از تنگه هرمز نمی‌تواند صرفاً بر اساس خواسته‌های آمریکا تعیین شود.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20871" target="_blank">📅 10:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20870">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=LcpIBDzj6l7kUUNwS3CkYdP0L-wt5sTCTNjb5Us708Fd6hhJbFgOy75SkgXMuPQsUF-KqG26X5zI89tPYklWwRmDxI0dKGHChdpVqjaPOw5sBlHaAlVNZCeW5WHryx8wBbNtd0ap7F2Oab0piZJQrqjAY18vwL1ZMmsgexlqv1rv_BdacqCE-ORr3j24X8oU2AtfC3SYOseAPxdYmrPTN9erGOOA8sdSTxYrOkNRusCN22O2BfKbJrMgfqVItzloe_vvCIDN1CeZaEjGeW4zlN7zzmHeE5BKncJsRW_bmXgrox3dfuryCP1ub-6yCu_IlY0urohB0XwcIfnD82mQtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97fd9de97.mp4?token=LcpIBDzj6l7kUUNwS3CkYdP0L-wt5sTCTNjb5Us708Fd6hhJbFgOy75SkgXMuPQsUF-KqG26X5zI89tPYklWwRmDxI0dKGHChdpVqjaPOw5sBlHaAlVNZCeW5WHryx8wBbNtd0ap7F2Oab0piZJQrqjAY18vwL1ZMmsgexlqv1rv_BdacqCE-ORr3j24X8oU2AtfC3SYOseAPxdYmrPTN9erGOOA8sdSTxYrOkNRusCN22O2BfKbJrMgfqVItzloe_vvCIDN1CeZaEjGeW4zlN7zzmHeE5BKncJsRW_bmXgrox3dfuryCP1ub-6yCu_IlY0urohB0XwcIfnD82mQtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ : «من از طریق سرویس مخفی و ارتش اقدام می‌کنم. آنها می‌خواستند من با پرواز دیگری، با هواپیمای دیگری بروم... من هر کاری که آنها بگویند انجام می‌دهم... حدس می‌زنم تهدیدی وجود داشته است. من واقعاً زیاد در مورد آن سوال نکردم. تهدیدهای زیادی دریافت می‌کنم.»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20870" target="_blank">📅 09:21 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20869">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=M6GmPjMr1Mucu3THQ_SlZO8S56nMvrvlCSqqzT98dJw0q0mJj2SYwHeQ8tSz8irs8ICOaHk98ltfwOaLpaRJEdNjuotrmWuwVILeDs4le7rROyFUjjP33x4N3JUoZqysi8HFfhPJSH3ERzkfZZM27dsuGQdccybqxad1F9WQXNLi1BUYIGdhynrIs2MZ5AbVYU9kSIftxr5cM6_mGhLuBZaLD3iV1fnJDKjPMbZ7ptJsbtpl5hU-TwUC4QYEqGLX2-EdbtO_E7UI2-p9L6tlyRCkIt0j-6zTewMjO3buZQe8ipWzMjDEwmz1yTZgfxXyxbYoimMaElQyo1xoxzr9bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e3f3981e.mp4?token=M6GmPjMr1Mucu3THQ_SlZO8S56nMvrvlCSqqzT98dJw0q0mJj2SYwHeQ8tSz8irs8ICOaHk98ltfwOaLpaRJEdNjuotrmWuwVILeDs4le7rROyFUjjP33x4N3JUoZqysi8HFfhPJSH3ERzkfZZM27dsuGQdccybqxad1F9WQXNLi1BUYIGdhynrIs2MZ5AbVYU9kSIftxr5cM6_mGhLuBZaLD3iV1fnJDKjPMbZ7ptJsbtpl5hU-TwUC4QYEqGLX2-EdbtO_E7UI2-p9L6tlyRCkIt0j-6zTewMjO3buZQe8ipWzMjDEwmz1yTZgfxXyxbYoimMaElQyo1xoxzr9bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
من به ایران اعتماد ندارم، چرا؟ مگه فکر می‌کنید به ایران اعتماد دارم؟
من آخرین کسی‌ام که به ایران اعتماد می‌کنه مدام به من دروغ گفتن، الان ما کاملاً کنترل تنگه رو در دست داریم
اونا کنترلش رو ندارند، ما کامل کنترلش می‌کنیم، مال ماست، شاید یه زمانی کاری بکنن و اون‌وقت کارشون تمومه
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20869" target="_blank">📅 08:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20868">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ
:
تهدیدهای زیادی علیه من هست که شما ازشون خبر ندارید
هر رئیس‌جمهور تأثیرگذاری تهدیدهای زیادی دریافت می‌کنه، رئیس‌جمهورهای بی‌اهمیت تهدید نمی‌شند
فکر می‌کنم شاید من تأثیرگذارترین رئیس‌جمهور باشم
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/20868" target="_blank">📅 08:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20867">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترامپ
،
درباره نامزدیش :  دوست دارم دوباره تو سال ۲۰۲۸ نامزد بشم، ولی قانون اجازه نمی‌ده
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/20867" target="_blank">📅 08:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20866">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره اینکه چرا خودش با ایر فورس وان پرواز نکرد ولی خبرنگارا پرواز کردن : نمی‌دونم، اتفاقاً فکر می‌کنم هواپیمایی که من سوار شدم بیشتر در معرض خطر بود
خبرنگار : چرا؟ ترامپ : چون فکر می‌کنم همون هواپیمایی بود که احتمال بیشتری داشت هدف قرار بگیره
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20866" target="_blank">📅 08:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20865">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=uU_8bzRxPach-5ObQ0U2cRfwx5ArERwiXofctXT2PqVDPtmdwxAvx_MRfAzF5CHKw66nxNQQUrPdEFvIJPhG_FSFLccFRRV98a322hIsC8Vv9tDO2O6mOxNcgl0h_1p6ZUzmjslxrsjFCKztjuR61S8_J-S1UOnSpQaJ0B6Yn48WK3CBByi0eV9-7Z0bpMyqx-iaM8J0EeOnBlIj7v5aOF61gMh4KiCYIUSlPMoyzXXCAVMaraZzI_9HJxTT6_KmoK4QzcJCfpmGX2wcqblQ7B7nTb9bmlwPC69R7AXdRzMdvGlyRG_tp4CCr5P4X2L1Ojb1StKCGgG3wp2hxgnrLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edfa0f08c.mp4?token=uU_8bzRxPach-5ObQ0U2cRfwx5ArERwiXofctXT2PqVDPtmdwxAvx_MRfAzF5CHKw66nxNQQUrPdEFvIJPhG_FSFLccFRRV98a322hIsC8Vv9tDO2O6mOxNcgl0h_1p6ZUzmjslxrsjFCKztjuR61S8_J-S1UOnSpQaJ0B6Yn48WK3CBByi0eV9-7Z0bpMyqx-iaM8J0EeOnBlIj7v5aOF61gMh4KiCYIUSlPMoyzXXCAVMaraZzI_9HJxTT6_KmoK4QzcJCfpmGX2wcqblQ7B7nTb9bmlwPC69R7AXdRzMdvGlyRG_tp4CCr5P4X2L1Ojb1StKCGgG3wp2hxgnrLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
:
اوضاع ایران داره عالی پیش میره ما کاملاً کنترل تنگه هرمز رو در دست داریم و نیروی دریایی‌مون فوق‌العاده‌ست
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20865" target="_blank">📅 08:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20864">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">زاکانی : آقا مجتبی داشت تلویزیون میدید یهو تو اخبار شنید رهبر شده
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20864" target="_blank">📅 08:44 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20863">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=OHWQRoyQZhScSpFsMez0EwCR3Z32HvRzrhiPx3Z_GVeDjLu6k7SuFhnnRiEmDvLGKlMF6n_kdgfANqZ9xtFGgkry9y0QAPVFpavU9riJq_Rz7EXYb9rd91yxPMhd6UhjSCDnsLDhSuH3L0bzXJiEviqYxxA_tsQ4CrHOQWpJJGHOweonnIBpruq2EYmB1Ycbj7Dlzvo0aUOMMdjIWtW-H-KbpE9f5SbPht-M-RsEPUIq9nvp-3z6UoN1eJnHA8tVyAEXSMh1LRTYQuP1vOQCzc7vGlRc4_Ip2yVsH1Mc_gKeyZEsFcvL46V6arQt1ebDv3hRVwsUzkvnidIuQdzyyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c87bdfe17b.mp4?token=OHWQRoyQZhScSpFsMez0EwCR3Z32HvRzrhiPx3Z_GVeDjLu6k7SuFhnnRiEmDvLGKlMF6n_kdgfANqZ9xtFGgkry9y0QAPVFpavU9riJq_Rz7EXYb9rd91yxPMhd6UhjSCDnsLDhSuH3L0bzXJiEviqYxxA_tsQ4CrHOQWpJJGHOweonnIBpruq2EYmB1Ycbj7Dlzvo0aUOMMdjIWtW-H-KbpE9f5SbPht-M-RsEPUIq9nvp-3z6UoN1eJnHA8tVyAEXSMh1LRTYQuP1vOQCzc7vGlRc4_Ip2yVsH1Mc_gKeyZEsFcvL46V6arQt1ebDv3hRVwsUzkvnidIuQdzyyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در محل بازی‌های میهن‌پرستانه:  به والدین نگاه می‌کنم، آنها به فرزندانشان بسیار افتخار می‌کنند. و من به گروه افراد حاضر در این اتاق بسیار افتخار می‌کنم. عشق به کشورمان را می‌بینید. کشورمان هرگز بهتر از این نبوده است!
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20863" target="_blank">📅 02:56 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20862">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چیزی نیست رعدنیاهو بود غرب تهران
😂</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20862" target="_blank">📅 02:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20861">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش صدای رعد و برق شدید</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/20861" target="_blank">📅 02:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20859">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بلومبرگ
:
دونالد ترامپ موضع خود را در قبال ایران سخت‌تر کرده است و این امر، امیدها را برای دستیابی به توافقی جهت بازگشایی تنگه هرمز کمرنگ‌تر ساخته است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20859" target="_blank">📅 01:51 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20858">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارش ها از درگیری تمام عیار زمینی میان حوثی های یمن و نیروهای نظامی وابسته به عربستان در شمال یمن.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20858" target="_blank">📅 01:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20857">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آمریکا 2 هزار گیمر رو به‌خاطر تصمیم‌گیری سریع و عملکرد خوب تو شرایط پراسترس ، برای برج مراقبت فرودگاه‌ها استخدام کرده
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20857" target="_blank">📅 01:00 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20856">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=mRzir3BrqEAy9wQJ07jWQxGy6wF1rQbhrc5Bz3Vb-QjIZWT6XVs-5XNlrY5-XVSj2XArh7OYN_Y04-K_py3dXBky_k489_cT_SQeVAOPahqCa_uppux9frsjAwNJVprhcJWfC7JR9Ug4RkYqosU1bzegNBBU8sBDzZ0HBBdqL5aDrmBfG-0I0wLwqFPRqRUgG4LG_2mUpP1tNcK5Qd0SAH6AKB3M0Ia3e4PRVVmIVxhlCQeDx6ivFpicH4zfuMCO0mnkaiWCRoLuAeiEXbvL1HHAMJfX0ucOysYHVCUuZ8ma3ZgRe2eWQZp0h4ypRUrPQ84Gpuw2FUpKSLBk7jyI3nTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ab5e54bb.mp4?token=mRzir3BrqEAy9wQJ07jWQxGy6wF1rQbhrc5Bz3Vb-QjIZWT6XVs-5XNlrY5-XVSj2XArh7OYN_Y04-K_py3dXBky_k489_cT_SQeVAOPahqCa_uppux9frsjAwNJVprhcJWfC7JR9Ug4RkYqosU1bzegNBBU8sBDzZ0HBBdqL5aDrmBfG-0I0wLwqFPRqRUgG4LG_2mUpP1tNcK5Qd0SAH6AKB3M0Ia3e4PRVVmIVxhlCQeDx6ivFpicH4zfuMCO0mnkaiWCRoLuAeiEXbvL1HHAMJfX0ucOysYHVCUuZ8ma3ZgRe2eWQZp0h4ypRUrPQ84Gpuw2FUpKSLBk7jyI3nTZiw8F5FjhTDbo0um2rcOgUAdi8YfS7aBC7fidyLAktHKTIH8M9SA8f9HWm4PkjGiyjcXIUU1HmCoLg3Qj0wSdZw3ROKJXXJ1ZoA0spdQUtpShLvuWFv_CxnFmFvzaYAOAptHGhnR-KLvTsXAuhyZGzNlg9rYJeDkV6Or40qmpteEluuguNlTJtG4E-g6I0bt6WLAH3-Jnq3rB9w2qni7fBs9WWVdMJmN2xqbY1TtRK4njcrr7IQUebRs8KWDvrSajILLhg9HSuHJzU5MHdHrCPEkFNuWs9Qs7vCSolsR84I4-rL2hBEBDRssRT20nZ0YJ0W7D8I4QZXO50VaZ3dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ برای شرکت در رویداد
Freedom 250 Patriot Games
(رقابت‌های میهن‌دوستانه ورزشی ویژه جوانان آمریکایی به مناسبت ۲۵۰مین سالگرد استقلال آمریکا) عازم شهر ژنو در ایالت اوهایو شد و سوار هواپیمای ریاست‌جمهوری
ایرفورس وان
جدید شد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20856" target="_blank">📅 00:24 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20855">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش ها از هدف قرار گرفتن ایست ‌و بازرسی نیروهای نظامی توسط افراد مسلح ناشناس در شهر مرزی خاش در سیستان و باوچستان ، بر اساس گزارشات داخلی 4 نظامی در این حادثه کشته شدند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20855" target="_blank">📅 00:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20854">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محمدرضا نقدی، مشاور فرمانده سپاه، گفت که «این سازمان باید برای انجام عملیات هوشمند در خاک دشمن آماده شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20854" target="_blank">📅 00:04 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20853">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم  @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20853" target="_blank">📅 00:01 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bjp5COqRkAtsKWU1f9Z7gkpRQrA4C1s833ewsv_Y8JMJ0ZnvLttvXXMhUsV837xBob4rS92UU37Je7zyjQ_SOGw7lxd1M_9lpMPhwbIe5HCPO1NhyZv4O9SGAMALGpwQAzve-a5RXRSD1aX9FQwgHFT9mq6oqlNE--fy2p2KYRzsdFzXOG-eHmwp4TlUj9zOJt94iPKW5JITvlbypFdOzS3ArLile7hlcQj2tfz_oGxl2MXT212_NTWuBDtA21NerTZvbNCLrDJYk82JSjQ69BdGAp5X0V5Rf6nhrjovVwQYLx8miLsOwnuoOPLfZi07CfcZWUjU1DZRRzgFi67_gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۴ اسرائیل: مجتبی شش تندرو جدید را برای رهبری جنگ بعدی ایران منصوب می‌کند
با وجود شایعات فزاینده درباره سلامت مجتبی خامنه‌ای، تهران ادعا می‌کند که او شش تندرو از رژیم را برای رهبری جنگ بعدی ایران منصوب کرده است؛ پیامی نگران‌کننده برای اسرائیل و ایالات متحده مبنی بر اینکه رژیم در حال تشدید تنش‌هاست، نه عقب‌نشینی
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20852" target="_blank">📅 23:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">باراک راوید , آکسیوس : امید به توافق میان جمهوری اسلامی و آمریکا در حال محو شدن است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20851" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcRbF1gosaIK6bAO1WLu4eFD6owgCuwLK7ts8ZGc7BgEMy3ht-xThHGEwBXm0mbCPjjoeRp7_XtL982IJg4H4wiXilL9BF2E6afbP7fmIspl_86Zqnwe5N8snbNapGln5UDLyGJewjmbhcwED1-x_0nhxOIHrXswRkywaUFbD_Xmdrzli8XYHCNaDIET2RfPBX1LPztKMLbEsBDQso9A7nNBcj7vbvWofmvFzTzbbYfXNrU_OnlBUT7hCFNEMqfFx8Rbi6kI0d1WcshGuGgKnDOjI8nXuDmA5QxCKrSof1vnnoliGB2Hm6N7WFf3wfBpf3-quZS12At11A532WrCTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد نیروهای آمریکایی امروز کشتی باری «ولا نوا» با پرچم پاناما را هنگام حرکت به سمت یکی از بنادر ایران در خلیج عمان متوقف کردند. پس از بی‌توجهی خدمه به هشدارهای آمریکا، یک بالگرد MH-60 دو موشک هل فایر به اتاق موتور کشتی شلیک کرد و سامانه هدایت آن را از کار انداخت. سنتکام گفت تا ۱۱ اوت، ۵۵ کشتی تجاری را تغییر مسیر داده، ۳ کشتی را از کار انداخته و ۲ کشتی را سوار و بازرسی کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20850" target="_blank">📅 22:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA B</strong></div>
<div class="tg-text">یاشاار
جون هرکی دوست داری زارتان زورتان و حذف نکن از ادبیاتت
من هم توهمی دهنم سرویس شده
از وقتی نمیگی برکت از جنگ رفت
🤣
خداییش جدی میگم</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20849" target="_blank">📅 22:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سازمان دریایی بریتانیا: فعالیت‌های سپاه در تنگه هرمز در طول 48 ساعت گذشته ادامه داشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20848" target="_blank">📅 22:11 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دونالد ترامپ در چارچوب قانون اختیارات جنگ آمریکا (War Powers Resolution)، با ارسال نامه‌ای به کنگره که ۱۹ تیر ۱۴۰۵ امضا و ۲۲ تیر ۱۴۰۵ به‌طور رسمی اعلام شد، از ازسرگیری عملیات نظامی علیه ایران خبر داد. با این اقدام، مهلت قانونی ۶۰ روزه برای ادامه عملیات نظامی بدون مجوز جدید کنگره آغاز شد. این اقدام به معنای صدور مجوز جنگ از سوی کنگره نیست، بلکه صرفاً روند قانونی اطلاع‌رسانی به کنگره و آغاز مهلت ۶۰ روزه را فعال می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20847" target="_blank">📅 21:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20846" target="_blank">📅 21:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">من با دیتا های اپن سورس تحلیل میکنم پیشگو که نیستم ! هیچ تاریخی هم نمیدم فقط احتمالاته اگه انقدر حساسی  پس از الان رو نزدن حساب کن  ! اگه حرفه ای هستی پس ویس هارو گوش کردی کامل روحیات منم میدونی و دیگه سوألی هم نداری که هی داریکت بدی</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20845" target="_blank">📅 21:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20844" target="_blank">📅 21:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSajad Mousavi</strong></div>
<div class="tg-text">به نظرت قطعی شنبه میزنه من میخوام با بچه ها شرط ببندم</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20843" target="_blank">📅 21:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20842">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20842" target="_blank">📅 21:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20841">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش ۲ ‌انفجار یا پرتاب موشک/پهپاد از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20841" target="_blank">📅 20:48 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20840">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ اعلام کرد که رابرت گیلمن، سرباز سابق نیروی دریایی ایالات متحده که در سال ۲۰۲۲ در روسیه زندانی شده بود، پس از گفتگوها با ولادیمیر پوتین، آزاد شده و به ایالات متحده بازمی‌گردد.
ترامپ گفت که روسیه موافقت کرده است گیلمن را بر اساس «ملاحظات انسان‌دوستانه» آزاد کند و «هیچ مبادله‌ای انجام نشده است».
ترامپ همچنین گفت که اولین درخواست گیلمن یک «همبرگر عالی» بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20840" target="_blank">📅 20:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ : ما بر پول ایران کنترل داریم و کنترل کاملی بر آن اعمال می کنیم
ترامپ : سلاح و جنگنده به اروپا می‌فروشیم و آن‌ها در ارسال به اوکراین آزادند
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20839" target="_blank">📅 20:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20838">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسرائیل و ونزوئلا پس از ۱۷ سال قطع روابط دیپلماتیک، توافق کردند که روابط کنسولی خود را از سر بگیرند و یک کانال هماهنگی رسمی ایجاد کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20838" target="_blank">📅 20:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/797367122e.mp4?token=sKCO6iIUlEATnJPg0SBweSKUBE682M3nz3E92i1RcNEpgxLWWALMCa5ZbfQRyD4njKJZHl-81EA0V1ewV2F_vSiruKA4kJSzwH7ur7JSDYzmXxAF7akx7dqqY4ErP3Qv70hPqZKcBQcEd4u4AZERofTiqoSmvbSf74H9ayWuNbxyd0SoQgz1Fa-RMC6COLdvKqWeRO146NpLvZ3Ws6dMy9Ks19j9jvF_GnGUw0_wpdJkRd75gvzIjkbohzMwnzPWj8S3Dn4SlECf-Y22GHSjWe5glALPUSbljqbKwtzxXKolUPQhhbmIE15xXsclIVAclCT22IlH6ySAJ_SJFgXsoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/797367122e.mp4?token=sKCO6iIUlEATnJPg0SBweSKUBE682M3nz3E92i1RcNEpgxLWWALMCa5ZbfQRyD4njKJZHl-81EA0V1ewV2F_vSiruKA4kJSzwH7ur7JSDYzmXxAF7akx7dqqY4ErP3Qv70hPqZKcBQcEd4u4AZERofTiqoSmvbSf74H9ayWuNbxyd0SoQgz1Fa-RMC6COLdvKqWeRO146NpLvZ3Ws6dMy9Ks19j9jvF_GnGUw0_wpdJkRd75gvzIjkbohzMwnzPWj8S3Dn4SlECf-Y22GHSjWe5glALPUSbljqbKwtzxXKolUPQhhbmIE15xXsclIVAclCT22IlH6ySAJ_SJFgXsoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز بالگرد آپاچی ۶۴ آمریکایی در نزدیکی قشم
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20837" target="_blank">📅 20:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20836">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">رسایی : چونکه نمیدانیم اسرائیل کِی حمله میکند مجبوریم جلسات مجلس را مجازی کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20836" target="_blank">📅 20:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20835">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پست قبلی بی بی پاک شد این پست کارای اداری رو انجام بدید
https://www.instagram.com/reel/Db6BHf7MYhi/?comment_id=17896725462373851</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20835" target="_blank">📅 20:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20833">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو : جولان سرزمین ماست و برای همیشه متعلق به اسرائیل خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20833" target="_blank">📅 18:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20832">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دونالد ترامپ: ایالات متحده می‌تواند بزودی و با قدرت بسیار زیاد به ایران حمله کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20832" target="_blank">📅 18:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20831">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یوآو کیش، وزیر آموزش اسرائیل:
صرف نظر از اینکه رئیس جمهور آمریکا چه کسی باشد، حتی پس از ترامپ,  اگر لازم باشد به تنهایی اقدام کنیم، به تنهایی اقدام خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20831" target="_blank">📅 17:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2XzjFpB_YPCjhDElcqXw5f7VN3CRBmRqSVwchkbLwNYG2_mbDXoPFk8bnUYzKJgZedcB4-MWCTe0u3e4qE-3ZASjSSJEYw2_aIpQBBKpRPN04bBHBj98murc60rMdF5FynaMbA5jSLh3JHtDY5KMRbqkSuAkLCU_nfJIZ4ZvTXKkxsPqbX6RQdTqdACg53IW_6_VJf-WkNEUud3qwyQwzIHMGG1clqWnAZzWKvuBAAWNhQQHXYpvVi4f5pxB4Dm06jKSDMBJo2gox6qTNlCnDgkBX1acQ30AQL0Xz3rSv93Ib6RkqBvvcqiVx7P-hcKYXHVNyjPOq4KoU5ghSXbRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه اسرائیل : ترکیه این جسارت را دارد که از اسرائیل انتقاد کند؛ اما واقعیت‌های میدانی چیست؟ هزاران سرباز ترکیه و ده‌ها پایگاه و موضع نظامی در سوریه، عراق و قبرس مستقر هستند. در حالی که تجاوز نظامی اردوغان مرزی نمی‌شناسد، ترکیه ۳۶ درصد از خاک قبرس، ۵ درصد از خاک سوریه و ۲ هزار کیلومتر مربع از خاک عراق را در اشغال خود دارد. در مقابل، اسرائیل به‌طور موقت تنها ۰.۱ درصد از خاک سوریه را در اختیار دارد؛ منطقه‌ای حائل که به گفته اسرائیل، برای حفاظت از شهروندانش در برابر تهدیدهای امنیتی اثبات‌شده ایجاد شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20830" target="_blank">📅 17:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به گزارش رسانه‌های اسرائیلی،
یوسی کوهن، رئیس پیشین موساد در نشست «مجمع جلیل» در شهر صفد گفت: «ما بارها از سایت هسته‌ای فردو بازدید کردیم تا این سایت را درک و شناسایی کنیم.»
او مشخص نکرد که این بازدیدها چه زمانی انجام شده یا دقیقا چه کسانی از این سایت بازدید کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20829" target="_blank">📅 17:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20823">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20823" target="_blank">📅 16:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20822">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsjQ1Lhl6ipfdjNhJZwYBGu8J9Y59ttJ2DjlfURp0taXNGkQL8X1xUIB_xWr7ZLfJhqu_6vigX4nAA7LlnaoTYXCanbJxcSCMzvDdiHot7oV3HpxwC3yqZ1rp17x1VK-CPEmDw4kzu0cGAOatv0tAdPIe7CtCNtHayLGRvB3knS19iaxWkRyqaYA-iRL6tFGqbj9eFU3IudJO_9DHIQV6XjPKFaDwVBnJ7URTI7eGP_jMurUtymxb8BDVnE0NlwToSbTbJIcDPnsDrb8v3_UJr1IBrAaCFlBY5PdOjr10wGIRFXXoiOtrf5mNJFZdquXsqkTrApmZL6wp3o7KaBZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی بی دوزندهیاهو : آتش‌سوزی در کارخانه نخ اطراف بیدگنه،  ملارد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20822" target="_blank">📅 16:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20821">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دبیر شورای عالی امنیت ملی ج.ا : ما در یکی از حساس‌ترین و سرنوشت‌سازترین مراحل تاریخ معاصر خود قرار داریم , در برابر تهدیدها، از حقوق خود و منافع ملت‌مان عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20821" target="_blank">📅 16:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20820">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه. @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20820" target="_blank">📅 16:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وال استریت ژورنال : نیروهای آمریکایی امروز به سمت یه کشتی که با پرچم پاناما حرکت می‌کرده، شلیک کردن. ظاهراً این کشتی قصد داشته محاصره بنادر ایران توسط آمریکا رو نقض کنه.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20819" target="_blank">📅 16:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر دفاع پاکستان به بلومبرگ:
نشانه‌های روزهای گذشته حاکی از آن است که به توافق صلح (یاشار: بمباران) نزدیک می‌شویم
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/20818" target="_blank">📅 16:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">روال هر روز پیج اینستاگرام در ۴ دقیقه ریکاوری شد
😁
عرضشی عر بزن
🤣</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20817" target="_blank">📅 16:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس
:
به گفته مقام‌های آمریکایی و اسرائیلی، دولت دونالد ترامپ در پشت‌پرده میان سوریه، اسرائیل و آژانس بین‌المللی انرژی اتمی برای خارج کردن مواد هسته‌ای از «سایت ۹۹» سوریه، مرتبط با برنامه هسته‌ای مخفی حکومت بشار اسد، توافق ایجاد کرد. این مواد شامل «کیک زرد» است که برای ساخت سلاح هسته‌ای کافی نیست، اما می‌تواند در بمب‌های رادیولوژیک به کار رود. اسرائیل پس از سقوط اسد با نگرانی از دسترسی به این مواد، ورودی‌های سایت را هدف قرار داده بود. عملیات انتقال هنوز انجام نشده، اما مقام‌های آمریکایی می‌گویند به‌زودی اجرا خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20816" target="_blank">📅 15:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">وال‌استریت ژورنال : خامنه‌ای با تغییر مقام‌های ارشد امنیتی بر ادامه تقابل با آمریکا تاکید دارد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20815" target="_blank">📅 15:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش حمله موشکی به اردوگاه گروه‌های کورد در شمال شرقی اربیل
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20814" target="_blank">📅 15:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FX3hOc1hRVhiZp6iF2y5TGp0m0Gh7DcYgK0by7fno4dKClw77Dv1zgR283kxLoLwywkT7Y9olh8uOZJ2QWKGpz8B9QLtV-hgbjXMoU7qwiU-kMmfJuj-I0vtZOA6LQcfyiEQrKobUEaQ-JpmmK5IPO7aDpD0ncAnq1wcz1Or7KIehnolMhSpXQKVrAtC0HRjYMxwaLVs6UbfU4_RKokJ-RwUL-rogBNX3rbaBOCY5D12lK_iD29Zl_fi1ecnE-FDVrg4cDhkYhnmxGgLfo6CjTKkGyFdeCCKaGmwiBUbN-ItZE0hcOIL3BNL0ZHSs5Y_8avR-8drR1F-OH6eaHnUyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش خبرگزاری رویترز، سازمان حمل و نقل دریایی بریتانیا (UKMTO) از حادثه‌ای در سواحل المخا، یمن مطلع شده است. گزارش شده است که یک کشتی باری در دریای سرخ جنوبی مورد اصابت یک موشک/پهپاد ناشناخته قرار گرفته و منجر به تلفات جانی شده است ، این در حالی است که یک کشتی سعودی صبح امروز مورد هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20813" target="_blank">📅 14:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سید محسن رضا نقوی، وزیر کشور پاکستان برای گفتگو با مقامات ایرانی وارد تهران شد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20812" target="_blank">📅 14:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رسانه عبری : مجتبی خامنه‌ای، از احمد وحیدی، فرمانده کل سپاه پاسداران، خواست تا برای «عملیات تهاجمی قدرتمند علیه دشمن» آماده شود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20811" target="_blank">📅 13:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره ایران: ما سه راهبرد داریم , همین کاری را که الان انجام می‌دهیم ادامه دهیم؛ فقط به همین شکل پیش برویم و ببینیم اوضاعشان چقدر بد است، چون تورمشان ۳۰۰ درصد است. پولشان تقریباً هیچ ارزشی ندارد. حقوق سربازانشان را نمی‌دهند. سربازانشان در حال ترک خدمت هستند. بنابراین همین روند را ادامه دهیم، چون این وضعیت پایدار نیست.
خیلی، خیلی سخت به آنها ضربه بزنیم؛ یا در واقع، راه سوم این است که از نظر اقتصادی آنها را شکست دهیم. البته همین کار را همین حالا هم انجام می‌دهیم. این تا حدی بخشی از راهبرد اول است.
بنابراین از نظر اقتصادی، آنها در وضعیت بسیار بدی قرار دارند. نمی‌توانند پول قرض بگیرند. ما کنترل پول آنها، یعنی آنچه در اختیار داشتند، را در دست داریم؛ و مقدار آن هم زیاد است. آنها پول زیادی داشتند و ما کنترل کامل آن را در اختیار داریم.
من بانکدار آنها هستم. من بانکدار آنها هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20810" target="_blank">📅 13:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ : می‌خواهید یک گورستان پرندگان را ببینید؟ گاهی اوقات به زیر یک آسیاب بادی بروید و هزاران پرنده مرده خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20809" target="_blank">📅 13:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">جورسلیم پست : ترامپ از حمله گسترده دیگری به ایران خودداری کرد ، با این امید که فشار اقتصادی بیشتر می‌تواند تهران را مجبور به تسلیم کند، بدون اینکه منجر به یک جنگ منطقه‌ای گسترده‌تر شود.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20808" target="_blank">📅 13:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcJxtVSBpVpxctj76Hy7dSk5wQ-sz3xJEbI3XU7jg-lOQIe1lfPjvV6MeKD91QmLtmlS1kc-Nl_O_hKE0344LW4qjtcyNmBVpmZRCA0bDU5BVqFR0fBaTa0Lvp7xJtWKo8cJ-aOSZHzlaG8WUKcHb3OYmpnUrukulESOfyjkr9sCebDAihBL-KNEfi36stnTWpsfbJ6R-0G5FQz0HkV5z7Qo18Vq4l5Dgn9ib-ogKEOEENn6CBA-F3Dl-8rCys9a43BWHgFqCj2nmTs63ExA90qcHoDLePEXNLeWrFmb4rj276PASXsUBaXZPPcJWDjk9-Rajyw0a76BJ-AQL16Reg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) گزارشی درباره وقوع حادثه‌ای برای یک نفتکش و نیروهای نظامی در خلیج عمان دریافت کرده است. مقام‌های مربوطه در جریان این حادثه هستند و تحقیقات مرتبط همچنان ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20807" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaiyYB0Iy0DnIxnOH3QDLb_c7Fsf275CnHc8i-eJ2ZJI3of3UGLiqouBlxBNTeOInTxw1sY9zXSaPwYQsJZ4-BwxFI0Waca6d_c12KvPISzegKG5AiKHGe1M8QW73tEU6BZbR_TSW7Iv4E8CkevT8AcmAmezM1lD_CPskkStLYyVqgC8LzsRv30llA3GvVjHdnOhmVldsrpkx2wKU7ubU_S9axWE-ZSZJIQdZv9i263_Zgv-BfvbWKsCeG3zh7MbxtvSGKxLBZTYUAd4VKDNVppkVYkrRawlPntU_FMsWpXEcExlkF2ZYiILLMwjK7KiIyBee0BBavkj8f1PrHGPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان KC-46A پگاسوس نیروی هوایی آمریکا از پایگاه‌های مبدأ خود در غرب ایالات متحده به پایگاه هوایی مک‌دیل در فلوریدا، در شرق آمریکا، منتقل شده‌اند؛ جابه‌جایی‌ای که می‌تواند نشانه‌ای از آماده‌سازی برای اعزام قریب‌الوقوع شماری از هواپیماهای…</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20806" target="_blank">📅 12:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دادگاه جنایی دمشق حکم اعدام برای بشار اسد صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20805" target="_blank">📅 12:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">https://www.instagram.com/reel/Db5HBuLozsg/?igsh=ajBqMW82djZrZW96
استوری که درخواست زیاد داشتید رو به صورت تریال پست کردم</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20804" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشهای رسانه های‌عربی حاکی از کشته شدن ۳ نفر در پی حمله حوثی ها به یک کشتی در تنگه باب المندب است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20803" target="_blank">📅 10:41 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGi9_MK8njr1IkePB0yBstbXg39_wuWllQL4HjI62s7JZcExgg5LgMk0gOcgekwF1I2N1mM0QqbjmNxOliIr71QIcXaZgI2Z_M2XbLpIDXPVT9fhv9Xex7nCMBEkyrG5MC5qInXMRHbpFBYSUIHO9_G0hpRknLlau78Jhrmp8kKOYM6mbcG2-B4sRTPUel44ZWHquiuSpIAXWhvdp7At7wOrYSs3p0DZg4Mv369jp8rPhAf5hm4EmI8dmLF4P1Y_wXSSU8-y18PMIOmoHxJCpoeNdOP7evH_Nextsm2WIAkhBKZVAp30ySgffLOlUACuh85wH-9P-1q_6JrDbU3UfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برای عبرو از ۹۰$ خیز برداشت
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/20802" target="_blank">📅 10:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع. @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20801" target="_blank">📅 10:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند ‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند.…</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20800" target="_blank">📅 10:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏رییس اتاق بازرگانی ایران و چین با تاکید بر لزوم پایان محاصره دریایی بنادر جنوبی ایران گفت : «چه با مذاکره،
چه با خواهش
، چه با تهدید و چه با جنگ باید این محاصره دریایی خاتمه یابد» و افزود: «تبعات محاصره از جنگ هم بیشتر است.»
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20799" target="_blank">📅 10:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رویترز: تعداد کشتی‌هایی که از تنگه هرمز عبور می‌کنند، به ۶ فروند در روز دوشنبه کاهش یافته است، در حالی که میانگین این تعداد در ۱۰ روز گذشته حدود ۱۱ فروند بوده است. این کاهش در حالی رخ می‌دهد که امیدها برای دستیابی به توافقی بین واشنگتن و تهران رو به کاهش است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20798" target="_blank">📅 10:06 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: ما بر اساس سه سناریو با ایران عمل می‌کنیم: اول، نظارت بر وضعیت نامناسب آن؛ دوم، اعمال فشار اقتصادی؛ و سوم، حمله نظامی قاطع.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20797" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=tKlvivnetd3ifiwWQozXScp2Or2ms8yilZFIqLTwBBJMFWAOiCjO3qBZzwBpzZm8TGnWs8paKSrVXgtJgOfCRN9nT7CYfsLkReugdqutf_TM-JHFy8KhLPz7jj6TrFXVOndFhloreKcBBznraqXd7K0abpHhYmrEZ2Wn-TW9_6gMta79u9iJAgE3zQ5UJaWPiwnsdbqDCfGd34uO6lqEmrcQP_sXJUNFgEb9AYawtvxC5zs3_bG5c2iGMNaHBZte0mg5E9UZD_MuI_Vh04CtMhU7Ke8_2suctyALOyMQhEF43LHmnIPxke9mMwzt-zod9l7lNgQjJmmbS3DEz5XX0y6W1XATvAWpBnkM3okOSqPjrC1moajPNz7XUJJXh3uFfDEOzG5Vmn6hBrjPMcNcjocc4ck9kaDHT6IV9ZVmnSbHgPgexgHeiSRxY5O2X8U5Hih2Z3kq-dh2BrCVX-0kiCZc42qOa3gZseOwKj_5AnT5EX4Dc7AsroJd0bk2h-7-lDV-vRfdNVs1z1Q8gKg7a-_LYMmoooNKpk7U7oDH9VKHBc10swsYHZLUnlRe1Gi6VfpSl4NdtXJ7YRbv1BD_vAQCTKdj7VMNCOBch5aqL6U86EIGX-dyW6TgSH4Fgp2vH5pNEPJxcUSDFFWk_PfRCzAokF56n-svVMdtXObyZA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bdb30a06.mp4?token=tKlvivnetd3ifiwWQozXScp2Or2ms8yilZFIqLTwBBJMFWAOiCjO3qBZzwBpzZm8TGnWs8paKSrVXgtJgOfCRN9nT7CYfsLkReugdqutf_TM-JHFy8KhLPz7jj6TrFXVOndFhloreKcBBznraqXd7K0abpHhYmrEZ2Wn-TW9_6gMta79u9iJAgE3zQ5UJaWPiwnsdbqDCfGd34uO6lqEmrcQP_sXJUNFgEb9AYawtvxC5zs3_bG5c2iGMNaHBZte0mg5E9UZD_MuI_Vh04CtMhU7Ke8_2suctyALOyMQhEF43LHmnIPxke9mMwzt-zod9l7lNgQjJmmbS3DEz5XX0y6W1XATvAWpBnkM3okOSqPjrC1moajPNz7XUJJXh3uFfDEOzG5Vmn6hBrjPMcNcjocc4ck9kaDHT6IV9ZVmnSbHgPgexgHeiSRxY5O2X8U5Hih2Z3kq-dh2BrCVX-0kiCZc42qOa3gZseOwKj_5AnT5EX4Dc7AsroJd0bk2h-7-lDV-vRfdNVs1z1Q8gKg7a-_LYMmoooNKpk7U7oDH9VKHBc10swsYHZLUnlRe1Gi6VfpSl4NdtXJ7YRbv1BD_vAQCTKdj7VMNCOBch5aqL6U86EIGX-dyW6TgSH4Fgp2vH5pNEPJxcUSDFFWk_PfRCzAokF56n-svVMdtXObyZA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واشنگتن پست:
در پی تهدید به ترور از سوی ایران، دونالد ترامپ هنگام ترک نشست ناتو در آنکارا، ابتدا مقابل دوربین‌ها سوار هواپیمای قدیمی «ایر فورس وان» (بوئینگ ۷۴۷) شد، اما سپس به‌صورت محرمانه به یک فروند هواپیمای ‌کوچکتر
C-32A
منتقل شد. در همین حال،
هواپیمای قدیمی ۷۴۷
به‌عنوان هواپیمای فریب با شناسه «ایر فورس وان» به پرواز ادامه داد و خبرنگاران و حتی برخی کارکنان کاخ سفید تصور می‌کردند ترامپ داخل آن است.
در ویدئویی که از این عملیات منتشر شده، ادعا می‌شود
انتقال ترامپ با استفاده از یک کامیون خدمات فرودگاهی، احتمالاً کامیون حمل پول آرمور(زره ای) ، انجام شده است. این در حالی است که
هواپیمای
ایر فرس وان
جدید ۷۴۷-۸ اهدایی قطر
، هواپیمای رسمی جدید رئیس‌جمهور آمریکا محسوب می‌شود و با آن به آنکارا آماده بود و در این سفر، نخستین مأموریت خارجی را انجام داده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20796" target="_blank">📅 09:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyHF6z0LrixYxY_iMiu750n3GpQMKPqz72ySNjNK7dgRlqj4DSiFnHuVRqOIb0LZPCNXdctPKkdvYOQK3cX9EroRW9s9F62wiyAMWQeO5U-VDFiT58uhhnAVwh8fr32nznUuG9ArNG76OwtCEMTsnhxlHKOWPgLGU5pOFCC1KmvxqUa_FePyf4H9VSYVkcrJQYsrzwkI-z1-V8WSGYcFddck2bAvqGcGY-ZAv-oHl7PGXc5tSOLnIxh0Qz-HyojeMUm-YlWMCf2coYH2BNE-wbmuj7bGzGL8LBeB6KfwyF6fKphr4juFVworweY01qiQvfdzQ1TBrKq5jXbwbXjK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ آخر هفته را در زمین گلف خود در بدمنستر سپری کرد؛ در حالی که یک سامانه پدافند هوایی کوتاه‌برد
AN/TWQ-1 Avenger SHORAD
نیز در محل مستقر بود.
(سامانه AN/TWQ-1 Avenger SHORAD:
یک سامانه پدافند هوایی کوتاه‌برد آمریکایی است که روی خودروی هاموی نصب می‌شود و مأموریت آن حفاظت از افراد و تأسیسات در برابر تهدیدات ارتفاع پایین است. این سامانه معمولاً به ۸ موشک دوش‌پرتاب
استینگر (FIM-92 Stinger)
، یک تیربار ۱۲.۷ میلی‌متری و سامانه‌های دید حرارتی و هدف‌گیری مجهز است و برای مقابله با پهپادها، بالگردها، هواپیماهای ارتفاع پایین و برخی موشک‌های کروز به‌کار می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20795" target="_blank">📅 02:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ادعای وال استریت جورنال : مسئولان ارشد دولت و کاخ سفید به ترامپ توصیه کرده‌اند که تشدید تحریم‌های فعلی و اعمال تحریم‌های جدید علیه ایران، ممکن است موثرترین راه برای وادار کردن این رژیم به تسلیم باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20794" target="_blank">📅 02:04 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=snCKqq3ucLeMXD1FqYtmR41WDGylj-JWykvG1vf1xt9RzlmZ-yO3ZlqH6NJCNKgdOT3VmqQ20YLhr0fkxovka2uxEzNnvifAOljFpXYsPjmllGdui_Go3YIvuVt_SV1Z-TknbXMob9s1aSYzzDPaVyIa5THmaDEqIHoEDB_uCKLuUjbLiHRRlYgSTTemPfLPUPdEGc18EAtDFDRh6hbtFPT9hU0hpIDlibZ5QqaEVlNfRLp1HrM29y-TwoVx7hoCGO75DINFyXoKCfyhIXgOt6t_8IhMTmtkDKB6U9u0VXpCENeXBFe6Eo90YSwtTejn6b7vYo3tcVcJ8Q6sKJq8_7OLxTJ8TFT5sIdv7QT4ffJgOGyqQdDSx4o0hHW1AKJ_RqB9tQXVT0YEOxWx_cL1G19Zoc2OcpBZoBNUMmVwJBHu8s8ficTMH9C9k2tp60F_yyH5CL4GE63DvVc6-uvvZCzO-8CWajBUDyLfgqgBzVAzcSn2L_zGkB_vvmPjnhjbyAsi4TwrfH_Iz3oJJOdJ7Eh8HfUhCiDxHcCGFwUPyuDJ7BXseoVGyv5mxoCdHeUCXYF1AvhJGIjPe3drFH24_dQ4qmmZVqvI2Clt2z7FYoHWYQeBTDunZdwLompzcK3QfGdiPNLz6FUmppON057daUCfe0RTt1uqpRXZ9mTjRME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1faa6dd22c.mp4?token=snCKqq3ucLeMXD1FqYtmR41WDGylj-JWykvG1vf1xt9RzlmZ-yO3ZlqH6NJCNKgdOT3VmqQ20YLhr0fkxovka2uxEzNnvifAOljFpXYsPjmllGdui_Go3YIvuVt_SV1Z-TknbXMob9s1aSYzzDPaVyIa5THmaDEqIHoEDB_uCKLuUjbLiHRRlYgSTTemPfLPUPdEGc18EAtDFDRh6hbtFPT9hU0hpIDlibZ5QqaEVlNfRLp1HrM29y-TwoVx7hoCGO75DINFyXoKCfyhIXgOt6t_8IhMTmtkDKB6U9u0VXpCENeXBFe6Eo90YSwtTejn6b7vYo3tcVcJ8Q6sKJq8_7OLxTJ8TFT5sIdv7QT4ffJgOGyqQdDSx4o0hHW1AKJ_RqB9tQXVT0YEOxWx_cL1G19Zoc2OcpBZoBNUMmVwJBHu8s8ficTMH9C9k2tp60F_yyH5CL4GE63DvVc6-uvvZCzO-8CWajBUDyLfgqgBzVAzcSn2L_zGkB_vvmPjnhjbyAsi4TwrfH_Iz3oJJOdJ7Eh8HfUhCiDxHcCGFwUPyuDJ7BXseoVGyv5mxoCdHeUCXYF1AvhJGIjPe3drFH24_dQ4qmmZVqvI2Clt2z7FYoHWYQeBTDunZdwLompzcK3QfGdiPNLz6FUmppON057daUCfe0RTt1uqpRXZ9mTjRME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏تام کاتن در برنامه مارک لوین در فاکس‌نیوز: مردم ایران باید آزادی و سرنوشت خود را پس بگیرند
‏سناتور تام کاتن با تأکید بر حمایت آمریکا از نیروهای آزادی‌خواه گفت مردم ایران نخستین و بزرگ‌ترین قربانیان حاکمان رژیم جمهوری اسلامی هستند و شایسته آینده‌ای بسیار بهترند. او گفت: «همان‌طور که رونالد ریگان در قرن گذشته در برابر کمونیسم شوروی ایستاد، ما نیز باید همواره در کنار نیروها و دوستان آزادی بایستیم؛ چه دولتی طرفدار آمریکا در برابر شورشی ضدآمریکایی باشد و چه مبارزان آزادی‌خواهی که برای رهایی از دیکتاتوری‌های کمونیستی یا اسلامی تلاش می‌کنند. همان‌طور که پرزیدنت ترامپ اوایل امسال بارها گفت، کمک در راه بود و مردم ایران باید آزادی و سرنوشت خود را دوباره به دست بگیرند. اگر مردم ایران به آینده‌ای بهتر دست یابند، آمریکا امن‌تر و جهان نیز امن‌تر و صلح‌آمیزتر خواهد شد.»
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/20793" target="_blank">📅 01:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBT4Qn3daN3fjFx-hlHRCFlfJUwfrJPE8IMjl7VKHZV0_UhVXjD2DXGaqCbtgbGrZ5Bk2GmREoieqJvBJR-crmUWVvK8wue8pFr15fYoa9D6XvgAGlyEGcTgw34poNIyMBUG_n9JF3Kgr2eYAIREGEPjtr_7XlU6mC7eEAM15F6GvQyhUS50QqYeajDghF9kIBo7Bgha2PRBQ6aZfFkxK4THdLKiTeqMb0ySzEF8N5Ym37Mwvj9b7kssQXLXMipBJvrTgt_xGIc-G0OPi9QMkaSo5XDctdAsNaN7IbLSz_uOCpdhimXyZWWnOFwlbeMbcb3VhHnt1vYHa0VXYUsnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیش از ۱۵ نفتکش مرتبط با عربستان، که بیشترشان نفتکش‌های بسیار بزرگ و خالی هستند، در حال حرکت به سمت خلیج فارس هستند.
ترامپ همچنین امشب اعلام کرد که تنگه هرمز کاملاً مین‌روبی شده است. باید ببینیم میتوانند عبور کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/20792" target="_blank">📅 01:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اتاق جنگ با یاشار : کنگره آمریکا در تعطیلات تابستانی قرار گرفت.
سنا از ۸ اوت ۲۰۲۶ تا ۱۴ سپتامبر ۲۰۲۶
عملاً در تعطیلات است و جلسه عادی بعدی آن
۱۴ سپتامبر (۲۳ شهریور)
خواهد بود. مجلس نمایندگان زودتر برمی‌گردد و
۳۱ اوت (۹ شهریور)
رأی‌گیری‌های عادی را از سر می‌گیرد.
حالا اگر آمریکا در این فاصله به ایران حمله کند، تعطیلی کنگره از یک جهت می‌تواند برای دولت ترامپ یک مزیت سیاسی ایجاد کند:
ترامپ همچنان فرمانده کل است و تعطیلی کنگره به‌خودی‌خود مانع دستور حمله نمی‌شود؛ اما نمایندگان و سناتورها برای تصویب قطعنامه، محدود کردن بودجه یا اعمال فشار فوری علیه عملیات نظامی، امکان بسیار کمتری برای اقدام سریع دارند
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/20791" target="_blank">📅 00:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پرتاب موشک/پهپاد از سیریک
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20790" target="_blank">📅 00:45 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
