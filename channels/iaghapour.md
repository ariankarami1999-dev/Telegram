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
<img src="https://cdn4.telesco.pe/file/QsRHHJQeTPKM1JiDOAZCJOP3SmLNZ1OCAWde_CbT8UxGTgqzQBz6u_CQMrURrrKYOXUoRXhIKZmb4Wla4a8T5cRNqibiN9WCM54H0GGqyVzOAgHB1nB3hx_oeTPU15x3TlW39-pUF2TgVDA_Yy0kmVMF3KiCsZO0sh5md5Vrm6Q4IUe8yjv6O4-07lYa_bwaAPa90kJ-Y1zFtd7MEUy4a-nCoc599fJNrbSQxGnmyLDXfUL5vuzF5bNC8sbcRspOF4GLZlY6vuLbPdomejsj2DYS14sxi6d__8e7Tsh0D9WS3h7YbPZmdPz0qlUfspY65EfOYorhgjEiUpG_Nv2uAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.6K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 02:20:54</div>
<hr>

<div class="tg-post" id="msg-3054">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovinCloud - ابر نوین</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFu0pgNwhedsJoI8L-s-qn5dIu_uKZiB_pJiRpC1uSCF9zplZpedhjKscdKYNgN3jh0587NA5Ckbp_UQqhctHYUKGTrmTdEUnByVrq0CQ3dwyFCceiPkXuYUzGMXKSpYlKZyCdiG_7naNpH3X5jtuQ3WztMnSQJwOPQlDrahV42Oj0U4YLak3NeMKUBe5m2c86k4Z2Ru3xwQVCtVW0sSDpmNdUyUWHk8agdAbB9SrpAHHzotU1s8RwaWoIei5UOCKcE39YUDUALaSrX5Cx_EbbZn3OqCLQMVeEICKGjkzcOlTenTU2rZUIWSHRvXioJ6BjmSDz3SrEQVYpeVj-Al0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">50%
تخفیف
ویژه خرید سرور مجازی ایران از
ابرنوین
🇮🇷
سرعت، قدرت و پایداری
VPS ایران
میزبانی شده در قلب تهران را اینبار با
50% تخفیف
به صورت یکجا تجربه کنید
⚡️
🛍
کد تخفیف
:
iranvps50
🖥
جهت مشاهده توضیحات بیشتر، قیمت و مشخصات پلن ها اینجا کلیک کنید
چرا
ابرنوین
را انتخاب کنیم
⁉️
بیش از 10 سال سابقه میزبانی موفق
✅
سرورهای جدید نسل 9 الی 11
✅
پهنای باند بالا تا 10 گیگ بر ثانیه
✅
میزبانی در بهترین دیتاسنترها
✅
پنل مدیریت حرفه ای
✅
ترافیک ارزان و آپلود رایگان
✅
تحویل آنی و پشتیبانی 24 ساعته
✅
🌐
آدرس سایت:
www.novincloud.com
💬
تلفن پشتیبانی:
91035587-021
ابرنوین
، میزبان ابری شما
💙
🌨</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/iaghapour/3054" target="_blank">📅 21:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3053">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofd_18MMmrSm4O6YQBRxxDd5tKDHW4h9e2vXAHItGHK7T0IX2HZubMm1EbLUDrKwSFoSkX-c84Jx__vfhkvbke2q3L4Nsdu96gqeQhse-SPS-R9Gau46dRqj00tIMBQVqGjhfYivshNtRa5kFL-b3wufIR6ljyD0BzashIaugGDeZCN7210L5A-LdknZ4EOdxxMisYrYmu-xULZUuRuhjUk0ziO1Oi3qWdi3ZukBPbSTxNSIpuIyIGIp0o5bXtC7lE4yX7cGu0li4I7limp5bJMaA3a3xu2DIBnrxGjNYeNlV_kU6PZnssXpC1TvSP8P2ue-pvslDLZvaiG5VDbavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
انتشار نسخه جدید Subify v2.9.16؛ فراتر از ترجمه انگلیسی به فارسی!
ابزار کاربردی
Subify
با یک آپدیت بزرگ به‌روزرسانی شد. مهم‌ترین تغییر این نسخه، اضافه شدن قابلیت انتخاب زبان مقصد است؛ حالا می‌توانید زیرنویس و دوبله هوش مصنوعی را به هر زبانی که می‌خواهید دریافت کنید.
🔹
پشتیبانی چندزبانه کامل:
ترجمه زیرنویس و تولید دوبله صوتی به زبان انتخابی کاربر همراه با کشینگ هوشمند ترجمه‌ها.
🔹
پشتیبانی از پلتفرم‌های جدید:
اضافه شدن امکان ترجمه و زیرنویس در اینستاگرام و توییتر (X).
🔹
رفع باگ‌ها و بهبود پایداری:
حل مشکل پریدن زیرنویس بعد از رفرش یوتیوب و ارتقای بازیابی خودکار زیرنویس‌ها.
🔹
بهبود ظاهری و فنی:
فونت‌های فارسی تمیزتر، نمایش روان‌تر لایه زیرنویس (Overlay) و بازطراحی رابط کاربری.
🌐
سایت برای نصب افزونه
💻
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/iaghapour/3053" target="_blank">📅 20:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3052">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCnys4xSAIu1Ax44YeazQU-sfPD6D1aguHJe7T_amXRPYInD8kqXu0teeFw52R5OZ4mjvE6hf3096iUf09T5Yk9CM97Mj2ZddcIAboNLjC5PahVfy8nEcOYcYFPtxhWkcHUvSCdP7tiTkDYA2CM9lyoo1sRO_ppiTdD5IYkjQvwRfBFOrRL-CZGxrOfWpldNltbpa8nLAy_6NJphhH5zSOyR4kAVQhDJxoJEq-ouOIYyAdP8pMKblvAtrayBV2j2pion305Skzo0qY9PUBGRIZEs8LCc7QfdQqVNu_VaBn4pB24JjNn_hEpJNZE6FwQNJZct_W1Zj4X_NdBWHvXj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی جعبه‌ابزار کاربردی مدیران سرور و دواپس
یک ابزار تحت وب و رایگان که تمام کانفیگ‌های کاربردی لینوکس را به‌صورت بهینه و استاندارد تولید می‌کند:
🔹
ستاپ اولیه سرور:
تولید اسکریپت شل برای امن‌سازی SSH، فعال‌سازی BBRv1/v3، فایروال، Fail2ban و نصب داکر.
🔸
تیونینگ TCP/IP و کرنل:
تنظیم بهینه
sysctl.conf
متناسب با رم و پهنای باند سرور، کاهش پکت‌لاس و بافربلوت.
🔹
کانفیگ Nginx:
ساخت پروکسی معکوس با TLS 1.3، پروتکل HTTP/3، سوکت و هدرهای امنیتی.
🔹
فایروال و روتینگ:
ساب‌نت ماشین، پورت فورواردینگ (NAT)، رفع تداخل داکر و خروجی مستقیم برای iptables و nftables.
🌐
آدرس وب‌سایت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/iaghapour/3052" target="_blank">📅 19:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3051">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYZnqRrI4Um8uV_nOTID55_tLc9KauLHncwz_Ifr1LZ9tin91IWTihKK4dRZLpWwTvKJnGqEarikjRwM6wn6DiVy9bgz8nTLjFXBDH_lATf7Tjx8Wuc1ddea2FEhRihBVimcSMudA8oVQkLmxJoACHYly1qZL427NcYOw62NPiky6KHzC0LLAaWo85utS4_1bhNuhpO7MTqQ4Rby1vLF-JbCcO68ljESBG7rXrIeG0I9GOubq6kZ9K0N4rXVVsaYtuZwhDQJMtapAyGbvlCE6_dCvwJUT_jdDMh6yt8m0YJi2OpcRwtAENdf7HpT_zq7BMfICOu8h7zlyjxF7QTWnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گزارش رگولاتوری از ماجرای اتمام زودهنگام بسته‌ها
سازمان تنظیم مقررات پس از بررسی گلایه‌ها درباره پایان زودهنگام بسته‌های اینترنت، اعلام کرد اپراتورها تخلفی نداشته و ضرایب مصرف را رعایت می‌کنند.
⚙️
دلایل اعلام‌شده برای اتمام سریع بسته‌ها:
🔹
کیفیت ویدیوها و فرآیندهای پس‌زمینه:
افزایش حجم محتواهای ویدیویی، آپدیت خودکار نرم‌افزارها، بکاپ‌های ابری و فعالیت برنامه‌ها در پس‌زمینه از دلایل اصلی جهش مصرف عنوان شده است.
🔹
شفاف‌سازی ریزمصرف:
رگولاتوری اعلام کرد عدم شفافیت برخی اپراتورها در تفکیک ترافیک داخلی و بین‌الملل پیگیری و اصلاح شده تا مشترکان دقیق‌تر مصرف خود را ببینند.//شبکه‌چی
💬
خلاصه اینکه اگه قبلاً بسته ۱۰ گیگی یک ماه براتون کار می‌کرد و الان یک هفته‌ای تموم میشه، مشکل از سیستم نیست؛ مصرفتون یهویی رفته بالا و شما حواستون نیست!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/iaghapour/3051" target="_blank">📅 18:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3050">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/iaghapour/3050" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3049">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjwVzNvJvwti5gXw7cBuFqbjpFxwwiP7Pqx75ZlSLuFLJTKtevHK2y01RKPPylwDuAVCFc6w-ldIBUiWYBYn6bof5hvWCBq8EtFMVnussurHvXB3px0BLnHuYIoTGMipHVP900VWPJwPCCQilmOOX2cY2z7K4-KWoQ3psDKbAYPR7YPyqOVU6dtszgu6NycKc-DjUAcOtElpkF02kaztm1SpELmtksm4TCVa78TFujFAPvNWnSDIQxKP9UJudf7Pcwo-OqEH-wTfijutHELJf_sImO0CEWR7_1IiYcKeBnfeFS0XnobkTXqeMWGiWxDEb3tgW5ztvm6V0jaNRyZyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی بدون تانل + پنل مدیریت (مشابه شکن)
🔹
خیلی وقت‌ها برای دور زدن تحریم‌های اینترنتی (سایت‌های برنامه‌نویسی، بازی‌ها، صرافی‌ها و...) نیازی به درگیری با تانل‌های پیچیده نیست. تو این ویدیو بهتون آموزش میدم چطوری یک تحریم‌شکن شخصی قدرتمند (مشابه سرویس شکن) بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/iaghapour/3049" target="_blank">📅 17:14 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3048">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr3ystJFpDforL70HpDMO9eGMPn7AucirXzApN3y-rPh6VX_oXSTdVfjxHsZFzWK1uCpu8pyQlqdBdDsO8STCPoiUxCVH3Hyz9vnCADbIN816pd4UBvd55jhF8HiLIMZoL50Myz95dXV35fCrAtXzmFG5jIWklsY3xqZM49NivJxHVd8hlY6jEra349wkJSYo7_xZAUSlMDR-esSd397zlUCZ820nqcD4-PBN_KpDtbNzGzOu39kl-IU4QQ6VoCrYdBZlhwu3N0YuVMBmFUMzAdDqOz-DoraDxxjthcbqCkycN1JP2mkDawzuGUEN0QrU4AdLPoeyBOWx-9Ate2d0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی GPT-6 Sol و GPT-6 Luna؛ مدل‌های جدید اوپن‌ای‌آی با نصف قیمت!
اوپن‌ای‌آی دو مدل جدید
GPT-6 Sol
و
GPT-6 Luna
را با تمرکز بر سرعت بالاتر، خطای کمتر و
۵۰٪ کاهش هزینه API
معرفی کرد.
🔹
هزینه بسیار پایین‌تر:
ورودی Sol به ۲ دلار و Luna به ۰.۱۰ دلار به ازای هر میلیون توکن رسیده است.
🔹
عملکرد قدرتمند:
در بنچمارک‌های برنامه‌نویسی و اتوماسیون (نظیر AutomationBench و DeepSWE)، مدل Sol رقبا مثل Claude Opus 5 را با کسری از هزینه شکست داده است.
🔹
کاهش ۵۰ درصدی خطاها:
دقت اطلاعاتی مدل به سطح GPT-6 Astra نزدیک شده و پاسخ‌ها در کارهای فنی شفاف‌تر و کوتاه‌تر شده‌اند.
🔹
دسترسی:
فعال در API با شناسه‌های
gpt-6-sol
و
gpt-6-luna
، ابزار Codex و به‌صورت تدریجی در ChatGPT Work و دسکتاپ.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/iaghapour/3048" target="_blank">📅 16:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3047">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDtr282Lo8_z6YmNbeP7Qe3DFTIF7ou4FpQKBhw5Z8G0Q0FqmrfB5QRvMY9W1uq2ZGfyJ_n5s7FhQMTVcPl_C4gOWGIycFNAbbk6JXj5ZTzf2YdjaKkAdyC6ti8ID0DKP54ElUuhExrBnmmtNsk4FKcDEbhHunBMCgM-fw90T6c26vQGLTcLdS2P3yL0oEGKOGyUWO-ovjTNIosbGV0y-16DAtIOv-zTIdts_vuOE-BQ3Q6CFWmcmuh0887NGsXMSrdqjTRS_OPrK-JSoPY6LMlp6frRExVfSMovwFQqPER_nJvmTCo3eO1qmLbISYGGuMP_9N767QFnKI13MQw0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
رگولاتوری: آسیب کابل‌های دریایی عامل افزایش پینگ بازی‌های آنلاین است
سازمان تنظیم مقررات (رگولاتوری) در واکنش به اعتراض کاربران درباره وضعیت پینگ بازی‌ها اعلام کرد:
🔹
علت اختلال:
آسیب‌دیدگی و قطعی بخشی از کابل‌های ارتباطی دریایی در مسیر کشورهای همسایه جنوبی به دلیل حوادث ناشی از جنگ.
🔹
وضعیت تعمیر:
به دلیل ماهیت زیرساختی و نیاز به هماهنگی میان کشورهای واقع در مسیر، رفع مشکل زمان‌بر خواهد بود.//زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/iaghapour/3047" target="_blank">📅 14:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-3045">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=RyVKCczaL3llwhPGN0Vo0Zub-qqcLUmfyyyOlN77Oii-OVegT6M1dkvnyH-PkSnIbe0zY5xBDjIuOAQZkoWteFH0HqmoVzuoPPWtFj6HvCHSI95g4dyEW7ucSGaU6-i8VHfI4Vv7j4KFlj8P14BTHoT6J4EJQGTF-97qBu0n1vjRWBL7s0G07JzdtQdUWytzVwlt2RHVagnj4wknkIyOiokMUZpSaAe4NmEI35KUhjD4a_idN_TgqtGPzoWbe9wwOuj3KPouiwr6mW6ffsGi7aRt8bCNwnK3fX69BLAYqrY_JKML8kKcblY6kRT3eL4LpCoIUmOQToHRNMFx3YzTjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18b6a6a1bb.mp4?token=RyVKCczaL3llwhPGN0Vo0Zub-qqcLUmfyyyOlN77Oii-OVegT6M1dkvnyH-PkSnIbe0zY5xBDjIuOAQZkoWteFH0HqmoVzuoPPWtFj6HvCHSI95g4dyEW7ucSGaU6-i8VHfI4Vv7j4KFlj8P14BTHoT6J4EJQGTF-97qBu0n1vjRWBL7s0G07JzdtQdUWytzVwlt2RHVagnj4wknkIyOiokMUZpSaAe4NmEI35KUhjD4a_idN_TgqtGPzoWbe9wwOuj3KPouiwr6mW6ffsGi7aRt8bCNwnK3fX69BLAYqrY_JKML8kKcblY6kRT3eL4LpCoIUmOQToHRNMFx3YzTjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی اکانت هوش مصنوعی 18 ماهه (دوره دوازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی 18 ماهه مشخص شد:
👤
برنده عزیز با آیدی matintarafdar4000، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/iaghapour/3045" target="_blank">📅 20:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3044">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYqr5w7JWCrjUCaDHGYk84ORkHvBT8iWUEaSNgcpVdHQR9NCh7Pld-3dLehs667tTwa-hT3VmCyIegSme51xZL1bJYcuYvwv-6ql9AgnkyXlJ4lYyV7gA8E5uw6VJvWww14Q9JqHt6gHrGTZmRK7rFkZA_tlNh2l92G3ANyZa9GR8Kk7UQ4Lr53cy_9ojqrnCrkQyHG0SYAa6p0Kwh9EA6KePzV7acNGbYa9amNBiszf2VdVryDjW2ehzClgi_0UOv4HT6CBTrMERzZWOygSanwBPuYGTNbKXsMUPv00pF54uIFLLvgH9qvc34v_Krkm9AcN9GdZWHLCarvyqIEanQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل DeepSeek V4 Flash در OpenRouter رایگان شد!
نسخه
DeepSeek V4 Flash
بدون محدودیت سخت‌گیرانه (Rate-limit) روی پلتفرم OpenRouter به‌صورت رایگان در دسترس قرار گرفت.
🔹
سرعت فوق‌العاده بالا به لطف معماری بهینه MoE
🔹
کانتکست عظیم (بیش از ۱ میلیون توکن) مناسب تحلیل اسناد و کدهای حجیم
🔹
اتصال آسان از طریق API به افزونه‌های هوش مصنوعی در VS Code و ابزارهای مختلف
🔗
لینک دسترسی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/iaghapour/3044" target="_blank">📅 19:01 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3043">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l63qnsucf3BUtgP8A3EnXdlfDxTYTtnKtEBhWXYTaX_5h50HkNbLTeNSB2HUdsqg_aLfQhe4pQ48EelVc32A7QLVM83_lCWhnmhHO5nr8b8C-8KXpmDGjIzh9rOKcCSR4Wy0P_D0mbeOPeygxO_RaN2t4T9ozs8pOz8J-OTr5DglEDHbi7e8u5bft6uQ2Az8udRSOyfFByBVd4LIuT3xtXT5yiJw27o3kn6MDZKeHiSou0SQyZJ0ktZhj9TWWNPncEgfB7aS_hJDH3kmeD4edX4vNxrixq8GMb8ILT6bvDEGEuBsbCqXv79bCAh3g9DEaZkT9dFhJxbv3OIN32si1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارت اینترنت دیال‌آپ، صدای قیژوویژ مودم و استرس اینکه مبادا کسی تلفن خونه رو برداره قطع بشیم... و در نهایت رسیدن به این صفحه جادویی!
✨
نسل جدید هیچ‌وقت لذت و هیجان این لحظه‌ها رو تجربه نمی‌کنه:
• لرزوندن صفحه چت طرف با BUZZ وقتی جواب نمی‌داد
😂
• ساعت‌ها گشتن تو روم‌های ایرانی و چت با غریبه‌ها
💬
• تیک زدن گزینه
Sign in as invisible
برای اینکه مخفیانه بیای.
👀
• استاتوس‌های سنگین و خفنی که با کلی فسفر سوزوندن می‌نوشتیم!
تلگرام و دیسکورد هرچقدرم پیشرفته باشن، اون ضربان قلبی که موقع چرخیدن این آدمک طوسی و لاگین شدنش داشتیم، دیگه تو تاریخ اینترنت تکرار نمیشه.
😊
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/iaghapour/3043" target="_blank">📅 17:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3042">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmUe4bpECC1shYyOpWjXysBM4UzxY5KEjC8wfAkaDhLt3rbdss2eIYi-PeM5Skh1XWSXHSeDQa147b_ddjwd-0ZuaKNjr4VgFNdinV6B7EsNfGKbYGcDetuVZeZhOO6bxCIFp6Ieihcdj_kIZutOhYtn3Mo2NQfqhmuHan9mTVpgyGNbH6QSGfqYKOv15QXEbGqVLu3P5Dxg-WdVWllZ3lO7WQaJVp6NGq8lSIyb56y6T8nCpgS425cWzV830P2cer4SgeeiWLFyOENGCVWHazFaSv2EgMif52tYX330_8tWkH6jqijqtsJKveHOLFhMByb1Ciw_4zO_J8rJ1e6WQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هشدار مهم امنیتی: انتشار آپدیت حیاتی سپتامبر ۲۰۲۶ برای اندروید ۱۴ تا ۱۷ با رفع ۱۸۰ آسیب‌پذیری
گوگل به‌روزرسانی امنیتی ماه سپتامبر ۲۰۲۶ را برای نسخه‌های
اندروید ۱۴ تا ۱۷
منتشر کرد. این بسته به دلیل تغییر سیاست گوگل به بولتن‌های فصلی و عدم انتشار جزئیات در ماه‌های جولای و آگوست، حجم بسیار بالایی دارد و
۱۸۰ حفره امنیتی
را ترمیم می‌کند که بیش از
۳۰ مورد از آن‌ها دارای سطح خطر «حیاتی» (Critical)
هستند.
⚙️
تفکیک پچ‌های امنیتی:
🔹
پچ اول (سطح سیستم و فریم‌ورک):
رفع
۹۵ باگ نرم‌افزاری
که شامل ۲۶ رخنه حیاتی در هسته سیستم و فریم‌ورک اندروید است؛ خطرناک‌ترین آن‌ها امکان
اجرای کد از راه دور (RCE)
بدون نیاز به تعامل کاربر را به مهاجم می‌داد.
🔹
پچ دوم (سخت‌افزار و تراشه‌ها):
ترمیم
۸۵ آسیب‌پذیری
مرتبط با چیپست‌ها و درایورهای سخت‌افزاری شرکت‌هایی نظیر کوالکام، مدیاتک و آرم.
⚠️
خطر حملات هدفمند علیه گوشی‌های پیکسل:
گوگل تأیید کرده که شواهدی مبنی بر سوءاستفاده‌های محدود و هدفمند هکرها از برخی از این آسیب‌پذیری‌ها روی دستگاه‌های پیکسل مشاهده شده است.//پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/iaghapour/3042" target="_blank">📅 16:28 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3040">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncz6ZyJHFMiy8FA3Ml8u7IvTTUyySlXIHFI2OQRBLZ8OcFl8w4flgS6alJPM0Eg4g6K8P60KvahNgX2QrmRIsVjdUQmVenuwTMRnIwey9o7Xsc_eLShGLFxCeMJCKa1VZDXC_7n7Misyz1asMP5swIesGRDT2BA3E87o3qCz0NC_zIjfyqcetQFbG8-0BEm2-hs2BgA9ElEOYLUj7SP4CtpXuJ-qfJCQv5g2a3BrdD-l--Mnfj05J_Q-_T9wTn-eVSo_3mOdg1PTLD5-dlbVGdSE-JnUrsCJmrzokh4sIv6AntlgKMsmbrZU3JTyNsDwwMV4SE5HG1nZD5I1F_KBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
آماده‌سازی اینترنت برای AI Agentها توسط کلادفلر
کلادفلر در حال ساخت زیرساختی است تا عامل‌های هوش مصنوعی (AI Agents) بتوانند پروژه‌های توسعه‌یافته روی
localhost
را بدون دخالت انسان تست و اجرا کنند.
⚙️
نحوه کار:
🔹
ساخت فوری URL:
با ابزار
TryCloudflare
، ایجینت بدون نیاز به دامنه یا لاگین، سرویس لوکال را به یک آدرس اینترنتی عمومی و موقت تبدیل می‌کند.
🔹
تست و بررسی با مرورگر:
ایجینت آدرس ساخته‌شده را با مرورگرهای هدلس کلادفلر (مثل Browser Rendering) باز می‌کند، المان‌ها را بررسی و خطاهای کنسول را می‌خواند.
🔹
دیباگ خودکار:
در صورت وجود باگ، ایجینت خطاها را تحلیل کرده و کد را در لحظه اصلاح می‌کند.
🔗
تست سریع ابزار
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/iaghapour/3040" target="_blank">📅 20:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3039">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFpbfs6wCvZNZv5pwJxJR_orVrjxVIcK2ki_p8qOAs9Ok4-MJenuDpffsGCYux8LCOCNLSTYGNZZxTBQVBQdMI6PcMRWyK4MhXH3ZR9RdGOsNP9L0KwmcYHVaJTkYNPkQQmkwKlUjcWUMsyLtUcmqq-OXzB-HXqRN5UkJJUP5QyViutdR4JLMekjCPg1MFJVxLzcOQ4oH2nrFPSZo7tgvl-rjQ7DNaW7eEDBZ4Zxx3Y7O8F5VMnc_VQTT8Li7bXp9Nd803cQo6uwH0TH9Y6e_-uP4nbBIInssxNYc8Sal7umwxcczNuHSkCverEuWYrA-nQvxrDby7gevNemLaUKuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش افزایش سرعت بوت و بالا آمدن ویندوز
اجرای خودکار نرم‌افزارهای سنگین و انیمیشن‌های سیستمی از دلایل اصلی کندی بالا آمدن ویندوز هستند. با دو اقدام زیر زمان بوت سیستم را به حداقل برسانید:
⚡️
۱. غیرفعال‌سازی برنامه‌های استارتاپ (Startup):
— کلیدهای ترکیبی
Ctrl + Shift + Esc
را بزنید تا
Task Manager
باز شود.
— به تب
Startup apps
بروید.
— در ستون
Startup impact
به برنامه‌هایی با برچسب
High
دقت کنید (بیشترین مصرف منابع را دارند).
— روی برنامه‌های غیرضروری راست‌کلیک کرده و گزینه
Disable
را انتخاب کنید.
⚡️
۲. تنظیم سیستم روی بالاترین کارایی (Best Performance):
— وارد
Settings
شوید و به مسیر
System
⬅️
About
بروید.
— روی
Advanced system settings
کلیک کنید.
— در تب
Advanced
و بخش
Performance
، گزینه
Settings
را انتخاب کنید.
— تیک گزینه
Adjust for best performance
را بزنید و روی
OK
کلیک کنید تا افکت‌های گرافیکی سنگین غیرفعال شوند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/iaghapour/3039" target="_blank">📅 19:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3038">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwAnJSxgK4Lsb5v8Yp1qLTWz_BoM67r_992rMtG66G4GfMfEuiFUYlm7oH3Sa1Ji1kiSfvm4hUNFSp3GIwOGf7dWh8PgxIjrCHJ9gTaICD57uzTAxqCZjER1eCDer0Ib4ckV-q3lCfgN0W7UoAbHbndnw7LHhENSch65DhY1GAt2CcpcmWbcMXCqNlk1_x8SyBamD9Q2UgaV_JaGZ8bq9HtWdC9t4IYnhnQGpnGsvJ8Pnl_ijeGnl5LOtDu-q8dCJGWz2HBTedKn79NmA5P4dECWw7BXUcmmmTRFbIdDsizaZZ77WoPznusFA_BeojWlFZKHWRjVW8ISe-5sWSrsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
هوش‌ مصنوعی Qwen و Kimi هم کاربران ایرانی را محدود کردند؟
دسترسی کاربران ایرانی به دو ابزار محبوب هوش مصنوعی چین، Qwen متعلق به علی‌بابا و Kimi ساخته‌ی Moonshot، با اختلال جدی مواجه شده است.
🔸
گزارش کاربران نشان می‌دهد دسترسی به نسخه وب و حتی API این سرویس‌ها در برخی موارد با خطاهایی مثل 403 Forbidden مواجه می‌شود؛ با این حال، هنوز هیچ‌کدام از این شرکت‌ها به‌طور رسمی درباره مسدودسازی کاربران ایرانی اطلاع‌رسانی نکرده‌اند.
🔹
هنوز مشخص نیست این محدودیت موقت و مرتبط با سیستم‌های امنیتی است یا آغاز یک محدودیت جغرافیایی دائمی.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/iaghapour/3038" target="_blank">📅 14:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3036">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8YMVDHNBvdo-EJaBeqdonZfHwEC82HfAiKcIyG6hs-tXx8YcrfQbBSfAUcJ1EHuCOjJs3rqWodXz2mfC4LwVx9-P9TqDy-nVEtOgHrn08c_VbQoWjGRJ-lds2nDJSaRHPZkfJ_oNYhdfvbSaK6rJwbPzoa2uLR_4NV-8asFg7BwlsAlifAduVTQkjNT24cQx1IeLGXUSNnK_36EyHxgwhlWXOy5laKkQ2FjOk5RCB3ZPhFFuR8GuSej_9_TxdVyTaJmzlniwpzo9ddsYYMpeyBkRanrmUtKt2s2N7VWBWkYK4H3KYLgyvlnuwNPv-adwj-2AMQYoXIsEWz8kdeBpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
یک پنل، ۹ پروتکل فیلترشکن! با پشتیبانی همزمان
😍
🔹
در این آموزش، نحوه ساخت یک پنل حرفه‌ای با پشتیبانی همزمان از ۹ پروتکل و سرویس مختلف شامل OpenVPN، WireGuard، AmneziaWG، IKEv2، SoftEther، SSTP، L2TP، Cisco و Telegram Proxy رو یاد می‌گیری.
🔹
این پنل علاوه بر پشتیبانی از چندین پروتکل، قابلیت‌های متنوعی مثل نمایندگی، مدیریت حرفه‌ای کاربران و امکانات کاربردی دیگه رو هم در اختیارتون قرار می‌ده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو قرعه‌کشی اکانت هوش مصنوعی 18 ماهه داره،
برای شرکت توی قرعه‌کشی فرصت محدوده (شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3036" target="_blank">📅 17:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3035">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkq09qjDDLPKkLqGs2UodQacMH0VK7_OFKOdtEIVVgIJLDkOD28XI2r-WKOreUBTmKNhKA3gFjosoCn5OVAm-HtXVZX30kdVuOCyxFGl1L9hNiI46m0q-tl3-6O-5UqGull9eAj-sN-aa7JBPQ69sFCw3gObwFX_4FvMu_llqfayAfvT4GVBEHMelabxN2L0qST-gsHwOnR3aTOIAvqmFm6yLs95D5McCRtAEUIL8655RwYoEvecm_fmKUgH7u1sjNzkWrkKfosz57LQQ9riUQUL17IJa65kwIQngNpDF8iq4Gdsmbg3DoNje3EB6VoAZBit2GRbLcHZ3Uc-poa4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
حجم ویدیو و عکس‌هات رو راحت کم کن!
اگه برای ارسال یا ذخیره‌سازی فایل‌های حجیم ویدئویی و تصویری مشکل داری،
CompressO
می‌تونه یک گزینه کاربردی باشه.
🔹
یک ابزار
رایگان و متن‌باز
برای فشرده‌سازی ویدیو و تصویره که روی هر سه سیستم‌عامل
Windows، Linux و macOS
اجرا می‌شه.
🔹
پردازش فایل‌ها به‌صورت
کاملاً آفلاین
انجام می‌شه؛ بنابراین برای فشرده‌سازی نیازی نیست فایل‌هات رو روی سرور یا سایت خاصی آپلود کنی.
⚙️
این پروژه از ابزارهای قدرتمندی مثل
FFmpeg، pngquant و jpegoptim
برای کاهش حجم فایل‌ها استفاده می‌کنه.
🔗
مشاهده و دریافت پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/iaghapour/3035" target="_blank">📅 16:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3034">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشب روشن</strong></div>
<div class="tg-text">چشمان یک انسان دیگر باش... فقط با نصب یک اپلیکیشن رایگان!
👁️
❤️
.
تصور کن گوشیت زنگ می‌خوره؛ یه تماس تصویری ۱۰ ثانیه‌ای!
پشت خط، یک فرد نابینا است که فقط می‌خواد بدونه تاریخ انقضای این خوراکی چیه یا تابلوی جلوش چه آدرسی نوشته. تو توی چند ثانیه جواب می‌دی و استقلال و لبخند رو بهش هدیه می‌کنی!
✨
برنامه Be My Eyes داوطلب‌ها رو به افراد نابینا وصل می‌کنه تا کارهای روزمره‌شون رو راحت‌تر انجام بدن.
📌
چرا نصبش کنیم؟
🔹
کاملاً رایگان برای اندروید و iOS.
🔹
بدون تعهد زمانی (وقت نداشتین تماس رو رد می‌کنین).
🔹
حس فوق‌العاده با یک کمک ساده.
📲
دانلود:
نصب از گوگل پلی برای اندروید.
نصب از کافه بازار برای اندروید.
نصب از مایکت برای اندروید.
نصب از اپ استور برای آیفون.
📢
لطفاً این پست رو توی گروه‌ها و کانال‌های دیگه هم بفرستید.
شاید فوروارد شما باعث شه افراد بیشتری نصب کنن و گره از کار ده‌ها نفر باز بشه. مهربونی رو تکثیر کنیم!
🕊️
✨
.
@shaberoshanIR</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/iaghapour/3034" target="_blank">📅 16:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3032">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUBSlAjzrHzNweGxZBAYxeksDsiMwz1mmqyB_2AgMZT_vlbPS6B3PHhYQjFR2YHVj_WU3t43l1yAt2YGu5eINmXiVYv9LF--w-LLUpn-veOjuBXVWNUGn29U3DspbEyYOx1ygu995vr33I1TpehST-iR8IZK1YoAtg1HC4hpjMzzuRy-gKSs8-FosT1EoALUXxxacRhGqzKB7vJeYEJl7VMfQAco15v_9XLVN0bRXcLGLK__UseSM-t-2VsbSANzZo-hhmQcFBpOIUNvXUVgGiW0Sx8JNqQp0Q5I5bRrEQa_gfRLNeDbrsMsAfnqowT-YwP7lfuvv--8dVAuR7aNQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خروج جمنای از محیط آزمایشگاهی و نفوذ به ۳ شرکت واقعی!
گوگل اعلام کرد هوش مصنوعی Gemini در جریان تست‌های امنیت سایبری، به دلیل دسترسی ناخواسته به اینترنت، از محیط قرنطینه خارج شده و به زیرساخت ۳ شرکت واقعی نفوذ کرده است.
🔹
نقص در اتصال به وب:
دسترسی اینترنتی ناخواسته در محیط تست به مدل اجازه داد فراتر از آزمایشگاه عمل کند.
🔹
خطا در تفکیک هدف:
مدل قرار بود یک شرکت فرضی را تست کند، اما به دلیل تشابه نام، شرکت واقعی را هدف گرفت.
🔹
ورود با حدس پسورد:
جمنای با کشف و حدس گذرواژه‌ها وارد شبکه‌های این شرکت‌ها شد.
🔹
توقف خودکار:
مدل پس از تشخیص واقعی بودن محیط، عملیات را فوراً متوقف کرد و آسیبی به بار نیامد.
⚠️
باگ دسترسی اینترنتی در محیط‌های تست برطرف شده و به شرکت‌های هدف اطلاع داده شده است.
🧠
@NovinAIplus</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/iaghapour/3032" target="_blank">📅 20:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3031">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzwblrKTCFo5zDIEvvMrA1zt6EAJwepBpksSSucSM0EO0BiQYqU91lwOOKOF1PYH3LVaEKuT3HD9ohTHn-03G78uN2DQAmZm0u-ZZP_VHjYUjgE_F4tHbSJqHnSA4C1inXIacndNdOB4JLcdAi0uwxvviw6pf5SToGDLtRyWneOSho_uckDcopOXVJTjVpIKMW9UqNxZM6RCdIUAHOMsdzBu499kIHlPcTSKIegiwnERMBodVsD7h7cWkaH0jerJTOky_OLdCBG-7j33hVrwOgy7LIZChIEDTF7-aHuKudTJEhDTxahojb9nkvAeblLSiAlQrQ-tdUa5uCLSiWxNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توقف ارائه خدمات میکروتیک به کاربران ایرانی؛ روترها از کار می‌افتند؟
شرکت میکروتیک (MikroTik) در پی اعمال مقررات تحریمی الزام‌آور اتحادیه اروپا، سازمان ملل و آمریکا، ارائه خدمات و پشتیبانی مستقیم به کاربران با IP ایران را متوقف کرد.
🔹
روترهای فعال از کار نمی‌افتند:
سیستم‌عامل RouterOS پس از فعال‌سازی، لایسنس را به‌صورت محلی روی دستگاه ذخیره می‌کند و عملکرد روزمره روتر وابسته به اتصال مداوم به سرورهای میکروتیک نیست.
🔸
چالش‌های حساب کاربری و لایسنس جدید:
در صورت تعلیق حساب‌های کاربران ایرانی، فرآیندهایی نظیر خرید لایسنس جدید، انتقال لایسنس به سخت‌افزار دیگر، بازیابی کلیدها و ثبت تیکت پشتیبانی رسمی مسدود خواهند شد.
🔹
ماشین‌های مجازی و سرویس‌های ابری CHR که نیازمند اعتبارسنجی مداوم لایسنس و تمدید هستند، بیش از روترهای سخت‌افزاری با ریسک و اختلال مواجه خواهند شد.
🔹
با پایان رسمی پشتیبانی از RouterOS نسخه ۶ در سپتامبر ۲۰۲۶ و عدم انتشار پچ‌های امنیتی جدید، مهاجرت به نسخه‌های جدیدتر برای سازمان‌ها با وجود محدودیت‌های جدید با چالش فنی و لایسنس همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3031" target="_blank">📅 18:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3030">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1IjsQlS0Pon92NWsMzmuGR43Oafygqsx9-Z9Qc-TtC3EvSXVDSqpFKqA4az8MTOY066NCiBodAnc-qZsr_iQEFiWjma3Drs85Tip3RLSVg0aVFEFQwsbt1Rh24NxZvkg3BAu9PDphUFhaSm1H-86otovjtSeYN9lWP_ISaoPGHo8HZ_T3JDaAxl_u6MXu_2NbyeyszeztPylVWFrLgfg9nYkiWpr71oTRHsUPQ4jg6KtKtNYkPzNLHweTazfVqPYSEagfdXdvDW3Peh3Wg-KmElmbChOlDGtO3YpI4R5NCryFVkFumd_ea87LN_nNm_TRGTcGmMWVCFTLY6TQPhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎭
دم خروس پاول دورف از زیر لباس ایتا بیرون زد!
سال‌ها با بودجه‌های چند ده میلیاردی گفتن: «ما با اتکا به دانش بومی و نخبگان داخلی، پلتفرمی کاملاً ملی، مستقل و امن ساختیم!»
حالا توی جدیدترین آپدیت نسخه وب مسنجر ایتا، دولوپر خسته یادش رفته حتی کامنت‌ها و استرینگ‌های سورس تلگرام رو کامل Find and Replace کنه؛ کاربر زده سابقه جستجو رو پاک کنه، پاپ‌آپ اومده بالا با فونت درشت و انگلیسی:
«Telegram: Are you sure you want to clear your search history?»
قشنگ مشخصه برنامه‌نویسه کدهای Telegram Web رو کلون کرده، کنترل+F زده هرچی Telegram بوده رو کرده Eitaa، بعد سر این یدونه دیالوگ اینترنتش قطع شده یا چاییش سرد شده یادش رفته Replace All بزنه!
خلاصه که زحمت نکشید فیلترشکن بزنید برید تلگرام؛ خود تلگرام با سورس رایگان و دست‌نخورده در ایتا منتظر شماست، فقط سرورش توی ایرانه!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3030" target="_blank">📅 16:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3028">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔸
بچه‌ها چطوره تو ویدیوی بعدی به جای اکانت ۱ ماهه هوش مصنوعی، اکانت ۱۸ ماهه جایزه بدیم؟ نظرتون چیه؟
🔹
راستی، موضوع ویدیوی قبلی چطور بود؟ سعی کردیم یه خورده از شبکه فاصله بگیریم :) اگه دوست داشتید بگید از این سبک ویدیوها بیشتر بسازیم براتون.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/3028" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3027">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=Wt5UKu8PRVZ3y4SIQjROAZWmXOuL225agGCSM-ZX-wmoobEmbGEH_JI6ZoCS3R2fDbbr3aW3SJeGwikoU2mGEUcLXng56tAA1iPLTZeU4h_KxLqRYpGDsjoxsP4LsVoGzG6ap3Vni9QszmqD2p6_MWtv82Clx778Vz2LYMsR--_tcsMX4vLaNy9hRTjXr5WLi07GafikkN3i0QOLEvG_J8ieD4pr0K-0Qc2aOAq8sPgoJElyyzVDJrF6Nviju54ualedHymI9OHc0v-js-VdSrh1ZZ5S0Jb3JV7F-QK3G_61nHma6Mu6iVKOB8De3ZrQJnDgatkdcMEx4jqNgK8N7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90353dca7.mp4?token=Wt5UKu8PRVZ3y4SIQjROAZWmXOuL225agGCSM-ZX-wmoobEmbGEH_JI6ZoCS3R2fDbbr3aW3SJeGwikoU2mGEUcLXng56tAA1iPLTZeU4h_KxLqRYpGDsjoxsP4LsVoGzG6ap3Vni9QszmqD2p6_MWtv82Clx778Vz2LYMsR--_tcsMX4vLaNy9hRTjXr5WLi07GafikkN3i0QOLEvG_J8ieD4pr0K-0Qc2aOAq8sPgoJElyyzVDJrF6Nviju54ualedHymI9OHc0v-js-VdSrh1ZZ5S0Jb3JV7F-QK3G_61nHma6Mu6iVKOB8De3ZrQJnDgatkdcMEx4jqNgK8N7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤖
ورود مستقیم آنتروپیک به رقابت با آفیس و جمینای؛ معرفی قابلیت‌های Claude Docs و Claude Slides
شرکت آنتروپیک با رونمایی از دو قابلیت جدید متنی و ارائه‌محور، چت‌بات کلود را به ابزاری جامع برای محیط کار و رقابت مستقیم با پلتفرم‌هایی نظیر گوگل داکس و جمینای تبدیل کرد.
🔹
ابزارهای Docs و Slides (نسخه بتا):
کاربران اکنون می‌توانند مستقیماً درون محیط چت، اسناد متنی کامل و فایل‌های اسلاید ارائه ایجاد، ویرایش و دانلود کنند یا لینک اشتراکی آن‌ها را برای دیگران بفرستند.
🔸
همکاری تیمی هم‌زمان و ثبت کامنت:
همانند گوگل داکس، فایل‌ها قابلیت اشتراک‌گذاری، ویرایش گروهی به‌صورت زنده و ثبت بازخورد یا کامنت توسط همکاران و خود چت‌بات را دارند.
🔹
عرضه و دسترسی:
این قابلیت‌ها ابتدا برای مشترکان پلن‌های Pro و Max در وب، دسکتاپ و موبایل فعال شده و به‌مرور در اختیار کاربران رایگان و پلن‌های Team قرار خواهد گرفت.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/3027" target="_blank">📅 17:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3026">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9NaUHeGm1gDxVSV7c-PxDuPFMSNDuLSio13NO-BlHpYBrBfTxTckU6MygfR6pgGXTH9csWOTlgrJuuzLkozfg5Tbx_TA6-dzO25jsOXWR-nivGxq_utZ_1bUCB7pbBTRQSSpVvXhhFA_ilFvLlxzkrhgfLTa9vzbs9Kdm1xconhWYQIJlQI_prxCNrouAIfwo9vkATbl7U3iwnaCsyUO4mLQo__3rZT1-lj0p0NCVUSzg0kP82qxNvhv4Qbx86e4l3p3Pl5kwXpuJa89XEZDmQR5hi2iVRnZ5CgL_RmrRwX479HbUSdLT8YWEj9JhKb5VFYaF0wfO9HEiQMPAr7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
هشدار پادشاه بریتانیا به غول‌های هوش مصنوعی: تضمین دهید سرنوشت بشر از کنترل خارج نمی‌شود
چارلز سوم در یک رویداد سلطنتی در اسکاتلند، با چهره‌های ارشد هوش مصنوعی پشت درهای بسته دیدار می‌کند تا از آن‌ها تضمین بگیرد که پیشرفت پرشتاب این فناوری آینده و بقای بشریت را تهدید نخواهد کرد.
⚙️
نکات کلیدی این نشست و حواشی آن:
🔹
حاضران کلیدی نشست:
دمیس هاسابیس (هم‌بنیان‌گذار گوگل دیپ‌مایند)، نمایندگان ارشد OpenAI، انویدیا و آنتروپیک، به‌همراه کاناتیشکا نارایان، وزیر هوش مصنوعی بریتانیا.
🔸
شکاف عمیق میان رهبران فناوری:
درحالی‌که داریو آمودی (آنتروپیک)، سم آلتمن (OpenAI) و دمیس هاسابیس خواستار ترمز در توسعه و مدیریت ریسک‌های مرگ‌بار این فناوری هستند، جنسن هوانگ (مدیرعامل انویدیا) با هرگونه توقف، کندسازی یا قانون‌گذاری مازاد مخالفت کرده است.
🔹
نگرانی از پژوهشگران فراری:
هم‌زمان با این نشست، استعفای دو تن از محققان برجسته دیپ‌مایند و آنتروپیک با ادعای «مرگ‌بار بودن پتانسیل‌های کنترل‌نشده AI»، موجی از هشدارها را در محافل علمی و رسانه‌ای ایجاد کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/3026" target="_blank">📅 16:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3024">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVe--QIaX6nnUvYgoHactKgnh2seyrnuEYwpCz-ne8KJwus_XJpePdp09By2JRJYac1jkD9YCWs8QCzhBi0UTIF4VWf1i0v4pBV75IR1-HA2vxbAQKPh-QF8GorqoowmGsgQZs2HgXt0_BkxGGjhvTu4pVN2YG7hG-9b6--flxXn-_G1n9uYf94qj6DP3iG1C716Ma58pSQC2yBr-XPVNcDMZmZzfQbkCRJztcc-pV4oKXwRYDGXomrq7nuoehGJj2wiMdaVAYvUwDzUUGJrWsDiNSAiAM3-lU1mcF9Tg8t7jpXMPd6XFzsUtF2tAwiMEPRbO64C0_F-JSoypXtQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دانلود فایل ایزو ویندوز اورجینال از سرور‌های مایکروسافت (با ۱ کلیک)
🔹
اگه از نصب ویندوزهای دستکاری شده و پر از باگ خسته شدید این ویدیو دقیقاً برای شماست. تو این آموزش، ۲ روش فوق‌العاده ساده و سریع رو بررسی می‌کنیم تا بتونید با ۱ کلیک، فایل ISO ویندوز اورجینال (ویندوز ۱۰ و ۱۱) رو از سرورهای خود مایکروسافت دانلود کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#ویندوز
#اورجینال
#windows
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3024" target="_blank">📅 17:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3023">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAxehtM9lAcx0DzwIYrZ861q9MX8MHeKIYrDVJVOmOcVUPWHjvAushf-hE_6LC5qZOgvJjl6Nb15zuMY0nuanf2wmFBn_u1g3HvljeeEKnXlc1agQjIzJQNWVm89BxTarp0ma3UIMRRqW4e7IVpA6NA6KaNP6hoMjblVg_JRGAnH5zcSnu3kFxUNsi_jRS4MSzPASqM2D9FMUNBbBjNskpT2BMDCEvlIx2rxa44xc-_oDUh93xyNmm-Z_On-0HHpg4E2Ho2RyxLBMtMctRV_7KCJNMkBfwwX5ttRadzgTX-XFoOfPs1b7pUX2_eJ_Fak1qyGMJ9TkVMMShC3masJDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
کرکر سرسخت دنوو با وجود شکایت قضایی دست از کار نمی‌کشد!
با وجود فشارهای حقوقی و تلاش شرکت توسعه‌دهنده نرم‌افزار ضد دستکاری
Denuvo
برای شناسایی و توقف فعالیت کرکر ناشناس، او اعلام کرده به دور زدن قفل بازی‌های ویدیویی ادامه می‌دهد.
🔹
شکستن قفل‌های پیچیده:
قفل دنوو سال‌هاست به‌عنوان سرسخت‌ترین لایه حفاظتی بازی‌های ویدیویی شناخته می‌شود و دور زدن آن مهارت بالایی می‌طلبد.
🔸
شروع درگیری قضایی:
کرکری با نام مستعار
voices38
توانست پس از حدود یک ماه و نیم قفل بازی
Resident Evil Requiem
را بشکند؛ اقدامی که خشم دنوو را برانگیخت و باعث آغاز پیگیری‌های قانونی برای فاش‌کردن هویت واقعی او شد.
🔹
پیام جسورانه در ردیت:
با وجود تشکیل پرونده قضایی و تلاش برای شناسایی او، این هکر با انتشار پیامی در ردیت به کاربران اطمینان داد: «همه‌چیز مرتب است و تمام کارها طبق روال عادی ادامه خواهد یافت.»
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/3023" target="_blank">📅 16:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3021">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یه مدته زیادی رفتیم تو فاز شبکه و ساخت فیلترشکن و این داستانا :)
گفتم یکم تنوع بدیم و بریم سراغ ویدیو‌های متفاوت‌تر؛ از اونایی که اتفاقاً خودتونم خیلی پیگیرش بودید و درخواست داده بودید.
فردا یه نمونه‌شو براتون می‌ذارم، ببینید چطوره.
😉</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/3021" target="_blank">📅 20:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3020">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ee3UxHsIGsTPz_sDwokcr0aeijnxEYBF8ZDarPOZcl9jDrfx9fnN1wUX0X346N73pLu1p9nJJPi1ogKmZ_WZmv5G9DC3lmrFCdYzTPVA8nOUEejcs1EELUh3wmlwc6obFbaZZNEI-iQF8eyJJRmram6NlLOhGd9CVXJBRpiCyWjDxQX7VjKk1-q_Gz4eH-9nwoNMk3l6GU6i_k99YYngsNq8JpZTPHaYFrJ1idJgLQrpf5sLYXGjLAf2cdfGZJZWJE7xCEYbv42AVPqFZC7LzhIIYoP_kCNGJlPu-ty7IzsnDt0aC0dZmQB2VmWvDpOtXSxkuyRdZ3ZPxJo_V_FTdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Screenbox؛ پلیر مدرن، سبک و جایگزین شیک VLC برای ویندوز
اگر پلیر پیش‌فرض ویندوز نیازهایتان را برطرف نمی‌کند و از طرف دیگر ظاهر قدیمی، شلوغ و منوهای تو در توی VLC کلافتان کرده، برنامه متن‌باز
Screenbox
دقیقاً همان گزینه‌ای است که دنبالش هستید؛ پلیری با موتور پخش قدرتمند VLC اما با رابط کاربری کاملاً مدرن و هماهنگ با طراحی ویندوز ۱۱.
🔹
موتور پخش قدرتمند LibVLCSharp:
اجرای روان تمام فرمت‌های صوتی و تصویری رایج، پشتیبانی دقیق از انواع زیرنویس‌ها و هماهنگی کامل با موتور اصلی VLC.
🔸
طراحی بومی و مینیمال ویندوز ۱۱:
رابط کاربری مدرن، شفاف و چشم‌نواز بدون گزینه‌های اضافی و سردرگم‌کننده.
🔹
بهبود کیفیت تصویر (Upscaling):
قابلیت ارتقاء وضوح ویدیوها در محیطی با تنظیمات ساده، سرراست و قابل‌فهم.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/3020" target="_blank">📅 20:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3019">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tiw4mfjPgmkxzJAItrVD7eIr5NnAABaDtKvjQ0y4tV05u1tdBvhI1bMQn0vyRW5NO1VxbFnxN98sD-dZ5ki9MuJxPYJMtbnOlaV_sgo6J6hbQle4vq8bR4qtJEWWYG4Ncs7x3rNd9Nqs4Blc-hLtzBdsmVf7_o8xejAFAP7pKLulUAPgQdLVIuIaewrgxrsg7CGNcxhrxfW9gGhfwdk9_ZQaebWzXG7D7QFjIm59qH678JfSj_fEK4bsENN3kqOQTG1YeKq6YR85bejm-FP_FDaLYA4yOyOs_kaZ8gMN0JXdL1-FSV7XFX9Wfoz5veUoHyEHQWKZN__NpmfN7MoKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اعلام تعطیلی رسمی صرافی کوینکس (CoinEx) پس از ۹ سال
صرافی شناخته‌شده
کوینکس (CoinEx)
که از سال ۲۰۱۷ فعال بود و به‌دلیل عدم اجبار احراز هویت (KYC) در سال‌های گذشته یکی از اصلی‌ترین مقاصد کاربران ایرانی به‌شمار می‌رفت، رسماً اعلام کرد که فعالیت خود را متوقف کرده و تا
۱ دی ۱۴۰۵ (۲۲ دسامبر ۲۰۲۶)
به‌طور کامل بسته خواهد شد.
⚙️
زمان‌بندی مراحل تعطیلی صرافی:
🔹
۲۴ شهریور (۱۵ سپتامبر):
توقف ثبت‌نام کاربران جدید و انتقال بخش معاملات فیوچرز به حالت Reduce-Only (فقط بستن پوزیشن‌ها).
🔸
۳۱ شهریور (۲۲ سپتامبر):
توقف کامل معاملات فیوچرز، استیکینگ، وام‌دهی (Lending) و بخش واریز اکثر ارزها به صرافی.
🔹
۷ مهر (۲۹ سپتامبر):
توقف معاملات اسپات (Spot) و بازخرید توکن CET با نرخ ثابت ۰.۰۰۵ تتر.
⚠️
نکته بسیار مهم:
صرافی اعلام کرده رمزارزهای غیر از تتر را ترجیحاً تا قبل از ۷ مهر خارج کنید؛ پس از این تاریخ ممکن است دارایی‌های غیرتتری به تتر تبدیل شده یا رمزارزهای کم‌حجم پشتیبانی نشوند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3019" target="_blank">📅 17:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3018">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeWjNfC8nRe2_uGEjQjvJ5JwCQh4-qcSfw7BoqYd3bnSWsMZ6NknMaQFIpaTWSQo8CNSLQGalalFvpEIUb6WOskAMLYGWvNkQa_MZDXOGT2j2bwwHeeK_j2whEX2toscOv_nvysIqY14bOL2qNRN8EmNKy5b_f2ocjz9MD0jS57-MXLdF5xaXBJoOBI5k2Ue-L5wu6wZ3GtLIK3zy4uu3D3xGqQpZMKAXO_NGtY4iQnPfHbAvdpoyAESrWtlbKsEe5hEQVwN5YB_fat4Ln25xVwH9CRMFS-wePMCQwT3l0BQ0XnZWV7QHy9YWDM8wAWbt8P4E7eIWwGU_922mNqreg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
معرفی Subify؛ افزونه هوشمند ترجمه و دوبله زنده ویدیوها به فارسی
سرویس
Subify
یک ابزار کاربردی و مدرن برای مشاهده ویدیوها با زیرنویس دقیق فارسی و حتی دوبله صوتی هم‌زمان است که بدون نیاز به دانلود فایل جداگانه و با استفاده از API شخصی هوش مصنوعی کار می‌کند.
🔹
ترجمه آنی و بدون تاخیر:
استخراج مستقیم کپشن‌های زمان‌بندی‌شده یوتیوب و ترجمه پیش‌دستانه (Pre-fetch) با سینک زمانی میلی‌ثانیه‌ای بدون معطلی.
🔸
دوبله زنده صوتی
: دوبله هم‌زمان صدا بر بستر مدل‌های جمنای، با امکان تنظیم بلندی صدا، کاهش صدای اصلی ویدیو (Audio Ducking)، انتخاب گوینده و تنظیم سرعت.
🔹
پشتیبانی از مدل‌های AI متنوع:
اتصال به کلیدهای API شخصی در Google Gemini ،OpenRouter و OpenAI به‌همراه سیستم فال‌بک (Chunked) هنگام قطعی مسیر لایو.
🔸
شخصی‌سازی و فونت‌های فارسی:
تنظیم کامل فونت، سایز و استایل زیرنویس با فونت‌های جذاب وزیرمتن، استعداد و لاله‌زار به‌همراه پیش‌نمایش لحظه‌ای.
🔹
استخراج لغات کاربردی از دل ویدیو و امکان مرور کلمات به‌صورت فلش‌کارت در حافظه محلی مرورگر.
🔗
دانلود
افزونه برای انواع مرورگر
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/3018" target="_blank">📅 14:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3016">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abpIBWJKdo_YipJ8glSS20MCWZiA2QUuck7VzgB7Zt302jx0etq8scnREJhGs1bZgRp9_SL9h23bwNvjNzj1yoNu_CZ336POQWIlY2RV4Gl75QNaZL4cQ0boJwmunl299zSSWQK3JBniRzQz3mbmfYNTxE-NAVaifDWX2Vq6uaPG7RHSVgt6DXEC9RoScVDyJPrV47_lfpRu4-1XafU4yrpwfOfwX6LXrAnQXiY2ChBOY9B-qvxcelFdC959fF4NPcgevHo17bI__HjbiwPCWSaoYLaoZd6nmmNarpkN-IB1AFLw9FifCEEhjApC9Oo9U4ebn0jHqTb1u_KfJEvDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل سبک Zefira؛ مدیریت هم‌زمان چندین پروتکل
پنل
Zefira
یک ابزار پایتونی سریع و کم‌حجم (مبتنی بر FastAPI و SQLite) برای راه‌اندازی و مدیریت اکانت‌های VPN است که بدون درگیر شدن با Docker، امکان ارائه چندین پروتکل را در قالب یک لینک اشتراک واحد فراهم می‌کند.
🔸
پشتیبانی از پروتکل‌های اصلی:
پشتیبانی از VLESS (همراه با REALITY و چرخش خودکار SNI)، هسیتریا ۲، تروجان، VMess، شادوساکس، WireGuard و OpenVPN
🔹
لینک سابسکریپشن یکپارچه:
ارائه همه کانفیگ‌ها در یک لینک با خروجی‌های Base64 و فرمت Clash YAML
🔀
مدیریت تانل:
تسهیل ارتباط سرورهای ایران و خارج به‌همراه بررسی وضعیت اتصال نود ایران.
👥
کنترل دقیق اکانت‌ها:
تعیین حجم، تاریخ انقضا، لیمیت دستگاه، فعال‌سازی با اولین اتصال و تایید دو مرحله‌ای (2FA).
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/3016" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3015">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=luxeEDfcPEf1ixnxSt4k8auiqCGVFfXYyVCKv94xJcEuzAPNVwAqbYKK2wn2MvYafk7L4I3V_NUJa29aVejGjuvr10Bsm6ibrCpH-JeHqSgrkARUKTpd8IdYzz9C9B_UEYcGmvu2dhiPXh_YvPjyXck-Z_tYkfQRRB5Jj21Rz3nAxhg6jxMkfAPwCGML5G03CIOXwCT4jIHOCgApH8Lt715ovEkNECVUcw5x4mXnt9bWKJyb1aHhQvgw0E33nn4YFLjECSZDjQ-sr8nY17m1XtVIr_BUHx3xdJV3FB5IWI_gUrsu15QJK5jevh6E_9W0WnMrmxYoSP3DoEMaKrpLLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/004cfc664f.mp4?token=luxeEDfcPEf1ixnxSt4k8auiqCGVFfXYyVCKv94xJcEuzAPNVwAqbYKK2wn2MvYafk7L4I3V_NUJa29aVejGjuvr10Bsm6ibrCpH-JeHqSgrkARUKTpd8IdYzz9C9B_UEYcGmvu2dhiPXh_YvPjyXck-Z_tYkfQRRB5Jj21Rz3nAxhg6jxMkfAPwCGML5G03CIOXwCT4jIHOCgApH8Lt715ovEkNECVUcw5x4mXnt9bWKJyb1aHhQvgw0E33nn4YFLjECSZDjQ-sr8nY17m1XtVIr_BUHx3xdJV3FB5IWI_gUrsu15QJK5jevh6E_9W0WnMrmxYoSP3DoEMaKrpLLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی (دوره یازدهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mahdi9226، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/iaghapour/3015" target="_blank">📅 20:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3014">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fx18SmcfNqFxolL9JavAzgRB1Jjh6TNPZ6VP6Icl_HjroeaB47ySk-JaZyYSvJgszfOBJponm4SJ1ywb2XqiIVa6bfkbPqUBGvqUfzp_BaHt-WPztrekwbW_9vyvy14hndw9JtV6B0mvc1eRwouGFDKyFljrIHPvIte-n1Q3qj0A3qKP0qxiohS2VhupNKMI6LvosYSh8WQ537EAuuJ09VS4UHr3fXs5LBpmG1vVTCKb5qXdmXYi-ey7wcekNilklxdSKi13KkH47h0_QrHdqNsAiZC0LrZ97gtK10s7l1N5zOl1yTZVwgzPAoBYwEMhOdU8GJUpW0rCaWJ5UFsAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی DNS Changer؛ ابزار مدیریت و تغییر سریع DNS برای تمام پلتفرم‌ها
اگر برای گیمینگ، عبور از تحریم‌ها یا افزایش امنیت مدام در حال تغییر DNS هستید، برنامه
DNS Changer
یک ابزار رایگان و کراس‌پلتفرم است که این کار را با یک کلیک و بدون نیاز به دستکاری تنظیمات شبکه سیستم‌عامل انجام می‌دهد.
⚡️
پشتیبانی از بیش از ۳۰۰۰ سرور DNS:
دسترسی به دیتابیس عظیم ارائه‌دهندگان معتبر جهانی به‌همراه تست پینگ لحظه‌ای.
🛠
شخصی‌سازی کامل:
امکان افزودن، ذخیره و دسته‌بندی DNSهای اختصاصی برای استفاده مجدد.
🖥
پشتیبانی از همه سیستم‌عامل‌ها:
دارای نسخه اختصاصی برای اندروید، ویندوز، لینوکس، مک و محیط خط فرمان.
🔗
دانلود برای پلتفرم‌های مختلف
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/3014" target="_blank">📅 17:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3012">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚀
نصب خودکار و یک‌کلیکی اسکریپت‌ها در پنل دوپراکس!
🔹
دوستان عزیز، همونطور که در ویدیوی آموزشی مشاهده می‌کنید، پنل دوپراکس (Doprax) یک قابلیت فوق‌العاده جذاب در بخش
مارکت
داره که کار شما رو برای راه‌اندازی سرویس‌ها بی‌نهایت ساده کرده!
🔸
دیگه نیازی به درگیری با کدهای پیچیده، ترمینال و تنظیمات طولانی نیست؛ فقط با چند تا کلیک ساده می‌تونید هر اسکریپتی که نیاز دارید (مثل پنل معروف 3x-ui) رو در کمترین زمان روی سرورتون نصب کنید.
📝
مراحل نصب خودکار:
1️⃣
ورود به مارکت:
از منوی پنل، وارد بخش مارکت (App Market) بشید.
2️⃣
انتخاب اسکریپت:
از بین برنامه‌های موجود، اسکریپت دلخواهتون (مثلاً
3x-ui
) رو انتخاب کنید.
3️⃣
انتخاب سرور:
سروری که از قبل تو پنل ساختید و آماده کردید رو به عنوان مقصد مشخص کنید.
4️⃣
نصب با یک کلیک:
در نهایت فقط کافیه دکمه
Install
رو بزنید!
✅
نتیجه:
سیستم به صورت کاملاً خودکار تمام کارهای لازم رو انجام میده و اسکریپت رو روی سرور شما نصب می‌کنه و اطلاعات ورود رو در اختیار شما قرار میده.
🌐
وب‌سایت:
www.doprax.com
💬
کانال دوپراکس:
@dopraxcloud
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/3012" target="_blank">📅 20:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3011">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhmNZKmLNUrEtQw7zCHPWFKTqI4yq3W40Ze0x2zW4liPSOXQdG9d8jR3-ExuVF--qnME3qhfFKYTPSeNld1i-3y_WfPfnDWM8c1iuLRh_o_8xq0aC0HEAP2JI80nVIZYlAqUgR-uyjF7-m71KyDeCtXeWcu_uKRhHtnUW5IkrlH_vRzRkXn_Nr5bdSsKPd5gjt0Z1rDvz4AP-_CmyN6bcxYg50-K0gftQNVaUu39Cf5ZnzQ9jzD7p8tq_Qu5_MhpKJjsEaKuAaIpBhd3Yr2NnJCPgqO6mPy_ZcccVoT1OWpHByz4CHw3O4rRR2JDUHOVLgcrstbkiIp3ELax-V74HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل idontScanner | جعبه‌ابزار تست شبکه و TLS روی VPS
اگر مدیر سرور هستید یا می‌خواهید کیفیت اتصال، اختلالات شبکه و وضعیت پروتکل‌های امنیتی سرورتان را دقیق رصد کنید، پروژه متن‌باز
idontScanner
یک ابزار سبک، سلف‌هاستد و سریع برای همین کار است.
🔹
کالبدشکافی دقیق TLS & SNI:
تفکیک دقیق زمان‌های DNS ،TCP و TLS Handshake به‌همراه نمایش جزئیات گواهی SSL، نسخه پروتکل، Cipher و ALPN.
🔸
بررسی در دسترس بودن Endpoint برای لینک‌های VLESS ،VMess ،Trojan ،Shadowsocks ،Hysteria2 و WireGuard (بدون ذخیره افشای کلیدها و UUID).
🔹
سنجش لتنسی، جیتر و پاسخ‌دهی پلتفرم‌هایی مثل YouTube ،Instagram و Telegram مستقیماً از مبدا سرور.
🔸
دارای رابط کاربری روان به همراه منوی مدیریتی تحت ترمینال برای تغییر پورت، مشاهده لاگ‌ها، اتصال ربات تلگرام و آپدیت بدون از دست رفتن داده‌ها.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/iaghapour/3011" target="_blank">📅 19:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3010">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hkBEZRPyYovv_8FJ87Tra3U014pn68H4pySyb-P464kk9KnM-ZCxlcEy93y68PFYKQRwWV91E25lmRifrsv9chp3_GsHiyJmWwl1QNkfc-kJVlCyr82LdN9iPCNKItk8UReomqhj88S6fnVayELLf2w47bwfDdYiRdNDlfAEhecx0g6gp8l4dN-nq7T80S90kqSFhd7smda4h7Rfc8yjtAveJciA2q_TrimcF6qw6HX_HFlYAvY583mD3mWNgmRPdLy6oaE7TN12g43y_0_vr_V9pBanhh5AgU31km6HcVgw_WJQz7G1u5SG68J4PcDKyBvgoJnv5wwGqMMMrDuztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
اعتراف مدیرعامل زیرساخت: ۱۰ درصد ترافیک اینترنت کشور به استارلینک کوچ کرد؛ سهم 5G تقریباً صفر!
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، در نشست خبری خود از واقعیتی پرده برداشت که نشان‌دهنده شکست سیاست‌های محدودسازی اینترنت است: حدود ۱۰ درصد کل ترافیک کشور اکنون روی بستر اینترنت ماهواره‌ای استارلینک جابه‌جا می‌شود.
🔹
سهم ۱ ترابیت‌برثانیه‌ای استارلینک:
اکبری اعلام کرد با وجود بازگشت ۹۰ درصدی ترافیک، ۱۰ درصد باقی‌مانده دیگر به شبکه داخلی بازنگشته و جذب مسیرهای ماهواره‌ای غیررسمی شده است؛ حجمی که حتی از کل ترافیک برخی اپراتورهای داخلی فراتر است!
🔸
تداوم فعالیت ترمینال‌ها:
به گفته وی، استفاده از استارلینک به‌ویژه در دوران تنش‌ها و محدودیت‌ها جهش پیدا کرده و ترمینال‌های فعال‌شده همچنان آنلاین و در حال سرویس‌دهی باقی مانده‌اند.
🔹
سهم ۵G نزدیک به صفر:
در شرایطی که میانگین جهانی مصرف دیتا روی نسل پنجم به ۵۰ درصد رسیده، سهم ترافیک 5G در ایران تقریباً روی عدد صفر قفل شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/3010" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3009">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExmVJE0kGIfeOuf7E-0mmtrMT-vyKm8fY71LN25YJXIeQa5wZl8cQdc5eUO1uHcHfqO1YJctLGh8SA0DkdpmDltSZN1Hl_sB9EHySWkEjeJEemfqsROMA3CFL4RmwrDoCuLRAvLQRRwr1fVBvORd8S3YYFqnkP8olgjlPEUxfT3bT2V_sUYAok-5JTEf0KjcNRCqDSfYYKkkGyQIoznksjLVwEWw7j2gEQx0RK0at77D-oAdrppAjZN8NkY7m4ADQeQslozRvZoSLH_4iQrivgbN5s8AkCpO0Ia1t_wOOOzzMz3opP-2nRuV7CeOp4ljoc932O-s0CG5qznk3mMlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رفع محدودیت‌های ترافیک IPv6 در کشور
بهزاد اکبری، مدیرعامل شرکت ارتباطات زیرساخت، پس از تذکر اخیر وزیر ارتباطات اعلام کرد که محدودیت‌های اعمال‌شده روی پروتکل
IPv6
برداشته شده و اپراتورها از امروز هیچ منعی برای استفاده از آن ندارند.
⚙️
جزئیات و نکات کلیدی خبر:
🔹
۹ ماه مسدودسازی بی‌دلیل:
ترافیک IPv6 که نقش مستقیمی در کاهش تاخیر (Latency)، پایداری شبکه و افزایش سرعت ارتباطات دارد، از دی‌ماه ۱۴۰۴ تا امروز دچار مسدودسازی و اختلال گسترده بود؛ محدودیتی که حتی خود وزارت ارتباطات هم مدعی است مصوبه قانونی مشخصی برای آن وجود نداشته است!
🔸
وضعیت ترافیک در کلودفلر رادار:
با وجود اعلام رسمی شرکت زیرساخت، داده‌های لحظه‌ای
Cloudflare Radar
هنوز تغییر محسوسی نشان نمی‌دهد و سهم ترافیک IPv6 ایران همچنان روی رقم ناچیز ۷ الی ۸ درصد ثابت مانده است. انتظار می‌رود در روزهای آینده با بازگشایی شبکه اپراتورها این سهم افزایش یابد.//شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3009" target="_blank">📅 14:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3007">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8K4dg8uZQ4vQuaA1lWI2rO-_jZDuYSC2_krGouGEH3pLVI916QDWvrir9uxcQcI-XP37wndajA1i-GwW3TVq-Y3AvnBhfUpzIHQ0Gs3GBH7ADObzhklZZEdlB9B1xWz_Fqyv8vtVXqePn5A-OLRepqzOmPm_e9I6OtFq6lWcGiwwN3yiJOQ1kGmujh_O2HXd0Ean21CRa6pUVClj7tv1QtKBGhj02VjhB1ioJ9C16izGrY9yzbqy4EoSkk0vo2IaLgPsEGvexZfURIMUMM0rXKHFFr505v2QUBwR_XgaOFBKJdqURpekhWKAx5fSz8f8xTH5eb5cxWpfbyr9fcwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت تحریم‌شکن شخصی + پنل مدیریت و فروش «مشابه شکن»
🔹
تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم چطور یک سرویس رفع تحریم اختصاصی (شبیه به سایت معروف شکن) بسازید و با استفاده از یک پنل مدیریت حرفه‌ای، کاربران رو کنترل کنید، اکانت بسازید و به راحتی فروش داشته باشید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#شکن
#dns
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/3007" target="_blank">📅 18:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3006">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">شنیدم خیلی‌هاتون دنبال ساخت یک سرویس تحریم‌شکن اختصاصی (شبیه «شکن» یا «الکترو») هستید که حتی بشه ازش درآمدزایی کرد و اکانت فروخت؟
😎
یه تحریم‌شکن که گیمرها بتونن با پینگ خوب و بدون دردسر تحریم بازی‌ها رو دور بزنن! درسته؟ :)
منتظر ویدیو باشید!</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/3006" target="_blank">📅 16:02 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3004">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">💬
راهنمای خرید سرور از هاستینگ هایی که معرفی میشه
رفقا سلام.
بعد از
هم‌فکری با شما
و بررسی نظرات خریدارها و فروشنده‌های عزیز، به یه جمع‌بندی نهایی رسیدیم. برای اینکه هیچ سوءتفاهمی پیش نیاد و همه چی کاملاً شفاف باشه، رعایت این موارد میتونه بسیار مفید باشه. این موارد قانون نیستن بلکه یک راهنما هستن برای اینکه شما با آگاهی کامل بتونید خرید کنید.
🔹
۱. ملاک قطعی سلامت آی‌پی:
تنها معیار سالم بودن سرور در زمان تحویل، موفق بودن تست پینگ و
باز بودن پورت SSH
از طریق سایت
Check Host
هستش، نه تست بین ده‌ها اپراتور کشور که هر کدوم فیلترینگ داخلی و محدودیت‌های خودشون رو دارن.
🔸
۲. داستان اپراتورها و فیلترینگ:
اگه سرور تو چک هاست اوکیه ولی روی نت شما (مثلاً ایرانسل) جواب نمیده یا بعد از چند روز آی‌پی مسدود میشه، این موضوع به خاطر فایروال‌ها هستش، نه خرابی سرورِ فروشنده.
🔹
۳. تعویض آی‌پی:
وقتی سرور با Check Host سالم تحویل داده شد، در صورت فیلتر شدن آی‌پی بعد از تحویلِ موفق (بعد از چند ساعت تا چند روز)، فروشنده تعهدی برای تعویض رایگان نداره و این ریسک در شرایط فعلی اینترنت پای خریداره.
🔸
۴. ارتباط سرور ایران به خارج:
سرورهای ایرانی که تهیه می‌کنید، باید ارتباط باز و بدون محدودیت با خارج (ترافیک بین‌الملل) داشته باشن.
🔹
۵. وضعیت پهنای باند و ترافیک:
فروشنده موظفه کاملاً شفاف بهتون اعلام کنه که پهنای باند سرور
«اختصاصی»
هستش یا
«اشتراکی»
. همچنین سقف دقیق مصرف منصفانه برای سرویس‌های اصطلاحاً "نامحدود" باید مشخص باشه.
🔸
۶. مرز پشتیبانی:
وظیفه هاستینگ تحویل سرور خامِ سالم با شبکه متصل هستش. نصب پنل، کانفیگ، ران کردن اسکریپت و رفع خطاهای نرم‌افزاری سمت سرور، به عهده خودتونه.
🟢
و اما یه نکته دوستانه و مهم:
— بچه‌ها، ما تو این کانال همیشه فیلترهای سخت‌گیرانه‌ای داشتیم و
فقط هاستینگ‌هایی رو معرفی می‌کنیم که دارای نماد اعتماد (اینماد) و سابقه مشخص هستن
. هدف ما ایجاد یه پل ارتباطی امن برای شماست. با این حال، وظیفه ما صرفاً «معرفی» هستش و صفر تا صد توافقات خرید و پشتیبانی، بین شما و فروشنده انجام میشه.
—
یادتون باشه هر هاستینگی ممکنه قوانین و شرایط فروش اختصاصی خودش رو داشته باشه که لزوماً صد در صد با موارد کلیِ بالا هم‌راستا نباشه.
پس حتماً قبل از نهایی کردن خرید، قوانین خود اون سایت رو مطالعه کنید و با آگاهی کامل خریدتون رو انجام بدید.
— چنانچه خدای نکرده مشکلی هم پیش اومد که نتونستید با فروشنده به توافق برسید، می‌تونید از طریق همون نماد اعتماد به صورت رسمی و قانونی شکایتتون رو ثبت و پیگیری کنید. این مسائل از دست و مسئولیت کانال ما خارجه.
🔻
امکان آپدیت در روزهای آینده وجود داره!
دمتون گرم که با آگاهی کامل خرید می‌کنید!
🌹</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/3004" target="_blank">📅 20:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3003">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3rjv1C8VBRCmpOaPJXHA3gZ7XtuqdL3fC8x5ihLiFzzF_lG4FAb1qjPGPQbfJGkjlkuQOo0Ai_9JunXISTcLbdl5Pew4ip7h240s8-jzFvZEEC0m93wVw13pKe8481Jg3Hk_HL45OYURhGQBG9P_Iz79KaLO_UjYnFAQldcYTPSq_aYZEKXmMrlpkjf17BmshI5GxzjHKtV_-8vsBjx566tGd5bGA8Ln8VpwRozbJOiXfwkJi7DXVXyEf_lGarYn5uiJjdJwDtGTtbF1pQMi4x_UG6ivuJeQpDAS1vpNABB3YeB9zv3lKv_sLk_yzBQ4NTHiJaeGPXJI1tbmFMPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دستور وزیر ارتباطات برای بررسی و رفع محدودیت‌های پروتکل IPv6
ستار هاشمی، وزیر ارتباطات، در جلسه شورای راهبری شبکه ملی اطلاعات خواستار تعیین تکلیف سریع و رفع محدودیت‌های اعمال‌شده روی پروتکل
IPv6
شد.
🔹
نبود توجیه قانونی برای محدودیت IPv6:
وزیر ارتباطات تأکید کرد اگر مصوبه قانونی برای محدودیت پروتکل IPv6 وجود ندارد، اعمال محدودیت فنی روی آن هیچ دلیلی ندارد و موضوع باید فوراً رفع شود.
🔸
همگام‌سازی شبکه با استانداردهای جهانی:
هاشمی اعلام کرد شبکه ملی نباید در تقابل با فناوری‌های روز دنیا باشد و مهاجرت به استانداردهای بین‌المللی مثل IPv6 از الزامات توسعه زیرساخت است.
🔹
پایان نگاه دستوری به فناوری:
وی با اشاره به شکست پروژه‌های دستوری مثل جستجوگرهای بومی، تأکید کرد فناوری با دستور پیش نمی‌رود و سامانه‌ها باید توجیه اقتصادی و رقابتی داشته باشند.
پ.ن: سال‌هاست به بهانه اختلال در سیستم‌های فیلترینگ و رصد ترافیک، پیاده‌سازی کامل IPv6 رو توی کشور معطل نگه داشتن و شبکه رو از استانداردهای جهانی عقب انداختن!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/3003" target="_blank">📅 18:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3002">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQCYeOGgs5sFC7aUzl5WrtzKoIt0piS9Kgd-m4uw8j9gsGVrd7R2AJc2CKaejHEyXKqEQDqzo50bNsKoqTU_Q5IsXX2v1XJXdMF_J1fSl7CxqbeUh_RyyuFsWupeXCl8UwhbyXYVHS0iWvrd0EVTlsEIOwv9zVmaBfyOWBdXIB_kKGEWC99leMitkjvxMuXH20qJjVL0bIHuKkWuWhY3uH9fjVQKnRMcOM5lE29V14At0czdsyJS_RFFfAfY_4KfGYMtG9R4zHTHDI1PB5FZHGFb0wTGHmD3ZazMg3ZdvDSp9BaBw3vpg_ELqAtfqIGp1C0Z-NTqBRINCIBPxl0FIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی اوپن‌ای‌آی از ChatGPT Sites؛ طراحی و انتشار وب‌سایت تنها با پرامپت متنی
شرکت OpenAI قابلیت جدید
ChatGPT Sites
را به‌صورت بتای عمومی عرضه کرد؛ ابزاری که امکان تولید، ویرایش و میزبانی مستقیم وب‌سایت‌ها و وب‌اپلیکیشن‌های سبک را صرفاً بر اساس توضیحات متنی زبان طبیعی فراهم می‌کند.
💬
طراحی پرامپت‌محور (Sites@):
ساخت رابط‌های کاربری چندصفحه‌ای، داشبوردها، پورتال‌های درون‌سازمانی و ابزارهای تعاملی با ارسال متن، فایل‌ها و دیتاست‌ها
🚀
میزبانی و هاستینگ رایگان:
میزبانی خودکار وب‌سایت روی زیرساخت OpenAI، تولید لینک اختصاصی با قابلیت تعیین سطح دسترسی (خصوصی، سازمانی یا عمومی بدون نیاز به لاگین)
🧩
المان‌های تعاملی و شبه‌وب‌اپ:
پیاده‌سازی فرم‌ها، فیلترها، سیستم جست‌وجو، جداول داینامیک، نمودارها و سیستم احراز هویت اولیه
👥
همکاری تیمی (Collaboration):
امکان کار اشتراکی روی پروژه، اعمال تغییرات و به‌روزرسانی نسخه‌های منتشرشده با اعضای فضای کاری
📊
دسترسی:
دسترسی برای اکانت‌های Business، Enterprise، Pro، Pro Lite و Edu فعال شده و عرضه تدریجی آن برای کاربران پلن Plus نیز آغاز شده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/3002" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-3000">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9tSpzitmRyVKvIzn6Li13gTP5GYW0esgf3IL3t8KG5vN4-va1ozmw6Mfj9D9HsM0BKhR0PBZXqPA43Ra4Utv7u9TYwhU0r91DoSLLeJzyjGzYH0_NQWAN01gFQdBBmrsF3waCYFkaqCkH6Dic3G726utDHdeM3PIfpRWoFm2DN1nnwWIs9vkOCylJwcXT_2HTu4H3E_AAgtslck4emAB2diKlhGhKYv4ah767hKwPF3KwBjTf7_ZGravZTrdeyl8xmDSuzOsKWbcZ3qmJhg9hlR1Kdql7TkhmqVCDYC3dJhvayZNnNay71h5DrfcA5c1SbGMzqGiGDfrfZtiYerFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📦
بکاپ خودکار از پنل‌های V2Ray و تحویل مستقیم در تلگرام با ابزار bkup
ابزار
bkup
یک سرویس سبک برای سرور است که در فواصل زمانی مشخص از دیتابیس پنل‌ها فول‌بکاپ می‌گیرد و فایل خروجی را مستقیماً به تلگرام می‌فرستد.
🔄
پشتیبانی از ۴ پنل:
اتصال به پنل‌های 3x-ui، HM Panel، PasarGuard و Rebecca با دکمه تست آنلاین اتصال.
📤
تحویل خودکار در تلگرام:
ارسال مستقیم فایل بکاپ به چت یا کانال بدون نیاز به دانلود دستی از سرور.
⏱️
زمان‌بندی دقیق:
تعیین فاصله بکاپ‌گیری بر حسب ثانیه، اجرا در قالب سرویس Systemd و فعال ماندن پس از ری‌بوت سرور.
🧩
ابزار Reassemble:
قابلیت چسباندن پارت‌های چندتکه بکاپ‌های حجیم ارسالی تلگرام در پنل وب و ساخت فایل کامل
💻
مدیریت وب و ترمینال:
دارای داشبورد گرافیکی با لاگ زنده، به‌همراه منوی ترمینالی برای آپدیت، حذف و تغییر پورت یا پسورد.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
صفحه پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/3000" target="_blank">📅 20:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2999">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=GGD0rYmg7QBqBEk0-VxXRERd3foFEDF6F736VZVwve6PLFAKyGjKxNZeksOPsLwJ522RDEWkbwbUNuf3EY5y-17S4_mfgAxfC5w-s-ugueEP3hp59t7i3VGtqpTPWH8fqzsf4Tp4WrixTpLSnAASHy5x1Aup9G3doaeZVyPa-WSoiFYAOIgWRuqKjWg5HiGN_hFxbeYspwbfplsa0MItQ7ZTt7ctdi0bFrBBKtop5fBXP1g_s_C2OeXQL0S7Nodbzv11e5CvnGujdBgazO8Ga_sR6lgLVbUK5O9RL1XIYmhaPYqZdMrLFzjEcCVMQXeH60zGq6fFJatSIsY56LF-7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5cd795a1.mp4?token=GGD0rYmg7QBqBEk0-VxXRERd3foFEDF6F736VZVwve6PLFAKyGjKxNZeksOPsLwJ522RDEWkbwbUNuf3EY5y-17S4_mfgAxfC5w-s-ugueEP3hp59t7i3VGtqpTPWH8fqzsf4Tp4WrixTpLSnAASHy5x1Aup9G3doaeZVyPa-WSoiFYAOIgWRuqKjWg5HiGN_hFxbeYspwbfplsa0MItQ7ZTt7ctdi0bFrBBKtop5fBXP1g_s_C2OeXQL0S7Nodbzv11e5CvnGujdBgazO8Ga_sR6lgLVbUK5O9RL1XIYmhaPYqZdMrLFzjEcCVMQXeH60zGq6fFJatSIsY56LF-7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی اوپن‌ای‌آی از ChatGPT Images 2.5؛ تبدیل اسکچ ساده به تصاویر واقع‌گرایانه
اوپن‌ای‌آی نسخه جدید مدل تولید تصویر خود را با نام
Images 2.5
معرفی کرد؛ مدلی با نورپردازی طبیعی‌تر، بافت‌های غنی‌تر و بهبود چشمگیر در وفاداری به تصاویر مرجع و ویرایش‌های متوالی.
⚙️
امکانات و ویژگی‌های جدید:
✏️
قابلیت Sketch@:
امکان رسم طرح اولیه و نقاشی ساده داخل محیط چت برای تبدیل مستقیم آن به تصویر پرجزئیات نهایی
⚡️
کاهش ۵۰ درصدی تاخیر:
سرعت تولید و بازبینی تصاویر دو برابر سریع‌تر از نسخه Images 2.0
🎯
ویرایش موضعی پایدار:
تغییر دقیق بخش‌های مدنظر (مانند متن تبلیغاتی، پس‌زمینه یا سوژه) بدون دست‌خوردن هویت اصلی یا افت کیفیت در مراحل بعدی
📁
قالب‌های آماده (Templates):
تسهیل ساخت پوسترهای تبلیغاتی، تراکت‌ها و عکس‌های صنعتی محصول
این مدل برای تمام کاربران در وب، موبایل و دسکتاپ فعال شده است. برای توسعه‌دهندگان نیز در دو نسخه ارائه می‌شود:
Flare
(پیش‌فرض، سریع و کم‌تاخیر) و
Sunburst
(مخصوص خروجی‌های بسیار دقیق و سنگین).//دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2999" target="_blank">📅 18:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2998">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Nso261CMZ_CmxiunpIEhnMHx4m3B7NldONzm0aAXWIHgUBlvv62tGC1m8rkv0aznjPIb0vVtzuT7b_cvpxB0koL05bz9ADwp_SUtptcPAYri4ojy9R7At660mMf_gyqhzLI_YvvNVYWVaf3nGCPCbEAnqihm9u2ycRH97aunOsE83WRoFMTIKM82AMT9v-2pP54ARe0PGUZD85QJabej0zfQBJB3osUkWhFWgTySzlFZN7YXGJoF0GzIHN-B2H7SWrFk4U0S_4HMAmbRGhH36X7KpIR1OwzDphFWJIJgud3lYGNFAOSEPWkFGsYWFpD8SRlAI8DcV63enASbuQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
راهنمای نقشه ذهنی کلیدهای میانبر کامپیوتر با کلید کنترل
🔸
این تصویر یک نقشه ذهنی از کلیدهای میانبر عمومی کامپیوتر است که هسته اصلی آن، کلید کنترل (Ctrl)، قرار گرفته.
🔹
هر شاخه شامل لیست‌های دقیق از کلیدهای ترکیبی و عملکردهای مربوطه است که به راحتی قابل درک و یادگیری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2998" target="_blank">📅 16:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2996">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.  گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/iaghapour/2996" target="_blank">📅 20:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2995">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=QcA4CL3h7I7pr3Ze2DodkQ8oyMnZX0VqxmtApeFwqh081ft4v0jezXbxNCx9q4gDdICPtrb9xPBFj8HsJfNzwRPV2fu3DccOeYVYo7nyD4oZsywogVyxYSIdMZT4eLK4leFjGMi4R0WxQ1XJr4ow3d42Y9Ab0axWPQlK1ToGt1i0-AK3HuZd22E3gCLgE7yWmJ609ljVNu9n0uhqG2vb4FAfgihXDLhIcPpawKIjYe0eMHDJPwrOymABUX8N6mYC6GKi7ivaRiB9UflKDEJrBt7uouwwy2tcwEc-gmSWV00R94Hqd1wtYYH1gVgei9kpACedtGNo6G48XDvdg6Qo2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a805e4a96a.mp4?token=QcA4CL3h7I7pr3Ze2DodkQ8oyMnZX0VqxmtApeFwqh081ft4v0jezXbxNCx9q4gDdICPtrb9xPBFj8HsJfNzwRPV2fu3DccOeYVYo7nyD4oZsywogVyxYSIdMZT4eLK4leFjGMi4R0WxQ1XJr4ow3d42Y9Ab0axWPQlK1ToGt1i0-AK3HuZd22E3gCLgE7yWmJ609ljVNu9n0uhqG2vb4FAfgihXDLhIcPpawKIjYe0eMHDJPwrOymABUX8N6mYC6GKi7ivaRiB9UflKDEJrBt7uouwwy2tcwEc-gmSWV00R94Hqd1wtYYH1gVgei9kpACedtGNo6G48XDvdg6Qo2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره دهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی mmdoo-yt، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2995" target="_blank">📅 18:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2994">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0KumWUTnAjAySnbif_GZWvgwoZAXmbmK9SS9PbOPzgdwLawv5J3lIiHXC9Gq__wZotO7xeXUJ2C0OuwoRDZhluSowlSjou7DBPL04ZKPmElZEeQfU8-StWR6xUF0AxEfPFG31sD0UljqHmqfvmfQhLBIXRAW8lfnCDaZS32Ch06nVkXB4whpVdcm8jJ7bic0-n0ppSL-RwZMpu8lNgqzwKdR3MHgx0nS2rxZw6sppPrCDL7r4yff9ctMPmRYvZfhATCnrWC4zHw5aSifhGs62liXKYjL_BI8hU_z1H5xts_-ividqMKiw6uUvcjRoYqUW90yl9N0dft7gywszjoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نسخه 0.12 مسنجر سانگبرد منتشر شد
🔹
با این اسکریپت میتونید در سرور خودتون یک مسنجر بالا بیارید و با دوستان خودتون چت کنید.
👇🏻
تغییرات کلیدی سانگبرد (Songbird)
:
🐘
پشتیبانی از دیتابیس PostgreSQL
🪣
ذخیره‌سازی ابری روی آبجکت استوریج‌های سازگار با S3
📥
پشتیبانی کامل از استقرار به صورت PaaS یا CaaS (
دیپلوی آسان در Railway و Render
)
🎬
ورکر مستقل مدیا برای پردازش و تبدیل ویدیوها
📴
کارکرد چت در حالت آفلاین (صف‌بندی پیام‌ها و ارسال مجدد خودکار)
🛡
دسترسی اضطراری به پنل مدیریت
👥
عضویت خودکار کاربران جدید در چت‌های عمومی
📦
قابلیت Rollback (بازگشت به نسخه قبل) در اسکریپت نصب
👇🏻
بهبودها و رفع باگ‌ها:
🔸
استفاده از شناسه UUID برای کاربران، چت‌ها و پیام‌ها
🎨
بازطراحی رابط فهرست چت‌ها با تایپوگرافی بزرگ‌تر و ظاهر مدرن
🔧
ارتقای امنیت با رمزنگاری اختصاصی تامبنیل‌ها و فایل‌ها
🚪
رفع پرتاب کاربر به صفحه ورود در صورت قطعی موقت سرور یا اینترنت
🔗
داکیومنت پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2994" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2991">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i3krzO_SrI4rAS_dOJ8igukoSjUoptfRDyiGcPimELmp9ZwoujW0L-RXOJCMxlruFadv-s_pQC9kQm8qVrH7VeFjcngV6WDHFeJjqmqnpk3wRICCnxy3IinI4OVkcCvHoF8uhi1GUtg8_7TDyTEIbeuO6i68L_tOWv5Ya-5OmywIjjPX3w43RHI5H7yLzDXA9PKeGHbFOG5Ri5naOgIp8JukhG2QNctHU8PpM2w7F_7_icBq0osJTG5-CV5WotZ-CQa4rm9_Li37I5hF_nB2jk0LQc6lkQmmmqHH8Fq23YrnBbkVJ-n1gLuqecm4SD1zd7ZgxVQ_T4RKiVWtTTlJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKruaLIpZpzJA1_ohia_UXAShZ2q2RdbvGByKqjlZIA34r2yCnf6L5Ufkwnb2Uvtr-SRNmF6FUEIM_iTti6AW7SIgJYtMMepaJ19D26SVKy_I-Mh6JmjgXQXi3N2-Q5BADzkEBKU1aYBgs6SpAuaDqjv_FhvM3dYrFyoaFW8E-18APz8-CU4_HAVUC8B3-3tZPx7ZwVqd7gGc2VM2NVvJjWbYydxWhTY8eBx_M0Ko4YuzExm-pJ6AkjOlKmHDsA7900_jsK0nVEglOWluw0jAsVYA04n-uLMLvpulsieLNQ7qDAtwhAPLfmBEOCDkaziluDk16tKTz4TppSgs-gsaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jSR5ya1ez4y7QW50foPMoJYyyQOvZTogqv8hnTBgSwcPB_PPeFbEum38qG-OswrzWnMtNHw00no719GNYqFChnFBRxYK4xcmkxc1w-0ly6KOHZUfrkpRRN79DFwZRipGvt-SkCPdBBQx7qMnbRqnDll-gqkJpkGhtIQbyv59wtb7p_ocjC_s-FfblswWVbaoYGkxQKsljANoWorxnMQd52XGb-niK1UPSNFzPXvefr-U5V3NkYitBq9w6fKtlNOSkTlIy6FoU7vV_F-ZBCTzKKGA3Xnu_CemvyWrGVSwkWCnKNUGQCIKbQ1n1RcJ3R0grzlYz03CtKRzCiOoyX6hHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
رکوردشکنی تاریخی قیمت آیفون در ایران؟!
اپل رسماً قیمت گوشی تاشوی جدید خود یعنی
iPhone Duo
را در نسخه پایه (۲۵۶ گیگابایت)
۱٬۹۹۹ دلار
و در بالاترین کانفیگ تا
۲٬۹۹۹ دلار
اعلام کرد؛ رقمی که با ورود به بازار ایران احتمالاً به برچسب نجومی
یک میلیارد تومان
خواهد رسید!
⚙️
چرا پیش‌بینی قیمت ۱ میلیارد تومانی برای آیفون دوئو دور از ذهن نیست؟
🔹
مقایسه با قیمت آیفون ۱۷ پرو مکس:
نسخه پایه ۲۵۶ گیگابایتی آیفون ۱۷ پرو مکس با قیمت دلاری ۱٬۱۹۹ دلار، در بازار ایران به صورت رجیسترشده در محدوده
۴۴۰ تا ۴۵۰ میلیون تومان
معامله می‌شود. بنابراین پایه دلاری ۲ هزار دلاری Duo با احتساب هزینه‌های رجیستری، سود واردکننده و حباب هیجانی روزهای نخست، به سادگی مرز ۱ میلیارد تومان را رد می‌کند.
🔹
چالش بزرگ eSIM در ایران:
اپل در آیفون دوئو درگاه سیم‌کارت فیزیکی را به‌طور کامل حذف کرده و فقط از
eSIM
پشتیبانی می‌کند؛ با توجه به عدم فراگیری و محدودیت‌های گسترده فعال‌سازی eSIM در اپراتورهای داخلی، استفاده از این دستگاه در ایران با دردسرهای فنی جدی همراه خواهد بود.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2991" target="_blank">📅 17:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2988">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4oJ5w6sURCBgmAWDx7NEjEDKvdzOSpraK5uoPUSFZcjM0yk6yWMcj_NARJo5HJM2ivc1XBD6C-uWjd-sgDRDluiPAABGtSdUrbJYP40kjKCd1skSoGL0mkKESsr-7BDemZkLI0PJtChZizGqegrJKjT1nbztuOn9BzYMB5ptzYfvi3cvb0XCiTgrByNiyLhfDb0YeHNfB-BFYXnkShltFysqSOVnfCpQ4GiGy41eVnYlpcIf8YHgfo0K31v_VVnI7mif1vsb6aONCxoSO_lIRd6v-3bHc887txDNH9jjY88j6wEZFLANS1B-5r9mpjbvOJKdX-YmKn3yrIAoX8ubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بازم داستان تکراری؛ اینترنت داغون، اما ادعاها برقرار!
🔹
از دیروز وضعیت اینترنت رسماً افتضاح شده؛ پکت‌لاس شدید، کندی اعصاب‌خردکن و قطعی‌های مداوم. بهزاد اکبری (مدیرعامل زیرساخت) هم طبق معمول اومده توییت زده که علت کندی «قطعی فیبر نوری در ارمنستان» بوده!
🔹
الانم ادعا می‌کنن مشکل حل شده، ولی در عمل کیفیت شبکه—مخصوصاً روی اینترنت موبایل—هنوزم افتضاحه و هیچ تغییری حس نمی‌شه.
✍🏻
جالبه که با یه قطعی سیم توی کشور همسایه کل اینترنت مملکت فلج می‌شه، ولی موقع افزایش قیمت بسته‌ها همه‌چیز سر جاشه و وزرا توی صف اول توجیه گرونی می‌ایستن! اول یه اینترنت پایدار و بدون قطعی تحویل بدید، بعد دم از گرون کردن تعرفه‌ها بزنید.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/iaghapour/2988" target="_blank">📅 20:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2987">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF8Ttf3Bju1RqYKOmqtPN9YL3ha7JwkFwj0QlA7pduFK0wY67rmpN2B34_PapwUne_8UdTlf6x0CSb361-fjAddWavvXvaHuV0OcZSvKfe4Z8FvLlYtspS3g1itoPmVdkImpDjUee8ERsAii5J53EsnRTxGEgOdDKsfhFR3Qc0Yv1MaSK3m_jBhupAYchA-3r-x_j0ZPk0n9wa29U1PIMtMgyKlTRclrz9ark_SeqRkUIpP-seeg0sdvOKVHodgKqaeZNcGHWSxlcpvqUuifwN1SEy2y7OfJ6hncdTFKt9cdzSBYeWMpj-JguI6hqFvXeRGrx8Hy2dQqfJ5mMf63rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زنگ خطر امنیتی؛ لو رفتن دیتابیس حساس کاربران JumpJumpVPN
🔻
دیتابیسی که ادعا میشه مربوط به کاربران فیلترشکن JumpJump هست، توی یکی از فروم‌های دارک‌وب منتشر شده. منتشرکننده با شناسه leakhunter ادعا کرده این مجموعه فقط شامل اطلاعات معمول کاربران نیست و اطلاعات شخصی و نسبتاً حساسی مثل اطلاعات پرداخت، اطلاعات کارت‌های بانکی، تراکنش‌ها، موجودی، لاگ فعالیت کاربران و اطلاعات دستگاه‌ها رو هم شامل میشه.
البته فعلاً نمی‌شه صرفاً بر اساس ادعای منتشرکننده با اطمینان گفت تمام این اطلاعات واقعاً متعلق به کاربران JumpJump بوده یا اینکه کل دیتابیس ادعاشده صحت داره، اما درصورت صحت‌سنجی، همین اطلاعات نشون میده جامپ‌جامپ ظاهراً اطلاعات شخصی و جزئیات مختلفی از کاربرانش رو نگهداری می‌کرده، که این نشت می‌تونه برای کاربران دردسرساز بشه.
اگi از این فیلترشکن استفاده می‌کنید یا قبلاً استفاده کردید، بهتره موضوع رو جدی بگیرید و حواستون به امنیت اطلاعات خودتون و افرادی که باهاشون در ارتباطین باشه.
©
hamedvpns || ircfspace
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/iaghapour/2987" target="_blank">📅 19:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2986">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9tW5JSrIQityLcEjVD5YhLFjOGLPcKQ9ZiQRNi6XhCU2aV8szJNryyuF2Cgf3DPDS9Vo0W2Pf-LLUJuQhNPnT2AxW9SgmZLPKS59Sq5p4Au9cH3b3DPZA_LRRw82DodBhykCNRkRLpPHd_vDlBBPH0JmcmhQy-Tk7387eqM4yNetubNirzbgnTU3fm_tcsJl9qheM-L34mFZWd1ELs1glNRmvK29Ob7LRbi_fb7YpT7g5OtylENNKKmyvvp3igfABcEWendmcjYVgp306e4wEwzvPYkmf4LL9VP4OPkuSM_zufOziERbbKJgvPiUcxva7NQGY4ktxEOCTxP_V0wBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بروزرسانی جدید برای نسخه اندروید oblivion منتشر شد
🔹
فیلترشکن رایگان
oblivion
به صورت اوپن سورس و امن برای اندروید توسعه داده میشه و میتونید ازش استفاده کنید.
🔸
هسته برنامه از وارپ‌پلاس به Aether سوییچ کرده، تا امکان اتصال و دورزدن فیلترینگ از طریق متدهای وارپ، گول، مسک و سایفون فراهم بشه.
🔗
دانلود از گیت هاب
#فیلترشکن
#oblivion
#رایگان
برای دور زدن فیلترینگ و آموزش کامپیوتر و تکنولوژی و... ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/iaghapour/2986" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2984">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">SoftEther Code -- @iAghapour.txt</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/iaghapour/2984" target="_blank">📅 23:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2983">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">SoftEther Code -- @iAghapour.txt</div>
  <div class="tg-doc-extra">3 KB</div>
