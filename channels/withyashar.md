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
<img src="https://cdn4.telesco.pe/file/RVZYYWzaUqyi82X1EOAybPjls-dKsXvtMnCEMhggy13j9qS7bVEE8TvubgnSF_Y0eKlxGar7kOgXMHjOreL1uPRB8JdEjgu9DgGXLsw-MoPvTJiDdnPhL6MmRCsj8GxNKyVj6vYgXapDjumHZ-uMD3ZEaXNU5dNPXJ9SXF-VxsPLYWYxFO3CDubf79vtWaxxDuHDOrF_qxEqA9UYgPYcLuPertbA0Jc1fAKVRhOE6EEt2h1t_zqaVePMPIJrJOIMsI6vB0-JaEi2BmYvdzlHeO-xz8xko6SuSCo7pQsReNkte2KcSXANCsI_BgT2SulYw1ox2pPrVNY25_TU6aNsfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 414K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 08:29:30</div>
<hr>

<div class="tg-post" id="msg-19001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چابهار آخرین نقطه قبل ناوه دارن برمیگردن رو ناو بشینن هر چیزی مونده خالی میکنند چابهار …
@WarRoom
⚠️</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/19001" target="_blank">📅 05:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">چابهار ۳ انفجار الان و ۲ انفجار کنارک
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/19000" target="_blank">📅 05:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3690b0e4b.mp4?token=c8TDMLVfdY7dnrokmKsZCk8IeEIX-yUQWTx7nGxbeKWP2NOw7HNdRAj8kKWeQXf2LZmuoRqzjsUKZkHmtKAjmehVnH63jz8ctAqSEBlr_mtcblnaPlzodMPj_05Rwto3jCD1lGr9Xg-HnuAXj8bn8moOxlecEZD-iqd0ShXfBFlyEA_MlfgDj4KhHs6BfOGV6ZD474fG8GgFZY96GVDu8ise49YXpdpmAkVEQNfCJ1dLo-ThvDdJNN5bo_ylnmOEsjQupYmBcZaHsOTG8BPnGvS5OFAdEaVR7ZYKYa288cb0o0o936bm-onQsrahf7LtbRRG5kgCdfCsW8KZmgETUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3690b0e4b.mp4?token=c8TDMLVfdY7dnrokmKsZCk8IeEIX-yUQWTx7nGxbeKWP2NOw7HNdRAj8kKWeQXf2LZmuoRqzjsUKZkHmtKAjmehVnH63jz8ctAqSEBlr_mtcblnaPlzodMPj_05Rwto3jCD1lGr9Xg-HnuAXj8bn8moOxlecEZD-iqd0ShXfBFlyEA_MlfgDj4KhHs6BfOGV6ZD474fG8GgFZY96GVDu8ise49YXpdpmAkVEQNfCJ1dLo-ThvDdJNN5bo_ylnmOEsjQupYmBcZaHsOTG8BPnGvS5OFAdEaVR7ZYKYa288cb0o0o936bm-onQsrahf7LtbRRG5kgCdfCsW8KZmgETUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد
نهمین شب متوالی حملات علیه ایران
در
۱۹ ژوئیه، ساعت ۱۰:۰۰ شب به وقت شرق آمریکا (ET) (۰۵:۳۰ بامداد ۲۰ ژوئیه به وقت تهران)
با موفقیت به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی
مراکز فرماندهی نظامی، سامانه‌های پدافند هوایی، مراکز دیده‌بانی ساحلی، توانمندی‌های دریایی، محل‌های پرتاب موشک و پهپاد، و شبکه‌های ارتباطی ایران
را هدف قرار دادند تا توانایی ایران برای حمله به کشتی‌های تجاری و خدمه غیرنظامی عبوری از
تنگه هرمز
بیش از پیش کاهش یابد.
سنتکام افزود که
به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)
، ارتش ایالات متحده ایران را در قبال اقداماتش پاسخگو می‌داند و نیروهای این فرماندهی همچنان در
آماده‌باش کامل، متمرکز، مرگبار و آماده اجرای مأموریت
قرار دارند.
@WarRoom</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/withyashar/18999" target="_blank">📅 05:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه:
هواپیماهای ترابری بزرگ C-17 و هواپیماهای فرماندهی و کنترل P-8 ارتش آمریکا با موشک‌های بالستیک در فرودگاه عقبه هدف قرار گرفتند.
@WarRoom</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/18998" target="_blank">📅 05:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ارسالی : درود بر شما همین الان کلی امبولانس و اتش نشانی دارن میرن سمت خجیر ، انفجار بوده
@WarRoom</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/18997" target="_blank">📅 05:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/18996" target="_blank">📅 05:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gA6wOpJ3ruioNd8FMiwP9kvqIjgWw0i1XYEePyr1jUR5bW41WmruUU42NIEpK04qmTfXQQMw8z4OUbt_Hy0RNq8NYWk5LOtQb6hdBrlfsIjQtIrIpmgqOxEsHOj2U7LpyHXt-ZTZwuWY6F9kxZgwQilNkv4pngh3wbOPfBgWsI9uuIiJ75Cml26gQQSa4ShrCn6NGZ2v-kovdIj5NS5er0E9AymuSEaqZ1sYPm8OAa0Tzn3RkIV2ePKPGCQdX2HYb011DHB7zKd_xtHC4Q5d2agjTG-qJQqn6PBi4QwHG4xmUnie-cLqhg-BX7ZukTMR5KgPvl3KNbSMea_DoM_jtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدبان اتاق جنگ : درود و عرض ادب یاشار جان.
من سمت شرقم و اینجایی که زده سمت خجیر میشه ولی من صداشو نشنیدم ولی دودش معلومه.
تاییده انفجاره شرق
@WarRoom
یاشار: من بالای پانزده پیام دارم که صدای انفجار را شنیده‌اند. حتی یکی از کاربران با ماشین در خیابانها افتاده و دنبال مکان انفجار میگردد. ممکنه حمله هوایی نباشد و یک انفجار دیگری باشد، ولی به هر حال این دود مشاهده میشود و صدا شنیده  شده.</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/18995" target="_blank">📅 05:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شهرهایی که امشب تا این لحظه مورد هدف حمله قرار گرفتند؛
💥
تبریز
💥
بندرعباس
💥
چابهار
💥
ماهشهر
💥
سیریک
💥
کنارک
💥
جاسک
💥
خورموج
💥
دشت آزادگان
💥
خرم آباد
💥
سربندر
💥
دزفول
@WarRoom</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/18994" target="_blank">📅 04:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش انفجار شرق تهران
🤯
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/18993" target="_blank">📅 04:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش انفجار کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/18992" target="_blank">📅 04:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش انفجار کرمانشاه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/18991" target="_blank">📅 04:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">دقایقی پیش, مرکز تجارت دریایی بریتانیا: گزارشی مبنی بر وقوع یک حادثه در فاصله ۸ مایلی شمال غربی شهر کومزار، عمان، دریافت شده و یک کشتی در حال سوختن است @WarRoom</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/18990" target="_blank">📅 04:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به گزارش خبرگزاری صدا و سیما، حملات هوایی ایالات متحده بندر سیریک در جنوب ایران را هدف قرار داد تا عملیات جمع‌آوری اطلاعات ایران در تنگه هرمز را مختل کند.
@WarRoom</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/18989" target="_blank">📅 04:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رسانه های رژیم : به دستور مجتبی خامنه‌ای ، موشک‌ها و پهپادهای "ولایت" به زودی به پایگاه‌های دشمن آمریکایی در منطقه ضربه خواهند زد.
@WarRoom</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/withyashar/18988" target="_blank">📅 04:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ : اگر نگاه کنید، پس از حدود یک هفته و نیم تا دو هفته از آغاز جنگ، احتمالاً جلوی پیشرفت آن‌ها را گرفتیم؛ البته نمی‌خواهم از واژه «احتمالاً» استفاده کنم
@WarRoom</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/18987" target="_blank">📅 04:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صداوسیما : انفجارهای تبریز اولین انفجارها از نوع خود از زمان آغاز حملات جدید آمریکا به ایران در روزهای اخیر هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/18986" target="_blank">📅 04:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دریا بانی گروگ  رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/18985" target="_blank">📅 04:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فاکس نیوز : فرمانده کل قوا(ترامپ) هیچگونه مذاکراتی رو قبول نمیکنه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/18984" target="_blank">📅 04:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_c75SoDJCMavY9_iodVkyp8LjjRUtd4_E94sLO1Lfch-Ng7tOvOXvM-PK8hLz_TpQckBgL29XqGCGwMb_AfqW5icH4uqfVf1fxXL6NW_KjcX52Lev683HPaQfTnFDAaU4H7OoC7TXXdbm2ZRbheYOBo2UIl9HnZsW-8MzxJD1GPtn-kK5wA7y2ABP-1c1SWsSkWzlXShmYWTGteNSA3vBwtOnWPRIjkayrTZkg8f0mc4ZAatPb9ykoFgpx0kRZeIvjvEFvx04dWU_mGIkcj7V9FMnB8cmLE_s503dl7v1I4uJJcCiZb_kYDZK-iuYotMSqOfpZxRuwF9DUpu3hZrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقایقی پیش
,
مرکز تجارت دریایی بریتانیا: گزارشی مبنی بر وقوع یک حادثه در فاصله ۸ مایلی شمال غربی شهر کومزار، عمان، دریافت شده و یک کشتی در حال سوختن است
@WarRoom</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/18983" target="_blank">📅 04:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebbc46a29a.mp4?token=mS8ulGbvOXx7X8qvqwNA7jURJzBDo8WGcnjcTdz2t4YlUFpnsuxUfUX8GKNY5FDJg5T7TXbvp_idWMQ2DiI153z01roHqmGrH6wi04Gp48GLiI4inQjkTDHqJ19kiAyN6GhYF_jeXIsFNwEZXSzRRoW7f13EC7Nb3QNqsPuTRGOZ8OH7-Dp38ZE9ftKVeT8xYiS4SyZeacMZKNRfSE0_c6VMEefug_De_XmZU-WDMihzZRq25AUz_5mGu90Jfj70mCcNCQxc1386Ci4mDbBfX3lFeWjtNmccmzRZUqlj5lVZGUL5pnUuohHuE3vTg9ABR3QbnNNXOcDteIz2koXkkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebbc46a29a.mp4?token=mS8ulGbvOXx7X8qvqwNA7jURJzBDo8WGcnjcTdz2t4YlUFpnsuxUfUX8GKNY5FDJg5T7TXbvp_idWMQ2DiI153z01roHqmGrH6wi04Gp48GLiI4inQjkTDHqJ19kiAyN6GhYF_jeXIsFNwEZXSzRRoW7f13EC7Nb3QNqsPuTRGOZ8OH7-Dp38ZE9ftKVeT8xYiS4SyZeacMZKNRfSE0_c6VMEefug_De_XmZU-WDMihzZRq25AUz_5mGu90Jfj70mCcNCQxc1386Ci4mDbBfX3lFeWjtNmccmzRZUqlj5lVZGUL5pnUuohHuE3vTg9ABR3QbnNNXOcDteIz2koXkkIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: امشب ایران رو بازم شدید هدف قرار دادیم!
این حمله در پاسخ به کشته شدن نیروهای آمریکایی بود؛ ۳ نفر از نیروهای ما کشته شد
ایران از نظر نظامی تقریباً همه‌چیزش رو از دست داده؛
فقط تعداد کمی موشک، پهپاد و توان تولید براش مونده، ما تنگه رو کنترل می‌کنیم و ایران هیچ کنترلی روی اوضاع نداره
@WarRoom</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/18982" target="_blank">📅 04:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: امشب حمله بسیار قدرتمندی علیه ایران انجام دادیم
ایران آسیب بسیار شدیدی دیده و نمی‌تواند سلاح هسته‌ای داشته باشد.
ایران ممکن است تعدادی موشک و پهپاد داشته باشد، اما تعدادشان زیاد نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/18981" target="_blank">📅 04:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو انفجار بندر عباس
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/withyashar/18980" target="_blank">📅 03:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CK2aLGLaso7HgIiMDI7pmW1dRd90q1AJyNdWgsymsTZmsVZgY7sTg2y4gTJxhKtGe8JBiAGPVrPVr9Kj_DLxdBntuwYGwCLUHT1EdTO1PIgaCLhvBRcRXSC-bWRqbdz3gvTI1K2vwqlifMYfD0i6IzDrnqcEPRo8_GsnpUR-PVo1tK3zSPypmGzGcKI5rI7YarB3B37U6OuUUqKM1DziMjkek3QoZfcAF-oLLijg49Ce5Ycvqy7jg-dOg3wTwKKV9G_YOquxqdO93GjH3MOR8EVD55lLnBxKp05GZq_0br_6liyDoVqIe_aqvjy5DZC57vPyYO8N4GDDAl7EqWRP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کنارک انفجار سنگین
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/18979" target="_blank">📅 03:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTRw6gk0kGOf9dc0PTyH6CMoL_ZMSaiHJzkP35k2DQb9rAO8vX3nZ3d17O37Z9sha_flbAHKsK6vWCz-xHU3-JDIxC0jbp_D5E5u6DwWHTAdq5Vu8SL2BLa40gskssM1x0DzsOj55CFwKI8wkTbi144AbLJpaqO2ZD82Rs4eCcD1ZG8IQw0eU71Epao1fg-56qR_9QMJYDYDUQPDLLKXbJQSQ2ThFA7yjH0q1N24vUmATRA4XXnBeT05dwllbbkWCvbxqLzPsrz-00ilIb5qkyKjMpzySAHJac4A8JfeIl_RQIvtrqe8pDiFuWN6tJs73U0BYmSBUGDKkirnvsNeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیریک اسکله طاهرویی
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/withyashar/18978" target="_blank">📅 03:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7dd005bae.mp4?token=nMy7Xy7E2yKbIiAlBaLDh3vYwpKWirEuYUjEcxP3UvXN2QUZS39cMGJZuA8rJNMvFy85BE1tDJvywADnR9_KdnNHkKE1XjFqCnU-hPUTEDsemHWMhGgC5lSapvgMuW6bZkhbhMQGFcBWn-3M6aFbnLFyhawQ7vRXGlrLFQM7p4Im4DDJ9l5VfVVMHcAwxTM5dF0aOPRmHwJz_l9GJSRLN9z9lfCLgct3UWvc_Db6Qa1odN1Pw5sWodUoKIKsuvXxZ_Fgh63a_OIvQqi3JcsILJEnsiDX5xtGwcUfQZzaI4rPLUF0NJnTA78vkUGagA343lJ0-FLsA1qcJzb1htSBgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7dd005bae.mp4?token=nMy7Xy7E2yKbIiAlBaLDh3vYwpKWirEuYUjEcxP3UvXN2QUZS39cMGJZuA8rJNMvFy85BE1tDJvywADnR9_KdnNHkKE1XjFqCnU-hPUTEDsemHWMhGgC5lSapvgMuW6bZkhbhMQGFcBWn-3M6aFbnLFyhawQ7vRXGlrLFQM7p4Im4DDJ9l5VfVVMHcAwxTM5dF0aOPRmHwJz_l9GJSRLN9z9lfCLgct3UWvc_Db6Qa1odN1Pw5sWodUoKIKsuvXxZ_Fgh63a_OIvQqi3JcsILJEnsiDX5xtGwcUfQZzaI4rPLUF0NJnTA78vkUGagA343lJ0-FLsA1qcJzb1htSBgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایگاه امام علی در چابهار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/18977" target="_blank">📅 03:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/withyashar/18976" target="_blank">📅 03:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دانش آموز های ساری تهران و اصفهان تبر دارن میزنند ، هیچ خبری نیست</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/18975" target="_blank">📅 03:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q70v_GQrPgYK_iYXQyRNwwTvbyeFAmINKbr8l_xtTjPcyiUXUmBP2jF7LJFzw_GjGoLFtYKcMXM2vwtmhaweUx3Tj_P41MvUf24u2n1fJWgK2VlwBYUV2HsXeFniJzltx-D_4bbXWOKKSeqyA8K4ekvKt5vIyI3RkEhKMHc7CyY6fYImRKWoyoRXH0avgcO5n3MURGJzMfeYXhB1QniQ_LVvLNvAnlYQGeV_UQV3chWAU4Y4Jj5_t08tfCY37Ybe6KHEazd6ZwYM_cZLLYda_MzlEgkGiHEr1YO-2fiV5FEdbcd8YpT9wVHXwyDjOgTfPBMY2hrwObCXgTgGmFB4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقدر آزارم ندید !
😔
اخبار فیک نفرستید تهران تهران</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/18974" target="_blank">📅 03:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یاشار همین الان جاسک دوتا انفحار وحشتناک به فاصله ۵ دقیقه از هم
@WarRoom</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/18973" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سیریک رو با جنگنده بد زدن @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/18972" target="_blank">📅 03:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سیریک رو با جنگنده بد زدن @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.8K · <a href="https://t.me/withyashar/18971" target="_blank">📅 03:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDoetqG45h7DM3o8b0gP1Ju4KtkGmNoBs1J530qJJWwnVcrRpwYmMZqAqiFnWnDZdfc1a9i4oXy4O8tpDNQH2eBBSGNrYT4jb9zF8T_WGQkLzeFCwdx2VX2onRyJz-l4-rm_dKYWXhZx8Of1m0xTLnzV6uqT6nOzn807dqL_NPwsawxAmVdQ8p10RPL3iNWREvNsLMPzAZL6LTBWLyHpLPxmeCGHfPiKRbUVyTvtONanEkbH7vUw_Gzuq3uYwcYQmKg_N8PY7_l3H3VWjcK8B_wGc5Yy_qks3bHelX9BynS-H2A3EVED8jwZ4oQaVCiy8qP9OH5cXhs0uAuF50kQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سربندر / ماهشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/18970" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خورموج ، برق رفته و میزنند تند تند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/18969" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سیریک رو با جنگنده بد زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/18968" target="_blank">📅 03:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گزارش‌ ۳ انفجار در تکاب آذربایجان غربی
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/18967" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4812b607a5.mp4?token=dQc30Dm0zJjLGpdSsZENZgXZdMb6UtY69Stuw1nZhBEKMu8PMYr0l2lR5DNVmPWFpiEEw6ayuHY7mGtgmnRGg5UNKAut5btKNciMDFbu_QdMWwCCnQoYgBrjSHCmIAFWLkfB8hfQQSV9IPPbjQZBW7dIuzVvA7n47j2qz_zSbQFmr7YTCpVfuZiPxXXniSdpy4Cd6JRi_KM6KlcPSEuihXLpx99Vj6Z6IQ6uIA3jOUJAQtVELGRYb33CFP9uslxf5oFSMGdMRx91HfGztZUqxi8OxcZWIOXFfmgr15ssH1tm73jrRYj-0vIyIJoH0AQnomfG1uv_xwOJsBjzKWqbzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4812b607a5.mp4?token=dQc30Dm0zJjLGpdSsZENZgXZdMb6UtY69Stuw1nZhBEKMu8PMYr0l2lR5DNVmPWFpiEEw6ayuHY7mGtgmnRGg5UNKAut5btKNciMDFbu_QdMWwCCnQoYgBrjSHCmIAFWLkfB8hfQQSV9IPPbjQZBW7dIuzVvA7n47j2qz_zSbQFmr7YTCpVfuZiPxXXniSdpy4Cd6JRi_KM6KlcPSEuihXLpx99Vj6Z6IQ6uIA3jOUJAQtVELGRYb33CFP9uslxf5oFSMGdMRx91HfGztZUqxi8OxcZWIOXFfmgr15ssH1tm73jrRYj-0vIyIJoH0AQnomfG1uv_xwOJsBjzKWqbzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله آمریکا به سایت موشکی تبریز :
@WarRoom</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/18966" target="_blank">📅 03:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خبرگزاری رژیم تسنیم :
از دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی شنیده شده است
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/18965" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجار سنگین و بی سابقه در ‌سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/18964" target="_blank">📅 03:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ0JeoSa6if9BV1mYwpoNERgrs45M-i2cVplwJTI6t83iIJpDXSIOdy_TmOfAjLLKqpbrZzKOKcpbUwllvPpxQTrdW6YOR9t_m2UUyHEzrdxnAA-ewiR2KP30gr6iIT6cC6DFuhqrbh6QkxQa4tW3eu0rEZ2CzzRrcJ9miwOsXwwRFFVsXYE-Yk0QzfJzT0aWufCGcZjaC01KdvPXOoZDcdsXipQ_0-_VofBJnmR-BtDmfyFh-XCbdaTNrMr9_mxX6oOcVDL6DHqL6rehqfjIbzokXi_e7gaAQFx2duxgI1lqxb46wWlNeF8mVF2ELfR55UppcZ1wZdyBVWvDaofIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار و ستون دود در جنوب غرب تبریز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/18963" target="_blank">📅 03:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گزارش از شلیک موشک از کویت به ایران
@WarRoom</div>
<div class="tg-footer">👁️ 93.8K · <a href="https://t.me/withyashar/18962" target="_blank">📅 03:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چابهار همچنان میکوبه
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.8K · <a href="https://t.me/withyashar/18961" target="_blank">📅 03:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار در بندر ماهشهر و اکام هم گزارش شده
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/18960" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تبریز رو زدن بدجوررر
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/18959" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18957">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش ‌انفجار‌ چابهار
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/18957" target="_blank">📅 02:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18956">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سنتکام : امروز، ساعت ۷ بعد از ظهر به وقت شرق آمریکا، موج جدیدی از حملات علیه ایران را برای نهمین شب متوالی آغاز کرد. این حملات به تضعیف قابلیت‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامی در حال عبور از تنگه هرمز استفاده می‌شوند، ادامه خواهد داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/18956" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18955">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کویت زیر حملات
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18955" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پهپادهای موتور گازی در آسمان شهر سلیمانیه در شمال عراق.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18954" target="_blank">📅 01:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پدافند شاهین شهر اصفهان درگیر شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18953" target="_blank">📅 01:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18952">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان بی بی میاد به جای مسی‌گل میزنه
😂
دقیقه ۱۱۹</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18952" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18951">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btlp7ilQVCcCu5siGicc6dKMOAkDZJA2r-d7qSRPI2JYbI2PjiKIfTOPZafQmd1BrqQVgA9P3ijLkMdxdjWw2Q9IY9V5TUuLV7mJF58GARIvFHWdtos8LbVeyPhmOt_s24sPxwZ9F2MM2TX7oFFmXsUJxP4nOAwFIFols1LarphQqOZWL0TFySQ560Tbfari5eeU3mhQIrWVXjDK8Pzp2c9z1xWiTpU1Q5sdx1HoDD65OociI5mW4cfPpCrlclCa7pZIEufXpQjqwJ-H-Tuo51SAMd2fSjSBGLNdeG6dh0hPe54za18guclnvMuwN0mfbrH2D565GrBjHDGexQPyzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام و اسپانیا قهرمان شد
🥲
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18951" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18950">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گلللللللللللللللللللللللل دقیقه 105 برای پرتغال توسط رونالدو توی PS5 @WarRoom
🤯</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18950" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18949">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من اینجا شوخی‌کردم بخدین وای گل اسپانیا واقعا دقیقه ۱۰۵ زده شد
🤯
🤯
🤯</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18949" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18948">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گللللللللللل برای اسپانیا
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18948" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18947">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیدبان اتاق جنگ : انفجار در سیریک تو دو نوبت یکی بین دو نیمه یکی هم وسط نیمه دوم شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18947" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18946">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلللللللللللللللللللللللل
دقیقه 105
برای پرتغال توسط رونالدو توی PS5
@WarRoom
🤯</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18946" target="_blank">📅 01:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18945">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15c3751fd1.mp4?token=RfhctD7zMp1MVJD7ODTeJjy_gSHz7n3y5e_PhHLDtOUaSWDoMWwE5LB3gCWN32diOUf6CPMQPTtGeg8-3DdXnirWfzjt03vKFO5zxY36VvAlBzH9kUa4Nlok2STqZSRv9LE3xy8FeD4c9dKlhyo0L5QhA9r_-AzbJEKfReJ8Yjn_k0TwB9jlH-ab4DyGRCQZYWaW39dOoxQBlqScrka-a64eBS6AEWqbA1qw6i0egche24C5c8yHqguVppJ4PQj_fgHzG7TJYxCQO1EX0oz0-FZrbTzPAERHZDEQeXvlOb2xn_wumCzWz9Ol1jBWbfw03cc0Hksd_A0TvZY5BF8qhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15c3751fd1.mp4?token=RfhctD7zMp1MVJD7ODTeJjy_gSHz7n3y5e_PhHLDtOUaSWDoMWwE5LB3gCWN32diOUf6CPMQPTtGeg8-3DdXnirWfzjt03vKFO5zxY36VvAlBzH9kUa4Nlok2STqZSRv9LE3xy8FeD4c9dKlhyo0L5QhA9r_-AzbJEKfReJ8Yjn_k0TwB9jlH-ab4DyGRCQZYWaW39dOoxQBlqScrka-a64eBS6AEWqbA1qw6i0egche24C5c8yHqguVppJ4PQj_fgHzG7TJYxCQO1EX0oz0-FZrbTzPAERHZDEQeXvlOb2xn_wumCzWz9Ol1jBWbfw03cc0Hksd_A0TvZY5BF8qhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گویا چون پرچم پشت دروازه آرژانتین است صدا و سیما نمیتونه سانسور کنه و هی نشون میده
😍
🤣
🇮🇷
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/18945" target="_blank">📅 01:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18944">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVbaLV-yIMEEWW3lX4xEHMSKZ6_j42FMmySKALGyN5Bnw8skjaFnmPDkNIL8Jf2D_yg9Ag5XppPzQkn14LQeKOO1tT5d25sDHbgdm_AKLc-SKxDxVeuqDAWaKHAbxF8rtX7O3ZU74wvo0L_xkQ0Z4jsffWygegQSgIHOKMGGVyBZjYicq2NhP-3h9MgKyXeGoM1wDpkK9p1B6TxN25ImHqZy52gp3zVu_bxdasadWM9gBrxmrS3mitGHLnqNvC3tkXZEmQj70g2usKTOCc4UL-7gs0--vqSF1bQGU-0wOuYU2oCDm8NT4oQnxqCl0dy3bHwb4GtvQwvjXS8GoH5xeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک همین الان بخش بمانی سیریک
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18944" target="_blank">📅 00:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18942">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfNtFoRpzVjSHWufvip0iFJUQrEntqssELbUQscvN5ogTFgdl1jMjq3A9lq58OvoAGnf0qx1hRWj23IC-cggIQrzIM7naoQ7kFhUQ0rdMMBELj2nXS2j9MfK6xfTcY5taXLcI3E2xTsZItI1VHadY7ChHvKb1yk5SCwNkgNQvLdj-ugkTlyCBreWXNt6QCCboCr4owDQCTGcZ8MYaryFmZhzYgrSx_V8SBYnJBpxErGzNg-ujDy2gkXqMW8Q5vQg5kEL2dD20vSTdWY8o93kff-KFxYD4-mZhviF3NG-g5tVMU6e9bPT9Mf-X3yck92_6ZHvsfkMCNWTf8toAJ1Mjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از اجرای طاعات و عبادات، هواپیمای E3B آواکس از ریاض عربستان بلند شد و یک سوخترسان هم ، هم اکنون روی باند در حال برخاستن است.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18942" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18941">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آرژانتین ۱۰ نفره شد
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18941" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18940">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آژیرهای هشدار در بحرین به صدا درآمدند.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18940" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18939">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی، از سرگیری محاصره بنادر ایران، ۶ کشتی تجاری را تغییر مسیر داده و یک فروند دیگر را غیرفعال کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18939" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18938">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بازی شموشک نوشهر از این فینال قشنگتره
😁
باور نداری ؟</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18938" target="_blank">📅 00:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18937">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd44e5f41.mp4?token=lUOD8T2vjmmUnIsFnrtcrp4ltBw0bLb8Q659xQtbuUHIATfKMFX2TvOr46kbwG1oX9S7zFskFpIf-ULg-S8pO7KBUKH5ZEzhJMZ3wMCcgEXjSd4yqLwAwz6nihi7mcDykhxCKeDhx_9kPnEUSVDghEXe1YV6GzvL05vawL_U-fIUlAW2LMDQ1OPgJlYCD7rbimmstSbokaiDJtyk-Aej6ZHz7f30lyNZh7qA2WS9uy79MQAeaM19girvdolnwBTKL8GoudGRK88KFW2mXzdto7354_zovEkyuOsslqYSiSJWDvCwcru4YvGO4RmY_9_BXb280gPRfCPrhH1dsXgo7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd44e5f41.mp4?token=lUOD8T2vjmmUnIsFnrtcrp4ltBw0bLb8Q659xQtbuUHIATfKMFX2TvOr46kbwG1oX9S7zFskFpIf-ULg-S8pO7KBUKH5ZEzhJMZ3wMCcgEXjSd4yqLwAwz6nihi7mcDykhxCKeDhx_9kPnEUSVDghEXe1YV6GzvL05vawL_U-fIUlAW2LMDQ1OPgJlYCD7rbimmstSbokaiDJtyk-Aej6ZHz7f30lyNZh7qA2WS9uy79MQAeaM19girvdolnwBTKL8GoudGRK88KFW2mXzdto7354_zovEkyuOsslqYSiSJWDvCwcru4YvGO4RmY_9_BXb280gPRfCPrhH1dsXgo7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای بیژن عزیز در فینال جام جهانی
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18937" target="_blank">📅 00:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18936">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرتاب موشک از ساوه @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18936" target="_blank">📅 00:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18935">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شهرک صنعتی ماشین هایی تحت عنوان عود اومدن اینجا با این نوشته eod نمیدانم از کدام سازمان هستن @WarRoom
🚨
🚨
🚨
🚨
یاشار : من میدونم سازمان خنثی سازی مهمات و بمب هست !!!!</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18935" target="_blank">📅 00:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارسالی : درود بر رضا شاه فقید من نگهبان سوله «سانسور شد» تو شهرک صنعتی کاوه هستم  شهرستان ساوه استان مرکزی اینجا یکی از سوله ها دود شدیدی میده متسفانه نمیتونم عکس بگیرم صداش شیشه های کانکس منو شکوند @WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18933" target="_blank">📅 00:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc79a4e2e.mp4?token=mWVCUzeyT_Qe8lBl2lA2pGr7eLZWHlK5C32kmPujvsOM9ftZsgO66JTD0fOptI_7dEPCLyvDug-w780G3k3gi3mYfI0z34wRyexG03SMrQI6CLtqwdPfX3KPLbdLbmhNBGz0H6WazsTGEsPEICATF5d5OhzptxRAwbotRkRUM-8aWjeFP_Mvi1MxxtmlXpCUS1QOKWD9RY3M7VMrAU-1V7MhwHZ_GmwpF84uwABy919pBbnG0eDLjTHsNRaMbuZ0GfIElH4y2XCut_8gIMXgKyo4Mc49Z1_IuY6NTMA2pBpEPIAbtnYio1_5VI1hBwL49jWymHHXK3dNYa6UfA9kaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc79a4e2e.mp4?token=mWVCUzeyT_Qe8lBl2lA2pGr7eLZWHlK5C32kmPujvsOM9ftZsgO66JTD0fOptI_7dEPCLyvDug-w780G3k3gi3mYfI0z34wRyexG03SMrQI6CLtqwdPfX3KPLbdLbmhNBGz0H6WazsTGEsPEICATF5d5OhzptxRAwbotRkRUM-8aWjeFP_Mvi1MxxtmlXpCUS1QOKWD9RY3M7VMrAU-1V7MhwHZ_GmwpF84uwABy919pBbnG0eDLjTHsNRaMbuZ0GfIElH4y2XCut_8gIMXgKyo4Mc49Z1_IuY6NTMA2pBpEPIAbtnYio1_5VI1hBwL49jWymHHXK3dNYa6UfA9kaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از ساوه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18932" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارسالی : درود بر رضا شاه فقید
من نگهبان سوله «سانسور شد» تو شهرک صنعتی کاوه هستم  شهرستان ساوه استان مرکزی اینجا یکی از سوله ها دود شدیدی میده متسفانه نمیتونم عکس بگیرم
صداش شیشه های کانکس منو شکوند
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18931" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">از خمین موشک شلیک شد
@warroom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18930" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18929">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یاشار جان ما دلیجان هستیم و اولین بار هستش که اینجا صدای انفجار خیلی شدید اومد خونه ها لرزید اما تو شهر نبود فکر کنم جاسب و کوه های فردو که  یک ساعت ازمون فاصله دارن رو زدن
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18929" target="_blank">📅 00:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18928">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیشترین گزارش از ساوه و بعد از اراک داشتم الان ساوه خیلی بد لرزیده و همه نظرشون شهرک صنعتی ساوه هست</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18928" target="_blank">📅 00:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18927">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خنداب/خمین صدای انفجار
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18927" target="_blank">📅 23:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18926">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدای انفجار نزدیک به اصفهان
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18926" target="_blank">📅 23:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18925">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اراک بددددد  زدن
🚨
🚨
🚨
🚨
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18925" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18924">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شهرک صنعتی ساوه
🚨
🚨
🚨
🚨
در انتظار تایید هستم …..
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/18924" target="_blank">📅 23:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18923">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گزارش انفجار از  اراک و ساوه و…
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18923" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18922">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">گزارش های زیاد از صدای انفجار از نقاط مختلف ایران
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18922" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18921">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18921" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18920">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">روزنامه کویتی الجریده: خامنه‌ای (AI)
درخواست ملاقات نخست وزیر عراق را رد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18920" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18919">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzWq_JAUu6xewJh6DcUKbbtrpRpyrPcF5M01LIPuVXvghp7NMwyW_6SAM3n1X_IbyxqoJjX0khwPeDzuDhVMEbQhppyjxdGDhTuxDGHZ_W90_oT134gOjqQhcuCdwZA5J17S6-qSxJk5vaLOACe04z2igHaJ7kqgVlcVmr3Q_cfjmQU1xZFjfGaE2q2nR10gBbf8FAJjTzz2U-YKBIeffzrfAS6brE-RiBWA9wwJpbxIqUGmpnc5kA6B1FJ1nFUud0EXTEHQizqZrpqCLHTg0-yaX0nEE7jx7TA-mVtmhfG7ibUADVKS_346ywv9xN8qQkN2q53YVB39Em_ectw3Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو سوخت رسان با فرستنده روشن هم اکنون از تل آویو اسرائیل بلند شدند همچنین فقط یک سوخت رسان با فرستنده روشن در محدوده خلیج فارس تنگه هرمز قابل مشاهده است.
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18919" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18918">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارشگر صداوسیما رژیم : خیالتون راحت باشه که تا پایان بازی هیچ تصویری از ترامپ کو،دک کش و جنایتکار پخش نمیشه تا اذیت نشید.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18918" target="_blank">📅 23:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18917">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه سنتکام با تایم دیشب حمله را شروع کند حدود ۳ ساعت دیگر و بعد از پایان بازی و مراسم آن میشود …
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18917" target="_blank">📅 22:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18916">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">همچنین
سنتکام اعلام کرد
در ادامه حادثه حمله ایران به اردن در دو روز پیش ۱۷ ژوئیه (۲۶ تیر)، که پیش‌تر از کشته شدن دو نظامی آمریکایی و مفقود شدن یک نظامی دیگر خبر داده بودیم ، نیروهای آمریکایی پس از جست‌وجوی گسترده احتمالا بقایای پیکر سوم را در محل حادثه پیدا کرده‌اند. به گفته این فرماندهی، هویت این بقایا هنوز تأیید نشده و روند شناسایی و بررسی‌های پزشکی قانونی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18916" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18915">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سنتکام :
۱۸ ژوئیه (۲۷ تیر)
، یک نظامی آمریکایی در
شمال عراق
هنگام اجرای عملیات انفجار کنترل‌شده مهمات عمل‌نکرده متعلق به یک
پهپاد انتحاری ایرانی
کشته شد. در این حادثه، یک نظامی دیگر نیز زخمی شده و همچنان تحت درمان برای جراحات جزئی قرار دارد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18915" target="_blank">📅 22:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18914">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رسانه های عراقی :کشته شدن یک سرباز آمریکایی در شمال عراق.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18914" target="_blank">📅 22:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18913">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فاکس نیوز:با پایان سوت جام جهانی٫ سوت شروع مجدد جنگ علیه ایران آغاز میشود
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18913" target="_blank">📅 22:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18912">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ec470cd18.mp4?token=h7JnS3q3gSM9EnaYsW2arxAnPBVsnI3xZ7S-I_CDCtR3VGkO69_NiQOcJd2ksLXgZGyJ12nQXbE3lvqJEAZvjHeewycJ66WDHciiw4sqpTwrsvVkr9mgfDq1AM82mBDG9WFNmEd1O4Szuz_BY-du0noHYSNI48cqqWQHO_2b7OZjmMBFZg7_fCfRX3_SlA3ItbbEgiI7avP4OGHT8BsDP0LK5S-5MVYJBZura5umOD127fGmwigNdbCAU0YOv-vHlZi6iRvtOSEc1Cm83rhXYdFnZfYmQ2rStWsNag5RVzNGzN-MeIzScF0AumirqYzP7QlIxTP0KAlgusDuWclPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ec470cd18.mp4?token=h7JnS3q3gSM9EnaYsW2arxAnPBVsnI3xZ7S-I_CDCtR3VGkO69_NiQOcJd2ksLXgZGyJ12nQXbE3lvqJEAZvjHeewycJ66WDHciiw4sqpTwrsvVkr9mgfDq1AM82mBDG9WFNmEd1O4Szuz_BY-du0noHYSNI48cqqWQHO_2b7OZjmMBFZg7_fCfRX3_SlA3ItbbEgiI7avP4OGHT8BsDP0LK5S-5MVYJBZura5umOD127fGmwigNdbCAU0YOv-vHlZi6iRvtOSEc1Cm83rhXYdFnZfYmQ2rStWsNag5RVzNGzN-MeIzScF0AumirqYzP7QlIxTP0KAlgusDuWclPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون ترامپ به همراه رئیس فیفا و همسرش در جایگاه ویژه استادیوم نیوجرسی برای مشاهده بازی فینال جام جهانی حضور پیدا کرد. آیا او امشب رکورد دیگری را هم جابجا خواهد کرد و در تاریخ ثبت میکند؟ آیا او امشب دستور حمله شب نهم را به سنتکام میدهد؟ خواهیم دید چه خواهد شد. همزمان با بازی فرمان جنگ در ایران.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18912" target="_blank">📅 22:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18911">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: من دوست دارم تقریباً یک ماه را مثل مسی و رونالدو زندگی کنم.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18911" target="_blank">📅 22:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18910">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx30befmObJdreesUqdX4LKvDcGwqgKEVDkAfbSpsT6NsrWHxB-1lM9xt8Th1TLav6NcsWoxwFJkUJrCkINRBoTOtlzU46p0Kx-qWTrM7CCiI3L5appSJiEX_PtFbo9opzGy2C9plgVi2WuiQSnS4nXGcwz1Je4E-RpzplB1JgXBRaZu9QCtLMqGoBKOlTDMgHXW7HTWM2KKLH5cHoxzyHcQRTrSrSoE2_VtLgboafZZBJfXirdxaGr402cPGgoFZcss0v-nkP0IAvCQVX3UE7kBhRJuM2m2eAmf5HPrKiBa0yoKe7cNLUEstzwQR-fuwsxwx_CQ2q-x0FmqCFLf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب ضرب الاجل هفتاد و دو ساعته محسن کج بند تمام میشود.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18910" target="_blank">📅 22:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18909">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای با روزنامه نیویورک‌پست در دفاع از کشته شدگان جنگ با ایران گفت : آیا تا به حال از خود پرسیده‌اید که چند نفر در ویتنام جان خود را از دست دادند؟ آیا تا به حال از خود پرسیده‌اید که چند نفر در یک روز در افغانستان جان خود را از دست دادند؟ در یک روز، تحت رهبری جو بایدن.
ما در مورد دو جنگ صحبت می‌کنیم: ونزوئلا و این جنگ با ایران. این موضوع شرم‌آور است، اما در این مورد، آن‌ها جان خود را از دست دادند زیرا نمی‌خواهند ایران سلاح هسته‌ای داشته باشد و نمی‌خواهند شاهد نابودی خاورمیانه باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18909" target="_blank">📅 22:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18908">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">خبرگزاری CBS: جمهوری اسلامی ایران به حملات در روز دوشنبه ادامه میدهد تا قیمت نفت بیشتر بالا برود و ترامپ تحت فشار قرار گیرد
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18908" target="_blank">📅 22:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18907">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیویورک‌تایمز
:
دسته جدیدی از جنگنده‌های f-16 و f-35 از پایگاه‌های اروپا در راه خاورمیانه هستند
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18907" target="_blank">📅 21:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18906">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منابع به فاکس نیوز گفتند ، امریکا میخواهد در نبرد زمینی بزرگ ترین جزیره خاورمیانه که «قشم» است را تصرف کند و سپس لارک و هرمز و خارگو ابوموسی را تصرف کند
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18906" target="_blank">📅 21:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18905">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ادعای شبکه کان اسرائیل:  در حال حاضر، ایالات متحده می‌خواهد اسرائیل را از دور جدید تشدید تنش‌ها دور نگه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18905" target="_blank">📅 21:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18904">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بر اساس گزارش ها ترامپ به رهبران کشور های عربی اعلام کرده است برای جنگ با ایران در هفته جاری آماده شوند. @WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18904" target="_blank">📅 21:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18903">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بر اساس گزارش ها ترامپ به رهبران کشور های عربی اعلام کرده است برای جنگ با ایران در هفته جاری آماده شوند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18903" target="_blank">📅 21:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18902">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شبکه کان به نقل از مقامات ارشد اسرائیلی: ترکیه تهدید کرده بود که در صورت حمله نیروهای کرد به خاک ایران به عنوان بخشی از عملیات زمینی به رهبری موساد با هدف سرنگونی رژیم، از ایران پشتیبانی هوایی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18902" target="_blank">📅 21:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18901">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ارتش کویت: حملات جدید رژیم ایران تأسیسات متعلق به وزارت برق و آب را هدف قرار داد و باعث آتش‌سوزی و خسارات قابل توجهی شد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18901" target="_blank">📅 21:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18900">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجار در کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18900" target="_blank">📅 21:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18899">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرگزاری i24 : اسرائیل تنها در صورتی به چرخه کنونی حملات آمریکا و ایران خواهد پیوست که باور داشته باشد ایران قصد حمله دارد، یا اینکه رئیس‌جمهور ترامپ به‌طور رسمی از تل‌آویو درخواست مشارکت کند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18899" target="_blank">📅 21:34 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
