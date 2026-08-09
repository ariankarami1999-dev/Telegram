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
<img src="https://cdn4.telesco.pe/file/QY_HU2Yya9aMPyMnYzbNS4r6mShy8fDFDAzZng6aOkZmFv8h79511l63oGc_309f3nwCu-3SuB6AYW6vGKlHUPpJsGhuKYo34PC2FvNMrzC7MZWk8kwfZZ0HSDwaj1iA1KPtIySxiZqRUo_wmy0yccCMxxRxONg13ZaDsv6ZdyMS5iHAXYlWsDKeCTD8aXnnFfMeaKVHMDL0gv9f4WchFkngDHRXRB8TesR5cYI44K4FcoieOAJBRGMvXSVDSrNn19wFXTO7U1uHbbGzMLuHROnu7w6dPsXcCoFgNzDzuoXe4j0CUgEDtUnsElDdW8alkzUmr1Us7QlPFpOMeWnFgQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 446K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 00:29:48</div>
<hr>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=nuBklJ_qhd1YNAwBJxTier4VgHHoTxjJ_SUT67kgOK6vBcOhyhUuB0-KZjUWEsjsp58QVCiLvwsXJ7qXGo-ta1QVebLaz6PX-3gw-NuuM6PDcvY4_8ERJZRYqXyrgk61sMz0gwfv6JQE1kbIKZDbk9OMSu5xtuD0o91BXsfW8_FO9ttKNQuvkFsDMt7wcOsM2IPD_VetSfmFCfWWWaKOP2v_kzd63YcrXGz4xzoeXmc8KrWJCeca9U69WZDvYgF0PysddTxu-7AjBu17Nvy5zAKJcDoOjQJY6VQBjKO4dVeFy5I-rZZtcDP0DfBcR2Z_tazQYyF7hBt4eZGDYCGycg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd95915a0b.mp4?token=nuBklJ_qhd1YNAwBJxTier4VgHHoTxjJ_SUT67kgOK6vBcOhyhUuB0-KZjUWEsjsp58QVCiLvwsXJ7qXGo-ta1QVebLaz6PX-3gw-NuuM6PDcvY4_8ERJZRYqXyrgk61sMz0gwfv6JQE1kbIKZDbk9OMSu5xtuD0o91BXsfW8_FO9ttKNQuvkFsDMt7wcOsM2IPD_VetSfmFCfWWWaKOP2v_kzd63YcrXGz4xzoeXmc8KrWJCeca9U69WZDvYgF0PysddTxu-7AjBu17Nvy5zAKJcDoOjQJY6VQBjKO4dVeFy5I-rZZtcDP0DfBcR2Z_tazQYyF7hBt4eZGDYCGycg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ
نیوجرسی را ترک کرد و جواب خبرنگاران رو هم نداد، تا ساعاتی دیگه میره دم توالت شروع میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/withyashar/20740" target="_blank">📅 00:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شبکه i24 NEWS: اسرائیل فاش کرد که رهبر حماس، "باسل صالیه" را از دو سال پیش بازداشت کرده است. این خبر پس از دستگیری او در شهر حمد منتشر شد. این گزارش حاکی است که او پیش از این با سنوار و الضیف اختلافاتی داشته است. اسرائیل او را مسئول شلیک موشک کورنیت به یک اتوبوس در سال ۲۰۱۱ می‌داند.
@WarRoom</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/20739" target="_blank">📅 00:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve0sNsWnvBz4brAhbQWYR9bLwc4izhD2J-GV2vXDuODpz9LwIq5RxrxD9H_5_F2ch_t2HmP2nOv7SvM_Kiqp1k-nZD1Y5v-JGZE5r85-BUstmNOhjw0WIoqRIOs4jUlDd9B38tTIjwjRazm7UPqI9RFqMpRiMUYnARi2xLFwqi421QYrZuVRojb2dATbEcuDUUwfIamZoKvY1BElD9UabAV0VmfeQN93VUX9Rja-5fmG_jxjmlWKOWgT1YwVNA0B9O6DlIvFGw4e2DVjCpjRjDFmw7uot_psqFGy5BBy0kCe6ZUiYBPwArBJ3aKnUyzAglxbwd7arDoTllTm1tjI0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرکت پیشرفته‌ترین نسخه عملیاتی خانواده E3-Sentry (آواکس)  بوئینگ E-3G Block 40/45  از پایگاه رامشتاین آلمان به سمت منطقه خاورمیانه،
با مشخصات :
قوی‌ترین ارتقای انجام‌شده روی E-3.
رایانه‌ها و نرم‌افزارهای مأموریتی کاملاً نوسازی شده‌اند.
توان پردازش اهداف بسیار بیشتر از مدل‌های قدیمی.
لینک‌های داده و ارتباطات پیشرفته‌تر
و موارد بکلی سری بسیار زیاد انجام شده
@WarRoom</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/withyashar/20738" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گزارش صدای انفجار  پرتاب  موشک/پهپاد از سیریک
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/20737" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=lP6qX46WCrWYnCWl4N9ZK-ydAb0MNOeo4urRgwyUdwtuC-QwQfAee84fyAEOdJ1LmXskBkwz4CGOA35OLA0mJRGqfb7mzjiUfX8CRwCAqRLXO9Eop_3eEXtJ1y-nftETiHc8OnKZtvZI5ZxyXfe2BLWsAhUfZLY2xTlO6-7-OkDNahnjgX1-KHdhIqHliVvcGO4eekdd_WPQ-YK1zujYWHImPRKI92RcfXoK3grAtLeKuNclRVno9e2ZA1QjcmxGPgERiiEE99XGlvWayL7S1_UmbFVCeGNBw2L0ghXuw2539pjs5Shf4c7HTPsfAid6TR3KIilpKBymA2p6xApxy0hrTaSvUAc4dXB_cwVdsgdEipUtbybXpKxH5N_-3NvFgeqrha4YJcN3aYBltuzcAiCVAeKH0gBbjotti9wTkMNpeQ2wlbesHyDxivQvO_jeBXVuZGX_UrK6IuP7PwLGeGxUH5f8ewA0KbNy-jYriZfZVP0GPif7rZHE8fTVyewTqcVqHYOezUkD79XIVSVVCvmwbUzM0le-6j-zMHluDhVbXLK3l5QWvWN2kWVPIKIqE_zpiUum_UwF96_C5-SUU8PQYnjxJy4IV6bT9GnZQ9NWOhO4CgLVh-NObkR_9WQ50c92i-YQhE_9E_AskY8j0oFrYQWjbsewok-IRVihPm0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130cc3cf42.mp4?token=lP6qX46WCrWYnCWl4N9ZK-ydAb0MNOeo4urRgwyUdwtuC-QwQfAee84fyAEOdJ1LmXskBkwz4CGOA35OLA0mJRGqfb7mzjiUfX8CRwCAqRLXO9Eop_3eEXtJ1y-nftETiHc8OnKZtvZI5ZxyXfe2BLWsAhUfZLY2xTlO6-7-OkDNahnjgX1-KHdhIqHliVvcGO4eekdd_WPQ-YK1zujYWHImPRKI92RcfXoK3grAtLeKuNclRVno9e2ZA1QjcmxGPgERiiEE99XGlvWayL7S1_UmbFVCeGNBw2L0ghXuw2539pjs5Shf4c7HTPsfAid6TR3KIilpKBymA2p6xApxy0hrTaSvUAc4dXB_cwVdsgdEipUtbybXpKxH5N_-3NvFgeqrha4YJcN3aYBltuzcAiCVAeKH0gBbjotti9wTkMNpeQ2wlbesHyDxivQvO_jeBXVuZGX_UrK6IuP7PwLGeGxUH5f8ewA0KbNy-jYriZfZVP0GPif7rZHE8fTVyewTqcVqHYOezUkD79XIVSVVCvmwbUzM0le-6j-zMHluDhVbXLK3l5QWvWN2kWVPIKIqE_zpiUum_UwF96_C5-SUU8PQYnjxJy4IV6bT9GnZQ9NWOhO4CgLVh-NObkR_9WQ50c92i-YQhE_9E_AskY8j0oFrYQWjbsewok-IRVihPm0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) اعلام کرد که جنگنده‌های اف-۱۶ این فرماندهی، چند هواپیما را در نزدیکی باشگاه گلف ترامپ در بدمینسترِ ایالت نیوجرسی رهگیری کردند؛ زیرا این هواپیماها بنا بر گزارش‌ها، محدودیت موقت پرواز اعمال‌شده بر فراز آن منطقه را نقض کرده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/20736" target="_blank">📅 23:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۳ : اسرائیل به فرمانده سنتکام اطلاع داده است که در صورت توسعه برنامه‌های هسته‌ای و موشک‌های بالستیک ایران، به ایران حمله خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/withyashar/20735" target="_blank">📅 23:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به گزارش اکسیوس، توافقی برای کنترل عبور و مرور از تنگه هرمز بین ایران، عمان و ایالات متحده مورد مذاکره قرار گرفته، اما چندین روز است که در حالت تعلیق مانده است.
مقامات آمریکایی می‌گویند اختلافات فزاینده‌ای در درون رهبری ایران وجود دارد. گفته می‌شود یک ساید به رهبری رئیس جمهور مسعود پزشکیان، به طور فزاینده‌ای نگران فروپاشی اقتصادی احتمالی است و معتقد است که تهران به توافقی با واشنگتن نیاز دارد. ساید دیگر به رهبری فرمانده سپاه احمد وحیدی، با امتیاز دادن به ایالات متحده مخالف است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/20734" target="_blank">📅 21:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دونالد ترامپ، به آکسیوس گفت که ایالات متحده در قبال ایران «فعلاً با سر و صدای کمی پیش می‌رود»؛ اظهارنظری که نشان می‌دهد واشنگتن اجازه می‌دهد فشار اقتصادی افزایش پیدا کند.
ترامپ گفت: «ما فقط به‌صورت نیم‌بند با آنها مذاکره می‌کنیم. ما فقط داریم ایران را زیر نظر می‌گیریم؛ با این تورم شدید و این واقعیت که پولی ندارد.» او با اشاره به وضعیت اقتصادی ایران مدعی شد که این کشور «در شرایط بسیار بدی» قرار دارد و در پرداخت حقوق نیروهایش با مشکل روبه‌رو است؛ آن هم در شرایطی که محاصره دریایی آمریکا فشارها بر ایران را افزایش داده است.
ترامپ درباره رویارویی با تهران گفت: «همه‌چیز درست خواهد شد. همیشه درست می‌شود. این مثل یک بازی شطرنج است.»
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20733" target="_blank">📅 20:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اکسیوس: میانجی‌های قطری و پاکستانی اطمینان داشتند که این توافق روز
چهارشنبه
اعلام خواهد شد، اما از آن زمان، چشم‌انداز دستیابی به توافق کمرنگ‌تر به نظر می‌رسد
یک مقام آمریکایی مدعی شد که حدود ۸ میلیون بشکه نفت هر شب از خلیج فارس از مسیر کریدور جنوبی تنگه هرمز و با هماهنگی ارتش آمریکا خارج می‌شود. آمریکا قصد دارد تا زمانی که توافقی حاصل نشده، تلاش کند نفت بیشتری از منطقه خارج شود.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/20732" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCAh8fePLqBv5GR7hP31ev0FEDYiyatXCtdXoSqV0mwe2vHcPV8XrznIXyfpAQgVbyg7LfhBRizuhvrOnLAL5Pq-S6ANglmTr0nY3bj6U4ywZcOGZDxTYzuIcxd7XnXpgsvRhPfLOyrsCOxpUj0Uqhbw-Y9qToEkVbYdCBa_EssXJlNlgCtwkwUM_tyjruNPurZJw8YnnRkMnjvarI8jI4oCjMUeRTbSpLCLTrojN6BxwDhhTDSGGjiQZp_1T4ys8JYF9UOjKGR9bMCSRaQbojrBu6EsSJDuIV9Gg4sQsLcyphztxJ12cY83NKpITtcGQ-g3NNOBHhWkb11xFVe_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : جت‌های جنگنده رادارگریز F-35A نیروی هوایی ایالات متحده در آسمان خاورمیانه گشت‌زنی می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20731" target="_blank">📅 19:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20730">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حسن قشقاوی، سخنگوی کمسیون امنیت ملی مجلس، اعلام کرد کلیات طرح «اقدام راهبردی تامین امنیت و پیشرفت تنگه هرمز»، با اجماع همه اعضای کمیسیون حاضر در جلسه به تصویب رسیده است.
- کنترل بسیار بیشتری بر تردد کشتی‌ها در تنگه هرمز اعمال کند.
- برای برخی کشورها یا محموله‌ها محدودیت یا ممنوعیت ایجاد کند.
- برای عبور کشتی‌ها نظام مجوز و در برخی موارد تعرفه یا عوارض در نظر بگیرد.
- از تنگه هرمز به‌عنوان یک ابزار فشار سیاسی و امنیتی استفاده کند.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20730" target="_blank">📅 18:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس مجمع تشخیص مصلحت نظام:
به هیچ قیمتی از موضع خود درباره تنگه هرمز عقب نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20729" target="_blank">📅 18:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=mNdpUWBy7YK0JGgzX9NPdoyBwdUhmDlx_ZdlC07SpF-nNUY-MLnn6nsasc2XjllRIu9zSWgzt84sQp3qE10keuZqNts9hLFOcVbJsZufUeqKkA1Aq4x_gRrGtkIPWp_QDQPM85LEOJhgoK7obFko9h9HVyEOn0ywywpsbqUd4GMXVep5BNILzpXBqUOdZ_T_XGnpn5hkVG3vcL-N6VhdXVzS2sxoV61BqAy9I0uKGrWbGss9XUuQMorXMDdjua9ds89TKSRJVzWEFFadaWCbM4dhl6YnzHEjIcsgv5_jWyJYxWrW7noLRbf8KThSxOP1qjQtsy7iVbLLyB5_nH7Q-wq69zaklGeHpgwzSaHrhAbNNQtZ5Oo1OW7B4jl5Ez8SA8PDeVMYYQ8SC9rTGzXA2t0KXe9BPyQsALLp8W_Rm7ZgLQhtIx1eGCXPVO8DdjEo6nmVSn__Z5wYQWH1lQ27UBfjkwpvhhe-LUkobMG6IMxhzcCFprtRDFA0XvM92TnjKbJE8dXwXBj1EYCzZFLrGvd35zPkDtVJbbl87if6iqFX7KEk_HLREbgPUCX9CcNJZyTWGnlCs3gSViYDL8eOCFJEgYLH7fcxiljRSz1CdAGslhN30teap6SNb_FstKnGgbxuvFeffAO8eRctWNTSoLncO9CWGEjDPkzG0LrkZtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c89aa1291c.mp4?token=mNdpUWBy7YK0JGgzX9NPdoyBwdUhmDlx_ZdlC07SpF-nNUY-MLnn6nsasc2XjllRIu9zSWgzt84sQp3qE10keuZqNts9hLFOcVbJsZufUeqKkA1Aq4x_gRrGtkIPWp_QDQPM85LEOJhgoK7obFko9h9HVyEOn0ywywpsbqUd4GMXVep5BNILzpXBqUOdZ_T_XGnpn5hkVG3vcL-N6VhdXVzS2sxoV61BqAy9I0uKGrWbGss9XUuQMorXMDdjua9ds89TKSRJVzWEFFadaWCbM4dhl6YnzHEjIcsgv5_jWyJYxWrW7noLRbf8KThSxOP1qjQtsy7iVbLLyB5_nH7Q-wq69zaklGeHpgwzSaHrhAbNNQtZ5Oo1OW7B4jl5Ez8SA8PDeVMYYQ8SC9rTGzXA2t0KXe9BPyQsALLp8W_Rm7ZgLQhtIx1eGCXPVO8DdjEo6nmVSn__Z5wYQWH1lQ27UBfjkwpvhhe-LUkobMG6IMxhzcCFprtRDFA0XvM92TnjKbJE8dXwXBj1EYCzZFLrGvd35zPkDtVJbbl87if6iqFX7KEk_HLREbgPUCX9CcNJZyTWGnlCs3gSViYDL8eOCFJEgYLH7fcxiljRSz1CdAGslhN30teap6SNb_FstKnGgbxuvFeffAO8eRctWNTSoLncO9CWGEjDPkzG0LrkZtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش فاکس نیوز آپدیت آخرین تحولات تا دقایقی پیش…
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20728" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtcQ3wjXO_H2Z3xzICoYX9HELGAfmme1-AykWZunapdWlZfkqdosT8xga1j1Mi8H0Ccs0dXX6TLfcrgGiHQCwaU3Mh1bmm03Xz7RIuMX9mD1zZV-x1f5hMXWSLQhylePawmgcdaevT1wKf-mIRV-LLv2UCIz_Rxt08S1-aKXvZ_Id2RaMehUdA3Vey2CxYCmsWfIUNjbk1GESZpuO2EwvomLbKzggGjig1IG11Qt4dD2LEvV3MykELOtwjG4y9G-tJt7TXexVFsonsxFfe2zmmcEVtqFbLWL9EAjEUqJDk_TD-_OsPPH5-AAM7KVjh4aIZavTY-cBm0JaCFmFGY4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود و صدای انفجار در اصفهان
چیزی نیست بی بی داره خنثی میکنه
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20727" target="_blank">📅 17:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77914048f8.mp4?token=iCAdxwCcmZC7HKnqNcVLc04E3FMUDFNYLGobcFC5KwJEmWpLb-xiTr7RsrpOVL-mL8RTpXkQawbLHrWIef4CvG-zJgvCsYtVEpEBBv8Ks7Gn3kxrhvne0HV0VCqgllCYaMxIg5JCbYulduoJOi68AxUjE537b5Po6p94dPpNr5NTz8RnwCYGc39752XJQkHKznOX0aXjSBKoy-VL9lP5tLKdnrkgcrHx_Jkvv4MI0CAPBcZU4NW6MTv1SrHl4S38vIFIniRudeaxK5eKI8AbspVVuc8stXMe_EDlpk9ncyR8-Ol12dmEY0vd_2Jp8YETrELyFC9BZNpMYe3seRLr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77914048f8.mp4?token=iCAdxwCcmZC7HKnqNcVLc04E3FMUDFNYLGobcFC5KwJEmWpLb-xiTr7RsrpOVL-mL8RTpXkQawbLHrWIef4CvG-zJgvCsYtVEpEBBv8Ks7Gn3kxrhvne0HV0VCqgllCYaMxIg5JCbYulduoJOi68AxUjE537b5Po6p94dPpNr5NTz8RnwCYGc39752XJQkHKznOX0aXjSBKoy-VL9lP5tLKdnrkgcrHx_Jkvv4MI0CAPBcZU4NW6MTv1SrHl4S38vIFIniRudeaxK5eKI8AbspVVuc8stXMe_EDlpk9ncyR8-Ol12dmEY0vd_2Jp8YETrELyFC9BZNpMYe3seRLr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دفتر شاهزاده رضا پهلوی با جمع‌آوری ویدیوهای تیک تاک از آهنگی در وصف پهلوی یک دابسمش منتشر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20726" target="_blank">📅 17:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgAW4pshUl2zdzq36V9RaKiveJYs-ubUUhWn11QnvQP1ufQdcUPDzjeOSp49U1WOsU_5pxJN9XIOiRDswPgaw9l0lH0ELls-jiAb0jSjwqAD94nSvdvvlNKHSIekrtA-UCEmg2j6o2rI2Hjtupc2Wz07AxAYqlo76Izkoj7voWd3SwP2ulc3tjue1KQi12VT9aGOmJFyI-OPqz-S7SitFY4QY2GMFcQs_mmgF_v4gGz47NTqTvXEndlRYnNPFG9aM93T5OYXm88Go1WusxAZ5UT-mxLUZqTJ1jDnc9-fl-pHyZdR53fS6Bf7bsayvUko7yelj5gKSY5VjkTbfCWoQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین با خطاب قرار دادن عراقچی به دولت آمریکا : این بیشرف می‌گوید هیچ مذاکره‌ای در کار نیست
یاشار: منظورش اینه بفرما این عراقچی بیشرف هم میگه مذاکره ای در کار نیست کار رو تمام کنید
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/20725" target="_blank">📅 17:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یکی از معاونان نیروی شبه‌نظامی بسیج ایران ادعا کرد که تصاویری که مجتبی خامنه‌ای، رهبر ایران، را در میان مردم و در خیابان‌ها نشان می‌دهد، در آینده منتشر خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/20724" target="_blank">📅 16:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucn9kctbGEaUre59wE62H2SdkJxWScu9G3T0yX7bLTLQR1wlaJ8sy6LmFpOF9VRHtrGTX_dZAaPXqnHWR0PkC7QM9MzwI7QVrQQN3j-bdfQNcVRKO2zKV_JEnTE_JIkQDIBH0nL5puKdCZDCjIK8QJABB7hv5vTOo9PeayahEE1wMgzZICucDPRXH2mbmGSCp1X7X4Pd99ld6kkcBqdECNy4JMU_ydIhSKOMtt3OIoZCu5r5ixMqRuTIc_eQx0zKqJoLwy1wpnxJmMfLk2P4bAWJrQnBPGf4x4rhPMFLzY-4eyhsx9UHYJK2zfTdzUmGk1OouLno7omWFRlELp5fcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه هر روز پیجو میززن و برمیگردونم
پیج اصلی :
instagram.com/yashar
پیج دوم : ‏
instagram.com/yasharmotors</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/20723" target="_blank">📅 16:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=P0mV8Un4ppkK7I_NmtyWvcLPxCur9jMP0U_cLqlFW-22DUhFsGwCrSKXCNxsU96HzJx_oKfOt1TGoi_F7_zYk16E_0WkXRVSHMzU9Brh2Ca0tN1yCdm2tol1ilbp45Y10aVEEucrsSdRcvnxoRUhogJkjN4TRHN8Kl9_dY_1ebWx1DEvr3pBz6kJOAye8PY-JJzqPtoVTOw8QenhDl0EjbyXFXm7VZQYhe2rdVffZpQOPTcqhEnjuK-I8sDbctU3mm0eMebQoklGyJmbsXjq7khwdEBPJD5T821ZZ3KqfPMouOHK5AHqN5uhNPBESBcB49aE-rHMgXabEIhVgS7A2CK2Eht_f9Y-tMuOQeKl25H5gmeYyTP783eGb8IQehgZeCQ8GRhY3ptr_OK1nHH7kLEa3EDxi6HLzcQ2dOYWPoTn3aFDhtdzxy8o0kubvooHZzM30Kxl_2X-ibOSfNUq9Ie0DFhtv8Wl0-ndXHWbRu93WOYL188dwVC5h6042g94vdGrxdww3o1wJ1P7rR8hR3r01Qtc0nanUBRtU5LTb6GMegIu1dyeDiYPdMHewiK3BgP1KEXLApHmI0Gr4XhdmDhe0l1Uq1xg1Acut9F90H9ac1jSxLV5xbJKQzo-Y2s3eMn18tzNUTm_wVGbINRp8dBup0IwBwgugLQ0g-DGmf8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067ef90d71.mp4?token=P0mV8Un4ppkK7I_NmtyWvcLPxCur9jMP0U_cLqlFW-22DUhFsGwCrSKXCNxsU96HzJx_oKfOt1TGoi_F7_zYk16E_0WkXRVSHMzU9Brh2Ca0tN1yCdm2tol1ilbp45Y10aVEEucrsSdRcvnxoRUhogJkjN4TRHN8Kl9_dY_1ebWx1DEvr3pBz6kJOAye8PY-JJzqPtoVTOw8QenhDl0EjbyXFXm7VZQYhe2rdVffZpQOPTcqhEnjuK-I8sDbctU3mm0eMebQoklGyJmbsXjq7khwdEBPJD5T821ZZ3KqfPMouOHK5AHqN5uhNPBESBcB49aE-rHMgXabEIhVgS7A2CK2Eht_f9Y-tMuOQeKl25H5gmeYyTP783eGb8IQehgZeCQ8GRhY3ptr_OK1nHH7kLEa3EDxi6HLzcQ2dOYWPoTn3aFDhtdzxy8o0kubvooHZzM30Kxl_2X-ibOSfNUq9Ie0DFhtv8Wl0-ndXHWbRu93WOYL188dwVC5h6042g94vdGrxdww3o1wJ1P7rR8hR3r01Qtc0nanUBRtU5LTb6GMegIu1dyeDiYPdMHewiK3BgP1KEXLApHmI0Gr4XhdmDhe0l1Uq1xg1Acut9F90H9ac1jSxLV5xbJKQzo-Y2s3eMn18tzNUTm_wVGbINRp8dBup0IwBwgugLQ0g-DGmf8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : ناتو وارد میشود
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20722" target="_blank">📅 15:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20721">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">نتانیاهو : ما می‌دانیم چگونه در موضع خود باقی بمانیم، حتی در برابر بهترین دوستانمان، زمانی که این کار ضروری باشد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20721" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20720">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‏مسعود پزشکیان: «دشمن افرادی را ترور می‌کند که گره‌گشا و حلال مسئله هستند.»
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20720" target="_blank">📅 14:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20719">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست وزیر هستم، هیچ کشور فلسطینی، نه در غزه و نه در کرانه باختری، وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20719" target="_blank">📅 14:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20718">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو : در روزهای اخیر در لبنان عملیات هدفمند انجام دادیم، از جمله در منطقه تپه علی الطاهر، اما وارد جزئیات نخواهم شد.
ایران به اسرائیل حمله نمی‌کند، زیرا می‌داند اگر چنین کاری انجام دهد، ضربه سنگینی به آن وارد خواهیم کرد.
من طرح ۱۵ بندی «شورای صلح» درباره غزه را رد می‌کنم و از غزه عقب‌نشینی نخواهیم کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20718" target="_blank">📅 14:38 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20717">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یکی از رسانه های رژیم نزدیک به جبهه پایداری، با انتشار پیامی از هوادارانش خواست برای سلامتی مجتبی خامنه‌ای دعا کنند و «قربانی گوسفند» انجام دهند. در این پیام ادعا شده که «گروهی از علما» از در خطر بودن جان او خبر داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/20717" target="_blank">📅 14:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20716">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با کانال «12 نیوز» پیش‌بینی کرد تنگه هرمز طی 2 سال آینده اهمیت خود را از دست بدهد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20716" target="_blank">📅 14:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20715">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌ @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20715" target="_blank">📅 14:27 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20714">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ادعای تسنیم : محسن رضایی کج بند ،نماینده مجتبی خامنه ای در شورای امنیت ملی شده‌
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/20714" target="_blank">📅 14:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ادعای فارس : پزشکیان با مجتبی خامنه ای دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20713" target="_blank">📅 14:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار @WarRoom</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/20712" target="_blank">📅 13:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfmFaAPsusDK-5nkkWjhlQw95EkIDR7uYe2vhWUgJ5D_aJH1Uq-wCK89T6_1ohN8l0ciotv14E8teYQfC-JJFJO6nyFylMpz354Sf15Ebkvrzsb6bDDY94mMYBAXg67omG6iK3NH7iLJzkx00HOof3ujEUUjV09emuPcoCOBnbktiLKXBaqNhHy2N0LR3AWSBVG95ccEbA2zbgye-uEUovLIZPnkViAf3_VB_FC3U3ympQ9Wj0hRM4RgLBvcsSXbcTL-bdPUcDkKUQSeQw0v5aLVnzAn0VSrANsd5uxIft83fGRN3iJDm9NJkWQX2kORA0PrXk94CbnG6aUYLfEdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : دو آمریکای بسیار متفاوت.
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20711" target="_blank">📅 13:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from╚»میلادم«╝</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi6YrGZgkHtTIcwH19i0ATH1t98BTqXGxjr5w5xqPW-QMMhqY45KkQRVIHgJaj1jivlrEWqF-JGbviIt9n_edHRIKqykhUNbKHaJrmOacD8dqi0Me1H60rwioy60QEfDqqfCiaZqb_y5qLv-f2Y9ahPgGgFgPMtrmkiGdGEkVqfePa82mo_XTl7ttEuxLIyd4UAsrdbd4sS-ydS87caDrP9sbPJDfPaHle6CoFmHYCjMQ4Yw0j1DlxlFc84e2-KMYdVOymdTkiel6e-9HFvtjOi33RHuuethHyYhP4r9euHsAty3gDT5k-EJAw5gGkfEMY6xAqmPLT90Wq85QirABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20710" target="_blank">📅 12:52 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">عراقچی : در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/20709" target="_blank">📅 12:28 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد. @WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20708" target="_blank">📅 12:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏وای‌نت : دولت اسرائیل امروز اختصاص یک میلیارد شکل(حدود ۳۴۰ میلیون دلار) به وزارت دفاع برای خریدهای فوری تسلیحات را تصویب خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20707" target="_blank">📅 12:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سپاه : استراتژی ما حفظ تنگه هرمز است تا زمانی که دشمن تمام شرایط ما را بپذیرد.
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/20706" target="_blank">📅 12:08 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حملات توپخانه‌ای اسرائیل به جنوب لبنان
رسانه‌های لبنانی از گلوله‌باران منطقه واقع بین دو شهرک «میفدون» و «زوطر شرقیه» در جنوب این کشور توسط توپخانه‌های اسرائیلی خبر دادند.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20705" target="_blank">📅 10:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=GrZQRlPzvUcx3RtYWvLK9yMKWwQ25l2Ro5y4gM4Ef9NFOu21GuQCVkSy_iADSmmBaS184hkna326wLr1HgvKqP2ul1-VU0gkHGmE60pVx7Kgx36KhX0-HI1ZR4qjLL2MUAeZySvLNenXQmPYudoFcVUaoujoUKY_YvIDe6_OSNyuBqm5GVutq3pTEFhNrgkArYdJVuTiZ-94StSV0DSLPXVP60h4gY1LsRAJMRNYNFJjiM-VXw3UnBBfDauaeCKwZcfoU3P6SqyfQJZqjciM783nfNitLCxOfxMh1GOmHUDD0XIV-2QaQx31Za9MxyTORTmH_ythp0LNOC9khHQk5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5786aba1.mp4?token=GrZQRlPzvUcx3RtYWvLK9yMKWwQ25l2Ro5y4gM4Ef9NFOu21GuQCVkSy_iADSmmBaS184hkna326wLr1HgvKqP2ul1-VU0gkHGmE60pVx7Kgx36KhX0-HI1ZR4qjLL2MUAeZySvLNenXQmPYudoFcVUaoujoUKY_YvIDe6_OSNyuBqm5GVutq3pTEFhNrgkArYdJVuTiZ-94StSV0DSLPXVP60h4gY1LsRAJMRNYNFJjiM-VXw3UnBBfDauaeCKwZcfoU3P6SqyfQJZqjciM783nfNitLCxOfxMh1GOmHUDD0XIV-2QaQx31Za9MxyTORTmH_ythp0LNOC9khHQk5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پی آتش‌سوزی یک واحد صنعتی در شهرک نصیرآباد، ۶ نفر مصدوم شدند که یک نفر جان باخت و ۴ نفر به بیمارستان منتقل شدند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20704" target="_blank">📅 10:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‏حوثی‌ها اعلام کردند پالایشگاه آرامکو عربستان سعودی در جازان را هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20703" target="_blank">📅 10:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahn9AtA5Az6I_D3uDaqEGHiDGMklYyN52sPU3YkjdmIcoXitzXoSPMQNuxfDjvBHQVy_RD25FEHLWSha1pU3TviBO4TOXtogCD8hBsJnNz2GttW4md2kC85_tnT8RF_RhhlRq7om-dhOCN3nHw_PDZ-5g1Zmg3J2btzvcReHTeYXb-JQfeTaDOXCdzxYWrrTkC8Oj8bA_pgG80yAny5LVlSgjcN8vM_shyT7xUMuN3ho_9LwhXg5ZMBO4g34JKJ3S9sj0TlxDnlJcE_hIguSOylbH89agl8yHY6e_Bo0-M6uzoS5Sk_4pjF-zkqojm1_7bIQYPG3uBcEKfdll4-PfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورشلیم پست : ایرانیان آزاده و اسرائیلی‌ها باید در کنار هم بایستند و اطمینان حاصل کنند که سنگ بنای صلح فردا هرگز قربانی تیترهای جنجالی نشود.
@WarRoom</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20702" target="_blank">📅 10:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">کانال ۱۳: ارتش اسرائیل به فرمانده سنتکام اطلاع داده است که اسرائیل برای جنگ علیه ایران نیازی به تأیید یا حمایت ایالات متحده ندارد و اعلام کرد ما در حال حاضر در حال آماده‌سازی برای شروع جنگ هستیم.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20701" target="_blank">📅 02:10 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اتاق جنگ با یاشار :
برخی کانال‌های تلگرامی عبری مدعی شده‌اند که یک ناو هواپیمابر جدید آمریکا در راه خاورمیانه است.
بر اساس ارزیابی‌هایم، محتمل‌ترین گزینه
USS Theodore Roosevelt (CVN-71)
است؛ ناوی که به‌تازگی مأموریت
RIMPAC 2026
(بزرگ‌ترین رزمایش دریایی چندملیتی جهان به میزبانی آمریکا در اقیانوس آرام) را به پایان رسانده و به
سن‌دیگو
بازگشته تا وارد چرخه آماده‌سازی برای استقرار بعدی شود. برخی گزارش‌ها حاکی از آن است که این ناو احتمالاً در
ماه سپتامبر
جایگزین
USS Abraham Lincoln (CVN-72)
در منطقه خاورمیانه خواهد شد، اما
تاکنون هیچ دستور رسمی و علنی از سوی وزارت دفاع آمریکا یا نیروی دریایی این کشور برای اعزام Theodore Roosevelt به خاورمیانه منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20700" target="_blank">📅 01:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">😁</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20699" target="_blank">📅 00:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvOsdLLJyM--QQJRokhLKI9aoRJ0CPIUA8gzTuLXlF4JJrHyfMRWiaYs8H79qeENfrYlkB_MAapdOczpYyifQEX1vPpg-rrZH02LxfvIaNUv-Le5uysPLWlu_0PLl7hCQMgXD-tZ3D0DbjPw5-58RE5aELq7dK-qjjhnLbmhanUOzzg-MLQ7lytOgJpKK95I8Ox9fL6CiUVNH7-qRFfDX7K8S5ahoauM0KbXBRhMGF61U4N3Xr78BKcoO_gxZwOgFtLYqDY2_GbzYFJxKEWmxgr7K2VIFeBD56--tDSIUlLnB9H0XgYcdpv_2asRSez5k0x_ygjHaCQKPBbM7CS6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین باز دید پیج اینستاگرام از شهر های داخل ایران
😁
تبریز
🥇
🏆
اصفهان
🥈
تهران
🥉
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20698" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeKGUoayuChJHTthwyOc0Gx-I7ExIRElTKPutctjjdm3-cJE7D0im4ib5--nPakstJqJjCHJr6zR0WceYHKML-DH4QgtBMd4bEWWSjCXUlO2_u38hm2vZjiSCBCK7sxV6r-6s1gcn4mc3UuezFntXud4ziez5AvrApmABYWf1scbLRehTfONtT1dgyPG1VP7Rh-x62qTLm1KCljE9tAzkkmU-1NmjvZCQmp1VgbbGu0d6eK9pQa-77b0AmicorKcnctpkEBgMga3Hdq2j46K8aP9vXrgtu87-MYTCzNLpn_lvGCIl5Lz7AjxsFaThrCXTSjBaeOQ0CqHjjPOExpgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: تأسیسات هسته ای کوه «کلنگ
گزلا» در تیررس ترامپ قرار داره
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20697" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtjnMuG9dtjxxCdkR4MA1ogsfvpaxQ6lEJjKcZR5VcVisKRUAtsi7n5JSw1-FxpLFrFR7ERghRHqYwOv6lYzGhY6vWf5tog9zHjv5sudOCDugj5nPeypdBokkw5cGj_96is_XfJGBra-NFoPssGBj5FwolA51CjrrzR5HgwNZnYGzhypkEeXpb4INhtGspBJwJ_I2LCvX9iSrWg7XhaRMLIxjr_FD9HfjcO0ApzOhsRSmezaDEHksUDGA8p4EzqtLXWBzaP3EDAtpKnEjo_RpRTU2y7jeyL2krkkWRVHgobYHcx2fEBEEUYSqMfuNBa0BgaMzs6E_BDBHIkkT2TBwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند. تا 8 آگوست، سنتکام 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20696" target="_blank">📅 23:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFAzDePvIXtCJFQ49kYaFlDT6dNemNr0cR0Rg6v1kVxJ9K27bRH1JnsHOMuZO3xGjh7icEhel9w85XIH_WotasoiDKeE9irDsJLnGQmEDwdc353FeWs0m8Gq5MtHTXzeNimv13jkHznVMWkYUcNd6vvFoZydR2AAraEq9xaWKDfUDV7GP7EMC9V18x68OQ2xjv6WVEYg9Hzfs3_puVelOpBHrA1Ww4ckKtXarqmArfiA1ZHr7MCcgyE7bhDo-kk8hkjuGnY4B9eI7k9bdZmvLEpOhpYvU4YuX1yqtGfEgBym4gESZkt67dWig588hswtqdw38WDtVE5umOccVKgIXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد  برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد. @WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20695" target="_blank">📅 22:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تمام مرخصی های نیروهای نظامی اسرائیل تا اطلاع ثانوی لغو شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20694" target="_blank">📅 22:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">وای نت عبری : آمریکا سلاح‌هایی را از آسیا و اروپا به خاورمیانه منتقل کرد، زیرا موجودی سلاح‌ها به سطح "نگران‌کننده‌ای" رسیده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20693" target="_blank">📅 22:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20692">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نیویورک تایمز به نقل از مقامات رسمی نوشت: ترامپ تصمیم گرفت با وجود هشدارهای ستاد مشترک ارتش در مورد مهمات، جنگ را آغاز کند و انتظار پایان سریع آن را داشته باشد
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20692" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20691">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرمانده سنتکام وارد تل‌آویو شد
برد کوپر با رئیس ستاد مشترک ارتش اسرائیل و دیگر مقامات ارشد ارتش دیدار خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20691" target="_blank">📅 20:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20690">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال ۱۳ اسرائیل : اسرائیل در حال آماده‌سازی برای احتمال اقدام یک‌جانبه علیه ایران است
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20690" target="_blank">📅 20:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fi4G4TtebPdrtZSiKjHfHDHp34YpALr1m8UYXGxOj-Huriv5eydqH7BTRbI-3SfIfA0EkbbjxvrifcH1V_UDTj-9OJAL7FAzFS27WecqZvYcKlpPlWhMQrBNqlUtDgajvzL0kLeZ4Yb9t5jn5cHwdCb81Nd9iGvMEG9RkMFOJln9XbUm17NlbsNLp10wEl2XOGeyXuGAl9XTZtgeThggYBXfeaxBnMRm62vP9Tt2OdoDlgF5PoZRBO73_BmF9abpYsZolyHnSdUxsmJnWY44WbAGMSD83dUJ5jBYBCWMSuSkPf42mE9qFcbI1doZm7JXD8D4TYRbKXct4RnCMPDU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است: B-1B "FROWN30" 86-0124 B-1B "FROWN31" (در انتظار تایید) @WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20689" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20688">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وال استریت ژورنال : ایران به دنبال منع عبور ناوهای جنگی آمریکا از تنگه هرمز حتی با توافق است
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20688" target="_blank">📅 20:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20687">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9dsZANVUVE4hplJFQf3dtzUDVOW1mAejd1HCfUqpJgaddQ4EZS2Vh7Cn0wwsWJOwTDWobP4DG3Pv44Y4sCI6iooobWBZQ4QtYMiwv3EygsxoTW06RKIwBF3hP_DzeU_Z4dz_zbRGE1IpeXuu8Iysl0JK34C_kKjDCtqcQdivnCpbTPPv4GQdQt--jbV7Amg1mjNqEOInoK7jvaHvsOtS1VUKYX6pKTyyw-qkkri5ZO9hwNgommEYOGA74IL-jMzW1drNKilKaUOqV5s9q3Xc852nCvfGLDECyByQkwcbGeIO4zC49ahjv-Le4oNDacE53OuqzAaMkuuBFHqhEW5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هفت سوخترسان از اسرائیل بلندشدند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20687" target="_blank">📅 20:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20686">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=aoj8kR4Fzhk6v2WBqvlHHhactWl-qeHSzA9AituVi9SMdpx55482Yeskx7Z2ILMZtfFihec2yt7Vnkii3Ct4uDBARV5rnXs6Vp_QhEuLeQnfD79kNmHtciBQzl8YXZYb6MLqva09MnIXzRAffWfYMsGANuVv2oGE7cN0vEkjvo1wcJBuectC6qmrH0iEsBm7BQd25udRlPfbUgoiOp1CAX-7VOLH1s2gI2M0Bs0HyybAYRdZTzRM16e63t_AhOjvaWcHZhNAQ5OKGVSUW3_ERAhssU1qd7qtOZ6kVeQPQnA00cin4BDDMeCrORERhIrhfRnE1JmSGK2wmkzb67TNmGAOkqbAZ5tICGAGa59yzPqRv1lH1n1my-vzROZwPYtVDLwvsrOfplhhzCDQicxV6h4f12D2Zg6J5qOFFU2ftAj_TalhGf2f20xpYatAdZPKIdUFKAaGTgeyhuHrudbsCGNpjlr3_Hv7-YswUaJbB8lThYXX69gnOTjVFYDulrpuchrWXtsOJv0z4sqf3nlgUAGW9Ric-YxXZX-dftb8LtQc8yGidgLjl9jsb06iA8FxihKI1sDRU8unKdcZGyfyrRFrBOJbW0vVjBOI7OmLfyeQI8mB54DI6R8Z3HP8fe5uxj_DCGFui52EF340N8F-NyejzU8nGwbHnARzZUORamM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dc8a5363.mp4?token=aoj8kR4Fzhk6v2WBqvlHHhactWl-qeHSzA9AituVi9SMdpx55482Yeskx7Z2ILMZtfFihec2yt7Vnkii3Ct4uDBARV5rnXs6Vp_QhEuLeQnfD79kNmHtciBQzl8YXZYb6MLqva09MnIXzRAffWfYMsGANuVv2oGE7cN0vEkjvo1wcJBuectC6qmrH0iEsBm7BQd25udRlPfbUgoiOp1CAX-7VOLH1s2gI2M0Bs0HyybAYRdZTzRM16e63t_AhOjvaWcHZhNAQ5OKGVSUW3_ERAhssU1qd7qtOZ6kVeQPQnA00cin4BDDMeCrORERhIrhfRnE1JmSGK2wmkzb67TNmGAOkqbAZ5tICGAGa59yzPqRv1lH1n1my-vzROZwPYtVDLwvsrOfplhhzCDQicxV6h4f12D2Zg6J5qOFFU2ftAj_TalhGf2f20xpYatAdZPKIdUFKAaGTgeyhuHrudbsCGNpjlr3_Hv7-YswUaJbB8lThYXX69gnOTjVFYDulrpuchrWXtsOJv0z4sqf3nlgUAGW9Ric-YxXZX-dftb8LtQc8yGidgLjl9jsb06iA8FxihKI1sDRU8unKdcZGyfyrRFrBOJbW0vVjBOI7OmLfyeQI8mB54DI6R8Z3HP8fe5uxj_DCGFui52EF340N8F-NyejzU8nGwbHnARzZUORamM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بورب مودین ، مأمور کا گ ب : همه دیپلماتها جاسوسند
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20686" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20685">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن. علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده. دقایقی پیش خبرگزاری‌های‌رژیم…</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/20685" target="_blank">📅 19:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20684">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیویورک تایمز : ایران فهرستی از درخواست‌ها را ارائه کرد که امیدها را برای بازگشایی تنگه هرمز کمرنگ می‌کند.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20684" target="_blank">📅 18:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20683">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‎معاون ترامپ، جی دی ونس : ما توان نظامی ایران رو به‌طور چشمگیری ضعیف‌تر کردیم
بعضی‌ها داخل نظام ایران درباره موضوع "عوارض" صحبت می‌کنند
اما ایران به ما گفته که هیچ برنامه‌ای برای گذاشتن عوارض تو تنگه نداره و قصد چنین کاری رو نداره
انتظار ما اینه که صادرات نفت و گاز از خلیج فارس دوباره به همون میزان قبل از شروع درگیری‌ها برگرده
ایران در ابتدایجنگ، تعداد زیادی مین تو نقاط مختلف کار گذاشت
الان تلاش ما اینه که یک مسیر و برنامه تردد مشخص طراحی کنیم
تا کشتی‌هایی که از این مسیر عبور می‌کنن، بتونن با امنیت کامل رفت‌وآمد کنند
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20683" target="_blank">📅 18:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20682">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">دبیر شورای امنیت ملی ایران می‌گوید که ایالات متحده باید دارایی‌های مسدود شده ایران را بدون قید و شرط آزاد کند، تحریم‌ها را لغو کند و غرامت دو جنگ اخیری را که علیه ما به راه انداخته است، بپردازد.
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/20682" target="_blank">📅 17:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20681">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1_Le1XWm1qEekknSRnQ1ZNuWmryM2jB-40IvWGBg3xCPAGoV7v_W8FxMOHuFxoZ2tI3Y_s7Jg4sNzZjHUPKSboxhLv0B7o9k1u_ENWYHQo089bnKSzUYVVomRUWN26brqQgRfeWKOdtQx5NQQUnqs0whzTz-HgLz0uc2VxoXz1wSycUELqKm5wy8K4O7MNrhbCMjy5vto5uj6zbLSGQq2Zm-uBgrR4uIxXUdViGqokr18gte-AuZJBHwug5FkZMJ0U4htT8uMnWBthc-TEzy4pscxiqmY6uWqOIfNd07evaSwqQsG0U0PcEsPkAg7xfcC97cgD0liT17pQ-GN_YAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار است امروز دو بمب‌افکن B-1B "Lancer" از پایگاه هوایی RAF Fairford (EGVA) پروازهای آموزشی انجام دهند و گرم کنن حسابی برا حمله اصلی . یکی از آنها در حال حاضر قابل مشاهده است:
B-1B "FROWN30" 86-0124
B-1B "FROWN31" (در انتظار تایید)
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20681" target="_blank">📅 17:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20680">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUJcd7Ux07ec06LPLJ3HIocrrYMqY8ylBQtDu8q-DA2zbgD9A_tVJBk3reKm3Oqjykknf-APHwJIqnFYQUU04r-V4__WLOD7vDMU3ABd1_mAaxOD-dtDippEbMjIDwRDI5vpnH5MvXB7eXeLyGFe6Xfhe9i3ZF_fZdgQ9tRoHVjE4oardJkKQolGWNrDqLza_HonD9fJGhmI0Lv-eZpAeVtoZz_b_7_X_y4qmTufD59-sLzYnlwmIERHwaMLq0DEN4_6hddwYHAahZDtL0I5kyKPZGjXNyq6nEs0fzX9ZqodfBTX7aG0CWimb-U7ifkeqaGe2urzrctKCt9Rvkc3Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمل و نقل دریایی بریتانیا (UKMTO) گزارشی از حادثه‌ای در ۱۸ مایل دریایی شرق خصب، عمان دریافت کرده است.یک منبع موثق گزارش داده است که یک کشتی مورد اصابت یک پرتابه ناشناخته قرار گرفته که باعث آتش‌سوزی شده و آتش خاموش شده است. هیچ گونه آسیب زیست‌محیطی گزارش نشده است. کشتی و خدمه در سلامت گزارش شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20680" target="_blank">📅 16:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20679">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=g7Xig0X64HwA93feRQXurBa3bPeM98HNzBpy7FGxEU8181aMVZvWdJdXz4sz-nC8xKikf8HlfpvNf_q6cgvXD0qQYPuoDs_xFPdIGEBuAt5x8TlhaFIyZ6pUubKhi5Xh7Lgt5BDJH5h1Cy5CITNIGKG0wWW3CdAJoZOoGngYZygo8CzDlcedf3xNnRYbpl8Quc7uJcXNipUFYhnwSRa9bNAgNeKFKq61lst651SxMSyFtKKjEFDoJLq4NzSc1ULnbRVd5E7PlG64Gp__WjDUay6Y9YAM87lib1B-Mf61JUFE-RN9kwnaOXd0gcNCYt_AGWE_9v4zoWFeVkdTHvWetA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb62efb6b.mp4?token=g7Xig0X64HwA93feRQXurBa3bPeM98HNzBpy7FGxEU8181aMVZvWdJdXz4sz-nC8xKikf8HlfpvNf_q6cgvXD0qQYPuoDs_xFPdIGEBuAt5x8TlhaFIyZ6pUubKhi5Xh7Lgt5BDJH5h1Cy5CITNIGKG0wWW3CdAJoZOoGngYZygo8CzDlcedf3xNnRYbpl8Quc7uJcXNipUFYhnwSRa9bNAgNeKFKq61lst651SxMSyFtKKjEFDoJLq4NzSc1ULnbRVd5E7PlG64Gp__WjDUay6Y9YAM87lib1B-Mf61JUFE-RN9kwnaOXd0gcNCYt_AGWE_9v4zoWFeVkdTHvWetA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله‌های توپخانه‌ای سنگین ارتش اسرائیل به شهرک المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20679" target="_blank">📅 16:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20678">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‎فایننشال تایمز: محاصره دریایی آمریکا بر ایران، صادرات نفت از ایران را متوقف کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20678" target="_blank">📅 15:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20677">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=Jdo0dpMUpnsWXyrdVOqS8XnP5DF-zHW3uRwJAmJy7o-N9Hfehrx0cCVZVCl2MmNwtUUxRxmYRiwYgHJZmhJlL6FQPOLN_t1KL2T_ECC-_NDCyvi_vtE9U7Sc_fc0j6bp3A3256tjdUXH2ArBvhDkZbgxrLoStF-_f3SlbFpADfIhJPYkn6ctg3GZZAX9xfR0XwZPe1KgWotuX4Z29CFtPQBPWVd5sbRhori_lK7gmqUVJbcPnsYQuxICecLoGHMLi6FFQhqwMS3-U_diwG_1gIfPVzWHm_6O9eTxyDU8VtwVG7fKqWl0olE-4U-eOkb7xhM7dJ4pTMlnGRa6j5Eejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f01922dde.mp4?token=Jdo0dpMUpnsWXyrdVOqS8XnP5DF-zHW3uRwJAmJy7o-N9Hfehrx0cCVZVCl2MmNwtUUxRxmYRiwYgHJZmhJlL6FQPOLN_t1KL2T_ECC-_NDCyvi_vtE9U7Sc_fc0j6bp3A3256tjdUXH2ArBvhDkZbgxrLoStF-_f3SlbFpADfIhJPYkn6ctg3GZZAX9xfR0XwZPe1KgWotuX4Z29CFtPQBPWVd5sbRhori_lK7gmqUVJbcPnsYQuxICecLoGHMLi6FFQhqwMS3-U_diwG_1gIfPVzWHm_6O9eTxyDU8VtwVG7fKqWl0olE-4U-eOkb7xhM7dJ4pTMlnGRa6j5Eejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسنیم با انتشار این کلیپ که قدیمی‌هست نوشت: پخش تصاویری از رهبر برای اولین بار
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20677" target="_blank">📅 15:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20676">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…  https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u  بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20676" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20675">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آغاز ساخت پناهگاه در پایتخت
معاون شهردار تهران:چندین مرکز را در سطح شهر تهران برای ساخت پناهگاه پیش برده‌ایم و کار اجرایی آنها آغاز شده است.امیدواریم در نیمه دوم امسال بتوانیم چند پناهگاه را به بهره‌برداری برسانیم.اقدامات احداث «پناهگاه و پارکینگ ـ پناهگاه» به تصویب رسیده و اقدامات اجرایی آن آغاز شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20675" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20674">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وکیل ترامپ در پرونده حق‌السکوت، وزیر دادگستری آمریکا شد
سنای آمریکا پس از چهار ماه و چهار روز از برکناری وزیر دادگستری، با ۵۰ رأی موافق و ۴۹ رأی مخالف تاد بلانش را به عنوان وزیر دادگستری و دادستان کل تأیید کرد.
بلانش پیش‌تر وکیل ترامپ و از اعضای تیم حقوقی او در پرونده پرداخت حق‌السکوت به «استورمی دنیلز» بود.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20674" target="_blank">📅 13:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20673">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۲ اسرائیل: پزشکیان برای وادار کردن خامنه‌ای به ملاقات فوری با او تهدید به استعفا کرد.
"وضعیت اقتصادی ایران غیرقابل تحمل است"
پزشکیان می‌خواهد برای خامنه‌ای روشن کند که پریشانی اقتصادی کشور به نقطه بحرانی رسیده است، تا جایی که دستیابی به یک توافق سیاسی و رفع فشار اقتصادی به یک نیاز فوری تبدیل شده است که نمی‌توان آن را به تعویق انداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20673" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20672">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmJFfTm9Z3hXAnGbUE7g0LfmjEAf_yy4DrlT95EZDDUvwhbI_XsJNNQ1djAw9EdAMacEjGHzWmrOWVKyEV_Bz5Jgqe7RvNoEhapdOuA0IxXWzB2cdvcyhS4hDP3hlVEnwI71wMcRiCATR26KgAeMuu0CO-jBUX1mbJghs193gTxH0xJoYx3f-Li-wi0_wn0lU-LtTXVYAdyzG9i5ahPCS7HndT2Lhdgy5g7rXiTD9DjUtKXOqalHNv4rd3p0VVtIV8AbnoiiD7wM4iWxaTbrf_fWGirKaM2qJdA_C0DJEQZuUEEKuhNkhSE3pf3iKw8zSHCa1I8T9De2psc1euNYWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کانال تلگرامی با دوتا فیلم از اون لحظه مدعی شده که نیروهاش "حمیدرضا رجب‌زاده"، بسیجی و مداحی که دو هفته‌ای هست گم شده بود رو به هلاکت رسوندن.
علت کشتنش رو هم گفتن که این مداح جزو نیروهای سرکوبگر بوده و در ۱۸-۱۹ دی، تک تیراندازی می‌کرده.
دقایقی پیش خبرگزاری‌های‌رژیم خبر کشته شدن این فرد رو تایید کردند
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20672" target="_blank">📅 12:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20671">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20671" target="_blank">📅 11:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20670">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yYC9tXIrIDV88TmVhyaNjujEDqBEoH-lL0WG1_DNByrTGB98PYjlA7laib3A5uU_xYcjiyVW97GVJHR6zkstueJa_-Fgf0UmuA_gzdcBMPV8KYFbnrY-2YrXuM7Yny6xydNpofEBwK_w4YNfzxUFw9mhqwpEZ1bdqj54enUFS7k3Ee_UeFH4EEdES5lHmGPGbfaMdrPrCf9QVkFeTayM5eJXongXzWl4kJW-ThYIJADbR-rBm0I2nbeTWJy4ffS1vQqApW6Y7uqksPDsU74b6bJM5svlA2z9wx3tF7TNrLKNQlCeXBFvudl7oyL7hDhW5ncjr5zk42Z_HQvwpODcj3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90587b68aa.mp4?token=QENoeQyJf51UjD1pH2uAw6Svn5n7-pO_gy9UnIkgl2DQWRudWPVzPKdPUq6hlPet2Ee9yJGA4x8Axy9l1T50p16XU6aZxs-0NA5J-6yxUOmc0bZC1DjsMIA-eq63yso43IE13k2sW9hzm3EZ9UMHfKUcusX87cZrF3oSYOVQShJo-Glw5pHOWcsuowYSGHvFrNKLSv3Tk5eCqiKzwzDnyg68Ineds7l0qIZWHmGd3GyFnMBXM24IdEau-8irTnPkfAWJZqcqDLRQkd_36TzNJyYbU0XDCTI3WNx9LMTRK__eMJQjcaGNEcUnZMfbbsS6cwI98kUc2nS5HoUxnk38yYC9tXIrIDV88TmVhyaNjujEDqBEoH-lL0WG1_DNByrTGB98PYjlA7laib3A5uU_xYcjiyVW97GVJHR6zkstueJa_-Fgf0UmuA_gzdcBMPV8KYFbnrY-2YrXuM7Yny6xydNpofEBwK_w4YNfzxUFw9mhqwpEZ1bdqj54enUFS7k3Ee_UeFH4EEdES5lHmGPGbfaMdrPrCf9QVkFeTayM5eJXongXzWl4kJW-ThYIJADbR-rBm0I2nbeTWJy4ffS1vQqApW6Y7uqksPDsU74b6bJM5svlA2z9wx3tF7TNrLKNQlCeXBFvudl7oyL7hDhW5ncjr5zk42Z_HQvwpODcj3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش ویژه آژیر خطر از فاکس نیوز: سربازان آمریکایی در جنگلهای بنگلادش تمرین آمادگی می کنند, حکومت ایران یا توافق را میپذیرد یا بمباران میشود. آیت الله گی قدرت پدرش را ندارد و اختلافات بالا گرفته… و عناوین دیگر که در این ویدیو خواهید دید
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20670" target="_blank">📅 10:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20669">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3moa5LzIhvDj3sUIpHFFx1mcY2XtA9wQifAjsHxmnuQd05gZ9tos53ov2myVBtcHdI_CKKVaqYYBMdTAOxzUmuNwAHOaopDJ_-01oHUeAX2XrYnEHolJ9znpDosATrBmEw1FNHBtztJSenCd16jfbbXevevpLZA_5FdBdCxNfNvzC43ZykkFiUpO5cyOsdRs4qjZU7wH-vr9HupzfBAzlHEIEd5aQcYGlAXfOJtbDWqZUwGzOr-nF-ND7E_JpmUVV2aKtVxkdBRgcm7BK55tEU9QrZ4wWP2UbIgWhqqTFgH6ZnAtUm0cKRR8m49q3pm_Dxb-3InEES3FuRFI_AMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسن روحانی توی خونه خودش یک هیئت دولت خونگی ساخته با هم جلسه تشکیل میدن و خاله بازی میکنند!
@WarRoom</div>
<div class="tg-footer">👁️ 185K · <a href="https://t.me/withyashar/20669" target="_blank">📅 09:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20668">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">سفر مکه
@WarRoom</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20668" target="_blank">📅 02:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20667">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_XUG_yDuJJ_FKu6qW2sEx0vLzrzF1KTvW7tXYLEBU70rAAQAL4JMQRLq-TwAQNSqjf2CgFcCbwda5MGKAhoaqifKRWQISScy5kyWhNCVv9_rI_0UVZMqzVa3nvbuYWVw_hZ3fMaoCdIB5_LT-dQo18qEJ_xQ3UeFBe0jrBheHTmGGQudaCHpLtcPIbDx58SaDpeWz30kOZVBJ3omDAx8TUaYHihAkfsobk2oQR2hlkgm6XT01_BfjCFedXTcj9_rW90eACrbRPWZpONiuZA0AWCmjyTuoWsay6yF1NNRKBfYZNaSjMvq29rJnCIDrz1vns9qJOtYwme05y3GUl0lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارک لوین به ترامپ : کلکشون رو بکن
@WarRoom</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/20667" target="_blank">📅 01:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20666">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20666" target="_blank">📅 00:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20665">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی خیلی آدم حسابی هستی عمرت طولانی تنت سالم بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 180K · <a href="https://t.me/withyashar/20665" target="_blank">📅 00:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20664">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">هربار نا امید میشم یهو میای و با انرژی ماوراییت میکشی بالا منو. نشسته بودم در اوج نا امیدی عرق میخوردم، کانالتو باز کردم و ویدیوی آخرتو دیدم‌ و چسبیدم به سقف. خیلی خفنی
خیلی آدم حسابی هستی
عمرت طولانی
تنت سالم
بمون برامون یاشار
❤️
🧿</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20664" target="_blank">📅 00:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20663">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d253696.mp4?token=BXqwW0-Wai7_WSREfs6UuL8yXpIwAh9VXUEQaOvM8Yc4oWSpaIKlVo3JJMIVyAH_95sC8DqCanSlDRKKNAUCnG8k0pN2OOH4ulFubuVcVXofnwtT2u9b46nite4i1k1QbWlMR79qUPte_vCDKCQxdObV8fxEP2UQ8QlW2pqDXf_BdTDM18TstfHW4MpzAQ-W_SyKMzLw2kIyDn7RSlT1u-aGuajqxCIoc0U5R0EPx25YR1bcVHOqXUBd6YvPeTZ1lO4_HZCymjfhz6n4XLMOnxjsHUH4n2gQxOtO0jk_fqCD0F7R1LxKXsD0IH5VbW2wquiKNLZ1ihoSuwlYaPv1tyPk07AucXuNtn2eHkTg7fsMEZCZy4N0r-FKumVbT8DAwFw4kLwEYJkmjNkRZCQ9lqUxwFpPODTRuZJ-7s_rNPE2pZA7r-RmEXz-uOYvQKPuRGa93k5KOXs1F7YqPQzTk8vJdNruV4FhEP3TCtw3tHaHVo0GvMYCFxz_hnZ0FspHTpw12TGMTa3hkzVaBmHZYrBCK7hmxOxgNYUuSFpMP8SP4VVUMTNzxl8ecwr7o5b1mlEukib5zkDIMICE_dpLMlBeOSIlHjJc9TEdzo1tNT5Sm-9q_j-U5xD1jwyjcwjJnTyJbOnDDTP8xzNoehaFN3XrjoNgtK7nkdnhpjWZxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d253696.mp4?token=BXqwW0-Wai7_WSREfs6UuL8yXpIwAh9VXUEQaOvM8Yc4oWSpaIKlVo3JJMIVyAH_95sC8DqCanSlDRKKNAUCnG8k0pN2OOH4ulFubuVcVXofnwtT2u9b46nite4i1k1QbWlMR79qUPte_vCDKCQxdObV8fxEP2UQ8QlW2pqDXf_BdTDM18TstfHW4MpzAQ-W_SyKMzLw2kIyDn7RSlT1u-aGuajqxCIoc0U5R0EPx25YR1bcVHOqXUBd6YvPeTZ1lO4_HZCymjfhz6n4XLMOnxjsHUH4n2gQxOtO0jk_fqCD0F7R1LxKXsD0IH5VbW2wquiKNLZ1ihoSuwlYaPv1tyPk07AucXuNtn2eHkTg7fsMEZCZy4N0r-FKumVbT8DAwFw4kLwEYJkmjNkRZCQ9lqUxwFpPODTRuZJ-7s_rNPE2pZA7r-RmEXz-uOYvQKPuRGa93k5KOXs1F7YqPQzTk8vJdNruV4FhEP3TCtw3tHaHVo0GvMYCFxz_hnZ0FspHTpw12TGMTa3hkzVaBmHZYrBCK7hmxOxgNYUuSFpMP8SP4VVUMTNzxl8ecwr7o5b1mlEukib5zkDIMICE_dpLMlBeOSIlHjJc9TEdzo1tNT5Sm-9q_j-U5xD1jwyjcwjJnTyJbOnDDTP8xzNoehaFN3XrjoNgtK7nkdnhpjWZxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت قرمز ۱۱ سوخترسان و ۱ آواکس در منطقه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 181K · <a href="https://t.me/withyashar/20663" target="_blank">📅 00:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20662">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qrzloe6n9HK1j77HZ6niWR9D_7LBtwF38Begz5HQ4611rtdlbhAb037HUKljiyL8do1yByakzKvksGxKOSdvzwxQoNqWuzNHhEeQlAA0CjQAIp1LaH6DQQxLO1Ufz4UhlWEnztTaUy7ghP3TqI4Zh_yztqQQKPkqnzVVknsiHMSDpQbKPG37509ssLlv0wyabXdNEm4TUfJ5OZx_WzAV7ZR45PRJ57XJMkM97VVfgx6SDOrIgO15gljPgG6R07mupjdD-YE0J1IqGoo5h9dOKVD5NIFkxtph6rIeFbSgz0adt-n3Ls-x3ZjCpkMipIEMYz5jt4zJVwS6wrUdPctEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁨ اتاق جنگ با یاشار : فیلمی که کمر خیبر شکن را شکست…
https://www.instagram.com/reel/DbwJLvzRBwp/?igsh=YzEwMDhhc3d3em9u
بررسی اینکه چگونه یک فیلمی که همه به آن خندیدند، پرده از اسرار مهمی از تکنولوژی مورد استفاده در موشکهای جمهوری اسلامی برداشت.</div>
<div class="tg-footer">👁️ 177K · <a href="https://t.me/withyashar/20662" target="_blank">📅 00:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20661">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ:پیروز جنگ غنائم میبره، منم غنائم  ایران عزیزو میبرم
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20661" target="_blank">📅 23:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20660">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=PLcfnhgdooCy-hV8VHLOBuiHd9P8OgmZ0o8TTtWOu9hgTSPL_4q-dCqfGDNQp3Of_PzkyTGToXShJB4t9gu-NSQmA3loNDZ-FEvyrafTs-zInftaGH2nUF0NMR8g8mXXmEktVSX2p9VrHahCtmJNMV7zPnDwWkE7knp9U5rUF2B_4ZaFvJ_R2TKK4VcO4Qk1pnbTShI47LHdZKhDLLeqAL5Mb1MtzTRXeXhmz-NccAOiS9FbAnLydqx5nSW2iIAC3SHUa9VOsuxUdBQpe6ussog4Zfy59PZR08u8CByUGyLjy8M61wyZlDlqvtotQNxdgRVKbVbq5E5Zzez5xfl0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6db8aff1a3.mp4?token=PLcfnhgdooCy-hV8VHLOBuiHd9P8OgmZ0o8TTtWOu9hgTSPL_4q-dCqfGDNQp3Of_PzkyTGToXShJB4t9gu-NSQmA3loNDZ-FEvyrafTs-zInftaGH2nUF0NMR8g8mXXmEktVSX2p9VrHahCtmJNMV7zPnDwWkE7knp9U5rUF2B_4ZaFvJ_R2TKK4VcO4Qk1pnbTShI47LHdZKhDLLeqAL5Mb1MtzTRXeXhmz-NccAOiS9FbAnLydqx5nSW2iIAC3SHUa9VOsuxUdBQpe6ussog4Zfy59PZR08u8CByUGyLjy8M61wyZlDlqvtotQNxdgRVKbVbq5E5Zzez5xfl0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به خبرنگاران و حاضران : اگر امکان داشته باشد، اگر بتوانید به سرعت از اینجا خارج شوید، من سپاسگزار خواهم بود، زیرا ما یک جنگ داریم که باید آن را به پایان برسانیم. این دلیل من برای خروج کمی زودتر است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20660" target="_blank">📅 22:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝓮𝓡𝓦𝓲𝓷🦅</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rERThtINf0_F-QUBW4KPmsDvE5cvwxsESRP2kKiSAN9JcS9u1uVEdOUxvqtCe3qXzl_tcg4lUInscap2MAkrqf-iNcF5b7suMiQyyf0PIUo8SrHLoyu_o8i12RP_G8EI4gIOkDEVZWrJ7gcKGlreWWB-7weEfwLeIXOtpJIRAXuLpO8MMd5yn_rN8Cvcpc8jSZyPgVf9be-4eNxUs17wS76OaFacAf1Wv9M3s8zwxqpu93WzigOG3R7DW0aDZCFGUtXza3QLdHnjPpbW6KC200J8TJk9oUukdK95XgEn_kWj5RwRUv0guQRD2oupfP3FrLnQzjP3vAjzoHPJKpw7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20659" target="_blank">📅 22:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F52TwvSQzg3_p8Gn3c9gLd0-m6mtdWH0WFjx7TS57LvfJtyEiUBsQ9TBn3bk3vuV5CndBAXeeR-23bjnWJuA656PU75QQLsphXm0dDn8hYY3t0xEHkEtmS0isp-XZFNncIrHNqJo5qVlrdf29CmeFr43tSEIZPXWLwANBnvzUqkerreL8pJJ_AsaclGZLkUi3FNY2ziq5OSQrETujilL5u_yyI9k9nRjaeH1ht4PjXH3IIVlIsXbs9sfws1Im4jIgZgRhcRwUtX16_rC5OOT7mRXxDMTjbAChyRLh6mV8aduKxUTxyMCbeAfmlYJ4mEBxErnWlpMeH3wy67mEbuNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد @WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20658" target="_blank">📅 22:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20657">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">رسانه آمریکایی WIRED گزارش داده است که پنتاگون در آستانه امضای قراردادی چندصد میلیون‌دلاری با شرکت AeroVironment برای خرید حداکثر ۲۰ سامانه لیزری ضدپهپاد قرار دارد؛ رقم حدود ۴۰۰ میلیون دلار ولی هنوز رسماً تأیید نشده است. سلاح اصلی این برنامه E‑HEL(لیزر پرانرژی پایدار؛ سامانه‌ای برای سوزاندن و ازکارانداختن پهپادها با پرتو لیزر) است که برای انهدام پهپادهای کوچک، پهپادهای انتحاری و اهداف پرنده گروه‌های ۱ تا ۳ (رده‌بندی ارتش آمریکا بر اساس اندازه، وزن و برد پهپادها) طراحی شده است. نسخه پیشنهادی آن بر پایه سامانه LOCUST(سلاح لیزری متحرک برای مقابله با پهپادها) توسعه می‌یابد و روی خودروهای ISV(خودروی سبک تاکتیکی برای جابه‌جایی نیروهای پیاده) و JLTV (خودروی زرهی سبک چندمنظوره برای عملیات نظامی) نصب خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20657" target="_blank">📅 22:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20656">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">رویترز: ایالات متحده به فروش ۵۲۵۰ موشک دفاعی به بحرین، کویت، قطر و امارات متحده عربی موافقت داد.
این اقدام با هدف جبران کاهش ذخایر موشکی سیستم پاتریوت این کشورها انجام می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/20656" target="_blank">📅 21:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20655">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزارت خزانه‌داری آمریکا: تحریم‌هایی علیه پلتفرم‌های خرید و فروش رمزارزها که از سپاه پاسداران پشتیبانی مالی می‌کنند، اعمال شد.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20655" target="_blank">📅 21:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20654">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اتاق جنگ با یاشار : صدای گشت زنی جنگنده های جمهوری اسلامی در آسمان بندرعباس هم زمان با افزایش حضور سوخترسان ها و متقابلأ جنگنده های رادارگریز آمریکایی
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20654" target="_blank">📅 21:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20653">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شبکه CBS :  مجلس سنای آمریکا به طرح قانونی درباره تحریم‌های روسیه و ایران رای مثبت داد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20653" target="_blank">📅 21:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20652">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20652" target="_blank">📅 21:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20651">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20651" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20650">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">امشب بیدار بمون</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20650" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20649">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromamir</strong></div>
<div class="tg-text">داداش دعا نویسم گفت امشب جنگ خواهد شد</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20649" target="_blank">📅 20:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20648">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw_m2C26_iNC4go-C8584IfTD-62Z-7vPFbZE8scCWUn3h58NyWlE8vWHezycvoIBrc0LfXF4OZJW_qwlPpM9He6Yf0vbUwZZINpsaENgEKVhA-IMlL0P0uCEMuHAWYXLoHvXWzGC82FdEwOOCZG9Tz_TqT9fOzwjOU5ocj3mOMzVTP9LkvjRHIRaCk01OqmeP0r7D_8xsCY_W4ZRhlB7jw1q3XbLqLZk_zBfo7vXaDmxFUipB3pdRtgDsn3hW_bVsOpg-cD8pUy66LdPLGDhItiOyRp-Z4do_i6TI5rdSwpgxMDetpHmWaXhHfI1P-3kQAf2JiG8EOND4dU-8Dmtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون ۳ سوخترسان از تل‌آویو بلند شدند و به سمت خلیج فارس می آیند. همچنین ۵ سوخترسان امریکایی و یک سوخترسان هم از کشورهای همسایه خلیج فارس در منطقه حضور قاطع دارد
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/20648" target="_blank">📅 20:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20647">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nq8o-bVVfzn-v5vvDmurIoQBUj5BClZ-c6FyrxdeBy17c0wyTqiag3mucjCa4xIndq-O0nMlMxw5WQ-_MicLd4BS-BlTrFEjXKRsZKRqizyvLBmMY4cMG6MZshj1MJMzmmBaX5x-n2JSMJc-wJblhoxOARS4DRyxVdj7JPeouO79YCT09WcMHmja3Z-Eeq1Q3P0o5xfpUhBDQoe91hTmPma2RJvIzTTBXEO5SxAiuwFeqAcsyD2xUB7Ov6EeKbi4zH1toDfVGVxa0AlS4Hr_69wJ8tiNyDuogv1DjZ5gslOMgGs-FD10t0UaEEtR8acZTft0o1HWG9ZlSaiPMNSHXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام : خدمه پروازی یک فروند هواپیمای سوخت‌رسان KC-135 نیروی هوایی ایالات متحده، در حال سوخت‌گیری یک فروند جنگنده رادارگریز F-35A در آسمان خاورمیانه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20647" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20646">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خزانه‌داری آمریکا: تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت
تنگه هرمز دیگر هرگز به وضع سابق خود باز نخواهد گشت، زیرا ایرانی‌ها از آن به عنوان یک گلوگاه استفاده کرده‌اند، یا تلاش کرده‌اند از آن به همین منظور استفاده کنند.آنچه در دو سال آینده شاهد خواهیم بود، این است که تنگه هرمز از اهمیت خود کم خواهد شد.این تنگه به یک آبراه معمولی تبدیل خواهد شد، و من معتقدم که بیش از ۵۰ یا ۷۰ درصد از انرژی که در حال حاضر از طریق این تنگه منتقل می‌شود، از طریق خطوط لوله زیرزمینی منتقل خواهد شد
‏در بیانیۀ وزارت خارجه آمریکا آمده: اقدامات ما شبکه‌ای از شرکت‌های مبادله مالی و شرکت‌های صوری که به ایران برای نقل و انتقال میلیون‌ها دلار پول کمک کرده‌اند را هدف قرار می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20646" target="_blank">📅 20:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20645">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزارت دفاع آمریکا پنجمین مجموعه از پرونده‌های مربوط به پدیده‌های ناشناس هوایی و بشقاب پرنده ها رو منتشر کرد در همین راستا شبکه خبری CBS دقایقی‌پیش مصاحبه انجام داده با «آوی لوئب» که ترامپ او را مأمور و نماینده تحقیق بر روی این پروژه کرده، از دست ندید.با زیرنویس فارسی
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20645" target="_blank">📅 19:06 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20644">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سناتور جمهوری‌خواه تد کروز، درباره جمهوری اسلامی : اگر شما یک اسلام‌گرا هستید که از آمریکا متنفر است و سعی دارد ما را بکشد، من از اینکه شما یک کشور یا ملت را رهبری کنید و منابع لازم برای کشتن آمریکایی‌ها را داشته باشید حمایت نمی‌کنم؛ این جایی است که ما باید بر آن تمرکز کنیم؛ حال، چگونه فروپاشی حکومت را رقم بزنیم
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20644" target="_blank">📅 18:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20643">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=qFhIYbDDlg9I4dI_ANDiHiscAbniSnN-qOehC0_FGAfB-nC_JhLsDzSiW-O7X5klS_obvXA3LlqYwI3EnGrM6sjL9u-F44q3IPPgqr2-f9iREMEYrOiJo9xZPnp7Vmfn6vp1VF41GcjDiJ2NmO-ixnWO86VmzBXDBgv7DZAI0f9S1CNg29lpVrROjygp1idKD3aubwPw8KlR9Mc3Cs4wIv4ZX0Kn-i09udBw2vlAkd27zgNv6SL3ZPX1Q9e0BjvUAKVf5O-4lOpFOno-CN8w-b6JL9zPA4WtZS14NS2GQULpDfSUbXicvVQmp0Qf3vKPmnbGgLvR-zXhAFJ3ag6cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f88f7a5ccb.mp4?token=qFhIYbDDlg9I4dI_ANDiHiscAbniSnN-qOehC0_FGAfB-nC_JhLsDzSiW-O7X5klS_obvXA3LlqYwI3EnGrM6sjL9u-F44q3IPPgqr2-f9iREMEYrOiJo9xZPnp7Vmfn6vp1VF41GcjDiJ2NmO-ixnWO86VmzBXDBgv7DZAI0f9S1CNg29lpVrROjygp1idKD3aubwPw8KlR9Mc3Cs4wIv4ZX0Kn-i09udBw2vlAkd27zgNv6SL3ZPX1Q9e0BjvUAKVf5O-4lOpFOno-CN8w-b6JL9zPA4WtZS14NS2GQULpDfSUbXicvVQmp0Qf3vKPmnbGgLvR-zXhAFJ3ag6cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد شهباز شریف، نخست وزیر، محمد بن سلمان بن عبدالعزیز آل سعود، ولیعهد و نخست وزیر عربستان سعودی و رجب طیب اردوغان، رئیس جمهور ترکیه نماز جمعه را در قصر الصفا اقامه کردند. در این مراسم، محمد اسحاق دار، معاون نخست وزیر و وزیر امور خارجه، سناتور محمد اسحاق دار، فرمانده ارتش و رئیس نیروهای دفاعی، سپهبد سید عاصم منیر، و مقامات ارشد سعودی و ترکیه نیز حضور داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20643" target="_blank">📅 18:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20642">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYOcctCRqTPkwndVRXpp9PrfmiFppIjRbzU2cPAzsdqvZBExSvn2Pdq3Q3y_2Ym1l_ZWkkg7V19PgxwktE2NhvrFfDUeDHgcVEr5_-6OMirpH6dnJ0OiSSVJTPhSjXYa9CSpTnogFkzrgk5OWn7oQ5EiSAY4mC5DPZK1XqRnLoTD45iR6UamplJar6fPP35ByCdJUKzHouIkXApqwtWim5cv1cN0JencLgSGePqekoaghhpWIgYna7vh50bY0bMFznQB86gNAtUhmFZ54HIG0yXeWm-P0LDiZXcANm4rSgCyjI72Naw0AjqnNo9d6HKT7aiftXWxOY5Mgz2eUavhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی امشب به روال هر جمعه بیداریم و کشیک رو میدیم
😁</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/20642" target="_blank">📅 18:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20641">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">شبکه کان اسرائیل: ایران صدها موشک پدافندی دوش‌پرتاب از روسیه و چین دریافت کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/20641" target="_blank">📅 17:58 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
