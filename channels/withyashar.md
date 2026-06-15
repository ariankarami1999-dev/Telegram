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
<img src="https://cdn4.telesco.pe/file/sm34u3GX-FugpzXxNJZws_30XSj_ZCYJqvCElZwthPaVd-zLvbG-yQUz3_1gbV-yWh_2Lln7JQzHrWcdh-JS5tJbB_ueNsWTWmd1D1-xLQ2eI9cGFU_ptInRD8ck6-lk5h0D8lxkDQ1i_bXSdHAHwIk7RdrxiGhA0WspqYVdC0u-EP26RI_XWLH_ihOEgJBHWluI41VN7mc8v4qNI7cRE0CesdaRp0PIdVljHVSMYDosrEjAGMxkSFq0rU7lMYVwxWEs1f4FD9XHKZruWeuZum_-8-y2uFhhIKurg3c3c_1z_BQnW-nTSZJ-cs4irIALxSbGNu6DArus2hlPkVpO0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 18:28:11</div>
<hr>

<div class="tg-post" id="msg-14968">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جزئیات دیگری از یک اتفاق قابل توجه درباره ساختار تفاهم اسلام‌آباد
یک منبع نزدیک به تیم مذاکرات در گفتگو با خبرنگار تسنیم، جزئیاتی از یک اتفاق قابل توجه در روز آخر مذاکرات مطرح کرد : بند 13 تفاهم‌نامه مربوط به این موضوع است که تا زمانی که برخی بندهای دیگر تفاهم‌نامه عملیاتی نشده، مذاکرات درباره توافق نهایی یعنی موضوع هسته‌ای صورت نمی‌گیرد.
وی خاطرنشان کرد: تا پیش از روز آخر مذاکرات، بند 13 شامل بندهای 4 و 5 و 10 و 11 بود؛ بند 4 مربوط به رفع محاصره دریایی، بند 5 مربوط به آغاز بازگشایی تنگه هرمز، بند 10 مربوط به اسقاطیه تحریم‌های مربوط به فروش نفت، پتروشیمی و مشتقات ایران و همچنین بند 11 مربوط به آغاز آزادسازی اموال بلوکه شده ایران است.
بنابراین بند 13 به این اشاره داشت که اگر این 4 بند گفته شده (4 و 5 و 10 و 11) انجام نشود، مذاکرات توافق نهایی آغاز نمی‌شود.
این منبع مطلع تاکید کرد: اتفاق مهمی که روز آخر مذاکرات به وقوع پیوست این بود که با پیگیری ایران، بند 1 نیز به بند 13 اضافه شد.
به گفته این منبع آگاه، معنای مهم این اتفاق آن است که اگر جنگ و هرگونه عملیات نظامی، از قبیل ترور و ... در ایران یا جبهه مقاومت از جمله لبنان اتفاق بیفتد، طبق تفاهم هیچگونه مذاکراتی برای توافق نهایی صورت نمی‌گیرد و طبیعتا اجرای تفاهم‌نامه (از جمله بازگشایی تنگه هرمز) از لحاظ ماده ۱۳ متوقف خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/withyashar/14968" target="_blank">📅 18:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14967">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عراقچی: جمعه تفاهمنامه ایران و آمریکا امضا می‌شود
اقتصاد ما نباید خود را متکی و موکول به این قبیل توافقات اقتصادی از طریق مذاکره با آمریکا بکند
در راستای منافع کشور، نیمی دیگر از راه مانده که باید طی کنیم که نیمه سختی خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/withyashar/14967" target="_blank">📅 18:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14966">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3gJ-K4mdRwKJxBKSdyntkU5TbW9eANzP6ps-cu_jpqWzgHX0HpForTIgYgLU5MV_emlgsAOm6WTpAP174vubJtsMQSmsv49GimemEL7S1RCoEQILNCkqG9anYnaTOvE4_3eEGhgDWBcYGIvia-KZIkhTe6kPUul65IhPJCR1riU-Ysh6oCchK8FLTBQ4C07M47OQKDFP8OX9GUCmS65CbsueNYtZENJvxTq8k52ySKfuuWoeokOLUZ4n8QSHWuPq43uY88-Nby5mj_7ZTwAgFN6s1Ib20mv8a4R3ObUXYjnAr7r1GbwyRY1Sv0cthfFHNTWZCrbKMbSApXWsViKVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ در‌تروث: متأسفانه، اگر افراد را از کشورهای جهان سوم وارد کنید، به سرعت خودتان تبدیل به یک کشور جهان سوم می‌شوید و هیچ کاری نمی‌توانید در این باره انجام دهید
آمریکا را دوباره بزرگ کنیم!
@withyashar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/withyashar/14966" target="_blank">📅 18:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14965">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ادعای جی‌دی ونس درباره ایران: ما دیروز به صورت دیجیتالی پیش توافق را امضا کردیم
@withyashar</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/withyashar/14965" target="_blank">📅 17:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14964">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=NiZewHQpNYihyGg_ZhTI-OQjf72gz14dM5ZhOI1fnSH4U-ybkGtWFM5CWBMNxco6_CiA9moNR_1nG4MxZaLVie7XKfclzjhor4LA62TXVbonXbIbYXDKvopYPu5OSomnPWTJAyShXORYKMTK4kT67b7VtSyf_2Km3hUSXdwWWhhY4FzHZjAV0Uv3OE3fC9ql_rFDlDUVJXWi0XR9maSlK_yg0i5wC1lUmKfWAScNlDAnDsAoP97xSYuOxGDdKATpXOGo0Eup6zjxLStITtGVV8Vj1HYK8hEumRjWbOTvUcmh9xZQRWWYejmihbYf8D02j2EDxx6ai0yq0gt1iLexP7ha6SmIhYacZ0aHEjM99ROHiIW7BlX_r4RMRoObmJHzJHpk5oIyi4WnYRSIWvAdIf8nva5d4Hpd3ggMolF7pzo4bLIBjvyKt9A0hzOAlBgvvfgWVVzaTGAO1qwhStn7xApoGxLTOYpuI1GN5yNGm6hEs09WRARr-8bzxW1CPWzT5o6aba2ZcGOa1DLG8cARZVPF8MYmRSf_zmCDD_1agf0AHaRa58inUC5sH9hMXTLHW1ZTvQmsTrdZbUHWSGEzBvgMeoMDZ55UUQrYSbofDJfIdYcy3-frsOhzXHRvUcZ9h1renWm3FcqzP0C0se_VY8E5stkDq5rC7WdDDTeZB4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/406b9170ab.mp4?token=NiZewHQpNYihyGg_ZhTI-OQjf72gz14dM5ZhOI1fnSH4U-ybkGtWFM5CWBMNxco6_CiA9moNR_1nG4MxZaLVie7XKfclzjhor4LA62TXVbonXbIbYXDKvopYPu5OSomnPWTJAyShXORYKMTK4kT67b7VtSyf_2Km3hUSXdwWWhhY4FzHZjAV0Uv3OE3fC9ql_rFDlDUVJXWi0XR9maSlK_yg0i5wC1lUmKfWAScNlDAnDsAoP97xSYuOxGDdKATpXOGo0Eup6zjxLStITtGVV8Vj1HYK8hEumRjWbOTvUcmh9xZQRWWYejmihbYf8D02j2EDxx6ai0yq0gt1iLexP7ha6SmIhYacZ0aHEjM99ROHiIW7BlX_r4RMRoObmJHzJHpk5oIyi4WnYRSIWvAdIf8nva5d4Hpd3ggMolF7pzo4bLIBjvyKt9A0hzOAlBgvvfgWVVzaTGAO1qwhStn7xApoGxLTOYpuI1GN5yNGm6hEs09WRARr-8bzxW1CPWzT5o6aba2ZcGOa1DLG8cARZVPF8MYmRSf_zmCDD_1agf0AHaRa58inUC5sH9hMXTLHW1ZTvQmsTrdZbUHWSGEzBvgMeoMDZ55UUQrYSbofDJfIdYcy3-frsOhzXHRvUcZ9h1renWm3FcqzP0C0se_VY8E5stkDq5rC7WdDDTeZB4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: ایرانی‌ها می‌گویند قرار است به یک صندوق ۳۰۰ میلیارد دلاری برای بازسازی دسترسی داشته باشند. درست است یا نادرست؟
جی‌دی ونس: چنین چیزی می‌تواند در دسترس آن‌ها قرار بگیرد، مشروط بر اینکه به تعهدات خود در این توافق پایبند باشند.
@withyashar</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/withyashar/14964" target="_blank">📅 17:28 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14963">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLo-DfizU2EnGt-MpCroH01ugMoTL5v7DyFq6aTYN6QUEj2p10E0QM9Ex4fOh_CiGTJ4kQ6_Z9sDXOVrpY_UZU_2fEaFS6ceL8dKoCDejJx7d5YMD8hXJCU2Vyb8w0pnN0JlOfZ74XUUA_oJ9r3pBM4DsgIAkp7wk-58WhEeTlno85F4ICzcmMNXkLAiWLrugJWMYh6YIEh5yIKrDCwQVJ108m8sIrGMP80jgOLRdSdU3hxLck9hF3i1bbOo7ZKw3AT6jM9boveasxyb6Pbu3DiITv4GXzK_QXs-vUKFikkf6Xtq08aY1Jyceg1G6WH54XKm4dhPhoqW0OokbJhOYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث: کشتی‌ها شروع به حرکت کرده‌اند، بسیاری از آنها با نفت بارگیری شده‌اند، از تنگه هرمز خارج می‌شوند.
آنها در امتداد «بزرگراه» جنوبی حرکت می‌کنند که کاملاً ایمن، مطمئن و بکر است. مناطق دیگری برای سفر نیز وجود دارد!!!
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/14963" target="_blank">📅 16:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14962">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مکرون:  پرداختن به برنامه موشک‌های بالستیک ایران در مذاکرات آینده مهم است.
@withyashar</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/withyashar/14962" target="_blank">📅 16:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14961">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تسنیم: یک منبع آگاه در گفتگو با خبرگزاری تسنیم، درباره وضعیت نیروهای آمریکایی در منطقه طبق تفاهم اسلام ‌آباد گفت: بر اساس ماده 4 تفاهمنامه، 30 روز پس از توافق نهایی، نیروهای رزمی آمریکایی باید از محیط پیرامونی ایران خارج شوند.
همچنین بر اساس بند 9 تفاهمنامه، در طول 60 روز مذاکرات برای توافق نهایی، نیروی جدید آمریکا در منطقه اضافه نمی‌شود و ایران نیز در این بازه اقدام هسته‌ای انجام نمی‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/14961" target="_blank">📅 16:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14960">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مقام ارشد کاخ سفید به آکسیوس:
هیچ دارایی مسدود شده ایران پس از امضای یادداشت تفاهم نامه در روز جمعه میان ایران و آمریکا آزاد نخواهد شد، همچنین هیچ کاهش تحریمی نیز برای ایران اعمال نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/14960" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14959">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ونس درباره توافق: جزئیات زیادی هنوز برای حل شدن باقی مانده است!
انتظار می‌رود طیف کاملی از نمایندگان ایران در مراسم امضای روز جمعه حضور داشته باشند
@withyashar</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/withyashar/14959" target="_blank">📅 16:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14958">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بقائی: ایران و عمان امنیت تردد در تنگه هرمز را تأمین می‌کنند هزینه‌های خدمات ناوبری و بیمه کشتی‌ها طراحی و دریافت می‌شود
مذاکرات هسته‌ای و رفع تحریم‌ها ظرف ۶۰ روز آغاز می‌شود
به اسرائیل اصلاً اعتمادی نیست همون‌طور که به آمریکا هم اعتماد نداریم تجربه هم نشون داده اینها در عمل به تعهداتشان هیچ‌وقت صداقت نداشتند
@withyashar</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/14958" target="_blank">📅 16:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14957">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">صدا و سیما: تنگه هرمز تا اطلاع ثانوی بسته است و بیش از ۹۶ ساعت است نیروی دریایی سپاه اجازه عبور هیچ شناوری را نداده است
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14957" target="_blank">📅 14:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14956">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/14956" target="_blank">📅 14:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14955">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f253e5fb18.mp4?token=gOswsR3u3nhwpGF5FeryS1eowd7a7-H46e_8vXcN-VCXWEMyVE_POFJvPDMb4pVrXvKcTpe2DYkuMaSezc5oLT-s9M6QXAT0Vwr_zQFjgDl_4i_VaJ-Y1o71ig4dj4zXRvXn-EMlUt18MP6iDKYYWNhbTU4eIpR7-50CQwc3zK1eT4Rtckg1e7vf4o8rGwmrgyrLcHnaXNF2eKhhPAxbSP7gO00Ib51X_yw1af7DzVFB6YEjYSNrdSk50X2ihu0dUBYBFUzD7JAltuzes1N9mG3GA0yph9FjDMXv6iLLnq1ojYwpO0kCKhxmAk4OUCNL00jO0Pjhk85WmvfHVLJU3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f253e5fb18.mp4?token=gOswsR3u3nhwpGF5FeryS1eowd7a7-H46e_8vXcN-VCXWEMyVE_POFJvPDMb4pVrXvKcTpe2DYkuMaSezc5oLT-s9M6QXAT0Vwr_zQFjgDl_4i_VaJ-Y1o71ig4dj4zXRvXn-EMlUt18MP6iDKYYWNhbTU4eIpR7-50CQwc3zK1eT4Rtckg1e7vf4o8rGwmrgyrLcHnaXNF2eKhhPAxbSP7gO00Ib51X_yw1af7DzVFB6YEjYSNrdSk50X2ihu0dUBYBFUzD7JAltuzes1N9mG3GA0yph9FjDMXv6iLLnq1ojYwpO0kCKhxmAk4OUCNL00jO0Pjhk85WmvfHVLJU3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت تو اجلاس گروه ۷ به فرانسه پرواز کرد
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14955" target="_blank">📅 14:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">والانیوز عبری: تاکنون هیچ درخواستی از جانب امریکا برای خروج اسرائیل از لبنان وجود ندارد!
@withyashar</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/14954" target="_blank">📅 13:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری واس: شاهزاده فیصل بن فرحان، شاهزاده سعودی در گفت‌وگو با عراقچی اعلام کرد سعودی از توافق برای پایان دادن به عملیات نظامی استقبال می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 98.8K · <a href="https://t.me/withyashar/14953" target="_blank">📅 13:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f0a7cffc.mp4?token=rkaoj6POP7QUC9F-Aopjxooe4Pz6TkaK2NDLk14ImGbftwuHEB-83lw4_jklrtagkoC6sqx6ogce9cKc26NXVfl1BK-GrW60tboMVvISCtsdaltHsfptelz08OdsjhlxHq3XGfjqJeSwSbcMoEU6mdZyEDnHc_XPvnregDtDmUnRnoXDrjocnaN-28iRL39Ckf5svq739TBknDwFtJcDbVWISMiCQSOfTkcOphXdW3HzAmrE4Vo7dLvucKLvik5FKy3_9Y_ZpwE-1dChBHO_tQeBdBujk6h3iZz0ixGKHsOGUOkD-_7dpY27vH4A1ex-QWx8tus1RMJ-Gxi81q2XOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f0a7cffc.mp4?token=rkaoj6POP7QUC9F-Aopjxooe4Pz6TkaK2NDLk14ImGbftwuHEB-83lw4_jklrtagkoC6sqx6ogce9cKc26NXVfl1BK-GrW60tboMVvISCtsdaltHsfptelz08OdsjhlxHq3XGfjqJeSwSbcMoEU6mdZyEDnHc_XPvnregDtDmUnRnoXDrjocnaN-28iRL39Ckf5svq739TBknDwFtJcDbVWISMiCQSOfTkcOphXdW3HzAmrE4Vo7dLvucKLvik5FKy3_9Y_ZpwE-1dChBHO_tQeBdBujk6h3iZz0ixGKHsOGUOkD-_7dpY27vH4A1ex-QWx8tus1RMJ-Gxi81q2XOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون امام علی نزدیک خیابون دماوند
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14952" target="_blank">📅 12:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">تتر ۱۶۳.۵۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14951" target="_blank">📅 11:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کانال ۱۲ اسرائیل: حدود ۱۰ ساعت از اعلام توافق بین واشنگتن و تهران می‌گذرد اما نتانیاهو هنوز در سکوت به سر می برد
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14950" target="_blank">📅 11:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نشست سران گروه هفت (G7) امروز در شهر اویان-له-بن فرانسه برگزار می‌شود؛ جایی که رهبران کشورهای صنعتی جهان درباره‌ی مجموعه‌ای از بحران‌های جهانی گفت‌وگو خواهند کرد.
گروه G7 یک گروه متشکل از هفت اقتصاد بزرگ جهان شامل آمریکا، بریتانیا، کانادا، فرانسه، آلمان، ایتالیا و ژاپن است که از دهه‌ی ۱۹۷۰ و پس از بحران نفتی اوپک شکل گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14949" target="_blank">📅 11:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ایران فعلا در تنگه هرمز پولی دریافت نخواهد کرد
ایسنا: براساس جزئیات تفاهم‌نامه، ایران تنگه هرمز را مدیریت خواهد کرد و عوارض را «در تاریخ بعدی» دریافت خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14948" target="_blank">📅 11:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">️ترامپ به نیویورک تایمز:
«کنار آمدن با نتانیاهو فوق‌العاده دشوار است و او باید از ما بسیار سپاسگزار باشد، زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل وجود نداشت.»
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14947" target="_blank">📅 11:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر دفاع اسرائیل: همراه با نتانیاهو سیاستی روشن را دنبال میکنم که بر اساس آن، ارتش در مناطق امنیتی در لبنان، سوریه و غزه باقی خواهد ماند
با وجود تمام فشارهای فعلی و آینده، خروج ارتش اسرائیل از لبنان را نمیپذیریم
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14946" target="_blank">📅 10:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=brBjXH3uOn5mhWNsSIl_BtiL-KU4HPkm7ELuOHytkrDNoR68Wo_P2lXOn3aMnt8xaT1X34D2TLWN3wiUWez6UX2LPYlt6NWuJUyHdcB7l5mi9Wztg9F5SCVBfceuBMJH-v_n5PLiLlslXC_2m3S6eP3WN84VDCyPBbv-FBLMQOgSlErLVsViw4OL5dRn8tqty_r3e07sRBbQF9fpGH3lFZmU68ri-puSZ1xNfUL1Zx9rjjrcxOC6EXnJ1ecm5b32vc7IQuwgYgNd65lsqAfMpKH45XwfS8KprHKTZRAKqX_XY-x6zCeFU53Uh0mLMqf52IGJnvxj5t7Dc2MAvGoHOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d30fe0e63.mp4?token=brBjXH3uOn5mhWNsSIl_BtiL-KU4HPkm7ELuOHytkrDNoR68Wo_P2lXOn3aMnt8xaT1X34D2TLWN3wiUWez6UX2LPYlt6NWuJUyHdcB7l5mi9Wztg9F5SCVBfceuBMJH-v_n5PLiLlslXC_2m3S6eP3WN84VDCyPBbv-FBLMQOgSlErLVsViw4OL5dRn8tqty_r3e07sRBbQF9fpGH3lFZmU68ri-puSZ1xNfUL1Zx9rjjrcxOC6EXnJ1ecm5b32vc7IQuwgYgNd65lsqAfMpKH45XwfS8KprHKTZRAKqX_XY-x6zCeFU53Uh0mLMqf52IGJnvxj5t7Dc2MAvGoHOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین شناوری که پس از اعلام توافق صلح میان ایالات متحده و جمهوری اسلامی ایران از تنگه هرمز عبور کرد، نفتکش گاز طبیعی مایع (LNG) با پرچم مالت به نام “دیشا” (Disha) است که از طرح تفکیک ترافیک دریایی ایران استفاده کرد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14945" target="_blank">📅 10:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">حمله اسرائیل به الخیام جنوب لبنان!
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14944" target="_blank">📅 10:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">کانال ۱۳ اسرائیل به‌نقل از یه مقام ارشد:
توافقی که داره صورت میگیره فاجعه‌بارترین توافق تاریخه. از نخست وزیر گرفته تا رئیس ستاد ارتش کل غیر از این فکر نمیکنه
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14943" target="_blank">📅 10:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gw_a-1rbevh3G5M8tvd2qvi_CXau7G-xmR_mTOqy0z19RI3BBs2dfaH-infXlMgHlyJLovk2jrmuiGWePN5ZslPgZI9QMPz2jWEG3yHFkE6xC1RQQb3ta5VwgD8p6Bfv_hpq41DKRRE0uLe72bkQ3TXwbcuXq8nDvdZATFe_3_t_iDWsAeLajUBTVoUwLLLLJvPM8VCeIfNFLA8g6Rr6_gzx2EdwO4YjCnNk0hz4Czf-9AEaKIyKSs7y7nPTwJ_JuK3norEBJYzfbQfacHIxGef4GPvehBZhmvFG2cwRXznnDT8_uMRBtQ0F0h9xVqZKRqAvacuNNhQNcG09CwOokw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق خوب، توافقی است که هیچ یک از طرفین راضی نباشند
-کتاب قدرت مذاکره جلد سوم صفحه ۲۳۶
یه توافقی بستم که هم ایران ناراضیه هم ملت ناراضی هستن هم براندازا ناراضی هستن هم آمریکا ناراضیه هم اسراییل ناراضیه
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/14942" target="_blank">📅 03:17 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نیویورک تایمز: تهران نهایی کردن توافق را تا بعد از نیمه‌شب به وقت محلی به تعویق انداخت تا از همزمانی این لحظه تاریخی با تولد رئیس‌جمهور ترامپ در روز یکشنبه جلوگیری کند
اختلاف زمانی هفت و نیم ساعته به هر دو کشور ایران و آمریکا اجازه داد تا جدول زمانی مورد نظر خود را حفظ کنند، به طوری که ترامپ گفت توافق در روز یکشنبه نهایی شده در حالی که مقامات ایرانی تأکید داشتند که این توافق در روز بعد به پایان رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14941" target="_blank">📅 03:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ به نیویورک تایمز: نتانیاهو فرد بسیار نمک نشناسی است. او باید به شدت از ما بابت انجام این کار سپاسگزار باشد.
زیرا اگر ایران سلاح هسته‌ای داشت، اسرائیل دو ساعت هم دوام نمی‌آورد.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14940" target="_blank">📅 03:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پرزیدنت ترامپ به نیویورک تایمز گفت که در صورت شکست مذاکرات برای دستیابی به توافق هسته ای نهایی، حملات نظامی خود را علیه ایران از سر خواهد گرفت.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14939" target="_blank">📅 02:55 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14938" target="_blank">📅 02:53 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">@withyashar
khatme kalam</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14937" target="_blank">📅 02:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14936" target="_blank">📅 02:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نیویورک تایمز
:  محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، و عباس عراقچی، وزیر امور خارجه، برای امضای توافق با جی‌دی ونس، معاون رئیس‌جمهور، به ژنو سفر خواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14935" target="_blank">📅 02:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هم اکنون محاصره دریایی آمریکا علیه ایران کاملا برداشته شد
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14934" target="_blank">📅 02:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14933" target="_blank">📅 02:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14932" target="_blank">📅 02:29 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14931" target="_blank">📅 02:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">@yasharrapfa
👻</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14930" target="_blank">📅 02:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قشم شنیده شدن صدای انفجار از سمت دریا
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14929" target="_blank">📅 02:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش های از صدای انفجار از فرودگاه مشهد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14928" target="_blank">📅 02:14 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جزئیاتی از یادداشت تفاهم ایران و آمریکا
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
طبق گزارش المحور نیوز، آتش‌بس کامل در تمام مناطق و خروج اشغالگران صهیونیست از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14927" target="_blank">📅 02:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14926" target="_blank">📅 02:07 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14925">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شعار مرگ بر آمریکا دیگه کنگله
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14925" target="_blank">📅 02:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14924">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlm8sILZePHEj6Agzj9Az5Smrs5CExEPNs0vWhUdikEBdv0at886yT7ZjCJAzYwt0nJjzT5UjeoxBecsUJMrMQ1PSwD4cxzXKNHCX0Fl7ZMTzY_WrlgogDRFl440s7Wf5G6_zB3jOA9BIZt5bHcU2wJqorQmPwf0FDcBusde-z2KSY9aS4D8bBwOz5XuzWtglP-Uf6OtivoBU2PP1bTTNsUbX1ivVh4KEoH7tACm0UdLb7_UfTMdTq353O9zHdNTeeYf9D0DuhRu25orVOkRW3Sb8bopZcSE-nzNejWot4Re-6u_3Py5R29ipZKHDiMOqGuVLQmoiBLcEK5e4Fz5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14924" target="_blank">📅 01:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گزارش از سیریک پهپاد شلیک شد به سمت کشتی ها !
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14923" target="_blank">📅 01:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">@withyashar
⚽️</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14922" target="_blank">📅 01:50 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14921" target="_blank">📅 01:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">جنگ تمام نمیشود بشینید و ببینید
✌🏾</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14920" target="_blank">📅 01:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">جی‌دی ونس، معاون ترامپ اعلام کرد: من برای شرکت در امضای توافق با ایران به ژنو خواهم رفت
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14919" target="_blank">📅 01:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14918" target="_blank">📅 01:35 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14917" target="_blank">📅 01:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14916" target="_blank">📅 01:24 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فارس: دقایقی دیگر بیانیه رسمی دبیرخانه شورای عالی انقلاب ملی درباره توافق آتش بس منتشر خواهد شد
بر اساس این گزارش، ایران پس از حمله به ضاحیه بیروت، مذاکرات خود را لغو و آماده حمله به رژیم صهیونیستی شده بود. اما در نهایت با امتیازهای لحظه آخری که از سوی دونالد ترامپ، رئیسجمهور آمریکا ارائه شد، از جمله حفظ تمامیت ارضی لبنان و عقب نشینی اسرائیل از مرز لبنان و بازگشایی بلادرنگ محاصره،  متقاعد گردید که از انجام حمله خود صرفنظر کند.
همچنین مقرر شد نظام حقوقی تردد در آب‌های خلیج فارس با همکاری ایران و عمان  تنظیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14915" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14914" target="_blank">📅 01:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14913" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/610e7fc5e5.mp4?token=Ii0ZJ2Irpg9QIJd9P7SxBd6D4gvdcqdtLTra2dZCdwkwKTQjYO53CjX6mjcBPUBWG4jzPLm1gyoGzKvcJeDcSXO6drvPafk8aSPwA1S1QuqFyz0hW55ar99DSkmO7mDmQekrRkST1r_L2B35FuJbwjNH5wGX7PcrhbsS4OL7TC1OyrDW50m2GiEfZaYJbbwSwaUaGxnPrtCxU_dkxZFkGpeYcUFl1eHy1faCeyriCUtxiIbolgiPJxd9USnRYmIP2drMnlZAkM33mLDrBqZ8f2xki9cZZw_EsJDDjorpzjshdU-Ditg8jR_rfbKmXIAWrGxNCC4GXplX1fRD7Y6RyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/610e7fc5e5.mp4?token=Ii0ZJ2Irpg9QIJd9P7SxBd6D4gvdcqdtLTra2dZCdwkwKTQjYO53CjX6mjcBPUBWG4jzPLm1gyoGzKvcJeDcSXO6drvPafk8aSPwA1S1QuqFyz0hW55ar99DSkmO7mDmQekrRkST1r_L2B35FuJbwjNH5wGX7PcrhbsS4OL7TC1OyrDW50m2GiEfZaYJbbwSwaUaGxnPrtCxU_dkxZFkGpeYcUFl1eHy1faCeyriCUtxiIbolgiPJxd9USnRYmIP2drMnlZAkM33mLDrBqZ8f2xki9cZZw_EsJDDjorpzjshdU-Ditg8jR_rfbKmXIAWrGxNCC4GXplX1fRD7Y6RyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری صدا و سیما:
پیروزی رو به ملت تبریک میگم
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14912" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWzpYiSVsK5Um6H2uCALlgozM5o_4BMUB9YvlD4zjc7lnA1gRdeA4BUhyaQi6yQ9jSWtRqtI09AJxxAK6L0jqfQrvKV-WVoNRo1Pu7CEEwkmnEKwlIRL8H83aAq9j3HnA6kIeQmuwT3Snw6tUlc1nyuUmxloj0b6wCdzgjPqfZZ-CEehy15wz9gQcBQE_-H9K1MBSEMEuv7kVmVcajOT-sO1qIi-u89dEal-Mcft9quL27xxHNeQwSLIFgZYcHNR18FkhNHQ6jbWeiPuhwu_I9pB1WCzamrDoq9jrDnd7A2RosO2XyvxNIHtb5wyHUMmziSFaVrD5U8i31hqEzGZJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداسیما : ترامپو  وادار کردیم در همه جبهه ها جنگ رو متوقف کنه
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14911" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اتریوم داره پرواز میکنه
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14910" target="_blank">📅 01:04 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMGIMus5mCYMS573MlXRMvni9DZL7dHIGm6SVT25A6rXyuuulmRfOg7Tx1S0cvybNnsyzBxR8ECj38vPWXqOwwNBCa18mmRwn1fADri5qwlcf_DGOhgW7yzUOYTpXJyt8jBJqIhcOPVwvRTxoyFXBElPjma01XtenEMv-oPLppXdnXm0XRtH0t7AjT8Qh1ooM8otswiRfyMJExjQ14TeZvigS1nLHd_OyS_diWpVukgiL5Uuy13fr4maU3ebGNlmfaKoEDrhN1927PoxPYLwjqNp9o5fWon77oA_yTkb7R8GV8VWjktKmH4dy9SxGDQWRUdiUeDvVMMHsV-m21LE0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «توافق با جمهوری اسلامی ایران اکنون نهایی شده است. به همه تبریک می‌گویم! من بدین‌وسیله به‌طور کامل مجوز بازگشایی رایگان تنگه هرمز را صادر می‌کنم و هم‌زمان، دستور رفع فوری محاصره دریایی ایالات متحده را نیز صادر می‌نمایم. ای کشتی‌های جهان، موتورهای خود را روشن کنید. بگذارید نفت جاری شود!
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14909" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14908" target="_blank">📅 01:01 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14907" target="_blank">📅 01:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چیزی‌ امظا نشده
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14906" target="_blank">📅 00:58 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idKQDx6ZZmTVEBpJB1CmjHFAmtE70hLqERFS6phn33IW8h4JxqAq_OkxF4pGIcKJbSqNF-1nP3M04EEl0lZnocbLwX-1rO2FL-oEyHf_vvykvExhB68BpchkvULZocxxkqXhmTpmgJ4FWAt3Zdp6bt38O54266lfnI3ewrHCn0-HeSp9aTxR25cS1gbQbZp-GWgulFfIUa_Z3bgzk_A3ew7mJn5ZAC3sPxNHaEy4bhJWcEkR6GAgzi2eyV6bEcXpOhcS_XINBVBD-eJer47f0lGUQL6roh6KoJApBJcKhc4XIGBb6jnnIzbbG3mMDR7viAmQGWXKUAlxXjHdRmJPRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر :توافق با امریکا انجام شد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14905" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نخست وزیر پاکستان: پس از مذاکرات فشرده، با کمال خرسندی اعلام می‌کنیم که توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شده است. هر دو طرف توقف فوری و دائمی عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، را اعلام کرده‌اند.
مراسم رسمی امضای توافق‌نامه روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14904" target="_blank">📅 00:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ: «بعداً مسائل هسته‌ای را حل می‌کنیم» و افزود که «هیچ عجله‌ای نیست» و می‌توان ظرف یک یا دو ماه آینده به آن پرداخت
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14903" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: بزودی یک بیانیه خواهم داد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14902" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">خبر تسنیم فیکه مثل خودش
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14901" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🤣
🤣</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14900" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14898">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ می‌گوید توافق با ایران قریب‌الوقوع است، اما تهران تاکنون آن را تأیید نکرده است  رئیس‌جمهور در مصاحبه‌ای می‌گوید که قصد دارد به زودی بیانیه‌ای صادر کند و تأیید کند که ایالات متحده با ایران به توافق رسیده است @withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14898" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14897">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMUMZXYPf1gyNTLDH3ImzHIELMx9AiIbDQRkI3bqif6Be4T9RH0oXgBveRkcFdn-6il2G-bKBXAfWqwifCvlL-fWHuhNLMpANR_cWnFZHTrrX3TIdBhU8pzZP4zNEgcYThh12l2x4B9OLVzXhMyF7HxFfEgMkCuiyj-rpI0uLWIfkjxUKUYiGbnMdnSrZikrDJtWhDnZ9pSfydt9mH3vDGviY64One-CdzeMYzRFc0whlWTkwEkQefup2YC2yVsQIaWy4H96TkIow1aFo_ynsoJQEpa19i2EUDHms9iFc74i4z7OZUXg8mQTNURRd2YIEbasfyJS5EZgt3wJXymr4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با ایران قریب‌الوقوع است، اما تهران تاکنون آن را تأیید نکرده است
رئیس‌جمهور در مصاحبه‌ای می‌گوید که قصد دارد به زودی بیانیه‌ای صادر کند و تأیید کند که ایالات متحده با ایران به توافق رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14897" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14896">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ به وال استریت ژورنال گفت که قصد دارد به زودی بیانیه‌ای صادر کند و در آن توافق آمریکا با ایران را تأیید کند
@withyashar
ترامپ کله پوک: من علاقه‌ای به تغییر رژیم در ایران ندارم</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14896" target="_blank">📅 00:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14895">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">توییت وزیر کشور پاکستان: الله اکبر
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14895" target="_blank">📅 00:34 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14894">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">میگن توافق امضا شد
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14894" target="_blank">📅 00:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14893">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سی‌ان‌ان: مذاکره کنندگان قطری همین حالا تو تهران حضور دارن تا با هماهنگی امریکا توافق رو به سرانجام برسونند و از نهایی شدن روند مذاکرات اطمینان کسب کنند
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14893" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14892">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حسین پاک، خبرنگار صداوسیما در لبنان:
امشب به صورت همزمان ایران، یمن و حزب‌الله به حمله اسرائیل به ضاحیه پاسخ می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14892" target="_blank">📅 00:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14891">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCsIk53gnVZR7aMWnnsb5C97r3Bz6f-4EdDwgoYJ8KjBWNiJ1fSHrMTMBkrAMaA5fLsms60K40utRfOVMuyarmEkftAqeD3OlcNuNtaXj29wj5B12EL_Uwb_6mjzRxaIjd3Ohkx3VUTRT8jxupFKk1YR0q76woSDXSahAz8vcysRfb60nipIrvBuFLxu6qytxdZ2gTXEzmV8vcA88KWHWIQCOTwLIkMwBnK-hxY2DfnlhdJynK3ce9UY6ZtPUrn5D4DpBn0t9DM_dUQ8UPz5IS0Zp6zMvYaKZsUL_2_bq7wb4ntaBplPOKFgFi5-nAfiSDcJpgqYn_qlOeowoEINOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد اومد بازی‌رو از‌ نزدیک دید
😂
بازی امروز آلمان و کوراسائو (Curaçao) در جام جهانی ۲۰۲۶ با نتیجه
۷ بر ۱ به سود آلمان
به پایان رسید.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14891" target="_blank">📅 00:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14890">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی @withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14890" target="_blank">📅 00:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14889">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ در تروث : ویکتوریا کوتس از بنیاد هریتیج واقعاً فوق‌العاده است! او مثل کمتر کسی این موضوع را درک می‌کند. ویکتوریا، متشکرم. ایران هرگز سلاح هسته‌ای نخواهد داشت و تنگه هرمز خیلی زود برای تجارت باز خواهد شد!!! رئیس جمهور دی‌جی‌تی
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14889" target="_blank">📅 00:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14888">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کانال ۱۲ اسرائیل: دقایقی پیش ترامپ و نتانیاهو گفت‌وگو کردن. ترامپ، نتانیاهو رو در جریان پیشرفت‌ها برای امضای توافق با جمهوری اسلامی قرار داد؛ توافقی که ممکنه حتی از امشب امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14888" target="_blank">📅 00:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14887">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیویورک‌تایمز: قطر در تلاشه تا اختلافات باقی مونده میان آمریکا و جمهوری اسلامی رو حل کنه تا همین امشب توافق امضا بشه.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14887" target="_blank">📅 00:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14886">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bknvjXVMpo5u03zN_D6KHIaJ5TMdUfSLzyvyut5Uxr71z01F_4su1NqiySUQsbBpMOoZB067DJ9Ron7o7IfRs6gPasr1zEqMtgfXT2VQRtcNlZt5rtxQpSps8KF49wJ__eSo5M1ANkW-mUAPfuEB3DxRWpxRupxR-J60pBhm8JdnoMrqmcQFTywxP_a_VZ5ABHmk2BZXCso1aWWaBo79i3ZEsqM8uvkT4gBKyRXMWlHihPPegK05NR_bOmYwOF4VzCHKcNYXctedwIWiTzv9FUXSGEI19-3Lqu4K3Q460rB_ydzUp1lpJdNS6Pab1VAjl2GVBSk6OzNzQBMsNVcqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث : جک رید، سناتور رود آیلند، گفته توافقی که الان بستیم از توافق زمان اوباما هم بدتره
به نظر من یا داره عمداً دروغ میگه یا اصلاً نمی‌فهمه موضوع چیه
توافق اوباما عملاً راه رو برای رسیدن ایران به سلاح هسته‌ای باز می‌کرد و کلی پول هم بهشون می‌رسوند؛
یکی از بدترین و احمقانه‌ترین توافق‌هایی که آمریکا تا حالا بسته بود
اما توافقی که ما الان انجام دادیم دقیقاً برعکسه؛ مثل یه دیوار محکم جلوی هرگونه دسترسی ایران به سلاح هسته‌ای رو می‌گیره
مقایسه کردن این دو تا اصلاً منطقی نیست. جک رید باید پاسخگو باشه
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14886" target="_blank">📅 00:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14885" target="_blank">📅 23:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‏سناتور لیندسی گراهام به انتقاد از ترامپ‌برای سرزنش بی‌بی:
«آمریکا در شرایط مشابه چه می‌کرد؟»
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14884" target="_blank">📅 23:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کارشناس شبکه افق:   امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند @withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14883" target="_blank">📅 23:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کارشناس شبکه افق:
امام شهید ما چونش را برای اورانیوم گذاشت ولی امروز مسئولین جلسه می‌گذارند و می‌گویند اورانیوم به درد نمی‌خورد/ کسانی که امروز به ترامپ امتیاز می‌دهند بدانند که حتی آن‌ها را هم ممکن است آمریکا ترور کند
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14882" target="_blank">📅 23:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSOOcweplxaOCsUK4meqiaU9ROYBe0t9vy-xXbeJthelo7eCUdIGMhnrWJu8OsMFJdcQBFJ3NdA70L-fZByn3NN-E5M9dKLmj0I95Qg0EiR6XoWSNrJM24_bF_NuIdDt8UVFlwqwFBSuRCw056-DzatkA90mmxu9iQoUUto7J9KIY-wlnMdVt28bt3RQDQ540BfV41jecfFEb-Eo8N8-6ZP5sw10OAvbECre0UuMOkujwYg9UxxlSmkM3Ct3I8yRm2rqa86Tj1G0qyV75pU-_2uwfXJzUXc9KBqFjzj2Zs4LZ-_pcOmC1uD1NJMatmmX38AisJUEFjHINtlJqNpt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: فرمان صادر شد؛ لانچرها آماده پرتاب میشوند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14881" target="_blank">📅 23:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تیم جمهوری اسلامی با ویزا ساعتی عازم لس آنجلس شد برای بازی با نیوزلند
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/14880" target="_blank">📅 23:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">وای نت: ممکن است ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایرانی به اسرائیل جلوگیری کند
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14879" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=K8H30TRznRrdkybu68psbZmRBNodUEvQRtmZ_0SIbOWbyM7jNXigo4MMcuAdouWqy192WW828tFe_9mbm-9LTEcq8SOevRzOKSfomR58kzDYMez7nCEgAtg3n1_VqKnJBl50iisZYthBMh59vsTFpWK9S_igGFrtjJc8vyqYgV2u_dxKjlyfV_EkUVtVUw0C7J1EZ_fVdm2HvIfz80ZNiq0m1dsPQImru9yPvZjqSlWNA6moE4nPkkS5AKwvHs73CT0KusYFBwzyvP7qqjRsce4zNNcaOxmcgUCanoBUNcUwiA6fJWZrUJQZeX3EPhq8MrXI5xELCFoZCl_mDuc7yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07020c75c7.mp4?token=K8H30TRznRrdkybu68psbZmRBNodUEvQRtmZ_0SIbOWbyM7jNXigo4MMcuAdouWqy192WW828tFe_9mbm-9LTEcq8SOevRzOKSfomR58kzDYMez7nCEgAtg3n1_VqKnJBl50iisZYthBMh59vsTFpWK9S_igGFrtjJc8vyqYgV2u_dxKjlyfV_EkUVtVUw0C7J1EZ_fVdm2HvIfz80ZNiq0m1dsPQImru9yPvZjqSlWNA6moE4nPkkS5AKwvHs73CT0KusYFBwzyvP7qqjRsce4zNNcaOxmcgUCanoBUNcUwiA6fJWZrUJQZeX3EPhq8MrXI5xELCFoZCl_mDuc7yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما:
امشب اسرائیل به شدت بمباران خواهدشد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14878" target="_blank">📅 23:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">راشن تودی: ورود اضطراری «جی دی ونس» به کاخ سفید همزمان با اوج‌گیری تنش‌ها در منطقه!
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14877" target="_blank">📅 23:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">کابینه اسرائیل: اگر ایران حمله کند، ما نیز حمله خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14876" target="_blank">📅 23:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشهایی از شما مبنی بر مشاهده موشک در آسمان
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14875" target="_blank">📅 23:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14874">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اسرائیل بی‌اعتنا به ترامپ عملیات خود در  لبنان را ادامه می‌دهد ، سه انفجار مهیب در شهرک الطیری در جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14874" target="_blank">📅 23:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14873">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ادعای رسانه‌های عبری:
تحرکات موشکی سپاه پاسداران در یزد، شیراز و اصفهان درحال مشاهده است
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14873" target="_blank">📅 22:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14872">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=upa1dYTq-qUpK0qGhfM3BV5-lPmhHZzWb3nqqQbilA2zLmseIDWhJFEjOzLid3n96nmbhvW4F86h2D1FwkL86MnwU5MzgDaY5_WYliDyhjQxrmr7h-KlLpl8QqH37d9-ZcHF83zaPbUCXEAEI5QvPZyiLG6rAPlh5s5VCa_WvX0SIWy2VpDUAx4jk6yQGL0Y-zJ6mOu2cwP4RAR2VZPps9Fa77MEPGra0jIB2fgdTkG-diYlfgmyKMacfokQv60sT0IIyM_YUPnkxhmrOEL8C1gy2fhcvKkehz-FuRLciqfr-0u2Ty9WHzmLkXtcXWyPRE3EkbuektAwCAjetOJFUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1cd002a5.mp4?token=upa1dYTq-qUpK0qGhfM3BV5-lPmhHZzWb3nqqQbilA2zLmseIDWhJFEjOzLid3n96nmbhvW4F86h2D1FwkL86MnwU5MzgDaY5_WYliDyhjQxrmr7h-KlLpl8QqH37d9-ZcHF83zaPbUCXEAEI5QvPZyiLG6rAPlh5s5VCa_WvX0SIWy2VpDUAx4jk6yQGL0Y-zJ6mOu2cwP4RAR2VZPps9Fa77MEPGra0jIB2fgdTkG-diYlfgmyKMacfokQv60sT0IIyM_YUPnkxhmrOEL8C1gy2fhcvKkehz-FuRLciqfr-0u2Ty9WHzmLkXtcXWyPRE3EkbuektAwCAjetOJFUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگست : ما در تمام این مدت کنترل تنگه‌ها را در اختیار داشته‌ایم.
‏مجری : اما شما در حال مذاکره با ایران هستید تا تنگه هرمز را دوباره بازگشایی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14872" target="_blank">📅 22:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14871">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">هاآرتص: نتانیاهو به ترامپ
نه
گفت
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14871" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14870">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خالیباف خطاب به اسرائیل بچرخ تا به بچرخیم
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14870" target="_blank">📅 22:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14868">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👻</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14868" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14867">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هیچ نوتام جدیدی درباره محدودیت پروازی صادر نشده است
مجید اخوان، سخنگوی سازمان هواپیمایی کشوری در گفتگو با خبرنگار مهر درباره برخی اخبار منتشرشده در فضای مجازی مبنی بر صدور نوتام جدید برای محدودیت پروازی در فضای هوایی کشور، اظهار کرد: هیچ‌گونه نوتام جدیدی در این خصوص صادر نشده است.
نوتام مربوط به محدودیت پروازی در غرب کشور، همان نوتام قبلی است و اطلاعیه جدیدی در این زمینه صادر نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14867" target="_blank">📅 22:25 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
