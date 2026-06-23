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
<img src="https://cdn4.telesco.pe/file/bYcQ_RH6kGEfPxD8DLblT-Cxu1lxmt1wibxJvH8O2XPYH4Zeey0Be01zqTtxUfwHz-SpaRMc5RDUFYfBQ7t3Mjoa03k0WFgB4_7PA3bO187D4yhqKizIxtnqkTDTwkX5OHmgFtOZijSFl_yjuQYHWtICXWoiNMh0hHY7tHX4KBusnpz5FtU4SLCB5ZB31I-BuI615uzTP2GfoDKysPRwlpAOOm9UKueAlq_7Sc-oqeLwaq_yp4l64onhgxL_N3oqyGDeL1D9vCvmXZUw_UsF8yhSojBQkFfyKGeMmvrXvJs-ihXddRKfcopqKXsQDJckceSArLlmqZY6eVMTzEXMpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 53.3K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 03:19:16</div>
<hr>

<div class="tg-post" id="msg-2700">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙢 𝙢 𝙙</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErZ_4ft87XPsiYA2ZKcjjjHNaT8XnN1A70zULdZ-YyAWFAX9D5nhngq7UItkydBqSyv0clqdZ2C9qDIkjgTuj5t-_0drBlB3ZidBFS-qJsI9ph0Gjv-OeIWtAzPv-rWX6p-wj3ol2AIbLSVObH1dBwshstE2pLwuMHUytx_SjM7EtFv381qZruy8z2Tt7GkpM9n7IeBnKS09Zbb-xFLWVpYTke_RnQCyjG-sVvLST86otXmC08-EmP0YnUAXDJ_Llr7I7uKyqJnHlG244G8GNL2J4r-F4wexaZ1V2vfZfmJWzvqjXJ1Kk1IHKxjM7fo24Qoi2nQSfZTtM8tyhG5xUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">​«فقط بفروش، پشتیبانی رو بسپار به پارس پنل!»
💼
〰️
​اگر به دنبال یک درآمد عالی، بی‌دردسر و مطمئن هستید، پارس پنل تمام زیرساخت‌ها را برای شما آماده کرده است. شما فقط روی فروش تمرکز کنید، بقیه کارها با ما!
​
🌟
🌟
چرا پارس پنل؟
🤔
​
🌍
پنل مولتی لوکیشن: اتصال همزمان به چندین کشور از جمله:
🇩🇪
آلمان |
🇦🇪
دبی |
🇹🇷
ترکیه |
🇫🇮
فنلاند |
🇳🇱
هلند |
🇫🇷
فرانسه |
🇺🇸
آمریکا |
🇮🇹
ایتالیا |
🇦🇿
آذربایجان |
🇮🇳
هند |
🇵🇱
لهستان |
🇸🇪
سوئد |
🇬🇧
بریتانیا
​
🎁
هدیه شروع: با استارت ربات، همین حالا
10 هزار تومان هدیه اولیه دریافت کنید!
​
⚡️
تحویل فوری:
پنل اختصاصی خود را زیر ۱۰ ثانیه تحویل بگیرید.
​
💰
جشنواره شارژ: برای هر بار شارژ حساب، هدیه و بونوس ویژه بگیرید.
​
🛠
تست رایگان:
اول مصرف کن، بعد پرداخت کن!
(تضمین کیفیت خدمات)
​
🔥
با پارس پنل می‌توانید تفاوت را احساس کنید.
​
⬇️
همین حالا روی لینک زیر کلیک کن و پنل رایگانت رو تحویل بگیر:
🆔
panelparsbot</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/iaghapour/2700" target="_blank">📅 20:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2699">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/iaghapour/2699" target="_blank">📅 20:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2698">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
حمله سایبری به شبکه بانکی
!
شرکت خدمات انفورماتیک با انتشار اطلاعیه‌ای، دلیل اختلالات گسترده در کارت‌های بانکی را تشریح کرد.
🔹
جزئیات این اختلال بانکی:
🔸
دلیل اصلی قطعی:
وقوع حملات سایبری به سامانه‌های کارت‌محور بانک‌های ملی، صادرات و تجارت.
🔸
اقدام پیشگیرانه:
این شرکت اعلام کرده برای جلوگیری از دسترسی غیرمجاز هکرها و حفظ امنیت داده‌ها و موجودی مشتریان، خدمات مبتنی بر کارت را موقتاً و به‌صورت عمدی از دسترس خارج کرده است.
🔸
گستردگی مشکل:
با وجود اینکه در اطلاعیه رسمی فقط نام ۳ بانک آمده است، اما بررسی‌ها و گزارش‌های مردمی نشان می‌دهد قطعی‌ها گسترده‌تر بوده و بانک‌های دیگری مثل «ملت» هم درگیر این اختلال شده‌اند.
🔸
وضعیت فعلی:
تیم‌های فنی و متخصصان امنیت سایبری در حال کار روی شبکه هستند تا این مشکل برطرف شده و خدمات بانکی به حالت عادی برگردد.
پ.ن: بابا ولش کنید‍! بعد 2 هفته اختلال این حرفا چیه میزنید؟ مثل قبل همون روند تکذیب رو جلو برید. بگید که ما هک نشدیم و قطعه سخت افزاری سوخته!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/iaghapour/2698" target="_blank">📅 19:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2697">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lglfrfSDyDTWn3AhvzQtVuXu3qvtpN9Jaeqbpht-sg4zguF3HGFl_oQ8GnLACxUj9Ajdq87MVFDd1TBwT90sa0-2bn9f34h0LwqzCNN-_E9Zd-CcXEorzkzsF7yjPQB_sncTtjwbujKvoYuJFD_Zk8MKWjbZQ-t3ZCG-nBUAj-yBY1ZkF2_YghA3DiPhKPNf_srU1TsYoZqCoO_V1sOoLpgfE3f98LuIB0F4ahpH_dxRjeP5U7uITi-liKJKIEczgFoSiRmC2wbA9knq_nm9cjCuukPYZiASVJsUORZLiq_Eri9tKv7NXbWjtA6VQA6zXdLOTAP8ltotMtkq58Trww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
چرا فعال نبودن IPv6 در ایران یک بحران است؟
در حالی که دنیا به سمت استفاده کامل از IPv6 رفته، اتکای شبکه ما به ظرفیت محدود IPv4 چه مشکلاتی ایجاد کرده است؟
🔹
پیامدهای اصلی این عقب‌ماندگی:
🔸
کابوس CGNAT:
به دلیل کمبود IP، اپراتورها هزاران کاربر را پشت یک IP مشترک مخفی می‌کنند؛ یعنی شما عملاً هویت مستقلی در اینترنت ندارید.
🔸
دردسر همیشگی کپچا:
چون درخواست‌های هزاران نفر با یک IP ارسال می‌شود، سایت‌های خارجی شما را ربات تشخیص داده و محدود می‌کنند.
🔸
مشکلات گیمرها:
گیر افتادن در لایه‌های NAT باعث خطای Strict NAT، افت پینگ و قطعی در بازی‌های آنلاین می‌شود.
🔸
اختلال در دسترسی‌ها:
بدون IP مستقل، راه‌اندازی شبکه‌های خصوصی و دسترسی از راه دور به دوربین‌ها و تجهیزات هوشمند بسیار دشوار است.
🔸
افت کیفیت شبکه:
بار سنگین سیستم‌های تبدیل آدرس (NAT) روی سرورها، باعث تاخیر در مسیریابی و کاهش پایداری اینترنت می‌شود.
پ.ن:
دنیا با میلیاردها آدرس مستقل به دنبال سرعت و پایداری است، اما ما هنوز برای یک ارتباط ساده، درگیر پیدا کردن یک IP تمیز و عبور از لایه‌های NAT اپراتورها هستیم!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2697" target="_blank">📅 22:56 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2696">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUCAiYZ7nktmj2NNKeYyWkrdaPA05ZBPzCHm6dC91qoQTEwH1d8tQCGIXF-G1GobhrMgOSMgwDs95RxI1FpIZV8VSbPZnkjG5cCTRF-CBk9bP2drqjqlv70Nm8Rbl7lWyCBE7xzwGGy7y6JRufuXeChuW_8i6920n60XHMTkAk635qEm-Nj0EyoH9GzM7S7hDY7vCjVidaTHjq2o125aHjbSIEGCc6w5UsUAlvF1QaMeVMiFk1jshN3YjRAXn8gKGpDu_rR_66eSm3gGSs2WsLF4pJjN7F_9J5DTGfAPyUzGpPokBTLoijf_It5GqcsmRrZke6a24oDeP_LTQwKK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
بحران خاموش در دیتاسنترها؛ اینترنت برگشته، اما نه برای کسب‌وکارها!
پس از گذشت چند روز از قطعی گسترده و مسدود شدن کامل ارتباط با اینترنت بین‌الملل در سراسر کشور، اکنون در حالی که اینترنت کاربران خانگی و اپراتورهای موبایل تا حدودی به حالت عادی بازگشته، اما گزارش‌ها حاکی از آن است که دسترسی بسیاری از دیتاسنترهای داخلی به اینترنت جهانی همچنان قطع یا دچار اختلال شدید است.
این دسترسیِ قطره‌چکانی و عدم اتصال دیتاسنترها، پیامدهای مخرب و گسترده‌ای برای زیرساخت‌های شبکه و کسب‌وکارها به همراه داشته است:
🔸
فلج شدن سرویس‌های آنلاین:
بسیاری از استارتاپ‌ها، پلتفرم‌های خدماتی و توسعه‌دهندگانی که برای کارکرد صحیح نرم‌افزارهای خود به APIها، کلادها و منابع بین‌المللی وابسته‌اند، با اختلال جدی مواجه شده‌اند.
🔸
خسارت‌های پنهان و سنگین:
وصل شدن اینترنت گوشی‌ها تنها ظاهر ماجرا را عادی جلوه می‌دهد؛ در حالی که شریان حیاتی بسیاری از کسب‌وکارهای دیجیتال در دیتاسنترها مسدود مانده و خسارت‌های مالی و فنی جبران‌ناپذیری در حال رقم خوردن است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/2696" target="_blank">📅 19:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-2694">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/iaghapour/2694" target="_blank">📅 21:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2693">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OU850d9oVzCVhQULdEhNjskPbFfKeTozg_UG5f7Ap2OzSvFmLkAMRsQgDQfso5LNQ7uzNY5PihlhU6VRYHJiz7zIT3X_xY66xfKKFXrwmKqmrvMX_eXKhNBqBUwBEwRy-W8oxt5r6Dp06tO_nqgesCDA5ul01wnh_lRYStayRPeCz0ZvQqmLFfr7-Z_GZqyOpc69Msr7DkN2la9XAzAYIZWygj-l4bS44RrI2ZQQhJmtJSRrDZXUpw2kd5QLbsUIo3YQnCLshcbggUt8MAqInbhU-lXyB3ZrI_dTss7jpZq0toePfiRv5xAJ_nbEMRFosxjJtPPcBVP8d6BQlqBBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رئیس سازمان بازرسی کل کشور از توقف اینترنت پرو خبر داده و گفته اپراتورها اقدام به ثبت‌نام گروه‌هایی از جمله وکلا، مدیران و اعضای هیئت‌مدیره شرکت‌ها برای دریافت اینترنت با شرایط ویژه کرده بودند.
در اجرای این طرح، هماهنگی‌های لازم با رگولاتوری و وزارت ارتباطات به‌طور کامل انجام نشده یا در برخی موارد محل اختلاف بوده. بنابراین مقرر شده از ادامه اجرای بخش‌های دارای اشکال جلوگیری بشه و مبالغ اضافی دریافت‌شده از مردم رو بهشون برگردونن. /فارس /
ircf
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/iaghapour/2693" target="_blank">📅 21:34 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2691">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9bEIw9-cBij2ebmixKl-BIPVQNpfD1bBEZpFosiQSvdXzUxaYFUvXXmlirW-pbH6d3JGUU63gNxiB-0FMFaNFNauoqofRrPTZFnKlQ4IPni2RC2Nr3F3NS-QK1_F-adlGd9PZn_pXpr-a8Ikh5kAZr1PanlNsvt2fDl1AcPGqOwLcxzQmBu-QhCydXnHA8DlZnMUuQYYpwbTCSAe2LCMRN5xbo4SoD62Svvc9V61pHUr1AGxJ9wqHhzEFDckjNNLHAOk_0S8e-a6MbEDNfcMSVUDFpcYptlWf-vgVY0Ld_V9m0hLpuJutfDlKD3TvJ47MWHAmpp6q_5imnspVhuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش 4 روش تانل پیشرفته و مقاوم در برابر فیلترینگ
🔹
تو این ویدیو قراره با هم ۴ تا از بهترین روش‌های تانل زدن رو بررسی کنیم و یاد بگیریم چطوری تانل‌هایی بسازیم که در برابر فیلترینگ پایداری خودشون رو حفظ کنن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2691" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2690">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
دوستان عزیز،
ربات «تماس با ما»
چون نسخه رایگانه، به محدودیت ۵ هزار پیام در ماه رسیده و رفته رو حالت تعمیر!
اگه تنظیماتش بر اساس تایم‌زون باشه، اول ماه جدید یعنی 2 روز دیگه خودبه‌خود درست میشه؛ وگرنه به ناچار نسخه پرو رو می‌خرم تا دوباره در دسترس قرار بگیره.
🥸</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2690" target="_blank">📅 17:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2689">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2689" target="_blank">📅 16:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2687">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🌐
مدیرعامل سروش‌پلاس: فیلترینگ و قطعی اینترنت به ضرر ماست!
امین شریفی، مدیرعامل سروش‌پلاس در نشست گزارش عملکرد سال ۱۴۰۴ اعلام کرد که قطعی اینترنت و اعمال فیلترینگ نه‌تنها به رشد پلتفرم‌های داخلی کمکی نمی‌کند، بلکه نتیجه‌ای جز عصبانیت و لج کاربران ندارد.
🔹
چکیده مهم‌ترین آمارهای گزارش سالانه سروش‌پلاس:
🔸
ریزش کاربران پس از رفع محدودیت‌ها:
با آزاد شدن دسترسی به سایر پیام‌رسان‌ها، سروش‌پلاس با افت ۱۰ تا ۱۵ درصدی در تعداد کاربر و کاهش ۱۰ تا ۳۰ درصدی در شاخص‌های فعالیت مواجه شده است.
🔸
وضعیت کسب‌وکارها:
آمارها نشان می‌دهد حدود ۷۰ درصد از فعالیت کانال‌های فروشگاهی، آموزشی و تولید محتوا که در دوره محدودیت‌ها ایجاد شده بودند، همچنان در این پلتفرم ادامه دارد.
🔸
رشد آمار کاربران و پیام‌ها:
تعداد کل کاربران ثبت‌نامی این پیام‌رسان از مرز ۵۲ میلیون نفر عبور کرده است که از این تعداد حدود ۲۰ میلیون نفر کاربر فعال ماهانه هستند. همچنین در سال ۱۴۰۴ بیش از ۳۰ میلیارد پیام توسط کاربران جابه‌جا شده که ۷۶ درصد از آن‌ها مربوط به چت‌های شخصی بوده است.
🔸
امکانات و تغییرات جدید:
رونمایی از مدل اشتراکی «حساب پرو» (با قابلیت‌هایی مثل نشان ویژه و حذف تبلیغات)، توسعه تنظیمات حریم خصوصی و همچنین افزایش جایگاه‌های تبلیغاتی پلتفرم از ۳ به ۱۳ مورد، از اقدامات مهم این سال بوده است.
🔻
پ.ن: من داشتم میخوندم خندم گرفت این چطوری داشت میگفت خندش نگرفت؟
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/iaghapour/2687" target="_blank">📅 19:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2685">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASPT3PngCuzd1OmO0cDZESfez_uY9v7QYaX4_kdRCXhSP2q3ofdRaXxYb7rAZdlMrhZMVa8t4rPBXYYqdPUpT1I_vhzdEtMAGM5Do8kFlbsc3vlWfkejw4k9IfNAixmjBt2nITmoBH67YE1wQLFKB8GM4hZQlJJ2sHdU7yE_2TmhHrcPapUzr2T9x8ON0LkDGgqN2BJGnUFO9kF3D9sqNjoUrKbg0zHSq_4tRwou1PGcyaUCrwds_OmURsEWdPQ-EigOZj1mLWbWRksi_jBeE7TEJ20fdgBdTmEMmhRzf-hokpw2NlwM4LgIalsLCSdoL1N0CjTmd0KUDHmeKxqlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (NovaProxy v3)
🔹
تو این ویدیو قراره یه روش فوق‌العاده برای ساخت یه فیلترشکن کاملاً رایگان و پرسرعت رو با هم یاد بگیریم. این بار رفتیم سراغ ورکر کلودفلر و قراره از اسکریپت قدرتمند NovaProxy v3 استفاده کنیم. تو این ورژن حل مشکل تماس صوتی و تصویری رو هم آموزش دادیم.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ورکر
#novaproxy
#worker
#کلودفلر
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/iaghapour/2685" target="_blank">📅 19:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2684">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOllFrh4PY74OcgGLKAHlTd9bHGaGg0tf3luNvUaymJ_xzn6Vlvyjc10N_8FWjkstnaUJbmws51dZbozWQDPlOIaab8MS174ETAgVX6HlB1C4gWXULFndtrqdIx2HHQaOXfM8fVvmaECWnuEHzJK-Sh-qybE21SiYCT7mw1GrqEJP-x-tCo359aR9stjlcvdtsesbbKCHG_ilIoTsWL6Ulgl0nETSBnbFhrCwISKE56JRF5cTzpzHTPLvrELjVxrJjOcjBCSFyyZRgjxKvIF8F4wnN1teFuyXTnMqIlv_2GX5H6wdpHDBZ5zoSiOFZQdbVNbBJg3xIqAPfG8edjzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
افشای ۱۲۴ میلیون پسورد و ۵۶ میلیون ایمیل؛ آیا اطلاعات شما هم لو رفته؟
پایگاه داده سرویس معروف Have I Been Pwned به‌تازگی آپدیت شده و آمار نگران‌کننده‌ای را منتشر کرده است. این بار هکرها مستقیماً به سراغ کامپیوترها و دستگاه‌های شخصی کاربران رفته‌اند و بدون اینکه کسی متوجه شود، حجم عظیمی از داده‌های حساس را سرقت کرده‌اند!
🔹
نکات مهم این نشت اطلاعاتی:
🔸
منبع سرقت:
این اطلاعات نتیجه هک شدن یک سایت خاص نیست؛ بلکه بدافزارهای مخرب، پنهانی روی سیستم‌ها (مخصوصاً ویندوز) نشسته‌اند و پسوردهای ذخیره‌شده، کوکی‌ها و داده‌های مرورگر را دزدیده‌اند.
🔸
خطر پنهان:
از آنجا که بسیاری از کاربران اصلاً متوجه آلوده شدن دستگاه خود نمی‌شوند، این سرقت اطلاعات می‌تواند تا مدت‌ها بدون هیچ ردپایی ادامه داشته باشد.
🔸
اقدام فوری:
همین حالا به وب‌سایت
Have I Been Pwned
سر بزنید و ایمیل خود را جستجو کنید.
🔸
راه‌حل‌های امنیتی:
اگر اطلاعاتتان لو رفته بود، سریعاً رمزهای عبور خود را تغییر دهید. همچنین برای جلوگیری از نفوذ، حتماً تایید دومرحله‌ای (2FA) را برای حساب‌های مهم خود فعال کنید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/iaghapour/2684" target="_blank">📅 17:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2682">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">💰
مدیرعامل همراه اول: قیمت فعلی اینترنت با قیمت واقعی آن هیچ سنخیتی ندارد!
مهدی اخوان، مدیرعامل همراه اول، در مجمع عمومی سالانه این اپراتور با گلایه از تعرفه‌های فعلی اعلام کرد که هزینه‌های سرمایه‌گذاری ارزی آن‌ها کاملاً مشابه اپراتورهای منطقه است، اما قیمت هر گیگابایت اینترنت در ایران بسیار پایین‌تر از آن کشورهاست.
پ.ن:
جناب مدیرعامل! اتفاقاً تو این مملکت خیلی چیزها هست که هیچ سنخیتی با هم ندارن؛ از کیفیت اینترنت شما و چیزی که واقعاً به دست ما می‌رسه بگیر تا درآمد بالای مردم منطقه و حقوق‌های پایین ما! از همه مهم‌تر، بین زندگی و رفاه شما و واقعیتِ زندگی مردم هیچ سنخیتی نیست!
اگه واقعاً کار براتون نمی‌صرفه ما هم راضی به ضررتون نیستیم، کلاً درِ این اپراتورها رو تخته کنید و جرم‌انگاری استارلینک رو بردارید تا ببینیم تو یه بازار آزاد اصلاً می‌تونید باهاشون رقابت کنید یا نه! واقعیت اینه که سودهای کلان این اینترنت انحصاری (پرو) حسابی به دهنتون مزه کرده و حالا با گرون کردن‌های نجومی و پشت‌سرهم، به هر دری می‌زنید تا جیب مردم رو خالی‌تر کنید. وگرنه این چیزی که دارید به ما می‌فروشید اصلاً اسمش اینترنت نیست؛ هر وقت یه اینترنت واقعی و بدون فیلتر دست مردم دادید، اون‌وقت پولش رو هم بگیرید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/iaghapour/2682" target="_blank">📅 21:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2680">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUlhdKi-zHCvK-Zvw1VNJVdJtdEOPjm5pmjNG2AlfkunIvZbl22TrmYApFubsFkbycfAg701A_iXrLoCjnGwW2Hcgku_rGsCOOUReypDnuJ3TYagRa1_aGGHHzPPHvorteX8h9KKiXVd32VFv9qn19D8GsD3ReliucUsDrfVwBqBp-sEO-oY_nk_CyLxF53zRcqEvdMTwDZuuKV7Zy2onbTWCBfVLpLsqFzoyaSVrkeU9YMW6LmZe4bI-YrfZPY6XhoLaEVLZdQ5q7_hUqsP9la69DSq4sY38DyuFlcXHOWxSDYK_NL_fvPtFb8D1a6vyA7k0vf18naVW5gbd6dCrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار خیلی مهم: خطر فریز شدن دارایی‌ها در صرافی‌های خارجی!
بچه‌ها، همونطور که تو تصویر می‌بینید، صرافی‌های خارجی یه اخطار خیلی جدی در مورد تراکنش با پلتفرم‌های تحریم‌شده توسط OFAC (دفتر کنترل دارایی‌های خارجی آمریکا) منتشر کردن.
⚠️
تو این هشدار صراحتاً اسم ۴ تا از صرافی‌های معروف ایرانی آورده شده:
🔹
نوبیتکس (Nobitex)
🔹
والکس (Wallex)
🔹
بیت‌پین (Bitpin)
🔹
رمزینکس (Ramzinex)
❌
مشکل چیه و چه خطری داره؟
این صرافی‌ها اعلام کردن که سیستم‌های ضد پولشویی (AML) به شدت تراکنش‌ها رو بررسی می‌کنن. اگه مستقیم با این پلتفرم‌های ایرانی تراکنشی داشته باشید، ممکنه حسابتون محدود بشه یا حتی کل دارایی‌هاتون رو فریز و مسدود کنن!
💡
حالا باید چیکار کنیم؟
به هیچ‌وجه انتقال مستقیم ارز بین صرافی‌های ایرانی و صرافی‌های خارجی انجام ندید. حتماً از کیف پول‌های شخصی (مثل تراست ولت، یا ولت‌های سخت‌افزاری) به عنوان واسطه استفاده کنید تا مشکلی برای سرمایه‌تون پیش نیاد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/iaghapour/2680" target="_blank">📅 16:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2678">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atpVTpRTkCCskcJM6liKdQkdbvnpRWRqvu5R2iiDEhWXVB47x07ULWlHftxEv7sTnl-hwoUJrgeR_YD8h78s1UeGlplqQkej8awgaPfDhqn79j8-J0OrAw0sQrCZPPRk1sWFIEH8eMQ8yM0sJvHyR8A_HlUdTzZwFK3pvxlQf5isqCPnOaOOzOAi1bcdCxrD8T_7aAVlNGKiVik5R6TcV580LyCsbwB5dGDD3VxcD-oCaTWLrChXrGwW8RaoEXam0_NAulH1_8yQR5hi3gVOYDznshCR5r0vAsaTvJ3dgxqCCjUvjEMeBVFHd3GqsksWmtkP-L2qGmH3fI056ZOrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل بین سرور ایران و خارج (۲ روش سبک و سریع)
😍
🔹
تو این ویدیو قراره با هم دو تا از ساده و سبک‌ترین روش‌های تانل زدن بین سرور ایران و خارج رو یاد بگیریم. اگه برای ساخت فیلترشکن شخصی‌تون دنبال یه راه ساده و بدون دردسر برای اتصال سرورها هستید، این آموزش دقیقاً همون چیزیه که نیاز دارید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/iaghapour/2678" target="_blank">📅 19:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2677">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⭕️
دسترسی مستقیم و بدون واسطه به اینترنت آزاد
🔹
کافی است آدرس subscription را در برنامه v2rayN/v2rayNG وارد کنید:
https://raw.githubusercontent.com/patterniha/Serverless-for-Iran/refs/heads/main/Subscription/Serverless-for-Iran.json
— نکات استفاده
👇🏻
۱. کانفیگ سرورلس برای اجرا نیاز به هسته Xray-core حداقل ورژن 26.6.1 دارد (حداقل v2rayNG v2.2.3)
۲. سرویسها و سایتهایی که ip آنها به طور کلی از سمت ایران بلاک شده با این روش مستقیم قابل دستیابی نیستند، همچنین از آنجایی که سرویسهای خارجی ip ایران را مشاهده میکنند، سرویسها و سایتهایی که ایران را تحریم کرده اند نیز با این روش مستقیم قابل دستیابی نیستند.
۳. در تنظیمات v2rayNG دقت کنید که Enable Hev TUN FEATURE فعال باشد و همچنین پورت پیشفرض 10808 را تغییر نداده باشید.
۴. از آپدیت بودن فایلهای جئو مطمئن شوید (قسمت Asset files در برنامه v2rayNG و قسمت Help-Check Update در برنامه v2rayN)
۵. برای تجربه بهتر پیشنهاد میشود IPv6 خود را فعال کنید (در تنظیمات v2rayNG تیک Enable IPv6 را بزنید و همچنین در صورتی که از اینترنت همراه استفاده میکنید باید IPv6 را در قسمت Access-Point گوشی خود فعال کنید)
۶. در اندروید برای عدم تداخل با (dns و sniffing) کانفیگ بهتر است Private DNS در تنظیمات اندروید و Use secure DNS در تنظیمات کروم خاموش باشد.
۷. از کانفیگها تست نگیرید، نتیجه‌ی تست ارتباطی با کار کردن یا کار نکردن این نوع کانفیگها ندارد.
🟢
به گفته یکی از بچه ها با روش زیر میتونیدمتصل بشید:
کاربر اگر فیک دی ان اس رو از تنظیمات برنامه روشن کنه سرویس هایی که آیپی ایران رو محدود و مسدود کردن مشکلش حل میشه و سایتا بالا میان.
⚠️
برای کارهای حساس از این روش استفاده نکنید!
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/iaghapour/2677" target="_blank">📅 12:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2676">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlJaBfboLt_7M-rHaRfalreqHOkgm3ky-Y4v7nN0G9jXzOfGnqxP8zffUZtS_JrctP3mj4u5grpfAYpVFp1qOQG3K5x0-BhrgXpPmCS8fw55TqpP0qvBgi2N3ZWQtGCmDy4L8xwdCSQL0qSY3WkVEX8xfY1yUdT6gQudt0Ov89DG0Frb58zJPQPOkTWxY2TxBW_uDjEiOl2BdR2o0Zw8-RwTRYEpLjubd4UkaH13OqCWhdvTZ29prQNMTc0xK9fFkaY7-rSUG1Lzwnbm7w6HoAM9mqIuuySZ8qfXGI4DNgXbp7MUiKRTnX-8lo4Eav11rGRIHtnsywxuu7Whr63U8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ادعای ایلان ماسک: پهنای باند استارلینک ۱۰۰ برابر می‌شود!
اسپیس ایکس از دستاورد جدیدی خبر داده و اعلام کرده که تعداد مشترکان اینترنت ماهواره‌ای استارلینک از مرز ۱۲ میلیون کاربر در ۱۶۰ کشور عبور کرده است. اما این تازه آغاز راه است و ایلان ماسک برنامه‌های بسیار جاه‌طلبانه‌ای برای آینده دارد.
🔸
انقلاب ماهواره‌های نسل سوم:
ماهواره‌های نسل سوم استارلینک، پهنای باندی ۱۰ برابر نسبت به ماهواره‌های فعلی ارائه خواهند داد. همزمان، سرعت پرتاب این ماهواره‌ها نیز ۱۰ برابر افزایش می‌یابد که در نهایت منجر به
افزایش ۱۰۰ برابری پهنای باند کل منظومه استارلینک
خواهد شد.
🔸
کاهش محسوس تاخیر:
ماهواره‌های نسل جدید قرار است در مداری پایین‌تر (فاصله ۳۵۰ کیلومتری زمین به جای ۵۵۰ کیلومتر) حرکت کنند. این کاهش فاصله، طبق ادعای ماسک، زمان تاخیر را به
نصف
کاهش می‌دهد.
🔹
وضعیت در ایران:
این جهش‌های تکنولوژیک در حالی رخ می‌دهد که در ایران، استفاده و خرید و فروش تجهیزات استارلینک همچنان ممنوع و جرم تلقی می‌شود. با این حال، در پی قطعی‌های اینترنت در یک سال اخیر، ده‌ها هزار ترمینال به صورت قاچاق وارد کشور شده است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/iaghapour/2676" target="_blank">📅 18:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2674">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✍🏻
دوستان، در حال حاضر بیش از ۷ اسکریپت (شامل اسکریپت‌های تانل و روش‌های مستقیم و رایگان) رو در دست بررسی داریم. هر کدوم که بدون مشکل جواب بده رو توی یوتیوب معرفی می‌کنیم. اما مواردی رو که به هر دلیلی (مثل محدودیت‌های دیتاسنتر سرورهایی که استفاده میکنیم و...) نتونیم خودمون ازشون جواب بگیریم، داخل کانال تلگرام معرفی میکنیم تا شما بتونید تست کنید.
ممنون از حمایت همیشگی شما.
💚</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/iaghapour/2674" target="_blank">📅 20:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2673">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واقعاً باید درِ این بانک‌های مزخرف رو گل بگیرن! سالی ۳ بار یا هک می‌شید، یا اپلیکیشن بانک کار نمی‌کنه، یا اختلال دارید و هزارتا کوفت و زهر مار دیگه! آخه مگه می‌شه بانک این‌همه بی‌در و پیکر باشه؟
😒</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/iaghapour/2673" target="_blank">📅 20:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2671">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCSpH2Lr6vbcsQmO1j69A0q3vm6DZh6o6AWHBuI5p5v6Z-FIhOY5ZRPpgJ0liA3g9HG4wCk55duNE0Uj3V1-8C3v1oXdJPE94iqiO7FufLd01x1cMVUNBUTW5B7buDI7Cp1-HV-cW9hvyItuRFkwwtKtUodMraHwBwZIhTzjHilrrEbAHu9GkA89vxYouJOERLmfMeqGFeoF7A9n5vH5nFIhcbb1B7h-WO4ToxSZ3bcpNTprf2QaH7H3lH8jQTDp0kzO8Wrt6E5nVv4fwju8E4DjJgJKHjCsNUYXHQuEEQrMGnD5oJIlYOtIXpLDHGx_dk1aZPOHNnA-yjdmQGPL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
درخواست حمید رسایی و ۱۱۹ استاد برای انحلال «ستاد ویژه فضای مجازی»
بیش از ۱۲۰ تن از اساتید حوزه و دانشگاه، و چهره‌های سیاسی از جمله حمید رسایی در نامه‌ای به رئیس قوه قضائیه و فقهای شورای نگهبان، خواستار ابطال فوری مصوبه دولت برای تشکیل «ستاد ویژه ساماندهی و راهبری فضای مجازی» شدند.
🔹
مهم‌ترین دلایل مخالفان:
🔸
تشکیل این ستاد ناقض جایگاه «شورای عالی فضای مجازی» به عنوان تنها نقطه کانونی سیاست‌گذاری است و یک ساختار موازی محسوب می‌شود.
🔸
به اعتقاد نویسندگان نامه، رئیس‌جمهور صلاحیت ایجاد نهادهای فراقوه‌ای با کارکردهای کلان حاکمیتی را ندارد.
🔸
واگذاری اختیار محدودسازی اینترنت به ستاد جدید، با صلاحیت قانونی (کمیته فیلترینگ) و دادستانی کل کشور در تعارض است.
🔸
ایجاد این ساختار جدید، مصداق تشکیلات غیرضروری بوده و تنها باعث افزایش لایه‌های تصمیم‌گیری در فضای مجازی می‌شود.
پ.ن: جالبه تو این مملکت انگار با فساد و رانتِ کسی کاری ندارن؛ اما وای به روزی که بخوان اینترنتی رو که دست مفسدها رو رو می‌کنه، یه ذره آزاد کنن!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/iaghapour/2671" target="_blank">📅 21:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2670">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stbLR5VMly5ShEM-7Rs8pjZSH0iuHRck1JvDOKcLYNCR0V6oYb_Mr1HuHTaeDmQ0Vi5ZRgi0MpOu94aG_gIwvULqfFjdSykkjOBZ2lV9EStkFucNn0H9tyZTKGEiw_UsXtKkYxQMeb2pqXKKCw9yLvJ6znAKOY7kGMzf65T39pAAkTA_KQ9jv0TFgnOoUSrRceoTJjmQzUfF638p9Prb_KjfZIEarvkwyIBdIOW86bCYgBQpXuV-n90JnsAwZCoZioJHzcRf4E2qT4g7cJfoEd-Ob8Ak5km-gbAwh3Brx9ouRx2IB488uaHhCEx2SC4_TskM9_haDawqFkQ4dVNv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
وزیر ارتباطات: محدودیت‌های اینترنت شفاف و زمان‌دار می‌شود / خسارت روزانه ۱۵ میلیون دلاری قطعی‌ها!
ستار هاشمی، وزیر ارتباطات در نشست خبری خود با انتقاد از وضعیت فعلی گفت: «در عصر هوش مصنوعی، دردناک است که هنوز دغدغه وصل بودن اینترنت را داریم.» وی تاکید کرد که قطعی اینترنت در فضای غبارآلود شایسته مردم نیست و سازوکار اعمال محدودیت‌ها باید تغییر کند.
🔹
چکیده مهم‌ترین صحبت‌های وزیر ارتباطات:
🔸
شفافیت و زمان‌بندی:
از این پس اگر قرار است محدودیتی ایجاد شود، باید مشخص باشد کدام نهاد و کمیته آن را تصویب کرده و
دقیقاً تا چه زمانی
ادامه دارد.
🔸
خسارت نجومی:
بر اساس گزارش مجلس، کشور روزانه ۱۵ میلیون دلار از قطعی اینترنت آسیب می‌بیند.
🔸
عادی‌شدن فیلترشکن‌ها:
استفاده از VPN که در گذشته قبح داشت، به دلیل سیاست‌های اشتباه به یک رویه عادی و روزمره برای کاربران تبدیل شده است.
پ.ن: وزیر مشکلی با محدودیت و قطعی نداره بیشتر داره میگه شما که داری قطع میکنی بگو تا کی که مردم اطلاع داشته باشن :)
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/iaghapour/2670" target="_blank">📅 21:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2668">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8b8D5Qs6_ocGAuxo5bcVVi06DQVyoLFDlYTUs1jjHIVcgYlvxHWsYvpyjL1bqfKqeEK6WTlaAc8_ejXhpGP8XDiLeNou0x5fbGoZthZY5Hg2wiwqpr8rsm8yBQoK81blVscvkc8NSIIcuOW94lKCVuB2O7hEKWG6T0eviVUJbU1PUjJ6hf6yJC8yP5scrtM6aVHvufWcrDXq_H-CQGKE3Yv2PeAh5HvA1xwym7vIaqn_3-eMkaXG6GK5LPhUtRVfNyzuuUAallBdbQ7v7p_8SASt8IbO9jUU5PTaJlSGC_An4yWG48vQxVWw7TEbi8FhTio2RSa_7diYfLl-8CyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای ساخت فیلترشکن شخصی با ۲ هسته در پنل پاسارگارد
🔥
🔹
تو این ویدیو قراره با هم یاد بگیریم چطوری یه فیلترشکن شخصی فوق‌العاده با استفاده از پنل پاسارگارد بسازیم. این پنل از 2 هسته Xray و وایرگارد ساپورت میکنه و همینطور از قابلیت نود هم پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پاسارگارد
#pasarguard
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/iaghapour/2668" target="_blank">📅 19:34 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2667">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=bHjE9SDXRCvJPJNci6uJakP5oLIu-OMQ1A0N068doG2URO54YJagnOeK60g4pTZhhdpB9yRs7RnrHlJXZTMuFpI3mgt-mhpapLK2Q3aFmjEKE7qvNf0NDN_UnFIiPuoFodBILs_4HbxAUiqihQWGBoktZ4V7OvvLpoanAg_rkfDHawRC9cUQOXgOFwYDWYDBFrV7oz7m2vHjXhmypCLbvEBfqU0R2VrX5paBanN0fv05N4LVuhQMje5_ne-lEIZq3zdIOIPQGCSWN0CB7UZdXovydXWB_Tw59novyKwpKR6Mt0zuoRRKKEQ1Lxz0eeu4iFTykf2cIvsHXN5ZuZvoCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127cc882e.mp4?token=bHjE9SDXRCvJPJNci6uJakP5oLIu-OMQ1A0N068doG2URO54YJagnOeK60g4pTZhhdpB9yRs7RnrHlJXZTMuFpI3mgt-mhpapLK2Q3aFmjEKE7qvNf0NDN_UnFIiPuoFodBILs_4HbxAUiqihQWGBoktZ4V7OvvLpoanAg_rkfDHawRC9cUQOXgOFwYDWYDBFrV7oz7m2vHjXhmypCLbvEBfqU0R2VrX5paBanN0fv05N4LVuhQMje5_ne-lEIZq3zdIOIPQGCSWN0CB7UZdXovydXWB_Tw59novyKwpKR6Mt0zuoRRKKEQ1Lxz0eeu4iFTykf2cIvsHXN5ZuZvoCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
چرا عنوان ویدیوهای یوتیوب یا زبان ویدیو برای بعضی‌ها انگلیسی شده؟!
سلام رفقا! جدیداً خیلی‌ها پیام دادید که چرا با وجود فارسی بودن ویدیوها، عنوان و توضیحات کانال رو به انگلیسی می‌بینید. یا اینکه حتی زبان ویدیو هم انگلیسی شده.
علت چیه؟
تقصیر هوش مصنوعی یوتیوبه! اگر زبان گوشی، لپ‌تاپ یا اکانت گوگل شما روی انگلیسی تنظیم شده باشه، یوتیوب به طور خودکار عنوان‌های فارسی و حتی زبان ویدیو رو براتون به انگلیسی ترجمه می‌کنه.
🛠
راه حل سریع فارسی کردن یوتیوب:
👇🏻
در اپلیکیشن موبایل:
🔹
وارد برنامه یوتیوب بشید و روی عکس پروفایلتون بزنید.
🔹
آیکون تنظیمات رو لمس کنید.
🔹
وارد بخش General و سپس App language بشید و زبان رو روی فارسی بذارید.
👇🏻
در نسخه وب (کامپیوتر/مرورگر):
🔹
سایت
YouTube.com
رو باز کنید.
🔹
روی عکس پروفایلتون در بالا سمت راست کلیک کنید.
🔹
گزینه Language رو انتخاب کرده و اون رو روی فارسی بذارید.
🎙
حل مشکل صدای انگلیسی (دوبله خودکار):
اگر وارد ویدیو شدید و دیدید صدای من انگلیسی شده، روی علامت چرخ‌دندهِ خودِ ویدیو بزنید، وارد بخش Audio track بشید و اون رو روی Original (فارسی) بذارید.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2667" target="_blank">📅 16:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2665">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در حال تست و ضبط چند ویدیو جدید هستیم.
👌🏻
ممنون میشم سوالات رو فقط در یوتیوب بپرسید و در بخش ربات ارسال نکنید.
🙏🏻</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/iaghapour/2665" target="_blank">📅 21:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2664">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqew99aNPzKeIeYmHGsxhpIw8JAUI0uvTY5AbnI-H4olmBFQI6pSV1mp6P2QZ1BayjPVRv0iEqN5Z1GEfjx8JnMvW_y3uuwOyDd9Ifi1GhfL5av3eEkMONYVwVso-ywBdzVG4b7ln7voj_Iau7Zel4s2pB7HVIyCep1iyLDPeh6hT5V-m2hEtBFHqEXxhd_D5LTL2z_rViX0i8TSbdKyUCdtnnOXCUEF0UXb4Wzr6NycZ931tr5g0q8uUUfDB4Sc1C1XKyN2fqt879FU4CxxXO4wI8s-8Py_xjmOJ2f9v4HffZMRBTNRmnkA9A0HAL6rlV-42wnKE06zztCK710yQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پولی شدن پیامک فعال‌سازی تلگرام برای برخی پیش‌شماره‌ها!
🔹
تلگرام در جدیدترین به‌روزرسانی‌های خود، سیاست سخت‌گیرانه‌ای را برای ثبت‌نام یا ورود کاربران در برخی از کشورها و پیش‌شماره‌های خاص اعمال کرده است. طبق گزارش‌های کاربران و تصویر منتشر شده، بخش جدیدی به نام
SMS Fee
به اپلیکیشن اضافه شده است.
❓
ماجرا چیست؟
تلگرام اعلام کرده که به دلیل بالا بودن آمار ساخت
حساب‌های جعلی (Fake Accounts)
و همچنین
هزینه‌های بسیار سنگین ارسال پیامک بین‌المللی
در برخی از کشورها، کاربران این پیش‌شماره‌ها باید هزینه پیامک ثبت‌نام خود را پرداخت کنند.
💵
کاربران برای دریافت کد تأییدیه مجبور هستند مبلغ
۱ دلار
پرداخت کنند. تلگرام این پرداخت را در قالب
خرید اشتراک ۱ هفته‌ای تلگرام پرمیوم (Telegram Premium)
ارائه می‌دهد.
پی‌نوشت: این محدودیت فعلاً برای تمام شماره‌ها نیست و تنها روی اپراتورها و کشورهایی که هزینه‌ی مخابراتی بالایی دارند یا سوءاستفاده از آن‌ها زیاد است، فعال شده. خوشبختانه
#ایران
تو این لیست نیست ولی اگه از شماره های مجازی استفاده میکنید باید حواستون به این موضوع باشه.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/iaghapour/2664" target="_blank">📅 00:10 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2663">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه چیزی میگم شاید باورتون نشه.
مردم الان بیشتر از اینکه نگران جنگ باشن نگران قطعی دوباره
#اینترنت
هستن.
کسب و کارهای آسیب دیده تا میان دوباره سرپا بشن اینترنت رو قطع میکنن یا اختلال میندازن و....
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/iaghapour/2663" target="_blank">📅 16:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2661">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO7qKShtsIHF6my7OrSQAjOGVKfEAlSAQsbAPP8VK-ZMLAKcXjz3pVYZh74OWtz0LQuibw-pKFEZWNwX0S_m2oloa-knJ28m9ApdUVPL1z2L34705OxbAuMHqSpJ9ms4sfhsPcx_Gs11McW3iSGTkTW9znJajbJomAacl-0rGHcZNqKBR2csCdT1hX1xENbKp14tIla-HGMGkVpFZwhfGpyEuvgBRDzXc_8HjAbkZi92MLF_GyBPUTFZQpqaTWeVXPg8H60lXYQ_m_2g0M-0GonHZnzhak32I-NBR2xOftXdtAETYPg3jdJMPk4ePZqVyIFnlBT4hUw9cneUZRJ69A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مدیرعامل آسیاتک: اینترنت دیتاسنترها هنوز وصل نشده است!
محمدعلی یوسفی‌زاده اعلام کرد اینترنت کاربران وصل است اما مراکز داده دسترسی کامل ندارند و شبکه به وضعیت عادی برنگشته است.
فقدان پاسخگویی:
پیگیری‌های زیادی انجام شده، اما مسئولان هیچ دلیل یا پاسخی برای این قطع بودن ارائه نمی‌دهند.
⚠️
مشکل اصلی چیست؟
اینترنت کاربران با اینترنت دیتاسنترها مسیر متفاوتی دارد. در حال حاضر کاربران به سایت‌های داخلی دسترسی دارند، اما
سرورِ خود این سایت‌ها
در دیتاسنترها به اینترنت جهانی وصل نیستند.
—
نتیجه این اختلال:
قطع شدن اتصال سرورها به ابزارهای حیاتی خارجی مثل گوگل، کلادفلر و گیت‌هاب (APIها).
— عدم امکان آپدیت، دسترسی به ریپازیتوری‌ها و سرویس‌های ابری (CDN).
📌
نتیجه:
اینترنت دیتاسنترها قطع است؛ یعنی پلتفرم‌های ایرانی از پشت صحنه به جهان متصل نیستند و زیرساخت فنی آن‌ها عملاً فلج شده است.
پ.ن: البته از وضعیت دیتاسنترهای دیگه اطلاعات زیادی در دسترس نیست.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/iaghapour/2661" target="_blank">📅 21:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2660">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qgcc8kbPfGWrN6SH8u7sVlSq7YvVtfp3ZAWY4QzH-GeRY0kVV8dsmGATsBAOsCXysKujE128rOAZdYzOnVq6-LiQCsd_2PHILO1npcCYhXcE0vcXw3J17JZdO8NvlETX-k8br-d8Q4LFWPSpv2O9r0Nf-wEBiHug1Idi7RhosyGj-bUP2AdTKrbGHbMQyca-MklQYN6cKy-casz7YGTF1cwjGwNefxwfBSB9AJf0zn_FtHYwFbfB0_l1MBkgUVJlOXEHAgVtUh-oiPmf3vQMQfemZj-jCYEiFCufuKfSTt3g7a8yhiWA1igJAWFMRii1jTLvz3FI6XIsctAWrwgQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرقت بی‌اجازه ترافیک کاربران؛ پشت‌پرده دسترسی ناگهانی به کلاد و اسپاتیفای چیست؟
دسترسی ناگهانی و بدون VPN به پلتفرم‌های تحریم‌شده‌ای مثل
کلاد (Claude)
و
اسپاتیفای
، حاصل لغو تحریم‌ها نیست؛ بلکه نتیجه
دستکاری پنهان و بدون اجازه ترافیک کاربران
توسط زیرساخت اینترنت کشور است.
🔍
لایه‌های فنی و عملکرد
روش کار:
دولت ترافیک کاربران را به سمت سرورهای خود هدایت کرده و از آنجا به مقصد پروکسی می‌کند. کارشناسان این کار را مشابه
حملات هکری DNS
می‌دانند که پیش از این در سرویس‌های رفع تحریم (مثل شکن و ۴۰۳) اما این‌بار به صورت اجباری و پنهانی اجرا می‌شود.
امنیت داده‌ها:
به دلیل پروتکل‌های امنیتی، دولت توانایی دیدن محتوای پیام‌ها (مثلاً چت با هوش مصنوعی) را ندارد و فقط می‌تواند ببیند کاربر از چه سرویسی استفاده می‌کند.
⚠️
پیامدها و خطرات
خطر مسدود شدن اکانت‌ها:
ارسال انبوه درخواست‌ها از چند آی‌پی مشخص، پلتفرم‌ها را حساس کرده و ریسک مسدود شدن حساب را بالا می‌برد.
اختلال فنی:
این دستکاری باعث قفل شدن مداوم اکانت‌ها در سایت‌های تخصصی و افت شدید کیفیت VPNهای اختصاصی (به دلیل پدیده تونل در تونل) می‌شود.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/iaghapour/2660" target="_blank">📅 20:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2659">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hN2glH1YAtkITiqEYUSAw7C-PSAFauT_LLbIDMcGNFwEAC7GZGtIjOqSx8ubujNT0Du_dYmdTS7-W1Z78AcJwQwz7w1NydVTJ2tepmK7JF3S7A1S-MK0EmyPr7UWqPWqbsytYgzcJav6MZ9YmQknwtrFVngjHb8EUC29elN7h-rgeu_-9X55Ftq_c-YZXQJbq8Kh8frtfXNgu_hC9grM9ofQPR3ZL3SHSeYbnXFXAS3hhi8G6n9yG0PDPENRaVZ4YJeEp1DQUHGBpYkIRZspg2rTz1odIETr_yFoytUM5gzmJZv6IqbnNfaaVaq6Q1kpFs0vnVkdu6iQLmS9oQl7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نصب خودکار داکر روی سرورهای ایران
اگر روی سرورهای داخل ایران داکر نصب می‌کنید، حتماً می‌دانید که به خاطر تحریم‌ها و اختلالات شبکه، باز کردن مخازن داکر و دانلود ایمیج‌ها مکافات است. این اسکریپت متن‌باز و امن، کل فرآیند نصب داکر را خودکار کرده و در انتها به شما اجازه می‌دهد از بین ۶ میرور ایرانی (ابرآروان، داکر آی‌آر، لیارا و...) بهترین را برای رفع تحریم انتخاب کنید.
💻
روش اجرا: کد زیر رو کپی کنید و در سرور اجرا کنید:
curl -fsSL https://gist.githubusercontent.com/ShahinDadashpour/35892443c09d582e53b36d09fb5a5df6/raw/install-docker.sh | sudo bash
🔗
لینک سورس کد در گیت‌هاب جهت بررسی
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/iaghapour/2659" target="_blank">📅 01:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTX43H1RiRRJCWutJOl3hRpx9RPlKGHLh2txRes610BI2LXuoIWqDJbWC_Ew2vxnGjfu_RzM5nPy2GKtc1WJg5EEdewFxPcp0iOvCXPouDp29BCtAUaHEdSbZMIUkgx4wrifQcjsVc1TlDAgDGGL_DmptrcSd80JlPI0ZNzAOFeBrNBuZLgXDrb73GS5a22LEzPaClQ53Uz4G7Hg07kVn-YNI-wsf3qK-B9dLr1EOXETFR1_niEafkPX0cKXwRZRZ2DQ1WZM9ZapzwFZRkln8a36u3KZPuTDCiaQArOnnN-rUol0YEbEX0IJzJZnPgsaP6qk2o4ANSl1pT6a5J_3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن بدون تانل و بررسی روش های موجود
🔹
خیلی‌ها فکر می‌کنن برای داشتن یک فیلترشکن شخصی حتماً باید درگیر دردسرهای تانل زدن بشن، اما تو این ویدیو تمام روش‌های موجود رو بررسی کردیم و بهتون آموزش دادم چطور بدون نیاز به تانل، یک فیلترشکن پرسرعت بسازید.
👇
در این ویدیو به چه مواردی اشاره شد:
— چرا تمام روش ها منتشر نمیشه؟
— چه روش هایی در شرایط سخت کار میکنه؟
— آموزش روش مستقیم ساخت فیلترشکن.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#ملی
#vpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/iaghapour/2657" target="_blank">📅 18:35 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Olt1_I0t3_ulDlRH2ffFH5g2Uby9Ln_iVKQnq0Bi0XLYxkKKmBEvX7aoycv1fXlEk05_5jtmcxII0Dz22OOlZxxaQYvfo6T5tJPAz9OELW2c7cy1KHJiciAQornGDfJBYmxMzVXa-daqS2danmJv4x-iXgx2QEzEUMJGoiBrfzi596ZVmYn4TQbX75w5EYiTj7-88jRYpgBIDgS2L6TatgdvquvIiTyC4sQPWHIlg1aFfznLGDGaWFUFggoi0ROUjG9KJ9-pnO7Lanv_ob0szOSs1oTE9fsQFgW4jbTrIP-d8VnUBLdRniCWcQS_iYxPt7KPQ19eQMI7i8ks1Kzf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بلوکه شدن ارز دیجیتال در خریدهای خارجی (CoinGate)
دوستان، یکی از کاربران هنگام خرید از سایت
Hostinger
با ترون از طریق درگاه
CoinGate
، متأسفانه به دلیل تحریم‌ها پولش مسدود شده است. طبق اعلام رسمی پشتیبانی این درگاه، به دلیل قوانین بین‌المللی، وجه بلوکه‌شده
به هیچ‌وجه ریفاند (برگشت) داده نمی‌شود!
⚠️
چرا شناسایی می‌شویم؟
درگاه‌های خارجی تراکنش‌ها را رهگیری می‌کنند. اگر IP شما نشت کند یا ارز را مستقیماً از صرافی‌های ایرانی به کیف پول خود (مثل تراست ولت) منتقل کرده باشید، به راحتی به عنوان کاربر ایرانی شناسایی می‌شوید.
✅
راه‌حل و پیشگیری:
—
هرگز
مستقیماً از صرافی ایرانی به درگاه‌های خارجی واریز نکنید.
— همیشه از
کیف پول واسط
استفاده کنید (ارز را از صرافی ایرانی به ولت اول، سپس به ولت دوم بفرستید و در نهایت از ولت دوم خرید کنید).
— هنگام پرداخت، حتماً از IP ثابت و معتبر استفاده کنید تا نشت IP نداشته باشید.
لطفاً این پیام را به اشتراک بگذارید تا سرمایه سایر دوستان به خطر نیفتد.
🙏
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/iaghapour/2656" target="_blank">📅 17:00 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">📢
دو نکته خیلی مهم برای شما دوستان عزیز
سلام بچه‌ها! امیدوارم حالتون عالی باشه. برای اینکه بتونم تو کانال بهتر راهنماییتون کنم و محتوای باکیفیت‌تری براتون بسازم، نیاز دیدم این دو تا نکته مهم رو باهاتون در میون بذارم:
۱. درباره سوال پرسیدن از ویدیوهای قدیمی
:
همون‌طور که می‌دونید تعداد ویدیوهای کانال زیاده و واقعیت اینه که من مو به مو یادم نمی‌مونه تو ویدیوهای ماه‌های گذشته یا سال‌های قبل، دقیقاً چه مواردی رو پوشش دادم یا چه جزئیاتی رو گفتم. پس اگر درباره یک ویدیوی قدیمی تو کامنت‌ها سوالی براتون پیش میاد، لطفاً
خیلی دقیق و با جزئیات
بپرسید. اگر ممکنه، مشکلتون رو کامل توضیح بدید یا حتی تایم‌لاین (دقیقه و ثانیه) اون بخش از ویدیو رو بنویسید تا سریع متوجه موضوع بشم و بتونم جواب درستی بهتون بدم.
۲. درباره تست روش‌های تانل
:
نکته دوم در مورد آموزش‌های تانلینگ هست. ببینید بچه‌ها، وقتی ما یک روش تانل رو معرفی می‌کنیم، منطقاً امکانش وجود نداره که اون رو روی
تمام
روش‌ها و پروتکل‌های دیگه (مثل وایرگارد، OpenVPN و...) تست کنیم. خیلی وقت‌ها تو کامنت‌ها می‌پرسید که «آیا این تانل روی فلان پروتکل هم جواب میده؟» راستش ما هم اطلاع دقیقی نداریم؛ چون زمان و زیرساخت تست کردن یک روش روی تک‌تک سناریوها وجود نداره. بهترین کار اینه که خودتون اون روش رو روی پروتکل مدنظرتون تست کنید و اتفاقاً نتیجش رو تو کامنت‌ها بنویسید تا بقیه بچه‌ها هم از تجربه‌تون استفاده کنند.
ممنون که مثل همیشه درک می‌کنید و با انرژی خوبتون همراه کانال هستید!
❤️</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/iaghapour/2655" target="_blank">📅 21:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2652">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رفقای عزیز سلام!
✌️
دارم روی یه ویدیوی خیلی کاربردی کار می‌کنم که سعی می‌کنم فردا یا نهایتاً پس‌فردا به دستتون برسونم. تو این ویدیو قراره به خیلی از سوالاتتون جواب بدم، ابهامات رو برطرف کنم و یه گپ و گفتی درباره شرایط فعلی داشته باشیم.
ضمناً خواستم یه تشکر ویژه بکنم بابت تمام حمایت‌هاتون؛ چه کامنت‌های پرانرژی‌تون تو یوتیوب و چه حضورتون تو شبکه‌های دیگه. مرسی که با تماشای ویدیوها (و صبوری کردن برای تبلیغات!) از کانال خودتون حمایت می‌کنید تا بتونیم با قدرت بیشتری به کارمون ادامه بدیم. دمتون گرم!
❤️</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/iaghapour/2652" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2650">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-text">⭕️
کدهای مخفی چت جی‌پی‌تی؛ ۸ ترفندی که پاسخ‌ها را متحول می‌کند!
بیشتر افراد از چت جی‌پی‌تی فقط مثل یک موتور جستجوی ساده استفاده می‌کنند و پاسخ‌های کلیشه‌ای می‌گیرند. اما کاربران حرفه‌ای می‌دانند که با اضافه کردن چند فرمان کوتاه، می‌توان نحوه تفکر و خروجی این هوش مصنوعی را کاملا تغییر داد.
🔹
ساده‌سازی مفاهیم (ELI5):
اگر موضوع علمی یا پیچیده‌ای را متوجه نمی‌شوید، در درخواست خود بنویسید «توضیح بده مثل اینکه ۵ ساله هستم (ELI5)». چت جی‌پی‌تی تمام اصطلاحات تخصصی را حذف و موضوع را به ساده‌ترین شکل بیان می‌کند.
🔸
استخراج چکیده (TL;DR):
اگر حوصله خواندن یک مقاله یا ایمیل طولانی را ندارید، متن را ارسال کنید و در انتها بنویسید «خلاصه کوتاه (TL;DR)» تا در چند جمله لپ مطلب را بگیرید.
🔹
خروجی جدولی (FORMAT: TABLE):
به جای دریافت پاراگراف‌های نامرتب، مثلا هنگام مقایسه دو محصول، عبارت «نمایش به صورت جدول (FORMAT: TABLE)» را اضافه کنید تا اطلاعات کاملا منظم و خوانا تحویل داده شود.
🔸
کشف نقاط ضعف (DEVIL’S_ADVOCATE):
یک ایده کاری دارید؟ با اضافه کردن عبارت «وکیل مدافع شیطان»، هوش مصنوعی تمام دلایل احتمالی شکست ایده و نقاط ضعف آن را بی‌رحمانه به شما گوشزد می‌کند.
🔹
درخواست اطلاعات ناقص (MISSING_INFORMATION):
به جای اینکه هوش مصنوعی با اطلاعات کم شما یک جواب ناقص بسازد، عبارت «ابتدا اطلاعات ناقص را مشخص کن» را بنویسید. با این کار، چت جی‌پی‌تی ابتدا سوالات ضروری را از شما می‌پرسد تا دقیق‌ترین خروجی را بسازد.
🔸
تحلیل گام‌به‌گام (CHAIN_OF_THOUGHT):
با استفاده از دستور «تفکر زنجیره‌ای»، هوش مصنوعی مجبور می‌شود مراحل استدلال و حل مسئله را قدم‌به‌قدم به شما نشان دهد که خطای منطقی پاسخ‌ها را به شدت کم می‌کند.
🔹
شبیه‌ساز مصاحبه شغلی (MOCK_INTERVIEW):
با نوشتن دستور «مصاحبه شبیه‌سازی‌شده برای موقعیت...»، چت جی‌پی‌تی نقش یک مصاحبه‌گر را می‌گیرد، مرحله‌به‌مرحله از شما سوال می‌پرسد و پاسخ‌هایتان را ارزیابی می‌کند.
🔸
ریست کردن حافظه (IGNORE_PREVIOUS):
وقتی مکالمه طولانی می‌شود و هوش مصنوعی گیج می‌زند، با فرمان «بازنشانی دستورهای قبلی» به او بگویید کل پیام‌های قبلی را نادیده بگیرد و با یک نقش جدید شروع به کار کند.
با استفاده از این دستورات ساده، می‌توانید هوش مصنوعی را از یک ربات پاسخ‌گوی ساده، به یک مشاور، تحلیلگر و همکار حرفه‌ای تبدیل کنید.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/iaghapour/2650" target="_blank">📅 22:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2648">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYyJDi8s0HPni5WCsO6zeZnLnZaw7P0MqlHIhsCTvd2jfBCnC0wlRs0VwtZuXZb6jdE115EhZaXmKMK98_NkfsEcn6qP7fHUndtSrsi3QZzw4Lh81nLcMDogKUdmNLG3CtmzyHDxn4T3jI9qoNn3PvmPPJM3XtOam_UM1OopZF7lREhu7Uw_rjYDWO8cyE68IrNVbiTJEAE6QTZkrqYpVrySwuilIFu5xE4xefXKuEl61qEMnjSDNQaq8_ES2cvUFQW6Jp75gjNGxwFLopVTi_RxbL7HZqajyEUTMP2EAXeeE2ygNPExJygqds5iMiUI0gBXbPgqpTyTh1gPj4fthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی GenyConnect؛ جایگزین مدرن v2rayN برای مدیریت پروکسی
نرم‌افزار GenyConnect یک کلاینت تونلینگ و VPN مدرن (با کاربردی شبیه به برنامه محبوب v2rayN) است که با تمرکز بر عملکرد بالا، حریم خصوصی و کنترل دقیق ترافیک طراحی شده است. ویژگی مهم این ابزار، وابسته‌نبودن به یک پروتکل خاص است؛ به این معنی که می‌تواند به عنوان یک بستر یکپارچه برای موتورهای مختلف تونلینگ عمل کند.
🔹
مسیریابی پیشرفته:
امکان تعیین مسیر ترافیک بر اساس لیست سفید، دامنه‌های خاص، و حتی مسیریابی در سطح اپلیکیشن‌ها و پروسه‌های سیستم.
🔸
سبک و شفاف:
این ابزار با کمترین مصرف منابع سخت‌افزاری کار می‌کند و اطلاعات کاملی از وضعیت شبکه، لاگ‌های زنده و آمارهای لحظه‌ای ترافیک را به شما نمایش می‌دهد.
🔹
انعطاف در پلتفرم‌ها:
برخلاف برخی کلاینت‌ها که فقط مختص یک سیستم‌عامل هستند، این برنامه به صورت یکپارچه برای
ویندوز، مک، لینوکس و اندروید
در دسترس است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/iaghapour/2648" target="_blank">📅 21:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2647">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymq9jSaB6kDq4kw06ULLngdCJCU7vJIHQb0e_KuqNbYZFwjgHP4PtNvKMpSGce0ySicuraA9VIH9T9Wq6xqKqrquDqTkPYhe4Qrs2xtzDXdscamzwBoJmoppmGKpEtBtK0uy1FEV0_5K82Z6Df3cLm3ytZkue-Tl-SPZkg-oWwtTNZ4fijogmS1vZuN4MzRQ-dSVH4yiylKL-NfS8p6eBgpe1D-s3Jcho0Ncd3sHm-yHc6GGAHkO4emYNAlzw22ryjISCOfPrVHx_j8HiYhxG2RJzo6ez8xdjfWofmNIVZh58OFjQiSoKfuFiB5kUaQgODALXri1s07rqsHCeUXPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تون‌کوین به (Gram) تغییر نام می‌دهد!
پاول دورف در کانال رسمی خود خبر بسیار مهمی برای کاربران و سرمایه‌گذاران شبکه TON اعلام کرد. بر اساس این اطلاعیه، ارز دیجیتال بومی این شبکه قرار است با یک ری‌برندینگ بزرگ، نام فعلی خود را کنار گذاشته و به نام اصلی و اولیه‌اش یعنی Gram تغییر کند.
نکات کلیدی که دورف در این پست به آن‌ها اشاره کرده است:
🔹
بازگشت به ایده اولیه:
دورف یادآوری کرده که Gram نام اصلی ارز شبکه در اولین وایت‌پیپر این پروژه بود. او این اتفاق را بازگشت به ریشه‌ها و شروع یک فصل جدید توصیف کرده است.
🔸
زمان‌بندی انتقال:
فرایند این تغییر نام و انتقال، حدود ۳ هفته زمان خواهد برد.
🔹
نام بلاک‌چین تغییر نمی‌کند:
با وجود تغییر نام ارز بومی (از Toncoin به Gram)، نام خود شبکه بلاک‌چین همچنان TON باقی خواهد ماند.
🔸
قدم چهارم از یک نقشه راه:
این ری‌برندینگ تنها یک تغییر اسم ساده نیست، بلکه به گفته دورف، راه را برای اتفاقات مهم بعدی هموار می‌کند و قدم چهارم از یک برنامه ۷ مرحله‌ای برای «عظمت دوباره بخشیدن به TON» است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/iaghapour/2647" target="_blank">📅 21:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2646">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUz67nDc0Jz92JtBINc2c9lkdS9qpJ_GwjjwqS7h0H_TEuquGIbg3Zqy2RYE8nBawb9NA6ZHPLR0jnMKKE9vctfrdZlOTECsrSOIsT6_aN_tIBI19V3VTbLpNgB5mah0SjClh_JB5ibMFHhZU8t6RXyPCYe9cN56-wNVMD7e2ylx6pOI8NOAmv-9qEdvT_qyXJ0N9v3ciISRlCuj4OHK5js-cyXTyfAE51-8ESpF8VrpMqQneTf3vTnQBHnflWkMwZrfQxK5NrDZhrwCqEJYICEkAneMyWEnWhXGjkyGPIFxWS5JZVthR-pOv6AyX894FJHX5dVQZwLJj8e5EJYjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اسکنر IP سفید کلودفلر با نوا رادار
🔹
نوا رادار یک
اسکنر IP دسکتاپ
است که با Wails v3 (بک‌اند گو + فرانت ری‌اکت/تایپ‌اسکریپت) ساخته شده. این برنامه رنج‌های IP کلودفلر را از منابع متعدد اسکن می‌کند، تأیید پروتکل واقعی (TCP + TLS handshake) انجام می‌دهد و IPهای سالم را مرتب‌شده بر اساس سرعت تحویل می‌دهد.
—
اسکن چندمنبعی
— ۹ منبع IP قابل انتخاب
—
تأیید دو مرحله‌ای
— اسکن سریع TCP → تست عمیق TLS
— مرتب‌سازی بر اساس سرعت
— قابلیت انتخاب پورت
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/iaghapour/2646" target="_blank">📅 16:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2644">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">IP List -- @iAghapour.zip</div>
  <div class="tg-doc-extra">4.7 KB</div>
