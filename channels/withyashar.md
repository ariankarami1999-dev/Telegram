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
<img src="https://cdn4.telesco.pe/file/BHz2rOn3dNwbhVZO33DX8ri94Fc-n1txl5Va6dOPTB_LGCTp2BMYGuglrR9_R370npXe0YoPVhJ3h7S-Q-ILsymc42LD_o34x6f4HDh4lJkIS2QkS2PWHMvBfshOXvutBiicdb29TVJl87-QR9-11umtpov5LzcZJpfIb-Xp1c7PtXgOVSueLg8qihBlmDDGKEmQaJ0mR970RXyuAAfS9ho7p8b78vN9IJPmNSygaRTDOqH50RhuQbXRGJ8Z7YaqIVg9cyAqFKuj3r6Vc0oxVIijg0G-3_-1Yw0HRpL3UzSUHp6_lF8yzoN4Eha3CaYStRCCrG2-ZN7yVGI3b-elwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 305K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 01:38:00</div>
<hr>

<div class="tg-post" id="msg-14089">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کن کلیپنشتاین، روزنامه‌نگار آمریکایی، مدعی شده اسناد محرمانه‌ای را دیده که نشان می‌دهد بخشی از نیروهای لشکر ۸۲ هوابرد آمریکا در آوریل ۲۰۲۶ به‌طور مخفیانه به اسرائیل اعزام شده‌اند. به ادعای او، این نیروها در چارچوب برنامه‌ریزی مشترک آمریکا و اسرائیل برای سناریوهایی از جمله تصرف جزیره خارگ ایران و ایجاد یک منطقه ساحلی در داخل خاک ایران آماده شده بودند. این ادعا تاکنون از سوی پنتاگون یا دولت آمریکا به‌صورت رسمی تأیید نشده است.
@withyashar</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/withyashar/14089" target="_blank">📅 01:26 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14088">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ به اسکای نیوز:
من فکر نمی کنم اسرائیل به جنگ با ایران بازگردد. همه چیز خیلی خوب پیش می رود.
ایران کاری را که باید انجام دهد انجام می دهد. من فکر نمی کنم این اتفاق بیفتد، اوکی؟
@withyashar</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/withyashar/14088" target="_blank">📅 01:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14087">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">زلزله شدید بندرعباس الان @withyashar</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/14087" target="_blank">📅 01:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14086">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یک منبع جمهوری اسلامی به الجزیره: آمریکا تغییرات غیرقابل قبولی در پیش‌نویس یادداشت تفاهم ایجاد کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/withyashar/14086" target="_blank">📅 00:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14085">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">جنگنده غرب تهران
قشنگ دیده میشد
@withyashar</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/withyashar/14085" target="_blank">📅 00:42 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14084">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">زلزله شدید بندرعباس الان
@withyashar</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/withyashar/14084" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14083">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">صدا جنگنده در آسمان تهران
@withyashar</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/withyashar/14083" target="_blank">📅 00:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14082">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله پهپادی حزب‌الله به اسرائیل
🚨
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/14082" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14081">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش صدای انفجار از‌ دروازه دولت
🚨
@withyashar</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/14081" target="_blank">📅 00:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14080">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش از وقوع انفجار مهیب در محدوده گیشا تهران؛ لرزش شدید ساختمان‌ها و شیشه‌ها.
هجوم شهروندان به خیابان‌ها در پی شنیده شدن صدای انفجار و ایجاد رعب و وحشت.
@withyashar</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/withyashar/14080" target="_blank">📅 00:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14079">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یک پهپاد از لبنان به شمال اسرائیل نفوذ کرد و آژیرها به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/14079" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14078">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">جروزالم پست :  هشدار نفوذ پهپادها گالیلای علیا و جولان (1 مکان). در حال به‌روزرسانی...
وارد اتاق امن شوید و تا اطلاع ثانوی در آن بمانید
@withyashar</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/withyashar/14078" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14077">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArad</strong></div>
<div class="tg-text">گیشا یک صدایی شد پنجره لرزید و مردم چند نفر ریختند بیرون</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/withyashar/14077" target="_blank">📅 00:25 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14076">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمکران</strong></div>
<div class="tg-text">صدای انفجار اومد سیریک ولی دور بود</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/withyashar/14076" target="_blank">📅 00:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14075">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">فکر کنم گیشا رو زدن</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/14075" target="_blank">📅 00:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14074">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر دادگستری لبنان: حزب‌الله باید سلاح خود را به دولت لبنان تحویل دهد تا موضع مذاکراتی ما تقویت شود. مذاکره جایگزینی جز گرداب جنگ‌ها و ویرانی ندارد. جنگ به اشغال شدن بخش بزرگی از جنوب لبنان منجر شده است.
@withyashar</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/14074" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14073">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فارس:
جنگنده‌های اسرائیلی
در  عملیات‌های شب گذشته
بدون ورود به آسمان ایران
و از خارج از مرزهای کشور اقدام به شلیک تسلیحات دورایستا کرده‌اند.
این تغییر الگو نشانه‌ای از افزایش ریسک ورود مستقیم جنگنده‌های دشمن به حریم هوایی ایران بود
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/14073" target="_blank">📅 00:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14072">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">مقام ایرانی به الجزیره: توافق فقط به شرط آزادی دارایی‌های ایران حاصل می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/withyashar/14072" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14071">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یک مقام آمریکایی به Axios گفت:
بی بی برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14071" target="_blank">📅 23:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14070">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">@withyashar
جنگ مخفی</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14070" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14069">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سامانه های پدافندی آمریکا در اقلیم کردستان، عراق در حال فعالیت می‌باشند.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14069" target="_blank">📅 23:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14068">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جنگنده های آمریکایی در شمال عراق به پرواز درآمدند.
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14068" target="_blank">📅 23:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14067">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393b6e499.mp4?token=dEvym4isFW47mwGWlkQFzcZLxl23Mx_NC6E3k1apoQq_zw_XEvum-iHM6fNARV8iGToKepa5nP7rGB-EuW2BDPME9EzjFMBcp69GQvS5btuyMMxYjPVxKHFVbYrovAfwFFBua8wnYn4E85KoeN0A3LCOmQgY19CUDlMecC-yb8tydnMbPQZZgCf0V23asBd0_g1JDNAjW2c2xwSUwB4MdWSLC9TRbj0pxjtBQHUmDlEXebU6kLeoMKJ7mQ69CIjnSx4k4xHDhDOpxFKAaeORLh3d0aFBdgutYNAec50MQbovY3UG5qh3IhgM0VDN6DGePqrKZaRGEyCLJ6os2o5lNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393b6e499.mp4?token=dEvym4isFW47mwGWlkQFzcZLxl23Mx_NC6E3k1apoQq_zw_XEvum-iHM6fNARV8iGToKepa5nP7rGB-EuW2BDPME9EzjFMBcp69GQvS5btuyMMxYjPVxKHFVbYrovAfwFFBua8wnYn4E85KoeN0A3LCOmQgY19CUDlMecC-yb8tydnMbPQZZgCf0V23asBd0_g1JDNAjW2c2xwSUwB4MdWSLC9TRbj0pxjtBQHUmDlEXebU6kLeoMKJ7mQ69CIjnSx4k4xHDhDOpxFKAaeORLh3d0aFBdgutYNAec50MQbovY3UG5qh3IhgM0VDN6DGePqrKZaRGEyCLJ6os2o5lNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از رهگیری موشک یا پهپاد های جمهوری اسلامی توسط امریکا همکنون در عراق
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/14067" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14066">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واقعا یه خبرایی ‌هست
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/14066" target="_blank">📅 23:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14065">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هم اکنون گزارش‌های تایید نشده از عراق، حاکی از حمله پهپادی گسترده ایران به پایگاه‌های آمریکا / کرد ها در شمال عراق است.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/withyashar/14065" target="_blank">📅 23:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هم اکنون گزارش‌های تایید نشده از عراق، حاکی از حمله پهپادی گسترده ایران به پایگاه‌های آمریکا / کرد ها در شمال عراق است.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/14064" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14063">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزارت خارجه آمریکا: آزادی اموال بلوکه شده، مادامی که ایران به تعهدات خود پایبند نشود، رخ نخواهد داد
محاصره دریایی اعمال شده علیه ایران تا دست‌یابی به توافق پابرجا خواهد ماند
@withyashar</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/withyashar/14063" target="_blank">📅 23:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14062">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کاور @withyashar</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/withyashar/14062" target="_blank">📅 22:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14061">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">برم اتاق جنگ رو پست کنم</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/14061" target="_blank">📅 22:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14060">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">استان یزد فردا تعطیل شد
@withyashar</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/14060" target="_blank">📅 21:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14059">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ: جمهوری اسلامی از ما خواست تا اسرائیل حملاتش به ایران را متوقف کند
@withyashar
جمهوری اسلامی هم میگه آمریکا خواست
🤣</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14059" target="_blank">📅 21:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14058">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14058" target="_blank">📅 21:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14057">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14057" target="_blank">📅 21:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14056">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">صدا های مشکوک به انفجار‌ همکنون تهران
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14056" target="_blank">📅 21:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14055">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/14055" target="_blank">📅 21:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14054">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14054" target="_blank">📅 21:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14053">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐥𝐢 🇺🇸𝐬𝐡𝐚𝐤𝐮𝐫</strong></div>
<div class="tg-text">درود سرباز شاه پیام که برای رضا پهلوی (شاهزاده ) فرستادی پاک کنین ، دشمن دنبال همین پیام ها هستن ، همه میدونیم ادمین کسی دیگس</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14053" target="_blank">📅 21:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14052">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14052" target="_blank">📅 21:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14051">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from:)</strong></div>
<div class="tg-text">یاشار دادا فکر کنم اون گز اجیلی که از چهارماه پیش برای روبیو  و ونس بردن تازه داره دعا جادوش  عمل میکنه جنس ایرانیه  دووم  نداره دیر کار شروع میشه زودم تموم میشه
اینا تموم شدن. اینم مثل جنگ ۱۲ روزه یه تست بود که بییین اینا چقدر داستان دارن که فهمیدن فقط بوق کرناس هیچی ندارن
✌🏻
دمتم گرم خسته نباشید
❤️</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/14051" target="_blank">📅 21:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14050">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ به کانال 12 اسرائیل:
به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کنه، اونو تنها خواهم گذاشت.
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14050" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14049">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14049" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14048">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است. @withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14048" target="_blank">📅 20:41 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14047">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/14047" target="_blank">📅 20:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14043">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فرماندهی مرکزی آمریکا (CENTCOM) اعلام کرد نفتکش
Marivex
با پرچم کشور پالائو را در حالی که از آب‌های بین‌المللی دریای عمان
به سمت ایران در حرکت بود
، هدف قرار داده است.
پس از آنکه خدمه کشتی از اجرای دستورات نیروهای آمریکایی خودداری کردند، یک فروند جنگنده
F/A-18 سوپر هورنت
مستقر بر روی ناو هواپیمابر
آبراهام لینکلن (CVN-72)
یک مهمات هدایت‌شونده دقیق را به بخش موتورخانه و سامانه هدایت کشتی شلیک کرد
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14043" target="_blank">📅 20:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14042">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حریم هوایی ایران در حال باز‌ شدن است
@withyashar</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/14042" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14041">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14041" target="_blank">📅 19:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14040">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند. @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14040" target="_blank">📅 19:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14039">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خضریان، عضو کمیسیون امنیت ملی مجلس: حملات موشکی ما تا برقراری آتش‌بس در لبنان ادامه داره
@withyashar</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/14039" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14038">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">نتانیاهو: ایران و حزب‌الله امروز از هر زمان دیگه‌ای ضعیف‌ترن و اسرائیل از همیشه قوی‌تره، اما کارزار ما علیه اون‌ها هنوز تموم نشده. تو 24 ساعت گذشته، ایران و حزب‌الله سعی کردن قواعد جدیدی به ما تحمیل کنن، اما من این موضوع رو نمی‌پذیرم. همون‌طور که سال‌هاست انجام دادم، روی حق اسرائیل برای پاسخ دادن به این حملات پافشاری می‌کنم.
و اگه ایران دوباره اشتباه کنه و حملاتش رو از سر بگیره، با قدرت بهش پاسخ خواهیم داد، اسرائیل حق دفاع از خودش رو داره و این حق رو حفظ خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14038" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14037">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نتانیاهو: همانطور که به دوست خودم ترامپ میگم: ما اسرائیل رو با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت رو به شمال اسرائیل بازخواهیم گرداند.
@withyashar</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/14037" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14036">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو: ایران نمیتونه معادلات رو به ما تحمیل کنه. من این موضع رو تأیید میکنم. پس از اینکه حزب‌الله به اسرائیل شلیک کرد، ما به بیروت حمله کردیم. و پس از اینکه ایران به اسرائیل حمله کرد، ما به مناطق دیگری در ایران حمله کردیم.
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14036" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14035">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نتانیاهو: در حال حاضر آتش در جبهه ایران محصور است، زیرا پس از اینکه رژیم تروریستی در تهران آماده شد، دیگر به ما حمله نکرد. اگر دوباره به ما حمله کند - با قدرت پاسخ خواهیم داد
@withyashar</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/withyashar/14035" target="_blank">📅 18:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14034">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=IFYrxtr_79Kh1tx9dlN_ZzQtMnJs2-vnv358w2GDlqqxZWhEvU_fa2EjeujQICINoWR-g8lfBh_5tNdMsbUDyUdeQfRaiW69VNJ91iqif-NhVghd6UaIG3KCy78_XDa30oDgv-v59wqZ003obGm_SiIvRQVE8-ZDuW3hytzG7c4WZpfmlHcTCuNM9lya5qp-xUKlQwyVe6pE56_fiFJ8yytVvqB-b_mJpb1CQo782p-F_lGekVbp5hOqewJinaC7bft9BTuC3ujqUikiEb-k3zudOb2q_6JL640J3Kq5gDKTtchrWjq6nImu8HxvDyQQO6UjWIs3J-DkPGcmRRyU6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c95feb74.mp4?token=IFYrxtr_79Kh1tx9dlN_ZzQtMnJs2-vnv358w2GDlqqxZWhEvU_fa2EjeujQICINoWR-g8lfBh_5tNdMsbUDyUdeQfRaiW69VNJ91iqif-NhVghd6UaIG3KCy78_XDa30oDgv-v59wqZ003obGm_SiIvRQVE8-ZDuW3hytzG7c4WZpfmlHcTCuNM9lya5qp-xUKlQwyVe6pE56_fiFJ8yytVvqB-b_mJpb1CQo782p-F_lGekVbp5hOqewJinaC7bft9BTuC3ujqUikiEb-k3zudOb2q_6JL640J3Kq5gDKTtchrWjq6nImu8HxvDyQQO6UjWIs3J-DkPGcmRRyU6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اگر رژیم جمهوری اسلامی اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما به شدت پاسخ خواهیم داد، زیرا اسرائیل حق دفاع از خود را دارد و ما این حق را حفظ خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 96.3K · <a href="https://t.me/withyashar/14034" target="_blank">📅 18:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14033">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">رئیس جدید موساد، رومن گوفمن : مردم ایران را مسلح کنید , بازی را تغییر دهید
@withyashar</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/14033" target="_blank">📅 18:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14032">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اسرائیل هیوم: درگیری 24 ساعت اخیر نشان داد قدرت نظامی ایران حتی نزدیک به شرایط قبل از جنگ هم نیست.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14032" target="_blank">📅 18:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قالیباف: معادله آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان رو به هم زدیم. تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14031" target="_blank">📅 18:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14030">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رسانه I24News: اسرائیل به پمپی که مواد را در کارخانه بزرگ پتروشیمی در ایران حمل می‌کند حمله کرد. حمله‌ای به یک قطعه حیاتی (و گران‌قیمت) با هدف از کار انداختن کارخانه‌ها.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14030" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14029">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو دقایقی دیگه صحبت میکنه</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/14029" target="_blank">📅 18:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14028">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">لغو تمام پروازهای کشور تا اطلاع ثانوی
شرکت فرودگاه‌ها و ناوبری هوایی ایران:‌
در پی صدور اطلاعیه رسمی هوانوردی (NOTAM) توسط سازمان هواپیمایی کشوری مبنی بر بسته‌شدن فضای پروازی غرب کشور، تمامی پروازهای فرودگاه‌های سراسر کشور تا اطلاع ثانوی لغو شده و انجام نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14028" target="_blank">📅 16:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14027">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=jpQRtQZsyfoELImtw2-oOrOBdbn0vVqaOVmcOIZsQbI6HJfC7EZSoHWQW74a8MECiOIDGwImRWqZJ9y75sZ4YY1NGnv8Pauv6uqkSPGMAxIZa118vHYV6gbB4IGtOwQowJWAr9L18rP2-wgh8CySYFdoJ4e4vLu19Z4h1iElhkkrLPKW9zkq3cz1ETtcTlC5ucWZ89gVdjjRkEX4trCQBinN8ESX0re_IMVlhxDDgCT-AfchIcc8TLN1VS8GvkjkrgI-L8MBGSL9xSPuHjMwD_2AT3r2DWJxf-Z5EsG7VZwZXVl64ueLkOZPbyRxggip6ZP0hHZNh2I4n2WrJw1NGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906b9a08b0.mp4?token=jpQRtQZsyfoELImtw2-oOrOBdbn0vVqaOVmcOIZsQbI6HJfC7EZSoHWQW74a8MECiOIDGwImRWqZJ9y75sZ4YY1NGnv8Pauv6uqkSPGMAxIZa118vHYV6gbB4IGtOwQowJWAr9L18rP2-wgh8CySYFdoJ4e4vLu19Z4h1iElhkkrLPKW9zkq3cz1ETtcTlC5ucWZ89gVdjjRkEX4trCQBinN8ESX0re_IMVlhxDDgCT-AfchIcc8TLN1VS8GvkjkrgI-L8MBGSL9xSPuHjMwD_2AT3r2DWJxf-Z5EsG7VZwZXVl64ueLkOZPbyRxggip6ZP0hHZNh2I4n2WrJw1NGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خطر
⚠️
اگه ناراحتی قلبی دارید نبینید
🤣
بی اختیاری ادرار میاره
این ویدئو رو صدا و سیما خودشون پخش کرد!
اخطار سرفرماندهی نیروی دریایی جمهوری اسلامی برای تنگه هرکز
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14027" target="_blank">📅 16:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14026">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بریتانیا هشدار تخلیه به شهروندانش از اسراییل رو صادر کرد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14026" target="_blank">📅 16:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14025">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY0WaqQFGvzP5mNtjg88J40reVT9Vbtotgz8t9GczLHY7y-v4qgjw73g5ha5MyiAg6t8sBk0W6SKl3Kmfxboaxz6F99LqnlOsDxKbD5De5CokrsrHSLP-6S3B_kXJK-wANQQwDCS6Lz_MWCkDUKfB8aknEAXasoJ-WUoAIWtjdMdUU8qsv7X90U0wzxyk_D60MaQOPigVAu9cLkUrnhellVV_K3s9LeE0B4YfvkZn8OcpbmIoaJf6l4r9scXdmgxO5kONemlcKZSMIWF5c2tNqEdKb4zsORMzJ33MzMnuao5-6H8pWveaz-VeI_MZA-OhrhMLnVJpxc4S6KxyNQtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل هم داره جنوب لبنان رو خیلی شیک و مجلسی هوایی میزنه.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14025" target="_blank">📅 16:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14024">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14024" target="_blank">📅 16:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14023">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترافیک سنگین در محورهای چالوس و هراز
@withyashar
خوش بگذره به هم وطنام
❤️‍🩹
جای‌منو خالی کنید</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14023" target="_blank">📅 16:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14022">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14022" target="_blank">📅 16:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14021">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vxe2Sklpxtgjgh9Uxp8Pwh8irpk5QnMQyYIRl7lOGaNbXnLe3AHqRcH9y6ZPXrxZ9HlJTXh0WOnMXxL_qLkEi8kvuNeWb06pRM_0Swlwc_Ft8lUkQrMr3_BEimcr3OZBudOvsZwd8Ln5SLpnSnORFuOnMJGfAjBSzZPnKLvtAet0amEREAMGgV9Ud1-hDOFsKVqhVu8TLsvgyfdhxdf3UIaoyIYXyyazmjy70NdtjLmkK7nGXR7v7fw-ZuOYtNKkCnWrCrTYiIm_8RsYgsvvRyhGh6SBRxsRJ71d6AVq1HLIhBTFKp5bpkPSX-df6oqrwbyGf8vna23TvoNX93Ckqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14021" target="_blank">📅 16:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14020">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14020" target="_blank">📅 16:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14019">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حزب‌الله هم حمله موشکی کرد به سمت اسرائیل و آژیرها فعال شد.
اسرائیل : 5 موشک رهگیری شد.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14019" target="_blank">📅 15:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14018">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یک مقام آمریکایی به آکسیوس:
تماس تلفنی ترامپ با نتانیاهو «مودبانه» بوده، اما نتانیاهو با درخواست ترامپ برای توقف اقدامات بیشتر مخالفت کرده.
به نتانیاهو صراحتا گفته شد که این چرخه باید پایان یابد. آمریکا با این حملات موافقت نکرد و از آنها حمایت نکرد.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14018" target="_blank">📅 15:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14017">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عراق از بازگشایی حریم هوایی خود خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14017" target="_blank">📅 15:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14016">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کانال 12 اسرائیل: ترامپ و نتانیاهو دقایقی پیش صحبت کردن.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14016" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14015">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هم اکنون اسرائیل به لبنان حملهِ کرد
@withyashar
😁</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14015" target="_blank">📅 15:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14014">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدا و سیما:جنگ پس از شکست دشمن به پایان رسید و زندگی به روال عادی بازگشت
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14014" target="_blank">📅 15:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14013">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تحلیل کمی دیگه در‌اینستاگرام پست میشه</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14013" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14012">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ به نیوزنیشن: یک جنگ دیگر را پایان دادم
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14012" target="_blank">📅 15:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14011">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=jhUp4Que3338eP_sIQJ7TcdJW0CeJKOZChAPKzKNGlbr81lclLUELh_FQAQyrPneNczahXJ4sOu2P-rAH1dbBjdxeyCHpxSREoKyE82Mkfqp501NIJfstAKG9fnYSnBy2N9kaC_e4m_SJWT-qLcC1S2d2wyc1X-qs7byXO-1wnzrvJlU70rb2lox8bZ7SOdfyCQ2WzF6wox69GzbpZQOiPZjHERJJn06VgjH_EAFZa1XBhYW42it8kd6vzUkRDJLtjzN4TzUafPFSyVs98UoDyylVob5Gtu3WZjgqgk_q4SzoKyt9_5ALsMSQrHJ22emKIbG_6_mx4JgDLuJ-QcuJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=jhUp4Que3338eP_sIQJ7TcdJW0CeJKOZChAPKzKNGlbr81lclLUELh_FQAQyrPneNczahXJ4sOu2P-rAH1dbBjdxeyCHpxSREoKyE82Mkfqp501NIJfstAKG9fnYSnBy2N9kaC_e4m_SJWT-qLcC1S2d2wyc1X-qs7byXO-1wnzrvJlU70rb2lox8bZ7SOdfyCQ2WzF6wox69GzbpZQOiPZjHERJJn06VgjH_EAFZa1XBhYW42it8kd6vzUkRDJLtjzN4TzUafPFSyVs98UoDyylVob5Gtu3WZjgqgk_q4SzoKyt9_5ALsMSQrHJ22emKIbG_6_mx4JgDLuJ-QcuJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14011" target="_blank">📅 15:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14010">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود @withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14010" target="_blank">📅 15:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14009">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌: توقف عملیات نیروهای مسلح اعلام می‌گردد؛ اما در صورت تداوم حملات، از جمله در جنوب لبنان، اقدامات شدیدتر در راه خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14009" target="_blank">📅 14:53 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14008">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اسرائیل هیوم: اسرائیل و ایالات متحده پیامی به ایران ارسال کردن که اگه تهران حمله دیگری انجام نده، هیچ حمله‌ای علیهش نمیشه
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14008" target="_blank">📅 14:52 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14007">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=L5Hzxdxke78df01otaAOyE5do22aFL5v6O_LSkk_d5UxPSLmJ88i8g2DK26mOCkOBgtyHWkT9sHCZuWwHXCyRRHw0Qu2BPU7y6XcccWZJDmLexoxlDFIX5LtMOimfnVsLE-w6Rz_SzdZbei74qZCvj3NB8RoMC53mWZjMvQwJbtkny0lLWDhc2EiE7LIfV2lhDsb6kGpoyMRM0CgU61NwpH1D4kFXOoNcCJUCrRzOdVx2FKyhC6gi9mhnaMoJaGZlOZ2TeUf-nlecWnD2di3f419xD-UDAfoQ_96UmtEgYVD_HVw5sLO-B1tDb1b7rFUQjw56gmvt0egAdwuxHH2FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e67efef8f3.mp4?token=L5Hzxdxke78df01otaAOyE5do22aFL5v6O_LSkk_d5UxPSLmJ88i8g2DK26mOCkOBgtyHWkT9sHCZuWwHXCyRRHw0Qu2BPU7y6XcccWZJDmLexoxlDFIX5LtMOimfnVsLE-w6Rz_SzdZbei74qZCvj3NB8RoMC53mWZjMvQwJbtkny0lLWDhc2EiE7LIfV2lhDsb6kGpoyMRM0CgU61NwpH1D4kFXOoNcCJUCrRzOdVx2FKyhC6gi9mhnaMoJaGZlOZ2TeUf-nlecWnD2di3f419xD-UDAfoQ_96UmtEgYVD_HVw5sLO-B1tDb1b7rFUQjw56gmvt0egAdwuxHH2FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارتش اسرائیل : ما سیستم‌های پدافند هوایی رژیم تروریستی جمهوری اسلامی در غرب و مرکز ایران را نابود کردیم
‏پس از حمله، انفجارهای ثانویه‌ای شناسایی شد که نشان می‌داد موشک‌ها در پرتابگر بوده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14007" target="_blank">📅 14:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14006">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=fQc4F1uK1wYI_momup27ldPyIEb2pfZlaTcsiuqAstPQ-0wzPaicPstedzGs8bnMqgfmrY3cmI4yqwRSi1X5FPTTgHo7zpT4QTw3u1e2yaUD18Hk1Ry3dhKWZulNUqR-K-x_Zi7gEvgDDYCajNJCDfmBKT54mn0Sp57Zcfsebj59p41iXkxIZR5xRbQATqL6IqqxUPMKF7V2g_Z4bXVkHkjJCx9ntov8cnkI5z_kiQDMpqP5Zffj6h9HBhq7lvn2Y4AJ0YbnE972vmo80dpqXJL3bIkTt1SPspPOb1LWwt0VzT3s9Lr11OrGLQAzR-oPP8663o1APHNqm1fAxHCwZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d567e74a89.mp4?token=fQc4F1uK1wYI_momup27ldPyIEb2pfZlaTcsiuqAstPQ-0wzPaicPstedzGs8bnMqgfmrY3cmI4yqwRSi1X5FPTTgHo7zpT4QTw3u1e2yaUD18Hk1Ry3dhKWZulNUqR-K-x_Zi7gEvgDDYCajNJCDfmBKT54mn0Sp57Zcfsebj59p41iXkxIZR5xRbQATqL6IqqxUPMKF7V2g_Z4bXVkHkjJCx9ntov8cnkI5z_kiQDMpqP5Zffj6h9HBhq7lvn2Y4AJ0YbnE972vmo80dpqXJL3bIkTt1SPspPOb1LWwt0VzT3s9Lr11OrGLQAzR-oPP8663o1APHNqm1fAxHCwZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان کرج سمت میدان استاندارد و فردیس
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14006" target="_blank">📅 14:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14005">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسانه های رژیم با ذکر الله اکبر ،  نوشتند تنگه هرمز کامل بسته شد @withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14005" target="_blank">📅 14:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14004">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وزیر آموزش و پرورش اسرائیل: تعطیلی مدارس فردا سه‌شنبه نیز ادامه خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14004" target="_blank">📅 14:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14003">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرنگار I24News خطاب به پست رئیس جمهور ترامپ:
من واقعاً نمی‌دانم این مذاکره درباره چیست
این مذاکرات به مدت یک هفته و نیم به دلیل لجاجت ایرانی‌ها متوقف شده است. پیام‌های ترامپ هر روز خجالت‌آورتر می‌شوند
و تا جایی که می‌دانم، اسرائیل خواستار آتش‌بس فوری نیست
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14003" target="_blank">📅 14:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14001">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JEQ12HL-dydq8Wq_2Rf6Me7vmnHXJPYgLkDRi4WGuoLVq1JQuHNj28hmVt_S108oCEssqfKteyUV_eBrQU-fO786EzWn1PcvtG0nXDyCs5jZweOjmf3KblShwKXEBSXYr4LdYDbIglhlb-JiqF6aVXQCBDm8mLFFYF1o_FNuQrAeDOfA5QLQ2sEy0NcuvxUCaWFQTl2-l11qxtrry0Hj7q6qIqwdvfj0QbHdOJww2RUf-qt5h-p5zs4EndYTBALMeddaKxo7ecxC22l-V0SsAflPWCMOCB7IQF8FBr8z9Y7MkhCWEMWsEExkdq6g3rUX9jjsga22Hin2Zy3tE4J4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: هر دو طرف، اسرائیل و ایران، به دنبال برقراری آتش‌بس فوری هستند!
مذاکرات نهایی درباره «صلح» در حال پیشرفت است، مشروط بر اینکه جهل یا حماقت مانع آن نشود.
محاصره به قوت خود باقی خواهد ماند و با قدرت کامل اجرا می‌شود، تا زمانی که «توافق نهایی» حاصل شود.
اوضاع باید سریع پیش برود. از توجه شما به این موضوع سپاسگزارم!
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14001" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14000">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtoh-14IMrxJGKfE8qcnMW_BF3TgIBpA2xh0FXSU0aGp2CSRmBcjUTN-bu9vuXJu0nFHdjdVszDg422G9VyEQwGYnQDsBoFkjqLORLDy6hoSUGPlJ3rJpUBqlTsxdzs9ZjRpVdSAy_4NbGEc1QcqR8ZwklOs1RQzGTrMCmjBWgHXdqQzOX8Zk8wwLqV_1AGvJcTcLbgPRmtGEbEaozFX7bNjqTw4LuWHSVc6L4qgl-vRa9O6_P2PHLtJ-dV9PGMMy13F0s4fe_hJrAp6xPiI1fO6oBH8t_tI58MpP5u28HjRF_CEogLWP-kSSX8N6uRp36OhMZLs53MyRcRiaCqjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود از انفجار در شیراز، ساعتی پیش
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14000" target="_blank">📅 14:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13999">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رسانه های رژیم : پدافند یزد فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/13999" target="_blank">📅 14:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13998">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=lf0pWIRIOP0M6VIhEFIAPch9mRIaib8WrZqLK9FOZeVE8KBJSWxhCuEF8vUGBtvPMAFb45po09ETJIeBaiB1noQwMcI-kEcshqvE8cCPHgiXmg3s5E9OUo1bs7OEmnP0ACzsy3VWFxtGsNn07BY08UushFCK2vwahhlG40xW-XUofPT-O9XFv0mScc9zM_Q73nqGxE6ZKrHCIdlD_URrB9gLfDRdGXrwXheT1IFBPLrenrQkFndO19YNld4w1LhE4yigXNcwWJaRR5ekX073M-NHTETjgg71T-T0Wxta3Wm-jJLHcDup54X7AIQNXaU9g_cWxCnNrwfQvXOMMBMx5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1b83882f.mp4?token=lf0pWIRIOP0M6VIhEFIAPch9mRIaib8WrZqLK9FOZeVE8KBJSWxhCuEF8vUGBtvPMAFb45po09ETJIeBaiB1noQwMcI-kEcshqvE8cCPHgiXmg3s5E9OUo1bs7OEmnP0ACzsy3VWFxtGsNn07BY08UushFCK2vwahhlG40xW-XUofPT-O9XFv0mScc9zM_Q73nqGxE6ZKrHCIdlD_URrB9gLfDRdGXrwXheT1IFBPLrenrQkFndO19YNld4w1LhE4yigXNcwWJaRR5ekX073M-NHTETjgg71T-T0Wxta3Wm-jJLHcDup54X7AIQNXaU9g_cWxCnNrwfQvXOMMBMx5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از حمله به یک کشتی باری با پرچم پالائو با ۲۴ خدمه هندی در نزدیکی تنگه هرمز ساعتی پیش , بر اساس این گزارش‌ها، در این حمله موتورخانه کشتی هدف قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/13998" target="_blank">📅 14:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13997">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سخنگوی وزارت خارجه چین : پکن به‌شدت نگران وضعیت فعلیه
@withyashar
🥴</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/13997" target="_blank">📅 14:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13996">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کابینه جنگ اسرائیل امشب ساعت 9 به وقت اسرائیل تشکیل جلسه خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13996" target="_blank">📅 13:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13995">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سرپرست سرکنسولگری ایران در کربلا: هماهنگی‌های لازم با عراق جهت انتقال حجاج انجام شده است
@withyashar
حجاجی که نیومده بودن باید برن عراق زمینی‌ بیان</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13995" target="_blank">📅 13:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13994">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یک کشتی هندی در دریای عمان هدف قرار گرفت و دچار آتش‌سوزی شد
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/13994" target="_blank">📅 13:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13993">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034343a08d.mp4?token=d2ZnQc2cVHtuzu5vaV8dSkMYeALBYe9EDYrqIPbEuH7D4iCfIL-ws2_dfeGX3GRJ4nKiSRluszw03qgsCCXTdJ4hh8Lxl5wRBlTSZMCI744Is6X8hbyIp930OvqW709iRdMuQU7D7fIXHVUFu4Id1sOeyXGUjEQ_drFvNysaymdEGWXp8fKVJBMZ-OEiUtyFNaMUg0RVaTsFQHXpwJbXObsMhF25HZITa7OsYuoNYuKHSH_8aXbz-FXwtKeeB2vbavBMu6YGs_u82mpcl6R8pAb5n7lMGX4rU4-RqZT7NOlfSu7efU79THGAVNlon9oWItOquRjq3MG60abezvDMTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034343a08d.mp4?token=d2ZnQc2cVHtuzu5vaV8dSkMYeALBYe9EDYrqIPbEuH7D4iCfIL-ws2_dfeGX3GRJ4nKiSRluszw03qgsCCXTdJ4hh8Lxl5wRBlTSZMCI744Is6X8hbyIp930OvqW709iRdMuQU7D7fIXHVUFu4Id1sOeyXGUjEQ_drFvNysaymdEGWXp8fKVJBMZ-OEiUtyFNaMUg0RVaTsFQHXpwJbXObsMhF25HZITa7OsYuoNYuKHSH_8aXbz-FXwtKeeB2vbavBMu6YGs_u82mpcl6R8pAb5n7lMGX4rU4-RqZT7NOlfSu7efU79THGAVNlon9oWItOquRjq3MG60abezvDMTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش السیسی محموت احمدی‌نژاد
🤣
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13993" target="_blank">📅 13:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13992">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnk9B8F5tGgw_E5F6J8TrLVIu0FjKrZE_P1WqerGGB8HhdUzK5N4fQLDguMREu0XLz-AbAqRmM00UMebtotW9RCkIz1yppRZD-zkjzPIFYBUC5Dn28aYES6XyjONdagbbQDsVQED_rcORQgDAEljH33odNYtraLP-5RGc5R_Bmffp9cgMEULO-_PnHW_8LXM1yyXVzv40aTjr2YH3KVIfD1a4NwQRiO2zpb2O7S3NJvGtFqmKXir1dZiWgxiiXnQ2wUoqO4FA4-nK5WmYG4oAQdRaKs-SYla0e1_li4njRROoi7-QSWVqfz2ULRX6fZYxyLp1aGMFMa8VVIi3Rsbwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله اسرائیل به سایت موشکی تنگه کنشت کرمانشاه
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13992" target="_blank">📅 13:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13991">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یک منبع نظامی به تسنیم: ایران برای جنگ طولانی مدت آماده شده است
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/13991" target="_blank">📅 13:38 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13990">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رسانه های عبری: درگیری ها تا ساعات آینده گسترده و سنگین‌تر خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13990" target="_blank">📅 13:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13989">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنقلات خود را آماده کنید</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/13989" target="_blank">📅 13:36 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13988">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یک منبع ارشد نظامی در ایران: حزب‌الله  روزهای آینده نشان خواهد داد که محاسبات اسرائیلی‌ها و آمریکایی‌ها همیشه اشتباه است، و ایران ثابت کرده که دوستان خود را رها نمی‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/13988" target="_blank">📅 13:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13987">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فارس: تو غرب تهران پهپاد زدیم
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13987" target="_blank">📅 13:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13986">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترامپ با لهجه استانبلی
🤣
:
📿
الله لله</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/13986" target="_blank">📅 13:24 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
