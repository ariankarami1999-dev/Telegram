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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 23:56:59</div>
<hr>

<div class="tg-post" id="msg-126627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزیر خارجه انگلیس: خواستار مذاکرات موفق ایران و آمریکا هستیم
🔴
می‌خواهیم شاهد پایان سریع و موفقیت‌آمیز مذاکرات بین ایران و آمریکا باشیم.
🔴
تجارت جهانی از طریق تنگه هرمز باید به سرعت از سر گرفته شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/alonews/126627" target="_blank">📅 23:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
جی‌دی ونس: به توافق با ایران نزدیک هستیم؛ شاید هفته آینده، شاید چند ماه دیگر...!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/126625" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ به واشنگتن پست گفت که محاصره باعث شده ایران «بسیار فقیر» شود و گفت آن را تا زمانی که لازم باشد در جای خود نگه خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/126624" target="_blank">📅 23:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
دونالد ترامپ در گفتگو با وال‌استریت ژورنال، درباره حادثه سقوط بالگرد آپاچی گفت که "مسئله خیلی مهمی نیست" و افزود که خلبان حالش خوب است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/126623" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
فوری /شلیک موشک از خاک یمن به سمت اسرائیل
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/alonews/126622" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
فوری/ خبرنگار: شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
🔴
ترامپ: من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/126621" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ درباره ایران به ABC: یک نفر باید همه آن زیرساخت‌ها را بسازد، پل‌های جدید، فلان چیز جدید، نیروگاه‌های جدید... آنها از یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر...
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/126620" target="_blank">📅 23:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: به زودی پایان جنگ و پیروزی آمریکا بر ایران را اعلام میکنم امسال جام جهانی خوبی خواهیم داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/126619" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری /شلیک موشک از خاک یمن به سمت اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/126618" target="_blank">📅 23:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
هشدار فرانسه در شورای حکام: جمهوری اسلامی ایران مقدار بسیار زیادی انباشت اورانیوم غنی شده در اختیار دارد و مشخص نیست چیکارش کرده و کجاست، همکاری فوری جمهوری اسلامی با آژانس بین‌المللی انرژی اتمی ضروری است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/126617" target="_blank">📅 23:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
روزنامه نیویورک پست گزارش داد که هزینه بالگردهای مدل AH-64 «آپاچی» بیش از ۳۵ میلیون دلار برای هر فروند است و ادعا کرد که این بالگردها در سراسر دریای عمان و تنگه برای اعمال محاصره به عملیات مشغول هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/126616" target="_blank">📅 23:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گزارش ها از شنیده شدن صدای 3 انفجار در نجف عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/126615" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
معاون وزیر خارجه ایران به الجزیره:
ایران پشت حمله به بالگرد آمریکایی آپاچی در بالای تنگه هرمز نیست.
🔴
این احتمال وجود دارد که چنین حوادثی به دلیل فضای پرتنش در تنگه هرمز به صورت غیرعمد رخ دهند.
🔴
هیچ هدفگیری عمدی از سوی ایران علیه بالگرد آمریکایی در بالای تنگه هرمز صورت نگرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/126614" target="_blank">📅 23:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ به ABC : حمله اخیر اسرائیل به ایران لازم نبود، ولی انگیزه‌های اسرائیل رو می‌فهمم
🔴
به نتانیاهو گفتم کاری نکنه که به مذاکرات با ایران ضربه بزنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/126613" target="_blank">📅 23:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibhzd0XYVyAJTIiasFr6F61PJI0h058IGAoTyWL8KfrB6zs4IUxsqnes1PWPdIoXoEAlPWn1P6fo_V7cWx1spDUKd7D1zZyyorObcYzC5OhrttFSQNN4MfdphNa7aDFcXP1MwlDZGAvIFla1oUEzGjle5m8YB0zkq6rFeeHeFGIn20hjFzzJAFqh8IUiDyZ9X6z4pmRH0mNqlOubsmoX6pYtm5-HOMBrKfPFoPO1T3UeyjK3-DuX7GBhpNgI2DcS4C7-BO1nA-XKtJx0fO6p9Yk5Y_gs6UjlUVCfCXFJ_c0THWf8fi152009GZpt-lGxDybIgRLVzuHN_ioQU6NIsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: تردد کشتی‌ها در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/126612" target="_blank">📅 23:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBvPrC2a6Ip0FDFZNyGmIMvnShQIin6N7FMMytxsge-K60rIxbVJSkwHLP_b-n0VecO6ibeoDGw3fCPH60kEZnSNENf28W3nqAJRJtwPhikG8FUXMTwHXL-uRqPZxWjm72FiDyfG7BAeEOfsbGtHXTIWDSqLhSZGlLJgyIimRii0t3DJHqZAbbthgDmvLhEg7HynTeZdiHG8QqGDZnZlHPdWRs7mnrjAOWG8UTSmITFPeljvYz8kOgbeIhnPfZUEHBmHIoUGNJ6cvoMvnxkmnkbe1aT4d1vTRN1rSiu6dMLjX1hyYRRBeEjCOKMjvemPbjh3z6ajmHzrNGJhBRNbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های کشتیرانی: صادرات سوخت جت عربستان سعودی به اروپا از سطح پیش از بسته شدن تنگه هرمز فراتر رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/126611" target="_blank">📅 23:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jhe3lKYlRAKXIcRIVM7MqwxDC9VwYNGTFI9F7-phpHwC3YJANJWpBwmLhBA2xqD37NcMnBJv1J733mMhu7P9_JTh-EjoS4I-VsIaCMHOqH62pCbkAB5ViRf3iEt-s6yChidyjfQIDfaAjZF4WcTZGJDIMTjYVAWBKyL7Q45jSkE6eaveAeWRTkAkIncta2gbt9D2BqLrw4djftG54f_RY5Wpkg863IoNROywVc6m7oq3QHosLOtNt29K51hdVw3sqlK4gAT9bbFpL6tN0PHSUanTP8i737MCjiTlhmWDMq1Z5xDZFtXJB49KTinJDH25SHUNUvNwZH5BbNt-ifFIow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی آمریکا هم‌اکنون هفت فروند هواپیمای سوخت‌رسان را در منطقه خاورمیانه به پرواز درآورده است.
🔴
از این تعداد، شش فروند در مجاورت خلیج فارس در حال انجام عملیات پروازی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/126610" target="_blank">📅 23:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
طبق گزارش ها تهران در حال حاضر شاهد اختلالات گسترده در GPS و خطای سیگنال‌های ناوبری (Spoofing) است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/126609" target="_blank">📅 23:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQcrp3-9nZEP7maaaGPEu6hJRhvF1Ohu6dOceSqHG5HPKe0qv72g2lyirvsZRGCCl1t36yrb-Xf6yiz1GCv0M9erVm84srmQzDQCtMJEyGUEF-mEihGRAsF45aAmiDEHC9ki7TwQNx17evC1r-FIwBxeIOPC_tWKc-hTint7Xb_WUxiRyMCDlZetHT4HocptHZKN3SAGNMXkQW_8kLXsob9Hd8USdellNaUP4TWHEA3YEQ6LhEqCM4RvfsuB-6kVXzgxTAUn5BOjjgSRBDz7O-RPC4lUnVDV-eqRCsJIIpqlUr-2eMBLPZ9Qfc4H0NnlqXjXBb0nv4c-0roYtBz05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ لیست ترور منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/126608" target="_blank">📅 23:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / شورای امنیت رأی‌گیری درباره قطعنامه ۱۷۳۷ را پیش برد و با ۱۱ رأی موافق، بررسی بازگشت تحریم‌ها علیه جمهوری اسلامی ایران را تصویب کرد
🔴
بریتانیا از فعال شدن تمام تحریم علیه  ایران استقبال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126607" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: احمد وحیدی فرمانده کل سپاه پاسداران گفته تا جمهوری اسلامی پول نقد دریافت نکنه هیچگونه توافقی امضا نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/126606" target="_blank">📅 23:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
فارس به نقل از منبعی مدعی شد: پیشنهاد جدیدی از سوی ایران برای آمریکا ارسال نشده است.
🔴
اسکای‌نیوز امروز در خبری اعلام کرد که تهران پیش‌نویس جدیدی برای طرح صلح به واشنگتن ارسال کرده و گزارش‌های اولیه نشان می‌دهد که طرف آمریکایی آن را «قابل قبول» می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/126605" target="_blank">📅 22:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c298926e7d.mp4?token=YW8zI8JYZ3VgVwMkMD3pmBlCEnPicUarHuMdkPhVPBcSZ-jn1EbHxfwAK-VIOowFuV6zgswykCNQx6Qz6WYB8MGPLh0PpdNIsAUUyinMlNCBfblGTMm34YfmQjdQlrZLW5-5wUxVPX4PH4dL_9edlzsEvcc1-AIVICUTYsqBr_PYSqLrCsg_q-BHvzA9JQTTDCt9HdF94tKcmZBH_6EeZ_FNT2j-NsrHacpirG3twWj4yN2lY_3sQdwuVWKSUgGsdTHGOL2aUPRmsu0T0AMcKKmBly9omXrJHK56habQogtTPYD10kVaZLoB05VRMcNiX9Yj7YuY2VjxgkRzTyInsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c298926e7d.mp4?token=YW8zI8JYZ3VgVwMkMD3pmBlCEnPicUarHuMdkPhVPBcSZ-jn1EbHxfwAK-VIOowFuV6zgswykCNQx6Qz6WYB8MGPLh0PpdNIsAUUyinMlNCBfblGTMm34YfmQjdQlrZLW5-5wUxVPX4PH4dL_9edlzsEvcc1-AIVICUTYsqBr_PYSqLrCsg_q-BHvzA9JQTTDCt9HdF94tKcmZBH_6EeZ_FNT2j-NsrHacpirG3twWj4yN2lY_3sQdwuVWKSUgGsdTHGOL2aUPRmsu0T0AMcKKmBly9omXrJHK56habQogtTPYD10kVaZLoB05VRMcNiX9Yj7YuY2VjxgkRzTyInsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار فاکس‌نیوز در کاخ سفید:
«رئیس جمهور ترامپ احتمالاً در شرف دستور دادن به یک انفجار بزرگ در ایران است... هیچ سرباز آمریکایی در اینجا کشته نشد، اما به نظر می‌رسد که ایران واقعاً، واقعاً سخت تلاش می‌کرد تا سربازان آمریکایی را بکشد، زیرا آنها یک هلیکوپتر آپاچی را سرنگون کردند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/126604" target="_blank">📅 22:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126603">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
حداقل 4 پهپاد کامیکازه شاهد-136 سپاه به یکی از مقرهای حزب دمکرات کردستان حمله کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126603" target="_blank">📅 22:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نبویان، نماینده مجلس: غنی‌سازی ۹۳ درصد می‌تواند به صورت صلح‌آمیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/126602" target="_blank">📅 22:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/ ایران در حال انجام حملاتی به مقر گروه‌های مخالف کرد ایرانی در اربیل عراق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/126601" target="_blank">📅 22:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70603bf6a8.mp4?token=FLRNy7o4dClwwejrc6rnRxbAaA97-QYGjhc98ueZelHNzIGwdqo3JD7zbybD3G82Sys7HcnmQQN-W-IlZKlbm55rIGOH17TJq-_pznUNp8uNWDrI9eyarnF2xPgSLvlyzi_gj5WcJyfMlRzwDEM_BluqeX9K954FXOe792DZZc-gmBaGCm01bWfJgkwF2oEYpwfB7V_RFxZt36Ol8MJQVmC1JViueXECKBeB7fjykAgLHIOekdPsy9vZAGVZ-8aTmAeo4Hwp9QHF4iJJ6qZgo2g2pG1x8qpQJ83ZcNvLNt3saX_6ulhTws2_9Gjzeww4CI-iTkSgPaOPSGb1ecjMng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70603bf6a8.mp4?token=FLRNy7o4dClwwejrc6rnRxbAaA97-QYGjhc98ueZelHNzIGwdqo3JD7zbybD3G82Sys7HcnmQQN-W-IlZKlbm55rIGOH17TJq-_pznUNp8uNWDrI9eyarnF2xPgSLvlyzi_gj5WcJyfMlRzwDEM_BluqeX9K954FXOe792DZZc-gmBaGCm01bWfJgkwF2oEYpwfB7V_RFxZt36Ol8MJQVmC1JViueXECKBeB7fjykAgLHIOekdPsy9vZAGVZ-8aTmAeo4Hwp9QHF4iJJ6qZgo2g2pG1x8qpQJ83ZcNvLNt3saX_6ulhTws2_9Gjzeww4CI-iTkSgPaOPSGb1ecjMng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فعالیت جنگنده ها در آسمان کردستان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126600" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126599">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
صابرین نیوز : باند اپستین در حال تدارک حمله گسترده به بهانه واهی است
این چندمین‌بار است که آمریکا در وسط مذاکره به ایران حمله می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/126599" target="_blank">📅 22:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126598">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
گزارش ها از پرواز جنگنده های آمریکایی / اسرائیلی برفراز سوریه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126598" target="_blank">📅 22:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126597">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">💢
فوووووووری/حمله شروع شد؟  هم اکنون هشدار در پایگاه‌های آمریکایی
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126597" target="_blank">📅 22:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126596">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pyt8dpnUU6FGVnzypTnxgRqjISttNpi8NQpIZB8pvngzNFHhW-R-seAOgDZgGMaduyMUyy96tHsYZwWoJDSGJl4c7vE5HYfrqEL4nyovHFO1lRhX57M-MYy4BGtVvDYEX4QOdC372buyvkjWYnDMntaEMiQnUNWubKmX_-vipPFsXsMhatHvA5ffq-j6p4jIJ1BQEMxgsuI6pzDy6GZ-a61PWKXupxEtq-_J5NdmTeqLxWUhN6vn3w2pEYG5DE8lfOtpyvBgVvUeSxMid-tkHGzuG0-9aYPRWwu4WY1lilNf3hWStmCbh72H5XEIsXEZcpVW1DNEbMC57oqBJMdL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت حداقل 9 سوخت رسان ایالات متحده در خاورمیانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/126596" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126595">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
فوری/فعالیت پرتعداد جنگنده های آمریکایی در آسمان عراق گزارش میشود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126595" target="_blank">📅 22:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126594">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
نیویورک تایمز : مشخص نیست که آیا مذاکرات با ایران پس از تعهد ترامپ به پاسخ به سرنگونی بالگرد، از سر گرفته خواهد شد یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/126594" target="_blank">📅 22:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
ترامپ: من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/126593" target="_blank">📅 22:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
یک مقام ایرانی به الجزیره: بالگرد (هلیکوپتر) آپاچیِ آمریکایی بر فراز آب‌های بین‌المللی پرواز نمی‌کرد.
🔴
ایران به هرگونه حملهٔ آمریکا که متوجه این کشور شود، با قدرت و به‌صورت فوری پاسخ خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/126592" target="_blank">📅 22:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ24OzF2bQa6eUXcDOBAw9PWls3JbG3Rg5Qa1MKO3FZ5hSvIUHwUpKofiXblt_xqCCxtRw6PisaT1WitVCXEs_G-M2d3pbCR2bR62gFWrWBDPg-TJCAQ3TNhiRduiww-wOOiveLzKENj1oSrIcRRU21FrWelhxMC4oGkBToMWKHruojHJsqunN0z9-I0CgdCQgK-9o_mVW8z76wOAV4tBulP8O8xH3fYK2QvoIk1OUk2SkfQmQKeGv4gkL3X8RhW8uZWjDi-m3L4zz4MYtiNPvGk45_PJH92XEX6d5WUd7t2fJnExPs6DQH1TZzq_6IDrJPosi9QeybQfRns2t5ezg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۳۵ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/126591" target="_blank">📅 22:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126590">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ : قضیه خیلی ساده‌ست هرکی قدرت بیشتری داشته باشه، برنده‌ست و ما هم همه قدرت رو داریم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/126590" target="_blank">📅 22:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126589">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عباس عراقچی، وزیر امور خارجه:
نیروهای خارجی در نزدیکی قلمرو ما به دلیل اشتباهات انسانی خود، حوادث ساده یا احتمال گرفتار شدن در آتش متقابل، همواره در معرض خطر هستند.
🔴
برای کاهش خطر، بهترین راه حل این است که آنها منطقه را ترک کنند.
🔴
ما زبان دیپلماسی را ترجیح می‌دهیم اما به زبان‌های دیگر نیز صحبت می‌کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/126589" target="_blank">📅 22:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126588">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
🔴
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم!
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/126588" target="_blank">📅 22:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126587">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / ترامپ به ABC : اگه یه عده بخوان احمقانه رفتار کنن
🔴
ممکنه کار به جایی بکشه که مجبور بشیم کل زیرساخت‌های یه کشور رو نابود کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126587" target="_blank">📅 21:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126586">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bO-zctFAwzvEZTSsGEiGdgqh3_1HXVRfTN1PwtMW_R5eH8FL5pQgu8aruPwDS8KFzZ0g8Pd_d4pdY4bJDWSlfaGmCOtXnn74thZCZ7SzwmaU7xoFOStElkGDnoyGhBS8i9yourbOu5ZvaOeC5QZ0F44s7ju7XMZiaZzHxy9RKQLLyYDbWg-kEy2hoPAWxoZZEo1_7BTY3p3LDk-FR_1aaS1ygNaf0zEWUkkAl23swuiUbvZI1K3Cv5MLwtTFn7A8yDEuwOmuuF5W_n2WtoVTVE_yM9qDLCisJBJeiw6ORAt8gd-y7D6cXxLhkycQ8wMu0zJW6MHS7pa-ODuNo1In-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون آسمان منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/126586" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126585">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/126585" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126584">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوری / سوخت‌رسان‌های نیروی هوایی آمریکا از مکان‌های مختلف برخاسته و در حال حرکت به سمت خلیج فارس هستند!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126584" target="_blank">📅 21:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126583">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
فوری / مقام آمریکایی به الحدث: گمانه‌ها حاکی از آن است که هدف قرار گرفتن بالگرد آمریکایی از سوی ایران عمدی بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/126583" target="_blank">📅 21:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126582">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سفارت هلند در تهران فعالیت خود را از سر گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/126582" target="_blank">📅 21:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126581">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
فوری / خبرنگار شبکه فاکس نیوز در واکنش به پست ترامپ درباره سرنگونی هلیکوپتر آمریکایی: به نظر می‌رسد این به معنای آن است که رئیس‌جمهور دستور یک اقدام بزرگ در ایران را می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126581" target="_blank">📅 21:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126580">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/126580" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126579">
<div class="tg-post-header">📌 پیام #53</div>
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
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/126579" target="_blank">📅 21:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126578">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فوری / رسانه‌های اسرائیلی: «اسرائیل» برآورد می‌کند که ایالات متحده ممکن است در ساعات آینده دست به اقدام نظامی بزند، اما به شکلی که به ازسرگیری جنگ منجر نشود و در عین حال تلاش کند تا حد امکان حادثه را مهار کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126578" target="_blank">📅 21:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126577">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قشقاوی، عضو کمیسیون امنیت ملی مجلس: تا در کل لبنان آتش‌بس برقرار نشود، امکان ندارد جنگ به پایان برسد
🔴
کسانی که ایران و لبنان را از هم جدا می‌کنند اطلاعات تاریخی ندارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126577" target="_blank">📅 21:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126576">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126576" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
فوری / سی ان‌ان یک پهپاد شاهد ایرانی یک هلیکوپتر آپاچی آمریکایی را سرنگون کرده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126575" target="_blank">📅 20:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
شرکت کشتیرانی سی‌ام‌ای سی‌جی‌ام (CMA CGM): هزینه دور زدن تنگه هرمز در سال ۲۰۲۶ به ۳۰۰ میلیون دلار رسیده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126574" target="_blank">📅 20:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126573">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/126573" target="_blank">📅 20:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ: من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126572" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: من همین الان توسط ارتش بزرگمان مطلع شدم که دیشب ایرانی‌ها یکی از هلیکوپترهای پیشرفته آپاچی ما را هنگام گشت‌زنی بر فراز تنگه هرمز سرنگون کردند.
🔴
دو خلبان درگیر بودند که هر دو سالم و بدون آسیب هستند.
🔴
با این حال، ایالات متحده باید به این حمله پاسخ…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/126571" target="_blank">📅 20:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126570">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrtfR6iSuXWlWpHSE2iHpd-1Wlfb8iPhsePkp-qJYaRaL_GFlE7iQLNJL7BQMVtvY3wv2rS73e1pFHqeR6rhjiHTOYUCIhxsOuKnBVFKh5gkAb5b2wOgcgFGLSA0pa-LFss5x_XJbUzKXvOiPzfevpYRa04WwudkTxZWB06AuU9QrW0V5Eynj_U_ujSvHXPhnrMp69iuyAH_4296lg6WyMKTdydM1yyVCS6VM7jE7TQVAqhOQVTxbbYG31xfz4qqaPi6w7ErVnkZ0FvTpcM7C9TBge4PqJbJSOt-Jt32dv0wTy1qEkdHAo-1RTzyNPEKvcuzdEYX_wjjfrZB1MLDAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز: ترامپ از اینکه نمی‌تونه مستقیم با آیت‌الله خامنه‌ای صحبت کنه خیلی ناراحته و حسابی ناامید شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/126570" target="_blank">📅 20:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126569">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta-8TbP0FN3sZVATszFG83ITNWgOSUYc967c276NkuaheYJlZB27Lm7yGLNhuT5f1-5_urdDIdMr9NO9ZfLuY6P0ss9cYem6kRm5BkvbfyxS6jTkoXRSJgl5D9Oyw7NiqWvWeuT7QzcuRX6276zwDcUi4YsVc3Xm6D0oJhMbasUdF9HWTkXvaexUlkkBfLRwjvxa0PIlS6A-7Lh_vZNBl-NfAb5nfrtv2ymc33YkauUYc6V2LjdLCYKm7nt88efsF2g3TPn02wFokv15McJvq807tRIXQh-wJZ4fh-UtmGF3jeysXTXD3hmYgCc3pvLh4XfF3RW3STjEwDVEDJSISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ادعای شبکه کان اسرائیل: امارات ۳ میلیارد دلار پول به ایران تحویل داد
🔴
به درخواست ایالات متحده، امارات متحده عربی یک هواپیما حامل ۳ میلیارد دلار پول نقد را به ایران تحویل داد؛ در ازای آن، ایران حملات خود علیه اسرائیل را متوقف کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126569" target="_blank">📅 20:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126568">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
قالیباف: ما زبان دیپلماسی را ترجیح می‌دهیم، ولی زبان‌ غیردیپلماسی را روان‌تر صحبت می‌کنیم / شما سوار همان اسبی می‌شوید که زین کرده‌اید
🔴
ما زبان دیپلماسی را ترجیح می‌دهیم، اما زبان‌های دیگر را بسیار روان‌تر صحبت می‌کنیم.
🔴
اگر تعهدات خود را بشکنید، ما به همان زبان که خودمان بهتر بلدیم، روی می‌آوریم. شما سوار همان اسبی می‌شوید که زین کرده‌اید!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126568" target="_blank">📅 20:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126567">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126567" target="_blank">📅 20:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126566">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ونس: فکر می‌کنم موفق خواهیم شد. اگر این دیپلماسی در نهایت از هم بپاشد، رئیس‌جمهور ابزارهای دیگری در اختیار دارد. اما تا زمانی که این قضیه را به مأموریت اصلی خود گره بزنیم - جلوگیری از داشتن سلاح هسته‌ای توسط ایران - به باتلاق تبدیل نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126566" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126564">
<div class="tg-post-header">📌 پیام #39</div>
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
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126564" target="_blank">📅 20:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: بازگشت جریان انرژی به حالت عادی ماه‌ها طول خواهد کشید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126563" target="_blank">📅 19:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126562">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126562" target="_blank">📅 19:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ونس: جنگ ایران یک سال دیگر به تاریخ خواهد پیوست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126561" target="_blank">📅 19:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گفتگوی وزرای امور خارجه مصر و عربستان درباره تلاش‌ها برای کاهش تنش در منطقه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126560" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
فعالیت‌های پروازی فرودگاه کرمانشاه از سر گرفته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126559" target="_blank">📅 19:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
العربیه : حزب‌الله اعلام کرد دولت لبنان باید «روابط خود با ایران را اصلاح کند».
🔴
حزب‌الله همچنین تأکید کرد اتهام‌زنی‌های دولت علیه ایران «برخلاف منافع لبنان» است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126558" target="_blank">📅 19:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
منابع خبری از حملات جدید اسرائیل به صور لبنان خبر دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126557" target="_blank">📅 19:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
به دلیل ریزش آوار در معدن گلتوت زرند، یک کارگر جان باخت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126556" target="_blank">📅 19:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
رادیو ارتش اسرائیل: ارتش از پایان وضعیت اضطراری در شهرهای اسرائیل در بخش شرقی مرز با لبنان خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126555" target="_blank">📅 19:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKYLVI_NRSTJZuMbB09VZzQ4mCe4p21FZX7kOL_WuyeHgReKKNLoTSAmURY-Asaqfp_2rXhtXew8T58tW38mvw0L0RozKIzXBy5ypNhBtHj5n9Rtvga7kDg2RjxgfbksSfbIBUyRCgQ4GSyz0A_AWD2zJmXhPWjD255Zd4P6cCfB3txoef5yOB_D2ss6T9g1q9CuXduza8mF0fZndTC1BWqCbT42ABUUZkGitmSLvLfWe_LZULBvtXXOA35C4YPlMvQO3Po7KcjsMqDXERzsaDuOFbyevFHfqXYoIFTqWicjCsRrqB18UN2JS2pYMOoVP2wLzjYi55mqnlNOSifSUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: در طول آتش‌بس دو ماهه جنگ ایران، تیراندازی‌ها واقعاً متوقف نشده است. با وجود این، یا شاید به همین دلیل، اقتصاد جهانی، نفت و بازارها به خوبی از این وضعیت عبور کرده‌اند - اما تحلیلگران هشدار می‌دهند که این وضعیت نمی‌تواند برای همیشه ادامه یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126554" target="_blank">📅 19:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126552">
<div class="tg-post-header">📌 پیام #28</div>
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
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126552" target="_blank">📅 19:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126551">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
زلنسکی: روسیه درک می‌کند که اگر ۶۰۰+ پهپاد و موشک وجود داشته باشد، آن‌ها این جنگ را دقیقاً همان‌طور که ما احساس می‌کنیم، احساس خواهند کرد، اما آن‌ها این را در خانه خود احساس خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126551" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126550">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126550" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126549">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: تردد کشتی‌ها از تنگه هرمز به‌طور چشمگیری افزایش یافته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126549" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126548">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNwIiueLekstbd2GJpLU4wtSTcW9c_ys_m1K0XlKuSPrl_EktBGlb-Q8syaehTnjfhu_WtFw-LvpXWD_qsqcKL3sObsWlwKnX0hFyUkfpWyvJ5lXj3TpxHZh2FtQW0c8BGAePbdhtSJ-C5Bgycde3St-yLy9sTgUicSnwlem7PnVKpxDNXAVBFTD3BCO0UgJts-D5K3bOpi1rKevuuQToQdbupRFWNxGP_Tqgud63JoPoLnL-psmVfh7CvuPrQImTNmH97yKndyRieyF404YvmL50vVkJ2z_5HNXBuLl4N4WZ9tSPIjFHR7Z3iLi2BnUctXOYgX-15sPV4gUblDZXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید حساب رسمی کاخ سفید در X
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126548" target="_blank">📅 18:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126547">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knitpwVh_eoRZyEoZ-qWCCdo1bC4pxbSpiRPxZKZBLngU6v13m4Ben2x2Y5wMGdFYzeO9m98AKoTUerJVB_mYE2xdJcEYWmrD2ZWmLrC2BxesAuauUcFH27tdaYgbgaS3F2O8isO8iBY90RYOF7As7FNmoen-8pU0kzg_XubKxWTx_BS1hAF6CG4NQtkO8ye_nGrF5uPjhGKSo-bJq_vHghdRFFYGdTx-rot4-bbBhbA0GUuFFsqzgLz5PoaQxXoHcmj4o4j8YSPm-EznbDNNf4y10ysWnnCzOFFHJrAMITZD8pBI0pU_H4rcdX7juBLrJUSCvN7_e8igbt68kLSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه رسمی فیفا : دیدار ایران و مصر قطعا دیدار افتخار همجنسگرایان خواهد بود و به هیچ عنوان این رویداد لغو نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/126547" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزیر دفاع بلغارستان: ما دیگر به اوکراین سلاح ارسال نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126546" target="_blank">📅 18:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNfFAYhfdlV1Tie3ZUbxLoL8-46_PpRF9Rdc98N2o1cY0uwKnaQ5P8vPwhOHRSTJ1q-zEqSN2zysURU9pPiyc_7sLve7ifugeJQFy-gIjfTXpmZoBjp7g10IGwdqhAmiAuOsCQh7cQvD1oquyacCr0842C61e8Zz6zEVtEBED83Mr8Gbsuv-jKyauHc5yh_ONuUNcRVwhmA2BLc1zv2gbDFCcFJjNZCxJ_Te-3fJzOgw2Q7m1o82pTNlVdHxkDbV0e9lU8Xff7BeXTvGx0GGsaY5f85NAN3XHbjsP9G6C0fNuJibfoPudtvaK-MOY5lR7yUWqjkjfsmDLFaQy7ctww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126545" target="_blank">📅 18:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
سخنگوی جنبش حماس:  گذار به مرحله دوم توافق آتش‌بس، منوط به توانایی میانجی‌ها، کشورهای ضامن و «شورای صلح» است که بتوانند اسرائیل را به توقف نقض توافق و پذیرش این توافقات ملزم کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/126544" target="_blank">📅 18:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
شبکه العربیه، به نقل از یک مقام کاخ سفید: مذاکرات درباره توافقی برای جلوگیری از دستیابی ایران به سلاح هسته‌ای نتایج مثبتی به همراه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126542" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126541">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWU7bd3Rh0EX79ciPbGbEbHQ3GY5laCRxIE-CMS80yuSVnt6rksMBj4pj1E8_-K0IT7srUQHf62qPSPd6nECMSokC_UdhxfWFfM4SFka0vGKgE3SQEToWfJFswWcgStJnlT2ZA4fsWAVNFxK5NzRoc9masoni7XZk2pC1rqjUDFJV5p0HRmn0SM-T1WazqYdwRdEmMX28uwHpBMRLh0XvB9mBlK68JseFcnjV7HyyzP-Y7tlG7398B658QQMhNWNny3p4zVy2pkP8WWYjm9NwscqpTfjzrMq7alDcwJivCRQb1lvw_oQb1UqINUyyVr3khZm39nIPLbQKwI_z3W35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داخل امارات یه منطقه ای هست که جزو عمانه و داخل اون منطقه یه منطقه دیگه هست که برای اماراته!
خاورمیانه همینقدر عجیب غریبه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126541" target="_blank">📅 18:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126540">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
منابع دولتی پاکستان به خبرگزاری آناتولی:
دستیابی به توافق برای پایان دادن به جنگ بین آمریکا و ایران در چند روز آینده به دلیل وضعیت پیچیده فعلی، که عمدتاً ناشی از نقض‌های بی‌وقفه آتش‌بس توسط اسرائیل در جنوب لبنان است، بعید به نظر می‌رسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/126540" target="_blank">📅 18:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126539">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126539" target="_blank">📅 18:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126535">
<div class="tg-post-header">📌 پیام #15</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126535" target="_blank">📅 18:01 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126534">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/126534" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126533">
<div class="tg-post-header">📌 پیام #13</div>
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
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126533" target="_blank">📅 17:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da6cf7b2a.mp4?token=VjdVIXM2HGRwtDCa-BVCkjpQ01TZQVAaMgMWIi6AFw3vSxRlOwNpN8UU9u4bL5MoHu1nrCOmAv9DraRhm6dzlsQd0XGnmXGB0tVtzo4gZrIbkrWXiy56mr8QToeehcB4XFUp-xW9fkzVoSwKDwCBFuhqcibc4tfZ_2852AsR8rlyVOTYq7uHeCfMgQPvjNUTOPEN4RyJD3kb6F6UxSSoHwfQQFHuiCptneldKd4gSHKlD2UouoGGUqtNQtv8riNo2-lqx-Ha0mEXeaqsRbKE_5qoAuF13DNsWKLID8dGg0mmmFbEgAAvDRmJ1ZGKTddj8qg2tPO-0CE2Oem5VS9DJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da6cf7b2a.mp4?token=VjdVIXM2HGRwtDCa-BVCkjpQ01TZQVAaMgMWIi6AFw3vSxRlOwNpN8UU9u4bL5MoHu1nrCOmAv9DraRhm6dzlsQd0XGnmXGB0tVtzo4gZrIbkrWXiy56mr8QToeehcB4XFUp-xW9fkzVoSwKDwCBFuhqcibc4tfZ_2852AsR8rlyVOTYq7uHeCfMgQPvjNUTOPEN4RyJD3kb6F6UxSSoHwfQQFHuiCptneldKd4gSHKlD2UouoGGUqtNQtv8riNo2-lqx-Ha0mEXeaqsRbKE_5qoAuF13DNsWKLID8dGg0mmmFbEgAAvDRmJ1ZGKTddj8qg2tPO-0CE2Oem5VS9DJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به صور لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/126532" target="_blank">📅 17:22 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
شبکه الحدث:
نبیه بری،رئیس پارلمان لبنان به سفیر آمریکا اطلاع داده است که جنبش امل و حزب‌الله آمادگی خود را برای برقراری آتش‌بس فراگیر اعلام کرده‌‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/126531" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126530">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی:
🔴
ما در حال بررسی این موضوع هستیم که آیا شلیک گلوله از سوی ایران باعث سقوط بالگرد آپاچی در نزدیکی تنگه هرمز در روز دوشنبه شده است یا خیر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126530" target="_blank">📅 17:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126529">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شلیک مستقیم نیروهای طالبان به معترضان در شهر هرات
🔴
طالبان میگوید که اینها مردم نیستند و نیروهای تروریستی هستند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126529" target="_blank">📅 17:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a789mwh72weXBEl8ZQHfGM1I16b5KFs5Bz-dzxAK_bjEt9Gn7kgETTcJlNkRCo4sRmq4VKVFeW-Vh0xGNTncC1s6sE0gIA5tQz_PdoIfOKaA8nkQLDhqv8Yc--l9zOtnXbJwEm0WaJz-qjxd9wFkOTX0t3eXVC18-sZIwt0SLfdBuwyBx1DLEQpC1bn2u9y6W0HIuQ8Us0P7v5kzxQe4pQGzq6QJs6JWoGCT1YJ9EZ3nO5zBTAIPwnw-E_PCeyEyq7A2Ej2etBlVbxxWlduWssKAvMiCvQ-fthtnuWfClFri7QNHodz0kI_yU9wSDcwasqh14_S73bsW6kQYRZCIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیا خانم ایران
۵ قلو زایید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126528" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126527" target="_blank">📅 16:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126526">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
تاثیر معدل پایهٔ یازدهم در کنکور امسال مثبت شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126526" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126525">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C6oNjj1nnppyGmWZhybHRw0z6iWIJO0yWKZB2_fhwSPvb5AMgALs8xA1sFekye_5UTDNYkZxm2IoRriae45v_Mw41w12tay8isfP1QgsZ7aBUrbvTfgFKzYEoocFRwNGFjsJd3ZQifywIgHrnEvyV5OJ3eZLtp3hIlB4267_Kve8b7_aHfUSrYB3AF7R4JTae887ImE9aReM7SKMAm6xjBVtPLDxZJa9irGN8VitbuygyxOel-odaPzKvkyuvOtTMX07mr4jYhWDkCY42CWKh3N2piwgdWip4z8VYgOpNDNvBq_cH1sh9TIdpDb-RySnFLH4LQWK3QXTCNTboVCehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خان میرزا بلاگر ایرانی در حمله اسرائیل به عراق کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126525" target="_blank">📅 16:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126524">
<div class="tg-post-header">📌 پیام #4</div>
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
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126524" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu-HBinKNcpae9RBU4rslVbFzvdxPAXwZR6QDcoa6ovpk0cdLObXpfhfXPCtQvRsWOnWp2elNaIwkpDCKA_OhPwLxSZQAL31oj0ep2VxuFqV9nmrBrK8xJvAcioZ1L18mIkNigfTUaZX2579iBFzwqw5fc6MAEkA9TJ6VenaovjCDCEGUC-IFH-0kncYokT5EMQ8fi-I56G_HplVfbFjmQZldrJWl4UHcxAmor34GyjIRHxyDGNK5x7FdIUMQ-uXH22QK6OUn9nVWXpMwP79JOycP2g1qTEpreXmr9svEgjSVJchqGQzeRZaENI6HLPRsI0v6BOYV3LTsvOTcupEEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / اسکای نیوز: ایران یه پیش‌نویس جدید برای آمریکا فرستاده و گزارش‌های اولیه نشون می‌ده طرف آمریکایی اون رو قابل قبول می‌دونه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126523" target="_blank">📅 16:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
حزب‌الله ادعا می‌کند که با حمله پهپادی به ساختمانی در تلات الصلعة در شهر قنطرة در جنوب لبنان، یک نیروی اسرائیلی را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126522" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیل به شهر عین بعال در منطقه صور در جنوب لبنان هدف قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/126521" target="_blank">📅 16:38 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
