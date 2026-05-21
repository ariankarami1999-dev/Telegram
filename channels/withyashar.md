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
<img src="https://cdn4.telesco.pe/file/fkji1fAccef8nQhzInt21SAqWLXMZ40SgF_hOJrgasQCk3_ZWgjOzD-DNagm2aQR7wLdjDpZEXjKn1RjW1N6AcHD3J9z7o4f_y_pj8LLuSsH0ZkjYvjEIE02ipj7n0AwT_WxJrJhi-DISWXdcPaK0zvAciSwLF4a05quThAFdFDvxti1CO4gqFZwphoiR3YEbfrOOXgldvBx1NzTXb7xh1IR_DDcL_UsHmy_xo6mIFEwVwSJweu1JLpbQiIwjdIy0LRlzd298xvsfBoNtUamwn_x1ReJgfFqOiXHrxbkYyuqMkOeSalfwgv4Mu-juSVYPWGv-LG4VLRiKE4Q8annrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 268K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-11845">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/withyashar/11845" target="_blank">📅 17:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11844">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/withyashar/11844" target="_blank">📅 17:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11843">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شاهزاده رضا پهلوی: جمهوری اسلامی از روز اول ایران برایش مطرح نبود. رژیمی که به جای پرداختن به مشکلات اقتصادی ایران، میلیون‌ها دلار صرف حزب‌الله و حماس می‌کند. در بیروت بیمارستان برایشان می‌سازد. در حالی که مردم پشت در بیمارستان‌ها در ایران از بین می‌روند.
غیر ممکن است از چنین نظامی انتظار داشته باشید که از دید منافع ملی کشور به قضیه نگاه بکند. این رژیم از روز اول در جهت «مصلحت نظام» عمل کرده. نه به نفع منافع ملی
@withyashar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/11843" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11842">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1663101b52.mp4?token=iWmN-P1hGXIJUnM1itIiUw2blQBl967FBDHApGDpLck3yVXsKFUYm8s5ETR2tYl1dSb2Q-BdC6xiTSep9B2VE7Migew8XPEd4lkC4d07aBTa8DYQuFn3VqbKkuLhd1T1-7CIjN48tHMnxyOFxNDq8eC3x6Wu0VeQMX4oCoRmxAS-pAHsHtrholo3wyHTNntvnXbMJZy7jvY1xtpV1DcLRaxbzAize0KVgHXdTVif6wsE_whH5-tW1iQ9c1MNi-yYqzU-TbaBFLpsyAQO6trDHEXc4eseZ7Kd885ecfeoKPGoUEE3alY1jmxytub-7fRwSf2wtFFfi4hok7gPHMV0Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1663101b52.mp4?token=iWmN-P1hGXIJUnM1itIiUw2blQBl967FBDHApGDpLck3yVXsKFUYm8s5ETR2tYl1dSb2Q-BdC6xiTSep9B2VE7Migew8XPEd4lkC4d07aBTa8DYQuFn3VqbKkuLhd1T1-7CIjN48tHMnxyOFxNDq8eC3x6Wu0VeQMX4oCoRmxAS-pAHsHtrholo3wyHTNntvnXbMJZy7jvY1xtpV1DcLRaxbzAize0KVgHXdTVif6wsE_whH5-tW1iQ9c1MNi-yYqzU-TbaBFLpsyAQO6trDHEXc4eseZ7Kd885ecfeoKPGoUEE3alY1jmxytub-7fRwSf2wtFFfi4hok7gPHMV0Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترسناکترین سناریو جام جهانی
😂
@withyashar</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/withyashar/11842" target="_blank">📅 16:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11841">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">رویترز:  رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند @withyashar</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/withyashar/11841" target="_blank">📅 16:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11840">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ در تروث: مقاله نیویورک پست را انتشار داد با عنوان «چگونه تهران را در سه حرکت درهم بشکنیم»
۱-
ادامهٔ محاصره و جنگ اقتصادی
آمریکا باید با محاصرهٔ دریایی، تحریم و بستن راه‌های دور زدن تحریم‌ها، اقتصاد ایران را تحت فشار شدیدتر قرار دهد تا حکومت از نظر مالی ضعیف شود.
۲-
تقویت برتری انرژی آمریکا
با افزایش نفوذ انرژی آمریکا در جهان، هم اثر افزایش قیمت نفت کنترل می‌شود و هم نفوذ چین تضعیف خواهد شد.
۳-
کنترل تنگهٔ هرمز با قدرت نظامی
نویسنده پیشنهاد می‌دهد ارتش آمریکا با عملیات دریایی و هوایی مسیر تنگهٔ هرمز را تحت کنترل بگیرد و آزادی عبور کشتی‌ها را تضمین کند؛ اقدامی که به گفتهٔ او باید همراه با تهدید جدی ایران در صورت نقض آتش‌بس باشد
@withyashar</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/withyashar/11840" target="_blank">📅 16:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11839">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استوری علی کریمی : "اولين راه براى فهميدن ميزان هوش يك حاكم، نگاه كردن به آدم هايى ست كه اطراف او هستند."
"نيكولو ماكياولى"
@withyashar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/withyashar/11839" target="_blank">📅 16:18 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11838">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرنگار:
پیام شما به خانواده‌های آمریکایی که از گسترش هوش مصنوعی نگران هستن چیه؟ اونا می‌ترسن که بچه‌هاشون تو آینده نتونن شغلی داشته باشن...
ترامپ:
ایران نباید سلاح هسته‌ای داشته باشه.
😬
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/11838" target="_blank">📅 16:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11837">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">بر اساس تازه‌ترین نظرسنجی فاکس نیوز، ۶۵ درصد رأی‌دهندگان معتقدند آمریکا در جنگ با ایران در حال پیروزی است.
این در حالی است که وزارت خارجهٔ ایران در حال بررسی آخرین پیشنهاد صلح آمریکا است و هم‌زمان میانجی‌های پاکستانی برای پیشبرد توافق به تهران سفر کرده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/withyashar/11837" target="_blank">📅 16:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11836">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار فاکس‌نیوز در تل‌آویو: ترامپ و نتانیاهو، در یک تماس تلفنی حساس، درباره گام‌های بعدی در خاورمیانه گفتگو کردند.
@withyashar</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/withyashar/11836" target="_blank">📅 16:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11835">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع اسرائیلی به رویترز:
ترامپ به اسرائیل قول داد که اورانیوم غنی‌شده از ایران خارج شود و هر توافق احتمالی شامل این بند خواهد بود
!
@withyashar</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/11835" target="_blank">📅 15:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11834">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یزدی خواه: اینترنت جهانی فعلاً بازگشایی نمی‌شود/ دسترسی ویژه برای گروه‌های موردنیاز برقرار است
@withyashar</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/11834" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11833">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/11833" target="_blank">📅 14:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11832">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رویترز:  رهبر ایران دستور داده است که اورانیوم با درجه نزدیک به تولید سلاح باید در ایران باقی بماند
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11832" target="_blank">📅 14:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11831">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ادعای اندیشکده آمریکایی: طبق ارزیابی کارشناسان، وحیدی و اعضای حلقه نزدیک او کنترل نه‌تنها پاسخ نظامی ایران در این درگیری، بلکه سیاست‌های مذاکراتی تهران را نیز در دست گرفته‌اند.
@withyashar
من دو هفته پیش در این ویدیو به این مسئله اشاره کردم
https://www.instagram.com/reel/DYIY6lnxd_R/?igsh=bjlqYWRvcDZ5NHIz</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/withyashar/11831" target="_blank">📅 14:08 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11830">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر کشور پاکستان با احمد وحیدی، فرمانده سپاه پاسداران در تهران دیدار کرد. @withyashar یکی اینو آخرش از سولاخ کشید بیرون دیگه مابقی با موساده
😅</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/11830" target="_blank">📅 14:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11829">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تایمز اسرائیل:  ایران در جریان آتش‌بس از فرصت برای جابه‌جایی لانچرهای موشکی و آماده‌سازی برای دور جدید درگیری استفاده کرده
@withyashar</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/withyashar/11829" target="_blank">📅 13:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11828">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">روسیه: ایران به تنهایی باید در مورد سرنوشت ذخایر اورانیوم خود تصمیم بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/11828" target="_blank">📅 13:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11827">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش های تایید نشده از ۳ انفجار در بندر عباس و قشم
@withyashar</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/withyashar/11827" target="_blank">📅 13:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11826">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همکنون زلزله در بندر عباس
@withyashar
مرحله بعدی زامبی و گودزیلا است</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/11826" target="_blank">📅 13:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11825">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏علی قلهکی : آمریکایی‌ها پس از دریافت نظراتِ ایران، پیشنهاد کرده‌اند که «پایانِ جنگ در تمامیِ جبهه‌ها»، «رفع محاصره تنگه هرمز توسط آمریکا»، «بازشدن تنگه هرمز توسط ایران با تعرفه و مسیر دریایی مدنظر ایران»، «آزادسازی ۲۵٪ از اموال بلوکه شده ایران _حدود ۲۵ میلیارد دلار»، «معافیتِ فروشِ نفت ایران به مدت ۳۰روز» و فازِ اصلیِ مذاکره یعنی «خروجِ ۴۰۰ کیلو اورانیوم از ایران _در بهترین حالت ارسال به کشور ثالث_» و «قبولِ حقِ غنی‌سازی ۳.۶۷ ٪ برای ایران (بعید است در فاز نهایی آمریکا آن را بپذیرد)» و «تعطیلی مراکز هسته‌ای _منهای راکتورِ تهران صرفا با کاربرد پزشکی) به طور یکجا توسط ایران امضا شود!
‏ایران می‌گوید تمام فازهای پیشنهادی آمریکا  برای راستی‌آزمایی به مدت ۳۰ روز انجام شود تا هم ایران نفت خود را بفروشد و هم‌مُجاب شود در بحث هسته‌ای مذاکره را انجام دهد!
‏پی‌نوشت: ۱. اختلاف جدی بَر سَرِ مباحث هسته‌ای است؛ «۴۰۰ کیلو اورانیوم» خط قرمزِ دیکته‌ای اسرائیل برای آمریکاست! ایران ۴۰۰کیلو اورانیوم را نمی‌دهد، غنی‌سازی را هم حتما می‌خواهد و ۲۰ سال آن را تعلیق نمی‌کند. ایران با ارسال ۴۰۰ کیلو اورانیوم به کشور ثالث _چین و روسیه_ موافقت نکرده، آمریکا هم همینطور و خودش آن را می‌خواهد. نقطه‌ی جدی شکستِ توافق اینجاست. ایران مذاکره بر سر «پرونده‌ی هسته‌ای» را جُدای از «پرونده بازگشایی تنگه هرمز» و «اتمامِ جنگ» می‌داند!
‏۲. ایران و آمریکا سر فاز بندی توافق اختلاف دارند؛ ایران یکجا توافق نمی‌کند و آمریکا دنبالِ توافق یکجاست!
‏۳. آمریکا متعهد به متون و محورهای ارسالی نیست؛ محورهای ذکر شده با اینکه فاصله جدی با شروط ایران دارد ولی همین‌ها هم توسط آمریکا به مرحله اجرا در نمی‌آید!
‏۴. آمریکا تحریمی را لغو نمی‌کند؛ شاید تعلیقِ مدت‌دار در بهترین حالت، قسمتِ ایران در توافق شود.
‏۵. بر فرض توافق با آمریکا، هیچ تضمینی برای جلوگیری از ترور سطح بالا توسط اسرائیل نیست!
@withyashar</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/withyashar/11825" target="_blank">📅 13:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11824">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f70e8f6f5.mp4?token=pioducl-_ULHAAmgNpIgNzeiOWdhUAPz0EJ5t29VDAfYY2ikVEGolgG8mf0WHdCbA179wKZKdw0svKQxDudEBTL3PgHksDQLGruRwS7PS5G3fzN0UbE9jl8negrlch6KPv3s-kX0RMfgdgowsTZMBB_VtLUfE64SIwGoyN8jcF7VB8S_ldx__mQ1rdvmOQkQPg6FXb21p8wtuvS1WMwttvX2WgkzDifdg-cvicJP8VEOSrwfW7kMVYE2t2J5WuDH0mB4PRWA1WDe345Qpz62pqmIiSqIWkmnjkwAXInvNWbIdpjlmafaeJ_jbYfVmCKh1pYbWlA5vkoNK0Z5UL7YKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f70e8f6f5.mp4?token=pioducl-_ULHAAmgNpIgNzeiOWdhUAPz0EJ5t29VDAfYY2ikVEGolgG8mf0WHdCbA179wKZKdw0svKQxDudEBTL3PgHksDQLGruRwS7PS5G3fzN0UbE9jl8negrlch6KPv3s-kX0RMfgdgowsTZMBB_VtLUfE64SIwGoyN8jcF7VB8S_ldx__mQ1rdvmOQkQPg6FXb21p8wtuvS1WMwttvX2WgkzDifdg-cvicJP8VEOSrwfW7kMVYE2t2J5WuDH0mB4PRWA1WDe345Qpz62pqmIiSqIWkmnjkwAXInvNWbIdpjlmafaeJ_jbYfVmCKh1pYbWlA5vkoNK0Z5UL7YKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای تیم ملی فوتبال ایران برای درخواست ویزا به سفارت آمریکا در آنکارا مراجعه کردند
@withyashar</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/withyashar/11824" target="_blank">📅 12:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11823">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">الجزیره به نقل از یک منبع پاکستانی:
مقامات ایرانی از پاکستان خواسته‌اند تا مهلتی برای ارزیابی و بررسی معیارهای آمریکایی برای مذاکره دریافت کند.
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
ژنرال منیر هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
@withyashar</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/withyashar/11823" target="_blank">📅 12:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11822">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8D7vL0-IKC6-JTLGEVCXrWkBDTcIDxB13YKtLsvWGwLbQypHdyHma5NJ_367cAIG-yyiqodSfDOcLeGCPxAB-6BAk5MHOktBX_M7snDidmIlrnSTDNQMwNeWxQCdadUBGfotdW5eEGDFj16Y-J2KQyTI09lb1KwTU1lL3N-fujiHU1meZBA6apMizchESkfQfn_FO3R0dVGwhjSQT7WY_20EFGvL1a8PjENLdax4h0WpeVrAVAYExU-00ZQvq5FE6sGYslF0gOR8_hrEeJT4nE_cr2yTdtidZTWFzcDPJXV_zzSyaIR2EHkHiBaN7PZyUAWHCCQletXufg0xGws2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما :
تا عید غدیر مجسمه‌ای ۱۵ متری از مشت علی خامنه‌ای در میدان انقلاب تهران نصب میشه‌.
@withyashar</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/withyashar/11822" target="_blank">📅 12:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11821">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">فاکس نیوز در گزارشی به نقل از عمر محمد، کارشناس مبارزه با تروریسم، نوشت سبک زندگی مجتبی خامنه‌ای به سطحی از ناپدید شدن رسیده که اسامه بن لادن سال‌ها در ایبت‌آباد تجربه می‌کرد؛ زندگی بدون ارتباط مخابراتی و با اتکا به پیک‌های مورد اعتماد.
@withyashar</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/withyashar/11821" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11820">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">۲۰ ملوان ایرانی به کشور بازگشتند
سفیر ایران در پاکستان از بازگشت ۲۰ ملوان ایرانی که به‌دلیل توقیف کشتی‌شان در آب‌های سنگاپور گرفتار شده بودند، به ایران خبر داد.
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل و ساعاتی پیش به میهن بازگشتند.
@withyashar</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/withyashar/11820" target="_blank">📅 12:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11819">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ایران در حال پاسخ به متن ارسال شده از سوی آمریکا است
ایران در حال گفت و گو‌ بر سر چارچوب کلان، برخی جزییات و اقدامات اعتمادساز به عنوان تضمین است.
متن ارسالی به میزانی شکاف‌ها را کم کرده است
اما کمتر شدن شکاف‌ها نیازمند پایان یافتن وسوسه جنگ در سمت واشنگتن است.
ورود ژنرال عاصم منیر به تهران، به منظور کم کردن این شکاف‌ها و رسیدن به لحظه اعلام رسمی پذیرش یادداشت تفاهم است.
/ ایسنا
@withyashar</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/withyashar/11819" target="_blank">📅 12:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11817">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش CNN: حکومت ایران در طول آتش‌بس بخشی از تولید پهپادهای خود را از سر گرفته است، که نشان می‌دهد در حال سریعاً بازسازی برخی توانایی‌های نظامی است که در حملات آسیب دیده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/withyashar/11817" target="_blank">📅 11:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11816">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امروز ۲۱ می روز جهانی چای است
و یادی میکنیم از  پدر چای ایران ، حاج محمد میرزا (کاشف السلطنه)
او معتقد بود مردم ایران نباید برای چای و قند و نفت سفید به کشورهای دیگر وابسته باشند. از این رو به عنوان سفیر ایران راهی هند شد و در پوشش تاجر فرانسوی بصورت مخفی در مزارع چای مشغول یاد گیری کشت چای شد. دلیل این کار این بود که فن چای کاری را سری و انحصاری میدانستند و حاضر نمی شدند کسی آن را یاد گرفته و در سطح وسیع عمل کند. وی قبل از مراجعت به ایران تخم چای و چهار هزار گلدان نهال چای به ایران فرستاد و با سختی و مشقت فراوان موفق به کشت و توسعه چای در ایران شد و از طرف مظفرالدین شاه کاشف السلطنه لقب گرفت.
برای آموزش چای کاری به کشاورزان چهار چای کار چینی توسط وی به ایران آورده شدند که منجر به اسلام آوردن آنها و تشکیل خانواده در ایران شد.
انگلستان که منافعش در انحصار چای در ایران به خطر افتاده بود طی توطئه ای وی را به قتل رساند در برخی نوشته‌ها هم عنوان شده که او در سال ۱۳۰۸ خورشیدی در یک سانحهٔ اتومبیل  مشکوک در مسیر بوشهر–شیراز درگذشت
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/11816" target="_blank">📅 11:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11815">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رسانه عبری والا: منابع اسرائیلی می‌گویند آمریکایی‌ها در مذاکرات با ایران یک قدم به جلو برداشته‌اند، بنابراین برآوردها این است که حمله‌ای به ایران در ۲۴ ساعت آینده تکرار نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/withyashar/11815" target="_blank">📅 11:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11814">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ادعای یدیعوت آحارانوت به نقل از یک مقام امنیتی اسرئیل:
ما ممکن است جنگ‌هایی را با سرعت بیشتری علیه ایران آغاز کنیم تا برنامه هسته‌ای و موشک‌هایش تهدیدی ایجاد نکند.
@withyashar</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/withyashar/11814" target="_blank">📅 11:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11813">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">سید محسن نقوی وزیر کشور پاکستان با سید عباس عراقچی وزیر امور خارجه دیدار و گفت‌وگو کرد.
@withyashar
پاکستانی ها از‌ عمانی ها هم پیگیر ترن ، پلنگ مارو ول کرد تو ما رو ول نکردی !!!</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/withyashar/11813" target="_blank">📅 10:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11811">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سازمان هواشناسی: امروز برای استانهای شمال غرب  ، مناطقی در غرب  ، دامنه های البرز  ، شمال و شمال شرق کشور  در برخی ساعات بارندگی ، رعد و برق و وزش باد شدید پیش بینی می شود.
@withyashar
هوا هنوز مساعد حمله چکشی نیست</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11811" target="_blank">📅 10:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11810">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خبرگزاری نور: سخنگوی وزارت خارجه ایران، بقائی، گزارش داد که پاسخ ایالات متحده به طرح ۱۴ نقطه‌ای خود را دریافت کرده‌اند و در حال بررسی آن هستند.
«بر اساس همان متن اولیه ۱۴ نقطه‌ای از ایران، تبادل پیام‌ها چندین بار انجام شده است و ما دیدگاه‌های طرف آمریکایی را دریافت کرده‌ایم و در حال حاضر در حال بررسی آن‌ها هستیم.»
@withyashar</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11810" target="_blank">📅 10:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11809">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V27f9-SrbVh28ODnjOm715VCV_hUxwQC6AXG9fZh-kn5FboyFsbSlBK4Of2ANQarbWM0DtP1o0tGV9_xB2x6jjMki6EkwFdVVsDt44bN2G5tcE8GMws-XpSOQmHOlSgRnATO8HmRuYA2DPivqR60wv2DHoBe9PryGG5Xu7F8LnHN7Tk9_16o125yoIsMlXhLECYj0EIqIwF4dAcD18oeR85IQdraB8GkoHuG_Qusa8Z67dpEKk_c9P8IoGA8IpYVWtfF4JxRwgubYHX2xj6deaB9jCdZ7qB2lub-PbNUw6ot7S7vZ98IEjqxTSnOcaApS_Nzwu9a9fDqxcFvrMRrcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام با انتشار این عکس تایید کرد : یک بمب‌افکن B-1B لنسر متعلق به نیروی هوایی آمریکا، در جریان یک پرواز آموزشی بر فراز آب‌های منطقه‌ای خاورمیانه، از یک هواپیمای سوخت‌رسان KC-135 استراتوتنکر سوخت‌گیری کرد.
@withyashar
در این ویدیو اتاق جنگ چند روز پیشاین هواپیما رو رهگیری کردیم …
https://www.instagram.com/reel/DYQCr39RJ4i/?igsh=MThycjJiYWZmbnJ3dA==</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/11809" target="_blank">📅 10:02 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11808">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رایزنی‌های مصر، عربستان و قطر درباره آخرین تحولات مذاکرات تهران-واشنگتن
وزیر خارجه مصر با همتایان سعودی و قطری خود درباره آخرین تحولات مربوط به مذاکرت تهران-واشنگتن گفت‌وگو و تاکید کرد که استمرار این مذاکرات اهمیت داشته و در هر توافقی در آینده حاصل می‌شود، باید دغدغه‌های امنیتی کشورهای منطقه در نظر گرفته شوند.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/11808" target="_blank">📅 09:54 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11807">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfxXkDHy04FtaLngE7dAsb2_6QG8oe8WWH8uDE8kHBI4EH7iIOrY68mwwg6rN6FtpRzCPcWCE-FMVqa0Ej5erRykkSMW5Ilqh6i95zV7O8ScvG2434qBI7sIkX4GzxERnWLGUUrec8kTpadxPVRIzxmSCQwTFtKjGL9_GZlnLYaSqeBLnSZ2v47wyU88TJPLD8qv5PLAona8d3zad7c7tGFVdk57_ZCsnDxiX_1peN6zWpWTcGU-yZd830ygsNG3m1uVWoHr1Ylj3u0IwZu1tRNQmmTLCbd2CvBZ2ZaVkKw3irnvUlO32WVENHpr5Odk9V0nqDS-3shXf0Aif3JQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب رسمی کاخ سفید تصویری از ترامپ منتشر کرد که زیر آن، خامنه‌ای و یکی از رهبران داعش با برچسب «کشته‌شده»، مادورو با برچسب «بازداشت‌شده» و کاسترو با برچسب «تحت پیگرد» دیده می‌شن.
کاخ سفید در این پست نوشت: «عدالت اجرا خواهد شد.»
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11807" target="_blank">📅 09:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11806">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">https://t.me/boost/withyashar
۴۷۵ بوست تا آزادی استیکر حامله
😅
😂</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11806" target="_blank">📅 02:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11802">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F5NSeQJAJn-nmV6EL0tIzmbWITXGbRYQFcGFSJ43-Bll5kfhiuLrrxfHWKy1PRQLHxz1oQ5ZNP7aW4mDGqO5tl_mZjWgd6HL929gJiXXXlMpBu3rI4qVaxEGTJWYJTPfxZVRA1EQCYpKvWRYx3vIxiiTUQ2gACZRtc4rqd-2cM0Ri0hX8fvjx1aBG1Jv6IQcwNwVzqBiyOwbfEyoHvoYs3bLkU6dRyAzlI8pTSn96l3RL7drINJ2EacdmpAobCNJ288JeKBjgV0fMVf3t49z7FD3ROYAY-_BSgMWtDY8GB3xncSKc-A7IlLG7FjXcJnr38RUf7tvUi2MlR9noAvhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqXfUPDdbV1DlG4edz1mrjna2_s7K5NWVA5WrmAWXyTbzDP-LEy9dRm_pjMkFcl3bQQVbWL8k303LRbOnzXBz8YuEuWYeDsag7xMzt-81UZqVnR6rdXDmd0cjkEBLjX6Pr1j0HpP4zz06Q3mJBouoInmVoiCbLBHecnUE6X1zvQrfvxIXFsmQ5JIs0NeGYvBY5vMbrvAqdvHN70zl8W5EGd8xd8FHNJQLk5MDZdWT0f6jy-VGEd1lZLEoRWYBd45r4gpI3xcwc_MQkei70A_mFUU51WYwPXYBgWl7wNBSX_ZjhLPNv9pvG4cG3jhmuekdSOWTh_8LS3thij90ki66w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزیر کشور پاکستان با احمد وحیدی، فرمانده سپاه پاسداران در تهران دیدار کرد.
@withyashar
یکی اینو آخرش از سولاخ کشید بیرون دیگه مابقی با موساده
😅</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/withyashar/11802" target="_blank">📅 01:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11801">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ادعای «میدل ایست آی»: دونالد ترامپ، حمله برنامه‌ریزی‌شده به ایران را در این هفته به تعویق انداخت، چراکه متحدان عرب و مقامات دولت خودش به او هشدار دادند در ایام حج، جنگ را از سر نگیرد.  به گفته دو مقام ارشد کشورهای حوزه خلیج‌فارس، به ترامپ گفته شده بود که حمله…</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/withyashar/11801" target="_blank">📅 00:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11800">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ادعای «میدل ایست آی»: دونالد ترامپ، حمله برنامه‌ریزی‌شده به ایران را در این هفته به تعویق انداخت، چراکه متحدان عرب و مقامات دولت خودش به او هشدار دادند در ایام حج، جنگ را از سر نگیرد.
به گفته دو مقام ارشد کشورهای حوزه خلیج‌فارس، به ترامپ گفته شده بود که حمله به ایران در ایام حج، بحرانی را در میان کشورهای عربی حاشیه خلیج فارس ایجاد می‌کند، زیرا این حمله باعث می‌شود صدها هزار زائر حج سرگردان بمانند.
منابع همچنین گفتند که به ترامپ گفته شده بود حمله در این ایام مقدس که منتهی به عید قربان می‌شود، بیشتر از این به جایگاه آمریکا در جهان اسلام لطمه می‌زند.
یک مقام ارشد آمریکایی که از بحث‌های جریان‌یافته در دولت ترامپ آگاه است، تأیید کرد که این گفت‌وگوها انجام شده است
@withyashar</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/withyashar/11800" target="_blank">📅 00:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11799">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">معاون نیروی دریایی ۳پا :
همه نیروهای مسلح دست به ماشه و آماده هرگونه پاسخ به هر تعرض دشمن هستند
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/11799" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11798">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">صدا و سیما : مردم یه سر به فضای مجازی بزنن تا ببینن چطور مردم کل دنیا منتظرن جمهوری اسلامی مقابل آمریکا و اسرائیل بایسته و یه تو دهنی محکم بهشون بزنه؛ پاسخی که دل خیلی‌ها رو خنک کنه.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/11798" target="_blank">📅 23:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11797">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آکسیوس: تماس سه‌شنبه ترامپ و نتانیاهو درباره طرح جدید صلح ایران که با میانجی‌گری قطر و پاکستان ارائه شده، «تنش‌آلود» بوده.
ترامپ هنوز معتقده امکان رسیدن به توافق با ایران وجود داره، ولی نتانیاهو به شدت میخواد که اقدام نظامی علیه ایران انجام بشه. نتانیاهو بعد از این تماس «به‌شدت نگران و آشفته» شده بود!
@withyashar</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/11797" target="_blank">📅 23:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11796">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آکسیوس : یک منبع آمریکایی که در جریان این تماس تلفنی قرار داشت به من گفت: «موهای بی‌بی بعد از تماس آتش گرفته بود.»
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/11796" target="_blank">📅 23:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11795">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edZgbVIu1eKyhbML0zstS9uS-zA0jCgID8UOUTJm0tpNyaypm1uJEm3DTLTK01Hy_l9codDV6O9JuLKpa-Hlzd0e9IJxvjIxV9sLg0NTOP451exgg020jo4VHbKx5foxeCCxypDRuFcbFOHvMbYBUb-0s7NojZuyC_KC0qPPGF0VGBEY_zxqdtH2MT4ibzZBCLGBXW5yrT-zuqh1tmdEGQ15Mp-P5LXGlcIGLA4wUzeTHyM3eX6f0kleUb7Dmg2eJDWONjZ2FvNTQE3gVTsKJaOu6UsWbYDLzBvlW0wc9_SzJl-1hLFkRE4E8-nSjppmtjUOaYLmwFPdLmNbJvfjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیا با نفس حبس‌شده در انتظار موج بعدی اسناد یوفوهاست؛ پس از آنکه مقام‌ها وعده دادند این اسناد «به‌زودی» منتشر خواهند شد.
شان پارنل، سخنگوی ارشد پنتاگون، در ایکس اعلام کرد که این مدارک هم‌اکنون «به‌طور فعال در حال آماده‌سازی و پردازش» برای انتشار هستند.
مقام‌های سابق سیا و پنتاگون اخیراً مدعی شده‌اند «چهار گونهٔ بیگانه» به زمین رفت‌وآمد دارند: خزنده‌ها (Reptilians)، حشره‌مانندها (Insectoids)، گری‌ها (Greys) و نوردیک‌ها (Nordics).
آیا ما برای حقیقت آماده‌ایم؟
@withyashar</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/withyashar/11795" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11794">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش کانال ۱۴ اسرائیل : آیا ارزیابی ایران از شرایط کاملاً اشتباه است؟
با وجود تبلیغات تهاجمی، تهران در خفا عمق بحران خود را درک می‌کند. حکومت روی لبهٔ تیغ حرکت می‌کند؛ از یک سو ترامپ را تحریک می‌کند و از سوی دیگر، به‌طور پنهانی افکار عمومی ایران را برای یک تشدید بزرگ نظامی آماده می‌کند.
افراد در داخل حکومت اذعان دارند که حملهٔ آمریکا بسیار محتمل است، اما روی این موضوع شرط بسته‌اند که ترامپ یک حملهٔ محدود انجام دهد، اعلام پیروزی کند و سپس متوقف شود.
«همهٔ ما فقط امیدواریم که این هم یکی دیگر از ارزیابی‌های اشتباه ایران از شرایط باشد.»
@withyashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11794" target="_blank">📅 23:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11793">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یک مقام اسرائیلی به روزنامه اسرائیل هیوم : حکومت ایران هنوز درک نکرده چه بر سر این کشور آمده و افزود همان‌گونه که این حکومت لبنان، عراق و یمن را به عقب‌ماندگی کشاند، اکنون خود ایران نیز به کشوری عقب‌مانده تبدیل شده است.
به گزارش اسرائیل هیوم، در اورشلیم سقوط حکومت ایران همچنان سناریویی محتمل تلقی می‌شود و مقام‌های اسرائیلی می‌گویند پس از پایان مرحله کنونی، احتمال ازسرگیری اعتراض‌ها وجود دارد.
این روزنامه همچنین نوشت آسیب‌های واردشده به ایران بسیار قابل توجه بوده و برآوردها حاکی است در دو دور درگیری حدود ۳۰۰ میلیارد دلار خسارت اقتصادی به ایران وارد شده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/withyashar/11793" target="_blank">📅 23:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11792">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو با نظر ترامپ در مورد مذاکره مخالفت کرد
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11792" target="_blank">📅 23:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11791">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">کانال ۱۲ اسرائیل
: نیروهای آمریکایی بر روی یک نفتکش ایرانی در خلیج عمان سوار شدند.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11791" target="_blank">📅 23:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11790">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6ae960da.mp4?token=Q-hK2hmzkBcWzlXbflrB7ZGNreIwj-9SmeC-8vxuvaYPtCl-jM5rwsqi5l70WSdI6unPqMR53byJpNUfeYVnfvQTUi_pLubyqx4kpQoLi2tGkGCIeXbZAhOTZ6jiQUZgXa9HZLqNr9F0PklhpBOWmtLIKsOiDaMk03Reu-_b0YplUV2LHJ0MU3NZ2rIbXCA1TAIWEwMjMesUhpu6dbF2orwxWZ87G4lXkz401RStrZWf8mRKv-MFQ8uK8-Sf0VHnYTkq5Kp7mieNJfuvEt4NXZgPKCxYUqFI8qLMUEL6MlP_RhoBj-5kPMI-wQqgZ2m6WUJcvp9iGqhScvBY6TcSlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6ae960da.mp4?token=Q-hK2hmzkBcWzlXbflrB7ZGNreIwj-9SmeC-8vxuvaYPtCl-jM5rwsqi5l70WSdI6unPqMR53byJpNUfeYVnfvQTUi_pLubyqx4kpQoLi2tGkGCIeXbZAhOTZ6jiQUZgXa9HZLqNr9F0PklhpBOWmtLIKsOiDaMk03Reu-_b0YplUV2LHJ0MU3NZ2rIbXCA1TAIWEwMjMesUhpu6dbF2orwxWZ87G4lXkz401RStrZWf8mRKv-MFQ8uK8-Sf0VHnYTkq5Kp7mieNJfuvEt4NXZgPKCxYUqFI8qLMUEL6MlP_RhoBj-5kPMI-wQqgZ2m6WUJcvp9iGqhScvBY6TcSlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : قصد داری به اونا ( ایران) حمله کنی‌؟
ترامپ : اینو بهت نمیگم
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/11790" target="_blank">📅 22:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11789">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خبرنگار : از این رفت و برگشت با ایران خسته نمیشی؟
ترامپ : من هیچوقت خسته نمیشم ولی اگه با چند روز صبر کردن بشه جلوی جنگ و کشته شدن مردم رو گرفت کار خوبیه
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/11789" target="_blank">📅 22:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11788">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: چند روز منتظر پاسخ ایران می‌مانیم
ایران یک کشور شکست‌خورده است و ما امیدواریم بتوانیم با آنها توافق کنیم که این برای همه عالی خواهد بود.
من هیچ تحریمی را علیه ایران تا زمانی که به توافق برسیم رفع نخواهم کرد. تا زمانی که ایران توافق را امضا نکند به ایران هیچ معافیت نفتی نخواهم داد و پیشنهادی هم برای انجام این کار نداده‌ایم.
اگر پاسخ‌های درست را نگیریم، اوضاع خیلی سریع پیش می‌رود. همه ما آماده‌ایم. باید پاسخ‌های درست را به دست آوریم.
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11788" target="_blank">📅 22:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11787">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25eebf00dd.mp4?token=PlHlZtL4C5gMPDAT2tBmmZXBLFRmNzCTreiV8hkqVlIKdO_BRdeeV9_z88BHM5zDfg7ADUMZwQHN7A1Jul3B7dPmHOy2bBh2mR3tKieC_8bCO9rQ5U8zWZMirRMs2EiSs2iqoxi3IOWNm2b0Qxs5ojCr2UWoFpwugcat_MYXVxKtZl2rbJe_czlUKU6j7WGojzT0O4DOCZeIi5To7v6s5209Ss6sLK7rFW6RCEI5Xv5wipZcAXn2RGRc98PXm9OvTFAd33sttsYdrwDbfgJnQ-8c4Vawzyv0vJAebHjKK2bZi_iZBD5DGg2ZufRbY4gcFKOUQrR-UzjTMIFUwEDXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25eebf00dd.mp4?token=PlHlZtL4C5gMPDAT2tBmmZXBLFRmNzCTreiV8hkqVlIKdO_BRdeeV9_z88BHM5zDfg7ADUMZwQHN7A1Jul3B7dPmHOy2bBh2mR3tKieC_8bCO9rQ5U8zWZMirRMs2EiSs2iqoxi3IOWNm2b0Qxs5ojCr2UWoFpwugcat_MYXVxKtZl2rbJe_czlUKU6j7WGojzT0O4DOCZeIi5To7v6s5209Ss6sLK7rFW6RCEI5Xv5wipZcAXn2RGRc98PXm9OvTFAd33sttsYdrwDbfgJnQ-8c4Vawzyv0vJAebHjKK2bZi_iZBD5DGg2ZufRbY4gcFKOUQrR-UzjTMIFUwEDXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا همانطور که رسانه های دولتی ایران گزارش داده اند، ایالات متحده در جریان مذاکرات صلح پیشنهاد کاهش تحریم های نفتی ایران را داده است؟
ترامپ: نه، من این را نشنیده ام. تا زمانی که توافقی امضا نکنند، هیچ کمکی نمی‌کنم.
وقتی آنها توافق نامه ای امضا می کنند، ما می توانیم دوباره آن مکان را بسازیم و کشوری داشته باشیم که واقعا کشور خوبی برای مردم باشد.
اما نه، ما چیزی پیشنهاد نکرده ایم.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11787" target="_blank">📅 22:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11786">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مسعود  زرشکیان : وادار کردن ایران به تسلیم از طریق اجبار چیزی جز توهم نیست.
احترام متقابل در دیپلماسی بسیار عاقلانه‌تر، ایمن‌تر و پایدارتر از جنگ است
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11786" target="_blank">📅 22:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11783">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/withyashar/11783" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11782">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/withyashar/11782" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11781">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کلش ریپورت:  اردوغان در تماس تلفنی با ترامپ درباره روابط ترکیه و آمریکا و مسائل منطقه‌ای صحبت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11781" target="_blank">📅 22:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11780">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">به ادعای آکسیوس : امروز اوایل روز، بحث داغی در داخل کاخ سفید درباره ایران شکل گرفت، جایی که جی‌دی ونس، استیو ویتکاف و جرد کوشنر برای توافق اولیه‌ای جهت پایان دادن به جنگ تلاش می‌کردند، در حالی که پیت هگست و مارکو روبیو برای فشار بیشتر و احتمال اقدام نظامی استدلال می‌کردند
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11780" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11779">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">لطفا دایرکت بی مورد و چند پیغامه ندید
🙌🏾</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11779" target="_blank">📅 22:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11778">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با یاشار : اول مهر مدارس مختلط است
😎
@withyashar</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/withyashar/11778" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11777">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده: پس از ارسال متن ۱۴ بندی ایران که سه روز پیش صورت گرفته است،
آمریکایی‌ها بار دیگر متنی را از طریق میانجی پاکستانی به ایران داده‌اند.
ایران در حال بررسی متن است و هنوز پاسخی داده نشده است.
میانجی پاکستانی در تهران به دنبال نزدیک کردن متون به یکدیگر است.
هنوز چیزی در این میان نهایی نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/11777" target="_blank">📅 21:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11776">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11776" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11775">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ادعای آکسیوس به نقل از یک منبع آمریکایی: ترامپ به نتانیاهو از یک دوره 30 روزه مذاکره درباره برنامه هسته‌ای ایران و تنگه هرمز اطلاع داد
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11775" target="_blank">📅 21:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11774">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خبرنگار العربیه: بعد از تماس اسرائیل در دو حمله هوایی شهرک‌های «حداثا» و «تول» در جنوب لبنان را بمباران کرد.
@withyashar</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/withyashar/11774" target="_blank">📅 21:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11773">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">«آکسیوس»: نتانیاهو از مکالمه تلفنی خود با ترامپ درباره ایران «بسیار عصبانی» شده بود. قطر و پاکستان تعدیلاتی بر طرح پیشنهادی برای پایان جنگ اعمال کردند.
@withyashar</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/withyashar/11773" target="_blank">📅 21:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11772">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وب‌سایت «آکسیوس»: گفت‌وگوی اخیر ترامپ و نتانیاهو بسیار متشنج و دشوار بود.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11772" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11771">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">رویترز:برخی کشتی‌ها بیش از 150 هزار دلار به ایران پرداخت می‌کنند تا عبور از تنگه هرمز را تضمین کنند.
‏هزینه عبور کشتی‌ها از تنگه هرمز برای همه کشورها اعمال نمی‌شود.
‏مکانیزم جدید ایران در تنگه هرمز به کشتی‌های مرتبط با روسیه و چین است
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11771" target="_blank">📅 21:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11770">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hlu60aI-Kgr6ax0xSxsEBbEDVZY4cllIOFOazHs49wt03eUw7pl5UTYnTk_EdT9S47oLK5KbkeHBwJ1gGWgi2waXC4hHBIqo8mqWrTlwM2fzspJLQzzKfkFBj35VxAtoAbLU0OaaAZCLhcWK8B2VDpE38RjlWF-ngFKYlaLTGRXVY6q7VQmu6-P1i-yNeSZnRT6_GkcLCGrH_G-X7-V4BKF9b66E5bgBPLYvzbFnkKIn8Rx2_26EJ8IgQUCNUzsdfOey6zMLCu3fmpJPHSqgqiU5fWZtteepkkeQCcnBrqK622EJOV-PbSRaLy1QFciPApF90e0H1kiaRARMPzMazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11770" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11769">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه مقام ارشد اسرائیلی : اطرافیان ترامپ دارن روش فشار میارن که به توافق برسه  نتانیاهو هم باهاش درباره این موضوع صحبت کرده، و از نظر ترامپ گزینه حمله وجود داره که فقط بحث زمانشه
@withyashar</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/11769" target="_blank">📅 20:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11768">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دونالد ترامپ:
هیچ‌وقت تسلیم نشو. هر اتفاقی که بیفتد، مهم نیست در چه جایگاهی از زندگی هستی یا در چه شرایطی قرار داری، به جلو حرکت کن و ادامه بده.
همیشه رو به جلو حرکت کن. هیچ‌وقت از پیش رفتن دست نکش.
@withyashar</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/withyashar/11768" target="_blank">📅 20:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11767">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دونالد ترامپ دربارهٔ ایران:
ما ضربهٔ بسیار سختی به آن‌ها وارد کردیم. ممکن است مجبور شویم حتی سخت‌تر هم به آن‌ها ضربه بزنیم اما شاید هم نه.
ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست پیدا کند و کل خاورمیانه را منفجر کند و بعد هم به اینجا بیاید و شما را هدف قرار دهد.
@withyashar</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/11767" target="_blank">📅 20:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11766">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اتاق جنگ با یاشار : امشب میخوام یه تحلیل سنگین کنم با طعم پیشبینی ، خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11766" target="_blank">📅 19:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11765">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73c5fdf4b.mp4?token=KcdelrDMKDE6NDm7r6B3CY5exAgza2C1JBabrwV56uNprDcO50AKP1trGB18ig1LWRMsGr7rQ-c870KHK65aOi9PoznTyUnbX01dUfN1tNWDnS6AjcLmS2ac30n8qn7UTP7bepLB-NBSNoNXh5yYQKjlGa5nPhhy43PVOS5H33zFQuVOrI75BHlZ9ixUEfwScKcUnoe5fAMCWGWhb3hUMImu0qMU2OmvrkhGnHul1KQOU7K6EdlfYKv1u1eFqS80kBNT5z3FV8iEhwKWKr-o0jUafELf88w4yDIRjvz_5Xb0hdhjHgZ0wUAgjuomH22NGlz1rOpCduunvV_JmArEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73c5fdf4b.mp4?token=KcdelrDMKDE6NDm7r6B3CY5exAgza2C1JBabrwV56uNprDcO50AKP1trGB18ig1LWRMsGr7rQ-c870KHK65aOi9PoznTyUnbX01dUfN1tNWDnS6AjcLmS2ac30n8qn7UTP7bepLB-NBSNoNXh5yYQKjlGa5nPhhy43PVOS5H33zFQuVOrI75BHlZ9ixUEfwScKcUnoe5fAMCWGWhb3hUMImu0qMU2OmvrkhGnHul1KQOU7K6EdlfYKv1u1eFqS80kBNT5z3FV8iEhwKWKr-o0jUafELf88w4yDIRjvz_5Xb0hdhjHgZ0wUAgjuomH22NGlz1rOpCduunvV_JmArEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای هزارمین باز: همه چیز از بین رفته تو ایران
تنها سوال من اینه که آیا ما میریم و کار رو تمام می‌کنیم؟ ، یا اونا قراره سندیو امضا کنن؟ خواهیم دید چه خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11765" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11764">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11764" target="_blank">📅 19:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11763">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ddb6e4b5.mp4?token=f0XU5hpZHVHd1e-ovO9YWSYFZP0A7o8fKpG6Ylq9ZJTCBmEsFfAHSecML_xQLfGmYwWij8i6mPPO8MHF7slc6CM4-7NR1sQFAdQGi6tgUKHziI0RsPl5CRtVwglJTzfbAF-PbyCb3goy458dpFkiXWxRth2l9JeMJhDz6foXQ4Bpv9-kftgH7QEAGbgPBteZmGy3tfuQ61kkV-9jXxkvl6YLoa0fPo-5vOA_4miDetbIRmfMHJBLESIjPQPReXrMuH05Ki8o4pTI50AAR7RJ26M_3XM4NdFI3ffyPjKNVAdxPL-upXImbUcvsd1mzcJMNmK3HGvVLiqBlMbFIh9deA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ddb6e4b5.mp4?token=f0XU5hpZHVHd1e-ovO9YWSYFZP0A7o8fKpG6Ylq9ZJTCBmEsFfAHSecML_xQLfGmYwWij8i6mPPO8MHF7slc6CM4-7NR1sQFAdQGi6tgUKHziI0RsPl5CRtVwglJTzfbAF-PbyCb3goy458dpFkiXWxRth2l9JeMJhDz6foXQ4Bpv9-kftgH7QEAGbgPBteZmGy3tfuQ61kkV-9jXxkvl6YLoa0fPo-5vOA_4miDetbIRmfMHJBLESIjPQPReXrMuH05Ki8o4pTI50AAR7RJ26M_3XM4NdFI3ffyPjKNVAdxPL-upXImbUcvsd1mzcJMNmK3HGvVLiqBlMbFIh9deA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11763" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11762">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b1ee80c2.mp4?token=i5MwJlD2s4tdo_q1h_tvUcim8m01g45AsoWDQNnQuwI-9kQyjeOOz8gJtAowOq8AzpRYRwdVdghuTkQY2XB-q0nvm_GuVwSWiyFC-YcD7FI1GUsclSKm56we9AMMmj5uifTcfsypTjJ_G81u96s8_Nx1h21v_w_ExqycoMNgCXp66Ndq1tRsXm3cGzKKhTxtrLJS6hOsTj9Ytlo-dZwi4JaTLl8q_-xo_d4yj6vkfSV47qt-oD0BVS_Yd35ux1SyvPpcmwmAX2TF97xs5aEnnXi1qX1lrfCp2ein8x6X60nqbNVXL3Hso6bgxyJUbL4AYCjHOqWpD0vN1D_zmFQRUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b1ee80c2.mp4?token=i5MwJlD2s4tdo_q1h_tvUcim8m01g45AsoWDQNnQuwI-9kQyjeOOz8gJtAowOq8AzpRYRwdVdghuTkQY2XB-q0nvm_GuVwSWiyFC-YcD7FI1GUsclSKm56we9AMMmj5uifTcfsypTjJ_G81u96s8_Nx1h21v_w_ExqycoMNgCXp66Ndq1tRsXm3cGzKKhTxtrLJS6hOsTj9Ytlo-dZwi4JaTLl8q_-xo_d4yj6vkfSV47qt-oD0BVS_Yd35ux1SyvPpcmwmAX2TF97xs5aEnnXi1qX1lrfCp2ein8x6X60nqbNVXL3Hso6bgxyJUbL4AYCjHOqWpD0vN1D_zmFQRUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین پکن رو ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11762" target="_blank">📅 18:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11761">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طبق ادعای تایید نشده رسانه الحدث: احتمالاً توافق تهران و واشنگتن برای شکل دادن دور دیگه‌ای از مذاکرات، طی ساعات آینده نهایی می‌شه. این مذاکرات احتمالاً پس از پایان حج تو اسلام‌آباد برگزار می‌شه.
@withyashar</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/11761" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11760">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دونالد ترامپ دربارهٔ خودش:
شما در نهایت خواهید گفت: او بزرگ‌ترین رئیس‌جمهوری بود که تاکنون زندگی کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/11760" target="_blank">📅 17:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11759">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ درباره ایران: الان خشم زیادی در ایران وجود دارد، چون مردم در شرایط بسیار بدی زندگی می‌کنند.
التهاب و ناآرامی زیادی به‌وجود آمده که تا این حد قبلاً ندیده بودیم.
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/11759" target="_blank">📅 17:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11758">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرنگار: درباره جنگ ایران چی میگید؟
ترامپ: بذار اینجوری بگم، شما تو ویتنام 19 سال توی جنگ بودید، جنگ جهانی دوم 4 سال بودید؛ من 3 ماهه تو ایران درگیرم، خیلیاش هم آتش‌بس بوده. تو دوتا جنگ، ونزوئلا و اینجا، ما 13 نفر از دست دادیم، تو جنگ‌های دیگه صدها هزار نفر کشته دادید. ما عملاً ونزوئلا رو گرفتیم تقریباً هم ایران رو هم گرفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/11758" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11757">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دونالد ترامپ دربارهٔ ایران:
من هیچ عجله‌ای ندارم. همه می‌گویند: «انتخابات میان‌دوره‌ای.» من هیچ عجله‌ای ندارم.
@withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/11757" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11756">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرنگار: «آیا شما و بنیامین نتانیاهو دربارهٔ ایران هم‌نظر هستید؟»
دونالد ترامپ: «بله.»
«بی بی نتانیاهو پسر خیلی خوبی است»
@withyashar
😃
🤣</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11756" target="_blank">📅 17:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11755">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d428ef0134.mp4?token=ZJWdjPm5Zmty-igMMJPkPfRV23NZ3akmel_skkfk8o0TMw5xWAuuPeiUdAxC3kVxgR-jkQRX2kAxZv2iVVmrhx_zKpNGxfMHD6Jva6Qqkg_b_tgnSl6xMLDFg-_QAeMIsU6fk0bWmo12FGHA4VEZVGjn4rK0uN3rRB4V5eFthai5opPywwpl3cvuuib3F4qd9DkmhcXAHsroJV7BcP6p7_27ebrN-Wgema4HBMan_todnub90lVlU0jxpgjucAsIN6lQgm-KHZUICTZi38Pqd5qTN_t3P4C3-fThW1OwSc2bASJz-hfCVTtXijWzdW-dpGiHahbIY0QRtWsByOYODA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d428ef0134.mp4?token=ZJWdjPm5Zmty-igMMJPkPfRV23NZ3akmel_skkfk8o0TMw5xWAuuPeiUdAxC3kVxgR-jkQRX2kAxZv2iVVmrhx_zKpNGxfMHD6Jva6Qqkg_b_tgnSl6xMLDFg-_QAeMIsU6fk0bWmo12FGHA4VEZVGjn4rK0uN3rRB4V5eFthai5opPywwpl3cvuuib3F4qd9DkmhcXAHsroJV7BcP6p7_27ebrN-Wgema4HBMan_todnub90lVlU0jxpgjucAsIN6lQgm-KHZUICTZi38Pqd5qTN_t3P4C3-fThW1OwSc2bASJz-hfCVTtXijWzdW-dpGiHahbIY0QRtWsByOYODA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :  الان میزان محبوبیت من در اسرائیل ۹۹ درصد است. من می‌توانم برای نخست‌وزیری نامزد شوم؛ شاید بعد از اینکه این کار را انجام دادم، به اسرائیل بروم و برای نخست‌وزیری نامزد شوم.
@withyashar</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/withyashar/11755" target="_blank">📅 17:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11753">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607ea22bcb.mp4?token=ps1xMSAqYl-hpVDnfAb0uTgN3JLhlierIcGrvow6ukuW1YnM3friKYs7ScoOniVpLuDgnziM-Y-ALYEfFNjjqD7ecOrNf9-XpivNLVbCfSRDZSX-it0vZahKSYaYQM0T5YF-bUCT19Xe4sHOrAjP05nazTvSoZIAh9lmU8HfaRmWm4J0jiUANbd2lEIjHqn2vTPmd94IodAnIhBikUdPHvfEeWhSMGUwVB3zn7UWjRMV3wRN2KFQCP3sDyxKafEQ92pg-Ugsjvuzw1pgs-lbq_FFMQbFLq1_IuFVlyPCOmrNLNnB_bkD3DVpAgy7vPaS-RLxJKOLvw8JAdjGtN3TLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607ea22bcb.mp4?token=ps1xMSAqYl-hpVDnfAb0uTgN3JLhlierIcGrvow6ukuW1YnM3friKYs7ScoOniVpLuDgnziM-Y-ALYEfFNjjqD7ecOrNf9-XpivNLVbCfSRDZSX-it0vZahKSYaYQM0T5YF-bUCT19Xe4sHOrAjP05nazTvSoZIAh9lmU8HfaRmWm4J0jiUANbd2lEIjHqn2vTPmd94IodAnIhBikUdPHvfEeWhSMGUwVB3zn7UWjRMV3wRN2KFQCP3sDyxKafEQ92pg-Ugsjvuzw1pgs-lbq_FFMQbFLq1_IuFVlyPCOmrNLNnB_bkD3DVpAgy7vPaS-RLxJKOLvw8JAdjGtN3TLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم تکرار میکنم نفرستید این ویدیو ها فیک هستند !!!
@withyashar
جدا از جعلی بودن روسیه الان برف ‌نیسن !
علی گدام مارکت بورو نیست یه عمری خودش خودشو نشسته ! حمام هم کس دیگه لیف زده !
😂</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/11753" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11752">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/11752" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11751">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5c69f230.mp4?token=TAHuGayv852y9gyoY7t4WUJgjv7fX7iGDCEWEAvCOGDK6wND3vQFlUVk0MNGqvUezrw-EZcYujpePBnt3S-x1LhEob3DAbfujTFSq8s5oFw4lwbKFYybf6F8kNEiPH1A_QD3U7ojbBqNwOhL8no7MMgK0_AJ0HdVvsoh47UN0vZZRSVxfItppNhUYricrV42dvZJ9kTCBpTqiM4svL5czG5Tupn147eiSQd6ulJ3pArcTDgEJgrsbLZVIKquOdP0jyGx4aq1Mmv8gQgfZWXeLlRhiHAMkpjY0JBV7biwmCCP4xMqLz2QrjZkyDuOLTJTxuxnTVKjSsqTuymQu7iIRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5c69f230.mp4?token=TAHuGayv852y9gyoY7t4WUJgjv7fX7iGDCEWEAvCOGDK6wND3vQFlUVk0MNGqvUezrw-EZcYujpePBnt3S-x1LhEob3DAbfujTFSq8s5oFw4lwbKFYybf6F8kNEiPH1A_QD3U7ojbBqNwOhL8no7MMgK0_AJ0HdVvsoh47UN0vZZRSVxfItppNhUYricrV42dvZJ9kTCBpTqiM4svL5czG5Tupn147eiSQd6ulJ3pArcTDgEJgrsbLZVIKquOdP0jyGx4aq1Mmv8gQgfZWXeLlRhiHAMkpjY0JBV7biwmCCP4xMqLz2QrjZkyDuOLTJTxuxnTVKjSsqTuymQu7iIRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها فیلم موجود از جعفر شفیع زاده
«در پشت پرده های انقلاب» عنوان کتاب خاطرات جعفر شفيع زاد، بچه قصاب قهدری‌جانی است که نخستین بار در سال ۲۰۰۰ در آلمان منتشر شد.
او یکی از اعضای بادی گارد خمينی بود که در سال ۵۶ در سوريه بدستور قطب زاده؛ ابراهيم يزدی؛ بنی صدر و.... دوره آموزش نظامی مخصوص و چريکی گذرانده و از زندان اصفهان و روستای قهدريجان به فرانسه و دمشق و ليبی (طرابلس) فرستاده میشود.
برای  اندکی ممکن است که سبک نگارش خاطرات شفیع زاده در کتاب «در پشت پرده های انقلاب» به صورت مستند نباشد و یا اینکه اسم افراد و یا مکانها بنا بر ملاحظاتی با آنچه که واقعا اتفاق افتاده باشد دقیقا همخوانی نداشته باشد. اما تجربیات، مدارک موجود و اطلاعاتی که بعد از انتشار این کتاب به دست آمد نشان داد که همه مطالب بیان شده در این کتاب بخصوص دخالت کشورها  در به پایان رساندن انقلاب ۵۷ و دستنشاندگی محافل اسلامی و رایطه شخص خمینی، کاملا واقعی است.
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11751" target="_blank">📅 16:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11750">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/leNypXbW2x7X4vkJY8ovK9i_bP7NGuLJer8nCdVNzEci_5ucyY1L0kVBs1uuEsmiGbBc2P_IJntzkP_WxXUPQkQoYAUViH6j4KG8yadRsIClPbOyvIVNW95Gq3pUV_IqfXwD_C6w0XenTQxkijM0HfIIt_svsyAt6Y0UrVun1_YczGW_7roAWOholgjdTSeE3TkfRuggfpdKPMcPtPYQtboc3c8I8_S5k0l20ZuHMlQwXIcuVbSNTyQMizLK_hZ5vs-pYWXD5gy_I660tSTib0kYp_Xj0IZBcQ7ZIoN6J47RjF7WJnHyHD6ZiDuiFEWjOkDahYPcuoown_szzkz9PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">poshte-pardehaye-enghelab (@withyashar).pdf</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11750" target="_blank">📅 16:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11749">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">العربیه: آمریکا به پاکستان اطلاع داده که در موضوع هسته‌ای و تنگه هرمز هیچ امتیازی نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/withyashar/11749" target="_blank">📅 15:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11748">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شبکه الحدث: جمهوری اسلامی و پاکستان در خصوص مذاکرات دچار اختلاف‌نظر شده‌اند
الحدث گزارش داد در دو هفته گذشته، همکاری میان حکومت ایران و پاکستان با چالش‌هایی روبه‌رو شده و فضای بی‌اعتمادی بر سطح هماهنگی‌های دو طرف سایه انداخته است.
این رسانه افزود میان تهران و اسلام‌آباد درباره کانال‌های مذاکره و محل برگزاری گفت‌وگوها اختلاف‌نظر وجود دارد.
بر اساس این گزارش، پاکستان از ایجاد کانال‌های ارتباطی جدید میان تهران و واشینگتن ابراز نارضایتی کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11748" target="_blank">📅 15:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11747">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/11747" target="_blank">📅 15:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11746">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/11746" target="_blank">📅 15:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11743">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OWaTFFNqfMZYB1HRYz0sUtO3jK-KzclZTgvbT7FkUti95z5mKpeJHeKDev8rAGEqDlgYWVIQgZaaZUEfFqfx1zCC8LUZVgpwDEpN9IGjuvf5R5AW2maTDYh5ymtVBdfnjJDDxsRIc8tZ7q7pvESdkmNQFO2uSNNA65pxQFqtr_xAvpJyKSasHZFpU5b-VDLaKRUou7bfyVbj1V9ADhy9Zn8M-oh6CDpHBfJ3HibSDKwzVoYzJoy3X0lG5lq8VQUMLddauH2aB6qrmBI267hv1GWk0AxlK7HFGKwtYDdFIZfss8te82IM9Em3-ODZA2MmqZOCbszAloSk74V7ySl4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xm6BDS4rON6sgL1AYShV7AkyKHnG-91xgYKEp3_fj2jRNJafZK6wXggR8x51FZZHMiE-bW_fwov6BTcdzGGlOoflXVVv4_Yc_soWErRo8nEjF9XS2PmKhcBcsPOVQ4iRZOH8QTv9RnNQGJllMFmNQ1WtRN77YI3i4kDh5jqdBvkKi8QfwsSAMu58-Ey33yTipP6YhHpC2PSNyQK_WnP3QIxzkg86APRbYVZI1w4xwaImUrFwBf05og7EGXlSTDOUg4GgpYiv1aYf3OzBvzWn3V3U4BPmF7HfUePYSdRVvx_6qgJMidj4tYtW3GwG2Az-llKSkyx0HNR0rTUGxU1_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkdfEwOtjPHTFVbXrIQ3aiB_3mN1xpSZSGKlcWpzlv_qyPuSlE-AVLUsm_WLlnxl05gJtq23ZJs9INCifbqkePBTNXhzc6PB_oiRKaI3_7jHwfzIAFNyKOwmhfch3qBGDvoJIZaf-yjAupqgVx62Q6N2K2R3D0ELwNr2oDrYjZo7oEW0e3tsKGJkN0iFbN0MrGuh52xtoLo7aTe0RLsynjwZ6yEGleYSaWhE9F1TULfALIVv_M9shCtcpUKmJjU4UsZEsF8zV1pWKNQRLgVN07Mae6BuQRWf7ikzrRlf_nLFwx4Rl4Jk8_zrQ4uDRA9TBm1eHCtrIDcGSzWfXau5pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فال حافظ محمد رضا پهلوی…
فلک به مردم نادان دهد زمام مراد
تو اهل فضلی و دانش همین گناهت بس
@withyashar
عکس اون روز هم به دقیق ترین حالت ممکن براتون بازسازی کردم
@withyashar</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/11743" target="_blank">📅 15:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11742">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">من رفیق نیمه راه نیستم! مرسی از پیغام های زیباتون
😃
تازه خلیلی هم خوش مسافرتم اینو همه دوستام میدونن ، شما هم دیگه متوجه شدید
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/11742" target="_blank">📅 14:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11741">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/withyashar/11741" target="_blank">📅 14:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11740">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11740" target="_blank">📅 14:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11739">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11739" target="_blank">📅 14:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11738">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گروسی: برای تضمین امنیت هسته‌ای به خلیج فارس سفر می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/11738" target="_blank">📅 13:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11737">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وزیر کشور پاکستان عازم تهران شد
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/11737" target="_blank">📅 13:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11736">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/11736" target="_blank">📅 12:55 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
