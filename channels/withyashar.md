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
<img src="https://cdn4.telesco.pe/file/XrPGZKWlPGPPA68Zo9HES1nnocbOefdvbfxUyQ81aOlyNYl3SoXtMCYwLpNa0CF4DW3PJJeE265Ag-vWB3hmBTlk9kWPbUqyzzPF7BjuR5KNWe2lf4GHSDOa2rBHDAmtr09yMQBzFyYWAaasRyNb5g3MgEaMdbE90-pUs63k1zyGVV9jwFoTL4vUtPWkwS385CX7inLUPJzSVocc7x0A30DgSvImUP1enRClkFWVDVjg-T09SCPpo4NE2dRF9w2IEYNrL8hRhkN7budGflDj5EeC0wETJajcO0fvpH74jzpYji106Qj9zcccqluAxoUl-dXWRQYMja8UiCj7WRHmcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 424K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 21:23:04</div>
<hr>

<div class="tg-post" id="msg-19480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MvqJNZnZhmeITNLlYPXAMwLmWFYR5F9ub_a5-AwpKzdDjrYnKJBihx_TIt1L1Mc-rbFR2xg0ESJIqYcc8EyxdpcC_QC0XfMjpYBG4eGKStZPCGJErNb8-GVeAyS7JcOf-OsB43DwQ_mc34VAeZMcMydPzyL9wXtwKWX3HpUMRiZ1ecwMfekAz8KxGyELAlXj0DA7vmID1CxFf2YrlFktKs4rsXmWDccTaiTzFc61FPJbdeNkODKUU6j7sqnkM6YMmhKZFTNV_YmMBmEdfTTVOSpuwePItOeYtvjhGQl4yzfJWVJIcgeHuIS5Lr0S2rEGQrU3ce7GYISeZ3CovhN1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون؛ نفس های آخر رژیم
،
استقرار
موشک ذوالفقار در میدان آزادی
@WarRoom</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/withyashar/19480" target="_blank">📅 21:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به گفته منابع غیر رسمی اعضای سفارت آلمان از ایران خارج شدند
@WarRoom</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/19479" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19477">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بریتانیا پس از تهدیدات جمهوری اسلامی : نیروهای ما آماده مقابله با هرگونه حمله هستند،.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/19477" target="_blank">📅 20:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19476">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است ‌@WarRoom</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/19476" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19475">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تسنیم: تکذیب هرگونه اصابت جدید در جزیره لارک/ صدای انفجارها از سمت تنگه هرمز است
‌
@WarRoom</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/19475" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19474">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کانال ۱۴ : موشه سعدا، نماینده مجلس از حزب لیکود، در یک برنامه زنده تلویزیونی گفت: «همه ما می‌دانیم که به سمت حمله به ایران، شاید حتی همین آخر هفته، می‌رویم»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/19474" target="_blank">📅 20:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19473">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سنای آمریکا سد راه محدودیت جنگی ترامپ شد
مجلس سنای آمریکا، طرحی را که قصد داشت اختیارات نظامی دونالد ترامپ برای آغاز جنگ احتمالی علیه ایران را محدود کند، متوقف کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/19473" target="_blank">📅 20:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19472">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وزارت امور خارجه آمریکا: از شهروندان آمریکایی مقیم خاورمیانه درخواست می‌شود برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی در این منطقه آمادگی داشته باشند. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/19472" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وزارت امور خارجه آمریکا: از شهروندان آمریکایی مقیم خاورمیانه درخواست می‌شود برای احتمال لغو پروازها و بسته شدن مسیرهای هوایی در این منطقه آمادگی داشته باشند.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19471" target="_blank">📅 19:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی:
ایران آخرین پیشنهاد آمریکا برای صلح را رد کرده است.
ما در حال تلاش هستیم، اما ایرانی‌ها تمایلی به همکاری نشان نمی‌دهند
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/19470" target="_blank">📅 19:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امیدیه ستون دود دیده میشود ولی صدایی به گوش‌ نرسید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/19469" target="_blank">📅 19:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اهواز هم زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/19468" target="_blank">📅 19:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝒎𝒐𝒉𝒂𝒎𝒎𝒂𝒅</strong></div>
<div class="tg-text">https://t.me/boost/withyashar
یاشار لینک boost رو دوباره بزار اعضای جدیدی که پرمیوم دارن هم حمایت کنن سطح ۲ رو از دست نده کانال.</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/19467" target="_blank">📅 19:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خبرگزاری‌  رژیم : یک موشک آمریکایی منطقه ای در ساحل شهر سوزا در جزیره قشم، در جنوب کشور را هدف قرار داد. @WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19466" target="_blank">📅 19:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجار در کویت
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/19465" target="_blank">📅 19:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرگزاری‌  رژیم : یک موشک آمریکایی منطقه ای در ساحل شهر سوزا در جزیره قشم، در جنوب کشور را هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/19464" target="_blank">📅 19:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارهایی از جزیره بوبيان گزارش میشود
.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19463" target="_blank">📅 19:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پدافند قشم فعال شده
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19462" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19461">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به نشریه "اکسیوس" گفت: ایرانی‌ها می‌خواهند مذاکره کنند، اما در حال حاضر آمادگی امضای توافق را ندارند و هنوز به اندازه کافی تحت فشار قرار نگرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/19461" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19460">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مجری : آیا مجتبی خامنه‌ای زنده است؟  نتانیاهو: فکر می‌کنم او زنده است. @WarRoom</div>
<div class="tg-footer">👁️ 93.5K · <a href="https://t.me/withyashar/19460" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19459">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ به نشریه اکسیوس: اسرائیل در عرض دو دقیقه به حملات علیه ایران خواهد پیوست، اگر از آن بخواهیم، اما ما نیازی به این کار نداریم.
@WarRoom</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/19459" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19458">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترامپ در گفتگو با شبکه ۱۲ اسرائیل اعلام کرد که در حال بررسی یک «حمله گسترده»، بزرگ‌تر از هر آنچه پیش از این انجام شده، است و گفت که به اتخاذ تصمیم نهایی نزدیک شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/19458" target="_blank">📅 19:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19457">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbda7bde91.mp4?token=RvDN5wq-uPBX3xhwrHVrjoMRzJNNXsQGgbn6uOsa7XqJdWZuTEM23G23ps4A8zVr_9I9vEuu35W8Ma-gw0jO-KC7xxUXy3Yrqu6Z14ZgwDmcoWNe9VaoK7_3yLmVZ2qqoZA34W7-XiUTQbGRr5-Ft8_VQIs0OIJ1mAmzEBdVdSKTU8VqtvMXppmZGjG9knmVK1fo-rGRLXnvDN2e29LVo5_-uNtaA02KDtF2frcOLBwFSchoXBsuqzbcjUaaHgM9TJfcZZINIJVzH6h3Lv6P6jiBQ0_njXP2qFMvm0VsnLcOYJkr946NedbmNm1TGdWtPKaA3W_egMImnqP4vh2BXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbda7bde91.mp4?token=RvDN5wq-uPBX3xhwrHVrjoMRzJNNXsQGgbn6uOsa7XqJdWZuTEM23G23ps4A8zVr_9I9vEuu35W8Ma-gw0jO-KC7xxUXy3Yrqu6Z14ZgwDmcoWNe9VaoK7_3yLmVZ2qqoZA34W7-XiUTQbGRr5-Ft8_VQIs0OIJ1mAmzEBdVdSKTU8VqtvMXppmZGjG9knmVK1fo-rGRLXnvDN2e29LVo5_-uNtaA02KDtF2frcOLBwFSchoXBsuqzbcjUaaHgM9TJfcZZINIJVzH6h3Lv6P6jiBQ0_njXP2qFMvm0VsnLcOYJkr946NedbmNm1TGdWtPKaA3W_egMImnqP4vh2BXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری
: آیا مجتبی خامنه‌ای زنده است؟
نتانیاهو: فکر می‌کنم او زنده است.
@WarRoom</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/19457" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کلیسای جامع ملی واشنگتن اعلام کرد مراسم یادبود سناتور لیندزی گراهام در ۲۸ ژوئیه(۶مرداد) برگزار می‌شود. این مراسم با حضور خانواده، دوستان، همکاران سیاسی و رهبران ملی برای بزرگداشت زندگی و چند دهه خدمت عمومی او برگزار خواهد شد. دونالد ترامپ نیز در این مراسم سخنرانی می‌کند و از نقش گراهام در سیاست خارجی، امور دفاعی و حزب جمهوری‌خواه یاد خواهد کرد. جزئیات بیشتر درباره دیگر شرکت‌کنندگان و برنامه مراسم بعداً اعلام می‌شود.
@WarRoom
یاشار : بی بی هم حتما میره !</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/19456" target="_blank">📅 18:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سپاه: دیگر اجازه نمی‌دهیم آمریکا با آتش‌بس‌های فریبنده، ذخایر نفت و مهمات خود را جایگزین و پس‌از آن مجدداً حملات را از سر بگیرد.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 99.8K · <a href="https://t.me/withyashar/19455" target="_blank">📅 18:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">خبرنگار زن : آیا روسیه به ایران در هدف قرار دادن نیروهای آمریکایی کمک می‌کند؟
لاوروف، وزیر امور خارجه روسیه: مدل موهات قشنگه!
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/19454" target="_blank">📅 18:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رویترز : ایران این ماه چند تا از فرمانده‌های سپاه و تجهیزات مربوط به موشک رو که با هزینه خودش خریداری کرده ،برای حوثی‌های یمن فرستاده! به ارزش بالغ بر 20 میلیارد دلار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19453" target="_blank">📅 17:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46d0627615.mp4?token=tKfV14FiW_c5C90BilkR4hU7IRtKBnpE2ZZBZIm3Bq_bEySL1lBUNfzJBhmlqkU93J02wr-UJlI3A5iAA-oge5Z4KAF0UM2pk3vRQvma8iPTkV2bkrUfrwjLPEoRViJ34zg-fxws8I82XGkvcUd4Lz3zJ63Wuc6kFR0_yjU6xR7wqeHWr-7r2d3sjJEv64HhgqSFvWLBKNQSkaQ0UMwHOIZxPRRsHzdIOmWT-FsI2h-kmnwMZloy24QzQzE2p6st081EXRsyUgUv7aHrp0Zckikp6BIZZJhaH1fbGnFUqEs0e6yKCnIPe2SSEReJPnfkFoUB1Xz2NGMFFylYqcHueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46d0627615.mp4?token=tKfV14FiW_c5C90BilkR4hU7IRtKBnpE2ZZBZIm3Bq_bEySL1lBUNfzJBhmlqkU93J02wr-UJlI3A5iAA-oge5Z4KAF0UM2pk3vRQvma8iPTkV2bkrUfrwjLPEoRViJ34zg-fxws8I82XGkvcUd4Lz3zJ63Wuc6kFR0_yjU6xR7wqeHWr-7r2d3sjJEv64HhgqSFvWLBKNQSkaQ0UMwHOIZxPRRsHzdIOmWT-FsI2h-kmnwMZloy24QzQzE2p6st081EXRsyUgUv7aHrp0Zckikp6BIZZJhaH1fbGnFUqEs0e6yKCnIPe2SSEReJPnfkFoUB1Xz2NGMFFylYqcHueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی پیش انفجاری عظیم در جنوب لبنان منطقه کفار تبنیت  توسط حمله جدید نیروهای اسرائیلی انجام شد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19452" target="_blank">📅 17:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تایمز اسرائیل : بانک اهداف کاملا بروز شده
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19451" target="_blank">📅 17:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بیانیه شماره ۴۶ گروه تروریستی سپاه : ارتش متجاوز آمریکا که در تجاوزات خود بعد از شروع رسمی مجدد جنگ از پرتاب موشک های کروز از شناورهای خود در اقیانوس هند بهره می‌گرفت، با پایان یافتن ذخایر موشکی ناوهای مذکور، روز گذشته به استفاده از هواپیماهای B1 با پرواز…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19450" target="_blank">📅 17:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عراقچی راهی قرقیزستان شد
عراقچی در راس هياتی سیاسی امروز به منظور شركت در اجلاس وزرای امور خارجه كشورهای عضو سازمان همكاری شانگهای عازم قرقيزستان شد.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/19449" target="_blank">📅 17:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بیانیه شماره ۴۶ گروه تروریستی سپاه : ارتش متجاوز آمریکا که در تجاوزات خود بعد از شروع رسمی مجدد جنگ از پرتاب موشک های کروز از شناورهای خود در اقیانوس هند بهره می‌گرفت، با پایان یافتن ذخایر موشکی ناوهای مذکور، روز گذشته به استفاده از هواپیماهای B1 با پرواز از پایگاه هوایی فیرفورد انگلیس روی آورد.
هر پایگاهی که برای تجاوز به خاک ایران استفاده شود، هدف مشروع ما است.
به رژیم پادشاهی انگلیس که عامل اصلی بدبختی های مردم منطقه ما بوده و سوابق سیاه تجزیه کشورهای اسلامی، کشتارهای گسترده در این کشورها، تحمیل دولت های استبدادی و بدتر از همه سازماندهی هدایت عملیات اشغال فلسطین و تشکیل نکبت اسرائیل را در پرونده خود دارد و بیشترین مشارکت را در تجاوزات اخیر آمریکا و رژیم صهیونیستی ایران داشته، هشدار میدهیم بیش از این پرونده خود را سنگین نکند.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19448" target="_blank">📅 17:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏دفتر نتانیاهو: پیوستن عربستان سعودی به پیمان ابراهیم جهشی تاریخی برای صلح خاورمیانه خواهد بود,  اقدام نظامی مشترک آمریکا و اسرائیل علیه رژیم تهران و درهم شکستن محور ترور جمهوری اسلامی، زمینه گسترش دایره صلح را فراهم کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/19447" target="_blank">📅 17:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19446">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYUkJh7tNBq9RrlhExbMWHcE4NvkAhVlLABKNoxwAJy8_pPE6JnJikV_goKOqQDv0DX08BYJH4PPWs7mGsu9Sf0c3zZOfsV5XuwxV39VABLyxpXSfm040k8KgQdTr2GDV8Ju6bnVnBDGgGZhz2B75gqwPYfK0fjUaQumrUxJK6i4vVPmho9O4IfIS-zQMcvt4PELJIOG_HoDtaM0YGZDiuMPQXHty6Gj-LWgabjA33gS7Hnk2TWkdCB3lpNlH9pyTymb5CajRSoRGFCW8owo8Mji3b_4cW7WGBnWM5fU2K3LH_OYTSYajEYLC-g1-yf0NXWZuEoE6TjsoitXbPJwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت از ۱۰۰$ عبور کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/19446" target="_blank">📅 16:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19445">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ در‌تروث : اگه حوثی ها دوباره به کشتی ای حمله کنند، ایران را مسئول خواهم دانست
یک سال پیش، ایالات متحده آمریکا به طور جدی به حوثی‌ها به دلیل دخالت آن‌ها در تجارت و بازرگانی، با شلیک به کشتی‌ها، حمله کرد.
از آن زمان و در طول درگیری ما با ایران، آن‌ها به طور مسئولانه عمل کرده‌اند. متاسفانه، اکنون آن‌ها دوباره این کار را شروع کرده‌اند و شب گذشته به دو کشتی سعودی شلیک کردند.
لطفاً این حقیقت را در نظر بگیرید که اگر آن‌ها این کار را دوباره تکرار کنند، ایالات متحده ایران را مسئول خواهد دانست، زیرا حوثی‌ها یک ابزار و/یا نماینده ایران هستند، و مجازات‌های نظامی جدی بر ایران و البته خود حوثی‌ها تحمیل خواهد شد. من از عملکرد آن‌ها بسیار ناامید هستم، زیرا آن‌ها تا به حال به طور حرفه‌ای و هوشمندانه عمل کرده‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/19445" target="_blank">📅 15:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19444">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">فرانسه کارکنان سفارت خود در تهران را تخلیه کرد
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19444" target="_blank">📅 15:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19443">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNqFmDrgYcu3h5d1qj2FgiKQu_l-poBWyEITPrma_eNCshsR6jIoBODzUSSex6P54s4R32WWRe6y3-2tKJNk9F9K9BWkJPCWVr_sF3jNn2CtWy2iRdHOi8Ttjo4BqlEcWe9RCZ8MErs8Y9fDCTeNbPsd8Uv6BG8-rrGEjBc53894gy1mceOUGrbRA8pk9SGI4pYsNqwV9QSi_AT5vg7Lxj_eyeUgBeAOq3ydpSU4XtlrceHbjB1ZOGicLCZEC_Q968jzB86qH5PiVcMSv6_BIcnFF2xno8ZuGgO6NxhiogvgpKOJb7oOZhdBIW7cpaMH2LKKYx9lE28-HUYXPh8Fww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : توافق هسته‌ای غیرنظامی (هیچ‌گونه غنی‌سازی مواد در کار نخواهد بود!) که میان وزارت انرژی ایالات متحده و عربستان سعودی در حال تنظیم است و صرفاً به استفاده‌های غیرنظامی، مانند برنامه‌هایی که ایران، امارات متحده عربی (و کشورهای دیگر) از قبل دارند، مربوط می‌شود، تأیید خواهد شد؛ اما این تأیید کاملاً مشروط به پیوستن عربستان سعودی به توافق‌نامه‌های بسیار معتبر و موفق ابراهیم است.
ایالات متحده با تأسیسات هسته‌ای غیرنظامی (بدون غنی‌سازی) مخالفتی ندارد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19443" target="_blank">📅 15:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19442">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">متأسفانه امروز صبح خواهران دوقلو رومینا رحیمی و  ترانه رحیمی اعدام شدن @WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19442" target="_blank">📅 15:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19440">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dk7g0jx6e_qRk_6rMgLS26AI1Zu5XRR0tuoqVKoM9f7UmRKeeclVb-ZlO01QGN56T1GRWHrzh6AUddPHSOUVEylOYgUZun2mxmI72jEmr1ECJisSoJ5ZH2EaYNGc2A8Rwj-qrzWrSDmz0dw3vvfC-9sNm3-iIY1aCML8tEI-oRB6g3wF9zybmfdEwq1Gt60v-OR1QRG1ZB7-dt-sM-3mLbrCdVQhhOGnKx7H1-A9Vl29JfGJvFmZS2fvjd7Ca0WWnqrV-MpLeCRmxEPcA-E1nCpL1BDYY4gcs6oBhxn2jQ835yfhwyKHSZM0yPsSq5mRY5psFPgDK7s-gzuaYdgUqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85c6b93d2.mp4?token=vVS6LODRbZKmoJuxiJKYA5Vn0ygs9-upzqa1OaCA6s-oeiM0WwbR5eD_jOXH7GDlIlP4uFHZKfKZ88VhUiaFHUouXy82cvqCihT0Y8z-fnaVm92LMaOOvYxp1CsqVrCv7Dc6gvrlDjzVSaBAP0S6QPQlJPSDrXqTX04sXYEjSnNjc4QvIogH0JQKPufifHNlXrRnvfLTTK6J8hBs0sfuKEXyCh9LlglQCdApYel1qoYv9n8vE5wPu6Ej-_bqvO3Mh30tSvo907K8xN_QQrtM86zljs5qIPxFfHhdxAA9sWVtHU9Jpl5N5c2rs-cbvpnTIHCZTQFvNYFVhIneJT5fJ1JYTNovKUN6TJYvX-fbZv8JtIzxNJuPoJy2juVW9NLuYCJAgyQq7LWfjKgUIdESU3R6oZzA9Yd8bpZbHIIU1iffDiA_zqcrXg1tGvUj_D07QgGa07aJW91SqiO456XC5Mv0Ps-F92vCVhXKvVDmxZgeYa1xRrr8ecDfZKRtJdbLMTOry6pS6iuwWcztedQRA36hHSKfD85DL_1fRUwtC3J0pNyWaitCd2iWEDXvU6Wjt-xJ__9T3u8lasXi8gxXrF-HH1AL8ztxeflj5o7Yg_r8Sw95eiweBKj-0VuqSu8cDTsTd5hzjQ9cyJiA3nUfihZDps7eRmhUBTDcDDWjlaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85c6b93d2.mp4?token=vVS6LODRbZKmoJuxiJKYA5Vn0ygs9-upzqa1OaCA6s-oeiM0WwbR5eD_jOXH7GDlIlP4uFHZKfKZ88VhUiaFHUouXy82cvqCihT0Y8z-fnaVm92LMaOOvYxp1CsqVrCv7Dc6gvrlDjzVSaBAP0S6QPQlJPSDrXqTX04sXYEjSnNjc4QvIogH0JQKPufifHNlXrRnvfLTTK6J8hBs0sfuKEXyCh9LlglQCdApYel1qoYv9n8vE5wPu6Ej-_bqvO3Mh30tSvo907K8xN_QQrtM86zljs5qIPxFfHhdxAA9sWVtHU9Jpl5N5c2rs-cbvpnTIHCZTQFvNYFVhIneJT5fJ1JYTNovKUN6TJYvX-fbZv8JtIzxNJuPoJy2juVW9NLuYCJAgyQq7LWfjKgUIdESU3R6oZzA9Yd8bpZbHIIU1iffDiA_zqcrXg1tGvUj_D07QgGa07aJW91SqiO456XC5Mv0Ps-F92vCVhXKvVDmxZgeYa1xRrr8ecDfZKRtJdbLMTOry6pS6iuwWcztedQRA36hHSKfD85DL_1fRUwtC3J0pNyWaitCd2iWEDXvU6Wjt-xJ__9T3u8lasXi8gxXrF-HH1AL8ztxeflj5o7Yg_r8Sw95eiweBKj-0VuqSu8cDTsTd5hzjQ9cyJiA3nUfihZDps7eRmhUBTDcDDWjlaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو فروند هواپیما جنگ الکترونیک آمریکا،مدلEA-37B CompassCalI II ساعاتی پیش در مسیر خود به سمت خاورمیانه به فرودگاه RAF Fairford بریتانیا رسیدند.
تا کنون فقط پنج فروند از این مدل ساخته و تحویل شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19440" target="_blank">📅 14:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19439">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">قیمت نفت خام برنت به ۹۹ دلار به ازای هر بشکه رسید.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19439" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19438">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فاکس نیوز : ایران متوجه شده است امریکا شنبه و یکشنبه که بازار جهانی تعطیل است را برای جنگ انتخاب میکنند‌ و ایران مابقی هفته را برای فشار به بازار جهانی
نفت که در حال رسیدن به ۱۰۰ دلار است
پاییز غرب زودتر فرا میرسد و جهان نیازمند سوخت
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19438" target="_blank">📅 13:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19437">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خبرگزاری هاآرتص : در اسرائیل خود را برای احتمال حمله از سوی ایران در شنبه و یکشنبه آماده می‌کنند
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19437" target="_blank">📅 13:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19436">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">روبیو: ایران توسط روحانیون تندرو اداره می‌شود «اگر آنها پولشان را صرف مردم و اقتصادشان می‌کردند، امروز ایران احتمالاً ثروتمندترین کشور منطقه بود.» عراقچی می‌گوید سیاست آنها چشم در برابر چشم است. سیاست ترامپ سر در برابر چشم است.  اگر وضعیت با ایران به همین…</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19436" target="_blank">📅 12:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19435">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قیمت قراردادهای آتی گاز در اروپا به ۶۴ یورو نزدیک شده و از بالاترین سطح خود در زمان جنگ در منطقه هم فراتر رفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19435" target="_blank">📅 12:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19434">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هم اکنون آژیر حمله پهپادی/موشکی در بحرین
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19434" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">روزنامه maariv : شهردار رمت گن در اسرائیل دستور بازگشایی پناهگاه‌های شهری را صادر کرد:
«احتمال شلیک موشک از سوی ایران در پایان هفته افزایش یافته است.»
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19433" target="_blank">📅 12:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یک اسکادران جنگنده پنهانکار F-35 با عبور از اقیانوس، توسط دو سوختستان استقبال و کمی دیگر در انگلستان به فرود میآیند. یکی از آنها، احتمالا به علت نقص فنی یا برای نشان دادن خود به جهان و تمرین ، آلارم فرود اضطراری روشن کرده است. @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19432" target="_blank">📅 12:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19430">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35bc0c2eb1.mp4?token=ZzixWHlLVFnMmh0N2diz-0YapDn_f0i7P_hk6AGo5LmLI03WNXMBXbpGSmlr7iEoNXcVN531-ZHrC0avW_SYJ3Ri4yOhlgreH9WK5ol7vbspT45nBb90tVrNpWqhATB-X_0Ny-VWsdBO3Yal1kUSSSF0gcYFRIE5tGZpZHAUKhf1GMB8d9_y_MAO4L4YlaDX7Pzm9A7RuF64x33cZk0Kuj8rYldQyCIQTiWUeYvYac1AcBsNXJQcXB7wQ4hkt3nzeATiJqfxQXHE-3w_gRFp1N8QHP1IinqOPEY8GI0oh_DJa2heT0Nd3615fc1UBBHnLzviXJLYpTDTHYx1Dw0zDasrvh7wTM4wB6UXN6S5lZ2yw31YE5LnZSxoWCxIcygGIvnQfrAscPUrZXlQu0G_228O-5fy3CXLCuHq_P-_j3VZ1jzFtBDx9ewyOF8LwLsp8uXt9ELV1_sPSrQk2MpwRMKOHvgbIDdtLhIyema0GEgjsOsYhoWQ8IHsdx7AWWbo8uDa-W4h_OyL4Z3MFGgBuQmUYe7y0dLswX-CvjE4q1HX6GpgTk11y6BGn62KEfdv5_7YNbj4g0Fmvbl4B_3cflczQIGlWq4HqtNX5QyX11hmwzYoGjx3gYUG-v0KKpe5YlOIhUNQ5auSTADH4rXEwoZzClwQPPziuG-HbX-u8fI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35bc0c2eb1.mp4?token=ZzixWHlLVFnMmh0N2diz-0YapDn_f0i7P_hk6AGo5LmLI03WNXMBXbpGSmlr7iEoNXcVN531-ZHrC0avW_SYJ3Ri4yOhlgreH9WK5ol7vbspT45nBb90tVrNpWqhATB-X_0Ny-VWsdBO3Yal1kUSSSF0gcYFRIE5tGZpZHAUKhf1GMB8d9_y_MAO4L4YlaDX7Pzm9A7RuF64x33cZk0Kuj8rYldQyCIQTiWUeYvYac1AcBsNXJQcXB7wQ4hkt3nzeATiJqfxQXHE-3w_gRFp1N8QHP1IinqOPEY8GI0oh_DJa2heT0Nd3615fc1UBBHnLzviXJLYpTDTHYx1Dw0zDasrvh7wTM4wB6UXN6S5lZ2yw31YE5LnZSxoWCxIcygGIvnQfrAscPUrZXlQu0G_228O-5fy3CXLCuHq_P-_j3VZ1jzFtBDx9ewyOF8LwLsp8uXt9ELV1_sPSrQk2MpwRMKOHvgbIDdtLhIyema0GEgjsOsYhoWQ8IHsdx7AWWbo8uDa-W4h_OyL4Z3MFGgBuQmUYe7y0dLswX-CvjE4q1HX6GpgTk11y6BGn62KEfdv5_7YNbj4g0Fmvbl4B_3cflczQIGlWq4HqtNX5QyX11hmwzYoGjx3gYUG-v0KKpe5YlOIhUNQ5auSTADH4rXEwoZzClwQPPziuG-HbX-u8fI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو: ایران توسط روحانیون تندرو اداره می‌شود
«اگر آنها پولشان را صرف مردم و اقتصادشان می‌کردند، امروز ایران احتمالاً ثروتمندترین کشور منطقه بود.»
عراقچی می‌گوید سیاست آنها چشم در برابر چشم است. سیاست ترامپ سر در برابر چشم است.
اگر وضعیت با ایران به همین منوال ادامه یابد، آن‌ها بهای سنگینی خواهند پرداخت.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19430" target="_blank">📅 12:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19429">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وزارت خارجه آمریکا برای سومین بار پیام هشدار صادر کرد:
تنش در خاورمیانه بالا است، خطر تشدید ناگهانی وجود دارد.شهروندان آمریکایی احتیاط بیشتری داشته باشن
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19429" target="_blank">📅 12:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19428">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a1de54c5.mp4?token=JYjGVJJ3h7SErqAltTpiQ1C6A5rXLffPeyHmCpU3ChxRH6FzO-txpHo6UbYhjZp1Jq1HzRWk9HTrSWn_pu4k-0TzWtoiGS-cqOWOkQfWBxl5zue0nW5RpQTSFytMk4sBj2jCRNi85BwwdNBPBldvNzkmZSv6-BuAS7J8cWF_SmcZiV67OVzq5Zuz5liAPfhZuohbJTviVebz-pwPvo13yXF_FcUSGWIs2hipYqIEVdB0gS0oOdtVcHeVe4TB6HrZpzQWBMu5mX-GRv0Ibtw8FWy0pm_UwC5P03KW53svRC23a4a_AJHguyrCz2pGsft0wMetE92T3ed3WbvqFuC4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a1de54c5.mp4?token=JYjGVJJ3h7SErqAltTpiQ1C6A5rXLffPeyHmCpU3ChxRH6FzO-txpHo6UbYhjZp1Jq1HzRWk9HTrSWn_pu4k-0TzWtoiGS-cqOWOkQfWBxl5zue0nW5RpQTSFytMk4sBj2jCRNi85BwwdNBPBldvNzkmZSv6-BuAS7J8cWF_SmcZiV67OVzq5Zuz5liAPfhZuohbJTviVebz-pwPvo13yXF_FcUSGWIs2hipYqIEVdB0gS0oOdtVcHeVe4TB6HrZpzQWBMu5mX-GRv0Ibtw8FWy0pm_UwC5P03KW53svRC23a4a_AJHguyrCz2pGsft0wMetE92T3ed3WbvqFuC4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله صبح امروز به منطقه دوم دریایی ولایت نیروی دریایی ارتش در جاسک ، جنوب شرقی ایران
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19428" target="_blank">📅 12:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19427">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">صداوسیما:دقایقی پیش صدای چند انفجار در کنارک شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19427" target="_blank">📅 11:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19426">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏رویترز: آمریکا در حال اعزام نیروهای تقویتی به خاورمیانه است
‏خبرگزاری رویترز گزارش داد پس از تهدیدهای گروه تروریستی حوثی جمهوری اسلامی، آمریکا در حال اعزام نیروهای نظامی تقویتی به خاورمیانه و گسترش گزینه‌های نظامی خود در منطقه است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19426" target="_blank">📅 11:28 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر امور خارجه آمریکا، روبیو : ایران در حال حاضر آمادگی لازم برای انعقاد توافقی با ما را ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19425" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=S4SxAHBR9ByhM8UqLEfL632NOhTmhbUJPFjS5JL9yoSa6kwXPpDLtCeserNnChRTd2sCEXUSFekhIibH09xd-T36fyA_8OXlMuUFHD3ajik8TCj4jU4p4cCRBteHdcoTJW8H9-EnHArw-5cBjev1y7QeztA5bo0AevCR7JIGL_VmrkgYdpDfUdjq9Up04LUPJI-zc5ZI8WmZC90aXkpLgn4XcWLB3U3kZlB-IWzwDtxVflqTUZk-lgJG8edlKvPWuE8qFI7PR8oDKpm5QJ6gWJa4YvhMVRvsSuyFsla_udQAz5zT9LK6YYtfLelnkEL5plhwP5-n39-gtCM5dMq7xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3405b1189d.mp4?token=S4SxAHBR9ByhM8UqLEfL632NOhTmhbUJPFjS5JL9yoSa6kwXPpDLtCeserNnChRTd2sCEXUSFekhIibH09xd-T36fyA_8OXlMuUFHD3ajik8TCj4jU4p4cCRBteHdcoTJW8H9-EnHArw-5cBjev1y7QeztA5bo0AevCR7JIGL_VmrkgYdpDfUdjq9Up04LUPJI-zc5ZI8WmZC90aXkpLgn4XcWLB3U3kZlB-IWzwDtxVflqTUZk-lgJG8edlKvPWuE8qFI7PR8oDKpm5QJ6gWJa4YvhMVRvsSuyFsla_udQAz5zT9LK6YYtfLelnkEL5plhwP5-n39-gtCM5dMq7xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان  @WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19424" target="_blank">📅 11:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19423">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نفت ۹۸$
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19423" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19422">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">گزارش انفجار ‌در ‌قطر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19422" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19421">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Urk-pRYPeRI6aFtLShKHlMDq-pvzUV0Rcq4yIy6h2nbIhnLjtAJc9-tAtItD37VfLRwy7hSWStfxXK08aJqYc16VLuEZlXuYTxjY3NUzr9_-VYzQSJdBSDDKyPf3NQvBvjTXLOdTYniF1KQNTaP_xorLsbJ4cSXhqzdNFKaj-W06TdGKYYsmwFKlSBqya4pp0eT0MLgaHFFVlvW1oYekgqRYjCbe5EE63CkVmjlkm_DeOb1vcdpmBCDWPPaNy2IrFPcsNR74P9IXm114M4v-y3976ACp5sbhKAw6EARmkbIN6_nkwcuIt2cJzxBNNFaMxH2NnHwEpwPBl1xBUo4IXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب ۲ موشک با صدای مهیب از خرم آباد لرستان
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19421" target="_blank">📅 11:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19420">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">معاون امنیتی استاندار بوشهر: شهر دشتی سه بار مورد حمله آمریکا قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19420" target="_blank">📅 10:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19418">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آلارم اتاق جنگ : فردا شب از نزدیکی منطقه های حساس نظامی ، تونل و پل های مهم که مسیر عبور تجهیزات نظامی هستند عبور نکنید !
⚠️
⚠️
⚠️
@WarRoom
یاشار : فردا شب ویسکی و آبجو میکس
🤒
⚔️</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19418" target="_blank">📅 10:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19417">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Aq7sb7HCDCAcUxFjOKYQpqeQ9RcV4QRto14RHJQkfBNAqcD5znuyKOfqA449rKqz70XCMHSYUiVAqgUx6WcT-WZ2Ry93Vl8zXXX4tGBE_wEPZgzZ0pdbVYQGPKHh6KZT3lX8r8AOXSFCty4AOLQvGJd3ud498Gg1CSKpba6zE0yO5_yb1J1xHKpn_zb9-5TCIRArpt1gEt7HkkPbAK2jl9N07VJ8En-hdLqyqFiWTUfyaoZcmyY_ccwxlr_D0a_LIHsIepimEiRxWonxptq-b5vU0Lt5By_VONMOuoq7_KQvrzNXIbDCZi0-fBewSP1iP1RZYwgEoVuvR4RcAezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همانطور که در پست اینستاگرام (اتاق جنگ دروازههای جهنم) نشان دادم، هواپیماهایی که دیشب از آمریکا حرکت کرده بودند همکنون روی اروپا و نزدیک به خاورمیانه هستند.
فعالیت هواپیماهای ترابری نظامی C-17 و C-5M نیروی هوایی ایالات متحده در مسیر بین اروپا و خاورمیانه، به سطحی افزایش یافته که مدت‌هاست مشابه آن مشاهده نشده است.
منتظر یک جنگ تمام عیار باشید. دروازهها باز شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19417" target="_blank">📅 10:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBxqh6ss5aqCj0zBRSvqyCfUoZ8_M98wKvP37jmvQA3zwNBQn6xMnDhnLfHKu-hhDHShLJwlaoVUdrWXqgzwZOyKGOgACh6FMDi69w0o48fbvM4t2ky-jLOzx7j1oa9FGP_7m-aEXxrxyasCJDC13FEMz3QaKnJAx8Rup-S6MjlFAvPSa4lEIrYzD-pcF7FA8i1YO7Kl8N1fz9MMXrozvZpwsHGh4NB7dzvNQMy9qwUvf84Tsy1Rd7rgi2m8HFTImhgsPXvKtgL9sxkUBZC_MQlsD59Br2VBekQtMQ3_MzFOhEdf2IRcmTMuw-aJCabrm20gglDBHqCtXXZ7vwkOAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متأسفانه امروز صبح خواهران دوقلو رومینا رحیمی و  ترانه رحیمی اعدام شدن
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19415" target="_blank">📅 10:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOudGEW5NhF47akn5c5I7J_CgeMd0eA6U6tsFR1_rkdg58Goz-07lpXqDiA1hxlA_YNUDPL2o1xdnbbB1THIWLNWfRmwSFpUHL8_GxYNYSDhpC9LP-newa_gf5wT2N1fbs1Hj-_Q6SNYHsAC4tZOxf6q9qXlp3p5YOCux0W1dUS6uductrulSe4Qnm8G1W-2JUyQ3zDsDASPN0Kc4fvbugIlKIYgKdn-K6HIHj6tB7paO--fv21RBG4_99E5Wj8RmVeK6COoPxOcIphYcnmpIjgCIdgNuz5ssgDhmSPB7mjhV2mVHn73e4hxmL8R82_XGQkMgrKjHW-mMWiuEM36Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موج جدید موشکی سپاه : هم اکنون پرتاب دو موشک از خمین
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19414" target="_blank">📅 10:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7LTyAvUJR0c8VwuA3JzXaa6GKj8G-P9pjoXva8R-jlaMrok0fn00dOY-h1j8vvT8w8sMHsR1fXE0XsgGMr3wQ2y4Ma_xRYxCQJekFyWC6w1jfEL75c2mwoNQzItYfuvUy_zzE1SgI7ca4obQtbbbcyoU42_1raCpizI9bravMpgbIboTpi3MYI-_5_1-m_szzL-euAg-tCe7u1rRnNoK48ZRBUHhmuTXb9ob1MyfwBUm2_O8-Y2VF9DdrQ1i1mR5sT6fmFf8QF2vomcyrU79bio8uD9DjNGSJLu37ALTHjSSb-kjQ3z6HMG0peu4dZATrmwni-3FU5BhTXB6_riBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏مجله معروف ایتالیایی "اسپرسو" با نشر مقاله اخیر خود، اذعان داشت:
‏دیگر نمیشود به محمدرضا شاه پهلوی گفت «آخرین شاه ایران»
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19413" target="_blank">📅 10:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بامداد امروز، در پی حمله آمریکا، نقطه‌ای در شهرستان کیار هدف حمله هوایی قرار گرفت.
عبدالعلی ارژنگ معاون سیاسی، امنیتی و اجتماعی استاندار چهارمحال و بختیاری با تأیید این خبر اظهار کرد: این حمله در ساعات اولیه بامداد امروز رخ داده و دستگاه‌های مسئول بلافاصله در محل حاضر شده و اقدامات لازم برای بررسی ابعاد حادثه و ارزیابی خسارات احتمالی را آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19412" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران: من آن را یک درگیری می‌نامم. ما با جمهوری اسلامی ایران درگیری داریم. آنها آنقدر ضربه می‌خورند تا معامله کنند، اما من می‌گویم که آنها آماده معامله نیستند. آنها آماهده نیستند چون بعد زیرش میزنند. اما خیلی زود آماده خواهند شد. @WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19411" target="_blank">📅 10:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کنگره آمریکا نسخه خود از قانون بودجه امنیت ملی سال مالی 2027 (NDAA) را تصویب کرد که شامل بندهایی برای افزایش همکاری‌های امنیتی بین ایالات متحده و اسرائیل است.
این بودجه، بیش از 750 میلیون دلار را به برنامه‌های همکاری‌های امنیتی بین دو کشور اختصاص می‌دهد، که حدود 65 میلیون دلار بیشتر از سال گذشته است، و همچنین شامل طرح‌هایی برای گسترش همکاری‌ها در زمینه فناوری‌های امنیتی می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19410" target="_blank">📅 10:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=W5ldXbELBEZg7eoJmfa4Jv93cFvZBFZmmcl2fdIfW-7QiU4dQ90Q8cOyLhtcPIPnpBAEO0vJ_AJEqXty04mVjt-EO2meT-l2kLLd9e4qo1_EFKkys5ievCQ6K_BawLDU1AKL2D7v37VWR40DQWBtcnhn1_iQ8ZDK4-9ngfsSx77JZJ7j3SvR_snw8KD4HVj6F1H0AsGLIBx7Iqa7UxhYtrVmwJj4QqcS1Ub1qu_u-6-VcFdVc0Fe3FeUkmNJjp8sLbUVxqxxuJl0RHXGjv9yq-YQyh2LDagwb6XA728AdceE7cca-PMXWQRAea8l6rkSLt0aAXVuBTJkIiFEtUY-RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a1f97fe0f.mp4?token=W5ldXbELBEZg7eoJmfa4Jv93cFvZBFZmmcl2fdIfW-7QiU4dQ90Q8cOyLhtcPIPnpBAEO0vJ_AJEqXty04mVjt-EO2meT-l2kLLd9e4qo1_EFKkys5ievCQ6K_BawLDU1AKL2D7v37VWR40DQWBtcnhn1_iQ8ZDK4-9ngfsSx77JZJ7j3SvR_snw8KD4HVj6F1H0AsGLIBx7Iqa7UxhYtrVmwJj4QqcS1Ub1qu_u-6-VcFdVc0Fe3FeUkmNJjp8sLbUVxqxxuJl0RHXGjv9yq-YQyh2LDagwb6XA728AdceE7cca-PMXWQRAea8l6rkSLt0aAXVuBTJkIiFEtUY-RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یه دلقکی اینجوری پشت ترامپ ادا شو درمیآورد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19409" target="_blank">📅 09:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19408">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptmfKyS3uCANQ-WcwjwZvdsZvnho4bdnBYDGoCkFoUXYM021NUVIMcIy7aq5G-MKda3YepPcohWoCzB8ICNgLZF_KKroYfozfLEpdvnLdUBetFCChJchw0amm2lAikNIdYetLsCl-JzDl2wAqU-nUz5M8iPHEsaHwLQHvc4VwR1koll26V_j5JlhT0kVA30-Rfi6r02tA7OGT3S5xhzhjk7rMZub7ocdciiJ-UJCPSg5hMrJbjshL54LfyKAgdT09r7eTZLISQMR966t0i18ZQcO_cYBNFfFFMgVlDfDam0VIIc11QT_fRvSFyvWXc40JSZe6sGrR1jgi-fuwtzD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏گزارش‌ها حاکی از آن است که بامداد امروز دو شناور جستجو و نجات دریایی «ناجی ۱۵» و «ناجی ۱۶» در حمله نیروی دریایی آمریکا هدف قرار گرفته و آسیب‌های سنگینی دیده‌اند. بر اساس گزارش‌های اولیه، احتمال غرق شدن هر دو شناور وجود دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19408" target="_blank">📅 09:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19407">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-PxDWuhjB0V52LUDWwsTtOSG5egVK0XdQY2x4n5ron-7R_HlSXUA6giHNvAqO2h5SwwuywDf2CFOwjivLI6H9xzz6O-DvDmC2wFWDwsiPlI-tHV_bxCZb9oqmXxbfwfe1UPukjEp6gCpywMGbu_GhKGU0Vge1FNWuzCz5GDFZnBIosjQfr0Gt9RQyX7P2v1JF3Xq37JhyEnl44DlIssAyUlIPZY-ll3lopYKrAoZGLqJpJOSTMas132mux9Tnmryex0OahJToWM1UM04igTuQSo-p-IsstaD5y2gjPP_6JoRxOgsiBfZ7hRTRNF-zn0vu7M2n66BteAo_fxHReDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان، با توجه به سوالات شما، حضور رادان ساعاتی قبل از حمله در شلمچه تایید شده است. ولی این که آیا هدف ترور بوده و کشته شده یا نه، هنوز مشخص نیست. در لحظه که خبری به دستم برسد، شما را در جریان خواهم قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19407" target="_blank">📅 09:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19406">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لیست نهایی شهر هایی که دیشب مورد حملات آمریکا قرار گرفته‌اند
💥
شلمچه
💥
سیریک
💥
رامشیر
💥
بندرعباس
💥
بندر جاسک
💥
بوشهر
💥
اهواز
💥
بندر ماهشهر
💥
اندیمشک
💥
اسلام آباد غرب
💥
ابهر
💥
کرمانشاه
دوازدهمین شب و کشیده شدن حملات به غرب کشور
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19406" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19405">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گروه حوثی‌های یمن امروز پنج‌شنبه اعلام کردند دو نفتکش متعلق به عربستان سعودی را که در حال عبور از دریای سرخ بودند، با موشک و پهپاد هدف قرار داده‌اند. ساعاتی بعد، عربستان نیز اصابت پرتابه به یکی از این کشتی‌ها را تایید کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19405" target="_blank">📅 08:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19404">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">گزارش CNN: یک مامور سازمان اطلاعاتی از تیم امنیتی معاون رئیس‌جمهور، جی-دی ونس، به دلیل افشای اطلاعات به رسانه‌ها، از سمت خود معلق شد.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/19404" target="_blank">📅 08:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19402">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=IAWCf99vTDtKfiUyskjtVMzTRvxBC4SRHuwMlwOCL8b1bEXOVA1X-HQscR1sucpkbFg2eaVaKafk0rbDbO9IGxs0-C42BR3dZIM7YNgVSZZpcqFlt9mEpBqYXBiAC8UXcqPFPi4lNj8GsZk1R-nCD_G2qXtINlSnktxdqEDJNNSgfFC8jSrP_qHCo7gNej6PTxHq4zaXB-r4xS911G7yBznhD6pdiK0FBRhr0TajbSuQNktGHbTawF4SZo_xP709tudApmOhxeVWDRRmKfq0mLOWJXoCVz1BvZitT7BpvjKBU0BepacPyIlFXHx_hC3rPLKEZpBbS8ROWL04HjlT3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a54a3c2c.mp4?token=IAWCf99vTDtKfiUyskjtVMzTRvxBC4SRHuwMlwOCL8b1bEXOVA1X-HQscR1sucpkbFg2eaVaKafk0rbDbO9IGxs0-C42BR3dZIM7YNgVSZZpcqFlt9mEpBqYXBiAC8UXcqPFPi4lNj8GsZk1R-nCD_G2qXtINlSnktxdqEDJNNSgfFC8jSrP_qHCo7gNej6PTxHq4zaXB-r4xS911G7yBznhD6pdiK0FBRhr0TajbSuQNktGHbTawF4SZo_xP709tudApmOhxeVWDRRmKfq0mLOWJXoCVz1BvZitT7BpvjKBU0BepacPyIlFXHx_hC3rPLKEZpBbS8ROWL04HjlT3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برج راداری گذرگاه مرزی شلمچه
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19402" target="_blank">📅 07:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19401">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKBcukiXtvK9aASzUlJjkAXlj5VdfEPlWgr6V0oGYxQGPXu-bH63-JKR-maUGl4WiT8w55wm3QLtaAO6amsiPuqvwb3zo4gV47ERFrDiVh6OSeaVf98wQwbLgLesGA9M8aInxsM_ob2MXp42iohrABLYsApDiykpWyyT_Z-oEGA6LfJ8Ar94RZB4lx5eZPaOOvB1yyUJXFcXyiOr6mDQMUswb_4Knn6MGHGYuEmMJI846YX7BtyTnSZQVzmp7Pv7THxyQLXVUIRFdWeB3ltc28f2jzifTCWLtvbYwcFuJudnRsKIeZt3IUruzsPu68HEyNhyO9p5bDhPWTJE-AqV3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: بمب‌افکن دوربرد بی ۱ آمریکا مواضع سپاه پاسداران را هدف قرار داد
‏اکسیوس به نقل از مقام‌های آمریکایی گزارش داد یک بمب‌افکن بی ۱ نیروی هوایی آمریکا روز سه‌شنبه با پرواز از پایگاهی در بریتانیا، اهدافی متعلق به گروه تروریستی سپاه پاسداران در ایران را بمباران کرده است. این نخستین استفاده آمریکا از بی ۱ از زمان ازسرگیری درگیری‌ها در ۱۲ روز گذشته است. این بمب‌افکن فراصوت توان حمل ۲۴ بمب ۹۰۰ کیلوگرمی یا ده‌ها موشک کروز را دارد و از بیشترین ظرفیت حمل مهمات در میان بمب‌افکن‌های آمریکایی برخوردار است. مقام‌های آمریکایی و اسرائیلی می‌گویند هم‌زمان با تقویت حضور نظامی آمریکا در منطقه، پرزیدنت ترامپ در حال بررسی آغاز دوباره عملیات گسترده علیه رژیم تروریستی جمهوری اسلامی طی روزهای آینده است.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19401" target="_blank">📅 07:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19400">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">معاون استانداری خوزستان:
در حمله موشکی آمریکا به گذرگاه مرزی شلمچه تاکنون دو نفر شهید و ۱۱ نفر مجروح شده‌اند
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19400" target="_blank">📅 07:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19399">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bf35d9766.mp4?token=tSU9KxUw_kwl7RzPbKyfhAH3esLrHV4czyK_89K2j2RBxO5KzsPY5tjJOYrygJ7Ks_psTdHq0rr6b2-vGl-VOo5m1lhCIu7QPHbDdmdcATGW95Cl228h0k43lBBBz7i-WeVJXpK3e64p-x2AfxBucaHMoH1xWV6ZZomw50URgT1GtcUfwg19ZbOfZOp8naVH9grGSjAh_JHL98O0A-W9UomOUiqyghuyTIvsf4-v5AxfQznM2n89jmFIvowYjlFWuZuZHBVTlfuIII4dniExqsk8iF_OS1INRWGbRpczjN676FRq5M-fpZS4t33sDyX_ZwV7CtHlwD2rhsa1uuZkLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bf35d9766.mp4?token=tSU9KxUw_kwl7RzPbKyfhAH3esLrHV4czyK_89K2j2RBxO5KzsPY5tjJOYrygJ7Ks_psTdHq0rr6b2-vGl-VOo5m1lhCIu7QPHbDdmdcATGW95Cl228h0k43lBBBz7i-WeVJXpK3e64p-x2AfxBucaHMoH1xWV6ZZomw50URgT1GtcUfwg19ZbOfZOp8naVH9grGSjAh_JHL98O0A-W9UomOUiqyghuyTIvsf4-v5AxfQznM2n89jmFIvowYjlFWuZuZHBVTlfuIII4dniExqsk8iF_OS1INRWGbRpczjN676FRq5M-fpZS4t33sDyX_ZwV7CtHlwD2rhsa1uuZkLIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در ساعت ۱۰:۳۰ شب به وقت شرق آمریکا (۶ صبح به وقت تهران) در ۲۲ ژوئیه، برای دوازدهمین شب پیاپی، دور دیگری از حملات علیه ایران را به پایان رساندند.
@WarRoom</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/19399" target="_blank">📅 07:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19398">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حمله رژیم به کویت و اردن
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/19398" target="_blank">📅 03:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19397">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/19397" target="_blank">📅 02:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19396">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromrebel1</strong></div>
<div class="tg-text">ما رفتیم پشت بوی با یه فلاکس پر چای و سیگار
🤣</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19396" target="_blank">📅 02:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19395">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e59327e2a3.mp4?token=v-156P5Wqcs8sL-K6WWMnJXUHr0UoSOMOkocnHIjjf2XwhmkaVc4P4HZRE2lz-azqnKU5S9pyBvF__WHY_mXAH6Ko9apsjI7m571-grrXlKCywmAwn8lFNmOi8x87KYFpdxhH4s_2BHHHFiNrAFCoi4Ef5-9Jx4V_K0WWfehw-DlivfgPT_oGWuu2m14ptqEW1cv_fE_fuweJb2wV6Ym-HyytyYLkkPsT0wJQzSEYfA7wmnReQkSNX4RI_yQ-r7e7a6L3UW26lnin8myyrSQlgvKb4xBFOOpYh6Gusv8C6EeBVufbo6jwMDROAXT3pRj9VQHepPr5j8R59M3vjFp_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e59327e2a3.mp4?token=v-156P5Wqcs8sL-K6WWMnJXUHr0UoSOMOkocnHIjjf2XwhmkaVc4P4HZRE2lz-azqnKU5S9pyBvF__WHY_mXAH6Ko9apsjI7m571-grrXlKCywmAwn8lFNmOi8x87KYFpdxhH4s_2BHHHFiNrAFCoi4Ef5-9Jx4V_K0WWfehw-DlivfgPT_oGWuu2m14ptqEW1cv_fE_fuweJb2wV6Ym-HyytyYLkkPsT0wJQzSEYfA7wmnReQkSNX4RI_yQ-r7e7a6L3UW26lnin8myyrSQlgvKb4xBFOOpYh6Gusv8C6EeBVufbo6jwMDROAXT3pRj9VQHepPr5j8R59M3vjFp_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان لانچرها خف کرده در تونل آزاد راه اراک خرم آباد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19395" target="_blank">📅 02:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19394">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/19394" target="_blank">📅 02:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19393">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJIw1Hw2H8p60ndxd6CIJ3DP2xXdHVjhdsDkElXz8cV5m7gxWuNIAy9VZFseQ7Ve011Jbss-XixES9PYy9ZItCTFgWvgyQFpKFyY0C4p78H-OZHfkQktgHNaLpPsZTLjwy3ZHo4sNbY-ffzZFcnjEv_UT-GZPV72pZNA-nQS1F0r76nY3XLk5Jjn8EvN_23iM2K3RM33KxtNMGfdy_xfunVrSIu6E5101rGbgR9ZjsHCQdlRhCDr81msMs__TzkleLx0wGnslU8SWod-0hj6p6bjJxnKiqnvFC1SpedmlhXcrQ6PZTks4CGo5efvltaCDz47AJUIUMygZzz2dRt-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌های امشب مبنی بر حملات ایالات متحده به ایران تا این لحظه در مکان‌های زیر منتشر شده است:
💥
پایگاه دریایی زیارت سیریک،
💥
سیریک، استان هرمزگان
💥
رامشیر، استان خوزستان
💥
اهواز، استان خوزستان
💥
بوشهر
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19393" target="_blank">📅 02:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19392">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ادعای وال استریت ژورنال:
ارتش آمریکا در حال اعزام نیرو های عملیات ویژه، پزشک، سلاح و مهمات به خاورمیانه می‌باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19392" target="_blank">📅 02:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19391">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فرماندار شهر بوشهر در ایران: یک نیروگاه برق روز چهارشنبه در نزدیکی نیروگاه هسته‌ای بوشهر، در جنوب این کشور، مورد اصابت موشک قرار گرفت.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/19391" target="_blank">📅 02:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19390">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش انفجار بوشهر جدید
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/19390" target="_blank">📅 01:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19389">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مجلس نمایندگان آمریکا بودجه 95 میلیارد دلاری تامین هزینه جنگ با ایران را با 216 رای موافق و 214 رای مخالف ، تصویب کرد.
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19389" target="_blank">📅 01:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19388">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سنتکام: امروز ساعت 5:30 بعد از ظهر به وقت شرق آمریکا، نیروهای آمریکایی با دستور فرمانده کل، حملات بیشتری رو علیه اهداف نظامی ایران آغاز کردن.  این عملیات با هدف تضعیف بیشتر توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای…</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/19388" target="_blank">📅 01:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19387">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سنتکام: امروز ساعت 5:30 بعد از ظهر به وقت شرق آمریکا، نیروهای آمریکایی با دستور فرمانده کل، حملات بیشتری رو علیه اهداف نظامی ایران آغاز کردن.
این عملیات با هدف تضعیف بیشتر توانایی ایران در تهدید ملوانان غیرنظامی و کشتی‌های تجاری در حال عبور از آب‌های منطقه‌ای انجام میشه.
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19387" target="_blank">📅 01:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19386">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سندی محکم از قرار دادن لانچر کنار اتوبان و یک شرکت دارویی که مردم را  سپر انسانی و در خطر قرار میدهد تا در صورت حمله بگویند که آمریکا شرکتهای داروسازی و مردم را هدف قرار میدهد ، همچنین امروز هم یک ویدیو از هدف قرار گرفتن یک لانچر با پوشش استتار شده قرار دادم…</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/19386" target="_blank">📅 01:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19385">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نفطه زنی لانچر با پوشش کاه و یونجه در اتوبان قم به کاشان @WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19385" target="_blank">📅 01:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19384">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سندی محکم از قرار دادن لانچر کنار اتوبان و یک شرکت دارویی که مردم را  سپر انسانی و در خطر قرار میدهد تا در صورت حمله بگویند که آمریکا شرکتهای داروسازی و مردم را هدف قرار میدهد ، همچنین امروز هم یک ویدیو از هدف قرار گرفتن یک لانچر با پوشش استتار شده قرار دادم که شاهد عینی لانچر را به وضوح دیده بود ولی هدف حمله بعضی افراد قرار گرفتم اکنون این ویدیو سند و محکم است که رژیم این کار را از کنار اتوبانها هم انجام میدهد.
این پست را به تمامی زبانها در همه جا منتشر کنید تا به دست جامعه جهانی برسد.
https://www.instagram.com/reel/DbHEPESRguI/?igsh=ZWJjcW5qdTU0b2xv</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19384" target="_blank">📅 01:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19382">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گزارش انفجار بوشهررررر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19382" target="_blank">📅 00:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19381">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سازمان دریانوردی بریتانیا:
دقایقی پیش یک نفتکش عربستان در نزدیکی این کشور مورد اصابت یک موشک قرار گرفت و آتش سوزی گسترده ای نفتکش را در بر گرفته است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19381" target="_blank">📅 00:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19380">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/19380" target="_blank">📅 00:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19379">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">گزارش انفجار دزفول
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19379" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19378">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پاسگاه سیریک رو زدند
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19378" target="_blank">📅 00:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19377">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kz2Pq6lPs8-PLXbomcicVqnfV0yyFwZvXa_WlrixoLhmWle5Kibp-Y5zy0bPC_qlGuynn1uN_Xd47MRdYGG4kj0rI9azwdI-2xwLzWYGPy3RmCll3iO9-c6Nmv4JAeSuRwAdLMhKRexR6Sq8TS8oZ4paTPct3rkEKA-QBf8Yd-Aahxd1HyEIzyOXL6ARrUJBmRr9Wbe2ijZSMTH4jMeSFCcK_wgEEhiHiC56MC-ovHlUgp9H0Jk7Oy4wWmmQVm8PHz3H2Uiba8xuY3oH5LjM3AjzA8_3d0i3C-q5WIT1hHoXMKlBv633wDzYA7xW0QLyktxyH2Ea8Foqx29lwsjO9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای که امشب مردم ایران منتظرند روی فلایت رادار ببینند.
@WarRoom</div>
<div class="tg-footer">👁️ 173K · <a href="https://t.me/withyashar/19377" target="_blank">📅 00:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19376">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صداوسیما: دقایقی پیش؛ شنیده شدن صدای انفجار در بخش بمانی شهرستان سیریک
همچنین دقایق پیش صدای چند انفجار در اطراف روستای زیارت شهرستان سیریک شنیده شد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/19376" target="_blank">📅 00:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19375">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش انفجار رامشیر خوزستان
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/19375" target="_blank">📅 00:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-19374">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پرواز جنگنده تبریز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/19374" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
