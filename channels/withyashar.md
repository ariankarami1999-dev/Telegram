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
<img src="https://cdn4.telesco.pe/file/fHPZHJZtUXiINapr0PgZLJZIbrSzzD-MoaifJm43THw8FArR_M5Qyl_ud3JLhGyoGRnJEEZqnYuYcjomCESd-HE8MlE_gz_F_LupMoq2exmF85qflGwbIyBGKlDVM3GF7Jt9PRthbiMs_V-tWA_AZcz0w9iabsvPmKs1TX6KaY4dcSFYn8lZJCBC9B3Fp8YocUP_HfpOMsshc4GDmu2KPunbNsXXJCeAgsWz_--tEhOiRHpupkenLXoJXIxf_VpZGM2GUuXObAXtQS4nVHRHiSxgJq4h4Sy4XYPs1VlBmc6ulghQ8K0ba0C-UGotMfVRM_T-Fp9I5AEUBE4LdqtvwQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 310K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 10:30:37</div>
<hr>

<div class="tg-post" id="msg-14269">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">صحنه‌ای از پرتاب حداقل ۱۱ فروند موشک سوخت‌جامد بردبلند علیه اهداف آمریکا در منطقه طی حملات موشکی صبح امروز @withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/14269" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14268">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e315ffa564.mp4?token=qSMCvkgUXRqXHnTojR4bTDCFCb414kHEX_LbaPOli34uCFM5bcMWtdsGnm_C6QuPT1-XcH82onUnPlk9g0mBGFlVJn-0wlqHRNtfynkW-U1eCrhlc1W7-eTYisCMv8KmJkrYb_yLnVTPqtIdA37gN-WP032N0IHFBnw5Gtaqy3IqEIzyOkFFo18aPU1NI8on5lCSv55Y3d3dW-hFnb7AZt0mW2n-ktqf0I5s48USW7vTZSZeAdm0Vn5XP_QeXcOYHqVGjoZoy3BNCV-8CdtnbVk1J-PL_oG4HKH-hMLcamyABL4BrwvieoBnqQD8OoCU86drcQ55LPi2v07uuscEyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e315ffa564.mp4?token=qSMCvkgUXRqXHnTojR4bTDCFCb414kHEX_LbaPOli34uCFM5bcMWtdsGnm_C6QuPT1-XcH82onUnPlk9g0mBGFlVJn-0wlqHRNtfynkW-U1eCrhlc1W7-eTYisCMv8KmJkrYb_yLnVTPqtIdA37gN-WP032N0IHFBnw5Gtaqy3IqEIzyOkFFo18aPU1NI8on5lCSv55Y3d3dW-hFnb7AZt0mW2n-ktqf0I5s48USW7vTZSZeAdm0Vn5XP_QeXcOYHqVGjoZoy3BNCV-8CdtnbVk1J-PL_oG4HKH-hMLcamyABL4BrwvieoBnqQD8OoCU86drcQ55LPi2v07uuscEyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحنه‌ای از پرتاب حداقل ۱۱ فروند موشک سوخت‌جامد بردبلند علیه اهداف آمریکا در منطقه طی حملات موشکی صبح امروز
@withyashar</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/withyashar/14268" target="_blank">📅 10:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14267">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BeHD1LRQvuAR2MRav7tJe2GRMrkvq-jBXKxPpiiOTcBa_Mwy-8JyCb6IJyONwkIhnTGKb7pRTSJpXvEzA_wkP_6rUOg21Gl0TVUBpWiLJcPYsxi8JSjeh0YV_G-Dry-VSM5PHixwMgjWHmyuYYhx1VuWLOQRdRQlOxmVlqOhA7YPH-r-YBDzz5wP9W23UIHSP0-XqheSORjTSHAsPHCN4X0VgaYhWERPWwAuASmK3bvo94pXySNZUDbuZpNzbCBYtQeHms02RxelUecj7E3REAOGJLWqVyiBZmdXa4qdqcmt4_UKdWaZSc_W7x8JSrsAOqbAcZgp1kBdQyVXx9XhAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خمین دم صبح موشک اومدن ول بدن برگشته پایین
@withyashar</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/withyashar/14267" target="_blank">📅 10:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14266">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">هشدار مسکو به تهران:
صلح، پوشش حمله زمینی است، نقشه پنتاگون برای پایان آتش‌بس دوهفته‌ای
شورای امنیت روسیه در بیانیه‌ای تکان‌دهنده که توسط خبرگزاری «تاس» منتشر شد، هشدار داد آمریکا و اسرائیل از پوشش دیپلماسی و مذاکرات صلح برای آماده‌سازی یک عملیات زمینی گسترده علیه ایران استفاده می‌کنن
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/14266" target="_blank">📅 10:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14265">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:یک کشتی تجاری گزارش داده که در جنوب غربی بندر بلحاف یمن، یک قایق کوچک حامل ۶ فرد مسلح به آن نزدیک شده است.
به گفته این سازمان، بین قایق مسلح و تیم حفاظت مسلح کشتی تبادل تیراندازی رخ داده و در نهایت قایق از محل دور شده است.
@withyashar</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/withyashar/14265" target="_blank">📅 10:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14264">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">روزنامه همشهری: خوشبین نباشید، ترامپ از این جنگ دست برنمی دارد
روزنامه همشهری: واقعیت این است که دعوا بر سر چند درصد غنی‌سازی نیست، دعوا بر سر نظم منطقه است؛ بر سر این است که چه‌کسی گلوگاه‌های راهبردی جهان را کنترل کند و چه‌کسی موازنه قدرت آینده را شکل دهد.
برای همین شاید آتش‌بس باشد، شاید وقفه باشد، شاید جابه‌جایی تاکتیک‌ها را ببینیم‌ اما تصور اینکه این کشمکش با چند توافق فنی برای همیشه خاموش شود، خوش‌بینانه است.
@withyashar</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/withyashar/14264" target="_blank">📅 09:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14263">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حمله سنگین اسرائیل به جنوب لبنان
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/14263" target="_blank">📅 09:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14262">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD3J0zeOxO9u1qJJWncnUgVxpcovERYMWEIp2srmS-vCZ8vJ0E6wfE2zROuQrY9P6vlSUkcsq0B_krCjHdt4KPz5iflPZgbQQ-cHD7upWrV_u-jSMmsxKGeCSYi-jOJonmssyZFDAvZEDZ3MCbgLyYH4MgUPXhpA07UDdTZVyxGqjs-rCZt8bPVfwz9T_2gXRE6VZp9uKgfOftd3MwJXnbqvhns13RwbOVPKZSWFV1l1fW7gRQo_hfmJPZOehzEtAqLrXUk3K_E1V8yG3ZuMISoyVTfRkqfAqNyT9RdCVmx_Yw9pHeTn553t5G0mtPBYeB-oiI8CX4r4gsBw1td4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پالایشگاه نفت سامارا روسیه پس از اصابت پهپاد‌های اوکراینی
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/14262" target="_blank">📅 09:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14261">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سخنگوی طالبان:
دیشب ارتش پاکستان حریم هوایی افغانستان رو نقض کرد و چند خونه مسکونی رو در ولایت‌های کنر، خوست و پکتیکا بمباران کرد.
تو این حملات 11 کودک، یک زن و یک مرد سالمند کشته شدن و 14 نفر دیگه زخمی شدن.
@withyashar</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/14261" target="_blank">📅 09:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14260">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۳پا پاسداران: به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن 21 هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارت‌های دشمن، 4 هدف از جمله آشیانه‌های جنگنده‌های F-35 در پایگاه…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/withyashar/14260" target="_blank">📅 09:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14259">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">۳پا پاسداران:
به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن 21 هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارت‌های دشمن، 4 هدف از جمله آشیانه‌های جنگنده‌های F-35 در پایگاه هوایی ارتش آمریکا در الازرق اردن رو مورد هدف و انهدام قرار دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/14259" target="_blank">📅 09:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14258">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرنگار وای نت:
در چند ساعت اخیر در رویدادی جالب سامانه‌های پدافندی آمریکا تمامی موشک‌های شلیک شده به 3 کشور مختلف رو رهگیری کردن. صفر اصابت و شاهکار پاتریوت!
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/14258" target="_blank">📅 09:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14257">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقام‌های آمریکایی نوشت: ترامپ تمایلی به حمله به ایران نداشت، اما پس از توصیه وزیر دفاع و رئیس ستاد مشرک، نظرش را تغییر داد
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/14257" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14256">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیروهای مسلح اردن: پنج فروند موشک ایرانی که به سوی پایگاه الازرق شلیک شده بودند را رهگیری و سرنگون کردیم. در پی سقوط بقایای موشک‌های رهگیری‌شده، هیچ‌گونه خسارت یا جراحتی ثبت نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/withyashar/14256" target="_blank">📅 09:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14255">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">https://t.me/boost/withyashar
۳۹۰ بوست پرمیوم هاااا</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14255" target="_blank">📅 03:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14254">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">۴ انفجار‌شدید بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14254" target="_blank">📅 03:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14253">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هم اکنون انفجار سنگین سیریک و اطراف را لرزاند
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/14253" target="_blank">📅 03:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14252">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">حملات جدید به بندر عباس و سیریک
@withyashar</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/14252" target="_blank">📅 03:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14251">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گزارش انفجار در قشم
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14251" target="_blank">📅 02:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14250">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">کانال 12 اسرائیل: در موج دوم حمله‌ها به ایران، آمریکا داره پدافندهای هوایی و رادارها رو هم هدف حمله قرار میده.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14250" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14249">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-zJIBiyX_e4h75eKBFkGOXsQVQeTm1RGtZZPNReiF5OVtl9jmsQw3yEuBqoV_jJr01vex-q-YbJlvCH8-zc0l0mnRkpgEjoZGh8HVZ8mGSBEKbGPsVxm7GDGw-TmWx4ftdxAh4L20l03QY_fuhlYbEn4TzlF_w8zbrb6_cORfpJmkCI5FSS0rFoH-ji_IKH7d6YGDu3icBUP_bYKFHnwjyr7tIu9uWNeK-KmwVM7zlEkDfgG3keDGrJGNTF68H3m2C1bALP8h9yOT14Ne8wg57CScmIrW0W4ad4kovP5ropwI2nijPWS76k-AHy2XXXqCj3ggvC1wYnG8UsFknuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فاکس نیوز : بر اساس اعلام مقامات نیروی دریایی آمریکا، نزدیک به ۲۰ هزار ملوان و تفنگدار دریایی آمریکایی در حال حاضر در دریا و مستقر بر روی دو ناو هواپیمابر «یواس‌اس آبراهام لینکلن» و «یواس‌اس جرج اچ. دابلیو. بوش» هستند؛ به‌همراه ۱۸ ناوشکن مجهز به موشک‌های هدایت‌شونده، یگان اعزامی سی‌ویکم تفنگداران دریایی، و بیش از دوازده اسکادران هوایی.
این تجهیزات و نیروها در مناطق مختلفی از جمله شرق مدیترانه، دریای سرخ، شمال دریای عرب و دریای عرب پراکنده شده‌اند؛ جایی که نیروهای آمریکایی در حال کمک به دفاع از اسرائیل، مقابله با تهدیدات حوثی‌ها، انجام عملیات مرتبط با ایران، و حمایت از امنیت دریانوردی در اطراف تنگه هرمز هستند.
این نیروی دریایی بخشی از حدود ۵۰ هزار نیروی نظامی آمریکاست که در حال حاضر در سراسر خاورمیانه مستقر هستند.
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14249" target="_blank">📅 02:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14248">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دو دقیقه پیش سه انفجار از اسکله جاسک @withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14248" target="_blank">📅 02:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14247">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14247" target="_blank">📅 02:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14246">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/14246" target="_blank">📅 02:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14245">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دو دقیقه پیش سه انفجار از اسکله جاسک
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14245" target="_blank">📅 02:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14244">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فارس جوگیر شد و گزارش کرد :
گروه هکری حنظله: مختصات تمام نیروهای نظامی تروریستی آمریکا در کشورهای خلیج‌فارس به سپاه پاسداران انقلاب اسلامی منتقل شد.
به‌زودی به پهپادهای شاهد-۱۳۶ «خوش‌آمد» خواهید گفت.
شما بازی را شروع کردید؛ ما تعیین می‌کنیم چگونه پایان یابد.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14244" target="_blank">📅 02:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14243">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیویورک تایمز گزارش می‌دهد که حملات هوایی آمریکا به پایگاه‌های نظامی و دریایی، تأسیسات راداری و باتری‌های موشکی در پنج مکان در سواحل جنوبی ایران، از جمله موارد زیر، هدف قرار گرفته‌اند:
پایگاه‌های دریایی در سیریک و جاسک
سایت‌های دفاع هوایی در بندرعباس
باتری‌های موشکی در قشم۶
برخلاف گزارش صداوسیما مخزن آبی در سیریک هدف نگرفته است و مانند مدرسه میناب رو به دروغ آورند!
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/14243" target="_blank">📅 02:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14242">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">جنگ امیر تتلو و زندان
امیر تتلو از پشت تلفن زندان موزیک ضبط کرده و همین الان پخش کرده
https://youtu.be/ixhpdO88-IY?si=dmb7e06_W8ShLkkA
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/14242" target="_blank">📅 02:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14241">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرنگار صداسیما در سیریک: در پی حمله امشب دشمن آمریکایی به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/14241" target="_blank">📅 02:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14240">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اتاق جنگ با یاشار : با خسته شدن و خوابیدن ادمین های تلگرام جنگ هم تمام میشود
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/14240" target="_blank">📅 02:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14239">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258b122927.mp4?token=qtNh0pZDEQa1NZ5xWugulfpb6RHWPQfJk7KB9ztwJryGTEuK7yINWgnqBFI1u7py03yuCturM8CeoOKYqjXW9HHRjkCBBvMSov-FAMUsbMAYeqEOqI_sygQQK_rTu-VrGfj1B6Mgljdm998z0nQbYzG46me2WEFLkMiHnXj6OyKdC1KyWKXApSDWM2TVEmUsoxfdPZkh3fdvifvmMg_q7-ThFde-syzDNvQal5EM5PmNeJBXpUytGGJ-rWK0ds_fz_--rH-4R6VobjuUfLC3ZYPBs6aSaodnxm7ZTg8IpMsX9JlZlEGHZqjfNUP4YwiyUNIJq7Fq4XY4iMhRadb2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258b122927.mp4?token=qtNh0pZDEQa1NZ5xWugulfpb6RHWPQfJk7KB9ztwJryGTEuK7yINWgnqBFI1u7py03yuCturM8CeoOKYqjXW9HHRjkCBBvMSov-FAMUsbMAYeqEOqI_sygQQK_rTu-VrGfj1B6Mgljdm998z0nQbYzG46me2WEFLkMiHnXj6OyKdC1KyWKXApSDWM2TVEmUsoxfdPZkh3fdvifvmMg_q7-ThFde-syzDNvQal5EM5PmNeJBXpUytGGJ-rWK0ds_fz_--rH-4R6VobjuUfLC3ZYPBs6aSaodnxm7ZTg8IpMsX9JlZlEGHZqjfNUP4YwiyUNIJq7Fq4XY4iMhRadb2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فعالیت پدافند مشهد امشب.
@withyashar</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/14239" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14238">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جسی واترز از فاکس درباره مذاکرات ایران:
فکر می‌کنم ما همین الان یک پیشنهاد دریافت کردیم/از واشنگتن می‌شنوم که از آنچه می‌بینیم خوششان آمده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14238" target="_blank">📅 02:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14237">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f374eeb00.mp4?token=PzXGPxxmd8Y4p6MbGrnNAHf8itLKU2QGo9DQKmgFEGIaFWSkGf_LJTwtOmX-bvKHbJtaR2l43qp6FAiOBJF4q95d42wzfkkT4CaqKU7PtzXUQiAvyNr0xznoD__hOy0NGv4pvNXNfCQ4p5BxhreWEyzIdJz7tIoffsg0U-oOQo3Q-WisB39ieYU2Vz8TSNWxD9Akv2VwUoAH-aOKyWRb8PYZo3Y2_oTrO_DKzx5_rClm8jMU-p60C6zGSf6RoU4GLApVrV7avllUprT-z0BLYXCEMOmBE8eYkIDmVNo7H_69bhtdjc2MSSkEqC-Yg0oTU8Q2k4rLWwJOYwtgpj-JMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f374eeb00.mp4?token=PzXGPxxmd8Y4p6MbGrnNAHf8itLKU2QGo9DQKmgFEGIaFWSkGf_LJTwtOmX-bvKHbJtaR2l43qp6FAiOBJF4q95d42wzfkkT4CaqKU7PtzXUQiAvyNr0xznoD__hOy0NGv4pvNXNfCQ4p5BxhreWEyzIdJz7tIoffsg0U-oOQo3Q-WisB39ieYU2Vz8TSNWxD9Akv2VwUoAH-aOKyWRb8PYZo3Y2_oTrO_DKzx5_rClm8jMU-p60C6zGSf6RoU4GLApVrV7avllUprT-z0BLYXCEMOmBE8eYkIDmVNo7H_69bhtdjc2MSSkEqC-Yg0oTU8Q2k4rLWwJOYwtgpj-JMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهده پهپادهای انتحاری‌ ایرانی در آسمان عراق
@withyashar</div>
<div class="tg-footer">👁️ 93.2K · <a href="https://t.me/withyashar/14237" target="_blank">📅 01:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14236">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پولیتیکو به نقل از یک مقام ارشد در کاخ سفید: هیچ تغییری در شرایط بوجود نیامده و آتش بس کماکان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/14236" target="_blank">📅 01:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14235">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ولی یه حمله شکی توش‌نیست حمله شما به دایرکت اتاق جنگ
😭
🤣
❤️‍🩹
🙌🏾</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14235" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14234">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هم اکنون خاورمیانه:  حملات آمریکا به ایران حملات اسرائیل به لبنان حملات پاکستان به افغانستان حملات ترکیه به عراق حملات ایران به بحرین و کویت  @withyashar</div>
<div class="tg-footer">👁️ 96.2K · <a href="https://t.me/withyashar/14234" target="_blank">📅 01:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14233">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">شلیک دو موشک از سیرجان
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/14233" target="_blank">📅 01:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14232">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گزارشات از حملات توپخانه ای عربستان به یمن
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/14232" target="_blank">📅 01:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14231">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 92.7K · <a href="https://t.me/withyashar/14231" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14230">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سی ان ان به نقل از مقامات آمریکایی:
انتظار می‌رود چندین دور حملات دیگر بر علیه ایران انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/14230" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14229">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هم اکنون خاورمیانه:
حملات آمریکا به ایران
حملات اسرائیل به لبنان
حملات پاکستان به افغانستان
حملات ترکیه به عراق
حملات ایران به بحرین و کویت
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14229" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14228">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">هم اکنون حملات ترکیه به شمال عراق
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14228" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14227">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اتاق جنگ با یاشار : خدای من و شما شاهد است که هیچ ردبولی رو بیهوده حروم نکردم
🤣
✌🏾
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/14227" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14226">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مقام ارشد آمریکایی به باراک راوید خبرنگار آکسیوس: عملیات ادامه داره و آماده‌ایم برای چندین حمله دیگه.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14226" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14225">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش
انفجار در اهواز
.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14225" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14224">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک مقام آمریکایی به سی‌ان‌ان:
حملات جدید به منزله یک شلیک هشدارآمیز به ایران است و ایالات متحده معتقد است این حملات مانع مذاکرات برای پایان دادن به جنگ نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14224" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14223">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سید مجید موسی : ‏و ما النصر الا من عند الله العزیز الحکیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/14223" target="_blank">📅 01:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14222">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/14222" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14221">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هم اکنون بمباران مواضع حکومت طالبان افغانستان توسط F16 های ارتش پاکستان
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/14221" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14220">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ به ای‌بی‌سی نیوز:
من به پاسخ قوی اعتقاد دارم و این رویکرد من است. ما توافق بسیار خوبی با ایران داریم و فکر می‌کنم همینطور هم خواهد ماند.
@withyashar
یاشار : زبانم قاسمه کتلته</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/14220" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14219">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یک مقام آمریکایی به فاکس نیوز گفت: حملات هوایی علیه ایران «ادامه دارد» و اهداف شامل پدافند هوایی و تأسیسات راداری است.
@withyashar</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/14219" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14218">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گزارش ها از شلیک موشک‌های سپاه از کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/14218" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14217">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اتاق جنگ با یاشار : امریکا و اسراییل به طور هماهنگ و گازانبری به ایران و لبنان حمله کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/14217" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14216">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">۳پا :
حملات سنگین علیه امریکا در راه است..
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14216" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14215">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کشورهای حوزه خلیج فارس در حال بستن حریم هوایی خود میباشند.
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/14215" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14214">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انفجار در ضاحیه بیروت  @withyashar
🇮🇱</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/14214" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14213">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خبرگزاری تسنیم:
آغاز حملات ایران
جمهوری اسلامی: همانطور که چند ساعت پیش هشدار داده بود، پاسخ قاطعی به تجاوز آمریکا خواهد داد که تحت پوشش سقوط هلیکوپتر آپاچی انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/14213" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14212">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از خوزستان موشک زدن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93.7K · <a href="https://t.me/withyashar/14212" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14211">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار در ضاحیه بیروت
@withyashar
🇮🇱</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/14211" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14210">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🤣
🤣
🤣
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/withyashar/14210" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14209">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سامانه‌های دفاع هوایی دوباره در بندرعباس، قشم و سیریک فعال شده‌اند
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/14209" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14208">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فهرست اولیه اهداف:
– پایگاه دریایی سیریک
– پایگاه دریایی جاسک
– موقعیت پدافند هوایی بندرعباس
– باتری موشکی ساحلی میناب
– باتری موشکی ساحلی قشم
– بندر قشم
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/14208" target="_blank">📅 01:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14207">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">مقام آمریکایی: نیروهای ما به حملات خود علیه ایران برای دفاع از خود ادامه می دهند و عملیات همچنان ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/14207" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14206">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صداوسیما : پایگاه های آمریکایی رو هدف قرار میدیم.
@withyashar</div>
<div class="tg-footer">👁️ 92.8K · <a href="https://t.me/withyashar/14206" target="_blank">📅 01:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14205">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صدا و سیما می گوید دست کم صدای 6 انفجار در جزیره قشم شنیده شده است
@withyashar</div>
<div class="tg-footer">👁️ 92.1K · <a href="https://t.me/withyashar/14205" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14204">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">روابط عمومی نیروی هوافضای سپاه اعلام کرد تا لحظات آینده پاسخ سنگین به اقدامات خصمانه دشمن داده خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14204" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14203">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14203" target="_blank">📅 01:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14202">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گزارش‌ها از هدف قرار گرفتن دکل‌های مخابراتی درقشم
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/14202" target="_blank">📅 01:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14201">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
هم اکنون ترامپ به ABC درباره حملات ایران:فکر می‌کنم پاسخ دادن بسیار مهم است،آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم،
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند،من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد.
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/14201" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14200">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجارها در قشم، بندرعباس، سیریک و جاسک
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/14200" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14199">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال 14 اسرائیل: ترامپ نتانیاهو رو قبل از آغاز حمله در جریان قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/14199" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14198">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">۹ انفجار بندر عباس
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/14198" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14197">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjIfOz_vtLhQyr51awFJtE2LNdslkSugSgWHhOeRigWMXXYJyiEM_DCg2xOWOyMOIEqyUwZxczVnH843VuHOox2FTGl3hcj2OJ6I0rublrrrD6bSB54d96PEbrSeOp5Kww5WVDj3tHtqZgVLi2GSaUAqdkAUCFVnkLCZkVgU9TW-uoTV06U_s2jDeDPjOBlxp0IvcN1COjpl101KenvSoKb88Y8T-I-f-MYUxnq5sCLb8pxXE40HjhFvoEzYhpehmA8x_hvrzAln3SfqF3Vjy7hVvOPvpAQ-6HbkPI-1Ih4V5Q_sEQKxLWt2fMHtGczKM1meGHNekkODbdDG-tAgUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@withyashar
شکار‌ لحظه کردم</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/14197" target="_blank">📅 00:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14196">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">طبق گزارش ها تاکنون حملات در جنوب ایران متمرکز بوده است.
هم‌اکنون پدافند در جنوب ایران مشغول دفع حمله است
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/14196" target="_blank">📅 00:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14195">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارتش آمریکا از شلیک گسترده موشک های کروز به سمت ایران خبر می‌دهد.
@withyashar</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/14195" target="_blank">📅 00:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مسیج های زیاد از انفجار‌ در ‌سیریک @withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/14194" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14193">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOBas6mCMu1yRIXMiuaNcKa9Yy0pLAsX7vJr0s6GpBuGFHVTUyIo5mJuwNoJvHvRnNvoQx6q4wjGuBE8BFLwuiUpzdhqahfNBGOJfcdT3ziiaJNMQ-F6JuvEsuHhO2R48JD-XR17amj-IMARq8QmQGKDZw8v2y0nvqYBDdje8khkZ2G5MCchisBXZBdHIo0Z_6EgcnSJL_8B1MDCdIpjssb67Vy8S5qZeaxGo2Sxbkj5oBONFY1pUzSDr1IuWXL-NQMcP0tFnCL1pncgjGcSkdvGiztk7CfB-b8i2BYGldF1E2TlWdgu9_u21mNXur8wvBVM3zvM-fPrdI0t-zvuiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری : نیروهای سنتکام به دستور فرمانده کل، از ساعت ۵ عصر به وقت آمریکا، در پاسخ به ساقط شدن بالگرد آپاچی ارتش «حملات دفاعی» علیه ایران شروع کردن و این یه واکنش متقابل و متناسب به حمله ایران بوده.
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14193" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14192">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/withyashar/14192" target="_blank">📅 00:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14191">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گزارش‌های غیر رسمی از هدف قرار گرفتن پایگاه شهید راهبر در میناب
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/14191" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14190">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خبرنگار کانال 14 اسرائیل:
هرچند امیدوارم اشتباه کنم ولی پیش‌بینی‌ من اینه که ترامپ در پاسخ به سرنگونی بالگرد آمریکایی، یه حمله‌ جزئی و نمادین انجام میده؛ مثلا یک ایستگاه راداری و چند سکوی پرتاب ضدموشکی در منطقهٔ تنگه‌ هرمز رو میزنه.
یعنی حملاتی از جنس همان حملاتی که قبلاً هم چند بار در جریان آتش‌بس دیدیم، نه چیزی که جنگی رو با ایران شعله‌ور کنه.
@withyashar</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/14190" target="_blank">📅 00:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14189">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">گزارش های زیاد انفجار هم اکنون از قشم و بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/14189" target="_blank">📅 00:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14188">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_JUr5kN0Lforq-Xd0znoPA5JvRJal4fbooQtTNC6V0Iup0auimfFDFA46S2k7BLzb6UaKO5rbpG_OIriSkCBqfytlVcN8GlRoCG5SMRG1Ubmf8g5xW0WtJQZBWsdk9mQsUtj2D7FvvJO3JIss1RulBLOQE_dKfWEGuE6S-kKpE2WLjAXRiasoNbIzTFwFiJ5adNLak9fBzZyFdTk4ephKe0xjgO-kRdMB2wItnVE8u-5JZ7002ByzqbpWVAhmVhN2_FOKo8TppuNmJ93jSc_E1wBrGYAZVQ3F5BJgLjWy1ULvJvXHPs-Oi902bMfZTEzvt9VlGDJhfh3IzCrA0xhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون انبوه هواپیما های آمریکایی در جنوب ايران
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/14188" target="_blank">📅 00:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14187">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مسیج های زیاد از انفجار‌ در ‌سیریک
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/14187" target="_blank">📅 00:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14186">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/14186" target="_blank">📅 00:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14185">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ان بی سی : فرمانده سنتکام کلی اطلاعات به اعضای دو حزب ارائه داده که همه قانع شدن حمله ایران به هلیکوپتر اپاچی کاملا عمدی بوده و باید تلافی کنن
@withyashar
این اولین باره که دموکرات ها تایید میکنن حمله به ایرانو</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/14185" target="_blank">📅 00:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14184">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اتاق جنگ با شما : صداهای مشکوک اطراف اصفهان
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/14184" target="_blank">📅 00:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14183">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">صدا و سیما : به جون مادرمون ما هلیکوپتر نزدیم اصلا امروز کلا نبودیم
🤣
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14183" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14181">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aca1a7b7a.mp4?token=Vg8UKoOCluMwEqCnzfKpGldM7V1NIESP1E-az7p8jjNO9v3RsWapZZ710fh9sxA2Rb-VjnEgYZGMdYWm_-YbZZVmSnEUogzCcVADoqdeZp1cltnDRgHQikR7jRPpsZQjIkgEAppufVps03wfXLO0PgNOX9WgCPQVA9fIn_XyTv92b2Dtc8hVDPRVzXG_WSXJCTF30ZyWwEM9CwcG4YfCKQBQfLC_voFrN9HGQOzuzF7ployD-XB89VNpdeQQ-m-buzaMbRjQwmAnFLJcG9CcS7La-E1DPhw0FNulab5F0_q7Bh0-qmVdA4GBXQHY5BjBL3ELS3pzkz5FfPY3hwUWAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aca1a7b7a.mp4?token=Vg8UKoOCluMwEqCnzfKpGldM7V1NIESP1E-az7p8jjNO9v3RsWapZZ710fh9sxA2Rb-VjnEgYZGMdYWm_-YbZZVmSnEUogzCcVADoqdeZp1cltnDRgHQikR7jRPpsZQjIkgEAppufVps03wfXLO0PgNOX9WgCPQVA9fIn_XyTv92b2Dtc8hVDPRVzXG_WSXJCTF30ZyWwEM9CwcG4YfCKQBQfLC_voFrN9HGQOzuzF7ployD-XB89VNpdeQQ-m-buzaMbRjQwmAnFLJcG9CcS7La-E1DPhw0FNulab5F0_q7Bh0-qmVdA4GBXQHY5BjBL3ELS3pzkz5FfPY3hwUWAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/14181" target="_blank">📅 00:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14180">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/14180" target="_blank">📅 00:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14179">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/14179" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14178">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس :
محاصره دریایی یک عملیات نظامی است و ما به آن پاسخ داده و باز هم خواهیم داد.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/14178" target="_blank">📅 00:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14177">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الجزیره به نقل از یک مقام ایرانی :
بالگرد آپاچی که منهدم شد به علت پرواز در آسمان سرزمینی ایران منهدم شد و برخلاف ادعا ها بر فراز آب های بین المللی پرواز نمی‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/14177" target="_blank">📅 00:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14176">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9cb2f588.mp4?token=LX7yBivLhIoSsIQqMa_6ADHcf0vLu4mEnL3PteXm2sOG0N1-MIdjwGzhgqA667ob48sSayeaNFwyHkbBJDKD3FZRanTieS7SIqSkwPc4DQ7Zftj0oWlaDGSXKczEqCaj1sqaUmsdH2hNXnKWrFecxqFQfF_U9lNJdAhuqSvdO9JcJ8KMionT-TPmqQc7Ku_liR7lLj6O8Z0mrElVfFkvtw7DBLhlDirnltuc1YEQrnc2Ct_febYcgD4ZFr4nt71gCiHcldPEUXVvArqus1_Mqw2ya6DDonBcBtQcmtGCW_MKG0yguM93QAvkr5eih2VS_xbdLUUPmcY6YKhsOvTvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9cb2f588.mp4?token=LX7yBivLhIoSsIQqMa_6ADHcf0vLu4mEnL3PteXm2sOG0N1-MIdjwGzhgqA667ob48sSayeaNFwyHkbBJDKD3FZRanTieS7SIqSkwPc4DQ7Zftj0oWlaDGSXKczEqCaj1sqaUmsdH2hNXnKWrFecxqFQfF_U9lNJdAhuqSvdO9JcJ8KMionT-TPmqQc7Ku_liR7lLj6O8Z0mrElVfFkvtw7DBLhlDirnltuc1YEQrnc2Ct_febYcgD4ZFr4nt71gCiHcldPEUXVvArqus1_Mqw2ya6DDonBcBtQcmtGCW_MKG0yguM93QAvkr5eih2VS_xbdLUUPmcY6YKhsOvTvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 89.3K · <a href="https://t.me/withyashar/14176" target="_blank">📅 00:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14175">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc82e1504.mp4?token=H5efP7NjDe5KjnwKaGtPxJlWclvcXIAvjiifznXs2UNHLLgz_WGwNEBN1B7citUPbXHY4hJmHqo0PxqzWHmVbXMfriUAgDboPo8Su78kzCqdCvEccRWt--sAmbTZd-9QRmaB8ufysyb8o3YmtN3AOVpK8LDzBziFhmf8MVHua80IK6GsieJ-ykQl0U7RKYKI-oUyIHPuerrQVqGUzzDrTzcaZpU_pDT8Rq3hhaXsCPen9qFs8VEOLT3FV_6rMrILynu-YKsHTVth4CTpsIPYsPMLv9pSR8ulW4XmOtgXi6xbF7CLCalHI1FqrBmrwyg_zh0WvBx8qTHq4u4CyK-HCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc82e1504.mp4?token=H5efP7NjDe5KjnwKaGtPxJlWclvcXIAvjiifznXs2UNHLLgz_WGwNEBN1B7citUPbXHY4hJmHqo0PxqzWHmVbXMfriUAgDboPo8Su78kzCqdCvEccRWt--sAmbTZd-9QRmaB8ufysyb8o3YmtN3AOVpK8LDzBziFhmf8MVHua80IK6GsieJ-ykQl0U7RKYKI-oUyIHPuerrQVqGUzzDrTzcaZpU_pDT8Rq3hhaXsCPen9qFs8VEOLT3FV_6rMrILynu-YKsHTVth4CTpsIPYsPMLv9pSR8ulW4XmOtgXi6xbF7CLCalHI1FqrBmrwyg_zh0WvBx8qTHq4u4CyK-HCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/14175" target="_blank">📅 23:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14174">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس تروریستی ج.ا :
دست آن رزمنده‌ای که در تنگه هرمز با سرنگونی هلیکوپتر آمریکایی (همچون شهید نادر مهدوی) سیلی دیگری به شیطان زد را می‌بوسیم، از او به عنوان یک قهرمان تجلیل خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/14174" target="_blank">📅 23:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14173">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1747743dd.mp4?token=GKOj7x4evP5xoOTd5L04mYGJnv3RcdJdnURUkmbGd49PO8PBWuDV-xChg-bqqvRq140B39UumbUPJC8nsDrWIUEuQiUZ29EC0nCb4Z7tDVWRuIKzXrazfM5ezK2na2SM8s2yGqLrqEEc8wm7ksI6qDPUFgXPVB3YBZwydNOKJIdOlQENwyXIvlcW9KhwHkRsE0VwfMCAL66lRtAej8hcb61ngxrVt_IZYPYvjl2Qkx5A8mwwF2btEMMRd7RsgqDEKKm07r4SmslhXCmOcy_smbfnwcrljvz1YUEHnYSDg4cEpE9a48FBuitlkXjvxzW_iKuKslbSP-MAH4dWVtpz8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1747743dd.mp4?token=GKOj7x4evP5xoOTd5L04mYGJnv3RcdJdnURUkmbGd49PO8PBWuDV-xChg-bqqvRq140B39UumbUPJC8nsDrWIUEuQiUZ29EC0nCb4Z7tDVWRuIKzXrazfM5ezK2na2SM8s2yGqLrqEEc8wm7ksI6qDPUFgXPVB3YBZwydNOKJIdOlQENwyXIvlcW9KhwHkRsE0VwfMCAL66lRtAej8hcb61ngxrVt_IZYPYvjl2Qkx5A8mwwF2btEMMRd7RsgqDEKKm07r4SmslhXCmOcy_smbfnwcrljvz1YUEHnYSDg4cEpE9a48FBuitlkXjvxzW_iKuKslbSP-MAH4dWVtpz8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد واشنگتن به دستیابی به توافق با ایران نزدیک شده است.
ونس گفت:
«ممکن است این توافق هفته آینده حاصل شود، یا شاید چند ماه دیگر.»
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/14173" target="_blank">📅 23:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14172">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترامپ به وال استریت ژورنال: حادثه هلیکوپتر آپاچی موضوع جدی نیست و خلبان حالش خوب است!
ترامپ: به زودی پایان جنگ و پیروزی آمریکا بر ایران را اعلام میکنم امسال جام جهانی خوبی خواهیم داشت.
ترامپ: محاصره ایران رو به شدت فقیر میکنه و تا زمانی که نیاز باشه ادامه داره.
@withyashar
🚨
«این خبر ‌وال استریت ژورنال مال قبل از پست  تهدید ترامپ در تروث است»</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/14172" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرنگار: شما گفتید آمریکا باید به سرنگونی آپاچی پاسخ دهد، آیا هنوز هم این نظر را دارید؟
ترامپ: من مجبور نیستم کاری انجام دهم، ما همه کارت‌ها را در دست داریم. مجبور نیستم این کار را بکنم اما ببینید، احتمالاً این کار را خواهیم کرد، باشه؟
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14171" target="_blank">📅 23:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ درباره ایران به ABC:
یک نفر باید همه آن زیرساخت‌ها را بسازد، پل‌های جدید، فلان چیز جدید، نیروگاه‌های جدید... آنها از یک تریلیون دلار صحبت می‌کنند، احتمالاً بیشتر...
@withyashar</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/withyashar/14170" target="_blank">📅 23:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">منابع آمریکایی و اسرائیلی ادعا می‌کنند که اقدام نظامی قریب‌الوقوع آمریکا علیه ایران ظرف چند ساعت آینده انجام خواهد شد و آن را حرکتی بزرگ با دامنه نامحدود می‌نامند.
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/14169" target="_blank">📅 23:39 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
