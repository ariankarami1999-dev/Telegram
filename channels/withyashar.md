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
<img src="https://cdn4.telesco.pe/file/m7HSI1CjuaMlUgPzCXjAL96xqjICtueWt1IoRvdB6H3K-ysZiXycVYiBijw3TsJ1JqG_wQi2qakPz2_HKw-mnsRsjBc2QwZfQL-YQNz4YgrUIt2eYaP2HnZG2OlsBJAunSyT_l8uFUvprdZKiwoZ64pK7Yd9Ep_3dnlN5PwOYa8xjlYQ9RnSjjDZQ2ECjt3YyBqxbq-C8YVjgSUgo916Bpf4tSG3uVoHFUBkAB8lqLBoY4iF3AaaZcW4kN2tvofDS7-1JAGNqt4uAAQv59FgeBxdKglRpIsGdCbeL8brnmkwCYHhxZMACPI91xltaE9zMUxhlSEpP1MG9Dew-XVCWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 332K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-16044">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گل دوم کنگو توسط مایله در دقیقه 78
🇺🇿
ازبکستان 1
🇨🇩
کنگو 2  با این نتیجه دومین شانس تیک ملا هم از بین میرود  و فقط یک جون دارد @withyashar</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/withyashar/16044" target="_blank">📅 04:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16043">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدا های انفجار مانند از بوشهر ، یا داره میزنه یا میخوره ، یه خبری هست
@withyashar</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/withyashar/16043" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16042">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حمله‌های متعدد ازبکستان روی دروازه کنگو  ازبکستان
1️⃣
-
0️⃣
کنگو  با این نتیجه تیم ملی صعود میکند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/withyashar/16042" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16041">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dub9Jiia37p_tGRH_k2cxgDrUBxy1rc26dt9bVLUgpgS3eDN9FD70_u8doMM33mSYH5uq5WqK7kERUxNlNHZ17PzSYIzrOLmZYYzAk04lkF0n-bsPMlN-7H3ccD68rDg6Re2OA9E1ZZLXzy3JMpTRypcoFhL8TKRyVsRB2BLstZ7d-FjSUkgGejNZewDRylmWCjrX84B-OnjVzUnt9Ip6dJ8_zpMNLnrXtJsYdwyNaF3LulN-2faD8yxS8nKUo2wGaykXre9DapDjhRIuNJtfcmlz5P0glaWzz6vUT_KR9ElI_ldIlNmVPO7i63_h-2KDpWcUsPmkSkc9hJzGJ5W2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک شیء ناشناس در آسمان بحرین در حال پرواز است.
@withyashar</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/withyashar/16041" target="_blank">📅 04:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16040">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد نیروهای دریایی و هوافضای این نهاد، در پاسخ به آنچه «تجاوزهای اخیر آمریکا» عنوان شده، عملیاتی مشترک با استفاده از موشک‌های بالستیک و پهپاد علیه چند هدف نظامی انجام داده‌اند.
در این بیانیه ادعا شده است که در ساعات اولیه بامداد یکشنبه، چند زیرساخت مرتبط با نیروهای آمریکایی در منطقه از جمله در کویت و بحرین هدف قرار گرفته و «منهدم» شده‌اند. همچنین به حملاتی از سوی آمریکا به برخی نقاط ساحلی ایران اشاره و تأکید شده است که در آینده برخورد با کشتی‌های متخلف در تنگه هرمز با شدت بیشتری انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/16040" target="_blank">📅 04:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16038">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">موشک‌ها در آسمان بحرین در حال پرواز هستند و پدافند هوایی نیز درگیر شده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/withyashar/16038" target="_blank">📅 03:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16037">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اطراف بندرعباس شهر تازیانپ روستای خونسرخ صدای چندین انفجار ، قشنگ لرزید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/withyashar/16037" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16036">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله‌ای جدید این بار با موشک در بحرین.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/withyashar/16036" target="_blank">📅 03:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16035">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/withyashar/16035" target="_blank">📅 03:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16034">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پدافند کویت فعال شده
چندین انفجار شنیده شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/withyashar/16034" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16033">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای آژیر هشدار در کویت
برخی گزارش‌های تاییدنشده از فعال شدن آژیر هشدار در کویت حکایت دارند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/withyashar/16033" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16032">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/16032" target="_blank">📅 03:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16031">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گزارش رسانه‌های خبری رژیم حاکی است که پایگاه هوایی «شیخ عیسی» در بحرین هدف حمله پهپادی قرار گرفته است
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/16031" target="_blank">📅 03:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16030">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ در تروث: هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران، و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!  بسیار محتمل است که آن‌ها هرگز درس نگیرند!  ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار…</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/withyashar/16030" target="_blank">📅 02:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16029">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8eQFQBYLbO-ueuAEqrGKxu8uxhqe7ELGfDIHh9XmUxVDAdHO9cUoyyT5ZQo_UYvEBHTfbilpR_lj4Pm4bYZ4HVmKtFN2_mKXhi36-bsU5mQWpuM6uEeLltMJnv5Nz_3CVtCvsL_ySFyiPD98jgviN9FDPFtU3km6kHZfZk7sJQXcAt5Ke1dYOpCvgM7TELNR9dMKvJbiT1uEMrrY6a7X_Aivs5G0kfBwsW95zfqHcrVKr1AcTnOmKAl7cihOVI_k4VHNoLeJv77JpozzgjBNmHrZmqP2Ljba4KjDcrV-ITIOMGlYkxUZEq6SnDdEAxRk3h_xZ8PVPSatYJzuRYgvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران، و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/withyashar/16029" target="_blank">📅 02:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16028">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/16028" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16027">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صداوسیما : جزئیات عملیات امشب رزمندگان نیروی دریایی سپاه علیه متجاوزان آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/16027" target="_blank">📅 02:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16026">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صداوسیما:  شناورهایی قصد داشتند از مسیرهای غیرقانونی و ناایمن جنوب تنگه هرمز عبور کنند که نیروی دریایی سپاه پاسداران با آن‌ها برخورد کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/16026" target="_blank">📅 02:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16025">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال‌استریت ژورنال : یک پهپاد ایرانی به نفتکشی حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز اصابت کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/withyashar/16025" target="_blank">📅 02:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16024">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/16024" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16023">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">https://t.me/boost/withyashar
این بوستو بترکونین ایموجی اضافه کنم
😕</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/16023" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16022">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇭🇷
کرواسی 1
🇬🇭
غنا 0  پایان نیمه ی اول @withyashar</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/withyashar/16022" target="_blank">📅 02:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16021">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/16021" target="_blank">📅 02:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16020">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اهدافی که توسط آمریکایی‌ها مورد حمله قرار گرفته است.
دکل مخابراتی
پدافند هوایی
سایت های کروز
سایت های پهپادی
توانمندی مین ریزی دریایی
@withyashar</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/16020" target="_blank">📅 02:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16019">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/withyashar/16019" target="_blank">📅 02:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16018">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شب حمله
💥
@withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/16018" target="_blank">📅 01:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16017">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هم اکنون از مهرآباد جنگنده بلند شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/16017" target="_blank">📅 01:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16016">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
@withyashar</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/16016" target="_blank">📅 01:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16015">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">همزمان با حملات و تایید سنتکام بیتکوین دوباره اومد زیر ۶۰،۰۰۰$
@withyashar</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/16015" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16014">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری مهر: شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/16014" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16013">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">یه سر باید برم بیت رهبری
😂
الانه که موتور بزنم</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/16013" target="_blank">📅 01:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16012">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eC91IyXkzzyNU2eV6ZYw17hOkWlRZVE30nnCGIvf22Hyo__Dv0SuKjqMoLTV6QHaGKrFcCzftiP72R5i6qmOhWjpwMvQuTUgMEYsh7O14KdJZL0zQqBTAOZTpgGkZ6seJw94sJOFDY-mDqusO5co79jqYjmQw9GRrO3gtYAS_k4aC97fUb4oT8o58eEjcWaXnf39-qlJQn0S7vFyN05PYW5KtELU-7HwBQ7qvrAMfQIT0YUyTN-sStdnefhDfl5BzeQaaw3QJUVUv9Cv9WhPhlp2lDcupXMPf_oFXVoA82-OXWKP7GspxiSdNH7WbqBAm6grkPse0CDxG8xNoNkCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ، حضور نُه هواپیمای سوخت‌رسان آمریکایی در محدوده خلیج فارس و کمی دیگر ملحق شدن دهمی از اسرائیل به آنها
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/16012" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16011">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدای پهپاد و هلیکوپتر در قشم همراه با یک انفجار‌ جدید
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/16011" target="_blank">📅 01:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16010">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">فاکس نیوز : حمله فعلی آمریکا به ایران بزرگ‌تر از حمله دیشب است.
نیروهای آمریکا و بحرین ۹ پهپاد ایرانی را که به سمت نیروهای آمریکایی در بحرین پرتاب شده بودند، سرنگون کردند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/16010" target="_blank">📅 01:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16009">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/16009" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16008">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اتاق جنگ با یاشار : انفجار های جدید در‌ سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/16008" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16007">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : انفجار های جدید در‌ سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/16007" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16006">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNS4</strong></div>
<div class="tg-text">سیریک خیلی بد صدای انفجار میاد</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/16006" target="_blank">📅 01:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16005">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">هیچ شبی مثل امشب نزده.</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/16005" target="_blank">📅 01:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16003">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZtEI9B9gPpW-MgxjZnoDXmEtHu4pSeDnH6Z3POfalWAjEq1Giev9kFSKOPAXreRavKlUCT2neGph_OJqrl2a5X-EMHIWYth4Ocqk2pmASlXjtQfBuk5v3ztR-Rg4TUu0HXLjjjFgoPirZGQ43Tx5gkL4r9L6_hMRJgQEIILMH4gqjDoCtsHylsSXTSzT0Hl211kRSLUYMjxvWVLNXAmZMdr9dkqVyFTEEt9nEZhWPuozUGmXPj1Uh8Sgw4X4AI2oB9M85Uk5iNg8VPZyse-HMud0B5hFG9UqFxlPGPqs-JNePlOStmfPjEKPhb6MQOOBrhjuVdEQml327duJwldrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای آمریکا پس از حمله اخیر ایران به یک کشتی تجاری، حملات بیشتری انجام دادند
فرماندهی مرکزی ایالات متحده (سنتکام)
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۲۷ ژوئن به دستور فرمانده کل قوا، حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی «M/V Ever Lovely»، به ایران فرصت داده شد که به توافق آتش‌بس پایبند بماند، اما این کشور از این کار خودداری کرد و نیروهایش یک پهپاد تهاجمی یک‌طرفه را صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به کشتی «M/T Kiku» شلیک کردند. این نفتکش با پرچم پاناما در حال عبور در نزدیکی تنگه هرمز و حامل بیش از دو میلیون بشکه نفت خام بود.
در پاسخ مستقیم به ادامه اقدامات ایران علیه کشتیرانی تجاری، نیروهای سنتکام امروز حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های شناسایی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، مراکز نگهداری پهپاد و توانایی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز همچنان ادامه دارد. نیروهای آمریکا در حالت آماده‌باش، تهاجمی و کاملاً هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/withyashar/16003" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16002">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">سیریک رو چرا نمیگی بخدا نزدیک بود پنجره اتاق بریزه رو سرم</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/16002" target="_blank">📅 01:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16001">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار دوم در قشم اطراف فرودگاه
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/16001" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromₕₒₛₑᵢₙ</strong></div>
<div class="tg-text">خدایا یا من پولدار شم یا اتش بس نقض بشه امشب</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/16000" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صدای انفجار در قشم
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/15999" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/withyashar/15998" target="_blank">📅 01:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15997">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">صداوسیمای ایران به نقل از یک منبع آگاه نظامی این کشور گزارش داد صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/15997" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15996">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای هلیکوپتر در قشم ایران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/withyashar/15996" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15995">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دکل مخابراتی سیریک مورد اصابت قرار گرفت
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/withyashar/15995" target="_blank">📅 01:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15994">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آکسیوس : ارتش آمریکا تو منطقه تنگه هرمز حملاتی انجام می‌ده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/15994" target="_blank">📅 01:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15993">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش مردمی تایید نشده : چند تا انفجار بندر لنگه از سمت نیروی دریایی سپاه
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/15993" target="_blank">📅 01:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15992">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCaptain</strong></div>
<div class="tg-text">پولدارا کوشن یه گونی استارز ول کنن رو چنل
😅</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/15992" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15991">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار صداوسیما زنده از سیریک:
دقایقی پیش صدای چندتا انفجار مهیب از حوالی روستای طاهرویی سیریک شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/15991" target="_blank">📅 01:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15990">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گزارش مردمی : یکی طرف گز سیریک بود یکی دریابانی سیریک یکی هم طاهرویی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/15990" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15989">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گزارش مردمی‌تایید نشده : شهرک صنعتی سرخور طاعرویی رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/15989" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15988">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مثل همیشه دقیقا ۱۵ دقیقه جلو هستیم !
💥
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/15988" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15987">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صداوسیما: صدای انفجار در سیریک شنیده شد
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/15987" target="_blank">📅 00:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15986">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">صدای پهباد در قشم
@withyashar</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/15986" target="_blank">📅 00:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15985">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوستان از سیریک ، قشم و بندر لنگه گزارش ۳-۶ صدای‌انفجار‌شدید
میدند !!!!
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/15985" target="_blank">📅 00:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15984">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
۳ انفجار
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/15984" target="_blank">📅 00:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15983">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ امضای توافق با اسرائیل را به رئیس‌جمهور لبنان تبریک گفت
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/15983" target="_blank">📅 00:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15982">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فارس: کلیه خاموشی‌های شرق تهران برطرف شد
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/15982" target="_blank">📅 00:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15981">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نتانیاهو: توافق با لبنان ضربه ای به ایران و محور آن است
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/15981" target="_blank">📅 23:45 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15980">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بیانیه مجلس خبرگان رهبری:
بنابه‌نظر مجتبی خامنه‌ای، موضوع هسته‌ای نباید سرش مذاکره بشه.
باز شدن تنگه هرمز، خلاف تعهد مسئولان بوده.
«تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» از مطالبات رهبره و «هرگونه سهل انگاری در این زمینه» با واکنش مواجه میشه.
«بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/15980" target="_blank">📅 23:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15979">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فکر کنم تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15979" target="_blank">📅 23:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15978">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سردار حسن‌زاده:  در مصلای تهران بر پیکر رهبر شهید انقلاب نماز اقامه خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/15978" target="_blank">📅 23:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15977">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فکر کنم تنگه دعوا شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/15977" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15976">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9aaef7b78.mp4?token=BuRwH_ykn6dtNgJiV0ypbeBs_Y5CgPJtU3aGfqbebbflNfKdpJif-t7abeGzzijh0G9MlzGIQfBbgJ4RPsj8kXt9Ff9yjpGvycmfHjq1l0d2ueqljE5_DrZyK2TYcHB02CdgIhq7LfXLRZjfxFedz0xsMTT-jiXNCEauokft2oDWHKv1Jofc_67a_UCb7XZZcszvrOB6XJnOWBqZeWMeoME50tYrSs_tzGPtTuaki6Wgp-gEcs4Du1MWS6EsDz6RI5V_prE5ngHREIMzDdJuZWHFTeMnqy1tytrpALVboozqNnKpWY3UExu5omcndUhQWaYWfnP6hnC4oitjh1w-Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9aaef7b78.mp4?token=BuRwH_ykn6dtNgJiV0ypbeBs_Y5CgPJtU3aGfqbebbflNfKdpJif-t7abeGzzijh0G9MlzGIQfBbgJ4RPsj8kXt9Ff9yjpGvycmfHjq1l0d2ueqljE5_DrZyK2TYcHB02CdgIhq7LfXLRZjfxFedz0xsMTT-jiXNCEauokft2oDWHKv1Jofc_67a_UCb7XZZcszvrOB6XJnOWBqZeWMeoME50tYrSs_tzGPtTuaki6Wgp-gEcs4Du1MWS6EsDz6RI5V_prE5ngHREIMzDdJuZWHFTeMnqy1tytrpALVboozqNnKpWY3UExu5omcndUhQWaYWfnP6hnC4oitjh1w-Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف : اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه. @withyashar عرزشی
🤣</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/withyashar/15976" target="_blank">📅 23:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15975">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">قالیباف : اینایی که سوپرانقلابی و تندرون؛ هیچ غلطی برای این انقلاب نکردن. پس حق ندارن حرف بزنن و طلبکار باشن. دهنشونو باز نکنن و سرشون تو کار خودشون باشه.
@withyashar
عرزشی
🤣</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/15975" target="_blank">📅 22:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15974">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فارس : کیفر خواست رضا پهلوی و چندتا از عوامل منوتو و اینترنشنال صادر شده به جرم دست داشتن در اتفاقات دی ماه و باید برن دادگاه
@withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/15974" target="_blank">📅 22:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15973">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ونس: قیمت نفت الان به ۷۳ دلار در هر بشکه بازگشته، در حالی که تا ۱۲۶ دلار رسیده بود؛ این نشانه‌ای است که یک اتفاق واقعی دارد می‌افتد
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15973" target="_blank">📅 22:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15972">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ead84832.mp4?token=usAX4WP2eBv8hzRYYA-V7iVbjFck1LIpYR-e2TkDvYU31d3jfYekQdVtmR6L0MKiSgPzALvjsR5hQSnPwaGw9KNyNLvp08DdVmVf1EWM2rwFP0tg-9pdzflkQP7b0yoFZWlXYhj6ul8YXHYy3g12qCHKgk2cY8YbW21BX617PBXg6OpQsaXiN1U13FkFa51env3IJd5LeKlcuAVGOFfr_ya7KtXS2a0kdw6VZUBoNLu5Bm7vwk1sn0QglqTLwtXDS9lj2Z1OkIUFWiZgkpvlJfUxQa8XTtlS7G5bP7akiJeC8iI48d-V3sm5olVne1xJbyFv7zUICDXqGHLYpufy0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ead84832.mp4?token=usAX4WP2eBv8hzRYYA-V7iVbjFck1LIpYR-e2TkDvYU31d3jfYekQdVtmR6L0MKiSgPzALvjsR5hQSnPwaGw9KNyNLvp08DdVmVf1EWM2rwFP0tg-9pdzflkQP7b0yoFZWlXYhj6ul8YXHYy3g12qCHKgk2cY8YbW21BX617PBXg6OpQsaXiN1U13FkFa51env3IJd5LeKlcuAVGOFfr_ya7KtXS2a0kdw6VZUBoNLu5Bm7vwk1sn0QglqTLwtXDS9lj2Z1OkIUFWiZgkpvlJfUxQa8XTtlS7G5bP7akiJeC8iI48d-V3sm5olVne1xJbyFv7zUICDXqGHLYpufy0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر کانال صعودی بشکند، در پولبک، ما میتوانیم قهرمان شویم.
@withyashar
😂</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15972" target="_blank">📅 22:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15971">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab4f5549fd.mp4?token=e26op9L9a7SbXrKGj5MorHz0Fa3zb7SrMjaNffocOrW7FPeBJ77A6PbaTpH-bK2K9PdpLELalVxQzos8a_Hjjot-24cg71LQq5Ja6fW-S_HXhQRp4cmYeXmoOxIArSm-MAeu861yFwfR3CNhATw7j8gqoqSijwBiK2U3j6GbKg2t11yaCoEtxUsTJ_PwkHfCUO2O5xSIVMBVtZj0GXYJh1xdJxa-PjYnsNaIF3DIiCUBEk5pz_qwzs6JCr1yqL4zuFoIiYrRfMTg31eHRS6IcNDIXw8Y4QNNXsYeX0y27_aWqaWXUs4Ugl1kHuvdgHrmvf1c71iDBd6bufjLptYxcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab4f5549fd.mp4?token=e26op9L9a7SbXrKGj5MorHz0Fa3zb7SrMjaNffocOrW7FPeBJ77A6PbaTpH-bK2K9PdpLELalVxQzos8a_Hjjot-24cg71LQq5Ja6fW-S_HXhQRp4cmYeXmoOxIArSm-MAeu861yFwfR3CNhATw7j8gqoqSijwBiK2U3j6GbKg2t11yaCoEtxUsTJ_PwkHfCUO2O5xSIVMBVtZj0GXYJh1xdJxa-PjYnsNaIF3DIiCUBEk5pz_qwzs6JCr1yqL4zuFoIiYrRfMTg31eHRS6IcNDIXw8Y4QNNXsYeX0y27_aWqaWXUs4Ugl1kHuvdgHrmvf1c71iDBd6bufjLptYxcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا بیت‌کوین در آستانه تکرار ریزش ۲۰۲۲ است؟
تورم آمریکا دوباره در حال افزایش است و احتمال رشد نرخ بهره بیشتر شده؛ اتفاقی که در گذشته فشار سنگینی به بازار کریپتو وارد کرد.
برخی تحلیلگران هشدار می‌دهند اگر فدرال رزرو دوباره سیاست‌های انقباضی را تشدید کند، بیت‌کوین می‌تواند وارد فاز اصلاح عمیق‌تری شود.
هفته‌های آینده برای بازار بسیار مهم خواهد بود.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/15971" target="_blank">📅 22:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15970">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گزارش هایی از فعالیت پدافند بوشهر
@withyashar
🚨</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/15970" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15969">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نتانیاهو:ما محور دیپلماتیک جمهوری اسلامی را می‌شکنیم.
ما توانستیم به این چارچوب تفاهم‌ها برسیم به یک دلیل ساده: چون به حزب‌الله ضربه سختی زدیم.
و حزب‌الله که انتظار کمک از ایران داشت، آن را دریافت نکرد.
می‌خواهم به شما یادآوری کنم که در لبنان چه بود،حزب‌الله 150 هزار موشک و راکت داشت و ما حدود 90 درصد از این انبار عظیم را از بین بردیم
@withyashar</div>
<div class="tg-footer">👁️ 77K · <a href="https://t.me/withyashar/15969" target="_blank">📅 21:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15968">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">افشاگری کواکبیان، نماینده سابق مجلس:
مسئولی گفت کاری می‌کنیم اسرائیل دوباره حمله کند تا مردم بیایند پشت نظام
@withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/15968" target="_blank">📅 21:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15967">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نتانیاهو درباره لبنان:
اسرائیل همچنان در منطقه امنیتی زرد باقی می‌ماند که ما را در امان نگه می‌دارد. و این یک دستاورد بزرگ است. عظیم!
چون آنها چه کاری سعی کردند انجام دهند؟ آنها سعی کردند ما را از طریق انواع ابزارها، انواع فشارها از آنجا بیرون کنند. و البته، این اتفاق نیفتاد.
من از رئیس جمهور ترامپ و وزیر امور خارجه روبیو به خاطر مشارکت و سهمشان تشکر می‌کنم.
@withyashar</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/15967" target="_blank">📅 21:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15966">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">https://x.com/yasharrapfa?s=11
تویت جدیدم در اکس ، واقعا برام سوأل شده…</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/withyashar/15966" target="_blank">📅 21:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15965">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اسرائیل معتقد است که حزب‌الله ممکن است ظرف چند روز آینده در پاسخ به توافق چارچوب اسرائیل-لبنان، حملاتی علیه نیروهای دفاعی اسرائیل انجام دهد، طبق گزارش ینت.
اسرائیل برای احتمال تشدید در بخش شمالی آماده می‌شود و اضافه کرده است که انتظار نمی‌رود حزب‌الله «بی‌حرکت بنشیند.»
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/15965" target="_blank">📅 21:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15964">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سازمان پخش اسرائیل به نقل از منابع:
ارتش اسرائیل خود را برای عقب‌نشینی از دو منطقه آزمایشی در جنوب لبنان در فردا آماده می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/15964" target="_blank">📅 20:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15963">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">برق در بیشتر مناطق تهران رفته
@withyashar
🚨</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/15963" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15962">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منابع محلی گزارش دادند ارتش اسرائیل عملیات انفجار گسترده‌ای را در شمال شهر رفح در جنوب نوار غزه اجرا کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15962" target="_blank">📅 20:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15961">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMQFP2PRlwgnRH6hkjGuMLL-AJKYeKgjvTN0JpnF93BoDNfZ2R96GX1zRdV-LYsbmtmLpss-xZmE-kczHPSBFi5cJLyGocQVlPk5un_lr1r-MSkkllAZdRcfNhFjCTcdiG0hyPnMnbPoc8I9jcrgNKVgZc2mE7gVIFzn_CIBuhgK06fMxElmvB2jnUFMvTCWb6cqCeiIqKwr8j5nPg5JSy5y8_IMDBiXm6WubEL2IPqOAgndszGfsiVL7eVLgaEUhkOk4VpUuypofNBjNyYG-9VfwyLos6lsWKnHABm_FcVkcFSpaUzshdtenF_7BnPHSGhd_fZR_CHbeJozObC37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث :
گویا طلبکارم هست حتما یعنی بار کل دنیا رو دوش خودش و آمریکاست
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15961" target="_blank">📅 20:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15960">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a55c1168.mp4?token=ViKGrFR5NwA_p4lOZ2lgBgVLPDOT4HcJkoyrS6O5b2mzKdlepnb8g131eR9qVqh2Jtms0nCLhx3r17PaFYRZpMfm4XAEwK0frx2pm4oHjwEl_3GnX7kU6zJ3gzgTrQ55MaEcA89a3idZdz1Fm0SSNYNbtP-LeUs-p21io4PJ1ANg6w-BhIoBghdY3VSqVQfajHPh-zc3ZPhYSQ0gE5dHMkc2UTCRmKJEfsd6q-_bVAEvMpALu7KZLfcRqeRavjaa1CSY7etBSNSEJZbuQNEZk0tiWHKd_L4dFDms2b__aSS61kGutXycqAbslzikWjSut1REtvrUXklK92dIjVnk5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a55c1168.mp4?token=ViKGrFR5NwA_p4lOZ2lgBgVLPDOT4HcJkoyrS6O5b2mzKdlepnb8g131eR9qVqh2Jtms0nCLhx3r17PaFYRZpMfm4XAEwK0frx2pm4oHjwEl_3GnX7kU6zJ3gzgTrQ55MaEcA89a3idZdz1Fm0SSNYNbtP-LeUs-p21io4PJ1ANg6w-BhIoBghdY3VSqVQfajHPh-zc3ZPhYSQ0gE5dHMkc2UTCRmKJEfsd6q-_bVAEvMpALu7KZLfcRqeRavjaa1CSY7etBSNSEJZbuQNEZk0tiWHKd_L4dFDms2b__aSS61kGutXycqAbslzikWjSut1REtvrUXklK92dIjVnk5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصویر هوایی از تهران ساعتی‌ پیش
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/15960" target="_blank">📅 19:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15959">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مظفری مسئول مراسم خامنه‌ای: احتمالا تشییع جنازه هوایی انجام میشه
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15959" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15958">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از یک مقام آمریکایی: دو پهپاد ایرانی بحرین را هدف قرار دادند. یکی از آن‌ها رهگیری و منهدم شد و دیگری در منطقه‌ای دورافتاده در محدوده فرودگاه سقوط کرد. همچنین یک پهپاد دیگر یک نفتکش حامل دو میلیون بشکه نفت را در نزدیکی تنگه هرمز هدف قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/15958" target="_blank">📅 19:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15957">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c803f6a313.mp4?token=DvcBWOCKZrvQLHv6aynQbqLBC92xUyNytykCa2BobRaAOXcd7vWWC_8jkKXvXfvKDsK-XlgoaV1PWsIWiUJEshUsxF569HssZY-Q-xqQ-0mxiwrI4kOrmc1SvMUuASz4cAIWa3qR6xh_e6V-y0W4LZX6YlgRJaMRGeSMfhjLrgXcRdA7lsMHu7qMZu6jZVFD1m5EaJSOMDyImImwWAaVYlki-bV7NO0VuCI1FwCRFtzBS1J0v5jAKShWZgYcol50gOhuVhHsCiQLfuJZUu_ETLDsPLZfVeT78tD9r9Dtws6QyCp-gqQj-i9kmQyYubYDTURNjEhpjpLjMf1Unh-RKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c803f6a313.mp4?token=DvcBWOCKZrvQLHv6aynQbqLBC92xUyNytykCa2BobRaAOXcd7vWWC_8jkKXvXfvKDsK-XlgoaV1PWsIWiUJEshUsxF569HssZY-Q-xqQ-0mxiwrI4kOrmc1SvMUuASz4cAIWa3qR6xh_e6V-y0W4LZX6YlgRJaMRGeSMfhjLrgXcRdA7lsMHu7qMZu6jZVFD1m5EaJSOMDyImImwWAaVYlki-bV7NO0VuCI1FwCRFtzBS1J0v5jAKShWZgYcol50gOhuVhHsCiQLfuJZUu_ETLDsPLZfVeT78tD9r9Dtws6QyCp-gqQj-i9kmQyYubYDTURNjEhpjpLjMf1Unh-RKIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و صد افسوس…
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15957" target="_blank">📅 18:53 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15956">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دبیرکل حزب‌الله: سلاح مقاومت هرگز برچیده نخواهد شد ، توافق دولت لبنان با اسرائیل، مایهٔ ذلت، ننگ و واگذاری حاکمیت لبنان است
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/15956" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15955">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yqjd47OPeDDg0_Hj2pjKOmcJ320k7DsMD36TcQMsLE0Qlb0Je-jrgBmg7wKuPP2RWGxuPRqMUPiHMGBXIYEuTKNqSrhH7Xh48MuDDRRFT8Dl-zEQ-h95pV-XQZ6eMaXWgtzhQw-WU1Mbo1Azec0aTTbppB0u1Rdj8vRvpcK0cJQyNzw4Fe5ntamPYBNQTsQrhN_Y0VBHqDbNz-lbbf4YjbUHbWicTv0-rpRzVyExhHcGiycEzcm6NoPOK-cWjzK4jhdHLzFrREZemb8O5uhxbEF1Kb5yzKEoJsQhsIYcUnyNw-sQtNdgZGZbuYrqJ3DK-F6bBw7LBtJZ2X95FxiHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : شجاع خلیل زاده اولین بازیکن تاریخ جام جهانیه که بخاطر شادی گل نزده،کارت زرد گرفت @withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15955" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15954">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">علیرضا حقیر(دبیر) :عامل اصلی خوب نتیجه نگرفتن تیم ملی فوتبال ایرانی‌ها خارج از کشور بودن که باید ادب بشن.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15954" target="_blank">📅 17:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15953">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/15953" target="_blank">📅 17:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15952">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZ4ke-WJeosne3jMiXDN8gzLpfAXQQDpFnhKnovNC87NcIvyvYjSJyhfLicH1zEc5BUs1fmycmyTmdsz70fp8oR3yPKJ7NHiN3Uj765-rkHgXxvxVobt3e4mFihY_3rzIPNMcj91ujY56R0KlQfIZ5VEka6FsrtAmCAWFMLRizWi9mqCFmcMD9CWquUwbrGt99Y1JzsNLNX70V6vsY0AHKoV8CQ-pTWCFEDvUW8u143ngXnm5auBphCJilukKHv2p9L4FETM1VtzGp3Kx4eX9VLQZa2fbgLXJ-HAfKSlkKcXbk7N0-gm2010vwv9_-Qg2gmVBxhA2e4FOakBldsP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده @withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/15952" target="_blank">📅 17:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15951">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3JJ_vani0dXKQzGfoLfXvHL_9Uhe_GE0P0aY7W8YrMHRtxhsjeyrj0gWuRbZ0yLhbnVPQfwYuzD_FHtR_frEzOVc7xYCa5F7g1Ebgc-Km1ANae0qkml-nwqOUx4hHT2xQlDa5vHuAe_cOuiI-mhFS4CxIvZaqd1zyW59O87UaIjs_7vcJ1YI1C8tYHwHDLQ1P7aFeDQ6Aqhu88KcfirFy4FXrke7yce-BSoLyqiF_GQrSV6Kvd2rEK4cYI8Js2_kBAAjRLyxzAIcjVq1lpokrQ43yrrRUxaz5bP2mQ7XOF8jEiuWOzbJF9aXTuVfxaLcEkKWFITDFDKIIqtEgYt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت پر ریزون الان کرج !! ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15951" target="_blank">📅 17:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15950">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/withyashar/15950" target="_blank">📅 17:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15949">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سازمان دریایی بریتانیا: یک نفتکش در تنگه هرمز مورد حمله یک پرتابه ناشناس قرار گرفته است @withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15949" target="_blank">📅 17:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15948">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6530513224.mp4?token=BpuqwgfxmJoKyLfmxvQptbvHYACwNrB_IZ5-xEV_RJg0OJd2W5a58PeYEdm4XHzCdY0-a1wP_FPZo5jUtr5LYxKa1JuxKxPCx-bN892t6YUmzYn2LW5rBJpuQh8uFlfJdZ8chX-7Gpo1R_w5vR-gCxK9czhPhs-0oSZ0Sdpt_yC2Nc1mAR-knke3Xb1yWYDxWcdVgfbcn38Ul79PJJZM__mhZWIDJL2Y14xsMeY3lBfrmtqHhcQY7mHGITaU14WBFthZ_tx1IAtTQn9M-uMvY4NKDYQ9dfy112TDkeRqSt9rGkuCgnMxu21fHpGym3xWVTQ8nQjuq7HxXvAgAPZIQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6530513224.mp4?token=BpuqwgfxmJoKyLfmxvQptbvHYACwNrB_IZ5-xEV_RJg0OJd2W5a58PeYEdm4XHzCdY0-a1wP_FPZo5jUtr5LYxKa1JuxKxPCx-bN892t6YUmzYn2LW5rBJpuQh8uFlfJdZ8chX-7Gpo1R_w5vR-gCxK9czhPhs-0oSZ0Sdpt_yC2Nc1mAR-knke3Xb1yWYDxWcdVgfbcn38Ul79PJJZM__mhZWIDJL2Y14xsMeY3lBfrmtqHhcQY7mHGITaU14WBFthZ_tx1IAtTQn9M-uMvY4NKDYQ9dfy112TDkeRqSt9rGkuCgnMxu21fHpGym3xWVTQ8nQjuq7HxXvAgAPZIQjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت پر ریزون الان کرج !!
ایالات متحده با ایالات کرج دعواش شده
😂
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15948" target="_blank">📅 16:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15946">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKhTxseXvBQUQ0WSTJEX9QNikEUWq2a_rKinN3OT3Nqkrv7HlR2ISplk4q6imMw3a0s27WVV4FMGQgbSxWaV1C6Va1uBsBHaGJfB9vObKrkqB5MLlNyTufElE36j0fJ3v_uJgHHOAwQd4l1XDtI9QSNjBysSIzfmCX-tLKVLIqdYGMgno4KrhhRlYWGaoibEjuYVfTUrht1SShaVcgS8XugB_48MvzhypYTZQlg1Chfm-9sZsZ0goetWqz6N7hRJCzwcnRRLcUc8Gny6zZsrYcQaWb0P71KSQJomOzNmWr89hXCS2BH4p-vPM_ftMf26K3aVYEtd6NfQrsrmgLatBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=uDt78fAQ3K50VcsagcePMzhKazSrIx03lD-S-t5mDWBlj4YZOmdP_VxC1OuDVgaHclCkbFEQCcBqwpwiD97SrLj97JqKo9GFqKPglZCvfBSHm-VwAq0F22iVLnlT8qokFGxxjsipQdZeobvr-19qXNfVUjLf0gRfZvlpVQw51pRIJ9BH431NWPjRNMgYwjSGNAAJvFExq7V3v_mf51zQ33SHUMvq9Ye2hbRQT6ISdzyOm3KrrWpMLsSHzOKzGxIyFWoqkLl53hjIr9AT_Ll9cXVlE4XgS2vG7iPkD6cRKxgsaR0woyVxdMI2LlZz-12ttuZV_BvbSsfTsY4yaTCPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d33ddf14.mp4?token=uDt78fAQ3K50VcsagcePMzhKazSrIx03lD-S-t5mDWBlj4YZOmdP_VxC1OuDVgaHclCkbFEQCcBqwpwiD97SrLj97JqKo9GFqKPglZCvfBSHm-VwAq0F22iVLnlT8qokFGxxjsipQdZeobvr-19qXNfVUjLf0gRfZvlpVQw51pRIJ9BH431NWPjRNMgYwjSGNAAJvFExq7V3v_mf51zQ33SHUMvq9Ye2hbRQT6ISdzyOm3KrrWpMLsSHzOKzGxIyFWoqkLl53hjIr9AT_Ll9cXVlE4XgS2vG7iPkD6cRKxgsaR0woyVxdMI2LlZz-12ttuZV_BvbSsfTsY4yaTCPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل آفساید شجاع : سعید الهویی موقع خوشحالی با سر زده دماغ  هومن افاضلی رو ترکونده
@withyashar</div>
<div class="tg-footer">👁️ 84.7K · <a href="https://t.me/withyashar/15946" target="_blank">📅 16:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15945">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=jGgU18fT0jmWDB-h9dLARt5cNYYm3gA9G7Zovy4t31zkkr_OaF-olEc6rHbfKV_O2Tf4zNZ-qXDsTKe6NdU9IDUqaUVKoZ_C8nOlov8PO66VB5MILe1LlixzhMPBJ62jGCMOE-OYrKeCciudECdhcy_e8ctfZyVfb_sfgcBUgKkR9ufKdxrfgZjXJN0D6WjdwkUsVIDSXAExCVlJzFrKdmHKyAlJO1cL0x9vqA8Pp7jNqVguXQtklfiZ4mCupRyNZcQwAAuxFcu_x89H-ynUUUB0mTMKJzh6W8Nz6-t6rZTTCaPvIoPx-nns-CMOjfsJvK2B8UX5vPcpPMtqXXSD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b788f70cb.mp4?token=jGgU18fT0jmWDB-h9dLARt5cNYYm3gA9G7Zovy4t31zkkr_OaF-olEc6rHbfKV_O2Tf4zNZ-qXDsTKe6NdU9IDUqaUVKoZ_C8nOlov8PO66VB5MILe1LlixzhMPBJ62jGCMOE-OYrKeCciudECdhcy_e8ctfZyVfb_sfgcBUgKkR9ufKdxrfgZjXJN0D6WjdwkUsVIDSXAExCVlJzFrKdmHKyAlJO1cL0x9vqA8Pp7jNqVguXQtklfiZ4mCupRyNZcQwAAuxFcu_x89H-ynUUUB0mTMKJzh6W8Nz6-t6rZTTCaPvIoPx-nns-CMOjfsJvK2B8UX5vPcpPMtqXXSD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتیش بسیار بزرگ هم اکنون کرج
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15945" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15944">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv0SMW45sgDF4Bue4r-_AB8qb1R2pb7Rp9m6kFqwyNVAeOV6wIMuHMPD6n_-g4pFiSW4Ms4117nRfPjrQbku4SyGi2TkTUH3i5mncJ_D0AwpphP_UFhG_dTRF9XPOSkwArizHOwDzT41Aa_LMS_c4gmN46xmGfoTMrUhesDWy876FllBiAT7-gJmYmm0xirldaYVMi5cRZy1vkEXhHKBiTCdq6yUE6JGZw8RkAHe92XzA7_X15AUvazw2ARrQBDGIv02ZQ5Zt5EhxeGN-6bgrh9MZI0ZqUKxqxOamU3oO2-bATTg9m-m6KCZF4je8iUQYcuAaYDqkCLE6z8utU2DBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز
شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند
شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است
شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15944" target="_blank">📅 15:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15943">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محسن رضایی:پاسخ سریع و کوبنده‌ای در انتظار ناقضان تفاهم‌نامه است.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/15943" target="_blank">📅 14:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15942">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/15942" target="_blank">📅 14:36 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
