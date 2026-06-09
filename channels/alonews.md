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
<img src="https://cdn4.telesco.pe/file/jW6S-yCiFaKFmxA6l3b4xDlSAI0NDTvuToXB99bn-rwSRY0DCw4KkswGTKG-TYHbPE_3nkr69dqX6pKg6D6aGRQSUwghNo9Zi7nbr2dt38UBQr-Qh8bj1Qrt4XDC_F_tBebH10Kcpwyx3NaPml8yLjpUEeLcI1MeNG7nZqoWT9vEK7jSoUZp-lhYlXCI9hXQgA-62GScjRlZlJFUgs58QMfaPsD3zdJ43VlwSgx-CyXVz8pf3FQuUjz_4ECkSIwWr46UbJe7Dxy_tTuSyCIUbDy9q-abTSWO-t3BWmdIJaKHbxCI-PrUKuFWD6vHlIJhh48VpIwqoh1gC2aKCZj9oA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 977K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 21:58:03</div>
<hr>

<div class="tg-post" id="msg-126585">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
کانال آی ۲۴ نیوز اسرائیل: هشدار نتانیاهو: ممکن است مجبور شویم بدون پشتیبانی آمریکا با ایران مقابله کنیم
🔴
پس از تماس تلفنی ترامپ برای توقف حملات اسرائیل در پاسخ به رگبار موشکی ایران، نتانیاهو به وزیران کابینه خود چنین هشداری داد:
🔴
«ممکن است به وضعیتی برسیم که مجبور شویم به تنهایی و بدون پشتیبانی آمریکا با ایرانی‌ها مقابله کنیم، با تمام هزینه‌هایی که این موضوع به همراه دارد، کمبود مهمات و انزوای بین‌المللی. نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که ممکن است برسیم.»
🔴
رئیس ستاد کل ارتش اسرائیل، ایال زامیر، همچنین درباره توافق هسته‌ای در حال شکل‌گیری هشدار داد:
🔴
«از منظر ما در حال حاضر، تقریباً هر توافقی، یک توافق بد است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/alonews/126585" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126584">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
فوری / سوخت‌رسان‌های نیروی هوایی آمریکا از مکان‌های مختلف برخاسته و در حال حرکت به سمت خلیج فارس هستند!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/126584" target="_blank">📅 21:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126583">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به الحدث: گمانه‌ها حاکی از آن است که هدف قرار گرفتن بالگرد آمریکایی از سوی ایران عمدی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/126583" target="_blank">📅 21:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126582">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سفارت هلند در تهران فعالیت خود را از سر گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/126582" target="_blank">📅 21:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126581">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری / خبرنگار شبکه فاکس نیوز در واکنش به پست ترامپ درباره سرنگونی هلیکوپتر آمریکایی: به نظر می‌رسد این به معنای آن است که رئیس‌جمهور دستور یک اقدام بزرگ در ایران را می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/126581" target="_blank">📅 21:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126580">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048590050f.mp4?token=mz3mK9xTjIPusn3irJ7_P3YsQ1Kfu-2ePWxfTqnB3wJrDhtZQRIcWKhu4w0xMGs8IeYTEL1UTzDf_Ww-t8dmlB540sEvZyo-YLPXv8y-BCrbjxKq7wP_qhoI6Bl0I4io2JVsmFwsASGecCNbReuSxnNBsi6_Lk2x8UZSfbhRciwjRGPEjHEpPcp7lBnjiSxBmIqszPKwyUs4Y3aGSqnQ1JB4g_-DUzW2nJ8hRbSD3Ogb6Sd3lek2a8BNe3DUNjyv0xvhN_7z68WIyUaMm2OmRkTQpn-XpZpVeA182kK-HG4rxnjVCsF4WWtJpOvOY3jYeE-1vUT3GqeW0RlABetP_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048590050f.mp4?token=mz3mK9xTjIPusn3irJ7_P3YsQ1Kfu-2ePWxfTqnB3wJrDhtZQRIcWKhu4w0xMGs8IeYTEL1UTzDf_Ww-t8dmlB540sEvZyo-YLPXv8y-BCrbjxKq7wP_qhoI6Bl0I4io2JVsmFwsASGecCNbReuSxnNBsi6_Lk2x8UZSfbhRciwjRGPEjHEpPcp7lBnjiSxBmIqszPKwyUs4Y3aGSqnQ1JB4g_-DUzW2nJ8hRbSD3Ogb6Sd3lek2a8BNe3DUNjyv0xvhN_7z68WIyUaMm2OmRkTQpn-XpZpVeA182kK-HG4rxnjVCsF4WWtJpOvOY3jYeE-1vUT3GqeW0RlABetP_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار در خط لوله اصلی گاز داغستان‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/126580" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126579">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20aff12f03.mp4?token=HlkcUmlqWu4BehR95g49aGB6jqvLItDyld02P7ev1fVOnWi2bjHbDtySP8iWxg8ehM_VLbAq39XQgFD_Y7NB-HQc7KiX1xflOrmvtKaHeUp2UAp4u5UpzY9bkwh8MmCPVutg2PK5cdIGVOTS6RNHe2KyP18m1neVMXj3Z9yiqaS-B7DbKA0U4EUo_R-Lp0-OP6zvJYlYn5f0yAI7yEx02_DYlDqXxg--CdlBwCp1nt5q_xpeAtcyzAl6tpAz43sp1vSdsmH0StF_e07vLNuDVBBJyHi8l6QO63xRF7vcM1UquibMS0iEbYTAzfZvglV4PSm0MVlcWDLvnsvmDGdIUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20aff12f03.mp4?token=HlkcUmlqWu4BehR95g49aGB6jqvLItDyld02P7ev1fVOnWi2bjHbDtySP8iWxg8ehM_VLbAq39XQgFD_Y7NB-HQc7KiX1xflOrmvtKaHeUp2UAp4u5UpzY9bkwh8MmCPVutg2PK5cdIGVOTS6RNHe2KyP18m1neVMXj3Z9yiqaS-B7DbKA0U4EUo_R-Lp0-OP6zvJYlYn5f0yAI7yEx02_DYlDqXxg--CdlBwCp1nt5q_xpeAtcyzAl6tpAz43sp1vSdsmH0StF_e07vLNuDVBBJyHi8l6QO63xRF7vcM1UquibMS0iEbYTAzfZvglV4PSm0MVlcWDLvnsvmDGdIUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه سرباز
اوکراینی
با
اوربیتال
وِیپورایزر-۲۰۰۰
هدف قرار میگیره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/126579" target="_blank">📅 21:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126578">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
فوری / رسانه‌های اسرائیلی: «اسرائیل» برآورد می‌کند که ایالات متحده ممکن است در ساعات آینده دست به اقدام نظامی بزند، اما به شکلی که به ازسرگیری جنگ منجر نشود و در عین حال تلاش کند تا حد امکان حادثه را مهار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/126578" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126577">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
قشقاوی، عضو کمیسیون امنیت ملی مجلس: تا در کل لبنان آتش‌بس برقرار نشود، امکان ندارد جنگ به پایان برسد
🔴
کسانی که ایران و لبنان را از هم جدا می‌کنند اطلاعات تاریخی ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126577" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126576">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ادعای نیویورک تایمز: خطوط کلی توافق اولیه بین آمریکا و ایران تا حد زیادی مشخص است
🔴
مفاد کلیدی مورد بحث شامل بازگرداندن کشتیرانی عادی از طریق تنگه هرمز، کاهش محدودیت‌ها بر کشتی‌های ایرانی، مذاکرات آینده درباره ذخایر اورانیوم با غنای بالای ایران، کاهش تحریم‌ها و آزادسازی برخی از دارایی‌های بلوکه‌شده ایران است.
🔴
ترامپ مکرراً مواضع مذاکراتی را که قبلاً توسط فرستادگانش مورد بحث قرار گرفته بود، تغییر داد، از جمله اضافه کردن شرایط جدید مربوط به برنامه هسته‌ای ایران و دارایی‌های بلوکه‌شده.
🔴
میانجی‌گران می‌گویند هر دو طرف همچنان برای دستیابی به حداقل یک توافق اولیه تحت فشار هستند، زیرا عدم اطمینان مداوم همچنان بر ثبات منطقه‌ای و بازارهای جهانی انرژی تأثیر می‌گذارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126576" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126575">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / سی ان‌ان یک پهپاد شاهد ایرانی یک هلیکوپتر آپاچی آمریکایی را سرنگون کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126575" target="_blank">📅 20:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
شرکت کشتیرانی سی‌ام‌ای سی‌جی‌ام (CMA CGM): هزینه دور زدن تنگه هرمز در سال ۲۰۲۶ به ۳۰۰ میلیون دلار رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/alonews/126574" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126573">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
آی۲۴ نیوز: نتانیاهو دیشب به کابینه هشدار داد که اسرائیل ممکن است مجبور شود به تنهایی با ایران مقابله کند — بدون حمایت آمریکا، و هزینه‌های آن را بپذیرد:
🔴
قطع تسلیحات و انزوای جهانی.
🔴
«ما نمی‌خواهیم به آن نقطه برسیم، اما می‌دانیم که می‌توانیم.»
🔴
رئیس ستاد کل ارتش اسرائیل، زامیر، درباره توافق هسته‌ای در حال ظهور تندتر بود:
🔴
از دید ما در حال حاضر — تقریباً هر توافقی توافق بدی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126573" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126572">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126572" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ: من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126571" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126570">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrtfR6iSuXWlWpHSE2iHpd-1Wlfb8iPhsePkp-qJYaRaL_GFlE7iQLNJL7BQMVtvY3wv2rS73e1pFHqeR6rhjiHTOYUCIhxsOuKnBVFKh5gkAb5b2wOgcgFGLSA0pa-LFss5x_XJbUzKXvOiPzfevpYRa04WwudkTxZWB06AuU9QrW0V5Eynj_U_ujSvHXPhnrMp69iuyAH_4296lg6WyMKTdydM1yyVCS6VM7jE7TQVAqhOQVTxbbYG31xfz4qqaPi6w7ErVnkZ0FvTpcM7C9TBge4PqJbJSOt-Jt32dv0wTy1qEkdHAo-1RTzyNPEKvcuzdEYX_wjjfrZB1MLDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ از اینکه نمی‌تونه مستقیم با آیت‌الله خامنه‌ای صحبت کنه خیلی ناراحته و حسابی ناامید شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126570" target="_blank">📅 20:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta-8TbP0FN3sZVATszFG83ITNWgOSUYc967c276NkuaheYJlZB27Lm7yGLNhuT5f1-5_urdDIdMr9NO9ZfLuY6P0ss9cYem6kRm5BkvbfyxS6jTkoXRSJgl5D9Oyw7NiqWvWeuT7QzcuRX6276zwDcUi4YsVc3Xm6D0oJhMbasUdF9HWTkXvaexUlkkBfLRwjvxa0PIlS6A-7Lh_vZNBl-NfAb5nfrtv2ymc33YkauUYc6V2LjdLCYKm7nt88efsF2g3TPn02wFokv15McJvq807tRIXQh-wJZ4fh-UtmGF3jeysXTXD3hmYgCc3pvLh4XfF3RW3STjEwDVEDJSISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای شبکه کان اسرائیل: امارات ۳ میلیارد دلار پول به ایران تحویل داد
🔴
به درخواست ایالات متحده، امارات متحده عربی یک هواپیما حامل ۳ میلیارد دلار پول نقد را به ایران تحویل داد؛ در ازای آن، ایران حملات خود علیه اسرائیل را متوقف کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126569" target="_blank">📅 20:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
قالیباف: ما زبان دیپلماسی را ترجیح می‌دهیم، ولی زبان‌ غیردیپلماسی را روان‌تر صحبت می‌کنیم / شما سوار همان اسبی می‌شوید که زین کرده‌اید
🔴
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم.
🔴
اگر تعهدات خود را بشکنید، ما به همان زبان که خودمان بهتر بلدیم، روی می‌آوریم. شما سوار همان اسبی می‌شوید که زین کرده‌اید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126568" target="_blank">📅 20:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126567">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqlJoUaKrMetRT6VPtvmVm31jMkIWEN0jCin3YZxz02MJ5q0u_tjM9amTm5walWUW54vnmlt2hdR2OTsEivMOrR9h4Ny65wLSyJQWGoL_DHT9yKGAWRAAyQb5LVtgSxhUHrOEQ6bboTp9yCgK57TMQEF4dUy-M55zYChGNU4aRJUapJSKav9_-Tuey-EqY75sp9BWuUzY8CDiA27rApZmNfUFJRC3JnbxKYoAZ0sCMSFZ6ippsWj41-Qjg1-LBu74teNmxMrBXqi7U7ZQrkWvr1xDIkSi1q7CRXlY33vRrxk4qnQjVL08sy32PQ7_pqXmzehdxCBMsCjIlWjnZ1sWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/126567" target="_blank">📅 20:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ونس: فکر می‌کنم موفق خواهیم شد. اگر این دیپلماسی در نهایت از هم بپاشد، رئیس‌جمهور ابزارهای دیگری در اختیار دارد. اما تا زمانی که این قضیه را به مأموریت اصلی خود گره بزنیم - جلوگیری از داشتن سلاح هسته‌ای توسط ایران - به باتلاق تبدیل نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/126566" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126564">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orl3b2NSbnjCA8AnBQkq-ux2GpNDiA4bs-Y3Cl_IiGEUtiLNo7jXFc_EEkmRKcKq0QujPsuFO6maJAjQ08FF0pFSBoRrMLms-bG4VaQv9Sn-mzJkecgwxPjsNU6J2xfem2azwDbuBzEzBY_Dc8_g9vflGFDOat2VI_M4T2GMZivpKLEOpZKb14kNilodX3glzJrnvlywqgELLSKRuF19aaV_HqUR-iXQFwC8dAc195_R20f8SrLkPUnyE9KAN1mpasP_jT7ZjJYjpkYkI8MyFS6azGBk-m_LRejEbGQE7z9l6e204WJpnZmsfg7gnavhPsoPadNtJ1ckOySCOS7pqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ec2182e.mp4?token=SGxZ2hmN01rU9LxOUJzE3hGx9DrG3B94UjG9eBVy-5-Pg59YOgyBb8AiqtwjOeNmdi-9F14SoJq2awvyYsyIYpiuEYHWliyd8WCa5SPiiAgjxe1xkKu5nLBUldYahxr4rYiWEk9h5aHvdoX8N9_E82-lyJJx7rQ8eGKHisRZ6kAFpfMKQbXpcuauH1y5FdInCheaE7VAldYBZxgp_7DNBfh8B0vaiCdbtuKGkwU8k5osxblHbAybX_zS4ocIAGXfP4JbgYQ_x4H76hInNaqs2b9op54duWlb7LytzA_NIwmYPWjuAqbVC6bfxGkK4DtiyQ28--3-_KymJ39ZmADKCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ec2182e.mp4?token=SGxZ2hmN01rU9LxOUJzE3hGx9DrG3B94UjG9eBVy-5-Pg59YOgyBb8AiqtwjOeNmdi-9F14SoJq2awvyYsyIYpiuEYHWliyd8WCa5SPiiAgjxe1xkKu5nLBUldYahxr4rYiWEk9h5aHvdoX8N9_E82-lyJJx7rQ8eGKHisRZ6kAFpfMKQbXpcuauH1y5FdInCheaE7VAldYBZxgp_7DNBfh8B0vaiCdbtuKGkwU8k5osxblHbAybX_zS4ocIAGXfP4JbgYQ_x4H76hInNaqs2b9op54duWlb7LytzA_NIwmYPWjuAqbVC6bfxGkK4DtiyQ28--3-_KymJ39ZmADKCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی خود را در سراسر جنوب لبنان ادامه می‌دهند.
🔴
عکس از ارتفاعات الریحان و فیلم‌ها از سجود است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126564" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126563">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: بازگشت جریان انرژی به حالت عادی ماه‌ها طول خواهد کشید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126563" target="_blank">📅 19:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126562">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93151d3dbf.mp4?token=rS0a2W93AZonyfLr4ZpPxVJSTYESobaYP2_A9qKCJszUHmNqM62krms_hbO-RBNWavhIbdUWNpxFodmDVcJHgvIw2pNL2HXPcdlvh8MUHzw6NGeuHI57iIba2KFE3Ag7MTJd0JWXOudvTq2GYqQz58HVCgDPQX8_4T6hnCLVoVx20kjPkp4akMUmJgAvJEcbKYx4J0DeghBCBszja12ZLVHmk-K0SUIl_sRoNZbyZe8TgHaDu-RFNVhhFrZ2J2ave3iSOQT6qo77oqxnHpr4N2hFOxlPiphdT5yq5WtoBzaULDlHBDN4CIzVo5jiwhoMUC6CzEzeAFFYPuLwwfXK8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93151d3dbf.mp4?token=rS0a2W93AZonyfLr4ZpPxVJSTYESobaYP2_A9qKCJszUHmNqM62krms_hbO-RBNWavhIbdUWNpxFodmDVcJHgvIw2pNL2HXPcdlvh8MUHzw6NGeuHI57iIba2KFE3Ag7MTJd0JWXOudvTq2GYqQz58HVCgDPQX8_4T6hnCLVoVx20kjPkp4akMUmJgAvJEcbKYx4J0DeghBCBszja12ZLVHmk-K0SUIl_sRoNZbyZe8TgHaDu-RFNVhhFrZ2J2ave3iSOQT6qo77oqxnHpr4N2hFOxlPiphdT5yq5WtoBzaULDlHBDN4CIzVo5jiwhoMUC6CzEzeAFFYPuLwwfXK8DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر نشان می‌دهند که یک سرباز چینی در حال آموزش برای فرار از حملات پهپادهای FPV است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126562" target="_blank">📅 19:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126561">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ونس: جنگ ایران یک سال دیگر به تاریخ خواهد پیوست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126561" target="_blank">📅 19:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126560">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گفتگوی وزرای امور خارجه مصر و عربستان درباره تلاش‌ها برای کاهش تنش در منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126560" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126559">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
فعالیت‌های پروازی فرودگاه کرمانشاه از سر گرفته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126559" target="_blank">📅 19:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126558">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
العربیه : حزب‌الله اعلام کرد دولت لبنان باید «روابط خود با ایران را اصلاح کند».
🔴
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران «برخلاف منافع لبنان» است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126558" target="_blank">📅 19:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126557">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
منابع خبری از حملات جدید اسرائیل به صور لبنان خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126557" target="_blank">📅 19:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126556">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
به دلیل ریزش آوار در معدن گلتوت زرند، یک کارگر جان باخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126556" target="_blank">📅 19:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126555">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ارتش از پایان وضعیت اضطراری در شهرهای اسرائیل در بخش شرقی مرز با لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126555" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126554">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKYLVI_NRSTJZuMbB09VZzQ4mCe4p21FZX7kOL_WuyeHgReKKNLoTSAmURY-Asaqfp_2rXhtXew8T58tW38mvw0L0RozKIzXBy5ypNhBtHj5n9Rtvga7kDg2RjxgfbksSfbIBUyRCgQ4GSyz0A_AWD2zJmXhPWjD255Zd4P6cCfB3txoef5yOB_D2ss6T9g1q9CuXduza8mF0fZndTC1BWqCbT42ABUUZkGitmSLvLfWe_LZULBvtXXOA35C4YPlMvQO3Po7KcjsMqDXERzsaDuOFbyevFHfqXYoIFTqWicjCsRrqB18UN2JS2pYMOoVP2wLzjYi55mqnlNOSifSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: در طول آتش‌بس دو ماهه جنگ ایران، تیراندازی‌ها واقعاً متوقف نشده است. با وجود این، یا شاید به همین دلیل، اقتصاد جهانی، نفت و بازارها به خوبی از این وضعیت عبور کرده‌اند - اما تحلیلگران هشدار می‌دهند که این وضعیت نمی‌تواند برای همیشه ادامه یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126554" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126552">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFc0lyePZ7vVCzszoXHva4cdbFVT0CX_IEKyqjNjASTJFrZ4jt3ZdnBXOoIQ3CRFA-rjdQM9cn3ql45hM5jHDJ2VUvSShAVff3PNXvwl4zjdPpi9aLSCh0329T1XjCl4pKCZgzsZEP_WHVjpLuWqOUZ2g0xIOfiwzyIGBwodbgITlvreIEQonetnZmE9aSHq0rD-mdt8ADy85z4qk0TE-aUJMfWiuP9tdKlpUGGZfHaBYhqr-xyLZoQJNnvyRYPNpmeTOMhHIw0o2zurbk3cQ2G1Tc-s0PrABKs1a5pW1BYzjKGZAyYHF-UIxHfSLjCZO_xo7iSpNWeXNIzhTxm2Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8884fe0fce.mp4?token=la0IN0TTmZG7N2ikKOdV8UQnOuB3AYkHIXRvLxI1WXGoKZYoDwLJNuGyNthoGkV6T7GUJKzNfkBEYKLLsuyKbWDv_HpIPD-oVFMYu8WdyAue1lgjlPG4_-p7xHcpjGrI-B0T_mYdoZPm8GHuNaphV7gTbFbnGkd1ms3s6U8BZHGfNdfBM4HKrJ4ZNiSRSOYNo_XR12LPVkZ2ojC4-WST_0Nj3UUr5NNn59VEjCYIJLuB7UWM97L6yBG2TG1in7fn-Q6SDAdHgnBVAPSaUYBWu8OEJpvjFfw07vwZ7HVYKAg8AzUY2ce_w0cuksOpbU2tVmViz-OfUrNcLHfjPbZk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8884fe0fce.mp4?token=la0IN0TTmZG7N2ikKOdV8UQnOuB3AYkHIXRvLxI1WXGoKZYoDwLJNuGyNthoGkV6T7GUJKzNfkBEYKLLsuyKbWDv_HpIPD-oVFMYu8WdyAue1lgjlPG4_-p7xHcpjGrI-B0T_mYdoZPm8GHuNaphV7gTbFbnGkd1ms3s6U8BZHGfNdfBM4HKrJ4ZNiSRSOYNo_XR12LPVkZ2ojC4-WST_0Nj3UUr5NNn59VEjCYIJLuB7UWM97L6yBG2TG1in7fn-Q6SDAdHgnBVAPSaUYBWu8OEJpvjFfw07vwZ7HVYKAg8AzUY2ce_w0cuksOpbU2tVmViz-OfUrNcLHfjPbZk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال انجام تخریب‌ها در بیت لاهیا، نوار غزه هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126552" target="_blank">📅 19:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126551">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
زلنسکی: روسیه درک می‌کند که اگر ۶۰۰+ پهپاد و موشک وجود داشته باشد، آن‌ها این جنگ را دقیقاً همان‌طور که ما احساس می‌کنیم، احساس خواهند کرد، اما آن‌ها این را در خانه خود احساس خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126551" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126550">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fde767e669.mp4?token=IJKG1yaGvQlxGEw8bWGAq-czlwxdcHARSeNmkBsz5Lz3B0GTvqNFbAx5jIknfbznlDX8gNIinkj5p0hMpiPQg999Y2D9xRFVirjTCYkY9SMjG0-_FPFdb6sJA0YeNonw3T1j_StbG90slUvgQW12d8PR6PPUf436-m_uCB7nh3w0ZNlu4A7FhIOiryD7-YAqdeZhf1sOlLbaxtW95vNteCeHez7dY7vIdOX_vSkZW7SrT3-n6AZLb-yfYjUzGE4kt32kqwULQZgLTtoyT3enB9-_3k0QKSo19epGeqaV3xZTD-pLE4W8ZzYuM7n3m5eBeDcBCDeN0jJfdS1LzWkcxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fde767e669.mp4?token=IJKG1yaGvQlxGEw8bWGAq-czlwxdcHARSeNmkBsz5Lz3B0GTvqNFbAx5jIknfbznlDX8gNIinkj5p0hMpiPQg999Y2D9xRFVirjTCYkY9SMjG0-_FPFdb6sJA0YeNonw3T1j_StbG90slUvgQW12d8PR6PPUf436-m_uCB7nh3w0ZNlu4A7FhIOiryD7-YAqdeZhf1sOlLbaxtW95vNteCeHez7dY7vIdOX_vSkZW7SrT3-n6AZLb-yfYjUzGE4kt32kqwULQZgLTtoyT3enB9-_3k0QKSo19epGeqaV3xZTD-pLE4W8ZzYuM7n3m5eBeDcBCDeN0jJfdS1LzWkcxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زلنسکی: همان‌طور که شریک امروز در طول جلسه ما گفت، اروپا بدون اوکراین نمی‌تواند از خود محافظت کند. و این بدان معناست که اوکراین باید در ناتو باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126550" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126549">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: تردد کشتی‌ها از تنگه هرمز به‌طور چشمگیری افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126549" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126548">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNwIiueLekstbd2GJpLU4wtSTcW9c_ys_m1K0XlKuSPrl_EktBGlb-Q8syaehTnjfhu_WtFw-LvpXWD_qsqcKL3sObsWlwKnX0hFyUkfpWyvJ5lXj3TpxHZh2FtQW0c8BGAePbdhtSJ-C5Bgycde3St-yLy9sTgUicSnwlem7PnVKpxDNXAVBFTD3BCO0UgJts-D5K3bOpi1rKevuuQToQdbupRFWNxGP_Tqgud63JoPoLnL-psmVfh7CvuPrQImTNmH97yKndyRieyF404YvmL50vVkJ2z_5HNXBuLl4N4WZ9tSPIjFHR7Z3iLi2BnUctXOYgX-15sPV4gUblDZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید حساب رسمی کاخ سفید در X
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126548" target="_blank">📅 18:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126547">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knitpwVh_eoRZyEoZ-qWCCdo1bC4pxbSpiRPxZKZBLngU6v13m4Ben2x2Y5wMGdFYzeO9m98AKoTUerJVB_mYE2xdJcEYWmrD2ZWmLrC2BxesAuauUcFH27tdaYgbgaS3F2O8isO8iBY90RYOF7As7FNmoen-8pU0kzg_XubKxWTx_BS1hAF6CG4NQtkO8ye_nGrF5uPjhGKSo-bJq_vHghdRFFYGdTx-rot4-bbBhbA0GUuFFsqzgLz5PoaQxXoHcmj4o4j8YSPm-EznbDNNf4y10ysWnnCzOFFHJrAMITZD8pBI0pU_H4rcdX7juBLrJUSCvN7_e8igbt68kLSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه رسمی فیفا : دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126547" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126546">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
وزیر دفاع بلغارستان: ما دیگر به اوکراین سلاح ارسال نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/126546" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126545">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNfFAYhfdlV1Tie3ZUbxLoL8-46_PpRF9Rdc98N2o1cY0uwKnaQ5P8vPwhOHRSTJ1q-zEqSN2zysURU9pPiyc_7sLve7ifugeJQFy-gIjfTXpmZoBjp7g10IGwdqhAmiAuOsCQh7cQvD1oquyacCr0842C61e8Zz6zEVtEBED83Mr8Gbsuv-jKyauHc5yh_ONuUNcRVwhmA2BLc1zv2gbDFCcFJjNZCxJ_Te-3fJzOgw2Q7m1o82pTNlVdHxkDbV0e9lU8Xff7BeXTvGx0GGsaY5f85NAN3XHbjsP9G6C0fNuJibfoPudtvaK-MOY5lR7yUWqjkjfsmDLFaQy7ctww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126545" target="_blank">📅 18:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126544">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سخنگوی جنبش حماس:  گذار به مرحله دوم توافق آتش‌بس، منوط به توانایی میانجی‌ها، کشورهای ضامن و «شورای صلح» است که بتوانند اسرائیل را به توقف نقض توافق و پذیرش این توافقات ملزم کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126544" target="_blank">📅 18:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126542">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
شبکه العربیه، به نقل از یک مقام کاخ سفید: مذاکرات درباره توافقی برای جلوگیری از دستیابی ایران به سلاح هسته‌ای نتایج مثبتی به همراه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/126542" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126541">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWU7bd3Rh0EX79ciPbGbEbHQ3GY5laCRxIE-CMS80yuSVnt6rksMBj4pj1E8_-K0IT7srUQHf62qPSPd6nECMSokC_UdhxfWFfM4SFka0vGKgE3SQEToWfJFswWcgStJnlT2ZA4fsWAVNFxK5NzRoc9masoni7XZk2pC1rqjUDFJV5p0HRmn0SM-T1WazqYdwRdEmMX28uwHpBMRLh0XvB9mBlK68JseFcnjV7HyyzP-Y7tlG7398B658QQMhNWNny3p4zVy2pkP8WWYjm9NwscqpTfjzrMq7alDcwJivCRQb1lvw_oQb1UqINUyyVr3khZm39nIPLbQKwI_z3W35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
خاورمیانه همینقدر عجیب غریبه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126541" target="_blank">📅 18:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126540">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی:
دستیابی به توافق برای پایان دادن به جنگ بین آمریکا و ایران در چند روز آینده به دلیل وضعیت پیچیده فعلی، که عمدتاً ناشی از نقض‌های بی‌وقفه آتش‌بس توسط اسرائیل در جنوب لبنان است، بعید به نظر می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126540" target="_blank">📅 18:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126539">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5669cdcaa7.mp4?token=lzUD4GV11PJmeiFxLfnf9YvYwFN-eMEMV3cRi1QTwl7JFhaH3Hkmv87UjU_PihwgX98L6x6BPEehYQfIpkIgfSyXwVbQdkKffinZwaPoSHPy1LvqOb-DbHPWm_ObxsqcqIye8MZeE1mVcVXEWKkjk3Jgb_hiaSY0k1N1T8xpdQBqfdk0sU-x3tatRtfdJRCs3SnUpnB2Ho6hB4ySwNoXYy_6tFxaUe-sO_g8XFyIvfUGEXTsDWJyyMtfYML1Q8berW96f6hDaJDsNXBlRoNNZ_fWwd_jybpbZkb7fC6gHjhZ-Sa9FdcTF-jsSZtwAAyJ2jyPJe4Cq3TXDk6YdHS8cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5669cdcaa7.mp4?token=lzUD4GV11PJmeiFxLfnf9YvYwFN-eMEMV3cRi1QTwl7JFhaH3Hkmv87UjU_PihwgX98L6x6BPEehYQfIpkIgfSyXwVbQdkKffinZwaPoSHPy1LvqOb-DbHPWm_ObxsqcqIye8MZeE1mVcVXEWKkjk3Jgb_hiaSY0k1N1T8xpdQBqfdk0sU-x3tatRtfdJRCs3SnUpnB2Ho6hB4ySwNoXYy_6tFxaUe-sO_g8XFyIvfUGEXTsDWJyyMtfYML1Q8berW96f6hDaJDsNXBlRoNNZ_fWwd_jybpbZkb7fC6gHjhZ-Sa9FdcTF-jsSZtwAAyJ2jyPJe4Cq3TXDk6YdHS8cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇺🇿
کاروان ازبکستان وارد خاک آمریکا شد؛
پلیس آمریکا هم بلافاصله با سگ‌های موادیاب و انواع دستگاه‌های ردیاب به سراغشون رفت
😂
@AloSport</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126539" target="_blank">📅 18:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3Jl2EQHlX6FOfWI87hl-H8Y6Zo-5zsE6Ns8knU8QhHb8v2mEEyzJ7f2Om9Ip_1J3Ov3MgTFujUJArY4fsPv4Gf5nY3zv0Qp0Cq-qxX-0IGuSphmocMTAvvroHjJEz-FwXnZ5Jfi7p6x9c8y5YyIAMdNGSn9rLjLKyvNlA2OzYUF-RTM09LsvcET9KQw0CDdr343Wx_5Pp52fIKi6JK7caZcF8R0hc2NM37FpfjmNgnY08nF_4PwmoQ6j3y-3Zua4db-f3Lu6TE_IyAKc_cDswE4O25Goi5EKpS8bnH1bpBTcAOyMT3yfsRcsvrTBGJMAf8spkA1s3ca-jNsWNJSgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Aqx3YkERBkVunjydVA_YfIFGLxZY3qj_GaTBagYFChGkK739FQrLbVGfegZPRxvVTjRQgtxv_ov0eO8WwlvdkqlY-r_3y1QCXQ6GrxgaTlb8h3tZXR7Flt0THrJ4z4vQnDQdIlN7jpVb1NkMq2wT2RNRXdMbV49C_GwX75TQ_4fFXi3N70F-x7URXy2GcJ5LNAQ_suOUdPU0T9gFpDm4i6_LUaqafcK62dafuUOZULTeVXC1bGOkAc5nSJSDPKiXJ-BBOLMO2_ZcvRckf9Rr60T93wTZ07kPJujo_dcF8RIsWauoS6cn202ITQu3awfzLtk7jvNj6zTjL-9xkVUXOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=YQkyjKan_cr2NEq0xT6VTzmM8nrRHHAAkQC0xI6AqmTGvg-pADp2I8oy4JuBUzpgIt4PMV2q05lWRDZ4bYVW2KGPbmiLes0eaKHuQcF0e8Zf63hdwAfemKcaEehrwg87ZFeweYqwgnCM4kLgC1O7OifK9rzjpEq5ySyMJwXrjOHGk83ptHzYmxUpmUV1AB_W5HBibzvi8zZZ2O2AZO5drqEXPfjMpMbITGIHkQgpYmcfeIiMzVZZ8f_X18ksWxuVw98IoDhwTj3CB9nITaaf8QukS-zsgSi6Aw4QA6Auhp5fil8wsYwc5vXHcOyMuTEgc-nA6o_AsXiCaZxpgMfQaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=YQkyjKan_cr2NEq0xT6VTzmM8nrRHHAAkQC0xI6AqmTGvg-pADp2I8oy4JuBUzpgIt4PMV2q05lWRDZ4bYVW2KGPbmiLes0eaKHuQcF0e8Zf63hdwAfemKcaEehrwg87ZFeweYqwgnCM4kLgC1O7OifK9rzjpEq5ySyMJwXrjOHGk83ptHzYmxUpmUV1AB_W5HBibzvi8zZZ2O2AZO5drqEXPfjMpMbITGIHkQgpYmcfeIiMzVZZ8f_X18ksWxuVw98IoDhwTj3CB9nITaaf8QukS-zsgSi6Aw4QA6Auhp5fil8wsYwc5vXHcOyMuTEgc-nA6o_AsXiCaZxpgMfQaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل از اوایل صبح درحال بمباران شهر بندری صور در جنوب لبنان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126535" target="_blank">📅 18:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8ZaeeFtcu7h12SkFNXKeZ-wdxEk-8KBPurPCIAREgEvxvewrusKCurlDONjiNODotGvVVH725d2A7dRJPlmcEOkH4g7I3LQzO9NmjaymiX06AnYFQI1bprzprk1o6bSq0pxPlLsI0y-OO_evgqlBz4JfBYIbhsfSauU1DwYmnOLnNrc97yT2TfrdbrZmfJu28SE1xwkGUd63AqRpVhIPOJDOH2KpTt8v-2o8tinIL-XkmkzrwsmIKgE-etry-f05FDBIAxdQ_QzTdo3CxWY-BFk99bYZ4corY1Juh9bERHJrBXjAwRwy0BfZCGP1VUwbT71-KucpoJynuxNTVDJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس ستاد ارتش اسرائیل به i24 :
🔴
حمله‌ای که به ایران انجام دادیم فقط مقدمه بود و برای یک حمله خیلی سنگین‌تر و گسترده‌تر آماده شده بودیم
🔴
تلاش ایران برای تحمیل معادلات جدید و تغییر شرایط موجود شکست می‌خوره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126534" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e18f9d77.mp4?token=bxuVm67HzUzflbz7VlPeaA-7_HbcCbJX7R0T_kkyzdsEkm2KH1KgpXTHo9q5EVyymo_STK3AhPNmhddaWclWVmzr0zl7twYM6CUsBzqDebPzWlilfGRNVEe5g9fFTbslZS6j7hhkECZGz7OeaUWSxOo18QRF_fuPKFGE_tLRSRYrCgxYaR4spb7yzsrn4rmB55105-ZDQZN5pz_kBX5ABbeosgbrvumOq0qOJhteuVvGAqitN0iN2DY9ya082ZlrIXk7LgNjQRzRjAkjT1qBTw36a8B9WjjgDGQZMfDbVUYnMTr6x08ekQoLRHbbuKUspWZiwsM5UOwRDncb5dnsBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e18f9d77.mp4?token=bxuVm67HzUzflbz7VlPeaA-7_HbcCbJX7R0T_kkyzdsEkm2KH1KgpXTHo9q5EVyymo_STK3AhPNmhddaWclWVmzr0zl7twYM6CUsBzqDebPzWlilfGRNVEe5g9fFTbslZS6j7hhkECZGz7OeaUWSxOo18QRF_fuPKFGE_tLRSRYrCgxYaR4spb7yzsrn4rmB55105-ZDQZN5pz_kBX5ABbeosgbrvumOq0qOJhteuVvGAqitN0iN2DY9ya082ZlrIXk7LgNjQRzRjAkjT1qBTw36a8B9WjjgDGQZMfDbVUYnMTr6x08ekQoLRHbbuKUspWZiwsM5UOwRDncb5dnsBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اعضای طالبان در ملاء‌عام گوشی‌های هوشمند خودشون رو با چکش شکستن تا وفاداری خودشون  رو به رهبرشون که خواستار ممنوعیت گسترده‌تر گوشی‌های هوشمنده نشون بدن.
🔴
این در حالیه که طالبان تقریباً تمام حکومت خود را از طریق واتس‌اپ اداره می‌کند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126533" target="_blank">📅 17:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da6cf7b2a.mp4?token=pDBQ24Xark0Dj6TCsDOw_yFWong9TB-R_oj4LlxMClr4GqJYihwhSUsHnKfEYZwAQFFnb3SAPau7_idI5smN1t7QaJj4Lzhzt8z9r3ixIvibsgaN8YpKrEdPOlpS5laFeQOstTDqXWCVrWrI4wC6favjTSvAC7vrUiaHpSb-Sk7csAkrHr99guM2GS1XdTmjM8Q3C4LDTvAokGZuNoqMHI8u6Rb2NzW1KttXzDKJBXO_EbyTs0SX7NcO-eVXSL4RNlVn40_GGdAvgswkOVLDiSDdHdUSyPGUH6-6z3Ksbb6yHLvkbEZiWZo7yn7SJJL8aKUBxm_aAEml3uZEMBrIuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da6cf7b2a.mp4?token=pDBQ24Xark0Dj6TCsDOw_yFWong9TB-R_oj4LlxMClr4GqJYihwhSUsHnKfEYZwAQFFnb3SAPau7_idI5smN1t7QaJj4Lzhzt8z9r3ixIvibsgaN8YpKrEdPOlpS5laFeQOstTDqXWCVrWrI4wC6favjTSvAC7vrUiaHpSb-Sk7csAkrHr99guM2GS1XdTmjM8Q3C4LDTvAokGZuNoqMHI8u6Rb2NzW1KttXzDKJBXO_EbyTs0SX7NcO-eVXSL4RNlVn40_GGdAvgswkOVLDiSDdHdUSyPGUH6-6z3Ksbb6yHLvkbEZiWZo7yn7SJJL8aKUBxm_aAEml3uZEMBrIuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به صور لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/126532" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/126531" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126530">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
🔴
ما در حال بررسی این موضوع هستیم که آیا شلیک گلوله از سوی ایران باعث سقوط بالگرد آپاچی در نزدیکی تنگه هرمز در روز دوشنبه شده است یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126530" target="_blank">📅 17:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126529">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
شلیک مستقیم نیروهای طالبان به معترضان در شهر هرات
🔴
طالبان میگوید که اینها مردم نیستند و نیروهای تروریستی هستند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126529" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126528">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a789mwh72weXBEl8ZQHfGM1I16b5KFs5Bz-dzxAK_bjEt9Gn7kgETTcJlNkRCo4sRmq4VKVFeW-Vh0xGNTncC1s6sE0gIA5tQz_PdoIfOKaA8nkQLDhqv8Yc--l9zOtnXbJwEm0WaJz-qjxd9wFkOTX0t3eXVC18-sZIwt0SLfdBuwyBx1DLEQpC1bn2u9y6W0HIuQ8Us0P7v5kzxQe4pQGzq6QJs6JWoGCT1YJ9EZ3nO5zBTAIPwnw-E_PCeyEyq7A2Ej2etBlVbxxWlduWssKAvMiCvQ-fthtnuWfClFri7QNHodz0kI_yU9wSDcwasqh14_S73bsW6kQYRZCIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیا خانم ایران
۵ قلو زایید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126528" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126527">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126527" target="_blank">📅 16:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126526">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126526" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126525">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6oNjj1nnppyGmWZhybHRw0z6iWIJO0yWKZB2_fhwSPvb5AMgALs8xA1sFekye_5UTDNYkZxm2IoRriae45v_Mw41w12tay8isfP1QgsZ7aBUrbvTfgFKzYEoocFRwNGFjsJd3ZQifywIgHrnEvyV5OJ3eZLtp3hIlB4267_Kve8b7_aHfUSrYB3AF7R4JTae887ImE9aReM7SKMAm6xjBVtPLDxZJa9irGN8VitbuygyxOel-odaPzKvkyuvOtTMX07mr4jYhWDkCY42CWKh3N2piwgdWip4z8VYgOpNDNvBq_cH1sh9TIdpDb-RySnFLH4LQWK3QXTCNTboVCehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126525" target="_blank">📅 16:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126524">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR55R6RIrmA8wUoyZxg4jue2m1zU2--6DY2Y_LLaf3saYnYVI0a1cC7IlaYb9TGFLlm6dy0oUWYksZIBul8PSai_zWmfeYlrQ4GcjogrsPN47uhUFL-eiJ4MNZUozJSbTGa-hgTogId31Q6jsepBjS_UP3gIo64j2WATFFk9IwbYu4KqR6Pzuo9Rw0aNgOSyS-sVmKHHOqaJxZhsOEhHrVbpskbzQj78sAq7i-K6pCjEIxPf6jzYE4PH4osRLbctMM1JatuWCxMJCkTyENqfs2auLf2Pc42ovhSmEiaeGqqvnZ1MNJRuVaYpKe2UNMPADE_YPKv6cilulZRY-nhFtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126524" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126523">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-HBinKNcpae9RBU4rslVbFzvdxPAXwZR6QDcoa6ovpk0cdLObXpfhfXPCtQvRsWOnWp2elNaIwkpDCKA_OhPwLxSZQAL31oj0ep2VxuFqV9nmrBrK8xJvAcioZ1L18mIkNigfTUaZX2579iBFzwqw5fc6MAEkA9TJ6VenaovjCDCEGUC-IFH-0kncYokT5EMQ8fi-I56G_HplVfbFjmQZldrJWl4UHcxAmor34GyjIRHxyDGNK5x7FdIUMQ-uXH22QK6OUn9nVWXpMwP79JOycP2g1qTEpreXmr9svEgjSVJchqGQzeRZaENI6HLPRsI0v6BOYV3LTsvOTcupEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/126523" target="_blank">📅 16:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126522">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
حزب‌الله ادعا می‌کند که با حمله پهپادی به ساختمانی در تلات الصلعة در شهر قنطرة در جنوب لبنان، یک نیروی اسرائیلی را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126522" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126521">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به شهر عین بعال در منطقه صور در جنوب لبنان هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126521" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126519">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaW-Hws7SD9TKgW1oibbeI2cqaYJg8MYEbc9E2vX2evyBWTEyoCNq4X7yAYEyEfyrsmjf4YFnKXFyYgZupOIaSDwoGQAb2MC-abVp4GlLpAfIdhqCMbEddXiT-7GfcJ2FYZTKSbLnTX2uVrztILBK2Z2r7hNjqWl-CW3oGNGb85x4Z2w_WuM5FQeqVivdnS2je4SOrFmv56ZKcytgSJRxC-h4eE4ZtNL2mvSSvvKioV-M2n_GVZpUStWZwdOvdbZvrw1Ivl-bwPln7D9xRE3p3NtvfxuF5m58pESWS5QY5d3h3y8u-xAnauJ6v3BNWBn9O8mqOlqWDx2KdIUxB_emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه و عربستان برای بازسازی خط آهن مشهور حجاز به توافق رسیده‌اند
🔴
قرار است این مسیر ریلی به عمان و بنادر اقیانوسی نیز متصل شود تا به گونه‌ای برای دور زدن تنگه هرمز هم مورد استفاده قرار گیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126519" target="_blank">📅 16:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126518">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت دفاع ایالات متحده ۴ شرکت چینی، علی‌بابا (پلتفرم تجارت الکترونیک)، بایدو (گوگل چین)، بی‌وای‌دی (تولیدکننده خودرو) و نیو (تولیدکننده خودرو) را به فهرستی از شرکت‌هایی که گمان می‌رود با ارتش چین همکاری می‌کنند، اضافه کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/126518" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126517">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urjz2ho2LbimJNi77Rz0ivogBS-yjiNBCkV1WCsSuriFIH_jL6fyqp6tZaQcxsX-Udvcc-iMofWu6z0rFMWIXhyiaSmjxsuP8VQiGCnwNYDbSMlK0UlvCQm21RO493wUg_ytYrNWZCpal2MMcxQA2Z6p6-IPBuSlfud4WDdivZE8fKbVTNkUatMiJnZqyGMc0JXRzT-OvzLRZmjQh0MR1kdrcr4lYGZutsWS527XQ2G3v3jV4Xasa13noK5rD0LqMQ1lq2y4IbEoZK50ah_TiOSHNPJLtKjfRJ_7vA4DVjQRNfF1dbKTbQcYLnuBolQvjnZOhJdj3PqbSHxum2WcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیوان عدالت اداری شکایت برخی مسولین تندرو بر علیه رئیس جمهور جهت تشکیل ستاد راهبردی فضای مجازی و آزادسازی اینترنت توسط وزارت ارتباطات رو رد کرد و به نفع دولت و ستاد راهبردی فضای مجازی رای داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126517" target="_blank">📅 16:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126515">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Qj77ORLdTMhO1wWXMQ8gOrV-8lvDEFNLd3YIf4TonDhVUdcyQObcKrdDr3TJsv-2q8fikR1h-3myaWtkaHIDDeC7FU9SrWoU42BHUOdFP-cZ9slf601gtnachRGfGiretR-7llBe-Fzas2V0GxpNfUKmp4dSQ-EesGqvn0NVMqwWeExV4T08wLwH-LWTYnGe7W-XtOXUupJyb_cxI7pY1Yyydw9zJDioA6Itmwo2uxOO-sufd2PTe_RIjSujkpN8lXIz6wmkoUEXaZ49BPumu5522-EKJO2hBQNbYQn_08LMj8zUfqCb55hq6xtp-j4m2fxmzqRIIPp1iS3YMK3F4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BfRpcIc99y8Ml0NZLgEHhTLMa9ccI_GmbBobq-5tZPweb6kyjKa56GHrpUq0LZpxxUkdMZ64qj8v66zE0mW-nVXtEEBNmUwrZMVVs-fq3xDGfbI7PFeu9qTorcxF28J_5DhhuCNEBRCgBimnIgym484uvTeOew0gmJ472xXCELVXfnzL_zNy_K474agvS4ERQf-eeVo8vb6O5bKP-mEdUwA-xcnRp_1FMiPHwU335Adwy8zNI8HSPbMaOa3g6gUteywQzzQbeCZYxmrSeCEFXB-ZVg2eD5z7yz-TIsnv0nvEFO2X3CPPYRwOx03Xr_ipi64sTkq-7uvnPeypIb6Myw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
گویا امارات صادرات روزانه ۱.۵ تا ۲ میلیون بشکه نفت خود از طریق انتقال کشتی به کشتی که نیمی از آن در لنگرگاه صحار عمان انجام می‌شود را از سر گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126515" target="_blank">📅 16:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126514">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بر اساس نامه شرکت مخابرات ایران به سازمان بورس، این شرکت مجوز افزایش ۴۵ درصدی حق اشتراک (آبونمان) تلفن ثابت را از ابتدای خرداد ۱۴۰۵ دریافت کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126514" target="_blank">📅 16:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126513">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn2UAIMnDHf_prGE236_Tx-z3gPRanlvXjoDjea9kcfSSTQEanLak5bZkULCzaJPNnqA02KYSpYaM5gLP6tCBewKVKom1_wPtdgIFp-X8TROue_ZX2czkSZHAWsjhI3ILOJxnq19819wGAyfWWlYgEWWzW_224oranH4Q6mB055twry5f07kCkue0NKXj_UKQ5ExNialldRtOT8CbYBlI7f3RPL3pBNhcqDfGI0TwXe-Sk0lOShMb1ugJU5vpz9fxZ5r8p1wAA2OK5_IlY7JbFixYMrCyEy-fpI9ugXXZaqW3a5mTYy1ak8gDVJsVoTSuL4QulHhpaCSGBZRHVfL5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت آمریکا کاهش بیشتری یافته و به زیر ۹۰ دلار در هر بشکه سقوط کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126513" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126512">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEUMK0dDhDJlnopaqR82xQKdD6PtHCNLRDhQRwjLmJJjIfE4guFJs1iuW4oP-hi5Y52gpSghJLIz-R5vikOttg4s3KadCPFN0TOR_-h5SYmYuPnS12_346IUL6gFBtdm80LgckITXv4532C278vTRt7IJijsfjujPZXBpW-5aPcBA0ctrsMzJD6i-Mn0bQZfHXbKwvFsEzq124Ldxehnh5GsvQ00R8D7OEtZxWE74P-uA-N04_TITpwE4hrKShMriMkyVhS2XtkIgmJJUFKl5VXwf8C7Ce3Ewod8csSeAHeWfL78hjweyULOgtfNds9uBtsehR801HrhII6zURDZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز مدعی شد، یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده (USV) که توسط گروه ویژه ۵۹ اداره می‌شود، پس از سقوط یک بالگرد تهاجمی AH-64 آپاچی ارتش ایالات متحده در تنگه هرمز، به نجات دو خدمه کمک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126512" target="_blank">📅 16:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126511">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
به گفته اسرائیل ارتش، یک فرد مسلح که از لبنان به خاک اسرائیل نفوذ کرده و در منطقه رامیم ریج به سمت نیروهای اسرائیلی آتش گشوده بود، به ضرب گلوله کشته شد.
🔴
ارتش اسرائیل می‌گوید در این حادثه هیچ مجروحی نداشته است و نیروها در حال بررسی منطقه برای یافتن مهاجمان احتمالی دیگر هستند. یک پهپاد نیروی هوایی اسرائیل نیز برای کمک به جستجوها به منطقه اعزام شده است.
🔴
به ساکنان جوامع مرزی میسگاو آم، مارگالیوت و منارا در منطقه جلیله پنهندل دستور داده شده است که تا اطلاع ثانوی در خانه‌های خود بمانند و یک بزرگراه در نزدیکی آن به روی ترافیک بسته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126511" target="_blank">📅 16:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVGaUSQgjkneVjns3b9wJnbjiu3UX7I4-MSuCcSSbTvW0JgThc37dk6xwfvF19_jgGoOGFGsNU8yuTyf0Rc4DCTvtP8c-Ov9qeNJg0fJ78xu64aRi0yzq7zLaneJELslMIRZTfzsjc_sVd2vCaThV1fnlB4OG-wFyOEi3CW4NC0MTXidNttEQC8UYyu88RmCfiCqL4nVGwHKMPrl5PcZ9Pk8bPixrC07tOG1PlaoFllE8gjimkV9_wKVV02VMczOXxMhGuHwq81SB8Ut_xMuogaPQgSxYopKaLyhGBwzDewFsEHfAi78ZvsLUqe6-xZCydlZXvHpeSfrfivl8ckmgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eEcTAovwx2IPu7yZEQ9T-RWzQCIJGjPxqOECwO-zR_YRcJ0Qz5wDZDip02B10mQMEmVmsO1igppFyYOR3jZstqjOH9HM6phd22xYAU5hHH895p9vnh0Qsha_aIMFDbChTbdS49TG56y_RGimT23ZgFkZ90os50hqL0VZeoKpAl4iz57JdZqyi9W7TSsivUHPHbyJYNkeLsB08yQ3Zbc43dck5TSzT4TAkifUI0i3zh5hTQ_wY_iw2hjhBscy3wdO0M4Uphlcmy5UibAl5KoEH-R9qJfjCNjILM4ouK18nmh4nY7PPwuFdHLtPdEJfy_21vszF_aNYW-wieBmXcoJsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
زبان ترکی به سوپر اپلیکیشن بله اضافه شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126509" target="_blank">📅 15:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
وزیر خارجه بریتانیا: با عراقچی صحبت کردم و به او گفتم که از سرگیری درگیری به نفع هیچ‌کس نیست
🔴
از اعلام توقف حملات متقابل ایران و اسرائیل استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/126508" target="_blank">📅 15:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126504">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0SKtBZDe2koNiq8Nw9F6TWGuezLqLPqGFyaozSLRAPfJXRWjPe9xjlUi9xcF3hk6DvX6g0bC_w4scUClP1A8SV6l7yNv1fU2i-yTslXDkAQDGvFPlqrbQKA3mlVuQXFx69rBmSFq0uEXYlL4gdAK2MmJLq6QrmFcLTK_iZqC0QcKv-XWrJgafiUZ-2JCUGLUk0SuRWCi0sAnO7AU7eVkfXsIC9GqkBTQO73OBQrdYA08QNa6T4tF_WmZyj1bmn4pPb9QASo-mVsPTbJ3u_lNUJ5wwTwVPQ-GGf5gv3h40Mxox8JV4_rTqLLAvY2tc89HMBrYzuMppWpQ1ilP3iAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DG867QiRJd-4r706gx-49YwbKxkk57FkOs7qO8KZl1zx_gxIRwvtEVXOyqCYr_nwtuypXi_N0vnSBzpm7b42TEXTSfzjM-A2dIT_afIu1cTPgtzTZnF08Qg69Q-zzCRXIPQqq-qQJbwQ6ulbQyMObQqhprx07QwyCLZNqsPhymwadI2tTx7kk5PrKQnHFn81jr61KmRFgpzjEjZfh36PS2uWEprBzbuWLZaMfQEV3GGlNVfIpVIR2hwp0PZqQG4bD6jcCsmE4cxRyPN0NoSbXF2MzIsI2j4E209gd-b6ZeEyEz4BpTcJ9YcmUwCTqxo0GLnGA8EF89k4blqX0oOAuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=KJr_KuZAONYR-FhbqJuoUe2Ob7mf7XGL_3QETLrw-nH-LzYaMd1wsuTdVZUnR8zY85CJRhcd0FcHHk4NDTQcRqxakSx2T2jqGMO8-d-IPOZSHoJT_G9ylkWl7EQFhD4LXaiyNscS2CkymHa4w5HmERLmOyiL7dhXafZ1cDrEe22CB9x-7IjlwembzvCuWp2F9XV2j85vX-8d6f3yuZqa3EKGHheTiywP4yXnA0TVlHoXsBVENg03M1dru7PPpD2rkbMrCNA_Vz84ZgOEmeWzGt8XD7RcfA3VW_YgH4wOnu5BOyzw6h6rn0I6VnlxRNQ0bUITycfqDEXAtzVusTvmnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64b9e99782.mp4?token=KJr_KuZAONYR-FhbqJuoUe2Ob7mf7XGL_3QETLrw-nH-LzYaMd1wsuTdVZUnR8zY85CJRhcd0FcHHk4NDTQcRqxakSx2T2jqGMO8-d-IPOZSHoJT_G9ylkWl7EQFhD4LXaiyNscS2CkymHa4w5HmERLmOyiL7dhXafZ1cDrEe22CB9x-7IjlwembzvCuWp2F9XV2j85vX-8d6f3yuZqa3EKGHheTiywP4yXnA0TVlHoXsBVENg03M1dru7PPpD2rkbMrCNA_Vz84ZgOEmeWzGt8XD7RcfA3VW_YgH4wOnu5BOyzw6h6rn0I6VnlxRNQ0bUITycfqDEXAtzVusTvmnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی امروز چندین حمله هوایی به صیدا در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126504" target="_blank">📅 15:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126503">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: تنگه هرمز بلافاصله پس از امضا باز خواهد شد، که ممکن است در دو یا سه روز آینده باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126503" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126502">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
سفیر اسرائیل در آمریکا: می‌خواهیم جنگ را طوری پایان دهیم که تضمین شود ایران برنامه تسلیحات هسته‌ای یا موشکی و حمایت از نیروهای نیابتی خود در منطقه، از جمله حماس و حزب‌الله را متوقف کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/126502" target="_blank">📅 15:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126501">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
خبرنگار الجزیره: حمله هوایی اسرائیل به شهر نبطیه الفوقا در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126501" target="_blank">📅 15:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126500">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پاریس:  ورود بتسالل اسموتریچ، وزیر دارایی اسرائیل، و ۴ نفر از رهبران سازمان‌های شهرک‌نشینان و ۲۱ شهرک‌نشین به فرانسه ممنوع اعلام شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126500" target="_blank">📅 15:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126499">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ارتش اسرائیل مدعی شد دو فرمانده ارشد وابسته به جنبش جهاد اسلامی فلسطین را در حمله‌ای هوایی در جنوب غزه هدف قرار داده و عملیات موفقیت آمیز بوده است.
🔴
در این حمله «ایاد محمد عبدالعزیز نفل»، از فرماندهان نیروهای نخبه جهاد اسلامی، و «احمد معروف»، رئیس یک هسته عملیاتی مسئول اجرای حملات راکتی علیه اسرائیل، ترور شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126499" target="_blank">📅 15:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126497">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh4Hq-3nRQgLFdLnVr-pRKTviR3soJ0lF9mozNATA5HQNHy3ZpiEcdD3V13xt7QT9sAMhfG4FSm8RlD9sV2HdZItDJqQkt40BPNmZDNehnHYHM5xXIDbdu6YcCxeVwVS4oBZMRS7_KPFEnnq8cU7OhP02adIduoLUQuo6So9w1gLX1NSyFq9ve1dWL3r2q-zhRhiKQg5iE2nVq6Ux9zx888_CBHymXY1_2_qGhQhLTWJ8v9f8weVefkpO60ZSFoVYp4xrJhj1J6sYralFICSsyODXFrxr3i0oYjc9UUm6fne3MQIhWO_AcEsZL99-9Kxzy2ApjC-MOS4QNSWRMoxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaJHAfaNwmWUMiSTuJZcmB2Glx2N6OyqSLXdQmhinVBUmo5UufTpYJrzLlCfxFDGvrL4yAenZQ8MtMGTRH9uyFF09Gf8X0hPx3OfEzwXqCjUTqQZUTZJB3ObDpmQ9mhWQVTmir8xJ768r8a1xxppUTLMHnTJSX9ja15HjDJ7u2-FlqwxMBRRd6ET_wkSaneV2WKYx4HVqY3YwPGrcM9C5KFkq44J8Te2mJwo7Cb7x_yBcO3NTbQBjj5OtpxsRhXuO4blaKBodCoCJcP4pf3PZOx1LdgS12AKcwM213i7Ql7ndQzLN8t7Ta23t18qun4uhFqJ44gjH7JLT-hr7iCpQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملهِ هوایی به شهر کوثریه الرز جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/126497" target="_blank">📅 15:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126496">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
شبکه ۱۳ اسرائیل : شورای وزارتی کوچیک تصمیم گرفته هر موشکی از لبنان سمت اسرائیل شلیک بشه، جوابش با حمله به بیروت داده بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126496" target="_blank">📅 14:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126495">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
اسرائیل هیوم: مارکو روبیو نقش کلیدی در متقاعد کردن ترامپ برای حمایت از حمله اسرائیل به ایران پس از حمله موشکی تهران ایفا کرد.
🔴
بر اساس منابع اسرائیلی و آمریکایی، روبیو از استدلال اسرائیل حمایت کرد که عدم پاسخ دادن به ایران برتری می‌دهد و تشویق به حملات بیشتر می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126495" target="_blank">📅 14:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126494">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
نماینده ایران در آژانس بین‌المللی انرژی اتمی: تجاوزات و تهدیدهای مداوم که شرایط استثنایی فعلی را ایجاد کرده‌اند، متوقف نشده‌اند
تلاش‌های آمریکا در شورای حکام آژانس بین‌المللی انرژی اتمی الگویی برای توجیه تجاوز بیشتر علیه کشورمان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/126494" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126493">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e8515ff.mp4?token=X_ZLmc1ONXuwOyHi7-e2ikbGtD6HqqnpZ3syaVz-hc3ELP-dbAuAwy0x2YGf2V3tjnFRiIkREzCsWtRoLwcEl4F-PrCXplZ3sMAFMZXXGQB7ZLoYP8HSEGpfielMSooP5sBr54-WAu5FsXlOp-hfNhN5m-lHXeQ30K5y-quCDi7Uh1vZhAm4RUvKVf5rL0VMgnTw0kFSxG_0QyxRYZFNwL8YpodgtQA1wkICogOtOPX9bn81pEI5Y7jEqkKSMGCkSTMyB5jv1bHtQd05IKR2Cpt0wm0oUeIez0l2C2NqYPRi8gZOwLHmMmxN-TkRIQOFOtzoeTWsGSevDG6zJmORbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e8515ff.mp4?token=X_ZLmc1ONXuwOyHi7-e2ikbGtD6HqqnpZ3syaVz-hc3ELP-dbAuAwy0x2YGf2V3tjnFRiIkREzCsWtRoLwcEl4F-PrCXplZ3sMAFMZXXGQB7ZLoYP8HSEGpfielMSooP5sBr54-WAu5FsXlOp-hfNhN5m-lHXeQ30K5y-quCDi7Uh1vZhAm4RUvKVf5rL0VMgnTw0kFSxG_0QyxRYZFNwL8YpodgtQA1wkICogOtOPX9bn81pEI5Y7jEqkKSMGCkSTMyB5jv1bHtQd05IKR2Cpt0wm0oUeIez0l2C2NqYPRi8gZOwLHmMmxN-TkRIQOFOtzoeTWsGSevDG6zJmORbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس
:
خود آمریکایی‌ها تو مذاکرات غیرمستقیم به ما گفتن حرف‌های ترامپ رو جدی نگیرید
🔴
اون چیزی که از طرف آمریکایی‌ها تو مذاکره‌ها به ما می‌رسه با حرف‌هایی که علنی می‌زنن فرق داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/126493" target="_blank">📅 14:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126492">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPbhw_b5yHAnNtwvVhZ7HoNFPCoX6Mr97j5sFowcHh0T7ujW1mrAS5XSEjvqZj7-5VcYqILcJBWhMgCQWrNNAQZN6tPfjqEtPjs7sinEP8hhdh_2FLkb247A9WyeJcF611rapbzv9ZqzefcOvs1Rm0vhFtetufsHlDsmCc30GxMhP2-ZjG33E3P5458y-4BslVhGwzyfCfMmiHjASYHVIgWraQq0cSYGnR6u77cd6A7B722RT2Fz79TQ7Q37ODf6Eixw6MnNauXfpHfOXOelUyG9CGC0hPVCrqN_rnaZBL9vBsFYFQjKqQOQn095KqT8AOUPfcOqwOUIqx-KQfHzGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس گزارش بلومبرگ، سقوط قیمت بیت‌کوین به زیر $۶۰,۰۰۰$ دلار در روز جمعه گذشته، بدترین عملکرد هفتگی این رمزارز را از زمان بحران و فروپاشی صرافی FTX (متعلق به سم بنکمن-فرید) در سال ۲۰۲۲ رقم زده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/126492" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
ادعای یک منبع پاکستانی به شبکه العربیه: اسلام‌آباد در حال انجام تماس‌ها و رایزنی‌هایی با همه طرف‌هاست تا در همین هفته به یک تفاهم دست یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/126491" target="_blank">📅 14:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126490">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کانال ۱۲ عبری، به نقل از یک منبع امنیتی:
ما وارد مرحله «دورهای مکرر» با ایران شده‌ایم. ارزیابی‌ها حاکی از آن است که تشدید اخیر، رویارویی نهایی با ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/126490" target="_blank">📅 14:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126489">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
حمله به نیروهای امنیتی پاکستان ۱۴ کشته بر جای گذاشت/ ۷ نفر ربوده شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/126489" target="_blank">📅 14:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126488">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZE4N_3XDp5L2StDzPtQPapujLONOQ7ehfvLf6weDlgc75RQQOw8qeEK-EplzyIdHeeqg0eeLdt5d6EFFs3aZ8HUYdowGV65QS72B9QobPVeQud1L1et881xT0IdZflmOeZu246lA5EzZF4IRo5di0u9PdqIn9aZeaDHumFSSSEKcZd9fPEQyFVHgoYJk8u5m7VX3G6xcK-6vffuQMlQJIRRPXg6RQT1tXx9b2Fh1lrIQL-xczMitwu5AEaFY34J-LbjrLpBS8C_NZSU9YDFyCm1raCzmSe4bkO_ZAJEbAY0CfgOg94_9TlcltJz4TN7x8aqk201SKAuD_Ptzt-abw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش اکونومیست، ایران و اسرائیل که برای دهه‌ها درگیر جنگی پنهان با تابوی حملات مستقیم بودند، اکنون آماده‌اند تا با شکستن این مرزها، خطر یک درگیری تمام‌عیار را به جان بخرند؛ وضعیتی که دونالد ترامپ را در برابر یک دوراهی دشوار قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/126488" target="_blank">📅 14:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126487">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: ما دو خدمه یک بالگرد آپاچی را پس از سقوط آن در نزدیکی سواحل عمان در حین گشت‌زنی نجات دادیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126487" target="_blank">📅 13:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126486">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
کرملین: میانجیگری آمریکا در مورد اوکراین در حال حاضر متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126486" target="_blank">📅 13:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126485">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=mq7G1X9gII9eGzb5eKs6R5T3DWqhOEQOzhj2V_Wfig27ZHbdW6GZ5gJPgUgAnilZ3nmfItIk3ErQIJv7aJNLUaI650bZYR6mIAByc4ZdCkjsX-LRy9U9WIuSkI47twgxbWl7KWGvzqn1jgcWNBDqMuUTLCjCG3-Ye7KiDzAk1v3h4OgL5vUZg357MaZFHqz7Tq0CZVW-jv91ah5NsATtNKrKiOS3_I0YH036bQxhgbWEGqFv-KF5-AJ9jd7m03WueGv9EMbX6FeUAm2XOzNsIwxl9WcOn0QidOvPpJk0g2Aif2aybGglM4_ZW4ZtIjcLnNlr0mqSyvFAq1iFXmFw0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c08628adf6.mp4?token=mq7G1X9gII9eGzb5eKs6R5T3DWqhOEQOzhj2V_Wfig27ZHbdW6GZ5gJPgUgAnilZ3nmfItIk3ErQIJv7aJNLUaI650bZYR6mIAByc4ZdCkjsX-LRy9U9WIuSkI47twgxbWl7KWGvzqn1jgcWNBDqMuUTLCjCG3-Ye7KiDzAk1v3h4OgL5vUZg357MaZFHqz7Tq0CZVW-jv91ah5NsATtNKrKiOS3_I0YH036bQxhgbWEGqFv-KF5-AJ9jd7m03WueGv9EMbX6FeUAm2XOzNsIwxl9WcOn0QidOvPpJk0g2Aif2aybGglM4_ZW4ZtIjcLnNlr0mqSyvFAq1iFXmFw0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودروی بمب‌گذاری شده در مسکو
🔴
یک نظامی عالی‌رتبه ارتش روسیه در انفجار خودروی بمب گذاری شده در مسکو ترور شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/126485" target="_blank">📅 13:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126484">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AE8byJVqXQS-Ana65mTNeGRrpHTWWiwqamrBc3QyTFItAkz5-vN14fdfRzaBSTmcmEGlkxDIpE6p5QeLoU2U0tQSsTESKr0X00KguoSLrW1BJK8aqt0qHosUI2w24RteEu40rEU_N09M4OVpQkzrc42W58CscBTHWoliTjSu5D5pm5vRLBx1uatDTXocvtl0uKM7CSHlTwvhzN9sab8isvmS2AKC51cys3RppAf_dJ7K2OA500t3Lvf0a27aXiML83F4lY_ufETRMspn0W2FUz4yLq6f-O3QsOevVABw2uJ_34l3wcvBjC5CEfbJN5u4_f4RKbSDr_EKUJwyeJu_ogIIxgHL3US7VI0S-1MkEAkw8osHrndh_yjN1HTF9GT2ZCOyMcKCNC1y6jjSRsEu_R8Lyn6kugw0eMW6D1m0KjCKSBCUEDqsGgrP6108vZqYQsVi_L-fJ51E6MNKW4MuwaZbD2KnUhyNx5aECMT94Ik_TUcuXbg7w62R-1eFxke03-EmHcBLi3yAVH_9O5zzngeRtd0ymSfjvNh04ejl4JngZY6woAEkO4Nd9PNyENuCTURYCanhiWbnUlr8Wgn5XsAI5kKagPKQ0ygeLYaoF_Hdpp89POdRUqSHSwMC9dj63LUcMZZxHLhDtQDiiZM5JUlBJ8tppOL9KNT4OsdU_w4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dcf528f85.mp4?token=AE8byJVqXQS-Ana65mTNeGRrpHTWWiwqamrBc3QyTFItAkz5-vN14fdfRzaBSTmcmEGlkxDIpE6p5QeLoU2U0tQSsTESKr0X00KguoSLrW1BJK8aqt0qHosUI2w24RteEu40rEU_N09M4OVpQkzrc42W58CscBTHWoliTjSu5D5pm5vRLBx1uatDTXocvtl0uKM7CSHlTwvhzN9sab8isvmS2AKC51cys3RppAf_dJ7K2OA500t3Lvf0a27aXiML83F4lY_ufETRMspn0W2FUz4yLq6f-O3QsOevVABw2uJ_34l3wcvBjC5CEfbJN5u4_f4RKbSDr_EKUJwyeJu_ogIIxgHL3US7VI0S-1MkEAkw8osHrndh_yjN1HTF9GT2ZCOyMcKCNC1y6jjSRsEu_R8Lyn6kugw0eMW6D1m0KjCKSBCUEDqsGgrP6108vZqYQsVi_L-fJ51E6MNKW4MuwaZbD2KnUhyNx5aECMT94Ik_TUcuXbg7w62R-1eFxke03-EmHcBLi3yAVH_9O5zzngeRtd0ymSfjvNh04ejl4JngZY6woAEkO4Nd9PNyENuCTURYCanhiWbnUlr8Wgn5XsAI5kKagPKQ0ygeLYaoF_Hdpp89POdRUqSHSwMC9dj63LUcMZZxHLhDtQDiiZM5JUlBJ8tppOL9KNT4OsdU_w4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر ارتباطات: پزشکیان، عارف و من نظرمان این است که وضعیت حکمرانی در فضای مجازی مناسب نیست
🔴
ستاد ویژه ساماندهی و راهبری فضای مجازی با قوت به کار خود ادامه می دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126484" target="_blank">📅 13:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126483">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پروازهای فرودگاه هاشمی‌نژاد مشهد به روال عادی بازگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126483" target="_blank">📅 13:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126482">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=GbvWxNQTEkfg1VlwDlu1TL_8A3djUdha8FCIuUfrDrRPNnAfWiiuI18mq5XqyqMMbz0IWgEF9p74c1Cs5bwufU6DpvalAWO32Zdz_8Yc6EGaHvA4MPbaOnPTbLF0UA_M-zySnD_oiZNloAH_QliVzJJADeZYsVszErFpfw3piO-KqC7lLUT8_budantBfwLl5WscvT8qVhpbLGiZvkRe26xQKZFcOnkAE8tMWRL-gbKyoOcaoGAq4qZzXoovmtS1wgByCmOfAglqbvp-XXanigqECRsAm6Fk8iCVcfxpmRjmyWeC9HaQc8COOb75WScY8r_PWXdqCrg9LYJz31FMP2XhqeLiRGYrM7x9MWLSblDioV563jIwurWRsRFECrje11W856O5qCyIF0iLeVAE55h5GqPBQwIMqnQDofx9j4c9LgSsBWsgGsMixkqbksj1mVrmh-gIUOBZ_BSxeBWIdpPLqM3qPlN19zpZiQkgzEW2nsk7DYYwT8I--AW-oyZNsOEOz_uPuIeChIWTfVrIOchxCsZyP5B5p5oG0Av27H3TaZiWT8zXOHKA_PXciUJzVzKQbGCngRPhy1iKITsPjNpzBXDgz0sQc6bYwntw-3NYV-m4QhKxjSpPjprsELx4EmDUSyTX8CW_da0C0t51tetXmZegQEU_mdCnPBKq-FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa05669d1.mp4?token=GbvWxNQTEkfg1VlwDlu1TL_8A3djUdha8FCIuUfrDrRPNnAfWiiuI18mq5XqyqMMbz0IWgEF9p74c1Cs5bwufU6DpvalAWO32Zdz_8Yc6EGaHvA4MPbaOnPTbLF0UA_M-zySnD_oiZNloAH_QliVzJJADeZYsVszErFpfw3piO-KqC7lLUT8_budantBfwLl5WscvT8qVhpbLGiZvkRe26xQKZFcOnkAE8tMWRL-gbKyoOcaoGAq4qZzXoovmtS1wgByCmOfAglqbvp-XXanigqECRsAm6Fk8iCVcfxpmRjmyWeC9HaQc8COOb75WScY8r_PWXdqCrg9LYJz31FMP2XhqeLiRGYrM7x9MWLSblDioV563jIwurWRsRFECrje11W856O5qCyIF0iLeVAE55h5GqPBQwIMqnQDofx9j4c9LgSsBWsgGsMixkqbksj1mVrmh-gIUOBZ_BSxeBWIdpPLqM3qPlN19zpZiQkgzEW2nsk7DYYwT8I--AW-oyZNsOEOz_uPuIeChIWTfVrIOchxCsZyP5B5p5oG0Av27H3TaZiWT8zXOHKA_PXciUJzVzKQbGCngRPhy1iKITsPjNpzBXDgz0sQc6bYwntw-3NYV-m4QhKxjSpPjprsELx4EmDUSyTX8CW_da0C0t51tetXmZegQEU_mdCnPBKq-FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به شهر ساحلی جنوبی صور حمله کرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126482" target="_blank">📅 13:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126481">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ix_by70aGyPnjQjbwZIn9RX85rerRBVOBLqlXuwMdGT_UMURhYU9su101PboI-NbuTW3rvLeqPMrDuECWbE1gAk3inoj3G2URKz8UeLBkO_-GJinoVGe_nhR-SItkwr-3Oj2ZUCJe1bIIfdEkq2LFWsSsAFNJgx9l0Y4S5n8cLvW4T4Hs0nrptWUBxaHU7sgSrjPiN7k5DlFrO_rMcWJd4sNqtqnEP14wXM5UBYtOXIsvW7SArqPinkO2xXMqbCYYgQpnM0agwlfgBbc8A1jK9MXMk14t0zF-qiZpzVRdchezb2ULi4rwc-dz3eLw64RVAv3678r0kvNYiXnlQJLHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۲.۱۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126481" target="_blank">📅 13:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126480">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نیروهای اسرائیلی در یک بازرسی نزدیک اورشلیم، هشت عرب از یهودیه و سامریه را که در دیوار دوجداره یک خودروی تجاری پنهان شده بودند، کشف کردند. راننده تلاش کرد فرار کند، اما پس از تعقیبی کوتاه دستگیر شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126480" target="_blank">📅 13:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126479">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
به گزارش تسنیم دو عضو از یگان‌های پدافند هوایی روز گذشته در حمله اسرائیل کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/126479" target="_blank">📅 13:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126478">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
زلنسکی، رئیس جمهور اوکراین :
- روسیه جنگ رو نمی‌بازه، ولی هر روز داره کم‌کم ابتکار عمل رو از دست می‌ده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/126478" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126477">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
جهت رزرو تبلیغات فوتبالی ویژه جام جهانی و vpn در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/126477" target="_blank">📅 13:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126476">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
یک شاهد عینی اعتراضات روز سه‌شنبه در هرات به افغانستان اینترنشنال گفت که یک کشته و دست‌کم ۲۲ زخمی را از نزدیک مشاهده کرده است.
🔴
منابع محلی دیگر نیز زخمی شدن شماری از شهروندان و احتمال کشته شدن یک نفر را تأیید کرده‌اند. با این حال، تاکنون آمار دقیقی از شمار قربانیان در دست نیست.
🔴
اعتراضات روز سه‌شنبه در منطقه جبرئیل هرات در واکنش به موج بازداشت زنان از سوی طالبان آغاز شد. به گفته شاهدان و منابع محلی، نیروهای طا/لبان برای متفرق کردن معترضان به سوی مردم شلیک کردند و تجمعات اعتراضی را سرکوب کردند.
🔴
منابع همچنین گفته‌اند که طالبان شماری از معترضان را بازداشت کرده و برای بازداشت زخمی‌ها و معترضان به شفاخانه‌ها مراجعه کرده‌اند. به گفته منابع محلی، طالبان همزمان نیروهای بیشتری را در منطقه جبرئیل مستقر کرده‌اند و فضای شهر به‌شدت امنیتی و نظامی شده است.
🔴
طالبان تاکنون به‌طور رسمی درباره این رویدادها اظهار نظر نکرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126476" target="_blank">📅 13:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126475">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ به بی‌بی‌سی: اگر به نتانیاهو بگویم کاری انجام دهد، او انجام می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/126475" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126474">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
تنکرترکرز: نفت‌کشی که در ۱۵ مایل دریایی سواحل عمان دچار آتش‌سوزی شد، با شلیک جنگنده F-18 آمریکا از کار افتاده است؛ موضوعی که سنتکام نیز در بیانیه‌ای به آن اشاره کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/126474" target="_blank">📅 13:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126473">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
سخنگوی دولت: ایران و لبنان نه نیروهای نیابتی یکدیگر هستند، نه برای هم می‌جنگند، بلکه دشمنی مشترک دارند
🔴
تیم دیپلماسی ما متشکل از افرادی است که به شدت به میدان آگاهی دارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/alonews/126473" target="_blank">📅 12:58 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
