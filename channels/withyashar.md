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
<p>@withyashar • 👥 267K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 23:33:35</div>
<hr>

<div class="tg-post" id="msg-11795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edZgbVIu1eKyhbML0zstS9uS-zA0jCgID8UOUTJm0tpNyaypm1uJEm3DTLTK01Hy_l9codDV6O9JuLKpa-Hlzd0e9IJxvjIxV9sLg0NTOP451exgg020jo4VHbKx5foxeCCxypDRuFcbFOHvMbYBUb-0s7NojZuyC_KC0qPPGF0VGBEY_zxqdtH2MT4ibzZBCLGBXW5yrT-zuqh1tmdEGQ15Mp-P5LXGlcIGLA4wUzeTHyM3eX6f0kleUb7Dmg2eJDWONjZ2FvNTQE3gVTsKJaOu6UsWbYDLzBvlW0wc9_SzJl-1hLFkRE4E8-nSjppmtjUOaYLmwFPdLmNbJvfjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنیا با نفس حبس‌شده در انتظار موج بعدی اسناد یوفوهاست؛ پس از آنکه مقام‌ها وعده دادند این اسناد «به‌زودی» منتشر خواهند شد.
شان پارنل، سخنگوی ارشد پنتاگون، در ایکس اعلام کرد که این مدارک هم‌اکنون «به‌طور فعال در حال آماده‌سازی و پردازش» برای انتشار هستند.
مقام‌های سابق سیا و پنتاگون اخیراً مدعی شده‌اند «چهار گونهٔ بیگانه» به زمین رفت‌وآمد دارند: خزنده‌ها (Reptilians)، حشره‌مانندها (Insectoids)، گری‌ها (Greys) و نوردیک‌ها (Nordics).
آیا ما برای حقیقت آماده‌ایم؟
@withyashar</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/withyashar/11795" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گزارش کانال ۱۴ اسرائیل : آیا ارزیابی ایران از شرایط کاملاً اشتباه است؟
با وجود تبلیغات تهاجمی، تهران در خفا عمق بحران خود را درک می‌کند. حکومت روی لبهٔ تیغ حرکت می‌کند؛ از یک سو ترامپ را تحریک می‌کند و از سوی دیگر، به‌طور پنهانی افکار عمومی ایران را برای یک تشدید بزرگ نظامی آماده می‌کند.
افراد در داخل حکومت اذعان دارند که حملهٔ آمریکا بسیار محتمل است، اما روی این موضوع شرط بسته‌اند که ترامپ یک حملهٔ محدود انجام دهد، اعلام پیروزی کند و سپس متوقف شود.
«همهٔ ما فقط امیدواریم که این هم یکی دیگر از ارزیابی‌های اشتباه ایران از شرایط باشد.»
@withyashar</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/withyashar/11794" target="_blank">📅 23:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یک مقام اسرائیلی به روزنامه اسرائیل هیوم : حکومت ایران هنوز درک نکرده چه بر سر این کشور آمده و افزود همان‌گونه که این حکومت لبنان، عراق و یمن را به عقب‌ماندگی کشاند، اکنون خود ایران نیز به کشوری عقب‌مانده تبدیل شده است.
به گزارش اسرائیل هیوم، در اورشلیم سقوط حکومت ایران همچنان سناریویی محتمل تلقی می‌شود و مقام‌های اسرائیلی می‌گویند پس از پایان مرحله کنونی، احتمال ازسرگیری اعتراض‌ها وجود دارد.
این روزنامه همچنین نوشت آسیب‌های واردشده به ایران بسیار قابل توجه بوده و برآوردها حاکی است در دو دور درگیری حدود ۳۰۰ میلیارد دلار خسارت اقتصادی به ایران وارد شده است.
@withyashar</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/withyashar/11793" target="_blank">📅 23:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
نتانیاهو با نظر ترامپ در مورد مذاکره مخالفت کرد
@withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/11792" target="_blank">📅 23:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">کانال ۱۲ اسرائیل
: نیروهای آمریکایی بر روی یک نفتکش ایرانی در خلیج عمان سوار شدند.
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/withyashar/11791" target="_blank">📅 23:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11790">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/withyashar/11790" target="_blank">📅 22:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11789">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خبرنگار : از این رفت و برگشت با ایران خسته نمیشی؟
ترامپ : من هیچوقت خسته نمیشم ولی اگه با چند روز صبر کردن بشه جلوی جنگ و کشته شدن مردم رو گرفت کار خوبیه
@withyashar</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/withyashar/11789" target="_blank">📅 22:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11788">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ: چند روز منتظر پاسخ ایران می‌مانیم
ایران یک کشور شکست‌خورده است و ما امیدواریم بتوانیم با آنها توافق کنیم که این برای همه عالی خواهد بود.
من هیچ تحریمی را علیه ایران تا زمانی که به توافق برسیم رفع نخواهم کرد. تا زمانی که ایران توافق را امضا نکند به ایران هیچ معافیت نفتی نخواهم داد و پیشنهادی هم برای انجام این کار نداده‌ایم.
اگر پاسخ‌های درست را نگیریم، اوضاع خیلی سریع پیش می‌رود. همه ما آماده‌ایم. باید پاسخ‌های درست را به دست آوریم.
@withyashar</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/withyashar/11788" target="_blank">📅 22:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11787">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/withyashar/11787" target="_blank">📅 22:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11786">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مسعود  زرشکیان : وادار کردن ایران به تسلیم از طریق اجبار چیزی جز توهم نیست.
احترام متقابل در دیپلماسی بسیار عاقلانه‌تر، ایمن‌تر و پایدارتر از جنگ است
@withyashar</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/withyashar/11786" target="_blank">📅 22:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11783">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/11783" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11782">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/11782" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11781">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کلش ریپورت:  اردوغان در تماس تلفنی با ترامپ درباره روابط ترکیه و آمریکا و مسائل منطقه‌ای صحبت کرد.
@withyashar</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/11781" target="_blank">📅 22:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11780">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">به ادعای آکسیوس : امروز اوایل روز، بحث داغی در داخل کاخ سفید درباره ایران شکل گرفت، جایی که جی‌دی ونس، استیو ویتکاف و جرد کوشنر برای توافق اولیه‌ای جهت پایان دادن به جنگ تلاش می‌کردند، در حالی که پیت هگست و مارکو روبیو برای فشار بیشتر و احتمال اقدام نظامی استدلال می‌کردند
@withyashar</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/withyashar/11780" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11779">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">لطفا دایرکت بی مورد و چند پیغامه ندید
🙌🏾</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/withyashar/11779" target="_blank">📅 22:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11778">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اتاق جنگ با یاشار : اول مهر مدارس مختلط است
😎
@withyashar</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/withyashar/11778" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11777">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تسنیم به نقل از یک منبع نزدیک به تیم مذاکره‌کننده: پس از ارسال متن ۱۴ بندی ایران که سه روز پیش صورت گرفته است،
آمریکایی‌ها بار دیگر متنی را از طریق میانجی پاکستانی به ایران داده‌اند.
ایران در حال بررسی متن است و هنوز پاسخی داده نشده است.
میانجی پاکستانی در تهران به دنبال نزدیک کردن متون به یکدیگر است.
هنوز چیزی در این میان نهایی نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/withyashar/11777" target="_blank">📅 21:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11776">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/withyashar/11776" target="_blank">📅 21:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11775">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ادعای آکسیوس به نقل از یک منبع آمریکایی: ترامپ به نتانیاهو از یک دوره 30 روزه مذاکره درباره برنامه هسته‌ای ایران و تنگه هرمز اطلاع داد
@withyashar</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/withyashar/11775" target="_blank">📅 21:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11774">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خبرنگار العربیه: بعد از تماس اسرائیل در دو حمله هوایی شهرک‌های «حداثا» و «تول» در جنوب لبنان را بمباران کرد.
@withyashar</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/withyashar/11774" target="_blank">📅 21:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11773">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">«آکسیوس»: نتانیاهو از مکالمه تلفنی خود با ترامپ درباره ایران «بسیار عصبانی» شده بود. قطر و پاکستان تعدیلاتی بر طرح پیشنهادی برای پایان جنگ اعمال کردند.
@withyashar</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/11773" target="_blank">📅 21:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11772">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وب‌سایت «آکسیوس»: گفت‌وگوی اخیر ترامپ و نتانیاهو بسیار متشنج و دشوار بود.
@withyashar</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/withyashar/11772" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11771">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز:برخی کشتی‌ها بیش از 150 هزار دلار به ایران پرداخت می‌کنند تا عبور از تنگه هرمز را تضمین کنند.
‏هزینه عبور کشتی‌ها از تنگه هرمز برای همه کشورها اعمال نمی‌شود.
‏مکانیزم جدید ایران در تنگه هرمز به کشتی‌های مرتبط با روسیه و چین است
@withyashar</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/withyashar/11771" target="_blank">📅 21:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11770">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pp1LJa0aJ0zjr3QwkFWmJt2Pxv6X1oCPXB5x4mKWDnEb3IWWTzzc7GgAw7R7N5lR0_KtkGd7v3Vs3FeZuR2Iig2m2eo5Qz-Khn2Mh6AsEfiEePT1gy6IBZlE5vdtPoYNvu5wFXOCDNgB7FlKObhurpBcFnoEsSehvNr8W5N-AQBslxHqYiWZVIj2ZOH33wELOYui0FS7R9tE5q5fVFjL4Oh6GplwN-vdS4e9ls2yTW0ZAPToVS2Fhib_5wHqz0mhUyA09OHn-MTmxRu0B2iBIwxPgyDWR-_hFBpnI3N7s4Uan0giRW1VUJOyuP9DVBVEFiIslQ5x09Eth6AS__-nTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/11770" target="_blank">📅 20:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11769">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">یه مقام ارشد اسرائیلی : اطرافیان ترامپ دارن روش فشار میارن که به توافق برسه  نتانیاهو هم باهاش درباره این موضوع صحبت کرده، و از نظر ترامپ گزینه حمله وجود داره که فقط بحث زمانشه
@withyashar</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/withyashar/11769" target="_blank">📅 20:49 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11768">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دونالد ترامپ:
هیچ‌وقت تسلیم نشو. هر اتفاقی که بیفتد، مهم نیست در چه جایگاهی از زندگی هستی یا در چه شرایطی قرار داری، به جلو حرکت کن و ادامه بده.
همیشه رو به جلو حرکت کن. هیچ‌وقت از پیش رفتن دست نکش.
@withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/11768" target="_blank">📅 20:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11767">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دونالد ترامپ دربارهٔ ایران:
ما ضربهٔ بسیار سختی به آن‌ها وارد کردیم. ممکن است مجبور شویم حتی سخت‌تر هم به آن‌ها ضربه بزنیم اما شاید هم نه.
ما اجازه نخواهیم داد ایران به سلاح هسته‌ای دست پیدا کند و کل خاورمیانه را منفجر کند و بعد هم به اینجا بیاید و شما را هدف قرار دهد.
@withyashar</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/withyashar/11767" target="_blank">📅 20:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11766">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">اتاق جنگ با یاشار : امشب میخوام یه تحلیل سنگین کنم با طعم پیشبینی ، خواهیم دید چه خواهد شد !</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/withyashar/11766" target="_blank">📅 19:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11765">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73c5fdf4b.mp4?token=bzh91s_Z57pjaJPe_G-GBbZKEIq2sQwQ9K25RAecBG4bSmgV0woS-ca0fVwXA3md7Wmq_l2d_kBEDCru2ZZ-F172T6LNVsEF50cxGT7DppO15s_qnVO9wXO582MT_dyyeku-TCEXZ-82sI6SnU4-4uKuvGcoUyReVsQqbngzBbVIEDvaQqOHhQ3AhgGJL5bZzPIvtiuNOpA4irH2nC7MJWEABQ34Yl08nh30nsZ8khXfS3osd3cUv_gx5zm5uENGM7i3FTwbep-lz9JJK0PefKGZ45sEX_oliAjrYxGFvIEwtZjwCoxwaPNP2DNOPaGAwjvMgR8IyaSJPHQT0l23uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73c5fdf4b.mp4?token=bzh91s_Z57pjaJPe_G-GBbZKEIq2sQwQ9K25RAecBG4bSmgV0woS-ca0fVwXA3md7Wmq_l2d_kBEDCru2ZZ-F172T6LNVsEF50cxGT7DppO15s_qnVO9wXO582MT_dyyeku-TCEXZ-82sI6SnU4-4uKuvGcoUyReVsQqbngzBbVIEDvaQqOHhQ3AhgGJL5bZzPIvtiuNOpA4irH2nC7MJWEABQ34Yl08nh30nsZ8khXfS3osd3cUv_gx5zm5uENGM7i3FTwbep-lz9JJK0PefKGZ45sEX_oliAjrYxGFvIEwtZjwCoxwaPNP2DNOPaGAwjvMgR8IyaSJPHQT0l23uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای هزارمین باز: همه چیز از بین رفته تو ایران
تنها سوال من اینه که آیا ما میریم و کار رو تمام می‌کنیم؟ ، یا اونا قراره سندیو امضا کنن؟ خواهیم دید چه خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/11765" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11764">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/11764" target="_blank">📅 19:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11763">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92ddb6e4b5.mp4?token=D3hDj8g5i6GYK8tqsGPHOgqyYv_GDPRmXGcT5uaSbkhjTB9uPRAZq2umP1XDiSDZ1sqFrJ2Ot5cddbHXb6tnxu73LYHyr0kvmEFZgV6J8X95RacN_49qQUa5lnQ6PTGvDcDMohEqFPk4ccdcn2Jz8YV-rQ1YqBIG9rRohXgWb7dQ6dlEUSxTO3mqTbqO658YGGThldYEmTBan3s6Jwz0KBobmvX5lJunk-j5raskzRXAeRBgb9M5CH50oCn5s8oKKu-q0wOrr3kt8vPLXM7sUE0Rc5mNOmqeYtRMvAMXra900G-MnKl67cmj2-qJhSsN9eFyW-5lvNrf9xtEpYsMpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92ddb6e4b5.mp4?token=D3hDj8g5i6GYK8tqsGPHOgqyYv_GDPRmXGcT5uaSbkhjTB9uPRAZq2umP1XDiSDZ1sqFrJ2Ot5cddbHXb6tnxu73LYHyr0kvmEFZgV6J8X95RacN_49qQUa5lnQ6PTGvDcDMohEqFPk4ccdcn2Jz8YV-rQ1YqBIG9rRohXgWb7dQ6dlEUSxTO3mqTbqO658YGGThldYEmTBan3s6Jwz0KBobmvX5lJunk-j5raskzRXAeRBgb9M5CH50oCn5s8oKKu-q0wOrr3kt8vPLXM7sUE0Rc5mNOmqeYtRMvAMXra900G-MnKl67cmj2-qJhSsN9eFyW-5lvNrf9xtEpYsMpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/11763" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11762">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b1ee80c2.mp4?token=nHdOv3_xgQ6cUG5G1Cho2bO1779m0fOrBVPnlmI8pVaeGEpZ_ZXEbNQ53LaWXCTeZPw1KHLrCmlOYhRSeKwT_mv8HmSpuaS_JPboEoEObxJnHVUeJ68mgczCrBVUsTl3dK-0WMnnnX8dEiWYLAlJyIEo__tmw4YeHQh_xSMM3LQ_FgBR19R75WZIWOIKrC0oKnEEwuoSaPGH1rTeVrxde270NLbUI6geOv_qGH0YSPncbYNq7eSR1mKrBW0UbH3NxB1rnWK1wmznOEaRANDQ3yal3wr602IynmInwQSNK2pgbB4tAqwtGHpF2iOINOwDaE2kwmDCuwwt15VQLDP_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b1ee80c2.mp4?token=nHdOv3_xgQ6cUG5G1Cho2bO1779m0fOrBVPnlmI8pVaeGEpZ_ZXEbNQ53LaWXCTeZPw1KHLrCmlOYhRSeKwT_mv8HmSpuaS_JPboEoEObxJnHVUeJ68mgczCrBVUsTl3dK-0WMnnnX8dEiWYLAlJyIEo__tmw4YeHQh_xSMM3LQ_FgBR19R75WZIWOIKrC0oKnEEwuoSaPGH1rTeVrxde270NLbUI6geOv_qGH0YSPncbYNq7eSR1mKrBW0UbH3NxB1rnWK1wmznOEaRANDQ3yal3wr602IynmInwQSNK2pgbB4tAqwtGHpF2iOINOwDaE2kwmDCuwwt15VQLDP_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین پکن رو ترک کرد
@withyashar</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/withyashar/11762" target="_blank">📅 18:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11761">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">طبق ادعای تایید نشده رسانه الحدث: احتمالاً توافق تهران و واشنگتن برای شکل دادن دور دیگه‌ای از مذاکرات، طی ساعات آینده نهایی می‌شه. این مذاکرات احتمالاً پس از پایان حج تو اسلام‌آباد برگزار می‌شه.
@withyashar</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11761" target="_blank">📅 18:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11760">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دونالد ترامپ دربارهٔ خودش:
شما در نهایت خواهید گفت: او بزرگ‌ترین رئیس‌جمهوری بود که تاکنون زندگی کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/withyashar/11760" target="_blank">📅 17:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11759">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ درباره ایران: الان خشم زیادی در ایران وجود دارد، چون مردم در شرایط بسیار بدی زندگی می‌کنند.
التهاب و ناآرامی زیادی به‌وجود آمده که تا این حد قبلاً ندیده بودیم.
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11759" target="_blank">📅 17:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11758">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خبرنگار: درباره جنگ ایران چی میگید؟
ترامپ: بذار اینجوری بگم، شما تو ویتنام 19 سال توی جنگ بودید، جنگ جهانی دوم 4 سال بودید؛ من 3 ماهه تو ایران درگیرم، خیلیاش هم آتش‌بس بوده. تو دوتا جنگ، ونزوئلا و اینجا، ما 13 نفر از دست دادیم، تو جنگ‌های دیگه صدها هزار نفر کشته دادید. ما عملاً ونزوئلا رو گرفتیم تقریباً هم ایران رو هم گرفتیم.
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11758" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11757">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دونالد ترامپ دربارهٔ ایران:
من هیچ عجله‌ای ندارم. همه می‌گویند: «انتخابات میان‌دوره‌ای.» من هیچ عجله‌ای ندارم.
@withyashar</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/withyashar/11757" target="_blank">📅 17:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11756">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرنگار: «آیا شما و بنیامین نتانیاهو دربارهٔ ایران هم‌نظر هستید؟»
دونالد ترامپ: «بله.»
«بی بی نتانیاهو پسر خیلی خوبی است»
@withyashar
😃
🤣</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/withyashar/11756" target="_blank">📅 17:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11755">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d428ef0134.mp4?token=bGh_lPAlthJo6feGuMhp178N_vIigQR53PN84oz4JfjzlHcczf66J4LMDVhV9mg9d2GRHk9dKWt46g2yAbjXyKtUMgA4Wpynp4Oa9jy_SEmIGJvbasx5mwAREX6Hlp-5NqF7Vj0B093ffIjy5QDN2h2poOOSazcYSlEvaaAtKxWKN7cKfDxudbUIyDeePOBx36-ioeV9my8fiM7oa8OO3tANZYHimWKwSZ5kCyUp86xpM6qZivsmB_ceE5BqtvFRlaVICTADJcG17BywjKTiYW8YV1KYbugnMHApnp7XRfP8g7sbPCZpiB3xqBSimjw3risX9cBbPKl7uNgPIelDbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d428ef0134.mp4?token=bGh_lPAlthJo6feGuMhp178N_vIigQR53PN84oz4JfjzlHcczf66J4LMDVhV9mg9d2GRHk9dKWt46g2yAbjXyKtUMgA4Wpynp4Oa9jy_SEmIGJvbasx5mwAREX6Hlp-5NqF7Vj0B093ffIjy5QDN2h2poOOSazcYSlEvaaAtKxWKN7cKfDxudbUIyDeePOBx36-ioeV9my8fiM7oa8OO3tANZYHimWKwSZ5kCyUp86xpM6qZivsmB_ceE5BqtvFRlaVICTADJcG17BywjKTiYW8YV1KYbugnMHApnp7XRfP8g7sbPCZpiB3xqBSimjw3risX9cBbPKl7uNgPIelDbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ :  الان میزان محبوبیت من در اسرائیل ۹۹ درصد است. من می‌توانم برای نخست‌وزیری نامزد شوم؛ شاید بعد از اینکه این کار را انجام دادم، به اسرائیل بروم و برای نخست‌وزیری نامزد شوم.
@withyashar</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/withyashar/11755" target="_blank">📅 17:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11753">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607ea22bcb.mp4?token=LCHu9tpySejpL-ktXKCDbE1jovbuKkxq7TXsZMEzacnzCiPfe3K8W1TRBM1T03E1bachSu7TdiwdDTYr2umnP6jlivIda97mo6RYKt6htICQ-3DOspwlXEXNCNb0cw4xHkmDFc_67CYxtxNBkwPTUAfjpVXCnY1OCyEbCEYebLVcoXLoj0urWLsUVwLNtn6MwRJ5B4VmwMe9eqrVMqz9WFvZ6Yr9aI6e-tz4FkZ4xb0sytB2O9iYVbiN-tMamslzEia7fNKfuNABTqeKUIbZIfEKCPe-RRYgFKylDU5e1zF8pSYK0qTzCfISTJEMfREMTbgYOmhDNrc4qs2x_Y4OcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607ea22bcb.mp4?token=LCHu9tpySejpL-ktXKCDbE1jovbuKkxq7TXsZMEzacnzCiPfe3K8W1TRBM1T03E1bachSu7TdiwdDTYr2umnP6jlivIda97mo6RYKt6htICQ-3DOspwlXEXNCNb0cw4xHkmDFc_67CYxtxNBkwPTUAfjpVXCnY1OCyEbCEYebLVcoXLoj0urWLsUVwLNtn6MwRJ5B4VmwMe9eqrVMqz9WFvZ6Yr9aI6e-tz4FkZ4xb0sytB2O9iYVbiN-tMamslzEia7fNKfuNABTqeKUIbZIfEKCPe-RRYgFKylDU5e1zF8pSYK0qTzCfISTJEMfREMTbgYOmhDNrc4qs2x_Y4OcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم تکرار میکنم نفرستید این ویدیو ها فیک هستند !!!
@withyashar
جدا از جعلی بودن روسیه الان برف ‌نیسن !
علی گدام مارکت بورو نیست یه عمری خودش خودشو نشسته ! حمام هم کس دیگه لیف زده !
😂</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/11753" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11752">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">قالیباف: آمریکا دوباره در جنگی بی‌پایان که در آن امکان پیروزی ندارد گیر خواهد افتاد
@withyashar</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/withyashar/11752" target="_blank">📅 16:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11751">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de5c69f230.mp4?token=JAKUqo_burdIPKp--m3cth_3EUa644I7iQ_sAod5wGu_dpJ0tc9ZHiyvmwDAp15NKmpU-BL7hgLiNQNfg62dDLaVr5oggNFQjmIxck-7zQRLg8RIG2hd-JuwZD6VViMyToOzZZSraru_uw3Lw16L1KjJnMWG92PAJpH3lZ_KP14WhRdFPIlUa7LFZdib_u6-e0dDg3RqQSpnY3Y8vwDnSXyar_B1hw9bQ458a-7C6-YwVCGnpqhge1Q-YMDpd3j40Wz2wBnEDb4qKOMe17_4YH0RjwO_ebMpVdYNPNja2H3gOjCs-0iP-0MEn9oh8lWies0B5n2jFgadeTtpbNE5EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de5c69f230.mp4?token=JAKUqo_burdIPKp--m3cth_3EUa644I7iQ_sAod5wGu_dpJ0tc9ZHiyvmwDAp15NKmpU-BL7hgLiNQNfg62dDLaVr5oggNFQjmIxck-7zQRLg8RIG2hd-JuwZD6VViMyToOzZZSraru_uw3Lw16L1KjJnMWG92PAJpH3lZ_KP14WhRdFPIlUa7LFZdib_u6-e0dDg3RqQSpnY3Y8vwDnSXyar_B1hw9bQ458a-7C6-YwVCGnpqhge1Q-YMDpd3j40Wz2wBnEDb4qKOMe17_4YH0RjwO_ebMpVdYNPNja2H3gOjCs-0iP-0MEn9oh8lWies0B5n2jFgadeTtpbNE5EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنها فیلم موجود از جعفر شفیع زاده
«در پشت پرده های انقلاب» عنوان کتاب خاطرات جعفر شفيع زاد، بچه قصاب قهدری‌جانی است که نخستین بار در سال ۲۰۰۰ در آلمان منتشر شد.
او یکی از اعضای بادی گارد خمينی بود که در سال ۵۶ در سوريه بدستور قطب زاده؛ ابراهيم يزدی؛ بنی صدر و.... دوره آموزش نظامی مخصوص و چريکی گذرانده و از زندان اصفهان و روستای قهدريجان به فرانسه و دمشق و ليبی (طرابلس) فرستاده میشود.
برای  اندکی ممکن است که سبک نگارش خاطرات شفیع زاده در کتاب «در پشت پرده های انقلاب» به صورت مستند نباشد و یا اینکه اسم افراد و یا مکانها بنا بر ملاحظاتی با آنچه که واقعا اتفاق افتاده باشد دقیقا همخوانی نداشته باشد. اما تجربیات، مدارک موجود و اطلاعاتی که بعد از انتشار این کتاب به دست آمد نشان داد که همه مطالب بیان شده در این کتاب بخصوص دخالت کشورها  در به پایان رساندن انقلاب ۵۷ و دستنشاندگی محافل اسلامی و رایطه شخص خمینی، کاملا واقعی است.
@withyashar</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/withyashar/11751" target="_blank">📅 16:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11750">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvOwOuWPqWL6oiwpz3bEN2Fw77A_bcb4vVrZDD7iZYqk5FQON8nMeaEcF7b_tsnUwgPDg7T3jctFTEgAUDxKkgIz4hnGp-qOhbaciAmrPdO0FYpCnURmZG5bQEmeVHBbEFcZCtrWtvFtXJvxslV9EyxYELi_KzwHKojn5s8yYTJk_AuWQOqYFCZSITeUV0zQC96rATQrBuOUmqJynOopYfJta7mi_oA_1f_zlklxFHjjMMd8ogff301MKl7Grk2alYZkaVP-uxODjetgsEIHjKPhJVKt20jrb0PiGENlQbEJhxGCeNYfROd3M0Ul26X7A_2BYeE4m0H6VAiJdmAblw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">poshte-pardehaye-enghelab (@withyashar).pdf</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/withyashar/11750" target="_blank">📅 16:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11749">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">العربیه: آمریکا به پاکستان اطلاع داده که در موضوع هسته‌ای و تنگه هرمز هیچ امتیازی نخواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/withyashar/11749" target="_blank">📅 15:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11748">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شبکه الحدث: جمهوری اسلامی و پاکستان در خصوص مذاکرات دچار اختلاف‌نظر شده‌اند
الحدث گزارش داد در دو هفته گذشته، همکاری میان حکومت ایران و پاکستان با چالش‌هایی روبه‌رو شده و فضای بی‌اعتمادی بر سطح هماهنگی‌های دو طرف سایه انداخته است.
این رسانه افزود میان تهران و اسلام‌آباد درباره کانال‌های مذاکره و محل برگزاری گفت‌وگوها اختلاف‌نظر وجود دارد.
بر اساس این گزارش، پاکستان از ایجاد کانال‌های ارتباطی جدید میان تهران و واشینگتن ابراز نارضایتی کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/11748" target="_blank">📅 15:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11747">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/11747" target="_blank">📅 15:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11746">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/11746" target="_blank">📅 15:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11743">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aX1vrhTxOMw5_jvQUXbm-42gM7842R-d9iLzZ0CCRFei3FOHfz6Xc0gumnDt6xfXoJ65Mz6CnZrt-LkxoOm9p_-dQyI0pYh_-shH7fVMWRYNyQCODdez6kfkHb-WWkgmgnNhbY4sFqvLBVFm7p44W2bk_KZgWKm6dp5t4Blj442v4lingZHDfyI4Dhk6vPaE2xxhv27rHRe-vM6JUSlcglGS_Jy7Z_KQgeuoKsp-gj-CEmSpM9YCd2ETEYdo6Tg5GrUgkWUPjtM2-fzgq905Q_bSYiJyjF36MqdtNcZ686qu76lNnkdB7t4kQGv9P5bvpfUX9PH249di2xY6-OAfyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xi92a_xJ3Iuv-SD_zttaaSxpcdz5oMGfkYHjJp3l0wMwr3w4lE6gZ_ozJXoFfyd4CEaFHngN0NVcb5V1UEmWyUNOA_-yI4QnVSgpGe4d8jXpVCUw8YBiW4kbRR6raeBlrb2HiTlbgNvBB3pSNW-8CpNWoZBFIjp_tDV549zjLWNYAgES5oTcUIDm8gHQd9i1i9inLz4lAzXSlHL2FMtESaoXvZXhA86JbNlr8X67EFx3gPYtrRnWk2Tgba0U2w2L3zv_8Gk5VTpwnGxNCnImn5MT5Mdm9t6KgaYFxW3omJmEuckxQWNM_YnZlZC6Zfkb-nchdPPNeCraHUilBSKi9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkvRor0_nSCflCSu7Z1W7-hbQor6LKyI7kZiwNVgePnFQdonAmeqHvVd6E2upG_INJOSX1CP3LBPcRJwme3IIsOrDE2YCjawgK4X9irqWyF815VmS0jkU1EIuTdRekPuMe9qkIfbfD5qXIY-ozhaoSvuN0-anK_uJsR54EmX3_z3-gE11yL3as_KrrTMSisNWWYE8Hcq_OfSN1EOckBIk5mhDqGRTQx83X0ZLmndJqjBYhX6fJ8apxX5rs_LyHl6hgD4xZwS42x19D0_CgRNtP76kcalhLwBmx8CuK3ScT4g-iSWds1tRuHHz_PuESibYR-C5kFQFsC94psV0-T1Kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فال حافظ محمد رضا پهلوی…
فلک به مردم نادان دهد زمام مراد
تو اهل فضلی و دانش همین گناهت بس
@withyashar
عکس اون روز هم به دقیق ترین حالت ممکن براتون بازسازی کردم
@withyashar</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11743" target="_blank">📅 15:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11742">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">من رفیق نیمه راه نیستم! مرسی از پیغام های زیباتون
😃
تازه خلیلی هم خوش مسافرتم اینو همه دوستام میدونن ، شما هم دیگه متوجه شدید
🤣
🙌🏾</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/11742" target="_blank">📅 14:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11741">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/11741" target="_blank">📅 14:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11740">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/withyashar/11740" target="_blank">📅 14:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11739">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11739" target="_blank">📅 14:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11738">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">گروسی: برای تضمین امنیت هسته‌ای به خلیج فارس سفر می‌کنم
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/11738" target="_blank">📅 13:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11737">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر کشور پاکستان عازم تهران شد
@withyashar</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/11737" target="_blank">📅 13:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11736">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/11736" target="_blank">📅 12:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11735">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKaoi-xiwcVv_VfTnTc98n_VKrU9_qsCx-_MNOcUG0DhH9wFo_OjEJse-n_zGDxF9Kb7PpxYg2Z6t4aon-xODvofHXpnzSuv_jnjDrO-sd5NM4oZle7xxC85rMJweLnLCrkVu-rFHdjurJ7qcAzdadV5QzS2J0jthUehwcf3QV4kKQQp96-PdwHLxDwuyVKDmErTaLCBDhWfOJJ0Whmp1KtRvkeioabSUcedEnB23TiWydpJ_kInEyDSys8wP6RVUzizXeKBkR2gWugrGdTTNHW8AH4t5KfjBlEvxqtYMISqeqON6aUWpcSthyePQUg58_nLlPKF4E8ivBvVEWPC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل: ترامپ و نتانیاهو دیشب تماس تلفنی طولانی داشتند که یک تماس محوری توصیف شده است
@withyashar</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/11735" target="_blank">📅 12:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11734">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ff90ab27a.mp4?token=QnuXCdkjl6hla6ewxaBgy8hBojZ4jEitvOpXTSSUHxtiEPHnBthWcLYHavo5IbX7sD-vYfPod24CMqmp5t8l9LDR07_aNAhYWsZLrs4UAdnK-gU84aeZmPwJy1BWR-zVTTqbyDCJBxdUVMjSAT-ecTzSjyXjRqey9_9TtOUB9HnEREsfjovJ_bsfKuV0bxyc-bn_HOVOF2lRpPWgY-Q4bB-Y1Bs0wnCQ7Tsj0krEqQJTiLONUmlllT1oaF_x379Lc7NitCxktGsT66MicsQHN5gIPpfLv2tHrbRQjEmXS3rhKhoU17q-sNRsI1LfRMem-LaIAGKysQG1cO8PlUagUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ff90ab27a.mp4?token=QnuXCdkjl6hla6ewxaBgy8hBojZ4jEitvOpXTSSUHxtiEPHnBthWcLYHavo5IbX7sD-vYfPod24CMqmp5t8l9LDR07_aNAhYWsZLrs4UAdnK-gU84aeZmPwJy1BWR-zVTTqbyDCJBxdUVMjSAT-ecTzSjyXjRqey9_9TtOUB9HnEREsfjovJ_bsfKuV0bxyc-bn_HOVOF2lRpPWgY-Q4bB-Y1Bs0wnCQ7Tsj0krEqQJTiLONUmlllT1oaF_x379Lc7NitCxktGsT66MicsQHN5gIPpfLv2tHrbRQjEmXS3rhKhoU17q-sNRsI1LfRMem-LaIAGKysQG1cO8PlUagUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم عروسی جان فداها: عروس رفته تنگه هرمز گل بچینه!
@withyashar
😂
جلبک دریایی
🪸</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/11734" target="_blank">📅 12:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11733">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دو نفتکش چینی پس از دو ماه معطلی در خلیج فارس، روز چهارشنبه از تنگه هرمز عبور کردند.
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/11733" target="_blank">📅 12:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11732">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">@withyashar_‎⁨پاسخ_به_تاریخ_محمدرضا_شاه_پهلوی⁩.pdf</div>
  <div class="tg-doc-extra">8.3 MB</div>
