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
<img src="https://cdn4.telesco.pe/file/uljMtn0IZLWNiO8cEp2u0l9vPbiwjWn5evvzY4KDNAwgpLiXD9YthMR9i4zEsY17rNC3j6hrVaa-9WSDnkBBHHP2V4ea_y0i0__8vUvBuheVJ99O-UJ7JFKsToHb3ZJWg7qYdiOVVrVdgjjncj9t5ncQi-wT8jOH_877EOmVVBcYXjfVwcUn1dZpQvS5dBMEN07uuTU09yte7IT74msm-HVMybKsqVHSkIW3RyTFGvD0F6Clt04hZ2-R1pt94DYiIA7YSfma19GUJBzAk9U8msliwTjEdm5vITkUcT91p8rPYEtnBpuPY6xI-IHs3cKYklLzeKNgAZnKBoFo7uDYdA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 454K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 15:01:28</div>
<hr>

<div class="tg-post" id="msg-23698">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بیرانوند دماغ به دلیل خالکوبی خواستار بررسی معافیت سربازی به دلیل اعصاب و روان شد. خالکوبی به تنهایی دلیل معافیت نیست، اما در صورت تشخیص پزشکان مبنی بر این که خالکوبی نشانه مشکلات اعصاب و روان است، امکان معافیت وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/23698" target="_blank">📅 14:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23697">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کرملین : روسیه هیچ اختلاف نظر با کشورهای اروپایی ندارد که بتواند منبع درگیری شود
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/23697" target="_blank">📅 13:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23696">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eba0f5326.mp4?token=imkmw505_xwtr4Ac6vUqMVzAWtmU_EoPr463vYdAbpOthZ8y5u_FFyMzw58gK4u8iEvzsLm01MjMJ2WRm_9EfMij0eE7GwY0smLPR91NCZes5WgewwHKE0vMgKYzCZvAJwsOY-NDrt_uEeYjNhJdgoT9uX1ZzrTzGSEwA3HdVPWkcoxA8a2NoQy8NFm9DDc_j3Id1gXY3NRtribYvKTn2zhw_JVPSuuE_w31uDoRV66Bq0qDTN2yN3VZP3yRQVO_pNn9f93SgFanY-0eg0BAkXG3Qfv8G9SXvpoPRTV069t_STSdQUm8KfI_ElRSlPe8MEaLZ2VxXNcvmSmO7rPMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eba0f5326.mp4?token=imkmw505_xwtr4Ac6vUqMVzAWtmU_EoPr463vYdAbpOthZ8y5u_FFyMzw58gK4u8iEvzsLm01MjMJ2WRm_9EfMij0eE7GwY0smLPR91NCZes5WgewwHKE0vMgKYzCZvAJwsOY-NDrt_uEeYjNhJdgoT9uX1ZzrTzGSEwA3HdVPWkcoxA8a2NoQy8NFm9DDc_j3Id1gXY3NRtribYvKTn2zhw_JVPSuuE_w31uDoRV66Bq0qDTN2yN3VZP3yRQVO_pNn9f93SgFanY-0eg0BAkXG3Qfv8G9SXvpoPRTV069t_STSdQUm8KfI_ElRSlPe8MEaLZ2VxXNcvmSmO7rPMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت موبایل یک پاکبان در مشهد
@WarRoom</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/23696" target="_blank">📅 13:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23695">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">جماران:
آمریکا برای
هیچ‌یک از اعضای تیم رسانه‌ای همراه مسعود پزشکیان
جهت حضور در مجمع عمومی سازمان ملل در نیویورک ویزا صادر نکرده است. مدیرکل تولیدات رسانه‌ای دفتر رئیس‌جمهور گفت قرار بود یک تیم رسانه‌ای کوچک برای پوشش سفر پزشکیان اعزام شود، اما با صادر نشدن ویزا،
هیچ‌یک از اعضای تیم رسانه‌ای رئیس‌جمهور نمی‌توانند او را در این سفر همراهی کنند.
آسوشیتدپرس تأیید کرده که برای پزشکیان، عباس عراقچی و کارکنان ضروری هیئت ایرانی ویزا صادر شده
و هیئت ایران امسال با تعداد کمتری از اعضا در نیویورک حضور خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/withyashar/23695" target="_blank">📅 13:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23694">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">قطر ایرویز
به‌دلیل
جنگ ایران و افزایش قیمت سوخت
، شماری از پروازهای کم‌سود خود را به حالت تعلیق درآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/23694" target="_blank">📅 13:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23693">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpNxjgwNliWoAgjp7mq6hgsNJHS7PVW1cwM5l83zTm4S9RJYaFryMY-pBbzbaiRfbmRpj9fyyKK8VpWrftO8XP5iGiu4Sg825DQbSfZqTGs117DNw0wFBE0G1LHix8pJP6qMRKhkJDwHTfOgtNcCmTf1LSCi4g7ovityo4ZF7aRi8Ifpi3t0mn9gLnflS4LymeqD7ewIZ6h4iMRBZUKbv01XrQEwR2uarpht9CxHL8qN0RcFCyGTzE1aI7Oe-dbkVd-TNASMTGBk-GsrfiofQNOATgxzV_uaAJniSrZZ57uIbDGmL2ZqmaG4ffNaqdRAdVyTyBAIfNF65fcQhRXFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏هم اکنون آتش سوزی در میدان آرژانتین,  تهران
@WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/23693" target="_blank">📅 13:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23692">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-2dpySzI2zSialPOBV4p4KrJwj4p4xQdcxnlamDTmL8rhobmWEs4Ck68O86CQ89H2r8arvcXES2HBxVdV8A2Y24TexHBnxcjphyI1h01rdmj0ALK-NvrealDrcizGdlg_Cy6TMG5RpM7d_4xVZ1kA6skIa5yQz9vuNucp6qSnbhm1IXYmf1vkq--pqq_Y_ZipcI3XFAUyibbJ2wGUzRP8FTDZPerOxKzWAR5_r0hqSCfbE1yxksN4mtLCkurLYZ6hH2eaBbkTCCGzUN9rgVE-R0p71M02pjymLlQ-kiF6k1nc5ucEOAfWAwKHi8K1GKf7O4OXcl2XmLyjHcUSKd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار ما دریاچه چیتگریم ی صدا اومد الان  پاشدم با این صحنه رو به رو شدم ی بوی باروتی هم پیچیده @WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/23692" target="_blank">📅 13:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23691">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پرتاب موشک از گرمدره ۸:۳۰ دقیقه صبح امروز @WarRoom</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/23691" target="_blank">📅 13:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23690">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">BTC 84,100$  @WarRoom</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/23690" target="_blank">📅 13:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23689">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ly6OXSBrk2tfmRTlxjQMEFiXjPuqSpTH135wamjr1HHMGBwv2k_FJwT08HdY_klPU_antoeXLOQFJYutyl1UAIp4dpOvBmfggr6ieYBpMcmdqm7nND0xQACORi8UcoL80gpMRw6aoIZYjaYXsXOSddyI6gW1x30W7-jmTfqbBLMtWTySpUuLEmq76og1RbgPKfekYnAK7nVs7xIV4Jjh_P5WPlyesrgAoZwYUwFM5IGfFkuI-y-C2owA76Cq9LhVJZMEwQcY2HUNl9J-l5pspp4TzI1qkSbgerfddXtKNHMh9YOGbel_O0rj9G0kdPv3B2WjEJHTVzvhBykXtvZwmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) به نقل از مقامات نظامی گزارش داد که یک نفتکش در حال عبور به سمت داخل تنگه هرمز، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
دو تن از خدمه دچار جراحات سطحی شدند، اما شناور همچنان با نیروی پیشران خود به حرکت به سوی بندر بعدی ادامه می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/23689" target="_blank">📅 13:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23688">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/withyashar/23688" target="_blank">📅 13:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23687">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق CIA:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!! صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند. این‌طور بود: «در این گوشه…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/23687" target="_blank">📅 13:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23686">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک شاخص مهم تکنیکال بیت‌کوین دوباره فعال شده است. گزارش امروز BeInCrypto می‌گوید بیت‌کوین برای نخستین بار طی ۴۵ هفته بالاتر از میانگین متحرک ۵۰هفته‌ای خود بسته شده؛ Galaxy این سیگنال را در چرخه‌های قبلی با کف‌های بازار مرتبط دانسته است، هرچند این به‌تنهایی…</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/23686" target="_blank">📅 12:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23685">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز:
یک نفتکش عظیم حامل حدود
۲ میلیون بشکه نفت عراق
در نزدیکی فجیره در حال انتقال محموله خود به نفتکش دیگری دیده شده است؛ این یکی از روش‌هایی است که برای ادامه جابه‌جایی نفت در شرایط اختلال تردد در هرمز استفاده می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/23685" target="_blank">📅 12:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23684">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">استنفورد:
پژوهشگران پزشکی استنفورد روشی ساخته‌اند که در آن
مقالات علمی به عامل‌های هوش مصنوعی زنده تبدیل می‌شوند و این عامل‌ها می‌توانند با یکدیگر گفت‌وگو کرده و فرضیه‌های جدید علمی تولید کنند.
این پروژه برای استفاده از AI در کشف علمی طراحی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/23684" target="_blank">📅 12:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23683">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3147444cd0.mp4?token=uGo-yps8bEeGmvxAYPZgUnT0l7JDbUJl7ZRHQvXqniqGW6yYJisyqcCG92d5H2frhMlZRF0HbzMp8UwA_MGAomErVEgvyobhc3BYT0JL9SjjOKq2YU4t2UrfjWHOAEPFuIw1nNXsrE8TnoQhYs3vp5vwE0IUFFMXpEt6j9bXsLRpEfhKLUZSP5xGTS016tAHPT518N-vDY2mfpjSIqhp1fO7vyvTB5IZzQ41mzE2dJNKH0o8wpdyfpc8DyogxJdtcdkwjQ7LiyZml85fshCEGdEz7hVnsgs8tT930p4boIvcKHz9vQKPiVr4zgx4L9ewJ5FYYeX0FK-httBoH-C5YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3147444cd0.mp4?token=uGo-yps8bEeGmvxAYPZgUnT0l7JDbUJl7ZRHQvXqniqGW6yYJisyqcCG92d5H2frhMlZRF0HbzMp8UwA_MGAomErVEgvyobhc3BYT0JL9SjjOKq2YU4t2UrfjWHOAEPFuIw1nNXsrE8TnoQhYs3vp5vwE0IUFFMXpEt6j9bXsLRpEfhKLUZSP5xGTS016tAHPT518N-vDY2mfpjSIqhp1fO7vyvTB5IZzQ41mzE2dJNKH0o8wpdyfpc8DyogxJdtcdkwjQ7LiyZml85fshCEGdEz7hVnsgs8tT930p4boIvcKHz9vQKPiVr4zgx4L9ewJ5FYYeX0FK-httBoH-C5YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از گرمدره ۸:۳۰ دقیقه صبح امروز
@WarRoom</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/withyashar/23683" target="_blank">📅 12:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23682">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">BTC 84,100$
@WarRoom</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/withyashar/23682" target="_blank">📅 12:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23681">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e4ac1ec1.mp4?token=IVblGl-7UVwzsXM8wVADTD_L8p4tPk6KEzCjFUeTdMxUscfdFdQZqal2R4MwRE_yBC7UqMtZJq7_2Xv6_IgIqwF2bGgD5LLLC-VTG6qvHvHhmM2UIcp2RYwT7_n5cNfMKsNgdxAnC1_q_zlj8OcJESC2ppusutszK3Wzwe4an9L7_h46XYVvMaNQiF7Qh_Q2LSmgcVeqbl4n77KiXh5_FBa12bI1l4ypzlPp7jKe-fApfrx1lmNDuuo9v4wjc6fqhdIhO9nnfeYCDsral3OllGuxjAJShpFK6SdjeXS9pWV_vmfmnTP9yrvdPORUlwlA1DMl4C_FS0TCYy6VppeETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e4ac1ec1.mp4?token=IVblGl-7UVwzsXM8wVADTD_L8p4tPk6KEzCjFUeTdMxUscfdFdQZqal2R4MwRE_yBC7UqMtZJq7_2Xv6_IgIqwF2bGgD5LLLC-VTG6qvHvHhmM2UIcp2RYwT7_n5cNfMKsNgdxAnC1_q_zlj8OcJESC2ppusutszK3Wzwe4an9L7_h46XYVvMaNQiF7Qh_Q2LSmgcVeqbl4n77KiXh5_FBa12bI1l4ypzlPp7jKe-fApfrx1lmNDuuo9v4wjc6fqhdIhO9nnfeYCDsral3OllGuxjAJShpFK6SdjeXS9pWV_vmfmnTP9yrvdPORUlwlA1DMl4C_FS0TCYy6VppeETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی عجیب یک هم میهن از چسب محافظ پنجره در برابر انفجار
@WarRoom</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/withyashar/23681" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23680">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e81b36f52.mp4?token=nBQjdASpTMb4KSLosmCKgLOdndIEZYz-C67twAXF5AnDSZW2Y1gdSYd9QoAaaybCVWsu4N42_PLBfuP4PgKqkuZuw1koJObSmM1LnUy_VmLESPn5zMbIvjSqtJGQ256F0XzuCRoqESk-l3wQ3Dcs2DCkDhX1VnSgVdh5ps_0tqjkaGVhM1p1d-N2Em2-FHUvk6-kUy1zzIkkuFMbe2xWI1dyX8cR6yUNqX6y6fXSGia4OHZ5Tl257CwjMMIPi3NO4IQjbMxn9tp8OCyrKAp3JlD6didRqiwCFpbiQFTPhEnAXjIEzWxJP556RuQ3bkSaq_zAp-lfGm1uLITGMlq0tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e81b36f52.mp4?token=nBQjdASpTMb4KSLosmCKgLOdndIEZYz-C67twAXF5AnDSZW2Y1gdSYd9QoAaaybCVWsu4N42_PLBfuP4PgKqkuZuw1koJObSmM1LnUy_VmLESPn5zMbIvjSqtJGQ256F0XzuCRoqESk-l3wQ3Dcs2DCkDhX1VnSgVdh5ps_0tqjkaGVhM1p1d-N2Em2-FHUvk6-kUy1zzIkkuFMbe2xWI1dyX8cR6yUNqX6y6fXSGia4OHZ5Tl257CwjMMIPi3NO4IQjbMxn9tp8OCyrKAp3JlD6didRqiwCFpbiQFTPhEnAXjIEzWxJP556RuQ3bkSaq_zAp-lfGm1uLITGMlq0tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق CIA:  اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت!!
صدها هزار پناهنده افغان در ایران هستند و هرگز تابعیت ایران را نخواهند گرفت.ناامیدند و اسرائیلی‌ها همین افراد را استخدام کرده‌اند. این‌طور بود: «در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار. اسرائیل هزاران نفر از این افراد را استخدام کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/23680" target="_blank">📅 11:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23679">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHyEszb8kT1o66aPzH2BC0z29WCGJrc7rTiVQoUaYubgHoN-O-Ggma1TjbGzT9szOAkmHuA75XA_pLv_AyuuvWXY_-jiEasPzLDZMH2D0KGiiGkbv5CWaGpqdO4zxjujRVdVyn4vieeJ87knJiAPuZta9-pSTPIaykdEJPfwPG6T_cj2xebKPV_oPX3weFQ881pyKAWTlgZ5kvN94OyfkJ2wk_Qgyt21UcddHZ0Zc49RS_YvJZ8zEv9nsAnOC1KELGIZPvujnSEb-pi27xH36NgbB447UsYK8yav-z4nFEMzw9m6MIzGXcgkBgewCbv6jPjuPpdbRsGXUvR1LzKUgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/23679" target="_blank">📅 10:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23678">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فایننشال‌تایمز:
اسکات بسنت، وزیر خزانه‌داری آمریکا، و
هه لی‌فنگ، معاون نخست‌وزیر چین
، روز یکشنبه در نیویورک حدود
۸ ساعت
مذاکره کردند. محور اصلی گفت‌وگوها
تجارت، تعرفه‌ها، هوش مصنوعی و مواد معدنی حیاتی و عناصر خاکی کمیاب
بود و دو طرف درباره ایجاد کانال گفت‌وگو درباره هوش مصنوعی نیز به تفاهم‌هایی رسیدند. در این مذاکرات، نگرانی‌های آمریکا درباره
حمایت احتمالی چین از ایران
نیز مطرح شد؛ از جمله ادعای استفاده از تصاویر ماهواره‌ای برای کمک به هدف‌گیری مواضع آمریکا.
@WarRoom</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/23678" target="_blank">📅 10:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23677">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیویورک‌تایمز:
ترامپ در آخرین لحظات تصمیم گرفت حملات آمریکا علیه حوثی‌ها در یمن را آغاز نکند؛ این در حالی بود که پنتاگون از قبل برای عملیات آماده شده بود. پس از درخواست
محمد بن سلمان، ولیعهد عربستان سعودی
، ترامپ به پنتاگون دستور آماده‌سازی حملات هوایی را داد، اما تا روز یکشنبه بار دیگر از تصمیم خود عقب‌نشینی کرد. به گزارش نیویورک‌تایمز،
فهرست اهداف تأیید شده و بمب‌ها در حال بارگیری روی جنگنده‌های آمریکایی بود و حملات تقریباً آماده آغاز بودند
که ترامپ دستور توقف عملیات را صادر کرد. همچنین بیشتر افراد نزدیک به ترامپ نسبت به ورود آمریکا به جنگ عربستان با حوثی‌ها تردید داشتند یا مخالف آن بودند، به‌ویژه با توجه به فشارهای نظامی آمریکا در جنگ با ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/23677" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23676">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سخنگوی سپاه گفت
جنگ تمام نشده و سپاه برای یک جنگ طولانی‌مدت آماده است
. سردار محبی همچنین گفت در صورت حمله جدید، ایران «جغرافیای جنگ را تغییر خواهد داد» و از رونمایی سلاح‌های جدید سخن گفت.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/23676" target="_blank">📅 09:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23675">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQwM5KnyPuXO4ttIWTbiB1YHKh8tf2-dXBUTAuKyTBhWtsyniKvxuRI8XNy8o3r19Ta70jbvhHxDJz5OfWMJ4xqtWx5g-0AGBVOBrkD19VGIXdncgcxE-cr785vVoupuHBRCSEYVUcRGSxQz-WBuQsBukV5aPw00bILyGa-zUz7nY2hLsixI6dBHVGKIe_DNBRqxfYKX1RNpYTxyQ25FMB-jOBo4xSAZGY98vmHkaZ1laKvLzYwbpaky9qiyBvlXoBfd1J1yv2v5o7vDNZrlVANoM-6G2kgRGgp-yCfMZ1gkDtjNzHzwtw2u9URv2PIu-qM7kcOezq4uxRzsflhDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
:
«قیمت بنزین در دوران
بایدن
بسیار بالاتر از دوران
ترامپ
بود. تقریباً
قیمت همه کالاهای دیگر
نیز همین‌طور بود.»
@WarRoom</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/23675" target="_blank">📅 09:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23674">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بیت‌کوین دوباره از ۸۱ هزار دلار عبور کرد. قیمت BTC در معاملات امروز تا حدود ۸۱٬۸۰۰ دلار بالا رفت و در ۲۴ ساعت حدود ۱.۴ درصد رشد داشت؛ در یک هفته نیز حدود ۵ درصد افزایش ثبت کرده است. @WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23674" target="_blank">📅 09:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23673">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بیت‌کوین دوباره از ۸۱ هزار دلار عبور کرد.
قیمت BTC در معاملات امروز تا حدود
۸۱٬۸۰۰ دلار
بالا رفت و در ۲۴ ساعت حدود ۱.۴ درصد رشد داشت؛ در یک هفته نیز حدود ۵ درصد افزایش ثبت کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/23673" target="_blank">📅 09:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23672">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اروپا امروز ۳.۳ میلیارد یورو کمک دفاعی جدید برای اوکراین اختصاص می‌دهد.
این بسته از سوی کمیسیون اروپا پرداخت می‌شود و در چارچوب حمایت دفاعی اتحادیه اروپا از اوکراین است
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/23672" target="_blank">📅 09:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رویترز : با باز شدن بازار نفت برنت در معاملات آسیایی حدود
۱۰۲.۰۸ دلار
و نفت آمریکا حدود
۹۸.۵۳ دلار
بود؛ بازار بین افزایش عرضه خلیج فارس و ریسک هرمز در نوسان است.
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/23671" target="_blank">📅 09:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تشدید تنش میان کابل و اسلام‌آباد؛ جمهوری اسلامی پیشنهاد داد میانجی شود
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23670" target="_blank">📅 04:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23669" target="_blank">📅 03:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23668">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گزارش های بسیار شهر‌ری شیشه‌ها لرزید و انگار زازله اومد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23668" target="_blank">📅 03:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23665">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4130309e48.mp4?token=UW4B4-uIttbYozfXu4sTMr-iHErDT--NWjQnEXg7XXWOnfHLIYF1b7YWo1RYAQHzFdUcM_EoGzcgaKERYhnfsQhx2h7gNT8rbQzbEy1C00rYO8XIFPg1EmXJt6YcniKf73XvsI1mZaCBvOpMLUPjmBngmS9zkGnw_-rcqfQgosml3xPiGAkEOI4NRFeCkrPnLZYoYPT8dgbOoE2kt2oEObA02N6FP9OluiVOC8U1AXjxjNtO1Rl7Ky6TE9QG5zInjBGDsGyKNyBD5R5J1pc39-zb5jWnFIIK_BxtrzTz8ui-RY7afMzK4Oy_o_jLWhGZef3b2a2TfW4sI5g4iJHhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4130309e48.mp4?token=UW4B4-uIttbYozfXu4sTMr-iHErDT--NWjQnEXg7XXWOnfHLIYF1b7YWo1RYAQHzFdUcM_EoGzcgaKERYhnfsQhx2h7gNT8rbQzbEy1C00rYO8XIFPg1EmXJt6YcniKf73XvsI1mZaCBvOpMLUPjmBngmS9zkGnw_-rcqfQgosml3xPiGAkEOI4NRFeCkrPnLZYoYPT8dgbOoE2kt2oEObA02N6FP9OluiVOC8U1AXjxjNtO1Rl7Ky6TE9QG5zInjBGDsGyKNyBD5R5J1pc39-zb5jWnFIIK_BxtrzTz8ui-RY7afMzK4Oy_o_jLWhGZef3b2a2TfW4sI5g4iJHhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : یاشار ما دریاچه چیتگریم ی صدا اومد الان  پاشدم با این صحنه رو به رو شدم ی بوی باروتی هم پیچیده
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23665" target="_blank">📅 03:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23664">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f5195837.mp4?token=ZCQajU4YJMb04ho_ATQBb3Z8EOJGtSVJ9o8pSlvmqr3Lmc862tIxZKk36jL39zJSUeqK4__cBosacOloL3LmbWR-oJ148KSpoR4rdYl102805Gg1LGcDFrUe02Z_tOacrDiL1UisvHQuPMdSXI_ydtogT7qXTIWhyNQC7357ZpcWsxUxMY6D7ljFO5rpZK_jBB8uMgfjCI9qFThusik02G3p3HU8cahC0WJyUvJidE-_9nyw7hIw6bs1Fdqqa8yz8jeRboBTEFznyhBLV-OEJm52BQ3zv40OPcGN0e5d6UfsTkRRixAYpNb4ghFaR3LQlo0A4NPL7sbaoxtc-35SLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f5195837.mp4?token=ZCQajU4YJMb04ho_ATQBb3Z8EOJGtSVJ9o8pSlvmqr3Lmc862tIxZKk36jL39zJSUeqK4__cBosacOloL3LmbWR-oJ148KSpoR4rdYl102805Gg1LGcDFrUe02Z_tOacrDiL1UisvHQuPMdSXI_ydtogT7qXTIWhyNQC7357ZpcWsxUxMY6D7ljFO5rpZK_jBB8uMgfjCI9qFThusik02G3p3HU8cahC0WJyUvJidE-_9nyw7hIw6bs1Fdqqa8yz8jeRboBTEFznyhBLV-OEJm52BQ3zv40OPcGN0e5d6UfsTkRRixAYpNb4ghFaR3LQlo0A4NPL7sbaoxtc-35SLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : سمت چیتگر مسیر کرج به تهران همین الان
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/23664" target="_blank">📅 03:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23663">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">امروز، ۳۰ شهریور، چهارمین سالگرد کشته‌شدن نیکا شاکرمی است.
نیکا، دختر ۱۶ ساله اهل خرم‌آباد، در جریان اعتراضات ۱۴۰۱ در تهران ناپدید شد و چند روز بعد پیکر او به خانواده‌اش تحویل داده شد. نام نیکا شاکرمی همچنان یکی از نمادهای اعتراضات  است
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23663" target="_blank">📅 03:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23662">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/23662" target="_blank">📅 02:38 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23661">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نور های هواپیما چه معنایی دارند @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23661" target="_blank">📅 02:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23660">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRyrD0ZxenoTyQw92x-ZIscOTtVd__Uzhtc_h7MUwUvTQcTtdchHSwrrGnsEB70uT7UUfmegmoihEkKto_dDCwppmfHWdGIDj0dV8Sjbjt9ZpF3aaCow7BbluZpO-Wb8-yLyknI5ow4gWNUYi9PlOiERP4dR18ITSFHAD4NlXCSOhMTnUKmn3XI26U81EYhEHEKn-8Qz-SMfiOkoKFTNFrceJhvv2Zl9j13NN7TBCfRZtc3TQr4HnqEdU7ntDk73H4GRElCerJrmCxAsmQWtnWTtABW4aFmNutNS7GWKnYj0TZdut20nnJ9Shbi25AoN_7KCPDcQhX0piJb0I2AMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین های فیک بیسواد تلگرام این هواپیما رو جای یو اف او قالب کردن ملت
😂
😭
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23660" target="_blank">📅 01:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23659">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd534fa54f.mp4?token=smJbA5s7t7rFe_ILyRVCDOfukjhmTO_w4w4JoX0QbUdOD3Cf2ugXRfrUD2rnurlwqo27TUpE7St1gs8jwmkZPe0As-Y46fcCGTXxV7MMUvvfaLbrU_XC5Wo3A7D9uk0PNHLGGwAJV3TGyX53Jq7QMwKu71CfUps2gvhzDzMxTed8evfPoSfxcjs-BENkCzHuX29ICfCopvuSi-VOXX4H6EVH9WPvXS0ShMMAYJtCTPnErE31cHPEGPcaolosMrD9b582IF4s0Bl3BYNzZw7bzxKpvNugwcxnbgfhokAfzAeJV1jDBVHfu-i4fVtFjl4SaaPCtUkkV_r6K_ocrU0_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd534fa54f.mp4?token=smJbA5s7t7rFe_ILyRVCDOfukjhmTO_w4w4JoX0QbUdOD3Cf2ugXRfrUD2rnurlwqo27TUpE7St1gs8jwmkZPe0As-Y46fcCGTXxV7MMUvvfaLbrU_XC5Wo3A7D9uk0PNHLGGwAJV3TGyX53Jq7QMwKu71CfUps2gvhzDzMxTed8evfPoSfxcjs-BENkCzHuX29ICfCopvuSi-VOXX4H6EVH9WPvXS0ShMMAYJtCTPnErE31cHPEGPcaolosMrD9b582IF4s0Bl3BYNzZw7bzxKpvNugwcxnbgfhokAfzAeJV1jDBVHfu-i4fVtFjl4SaaPCtUkkV_r6K_ocrU0_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین های فیک بیسواد تلگرام این هواپیما رو جای یو اف او قالب کردن ملت
😂
😭
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/23659" target="_blank">📅 01:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23658">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ارسالی : یه سوله کنار ‌ایران خودرو در آتش میسوزد
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/23658" target="_blank">📅 01:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23657">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش صدای انفجار/پرتاب ؟!؟ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/23657" target="_blank">📅 00:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23656">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28d06fec75.mp4?token=dVbo2cVZjgfZApFf9T3ciCHjDDdP22ubt49gSy885BZS9yU2vRoD-JGQwmCy5W38FAsgPa4kyG5diY5bZ07-RQ1B3Tk85qXbTYrWqsobNsG7M0rkxA3cygS8uxY4TYYahoifx5n2RmHuMIQxNYNIkL43RL4Siq6NU-35hDI6EYaKlGzXy-yj7bnxfXFVSrWH2VN1046EguQ5NKQzoaZ3Olr2isrBJiU9r_j0KHfQrvWGc3NGrRYMDnOVbM0vnoPFcaOYy36_9Jm8M2zzl2YnCFkqSImjd1CNz-1He_aq5Usbmj2XhnDuwJ9zPRFN3xABGyV-EHM76AFKElZmomv0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28d06fec75.mp4?token=dVbo2cVZjgfZApFf9T3ciCHjDDdP22ubt49gSy885BZS9yU2vRoD-JGQwmCy5W38FAsgPa4kyG5diY5bZ07-RQ1B3Tk85qXbTYrWqsobNsG7M0rkxA3cygS8uxY4TYYahoifx5n2RmHuMIQxNYNIkL43RL4Siq6NU-35hDI6EYaKlGzXy-yj7bnxfXFVSrWH2VN1046EguQ5NKQzoaZ3Olr2isrBJiU9r_j0KHfQrvWGc3NGrRYMDnOVbM0vnoPFcaOYy36_9Jm8M2zzl2YnCFkqSImjd1CNz-1He_aq5Usbmj2XhnDuwJ9zPRFN3xABGyV-EHM76AFKElZmomv0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امیر تتلو 39 ساله شد، امیدوارم مشکلاتش حل بشه، جاش تو این روزا خالیه.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23656" target="_blank">📅 00:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23655">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el5R2NN3B2OIMBtOIdW_tXk5HSkPmgE0yqwsVzi2GC_N9Z3FdvpXLZb27NFfTdiarjrULm2Cah5vf9UhKVycXesqVkGoX0PfZdZ6YubHpcwE8nIPWGTwigUKUzOAt_fXQZ46mveG0JU2uqP5XramyKM8wMXp-mCOWrsp2rEavrhl7h44OUqtbhe_TcsL_ObXVDHTZcj32TKdKJOwiqC_apMQgpmvIWnS4gFbixS_s-qoQ3L4soRx8Wcibhi0OmEpfUyJF5IFtM7B12eU2UmFcbgiK5KGXqVgf8ZcO72nhdEHX6LwJn9H3Kxl39Hxt-eidi1L3LSnMY9u8UtBjcPIAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشت سوخترسان آمریکایی و دو سوخترسان از کشورهای حوزه خلیج فارس هم اکنون در حال انجام مأموریت در آسمان منطقه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/23655" target="_blank">📅 00:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23654">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23654" target="_blank">📅 23:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23653">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/23653" target="_blank">📅 23:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23652">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وال استریت جورنال به نقل از مقامات آمریکایی: دولت ترامپ در حال آماده‌سازی برای تحریم‌های گسترده علیه دادگاه کیفری بین‌المللی است.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/23652" target="_blank">📅 23:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23651">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس" به نقل از یک منبع آگاه، ترامپ بارها از زلنسکی درخواست کرده است تا حملات به پالایشگاه‌های نفت روسیه را متوقف کند، زیرا این حملات باعث افزایش قیمت جهانی گازوئیل می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/23651" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23650">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/23650" target="_blank">📅 23:31 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23649">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMC9Dql7e41zdCBTPcmNI-NNNuiKVGwcYHdXCWqHKgQkvLZ8-NOZAclU4Dd0t7OglPymAgGA2ZgqEGDTFLvb9Dso67YvADCIpTvZgl_HjE3WiBc7pjizDKTNmZmf59mDOB1iym6PyxQSRSOCDYCwC7NyiX-JIyTmOh3kYeWM2_Qp3rgotlLvNrvdM4YOCy0L7e2BLQnIsI6AjLlkASuEucXzDAnjy812tjARTLP6F8xrQ8yt-h-90fYgTlIvJiqwFowFLxKyt0xlN8MHebq0qbmtUnJXJWDutZh8fzHOGskhO42IokFNaff_zFG0xPDxMPL0Igl-9j0AZzCcKnZgjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت آنلاین آمریکا در ایران از تمام شهروندان آمریکایی حاضر در خاورمیانه خواست برای احتمال لغو پروازها و بسته‌شدن حریم‌های هوایی آمادگی داشته باشن
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/23649" target="_blank">📅 23:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23648">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/23648" target="_blank">📅 23:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23647">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">مستندی برگرفته از اسناد محرمانه ی ایالات متحده درباره ی رخدادهای شب بیست و ششم شهریور سال ۱۳۵۵.  به همراه مکالمات رادیویی واقعی از گفتگوی خلبان های نیروی هوایی ارتش ایران با برج مراقبت و مرکز فرماندهی.ماجرا از این قرار است که شبی آرام در اواخر شهریور ماه حوالی ساعت 10 شب تلفن برج مراقبت فرودگاه مهرآباد به صدا در می آید و حسین پیروزی 35 ساله مسئول برج گوشی را بر می دارد. پشت خط خانمی با صدای نگران خبر از رویت چیزی عجیب با پره هایی شبیه پروانه های اتومبیل در آسمان می دهد...
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/23647" target="_blank">📅 23:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23646">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBCpL670CsGRXrZTI9FAtxepujzNVvYAn2-Ygb7oDFShWmnVNJTizSj95T3IXxG-n6Ib3BlvtgNwhxXw9TGbyhOMh70QKnB8kK247rXsQvX6DpeFpSZh_KqN5L9C3UiTXhdmnpGjKaNomoF7_GzMwaw_0B7C_OqIEFISTSFdyKjj9ZhEKovG4LR91p1og0Bq7hL_g_l0snRfM1rlcLlEcQTqVYQ4bYEvIewG-FRl_cH8kEvzy_SBcIv6PhOs1uLbZhcPVkXP0AzLp9A_Y8vFDwX_fCZ5mZaUQMnNHBBRIqZ-hPZkqIPtVp0MkMTqPwDPxJ00BK4IuPeqXfTCnHxOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از بى نظير ترين عكس‌های بشقاب پرنده در جهان (پارک جنگلى تپه‌هاى عباس آباد تهران) قبل از انقلاب
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/23646" target="_blank">📅 22:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23645">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95feb353e9.mp4?token=gbhRvuWPUc4bepoAO0TGYS910LKKU2OmxtGXr-0TENlCXaD00X9uX38PlL2oVau-QqyZHxNZvaAlbcQiGOyAyBVDXxto-WfCCIZQ3eRd9EBIZ8ezCIiodjYT5dVOv6rv0FPx7YxpnhXH_kLoz9yV_ROb7vvQbgJ2lT0TVN91cqL-x-2wOVpD_wxH0yKKMfvVNHvcE8vmOU4cbiP81ZKJ2NxZnDps1OVj3O17OPla__z9U9d5ceCM93d8kqILr27zfHlG_C0G-Wy8jESAdm0diotduXwKCCunxgCvw5y7VBCZUz3OuoAto1-miE8bWQPnOhbqbgCv2nHIQs-JESTsbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95feb353e9.mp4?token=gbhRvuWPUc4bepoAO0TGYS910LKKU2OmxtGXr-0TENlCXaD00X9uX38PlL2oVau-QqyZHxNZvaAlbcQiGOyAyBVDXxto-WfCCIZQ3eRd9EBIZ8ezCIiodjYT5dVOv6rv0FPx7YxpnhXH_kLoz9yV_ROb7vvQbgJ2lT0TVN91cqL-x-2wOVpD_wxH0yKKMfvVNHvcE8vmOU4cbiP81ZKJ2NxZnDps1OVj3O17OPla__z9U9d5ceCM93d8kqILr27zfHlG_C0G-Wy8jESAdm0diotduXwKCCunxgCvw5y7VBCZUz3OuoAto1-miE8bWQPnOhbqbgCv2nHIQs-JESTsbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/23645" target="_blank">📅 22:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23644">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6GqQna3fYIMwl1wba5ZiRkGALT7SthDrQCtGgVtd1lL3pppW0EM7F3nxf1d_iPTwvdFmGpqgupXzSftq51pypWdNZ-cHtIIx9_FcFH6LxvfaPTsLwfGYGcuTEe0gZEs0jtEuWVwzqYheKmAk97v4kjEgC5rrJrSlchLU3tpqnOdpothqHwP2g_XBHL-OvC-6G8PSwWx57ph_VLaj_CIK1FJl6Htvx0JrKdOE3IZZy3bRaHp8P85HZ6m0CWJOkgOp3_cTIi830ibT93p_95DdjtHWldlNWi3DJwhe439PjUZNVlOfSIFap7KNgx46_tFI4eXhTTK6dpqbAoEb3x7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای عراقچی بعد از توقف کوتاهی در دوحه قطر دوباره به تهران بازگشت و میان انبوهی از هواپیماهای سوخت‌رسان و جنگندههای رادارگریز آمریکا عبور کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/23644" target="_blank">📅 22:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23643">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/23643" target="_blank">📅 22:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23642">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d2baa686.mp4?token=B8VJYfszYEW5n2UhkUC3uxYUcqkRecrY37hND_5PoNFeRCoIB6I-zwLRqst-r-p2yZaQZWixwkLIYF_GTgRLy8puUxPl2aYIjpO7yrW1NToQbihL2cag38V19Ixo_65j7hlmhn5M08eDHyY9kgT0SWs1CpGOyfVtiSshFPz-vWav8S1rqbue1I5qmENmNVtt64YPQpxU-_7QeT_FNPDa1CruWsVi-eAa4VZhczorp4sWxF3wMHneWfGeq7Vh1KE-UOI5PNa5WzhVC1D2hjZXm3Kwf0NeEWXnL2pcRuv1aAnTfUQe1k1NL0aftR9rWvZlYmeDIiEGaAYyXPoGXz0dFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d2baa686.mp4?token=B8VJYfszYEW5n2UhkUC3uxYUcqkRecrY37hND_5PoNFeRCoIB6I-zwLRqst-r-p2yZaQZWixwkLIYF_GTgRLy8puUxPl2aYIjpO7yrW1NToQbihL2cag38V19Ixo_65j7hlmhn5M08eDHyY9kgT0SWs1CpGOyfVtiSshFPz-vWav8S1rqbue1I5qmENmNVtt64YPQpxU-_7QeT_FNPDa1CruWsVi-eAa4VZhczorp4sWxF3wMHneWfGeq7Vh1KE-UOI5PNa5WzhVC1D2hjZXm3Kwf0NeEWXnL2pcRuv1aAnTfUQe1k1NL0aftR9rWvZlYmeDIiEGaAYyXPoGXz0dFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از بهترین فیلم‌هایی که در طول بیست سال تحقیق و جستجوی من در مورد فرازمینی‌ها دیدم، مخصوصاً این‌که در ایران است. هم اکنون توسط دیدبان اتاق جنگ با یاشار در اتوبان آزادگان گرفته شد
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/23642" target="_blank">📅 22:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23641">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/23641" target="_blank">📅 22:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23640">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/23640" target="_blank">📅 22:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23639">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : جنگنده‌های F-22 رپتور هم‌اکنون در نمایش هوایی نیروی دریایی آمریکا در پایگاه اوشیانا در ویرجینیا بیچ در حال اجرای نمایش هوایی هستند. نمایشگاه NAS Oceana Air Show امروز، ۲۰ سپتامبر، در حال برگزاری است و تیم نمایش هوایی F-22 رپتور یکی از اجراکنندگان رسمی این مراسم است.
در نتیجه خبر پرواز پنهانی F22 ها فیک نیوز است
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/23639" target="_blank">📅 21:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23638">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cdf7c3621.mp4?token=UjgrTTS2aQ9vXsH1nXFNw2bpZ3TuqLC_zOW-qnCRrNFUFypHp4RYukfJWmv4CrUsnFPZseBsoLiUrGDxXRwxxrX32iKS3l9v9OwUjVEmrIsTDoTj4o3OIa9HZQNyvtlzEGUgLjRHqyUSla_ySM4--_KaaluOBSMqFwHTJ1Ah03_JOASjRaGPApqx25f-rAZHc03TXYz4BDTfoaOEn-gMnhDMM6IKjSTpJ00UsB9vSF7nAhQ-I8hGmVnoYy3YIain-lK3Tf2xUdpPjuXIBxWT2wk4Bj2jiYQQtm7wfyFE5ucmtRBkYy0ZfL1tjgbmhIGZKMfxZIK8wdiek7H4kkSXVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cdf7c3621.mp4?token=UjgrTTS2aQ9vXsH1nXFNw2bpZ3TuqLC_zOW-qnCRrNFUFypHp4RYukfJWmv4CrUsnFPZseBsoLiUrGDxXRwxxrX32iKS3l9v9OwUjVEmrIsTDoTj4o3OIa9HZQNyvtlzEGUgLjRHqyUSla_ySM4--_KaaluOBSMqFwHTJ1Ah03_JOASjRaGPApqx25f-rAZHc03TXYz4BDTfoaOEn-gMnhDMM6IKjSTpJ00UsB9vSF7nAhQ-I8hGmVnoYy3YIain-lK3Tf2xUdpPjuXIBxWT2wk4Bj2jiYQQtm7wfyFE5ucmtRBkYy0ZfL1tjgbmhIGZKMfxZIK8wdiek7H4kkSXVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/23638" target="_blank">📅 21:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23637">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حقیقت یاب اتاق جنگ : اسرائیل از امشب همزمان با آغاز یوم‌کیپور، حریم هوایی خود را به روی پروازها می‌بندد و فعالیت فرودگاه‌ها متوقف می‌شود. این تعطیلی مطابق برنامه یوم‌کیپور انجام می‌شود و حمل‌ونقل عمومی نیز در سراسر کشور متوقف خواهد شد. یوم‌کیپور، یا «روز کفاره»،…</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/23637" target="_blank">📅 21:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23636">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حقیقت یاب اتاق جنگ :
اسرائیل از امشب همزمان با آغاز یوم‌کیپور، حریم هوایی خود را به روی پروازها می‌بندد و فعالیت فرودگاه‌ها متوقف می‌شود.
این تعطیلی مطابق برنامه یوم‌کیپور انجام می‌شود و حمل‌ونقل عمومی نیز در سراسر کشور متوقف خواهد شد.
یوم‌کیپور، یا «روز کفاره»، مقدس‌ترین روز در تقویم یهودیان است؛ روزی برای
روزه، دعا و توبه
. در این روز زندگی عمومی اسرائیل تقریباً به‌طور کامل متوقف می‌شود؛ پروازها و حمل‌ونقل عمومی تعطیل می‌شوند و کسب‌وکارها نیز فعالیت نمی‌کنند
@WarRoom
یاشار : جو چنل های دروغ و زرد رو باور نکنید</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/23636" target="_blank">📅 21:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23635">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMEg5kdcKd405CccoJohYIlXEY6DeKHdff2I9bkm4-rRwLRIoyiGpD9QL4_lErsJpyxJ7rAf9pv-ghvQNuW9jejtlnwM3alkwpMJsE-NfEbFjNjZLY-QKpT9Gy0XfVx1QvhLmn_GCE68kPM7JcEFZP-kUfc5eNODP5SXGcsk1kuu4lOcCkcBLudDDLbJU7g73clAXpVQ0V5Wu12U0O_Yknzp7tOdnCFa90GO3Hf1Uq07l0coFajtHy0L1vqKsCwfS7glnbm-ChC76dPBrqPmZGysEpOyCJaR5GZ-wZHvPNslIDST0hghU7qPL3gyXqN5r_ZYWsbur2ZxKsSnGRQD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول   اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن  https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/23635" target="_blank">📅 21:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23634">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrlHwK3gIDc-bkWaih6b_gCD3ZUfHmC3wHD_k9gBSj_ODBMugfLjLxiq50ZSWNxwTtme1nOmI3cVaOAhpuaJKLXxmKu17kvNbYcHBU75OnRcYCfQhbvSj3CAZzZcHKpQO_r8Axi2ekUiZT4EnwuMivFkaUSoyoBagYnNg_-um7HXchptKoRbL45mTu0zBzDTf7TOTZ28R9qdeDSSoSuU9VvVHHS_sUZiJi5xwmnFjNa5J2uGlEIjBpwIYdEASVjwyrcXmHFgDc7fITgDad3ONq7HoeQClqISxk2iVPuE-hz01jmPk_3vq_QRfN7mGfgX8ha3YqsHyubMrNLKsTvEJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصاویر ماهواره‌ای جدید نشان می‌دهد چین در یک میدان تمرینی در نزدیکی لوپ‌نور با ماکتهای جنگنده‌های اف-۳۵ و اف-۱۶ آمریکا، سامانه‌های پاتریوت و هواپیمای آواکس ای-۷۶۷متعلق به ژاپن را ساخته است.
اهمیت ای-۷۶۷ در این است که
ژاپن تنها اپراتور این هواپیماست و فقط چهار فروند از آن دارد
؛ موضوعی که می‌تواند نشان‌دهنده تمرین برای
سناریوی احتمالی درگیری بر سر تایوان و ژاپن
باشد. چین از سال ۲۰۲۱ در بیابان‌های سین‌کیانگ ماکت تجهیزات نظامی آمریکا و ژاپن را برای
تمرین‌های تیراندازی و آزمایش موشک‌ها
می‌سازد و اکنون با اضافه‌شدن پاتریوت و تجهیزات اختصاصی ژاپن، مجموعه اهداف خود را گسترش داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/23634" target="_blank">📅 20:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vhw9hvXJoiTFscm-CzQMJctAeofWwjBemhds2OZBIHBhoqaVZ2IFi33lTzV3k9ZjHIPyt03QLUGr6FwN5HQqXSh9W94P1DTjk-dkhrF3UkY37GMmtMTVr8hh56ovYUgBDfktAToyR99LpxaVirrHkrbRShT1So7EOc--1Q3M4VVQ8B7eyO2k4fBZEKuGc35hsQWOsO95gUKB10SlWqenlR57QfU5Pyeb26EWr-8iiRN9DXjUHeC1xwzRETU9SUUPuBBjkZ9XNTCRa02YRx7IZyMYx1BBWUUDYZTc7onI8-i7_QwtnQqOKKPbrWYDM2u5uH8mwBfjxHC2KaIj9oz_mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفارت ایالات متحده در عربستان سعودی اعلام کرد
که به دلیل شرایط امنیتی فعلی در این کشور، برای تمامی کارکنان دولت ایالات متحده که قصد سفر به شهرهای یانبو و طائف در غرب عربستان سعودی را دارند، مجوز ویژه‌ای لازم است.
این اطلاعیه پس از حملات موشکی و پهپادی سازمان انصارالله به تاسیسات شرکت آرامکو در یانبو و پایگاه هوایی پادشاه فهد در طائف منتشر شد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/23633" target="_blank">📅 20:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz4N4Npj4Zs5LPpRohy_ctSrHp-LhzikMkuua2ZcSuPM9tgEnt8gtsPnG49actAsB1MPUj99fzFDa3BxJU-8ydQJtLHM9Rm9K7M5bhCVlipYhDqZZz3u3Lve6D9QtEIJs-lrg3y-8F2DRXuj_6I2vLqEQvymYxUlnrZvKnYedXoli7j_bZPuflt9gKPgNJzBeyH-A6vLB0CqRqGhF1wNI6SDXyQPYME3FKVX1XuzXdL0l-2kEbaDPgOd7iBx0hN3BP5TsHc3dZKorLl7EQqo_1gIJXJo07-Kan8VfR1qw-jFxn_O_D4OqWA0dvXBSvRP8HIMGrU6Kvgoft2XrGtSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید پرزیدنت ترامپ دیس به خبرگزاری هایی که اجازه ورودشون‌به کاخ سفید رو نداده
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23632" target="_blank">📅 20:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yzw1wsT6BoT3ZGl1pimPphgO_iFqY-0bEcoOggUhKGvSZ3kJXWwSdZa4WwJLwN6ceLrYgZw34JxfIFjGs0KvdhDnoE0q9_9HvIgA-zHpQ1NNiUOq2Y9XpPzO3P8ExHta7sQeA55Eek7fc0nvLUcmnDAzp_WvJZHKM1wmj6xk10NwxG53HChxNpA7zGlTEq-cw52BUxUZR280cSRuP-gQwzbcHoPLNJaKxROmEvQ1APY297-pZyojMkFZld9N91Lu3Bbx5v1-zqD9SMu5lnStUI9RoddfVopKFRcORdpuaoefxRAom2JNjlstm5SBOfpJNhh8FYcxJ2HdQ08RpfkN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو سال پیش، در همین ساعت، تروریست عبد القادر و تعدادی از رهبران جنبش مقاومت، به هلاکت رسیدند. این خبر، ضربه روحی شدیدی به حسن خرسی، وارد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23631" target="_blank">📅 20:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دیدار وزیر خزانه‌داری آمریکا و معاون نخست‌وزیر چین در نیویورک:
اسکات بسنت، وزیر خزانه‌داری آمریکا، با «هه لی‌فنگ»، معاون نخست‌وزیر چین، در نیویورک دیدار کرد.
این نشست در آستانه
دیدار احتمالی دونالد ترامپ و شی جین‌پینگ
انجام شده است. بسنت درباره این دیدار گفت مذاکرات دو طرف به
زمینه‌سازی برای پیشبرد منافع اقتصادی آمریکا و دستیابی به نتایج ملموس برای مردم این کشور
کمک می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23630" target="_blank">📅 20:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23629">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الکس پلیتساس، تحلیلگر امنیت ملی CNN:
به من گفته شده جلسه
دونالد ترامپ در کمپ دیوید برای بررسی و رایزنی درباره گزینه‌های حمله به یمن
برگزار شده است. پلیتساس همچنین گفت که همزمان، سفارتخانه‌های آمریکا در کشورهای خاورمیانه که ممکن است در صورت حمله هدف حملات تلافی‌جویانه قرار بگیرند،
هشدارهای امنیتی صادر کرده‌اند
و ترامپ نیز زودتر از برنامه اعلام‌شده به کاخ سفید بازگشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23629" target="_blank">📅 20:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23628">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : مایلم با پزشکیان در حاشیه اجلاس سازمان ملل دیدار کنم @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23628" target="_blank">📅 20:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23627">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول   اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن  https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23627" target="_blank">📅 20:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23626">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23626" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23625">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول   اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن  https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/23625" target="_blank">📅 20:04 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23624">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DGj1GnW8uPxWnMYf_EOwTfgVlZQumP1KA4BplRbMRwjnL2-mjjwuJzGo8wzZGn6SWWfTTlCpaVP3LSU2LPm-yoge2OPOC6kaQCSweHjTXk3nKLfNJsCVkrHSdIpOrAMHUjh6jVxupyudpD9kb9WMpLcrdZwonxieHAtBXhuQqAmYo7iZuVv8aAVYovyb8kBzM7dILHIn5ilkDmQIHrcoq72jqp67RqL4aC9M3-iPCpkOXILh4mZhyJK5-2mZ5LU6YJuqkGF4Zf0BzMfRIVKI7fF_515zgKVlGM0Tb5OnazqPRxWZj-nwU7nHavc19Y7fH4e544VdgpdG3Dt4_NbHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : فرمول
اگه دلت تنگشده شده برای اتاق جنگ کامنت کن بگو،  پستم برا همه بفرست و اد استوری و کارای اداری رو بکن
https://www.instagram.com/reel/Ddg_S1cI4zx/?stkn=c2hueTJ1bmoybXI5</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/23624" target="_blank">📅 19:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23623">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23623" target="_blank">📅 19:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23622">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zld0KUsrW7o2gZb4Po7xZ68AD8Qj5u-qCkKto9vwiZzlLqSaz9z2LzAit6iXx7QVZn552ehdWbXNHGGiPBKeRyBVo-B_1f-AAXvS7ZX7dkIp8lw7vglNJOOgqsbZPP3S_V8hqILKE5Gm72KX6nMuajYk0Ep7h3jp-YLya-ykC_CA66UXCQnh38kZ5F3PdIC2zD-OfKpE_Ja9KbdSkyB_7rXwwlgGrrNnIK6CX8Z__m8gEKXmFYjOkV9jG1DaoLsX7xuBOeMlx4Zwj2tAMw-DMorwGsX4piSU02jqvU5rtDSTpb42YLEO-OiIWdbTEK7VOYtkaQC3PB-Ohu8u2NugsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارسالی از خرم آباد لرستان ، وضعیت امنیتی در سرتاسر این شهر
البته کل ایران همینه و حکومت پاپیون کرده
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/23622" target="_blank">📅 18:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23621">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_XPiYBa2gRVT2JmHePpQNlysyaWNGhgFHNFke_L6wLvR6FaUKl-CfxouGO8fdHLRHtAGJJXydVKWz3on0wvL4XI1U98hukbbVEGN53EUfZ_yudQRXlcf4sQZwsSK_RrrAUNYV-t9cYn50EmErdgC-WRFSqS5_bekUNZ-j8N5WOvsnpcOQBMFqtevUgwzUtixG_KfeWTx1zC0ECAJvJbdU3C8U_dcrwN7eGwsBAL3UBHomDRdYhcuSpN6-T0nbzINh8I2PoQF228em1bnRVnagWiLh35Stby07Fq3VUlRxGb-KmLHZkRBCzmnxjOg9UB_MW0ShCp_HafgzJ-NCtkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام
:
نیروهای آمریکا در چارچوب
محاصره بنادر ایران، مسیر ۱۰۹ کشتی تجاری را تغییر داده‌اند.
این آمار نسبت به آخرین به‌روزرسانی سنتکام در روز جمعه،
۴ کشتی افزایش یافته است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23621" target="_blank">📅 18:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23618">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eeb6a24e5.mp4?token=esYskLnZge85JvfTOZFEDCdKfhalw7eZ01iQEjMdUXStjak9ncE6twv8tHo17sWsvaPKeTf9PInBlwQTw1OVXnPJ--5l-puxFJNFteiG0DT7ssLrVhNyRY9r1-v9AmIe6ggEZ5LK6CLIRf1vAX1RFlU-PRroCvbV6IOSE7cOU6_CuiMtJoBQKv6Y7dRuX6VqJnzAjbRolcLJ0DdUiYiI_cwFAQV0TRedppksA0L532XGMrzPabY-WgLAmHBjt9pP4FwM64ut69iGAOwe4OhnLFYlgI-ebGB-rVoi3EVWasKnVothhKN4Z6qcbioA2kW9ySYIteU757D-Y77tMyIyOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eeb6a24e5.mp4?token=esYskLnZge85JvfTOZFEDCdKfhalw7eZ01iQEjMdUXStjak9ncE6twv8tHo17sWsvaPKeTf9PInBlwQTw1OVXnPJ--5l-puxFJNFteiG0DT7ssLrVhNyRY9r1-v9AmIe6ggEZ5LK6CLIRf1vAX1RFlU-PRroCvbV6IOSE7cOU6_CuiMtJoBQKv6Y7dRuX6VqJnzAjbRolcLJ0DdUiYiI_cwFAQV0TRedppksA0L532XGMrzPabY-WgLAmHBjt9pP4FwM64ut69iGAOwe4OhnLFYlgI-ebGB-rVoi3EVWasKnVothhKN4Z6qcbioA2kW9ySYIteU757D-Y77tMyIyOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز:
پدافند هوایی در اربیل، مرکز اقلیم کردستان عراق، یک پهپاد را در نزدیکی فرودگاه بین‌المللی اربیل سرنگون کرد.
فرودگاه اربیل محل استقرار نیروها و تأسیسات ائتلاف به رهبری آمریکاست و در ماه‌های اخیر بارها هدف حملات پهپادی قرار گرفته است.
هنوز مشخص نشده این پهپاد متعلق به چه طرفی بوده و آیا قصد حمله به فرودگاه یا نیروهای آمریکایی را داشته است.
همچنین تاکنون گزارشی از تلفات یا خسارت ناشی از این حادثه منتشر نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23618" target="_blank">📅 18:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23617">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9165e4cc1c.mp4?token=IAGbxoYXL9xM8YvgYVpNKoC7-cjf1cpTu1XaUpKgCYb5VdU_h7YSKhg1_ExK8IC9ObA2dpMTv_cgOXw3JIhJ2luPTEtwpOxRiTexCUsYgHuTvnkNBW3n9g8ZS1OyEu4o4ww56CR1xufxt9Zg-CjZP2gw2ka0dXQyic_ZxNLjhMhUOkjQf6qBpbsvlq4PDjim3EmIIunUOWCogqQk23XlmOv6oKkfHOVJEt0i580Rzd9-rXvKoUQG1juslwVbeKRLBV-dVnY5ocNv3fp3nojgo-O7J8gf3EAPJO1KoZLU6gNkTpk6u8-5BwRmg7SSnt2KG34uK3bXKFPBCuiuXwRAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9165e4cc1c.mp4?token=IAGbxoYXL9xM8YvgYVpNKoC7-cjf1cpTu1XaUpKgCYb5VdU_h7YSKhg1_ExK8IC9ObA2dpMTv_cgOXw3JIhJ2luPTEtwpOxRiTexCUsYgHuTvnkNBW3n9g8ZS1OyEu4o4ww56CR1xufxt9Zg-CjZP2gw2ka0dXQyic_ZxNLjhMhUOkjQf6qBpbsvlq4PDjim3EmIIunUOWCogqQk23XlmOv6oKkfHOVJEt0i580Rzd9-rXvKoUQG1juslwVbeKRLBV-dVnY5ocNv3fp3nojgo-O7J8gf3EAPJO1KoZLU6gNkTpk6u8-5BwRmg7SSnt2KG34uK3bXKFPBCuiuXwRAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس نیوز
:
برخی از مقامات ایرانی مانند موش‌صحرایی پنهان شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23617" target="_blank">📅 18:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رئیس ستاد کل ارتش اسرائیل:  نیروهای ما در تمام جبهه‌ها در آماده‌باش کامل، مستقر و آماده هستند
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23616" target="_blank">📅 17:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ به فاکس نیوز : ایالات متحده با حوثی‌ها در ارتباط مداوم است و آن‌ها موافقت کرده‌اند که با ما وارد جنگ نشوند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/23615" target="_blank">📅 17:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ترامپ به فاکس نیوز: با وجود هشدارهایی که به شهروندانمان در سراسر منطقه داده‌ایم. این هفته با هفته‌های دیگر در خاورمیانه تفاوتی ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/23614" target="_blank">📅 17:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دونالد ترامپ به شبکه فاکس نیوز گفت: برخی از مقامات ایرانی پنهان شده‌اند و نمی‌توان افرادی را پیدا کرد که قادر به انجام یک توافق باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23613" target="_blank">📅 17:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپبه فاکس‌نیوز: من در حال حاضر در "حالت تصمیم‌گیری" هستم و اتفاقات بسیار مهمی در آینده‌ای نه چندان دور رخ خواهد داد. انتخاب‌ها اینها هستند: نابودی ایران، اجازه دادن به فروپاشی اقتصادی آنها، یا امضای یک توافق. آنها باید رفتار بهتری داشته باشند! @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23612" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23611">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3cbef80a4.mp4?token=lDKqmYixifEU-XxMlBljbA2oDjLnfrPXLFIYyWgSkQz9J8icqDQnRLotZTT7rjWXGwoUTsXHxoToX6jP1Mbfxo9oZKt7ewEJeuf_2yMQHKINFXYarI28XTkcj5K72ggCy0IsCV_AaE8HQbGsPaArtnZ7j7EdplWqE_cneuAprvL45ZEP5qfjwYi29CH7zKCrTj5QpnaHo3joBRXAwT2DTWAXf8H_zpuPcT_kAcHbux4vNhPwc3RxHvJnJZ4T5baGEDhSEYKS7wpbwO1EyzAdVuZgRPygPyGbuVcne1mEU-ALXeVHH6wGuWvHCjS07HAGY7Ehvw945o0E8jZWrvJjUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3cbef80a4.mp4?token=lDKqmYixifEU-XxMlBljbA2oDjLnfrPXLFIYyWgSkQz9J8icqDQnRLotZTT7rjWXGwoUTsXHxoToX6jP1Mbfxo9oZKt7ewEJeuf_2yMQHKINFXYarI28XTkcj5K72ggCy0IsCV_AaE8HQbGsPaArtnZ7j7EdplWqE_cneuAprvL45ZEP5qfjwYi29CH7zKCrTj5QpnaHo3joBRXAwT2DTWAXf8H_zpuPcT_kAcHbux4vNhPwc3RxHvJnJZ4T5baGEDhSEYKS7wpbwO1EyzAdVuZgRPygPyGbuVcne1mEU-ALXeVHH6wGuWvHCjS07HAGY7Ehvw945o0E8jZWrvJjUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/23611" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23609">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌ @WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23609" target="_blank">📅 17:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23608">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ به فاکس‌نیوز : گزینه‌های فعلی روی میز، محو کردن ایران، رها کردن آن به پوسیدگی اقتصادی یا رسیدن به توافق است.‌‌
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/23608" target="_blank">📅 17:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23607">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه های عبری : انتظار می‌رود ظرف چند ساعت آینده حمله‌ای قابل توجه از سوی آمریکا به «کوه کلنگ گزلا»در ایران یا حمله‌ای بزرگ به حوثی‌ها صورت گیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23607" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23606">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqwUuuT5JR15g5mfVDQSf0x857jGGtSe6Rt5ubghZHIA5q8D5_MvHmxJPMS-WT5JA4g_GFgAyvRGC_AUDueJjV1Uni3GkwEP6eBTpNPqwK2XUw54FjZCQUu_Y521Y9tOxmQxNUJ_f81JQ0t9B0jJpq20QghkmAo8-NHSzW8_raNNR16wB5KKwOSdt4deaDIIQmB57yy7QmuWVEGDPSTvXunAfimrFYaWl-2ctVk4GUBU3O6Pinu-Ah1orKPoCUxvXbmsnGJbvbK2kExyhKysZhf8M7CC4zqSJAhs10CyPEuesft-Y-XtrE29hskMjTlb53HMPfEvRRQ6hf3JKZnnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس تصاویر ماهواره‌ای «سنتینل-۲» داغ داغ امروز، پایگاه هوایی «العدید» در قطر مملو از هواپیماهای سوخت‌رسان نیروی هوایی ایالات متحده است.
این وضعیت نشان می‌دهد که در ساعات پیشِ رو هیچ‌گونه حمله آمریکایی صورت نخواهد گرفت، چرا که انجام چنین اقدامی این هواپیماها را در معرض خطر قرار می‌دهد.
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/23606" target="_blank">📅 16:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23605">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">معاون سیاسی پیشین سازمان صداوسیمای جمهوری اسلامی اعلام کرد که در شب ۱۸ دی ۱۴۰۴ ، معترضان آزادی خواه به ۱۳ مرکز این سازمان در شهرهای مختلف حمله کردند و مرکز
صدا و سیما جزیره کیش به تصرف
آن‌ها درآمد.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23605" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23604">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">العربیه: مذاکره‌ای در کار نیست و فقط جنگ تکلیف رو مشخص میکنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/23604" target="_blank">📅 16:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23603">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idoRr-2VMhERie9c-lI0BgscIB0b0X0uQxdYmsCurzu0Qqv3IqUZr8nYjtHaoqgPBwI4rxY03anPtlPLD_TepxkOY3Ly7ZKMLv-YYucOGtwtye8_ogPUaS-eqXbXVHSqgB0-DzCULROj-LgJ4JyIqrT6J9QroAyc4qDIiE_01mUs1arEq0uCwiGACEX8dx5yawdAwcATnBt7xRSNWWjbsnKRXs1WRC12L8NIA3avM2WTN8Q8MOfrExSdRPsk-ixkVpbds6O0OLZXegWHKoIL56gZfwn7UeQamWFZ9CbG1eWkGjys7BlcNjOOnK7ZQ_OKwWmbjzlpNamTijIZ3D8iXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
:
به درخواست جدی ارتش آمریکا و با هدف حفظ امنیت ملی، موافقت کرده‌ام که
طاق پیروزی باشکوهی
را که طرح ساخت آن از دوران جنگ داخلی آمریکا، سال‌ها پیش، مطرح بوده و در
میدان مدور مجاور پل یادبود آرلینگتون
قرار دارد، به یک
مجتمع نظامی درجه‌یک و طاق پیروزی
تبدیل کنیم؛ مکانی برای استقرار و نگهداری و همچنین امکان استفاده سریع از
تعداد زیادی پهپاد
، به‌علاوه
تک‌تیراندازها روی سقف و در محوطه میدان
و همچنین نگهداری و ذخیره
مقادیر زیادی مهمات تک‌تیرانداز
.
هیچ تأسیساتی مانند این در هیچ جای دنیا وجود نخواهد داشت.
از میان ۵۹ شهر و پایتخت بزرگ،
واشنگتن دی‌سی تنها شهر در جهان است که طاق پیروزی ندارد، اما حالا خواهد داشت و با فاصله، بزرگ‌ترینِ همه آنها خواهد بود!
از توجه شما به این موضوع سپاسگزارم.
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23603" target="_blank">📅 15:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23602">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106a710ba4.mp4?token=JweWigWxlwVbwdRuLMivDTsKKLMgqO8UroD3RWN_gASFvQj8wfOaQVSYVZW1mVJLzHnxEDtVtXhCy3f7OfyeoFHZtU4hqEuFBQNk1FP3gnGYv8duGHHuhwmsdaGzpNfQdkiP7u5T9OTbxfDVxLHGFZ7UZEndrMH7cOkmTS0veXAqfdbR3P_FRUO1yY-ea2n9m_XwM13fFnezSlPwXZtgbeCqLWsoDMnOj8mw-lTq_pIPaF_AAdOS0XWrHrFA127aw-RwsNaDJsFtevO3_9hR0xLFNRJ2VCkfppY2vtPQW566-BNsLur1aGwwk7osG77cA1w5NveWgsLna6Mu7i4Dfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106a710ba4.mp4?token=JweWigWxlwVbwdRuLMivDTsKKLMgqO8UroD3RWN_gASFvQj8wfOaQVSYVZW1mVJLzHnxEDtVtXhCy3f7OfyeoFHZtU4hqEuFBQNk1FP3gnGYv8duGHHuhwmsdaGzpNfQdkiP7u5T9OTbxfDVxLHGFZ7UZEndrMH7cOkmTS0veXAqfdbR3P_FRUO1yY-ea2n9m_XwM13fFnezSlPwXZtgbeCqLWsoDMnOj8mw-lTq_pIPaF_AAdOS0XWrHrFA127aw-RwsNaDJsFtevO3_9hR0xLFNRJ2VCkfppY2vtPQW566-BNsLur1aGwwk7osG77cA1w5NveWgsLna6Mu7i4Dfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی : موشتبی مفقود است
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23602" target="_blank">📅 15:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23601">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJdUD4byOgvn7w9YC2uITA5KPOolleFMBMSiLdGCFA4P-r1vQw5b2MTh_G6HJAJvPM4vqBUJul05vHb36bV4ysNE4Y8oMCc1Cmn10T1vjgp_AI9scnPudGh6ZkgmYbaJBwgw9fn4NN7UvDlq5GzEo-BlPY1nR-HEOt30DAeCVssP7gMqrDY41illG7f85csQ9XLSKAzqp2ZrdQO8qMyEfS32QSLkpD4WRomO6GMKHsZk7xKuqFMwzKzKWL6hr33r4XFgbGTwNEELWTwVgx7Bh6S-bwfhXrXrOVUUsxOt23efsMJ73CXl5bLeNFrPNaeLOqZvY4EYCCWLeBQNbxXXIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن در جزیره گوام مشاهده شد
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23601" target="_blank">📅 15:44 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23600">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز: Anthropic به‌صورت مخفیانه یک آزمایشگاه زیست‌شناسی در منطقه خلیج سان‌فرانسیسکو راه‌اندازی کرده است. این شرکت هوش مصنوعی در حال گسترش فعالیت خود به زیست‌شناسی فیزیکی و استفاده از هوش مصنوعی برای پژوهش‌های دارویی و زیستی است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/23600" target="_blank">📅 15:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23599">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مهر: ایالات متحده مجوز لازم را از چندین کشور منطقه برای از سرگیری جنگ گسترده علیه ایران دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/23599" target="_blank">📅 15:41 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23598">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">کوین‌دسک:
بیت‌کوین بالای ۸۰ هزار دلار باقی مانده و بازار رمزارزها پس از افت‌های اخیر دوباره تقویت شده است.
در آخرین موج صعودی گزارش‌شده، اتریوم حدود ۷.۳ درصد، XRP حدود ۸.۹ درصد و سولانا بیش از ۱۲ درصد رشد کردند و ارزش کل بازار کریپتو به حدود ۲.۶۶ تریلیون دلار رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/23598" target="_blank">📅 15:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23597">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">صداوسیما: حمله به ایران قطعی است و در وضعیت آماده‌باش هستیم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/23597" target="_blank">📅 15:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23596">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبر گزاری صدى‌البلد:
جان راتکلیف، رئیس سازمان سیا، به‌طور ناگهانی وارد قاهره شد و با عبدالفتاح السیسی، رئیس‌جمهور مصر، دیدار کرد.
طبق این گزارش، دو طرف درباره همکاری‌های اطلاعاتی و امنیتی و همچنین
بحران ایران و تحولات امنیتی خاورمیانه
گفت‌وگو کردند. جزئیات بیشتری از این سفر اعلام نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23596" target="_blank">📅 15:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23595">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">محسن کج بند رضایی در گفت‌وگو با الجزیرة:
اگر جنگی دوباره آغاز شود، کشتی‌های آمریکا حتی اینکه اقیانوس هند را ترک کنند ، در هر نقطه‌ای از این اقیانوس که باشند، هدف حمله قرار خواهند گرفت..
ما سرعت موشک‌های هایپرسونیک خود را از ۶ ماخ به ۱۰ ماخ افزایش داده‌ایم.
همچنین سامانه‌های جنگ الکترونیک خود را توسعه داده و پدافند هوایی‌مان را ارتقا بخشیده‌ایم؛ علاوه بر این، تاکتیک های دیگری نیز در اختیار داریم که در زمان مناسب از آن‌ها استفاده خواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/23595" target="_blank">📅 14:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-23594">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتانیاهو: نیروهای امنیتی ما در حال حاضر در تعقیب مهاجمی هستند که حمله را در بنیامین انجام داد. هیچ مهاجمی در امان نخواهد ماند، همچنین کسانی که به آنها کمک کرده‌اند. ما همه آنها را در غزه، لبنان، یهودا و سامریا پاسخگو خواهیم کرد. همزمان، نیروهای ما یک مهاجم…</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/23594" target="_blank">📅 14:41 · 29 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
