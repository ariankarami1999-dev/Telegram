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
<p>@withyashar • 👥 328K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 13:31:37</div>
<hr>

<div class="tg-post" id="msg-14773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43d5bc7f03.mp4?token=VGvwGg8653WT3d82taBj_dJqgeu-8QdiDj7l4JAGeJ9HvFK74y7_Z0NhUZIgWtNMFrIe51EVSHkImfD9H1fGoI9erdzGNOzqH-UDOuQGDQIxEr2rgfqxSotfwiikMj1doX1kxi2WDjc7Pky6UoPg5DyN80MQFVxDJvTXOhnW2U-2cFL8U7uG1mEgb_yRFjNLwRPAk-kNfW7JF-KSA8dmeO0kq1IFxR4KiQHzgLFuMVv2e2j7uGP7A81zpMGZZ4V4MKWMsdsP7ppPJ3e0ru4jhYczf6HaItgFqo-IrepOVKBC6LfWTfyd6Nj8fWNrdlQwaBgu6L9an0uzBw067CFkMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43d5bc7f03.mp4?token=VGvwGg8653WT3d82taBj_dJqgeu-8QdiDj7l4JAGeJ9HvFK74y7_Z0NhUZIgWtNMFrIe51EVSHkImfD9H1fGoI9erdzGNOzqH-UDOuQGDQIxEr2rgfqxSotfwiikMj1doX1kxi2WDjc7Pky6UoPg5DyN80MQFVxDJvTXOhnW2U-2cFL8U7uG1mEgb_yRFjNLwRPAk-kNfW7JF-KSA8dmeO0kq1IFxR4KiQHzgLFuMVv2e2j7uGP7A81zpMGZZ4V4MKWMsdsP7ppPJ3e0ru4jhYczf6HaItgFqo-IrepOVKBC6LfWTfyd6Nj8fWNrdlQwaBgu6L9an0uzBw067CFkMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا سیما
: پاکستانی‌ها برای میانجی‌گری به ایران نمی‌آیند، بلکه مرتب پیام تهدید و‌ ترور می‌آورند
!
@withyashar</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/withyashar/14773" target="_blank">📅 13:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صندوق سرمایه گذاری عمومی قطر اعلام کرده بعد از گلی که دیروز بوعلام خوخی در دقیقه‌ی ۹۵ به سوئیس زد ۳ میلیون دلار به همراه یه رولز رویس فانتوم آخرین مدل به ارزش ۵۵٠ هزار دلار پاداش خواهد گرفت!
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/14772" target="_blank">📅 13:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14771">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرمانده مرزبانی آذربایجان‌غربی اعلام کرد حسین رسولی ستوان سوم نیروهای مرزبانی هنگ مرزی چالدران در جریان درگیری با نیروهای پ.ک.ک كشته شده است. PKK مخفف نام کردی ‌به معنی (Partiya Karkerên Kurdistanê)
«حزب کارگران کردستان»
@withyashar</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/withyashar/14771" target="_blank">📅 12:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14770">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzxnHO4lGISlFf74QfRnHufDHvkYAQwnUpdBjMTLuYzITuzGe_Vr2Wt_ho6y_EszyC_hCk98YTTCrLpfTlyQCpTvg5_oqMNQC-9S5tT93SssG4YLVrYkS1qGpod9b6YGDNe76prDtW_r1-3kXRwcH_vlVcXSXjFofVePRIqrCBUI-pn6B1PpVj9OE_WTxJIc8LCEunieua697pGCEv0Oe9uGYlmCYTKNWJdOYapsIX3BmvQ-dtgl7ZUvulJppH2hTxImbSDTFCVlku2OPYk4ZHRV9Zqq-XRBI-jiOMONKY7MAMNPdGX7y7HPH8PZV1gtj1o-7aywZQsEMLmFCLCdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی‌ها: تا مجتبی خامنه‌ای نیاد جلو دوربین و نگه از خون بابام و خانوادم گذشتم، ما این توافق رو قبول نمیکنیم
@withyashar
🤣</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/withyashar/14770" target="_blank">📅 12:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14769">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صدای انفجار ناشی از مهمات عمل‌نکرده در غرب تبریز
@withyashar</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/withyashar/14769" target="_blank">📅 12:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14768">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/14768" target="_blank">📅 12:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14767">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/withyashar/14767" target="_blank">📅 12:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14766">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d0048bfa4.mp4?token=k3mEPpgefzJR1ygfdHWClQ56LAXF6CnhcBcklkI3qR0n9EOqZpC_0NVv85XIVsCiRgiHOz3w5Fod3yT07GyPVNTA87lSsjjASLcHs6xV8FENxuGQcA3mSkjtnJevYQNKwcjLj9Gc7YAgUPKhJG0dVaWahsonRtmxPO1VooZnD3gypeo4lmSHl6uNRERl7MtDNdZzBka-ZX_bFqM-4xeJ87u0mgfuyUEG6G_0ZRZmW-UTtyYAi2t184heWZmMKdVuk7FgNEakndJS8dmzP8g7S_itcVdVZXZmBXOy8xUJVCjVDZxGAjjf_SyOcf804RTf55djZ7rE-dumN4Kgq5wv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d0048bfa4.mp4?token=k3mEPpgefzJR1ygfdHWClQ56LAXF6CnhcBcklkI3qR0n9EOqZpC_0NVv85XIVsCiRgiHOz3w5Fod3yT07GyPVNTA87lSsjjASLcHs6xV8FENxuGQcA3mSkjtnJevYQNKwcjLj9Gc7YAgUPKhJG0dVaWahsonRtmxPO1VooZnD3gypeo4lmSHl6uNRERl7MtDNdZzBka-ZX_bFqM-4xeJ87u0mgfuyUEG6G_0ZRZmW-UTtyYAi2t184heWZmMKdVuk7FgNEakndJS8dmzP8g7S_itcVdVZXZmBXOy8xUJVCjVDZxGAjjf_SyOcf804RTf55djZ7rE-dumN4Kgq5wv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترافیک کشتی‌ها در تنگه هرمز طی ۲۴ ساعت گذشته که با استفاده از اطلاعات سیستم شناسایی خودکار (AIS)
قابل مشاهده است، نشان می‌دهد که هیچ کشتی‌ای با استفاده از طرح جداسازی ترافیک ایران عبور نکرده است؛ با این حال، چند کشتی از طریق آب‌های عمان در امتداد مسیر امن پروژه آزادی که قبلاً ایجاد شده بود، عبور کرده‌اند.
همچنین مشاهده گشت زنی دو شناور نظامی آمریکایی در تنگه هرمز ، البته نوع این شناورها مشخص نیست
@withyashar</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/withyashar/14766" target="_blank">📅 11:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14765">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">منابع مطلع به شبکه «العربیه» : هیئت‌های نمایندگی آمریکا و ایران به منظور امضای نهایی توافق صلح، در یک نشست مجازی (ویدیویی کنفرانس) حضور خواهند یافت. یادداشت تفاهم صلح در جریان این نشست آنلاین با نظارت مستقیم میانجیگرانی از کشورهای پاکستان و قطر با حضور «جی‌دی ونس» (نماینده آمریکا) و «محمدباقر قالیباف» (نماینده ایران) به امضا خواهد رسید. بلافاصله پس از امضای این توافقنامه، محاصره بنادر ایران لغو خواهد شد. از دیگر نکات، بازگشایی تنگه هرمز و صدور مجوز عبور و مرور برای کشتی‌ها بدون نیاز به پرداخت هیچ‌گونه عوارض عبور خواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/14765" target="_blank">📅 11:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14764">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رسانه‌های کشورهای خلیج فارس: جلسه مجازی نمایندگان آمریکا و ایران با حضور واسطه‌هایی از پاکستان و قطر امروز انجام خواهد شد
در این جلسه مجازی آنلاین، یادداشت تفاهم با حضور ونس و قالیباف دیجیتال امضا خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/withyashar/14764" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14763">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سی‌ان‌ان: مذاکره‌کنندگان قطری برای نهایی کردن تفاهم راهی تهران شده‌اند
شبکه آمریکایی به نقل از یک منبع مدعی شد که مذاکره‌کنندگان قطری صبح امروز در هماهنگی با ایالات متحده به سوی تهران پرواز کرده‌اند تا به تسهیل روند نهایی‌سازی توافق (یادداشت‌تفاهم) بین ایران و آمریکا کمک کنند
@withyashar</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/14763" target="_blank">📅 10:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14762">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الجزیره: جمهوری اسلامی هنوز تصمیم نهایی خودشو درباره تفاهم‌نامه رو اعلام نکرده.
@withyashar</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/withyashar/14762" target="_blank">📅 09:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14761">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فاکس نیوز به نقل از یک مقام بلندپایه در دولت آمریکا: معتقدیم به توافقی عالی و بسیار مستحکم دست یافته‌ایم
ایران تنگه هرمز را بدون دریافت هزینه مجدداً باز خواهد کرد
محاصره آمریکا هم‌زمان با بازگشایی تنگه هرمز لغو خواهد شد.
مرحله بعدی بر عملیات مین‌روبی در تنگه هرمز متمرکز خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/14761" target="_blank">📅 09:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14760">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7ce7d92b.mp4?token=fcit87iLyjtrQI3JGPKhZe2ofx1NsTIsUG6MPDNeXGeiA3w7sL2cLU5PeFNzBL7mqnYg6fAefi_FNpvZ6S8pUfKTBVlnVTHDOvVh2L7H7kAmdDDV2KnAIRfvMafgsq6ZCEVwciBIunKGz80dT6GLk7uExfG7m2X9JfPiw91FLAnpztVA_YKRTuGR1-g0KSzcv_SkFZcD1T2X50tpfBEEbvF3W5wC7Bf6GvtQWn18wLNbnSQ9WiSkEK5CGl9SklGbCuI_GzmCf7d7KGqWtmEFvVjg75xVc3hELNXkAz3Sb2Wg31vP14aXginvTu5GfGMWXmtjJI4SWTEBsOwpXCM9Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7ce7d92b.mp4?token=fcit87iLyjtrQI3JGPKhZe2ofx1NsTIsUG6MPDNeXGeiA3w7sL2cLU5PeFNzBL7mqnYg6fAefi_FNpvZ6S8pUfKTBVlnVTHDOvVh2L7H7kAmdDDV2KnAIRfvMafgsq6ZCEVwciBIunKGz80dT6GLk7uExfG7m2X9JfPiw91FLAnpztVA_YKRTuGR1-g0KSzcv_SkFZcD1T2X50tpfBEEbvF3W5wC7Bf6GvtQWn18wLNbnSQ9WiSkEK5CGl9SklGbCuI_GzmCf7d7KGqWtmEFvVjg75xVc3hELNXkAz3Sb2Wg31vP14aXginvTu5GfGMWXmtjJI4SWTEBsOwpXCM9Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14760" target="_blank">📅 02:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14759">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8785098a7.mp4?token=Xz1c6oLYL5XEC_qXcYV8VaVLIlCiEBZ4E5-4CinkKyWowafz_ToyYEl0296IWa-RnY6PVN9kbINWrCVuyx3aPhgC4leB06r0PUl2TzDO5DFECrWw-iWwsSkQjfaZJCWrHB62O9ClTmSqtRtSw5RWgjdKSqGfyQFBBxVChIJJ6YrWMIGq_Gc61p94cmlAMY8JJf7yXqcirRGzj2Qq8erVSc3aCRwFIgs4tiJZCDuqagVW0FrxpNbzkMYybxeO9WfW9FrDLV-Xx-KEjM2husUYa35a6-doxeCASPC_pQEgrUIF2eV3wKk4eW1YX2vuc45OkFrw1-UW_Lyy1NQ3VPyPeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8785098a7.mp4?token=Xz1c6oLYL5XEC_qXcYV8VaVLIlCiEBZ4E5-4CinkKyWowafz_ToyYEl0296IWa-RnY6PVN9kbINWrCVuyx3aPhgC4leB06r0PUl2TzDO5DFECrWw-iWwsSkQjfaZJCWrHB62O9ClTmSqtRtSw5RWgjdKSqGfyQFBBxVChIJJ6YrWMIGq_Gc61p94cmlAMY8JJf7yXqcirRGzj2Qq8erVSc3aCRwFIgs4tiJZCDuqagVW0FrxpNbzkMYybxeO9WfW9FrDLV-Xx-KEjM2husUYa35a6-doxeCASPC_pQEgrUIF2eV3wKk4eW1YX2vuc45OkFrw1-UW_Lyy1NQ3VPyPeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توافق دیجیتال فردا
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14759" target="_blank">📅 02:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14758">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دوبار تنگه دعوا شده !
🚨
🤣
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/14758" target="_blank">📅 01:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14757">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قشم صدای انفجار‌
🚨
احتمالا از سمت تنگه
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14757" target="_blank">📅 01:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عبداللهی، سردبیر خبرگزاری تسنیم:
احتمال توافق نهایی با آمریکا بسیار بسیار ضعیفه؛ باید برای حمله ناگهانی آماده بود.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14756" target="_blank">📅 00:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پست جدید کلیک کنید کارای‌ اداریش رو انجام بدید
😁
✌🏾
https://www.instagram.com/reel/DZimqXCxxza/?igsh=Z3lhb2FhYWhlc2Yz
بسیجی‌ در ‌برابر سرکوبگر برنامه امشب خیابان های‌ تهران
🥴
استقبال زیاد باشه بازیشو میسازم
🤣</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14755" target="_blank">📅 00:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به وای نت:
این یک توافق بد است. هیچ‌کس از آن راضی نیست. آنها می‌فهمند که این برای ما خوب نیست و به منافع اسرائیل آسیب می‌زند.
چیزی که نگران‌کننده است این است که اسرائیل نمی‌تواند تأثیر بگذارد و صدایش شنیده نمی‌شود.
این عمدتاً یک «توافق جام جهانی-جشن‌های ۲۵۰ سالگی تولد ۸۰ سالگی ترامپ» است.
هدف این است که برای همه رویدادهای بزرگ فعلی در آمریکا کمی آرامش بخرد. واقعاً چیزی نیست که دوام بیاورد.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14754" target="_blank">📅 00:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14753" target="_blank">📅 00:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتاق فایت با شما : میدون ابن سینا درگیری شده
بین مامورا و تند روهاااا
میدون ابن سینا رو کامل بستن
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14752" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14751" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نبویان: آمریکا پیروز شد
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14750" target="_blank">📅 00:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYcsFMMiQgu7ALIT86QlRM167EmprN8BaMmK-siQLKV6v_nzKwJtlaqUJZz_1R0ZoJdbAr4wGpYcKmlnlHIULVph51w7YLSWzTbNbMCoxjIKEjQmTB2JN-z_SNNBjROXVc7lkx6YMD-7TC-ldo7bE9YT0CIgEb7Roj9bNUQfUj1YJJPCA8ofVf21Hxsx6FEH5xaR4C7XIZ-wQJ5I_veSlfn6TTHyVqKZwFXHzREORP_y3qvG0cQvlmjS41do0sjporuqWK6PibYm6PzrN8nJ1u68xnXQUZXk1GjlIW0D7W6OYANpIiQuS3dpV5ZmXyNg29WpcjVHri1UNj1cHvjflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوخت رسان ها از تلاویو بلند شدند
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14749" target="_blank">📅 23:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ظریف:
این جماعت مخالف توافق عده‌ای نفهم هستند که هیچ درکی از واقعیت ندارند.
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14748" target="_blank">📅 23:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
اطرافیان نتانیاهو می‌گویند: نگرانی بزرگ این است که ترامپ در بحث توافق با ایران، با ما همان کاری را بکند که اوباما با ما کرد.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14747" target="_blank">📅 23:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">«زمان تنها خدای واقعی است»
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14746" target="_blank">📅 23:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14745" target="_blank">📅 23:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14744" target="_blank">📅 22:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14743" target="_blank">📅 22:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14742" target="_blank">📅 22:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رسانه های آمریکایی: مراسم تشییع سید علی خامنه ای رهبر سابق جمهوری اسلامی ایران در روز 4 جولای، زمانی که آمریکا روز استقلال را جشن می گیرد، برگزار خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/14741" target="_blank">📅 22:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الان روبیکا ، بله و سروش فیلتر‌ میشه
😂
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14740" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شورای هماهنگی بانک‌های دولتی:
اختلال در سامانه‌های چهار بانک ناشی از یک حمله سایبری محدود بوده، اما هیچ‌گونه نشت اطلاعات یا دسترسی غیرمجاز به داده‌های مشتریان رخ نداده است
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14739" target="_blank">📅 21:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مقام ارشد اسرائیلی به کانال ۱۲ اسرائیل: این یه توافق مزخرفه
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/14738" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مردم طرفدار حکومت اعتراضاتی رو در چند استان شروع کردند @withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/14737" target="_blank">📅 21:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کارشناس شبکه افق:به زودی جنگ را به خاک آمریکا می‌بریم و دیگر قرار نیست در خاک خودمان با دشمن بجنگیم جمهوری‌ اسلامی هنوز کارت های خود را رو نکرده
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14736" target="_blank">📅 21:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14735">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb7b47099c.mp4?token=GOat9CXcMoT5kHcmCcELXDGZFDP0zs11wHHOssDBIjFoEETrrj8ngSGy-FHit8bjnrWWTjO6yz93OAstRQCKpgY3oStA7pH0OLp9RA1B5ARBGP43vqJwZSc7GO9rXPNKKiO98COU1QTOP8Qkb4R4Hwe2vCDQPaPG8AI1KiE-bLV78iz4dzAnvcX7hLAMp7HC3t229LeV7ThDoBN9_ZCI9RlFVVerDuaAGCqrTiJApWeX3c2AFPeTRpffjt5LAeeYLgPdFaQLpGkGzX3L1TGnTw_PvnifrVlXbAKI1CAHnhY-3DSCOYp6a5ff2x9XB1h1MSZLw8c-ia-Z21UhbSgKGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb7b47099c.mp4?token=GOat9CXcMoT5kHcmCcELXDGZFDP0zs11wHHOssDBIjFoEETrrj8ngSGy-FHit8bjnrWWTjO6yz93OAstRQCKpgY3oStA7pH0OLp9RA1B5ARBGP43vqJwZSc7GO9rXPNKKiO98COU1QTOP8Qkb4R4Hwe2vCDQPaPG8AI1KiE-bLV78iz4dzAnvcX7hLAMp7HC3t229LeV7ThDoBN9_ZCI9RlFVVerDuaAGCqrTiJApWeX3c2AFPeTRpffjt5LAeeYLgPdFaQLpGkGzX3L1TGnTw_PvnifrVlXbAKI1CAHnhY-3DSCOYp6a5ff2x9XB1h1MSZLw8c-ia-Z21UhbSgKGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم طرفدار حکومت اعتراضاتی رو در چند استان شروع کردند
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14735" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14734">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رادان : هرکس در تجمعات علیه وحدت ملی و مذاکرات شعار یا حرفی بزند بعنوان تفرقه‌افکن باهاش برخورد میکنیم.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14734" target="_blank">📅 21:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اسرائیل هیوم: اسرائیل ملزم به امضای توافق با ایران نخواهد بود و قادر به دفاع از خود است، اما رفتار آن باید با ایالات متحده هماهنگ شود
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14733" target="_blank">📅 21:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4U3xituq9vPlPY3MchWrpFJH15cEwSu9GiX5EXiMN24rTX5utpZYpp1S_pVcHa848IZToaTXj0eiL8rT7D8DAyw1zrY1dmxAgQ4dIulME-xrExnC4eDb5MWBmLPaTRpTd0SUNgpEJdZD59lBXsvWGe37LqMu176Oeqs1Gn6R9ky5HzQulOMvfe0FmomPGqME_c72wDboREfX0sTG8jUSlf8BPNLCKRVz99ZetzvbYRDWyeCdTcIvxGxnK70DgqRL0MSKubWwQV4oVWf-h5bmPV2egp_CKlV95KF7E0dx0FGsdB2GClpJQVp6agqzzg2AM1UEL5vDsLYpJ3-NKgdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «کتابخانه اوباما، ده سال دیگر، به “مکه” کسانی تبدیل خواهد شد که از آمریکا نفرت دارند.»
دونالد جی. ترامپ
نکته: واژه
“Mecca”
در زبان انگلیسی در این‌گونه کاربردها به‌صورت استعاری به معنای «مرکز تجمع»، «کانون» یا «مقصد اصلی» است و لزوماً اشاره مذهبی مستقیم ندارد
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14732" target="_blank">📅 21:26 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">آکسیوس: انتظار می‌رود ایالات متحده و ایران، با میانجیگری پاکستان و قطر، روز یکشنبه یک نشست مجازی برگزار کنند تا به صورت الکترونیکی تفاهم‌نامه‌ای را امضا کنند که آتش‌بس را به مدت ۶۰ روز تمدید می‌کند، تنگه هرمز را بازگشایی می‌کند و مذاکرات در مورد برنامه هسته‌ای ایران را آغاز می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14731" target="_blank">📅 21:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">فارس: با توجه به اینکه فردا تولد ترامپ است مسئولان ایران اجازه نخواهند داد توافق فردا امضا شود
@withyashar
😂</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14730" target="_blank">📅 20:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDKlmH7Ft8Y_VBkaSZbkH1aT8FJoabXWlTEk2EF2fWYfmUgPaOC_FQEmxXx3JsQhadeHvXvIwfIwK7gTq-edAeM1zMddW1M2zenv7sBGQGr70-wackjyWCHpP6mhTB4CZCGk29lKogx3oaVWLrDk7MENp9EA305UnE7fnxjacAVb-_i355xe4YxAlN5DFG2VzZPp2STI3MXbsr0fB9ByN8IpdmDxyRuGiXfFHqVSsN98yK-Zab8L7sa1UD2DnO6uaQdGLp-bSy-gCZPoQTt4VITo1EbCya20CWpD8XoPkrIR2mKd3QPnsjsIaytcqIluPXQfx1Fb-rY1A9ouzMx7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «توافق باراک حسین اوباما با ایران، یعنی برجام، راهی آسان، هموار و بی‌دردسر برای دستیابی به سلاح هسته‌ای بود؛ سلاحی که ایران شش سال پیش به آن دست پیدا می‌کرد و مدت‌ها پیش از امروز از آن استفاده کرده بود.
توافق من با ایران دقیقاً نقطه مقابل آن است؛ سدی در برابر سلاح هسته‌ای!
در حقیقت، آن‌ها دیگر خواهان سلاح هسته‌ای نیستند و همچنین هرگز به آن دست نخواهند یافت؛ نه از راه خرید، نه از راه ساخت و نه از هیچ راه دیگری.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضای آن، تنگه هرمز به روی همه باز خواهد شد.
روابط ما با ایران بسیار متفاوت و بسیار بهتر از روابطی است که دولت‌های پیشین با آن داشته‌اند.
برخلاف صدها میلیارد دلاری که اوباما به آن‌ها پرداخت کرد، از جمله یک میلیارد و هفتصد میلیون دلار پول نقد، در این توافق هیچ پولی میان طرفین رد و بدل نخواهد شد.
در زمان مناسب، هنگامی که همه‌جا آرام باشد، ما وارد عمل خواهیم شد و بقایای مواد هسته‌ای را که در اعماق کوه‌های عظیم گرانیتی مدفون شده‌اند ــ به لطف بمب‌افکن‌های بی-۲ ما و خلبانان برجسته آن‌ها ــ خارج خواهیم کرد و آن‌ها را رقیق‌سازی و نابود خواهیم ساخت؛ چه در ایران و چه در ایالات متحده.
ما مشتاق همکاری با ایران و با سراسر خاورمیانه در سال‌های آینده هستیم.
امیدواریم این روند به سرعت، آسانی و بدون مشکل به نتیجه برسد.
اگر چنین نشود، ما گزینه نهایی را در اختیار داریم؛ گزینه‌ای که امیدواریم هرگز دوباره نیازی به استفاده از آن نباشد.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14729" target="_blank">📅 20:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به گزارش تانکر ترکرز
یک نفتکش VLCC دیگر مرتبط با تحریم‌ها با غیرفعال کردن سیگنال ردیابی AIS خود، محاصره نیروی دریایی آمریکا را شکست.
این کشتی با سابقه پنج ساله نقض تحریم‌های OFAC آمریکا مرتبط با تجارت نفت ایران و ونزوئلا، می‌تواند حدود دو میلیون بشکه نفت حمل کند و به عنوان انبار شناور اضافی برای ایران عمل می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/14728" target="_blank">📅 20:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تلویزیون دولتی لبنان:
شهر استراتژیک مجدل زون در نزدیکی بندر صور در جنوب لبنان به دست نیروهای ارتش اسرائیل سقوط کرد.
@withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14727" target="_blank">📅 19:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الحدث به نقل از منابع آگاه:  منابع حاکی از آن است که یک هیئت ایرانی، شامل وزیر امور خارجه عراقچی، فردا وارد پاکستان خواهد شد. هیئت ایرانی بر مذاکرات فنی مربوط به این توافق نظارت خواهد داشت. @withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14726" target="_blank">📅 19:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">باراک راوید، خبرنگار اکسیوس:
یک مقام آمریکایی اعلام کرد که دونالد ترامپ روز سه‌شنبه در حاشیه اجلاس گروه هفت با رهبران خاورمیانه دیدار خواهد کرد.
نتانیاهو در مذاکرات دوجانبه ترامپ با رهبران خاورمیانه در گروه هفت شرکت نکرد.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/14725" target="_blank">📅 18:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">آکسیوس:فردا توافق بین ایران و آمریکا امضا میشه. @withyashar</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/14724" target="_blank">📅 18:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">آکسیوس:فردا توافق بین ایران و آمریکا امضا میشه.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14723" target="_blank">📅 18:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">الحدث به نقل از منابع آگاه:
منابع حاکی از آن است که یک هیئت ایرانی، شامل وزیر امور خارجه عراقچی، فردا وارد پاکستان خواهد شد.
هیئت ایرانی بر مذاکرات فنی مربوط به این توافق نظارت خواهد داشت.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14722" target="_blank">📅 17:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cS441IIjH-gTxhKD07LJjB-GRQzhw9pGjIPV2VqAgfUaiGvPrY6iFhKhdqeoS71zpgmBh_nu7XCPsRIhQaFqtsjSc2m8RceQYNfln6CRNOewosfbub8OzQzlBrfLRa-wQlLUplJ1jj0Xnt0hQt_QjBLZS9SJeM0bEpUbl1FWSKEFzXvD4PtBE_u84MaUlU0zlCewHJ1JsYwuqp0eINYYS4vHp94rwqbjmlEXBz-Up_E_wQjnwH7slLRtHWy01mx2QCdaQ203cOBqz9CkZFn-hmS_dmzKBTQiyFX04ahpXx7eNfQbAieS315bfvpzkXHzikDHvi8-zaRCBvyVqbwmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ توییت شهباز شریف نخست وزیر پاکستان را در‌تروث منتشر کرد :
شهباز شریف: «ما اکنون بیش از هر زمان دیگری به دستیابی به یک توافق صلح نزدیک شده‌ایم. با توجه به اینکه
انتظار می‌رود این توافق طی ۲۴ ساعت آینده نهایی شود
، پاکستان در حال آماده‌سازی برای امضای الکترونیکی توافق صلح بلافاصله پس از نهایی شدن آن است و پس از آن نیز گفت‌وگوهای فنی و کارشناسی در هفته آینده برگزار خواهد شد. مایلیم از ایالات متحده آمریکا و جمهوری اسلامی ایران به دلیل تعهد و همکاری مستمرشان در طول مذاکرات قدردانی کنیم و همچنین از برادران خود در منطقه بابت حمایت‌هایشان صمیمانه سپاسگزاری نماییم. ما اطمینان داریم که این توافق صلح تاریخی، بنیانی محکم برای صلحی پایدار و ماندگار فراهم خواهد کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14721" target="_blank">📅 17:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال های خبرگزاری فارس، بابک زنجانی، صرافی نوبیتکس، والکس، رمزینکس و بیت‌پین که تو یوتیوب فعالیت میکردن، به علت تحریمای آمریکا همگی مسدود شدن
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/14720" target="_blank">📅 17:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزارت خارجه آمریکا بار دیگر درخواست ویزای مهدی محمدنبی سرپرست تیم جمهوری اسلامی و مهدی تاج رییس فدراسیون فوتبال رو رد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/14719" target="_blank">📅 16:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egccOcIlsd6QwU6o7I_75DwWOavwJ5l4lFEC-0-f1KpgGryC_W0ik2QqI7Y6eUenWC5xXrdD1z_CfPRqu4ypize-HB5dQsOft8flyugzjI29Wy-9yHrTV71uE-Ki43tymMUINSSXjFNJbjKMbIQWfWndP_8TKViWr2vxVAL3JUX8zd3P61cj7_iTypvPepMLbelVLQKTNpKd2G_tJ-MxSk4tQXyPmp8U2KAMJhSGZU9oQUFhZ8Oagw6YbPo7jZUNLoxfgThgWRj5eFlVBdA_ezD3AHVN3fnAFKNCVS_icvf_pKUYLOLvExrxuH8oEC5OcYyBlYngtSvvncWf4EemQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">16 تا نماینده مجلس به همراه قشر تندرو امشب جلوی وزارت خارجه تجمع اعتراضی برگزار میکنن و به روند مذاکرات اعتراض میکنن‌.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14718" target="_blank">📅 16:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بقائی، سخنگوی وزارت خارجه:
درباره زمان دقیق امضای تفاهم‌نامه باید منتظر بمونیم؛ اگرچه فردا نیست اما احتمال اینکه در روزهای آتی این اتفاق رقم بخوره منتفی نیست.
@withyashar</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/14717" target="_blank">📅 16:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نماینده مجلس خطاب به  عراقچی وزیر امور خارجه:
مذاکره بعد از حمله نظامی، دیپلماسی نیست، مستعمره شدن است
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/14716" target="_blank">📅 15:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">وزیر آموزش و پرورش: به خاطر اهمیت حضور دانش آموزان در مراسم تشییع، تقویم امتحانات نهایی بازنگری میشه و احتمالا تاریخ امتحانات عقب میوفته
@withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/14715" target="_blank">📅 15:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعد از پخش آهنگ امیر تتلو از زندان که پشت تلفن اجرا شده بود، زندان تهران بزرگ تلفن او را مسدود کرد و تنها دلخوشی او هم گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/14714" target="_blank">📅 15:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بلومبرگ: جمهوری اسلامی به‌احتمال زیاد در جریان آتش‌بس، سلاح‌های پیشرفته روسی رو به ذخایر تسلیحاتی خودش اضافه کرده.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14713" target="_blank">📅 15:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14712" target="_blank">📅 14:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">نخست‌وزیر پاکستان: متن نهایی توافقنامه صلح بین ایران و آمریکا به دست آمد
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14711" target="_blank">📅 14:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جزئیات مراسم تشییع و تدفین علی خامنه ای رسما اعلام شد
شنبه و یکشنبه
13 و 14 تیر (19 و 20 محرم): مراسم وداع با پیکر در مصلای خمینی تهران
دوشنبه
15 تیر (21 محرم): مراسم تشییع در تهران
سه شنبه
16 تیر (22 محرم): مراسم تشییع در شهر قم
پنجشنبه
18 تیر (24 محرم، شب شهادت امام سجاد ): تشییع در مشهد مقدس و سپس
خاکسپاری در حرم امام رضا
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/14710" target="_blank">📅 14:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بلومبرگ به نقل از یک مقام آمریکایی:
در صورت تحقق شرایط، واشنگتن تحریم‌های ایران را کاهش داده و اجازه ادغام این کشور در اقتصاد جهانی را خواهد داد.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14709" target="_blank">📅 14:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فارس از احتمال حملات سایبری به ۴ بانک خبر داد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14708" target="_blank">📅 14:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تا دقایقی دیگر نحوه و زمان خاکسپاری خامنه ای را قرار رسانه های رژیم اعلام کنند.
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14707" target="_blank">📅 13:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">واشنگتن پست به نقل از یک مقام دولت ترامپ: تعیین میزان پولی که ایران می‌تواند به طور بالقوه دریافت کند دشوار است زیرا بستگی به آنچه آنها ارائه می‌دهند دارد.
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14706" target="_blank">📅 13:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دولت عراق خواستار تحویل سلاح نیابتی های سپاه وخروج هرچه سریعتر نیروهای سپاه از خاک عراق شد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14705" target="_blank">📅 13:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی سه بانک ملی، صادرات و تجارت دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد @withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14704" target="_blank">📅 13:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPVyUZRVfBWXvNU3TcvfkIVlA7U6aNyC6uX24Zh1K4ip7xIjvN2BmLfgRxuldzR2jmR7WuqfV0IoKdItK0L9BUWiG99Wu9xVsjXhBe_-62ma0z41aA-p9HzIG4UJX85SmLhZSww3i09YZDnZZ0s8w1i4jGsImBC8RoUv0uole-GWGpRAPHiaSPvT_RZ3AR7O1ODjvMGPdwtgpQkQmIpNY_nrc8Ox34X02lAzNiCRb1HB3shsqRuPWPtWiaeZLY5aljo0bdsvqcqfEp_YGLT2Wt3qKQ6g_xCDuml-3gtUnyJOvM7rU1w0klO2SQ1BAzGR4LYxR5oWOLRetc2dBwITQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنوب لبنان؛ ارتش اسرائیل پرچم این کشور رو روی تپه العویدات و کنار سازه «یا حسین» نصب کرده
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/14703" target="_blank">📅 12:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از صبح امروز شنبه ۲۳ خردادماه، سیستم بانکی سه بانک ملی، صادرات و تجارت دچار اختلال و قطعی شده و تا زمان ارسال این خبر همچنان مشکل ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14702" target="_blank">📅 12:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">هوش مصنوعی رقیب جدید مدرک شد
نتایج نظرسنجی موسسه پژوهش‌های اقتصادی «ایفو» نشان می‌دهد :
۲۰ درصد از شرکت‌های آلمانی استفاده‌کننده از هوش مصنوعی معتقدند که می‌توانند کارکنان دارای مدرک دانشگاهی را با نیروهای مجهز به ابزارهای هوش مصنوعی و بدون تحصیلات دانشگاهی جایگزین کنند.
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14701" target="_blank">📅 12:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14700">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">️اسکات بسنت، وزیر خزانه داری آمریکا اعلام کرد که با توجه به روند پیشرفت مذاکرات، انتظار می‌رود توافق صلح با ایران «احتمالا تا پایان همین هفته (میلادی) یا اوایل هفته آینده نهایی شود.»
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14700" target="_blank">📅 12:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">روزنامه خراسان (نزدیک به قالیباف):
تفاهم ایران و امریکا قرار نیست اختلافات را حل کند؛ فقط یک فرصت است که طرفین خود را برای جنگی دیگر آماده کنند
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14699" target="_blank">📅 11:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuFXuA6SaiGCGbWAGQ2pBMiW4wYupy3XhPS0M1zkrmhpiCN3CNxQkG8j8V6ZQtp4FRmickb7b1L2af1-hAUh3eR6txIvKMxhIuTI8CFWzUfQF2JQH0CGLA7oP_X4adYTvtZE9LmWio5QZaxdTf_Da-svd52DfnFHQXQV7UidCS9t6VStWR4es_zYPeH-gbgZlAzPiulNgnj2XaxZmEPt4cztjgUmv6E80tUjW4tvzGlUUbvWOIpEL8K1_lSB8baeZBtEB1UNiFtOsWvi9MyMDAL2zQ9uheJU9IvU3cI1MrxgS7E-0JiWfETDy0jBTwbwavL9kY47RyGkcqRaslDGYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود الان کرج
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/14698" target="_blank">📅 11:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به ادعای CNN: ایران بخش‌هایی از ذخیره اورانیوم بسیار غنی‌شده خود را با ریزش تونل‌ها و مین‌های انفجاری در اطراف ورودی‌ها مسدود کرده است. این اقدامات در پی نگرانی‌ها از احتمال عملیات آمریکا برای تصرف این مواد، دسترسی به اورانیوم را به‌طور قابل‌توجهی دشوارتر و خطرناک‌تر کرده و تلاش‌ها برای حذف یا نابودی ذخیره تحت هر توافق آینده را پیچیده می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14697" target="_blank">📅 10:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار آکسیوس باراک راوید: نتانیاهو امیدوار بود که جنگ منجر به تغییر رژیم در ایران شود، اما رقبایش اکنون او را متهم می‌کنند که با پذیرفتن شرایط آمریکا، اسرائیل را به (دولت دست‌نشانده) تبدیل کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/14696" target="_blank">📅 10:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ارتش اسرائیل، هشدار فوری تخلیه برای ساکنان ۲۰ روستا در جنوب لبنان صادر کرد! پیشروی در لبنان به سرعت ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/14695" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgvlMsSCudPCib3eCJ8sVjnTtoMHKNFNm3HMGawqGrgAUxznsyYn3lw5rlCXvbCn4HO430FLPEAKYHgs6fml1GKK5X2B7uG_17FxIZ39C4766GL-XTo0HI7pqY_UAzE7r4oKdJfMDW8u0cUoau3yKjZj7YD0l6ZiZ54oj0sj6DquQqJMZhjCunTZnU_mf-bS4kNOVIS62wMPzPFCLlL54onMjCEFbvgz1-BclPhSgUg5edezFRWWrp3LnFbuoRCTWijXW7kluMSrqsY_Y1Szy849xkQ5IRbMrz_v_yq5nFczkaLKK2b6tRPogBmUImg05EEkuNf1p0AjjSn7TWLevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام (فرماندهی مرکزی ایالات متحده):
«ایران چندین پهپاد انتحاری (یک‌بار مصرف) را با هدف حمله به کشتی‌های تجاری در حال عبور از تنگه هرمز به پرواز درآورد.
نیروهای ایالات متحده در ساعات اخیر همه آن‌ها را سرنگون کرده‌اند و جریان تردد دریایی از طریق تنگه هرمز بدون هیچ‌گونه اختلالی همچنان ادامه دارد.
این گذرگاه بین‌المللی تجارت همچنان برای عبور و مرور کشتی‌ها باز است.»
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14694" target="_blank">📅 10:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صدای انفجار دزفول ناشی از امحای مهمات است
از ساعت ۱۰ تا ۱۳ امروز شنبه ۲۳ خرداد، انفجارهای کنترل‌شده در برخی نقاط شهرستان دزفول و خارج از محدوده شهری انجام می‌شود.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14693" target="_blank">📅 10:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اکسیوس
:
برخی در واشنگتن معتقدند حتی اگر توافق اجرایی شود، نتانیاهو ممکن است بازهم بتواند نقش یک اخلالگر را ایفا کند
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/14692" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مقام اسرائیلی به یدیعوت آحارونوت: ایران هربار تصمیم بگیره در حمایت از حزب‌الله به ما حمله کنه، فوراً بهش پاسخ نظامی می‌دیم.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14691" target="_blank">📅 09:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">محسن رضایی:
ترامپ با آزادسازی 24 میلیارد دلار از دارایی‌های بلوکه‌شدۀ ایران موافقت کرده اما با صراحت این موضوع رو اعلام نمیکنه.
@withyashar
🥴</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/14690" target="_blank">📅 02:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zgdrj9hUW6QGFhjRMKaKP_UZvR3o4s2tX9DY1bMhNRV2L1uX9sYFgkpTjfx-GD9KSf6zmq-iHZ2HhajGJR4jFsX-tHZVvGHAElYuQ_16-o40yGOpKpMwTNWCSsKw2eb-hScflgKoCL-vlQr934ZLAjlsgq8Ji2bF2Zs4AAy8HTNcKAVrZoS6z_V3e5HW2fN8gAQeoFUIomJcEEWvbq7_LbJE86WIQ6mZZMIpKAAl-7U6U7pomCz1qsfSyc1ue5ZbETCqIO3f44KdEvzyfU3by7bqGBRSJexEKSLafjuEnncLYdBKIqIdG1GilzB43kgbfq6o18c9DuT5fvQHrVipjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشروی ارتش اسرائیل در جنوب لبنان؛ ۶.۷ کیلومتر تا نبطیه
ارتش اسرائیل به شهر ارنون رسیده و هم اکنون در حال حملات توپخانه ای سنگین به تپه علی الطاهر هستند.  l بالگرد های آپاچی ۶۴ اسرائیلی نیز به تپه علی الطاهر حمله کردند.  با تصرف این تپه مهم رسما تصرف شهر نبطیه برای اسرائیلی ها آسان خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/14689" target="_blank">📅 02:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">Bombardier E-11A در منطقه توضیح در ویس @withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14688" target="_blank">📅 01:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnETQIUMG07rnHfSNWbtXNEFA8ei9shVC2j586An1jsL_NHouOArf2yEPW2WwhO9fPKDdbQ6iu-OD6chMxSk8YIfreXvaTlqCunlz34kU6Hk_2fdwia47s-6HBJUb0xPPcVSmDmZxIxhmwU77mwcH3fygLnMMyS7B_wJkMGlcRiI2tZ8QXPzNsYN_nWSQ_YrnRSAIV2able0QdzKnPzrOx_ipsodB8MINaUoXYw51w326P0ZL0wrSqTOMzSiYdKMwE5FCJkXAYqXrlc68HdXvl4YuNQLrpQPxkEZpYni3hlUBkP12rECXNgBgxVN-86m7moG1JjYtHr4Y6856Nm0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Bombardier E-11A در منطقه توضیح در ویس
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14686" target="_blank">📅 01:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14685" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWRjmaNerQWFsCI4xlD4HD-EFhO8BgyPpHilhRdUcfc4QB2a5FDmoyAd3SW1UhA60FKd8EA8InG8P-BIuApY7sF6cF92vO5BDE1JHIGB2HPw26ROjVsQ2QUUWgnWL7Lki_H3z6FoXlNb5lGyhHH2rWMIXWyWMwffrdcb_h8Bo9CqXPrtXy51_GFCnb-b_73WWVxq3Z8slNxXowavgghiaC6fQy03ePNFN9cJuJgjDaotTXYMJmDQeRiezps60kMT9t5HwRTh2VyLlx5NURYDOua6HrE1fU7jVt8VrbC-SNhlxqUD6Ux1GO8VN2e313Fg0otQF7jkq82mahSE2xgZ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات ادعای رویترز بابت آزادسازی دارایی های ایرانو تکذیب کرد
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/14684" target="_blank">📅 01:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Khabam Nemibare Live(IG @yashar)</div>
  <div class="tg-doc-extra">Amir tataloo (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/14683" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
instagram.com/yashar
🌐
t.me/withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14683" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/14682" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14681" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⁨ اتاق جنگ با یاشار :  باز‌ تنگه دعوا شد ، گزارش عجیب از حضور هواپیماهای جاسوسی آمریکا همه با هم. !!!⁩
https://www.instagram.com/reel/DZgA2cQxrjS/?igsh=cnM5b3ViejIxcm5t
کلیک کنید و کارهای اداری پست را انجام دهید.</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14680" target="_blank">📅 00:39 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کاور  @withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/14679" target="_blank">📅 00:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">۳پا : کشتی هایی سعی کردند بدون مجوز از تنگه هرمز عبور کنند و مورد هدف قرار گرفتند.
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/14678" target="_blank">📅 00:35 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDtIDx9TLx16U2kMRSi9YAR5qWZHijmyDV4kVnYBzwa5kB9RZMiJ-2jBbeMQeyyGI7PpZRN_uG7SaueHfe8psqFwUPu2pBqfI95HJQn15TRr2oKOPMhT5cyX9G_uJXyTIiUpVf5BGWxMlCEWz_DM07l0zR827u6vzkri40ba2f_JgZSM6Sa1ZGIiko3hQzw3K1eV2O6ltfsu_ITxHjOD4k_51g5rlLuIoFAyTZPBXaP91sPqJmngrRSyER8IjXhyM1VATJRIJ4tT-345W3p_hThbUU26DmDcLQIGuqigVmtLYVShInc603g1CARKxiQjuPxHN8VIA9wzg5TXWbYJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14677" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14676">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تو تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14676" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14675">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مهر : شنیده شدن صدای انفجار در حوالی جزیره قشم و سیریک؛ گمانه‌زنی از درگیری دریایی
بررسی‌های اولیه نشان می‌دهد، در پهنه شهرستان سیریک انفجاری رخ نداده است و احتمالا صدای شنیده شده تلاشی برای کنترل تنگه هرمز و از سوی دریا بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/14675" target="_blank">📅 00:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/14674" target="_blank">📅 00:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-14673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صدای انفجار سیریک
🚨
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/14673" target="_blank">📅 23:59 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