</div>
<a href="https://t.me/withyashar/11732" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نسخه فارسی و بدون سانسور کتاب "پاسخ به تاریخ" نوشته‌ی، محمدرضا شاه پهلوی
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/11732" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11731">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKsewOl3zmcOeNiCEmdvgXIzeE9UBN3TZODMOK7gn8kvM4IKuF56jirzHY9avv3uYC4RIqYU3XwUKd0dWT19jwX4w6XI9aHoNm_IZa1pnzAD_ZZqr6AJt4N1bsFBvtmfLrrrPwP4LUzv6sOiajuAjWIH-7ba7NiE1RF7rKR5EnoV2DfBsv8virXdkUTVsVuUJ3tI_CtBDS-U6jY6EkWO6IZvk-UrWCeJYhA9DgOno-mcKfHTU1OgZJnm8UvbHE39P-tALQRmCXE3Xzr8nILRds7QeFT-hiCvZJkCGqObEjDWSR3HSzjkq4oDCLYY_LaTGLC561xqZcxaCz154XLiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار نشون می‌ده در ۳ ماه گذشته یک پاکسازی طبقاتی دیجیتال در ایران رخ داده. در این مدت سهم اندروید از ترافیک اینترنت ۲۵٪ افت و آیفون ۱۸۰٪ رشد داشته. این به معنی خروج میلیون‌ها کاربر طبقه متوسط و پایین از فضای آنلاینه. اونی که آیفون داره از پس هزینه کانفیگ یا اینترنت پرو برمیاد، اونی که نداره، اونقدر دغدغه مالی مختلف داره که عطای اینترنت رو به لقاش می‌بخشه
@withyashar</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/withyashar/11731" target="_blank">📅 11:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11730">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وزیر نیروهای مسلح فرانسه اعلام کرد این کشور از وجود مین‌های دریایی در تنگه هرمز اطمینان ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/11730" target="_blank">📅 11:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11729">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مقامات کره جنوبی تأیید کردند نفتکش «یونیورسال وینر» این کشور که حامل دو میلیون بشکه نفت از کویت است، از تنگه هرمز عبور کرد.
@withyashar</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/withyashar/11729" target="_blank">📅 11:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11728">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">وزارت خارجه روسیه اعلام کرد ایران از «پیمان منع گسترش سلاح‌های هسته‌ای» (ان‌پی‌تی) خارج نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/11728" target="_blank">📅 11:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11727">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">۳پا تروریستی : جنگ منطقه‌ای که وعده داده شده بود با تکرار تجاوز، به فراتر از منطقه کشیده خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/withyashar/11727" target="_blank">📅 11:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11726">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شاهزاده رضا پهلوی:
با دولت ترامپ و اعضای کنگره آمریکا در تماس هستم.
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/11726" target="_blank">📅 10:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11725">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYYZahmGap6Dv0CWnOxp1PXXek3wxfBQk2IbCmTwlpJm5mIsEl-kfTuHdRR54NecD__DkV4DjZssixoZnm4Rq2QRQwC-jIvftnfzraAz9ACqGVZ6jd7w0OL_kJEqoJhnsEkSAst-_oE1jN3RLGMQbn5Sb457a3pXDA-QghN5-kE2gEsFw-DPeZ8n4P8G82HgvpR51GaMpxXVVDfvsLXcrfgJSoS9B59cxJ3iOnxL2AGW0j0BFNhbcsa5su_QZzseIzgLEG24yh8j8_p5QRhxxCLFGDm9Dpp21sXvXmYdJkraCtpm3XsDpgYUsWw5ngHQLs06JnR9OueYy0gBEyn07w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رادار کلادفلر خبر از افزایش ترافیک‌ اینترنت ایران می‌دهد؛
شروعی برای موج قوی تر فیلترینگ؟
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/11725" target="_blank">📅 10:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11724">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فایننشال تایمز:  شرکت سرمایه‌گذاری خطر پذیر ترامپ که در حوزه هوش مصنوعی، فناوری دفاعی و املاک فعالیت می‌کند، در حدود یک سال از ۲۰۰ میلیون دلار به ۳.۵ میلیارد دلار دارایی رسید؛ یعنی جهشی ۱۷ برابری
@withyashar</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/withyashar/11724" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11723">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2248478d.mp4?token=semPElAGw-5m37C_DHp9ENvKhiJutnf6SzXDvDpIgTUNDuVTtV8390BcHcuC3OXN8kzUb9K0WIuTG_UqBq-jjzjy8Q7aHUA3ZgFtjBYb4jRYnLvVXePWGMKdwbTfM9OqXjQ4r2x9hjofey_2cfdrZb2JhFoeCC6_9fIG-aZaDoG05qzLmX8SJjDbPXgDX06JEaswnwDWHFS102Myupl0lD0uIWxb45PwxXouNkYTcW_EJ3BlKVamve1Q18rWA1u2s3SCQOJe09rBSBv4qGsDbWfdqKRr1YXj3JWvN45gagydd4Db3Nm5SiXUT6wTGQJKivlm4zfUq3d51Rp0NthYPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2248478d.mp4?token=semPElAGw-5m37C_DHp9ENvKhiJutnf6SzXDvDpIgTUNDuVTtV8390BcHcuC3OXN8kzUb9K0WIuTG_UqBq-jjzjy8Q7aHUA3ZgFtjBYb4jRYnLvVXePWGMKdwbTfM9OqXjQ4r2x9hjofey_2cfdrZb2JhFoeCC6_9fIG-aZaDoG05qzLmX8SJjDbPXgDX06JEaswnwDWHFS102Myupl0lD0uIWxb45PwxXouNkYTcW_EJ3BlKVamve1Q18rWA1u2s3SCQOJe09rBSBv4qGsDbWfdqKRr1YXj3JWvN45gagydd4Db3Nm5SiXUT6wTGQJKivlm4zfUq3d51Rp0NthYPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ بعد از زدن حرفهای همیشگی مانند رهبرشان مرده، نیروی نظامی ندارند و سلاح هستهی نباید داشته باشند
پس از سخنرانی ملانیا ترامپ در کاخ سفید، گفت:  عجب سخنرانی فوق‌العاده‌ای بود، من هیچوقت دوس ندارم بعد از بانوی اول آمریکا صحبت کنم، چون باعث میشه خیلی خوب به نظر نرسم.
@withyashar</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/11723" target="_blank">📅 10:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11722">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b141755bd2.mp4?token=qSrC3Yd-rvNzPuEsUc99KDpgCVoJCSPZUyhl5jZ2ZGv5qDjYe1zAWERJxHG-nRHytHwp8Zv2F3Im7RfzEuJSiH-ESXA_4WwZwl6qEEjFdKf4zwZyvFq0OkBaTVdVFK3x76jVEWKWxRO6c07jTUgwtaojko-yImNh-MbOgsNWWVIcz-k3eVnh1dhzAlsUV2IBfxdrXoYrktebmCNCWPYLOuxBMW31GObM-RXSy1jgTF92jVoF19ClEIgravVAXurOH80lNZw7qO-IGgdf81aI7dMRupopAKA31RMrJxgO2h_WGTXDqjRZ5teSEMXiAIGtJp28mLtt0drHuJyl2hOS1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b141755bd2.mp4?token=qSrC3Yd-rvNzPuEsUc99KDpgCVoJCSPZUyhl5jZ2ZGv5qDjYe1zAWERJxHG-nRHytHwp8Zv2F3Im7RfzEuJSiH-ESXA_4WwZwl6qEEjFdKf4zwZyvFq0OkBaTVdVFK3x76jVEWKWxRO6c07jTUgwtaojko-yImNh-MbOgsNWWVIcz-k3eVnh1dhzAlsUV2IBfxdrXoYrktebmCNCWPYLOuxBMW31GObM-RXSy1jgTF92jVoF19ClEIgravVAXurOH80lNZw7qO-IGgdf81aI7dMRupopAKA31RMrJxgO2h_WGTXDqjRZ5teSEMXiAIGtJp28mLtt0drHuJyl2hOS1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین و شی بیانیۀ مشترک تعمیق روابط چین و روسیه را امضا کردند
شی: جهان به دلیل اقدامات یک‌جانبه و سلطه‌طلبانه دیگر پایدار نیست، بنابراین ما به دنبال یک نظام جهانی جدید هستیم.
پوتین: همکاری ما در امور سیاست خارجی یکی از عوامل اصلی ثبات در صحنه بین‌المللی است.
در شرایط پرتنش فعلی در صحنه بین‌المللی، هماهنگی نزدیک ما به ویژه مورد نیاز است.
@withyashar</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/withyashar/11722" target="_blank">📅 10:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11721">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">فراخوان دادن هرکی با سیدعلی خاطره داشته بیاد تعريف کنه می‌خوایم سریال بسازیم
@withyashar
😬
😂</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/withyashar/11721" target="_blank">📅 10:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11720">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b18d34d22.mp4?token=gvaw1WgeYvlAuS3P2KWxAabWaSOYyX_4bttkERBEPMiL_pMAcspu9vy_a6dgxELYzMQkzaWIRKOvnBYpJUr1ScIgjMNadsChrqCwmKSdIIrHi9xNbbAc_V7fiFVvABNOm1PHj5TKs6rZafKTpyefdbqT_cj-HIfUrDFEoZw-Uwt4t685SDq_8uHc4lhHleUUGawfXtsIpcVWSVprUT501YaBdoEqvgbbR4M6aqikLFaoLp5zuKgLPHQeol7iD2FZjEwCGzH0691Zbghr8ITOaWc029kUTT6byqBQYTYFcSVHFI9Ek12shDzsEL8mRlqOQCn3vArDoSntrElEkFJgXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b18d34d22.mp4?token=gvaw1WgeYvlAuS3P2KWxAabWaSOYyX_4bttkERBEPMiL_pMAcspu9vy_a6dgxELYzMQkzaWIRKOvnBYpJUr1ScIgjMNadsChrqCwmKSdIIrHi9xNbbAc_V7fiFVvABNOm1PHj5TKs6rZafKTpyefdbqT_cj-HIfUrDFEoZw-Uwt4t685SDq_8uHc4lhHleUUGawfXtsIpcVWSVprUT501YaBdoEqvgbbR4M6aqikLFaoLp5zuKgLPHQeol7iD2FZjEwCGzH0691Zbghr8ITOaWc029kUTT6byqBQYTYFcSVHFI9Ek12shDzsEL8mRlqOQCn3vArDoSntrElEkFJgXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در ایران کار فوق‌العاده‌ای انجام دادیم؛ فکر میکنم خیلی زود این کار تمام بشه و آنها سلاح هسته‌ای نخواهند داشت؛ امیدوارم این کار رو به روشی بسیار خوب انجام بدیم.
@withyashar</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/withyashar/11720" target="_blank">📅 10:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11718">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfef4f2369.mp4?token=Fw27feF53PnyTMk2OYoP9pvvo75BTljSKSgjTZC1Ob8CSPzhWW0TuGXob2lp_JFnO47d4Skq7ag53CJK0fk5DaZXxSLBHR32IgutoRlLFuhNldxghBKxx6hAeSK-A9QTvOyckfNW99HOJNau1fZbvgCL3X89xxRPYjtq2Bu9k5xSneOQMGxFPZM-7BfVyMudluskSWqIPabx6wkTbcppGIvPR2eT6kSl9S3AbWqX6IGwUscn3wqLCuiazMoD3rN-DTl_C75FkOuVRjGPY8OohbgudAdUoNgIseGqf1Ns5wnv_wfgFct4Dwu4SOUoIaWL-d42R3lPBiuU0Ga4ESh2oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfef4f2369.mp4?token=Fw27feF53PnyTMk2OYoP9pvvo75BTljSKSgjTZC1Ob8CSPzhWW0TuGXob2lp_JFnO47d4Skq7ag53CJK0fk5DaZXxSLBHR32IgutoRlLFuhNldxghBKxx6hAeSK-A9QTvOyckfNW99HOJNau1fZbvgCL3X89xxRPYjtq2Bu9k5xSneOQMGxFPZM-7BfVyMudluskSWqIPabx6wkTbcppGIvPR2eT6kSl9S3AbWqX6IGwUscn3wqLCuiazMoD3rN-DTl_C75FkOuVRjGPY8OohbgudAdUoNgIseGqf1Ns5wnv_wfgFct4Dwu4SOUoIaWL-d42R3lPBiuU0Ga4ESh2oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شی از پوتین در پکن چین
@withyashar</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/11718" target="_blank">📅 10:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11717">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">طبق گزارش نیویورک تایمز، آمریکا و اسرائیل پیش از جنگ با ایران درباره طرحی برای نصب محمود احمدی‌نژاد، رئیس‌جمهور سابق ایران، به عنوان رهبر جدید کشور گفتگو کردند.
گفته می‌شود احمدی‌نژاد در این طرح مشورت شده بود، اما پس از زخمی شدنش در حمله اسرائیل به منزلش در تهران در روز آغاز جنگ، این طرح از هم پاشید. مقامات آمریکایی گفتند این حمله با هدف آزاد کردن او از حصر خانگی انجام شده بود.
احمدی‌نژاد زنده ماند اما پس از آن از تلاش برای تغییر رژیم ناامید شد و از آن زمان تاکنون در انظار عمومی دیده نشده و محل اقامتش نامعلوم است.
@withyashar</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/withyashar/11717" target="_blank">📅 09:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11716">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مرضیه حسینی، خبرنگار اینترنشنال:
منبع مطلع در کنگره به من گفت فردا شب یا پنجشنبه شب عملیات نظامی آمریکا علیه ایران آغاز میشه.
حملات برای یک عملیات دو سه روزه متمرکز است و به مراکزی با هدف بازگشایی تنگه هرمز انجام میشه.
@withyashar
یاشار : امیدوارم خبر زرد نباشه</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/11716" target="_blank">📅 02:17 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11715">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/withyashar/11715" target="_blank">📅 01:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11714">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/11714" target="_blank">📅 01:54 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11713">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a73b04b90.mp4?token=joUvizSuvfJp0cCkFwI9qG62reIpiFKrA2vvhmIimQCtGCeLttGa8swYRDv4nz8Y--jNgtUMdwlv1A0xfbE0rVXHett79egSRMngCAVTyzM7O8ZNmsEWV0WyOA6Lww9UfaH2R2Eomz8Njcn35YFqvN7p0VCP7QuGpuuk386HHsdvpBWQYMRzTXovkPOCmKUbLXQn5w3WJLsKqnZVsJKMUQ9Yn06uUMbflRGPCRtliVR4W7-r6iYa8nnQIB6ImTQDYmedW-sI6GdGKiZajZwAPy5llovtb6mKHFKqCQF0lI0rrnxvrwsomQMJaQ8B0wCHuOzNj_h1XucK9Ex_tevfvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a73b04b90.mp4?token=joUvizSuvfJp0cCkFwI9qG62reIpiFKrA2vvhmIimQCtGCeLttGa8swYRDv4nz8Y--jNgtUMdwlv1A0xfbE0rVXHett79egSRMngCAVTyzM7O8ZNmsEWV0WyOA6Lww9UfaH2R2Eomz8Njcn35YFqvN7p0VCP7QuGpuuk386HHsdvpBWQYMRzTXovkPOCmKUbLXQn5w3WJLsKqnZVsJKMUQ9Yn06uUMbflRGPCRtliVR4W7-r6iYa8nnQIB6ImTQDYmedW-sI6GdGKiZajZwAPy5llovtb6mKHFKqCQF0lI0rrnxvrwsomQMJaQ8B0wCHuOzNj_h1XucK9Ex_tevfvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/11713" target="_blank">📅 01:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11712">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/11712" target="_blank">📅 01:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11711">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromP</strong></div>
<div class="tg-text">چه طوفانی میاد تهران
پشمام ریخته</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/11711" target="_blank">📅 01:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11710">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سی‌بی‌اس: این طرح که توسط «تیم کین»، سناتور دموکرات ویرجینیا، ارائه شده، ترامپ را موظف می‌کند که «نیروهای مسلح ایالات متحده را از هرگونه مخاصمه در داخل یا علیه ایران خارج کند، مگر اینکه به‌وضوح با اعلام جنگ یا مجوز مشخصی برای استفاده از نیروی نظامی مجاز شده باشد.»
این رأی فقط گامی اولیه در سنا محسوب می‌شود. و حتی اگر هر دو مجلس کنگره این قطعنامه را تصویب کنند، انتظار می‌رود که رئیس‌جمهور آن را وتو کند.
اما دموکرات‌ها می‌گویند این اقدام حائز اهمیت خواهدبود و می‌تواند طرز فکر رئیس‌جمهور را در جنگ تغییر دهد.
@withyashar</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/withyashar/11710" target="_blank">📅 01:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11709">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پس از ۷ تلاش ناموفق، سنای آمریکا طرحی را تصویب کرد که مصوبه کنگره را برای ادامه حملات نظامی به ایران الزامی می‌کند.
سنا با رأی ۵۰ به ۴۷، اکنون به طور رسمی «قطعنامه اختیارات جنگ در ایران» را پیش برد.
@withyashar
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/11709" target="_blank">📅 01:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11708">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/withyashar/11708" target="_blank">📅 01:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11707">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">میانجی‌های منطقه‌ای و مقامات آمریکایی:
موضع ایران در مذاکرات با آمریکا عمدتاً بدون تغییر نسبت به پیشنهادات قبلی باقی مانده.
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11707" target="_blank">📅 01:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11706">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/11706" target="_blank">📅 01:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11705">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/11705" target="_blank">📅 01:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11704">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ در تروث : این یکی از فاجعه‌های بزرگ دوران ریاست‌جمهوری بایدن بود؛ دوره‌ای که پر از بحران و فاجعه بود، از اینکه اجازه داد بقیهٔ جهان زندان‌ها و تیمارستان‌های خود را خالی کنند و افرادشان را به کشور بزرگ ما سرازیر کنند، تا تسلیم شدن در افغانستان
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/11704" target="_blank">📅 01:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11703">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/11703" target="_blank">📅 01:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11702">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سناتور لیندسی گراهام ؛«من امیدوارم و انتظار دارم که پس از ماه‌ها مذاکره با ایرانی‌ها، دولت ترامپ هرگونه تلاش ایران برای به‌تعویق انداختن دوباره مذاکرات را رد کند. این رژیم ماه‌ها فرصت داشته تا به یک توافق برسد، اما به نظر من روشن است که در حال بازی دادن طرف مقابل است.
ترجیح من دستیابی به یک راه‌حل دیپلماتیک است، اما قدیمی‌ترین ترفند ایران در این‌گونه مذاکرات، تعویق، تعویق و باز هم تعویق است.
در مورد هر توافق احتمالی نیز، منتظر هستم تا آن را در سنای آمریکا بررسی کنم.»
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11702" target="_blank">📅 00:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11701">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اتاق جنگ با شما : عزیزم، ممکنه اون انفجار قارچی چند روز پیش در اسرائیل، تست یه بمب برای زدن اهداف عمیق و مخفی ایران بوده باشه؟</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/11701" target="_blank">📅 00:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11700">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اتاق جنگ با شما : عزیزم، ممکنه اون انفجار قارچی چند روز پیش در اسرائیل، تست یه بمب برای زدن اهداف عمیق و مخفی ایران بوده باشه؟</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/11700" target="_blank">📅 00:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11699">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/11699" target="_blank">📅 23:54 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11698">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA</strong></div>
<div class="tg-text">جای یه b2 خشکل روی میزت خالیه
❤️</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/11698" target="_blank">📅 23:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11697">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/11697" target="_blank">📅 23:51 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11696">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اینم پست جدید کارای اداریش رو انجام بدید
😍
🔥
💥
🙌🏾
بمبه
https://www.instagram.com/reel/DYiHl04xutP/?igsh=MWZhNHllczYzNGtvaA==
⁨ اتاق جنگ با یاشار : طوفان ، رهگیری هواپیمای E-2D Advanced Hawkey ناو هواپیمابر آبی خاکی USS BOXER LHD4
و آب و هوای منطقه برای حمله</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/11696" target="_blank">📅 23:45 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11695">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tI17jYqWEHUFID1lGVsA8a7Gc50Y_l8LVM2xM23u_reYDgmyFXKN7cS8UcduWQAQDBTQ-2X5WrMz-Y1Ml_sKjKvOue6wS7CGOsVu9AhZ7aWGM_p_EAYSR38HSx0X4gua4jMlRfFt-u3a1njcmsLcUfWSOf6vhKcUZX2Kh_kHhZQ9DjhGyhuiEgacJDjpjETqS_lsWnvKlY2DXHAmDxbt9j8NKPorifjxB62w9-KSty2tf7Pa3Om12sfclh1p2O2W8qq12BQiFviKPmDWjPoOBCv-Sv44BlpSG0hYXhiIGHOm70vHvKWbJ-0-a-FMEPBIGjPmrLYRY5P1wfbBhEuCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوستر
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/11695" target="_blank">📅 23:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11694">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">برد کوپر: مردم ایران مخصوصا کودکان به هیچ عنوان دشمن و هدف ما نیستند، طبق هیچ پروتکلی هدف قرار دادن غیرنظامیان قابل توجیه نیست، سپاه پاسداران دشمن ماست
@withyashar</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/11694" target="_blank">📅 23:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11693">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/11693" target="_blank">📅 23:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11692">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آی 24 نیوز: مقامات اسرائیلی به این باورن که ترامپ با وجود سیگنال‌های متناقض و حرفای عمومی 24 ساعت اخیر، باز هم به حمله به ایران ادامه میده.
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11692" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11691">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فرماندهی مرکزی ایالات متحده: 88 کشتی را در جریان محاصره دریایی ایران مجبور به تغییر مسیر کردیم. @withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/11691" target="_blank">📅 22:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-11690">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">معاون ترامپ ، جی دی ونس :
من 41 سال سن دارم و تو این سال ها همش دیدم رسانه های اروپایی مثل جیرجیرک دارن ایراد میگیرن از امریکا
اگه میخوایید از ترامپ ایراد بگیرید اول یک نگاه به خودتون و اینده داغون و خرابتون بندازید بعد راجب ما نظر بدید
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/11690" target="_blank">📅 22:01 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
