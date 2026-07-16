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
<img src="https://cdn4.telesco.pe/file/p-hI0ly1lm7c1VTKhaMth0gzLXHUlV2A-BH9E1cVMZJK35nMFBEVenufJqyVytgmMiKiMhSZw-8PipeW0OL4AsvSVTv4DKHUa4RDSIxQCltaRSvTzgS_mK-Y_kttN_AMOMJgVfwjnaLvbwxmhK7t1rDAj2_jZRvwg05tfLR6AyFWyXuz17WZhZo_F_84oiu7uPfagKdlVb0YlG3Ot02ftgh_xjncFzG_IMKxnVuggt2plHyAvbNfbzX9HElO_Cmu7UKR-tRxw6i4kf0iuOQn1DKAVvChCu1ER4wvWlxjZQvUhQruY2DltzEUVWSErjShU8GgIe0tNHUhTPsuuDBAbw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 396K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 19:40:15</div>
<hr>

<div class="tg-post" id="msg-18404">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری فارس:حملات هوایی دقایقی پیش چندین نقطه در اطراف بندر عباس را هدف قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/withyashar/18404" target="_blank">📅 19:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شاهزاده
رضا پهلوی:
سرکرده‌های رژیم آخوندها در تهران و پناهگاه‌های امن پنهان شده‌اند، اما سربازان وظیفه را در پادگان‌های آسیب‌پذیر رها کرده‌اند. او با بیان اینکه حکومت جان نیروهای نیابتی خود را بر جان ایرانیان ترجیح می‌دهد، از سربازان خواست جانشان را برای این نظام به خطر نیندازند و از خانواده‌ها نیز خواست تا حد امکان مانع اعزام فرزندانشان به خدمت سربازی در شرایط کنونی شوند. شاهزادت همچنین از اقدام مردم زاهدان و مناطق اطراف در کمک‌رسانی و اهدای خون قدردانی کرد و تأکید کرد جوانان ایران نباید قربانی بقای رژیم شوند، زیرا آینده کشور به این نسل نیاز دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/18403" target="_blank">📅 19:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حسن روحانی : قبل از آخرین جلسه ای که قرار بود تمام مسولین نظام خدمت رهبر برسند (رمضان ۱۴۰۴) احساس خطر کردم و پس از تلاش های فراوان و فرستادن پیغام های مختلف برای شخص رهبر و تیم دفتر ایشان، موفق شدم جلسه را لغو کنم
@WarRoom</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/withyashar/18402" target="_blank">📅 19:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1dea65f9.mp4?token=kjMORbZL7DI0OdorQkHMZFDnppsvqOgO1v6wivBIc30Fi7WrToDEZ6W1RrfRevGXXfS7EPAfwZsL8MlpPcfkO7l2BJtL49GKzCWHMOBc3yJYJbe0KxhebysgStsEwlr9DMNKDBlvMZqdL_F0W692DErJ_0VYg4wWflbEHQ72RBhQu5f2bM_Xvi4Dn5LGwFtPsVg9WDwm1V1iVcUs19JeyROOdb6BeHgDxPCBeaKhg14uCf6s8474Ktgp26H_WkkbvzY_SkJPt1Rr8myfw97rw18nHEbCURUiUT4aylgV8Z0ztu8_xG2zxIk8AYRnSIucEgjGMlwbY8IIhiXK1a1QFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان ، خوزستان
@WarRoom</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/18401" target="_blank">📅 19:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صداوسیما: عصر امروز یک پرتابه دشمن به روستای مسن قشم اصابت کرد
@WarRoom</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/withyashar/18400" target="_blank">📅 19:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سی ان ان: مطابق گزارش سی‌ان‌ان، ترامپ در مدت کوتاهی پس از خرید سهام شرکت‌ها توسط مدیران سرمایه‌گذاری‌اش، بیش از ۲۰ شرکت را در شبکه اجتماعی "تروث سوشال" مورد تحسین یا تبلیغ قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/18399" target="_blank">📅 18:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">@warroom
جی‌دی ونس</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/18398" target="_blank">📅 18:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir chvaie</strong></div>
<div class="tg-text">نظرت در مورد حرف‌های مفت جی دی ونس</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/withyashar/18397" target="_blank">📅 18:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18395">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">@warroom
تنگه باب المندب</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/18395" target="_blank">📅 18:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18394">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK!YΛП</strong></div>
<div class="tg-text">اون هواپیمایی که هرجوری که شده خودشو رسونده به یمن چه چیزی رو حمل می‌کرد؟</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/18394" target="_blank">📅 18:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18393">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای‌ انفجار از قشم/تنگه
@WarRoom</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/18393" target="_blank">📅 18:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18392">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه جولانی به حزب‌الله حمله کنه، پاکستان و عربستان به حوثی ها، آمریکا به ایران و اسرائیل به همهشون، روسیه هم که با اوکراین میجنگه. پس باید به زودی ناقوس جنگ جهانی خاورمیانه رو به صدا دربیاریم. جنگ جهانی ۲.۵
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/withyashar/18392" target="_blank">📅 18:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18391">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وال‌استریت ژورنال گزارش داد نیروهای آمریکایی در پیام رادیویی به کشتی‌ها اعلام کرده‌اند «مسیر جنوبی تنگه هرمز باز است». در یکی از ارتباطات، یک ملوان در پاسخ به این پیام با عبارت «گمشو» واکنش نشان داده است.
افسران نیروی دریایی آمریکا هشدار داده‌اند توان موشکی ضدکشتی و پهپادی ایران می‌تواند در صورت تشدید درگیری، تنگه هرمز را به یک «جعبه کشتار» برای نیروهای آمریکایی تبدیل کند. این گزارش تأکید می‌کند ایران همچنان دارای زرادخانه قابل توجهی از موشک‌ها و پهپادهاست که می‌تواند عبور کشتی‌های تجاری و نظامی در این آبراه حیاتی را مختل کند
@WarRoom</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/18391" target="_blank">📅 18:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18390">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانال 14 عبری: دستوری برای سیستم امنیتی تصویب شد مبنی بر اینکه حفاظت از نتانیاهو و همسرش در طول زندگی‌شان ادامه یابد، به دلیل نگرانی از احتمال وقوع انتقام‌جویی ایران از طریق ترور او. فرزندان نتانیاهو نیز در 5 سال آینده از محافظت برخوردار خواهند بود.
@WarRoom</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/18390" target="_blank">📅 18:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18389">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">رویترز،: یک مقام پاکستانی پس از واکنش یمن به عربستان سعودی گفت :رهبران ارشد ما به ایران اطلاع دادند که حملات به عربستان، حملاتی علیه پاکستان است و عربستان، خط قرمز ما است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/18389" target="_blank">📅 18:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18388">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : اگه جولانی به حزب‌الله حمله کنه، پاکستان و عربستان به حوثی ها، آمریکا به ایران و اسرائیل به همهشون، روسیه هم که با اوکراین میجنگه. پس باید به زودی ناقوس جنگ جهانی خاورمیانه رو به صدا دربیاریم. جنگ جهانی ۲.۵
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/withyashar/18388" target="_blank">📅 18:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18387">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رویترز: نیروهای پاکستانی در عربستان در حال آماده‌سازی برای اعزام برای جنگ با حوثی‌ها هستند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/18387" target="_blank">📅 18:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18386">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMeli</strong></div>
<div class="tg-text">یاشار من سرکارم تهرانپارس اومدم دیدم عکس شاهزاده رو چسبونده بودن رو دیوارا اینام داشتن تند تند میکندن
🤣</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/18386" target="_blank">📅 17:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18385">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">جلیلی : مردم میگن حاضریم تمام کشور رو فدا کنیم اما انتقام رهبر رو بگیریم.
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/18385" target="_blank">📅 17:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18384">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f54f24594a.mp4?token=Rb8xh-LU3zTQ4m2NT06LfqDLG75Yr_ZygD5SqzuskIej6A1-dI95kQ9tQpTS5gH7bjMLdf1mGHV6dpJN_eyr-GVvVultyldaOsxgEWE_49Dswz4-hUyMmqAzEAJluWb6WeaAiCkotI5hLzfLeyNwg0XSkYw-hmbaMpk4-miec6JMJcqt3WQ3JOheXYXiw1nHDd69217j1m2fdaQWLe1HpK1ShBg1vTiLXihYh8zNe7ezCu-QHfl1RsYGfRAXFL5UbHhKoSc8W9TOhFQIdGelrotGjSfbkGenidN62ayGnQ4QOnCiqc02ahaqm7X_DX__7ovZBzCdJLdEFO44f048qheoTN2tpB83fWSq4d030u35zoZDKkVdzVGShBhfIT-i-71AC69dbYTslqafSh-70GA2eYaWrAlrHH8NewV3rhG5Dc7gRdSbjh3BOz26p47fecdg9Px0hnuDPSvMSx-3M8GDO12D3sutzNzOJtxe7-mcSGiPjJNJuIgxxLfDkF_5tqW_VI6LxuvID64BMcCqrNVpKWtmXVXA6Hpxb2V8dB4a3O7JNJ_BlPkrLut6EWaI_Castk3tCxe1aKsHnB-UEhQctScyzwAytodzeFg0HUvHU9hwjaRI3r6TnZMSWKX2X3Q3KjQNlG0ZoCLbDmXNyQ-7kbm6qi_w9YKuHXJFR6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f54f24594a.mp4?token=Rb8xh-LU3zTQ4m2NT06LfqDLG75Yr_ZygD5SqzuskIej6A1-dI95kQ9tQpTS5gH7bjMLdf1mGHV6dpJN_eyr-GVvVultyldaOsxgEWE_49Dswz4-hUyMmqAzEAJluWb6WeaAiCkotI5hLzfLeyNwg0XSkYw-hmbaMpk4-miec6JMJcqt3WQ3JOheXYXiw1nHDd69217j1m2fdaQWLe1HpK1ShBg1vTiLXihYh8zNe7ezCu-QHfl1RsYGfRAXFL5UbHhKoSc8W9TOhFQIdGelrotGjSfbkGenidN62ayGnQ4QOnCiqc02ahaqm7X_DX__7ovZBzCdJLdEFO44f048qheoTN2tpB83fWSq4d030u35zoZDKkVdzVGShBhfIT-i-71AC69dbYTslqafSh-70GA2eYaWrAlrHH8NewV3rhG5Dc7gRdSbjh3BOz26p47fecdg9Px0hnuDPSvMSx-3M8GDO12D3sutzNzOJtxe7-mcSGiPjJNJuIgxxLfDkF_5tqW_VI6LxuvID64BMcCqrNVpKWtmXVXA6Hpxb2V8dB4a3O7JNJ_BlPkrLut6EWaI_Castk3tCxe1aKsHnB-UEhQctScyzwAytodzeFg0HUvHU9hwjaRI3r6TnZMSWKX2X3Q3KjQNlG0ZoCLbDmXNyQ-7kbm6qi_w9YKuHXJFR6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غروبه هرمز
@WarRoom</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/18384" target="_blank">📅 17:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18383">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مصطفی نجفی، مشاور محسن رضایی : تصمیم مهمی در تهران اتخاذ شده است؛ اگر حکومت جولانی بنا به درخواست ترامپ و فشار آمریکا دست به اقدام علیه حزب‌الله بزند، با حملات موشکی و پهپادی مستقیم ایران مواجه خواهد شد. این هشدار به جولانی داده شده است
@WarRoom</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/18383" target="_blank">📅 17:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">در اقدامی بی سابقه، وزیر دفاع عربستان سعودی و معاون فرماندهی مرکزی ایالات متحده سنتکام در 24 ساعت گذشته 2 بار با یکدیگر دیدار داشته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/18382" target="_blank">📅 17:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سی‌بی‌اس: ترامپ از رد پیشنهاد توافق هسته‌ای ایران ابراز پشیمانی کرده است
شبکه سی‌بی‌اس: دونالد ترامپ در محافل خصوصی، واشنگتن را به‌دلیل رد پیشنهاد تهران برای محدودسازی برنامه هسته‌ای مقصر می‌داند.
او معتقد است این تصمیم، فرصت کلیدی برای جلوگیری از گسترش درگیری‌ها را از بین برده است
@WarRoom</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/18381" target="_blank">📅 17:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هآارتص : ترامپ در حال بررسی عملیات زمینی در ایران و حمله به تاسیسات انرژی است
@WarRoom</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/18380" target="_blank">📅 17:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">منابع محلى از وقوع درگيرى دریایی بين نيروهاى مسلح ايران و نيروهاى ارتش آمريكا در تنگه هرمز خبر‌ می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/18379" target="_blank">📅 16:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">همه برای من زدن که میگن بندرعباس صدای انفجار میاد، ولی بچه های بندرعباس، رگباری کسی پیام نداده که بندرعباس صدای انفجار شنیده باشه.
@warroom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/18378" target="_blank">📅 16:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjX5UTr6JylIsWZa8s-6HXJLp-e4uTXSv07JXWr1M6oX0ako_eFvXsWqZlpN24oZozP_rdnNzw6zGs2Ui5fTLkze4bWohqFTk1WpW9tepRUnBTsCJ9NvKYKHQZbqF0lGaHaIt3QLr2ABE_YfAFmAQ5N-1c43C60e120SVYxTSclejGFoILeZW71vplAvEBMiRvJqL0UM9tfvJ_TK2P320CVhgpk_Z3J5dNURThyuPZSdYxoHFcseur_Baj-h5AKUt6gikTENVVtOMyv49NUwQxtKDNKu3s0h9502DF8Rrt7H9na5SGUmLN0dbRcIFKWp8YfBK2vMYpFKeGKAbjY0vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است. @WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/18377" target="_blank">📅 16:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFRbI1w1yz0BeL8n3CZA0eWynfn0sUtmxZDphs3Lb0u5f1HK6ENGGC7kEZ4Y9Hb_od4NH2_5KjFpn7S0F3GWOIt7edHW3iRpu-zSVtYRzBz2MvK58hS0hDqxxecQOIuUAHJYcTx85E5IelYG5WegI38m-rIKvszq-FjaIUpKUmKwqx3AGVsXorP-TUwsJ4qVyuAfxNWX_jnYbB8Pr925DGb1mfa7qNbLYyX_BVYrkeRBPlAjG5l9Jcf47P8o3R3s-jT4m5-npIITvct5SFsgH7C-DRpQ3goBA1IeFeaFnvFvcYU-Y1dOQM3yb6C5ohVG5TpCQwQrM2o-MZ7NQEWc7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سازمان آتش‌نشانی تهران: آتش‌سوزی مقابل شرکت مینو ارتباطی با این شرکت نداشته و ناشی از سوزاندن ضایعات توسط یک شرکت خصوصی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18376" target="_blank">📅 16:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">وال‌استریت ژورنال: ترامپ شامگاه سه‌شنبه نشستی برگزار کرد تا درباره احتمال اشغال جزیره خارگ یا بمباران کوه کلنگ گفت‌وگو کند.
ترامپ در مورد اعزام نیروهای زمینی تردید دارد؛ او بارها از بزرگ‌ترین تهدیدهای خود عقب‌نشینی کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/18375" target="_blank">📅 15:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18374">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اژیر خطر سفارت امریکا در بغداد فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/18374" target="_blank">📅 15:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18373">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کانال 12 عبری: دیشب، ایالات متحده و ایران با یکدیگر تبادل آتش کردند. آمریکا به هدف قرار دادن اهداف در منطقه ساحلی ادامه داد، اما برای اولین بار، اهدافی را در مناطق پایتخت یعنی تهران مورد حمله قرار داد. ایران نیز موشک‌هایی را به سمت کویت، بحرین و اردن شلیک کرد
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/18373" target="_blank">📅 15:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18372">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2488574cc7.mp4?token=PKJuCXAQwEDNluxnguDgeI71j_upZ8CrwAaZq3gek3ozmqIoHQgQJEw-OD6qY2iyJYNMUYwUtwXbN9FsZo1l4Xoxha5u0jqhieB76KBsnx86NxZpukokVrfTZUfIZnrr82kp1jzGbCT99i8gSvaNJ2h4mlcWDU8-yvyInd1H4q7Wg0e54ZvG5VG9JqXnl9aUPx2A4RyTsBCREx6ygGoZBqRyTRZo_7AUVlEu8bUwxCb-URuE_UnpPn35vquBN4r4BzGNj3d7llGDHz-QfAW6UHhkULLHF-RuPFaeDsIy0BSOo5XZQsT7_HgFF9IlKN7PSzct17HOPa5T-DUCpQ4gpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2488574cc7.mp4?token=PKJuCXAQwEDNluxnguDgeI71j_upZ8CrwAaZq3gek3ozmqIoHQgQJEw-OD6qY2iyJYNMUYwUtwXbN9FsZo1l4Xoxha5u0jqhieB76KBsnx86NxZpukokVrfTZUfIZnrr82kp1jzGbCT99i8gSvaNJ2h4mlcWDU8-yvyInd1H4q7Wg0e54ZvG5VG9JqXnl9aUPx2A4RyTsBCREx6ygGoZBqRyTRZo_7AUVlEu8bUwxCb-URuE_UnpPn35vquBN4r4BzGNj3d7llGDHz-QfAW6UHhkULLHF-RuPFaeDsIy0BSOo5XZQsT7_HgFF9IlKN7PSzct17HOPa5T-DUCpQ4gpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده‌های رادارگریز F-35A نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط یک فروند KC-135 Stratotanker در حین گشت‌زنی بر فراز خاورمیانه.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18372" target="_blank">📅 15:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18371">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">حمله هوایی اسرائیل به شهرکی در جنوب لبنان
شبکه الجزیره از حمله هوایی ارتش اسرائیل به شهرک النبطیه الفوقا در جنوب لبنان در ادامه نقض آتش بس خبر داد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18371" target="_blank">📅 15:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18370">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI_DGflDZX9TLzPFb6T_mAgyHcu3T83x5nq2d9wUKL-c8uCm7zFpl3zJ89oQXS1dO_bFuQmmUD9ip-lX-k-4Vtw2WX1VbVEW6PJ_waYv2MBppA7PcWDJQei88EnWOYoCFFpi6q8vDDas_2EH5GyZZYFeNNoZRIaCV40zYIM2vSl6gphsrR8vILRcBshopbsPJecGi2AfFB6NclSfSaD0mfDGoDzQTNgLI7dWib0cPldH9jZBcw9UpdDMDdht4i_3vEk-v770rMwYd-bnu2G4J7DRhlktjUoskuws23pafkD0QX6vLjnTVVITsQcySNoHE94NFUrvdDlCvknradCoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا فغانی به عنوان داور فینال جام جهانی ۲۰۲۶ بین آرژانتین و اسپانیا انتخاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18370" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18369">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش کویت: پدافند هوایی ما در حال حاضر در حال دفع حملات پهپادهای متخاصم ‌رژیم ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18369" target="_blank">📅 14:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18368">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هم اکنون موج حمله جدید رژیم به کویت و درگیری سامانه های پدافندی کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18368" target="_blank">📅 14:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18367">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ارتش ایران: کشتی‌های ایرانی به عبور از تنگه هرمز به سمت اقیانوس هند ادامه می‌دهند و اگر واشنگتن ما را تهدید کند، پاسخ ویرانگری دریافت خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18367" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18366">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : تمامی کودکان بیمارستان سرطانی اهواز در سلامت کامل هستند و حدود دویست نفر آنها به مکان دیگری منتقل شدند. این بیمارستان هدف هیچگونه حملاتی نبود. فقط چون حملات بسیار سنگین بود در اهواز و در نزدیکی آنجا، مانند تمام نقاط دیگر و تمام کودکان آن…</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18366" target="_blank">📅 14:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">استرالیا در بحبوحه جنگ ایران، هواپیماهای راداری Wedgetail را به خلیج فارس اعزام می‌کند
نیروی هوایی سلطنتی استرالیا در حال حاضر ناوگانی متشکل از شش هواپیمای Wedgetail را اداره می‌کند که به عنوان پلتفرم‌های اصلی هشدار زودهنگام و فرماندهی هوابرد استرالیا خدمت می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18364" target="_blank">📅 14:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">حمزه امرایی، معاون سیاسی استانداری همدان از حملات بامداد امروز آمریکا به نقاطی در شهرستان کبودرآهنگ در این استان خبر داده است.
جزئیاتی در مورد محل‌های مورد هدف منتشر نشده است.
پایگاه سوم شکاری نوژه همدان در شهر کبودرآهنگ واقع است.
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18363" target="_blank">📅 13:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مجلس نمایندگان آمریکا شب گذشته لایحه توقف کمک‌های سالانه ۳.۳ میلیارد دلاری آمریکا به اسرائیل را رد کرد.
رای مثبت 103 نماینده دموکرات به توقف کمک‌ها به اسرائیل بود. موضوعی که به هیچ وجه 10 سال قبل قابل تصور نبود!
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18362" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تلگراف: انصارالله یمن در حال آماده‌سازی برای بستن تنگه باب‌المندب است
حدود ۱۰ تا ۱۲ درصد از تجارت دریایی سالانه جهان از این تنگه عبور می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18361" target="_blank">📅 13:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انتخابات آینده اسرائیل؛ سختی را
ه
برای نتانیاهو افزایش یافته است
انتخابات سراسری اسرائیل قرار است روز
۲۷ اکتبر ۲۰۲۶ (۵ آبان ۱۴۰۵)
برگزار شود. در این انتخابات، شهروندان اسرائیل به احزاب رأی می‌دهند و نخست‌وزیر از میان فردی انتخاب می‌شود که بتواند ائتلافی با حداقل
۶۱ کرسی از ۱۲۰ کرسی کنست
تشکیل دهد.
بر اساس برخی نظرسنجی‌های اخیر، وضعیت حزب لیکود به رهبری
بنیامین نتانیاهو
نسبت به گذشته دشوارتر شده و احزاب رقیب توانسته‌اند حمایت بیشتری جذب کنند. با این حال، نتانیاهو همچنان شانس بازگشت به قدرت را دارد، زیرا در سیاست اسرائیل توانایی تشکیل ائتلاف نقش تعیین‌کننده دارد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/18360" target="_blank">📅 13:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromƁ۝۝M 𓆏</strong></div>
<div class="tg-text">یاشار قبر خامنه آیه آتیش گرفته کونش داره میسوزه
😂
😂
😂</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18359" target="_blank">📅 12:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cta7WRrYo1JKBLW04WslCBtnRDMoadTudq0OkClMGMY3ItrjhCTw2Iziixx_gm5tqkZDLgPYvnO--wKeVHKsVmjrxFxFM6E9oJjJuG7eeP6aBKtRFL9OJghPmd8N--HHhfhHQY2heoLsq_PbJ7Y4-qfJEaaamG4YnkJS9i1iTCKpvOsBZo5J-eAVAl8pO6iLD84LAJdw2XuC84uUx9DHzmd0D1wsMN6OyafKL9-nPIvihyZHYDgdki6SbUSffzBJwk4q6A_NqkG3pOh3xnhMcXOivnyosih1fbOjBDoEzB3d-4nuP4ty6tdispwXt9Wmizbn7XRKIPR_uWi-JU2gDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارگاه عمو قیرینیاهو وسط حرم
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18358" target="_blank">📅 12:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286e4fdb4e.mp4?token=lxnZ2N0D2-l6UxjMBng-mihdyHMtuabNetg9Myxglbqrr16k3RI5JejsreFm-9bGEWA1ZPnTcsvxDItkrc8PZkcJ8cdgipY-nQmeJeHmDQlKNIf-8K5C5ZwI-ky8eFVmq9WEM_2xWpFsiU3o_wjb8y-uHOIa8u0nllxA0J6V078he8o26V4B2pKwJVbhLjOi-FOzOuTnF3u9UiEnWGX5s0io5hbUhDaS8oqbDTwg4I3y5JokRS-jNo4n8yxsnfLCWyW60zFdd-I4KEUzkhbMq--SP3B5fhvS74jNNnZ_HPq5duRgdafk1iBLoIq10w-JU6gth-DksXIkFEmY0Yt64g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286e4fdb4e.mp4?token=lxnZ2N0D2-l6UxjMBng-mihdyHMtuabNetg9Myxglbqrr16k3RI5JejsreFm-9bGEWA1ZPnTcsvxDItkrc8PZkcJ8cdgipY-nQmeJeHmDQlKNIf-8K5C5ZwI-ky8eFVmq9WEM_2xWpFsiU3o_wjb8y-uHOIa8u0nllxA0J6V078he8o26V4B2pKwJVbhLjOi-FOzOuTnF3u9UiEnWGX5s0io5hbUhDaS8oqbDTwg4I3y5JokRS-jNo4n8yxsnfLCWyW60zFdd-I4KEUzkhbMq--SP3B5fhvS74jNNnZ_HPq5duRgdafk1iBLoIq10w-JU6gth-DksXIkFEmY0Yt64g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارگاه قیر مقدس مگه بوده که وسط حرمه ؟!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18357" target="_blank">📅 12:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سفر نتانیاهو به آمریکا، به تعویق افتاد. مراسم سناتور گراهام هم به ماه بعد موکول شد
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18356" target="_blank">📅 12:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">استانداری خراسان : یه کارگاه قیر اتیش گرفته @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18355" target="_blank">📅 12:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آتش سوزی گسترده هم اکنون مشهد سمت حرم @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18354" target="_blank">📅 12:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18352">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MzehJBsjJ6PXIvb8H7l-K1Xj3kNFgn42Y0cqrxCH7kEIRULDG47M6B7P8xVVEK2KA2yoJK7JbXh7ZPWADreAYN6915pOEn1GHfpAjMRXaVxBahXPKkoyGBKc4ftTrMkhDq23rUKhuxAfo6NEhkuStWMxeKYbULRQcc2yF6rC8xw_TqfDSaLECiWStbQ85Be3JdwcjO-FEyUI3yscKsruoY50KACnynWKFTKoQu8cAwgko04vgQtPbRhkUuCnQknN4-G-QsH_6nGLlfDsV6CRPbGkPrUfYdBx7Uu6b4YVcEkyuGnUeujQRGIuGWAWX1toca2QSbFEdIgAaXnBIoWKAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YxV9JkpK49ldBjowSNOEDwfqgG5lzq-efm-4ile3CBwkjUsx2ZIn5-8XLTKvdCBN9_0PMZM4uAtDvJ8ZfyplS8FKzTrluh1zkefAVl2pXkD0iYGEoP9iziaLG1xAAHxgvlWS1aLK5p2F23ncmcypgayBvvvhtckv4vzEg_KTrlOx1vk6iogjIwurWta6UDo_eIdYahCfqUtcjAVsDzRoc7zTO05DJ1trtO5IVR5b_tnTqK3LrAV12IGPiRjhltFwMmbaQerDxpEpvJ32q-cHMCliOyloNJM0hUC1-9sNDgL6m_YxgDl7OrCdluSm8xmh-MLR2mAhT80Sp0BzbzbmFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آتش سوزی گسترده هم اکنون مشهد سمت حرم
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18352" target="_blank">📅 12:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18351">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال الاخباریه سوریه، وابسته به رژیم جدید این کشور، از منبعی در وزارت کشور در دمشق گزارش داد که «یگان‌های ویژه، تلاش برای قاچاق محموله‌ای از سلاح‌های پیشرفته و موشک‌ها از طریق مرز با عراق را خنثی کردند.» به گفته این منبع، «تحقیقات اولیه تأیید می‌کند که محموله توقیف شده قرار بوده از طریق خاک سوریه به حزب‌الله منتقل شود.»
@WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18351" target="_blank">📅 11:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بیانیه جمع کثیری از ساکنان جنوب به اتاق جنگ :  ما ايرانيان ساكن جنوب
كشور، ترحم نمى خواهيم؛
ايرانى بدون جمهورى اسلامى
مى خواهيم.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18350" target="_blank">📅 11:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdd26b83a.mp4?token=u-i3qTVBf5rd89R59P-UIiDGjADY1FGseTgE-BbO_cQi-Hm2LFFq0a7twF0vgvsAninfFep5USHtMt-FAOxBk5aRimfHkz5COCqIaM7LriLulOJdOXV6kc-_UXyV4iNgFXHTCJIjK3RvmSaeysJKBzRRb4Ti_sS98DNHvSZpronc_CT56NQGTZ14J1xGtS_UnTeeNOtvj86oDF3vvQUGHWXzlL6WlosjQaenyuFYl85r9qplCcI-_f3P9qNcY_ti2oA_YVG4IVIRpDd-FKEjyuCYT8Bq-EItcVnqBDlwrPT3gDf029x7CwYQK7Z1CLVzrbEw6uNUleotnSZrA2B_81Ttp9dy4G2UKBjMm0evgodVHwGuiFWSVXd3wPb2r0v6hW8VSkT9NU21Iywt0UWLwcvlVgYq-XhXRInYyyt5kH4aXWduu8wfkCWJV11QpRYQRYU8fJ-rNf93vaA0P3fxJO8_Jr33fKZduCE0Oqrtcky9zexXzpPhp6s6KeZkskHa1B5XIc6q-yr3UBMMjeJLLjX5vCRYns0wdNU777gse_KZGcLNmfPpterR5qCji4ujgiUK_2P2ZeR3tQlXdxwvit_2pkM27N0-NazQUl1brJFVtea3qHEFsN3TGFxdX0vH_fRC1cih-1joL2vctDGwPriRdqM_gFdeVuEvld1dM1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdd26b83a.mp4?token=u-i3qTVBf5rd89R59P-UIiDGjADY1FGseTgE-BbO_cQi-Hm2LFFq0a7twF0vgvsAninfFep5USHtMt-FAOxBk5aRimfHkz5COCqIaM7LriLulOJdOXV6kc-_UXyV4iNgFXHTCJIjK3RvmSaeysJKBzRRb4Ti_sS98DNHvSZpronc_CT56NQGTZ14J1xGtS_UnTeeNOtvj86oDF3vvQUGHWXzlL6WlosjQaenyuFYl85r9qplCcI-_f3P9qNcY_ti2oA_YVG4IVIRpDd-FKEjyuCYT8Bq-EItcVnqBDlwrPT3gDf029x7CwYQK7Z1CLVzrbEw6uNUleotnSZrA2B_81Ttp9dy4G2UKBjMm0evgodVHwGuiFWSVXd3wPb2r0v6hW8VSkT9NU21Iywt0UWLwcvlVgYq-XhXRInYyyt5kH4aXWduu8wfkCWJV11QpRYQRYU8fJ-rNf93vaA0P3fxJO8_Jr33fKZduCE0Oqrtcky9zexXzpPhp6s6KeZkskHa1B5XIc6q-yr3UBMMjeJLLjX5vCRYns0wdNU777gse_KZGcLNmfPpterR5qCji4ujgiUK_2P2ZeR3tQlXdxwvit_2pkM27N0-NazQUl1brJFVtea3qHEFsN3TGFxdX0vH_fRC1cih-1joL2vctDGwPriRdqM_gFdeVuEvld1dM1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این به من قدرت میداد که در مقابل  حوادث و اشکالات هیچوقت خم نشوم
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18349" target="_blank">📅 11:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWNmiDrqwHTZx08S4bbAvSZstbrl6c5UG_O6XFc3R42ASed7F8g0XYfpCoR0DHNQ-cXQ5UH7tlWWSW0op5gMQ2fQHmctPIMCvSGv2DbUqi0fuNTQ2fFoy0PL3e2UpHPUYI9kAB2WIJvqfiak2Pd91ioXeNXehfTxH4RWro93YcIyXS6wkMa1x1K09P00XHqYetvIVgWxZNd5NIFtSl0J8BIB1JVqIOTF7TKjfxMKPGQ8w76uKtbCLGElyKFhy7OlLN5DKketCcXoVuckCjgRpBF6AYSEy-_2aHOb49oxQzOcWDO5iylm-IlN_MNAA9BMZLfYKdcMigWSjyKGzmyGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18348" target="_blank">📅 11:18 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18347">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گزارش های زیاد از‌ سر تا سر مازندران مبنی بر قطع شدن آنتن ایرانسل
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18347" target="_blank">📅 11:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">نیروهای دفاعی بحرين: سامانه‌های پدافند هوایی، تعدادی از حملات هوایی خصمانه رژیم ایران را امروز شناسایی و خنثی کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/18346" target="_blank">📅 10:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کپلر: ۷ کشتی دیروز از تنگه هرمز عبور کردند که هیچ‌کدام نفتکش یا حمل‌کننده گاز نبودند.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18345" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وزارت خزانه داری آمریکا؛ ۱۳۰ میلیون تتر دیگه از دارایی های ایران رو مسدود کرد!
جمع کل تترهای مسدود شده بانک مرکزی هم تو یک سال گذشته از ۱ میلیارد تتر عبور کرده...
@WarRoom
Tether = 189,000 T</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18344" target="_blank">📅 10:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتاق جنگ با یاشار : ‏قرمساقا هر چی دلقک و لمپن و خالتور تو فضای مجازی بود رو بعنوانِ کارشناس آورد تو صدای آمریکا فقط و فقط برای اینکه به پهلوی حمله کنن، تهشم میگفت صدای آمريکا بیان کننده نظرات رسمی دولت آمریکاست!
@WarRoom
🤡</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18343" target="_blank">📅 10:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">اتاق جنگ با یاشار : تمامی کودکان بیمارستان سرطانی اهواز در سلامت کامل هستند و حدود دویست نفر آنها به مکان دیگری منتقل شدند. این بیمارستان هدف هیچگونه حملاتی نبود. فقط چون حملات بسیار سنگین بود در اهواز و در نزدیکی آنجا، مانند تمام نقاط دیگر و تمام کودکان آن شهر و دیگر شهرها، در آنجا هم بسیار احساس میشد در نتیجه سوژه خوبی برای پروپاگاندا رژیم قرار‌گرفت ، تمام کودکان ایران فرزندان ما هستند و دردشان درد ما ! مانند دانش آموزان ما که صدایشان شنیده نمیشود و باید به آنها هم توجه شود !
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18342" target="_blank">📅 09:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شهر هایی که دیشب مورد حملات ارتش آمریکا قرار گرفته اند
💥
اهواز
💥
بندرعباس
💥
جزیره قشم
💥
سمنان
💥
سیریک
💥
چابهار
💥
کرمان
💥
بوشهر
💥
همدان
💥
کنارک
💥
راسک
💥
خنداب
💥
پاکدشت(پدافندی)
گسترده تر شدن موج حملات ارتش آمریکا و حمله به شهر های مرکزی
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/18341" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دفتر کاتس ،وزیر دفاع تأکید کرد که اسرائیل بر ماندن در مناطق امنیتی در سوريه، غزه و لبنان اصرار دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18340" target="_blank">📅 09:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18339" target="_blank">📅 09:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در درباره تهدیدهای مطرح‌شده از سوی ایران علیه جانش: «اصلا فکر نمی‌کند».
او در گفتگو با فاکس بیزینس تاکید کرد: «اگر به این مسائل فکر کنم، دیگر نمی‌توانم مؤثر باشم.»(۳دقیقه با زیرنویس)
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18338" target="_blank">📅 09:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اطلاعیه سپاه  استان تهران درباره صدای شنیده‌شده در پاکدشت : عملیات پدافندی بود؛ هیچ اصابتی رخ نداده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18337" target="_blank">📅 09:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18336" target="_blank">📅 08:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNarges</strong></div>
<div class="tg-text">وقتی صبح دیدم از ساعت ۲ هیچی نذاشتی، فکر کردم گرفتنت
😭
😭</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18335" target="_blank">📅 08:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وزیر علوم: کنکور سراسری در زمان مقرر برگزار می‌شود
برای برگزاری آزمون، هماهنگی‌های لازم از تأمین برق حوزه‌های امتحانی تا هماهنگی‌های امنیتی، با دستگاه‌های مختلف انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18334" target="_blank">📅 08:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مشاور رهبر در امور بین‌الملل: تنگه هرمز متعلق به ایران است و هیچ قدرتی در جهان نمی‌تواند حاکمیت ما را بر آن سلب کند.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18333" target="_blank">📅 08:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18332">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فارس: آمریکا در حملات بامدادی خود نقاطی در کبودرآهنگ، استان همدان را هم مورد هدف قرار داد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18332" target="_blank">📅 08:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">شب گذشته به فرودگاه سمنان / خنداب نیز حمله شده است
فارس ‌با تایید : سخنگوی ستاد بحران ناشی از جنگ استان سمنان: بامداد پنجشنبه، بخش‌هایی از فرودگاه سمنان هدف حملات هوایی دشمن قرار گرفت.
نیروهای دستگاه‌های امدادی در حال انجام اقدامات لازم پس از وقوع این حملات هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18331" target="_blank">📅 08:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15343948c.mp4?token=YTRLG8mM3dk_OtwwtLBx8WTAcHD1S3ZUlMOs_EHHnNxIyIA8TiIdOKi0OFMlrOtVo1N8eYJBF-fL38GSNBhzg7RxKcIXkl2KKqP9JmPoLzwIQwzhLAJb-mli1ID7yZHe1iG_YATNh8Vw39CbRHNKm7TtN6of729HcjtOVZaCXA0jKYD4Ceh9uo9ieE-bYHCUZ7NQoRn4ri1Ln4i3LjQQtP7uzLM0R3Wvt9CO7oQQ6rNbX_BLVOrD3Zwolw6ad8XrSQbHOCuZcGg-QYpHd_QmKnBGzEipjiDNTgOEibQgMBhLitKzw9xJ2NlEANm6yzFWgA7Xug3saETAEc4X-dSpYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15343948c.mp4?token=YTRLG8mM3dk_OtwwtLBx8WTAcHD1S3ZUlMOs_EHHnNxIyIA8TiIdOKi0OFMlrOtVo1N8eYJBF-fL38GSNBhzg7RxKcIXkl2KKqP9JmPoLzwIQwzhLAJb-mli1ID7yZHe1iG_YATNh8Vw39CbRHNKm7TtN6of729HcjtOVZaCXA0jKYD4Ceh9uo9ieE-bYHCUZ7NQoRn4ri1Ln4i3LjQQtP7uzLM0R3Wvt9CO7oQQ6rNbX_BLVOrD3Zwolw6ad8XrSQbHOCuZcGg-QYpHd_QmKnBGzEipjiDNTgOEibQgMBhLitKzw9xJ2NlEANm6yzFWgA7Xug3saETAEc4X-dSpYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب گذشته پدافند در شرق و غرب تهران فعال شد همچنین صدای انفجار در حوالی پارچین و پاکدشت شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18330" target="_blank">📅 08:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9Xlw51evGxdCvXbyS3EbMiMT0i_2Vz4cmiP99ANKV9TCIxDYHo9bmGt5fbAqA_61BikVbEd-6llw6HGDtvx1DYkIfs2EdyD0lVcF4xCxjp6rFZJhWnIFho5LfPrDV6MEd67sSqot6EKVGzK3_JrVGdLe-TTdZYVtMdNLiW5PnoDDy2Vu1RavGnj6Afh7PO2UoONyf7wqeDt4hPHZNRnzGAMR0rl-z0pU1bU6VR_W-BmCLtBcSzl2hIW5ufiyr6xI6h3-MTq-eF9T4_uTnDfXnE5F18LzN609hvNYUv5r7z3WhJaBpP3mAjmh1nuMBfZnj6zdQVdU6IgQMA4yPyRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایران به یک شهروند آمریکایی که در دسامبر ۲۰۲۴ در زمان «ریاست جمهوری» جو بایدن خواب‌آلود به ناحق بازداشت شده بود، اجازه خروج از کشور را داده است. او اکنون در سلامت کامل و در شرایط خوبی در خارج از ایران است. ایالات متحده آمریکا از این اقدام حسن نیت ایران قدردانی می‌کند!
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18329" target="_blank">📅 08:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c5179795.mp4?token=mLzqizEVzGToFV7CgJ4V1gKAFtLb82pF9o8cvh5RQlG3AGEZRiNX63NVDM-BkZJehXVfZA4k_m9Yxgf_5CFr8a5OI550bsavQlgVagTSCVEXSmmSKpUACSCxSc_M2hcpo1A9dS7OlV8_V3JsyC9zm6aj7V6Qy0lZpSAD6P18OxpZmGKQNZXfRvUSk1IH7T-wO5pDJbEp_8jU0c75HffedbWlUlEnTmDyOUPY0iWd84OrJw88EIGDtRLWKZDVwjpxGsBOjgMOY-udWxQOIO__0t_VUcBg9LE2CuR7qRf9Py7yAMa6ju-Hp5pRXSv9mOk2ddukmydt2uTBoYa60oHUjSGWYiBS99DburjqLWtSErtshgyEBvhiZEpQkQAF5l4KqWeD8swX5hBw3zWMb8CIfWJRA8Bqke-t8xk4cE1InThFDl2_f-wPqMSfm4vWS89dSVZvVIK81iNHvctODJFZVOtMu9AvextX4oZZ4viAnFm2EmioS_PCe_XUGO5joFyR72-bX-La12Il4TLMG4AFNgWVPsfX9sXJ8wqC_p2RQvQ1Kv9cMgVHW3EdU4jO17apOILGsPqIHdbNuSPe5bCm7swLZN1H5BTZnow06t7-E99nqZ6Md-ZkVUMO1eNsuEc739Pa1TRnyrSSL5IqVixwdzY5w2Ab2R8CtemDKT4Pw4M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c5179795.mp4?token=mLzqizEVzGToFV7CgJ4V1gKAFtLb82pF9o8cvh5RQlG3AGEZRiNX63NVDM-BkZJehXVfZA4k_m9Yxgf_5CFr8a5OI550bsavQlgVagTSCVEXSmmSKpUACSCxSc_M2hcpo1A9dS7OlV8_V3JsyC9zm6aj7V6Qy0lZpSAD6P18OxpZmGKQNZXfRvUSk1IH7T-wO5pDJbEp_8jU0c75HffedbWlUlEnTmDyOUPY0iWd84OrJw88EIGDtRLWKZDVwjpxGsBOjgMOY-udWxQOIO__0t_VUcBg9LE2CuR7qRf9Py7yAMa6ju-Hp5pRXSv9mOk2ddukmydt2uTBoYa60oHUjSGWYiBS99DburjqLWtSErtshgyEBvhiZEpQkQAF5l4KqWeD8swX5hBw3zWMb8CIfWJRA8Bqke-t8xk4cE1InThFDl2_f-wPqMSfm4vWS89dSVZvVIK81iNHvctODJFZVOtMu9AvextX4oZZ4viAnFm2EmioS_PCe_XUGO5joFyR72-bX-La12Il4TLMG4AFNgWVPsfX9sXJ8wqC_p2RQvQ1Kv9cMgVHW3EdU4jO17apOILGsPqIHdbNuSPe5bCm7swLZN1H5BTZnow06t7-E99nqZ6Md-ZkVUMO1eNsuEc739Pa1TRnyrSSL5IqVixwdzY5w2Ab2R8CtemDKT4Pw4M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که
موج حملات شامگاهی
علیه ایران در ساعت
۹:۰۰ شب به وقت شرق آمریکا (ET) روز ۱۵ ژوئیه
(۰۴:۳۰ بامداد ۱۶ ژوئیه به وقت تهران)
به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی
مراکز فرماندهی، سامانه‌های پدافند هوایی، توانمندی‌های موشکی و پهپادی، و تأسیسات پایش و دیده‌بانی ساحلی ایران
را هدف قرار دادند تا توانایی ایران برای تهدید دریانوردان و خدمه کشتی‌های تجاری که از
تنگه هرمز
عبور می‌کنند، بیش از پیش تضعیف شود. سنتکام اعلام کرد که در این عملیات از
مهمات هدایت‌شونده دقیق
استفاده شده و اهدافی در چندین نقطه، از جمله
بندرعباس
، مورد اصابت قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18328" target="_blank">📅 08:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1feec959.mp4?token=STN_eKlm0oGj392Sa7SyaGqrzRimlN0LWJWT4O9kMfPqn3Z0KTfLuFhRtWS589hpbLYj5TnMzSoBmrS_HKVTB5FT0R8lZ_ImE3FxD1-zhFBusp2Pkg193AYzNPOEOFiIA7RafqeyAtN9BbMEpyywTuIXzJJ0G-P4tZ35Te6K4lZoj-rZ5BiQztr7lgC21273FrNOwsOgzmJN3m8DDzQ6flDlZXU0UKS3DjKs_Vm-diC9I5r-m94bEpKly4USAg461uvs-R_kgPCoQhpiuSS54DMZGdcLUNSJbxJ7vs3mVFDPWI8g-DHm5qlI2Jm0ummNTsC4s2w703bnwA9Ofuq9jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1feec959.mp4?token=STN_eKlm0oGj392Sa7SyaGqrzRimlN0LWJWT4O9kMfPqn3Z0KTfLuFhRtWS589hpbLYj5TnMzSoBmrS_HKVTB5FT0R8lZ_ImE3FxD1-zhFBusp2Pkg193AYzNPOEOFiIA7RafqeyAtN9BbMEpyywTuIXzJJ0G-P4tZ35Te6K4lZoj-rZ5BiQztr7lgC21273FrNOwsOgzmJN3m8DDzQ6flDlZXU0UKS3DjKs_Vm-diC9I5r-m94bEpKly4USAg461uvs-R_kgPCoQhpiuSS54DMZGdcLUNSJbxJ7vs3mVFDPWI8g-DHm5qlI2Jm0ummNTsC4s2w703bnwA9Ofuq9jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند ثانیه از اهواز
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18327" target="_blank">📅 02:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قشم و سیریک هم گزارش صدای انفجار
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/18326" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18325">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بندرعباس رگباری دارم میزنند دوباره
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18325" target="_blank">📅 01:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آغاز حمله جمهوری اسلامی به پایگاه های آمریکا
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18324" target="_blank">📅 01:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سخنگوی سپاه: دشمن تصور نکند که می‌تواند جنگ را فرسایشی کند
عملیات‌های ایران فعلا متمرکز بر انهدام زیرساخت تهاجمی آمریکا در منطقه است. سپس گام‌های بعدی آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18323" target="_blank">📅 01:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">همین الان پایگاه هوایی بندرعباس رو زدند
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18322" target="_blank">📅 01:29 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بندر صدای انفجار
@warroom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/18321" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پدافند شرق تهران درگیر شده
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/18319" target="_blank">📅 01:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18315">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/18315" target="_blank">📅 01:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18314">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش انفجار های قشم به حدود ۱۰-۱۴ مورد رسیده
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/18314" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18313">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">استانداری هرمزگان تأیید کرد که نقطه ای در حوالی سیریک مورد اصابت موشک های آمریکایی طی اوایل بامداد پنجشنبه قرار گرفت.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18313" target="_blank">📅 01:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18312">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/18312" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18311">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بازم روستای «‌مسن» قشمرو دارن میزنند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18311" target="_blank">📅 01:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پرتاب موشک از شیراز
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18310" target="_blank">📅 00:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18309">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">قشم رو خیلی زدن پشته هم ۷-۸-۱۰ تا همه ریخت بیرون
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/18309" target="_blank">📅 00:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18308">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d120a1732a.mp4?token=js53jivl13_PyE27E8S4kCB-FTT565GonfRzJ70LmiNh3IyRpzwaDoluaXCv2ekEDDhGkQ1mRwnnAp7huR898tgPNw_g6erpmum6uPgfDEQr7T0F-pGJTR5ew4U6rVF2xVNbwvafk22KGT9hUP7LkqQibwD_TvWvN7XpCP9jQUFmv73f7hvz_ViU-2fyaxQEVQaXycqz6CDwxD3xDAK-9AKBru782JN0jQNjoC6zaPgtUnom3ITwN1CeIH0atW0bCMsSTv2w3W89Fwq6knacSX0urLoNJPdjFWT_I-m7eJm5TFpfTxWkzyWbM_f0d9dNkzeD65v3y_yOr0R5_A70rFV50iw5v95edDqvOrWpwyOr8UZ188jbrR3Bdr6HW8gQ4OgFcu3mL2EizJqFeYChsLg9NBSu85Rm_Xjzf0Ck-GOJVLZc3tISLHhSxKjbcu-YJXd7gPxKLAbr9pzZSUYXEDELvcjG4Rso_ntYnfaPi2ng4Wvg6dnBldL5pM0PggtO9CZaMLvD-z5P0yNxL281bWI2EkeHc080phOwTjs6ks67KhZkEufhqpLVdTM-Hh8ERjO_yMX7pi0XcjEZft1cGgrqaHNJbEkkKchFMDY7RUkIGrPilga3jpgTHyKQ8xpZMrVbkpFQewWRan_EV6KKvZvNhC2_rp7LmNqFGvHV83c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d120a1732a.mp4?token=js53jivl13_PyE27E8S4kCB-FTT565GonfRzJ70LmiNh3IyRpzwaDoluaXCv2ekEDDhGkQ1mRwnnAp7huR898tgPNw_g6erpmum6uPgfDEQr7T0F-pGJTR5ew4U6rVF2xVNbwvafk22KGT9hUP7LkqQibwD_TvWvN7XpCP9jQUFmv73f7hvz_ViU-2fyaxQEVQaXycqz6CDwxD3xDAK-9AKBru782JN0jQNjoC6zaPgtUnom3ITwN1CeIH0atW0bCMsSTv2w3W89Fwq6knacSX0urLoNJPdjFWT_I-m7eJm5TFpfTxWkzyWbM_f0d9dNkzeD65v3y_yOr0R5_A70rFV50iw5v95edDqvOrWpwyOr8UZ188jbrR3Bdr6HW8gQ4OgFcu3mL2EizJqFeYChsLg9NBSu85Rm_Xjzf0Ck-GOJVLZc3tISLHhSxKjbcu-YJXd7gPxKLAbr9pzZSUYXEDELvcjG4Rso_ntYnfaPi2ng4Wvg6dnBldL5pM0PggtO9CZaMLvD-z5P0yNxL281bWI2EkeHc080phOwTjs6ks67KhZkEufhqpLVdTM-Hh8ERjO_yMX7pi0XcjEZft1cGgrqaHNJbEkkKchFMDY7RUkIGrPilga3jpgTHyKQ8xpZMrVbkpFQewWRan_EV6KKvZvNhC2_rp7LmNqFGvHV83c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بزن زنگووووو
🔔
@WarRoom
رکورد جدید ۱۱ تانکر سوخترسان در خلیج فارس
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18308" target="_blank">📅 00:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18307">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گزارش انفجار های پی‌ در پی قشم
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18307" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18306">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به طرفداران ارژانتین تبریک میگم از جمله بی بی عزیز
😂
من خودم که فوتبالی نیستم ما دنبال این توپا نیستیم
😉
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18306" target="_blank">📅 00:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18305">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9690f3c84.mp4?token=RGFQ_-bK8tTadoBbqPA-Wt18jAyRrSbjbq-XITDA2p_H6vCuweOsqQlelSk-mNvJFFshna0dpjOL22ngizuLt9p-iasckWkdCCsHBEBzhRFG5q1J3lfJ1Z3iaVH6i39TChw8UnaG3-0oMvimwY8a1B-wQu6TsmrvBRNarKzCDfEbzSe3x0slAqr6-8-rSVRxbG7FenRgSYGkXWqSbu6PvcWWtdW19Fp1FHFrgc5AgXmHD-baR3F9CHHjEGSoqtVV_n7VLmbWr4ddqt0RmCGo1TjVAvzvEaqhQG4PT0yQG8q1_T5QGDMlogpmDXr6K0WolwYya62xcxhx7IaOIeeT_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9690f3c84.mp4?token=RGFQ_-bK8tTadoBbqPA-Wt18jAyRrSbjbq-XITDA2p_H6vCuweOsqQlelSk-mNvJFFshna0dpjOL22ngizuLt9p-iasckWkdCCsHBEBzhRFG5q1J3lfJ1Z3iaVH6i39TChw8UnaG3-0oMvimwY8a1B-wQu6TsmrvBRNarKzCDfEbzSe3x0slAqr6-8-rSVRxbG7FenRgSYGkXWqSbu6PvcWWtdW19Fp1FHFrgc5AgXmHD-baR3F9CHHjEGSoqtVV_n7VLmbWr4ddqt0RmCGo1TjVAvzvEaqhQG4PT0yQG8q1_T5QGDMlogpmDXr6K0WolwYya62xcxhx7IaOIeeT_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد نیروهای آمریکایی در
۱۵ ژوئیه
و در چارچوب اجرای
محاصره دریایی علیه ایران
، یک نفتکش خالی از محموله را که در حال حرکت به سمت یکی از بنادر ایران در خلیج فارس بود، از کار انداختند.
بر اساس اعلام سنتکام، نیروهای این فرماندهی نفتکش
M/T Belma
با پرچم
کوراسائو
را هنگام عبور از آب‌های بین‌المللی به مقصد
جزیره خارک
رصد کردند. به گفته سنتکام، این کشتی تجاری با وجود دریافت چندین هشدار، تلاش کرد محاصره دریایی آمریکا را نقض کند. در پی آن، یک هواگرد آمریکایی با شلیک
موشک‌های هلفایر
به دودکش کشتی، آن را از کار انداخت. سنتکام می‌گوید این کشتی دیگر به سمت ایران در حرکت نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18305" target="_blank">📅 00:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18304">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">جی‌دی ونس درباره ایران: «ما قرار نیست فقط بمباران کنیم، بمباران کنیم و باز هم بمباران کنیم.
ما تلاش خواهیم کرد از نیروی نظامی‌مان به‌عنوان یکی از ابزارهای متعددی که در اختیار داریم برای حل این مشکل استفاده کنیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18304" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18303">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین۲
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18303" target="_blank">📅 00:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18302">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18302" target="_blank">📅 00:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18301">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انگلیس ۱ ، آرژانتین ۱
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18301" target="_blank">📅 00:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18300">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef977aa121.mp4?token=X9KD5ID8CqlnSAM3ve8ziSLnVsVhuM0m-_NzIza5MmhiO5aLrtcHHMHgj_nWZlef0tog2qHdjfCvzZJV0JWI7VdWA3V2m-PdhZzZdbHXVc3jYmLr1uvDNh8AOVAdWE1KtrPhOVzULGv-Q6U0JIk-GpDJGl07fC8SLh5KFwBrnTtiMaXod6BIaHshBv4-0bkbSo1fAIHEiY6oFK0wRURNNSKm69enBGjua9Kq3fIG9bt8jl-kymETEd9Np3QUZ8I0QW-NKurvXQXXew5GkdIBQnE1oXyPgFaa4aZo5_8aQId_6EcmIiOMSxuDwxGGLPHpjXMlw7n4D313mdoMM_-kow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef977aa121.mp4?token=X9KD5ID8CqlnSAM3ve8ziSLnVsVhuM0m-_NzIza5MmhiO5aLrtcHHMHgj_nWZlef0tog2qHdjfCvzZJV0JWI7VdWA3V2m-PdhZzZdbHXVc3jYmLr1uvDNh8AOVAdWE1KtrPhOVzULGv-Q6U0JIk-GpDJGl07fC8SLh5KFwBrnTtiMaXod6BIaHshBv4-0bkbSo1fAIHEiY6oFK0wRURNNSKm69enBGjua9Kq3fIG9bt8jl-kymETEd9Np3QUZ8I0QW-NKurvXQXXew5GkdIBQnE1oXyPgFaa4aZo5_8aQId_6EcmIiOMSxuDwxGGLPHpjXMlw7n4D313mdoMM_-kow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما وارد خاورمیانه می‌شویم و آن(تروریسم منطقه) را از کار می‌اندازیم و بعد به خانه برمی‌گردیم. همه می‌پرسند چرا این کار را کردیم... ما بزرگی و عظمت بدست میارویم مثل کاری که ونزوئلا کردیم ( همه شوک شدن)
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/18300" target="_blank">📅 00:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18299">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ارسالی : شهرک صنعتی زنجان تمام شیشه هامون ریخت
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18299" target="_blank">📅 00:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18298">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ درباره ایران:
بسیار زود شکست خواهند خورد.
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/18298" target="_blank">📅 00:02 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
