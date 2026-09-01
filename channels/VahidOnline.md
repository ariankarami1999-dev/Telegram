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
<img src="https://cdn1.telesco.pe/file/lpY-ME0Mc0Emf0IIp9JGQz_sjZcxQ3Cy5hDTkskn7j-3EDKyAuwopNDbn0Mn_TYsmfygG5AIC4vrQa1fzSmajUXjmc6EJ8KfVBFkVoNV9pi228104EWKBB3z8T_AX-vGYiP5ylJSDcI-EQQ7XdUBL2ygOmEovjpEOMeNLr8O9soBAmoQVD-sMUxPT_vdHOIFsDSBOfEc23ntHLEkV7dzn1jkBVRLCadR-3lhDPlgNRKOY_OE1aEw-BlKp70FixRiTg3RiqmNYkCbDzKHcfsveMTSmFHSFXS0kY7WdYIu_JIOK0J09t-3Cd3Y7q-Mg1TKitRDj3ABLtc5fW2mM70SvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.41M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پیام مهم:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن.اینجا بعضی از چیزهایی که می‌خواستم ببینم رو همون‌جورکه می‌خواستم به خودم نشون داده بشن می‌گذارم.به لطف حمایت‌های ماهانهvhdo.nl/patreonو گاهانهvhdo.nl/paypalممنونم</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 01:22:27</div>
<hr>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=eH7k1yRL7_HvqKFGgOh9pUEbPfvZAIQ5Q9ULZpWw3eUrji8A6dJrtjeiBWYnauGztbuU2QecZo8rlFsWgHoZg02kvLGaCKb_P6GdHfKZBWNyDLAjxlG3fCT3zxnLHV_FH5-8HhRovZKmcpY2jabzOxJvVtZEop7X4sYjpeJAjGUrKu9M8T7_GEPErrOrylhamDV5J2inuqd-H_dyUxduV5cHZ8h7XkeRjkZdmhngbRrizfZXLrFuYnVm2_TXpK4qt0ppfg95ctz_-p57EqKPLTDZ-2mxnOSHgSR_9XrmP3FcgoOFIkJZo81Y_gXWzNCKW93d5tXUpHF71_117bkhSw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c60b2185fb.mp4?token=eH7k1yRL7_HvqKFGgOh9pUEbPfvZAIQ5Q9ULZpWw3eUrji8A6dJrtjeiBWYnauGztbuU2QecZo8rlFsWgHoZg02kvLGaCKb_P6GdHfKZBWNyDLAjxlG3fCT3zxnLHV_FH5-8HhRovZKmcpY2jabzOxJvVtZEop7X4sYjpeJAjGUrKu9M8T7_GEPErrOrylhamDV5J2inuqd-H_dyUxduV5cHZ8h7XkeRjkZdmhngbRrizfZXLrFuYnVm2_TXpK4qt0ppfg95ctz_-p57EqKPLTDZ-2mxnOSHgSR_9XrmP3FcgoOFIkJZo81Y_gXWzNCKW93d5tXUpHF71_117bkhSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که نگرانی خواب از چشمان  شهروندان ولایی و قاتل‌پرور کشور ربوده و شهروندان جلایی  آماده میشن که بگن چرخه خشونت داره چیز میشه، منابع حکومتی:
تصادف بوده، عمدی نبوده، راننده حالت عادی نداشته‌.
پلیس راهور: یک دستگاه هیوندای با سرعت بالا با یک دستگاه چانگان در مسیر موازی برخورد کرده که در پی این برخورد تعادل خودرو بر هم خورده و با جمعیتی که در حمایت از نظام و نیروهای مسلح در حاشیه خیابان حضور داشتند، برخورد می‌کند
راننده حالت عادی نداشته و پس از برخورد با بشکه‌ها و علائم ترافیکی، با جمعیت برخورد می‌کند و در نتیجه این حادثه تعدادی از شهروندان فوت می‌کنند و برخی نیز مصدوم می شوند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/VahidOnline/78173" target="_blank">📅 01:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=jRiy1BhfzB8PFKrA2Ut3hurTxRLz69no2U4cmjjdcLsRcgXYvyfIWuHFPCLnB-B7ueDl9B0QoKKlUiWjuFhxMf5fs-77WurnpIjRk8ywk02-f-pnIe5bDI1hnO7i1TCZfp1AxokqmJxjJaGkorNnft6Jb4lRVG4uM6KjRJkHXehNERqnBk6fEC5FL3J-aZ0zBbsrnuJ6Fw1cSN5JG6JVrKR2nhooYQvqm1zYG8-n6mGnaTZjt0mNpbnFmjOtm7K26T258EgOXE3WkvxLqvHQgs3uUk41SEaAbc5Jv83c_L3QMbRXwyC-EKAyb9AxhWM-ZMSgRG6QryNBIQ2sg2mWEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccb435b5a8.mp4?token=jRiy1BhfzB8PFKrA2Ut3hurTxRLz69no2U4cmjjdcLsRcgXYvyfIWuHFPCLnB-B7ueDl9B0QoKKlUiWjuFhxMf5fs-77WurnpIjRk8ywk02-f-pnIe5bDI1hnO7i1TCZfp1AxokqmJxjJaGkorNnft6Jb4lRVG4uM6KjRJkHXehNERqnBk6fEC5FL3J-aZ0zBbsrnuJ6Fw1cSN5JG6JVrKR2nhooYQvqm1zYG8-n6mGnaTZjt0mNpbnFmjOtm7K26T258EgOXE3WkvxLqvHQgs3uUk41SEaAbc5Jv83c_L3QMbRXwyC-EKAyb9AxhWM-ZMSgRG6QryNBIQ2sg2mWEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پیکر بی‌جان
ویدیوهای منتشر شده با شرح: یکی در
#مشهد
با خودرو کوبیده به تجمع بسیجیان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 227K · <a href="https://t.me/VahidOnline/78170" target="_blank">📅 00:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromILIA HASHEMI</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BRx63rH-4ad-6jGoZdp5BSitCo0b-vFKDGRBXQX5v880og12F4_4xKoa-HsZBLiomSXq9Q7mrhLdKo8ZgeTPIIMuau5OMbhHClzur5eaUxb2BVNbClR-_ehfFa9xlo-FM0UsyCSFpt2ZfN8Drk5kUU_8-nWNyZ96cm2jCfLqrugO55Mv4STzAhuwxYDurAwPmYa1zHdxkeZQP_w31jpgzJTrLdADbh4gn4QrpI8RauF8xOMxgcJoWQaTnJ1rxtZzh6a_VFMAS2tXGRHcR6rUB_ZEHLjE5gwR3AcfU6U7SpskUvesJVRFc1IYOorbY25Z5Syh0s3OusGO4k7VwKHolA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NVR3K6o83gyPnM6jVDaa8AOeUdqnH94ky-Sq7mEId0vks77FQZHdM-4_oskX8cqD9FcqoFVzLN5HeicrA75Sht0_QO1giRZIe8sf-FQ69odRRNmEkregH972-1YJ91r8wM9dazWiPqnGRqg5SflCfIfyvfP9-TZw189GYeA2Hrk3rUYzxgilt0Q71Ks_UciMoxWIeouSLpJaR25dtoOq8cEo7TcwOKOaJ0eOh5dIG7wk8R9ppMYKD-_uDpCKdUzATiJzx_hAl3PlxX01Z1yATlavwTMX4m9PopaA0AzSK5-pP-DHIZiVz4drnyDJgugPQoEGTedVIwG5uO-O0ZaboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت دکل مخابراتی کوهستک که در منطقه مسکونی واقع شده بود.
@iliaen</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/78168" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG_5RLFU6gjaNETkdFDWx143wUxyJa5cPvDuG3icgPIuQz9KegBE44nukDYyQD8zz4v4t-1m_GdpsRwiaJ0mzSY30tdx-3WrRoLCXEXZAsSPffEbbAZ5sHm3gTV6LlMRa16_azspBdFAwr6PLxf0MzJ5Q4FndGaygPGXuRUJ1STyknGThLKRNVeHx68eiIEvUvF3Leo4cyz-V55AlR6YLKKIIQGj4hpwDcESILhY8N-2MA7JJpFDuwcOffkTP6DwXPM0wKH1e4LrZlCAxIFyVNdzLr2VkHGVjMtJYFnj4bN2IlcD2Cp0sZHhixMvdOPwv09LeIuO1l2cBZcdhUHV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احمد نفیسی، معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان، اعلام کرد در یکی از حملات آمریکا، یک منزل مسکونی در منطقه کوهستک از توابع شهرستان سیریک که محل برگزاری یک مراسم عروسی بود، هدف قرار گرفت.
نفیسی در گفتگو با صداوسیما گفت بر اساس آخرین گزارش‌ها، در این حمله دو نفر کشته و بیش از ۲۰ نفر زخمی شده‌اند.
@
VahidOOnLine
در پیام‌هایی که من دریافت کرده بودم نوشتند هدف حمله یک دکل مخابراتی بوده و شهروندانی در اون حمله کشته یا زخمی شدند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 284K · <a href="https://t.me/VahidOnline/78167" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=Oa7y_j0lg9YP5x9Ev0vqqr9dMIp-Lw9fy0vKZbQh7HG-EObsd5lqdrMi2jpVcfIBWVGxWjaaFeE3qiZIeMbfBGzsUqbNGC2xgoCzLbldIZZgLc0ROsiWjO5kbMQ7RqdxQBnuoTCLV7lVl4XiTSXoJ0jDtGiE4tvO7hRVJz8eAo5bW0O4vGMePdjCuJEPwxE_2o-Pr89P-Yh-EdVeIo1iX8jM6Rug3yfU5YfseQIJQ91-gNdLCwNjuWLCb6YwFYmAoNXYADd3_n9-g524S9DnplJr-QXYRePvKtCrhxRkaL6Fe_kx8Mj6-tQrWSf0sgWAHc0yItvwKCk4oiz2nspgTw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/333da2f1a5.mp4?token=Oa7y_j0lg9YP5x9Ev0vqqr9dMIp-Lw9fy0vKZbQh7HG-EObsd5lqdrMi2jpVcfIBWVGxWjaaFeE3qiZIeMbfBGzsUqbNGC2xgoCzLbldIZZgLc0ROsiWjO5kbMQ7RqdxQBnuoTCLV7lVl4XiTSXoJ0jDtGiE4tvO7hRVJz8eAo5bW0O4vGMePdjCuJEPwxE_2o-Pr89P-Yh-EdVeIo1iX8jM6Rug3yfU5YfseQIJQ91-gNdLCwNjuWLCb6YwFYmAoNXYADd3_n9-g524S9DnplJr-QXYRePvKtCrhxRkaL6Fe_kx8Mj6-tQrWSf0sgWAHc0yItvwKCk4oiz2nspgTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از بیدگنه
سلام همین الان از بیدگنه موشک زدن
سلام از فردیس موشک فرستادن
سلام وحیدجان
ساعت ۲۳:۱۳ از سمت جنوب مهرشهر کرج صدای بلند شدن موشک میاد.
سلام الان از بیدگنه موشک زدن
از کرج موشک زدن چندتا
از بیدگنه ملارد بود احتمالا
درود همین الان صدای بلند شدن موشک از فردیس کرج اومد
همین الا از ملارد بیدگنه موشک شلیک شد
همین الان از بیدگنه چندتا موشک شلیک کرد
سلام از ملارد موشک زدن ساعت ۱۱:۱۲
+ ده‌ها پیام مشابه دیگر از این منطقه پرجمعیت که نمی‌رسم بخونم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78166" target="_blank">📅 23:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پیام‌های دریافتی:
سلام همین الان از کرمانشاه موشک زدن ۱۱و۰۷ دقیقه
داداش کرمانشاه پردیس دقیقا همین الان صدا اومد
همین الان از کرمانشاه موشک پرتاب کردن
صدا انفجار شدید کرمانشاه الان
وحید همین الان از کرمانشاه موشک فرستادن ۲۳:۰۸
کرمانشاه الان موشک زدن
کرمانشاه صدا جنگنده میاد وحشتناک [صدای پرتاب موشک با جنگنده زیاد اشتباه گرفته میشن.]
10:08 کرمانشاه موشک رفت
همین الان از کرمانشاه موشک فرستاد ...
سلام وقت بخیر الان هم از کرمانشاه صدای شبیه پرتاب موشک اومد ۲۳:۱۰
کرمانشاه دارن موشک میزنن، هنوز ادامه داره ۲۳:۱۱
موج دوم موشک از کرمانشاه ۲۳.۱۲
آپدیت:
پیام‌های کرمانشاه تا پنج تا موشک ادامه داشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78165" target="_blank">📅 23:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پیام‌های دریافتی:
الان موشک از،یزد زدن
از یزد موشک زدن الان
سلام وحید جان
همین الان از یزد موشک بلند شد
همین الان از یزد موشک زدن
وحید یزد همین الان موشک بلند شد ازش
الان از یزد موشک پرتاب شد
🔄
همین الان دوتا دیگه
دو تا دیگه از یزد زدن
۲۳:۰۸ دوباره از
#یزد
موشک زدن.
۳ تا موشک دوباره یزد بلند شد
سومین موشک هم شلیک شد
ساعت 11:08 دوتا موشک دیگه از یزد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78164" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bqUe-7hyLQUYdRgJ9y-EEA4QNlRebNO1O39IzCZTnglGOSb4ybZAX7SWeufVjyOn7nvsfDwxdu6wthNqhHv8a0O8cS5uMFXPG5Nr1fJbMlWTVP8SoWSQ6OqKteUbQHYdAt0lEXNh23Q8hk6ooqEIuSz4S6yOzE6QMk0vyyOrWJUkxvzL4cJElkD2NE_QPfhcvKQD0afQpLkp20huxKFQ8Vr25wjoe1Yd61N55iVv1YU57aP8UPIjjPeEIPogDYTMfB2qgo8-f1KvYpCPeiGllillp30GnH6gjKdXTLvtlNVb6eOG2LKurhrDDKBCfkDG_P34NZq8M_xHuiPijsLrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rAAgNFy8JwRODXrpk_bTCiSogMkri5yBk6mHHBKc-o2unsXH70Xv0ZK9wr60F27OLZFjWbc2AgE9KxI0DxPRfAILn2MFMCFFtMIJlXxvsuvrE-Isc2nt6uaOqyLLqYxvKUJSPwj3JcprMzPE3WYqzytXf0rXFeQT0Z-NDSgR_pYu2DoPdkLk4pJLkG_OcUkV0ceHOrPR_1AeulrYr8qpjLt0lhVcCUyV5skdUWX-K982Hc04GqBwSjySP4y10RHn803jfdOvwtbBxQkftpl8Vs4mshuEVwst8rY78edk5Ks_TwHzfFvrkTdsCXvqB0IMg9cz8PYJSl_Hjzn61GY9kA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=AqH4fYDSkb7yg43BWZ7f1ZZVsAZsHclW9dh0aW3jD8-JPMVbfZsUPGsE6CYdo2kbVz_6L5oRfBL4aRbyazrVe57oj0ARUlfig870XZ9FQhDHY2Eqm6xGV3_JMmi62ZXVdZQF5dY2FRM9ykNbh_8YmSP1ElLxdAyLXPUcqgD7Y5LCwEZ8Jhgz32al2yKY0TdtdGKCIt2nDtQ0KLGLSQa5a8jUgLdaoj-yPz86-nhEHNcINme8y59zunN5KMpcdLFAB-Z_3X2Fy2LzLa5B35YUnhJf-wUGVrZN-3ckj0NtLaWRj9qR2YSVeTFFuQz9lrHoZw27XiZIFDTCyau3wHUAxw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d52090feb6.mp4?token=AqH4fYDSkb7yg43BWZ7f1ZZVsAZsHclW9dh0aW3jD8-JPMVbfZsUPGsE6CYdo2kbVz_6L5oRfBL4aRbyazrVe57oj0ARUlfig870XZ9FQhDHY2Eqm6xGV3_JMmi62ZXVdZQF5dY2FRM9ykNbh_8YmSP1ElLxdAyLXPUcqgD7Y5LCwEZ8Jhgz32al2yKY0TdtdGKCIt2nDtQ0KLGLSQa5a8jUgLdaoj-yPz86-nhEHNcINme8y59zunN5KMpcdLFAB-Z_3X2Fy2LzLa5B35YUnhJf-wUGVrZN-3ckj0NtLaWRj9qR2YSVeTFFuQz9lrHoZw27XiZIFDTCyau3wHUAxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی: سه موشک از
#خمین
پرتاب شد
تصویر دریافتی سوم از آسمان ازنا در لرستان
سه‌شنبه ۱۰ شهریور
Vahid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 249K · <a href="https://t.me/VahidOnline/78160" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=DsqOmwbH-KiqIYJJD3hqO8bo8pMF_Bl9X6TOgq3bpDgSUti7d6-VNcPVtmNEOg-Mx_EmhGQpABRW72OwuZ1iPZmhuMYtLOdqViyALk3khZd-iPxkWOgDhkxYP8JOycl3sPESwzIyCrePNtsxWgiYf74louoKqxGl42fHTWfMRJtzpEQjhlckbpBwoEI-n9letvZzfrkAHFln2P_l3fZfrQ99Ik3V9Mxp4XR2s0vdiS-TakWAcg9RvjM5o9nivI8CBDbxlWmWDY_9VF8xI3IBfkTQKN8Xvtiy7IOSJ4bL2w1d3YbrghTPBP1t_lPgy84hJo_dRkw1Z8WpG5DlpH7NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31624e0a81.mp4?token=DsqOmwbH-KiqIYJJD3hqO8bo8pMF_Bl9X6TOgq3bpDgSUti7d6-VNcPVtmNEOg-Mx_EmhGQpABRW72OwuZ1iPZmhuMYtLOdqViyALk3khZd-iPxkWOgDhkxYP8JOycl3sPESwzIyCrePNtsxWgiYf74louoKqxGl42fHTWfMRJtzpEQjhlckbpBwoEI-n9letvZzfrkAHFln2P_l3fZfrQ99Ik3V9Mxp4XR2s0vdiS-TakWAcg9RvjM5o9nivI8CBDbxlWmWDY_9VF8xI3IBfkTQKN8Xvtiy7IOSJ4bL2w1d3YbrghTPBP1t_lPgy84hJo_dRkw1Z8WpG5DlpH7NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی:
خمین همین الان دوتا موشک زد
سومی رو هم زد
سه تا موشک از خمین زدن
سه صدای شلیک موشک از الیگودرز - احتمالا سمت خمین باشه
شلیک مجدد موشک از خمین، بیش از 3تا
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78159" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">پیام‌های دریافتی:
قشم دو انفجار شدید اطراف شهر
شد ۴بار پشت سر هم و شدید
ساعت ۲۲و ۲۸ دقیقه
۲۲.۲۹
دوتا انفجار بزرگ بندرعباس
سومین و چهارمین انفجار بندرعباس  ۲۲.۳۰
سلام قشم رو الان خیلی بد زدن
بندرعباس ۱۰:۲۹ سه تا صدا
چندتا صدای دیگه هم داره میاد
بندرعباس دو صدای انفجار
بندر دوباره دوتا انفجار
وحید شد ۴ تا
وحید جان بندرعباس مجدد 22:28 صدای سه تا انفجار از سمت ساحل اومد
ما خونمون بغل فرودگاس
شهرک صنعتی طولا قشم یا ناحیه سپاه چهارتا انفجار، صدای سوت موشک قبل از انفجار هم اومد
۲۲:۲۸
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78158" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pZBxWOARwKJ3fXX65i43LSfotWn7ee7BO62B3NsfPEQZ1dycQz_kAqdE3VRP39vkA-U8jaQGf9LRW97I5AWppySZXehZbndDFljm2ycc5J4W33-o1HWCziDnH8q1RAwdFuOrajKii8o0fQIQMSPeHtB7KUqH9da226C3zZFC18UjF5QcwL3NNJLTcXocn82dkkd-byRK3al1aAlUUNivxOIoHtpPZjKI2VjwsSANS-TeTrPq-5-SQZtyLNvjXH4-ojRJ8KgsV6Q62bnjtCtGwUpPNKmG_9RDfqkwpUVXOAPmo_x0xh_kxfl3Swk_Bqhsx4oBEvDsnBDvgbrbBZQk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش ترامپ به التماس‌های بازگشت به تفاهنامه اسلام‌آباد:
دونالد ترامپ، رییس‌جمهور آمریکا، روز سه‌شنبه ۱۰ شهریور در گفت‌وگو با شبکه فاکس نیوز بازگشت به «تفاهم‌نامه اسلام‌آباد» را رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد».
ترامپ درباره پاسخ جمهوری اسلامی به حملات آمریکا گفت: «اگر آنها پاسخ بدهند، با شدت بسیار بیشتری هدف قرار خواهند گرفت.»
او حملات انجام‌شده را «بسیار بزرگ» توصیف کرد و افزود اگر درگیری برای سومین بار تشدید شود، ایران «به‌عنوان یک کشور به‌طور کامل از بین خواهد رفت».
رییس‌جمهور آمریکا گفت حملات اخیر، سامانه‌های راداری در جنوب‌غرب ایران و نزدیکی تنگه هرمز را هدف قرار داده‌اند؛ سامانه‌هایی که به گفته او ایران در حال بازسازی آنها بوده است.
ترامپ گفت نیروهای آمریکایی بخش قابل‌توجهی از شبکه راداری ایران را منهدم کرده‌اند و افزود: «آنها تلاش کردند رادارهایشان را دوباره بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریبا آماده شود و بعد آن را هدف قرار دادیم.»
او همچنین گفت ناو هواپیمابر «یو‌اس‌اس جورج واشنگتن» به‌طور کامل برای ادامه عملیات در صورت نیاز آماده است.
ترامپ بازگشت به «تفاهم‌نامه اسلام‌آباد» را نیز رد کرد و گفت توافق با ایران «ارزش همان کاغذی که روی آن نوشته شده را هم ندارد». او افزود آمریکا فرصت‌های زیادی برای دستیابی به توافق در اختیار جمهوری اسلامی قرار داده است.
رییس‌جمهور آمریکا همچنین گفت متحدان واشنگتن در منطقه خلیج فارس پیش از حملات اخیر در جریان این عملیات قرار گرفته بودند و رهبران ایران درباره عزم او دچار «اشتباه خطرناکی» شده‌اند.
ترامپ در پایان سخنان خود درباره مقام‌های جمهوری اسلامی گفت: «آنها دست‌بردار نیستند؛ آنها دیوانه و احمق‌اند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 271K · <a href="https://t.me/VahidOnline/78157" target="_blank">📅 22:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=KyRYb5hO_IERwcK9jZhkLEB8Dy_lsLVqpertzPM7_wDwwLYoKZ948Zc2dHsSuzZIGsvWj2rMjm6N_HvOo2MsstloPtYEfXnIxuxi0tDcfmt3MilZyR8cxAt_0-JOIRmfcWyXcCIxXCG3boAMCbqa-cB2xIYFbhj-zmnz2dSeYS0WM8T423Nhb0AbGCEmOcJzuzb0RL9D_olLwE6k6p8YsZvkIO1HS4SrmYJ8wKs3tnlxhCzGAuAInJFbWHzSm__scv0mN7UoTwRipHguoikG8AqycqK4ZfV4JJTLNTfjh8xqx6-yRAqYgFWH82UJKJPB-nKG1uMVfSRdVQlUcSYt8g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1885075f5.mp4?token=KyRYb5hO_IERwcK9jZhkLEB8Dy_lsLVqpertzPM7_wDwwLYoKZ948Zc2dHsSuzZIGsvWj2rMjm6N_HvOo2MsstloPtYEfXnIxuxi0tDcfmt3MilZyR8cxAt_0-JOIRmfcWyXcCIxXCG3boAMCbqa-cB2xIYFbhj-zmnz2dSeYS0WM8T423Nhb0AbGCEmOcJzuzb0RL9D_olLwE6k6p8YsZvkIO1HS4SrmYJ8wKs3tnlxhCzGAuAInJFbWHzSm__scv0mN7UoTwRipHguoikG8AqycqK4ZfV4JJTLNTfjh8xqx6-yRAqYgFWH82UJKJPB-nKG1uMVfSRdVQlUcSYt8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
پرزیدنت ترامپ به فاکس نیوز گفت که امشب شمار زیادی از رادارهای ایران هدف قرار گرفته‌اند.
پرزیدنت ترامپ گفت: «آن‌ها تلاش کردند رادارهایشان را بازسازی کنند، چون نمی‌توانند چیزی ببینند. ما صبر کردیم تا تقریباً ساخته شود و بعد آن را هدف قرار دادیم.»
رئیس‌جمهور گفت اگر ایران پاسخ دهد، «ضربات بسیار سخت‌تری خواهند خورد... اگر کار به بار سوم برسد، آن‌ها به‌عنوان یک کشور کاملاً نابود خواهند شد.»
TreyYingst
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78156" target="_blank">📅 22:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">رسانه‌های وابسته به سپاه از آغاز حملات موشکی و پهپادی ایران به مواضع آمریکا خبر دادند
خبرگزاری فارس، وابسته به سپاه پاسداران، شامگاه سه‌شنبه ۱۰ شهریور به نقل از مشاهدات میدانی خبرنگاران خود از شلیک موشک‌ها و پهپادهای جمهوری اسلامی به سوی مواضع آمریکا خبر داد.
همزمان، خبرگزاری تسنیم، وابسته به سپاه پاسداران، نوشت «عملیات قاطع نیروهای مسلح ایران» در پاسخ به حملات آمریکا آغاز شده و «پایگاه‌ها و منافع آمریکا در منطقه زیر ضرب موشک‌ها و پهپادهای ایران قرار می‌گیرند».
تاکنون مقام‌های آمریکایی درباره این حملات جمهوری اسلامی اظهار نظر نکرده‌اند.
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78155" target="_blank">📅 22:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGi_vgpod8YwfnUmPQFspM3drBoPFuakpuYxhu9vmq1cgqWy5XIBiByCfhHoSnvGzvDEMQO1VkWoSMeQQ0UkFiqLkM0WYvVOxUazwXx6n2Cgo36gNOW70J4097FzI7LFs-ncgMg5ksUqZuGPRA4KFc7hkbSA38COdijeiFcTUH_d_5T2G7ms3w32Dhv_8hzgiqVYUfFL6MwikrY5e_NB0LzdlP876ZwrQd7e-opoN6OXauUXR8cZe3sjPxxs3LJI6n640uVHqkk9OhL2cwAIgPr36-FcBXQq7DtRQDvj_0r2UxctWqID0inReDa_g6rax0wGx5VIZQzylTnxcW0F3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با تری ینگست، خبرنگار فاکس‌نیوز و در پی آخرین حملات آمریکا به مواضع جمهوری اسلامی، هشداری صریح خطاب به تهران صادر کرد.
ترامپ با اشاره به پاسخ احتمالی ایران گفت: «اگر دست به تلافی بزنند، بسیار سخت‌تر هدف قرار خواهند گرفت؛ و اگر دوباره چنین کاری کنند، دیگر وجود خارجی نخواهند داشت.» او با انتقاد شدید از اقدامات تهران افزود: «آن‌ها دست برنمی‌دارند؛ رفتاری دیوانه‌وار و احمقانه دارند.»
رئیس‌جمهوری آمریکا در ادامه به جزئیات حملات اخیر اشاره کرد و گفت: «آن‌ها سعی داشتند رادارهای خود را بازسازی کنند چون هیچ دیدی نداشتند؛ ما صبر کردیم تا ساخت آن تقریبا تمام شود و سپس آن را زدیم.»
ترامپ همچنین با ابراز بی‌اعتمادی کامل به مسیر دیپلماسی با حکومت ایران تاکید کرد: «معتقدم توافق با آن‌ها حتی به اندازه کاغذی که روی آن نوشته می‌شود هم ارزش ندارد. ما شانس‌های زیادی به آن‌ها دادیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78154" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صداوسیما: فرودگاه جیرفت هدف حمله آمریکا قرار گرفت
خبرگزاری صداوسیمای جمهوری اسلامی شامگاه سه‌شنبه ۱۰ شهریور گزارش داد دقایقی پیش فرودگاه غیرنظامی جیرفت هدف حمله آمریکا قرار گرفته است.
این رسانه افزود اطلاعات تکمیلی درباره این حمله منتشر خواهد شد.
@
VahidOnLive
اسکندر پاسالار، فرماندار عسلویه، به خبرگزاری فارس، وابسته به سپاه پاسداران، گفت: «حوالی ساعت ۲۰:۱۰ شامگاه سه‌شنبه، صدای یک انفجار در شهرستان عسلویه گزارش شده است.»
فرماندار عسلویه گفت که از خسارات جانی و مالی این انفجار جزئیاتی مخابره نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/78153" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78152" target="_blank">📅 21:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=cTT19lcLoFgJH4ZlkkwaTgU8tRmQzxAMNfGJtgmVMhPsP-Af0sBbuZojvHtglME8MXdgocycgu8jZqCQFTQJo4CBWQqXbgS1fxFwo_Q6uzuMVyEyXFfTmBq9g_lrTZZ7WZRK-coazSRR3l7iuU8nbkiRb-x7MdXqM1H4KhvACiHIoVSRwL6h8h10OR5gK88E5YZHof3BnUYZGtUCf9Q10e6souRrwP_oSLT0BLpXvlWZLdeXgTSlz7g1OMjEZfYt_51IEWP4aW356IMts4ReprdAwG6uXuVVfykYBrLN0BY_BGBQJ6kPaROOWTborh3RoKdQ4oS2EcfXIniWm4R3xg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c7f913a5d.mp4?token=cTT19lcLoFgJH4ZlkkwaTgU8tRmQzxAMNfGJtgmVMhPsP-Af0sBbuZojvHtglME8MXdgocycgu8jZqCQFTQJo4CBWQqXbgS1fxFwo_Q6uzuMVyEyXFfTmBq9g_lrTZZ7WZRK-coazSRR3l7iuU8nbkiRb-x7MdXqM1H4KhvACiHIoVSRwL6h8h10OR5gK88E5YZHof3BnUYZGtUCf9Q10e6souRrwP_oSLT0BLpXvlWZLdeXgTSlz7g1OMjEZfYt_51IEWP4aW356IMts4ReprdAwG6uXuVVfykYBrLN0BY_BGBQJ6kPaROOWTborh3RoKdQ4oS2EcfXIniWm4R3xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های زیادی دریافت کردم که نوشتند حدود ساعت ۲۱:۲۵ از
#خمین
موشک شلیک شده ولی پرتاب موفق نبوده و برگشته.
ویدیوهای دریافتی: سه‌شنبه ۱۰ شهریور
Vahid
آپدیت:
منابع جمهوری اسلامی بعدا این ویدیوهای دریافتی رو با شرح هدف قرار گرفتن پهپاد آمریکایی منتشر کردند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 236K · <a href="https://t.me/VahidOnline/78150" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پیام‌های دریافتی:
صدا ۹:۰۵ بندرعباس
وحید بندرو دوباره زدن همین الان
صدای انفجار بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/78149" target="_blank">📅 21:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ISe8BFgZdg-GF2wmziQg2ODD0x4VlfvEikV7P13Cz0phzw_riQlEkJYRyGaEhSwgEiPRHh2eaC162wQVjtzzaZq65Mwbg-FBQCAUdlONVmYL0D_xCGALdRXDFJRMGLTMI_Ruvd6Z1iYxiy6FjsY_w02yldF04vUE_Nb52AOaUPVGqeQsUngDJ5bwbXnnJ0rrmkFe3vTxFW1JpcyxOBTKWmmgXSTBLbzKPZiZq1GzYJT3mg8_uRKKa1ga59O0jOvEHwezoDioVQiedy37U39mbzu-tSOsLo_c8OAGtBBNyojc-USAFUYuF6cWf0qI_gIYUvRRXEqugqmH608QyAhjmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر ایران پاسخ دهد، حملات آمریکا شدیدتر و گسترده‌تر خواهد شد
ترجمه ماشین:
ایالات متحده همین حالا، در حالی که صحبت می‌کنیم، در حال حمله به اهدافی ایرانی در نزدیکی تنگه هرمز است.
این حملات گسترده و قدرتمند هستند و در تلافی تلاش نافرجام ایرانی‌ها برای افزودن مین‌های دریایی به تنگه انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (همه آن‌ها به‌طور کامل جمع‌آوری یا منفجر شده‌اند!)، و همچنین در تلافی شلیک هشت موشک از سوی ایرانی‌ها به پایگاه نظامی ما در اردن که همگی با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه دست به تلافی بزند، بار دیگر و در سطحی بسیار شدیدتر و بالاتر مورد حمله قرار خواهد گرفت؛ اما آن هم بزرگ‌ترین حمله از همه نخواهد بود. آن حمله هنوز در انتظار است و وقتی به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 270K · <a href="https://t.me/VahidOnline/78148" target="_blank">📅 21:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پیام‌های دریافتی:
سلام صدای چند انفجار اومد بندرعباس ۸٫۵۰
۸:۵۲ قشم یه انفجار حس شد
بندرعباس صدای 2 انفجار دیگه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/78147" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRz70M3Yz0JAh9RBl8G4f8vAyWs-x8wZQmC4SxBCvVOMwP9XWE_fc53jjOWnny_Yee0YUCo7rxiXoaa9c1njdzqLfHyK42ar09Xb4TuZl_ETXUcUVU92-oRMoX1LzfLRCtUsM0A1M-kpxCRfr7CEH5HyrFkD4IR0H1pZitw3OiFjhjLQFnwG8uAby2-ooLMYVQ9OBMhLc1YDjatQZYBeLZjdwA3jsJvuvUJVvkqQsXirNnlkQZoXvUic0wImhhpHGY7xR5HiS2ipCrwcI6ehPsHSJDxvWh03Lm7GcglsrXY5lvqxV9vf9EZIFJ7eiXnO_6_JiaeTzrzp4EZJWoDyrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز سه‌شنبه ۱۰ شهریور، در پی شروع دور جدید حملات ارتش آمریکا به مواضع نظامی در ایران، خبرگزاری آکسیوس این اقدام را صحه‌ای بر گزارش خود مبنی بر طرح آمریکا برای حملات مداوم و دوره‌ای به مواضعی در شهرهای حاشیه تنگه هرمز دانست.
پایگاه خبری آکسیوس به نقل از مقامات آمریکایی گزارش داد که دونالد ترامپ و مقامات ارشد دولت او در حال بررسی طرح‌هایی برای انجام حملات محدود در تنگه هرمز و مناطق اطراف آن هستند. هدف اصلی این حملات، جلوگیری از بازسازی سامانه‌های راداری، پدافند هوایی و توانمندی‌های موشکی ایران اعلام شده است.
به گفته آکسیوس این طرح که توسط فرماندهی مرکزی آمریکا (سنتکام) تدوین شده و مورد حمایت پیت هگست، وزیر جنگ قرار گرفته، به دنبال مهار تلاش‌های تازه ایران برای تهدید شناورها و نفت‌کش‌هاست.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78146" target="_blank">📅 20:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RYjOO-mcuQQCz8gRj8srjnFsoofQ_93Q6s13r7AuCcprY6hI9Q1b86XvLjRY1ksu-UobxctxouTIJBukpuOLj9YaeuwgJwrazu9PX7vn-xwzjDO4hgWlrvDwurWyCL3rVPoJStp1j5wHnHcvcuOhkUosv3u8xdSLsnfaVLQKWkzt8Rl1JAlgdIdQJ5M9kh8IkugEJKF0ODd8aZXwbfnXqFI-6GKTZggDo7gIKnYrOZLVY3wtsP60zpVOOPKfOphgjDDUNo3vspWaTrbe9hM-vYbM1YdER86kEO58PpE1azRCmx3yy8-1cx-HKnAQxKWttbFDRU-LmibNZg4uuclQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سنتکام در این لحظه منتشر شد. چیزی که پیش‌تر در منابع دیگر پخش شد درست نیست:
امروز ساعت ۱۲ ظهر به وقت شرق آمریکا [ساعت ۱۹:۳۰ به وقت تهران]، نیروهای ایالات متحده حمله به اهداف سپاه پاسداران انقلاب اسلامی در ایران را آغاز کردند.
این حملات پس از تلاش‌های اخیر سپاه پاسداران برای حمله به کشتی‌های تجاری در تنگه هرمز و نیروهای نظامی آمریکایی مستقر در منطقه انجام می‌شود.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 262K · <a href="https://t.me/VahidOnline/78145" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FqGiMHlawYEjG1sarpixYgrhmnAWNavCIgrHpfVnTdD2mt5fbaGi3k7l6li7C2jFwPDvt92zqwL9q8E1emzFixtjlmMv9W56bWlWNSeU_FyiUysq4SfKioAMLeUUn0TeQ4ge-JFdJuvTFeb33VQXKblVxPgE-QN6ZQz50PW-PQp7qxBF0YTwv_nqb27THLqfeM53PS9yTBNqsK3bOTDkJxbL0zNNQ811HXfxlGhUNuzpmKed2inuQTt_z3c67RbQauavWiHhS6MIyWjocBJmA77xFP9nFP499w-Po-75pBCdnNFz1tvHH10ICndC1_QIgbCNE04CTiJPqTtCcO945w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری صدا و سیمای جمهوری اسلامی از شنیده شدن صدای چند انفجار در قشم در شامگاه سه‌شنبه خبر داد و نوشت: «دقایقی قبل صدای بیش از ۵ انفجار اطراف روستای مسن قشم شنیده شد.»
این خبرگزاری نوشت: «دقایقی پیش، صدای ۴ انفجار هم از سمت تنگه هرمز در قشم شنیده شد.»
رسانه‌های ایران از شنیده شدن صدای انفجار در بندرعباس، سیریک و چابهار نیز خبر داده‌اند.
معاون سیاسی، امنیتی و اجتماعی استانداری هرمزگان، می‌گوید تاکنون هیچ‌گونه اصابت یا حادثه‌ای در هرمزگان گزارش نشده است.
@
VahidOOnLine
علی خلیل‌آبادی، معاون امنیتی و انتظامی استاندار سیستان و بلوچستان، در گفت‌وگو با خبرگزاری دولتی ایرنا از اصابت چهار پرتابه در شهرستان‌های چابهار و کنارک خبر داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/78144" target="_blank">📅 20:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">پیام‌های دریافتی:
۱۹:۵۸  چهار انفجار پشت سر هم
بندرعباس ۷ انفجار شدید ۱۹:۵۷
دوباره زدن بندرعباس
صداهای پشت سر هم ولی این بار خیلی دور
7 صدای انفجار بندرعباس سمت شرق پشت سر هم ساعت نزدیک 8
سلام بندرعباس حدود 10 انفجار
7:57
صدای ۵ انفجار  (۳ انفجار پشت سر هم و ۲ انفجار جدا ) از فاصله دور جزیره قشم شنیده شد
ساعت ١٩:٥٧ دقیقه چندتا انفجار پشت سر هم شنیدم یندرعباس
شیش انفجار مجدد بندرعباس ساعت هفت پنجاه هفت دقیقه خیلیم شدید
7:57 بندرعباس 10 شهریور بالای 10 تا انفجار
بندرعباس ۱۹:۵۷
چهار پنج تا پشت سر هم زدن
دوباره زدن ، شاید هم صدای موشک از اینطرفه، صدا اینبار کمتر بود ولی تعدادش بیشتر بود
بندرعباس انفجار های پشت هم صداش قطع نمیشه
چقد زیاد ۷ تا انفجار توی ۱۰ ثانیه ساعت ۱۹.۵۸
دور از قشم
۱۹:۵۸  ۴ انفجار پشت سر هم
احتمالا بندرعباس
ولی از قشم به خوبی احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78143" target="_blank">📅 19:59 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام‌های دریافتی:
دوباره زدن بندرعباس
الان یه انفجتر دیگه بندر عباس از بقه بلند تر بود ساعت ۱۹:۴۵
یک انفجار شدید الان در بندرعباس
۱۹:۴۶ دوباره بندرعباس صدای ۲ انفجار متوالی
ما شرق بندرعباسیم، صدا ضعیف بود.
سلام دوباره همین الان قشم رو زدن دو مرتبه19:47
وحید جان صدای شدیدتر همین الان بندرعباس
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/78142" target="_blank">📅 19:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پیام‌های کمی از سیستان و بلوچستان:
19:34 کنارک انفجار اول
19:36 کنارک انفجار دوم
سلام وحید جان صدای انفجار چابهار همین الان
چابهار داره میزنه19:33
شیش هفت تا انفجار پشت سر هم
چابهار صدای پنج انفجار پنج دقیقه پیش
سلام وحید تو خونه ۶ تا شنیدیم شاید بیشتر بود
کنارک
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 253K · <a href="https://t.me/VahidOnline/78141" target="_blank">📅 19:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔽
#بندرعباس
پیام‌های دریافتی:
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندرعباس صدای ۳ انفجار ۱۹:۲۸
بندرعباس دو صدای انفجار
بندرعباس 3 انفجار همین الان
درود چهار صدای انفجار با موج انفجار بندرعباس ساعت ۱۹:۲۸
وحید بندر سه تا صدای انفجار اومد ۱۹:۲۹
بندر عباس 19:29
صدای ۴ انفجار سنگین
سلام، هم اکنون صدای دو انفجار در بندرعباس
درود وحید جان بخدا دیگه دارن میزنن بندرعباس الان دو تا انفجار محدوده فرودگاه ساعت ۱۹:۲۹ حالا یا زدن یا خوردن
سلام
۳تا صدای انفجار مانند الان بندر عباس اومد تو خونه حس کردیم نمی‌دونم چی بود دقیق
سلام بندرعباس الان با فاصله های چند ثانیه ای صدای ۴ تا انفجار اومد
صدای دوانفجار بزرگ بندرعباس ساعت هفت وبیست وپنج دقیقه شب
۱۹/۲۹ چند انفجار پشت هم قشم حس شد
احتمالا لارک، هرمز یا بندرعباسه
احتمال بیشتر لارک صدا از سمت جنوب بود
بندرعباس الان دوتا انفجار شدید
۱۹:۲۹ زدن
منطقه بهشت بندر صدا واضح بود
وحید جان سلام بندرعباس همین الان ۳ انفجار شدید
بندر رو زدن
وحید جان صدای دو انفجار سمت اسکله رجایی العان
دوبار ۲ تا دیگه
سمت قشم درگهان بود موج
درود وحید خان صدای 4 تا انفجار پشت سر هم بندرعباس از سمت بلوار شهید رجایی
خیلی شدید
درود وقت شما بخیر
ساعت هفت و بیست هفت بندر عباس صدای انفجار
قشم خیلی صدای انفجار میاد همین الان
شروع شد ۱۹.۲۹.  صدای ۴ تا انفجار دور از قشم
یکی دیگه دقیقه ۳۱ دور بود
سلام وحید جان قشم صدا و موج انفجار میشنویم
خیلی دوره ولی بزرگ احساس میشه
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 263K · <a href="https://t.me/VahidOnline/78140" target="_blank">📅 19:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/db6862775f.mp4?token=edmlMMG3Bw179JC3xHxe64QG5KxXSF5Js-qshd_NNp7qBT-3b86XvRmbGkTIdqt8scJq7TXVDARsX2q6a2mro0qoYQmNr0N1BGLQkZGj2kkMiGim5sntkHo6FXWkVV8kiX1CnVfPfDY-YmK_PrMQdJjOnNiG18hE18LttiD9bjaKT1B93UwPBGPXzoSQIkoGFtrfqablSQqIu1EynWOoeroW0LC7PC3-11mHhJ2n1ytvKGg3P2enXx9jpQ9zg9GAR7Dq8c_9rtt48b_dM8HwPRUyD3t3Q0yhHmjnJwnHA0SQug7RzzcH5ER1llWWR3E689LO3UiLKjAgN12MJN3y_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/db6862775f.mp4?token=edmlMMG3Bw179JC3xHxe64QG5KxXSF5Js-qshd_NNp7qBT-3b86XvRmbGkTIdqt8scJq7TXVDARsX2q6a2mro0qoYQmNr0N1BGLQkZGj2kkMiGim5sntkHo6FXWkVV8kiX1CnVfPfDY-YmK_PrMQdJjOnNiG18hE18LttiD9bjaKT1B93UwPBGPXzoSQIkoGFtrfqablSQqIu1EynWOoeroW0LC7PC3-11mHhJ2n1ytvKGg3P2enXx9jpQ9zg9GAR7Dq8c_9rtt48b_dM8HwPRUyD3t3Q0yhHmjnJwnHA0SQug7RzzcH5ER1llWWR3E689LO3UiLKjAgN12MJN3y_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.  درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید…</div>
<div class="tg-footer">👁️ 246K · <a href="https://t.me/VahidOnline/78139" target="_blank">📅 18:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ugJ45mhJoyL5lGHRMsIWBJV5vPAPpNEKxD8RFyYm2f43NHzyJnYgYlbJ6yx7o-dhld-oUnLTKTYnzuwTIxnFXi8y1S04WW-_-xV7Qmm8iWYCqYTB3wuNC5ijLKcRmmL1HcCKhR24Ab2_-SjKF_-JG7pezF_FYEHbIhTAl5JSJvi21ukSPBT3ggbiAQZSsFBN1TdyTxjkNv4FnauKn4-7L7cVNriKY1dltjdLfaPyOg1EMX2vEVCxkoRZkVBbAIq2z_2jzMBLuerTCwHKdADS-4HdfaERuZAL8lhSqMe18Ds-MQdQKtm3h9gdz9q0B0OuL9L_507_IC7_Z6U0HkT8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=LZpBGGpsjdCxnyh7cHHd4KbRRKbJtEgvr0OGjy5pPJvdnqQNoSeqUlqk0YufDJCP1Yvcct7RJdwnmFBXG-udbS7vvhsG-QzZVY6Joim33aTKtI4H3QDXvcWJEQesVLv6jHRY0BgHWB7VrZNvyKzFku9cZjskXNT1x_ky8xYu-YMb-7xM3nKP1Bpcb5WLsDUbkgimenTD0JuhLDoXuTAQlwvNHlbzKHr2XLzyhmN-R2PKfkotKtqV0JRgqMuuEvlzZRq3oRL3uBLpPxR_tmsFdPqGGvGWLpZE1XgLCFR-fxyiwd1X4keGJLBSBOp0LTKp2MELL19i5zj3VulA6pCzqw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a23e113ac.mp4?token=LZpBGGpsjdCxnyh7cHHd4KbRRKbJtEgvr0OGjy5pPJvdnqQNoSeqUlqk0YufDJCP1Yvcct7RJdwnmFBXG-udbS7vvhsG-QzZVY6Joim33aTKtI4H3QDXvcWJEQesVLv6jHRY0BgHWB7VrZNvyKzFku9cZjskXNT1x_ky8xYu-YMb-7xM3nKP1Bpcb5WLsDUbkgimenTD0JuhLDoXuTAQlwvNHlbzKHr2XLzyhmN-R2PKfkotKtqV0JRgqMuuEvlzZRq3oRL3uBLpPxR_tmsFdPqGGvGWLpZE1XgLCFR-fxyiwd1X4keGJLBSBOp0LTKp2MELL19i5zj3VulA6pCzqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا گفت: «جهان از رژیم مطرود و یاغی ایران خسته شده است و ترامپ به‌جای مماشات با آن‌ها می‌خواهد یک‌بار برای همیشه به آن‌ها خاتمه دهد. مردم ایران این فرصت را دارند که به نظام جهانی برگردند، به‌جای اینکه سرکوب شوند.»
IranIntl
بسنت گفت: «ما سر مار ایرانی را زیر خاک کرده‌ایم. مار هنوز نمی‌داند که مرده است و بدنش کمی حرکت می‌کند، اما با غروب آفتاب از حرکت باز خواهد ایستاد. رژیم ایران نابود شده است و به‌زودی خودش هم این را متوجه خواهد شد.» او تاکید کرد دونالد ترامپ قصد دارد این پرونده را برای همیشه ببندد.
@
VahidOOnLine
اسکات بسنت گفت: «ایرانی‌ها تلاش می‌کنند از تنگه هرمز به عنوان یک گلوگاه استفاده کنند. این تنگه برای آمریکا گلوگاه نیست، اما برای بسیاری از کشورهای دیگر هست. این وضعیت تا دو سال دیگر دور زده خواهد شد. تا دو سال دیگر، تنگه هرمز به پهنه‌ای بی‌ارزش از آب تبدیل خواهد شد.»
بسنت گفت: «نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.»
@
VahidOnLive
وزیر خزانه‌داری آمریکا: در حال شناسایی و ردیابی دارایی‌های سپاه هستیم
اسکات بسنت، وزیر خزانه‌داری آمریکا، روز سه‌شنبه ۱۰ شهریور در حاشیه نشست وزیران و مقام‌های ارشد مالی گروه ۲۰، از تشدید فشار اقتصادی واشنگتن بر ایران خبر داد و گفت آمریکا احتمالا این هفته یک بانک و هفته آینده یک بانک دیگر را تحریم خواهد کرد.
بسنت گفت: «احتمالا این هفته تحریم یک بانک را اعلام خواهیم کرد و هفته بعد نیز یکی دیگر را اعلام می‌کنیم.»
او افزود آمریکا در این زمینه با متحدان خود در حال گفت‌وگو است و از حمایت آنها برخوردار است.
وزیر خزانه‌داری آمریکا همچنین گفت واشنگتن در حال بررسی تحریم شرکت‌های لیزینگ هواپیما و دیگر نهادهایی است که با سپاه پاسداران تجارت می‌کنند.
او گفت: «ممکن است این‌ها نهادهای مختلفی باشند. ممکن است شرکت‌های لیزینگ هواپیما باشند که آنها را بررسی خواهیم کرد. ممکن است هر کسی باشد که با سپاه پاسداران تجارت می‌کند. ما در حال شناسایی و ردیابی دارایی‌های سپاه هستیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 218K · <a href="https://t.me/VahidOnline/78137" target="_blank">📅 18:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78136">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=qtQMKWeF48bP9k2FEu5Cr59Fz6NUJqY6WSLcaeaCZdGEsu_FcVlPEr97KqMHRPfgWq3tPmXEC3q8cGMAr1S6a_DjnA9bn4nSSZWMvmml0koPIQDBF0i8LEqEda8yLQ-B1MX6u7fyjG6548X67SYJDmG7AXH7sYqw6NSv9te2QLfLYndI7Nh1FPV_lF2Cqp7lEwioamqw_gbMpZEAg9b79YSHIRD3hRfzbR99Kd405HqkqA2TaX0OtwQJaphVfHqFUJrYtNlKSn0dIY6Yjo9SQCc9pABFdEA5t_X6g1dNY1QI-mdhpwce8atnegpg3VPFOeeDc7RG6DQmzjmUjzKDeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fb5fccd6a2.mp4?token=qtQMKWeF48bP9k2FEu5Cr59Fz6NUJqY6WSLcaeaCZdGEsu_FcVlPEr97KqMHRPfgWq3tPmXEC3q8cGMAr1S6a_DjnA9bn4nSSZWMvmml0koPIQDBF0i8LEqEda8yLQ-B1MX6u7fyjG6548X67SYJDmG7AXH7sYqw6NSv9te2QLfLYndI7Nh1FPV_lF2Cqp7lEwioamqw_gbMpZEAg9b79YSHIRD3hRfzbR99Kd405HqkqA2TaX0OtwQJaphVfHqFUJrYtNlKSn0dIY6Yjo9SQCc9pABFdEA5t_X6g1dNY1QI-mdhpwce8atnegpg3VPFOeeDc7RG6DQmzjmUjzKDeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر قالیباف، رییس مجلس شورای اسلامی، سه‌شنبه در پیامی ویدیویی با تاکید بر اینکه محاصره دریایی در قوانین بین‌المللی، یک اقدام نظامی محسوب می‌شود، گفت که اگر محاصره را تشدید کنند، حتما پاسخ نظامی می‌دهیم و همه ضرر خواهند کرد.
قالیباف گفت: «اگر دشمن اراده‌اش بر این باشد که ما از خلیج فارس نفت صادر نکنیم، هیچ‌کس نخواهد توانست نفت صادر کند.»
او گفت: «آمریکا می‌خواهد برخلاف تفاهم‌نامه از مسیر جنوبی تنگه هرمز عبور کند که این اجازه را نخواهیم داد.»
رییس مجلس افزود: «دشمن در حال حاضر در جنگ اقتصادی، بر روی جنبه روانی آن متمرکز شده است.»
قالیباف گفت که دشمن پس از «شکست در عرصه نظامی و دیپلماسی» سراغ جنگ اقتصادی و شناختی رفت و آن را به جنگ نظامی خود اضافه کرد.
قالیباف افزود: «هدف دشمن از جنگ ترکیبی این است که در داخل کشور، اغتشاش را به همراه ترور و حملات نظامی کوتاه آغاز کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 213K · <a href="https://t.me/VahidOnline/78136" target="_blank">📅 18:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Lfy30qV7C81o-H9BXwK_gtb2Doi6Bo1S6XPbfq2WcW9FRh_GLx15VxeOWPH0bqH1O81QYxsuKADmWQ4ZhH04uv5tKmF6V6z2sQAhv6YjZbXJ93uLPWlLS1S8VSyjgwYVurGzMT5in9LBRsqYZH6zgUi4r15BCdvng2TNA2JQBxyy8GcMw-5tUxP-g-kU_sQtcWr5HpZpPiTJX-9qzMmBCyDE4JYk8L0DMtaWOz-AsXltdS0WDqwh5Tk-fqLV3Sr4MhgK_zyEHErhCMQ8LPE6yh4n6J9HYjlKLKnP8MaWtF8PCoreDnuX2--SQnnxbhqQQo88c9uHkhVW-fE4e_GLUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همزمان با انتشار اخباری از حضور «حجاب‌بان‌ها» در بازار تهران و سخنان برخی از مقام‌های جمهوری اسلامی در رابطه با لزوم «اجبار حجاب»، تصاویری از نصب بنرهایی در شهرهای مختلف ایران منتشر شده که در آن‌ها زنان به مجازات قضایی در صورت رعایت نکردن حجاب مورد نظر حکومت تهدید شده‌اند.
در این بنرها، به تبصره ماده ۶۳۸ قانون مجازات اسلامی استناد شده و آمده است: «حضور بانوان بدون حجاب شرعی در معابر و انظار عمومی جرم و دارای مجازات حبس است.»
در بنر نصب‌شده همچنین به مواد ۷ و ۹ قانون موسوم به «حمایت از آمران به معروف و ناهیان از منکر» اشاره شده است. در توضیح ماده ۷ نوشته شده افرادی که در برابر «امر به معروف و نهی از منکر» مانع ایجاد کنند، مشمول تخفیف یا تعلیق مجازات نمی‌شوند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 200K · <a href="https://t.me/VahidOnline/78135" target="_blank">📅 18:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pp8bwNd1JZB4hpMhgRVYwqQ0pQ9KayBEP4_zFYt5luPXxxajpzADnmHk8R-iWsBefHPrm58kzH5GV2u9fBm7nCixNWxYXjwOYFzH3TnyGvUNVhx4LTdR1PCIBcH_H69wzqQZAad63on6iVkdvi9uY-ABhvTbQS33bLdHYgbJaJi9VWTLa4WNHbq3rjzUVW-cvPKWLccyxGfWJ7fMrgbUddb5KUBL9mfDw9yLLnBsI80Rq6X0LGtDArcH14ixsK7wYv15BTNz2R8WcUvmsYZdfnifeWX0sNecoTmACJSFdjZDe5EFKkZnZhgo-9hWXVY8-crOz70fWBT1_NcuxW3l-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت دلار در بازار آزاد ایران به ۲۱۳ هزار و ۷۰۰ تومان و حواله دلار به ۲۱۸ هزار تومان رسید. هر پوند بریتانیا نیز با ۲۸۹ هزار تومان معامله شد.
رقم امروز چهارمین رکورد پیاپی در چهار روز کاری است. دلار روز شنبه با ۲۰۶ هزار و ۴۰۰ تومان بسته شد، یکشنبه به ۲۰۸ هزار و دوشنبه به ۲۱۰ هزار تومان رسید.
همزمان با ثبت رکوردهای جدید در بازار ارز، رئیس کل بانک مرکزی در سی‌وششمین همایش بانکداری اسلامی گفت ایران کمبود ارز ندارد و ادعای فروپاشی اقتصادی کذب است.
همتی در پاسخ به اظهارات مقام‌های آمریکایی درباره نبود دسترسی ایران به منابع مالی گفت: «این ادعاها به‌طور کامل بی‌اساس است. ذخایر مسدودنشده، منابع پایدار و درآمدهای نفتی و غیرنفتی متعددی در دسترس بانک مرکزی قرار دارد.»
او افزود بانک مرکزی هفته گذشته ۵۰۰ میلیون دلار به بازار تخصیص داد و اکنون آمادگی دارد در صورت نیاز تا سقف دو میلیارد دلار ارز تزریق کند.
اظهارات امروز همتی با موضع پیشین او فاصله دارد. او هفته گذشته در گفت‌وگوی تلویزیونی گفته بود: «درآمد ما از فروش نفت صفر شده؛ یک واقعیتی است که نفت صادر نمی‌کنیم.»
چرخش لحن پس از پیام مجتبی خامنه‌ای، رهبر جمهوری اسلامی، به مناسبت هفته دولت رخ داد. او در آن پیام گفت گاهی بیان صادقانه ضعف‌ها کمک به دشمن است و بر ضرورت «تبیین و روایت قدرت و قوت ایران» تأکید کرد.
رهبر جمهوری اسلامی در همان پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/VahidOnline/78134" target="_blank">📅 18:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cykkR0SGNtJZXZwwYi0AIDaRHIQWkn2SoogtBxAnRYAEc8B2zGkNJlpoIEh3ohK3Y6XtDi9vzrGQ1Y6TPSNMeCgWz8jEMxdTPMB4gT-PvggY6UxMmbeRr9J_INvXWZUh8OJYY36q___QlrOudx0ecQc0BFVtIDXfN8-lg_nuaSl-0EKca1y6EdQiYnaDfXixrtF5Qbre8M1xrfjPzhkc1CCvMl_UV-B4uR28pVew-qSshIKDNf4pBsEA52w70ncxQCE2OWCM2nP-mSeyV9AyLY2fTeCBDuUQH60qHTJuIm4v5V_--iqqhnm4XIHr6FNPa5lFXOUmoawii9ULa_9pnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت‌های‌ ناظر بر کشتیرانی جهانی می‌گویند دو ابرنفتکش حامل نفت عربستان سعودی اواخر روز دوشنبه نهم شهریور هنگام عبور از تنگه هرمز به فاصله چند دقیقه از یکدیگر هدف اصابت پرتابه‌های ناشناس قرار گرفتند.
به گزارش خبرگزاری رویترز، شرکت یونانی امنیت دریایی «ماریسکس» روز سه‌شنبه دهم شهریور اعلام کرد که ابرنفتکش «سیدر» حامل نفت خام عربستان سعودی با پرچم همین کشور حدود ۱۶ مایل دریایی در شمال شرقی خصب، عمان، ساعت ۱۹:۵۲ دوشنبه به وقت گرینویچ مورد اصابت پرتابه‌های ناشناس قرار گرفت.
شرکت امنیت دریایی وانگارد تک هم گفته است نفتکش «سنگال پراسپریتی» با پرچم لیبریا دقایقی بعد در حدود ۱۷ مایل دریایی در شرق خصب مورد اصابت سه پرتابه ناشناس قرار گرفت.
پیشتر سازمان عملیات تجارت دریایی بریتانیا از حمله به این نفتکش خبر داده و گفته بود سه پرتابه به آن هنگام خروج از تنگه هرمز برخورد کرده است.
بر اساس گزارش‌ها، خدمه این دو نفتکش سالم هستند و هر دو به فاصله کوتاهی از یکدیگر متوقف شده‌اند.
داده‌های شرکت کپلر نشان می‌دهد که هر یک از این نفتکش‌ها هفته گذشته ۲ میلیون بشکه نفت خام عربستان سعودی را از بندر جعیمه در خلیج فارس بارگیری کرده بودند.
با تشدید دوبارهٔ درگیری ایران و آمریکا، قیمت برنت روز دوشنبه نزدیک به سه درصد افزایش یافت و به ۹۰ دلار و ۴۹ سنت رسید و روز سه‌شنبه نیز با ادامه روند صعودی به حدود ۹۱ دلار و ۱۵ سنت در هر بشکه رسید.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/VahidOnline/78133" target="_blank">📅 18:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vONh7qMiBQH7tgBez1JCtMO7L5ClgT5nyZP7rbiSX9ehrVHexY2Mz7EWKHWlw4kEsAKbpn57vV6y9PYYYvwvGSOzSX-V-axLqhcA2UzdNRWYJfkeulFb12GeYnvt_UZIA_1fkC2xte3Drq2M8zf4xuU-wnS3Zmr8i3zgaRM0gRBYvzkCSl6Xkpnn4flXWnSRpHd_WzIWuzTu-TqaxqkrTexzyeSZM6Xux57AUC1BNO9JqftYLdUzzVCtx6_BbBmKxQkPVxebd-oSvUDuNBFFPIToBncOnd0P-oL-EMs3850UOnZ6dA4hetRppPrWSTOjZWJ1XoMDqUdjuj0uxbsMNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدرضا نقدی، مشاور عالی فرمانده کل سپاه پاسداران، از ساکنان اسرائیل خواست به کشورهای خود بازگردند و «به‌سرعت فرار کنند». او گفت با کسانی که بمانند، مانند بنی‌قریظه رفتار خواهد شد.
نقدی گفت: «آنها باید بدانند رفتاری که نیروهای اسلام پس از رسیدن به آنجا در پیش خواهند گرفت، همان رفتاری خواهد بود که با بنی‌قریظه شد.»
او افزود: «پس باید به‌سرعت فرار کنند و هر کس بماند، بر اساس شیوه‌ای که با بنی‌قریظه رفتار شد و مطابق حکم تورات، نه بر اساس رحمت اسلامی، با او رفتار خواهد شد.»
بنی‌قریظه یکی از قبایل یهودی ساکن مدینه در دوره محمد، پیامبر مسلمانان، بود. بر اساس روایت‌های تاریخی اسلامی، پس از نبرد خندق و تسلیم بنی‌قریظه، مردان این قبیله کشته و زنان و کودکان به اسارت گرفته شدند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/VahidOnline/78132" target="_blank">📅 18:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eYpiBWEhl68JPAIrLu52PT5b7mqa6-3w1xTRihHAWNS6W5Ldr714CWQbXdYsgZ7M-9BxnZkgdcnoZi80j4iRBHGwS8TudVoncgYoz9-JTFdjOdZKmNwrph2zEheQ81_oDT_Ad-26F_4soLEr2lBmyH57b9149m3XlMhgK5rzQF5XTZDLgM1sDszVfnWejHANatj8ZYaJ2iscWRbAlJ3-JB6ph-CGx37Me9pJpZ1DyyodqS2NS1q9NMrQbrt0OhymJdc822faQLpSUNWeidEOesyTcagx77MuGL3Q1AbReET5rg-E1fFOr4zk9ZGJF_Vnjip2AzdYerPZZyAN2dNAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KrwHZH2ndpB93HgF1IEpQQhiKOsw_I9EuWkuZU7B-i_6fWPrt-UEtC6EXqZHX1wmawngBHVA9XyJaHIH94BqaUpqwDAPo9XFnl_iHg40YljX2T9oO7sNymUAQ2fHITnhc9fsyAmN6dngRu81GZTlW6JybigulTpKfOppptxJChXEkl3I_s0XktpUuZYAcP-7t9YvjGWBoTSPO8jhNo0xjEKVci1ybceHo3L4e27uXYklt905yNDumHeOnWS3dlFRbP_QAmXUqPNy9t1Qg2jCk-e8D3jfN70v9c-wERzQ_3Y5jO4PO1tHHuD7RSzoiR9A2sWtlaRQv-Mc2UIJf_5msA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">«کانون صنفی استادان دانشگاهی ایران» هشدار داده است اگر قانون ترمیم حقوق اعضای هیئت علمی تا پایان شهریور ۱۴۰۵ به‌طور کامل اجرا نشود، از استادان خواهد خواست فعالیت‌های دانشگاهی خود را از ابتدای مهر تعلیق کنند.
این کانون در بیانیه‌ای اعلام کرده است تعلیق فعالیت‌ها، حوزه‌های آموزشی، پژوهشی، اجرایی و مشاوره‌ای را شامل می‌شود و تا زمان اجرای «کامل و بی‌قیدوشرط» قانون ادامه خواهد یافت.
کانون صنفی استادان، سازمان برنامه‌وبودجه و رییس آن را به «مانع‌تراشی‌های سلیقه‌ای و خارج از عرف» متهم کرده و گفته است مکاتبه، مذاکره و رایزنی با مقام‌های مسئول نیز تاکنون به نتیجه نرسیده است.
این تشکل صنفی همچنین هشدار داده است ادامه بی‌توجهی به وضعیت معیشتی دانشگاهیان می‌تواند به افزایش مهاجرت نخبگان، کاهش بهره‌وری علمی و واردشدن آسیب‌های جبران‌ناپذیر به سرمایه انسانی کشور منجر شود.
مصوبه اصلاح حقوق اعضای هیئت علمی روز ۱۸ اسفند ۱۴۰۴ در شورای حقوق و دستمزد تصویب شد و قرار بود از ابتدای سال ۱۴۰۵ اجرا شود. این مصوبه، تغییر فرمول محاسبه حقوق و اصلاح ضر‌ایب مبنای پرداخت به اعضای هیئت علمی را در بر می‌گیرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 175K · <a href="https://t.me/VahidOnline/78130" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=suAIfj-4zaF0bEy9rWaVyZFoPDMzZgLnq7q41qjAS6FQuJIRkNijRrhOS1bvtmRBDDCi8eL9k7ki9h15-LaIhu0tWaetHmNau4ZrHJnmQSngXnJc5AjNCbkfs6VzE3McGCRZ3UQVkEGM-EA0jLwvsvqQxtm9d1x8k5Y6E_4ZUGzruquI_13xEaLUQT3HPxBvEv31SbG2-sW-NQv3X-yUpODNy2Uz-flUmzl53tDsoz6OXDHJajy5DBTQEVmyB4RkFZXclWhoOYIzEdeDgTdrBS9DDcSGnaa__BcEIcpIxwJRwKKKrLMt_X1bqiw3Ow9zyAdKHuucuPhiRk2utS-YHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/802f97efe1.mp4?token=suAIfj-4zaF0bEy9rWaVyZFoPDMzZgLnq7q41qjAS6FQuJIRkNijRrhOS1bvtmRBDDCi8eL9k7ki9h15-LaIhu0tWaetHmNau4ZrHJnmQSngXnJc5AjNCbkfs6VzE3McGCRZ3UQVkEGM-EA0jLwvsvqQxtm9d1x8k5Y6E_4ZUGzruquI_13xEaLUQT3HPxBvEv31SbG2-sW-NQv3X-yUpODNy2Uz-flUmzl53tDsoz6OXDHJajy5DBTQEVmyB4RkFZXclWhoOYIzEdeDgTdrBS9DDcSGnaa__BcEIcpIxwJRwKKKrLMt_X1bqiw3Ow9zyAdKHuucuPhiRk2utS-YHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، روز سه‌شنبه ۱۰ شهریور در دیدار با ولادیمیر پوتین، رئیس‌جمهوری روسیه اعلام کرد که اگر ایالات متحده آمریکا به تفاهم‌نامه اسلام‌آباد برگردد، تهران نیز آماده است که به مفاد آن عمل کند.
پزشکیان، در این دیدار که در حاشیه نشست سران سازمان همکاری شانگهای برگزار شد، حضور ایران در سازمان‌هایی چون شانگهای و بریکس را تلاشی برای مقابله با «یک‌جانبه‌گرایی» آمریکا توصیف کرد.
پزشکیان در ادامه با تاکید بر تفاهم ایران و روسیه در زمینه ضرورت چندجانبه‌سازی در سیاست و اقتصاد جهانی، ابراز امیدواری کرد که این فرآیند به شکلی موفق پیش برود.
@
VahidOOnLine
مسعود پزشکیان، رییس دولت جمهوری اسلامی، در دیدار با ولادیمیر پوتین، رییس‌جمهور روسیه، گفت: «از موضع روسیه درباره جنگ و تحریم‌ها تشکر می‌کنیم. می‌توانیم در برابر یک‌جانبه‌گرایی آمریکا مقاومت کنیم. آمریکا حق ندارد تحریم اعمال کند و قوانین بین‌المللی را نقض کند.»
پزشکیان گفت: «حمله آمریکا هیچ توجیه منطقی نداشت.»
@
VahidOnLive
ولادیمیر پوتین، گفت مسکو از هر فرصتی برای دیدار، گفتگو و انجام رایزنی با تهران استفاده می‌کند.
پوتین با ابراز خرسندی از دیدار دوباره با پزشکیان گفت روابط دوستانه روسیه و ایران در همه زمینه‌ها به‌طور باثبات در حال توسعه است و این روابط مطابق با «متن و روح پیمان مشارکت جامع راهبردی» میان دو کشور پیش می‌رود.
@
VahidOOnLine
عباس عراقچی در پایان روز نخست نشست سران شانگهای در قرقیزستان گفت: «یکی از موضوعات مطرح‌شده در تمامی دیدارها، تفاهم‌نامه اسلام‌آباد بود.»
عباس عراقچی گفت «آمریکا باید به تعهدات خود بازگردد و به مفاد یادداشت تفاهم پایبند باشد؛ پس از آن می‌توانیم از این وضعیت خارج شویم چون همه کشورها دغدغه دارند که جنگ هرچه سریع‌تر خاتمه پیدا کند.»
مسعود پزشکیان امروز در حاشیه نشست شانگهای با رهبران هند، پاکستان و آذربایجان به طور جداگانه دیدار کرد.
شی جین‌پینگ، رئیس‌جمهور چین، ولادیمیر پوتین، رئیس‌جمهور روسیه، مسعود پزشکیان و بیش از ۱۲ رهبر دیگر امروز در قرقیزستان گرد هم آمده‌اند تا در نشست دو روزه سازمان همکاری شانگهای شرکت کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/VahidOnline/78128" target="_blank">📅 18:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78127">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sxtjyfdcxBcQsloTQ5xbdn6Vh29cUZoYS5E9yqhcLJ5a7OoD14kIh2RPLohD-w4v3LNxREkZz7QVk7oo098hsP5wnIQG-01uV5e8UWqt_e2jBgMAll3L5-Y_XWLYM9rCJO5K1WvyYDlJnzD4ARNJMW7ynxhbjs4wsJEQDfsdR_mqBSwYSqxMFHZjfebCK0aOsctXSTnpmyF66dzGFsWhtaMZiYICQCCQTxhJq9jvbei1UW8aj16WcHvTjhcx44_wnlaH5ueAWHRa1kPlv-AsClZc9nomL5RiYxA2Nsf8GCd2f4hCSoqBh4Q6LVZStIcZ5xh70WAHNN9C336vcRjbZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر بختیاری، پدر پویا بختیاری از جان‌باختگان اعتراضات آبان ۱۳۹۸، از سوی شعبه اول دادگاه انقلاب بندرعباس در مجموع به ۱۰ سال حبس تعزیری دیگر محکوم شده است.
براساس حکم صادرشده، او با اتهام «فعالیت تبلیغی علیه نظام جمهوری اسلامی از طریق هم‌سویی رسانه‌ای با معاندان» به یک سال حبس، با اتهام «تحریک مردم به جنگ و کشتار با یکدیگر به قصد برهم‌زدن امنیت کشور» به چهار سال حبس و با اتهام «ارسال فیلم به شبکه‌های مجازی بیگانه برخلاف امنیت ملی» به پنج سال زندان محکوم شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 174K · <a href="https://t.me/VahidOnline/78127" target="_blank">📅 17:51 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CqaIBeE1Dur8L3TGbQqDb-9xWBtmrRD77s50qtF8bgM8nPyv8nyAypjwav9Pz1FDlWRJlMT5oJPRX2FGYxwmUSEF1czCdtkka1MszdhkiK5HAui3YtvtBEHirs-G2Eups6l2S4djV5pHNro5cqTg9NCkEGa3NQrvPnAaFjX3CmI3xsNvAHMCGh3z9TpaxS3zjD5A1EU-Y6jAZkTrvqfYmE62tbmCPm68cVtST2NEjKUSbFau6ZBm_2R86XSMqQtGNcsdKvtW559ApKWG3yrZ-PegEy87AKwBn3HmQBXv6uJs6M3B6RPu0UBHwoMqSYVQsTv8EUQw8CykYhbtJyN7Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=sYRlCCk_UTQ8AUL3wiMv3oJ82qQY8H7jLrSLebbrbedFW-1_MZoqyzv57XNfclE8yHiwYtmQtPG4KzmghA30lNqoRrL5xxuVVw1TWx9FvOAG3WcvC8FVplJDnzbAy80Gzazb3wcwbMUsed6oime9m1u7kaCybOTWUSqX78vttpbrgNbUDMKvfHVulFuyNkMl4weJSvjgGHpEAkgLTaedgntPZZt0tXsrhNIrN04DjjG1t9q0pGM9krGGqrsncp5_7jtbIuVTmp5pmffaEYsPjJelpD6OP02RRIQsIvCeExjIZHbN42KXIGtCTxfDipwsg6qgYjxn3vkg5Wly41mQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/88d499b7a4.mp4?token=sYRlCCk_UTQ8AUL3wiMv3oJ82qQY8H7jLrSLebbrbedFW-1_MZoqyzv57XNfclE8yHiwYtmQtPG4KzmghA30lNqoRrL5xxuVVw1TWx9FvOAG3WcvC8FVplJDnzbAy80Gzazb3wcwbMUsed6oime9m1u7kaCybOTWUSqX78vttpbrgNbUDMKvfHVulFuyNkMl4weJSvjgGHpEAkgLTaedgntPZZt0tXsrhNIrN04DjjG1t9q0pGM9krGGqrsncp5_7jtbIuVTmp5pmffaEYsPjJelpD6OP02RRIQsIvCeExjIZHbN42KXIGtCTxfDipwsg6qgYjxn3vkg5Wly41mQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی زارعی دوز دره سی، زندانی سیاسی و یکی از آسیب دیدگان اعتراضات سراسری ۱۴۰۱ که در زندان قزلحصار کرج محبوس است، توسط شعبه ۲۳ دادگاه انقلاب تهران از بابت اتهام «افساد فی‌الارض» به اعدام محکوم شده است.
بر اساس اطلاعات دریافتی هرانا، حکم اعدام آقای زارعی دوزدره‌سی از بابت اتهام «افساد فی‌الارض از طریق اقدام گسترده در انجام فعالیت‌های سیاسی، ایجاد انعکاس خسارت تصنعی، تهیه اخبار کذب، تبلیغ علیه نظام، برهم زدن امنیت و ورود و خروج غیرمجاز به کشور» صادر شده است. حکم مذکور در تاریخ 1شهریورماه ۱۴۰۵ به وی ابلاغ شده است.
آقای زارعی دوزدره‌سی که پیش از این در آلمان به سر می‌برد، در تاریخ ۸ اردیبهشت‌ماه ۱۴۰۵، پس از ورود به ایران توسط مأموران اداره اطلاعات بازداشت شد.
پرونده وی در مرحله تحقیقات مقدماتی در شعبه سوم بازپرسی دادسرای ناحیه ۳۳ تهران، موسوم به دادسرای امنیت، مورد رسیدگی قرار گرفت.
وی نهایتا در تاریخ ۹ تیرماه همان سال به زندان قزلحصار کرج منتقل شد. این زندانی در حال حاضر در واحد سه، بند ۳۷ این زندان نگهداری می‌شود.
علی زارعی دوزدره‌سی، حدودا ۲۷ ساله و ساکن تهران در جریان اعتراضات سراسری سال ۱۴۰۱ یکی از چشمانش با شلیک گلوله ساچمه ای آسیب دیده بود. وی پیش از این نیز سابقه بازداشت و برخورد قضایی را داشته است.
hra_news
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 248K · <a href="https://t.me/VahidOnline/78123" target="_blank">📅 17:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bccWKMZpKqmMYjCTSDnYabOY2N8EvQtgFy-J0GlnWqL4saIG5FonFnoX6SI9hd89AwGi8MIX9SWvV5PE8-WXawpjjJ-_TQ074FFoKrXtih_QnThQhgFXWmxqm7iFzAkDzF3nDnR0G-d3jPKuyUQZo_oDcbv7ceAJOyXbm51_pVn9XnnqgtS5vd-7BPgPUIK5jZcCmeB9RIza4SNfF9o4AUR41TJ8l_jnE_mbdb1L1ZBgzEOQ4nw9DW2JY7XeuQ6bxP8gxhu2FQa90rkf-sGiPRjO_s39sVn_OkULMsiGMkG_bccG26i6G8MssBBO9SwLKsnE5qfXq_mToFD0wmcC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک نفتکش در تنگه هرمز «هدف قرار گرفته است.»
براساس این گزارش، این نفتکش «هنگام عبور از تنگه هرمز و خروج از آن» هدف قرار گرفته است.
سازمان عملیات تجارت دریایی بریتانیا گفته این حادثه در فاصله ۳۱ کیلومتری شرق منطقه خصب عمان، «هدف اصابت سه پرتابه ناشناس قرار گرفته است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/78122" target="_blank">📅 03:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/78121" target="_blank">📅 00:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/l2G-5tkdbYh_wpOdwW_LD_4JB_mNwD_UcOMrRhfvv27JUu5YDzpoSmxWD1IOM4FT7XkfHl-Xb_EvQYpUyLyVldn4BjDJTedmM6scQeA4wzknqoQLIgjsdRnbhqS-3RLla0ZyMCYRrNsoq7qNzWxpkfgw7yrzNJjUAycsmCAx14kx-V7M3XEw6scoy36GO8IqG4hbO0kIgFxf9_AvaX71yovpw6jjIyg1QlRJzWxEB9TdctwXnrlHOZNnOSvxXiBpGP5odDnRCilHI5eB2ZEn3kaxSSRafzNpikIjqUx3_4odd2YHSYTa1-y_i9-454z4rrOx-FNUjcghmMYKHr0Phw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس به نقل از سه مقام آمریکایی گزارش داد دونالد ترامپ، رییس‌جمهور آمریکا، و مشاوران ارشدش در حال بررسی انجام حملات محدود در تنگه هرمز برای جلوگیری از بازسازی توانمندی‌های راداری و موشکی جمهوری اسلامی جهت حمله به کشتی‌ها هستند.
بر اساس این گزارش، این طرح که طی هفته گذشته توسط فرماندهی مرکزی آمریکا تهیه و از سوی وزیر جنگ، پیت هگست، حمایت شده بود، پیش از تبادل آتش این آخر هفته با ایران به تایید ترامپ نرسیده بود. اما او ممکن است پس از تشدید جدید تنش‌ها با آن موافقت کند.
یکی از مقامات آمریکایی گفت ایده اصلی این طرح، کاهش خطر حملات تهران به نفتکش‌ها، شناورهای نیروی دریایی آمریکا و هواپیماهای نیروی هوایی آمریکا است؛ به گفته این مقام، هدف «کوتاه کردن چمن» است.
یکی از مقامات کاخ سفید گفت: «رییس‌جمهور همه گزینه‌ها را در اختیار دارد. ایرانی‌ها می‌خواهند توافق کنند، اما همیشه یک روز دیر و یک دلار کم می‌آورند.»
ترامپ عصر دوشنبه به فاکس‌نیوز گفت که آمریکا به حملات جمهوری پاسخ خواهد داد و «آنها را به‌شدت هدف قرار خواهد داد».
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 338K · <a href="https://t.me/VahidOnline/78120" target="_blank">📅 22:55 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZfeP2idyf3v9VJtLKwy_wQcI30n0JKMtWsZSsTSk_6jIDAhyhui2qcYqRNqABtF77cUaFKm8U_IHLY7vuPrI2AHOSlPJTHIMlh8JYLMoPBtyEjpVl-IFkEPOrTtghe0YtQmOJaG191Ub_XIKV-DzCcF5sVPIms_8nyBqbltjtDqXTQeRY9eltD_wtgcMF4PW_kaqnZv3gLTAbI2A2-TSbHBpYt-v3b_xjmUf-P4_anY7uU4MFR2nVwPXwq1jTVmE2_nB3-lF_RJTWCosuXaThlHDcoeLa9nj6KEK6GmEkroe0zOeTNFAyPQpP5fyS4khldJ3iJTsJECKSOqUYK5NOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستادکل نیروهای مسلح جمهوری اسلامی روز دوشنبه در بیانیه‌ای مدعی شد که ایالات متحده از آسمان یا خاک برخی کشورهای خاورمیانه برای استفاده از ایران استفاده می‌کند و هشدار داد آنها را هدف قرار خواهد داد.
این بیانیه ساعاتی بعد از آن منتشر شد که دونالد ترامپ، رئیس‌جمهور آمریکا، اعلام کرد ارتش این کشور به حمله شب گذشته ایران به نیروهای آمریکایی در اردن، ایران را به شدت هدف حملات انتقام‌جویانه قرار خواهد داد.
ستادکل نیروهای مسلح ایران در بیانیه خود گفته است «ضمن احترام به حاکمیت ملی همسایگان»، در صورت ادامه حملات آمریکا، نیروهای نظامی جمهوری اسلامی «پاسخی سنگین‌تر» از حملات شب گذشته خواهد داد.
ارتش آمریکا اعلام کرد شامگاه یکشنبه «نیروهای مین‌گذار سپاه» در جزیره لارک را هدف قرار داده است. در پی این حمله، سپاه پاسداران از حمله موشکی به دو پایگاه نظامی در اردن خبر داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 325K · <a href="https://t.me/VahidOnline/78119" target="_blank">📅 22:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PjrXXcpMs5p1116topBfBpDa7RSHuvO5igu_zXLnVi5vHWxFOdtwemDMPSUzm5Dg5mtcinszPeaGbTonGkHGLinGzkCe7u7BLpiPbTmvitgwO7x6M2AdpbQJuDmqdWpsex8yUmHLgEUxXH9yFqYo12c_vuHZcVtSAYys6hJQaPrSjrudmhLqtFZBYZr-vLuzI8GbkJAf8UnYuBBMAF1V2JBF_H5K11lJChK0CxCf0qWUgSLg6DJmpLDmyod_XqCgwB3s3SO8bMkU8yoFSzXTQjIWSdVcP3XLTajEr_1DGQCnRSLP98miYSm056QUqmR_pBRXni5rwc7y9Dr_S9rekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه عربستان سعودی روز دوشنبه نهم شهریور در بیانیه‌ای اعلام کرد که کشور‌های عربستان سعودی، ترکیه و پاکستان توافق کرده‌اند در قالب «پیمان دفاعی مشترک مکه»، دبیرخانه‌ای را در عربستان سعودی تاسیس کنند.
بر اساس این بیانیه، ریاست این دبیرخانه در سه سال نخست بر عهده دبیرکلی از کشور پاکستان خواهد بود.
در همین راستا، وزارت امور خارجه ترکیه نیز اعلام کرد که تنظیم سازوکارهایی برای پیوستن سایر کشورها به این پیمان، در دست بررسی است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/78118" target="_blank">📅 19:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=DNTWUiTrRzSXBMlNiFBfAjRbOm-n7uxEjFmNe7TDQA-NZykUB7hp40Fu4o7ZEbNe4DQNA-OG0fZqqGoTMxkedH9YTBbzdBD5fOOuKpFf-Oq-k-ipfM0efpiY649ShnzmujkAqHVPwFzg_PVInRjoxBqbFNr60zqcFz-_tghTmpSMKwnS04_R6OVFwzfarvHn6SbhQa7MoHbDvsTY7kOrGflUOokMGba0S6BcynnJYNRi5Byh4d14uf-AJ4iYFeJ43qoD7GgCbA660rntsnncrDDZ-QS-K47WJJtrUDB9eDT569E7Xej1cWjsQERWqgKpscSTOXoKgR5zhm2pmULDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b1780d8686.mp4?token=DNTWUiTrRzSXBMlNiFBfAjRbOm-n7uxEjFmNe7TDQA-NZykUB7hp40Fu4o7ZEbNe4DQNA-OG0fZqqGoTMxkedH9YTBbzdBD5fOOuKpFf-Oq-k-ipfM0efpiY649ShnzmujkAqHVPwFzg_PVInRjoxBqbFNr60zqcFz-_tghTmpSMKwnS04_R6OVFwzfarvHn6SbhQa7MoHbDvsTY7kOrGflUOokMGba0S6BcynnJYNRi5Byh4d14uf-AJ4iYFeJ43qoD7GgCbA660rntsnncrDDZ-QS-K47WJJtrUDB9eDT569E7Xej1cWjsQERWqgKpscSTOXoKgR5zhm2pmULDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا ویدیوهایی ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.  ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»  این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر…</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/78117" target="_blank">📅 19:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=j0fDb766T_wfYjDZIkLaestrNXDEFgF1_4bJyRDMWO4W-fgzz1KPejcNsgHGlaCi1ught0stGPwWcR5A0Wosw0-PvtfLkyZwUenULukqIIw8m_Lq-md1WtZTMoyiQfO1CgFC7wF3j1WmIk5GcDbQNE4CbOlyQUNV3uwAu8vS6T2i4C2_jxQ85_xuwa8z39m3Rc5R_ZaxUZSAnzNDBP7J6_kPCWcKtb67xLgcJmVDDVstIb_JzeKztgygynGriOa4EwqJdVYB6lW9Ry3GUAFeJR5sh7Ff4llHhPVSdDkSz_HmmRQuQKcd1WVmRkBuOfBxBhOo8UchyRNVkytjRdVDeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/20878b3cf5.mp4?token=j0fDb766T_wfYjDZIkLaestrNXDEFgF1_4bJyRDMWO4W-fgzz1KPejcNsgHGlaCi1ught0stGPwWcR5A0Wosw0-PvtfLkyZwUenULukqIIw8m_Lq-md1WtZTMoyiQfO1CgFC7wF3j1WmIk5GcDbQNE4CbOlyQUNV3uwAu8vS6T2i4C2_jxQ85_xuwa8z39m3Rc5R_ZaxUZSAnzNDBP7J6_kPCWcKtb67xLgcJmVDDVstIb_JzeKztgygynGriOa4EwqJdVYB6lW9Ry3GUAFeJR5sh7Ff4llHhPVSdDkSz_HmmRQuQKcd1WVmRkBuOfBxBhOo8UchyRNVkytjRdVDeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، روز دوشنبه نهم شهریور ماه در حاشیه نشست «جی ۲۰» در اشویل آمریکا گفت واشنگتن به اعمال فشار اقتصادی بر تهران ادامه خواهد داد و ممکن است نتایج این فشار طی هفته‌ها یا ماه‌های آینده نمایان شود.
بسنت در پاسخ به پرسشی درباره زمان احتمالی فروپاشی اقتصاد ایران گفت: « مسئله این است که ما محاصره را داریم و به اعمال فشار ادامه خواهیم داد. ما همین حالا گفتگوهای بسیار خوبی در اینجا داشته‌ایم و فکر می‌کنم این می‌تواند طی هفته‌ها یا ماه‌ها رخ دهد.»
وزیر خزانه‌داری آمریکا افزود: «اقتصاد لزوما نباید فروبپاشد؛ فقط باید حکومت ایران به خود بیاید.»
این مقام آمریکایی افزود بسنت در حاشیه نشست گروه ۲۰ با همتایان خود دیدار خواهد کرد و برای افزایش فشار اقتصادی و منزوی کردن ایران تلاش خواهد کرد.
اسکات بسنت، در ادامه با اشاره به حمله ایران به پایگاه‌های نظامی آمریکا در اردن گفت: «به نظرم آنها به‌صورت نظامی دست به واکنش می‌زنند، چون از نظر اقتصادی در حال شکست خوردن هستند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 279K · <a href="https://t.me/VahidOnline/78116" target="_blank">📅 19:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=IMzOq5q8kMwyU9dgGxnlXG-qzvBSTRq2644J464_CAQ-73VFptekU7GQ0Iz7a4FAF_ZWoO3J0yDSKNajV5ItC0_raB0qmutLSwbMshGdufnjZTkKkn5-GHOCFS0UN2Qz64gbVglZ3Arho1gYCEG2rsLcOJZwHTWkILABLVBqXqXPo6wuE_yZ3cFlJjHM8Zg3icPjrcCfCzZnjv2ngRKWXn4e9ElUllmEIOY0pEh6145HqLunySu25e4O6rEkNwfGz3gx2LKiTkwQiRcfEw0Htzh6u67g9rZCNHpvWteShxpvPCKi0iN0WAY_DMdGssG6hNG79pIDlcftdRlW-hlj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a67dbde091.mp4?token=IMzOq5q8kMwyU9dgGxnlXG-qzvBSTRq2644J464_CAQ-73VFptekU7GQ0Iz7a4FAF_ZWoO3J0yDSKNajV5ItC0_raB0qmutLSwbMshGdufnjZTkKkn5-GHOCFS0UN2Qz64gbVglZ3Arho1gYCEG2rsLcOJZwHTWkILABLVBqXqXPo6wuE_yZ3cFlJjHM8Zg3icPjrcCfCzZnjv2ngRKWXn4e9ElUllmEIOY0pEh6145HqLunySu25e4O6rEkNwfGz3gx2LKiTkwQiRcfEw0Htzh6u67g9rZCNHpvWteShxpvPCKi0iN0WAY_DMdGssG6hNG79pIDlcftdRlW-hlj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز دوشنبه ۹ شهریور ۱۴۰۵، شماری از شهروندان جویای کار در شهرستان گچساران در اعتراض به روند استخدام نیرو در پالایشگاه لیشتر تجمع کردند.
در ویدیوی منتشرشده از این تجمع، تیراندازی نیروهای انتظامی برای متفرق‌کردن معترضان دیده می‌شود. برخی گزارش‌ها نیز از زخمی‌شدن یک نفر در جریان این تیراندازی حکایت دارد.
این تجمع در اعتراض به نحوه جذب و استخدام نیرو در پالایشگاه لیشتر برگزار شده است؛ پالایشگاهی که به‌تازگی افتتاح شده است.
@
VahidHeadline
نیروهای امنیتی و پلیس، جوانان عرب معترض به بیکاری در مقابل شرکت نیشکر «دعبل خزاعی» در اهواز را با ضرب‌وشتم و تیراندازی متفرق کرده‌اند.
در این ویدیو، مردی که در حال فیلم‌برداری است می‌گوید: «این جوانان همه گرسنه هستند، هیچ‌کس ما را استخدام نمی‌کند. هیچ‌کس برای ما ارزش نمی‌گذارد. هر کدام از آن‌ها با اسلحه کلاشینکوف به‌دنبال جوانان افتادند. ما کار می‌خواهیم. جوانان گرسنه هستند. ما هیچ آهی در بساط نداریم. ما کار می‌خواهیم.»
سازمان حقوق‌بشر «کارون» روز دوشنبه نهم‌شهریور۱۴۰۵ در گزارشی نوشته است که «جوانان و خانواده‌های معترض که به نمایندگی از ساکنان همجوار این شرکت دست به تجمع زده بودند، با طرح مطالبات خود اعلام کرده‌اند که شرکت نیشکر دعبل خزاعی در زمینی به مساحت حدود ۱۲ هزار هکتار فعالیت می‌کند که بخش قابل‌توجهی از این اراضی متعلق به منطقه و مردم بومی آن است. با این وجود و علی‌رغم حضور جوانان بومی دارای مدارک تحصیلی و تخصص‌های مختلف، مدیریت شرکت اولویت را به جذب نیروهای غیربومی داده و باعث شده تا جوانان منطقه همچنان از فرصت‌های اولیه اشتغال محروم بمانند.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78114" target="_blank">📅 19:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mo05x7aBudyhzpXRTpj5xNKNKESLya9oogWXSiIAKKqw7iUg2IUwU-oSIt2PkhOEybDvmdwuDKjaJsnhGKjSSdrbWevF0F6Vxsrma5I9PD-ljkpMkgA40jwP0mCGnxb6vWoCNOtQrUySk47B_VVRwQv7-FG90quc4Ndhy9-MdsWmjZaYmW-7YTa7_waRcIshT7AOfNNVB-XZx9yS94NTyVR5faUhKM5J0kHH9tNMIl-TGaaNDo2n4f0slmyQpLfYS8itPURCLKXtkhzY7kGCoBDw4ZYBMeXGPgDbDdm1_oVs2xSzFJgDlqpnkHdHfekaYweV0vfjD-5ZrS1SKwBkSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GgPH3UIp_APFpb5BH-RVCu8fBInHBD3NujX8RBkEsa76gbMlXkNlCLcymDGK_BvTYKISOkrvNZL-eBy0sBPeXmsa_YaWVXF-Qh6r5-6EMhk11t7tYhJgBmO9TBDnu4A5dkFXuTdq-FIe8vYXXZtT0IphUK6QehYlhAs6YcaLEvO8cLgPOKxOIKHHbQohf5KoEZQgTnwxJZOJxSnX-zSWSTkrAlbEuSKpaoRzvSvc5wnNE_Pn6tVT_hyrW6A_AvGpwGcg6zlKiSsPs5UjHa-BmE1-BQpZCWabmeF_bruVo11qpeR5PgPY3tCMJSiG33JxbiiQfYvdkn9BM3xp9QO5zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اژه‌ای معترضان را به برخورد قاطع‌تر تهدید کرد
در پی تشدید بحران اقتصادی و رسیدن دلار آمریکا به مرز ۲۱۰ هزار تومان، رئیس قوه قضائیه جمهوری اسلامی گفت این نهاد برای مجازات «عناصری که بخواهند امنیت کشور را مخدوش کنند، قاطع‌تر از همیشه است».
این تهدید پس از آن صورت گرفته است که دستگاه‌های حکومتی بروز اعتراضات مردمی را پیش‌بینی کردند.
غلامحسین محسنی اژه‌ای افزود تحکیم امنیت و مقابله قاطع با عناصر ضدامنیتی از مقولاتی است که مردم و مسئولان درباره آن اتفاق‌نظر دارند.
این رویکرد با پیام مکتوب مجتبی خامنه‌ای در هفته دولت تشدید شده است.
خامنه‌ای در این پیام اعلام کرد: «قاطعانه اعلام می‌کنم که ارتکاب هر آنچه به ضرر انسجام اجتماعی باشد، ممنوع است.»
@
VahidHeadline
خبرگزاری فارس، وابسته به سپاه پاسداران، با انتشار گزارشی به حضور «شماری از دانشجویان زن بدون حجاب اجباری» در جلسه رییس سازمان امور دانشجویان و مشاور وزیر علوم اعتراض کرد و خواستار «واکنش قاطع و فوری» وزارت علوم و واکنش نهادهای امنیتی و دستگاه‌های قضایی شد.
به نوشته فارس، انتشار تصاویر جلسه‌ای با حضور رییس سازمان امور دانشجویان، مشاور وزیر علوم و شماری از اعضای شوراهای صنفی دانشگاه‌ها که در آن تعدادی از دانشجویان زن بدون حجاب اجباری حضور داشتند، «با اعتراض گروهی از استادان و دانشجویان» مواجه شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 278K · <a href="https://t.me/VahidOnline/78112" target="_blank">📅 17:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UfPkWAzffcnP0oqG91zoIxLAIT7DlHnveI3IMBNaVx6b7D08xLKFOT9G8hcvsHNxCwAHyNz7DWPfxsnm-qckXEB0GuyOD47ub3xPe8AV6VESI-I1VdmYr_s3Iz1V_o25H5dedwleldrCK4EMiDGXxFSTL3u5vEYt35aCcTuyToY9R9Hoxz-LutZp22r63dIdlxFTpvjAILcVYg4y5KBqVPUlUCd9Ah7gw88_VHqLPFzNtelqDefDDOufVXbP0_ByaNLsWnbudylBUgfija-X8C2KJFlVU1jvtGaPA0CgwoPwBubhznpvvHFWhf5-Fak2lqOPovgDQgz9vjHWZwLFlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتحادیه اروپا روز دوشنبه اعلام کرد که به همکاری با ایالات متحده و سایر شرکای بین‌المللی و گروه هفت «برای حفظ فشار بر ایران و کمک به کاهش تنش و ثبات منطقه‌ای» ادامه خواهد داد.
در این بیانیه آمده است:‌ «اتحادیه اروپا از تلاش‌ها برای اطمینان از اینکه ایران فعالیت‌های بی‌ثبات‌کننده خود را متوقف کند و با حسن نیت در مذاکرات صلح شرکت کند، از جمله از طریق فشار اقتصادی بیشتر، شامل عملیات طرد اقتصادی به رهبری ایالات متحده، استقبال می‌کند.»
«عملیات طرد اقتصادی» عنوانی است که مقام‌های دولت آمریکا بر برنامه فشار اقتصادی تازه بر جمهوری اسلامی گذاشته‌اند.
بیانیه اتحادیه اروپا در آستانه آغاز نشست گروه ۲۰ به میزبانی آمریکا صادر شده است.
اسکات بسنت، وزیر خزانه‌داری آمریکا به خبرگزاری رویترز گفته است در این نشست از وزیران دارایی و روسای بانک‌های مرکزی کشورهای جهان خواهد خواست تا روابط اقتصادی‌شان را با ایران قطع کنند؛ در غیر این صورت با تحریم‌های ثانویه آمریکا روبه‌رو خواهند شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/78111" target="_blank">📅 17:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TtwssqDYkmLdHqc3t3SQPBrVEHmRTRGEgRCblA99HzQwxgTE3fPsQtMplYVblLAn8bY1Q_7hwPY3_Z6_VFqnFuYknv2fFV9FrckveSnk2as-a8IznzRH-WjVyYK071MqZJ5rPUeQsN-ooxQjLgI2Q10V5PAdkfhPFDxJaiDW1XaMXLTGekwDDVm6RR02KDzfY7C7J-51ABwIQ4XZazmicCJ0gnsOa1Bj9sTrNXVavT1_I3o8jTkYoNtxQd7rYAdNXb8Bg51BkJJkVvqU2Y_Y1qaoPqlXCL943t1sZ4r6Y0COYi2kKye-GhcD_8Rl7Df048CMghj5F9POAHIjc0PKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه روند نزولی ارزش پول ملی در ایران، قیمت دلار آمریکا دوشنبه، نهم شهریور از ۲۱۰ هزار تومان عبور کرد.
همزمان پوند بریتانیا از ۲۸۴ هزار تومان عبور کرد و یورو نیز به مرز ۲۴۳ هزار تومان رسید. قیمت هر سکه طلای طرح جدید، موسوم به «امامی» نیز از ۲۲۳ میلیون تومان فراتر رفت.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 268K · <a href="https://t.me/VahidOnline/78110" target="_blank">📅 17:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c5e_O1rhNHTaIJXH1yz8Q4OTuisGXejI0ASu6WnlDdlVUnElsTgpkclFxvwqHjL1CXGvmLTQSpQzuAyQWa4N97YM0Xv1l67V_R45qfPn1Cxg8qvqWyiTfm56QtQHBVnJI9sdR1RcdNDFEuNyUJwCtFiGQhKDANp4ppKqziLK1pVmT7SiiAVVJSow0L7jYGbtvinXJIduD5VjUjqm_DHpHdud5tkrc2ozt5BLvddPw7EI_FL6_Cze-G9v1RSyzvN9UBJERCD8HNuXh6g2n6XKuclf3tQwy4aBFFrEua3hixEdSoygh4xSIemQKSxJCr5Xm64OmsCpxp_-vVVLmxAVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست سنتکام:
🚫
ادعا:
سپاه پاسداران انقلاب اسلامی ایران (IRGC) ادعا می‌کند که یک ابرنفتکش هنگام عبور از مسیر جنوبی تنگه هرمز با دو مین برخورد کرده و کاملاً متوقف شده است. این ادعا
نادرست است.
✅
واقعیت:
هیچ کشتی‌ای در تنگه هرمز با مین برخورد نکرده است. این نیز یکی دیگر از تلاش‌های سپاه پاسداران برای ارعاب کشتیرانی تجاری منطقه از طریق انتشار اطلاعات نادرست است.
CENTCOM
📡
@VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/78109" target="_blank">📅 16:56 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78108" target="_blank">📅 16:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EEdxqlUyCh5fpGcPK5yXeBdR7dNPocFFdsnCgd_1BZmv8bayfD5oeJPQAZCAOBPHArmcIbAisTCpvujv_4l1laYAPUG3IKGXcByO3O-Jm-Eh7dLD_R7mC41SDO1GJTl5bMnQMt9_KRP9svZpWGCCLuuOf9mWJrMQ8EqwjLifqH3f0zxTH7k-eMuK5hVPMd-wniCucCjppKPf6AJooIIOwFEZ4NGYbyBjUKEOAP9aW4TEr3mWECIx1TN1iXrtZV-OfV_ZxHSgHtCYajfaOvEZSSZz-NhxGJk-xfjLLv_ICHd6O-QHnGiKjtx9gCuwkSo33PQy9COwKOuKPMxOlYqSPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز دوشنبه نهم شهریور، در شبکه اجتماعی «تروث سوشال»، جمهوری اسلامی ایران را رسما یک «کشور شکست‌خورده» خواند و خواستار محاکمه بین‌المللی رهبران آن شد.
ترامپ وضعیت ساختارهای اقتصادی و نظامی ایران را «فروپاشی کامل» توصیف کرد و نوشت: «ایران دیگر نه نیروی دریایی دارد و نه نیروی هوایی؛ ارز آن‌ها از دست رفته، حقوق سربازان و نیروهای پلیس پرداخت نمی‌شود و تورم به ۳۰۰ درصد رسیده است. رهبری آن‌ها در آشفتگی مطلق است و توانایی اداره کشور را ندارد.»
رئیس‌جمهوری آمریکا در ادامه با متهم کردن تهران به سرکوب خونین اعتراضات داخلی افزود: «تنها کاری که آن‌ها بلدند کشتار معترضان خود است که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است. مقامات تهران باید به اتهام ارتکاب جنایات جنگی علیه بشریت محاکمه شوند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 245K · <a href="https://t.me/VahidOnline/78107" target="_blank">📅 16:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/juaNkx1fg8VwJigsZP_YfUkf5KFaiC4N5Fq9x22ckAmmiS0QnOpJaNIZfDkY1xkZHrY_Aj6WTHq93Wh7rlRrhSL94KsDzLAx_Kuyhf0tipTdUdb-gPatXcJfcE6TyGSC-IUU7IYAjqPPQV_udHKxVUU1toqb3J_AqifCNplvsbiwYlFBqj5qr9Gk4p2ekhNDb8lfsxsiiqKassCGfUiFRUicGYCSyaZJ4oWS81D1P81GCDDN3u7kIrA5nEd1357ynZpK8a9dy5Y4FGlB8qVqiDm-MJAOBewFx1P-oSyNRHWuxRJu_mCsUupqiNsJmYChU7LRZ79u8uVjgOR_l4cwCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست عراقچی:
نتانیاهو در عبری آشکارا پُز می‌دهد که دولت آمریکا را فریب داده و به جنگ با ایران، به نیابت از اسرائیل، کشانده است.
نتانیاهو صراحتاً با خنده می‌گوید که چگونه با ۱۰۰۰ ساعت حضور در شبکه‌های تلویزیونی آمریکا، بر آمریکا «تأثیر گذاشته» است.
اما به انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار.
araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 232K · <a href="https://t.me/VahidOnline/78106" target="_blank">📅 16:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=NqtFa0AcgQ8qt16P7y5zJLL0xgVMFNuuomtQF4UBsVZrbLps6Wd3szO0Eoak2wRX1lNIYlkdVOYzu57c08Ymbbd-VPJzDTRr7gm-tfM3IIa93GNefry5RNCGXKoQhHNY1Io7FaQuPYIu9EbY-bJQVXdFKJ8pqCNxA8U7SlX2tZ-A5z9QbrdvNO7VNMNIrihnwrIXtu6LW4gCwpNomJK8ytUGib-dffr2i4Yp2ZubC12qdOUW6_wee4TXaQKP2CUkgOtb34srdfgEJHUpwg6cvqxaSQCHEDlQP4HtOcDgM5gGuy6G3l5TZfIXYC34aGNBEbOcHN1zkkx5XiGUZ8YWnA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0006ca2103.mp4?token=NqtFa0AcgQ8qt16P7y5zJLL0xgVMFNuuomtQF4UBsVZrbLps6Wd3szO0Eoak2wRX1lNIYlkdVOYzu57c08Ymbbd-VPJzDTRr7gm-tfM3IIa93GNefry5RNCGXKoQhHNY1Io7FaQuPYIu9EbY-bJQVXdFKJ8pqCNxA8U7SlX2tZ-A5z9QbrdvNO7VNMNIrihnwrIXtu6LW4gCwpNomJK8ytUGib-dffr2i4Yp2ZubC12qdOUW6_wee4TXaQKP2CUkgOtb34srdfgEJHUpwg6cvqxaSQCHEDlQP4HtOcDgM5gGuy6G3l5TZfIXYC34aGNBEbOcHN1zkkx5XiGUZ8YWnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزرای خارجه و دفاع ترکیه، عربستان و پاکستان همراه با فرماندهان نظامی سه کشور روز یکشنبه نهم شهریور در استانبول اولین نشست پیمان دفاعی خود موسوم به پیمان مکه را برگزار کردند.
عربستان سعودی، پاکستان و ترکیه روز جمعه ۱۶ مرداد این توافق را در شهر مکه امضا کردند.
بر اساس بیانیه سه کشور، حمله مسلحانه به هر یک از آنها به‌منزله حمله به همه اعضا تلقی خواهد شد؛ اصلی که شباهت آشکاری با ماده ۵ پیمان آتلانتیک شمالی، ناتو، دارد.
هاکان فیدان روز شنبه ۱۷ مرداد در گفت‌وگو با خبرگزاری دولتی آناتولی توضیح داد که ائتلاف جدید علیه ایران یا هیچ کشور دیگری شکل نگرفته و هدف از آن، ارائه یک تعهد کلی برای حمایت از امنیت سه کشور عضو است.
روز یکشنبه گزارش‌هایی از احتمال پیوستن هفت کشور عربی دیگر به این پیمان منتشر شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 235K · <a href="https://t.me/VahidOnline/78105" target="_blank">📅 16:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dLrBfgAZfEVC2S0zkM4PVv_VgQmyYn2Z20wPPZm_GLPFOdSRkqG0ogS0VXnjbUj11H0yYj_O1diQbv2012yYm_WM5Rj4i45gstAiXbLM5TaUAbAUba9XNZwVVgAXo2SmChYsTjJLjEdJAMpyobPq2v9Mp4lo905iG3Bhz8_hJkha9tTk8PU9XuI7Pb1CPgHxekNjHnD9REwpk_9kuOSV7gYKMzNoAKj2c4-BUYJ4bgZf71bmPC8mpKqcpSj3jcAiwiTUoKfwPWM1Epu-kRoOZ6x2TtcA1WWaU47Yj6UqM233baj28jomC4nLom4S1eDFrExxHSOUhTkrqGh-nCOEQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/XVpLCp67MP1uqQ2WrxI_EXibXIr-t_Jacxx4lSUpQw1YK3PmUx9ENrHSMmTLTInRcafAO2gEkbJOI43X0so1WajfxsGOdUWwuoljFMYu9vtzfKyMFpgB6o3hhRyHQlduhzuJVhMbr5tCUEKG8jg3f0dabL7v6Zy_pmAtjVftGDgki8KmOGZrgrFTKgkwO6QkkY-uxDandpnKhtYg8MW9nAEYJhLY3p-hKAKPRV7MG6Mx6lLRJjntfl2DXZaMGsHLURcPHJleLBwEbjuYoEsmOHugfP4IAeFnXUNkpcpsLznLwDd-xW4KBI7LrtLaYTsZ-sb5lWnHEe7LeUlKb50G-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وزارت دفاع امارات متحده عربی پیش از ظهر دوشنبه ۹ شهریورماه با صدور بیانیه‌ای گزارش‌ رسانه‌ها مبنی بر هدف قرار گرفتن پایگاه هوایی المنهاد با «موشک» را تکذیب کرد.
ارتش جمهوری اسلامی ایران ساعاتی پیش از حمله «پهپادی» به این پایگاه آمریکا در خاک امارات خبر داده بود.
در بیانیه وزارت دفاع امارات آمده است: «نیروهای مسلح همچنان در آمادگی بالایی برای پاسخ به هرگونه تهدید احتمالی هستند، به گونه‌ای که حاکمیت، امنیت و ثبات امارات متحده عربی را حفظ کند.»
@
VahidOOnLine
پیش‌تر:
روابط عمومی ارتش با انتشار ویدیویی از شلیک پهپادها نوشت که در پاسخ به کشته شدن جمعی از نیروهای سپاه و غیرنظامیان در جریان حمله نیمه‌شب آمریکا به جزیره لارک،  «محل های استقرار بالگردها و نیروهای» در پایگاه المنهاد امارات «با شلیک دهها پهپاد انهدامی، هدف قرار گرفته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 258K · <a href="https://t.me/VahidOnline/78103" target="_blank">📅 16:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Y0gxj8D8LVcFfmqc3EpYmOj-YWlQxkI0FhlqOWO12Ec55uaBUY3rDKZAvQPNM8BXzrgK3dgrLdX5ZMKFS44aiiLoLD1QWB4T7VT6iVTS-5ZAI_7vTuQ4cM5q34DwV2lk0lhK7pvFX6xLV5kHjYtyqMflJTN5FlfeItgReq6W3rVj2iBcyEZiUvR9-6lp8Dt8WGwryEH3CD96htjh9Cc9v02z0FAr3uAZnDVAaFZXH4w8NWrhvXXBVT_nhIwZR7lLFocDVYi9WABkWN65Slg-e-C1mSAwobUauLJLzgKXiMvrGWkKH-D0_z1I36fv7Gh-9s9UaV2qbfBxpO29YvWluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام درفشان، وکیل، روز دوشنبه خبر داد که حکم اعدام موکل او،‌ علی‌اصغر پیغمبری، از معترضان دی‌ماه ۱۴۰۴، در دیوان عالی کشور تأیید شده است.
درفشان به سایت خبری امتداد گفت: «حکم اعدام علی‌اصغر پیغمبری پیشتر از سوی دادگاه انقلاب تهران و با استناد به قانون تشدید مجازات جاسوسی و همکاری با رژیم صهیونیستی صادر شده بود.»
این در حالی است که به گفته این وکیل دعاوی «هیچ‌گونه ارتباط سازمانی یا ارتباط دیگری، به هیچ نحو، میان موکل و هیچ‌یک از گروه‌های متخاصم وجود نداشته» و پیغمبری تنها در اعتراضات حضور داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78102" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TivPYwiOmXfYLACA5sGaDkArUzKovRrUydoXkN9CDhcBU3HK0cwoKRnvmcNVeLS7KxpfU59I7imOfUYFXp-xGmSNl4t20_iu4H3JDRd0PwWlpL1_zVncbrwXtOqyk4LR380rGuj38wuKmng64pxpBFmtKfv6ZhGOiifjRozl3_71tn6noXJBqbdGMaEsyYL8iBNE-IhLIiyaV0YUqFk7dju7zU6wUIlysI-lpIBLlsC5AaSDNGtalu2R0c6qYwaT_uN91K3mcfU_lKku3b5h-ErVyIB8WgHtJy52CUTLq-OAO7I15m3CVvn-S8MnEaJ3mdP2vaGDBLffIVAgb3UR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه پاسداران روز دوشنبه در بیانیه‌ای که از تلویزیون حکومتی در جمهوری اسلامی منتشر شد از برخورد یک نفتکش غول‌پیکر با دو مین دریایی در تنگه هرمز خبر داد و گفت این نفتکش آتش گرفته و کاملا متوقف شده است.
سپاه در بیانیه‌اش مدعی شد که این نفتکش قصد داشته «به طور غیرقانونی» از بخش جنوبی تنگه هرمز عبور کند.
در پی جنگ آمریکا و اسرائیل با ایران، سپاه مدعی است که عبور کشتی‌ها از بخش جنوبی تنگه هرمز یعنی نزدیک به سواحل عمان غیرقانونی است. این ادعای ایران با قوانین بین‌المللی همخوانی ندارد.
در بیانیه نیروی دریایی سپاه به نام نفتکش و خدمه و مالکیت آن و زمان وقوع حادثه برای آن اشاره‌ای نشده است.
این نهاد نظامی به سایر کشتی‌های نظامی هم هشدار داده است که در صورت پیروی نکردن از «مقررات امنیتی» تنگه هرمز، «سرنوشتی جز این نخواهند داشت.»
بیانیه سپاه پس از وقوع درگیری‌های نظامی تازه آمریکا و ایران منتشر شده است.
اما تنها گزارشی که از بروز سانحه برای یک کشتی در تنگه هرمز خبر می‌دهد مربوط به ساعت‌ها پیش از حمله آمریکا به لارک است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 374K · <a href="https://t.me/VahidOnline/78101" target="_blank">📅 08:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=vwFpzSxMj2eJ1gDmtlXDnv6yjNpQd0kihNBW6REuw8TavQRFQuXMjBDqiwSi0miSrmH6Hh9oZFaXBsZRDu0yR0Wx3RddDyAl8HvCQjd8cGlXcJ4PFdaTC-RbvB7g-eyXC5JJDakOuD2yi2sgshUKuClOmFcwYDvexbL_TSdPKCeoasdW86UQR516-X02CxlRmq_M1eeJn9k8oR5HKphbrAYRBXTgJfYyXe0KiDGWeBWBTOW5Crgv56mXrdx4DimQeTxOhHagYBNiwdMNeD06EJHnZhHRA9QMkd6TQbU_n6OVVxC2YvIbio3lXZy8VKPNf5bcVCDtURD1LIHV5QUf7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41ed8a98ca.mp4?token=vwFpzSxMj2eJ1gDmtlXDnv6yjNpQd0kihNBW6REuw8TavQRFQuXMjBDqiwSi0miSrmH6Hh9oZFaXBsZRDu0yR0Wx3RddDyAl8HvCQjd8cGlXcJ4PFdaTC-RbvB7g-eyXC5JJDakOuD2yi2sgshUKuClOmFcwYDvexbL_TSdPKCeoasdW86UQR516-X02CxlRmq_M1eeJn9k8oR5HKphbrAYRBXTgJfYyXe0KiDGWeBWBTOW5Crgv56mXrdx4DimQeTxOhHagYBNiwdMNeD06EJHnZhHRA9QMkd6TQbU_n6OVVxC2YvIbio3lXZy8VKPNf5bcVCDtURD1LIHV5QUf7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا
ویدیو
ها
یی
ساخته شده با هوش مصنوعی را از حمله و انفجار در جزیره خارگ ایران در تروث سوشال منتشر کرد.
ترامپ نوشت: جزیره خارگ دارد با خاک یکسان می‌شود!!!»
این ویدیو ساعاتی پس از حمله سنتکام به دو پرتابگر موشک در جزیره لارک منتشر می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78100" target="_blank">📅 08:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tB-ZXQW7T7NMaw-aL3pMzORWpRx-aDRi8WlJbeHXG9wQSrIQJqrNmP4uq7jALFAxl-fuVBauLODAcB05DlK86uxcrzJso0viZQAt-FJhP7OZnCrDQ09E0aHKVDUakt_xE2Ldn0eAr3UfkDCQVQymNG0pWLXmHz3t8L0wYtY_b_07pTw1olrtzSkZREktAX8qq2TfOCpfQJ0X8qhfVN80Ywz8ngtKAsWRYyO0R368FH2wQn1VNnMWKYTKE-WWBYYBu-KMJBgL2VzXqRWfNCuOdBwul6ZOh2qr361EbefEFfB2keDNuPnyUwclS-Qtwc0EpeVsbGplSyZXFgI-5QvpRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین
تصویر دریافتی: اسکرین‌شاتی از وب‌سایت مرکز لرزه‌نگاری کشوری
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 371K · <a href="https://t.me/VahidOnline/78099" target="_blank">📅 07:40 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">لرزش زمین
بنا بر پیام‌های دریافتی از شرق تهران
سلام و درود همين الان زلزله اومد ٢/٣ ثانيه طول كشيد خونه لرزيد پنجره كوبيده شد من لواسان افجه ام ٧/٢٠ صبح
شرق تهران زلزله حس کردیم
تهرانپارس تهران زلزله شدید
چند ثانیه طول کشید
انقدر قابل حس بود ک من از خواب پریدم
زلزله تهران
یه تکون ناگهانی شدید
ادامه هم نداشت
داداش تهران همین الان لرزید
نمیدونم‌زلزله بود یا چیز دیگه
سمت جنوب غرب
تهران زلزله اومد شدیدهم بود ولی کوتاه.
زلزله اومد تهرانپارس لرزید
زلزله خیلی وحشتناک همین الان حکیمیه
سلامم تهرانپارس غربی لرزید
تهران چنددقیقه پیش زمین لرزید و زلزله اومد
زلزله بود؟؟؟
تهران زلزله
خواب بودم از خواب بیدار شدم، حداقل ۴ ریشتر بود
سلام. یه لرزش شدیدی سمت تهرانپارس تهران حس شد.
اقا وحید نارمک شرق تهران زلزله شد بد لرزید الان ساعت هفت پ بیست و سه دقیقه دوشنبه
سلام تهران علم و صنعت حیدر خانی همین الان زلزله
وحید زلزله شرق تهران کوتاه بود ولی سنگین
من سمت پارچینم
لرزش شدید
یا زلزله بود یا موج انفجار
سلام پردیس لرزید چند دقیقه پیش
شرق تهران ساعت ۷:۲۱ دوتا پس لرزه شدید اومد
سلام وحید جان دو دقیقه پیش به وقت تهران من رو زمین خواب بودم ..جوری زیرم لرزید که بیدار شدم مدتش کم بود و شدتش زیاد
آره وحید زلزله اومد سمت شرق تهران خیلی حس شده
سلام، فکر کنم حدود یکی دو ثانیه زلزله اومد تهران
من غربم :) اینکه گفتی شرق هم لرزیده مطمئنم کرد
تهران  الان  زلزله اومد  شدید و کوتاه بود
زمین لرزید الان
مرکز شهر تهران
من سبلان زندگی میکنم.. متوجه شدم
ماهم تو جنوب شرق مشیریه لرزیدیم
بحدی لرزش شدید بود ک ما تهرانپارس شرقی هستیم خواهرم تهرانپارس غربی
همه از خواب پریدن
لرزش شدید
شمال شرق تهران
همه رو از خواب بیدار کرد
شرق تهران.تهرانپارس
پحید اینقدر تکونه زیاد بود که از خواب پریدیم
حدودا ساعت ۷:۱۹ ۷:۲۰
ببین صدا نداشت ولی قشنگگگ خونه لرزید عین زلزله همه پریدیم
سلام من پاسدارانم از لرزیدن خونه از خواب بیدار شدم
لواسان قشنگ لرزید
سلام من جنوب تهرانم منطقه ۱۷ طبقه پنجم زندگی میکنم کاملا لرزش حس شد و تکون خورد
ما نارمکیم خونه ی ما یجور لرزید که من با وحشت از خواب پریدم
😭
سلام وحید شرق تهرانه چیه
من مهرآباد جنوبی سمت یافت آبادم
قشنگ خونه لرزید
تکون خورد
غرب تهرانم احساس شد
سلام ما دماوند هستیم لرزش احساس شد
من یوسف ابادم
ساعت ۷.۲۰ لحظاتی کوتاه زمین لرزید
تهرانپارس چند دقیقه پیش کوتاه لرزید
سلام صبح بخیر ، ۷:۲۰ دقیقه پردیس لرزید
نارمک هستیم در حد دو سه ثانیه زلزله حس شد ولی خیلی ضعیف بود
سلام وحید جان ، من ستارخان هستم و کاملا لرزش رو حس کردم فقط شرق نیست
وحید جان ما هم مرکز تهرانیم این زلزله رو حس کردیم ساعت ۷:۲۰ بود حدودا
سلام ۷:۲۲ سهروردی خونمون قشنگ لرزید یخچال تکون خورد ولی در حد یک ثانیه بود
تا مرکز شهرم ما لرزیدیم
خیلی کوتاه بود ولی بد لرزید
زمین‌لرزه_تهران‌پارس. شدت خیلی زیاد و کل خونه لرزید
سلام من سمت جنوب غربم خونه طوری لرزید که همه بیدار شدیم
سلام وحید جان سمت مشیریه هم لرزید ولی لرزش عجیبی بود شبیه زلزله های سابق نبود
وحید بد لرزید جوری که من همه رو بیدار کردم گفتم زلزله
اینجا نزدیک دانشگاه امام حسین
قشنگ شبیه موج انفجار بود یه تک لرزه
وای خیلی وحشتناک بود خیلی بدجور لرزید هنوز دستام داره میلرزه همه از خواب پریدیم ما شریعتی معلم هستیم
ما میدون شیخ بهایی هستیم
لرزش زمین اینجا هم حس شد
همه مون فهمیدیم در جا زمین لرزید
ساعت ٧:٢٠ صدای مهیب و لرزش زمین در پردیس شنیده. و احساس شد
مردم اومدن بیرون
سلام، من مرکز تهرانم و متوجه لرزش خفیف زمین شدم.
سلام شهرری خونه شدید لرزید ۷و۲۰ دیقه ۵دیقه پیش ما طبقه ۴م فهمیدیم
ما تهرانپارس هستیم دو تا تکان شدید مثل انفجار بود دومی خیلی شدید بود ، زلزله نبود چون لوسترهامون تکان نخورد
نمی‌دونم انفجار بود یا لرزش ولی ساعت ۷:۲۰ کامل سمت نارمک لرزید
جنت آباد هم لرزید و کوتاه بود
زمین لرزه شدید  شرق تهران   تختم  بد تکون  خورد
یک ثانیه بود ولی تکون خورد
منم رو زمین خواب بودم متوجه شدم ما مرزدارانیم
زمین کامل لرزید
سمت ظفرم
ولی لوستر تکون نمیخوره
سلام وحید جان شمال طهران هستیم اینجا هم زلزله رو حس کردیم ولی خیلی ضعیف تر از شرق طهران
سلام ساعت ۷:۲۶ دقیقه سمت میدان خراسون تهران زلزله حس کردیم به حدی بود که خواب بودیم از خواب پریدیم
نارمک خونه لرزید
انگار یه موج از زیرمون رد شد
حرکتش کاملا معلوم بود
من از رسالت (شرق تهران) یه چیزی ضربه ای خیلی شدید حس کردم شبیه زلزله نبود
منم لرزش رو حس کردم کوتاه بود ولی قوی بود
منم پیروزیم ساعتای ۷:۲۰ دیقه شدید لرزید
سلام خونه ما نیرو هوایی هست چند لحظه خیلی کوتاه لرزید ولی خیلی شدت تکان زیاد بود
ما نيرو هوايي هستيم از شدت زمين لرزه از خواب بيدار شدم
من هم لرزش رو حس کردم توی نارمک
دوتا لرزش بود شدتش زیاد بود ولی زمانش کم
فکر کردم از بالا مثلا همسایه محکم پریده روی زمین تا الان اومدم پیام ها رو دیدم
رودهن هم لرزید
سلام وحید من شرقم علم و صنعت
نمیدونم بگم زلزله بود چی بود
انگار بمب افتاد
خونه ما شرق تهرانه(حکیمیه) و حدود ۷:۱۵ برای سه ثانیه لرزید، نمیدونم زلزله بود یا چی ولی هیچ صدایی هم قبلش نیومد،
خواب بودم تختم عین گهواره شد بیدار شدم. اتوبان بابایی تهران
سلام اقا وحید زلرله ساعت ۷ و بیست دقیقه بومهن و لرزوند شدتش زیاد بود
من نارمکم، زلزله اومد، یه تکون شدید خورد قشنگ، از خواب بیدارم کرد
ساعت ۷:۲۰
سلام .تهران . نارمک شمالی. با زلزله از خواب بیدار شدم. تکون و صدای شدید داشت.
سلام زلزله شدید سمت نارمک میز کامل تکون خورد و لوازم لرزیدن از شدتش بیدار شدم
میرداماد هم حس کردم
به حدی که از خواب پریدم
هروی زلزله رو‌حس کردیم ....
و از خواب پریدیممم
۷:۱۹ صبح
پاسداران زلزله درحد تکون خوردن تختم از خواب پریدم/:
از شدت لرزش از خواب پریدم
خیلی عجیب بود
ساعت ۷:۱۵ ، نارمک هفت حوض
سلام وحید جان،حکیمیه از شدت زلزله از خواب پریدم هم خودم هم خانوادم!!
فرمانیه هم من کاملا متوجه شدم
ولی بیشتر از لرزه موج شدیدی داشت
سه تا موج پشت هم که قشنگ تو پنجره و دیوار پشت سرم احساسش کردم
ما پاسداران سمت حسین آباد هستیم
قشنگ خونه لرزید
پردیس حدود ساعت ۷،۲۱ لرزید
وحید جان افسریه جنوب شرق تهران لرزش زمین بود که از خواب پریدم
سلام ما شیان هستیم خیلی بد لرزید
به خانواده ام گفتن باور نکردن تا کانال شما رو چک کردم فهمید درست بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78098" target="_blank">📅 07:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پست سنتکام ترجمه ماشین:
🚫
ادعا: سپاه پاسداران انقلاب اسلامی ایران (IRGC) در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✅
واقعیت: نیروهای آمریکایی اقدامی محدود و دقیق علیه نیروهای مین‌گذار سپاه پاسداران که تهدیدی قریب‌الوقوع در تنگه هرمز ایجاد کرده بودند، انجام دادند. در اصل، ایران این تهدید را ایجاد کرد و ارتش آمریکا برای حفاظت از دریانوردان غیرنظامی، کشتیرانی تجاری و جریان آزاد تجارت جهانی، آن را از میان برد.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 363K · <a href="https://t.me/VahidOnline/78097" target="_blank">📅 05:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oeJWbdK-EA0DIg4JSKMMtGjcSEztmKt7whGbtc2X98p7CGR_9nh4dU9Hs0c5Vm3A0OHHBMiC7RHSbV1he-PwMadJ2Y6XOVgZCoJK7zxXuaqJ0wrMjFgJDjflAuSGwmFG2Zes4OJ1xKNn-vKqVB3EfWjzi65rFj31xyeRn6FSCQAmvJt5J8jyLeiD8xJztpZmo1kKBaTBrrbfrVEjx6J9CKhXEH7A_TlheE4bfgmrj29EnW_xY1gGnr5Frm2dKsfhkVdz9lx4qJfVzSbWli-HKBNRTNTY9HCFegfkVDd-ac7NZ7nuazm6Zm8YmBeJAxEHSn1WRc-ChfeGAXY8bldvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lEY4owAppwokiZGblZwDHWfc8ZL1MuDg8alv_U-Geg-Y0v7ki2_TaMJ768eFe5u_670qvh4GkrzGcNTvlLz3GgMR9GhDM9PS4mXmjNIysLfzSGo7vaRZyTcv__PyQjK6KnCH21C11CXopq0oIdY6MyHPc2G4IZYvGQUNPKOWaG-__g2InSZuNUD9aK1f3-ukFp-pPkACJ8xjFSuWn85sPHGz--XcGJk8nOvwmT57sgIGgzCYtoXFcs_njSDGBOQAfT1k4dBUmk8CqN0RGxzBAh-oCFnydul8g--WOjwwj8I5FbWlKGyeolyXUD4XhtQPHlU7Gdu_o4KSU8QZ5_1Vow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس جمهوری آمریکا در گفتگو با «فاکس نیوز» بار دیگر حکومت ایران را حامی شماره یک تروریسم در جهان معرفی کرد و گفت هیچ کس نمی‌خواهد آنها سلاح هسته‌ای داشته باشند، حتی مخالفان عملیات نظامی آمریکا در ایران.
ترامپ همچنین گفت که حکومت ایران به سختی خسارت دیده و رهبران و تجهیزات نظامی‌اش را از دست داده و او به دنبال یک امضا روی یک تکه کاغذ نیست.
ترامپ رهبران حکومت ایران را سرسخت و در عین حال «شیطان صفت» خواند و گفت آنها همین اخیرا ۵۲ هزار معترض را کشتند و همچنان در حال کشتن معترضان هستند.
@
VahidOOnLine
دونالد ترامپ، رئیس جمهوری آمریکا، شامگاه یکشنبه ۸ شهریور گفت جمهوری اسلامی به سلاح هسته‌ای دست نخواهد یافت، و تاکید کرد برای پیروزی در نبرد با رژیم ایران لزوما به امضای توافق با آن نیاز ندارد.
پرزیدنت ترامپ در گفت‌وگو با فاکس نیوز گفت محاصره دریایی و فشارهای مالی آمریکا ضربات سنگینی به جمهوری اسلامی وارد کرده‌اند و این رژیم اکنون در حال فروپاشی است.
او افزود: «در زمان مناسب، یا ما پیروز می‌شویم یا آنها کاری خواهند کرد؛ اما من با صرفا پیروز شدن مشکلی ندارم. نیازی به امضا روی یک تکه کاغذ ندارم.»
رئیس جمهوری آمریکا رژیم ایران را «بزرگ‌ترین حامی دولتی تروریسم» خواند و گفت: «نمی‌توان اجازه داد آنها سلاح هسته‌ای داشته باشند، و سلاح هسته‌ای نخواهند داشت.»
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در گفتگو با «فاکس‌نیوز» با دفاع از اقدامات نظامی و سیاست‌های دولتش در قبال تهران گفت: «اگر من رئیس‌جمهور نشده بودم، اسرائیلی باقی نمانده بود و به احتمال زیاد اساسا خاورمیانه‌ای هم در کار نبود.»
ترامپ با تاکید بر اینکه حکومت ایران در صورت دستیابی به سلاح اتمی از آن استفاده می‌کرد، افزود: «کشورهایی که سال‌ها در موضع بی‌طرف قرار داشتند، با آغاز درگیری‌ها بلافاصله هدف قرار گرفتند. از عربستان سعودی و قطر گرفته تا امارات، بحرین و کویت هدف گرفته شدند و همه از این اقدام شگفت‌زده شدند. همین مسئله باعث شد ایران حمایت و موضع بی‌طرفی آنان را کاملا از دست بدهد.»
رئیس‌جمهوری آمریکا در ادامه با تاکید بر جلوگیری از پیشبرد اهداف هسته‌ای تهران تصریح کرد: «اگر آنها سلاح هسته‌ای داشتند حتما شلیک می‌کردند و پس از نابودی اسرائیل و خاورمیانه، هدف بعدی ما یا اروپا بودیم. شما نمی‌توانید اجازه دهید آن‌ها به سلاح هسته‌ای برسند و هرگز سلاح هسته‌ای نخواهند داشت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 367K · <a href="https://t.me/VahidOnline/78095" target="_blank">📅 05:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZwFoGlfzRYpgSv469V8iGxL4z8UTCCPhloryISzBv7sCW06MS7wJcZmIfqVF6EWHawkPkAWosi3CvpiRKrQolRIEfl1RyPgwZEyDE8IAVZYnPoPq9Odf_m_nEd5pKaGGIlDeqfNcODN42tG03WMGq2b3IqqmHHfgETzhSXhuYg428_cFC6DPLGbo9KZRpPIZTUmPMNZMfCQmFclNHMH8aA6qBlb1X-GrqjIiG853NZ74ulI67N0BZYWFhY0HvAy4XWie9JRMzkJsBMGeLEqWMFh3mI1mmbhd8L58-dZJ1jLCdDDso-25JnYmo5LWZCXEgltUQ_1GTlLlQGJU6cOUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EvHFqwI-WFK0GmofHqK7fhuOE7SizBufVlwOV-h3_vZT13cRPRb6-9Wstc3PXCek5Drqx03OqM05qH7KizJW9Lj87ai7EMwSR5MZgK-nLtLJcwRVpG7kFS9QEyD0OWFdYbhxIow1SRH08i6AwsyEQIxpBHSdz14ZSjY4Qz6fgVUc-KJgwaUPiQh72_C70Tj7GAL8zY3qy_akDZtA8l_715QeWwOxIffbgFgHDn2_BTkVk0IDSPZRQp_040xX_TB2P0k3nV583nGkesuFLBGnCtvgC7EM2nGD5s4n7_5cRSL_Sd9-2BWgNjhVj8HFFPp7fkXOkX1XtSJouwsz2adiMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همزمان با گزارش خبرگزاری فارس، مبنی بر اینکه حملات پهپادی آمریکا به جزیره لارک از «مبدا اردن و با پشتیبانی پایگاه‌های این کشور» انجام شده بود، روابط عمومی سپاه پاسداران بامداد دوشنبه با انتشار بیانیه‌ای اعلام کرد: «نیروی هوافضا در پاسخ به حمله به جزیره لارک، در یک عملیات ترکیبی موشکی-پهپادی، زیرساخت‌های فنی، تعمیراتی و محل استقرار جنگنده‌ها در دو پایگاه هوایی ملک حسین و الازرق در اردن را با شلیک موشک‌های بالستیک هدف قرار داد.» در ادامه این بیانیه آمده است: «اقدامات نظامی، تضعیف‌کننده کنترل بر تنگه هرمز نخواهد بود و هرگونه شلیک با پاسخ‌های متقابل جواب داده خواهد شد.»
@
VahidOOnLine
شبکه فاکس‌نیوز به نقل از یک منبع آمریکایی گزارش داد در پی حملات نیروهای ایالات متحده به پرتابگرهای موشکی در جزیره لارک، سپاه پاسداران مواضع نیروهای آمریکایی در اردن را هدف حملات موشکی قرار داد.
به گفته این منبع مطلع، تاکنون هیچ‌گونه خسارت قابل‌توجهی گزارش نشده و سامانه‌های پدافندی موفق شده‌اند تقریبا تمام موشک‌های شلیک‌شده را پیش از اصابت به اهداف رهگیری و منهدم کنند.
پیش از این سپاه با انتشار بیانیه‌ای از هدف قرار دادن دو پایگاه هوایی «ملک حسین» و «الازرق» در اردن خبر داد.
@
VahidOOnLine
رویترز گزارش داد قیمت نفت بیش از دو درصد افزایش یافت و بهای نفت برنت بار دیگر از ۹۰ دلار در هر بشکه فراتر رفت.
این افزایش پس از حمله نیروهای آمریکایی به دو پرتابگر متعلق به سپاه پاسداران در جزیره لارک رخ داد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 410K · <a href="https://t.me/VahidOnline/78093" target="_blank">📅 03:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پرتاب موشک از خرم‌آباد
طی ساعت گذشت پیام‌های پراکنده مختلفی دریافت می‌کردم.
ولی در این لحظه یهو کلی پیام از خرم‌آباد اومد درباره دو صدا که خیلی‌ها نوشتند مربوط به پرتاب موشک بوده ولی بعضی‌ها هم تاکید دارند که بیشتر شبیه انفجارهای برخورد یا شکست پرتاب بوده.
هم‌زمان پیام‌های مشابهی از کنگاور در کرمانشاه دریافت می‌کنم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 438K · <a href="https://t.me/VahidOnline/78092" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HJwzQsjPTR31GNFp9bys9cVF3XC_OYEtNsBgqfPWzQu1UuQQapb11nSVT6oTdjbj8NSx9Ru3gj3C149NNHI6NEXg5zSspzqoJOLcii0blMf22NIOXcMsYRrhwZgLIdJeuIAW_ppXcVkFlMEtgEypDlMAHBQVtSnIREmUxicBV7PaknokksnJoi8BGdWUjilEh803q8jsu8d1BXIKJV0kmRHXbK28h1qJQTFnkrl-6rPWgaQmmdEEi6IwxMkraIlBlmYNgjuMBQy9jWyx_B1b50rH-m7cMIngeBjyfyPn0pfIPaI2s6efA1UVqApIYS3-sq7WdjUodnPllRVyv6Gbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه با تایید کشته‌شدن شماری از نیروهایش در حمله آمریکا به لارک: پاسخ خواهیم داد
منابع حکومتی:
روابط عمومی سپاه پاسداران انقلاب اسلامی:
🔹
دشمن آمریکایی - صهیونی بار دیگر بر مبنای استیصال خود در حل مشکلات داخلی و کاهش اعتبارش در بین کشورهای منطقه به دنبال احیای نقش شوم خود و توجیه افکار عمومی، در اقدامی تجاوزکارانه، با حمله به جزیره لارک منجر به شهادت و مجروحیت تنی چند از رزمندگان و هموطنانمان شد.
🔹
این اقدام توسط فرزندان ایران اسلامی پاسخ داده خواهد شد و تنبیه متجاوز را به دنبال خواهد داشت.
پیش‌تر یک مقام آمریکایی اعلام کرده بود که دو پرتابگر سپاه پاسداران که آماده شلیک به کشتی‌ها بودند در جزیره لارک هدف قرار گرفتند: @
VahidOnline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 479K · <a href="https://t.me/VahidOnline/78091" target="_blank">📅 23:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 462K · <a href="https://t.me/VahidOnline/78089" target="_blank">📅 22:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IOActtaGkgsCdBV8TSGIUpRLw65vE_sQBxrIUPk8j4q52_YV6rLnKT04MQLzu4mo0hL3Rfv1fqFc7kAmqI-iyWTDlhr63H1zWbsefryvyVCrx3PilaHbFmWo08Fcc7iywNkreRzuRgfsJtRb-d6mLjBgO7V97YLFI_tj8FxBS-ASFTIWlmkTJkMYT7fPHSnMph2dGTxoUR5sHB4hryKtwcLMV_5kpujsPQZMwRwKcU-P5gtlPxn8ACvmtDvaympvAJAu-whlDZ2XRJLvLFzuEEQmkWZ5bDfC_R1TWM_-VphNtr5pWEBJcks0cIDn5VCy5wAvWpgBe5wZQcpv7Hpg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
یکی از کارهایی که قرار است با نفت ونزوئلا انجام دهم، پر کردن ذخایر راهبردی ملی است؛ ذخایری که به‌خاطر جو بایدنِ خواب‌آلود عملاً خالی شده‌اند. روند «پر کردن تا ظرفیت کامل» به‌زودی آغاز خواهد شد و این هدیه‌ای از سوی ونزوئلا به مردم ایالات متحده است. متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 416K · <a href="https://t.me/VahidOnline/78088" target="_blank">📅 17:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/UhZN6rKuquHPnekSuOTrddjVJga49rg9aQ-J_TaMDbaxXoxsW6Hwb5QlHusov3ESq_phEVkdPbhH7uFncypzuOhkiCtvTHQwvXXCS1p999E0WMlzJow4gVibwIihwOIck0aX2djDwxeBfzCBXlj-JwRL3qsLV9yj5O1dZqamOExREVsqIOPFt6sjOtrair5ag_WM4NwwGosL4jJ-9BbAEtU7fpRaFBv0IN57oXs1O6UkX-lBR2YATQFPFbookfzha5AAzbEFriC3NP68mezdHiO1jVxxxSE-XTiP6qBFfq0UuCCtSYfG-wuDI87rbIPMDMsNSyCd8OLj2COoe5MAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشینگتن‌پست به نقل از افراد آگاه گزارش داد چند مقام ارشد نظامی آمریکا به پیت هگست، وزیر جنگ آمریکا، هشدار داده‌اند که ادامه عملیات نظامی گسترده علیه جمهوری اسلامی پایدار نیست و توان ارتش آمریکا را برای مقابله با تهدیدهای دیگر، از جمله دفاع از خاک آمریکا، تضعیف می‌کند.
به گفته این افراد، این هشدارها که روسای ارتش، نیروی دریایی و نیروی هوایی آمریکا، همراه با فرماندهان چهارستاره مسئول عملیات نظامی آمریکا در اروپا، آسیا و آمریکای لاتین، در نسخه ۲۳ مرداد «کتاب دستورات وزیر جنگ» به هگست ارائه کرده‌اند، بخشی از یک سند محرمانه است.
بر اساس این گزارش، با توجه به تاکید ترامپ بر اینکه گزینه نظامی همچنان روی میز است، ستاد فرماندهی مرکزی آمریکا (سنتکام)، که مسئول اداره جنگ با جمهوری اسلامی است، ماه‌هاست بیش از ۵۰ هزار نیرو را در حالت آماده‌باش نگه داشته تا در صورت صدور دستور حملات بیشتر از سوی رییس‌جمهوری وارد عمل شوند.
به گفته افراد آگاه، نسخه ۲۳ مرداد کتاب دستورات وزیر جنگ مقرر کرده است که بخشی از نیروهای مستقر در خاورمیانه تا پایان سپتامبر در منطقه باقی بمانند و ماموریت برخی دیگر تا سال ۲۰۲۷ تمدید شود. احتمال تمدید بیشتر این استقرارها باعث شد فرماندهان نظامی نگرانی‌های خود را آشکارا مطرح کنند.
به گفته این منابع، فرماندهان ارشد فرماندهی اروپا، فرماندهی اقیانوس آرام و فرماندهی جنوبی آمریکا، همراه با فرمانده ارشد نیروی دریایی، در این سند نظر «عدم موافقت» ثبت کرده‌اند؛ به این معنا که با دستور وزیر جنگ برای تمدید استقرار نیروهایشان موافق نیستند، اما آن را اجرا خواهند کرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78087" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KtfDyXxjrHS4ulJ-xN6XeZ8WS2a8T2_JmoCIGMKHfTji6IhoM6Y4pfellUbTg29sq9-5J8-PedcmHWyT1yS69eoHDAoa6iA_1W3llI9-xWdZnQZztbk2ZYMR0APoPLC3RTw-3XttC71cea1tFDuDk5bHu53qoaiI6TBKIvanvNdnLiQpFcdQ5xY7jkGcaQ07bmOipJmvEUqQ3ENEggIb4H5yxV5Bqd0DmTjLH_cOgULGhnfWKZl2SFCyqHpGZDv6GwXE4Znz-e5gos7XcC3xtgQCGWA86fK93bYWoE0gijpum-zCUc1OVgEZnehxoSEkhcZK-w5WWdVyiwjwNLfVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شعبه اول دادگاه انقلاب اصفهان ۱۰ نفر از متهمان پرونده موسوم به «میدان شهدای اصفهان» را به اعدام محکوم کرده است. شش متهم دیگر این پرونده نیز احکام سنگین زندان گرفته‌اند.
کانال تلگرامی خبرنامه‌ها خبر داد این احکام در مرحله بدوی صادر شده‌اند: @
MahmoudianMehdi
«ترانه رحیمی»، «نوید الیاسی»، «ابوالفضل دادگستر»، «مهدی منصوری»، «احمدرضا سعیدی»، «مهرداد بو‌ئری»، «محمد مهدی اسدی»، «آرمین غلامی»، «پارسا جعفری» و «مهدی جعفری»، معروف به «مهدی خسروی»، ۱۰ متهمی هستند که حکم اعدام گرفته‌اند.
در بخش دیگری از حکم، «رومینا رحیمی» و «میلاد بو‌ئری» هرکدام به ۲۵ سال حبس و «حامد مهرعلیان» به ۱۵ سال زندان محکوم شده‌اند. «ستایش ساعدی»، «سجاد عابدی» و «علی بوئری» نیز هرکدام به پنج سال حبس محکوم شده‌اند.
دادگاه همچنین هر ۱۶ متهم را بابت اتهام «اجتماع و تبانی» به پنج سال، «تحریک» به پنج سال و «فعالیت تبلیغی علیه نظام» به یک سال حبس محکوم کرده است.
پرونده «میدان شهدای اصفهان» در ارتباط با اعتراضات دی‌ماه ۱۴۰۴ تشکیل شده است.
متهمان این پرونده از ۱۴ بهمن تا ۲۴ اسفند همان سال در خانه‌هایشان بازداشت شدند. شماری از آن‌ها کارکنان فروشگاه‌های کفش و پوشاک در محدوده خیابان شهدا یا از بستگان صاحبان این فروشگاه‌ها هستند.
بیشتر متهمان این پرونده کمتر از ۲۳ سال دارند. ترانه و رومینا رحیمی، خواهران دوقلو، هنگام بازداشت ۱۹ ساله بودند.
جلسات رسیدگی به اتهام‌های این افراد از ۲۲ تیر ۱۴۰۵ در شعبه اول دادگاه انقلاب اصفهان آغاز شد. اتهام‌های آن‌ها «محاربه»، «معاونت در محاربه»، «تخریب اموال عمومی در حکم محاربه»، «اجتماع و تبانی» و «تبلیغ علیه نظام» اعلام شده بود.
این پرونده پس از کشته‌شدن «عباس کامرانی»، عضو سپاه پاسداران، و یک شهروند بی‌خانمان در اعتراضات ۱۸ دی تشکیل شد. بااین‌حال، در کیفرخواست صادر شده علیه متهمان، اتهام قتل مطرح نشده است.
منابع مطلع پیش‌تر گفته بودند در جلسات دادگاه مدرکی که نقش متهمان در کشته‌شدن این دو نفر را اثبات کند، ارائه نشده‌ و اعترافات گرفته‌شده در دوران بازجویی، مبنای طرح اتهام‌ها قرار گرفته است.
شماری از متهمان در دادگاه گفته‌اند اعترافات آن‌ها با ضرب‌وشتم، استفاده از شوکر و تهدید به تعرض جنسی گرفته شده است. «احمدرضا سعیدی» نیز در حضور قضات اعلام کرده بود که در دوران بازجویی شکنجه شده است.
براساس اطلاعات منتشرشده، یکی از زنان متهم این پرونده نیز از تعرض در زمان بازداشت خبر داده و شکایتی ثبت کرده است. بااین‌حال، دادگاه بدون رسیدگی به این شکایت، حکم او را صادر کرده است.
وکلای متهمان نیز از دسترسی کامل به پرونده محروم بوده‌اند. گزارش‌ها حاکی است دادگاه اجازه نداده است هر متهم از شمار قانونی وکلای مدافع برخوردار باشد.
«محمدرضا توکلی» و «مرتضی براتی»، قضات این پرونده، پیش‌تر نیز در پرونده‌های سیاسی و امنیتی اصفهان حکم اعدام صادر کرده‌اند. توکلی از قضات پرونده‌های «میدان علیخانی» و «توماج صالحی» بوده و براتی نیز در پرونده «خانه اصفهان» برای سه معترض حکم اعدام صادر کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 382K · <a href="https://t.me/VahidOnline/78086" target="_blank">📅 17:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a6xuOd97mPXlXc85W5yAoDT0GAsN99UiX9b1L2wiOGhMbofjq09hXOGLNHrBTMrxCdbQBC53bJcXFaHHMk-FsLeoXLWpdgzMLCv5Lok5J1cabXJ_vgdjbDXjUjPbRzsghuETsIHDtrbVF6IOQEwu9IjfJ2j1Mxbl0kL6jCsVWqF6h7WzSarrW7r8LBKeVGT-JowqY_8rpuLPDfge5mGkHxEB_5C8vgAKRV6gikNx_9YMHphvQIJPko-gcknGnnvXyn_PPwfwQeunc4BNoXqK-kIQncJzkKIb1RRIsyJRBrUua041fpb_t93gTq9-nhAAEwVYyKP7h-Sa0PPnIUtapw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولینگو اعلام کرد آزمون زبان این مؤسسه در ایران و برای دارندگان مدارک هویتی ایرانی در دسترس نیست. همزمان گزارش‌هایی از لغو آزمون تافل و عدم اعلام تاریخ‌های تازه برای برگزاری آن در ایران منتشر شده است.
این تحولات چند روز پس از تعلیق یکی از معافیت‌های تحریمی آمریکا در زمینهٔ خدمات آموزشی به ایرانیان رخ می‌دهد.
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (اوفک) روز دوم شهریور مجوز عمومی موسوم به «G» را که از سال ۲۰۱۴ برخی تبادلات دانشگاهی و ارائه خدمات آموزشی به ایرانیان را مجاز می‌کرد، برای مدت نامحدود به حالت تعلیق درآورد.
دولینگو، شرکت آمریکایی سازندهٔ اپلیکیشن آموزش زبان که آزمون آنلاین انگلیسی آن از سوی بسیاری از دانشگاه‌ها پذیرفته می‌شود، اکنون در صفحهٔ رسمی پشتیبانی خود اعلام کرده است که این آزمون در ایران و برای افرادی که از مدارک هویتی ایرانی استفاده می‌کنند، در دسترس نیست.
همزمان شماری از کاربران ایرانی در شبکه‌های اجتماعی تصاویری که به‌گفتهٔ آنان مربوط به از پیام‌های لغو آزمون تافل و نبود مرکز یا تاریخ آزمون در سامانه ثبت‌نام ETS (برگزارکنندهٔ آزمون تافل) است، منتشر کرده‌اند. رادیو فردا نمی‌تواند اصالت و منشأ این تصاویر را مستقلاً تأیید کند.
برخی داوطلبان نیز گفته‌اند آزمون‌های تافل تا همین روزهای اخیر در ایران برگزار می‌شده، اما پس از تصمیم تازه اوفک، پیام‌های لغو برای شماری از متقاضیان ارسال شده است.
تا زمان انتشار این گزارش، مؤسسهٔ برگزارکنندهٔ آزمون تافل اطلاعیه‌ای رسمی دربارهٔ توقف برگزاری این آزمون در ایران منتشر نکرده است.
در وب‌سایت این مؤسسه، ایران همچنان در فهرست کشورهای محل ارائهٔ آزمون اینترنتی تافل قرار دارد و اطلاعات تماس ویژهٔ متقاضیان ایرانی نیز در آن دیده می‌شود.
از این رو، هنوز مشخص نیست محدودیت‌های گزارش‌شده چه دامنه‌ای دارند و آیا مستقیماً ناشی از تصمیم اوفک هستند یا نه.
مجوز عمومی G که اوفک در مارس ۲۰۱۴ صادر کرد، از جمله به دانشگاه‌های معتبر آمریکایی اجازه می‌داد با دانشگاه‌های ایران برنامه‌های تبادل دانشگاهی داشته باشند و برخی خدمات آموزشی را به دانشجویان ایرانی ارائه کنند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 400K · <a href="https://t.me/VahidOnline/78085" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YQBucHZb4QYko9Hu77fnAm1kcakj7cFE5L7LtfGuxtldD1q_wIODjRNRJbECk7ZbKxOZa4vPXdyz3ci8o_eopD8pnWRs4xcRWms-h_u_vWqIdeZO2qzyFQ5IpTWwZwQDZE8t0YpMn0HPcUmvhmmlQxlTGx8tf-al8LH1IwXYpTutuznfuBvi4z8IwmOwBTw8mIvI83FDTnCV0oH01HkmRtQR_A2bgwTnZawmg1uVgeEMQCnaVVKREp9pX6z8KaJhDme75PXkIZozYfZORu87X6Bu5mFiVtAnKcHbH143lROb7HcqLGIvOIcfKAY5wjvuvh7dlsROtnS6pycQi2fwGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بر اساس آخرین نرخ‌های ثبت‌شده در بازار آزاد در روز شنبه ۶ شهریور ۱۴۰۵، قیمت دلار آمریکا به حدود ۲۰۵ هزار و ۸۸۰ تومان رسیده است.
نرخ دلار در بازار هرات نیز حدود ۲۰۵ هزار و ۲۳۰ تومان ثبت شده است.
داده‌های لحظه‌ای بازار همچنین قیمت دلار را در ادامه معاملات بالاتر از ۲۰۶ هزار تومان نشان می‌دهد.
در همین حال، هر یورو حدود ۲۳۸ هزار و ۹۱۰ تومان و هر پوند بریتانیا حدود ۲۷۹ هزار و ۹۰ تومان معامله می‌شود.
قیمت دلار کانادا نیز به حدود ۱۴۸ هزار و ۶۵۰ تومان رسیده است.
در بازار طلا نیز هر گرم طلای ۱۸ عیار بر اساس تصویر ثبت‌شده از بازار به حدود ۲۱ میلیون و ۸۱۰ هزار و ۷۹۰ تومان رسیده است.
قیمت هر مثقال طلای آب‌شده نیز حدود ۹۴ میلیون و ۴۸۰ هزار تومان گزارش شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 366K · <a href="https://t.me/VahidOnline/78084" target="_blank">📅 19:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=BtBGmLJGjrNmckqa3LA93jZ6aj2fHEQswMi4Woe459LVxJNlIJKnNWgM3cbaEIpMXbnydb6MQbUF6dGtwZyUb_r3koYghCuJIYzotnDpupsCbJmMfobS-Miotgyc3Y7M-N2R4RTC24BVTHxJT1tbr0n7n3Veu6Vy0nyGPdP0JmEXYvO5yYybxovWDI0Noi6cjkcjIJSvgiMvzGXYYxQYlfg6h63Vl9Lvf-wNwRISyR7lMPNmFSdse4UdRvxmEkbVBFh1SslmbwA_EeszHslHT6ih65qyS5QZWDO5xKCjgOLzerJU1HlGN-q9ldz3bvgNQ62j5l6c4Bg9VAlrmCh8mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ceeb0af509.mp4?token=BtBGmLJGjrNmckqa3LA93jZ6aj2fHEQswMi4Woe459LVxJNlIJKnNWgM3cbaEIpMXbnydb6MQbUF6dGtwZyUb_r3koYghCuJIYzotnDpupsCbJmMfobS-Miotgyc3Y7M-N2R4RTC24BVTHxJT1tbr0n7n3Veu6Vy0nyGPdP0JmEXYvO5yYybxovWDI0Noi6cjkcjIJSvgiMvzGXYYxQYlfg6h63Vl9Lvf-wNwRISyR7lMPNmFSdse4UdRvxmEkbVBFh1SslmbwA_EeszHslHT6ih65qyS5QZWDO5xKCjgOLzerJU1HlGN-q9ldz3bvgNQ62j5l6c4Bg9VAlrmCh8mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منابع حکومتی:
"اعزام نیروهای مردمی به تنگه هرمز در پاسخ به یاوه‌گویی‌های ترامپ"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/78083" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mbzm8csiiY3l3zbuw0LvNJ-kny2iW_m48OMLJKFRsZerRzOrYG6UDIj5mRFOxdha-tWKvz5D9eCVdG3cHsHkd6ppaW5NksTo7-MdFQoprMqqis8dqSvbXqtk4T1DPgV9djJFWAlA9STkCtW_bgnz4il33gPGH--exPMUPCKiVgSMRlDkTam-AbBC2MHDKk8SIpIq8lIGOuA_Ock_7C5XtzQfKrC6vtdFLg53MTOnuS-RNSHI5Tikv7UVWjCYHk-EclFXFjhYCRkVWUbuBAgIuASPJ9sAommfji9gvS9STS0TMLm-zIGdvqWQzc9QCs16KPg7Ge-lp7aEENiFh4806g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از ابتدای سال ۲۰۲۶ تاکنون، بنیاد عبدالرحمن برومند ۹۵۰ مورد اعدام را در ایران مستند کرده است. دست‌کم ۲۰ زن و ۳۰ معترض در میان اعدام‌شدگان قرار دارند و تا این لحظه، ۴۵ مورد اعدام در ماه اوت به ثبت رسیده است.
🔸
در نظام قضایی جمهوری اسلامی که بر پایه روندهای ناعادلانه، عدم شفافیت و نفوذ انگیزه‌های سیاسی بنا شده و در آن اصول دادرسی عادلانه به‌طور سیستماتیک نقض می‌شود، استفاده از مجازات اعدام، بر اساس حقوق بین‌الملل، مصداق سلب خودسرانه حیات است.
#نه_به_اعدام
@IranRights</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/78082" target="_blank">📅 19:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NiEvAfYd8sVsQMA5nhC3DM5GRlJ5Z5ibUhMTdKS_GmggHqFPmcN_lfUmNLO0f_5nWMbrda5pPXTvQYurhr4BzD7cz43mABgFatvyX65-hBz0lFy1dnsnOuKnoEbyr9h4RD2hBv6xMi2_Al6T9msvPqgmr6Cyzo9ZeaEiDrzs32tZkcATmbIb1fHKfRHafrnLAx7mee1yBZnkfJ_-8UO54qoaxBx0QRGyOli0OD8HxBagUoGp9tU2hPfUM8QnS3M824iRQ2s6bj5M6j2dk9APRhda68utW7uet_3YIOlA6VsDW81vD5n4PACp9B9lCE9raKTU-Fj8Zt4hyhbGHjOCSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/StEAu1GYyF47OFcpkHn2aaKbXqdc_sKeg4Y4iCxiP5WQ_mp79asFwtWCRu0iL1llSrTKWvYeAB7S2IaCGzDBXv60YoyxfdzY5bYvt7YS6g3HkV_5lcdyGtRwA_nfLpYIIIdNaFOgS64iDrlMRcpcIX77fXPRPxIjT6DDpcjUpn1hu9AqGrTOAAb7nH_asUjzygVlpaCxax-1vGTrbRqTgaXcw4wZEZZ3geoLktIvmIWu5oV7NefC70J89xcLDc9IG6qHnZdPY2ELL8NlDN3KWUAHOvvqOPWYq5bVwYuNM2DaszENqaiZDN5GjPUygA-16O0iFHXfDqrnOS1-awmXjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رییس‌جمهوری آمریکا، در تروت سوشال اعلام کرد آمریکا با ونزوئلا به توافقی دست یافته که آن را «بزرگ‌ترین توافق نفتی در تاریخ جهان» خواند.
ترامپ گفت بر اساس این توافق و با مشارکت بخش خصوصی، آمریکا کنترل اکثریت بیش از ۶۵ میلیارد بشکه از ذخایر اثبات‌شده نفت ونزوئلا را بدون تحمیل هزینه به مالیات‌دهندگان آمریکایی در اختیار خواهد گرفت.
او افزود مارکو روبیو، وزیر خارجه آمریکا، و پیت هگست، وزیر جنگ آمریکا، با همکاری دلسی رودریگز، رییس‌جمهوری موقت ونزوئلا، در دستیابی به این توافق نقش داشته‌اند.
ترامپ گفت این توافق ذخایر نفت آمریکا را بیش از دو برابر می‌کند، عرضه نفت را به میزان قابل‌توجهی افزایش می‌دهد و در بلندمدت به کاهش قیمت بنزین برای آمریکایی‌ها کمک خواهد کرد.
@
VahidOOnLine
مارکو روبیو، وزیر امور خارجه ایالات متحده، روز جمعه با اشاره به توافق نفتی جدید میان واشنگتن و کاراکاس اعلام کرد که این توافق علاوه بر تضمین ذخایر پایدار و کاهش بهای بنزین در آمریکا، نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی را به ونزوئلا سرازیر خواهد کرد.
روبیو در اکس نوشت: «برای مردم ونزوئلا، این توافق نزدیک به ۱۰۰ میلیارد دلار سرمایه‌گذاری بخش خصوصی به همراه خواهد داشت، از هزاران شغل با دستمزد بالا حمایت می‌کند، و پیشران بازسازی اقتصاد ونزوئلا خواهد بود.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 384K · <a href="https://t.me/VahidOnline/78080" target="_blank">📅 04:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=My34X2K7-CGc5GRywoiiPAoWWPoSEvUYUsYM99qX3xGRT5Dvt_WhZeSdaHxH6GHRboKyhmve2wssKF7RBjrh8RbygziY0Rr4ltvpC3lWIPBZUyiBxx7zfgvdva2ECTfTsS3EfgS7bTR4-jUju_EdJ_NrXQNS8_cyasS3UMOinfqEKVxcR4o9lijjpz8tNT0U4LcRWO_9uLDjsAqc35PUsXxUpDyzXE62BoUXnW9HMF7XEE5WMHr5FG6-nnM6bq53_X_AumAq1RhlhA7fWJc6mX31XP28itLa0BEW82Ra_BPxPPPel85H3fIxM_Z3X1aub5DA9YuwWGDohQzezbTvsw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/034defbf1c.mp4?token=My34X2K7-CGc5GRywoiiPAoWWPoSEvUYUsYM99qX3xGRT5Dvt_WhZeSdaHxH6GHRboKyhmve2wssKF7RBjrh8RbygziY0Rr4ltvpC3lWIPBZUyiBxx7zfgvdva2ECTfTsS3EfgS7bTR4-jUju_EdJ_NrXQNS8_cyasS3UMOinfqEKVxcR4o9lijjpz8tNT0U4LcRWO_9uLDjsAqc35PUsXxUpDyzXE62BoUXnW9HMF7XEE5WMHr5FG6-nnM6bq53_X_AumAq1RhlhA7fWJc6mX31XP28itLa0BEW82Ra_BPxPPPel85H3fIxM_Z3X1aub5DA9YuwWGDohQzezbTvsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: نرخ سوم بنزین حدود ۱۰ هزار تومان خواهد شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 387K · <a href="https://t.me/VahidOnline/78079" target="_blank">📅 22:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WKHeP8tPyr10BMv0qf3D8KvJFrwTCBXF4szQYXAO6REkNxUAyXncCyEJL2sk0M1ggBD57n5SPIMeyaC6-bAgVPub8QWVX69gzfTxsGLneqgQb-cmxbN27q4M0tTGx4Kqp8zRRVgwo7gh4zbgwp8Bbs2VjASUH6MK32KeKBFeKoMJkEbAuTD6t1NlbBEcvGvnLZtUAWWfqmDO0QgvgKWyoGQ40FWatlCNurj7ZHfdcvOWp5Zwk-6IVL4LfM4BhlnGFiQF_Pm-6B-wpwpH-aJ8oL17IMAqrZvk2ibDY1r7DkmhTn0cigaeJIvDBJRw3x1oAJ-EmjtWw1EAiJ8wxPT9Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.  به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم…</div>
<div class="tg-footer">👁️ 399K · <a href="https://t.me/VahidOnline/78078" target="_blank">📅 21:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری وعده داده بود که هر شریان اقتصادیِ باقی‌مانده برای تهران را قطع کند و سرانجام به تهدید رژیم ایران پایان دهد.
همچنین هشدار دادیم که حامیان ایران نمی‌توانند همچنان از دسترسی به دلار آمریکا و نظام مالی جهانی برخوردار باشند.
بانک مصر امارات تصمیم گرفت این موضوع را به شیوه سخت بفهمد، و امروز نخستین گام را برای پاسخگو کردن آن به‌دلیل حمایت مستمر و فاحشش از رژیم ایران برمی‌داریم.
SecScottBessent
وزارت خزانه‌داری امریکا:
امروز، در چارچوب «عملیات طرد اقتصادی» (Operation Economic Outcast)،  شبکه اجرای جرایم مالی (FinCEN) قاعده‌ای را پیشنهاد کرد که دسترسی بانک مصر امارات به خدمات بانکداری کارگزاریِ مؤسسات مالی آمریکا را لغو می‌کند.
علاوه بر این، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (OFAC)، رضا محمد تأییدی، مدیر بانک ملی دبی، را به همراه یک شرکت پوششی مستقر در هنگ‌کنگ که به پول‌شویی وجوه برای یک صرافی تحریم‌شده ایرانی کمک کرده است، تحریم کرد.
«عملیات طرد اقتصادی» در حال قطع کردن آخرین شریان‌های مالی‌ای است که رژیم ایران را سرپا نگه می‌دارند.
USTreasury
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 347K · <a href="https://t.me/VahidOnline/78077" target="_blank">📅 18:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78075">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHgAQyKFEA6nDZv1BHWeo-8FrXo_bJEfbSPP5crkGuXnlnfRBfnr_AOgWtBjAupRsftWOr3i_mjLssvC7ETP2D4XpamPIm4waXrlmHDyNd9hw8xWGKliEAzTPuJobKCfd3NLu_HiuRtV92juS5TlnWqIbNEtL6U2QJ0xZecODsPnTv5iMY5OC_2iAtirNmj879MRAqp6vA4AnkiprSZH-xgcccoObz4peS8EdeR-Vck4NTFP_5smQeJ5zmCv5Hfe5f_f4zGXYWATw0G4vMQFTrkDPk6TnptLfD8tMkkqBRghbdQMMCIaJpnBqiRhoPQS82u8dO0h1j6KMMnzq3Goyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا نوری، امام جمعه بجنورد، در خطبه‌های نماز جمعه این شهر گفت: فشار اقتصادی کمر خود آمریکا را هم دارد می‌شکند و با فشارهای مردم در آمریکا بر علیه خود ترامپ، او که رای اول را در آمریکا داشت امروز محبوبیتش به زیر ۳۰ درصد رسیده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/78075" target="_blank">📅 16:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tqRfdLPRF7Vw67EB4R-dWSi3mHkuO0HCSEe3E4g-dSpvLt5WkTWGVmHs6lhbDXdAXGEntfx_5JBCl10DrcWtLreFJx5clyHMpR_e3hKpTkdcZHO8fgIKlMjSWzJ13Xw1_RAuVuj69Npc7_jJ9Qb-V6KeI2cSu5R65y-PiXMJiqFCxnaXsz4hB52Dugod6fSklnEp1d-CkCaGdN6i3x6ZP7GUG7FRIqThI33XqDiF6SNBKz3Vym1dxrWm0fIRoNVhQVhgrfFyH9Hgho-kGx3XocOD90ShwxXTJXIgX5HSYpjqVwybzL5S39mc0eKmHo0ZNopHj-jWmePmQTekF7kDpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه جمهوری اسلامی در واکنش به دور تازه فشارهای اقتصادی آمریکا، از کشورهای جهان خواست از اجرای تحریم‌های یک‌جانبه واشینگتن علیه ایران خودداری کنند.
این وزارتخانه روز جمعه، ششم شهریور، در بیانیه‌ای «عملیات طرد اقتصادی» آمریکا را «تروریسم دولتی» خواند و مدعی شد تحریم‌های جدید واشینگتن با منشور سازمان ملل و اصول حقوق بین‌الملل مغایرت دارد.
در این بیانیه، جمهوری اسلامی آمریکا را متهم کرده است که با استفاده از نقش دلار در نظام مالی بین‌المللی، کشورهای دیگر را برای قطع روابط اقتصادی با ایران تحت فشار قرار می‌دهد. وزارت خارجه جمهوری اسلامی این اقدام را نقض حاکمیت ملی کشورها و اصل برابری حاکمیتی دولت‌ها دانسته است.
وزارت خارجه جمهوری اسلامی همچنین به قطعنامه‌های مجمع عمومی سازمان ملل درباره منع مداخله در امور داخلی کشورها و اصول روابط دوستانه میان دولت‌ها استناد کرده و گفته است دولت‌ها نباید آثار تحریم‌های یک‌جانبه آمریکا را به رسمیت بشناسند یا در اجرای آنها مشارکت کنند.
در بخش دیگری از این بیانیه، تهران تحریم‌های تازه آمریکا را ادامه «جنگ اقتصادی» علیه جمهوری اسلامی دانسته و مدعی شده است این اقدامات با هدف تحمیل فشار و آسیب اقتصادی بر مردم ایران انجام می‌شود. وزارت خارجه جمهوری اسلامی همچنین از سازمان ملل و کشورهای عضو به دلیل آنچه «مماشات» در برابر اقدامات آمریکا و اسرائیل خوانده، انتقاد کرده است.
این موضع‌گیری پس از آن صورت گرفت که آمریکا در روز دوشنبه، دوم شهریور، از آغاز کارزار تازه‌ای با عنوان «عملیات طرد اقتصادی» علیه جمهوری اسلامی خبر داد. هدف اعلام‌شده این کارزار، تشدید فشار بر روابط اقتصادی ایران با دیگر کشورها از طریق تهدید به اعمال تحریم‌های ثانویه و محدودیت در دسترسی به نظام مالی آمریکا عنوان شده است.
عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، نیز در نامه‌ای به آنتونیو گوترش، دبیرکل سازمان ملل، از این سازمان و کشورهای عضو خواسته است در برابر اقدام تازه آمریکا واکنش نشان دهند و واشینگتن را مسئول پیامدهای تحریم‌های یک‌جانبه دانسته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 297K · <a href="https://t.me/VahidOnline/78074" target="_blank">📅 16:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78073">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/693aecab40.mp4?token=DmASHG7aDHbxy3LYTrHLxhZMMmi1nj-jA9tx_zg9H0CmF0z_BEPNsuq1mgofxXMfAEJ3GxmnJRAQcvZQPMmXSBKFpLgoCMa0t2o3NxgJZrSlwN-ayH4MayaO2NeT-FwslNP_iH5vgRqVXeLzu2obL2rU6WhDya9-vsO9fKXt3lbeHSI6XFpPcc41-cUUHhy89CVinXxKAUEE0u1gEhOwht462gZpWS-iD1plySyIhaLRrZIFbdm6e-0d1tXm50UUCpcULUR953L-JpI7pc-sAx2zC4mqWNYshPL-jJC6rdLSdc6n8Uu18fVth3jgQg3ixKym6A5H8_a95mKXqEiSRg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/693aecab40.mp4?token=DmASHG7aDHbxy3LYTrHLxhZMMmi1nj-jA9tx_zg9H0CmF0z_BEPNsuq1mgofxXMfAEJ3GxmnJRAQcvZQPMmXSBKFpLgoCMa0t2o3NxgJZrSlwN-ayH4MayaO2NeT-FwslNP_iH5vgRqVXeLzu2obL2rU6WhDya9-vsO9fKXt3lbeHSI6XFpPcc41-cUUHhy89CVinXxKAUEE0u1gEhOwht462gZpWS-iD1plySyIhaLRrZIFbdm6e-0d1tXm50UUCpcULUR953L-JpI7pc-sAx2zC4mqWNYshPL-jJC6rdLSdc6n8Uu18fVth3jgQg3ixKym6A5H8_a95mKXqEiSRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش ایالات متحده در ویدئویی که روز پنجشنبه پنجم شهریور منتشر شد اعلام کرد که نیروهای آمریکایی مین‌های دریایی را از تنگه هرمز پاکسازی کرده‌اند و مسیرهای بین‌المللی کشتیرانی باز هستند.
دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ارتش ایالات متحده، سنتکام در یک پیام ویدئویی که در رسانه‌های اجتماعی منتشر شد، تاکید کرد که «امروز، خطوط کشتیرانی بین‌المللی باز هستند و تردد در حال افزایش است.»
کوپر با اشاره به پاکسازی مین‌ها در تنگه هرمز گفت: «شرایط، می‌توان گفت، چالش‌برانگیز و خطرناک بود. اما ما کار را انجام دادیم.»
پیشتر دونالد ترامپ، رئیس‌جمهور آمریکا، هم از پاکسازی تنگه هرمز از مین‌های کار گذاشته‌شده‌ ایران در تنگه هرمز خبر داده بود. سپاه پاسداران اما با رد این اظهارات بارها تأکید کرده که تنگه هرمز همچنان مسدود است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/78073" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VRrJu33HXEgMQyJLtYEQ44hM2ZI5QVvk960euAMS8mrMjtWWslA50dd0a55WeT31cyQYqhFnfelcSRFuJ4ZOnYW-irOqUKeoxo3Q-eiz00tIsQn6e0IxfGUmbw0FH8N1nt90f5BNkyyjeNKBTA4nMYMfUTHfBnwu5Lshk1tU14WPtkG1noMXJsw2V_ka_v7E57aWfjz68Z7B42I1c8go4uYhHbpju09MxgSNRtE4URdVmvxcpfc0gmxLAQonA-jn6zsFc4TqIAbaV2kPMq62CfL-6sm2Q1JUaSZ280Rsep1xkCL7XKRzwjf5jS0FTONzjX3DYXkci_f08n1A1qSG_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fBNLhQIjfLF4wq52rhUvcxBAGgxxy9NyY7YoiNaZ2O5gYvXRMsGIXiHu-25mzi6WAbZUhS-flyBeYy-VSVgi0baeIJp9_dWug28JCxycENV440x3rffUUKzmrnLKyhDyVhMomWo-ueozXlsMLA1qCXwa31Mvud2lroB5HusguVUiP2TvnaIo1HcBHt-prQ8vdpE0rw6Fs2dTJb90WTZar6Gwk0kobKgTUdkxiieYOoDYKWfHrSHiY0pJ7lflFVHSNrg5GNBlDoMHaD7D_DLlopaJF2zNq9CH4lM2dDWkaRdkdu7LlAG5o4uCzNpFGsvYO21aXM6XovKQStD-2sprxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری آمریکا، در گفت‌وگو با اکسیوس درباره تنگه هرمز تاکید کرد که این تنگه «باز است.»
او گفت: «پاسخ ایران بسیار ملایم است. آنها نمی‌خواهند ما دوباره به آنها حمله کنیم. تمام ماجرا همین است. بقیه چیزها اهمیتی ندارد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 259K · <a href="https://t.me/VahidOnline/78071" target="_blank">📅 16:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lXHSPWU7tJcb5a_rQvYW4xl2bwBlA9zMV9Gp_k-Hc9MFS6LWxfE3jgkCUYv3snk3oCNPruI-oz51E9dIXPXmL1N3fY4DN7wjWXe6XO1KtnNo8eE87dQnctWw_2B9yBZbWPNrwJXmlQOQMyUYhmsc8BwX4u9TkOF9VDDoNLa8Wm7n8WTCM8QBWBm1k0448Jo-DwtMEn95weMt4OxQ_6yfDBZaIR7QsxojApycpRXcoIja96Lk9-nz6VPltcFf9UKIxoXuBmlFemKGrjfZTwwP6C5_MJUDdalI4Q2N7vC28ZaSrEjbE5Q29RLr24_lE4OryhTsfIPCuRc3gDJ8oDs62g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mtGL1PzwKCrBu5msuW2C-6S9toaInSH5RcV6uOhO9M6wfbOdOZVXtaIGqcSJPWMN2oVwxomGMJM3qlN8a34sNgK9YFA0aUgkqdKSSFZrycMbXaWxS6WrgdfjnhgPCLNiMQ41DnmsEPWuu-RVl4gQd9ZuiBTkvqyBfpfHfpYDy8AY44JdQeguovFBNvQFEOU4s6N9ldnthn-NTB4vmspfeWbQDqax9e1JORBoCzwnYcep5kMTTTSIxeKt7Qzk1vzB0boukR69gzSAmrMKoBdaeeBbxNSkU5GunW6JiIg9UJFrl6sZfDSbdpRUzbPz-HugccruRAv4GPTkDI9w2tYZvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">منابع آگاه به رسانه‌های آمریکا گفته‌اند جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا (سیا)، در جریان سفر محرمانه خود به مسکو از مقام‌های اطلاعاتی روسیه خواسته است اطلاعاتی را که می‌تواند به ایران کمک کند، در اختیار تهران قرار ندهند. همچنین گفته می‌شود موضوع حمایت روسیه از ایران از محورهای گفت‌وگوهای او با طرف روس بوده است.
این دیدار در جریان نخستین سفر برملا شده یک رئیس سیا به مسکو از سال ۲۰۲۱ به شمار می‌رود. کرملین تایید کرده است که آقای رتکلیف با مقام‌های اطلاعاتی روسیه دیدار کرده، اما با ولادیمیر پوتین، رئیس‌جمهور روسیه، ملاقات نداشته است.
بر اساس گزارش‌ها، جان رتکلیف علاوه بر موضوع ایران، درباره نگرانی‌های آمریکا نسبت به امنیت کشورهای عضو ناتو نیز با مقام‌های روس گفت‌وگو کرده است. با این حال، مقام‌های آمریکایی و روسی جزئیات رسمی درباره محتوای مذاکرات منتشر نکرده‌اند و سازمان سیا نیز از اظهار نظر درباره این سفر خودداری کرده است.
@
VahidHeadline
وزیر خارجه روسیه می‌گوید مسکو با دریافت عوارض از کشتی‌های عبوری از تنگهٔ هرمز موافق نیست؛ با این همه به گفته او، این موضوع به مذاکرات بیشتر نیاز دارد.
به گزارش خبرگزاری اینترفکس، سرگئی لاوروف در گفت‌وگویی با تلویزیون «آربی‌سی» با اشاره به باز بودن تنگهٔ هرمز تا قبل از آغاز حملات اسرائیل و آمریکا به ایران در ۹ اسفند پارسال، گفت: ایرانی‌ها «تنها برای این‌که تنگه هرمز امروز کاملاً باز باشد، در حال بحث در مورد عوارض عبور هستند. تا زمانی که ایالات متحده و اسرائیل آن قمار را آغاز نکردند، هیچ عوارضی وجود نداشت».
لاوروف تصریح کرد: «آمریکایی‌ها اکنون از ایران می‌خواهند تنگهٔ هرمز را باز کند و ایران می‌گوید که در ازای آن باید تحریم‌ها کاهش یا لغو شوند. و آن‌ها این کار را خواهند کرد».
رئیس‌جمهور آمریکا روز پنجشنبه گفت که دیگر نمی‌خواهد با مقام‌های جمهوری اسلامی مذاکره کند.
ترامپ افزود: روسیه رفتار مناسبی در تنگهٔ هرمز داشته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 238K · <a href="https://t.me/VahidOnline/78069" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W0vq2hfGVRnI-MKeQfrBNFHeeYeiLF-ozlCdYqzQh4IzCdZVrvzPfRstVAKpfVDkh9hnx_oBeeYIENt0m29ST46hhhBTGCLQgTtFO8NNtf4RoIyKPAKG9wB0j395vh7LHJWs_K9CQj76XpA-O7qF8EsDHajqdRikXfndWWRUM2-DGYOw2gNset_RSyx8IjfoVk5CQXMHsSMZZ3vnVW3eA2F3V88jINzsankNEJJzIRYZLnbdnp1b7BmiSuc3WAXVwxneeYaoE1rgD6qappRe7YRXSsHyFOzG8K67WEvMiCOut8yoNYWoM8_JzrBM5YvjXuh6CIYQNADPxPaskB1aCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه جهان صنعت بر اساس آمار بانک مرکزی گزارش داد که تورم نقطه‌به‌نقطه در مرداد ۱۴۰۵ به ۸۴.۴ درصد رسید؛ رقمی که نسبت به ۸۳.۹ درصد در تیرماه افزایش نشان می‌دهد.
براساس این گزارش که صبح پنجشنبه ششم شهریورماه منتشر شده، تورم نقطه‌به‌نقطه در بخش کالا به ۱۲۱.۵ درصد رسیده و از افزایش چشمگیر قیمت اجناس طی یک سال گذشته حکایت دارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 225K · <a href="https://t.me/VahidOnline/78068" target="_blank">📅 16:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=riOESsR6PuXNmEZJMRUiy-pss1DfDH1ODLLqI0-NyIOo9UXgIZw4URnYq4btHuZ7qAOrr_n48xfJiNecG8MziTRRPqib0waOBGp7LLP9WllPr9PEFIxYEGB1R6Gr7Rulbc18f1GywRhChGbnlCme4f_FKAKSX3hwauP5opVvQKCcu9doTi7Q4RG-B-b0Q3D6-kGRVarFeSThhObn9ipX-8-4PSrjESUgZXQbhSIfgJzPu-3mUw-R_umIDSEFMiOedWDObx59fVmvVek_-YuUfbNvYq-l7YTzqux9rHzfCyi8zIbrDp_Q5dDM6hLExS12Vl0QcT-rWtIZcFUo8Hvajg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/67cc2d39e8.mp4?token=riOESsR6PuXNmEZJMRUiy-pss1DfDH1ODLLqI0-NyIOo9UXgIZw4URnYq4btHuZ7qAOrr_n48xfJiNecG8MziTRRPqib0waOBGp7LLP9WllPr9PEFIxYEGB1R6Gr7Rulbc18f1GywRhChGbnlCme4f_FKAKSX3hwauP5opVvQKCcu9doTi7Q4RG-B-b0Q3D6-kGRVarFeSThhObn9ipX-8-4PSrjESUgZXQbhSIfgJzPu-3mUw-R_umIDSEFMiOedWDObx59fVmvVek_-YuUfbNvYq-l7YTzqux9rHzfCyi8zIbrDp_Q5dDM6hLExS12Vl0QcT-rWtIZcFUo8Hvajg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک زن شاغل در حرفه قصابی با انتشار ویدیویی از وضعیت کساد بازار و تشدید فشار معیشتی مردم می‌گوید مشتریانی به مغازه‌اش می‌آیند و می‌گویند شش ماه یا حتی یک سال است گوشت نخورده‌اند.
مرکز آمار ایران در تازه‌ترین گزارش خود از ادامه جهش قیمت مواد غذایی در مردادماه خبر داده است.
در میان گروه‌های خوراکی شیر، پنیر و تخم‌مرغ و همچنین گوشت و فرآورده‌های آن، از جمله گروه‌هایی هستند که در ماه‌های اخیر افزایش قیمت بالایی را تجربه کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/78067" target="_blank">📅 16:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ei5_2OtpGJb2UmmwO_iULRgs3wp8TpZzP_IjBbHRggsobbltohHokumFr4w-e4jSvgw82jBxJA4dMvX2TUYqlcZxGGvriIuDzlgPns0iKJMYgSNR9rLzWvErh5RaA-vQ-jCXp8EDeAKpchpW12kWiFo4fE0xTnWDFKi_oe2b_nQRvn0_FGNu-siwn-dGyC2IO_PHyIM9GDRnwfOO3piRyeCsVP_PLWjFcovxAZpH_a8qtlPHoab8MrWU1dv024lozjDqv89K_Wi8VahM0yRdtEk570CM7QGU-ku5oW-3tqoRBsCTUNsZ8xnNvOX4jSBb-cst4jfmIyixPZU4UCBBlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رضا زنگنه، جوان ۲۷ ساله اهل روستای کلیل‌آباد ملایر و ساکن کرج، با اتهام «محاربه» به اعدام محکوم شده است.
پرونده او اکنون برای رسیدگی به فرجام‌خواهی به دیوان عالی کشور ارسال شده و در صورت تأیید حکم، این زندانی با خطر اجرای اعدام روبه‌رو خواهد بود.
بر اساس اطلاعات رسیده، رضا زنگنه روز ۱۳ فروردین‌ماه از ملایر به کرج بازگشت و روز بعد، ۱۴ فروردین، هنگامی که مغازه خود را باز کرده بود، مأموران به محل کار او یورش بردند و او را بازداشت کردند. شماری از مغازه‌داران و کسبه اطراف شاهد بازداشت او بوده‌اند.
زنگنه تعمیرکار خودروهای لوکس و خارجی است و هم‌اکنون در زندان قزلحصار کرج نگهداری می‌شود. او از ابتدای پرونده وکیل تسخیری داشته، اما خانواده‌اش در جریان رسیدگی قضایی، وکیل انتخابی نیز برای پیگیری پرونده معرفی کرده‌اند.
@
Tavaana_TavaanaTech
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/78066" target="_blank">📅 16:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Gt10maU3jUrEuzZbYtXt0bmgbpMoMIwn-hmoYfJ5LdEMqms74GWvhFLz-YNy9r_cBWrcLiCpV-2RmYqZBxgwu-cgnGwiYXNYGJ4RdTicZb4FKhIIWsB9ihZoOBTXVrQ0boTkNuaxHUjf97l4FyWI2uwrRg8L1pRwgHT2WuLAy8S54ZBBzyDE8FNZT-NUvh1BbBVL4o3Y5lgV_SyDzvJ1NJ6m2ISrcu-muiVfSM_E-Y5rbWt4ywBXmkw11txp0sBup1brF0YdkWo50R-e75NjsuttFEDBp7TNJQPJzAfaIENGXDjnQxiXp2nXGxNWqU7jKR1RmPxDKBEnKlUAQYG5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت دونالد ترامپ به میانجی‌ها اعلام کرده است که تمایلی به بازگشت به مفاد توافق اولیه ماه ژوئن با جمهوری اسلامی ندارد.
این موضع تلاش‌های تازه قطر، عمان و پاکستان برای احیای مذاکرات میان واشنگتن و تهران را با مانع روبرو کرده است.
روزنامه وال‌استریت ژورنال روز پنجشنبه پنجم شهریورماه به نقل از افراد مطلع گزارش داد که دولت ترامپ این موضع را بارها به میانجی‌ها منتقل کرده است.
توافق اولیه که با میانجی‌گری پاکستان شکل گرفت، بازگشایی تنگه هرمز و آغاز گفتگو درباره برنامه هسته‌ای جمهوری اسلامی و پایان جنگ را دنبال می‌کرد. در مقابل، کاهش تحریم‌ها و دسترسی تهران به دارایی‌های مسدودشده در نظر گرفته شده بود.
به نوشته وال‌استریت ژورنال، ترامپ اکنون فشار اقتصادی بر جمهوری اسلامی را در اولویت قرار داده و آماده است برای مشخص شدن نتیجه این سیاست صبر کند. آنا کلی، سخنگوی کاخ سفید، نیز گفت هیچ مذاکره‌ای با جمهوری اسلامی در جریان نیست یا برنامه‌ریزی نشده و محاصره دریایی و «عملیات طرد اقتصادی» ادامه خواهد یافت.
این گزارش در حالی منتشر شد که عاصم منیر، فرمانده ارتش پاکستان، اوایل هفته جاری برای گفتگو به تهران سفر کرد. وزیر خارجه عمان نیز برای دستیابی به تفاهمی درباره مسیر عبور کشتی‌ها از تنگه هرمز با مقام‌های جمهوری اسلامی گفتگو کرده است. نخست‌وزیر قطر نیز پنجشنبه پنجم شهریورماه در تهران با مقام‌های جمهوری اسلامی دیدار کرد.
وال‌استریت ژورنال نوشت اختلاف بر سر نحوه تفسیر توافق ژوئن و شرایط بازگشایی تنگه هرمز، دستیابی به چارچوبی برای ازسرگیری مذاکرات را دشوار کرده است. هم‌زمان، تهران بر اجرای مفاد توافق پیشین تاکید دارد، در حالی که واشنگتن مسیر فشار اقتصادی را دنبال می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/78065" target="_blank">📅 23:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=Astb5ir_HGmHOvOnZzRVMP5FAFLeMTVboZH3LT5S2YoS_3Df6lbzJeUFjUAp_W2q4HsGdplVI95VaQwaJ5f6XzLhWuMycDAMO82INQI0uV87L49qHvkiUkTng0eIVInW_vIL4SFbnblaZ1d7qhGo3wu93EDzBYQ_mcwILSnPjtBRGaVYE6DpI-sPkK3ZrLYAMmGo758dmzbVm3sOJ8sjN6WJbWFMghpgBf_vFQqDxcNMDPxWOJbajs9c8ThLf8OIByEKRepRf-IhTLkwlA6n3_0CKkulwTD1GUdgsBfj4DSgXU-XTH0zGQ-mlL1xPt3AuWZLhigk_Atjou6ebbj51g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0c8bbd6d37.mp4?token=Astb5ir_HGmHOvOnZzRVMP5FAFLeMTVboZH3LT5S2YoS_3Df6lbzJeUFjUAp_W2q4HsGdplVI95VaQwaJ5f6XzLhWuMycDAMO82INQI0uV87L49qHvkiUkTng0eIVInW_vIL4SFbnblaZ1d7qhGo3wu93EDzBYQ_mcwILSnPjtBRGaVYE6DpI-sPkK3ZrLYAMmGo758dmzbVm3sOJ8sjN6WJbWFMghpgBf_vFQqDxcNMDPxWOJbajs9c8ThLf8OIByEKRepRf-IhTLkwlA6n3_0CKkulwTD1GUdgsBfj4DSgXU-XTH0zGQ-mlL1xPt3AuWZLhigk_Atjou6ebbj51g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهوری ایالات متحده، در کاخ سفید و پس از امضای فرمان اجرایی تغییر نام «دریاچه اونتاریو» به «دریاچه آمریکا»، به پرسش‌های خبرنگاران درباره نحوه اعمال تحریم‌های ثانویه علیه کشورهایی که با جمهوری اسلامی ایران روابط اقتصادی داشته باشند، پاسخ داد.
ترامپ در واکنش به پرسشی درباره عملکرد روسیه در منطقه و برخورد احتمالی آمریکا در صورت تداوم معاملات با ایران گفت: «تا اینجا رفتار روسیه در رابطه با تنگه هرمز بسیار خوب بوده است.» او با تاکید بر تقابل پایاپای واشنگتن با سایر قدرت‌ها افزود: «باید در نظر داشته باشید در برابر هر کاری که آن‌ها انجام می‌دهند، ما هم انجام می‌دهیم.»
رئیس‌جمهوری آمریکا همچنین در پاسخ به نگران‌کننده‌بودن اقدامات پکن گفت: «یک نفر درباره چین می‌گفت شنیده‌ایم آن‌ها دارند جاسوسی می‌کنند؛ ما هم از آن‌ها جاسوسی می‌کنیم. وضعیت همین‌طور پیش می‌رود.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری ایالات متحده، روز پنجشنبه پنجم شهریورماه، فرمان اجرایی جدیدی را امضا کرد که به موجب آن دستور داده شده نام «دریاچه اونتاریو» فورا به «دریاچه آمریکا» تغییر یابد.
ترامپ پیش از امضای این فرمان در دفتر بیضی کاخ سفید اعلام کرد: «ما نام دریاچه اونتاریو را تغییر می‌دهیم و این تصمیم از همین لحظه لازم‌الاجراست.» بر اساس اعلام یکی از مقامات کاخ سفید، این فرمان وزارت کشور آمریکا را موظف می‌سازد پایگاه داده‌های جغرافیایی ایالات متحده را برای بازتاب این نام جدید به‌روزرسانی کند.
این اقدام نمادین پس از شکست مذاکرات تجاری میان واشنگتن و اوتاوا، وضع تعرفه‌های تلافی‌جویانه و تیرگی شدید روابط میان دو کشور همسایه رخ می‌دهد.
با این حال، مقامات کانادایی پیش‌تر صراحتا اعلام کرده‌اند که این تصمیم یک‌جانبه واشنگتن را به رسمیت نخواهند شناخت و نام این دریاچه مرزی مشترک در خاک کانادا همچنان «دریاچه اونتاریو» باقی خواهد ماند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/78064" target="_blank">📅 23:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78063">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PM-3Ouro7-k5rhyV6WIkevm0zIEdcHTKAvFXpbuWesaUBmkgoMYyfrH8oVQ2BJ07xixN9u3yIIzJpec1WGcQ4-9DPLAeOy19GYe4ogsmhrhxYo1AH-lA9WZOTVTzwPtNZ_BkBfyhkZaCFUjU_0UiBSoHp2JF-niieTU_F92PQvsDk8x4v0-pQ-nqQnxApEWXBtzWgQwDacb78G9drBJkJoypweoaJFBWtz5aGon3DYK3gQROVdfAanxull-fR2SeXsNxLJ7b1iO6vWb_0GWJLjPqtalLBDMPYiQYywBUZkr5xkukJvF3iF8bB4qUHgqEoh-JOO_nDBw8A64FhrgUjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان اطلاعات سپاه روز پنجشنبه ۵شهریور۱۴۰۵ با انتشار بیانیه‌ای نسبت به تشدید نارضایتی‌های اجتماعی هشدار داد.
در این بیانیه به ناکامی «دشمنان ایران» در «تلاش برای تغییر حکومت ایران از طریق حملات نظامی» اشاره شده و آمده است: «مخالفان جمهوری اسلامی در حال تغییر راهبرد خود هستند.»
این نهاد نظامی و امنیتی مدعی شد که فعال کردن بحران‌های داخلی، جنگ روانی، فشار اقتصادی و عملیات‌های امنیتی از محورهای این تغییر رویکرد است.
سازمان اطلاعات سپاه در این بیانیه نسبت به افزایش نارضایتی‌های اجتماعی و احتمال اعتراضات خیابانی هشدار داد و گفت مخالفان جمهوری اسلامی بر «برهم زدن ثبات و کاهش تاب‌آوری ملی» از طریق «نبرد شناختی و تولید ترس و ابهام» تمرکز کرده‌اند.
این نهاد همچنین از شناسایی آن‌چه «ساختار محرمانه و اختصاصی» موساد، سازمان اطلاعات اسراییل برای اعمال فشار از داخل ایران خواند، خبر داد و مدعی شد این ساختار از طریق ارتباط با گروه‌های مخالف، انجام عملیات خرابکارانه و به‌کارگیری عوامل محلی فعالیت می‌کند.
در این بیانیه ادعا شده که جمهوری اسلامی از وضعیت «صرفاً پاسخ‌گویی» به حملات خارج شده و در پی افزایش نقش خود در تعیین روند جنگ و دیپلماسی است.
در بخشی از بیانیه منتشر شده آمده است: «ایران دیگر صرفاً در موقعیت پاسخ به حملات طرف مقابل قرار ندارد» و به سوی «افزایش ابتکار عمل راهبردی و اثرگذاری بر زمان، مکان و هزینه جنگ و دیپلماسی» حرکت می‌کند.
سازمان اطلاعات سپاه همچنین ادعای حاکمیت ایران بر تنگه هرمز را تکرار کرد و نوشت توانایی‌های نظامی و «نامتقارن» جمهوری اسلامی حفظ شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/78063" target="_blank">📅 23:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78062">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/K2Dz7XeiglVMUmFakZ4APL2VI5dMgZlYgeGFTiMV6--xhPQ4W0gN4p4X9iL1u5-9UU95yXAzapTnSQoFnpe3-XK-5-aXINdXAJ37_XUlvMUEhVBasZNyS6DtOnnjleR0C5I_yPdni2t4O3Ab4A_B77lxGRzD1PIUHzxQ3IjPMCWRiqP8RjJpKzYL0jIX1u2L-axNL7Sys3Efg3F8dCYEWJhvWkhMlrOM_QxtGD3j6t1QZsHCVFnihKym6XLA6z4BFuAng-MKCydFGvnO0Wz0HfLxIumNncl9P6XhT02qO175-ybepWEv_loykRYXVpums_hsNfmiznOARDTjzjHIWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اجرایی رئیس‌جمهور ایران تأیید کرد که دولت جمهوری اسلامی به‌دلیل محاصرهٔ دریایی آمریکا نمی‌تواند بنزین وارد کند.
به گزارش خبرگزاری ایرنا، محمدجعفر قائم‌پناه، شامگاه چهارشنبه چهارم شهریور، ایجاد تغییرات در قیمت حامل‌های انرژی شامل بنزین و گازوئیل را لازم خواند، و در توضیح دلیل آن گفت: «توزیع بنزین عادلانه نیست و تداوم این مسیر غیرممکن است. ضمن این‌که تولید بنزین کفایت نمی‌کند و با محاصرهٔ دریایی آمریکا نمی‌توانیم بنزین وارد کنیم.»
این مقام دولت ایران در عین حال گفت مشخص نیست این تغییرات به چه میزان و چه زمانی انجام می‌شود.
در روزهای اخیر، هم‌زمان با افزایش اظهارنظرهای مقام‌های جمهوری اسلامی دربارهٔ لزوم افزایش قیمت بنزین، گزارش‌های مختلفی از تعطیلی برخی جایگاه‌های عرضهٔ سوخت در تهران و تشکیل صف‌های طولانی مقابل آن‌ها منتشر شده است.
بر اساس آخرین آمار اعلام‌شده، تولید روزانهٔ بنزین در کشور حدود ۱۱۵ میلیون لیتر و مصرف آن حدود ۱۲۹ میلیون لیتر است. به این ترتیب، میزان تولید روزانه روزانه حدود ۱۴ میلیون لیتر کمتر از میزان مصرف است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/78062" target="_blank">📅 19:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fNfrP-hz-AOz-YozUovIVRNHebk9bKFg-oJ0Z-ClMnQ6HnTRv3joAQyHSOtXiArfQy8-8LfzJRMZe_dEGClxJ900pcbcfiDC4fIgzveSbD-RxaJKlcFUHodiplwm0z2h4rPIeFqzwQFA7ywZzTeinVW4e7J-bWSo2xIJIvhh5PuGytzd11wrsSW0NKfbZ_-3q1NVenOxD8PqHUzLTbj0Stp8_yMTCy_h4FMgHxn5_9XwgAaFTROpLq-N1oRy7DjtKauchH6TvvYYdqV2Bk7kQaVlOieSME6J4t0GEcX4rn-MSOfOUV3loCCbvvp7V0Fu9qlMDnORMOpoCjo05N70AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SRFza_7D8ZcNkXctUAv4IWgNMscC54aa4XFdeM5OLyNnD0Oz-gnHmKKpdND9JmvIPRbTt6V2I3851BJshOFKgAkCe4-2lKDVsH6hr56Jr6exy1jGJejLEQowOw7uBqTW6Xh-rlUXV8zqhC1t63xYXpeqIB2DNBfk9HbTQUjQIIdFmsQqYHvKNr2WG83i5qUBLeH_fgUCS8ft19xjuDipVD8loHCHO9QljM1QhuIg-YbYA2Bolwq3ONUUnNAr5suNApQ8BFRh4ySWb-aMPDaOLkwTbPMJaogl4TpjKW2DjCsENjHPosM7jaYsiFdZr-x5YUncd84mjCZ4PjX22QPZ-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محمد بن عبدالرحمن آل ثانی، نخست‌وزیر و وزیر خارجه قطر، در سفر به تهران با مسعود پزشکیان دیدار کرد.
وزیر خارجه قطر در این سفر با محمدباقر قالیباف، رییس مجلس شورای اسلامی نیز دیدار کرده و درباره راه‌حل برای از سرگیری مذاکرات میان واشینگتن و تهران گفت‌وگو کرده بود.
@
VahidOOnLine
وزیر خارجه قطر همچنین به قالیباف گفته است که گفت‌وگو بهترین راه برای حل اختلافات و جلوگیری از تشدید بیشتر تنش‌ها در منطقه است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 266K · <a href="https://t.me/VahidOnline/78060" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hoR9ZzlDsTq0jRWDhuJxdIz9umJHOlejAayp52WhDSa54YP1Giodvra1y1dWq8QKwUO-fUMlJNDT8xZQ4WeBcbazm8vxlpK2kXETCc6KOQ_3s8_l4_SfjDQaabV7jrJ2WQ2pcmzRyob9nXdqCqqVGJs4tM86rLGDyChqhtJFiYb8uZGcDbic0hnmFl6mGUK1UoRiWav_9s0z36s9dPP4gp0_y1PrvPZgeMV60_sXXFE8RWgHd3gifSB52ExOBPVRz4bYtYURGhfB-ItaDHku1UxjNa6GyY-V3L3CoFVP67tORH9sEpWcyekpp-LLVI1XIJswWIwr1NHyk06pn-49rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسیه رمضانی، زن ۳۹ ساله و مادر دو فرزند، در جریان سرکوب اعتراضات دی‌ماه ۱۴۰۴ در تهران با شلیک مستقیم نیروهای جمهوری اسلامی کشته شد.
ماموران بامداد جمعه ۱۹ دی ۱۴۰۴، از فاصله‌ای نزدیک و از پشت به رمضانی شلیک کردند. گلوله پس از عبور از پشت و قفسه سینه، به قلب او رسید و جانش را گرفت.
آسیه رمضانی مادر یک دختر نوجوان و یک پسر دبستانی بود.
خانواده‌اش می‌گویند پس از تیراندازی، او را به یک درمانگاه منتقل کردند؛ اما بدون رسیدگی پزشکی موثر، برای حدود پنج ساعت در حال خون‌ریزی رها شد.
خانواده رمضانی پس از بی‌خبر ماندن از سرنوشت او، سه روز میان پزشکی قانونی کهریزک و بهشت زهرا در جست‌وجویش بودند تا سرانجام پیکرش را پیدا کردند.
خانواده، زمانی که پیکر رمضانی را یافتند، گونه‌اش کبود بود و از زیر کاوری که پیکر را در آن قرار داده بودند، همچنان خون دیده می‌شد. آن‌ها گفته‌اند پیکر او در شرایطی «ناشایست و دردناک» نگهداری شده بود.
خانواده رمضانی همچنین می‌گویند لباس‌ها، کفش‌ها و دیگر وسایل شخصی او برداشته شده و به آن‌ها تحویل داده نشده است.
آن‌ها پس از تحویل پیکر متوجه شدند قلب رمضانی که با گلوله شکافته شده بود، بدون اطلاعشان بخیه زده شده است. خانواده آسیه رمضانی در روایت خود نوشته‌اند: «ما آن سه روز را فراموش نمی‌کنیم. آن پنج ساعت، آن خون، آن کاور، آن قلب شکافته‌شده و وسایلی را که باید به خانواده‌اش بازگردانده می‌شدند، فراموش نمی‌کنیم.»
آن‌ها تاکید کرده‌اند که همه واقعیت‌های مربوط به کشته‌شدن او هنوز روشن نشده است و افزوده‌اند: «هزار سال هم که بگذرد، خون عزیزانمان پاک نمی‌شود. نامشان را تکرار می‌کنیم، روایتشان‌ را زنده نگه می‌داریم و دادخواه می‌مانیم.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/78059" target="_blank">📅 17:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v5GQBEI83cZ-VqqTba5cfGjsvqnd2vP0Qjni9B4YIw-EN-5zzvwj5rp4OKTfwH8Ao7VbSzxYXzAmu0OqaFTcgZLA3hxyZhgemraYIXRYMVLe-lSBmjvQ6zNw3pjlscJIYYBBqoFcfkSI9IHmCDxU2bpHDLCAFDeranMrzMYmlBmkIB-F3V_Wh0DsxkLxlke26qCFBJPKYSBjuIB-QMTLAYJWhnHXzZ4FqANN6-ip8tu2tNekF5rfe7XPpkDNUPVnYyj2LKFM9N8AuMdm3g-6ONnZyDbJsqXVLX4alL054909WFcry7PFqMstl8sWUbFk9cn6CmXGdDuJxqmTE56Ihg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده، با انتشار پیامی در شبکه اجتماعی ایکس، با انتقاد از سیاست‌های مالی جمهوری اسلامی، خواستار اختصاص منابع مالی کشور به مردم ایران شد.
بسنت در پیام خود نوشت: «در حالی که مردم ایران برای تامین نیازهای اولیه خود با مشکلات معیشتی دست‌وپنجه نرم می‌کنند، حکومت فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.»
وزیر خزانه‌داری آمریکا در ادامه افزود: «حکومت ایران به جای تزریق میلیاردها دلار به گروه‌های نیابتی تروریستی خود، باید این پول را صرف مردم کشورش کند.»
این اظهارات هم‌زمان با تشدید کارزار تحریم‌های مالی ایالات متحده برای محدود کردن دسترسی حکومت ایران به منابع ارز خارجی مطرح می‌شود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/78058" target="_blank">📅 17:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s7gG3jpBiaf9-ORZEkWsl4t-9AJ6thIxKIcvFEnnFx9TAH3Oam-PoTPoONTpHcWgLIJr0D8Y-baDpFeoQY7HXRsPRoxhd7BE2R2Mmg8WHHDSJVBR6TSLIepctfv8a7TmpSh8dA3KFCFg30PJEWNi58a0ITcVRedQEE7HE-AucBqJ5gRcEloQtSe1GJhTTd-E5tfmwvLOxD98IibFC9lrn4XKnFNw_VjBoWd1YW_Bq_u8lnvm47VjQtsXYC86ZmITgRtu5WwbptvsPIR9RdQSRTbumXilNYySdzd7G7vZPx_Y2tJLVJjPp3paemFKfDmLZ85OQvUjytle2IFyxFRWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت نفت شاخص برنت در پی بهبود وضعیت تردد کشتی‌ها از تنگه هرمز و انتظارها درباره مذاکرات مثبت میان ایران و قطر روند نزولی خود را ادامه داد و روز پنج‌شنبه به ۸۶ دلار و ۷۵ سنت رسید.
قیمت نفت طی روز جاری نسب به روز چهارشنبه بیش از یک دلار و نسبت به هفته گذشته حدود هشت دلار افت کرده است.
در پی سفر وزیر خارجه عمان و فرمانده ارتش پاکستان به تهران طی روزهای گذشته، اسماعیل بقائی، سخنگوی وزارت امور خارجه ایران، روز چهارشنبه اعلام کرد نخست‌وزیر قطر نیز قرار است به زودی به تهران سفر کند.
هم‌زمان وزیر خارجه قطر در تماس با همتای ایرانی خود بر حمایت دوحه از تمام تلاش‌های دیپلماتیک و اقداماتی تاکید کرد که هدف آن دستیابی به راه‌حلی برای تضمین آزادی کشتیرانی و فراهم کردن زمینه توافقی جامع برای برقراری صلح پایدار در منطقه باشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 239K · <a href="https://t.me/VahidOnline/78057" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78056">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CNhsFJl2T3kogalpE2tWsdsSU9kcuon70v8lbK5aQOyf-9mdyp8fw1ZM5nc69An5kukJ1wscOeD0BMrrvOm3iGNm_nj5fnCYv2wNSLdY2F-Pq8YrzYgO2IhMDmd28xMsgzKowJOVrQvHyQHeK91_1kDkRItzsHwQj-DtlQg-TVXm-oWl4ZZmkR6yKVg0w_vNmH_a89nAALOhcRohR0FQvcuJ2CB14u7Kam47ODlPtgVFjFJWWm6jaRLNjLyyYbMqkctc_slp2YsLm8zuWPrVxcsVJWea_zqxKXUryfnU5RNfxOgRSIziuSpHKWQkuf1sufHddHOqkixcmX8j8zRR6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاوه مدنی، پژوهشگر و متخصص ایرانی حوزه آب و مدیر مؤسسه «آب، محیط‌زیست و سلامت» دانشگاه سازمان ملل در کانادا روز چهارشنبه چهارم شهریور جایزه آب استکهلم ۲۰۲۶، معروف به «نوبل آب»، را از کارل گوستاف شانزدهم، پادشاه سوئد، دریافت کرد.
این جایزه در مراسم رسمی هفته جهانی آب در استکهلم به پاس پژوهش‌ها و فعالیت‌های کاوه مدنی در زمینه مدیریت منابع آب، حکمرانی آب و ارائه دیدگاه‌های نوین برای مواجهه با بحران آب به او اهدا شده است.
کاوه مدنی پیش‌تر در ماه مارس به‌عنوان برنده این جایزه معرفی شده بود و کمیته جایزه، از پژوهش‌های او در مدیریت منابع آب و پیوند دادن علم با سیاست‌گذاری، دیپلماسی و ارتباطات عمومی تقدیر کرده بود.
جایزه آب استکهلم از سال ۱۹۹۱ به صورت سالانه اعطا می‌شود و مراسم آن را بنیاد آب استکهلم با همکاری آکادمی سلطنتی علوم سوئد برگزار می‌کند.
این جایزه که شامل یک میلیون کرون سوئد و یک تندیس کریستالی است به افراد یا سازمان‌هایی اهدا می‌شود که دستاوردهای برجسته‌ای در حفاظت، مدیریت و استفاده پایدار از منابع آب داشته باشند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/78056" target="_blank">📅 17:24 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V0B1ZFkbWR5PCqxIi9e1tLuuqEbyuXQfBePXlztZvW6d9N_XisXVvfZkmI6EBQOJexO6P_VY8YCJVeI4iA1l5qavqi8jUb-sFWHkI3rW5ks6q5Y_zKQ_EIKiZKcSu_-tOkGacFhZ9K12hvNbW3WFvoLZvX-1b5SELx3CUGoxXd_ExOnyaAE-eyyU0gW1E_EG8ajwEzDKwKNrPAHRXkE7kDIz5cucokNFCM3qkRSeBE_v10uci56cxxZTk_kezph5ggz0IZSH2U8AsPqcouiPwwoNQ14ZeLgpDUNWk6HI9_UXu5iu97iGteW0DBK8bmOdUgjcSymRKoeiWSsaD9mtBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیلا ابوالحسنی، از بازداشت‌شدگان اعتراضات دی۱۴۰۴، به اتهام «محاربه» به اعدام محکوم شده و پرونده او پس از اعتراض به حکم، اکنون در دیوان عالی کشور در حال بررسی است.
لیلا ابوالحسنی، حدودا ۴۳ ساله و مادر دو نوجوان، از ۱۸دی۱۴۰۴ در زندان دولت‌آباد اصفهان نگهداری می‌شود.
یک منبع گفته است که ابوالحسنی روز ۱۸دی در شاهین‌شهر و هنگامی بازداشت شد که در حال عکس گرفتن از آتش‌سوزی یکی از فروشگاه‌های «افق کوروش» بود.
به گفته این منبع، دستگاه قضایی او را به دست داشتن در آتش‌زدن این فروشگاه متهم کرده است؛ اتهامی که به صدور حکم اعدام علیه او منجر شده است.
در حال حاضر، دیوان عالی درباره اعتراض او به حکم اعدام در حال بررسی پرونده است.
لیلا ابوالحسنی از زمان بازداشت تاکنون، بیش از هفت ماه را در زندان دولت‌آباد اصفهان سپری کرده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 283K · <a href="https://t.me/VahidOnline/78055" target="_blank">📅 17:22 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/e5q146Z1xDmwCwsYWjEHRK7TVDfakFAdw6GFGTYs9bqfY9-H_RdzSwHJOS15_uxOg1aZ-W6rWMmsWeBvMz9-q8DrL98Oo6agucnr1EeIiIzHqzKChtCdIdeRI10dlyjdfXgYs4y4nBvaPGCVw8NONsEq2EqrV1TMT-TCSCYUnFVyoiyeFNcOH5cWdL45NrI_HiDTSAMtKMBcDYzWNey4gfZi4yTEpEAxfaKJQP-x7F4jekxYO9wB8YHRC8mbrKajL9CU42KHht_XRlco5YcbGNNMsxSp33oiZif-URaxIda-qHssJNieiWluIEpuZTIBuHMqwY616r_olsordx9VZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">UKMTO:
مرکز عملیات تجارت دریایی بریتانیا گزارشی از وقوع یک حادثه در تنگه هرمز دریافت کرده است.
مقامات محلی گزارش داده‌اند که یک نفتکش با پرتابه‌ای ناشناس هدف قرار گرفته و در پی آن کشتی دچار آتش‌سوزی شده است؛ آتش‌سوزی از آن زمان مهار شده است.
گزارش شده که همه اعضای خدمه سالم هستند و حضور همه آن‌ها تأیید شده و هیچ گزارشی از پیامدهای زیست‌محیطی دریافت نشده است.
مقامات در حال تحقیق درباره این حادثه هستند.
UK_MTO
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/78054" target="_blank">📅 05:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=nMaJ6Q8R1cMC5tAlPBuD64agg5mRGGpM7x8XdWS3_BITeIlK6kSOVG55Gd7n4P_oodkAF9DXNPvB8iCpkNFwgqMl0EgxNj55_ppb0OwnJEQxdxE5Y6AG5u9bctfWZjt6c1md5R_rCBG-EOuAeCIbDiETL0bWu5cD9_SfvBbuN4GBMKJjbab9JZdrjAzmdTUUF9CMRX-9L0GUGCdxDq2eNpM98BYWGBg96ZknAEffEphsQsNX2vZ1gGetNbUlK00Px6Kq0mylcqHyXcWLrjrQ3Ad5wXDymhc7xugIRB3ZzEntTOO30oO5P7ESWUlIMjATDI8xf1SOtjqmimJu02GLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b0498b32fb.mp4?token=nMaJ6Q8R1cMC5tAlPBuD64agg5mRGGpM7x8XdWS3_BITeIlK6kSOVG55Gd7n4P_oodkAF9DXNPvB8iCpkNFwgqMl0EgxNj55_ppb0OwnJEQxdxE5Y6AG5u9bctfWZjt6c1md5R_rCBG-EOuAeCIbDiETL0bWu5cD9_SfvBbuN4GBMKJjbab9JZdrjAzmdTUUF9CMRX-9L0GUGCdxDq2eNpM98BYWGBg96ZknAEffEphsQsNX2vZ1gGetNbUlK00Px6Kq0mylcqHyXcWLrjrQ3Ad5wXDymhc7xugIRB3ZzEntTOO30oO5P7ESWUlIMjATDI8xf1SOtjqmimJu02GLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی نیروهای مسلح: رسانه‌های فارسی‌زبان در بانک اهداف نظامی ما جای می‌گیرند
1:11
سخنگوی ارشد نیروهای مسلح جمهوری اسلامی،  در مصاحبهٔ تلویزیونی با خبرگزاری «دفاع مقدس» مدعی شد رسانه‌های فارسی‌زبان خارج از کشور مستقیماً به «موساد»، «سی‌آی‌ای» و «سازمان‌های اطلاعاتی دشمن متصل هستند».
به گفته ابوالفضل شکارچی  «نیرو‌های مسلح جمهوری اسلامی به این بنگاه‌های خبرپراکنی به‌عنوان رسانه نگاه نمی‌کنند» و کسانی که در این رسانه‌ها کار می‌کنند را به عنوان «سربازان صهیونیست و آمریکا می‌بینیم و حتی می‌شود آن‌ها را در بانک اهداف نظامی خود پیش‌بینی کنیم».
@
VahidOnLive
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 339K · <a href="https://t.me/VahidOnline/78053" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PrMJNWggZxn310QbBqR7NtjFCHZB1GflqrusTusjX_FR1IzPlVQvYXb596-CWocL0GIZClZl-J3lcIysjWruj4Br09wGBi29QOBNoEkUDvbJQ98wtbw4kwee284Q-nvIgzRNq_buCmHyra6CaUrS-60K-4v5_Jf2iDVbvgQm6g6Ztk5qJ0XT5wZD2P6mS_YG6a3Ukw4S0XhzZH_unsVkzbbE9Bx8HtIOkL3qoM9n7Iz8W12OTVDN3EDfY6iQZMAYvmyDTvVH_L7radYcuxsdR7KRQW-MppeXnD2Ls-AbgFRETQNqy1onQ1a9TZ2X-bj11oUDzbKXQ0y3LY3VsOM-Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/me80LUKACqlTXEbzby573huRs71hA_0Vd0JZxgwllVVP-1rrBTIrqMHrwQOB6uTafg8aQ_QB8Cjuc3P-SEAA7UerQafwY9k_Rgmz7aoNSfu32ZPnmbM74M4xxfG-8sZeqnwBmtFaViywB4ZEP1Qqv-Z-X21DFUYb3cX0zrH377byJbdIQxp6Ezle5SuxS0UjGfdUmFv2ABKJs7otqfyODL0_60JtKYnMP_xJlPTZPur31Zv_b0KlWwJZqAJyFqLfoMZjnpVlJptk8oBP9znuFhgUM2OBy9iuVfKNXsWrf7MmmdGDdWvsHU-p4qakzyFfRZ2SF1xJRUwegPqbjQzSbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ درباره اعتراضات در ایران اعلام کرد «فکر نمی‌کنم وقتی یک مسلسل روبه‌روی شما باشد، آنجا بایستید؛ تک‌تیراندازهایی واقعا بالای ساختمان‌ها هستند.»
او گفت: «مردم هنگام اعتراض هدف گلوله قرار می‌گیرند و جمهوری اسلامی برای ایجاد ترس در میان جمعیت، لزوما نیاز ندارد تعداد زیادی را هدف قرار دهد.»
او افزود: «وقتی می‌بینید پنج، شش یا ۱۰ نفر در میان جمعیت ۱۰۰ هزار یا ۲۰۰ هزار نفری به زمین می‌افتند، مردم محل را ترک می‌کنند. فرقی نمی‌کند چه کسی باشید، می‌روید. وقتی افرادی آماده‌اند به شما شلیک کنند و شما را بکشند، اعتراض کردن بسیار دشوار است. به همین دلیل است که آنها اعتراض نمی‌کنند.»
ترامپ گفت: «نیروی دریایی‌شان همان‌طور که می‌دانید، کاملا از بین رفته است. نیروی هوایی‌شان کاملا از بین رفته است. بسیاری از سربازانشان حقوق دریافت نمی‌کنند. فکر می‌کنم تورمشان ۳۹۰ درصد است و پولشان تقریبا بی‌ارزش شده است؛ منظورم این است که وضعیت خوبی ندارند.»
@
VahidOOnLine
دونالد ترامپ، رئیس‌جمهوری آمریکا، روز چهارشنبه چهارم شهریورماه، در مصاحبه رادیویی با گلن بک اعلام کرد که وضعیت حمل و نقل انرژی در تنگه هرمز به حالت عملیاتی بازگشته و حجم بالایی از نفت از این آبراه در حال عبور است.
ترامپ با اشاره به اقدامات انجام‌شده برای پاک‌سازی مسیر گفت: «ما از شر مین‌ها خلاص شدیم و این تنگه اکنون فعال و در حال کار است.»
او با اذعان به وجود برخی تهدیدهای پراکنده افزود: «بله، هر از گاهی پهپاد، راکت یا چیزی شلیک می‌شود، اما تنگه کاملا فعال است و نفت زیادی از آن خارج می‌شود؛ به‌طوری که همین دیروز ۱۰ میلیون بشکه نفت از این آبراه عبور کرد.»
@
VahidOOnLine
دونالد ترامپ، رییس‌جمهوری آمریکا، چهارشنبه چهارم شهریور در مصاحبه با برنامه رادیویی گلن بک گفت فکر نمی‌کند مجتبی خامنه‌ای، رهبر جمهوری اسلامی، کشته شده باشد.
رییس‌جمهوری آمریکا اعلام کرد: «او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دستش، پایش، همه این قسمت‌ها به‌شدت آسیب دیده بود.»
ترامپ همچنین افزود حتی اگر مجتبی خامنه‌ای مرده باشد، جمهوری اسلامی «نمایش خوبی» اجرا می‌کند.
ترامپ گفت: «جمهوری اسلامی همچنان درباره مراجعه به رهبرشان برای گرفتن تایید نهایی در امور مختلف صحبت می‌کند.»
رییس‌جمهوری آمریکا همچنین افزود توافق با جمهوری اسلامی آسان نیست و آن‌ها «چندان پایبند به اصول» نیستند.
@
VahidOOnLine
دونالد ترامپ روز چهارشنبه چهارم شهریورماه، در گفتگو با شبکه الجزیره اعلام کرد که هم اقدامات اقتصادی و هم گزینه‌های نظامی «اثربخش» هستند و او در رابطه با مذاکرات با ایران «عجله‌ای ندارد».
او در پاسخ به پرسش‌های تانیا نوری، خبرنگار این شبکه، افزود: «من هیچ جدول زمانی ندارم؛ هیچ عجله‌ای در کار نیست.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/78051" target="_blank">📅 17:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I26Q4XLnocMwJDLltBBg4GgCxi8KHKISC1TkGLVaRfgb-pN3uEj5A365m3Tjwi1koY5a6hY4vDNf6hkSO5wSTgfDJY-8LPRQEeqC-fQgdlQoNAQL407B8gS_L25jG_ucIuRu_couCRPMI6mWEruMDdg9Mf5eY3_koC2gIpKfIxKC40NKXRoI3Lt7jb1A7lqtibyj4VlZCFPEGDIpMf9dPyO89WaZ_Jni03ukgwmn4thuih8Dj3fjW90ZduBzI5XgdTE5O_Qn6qqbyhsY3yJkVZeIEqMXJFOvhpUHy61IHfztP0vOiad5xrmFduXz9Ivge2rt4Dax2gubbbV8zUM51Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران، بار دیگر موضع قبلی خود دربارهٔ ضرورت پایان دادن به جنگ با آمریکا را تکرار کرد و گفت: «جنگ همیشه راه‌حل نیست. گرهی را که می‌توان با دست باز کرد، نباید با دندان باز کرد.»
پزشکیان روز چهارشنبه چهارم شهریور در یک مراسم عمومی بار دیگر ایران را «پیروز میدان» خواند و در عین حال افزود می‌توان با «تدبیر و اندیشه» از این مسیر عبور کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 304K · <a href="https://t.me/VahidOnline/78050" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/j0x_oR5GZpO7wQ3x8aiT9p4xc5u0ZEKpbVoKvHUthqNK6QwOytkClt4Efe45awiM8FZIP2XN36UhoAE41rWULxPw9tTUu1CF26t4d-RVrJkgjOeqCBUXUZibFtGsGZGXwn2sa5xuBPu38DBDzN_t1PxmdrgDV4YL_Y86w6h9FhzgI_U1C5XupCOP8LNJald3e_ORuk7pSX0f0Dxx2vCMa_PB9etxw7fdp53DdUZHstTEKzIZAaX-eN6goNKhOr2R8KsZo0NrfoXmEVwwxLeDQb4Ln2HMevAIQ5Va9gSOGaWCL0FS_5Je93bWnFzMFtrdEkOzBgqGYmtPwIVUxy_T7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری هرانا گزارش داده است که حسین نظری، شهروند ۲۵ ساله و از بازداشت‌شدگان اعتراضات دی‌ماه ۱۴۰۴، توسط شعبه اول دادگاه انقلاب مشهد به اعدام محکوم شده است.
بر پایه این گزارش، دستگاه قضایی جمهوری اسلامی آقای نظری را با اتهام‌هایی همچون «ارتباط با دول و گروه‌های متخاصم» و «اجتماع و تبانی برای ارتکاب جرم علیه امنیت کشور» محاکمه و حکم اعدام او در تیرماه سال جاری صادر شده است.
نظری، متولد ۱۳۸۰، در جریان اعتراضات دی‌ماه توسط نیروهای امنیتی بازداشت و پس از طی مراحل بازجویی و قضایی به زندان وکیل‌آباد مشهد منتقل شد. او همچنان در این زندان نگهداری می‌شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 274K · <a href="https://t.me/VahidOnline/78049" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