</div>
<a href="https://t.me/iaghapour/2983" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🟢
لیست
دستورات برای ویدیو
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2983" target="_blank">📅 19:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2982">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_jxXVqvRd-XADOvNQmHjejDFlN7Ffid67fJDw0-gQBkDrannzt6eOVldB2JttJctD_AkCj70bJZHQRpWCovZW1996l9dUtrHIHHPzzDr7PeiKidoVlWr1pXe8Orb0rpFNPHqKj-hfzC5JbFJX_ILTdXeKa9MZzURImZR1fhRA-pi6fRkdFkhPt5Rsvz3UmQ-y8uecuHrXx5aRdOaTVJ7ax2cDwcOcI-jbJwCbUEeq6s4OgRVRLPLOcmHHm0Ojwvg2X72LaZLfvd3JTl3UUlXkcedh_N2UE1uzYx5bhP4d9ePSRue0ajwGGpyrS-jCIvjubmJdB_Rc-Vi1t_Y8EQ9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
قوی‌ترین فیلترشکن خودت رو بساز (سافت‌اتر + پنل وب + تانل)
🚀
🔹
توی این ویدیو قدم‌به‌قدم بهتون یاد می‌دم چطور سرور SoftEther رو به همراه یک پنل تحت وب اختصاصی راه‌اندازی کنید. این پنل قابلیت‌های زیادی مثل مدیریت کاربران، اعمال محدودیت حجم و امکان استفاده از پروتکل‌های مختلف رو در اختیارتون قرار میده.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#سافت_اتر
#openvpn
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2982" target="_blank">📅 19:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2981">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭕️
دفاع وزیر ارتباطات از گرانی اینترنت: کمتر از بقیه کالاها گرون کردیم!
ستار هاشمی، وزیر ارتباطات، در صحن علنی مجلس در پاسخ به سوال نمایندگان درباره گرانی شدید بسته‌های اینترنتی، از افزایش تعرفه‌ها دفاع کرد و آن را با سایر کالاها مقایسه کرد؛ پاسخی که در نهایت نمایندگان را قانع نکرد و منجر به کارت زرد مجلس شد.
⚙️
محورهای صحبت وزیر و استدلال‌های گرانی:
🔹
مقایسه با تورم سایر کالاها:
وزیر ارتباطات مدعی شد طی ۵ سال گذشته، با وجود جهش ۲۰۰ تا ۵۰۰ درصدی قیمت اکثر کالاها و خدمات، رشد تعرفه‌های ارتباطی کمتر از ۸۰ درصد بوده و در نتیجه گرانی روزافزون اینترنت مطابق واقعیت نیست!
🔹
عوامل توجیهی افزایش قیمت:
افزایش هزینه‌های ارزی، مصرف برق و انرژی، هزینه‌های نیروی انسانی و نگهداری زیرساخت‌ها به عنوان دلایل اصلی افزایش تعرفه‌ها عنوان شد.
🔹
کارت زرد مجلس:
پاسخ‌های وزیر درباره گرانی بسته‌ها و عدم توسعه فیبر نوری نتوانست نمایندگان را قانع کند و به او کارت زرد دادند.//شبکه‌چی
پ.ن: می‌گن «چون بقیه چیزا ۵۰۰ درصد گرون شده، اینترنت رو ۸۰ درصد گرون کردیم.
جالبه که هیچ‌وقت کیفیت خدمات رو مقایسه نمی‌کنن، ولی برای افزایش قیمت سریع دست به دامن مقایسه با تخم‌مرغ و گوشت می‌شن. کاربر الان نه‌تنها بابت همین اینترنت محدود و کند پول گرون‌تری می‌ده، بلکه مجبوره‌ ماهانه به اندازه همون بسته (شاید هم بیشتر) پول فیلترشکن و سرور بده تا فقط بتونه به اینترنت آزاد دسترسی داشته باشه؛ این هزینه‌های تحمیلی رو چرا توی آمارهای ۸۰ درصدی حساب نمی‌کنید؟!
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/iaghapour/2981" target="_blank">📅 17:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2980">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W-e2UQt5ZCOFC0AqMITM6ykFwopND0lcaQ5gPL8yayFuRLPLFKTLS9-bq1_bzMrZNicTHzrZbo-79hbRsQeqZfT9U1IBjkZgnxdpIA3K1dkpS4O0o1wmISMvE6-nOpAnSDucwIkYWUzHn_lbmWvLhbGE0GdW0WYqpZl9m1OZ2naqJgyxfvqs2LNnQ63vj8wUJLKy-Y183yvmx7uao5D1pBa06hyjh1D-6qZaI76Xg0allsp1AOdn-W36IDmKVfFo98qiIEVaxJwSLyuqgMGjdLCnDT1apubi1y1xoGYfeFxCk2p90oIrD8CJ5lVaAq9lY5IbShfb13-JTelD1f37nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی EMS IPAM؛ سامانه مدیریت آدرس‌های IP و تجهیزات شبکه
اگر برای مدیریت ساب‌نت‌ها، رادیوهای وایرلس و تجهیزات شعب مختلف هنوز از اکسل استفاده می‌کنید، ابزار
EMS IPAM
یک پنل متمرکز و گرافیکی برای سامان‌دهی و مستندسازی شبکه است.
🔹
مدیریت ساختاریافته IP:
پشتیبانی از رنج‌های /16 تا /32، جلوگیری خودکار از تداخل ساب‌نت‌ها و نمایش ظرفیت آزاد/مصرف‌شده.
🔸
مستندسازی شعب و تجهیزات:
ثبت موقعیت شعب، پورت‌ها، توپولوژی و ذخیره راه‌های دسترسی سریع (WinBox، SSH، RDP و وب).
🔹
پایش مستقیم میکروتیک:
اتصال به RouterOS از طریق API و نمایش زنده وضعیت اتصال، سیگنال و پهنای‌باند رادیوهای وایرلس.
🔸
کلاینت ویندوز:
باز کردن مستقیم نرم‌افزارهای مدیریتی (مانند WinBox) با یک کلیک از داخل پنل بدون درج رمز در مرورگر.
🔹
تعیین سطوح دسترسی، ایمپورت/اکسپورت ساب‌نت‌ها و پشتیبان‌گیری خودکار.
🔻
این پروژه کاملاً رایگان و اوپن‌سورس است، اما کدهای آن توسط ما به‌طور کامل بررسی امنیتی نشده؛ پیشنهاد می‌کنم قبل از استفاده، سورس‌کدها و اسکریپت نصب را با ابزارهای هوش مصنوعی بررسی کنید و بعد استفاده نمایید.
🔗
پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2980" target="_blank">📅 16:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2978">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U47-NucCcsEbplFhos_OPzEgUlJy9dyKntRSYbL62lUh5hxCmBAJEf7hPp80gFXRqwNtWXMeN8pyB5fDlGDzXaws-aoRh_aPTNlitVjWsxQCnOn_-XgvrzykfBFnYR7QD9WRuyRBVGdsMOjMjQht8k9_7YW7yc_1NznGHXEVglCtBGcWdm8gJSjWieTp0qApfRnwL7Ph-3EnjJaok8LVAgM-mjwgRlJcEA4W_F1aw1ur7P6UI0dwK6gCXp6EK9FgA6tU3iJF_ydGX13GiG7YEzs3jdxNvqFaekIOIzxinfC9ZPO-KTLkXFac3vH6BhgMYt0qxGqqA_X5nS5JpUjpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛡
نرم‌افزارها در پس‌زمینه سیستم شما چه می‌کنند؟ کنترل کامل ترافیک با فایروال متن‌باز Portmaster
اگر زیاد اهل تست و نصب نرم‌افزارهای مختلف هستید یا نگرانید برنامه‌ها دور از چشم شما تله‌متری و اطلاعات به سرورهای ناشناس بفرستند، ابزار
Portmaster
دقیقاً همان لایه محافظتی مورد نیاز شماست.
⚙️
قابلیت‌های کاربردی و مهم:
🔹
دیده‌بانی زنده اتصالات:
نمایش شفاف و لحظه‌ای اینکه هر برنامه دقیقاً با چه IP، سرور، در چه ساعتی و از چه طریقی ارتباط برقرار کرده است.
🔹
مسدودسازی هوشمند ترافیک:
امکان بستن ترافیک‌های مشکوک، ردیاب‌ها (Trackers) یا تبلیغات به‌صورت موقت یا دائمی با یک کلیک.
🔹
ایزوله‌سازی آفلاین:
امکان قطع کامل دسترسی به اینترنت برای یک برنامه خاص تا صرفاً به‌شکل لوکال و آفلاین اجرا شود.
📥
دانلود از وب‌سایت رسمی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/iaghapour/2978" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2977">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTpN7dYSn6ulJe17mUQIOlW4ZlTkp2ojg6ZgB6C9aL4tgDwyvCpZIzLhKc1xqdaw-bflCPO-6nhGjm-hqUD2vuI-C5W4xXifmOsAxpKMnVUV7YPkFusaol2Ppbpe5520qLDEVK98uxoidW1dwy_amKp_SFCxxMRd9XBLLXHdncBQspdRgUaja0050941wEefUTGn0hN7SKMAuLuyo4IPNQFJ2e35nUl6r5uu5tu5Zoz-d1xziokTL5pKAyhGZtkq2oi0otl-qmJTwsi5ceHI0Vn5UZgS14duda_GzoApmXscDgRyfAt0pOzFFVhkUxcuhy5pkvSQiY_s0qc5QcFLkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بحران لغو گواهی‌های SSL در شبکه بانکی ایران
🔸
تحریم مراجع بین‌المللی صدور گواهی امنیتی مانند Let’s Encrypt و Certum علیه زیرساخت‌های ایرانی، سیستم بانکی کشور را وارد یک بحران امنیتی تازه کرده.
🔹
تغییر آدرس به جای حل ریشه‌ای:
برخی بانک‌ها (مانند بانک ملی و بانک ملت) برای دور زدن باطل شدن گواهی SSL، اقدام به تغییر دامنه‌های اصلی خود کرده‌اند؛ حتی در مواردی بدون ریدایرکت خودکار یا اطلاع‌رسانی دقیق، که مستقیماً کاربر را در معرض صفحات جعلی و لینک‌های فیشینگ در گوگل و شبکه‌های اجتماعی قرار می‌دهد.
🔹
عادی‌سازی خطای مرورگر:
مواجهه مداوم کاربران با خطای قرمز «اتصال امن نیست» در سامانه‌های رسمی بانکی، حساسیت عمومی نسبت به هشدارهای امنیتی را از بین می‌برد؛ کاربری که یاد بگیرد این خطا را نادیده بگیرد، طعمه ساده‌ای برای حملات فیشینگ و صفحات جعلی درگاه‌های پرداخت خواهد بود./دیجیاتو
پ.ن: اگه فردا روز دیدید یه «SSL ملی» راه انداختن اصلاً تعجب نکنید! چند وقت دیگه میان به بهانه تحریم و امنیت، همه کسب‌وکارها رو مجبور می‌کنن برای گرفتن درگاه پرداخت و ای‌نماد از همین سرتیفیکیت داخلی استفاده کنن.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2977" target="_blank">📅 17:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2976">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqBwEXl_UmbJW2opp2jE54E0qNmJlCg1ePKVLEQ8oSeWpbbqmrr8e7bmEPNy6L3BMRZZv7UCrE4Lnx2mCrDthFWwasQDS3enyLP8vEuVkrtOrU9wgllJxH29avvhU1WF7z3TqBnudBS66fJDmfR8Lmtdb5TbEkeY1J27i7KR0R-eSnQphif9VMYnrcWOK53_2mbCeOFTWha37FxIjqWr-m3oTGb2r9LIl3mhUzff2hYqrGA3zM1jfNHs_JnZSOTaVRBoTjP5f03tSq7q48etQpATBeoSGvSjJKB_ZX-rm5TffZtltvl_p0VG-ssh6IRduOEu-BW8sGgd3u1br4KP4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
رونمایی از «آیزا»؛ دومین آنتی‌ویروس بومی مبتنی بر شبکه ملی اطلاعات
دومین آنتی‌ویروس بومی کشور با نام
«آیزا» (Ayyza)
رونمایی شد؛ سامانه‌ای امنیتی که با تکیه بر هوش مصنوعی و ساختار شبکه ملی اطلاعات، امکان شناسایی تهدیدات و دریافت آپدیت‌ها را بدون وابستگی دائم به اینترنت بین‌الملل فراهم می‌کند.
🔹
موتور تشخیص هوش مصنوعی و سطح کرنل:
توسعه انجین اختصاصی مبتنی بر یادگیری ماشین و بهره‌گیری از فناوری‌های سطح هسته ویندوز (Kernel-level) جهت پایش دقیق‌تر، واکنش سریع‌تر و بهینه‌سازی مصرف رم و پردازنده.
🔹
عدم وابستگی به اینترنت جهانی:
قابلیت آپدیت به‌صورت آفلاین و انتقال داده‌ها و امضاهای امنیتی از طریق بستر شبکه ملی اطلاعات (اینترانت داخلی).
😁
🔹
اکوسیستم امنیتی یکپارچه:
ترکیب فناوری‌های EDR و XDR برای شناسایی حملات چندگامی و روز صفر، در کنار هماهنگی با سیستم‌های جلوگیری از نشت اطلاعات و مدیریت دسترسی‌های ویژه (PAM).
✍🏻
حواستون باشه قبل نصب با آنتی ویروس معتبر مثل کاسپر اسکن کنید آیزا رو :) تازه با اینترنت داخلی هم کار میکنه :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2976" target="_blank">📅 14:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df60791764.mp4?token=sMdUgoQjMoaa4OWfAcs1_KQNLgLG9kl5Qe8WiGT4t-BW4-OdBuLnzN3fw0K6YlueX6KNHMhmJal5vqqK2l4fmfKCXnsDoyn0jZSDCnt7cxtpiGfq6jiEnqaau2mFal0jMUlGYPRHTfcyXnZWocrFoB_jBdkkST_CzC1PoCkQhtQVDyRTFU6PHVuoHaM-zJf8IpyQViWRM5uWBVzjUXTnUubG4U3rua3C5wR1jfpz_UtJmF-rogxxTDb9gyfGOgKsC_gN6ZRQnlJcalbmj6nrwCSf-oDpgOhoQzRA8Qtz70eoSAzDdjRAoFOpv5ePjbmgoA30aZydWrJu03tT_I_HlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df60791764.mp4?token=sMdUgoQjMoaa4OWfAcs1_KQNLgLG9kl5Qe8WiGT4t-BW4-OdBuLnzN3fw0K6YlueX6KNHMhmJal5vqqK2l4fmfKCXnsDoyn0jZSDCnt7cxtpiGfq6jiEnqaau2mFal0jMUlGYPRHTfcyXnZWocrFoB_jBdkkST_CzC1PoCkQhtQVDyRTFU6PHVuoHaM-zJf8IpyQViWRM5uWBVzjUXTnUubG4U3rua3C5wR1jfpz_UtJmF-rogxxTDb9gyfGOgKsC_gN6ZRQnlJcalbmj6nrwCSf-oDpgOhoQzRA8Qtz70eoSAzDdjRAoFOpv5ePjbmgoA30aZydWrJu03tT_I_HlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره هشتم و نهم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
برنده عزیز با آیدی AhvanSalehi-f3r، مبارکتون باشه!
✨
👤
برنده عزیز با آیدی abolfazlghasemi1-q7t، مبارکتون باشه!
✨
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2974" target="_blank">📅 20:24 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVzuAdMZIwTOF_rLz4yeu0WdiVkkdR1X9nOvN_70BANhJtuwuKzy-sa410qbOwIadVZ5BW2dkfvGQOHJG0PRkxSY8j7-I47Re-NHg1MkV9wP_KB-nQZL0qyibvyA6e5TsMSVSW-Pr9nlE9WUXXYmkzRBFrBgvidDbRFgLqFdQkBbx0-KUSgKP9JKWGpwRqbYwse8oFJX4mGPmlHZoN0Co1BpfO7I-6D8iXZNm1CvaN45TNmHSg-4ockGT9z5zS5kEI6D5QWoWotMVOB-h22EtERT7knrIHJ_0AHmZMFjDX0I_-Bf2n2vNNo4ZdX8iHtSW0j0TZdgT2MMlQg6y-B7TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
وقتی خودتونم توی پلتفرم داخلی دووم نیاوردید!
🔹
سال‌ها اینترنت رو بستن و با فیلترینگ شدید خواستن مردمو به‌زور بفرستن سمت پلتفرم‌های داخلی، کلی هم بودجه خرج کردن و هر روز گفتن حمایت از پیام‌رسان بومی!
🔸
حالا بعد از این‌همه وقت، ستاد فضای مجازی خودشون جلسه گذاشته و گفته ممنوعیت حضور ارگان‌های دولتی توی پیام‌رسان‌های خارجی رو برداشتم، اسمش رو هم گذاشتن «پایان یک خودتحریمی عجیب»!
🔻
جالب اینجاست که می‌گن: «برمی‌گردیم همون‌جایی که مردم هستند». خب اگه مردم اونجان و خودتونم فهمیدید بستن این پلتفرم‌ها جواب نمی‌ده، چرا باید برای ارگان‌های دولتی آزاد باشه و پیج بزنن، ولی همون مردم برای باز کردن یه اپلیکیشن عادی هر ماه پول فیلترشکن بدن و با قطعی سر و کله بزنن؟!
این یعنی همون یک‌بام‌ودوهوای همیشگی؛ خودشون توی اپ‌های داخلی دووم نیاوردن و برگشتن، ولی زحمت و تاوان فیلترینگش هنوز رو دوش مردمه.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/iaghapour/2973" target="_blank">📅 19:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✍🏻
یه موضوعی هست که فکر می‌کنم بد نیست در موردش صحبت کنیم تا از سوءتفاهم‌ها جلوگیری بشه.
گاهی پیش میاد دوستی از سایتی که تو کانال ما تبلیغ شده سرور تهیه می‌کنه، چند روز یا یک هفته ازش استفاده می‌کنه، کانفیگ‌ها و متدهای مختلف رو روش تست می‌کنه و بعد که به هر دلیلی آی‌پی روی یه اپراتور مثل ایرانسل دچار اختلال یا مسدودی میشه، پیام میده که «سرورتون خرابه، بیاید رایگان آی‌پی رو عوض کنید.
واقعیت اینه که این روال، نه از نظر فنی درسته و نه منطقی
.
🔹
تست اولیه حق شماست:
وقتی سروری رو تحویل می‌گیرید، همون ساعات اول کامل تستش کنید. اگه دیدید همون بدو تحویل روی اپراتور مدنظرتون پینگ نمیده یا دسترسی نداره، کاملاً حق دارید به پشتیبانی پیام بدید، درخواست بررسی کنید یا حتی طبق قوانین هاستینگ سرویس رو عودت بدید. این حق کاملاً منطقی و محفوظه.
🔸
تفاوت خرابی سرور با محدودیت اپراتور:
وقتی سرور روشن و سالمه و روی بقیه شبکه‌ها یا اینترنت جهانی کار می‌کنه، یعنی سیستم مشکلی نداره. مسدود شدن آی‌پی بعد از چند روز کارکرد، ناشی از حساسیت فایروال اپراتور روی ترافیک عبوریه، نه نقص فنی سرور.
🔻
ارزش منابع:
آدرس IPv4 منبع محدودی در کل دنیاست و هزینه جداگونه داره. هیچ مجموعه‌ای نمی‌تونه آی‌پی‌های سالمش رو به خاطر مسدود شدن‌های بعد از استفاده، پشت سر هم و رایگان بسوزونه و جایگزین کنه.
👈🏻
ریسک اختلال روی شبکه‌های مختلف توی این بستر وجود داره و همه ازش باخبریم. بهتره با آگاهی از این شرایط خرید کنیم، تست‌های لازم رو همون ابتدای کار انجام بدیم، و اگر بعد از چند روز استفاده آی‌پی دچار محدودیت شد، مسئولیت این ریسک رو به پای خرابی سرور یا کم‌کاری ارائه‌دهنده نذاریم.
🟢
در همین راستا و برای حفظ حقوق شما، از امروز تمام ارائه‌دهندگان سرور که در کانال ما تبلیغ می‌شن، ملزم هستند تا ۱۲ ساعت بعد از خرید، امکان عودت سرویس یا تعویض آی‌پی رو در صورت وجود مشکل برای کاربر فراهم کنن.
بنابراین حتماً به محض تحویل سرور، تست‌هاتون رو انجام بدید تا در صورت وجود هر مشکلی، بتونید توی این بازه از این ضمانت استفاده کنید.
// قوانین در حال بروزرسانی و قابل تغییر هستش.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/2972" target="_blank">📅 19:09 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2971">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE0dUG-HAT6gZOqFqXxoLvCGJ4dSpWQs2eVo9G__a1wuH1N7yax6dG_ym3FtL_ArFVkXw2M6rpYcxpQvxetCwBNtYhyQ2DhZzVQO1ya0MZNY71RSNNt8d_yq30__NmAToJPbsf4pp31YGmhHgh5BRN3Aef5mMH9KwOKD4bi9fAnCrhAMRWPezzeuFz5Zeh2mrS-MgyFw4RTeM7z3RCEh5WJgGfsPktHvh3zasf-fm5-Knwnyk7BHyTGcEosY_VNlDh-Or1-HJ13r4mssRAH_PYLCpix9oxtqmXEQ-eOyhRSVLxS5fmUVyzfYdhgHti4GGikf8wyvtGLZULwbYgxfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
شکست قفل Denuvo بازی Mortal Kombat 1 و قدرت‌نمایی هکر Voices38
قفل امنیتی جنجالی
Denuvo
روی بازی پرطرفدار
Mortal Kombat 1
بالاخره پس از گذشت حدود سه سال توسط کرکر سرشناس موسوم به
Voices38
شکسته شد.
⚙️
چرا جامعه گیمینگ می‌گوید دنوو به سخره گرفته شده؟
🔹
طوفان کرک در ۲۴ ساعت:
هکر Voices38 نه‌تنها Mortal Kombat 1، بلکه در یک روز ۵ بازی سنگین و مجهز به دنوو از جمله
Persona 3 Reload
،
Star Wars Outlaws
،
Metal Gear Solid V: Complete
و
Prince of Persia: The Lost Crown
را کرک و منتشر کرد!
🔹
جانشین بی‌حاشیه دوران پس از EMPRESS:
برخلاف رفتارهای پرحاشیه و بیانیه‌های طولانی کرکرهای سابق، Voices38 صرفاً روی بایپس و حذف اجراییِ قفل در زمان کوتاه تمرکز کرده و عملاً انحصار دنوو را در سال جاری به چالش کشیده است.
🔹
آزادسازی منابع سیستم:
بازی‌های مجهز به قفل دنوو همواره به‌دلیل ایجاد لکنت، افزایش استهلاک پردازنده و افت فریم مورد انتقاد گیمرها بوده‌اند و حذف کامل این لایه محافظتی معمولاً به بهبود روانی اجرای بازی کمک می‌کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2971" target="_blank">📅 18:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2968">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz2QtR1kSqoBMi3WREJyNbYZd0BskxF_OE1lonfHZUCjhkKKtIUxLMI8qRQ-xYtrYodZyirR0DDu3yCCdQ-fLcBkVhmBTcJjpA6HxrajFQul6U_sq7JhxdfQ4m4qCvP9sJh-7o_yCUvc1O6V_wE3a9GLEydKYJ29Viy_-PQCZQJ8_0LhCHhtN1T3XNKN5oXOcpM6jj_NeWA7DO7iKtYh1U6-N9wPy6VS2yUfn0AeMAHvxO5Z4X3E2HHhpIEthvOe_ZZCDUgBmnwcm5Y2ZTpDffUUlQUkgdfumcXRgeaKdrzxiZqWRJJ_iYxm3J0UONH1LWgQMbEVb1NcjHBq4E5VDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بهترین پنل وایرگارد همراه با مدیریت حرفه‌ای کاربران + تانل
🚀
🔹
تو این آموزش بهتون یاد می‌دم چطور یک پنل جامع و سبک برای وایرگارد نصب کنید که هم امکان تعریف و مدیریت دقیق کاربران رو بهتون میده و هم قابلیت تانل زدن پایدار بین سرورها رو به ساده‌ترین شکل ممکن فراهم می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم قرعه‌کشی اکانت هوش مصنوعی داره و فقط تا فردا فرصت دارید! (شرایط: فقط قرار دادن کامنت زیر همین ویدیو).
👈🏻
قرعه‌کشی این ویدیو و ویدیوی قبلی با هم انجام می‌شه.
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2968" target="_blank">📅 18:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2967">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6kN_hqeU_ygrpx_gC4FyNcPs5UGS_XZ9RPWERBiWYs1Y1PMryIQ9tC7qkbL9QGgu8uRu-tWV4GIT2g5milQz3lpoPH4YfOEUrp5DIMI9whDxw4sQwycWvE8atbnbAQKW2BEh9JIYaCHyWAj94ZIX1CePo0hqei53kypoUZn4_q4lqc81s3ulzCZr4ZssPzbIqTarKdbrXb7la04lIrKrzChEzOC1-sBSHq0qRflE2nZ-rlfuZIR3QQWBW3uTbM8AUE7__QVxCMY3x8ZVaumtwPkWcaXp8PJTttlvK-Ypml9eLbN58G23hT9t5eUtnz6679iGEJbkoLAOJDOIVYBLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مایکروسافت از Project Zenith رونمایی کرد؛ نسخه‌ای اختصاصی برای توسعه‌دهندگان
مایکروسافت پروژه جدیدی با نام
Project Zenith
معرفی کرد؛ نسخه‌ای بهینه‌سازی‌شده، مینیمال و «آماده کدنویسی» از ویندوز ۱۱ که بخش‌های اضافی و نرم‌افزارهای غیرضروری را حذف کرده و تجربه‌ای نزدیک به لینوکس برای برنامه‌نویسان فراهم می‌سازد.
🔹
تمرکز ویژه بر هوش مصنوعی محلی
:
امکان اجرای مدل‌های زبانی محلی با بیش از ۳۰ میلیارد پارامتر (+30B) بدون محدودیت و افت کارایی.
🔹
پیش‌نیاز سخت‌افزاری سنگین:
طراحی‌شده برای سیستم‌های قدرتمند توسعه با حداقل
۶۴ گیگابایت حافظه رم
و پهنای‌باند بسیار بالای حافظه؛ نخستین بار روی مینی‌دسکتاپ Ryzen AI Halo شرکت AMD عرضه می‌شود.
🔹
بهینه‌سازی محیط برای کدنویسی:
نصب پیش‌فرض محیط‌های اجرایی (Runtimes)، ابزارهای ضروری برنامه‌نویسی و اعمال تنظیمات پیش‌فرض مناسب توسعه‌دهندگان.
⚠️
با وجود استقبال برنامه‌نویسان از یک ویندوز خلوت و بهینه، محدود شدن این نسخه به سخت‌افزارهای گران‌قیمت ۶۴ گیگابایت رم در بحران فعلی بازار حافظه، دسترسی بخش زیادی از توسعه‌دهندگان مستقل را با چالش مواجه کرده است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2967" target="_blank">📅 16:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2966">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=ektDWaln1biiIVIz7BYI0Tq_uXfyVX7hd21oXSjRoQqSnhYlQKcDTKLYqftVfwPpWdYJt2C0hfz_aK5ccryRvwvXjW8J6cQBa1-wo6tp4N2e5y3O6Dc00vpDxkmW0I99ZOlnFRkDgbf7BXpzXAU8iNjG_J2W-wmYNGY2fn2_682A6KonSSFR_z51hxTvYEATndQ63XLvSYa4-Qh7PRbYggZP6hev2rQMqUtVnf6ge61DCHQxbzA0bez2G9PrNgbo3sU6uVmhv06y5DPp_KKjmXLpDLPH6MDTq8xxMudxNfvzd0m2z3iM2BC3b8ktPCAUU-RROcNaL3IIETu_HeWFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8648566d.mp4?token=ektDWaln1biiIVIz7BYI0Tq_uXfyVX7hd21oXSjRoQqSnhYlQKcDTKLYqftVfwPpWdYJt2C0hfz_aK5ccryRvwvXjW8J6cQBa1-wo6tp4N2e5y3O6Dc00vpDxkmW0I99ZOlnFRkDgbf7BXpzXAU8iNjG_J2W-wmYNGY2fn2_682A6KonSSFR_z51hxTvYEATndQ63XLvSYa4-Qh7PRbYggZP6hev2rQMqUtVnf6ge61DCHQxbzA0bez2G9PrNgbo3sU6uVmhv06y5DPp_KKjmXLpDLPH6MDTq8xxMudxNfvzd0m2z3iM2BC3b8ktPCAUU-RROcNaL3IIETu_HeWFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
رونمایی مایکروسافت از MAI-Image-2.6-Flash؛ تولید ارزان و سریع تصویر
مایکروسافت نسخه سبک و کم‌هزینه مدل تولید تصویر خود را با نام
MAI-Image-2.6-Flash
از طریق پلتفرم Microsoft Foundry در دسترس توسعه‌دهندگان قرار داد.
⚙️
ویژگی‌های کلیدی:
🔹
سرعت بالا و صرفه اقتصادی:
۲.۸ برابر سریع‌تر از GPT-Image-2-Medium و با ۷۲ درصد کارایی بالاتر؛ ایده‌آل برای اتوماسیون و ابزارهای تعاملی پرمصرف.
🔹
ویرایش نقطه‌ای:
اصلاح دقیق اشیا، نوشته‌ها و چیدمان بدون تغییر در سایر بخش‌های تصویر.
🔹
ثبات کاراکتر و محصول:
امکان بارگذاری حداکثر ۵ تصویر مرجع برای حفظ یکپارچگی چهره و کالا در خروجی‌های مختلف.
🔹
اتصال به وب:
ارتباط مستقیم با موتور جستجوی بینگ برای رندر دقیق سوژه‌های واقعی.
💰
هزینه خروجی تصویری:
۱۹ دلار به‌ازای هر میلیون توکن (در برابر ۳۸ دلار برای نسخه پایه 2.6).
هر دو مدل هم‌اکنون در مرحله پیش‌نمایش عمومی در دسترس هستند./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2966" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2964">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psXnNRquQmOT3212a_g5sDNA4ovTSG34Xane8CsoUxFq0wnFG00ZHuIP0a1s69ij1Kr0QNMfplTD-b80edBNuilPYxXrWGu7kMN0UeyU3kl6L7bjpIp20PCVoHKkXNKiP0NWAVCIne1-sBXZiC9To8LVWxdoz9gtGv_Jlc6R_crlPEO2gis16q7dcjwdcpGuC8JtdQo7lvcnoXOdcFgmGNcO2Y9sk391TNRScylc65ocA3FNc9wZxDl4uDhH7D17gUJH1Mb9Mxsa1OBU3_FCzDjQPcctDHR2VQBABit8R9cY-4LId46tEOLPbLgNCuOEtGmpxLvyoz-AXjyKs48VDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل «زاگرس» (Zagros)؛ فورک چندهسته‌ای مرزبان
پروژه
Zagros
یک فورک از مرزبان است که محدودیت تک‌هسته‌ای را برطرف کرده و به شما امکان می‌دهد تمام هسته‌های معروف VPN را هم‌زمان روی یک سرور و نودهای مختلف مدیریت کنید.
⚙️
هسته‌های تحت پوشش:
🔹
هسته
Xray:
پروتکل‌های VLESS، VMess، Trojan و Shadowsocks
🔹
هسته
sing-box:
پروتکل‌های Hysteria2 و TUIC v5
🔹
سایر هسته‌ها:
WireGuard، OpenVPN، SoftEther، SSH Tunnel و PPTP
🚀
ویژگی‌های کلیدی:
🔹
اکانتینگ یکپارچه:
اعمال سهمیه حجم و محدودیت تعداد دستگاه متصل به‌صورت سراسری روی همه هسته‌ها و نودها
🔹
کلاستر نودها:
اتصال امن نودها با تایید Fingerprint و مدیریت هسته‌های مجزا برای هر نود
🔗
گیت‌هاب پروژه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2964" target="_blank">📅 20:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2963">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🧠
رونمایی اوپن‌ای‌آی از پرچمدار GPT-6 Astra؛ ادعای ورود رسمی به «عصر AGI» و انقلاب در کار با کامپیوتر
اوپن‌ای‌آی با رونمایی رسمی از مدل پرچمدار
GPT-6 Astra
، آن را جهشی نسلی در حوزه‌های امنیت سایبری، برنامه‌نویسی و تعامل مستقل با سیستم‌ها نامید؛ تا جایی که گرگ براکمن صراحتاً اعلام کرد:
«به عصر AGI خوش آمدید»
.
⚙️
ویژگی‌ها و قابلیت‌های محوری GPT-6 Astra:
🔹
توانایی عامل‌محور و کار با کامپیوتر:
این مدل بدون نیاز به رابط‌ها و APIهای پیچیده، مانند یک کاربر انسانی با موس، کیبورد و صفحه تصویر کار می‌کند؛ فرم‌ها را پر می‌کند، رکوردهای CRM را تغییر می‌دهد، نرم‌افزارهای مهندسی (KiCad/FreeCAD) را اجرا کرده و کدبیس‌های پیچیده را مدیریت می‌کند.
🔹
سرعت و بنچمارک‌های خیره‌کننده:
🔸
در تست OSWorld 2.0 امتیاز
۷۲.۶٪
را با سرعت حدوداً
۴۷ درصد بیشتر
از GPT-5.6 به ثبت رسانده است.
🔸
ثبت امتیاز
۹۸.۶٪ در آزمون معتبر تعمیم‌پذیری ARC-AGI-3
و امتیاز ۱۰۰٪ در بنچمارک ExploitBench.
🔹
جهش آموزشی با زیرساخت Stargate:
نخستین مدلی که با بیش از ۱۰۰٬۰۰۰ واحد پردازشی آموزش دیده و برای اولین بار، مدل‌های نسل قبل به صورت خودکار بخش اعظم نظارت بر آموزش آن را بر عهده داشته‌اند (حرکت به سمت خودبهبودی بازگشتی).
⚠️
ابهامات و حواشی مهم پیرامون رونمایی:
🔹
غیبت بنچمارک اقتصادی GDPval:
در گزارش‌های منتشرشده، نتایج آزمون GDPval (سنجش کارهای واقعی بازار کار و اقتصاد) دیده نمی‌شود که این امر تحلیل دقیق بازدهی سازمانی آن را فعلاً با شکاف روبه‌رو کرده است.
🔹
سایه بحران‌های امنیتی پیشین:
این رونمایی پس از حادثه جنجالی نفوذ یک مدل داخلی و منتشرنشده اوپن‌ای‌آی به هاگینگ‌فیس انجام شده و مدیران شرکت بر حفظ لایه‌های نظارتی سخت‌گیرانه روی ایمنی Astra تاکید دارند.
🔹
عرضه:
دسترسی سازمانی برای بخش امنیت سایبری از امروز آغاز شده و طی روزهای آینده برای کاربران Plus، Pro و Enterprise فعال خواهد شد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2963" target="_blank">📅 18:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2962">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev5q2YNdDbX4CFA-l-Ljh7Op3nlav_jMedKGyE3aT8gCSk4cjyZ9gA-L82gd_s2_5yEgRyKp-pNx2oMPPE97GwLe1T7o2t8_CYh9gvbhNshN_o5gUNBvg6pd87qVTAhExQqombUfSFosjmPfOAnjPr32KyWtMwXsCq_w2bMcMcLztzyYN11PSTXZxtAhwWcpMKC2F0tACWN2zIxCp2sZ2XKTdZAMfdA2B0IakbHNgW69F-DKfVocrahm0xIlsE_yuSbs3zX4QRjdmpvTfOkzgJ88jmjVt-Q_gtzHtlgwmlhZcW_Zz1rwZcX9Xsadv0ZzbkLHv3RYX3lgwzyobyPTKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏛
مخالفت زاکربرگ با طرح نظارت بر هوش مصنوعی در گفتگوی محرمانه با ترامپ
به گزارش نشریه
Politico
، مارک زاکربرگ، مدیرعامل متا، در یک تماس تلفنی خصوصی با دونالد ترامپ با پیشنهاد ایجاد یک نهاد نظارتی ملی و فدرال برای هوش مصنوعی به مخالفت پرداخته است.
⚙️
محورها و جزئیات کلیدی خبر:
🔹
پیشنهاد نظارتی به سبک FINRA:
این طرح که با حمایت دمیس هاسابیس (مدیرعامل گوگل دیپ‌مایند) و برخی مشاوران ارشد کاخ سفید مطرح شده، به دنبال ایجاد یک نهاد شبه‌مستقل ناظر (مشابه FINRA در بازار مالی) است تا مدل‌های پیشرفته هوش مصنوعی را پیش از عرضه عمومی، از نظر خطرات امنیتی و فنی ارزیابی و آزمایش کند.
🔹
موضع زاکربرگ:
مدیرعامل متا در گفتگوی ماه اوت خود با ترامپ تاکید کرده که هرگونه ساختار نظارتی باید با رویکرد «مداخله حداقلی (Light-touch)» دولت همسو باشد تا مانع رشد نوآوری و سرعت شرکت‌های فناوری آمریکایی نشود.
🔹
دو‌راهی دولت ترامپ:
کاخ سفید در حال حاضر بین دو گزینه مردد است: پذیرش مدل نظارتی مشابه FINRA یا انتخاب رویکرد صنعت‌محور و پیشنهادی دیوید ساکس (David Sacks) با حداقل سخت‌گیری دولتی.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/iaghapour/2962" target="_blank">📅 10:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYqD6RTHj5cvGUBPI6onOeWIqChwL4Dtcp1ljm7cBGYWpS9Ef9-V_65C1PM87UtLbus-EDTTYX4vCR7TT1S1vt2IO8R8bhcPFiK2tDRV3z1FJJ2dYvC11sXHG5d-J2v4mfTIePkmp16XoTogeDUFWbue1sOEvl6pNxDzLSYcc4h8AuEjia4zDpDvl5gpxXyw9S18-wiW-yybSx3bSz3FkO0hfeeOIqcUes4NaR1RqeS7ti24xvesBqfPmgYY9EJww7vEQ_FvVZz3yMGbKRumFdNOd61PIvLVzBYQqB017TqVUOKBGQ7btuq3lC6y52_jFUBgyb8fhYeVvGi3s8cfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
توصیه بابک زنجانی در الکامپ: گیر کلاهبرداری نیفتید
— بابک ولمون کن!
— بابک خجالت بکش!
— بابک حیا کن!
— بابک شعور داشته باش!
بابک زنجانی در قالب هلدینگ «دات‌وان» (با ۲۷ شرکت زیرمجموعه) در نمایشگاه الکامپ حضور یافت و از چند پروژه رونمایی کرد:
🔹
توکن و بلاکچین «دوتو»:
وعده پرداخت کوین به رانندگان تاکسی اینترنتی (بدون تاییدیه بانک مرکزی و بدون لیست شدن در صرافی‌ها).
🔹
سیم‌کارت و شبکه اجتماعی:
معرفی اپراتور مجازی «دات‌وان سل» بر بستر eSIM، پیامک انبوه و پلتفرم «مای دات».
🔹
پلتفرم معاملات طلا:
ادعای عرضه طلای ۲۴ عیار بدون حباب با ۱۹ لایه امنیتی.
⚠️
ابهام در مجوزها:
بانک مرکزی پیش‌تر اعلام کرده بود فعالیت‌های وی در بازار طلا و ارز فاقد هرگونه مجوز قانونی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2960" target="_blank">📅 20:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhODucmETABgRZb2fFK--XE5z2WXZG7jyeJnSmQb03bmTgHw_Ff0Dvi3PxzF1ThqIhNeLsh-XgUI9Vb5Yig4nAEszvAHbKN2g1VFQYQpBNO-6DoMtTSg2GgSQ2fPjvOIui9MYGcIG2vvpm4mi0RJDc1Evo7tlxB7BmmX0S_buy2oRY9OK5s4B-CEkFn7sVljR4Z9wKs0xEdiq6q4K4pPf4qYreSlL2XdDy7GeZIEIpsYNwa9Sb7f4lnegrvz6LQBgR_LNFkrzVB9AT26Fmo6iHnW3YoEtGCqreovCS7p2KD-wZB6u8dGVHq4Frk5h-7gmudWC2yK7IZKQYLQMa6vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
خاموشی هم‌زمان چت‌جی‌پی‌تی، گراک و کلاد
سه چت‌بات بزرگ و محبوب دنیای هوش مصنوعی شامل
ChatGPT
(اوپن‌ای‌آی)،
Grok
(ایکس‌ای‌آی) و
Claude
(آنتروپیک) به‌طور هم‌زمان دچار قطعی گسترده و سراسری در جهان شدند.
⚙️
جزئیات اختلال و سرویس‌های آسیب‌دیده:
🔹
دامنه قطعی:
دسترسی به رابط‌های چت، APIها، قابلیت‌های صوتی، تولید تصویر و بارگذاری فایل‌ها در هر سه پلتفرم با خطاهای گسترده روبه‌رو شده است.
🔹
اختلال در ChatGPT:
نمایش خطاهای مداوم و از کار افتادن سرویس ورود و جست‌وجو؛ این اتفاق هم‌زمان با انتشار پیش‌نمایش‌های مدل جدید
Astra
رخ داده است.
🔹
قطعی کامل در Claude و Grok:
سرویس کلاینت و کدنویسی Claude Code و همچنین چت‌بات Grok در وب، اندروید و iOS به‌طور کامل از کار افتاده‌اند.
🔹
علت نامشخص:
تاکنون هیچ‌کدام از شرکت‌ها دلیل دقیق این خاموشی هم‌زمان یا ارتباط احتمالی میان این اختلالات زنجیره‌ای را رسماً تایید نکرده‌اند و تیم‌های فنی در حال رفع مشکل هستند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
قیمت آیفون ۱۸ پرو و ۱۸ پرو مکس لو رفت؛ افزایش ۱۰ تا ۲۰ درصدی به‌دلیل بحران حافظه
✍🏻
احتمالا با این وضعیت دلار و سودی که  دولت بابت ریجستری گوشی میگیره که در اصل یکی باید برای دولت بخری یکی برای خودت فکر کنم بالای نیم میلیارد پول این گوشی باشه تو کشور.
😐
بر اساس تازه‌ترین گزارش مؤسسه پژوهشی
ترندفورس (TrendForce)
در آستانه رویداد جدید اپل، پرچمداران سری پرو نسل جدید احتمالاً با افزایش قیمت ۱۰ تا ۲۰ درصدی نسبت به نسل قبل روانه بازار خواهند شد.
⚙️
پیش‌بینی قیمت‌ها و مدل‌ها:
🔹
آیفون ۱۸ پرو:
بازه قیمتی
۱٬۲۴۹ تا ۱٬۲۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۰۹۹ دلاری آیفون ۱۷ پرو).
🔸
آیفون ۱۸ پرو مکس:
بازه قیمتی
۱٬۳۴۹ تا ۱٬۳۹۹ دلار
(در مقایسه با قیمت پایه ۱٬۱۹۹ دلاری آیفون ۱۷ پرو مکس).
🔹
آیفون تاشو (آیفون اولترا):
ورود به بازار با قیمت پایه
۲٬۰۹۹ تا ۲٬۲۹۹ دلار
و احتمال عبور قیمت قوی‌ترین کانفیگ از مرز
۳٬۰۰۰ دلار
.
🔍
علت اصلی گرانی؛ بحران و تقاضای هوش مصنوعی:
🔹
هزینه تامین تراشه‌های حافظه ۲۵۶ گیگابایتی به دلیل توسعه سنگین زیرساخت‌های AI در سطح جهان نسبت به سال قبل نزدیک به
۴۰۰ درصد جهش
داشته است.
🔹
هزینه تمام‌شده قطعات (BOM) برای یک نسخه پرو ۲۵۶ گیگابایتی حدود
۳۸ درصد افزایش
یافته که زنجیره تأمین اپل را تحت فشار گذاشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/iaghapour/2958" target="_blank">📅 18:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vv0lxxH-ikQZxdau9TkWW9sp2kPf6iPdlVvn_ydAYU6Sqy1VolkvOAI_YbdrYbph_e4XtA7y3E8CQtK_chE6kqTXYlyd5H5IrrROZFaSji_CCn5MBMlHhhNEEkjXST7J1JM8ew8lULk7LPdZutjvWOmntSxfaDzpAsmKYa6-NHc0u5zoV3Y4oLXjsvfhFHAnbN7fnEvqs7-hSkclg6AUs150miqnS0BsRI7ki-hkkereWRkLgKYb7f6B4VFFehf7heIFQ8A7SndY1x2LViIc31x49KP4Qcgee_SZ1ugeC0XN5Q_2yR8c8551QZPfp2VK0vUnVURuRsBQ677SIoYIXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پنل همه‌کاره فیلترشکن (انواع هسته + تانل داخلی و مدیریت با هوش مصنوعی)
🚀
🔹
تو این آموزش یک پنل فوق‌العاده رو بررسی می‌کنیم که نه تنها از هسته های مختلف (مثل Xray و وایرگارد و OpenVpn و L2TP) پشتیبانی می‌کنه و تانل داخلی اختصاصی داره، بلکه به کمک هوش مصنوعی تنظیمات و کانفیگ‌ها رو براتون بهینه‌سازی و مدیریت می‌کنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#پنل
#تانل
#وایرگارد
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🛡
چک‌لیست طلایی امنیت اینستاگرام؛ ۷ قدم تا ضدگلوله کردن حساب کاربری
با صرف چند دقیقه وقت و اعمال این ۷ تنظیم کلیدی، احتمال هک و نفوذ به اکانت اینستاگرام خود را به حداقل برسانید:
🔹
۱. تغییر رمز عبور یا فعال‌سازی Passkey:
استفاده از پسورد طولانی و ترکیبی یا کلید عبور هوشمند.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Change password
🔹
۲. فعال‌سازی تأیید هویت دومرحله‌ای (2FA):
ایجاد لایه امنیتی قدرتمند؛ حتماً از اپلیکیشن‌های Authenticator (مانند گوگل یا مایکروسافت) استفاده کنید، نه پیامک (SMS).
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Two-factor authentication
🔹
۳. بررسی نشست‌ها و دستگاه‌های متصل:
مشاهده نشست‌های فعال و لاگ‌اوت کردن دستگاه‌های ناشناس یا مشکوک.
📍
مسیر:
Settings and activity > Accounts Center > Password and security > Where you're logged in
🔹
۴. لغو همگام‌سازی مخاطبین گوشی:
جلوگیری از آپلود شماره تلفن‌ها و پیشنهاد اکانت به مخاطبان دفترچه تلفن.
📍
مسیر:
Settings and activity > Accounts Center > Your information and permissions > Upload contacts
🔹
۵. خصوصی‌سازی پیج (Private Account):
محدود کردن دسترسی به پست‌ها و استوری‌ها فقط برای دنبال‌کنندگان تاییدشده.
📍
مسیر:
Settings and activity > Account privacy > Private account
🔹
۶. حذف دسترسی برنامه‌ها و سایت‌های متفرقه:
قطع دسترسی ابزارها، ربات‌ها و وب‌سایت‌های شخص ثالث به اکانت.
📍
مسیر:
Settings and activity > Website permissions > Apps and websites
🔹
۷. عدم نمایش پیج در بخش پیشنهادات (Suggested):
جلوگیری از نمایش حساب شما در بخش اکانت‌های پیشنهادی به سایر کاربران (از طریق نسخه وب اینستاگرام).
📍
مسیر: ورود به وب‌سایت
instagram.com
> بخش
Edit profile
> غیرفعال‌سازی تیک
Show account suggestions on profiles
©️
پس‌کوچه
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNOfBiSm9CRP4ZDEk0rZsWez42Hb0lKFIzLjpYDqj8TcfbEsHdxNcflz_0qJyjKHK6NS4bOMn-FhjYX0BrgcHeQDpRi-CRNYe21_d2f2MjsnUZ80jAU7hCnulX5AOtmTzQ1wlu1bkhqfolJNhjh-pGMTMTKmPSuB-NjlBKzU-dRe29fJs99zTonYrAozHTPkDf0S8nO8dC2gvUaZt5iou4ft94DB3uO-5fsc76cIQZbtOTH9_WLyha7SRzl5fnUBi5dlI2HxGqCnyXP0fM5VLuCd_P-W_MKjxrtkmq_ueAXCgUjdZjoXasP3Efwemfb8lZRkUT2KOaGS2Dw6TDCIUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2951">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b89lrMavKdhuNKXWUSRSB65RMSytAqX7OpvWYeijORiUHwwpqatYwK3uOA9A7ZOovgQafrSktPAtNKD_7Jxw7UjTwQurl688ntQuhALuj6ZMDDJcMZb_FyX0rwS6Yu0Mw-aTxTwSfHqYJGOBb1AP-Otobzdxmgrgk0YinLx0Xpxy6GMEFcng9l8JgW395acFHxvXxrKMEZuZYUFtAl7zbVtjKGkKSLt6oIA7Y2kksYpHkDj1XBxIlfRMMQzJ0Hhy8Vlp-Q29BXW_wbxUS3WDB49FiHMO3v5J_gJLyVQAx4-Y8oppLgq2uJeAwV2O7dzvRkBexXAkKaaZuxKjLGEycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنتر ها است.
در این طرح شماره موبایل + شماره ملی + آی پی به هم وصل می‌شوند و بدون ثبت آی پی در سامانه شاهکار دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©️
Saeed Souzangar</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/iaghapour/2951" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2949">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ncfJoSdPnAlCUJ7hZEVOGy2iwnOkd4IPSji1EukjIU2t6lKGCXaynCtOuRZvOyEfE3v3RhDcfwtF54C1-GKjH31k17aAx2V3iixCoQw4JDkzrGv_wnKk9r0jcsu8IEZY1XWe0cBcQqjAKQ_kiKpwmEm33w9XiWIyXmuXLfDqs63jRxQCpnddKv3k0F0zhgp20DIBTK4_LIYXvxewtbhIyTmqYoWiVrzwuzKCKuO3DT7hylb98T1DrOiv6IVgLp-p3-ijUtd-_8M9o4437CKmf0XeO4mGqXN0yYLikaRmqtW79jCqkBkv-u8-Z-Kiu3Wo8Tmlm51bPLfy2Bw1UUmskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معاون وزیر ارتباطات: گران‌فروشی اینترنت احراز نشده است / فیلترشکن‌ها منشأ اصلی حملات سایبری هستند
محمد حاتمی‌زاده، معاون حقوقی و امور مجلس وزیر ارتباطات، در جمع خبرنگاران پیرامون ادعای تغییر حجم و قیمت بسته‌های اینترنتی توسط اپراتورها و چالش‌های امنیتی شبکه توضیحاتی ارائه داد.
🔹
عدم احراز گران‌فروشی اپراتورها:
علیرغم دریافت گزارش‌های مردمی و بررسی اسناد توسط سازمان تنظیم مقررات (رگولاتوری)، تا این لحظه وقوع تخلف یا گران‌فروشی بسته‌های اینترنت اثبات نشده است و نظارت‌ها همچنان ادامه دارد.
🔹
فیلترشکن‌ها؛ حفره امنیتی و اقتصادی:
استفاده گسترده از فیلترشکن‌ها به ساختار شبکه مخابراتی ضربه زده، باعث نارضایتی کاربران شده و ریسک‌های امنیتی بزرگی را به کشور تحمیل کرده است.
🔹
منشأ داخلی حملات سایبری:
به گفته وی، بیشتر حملات سایبری ثبت‌شده در کشور از طریق بستر همین فیلترشکن‌ها و از داخل خاک کشور هدایت و انجام می‌شوند.
🔹
محدوده اختیارات وزارت ارتباطات:
تمرکز این وزارتخانه صرفاً بر اقدامات و مدیریت فنی است و ساماندهی کامل این فضا نیازمند همکاری نهادهای امنیتی و نظارتی است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/iaghapour/2949" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcn--BO3Mz2NLtT7z9Vlqx419ZO8c4T_vfi7NeqehOz2ZApsVVR6kpaed9boBik5jNvGzwtgIGS2cZiJ1Gg5p5TTwxvAU1L_LP6m05jQU6UiN7gFsCaKtrsBynVcKWde2Wp8OCBw9Tz3YGvinl5xZs0ilEcX0A37VaTkvA1kqjLfcVSAzpMaJLM-hcyNq1Xnp4fDRhq86-6g4A_yIogSO0WzfPNe_tMZ2N4Jen12J7WfUrnuZ9689eWf0-NmkhqbGht8Dvxxt-PTw_lxqagJI3_lDR5EsiDHO19x7eXjxIk27LWAD40ijZfsmBY21UDO0PGAgNnJQuj6LxK6M49t_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌸
تقدیر و تشکر از یک همراه همیشگی کامیونیتی | مارک عزیز
در روزهایی که دسترسی آزاد به اینترنت و سرویس‌های پایه برای کاربران و توسعه‌دهندگان ایرانی به یک چالش روزمره و فرسایشی تبدیل شده، حضور افرادی که بی‌سروصدا و بدون چشم‌داشت برای رفع این موانع تلاش می‌کنند، غنیمتی بزرگیه.
امروز میخوام از
مارک
عزیز صمیمانه تشکر کنم. کسی که شاید خیلی از ما اون را نشناسیم یا از حجم فعالیت‌هایش بی‌خبر باشیم، اما مارک همیشه حامی دسترسی آزاد به اینترنت بوده.
مارک عزیز، از طرف کل کامیونیتی، بچه‌های شبکه و همه اونایی که نتیجه زحماتت بهشون می‌رسه، بهت خسته نباشید می‌گیم. واقعا مرسی که اینقدر دلسوزانه پیگیر کارها هستی. دمت گرم که همیشه هوای بچه‌ها رو داری!
💚
✌️
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⭕️
موضع دفتر رئیس‌جمهور درباره فیلترینگ: دوره محدودیت و اینترنت طبقاتی گذشته است
سید عباس موسوی، سرپرست معاونت سیاسی دفتر رئیس‌جمهور، در گفت‌وگویی مواضع دولت پیرامون رفع فیلترینگ، اینترنت طبقاتی و فناوری‌های نوین ارتباطی را تشریح کرد.
🔹
پایان دوره فیلترینگ با پیشرفت فناوری:
با گسترش فناوری‌هایی نظیر اتصال مستقیم گوشی‌های همراه به اینترنت ماهواره‌ای، سیاست‌های اعمال محدودیت و فیلترینگ دیگر کارایی فنی ندارند و دوره آن گذشته است.
🔹
رد کامل اینترنت طبقاتی و تجارت فیلترشکن:
تداوم محدودیت‌ها در زمان صلح، ایجاد دسترسی‌های طبقاتی به اینترنت و شکل‌گیری بازار فروش فیلترشکن به‌هیچ‌وجه قابل قبول نیست.
🔹
تفکیک شرایط جنگی از زمان صلح:
اعمال محدودیت‌های مقطعی ارتباطی صرفاً در شرایط اضطراری، بحران‌های امنیتی و جنگی برای مقابله با تهدیدات سایبری توجیه‌پذیر است، نه در شرایط عادی.
🔹
رویکرد پیگیری رفع فیلترینگ:
پیگیری موضوع رفع محدودیت‌ها در جلسات تصمیم‌گیری بدون ایجاد تنش و بر پایه اقناع و وفاق انجام می‌شود./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/iaghapour/2947" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=YnS6nB6FoijtPy2rLhi9wauUaKSUQg1Mm2q3U4N0fAkF3X4sinC2GQl6Y8YkhtMQph4vZ1tLW4kL9pyB6epAd-HMkzo33iKugHTaiqxM9aEVoJLchzQ2v6Se-ea4cYVOxRg_BAkhy2ZvsOxPvIsvtMNd-fDYmQ0B3D2bCGvcLseUhJL-BraAjIf6szuY53ZSIzuMTpuPSRWe4lPYY9KLFwgtjd2sGno2BPGCQFNhGIciPlQZmfWlfAOXYYkdHDVUPogB21_KMuzPfnoShijW5x3P526myiIVEyNJ1tl_DEIxQRsBmd-lSO8MOj3LPeLmmpOafle-rudf0bdBNHjVpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=YnS6nB6FoijtPy2rLhi9wauUaKSUQg1Mm2q3U4N0fAkF3X4sinC2GQl6Y8YkhtMQph4vZ1tLW4kL9pyB6epAd-HMkzo33iKugHTaiqxM9aEVoJLchzQ2v6Se-ea4cYVOxRg_BAkhy2ZvsOxPvIsvtMNd-fDYmQ0B3D2bCGvcLseUhJL-BraAjIf6szuY53ZSIzuMTpuPSRWe4lPYY9KLFwgtjd2sGno2BPGCQFNhGIciPlQZmfWlfAOXYYkdHDVUPogB21_KMuzPfnoShijW5x3P526myiIVEyNJ1tl_DEIxQRsBmd-lSO8MOj3LPeLmmpOafle-rudf0bdBNHjVpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی
(دوره هفتم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 1 عدد اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
برنده عزیز با آیدی pinkpantheranim مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسر عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در ویدیو بعدی باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎮
ویدیو مقایسه جذاب GTA 6 با GTA 5؛ جهش خیره‌کننده گرافیک و گیم‌پلی بعد از ۱۳ سال
با نمایش گیم‌پلی بازی موردانتظار
GTA 6
، مقایسه‌های فنی میان این نسخه و بازی محبوب GTA 5 نشان‌دهنده یک ارتقای نسلی و عمیق در استانداردهای بازی‌های جهان‌باز راک‌استار است.
🔹
جهش چشمگیر گرافیک و جزئیات بصری:
بهبود محسوس در طراحی چهره، فیزیک و انیمیشن موی کاراکترها، سیستم نورپردازی پیشرفته، ارتقای کیفیت بافت‌ها (Textures) و ارائه پوشش گیاهی و محیط‌های شهری فوق‌العاده زنده و واقع‌گرایانه.
🔹
انیمیشن‌های طبیعی و گیم‌پلی واقع‌گرایانه:
طبیعی‌تر شدن فیزیک حرکات شخصیت‌ها و تعریف استانداردی نوین در زمینه تعامل با محیط، اکوسیستم شهری و واکنش‌های هوش مصنوعی NPCها (شخصیت‌های غیرقابل‌بازی).
🔹
پلتفرم‌های مقصد و قیمت‌گذاری:
نسخه استاندارد با قیمت ۸۰ دلار و نسخه آلتیمیت با قیمت ۱۰۰ دلار در دسترس پیش‌خرید قرار دارند.
📅
تاریخ انتشار رسمی:
۱۹ نوامبر ۲۰۲۶ (۲۸ آبان ۱۴۰۵)
برای کنسول‌های پلی‌استیشن ۵، ایکس‌باکس سری ایکس و ایکس‌باکس سری اس. /منبع:sargarme
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqJ5CEF-tJMdn7svGeZcfdGOYoIz91EnHDUO9kfXgmED6feJalKsC_y0VIg8QiZZTv-aLF8PjHZaSGsW-s7EM7z5O17orPWl8F4-x4sgBhdYFBynwCykwN1VrFUJ4YS-kD1nDEvZ7Q4PZwrg08iE6uA2o4vg9Ccq3XvgTrlIdjosxMW4Ah7d6TRThWGETKamyqG-DYKdkfjWbJqr66UxNVg_CkvR9IaAjOFM-wuebERZ54AwVXFc5-sa07XSp75NGoq3_Cch3KdmASN2g4lPMgD6C57Y2gAk2EV5FnfqpgO8Ox61V_NOhNabxgjL3g2M1jZGhA2gvzUUg3Y3Ddj-Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی PingTunnel VPN Client؛ کلاینت ویندوز برای پروتکل ICMP
پروژه
PingTunnel-VPN-Client
یک کلاینت مدرن تحت ویندوز (WPF) است که با ترکیب
pingtunnel
،
tun2socks
و آداپتور
Wintun
، امکان عبور دادن کل ترافیک سیستم از بستر پکت‌های ICMP (پینگ) را فراهم می‌کند.
🔹
مانیتورینگ و نمایش زنده ترافیک:
نمایش لحظه‌ای سرعت دانلود و آپلود تانل به همراه مصرف کارت شبکه فیزیکی و سیستم لایو لاگ (Live Logs).
🔹
امنیت DNS و بهینه‌سازی ترافیک:
مجهز به فورواردر و کش داخلی DNS جهت جلوگیری از نشت DNS (DNS Leak Protection) و مسدودسازی UDP روی اینترفیس TUN جهت جلوگیری از خطاهای ناشی از ترافیک QUIC.
🔹
پایش سلامت و اتصال پایدار:
بررسی مداوم تاخیر (Latency) با قابلیت ری‌استارت خودکار در صورت افت کیفیت، به همراه سیستم بازیابی پس از کرش و پاک‌سازی رول‌های فایروال.
🔹
قابلیت Split-Tunneling:
امکان مستثنی‌کردن ساب‌نت‌ها و رنج‌های آی‌پی مشخص جهت عبور مستقیم ترافیک بدون رفتن به داخل تانل.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOd6HxMDhH48-zQW9Ctt_QVv4YH2riqAWcXwly0MKRKqmDVJhGVJp-U-9fqqjTrp1pva_bc7PZ04RZysRnWJXU8E4cbzdBDV9t_QBjCmubPYdzSEtR8Pi2UnRVuiyvMjnQMhcDanLaxIEn4f3etmjOMpal2RQ50ZZ5Y8x-KdJ0FxWMYVWmEX55E9Bvrf9D_bzgmcOeNFsbK5wVOqaEB7jHxKs5_yycNLyEEjDYbPnMFy6YIYuLFzDjEqlllruoUp7kF-JkSZyqUVEiV5k6S6lRuGi9lOTSSdHXZ3eEdj2tGXFm-RMIGwl2TnRa_0J_ceOfr_Mrjyy-nduaL_0WARzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مقایسه WiFi 6 در برابر WiFi 7؛ کدام نسل در سال ۲۰۲۶ ارزش خرید دارد؟
با گسترش روترهای
وای‌فای ۷
انتخاب میان خرید یک روتر جدید نسل ۷ یا یک مدل مقرون‌به‌صرفه نسل ۶ به یکی از دغدغه‌های اصلی کاربران شبکه تبدیل شده است.
⚙️
تفاوت‌ها و مزایای اصلی WiFi 7
:
🔹
پشتیبانی از فناوری (Multi-Link Operation):
ارسال و دریافت همزمان داده‌ها روی سه باند ۲.۴، ۵ و ۶ گیگاهرتز که پایداری ارتباط و سرعت را به‌ویژه در محیط‌های شلوغ به اوج می‌رساند.
🔹
افزایش پهنای باند کانال تا ۳۲۰ مگاهرتز:
دو برابر پهنای‌باند WiFi 6E که برای استریم محتوای 4K/8K و کاهش تاخیر ایده‌آل است (در مدل‌های پیشرفته سه‌بانده).
🔹
سرعت تئوری و برد بالاتر
و
سازگاری کامل با نسل‌های قبلی
دستگاه‌ها و تجهیزات قدیمی.
🤔
آیا خرید WiFi 6 هنوز منطقی است؟
🔹
بخش زیادی از لپ‌تاپ‌ها و گوشی‌های فعلی هنوز از پهنای‌باند ۳۲۰ مگاهرتزی یا سه باند همزمان پشتیبانی نمی‌کنند.
🔹
برای کاربردهای روزمره، استریم و سرعت‌های معمول اینترنت، یک روتر باکیفیت WiFi 6 کافیه./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLC5ePRi3ck1NtQ8K6G8wcPm9MH8t8p0c-KX97yUq70foD93ED0sBgnzqprVFOv1_c6QKpcob4OIYNeXqYAaEVWWXdybcJZd-1iWt9BP36Rp4jqFi95B3vba1nud2TcXry82DBCyjmfMOjzWLY3m1iP-dlG3FayyOWHUjMVlzMwFnriBLjHX9msEgf800w9d3w-4fN1v4IywqeFNhhNyrwas5IeLRLC276BsIAbLU6a9OOq5vfdWLImNmeYQsUN4Sc3wcVp8q3DNlsvQgo28CqCJaXuTdkR7vcc1QJ6h7KGjgKYDIWfIjOUFPEWXW-QMisBcP19QSaoASnaDhFpFUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
گوگل در حال آزمایش هوش مصنوعی Gemini 3.8 Flash
بر اساس گزارش‌های فاش‌شده، شرکت گوگل فاز آزمایش داخلی نسخه پیش‌نمایش مدل جدید
Gemini 3.8 Flash Preview
را روی پلتفرم کدنویسی اختصاصی خود موسوم به
Jetski
کلید زده است؛ اقدامی که از احتمال انتشار عمومی آن در آینده بسیار نزدیک خبر می‌دهد.
🔹
پیشرفت چشمگیر نسبت به نسل قبل:
طبق ارزیابی‌های اولیه کارکنان، نسخه ۳.۸ فلش عملکردی به‌مراتب بهتر و ملموس‌تر نسبت به ۳.۷ فلش در سناریوهای مختلف ارائه می‌دهد.
🔹
تمرکز ویژه روی مدل‌های اقتصادی و پرسرعت (Flash):
در حالی که مدل‌های سنگین پرو در دست توسعه هستند، گوگل تمرکز اصلی خود را روی بهینه‌سازی مدل‌های ارزان، سبک و پرسرعت سری فلش برای کدنویسی و توسعه دستیارهای هوشمند (Agents) گذاشته است.
🔹
سرعت سرسام‌آور چرخه انتشار:
پس از عرضه نسخه ۳.۶ در اوایل تابستان و معرفی نسخه ۳.۷ تنها با فاصله ۳ هفته، اکنون نسخه ۳.۸ وارد فاز تست شده است.
🔹
رؤیت در بنچمارک‌های جهانی:
شواهد نشان می‌دهد که ردپای تست‌های آزمایشی این مدل به‌تازگی در وب‌سایت معتبر ارزیابی هوش مصنوعی
Arena AI
نیز مشاهده شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JM2j3kio7_gpwb3DMccS28h9KG9WgLb6wL7V7_6dpVT9-jLO97U-wjRW0hohcicPjIl2_JT5uxUBI1EBoIhToFZ4IlCCVflKgZI3mX_gov1z8yNbUGyjGPb63e1e_CQAZG88_cGclDlw4BYG-aU3NtYxLgEGmPXl6_m5yws6fHsI2m7IzrHfW3dLGUBVa9C1GSPDy-KR9W_NcRiwB0qawdNUb-FIW_7K_bS2Y4kH5cPS5DHqBnCpFj4SSV6k7ubEwSZsNW4aViclJvnysevhtsg86dp20PjqBrOU1QChIk1D6ZYkzHp8p_87cFQgqIKvj9Hi7ZW3ThFQevIuQF90GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GIWhymn8AcXUoolsc27T4mXqw0ANDHhKHaJeaJRMuSb-BQ_eLMLqEArh6Y6A7n68sWEcyUSh1ceFwZ65b7EgpeM8iX8eEyd32FNr0Fh4zhkqLIv5X3Pa6cNQssTh34iTS8FQ3_jwe0-NjxsHSonmKsYr7Sr4Q04fhvM7S051Gf6AzA4FcHJW6Ly5ccZjbSfEDMLNFfVgKKWpvfS__sdlPIXYxhDmjreq4HaJPJioZd7BlXsDWhP8hS6j5uilBwCnPKw5lSipAkNvEf8MSbLuMzwkPVZDksYvOf5o_ZydA4rnqNuaSdEuLK7-JQJvwbg6xqgDee7HR9Xm_U5OyzTVIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎮
فناوری DLSS 5 انویدیا پیش از عرضه رسمی لو رفت
تصاویر فاش‌شده از نسخه آزمایشی و اولیه
DLSS 5
انویدیا روی بازی‌های کامپیوتری نشان می‌دهد که این فناوری رندر عصبی هنوز تا رسیدن به استانداردهای مطلوب فاصله زیادی دارد.
🔹
تغییر رویکرد در آپ‌اسکیل:
برخلاف نسل‌های پیشین که تمرکز روی افزایش شفافیت تصویر بود، DLSS 5 با بازتولید هوش مصنوعی تلاش می‌کند متریال‌ها و نورپردازی را بازسازی و فوتورئالیستی کند.
🔹
نتایج عجیب و غیرطبیعی روی چهره‌ها:
در تست‌های اولیه روی کاراکترها چهره شخصیت‌ها دستخوش تغییرات سنی نامتعارف شده و ترکیب این چهره‌های تغییریافته با انیمیشن‌های حرکتی ثابت بازی، حس غیرطبیعی و ناهماهنگی ایجاد کرده است.
🔹
افت FPS:
فعال‌سازی قابلیت رندر عصبی در بازی Control روی کارت گرافیک
RTX 5070 Ti
در رزولوشن 4K، فریم‌ریت را از
۷۱ فریم‌برثانیه به ۳۵ فریم‌برثانیه
کاهش داده است.
🔹
نسخه رسمی DLSS 5 برای پاییز برنامه‌ریزی شده و باید دید انویدیا تا چه حد می‌تواند با بهینه‌سازی نسخه نهایی، مشکلات افت پرفورمنس و رندر غیرواقعی را برطرف کند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grS7bWB8A2oMW7FyIFeNuSoGiF1wxtdrbSlIzMWa5bVPQoc_E-fVOzEGAU4uD19WAD7FaA3ikPhHBxk3pMic2YlfjY95g02f7mBikSuU9JiVrWOJ5ISXR-Scm8aftYfHKrzGejJEp-9fCj-25clRzFS_OP5wjce3TrE6YIUZtxv2oHjDuFWnmgpIA7zfsJvJ5R0PGz2coz7ufuS2Qlh8IRUjBEKFaxRu0_Cy77d3Rm_vQorNY-EL1-p8PzbVrnFVosYyrgV4V5aiZJ4Gmg9jwc-hUJJAE6DHbpSh94U3tLgWg7LSLnFbSOIif81TAcZH_CcFwIU6-vpt1KsFbN0Q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚫
توقف کامل آزمون زبان دولینگو (DET) برای تمام دارندگان مدارک ایرانی از اول سپتامبر
بر اساس اعلام رسمی پلتفرم
Duolingo English Test
، از تاریخ
۱ سپتامبر ۲۰۲۶ (۱۰ شهریور)
، دسترسی به این آزمون برای تمام متقاضیان داخل ایران و همچنین افراد دارای مدارک هویتی ایرانی متوقف خواهد شد.
⚙️
نکات و جزئیات مهم این تصمیم:
🔹
محدودیت فراتر از موقعیت جغرافیایی:
این تصمیم صرفاً مسدودسازی IP یا موقعیت مکانی ایران نیست؛ بلکه تمام افراد دارای مدارک هویتی و پاسپورت ایرانی (حتی در صورت سکونت در خارج از کشور) امکان احراز هویت و شرکت در آزمون را نخواهند داشت.
🔹
تاثیر بر مهاجرت تحصیلی و اپلای:
با توجه به پذیرش مدرک دولینگو در بسیاری از دانشگاه‌های معتبر بین‌المللی، این تصمیم فرآیند اپلای متقاضیان ایرانی را دچار چالش جدی می‌کند.
🔹
پیشنهاد به متقاضیان:
متقاضیان ادامه تحصیل باید پیش از هرگونه اقدام، فهرست مدارک زبان مورد تایید دانشگاه مقصد را بازبینی کرده و آزمون‌های جایگزین (مانند آیلتس یا تافل) را در برنامه خود قرار دهند./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ScGvriD7loRCdDhuuiJCQzErle85_Y3XP9tm22l-V5TgRg96BN1PQ1aaupR8o0X-i5jo35O9_NueS90Am3u-jdv2SWwAs6bSE4G0a4h6OagxvrsrkugH_3M5eyJJygjxU5FKMcOUFbOLUQ8zr5e3i_M6isc5QW9a97UaozX_hNDlTbRPj6LCYSvLsBDATkuoiMneM0AFyQrWNoy_9WQ3_SEbMAy1SRwVFpZT7J6aZ5ul36S6vZlGYgmnWnf71ihBlViPmElgDKrOdjdmBynlomxl7KCvhU4UVzkyfe7EdtPiJHwj9JjolMmHURg_BVv1TOYjoquWXDroV7b0WUnKIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی پنل مدیریت نمایندگی و ادمین برای 3X-UI
پروژه
x-ui-reseller-panel
یک واسط تحت وب مدرن است که به مالکان سرور اجازه می‌دهد بدون دادن دسترسی مستقیم به پنل اصلی، دسترسی‌های مدیریت‌شده و تفکیک‌شده به نمایندگان بدهند.
🔻
امکانات اختصاصی ادمین:
🔹
ایجاد، ویرایش و حذف اکانت‌های نماینده
🔹
تخصیص سقف ترافیک اختصاصی برای هر نماینده
🔹
محدودسازی دسترسی هر نماینده به اینباندهای مشخص
🔹
مانیتورینگ کاربران آنلاین و آمار مصرف ترافیک زنده
🔹
پشتیبان‌گیری از دیتابیس پنل و پشتیبانی از تم تاریک و روشن
🔻
امکانات پنل نماینده
:
🔹
صفحه ورود مستقل برای هر نماینده
🔹
ساخت، ویرایش، حذف کاربر و ریست حجم مصرفی
🔹
باطل کردن لینک اشتراک (Revoke Subscription)
🔹
مشاهده کاربران آنلاین و حجم باقی‌مانده
🔹
همگام‌سازی خودکار ترافیک با پنل اصلی X-UI
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZVnCf2ogQno7Uub58k8rjUaOPv7xqtOGi943D9C3H4Gg6YCsBdrJRAmfkU5-wBoKZx1Ho0PBpJfnNNw6wYBNO-5OViXHN28cv8jKFcuZbbVH5d5ubg2jJk_d7Rr28w-fah0VfyQNNpMn7NqA1-b8i0f1XgaRZNSHnJFBD9XoNaCs6zzLp3qxGtpI4jN6M0GzbrXohq9zaOijHv2BjQ1pSzPSE_OGB6vfjJdBPnWjx3D6huqsyIOmrL3nQNHYL6briVNE0uTZw5iYPW86d763nvUtdb3Lp3mQxFaL0kSnlOFgG570DcjkKyE7WyQB7M4uAIiSLLM2t4lRQ3J1kMebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ربات فروش خودکار کانفیگ تلگرام (جایگزین ربات میرزا) + آموزش راه‌اندازی
🔹
اگه دنبال یک راه بی‌دردسر برای اتوماتیک کردن فروشتون هستید، این ویدیو دقیقاً همون چیزیه که بهش نیاز دارید. تو این آموزش یک ربات تلگرامی فوق‌العاده رو بررسی می‌کنیم که تمام مراحل تحویل و مدیریت رو براتون به صورت خودکار انجام میده و از تمام پنل ها پشتیبانی میکنه.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت توی قرعه‌کشی فرصت دارید. (شرایطش هم خیلی راحته؛ فقط کافیه زیر همین ویدیو برامون کامنت بذارید).
#آموزش
#فیلترشکن
#ربات
#فروش
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMPxqhupQxrhvCPrpGAKgvq-PtIn3Yy9N4A0RQxBRHRaSQmWjrSPq8q581s_4QCfNC45IOuiZPpX6J_RBMzHJZpINOO8J0hKUW1SgD5yiZtx2AUtn-WMwQPbvEyg9kriQR_RFgd6kH69JdAG8jXRgNGptVRebQ32pkKoebDTK7Yg86N48U3ivHTUNvwVyfRneKXvLKOh9IuIhZuUf_dhIPjjhkyEGisURnQkkYH06rUpyx5s3u9aT7-kap-XfsChjcFPJxmfHQu51vjcYHCnq_kOMEi4hJaGQ75507unmsg57lVH_x2wjtrEewOnurqKog9QLhzdsIQH7vZLoKW0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شناسایی شبکه گسترده افزونه‌های جعلی فایرفاکس برای سرقت رمزارزها
محققان امنیتی شرکت
Socket
شبکه‌ای سازمان‌یافته شامل ده‌ها افزونه مخرب را در مرورگر فایرفاکس شناسایی کرده‌اند که با هدف سرقت کلیدهای خصوصی و عبارت‌های بازیابی (Seed Phrase) کاربران وب ۳ طراحی شده‌اند.
⚙️
روش کار و جزئیات این حمله:
🔹
جعل هویت کیف‌پول‌های معروف:
این افزونه‌ها نام و رابط کاربری ولت‌های معتبری مانند
OKX
،
Rabby Wallet
و
TronLink
را شبیه‌سازی کرده و بلافاصله پس از ورود اطلاعات توسط کاربر، کلید خصوصی را به سرورهای مهاجم ارسال می‌کنند.
🔹
تغییر ماهیت بعد از جلب اعتماد:
تعدادی از این افزونه‌ها ابتدا ماه‌ها در قالب ابزارهای نمایش نتایج زنده فوتبال و بسکتبال، تم تاریک، پسورد منیجر یا وی‌پی‌ان فعالیت می‌کردند و پس از جذب نصب بالا و امتیاز مثبت، با یک آپدیت مخرب به بدافزار سرقت دارایی تبدیل شدند.
🔹
ابعاد کمپین:
کارشناسان موفق به ردگیری ۷۷ شناسه مرتبط شده‌اند که مخرب بودن حداقل ۴۰ مورد آن‌ها به‌طور قطعی تأیید شده است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJnJMU4t9SMog8n9HeqrscrhRVltyhdHbqOmjmFqPvO2c17HG6qJPI6PddSQaStZFSWK8f_Uht5zID8KU4O0-Wkem_91PDzxIeQgxcc9qGb7wMb-ECttPrP6ofJbhuvvVxcBJItIXSyuEAKL0q9QecGTigJUfDVqRFk94XAkAUykeIdpjdUD5-cXMNV-mggUcKmqFwPOhie16yA6iem-WO-RJCPc7NozYpQ9AAzMlHp4cSFsyzGN-Oy-fuImQ5leVG0gi_YzdRXmxG4X4rlzRxVo8ygGgOowEtUUM-7BwnG091fAMoRItB2xHas1g8WGzWm5MdFb0Enhx4d8DZjoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
لطفاً برای هر ایده ساده، اسکریپت جدید نزنید!
✍🏻
دم همه‌ی دوستانی که توی این یک سال اخیر با کمک AI اسکریپت‌های کاربردی نوشتن و به بقیه کمک کردن گرم. ولی یکی دو تا نکته هست که باید بهش دقت کنیم:
۱.
فورک‌های بی‌مورد:
لازم نیست هر فیچری که حس می‌کنید یه پروژه کم داره رو سریع فورک کنید، بهش اضافه کنید و با یه اسم جدید بدید بیرون! با این کار فقط کامیونیتی تیکه تیکه میشه و کلی ریپوی نیمه‌کاره و بدون پشتیبانی روی گیت‌هاب رها میشه. اگه واقعاً ایده‌تون کاربردی و درسته، بهتره همون رو به صورت Pull Request برای نویسنده‌ی اصلی بفرستید تا روی سورس اصلی مرج بشه.
۲.
تمرکز روی نیاز واقعی، نه هر ایده‌ای:
لازم نیست هر چیزی که به ذهن می‌رسه رو با عجله کد بزنیم و فکر کنیم حتماً به درد همه می‌خوره! مثلاً واقعاً نیازی نیست برای یه دستور ساده‌ی Iptables بیایم اسکریپت نصب آسان بنویسیم.
۳.
مسئولیت نگهداری و امنیت:
ساختن اسکریپت با هوش مصنوعی شاید با چندتا پرامپت ۵ دقیقه زمان ببره، ولی پشتیبانی، رفع باگ‌ها و حفظ امنیتش کار راحتی نیست.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭕️
طرح جدید «نظام‌بخشی فضای مجازی»؛ از جریمه ۱۰ درصدی درآمد تا لغو مجوز پلتفرم‌ها
پیش‌نویس سند «طرح نظام‌بخشی فضای مجازی» با هدف تفکیک وظایف تنظیم‌گری، تعیین مجازات برای پلتفرم‌ها و تعریف حقوق کاربران نهایی شده است.
🔹
تفکیک وظایف تنظیم‌گری میان نهادها:
مدیریت اینترنت، کلاود و دیتاسنترها به وزارت ارتباطات؛ پرداخت‌ها به بانک مرکزی؛ ضد انحصار به شورای رقابت؛ صوت و تصویر فراگیر به ساترا؛ و اخلاق و ایمنی الگوریتم‌ها به سازمان ملی هوش مصنوعی سپرده می‌شود.
🔹
ضمانت اجراها و مجازات‌های سنگین:
شامل اخطار، انتشار عمومی تخلف، محرومیت ۱ تا ۳ ساله از تسهیلات،
جریمه نقدی ۱ تا ۱۰ درصد از درآمد سالانه
، تعلیق و در نهایت لغو کامل مجوز فعالیت.
🔹
مهم‌ترین مصادیق تخلف پلتفرم‌ها:
نقض حقوق کاربران، رفتارهای ضد رقابتی، عدم احراز هویت معتبر کاربران پیش از ارائه خدمات، خودداری از ارائه اطلاعات به تنظیم‌گر و عدم رعایت مصوبات قانونی.
🔹
به‌رسمیت شناختن حقوق کاربران:
تاکید بر «حق دسترسی به شبکه»، ممنوعیت قطع یا دستکاری ترافیک بر اساس اصل «بی‌طرفی شبکه (Net Neutrality)» و رعایت رده‌بندی سنی و حقوق کودکان.
🔹
سامانه حکمرانی مشارکتی:
الزام به انتشار پیش‌نویس مصوبات ۲ هفته پیش از تصویب جهت نظرخواهی عمومی از مردم و کارشناسان در یک سامانه هوشمند./
مقاله کامل
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzqlXfqxDbV5eow5YHHIOToIwuUgbPbvh5EyOe_eP9ABvV1dO6t2BBlVMHKzIJzgLLwHqa6cZpUQwLEQWOkeZuDhpO0XrAXNfUvvt5A2S5btu2Nvudub1WQ57hX9wWJGqBIrDthtnvGqucCwkukfairbaEhK-e646HkvW-qwoIakSvARwoM95G4_kDU_e90uSihhDo4A5lB6P1iCS4Cbmq2cE2Qkm0d85Z5UA0YM1lzXCaOqWitahzjz87jW0v0nykJpnO8KL5pOGf-fXLMyXdzfjvz1vcg1qrKAH1tCKRJHh5HCfgDNML-Ry6jdlJJgwQ0ArLbw7YISQhcgP6al_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی تانل سبک و بهینه Netlink Tunnel
پروژه
Netlink Tunnel
یک ابزار تانلینگ سبک، بهینه و کاربردی است که امکان مدیریت کامل و سریع تمام اتصالات را از طریق خط فرمان (CLI) فراهم می‌کند.
🔹
تشخیص قطعی و پایداری بالاتر:
واکنش سریع‌تر سیستم در شناسایی قطع ارتباط و اعمال Reconnect خودکار.
🔹
مانیتورینگ و آمار ترافیک Live:
نمایش لحظه‌ای حجم دانلود، آپلود و مجموع ترافیک مصرفی.
🔹
گزینه Optimize:
ابزار اختصاصی بهینه‌سازی پارامترها و تنظیمات شبکه.
🔹
پشتیبانی از پروتکل‌های متنوع شامل TCP، TCP Mux، حالت‌های مخفی‌ساز TCP Stealth و TCP PCK
🔹
پشتیبانی از اتصالات وب‌سوکت WS / WS Mux و WSS / WSS Mux
🔹
انتقال پایدار روی بستر UDP + FEC (تصحیح خطای رو به جلو)
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0kaMZEKHB_ErIk_9g7J-yU-dj4Iwi-2hwkEtR8IdQRplOtLf6373JaPKSPmwG_KDvQ-SYW53rQ1vIa6fLmZbT8Hu1MkJrYat1NlY7EC5pxgpCLZryqFAzSOz54qF8Nf4hmTcB2OUpnFJzzgt0WgIFKuEn6hGIesbywleq_8Wn-PP3MxJo9HZkNfyh367MNmJlVBp_sCF9OoJNlOuVEz6K6D3NKEGG94pd8CAji8q4auXsVWCr1RCY0BcE6ecYEr8RHYooHzBSbrkVQZbhKt5RPSM1jNYjLFE3qpJlZQ1fwmLvbBPgkwgPtAvcIuSUnwl0EONkyJ6EpBYDUmUF1kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔐
معرفی DayLock؛ گاوصندوق دیجیتال و ‌امن
پروژه متن‌باز DayLock یک سرویس اشتراک‌گذاری پیام و فایل بر پایه معماری «دانش صفر» (Zero-Knowledge) است؛ یعنی سرور هیچ دسترسی یا کلیدی برای خواندن اطلاعات شما ندارد!
🔹
رمزنگاری سمت کاربر:
تمام داده‌ها مستقیماً در مرورگر شما رمزنگاری می‌شوند و سرور فقط کدهای نامفهوم را ذخیره می‌کند.
🔹
پنهان‌نگاری پیشرفته:
مخفی کردن امن فایل‌ها و متن‌های حساس داخل تصاویر (PNG) یا فایل‌های صوتی.
🔹
رمز فریب‌دهنده (Decoy):
امکان ایجاد یک گاوصندوق جعلی برای مواقعی که تحت فشار مجبور به باز کردن فایل‌هایتان می‌شوید.
🔹
قفل‌های هوشمند:
محدود کردن دسترسی بر اساس کشور (Geo-Lock)، شبکه اینترنت (ASN) یا تنظیم زمان مشخص برای باز شدن پیام (Time-Lock).
🔹
تخریب خودکار:
قابلیت حذف برای همیشه پس از اولین بازدید (Burn-on-Read) یا پاک‌سازی خودکار در صورت عدم فعالیت (سوئیچ مرد مرده).
🔗
لینک بررسی و نصب در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIuQFw9UuHR9I96GFziY23WnU091Y8-VQSDO3V38wjzIVbf3qVFX54E9FyY4FzVV7nfr2D5YAOLw-rYaqWzfDRExLDgLRiTqbH3NTrycHdVDSUo-rVslHf6njybUiL6pFCdRlrNH_9QzgCfKXudX5RuroQgPzIlVbuV4bNvnwsV1XNbr8yghTdZT3eQmc0zliJtQSLlcTg23KQC2fv4LiU6lzRYOZaQCAptTvFGMQuV74uXqujuiQiO6a5BfGsOVF31ckdve5G2wlkCzSfJsVAgMXKlNGO_ejc2GDw5WRbn7GNOFYeAuTCsu0B8NyvpD3i-7NfGnzC-QZV4CAJHtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRoz2X2T8Ae2mrw6q6Eak42MrXG772ZhVbQqSE3FB0pTW9SGEdfWLBgIM4QLFb-Cxpc2LkFRlqOhFcOJcHDfm1m4G1zAFjczhuMphZycuIO0MCIlMoqownMM4DYa7cQeXzLXjrakcINSTdTCsakAftyQEUfIbBan3tTTMmX3yOUKKz2n8yR8HfEPoug5ZpNc29kI5c7hh_TPA_x3wX5nVaC7UlMhu_pgutiuoeAyaKiP2YQBXTgJB-e9KVTXA1a7qYH5qxcTx7VdR4J-iNGyWmkWzh7UjuvMsaERayPfv1bWTMjrNbfcAzCuDcJ7r3esT3g5ARNK3UZ9ymRHKu3LmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
آپدیت بزرگ ۱۳ سالگی تلگرام منتشر شد؛ از فایل‌های درون‌متنی تا پیام‌های خوشامدگویی اختصاصی
تلگرام هم‌زمان با سیزدهمین سالگرد فعالیت خود، آپدیت جدیدی را همراه با قابلیت‌های کاربردی برای کاربران، مدیران کانال‌ها و توسعه‌دهندگان بات‌ها معرفی کرد.
🔹
پیام‌های خوشامدگویی:
مدیران گروه‌ها و کانال‌ها اکنون می‌توانند بسته‌های خوشامدگویی شامل متن، عکس، ویدیو و جداول بسازند که تنها برای کاربر تازه‌وارد نمایش داده می‌شود.
🔹
دکمه‌های تعاملی درون پیام‌ها:
با به‌روزرسانی
Bot API 10.3
، توسعه‌دهندگان می‌توانند دکمه‌های کنترلی تعاملی را مستقیماً داخل پیام‌ها قرار دهند و امکان اجرای بازی‌ها (مانند شطرنج)، آزمون‌ها، نظرسنجی‌ها و سفارش کالا را به‌صورت زنده فراهم کنند.
🔹
قراردادن فایل داخل متن:
ویرایشگر پیشرفته متن اکنون امکان گنجاندن فایل‌ها و آهنگ‌ها را درون بخش‌های مختلف نوشته فراهم کرده است (با نوشتن بیش از سه خط متن فعال می‌شود).
🔹
افزودن امضا و پیام به هدایا (Gifts):
هنگام خرید هدایای کمیاب (Collectible) با استفاده از Telegram Stars، می‌توان امضا و متن شخصی دلخواه را به هدیه پیوست کرد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🛑
یه اشتباه خیلی رایج و خطرناک: «هر اسکریپتی که اوپن‌سورسه امنه!»
سلام دوستان عزیز
✋
همون‌طور که می‌دونید، هدف اصلی این کانال معرفی اسکریپت‌ها و ابزارهای اوپن‌سورس برای دور زدن فیلترینگه. اما یه سوءتفاهم خیلی بزرگ و خطرناک بین کاربرا وجود داره که وظیفه خودم دونستم حتماً در موردش باهاتون صحبت کنم.
خیلیا فکر می‌کنن چون یه برنامه «اوپن‌سورس» هست، پس قطعاً هیچ بدافزاری توش نیست و ۱۰۰٪ امنه. اما واقعیت اصلاً این نیست!
متن‌باز بودن فقط معنیش اینه که کدهای اون برنامه برای همه قابل دیدنه.
این ویژگی به خودیِ خود امنیت رو تضمین نمی‌کنه؛
بلکه امنیت زمانی وجود داره که متخصص‌ها، اون کدها رو خط‌به‌خط بررسی کنن. اگر کسی کدها رو نخونه، یه بدافزار خیلی راحت می‌تونه جلوی چشم همه تو همون کدهای اوپن‌سورس قایم بشه.
من خودم همیشه قبل از اینکه اسکریپتی رو معرفی کنم، تمام تلاشم رو می‌کنم تا در حد توانم و با کمک هوش مصنوعی، کدها رو بررسی کنم تا مورد مخربی توشون نباشه. اما یه مشکل بزرگ وجود داره:
👈🏻
اسکریپت‌ها مدام آپدیت میشن!
🔹
یه اسکریپت ممکنه بعد از اینکه تو کانال معرفی شد، تو همون چند هفته اول ده‌ها آپدیت جدید بده. بررسی تک‌تک این آپدیت‌ها برای منِ نوعی واقعاً غیرممکنه. این یعنی ممکنه اسکریپتی که ماه پیش کاملاً امن بوده، تو آپدیت امروزش حاوی کدهای مخرب باشه (حالا یا عمدی توسط خود سازنده یا به خاطر هک شدن اکانتش و...).
💡
خب راه‌حل چیه؟ چطور امن بمونیم؟
۱.
هیجانی آپدیت نکنید:
هیچ‌وقت به محض اینکه سازنده یه آپدیت جدید داد، سریع نرید اسکریپتتون رو آپدیت کنید! حداقل چند روزی صبر کنید. اگر تو آپدیت جدید بدافزاری باشه، معمولاً بقیه برنامه‌نویس‌ها زود متوجه میشن و گزارش میدن.
۲.
استفاده از نسخه‌های تست‌شده:
سعی کنید از همون نسخه‌ای (Release) استفاده کنید که روز اول تو کانال معرفی کردم و داره کار می‌کنه. تا وقتی اسکریپت فعلی‌تون بدون مشکل وصل میشه، لزومی به آپدیت کردن مداوم نیست.
۳.
به اعتبار پروژه دقت کنید:
پروژه‌هایی که تو گیت‌هاب ستاره (Star) بالایی دارن و افراد زیادی اون‌ها رو فورک (Fork) کردن، معمولاً بیشتر زیر ذره‌بین متخصص‌ها هستن و امنیتشون از اسکریپت‌های ناشناس بیشتره.
۴.
گزارش موارد مشکوک:
اگر خودتون برنامه‌نویسی بلدین و کدهای آپدیت‌های جدید رو نگاه می‌کنید، اگر مورد مشکوکی تو آپدیتی دیدید، ممنون میشم به ربات ما پیام بدید.
در نهایت فراموش نکنید همیشه حواستون جمع باشه و به هیچ ابزاری، حتی اوپن‌سورس، چشم‌بسته اعتماد نکنید.
🛡
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz8TRPw7jijSpIdAnjwXhsNpTPtFJvs3PrspybeQLOZEIX1Wdg1Wo76daxAoqY9EEiw3Wpkl8jtnRYYQBGzUiRVaH2SX12Qql_dJFmF4yRNycUJ0IFJ0PvvXJsxdxK5GnDXdHVZDGu0kMIk0EIBrH56pVW1cUKbBnDlQ5vhIkB9NWsjy17iGA7yzSUh7jz3cpHNHChnmWaXKfDBUdHDxmRs4ctQB3FOB-IEQFNLHrjfhqe-dlMbhWafi7ExXeUVsSVvgXoExSrDQUZC7BLqYtV37jm_6BgrqC03aD_rPJ9ZDF8-8763WRIUyV-wm8rpbtB_RKVwLyfe2u2PAtExFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگه سوال مالی داشتید میتونید از آرش بپرسید بچه ها :)</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2922" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLsXDcfWxfdeAJ2Ve36PqZN7PsDF6lBj54ooe1Y_sw7suiVK0xnE5KMHlMNn8Du2u-eE02zfK5HI23ImwpgyrbWZeAUL4KLoYd8cIzpoMhPZxVQUHEVy1qA9Pu1KkdVE4RspzxbV2nerf9l1GSfPIXZiDXSiYZdHELQhVq2aOnPYyAhW-aYvv9d0IZvdKXAaux9NpOgCaogRj-jVSit1uyq45i6LehEgXpYDHs1Phs3xYn2UlOmcLUBB9Lei22KMYXuN51cnEp1hUL6Wt24hs_bXrvpCqxnB_Jt5wwHNHcshq8VNwJmCoXfLrARvRSRd9XQh-9DmD92l5fNqdH1wkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
وضعیت اینترنت این هفته
🔹
بر اساس داده‌های Cloudflare Radar، ترافیک بین‌الملل ایران همچنان حدود ۵۹٪ سطح عادی پیش از قطعی است. برخی مناطق مثل مازندران، کرمان و آذربایجان‌غربی افت محسوس‌تری داشته‌اند.
🔸
اگر این هفته با کندی یا قطعی مواجه بودید، تنها شما نیستید.
منبع: توییتر سایفون
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2921" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
