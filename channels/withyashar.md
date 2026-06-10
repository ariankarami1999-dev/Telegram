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
<img src="https://cdn4.telesco.pe/file/FndBMVPKIZfOBegxH5jLnafjadZaEVRrJev0Lm217Ei9x8ZL97LI4ptgU5a2VOMcbyQ4FRNQPkr-0BnIpV129S33EcTtI76vipQah_C4IzEihKFqZOq_e_BSUZUzw5nyKHVHgs5W0l_JF2DQSThElX2jpwl5Hu_B5id_npnenOp5Hv_W63hQ9GzmaX8hjfhPZ6lwNJt71EuOS3pjsT2ubGVd9TbsWxb7RvDEfI8md1s1LBhJYJc5QA72yJKBzITEeYZuH8V9E3UkXAjENmYlTLVI6cdR67l5ELR4MwGI6wSd3FAxQeirKRkZg0waxFObmbJCBDskiVO9x_571XCX-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 314K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 23:44:16</div>
<hr>

<div class="tg-post" id="msg-14378">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ :
به همه پیشنهاد میکنم امشب تلویزیون رو روشن کنن ( یک ساعت و نیم دیگه )
@withyashar</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/withyashar/14378" target="_blank">📅 23:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14377">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">استرالیا و کانادا از همه شهروندان خود در ایران خواسته‌اند فوراً کشور را ترک کنند.
@withyashar</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/withyashar/14377" target="_blank">📅 23:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14376">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رسانه های اسراییل : ترامپ خبر از حمله بزرگ طی ساعات آینده به ایران داده است ٫ ارتش اسراییل اماده شده
@withyashar</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/14376" target="_blank">📅 23:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14375">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش صدای انفجار از نجف‌آباد اصفهان
🚨
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/14375" target="_blank">📅 23:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14374">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">24 ساعت دیگه بازی افتتاحیه جام جهانی شروع میشه
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/14374" target="_blank">📅 23:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14373">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جواد خیابانی پس از ۳۵ سال فعالیت مستمر در سازمان صداوسیما بازنشسته شد
@withyashar</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/14373" target="_blank">📅 23:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14372">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">میانجیگر قطری هم تهران رو ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/14372" target="_blank">📅 23:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14371">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
طی ساعات آتی احتمال شعله‌ور شون جنگ بزرگ وجود دارد
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/14371" target="_blank">📅 23:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14370">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">باراک راوید: ممکنه مذاکرات ظرف ۲ تا ۳ ساعت آینده به فروپاشی کامل برسه!
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14370" target="_blank">📅 22:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14369">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امروز دو فروند هواپیمای گشت دریایی P-8A Poseidon متعلق به نیروی دریایی آمریکا از پایگاه هوایی سیگونلا (NAS Sigonella) به سمت شرق پرواز کردند؛ مسیری که احتمالاً به خاورمیانه یا شاخ آفریقا منتهی می‌شود. اگرچه این جابه‌جایی به‌خودی‌خود قابل توجه بود، اما آنچه توجه علاقه‌مندان به ردیابی پرواز را جلب کرد این بود که یکی از این هواپیماها به نظر می‌رسید کد هگز ICAO متعلق به یک بمب‌افکن B-52 نیروی هوایی آمریکا را ارسال می‌کند.
این ناهنجاری به‌سرعت باعث گمانه‌زنی‌هایی در فضای آنلاین شد مبنی بر اینکه یک B-52 استراتوفورترس از سیسیل به پرواز درآمده است. با این حال، شواهد موجود نشان می‌دهد که هیچ B-52 از سیگونلا عملیات نداشته و هواپیمای مورد نظر در واقع یک P-8A بوده است.
هواپیماهای نظامی گاهی به دلایل فنی، عملیاتی یا اداری داده‌های شناسایی غیرمعمولی ارسال می‌کنند. در برخی موارد، تنظیمات ترانسپوندر ممکن است اشتباه باشد؛ در موارد دیگر، آزمایش‌ها یا فعالیت‌های تعمیر و نگهداری می‌تواند منجر به ارسال داده‌های غیرمنتظره شود.
اما برای تحلیل‌گران متن‌باز (OSINT)، چنین ناهنجاری‌هایی می‌تواند پیامدهای قابل توجهی داشته باشد.
نمایش یک B-52 بر فراز مدیترانه مرکزی فوراً توجه‌ها را جلب می‌کند، زیرا این بمب‌افکن یکی از اصلی‌ترین پلتفرم‌های حمله دوربرد ایالات متحده است. گزارش حضور B-52 در سیسیل به‌طور طبیعی باعث گمانه‌زنی درباره عملیات احتمالی نظامی، تغییر آرایش نیروها یا آمادگی برای سناریوهای منطقه‌ای می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14369" target="_blank">📅 22:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14368">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
بمب افکن مخوف بی-۵۲ آمریکایی همکنون وارد حوزه خلیج فارس شد. قبل از رسیدن به تنگه هرمز یک هواپیمای سوخت‌رسان انتظارش را می‌کشد. خواهیم دید چه خواهد شد. @withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14368" target="_blank">📅 22:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14367">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaGfLaCIibeN8ossoi61Gtu8nT7OAam3NCgUDrAQjV0Cgvjc_Whnru0kxWt_oelBeXP4CyGqCv_4oxC3grbkNmeu0a9Jcfb_tUzK7oeTuGSln6D8BPxscnVWAw7gl2joYh1GGX25LnRMjW5HgOoc4gQA9K7MerBnwjopuS1VYQQFFGc9k8FdBpa5LIhuaUAi96kegh8Io7XJqlO3wr8VBs6lXn7gMQ2m1GNu7VggZ3ptj4UJcOUFLJSSBdjetM7NwJQFRTjJx1xDjVQkYXPNvzbZ4Zi9KsBh9JE8wmaLrALLO7nnfmtJ6_7iA4VAYpARGEpaLVysBc1Lg1GFqyshbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
بمب افکن مخوف بی-۵۲ آمریکایی همکنون وارد حوزه خلیج فارس شد. قبل از رسیدن به تنگه هرمز یک هواپیمای سوخت‌رسان انتظارش را می‌کشد. خواهیم دید چه خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14367" target="_blank">📅 22:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14366">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پدافندهای کل کشور به حالت آماده باش 100 درصدی درآمد
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14366" target="_blank">📅 22:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14365">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">منابع عبری: اسرائیل درحال آماده سازی جهت حمله به ایران است
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14365" target="_blank">📅 22:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14364">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آکسیوس: قطری‌ها امروز سعی کردن یک دیدار سه‌جانبه ترتیب بدن تا مستقیماً درباره شکاف‌های باقی‌مانده مذاکره کنن، اما ایرانی‌ها نپذیرفتن.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14364" target="_blank">📅 21:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14363">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sph9GUIx2Bd5K60m31-kpiyntt57SkoX8WuLhTkPfWNgjOf81lihsdAXIp7g6EEHWfut8jWIJLpt-fbSgKpOdG2pn-zKqWyBLJJfpSdH6wTcHQXz0iL0cj7MFU9vnO9uvsxbqLXhb3F65zJQQGofaIxvOhwub7C8jm1FSwda2vnvfy76wlTmd3hwJFMj-Ixupg8rpvEuOLsShHLgVkXbAn5YGzksgYhsvty10OKspEeZ-5UhNz3t3_UtPiAya9MKp6XL_Zrp2jB2IvrlsZLFjYrCnJOsg3VOK1DQ-rBqOtLyVGlOjk-HIxDjV05juW0ddEhjib7W5Fh2REwO4iX1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ:
در ماه گذشته، من ارتش ایالات متحده بزرگ رو برای انجام یک ماموریت مخفی به منظور حمایت از نفتکش‌ها و سایر کشتی‌های تجاری از طریق تنگه هرمز هدایت کردم. امروز خوشحالم اعلام کنم که این تلاش منجر به عبور بیش از 100 میلیون بشکه نفت از طریق تنگه و به بازار آزاد شده. بیش از 200 کشتی تجاری با امنیت از تنگه عبور کردن. این تلاش بسیار موفق به دلیل کنترل ایالات متحده آمریکا بر تنگه هرمز است.
نه ایران. ارتش آنها شکست خورده و اقتصادشان نابود شده. کار ایران تمام شده!
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14363" target="_blank">📅 21:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14362">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیدبانهای اتاق جنگ مثل پلنگ آمده هستن</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14362" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14361">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromعمو آریا</strong></div>
<div class="tg-text">سلام یاشار
اندیمشکم پشت بوم نشستم بخدااا سه تا پهباد تا الان دیدم دارن رد میشن هرکدوم به یه جهتتتت یاموسیییی</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14361" target="_blank">📅 21:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14360">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ایران ما، امروز بیش از هر زمان دیگری به اتحاد نیروهای ملی نیاز دارد. چه با حمایت خارجی و چه بدون آن، سرنوشت ایران در دستان خود ماست. ما از این رژیم فرسوده و درمانده نیرومندتریم. ما از مزدورانی که برای نمایش‌های تبلیغاتی به خیابان فرستاده می‌شوند، مصمم‌تر و استوارتریم.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14360" target="_blank">📅 21:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14359">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وزیر دفاع اسراییل کاتز:ارتش اسرائیل آماده حمله‌ای بسیار قوی به ایران است
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14359" target="_blank">📅 21:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14358">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
به گزارش i24NEWS، ایالات متحده در حال آماده‌سازی موج گسترده‌تری از حملات علیه اهداف ایرانی در ساعات آینده است که فراتر از دامنه حملات قبلی خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14358" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14357">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سفیر ایالات متحده در اسرائیل مایک هاکبی:ممکن است به زودی اوضاع در منطقه کمی داغ شود.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14357" target="_blank">📅 20:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14356">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCv0yc6FvV5CupdH4r6yREaayIR_vZJfl_1iHb7ZmQ4TB9LRxB458_GkcCXN7babcCFfiwvAtzvJgpiCg3y-ey1aJOkJPMrbKlIh_JT67rsRTsKQrQZ0DD_VwpbGzrScsBvUXkvq7TzKKG0hLkB-aXLnTUGTO_aXOvUw9CQwycLYiBwWPF2FRWEoYkJ5F0uaF2S-Fl2DVZ-bubn0ZLQ_-AZN_VAMtorOear0Zxi26BS1WPQxPv6ZHnkuco_q76LiN1lYDfohlfSGOAVS2IEECPorcKS4X6H1sxARTuYweMUOW9KW4TDc9FIXdnoMTV7ZBJU7ZSNIoSWdQbcLRWleyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی ۵۲ هم اکنون روی آسمان سعودی است
🚨
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14356" target="_blank">📅 20:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14355">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فعالیت جت‌های جنگنده ارتش بر فراز خرم‌آباد و کوهدشت، استان لرستان، غرب ایران نیز گزارش شده است
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14355" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14354">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ خطاب به سازمان رادیو و تلویزیون اسرائیل: ما در حال پیشرفت عالی با ایران هستیم
بدون من، اسرائیل وجود نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 98.1K · <a href="https://t.me/withyashar/14354" target="_blank">📅 20:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14353">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حنظله تهدید کرد !
گروه هکری حنظله: به تفنگداران دریایی آمریکا توصیه می‌کنیم همین حالا با خانواده‌های خود تماس بگیرند و خداحافظی کنند
موشک‌ها آمادهٔ شلیک هستند و «حنظله» منتظر یک حماقت از سوی شماست. ضربهٔ ساعت‌های آینده تلخ خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14353" target="_blank">📅 20:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14352">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDANNY</strong></div>
<div class="tg-text">یاشار ضربه اخرووو بزن</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14352" target="_blank">📅 20:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14351">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSkNAR-Iidsr74_Y3jXrpnqENvrhAzbvsTsa2HK-JP5Row9fIj6ChrswX_FKHHYr5E7MBtLrwnAjEZ8DZsKfOumMVdqOTD4TPkeFueWY9-Mi29AhJR40AYrwBhCuX0UI8oG3iEaNBnuxqpuXNAJ7RDZyP2atFPwjtmlrqMgO85YMLGqtZdDhiVczgWYDUMGfXU1neGO3yO4jdWSJ3c8wH-AO098dchEnrd9EvhSIaRn4Z5GOX2CSAwROzaTkWBzE8CoBhzj2BZ3VKyNGWsSA0Wo3cxETmt_HQJh5dS-EZ46EIStd13qOvXWXHb-3VXJ50sgfldTFqY0mCByohvgrbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش مردمی: آتش سوزی بزرگ میدان قیام تهران
انبار فرش ، بغل پمپ بنزین زیر پل ری!
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14351" target="_blank">📅 20:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14350">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdMx05tT6u8L-mf68vxDonAfE6bUkWqaOWmzq-NGRNGLQ_h39ZBlnVyVxnIorIW2p73QBM0jF_1kE9dOxIEm-_eJNWQbudPGxD_7zhlhl-Tx_hfyK01MbfqAr-in_fF6uElWPIIWCsDC8eyIyW3LCIDwS63juE10jjYtgdJZr_TVz_xGA461nqmQRly44l92LrAz8E8l_2dDno6_hHGRRgMWLODdUh2A8OX8LnQkE2XzWVUztJsv2NSiNa-jw_P77FRpu5Die9cOrK8OCL4WpuaXasl5C-O535fd9J7BLVQv3-N_YLV-7tZtrwEVDSJXyzOuL9DbUAYggmAiBRU3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران داره از همه جاش دود میزنه بیرون.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14350" target="_blank">📅 20:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14349">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شاهزاده رضا پهلوی اعلام کرد امشب ساعت 21 پیامی برای مردم داره
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14349" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14348">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14348" target="_blank">📅 20:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14347">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ: با بمب‌افکن‌های B-2 به ایران حمله می‌کنیم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14347" target="_blank">📅 20:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14346">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAfshin T</strong></div>
<div class="tg-text">راست گفتی باید پوشک ببندیممممم</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14346" target="_blank">📅 19:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14345">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: عینک دودی مکرون که در فضای بسته از آن استفاده میکند از سلاح هسته ای خطرناک تر است، به عنوان دوست به او میگویم اصلا عینک زیبایی نیست
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14345" target="_blank">📅 19:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14344">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ: فکر می‌کنم آنها بخواهند معامله‌ای انجام دهند.
@withyashar</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/14344" target="_blank">📅 19:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14343">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ :  وقتی این جنگ تموم بشه، تورم مثل یه سنگ سقوط می‌کنه.
ما داشتیم میلیون‌ها بشکه نفت خارج می‌کردیم؛ اینو امروز برای اولین بار اعلام می‌کنم، اما مدت‌هاست که این کار رو انجام می‌دیم. هر شب نفت خارج می‌کردیم.
حالا دارم بهتون می‌گم چون ایران تازه متوجه این موضوع شده. حالا که فهمیدن، می‌تونم درباره‌ش صحبت کنم. برای من خیلی سخت بود؛ دلم می‌خواست زودتر بگمش، ولی نمی‌خواستم این عملیات به خطر بیفته.
میلیون‌ها بشکه نفت خارج شده و به همین دلیله که قیمت نفت به‌جای ۲۵۰ دلار، حدود ۸۵ تا ۹۰ دلار در هر بشکه است.
اما ما قدرتمندترین ارتش دنیا رو داریم.
به درخواست پاکستان به ایران فرصت دادم. فیلد مارشال و نخست‌وزیر پاکستان آدم‌های فوق‌العاده‌ای هستند.
ما جلوی جنگ بین پاکستان و هند را گرفتیم
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14343" target="_blank">📅 19:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14342">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عرزشی ها ریختن دایرکتم دارن دیوارو چنگ میزنند
🤣
🤣
بای بای بی پدرو مادرا</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14342" target="_blank">📅 19:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14341">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کانال ۱۴ اسرائیل: مشکل ترامپ این است که تهدیدهایش دیگر نه تنها در نگاه غربی‌ها، بلکه در چشم ایرانی‌ها نیز اعتبار خود را از دست داده است
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14341" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14340">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ: ایران وقت‌کشی می‌کند و من می‌گویم چند روز دیگر هم به آن‌ها فرصت بدهیم، اما آن‌ها همچنان به تعلل و وقت‌کشی ادامه می‌دهند.»
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14340" target="_blank">📅 19:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14339">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ : پاکستان همین الان داره تلاش میکنه تا ایران راضی کنه توافقی انجام بدن
@withyashar</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/withyashar/14339" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14338">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: شب گذشته و در گذشته برای هدف قرار دادن رادارهای ایران کار کردیم
@withyashar</div>
<div class="tg-footer">👁️ 95.1K · <a href="https://t.me/withyashar/14338" target="_blank">📅 19:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14337">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتاق جنگ با یاشار :
⌛️
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/14337" target="_blank">📅 19:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14336">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گزارشگر: برای تولدتان چه آرزویی دارید؟
ترامپ: صلح برای کل جهان
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14336" target="_blank">📅 19:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14335">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اتاق جنگ با یاشار : امیدوارم به لحظات ملکوتی نزدیک بشیم … همه دعا کنید و انرژی بدین ،اول برای خودتون و خونوادتون همچنین ایران و برا منم دعا کنید که بدنم بکشه و مشکل گشا باشه واسم تا مأموریتم و خدمت به شما رو به پایان بتونم برسونم
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14335" target="_blank">📅 19:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14334">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: خیلی به توافق نزدیک بودیم ولی اونها معطل کردن مارو بازی دادن
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/14334" target="_blank">📅 19:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14333">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">lترامپ درباره ایران: یا باید راه حلی با آن پیدا کنیم یا آنها رو از بین خواهیم برد.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14333" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14332">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: فاش نمیکنم که آیا پل‌ها و نیروگاه‌ها رو هدف قرار خواهیم داد یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14332" target="_blank">📅 19:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14331">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: تا زمان امضای توافق به ایران با قدرت حمله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14331" target="_blank">📅 19:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14330">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: ما به آنها حمله خواهیم کرد و بسیار شدید حمله خواهیم کرد. ما بمباران رو از سر خواهیم گرفت. ما حق انجام این کار رو داریم. آنها هلیکوپتر ما رو ساقط کردن.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14330" target="_blank">📅 19:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14329">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: امروز دوباره به ایران حمله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14329" target="_blank">📅 19:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14328">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صداوسیما: یه پهپاد جاسوسی آمریکایی بر فراز آسمون تهران سرنگون کردیم
@withyashar</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/14328" target="_blank">📅 19:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14327">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اتاق جنگ با یاشار : امیدوارم به لحظات ملکوتی نزدیک بشیم … همه دعا کنید و انرژی بدین ،اول برای خودتون و خونوادتون همچنین ایران و برا منم دعا کنید که بدنم بکشه و مشکل گشا باشه واسم تا مأموریتم و خدمت به شما رو به پایان بتونم برسونم
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14327" target="_blank">📅 19:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14326">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آژانس انرژی اتمی طی گزارشی قبل از شروع جلسه شورای حکام، جمهوری اسلامی ایران رو به پنهان‌کاری متهم کرد.
@withyashar
دفعات قبل (جنگ ۱۲ روزه) بعد از گزارش آژانس، حملات شروع شد!</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14326" target="_blank">📅 18:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14325">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تصویب قطعنامه علیه ایران در آژانس اتمی
الجزیره:شورای حکام آژانس بین‌المللی انرژی اتمی قطعنامه‌ای را در مورد برنامه هسته‌ای ایران با ۲۱ رأی موافق، ۳ رأی مخالف و ۱۰ رأی ممتنع تصویب کرد.
گزارش‌ها حاکی است روسیه، چین و نیجر به این قطعنامه رأی مخالف داده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14325" target="_blank">📅 18:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14324">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/783785aee6.mp4?token=FVPc5tMSmnbo4Vm_BiMPFTBpovWfEMfnMgm9EiwmhW92RoPegVZYx8-nV165uMzIxxwiiQ5-HCtt3Ua8yKqk-G5nOutxi8PpJaLxYSGSn6bG27YeP8dnrtowKaJYjeGSSr84HDEd2JaE2-qKkfbNTa6_x_v4mYnFx0fhYqIyJKTBNaLfjZ9M6LkMuILf4syJsQx6EJoZKZxkxiDASJaowmHFRwcp7wUFp6UXEHjSpAHfA7eISuE3MLKX_sL_QOOad7n2xXoo5uwxfjuAK2UprkDUzImRmVstA-lK3kdmPwBqrUr-6WDPGm4ymOL8zZInFNPy7Qnf65E6J0F8gGdbDbaGSetmlt4DU-MsB9eW8EHvvOW_z8T-9DkjJ7IL_XJZoxgFXJV1aqr0-WDYRy9VXi8p3ppQtyAkheT-ihMd0fj7Y8HyGnW5XN8vgVjA-eawb4tW9cCpATAdNcOe5x1D_6bMcHf70qyg7v2r-s5Va9MUpBaxssbakvOXAERcHW0FJn_qRajjQlU-DKj9G6q0N53_F5or8vpPLoRomYAqqVmCoEXpJ_jLde9HBzi2XSYxvFwivmk1ZdFyhflNmFPjphriILTSDgKSpCckbz26-xF9FjtpN2Z-lOOYIEjXi-AHGSy4mqeCeeBUfTF-LMpYazVBOpTr_qyhbz8GA8kyQMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/783785aee6.mp4?token=FVPc5tMSmnbo4Vm_BiMPFTBpovWfEMfnMgm9EiwmhW92RoPegVZYx8-nV165uMzIxxwiiQ5-HCtt3Ua8yKqk-G5nOutxi8PpJaLxYSGSn6bG27YeP8dnrtowKaJYjeGSSr84HDEd2JaE2-qKkfbNTa6_x_v4mYnFx0fhYqIyJKTBNaLfjZ9M6LkMuILf4syJsQx6EJoZKZxkxiDASJaowmHFRwcp7wUFp6UXEHjSpAHfA7eISuE3MLKX_sL_QOOad7n2xXoo5uwxfjuAK2UprkDUzImRmVstA-lK3kdmPwBqrUr-6WDPGm4ymOL8zZInFNPy7Qnf65E6J0F8gGdbDbaGSetmlt4DU-MsB9eW8EHvvOW_z8T-9DkjJ7IL_XJZoxgFXJV1aqr0-WDYRy9VXi8p3ppQtyAkheT-ihMd0fj7Y8HyGnW5XN8vgVjA-eawb4tW9cCpATAdNcOe5x1D_6bMcHf70qyg7v2r-s5Va9MUpBaxssbakvOXAERcHW0FJn_qRajjQlU-DKj9G6q0N53_F5or8vpPLoRomYAqqVmCoEXpJ_jLde9HBzi2XSYxvFwivmk1ZdFyhflNmFPjphriILTSDgKSpCckbz26-xF9FjtpN2Z-lOOYIEjXi-AHGSy4mqeCeeBUfTF-LMpYazVBOpTr_qyhbz8GA8kyQMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : فرود گا ، بمب افکن مخوف بی ۵۲ به سمت ما در حرکت است !
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14324" target="_blank">📅 18:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14323">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">کاخ‌سفید اعلام کرده ترامپ قراره ساعت ۱۷:۳۰ به وقت واشنگتن ( ۱ صبح تهران ) سخنرانی اضطراری داشته باشه
@withyashar</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/14323" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14322">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو خطاب به اردوغان: به من درس اخلاق نده!
نتانیاهو مدعی شد: «اردوغان، دیکتاتور یهودستیز که مرتکب نسل‌کشی علیه کردها می‌شود، از سازمان تروریستی حماس حمایت می‌کند، مردم خود را سرکوب می‌کند و مخالفان سیاسی خود را زندانی می‌کند، او آخرین کسی است که می‌تواند به دولت اسرائیل درس اخلاق بدهد.»
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/14322" target="_blank">📅 17:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14321">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ساعت 01:59 به وقت جهانی (UTC)، یک بمب‌افکن B-52H متعلق به نیروی هوایی آمریکا در حال پرواز بود.   این هواپیما از پایگاه ماینوت در آمریکا حرکت کرده و به سمت پایگاه هوایی فِیرفورد در بریتانیا می‌رود.   این پایگاه یکی از مراکز مهم برای استقرار بمب‌افکن‌های راهبردی…</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/14321" target="_blank">📅 17:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14320">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">نتانیاهو رسما نامزد انتخابات آتی اسرائیل شد
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14320" target="_blank">📅 17:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14319">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مقامی آگاه گفت : ترامپ رسما در یک تلفن با شریف نخست وزیر پاکستان و بن حمد امیر قطر، پایان مذاکرات با تهران را اعلام کرد.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14319" target="_blank">📅 17:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14318">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش صدای انفجار‌ از محدوده سوهانک / دارآباد تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14318" target="_blank">📅 17:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14317">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یورو نیوز : در جریان یک رزمایش، تایوان یک موشک‌ آمریکایی به سمت چین شلیک کرد
ارتش تایوان امروز چهارشنبه دهم ژوئن (۲۰ خرداد ۱۴۰۵) در جریان یک رزمایش نظامی، با استفاده از پرتابگرهای سیار موشکی «شلیک و گریز»، به سمت چین راکت‌‌هایی شلیک کرد. این تمرین نشان می‌دهد که تایوان در صورت حمله احتمالی چین چکونه از خود دفاع خواهد کرد.
@withyashar
خوب اینام شروع کنن تیم تکمیله
🤣</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14317" target="_blank">📅 16:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14316">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت: تهران مذاکرات صلح را به تعویق انداخت که در نهایت منجر به پیشرفت بسیار محدودی شد‌‌
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14316" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14315">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صدای انفجار در کویت
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14315" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14314">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نتانیاهو: اسرائیل به شدت علیه ایران و نمایندگانش که خاورمیانه و جهان را تهدید می‌کنند، به فعالیت خود ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14314" target="_blank">📅 16:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14313">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فاکس نیوز به نقل از یک دیپلمات آگاه:
پس از رایزنی با ایالات متحده، مذاکره‌کنندگان قطری امروز صبح برای دیدار با ایرانی‌ها به تهران سفر کردن تا در تلاشی برای رفع اختلافات باقی‌مانده در فرآیند مذاکره باشن.
@withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14313" target="_blank">📅 16:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14312">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ در گفتگو با فاکس نیوز: بالگرد آپاچی AH-64 ارتش ایالات متحده که اوایل این هفته سقوط کرد، توسط یک پهپاد که بین دو خلبان خورده بود، مورد اصابت قرار گرفت.
با وجود آتش گرفتن و ایجاد گرمای شدید، پهپاد منفجر نشد و به خلبانان اجازه داد تا در دریا فرود اضطراری داشته باشند.
خدمه حدود دو ساعت بعد توسط یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده نجات یافتند.
ترامپ زنده ماندن خلبانان را یک "معجزه" توصیف کرد
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14312" target="_blank">📅 15:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14311">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">معاون وزیر ارتباطات از بازگشت ۷۸ درصدی ترافیک اینترنت به شرایط پیش از محدودیت‌ها خبر داد و ابراز امیدواری کرد حداکثر طی دو هفته آینده وضعیت به طور کامل عادی شود. وی همچنین شایعه اعمال فیلترینگ جدید را تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14311" target="_blank">📅 15:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14310">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به فاکس نیوز : فرصت اینو داشتند توافق رو امضا کنند و زنده بمونن
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14310" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14309">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ به کانال ۱۳ اسرائیل:احتمال واقعی وجود دارد که جنگ جدیدی علیه ایران آغاز کنم
@withyashar</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/14309" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14308">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">معاون عراقچی به الجزیره: سرنگونی هلی کوپتر آمریکایی عمدی نبوده است
@withyashar
🤣</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/14308" target="_blank">📅 15:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14307">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تحلیلگر عرب:با درگیری‌های دیشب و چند روز پیش آمریکا و اسرائیل به اطمینان رسیدن که قدرت نظامی ایران به مقدار خیلی زیادی نابود شده و این یکی از دلایل برای شروع مجدد جنگ گسترده.
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/14307" target="_blank">📅 15:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14306">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش صدای انفجار‌ از محدوده سوهانک / دارآباد تهران
🚨
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/14306" target="_blank">📅 15:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14305">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1ap_lalh9mQVypW7bFwD4SCQcAciHrINoccfiP6j8vchHZRBiTMjweNsdmW5PJSviRKynbqZ0EvTgvXj1NTmFvHAfcGdRjTKJhgbzjYs_UWv4-8NRZ8fPQbvZy1SYuII5fYfPqXg3GeqNiTW7vepDOJ862NBknym5f9FLzFXWyk1L5FiF5CvkLbNsDiF7Y5BmeOglhJ3JYYN1_bEAbnXpk6UedAZn4H9rbOdaip16yhTEBfl1whv5j1RajsrQUOfoQOddxKxAD0EZL_kJAyTz6ZTMfAuAVA-Fb7qkdkDc8c0RQlJrQIogGV_Gm2efxbWL83K2G9g7OP2K7ENqJdXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید:
قلدر خاورمیانه مُرده است!!!
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/14305" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14304">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: حملات بیشتر آمریکا به ایران، یک گزینه واقع بینانه است.
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/14304" target="_blank">📅 15:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14303">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/951e923604.mp4?token=PjsXuyu60_31W2G6cf8XlqQo3-W7htCaWpoB7LBGJC9j3WFgYPUIMgNaZfkkqukLzE3MpiAgJjOr_OCFVCb1JeDDm9g-HhhpIP2BP9h7SzV1TsDg56bZyQ00yRMVXtgvAN1wq6EHCcYe2nf08tfIYpU0RvMUiQKAffiqP69SYxfyrFMR01AKq5rArNI_-PiwoeipBMzultgvi84ASAo2Ma3KRvQom0yUF9OpPb-Uv3mnG-LQbq7cPebDNjHnOl0b4TSsqHIWf7wqh3HfuAMR7bgj1kUo9ZQcuFdYZ-hMA5H6MII5eSr8G8MJ1KdDLDuIZH9frUmuN4tsFtiikzqf_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/951e923604.mp4?token=PjsXuyu60_31W2G6cf8XlqQo3-W7htCaWpoB7LBGJC9j3WFgYPUIMgNaZfkkqukLzE3MpiAgJjOr_OCFVCb1JeDDm9g-HhhpIP2BP9h7SzV1TsDg56bZyQ00yRMVXtgvAN1wq6EHCcYe2nf08tfIYpU0RvMUiQKAffiqP69SYxfyrFMR01AKq5rArNI_-PiwoeipBMzultgvi84ASAo2Ma3KRvQom0yUF9OpPb-Uv3mnG-LQbq7cPebDNjHnOl0b4TSsqHIWf7wqh3HfuAMR7bgj1kUo9ZQcuFdYZ-hMA5H6MII5eSr8G8MJ1KdDLDuIZH9frUmuN4tsFtiikzqf_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل نان استاپ داره لبنان رو میزنه، یه خودرو رو هم با پهپاد نقطه‌زنی کرده، هدفمند.
@withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14303" target="_blank">📅 15:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14302">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: در آتش بس 55 درصد از آنچه که ایران درحال بازسازی آن بود را ویران کردم هنوز با ایران کار دارم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14302" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14301">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک منبع مطلع به i24NEWS می‌گوید:   رئیس‌جمهور ترامپ دیشب با نخست‌وزیر نتانیاهو صحبت کرد و او را در جریان حمله احتمالی امشب قرار داد.  این دو همچنین درباره موضوعات دیگری مرتبط با مذاکرات با ایران بحث کردند.  در آمریکا از وضعیت مذاکرات ناامید شده‌اند و صبرشان رو به پایان است.
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14301" target="_blank">📅 15:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14300">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ این جمله را برای بار دوم دارد می‌گوید: «بلوکاد «حبس دریایی» ما علیه ایران آنقدر موفق است که حتی خدای آنها (الله) هم دارد علیه آنها کار می‌کند و من را تأیید می‌کند، ستایش بر الله باد!» @withyashar</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14300" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14299">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نتانیاهو: اسرائیل به شدت علیه ایران و نمایندگانش که خاورمیانه و جهان را تهدید می‌کنند، به فعالیت خود ادامه خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/14299" target="_blank">📅 15:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14298">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پست جدیدتر ترامپ: رسانه‌های اخبار جعلی از گزارش میزان اثربخشی محاصره دریایی ایالات متحده، که موفق‌ترین محاصره در تاریخ جنگ دریایی است، خودداری می‌کنند.  هیچ چیز عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران هیچ تجارتی ندارد، به ارتش خود…</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14298" target="_blank">📅 15:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14297">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ: میدونی خیلی وقت کشی میکنن خیلی باعث میشه تصمیم حمله بگیرم
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/14297" target="_blank">📅 15:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14296">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ داره قاهره رو رد میکنه اقا ترمز کن
🤣
🤣</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14296" target="_blank">📅 15:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14295">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza</strong></div>
<div class="tg-text">ترامپ داره قاهره رو رد میکنه اقا ترمز کن
🤣
🤣</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/14295" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14294">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2L6-hdbu7OdNgGrA7ONUdRfmDePXzMv8DG6eWN6ftmMC_K3tpCBhfPx2WwUfr_wCvInFMRd4imwmt_ir0qo6mNkYuOBa14Adz19NgKhUVl9385qhoF1CKfqugL3Lkktg9wLL_47pDZtTl7shdvfCTsrApqnW5aIR0c4QObX3sqP5Z4ZroTSe_Ia6jcaiNix6T4_JPKnYljfzSem5PPnAFJkBDMmaMZ6Iq_JR9GNnPXsenqVz6b1WMfxNKNbtWQjXXORS8RAc4GO0X9jWYBtNeqY4zeZWj1TFq89YMfChNrFWi27mOLjQuKTIB78gBWgpIv5qXIKpZqNPy0NjhYmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدیدتر ترامپ:
رسانه‌های اخبار جعلی از گزارش میزان اثربخشی محاصره دریایی ایالات متحده، که موفق‌ترین محاصره در تاریخ جنگ دریایی است، خودداری می‌کنند.
هیچ چیز عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران هیچ تجارتی ندارد، به ارتش خود یا هیچ یک از صورتحساب‌هایش پرداخت نمی‌کند و به سرعت به یک ملت شکست خورده تبدیل می‌شود! نفت زیادی در حال خروج است.
الله  را شکر !
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/14294" target="_blank">📅 15:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14293">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فاکس نیوز: ترامپ در حال مشورت با مشاوران خود برای بازگشت به جنگ با ایران است و گزینه حملات به نیروگاه‌ها و پل‌های ایران را بررسی می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/14293" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14292">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف: با وجود شهادت فرماندهان و دانشمندان در جنگ ۱۲ روزه، نه حرکت علم و دانش در کشور متوقف شد و نه توان دفاعی و بازدارندگی ایران کاهش یافت
@withyashar</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/14292" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14291">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ : ما کارمون با ایران رو ادامه می‌دیم و جلو می‌ریم
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/14291" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14290">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ به فاکس : به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/14290" target="_blank">📅 15:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14289">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وزیر فرهنگ اسرائیل:
دیکتاتور اردوغان که دستانش آغشته به خون است باید درباره جنایاتش پاسخگو باشد و به تنها کشور دموکراتیک در خاورمیانه موعظه نکند. اگر جرات کند ما را امتحان کند - سرنوشتش بدتر از رژیم رو به زوال ایران خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/14289" target="_blank">📅 14:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14288">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قالیباف، رئیس مجلس ایران :
توان دفاعی و بازدارندگی ایران همچنان پابرجاست و آسیبی به اون وارد نشده
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/14288" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14287">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو بعد توییت ترامپ: ایران نباید سلاح هسته ای داشته باشه.
@withyashar</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/14287" target="_blank">📅 14:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14286">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5y1oN_kakPB-kGrov_sXX6olhl3eKoUxy9hdYmcEUxHMNcncLcY9POqVCh-g4rsv0ltQ16CLSfO2xJOKdcV-BVeTIZYblNTdHsSr3qSeb8WbtrfSXRaBteTdeMv7031xJqpRi8q6gFZG7YjW5iIvCde1L5Ybo176tYrcX3Sww0gaAEAs7sP0p8LUCrOuVHyfKA1wy8CLXTGIsrqoPgIz_HypmMinuJqnZ41sD_mJtvvdaq1QxWmlEz4nc36psKy2dIG6NZ3-rPakA1Xnw4ljmLKg09dzqMx-nzVLF7_DRsj2Vopr1Gybk8YSBOy1kAbZLzY2gc4_mylQCpg8XPXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:  ارتش ایران کاملاً از هم پاشیده و نابود شده. بخش بزرگی از توان نظامی ایران، از جمله نیروی دریایی و نیروی هوایی، عملاً دیگه وجود نداره. ایران به طور کامل شکست خورده. ایران فقط حرف می‌زنه و کاری انجام نمی‌ده. قلدر خاورمیانه مُرده! خیلی بیشتر از حد لازم برای مذاکره روی توافقی که می‌تونست به نفعشون باشه وقت تلف کردن و حالا باید بهای این کار رو پرداخت کنن
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14286" target="_blank">📅 14:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14285">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سناتور لیندزی گراهام در رقابت با بازرگان مارک لینچ، در انتخابات مقدماتی سنای جمهوری‌خواهان کارولینای جنوبی پیروز شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14285" target="_blank">📅 14:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14284">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43d918eef.mp4?token=e4QFy226tLE39MZfNSTeH2zB8RJWbrNhi8NBjXnWqzzlMxxHQrRakim72MSrnKEuPvubOmgtDbgowhLyDGK_tpWzzHrwnrb3ntoAsVkUlotkWqgi0Ph3kik68fkN8v5CppQcNQLPFyV3dLJKGPBjwqbZE0BlnaZf6pA8ZiV6Dpm--yIHIVteOKauyoNMnKcFWzrORoOfVZ8RTdT-heOXN2O0Lvg5BEiIp5_ObevVq3kMVqyxNg32jnLyutxCdT_LHU7xsCxKfuGTZz2kXkZ0bvAQjGn0ksG0Ila-OpGMcm3AgxEv-3_gLe8aI86IVFJcdAUJHFlLu-AUxh-sAwxaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43d918eef.mp4?token=e4QFy226tLE39MZfNSTeH2zB8RJWbrNhi8NBjXnWqzzlMxxHQrRakim72MSrnKEuPvubOmgtDbgowhLyDGK_tpWzzHrwnrb3ntoAsVkUlotkWqgi0Ph3kik68fkN8v5CppQcNQLPFyV3dLJKGPBjwqbZE0BlnaZf6pA8ZiV6Dpm--yIHIVteOKauyoNMnKcFWzrORoOfVZ8RTdT-heOXN2O0Lvg5BEiIp5_ObevVq3kMVqyxNg32jnLyutxCdT_LHU7xsCxKfuGTZz2kXkZ0bvAQjGn0ksG0Ila-OpGMcm3AgxEv-3_gLe8aI86IVFJcdAUJHFlLu-AUxh-sAwxaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اردوغان: ما کاملاً آگاهیم که هدف نهایی توهم «اسرائیل بزرگ» چیست.
ان‌شاءالله هرگز اجازه نخواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 94.1K · <a href="https://t.me/withyashar/14284" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14283">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ایران می‌گوید دیپلماسی با ایالات متحده به دلیل این حملات تضعیف شده است.
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14283" target="_blank">📅 13:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اردوغان درباره رئیس جمهور آمریکا، ترامپ: «شرکت او در اجلاس ناتو در آنکارا برای وحدت اتحادها مهم است»
@withyashar
یاشار : امیدوارم ترامپ به این اجلاس نره ! جدا از تمام مسائل مذاکرات، می‌تواند به آخرین تیر ترکش جمهوری اسلامی برای به خطر انداختن جانش هم تمام شود.</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/14282" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO): گزارشی از یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرق صحار در عمان دریافت کرده است. در پی آتش‌سوزی در اتاق موتور یک نفتکش، یک نفر زخمی و دو نفر از خدمه مفقود شده‌اند؛ این نهاد، هیچ‌گونه آلودگی زیست‌محیطی گزارش نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 97.1K · <a href="https://t.me/withyashar/14281" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14280">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یونی بن مناخیم، تحلیلگر ارشد مرکز اورشلیم، به کانال ۱۴ گفت که ایران سیستم‌های دفاع هوایی که چند هفته پیش توسط ایالات متحده و اسرائیل نابود شده بود را بازسازی کرده بود. بهبودی با این سرعت بدون کمک مستقیم چین امکان‌پذیر نبود.
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/14280" target="_blank">📅 12:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هم اکنون صدای انفجار‌ در‌ سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14279" target="_blank">📅 12:35 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