</div>
<a href="https://t.me/iaghapour/2644" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
آی‌پی ها و فایل html مربوط به ویدیو
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/iaghapour/2644" target="_blank">📅 20:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2643">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNb0wnVTQdhyPM23_VK6L-U-fu-o4_cpYomcXmwH89urFiZ9JPQzbQbFnYx4lU30BUXiqU8ncG2KfthKWUM4l4ufj6S8C-jJ_jYb6o6i6HoSUgwGtjqTu3_iJdlrdHtp7j7L7JwYAfVfC2UnGdNgoxwKs9wTFyllVgjCh605w7jVoG8ytPVUWXnPTLv4qSqLXh15Qt0oZX3OIbeeJwC8jcm8kGyAJHCp0RPNVPhAl_p2CqlShjf4lUclSXOM6YmqNpoS7B8cBNorFjENhnTVTSdcVm9JHqgbsyDXC7xCG5Fr_E3heQYupTOakaAcN5vQ6O4NGEaNwqAWUd3qWMRn2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت فیلترشکن پرسرعت و رایگان با ورکر کلودفلر (تست شده)
🔹
در این ویدیو به صورت قدم‌به‌قدم بهتون آموزش دادم که چطور با استفاده از Cloudflare Workers یک فیلترشکن کاملاً رایگان، و پرسرعت برای خودتون بسازید. این روش کاملاً تست شده و می‌تونید به راحتی روی گوشی و کامپیوتر ازش استفاده کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#رایگان
#پروکسی
#نوا
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/iaghapour/2643" target="_blank">📅 19:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2642">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJIEleOzKFzF6cWbZjJsCDBlOi0f52_4-MYS7o8MkPl3nZbJXanJrKJNKGbyH-V7BRViM4tTCYUFDGAw4t1O4q6Nv_YA6Yj6xSrnKRiFmXdJCaO2Kulunoc7JAtccDb-cX3R0tw8WHsrNPA8YcTZkS3ZIkRtqW4XC3Gm9pVa6Yf66UnkhHQ38sll1djNkcPxew50giZN7ib_TrgUTcR1Gz-MMXSDOfHi954WowVoT3uM4TJBkqpPU-9wqLrSL2b0QLNIdQIJ2VKwSqXvkFwpIzx_3EiHcbCChHgedX94G6ADacF78Yu822_wKkfC1GU81EryIa4gyH1mXEamZ8l3Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ ویندوز ۱۱ منتشر شد؛ پرسرعت‌تر و هوشمندتر!
مایکروسافت به‌تازگی آپدیت جدید ویندوز ۱۱ (نسخه‌های ۲۴H۲ و ۲۵H۲) را با تمرکز بر افزایش سرعت و هوش مصنوعی منتشر کرد.
مهم‌ترین تغییرات این به‌روزرسانی:
🔹
اشتراک‌گذاری صدا:
امکان اتصال هم‌زمان دو هدفون بلوتوثی مجزا به یک سیستم برای تماشای فیلم یا گوش دادن به موسیقی.
🔸
دوربین مشترک:
دسترسی هم‌زمان چند نرم‌افزار به وب‌کم بدون مسدود شدن تصویر.
🔹
افزایش سرعت و جستجو:
ارتقای چشمگیر سرعت منوی استارت و اجرای برنامه‌ها، به همراه امکان پیدا کردن سریع فایل‌ها با جستجوی تنها دو حرف.
🔸
پایش هوش مصنوعی و باتری:
نمایش دقیق میزان مصرف پردازنده عصبی (NPU) در تسک‌منیجر و بهینه‌سازی مصرف انرژی لپ‌تاپ‌ها در حالت استندبای.
این آپدیت با رفع خطاهای ناگهانی و بهبود سیستم امنیتی Windows Hello، تجربه بسیار روان‌تری ارائه می‌دهد و در ژوئن ۲۰۲۶ به‌صورت خودکار برای همه کاربران فعال خواهد شد.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/iaghapour/2642" target="_blank">📅 20:25 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2640">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/iaghapour/2640" target="_blank">📅 21:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2639">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEJGjJVjO3y_5Gdng_POFsUmMEL8OTxeekhoeeQHV9zskvGo3CEq0hVN5A4tnCA-vHQT-tYFzv4XU-QkXnrah0vGlguSiTQKY1BAg0XBHvf4ok8jbEiHdDcupCKsxMEtBM42y082bv198oRCrwRBiCJ1-huSieb9D3FygsnliUBVztVem7MVQJJTQjwunRSYIShwon81TDKXOI1IOnC4BvfN0shSLaAlFtPWWkJ1xAGoBulmzp9-7lCyOlhn2GZrerzoevIfWJYrrB9RIgCihIF8pRMkZNoYLp69EOVZZO3KPYBccLxm7pqTaL3geXSILXzc9_RTnqkCiFWWARpjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم ایران در حال برگشتن به تلگرام
😀</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/iaghapour/2639" target="_blank">📅 20:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2638">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">💢
وضعیت اینترنت جوری شده که وقتی نت ملی بود فیلترشکن ها راحت تر متصل میشدن!
راستی گوگل پلی و اپ‌استور در دسترس قرار گرفتن و البته ویندوز آپدیت و...</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/iaghapour/2638" target="_blank">📅 20:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2637">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/iaghapour/2637" target="_blank">📅 22:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2636">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
بچه ها میگن انقدر پهنای باند دیتاسنتر ها پایین هستش که اکثر روش های تانل که اجرا میکنن سرعت بدی داره یا دچار قطع و وصلی و اختلال زیاد هستش.
خیلی به روش تانل بستگی نداره بیشتر مشکل پهنای باند ضعیف دیتاسنتر ها مربوط هست.
امیدوارم در روزهای آینده وضعیت بهتر بشه.</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/iaghapour/2636" target="_blank">📅 13:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2634">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">میبینم که رو فیلترشکن ها تخفیف زدن :)
هر گیگ رو 10 و 20 هزار تومن دارن میفروشن :)
پولی که بعضی از افراد به جیب زدن تاجر ها نزدن. طرف داخل سرور ایران سایت فروش فیلترشکن داشت! قعطی نداشت. بالای 10 هزار ممبر داشت. اوایل حتی درگاه ریالی داشت. بعد بعضی ها انتظار دارن ما باور کنیم اینا به جایی وصل نبودن!</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/iaghapour/2634" target="_blank">📅 21:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2633">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭕️
چند خبر کوتاه از رسانه ها
🔸
معاون وزیر ارتباطات در پاسخ به زومیت در خصوص زمان بازگشایی اینترنت سیار نیز گفت: «امروز اینترنت همراه نیز وصل خواهد شد.»
با توجه به این اظهارنظر باید منتظر بازگشایی اینترنت همراه تا پایان امروز، سه‌شنبه ۵ خردادماه، در دسترس کاربران قرار بگیرد. هم‌چنین، طبق اعلام‌های قبلی، تا فردا روند بازگشایی اینترنت به وضعیت پیش از دی‌ماه ۱۴۰۴ تکمیل خواهد شد.
🔹
نت‌بلاکس بازگشت بخشی از اینترنت ایران را تایید کرد؛ سطح اتصال به ۳۴ درصد رسید
🔸
چه ‌وب‌سایت‌هایی در دسترس قرار گرفته‌اند؟ /دیجیاتو
ویکی‌پدیا
اپ‌استور
پینترست (Pinterest)
کنوا (Canva)
نوشن (Notion)
تردز (Threads)
کالاف
CallofDuty.com
پابجی (Pubg)
یاهو
دراپ باکس
پلی استیشن
ایکس‌باکس
استیم
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/iaghapour/2633" target="_blank">📅 18:31 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2632">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/iaghapour/2632" target="_blank">📅 18:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2631">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اینترنت بین‌الملل وصل بشه یجوری از اینترنت استفاده میکنم اختلال بخوره دوباره قطع بشه.
🫠
گوشی باید آپدیت بشه.
ویندوز باید آپدیت بشه.
لینوکس باید آپدیت بشه.
برنامه ها باید آپدیت بشه.
و...
حس میکنم شما هم با من هم نظر هستید
🫣
😁</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/iaghapour/2631" target="_blank">📅 10:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2630">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
این روزا انقدر شایعه و خبر بی‌خود درباره وصل شدن اینترنت پیچیده که واقعاً حس و حال خبر زدن در موردش رو ندارم.
با این حال، سعی می‌کنم اسکریپت‌هایی که زحمت کشیدید فرستادید رو حتماً بررسی کنم، به هر حال از دست رو دست گذاشتن که بهتره. راستش با این وضع زندگی، اصلاً هیچ انرژی و انگیزه‌ای برای آدم باقی نمونده.</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/iaghapour/2630" target="_blank">📅 21:34 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2628">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VVF3gYIvpgLC8GmzGWIK99SiqeKjMYn4ujXEkG9rAhh10NAFWbfhG48xB_-6VkOHhB7HGVcPQqlTcZgpGSydTEPULlIYBfmM79A6VCUTK4v8JpiYDr6lwRHWsLMAyxtMaCivLWX0tes-sH659T2DhBWito7WjoaAdo92ED7bbSIWOtBDOE1-0Rcgyo3QWRWT7MWD9AZeFSlFzJ4Nk0eb8AYYF-0A1hYL5s-P8oCyd0a4FSl8JiVSEiBssoJzD7yqX3bwowRSgDMKzC2QaP7IJDd5QgnuIUufc1urdrCh6fsUqksOrI03KV5a9uNlMoKKEYtEE-ouv6aKZbHIghRxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت جدید کلاینت اندروید GooseRelayVPN
🔹
این مخزن، کلاینت اندروید GooseRelayVPN است که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد.
🛠
پایداری و رفع کرش
‏
🌐
رفع کامل لو رفتن آی‌پی (IPv6 Leak) با موتور جدید tun2socks gVisor FakeDNS.
‏
🎛
پیاده‌سازی کامل Quick Settings Tile.
‏
📊
نمایش کاملاً دقیق سرعت و حجم مصرفی.
‏
🗂
اضافه شدن حالت Bypass به بخش Split-Tunneling.
‏
❄️
رفع فریز شدن برنامه در پس‌زمینه.
‏
📜
اصلاح پرش ناگهانی اسکرول لاگ‌ها و بازطراحی کارت وضعیت اتصال در صفحه Home
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/iaghapour/2628" target="_blank">📅 20:41 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2627">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭕️
رکورددار تاریکی دیجیتال: ایران طولانی‌ترین قطعی اینترنت جهان را تجربه می‌کند!
روزنامه معتبر اسپانیایی «ال‌پایس» در گزارشی تکان‌دهنده اعلام کرده است که ایران با گذشت حدود ۸۰ روز خاموشی دیجیتال، رکورد طولانی‌ترین قطعی سراسری اینترنت در تاریخ یک جامعه دیجیتال را به نام خود ثبت کرده است. این محدودیت‌ها که ابتدا با توجیه شرایط امنیتی و جنگی آغاز شد، همچنان ادامه دارد.
طبق گزارش این رسانه و به نقل از نت‌بلاکس، این وضعیت حالا حتی از قطعی طولانی‌مدت اینترنت میانمار در سال ۲۰۲۱ نیز فراتر رفته و زندگی میلیون‌ها ایرانی را در بن‌بست قرار داده است:
🔹
آوارگی برای یک اتصال پایدار:
ال‌پایس داستان تلخ افرادی را روایت می‌کند که برای حفظ شغل خود مجبور به مهاجرت موقت شده‌اند. مانند معلم زبانی که برای رهایی از اضطراب قطعی اینترنت، با هزینه ۴۰۰ دلار در ماه به زیرزمینی تاریک در ارمنستان پناه برده است.
🔸
ضربه مهلک به کسب‌وکارهای زنان:
تداوم این اختلالات، آسیب‌های ویرانگری به مشاغل کوچک وارد کرده است؛ به‌ویژه کسب‌وکارهایی که توسط زنان اداره می‌شوند و حیات آن‌ها کاملاً به پلتفرم‌های آنلاین و شبکه‌های اجتماعی گره خورده بود.
🔹
فلج شدن زندگی روزمره:
از کار از راه دور و تبادلات مالی گرفته تا ساده‌ترین ارتباطات انسانی و دسترسی به اطلاعات، همگی تحت تأثیر این محدودیت‌های بی‌سابقه مختل شده‌اند.
گزارش این روزنامه نشان می‌دهد که جهان در حال تماشای انزوای دیجیتال جامعه‌ای است که شهروندانش برای دسترسی به ابتدایی‌ترین حق ارتباطی خود، ناچارند هزینه‌های سنگین روانی، مالی و حتی مهاجرتی بپردازند./ دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/iaghapour/2627" target="_blank">📅 16:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2625">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS8-f4H7BgmN3OR8HMbqA0xnRTykwO-e6bai6kGxAQcqu8AGYEoSFZKaPR6UJ9GtnqIaNtUxmE7_H4kS2WBWp_oF4pkbnFCgKhyhoVxnn5ti_0wRt75hypr-xWgBKgyTNX0jtbcrgSAw25vtSFVrzdXHMMt39qswN8TIoM9zLgAdws2d5BJz8Q9NZYO3MBN0ayJ53UxP4dF9jr3hwVt860-5FYK2p0OIj7cnlnAGR4bBkl5B75dCiB6PDpUS9J_Z7rYCdgjA2SIEYLN46py21yETWVvoDhh-4csyKU8BDK4mUKrSZrqwUko9cgDtOG6Gew1u_NZPtJrltH0CvQfxZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پروژه XPlex؛ راه‌حل هوشمندانه برای جلوگیری از قطعی و پکت‌لاس کانفیگ
اگر از کانفیگ‌های v2ray استفاده می‌کنید و پایداری اینترنت در کارهای حساسی مثل آزمون‌های آنلاین، جلسات ویدیویی یا ریموت‌ورک برای شما حیاتی است، پروژه جدید XPlex یک راه‌حل فنی و کاربردی برای شما دارد.
منطق این اسکریپت ساده اما بسیار کارآمد است و به شما کمک می‌کند تا یک اتصال بدون قطعی را تجربه کنید:
🔹
استفاده هم‌زمان از چند کانفیگ:
منطق کلیدی این پروژه این است که اگر چند کانفیگ v2ray داشته باشید، اسکریپت به صورت هم‌زمان از آن‌ها استفاده می‌کند و ترافیک شما را روی کانفیگی می‌اندازد که کمترین پینگ ممکن را دارد.
🔸
خداحافظی با پکت‌لاس و تایم‌اوت:
این ابزار برای افرادی که کارهای حساسی دارند و ثانیه‌ها برایشان مهم است طراحی شده؛ مثل شرکت‌کنندگان در آزمون‌های آیلتس آنلاین، جلسات کاری با خارج از کشور و...
🔹
هزینه مصرف حجم:
باید توجه داشته باشید که به دلیل ماهیت کارکرد این ابزار، مصرف ترافیک و حجم v2ray شما تقریباً دو برابر خواهد شد که بهای به دست آوردن یک اینترنت کاملاً پایدار است.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2625" target="_blank">📅 20:54 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2623">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">⭕️
نماینده مجلس: ۹۰ درصد مردم با قطعی اینترنت مشکلی ندارند!
علی یزدی‌خواه، نایب‌رئیس کمیسیون فرهنگی مجلس صراحتاً اعلام کرد که اینترنت جهانی فعلاً بازگشایی نخواهد شد و مسئولان به این نتیجه رسیده‌اند که اتصال مجدد آن به صلاح نیست. او مدعی شده که با پلتفرم‌های داخلی، احتیاجات اکثریت جامعه برآورده شده است!
این اظهارات نشان‌دهنده اصرار بر ادامه سیاست اینترنت طبقاتی و نادیده گرفتن نارضایتی‌های عمومی است:
🔹
انکار نارضایتی‌ها:
این نماینده مدعی است به عنوان نماینده مردم، مراجعات مکرری برای اعتراض به قطع اینترنت نداشته و ۹۰ درصد مردم هیچ مشکل عمده‌ای با این وضعیت ندارند!
🔸
رسمیت یافتن اینترنت پرو:
به گفته او، تا کنون به بالغ بر یک میلیون نفر از افرادِ واجد صلاحیت (مثل تجار و دانشگاهیان) دسترسی به «اینترنت پرو» داده شده و هر قشری که نیاز داشته باشد هم می‌تواند آن را پیگیری کند.
🔹
کوچ اجباری به پلتفرم‌های داخلی:
او مدعی شد که ترافیک شبکه‌ها نشان می‌دهد بیشتر کسب‌وکارها به پلتفرم‌هایی مثل روبیکا و سروش کوچ کرده‌اند و تنها یک «اقلیت ناچیز» باقی مانده‌اند که آن‌ها هم بستر مشخصی برای پیگیری دارند.
در حالی که مسئولان از پایداری وضعیت فعلی و رضایت مردم سخن می‌گویند، بخش بزرگی از جامعه، کسب‌وکارها و متخصصان، اینترنت طبقاتی و محدودیت‌های فراگیر را تلاشی برای حذف کامل دسترسی آزاد به دنیای دیجیتال می‌دانند. / زومیت
پ.ن: اینا نماینده کدوم مردم هستن؟ 90 درصد مشکل ندارن؟ عجب!
حالا فارق از اینکه این ادعا از اول تا آخر دروغ هستش ولی من قبلا هم خواهش کردم اگه مجبور نیستید وارد شبکه های داخلی نشید! اگه مجبور نیستید لطفا سیم‌کارت پرو نخرید! اینا واقعا فکر میکنن مردم به ایتا و بله علاقه دارن! متوجه نیستن خیلی ها به اجبار مهاجرت کردن! در غیر اینصورت کی این اپلیکیشن ها رو به تلگرام و اینستا ترجیح میده؟
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/iaghapour/2623" target="_blank">📅 19:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2622">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
دوستان عزیزی که درخواست معرفی افراد معتبر برای خرید فیلترشکن دارید؛ طبق بررسی و نظرسنجی که در
این پست
قرار دادیم، با چندین نفری که از سال‌های قبل همکاری داشتیم صحبت کردیم و ازشون یکسری درخواست‌ها داشتیم؛ از جمله ضمانت بازگشت پول و اینکه مبلغی رو به عنوان ضمانت پیش ما بگذارند.
به همین دلیل ۹۰ درصدشون قبول نکردن و فقط تعداد محدودی پذیرفتن که هفته پیش یکی از اون‌ها رو بهتون معرفی کردیم. بازم اگه کسی از افراد قدیمی شرایط ما رو قبول کنه حتماً معرفی می‌کنیم.
افرادی که به ما تبلیغ می‌دن می‌دونن چقدر تو تبلیغات سخت‌گیر هستیم حالا در هر موضوعی باشه. بیش از ۳۰ درصد کسانی که پیام می‌دن، چون کانال قدیمی یا کاربر زیادی ندارن یا سایت معتبری ندارن، با نهایت احترام تبلیغشون رو اصلاً قبول نمی‌کنیم.
🔹
با این حال بازم سعی می‌کنیم همین یکی دو تا فردی که می‌شناسیم و شرایطمون رو قبول کردن بهتون معرفی کنیم؛ البته اگه خودشون دوباره قبول کنن تبلیغ بدن :)
ممنون میشم افراد جدید برای تبلیغات در زمینه فیلترشکن فعلاً پیام ندن. شرایط رو کامل در
این پست
براشون توضیح دادیم.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/iaghapour/2622" target="_blank">📅 21:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2621">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⭕️
اعتراف رسمی دولت: ۷۰ درصد مطالبات مردم، رفع محدودیت‌های اینترنت است
معاون اجرایی رئیس‌جمهور صراحتاً اعلام کرد که طبق نظرسنجی‌های نهاد ریاست‌جمهوری، بیش از ۷۰ درصد گلایه‌ها و خواسته‌های مردم به محدودیت‌های اینترنت مربوط می‌شود. او تأکید کرد که سیاست پایدار کشور نباید بر مبنای فیلترینگ باشد.
نکات کلیدی سخنان معاون رئیس‌جمهور درباره وضعیت اینترنت:
🔹
تصمیمات اضطراری باید تمام شوند:
محدودیت‌های اخیر به دلیل شرایط خاص امنیتی و جنگی بوده، اما تصمیمات دوران اضطرار نباید دائمی شوند و سیاست پایدار کشور نمی‌تواند بر محدودسازی بنا شود.
🔸
اعتراف به شکست فیلترینگ:
تجربه عملی نشان داد محدودیت‌های فراگیر ارتباطی به نتایج مورد انتظار منجر نشده و استفاده گسترده از فیلترشکن‌ها اثربخشی این محدودیت‌ها را از بین برده است.
🔹
حق آگاهی مردم:
اعتماد عمومی مهم‌ترین سرمایه است و مردم حق دارند بدانند محدودیت‌ها بر چه مبنایی اعمال می‌شود، چه دامنه‌ای دارد و تا چه زمانی ادامه خواهد داشت.
به گفته قائم‌پناه، کشور به یک تفاهم ملی در حوزه ارتباطات نیاز دارد؛ چرا که آینده ایران متصل و فناورانه است و دسترسی پایدار به اینترنت، پیش‌شرط تحقق این آینده خواهد بود./ زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/iaghapour/2621" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2620">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7x0QamdlfTZMehz-CqQXmFJicH9Ul-0LMwJWLlOslMSWbHzTv50CXUOr1QmxhaVQRU6l5OR7cKc_af5PxwiLi1lSawSjePYUUJYC3nzLLXcp7OzHoV9QUStIqkzZJvt7ytuMVzjujAW41IGjkJPtu3M7WMdoVQ-U4XIgakdSu7H_BsROklgSphBRUMfijSYvwc1swtFY0njh6lbB8lkTs_zWQd5yhjwI1kPHOFjMZvQZCEiksDkBZUYB75kFOXohehy5bYoGHI_IWCQAP7FL67X0yNAswIZ-tyTScO8Y8CHve36wkMTcw9_uvBZ_F0Ek379Pg_vamMBWfekjfeXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
بحران خاموشی دیجیتال؛ ضربه‌ای جبران‌ناپذیر بر پیکر اقتصاد و جامعه
🔻
بیش از ۱۹۴۴ ساعت خاموشی دیجیتال، تنها قطع یک ابزار ارتباطی روزمره نیست، بلکه یک «بحران تمام‌عیار اقتصادی و اجتماعی» است. در زمانه‌ای که در سراسر جهان حتی چند دقیقه اختلال در اینترنت زیان‌های هنگفتی به بار می‌آورد، تداوم ۸۲ روزه این وضعیت در ایران، آسیبی عمیق به شریان‌های حیاتی کسب‌وکارها و زندگی عادی مردم وارد کرده است.
در واقع، تداوم این قطعی طولانی‌مدت نشان می‌دهد که حفظ حیات اقتصادی مشاغلِ وابسته به فضای مجازی و نیازهای ارتباطی جامعه، در اولویت تصمیم‌گیری‌ها قرار ندارد؛ رویکردی که پیامدی جز نابودی معیشت هزاران نفر، فرسایش سرمایه اجتماعی و آسیب جدی به بدنه نوپای اقتصاد دیجیتال کشور نخواهد داشت.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/iaghapour/2620" target="_blank">📅 12:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2619">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTKVic3yTmnCGHjxnRhjrKdQwZXOG8m91mwTgG9zSL8iLNo0qxGuNrbQfxsN6ofGNf-jfR4alFvV2g5f62tF7EAlZEtKr-xXfPOVQfCLyxb5FxMOl9nh-HLCcRhFpE3SaceV5ER4bAw3VPWrYXAv2gAbQmjsUxoH1QtEuR-4w6N2ZV1Gafp_Iz7yujKHEOQw_sNJ9goDNfhneAHqiCmCeeAz7Vw8Yxz2EDU6XrROzxH0BJinAJu3NxQEytOsNT5EqmFGhiLwLHWVy6qHlEvcYVvIEQLudjsyXaXaWssZl68vQhvyey06DbIzL3FckFiqmV3L0DdXudA4l0S1ET1EaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
شگفتی گوگل در Google I/O 2026؛ معرفی جمینای ۳.۵ فلش با سرعتی باورنکردنی!
در گام نخست، مدل جمینای ۳.۵ فلش عرضه شده است؛ مدلی که با وجود طراحی شدن برای سرعت بالا و هزینه کم، در کمال شگفتی توانسته مدل‌های پرچمدار و پرو نسل‌های قبل را در بنچمارک‌های تخصصی شکست دهد.
🔹
پادشاهی در بخش ایجنت‌ها:
این مدل با توانایی برنامه‌ریزی بالا، می‌تواند چندین ایجنت را به صورت موازی برای پیشبرد پروژه‌های پیچیده و کدنویسی مستقر کند.
🔸
سرعت خیره‌کننده و کاهش هزینه‌ها:
ساندار پیچای اعلام کرد این مدل با سرعت پردازش ۲۸۹ توکن در ثانیه، حدود ۴ برابر سریع‌تر از رقباست.
🔹
شکست رقبای سرسخت:
جمینای ۳.۵ فلش در آزمون‌های تخصصیِ مربوط به کارهای ایجنتی، امتیاز بی‌نظیر ۱۶۵۶ را کسب کرده و عملاً رقیب سرسختی مثل کلود سونیت ۴.۶ آنتروپیک را پشت سر گذاشته است.
🔸
همچنین نسخه قدرتمندتر یعنی جمینای ۳.۵ پرو در ماه ژوئن ۲۰۲۶ رسماً عرضه خواهد شد.
جمینای ۳.۵ فلش هم‌اکنون به عنوان مدل پیش‌فرض در اپلیکیشن جمینای و بخش سرچ گوگل فعال شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/iaghapour/2619" target="_blank">📅 09:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2618">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuG7K-iyv_K4gU67CzPs73lvfbC7APFFFpPVVzARDuW-zZ1auZ3saZ46DiEK2eeUl4CNdSe7yA3wgA9D3myoDuzN7sARdwX7rzepfvdvWEXrbdWp8hqBt5TR-rkbqomwBMln2A_JtVT1nppaquOVPNA46cN_P5HyRTBsJU_O60TQ8v8wR3mqvLz2qsU0LiyBrApc53jrI2ja8W_KDaNqKzeaoUs5VcbaUB9IZG1eEyaJGXREhniPtvFgLZzB5h4viBD5_wh33XdWhe2QD3qZJBjpM_nu5_nbJzAEcH4KmjJRIL4IUXel7xqBunlFK-F3icsM_NTnxEe6JdsYvP6D8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دیگه پول فیلترشکن نده! آموزش ساخت فیلترشکن شخصی و رایگان با سرعت بالا
😎
🔹
در این آموزش قدم‌به‌قدم بهت یاد می‌دم که چطور بدون نیاز به دانش خاصی، یک فیلترشکن (VPN) شخصی، امن و کاملاً رایگان برای خودت بسازی. این روش روی تمام اینترنت‌ها جواب می‌ده و سرعت خوبی برای تماشای یوتیوب، وب‌گردی و … داره.
🔗
تماشا ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#رایگان
#novaproxy
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/iaghapour/2618" target="_blank">📅 16:00 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2617">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">از هر 10 نفری که که تو اینستاگرام وصل هستن 8 تاش دختره, 2 تاش هم پسر کانفیگ فروش
🥸</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/iaghapour/2617" target="_blank">📅 17:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2615">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHvpD-i7O6Wa0ocbzePvCBAP1CgwcL-kfnG2xWS0Blj9njkNeXdzrhuCvgjlF036fSDkVIrDr0gsxFntHEBTj7NGftpdlYdSIisxhnmsyUIL_70dPqrwr5HOLpwznbuj8gou57mK944AoTWoSASXN_qhggbJnFhCDbQQ-LHwzwO0KbZMi3CcQpkC4cmP9tEhum0T9suwXIhvyI8AUq_JwjLzejauO_bv1hM4F2MRR3715KB8cQdxzVbggLFTTYTYuYOELYdJI58mZp45P6Kr0-bPAF3ORZx_1UTi1VS5ksRtKvlu2QDmoly0SuMeyy81OSt0jXEU_T-xwesB2Rz9Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش نصب ساده و آفلاین 3X-UI روی سرور ایران + SSL (+ معرفی قابلیت های جدید)
🔹
در این ویدیو به سراغ یکی از بزرگترین چالش‌های این روزها رفتیم: نصب پنل 3X-UI روی سرورهای ایران همراه با سرتیفیکیت به صورت کاملاً آفلاین و بدون نیاز به اینترنت آزاد! همینطور سعی کردیم یک معرفی ساده از قابلیت های جدید این پنل داشته باشیم.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
#آموزش
#فیلترشکن
#پنل
#xui
#3xui
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/iaghapour/2615" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2614">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⭕️
بحران در زیرساخت فناوری؛ سقوط درآمدها و خطر عقب‌ماندگی ۱۰ ساله!
اختلالات اینترنتی دیگر فقط یک مشکل ساده برای کاربران عادی نیست؛ بلکه به گفته رئیس کمیسیون شبکه سازمان نصر، تیشه به ریشه‌ی زیرساخت‌های فناوری کشور زده است. این وضعیت نه تنها درآمد شرکت‌ها را تا ۷۰ درصد کاهش داده، بلکه باعث فرار متخصصان کلیدی و فرسودگی شدید تجهیزات شده است.
🔹
سقوط درآمد و انفجار هزینه‌ها: شرکت‌های حوزه شبکه با کاهش درآمد ۳۰ تا ۷۰ درصدی روبرو هستند. از سوی دیگر، به دلیل اختلال در مسیریابی و افت کیفیت، این شرکت‌ها مجبور به پرداخت جریمه‌های سنگین ناشی از نقض توافق‌نامه سطح خدمات (SLA) شده‌اند.
🔸
تهدید امنیت سایبری: محدودیت دسترسی به مخازن اصلی و سرورهای به‌روزرسانی جهانی، ریسک نفوذ و حملات سایبری را تا ۴۰ درصد افزایش داده است. در واقع، امنیت سایبری قربانی ناپایداری شبکه شده است.
🔹
تخلیه ژنتیکی تخصص: صنعت شبکه با بحران خروج نیروهای کلیدی مواجه است. تربیت یک متخصص ارشد سال‌ها زمان و هزینه‌ی ارزی سنگین می‌طلبد که با مهاجرت این افراد، سرمایه‌های انسانی چند میلیاردی کشور به راحتی از دست می‌رود.
🔸
عقب‌ماندگی ۱۰ ساله: ادامه این وضعیت، ایران را با شکاف تکنولوژیک ۱۰ ساله نسبت به کشورهای منطقه مواجه می‌کند؛ شکافی که در فضای پرشتاب فناوری، جبران آن تقریباً غیرممکن خواهد بود.
زیرساخت شبکه کشور به جای اتصال طبیعی به اینترنت جهانی، در حال حرکت به سمت یک ساختار جزیره‌ای و فرسوده است. اگر ثبات پیش‌بینی‌پذیر به این فضا بازنگردد، شرکت‌های بزرگ فناوری به اپراتورهای ساده تجهیزات قدیمی تنزل پیدا خواهند کرد. / دیجیاتو
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/iaghapour/2614" target="_blank">📅 10:38 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2613">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXb7cSo5It_Eqo9E1n_hQAelDIi6bD3I3MC8P_CrlBQ4IERBLPuFk3yLH6ySD-ru_C0ks8b_qc-w1SpCBzJq9RnSuIm4qG0TzEC0kYKFQ49c5-KHniRppDzEYk4ZB3ZDH91vU7jhMlcKAaW2UHrjYz2x7OVbyyjRnx0mAkCxYvWJBoJCjfsGeynCCMge2h9lO8wgxqgh0-SvJLGEh3JH0oE30emxtLc2L8tbgaFiInGZ9QGzbXvJxv6XeftvJwECCtMMw5SNR-RRXJIOLh6PGBpipsjyEGSqtldURYYy48VynJ9YRPc3Op7Yyxf5-LxhJ2_-r80-Zs5AEANXri-a8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
حرف‌زدن درباره‌ی قطعی
#اینترنت
شاید فوری اینترنت را برنگرداند؛ اما
#سکوت
دقیقاً همان چیزی است که ادامه‌ی این وضعیت به آن نیاز دارد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/iaghapour/2613" target="_blank">📅 22:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2612">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/iaghapour/2612" target="_blank">📅 17:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2609">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">کل ریپازیتوری گیت هاب علیرضا که شامل X-UI و S-UI میشد بسته شده و هنوز دلیلش مشخص نیست.</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/iaghapour/2609" target="_blank">📅 19:58 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2608">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
سوپراپلیکیشن ایتا اعلام کرد امکان ارسال فایل تا حجم ۲۰ مگابایت مجدداً برای همه کاربران فراهم شده است!
کاش تلگرام بیاد از شما یاد بگیره :)
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/iaghapour/2608" target="_blank">📅 12:07 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2607">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✍🏻
دوستان عزیز، همون‌طور که احتمالاً متوجه شدید، در یک هفته گذشته به دلایل مختلفی فعالیت ما کمتر شده.
🔹
در این مدت پیام‌های زیادی داشتیم که درخواست آموزش «روش جدید سنایی» رو داشتن. وقتی بررسی کردیم، متوجه شدیم خود ایشون زحمت تهیه ویدیوی آموزشی رو کشیدن؛ بنابراین نیازی به آموزش مجدد  نبود.
🔸
برای اطمینان بیشتر، این آموزش رو به چند نفر از دوستان دادیم تا تست کنن. بیشتر افراد موفق به اجرا نشدن، اما یکی از کاربران تونست متصل بشه. طبق بررسی‌های ایشون، این روش به‌شدت به رنج آی‌پی‌ها (هم سرور ایران و هم خارج) وابسته است. مشکل اصلی اینجاست که بعد از اتصال و مصرف حجم کمی از اینترنت، ارتباط قطع می‌شه و باید آی‌پی رو عوض کرد؛ هرچند آی‌پی قبلی بعد از ۱ تا ۲ ساعت دوباره قابل استفاده می‌شه.
🔻
متأسفانه در این بین، عده‌ای بدون این‌که تست درستی از پایداری تانل بگیرن، شروع به آموزش کردن که نتیجه‌اش فقط ضرر مالی برای کاربران بوده. چون کاربرا رفتن سرورهای گرون قیمت رو خریداری کردن که البته تعداد این افراد اصلا کم نبوده. (نمونه‌اش رو در عکس ضمیمه می‌بینید).
🟢
در مجموع، به نظر می‌رسه این روش هنوز پایدار نیست، اما از بچه‌های تیم خواستیم تست‌های بیشتری روش انجام بدن. اگر خودتون هم مایلید آموزش رو ببینید، می‌تونید مستقیماً به کانال یا گروه سنایی مراجعه کنید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/iaghapour/2607" target="_blank">📅 22:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2606">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⭕️
خلاصه اخبار چند روز گذشته
🔸
اینترنت بین‌الملل به گیمرها ارائه می‌شود؛
ثبت درخواست در سامانه همگرا (اینترنت طبقاتی)
🔹
دولت و مجلس به دنبال حمایت تازه از پیام‌رسان‌های داخلی (رانت و فساد جدید)
🔸
نماینده مردم تهران در مجلس:
درباره خسارت‌های قطعی اینترنت جوسازی می‌شود. (حرف بیخود)
🔹
معاون رئیس‌جمهور:
اینترنت بین‌الملل حتما وصل می‌شود؛ دولت قصد دائمی‌کردن محدودیت‌ها را ندارد. (حرف الکی)
🔸
برآورد انجمن بلاکچین: خسارت ۳۰۰ تا ۷۰۰ هزار میلیاردی از قطعی اینترنت.
🔹
معاون رئیس جمهور: محدودیت حجم و گرانی اینترنت پرو برای جلوگیری از استفاده غیرضروری است. (عجب بابا عجب)
🔸
قطع اینترنت به هفتاد و پنجمین روز خود رسید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/iaghapour/2606" target="_blank">📅 18:43 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2605">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jC34EeND3lGwms0foSnCldgI-Mmk-tVYFhBwZsPw8w_1w1_xQpWzHg7lbGxzGqJHBGL-eJjLHfU611QrGE138BxqjxFtWpkxyc4ziKu0Ukakpw907aXfqloqfGWsrCf2418YEYGkMVQAZ-lkHU7wfbcblJQoDsH-l1lrGkfEOQdd-I-JDxUm9YnBxs6AQYX1IlkaxXpWCdhYOjGYw7KrqXZoSvVmxyZkL5Pe3C5DuzhuCLvX5Rwrx-fsW3_YfVXWZvqqNEutawvNSz53UFI1n8pef1sQNHg8RnzB2pKmuZ2FvjIAN8a0DGM1yTz24PTG8mSjIoU20c4k0fthxoyDDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
با اپ TunnelX در ویندوز از قابلیت Split Tunneling استفاده کنید.
🔹
اپ TunnelX برای زمانی ساخته شده که کاربر نمی‌خواهد تمام ترافیک سیستم از وی‌پی‌ان عبور کند. با این برنامه می‌توان فقط برنامه‌هایی مثل مرورگر، تلگرام، ابزارهای توسعه یا برنامه‌های مشخص دیگر را وارد تونل کرد و بقیه ترافیک سیستم را روی اینترنت عادی نگه داشت. همچنین در صورت نیاز، حالت Full-route برای عبور کل سیستم از تونل در دسترس است.
🔗
دانلود اپ از گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/iaghapour/2605" target="_blank">📅 14:15 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2603">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✍
آدم راننده شوتی باشه به مراتب اضطرابش كمتر از کسیه كه شغلش تو ايران به اينترنت وابسته هستش...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/iaghapour/2603" target="_blank">📅 21:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2602">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚀
آپدیت بزرگ و انقلابی پنل 3x-ui (نسخه‌های 3.0.0 و 3.0.1)
بالاخره یکی از مهم‌ترین آپدیت‌های پنل محبوب 3x-ui منتشر شد! در این نسخه‌ها شاهد بازنویسی کامل رابط کاربری، اضافه شدن قابلیت‌های مدیریتی کلان و بهبودهای چشمگیر امنیتی هستیم.
🌐
۱. بازنویسی کامل و سریع‌تر شدن پنل (مهاجرت به Vue 3)
رابط کاربری از پایه بازنویسی شده است! این یعنی سرعت لود بسیار بالاتر، طراحی مدرن‌تر، صفحه لاگین جدید و بهبود چشمگیر تم دارک.
⚡️
۲. آمار زنده و در لحظه
: با جایگزینی سیستم قدیمی با
WebSocket
، از این پس تمام آمارهای داشبورد، مصرف حجم کلاینت‌ها و وضعیت سرور به صورت «زنده» آپدیت می‌شوند و دیگر نیازی به رفرش کردن صفحه نیست!
🌍
۳. مدیریت چند سروره (Multi-Node Deployment) -
🌟
ویژگی طلایی
یکی از مورد انتظارترین قابلیت‌ها اضافه شد! حالا می‌توانید از طریق یک پنل مرکزی (Manager)، کانفیگ‌ها و اینباندها را روی چندین سرور دیگر (Remote Nodes) مستقر و مدیریت کنید.
📱
۴. رابط کاربری کاملاً سازگار با موبایل
: داشبورد، لیست کلاینت‌ها و بخش لاگ‌ها حالا به صورت "کارتی" و کاملاً بهینه برای نمایشگرهای موبایل طراحی شده‌اند تا مدیریت پنل با گوشی بسیار راحت‌تر شود.
⚙️
۵. خداحافظی با کدهای JSON و تنظیمات آسان‌تر
فرم‌های ساخت کانفیگ (Inbounds) کاملاً ساختاریافته و گرافیکی شده‌اند. دیگر برای تنظیمات پایه نیازی به دستکاری JSON خام نیست (البته تب Advanced برای حرفه‌ای‌ها همچنان وجود دارد). همچنین مدیریت DNSها بسیار پیشرفته‌تر شده است.
👥
۶. مدیریت گروهی کلاینت‌ها (Bulk Actions)
امکان انتخاب گروهی  کلاینت‌ها برای حذف یا اعمال تغییرات اضافه شده که کار ادمین‌ها را بسیار راحت می‌کند.
🛠
۷. امکانات جدید Xray و Outboundها
اضافه شدن پروتکل Loopback، دکمه
Test All
برای تست همزمان همه Outboundها و ارائه گزارش دقیق از تایم‌اوت‌ها، و همچنین خاموش شدن امن هسته Xray.
🔒
۸. ارتقاء امنیت و نصب راحت‌تر
➖
اضافه شدن سیستم امنیتی CSRF Protection برای جلوگیری از حملات.
➖
اضافه شدن گزینه
skip-SSL
در اسکریپت نصب (بسیار کاربردی برای کسانی که از ریورس‌پروکسی یا تانل استفاده می‌کنند و نیازی به سرتیفیکیت روی خود سرور ندارند).
➖
اضافه شدن صفحه مستندات API (API Docs) در داخل خود پنل برای برنامه‌نویسان.
و بسیاری از تغییرات دیگه که میتونید در
این لینک
مطالعه کنید.
💡
نکته:
برای تجربه این تغییرات فوق‌العاده، پیشنهاد می‌شود هرچه سریع‌تر پنل خود را آپدیت کنید. (توصیه همیشگی: قبل از آپدیت بکاپ فراموش نشود!)
✍🏻
با تشکر از ثنایی عزیز.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/iaghapour/2602" target="_blank">📅 18:32 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2601">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
عصبانیت سخنگوی دولت از انتقاد خبرنگاران از قطع اینترنت
فاطمه مهاجرانی در نشست خبری امروز خود به اعتراض خبرنگاران بابت ادامه قطعی اینترنت واکنش نشان داد.
سخنگوی دولت گفت: «در شرایطی که رئیس جمهور آمریکا اعلام می‌کند آتش بس به دستگاه تنفس مصنوعی وصل است، پاسخ شما چیست؟ کشور در جنگ است. بپذیریم که ویژگی جنگ، امنیت مردم است.»
✍🏻
پ.ن:  خانم مهاجرانی اگه دوباره عصبی نمیشید خواستم بگم کاش به فکر امنیت اقتصادی مردم هم بودید! کاش به فکر امنیت ذهنی و روانی مردم هم بودید! کاش یه فکری برای چند میلیون آدمی که با قطعی اینترنت بیکار و ناامید کردین هم بودید!
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/iaghapour/2601" target="_blank">📅 14:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2600">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔻
نمیتونم خبر رو تایید کنم ولی میگن:
— افغانستان اینترنت 5G آورده.
— عراق تلگرام رو رفع فیلتر کرده.
— سوریه هم که ویزا و مستر کارت و...
این که ما درگیر فیلترینگ مسخره هستیم واقعا گریه داره...</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/iaghapour/2600" target="_blank">📅 09:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2599">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلام خواستم یه نکته کوچولو بگم
فقط بحث کسب و کارهای کوچیک نبود
فقط بحث آنلاین شاپ ها نبود
ماهایی که ۴ سال تو دیجیتال مارکتینگ بودیم توی طراحی سایت و سئو و اتوماسیون کار میکردیم هم کاملا ورشکست شدیم
نه از ۹ اسفند
ما یه بار جنگ خرداد زمین خوردیم تا اومدیم بلند شیم از جامون و داشتیم اوکی میشدیم دلار دی ماه سر به فلک کشید و بعد یه قطعی دیگه داشتیم که خیلی ها بهانه کردن و پول ندادن آخر دی ما هیچی پروژه نداشتیم حتی بهترین کارفرماها اومدن گفتن کار شما خیلی خوبه ولی ما واقعا پول پرسنل رو هم به زور میدیم نمیرسه به سئو
بهمن اومدیم خودمون رو جمع کنیم تیر آخر رو اول اسفند بهمون زدن
دفترمون رو تحویل دادیم
نیروهامونو از بهمن تعدیل کرده بودیم
و الان چه جوون ها و چه پدرانی که بیکار شدن
منی که تمام تخصصم همیناست
یک متخصص بیکار محسوب میشم.
©️
پیام ارسالی از کاربر shafikhany</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/iaghapour/2599" target="_blank">📅 01:31 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2598">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✍
حدودا 500 پیام بررسی نشده از 2 روز پیش داریم که پشتیبانی تا فردا همه رو بررسی میکنه.
جدا از بحث بالا، از ته دل آرزو میکنم تو این روزهای عجیب و غریبی که داریم می‌گذرونیم، حال دلتون خوب باشه. می‌بینیم و حس میکنم که زندگی چقدر برای خیلی‌ها سخت شده و دغدغه‌ها چقدر زیادن.
امیدواریم هرچه زودتر این روزهای سخت جاشون رو به روزهای روشن‌تری بدن. هوای خودتون و دلتون رو داشته باشید.</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/iaghapour/2598" target="_blank">📅 03:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2597">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T95v4GfXezBR4yAc2ze5zvqMYAYPUokCOzqsawkoIF1YolL_v-fdgEuVfWIRhOEJnpqozBJss15HYuRN17n9hUyvk3V-YSgd2zsXVhcH3z2Nb7hbVX1hJkh-HmYYrFT8YJ1NXB4ZSdyQXhaXCIZ_qWQkQI6RBGD982sdSVYVva6SQZaf5v1bPY4r4cPFOPi0jh1AhJP_qODh_JcGBfumHd4eSh4Dl6GZ0gZddfsHENWLTy7Al-TsrjTjKXlGMSXao11-LSNAVgX5olDsGIXIvkfCZvqRgxo8vGmQ91TcWOa7716gu90JVeDWi_HyLpENmZcB5SXhiS8x9I-7WptPaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت ورژن 0.10.0 سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور ایران خودتون یک مسنجر شخصی بالا بیارید و با دوستان خودتون چت کنید.
توی آپدیت جدید سانگبرد با فعال کردن قابلیت Remote channel، میتونید پست هایی که تو یک چنل تلگرام ارسال میشه رو، به یک چنل توی سرور سانگبرد خودتون استریم کنید.
-
📡
قابلیت Remote channel
-
🔗
ساده سازی سیستم Invite link
-
🎨
بازطراحی بخش ساخت/تغییر کانال و گروه در UI
-
✨
انیمیشن build-up پیام ها در چت ها
-
🔔
بهبود عملکرد push notifications
- تغییرات گرافیکی اسکریپت نصب آسان
-
🐳
پشتیانی از TLS با سرتیفیکیت self-signed در Docker
-
🔧
رفع باگ های گزارش شده
-
📄
اضافه شدن نسخه فارسی فایل readme
🔘
اگه به هر مشکلی خوردین، حتما تو گیت هاب یک issue باز کنید و گزارش بدید.
⭐️
اگه از پروژه راضی بودین، با ستاره دادن تو گیت هاب از پروژه حمایت کنید.
🔹
چنل پروژه
🔗
لینک گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/iaghapour/2597" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2596">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">⭕️
ساده‌ترین راه برای دور زدن فیلترینگ با تانل DNS
اگه خانواده‌ شما هم داخل ایران برای اتصال به اینترنت مشکل دارند، این پیام ممکن است به شما کمک کند.
این برنامه یک برنامه‌ی  گرافیکیست که کار با آن بسیار ساده است و برای اتصال به اینترنت هر دو روش MasterDNS و VayDNS را پشتیبانی می‌کند.
👈
لینک گیت‌هاب
👈
دانلود
اپ
📖
آموزش کامل MasterDNS و VayDNS
▶️
آموزش روی یوتیوب
📱
آموزش KevinNet DNS
▶️
آموزش روی یوتیوب
🔄
آپدیت‌های جدید برنامه
در صورت وجود هرگونه مشکل یا سوالات مرتبط با KevinNetDNS میتوانید با آدرس ایمیل زیر در تماس باشید:
©️
متن تهیه شده توسط نویسنده اسکریپت KevinDNS
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/iaghapour/2596" target="_blank">📅 23:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2595">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⭕️
ادعای عجیب نماینده مجلس: با ۴ هزار میلیارد تومان ایتا را به سطح واتس‌اپ می‌رسانیم!
رئیس کمیته ICT مجلس در اظهارنظری جنجالی مدعی شده است که فاصله میان پیام‌رسان‌های داخلی مثل ایتا با نمونه‌های جهانی مانند واتس‌اپ، تنها در کمبود بودجه برای خرید سرور خلاصه می‌شود. به گفته او، ارتقای این پلتفرم‌ها هزینه چندانی برای کشور ندارد.
این نماینده مجلس معتقد است که پلتفرم‌های داخلی از نظر فنی کمبودی ندارند و تنها زیرساخت‌های سخت‌افزاری آن‌ها باید تقویت شود:
🔹
بودجه برای رقابت:
مصطفی طاهری مدعی است با صرف ۳ تا ۴ هزار میلیارد تومان برای خرید سرور، می‌توان کیفیت ایتا را به سطح واتس‌اپ رساند تا توانایی پذیرش بدون مشکل بیش از ۲۰ میلیون کاربر را داشته باشد.
🔸
هشدار درباره جاسوسی سخت‌افزاری:
این مقام مسئول همچنین به موضوع استفاده از بیگ‌دیتا (داده‌های بزرگ) اشاره کرده و مدعی شده که آمریکا قوانینی برای جاسوسی در لایه‌های سخت‌افزاری و تراشه‌ها (حتی پایین‌تر از سطح سیستم‌عامل) دارد.
این اظهارات در حالی مطرح می‌شود که کارشناسان حوزه تکنولوژی، موفقیت پلتفرم‌های جهانی را فراتر از صرفا تعداد سرور می‌دانند و مواردی چون امنیت، پروتکل‌های رمزنگاری، حریم خصوصی و نوآوری‌های مداوم نرم‌افزاری را از عوامل اصلی برتری آن‌ها به حساب می‌آورند.
یکی از کاربرا زیر همین پست در دیجیاتو کامنت جالبی گذاشته بود:
مامان‌بزرگ منم با چند میلیارد نیکی میناژ میشه!
پ.ن: حالا فارق از این حرفا داره میگه اینا دارن از کاربراشون جاسوسی میکنن برای همین ما باید اپ های خودمون رو داشته باشیم... من حرفی ندارم.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/iaghapour/2595" target="_blank">📅 18:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2594">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwEjEICk2qyUSm4QN8fVPoBBlqtJVmFj57SvhUFpVmsWhdEgGFFCeFeb7706lLlqjYYhTOYWG1MJn8Jci2fQeB-pZ7dDY9JHrYHbRTkQ9EarhfniO2di_I3P3wiI5nb5twOKLH5MgT3k74Fnd9z-amxXTXnhY9z3Apjtk4aNejYKIUQnjksDDmB7647vuuDzhc0ORppvcL45EowBAfFlhX_xwe_5xszYL7vDAXimrSCFBJTx7XbL2RCj7fD4ZhN5B7HRzITo_URD2ySDuOMorgq7i66w6CV4mqMb_HzcybdGM2ZnTgJABq2HsRk_wMQOMlJgt7h6pvZwghsRzSMEWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
ایران 11 هفته در خاموشی دیجیتال!
هیچ‌وقت تو زندگیم فکر نمی‌کردم یه روزی برسه که این‌جوری تلخ، شاهد از بین رفتن زحمت‌ آدما باشم. ۱۱ هفته قطعی اینترنت واسه خیلی‌ها فقط یه اختلال ساده نبود؛ قصه پدر مادرا و جووناییه که با هزار امید یه کسب‌وکار کوچیک راه انداخته بودن تا خرج زندگیشونو دربیارن و الان دستشون به هیچ‌جا بند نیست.
تا همین چند وقت پیش با کلی استرس می‌گفتیم کسب‌وکارهای نوپا و خونگی تو «مرز نابودی» هستن و همه‌مون چشم‌انتظار بودیم زودتر اینترنت وصل بشه؛ ولی الان دیگه حرف از مرز نیست. خیلی‌ها کل سرمایه، جوونی و حاصل سال‌ها تلاششون جلوی چشماشون دود شد و رفت رو هوا. کاش دردی که افتاده رو دوش این مردم، میافتاد رو دوش مسئولین...
🆔
@NetProPlus</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/iaghapour/2594" target="_blank">📅 11:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2592">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#فیلترینگ
به ما تحمیل شد,
ولی
#اینترنت_طبقاتی
رو شما باید درخواست بدی تا بهت بدن...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/iaghapour/2592" target="_blank">📅 18:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2591">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4be5_2aelOuuSYp730HBmy-r9ULv_BxcyWMk6eYP5OGM3B9viIlg3eoFOAIhVE4Okwf4fRJOBIWdKUc9RmWZkaY3yAvEno92ShevlY_29qZIAfuWW66SbkYoqFRNI3uw09YYs-qKOcLfr9_oGJGKf2IVqXrWacmOYrbGejI34x6LsiTG9ZHVUQYpdloFKtLMGQ7b5IArE57_rAX-vFw2NZ6b9exLRE_MzB6LzUMnVVJagRIQPsDy8fmRzivkLo_At2wgWw3x_J9e0bWqfU5rM16kI8e-FHz2ZE6PE2lwXzwTKwH_MX-_mZ3mabmdqpGUMvMc6ZqOeLOTUnELcAZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آپدیت بزرگ تلگرام: ورود دستیار هوشمند به پروفایل شخصی!
تلگرام در آپدیت جدید تمرکز ویژه‌ای روی هوش مصنوعی داشته است. در ادامه مهم‌ترین تغییرات این نسخه را مرور می‌کنیم:
🔹
ربات‌های مهمان:
فراخوانی ربات‌ها در هر چت یا گروهی، تنها با تگ کردن آیدی و بدون نیاز به افزودن آن‌ها.
🔸
منشی شخصی هوشمند:
قابلیت اتصال مستقیم یک ربات به پروفایل شخصی تا در غیاب شما به پیام‌ها پاسخ دهد!
🔹
تعاملات زنده هوش مصنوعی:
تایپ و نمایش لحظه‌ای پاسخ ربات‌ها، به همراه قابلیت جدید ارتباط ربات با ربات برای انجام وظایف پیچیده‌تر.
🔸
امکانات جدید برای کانال‌ها و تولید محتوا:
قابلیت محدود کردن نظرسنجی‌ها (بر اساس کشور یا عضویت در کانال)، مشاهده نمودار آرا، و همچنین ساخت استایل‌های متنی سفارشی.
🔹
اضافه شدن قابلیت انتخاب فونت از سیستم خودتون (میتونید فونت وزیر رو نصب کنید و استفاده کنید).
با این به‌روزرسانی که شامل جستجوی هوشمند ایموجی‌ها، ارسال بی‌صدای پیام زمان‌بندی‌شده و رفع ۲۰۰ باگ فنی است، تلگرام قدم بزرگی برای ادغام کامل پیام‌رسانی انسان و هوش مصنوعی برداشته است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/iaghapour/2591" target="_blank">📅 14:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2590">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
مومن‌نسب: فضای مجازی به هیچ وجه نباید به حالت قبل برگردد
حالا این آدم انقدر مهم نیست که دربارش صحبت کنیم ولی خواستم بگم این همون آدمیه که چندسال پیش تو صداوسیما میگفت من خطرات اینترنت رو میدونم و اطلاع دارم یک نفر با 2 گیگ اینترنت حامله شده و پدر دختره با گریه اینو برای من تعریف می‌کرد...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/iaghapour/2590" target="_blank">📅 11:35 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2589">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔻
اطلاعیه مهم: معرفی فروشندگان کانفیگ
طبق نتایج
نظرسنجی اخیر،
قصد داریم فروشندگان قدیمی و معتبری که از قبل می‌شناسیم را یکی‌یکی برای خرید به شما معرفی کنیم.
📌
قوانین و شرایط مربوط به فروشندگان:
—
عدم پذیرش فروشنده جدید:
در حال حاضر شخص جدیدی معرفی نمی‌شود؛ بنابراین لطفاً در قسمت
«تماس با ما»
برای معرفی خود پیام ندهید. افرادی که معرفی می‌شوند، همگی پیش‌تر در کانال ما سابقه تبلیغ داشته‌اند.
—
تضمین خرید شما:
مبلغی از پول این افراد نزد ما به عنوان امانت می‌ماند تا در صورت بروز هرگونه مشکل، بتوانیم مطالبات شما کاربران عزیز را پیگیری کنیم.
—
ضمانت بازگشت وجه:
این فروشندگان موظف‌اند در صورت لزوم (بسته به شرایطی که خودشان به شما اعلام می‌کنند)، بین ۴۸ تا ۷۲ ساعت امکان عودت وجه را فراهم کنند.
—
قیمت منصفانه:
تمامی این افراد تعهد داده‌اند که نسبت به شرایط بازار، قیمت‌های منصفانه‌تری برای کاربران کانال ما در نظر بگیرند.
— معرفی فروشندگان صرفاً در زمینه
فروش کانفیگ
انجام می‌شود. هیچ‌یک از فروشندگان معرفی‌شده مجاز نیستند پس از معرفی، در کانال شخصی خود تبلیغات مربوط به "
اوتباند
" قرار دهند و یا به کاربران پیشنهاد خرید آن را بدهند.
⚠️
نکات مهم برای کاربران عزیز:
—
انتظارات از کیفیت:
کانفیگ‌ها باید بتوانند تلگرام، اینستاگرام و یوتیوب را به راحتی باز کنند. با توجه به شرایط فعلی اینترنت، داشتن سرعت‌های بسیار بالایِ گذشته کمی دور از انتظار است (هرچند ممکن است کیفیت سرویس‌ها عالی باشد)، پس لطفاً واقع‌بین باشید.
—
اختلال و پشتیبانی:
ممکن است در طول هفته، گاهی با اختلال مواجه شوید. پشتیبان‌ها موظف‌اند در سریع‌ترین زمان ممکن مشکل را حل کنند؛ اما لطفاً صبور باشید، حداقل یک ساعت به آن‌ها فرصت دهید و از ایجاد فشار زودهنگام به پشتیبانی کانال‌ها خودداری کنید.
— در ضمن، توجه داشته باشید که
ما ذی‌نفع این کانال‌ها نیستیم
و فقط به دلیل درخواست‌های زیاد شما این دوستان را معرفی می‌کنیم.</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/iaghapour/2589" target="_blank">📅 23:36 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2588">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hz_VpdRSQbAWSAS3BdDDragmoXZ4-35foKJtvOKzM0VSruRJzme9U1iXqeZoAdY9dgrJHwniFNIJKROnPGU8ANFTeVmxKPjSkUYWRJmwlQn354zannTZE6Y6wmcUxjJQtXiy9U25ELJu4H5VdPjBWavcKl0oa4Zjcpkeeoa-tR_trxQprWhmLjSYG_KTmg8qsEvDfEXgujLu0owJgIuuvs9THLE118OVpr_HxxqHkfphwm6JcRkNgN7IXys61qahaueSC4nHt7FzJriLG3i7JrRlRyUbRGNMgd3dQceJipuLHqG_9bacAEgJPHwpkXK9rBSwKkp9oKuDralwu7C5JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
سخنگو وزارت خارجه حذف تیک آبی خود در شبکه X را (سرکوب حقیقت) خواند.
68 روزه اینترنت مردم ایران رو قطع کردن، بعد یه تیک آبی‌شو گرفتن میگه حقیقت سرکوب شد.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/iaghapour/2588" target="_blank">📅 20:22 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2587">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
تسنیم: درآمد طرح اینترنت «پرو» در سال به ۹۶ هزار میلیارد تومن می‌رسه!
🔹
خب با این رقم‌های نجومی و پول هنگفتی که درمیاد، معلومه که از این تبعیضی که راه انداختن حسابی راضی‌ان. وقتی محدودیت و فیلترینگ این‌قدر براشون سود داره، چرا نباید اینترنت داخلی و بسته رو بیشتر تحویل بگیرن؟
🔸
این وسط یه تشکر ویژه و خسته نباشید هم باید بگیم به اون دسته از دوستانی که رفتن تو صف اینترنت پرو و این سیستم طبقاتی رو خیلی راحت پذیرفتن. از رئیس فلان اتحادیه و مدیر فلان اداره بگیر تا نماینده صنف لاستیک‌فروش‌ها و یه سری کسب‌وکارهایی که واقعاً بدون اینترنت آزاد هم کارشون لنگ نمی‌موند. تو شرایطی که ۹۹ درصد مردم هیچ دسترسیِ عادی به اینترنت آزاد ندارن، مرسی از شماها که رفتین این اینترنت رو گرفتین و با این کارتون، قشنگ به این تبعیض و نابرابری رسمیت دادین!
پ.ن: البته به این نکته هم توجه کنید که خبرگذاری داخلی اینو گفته و ممکنه دقیقا مقصودشون از این حرف هم همین باشه که بگن چقدر این طرح خوب و سودآور هستش و...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/iaghapour/2587" target="_blank">📅 14:33 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2585">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⭕️
وعده بازگشت به وضعیت عادی؛ توجیه محدودیت‌ها یا امید به بهبود اینترنت؟
معاون ارتباطات دفتر رئیس‌جمهور به تازگی اعلام کرده که وضعیت فعلی اینترنت مورد تایید دولت نیست و رئیس‌جمهور، محمدرضا عارف را مامور ساماندهی این شرایط کرده است. به گفته او، این محدودیت‌های شدید و قطعی‌ها صرفا تصمیماتی از سوی شورای عالی امنیت ملی و به دلیل شرایط خاص امنیتی و جنگی بوده‌اند.
🔹
وعده روزهای بهتر:
این مقام مسئول قول داده که با عبور از این شرایط ویژه، اینترنت نه تنها به حالت قبل برمی‌گردد، بلکه وضعیتی بهتر از گذشته پیدا خواهد کرد و وعده‌های انتخاباتی رئیس‌جمهور در این زمینه همچنان پیگیری می‌شوند.
🔸
دفاع از اینترنت پرو:
در واکنش به انتقادات، دولت ادعا می‌کند طرح «اینترنت پرو» صرفا برای نجات کسب‌وکارها در روزهای محدودیت ایجاد شده و نباید به آن برچسب اینترنت طبقاتی زد؛ چرا که به گفته آن‌ها، در شرایط عادی اصلا نیازی به چنین طرحی نخواهد بود.
🔹
کاهش محدودیت‌های عمومی:
خبر دیگر این است که قرار شده تدابیر جدیدی برای دسترسی بهتر سایر شهروندان به اینترنت اتخاذ شود تا فشار محدودیت‌های فعلی روی مردم کاهش یابد.
در حالی که دولت تلاش می‌کند قطعی‌ها و طرح‌های بحث‌برانگیزی مثل اینترنت پرو را صرفا به شرایط اضطراری گره بزند، کاربران و کسب‌وکارها همچنان منتظرند تا ببینند آیا این وعده‌ها در عمل به یک اینترنت آزاد و بدون محدودیت ختم می‌شود یا صرفا وعده‌ای برای کنترل نارضایتی‌های فعلی است.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/iaghapour/2585" target="_blank">📅 21:12 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2584">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⭕️
ایده عجیب در مجلس: تاسیس «اینستاگرام دولتی» و مدیریت کامل اینترنت!
نمایندگان مجلس در تازه‌ترین نشست خود با وزیر ارتباطات، از طرح‌ها و نگاه‌های جدیدی برای کنترل بیشتر فضای مجازی پرده برداشتند. در این جلسه، پیشنهاد ایجاد یک پلتفرم کاملا دولتی مشابه اینستاگرام مطرح شد تا به زعم آن‌ها، نیاز کشور برطرف شود.
🔹
اینستاگرام دولتی:
یکی از نمایندگان با اشاره به بازار سیاه و چند میلیونی فیلترشکن‌ها، رسما پیشنهاد ساخت یک سکوی دولتی شبیه اینستاگرام را برای پر کردن جای خالی این پلتفرم ارائه داده است.
🔸
رویای مدیریت اینترنت:
نایب رئیس مجلس تاکید کرده که مشکل آن‌ها اصل اینترنت نیست، بلکه می‌خواهند در صحنه بین‌المللی، مدیریت اینترنت کاملا در دست خودشان باشد و این فضا را به یک جبهه تقابل تشبیه کرده است.
🔹
فرصت‌سازی از بحران:
بخش قابل توجهی از صحبت‌های نمایندگان، حسرت خوردن برای از دست رفتن فرصت در شرایط ملتهب و جنگی است؛ آن‌ها معتقدند باید از این شرایط استفاده می‌کردند تا مردم و کسب‌وکارها به اجبار به سمت سکوهای داخلی کوچ کنند.
این صحبت‌ها به وضوح نشان می‌دهد که دغدغه اصلی، کاهش نارضایتی مردم از قیمت و کیفیت اینترنت نیست؛ بلکه تلاش برای بومی‌سازی اجباری، قطع ارتباط با شبکه‌های اجتماعی بین‌المللی و کشاندن کاربران به پلتفرم‌های تحت کنترل و نظارت است. / زومیت
✍🏻
پ.ن: از سوپر اپلیکیشن های ایتا و سروش و گپ و بله که از تلگرام کپی کردین مشخصه توانایی اینکار رو دارید.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/iaghapour/2584" target="_blank">📅 19:36 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2583">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭕️
مرگ خاموش اقتصاد خرد: نابودی ۴۰ درصد از کسب‌وکارهای اینستاگرامی!
قطعی‌ها و محدودیت‌های اینترنتی فقط حق دسترسی آزاد ما به شبکه‌های اجتماعی را سلب نکرده، بلکه تیشه به ریشه‌ی اقتصاد خرد و معیشت مردم زده است. طبق اعلام پشوتن پورپزشک، عضو هیئت‌مدیره اتحادیه کسب‌وکارهای مجازی، فیلترینگ و اختلالات باعث نابودی بخش عظیمی از مشاغل آنلاین شده است.
🔹
فاجعه‌ی آماری: نزدیک به ۴۰ درصد از کسب‌وکارهای اینستاگرامی برای همیشه از بین رفته‌اند؛ این یعنی مرگ مستقیم بیش از ۴۰۰ هزار شغل!
🔸
دومینوی ویرانی: وقتی شوکی مثل محدودیت اینترنت وارد می‌شود، ابتدا کسب‌وکارهای کوچک و آسیب‌پذیر می‌میرند، اما این نابودی با کمی تاخیر گریبان شرکت‌های بزرگ اقتصادی را هم خواهد گرفت.
🔹
زنجیره‌ی به هم پیوسته: کسب‌وکارهای بزرگ در تولید، تامین و توزیع به شدت به همین کسب‌وکارهای خرد وابسته‌اند. توهم مصونیت برای شرکت‌های بزرگ، در نهایت منجر به فروپاشی خود آن‌ها می‌شود. منبع: زومیت
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/iaghapour/2583" target="_blank">📅 19:29 · 15 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2581">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسم این زندگــــــی نبود
یک مبارزه تمام عیار بود...
#جوانی
#زندگی
#جنگ
#اینترنت</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/iaghapour/2581" target="_blank">📅 19:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2580">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭕️
حل مشکل دانلود از ریلیز گیت‌هاب با LatestReleaseMirror
اگر در دانلود فایل‌ها از بخش ریلیزهای (Releases) گیت‌هاب به دلیل محدودیت‌های اینترنت مشکل دارید، این اسکریپت کاربردی دقیقاً برای شما ساخته شده است!
ابزار
LatestReleaseMirror
به صورت خودکار فایل‌های آخرین آپدیتِ ریپازیتوری‌های دلخواه شما را دریافت کرده و آن‌ها را به عنوان فایل‌های عادی در ساختار پوشه‌های گیت‌هاب ذخیره می‌کند؛ در نتیجه می‌توانید آن‌ها را به راحتی و حتی با اینترنت داخلی دانلود کنید.
🔹
دریافت و آپدیت خودکار آخرین نسخه با استفاده از GitHub Actions.
🔸
امکان فیلتر کردن فایل‌های مورد نیاز (مثلاً فقط نسخه‌های ویندوز یا اندروید)
🔹
دسته‌بندی تمیز فایل‌های خروجی در مسیرهای مشخص.
🔗
لینک ریپازیتوری و راهنمای استفاده
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/iaghapour/2580" target="_blank">📅 16:09 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2579">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ركورد جديد سرعت اينترنت ژاپن:
با سرعت 1.02 پتابيت بر ثانيه، كل نتفليكس را در 1 ثانيه دانلود مى‌كند.
✍
ما هم اینجا باید با DNStt وصل بشیم تا بزور بتونیم فقط این خبر رو بخونیم...
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/iaghapour/2579" target="_blank">📅 13:56 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2578">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭕️
اسکریپت بهینه شده XHTTP Relay ECO برای Vercel Pro
🔹
نسخه ECO طوری تیون شده که علاوه بر امنیت سفت‌وسخت v1.3، کم‌هزینه‌ترین رفتار ممکن روی Vercel Pro رو داشته باشه؛ یعنی با کنترل هوشمند Timeout، Inflight، Throttle و Logها، مصرف منابع و هزینه نهایی تا جای ممکن پایین نگه داشته میشه.
🔸
فقط با GET، HEAD و POST کار می‌کنه تا امنیت بالاتر بره.
🔹
احراز هویت فقط از طریق هدر x-relay-key انجام میشه
🔸
هدرهای اضافی پلتفرم و hop-by-hop رو بی‌رحمانه فیلتر می‌کنیم.
🔹
روی آپلود و دانلود محدودیت سرعت (Throttling) واقعی گذاشتیم.
🔸
بردیمش روی Node runtime با لیمیت ۱۲۸ مگابایت رم و مدیریت کانکشن‌های همزمان.
🔗
اطلاعات بیشتر در گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/iaghapour/2578" target="_blank">📅 22:28 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2577">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
ورژن جدید کلاینت اندروید GooseRelayVPN منتشر شد
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
هسته پروژه به ورژن 1.5.0 آپدیت شد.
🔸
قابلیت fake dns اضافه شد.
🔹
باگ ها در این نسخه برطرف شدن.
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/iaghapour/2577" target="_blank">📅 14:05 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2576">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHXmZiiMvgSA5uuI9KACDhOdF_yZGiLBcMmiz8Coge67uhCg5b7ggHKBfaA9dTdQ4CYW0SSZl7-tDk2LYbCvBatHqf0F4mBg_iYxDQSdQ68zyITuQbUDZYU9R9oBGZMaUUe-bKxCBM83UrjUnWBXPwHgNnLBgpy8n5um-vRyJzCQG90siMKOLsfH-R-ildxbbONDL6MGFgoinDMyrGzw0S4sKzMGHbbNwZ-DLFzToZHgRrlna8J9oxELO-eppgj8t54DDoOoLqAXSqKAY8e_wVmWLRfCQkb1R58oRYhjUeRZE0CmYwEZnXldNMOywtFl0txQGRryjpNl5Lvto7RPSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن رایگان و شخصی به 2 روش با نت ملی
🔹
با استفاده از دو ابزار قدرتمند MHRV و Nova-Proxy، دیگه نیازی به خرید کانفیگ‌ها و سرورهای گرون‌قیمت ندارید. تو این آموزش قدم‌به‌قدم به ۲ روش مختلف پیش میریم تا بتونید یه اتصال پایدار و بدون قطعی داشته باشید. حتماً تا آخر ویدیو همراه من باشید.
🔗
لینک ویدیو در یوتیوب
🔗
دانلود ویدیو با لینک مستقیم
🔹
دانلود کلاینت ویندوز
🔸
دانلود کلاینت اندروید
#آموزش
#فیلترشکن
#mhrv
#novaproxy
#رایگان
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/iaghapour/2576" target="_blank">📅 19:53 · 12 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2575">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHrfc501a4U6VZouD08vLgbGfBKNeuCJLGEeQcf3kwrXrAhmkoQ_-NCeCYqw094MIjtoG_ckPk5dbIlJ_M8CH4oYUzdPUqs1LIcenQx0JyHL-ooh0Aep6is0HMxLfurFAdK-7oJd8fDXUt-Ay3Y42uA1qq_MF6lx9Nfwlz2v-ojrnG8LdLlICFt43BLlv8qhqnuza9nqL58UjgZgZuNUj_34xEeiWeWHf_ziJR8N2EkKGN91YsnAg0_ZaZWxF3wLuykicblQASjqqToHzRlZTc_zNM5uFZitghFhmIncq5zPEtZy7MHxWfIH5b8eF8ljJQh230ITTt5O-l5FgF1XEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پشت‌پرده‌ی «اینترنت پرو»؛ امتیاز ویژه یا تله‌ی نظارتی؟
این روزها سیم‌کارت‌های بدون فیلتر با نام «اینترنت پرو» در ازای دریافت هزینه و ثبت کامل مشخصات هویتی به فروش می‌رسند. اما هدف اصلی این طرح، دلسوزی برای نیاز اینترنتی اقشار مختلف نیست.
هدف اصلی و پنهان این ماجرا، چیزی جز «تشخیص هویت دقیق و رصد لحظه‌ایِ کاربر» نیست.
👁‍🗨
وقتی اینترنت آزاد را مستقیماً با نام و کد ملی خودتان دریافت می‌کنید دقیقاً چه اتفاقی می‌افتد؟
🔹
پایان گمنامی:
تمام سایت‌هایی که سر می‌زنید و محتوایی که می‌بینید، مستقیماً و شفاف روی نام خودتان ثبت و مانیتور می‌شود.
🔸
تزریق خودسانسوری:
وقتی می‌دانید هر کلیک شما رصد می‌شود، ناخودآگاه وارد یک «زندان شیشه‌ای» می‌شوید که خودتان هزینه‌اش را داده‌اید!
🔹
تجارت با حقوق اولیه:
حق بدیهی دسترسی به اینترنت آزاد را مسدود کرده‌اند و حالا همان را به قیمت نقض حریم خصوصی، به عنوان یک «آپشن ویژه» به خودمان می‌فروشند.
«اینترنت پرو» یک امکان رفاهی نیست؛ ابزاری برای کنترل نقطه‌ای و عادی‌سازیِ اینترنت طبقاتی است. بهای اصلی این سیم‌کارت‌ها پول نیست؛ حریم خصوصی ماست.
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/iaghapour/2575" target="_blank">📅 15:30 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2573">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZntfcIBKpNLfRq_p4qcOZCFh_Fp1bdov_nt3AVE-zgR8r5PI7pNEpY5rtm0_uXnMt1H1l3hTzrtElLA-XfxK8XzXqT4PRdglD3xUxg36PR_e7ZjvhVlIdu7JRj02z3dXoMCNMHUN3gs2UyVkouTc8D6po01HQZb-svLOHG6OGBoXuQkoSQQ9HF5DKD-S3RtnCds9IUK_VEK0XDG0AHArzgFJUVF7UB2qzB3GNC-KFEevim4HMHBfu1Mjn63XO8oC0Qbj9VFfr0FnhhtFN7ndqriXsoK02MkjqmpnJPGKmLUOGPzhYl2G2nFr0nQ2Q0AAqFO77zIl21K_3LC1_tbK1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
کلاینت اندروید GooseRelayVPN
🔹
کلاینت اندروید GooseRelayVPN که هسته GooseRelay را از طریق Go mobile اجرا می‌کند و رابط کاربری کامل برای مدیریت VPN، پروفایل‌ها، لاگ‌ها و تنظیمات ارائه می‌دهد. این اپ یک SOCKS5 محلی روی اندروید ایجاد می‌کند و ترافیک TCP را از معماری GooseRelay عبور می‌دهد.
🔹
پیکربندی مبتنی بر پروفایل
🔸
وضعیت و تله‌متری در صفحه Home
🔹
تب Logs برای عیب‌یابی Android/Core
🔸
قابلیت Split Tunneling و Internet Sharing
🔗
آدرس گیت‌هاب پروژه
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/iaghapour/2573" target="_blank">📅 20:06 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2572">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">💢
رئیس اتحادیه کسب‌وکارهای مجازی
:
به شرکت‌ها زنگ می‌زنند و پیشنهاد فروش اینترنت بدون فیلتر(پرو) برای کارمندانشان را می‌دهند.
⁉️
اگر موضوع واقعاً امنیت ملی است، چطور با پرداخت پول، امنیت تأمین می‌شود؟!
منبع: کانال خبری
🆔
@iaghapour</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/iaghapour/2572" target="_blank">📅 13:23 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2571">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-poll">
<h4>📊 ⁉️نظرسنجی درباره سوال بالا (اگه واقعا نیاز دارید بله رو بزنید).</h4>
<ul>
<li>✓ بله معرفی بشه.</li>
<li>✓ خیر نیازی نیست.</li>
</ul>
</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/iaghapour/2571" target="_blank">📅 00:25 · 10 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-2570">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✍🏻
دوستان، همان‌طور که خودتون در جریان هستید، من در این چند ماه حتی یک مورد
تبلیغ فیلترشکن، اوتباند
و موارد مشابه
قرار ندادم.
الان هم واقعاً تمایلی به این کار ندارم، چون شرایط اصلاً به‌گونه‌ای نیست که بشه کسی را معرفی کرد.
با این حال، در همین چند ماه پیام‌های بسیار زیادی داشتیم که درخواست می‌کردند حتماً یک شخص معتبر را معرفی کنیم؛ چرا که خیلی‌ها از کلاهبرداری‌های پیاپی خسته شدن و ارسال این دست پیام‌ها تا به همین امروز هم ادامه داره.
به همین دلیل، اگه خودتون موافق باشید،
افرادی رو که
از قبل با ما همکاری می‌کردند
و تا حدودی قابل‌اطمینان هستند، یکی‌یکی به شما معرفی کنیم. در این مورد ذکر چند نکته ضروری هستش:
🔸
عدم تضمین صددرصدی:
ناگفته نماند ما واقعاً نمیتونیم کسی را با اطمینان ۱۰۰ درصدی تأیید کنیم، اما افرادی که معرفی میشن همگی سابقه همکاری با ما را دارن.
🔹
عدم پذیرش تبلیغ جدید و اوتباند:
تا زمانی که شرایط استیبل و پایدار نشود، تبلیغ
هیچ فرد جدیدی را قبول نمی‌کنیم.
در ضمن،
تبلیغ فروش اوتباند هم به‌هیچ‌وجه پذیرفته نمی‌شود.
🔸
قیمت‌های منصفانه:
تمام سعی ما بر اینه افرادی را معرفی کنیم که در این زمینه منصف باشند و قیمت‌های بالایی ارائه ندهند. ولی خب، طبیعتاً نمیشه انتظار قیمت‌های قدیمی را داشت؛ چون همان‌طور که خودتون میدونید در حال حاضر هیچ‌کس با اون قیمت‌های قبلی فروشی نداره.
اگه تمایل دارید، لطفاً در نظرسنجی زیر شرکت کنید.
البته نظر شخصی خودم اینه که اگه در حال حاضر واقعاً مشکل خاصی ندارید، در نظرسنجی همان گزینه
(خیر) را انتخاب کنید
.</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/iaghapour/2570" target="_blank">📅 00:24 · 10 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
