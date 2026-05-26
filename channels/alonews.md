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
<img src="https://cdn4.telesco.pe/file/IhvyOaqUacOi1_M3f_487NVX9KJCyfcXHPI3fho1Hw93Em7lMDlKgYpBoSxp89C0m9LPi82cTTyaxXey7gY9GrWvahBtJoy8mDUBd2yx8E4_1ZtqQ3fW8rh64eC4SOcjFgPkU1eVPZnm_EGoXMkwMgokZRTEzjxWYhIclf5QLAkuSOC00Ob5t0b73fS5lKcNYrqJBwDI8jWhR63hd0ovL2yryW8CObHqhuIS4W3M9Z_TbLzgTQr-DStuA9QXQNkGxVWhMQAKw3Rmv7Hq4kff1jm3KtelyHkGyew2pMJHeqI_yB2FXh3lC5uJqZVmKE6G2TlAuttLJKAF6cqABbrN9g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 935K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌پشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotجهت رزرو تبلیغات👇https://t.me/ads_alonewshttps://t.me/ads_alonews</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 21:10:54</div>
<hr>

<div class="tg-post" id="msg-122886">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی در گفتگو با کانال ۱۴: حمله به ایران پس از دریافت «پیام مشخصی» از ایالات متحده، در این مرحله از دستور کار خارج شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/122886" target="_blank">📅 21:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122885">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
صدا و سیما شروع کرده به صورت رگباری داره گزارش میده که اینترنت نباید وصل می‌شده و اشتباهه
🔴
حتی به عارف که گفته بود به‌خاطر یه راننده نباید اتوبان رو بست تیکه انداخت و گفت اتوبان قبلش باید ساماندهی بشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/alonews/122885" target="_blank">📅 21:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
نیروهای دفاعی اسرائیل دستورهای جدید تخلیه اجباری برای چندین شهر در سراسر جنوب لبنان صادر کرده‌اند:
🔴
— خیرابت سلم
🔴
— بیر السناسیل، قابریخا
🔴
— مجدل سلم
🔴
— قالاویه
🔴
— کفر دونین
🔴
— تولین
🔴
— ساوانا
🔴
— صلعا (صور)
🔴
— برج قالاویه
🔴
— جبیشیت
🔴
— القصیبہ (نبطیه)
🔴
— فرون
🔴
— ابیا
🔴
— دیر کیفه
🔴
— کفر سعیر
🔴
— صریفا
🔴
— الغندوریه
🔴
— النفخیه
🔴
— ققیات الجسر
🔴
— عدشیت الشقیف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/alonews/122884" target="_blank">📅 20:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122883">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH6sm4C2ciDLxid-CVYiRZ6u4jkL4YlcLE1QJHfc2QhgLORvPKJyFMVIFXfN7TjebF8SIt-Z6bqlTk1BiGQxgeL01T8SYAdhxZs0JYOi2XAoK_qILYUsrClNtCIL3I1Ngcq56ZgzVJqlPZdeVtqo2sPjMO6tQhxCqAdRJd2bhtxWIzbM9fuo69A_29dIBYFp4Xe8o2RaKb3aPiTJGvnfGpHgAuFJFNWZDr1LDVCItWtYZDPUUuPBqcUUUoKHGKl_fXbpQljVwYcn462FxjgZVx2xI_a7bLY5wisezKQ9XO6vV_t-ntoyqzmvra1wRWlgrrdhGRyANCcH_d30TB5hUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانفیگ فروشا وقتی می‌نويسن خوشحالیم که همتون وصل شدین
❤️
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/alonews/122883" target="_blank">📅 20:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
ادعای عبدالخالق عبدالله مشاور سابق بن زاید و از چهره‌های بانفوذ امارات: امارات گام‌هایی محتاطانه و حساب‌شده را برای کاهش تنش با ایران برداشته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/alonews/122882" target="_blank">📅 20:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/QD-bwU8qvlYEv9mwA9CA4pBYJikj6bzLLW1q8varqcKXxFk_r4WRPHf4bjKA0nTC9CIU27BCxKgJdLTuenuV4SjQvf0p1PTH1mxlkcVLwDxKwUQ1NHTENw0s44aWemLj7tLnRrVO6khFaBqUuovDVoCamZrYj0wfKqOnZiEX1vwgaS3TVSd581__ZePu_w5ht1dAgj9bzF5T2JubY8_GnGg-RdoiV-tmFthCfqvMo7NwoRax64xT5fjPb1Vx1rUPueyRL0UxxMVegkK_uWCsC1XyEJ8SJT77jZQqqaCc-n0nq8Z2EK6Yflxz3RtHGCQT4YnKGJXrO6SEuX7eNCO5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ViJvvab1nYl9X2z4405-pKRDOiF07_pCVlbqW0K1aCVS_VD0S0DJBWOCkF4qcesTULhSaWgfY8-pHm2j3En4vmqMBmHt-BYxROIuLCCAd8AtXSZNujgH6y8d_prKkQDXbM769jPOL1Seuvw8zhAV-o2ib3TPUGvKuIAh75DkQMgdN9egjL5QesTjpobrn1QZFT43ynszbILX-B7WEWsqcP3DdaqqnIpwzhOjgb8PCDsT0nye6exIPxhv4Z8KdhpdeI4OgP7e6dEcO6dmkuip1xVyjxT8M44h8COxumUNSJQX0rTayRJjyQqJYtk01M2Fj0oYM3STwCvHFHsSGjt9_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعتی پیش بورس آمریکا و بازار کریپتو به صورت غیرطبیعی با ریزش شدیدی رو به رو شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/122880" target="_blank">📅 20:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کانال ۱۴ عبری: برآوردهایی در اسرائیل وجود دارد که توافق با ایران تقریباً به طور حتم لبنان را نیز در بر خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122879" target="_blank">📅 20:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: آمریکا به اسرائیل نسبت به حمله به هر شکل به بیروت هشدار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122878" target="_blank">📅 20:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خوش آمد میگم به رفقایی که تازه وصل شدن</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/122877" target="_blank">📅 20:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
گویا اینترنت ایرانسل هم درست شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122876" target="_blank">📅 20:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
گویا اینترنت ایرانسل هم درست شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122875" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
دفتر امیری قطر: امیر قطر در تماس با رئیس‌جمهور ایران درباره تلاش‌ها برای کاهش تنش و حفظ امنیت منطقه گفت‌وگو کرد
🔴
امیر قطر بر لزوم دور نگه داشتن منطقه از پیامدهای تنش و اهمیت راهکارهای مسالمت‌آمیز تأکید کرد.
🔴
امیر قطر بر موضع ثابت خود مبنی بر اولویت دادن به راهکارهای سیاسی و دیپلماتیک تأکید نمود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/122874" target="_blank">📅 20:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
معاون وزیر ارتباطات: سيستم عامل، مرورگر، آنتی‌ویروس، اپلیکیشن‌های بانکی و ابزارهای امنیتی خود را بروزرسانی کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122873" target="_blank">📅 20:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک منبع دیپلماتیک به الحدث گفت:
ایران در طول دوره مذاکرات خواستار آزادسازی دارایی‌های مسدود شده خود که حدود ۲۴ میلیارد دلار تخمین زده می‌شود، شد.
🔴
ایران اصرار داشت که نیمی دیگر از دارایی‌های مسدود شده خود را ظرف ۶۰ روز دریافت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122872" target="_blank">📅 20:23 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6175563a.mp4?token=R6WqHb5BsduS3onfjN9vd0JZSk3ymDqCznNtF_5T1ibI9_VkLG2TYx8YuKAR7BGDbYwtC01YjhA4-n8ckadZ2MWoyYYvZd3WTaS234jWxs6yQdu91OEF555u2Xw3ktEcCgujEIZ4r9zF5KfYTaK-cQKZqHOOtJhqsvimzK8MpcVp_tRAJ0d1BROFImBGtnT9c7wsCMXzdfcerLjYhjT1R33me8D7M4y62nYu404hXrX1y2nurFY-q08SE6RY3rWCLt2hCIo_zjX9kPpQ0extk0Snh80YcAEZrgfk_ZlpENsw42MS2ybnOYkl9MahP42Mngs0LhpazDFMcbXDX5_B5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6175563a.mp4?token=R6WqHb5BsduS3onfjN9vd0JZSk3ymDqCznNtF_5T1ibI9_VkLG2TYx8YuKAR7BGDbYwtC01YjhA4-n8ckadZ2MWoyYYvZd3WTaS234jWxs6yQdu91OEF555u2Xw3ktEcCgujEIZ4r9zF5KfYTaK-cQKZqHOOtJhqsvimzK8MpcVp_tRAJ0d1BROFImBGtnT9c7wsCMXzdfcerLjYhjT1R33me8D7M4y62nYu404hXrX1y2nurFY-q08SE6RY3rWCLt2hCIo_zjX9kPpQ0extk0Snh80YcAEZrgfk_ZlpENsw42MS2ybnOYkl9MahP42Mngs0LhpazDFMcbXDX5_B5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما عملیات خود را در لبنان تشدید می‌کنیم. نیروهای دفاعی اسرائیل با نیروهای زمینی قابل توجهی فعالیت می‌کنند و موقعیت‌های استراتژیک را تأمین می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122871" target="_blank">📅 20:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsKJVh1zd24r3NhF9Nhyuw6Vd-JRaK5BN_F5EdzSHne2UbWJOTOKClbvtOt_nKHp-ZVpI8cE4xXIPN4c64JFCyYynmKl_qo37hl1w_qUay3sxl1GsrtLpgNsPLqCxwhP5Ev7yXMvHi5SjIdIkHPX9d8OJQdiU6cpkIp1e0B9wbA1yN6_o4u24qTgPsQ1Ao-E_y4_Mq4zCEAKiJ_mRlFmyvNBEKpPCXbaAESLPoRhfYo5OyERKRihGPrg4cZqc2EviQRwY88RycnG-m_k8UwFWGnpYfIWHeti5VxL9A3JB9BonYF0XK2KMyiZ67hdyJTglVJOPxuv3b9ayr69xhoD4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق Truth Social:
تازه معاینه ۶ ماهه‌ام را در مرکز پزشکی نظامی والتر رید تمام کردم. همه چیز کاملاً عالی بود.
🔴
از پزشکان و کارکنان عالی تشکر می‌کنم! به سمت کاخ سفید برمی‌گردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/alonews/122870" target="_blank">📅 20:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKSJaUBTPxg2kc-MuodO3QEie6Whs7fy1S9lQdJ8qIAqJ0DCIfUSkltVeIcX4Dt5gdsbCwFoZ1rdsiMBXVNkTP75ZJRCx1PTFG3A7VAzC44mvC5XW7mG_2-u2rbRW9rct-w8svRPLMD_F9hd8BzwNLC_eJ8N9SzYP1aJ55bFbD5rNki4Jsx7tuEF78QmNTsjjE-Rhp4tG2axwGDnEo3gOqlWaOlHCSNXtZcLgS193GxW78TLgexeVMzD4MKaqH1Jdw6qZk6V1n7ZKlMGT6OOmKYjdxOrbs48cAvIuSHT9Fmr3EywZkraoaQY8ubhpZwJxQOcUPwNjKSmekExBRbrrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام : پروژه «آزادی» از سر گرفته نشده و نیروهای آمریکا فعلاً هیچ کشتی تجاری‌ای رو از تنگه هرمز اسکورت نمی‌کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/alonews/122869" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
الجزیره به نقل از یک مقام آمریکایی:
گزارش‌ها درباره ازسرگیری اسکورت کشتی‌های تجاری در تنگه هرمز توسط نیروهای آمریکایی دقیق نیست
🔴
نیروهای آمریکایی در حال حاضر با محموله‌های دریایی تجاری در تنگه هرمز همراهی نمی‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/alonews/122868" target="_blank">📅 20:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122867" target="_blank">📅 19:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
واکنش سخنگوی دولت به اتصال اینترنت بین‌الملل
🔴
تفاوت نگاه‌ها، در بزنگاه تصمیم‌ها روشن‌تر از همیشه دیده می‌شود.
🔴
با دستور رئیس‌جمهور محترم، روند بازگشایی و تسهیل دسترسی به اینترنت آغاز شد؛ اقدامی در جهت پاسخ به مطالبات مردم، حمایت از کسب‌وکارهای دیجیتال و توسعه خدمات هوشمند؛ مسیری که دولت چهاردهم از ابتدا بر آن تأکید داشته و دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122866" target="_blank">📅 19:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
رابرت اف کندی، وزیر بهداشت آمریکا، ویدیویی تو اینستاگرام منتشر کرده که توش با دست خالی دو
مار سیاه
رو می‌گیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/alonews/122865" target="_blank">📅 19:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122864">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/594bc11e42.mp4?token=cZKGJnvVGh39al0mXI4xIgvKnMf6c2Cx9dxpJntUx9FBPKYIAWoCedZK3OhhtZIv4jyFhh-kScXDkEgfFI7so3cb46zPZgdzsarNC8Ko6L-Wn98hUZf1dh0Keuh01DPJCdmzVzRLn_W3deDTnoogxwUQWEHAg0ym762JN_EfqYdZJ0mCX9G0KdfndeHt8n_Lxmt0_KCNuoVtLqSLGeqcozM6a9ZDd44XQLOxaz_ryfsLbiw5HOmDS6R0qK31pBbQfdMmUsYHCRmlOnIMOM_sxhH8F_9HAbGBbUIXwi3ALeNOxR311Ib4Gg7mF8LitiYC_-ApSnQNwpp3RsPSWGxqEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/594bc11e42.mp4?token=cZKGJnvVGh39al0mXI4xIgvKnMf6c2Cx9dxpJntUx9FBPKYIAWoCedZK3OhhtZIv4jyFhh-kScXDkEgfFI7so3cb46zPZgdzsarNC8Ko6L-Wn98hUZf1dh0Keuh01DPJCdmzVzRLn_W3deDTnoogxwUQWEHAg0ym762JN_EfqYdZJ0mCX9G0KdfndeHt8n_Lxmt0_KCNuoVtLqSLGeqcozM6a9ZDd44XQLOxaz_ryfsLbiw5HOmDS6R0qK31pBbQfdMmUsYHCRmlOnIMOM_sxhH8F_9HAbGBbUIXwi3ALeNOxR311Ib4Gg7mF8LitiYC_-ApSnQNwpp3RsPSWGxqEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحشت در فرودگاه بین‌المللی کمپگودا؛ خروج اضطراری مسافران هواپیما
🔴
پس از آنکه مشاهده دود در هواپیمای ایندیگو در هند، وحشت برای مدتی کوتاه فرودگاه بین‌المللی کمپگودا در بنگلور را فرا گرفت.
🔴
مسافران هواپیمای شرکت ایندیگو بلافاصله به صورت اضطراری از هواپیما خارج شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122864" target="_blank">📅 19:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122863">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری / سی بی اس: دولت قطر گزارش ارائه میلیاردها دلار به ایران برای تثبیت توافق صلح را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122863" target="_blank">📅 19:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122861">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BVwoMwef1H-JqMxoiw_-8POap7h99koIHqKMk_OBUy6KyKb_VlfLBEHPWmhYXq_kw6psnkyokNA96L_LH5e9VWRECwOtMRyKFoRFhs7gQFgmW-8q9xPwSUoHC5PIc1YnWyGUTfR5cUHAkFZQWS_FUiEsXfM9g_z1_A9kGIheiSE5OPxd7f1kB9Jt627VfkqD6SqyCIcBtrEs5PCGVf-VpTQUJF8OlO8b-uoU5KqoqzUN_scbNHj4oSjDaCi9zOmCyKU1LV-kNCQySPkPtWhyTDCas2iYVCrwNvn7CgQFjWP0pXkjaxsJAurR1M8GXkBYoofQ7P2DSDEaN7iYWVBuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dFzsTJx9tskL7-Mu0NhpaXOJ0dwBqApstHNopckK02NKNyMfl2noS-rtbeVEwYS_tWyeXXFb4c1VDE60-iInY7vUqNEZAsSeZ4tlED2FQV9q6sm5vYitv-WLbcs3E1Zf833eWQnA_WJvs2KJIHA_AtXl5O_dpj9GPYsh4aZgr7QNgu-KJ85qwEnR7Ul74tG3oFKDMFpwZyzTL7gCeYstkYBm6qcTAB0CZC01q2mtjbF33myCfbqxHP5nXzeeqSlPNuiw16au-NSflKx6ToEk54BNju35CmpY-o51-C60e5R_BDjyOdb_JtLKjHxQM9C_JcAxlOTGd812LaWrjoSmYw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی شهرهای سُهمور و مچغره در دره بقاع شرقی لبنان را هدف قرار دادند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122861" target="_blank">📅 19:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122860">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سنتکام : تا به امروز، مسیر ۱۰۸ کشتی تجاری رو تغییر دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122860" target="_blank">📅 19:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122859">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d3f034504.mp4?token=pLjvgNl-XR7i6myaWzQznOOZzBGp6IVwxQ6Zj3FmCnNdrgmQqCzcYkUpeIO0dLGLbMn3vb2CZI15bwwp7KyfwBhsml_bllemZLdMo5YpV4vIsaZxzMIxuKd3kkBTJhKFJ4SsBalOhwpR3F-SynHOpwDVeydttBeDdrFUwUBW30zdqBS2EKF-w7lvbSEFVB19iXXhbDi1xKzyAhsXUMz56hUMnxUVMncMBS5DOhAjRVzeM12qYKuKAhDqUh7TTlSA0CGhSEadxsEhdYwS_GBHQulHpc6K5d2Vjos8I-bZqiKelPvoM1W-ef_nnnVzL6_-rf9UCCUjOrF7CUixnmJ2Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d3f034504.mp4?token=pLjvgNl-XR7i6myaWzQznOOZzBGp6IVwxQ6Zj3FmCnNdrgmQqCzcYkUpeIO0dLGLbMn3vb2CZI15bwwp7KyfwBhsml_bllemZLdMo5YpV4vIsaZxzMIxuKd3kkBTJhKFJ4SsBalOhwpR3F-SynHOpwDVeydttBeDdrFUwUBW30zdqBS2EKF-w7lvbSEFVB19iXXhbDi1xKzyAhsXUMz56hUMnxUVMncMBS5DOhAjRVzeM12qYKuKAhDqUh7TTlSA0CGhSEadxsEhdYwS_GBHQulHpc6K5d2Vjos8I-bZqiKelPvoM1W-ef_nnnVzL6_-rf9UCCUjOrF7CUixnmJ2Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عزیمت ترامپ از کاخ سفید به بیمارستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122859" target="_blank">📅 19:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122858">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
شبکه آمریکایی سی ان در گزارشی نوشت، ذخایر اورانیوم و غنی‌سازی ایران، دارایی‌های مسدود شده و جنگ در لبنان موضوعات اصلی هستند که هرگونه توافق یا عدم توافق میان تهران و واشنگتن را شکل می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122858" target="_blank">📅 19:19 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122857">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با رئیس‌جمهور مصر: رویکرد ما همگرایی با کشورهای منطقه است / اقدامات ایران در چارچوب دفاع مشروع بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122857" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122856">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پزشکیان در گفت‌وگو با امیر قطر: ایران برای دستیابی به «چارچوب عزتمندانه» پایان جنگ و تنش در منطقه آمادگی دارد / شیخ تمیم: قطر از هیچ تلاشی برای صلح و ثبات فروگذار نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122856" target="_blank">📅 19:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122855">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
منابع عبری: در ساعات اخیر نتانیاهو مشاوره‌ای امنیتی در مورد وضعیت در جبهه های لبنان و ایران با رئیس ستاد ارتش اسرائیل، وزیر دفاع و دیگر سران نظامی ارتش اسرائیل برگزار کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/alonews/122855" target="_blank">📅 19:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122854">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادعای شبکه عبری کان: دیوید زینی رئیس شین‌بت (سازمان امنیت داخلی اسرائیل)، به تازگی از امارات متحده عربی بازدید کرده و با محمد دحلان یکی از مقامات سابق ارشد فتح و تشکیلات خودگردان فلسطین و مشاور امارات دیدار کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122854" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122853">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت قطع ارتباطات: اینترنت همراه، امروز (سه‌شنبه ۵ خرداد) وصل می‌شود / بازگشایی کامل به وضعیت پیش از دی‌۱۴۰۴ تا فردا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122853" target="_blank">📅 18:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122852">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
یک مقام آمریکایی به اورشلیم پست: نیروهای آمریکایی در حال حاضر کشتی‌های تجاری را از طریق تنگه هرمز اسکورت نمی‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122852" target="_blank">📅 18:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122851">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کلش ریپورت: نیروهای دفاعی اسرائیل حمله زمینی فراتر از منطقه بافر «خط زرد» که خودشان اعلام کرده‌اند را در جنوب لبنان آغاز کرده‌اند
🔴
این پیشروی به سمت سایت‌های پرتاب پهپاد فیبر نوری حزب‌الله است که در حال کشتن و زخمی کردن سربازان اسرائیلی در داخل این منطقه بوده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122851" target="_blank">📅 18:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122850">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
🔴
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122850" target="_blank">📅 18:47 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122849">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شرکت مخابرات: اتصال کامل اینترنت بین‌الملل مشترکان برقرار شد
🔴
کاربران سرویس‌های پهن‌باند ثابت شامل FTTH، VDSL و ADSL هم‌اکنون بدون محدودیت به شبکهٔ جهانی اینترنت متصل هستند و امکان استفاده کامل از وب‌سایت‌ها و خدمات بین‌المللی برای آن‌ها فراهم شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122849" target="_blank">📅 18:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122848">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نت بلاکس: سطح اینترنت به ۳۵ درصد رسیده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122848" target="_blank">📅 18:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122847">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/150e37cfe6.mp4?token=p4KwQQ_-YETEnMbjQefpOcUcBPyzLpCLtslugP9ptjPgj0951JSos-kBjCpGzW5OZOgMXIsVJ4pn4wPlZ7f-AGg9mHrIuTQsd9PGUbIzztzvSX0g1tZ-TqEgmf0WKDXV4dXKhri8GmDNBWii2qbwM1lT_6nJLcLn__W9ykThay1ERD3-O_ynPepu212VLknsV9qDxaqbpxlCK38vGQ6A1-aO6u-fYXaUb7_hDBlNyNS_9NkntbKMd4JR4oX-tw0WIH4Zkgtfkyh2ob8Tea0sglHQmsVv8llmZnel3h37A5i0rWzI276ex1EIbmEYOAasusqukZL76KuP83Oi5t7r_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/150e37cfe6.mp4?token=p4KwQQ_-YETEnMbjQefpOcUcBPyzLpCLtslugP9ptjPgj0951JSos-kBjCpGzW5OZOgMXIsVJ4pn4wPlZ7f-AGg9mHrIuTQsd9PGUbIzztzvSX0g1tZ-TqEgmf0WKDXV4dXKhri8GmDNBWii2qbwM1lT_6nJLcLn__W9ykThay1ERD3-O_ynPepu212VLknsV9qDxaqbpxlCK38vGQ6A1-aO6u-fYXaUb7_hDBlNyNS_9NkntbKMd4JR4oX-tw0WIH4Zkgtfkyh2ob8Tea0sglHQmsVv8llmZnel3h37A5i0rWzI276ex1EIbmEYOAasusqukZL76KuP83Oi5t7r_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله های شدید ارتش اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122847" target="_blank">📅 18:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122846">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHc9GNfJEgo5LX6o37SYCSsRsXu_bXgAcPbgHst6hxDqVuLLOCu7v8LVGd46AXLgU0HXbo5j0qpTzhGK-GHBGuaZCDBfjWnw4lW6SiD26zGsfeDycASiOrZeWBW_X0iT1NALgd0Ib_an_FT9GMjOulfkKDIyrBq7mqu18yzUI41EX5FK9qoGLueCqBtIZmnB1mToMbSE9CM_4LI3wd1EO20-lCzX3xLghMLAyUWtQLnt0eNk1e2bcUHeWt25wjP1HF2mBXPl7t4MBlYHFBSHsDpfY031V7GEJp1DhnjB_rDlNrEXDvXcuBwWR5La6Gv6ws6QaqSOjcdRgy660I9gVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هلیکوپتر آپاچی AH-64E ارتش ایالات متحده در ۱۸ مه در یک شالیزار نزدیک پیونگ‌تک، کره جنوبی فرود احتیاطی انجام داد.
🔴
هواپیما پس از اینکه خدمه در حین پرواز مشکلی احتمالی در موتور تشخیص داد، فرود آمد. هر دو خلبان سالم بودند و هلیکوپتر آسیبی ندید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122846" target="_blank">📅 18:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122845">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر امور خارجه پاکستان: طولانی شدن درگیری در خاورمیانه به نفع هیچ‌کس نیست
🔴
جهان نظاره‌گر پایان بحران در خاورمیانه است و ما باید موفق شویم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/122845" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122844">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
🔴
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122844" target="_blank">📅 18:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122843">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
مارکو روبیو وزیرخارجه ترامپ ادعا کرد ممکن است چند روز طول بکشد تا جزئیات توافق احتمالی با ایران نهایی شود و افزود که مذاکرات به پیش‌نویس اولیه نزدیک است
🔴
او گفت که دونالد ترامپ، رئیس‌جمهور آمریکا، اخیراً تماس‌های منطقه‌ای برای پایان دادن به درگیری برقرار کرده است، اما تأکید کرد که آمریکا فقط "توافق خوب" را می‌پذیرد، وگرنه هیچ توافقی نخواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122843" target="_blank">📅 18:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122842">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qekf4m8pFfPf6XOd7HKaLyzu6EqwCzEBR5glcIu7rga2y6GSUeaiAYlU_YHmpA5y5LwIXDeq1RO2kyz1HX6BBJDhUz6qcheJhR65LaZTIeeg_U7j7Zudxxltd58--ronwCc8cwo_cebjj6Va7rnMNVYNbK03o6KTnhjMetQUCmuWzkafPedvLlR_gMvLV8z20HRkNukGZbcbmmMsYvsp-2DJABwnKyPUQr4zBtuZHiBpopIfMm-drCe7BhfFibc-S5ImuHeF5wKPF7C7OOPfObm-AG_GHtMX5rK261_fad3lUXC0riHsMD0cJAJ66KTtxAmfeFA3qsY-Ra1vgFAUig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون رئیس شورای امنیت روسیه، دیمیتری مدودف: اتحادیه اروپا اعلام کرده است که حضور دیپلماتیک خود در کیف را بدون تغییر حفظ خواهد کرد، علیرغم هشدارهای روسیه.
🔴
خب، ظاهراً آنها دیپلمات‌های اضافی دارند و نیاز به کاهش تعداد دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122842" target="_blank">📅 18:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122841">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d-eOBOgB7XMFJVU1M4TQD8FdfN1FCHeyJslsJH3rkuTA3JvgAM6dJ8vyde1ctRLV1a6wEGe63PtPKg612GLEpaujtNxdyHh5IksejWrRdooDFsnbYfhYQkTs6LlauIMQ1qvW47UL4TnocOtvZ5NmLIRWKPOcvnZx679Y0GGFL56x7OYkigdA5aX_wH-yn2Us4SxfcZWyCQ2DbDIy6JsTFUPNaFqE-pTSL0jIHm07mQvLWCgNbZg7URUjysUjZM7tZCP6WAjQmcaKdmX_cddjykNg2GHipdCuXONK5wKyMT5yIQN0WVTwBn5v6RBhQ6K5-r0Q3PMdMYqBkyyDFY0SaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به دنبال اختلال در مذاکرات، بار دیگر صعودی شد و از ۱۰۰ دلار گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/alonews/122841" target="_blank">📅 18:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122840">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
رئیس‌جمهور ترکیه، اردوغان، با رئیس‌جمهور ایران، مسعود پزشکیان، در مورد روابط دوجانبه و مسائل در حال توسعه منطقه‌ای تماس تلفنی برقرار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122840" target="_blank">📅 18:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122839">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وال استریت ژورنال: به گفته مقامات نظامی آمریکا، نیروی دریایی ایالات متحده کمک به عبور کشتی‌ها از تنگه هرمز را دوباره آغاز کرده است.
🔴
این مقامات به وال‌استریت ژورنال گفتند که یک ابرنفتکش یونانی حامل دو میلیون بشکه نفت خام، هنگام عبور از این آبراه در سواحل عمان، توسط نیروی دریایی آمریکا هدایت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122839" target="_blank">📅 18:12 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122838">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
طبق گزارش نیویورک پست، انتظار می‌رود دونالد ترامپ فردا برای یک جلسه نادر کابینه به کمپ دیوید سفر کند، زیرا مذاکرات با ایران به مرحله‌ای حساس نزدیک شده است
🔴
انتظار می‌رود تمام اعضای کابینه، از جمله تولسی گابارد، مدیر خروجی اطلاعات ملی، در این جلسه در محل استراحت ریاست‌جمهوری حضور داشته باشند، هرچند ممکن است به دلیل شرایط جوی شدید در منطقه واشنگتن، مکان جلسه تغییر کند.
🔴
انتظار می‌رود بحث‌ها بر روی ایران، دستاوردهای اخیر دولت در زمینه اقتصاد، کسب‌وکارهای کوچک، تلاش‌های ضد تقلب و تحولات سیاست خارجی متمرکز باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122838" target="_blank">📅 18:08 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122837">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28e4bed3b5.mp4?token=dKPRpkwF8lMlUA1TvxtlocAAJUzA4EbLImcXKs4Yqj4hh9kIbzjfNl6fZk98mQ41Rr0Ac4bVCjpFDSizpf_le1Oii46vDYDh2knIywKIigiTsV2plDKNSXxcDauV94XAbRd3UagdCebUpvXiIych6vheSoxKshyCmjW_vITJQYv1iXp3FtwkzjQByTs61dkeYtNa40OH5F0Ju6Jl8EpSYdfNI1NLxnxu2UDnw53v4m2HZ9NsQ9nBk8mf_RzM6pLg0_4Yd_NVi4z04Zrb4InGxdTOJzzNiFkWe-bUCmAHgkoAeIRbuJ5xfP8FwhgzUESMcTvjgJCQAw5r9LhcIJdK3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28e4bed3b5.mp4?token=dKPRpkwF8lMlUA1TvxtlocAAJUzA4EbLImcXKs4Yqj4hh9kIbzjfNl6fZk98mQ41Rr0Ac4bVCjpFDSizpf_le1Oii46vDYDh2knIywKIigiTsV2plDKNSXxcDauV94XAbRd3UagdCebUpvXiIych6vheSoxKshyCmjW_vITJQYv1iXp3FtwkzjQByTs61dkeYtNa40OH5F0Ju6Jl8EpSYdfNI1NLxnxu2UDnw53v4m2HZ9NsQ9nBk8mf_RzM6pLg0_4Yd_NVi4z04Zrb4InGxdTOJzzNiFkWe-bUCmAHgkoAeIRbuJ5xfP8FwhgzUESMcTvjgJCQAw5r9LhcIJdK3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حمله‌ای هوایی به سد قراون در دره بقاع جنوبی لبنان انجام دادند.
🔴
سد قراون بزرگترین سد این کشور است و به عنوان منبع اصلی تولید برق آبی، آبیاری و آب آشامیدنی عمل می‌کند و ظرفیت تولید برق آن حدود ۱۹۰ مگاوات است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122837" target="_blank">📅 18:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122836">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69262d7ad7.mp4?token=k3Matu0-v4LPU8yTRSSW7W0hei4k7dVSL9KvE0gNnyGP5-9NC_dnjCUmtLctu0K3SRySwqd_zbL3dGv1i2uneOG6UCgU7WmyhE9AgAYvsfq_6LGP2mLORg7rJdGB7roIteU8ahA7yqGo-cFR_xuyJu6oUEyLh4NrrKwlwrx5jiu5LYKFJFMuM8pwrLA2YD80uXZ5S0Is4p_7Qim63KD94HyKNSI-j8ICyVdgeFvqTxZ67fhqg5KfgY1cAjfuhT-nzSlXN9Npo8NGyseCY87n0Rnbi4WRfBWQyT8xldtB1kTHP-YLXNJvTgK1sijfUr9AEv2VJTiV_oe5OnBSU5DSOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69262d7ad7.mp4?token=k3Matu0-v4LPU8yTRSSW7W0hei4k7dVSL9KvE0gNnyGP5-9NC_dnjCUmtLctu0K3SRySwqd_zbL3dGv1i2uneOG6UCgU7WmyhE9AgAYvsfq_6LGP2mLORg7rJdGB7roIteU8ahA7yqGo-cFR_xuyJu6oUEyLh4NrrKwlwrx5jiu5LYKFJFMuM8pwrLA2YD80uXZ5S0Is4p_7Qim63KD94HyKNSI-j8ICyVdgeFvqTxZ67fhqg5KfgY1cAjfuhT-nzSlXN9Npo8NGyseCY87n0Rnbi4WRfBWQyT8xldtB1kTHP-YLXNJvTgK1sijfUr9AEv2VJTiV_oe5OnBSU5DSOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ملونی نخست‌وزیر ایتالیا : اگر نمی‌دانید چگونه از خود دفاع کنید و از کسی دیگر می‌خواهید امنیت شما را تضمین کند، بابت آن در قبال خودمختاری، حاکمیت و توانایی دفاع از منافع ملی خودتان هزینه پرداخت خواهید کرد. هزینه دفاع، قیمت آزادی است و من می‌خواهم ایتالیا یک ملت آزاد باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122836" target="_blank">📅 17:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122835">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb7b04a0e5.mp4?token=Wqr4EjzK8kr2Nr3gND-e0tIpMlQFV-cIgOcvVAtwvaIoX1XpmnNGTP8g7JdLv9VYOZu4qz2Vxi0ZMEOBRfAS4qbIXUcLmgf7CvwGey64cmV6WPDWpeAl6DKS_ddWruqpNO9qTf1XSQI2FI0JP9qc8XgSN4VTPYIUc-Ne46MAjMUgm_Mvc18aATd9eTq55d2zsjq9xQ-q0RQ-Ytm_-tyS0TyGYy0JYyOC0RbB0kCuh0VhJvsqmB_x5iXBWCghSC0bLbNpmGwwVOXG_6zgEusxWfi29sIFah7xJpXJGbOWZ0xwUnn06Ghq_yf8Z0fBdS5zmRFoZrtR-ryy7uqVlV3T5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb7b04a0e5.mp4?token=Wqr4EjzK8kr2Nr3gND-e0tIpMlQFV-cIgOcvVAtwvaIoX1XpmnNGTP8g7JdLv9VYOZu4qz2Vxi0ZMEOBRfAS4qbIXUcLmgf7CvwGey64cmV6WPDWpeAl6DKS_ddWruqpNO9qTf1XSQI2FI0JP9qc8XgSN4VTPYIUc-Ne46MAjMUgm_Mvc18aATd9eTq55d2zsjq9xQ-q0RQ-Ytm_-tyS0TyGYy0JYyOC0RbB0kCuh0VhJvsqmB_x5iXBWCghSC0bLbNpmGwwVOXG_6zgEusxWfi29sIFah7xJpXJGbOWZ0xwUnn06Ghq_yf8Z0fBdS5zmRFoZrtR-ryy7uqVlV3T5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روبیو داره برمی‌گرده به واشنگتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122835" target="_blank">📅 17:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122834">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
سی‌بی‌اس : ترامپ چهارشنبه جلسه کامل کابینه رو تو کمپ دیوید برگزار می‌کنه
🔴
پ.ن : کمپ دیوید محل جلسات استراتژیک محرمانه‌ست دور از واشنگتن هست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122834" target="_blank">📅 17:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122833">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزارت خارجه جمهوری اسلامی ایران حملات اخیر ایالات متحده در استان هرمزگان جنوبی را به عنوان «نقض فاحش» آتش‌بس محکوم کرد و هشدار داد که واشنگتن مسئولیت پیامدها را بر عهده خواهد داشت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122833" target="_blank">📅 17:46 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122832">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رئیس مجلس و رئیس هئئت مذاکره کننده کشورمان که دیروز در راس هیئتی برای رایزنی با مقامات قطری به این کشور سفر کرده بود ساعتی پیش به ایران بازگشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122832" target="_blank">📅 17:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122831">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
تماس تلفنی رؤسای جمهور مصر و ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122831" target="_blank">📅 17:42 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122830">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بررسی‌ها نشان می‌دهد از میان وب‌سایت‌های مهم، موارد زیر در دسترس قرار گرفته‌اند:
🔴
ویکی‌پدیا
🔴
اپ‌استور
🔴
پینترست (Pinterest)
🔴
کنوا (Canva)
🔴
نوشن (Notion)
🔴
تردز (Threads)
🔴
کال آو دیوتی (CallofDuty)
🔴
پابجی (Pubg)
🔴
یاهو
🔴
دراپ باکس
🔴
پلی استیشن
🔴
ایکس‌باکس
🔴
بازگشایی اینترنت به تدریج در حال انجام است. به همین علت ممکن است برخی از سرویس‌های بالا هنوز در دسترس گروهی از کاربران قرار نگرفته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122830" target="_blank">📅 17:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122829">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxfnBpxm_PySPASjdkf8D5bPNMzsyF-7EfmToW4B3OMCEDT9NW6HwpsLqaVg4_H5Tc5MGsbF2ZuE4CJ2vsao4BHleqCQoQroKLvBEWK97cWr8OND9ogjIHPhOc2jlevkZ8vo98YwgoF_njYkUHGZ1wNJUA3V3-LQ9_Ei4CLTaV25s_DMp_Q1jy1HUXPCHQAOK4IBmeHo-V1lpSqr9gqIiBoOGGnfYpaQShNRkQIUzSiQj6ldxbYqiO626wYkZ5duejDZwYOvTs-0Ujaf2PvoawA7kxNwc6RpGehmthtGTlcjHIcrzbBaAOUB7ck6kXXiUzlhsNVBmnUCqAWM8UGOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار در نزدیکی کشتی در سواحل عمان گزارش شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/122829" target="_blank">📅 17:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122828">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رسایی: آقا بازش نکنید
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122828" target="_blank">📅 17:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122827">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuyAhuudeKooChh7fDwLD3mrHhYytu9GMAFa9_cPV9hi98-H6gVO5tekN9xkbNc8OfYkJTaG2f0aPbsVEFGl8aVa2xWPttv0M7cU6A91XlE3b7HOCRpmmsAMsVCYifyyEJ5ppChe2cwpPj1PHqxXfnS4_dN9mPcW4lPu-RwJ6uFBkWn4z0K0MfZEpVIsPdDEx7zLrk-krbmQBy83hZVBy3g9yXW1BbHNOjNjS6frBgDwCUgLK6RmZ0ZiIbkyKE5AKhotTfZUlxszcyS96brY0tJgluAzELjm4EW5TOgzu3FRWca_LDdLIyAMWt3x-S3oCNIivpwyJGbFxwyyC-_L5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) در لبنان فراتر از خط زرد (خط توافق شده در قرارداد صلح سازمان ملل) عملیات زمینی را آغاز کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122827" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122826">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع آگاه نوشت: ارتش اسرائیل عملیات زمینی خود را در جنوب لبنان گسترش می‌دهد تا کسانی را که حملات پهپادی (FPV) انجام می‌دهند، عقب براند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/alonews/122826" target="_blank">📅 17:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122825">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
نیرو زمینی اسرائیل دستور تخلیه اجباری برای شهرهای مشغره و سحمر در دره بقاع شرقی لبنان صادر کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/alonews/122825" target="_blank">📅 17:25 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122824">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
طبق گزارش ها ایران ارتباطات رادیویی را در مناطق خاصی در داخل روسیه  و گرجستان  قطع کرد — و برخی از ارتباطات در ایران به دلایل نامعلومی قطع شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122824" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122821">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZbzHnh2PvACpaybWii7IsKeW4Kytwb4P88WcF4QtaghZNqwlsNUkv2aLFnomcCEM7Qn4mCBrz8kiLeVmrsKYbuyW15fu8X_U6-npLAYIxGcOCJGgdYCB1FculQhuusVS-jAt3MOOEZ_1EYlsZNJcZEqB-bmym95PnqHm43WbyOYCoG4ztjFMUN7BDi0LhseDyzQX5ek4b98zdMyNfquBrxVEw_ZpbMR5yp4pDi5S9utguoMLsMJjVyeLGeaogKNiJPZHyVowCF6UCX-aq2W2uNPzYWJkF2HtWX7KmvpPsA0S7Ci3y_zNdxt_1fcCrq1qepTisfharzyTmHXwPVv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9CYuNtUSxpJeY_V-lbmMPgYlqM1KTMoYtjPVqAu0Wn9_NQZPk7pBF5pweab84018qtFtQXIzEoBsAIBzU-5_tnI3m1QH_HynDo0vcRIVZ8kHTBpuyZjP3uPtK4jMjMdpZBBrMyPF5ecW0QAUkbC9xRlUP7xHxos6IbiAeW-IqOhhd5GtQJ5XI-tJI_VbVsz9QX0cqG_lczDphIq6-04n4RAL8TNqdCLVD-FcAQTzMRVklLQjoLocnAPbVg-kN7705AknvqJ9EsNvZVueli_BE5Bsa70BOZxfllo1kVWbhHdWwDkgiMwtLNtO2zWEquxca18yyDPzNkNmODXk6WP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tevxC8VM1DgNcnZEBLQ7sUNGEFcS6qqkXLjTma5rKRXPKSJgQHmQy9IWxXNouVqQj-25KmUgrzTapFrNmwDOMLvEdyBYWB5P6PGNuS7yMPQRvf-iGLIz-7nHI2k_ptxBzfQu7quWEGWFfFKl7T9llsOl72y24YeCeBxkLwlUsbotEpOgbHU0qVskMxea0wp3SxIVK_MK4ax5BwvmNbxPwzGwa1j4FvgZTOYwyTFWXtlqUtlaI3NMKMJtkPwPlGspR_Y3ZROZydv2fvWVG7ZKQjDzGB7jBDqZlZ-Wb0i_Iuz1RFWzzqT6c0m731kZG-oZJdbvSEJFv41KI4mldufdjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی حملات هوایی به کفرتبنت، خربت سلم و زوطر الغربیة در جنوب لبنان انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122821" target="_blank">📅 17:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122820">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
تسنیم : ترامپ به بیمارستان اعزام شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122820" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tre4t3CT3faIpr5gvAA0QbUzUOtzWpOiKdS82GQSV9vTyCeXxCPbeY3liYhM3hcsVz2U1jFnGNP5meBMeVgHzryS3BRpxupT8HHrKDntSgsAfNVSgwoW-10rpbL1ioZ-b3zpYEoC7nzPYt5TAGYTi3KZ37mApwdNF_9vGAwTZ4oPxigmovv4Zdbsr9QTuzgigu22QXygFnewcM4tPNGr8So5sy4t7WYp-xvb8CHz3DrBbRes7E9GT7Ir7iqMAqSpm9-6Ew6hZxUp0X0ezul_uzdIuP7Y2s8qKOGF-YZjrAU05qd-ULvKzkHLwDnQY9ElnIRu8nP3Fh7SGAIvaq5smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عارف: گام نخست دسترسی آزاد و ضابطه‌مند به فضای مجازی برداشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122819" target="_blank">📅 17:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122818">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkrlKLNJtMFP633NTumKVREVQ1MJpweXDNtmDK0VhtS77a7bQEAIVsZukzcpIBQ6iY89dcB7uN4l0p3mrvlu7rF53F5yKMeMcOqkM24BeogIWoKsJ7oOyR6iseIyO78vji6hVjmml9o2fFMVskjTK2FC2NXMEuklavF3bNPVybHPHRbepuNKqKKhL27Pv7pOxQAHfxmDWLVetfD9Tz1VPU9OHDVkr7qu359gAPjUjhRNQaZdMa4gOCURhIAoCXM81_gHiryH3tq7RXQhI7TxxfPl6sgY-ofugPXLg_t7TOUoIfg2hT_5ZP-C_bVhorWCFOlVWFAzDDmM03nXOyPYqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صحنه‌هایی از معرکه، جنوب لبنان، پس از حمله اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122818" target="_blank">📅 16:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122817">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
تسنیم : ترامپ به بیمارستان اعزام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122817" target="_blank">📅 16:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122816">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / گزارش ها از زلزله در مشهد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122816" target="_blank">📅 16:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122814">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KORMaq-gPVQ_5BRQiC-0hoKJwWlv-DjkoQ4_3H_9wKH00s4AvUIxO0-ZITWrMuy96Qcf3Fp7_bp8yV0vQxTwEVM4ApLaULVwzp6ZoH7LhNQIMVdT1VthqFiNeaoVjOWO6v72qWyzkpqmqKwIPEwrbE8RE9n34VBoe4CF40nxvd_zXf4CbjxARMJyAdeHP3OHl4CJHOq0c3phFKa2wTBbQjvmuU_M5KwocRXq6g_GFguyWksKU3AGq7w3Yxpsk-JTSW9Zc27YXG1bmdoYZAtm4XJ78iyMJNJyJsly7mh4dUgVyxElPAdRSRilCOoT_r6YOO7ZmXQgFA0HQeBKtQQ7UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R92ae5kgg9LvzN3n6AlrWRiDKJgJamAOsV6W0md_La_e5DD5DlhxqDRZ_rCJbdzeigqAod1Qj_2VNIT4X6-PtwOrcp3k31SsWFYBxwQDyXRoP3GnZX-ICKwlN3Si4oYscHybF1vLcZdhRKocK2RXP-ebVlUx7bUn9NUDqC3ttClxO79N-mOY3mawC6_NUBUYSdfwWGuzvvO9SLfX2CD-sebRgCUixjQyezEO7h2Of3aTUKB0lFQXKe-pb752zLJt-IBPu4aK6WKKE5aIlfCf02p1BmUeV--52kMuEnvjMNQ0bDtUd3JFdYE-RiAwZ08jLdtnpXAAV2_4ITUfJgCmtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
پست های جدید ترامپ در تروث سوشال
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122814" target="_blank">📅 16:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122813">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فعلا پروکسیا و یک سری VPN ها روی مخابرات،شاتل و بقیه مودم ها وصل شدند،نت موبایل هنوز باز نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122813" target="_blank">📅 16:43 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122812">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcnxqjrjAVjutfzSzVvMITWypNAzbiDmDV_nKSeJhlmTatdY-81AlqrKeRF16KVDXMVMU-euwIM1CtCoa0L0eL25-rPiQZ3iRSsTHLYlzsgvoBg9wQtCQH4A3hw7SiOwZA23Y3WWVQEKgssJhe02bV0tPcOs1W3wzC-Cgg0FK-QRZWPf2NpIt8w-JCmWGK27vvYrNELrV-f0GCDpPxCTKDolLOacC-TBR0w0_d3k73X-tszSyXG9Rtp12jQ2dYIvrPTxw3eNV9tCNvwZKY7HQBTorYgYDeEXz3MIEvTlaZfs0hBZwH0zpcqhLlQ_3yXurxvOdAkAd2Ta-bfigyu4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت کسب و کارهای اینترنتی بعد وصل شدن اینترنت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122812" target="_blank">📅 16:41 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122811">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تکلیف اونایی که پرو خریدن چی میشه؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122811" target="_blank">📅 16:38 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122810">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lygyh9BsazoL1WT1RfHNqLoYLEkR7um9mAG8Bf0lWZh9dfmlVQBRj2k007QIB6OPDztlSmMzFeUPYrZCPOgmKKQZnEPCtMlj8WCm1smmEAdBEj_-Ft2cFEAV_HjEMTDtkpHgH2nzJtn1FWu7S1ex90tXUAOIwySoYcIETQ_KiObLSZ2HsWr91yT7Hop2Q1lm7XfjbaRdVkSjnqHsX1_iMqOIfRMdwFcaugLuDqkZ9uDy028gjRsHBTi5PJukzLSff2FTkQKaZmDfBH9Dl-j6GthfiGPuzyRXjE5PBHEClbv3drdmD7r_AHTo-oIcADdDeJudz_fxGM6vL_ltlEzNHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از ۸۸ روز و حدود ۲۰۹۳ ساعت قطعی و انزوای شدید از اینترنت جهانی، اتصال اینترنت تو ایران تا حدی برگشته
- ولی هنوز معلوم نیست این وضعیت پایدار بمونه یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122810" target="_blank">📅 16:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122809">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
ادعای وزیر دارایی اسرائیل: ما در حال تغییر خاورمیانه هستیم
🔴
ایران امروز بسیار ضعیف‌تر است، حتی اگر هنوز فرو نپاشیده باشد
🔴
این هم هدفی است که با کمک خدا به آن خواهیم رسید.
🔴
نگاهی به وضعیت غزه بیندازید. نگاهی به وضعیت لبنان بیندازید.
🔴
ما کاملاً معادلات را تغییر می‌دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122809" target="_blank">📅 16:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122808">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8z2_gqtp_qSbzrnufmU009Q-KXfFA43CPPWI52V35LTVcxY2YhtOHaYGAveCJcDxD7tDZszcB0LZ2aRC_6t1LMqVgIvUwIG2txhDTyMObeWnGBjtOyN46q5sogoluH0Sd_rm0luoMvt9uIHIfSiHrst2PBHlHleE2W97NBoPZwF_BihrpGmT8NxbACh7ef5FZ-ivDczan-SzTbAjJ1-xHhR_UwX6dEYVH59KBfGUl0AUJtR0wW73x4C3n4A4oPxxSN1CRvAXL4zQON5IOKG_AjaPNWZpjADAf49LYCW1BL89nP9c3aAJXXQWBMkukUfnY13Db2KRRxlCgR7N_ZWDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال:
قالیباف برای گفتگو درباره پایان جنگ برای دومین روز متوالی در قطر مانده
🔴
وال استریت ژورنال مدعی شد مقامات ایرانی و میانجی‌گران عرب گفتند: «محمدباقر قالیباف» برای دومین روز متوالی در قطر مانده است تا درباره توافق پایان جنگ گفتگو کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122808" target="_blank">📅 16:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122807">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / گزارش ها از زلزله در مشهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122807" target="_blank">📅 16:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ادعای وال استریت ژورنال:
بر اساس گفته افراد مطلع از موضوع،
اسرائیل از آمریکا می‌خواهد که آزادی عمل این [رژیم] در لبنان را به عنوان بخشی از توافق صلح پیشنهادی با ایران بگنجاند.
🔴
این تلاش، می‌تواند به یک نقطه اختلاف دیگر در مذاکراتی تبدیل شود که ایران اصرار دارد هر آتش‌بسی باید شامل پایان جنگ در لبنان نیز باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122805" target="_blank">📅 16:20 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سناتور تام کاتن: رژیم ایران تا ۹۰درصد تغییر پیدا کرده و این یک موفقیت است
🔴
پ.ن:حتی رژیم غذایی پزشکیانم عوض نشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122804" target="_blank">📅 16:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اینترنت هم برمیگرده اما اون داغ تا ابد میمونه</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/alonews/122803" target="_blank">📅 16:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKZyuBA64_1iR1mmgbHFZ6YL4A3sQIHHw6u6p0gh2WqJapYjG5C5zKmiHf1BGQ_I1TxCYyeQrFyBOCV1YgJvd9oc5XQkAobJKnVY2QADHPAaR_1pmLCBxn8qiYG8XCVlXulnchTzt7yvC03X7YSC-YEPVyT4fpTyG3gZyTsRQbNFsFIOCR59lwAsAfm0gzWyZ0eLo8Qo8OP6wQRY0GNNv8V5XxrTWWPdgP3yRwPS8Zg1O3qN1vDtf42_fFLqwgENitqCj_-ZouenSYvRuDIuJRtIHoe2C059PY6S1OWDOnfR5g5cYe34g-DuRcVX9YOWasisrPpOK62XUnkkS8a0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت دیتاسنترها نیز در حال بازگشایی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122802" target="_blank">📅 16:11 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ccc8c541c.mp4?token=dj3bN0_SDbWS3rcRTP5mAEjtXmZ_jKFUbCW-a1SM4zlXOcaY_tyPnX6YzbCdoYR8WbPy8B5gyvnYUS_i4JkMPJ__QNHun5KM26eXiow-t7nBaTdNQME8J2ODcxiM-KJ7nDA1W1dK5r6qHpN1Bikg-co0kjZnNGjFS_eMZPcfc5uFTwk4u-uHH_B23tBoGwX8o1MVVllz9KIWdZY4js4ekWI5Uy5MoKKoMZ-IleVt86MplR-wO3peMO65rs3RMZaQn7TYZYi6jH4bCeq8KgUaa1exzdXcuYJFY-nQEoUxVg9PooYiqnI3191bLHlhN83l7wqUum0MgN0PtPY8Ry8OPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ccc8c541c.mp4?token=dj3bN0_SDbWS3rcRTP5mAEjtXmZ_jKFUbCW-a1SM4zlXOcaY_tyPnX6YzbCdoYR8WbPy8B5gyvnYUS_i4JkMPJ__QNHun5KM26eXiow-t7nBaTdNQME8J2ODcxiM-KJ7nDA1W1dK5r6qHpN1Bikg-co0kjZnNGjFS_eMZPcfc5uFTwk4u-uHH_B23tBoGwX8o1MVVllz9KIWdZY4js4ekWI5Uy5MoKKoMZ-IleVt86MplR-wO3peMO65rs3RMZaQn7TYZYi6jH4bCeq8KgUaa1exzdXcuYJFY-nQEoUxVg9PooYiqnI3191bLHlhN83l7wqUum0MgN0PtPY8Ry8OPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو ساعتی پیش تو مقر کریا با وزیر جنگ اسرائیل و رئیس ستاد ارتش جلسه امنیتی برگزار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122801" target="_blank">📅 16:06 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNJ23u0kfv9oS4mFKb-WFzxjb-AMgb8DWRKMXq956Ts2luaUp8xko8WPPlDd0m2M_1_gpKH17Zk2fZQTXC2s6_-E84DC7wwTzZHdYhjU9YWrNDGG6hmPS2jDdNW-l63X7XsqpJB4l0cfJXcfciwYQgLAPna_JIZru-BmADlnajXhoF2b6NduMIinrocj-AmIAT4ZnGMkFQvlXy1um_lVRDqltSK0NpvwCv8bQaOCueB7GV22eXF84Q3dY2bCy2heYbffU0Ft3oXvGVrr2rRtQ-Pjm_KuUcN6me5P8QSbKAdnlxdSTe4wieIT5icYJ-M1Sr0P4P5lz8jn0ILa0c6iLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122800" target="_blank">📅 16:00 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-oR4ar5G3MzYoClXAxUJNgtH9JEm0EfAyE5bSSkyFlnKibTxB-0tkicB30Ntn-K2kTBwXrv81umDWfO8cUK4IYAoYNAT7O_U0ZzuOYm9Lzw8ZMBOocsuMJ4gFJT3bgJTIPvEM1_jj7-OqGTwd65Y95NQXgX3oiKvHBVvQy1_K7rPJAPbVd-od2BGQito4JsuZdxIKAQdaGYMAzu7aA5VVMtUgCCpag8cAYJzBhzoMgLwMSnJAMNTt7PNWySnnxOCa0ToAP9lLorTIFxGghtkRvWdJlkON65oCcUM3-kSBtyQPSIoqyycljueNhv83I6q6lJZOarUwCo9KfCnnfXvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی
: آقا بازش نکنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122799" target="_blank">📅 15:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122797">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWEtI2xp_MrRtJjhxXW6_j1w3o4IkMXru0vw8P6nEtOSEJNxjBLHKEOEpq-Fy4EspMQiwWycRObqFD-UKDtVLZ4021Nf9CjpC5dC22Gm2NkEwzN_TXKfjwyzGI5x9hhVzWjVWjqTZH-VT52xKf0tDrBE_y5v8S0PHRHXyUd8dWKVFsDALhI8ljdxmdBv9dTgyMKJ3Eb0n3yZVU4a9XCpCPsbB072CKbV4YXwYNHoX1lA0LpNh77GrLIa2iY4qX4rWj5QR4OjUCZbE0zXdzWjnWgirf6yGkcOm7kwNRyo2a-cGyuOZqa1VgWSFAl9MiCs2Zgbgx1lqeLwon-33F_XKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستار هاشمی، وزیر قطع ارتباطات :
با دستور مسعود پزشکیان، فرایند برگشتِ اینترنت کشور به وضعیت قبل از دی‌ماه 1404 رسما شروع شده؛ اتصال جهانی ایران هم از همین حالا شروع میشه و تا 24 ساعت دیگه دسترسی کامل مردم به اینترنت ممکن میشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122797" target="_blank">📅 15:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122796">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
الحدث: گزارشی از یک حادثه در فاصله ۶۰ مایل دریایی از مسقط در سلطنت عمان.
🔴
یک نفتکش از انفجار در اطراف خود در نزدیکی مسقط خبر می‌دهد.
🔴
خدمه و نفتکش‌ای که در نزدیکی مسقط دچار حادثه شده، با وجود نشت مقداری سوخت، در سلامت هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/alonews/122796" target="_blank">📅 15:49 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122795">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aBtZJNIutyQXe89Uog1WS7R_0W71jkarlmtH1iJBomMN1vze_hzN5RgohCDmBG-q1mlRFk-FrTl9Ls5SxwC93yRHEh25IQ0RfDuxWW8du0EY24WdNJ1qSoXDKveJKIsOfL-OehKjMhaEl1znUmDFHP8ktlbILf1CsqznP7FR41-ZxqvFUGlKuVmSSWTEI4GDExsz--Z5AOTNP8onVWMBMVeNC5Ly1G4jVJWD0VGotYpgCjrYcTtimbg-X5XDv_TjyMzGHhVGvQhoTvIqXR9ArD4M8RdZQnviEIcxM31695osQNoTD9ZCdZ7OScTHtRTeVapoUHaAp6LytxT-KufwHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت امور خارجه بیانیه‌ای در محکومیت حمله آمریکا در شب گذشته منتشر کرده و می‌گوید: «ایران هیچ شرارتی را بی‌پاسخ نخواهد گذاشت و در دفاع از ملت ایران تردید نخواهد کرد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122795" target="_blank">📅 15:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122794">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه، وارد ارمنستان شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122794" target="_blank">📅 15:37 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122793">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
تسنیم : طبق اعلام دیوان، تا وقتی پرونده‌ها و شکایت‌ها کامل بررسی نشن، هیچ‌کدوم از تصمیم‌ها و مصوبه‌های ستاد فضای مجازی اعتبار اجرایی ندارن و قابل اجرا نیستن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122793" target="_blank">📅 15:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122792">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
یک سری دسترسی ها به اینترنت وصل شده بود که دوباره قطع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122792" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122791">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فارس به نقل از یک منبع آگاه:
گفته شده آخرین اختلاف جدی میان ایران و آمریکا بر سر آغاز مذاکرات که مربوط به نحوهٔ دسترسی به منابع مسدودشدهٔ ایران بود، با میانجی‌گری و ابتکار قطر درحال برطرف‌شدن است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/alonews/122791" target="_blank">📅 15:32 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122790">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2UOSE6kQpmRCfS4HjWMVzf5eHA_qN0Mv-GSzaFbBL0nO6gS59q03mco-aOOBVSSEks94a8PYk1NU3OiYBp1tGzUjfsfVxLdKLucJzDfNqZUSQ2P7qFWsCaBtc-VwxHRzsDEioMfRWYJZ5hGlHGAoo5MsRfFp0FRbQvhPqARZBMQsWbZmrAx8iZvvceBL3g0DBhZa1A1FrvSw3PfbgUto37onxmUQHXjdaZbGUUC6N3Tcctc30_Mr2HaqOy6kUghV1RXxHCsRbvt8KLJWpvlYCusmGXC1caMl64Uc94U_4mo_hlRu5F8PaRjNDWB7oC3pDcWtxxsRrP0itCbPPS7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
از صدا کردن اسم جاویدنام غلامرضا خانی شکرآب تا اعدام شدنش به ۲۴ ساعت هم نکشید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/alonews/122790" target="_blank">📅 15:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122789">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F23qZsNLDBX9G4Oci7sqlbR2y_mYPnSmRsMDo8NT9cxaG465uw6kYQulP3TH-Ue0AYTlRWchRmpZ0gI4pmyRxEahZ6w-Oj6_NBzquRxFq82ztE6loN_lQR1IvP7wwf415LdXkLfGXQX008K8NzFX-x0FDbGLKP4y8v2uZa_h0b5Nevd1Wf8utrKp6TK7by2WsWo3VcWT_CN5FJebbE_u2SMfKXe2Fcqz6HzjnK-ogJ24f3-uYtrorfKhah86AqblH5Xko_YFb8-S8XGwzZ7xhLPc4Db6q8QFCXWoXz8tQLVOBfC-aVBOaogfvSEmF_UDDI5u1JMqXsBZa6jEB8vSFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل سد بقاع تو لبنان رو هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/alonews/122789" target="_blank">📅 15:27 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122788">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTFN7XoV7RzC2vbOMTwAIUv859npIt02Yhc9pviFWhLot_jjC-aRiBKBBxBFXmtbDGCjG-4E55yX4cqgQiM8MglZgvc5dv6XLxbVmYFX7h8lL1VXTfGtFPRI_NbHQcpeteOYF9UCL9T1WA9Ke7GNQmEKDFAaPhRRwG07U4oBhhk-ThmJIccMAskQUBa1rejz4e1PSsMSHtUVGJSjr-f-TSDKdU_f2wLBTYRjJbzrkNydfIoig_fe_dkrDomckp03mh4D5MN2r1nC7NKciAnEdBECzYhAR09q9zvfJF7xy2aev2U2raRX_LOQiVKAfRLUww2u-oGBDPLGNn0joMUduQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: بازی تمومه، دولت عمیق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/alonews/122788" target="_blank">📅 15:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpA7pXzT-RAPmYAxlpoWaWn_j9a1Af2BYqrzKZf3gA1k11HilPmlkphflG3CP9GWkTU1Tr8bPZgajKcn5P4lsS7fv15qpIC9x4Me22bEuc-KSH2aIR9ZjmuSCzeWdHoGfM540xzYbstShEiiv-viYnnuf7Z3GO4-QHxy-ccNdfNmUYDcIakKWOFbs96LOMthKE1chObjXVQ-v3WPEbWNxM3SdASiANlOEJu16asw63z8IyMj0aHvcfZyt8ZS4ZlI1K2r7F3XWgMLR8ZZt99TtuAVV_nTV-D76vLpv1lEgFQmFRVCa14vqXZrB5CsUHI3zt3FvDj3sdzTqEsgk9Sjbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجتبی خامنه‌ای : اسرائیل 15 سال آینده رو نخواهد دید!
🔴
غدّه‌ی سرطانی اسرائیل به مراحل پایانی عمرش نزدیک شده و به فضل الهی و طبق آینده‌نگری 10 سال قبل پدرم، 25 سال بعد از اون تاریخ رو نخواهد دید، ان‌شاءالله.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/alonews/122787" target="_blank">📅 15:13 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزیر کار: تا کنون 260 هزار نفر برای دریافت بیمه بیکاری ثبت‌نام کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/alonews/122786" target="_blank">📅 15:02 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122785">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfslAFL1-6zPccejsthgyA3McpDu5Z58VXYd79a8rBxP4u7VvqDIniNmqMTQ1qdRMrj8kw4eYfu-ZjFZexIKvsUvuuEm2NGX1Cfhd3HcYAXKPUU_XpBSmZNymZAgqYhDfxd_vQSlaXssfnXviFAfQBrNyyw5tgJbQPNnw1UR1Tx_n0Aby_BXHG0-oiAoZRkO2KfStRkqSvdNAx237I-svjwdewaSRd4nFhGF4x90bjBUxdmn2OhsSjC-vf88YqObds9oPhgFFnN9PnprVjaGJjo6LlddLcYKZf-HS40eQl6klkt_DXHqW6IiVOw7P_k2EsQ-2YWUk9U5StQ3jHSagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی دولت:
گرونی تو همه دنیا هست و فقط ایران نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/122785" target="_blank">📅 14:55 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122784">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⭕️
⭕️
اپلیکیشن‌ها را فقط از Google Play یا App Store نصب کنید.
🔴
فایل‌هایی که در تلگرام، کانال‌ها، گروه‌ها یا از طریق لینک مستقیم دانلود منتشر می‌شوند، اگر از منبع معتبر نباشند می‌توانند خطرناک باشند.
🔴
نصب این فایل‌ها ممکن است باعث شود اطلاعات شخصی شما، رمزها، حساب‌ها یا حتی دارایی‌های کریپتویی‌تان در خطر قرار بگیرد.
🔴
قبل از نصب هر برنامه یا باز کردن هر فایل، حتماً مطمئن شوید که منبع آن قابل اعتماد است.
🔴
امنیت را ساده نگیرید؛ یک کلیک اشتباه می‌تواند خسارت زیادی ایجاد کند.
⭕️
تحریم ها ارتباطی به موجودی کریپتو شما در تراست والت یا سایر کیف پول ها ندارند.
🔴
درصورتی که کلید والت خودتان را در برنامه غیر مطمئن وارد کرده اید حتما نسبت به تغییر کلید و انتقال موجودی به والت امن اقدام کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/122784" target="_blank">📅 14:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
از عجایب مملکت:
🔴
فارس: اینترنت وصل نمیشه
🔴
ایسنا: اینترنت وصل میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/122783" target="_blank">📅 14:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122782">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فارس:
ساعت ۹شب بیایید پشت بوم و بگید الله اکبر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/alonews/122782" target="_blank">📅 14:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122778">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qHRHvBXKlIQMh81XQxx6dPRuUgfrbQjm48zbuMN3JpiuvzguHLVEGjr7N1hCBUhnuWmBgDbRMqQ76DShsM9u0-A3RVb9OujMUiId-NWsn6rWmepzBDOe3UI3g9nn7pdRO1WuHgmA1dX5lwz4i8D25eeFtS8Wu_uipEBNnke0PCYjsuxMYgHN0-f-sQ1GmiS-j0UfZBH7iTqc6R4OrjOzkiAu4_29GSlCaib-Ew-N63KiDVUvhC9PjY3uqczpFv9Gucg48CxrN_Ct3Xrjf5lxS8m-TrtK-rMcUMJry1blpWCyupRReA4wIjd9dvuFsCj7KvQEs6sKRZkAaHxo1rYCAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfhHXR9IIdl2A93fTlqEZGMrv7EfTAYES9RXNx-OyQIvtLXMrkhPdqgAY0m3_NFf-Il98kC9xT924_D-kYXiBPB79Vi3UhgklJHZFnvFD-0qzC5RaksED-3pZHs2lJKbT7gqc0yt7-ox18VzcI6FBFwkJI_PhdEtvQdjFnI1cwkGFKHvNNBIr7Yk7irEWUrgA9NMK-19bLko9OUvF1qrzZo-I3IZ3GzEusIWnuuygVoKyr6K42Jvn--aeKoKyJDj8BF7oq7EWixKl59VJCTEy6xPOygi5fqny8DO1A73F8qiCXxdyGBCQzVT4ig6Q5LtexQCi3hfvBpgHVlO3VMPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UWMeTVOCpmrCr_3xoEL-fMMUVtem2g-yfJ10Y_QXMDK3tf4GLIjGgkbl8BtXgGwkgdjfcGNVZxLoKl2tVj3VmBL_4hre3Fa4phbpeQX1uhjgLQ0CJoYp6oygD736EbeaZ_zLWZDxgLa0k4wGg8g86LifE0V1TzbR42i4g9RcK59A0ZDMNoKi6dGTyg3Mm5mUTD4aEML5o4mQusy7nic6oV1ts0mHT1bH3aOATgsVYiKm0N6CvKvqjfRbpAsfGqVa05E19BTCC_9tTlvJIDg586IYJnSLdkGKCywnnVJu7p9svVUrtLLcuxW8PgJ1QYYvEKa91pBBph5JRKLA4kmjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZOWY4e0pTlkSq-UfkcPEY0sw5xgTbNQoAR7ekDCrlwSdVBOUuJRMNo4nMdpa0ucjCgs_1QAiFwB9sgmpjRwXFaM75bLhgxJrk7YAL0fo1io08-CWxiDmFeE5H5tNqbmipggRBnmiXPuPH0zsYRdhJ5LQ4BTKuAEnFYL__YMhle6-sC8nS-zZKZgN6hBW6hIw4ZhxxhMLhwhwGzlxoxoFdX_ov3wUcObn8bgHlAvIg9NgUIEB0qRVn5w1KxopJxjaoYanpcSP0uv5n1ZBPx6nw9Lh-4GAE6mfdX8BLuUGW1hBnW2RC2Qlu2ay1mTt405miaM03mGt3ay1gpImecX3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مرکز رسانه قوه قضاییه:  با دستور موقت دیوان عدالت اداری به دلیل بررسی غیرقانونی بودن ساختار ستاد ویژه ساماندهی و راهبری فضای مجازی کشور دستورات و مصوبات آن تا زمان رسیدگی قانونی قابل اجرا نیست.
🔴
دیوان عدالت اداری ورودی به موضوع قطع یا وصل‌بودن اینترنت بین‌الملل…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/alonews/122778" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-122777">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
رسمی/با اعلام قوه قضاییه اینترنت فعلا متصل نمیشه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/alonews/122777" target="_blank">📅 14:33 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
