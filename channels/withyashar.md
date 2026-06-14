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
<img src="https://cdn4.telesco.pe/file/ibnf0F9-tf6r2wrUf8JY-Sr5svkjz_sBvxtmdvzkiEQ60wtDTR9u6zqMHOIx_CuPmvZmFNUkBM-IJF4MuSc_TXpNIylZ4WXVQtR7wGJIvTFXrcclxDGLKwjqKpFeQq0ANz0CSR_99UUCysWvTJCJ54zoAbERpwM3NqUuM1FXQmsvKre0OLmXw7yvyaepOv0vht88u3VzddDQ6bfR_Zrw5ywuc3paHMPdrhStciXsYFnGx0bIK706qsP2BekQKI-AEeH323FT6punZ9IOPRYMnesySnv2HQYe2xuXWm0IoE_QPXqjFNg0_vnzPDi_UQAZcaAcVHzxcmXUN19Evyp9kw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 329K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 21:24:35</div>
<hr>

<div class="tg-post" id="msg-14855">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=r5A4CXdfCeT_P8OgKd8_f0M-7Ah9R9lDRjAeKpdlzysfpVqSZgdb_Oovcxjnl-fiVOl65yKW8Gp0yWI10_jQO4USGDtOA4-fXtIKHNjD8Jvsq2g50cm4FpK4kWooSSU1-Fjn6bCt0rkHRjGIpMbfdKfTUzgM898Ev_qG0ZdGGbu4YNBBJ-b6JP-K-TzvsLaxCnZjl9fitFFDadfmXbRsi1CAYIIrBlmTLeaOuCbqRYFmuoVN3g4cd8D5Jj1cyzivh87Tfw87JZ90T4wOyDFlB3nRHIKB6_1aQbj9rkddqlfaUMYVU_fcrkdjtH1_6hX7KpKLLq0rToSLGR0f60iySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb472a4ecd.mp4?token=r5A4CXdfCeT_P8OgKd8_f0M-7Ah9R9lDRjAeKpdlzysfpVqSZgdb_Oovcxjnl-fiVOl65yKW8Gp0yWI10_jQO4USGDtOA4-fXtIKHNjD8Jvsq2g50cm4FpK4kWooSSU1-Fjn6bCt0rkHRjGIpMbfdKfTUzgM898Ev_qG0ZdGGbu4YNBBJ-b6JP-K-TzvsLaxCnZjl9fitFFDadfmXbRsi1CAYIIrBlmTLeaOuCbqRYFmuoVN3g4cd8D5Jj1cyzivh87Tfw87JZ90T4wOyDFlB3nRHIKB6_1aQbj9rkddqlfaUMYVU_fcrkdjtH1_6hX7KpKLLq0rToSLGR0f60iySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پدر و  دختری،  احمد ایراندوست(غول برره)، وسط این هیر و ویر‌…
@withyashar</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/withyashar/14855" target="_blank">📅 21:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14854">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قالیباف : بازی پلیس خوب و پلیس بد قدیمی شده است.
@withyashar</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/withyashar/14854" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14853">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خضریان، نماینده مجلس:
ارتباط واتساپی عراقچی با ویتکاف باید کاملاً قطع شود!
@withyashar</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/14853" target="_blank">📅 21:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14852">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">زیرنویس شبکه خبر :
پاسخ به حمله اسرائیل قطعی است.
@withyashar</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/withyashar/14852" target="_blank">📅 21:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14851">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لارنس نورمن خبرنگار وال استریت ژورنال:
در عرض دو هفته، ترامپ از این موضع که «لبنان از موضوع ایران جداست» به این موضع رسیده که «لبنان مرتبط است اما اسرائیل حق پاسخگویی دارد» و بعد به این موضع که «لبنان مرتبط است ولی من فکر نمی‌کنم اسرائیل حق پاسخگویی داشته باشد چون باید توافق را منعقد کنیم»
@withyashar</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/withyashar/14851" target="_blank">📅 20:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14850">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ادعای ترامپ در گفتگو با اکسیوس:
این توافق به نفع اسرائیل خواهد بود، زیرا مانع از دستیابی ایران به سلاح هسته‌ای شده و این کشور را ملزم به رهاسازی مواد هسته‌ای می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/withyashar/14850" target="_blank">📅 20:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14849">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">یدیعوت آحارونوت: کابینه امنیتی اسرائیل امشب تو یه مکان مخفی تشکیل جلسه میدن
@withyashar</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/withyashar/14849" target="_blank">📅 20:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">https://t.me/withyashar/s/5</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/withyashar/14847" target="_blank">📅 20:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14846">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ به پوتین اعلام کرد توافق پایان جنگ با ایران تقریبا کامل شده. پوتین هم از پیشرفت این موضوع ابراز رضایت کرد
@withyashar</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/14846" target="_blank">📅 20:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14845">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فرمانده قرارگاه خاتم الانبیا: فرزندان ملت در نیروهای مسلح «دست به ماشه» آماده شلیک به قلب دشمن هستند
@withyashar
🚨</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/withyashar/14845" target="_blank">📅 20:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14844">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل توسط جبهه مقاومت قطعی است
@withyashar</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/14844" target="_blank">📅 20:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14843">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
توافق با ایران از راه دور امضا خواهد شد، سپس امضای حضوری آن ممکن است یک هفته بعد در اروپا انجام شود
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/14843" target="_blank">📅 20:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14842">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بن‌گویر خطاب به نتانیاهو: قوی باش، نترس
@withyashar
🥥
🥥</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/withyashar/14842" target="_blank">📅 20:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14841">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ به باراک راوید گفت: چرا بی‌بی (نتانیاهو) باید یک حمله‌ی لعنتی انجام می‌داد؟ من خیلی عصبانی شدم. به او گفتم.
او اصلاً هیچ قضاوت لعنتی ندارد. من این را به او گفتم.
اگر توافق امشب امضا شود، فوراً دستور لغو محاصره دریایی ایران را خواهم داد.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/14841" target="_blank">📅 20:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14840">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ در گفتگو با فاکس نیوز اعلام کرد که از ایران خواهد خواست که به حملات اسرائیل علیه حزب الله پاسخ ندهد. ترامپ همچنین اعلام کرد که توافق با ایران ظرف ۲-۳ ساعت آینده به صورت الکترونیکی امضا خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/14840" target="_blank">📅 19:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14839">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ به کانال ۱۲ اسرائیل: از ایران می‌خوام موشک به اسرائیل شلیک نکنه. این توافق در ساعات آینده امضا خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/14839" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14838">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">صابرین نیوز تایید کرد :
برکناری سعید جلیلی از شعام و جایگزینی باقری کنی با وی
@withyashar
یاشار : پوست اندازی رژیم  ادامه ‌داره</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/withyashar/14838" target="_blank">📅 19:55 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14837">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به باراک راوید از اکسیوس گفت:
قرار بود امروز صبح توافق را امضا کنیم، اما حمله اسرائیل به بیروت آن را به تأخیر انداخت.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14837" target="_blank">📅 19:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14836">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ به آکسیوس : به او گفتم، او هیچ قضاوت درستی ندارد
وی همچنین به ناتانیاهو گفت هیچ حمله دیگری به لبنان انجام ندهد و هشدار داد که این حملات می‌تواند توافق را به خطر بیندازد.
ترامپ می‌گوید از ایران خواهد خواست که در پی حملات اسرائیل به لبنان، با حملات موشکی پاسخ ندهد.
@withyashar</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/14836" target="_blank">📅 19:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14835">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ترامپ: من با نتانیاهو صحبت کردم و بهش گفتم:داری چه غلطی می‌کنی؟
@withyashar
🤣</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14835" target="_blank">📅 19:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14834">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کرملین: پوتین و ترامپ درباره ایران و اوکراین گفتگو کردند
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/14834" target="_blank">📅 19:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14833">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در تماس اخیر با رئیس‌جمهور ترامپ گفت که اسرائیل با عقب‌نشینی کامل از جنوب لبنان، از جمله پنج نقطه‌ای که در حال حاضر توسط نیروهای دفاعی اسرائیل (IDF) در اختیار است، موافقت نخواهد کرد، طبق گزارش معاریو.
نتانیاهو همچنین عقب‌نشینی از خاک سوریه را که اسرائیل از زمان سقوط بشار اسد اشغال کرده است، رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/14833" target="_blank">📅 19:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14832">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شبکه ۱۴
:
ایالات متحده در حال حاضر از طریق واسطه‌های مختلف تلاش می‌کند از هرگونه حمله احتمالی نیروهای نظامی ایران به اسرائیل جلوگیری کند.
@withyashar</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/withyashar/14832" target="_blank">📅 19:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14831">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">باراک اوباما : توافق ترامپ که از ماله من زاقارت تره
باراک اوباما، رییس‌جمهوری پیشین آمریکا، در گفت‌وگو با ای‌بی‌سی نیوز گفت بعید است هر توافقی که میان آمریکا و جمهوری اسلامی حاصل شود، تفاوت چشمگیری با برجام داشته باشد یا نسبت به آن بهبود قابل توجهی محسوب شود.
اوباما با اشاره به برجام گفت این توافق بر محدود کردن برنامه هسته‌ای ایران، تعیین سقف برای غنی‌سازی اورانیوم و پذیرش بازرسی‌های آژانس بین‌المللی انرژی اتمی در ازای رفع بخشی از تحریم‌ها و آزادسازی دارایی‌های مسدودشده ایران استوار بود.
او همچنین ابراز امیدواری کرد بمباران‌ها متوقف شود و مردم عادی دیگر از پیامدهای جنگ رنج نکشند.
رییس‌جمهوری پیشین آمریکا تاکید کرد دیپلماسی را به اقدام نظامی ترجیح می‌دهد و گفت نباید تصور کرد که می‌توان با زور یا بمباران به راه‌حل دست یافت.
اوباما خواستار بررسی کامل گزینه‌های دیپلماتیک شد و گفت توافق‌هایی که همه مشکلات را حل نمی‌کنند اما ۸۰ یا ۹۰ درصد آن‌ها را برطرف می‌کنند، می‌توانند از جنگ جلوگیری کنند.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14831" target="_blank">📅 19:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14830">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رسانه‌های اسرائیلی: شهرداری‌های ایلات، تل‌آویو بزرگ، نتانیا و حیفا پناهگاه‌های عمومی را باز کرده‌اند.»
@withyashar</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/withyashar/14830" target="_blank">📅 18:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14829">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">منابع عربی : امریکا در پیامی به اسرائیل گفته امشب ایران حملات موشکی انجام خواهد داد
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/14829" target="_blank">📅 18:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14828">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1fbuXsikBY6sQ54CRt5zCh-cXtibL164ss5QNSV2UODHmos29M3hmBljZ7wZPpwJWAy9Rsqz_jZN5eyXMlS0jq1zzjmVIqePhWDO7IZrA0h80bu5gLA0b0J7SJMavZuBLWKreFwrehx3R4Zk5WrpRPi-Yk0ekpqryC7xTJWXjSf0Idvib9G_yu0LoXmVke2NfBlyzJbUWDpL9LRFYqyBbXbD2_e_aWBmbmcI2lW1rICfQn2u5wprDD3-hNQODuL1Vm5otySvujlqtlLg12FPmNp3XmCZ5VQz_sH4TWXdPJX80Nl8exFPfG9_ZmamiRlIIKJFTkadNipRHC7gUvl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «حمله امروز صبح به بیروت نباید رخ می‌داد، به‌ویژه در چنین روز مهمی که ما تا این اندازه به دستیابی به یک توافق صلح با ایران نزدیک شده‌ایم. اسرائیل حق دارد از خود در برابر تهدیدها دفاع کند، اما حمله‌ای که در واکنش به آن انجام شد بسیار کوچک و بی‌اهمیت بود؛ هیچ‌کس آسیب ندید، مجروح نشد یا کشته نشد و نباید این روند مهم را مختل کند. ما بسیار به توافقی نزدیک هستیم که صلح را برای منطقه، از جمله لبنان، به ارمغان خواهد آورد و همه طرف‌ها باید از درگیری و تشدید تنش خودداری کنند. نباید هیچ حمله دیگری از سوی اسرائیل در هیچ نقطه‌ای از لبنان انجام شود، اما در عین حال نباید هیچ حمله‌ای از سوی هیچ طرف دیگری، از جمله حزب‌الله، علیه اسرائیل صورت گیرد. این می‌تواند آغاز یک صلح طولانی و زیبا باشد؛ نگذارید این فرصت از بین برود! از توجه شما به این موضوع سپاسگزارم. دونالد جی. ترامپ، رئیس‌جمهور ایالات متحده آمریکا»
@withyashar</div>
<div class="tg-footer">👁️ 87.8K · <a href="https://t.me/withyashar/14828" target="_blank">📅 18:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14827">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">هگست، وزیر جنگ آمریکا:
من انتظار ندارم که حملات اسرائیل به حومه جنوبی بیروت مانع توافق با ایران بشه؛ اگر ایران میخواد این موضوع ادامه پیدا کنه، باید حزب‌الله رو مهار کنه.
@withyashar</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14827" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14826">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/14826" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14825">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromALIREZA</strong></div>
<div class="tg-text">تو ویس گفتی یه سری بزنیم به کانالهی رژیم اسگولا اینو منتشر کردن</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/14825" target="_blank">📅 18:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14824">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlcDyNhTaIpe2kuwQj7Benq0H2c36WFZ80mOxioZFUGe1lFMIzvDhY4W_Y5pGbezoWdXwi74B2lFUz01t6jhwJ21QE7g_U87faDNhC8U6JzScS-_4LiDtjRv4MVMLQuxvJN0q2KGPnRt-4RlhmH8J3Nej1OaPPGdmsEcKrvL9KxqjtRohT-KoWnNTpd74N-HcKgWKJFBkZQd1lBHVcc6HICFX7TVL-vdtaQOJEtAc6Lr84OUHsrLwSZfvhRx6gVIiDAyutHhx1J6DMzbJ5VkwEJa2T7W4g7fKIgOnGBuK6kLUTBN5FMLPDgWPZ4Ohxw6EPur--cDYnIAK7VNrXIbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمی‌پیش ستون دود جنوب‌کرج
@withyashar</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/14824" target="_blank">📅 18:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14823">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1de42f04e.mp4?token=PmY3zlamaTpyerBCGIUsS6fhqWGGOCU_j4DldkGJde_sLxbkZJ58ZmHiyk2qubnwwJlUb25Kent9SYxZ9egiBy9YKIKCTo5jfpznGIaQIpkAi97Qcro6PqW2idREz3gdiunXXSmiEGHs1drfueZm8aUk1fIpfKfErdg6resEhWGf8QFVf07bPHIt8W2BY_NGWIPfT5GM1X09m0DdUJPclSynPYgjpJQ0f5gn2gOH2X2yD2vCVYSO1btQuYqq8o6lZETbsxi6aKnZk2MMBHW9QdAfKB1Ik3pEPS8rlPHtB0tFGW3siWgLPn0E1COV8iRjWbU_1wYqiSf8o1ngaA9VDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1de42f04e.mp4?token=PmY3zlamaTpyerBCGIUsS6fhqWGGOCU_j4DldkGJde_sLxbkZJ58ZmHiyk2qubnwwJlUb25Kent9SYxZ9egiBy9YKIKCTo5jfpznGIaQIpkAi97Qcro6PqW2idREz3gdiunXXSmiEGHs1drfueZm8aUk1fIpfKfErdg6resEhWGf8QFVf07bPHIt8W2BY_NGWIPfT5GM1X09m0DdUJPclSynPYgjpJQ0f5gn2gOH2X2yD2vCVYSO1btQuYqq8o6lZETbsxi6aKnZk2MMBHW9QdAfKB1Ik3pEPS8rlPHtB0tFGW3siWgLPn0E1COV8iRjWbU_1wYqiSf8o1ngaA9VDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 79.5K · <a href="https://t.me/withyashar/14823" target="_blank">📅 18:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14822">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02564fdd83.mp4?token=KaG3wGsWs6bffCncTXR78RaRPDpLepjbgJ1sdgZ2A3tpSN0UASdYntHu1W7B9Uovzlfdl5Jl8KYazS2vKlkRROuVflXz384IwYm1kMxIphhQL40_fNhFTTtRAe_Hocj5537F-tHBWlU1MD9fOpbo4dNN_WdQGYVLcFanM_dxlpr09x6-GN2WC_ledUbjRzuRWGG3BOqIbfZysWyyGbFsVd709fHiPLhHPUIBgf8taNN6Qm9mKpLVeaqvNOdarLYKpBgEGcPgLofQ55glNSSl1ULSHw5zuWdkx9wHPRVn3I47Qjf-kk8pKx8vPgwZJlwZA-j9nnUa6bVbiYNPfoTC_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02564fdd83.mp4?token=KaG3wGsWs6bffCncTXR78RaRPDpLepjbgJ1sdgZ2A3tpSN0UASdYntHu1W7B9Uovzlfdl5Jl8KYazS2vKlkRROuVflXz384IwYm1kMxIphhQL40_fNhFTTtRAe_Hocj5537F-tHBWlU1MD9fOpbo4dNN_WdQGYVLcFanM_dxlpr09x6-GN2WC_ledUbjRzuRWGG3BOqIbfZysWyyGbFsVd709fHiPLhHPUIBgf8taNN6Qm9mKpLVeaqvNOdarLYKpBgEGcPgLofQ55glNSSl1ULSHw5zuWdkx9wHPRVn3I47Qjf-kk8pKx8vPgwZJlwZA-j9nnUa6bVbiYNPfoTC_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای عراقچی‌ شما گوه میخورید
🤣
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/14822" target="_blank">📅 18:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14821">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 82.6K · <a href="https://t.me/withyashar/14821" target="_blank">📅 17:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14820">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتش اسرائیل: آماده شلیک از ایران در ساعات آینده هستیم، در حال حاضر تغییری در دستورالعمل‌ها وجود نداره.
@withyashar</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/withyashar/14820" target="_blank">📅 17:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14819">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">کانال 15 اسرائیل:تمام سامانه های پدافندی در اسرائیل به حالت آماده باش کامل درآمدند و در انتظار پرتاب موشک قریب‌الوقوع از سمت ایران می‌باشند
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/14819" target="_blank">📅 17:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14818">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رئیس ستاد ارتش اسرائیل دستور تشدید عملیات‌های زمینی در جنوب لبنان رو صادر کرده و به نیروهای دفاعی اسرائیل دستور داده که عمیق‌تر به خاک لبنان پیشروی کنند.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14818" target="_blank">📅 17:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14817">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سفیر آمریکا در سازمان ملل متحد:
رئیس جمهور ترامپ و معاونش جی‌دی ونس، کاملاً به امضای توافق امروز متعهد هستن.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14817" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14816">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگر در کار نخواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14816" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14815">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزارت امور خارجه‌اسرائیل در واکنش به تهدیدهای ایران اعلام کرد: “این حکومت طبق معمول دروغ می‌گوید. نماینده ایران، حزب‌الله، همان طرفی است که به اسرائیل حمله کرده است. ما شلیک آتش به سوی خاک خود را تحمل نخواهیم کرد.
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14815" target="_blank">📅 17:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14814">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ بیدار شد
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/14814" target="_blank">📅 17:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14813">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">الحدث: علی الحاج، از فرماندهان ارشد حزب‌الله در حمله به ضاحیه بیروت هدف قرار گرفت. تداوم ضربات سنگین به بدنه فرماندهی گروه‌های نیابتی رژیم ایران در لبنان. @withyashar</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/14813" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14812">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">الحدث: علی الحاج، از فرماندهان ارشد حزب‌الله در حمله به ضاحیه بیروت هدف قرار گرفت.
تداوم ضربات سنگین به بدنه فرماندهی گروه‌های نیابتی رژیم ایران در لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14812" target="_blank">📅 17:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14811">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وب‌سایت اکسیوس گزارش داد ارتش اسرائیل اندکی پیش از حمله به منطقه ضاحیه بیروت، فرماندهی مرکزی آمریکا (سنتکام) را از این عملیات مطلع کرده بود.
ارتش اسرائیل پیش‌تر در بیانیه‌ای اعلام کرد در واکنش به شلیک پرتابه از سوی حزب‌الله به شمال اسرائیل و نقض آتش‌بس از سوی این گروه تحت حمایت جمهوری اسلامی، یکی از مقرهای حزب‌الله را در ضاحیه بیروت به طور دقیق هدف قرار داده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14811" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14810">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الحدث به نقل از منابع:
علی الحاج، فرمانده حزب‌الله، در حمله هوایی اسرائیل به حومه بیروت ترور شد
@withyashar</div>
<div class="tg-footer">👁️ 92.9K · <a href="https://t.me/withyashar/14810" target="_blank">📅 16:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14809">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خبر ترور ‌نعیم قاسم تایید نشده است منتظر تایید هستیم @withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14809" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14808">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال های امنیتی: فرماندهی موشکی هوافضا ایران در حال آماده سازی یک حمله گسترده
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/14808" target="_blank">📅 16:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14807">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">موسوی، سخنگوی پیشین هیات رئیسه مجلس:
هدف حمله امروز اسرائیل به ضاحیه بیروت در روزی که قرار بود توافق امضا بشه، تحقیر جمهوری اسلامی بود.
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14807" target="_blank">📅 16:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14806">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فاکس نیوز به نقل از  دیپلمات شرکت‌کننده در مذاکرات:
حملات امروز بیروت مانع از نهایی شدن توافق شده‌اند
این یک تلاش آشکار اسرائیل برای خراب کردن توافق رئیس‌جمهور و کشاندن مجدد ایالات متحده به جنگ است
@withyashar</div>
<div class="tg-footer">👁️ 90.9K · <a href="https://t.me/withyashar/14806" target="_blank">📅 16:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14805">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsLwKioMWy6RHoRZb4gLFqBlWvREwz95jNtnUiTHmgVnkENVSHBWM52-qi8jMppYhD6IAFpf7_VTbKcIJ47GcIzLSIP7BBb40ggnS3JWVTxOOWDFsE54MGlQxLFX1O45DBSoOc6xRs2FfWkDd7wKDkquj8bJTk7QH3un1OfH_3BymLo2A4nQtkWEjVH1Z3HuO_KYwF_7lgOFVE1SrOtUi4qVqx12BVkf6LGWN_j0iI4jkxmAem9X8RstqAY2VjdGZmlrR0tXmsWHwsxWoLMcqOukrWgr6rX7Jt-efdpwWCagmNfAVRaoHhX6vPAxiqgYXU-rv1MgEqXhk_-JrTboFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بزرگ شطرنچ نتانیاهو اول تصویری از حمله به بیروت رو منتشر کرد و تو پست بعدی تولد ترامپ رو تبریک گفت :
@withyashar
😁</div>
<div class="tg-footer">👁️ 94K · <a href="https://t.me/withyashar/14805" target="_blank">📅 16:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14804">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/14804" target="_blank">📅 16:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14803">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/withyashar/14803" target="_blank">📅 16:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14802">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/14802" target="_blank">📅 16:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14801">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرارگاه خاتم: پاسخ کوبنده میدیم
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14801" target="_blank">📅 16:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14799">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فاکس‌نیوز: یک دیپلمات حاضر در روند مذاکرات گفته حمله اسرائیل به بیروت فعلاً توافقات رو به گره انداخته و به همین خاطر امضای توافق تا این لحظه انجام نشده.
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14799" target="_blank">📅 16:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14798">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبر ترور ‌نعیم قاسم تایید نشده است
منتظر تایید هستیم
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14798" target="_blank">📅 15:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14797">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانال ۱۲ اسرائیل به نقل یه مقام امنیتی: حتی یه موشک از سمت ایران پرتاب بشه، با حمله‌ای گسترده به اونا پاسخ میدیم و آماده هر سناریویی هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14797" target="_blank">📅 15:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14795">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/14795" target="_blank">📅 15:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14794">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرگزاری رسمی اسرائیل: حمله به حومه جنوبی بیروت توسط دو هواپیمای جنگی انجام شد که چهار موشک هدایت‌شونده شلیک کردند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14794" target="_blank">📅 15:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14793">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgVMZYbTfLDihuJAWzFiLToAxEOVQx5hOMk3v2gms76u4FrTCM5-gq6psjBqxYRPqM2bTJCPipmkdaJEAEOtmYdrhtGCTWCLtPpKBMnC4KcpuTCumzJEwiQp8Xs7hAYoaIEpHHF1c9MfrVECPYtInO78iezoztgxjfR6Dkmd3SLg9YSFzivRRb2JowbY1KfUpwL5JpLjM734uapZNNMtvvhwXOU2ta1z17VDzBvvV_y0iMlOPcDOKtIt3uN8Cm-ioKywk6_HsBw6ps7Wd0qULm_poxQT7A16MVjVWpDmdy1iRCzk7YwNFMYSRaYPL8bH0dRp2sO4lV45-zHUYrjnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصفهان دید از ملک شهر الان
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14793" target="_blank">📅 15:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14792">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرنگار صداوسیما: تنگه هرمز طبق اعلام نهاد مدیریت آب‌راه خلیج فارس تا اطلاع بعدی همچنان مسدود است و هیچ کشتی خارجی حق ورود و خروج ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14792" target="_blank">📅 15:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14791">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">العربیه: قطری ها و پاکستانی ها فشار زیادی می‌آورند تا تشدید تنش رخ ندهد!
@withyashar</div>
<div class="tg-footer">👁️ 99K · <a href="https://t.me/withyashar/14791" target="_blank">📅 15:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f830c996b.mp4?token=jnRns7hNBgGb9NEui4WOGUbFG-JQZUp1x1zZx7xSS4V7gkV2YrFCdbaUZaAHdCfUP4Ja8MPbvvTjG0LnyusN2hHimB33IA8wgC8fPAriWcQ-YS5Y93zePUrrLeQZNCluZn_KlQft1uN2gX71qu4OGneGKIxBEWwxdT7yJNIDB_kNVvlmGtv8G0v1ZDpauURkCvO9BhRKMp4q-DRt3K7A_qMaK6XxAj6iGRt3j59GF9gWrZHmJo3aMpa0C143RFDPAQWM_0SCl3317H1LGs7CaXcyHBengyXqrHEBxeHdcQT-ojzJjuQ-9GSSuqk0Ylha9-OnziR0NKuEN0DiD8mE4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f830c996b.mp4?token=jnRns7hNBgGb9NEui4WOGUbFG-JQZUp1x1zZx7xSS4V7gkV2YrFCdbaUZaAHdCfUP4Ja8MPbvvTjG0LnyusN2hHimB33IA8wgC8fPAriWcQ-YS5Y93zePUrrLeQZNCluZn_KlQft1uN2gX71qu4OGneGKIxBEWwxdT7yJNIDB_kNVvlmGtv8G0v1ZDpauURkCvO9BhRKMp4q-DRt3K7A_qMaK6XxAj6iGRt3j59GF9gWrZHmJo3aMpa0C143RFDPAQWM_0SCl3317H1LGs7CaXcyHBengyXqrHEBxeHdcQT-ojzJjuQ-9GSSuqk0Ylha9-OnziR0NKuEN0DiD8mE4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل به فارسی با انتشار این گیف از ظریف نوشت:
هفته خوبی داشته باشید
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14790" target="_blank">📅 15:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">منابع عبری: ارزیابی‌های کنونی در اسرائیل نشان می‌دهد که ایران تعادل را حفظ کرده و به حمله در حومه جنوبی بیروت پاسخ خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14789" target="_blank">📅 15:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مقام اسرائیلی به نیویورک تایمز :
توافق آمریکا و ایران آخر بازی نیست و هنوز ماجرا ادامه داره
ما از آمریکا خواستیم تو محدود کردن عملیات نظامی‌ تو لُبنان دخالت نکنه
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14788" target="_blank">📅 14:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سخنگوی آتش نشانی تهران: دود مشاهده در قسمت شمالی شهر تهران، مربوط به حریق فضای سبز در محدوده ولنجک است.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14787" target="_blank">📅 14:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57768c317.mp4?token=MSmHqAxPE-7AcYBPO1v6Gb_oUNt_EmkuVVRP1P0aATOIyeaNwB6xaz9icUhCp3Pp22cs6o0LUKXWuw_Y3XKcU-VW-B4aqldF6IpLWmO6Wo2neccd9GxPM7fzAD6jN1KPsB1kte-upQjCA5vh3YFu2dZr7Mm4waJfgJq2IMDWUk1LCqQVwltScpuZL6n7hKXEr4_XHz2hlvGh9Sg4p4fcjlX2sBV75LKmrltsSS5sGWL3sc0AuTHTgsEnDFnv0z65GeoNLeskgIpw-yZD1yUA3A3sx0o4682tw31Ua8a7CKs_HZMBxqs2CXH4iJcrZcI-9imFzggUyucaCVsMWxq0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57768c317.mp4?token=MSmHqAxPE-7AcYBPO1v6Gb_oUNt_EmkuVVRP1P0aATOIyeaNwB6xaz9icUhCp3Pp22cs6o0LUKXWuw_Y3XKcU-VW-B4aqldF6IpLWmO6Wo2neccd9GxPM7fzAD6jN1KPsB1kte-upQjCA5vh3YFu2dZr7Mm4waJfgJq2IMDWUk1LCqQVwltScpuZL6n7hKXEr4_XHz2hlvGh9Sg4p4fcjlX2sBV75LKmrltsSS5sGWL3sc0AuTHTgsEnDFnv0z65GeoNLeskgIpw-yZD1yUA3A3sx0o4682tw31Ua8a7CKs_HZMBxqs2CXH4iJcrZcI-9imFzggUyucaCVsMWxq0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل: مرکز فرماندهی حزب‌الله تو ضاحیه بیروت رو زدیم
@withyashar</div>
<div class="tg-footer">👁️ 99.1K · <a href="https://t.me/withyashar/14786" target="_blank">📅 14:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف حمله هوایی در ضاحیه جنوبی، فرمانده ارشد در سیستم ارتباطات حزب‌الله بود
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14785" target="_blank">📅 14:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اتاق جنگ با یاشار : این موج مکزیکی بلند رو مدیون بی بی هستیم
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14784" target="_blank">📅 14:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14783">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسانه های اسرائیلی از اماده باش کامل ارتش اسرائیل برای حمله احتمالی ایران خبر می‌دهند.
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14783" target="_blank">📅 14:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بیانیه نتانیاهو و کاتس: ارتش اسرائیل اهدافی متعلق به حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد
زیرساخت‌های حزب‌الله در ضاحیه جنوبی را با دقت هدف قرار دادیم
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14782" target="_blank">📅 14:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شبکه ۱۴ اسرائیل : ما جشن تولد ترامپ رو امروز تو بیروت جشن گرفتیم!
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/14781" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">پنج ساختمان در بیروت مورد حمله  هدفمند قرار گرفته اند!
@withyashar
🚨</div>
<div class="tg-footer">👁️ 95.9K · <a href="https://t.me/withyashar/14780" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14779">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کانال ۱۲ اسرائیل: هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@withyashar</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/14779" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14778">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اتاق جنگ با یاشار :  سفت بگو یا موسییییییییی
@withyashar</div>
<div class="tg-footer">👁️ 94.9K · <a href="https://t.me/withyashar/14778" target="_blank">📅 14:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14777">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ارتش اسرائیل: حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم
@withyashar</div>
<div class="tg-footer">👁️ 96.9K · <a href="https://t.me/withyashar/14777" target="_blank">📅 14:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14776">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79c0e7c974.mp4?token=XAJ4jT9YRCYA5oRwRdUbTOQPKeDrTIPGHAy1x7R8zCv2AptAg7AhhcT6axHvLV0tgACbK9FG4WjBd43hBi2UlTiFRPJbbWZV0DPbnsDdzMe2YOlVcvzfmTu24M1zuZhOVJaf4-QNdM7oQSM_E31AT2nv9yvz7r9hG1MPsb7Q2VSE2L26CVJ6I45WwLlfbWCtSEuoROXIFvRQqi7Q1Mqn1V0Vfgu5OX91oJHkbMf1Cxz-0iBpdQU1qHo-IYhMn-dfLWy3VPQ_kdy_ACKe7FjiKrUvaM-t3c37YL78N1WJ2BIG_htLMwUWeaD3jBFN5W7CM044bfF-zbgnG6jKbqL7xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79c0e7c974.mp4?token=XAJ4jT9YRCYA5oRwRdUbTOQPKeDrTIPGHAy1x7R8zCv2AptAg7AhhcT6axHvLV0tgACbK9FG4WjBd43hBi2UlTiFRPJbbWZV0DPbnsDdzMe2YOlVcvzfmTu24M1zuZhOVJaf4-QNdM7oQSM_E31AT2nv9yvz7r9hG1MPsb7Q2VSE2L26CVJ6I45WwLlfbWCtSEuoROXIFvRQqi7Q1Mqn1V0Vfgu5OX91oJHkbMf1Cxz-0iBpdQU1qHo-IYhMn-dfLWy3VPQ_kdy_ACKe7FjiKrUvaM-t3c37YL78N1WJ2BIG_htLMwUWeaD3jBFN5W7CM044bfF-zbgnG6jKbqL7xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به بیروت
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/14776" target="_blank">📅 14:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14775">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیانیه مشترک نتانیاهو و کاتز:
ارتش اسرائیل اکنون در پاسخ به شلیک حزب‌الله به سمت اراضی اسرائیل، اهداف متعلق به سازمان حزب‌الله را در بیروت مورد حمله قرار می‌دهد. اسرائیل با شلیک به سمت اراضی‌اش مدارا نخواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 98K · <a href="https://t.me/withyashar/14775" target="_blank">📅 14:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14774">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز: آمریکا موافقت کرده است که ایران اورانیوم غنی‌شده را در داخل خاک ایران رقیق کند
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/14774" target="_blank">📅 13:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14773">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d5bc7f03.mp4?token=R3pbIrs0dFXauZWCeJKHphI_qA594N7GiaZMUAO8Vdfej_4qOUtR5DKVhXwjv_OCjiX1xfAK5SwDvf_AeaSQfxygmWrfruaAep1N8Xi7R1gXfA5rmwt3Gs0mD_KkRvQ_MUdiiPEJjv4uKzcQ212l5ClSSPk1Ttvp7hUnm3R5w8UrlYHINbq8IiosAIe3khSoDKnVRvOhRfjroQrG8Uy-j57gLUYC1_u-8AmeuA82TWFj9E1-NQMRfkPXitj_d_vW1-FQsCQpB8JcLtk-M3nuNYVw0Nj9CkIff1bAM5P3YSNOxkSCjMayZ8rOGSfgPQEuTZ-Mpwj8vS_mnhFzhnSA0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d5bc7f03.mp4?token=R3pbIrs0dFXauZWCeJKHphI_qA594N7GiaZMUAO8Vdfej_4qOUtR5DKVhXwjv_OCjiX1xfAK5SwDvf_AeaSQfxygmWrfruaAep1N8Xi7R1gXfA5rmwt3Gs0mD_KkRvQ_MUdiiPEJjv4uKzcQ212l5ClSSPk1Ttvp7hUnm3R5w8UrlYHINbq8IiosAIe3khSoDKnVRvOhRfjroQrG8Uy-j57gLUYC1_u-8AmeuA82TWFj9E1-NQMRfkPXitj_d_vW1-FQsCQpB8JcLtk-M3nuNYVw0Nj9CkIff1bAM5P3YSNOxkSCjMayZ8rOGSfgPQEuTZ-Mpwj8vS_mnhFzhnSA0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا سیما
: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
!
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14773" target="_blank">📅 13:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14772">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صندوق سرمایه گذاری عمومی قطر اعلام کرده بعد از گلی که دیروز بوعلام خوخی در دقیقه‌ی ۹۵ به سوئیس زد ۳ میلیون دلار به همراه یه رولز رویس فانتوم آخرین مدل به ارزش ۵۵٠ هزار دلار پاداش خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14772" target="_blank">📅 13:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14771">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فرمانده مرزبانی آذربایجان‌غربی اعلام کرد حسین رسولی ستوان سوم نیروهای مرزبانی هنگ مرزی چالدران در جریان درگیری با نیروهای پ.ک.ک كشته شده است. PKK مخفف نام کردی ‌به معنی (Partiya Karkerên Kurdistanê)
«حزب کارگران کردستان»
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/14771" target="_blank">📅 12:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14770">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXYQmF2tfdA0qyYpqkqdXyK5_kDBcVczAqy9PqssPuQmfo2GgskZpRUID0vHO64-t-KxBqtFAIJRfFiQsbge1x49ONTEnw--fdPNPoBAudDzhMaE3FOxa4Lacxwl1A5EbOpuIzjPoNj3whEKQAhtaUiOhCLnkIVGpp9f1GHq8G-A7zTsJ7Vj6n2EqJx3etPAJuBscXecIee56j4QUvm5t_QEqwOMub2Hud8vdNmWtn6pd1pwgvf-xqb3pk1BmN3GaS_KtfQFi9lk8D6KAcT5VpEB0nPvESofjjLCsO0iuvNy7hAURr_cgg5Rryy7IsPnnzgAv6dk-SSsuQC7_xa84A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی‌ها: تا مجتبی خامنه‌ای نیاد جلو دوربین و نگه از خون بابام و خانوادم گذشتم، ما این توافق رو قبول نمیکنیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14770" target="_blank">📅 12:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14769">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">صدای انفجار ناشی از مهمات عمل‌نکرده در غرب تبریز
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/14769" target="_blank">📅 12:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14768">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/14768" target="_blank">📅 12:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14767">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14767" target="_blank">📅 12:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14766">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0048bfa4.mp4?token=b7m_io3_uVJHWPyfx3yaY5HI-QqR2ffIykvwJeM0U0kVtHdHaR8KX6roi1XLAWkCnyE2uW_igXQiqtpt3OCy87RahAmGoGhD0B3tLzJ9MUGP9YAyX4HJ6mArYgW9eR1dgsx2GFH6fW7MpkPU_xudC0mjISFf1j32oTdW8kEMz2uV449AqA74lzsir9nl1tJ6LkBtqzAfr5e--hanModaWpcW2pOHrcOe2b5wxZGueB1ftWxSxG7G7suXTWn3I9Ogt6qKU_yYTX3_dy1RFEFlhzaqm4boFxFHzlZmXjU3t2YfxgvTfI2phATa3kdDJi1YAWtrl-XIWqVjiqR-vCaq9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0048bfa4.mp4?token=b7m_io3_uVJHWPyfx3yaY5HI-QqR2ffIykvwJeM0U0kVtHdHaR8KX6roi1XLAWkCnyE2uW_igXQiqtpt3OCy87RahAmGoGhD0B3tLzJ9MUGP9YAyX4HJ6mArYgW9eR1dgsx2GFH6fW7MpkPU_xudC0mjISFf1j32oTdW8kEMz2uV449AqA74lzsir9nl1tJ6LkBtqzAfr5e--hanModaWpcW2pOHrcOe2b5wxZGueB1ftWxSxG7G7suXTWn3I9Ogt6qKU_yYTX3_dy1RFEFlhzaqm4boFxFHzlZmXjU3t2YfxgvTfI2phATa3kdDJi1YAWtrl-XIWqVjiqR-vCaq9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک کشتی‌ها در تنگه هرمز طی ۲۴ ساعت گذشته که با استفاده از اطلاعات سیستم شناسایی خودکار (AIS)
قابل مشاهده است، نشان می‌دهد که هیچ کشتی‌ای با استفاده از طرح جداسازی ترافیک ایران عبور نکرده است؛ با این حال، چند کشتی از طریق آب‌های عمان در امتداد مسیر امن پروژه آزادی که قبلاً ایجاد شده بود، عبور کرده‌اند.
همچنین مشاهده گشت زنی دو شناور نظامی آمریکایی در تنگه هرمز ، البته نوع این شناورها مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14766" target="_blank">📅 11:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14765">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">منابع مطلع به شبکه «العربیه» : هیئت‌های نمایندگی آمریکا و ایران به منظور امضای نهایی توافق صلح، در یک نشست مجازی (ویدیویی کنفرانس) حضور خواهند یافت. یادداشت تفاهم صلح در جریان این نشست آنلاین با نظارت مستقیم میانجیگرانی از کشورهای پاکستان و قطر با حضور «جی‌دی ونس» (نماینده آمریکا) و «محمدباقر قالیباف» (نماینده ایران) به امضا خواهد رسید. بلافاصله پس از امضای این توافقنامه، محاصره بنادر ایران لغو خواهد شد. از دیگر نکات، بازگشایی تنگه هرمز و صدور مجوز عبور و مرور برای کشتی‌ها بدون نیاز به پرداخت هیچ‌گونه عوارض عبور خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14765" target="_blank">📅 11:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14764">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رسانه‌های کشورهای خلیج فارس: جلسه مجازی نمایندگان آمریکا و ایران با حضور واسطه‌هایی از پاکستان و قطر امروز انجام خواهد شد
در این جلسه مجازی آنلاین، یادداشت تفاهم با حضور ونس و قالیباف دیجیتال امضا خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/14764" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14763">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14763" target="_blank">📅 10:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14762">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">الجزیره: جمهوری اسلامی هنوز تصمیم نهایی خودشو درباره تفاهم‌نامه رو اعلام نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14762" target="_blank">📅 09:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14761">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام بلندپایه در دولت آمریکا: معتقدیم به توافقی عالی و بسیار مستحکم دست یافته‌ایم
ایران تنگه هرمز را بدون دریافت هزینه مجدداً باز خواهد کرد
محاصره آمریکا هم‌زمان با بازگشایی تنگه هرمز لغو خواهد شد.
مرحله بعدی بر عملیات مین‌روبی در تنگه هرمز متمرکز خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14761" target="_blank">📅 09:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14760">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7ce7d92b.mp4?token=Jkb_A20Tet9OKFMrbaPQtm1LGgG90PtHMKLzgliXBfmTYTPyw_uNn7v6_iEFEPovgIHgpeutOFWtW-ac17K3wZqfe9LuBuDlK4k2dqASFeHYCAqn38ZimSqLuyPHFPA0giiIZ4A8Qxks2BMN4OHH4TBDBx1OSl917QXk9m3zOroMWami9-ghdkarINB6Iap0M9C2S_xGDEAisHHP2p7bZkMEx65G0Wxrcgqz2H7proTJTs83ijB-ejXSr0IbEPLsWh_hzq2ewY042FRCPnYKcbJP6zRevcrw8vTHTRNTpGwn3oV5MYgULjW_vLJhLId_ugqxdsjXlcDVMOZiX0gQow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7ce7d92b.mp4?token=Jkb_A20Tet9OKFMrbaPQtm1LGgG90PtHMKLzgliXBfmTYTPyw_uNn7v6_iEFEPovgIHgpeutOFWtW-ac17K3wZqfe9LuBuDlK4k2dqASFeHYCAqn38ZimSqLuyPHFPA0giiIZ4A8Qxks2BMN4OHH4TBDBx1OSl917QXk9m3zOroMWami9-ghdkarINB6Iap0M9C2S_xGDEAisHHP2p7bZkMEx65G0Wxrcgqz2H7proTJTs83ijB-ejXSr0IbEPLsWh_hzq2ewY042FRCPnYKcbJP6zRevcrw8vTHTRNTpGwn3oV5MYgULjW_vLJhLId_ugqxdsjXlcDVMOZiX0gQow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14760" target="_blank">📅 02:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14759">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8785098a7.mp4?token=qgcZQAk2FQRwjBpNvAkR2DClNbBEgOxdzpWrNypBR1JUXR329OpTXwSI5SSD19kddD5Qc78qsfUITcBjE3yaWbMLIyKCDLd7LKTWOpszzS3zYT22EuxTJg3qQMS-psSxRTtqBTUAfME7Ns5d2JhpL4PxS3F0AwCAiFSYIrafePcRXvcFSpNDW8wp9lh4e8nlqxlDRIfPfBYuSj9oJSUJp2MEeEteAmhWm6rE8rCCAZMMFeX6fZGaDzIWL_4JoZr8AxsWV2EhazlYn8fE19fxLvM35j60PVqbAq0dPTZS0Wyxo6FbzdxkvJ0WBwo0g3mLU5E2XUf9XvWyokcL8qXFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8785098a7.mp4?token=qgcZQAk2FQRwjBpNvAkR2DClNbBEgOxdzpWrNypBR1JUXR329OpTXwSI5SSD19kddD5Qc78qsfUITcBjE3yaWbMLIyKCDLd7LKTWOpszzS3zYT22EuxTJg3qQMS-psSxRTtqBTUAfME7Ns5d2JhpL4PxS3F0AwCAiFSYIrafePcRXvcFSpNDW8wp9lh4e8nlqxlDRIfPfBYuSj9oJSUJp2MEeEteAmhWm6rE8rCCAZMMFeX6fZGaDzIWL_4JoZr8AxsWV2EhazlYn8fE19fxLvM35j60PVqbAq0dPTZS0Wyxo6FbzdxkvJ0WBwo0g3mLU5E2XUf9XvWyokcL8qXFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافق دیجیتال فردا
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14759" target="_blank">📅 02:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14758">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دوبار تنگه دعوا شده !
🚨
🤣
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14758" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14757">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قشم صدای انفجار‌
🚨
احتمالا از سمت تنگه
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/14757" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14756">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">عبداللهی، سردبیر خبرگزاری تسنیم:
احتمال توافق نهایی با آمریکا بسیار بسیار ضعیفه؛ باید برای حمله ناگهانی آماده بود.
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14756" target="_blank">📅 00:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14755">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پست جدید کلیک کنید کارای‌ اداریش رو انجام بدید
😁
✌🏾
https://www.instagram.com/reel/DZimqXCxxza/?igsh=Z3lhb2FhYWhlc2Yz
بسیجی‌ در ‌برابر سرکوبگر برنامه امشب خیابان های‌ تهران
🥴
استقبال زیاد باشه بازیشو میسازم
🤣</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14755" target="_blank">📅 00:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14754">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به وای نت:
این یک توافق بد است. هیچ‌کس از آن راضی نیست. آنها می‌فهمند که این برای ما خوب نیست و به منافع اسرائیل آسیب می‌زند.
چیزی که نگران‌کننده است این است که اسرائیل نمی‌تواند تأثیر بگذارد و صدایش شنیده نمی‌شود.
این عمدتاً یک «توافق جام جهانی-جشن‌های ۲۵۰ سالگی تولد ۸۰ سالگی ترامپ» است.
هدف این است که برای همه رویدادهای بزرگ فعلی در آمریکا کمی آرامش بخرد. واقعاً چیزی نیست که دوام بیاورد.
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/14754" target="_blank">📅 00:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14753">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14753" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
