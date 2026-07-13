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
<img src="https://cdn4.telesco.pe/file/i8YK43z2eXTE5KeXgvS0kEYH8oPa8dGmhvM80gb9P29YPlqClGS_c4-i2J0OfNveJcQ7c59vgN8dWHk7aDJnyVQ4mZFyKX1QXt9paeD83s0lrfBdTw_--B5dOr3VWZa1Yc2722IYxri-xn8KqqBu3D1Tcz4vZ4UUt6a_v4a0xzXmWhYeuZ_j3YZ-ChAeyrgzKOvBVBzEeR5baLietXKMi_Zs3BjZqU6oQtpDrendq0UHLfoLDep_yqjGSEFjW92ofFrETUnJaKPwIMs6lSbabt4Hgb6XVvJk14KQee_PfQRVomAycKTMpFpPBfG-DTRCp2ZILHOqP6OvjD2P4jMsvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 918K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 20:15:07</div>
<hr>

<div class="tg-post" id="msg-133835">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک مقام یمنی: زیرساخت‌های عربستان را هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/133835" target="_blank">📅 20:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133834">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
اکسیوس: محاصره دریاییِ ازسرگرفته‌شده، هنوز اجرایی نشده است، زیرا طبق یک الزام قانونی باید ۲۴ ساعت پیش از اجرا، به مالکان کشتی‌ها اطلاع داده شود.
🔴
یک مقام آمریکایی گفت که فرماندهی مرکزی ارتش آمریکا (سنتکام) زمان دقیق اجرای آن را بعداً در روز دوشنبه اعلام خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/133834" target="_blank">📅 20:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133833">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
سازمان بین المللی دریانوردی: با اعمال عوارض بر تنگه هرمز مخالف هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/133833" target="_blank">📅 20:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133832">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پزشکیان در دیدار با وزیر انرژی روسیه: ایران و روسیه یکجانبه‌گرایی و تلاش برای تحمیل اراده بر دیگر ملت‌ها را نمی‌پذیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/133832" target="_blank">📅 20:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133831">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QcD8Ri5QX9pqkkMcHsHCXgcuwIdRN8GhJ44TGW4d7pZyBuGbivfFWuX-GxodFStnRnio91i3bDcWOxt0f6zbz6FxoSCVqeub3_H_aF1NHy6s7X62plltE4fFZSpMVJcsBW6b2dOTg9VNlg4DS2hkv8LaOip5TqV_4dWg7OvQwMz2hfVsG8nUB1aMMwUnNSthB9XqA3kCsyNy3g28BE4qcMOaMbfyrAlB9W5Nk3FNxsEtkBCJ9Rp8ZGFH-VDaiZe4NJmenSa7jiiY9stHS5ZdD0BH4T8vUVSMFCMAxv5-aTJotUO46CnsDTYrpd_CuNdu6U47WGME1xh6-SfsrGznQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل چندین خانه را در کفر تبنیت جنوب لبنان ویران کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/133831" target="_blank">📅 19:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133830">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
سازمان بین المللی دریانوردی: با اعمال عوارض بر تنگه هرمز مخالف هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/133830" target="_blank">📅 19:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133829">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
نشریه آتلانتیک به نقل از لیندسی گراهام:
اگر می‌خواستم ترامپ، از یک موضع سیاست خارجی حمایت کند، به او می‌گفتم که اوباما دقیقاً برعکس آن را انجام می‌داد
🔴
متوسل شدن به تمایل ترامپ برای تمایز خود از اوباما، راه بهتری برای متقاعد کردن او بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/133829" target="_blank">📅 19:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: احتمالاً قبل از انتخابات شاهد اعلام رسمی دولت اسرائیل برای ایجاد یک هسته شهرک‌سازی در نوار غزه خواهیم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/133827" target="_blank">📅 19:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEEPYYvWaNo8J77w3sl7Lc33VmJMnCFtdRfEgkYLz7deFXrXRHSGfWUTc8DloDOnzAYUSJzhxDwGYAxKTexMrwKsjYzg2rIpjl28u0eh2_Rp3SVkOewvegGGpgtVaxgnKwx50ZLd8Gbh-5iOi0CzyyOgTsLnMWdw7ZC3VXvxOXxSEzKijJRCtAEQjHyUVn46beCU-3S-qGa_x4aWUGD04imcVBJtx-cK_zjitXWOF8aHYOM_15_x3x0M74eZymG048y5_cLLdDU1QWXZ_jAtEvg6M4bKH8KE-E7Sl6Wx-KnQRtyHyHtk4bWhUml_as0vLApgk70aPTuzGmeleIX4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هاآرتص مدعی شده موساد با هدف تغییر حکومت ایران، احمدی‌نژاد را به‌عنوان گزینه رهبری پس از سرنگونی در نظر گرفته و با او ارتباط داشته؛ اما این طرح در نهایت قبل از اجرا فروپاشیده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/133826" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ادعای سلیمی، نماینده مجلس: تنگه باب‌المندب به زودی بسته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/133825" target="_blank">📅 19:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ادارات هرمزگان در روز سه‌شنبه و چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/133824" target="_blank">📅 19:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2cvlTUEPpD2oBeF4Di9qq2XDCt-ryqJODNxDUxMgtnwlk-JM1S41NZMHlto1eBexqvpRmFOiFNWLoGgaNRZup1RvmtrtHVf7ovj3J5LySp7EF_S9Q8Q9sFucbusO8LMF6LKDxHQ1pgX9ijdYYsFBGpD8fSXPQm2_Mph-5xmK07J0XndZxwoSD3Irh7aldwjKKz5DWfqpY57fXjRrGAb1_9ukMeYXEUY6BbnBcRLQBdOuht_yKz6KhHrkKx5eldNb_MfO8011GVTFnbX2qxOyTGk1mKEkmNd2DWyHsxtLPIAj_cerbymNA8bI75BBQwX_VgRrlyHlqlu8yfhx6Jftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ایرانی ماهان ایر از فرودگاه الحدیده بلند شده و در حال بازگشت به تهران است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133823" target="_blank">📅 19:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوری/سنتکام: اواخر امروز محاصره دریایی ایران را آغاز خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133822" target="_blank">📅 19:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZxnygmvhQQqStZx1wF2DHroAU35Wm065QczQog6T1SQuyLKGGoiUDKhqnyvKyuTXwADQNXq0jum5JUvoMj8uGpVeV1IGDCXucA_uAIyDznr81Zb-Xwx0fOFJ_4Ec6SzA-nR1-4HsAg2UatlNRxTVjhbMkXfnithSH250cjIt_eAWTuQqmZJ4ZxTeVwqYe0uxAd9n-4HRuLfHuNtxi8Q8NHBgDQ9OZ2-q_Zr5ylWc4ncTcQZxp3JElsCpKJx71nxME9bK84tDHqBcUjcJNdWgRmYpa8Ra2gQFOffjOVCdJjAT_55zOw_MgMvd46vjp4XADvLwHpLbsKiBeq_eVhiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عبدی و روزنامه اعتماد مجرم شناخته شدند
🔴
سخنگوی دادگاه مطبوعات: هیئت منصفه دادگاه‌های سیاسی و مطبوعاتی با اکثریت آرا عباس عبدی و روزنامه اعتماد را مجرم شناخت و آنان را مستحق تخفیف در مجازات ندانست.
🔴
پیش‌ازاین، دادستانی تهران با استناد به محتوای یادداشت عباس عبدی در ۱۶ اردیبهشت، مواردی از جمله «ایجاد دوقطبی کاذب و اختلاف میان اقشار جامعه» و «پخش شایعات و مطالب خلاف واقع» را از مصادیق بندهای ۴ و ۱۱ ماده ۶ قانون مطبوعات دانسته و علیه عباس عبدی و صاحب‌امتیاز روزنامه اعتماد اعلام جرم کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/133821" target="_blank">📅 19:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
جدیدترین گزارش ماهانه اوپک نشان داد تولید نفت ایران طی ماه میلادی گذشته افزایش یافته و به ۲.۴۴۱ میلیون بشکه در روز رسید.
🔴
قیمت نفت سنگین ایران در ژوئن به ۹۰ دلار و ۷۷ سنت رسید که ۲۴ دلار و ۶۲ سنت نسبت به ماه قبل کاهش داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/133820" target="_blank">📅 18:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اکسیوس: یک منبع ارشد در خلیج فارس گفت که آمریکا موضوع احتمال دریافت عوارض برای تأمین امنیت تنگه هرمز را با متحدان خود در منطقه مطرح نکرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133819" target="_blank">📅 18:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efc5b95abb.mp4?token=e7HKMhGo1fJSMB_VY_Atl0fErYM9KdJGArP9lNlPKlSejokFg1hhemyq2FI7LAG3O-eRe5D9nlynyO2s0uChUxT1ECC8C6duZsEIjPC1krnwoffqQ8IG3bV2XfzCYWjvIGQeneXm_6RWJs0oGON_ePIZ2Fk7WFrGcNnLgQ90aMD2mbyswZeJiFwAW-gEcGlRcpa2ZxqfalNyuCYatUhAzEHTiN3dFZgfaStNNjCsOIDqGperR7UHq1mQERAe2aLFPjpNW3ml3ZGguGlO_gqh2ileKcoNAysICY2TeSrCBoLO_SQvFQOncTcPXDr7r9-lmYBvg8GIRc6PKjjgOr2YZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efc5b95abb.mp4?token=e7HKMhGo1fJSMB_VY_Atl0fErYM9KdJGArP9lNlPKlSejokFg1hhemyq2FI7LAG3O-eRe5D9nlynyO2s0uChUxT1ECC8C6duZsEIjPC1krnwoffqQ8IG3bV2XfzCYWjvIGQeneXm_6RWJs0oGON_ePIZ2Fk7WFrGcNnLgQ90aMD2mbyswZeJiFwAW-gEcGlRcpa2ZxqfalNyuCYatUhAzEHTiN3dFZgfaStNNjCsOIDqGperR7UHq1mQERAe2aLFPjpNW3ml3ZGguGlO_gqh2ileKcoNAysICY2TeSrCBoLO_SQvFQOncTcPXDr7r9-lmYBvg8GIRc6PKjjgOr2YZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیندسی گراهام حدود ۲۰ روز پیش:
به نظر من این اتفاقاتی است که بعداً می‌افتد: اگر توافق شکست بخورد ترامپ تنگه را به زور کنترل می‌کند و از کشتی‌ها عوارض می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/133818" target="_blank">📅 18:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/897dd5d867.mp4?token=iCuo04rULgAsq-_CwcFHyxxFEMZwsGOu1o2HJNJdcdqZhXoe7mCrIWrH1TxgMgm4v-uNY9X-ZxKOR3y7VqdXvgsZfFJ4DZI5s5L2Wo1sPb-Qx4L8FzrEktIhD6cKfG7QdDwXOdj7zBuL6iY5Ld02j-twg55sM6v9vbbOi968xdsnrN7FkMRAh5nrqrpM1wqRhFPJp6FTixa4W3jgGF-96z8yRHdFVu_UQ9w15vDKsPSG_zJ3f8eAtVIkVEWuwZBo8F9Wct6Se26KoWLyziv5Tr5F5CwjCM_0Rex6y54vHJXb6H_mFHFzwEdmLSuwCufScOka0ElSTdHxLK3RcEagvocM-W4wLtlXcuSW8YBI0-JIKd_ezk3Vw1hPdKHiT67Mv9cVEIm3bzWhtz8uKS_VZByt_LhsBYcYwcQLCeEoeZox4L1YFzB5JLxn_CF5ymhR312tj2llpGWb7AXSGA25R_obb6hWF7PkA4HZUKh2JAOUNqSYGERqKOt-Kl0bIo_lvCRINW48NRVmOKbYkZQ-L5cYUZDmgY5jR-33JvnKmeznG6yr0Wih5vCTTk2JhRo5gyIz7SWYe12ErYF4FSsJUBLOH0c4f4wSa4-1tqwQeaVFiQO5iOUQ4TRsTp8HpdSKGpI465ZdjF6LhHc-7baNALUlTRFRq9bqHEBtSfPTGmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/897dd5d867.mp4?token=iCuo04rULgAsq-_CwcFHyxxFEMZwsGOu1o2HJNJdcdqZhXoe7mCrIWrH1TxgMgm4v-uNY9X-ZxKOR3y7VqdXvgsZfFJ4DZI5s5L2Wo1sPb-Qx4L8FzrEktIhD6cKfG7QdDwXOdj7zBuL6iY5Ld02j-twg55sM6v9vbbOi968xdsnrN7FkMRAh5nrqrpM1wqRhFPJp6FTixa4W3jgGF-96z8yRHdFVu_UQ9w15vDKsPSG_zJ3f8eAtVIkVEWuwZBo8F9Wct6Se26KoWLyziv5Tr5F5CwjCM_0Rex6y54vHJXb6H_mFHFzwEdmLSuwCufScOka0ElSTdHxLK3RcEagvocM-W4wLtlXcuSW8YBI0-JIKd_ezk3Vw1hPdKHiT67Mv9cVEIm3bzWhtz8uKS_VZByt_LhsBYcYwcQLCeEoeZox4L1YFzB5JLxn_CF5ymhR312tj2llpGWb7AXSGA25R_obb6hWF7PkA4HZUKh2JAOUNqSYGERqKOt-Kl0bIo_lvCRINW48NRVmOKbYkZQ-L5cYUZDmgY5jR-33JvnKmeznG6yr0Wih5vCTTk2JhRo5gyIz7SWYe12ErYF4FSsJUBLOH0c4f4wSa4-1tqwQeaVFiQO5iOUQ4TRsTp8HpdSKGpI465ZdjF6LhHc-7baNALUlTRFRq9bqHEBtSfPTGmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام : برای اولین بار از پهپادهای دریایی توی یه عملیات نظامی استفاده کردیم
🔴
یه مرکز تعمیرات ناوگان ایران رو تو بندرعباس رو هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133817" target="_blank">📅 18:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIUkcCCoC26UkLALLIHJJ2_hzJUtTZXpdoHnOR3CJlb4E7weFhVNUJpfWJW3S7nBw9MNCOnc9h34F_RvvDJwTtqKLlSr_YJpISsqnw1oKnLbXJDl01_MVdO65HPYSS7AvrPlemah6E7S4cX04pzMUXY-ZdKghQUrtzIJ9-9u2U0nJbFdVPHNxdV4wvPA-mPkElBprShwRiEzhxJ8YRPwFCa7049boa6FPh7Ng-47Kf1alyKpDJYDmeXJEy80PUYZVbZQlrUSjyU7IzC0TkrFRUwVeG1Xb2D4hmIOTqox6BUUw3_zJNvQvQ_zBA371E80y8e7wThFAK4qRjBZ_p8TYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بلومبرگ: در نگاه اول سود ترامپ از تنگه هرمز، حدود ۱۵ دلار به ازای هر بشکه نفت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133816" target="_blank">📅 18:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pjSb8BenvjjFC72mkiRpUl7K7PSSxBSH2hywdsQVOklxN1R-35FQFpPFYRA5oOEFMj0e9YzzFq5_1R95esYjL1JmC2Wj1Vzw8-tEtbNDvqZo01XCb2ESpwG0jht9cpa1YZ7uEX3XDrfcrGaHQntmW_WT8g7QIeiRpUWUSGHujWDb-DPuhKuzi-K-ZuMiHqic4n6ckYWWU4reuqSXYIGu2mz-ZkvwQo5-kNgHe7NTE-Iq59Flb1t0Fj0TRfo7qZoLgH1kLpLr3RAC3ai6Kr4laE3lQSpK9x4zwpO8LP0zj8PBUZPDk7XrgNfHns72-6vqYYd5GgeX1Ii528q2TQdNzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در Truth Social: به فرماندار هنری مک‌مستر پیشنهاد دادم که دارلین گراهام، خواهر فوق‌العاده لیندزی گراهام، را به‌عنوان سناتور موقت ایالت کارولینای جنوبی منصوب کند.
🔴
این بهترین ادای احترام به لیندزی خواهد بود؛ کسی که عشق و علاقه زیادی به خواهرش داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/133815" target="_blank">📅 18:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYuisV7rZCYgIvlI4E1fFBXPcxHiPL1t7lc2L7ZD7P27cQUSDYtDKmmxgUxPyEtSJc7qsk4YRfdPAIjqbo0hOGVElGH1nPBfmGHLAkE8Vndvj0AoxNg1dqd3RA_fSdS1HF6jYQnAJoZZjX1gbRkFOKbUFHAggHZAyPNH4miL_fFIMVOm34mwc4xXBr_nwsgy3i8iC6dHcReMiHny8KLTI-SWaH5-445-2YaVpJd-lCTy8AweILNae2ghbc-QSLWoORv40ECgfpPJ_7rCV1ZEPH9d7EockPQJcLrHM-Ce-2Qb29ZBLkMVNxzTqO518SKzelm5hx2eNdbWDWPb3cmyzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی مجلس:
ترامپ مدعی شده که می‌خواهد نگهبانِ تنگه هرمز شود، برای حراست از تنگه نیازی به کارگر خارجی نداریم! اگر خیلی اصرار به شغل نگهبانی دارد برود نگهبان قبر گراهام بشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/133814" target="_blank">📅 18:26 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
پیت هگست، وزیر دفاع آمریکا:
وزارت دادگستری آمریکا و پنتاگون یک کارگروه مشترک تشکیل داده‌اند تا افشای غیرمجاز اطلاعات محرمانه به رسانه‌ها را بررسی کرده و عاملان آن را تحت پیگرد قانونی قرار دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/133813" target="_blank">📅 18:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133812">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqEvd-A_Qrjr8ATsN4kr1-wWoPzyQcLuH3XLyJErcsSmYuIW92M00VB2PqAHVkdHbpyKf9Q38zewrfJsSTb9sgrC_g6bO9uDPwdY7VcqWku1Sv0Fksy--lOnKz70qWLWTOOdQA3SmvMAfIjdW2YIs7P7zn1Ycz9dU9dkqromA79XAjzfh9cBqZJXlgpYEDblkVO9sx1CQI-EiA2Q1B6QD2sg-sZOu7F2qB6n-GMUZpUDIOzqU4rbNionvZYY_eVHC7zrGvBR9ND5yTnOGipCyv9ADQkvJyT580SXRo3KMup2F8HAvVQiXl99pDeE6oeLuTHTY1ST9h5IK3YRC0wiag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
درحالی قیمت هر کیلو زعفران در معاملات بورس کالا از ۲۶۶ میلیون تومان عبور کرد که قیمت این محصول در برخی پلتفرم‌ها تا کیلویی ۵۷۰ میلیون تومان هم رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/133812" target="_blank">📅 18:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133811">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
شبه‌نظامیان تحت حمایت عربستان سعودی در یمن: با تمام ابزارهای موجود با هواپیماهای ایرانی که به فرودگاه بین‌المللی صنعا پرواز می‌کنند، مقابله خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/133811" target="_blank">📅 18:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133810">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
رویترز: قیمت نفت خام آمریکا و نفت خام برنت ۵ درصد افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133810" target="_blank">📅 18:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133809">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JG8eRBv9AhkM3ongYn7BBlmczSAccWL1QiVLXvaLJA2q-1k3b45ZrBgjbrPw6KFOQ4VrDxspJNeJ7oAkhxS5Be-q3DBa9D-goGpBxRzp_mBUhxZhd2d8_Ybwe7IYb-yxQL6-QNCgzcB9MIMxrYKImJ_FtTwpfMKV1SrJFs_X0OMZdb5-mBMuITB9hfr1i1wbAoYzRvJjeYUThufu8_JBxWVaYAWcPlAcA7QbL35DMcTpLUQuo0mN92PwzB3PPZh36b7prpscGeyCmSt4rdya9SG5ZKr6hPIkGssMyHXqjjsai4F2JVsxYl4dgl-UcDijCu5-2L3kvrrhdLVeNSU8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: به احترام سناتور لیندزی گراهام، سنای آمریکا باید قانون کلاریتی را تصویب کند.
🔴
چین و بسیاری از کشورهای دیگر به دنبال کنترل کامل و تمام‌عیار بر این رویداد بزرگ مالی و همچنین هوش مصنوعی هستند، جایی که ما اکنون پیشتازیم، اما آنها سخت در حال رقابت هستند.
🔴
نگذارید چین در هیچ‌یک از این دو موضوع پیروز شود!!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133809" target="_blank">📅 18:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133808">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری /  ترامپ: عملیات محاصره ایران بلافاصله آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/133808" target="_blank">📅 17:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133807">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
مارکو روبیو، وزیر خارجه آمریکا:
دادگاه کیفری بین‌المللی (ICC) به‌دنبال آن است که خودش را به یک مرجع بدون پاسخگویی برای اجرای نوعی قانون جهانی جدید تبدیل کند؛ نهادی که بتواند هر زمان بخواهد شهروندان ما را تحت پیگرد قرار دهد یا بازداشت کند و حاکمیت آمریکا را به خطر بیندازد.
🔴
ما به دادگاه کیفری بین‌المللی نشان خواهیم داد که عزم و اراده آمریکا واقعاً یعنی چه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133807" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133806">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
فوری /  ترامپ: عملیات محاصره ایران بلافاصله آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/133806" target="_blank">📅 17:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133805">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFW5vw31AQ35C3vgwNG6qIMxQVgTfvA81f8uirHJn7VIQXUGFURV4L7AbO90DJWWM-RDXDj0q48dzvxg9-B_Sp2sBGNtgwMuz3p5-MWCYfeGMAyT0K29V0jwLDgMM3H_adC3KVLoKSP2_tR5LnIH0bXeaEeWe7waB8Pz32fzwS8KAgD0ZiWpYW_s5aT9pVzIn3PScIIJT3-c9N5AHRqiJDOrs3ES9va6Jut36Vwr0juL64YONuHIEOJdThu-tRd7WzRL-15XoYf559hZBSJngLy_4zyWjmvA8mxuyv7inl_wx2wrIgfUzWROBOVLIhdHpzHSJ9n73-98yQ5Y8Qb-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی صاحب امتیاز راه دیالمه شد!!
🔴
راه دیالمه با تیتر های اختصاصی رسما به نام ثابتی سند خورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133805" target="_blank">📅 17:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133804">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
پوتین: حملات اوکراین «مشکلاتی برای فرآورده‌های نفتی» در روسیه ایجاد کرده، اما وضعیت به تدریج بهبود خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/133804" target="_blank">📅 17:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133803">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26b413117.mp4?token=nmIE8a1_3loMhSbEE6-emRmmg3u74B4OiWO2AOsliZmug1wwBt6Lccd5dlCYSa-joYB_5z2Zn67Jk6Fll2Z3gJb7J4b4elXAMdq7_-sUFCOCGkTgsellC7ThOSNPWUjoGe2LDOO25lEOGcl9YuhzNYP9T39r_rspcRdazhJLh0kdlTngY_9fOE-qNDEICOz7oZ1O2r8hhKLqr9Z8dyE5ZKBvX1vi9HISmJv-LE1lRw83t4n-N1B6ec5Yq8hpEoYvf031JpNdcnv9McDcVvrmBdmpmCNixWA6ZFSPToxVTaPPMTeS1vwZ3Hb_PDxQ3tFoO3zqNfwVRsyHy_GiE40Uh6MSYx0qlYKz2tt89f57E2sfAO5D8WGd8kNPwyF7zz5hVCprpt_UBmrG7cP0vka82NBWZi0Z83rSL21GNtP8NlCYGr6EcteXuWHRHJyfhlaZF_EVu7uVumJGA6YCT9enxmaYSL7YyS-r9Aw3_0rTI1LdifRpEZ73eUWreviFFGD2xOk2gU9cwQtngXmXc9A_jEwFcqjrpnw7KpIh5CbZxp4WolIVCqWPFUy0IL-s47LL22jYNKbqrYI16c84tic9hH30ZZMIRBqwdPojdTnaQPHsCsYbiRMIodoeehiDZvl6IVcWjSHQB8TFw3a0ojQ_EljMpKwtmIjMyTWxmRX5-Ho" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26b413117.mp4?token=nmIE8a1_3loMhSbEE6-emRmmg3u74B4OiWO2AOsliZmug1wwBt6Lccd5dlCYSa-joYB_5z2Zn67Jk6Fll2Z3gJb7J4b4elXAMdq7_-sUFCOCGkTgsellC7ThOSNPWUjoGe2LDOO25lEOGcl9YuhzNYP9T39r_rspcRdazhJLh0kdlTngY_9fOE-qNDEICOz7oZ1O2r8hhKLqr9Z8dyE5ZKBvX1vi9HISmJv-LE1lRw83t4n-N1B6ec5Yq8hpEoYvf031JpNdcnv9McDcVvrmBdmpmCNixWA6ZFSPToxVTaPPMTeS1vwZ3Hb_PDxQ3tFoO3zqNfwVRsyHy_GiE40Uh6MSYx0qlYKz2tt89f57E2sfAO5D8WGd8kNPwyF7zz5hVCprpt_UBmrG7cP0vka82NBWZi0Z83rSL21GNtP8NlCYGr6EcteXuWHRHJyfhlaZF_EVu7uVumJGA6YCT9enxmaYSL7YyS-r9Aw3_0rTI1LdifRpEZ73eUWreviFFGD2xOk2gU9cwQtngXmXc9A_jEwFcqjrpnw7KpIh5CbZxp4WolIVCqWPFUy0IL-s47LL22jYNKbqrYI16c84tic9hH30ZZMIRBqwdPojdTnaQPHsCsYbiRMIodoeehiDZvl6IVcWjSHQB8TFw3a0ojQ_EljMpKwtmIjMyTWxmRX5-Ho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرویس امنیت فدرال روسیه (FSB) مدعی خنثی‌سازی حمله پهپادی اوکراین به دو پایگاه هوایی شد
🔴
سرویس امنیت فدرال روسیه اعلام کرد از یک حمله پهپادی گسترده که پایگاه‌های هوایی «اوکراینکا» در آمور و «شاگول» در چلیابینسک را هدف قرار داده بود، جلوگیری کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133803" target="_blank">📅 17:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133802">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
پوتین: پاسخ روسیه به حملات اوکراین، متقابل و چندین برابر قدرتمندتر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/133802" target="_blank">📅 17:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133801">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f130a67f.mp4?token=vSx8AiiW2F6Qug_gjd0L_aRD42hFCu0GyvwCR7S28FcPtxiDq8_3qy3HjelZiZFdcWIouo9m841jHtYQgip4ryFv_p195HfLLXXHFcH-snC6l9NchDlD2VJNDvLNxvRzxdpUCf0FpSrrcLnv5MjuDKWlUu5LknR_MZllMIxBKMucv-DRImjypYh-YHz2WM-0WOTwftD6KMe90XDTvRA8rClzFeT82T6alqyfvDZPXt2UKMBvUO9scPngJkcztFJsltz0l34Si_fm2im-vYaBtDvgfCpZHwgei2DAn3IahZAfFgjw-eVkArpNCRjwGVJZ_z7TczK0PkP3OizDFfIFWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f130a67f.mp4?token=vSx8AiiW2F6Qug_gjd0L_aRD42hFCu0GyvwCR7S28FcPtxiDq8_3qy3HjelZiZFdcWIouo9m841jHtYQgip4ryFv_p195HfLLXXHFcH-snC6l9NchDlD2VJNDvLNxvRzxdpUCf0FpSrrcLnv5MjuDKWlUu5LknR_MZllMIxBKMucv-DRImjypYh-YHz2WM-0WOTwftD6KMe90XDTvRA8rClzFeT82T6alqyfvDZPXt2UKMBvUO9scPngJkcztFJsltz0l34Si_fm2im-vYaBtDvgfCpZHwgei2DAn3IahZAfFgjw-eVkArpNCRjwGVJZ_z7TczK0PkP3OizDFfIFWjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی عجیب سالها قبل روح الله زم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133801" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133800">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
خبرگزاری دولت: قطعی برق در تهران بدون اطلاع قبلی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/133800" target="_blank">📅 17:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133799">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
رویترز به نقل از داده‌های کشتیرانی:
تعداد نفت‌کش‌هایی که از تنگه هرمز عبور می‌کنند، دیروز به پایین‌ترین سطح خود در دو ماه اخیر کاهش یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133799" target="_blank">📅 17:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133798">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
فنلاند سفیر روسیه را احضار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133798" target="_blank">📅 17:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133797">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
گزارش فایننشال تایمز، دبی برنامه دارد تا با ساخت بندر جدیدی ، تنگه هرمز را دور بزند و وابستگی‌ به این تنگه را کم کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133797" target="_blank">📅 17:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133796">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یمن حریم هوایی خود را تا اطلاع ثانوی بست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133796" target="_blank">📅 17:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133795">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z68vfA1BbPuauvCwz_zh0vGJWqMVq_gNVZuBFYrPMHuGAWA8EkqVNKzYBx_X5e04k-9u7r9AeqIHShe8qM7v0IexYr6MTOZPAkhjJKSqLPie0QGXykCSukYYaSWRVFQ7m1E8MCVjlBnf0o9rEPOc1Jr3kMdTqeaym5JZYAMo18VPMSj8yofPWKlc4K0HH_x9Py0ovVMx6FK2RgOVG_NlZmEvcfbisGzP4-XvE1TROZcgwzX44tf2OnM50QePqfTGWmgxzJAffiNlcmp924xc8voICm3402cR_OT9W1_8WDdbW1tUnaUJHhWkoviv3IKV91CPegQeCq53aTboyDhFnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه نظامی حوثی‌ها: پاسخ در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133795" target="_blank">📅 17:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133794">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmsBcXHzFxndUER5RDXAajaGil90y1wU4837GFZCy-916uiLJzjpSxMGWyHNUji86TAIkqrNROlSjMdhBeioEvtnv7XfyWqyO4mZw99ZmD8MfjR0J6GpwhUb8Y3-JVXYMJoT089-wGZfUsBC42_axLtydjlgjFqPcnDk_ZB_h3bT5vA6_0ZUjf7HX_NXNYXNMhD732ERyhGsGrjPLL9CIq1iQyUgr9YdVfx7XmwnZUXZoTwZkbM8eh1Vy7172VftTLnNal6O79VJJ4aXUlDwwoLrJtj4t8kctlFxnFiM4hrtnNGxNAXkjzAb-RQdlNTdwIBF6wLPAiStI9AofsTojQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، کاخ سفید خود را با کاخ سفید دوران بایدن مقایسه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133794" target="_blank">📅 17:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133793">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOjevY-eDf7kO7M1hIZi9zYm-EqIubAPSdIEV_luuPCYSKg61n7WFb7nEJbUgpsaBm3k-m66Nzy_wB8gfcgkaCeJWxxPTlZmNvAFxoLjkXwJQH2TrthlRo_p2HZ3YLAiPx9EiqiddrKoMWCbMRwnJNk4Rc_aiXlwT3BWtNMokCAvy8oLk_wnCF9wd3jr98QGfaOhM-MvtIORit0u0WyGhJwiMT4Wfj3HGnN4A27wt2AvJMjPRgoaZUl4Yc06CaaWDwU2J3ArMhGAScyG5KfjArHDzYOyezrO68wnO_8T0m63paqy0EyOQLp7Y6dh25UQr-Yg9SPcXcrsUH9uk1MrPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ جنگ با ایران رو شبیه یه «مأموریت تنبیهی» توصیف می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/133793" target="_blank">📅 17:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133792">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bf39227ea.mp4?token=Jd9FoiTFFr5nxOUmHNxZG9qL5fvoJoO_aG6xOYSjkKqyOCzqStXxgKtGml-lZVZz2LnneJTrjypqnG1oSpzBeaaqFbelEAJKxxFh7bVFOjVv-bTHkiLpDeaad6-ht_paJW9ktty2zIgQhjcCiNREautISBy0FI8_suM1mRGsztMgV8NidCY2XI2AY_sM235NVHFPShIOLGb-THC608l2PJPATfX4AzGezu8l0QaIejKsxkERofnzDF5PEf-cUknkDJkBQinC-_hiFBvxpPfyVaocSW3ativDwbHrHMmgxB6J___I36ba9S8aHRxXSEwpwgbrD8YTYZHcMwnfqWhUjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bf39227ea.mp4?token=Jd9FoiTFFr5nxOUmHNxZG9qL5fvoJoO_aG6xOYSjkKqyOCzqStXxgKtGml-lZVZz2LnneJTrjypqnG1oSpzBeaaqFbelEAJKxxFh7bVFOjVv-bTHkiLpDeaad6-ht_paJW9ktty2zIgQhjcCiNREautISBy0FI8_suM1mRGsztMgV8NidCY2XI2AY_sM235NVHFPShIOLGb-THC608l2PJPATfX4AzGezu8l0QaIejKsxkERofnzDF5PEf-cUknkDJkBQinC-_hiFBvxpPfyVaocSW3ativDwbHrHMmgxB6J___I36ba9S8aHRxXSEwpwgbrD8YTYZHcMwnfqWhUjIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور روسیه: در حالی که بخش‌های روس‌ستیز غرب در تلاش برای مبارزه با روسیه هستند، این کشور همچنان به روند توسعه خود ادامه می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133792" target="_blank">📅 17:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133791">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvBS5re27p75smDZ3M6GTYBs2L79upVF8SmNp_-CXrOIBZFrBG7GFUuUv7WwRxoXykL26v4_SWKguQQ0nWIW6eRQvONUFr7FdHcf2OgaVdU_-j9QXuyp5Q6GGt4mgbJ3M7NXpS7Drdrou6Dny01LwxuHp2nrImN_Y2c7-HuDL9N7Eg6Uv3u7Jy9A9d1moUAMfB_0G2UI_W_Y9bTlJbiV-ic_0QrnvaRiN_LpePatsqrOV4PsHFGQygNaB8tQgDDClkATmsoeJm2P2rOQmTvFObd4HlUtRdUmmGoP5TCwJCpFk9ez2tz28DP8RqiqPgjgNTdDC17psfOl0SUVeJ4wrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت دوباره رفت بالای 79 دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133791" target="_blank">📅 16:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133790">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رسانه های عربی: سطح هشدار در تمامی فرودگاه‌های عربستان سعودی افزایش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133790" target="_blank">📅 16:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133788">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNynf3Vmflp4JcDO236xMp8e7gPV1QM3IKTDLCNbJoyIgczRk6Mw7h56guGFgMXcvyMojLQ9_jgbRp4otWMTvIhXur8RilIOk2xsYWCWcZoIt71FzFOJz86gyyAgZYXkCXei0lNNxO7sqUnKCiAbPgPMDKzZFHFcdr7ffGSZhieIfe66C5dDD5Bx4TU_zlkYomgnz6OvL2QNaGNbkqfka-do27G88pka0xnwZ7yWvafj80BFVjixJj5WCI-YEZaWX0Xq_24jUi2MrjBTvO0EuwKvEMbJn305EyBxZ9c1-OOfn61texLBxOJJc0WDCGoCdc2Il5pDXNGsBr2vuvkSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EWf-OJ7JcOyGY8K5h6JuSfAwUfxPwTUShfQ60fz-ChHak94-0c3qAmtJKBR-01bgWaqvoFnqdd13UTeJ7CgnYY24f-Z8fjFFT3YDnXs386FkinuOtPcdjhTnyU8YN1vPNMmPSs62nMK104Fz8IJdvWfoC65Xd5hZtc7FKCm0AfKCRR2vxzkj21-UbmT2hYVtusMW9VhEE-S2VuM8Bq0K05yzZYOXtFBK9kx8QXQKzwqB4Z6EqgCwhvsmFTp9HicSaysXcbFGxMbergvcI6Smod2fUiWJzyzLp5QpSLSaqINbPFJr1MBQHfagldam9rq5pY3Wo53rzU7AHngGdNl9Tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترکیه و مصر یک توافقنامه همکاری امضا کردند که چارچوب همکاری‌های آینده آن‌ها در حوزه صنایع دفاعی را تعیین خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133788" target="_blank">📅 16:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133787">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزرای خارجه آلمان، فرانسه و بریتانیا حملات ایران به کشور های عربی و همچنین ناامن کردن تنگه هرمز را محکوم کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/133787" target="_blank">📅 16:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133786">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی قرارگاه خاتم‌الانبیا:
نمی‌گذاریم آمریکا در تنگه هرمز دخالت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133786" target="_blank">📅 16:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133785">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خاتم الانبیا: مسئولیت همه ناامنی‌ها و گسترش جنگ در منطقه، متوجه آمریکا و کشورهایی می باشد که با ارتش جنایتکار آن کشور، همکاری می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133785" target="_blank">📅 16:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133784">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb0fc1149.mp4?token=VHINaSKFNYsEgvQesWr3aHMP46iGNlNmuWgWfWeCiRBdk6fBUOYkke1ue2tlqfPFxLzFJQiTUapKLt0FCZ5S13AfSPa5zL2Z2C4vAgF4dicfNnEulGDreggdm6NGjFYDS6kKgxKDuZB2dd1EFkNAgi2MGkDcw2bQvSJ5xgwDXGE7nQbYmo74UXW29amvi8MTOmS1nnXpwQxPX4yGs5-WAXNFRNeV_2Rp4THvtPUufrRHQ83vc2UycmGj0yaa9kuYIjjHqmbKAK4w9r45iLcS8cXVUaGh3QSm6arNFtEP5-H1LwgmSYQX_IQYpwOSkinQ7ANV5Ow5j_cElWV68To-iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb0fc1149.mp4?token=VHINaSKFNYsEgvQesWr3aHMP46iGNlNmuWgWfWeCiRBdk6fBUOYkke1ue2tlqfPFxLzFJQiTUapKLt0FCZ5S13AfSPa5zL2Z2C4vAgF4dicfNnEulGDreggdm6NGjFYDS6kKgxKDuZB2dd1EFkNAgi2MGkDcw2bQvSJ5xgwDXGE7nQbYmo74UXW29amvi8MTOmS1nnXpwQxPX4yGs5-WAXNFRNeV_2Rp4THvtPUufrRHQ83vc2UycmGj0yaa9kuYIjjHqmbKAK4w9r45iLcS8cXVUaGh3QSm6arNFtEP5-H1LwgmSYQX_IQYpwOSkinQ7ANV5Ow5j_cElWV68To-iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه بمباران فرودگاه صنعا توسط جنگنده‌های سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133784" target="_blank">📅 16:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133783">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
اظهارات ترامپ درباره ایران: نرخ تورم در ایران ۳۵۰ درصد است.
🔴
شش ماه پیش، این نرخ ۵ درصد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133783" target="_blank">📅 16:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133782">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25f9f23c23.mp4?token=fp2sQ0Z5s150FtNU4-Fhm0Rbx2RRoYgtifnJqjuf2jR6LfygHUbygPwEou7w7viQljISvZ41d3i1V4BiWksMIO-05ISMXhyXu8P_gVvNM4HeqI7qSVBFbqxtheDE0wt12c6FVpDg9dSjvopJovabiSCXBNIrM-_CDXmEyylSCYNahUlX_TsnbTPkImgkyJa5Lsxw132poRngPmzvueATpoUYI0kkZnst_RS7eZioNEJwSGfIaAFiHmaKx_Ys9c89dVvnpZhUw-ei07eanTGICBuwUGieB9nizKp2VlzaWGsapWgFTakUZ1ipdM1h-aVB_zXtW6_tRH9g4abbs89dvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25f9f23c23.mp4?token=fp2sQ0Z5s150FtNU4-Fhm0Rbx2RRoYgtifnJqjuf2jR6LfygHUbygPwEou7w7viQljISvZ41d3i1V4BiWksMIO-05ISMXhyXu8P_gVvNM4HeqI7qSVBFbqxtheDE0wt12c6FVpDg9dSjvopJovabiSCXBNIrM-_CDXmEyylSCYNahUlX_TsnbTPkImgkyJa5Lsxw132poRngPmzvueATpoUYI0kkZnst_RS7eZioNEJwSGfIaAFiHmaKx_Ys9c89dVvnpZhUw-ei07eanTGICBuwUGieB9nizKp2VlzaWGsapWgFTakUZ1ipdM1h-aVB_zXtW6_tRH9g4abbs89dvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ خمینی و سلیمانی رو اشتباه گرفت: من خمینی را کشتم، که یک ژنرال باهوش اما دیوانه بود.
🔴
ببخشید سلیمانی من سلیمانی را کشتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133782" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133781">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت: نمی‌توانیم انتظار داشته باشیم که کشورها از ما بخواهند به صورت رایگان از تنگه هرمز محافظت کنیم، همانطور که سال‌ها این کار را انجام داده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133781" target="_blank">📅 16:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133780">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3755f54a.mp4?token=nLKRZfgw28H89_JFkAvl2OB8EXfTAXcYURrGy7xr6XzdZxLZr4BcypxupS3IY1omiA2QBlQt1cG9Vb1GtbDSUjixQSpGk1YVRgl3fmn1icCtjNUPzrBZJfzPDUYAEWPqs6UVFpLMJQOwqvMWenfepoxNVcNDIbTsrKqVJGxA9oc9FnAjiWse7FxxQiy06CeynjbV_3EvxkQGzlXOM_6WuiEjASjf4T-2r29cIpJCo13-SX1-IqLnODbB3RwIX46-2htr5XfSxngCHTvfYRvtodbOnvVfgRUmwEyrAlQqZsW-aeb7zx9vK--c1DX0oC8jwLuFK9Wxq8hcDiFfmz95Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3755f54a.mp4?token=nLKRZfgw28H89_JFkAvl2OB8EXfTAXcYURrGy7xr6XzdZxLZr4BcypxupS3IY1omiA2QBlQt1cG9Vb1GtbDSUjixQSpGk1YVRgl3fmn1icCtjNUPzrBZJfzPDUYAEWPqs6UVFpLMJQOwqvMWenfepoxNVcNDIbTsrKqVJGxA9oc9FnAjiWse7FxxQiy06CeynjbV_3EvxkQGzlXOM_6WuiEjASjf4T-2r29cIpJCo13-SX1-IqLnODbB3RwIX46-2htr5XfSxngCHTvfYRvtodbOnvVfgRUmwEyrAlQqZsW-aeb7zx9vK--c1DX0oC8jwLuFK9Wxq8hcDiFfmz95Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
رژیم ایران ۵۲ هزار معترضِ رو کُشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133780" target="_blank">📅 16:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133779">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
ترامپ در مورد ایران: ایران در آستانه دستیابی به سلاح هسته‌ای قرار داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133779" target="_blank">📅 16:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133778">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ :هر بار که ایران پهپاد پرتاب کرده، نیروهای آمریکایی پاسخ بسیار سختی داده‌اند و ایران تاوان این اقدامات را پرداخت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133778" target="_blank">📅 16:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133777">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e61353409c.mp4?token=j8_ul6p9WyumbcCSY9ZRh8N5XQezfzZy8fJcEIfOuSASbEQmg7jYN4CmVWDi7Eyv8Fc_jkkMfsrpxFqUiIJem8vMqKgybx6t5GtALkdm_7yY-IdhYFuGWTA0UHo8qZ_k6mtSnXMh9yt8IuT5qXeCs5unWmgAFwOk8vtz5q38R6O3NW3ZJC6U8OYouCxQFbt49xyUBE8Eh8-rsAu5n92px_iNIJO2bn6NwSSEfEv1x4dgpv9RbaBQsNTzXHMTmkjjff9MCEd2X6Tn7WU4B_t_uZCj81iO_05DGzi-j24WEmfvnmy-FUt3YNtlOflyRrcdfgi6o3L8QspguGWNjDjBkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e61353409c.mp4?token=j8_ul6p9WyumbcCSY9ZRh8N5XQezfzZy8fJcEIfOuSASbEQmg7jYN4CmVWDi7Eyv8Fc_jkkMfsrpxFqUiIJem8vMqKgybx6t5GtALkdm_7yY-IdhYFuGWTA0UHo8qZ_k6mtSnXMh9yt8IuT5qXeCs5unWmgAFwOk8vtz5q38R6O3NW3ZJC6U8OYouCxQFbt49xyUBE8Eh8-rsAu5n92px_iNIJO2bn6NwSSEfEv1x4dgpv9RbaBQsNTzXHMTmkjjff9MCEd2X6Tn7WU4B_t_uZCj81iO_05DGzi-j24WEmfvnmy-FUt3YNtlOflyRrcdfgi6o3L8QspguGWNjDjBkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اونا یه مشت آدم بد هستن، اینو مطمئن باشید
🔴
من معمولاً این‌جور حرف‌ها رو زیاد نمی‌زنم
🔴
الان هم با دردسرها و مشکلات خیلی جدی روبه‌رو هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133777" target="_blank">📅 16:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133776">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
ترامپ: ما دیروز یک نشست ۱۱ ساعته با ایرانی‌ها برگزار کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133776" target="_blank">📅 16:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133775">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ: این یک توافق قطعی‌شده بود، و بعد آنها آن را شکستند. آنها همیشه توافق‌ها را نقض می‌کنند. ما با این افراد ۱۰ توافق داشته‌ایم و بنابراین ما فقط قرار است ضربه بسیار سختی به آنها بزنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133775" target="_blank">📅 16:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133774">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ترامپ : بایدن به سمت ایران متمایل شد و همین باعث شد ایران قوی‌تر بشه
🔴
ایران به خاطر سیاست‌های بایدن خیلی قدرتمندتر شد
🔴
البته به نظرم خود بایدن هم تصمیم‌گیر اصلی نبود، چون آدم باهوشی نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133774" target="_blank">📅 16:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133773">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: باید 47 سال پیش علیه ایران اقدام میشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133773" target="_blank">📅 15:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133772">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
ترامپ : ما کنترل تنگه هرمز رو دست می‌گیریم
🔴
احتمالاً این کار رو انجام می‌دیم.
ما نگهبان تنگه هرمز می‌شیم و این بار بابتش پول می‌گیریم
🔴
۵۰ سال از این تنگه محافظت کردیم و حتی یه دلار هم نگرفتیم، اما از این به بعد ازش درآمد کسب می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133772" target="_blank">📅 15:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133771">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
ترامپ: ۵.۲ درصد از رؤسای جمهور کشته می‌شوند و ۸.۵ درصد هدف گلوله قرار می‌گیرند.
🔴
رئیس‌جمهور بودن خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/133771" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133770">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ترامپ درباره ایران: اوباما از همه بدتر بود، چون اوباما واقعاً به طرف آنها رفت؛ چون، می‌دانید، او یک، خب، بهتر است نگوییم. بگذارید آن را برای زمان دیگری نگه داریم.
🔴
ایران مجموعه‌ای از "افراد بد" است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133770" target="_blank">📅 15:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133769">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / ترامپ: ایالات متحده قصد دارد حملات جدی علیه ایران انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/133769" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133768">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ترامپ: ایران از من چیزی دریافت نکرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133768" target="_blank">📅 15:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133767">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: ما عوارضی را برای اسکورت کشتی‌ها در تنگه هرمز دریافت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133767" target="_blank">📅 15:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133766">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ برای  بار هزارم درباره ایران: ما یک توافق داشتیم، و آن‌ها آن را نقض کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133766" target="_blank">📅 15:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133765">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ترامپ: شب گذشته به ایران ضربه بسیار سنگینی وارد کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133765" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133764">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: ما همه چیز را از ایران می‌گیریم - نفت، طلا، زمین، غذا، همه چیز متعلق به آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133764" target="_blank">📅 15:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133763">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری / ترامپ: رهبران ایران مذاکره‌کنندگان حرفه‌ای هستند/ما کنترل تنگه هرمز را در دست خواهیم گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133763" target="_blank">📅 15:45 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133761">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0tK2UzXaKqMrfpgYcROgEwRMYxbXVZue7KNh62vC2dmv3lZcFmcq1fXDBIRx82b2JWeOV0C6ewfz2FJArZDQU5VoIGSCeOIDAD5sY4qvM5jSjJ2Wpx14SFvbmDoqWtz-pz4u1ir-sS2npSshGmagVtwZWsM7DaO17DnMswv-IjR3-Q_8hwR4mSuHpY9nMebpts1Xfv9Qy7XjUldy5XrzKcFIZMH9_cRDdIUUSmGK12C1ipu7PVy6Wtd9cWjxvcnYNuxThsqSr9jKJhTOxizWceKbS13PVDJRqx8BpXUhNE1GLnWM_o-caJuySZ11er-DgjYGm2dxAGQU9v2DPh0Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a550f8c82.mov?token=mLFYR-5vxy3eFJHSj1Ve8ii0ikbK97ZSZeWQTaeeggSi087gJLaLzIgoQiqH5JSK2aK8RhtN6PMs5TQNnMK-2KNyMvKHFaEkFdQl0NFoUlG7gay4o3oEQW8y_VI2DvKNuPxf6o0TU6nvOSw9-jXnll1WH0WAgJMnjQSBjtSOaXcs8lkcs0cB1MmNGYkg3vljS43aLwzP9qWPiIR7obqYuqWrUZSWnBlf2yLtl3FPWW8W58wn04XlOJ4io4R7SERdREs85Y_obevrdREQLB1Zra4mPbTc1zzZs6rJw0NFz9fDCxGmTLIjYp6U7py9tAl2fzIPGMuaM1FU9kbebCle7oeHGboaBTdt-D_nqMbK9L0_AewBNuBV7ZHsntlRkmvEm7d40Vx-GsioyEx2IR3_Ai-ZdJPXhGaa0DBVH934N6AWRDVk3_hRlTh9boWaMcp-_5mX9FHV9qxXxYxs9SNxuQl2LDZzOX11KcJL1gWSz0SQPhstu21zXQIXhPFoDpshtim8oYxGolEbfJGzume9pdHXFi2FETuRYVscKvcOVi1dNMDA9LbMhRs12KWQVZgPMFAx8zSzqD-AVU4q1-k_I_QO8ywMIoRlGfU4cLFSSdIMQqZmBKozNe6U_zJMsdMdtAXwBzzJs4HaRAaFrymvhZn2W234xewpWtIuwe5Skio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a550f8c82.mov?token=mLFYR-5vxy3eFJHSj1Ve8ii0ikbK97ZSZeWQTaeeggSi087gJLaLzIgoQiqH5JSK2aK8RhtN6PMs5TQNnMK-2KNyMvKHFaEkFdQl0NFoUlG7gay4o3oEQW8y_VI2DvKNuPxf6o0TU6nvOSw9-jXnll1WH0WAgJMnjQSBjtSOaXcs8lkcs0cB1MmNGYkg3vljS43aLwzP9qWPiIR7obqYuqWrUZSWnBlf2yLtl3FPWW8W58wn04XlOJ4io4R7SERdREs85Y_obevrdREQLB1Zra4mPbTc1zzZs6rJw0NFz9fDCxGmTLIjYp6U7py9tAl2fzIPGMuaM1FU9kbebCle7oeHGboaBTdt-D_nqMbK9L0_AewBNuBV7ZHsntlRkmvEm7d40Vx-GsioyEx2IR3_Ai-ZdJPXhGaa0DBVH934N6AWRDVk3_hRlTh9boWaMcp-_5mX9FHV9qxXxYxs9SNxuQl2LDZzOX11KcJL1gWSz0SQPhstu21zXQIXhPFoDpshtim8oYxGolEbfJGzume9pdHXFi2FETuRYVscKvcOVi1dNMDA9LbMhRs12KWQVZgPMFAx8zSzqD-AVU4q1-k_I_QO8ywMIoRlGfU4cLFSSdIMQqZmBKozNe6U_zJMsdMdtAXwBzzJs4HaRAaFrymvhZn2W234xewpWtIuwe5Skio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از یک کشتی باری غیرنظامی با پرچم توگو که امروز صبح مورد اصابت پهپادهای انتحاری "گران-4" روسی قرار گرفت، در حالی که در حال تخلیه کودهای معدنی در یک بندر اوکراینی در منطقه اودسا بود.
🔴
گزارش شده است که ۱۰ نفر مجروح شده‌اند، که حداقل ۳ نفر از آن‌ها جان خود را از دست داده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133761" target="_blank">📅 15:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133760">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دفتر سیاسی انصارالله یمن: در اقدامی تشدیدکننده و خطرناک، عربستان سعودی به فرودگاه صنعاء حمله هوایی کرد تا از بازگشت هیئت ما [از ایران] جلوگیری نماید، اما در این کار ناکام ماند.
🔴
جنایت هدف قرار دادن فرودگاه صنعاء، تجاوزی وحشیانه علیه مردم ما، تعرض آشکار به حاکمیت ملی و نقض قوانین بین‌المللی به شمار می‌رود.
🔴
هدف قرار دادن فرودگاه صنعاء گامی است که نشان‌دهنده سطح کینه و جنایت‌کاری رژیم سعودی و پشت پردهٔ آن یعنی آمریکا می‌باشد.
🔴
این حمله در چارچوب تحقق خواستهٔ آمریکا برای تداوم وضعیت محاصرهٔ ظالمانه‌ای صورت می‌گیرد که بیش از ۱۰ سال است برقرار است.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133760" target="_blank">📅 15:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133759">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vc4Eapdgq-i7Xf464UTshib5bL69Y6kpcEWDNUl_FJkc6PCSF6w6lNlHEfLQf-LUoYTtPKX9YXCtAtONmoA1MFQv4IeLaS6KsL8kK3E3HqKV9E0oSmodPW9b7nBLfXjHE_ATTpDneO2pP7cJlSqvP9nfE6_TEhEmScKukoNXUi4BM4P5TIjZHfyCz0DLl-KGSLuH9krZUgD6c0d0h6p3WdlnE6Kt7LxZCLGf_e2ut61Tr8tEjCflsHJ7u6yTyYSHUkMhu1qS9Na1yLvF44YQ8Tzhvjig0SdT0iYT-3XwoAJxNBmMZwZ8ze2gm_HNjCr-NerCFObsp3oGxHNxYWBCmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون هواپیما ماهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133759" target="_blank">📅 15:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133758">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg736C4akKpEIt0hCCOxn-k1qPspSuFZ48bswN126nF4q8q2Xj3Q-rT-f6Kq9vxilPZteRm-faqSJUWuKuN37J-bWT_fs1zBpZsWrDfQLsIhNPCUtRGyvFWl-pyQ5Ou6Uf1ACJevYcvt7VFYMy2mLSB_ssuIJjPyCgHsIseVPTj9DcBEs1k1BrdotfaZ22nPDYoOXcbaS54oNGxAl-mPR8dKXqqrCYr32vqo5bwkM8fdl36_E-6I6D0wlRMUYCuxvzp3175TqaUcV80ZH980b9EKenVQ0tvW35IJBOuzHVNuR_iwRyVWq2qhKgTHw-olDg8VSBwuXd75p_ZXr4pktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزام الاسد، عضو ارشد انصارالله یمن نوشت:  هواپیما به سلامت فرود آمد، هیئت اعزامی رسید و محاصره با قدرت شکسته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/133758" target="_blank">📅 15:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133757">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری / تاییده نشده: برخی از مقامات و فرماندهان ایرانی برای ملاقات با مقامات انصارالله یمن (حوثی ها) در هواپیما حضور داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133757" target="_blank">📅 15:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133756">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
وزیر دفاع یمن اعلام کرد ما به هر طریقی که شده با ناقضان حریم هوایی یمن مقابله می کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133756" target="_blank">📅 15:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133755">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
فارس:  هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133755" target="_blank">📅 15:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133754">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
فارس:  هواپیمای ایرانی پس‌از حملهٔ عربستان به فرودگاه صنعا، در فرودگاه الحدیده در غرب یمن فرود آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133754" target="_blank">📅 15:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133753">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
حزام الأسد عضو انصارالله : رژیم سعودی متوجه خواهد شد که خودش، قبر خودش را با دست خود حفر کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133753" target="_blank">📅 15:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133752">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا: یک حادثه در فاصله ۵۰ مایل دریایی جنوب عدن در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133752" target="_blank">📅 15:17 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133751">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axLtLGXeVt3NpM89k5pf9cNCPRgYvtmpasqGN73_HFePF5h7j7s8KR0FqdvAqDWUoijshFHczfHm8n51sgEyCyHTTpeD6G1p2UgMqxcVvHnL0ejwB5jRNxI8QYhMBa2TxB347H3rYS6G1IhcMnjVnU-9lYsW7dcyoPTwRCVvRhnnmWl85Sk29n79pn3LEbml3AN8tvrUB5H8M90fokeSGZFulPDqMHlso6PG9lj6-UOKXEcjPlOVeN2imFiZ13SPM1Z4NgwbJ29dAkwKM0RAgdmGOEFAWCUhlxJsHhBWfnqnVFu5tIjWaam0vI5WFqnqVxhsZdIIXJ6Q_jxaLxXKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عملیات تجارت دریایی بریتانیا: یک حادثه در فاصله ۵۰ مایل دریایی جنوب عدن در یمن رخ داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133751" target="_blank">📅 15:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133750">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
فوری / عملیات یمن شروع شد
🔴
هدف قرار دادن یک کشتی نفتی در سواحل یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/133750" target="_blank">📅 15:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133749">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فوری/ بریتانیا رسماً سپاه پاسداران  را به عنوان یک سازمان تروریستی معرفی کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/133749" target="_blank">📅 15:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133748">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
یحیی فست: دوران کاهش تنش تمام شد و بزودی از عربستان انتقام میگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133748" target="_blank">📅 15:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133747">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
وزارت امور خارجه دولت صنعاء اعلام کرد که عربستان سعودی اعلام جنگ کرده و باید مسئولیت کامل این اقدام را بر عهده بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133747" target="_blank">📅 15:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133746">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
وزارت دفاع یمن: شبه‌نظامیان حوثی مانع از فرود هواپیمای ملی یمن در فرودگاه صنعا شدند و بر نقض حریم هوایی یمن توسط ایران اصرار ورزیدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133746" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133745">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
تصاویر دیگر از فرودگاه بین‌المللی صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/133745" target="_blank">📅 14:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133744">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فوری / صدای انفجار در پایگاه بن زاید، امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133744" target="_blank">📅 14:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133743">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / صدای انفجار در پایگاه بن زاید، امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133743" target="_blank">📅 14:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133742">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2PxnAk1jhLessCaQznmaHvx_cWXDbJRO0oA3rmMagckMSUNCOYWLG2MYj79aTCZiZFPJwmfCna7QqSa7aEqDCsISe_qfx3r1joAz26Ko5_vmhyuUZCIg7f4x-f678xGfJu6vPIS_U51M5sDnKXzra2E9K3va_YL13q7EUUBDTePg4H24krhNXflapUCdfn3fj9fgi66FOzey7tDu7vDhF9z5Q0-QkDzazl3V1ktkxO9iMIzmH0STcR0cO4wyBof6l54veriby2I_vg6VfvOOpuUMKwm4w9E-m1hw9RBpzB2-2UIy6rkifjcZMijiUeYUFoi0snbkWhuV0isDRfBCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیش از ۳۳۰۰۰ نفر درحال مشاهده حرکت هواپیمای ماهان به سمت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133742" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133741">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
هواپیمای ایرانی اصلا به هشدار های عربستان دقت نمی‌کنه و درحال کم کردن ارتفاع برای فرود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133741" target="_blank">📅 14:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133740">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: عربستان به مرحلۀ کاهش تنش‌ها پایان داد
🔴
حملۀ عربستان به فرودگاه صنعا بدون پاسخ و مجازات نخواهد ماند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133740" target="_blank">📅 14:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133739">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PecYWNAW319njrHeQcQFuKTZswa2Xv0oQDL_QRaG0OKS33qRF6Ak1Raqhi5XCgXsdIcLgY9jg8sHUT8ic3fs1t9TB3LOfAlq2JUfP2blYZ89j0AfofvM7SAB1vbkg8EuYrjOSALMDzxhjUAwIXs983s-RhSeSFUBFfCuUTDik4Qz3DqiCYR74XBr7rilAHulN2BNZQzBhjCoFn_e_ElasFPcart_fJyo5lA--1OK8SSl7MwPigHbrgnCJlywqx0lmdyjGL_RNpxfq1Jge-gU47u1dzwZYsPY2fMuBdSeAnVg0bnwaSvVcTdROCgNQbo1faV6VAAdculiZd9hcUkk_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای ایرانی اصلا به هشدار های عربستان دقت نمی‌کنه و درحال کم کردن ارتفاع برای فرود است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/133739" target="_blank">📅 14:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133737">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puUiOBbU1uoL1TgDC93N-wokorixCJJ_vR2txOv7-iJIdgXszHGBjCiWiAzBWnxhzXcTLKhMIBRTMt2Bfpibcbp_rw5QayVXRI68_zOpWl1BypUlXCatQVj0sSBI7Z9cSypS9ZDn2MQcjifsyHTR5AQZAXyxRy2GaJA1iQYEtSK41rcu3_SVnutHOmmRo6gEHgrQ6NYeBL91q9b1q2-PjASJyCPORD726suCUaNTmbxKQnUK9gpyH0y5czbZoSZhl2bve7S8uis9dFL0vPirj1_ptX2uhmSikLA5gB1fNYfkTg0YW2GHF5_Y7M1y1CwB7u3Cm-owVVDd40eerdP2BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5rI-dxCu0AJ4bLr9zG-anz7bFcc-UKfpxP0cocmVLX3RPmR5ijfYGWz6cN2m4cYxingJbysm25Qi9WTtaU4lzuiDFE7DgCoFA0x5nKi8p0lMtb97q1wF7-okzXT9gOjTm-BssUabA3kv71bxFGkL5j-SqVztKiK8561yWPWXSv7PPfISB6CthJ6dkOBg0WSezXczjH-x_FsiigxxVpxH06txoMG_W48DdTN8W8aErZ3UDEjRIVg7pTPd-D6UD6tW8u75miHe-YjKT2H2QAbc6dSSC0y1UHShCOeNIr7cUnRl51W32pXV0ZXsM3nPqpIiIY4EE3xhDvHdCc9uThppQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از فرودگاه بین‌المللی صنعا
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/133737" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133736">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjvDtrqoyL7EOZg0YNUx4E03RePkneDIT817ceB5AMxDWXDwi1fLiekKbou0TUrRaE7MWeGccyzsF0eDKi8DSd2d5_2ZkeSMgpNKZXiR2TWczfKTUQn4IUI9lz1cHnII5PQv5dHlRzXrifNhaifBejNXkRBXSZnAf6aGH5o8yC9zvaxN8qFfhFGmOU2i0_4_PMinV8zun5Ave-xN6duYxmimD3VQMM_zjMUHpigBs1DWbFxtgGD40cW17ECqH0OM2A_gsSodgI-vmVVAePtCZAZgXwcHXmE_zWPdWDNXon64nQf4bZ3Zpp_-QUxt-MCyFrL46vwDNvEAxdeThUEB-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جنگنده‌های سعودی، فرودگاه صنعا را بمباران کردند و دود بر فراز این فرودگاه دیده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133736" target="_blank">📅 14:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133735">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری / شبکه المسیره از بمباران فرودگاه صنعاء توسط ارتش عربستان سعودی خبر داد.
🔴
همزمان وزارت دفاع دولت وابسته به ریاض نیز خواستار تخلیه فوری این فرودگاه شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/133735" target="_blank">📅 14:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133734">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
چین: تردد از تنگه هرمز باید به درستی مدیریت شود، تنگه هرمز یک آب‌راه بین‌المللی برای کشتیرانی است
🔴
از سرگیری هرچه سریع‌تر تردد آزاد و ایمن در این تنگه به نفع تمامی طرف‌هاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/133734" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133733">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
صداسیما: تنگه هرمز به دلیل نقض تفاهم‌نامه توسط ارتش آمریکا، همچنان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/133733" target="_blank">📅 14:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133732">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
وزیر دفاع یمن: با تمام توان با هواپیماهای متخاصم ایرانی مقابله خواهیم کرد
🔴
ما ایران را از نظر قانونی و اخلاقی مسئول نقض حریم هوایی یمن می‌دانیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/133732" target="_blank">📅 14:21 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
