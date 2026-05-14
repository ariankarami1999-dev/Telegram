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
<img src="https://cdn4.telesco.pe/file/ldU5m6jlgZaD6v06j4HiQZB9vCJJC85emLDx58iUQW3aGLrAVwVsGb6zJKSlmBRHiYO_3mILmkJYzPbmY__xDHIJmdKHeX_P9IgFHHlRls-z3Pj-bb1ZUEEBBvWERjptlVmiyU595yRKiACTqitboTCgCMq53rtSZL2GyZ8QjWt1OpfjQIlAwoHNOD1fRkQ2rbFXmJtfXbijds9AGbJp6njZuHH7sZNGJsm5ZqdFzVfzsToI_qcj_PvJl_5eD-UEFQ9ncDe9zfFUMM-GrNJNF4GddPSU2s2oHEso6KpIUu6rc1SS8iVO8pp0X8R9AtVaAS5cmuCAA492EmT29S8PPg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 959K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 12:58:16</div>
<hr>

<div class="tg-post" id="msg-119891">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7e782c88f.mp4?token=BQGGCY2WQm8_2LkSA19Jp9s7m-QHBORg6zciDrGj_YpL4ysy9DNow9HeQ0GLrMXjSAdKV4sjtBBjXDoqscWyFy5PvKb--yqiKEXD2bvcmksYGNqto86l8Bzq28GEAuf9jXDNgfVh_tr2koywG61poqAtz8IW3p0y7jo-f4KlkcIaQdWAuPc0ifrA_y3eottnD90n9PoPCzxBnaLACs47Nyqhn2uVN3vr46ybCZe4fsC8gtDQ8-EVitEVpq0hpanQM120MV37kJcgjUmtC-8oCPYAPBU0WtB1Y4gnvobXZti24qsGjZ5fKO6rWNHo6Obd7Lsz8Z4UZf4hNm5-X1cvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7e782c88f.mp4?token=BQGGCY2WQm8_2LkSA19Jp9s7m-QHBORg6zciDrGj_YpL4ysy9DNow9HeQ0GLrMXjSAdKV4sjtBBjXDoqscWyFy5PvKb--yqiKEXD2bvcmksYGNqto86l8Bzq28GEAuf9jXDNgfVh_tr2koywG61poqAtz8IW3p0y7jo-f4KlkcIaQdWAuPc0ifrA_y3eottnD90n9PoPCzxBnaLACs47Nyqhn2uVN3vr46ybCZe4fsC8gtDQ8-EVitEVpq0hpanQM120MV37kJcgjUmtC-8oCPYAPBU0WtB1Y4gnvobXZti24qsGjZ5fKO6rWNHo6Obd7Lsz8Z4UZf4hNm5-X1cvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: ما تنگه هرمز را نبسته‌ایم، آمریکا بسته!
🔴
از نظر ما، تنگه هرمز برای تمامی کشتی‌های تجاری باز است، اما آن‌ها باید با نیروهای دریایی ما همکاری کنند.
🔴
ما هیچ مانعی در تنگه هرمز ایجاد نکرده‌ایم؛ این آمریکاست که محاصره ایجاد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.27K · <a href="https://t.me/alonews/119891" target="_blank">📅 12:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119890">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
سی‌ان‌ان: کاخ سفید می‌گوید ایران بر مذاکرات «خوب» ترامپ و شی جین پینگ سایه افکنده است
🔴
کاخ سفید روز اول مذاکرات پرمخاطره بین دونالد ترامپ، رئیس جمهور آمریکا و شی جین پینگ، رهبر چین را مثبت ارزیابی کرد و از متن مذاکرات مشخص است که ایران یکی از موضوعات کلیدی این گفتگو بوده است.
🔴
ایران روابط نزدیکی با چین دارد که بزرگترین مصرف کننده نفت ایران است. انتظار می‌رفت ترامپ، شی جین پینگ را برای اعمال فشار بر ایران جهت بازگشایی تنگه هرمز، یک گذرگاه حیاتی نفت، تحت فشار قرار دهد.
🔴
یک مقام کاخ سفید گفت: «دو طرف توافق کردند که تنگه هرمز باید برای حمایت از جریان آزاد انرژی باز بماند.»
🔴
این مقام رسمی به طور مشخص نگفت که آیا شی جین پینگ با گسترش مشارکت چین در کمک به پایان دادن به این درگیری موافقت کرده است یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/alonews/119890" target="_blank">📅 12:52 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119889">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
دقایقی پیش زمین‌لرزه‌ای ۵ ریشتری در عمق ۸ کیلومتری بردسیر کرمان را لرزاند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/alonews/119889" target="_blank">📅 12:51 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119888">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خبرگزاری فرانسه: چین قول می‌دهد درها را به روی شرکت‌ها بازتر کند
🔴
شی جین پینگ، رئیس جمهور چین، در دیدار با رهبران تجاری آمریکا، با تأکید بر تمایل پکن برای تقویت همکاری اقتصادی و تجاری با ایالات متحده، تأیید کرد که درهای چین «حتی گسترده‌تر» به روی جهان باز خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/alonews/119888" target="_blank">📅 12:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119887">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adee5fe5fe.mp4?token=nnqWH8rhL-ruZchL9vAIWmhyPzIdefPTsw-XoDNhMcoV_PP7LzjXNDtZDYft1zfTghfXhiGcXYLFBS5gPENW0Szpvb7OwHyvJ75fIk69LJrRMDLpY1luSU9qqye5XcRImBACDF6GLTZCY3ul4ItyHlxS-8-iwtrkSbzwhQhvmOf4S_DRXQGhzq_xRM1mSBkR9-mmeAZgPH1WCsm9rjZRflpdiwub4UUblnjFdeU-brLH6UskDbq9XM21JGUAKPiCeTbeNyuZlcMzLShFwAIEnrnAIBh5bmC9HrgGrVhooKuQrKHrgctqbYEtlLidlS2trXifO0knZgMka7G8t3lMQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adee5fe5fe.mp4?token=nnqWH8rhL-ruZchL9vAIWmhyPzIdefPTsw-XoDNhMcoV_PP7LzjXNDtZDYft1zfTghfXhiGcXYLFBS5gPENW0Szpvb7OwHyvJ75fIk69LJrRMDLpY1luSU9qqye5XcRImBACDF6GLTZCY3ul4ItyHlxS-8-iwtrkSbzwhQhvmOf4S_DRXQGhzq_xRM1mSBkR9-mmeAZgPH1WCsm9rjZRflpdiwub4UUblnjFdeU-brLH6UskDbq9XM21JGUAKPiCeTbeNyuZlcMzLShFwAIEnrnAIBh5bmC9HrgGrVhooKuQrKHrgctqbYEtlLidlS2trXifO0knZgMka7G8t3lMQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ بعد از ۵۰ سال اولین رئیس‌ جمهوری شد که رفت معبد آسمونِ چین
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/alonews/119887" target="_blank">📅 12:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119886">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6393ab5f.mp4?token=ZPcoUnoFaBmAT1pU4lwlW873rJ75SWl7hyl-3bkadfP2IButZFqveF3JS4cuNg0fb986rZ23-GXxxn9a9MJstcTh_I8dYIiVNx6hZdwH6IbENCa1zqfess4vpyFWPooRVR_669zlO_kudJHNZ5LIUWTjr9u_XrkgaGEIV83Lcp7gXT-zLhcQqR0hXwAZ2cNknwfESQcrNYlL_pWFbhqfOmHoujY7mTX5Q0dazWKvkmJFISzzXIFt_Sbl3xGmqdBECAEVOn7gsAX8J9XrBR-l0O3KjHL1CGDIZNIxWTuDseNNRSAk3wWR1AmEWcmNSL7QuWNinbS4nY_vK1A9rdxLmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6393ab5f.mp4?token=ZPcoUnoFaBmAT1pU4lwlW873rJ75SWl7hyl-3bkadfP2IButZFqveF3JS4cuNg0fb986rZ23-GXxxn9a9MJstcTh_I8dYIiVNx6hZdwH6IbENCa1zqfess4vpyFWPooRVR_669zlO_kudJHNZ5LIUWTjr9u_XrkgaGEIV83Lcp7gXT-zLhcQqR0hXwAZ2cNknwfESQcrNYlL_pWFbhqfOmHoujY7mTX5Q0dazWKvkmJFISzzXIFt_Sbl3xGmqdBECAEVOn7gsAX8J9XrBR-l0O3KjHL1CGDIZNIxWTuDseNNRSAk3wWR1AmEWcmNSL7QuWNinbS4nY_vK1A9rdxLmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نحوه دست دادن رئیس جمهور چین و آمریکا مورد توجه رسانه ها قرار گرفته است
🔴
شی جی پینگ در جای خود ثابت ایستاده تا ترامپ به سمت او بیاید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/alonews/119886" target="_blank">📅 12:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119885">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
عراقچی: باید برای همگان روشن شده باشد که ایران شکست ناپذیر است / برای دفاع از آزادی و سرزمین خود آماده‌ایم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/alonews/119885" target="_blank">📅 12:38 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119884">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کاخ سفید : ایران هیچ‌وقت نباید به سلاح هسته‌ای برسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/alonews/119884" target="_blank">📅 12:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119883">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
کاخ سفید: شی به ترامپ تأکید کرد که چین با نظامی شدن تنگه هرمز مخالف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/alonews/119883" target="_blank">📅 12:15 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119882">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
کاخ سفید: روسای جمهور آمریکا و چین درباره تقویت همکاری اقتصادی گفت‌وگو کردند.
🔴
ترامپ و شی درباره تسهیل دسترسی شرکت‌های آمریکایی به بازارهای چین بحث کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/alonews/119882" target="_blank">📅 12:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119881">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کاخ سفید : ترامپ و شی توافق کردن که تنگه هرمز باید باز بمونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/alonews/119881" target="_blank">📅 12:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119880">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b945b421dd.mp4?token=as1Gf_SARJzw6gubi13Rc3XRuH_-A-AMPkabTvHXTqqijkKDv1Ts-aUjMlC2l0jGoWNZ7FDB3uma81ODWgFlV5UHhPreh3MSDN6YoKuu3Yoo_wjAsAHIz5NFMpeMeK1ilIUcCGGgI9n-X-cLxAASb4ELfF_5_taeXgeZIW1jQLiwQR6yAltzlLZSGtYNwVs20UTmJExcjYU4hOvVyIHKbYTmDrDuNlR1JooDJs71nNilV0gh8j_jkNXx8ufAEbLhJNVVD38uEgw4F97Na4KnT6qd4KSe90WBnFKzbeRi1jLdbamnFXEYUeqQHoex1R9lTERDAJzK2wdPAP4uHCoD4EDG-p-3bsb4a2dVDudafDEl-kn1wJcmR2gBBPbEPykhgURJ2v_P4vKns7YpBAqUkABuoYPfyL_ayJpOHz7-xI7OdRN-LbR7le8cN_RXjLX9EHN6hLwPQBzp48-mWpCDZ7LnL_7JOrt87VaB_E9DFl_AkKp8_sbRhThJ7gZbTVdZ1_ON7p7dVaS8vi-9W6M-C4iojvQc2JUb9vQN9tHeW0srBXZaUXYd6diLd36HIDnRLH4dR5AvZ6QzVcitn-Wbxx87gFIEm8yAepvpKLmwqbjjNgsu0P3rUtc3jY92obX6RRBpaz2MxWJoMHJU4DfNuwHB3an_zIaXbY84O1y1hNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b945b421dd.mp4?token=as1Gf_SARJzw6gubi13Rc3XRuH_-A-AMPkabTvHXTqqijkKDv1Ts-aUjMlC2l0jGoWNZ7FDB3uma81ODWgFlV5UHhPreh3MSDN6YoKuu3Yoo_wjAsAHIz5NFMpeMeK1ilIUcCGGgI9n-X-cLxAASb4ELfF_5_taeXgeZIW1jQLiwQR6yAltzlLZSGtYNwVs20UTmJExcjYU4hOvVyIHKbYTmDrDuNlR1JooDJs71nNilV0gh8j_jkNXx8ufAEbLhJNVVD38uEgw4F97Na4KnT6qd4KSe90WBnFKzbeRi1jLdbamnFXEYUeqQHoex1R9lTERDAJzK2wdPAP4uHCoD4EDG-p-3bsb4a2dVDudafDEl-kn1wJcmR2gBBPbEPykhgURJ2v_P4vKns7YpBAqUkABuoYPfyL_ayJpOHz7-xI7OdRN-LbR7le8cN_RXjLX9EHN6hLwPQBzp48-mWpCDZ7LnL_7JOrt87VaB_E9DFl_AkKp8_sbRhThJ7gZbTVdZ1_ON7p7dVaS8vi-9W6M-C4iojvQc2JUb9vQN9tHeW0srBXZaUXYd6diLd36HIDnRLH4dR5AvZ6QzVcitn-Wbxx87gFIEm8yAepvpKLmwqbjjNgsu0P3rUtc3jY92obX6RRBpaz2MxWJoMHJU4DfNuwHB3an_zIaXbY84O1y1hNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
منوچهر متکی : به بحرینی‌ها گفتم جوری می‌زنیمتون که اسمتونم یادتون بره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/alonews/119880" target="_blank">📅 12:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119879">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ با استناد به داده‌های کشتیرانی: از روز یکشنبه تاکنون ۹ نفتکش نفت و گاز از تنگه هرمز عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/alonews/119879" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119878">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40de0aedfe.mp4?token=gAuL19jI99TBfKBD1AAMAJPdfVdXZGlz4CiADdc5xFThUpWVl6FUtK-7wZKDcjPOcytqwD_Boe_EKS1nWU4IFEtBMvj8nhMjbhIDMWfe8RM8I9D7kpakoaI4JMtpHkhZWcZ0Kr1Jdmxfl0WfJU-gzvY_n5OAZEY8pM0DtR9j90rsRUAhJQVnx_yJsyGt2Wt3iescjOSPhjLJjL9XhI_lBnoSCOIWyNZyTqOEqdtonIfyoJf8ot2vzQhY1dvcGIfmFtWF8hTTj0-EJnAd2UYFiPvtTikpsgpKkwQHeIQUIb09jX2bDUQuVOc0wbbX1J9_irqQbyZSJhsQ8ewxExQkYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40de0aedfe.mp4?token=gAuL19jI99TBfKBD1AAMAJPdfVdXZGlz4CiADdc5xFThUpWVl6FUtK-7wZKDcjPOcytqwD_Boe_EKS1nWU4IFEtBMvj8nhMjbhIDMWfe8RM8I9D7kpakoaI4JMtpHkhZWcZ0Kr1Jdmxfl0WfJU-gzvY_n5OAZEY8pM0DtR9j90rsRUAhJQVnx_yJsyGt2Wt3iescjOSPhjLJjL9XhI_lBnoSCOIWyNZyTqOEqdtonIfyoJf8ot2vzQhY1dvcGIfmFtWF8hTTj0-EJnAd2UYFiPvtTikpsgpKkwQHeIQUIb09jX2bDUQuVOc0wbbX1J9_irqQbyZSJhsQ8ewxExQkYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وایرال شدن تصاویری از فیلم‌برداری ایلان ماسک در سفر چین
‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/119878" target="_blank">📅 11:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119876">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnVjbfSMf64TLxzQlVds17gp_RVLhSthAhm1DJ1UYoP93IJJHtOGlx-UYGuFM4h92fCj9jILXCqNybh16L7l8lsiCyOny6VPFEw_muCki_7JFqGz8Rx1QRaejyLNt3HjJEFn6aw0NYM5EJUzN_0vyrotbm_jDRCfBT-tA2KyjHswfa6DuwSreIiJzvOuJxj_W8n-4mS3VgRd71cYELEflv8GAU0zoDuGSgptDXfCEs_DDJejJO0WWwJ6QFpKDCsD2SjGmZe0BewgwOtnVSpYCyvK5DXwVLDH9EuKFYZ_wrB9QHpuaiBluGQnj9R3Qq-KFEZjrw6odJAtuR0DDC64Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlBxSxpKU8QCPtpMojUYzlHd5frOHWWnVE3yK79iQsKgFn8lPhNj6PCEh4hSUXRlSSVadJGNHBpknvMxGXOHORpC3Tq-Wk4vWxscHQe7BSU_0fpj_CmQaiEf-bD0St9Ts0fE4OKWG-tyUmrTRxREtVGIwVmrwOVvEVSwxv_6LgJuCh5TrSrbu3Fnje51pmaW7H8zU8af76YHMCvcYdvgso0ByPAn5fZ_QQlSFxhbPFCtDLHTEOyPlFn7-6DOhOM13WmHxJsWNAAn-J0Q8J5AFapzeJHLgIGA5ct5WdU0cajIWdsN0nC8OVyZ_IlhASrxcmDYlYIpnoZDx25CXCHStg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محسن مسلمان که حسابی تو تجمعات حامیان حکومت فعال بود، به کادرفنی تیم امید پرسپولیس پیوست.
@AloSport</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/119876" target="_blank">📅 11:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119875">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
دقایقی پیش زمین‌لرزه‌ای ۵ ریشتری در عمق ۸ کیلومتری بردسیر کرمان را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/119875" target="_blank">📅 11:46 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119874">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlnxmwyRV1GwNUd13sRVJ9WzKj5U6z2cmT766HiEXl6t_Pn1a-WUNuGzEjFTqiCLqIYZaW711poU2Bc6SE5pQwtW0odfpKoH1Ph42kI2QkNRPmlxMoXSE1xmeVp1GJ6h6Q1GDNKnmywjEFtTpoP5SuWulpvaizO_FHoKDOF-5DJlxe6eT9j7kyWo8aNkK_gmvLlMetdOX841wcDxe_eZQGb-i96-lDkyKTyY378-Zzz9bTP0QstDk5oe2ezXumboSxT1Hh2j9ORoA-Svw3hsqctjszjv6p6Cj0g7crXFexn36ixjXJla-x2UrUg6fOG0yoz5XoDMBGHEbGErei9EJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فواد ایزدی، تحلیلگر ارشد صدا و سیما: ترامپ رفته چین تا التماس کنه که ایران ولش کنه و انقدر نزنیمش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/119874" target="_blank">📅 11:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119873">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزارت خارجه چین: پکن و واشنگتن بر سر جهت‌گیری جدید روابط توافق کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/alonews/119873" target="_blank">📅 11:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119872">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VviXCvhsxPea1h6BWaPkwcRwpN7C0MAakFOHTd9LRcUYoIMdTXZZ5-XkcjCEPiDLoQHDEz6JPuZMA3O6tt_Z0IvVKhqqnGKW_fvRFXUcvjAimrXzGCSNSxmyoEVKf3RDLkeW8ZZSElxMqz18yaPWREj-hokeOMfbwciNoFmgYjRu4sHEj__AbKynZ0IwzLHnHMcGmNXLNgQVkZe6sAm7gO4hbs-QQRE51frMN2LbWh_wyRSBOr-gOo4lkrKfTy8rwqXaGs2wFpBxhDuUSPMWtc42OwVPPnyojtsEcH3E7D4iyL-EJvoJCdibDiJDrhrb23UIgrJNkZAfrE3qj8poWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه هند اعلام کرد که یک کشتی با پرچم هند در سواحل عمان دیروز مورد حمله قرار گرفت، این حادثه را «غیرقابل قبول» دانست و نگرانی خود را از هدف قرار گرفتن مداوم کشتی‌های تجاری و دریانوردان غیرنظامی ابراز کرد.
🔴
دهلی نو تأیید کرد که همه اعضای خدمه هندی حاضر در کشتی در امنیت هستند و از مقامات عمانی برای انجام عملیات نجات تشکر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/119872" target="_blank">📅 11:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119871">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
تسنیم: کیفرخواست زیباکلام و مدیرمسئول خبرگزاری آنا صادر شد ممنوعیت زیباکلام از انجام هرگونه فعالیت رسانه‌ای به مدت سه ماه  صادر شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/alonews/119871" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119870">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
جهت رزرو تبلیغات vpn در کانال
#الونیوز
به کانال زیر مراجعه کنید
👇
📃
https://t.me/ads_alonews
📃
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/119870" target="_blank">📅 11:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119868">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlMfuaIpDPqlTp2OXlWt2HVgNpcAcCU-dsbu7z33HzrAimcjnOjG06jesBB80KiQqdQ53ptKrPppiPk9eg8VWYIeSe9Cwnd9Hf-jDDLdcz6nrQFZkIi3H0SlpUQdktI4O9dy20v45ZBjPCVYau_Lpi7zy8QBtCwB5C50L62EqP7NYBrAJiaW4x473WzcvL5lnHdS2f1H9I5V3rI3x3qsKKgSR7laWPBaNCTcX721tEbW2AGL5Brw9Q0nJvAhuUOocraH-XSCy-zoVK4ktIUXlCgdHRl4LbWl00BWn14KUkk_YfTAXNtg3AuerMMnsA_MHTY69SvIiZ79zzmQ-lsXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تورم تخم مرغی
!
🔴
با ۵۰۰ هزارتومان(هزینه هر شانه تخم مرغ در این ماه) در ماه های مختلف چند شانه تخم مرغ می‌توان خرید؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/119868" target="_blank">📅 11:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119867">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/سازمان تجارت دریایی بریتانیا اعلام کرد: قایق های تندرو سپاه یک کشتی را که خارج از تنگه هرمز لنگر انداخته بود را تهدید به هدف قرار دادن و سپس توقیف کردند و اکنون در حال بردن آن به سوی بنادر ایران هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/119867" target="_blank">📅 11:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119866">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
خبرگزاری دولتی شینهوا: رهبران چین و آمریکا «درباره مسائل مهم بین‌المللی و منطقه‌ای از جمله وضعیت خاورمیانه تبادل نظر کردند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/119866" target="_blank">📅 11:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119865">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سی‌ان‌ان: تایوان اظهارات شی جین پینگ درباره استقلال این جزیره را رد کرد
🔴
تایوان پس از آنکه شی جین پینگ، رهبر چین، گفته است استقلال تایوان با صلح «آشتی ناپذیر» است، چین را «تنها منبع» ناامنی در منطقه دانست.
🔴
میشل لی، سخنگوی کابینه، در پاسخ به خبرنگاری که درباره اظهارات شی جین پینگ درباره تایوان سوال پرسیده بود، گفت: «تهدید نظامی چین تنها منبع ناامنی در تنگه تایوان و منطقه وسیع‌تر هند-اقیانوس آرام است.» او همچنین گفت: «تقویت مداوم دفاع و بازدارندگی مشترک مؤثر، مهم‌ترین عوامل برای تضمین امنیت منطقه‌ای هستند.»
🔴
رسانه‌های دولتی چین گزارش دادند که واکنش تند تایپه پس از آن صورت گرفت که شی جین‌پینگ به دونالد ترامپ، رئیس‌جمهور آمریکا، گفت تایوان «مهم‌ترین مسئله در روابط چین و آمریکا» است و در صورت عدم مدیریت صحیح می‌تواند «وضعیت بسیار خطرناکی» ایجاد کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/119865" target="_blank">📅 11:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119864">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
تایوان: واشنگتن حمایت آشکار و قاطع خود را از این جزیره تجدید کرد.
🔴
تایوان اعلام کرد که ایالات متحده «حمایت آشکار و قاطع» خود را از این جزیره تجدید می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/119864" target="_blank">📅 10:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119863">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
عدد جدید از خسارت قطعی ۷۴ روزه اینترنت ایران؛ ۳۰۰ تا ۷۰۰ هزار میلیارد تومان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119863" target="_blank">📅 10:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119862">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
ارتش اسرائیل دستور تخلیه 8 شهرک و روستا در دره بقاع و جنوب لبنان را صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/119862" target="_blank">📅 10:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119861">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا از وقوع حادثه‌ای در ۳۸ مایل دریایی شمال شرقی فجیره خبر داد
🔴
برخی رسانه‌ها گزارش دادند، انفجارهایی در سواحل فجیره امارات در پی حمله پهپادی به یک کشتی رخ داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119861" target="_blank">📅 10:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119860">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ارتش آمریکا با استفاده از تاسیسات گارد ساحلی و تاسیسات نظارتی و لجستیکی کویت در جزیره بوبیان اقدام به استقرار سامانه‌های متحرک پرتاب موشک‌های هیمارس در جزیره بوبیان و تعرض به خاک جمهوری اسلامی ایران کرده بود.
🔴
این عملیات تجاوزکارانه از خاک کویت در روز ۴ فروردین سال جاری انجام شده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119860" target="_blank">📅 10:40 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119859">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر انرژی و معادن کوبا اعلام کرد که کشور به طور کامل از دیزل و نفت کوره خالی شده است و تولید برق به صورت کامل متوقف شده، در حالی که ایالات متحده جزیره را محاصره کرده است،
🔴
بسیاری از محله‌ها در پایتخت کوبا در حال حاضر با خاموشی‌هایی مواجه هستند که 20 تا 22 ساعت در روز طول می‌کشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119859" target="_blank">📅 10:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119858">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZI530oxAUnHVUyWUU0hEeGKTYkYyQpaTR8uNcoAj0RE-G8wc5V5KTtV90CC5HGX48K51gBT1FOISqxAzz9DbFSVIK16BvzyVdYKg1nBR52VWo5HyfYDEclPwN-sRJRjqK0fBxY8wFC5mg1vtKAyldRmkmoSX5t-_8B3a94sWsovJb66JrczLsAIfdKXhIsmPcO-VzTdr9clCL5n5lBjj2EbQl-8u1wJoCqo0lUP4fcdkBQrrjibKPkm8HJn9t4L6aeBns6o5f1DiTG7XVGJqnGsQDymn6SFCpocj2EzwoWTDm6C242iN78MfBlZ45eYSdz0G0ctxG3CDXEn3h6WVMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت دفاع اسرائیل و شرکت البیت قابلیتی را برای افزایش برد پرواز جنگنده ادیر (F35) ایجاد خواهند کرد. این قرارداد که ارزش آن ۱۰۰ میلیون  تخمین زده می‌شود، شامل توسعه و تطبیق مخازن سوخت خارجی، بر اساس طرح موجود برای هواپیماهای F16، می‌شود.
🔴
تصویر اف۱۶ اسرائیلی با مخازن سوخت تطبیقی کنار بدنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119858" target="_blank">📅 10:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119857">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
عراقچی در نشست وزرای امور خارجه کشورهای عضو بریکس گفت که همان‌گونه که همگی شاهد بوده‌اید، کشور من طی کمتر از یک سال، دو بار هدف تجاوزی وحشیانه و غیرقانونی از سوی ایالات متحده و اسرائیل قرار گرفته است.
🔴
حقیقت آن است که ایران، همانند بسیاری از کشورهای مستقل،…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/alonews/119857" target="_blank">📅 10:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119856">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgAhEYd29MRiQVFF4_cgDcuZXbmoaE2sSZAayaxMwdiKyxZq3Xfq0pbtFiBXF60U5tNdGwKcBGRiT0_Aim8BmnzLFxCSFRKops6j_RB84K7R200u-OI7zYs6YjX_M3AJ4yiYOk6fj1qOjTsn-r6_1R9-iE1xY9LrP9PIkx-N0UUpszsk2wGT6fbYb0JFbWA6CLII9iuVdRO-77X3Ti40J6LJULkn-cuhB3wb-j7Ftn2uTXQUXKcEHvra81rydT__l3-IodlCrWyYzJdHjlSF6aTpCRh1Tv7DGh7Sv4mh4TeSowlwNxa52KFwefVT5PEYFgjyaYC2NmJM0_MSeYndcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش رویترز، ایالات متحده و چین توافق کردند که هیچ کشوری نباید اجازه داشته باشد عوارض حمل و نقل در تنگه هرمز را دریافت کند.
🔴
وزیر امور خارجه چین، وانگ یی، و وزیر امور خارجه ایالات متحده، مارکو روبیو، این موضوع را در تماس تلفنی آوریل مورد بحث قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/alonews/119856" target="_blank">📅 10:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119855">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
روبیو: چین باید برای مهار بحران ایران نقش فعال‌تری بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/alonews/119855" target="_blank">📅 10:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119854">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5f0f6e39.mp4?token=qSXCH1cNQpvKTQqZ5x7mmoa26qqfFyk2UKOEzXnlyi1E-dNqrCh_xd6AH9REwnQ2atlhxlW_lotmCi8d5EszcWNlZT-6-U_P-Ng3qaC1UXs9rSgjES066AbU80CGoMxgucee-IaU41w_ISkqMLpOJ9ki3-dIRt4k8cv9crzbWmuCyOEg1OIKmkHOUmk8kjFmCb9TiLT-0f-5XE-hZt0rbgvHMW5DsGZb9FiSenZtUc57YL0rk7_DIRkdlnSVjzMHOfdkcEIkAmlv_nUGpXkSwn7wD-5JEjCNsV_xj6r-pLfxtCRNXLkDvtvLG6CTPEaIK_tch8goqHeGMic8EJYnQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5f0f6e39.mp4?token=qSXCH1cNQpvKTQqZ5x7mmoa26qqfFyk2UKOEzXnlyi1E-dNqrCh_xd6AH9REwnQ2atlhxlW_lotmCi8d5EszcWNlZT-6-U_P-Ng3qaC1UXs9rSgjES066AbU80CGoMxgucee-IaU41w_ISkqMLpOJ9ki3-dIRt4k8cv9crzbWmuCyOEg1OIKmkHOUmk8kjFmCb9TiLT-0f-5XE-hZt0rbgvHMW5DsGZb9FiSenZtUc57YL0rk7_DIRkdlnSVjzMHOfdkcEIkAmlv_nUGpXkSwn7wD-5JEjCNsV_xj6r-pLfxtCRNXLkDvtvLG6CTPEaIK_tch8goqHeGMic8EJYnQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تحت تأثیر قرار گرفتن مارکو روبیو از سقف و چراغ‌های داخل تالار بزرگ محل دیدار ترامپ و شی
🔴
حرکات او مورد توجه رسانه‌ها قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119854" target="_blank">📅 10:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119853">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/862de39cb2.mp4?token=YEf-hgVymQZfT8tSoMD_SzeKXkS11IZamHLPkP5YudObSRMcWP0HJOsoEdfQqdANgXGRbX22Llli7iQfpB0s6BvRSvUlOz6yLM-PwGcNCenZl22BeX2Dvi1DxqCBFri3ZtB8UX2bcQAxDugbKHv8IRHVljB_s1-ni0r7vOMctqKRUGtiF0lMpZcPSZDQqyUo3LqSWs0HlpMdz2b4p4fPiD-dl3lTmD8awXIvc_R5TuMp6yRtcTkplke6xRkheBnYnlOgXl2Y9TW33uZlGUk9tVWZByvrSrnDjN0Wxz7qLNM_DK6wkINyN3ooFvX8-nJamv2SGmbUNURhsV39PsGcIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/862de39cb2.mp4?token=YEf-hgVymQZfT8tSoMD_SzeKXkS11IZamHLPkP5YudObSRMcWP0HJOsoEdfQqdANgXGRbX22Llli7iQfpB0s6BvRSvUlOz6yLM-PwGcNCenZl22BeX2Dvi1DxqCBFri3ZtB8UX2bcQAxDugbKHv8IRHVljB_s1-ni0r7vOMctqKRUGtiF0lMpZcPSZDQqyUo3LqSWs0HlpMdz2b4p4fPiD-dl3lTmD8awXIvc_R5TuMp6yRtcTkplke6xRkheBnYnlOgXl2Y9TW33uZlGUk9tVWZByvrSrnDjN0Wxz7qLNM_DK6wkINyN3ooFvX8-nJamv2SGmbUNURhsV39PsGcIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارش خبرنگار فاکس‌نیوز از ربات فروشنده در چین و درخواست خرید سوسیس از این ربات
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119853" target="_blank">📅 10:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119852">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عراقچی در نشست وزرای امور خارجه کشورهای عضو بریکس گفت که همان‌گونه که همگی شاهد بوده‌اید، کشور من طی کمتر از یک سال، دو بار هدف تجاوزی وحشیانه و غیرقانونی از سوی ایالات متحده و اسرائیل قرار گرفته است.
🔴
حقیقت آن است که ایران، همانند بسیاری از کشورهای مستقل، قربانی توسعه‌طلبی غیرقانونی و جنگ‌افروزی شده است. این‌ها پدیده‌هایی زشت هستند که هیچ جایگاهی در جهان امروز ندارند.
🔴
همان‌طور که بارها تأکید کرده‌ام، هیچ‌گونه راه‌حل نظامی برای هر موضوعی که به ایران مربوط باشد وجود ندارد. ما ایرانیان هرگز در برابر هیچ فشار یا تهدیدی سر خم نمی‌کنیم، اما به زبان احترام پاسخ متقابل می‌دهیم.
🔴
هرچند نیروهای مسلح قدرتمند ما آماده‌اند پاسخی کوبنده و ویرانگر به متجاوزان خارجی بدهند، اما مردم ما صلح‌طلب هستند و خواهان جنگ نیستند. در این وضعیت شرم‌آور، ما متجاوز نیستیم؛ بلکه طرفی هستیم که مورد ظلم و تجاوز قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/alonews/119852" target="_blank">📅 09:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119851">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b9f713d53.mp4?token=do3Qqtk23H6neH_B6AQhCQScC5YjIXOALDc8sC5XnucfOvludOL7r0zie8AaAhBlDVdwRHLdEXiAM6lCX8TgRBHkpEFYEjWe_zbxHlKZie2eFDpypyjeZSLYea-rfI3rnZhvl8yLSjh62hcq_qgb-rYM_7gM4K0_3XUs33QG3nIueNxYbPW5O9bKuu6EZdACr1-GuXqONNwK1I10QmyxaknwF0vhDxJnPk5dYsDzNxUvq2f5ZzAmqUTO9YlWWKXtt31I3ecWB1IhIkK_RJzMlg0_SGjGGi-g8Qz8aUX5AZq2YsKL56DJd6NT7hWQXdgQ3Dn9XXSlZAy83efgicntSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b9f713d53.mp4?token=do3Qqtk23H6neH_B6AQhCQScC5YjIXOALDc8sC5XnucfOvludOL7r0zie8AaAhBlDVdwRHLdEXiAM6lCX8TgRBHkpEFYEjWe_zbxHlKZie2eFDpypyjeZSLYea-rfI3rnZhvl8yLSjh62hcq_qgb-rYM_7gM4K0_3XUs33QG3nIueNxYbPW5O9bKuu6EZdACr1-GuXqONNwK1I10QmyxaknwF0vhDxJnPk5dYsDzNxUvq2f5ZzAmqUTO9YlWWKXtt31I3ecWB1IhIkK_RJzMlg0_SGjGGi-g8Qz8aUX5AZq2YsKL56DJd6NT7hWQXdgQ3Dn9XXSlZAy83efgicntSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ناتو: من از ناتو حمایت کردم زیرا به ما اجازه داد تا پایگاه‌هایی در اروپا داشته باشیم که می‌توانیم در شرایط اضطراری، مانند اتفاقی در خاورمیانه، از آن‌ها استفاده کنیم.
وقتی شرکای ناتو اجازه استفاده از آن پایگاه‌ها را به ما نمی‌دهند، پس هدف این اتحادیه چیست؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/119851" target="_blank">📅 09:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119850">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62b70355a.mp4?token=tm7Mkh2PWKFK2d1WEiXFjKakYNyMlF-0SMr2ki0N70GlIsy9VjRm7et55tAktceDyRfSzDO6yHLcK9f7PB9J-oGVJ24xG5CFT0UWsCyODglCOmuylOO0EkMQhAuMiGHDkxqCmp6ncNH3W3vD9ouWJwkLlGzDz0Su1V-y4ZMIKZDNq7yjMojDPKu9PF0LFDGzdjFA0F2y7DvwrGpIsYrNh0hESci-ABTq1_lygFPv4tOfX2l0VSPNQl9Y850GtdVgQPSGdUEoygFE4b8mgQQKQ2FDk8WBwQFc-JLcf5kfFU5inUURHURZHgW6Zn2RqPeoV6iJvhiFxUYPzPZ8t9SIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62b70355a.mp4?token=tm7Mkh2PWKFK2d1WEiXFjKakYNyMlF-0SMr2ki0N70GlIsy9VjRm7et55tAktceDyRfSzDO6yHLcK9f7PB9J-oGVJ24xG5CFT0UWsCyODglCOmuylOO0EkMQhAuMiGHDkxqCmp6ncNH3W3vD9ouWJwkLlGzDz0Su1V-y4ZMIKZDNq7yjMojDPKu9PF0LFDGzdjFA0F2y7DvwrGpIsYrNh0hESci-ABTq1_lygFPv4tOfX2l0VSPNQl9Y850GtdVgQPSGdUEoygFE4b8mgQQKQ2FDk8WBwQFc-JLcf5kfFU5inUURHURZHgW6Zn2RqPeoV6iJvhiFxUYPzPZ8t9SIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو درباره ترامپ: او مایل است کاری را انجام دهد که دیگران درباره آن صحبت می‌کنند اما انجام نمی‌دهند.
🔴
وقتی می‌گویید: «خب، نمی‌توانیم آن کار را انجام دهیم»، او می‌پرسد: «چرا؟» او مایل است کارهای ناتمام را حل کند و آن‌ها را برای نفر بعدی، مرد یا زن، باقی نگذارد.
🔴
بخشی از آن بودن بسیار لذت‌بخش است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/alonews/119850" target="_blank">📅 09:44 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119849">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddca6e481.mp4?token=axNxRFntfM1ZmmfWry84sKQrkaNXmHuTBSElwh1iqRw6DSc8IS7cKGKHD1BoI2qlrfeAtVQGdt_B2tEFee-jbWN92753BcYHMeeKne2W9i-fwHNdjBM99YAysiIdfKIW0Og3kswD7-DhgioiotPn9X-nbk0sljAZ_-OYLswPomp_3yZlanddfwNSHB_qFrCig_E9PCNRXNFWQAbkTxR9Uf52ec3M4N4pdZ_hm-FBl4vo7fvaeJWKB981s4_nWL7STAq7-naeRtbJKp1caUlSYVsI3FIjRZM-9X8gCH45JDVgz3eJJTF2Xi5-OF51jhcPFvb0xvGsV3wKqkHfVFgJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddca6e481.mp4?token=axNxRFntfM1ZmmfWry84sKQrkaNXmHuTBSElwh1iqRw6DSc8IS7cKGKHD1BoI2qlrfeAtVQGdt_B2tEFee-jbWN92753BcYHMeeKne2W9i-fwHNdjBM99YAysiIdfKIW0Og3kswD7-DhgioiotPn9X-nbk0sljAZ_-OYLswPomp_3yZlanddfwNSHB_qFrCig_E9PCNRXNFWQAbkTxR9Uf52ec3M4N4pdZ_hm-FBl4vo7fvaeJWKB981s4_nWL7STAq7-naeRtbJKp1caUlSYVsI3FIjRZM-9X8gCH45JDVgz3eJJTF2Xi5-OF51jhcPFvb0xvGsV3wKqkHfVFgJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو
،
درباره ایران : مردم در برقراری این ارتباط مشکل دارند، اما این ارتباط بسیار واقعی است.
🔴
آن‌ها قصد داشتند آن‌قدر پهپاد و موشک داشته باشند که هیچ‌کس نتواند به ایران حمله کند، زیرا نتیجه آن برای منطقه فاجعه‌بار خواهد بود.
🔴
به محض اینکه آن‌ها به این مصونیت رسیدند، به سمت دستیابی به سلاح هسته‌ای می‌شتافتند. دونالد ترامپ اجازه نخواهد داد که این اتفاق در دوران ریاست‌جمهوری او رخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/alonews/119849" target="_blank">📅 09:42 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119848">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مارکو روبیو درباره کوبا: این کشوری است که مردم در آن به طور واقعی زباله‌ها را از خیابان‌ها می‌خورند.
🔴
کوبا نباید کشوری فقیر باشد.
🔴
کوبایی‌ها از کوبا می‌روند و به کشورهای دیگر می‌روند و موفق می‌شوند.
🔴
تنها جایی که کوبایی‌ها به نظر نمی‌رسد بتوانند شکوفا و موفق شوند، خود کوبا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/alonews/119848" target="_blank">📅 09:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119847">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0816ff7f7.mp4?token=nAO_T0-dGscvuDrm4Uvo8lvmpYEMVM1UUPD4FvAXDCDxgtMTE2c4_rqYXw281IcG7cczogdWNoqUiFdwFqv5JwS9B-CjHJIliEHjwrzWuVC4ua6swoXoymtj0o4iQaqgRg22zHgasKhIoXPtP_L88mgot5Lm4PkoxyJTtEmqDDQcUGJ1WXNAb0MEOTGGnOe5uWKX9rBkPkO3xzHfF7iU_dmVX7ieiNo1c30WrmHEgl6MBCMeGo50L5sRVI1HJELn1eoZPKXoNm6xfbcN4MvrmK5JGQMawn7vCp0ZSMnAmp3gddPaulYxYDlohUFhB-vwNmPfjQpSQsKKJP4zH0VYoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0816ff7f7.mp4?token=nAO_T0-dGscvuDrm4Uvo8lvmpYEMVM1UUPD4FvAXDCDxgtMTE2c4_rqYXw281IcG7cczogdWNoqUiFdwFqv5JwS9B-CjHJIliEHjwrzWuVC4ua6swoXoymtj0o4iQaqgRg22zHgasKhIoXPtP_L88mgot5Lm4PkoxyJTtEmqDDQcUGJ1WXNAb0MEOTGGnOe5uWKX9rBkPkO3xzHfF7iU_dmVX7ieiNo1c30WrmHEgl6MBCMeGo50L5sRVI1HJELn1eoZPKXoNm6xfbcN4MvrmK5JGQMawn7vCp0ZSMnAmp3gddPaulYxYDlohUFhB-vwNmPfjQpSQsKKJP4zH0VYoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به سوال خبرنگار درباره تایوان پاسخ نداد
🔴
خبرنگار از ترامپ می‌پرسد: مذاکرات چطور پیش رفت؟
🔴
ترامپ: عالی، چین زیباست.
🔴
خبرنگار: درباره تایوان صحبت کردی؟
🔴
ترامپ جواب نمی‌دهد.
🔴
خبرنگار تکرار می‌کند: درباره تایوان صحبت کردی؟
🔴
ترامپ جواب نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/alonews/119847" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119846">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
نخست‌وزیر ژاپن از عبور یک کشتی ژاپنی دیگر از تنگه هرمز خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/119846" target="_blank">📅 09:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119845">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
کیفرخواست زیباکلام و مدیرمسئول خبرگزاری آنا صادر شد/ ممنوعیت زیباکلام از انجام هرگونه فعالیت رسانه‌ای به مدت سه ماه
🔴
هفته گذشته و در پی مصاحبه صادق زیبا کلام با خبرگزاری آنا (برنامه پل حافظ)، دادستانی تهران علیه نامبرده و رسانه منتشرکننده اظهارات وی اعلام جرم کرد.
🔴
پس از تشکیل پرونده قضایی برای نامبردگان، متهمان به مرجع قضایی مراجعه کردند و پس از اخذ دفاعیات، تفهیم اتهام شدند.
🔴
در نهایت با توجه به مستندات و تحقیقات صورت‌گرفته قرار جلب به دادرسی و کیفرخواست پرونده صادر شد.
🔴
همچنین قرار نظارت قضایی ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی به مدت سه‌ماه به صادق زیباکلام تفهیم و ابلاغ شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/alonews/119845" target="_blank">📅 09:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119844">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
رویترز به نقل از شی جین پینگ: در جنگ تجاری هیچ برنده‌ای وجود ندارد؛ هر دو طرف به نتایج مثبتی دست یافته‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/119844" target="_blank">📅 09:18 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119843">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ در پاسخ به سوالی درباره مذاکرات با شی جین‌پینگ گفت: «عالی است»
🔴
ترامپ در پاسخ به سوال خبرنگار هنگام بازدید از معبد بهشت در پایتخت چین گفت: «عالی است».
🔴
ترامپ گفت: «جای فوق‌العاده‌ای است. باورنکردنی است. چین زیباست.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119843" target="_blank">📅 09:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119842">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
شی‌جین پینگ: تایوان مهم‌ترین مسئله در روابط چین و آمریکا است
🔴
رئیس‌جمهور چین، در جریان گفت‌وگو با دونالد ترامپ، تایوان را «مهم‌ترین مسئله در روابط چین و آمریکا» خواند
🔴
شی تأکید کرد که اگر این مسئله «به درستی» مدیریت شود، دو کشور می‌توانند از یک رابطه باثبات بهره‌مند شوند، اما در غیر این صورت، «دو کشور دچار تنش و حتی درگیری خواهند شد و کل روابط را در معرض خطر قرار خواهند داد»!
🔴
وی همچنین افزود که استقلال تایوان و صلح در تنگه تایوان «به اندازه آتش و آب ناسازگارند»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/alonews/119842" target="_blank">📅 09:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119841">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شی‌جین‌پینگ به ترامپ: تمام جهان در حال تماشای دیدار ما است.
🔴
آیا می‌توانیم، به نفع رفاه دو ملت‌مان و آینده بشریت، آینده‌ای روشن‌تر برای روابط دوجانبه‌مان بسازیم؟
🔴
در حال حاضر، تحولی که در یک قرن دیده نشده بود در سراسر جهان در حال تسریع است و وضعیت بین‌المللی سیال و پرتنش است.
🔴
جهان به یک چهارراه جدید رسیده است.
🔴
من همیشه معتقد بودم که دو کشور ما منافع مشترک بیشتری نسبت به تفاوت‌ها دارند.
🔴
موفقیت در یکی فرصتی برای دیگری است و یک رابطه دوجانبه پایدار برای جهان مفید است.
🔴
چین و ایالات متحده هر دو از همکاری سود می‌برند و از تقابل زیان می‌بینند. ما باید شریک باشیم، نه رقیب.
🔴
باید به یکدیگر کمک کنیم تا موفق شویم، با هم شکوفا شویم و راه درست برای کنار آمدن کشورهای بزرگ در عصر جدید را بیابیم.
﻿
🔴
ترامپ به شی جین پینگ: تو یک رهبر بزرگ هستی. من این را به همه می‌گویم که تو یک رهبر بزرگ هستی. گاهی اوقات مردم دوست ندارند من این را بگویم، اما من به هر حال می‌گویم چون حقیقت دارد.
🔴
من فقط حقیقت را می‌گویم
🔴
ترامپ به شی جین پینگ: افتخار است که با شما هستم. افتخار است که دوست شما باشم، و رابطه بین چین و ایالات متحده بهتر از همیشه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/alonews/119841" target="_blank">📅 09:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119840">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: چین تمایلی برای کاهش حمایت از ایران در برابر آمریکا ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/alonews/119840" target="_blank">📅 08:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119839">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
یک منبع امنیتی عراقی به شبکه العربیة: دو پهپاد حامل مواد منفجره، مقر یک حزب مخالف دولت ایران را در شمال اربیل هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/alonews/119839" target="_blank">📅 08:54 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119838">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a81f9fc6.mp4?token=m4BOga-seQqnqsXXRfN9C68yltYobMfQqJV2njxNGx7_9Wg2m-PrTWltcipcHix5YsSClcwnrL3mSFXdHmLT_g4OpcisjpypBnFuaG5SGaaKAvmrJ0j6nylO74NfebiRmFTa1CU-xCwGcICwSWLocGmHcgCcLRhmJ4mQifzMQTEjxrbUHMAgOkyUIwpeUry76w1oqwVuGGWDoG5vQcYl8LpVoj4B0_CRpV0NpkAWw7fe-f1xyBZG_cr6UdbbqxgaXAq_vtuIDJ216WGrLTdYx-AHEl8QrLsTqTcIneOVjV-patSh7lC-XY5QitLN86LXXexND4aamqbmTPGKz_K9uTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a81f9fc6.mp4?token=m4BOga-seQqnqsXXRfN9C68yltYobMfQqJV2njxNGx7_9Wg2m-PrTWltcipcHix5YsSClcwnrL3mSFXdHmLT_g4OpcisjpypBnFuaG5SGaaKAvmrJ0j6nylO74NfebiRmFTa1CU-xCwGcICwSWLocGmHcgCcLRhmJ4mQifzMQTEjxrbUHMAgOkyUIwpeUry76w1oqwVuGGWDoG5vQcYl8LpVoj4B0_CRpV0NpkAWw7fe-f1xyBZG_cr6UdbbqxgaXAq_vtuIDJ216WGrLTdYx-AHEl8QrLsTqTcIneOVjV-patSh7lC-XY5QitLN86LXXexND4aamqbmTPGKz_K9uTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیدار شی جی پینگ و دونالد ترامپ
🔴
دونالد ترامپ با ورود به محوطه تالار بزرگ خلق، با شی جینگ پینگ دیدار کرد و قرار است گفت‌و‌گوی دوجانبه انجام شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/119838" target="_blank">📅 08:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119837">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f65176faa.mp4?token=UykVGo_gKhi0qKJV29a8Jo0-IF3BIWN7JR3BSQN5N24fE9lulZKILLLlP03VbNh_z-iErV7T_wq1nj2oiAtO1Vx8HrfUKsGzxr049V_nw2yUZluDEwzHOtVwAiXP7kq7L5cGe7B91Ldu11HUb0brrvRst-9j9-AYbEyZDcaSjlg-ReNawsbFtwC0W_NCS4ZE5mrTlVkCqx21D_nDeL2wMK7VDyeOH06IXCakzf8Lf9HYzcPk5hJ-eMZTPbfiGj3jF3piprpKkOWcDKST6Ftsv5hsLu6Llhdo8kx2jMgNEZcNob6LMeep4CVFqkABE-GB66gOEnpZHG9CnpqWtG8BWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f65176faa.mp4?token=UykVGo_gKhi0qKJV29a8Jo0-IF3BIWN7JR3BSQN5N24fE9lulZKILLLlP03VbNh_z-iErV7T_wq1nj2oiAtO1Vx8HrfUKsGzxr049V_nw2yUZluDEwzHOtVwAiXP7kq7L5cGe7B91Ldu11HUb0brrvRst-9j9-AYbEyZDcaSjlg-ReNawsbFtwC0W_NCS4ZE5mrTlVkCqx21D_nDeL2wMK7VDyeOH06IXCakzf8Lf9HYzcPk5hJ-eMZTPbfiGj3jF3piprpKkOWcDKST6Ftsv5hsLu6Llhdo8kx2jMgNEZcNob6LMeep4CVFqkABE-GB66gOEnpZHG9CnpqWtG8BWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جریمه سنگین دوربین‌های نظارتی چین برای مجری فاکس‌نیوز / برت بایر:
🔴
”به معنای واقعی کلمه همه جا دوربین وجود دارد.آنها همه چیز را می‌بینند... راننده ما به مدت ۲ دقیقه غیرقانونی پارک کرده و ۴۰ دلار جریمه شده است!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/alonews/119837" target="_blank">📅 08:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119836">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laioWWpUIMghNHqfONyCrHYhL9gVblu1Yjx4Dn6TFAUTSc2EX0f4Y48mjw_U8T9jVzqScGRYZ-xoM0pnkxZ0CsJCo0if93K2CzrmBz0oaF1bQD7L_uXqAi_X8xfgGM6RfjUpwydBZ904BxAfR71VC49tiWT7fW3AoTUtIi3oIqECjQK9Li6j0sAVYs2okfKpt30bz9_HAAoI18fIqxzvuigQfSckkRbB84YCfM4LqH7CnqtBEagU2YmfjJRufLg-FpOH_D0lB-zAvX838rsmD-b5Ksxj_2h1sKsHqsGs8nNDAbszuJOlaxhCwEcB9n_t8Vi6nu3X-BgR4aSmg_q0NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معین: مهدی تاج الکی میگه، من قرار نیست هیچ آهنگی واسه تیم فوتبال تو جام جهانی بخونم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/alonews/119836" target="_blank">📅 02:41 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119835">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGMOsdY1F7Xks2xzp7_pgRVZAJWK8KHqAE5We9dl_4kx9fVBhqBwpBDbqNaFYN8nCeLxVfvn_EI_8QEO68r97crHcMInsYvgVNNh8BwrXf5Zfz3YdKifPCG03q0le2EeEPj8oxliHYz5eXqZeaLijtMw0tyI1rAgJ-hFBYj7gCJpPbp9wHsr-uOk2BdBTbv5OLKeBTcO1PXiJxy247wSh-cwDKB0nbBq5PybKHErbyXd76y4zKyus4t9oGfhpx_0wzsp3T_wCjXRZEd7Kb9wCpiTK1w_z4IIIHh6qouxDZaf8fJ8aed4kyGa9si1Jj_okX79HUAp9X-Cr8niEKcR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش رویترز، ایالات متحده و چین توافق کردند که هیچ کشوری نباید اجازه داشته باشد عوارض حمل و نقل در تنگه هرمز را دریافت کند.
🔴
وزیر امور خارجه چین، وانگ یی، و وزیر امور خارجه ایالات متحده، مارکو روبیو، این موضوع را در تماس تلفنی آوریل مورد بحث قرار دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/alonews/119835" target="_blank">📅 01:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119834">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ارتش اسرائیل: مدتی پیش حزب‌الله لبنان از جنوب این کشور با پهپاد و چندین موشک ضدتانک بهمون حمله کرد که هیچکس آسیبی ندید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/119834" target="_blank">📅 01:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119833">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ef57f203e.mp4?token=FItVs7JvBW30N55mW_TPfatTHyMh4B32m6gVRUF05MBaEODG8SIux-lm2NujvZCw8KxobkXN_WZEunbxI0C0b2A9pZM2rgt1DYVuh0-m4dFUF7Mg0WjMEfyrXBWScQ33vPKGKNkw0YSuzZwiDSbaPxXVld3NJWJfGkwEXVlZuYX4Wemdsa8S_ixJgZUk_Q_bcSgZHd82OqQCSoQ2RbQfRLLYjyBwWWfnKCuNXrFGjZH-iIFUtbVfxXZpUsJNN5MCsxiA2Fc5ndsIt1w-lMMLoovgYYOYttkZSKzBrYQMwEwyVcrvcy2uasCRFe7hKppy9n4pQUCSpuhrvDz1yYuSHRAV3k03EYSBUVa1vQYXC86HeW5gXO5jooJOAYwJdKm-AnyQfltd45DDKDU1ReN0eKociWvOZzfcYHviFa7Al6XdY_g8vD_R-l35nE9Mj1QrcsmvKFvBPgAHwmlWxHLp6Yn7WZcD0yHjGCPwShtE630IVpfwp3u9QHCijsLOoEQyOpLteKw3bKB6khMX6u1yEFN7Sc9V_9xSflezEkEMDJz-8-df0SV11MgPQuRt30QlmFt5lmwc2PPi5R8HFI4MLCcBFpq9U_dOsh8sQQqhMvxFbBHfiUdSNVL2AGHbez5_cGBhY_HMkl8TsRfdKLJJmFjMiIMK0wAEgiwk2_xq-uY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ef57f203e.mp4?token=FItVs7JvBW30N55mW_TPfatTHyMh4B32m6gVRUF05MBaEODG8SIux-lm2NujvZCw8KxobkXN_WZEunbxI0C0b2A9pZM2rgt1DYVuh0-m4dFUF7Mg0WjMEfyrXBWScQ33vPKGKNkw0YSuzZwiDSbaPxXVld3NJWJfGkwEXVlZuYX4Wemdsa8S_ixJgZUk_Q_bcSgZHd82OqQCSoQ2RbQfRLLYjyBwWWfnKCuNXrFGjZH-iIFUtbVfxXZpUsJNN5MCsxiA2Fc5ndsIt1w-lMMLoovgYYOYttkZSKzBrYQMwEwyVcrvcy2uasCRFe7hKppy9n4pQUCSpuhrvDz1yYuSHRAV3k03EYSBUVa1vQYXC86HeW5gXO5jooJOAYwJdKm-AnyQfltd45DDKDU1ReN0eKociWvOZzfcYHviFa7Al6XdY_g8vD_R-l35nE9Mj1QrcsmvKFvBPgAHwmlWxHLp6Yn7WZcD0yHjGCPwShtE630IVpfwp3u9QHCijsLOoEQyOpLteKw3bKB6khMX6u1yEFN7Sc9V_9xSflezEkEMDJz-8-df0SV11MgPQuRt30QlmFt5lmwc2PPi5R8HFI4MLCcBFpq9U_dOsh8sQQqhMvxFbBHfiUdSNVL2AGHbez5_cGBhY_HMkl8TsRfdKLJJmFjMiIMK0wAEgiwk2_xq-uY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاج: احتمالا معین موزیک رسمی تیم‌ملی رو بخونه!
@AloSport</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/119833" target="_blank">📅 01:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119832">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1rat1eX10Z2GoF87sQURJWEHKbmrGKGDGKH7cBoHfCSvjW8WlZmuXn7FKELaw7lxVCSm-1FxWkOoN5STv8Q6rMTRyRdZZiUtHhR8ywohG9SsDWwezDFg1dajW55UeAGg1K1M7U1EcL5fU70CUWRaJIbA4Uv3145Hr3bewrNnZTV6Zxpcry8wG1bzH-PeMg1Rdmc8Rl1RDpl3Jdnx9s-G8s1uoIQhi9ioh34743BL0tmOfzRjH1nsZbcvHQIhDKZHY6a84O5eBZMMnsp1zKNlLqMXmpyi6Tm14qbdHQEsBBTw5Sv9JpWbbtMgHVfDI_XZ6TusiNcQipYIUrSsmIJLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا "نصرالله معین" قراره واسه تیم ملی فوتبال به مناسبت حضور تو جام جهانی 2026، آهنگ بخونه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/alonews/119832" target="_blank">📅 01:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119831">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1278f5774c.mp4?token=AWnC8IpbSv-YUgUbcAFYQWiTCzXf-5FeNUmJWmL44lfFZnNIFN3_M8_FTS8wkTHo7q3L0fXX9zfHk3WCktgfWSHAJocsj-KLfU5qF-0ysZXTcaOQfIkqU0hAccA6AXC_a-7FWEkytbxWu3fcdIaMj2mH-lH0KsPOOkVQM4JW-zSBvhXLwOBFBLrj8eVK4Q4ZW9XsftK-qS2j_hhFNQT24f-4L1a_yoRnwBW8Trrf_87g_ANe-b7VCFjl9CimEfaJWt2P_YuCG6aICaszYxuqzHMpEOXn-LN6_uSXHQb81KaRCdAfsP4Wo_UbnkP53NkSGZhTQSgo3_lSBdIW8pAdKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1278f5774c.mp4?token=AWnC8IpbSv-YUgUbcAFYQWiTCzXf-5FeNUmJWmL44lfFZnNIFN3_M8_FTS8wkTHo7q3L0fXX9zfHk3WCktgfWSHAJocsj-KLfU5qF-0ysZXTcaOQfIkqU0hAccA6AXC_a-7FWEkytbxWu3fcdIaMj2mH-lH0KsPOOkVQM4JW-zSBvhXLwOBFBLrj8eVK4Q4ZW9XsftK-qS2j_hhFNQT24f-4L1a_yoRnwBW8Trrf_87g_ANe-b7VCFjl9CimEfaJWt2P_YuCG6aICaszYxuqzHMpEOXn-LN6_uSXHQb81KaRCdAfsP4Wo_UbnkP53NkSGZhTQSgo3_lSBdIW8pAdKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو : کشتی‌های چین توی خلیج فارس گیر افتادن  یه کشتی باری چینی هم آخر هفته آسیب دیده
- مطمئنم ایران عمداً این کار رو نکرده، ولی به هر حال اتفاق افتاده،واسه همین این کشتی‌های چینی اونجا گیر کردن
- این وضعیت خیلی بی‌ثبات‌کننده‌ست،حتی بیشتر از هر جای دیگه دنیا می‌تونه آسیا رو به هم بریزه، چون انرژی‌شون خیلی به این تنگه‌ها وابسته‌ست
- این به نفع خود چینه که این مسئله رو حل کنه
- ما امیدواریم بتونیم قانع‌شون کنیم نقش فعال‌تری بازی کنن تا ایران رو وادار کنن از کاری که الان تو خلیج فارس داره انجام می‌ده عقب‌نشینی کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/119831" target="_blank">📅 01:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119830">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
کانال N12: ترامپ داره به صدور دستور برای از سرگیری درگیری با ایران فکر می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/119830" target="_blank">📅 00:47 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119829">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bhSMLHvFxSthf1fPIcvsuC7_ZS5MyAssQxki_rX9HVXBvfJYqR_8w34LlWTQmd0A3XGcz2_R3G9XfJgul3xrr-GKPoHWcpfYVwgNfaOE2uqjvnVkZ9wF1eX0589CaIwOqXAJ2VkxE9OgZA_9MVUz8iVXYY6YJp8eWcr0wcH4VDjsVtvjFSEbs1RodWjQyaEhJmt5rL9wtWnvXid16faZOkMSsCFISApyBtmKafQSSE0f46-qpfy3oc_yO_bWOP-WSNDfoQI8f8x91fFv151D0uvkMP3GNA318ARYAHQbuYal7SmHPle__9QRKRhAtdletskqagUk5lFhuYodSxjhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خیلی شیک و‌ مجلسی روی شیشه دفاتر پیشخوان آگهی فروش اینترنت پرو میزنن که تلگرام هم روش بدون فیلتره.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/alonews/119829" target="_blank">📅 00:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119828">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
مدیرعامل شهر فرودگاهی امام : روزانه بین ۳۵ تا ۴۰ پرواز از فرودگاه انجام می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/119828" target="_blank">📅 00:29 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119827">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
خوش‌چشم: ترامپ رفته چین التماس کنه تا میانجی بشه که ایران جنگ رو تموم کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/119827" target="_blank">📅 00:28 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119826">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a20b6d8ff5.mp4?token=ODEv7Qt42ViDa6mvHHQZjzyqC5ugPbiBX36w30VqSyEnmi8I21-qsNJGGG7cU27Xc2f-2blwweaMxikqxA0_7V2x_des85q4dHEi1vPobsgQuHayPlX7mn52mfVE_c52u9Kr2TlfeyY9blxYjtCtC7qdWA_aNFZSsK-axBI6V1MbanzS2HGIjCDI_ETxuGcbmkJNIG9YCPTWIFAvecYqSTi1MYTdHCqQiGN_O2a0b0p6YVa3am-ZPWsFMoCU8JGmvwJ7HXHl3UlN5uIVNBkJicu3Sb4d7MJqC_3wbIjDOII3KLyjAjzsfiX9v_IZ52K-0Z_3QTL_BMNK7BEel2YtUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a20b6d8ff5.mp4?token=ODEv7Qt42ViDa6mvHHQZjzyqC5ugPbiBX36w30VqSyEnmi8I21-qsNJGGG7cU27Xc2f-2blwweaMxikqxA0_7V2x_des85q4dHEi1vPobsgQuHayPlX7mn52mfVE_c52u9Kr2TlfeyY9blxYjtCtC7qdWA_aNFZSsK-axBI6V1MbanzS2HGIjCDI_ETxuGcbmkJNIG9YCPTWIFAvecYqSTi1MYTdHCqQiGN_O2a0b0p6YVa3am-ZPWsFMoCU8JGmvwJ7HXHl3UlN5uIVNBkJicu3Sb4d7MJqC_3wbIjDOII3KLyjAjzsfiX9v_IZ52K-0Z_3QTL_BMNK7BEel2YtUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تمرینه بمب‌افکنِ " B-52 " و فرود به پایگاه فِرفورد بریتانیا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/119826" target="_blank">📅 00:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119825">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LOrtpSx4S971AszgyOQKsute6mPnTb0hWYVPNZ9K1PGQUqg7l6AqnrB6rgnpdS4HPvqd-V11j2e9oY9bbIYCv4TYNsyxPWVFFPUE39JOu6GIs-Y74hKnRCgdfbaY0QHsQB3_WQgcrqgt6-XXNlMSqo_JjyvYi52NWVmmh4VvFOpzNV6mfdetqporNvoN4xic9XL0AB4_JBXzB47a4wCggTTE3H_JZgcobdP5VY-srL6dM2xCyo39jpsayug38YpL0wd5xWeFzDARkI2eJQkI04Vsi2GwmC83ij0Bl5swmwEcYJe-L0EcosdpfMNis02sKGWKlBNmVBD-Ii6UMV1q4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بابک زنجانی: در تاریخ ۲۸ خرداد، شبکه اجتماعی مای دات به‌صورت فراگیر برای عموم بازگشایی و طی مراسمی در برج میلاد رونمایی خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/119825" target="_blank">📅 00:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119824">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
روزنامه South China Morning Post: شرکت تصاویر ماهواره‌ای چینی MizarVision که با تحلیل‌های خود از استقرارهای نظامی آمریکا در جنگ آمریکا و اسرائیل علیه ایران به شهرت رسید، افزوده شدن خود به فهرست تحریم‌های آمریکا را به عنوان نشان افتخاری در کمپین استخدامی خود به کار می‌برد.
🔴
این استارت‌آپ اطلاعاتی با منابع باز (OSINT) که با نام رسمی Meentropy Technology Hangzhou Co Ltd شناخته می‌شود، در تحلیل داده‌های ماهواره‌های تجاری تخصص دارد و در ماه‌های اخیر چندین بار تحرکات نظامی آمریکا را رصد کرده است.
🔴
این شرکت روز جمعه به فهرست تحریم وزارت خزانه‌داری آمریکا اضافه شد که در  پی انتشار «تصاویر با منبع باز که جزئیات فعالیت نظامی آمریکا را در جریان عملیات خشم حماسی (Epic Fury) نشان می‌داد»، صورت گرفته است
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/119824" target="_blank">📅 00:14 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119822">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TcxDA20UDG_J8alNVkSrS2RwxK9Q9u1pNjCSsESxJRvVxLQQSGKADwfjx8PaUGxJ5BiB3_BtBKHgMkworAgz3j7f8aSOtN97MGgvkIA8tHVERsJWdu1Bu4_sBCpTtuwoAjTp-NYvNjafn7d-qfoTTneiS-v3MC0ONGUZhZ3LY7BqlFWWoynQULq8qo56P0tHC6_hPVu8oowRcE7gqZeF3tQPug-2xOaXfV8GUIrqoO3UeqHCB-6U67grfniozoi-SuJm3QuEY-12wXJRkI_77FaQl_ZJ8YRaIX58IuCSowXSE_CZEO6MUxdVnWQnX9KVGH8WOu6e96If7dVuIB-GWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sPVoQMh_e85-Dl9UtHYdInxa4ya9xf3ZG9FRsHk9yIar1R8_cFa_vSC6oAVLV_up05YPZ4JTOoQ08EKz-o64uAHSLVFcp2L2TYTpyyIRT96Kvu9JNMF0ozzvXITZl54PYOk5iTF4YoZlCgo1h_Iqs-OtjoD7t6fLSlIVCWCWO6eaPkdD4L6m-Xai9uz965FLD_mAjDgwC11Iwa4SRGG5PuWRrCAcpZQkVYmmYfmqFf22DVNNiTTXpHmrEsz7PLXOqbb75cKGlYAiYiMErpv_YHBFiXDKMNxI36UosU-4gK9_B0ZDbsbWJaJEZ-V0KQFSXmDJOjLHYLMI6w9lHrgPYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هزینه نجومی رجیستری گوشی آیفون ۱۷ و گلکسی سامسونگ!
🔴
رجیستری پایین ترین گیگ آیفون ۱۷ پرومکس: ۶۰۰ دلار!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/119822" target="_blank">📅 00:10 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119821">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
امارات : خبرهایی که درباره سفر نتانیاهو به امارات پخش شده، صحت نداره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/119821" target="_blank">📅 00:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119820">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff5j2zs7YNFC9ednVUaGBLSUhiCuw3fgaQCuNnYvfjYfqKPNX_BE39ZIU89facKaK7XWO2BkP982OZ5UeRA8hU0U30EclCjdit4PJgYdxMMXRh6kCbjmePDYRi4DTq85xasWVo-qklKggnRpf8tR7vqTG58HW33Oqa_Lwcrc0CN39s9rKccXaDImGEnfsYHyW3ov3IrhWh6wVKbI6xkyTq8zu9ykgedDyQ111A0r6Ay6Zz4_Cle1JGmdi9pe0n5NhNEzBGeG4qjIIARDHCt__QskoQOqYmW0hv3dmbBXZnJxmXim_iin9WfapPFrx8Wvvk92KgX4zMqGobERbhFPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: نتانیاهو اکنون به‌صورت علنی آنچه را که نهادهای امنیتی ایران مدت‌ها قبل به رهبری ما منتقل کرده بودند، افشا کرده است.
🔴
دشمنی با ملت بزرگ ایران، قماری احمقانه‌ است؛ و همکاری و همدستی با اسرائیل در این مسیر، غیرقابل بخشش است.
🔴
کسانی که در همدستی با اسرائیل برای ایجاد تفرقه نقش دارند، باید پاسخگو باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/119820" target="_blank">📅 23:55 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119819">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وال‌استریت ژورنال: در حالی‌که نگرانی‌هایی درباره کاهش ذخیره مهمات ایالات متحده وجود دارد، پنتاگون در حال تلاش برای خرید ۱۰٬۰۰۰ موشک کروز کم‌هزینه در طول سه سال است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/119819" target="_blank">📅 23:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119818">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
وزارت خارجه ایالات متحده: امروز، وزارت خارجه به‌طور عمومی پیشنهاد سخاوتمندانه ایالات متحده برای ارائه ۱۰۰ میلیون دلار کمک بشردوستانه مستقیم اضافی به مردم کوبا را که با هماهنگی کلیسای کاتولیک و سایر سازمان‌های بشردوستانه مستقل و قابل اعتماد توزیع خواهد شد، مجدداً اعلام می‌کند.
🔴
تصمیم با رژیم کوبا است که پیشنهاد کمک ما را بپذیرد یا از کمک‌های حیاتی نجات‌بخش زندگی خودداری کند و در نهایت در برابر مردم کوبا به دلیل ایستادگی در برابر کمک‌های حیاتی پاسخگو باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/119818" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119817">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fdf0426b5.mp4?token=hah0CVcHDm_EunieI60T19_G43Qot7ZhY7m8hRLwLJivfFFXV0iFxjWr9ikKYeENi6EouKxCUSnUKm31GU_a7khjQka2OWHYSI5gfI1XHqQXQIYkf-m6u0H8Hckx8ABy5SbRV5EXta_wL-LDIigR2ahvHYvgq4lq44FFPKcgPd_ArrEpaSVyGHVjlDuPFwJHt4wVB_GtnKkVS-_buSt6r1yZu5OczxCMd7IfQNlDTg-9_m9EuyNU4nAz42a9N8s5CHjH2E6mFMJQ6TEbnRJvLXdGHtQdMeYm8oPjRoI2YF2GSwPkkZ96H5PCLH-gXCjG1mtsJnh2MtSZv-ZXyI6vmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fdf0426b5.mp4?token=hah0CVcHDm_EunieI60T19_G43Qot7ZhY7m8hRLwLJivfFFXV0iFxjWr9ikKYeENi6EouKxCUSnUKm31GU_a7khjQka2OWHYSI5gfI1XHqQXQIYkf-m6u0H8Hckx8ABy5SbRV5EXta_wL-LDIigR2ahvHYvgq4lq44FFPKcgPd_ArrEpaSVyGHVjlDuPFwJHt4wVB_GtnKkVS-_buSt6r1yZu5OczxCMd7IfQNlDTg-9_m9EuyNU4nAz42a9N8s5CHjH2E6mFMJQ6TEbnRJvLXdGHtQdMeYm8oPjRoI2YF2GSwPkkZ96H5PCLH-gXCjG1mtsJnh2MtSZv-ZXyI6vmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کوین وارش با رأی ۵۴ به ۴۵ سنا ایالات متحده به عنوان رئیس فدرال رزرو تأیید شد.
🔴
جان فترمن تنها دموکراتی بود که از این تأیید حمایت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/alonews/119817" target="_blank">📅 23:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119816">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر امور خارجه سوریه: دمشق خواهان دستیابی به توافقی امنیتی با اسرائیل است که بر پایه احترام متقابل به حاکمیت دو طرف و حفظ ثبات منطقه شکل بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/119816" target="_blank">📅 23:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119815">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرنگار سی‌بی‌اس مدعی شد: پیشرفت‌هایی در مذاکرات با ایران دیده می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/alonews/119815" target="_blank">📅 23:20 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119814">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: امارات و اسرائیل به دنبال علنی‌تر کردن روابط خود هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/alonews/119814" target="_blank">📅 23:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119813">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
منابع عراقی از شنیده‌شدن صدای چندین انفجار در اربیل عراق خبر می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/119813" target="_blank">📅 23:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119812">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شبکه العربی: حزب لیکود درخواست انحلال کنست (پارلمان) اسرائیل و برگزاری انتخابات زودهنگام را ارائه داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/119812" target="_blank">📅 23:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کیر استارمر ، نخست‌وزیر انگلیس در نخستین جلسه مجلس عوام پس از بازگشایی پارلمان، بار دیگر ورود شتاب‌زده به جنگ علیه ایران را خلاف منافع کشورش دانست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/alonews/119811" target="_blank">📅 22:56 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm-TflWD9Tf4fJ4xe4nyyTw__rzfmQyU8ETjRCQFPYPlSm0UfcsvrHVlzGUzsAIKhop99q3ZbljuKNboDHvW3Qh0SZ3_hdZI1HjvpR-1OK24pzgszOGzhdHvSf4UQv9YA15szJL6q3iSsFDe1PtaQdng7yP6XubVM-NlihuYSWfp9xpRTtXsT86uOMgYi5eq0GcRjglLYvuguXxiAPlyvR2w-Su67cm1t_OYelRK4IMsx3gjrrUCSJ51ac1EPoB9tzwTTGRpVZYyRcYpejr1j2WPaJdPRhrlit55ray_ZUNUbHfNSKCiR5bMP5yVEgfHDmtA9j2h36U0vLlK9UQBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چین رئیس‌جمهور ترامپ را با حضور معاون رئیس‌جمهور رده‌بالا اما عمدتاً تشریفاتی، هان ژنگ، در پکن به گرمی پذیرایی کرد؛ انتخابی که طبق گزارش نیویورک تایمز، نشان‌دهنده مبادله نمادگرایی به جای ماهیت توسط پکن است.
🔴
ترامپ سه‌شنبه شب با استقبال یک ارکستر نظامی، گارد افتخاری و صدها جوان در حال پرچم‌زنی وارد شد — نمایشی که برای تحت تأثیر قرار دادن رئیس‌جمهوری که به جایگاه حساس است طراحی شده، در حالی که چین زمان می‌خرد تا از بازگشت به تشدید اقتصادی اجتناب کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/alonews/119810" target="_blank">📅 22:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کاخ سفید در نظر دارد که رئیس‌جمهور ترامپ به مناسبت ۲۵۰امین سالگرد آمریکا، ۲۵۰ عفو صادر کند، احتمالاً در ۱۴ ژوئن یا ۴ ژوئیه، طبق گزارش WSJ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/alonews/119809" target="_blank">📅 22:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
جنیفر جیکوبز خبرنگار سی‌بی‌اس:
جی‌دی ونس معاون رئیس‌جمهور امریکا به من گفت که امروز صبح با جرد کوشنر و استیو ویتکاف درباره ایران گفتگو کرده، همچنین با مقامات عرب.
🔴
او مدعی شد که پیشرفت‌ در حال حصول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/119808" target="_blank">📅 22:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر خارجه کوبا: حمله آمریکا منجر به حمام خون خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/119807" target="_blank">📅 22:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/alonews/119806" target="_blank">📅 22:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ادعای ونس، معاون رئیس‌جمهور آمریکا: ما درگیر یک فرایند دیپلماتیک فعال برای اطمینان از نداشتن سلاح هسته‌ای توسط ایران هستیم
🔴
رئیس‌جمهور گزینه‌های متعددی دیپلماتیک و نظامی پیش رو دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/alonews/119805" target="_blank">📅 22:26 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرنگار: آیا شما با موضع ترامپ موافقید که وضعیت مالی آمریکایی‌ها نباید در فرآیند تصمیم‌گیری درباره [ایران] مد نظر قرار گیرد؟
🔴
جی‌دی ونس: خب، فکر نمی‌کنم رئیس‌جمهور چنین چیزی گفته باشد. به نظرم این تحریف سخنان رئیس‌جمهور است.
🔴
اما ببینید، من با رئیس‌جمهور موافقم که ایران نباید سلاح هسته‌ای داشته باشد.
🔴
هدف اساسی این است که رئیس‌جمهور می‌خواهد جهان را ایمن کند، اما به طور خاص، مردم آمریکا را از داشتن سلاح هسته‌ای توسط ایران ایمن نگه دارد.
🔴
ما به وضعیت اقتصادی مردم آمریکا اهمیت می‌دهیم. ما همچنین چالش‌های متعدد دیگری هم داریم. طبیعتاً رئیس‌جمهور باید به طور همزمان با همه این چالش‌ها مواجه شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/119804" target="_blank">📅 22:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: شرکت‌‌های چینی به دنبال فروش سلاح به ایران هستند و قصد دارند آنها را از طریق کشورهای دیگر ارسال کنند تا منبع خود را پنهان کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/119803" target="_blank">📅 22:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل به نقل از یک منبع نظامی گزارش داد: حزب‌الله از ابتدای جنگ ۴۵۰ پهپاد پرتاب کرده است که شامل ۱۲۰ پهپادی است که با استفاده از فیبر نوری عمل می‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/119802" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
مقام ارشد ضدتروریسم کاخ سفید: ترامپ نامه‌ای خطاب به معاون خود، «جی‌دی ونس» نوشته که در کشوی میزش در کاخ سفید نگه داشته می‌شود تا در صورت مرگ یا ترور احتمالی وی، مورد استفاده قرار گیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/alonews/119801" target="_blank">📅 21:52 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrBLBezZf3os7AcE6Kntp2XJAzp4VOQ3uP7ng6rrz7Km6-vzROP4cbdEy0iIzsT7aD3kdde-pxlKo2y3j_AxCZDSyu5pjamgUlBeg-x-WZKSA6NXUQ_Yo9sEWhY0YylOVyshXyiR4XqwIxxHhslkUzK5EnAs7xkq_Mj5JRAErrhVsidJH8zBsFonxaXmZTQisjpxXF2tWPKHHw1h_s9PgYWAjvZEAhCuXd-ZBurp9nfN6kOKvCbH0n4XA0_Pe11cT7zTouKNRbEE5c4ddNj2dbte5PypiHGoLGkEIYPwMMzFFARZKOL5xge270fbm0dmqox6bQRWoUnvVcMupdGdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">املت قسطی هم اومد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/119800" target="_blank">📅 21:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4KInpR4B30rRJizVD2G2nJomGtfZgeBVcGEa-DkjgOBYVP0UGaoLO3Khu7F6Q5TKXFT0Xf-7SbQAjq4YSxKU2yY_3a4l7BiWgQb5NBR0i5znGRhIGqTOqJTZF80Gev3ukjAgj0a6dFyGUJttw_SW075Hr-Md4p1rtLXnOcLiiDmw95dYg2WaI8XFvaO8StiETvX4lIj4sUz3vHqdci1Oc8gG3z5m7lGo3WS7v3zSpxTNbQF7qNuYAAU67n2E-dP1gMz0lazy-SMxrgCzWy8dp5Zlj3lat5YFoBCo07YukEoamlbRcN6ZBKWlSjBC7yW_uwArQy9UnCieV0vadjBSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پیراهن تیم ملی برای جام جهانی 2026 رونمایی شد که دقیقا شبیه پیراهن 2014!
@AloSport</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/119799" target="_blank">📅 21:41 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وزیر گردشگری: گردشگری پساجنگ جهش پیدا خواهد کرد چون مردم دنیا علاقه‌مندند ایران جدید پس از جنگ و واقعیت‌های آن را از نزدیک ببینند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/119798" target="_blank">📅 21:35 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
المانیتور: عربستان در زمان جنگ مخفیانه به ایران حمله کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/119797" target="_blank">📅 21:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی و به نقل از داده‌های ناوبری، چندین کشتی باری و نفتکش مرتبط با چین در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/alonews/119796" target="_blank">📅 21:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d734fbc3e.mp4?token=MoqpWdz_YGNtYWiSWirqIbiiwOX6trBdJpsi3fVs0gy0i5RobI_t0MnQWLmVvgZl42y0TR9APMnggIKv3ds-MY0t17WDkChK7o_FBVDDg_2uXZSOBCpFtfi0G1tfgpzYlNfe3BCocGyHXQBCvlYOPSpUoPQmKinQrVe6arHHH4YpxZ0qdwNxQExG5w4mdKXxKHrITP6sInFmPuOyteIB9s-bKiiBc9d_gPGzdwtO7rvlkbDpg1oinQZYi3IgHD7xYJFHo6y2PwuzXZh_qXOXbjzNdP1Ko-tH7E3as6Pp06infgA7_E7io5oEVjkODO5UsGQNdd5_znEvZL6LZRGRrFLVNSTQdtlhOGv_qUBZceCkWKzCHPgx9LjBqQmBVnw9RaBzni-NkiomEt18IY8wGoOzJWnfQpnenE0X84yXTVWphCr2RFmbOll7pvD08YXtPM4CYC1yXMsM5a47UuMhy6ORPALEs_xBzrWnfT8CVffuM7718nn5V0nB_KoWio_x_zBsYiSHRi9d0NWYOH7NzJufKYapqpipIKsF1s-p2YoH2LyZoIRiBdRZ7dWSCsqCB9uxEasE9a6ja6LBaf-2c_AO8oQRtcr1lnTZ9vklQ8l5ct17BehjxcHWctwGiVwAMgBGLsanvoSrZBaUeC4W4q7_wT0xXatPtVTKbD_J1DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d734fbc3e.mp4?token=MoqpWdz_YGNtYWiSWirqIbiiwOX6trBdJpsi3fVs0gy0i5RobI_t0MnQWLmVvgZl42y0TR9APMnggIKv3ds-MY0t17WDkChK7o_FBVDDg_2uXZSOBCpFtfi0G1tfgpzYlNfe3BCocGyHXQBCvlYOPSpUoPQmKinQrVe6arHHH4YpxZ0qdwNxQExG5w4mdKXxKHrITP6sInFmPuOyteIB9s-bKiiBc9d_gPGzdwtO7rvlkbDpg1oinQZYi3IgHD7xYJFHo6y2PwuzXZh_qXOXbjzNdP1Ko-tH7E3as6Pp06infgA7_E7io5oEVjkODO5UsGQNdd5_znEvZL6LZRGRrFLVNSTQdtlhOGv_qUBZceCkWKzCHPgx9LjBqQmBVnw9RaBzni-NkiomEt18IY8wGoOzJWnfQpnenE0X84yXTVWphCr2RFmbOll7pvD08YXtPM4CYC1yXMsM5a47UuMhy6ORPALEs_xBzrWnfT8CVffuM7718nn5V0nB_KoWio_x_zBsYiSHRi9d0NWYOH7NzJufKYapqpipIKsF1s-p2YoH2LyZoIRiBdRZ7dWSCsqCB9uxEasE9a6ja6LBaf-2c_AO8oQRtcr1lnTZ9vklQ8l5ct17BehjxcHWctwGiVwAMgBGLsanvoSrZBaUeC4W4q7_wT0xXatPtVTKbD_J1DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دیسکوهای ایرانی دبی چه میگذرد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/119795" target="_blank">📅 21:22 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/119794" target="_blank">📅 21:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/alonews/119793" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVarzesh+plus | ورزش پلاس(K_B9)</strong></div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/alonews/119792" target="_blank">📅 21:08 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزیر خارجه عربستان: امنیت تنگه هرمز اساس ثبات اقتصاد جهانی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/alonews/119791" target="_blank">📅 21:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ادعای رویترز : منابع متعددی که از جزئیات ماجرا آگاه هستند، اعلام کردند که در جریان جنگ با ایران، جنگنده‌های عربستان سعودی اهدافی مرتبط با شبه‌نظامیان تحت حمایت تهران را در عراق بمباران کردند. بعلاوه، حملات تلافی‌جویانه‌ای نیز از کویت به داخل خاک عراق انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/alonews/119790" target="_blank">📅 21:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-119787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXa94xXAogV5bc0sBsQhVnStzr0VY408QqjpO7KKX1WBFXBH6f0-LwSOmQtAcsQ18noT-vnWS4oVAnUO1tZI3Hkm-ywi5gpPVSDOVeydNvUlZbDK4yhogOwz5wnKyIkM_STBef7dqQ9rDIF3H9H6l51j75Q5B7TrxEDoU4UOwzozVii5-iwvbCZuft10LEiLssjXLWrxBZEgqlBBTVB46utvDQaUF6cS4LCEIG5U0nFZFKnVL11MDeTb47Jd8LXygcn0JrqPJlFNGM1m0wxBqN3dX6yUN6xZf7VRSHEOsSERwLqHX8JfD6Iz5v6YegxYWGk72wYYpobnc3E7qBsy_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tP-gegI3qVXBOR8vvJdG2dxmY3Nb8wu4cHYuXEcKZm8JWXCV0Fo0LhiG0CpPRijQ2D-RpayL-80d8OPLoheFZp7Wu9bsxyFzdnGrcXnWsld2wCbD3B3ZQVL4HdlhkPm9ionaK4bO0LZ4pYlP3lmi2qT-Tu1CebX0xcqNSoyD-bQR5U6c_taxHO7p3K-SZy1RZSQa6JIPMOAmFHaKYPEY-PJcsyHWxIGmY_iTZXiDMshFgPAH60HtElribefxFvzWPg5dsR5vD3Nt82STdc8MN_u0T7EpyyZlH-JABfldDS5jw2JtacDl5E3IqYI62T6f6sOk8odjPvSik2C7RRy_Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxFpsuQmMpPrR7imQMQqAJTRkh0sYcvroju-JSEXRS6_di84_j1UWHqJt2R6_s3-AhbuoJLuZuB1xjKMhSVcBT6VLq-1YXRHhTKMGAFNiS1oIenSlDKbo27hYoJq4dBvPR4PZ-d1FlqSWD6ibJe7OJlC5AJBayu6PO2CNq1Sni2r6MtIuSwwty_SKHdXEe44mWG3Zp6_dpqRnd27KOZjAavsGsNtTtWRytXyUbVW3oNbAoFpYZtN_RUNH2gCe0lkpaeg64LEi7Lcwnvdj0DTnOBOVK8NpB-AHlwYjsEww_9gbdERthYGzJsDsJv7ZvmpdoxV7ULDfUwwJ8vrp-y2Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سرباز اوکراینی با دوش پرتاب FN-16 چینی مشاهده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/alonews/119787" target="_blank">📅 20:42 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
