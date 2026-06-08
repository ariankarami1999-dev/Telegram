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
<img src="https://cdn4.telesco.pe/file/BHz2rOn3dNwbhVZO33DX8ri94Fc-n1txl5Va6dOPTB_LGCTp2BMYGuglrR9_R370npXe0YoPVhJ3h7S-Q-ILsymc42LD_o34x6f4HDh4lJkIS2QkS2PWHMvBfshOXvutBiicdb29TVJl87-QR9-11umtpov5LzcZJpfIb-Xp1c7PtXgOVSueLg8qihBlmDDGKEmQaJ0mR970RXyuAAfS9ho7p8b78vN9IJPmNSygaRTDOqH50RhuQbXRGJ8Z7YaqIVg9cyAqFKuj3r6Vc0oxVIijg0G-3_-1Yw0HRpL3UzSUHp6_lF8yzoN4Eha3CaYStRCCrG2-ZN7yVGI3b-elwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 304K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 21:14:30</div>
<hr>

<div class="tg-post" id="msg-14052">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/withyashar/14052" target="_blank">📅 21:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14051">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from:)</strong></div>
<div class="tg-text">یاشار دادا فکر کنم اون گز اجیلی که از چهارماه پیش برای روبیو  و ونس بردن تازه داره دعا جادوش  عمل میکنه جنس ایرانیه  دووم  نداره دیر کار شروع میشه زودم تموم میشه
اینا تموم شدن. اینم مثل جنگ ۱۲ روزه یه تست بود که بییین اینا چقدر داستان دارن که فهمیدن فقط بوق کرناس هیچی ندارن
✌🏻
دمتم گرم خسته نباشید
❤️</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/withyashar/14051" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14050">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کنه، اونو تنها خواهم گذاشت.
@withyashar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/14050" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14049">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/14049" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14048">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/14048" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14047">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/14047" target="_blank">📅 20:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14043">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نفتکش
Marivex
با پرچم کشور پالائو را در حالی که از آب‌های بین‌المللی دریای عمان
به سمت ایران در حرکت بود
، هدف قرار داده است.
پس از آنکه خدمه کشتی از اجرای دستورات نیروهای آمریکایی خودداری کردند، یک فروند جنگنده
F/A-18 سوپر هورنت
مستقر بر روی ناو هواپیمابر
آبراهام لینکلن (CVN-72)
یک مهمات هدایت‌شونده دقیق را به بخش موتورخانه و سامانه هدایت کشتی شلیک کرد
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/14043" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14042">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حریم هوایی ایران در حال باز‌ شدن است
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/14042" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14041">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/14041" target="_blank">📅 19:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14040">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند. @withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/14040" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14039">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: حملات موشکی ما تا برقراری آتش‌بس در لبنان ادامه داره
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/14039" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14038">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: ایران و حزب‌الله امروز از هر زمان دیگه‌ای ضعیف‌ترن و اسرائیل از همیشه قوی‌تره، اما کارزار ما علیه اون‌ها هنوز تموم نشده. تو 24 ساعت گذشته، ایران و حزب‌الله سعی کردن قواعد جدیدی به ما تحمیل کنن، اما من این موضوع رو نمی‌پذیرم. همون‌طور که سال‌هاست انجام دادم، روی حق اسرائیل برای پاسخ دادن به این حملات پافشاری می‌کنم.
و اگه ایران دوباره اشتباه کنه و حملاتش رو از سر بگیره، با قدرت بهش پاسخ خواهیم داد، اسرائیل حق دفاع از خودش رو داره و این حق رو حفظ خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/14038" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14037">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/14037" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14036">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو: ایران نمیتونه معادلات رو به ما تحمیل کنه. من این موضع رو تأیید میکنم. پس از اینکه حزب‌الله به اسرائیل شلیک کرد، ما به بیروت حمله کردیم. و پس از اینکه ایران به اسرائیل حمله کرد، ما به مناطق دیگری در ایران حمله کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/14036" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14035">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو: در حال حاضر آتش در جبهه ایران محصور است، زیرا پس از اینکه رژیم تروریستی در تهران آماده شد، دیگر به ما حمله نکرد. اگر دوباره به ما حمله کند - با قدرت پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/14035" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14034">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=S1Au62P8kothmFPkTDtSpJ_vzwned_aN4ojW1hIg7bbsRsombbm6zI_S8WIYALAA6yvJ1iqAySAELtM1zq3DBr1zo1RwwC9qTPIQvzMMfr9de1OPdqk1hC7GXynUVvkwJlZSj5Fcqb1PjvySwa56Qk7P84qENQsgLu65ROGybAc8vFNipAUtgRIoC2G_CNLEKrc7bEN0mNH9B36dXDcSh_4O4mHXiYsDqgo_KwGevzxTzyi9Up4h9RVgmLrlYMOqpN7YCbiEv_Y7LT0NG_pPSCTqh3IvF34H7OdFS6fxItXXCQeh_l89SMMJJf_jGHqHFJVxWZps_kRK-MVVUXLliA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=S1Au62P8kothmFPkTDtSpJ_vzwned_aN4ojW1hIg7bbsRsombbm6zI_S8WIYALAA6yvJ1iqAySAELtM1zq3DBr1zo1RwwC9qTPIQvzMMfr9de1OPdqk1hC7GXynUVvkwJlZSj5Fcqb1PjvySwa56Qk7P84qENQsgLu65ROGybAc8vFNipAUtgRIoC2G_CNLEKrc7bEN0mNH9B36dXDcSh_4O4mHXiYsDqgo_KwGevzxTzyi9Up4h9RVgmLrlYMOqpN7YCbiEv_Y7LT0NG_pPSCTqh3IvF34H7OdFS6fxItXXCQeh_l89SMMJJf_jGHqHFJVxWZps_kRK-MVVUXLliA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد، زیرا اسرائیل حق دفاع از خود را دارد و ما این حق را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/14034" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14033">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئیس جدید موساد، رومن گوفمن : مردم ایران را مسلح کنید , بازی را تغییر دهید
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/14033" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14032">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسرائیل هیوم: درگیری 24 ساعت اخیر نشان داد قدرت نظامی ایران حتی نزدیک به شرایط قبل از جنگ هم نیست.
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/14032" target="_blank">📅 18:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14031">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">قالیباف: معادله آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان رو به هم زدیم. تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14031" target="_blank">📅 18:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14030">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه I24News: اسرائیل به پمپی که مواد را در کارخانه بزرگ پتروشیمی در ایران حمل می‌کند حمله کرد. حمله‌ای به یک قطعه حیاتی (و گران‌قیمت) با هدف از کار انداختن کارخانه‌ها.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/14030" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14029">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو دقایقی دیگه صحبت میکنه</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/14029" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 99.7K · <a href="https://t.me/withyashar/14028" target="_blank">📅 16:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14027">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=bRPekXh2J6tz6U7myPSkE6XKr9V_8hfu6FRbLy9hrWui1S-kgqcnViJUDD4uETrENb_6jaQWk_cjwZ4Xvbdk8X6FNnNYjErYi8LVkAtaVf2goSvE46H0rAtUwixxZZ1sWuYZgZKUM2J_sNfXoIyhQIQ_Dbak8vNbUe6UiM3PM6N6NKKxqCHJKBDyHv3NE5IvDldR_c1zcqMojUnvXRM8f3pS2jdZlzJ_wuqjvcA3P6cE2TXC1RgFysPojg2l003zKMszi6Rf_wR5HybA9dy8RGaYwUwDoPESdjJyRmqhhgJk0iuEcGqvpw_dvn-ujvCLKzvz9cc5U48miLd-u6CaEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=bRPekXh2J6tz6U7myPSkE6XKr9V_8hfu6FRbLy9hrWui1S-kgqcnViJUDD4uETrENb_6jaQWk_cjwZ4Xvbdk8X6FNnNYjErYi8LVkAtaVf2goSvE46H0rAtUwixxZZ1sWuYZgZKUM2J_sNfXoIyhQIQ_Dbak8vNbUe6UiM3PM6N6NKKxqCHJKBDyHv3NE5IvDldR_c1zcqMojUnvXRM8f3pS2jdZlzJ_wuqjvcA3P6cE2TXC1RgFysPojg2l003zKMszi6Rf_wR5HybA9dy8RGaYwUwDoPESdjJyRmqhhgJk0iuEcGqvpw_dvn-ujvCLKzvz9cc5U48miLd-u6CaEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر
⚠️
اگه ناراحتی قلبی دارید نبینید
🤣
بی اختیاری ادرار میاره
این ویدئو رو صدا و سیما خودشون پخش کرد!
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی برای تنگه هرکز
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14027" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بریتانیا هشدار تخلیه به شهروندانش از اسراییل رو صادر کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/14026" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14025">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUtHQQUT9NVVRuTP5Ec_l5mNGEuMzCmPRzy5-7EERQrFJwkCtGNYDqhY3-r-0MmikWgp4_x-ggiMQ-qhWoR6ak0VhdpW-gXU6xFURcBBmtsN7AOClxENlg-6lLhPM_WEYooNO34TdHklqS0FIKGtQVq9VTN7XflE9TWw3CZSkT7aGNKIwuZWLOgDGbSWVGKH-h5V2F2gg0fbgHU-p0WtEsDSZAnbHYcCtARHdJWg9-PAyz-tcmkrge1vcLEVNEsWPFMusyBxcCyr2cNm8dWf5_Vpvo_SerAIUxiuZ0tqvJf9sr0vrmLakDq7FSv4SeIQ9pFQGuh225PKZTuaVC1rkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هم داره جنوب لبنان رو خیلی شیک و مجلسی هوایی میزنه.
@withyashar</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/14025" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14024">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/14024" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14023">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترافیک سنگین در محورهای چالوس و هراز
@withyashar
خوش بگذره به هم وطنام
❤️‍🩹
جای‌منو خالی کنید</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/14023" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14022">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/14022" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14021">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9eAXmbs87hMtPl30hgkclBjwSAXpq1iIq7Y3s6jvtqIYjz8C20jsg1j8490aaIgUIy9968BOwgirtpuZyL72pSvt5EXZawe5z6IjCgcn-ndiODt7QoBfYCx-ONvHzskLz4LPE-71-mPnRVWKYypooOzixHJZU-1iS4HYreb3CzU29_hIK7PBWBFKl0P9gSyV1SdTHbe-Zr0bM86Jn2W25W2DrWbU1JRzuZwxv2WPlShha75wicDLTmQ-Fawe7ZB8oey2Ou1NLWvDU44avOTWGL03339wk2zlZkgDnjopeC3OjHeLFtNpTFS5aTdEqvx4PkQ6LhNNP4wGD8HLQ3cCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/14021" target="_blank">📅 16:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14020">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/withyashar/14020" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14019">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حزب‌الله هم حمله موشکی کرد به سمت اسرائیل و آژیرها فعال شد.
اسرائیل : 5 موشک رهگیری شد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14019" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14018">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
تماس تلفنی ترامپ با نتانیاهو «مودبانه» بوده، اما نتانیاهو با درخواست ترامپ برای توقف اقدامات بیشتر مخالفت کرده.
به نتانیاهو صراحتا گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت نکرد و از آنها حمایت نکرد.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14018" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14017">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عراق از بازگشایی حریم هوایی خود خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14017" target="_blank">📅 15:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14016">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">کانال 12 اسرائیل: ترامپ و نتانیاهو دقایقی پیش صحبت کردن.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14016" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14015">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هم اکنون اسرائیل به لبنان حملهِ کرد
@withyashar
😁</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14015" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14014">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">صدا و سیما:جنگ پس از شکست دشمن به پایان رسید و زندگی به روال عادی بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14014" target="_blank">📅 15:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14013">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تحلیل کمی دیگه در‌اینستاگرام پست میشه</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14013" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14012">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14012" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14011">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=KeEEuVwzqDennR11slOvCQUPxmTTvm5g_zW8iAychaefUNEr_D877aYl469riho_jL-rP-FIDO-axxK2UbvXuB_iWyjVhrXCcvzkHjwTkfM_RRY0txp-HUzeCCqfh4HWRYyWwKmKzEUxctq1wUKKf0-nHPOTIxZXJ9TN9GRcoAjtAk6TtdF0KfgJ6AUecikZFHZsIdpZLoXNbfEmE44X-UKMkwmZtAdB-QSq91Py6wuZPxm4AbqZRwc-S7NjvIKr3q_23s0JD8I3PKsXEUMMDl5XGrO8K2btCXqTYMh1UTPzDFXKi87wFQNugcwg1StweP6jjdWF-lt6dGLFAFrBNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=KeEEuVwzqDennR11slOvCQUPxmTTvm5g_zW8iAychaefUNEr_D877aYl469riho_jL-rP-FIDO-axxK2UbvXuB_iWyjVhrXCcvzkHjwTkfM_RRY0txp-HUzeCCqfh4HWRYyWwKmKzEUxctq1wUKKf0-nHPOTIxZXJ9TN9GRcoAjtAk6TtdF0KfgJ6AUecikZFHZsIdpZLoXNbfEmE44X-UKMkwmZtAdB-QSq91Py6wuZPxm4AbqZRwc-S7NjvIKr3q_23s0JD8I3PKsXEUMMDl5XGrO8K2btCXqTYMh1UTPzDFXKi87wFQNugcwg1StweP6jjdWF-lt6dGLFAFrBNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14011" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14010">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود @withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14010" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14009">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14009" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14008">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیهش نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14008" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14007">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=B79DE0KuwcVWYl71-Lo9W313yrGdhcFfuxEfk02TJIh3ZW2ulxUDcNn0mECFgjWLaknSD2hLpQIRYOY1wW0G2U5DTSbyNNtxqbc2SwDqVzlGu6QLq9oaXxWCAZ_uDIUrCms7tnKxnWgLHlT1YT_gNBrTU2i-VzFuEpWW5uDa_AOg3uGJv2w8ODn0EAcPbDSGdyYtOua4Kf6dkAHEiUlX8m8aTpdEHEraeZ3WCc25bGTS1DlMow6BGaTXdWlks8uh98TyKaDaZEerHUl0GJ7PnN5GTnqWZzZVhyXaOgiAUdM01HcD4nq4ZlIfyWETj3G_qADrznwVWqcBiDIf0Ymm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=B79DE0KuwcVWYl71-Lo9W313yrGdhcFfuxEfk02TJIh3ZW2ulxUDcNn0mECFgjWLaknSD2hLpQIRYOY1wW0G2U5DTSbyNNtxqbc2SwDqVzlGu6QLq9oaXxWCAZ_uDIUrCms7tnKxnWgLHlT1YT_gNBrTU2i-VzFuEpWW5uDa_AOg3uGJv2w8ODn0EAcPbDSGdyYtOua4Kf6dkAHEiUlX8m8aTpdEHEraeZ3WCc25bGTS1DlMow6BGaTXdWlks8uh98TyKaDaZEerHUl0GJ7PnN5GTnqWZzZVhyXaOgiAUdM01HcD4nq4ZlIfyWETj3G_qADrznwVWqcBiDIf0Ymm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل : ما سیستم‌های پدافند هوایی رژیم تروریستی جمهوری اسلامی در غرب و مرکز ایران را نابود کردیم
‏پس از حمله، انفجارهای ثانویه‌ای شناسایی شد که نشان می‌داد موشک‌ها در پرتابگر بوده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14007" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14006">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=oL6N1oRqE03oNxNoFMVYbYiSn5PKzUVUd5CJdPBP5fXxoY2LNySJfzY8Mc2yQB1BwP8ON_4OgwZdi6PupHIId0GX248paG91Kb00_W_TETX-06WB92wd1bEPzLHGy0BIP-gcf6Qb0s2giz-PqiXTVAkOwWjlV41-eJsVsHbP9_hkhLmpNcKoQ6a5EgmNaCDrpZ1to2jYyp075DzNvHMCJmtdUB8e8hwDvTxGTwXjOKbheQ5paxjj1FYft2ER3ipySqRHBlWx20dKQKOJHy8CzwxEkuNQCLReWh42dGKzWLeEMD3RMkZBUZ6LFUIpvW6wF5BPiUXpTfDCgMcSwPLd1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=oL6N1oRqE03oNxNoFMVYbYiSn5PKzUVUd5CJdPBP5fXxoY2LNySJfzY8Mc2yQB1BwP8ON_4OgwZdi6PupHIId0GX248paG91Kb00_W_TETX-06WB92wd1bEPzLHGy0BIP-gcf6Qb0s2giz-PqiXTVAkOwWjlV41-eJsVsHbP9_hkhLmpNcKoQ6a5EgmNaCDrpZ1to2jYyp075DzNvHMCJmtdUB8e8hwDvTxGTwXjOKbheQ5paxjj1FYft2ER3ipySqRHBlWx20dKQKOJHy8CzwxEkuNQCLReWh42dGKzWLeEMD3RMkZBUZ6LFUIpvW6wF5BPiUXpTfDCgMcSwPLd1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان کرج سمت میدان استاندارد و فردیس
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14006" target="_blank">📅 14:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14005">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14005" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14004">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزیر آموزش و پرورش اسرائیل: تعطیلی مدارس فردا سه‌شنبه نیز ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14004" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14003">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرنگار I24News خطاب به پست رئیس جمهور ترامپ:
من واقعاً نمی‌دانم این مذاکره درباره چیست
این مذاکرات به مدت یک هفته و نیم به دلیل لجاجت ایرانی‌ها متوقف شده است. پیام‌های ترامپ هر روز خجالت‌آورتر می‌شوند
و تا جایی که می‌دانم، اسرائیل خواستار آتش‌بس فوری نیست
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14003" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14001">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcEJyyrNmcse30ytnETLJR8U2LJucwAee-xMAJS8DhrU4Fw7vBG4aMfgKNkZlbcsMHcOCV5PJpH-dG1mWLQ7e1VaNRU3I2ulfgMva8VUxyt3zOnaQntrzQv0y70PXbVRLcULMnLlHA9-X4cED--1t3M43oHPXNkZOJfU0gTay0I29pemygOKeqwrVOC__I4TZqm5syCkTWFddRCSDcpbX6Vi8hnFVg6Abf0O5nSqIhtdmWWvVFzbRit0SlioPKy3XnGXu6HBsqzCfbUvgQnf__ZlTik2yO74_kXT5El3WCAKw9Ay1JuiG_SRd2AXqCph8AvwC0iPpaepIZhPMiQH6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14001" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14000">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8r3D60-kghPLzPWiOE-rlaH7V03yMJyPuAnbMYO_PHg4DXXZ1h90EeZ8eB-54j4MnYklEXN7fF7jQIbMFVyOfF0lxK6Ra_eDKlDJLFsZ9GY9tTfjzeXzDzfci7KNb8dZLSNsx_C_Le1XmH_A-7jdgGeSoOB4KTCTGs2CRF6Mx3_Q122d8dpvTJLCW0424ybDKVFGgnKC58oTn2w4ygFpHC8EYHReJp2Ocs7IeI-YFFwROcpKkI7DiYhQV2d4ZE-205q7M6UkshFPruIvSJPJ_CzOnCGlmQvqLpq7YQBhiOVpa7ZUzbOHG2INXPy5QiBbrAp-BrZMKgzBGkwVXNS_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود از انفجار در شیراز، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14000" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13999">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های رژیم : پدافند یزد فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13999" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13998">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=EznLXaNilvyVuUH4xXcwouRCui8QjBOZIh_dPT482PNNJkjpEHXKDJA-GeIzqySlnCeTnaiBhuixjPEfMqqXLLqQPUgOnBG6-BJTX_mkhiwTvCOmzQ9GpqFPHE_D05Tfn1kG9SbbhcERVvGR0IEd4ZASUS2G9BBEhyWNnZjp7xkCYCpHy8o__nSXuiksyMeA0_SxvFXTnELgRtF3L0oshDY35Ib5OM8ebnKkRilU2rmKFqYibHce7d7Ky3xCGQYbrKC9sP4WCm47jAm9vNfBAJlAhYupX7YRg3RMmwV93815Oiy0Kb2bZK99RGzL9Da05M1HTijwwTAbqT-RpVVzbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=EznLXaNilvyVuUH4xXcwouRCui8QjBOZIh_dPT482PNNJkjpEHXKDJA-GeIzqySlnCeTnaiBhuixjPEfMqqXLLqQPUgOnBG6-BJTX_mkhiwTvCOmzQ9GpqFPHE_D05Tfn1kG9SbbhcERVvGR0IEd4ZASUS2G9BBEhyWNnZjp7xkCYCpHy8o__nSXuiksyMeA0_SxvFXTnELgRtF3L0oshDY35Ib5OM8ebnKkRilU2rmKFqYibHce7d7Ky3xCGQYbrKC9sP4WCm47jAm9vNfBAJlAhYupX7YRg3RMmwV93815Oiy0Kb2bZK99RGzL9Da05M1HTijwwTAbqT-RpVVzbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13998" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13997">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلیه
@withyashar
🥴</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/13997" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13996">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب ساعت 9 به وقت اسرائیل تشکیل جلسه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13996" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13995">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سرپرست سرکنسولگری ایران در کربلا: هماهنگی‌های لازم با عراق جهت انتقال حجاج انجام شده است
@withyashar
حجاجی که نیومده بودن باید برن عراق زمینی‌ بیان</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13995" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13994">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13994" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13993">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034343a08d.mp4?token=K_Fz2_NIkrJ1vcWX-ooUpvWu3KpHlcTKnHKbB3oNAJG2tRln79u_rOQ5yIuNUQmRF6KSLCbcSuSIKKPZ5kKaKxMQhSdlQQkT4-1Ah2xLw386gKbrN9h7BqnTM1KLMmaRNtut1EBJC6c3JSakZVd0juS7uL2MTkwToDc9EXMMMsd_XkZa4jzXbpWZ72y6MDg_G7ogL2U7vYuaiKLZT9bukiHn25ES8T5iKqpfoYTd8dLjlFiGp7NjXUK_t19Vm0rWKK9xdtIBr-pUeY2HYtbxSJgRPmSwMhEO_9UZcQiDANT3KSOwkoJUwx0SISAz-cU-AGtLUgKk3uSEauMT4r_bug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034343a08d.mp4?token=K_Fz2_NIkrJ1vcWX-ooUpvWu3KpHlcTKnHKbB3oNAJG2tRln79u_rOQ5yIuNUQmRF6KSLCbcSuSIKKPZ5kKaKxMQhSdlQQkT4-1Ah2xLw386gKbrN9h7BqnTM1KLMmaRNtut1EBJC6c3JSakZVd0juS7uL2MTkwToDc9EXMMMsd_XkZa4jzXbpWZ72y6MDg_G7ogL2U7vYuaiKLZT9bukiHn25ES8T5iKqpfoYTd8dLjlFiGp7NjXUK_t19Vm0rWKK9xdtIBr-pUeY2HYtbxSJgRPmSwMhEO_9UZcQiDANT3KSOwkoJUwx0SISAz-cU-AGtLUgKk3uSEauMT4r_bug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش السیسی محموت احمدی‌نژاد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13993" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13992">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-NNzJcbHDoVf8NzWc2g66tYQ4Qsmuua_n459fxiJsb6559jNbwsJJy0E50vKFHLo9J_ROxer7qdeDC26htMMsrbsQZCgH0bAWqyPByhWoR4XdgbY13cMH0EO9u4hEPBfe3BLflkhLJKnEt4XrLX05XoFLo-GZBOe8YPTVSd5XabwozSvcMUy5MAsTuPdFHAu4CDbjbFhu2YyzRrDC6pZFDedot_-dzKGL4mRRlXGdGF-YO7ayOcyzWYVxCOEN7lt4nxRzqOaWChjBcb2gSs5I_WEzsiHD9FC5jHUyU12AjeGFcjI5pmZPt0aO1KZv6lw2t4DsZGLCTT2cU3BxkZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به سایت موشکی تنگه کنشت کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13992" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13991">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یک منبع نظامی به تسنیم: ایران برای جنگ طولانی مدت آماده شده است
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13991" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13990">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رسانه های عبری: درگیری ها تا ساعات آینده گسترده و سنگین‌تر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13990" target="_blank">📅 13:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13989">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنقلات خود را آماده کنید</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13989" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13988">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یک منبع ارشد نظامی در ایران: حزب‌الله  روزهای آینده نشان خواهد داد که محاسبات اسرائیلی‌ها و آمریکایی‌ها همیشه اشتباه است، و ایران ثابت کرده که دوستان خود را رها نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13988" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13987">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فارس: تو غرب تهران پهپاد زدیم
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13987" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13986">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ با لهجه استانبلی
🤣
:
📿
الله لله</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/13986" target="_blank">📅 13:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13985">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ @withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13985" target="_blank">📅 13:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13984">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ @withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13984" target="_blank">📅 13:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13983">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">مسافران محترم قاهره لطفا آرامش خود را حفظ کنید دایرکت جای  فحش‌به ترامپ نیست از مسیر لذت ببرید
🙌🏾
😁
مدیریت حمام اتاق جنگ</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13983" target="_blank">📅 13:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13982">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همکنون دو تا از رادار های بیدگنه رو زدند
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/13982" target="_blank">📅 13:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13981">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRT3TIxlcyb8Isvh8k6oSwDIas8OiHBxkBZB-8_RI0EgxZpsBvRUvnirzLxGedOxARe0F_90OeqvoWZQ42Ud_GumfwXqVjJQWPLBDZvQr1to_Z0_NooBv0VjV1BoJcVi6gESFk2Rcz73DHU9j5pkn3oBTv1xzDH6F468upIQ0vATFSXeXROVwLkznN9-4tAvFSRvtu9Lc4O_VZMf-Gdl37xj59H9he3GU2IgdE9rJ5EIQe5ipfwv1Vh83duafPnM_AHPY8mLbWWzrIy3iLflQ39FHaS3q53RqvZLkNOs2w36m_P___5GTfl7TmS5SwEqwOiRy7NE8k_9Kp_DLfnlBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل و ایران باید فوراً «شلیک» را متوقف کنند. پرزیدنت دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/13981" target="_blank">📅 13:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13980">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کابینه امنیتی اسرائیل ساعت یازده و نیم پیش‌ازظهر دوشنبه به ریاست بنیامین نتانیاهو تشکیل جلسه می‌دهد.
این مقامات همچنین گفته‌اند هر حمله موشکی ایران به اسرائیل «با حمله در ضاحیه» در لبنان نیز روبه‌رو خواهد شد.
وزیران راستگرای افراطی در دولت نتانیاهو به او گفته بودند در پاسخ به حمله موشکی ایران به اسرائیل، «تهران باید بسوزد».
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13980" target="_blank">📅 13:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13979">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ارتش اسرائیل: برای احتمال شلیک موشک از سوی حزب‌الله به خاک اسرائیل آماده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13979" target="_blank">📅 13:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13978">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یک منبع آگاه در حوزه ارتباطات به سیتنا اعلام کرد که تاکنون هیچ دستور، ابلاغ یا تصمیمی درباره قطع یا محدودسازی اینترنت بین‌الملل به دستگاه‌های مسئول اعلام نشده است، در همین حال شب گذشته پیک ترافیک اینترنت بعد از قطعی‌ها زده شد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13978" target="_blank">📅 13:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13977">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سازمان ملل از شرایط موجود ابراز نگرانی کرد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13977" target="_blank">📅 13:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13976">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کانال 12 اسرائیل: ارتش اسرائیل در حال آماده شدن برای احتمال جنگ طولانی با ایران در حالی که عملیات "غرش شیران" ادامه دارد همچنین در حال حاضر اهداف جدیدی نیز مشخص شده است.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13976" target="_blank">📅 13:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13975">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۲ اسرائیل: تاکنون، ایران بین ۲۲ تا ۲۴ موشک به سمت اسرائیل شلیک کرده است
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13975" target="_blank">📅 12:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13974">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13974" target="_blank">📅 12:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13973">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رادیو ارتش اسرائیل: در حمله به حومه جنوبی بیروت تردید نخواهیم کرد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13973" target="_blank">📅 12:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13972">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فوری رئیس ستاد مشترک کانفیگ فروشان به ادمیرال یاشار رئیس اتاق جنگ گفت :
آماده‌ایم تا به هرگونه قطعی اینترنت پاسخ‌ کوبنده بدهیم
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13972" target="_blank">📅 12:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13971">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اینترنشنال با استناد به ارتباطات زیرپوستیش : ارتباط مقامات و فرماندهان با مجتبی خامنه ای دچار اختلال شده.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13971" target="_blank">📅 12:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13970">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFEdODGmP-YcuVWRlfz0kJ957D0Zh1h2uupCF2ASZ3ag60Ts_8shkCYZdQNiITTR3zmXvtFMvDlpNFuFaNLAoevLTOmZxx3GpqlJuk7lAvoWKo_2eCdqVSV_bu1HZ3vZkJT0uHMO_VzLgHa1S1-yNPWXectIHQzTzNVExi5aGNx7Cnq4gnYTZzNIizZ4ico_4v_NCwTyseo3VtxZLbEWCIkdkaBvbjpSsPpDvdH_dUvijSTVxqc-LAHSCbnqjPGwh6fjzAdS4ZN0uHEPEXnW58Imkd90FhryykWOIr2bSHFZsOM39T7Hfqa_-EYaJaHcYzLDMuksY5f5RoM0Qq_leQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساعاتی پیش ایران موشک به سمت اسرائیل پرتاب کرد که گویا وسط دریا خورده
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13970" target="_blank">📅 12:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13969">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگه تازه بیدار شدی بدون که آتش بس آمریکا و ایران همچنان پا برجا است
🥴
🤣
@withyashar
ترامپ هم کابل رو گرفته و پستهای انتخابات میزاره…</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13969" target="_blank">📅 12:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13968">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تن و بدن عرزشیها داره تو دایرکتها میلرزه و چرتو پرته که مینویسن
😁
. اینها به هیچ وجه فکر نمیکردن که دوباره حمله شکل بگیره.
@withyashar
با عرزشی سوز ترین رسانه نسل شیک پاسارگادی با شما هستم.
✌🏾</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13968" target="_blank">📅 12:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13967">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش اسرائیل گزارش می‌دهد که حملات به ایران تنها توسط اسرائیل انجام شده است و هیچ مشارکتی از سوی آمریکا نبوده است
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13967" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13966">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دایرکت پر شده از مسیج‌هایی که چرا نمیشه تو چنل عضو شد. من اون سمت توی گوشی شما نیستم این علت رو بدونم ولی محتمل‌ترین حالت لیمیت شدن شما به علت استفاده از فیلتر شکنه ، اگر IP تون رو یا ساده بگم فیلتر شکنتون رو عوض کنین این مشکل حتماً حل میشود.</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13966" target="_blank">📅 12:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13965">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه های رژیم: خبر ترور فرماندهان یا مسئولان کذب است؛ هیچ تروری تاکنون انجام نشده است
@withyashar
یاشار : حالا نیس اینا خیلی گردنم میگیرن !
🤣
اول همیشه اسرائیل اعلام کرده</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13965" target="_blank">📅 12:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13964">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">روسیا الیوم نوشت: ترامپ به پیاده کردن نیروهای ویژه در ایران تهدید کرد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13964" target="_blank">📅 12:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13963">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">خبرهایی پخش شده از حمله به ایست بازرسی ولی هیچ گزارش مردمی در این رابطه به دستم نرسیده. به نظر من این خبر فیک برای توجه یا امید واهی است، فعلاً! ولی حتماً شروع و انجام خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13963" target="_blank">📅 12:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13962">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صدای جنگنده مرکز تهران
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13962" target="_blank">📅 12:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13961">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نائب ریس کمیسیون صنایع: امکان قطع اینترنت بین‌الملل وجود دارد
بالاخره شرایط جنگی است و مصلحت ایران اولویت دارد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13961" target="_blank">📅 12:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13960">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2689f38b.mp4?token=Wor0Rgg_wfeVW20sNLlZUstV5qSOi-jdLYQ3HYLF030Xg2m9Domdk5uhbeOyNGx1x8-G5sIMhNiqpH0AdgRsln-Oe8sjEc8UYXmh4qU8D5XhEVT3T2wy6djmyRR-9AIlmYEKG_jtYY95s7uGjFxNxS0OhkpbIVILnMCCpFN-dX6nWVvunvoJmsZA74WsT-jbCo4ai15ZYlg-v_7Cd9L-W4go60hUd0K3JrUGh1a-mKLgjrpT4TxuqQ0WkHlothKcCVG3EW4IQX3ChaultuD3JgTtM4oKyjXbqdlAjfuXPP17UctRSzi6OE1cGVLV_GeTBa3eX_RoImTOUT4nXdaJxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2689f38b.mp4?token=Wor0Rgg_wfeVW20sNLlZUstV5qSOi-jdLYQ3HYLF030Xg2m9Domdk5uhbeOyNGx1x8-G5sIMhNiqpH0AdgRsln-Oe8sjEc8UYXmh4qU8D5XhEVT3T2wy6djmyRR-9AIlmYEKG_jtYY95s7uGjFxNxS0OhkpbIVILnMCCpFN-dX6nWVvunvoJmsZA74WsT-jbCo4ai15ZYlg-v_7Cd9L-W4go60hUd0K3JrUGh1a-mKLgjrpT4TxuqQ0WkHlothKcCVG3EW4IQX3ChaultuD3JgTtM4oKyjXbqdlAjfuXPP17UctRSzi6OE1cGVLV_GeTBa3eX_RoImTOUT4nXdaJxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از پایگاه عظیم کوه معروف یزد الان شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13960" target="_blank">📅 12:22 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13959">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یه سر برم بیت رهبری الان میام
🥴
🙌🏾</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13959" target="_blank">📅 12:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13958">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">شهرداری تهران جنگ بیخ داره و داریم پارکینگ‌های زیرسطحیو برای استفاده به عنوان پناهگاه آماده میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13958" target="_blank">📅 12:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13957">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU8cxZ7V7Ho8lSMZwJRblcHRKqo-MXQRWkfauVK_UmOlrqHyVo2aA6ubIYMLULdA_clpCnHviXzk8tbZx79JmPW0RyR16wS54SI0soglGJb29Dt7d_0qwmoDm8s7zTqFpSbQI1T79SRA2p18Hwoff3vhtrB8tvydnxBj80QZ3Tjw_7LGla9nn09KPycd7PypiPxsyGy_vHB7k_s1zl2BSk62axDnioKFKWoW815cv2UnShD8K6lunCeH-_WY775v4L7LJSZouuVRsMI_QycPkawnZcEkCuPpkhg38aaEmGb9q1fJhxlWnCz6heqYBzzqxETNu6aGYtUMpuYTHB6PEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۰۰،۰۰۰ امین نفر کانال خانوم پی ام
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13957" target="_blank">📅 12:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13956">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
گزارشهای از یک تررور هدفمند در تهران
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/13956" target="_blank">📅 12:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13955">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoLKijcTxV1xMIA9GGawzxjvhqHI67JWeyexsLj0y8WsH5NQVA6E-txEhRY1SiA9fisK7Ys7FQlM1wn7kiuLapPn9nRlU9JbgDxhmJ0AD78wSMOhlNOaK1e9BO2KUCDk4ukpQmNkiTc7v9qEdcMPf2FN9k_6MDOXpcAYcRACbamukRopUtnKtsNug23j8uRIfVr79ASHt6E3mqFEH3mbpp1uoD3X4tjK4yjJ-jqCtKLKV3HmtDNbcayaGUtp5c1lpX1a2xGc_M_sLHAjtwI0FEG9F--GGlR5us1YGuIDElRmK2DOkoWwb6kVQGRuZVLIRNkcy6L6pjGFeU8Ca2dJmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهده دود از شرق تهران
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13955" target="_blank">📅 12:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سفارت هند در تهران از شهروندان خود می‌خواهد فوراً ایران را ترک کنن
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/13954" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رادیو اسرائیل: همکنون نتانیاهو ریاست جلسه‌ای کوچک از هیئت وزیران را بر عهده دارد تا درباره مسائل امنیتی و سیاسی در تمامی جبهه‌ها بحث و بررسی کند.»
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13953" target="_blank">📅 12:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13952">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گزارش چند انفجار در جنوب تهران
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13952" target="_blank">📅 12:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13951">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کان نیوز عبری: نیروی هوایی درحال انجام عملیات در ایران است
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13951" target="_blank">📅 12:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13950">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فارس: موج جدید حملات موشکی در راهه.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/13950" target="_blank">📅 12:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13949">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2Px_ana9Abh-8T9JECIWJlF5o-5T6EsDVujyeQYmBngyUuIgOGhJdD8R9H3HxUJPa6QWMwtM_aR9lwLe0BHEacXWwsgwf3gd9qZ8AATV8fGErSJN3LIeoPJaUDPwdsAcVbLshYIf647W4y8f6ciiVy2PhsJmuA2lnHvbgik7KjkIMd64taHyOhzs2mVc3xyWLKl2i-nWevItZ51HSoNVJsgxwLrXbq0DTUWL4TfccjfLn4AMpUZadqVOVgkko5E_C5bHP7GV_tg19veNeSXUextFxzExNU_2-dj11bgmzYejm2wNk5ndTKpCY8z-ydjHZiwsYlVWJavDfiKdD-KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان الان
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13949" target="_blank">📅 12:06 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
