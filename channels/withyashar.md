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
<img src="https://cdn4.telesco.pe/file/h_2uEUoCUNwm8N2a-Xe0F9KSjdnhU2r95Rd7VMfGAL0QOJpW1sVf-MnqG3fGiCj44jJeZpIfOo-2Pw0urnptWG4DUy-QXL66X5upAuAR4iA0ItOFj0RH7crQmINdDgE1VDIZemVGQor59XL5xLYOERv-zcl5UIGN1uGyDws4EJU_40a_Cl7BmbO8wHSa8eGYKmbvb7B02El6CCI58-g2mH5VHpver2f_YClrt5zQKZAHVhqZJbxC2nvSCP5wlt8ogCbumLN0I06tOp2XEb9VXT7sqLRjiCSFx4lRJ_gQpHuGePrmOw9uTC54_k0PC2BWlBB203yqFlNtjFgZBkfSwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 266K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 17:22:08</div>
<hr>

<div class="tg-post" id="msg-11657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ریکلین فاش خبرنگار اسرائیلی:
نیروهای ویژه ارتش اسرائیل دارن برای نفوذ به تأسیسات هسته ایی اصفهان تمرین می‌کنن تا اورانیوم غنی‌شده رو خارج کنن
مواد هسته‌ای اون‌قدرا هم عمیق دفن نشده و بعد از ورود به سایت، میشه منتقلش کرد
@withyashar</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/withyashar/11657" target="_blank">📅 16:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a861c5aeb.mp4?token=Zr07SYcb1Vg9jqp-WBAgYQFI2AI4GnSC-lzMEmFpdgGWtBPME4PKmsXCcd1Zb247R3t2JyumcgD4DhI-0MAgZnQKgN-QufL7geCGMkPMwyHXe9kHCGMDz8FYE-46PiCz--lEcGZXiCqqutLjanD3TSnheR9tSojUsf5lfJ6J3jCJuM751dVdSu5yYuVkfQxHJz7NR0hrtDMXLXoLV6hyjVxW-7TS93xelkWd9hVWXbmP97aIlTwXaokyYwFfcGq7HgKBS6WX5BRl6k-jJIEmIhxlOiq8tsm2XESUYemwu5X_6tHzslUsrma-b6YhsBJDapILKE9uTxUjyJVrhALMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a861c5aeb.mp4?token=Zr07SYcb1Vg9jqp-WBAgYQFI2AI4GnSC-lzMEmFpdgGWtBPME4PKmsXCcd1Zb247R3t2JyumcgD4DhI-0MAgZnQKgN-QufL7geCGMkPMwyHXe9kHCGMDz8FYE-46PiCz--lEcGZXiCqqutLjanD3TSnheR9tSojUsf5lfJ6J3jCJuM751dVdSu5yYuVkfQxHJz7NR0hrtDMXLXoLV6hyjVxW-7TS93xelkWd9hVWXbmP97aIlTwXaokyYwFfcGq7HgKBS6WX5BRl6k-jJIEmIhxlOiq8tsm2XESUYemwu5X_6tHzslUsrma-b6YhsBJDapILKE9uTxUjyJVrhALMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : ‏هزاران آمریکایی شجاع در لباس نظامی همچنان در سراسر خاورمیانه خدمت می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/withyashar/11656" target="_blank">📅 16:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده: 88 کشتی را در جریان محاصره دریایی ایران مجبور به تغییر مسیر کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/11655" target="_blank">📅 16:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ارتش اسرائیل : در ساعات اخیر،  ۲۵ انبار و سکوی پرتاب موشک متعلق به حزب‌الله را در جنوب لبنان نابود کردیم
@withyashar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/11654" target="_blank">📅 16:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک منبع آمریکایی به الجزیره:
بحث امنیتی که برای امروز در کاخ سفید درباره ایران برنامه‌ریزی شده بود، پس از اعلام ترامپ مبنی بر تعویق حمله برنامه‌ریزی شده، به تعویق افتاد
@withyashar</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/withyashar/11653" target="_blank">📅 16:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زلزله لرستان 4.6 ریشتر
@withyashar</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/withyashar/11652" target="_blank">📅 16:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رئیس روس اتم: قادریم برنامه بازگرداندن کارکنان نیروگاه بوشهر را اجرایی کنیم
@withyashar</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/withyashar/11651" target="_blank">📅 16:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سازمان عفو بین‌الملل اعلام کرد تعداد اعدام‌ها در جهان طی سال 2025 به بالاترین سطح در 44 سال گذشته رسیده.
طبق این گزارش، جمهوری اسلامی اصلی‌ترین عامل افزایش آمار اعدام‌ها در جهان بوده.
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/11650" target="_blank">📅 16:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رویترز: پیشنهاد جدید ایران به آمریکا برای پایان درگیری‌ها :
- عقب نشینی نیروهای آمریکایی از منطقه
- پرداخت غرامت توسط آمریکا
- رفع تحریم‌ها
- آزادسازی اموال بلوکه شده توسط آمریکا
- پایان محاصره آمریکا علیه بنادر
@withyashar</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/11649" target="_blank">📅 15:57 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">معاون امنیتی استان خوزستان :
امروز داشتیم پدافند هامونو تست میکردیم که به اشتباه  یکی از پرتابه ها خورد به یک ساختمون مسکونی و چندین نفر زخمی شدن.
@withyashar</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/11648" target="_blank">📅 15:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">افشاگری وال‌استریت ژورنال :  چند مقام خلیج فارس از برخی کشورهایی که ترامپ به آن‌ها اشاره کرده بود گفتند از طرح قریب‌الوقوعی که او درباره حمله به ایران توصیف کرده بود، اطلاعی نداشتند.
@withyashar</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/11647" target="_blank">📅 15:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">poshte-pardehaye-enghelab (@withyashar).pdf</div>
  <div class="tg-doc-extra">3.7 MB</div>
