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
<img src="https://cdn4.telesco.pe/file/LPcUEakLM79Uzdvf1TOP76-d1FQAtjWtGae-boeEeNEnkuZOEnLmuhanKFhMgV5RtE7_Yn89b-01BEn-SuseRP395NoS2SjhFom1AqTW6OKl_L7tTYdAongDL4QHg5TeXdieUMtBbBB9mPCda6LuUViJxBksHlc_UDi1zUsTZN3LS7gPm7ulCusY7k_x65XheQGlof47A_6vLGxKsjzxF5-lFdidBrPaUtpRJ2SG7m2BasUYnRFONH75URv1rkZ_yzBLce0_WKlgXT2rI0vAidDkkW5PWka-vJBGKjxvY0Mw9rU_UwHiXFbwpuLVYKBOXiTObn9m4L2eE3P-7LaL8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 292K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 19:37:35</div>
<hr>

<div class="tg-post" id="msg-13718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خالیباف :  نه به اتش بس پایبندن نه به گفتگو باور دارن و با محاصره دریایی و نقض توافق ها درباره لبنان نشون دادن فقط زبون قدرت میفهمن
محاصره دریایی علیه ملت ما و چراغ سبز امروز امریکا به رژیم صهیونیستی ، پایگاه ها و دارایی های امریکا و اسرائیل تو منطقه رو هدف مشروع کرد
@withyashar</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/withyashar/13718" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27f5183ea.mp4?token=qFjYHZVJkoLDttr5e_VnQLdTqW_0Ufr31TBmwytzVt1t4QcAkPpTwL2tUqIC8Gsyeqi_HybP8AhRD1tY72_n7EJhgpvcO7UNVzYLiqZ2kxKjmxDCjjV6kXz4COYHyn2Zhu9eblSyUE_W0PBPXZBxVrqz9ywgAiv1nqZ1pXKIeLPDbig6Edrbnfo6lnhZ9RfLLIqGQe_frtF37Hy7MIH2TdQ7cC1CXYqvJ-iLoctMs_s5BlJVRg-vJJ6-9Y8pai_sUQd3wxem8cQFqsJ7qkzWM5GXuLmtQ_LjdAq1-MSi7913GqiQsOH-e6ya1DFHvwto1FSu20zQXYq0qPyR0gF-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27f5183ea.mp4?token=qFjYHZVJkoLDttr5e_VnQLdTqW_0Ufr31TBmwytzVt1t4QcAkPpTwL2tUqIC8Gsyeqi_HybP8AhRD1tY72_n7EJhgpvcO7UNVzYLiqZ2kxKjmxDCjjV6kXz4COYHyn2Zhu9eblSyUE_W0PBPXZBxVrqz9ywgAiv1nqZ1pXKIeLPDbig6Edrbnfo6lnhZ9RfLLIqGQe_frtF37Hy7MIH2TdQ7cC1CXYqvJ-iLoctMs_s5BlJVRg-vJJ6-9Y8pai_sUQd3wxem8cQFqsJ7qkzWM5GXuLmtQ_LjdAq1-MSi7913GqiQsOH-e6ya1DFHvwto1FSu20zQXYq0qPyR0gF-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگزت، وزیر جنگ آمریکا، می‌گوید پرزیدنت ترامپ به دستیابی به توافقی که تضمین کند ایران هرگز به سلاح هسته‌ای دست نخواهد یافت، متعهد است و افزود که ایالات متحده آماده است در صورت شکست مذاکرات، اقدام نظامی کند.
@withyashar</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/withyashar/13717" target="_blank">📅 19:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آی۲۴ نیوز عبری:
در پی تحولات در لبنان و تهدیدات از سوی ایران: نخست‌وزیر نتانیاهو قرار است در ادامه امشب جلسه‌ای با وزیر دفاع کاتز و رؤسای دستگاه‌های امنیتی برگزار می کند
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/13716" target="_blank">📅 19:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">قطر با صدور اطلاعیه‌ای، مسیر پروازها از طریق حریم هوایی خود را تغییر داده و مسیرهای جایگزین برای هواپیماهایی که از دوحه و فرودگاه‌های عربستان سعودی حرکت می‌کنند، فراهم کرده است.
این اطلاعیه از امروز ۷ ژوئن تا ۱۴ ژوئن معتبر است.
@withyashar</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/withyashar/13715" target="_blank">📅 19:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یک منبع اسرائیلی به i24NEWS:
تفاهمات آتش‌بس (بیانیه مشترک اسرائیل-لبنان-آمریکا) از روز پنج‌شنبه این است که اگر حزب‌الله به داخل خاک اسرائیل شلیک کند، ما به فرماندهی‌های آن‌ها در ضاحیه شلیک خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/withyashar/13714" target="_blank">📅 19:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تسنیم: اسرائیل از ترس پاسخ ایران در آماده باش صد در صدی هستش
@withyashar</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/withyashar/13713" target="_blank">📅 19:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13712">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تا ۷۲ ساعت دیگه احتمالا لش خامنه ای خاک بکنن از کل دنیا سران کشورها رو مخفیانه دعوت کردن ایران @withyashar از منابع خودم جویا شدم گفتن اره مراسم چهارشنبه تا دوشنبه هست</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/13712" target="_blank">📅 18:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13711">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">صابرین نیوز به نقل از منابع آگاه
ایران قاطعانه به نقض آتش بس پاسخ خواهد داد
@withyashar</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/withyashar/13711" target="_blank">📅 18:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13710">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">تا ۷۲ ساعت دیگه احتمالا لش خامنه ای خاک بکنن از کل دنیا سران کشورها رو مخفیانه دعوت کردن ایران
@withyashar
از منابع خودم جویا شدم گفتن اره مراسم چهارشنبه تا دوشنبه هست</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/withyashar/13710" target="_blank">📅 18:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13709">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رادیو ارتش اسرائیل : اسراییل در اماده باش کامل قرار گرفته
مردم در نزدیکی پناهگاه ها بمونن
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13709" target="_blank">📅 18:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13708">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مرندی عضو تیم مذاکره‌کننده:
صهیونیست‌ها مجازات خواهند شد.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/13708" target="_blank">📅 18:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13707">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جلسه اضطراری شورای عالی امنیت ملی ایران حدود نیم ساعت پیش به پایان رسید و
«تصمیمی گرفته شده است»،
اما منتشر نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/withyashar/13707" target="_blank">📅 18:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13706">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بعد از تهدید سخنگوی کمیته امنیت ملی جمهوری اسلامی، اسرائیل حملات را شدیدتر کرد و با جنگندههای خود جنوب لبنان را به موشک بست.
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/13706" target="_blank">📅 18:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13705">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری اسراییل :احتمال دارد در ساعات آینده حملات موشکی هماهنگ شده ای از،چند جبهه به ما شود
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/13705" target="_blank">📅 18:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13704">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سخنگوی کمیته امنیت ملی در مجلس ایران، ابراهیم رضایی:
ما به حمله رژیم صهیونیستی به ضاحیه پاسخ قاطع و دردناکی خواهیم داد. باید این سگ دیوانه تنبیه شده و به جای خود بازگردانده شود.
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13704" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13703">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/withyashar/13703" target="_blank">📅 17:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13702">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">منابع عربی: تحرکات گسترده و انبوه موشکی در ایران مشاهده شده
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/13702" target="_blank">📅 17:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13701">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شبکه خبر: ساعات مهمی در پیش داریم
@withyashar
🚨</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13701" target="_blank">📅 17:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13700">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">العربیه: حزب‌الله پس از بمباران حومه جنوبی بیروت شوکه شده زیرا مقامات ایران به رهبران حزب اطمینان داده بودند که اسرائیل این منطقه را بمباران نخواهد کرد
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/13700" target="_blank">📅 17:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13699">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12e9d489ab.mp4?token=sbEpE2sL57sWRBOThndd3_dFUWo-gplmxt1-JW7z9Ls7IG0w2I6rZkmhF6xC2y8DyZLYZyupnV1AQN2t4exZbxhLutrNH3ydRu7BwIbtxHRxCCLJ3UxEWcOdPCS_ApU4RP6rEqfzwdfq1gof9FC7gwlFNR8ZYwkAtbpFYzb7ndwvedxsPP81Yvvscq8hmVacTlQ7UjK22UGJtAN6m5Tkcj6_L4QDp9vxLYM8YLCrhcvOJJmuPinD_Ofx9Zr3tY7io_TpQxRMQ3RsIRDnxYaXK4DsA7XwBLY_lH7plMlAjVneYTFKp_HZcDoGnFry9KL-PCxC7GNHijbGXhLik2VYXxhQvKWd_jbH0CQpC01ggOI2QzaRAn8TJNR-D3i7zCbDJpDXBwk13DpG0D9UrlmeSE2LJgH05MbAV8m0njhTs17yNFSbVYfXdSPPlPaoWX6PhniUi8e9TOyOpP3cQqW68qglfGRC9ky70poJFiDo77mEVCs6DzlLvFNwVglcviLwq4vGTSRyeYdk9rwIVP7qOmn3FzhxHdnPHQZIqRe9adH_lWIOFeY-yZMu0t4uDNeppl26DYf_dmd2TnH8HF7Ao52knVIHgbwDCK2VONe0MZSV6txaHI7T0Tc3C1oGBYh-d360Q9Mdw-TV78VS3WiDc4exzuaoqjMnPMyYzTXFFSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12e9d489ab.mp4?token=sbEpE2sL57sWRBOThndd3_dFUWo-gplmxt1-JW7z9Ls7IG0w2I6rZkmhF6xC2y8DyZLYZyupnV1AQN2t4exZbxhLutrNH3ydRu7BwIbtxHRxCCLJ3UxEWcOdPCS_ApU4RP6rEqfzwdfq1gof9FC7gwlFNR8ZYwkAtbpFYzb7ndwvedxsPP81Yvvscq8hmVacTlQ7UjK22UGJtAN6m5Tkcj6_L4QDp9vxLYM8YLCrhcvOJJmuPinD_Ofx9Zr3tY7io_TpQxRMQ3RsIRDnxYaXK4DsA7XwBLY_lH7plMlAjVneYTFKp_HZcDoGnFry9KL-PCxC7GNHijbGXhLik2VYXxhQvKWd_jbH0CQpC01ggOI2QzaRAn8TJNR-D3i7zCbDJpDXBwk13DpG0D9UrlmeSE2LJgH05MbAV8m0njhTs17yNFSbVYfXdSPPlPaoWX6PhniUi8e9TOyOpP3cQqW68qglfGRC9ky70poJFiDo77mEVCs6DzlLvFNwVglcviLwq4vGTSRyeYdk9rwIVP7qOmn3FzhxHdnPHQZIqRe9adH_lWIOFeY-yZMu0t4uDNeppl26DYf_dmd2TnH8HF7Ao52knVIHgbwDCK2VONe0MZSV6txaHI7T0Tc3C1oGBYh-d360Q9Mdw-TV78VS3WiDc4exzuaoqjMnPMyYzTXFFSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه پیاده‌شدن تیم ناملی از هواپیما؛
این کاروان با نام میناب ۱۶۸ کمی پیش وارد تیخوانا مکزیک شد
@withyashar</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/13699" target="_blank">📅 17:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13698">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسماعیل بقایی، سخنگوی وزارت امور خارجه ایران، در گفت‌وگو با CNN گفت:
مشکل اصلی در مذاکرات با آمریکا اینه که اونا مدام موضع خودشون و خطوط قرمز رو تغییر میدن و حرف هاشون متناقضه.
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13698" target="_blank">📅 17:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13697">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ در رابطه با مجتبی:
ولی اون به شدت زخمیه، دوست ندارم که بگم داخل ایرانه یا نه.
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/13697" target="_blank">📅 17:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13696">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ : مجتبی خامنه‌ای به شدت زخمی شده اما بسیار شجاعه
چون که خیلیا اگه جاش بودن عمرا تو این وضعیت به فکر اینکه با آمریکا چه مذاکره و توافقی داشته باشن اصلا فکر نمیکردن ولی اون براش مهمه پس شجاعه!
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13696" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13695">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b1d2798a.mp4?token=HADZ74fkjY8urIRCiCVqkfJx7T-0HOIgc96VGnFV4FaNKWsT2gmvjJNqBwcYWl1jy46adLBfDhbbmA_U9sbRGukVXJLv4WfoQyqsW9HeTnBoEZfr6hidZbRxWkq5Ay8bgotDxYuyVUfGM57T2tUedxYHoaqmJaigMOU1rf6xTRuAeKnM0y6GKqRcNoa5vkIjy1PmNk6T6H7rI94Hv_8-gvSHV-rZzMnBROgQ0JTiC6ZSmdNN6bCqv_KC4d7yPoHaZi4rBLMs4nxdOtotciS-SemquIuui0C6V-87ydcW5wNDPFDBCbTTmjX3YSuIkV4slTGWVH8t2pfzZjFJARZGvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b1d2798a.mp4?token=HADZ74fkjY8urIRCiCVqkfJx7T-0HOIgc96VGnFV4FaNKWsT2gmvjJNqBwcYWl1jy46adLBfDhbbmA_U9sbRGukVXJLv4WfoQyqsW9HeTnBoEZfr6hidZbRxWkq5Ay8bgotDxYuyVUfGM57T2tUedxYHoaqmJaigMOU1rf6xTRuAeKnM0y6GKqRcNoa5vkIjy1PmNk6T6H7rI94Hv_8-gvSHV-rZzMnBROgQ0JTiC6ZSmdNN6bCqv_KC4d7yPoHaZi4rBLMs4nxdOtotciS-SemquIuui0C6V-87ydcW5wNDPFDBCbTTmjX3YSuIkV4slTGWVH8t2pfzZjFJARZGvTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ما یک محاصره داریم. این بسیار مؤثر بوده است. و دلیل اینکه ما این محاصره را داریم این است که آنها تلاش کردند محاصره کنند، و حالا ما آنها را محاصره کرده‌ایم.
آنها محاصره‌ای ایجاد کردند، پس ما آنها را محاصره کردیم. ما محاصره نهایی را داریم.
من این را جنگ نمی‌دانم، اما اگر بخواهید آن را اینگونه تعریف کنید، فکر می‌کنم می‌توانید
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13695" target="_blank">📅 17:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13694">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ می‌گوید جنگ ایران یک «تمرین نظامی» است و اضافه می‌کند، «این برای ما جنگ بزرگی نیست
نیروهای آمریکایی را تا رسیدن به توافق نهایی با ایران در منطقه نگه خواهیم داشت
آمریکایی ها با پایان جنگ احساس آرامش خواهند کرد ، من قصد ندارم نیروهای آمریکایی را حتی در صورت آتش‌بس خارج کنم
بخشی از چالش در اجرای سریع صلح این است که مستلزم تغییر اساسی در نگرش دیرینه تهران نسبت به ماست.
ایرانی‌ها قوی هستند و به خودشان افتخار می‌کنند، و کارهایی هست که هرگز انتظار انجامشان را نداشتند، اما مجبور به انجامشان خواهند شد.
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/13694" target="_blank">📅 17:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13693">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ در مصاحبه‌ای با برنامه «Meet the Press» شبکه NBC News :
ترامپ مدعی شد: «اگر به توافق نرسیم، آن‌ها را با اقدام نظامی بسیار سخت و شدید از میان خواهیم برد. و در آن صورت، پیش از رفتن ما این کار انجام خواهد شد؛ بنابراین به هر شکلی امنیت خواهیم داشت.»
ترامپ همچنین ادعا کرد که ایالات متحده می‌تواند این فعالیت‌ها را زیر نظر داشته باشد، زیرا از ظریق «نیروی فضایی» آمریکا، «دوربین‌هایی در فضا» دارد.
او گفت: «می‌دانید، ما آنجا را زیر نظر داریم؛ کاملاً و از همه جهات. اگر کسی آنجا قدم بزند، حتی اگر خود شما آنجا راه بروید، من می‌توانم نام کوچک شما را روی نشان سینه‌تان بخوانم.»
ترامپ افزود: «و این‌ها دوربین‌ هایی هستند که در فضا قرار دارند. فناوری واقعاً شگفت‌انگیزی است.»
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/13693" target="_blank">📅 17:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13692">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ: «چند نکته باقی مانده است. حتی نکات بزرگی هم نیستند. آن‌ها پذیرفته‌اند که سلاح هسته‌ای نخواهند داشت.»
«در توافق بندی داشتیم که می‌گفت آن‌ها سلاح هسته‌ای توسعه نخواهند داد و همه از آن راضی بودند، به جز من.»
«من گفتم اگر آن‌ها خودشان سلاح هسته‌ای تولید نکنند، اما بروند و آن را بخرند یا به دست آورند، چه می‌شود؟ می‌خواهم واژه‌های “خریدن”، “تهیه کردن” یا “به دست آوردن” هم در متن باشد. چون این دیگر توسعه دادن نیست.»
«بنابراین آن‌ها نه حق توسعه سلاح هسته‌ای را دارند و نه حق خریدن، تهیه کردن یا به دست آوردن آن را.»
@withyashar</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/withyashar/13692" target="_blank">📅 16:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13691">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره‌ مجتبی خامنه‌ای به ان‌بی‌سی: اون منطقی‌تر از پدرشهِ
نمی‌خوام بگم که میدونم اون کجاست یا نه، اما احتمال خوبی وجود داره که بدونم کجاست
ترامپ: ما و ایران به امضای توافق بسیار نزدیک هستیم، اما من تهران را تحت فشار قرار می‌دهم تا از جاه‌طلبی‌های هسته‌ای خود دست بردارد
@withyashar</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/withyashar/13691" target="_blank">📅 16:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13690">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ به ان بی سی: هیچ پولی از ایران آزاد نخواهم کرد. تحریم ها هم کاهش پیدا نمی کند
اگر برای پایان جنگ به توافق برسیم، با ایران برای بازیابی و نابودی اورانیوم غنی‌شده با غنای بالا همکاری خواهیم کرد
اگر به توافق نرسیم، ارتش ایران را بیش از پیش تضعیف خواهیم کرد تا زمانی که نیروهای ما بتوانند با خیال راحت اورانیوم را بردارند.
@withyashar</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/withyashar/13690" target="_blank">📅 16:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13689">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار (t.me/withyashar) – (IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13689" target="_blank">📅 16:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13688">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ به ان‌بی‌سی نیوز می‌گوید که اصراری ندارد لبنان در توافق کوتاه‌مدت ایران گنجانده شود
@withyashar</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/withyashar/13688" target="_blank">📅 16:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13687">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری I24news: دولت ترامپ راجب حمله مطلع شده بود!
@withyashar</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/withyashar/13687" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13686">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صدا سیما: اماده باش فوق العاده ای برای وعده صادق پنج برای حمله به اسرائیل تذبیر شده است
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/13686" target="_blank">📅 16:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13685">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رادیو ارتش اسرائیل: ما یک ترور هدفمند با ارزش بالا انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13685" target="_blank">📅 16:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13684">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/13684" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13683">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromJvd</strong></div>
<div class="tg-text">یاشار : من حمله های اسرائیل به لبنان رو پوشش نمیدم
نتانیاهو: ی لحظه اجازه بدین
🤣
🤣
🤣</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/13683" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13682">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">عراقچی 48 ساعت قبل به صورت رسمی اعلام کرد در صورت حمله اسرائیل به بیروت،جنگ آغاز خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/13682" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13681">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaXvhtUeXj-w9-6GM8PPLr5JKuUH-xHCcshOvx-DBe5RkQBchhooz34ixDquP4Ae5enFS_AZACUa36uq10v9UrrKo3RUmTPqNcB6r0Ivq3eADM4lejwYJepHwDmebI-_G_T_KYtv2aDFYOrNGWa_caOS8ELxaqxuuLhe_b3Md8rmVUfJMtMpN0jNeI3QyFIu5i-43zwP7WBQrSQXxbDhGSeI-tr7JaPCRpJiNleS48ms6IShbn9CmulpXAZ_sdiwnKJuDJnkCFJK3go2HFORUmoAcVXXDYdGFCkmP6E5Rlm0fUbmy2aCFnxDS_QG0I3ubXrO67ZNEmaTDe98G2625Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساختمان هدف قرار گرفته در ضاحیه بیروت توسط نیروهوایی اسرائیل
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/13681" target="_blank">📅 15:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13680">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwmJOv3ubuUQ40zyekNviuf3NA4TreThvqueGrVpTY_wOCqUwC9xyCqFzDNSNQCrI0ibgtiYf6wXLS7tyhOGXYc9deLZKmaQ6EB5ZjOAdIwbt1YKp96TL43rZAGVUBI25k56O6rKiqOIuadFVh5EHu1DxbAAFGneHacOnQWzy1xnAgFMGLtFnP-g7X1mDt5tU19xnc_YZQASpNI_3QBnVsr30ROQLj-KmSVi19n2Xx5lMLVeDxV_NskEj1sD9yvGe3YMfbWZ3Oid6-M6ptreYU8jN-2N_F8bXZO__mrHrRnP3u6VVhqiaj4njE495I6W7FR-nT9FDvtBHlHA_MHRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست وزیر و وزیر دفاع اسرائیل در بیانیه مشترک از انجام حملات هوایی به مراکز فرماندهی و زیرساخت حزب الله در ضاحیه بیروت در پاسخ به حملات راکتی امروز صبح حزب الله خبر دادند.
@withyashar</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/13680" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13679">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نخست وزیر ناتانیاهو حمله به بیروت را تایید کرد.
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/13679" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13678">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ_Q8jhE1bU9HIu_eHdfjZRl46g80zG0T0t9vNfDgg2LxC8bwvhCMy5qZA_pe1ezlgZ_h9fA4OU-5CE0q-GXNEgqEj4fwJOXEEmqtBIsC5xM24ws6d3Sx1x7dwH7qDmZOnVu2A90YZT_zBht7NfyU28z2LUgBpZSusYubbXm3hLYrRwSqopCFrB69vXmMXsCiuvLa9-tVnnZFUMn0TfKBimjYzT3fRlCbItUMqT1QkZ_2gDr0ZkaGHeWVRAPsmtCZ9Pn7PPUgTr89-it8KawiCXH13O2m6jVNNAqOjwKU0rRwhjeBESx-XHqTjvA1v3quLHP9OO9RAXm0-edme9JfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : افسر عرشه ناو یو اس اس مایکل مورفی (DDG 112) در حالی که این ناوشکن مجهز به موشک‌های هدایت‌شونده، محاصره دریایی ایران در دریای عرب توسط ایالات متحده را اجرا می‌کند، یک کشتی تجاری را زیر نظر دارد. تا 7 ژوئن، نیروهای سنتکام 132 کشتی تجاری را تغییر مسیر داده و 6 کشتی را غیرفعال کرده‌اند تا از رعایت این ممنوعیت اطمینان حاصل شود.
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/13678" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13677">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/13677" target="_blank">📅 15:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13676">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو: صبح امروز یک تروریست پست حرکت خود را آغاز کرد، به یائیر رسید و متأسفانه پیش از آنکه از پای درآورده شود، موفق شد یک شهروند اسرائیلی را به قتل برساند و چند نفر دیگر را زخمی کند. ابتدا می‌خواهم از تیم‌های واکنش اضطراری که بلافاصله علیه تروریست‌ها وارد عمل شدند، قدردانی کنم. همچنین از مأموران پلیس اسرائیل که تروریست را از پای درآوردند و همدست او را دستگیر کردند، تقدیر می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/13676" target="_blank">📅 15:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13675">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">amme kojai(IG @yashar)</div>
  <div class="tg-doc-extra">TaTaloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13675" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/13675" target="_blank">📅 15:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13674">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/13674" target="_blank">📅 15:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13673">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/13673" target="_blank">📅 14:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13672">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیویورک تایمز: در گزارش تازه‌ای آمده است که اسرائیل در ماه‌های اخیر جاسوسی از مقام‌های آمریکایی را، به‌ویژه آن‌هایی که درگیر پرونده ایران بوده‌اند، افزایش داده و پنتاگون سطح تهدید ضدجاسوسی را به بالاترین سطح رسانده است. طبق این گزارش، نگرانی اصلی آمریکا این است که تل‌آویو توانسته باشد گفت‌وگوهای محرمانه واشنگتن با ایران را شنود کند و از مواضع داخلی دولت ترامپ درباره مذاکرات و سیاست خاورمیانه‌ای او آگاه شود.در این گزارش نام چند مقام آمریکایی هم آمده است؛ از جمله استیو ویتکاف، فرستاده ویژه ترامپ، البریج کولبی، مقام ارشد سیاست‌گذاری پنتاگون، و مایکل دیمینو، معاون او. نیویورک تایمز می‌گوید افزایش این نوع شنود و ردیابی باعث شده پنتاگون محدودیت‌های سخت‌گیرانه‌تری برای اشتراک اطلاعات با طرف‌های اسرائیلی در نظر بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/13672" target="_blank">📅 13:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13671">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه. @withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/13671" target="_blank">📅 12:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13670">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3vi0LHIxQ34trtIw816yL8hU3xhS0wVBk9HzXAdbooikcUhhAlGZ6iDv5jLwin3IxLpJv83A7A4EeEp79Prv45DRYN5zXjMKSD7slzNaw3HexClRVCDQqVWx39uOTU2CUmNUk8j5lz80t1eOZaTqWTiuvAHWSG-bnucKLkeQKSGJOXypDTlSwh3rQ9_qtsk9qIXu69rIgOnUYyBkHOLoiegtSyXUapjKXZ-L5EE8TlzlcnbCEzAsH9WYSfiMyL2zbAEMJTSGfb1CWSYQyLXCGgJDyPnENBu3WEygjIycziPSI0faf_Onf4wRNZG8PTcW325_re3JL-hndsv2b-saA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه.
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/13670" target="_blank">📅 12:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13669">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myrGlsU3_y4Dafja16taUJRouLwyUFpXqq06X4UFU8Rkks2b9P4biEZQpT3YLCPR30_u14pwojIIl8T1e_A1Csdq3fZ9Y3b6FwvPcrNPtEeQ8wTmusJw_377UgLvFDqlQKCAiGl1AEnUKdLXKMQSDxE6sID7-HhBqvSDPXi_0sHE0TBNWMqpJsMSSfD85Zc_m8JcXHPb9kYUVkIUdDtng_zoPDxo6UDMmEvNigQDync5jK7Wlnb9KTsnM2qOSqL_BldEazW4ClgKdl9jkoH-Z1fn4ZRetMx3YMl1ehiQv_Xi7qFZrVZPlrTrRMuZxTbZpZxWyzXRVu-LZapGsUOFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ پاکستان اعتراضات شده و دولتِ پاکستان اینترنت رو تقریباً کامل قطع کرده. بعد اینا شدن عباس پیگیر واسه ما فاز شخصیت و حقوق بشر گرفتنو از طرفین می‌خوان خویشتن‌داری کنن!
🧴
🚿
🧼
🧽
@withyashar</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/withyashar/13669" target="_blank">📅 12:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13668">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تلگراف : آمریکا در حال پرواز هلیکوپترها از سواحل عمان برای هدایت نفتکش ها به خارج از خلیج فارس از طریق تنگه هرمز است
شناورها سواحل عمان را در آغوش می گیرند و تا حد امکان از سواحل ایران و آب های بالقوه مین گذاری شده با اتکا به راهنمایی نیروهای آمریکا دور می مانند
@withyashar</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/withyashar/13668" target="_blank">📅 12:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13667">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر کشور پاکستان(سناتور سید محسن رضا نقوی)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود @withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/13667" target="_blank">📅 12:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13666">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کانال 12 اسرائیل :طرح موساد هنوز می‌تواند به سقوط رژیم ایران منجر شود
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/13666" target="_blank">📅 11:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13665">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">العربیه:مذاکرات متوقف شده بین ایالات متحده و ایران... و یک "پیام بسیار مهم" از پاکستان.
@withyashar</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/withyashar/13665" target="_blank">📅 10:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13664">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTqSKrNQnPBC_JKPKjK9WFjEPJZN4HobbXsOC-vi63jHzNf9oAvPSVzP2S9XAMDxq2mNRjzqE303A3n1u0uiE3Kaw_vCHEeVHu6Bmi-8w1yWnVnNi-2qFf3phsfxk4bpYA6OCfHI23vkIYYdX0PZJrbi8oTEfaKfvfqmmMmQBw0WvqkZjtoJVr3JxfVGdYlscPvdAcMeZoEweoTPDoEctGjyUmnZ1qBKM2qHsldUO4c1mMCIqg4q23Jd5xUsRXNZonXspjpKHKSAJ-5j8nfKjA4Rm-6ELNff_8e41dv1ZQM1vI7gT0-HW0v2LKAzJj3ariGS4zVIBEyKQquEWPE-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : خدای‌دریا  @withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13664" target="_blank">📅 05:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13663">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/13663" target="_blank">📅 03:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13662">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5NYmXqupScv__fvqNl5NjqfCa3kAgbWHLlMX7qvL1ge-65Z_nnAfQQW08Dwt8gIh6W0YPbEIHKUjdQtRV9zdbbIrasfqJz9GAMF9II3UZI6rh4Td4qzD_o57-6mXT2dOq4ySRCZQpczXjlmEQ6aS0Qc8Jvo-1W0JWdb5ZdO3h96lX5DdVzfcnX5-6-8QF4KUbLNHBsS-Cuizz3Y_yJN3TuZwFSI1P2-SMGXC4OvzXOawGlJv8mo6mDn2W5ZQ6PvIuN9en4TwnKAn6sAfb20M4suhg75h-u9mtZOeb0lku1UqHJUta_dtdOdJcTPJN1hHoabgueNFZVddrrbivl28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز تقریباً ۱۱۳ فروند قایق تندروی نیروی دریایی سپاه در مناطق مختلف تنگه هرمز درحال گشت زنی بوده اند
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13662" target="_blank">📅 02:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13661">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/13661" target="_blank">📅 02:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13660">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/13660" target="_blank">📅 02:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سی‌ان‌ان: اسرائیل پرسنل نظامی و اطلاعاتی خود را به‌صورت پنهانی در طول درگیری با ایران به جمهوری آذربایجان اعزام کرده @withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/13659" target="_blank">📅 02:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff55958846.mp4?token=SW0Vtu2pluu0_3uZ3JEfKHN7r9oV_vazSM7t9fAiuefMRgFTbFZ_4rZgtAwg0-yfNdGx3QjXuALoK7FrZNp1jx-g-vUUFtCiWfM9Ipra-sYmL7XD-ypu4-JSBM-tNClzbqda99zJWT7cvP-7rTu68MjExIlk-IxAMAUVf0OvYkbmxSjwgq3PjH_mWeHdiYeCHu2gcFnYyHW8md45nlyWRTdymUOMVQJ9GiKXJnvktd80UxLNzWmHMCZI_VoZJqKUpPnA_owL-qjMizHUibxIBN3_W-xfzFZFa_bI9nFM0CN7U03lEelkf7GCbBN1LtoC1nHOkaC1xI0uYE5DmnBAJiA2EZJ1Ghma9hN86RD6I0nBbZ9Y663U5s1nMgF5HfEeq4ZVPpk_CCkrJ3u460pPQiY4ES81veFd6aa5agtLcKRoEnkOqW3FKTosO2XZAUkK6o248kL8NvRQlgvrMe4EdnMeYr8pfZB0jFu2jJ_VEVZ9WFkhY-F03Wu6slQId-Ax0AtA0OW2UM0YC5hEVXNxVq5SzhccuVl4sjK-EfSwXFDXED0JKA3LAvMBbF7EGc0BvxIG_MSNm8CbWbevKjga2y8JfaBFkr_edB4CHJ3eoTgUmrfQttZ5U5Anc-hpgyGlzYajgQZGsSn2JNg-qVZAKo0Gqok11sDBknqH0ZrW7i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff55958846.mp4?token=SW0Vtu2pluu0_3uZ3JEfKHN7r9oV_vazSM7t9fAiuefMRgFTbFZ_4rZgtAwg0-yfNdGx3QjXuALoK7FrZNp1jx-g-vUUFtCiWfM9Ipra-sYmL7XD-ypu4-JSBM-tNClzbqda99zJWT7cvP-7rTu68MjExIlk-IxAMAUVf0OvYkbmxSjwgq3PjH_mWeHdiYeCHu2gcFnYyHW8md45nlyWRTdymUOMVQJ9GiKXJnvktd80UxLNzWmHMCZI_VoZJqKUpPnA_owL-qjMizHUibxIBN3_W-xfzFZFa_bI9nFM0CN7U03lEelkf7GCbBN1LtoC1nHOkaC1xI0uYE5DmnBAJiA2EZJ1Ghma9hN86RD6I0nBbZ9Y663U5s1nMgF5HfEeq4ZVPpk_CCkrJ3u460pPQiY4ES81veFd6aa5agtLcKRoEnkOqW3FKTosO2XZAUkK6o248kL8NvRQlgvrMe4EdnMeYr8pfZB0jFu2jJ_VEVZ9WFkhY-F03Wu6slQId-Ax0AtA0OW2UM0YC5hEVXNxVq5SzhccuVl4sjK-EfSwXFDXED0JKA3LAvMBbF7EGc0BvxIG_MSNm8CbWbevKjga2y8JfaBFkr_edB4CHJ3eoTgUmrfQttZ5U5Anc-hpgyGlzYajgQZGsSn2JNg-qVZAKo0Gqok11sDBknqH0ZrW7i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : خدای‌دریا
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/13658" target="_blank">📅 01:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/13657" target="_blank">📅 01:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش صدای انفجار در حوالی سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13656" target="_blank">📅 01:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از روی استوری تو اینستا وارد کامنت میشی کامنت دیده میشه ولی از پیج خود شاهزاده وارد میشی دیده نمیشه تقریبا هم ۶ هزارتا لایک خورده. من فکر کنم همه به ادمین پیج باید اعتراض کنن چون من خودم زیر یک پست دیگه اعتراض کردم اونم هیدن شد الان دوباره کامنت گذاشتم که…</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/13655" target="_blank">📅 00:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">از روی استوری تو اینستا وارد کامنت میشی کامنت دیده میشه ولی از پیج خود شاهزاده وارد میشی دیده نمیشه تقریبا هم ۶ هزارتا لایک خورده.
من فکر کنم همه به ادمین پیج باید اعتراض کنن چون من خودم زیر یک پست دیگه اعتراض کردم اونم هیدن شد
الان دوباره کامنت گذاشتم که این جور ادمین بودن خودش دیکتاتوریه</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/13654" target="_blank">📅 00:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رویترز: ایالات متحده در حال بررسی راه‌هایی است تا دارایی‌های ایرانی را در اختیار متحدان خلیج فارس قرار دهد تا به تأمین مالی بازسازی و تعمیرات ناشی از حملات ایران کمک کند
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13653" target="_blank">📅 00:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuHXx6tr3vBqqiGWeX62ssOgvQk7qhf--N_P8b3y0QBiZk2FwfS-y6q4E3TFVEhTA215Q4wvB4U51Q3N9C7hnTcDH6T5lXhWZFXFSn_3eMznBMHW29jptawV3M_SIAU1eXaPkpBGKErRLIsYkVuuEIT9x6SrZqLxlce_nKSihSACT4Nh6DmaX-63OEkMB5gGyyVfbTsdAdgnfrjzFsXFYxE2PLcn_WwI_JPFHeX8O_JPcpgRsHYUt-hha2noj-S4GscvL0GhrPVW-h8i7jBvyxEV6BJz9pqwRht22-wHYFzaooUhu-V1WGG0pLDH79wcQitjAwM15wjUI3lIjRpFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ در تروث شبیه آخر ویدیوی هست که پست کردم شبه حمله
😃
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/13652" target="_blank">📅 00:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13651" target="_blank">📅 23:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477  پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13650" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مهم ‌محمدجواد لاریجانی: سایه ترورها وجود دارد، آن‌ها هم باید بدانند که حتما بهایش را می‌پردازند و ترور، ترور دارد
کارشناس ارشد مسائل بین‌الملل: اینکه فکر کنیم در صورت تحویل اورانیوم‌ها و حق غنی‌سازی جنگ تمام می‌شود، اشتباه محاسباتی است
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/13649" target="_blank">📅 23:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/13648" target="_blank">📅 23:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خبرگزاری ایرنا به نقل از وزیر کشور پاکستان: «پیامی که برای رهبر ایران می‌برم مهم است و امیدوارم اوضاع خوب پیش برود.»
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/13647" target="_blank">📅 23:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477  پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/13646" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است @withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/13645" target="_blank">📅 22:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">https://www.instagram.com/reel/DZQKl3sRlmS/?comment_id=17866790943686477
پست جدید اینستاگرام ، کیا منتظر شب‌حمله هستن ؟!</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/13644" target="_blank">📅 22:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیویورک‌تایمز: اسرائیل مکالمات مربوط به مذاکرات آمریکا با جمهوری اسلامی رو شنود کرده.
اسرائیل تلاش‌های خود برای شنود مقام‌های ارشد آمریکایی از جمله ویتکاف و البریج کولبی، معاون وزیر جنگ آمریکا، رو افزایش داده.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/13643" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=hVohlBu_rSjsscuPBAfHHFTMObd4Ku0-h1s8D0qgsegpbt9JpLXdBRmR_TnFa8CWE5nAlMdVyXRytSYdBKx421V77OIMwcWJfaBhj5CgY4Qz22gZWfshI_QmMjgDZZtBohsw_44uHsOqSk1nJTMMG0m9m6cGlIeeA3GJM9kdPjP1SoSfGyWYcUJDIRxyCMGwcDCw1usLy1daWUI6ptBfwsfACiPPFau_a2JQ4wRy3bDqX4u0rSTXffDMoPhRF0hu8mz-pfZ8nkga8J6IFT6AD-3MK1Y2I1DSwUxbI0FqWOGKQ6uRuQQfVMm9QphoL-QbAldlfuqTp7WGYhKFJjxaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15cea3880.mp4?token=hVohlBu_rSjsscuPBAfHHFTMObd4Ku0-h1s8D0qgsegpbt9JpLXdBRmR_TnFa8CWE5nAlMdVyXRytSYdBKx421V77OIMwcWJfaBhj5CgY4Qz22gZWfshI_QmMjgDZZtBohsw_44uHsOqSk1nJTMMG0m9m6cGlIeeA3GJM9kdPjP1SoSfGyWYcUJDIRxyCMGwcDCw1usLy1daWUI6ptBfwsfACiPPFau_a2JQ4wRy3bDqX4u0rSTXffDMoPhRF0hu8mz-pfZ8nkga8J6IFT6AD-3MK1Y2I1DSwUxbI0FqWOGKQ6uRuQQfVMm9QphoL-QbAldlfuqTp7WGYhKFJjxaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نورتروپ گرومن سامانه دفاعی
«AN/AAQ-24 LAIRCM»
را برای هواگردها توسعه داده است؛ سامانه‌ای که برای مقابله با موشک‌های حرارتی و دوش‌پرتاب طراحی شده و به‌صورت خودکار با استفاده از لیزر، جستجوگر موشک را منحرف می‌کند تا به هدف نرسد.
رسانه‌ها آن را به تهدیدهای منطقه‌ای علیه هواگردهای آمریکایی و اسرائیلی در خاورمیانه وصل می‌کنند. نورتروپ گرومن می‌گوید همکنون این فناوری روی بیش از ۱۵۰۰ هواگرد از ۸۵ نوع مختلف به کار رفته است.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/13642" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=FRbcEhnOdZNbFdzA6zYA8_MXQjYr7uGLqMvbEn3fd7LvDeh1c_JA5_7RvRvBX9sI9b_TeiBwp3_qaEybW_KTklmktbjlXkj4BjVXOEsJXDrmJXw_iMpemuiu0epxdU49hJ2Auv7Y7sUWY0AJgzkrKtPGT37O25dXmQKCB_C26BUvFHB8nhXWBVKMBGqzt8yeUmn_aU0OH2ZjsKAd2eW58h7OGVTmPHnAwOriGI2_dxEpF80eZ3JK9r3IlCR5nSYAnjAO9eoPyVyWHW-UlFinh7eMIV64-QJxS626eABw0k5RAkj5XhJZjCTa2BXz6cyrKQGVrekTlSJA9DfPemAhbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3cd7dfbe.mp4?token=FRbcEhnOdZNbFdzA6zYA8_MXQjYr7uGLqMvbEn3fd7LvDeh1c_JA5_7RvRvBX9sI9b_TeiBwp3_qaEybW_KTklmktbjlXkj4BjVXOEsJXDrmJXw_iMpemuiu0epxdU49hJ2Auv7Y7sUWY0AJgzkrKtPGT37O25dXmQKCB_C26BUvFHB8nhXWBVKMBGqzt8yeUmn_aU0OH2ZjsKAd2eW58h7OGVTmPHnAwOriGI2_dxEpF80eZ3JK9r3IlCR5nSYAnjAO9eoPyVyWHW-UlFinh7eMIV64-QJxS626eABw0k5RAkj5XhJZjCTa2BXz6cyrKQGVrekTlSJA9DfPemAhbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین الان بابل پهپاد شناسایی دیدن با کلاشینکف دارن میزنند
🥴
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/13641" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13639">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مهر: صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
@withyashar</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/withyashar/13639" target="_blank">📅 21:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7q4UJ6ra4n9ilnw3VmYnexaZDuO6q8dIgkhrm-YPf0w9_5ilZW0qEy9M48aNzq7DSrrZPwO2NDedyMX9NzgwUHd_TNG2v63owEWUdbhaWjbAOYX0g-z79wx-B0iQdmO5_tRtU8076wWCxP6ZehGAzR06m69s7P6ngu7MmMd_-UVbeAXUz8RqaBS44Eqa8xnHAjTUHJEFnacEGse-X7lG9aVXJDrfGkUx4v1Lyu9SjQQV_MWjFuvMUbOPJ6lBGMiWgt_R6kGS1-7Or8o76b2zUm-ckXYwuANB_v4FmMIcriBbzlbznkllPFoZ8jvVVSCVhpc9Ca5dpBHttx9TLaxow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار وزرای کشور ایران و پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 87.6K · <a href="https://t.me/withyashar/13638" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13637">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده   https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/13637" target="_blank">📅 21:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13636">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/13636" target="_blank">📅 21:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کامنت رو رفتم زیر پست جدید پیج دوم شاهزاده
https://www.instagram.com/reel/DZQKl3sRlmS/?igsh=NzNsemFkNW9lcml0</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/withyashar/13635" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77683181b.mp4?token=t3MZxJffTUhysV7RfZreKeXk_JM9xmYy_N1SnD8wYwlMuklnjYJsuBd-IftGo9a7LVXx6KDuwLO4P66_znVL6K5xvfniryxW5avXc-qkNnQKeqXBgW-AD4Yhq9RjNc6n5WfJuf3z06uIQtgX2b3u8Sitl1oBZi_F_RlR3mCHj5uQ837mIAReMGgfSdzqU9okLoP1jZS4b4m3hDJVKE8TSxum3y9NXGQGT0EBXxDW88xUhsRu4iOKqa7uGa0bQ4AsskUStr9NUQgpVB8h2I5Zx57H6JLurWYt2mwM9bW3peZroTc3Gw09Wj_FCwEyRWFildnHWavDE8OfGTNT7n8Gaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77683181b.mp4?token=t3MZxJffTUhysV7RfZreKeXk_JM9xmYy_N1SnD8wYwlMuklnjYJsuBd-IftGo9a7LVXx6KDuwLO4P66_znVL6K5xvfniryxW5avXc-qkNnQKeqXBgW-AD4Yhq9RjNc6n5WfJuf3z06uIQtgX2b3u8Sitl1oBZi_F_RlR3mCHj5uQ837mIAReMGgfSdzqU9okLoP1jZS4b4m3hDJVKE8TSxum3y9NXGQGT0EBXxDW88xUhsRu4iOKqa7uGa0bQ4AsskUStr9NUQgpVB8h2I5Zx57H6JLurWYt2mwM9bW3peZroTc3Gw09Wj_FCwEyRWFildnHWavDE8OfGTNT7n8Gaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فعالیت جنگندهای ناشناس در آسمان بندرعباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/13634" target="_blank">📅 20:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/13633" target="_blank">📅 20:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=tI9hRoFnyb7yYu9QKXVYE2FOvtWBPfsJmZcKX_d57WKZHfRi4YALSmdjwd_Yu35LdSB76iRy6h2Gcb_LbI0wNKRq_VCGWKqZGD9hejAi-P8awnPS5BnR8HpQQLHq1XtHVqjiksqlRLYc1XBIgrTqAVa4jFPqB6qldrmmldVvWHnsGWMoNwOqgNLan-fXYpDExusmSuT6ejMX26OSMEOxkEtkc4UM8HhVFZn5WcCp7RdLO0XAChI2AubcSWr1tIYz3AVd4zyjrIYjg17uh1qQCgbgnaVdh6MjdZ-6IChyPcdT74EyGtaLuYkhBY98dbxBRkh5vf3BSu6SE8Y36CH-8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6234155d.mp4?token=tI9hRoFnyb7yYu9QKXVYE2FOvtWBPfsJmZcKX_d57WKZHfRi4YALSmdjwd_Yu35LdSB76iRy6h2Gcb_LbI0wNKRq_VCGWKqZGD9hejAi-P8awnPS5BnR8HpQQLHq1XtHVqjiksqlRLYc1XBIgrTqAVa4jFPqB6qldrmmldVvWHnsGWMoNwOqgNLan-fXYpDExusmSuT6ejMX26OSMEOxkEtkc4UM8HhVFZn5WcCp7RdLO0XAChI2AubcSWr1tIYz3AVd4zyjrIYjg17uh1qQCgbgnaVdh6MjdZ-6IChyPcdT74EyGtaLuYkhBY98dbxBRkh5vf3BSu6SE8Y36CH-8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/13632" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13631" target="_blank">📅 20:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3jpP6KzYsFXa7Dzm2y1Vi-c2E3JSr-rYT6zFR-QugeUyQ_i8SgT7Ir0l1wNl7hUtrn5GG5id8qq7GEz5Cb3MHBJSqnuKaam2iJzhkMaBlbnPYYoVOur6TF9tEzHhtFb3X7cV_QxV6SHPRzsPa2qjqKmtaLm30BS6PfQg3AAmLMULkOcZ7Kjf9IlDl8raXarMqPtJnqCrNl38l2is2r6Jm_GPSKAalZDGpr2lhyigmuWh7uU6uqA0NIvhH66_f9Fo9AdvKsPw_MHZq7MIXMgvp8fPpX_Pxk9s0SLNO6zzyjhplmhHOGMPviIvXKrE_p-92_sXwgzOie27oScuexMig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ ایران و بستن تنگه هرمز، به صادرات تکنولوژی‌های پاک چین مانند باتری، خودروی برقی و ... منجر شده و به بیشتر از ماهی ۲۰ میلیارد دلار رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/13630" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13627">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">العربیه:
ترامپ به میانجی‌ها اطلاع داد که مذاکرات با ایران بیش از 60 روز ادامه نخواهد داشت که این مهلت در روز های آینده به پایان می‌رسد و ایران باید به‌سرعت پاسخ دهد.
« این خبر فیکه که پخش شده »
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13627" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13626">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=GX6idBIQDcraB6ZsDQrvTjk17OrAFZyW-3XZECo11UT8gjGbiPFX2XZKXXPGnOfxyadTSQZnz0OmplYK40fmQryh7ynSdXG59fI9p8QgU_sYuFy7TK7EEYeBNm59LHcwHnis-2J6Cctex74pIsl4QCrb_-9aONVXIY2nFO_7Gb4O-sRgqYN_Z4byOAoQXUQq8tmwx8_-I6sDdnQBKbPhaRKZr1jfMzNyCXtm7Ey4u1ouhPyEyPa1LQfSDCM90W-jYiiAOfj-4dhhg8jFHzzeM5jB_05gPNgoXLNQSBcorSFyHxivzZJWDx2x4lc6ZrAxql5Od4I8WQUVRhRV5HyltUhGfiVQnz8T18R_ywLsJoMiSiBLVx3fTspLnd4Ik0T5IlddAWBQjs1LEfB5G2w9qjzXI70Kzk_3yanVtkeRzOnPbsJMwIrUZyRDKh_bmew2uHWQtW0qkCC_vnlC8oOS8eGNsStqkJZMuwd4D0ONFOXkQR6QV4_HDRY53U4zIrOOWM1h1cDG0IXODwLBs9YHzT2h3yCGtDOCTwbh5Obvh87UjiCp5LQQQxJrelC2khuZLvfUtvGtl795pF0zA6D-j0MxlseMc1mcbnp-FutF6izCjJdattSckQBPkA9_-XdPMVk4YHQT5pMsCfMCFTMjkOCm6YIn6Ik0qNbnx3TgRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d35551fc6.mp4?token=GX6idBIQDcraB6ZsDQrvTjk17OrAFZyW-3XZECo11UT8gjGbiPFX2XZKXXPGnOfxyadTSQZnz0OmplYK40fmQryh7ynSdXG59fI9p8QgU_sYuFy7TK7EEYeBNm59LHcwHnis-2J6Cctex74pIsl4QCrb_-9aONVXIY2nFO_7Gb4O-sRgqYN_Z4byOAoQXUQq8tmwx8_-I6sDdnQBKbPhaRKZr1jfMzNyCXtm7Ey4u1ouhPyEyPa1LQfSDCM90W-jYiiAOfj-4dhhg8jFHzzeM5jB_05gPNgoXLNQSBcorSFyHxivzZJWDx2x4lc6ZrAxql5Od4I8WQUVRhRV5HyltUhGfiVQnz8T18R_ywLsJoMiSiBLVx3fTspLnd4Ik0T5IlddAWBQjs1LEfB5G2w9qjzXI70Kzk_3yanVtkeRzOnPbsJMwIrUZyRDKh_bmew2uHWQtW0qkCC_vnlC8oOS8eGNsStqkJZMuwd4D0ONFOXkQR6QV4_HDRY53U4zIrOOWM1h1cDG0IXODwLBs9YHzT2h3yCGtDOCTwbh5Obvh87UjiCp5LQQQxJrelC2khuZLvfUtvGtl795pF0zA6D-j0MxlseMc1mcbnp-FutF6izCjJdattSckQBPkA9_-XdPMVk4YHQT5pMsCfMCFTMjkOCm6YIn6Ik0qNbnx3TgRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ در تروث
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/13626" target="_blank">📅 16:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13625">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5-CY-T4ulJELPOPnLDyVv2JxesCWODZVFjiLHCwoPiDsNRoOxCBIRSTpDSfjjVEM_8vF2AcysndyIdlrzG4zG8hTguzM-BKHzUIxg5YxNVgrlbi87dFfZIbZ5lmJFtgx5is_QlOjJd7Qfmpov62Jy6VM_iLuXjmy92PLdOzhKhKbToYykHSUY_db1AsjupuEJKGZzX2rM7dxN_yxXHrcWf8p3F_SpfPL-OVfsgTdGXH2iJzH9-wZwfAx7FpdM6JIfbOp6xcUDPw4VEksemcGRqOJ1afH0fF19Lvc0-vrGlERfzCcEzIjvdlykQSjrOpqfbPotWiRS6WzFZLmoACqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکل مخابراتی پایگاه شهید راهبر نیرو دریایی سپاه در بندر سیریک که شب گذشته، هدف پرتابه‌های آمریکایی قرار گرفت
پیش‌تر اسکله این پایگاه در طول جنگ هدف بمباران آمریکایی ها قرار گرفته بود.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/13625" target="_blank">📅 15:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13624">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزرای کشور کشورهای عضو شورای همکاری خلیج فارس (GCC) جلسه اضطراری تشکیل می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/13624" target="_blank">📅 15:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13623">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مدیرعامل آسیاتک: اینترنت دیتاسنترها همچنان قطع است
مدیرعامل شرکت آسیاتک، با اشاره به تداوم مشکلات دسترسی به شبکه در بخش‌های تخصصی، اعلام کرد که برخلاف برخی اظهارنظرها مبنی بر بازگشت وضعیت اینترنت بین‌الملل به شرایط پیش از دی‌ماه سال گذشته، دسترسی مشتریان مراکز داده (دیتاسنترها) همچنان برقرار نشده و کسب‌وکارهای اینترنتی کماکان با چالش مواجه‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/13623" target="_blank">📅 15:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13622">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ به میانجی‌ها گفته ایران باید زود جواب بده
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/13622" target="_blank">📅 14:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13621">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13621" target="_blank">📅 13:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13620">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدای انفجار قشم
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/13620" target="_blank">📅 13:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13619">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">(IG @yashar)‎⁨منتظریم کی شب حمله فرا می‌رسد⁩</div>
  <div class="tg-doc-extra">اتاق جنگ با یاشار (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/13619" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/13619" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13617">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">وزیر کشور پاکستان(
سناتور سید محسن رضا نقوی
)امروز به تهران می‌آید تا تلاش کند در مسئله دارایی‌های ایرانی مسدود شده، پیشرفتی حاصل شود
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13617" target="_blank">📅 12:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13616">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=ZcKo91uLKjZ9Eed5IqFQw_H3zYYNghywFMpY7D9kg8CNa2rEaHPs0zl1Jwk9sGUCE0ZEtK-obqOk7XDFsH-2IrY7oIhMAxp67hdYyTjpryiwQc0dMvNqv-_zdtXpJE4nMkF0d7CF14OPyZFj87gltR2mukwUBYF2K6iZV3iXx3w8cKcfCaEXzS9C69vjiefw_bcMVXgH7nt_Ywm5rtZBpkoa4z1LjDOQoKUzZfiVEuKYBRbwh0E5FH_vGNYG2tfxZMC_1GHULFdXUT8XAbwXgbua0Omk4bFOc2jlwZesqCYiTpRJT1owiUWLg3Z4pDC6bTrwtU0Qy1TQ0DwCF---QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d357648b.mp4?token=ZcKo91uLKjZ9Eed5IqFQw_H3zYYNghywFMpY7D9kg8CNa2rEaHPs0zl1Jwk9sGUCE0ZEtK-obqOk7XDFsH-2IrY7oIhMAxp67hdYyTjpryiwQc0dMvNqv-_zdtXpJE4nMkF0d7CF14OPyZFj87gltR2mukwUBYF2K6iZV3iXx3w8cKcfCaEXzS9C69vjiefw_bcMVXgH7nt_Ywm5rtZBpkoa4z1LjDOQoKUzZfiVEuKYBRbwh0E5FH_vGNYG2tfxZMC_1GHULFdXUT8XAbwXgbua0Omk4bFOc2jlwZesqCYiTpRJT1owiUWLg3Z4pDC6bTrwtU0Qy1TQ0DwCF---QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همکنون پرواز هواپیمای اف-۵ ئی
تایگر ۲( تک نفره )متعلق به هوانیروز جمهوری اسلامی برفراز مشهد
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/13616" target="_blank">📅 12:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13615">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MivWLE3IB9oURcMsebQ-49rfn2ifEBQajYc1AVOuYywhNPYkcpfj6sRRUl4_EcU9iuEokN8wbo3Mawb0tjKEdw__F4trXxkv40gKGZs7L837HoJ5qqAngmYs6WmBGklCLhybww1BkdV2_IPjdbyCw3IMsfRfaWFT0S9vd9vXa-XRN_54QC-o2diWvCtd6osySmoG7cM--MPf09lNqmwPteKjvrieQKukHwD-W_f3d6mBzbcuGrlQDi0nmCEc0MI3lYVo_61ueiihAOfN75oaqeMmgunH7W2qP9eLy2m6xMFuJxtelIHO7Suz6N7PrT-cX7IX0OupbdxFA35ysn198w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس های جدید پایگاه هفتم شکاری شیراز بعد از جنگ
@withyashar</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/13615" target="_blank">📅 11:32 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
