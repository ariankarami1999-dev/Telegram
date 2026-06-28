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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 20:29:22</div>
<hr>

<div class="tg-post" id="msg-16089">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد. @withyashar</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/16089" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16088">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اکسیوس: اسرائیل و لبنان به این نتیجه رسیدن که برای جلوگیری از دخالت جمهوری اسلامی باید توافق کنن.
@withyashar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/16088" target="_blank">📅 19:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16087">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هم اکنون نیروهای زمینی سپاه مواضع گروه کرد در کردستان عراق را با توپخانه هدف قرار دادند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/withyashar/16087" target="_blank">📅 19:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16086">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">وال استریت ژورنال: مذاکراتی که قرار بود این هفته بین واشنگتن و تهران در سوئیس برگزار شود، پس از تبادل حملات دیشب متوقف شد.
@withyashar</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/withyashar/16086" target="_blank">📅 19:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16085">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/16085" target="_blank">📅 19:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16084">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دلار و تتر ۱۷۲،۵۰۰
🚨
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/16084" target="_blank">📅 19:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16083">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">طالبان افزایش قیمت اینترنت را ممنوع کرد
@withyashar</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/withyashar/16083" target="_blank">📅 19:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16082">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
این بوستو بترکونین ایموجی اضافه کنم
😕</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/withyashar/16082" target="_blank">📅 18:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16081">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مجتبی خامنه‌ای بیانیه‌ای منتشر کرد که در آن خواستار اصلاحات گسترده قضایی، اقدام سختگیرانه‌تر علیه فساد و ادامه پیگیری پرونده‌های حقوقی درباره جنایات جنگی آمریکا و اسرائیل شده است.
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/16081" target="_blank">📅 18:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16080">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba88b4582.mp4?token=YF0sBFA2BsZfRNYJUApRIp2lQI3nGn5LgLxBJdVP1hB3Hx0bMysUrLpWkDZ4kQrG3kLIhFFB4Yz4V15DevrJAmakJuQ-0hEe6N6a1FIaXsbXh7HaczHvmz92Z4Ar2BbtyKMw_vRTzqnKlJRkurnbZOmLyFTWBE1rVtV-5EmcgBUp-rsFzCNXiVIZXu_M3G5E7tltkrwGV3-rlCVfCHETV7BrpDlOCFIyx4FkfmlC2VV2r0mxWqkgdn5eUQxckH8Qf-LtNZF3mTRjuLlIxIO9VmG2dtnp5CtScPc2ZZl3CwZGCUVqpNP6P3grcsagdKkzwKYFlJBrfKMTMtlPC9uYLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba88b4582.mp4?token=YF0sBFA2BsZfRNYJUApRIp2lQI3nGn5LgLxBJdVP1hB3Hx0bMysUrLpWkDZ4kQrG3kLIhFFB4Yz4V15DevrJAmakJuQ-0hEe6N6a1FIaXsbXh7HaczHvmz92Z4Ar2BbtyKMw_vRTzqnKlJRkurnbZOmLyFTWBE1rVtV-5EmcgBUp-rsFzCNXiVIZXu_M3G5E7tltkrwGV3-rlCVfCHETV7BrpDlOCFIyx4FkfmlC2VV2r0mxWqkgdn5eUQxckH8Qf-LtNZF3mTRjuLlIxIO9VmG2dtnp5CtScPc2ZZl3CwZGCUVqpNP6P3grcsagdKkzwKYFlJBrfKMTMtlPC9uYLYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صداوسیما: تا پیروزی کامل بر دشمن باید جنگ کنیم؛
جمشیدی، کارشناس صداوسیما: جنگ نیمه کاره به صلاح نیست؛ باید به نقطه بازدارندگی مطلق؛ سلطه و تفوق برسیم؛
@withyashar</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/withyashar/16080" target="_blank">📅 18:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16079">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">خبرگزاری رسمی عراق: کارزار نخست‌وزیر برای تعقیب و بازداشت متهمان به فساد ادامه دارد، تا کنون 47 نفر از نمایندگان و مقام‌های دولتی به اتهام فساد بازداشت شده‌اند. @withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/16079" target="_blank">📅 18:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16078">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بنابر اعلام منابع میدانی،در محور پیرانشهر به مهاباد درگیری بین رژیم و گروه کرد ها رخ داده
درگیری در اطراف روستای گاگش در محدوده مهاباد رخ داده و طبق اطلاعات منابع میدانی عامل این حمله گروهک کرد پژاک عنوان شده
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/16078" target="_blank">📅 18:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16077">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/16077" target="_blank">📅 18:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16076">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سخنگوی ارتش ایران : ما برنامه‌های جدی در دو حوزه داریم: تولید داخلی و تأمین تجهیزات پیشرفته از کشورهای دوست.ما قطعاً در روزهای آینده به سیستم‌های پیشرفته‌تری مجهز خواهیم شد.
@withyashar</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/withyashar/16076" target="_blank">📅 18:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16075">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ادعای کانال ۱۴ اسرائیل: در توافقنامه هیچ جدول زمانی برای خروج وجود ندارد و هیچ چیزی اسرائیل را به آن ملزم نمی‌کند.
در واقع این یک توافقنامه بسیار خوب است، اما حزب‌الله از این بابت عصبانی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/16075" target="_blank">📅 17:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16074">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فارس: جمهوری اسلامی در دوران گذار به نظم جدید جهانی، چاره‌ای جز ساخت بمب اتم نداره تا گزینه نظامی علیه کشور از روی میز برداشته بشه.
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/16074" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فارس: ۶۲ نماینده مجلس که که پیش‌تر اعلام کرده بودند روز یکشنبه مقابل مجلس حضور خواهند یافت، برنامه را لغو کردند
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/16073" target="_blank">📅 17:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16072">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حقیقت : نیروهای امنیتی عراق یک عملیات بزرگ ضد فساد اجرا کردند این عملیات در منطقه امنیتی «سبز بغداد» انجام شد چندین مقام سیاسی، نماینده پارلمان و مسئول دولتی بازداشت شدند برخی گزارش‌ها می‌گویند تعداد بازداشت‌ها بین ۷ تا بیش از ۱۰ نفر بوده و در برخی منابع غیررسمی…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/16072" target="_blank">📅 17:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16071">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گاردین و افشای سندی محرمانه؛ خیز «هیات صلح» ترامپ برای کسب مصونیت مطلق قضایی در غزه
پیش‌نویس قطعنامه‌ای که به دست روزنامه «گاردین» رسیده نشان می‌دهد «هیات صلح» مورد حمایت سازمان ملل که دونالد ترامپ اوایل سال جاری میلادی برای اداره غزه تشکیل داد در پی اعطای مصونیت حقوقیِ گسترده‌ به خود است.
به گزارش گاردین، متن به‌کاررفته در پیش‌نویس همچنین به این نهاد اجازه می‌دهد تا اموال عمومی در غزه را «به‌طور رایگان» در اختیار بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/16071" target="_blank">📅 16:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16070">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/16070" target="_blank">📅 16:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16069">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حقیقت : نیروهای امنیتی عراق یک
عملیات بزرگ ضد فساد
اجرا کردند
این عملیات در
منطقه امنیتی «سبز بغداد»
انجام شد
چندین مقام سیاسی، نماینده پارلمان و مسئول دولتی بازداشت شدند
برخی گزارش‌ها می‌گویند تعداد بازداشت‌ها بین ۷ تا بیش از ۱۰ نفر بوده و در برخی منابع غیررسمی عددهای بالاتر هم گفته شده
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/16069" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16068">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">رئیس جمهور و نخست وزیر عراق دیشب کودتا کردن هم یک خبر فیک نیوزه !!!</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/16068" target="_blank">📅 16:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16067">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پست ترامپ مبنی بر‌ اینکه مسی بهترین بازیکنه فیک نیوز هست !</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/16067" target="_blank">📅 16:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16066">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">زلزله مازندران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/16066" target="_blank">📅 16:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زلزله مازندران
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/16065" target="_blank">📅 16:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فایننشال تایمز به نقل از یک دیپلمات گزارش داد که میانجی‌ها در حال انجام گفت‌وگو با طرف‌های درگیر [ایران و آمریکا] هستند تا تلاش کنند تنش‌ها را کاهش دهند.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/16064" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">هاآرتص: سامانه‌های دفاعی اسرائیلی به قطر و عربستان سعودی فروخته شده‌اند؛ با وجود اینکه هیچ‌یک از این دو کشور روابط دیپلماتیک رسمی با اسرائیل ندارند
@withyashar</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/withyashar/16063" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اولین پارکینگ ‌پناهگاه تهران به پایان رسید
شهردار منطقه ۱۰: ساخت اولین پارکینگ پناهگاه تهران در یکی از مناطق پرجمعیت و پرتراکم تهران به اتمام رسید و بزودی بهره‌برداری از آن آغاز می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/16062" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراقچی رفته عراق ستاد مشترک تشکیل داده برای تشییع جنازه !   عراقچی : جنازه علی خامنه‌ای در بغداد، کاظمین، کربلا و نجف تشییع میشه @withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16061" target="_blank">📅 13:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16060">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">عراقچی رفته عراق ستاد مشترک تشکیل داده برای تشییع جنازه !
عراقچی
: جنازه علی خامنه‌ای در بغداد، کاظمین، کربلا و نجف تشییع میشه
@withyashar</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/withyashar/16060" target="_blank">📅 13:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHO0LFxy340aK63cYgKBJ3LgZLPM2qXh4OkfO76lh2YNRVixlgsSmk9R4t7VQIiBieDPQdq_6mrjXrgddjk3fznWtE9AlSY0je6_GbnOuKcHBTFmsudfGbbove30i26Q0qxvWAtDC7Rt22Fy-f03TqqTMcBmWU51D9cQjxb8QzmaQiMIS7wsQUcexVPS4VKdUWFDzqTEpjsFOMpl1Y1urnaPSqTrYEJHqalXOBJh0rI0xs6mHnfTGLrWAR1Dd-jW4C63p37Rlu5ME7iIDBVeqkhAbG3DYYxjIscGUwgnWa-rujiMO8MHCPducgSO2bl-Vbh3ZF28_ACF-uELTcP4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری خواهر جاویدنام
صهبا رشتیان
،
داور بین‌المللی
که در اعتراضات دی ماه، جونشو اهدا کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/16059" target="_blank">📅 12:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16058">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6v-OE1iIeID520_bN63gGdDwcNUP4wmmN5JpvpWEcnJZjW4N1zo8YQaCIsKCWkn7YfjoSChFFx_mDrLk0c9N59cMyIlG8o7BhjPVFm_1Ecze1zHlId0MzY8Hsvy3sQGkUMYBX_i8jzz89a8YxE_-IgSDKhyHFDSphzAwr7fd1r-_Wht19Im-MgWx0FxGYIXXtMBssjxbnDufQD7CfKqnHjF7KxePHd5WmmWMCPcR4xQ9ZlYrQNAVjAISeoO0muo1R1k8JmvmKwMpMWyzRM942Ob3Ff0tz48cgTMa8glTEMyUweUGJwWPDyeZ79GMdqEilsQbxlKj4MwHHIcUvpjvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر های دریایی عبور از تنگه هرمز  شماره ۱ : که ورودی از بالای جزیره لارک و خروجی از پایین آن عبور میکند  شماره ۲ : هم اکنون مین ریزی شده و به شدت خطرناک است شمار ۳: مسیر ایجاد شده توسط آمریکا که سپاه حملات اخیر را در این مسیر انجام داده @withyashar</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16058" target="_blank">📅 12:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در ساعت ۲۰:۳۰ هفتم تیر ۱۳۶۰ ( دقیق ۴۵ سال پیش و همین روز یکشنبه ) جلسه‌ای در سالن اجتماعات دفتر مرکزی حزب جمهوری اسلامی واقع در محله سرچشمه تهران و در جلسه‌ای که برای بررسی انتخابات ریاست جمهوری آینده برگزار می‌شد، بمبگزاری با ۲ بمب رخ داد که منجر به کشته‌شدن ۷٣ نفر از وزرای دولت، نمایندگان مجلس شورای اسلامی و اعضای حزب جمهوری اسلامی شد. سید محمد بهشتی رئیس قوه قضائیه و دبیرکل حزب جمهوری اسلامی از جمله کشته‌شدگان بود.
میدان هفتم تیر در تهران، به عنوان یادبود این حادثه نام‌گذاری شده است.
توسط سازمان مجاهدین خلق ایران و عامل انفجار ، محمدرضا کلاهی بود
@withyashar</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/withyashar/16057" target="_blank">📅 11:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/16056" target="_blank">📅 11:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Imous7D05ete_QAUrhKN1kfH-uzlnyfvuTVURzL5w1PgWdsLTg6PA0CnkWhiXdQYhWA5z99ebFQnFfEeweK9pDCE6MygdxUFE4C0dIG7nmFCN1M8UixQtIdF7Ef5dUePwMwY1oWErYmm9KHN7T1qU4eK7QL-qkrGBW0k6dpeFQnOLCIeRZROKaBjhtohZUJkNNdaLf0gEut6xHrgjnPapFwLplVBXn-asvRqK1Iery9JDsmzXe1pGotcV__nSHXGQe4ZtHxEtvYoFKxyGhRnPYBTyLhiEQ9uIy07wscvSETEtx5RE2P6mMwxmRWJeUqdoVVQiHjkg5H4OEoaA_93fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر اینگونه عجیب رقم خورد تا چهره میثاقی بشه تراپی
- ساعت 00:30 اومد گفت اقا غنا کرواسی رو ببره رفتیم مرحله بعد؛ نتیجه؟ غنا بازیو باخت
- ساعت 03:30 اومد گفت اقا این دفعه ازبکستان نبازه ما صعود کردیم؛ نتیجه؟ ازبکستان بازیو باخت
- ساعت 05:30 اومد گفت اقا این بازی برنده داشته باشه ما تو جام می مونیم؛ نتیجه؟ بازی مساوی شد
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/16055" target="_blank">📅 11:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">1$ Tether = 171,000 Toman
@withyashar
🚨</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/16054" target="_blank">📅 10:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16053">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه هنوز برات عجیبه پس این کد رو ببین ، تیم جمهوری اسلامی   ۳مسابقه + ۳تساوی + ۳امتیاز + ۳گل زده + ۳گل خورده  + ۳گل مردود = ۱۸ , که میشه روز ا‌ول کشتار جاوید نام ها  درجواب رامین و قلعه نویی و اون کفتار شغال شلیل زاده  که قرار بود به جنازه…</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/16053" target="_blank">📅 10:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVDOoh3xLBfWmDgdPfZ9WatuDPK-O2Xz9Rn05biitXMU3CS6SXWaE4uUsdu0y7Ap4blGO6nYjNADRsmjBr_dkQddb19DWp442WvOfP1tC3Ca5O1AK-CqeWsrK7aEHgw1GApVTNPnxisXMNKZz6zE6JuesNQFhh0h8Omwx8ItXaBMWaIMZ0qv9H27Y9GfKFyJYkpixQeXquSMnW0t163Loo4uWcpFLgPPrjU3HcwbysheYAfuNjZjIHaTO2gzAHUhIyrRgilyIUAn8Cqu6CUwEf_kFk3S9tOi3l0-_5zeUSKlUQVpzUtnwrGEY0fiL6e3bXJ-Wbljr2ytM7zJ3COKZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی ارتش اسرائیل به الخیام در  جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/16052" target="_blank">📅 10:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه هنوز برات عجیبه پس این کد رو ببین ، تیم جمهوری اسلامی
۳مسابقه
+
۳تساوی
+
۳امتیاز
+
۳گل زده
+
۳گل خورده
+
۳گل مردود
= ۱۸ , که میشه روز ا‌ول کشتار جاوید نام ها
درجواب رامین و قلعه نویی و اون کفتار شغال شلیل زاده  که قرار بود به جنازه رهبرش تقدیم کنه
@withyashar
اگه شما نمیدونید ما میدونیم واسه چیه ویا اینکه چرا خدا باهاتون سازگار نیست
پاینده ایران</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16051" target="_blank">📅 10:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYQiQ23M2MbwbmQDkMTNkOqQvTLITpaqBdWp5JVnUvkJgU1W89Cd7P3Ik6GvatF0CzPN4ypcMPvnmII0W1sK2Lk_4w-RG7bEyBZWnjhziXQB2lQZdOg_Q3a8AYegYasZDCeH1-MtaAFKcmdGZydwO-yV9E3Gpglu6ms8m6eBVw1IXsSUIrWGdhcrnxucNAaxiTYHXuHU_Sb23oc-idqX2_Y7ye7wpkMAFWX9yzkD6ZiQ4tZVQiHU52o6z2Cx5mkq-FtOybgE0Ma1MBKHyl-SISeve0fd0hGnWYM5nsRtDZ04sWq2ESqcGcgZp_wnFKAfJU7e0Evlmjw4bAXeDTFu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت کشور بحرین: در پی حمله ایران، یک ساختمان مسکونی در منطقه المحرق آسیب دید، اما هیچ خسارت انسانی در پی نداشت.
@withyashar</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/withyashar/16050" target="_blank">📅 10:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتاق جنگ با یاشار : صعود تیم جمهوری اسلامی رو به فرودگاه إمام لعنت الله تبریک عرض میکنم
😂
😂
😂
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/16049" target="_blank">📅 10:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اتریش و الجزیره هم ۳ بر ۳ شدن تیم ملا حذف شد
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/16048" target="_blank">📅 09:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5328c12b8e.mp4?token=nz3gSaaPL-xopzyvM39psZ7VUX8OOkRQVURl8MpuOGDq9Exf61OIHH_UIGMhTR6pXHNp5TXJ4WZuoYY-wY0zxpSbdYrZD8uN1WLcevP-UA0vI7E2c_jHLzOtyCsezjJHjdrLd4pcOiUEFm9pTsGIhnMn-uZtTW7PBUngVx381bosfSvxWOkwo48UBWlOr4FRECfqy7_pV0S3-rBsjcbH5NBIEJhWX_MZ5qvum9xW18-AGDmxXtztGOrACDtSvNHwe8t20dW7horMrldKOflZGV7p6Nz4uE3itN9HRscYshEc0L0fHOk8MvaadwdCZy1N_Vq8-qUxhRre6HCHx9Oxzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5328c12b8e.mp4?token=nz3gSaaPL-xopzyvM39psZ7VUX8OOkRQVURl8MpuOGDq9Exf61OIHH_UIGMhTR6pXHNp5TXJ4WZuoYY-wY0zxpSbdYrZD8uN1WLcevP-UA0vI7E2c_jHLzOtyCsezjJHjdrLd4pcOiUEFm9pTsGIhnMn-uZtTW7PBUngVx381bosfSvxWOkwo48UBWlOr4FRECfqy7_pV0S3-rBsjcbH5NBIEJhWX_MZ5qvum9xW18-AGDmxXtztGOrACDtSvNHwe8t20dW7horMrldKOflZGV7p6Nz4uE3itN9HRscYshEc0L0fHOk8MvaadwdCZy1N_Vq8-qUxhRre6HCHx9Oxzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از حملات هوایی ساعات آغازین امروز آمریکا به زیرساختهای رژیم
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/16047" target="_blank">📅 09:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16046">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ارتش اسرائیل: عبدالرحمن ماهر زیاده، فرمانده هسته النخبه در حماس، را کشتیم.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/16046" target="_blank">📅 09:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16045">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرنگار العربیه: عباس عراقیچی، وزیر خارجه ایران وارد بغداد شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/16045" target="_blank">📅 09:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16044">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گل دوم کنگو توسط مایله در دقیقه 78
🇺🇿
ازبکستان 1
🇨🇩
کنگو 2  با این نتیجه دومین شانس تیک ملا هم از بین میرود  و فقط یک جون دارد @withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16044" target="_blank">📅 04:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16043">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صدا های انفجار مانند از بوشهر ، یا داره میزنه یا میخوره ، یه خبری هست
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16043" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16042">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">حمله‌های متعدد ازبکستان روی دروازه کنگو  ازبکستان
1️⃣
-
0️⃣
کنگو  با این نتیجه تیم ملی صعود میکند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/16042" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16041">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dub9Jiia37p_tGRH_k2cxgDrUBxy1rc26dt9bVLUgpgS3eDN9FD70_u8doMM33mSYH5uq5WqK7kERUxNlNHZ17PzSYIzrOLmZYYzAk04lkF0n-bsPMlN-7H3ccD68rDg6Re2OA9E1ZZLXzy3JMpTRypcoFhL8TKRyVsRB2BLstZ7d-FjSUkgGejNZewDRylmWCjrX84B-OnjVzUnt9Ip6dJ8_zpMNLnrXtJsYdwyNaF3LulN-2faD8yxS8nKUo2wGaykXre9DapDjhRIuNJtfcmlz5P0glaWzz6vUT_KR9ElI_ldIlNmVPO7i63_h-2KDpWcUsPmkSkc9hJzGJ5W2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک شیء ناشناس در آسمان بحرین در حال پرواز است.
@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/16041" target="_blank">📅 04:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16040">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی در بیانیه‌ای اعلام کرد نیروهای دریایی و هوافضای این نهاد، در پاسخ به آنچه «تجاوزهای اخیر آمریکا» عنوان شده، عملیاتی مشترک با استفاده از موشک‌های بالستیک و پهپاد علیه چند هدف نظامی انجام داده‌اند.
در این بیانیه ادعا شده است که در ساعات اولیه بامداد یکشنبه، چند زیرساخت مرتبط با نیروهای آمریکایی در منطقه از جمله در کویت و بحرین هدف قرار گرفته و «منهدم» شده‌اند. همچنین به حملاتی از سوی آمریکا به برخی نقاط ساحلی ایران اشاره و تأکید شده است که در آینده برخورد با کشتی‌های متخلف در تنگه هرمز با شدت بیشتری انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/16040" target="_blank">📅 04:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16038">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">موشک‌ها در آسمان بحرین در حال پرواز هستند و پدافند هوایی نیز درگیر شده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/16038" target="_blank">📅 03:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16037">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اطراف بندرعباس شهر تازیانپ روستای خونسرخ صدای چندین انفجار ، قشنگ لرزید
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/16037" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16036">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حمله‌ای جدید این بار با موشک در بحرین.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.2K · <a href="https://t.me/withyashar/16036" target="_blank">📅 03:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16035">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/16035" target="_blank">📅 03:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16034">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پدافند کویت فعال شده
چندین انفجار شنیده شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/16034" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16033">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">صدای آژیر هشدار در کویت
برخی گزارش‌های تاییدنشده از فعال شدن آژیر هشدار در کویت حکایت دارند.
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/16033" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16032">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/16032" target="_blank">📅 03:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16031">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گزارش رسانه‌های خبری رژیم حاکی است که پایگاه هوایی «شیخ عیسی» در بحرین هدف حمله پهپادی قرار گرفته است
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/withyashar/16031" target="_blank">📅 03:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16030">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ در تروث: هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران، و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!  بسیار محتمل است که آن‌ها هرگز درس نگیرند!  ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار…</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/16030" target="_blank">📅 02:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16029">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhHX3555cJW2kLdVnlZo5dD8hzIFOvhGzsbp_yVNZU2kWEWQNfLRrl_wLupB0k2BqwlyDccyFddG7WALGb_OGYuL2pBZ4XeoOASwaX4kg7mhgvlz-rPOSg5DY9DG_n7UjEmT-4eCs07dbenno1yEbJGvVgFvHhvq0tkwjoUdcHeT7OzITequR5iwoq4MUT17JNvkqgG9n0OtdDP8OHC376quP3bKdkBbUeZo-L-19BI8iOcv8tirOpx0tIQu_G72_7Hs0Zi0P9Q9XYtwdIkCKGqz72y44L3OVE7xZlbALpRN9Yk6ml21wyGXFVghqQSVOVD73ZhfwUxpKaNHUfWJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث: هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران، و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@withyashar</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/withyashar/16029" target="_blank">📅 02:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16028">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/withyashar/16028" target="_blank">📅 02:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16027">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صداوسیما : جزئیات عملیات امشب رزمندگان نیروی دریایی سپاه علیه متجاوزان آمریکایی تا ساعتی دیگر به طور رسمی منتشر خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/16027" target="_blank">📅 02:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16026">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صداوسیما:  شناورهایی قصد داشتند از مسیرهای غیرقانونی و ناایمن جنوب تنگه هرمز عبور کنند که نیروی دریایی سپاه پاسداران با آن‌ها برخورد کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/16026" target="_blank">📅 02:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16025">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وال‌استریت ژورنال : یک پهپاد ایرانی به نفتکشی حامل ۲ میلیون بشکه نفت خام در نزدیکی تنگه هرمز اصابت کرد
@withyashar
🚨</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/16025" target="_blank">📅 02:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16024">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 75.2K · <a href="https://t.me/withyashar/16024" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16023">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">https://t.me/boost/withyashar
این بوستو بترکونین ایموجی اضافه کنم
😕</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/16023" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16022">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇭🇷
کرواسی 1
🇬🇭
غنا 0  پایان نیمه ی اول @withyashar</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/withyashar/16022" target="_blank">📅 02:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16021">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/withyashar/16021" target="_blank">📅 02:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16020">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اهدافی که توسط آمریکایی‌ها مورد حمله قرار گرفته است.
دکل مخابراتی
پدافند هوایی
سایت های کروز
سایت های پهپادی
توانمندی مین ریزی دریایی
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/16020" target="_blank">📅 02:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16019">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16019" target="_blank">📅 02:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16018">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شب حمله
💥
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/16018" target="_blank">📅 01:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16017">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هم اکنون از مهرآباد جنگنده بلند شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16017" target="_blank">📅 01:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16016">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام آمریکایی: حملات امشب آمریکا به اهداف ایرانی تکمیل شده است
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/16016" target="_blank">📅 01:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16015">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">همزمان با حملات و تایید سنتکام بیتکوین دوباره اومد زیر ۶۰،۰۰۰$
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/16015" target="_blank">📅 01:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16014">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبرگزاری مهر: شنیده شدن صدای چند انفجار در بندر لنگه و بندر‌کنگ
@withyashar</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/withyashar/16014" target="_blank">📅 01:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16013">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه سر باید برم بیت رهبری
😂
الانه که موتور بزنم</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/16013" target="_blank">📅 01:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16012">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-wdN59Ki3b0eh8swY3lNBtQwFDk3tr5zjbNTQtdmBth6qk82GKdWn-9FAW1SMZlbipOfikbA4GNb_Y79nJhnvONZ5RskzG1xFXtZrtpNc3B0g9xsMX4ug8BroUEP4lCU-aPSTV13Zur4dwUcpnhytQamZFw4YTzV1MHJanDgO_FhVBfNXgIjeHhnj8nD4lydXxbFqo0v7lFBgf1v62WAkaleCh3WknecwpmDrTB97oXiC_EwoNGwbsi0-kubziopNdJJCCWr2ugcOrZRwt-nWHJ0Udy6LVFIV1QwyRLKn8mmfMEfqpHqePKmwh2mI3uGt2HyS1bqZREcr_v83q6aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ، حضور نُه هواپیمای سوخت‌رسان آمریکایی در محدوده خلیج فارس و کمی دیگر ملحق شدن دهمی از اسرائیل به آنها
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/16012" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16011">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">صدای پهپاد و هلیکوپتر در قشم همراه با یک انفجار‌ جدید
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/16011" target="_blank">📅 01:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16010">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فاکس نیوز : حمله فعلی آمریکا به ایران بزرگ‌تر از حمله دیشب است.
نیروهای آمریکا و بحرین ۹ پهپاد ایرانی را که به سمت نیروهای آمریکایی در بحرین پرتاب شده بودند، سرنگون کردند.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/16010" target="_blank">📅 01:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16009">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در صورت تساوی تیم رژیم جمهوری اسلامی برابر مصر چطور صعود می‌کنند؟ رخ دادن یکی از این موارد کافی است:  1-غنا کرواسی را شکست دهد 2-کنگو نتواند ازبکستان را ببرد 3-بازی اتریش و الجزایر برنده داشته باشد @withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/16009" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16008">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اتاق جنگ با یاشار : انفجار های جدید در‌ سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/withyashar/16008" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16007">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار : انفجار های جدید در‌ سیریک
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/16007" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16006">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNS4</strong></div>
<div class="tg-text">سیریک خیلی بد صدای انفجار میاد</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/16006" target="_blank">📅 01:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16005">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">هیچ شبی مثل امشب نزده.</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/16005" target="_blank">📅 01:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16003">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfcxAzgOOo3QT9EsvWpbkJFvPEYp1P6eZn6Btdeb171LseHXAShvn-3nSDyOqL8Qa0jzhEGBrESt-M0bNFQVqHKww-1vLCZy_WT9AkOaFhLhL1dZrMoLMc0RpkbxYPwNNpcwtzVIe66gXglESIicv6ubfkNuNJ2SZfWN92Cjlqdqj_deQOhsxtlAcjqzfUCceW-uLTrFzUUM44VJFNGDcQxDt-kzyYsGsNGJ_0FCRbdQS1EG_JCSxN34hU-_3e9hA7LOkih1mshQK_6TK_Bhv4NblkBAqg14ISdjVYSvVZDT93ASEO5fcuEI7OISUVwsoi_2CVDZA88b2CNHwlv0vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای آمریکا پس از حمله اخیر ایران به یک کشتی تجاری، حملات بیشتری انجام دادند
فرماندهی مرکزی ایالات متحده (سنتکام)
تامپا، فلوریدا — نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۲۷ ژوئن به دستور فرمانده کل قوا، حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی «M/V Ever Lovely»، به ایران فرصت داده شد که به توافق آتش‌بس پایبند بماند، اما این کشور از این کار خودداری کرد و نیروهایش یک پهپاد تهاجمی یک‌طرفه را صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به کشتی «M/T Kiku» شلیک کردند. این نفتکش با پرچم پاناما در حال عبور در نزدیکی تنگه هرمز و حامل بیش از دو میلیون بشکه نفت خام بود.
در پاسخ مستقیم به ادامه اقدامات ایران علیه کشتیرانی تجاری، نیروهای سنتکام امروز حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های شناسایی نظامی ایران، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، مراکز نگهداری پهپاد و توانایی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز همچنان ادامه دارد. نیروهای آمریکا در حالت آماده‌باش، تهاجمی و کاملاً هوشیار هستند.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/16003" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16002">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahshid</strong></div>
<div class="tg-text">سیریک رو چرا نمیگی بخدا نزدیک بود پنجره اتاق بریزه رو سرم</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/16002" target="_blank">📅 01:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16001">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">انفجار دوم در قشم اطراف فرودگاه
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/16001" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-16000">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromₕₒₛₑᵢₙ</strong></div>
<div class="tg-text">خدایا یا من پولدار شم یا اتش بس نقض بشه امشب</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/16000" target="_blank">📅 01:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15999">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای انفجار در قشم
@withyashar
🚨
🚨</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/15999" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15998">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15998" target="_blank">📅 01:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15997">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">صداوسیمای ایران به نقل از یک منبع آگاه نظامی این کشور گزارش داد صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/15997" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15996">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش‌ها از شنیده شدن صدای هلیکوپتر در قشم ایران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/15996" target="_blank">📅 01:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15995">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دکل مخابراتی سیریک مورد اصابت قرار گرفت
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/15995" target="_blank">📅 01:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15994">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آکسیوس : ارتش آمریکا تو منطقه تنگه هرمز حملاتی انجام می‌ده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/15994" target="_blank">📅 01:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15993">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش مردمی تایید نشده : چند تا انفجار بندر لنگه از سمت نیروی دریایی سپاه
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/15993" target="_blank">📅 01:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15992">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCaptain</strong></div>
<div class="tg-text">پولدارا کوشن یه گونی استارز ول کنن رو چنل
😅</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/withyashar/15992" target="_blank">📅 01:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15991">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خبرنگار صداوسیما زنده از سیریک:
دقایقی پیش صدای چندتا انفجار مهیب از حوالی روستای طاهرویی سیریک شنیده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/withyashar/15991" target="_blank">📅 01:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15990">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش مردمی : یکی طرف گز سیریک بود یکی دریابانی سیریک یکی هم طاهرویی
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15990" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15989">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش مردمی‌تایید نشده : شهرک صنعتی سرخور طاعرویی رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15989" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-15988">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مثل همیشه دقیقا ۱۵ دقیقه جلو هستیم !
💥
💥
💥
💥
💥</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15988" target="_blank">📅 00:55 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