</div>
<a href="https://t.me/withyashar/11646" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کتاب ممنوعه «در پشت پرده های انقلاب»، اعترافات «جعفر شفیع زاده» فرمانده پیشین واحد مخصوص انقلاب اسلامی ایران و محافظ آیت الله خمینی در نوفل لوشاتو و تهران.
@withyashar</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/withyashar/11646" target="_blank">📅 14:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مهر: تو قشم صدای انفجار شنیده شد
@withyashar</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/withyashar/11645" target="_blank">📅 14:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دادگاه نتانیاهو امروز به دلایل جلسات امنیتی بازم لغو شد.
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/11644" target="_blank">📅 14:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">😾</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11643" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سخنگوی ارتش: ارتش ایران، دوره آتش بس را به منزله دوران جنگ تلقی کرده و از این فرصت برای تقویت توان رزمی خود استفاده کرده است.
اگر دشمن حماقت کند و مجدداً در دام اسرائیل گرفتار شود و دست به تجاوزی دیگر به ایران عزیز ما بزند، با ابزارها و شیوه‌های جدید جبهه‌های جدیدی را علیه آنها خواهیم گشود.
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/11642" target="_blank">📅 13:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اتاق جنگ با شما : پالایشگاه بندرعباس تخلیه شد همین الان
@withyashar</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/withyashar/11641" target="_blank">📅 13:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/withyashar/11640" target="_blank">📅 13:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eae116ed9.mp4?token=OkMMMfpxiIhR9T1nbUnjgFHKYNBJQOS5ujxje-HkFGqGqwRH8aLWuFqoKe0jt640dQtAdcMTw9b37TvG5NpktNGHCNZujKT_pHvqFHttdvifMidJJP9XQDy2f9hPZD37ni1zJIn8cALUyKWyyZt1TflDPuRbMDqkSSdtrDNXiHJ60oCltCXxW0ZgBk7XKBUSCXlAshSS48BgQm3HMZOuzHI5v7xd7j3SmVy8ttglVvmdfJp_4pxD8mT2GwKDyZZXKJgFBKIxHexWeuvlTP3jt3HRgEGXUwnTAKZd0zf2gEOzBX3RFDdNEsu3Wjs2qEDTG_-QD0xsCCEnzwGrdxIlOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eae116ed9.mp4?token=OkMMMfpxiIhR9T1nbUnjgFHKYNBJQOS5ujxje-HkFGqGqwRH8aLWuFqoKe0jt640dQtAdcMTw9b37TvG5NpktNGHCNZujKT_pHvqFHttdvifMidJJP9XQDy2f9hPZD37ni1zJIn8cALUyKWyyZt1TflDPuRbMDqkSSdtrDNXiHJ60oCltCXxW0ZgBk7XKBUSCXlAshSS48BgQm3HMZOuzHI5v7xd7j3SmVy8ttglVvmdfJp_4pxD8mT2GwKDyZZXKJgFBKIxHexWeuvlTP3jt3HRgEGXUwnTAKZd0zf2gEOzBX3RFDdNEsu3Wjs2qEDTG_-QD0xsCCEnzwGrdxIlOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب اتمی کره شمالی
@withyashar</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/withyashar/11639" target="_blank">📅 13:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">من سریع خوندم فک کردم میگه پاکستان میده به اونا ، در جواب پس یه ویدیو میبینیم با هم</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/withyashar/11638" target="_blank">📅 13:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">عمو اینکه جمهوری اسلامی به پاکستان گفته که ما سه تا بمب اتم داریم ، اگر حمله ای صورت بگیره کشور های همسایه پودر میشن واقعیه؟ ازشون واقعا برمیاد همه چی.</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11637" target="_blank">📅 13:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآژمان</strong></div>
<div class="tg-text">عمو اینکه جمهوری اسلامی به پاکستان گفته که ما سه تا بمب اتم داریم ، اگر حمله ای صورت بگیره کشور های همسایه پودر میشن واقعیه؟
ازشون واقعا برمیاد همه چی.</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/11636" target="_blank">📅 13:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">روزنامه واشنگتن پست به نقل از یک مقام پاکستانی: ایران می‌خواهد پیش از اعلام توافق هسته‌ای، به توافقی برای پایان دادن به جنگ دست یابد.
واشنگتن می‌خواهد توافق بر سر همه مسائل را یکجا اعلام کند.
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/11635" target="_blank">📅 13:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4f3a4b15.mp4?token=f0qYrmrT4c9d0EyjP8zr68fiutPo8P4Ai_Aoql3cLccksTqX9teKel5r78bnxcLm52Nk61kIhSbIWpKmwtlZUBeHB2ggOiVgCmGg7gGhkX916XiCGdmB9ikNxaHZtR23Raa3udJZtS1o9uY-omHTPcdQMYVa9O26oOq6dKVoxNZm3QV1i4MQiuOLV265PQzSZaFDsq_EqpcBqXmvzc4P6qRasm5y4Wg02PCf_eWk94O7oVYodGscPTb53hLvn4esN3QqjWVEK5VhMowgi36Q9g1gfrzGOxEPXbZs_-gJaRGONdJtWLcDYbKH91vqV7OygqVbjyfckUH1DXRyfifNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4f3a4b15.mp4?token=f0qYrmrT4c9d0EyjP8zr68fiutPo8P4Ai_Aoql3cLccksTqX9teKel5r78bnxcLm52Nk61kIhSbIWpKmwtlZUBeHB2ggOiVgCmGg7gGhkX916XiCGdmB9ikNxaHZtR23Raa3udJZtS1o9uY-omHTPcdQMYVa9O26oOq6dKVoxNZm3QV1i4MQiuOLV265PQzSZaFDsq_EqpcBqXmvzc4P6qRasm5y4Wg02PCf_eWk94O7oVYodGscPTb53hLvn4esN3QqjWVEK5VhMowgi36Q9g1gfrzGOxEPXbZs_-gJaRGONdJtWLcDYbKH91vqV7OygqVbjyfckUH1DXRyfifNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم جدید ..
😂
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11634" target="_blank">📅 12:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">صدای شدید پدافند دزفول اینم حتما پدافند کنترل شدست چیزی‌ نیست
😂</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11633" target="_blank">📅 11:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کمی پیش صدای انفجار و ستون دود در پادگان موشکی ۱۵ خرداد اصفهان @withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/11632" target="_blank">📅 11:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">@withyashar
part6</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11631" target="_blank">📅 11:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دیشب خود گوهشون گفتن فردا اصفهان صدا میشنوید</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/11629" target="_blank">📅 11:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFereshte A</strong></div>
<div class="tg-text">دیشب خود گوهشون گفتن فردا اصفهان صدا میشنوید</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11628" target="_blank">📅 11:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76652a92a4.mp4?token=fCzDlZ_d1y1K7r-WsTMUTYTCYyHBKFH4oXQF7qTo3pLJskUdI1MlW0srkVU5I3Skwrtk5XaMegHKJQuy9GRrxx2qwvJm8hxCtr1Sgwm8HWXseE8nAcNlB4wAf_CeCev6ztKb-CSaoX-fLYwqFj65mxVPR8u5AWUNs0SWGXGQJd2gHaHIsycQhjYyyGN9n52ffP5b-pcFwjj3uhURUlWPRASTPBuPYFR10I6F5SUsvl65ZIWAUgejGsST7RRZ3HaHpDWh2FYfTg2ljt0XP9P5ZvY7znKeF98AKD1K_zSZHHKLa17J3sgcDcDE9-Y0QygLj6SF9dl_5HJvqMsHPc7Onw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76652a92a4.mp4?token=fCzDlZ_d1y1K7r-WsTMUTYTCYyHBKFH4oXQF7qTo3pLJskUdI1MlW0srkVU5I3Skwrtk5XaMegHKJQuy9GRrxx2qwvJm8hxCtr1Sgwm8HWXseE8nAcNlB4wAf_CeCev6ztKb-CSaoX-fLYwqFj65mxVPR8u5AWUNs0SWGXGQJd2gHaHIsycQhjYyyGN9n52ffP5b-pcFwjj3uhURUlWPRASTPBuPYFR10I6F5SUsvl65ZIWAUgejGsST7RRZ3HaHpDWh2FYfTg2ljt0XP9P5ZvY7znKeF98AKD1K_zSZHHKLa17J3sgcDcDE9-Y0QygLj6SF9dl_5HJvqMsHPc7Onw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کمی پیش صدای انفجار و ستون دود در پادگان موشکی ۱۵ خرداد اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11627" target="_blank">📅 11:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4df8f056.mp4?token=HQLvxa90_EieGJhl76tII2DG_bYk7LVhuA_8ZTAK1VbbgHHzibd-v13quuFZKxrpT5Gln4kCOsVKFlRholYN9VqESKw3WbjbCe70NFGZFtox-OZxqpgTbCYckwmrHN0G6VVLYwafvgSZ-AyQEK1pDIBkcUP4iLRB3Fk21q4mTdQ1HXPQEcWrJ1phhOPIiwxlf8KgYwo-PwFjNeNCC3qdYjbUT9BVN1YcJJvLg8FQybjp2X_0dfljzwuC41Q7cgYVa6PAoeNJq_ZeTV6UL5SOsKHWjSCdDPu9tsSEWOl_zoSQunDlwDZL_kYioseUFQHoq1EvnRpfJv-bKoH3y3Vi7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4df8f056.mp4?token=HQLvxa90_EieGJhl76tII2DG_bYk7LVhuA_8ZTAK1VbbgHHzibd-v13quuFZKxrpT5Gln4kCOsVKFlRholYN9VqESKw3WbjbCe70NFGZFtox-OZxqpgTbCYckwmrHN0G6VVLYwafvgSZ-AyQEK1pDIBkcUP4iLRB3Fk21q4mTdQ1HXPQEcWrJ1phhOPIiwxlf8KgYwo-PwFjNeNCC3qdYjbUT9BVN1YcJJvLg8FQybjp2X_0dfljzwuC41Q7cgYVa6PAoeNJq_ZeTV6UL5SOsKHWjSCdDPu9tsSEWOl_zoSQunDlwDZL_kYioseUFQHoq1EvnRpfJv-bKoH3y3Vi7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ با تقلید صدای ترامپ گفت وقتی ترامپ صمت وزیر جنگ را به او داد گفت : پیت، باید خیلی خشن و محکم باشی… آماده ای؟
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11626" target="_blank">📅 10:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FtBETNVfMRpgLVLqGphvJCmeRVqSsbBgxI3pPfFx4GSFOSlz_rQTiczLt48rfACH-PrMXpvWL2LNpC8jzc6xwFChl010IjEidFbAxy4LvG0_5ymGgRLZOHcQQH2mpO0Ub6lg8xShIJdCfJKLMqp1C5VfvZeFE9S1VjBZFqqUr_awqo6_3LO92DyOgJCmnzRV5d9Tk2zKPIuXZR8EOumYEj7YZegUB7PDQl_ZKj7EsG8LjCdT9RYliZcdzh7qxyKTLw7D_leBP_aVy8QPfL1KR4pT1ORt6ciRcWRUiMgDqw2gra5tUci5X_T7Fa0FWmKlz9rvEISHQxHqTrae5bsYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZDFHW1brBSkSjtjZ5nEGK471B9d_pJ4fQFrW-mt02S_b1b4OKxuAxn_Lc7PLebKXqx_Ii-w4ENE65X63Qxy6XD3lP5XC2rsjbdaCnAv9i7wTLfghDg7cotBZiPJh3lJ9BgjHJ1TYyTcVC2mfdu4sGdDrs_Sp4d4tDSkU3cBa3oYdmbeW0qb0bZyI7KxEA3-mzV1D9-GRjL-ZvSaM8jQrHDk03y9D0i4RWJd3w_M0TeqZuPmEM6Ihgmb2IjGfKziIJYE5nN75Mzyrg_ajYOZ39YOvWHURDjYhAbvWp-QwnV4ZYndbigTu0aDx8m-1HZmBRP6ESgrM3Ne6ns72Kaqvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmQfdUN4sVFAFowtHzGWGDQ5jXo02brNg3E1VTg0Trb5KJGuMSaG3HV9dduqL5f6JxIt2o9HOGkQs1m3eFJat22bHbpG1K3MkNeOkNP8SC8cg2fC-2Mz-KJdc7jjWKccXtTa7O4UFLf0JPpTkt-3pE3xKKRhBikieCUD7cnXPArW-SvPyLseW5UeyK5SUiXElcK7TKL3Hmuu-t0KX3ySL7AHyo7zgHGBbAl7VDRhTn734YhTxrzDjpXUWOGK0LS7QTSGw9uQr6r4Y3DeVXzl9XH4SrKrpKdFqX_9AFKPKfZoQIVWPsLULWwn8fzwA164YyTdF2oEc5o-cQRwbQZqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DYM8HPesj1HX9TvNbLorbQlI0zYW-XBsZpiqIXwaQ_x2SM-AX3E4h2gy28Mh_hhZietC4_UKlq9ZHuCeJfvUqpTw-a7HE-qChv1d7YGX5xis-IgdCSXWaCrD7fQEo43uHbSAAj158iDmi2ghSuDynXFpviw3qgXq6wagJDR02XG02aFpUdgukd_I6gPXgjHYX4X3cVzOiDsN0c1yOzDkezXrhNvszin3P_yBajtIm2V0H-mU2ycbS4vsgu6ksTgTgSx_CxObgnCmM0Zi7DzIU6Wycr23pPPbQqESBLn3aSfJNNw-gvaB9rIdwwvG3tJmSeF1K0F31noGTQRuTrd5lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11622" target="_blank">📅 10:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">@withyashar
⚔️</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11621" target="_blank">📅 10:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581fa30397.webm?token=X_B-Wt_f5o6OrM-kbg0cGA-XpTQDbfGWjfVTbeo-0dbtB_uUeFXMdSm7Ak4jtZXV6wUNRwh2nD9Tm4EyuD1aM3VOGjlKhtm0TJi-n9kx8RNSxfrBuh3v77Lu2a0LzcSz9_R8PELvRGoHQXs29rh4KUVltLsWTUjSzfktRGXn3CzTc9wezBH50uZ6epd0PTFv3YM_6etfmXyPDpj9EGKG8fCdRs4lQOM19MKjzoHWfIcFU4KCijRlBibImW6PCVJ3E0jUH3yrpuuhdl_z0qNDxjQiiNrlnoalNsyWMTwVESa7YlwnXtNKgYkVRzbyxJFniWW3b9UYlvlLWC3n754ngA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581fa30397.webm?token=X_B-Wt_f5o6OrM-kbg0cGA-XpTQDbfGWjfVTbeo-0dbtB_uUeFXMdSm7Ak4jtZXV6wUNRwh2nD9Tm4EyuD1aM3VOGjlKhtm0TJi-n9kx8RNSxfrBuh3v77Lu2a0LzcSz9_R8PELvRGoHQXs29rh4KUVltLsWTUjSzfktRGXn3CzTc9wezBH50uZ6epd0PTFv3YM_6etfmXyPDpj9EGKG8fCdRs4lQOM19MKjzoHWfIcFU4KCijRlBibImW6PCVJ3E0jUH3yrpuuhdl_z0qNDxjQiiNrlnoalNsyWMTwVESa7YlwnXtNKgYkVRzbyxJFniWW3b9UYlvlLWC3n754ngA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/11620" target="_blank">📅 10:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیویورک تایمز: در صورت ازسرگیری جنگ، ایران ممکنه تاکتیک‌های جدیدی به کار بگیره.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/11619" target="_blank">📅 09:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش فایننشال تایمز: شی جین‌پینگ، رئیس جمهور چین، به ترامپ گفته است که پوتین از تصمیم خود برای حمله به اوکراین پشیمان است. از سوی دیگر، اشاره شد که ترامپ به شی گفته است که ایالات متحده، چین و روسیه باید علیه دادگاه بین‌المللی کیفری در لاهه با هم همکاری کنند زیرا این دادگاه «سیاسی عمل می‌کند»
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/11618" target="_blank">📅 09:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/withyashar/11617" target="_blank">📅 02:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">۲۶ روز مانده تا تولد دونالد ترامپ خردادی دوست داشتنی ۱۴ ژوئن ۲۰۲۶ (۲۴ خرداد ۱۴۰۵) تهران میگیریم ؟
😬
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/11616" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11614">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ به اسرائیل اطلاع داد که تاخیر در حمله به ایران تنها دو تا سه روز است. @withyashar</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/withyashar/11614" target="_blank">📅 02:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11613">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ به اسرائیل اطلاع داد که تاخیر در حمله به ایران تنها دو تا سه روز است.
@withyashar</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/11613" target="_blank">📅 02:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پدافند کیش فعال شده
@withyashar</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/withyashar/11612" target="_blank">📅 01:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ: «ما آماده می‌شدیم که فردا یک حمله بسیار بزرگ انجام دهیم. من فعلاً آن را برای مدتی به تعویق انداختم؛ امیدوارم شاید برای همیشه، اما ممکن است فقط برای مدت کوتاهی باشد، چون گفت‌وگوهای بسیار مهمی با ایران داشته‌ایم و باید ببینیم نتیجه آن‌ها چه خواهد شد.…</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/11611" target="_blank">📅 01:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترامپ : اگر بتوانیم بدون اینکه حسابی آن‌ها را بمباران کنیم به نتیجه برسیم، من خیلی خوشحال خواهم شد
اسرائیل را از تصمیم برای تعویق حمله به ایران مطلع کردم.
@withyashar</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/withyashar/11610" target="_blank">📅 01:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11609">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پرزیدنت ترامپ :
ما به جمهوری اسلامی هیچ امتیازی نخواهیم داد. فقط تسلیم کامل!
@withyashar</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/withyashar/11609" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11608">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4912a0af33.mp4?token=qsGdwk-Pg7RV-7P3rPOHJWjsORDBTlHT3cjDRDN0630SNYlw_W39FzmgTgI4RQGWBP_mCTwFSMKfgRwUCLWXmqAs8jCR2HUm5Kg_eE8BxahBV1dNCYwvBf0m-jaH0mMxcb8y0jjccbm-XgqHlGVNwvBfYoWTSF6sVoM1QPgF0j5juO_k0IKzT8mOTJmi8VvGxqxe3DzvgcyjJG2gY_04_WmJt9eWG8WZtO1Hl_lzlJTS2SeIrLhCV4_wgj6t4BPJPZ1U75B-8UJn9E-Yrka1PrcAsGbg_oFyD09P8wZWbjWo2Ifsgc7i7IwaPzmEqM4cFXcKGzTOkQdQb4_lKefLKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4912a0af33.mp4?token=qsGdwk-Pg7RV-7P3rPOHJWjsORDBTlHT3cjDRDN0630SNYlw_W39FzmgTgI4RQGWBP_mCTwFSMKfgRwUCLWXmqAs8jCR2HUm5Kg_eE8BxahBV1dNCYwvBf0m-jaH0mMxcb8y0jjccbm-XgqHlGVNwvBfYoWTSF6sVoM1QPgF0j5juO_k0IKzT8mOTJmi8VvGxqxe3DzvgcyjJG2gY_04_WmJt9eWG8WZtO1Hl_lzlJTS2SeIrLhCV4_wgj6t4BPJPZ1U75B-8UJn9E-Yrka1PrcAsGbg_oFyD09P8wZWbjWo2Ifsgc7i7IwaPzmEqM4cFXcKGzTOkQdQb4_lKefLKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: «ما آماده می‌شدیم که فردا یک حمله بسیار بزرگ انجام دهیم. من فعلاً آن را برای مدتی به تعویق انداختم؛ امیدوارم شاید برای همیشه، اما ممکن است فقط برای مدت کوتاهی باشد، چون گفت‌وگوهای بسیار مهمی با ایران داشته‌ایم و باید ببینیم نتیجه آن‌ها چه خواهد شد.
از سوی عربستان، قطر،  امارات و چند کشور دیگر از من خواسته شد که این اقدام را دو یا سه روز به تعویق بیندازیم؛ یک بازه کوتاه، چون آن‌ها فکر می‌کنند که بسیار به دستیابی به توافق نزدیک شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/11608" target="_blank">📅 01:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامپ درباره «گفت‌وگوهای مهم» با ایران:
«این یک تحول بسیار مثبت است، اما خواهیم دید که آیا واقعاً به نتیجه‌ای می‌رسد یا نه.
دوره‌هایی را داشته‌ایم که فکر می‌کردیم تقریباً به توافق نزدیک شده‌ایم، اما در نهایت موفق نشدیم؛ با این حال، این بار شرایط کمی متفاوت است.»
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/11607" target="_blank">📅 01:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ  : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد
@withyashar</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/11606" target="_blank">📅 01:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11605">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">@withyashar
part5</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/11605" target="_blank">📅 01:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11604">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cbe97257c.webm?token=ow21k_UURToKXslPSdt-DyaFxUvGkE-6bgijzlaNX5g91HcCTlWd0HjGyjthGNPQDDyFMt3VyQLR6XmxP7dj2sAbfcUXd3OuogzmOnvxGnh0jc_P1NEZjvL1hvp3E3qdtZV4SA1GyeVznMa4OYWATLKjFBr5ETcEp259j0WVtUwNoXlk8slnp0Gl1qgNwPr7CiQIh0-oQ4ibaJlw4WIvO8ypM4luoY-CMCXBhIOKEuNLEQiyS1zbiSAt3YHNxxkC-NC2tlUITKMFTNIucQjiTvz04oH1yL8plhXbE15OA-X_dQ88wuEkd30fo7Fbxmldp0tMbVzdoGt-CodHhLmXuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cbe97257c.webm?token=ow21k_UURToKXslPSdt-DyaFxUvGkE-6bgijzlaNX5g91HcCTlWd0HjGyjthGNPQDDyFMt3VyQLR6XmxP7dj2sAbfcUXd3OuogzmOnvxGnh0jc_P1NEZjvL1hvp3E3qdtZV4SA1GyeVznMa4OYWATLKjFBr5ETcEp259j0WVtUwNoXlk8slnp0Gl1qgNwPr7CiQIh0-oQ4ibaJlw4WIvO8ypM4luoY-CMCXBhIOKEuNLEQiyS1zbiSAt3YHNxxkC-NC2tlUITKMFTNIucQjiTvz04oH1yL8plhXbE15OA-X_dQ88wuEkd30fo7Fbxmldp0tMbVzdoGt-CodHhLmXuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/11604" target="_blank">📅 01:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11603">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">علی قلهکی، ‏فعال رسانه‌ای: ترامپ شنبه‌ شب قصد حمله داشت که صبحش قطر به ایران هشدار داد و سران نظام رفتن مخفی شدن و علت عدم حمله پیدا نکردن لوکیشن سران نظام بوده. @withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11603" target="_blank">📅 01:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علی قلهکی، ‏فعال رسانه‌ای:
ترامپ شنبه‌ شب قصد حمله داشت که صبحش قطر به ایران هشدار داد و سران نظام رفتن مخفی شدن و علت عدم حمله پیدا نکردن لوکیشن سران نظام بوده.
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/11602" target="_blank">📅 00:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL5LzzSAqc8KhoMQM9JgBo5xgHarXKCFptQI7FV1QgefZBN352WDgFJDnh4QqH_jmg2TZJgX81wtCK2pcbzLNF4jifJNbJVcjuy8hB3cGDhsM7WR7I1IAgGdof7NJZP2jf3qxQeTIHF---O0SgExP381orFrC2t68-CLqgjhsT8TROz89omSSaGfnQE32kyzL-tP1qU_Yw_x8LC23k2HjWxyx_BWeaNPOY0gtifAtgcO8H9wZGfw8uYPBrLqNcM57dXSz55LSAojaDnTl-yL9MqYTII0VD2hC24e0QmasMf0_3ZV_q2PWq0yztoAVgogpjoGDL3Ss8UKupvP2-QlzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیمون ریکلین، خبرنگار کانال ۱۴ اسرائیل، امروز احتمالاً اطلاعات محرمانه‌ای را به صورت زنده در مورد عملیات‌های مرتبط با کمپین علیه ایران فاش کرد، از جمله گزارش‌هایی درباره آمادگی‌ها برای عملیات زمینی احتمالی در سایت هسته‌ای .
ریکلین گفت تمریناتی انجام شده است که شامل نیروهای کماندو می‌شود که به سایت حمله کرده و اورانیوم غنی‌شده را استخراج می‌کنند، و افزود بر اساس آنچه شنیده، این ماده در عمق زمین در اصفهان دفن نشده است و «زمانی که وارد تأسیسات شوند، می‌توان لوله‌ها را استخراج کرد.»
سانسورچی‌های نظامی اسرائیل درخواست کرده‌اند این بخش از پلتفرم‌های پخش حذف شود.
اعضای یش عتید، از جمله رام بن-باراک و الازار استرن، از بوعاز بیسموت، رئیس کمیته امور خارجه و امنیت، خواستند جلسه‌ای فوری برای بحث درباره انتشار «اطلاعات ادعاشده محرمانه که می‌تواند به دستاوردهای کمپین در ایران آسیب برساند و به آینده استراتژیک کشور خسارت وارد کند» برگزار شود.
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11601" target="_blank">📅 00:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbcee282d2.mp4?token=USRpToVgBj_C4oOZph1u8SWfCv_CyVfaTvnqo5zhmHIuMRhh03TZ0UNSyjc4WGc1qVUxWJSh-Dbn9wDwjrAjmhqfstVx1CjltX6rgx-mZnu4Fhg5KjfcyAwliukQlyhFJdc78SbgQHwuHGRH7GKwTy7iVGSoMb_cLTciKQZwvNXchv0BrgoCwyaLLQBtE4jy5q_RTNGmOIh6LU4RFm66h0AJrfjjE-NhAK_x_z5rxHUJhetJmm_L0xGHkJvdMV89maPAPcWge9GyMho18j52WJljOPJJ4v72KqJy__TJ_gn8HONCaxpLAYitcBn4apNM7_tMMp-PVb12oii0dlLoMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbcee282d2.mp4?token=USRpToVgBj_C4oOZph1u8SWfCv_CyVfaTvnqo5zhmHIuMRhh03TZ0UNSyjc4WGc1qVUxWJSh-Dbn9wDwjrAjmhqfstVx1CjltX6rgx-mZnu4Fhg5KjfcyAwliukQlyhFJdc78SbgQHwuHGRH7GKwTy7iVGSoMb_cLTciKQZwvNXchv0BrgoCwyaLLQBtE4jy5q_RTNGmOIh6LU4RFm66h0AJrfjjE-NhAK_x_z5rxHUJhetJmm_L0xGHkJvdMV89maPAPcWge9GyMho18j52WJljOPJJ4v72KqJy__TJ_gn8HONCaxpLAYitcBn4apNM7_tMMp-PVb12oii0dlLoMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/11600" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اتاق جنگ با یاشار: تحلیلگران ارشد ایرانی ۱۰ روز پیش نظرشون این بود که اگه تا ۱۰ روز آینده جنگ نشه دیگه نمیشه … این ۱۰ روز چندین ساعت پیش به پایان رسید
😬
😬
😬
@withyashar</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/withyashar/11599" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خبرگزاری «مهر»: پدافند هوایی در اصفهان به‌دلایلی نامعلوم که تاکنون مشخص نشده فعال شد.
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11598" target="_blank">📅 00:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">@withyashar
part3</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/11597" target="_blank">📅 00:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرنگار آکسیوس:ترامپ از زمان شروع جنگ حداقل 12 بار ضرب الاجل ها را تمدید کرده و حملات برنامه ریزی شده به ایران را به تعویق انداخته
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/11596" target="_blank">📅 23:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:  مذاکرات جدی در حال حاضر برای دستیابی به توافق با ایران در جریان است.
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/11595" target="_blank">📅 23:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/11594" target="_blank">📅 23:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فارس: حمله پهپادی علیه گروه پژاک در شمال عراق
رسانه‌های عراقی گزارش دادند مقر گروه‌ پژاک در استان سلیمانیه عراق با چندین فروند پهپاد مورد حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/11593" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کاخ سفید : ترامپ تو هر زمانی همه گزینه‌ها رو برای مقابله با ایران داره.
@withyashar</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/11592" target="_blank">📅 23:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">https://t.me/boost/withyashar
۵۰۹ بوست نیاز داریم
🙌🏾</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/11591" target="_blank">📅 23:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">@withyashar
part1</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/11590" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ: من به وزیر جنگ، رئیس ستاد مشترک و ارتش امریکا دستور داده‌ام که آماده باشند تا در صورت عدم دستیابی به توافق قابل قبول، حمله‌ای کامل و گسترده و همه‌جانبه به ایران را با کمترین هشدار ممکن انجام دهند این آخرین فرصت ایران برای توافق است
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/11589" target="_blank">📅 23:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/11588" target="_blank">📅 23:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">معاون استاندار هرمزگان: صدایی که ساعاتی پیش در جزیره قشم شنیده شده است، ناشی از فعال شدن سامانه‌های پدافندی و درگیری با پرنده‌های دشمن بوده است .
وضعیت کاملاً تحت کنترل است و شرایط جزیره قشم کاملا پایدار است./مهر
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/11587" target="_blank">📅 22:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اتاق جنگ با شما : فرمانده دقیقا همین الان صدای پدافند
با ۷ شلیک کمتر از یک دقیقه به سمت جنوب کرمان اتفاق افتاد
بریم که داریم به قاهره نزدیک میشیم
@withyashar</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/withyashar/11586" target="_blank">📅 22:51 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اتاق جنگ با یاشار : یک پوکرباز خوب دستش را «شو» نمی‌کند، بلکه معمولاً فقط وقتی کارت‌ها را نشان می‌دهد که دست قوی را نشان ‌دهد تا تصویر «بازیکن صادق» بسازد و بعداً راحت‌تر بلوف بزند
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/11585" target="_blank">📅 22:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فعالیت پدافند در شمال تهران شروع شد
منابع نزدیک به سپاه: انهدام ریزپرنده در شمال تهران
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11584" target="_blank">📅 22:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">حمله فردا کنسل شد
ترامپ در تروث : از سوی امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس‌ امارات متحده عربی، محمد بن زاید آل نهیان، از من درخواست شده است که حمله نظامی برنامه‌ریزی‌شده ما علیه جمهوری اسلامی ایران را که قرار بود فردا انجام شود، فعلاً متوقف کنم؛ زیرا اکنون مذاکرات جدی در جریان است و آن‌ها، به عنوان رهبران بزرگ و متحدان ما، معتقدند توافقی حاصل خواهد شد که برای ایالات متحده آمریکا و همچنین همه کشورهای خاورمیانه و فراتر از آن، بسیار قابل قبول خواهد بود.
این توافق، مهم‌تر از همه، شامل این خواهد بود که ایران هیچ سلاح هسته‌ای نداشته باشد.
بر پایه احترامم به رهبران یادشده، به وزیر جنگ، پیت هگست، رئیس ستاد مشترک نیروهای مسلح، ژنرال دنیل کین، و ارتش ایالات متحده دستور داده‌ام که حمله برنامه‌ریزی‌شده به ایران را فردا انجام ندهند. اما همزمان به آن‌ها دستور داده‌ام که در صورتی که توافقی قابل قبول حاصل نشود، آماده باشند تا در هر لحظه حمله‌ای کامل و گسترده علیه ایران را آغاز کنند.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/11583" target="_blank">📅 22:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خدا بخواد به زودی تهران میرسه هر چی که هست
😂
🙌🏾</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/11582" target="_blank">📅 22:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اتاق جنگ با شما : یاشارررر
پدافند اصفهان چند دقیقه فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/11581" target="_blank">📅 22:27 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">زرشکیان لو داد میخوان مذاکره کنن:
گفت‌وگو به معنای تسلیم نیست
جمهوری اسلامی با عزت، اقتدار و حفظ حقوق ملت وارد گفت‌وگو می‌شود و به هیچ عنوان از حقوق قانونی مردم و کشور عقب‌نشینی نمی‌کند.
ما با منطق و با تمام توان، تا پای جان، در خدمت مردم و حافظ منافع و عزت ایران خواهیم بود.
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/11580" target="_blank">📅 22:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اتاق جنگ با شما : اره الان دوباره مجددا صدا اومد
جالبه تو دوران جنگ قبلی اصلا قشم پدافند این چنینی نداشت و ما اینجور صدایی رو واسه اولین بار هست تو قشم می‌شنویم
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/11579" target="_blank">📅 22:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با شما : سلام یاشار
همین الان پدافند قشم بدجووووور زد
پدافند خود شهر قشم حتی توی جنگ ۴۰ روزه هم کار نکرده بود
ولی پنج دیقه پیش بدجور شلیک کرد
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11578" target="_blank">📅 22:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11577" target="_blank">📅 22:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/11576" target="_blank">📅 22:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ: اگر فرد اشتباهی جانشین من شود، برای آمریکا فاجعه خواهد بود
رئیس‌جمهور آمریکا در مصاحبه‌ای که روز دوشنبه منتشر شد، گفت اگر پس از پایان دوره ریاست‌جمهوری‌اش «فرد اشتباهی» قدرت را به دست بگیرد، این موضوع برای ایالات متحده فاجعه‌بار خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11575" target="_blank">📅 22:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11574">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تامین‌اجتماعی: دریافت فیش حقوقی اردیبهشت‌ماه فعلاً مقدور نیست و زمان آن متعاقباً اطلاع‌رسانی خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/11574" target="_blank">📅 21:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11573">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">نظام وظیه: ۱۸ تا ۵۰ ساله ها بیایید خودتونو معرفی کنید که اگه جنگ شد بفرستیمتون با آمریکاییا بجنگید، تو محلتی که تعیین شده اگه نیایید تمام مزایاتون که به کارت پایان خدمت مربوطه قطع میشه
@withyashar</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/11573" target="_blank">📅 21:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11572">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPresident DONALD J. TRUMP</strong></div>
<div class="tg-text">تا یکشنبه میزنم، قول میدم</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11572" target="_blank">📅 21:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11571">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg-hPYrYK1kiceFT9DD5LweZoMnOS39CxC8J_fnUiPS5UcaOsqPrOFEL_ZYp6ZtxCSaD6-vxXXfl28uAY-vtGUKHD3pW-lCaYx2zyGX0ZBkBpjZDIItNhpcfmq1Q8Ui39zIbV1dkmbANxorGhuc1zKmICFCejbLuEMM38pjx8DkHQjlj2cvBHGlUqZ7QHA6hlyGhAXC7_1Z-uiJoYB1b-plML39PxE1-dkadlppD5cDUAagoOIBHmTEDhaiMXKzBTHByCimJpWouiSmiz9DpfFk16-sj5ulqaaYzw84MLy5FodxvrCbSe_SrP1QZIW_6cZhB3z05xtsy_3lIb4OqOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیتر نیویورک پست:
ایالات متحده در آستانه از سرگیری نبرد با ایران با تمام توان است!
@withyashar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/11571" target="_blank">📅 21:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11570">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ترامپ:من از دست تهران «کلافه» نیستم
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11570" target="_blank">📅 20:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11569">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار نیویورک‌پست:
هنوز حاضرید اجازه تعلیق فقط ۲۰ سال اورانیوم به ایران بدید؟
ترامپ: من اجازه هیچ چی رو نمیدم!
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11569" target="_blank">📅 20:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11568">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه مقام اسرائیلی امشب به i24NEWS گفت:
سطح آماده‌باش واسه احتمال از سرگیری جنگ تا آخر همین هفته، فوق‌العاده بالاست.
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/11568" target="_blank">📅 20:54 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11567">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ در پاسخ به پرسش نیویورک‌پست درباره ادعاهایی مبنی بر اینکه ایران در مذاکرات هسته‌ای سعی دارد زمان بخرد و منتظر واشنگتن بماند و همچنین موضوع بازگشایی تنگه هرمز، گفت:
«من چنین چیزی نشنیده‌ام.»
او افزود: «من چیزی در این مورد نمی‌شنوم. نمی‌توانم درباره‌اش با شما صحبت کنم.»
ترامپ ادامه داد: «این یک مذاکره است. نمی‌خواهم احمق به نظر برسم.»
@withyashar</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/11567" target="_blank">📅 20:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11566">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBL0NeJ6igt3GC9lF4szWKJR2JAuxU4HQ79EmA1WYHE8sf0QZuMXgvvKREQPQpEwnwy0qniO6RIsu7FBhQZ1_rEzh9T7Rlg0LJXwb9ziksFHMQd6yEQ4Elp_H6OVNjMbcmcvZ2j10s3U9Vki4DFMWJjO8ytEkRLyspQFvas-giaw8kg7E_JuKBZwP9xV75rYm3ZZRS9OjpMvyKFeWfIUI_TFrfNDO1NbGeq0gNt2eixut5wPBfMilhUQa67nkAaRkv9vrciEbe7CC6sU_YgTy9LLKiptjMVAay1RbZ9N0s--lfyIv3sP_Lyex-d_8WL1Kp6m6kpIeTmckgmtMQ3xmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص سفارش کوبیده در اطراف منزل شاهزاده در‌ حومه شهر واشنگتون و در بین پادشاهی و مشروطه خواهان آنجا بالا رفته
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11566" target="_blank">📅 20:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11565">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ به نیویورک پست : ایران می‌دونه که به زودی چه اتفاقی براش میوفته، هیچ امتیازی داده نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11565" target="_blank">📅 20:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11564">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e3bcea4b.mp4?token=Dw9CEVQzeBJ8lyfzdfauW2k73iYVC8od3dmrqhU2AGqNjDjG8PafdWpdEGM9tn7Az6lU_xJUWigYGK1W_21gmZvXuwZq0mrukhYfbZiYmt7CohbMQcpd7LYf6OG2iP8MdQwbxOaxKKl-J9r36BdEttKl4DXx6pPaUG-e4wQ_cjv7zeTi4Hp2MWTIOgrLWlgkEGqa8uc6F9FXnghiSy-Sf6MEofi0q0IbTOo812S3P_jRUTn9afCJbUMxYQlq22apWlibsD7c83ttNzS7hl9iKsTcRD-_PU82_4Q7xvlUbagr3cN9jPfSnasTaH1K3vNBwjYnR2Xr9iFVpzQICiAaLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e3bcea4b.mp4?token=Dw9CEVQzeBJ8lyfzdfauW2k73iYVC8od3dmrqhU2AGqNjDjG8PafdWpdEGM9tn7Az6lU_xJUWigYGK1W_21gmZvXuwZq0mrukhYfbZiYmt7CohbMQcpd7LYf6OG2iP8MdQwbxOaxKKl-J9r36BdEttKl4DXx6pPaUG-e4wQ_cjv7zeTi4Hp2MWTIOgrLWlgkEGqa8uc6F9FXnghiSy-Sf6MEofi0q0IbTOo812S3P_jRUTn9afCJbUMxYQlq22apWlibsD7c83ttNzS7hl9iKsTcRD-_PU82_4Q7xvlUbagr3cN9jPfSnasTaH1K3vNBwjYnR2Xr9iFVpzQICiAaLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داماد صداسیمایی تروریستی : مهریه زنم پهپاده
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/11564" target="_blank">📅 20:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">واشنگتن پست:
اسرائیل منتظر چراغ سبز آمریکا برای شروع عملیات است
@withyashar</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/11562" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11561">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آکسیوس: بمب‌ها مذاکره خواهند کرد
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11561" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11560">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌بی‌سی:
اظهارات رسانه‌های ایرانی مبنی بر موافقت واشنگتن با لغو تحریم‌های نفتی کذب است، هیچ تحریمی لغو نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/11560" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11559">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع «العربیه»:
وزیر کشور پاکستان بعد از آخرین تلاش‌هایش، تهران را ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11559" target="_blank">📅 20:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11558">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تری یینگست، خبرنگار فاکس نیوز‌ :  ما تو آستانه بازگشت به عملیات‌های رزمی تمام‌عیار هستیم
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11558" target="_blank">📅 20:04 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11557">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه های عبری:
ترامپ‌ امشب دستور بمباران را صادر میکند
@withyashar</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/11557" target="_blank">📅 20:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11556">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
رویترز:
آمریکا پیشنهاد جدید ایران را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11556" target="_blank">📅 18:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11555">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0kzSmTMnshZ71IoZqu6mawaZfLXPcLitDeGjvt3vddfktofvO0WlzCBRSj73bPF3iy3zx5lvLWk65ZMtH7oAQaPHKLmFjL6ET_E9-LswoDwOqZPDbvGp0nE83dnc_E2G57yqEB0mhoU-dYyZI6mmGIw55Rv2UalWftLpiTN3rqv-BIExsaPDVMyjH99BY2iv2uGWEBo9qIcrYVfWX9LTebaztBVuIJeycxiACEAD2a92SPev-EOdnG4MDNiE-24tiWmhPjz7UyLJb_Dz0nPvYu8iArIwnqlL0K_sj8V5tUB81eoFIbroM3swelNnFH23287PyyxPl_2kiORlKuORg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی‌ آقا عشقه ، چقدر راحت و خاکی‌ کانکت شدیم…  بد یه عده … چی بگم… درست میشه اونم … در آخر هر چیزی فقط‌ مردمن که مهم هستند
🙌🏾
❤️‍🩹
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/11555" target="_blank">📅 18:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11554">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کمی‌پیش ستون عظیم دود از جنوب تهران، دوربین به سمت : بزرگراه یادگار عمام، جنوب @withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11554" target="_blank">📅 18:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11553">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSa92IKA4rs9fStsQnA__yVTP1uyr0-xc-b07aKD-czip0-GobUZMckAkQueUSEUE9UojYIxq3Uiu8HBL46u1n5UFyhUWGEST9o34rPbbduH2FtWa0FHVO0YtOO3FcC_vVHaYCMgJpE0U83ZGQ6HMwxQ5fCkWh7jnkHAy6OQAFsoLZGniYe500dkSWbs4Q8ui-cWRnQ5-H6vpxyL8rwjpcqKEhOnO19W_KFg9hvvcb21uRpOsdRIRp3zEnaP2yrDCCEtRj0YcfrXy23pInyc2caBAD4uCDjV8AgMvsw7wrQPdzMjomLXvWqDdhltuBsO6naaRIOyKEepMDSbPv75bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی‌پیش ستون عظیم دود از جنوب تهران، دوربین به سمت : بزرگراه یادگار عمام، جنوب
@withyashar</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/withyashar/11553" target="_blank">📅 18:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11552">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تسنیم به نقل از منبعی نزدیک به تیم مذاکره‌کننده ایران:
ایران بر لزوم پرداخت غرامت از سوی آمریکا به دلیل جنگ، اصرار جدی دارد.
واشنگتن باید درک کند که پایان دادن به جنگ، در ازای تعهدات هسته‌ای نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/11552" target="_blank">📅 18:27 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
