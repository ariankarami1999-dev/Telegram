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
<img src="https://cdn4.telesco.pe/file/TXHD1TOUds_jFF2POIPeWL_RzrBLbX7TValMttmsIxydIWL3PFX8YM0a0NHt0I6rrbfC_LaXrUSo2fvsvsssTLM60k5t3oyoipB6NIJpYtkQOUOUm3mEqPEaza0oOrnsLzV5e_6u9iOEiWh8wNsLWmmuYqvdVRHg9kX7zGz8t2fLdRFt3SI-DnfVITRfJbRkKf606TOs2MQ7JxlNtoRhjuJWE2d-VzGO0VSB4W1nONpgDSoArhOCNeDArkQg9-GUzxzh1SVXmkQn-JwKltdSWBhMwQiP8hhqUOwN2qQ-PBkxdfjYI4tQx9WbCjbKgu6AL7iUbwYTGUIsWpTETOq7_g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 iAghapour | Digital Freedom🎯</h1>
<p>@iaghapour • 👥 51.9K عضو</p>
<a href="https://t.me/iaghapour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اینجا علاوه بر ویدیوهای یوتیوب، لینک‌های تکمیلی، فایل‌های مورد نیاز و اخبار مهمی که در یوتیوب گفته نمیشه رو به اشتراک میذاریم.💚⭐️فراموش نکنید کانال یوتیوب ما را هم دنبال کنید:http://youtube.com/@iaghapour📞تماس با ما | Contact US@iaghapourbot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 01:51:16</div>
<hr>

<div class="tg-post" id="msg-2961">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙢 𝙢 𝙙</strong></div>
<div class="tg-text">✔️
PARS PANEL | انتخاب حرفه‌ای
✔️
🔝
پارس پنل؛ مجموعه‌ای که
تمام نیازهای شما برای فروش
رو با
آپ‌تایم بالا،سرویس پایدار و امکانات کامل
تأمین می‌کنه.
🧨
نیاز به توضیحات بیشتر نیست!
👀
🤖
ربات رو استارت کن و تست پنل رایگان دریافت کن.
🔵
❤️‍🔥
اول تست کن، بعد تصمیم بگیر
‼️
https://t.me/panelparsbot?start=6352682229</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/iaghapour/2961" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2960">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VHbQrK3mChwVb6LDFrtah-NHDcv0He25FxtBo7YcCI5EzqFJ6nOqCccVdDsAMJnyntDGrVyvY2dd1M6efh2zD3CBaAhsIHi5M97I8rvLXZ3VtdYTuQCCvQit7iqUbT9cFUSkTrnb_oZOW2FWDoMJkY1AietQkc9krlkWeMpF81ICIb15OsfgYytndHB8rE4hjGquG31IanlXWQ9bpvK37kYFuaTwDw5aEEMC75LxsLWGueWjHfKldRpfZhUkEKMHy4TrVv3aVkra-XhdH9pCl4YU1eR0PUbVZu7vn-tZeH_qCBVMMLfSHXq6lDKM7zXKzxUElAr07KSJIu_J_0J7LA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/iaghapour/2960" target="_blank">📅 20:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2959">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4sYvhS-rg4Vq9VMQVFMWS-dksKOQ9LIvHmbvjhPWR_BarZPM1oJiwKstgQNA-BkSqxisGHdt_IXwfzmvyuntnTrxs1Pu_Ptfey9HvU8IZZHHQsqWhJ4vMtftj5-sXbs8GKeFNmDVIhuuFAnDQRg40w9zr6RmmVZDa7jFz94sFcP66BWbb9wYVuCwBpamfHwsqVhUAcoCEokJc3_kaEQbsQM5FNfsFsbOKU72s5XeOoItNqr8rsLq0XZP8XJ2aNsn_yyPPDFflQRuVfLnAXK4BwzXSon_CXLXObftp3375S7c_qZs9_qyOLcfmdk_3UObXyHdS6Ee6s_6XnOGnwwuw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/iaghapour/2959" target="_blank">📅 20:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2958">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/iaghapour/2958" target="_blank">📅 18:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2957">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تو گوشیم فقط چراغ قوه بدون فیلترشکن باز میشه :)</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/iaghapour/2957" target="_blank">📅 16:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2956">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهاستینگ افزونه نویس</strong></div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/iaghapour/2956" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2955">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grLjm07_lOM1cDFtd4KGGFG-R8SoNM0Fc32qdhcOWe3zN8IHdubaryPRW1VbseaTWEb8TDvAtBnJMfkh_2xLDCl3aeFXYzinB32TlIEuRJvQQBJeyH0s5b7Gxmz6ZpxBxhs54y8N2OoM4Pu8ktjA0ZQWpH7Q53biBmX8fK8BdgRbjhRx1iNCJBfZG1FjRkf9HSNYWSbk7sghIdroO5Vt4_hSuDLUwkX3r-RFLW6Hh_7i2AW0KhDFMUNU3aLR8mkQWakjAAVI_dvPj5gfabzeXj3HEg7elOOR7-t14Bgy_BDTxi3nB1_4QKDX3bn7bv71iJpwfKVsfVl08iwsPAmPqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/iaghapour/2955" target="_blank">📅 18:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2954">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/iaghapour/2954" target="_blank">📅 17:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2952">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SImMBO4qmMLkV1J7vvzAxr30yI6mmSOW0em9fWpa-FHTKw5SwywhUc_soHpWpqX4hYPUqj-ZX5WtqrDyK-t8GMceffRkCrS6vXaXkkDX9gmPtrq3AYwHnD3N_-kFpPDp_OAZrCUkl-loCoyKXyNg6ddJt9rzba-nLMmrMdJ4UfCpvjR7e1U26_TX-G0TVPFNPCqIf1dVcSbI8PPhXZfMkq_vg_WzsB4JR8Yi2QCH-7FpMEyoWF7stTK5n2_18sacojaez9dZ0lDd3NectQ03_TwW4e8Rc1CweN4thzSMrjVlUy08tZpIZdRbofcbigUPsl4b-ldSHmNjWlOmjs99JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل برنده عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آیدی pinkpantheranim عزیز، مبارکتون باشه!
✨
راستی فردا هم یه ویدیوی عالی داریم که تو اونم براتون هدیه در نظر گرفتیم!
🎁
💚</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/iaghapour/2952" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2951">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EudB561HHPSrW-F13O3MFqIsE7RwechAoCr0yXn39n_ci_Fd5cVzfjb1EUkmz_NPTsARTHe54MT5_TlICea0R6sMu5Xhy5WtApsVsdPdTrJItlMPIbHxkLwFK681tX8bhYsvBJyX0s6wqnZ01-ZBrzjAn329IBfgNittiedY-vRUZdowBIfNDKUoY16bVvPzaVEDfXC2WvtYFQ7XYwehj_5pjje6cD-mPggHSOC0pWKI4pqUmFpuQvIxrK9GGiVEjr0bhszwspgeqY3xDsfqLnLzuT2Je_XmdrXPqJ1sJsZPjvSCvGkUoPxqYXsYN1sDtzTFqfvmwjVjnM8PBi7BAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حکومت در حال تهیه لیست IP کاربران و در قدم اول مشتریان دیتاسنتر ها است.
در این طرح شماره موبایل + شماره ملی + آی پی به هم وصل می‌شوند و بدون ثبت آی پی در سامانه شاهکار دسترسی به اینترنت ممکن نیست!
نقض حریم خصوصی کاربران و حق ناشناس ماندن در اینترنت با قدرت در حال اجراست.
©️
Saeed Souzangar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2951" target="_blank">📅 17:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2949">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnjxSMTrPXe7PJc-b02YD6E7G_5GLzLhq109PtYANFQLfV4cn0iHqQFZWyfhvtwUEUvNoeNOnEI7l9nhhaZc7Sx2yWiF41K63wgP-7KgypoD4WhZXihaIHizEmIu9HLKvXxMFIlxpo_f6S0_gGzEWQ2imSa0zvbTDbiZpAX7_0Wy0WZWKzuqGcBxX7Fzj6DTThzj6CDygAi86yVyHT7BEIpo1pqsF5drhsghy9hq9GmMwxhxbuuREHOMm2sWNqYHTakgGAjy_aC93RVvrhP3R2Tj9nc7oX2JN5VB0aKHUBoUu_qqnWv9CPH8ggr_-2RwPNHUIqDaN67mgeBTyHH_Hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/iaghapour/2949" target="_blank">📅 21:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2948">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4lOcAQXP-8Lj1PQMFD7eELdSQwnLk85ikjeCgNyBopOF1Ihl3UFOGf_0xI_Bvj8ECL5OPxcKOVd0dIcB3tvapenq2okNJWvoOcKX3LAm2NtnpZxJtogv016R49Bx4vYMC3WbRdOnJ-GrYR6mJBQMnIP9KJdxg0M5VbI891RQN1L9IDTPPlhymwIGmwqew8IjIBN9jgy92yNf1-S5xHL4NnaHJxZY8Wl2cHMik7OoK97eowW26Mdhew8JQ4Hw137VQYwce0Foez1rMl0tqbk7Xl99YJogbiUZDBmvPCoO2V54FIhJ0v4UlgGZJOnRQIYvHecXK9MIfX14hgaKVazLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/iaghapour/2948" target="_blank">📅 19:46 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2947">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/iaghapour/2947" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2945">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=ah7xIb-0SLkfFkPGkMm_J5Vp5Z7jJ3tsbGSi7Z_ugaEKmil_lcqvwlR39gI7mPceI5aMb-vnDvPVgO70xloUtvs4QwXaJ24DRnhyubNiOxFLuRNBShdLDzfPnNDEy8VwUjVAH0oFqqL2byMoITzKVkfmseUK5LO916Yr50oP-OQiWIzYFvMoa2vu4ckalfZ9jiidar2CAcMXPA_uiOhumRtAK3ve0eVQ85KrIZLjkXh7AZXLUR-4AWOKXWjjA_ZssV2_LU64YXmK40EEmCwu-zDJ9o9eKIJNiX8g9TEY5jTVLRllYrOMqQexkdZCSp1Cu6t0U-DkLLRt5eLMc34PsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b35d2aaf3.mp4?token=ah7xIb-0SLkfFkPGkMm_J5Vp5Z7jJ3tsbGSi7Z_ugaEKmil_lcqvwlR39gI7mPceI5aMb-vnDvPVgO70xloUtvs4QwXaJ24DRnhyubNiOxFLuRNBShdLDzfPnNDEy8VwUjVAH0oFqqL2byMoITzKVkfmseUK5LO916Yr50oP-OQiWIzYFvMoa2vu4ckalfZ9jiidar2CAcMXPA_uiOhumRtAK3ve0eVQ85KrIZLjkXh7AZXLUR-4AWOKXWjjA_ZssV2_LU64YXmK40EEmCwu-zDJ9o9eKIJNiX8g9TEY5jTVLRllYrOMqQexkdZCSp1Cu6t0U-DkLLRt5eLMc34PsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/iaghapour/2945" target="_blank">📅 20:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2944">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/iaghapour/2944" target="_blank">📅 19:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2943">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csNJfC__hnCL4YjgjY5z7r60VG2yHCKTQdp2TgnrIXGur3RvUaCL8dG34tx-18ZQeLIstTiXtgDjBgqd6HasfEBZjHE8CV8cTZPnzd78T--Y2Ck2dStqoMgo07kUultPAiYPPi_bbDTzSuMNpJuGyT3m4NRSTBsh9ShenC5NE6H2QrvuVQ5SGhjRbTahnTcdgvjcAfyK-3lVDdJluAsdrqmg9-lvBKA_7mla26RcPSCQwCxcwyoRUjTqGp7J0E4OpnSQU9hiYvyhIAd4HMpJG2Je0gct9bwcSqPzHifQOUW__16tzxF1weNtw2TxHVZPXM3yq4SOXe4CsOulAt9jGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/iaghapour/2943" target="_blank">📅 18:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2942">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tl8B10W21RNhX6-hQFBYU4LJGn_wQJG0ZMFVC0ZYYHEloBg5a99qLzYARPOKiBhbayDIscAx3Hxc2PzHoQ1CG3Nn8gSn0mkwVfuXEAKRQB3QN4y_TYItu_EGiJD7qm8cn1sSXzuC74bEzAAd7IK0gUNQiGQyBs1he6tOUakmRNhRjBSMa8Yqr4qnNWhgZbFiqsNdXr8ay1jNLcKy5KKQ_gaZ3OwhstCHPRb7ZPT9kiM4mlbxIaZNmisSOqRHFz74mpUMcHW5NdUP889KxL705xn9YzzKZe8l0xeEsbQMhnjEdrrMHFcfTc-N-OdqIb4GN4dTdlr4YXdhLaVFYfnz6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/iaghapour/2942" target="_blank">📅 18:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2941">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4vtfcFZn4E3ryf9KjobnstENoGT2duCONpYXQK6Wz90iBavXF3BHD37TbFhVZflpOTB9m5MIJF9MRvBu6ZKrLHWA28bMLaKER0IoW6DyKlhOZLnipZ3pk39BO-In8M6_HUCYjwPoNZVzqtwmXiNUfI0u_AMFXQpZ6ZVC4raE4RjUsdfPLyBegoQ4lrXApaFKER0sAlKwC8ce-J50YK9FjtR_QbpcBuqG7qAbIC0IcLsRB7rmOAvG4GWfiBVWIwpiLUptfRtgQ1c8tkvHbMmxo1Cb7XIeeK4e53Ji8hqWNic3lJaj4oszMe-SiaZ3ioWnVMuWsmJoTrGPu3G9VTDpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/iaghapour/2941" target="_blank">📅 16:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2938">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urmkeYETDby-TaBEXwxls3dobIrrrIDN6jy9Juz5ShjrA0KZVi7526ZE2e_hBfiZcsbdvXy99lvfkA3gSAaCPbjUNkLZkAJb8UqGmvzU1zSr8Ks2H8nfLG5oBm-8B4WVm-q7JAj3ch_ketL_92Nb9WpQX9WcA37WOTqpgmGFagsk7tadi0MS-Ijn3YHt99MHwKMdG0DqxNHw0LqjED1w3HUR9KorMsGvJDI6T7Nnp2Hfl3UmvNrNrkj_FWeTPTkSKrjcfgAd3XgWn2IDr3gnwj-CnsKpL4bLA3dz7Nr1_3LzItTet_0WDH7Qu6Kbkum7IEgTQO5HLd2upYsetMmdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6rP1OB8AZkS-85i8TX-9HGRqXEsKj-NZ9AzV-C7lHCcgxPAQVXtoks7UDdU-LxJDyWsJqD72ztOnVR568ByLsuuFRP7iT_eKiWGMge-AKUHdTYHm9CpxuJEXKjucd0TR6Pj3HwyMpL7zcZn9kM7dK0JCfuWwqL9d8Uqj10KVIfp0xRACta40i7uUtSMqO66ACujZ44ImW68t92cglZ26Wz6o0Mpk8BEGUWBwYOkM3w0qoQxYC6DOniNJr2YoapaX18PFgwMwCkxb0hI85YEDSWDYP2GUf_qnPrkKGbV5nG9jSIKSRlQvR01UVUd7HxDAQk_6LDLWFsAHuFUGKXBhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/2938" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2937">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgTaZq-UjitQQUKuD4-6bg-1jrZtKfyXO_qsxKtvOlT9XrpFXIHEGrbSV0tolG3RqygnpwjcQb5upDxZZgppa66OqN7CZzUCxZuuuaukkoxvVwZWWF2V0PEaw7zUgLWHRHQwjYc5bSs7awBCFJhzHvWTkCBYm24_1_WJUI7-8bkWhm2t9qmSuvUczn47gWrkEBH5UBvztFKYd0nOpt27DPdgRsMrCl6dYSVoxnaa6WmvD0_12qsucTgHTCQrZrsQkceD1L-_NEGdyMuGMR9mKvIFdlJkjb4Sy40SjRswzYCU9gXmV-Uv34lpOa5BpAV5Bz0a6lwlU9G8ZDSEbmUv7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/iaghapour/2937" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2936">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L46rhDdpDC9tG_wVdXkSHwfV2nN9bRYmQ44Az79qBXOIq0xdu-wF1yFqtViNbCMGLdbjeqc7ed966Cxnqc8aTwIe4ifAU6VQQAMD753J5q5zNOhTPVMQYa9aUL-yOjy-aaN5nAsm26LDHkOrV-CsZ9659anGSnfGH28dRSE_aT49kpXbkde7_DJgzBuyDwzKgO1486CZI_PD6mjybTeVgLPOEy5owYNASCjz53JcMyfQ9lM3BGJuRUljWXkbLDgXRh3HwdWrspvwmHpGyycajtliKu-E-VGAlJG9iZDns5le74wTaNRRJQQ0pLO5qz6Q_Z8vskTvtBzsl5jaOOhyTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2936" target="_blank">📅 14:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2934">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hE2XSrJvOrV9il-5CfLWAcMGiFhV4zWqeddb_F01ZZuqd7RtHNzmzzJ_ttVYZajijWMa56VBbs45W0bAApjs7jK7n2kemb23HWtTgP-jkDh-ccesym1b_QdhjAUg4yhIK1QFXRv54iROEqn8MNX7chrqwws6QOW-3BBCMRc9jjU7udsjbdvX9wtLgxW7rc3xVjyIoVh9Iyn--fUUdBV-srxV8dEKDHGi3UuEkG36sr5ZYK5FnaLq_7m6QKeG8kJ8mUJIB2j3pPDEwSzS2HP2Cyci29g_w8kDrwIlCYAtPlzXiPOgNBxZ19_p0siqGRIhZHdjSa2vNdQo68p4HTuBbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/iaghapour/2934" target="_blank">📅 18:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2933">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptmhD_FkEHjkkeORZym51wwoLcHYwqrludwb0vf_TaMBMNsNCqk9XAVhySafnRDMYkEQXq2dsctqiiwQlDaESvclNE_1cUr--tuSJ31K7MvynQ_BAY6mUQTDuHnGLSetc--zMXrLmbyzAza_xRZORtEC4tN1Jaz8b4vpWSrHFsCc48epwMCF_urabx0cKTOC-o-A37EFAqbWu79nG0AgtV3Ta6rFX3p-Rt8OHv94A-7D7qc55L_713GWTeLJYrWKnwp9iSvvCWVjxSMvBQpbp1pF0w9wdm_o8HzlUyuVW-5efBSFRZ0Z-8sbepWISdGvlIRDJexkZsqhha4VSsBD7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/iaghapour/2933" target="_blank">📅 15:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2931">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QARaPVQcJauzN9BVfYe5hZQlK9riw1Rl7qgl53RMV65JNr-j1HzBxoTHN7OGjMkFYUKRTSG_IGPBNAnkXwH_qdXF4qAl8Fu4jWoPOX6YMcgAR4lPAhV5U1PejKrhaBB0s1LeRVzJfHYY61MRtWRCqBoXBl5kmv_gVLVV9C4H9ngW59LWKiP3GWq0_X2fvlRWH-wwtVXluSm0fwmoYpjVZ9eX-0H50K0GiMb_5cp9TXegThz74LKvfjAqSxZftUjJDsNO9tz2v7L8DIBXuKbIWHVc-eiuck5Ww2j6HR67FIyGmq_6wxrJjuZfUv4SSJejTCNRU7N9nRmIPN4rTNlGNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/iaghapour/2931" target="_blank">📅 20:56 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2930">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/iaghapour/2930" target="_blank">📅 20:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2929">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aoLMxEcrZcnHHOeNymdUs7CIFQXSMcwiFKgQbFD7kA3hNy0xTaf5CYqktkOcpDh1wdW6bGYcz0CwJEtlnHLxXybv4LyTMHL11a9m0f1UE1vzkctiZXzj_jrN8NpQ47ji2eQCHrvglW0kjQ8sokbwA5RN4AxPZFqVFNzrI628SmGkWF6PCbv6UA1C9AmwuQHR_X8XCoPyhFzki2vFmpnsZO5GxzktLdkYhm9C9chsqWFxVsAzst09jiLhP9mtB2af8YPlTeg32s7uQimgpepeuiVoXIVR31wnMGHEBtqudFhljH44RtoRjtNQKl55cprEGt6oqVB6-16vZ07JLp1MjA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/iaghapour/2929" target="_blank">📅 14:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2927">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiQvX-H22M7tHXFBh3PLIJXwFcrtpm564H58PyeG_iA1m0Pw6_UIQIIESYlb2p8isckaMlf7iYF3vlrdyT4zaQAG2TwpLqhJZq0lS-m_iaBLfufFSvCnqk6EPU7uGFOodI-1K5I-xOJ3_9F1OmYwZcQ7L8O4rBgtE-ur0mM34FColYEi4esSMHH3Cml__RTQnZaod3zuOkIi5FXq9imSCobo_wm-4e3hvJCUAoRQxi3jx7lEt6dUwUsS34Db0u6ar3ahqVlQf89VSkrksGdWNJcYEfK_EPXCfWiIbYDlB2vE8zbsQhTZNKOOujJZ7K6uZdM2I0fibM6ijP1sSCEw4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2927" target="_blank">📅 20:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2926">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpKSZHyMEcKNkJPAHrb3W5KmKSMnx_RrceKkHpPQ30FICdVyA0gAlEskw2fUb3RgY3rq4_rAJqeiUOZcSI0VSGF-oVS0hgR6B1XRkzzou8MjxFDzTV9s3WUoNMVXdFJWRfZgn69fOwSCqvAT2bbeGWl7y9nUxkk_a7wGeSaDqyVCT7E8QM6BxqpKlmAFZk6MDOGnsHoV-Hk4rQmxj6WbgUMmFOjtfSuqPN0em0dJNKPF4l2N1RrCI8FTskR_-3VrA3YqtkPwE2gfQFk3rwSCUy03iEpoqxvAbM7XyNd4It5a7VEBGIC84tJxkLwrbgYwXhHXuMP0kOjqysRzxoR7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رفتار آدم های معمولی با هوش مصنوعی
در مقابل
رفتار برنامه نویس ها با هوش مصنوعی :)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/iaghapour/2926" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2925">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgMV-FTuZK5RkW20nRKSBztSOfgGsmE07pw1Kk-a2pcYcS1LK56oqCg0gtZH9PuX9jT6h4MSXQVt2xGdZVRvWBExrAs9qPpWGFM4hDVzTQaIIL8B8OMK7v4lT6R1YS4JmNvlqbVZOpZI7tR0MxbCzRutAb23Sezg5Vw9EudRBKEnjgcVfuXuJSIDufnNMPzMm8KDvm_oQnzxQg4VYzi89q906KWGHOdpRpzHqZ1adrMrvVUc1rhroJFY1TksBIZE5KhzVY4XNWWhLkwnfXPSdNEImG2YJerOkxebzm4ejc_rb6UyC3yob5EFwuzLprDkCjNwlI0VTtakOIHbnl84uA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/iaghapour/2925" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2923">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2923" target="_blank">📅 20:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2922">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCe6Y1y5pYArD0MzmfkbBtfefwFBpFRETnS_WrKz3w-2V6PlIpluiWA-4XOIuEd_OJcjByPmUmihpXKEjV9DrRtTd90vXQGj63Wh8BLX5hQv9eyPKghNzGyxe_kd2l45YFhLPEt3cl9NyoN3lDYd7uF5dwS2ACtTd8h7i5KMAM69ZBcL3kLMWOCF1ZMCDNMisoGcR-i-kUCJ03g3rOGdIuegfST84UHO3byCpd0Zs-nQG5FuJtzgj3rs1Cvdv9gsDjH-0iAp9ebMfC2csxz_WAJIfnXXRqPBlBzuR4Kw1e-3XpDLAjX59WdtVqGNTRZPwP_aYZlywJzmXMsrlKlFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگه سوال مالی داشتید میتونید از آرش بپرسید بچه ها :)</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/iaghapour/2922" target="_blank">📅 19:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2921">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJT__ckTnf5R-4k1Ucyv37YhxTIZsXiWY7TV8gJ_6dToYQbJi5GjTkQIELfJuto0dj29Ac758m5UDcTai5o7FnqsAY6lRPpZu0ZwLFDRKdO4i1qYENUbW5V0MINK4CteD3qix2WBERxduWak02Vcdrvby2FPh3n6LnzmY5NcP2LhhbQ-08heynI84WOYuDtmQmPhwiVwagGcjSVwahmXRCugnohV2jktTdPjoEFmY5VGmBxIUT8s0Hs-uafeVNiBF64Bm4vfUAsyV4Xu_EXD0ev1YtwoZCaz0KugWgJZyTgLPq6zCL7st5tMtoKjJGtkoLzMN6a0VS1SDZTR5RO9XA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2921" target="_blank">📅 18:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2920">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQR8MO-DIlZ-Oj40qro5OirhgPrLWY7veR9npHMpKUNEfXi7gxKu0N2GnbBV1kMeSEbsTPWROm03y77Ig1mVXjTUJDcHPGa16ZS_1ix0XuiexwAdncR4cHceH9qGceFMShTCSmTbtl3ydo4BRr2W_0aMFDP2wGzR3nthtIVxP-hxOE-taLkFBc-mSD2TwvO4PG75eTleEIUUWt0C9ju7K8LuX33UzS60FxQTcmrKzjM76qXbnraqt2ehh76E2fIaNTC70eDt4Kdw3gZmnUK10uN9FIA2JOIqAWF3l74Jqcr-U3BR0TN6EmJkBlZrGpIUo8gUzi1o_ecp0G8ex1U34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ساخت پنل و شروع فروش در ۱۰ ثانیه! (معرفی ربات پنل‌ساز)
🔹
تو این ویدیو یک ربات پنل‌ساز رو بهتون معرفی می‌کنم که بدون نیاز به هیچ تخصصی، فقط با زدن ۲ تا دکمه می‌تونید پنل اختصاصی خودتون رو تحویل بگیرید و بلافاصله کارتون رو شروع کنید.
🔸
این ویدیو یه پیشنهاد عالیه برای دوستانی که پیام می‌دادن به خاطر شرایط خاص یا مشکلات جسمی دنبال یه راه درآمدزایی هستن.(می‌تونید ربات رو ۲ روز تست کنید و بعد از تحقیق و صحبت با پشتیبانی، کار خودتون رو استارت بزنید).
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#پنل
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2920" target="_blank">📅 18:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2919">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=DbKRXzTIY8n5ZjSrMW1NCBOhOXbnbAhF2awkLMsDSnFsy7BEaw8z_W8HmBoG-ekYL45FL3NHMzLU3TuZzpO8Rq7gkVO81wIv3IHLM_LOMzGr85WN753zo06BrRnDhwVKQ4NdctCIGkchrV6Z4IYmpe0SZJjohu59yHqZHvzY8b6L5NV_eoQZjw05NiqOoCNWBInhYEKJPZWbDKL5aPADWOU2BtYwx6EDPaWomE1I1AR66uNcn688W3b3Tz4cwL5MZ_HYqvIxRf45svlYNvJF33x4ZyuPjbHzWiV7a7jXfWQqPtJW4KeRZF8zaSKVxwtKPOq8sUAWRnF7x1mDHBWe2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ab5fc23.mp4?token=DbKRXzTIY8n5ZjSrMW1NCBOhOXbnbAhF2awkLMsDSnFsy7BEaw8z_W8HmBoG-ekYL45FL3NHMzLU3TuZzpO8Rq7gkVO81wIv3IHLM_LOMzGr85WN753zo06BrRnDhwVKQ4NdctCIGkchrV6Z4IYmpe0SZJjohu59yHqZHvzY8b6L5NV_eoQZjw05NiqOoCNWBInhYEKJPZWbDKL5aPADWOU2BtYwx6EDPaWomE1I1AR66uNcn688W3b3Tz4cwL5MZ_HYqvIxRf45svlYNvJF33x4ZyuPjbHzWiV7a7jXfWQqPtJW4KeRZF8zaSKVxwtKPOq8sUAWRnF7x1mDHBWe2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
علی‌بابا از مدل قدرتمند تولید ویدیوی هوش مصنوعی Wan 3.0 رونمایی کرد
شرکت علی‌بابا (Alibaba Cloud) رسماً از مدل پیشرفته و ارتقایافته
Wan 3.0
برای تولید ویدیوهای باکیفیت ۳۰ ثانیه‌ای رونمایی کرد. این مدل با هدف رقابت جدی در بازار جهانی تولید محتوای ویدیویی هوش مصنوعی عرضه شده است.
🔹
پشتیبانی از ورودی‌های متنوع:
امکان ساخت ویدیو از روی متن، اسناد، صفحات اکسل (اسپردشیت)، اسلایدها و صفحات وب.
🔹
پذیرش چندگانه فایل‌های مرجع:
قابلیت دریافت همزمان تا
۱۰ تصویر مرجع
،
۵ ویدیوی مرجع
و
۵ فایل صوتی مرجع
برای هدایت دقیق خروجی.
🔹
حالت تفکر:
پردازش هوشمند و تحلیل دقیق‌تر برای دستورات و پرامپت‌های پیچیده و چندمنظوره.
🔹
حفظ یکپارچگی کاراکترها:
توانایی حفظ ویژگی‌های بصری شخصیت‌ها در طول صحنه‌ها و سناریوهای مختلف با خروجی‌های بسیار واقع‌گرایانه و پرجزئیات.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2919" target="_blank">📅 16:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2918">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7_d3-C0vqojtvY5tKKn4ufqftkeJSjBzsDSzFjLor3gHSzrTxN4A41tABUUYMf8IoU9yJRvf0cmbV-8hYobbMgQBNmEKNIPdJTzrMQHd9Vuyrf0QyCJST5RXIprJl-rsIkLT6Nh7zMgv1Lac0RXhdGh4AKC4Hfm2bclECYjlZSESBiaOPPAbqCM_n8fth72uOaywV97_0iRfpOVC1xaw9OH_7_h_ps22mGUFhUCUC4_OaSBbGPrfaK56llvmFSylycsmYctrb0qpKDPZBAJHCq8aDqUcPL3HHsxbewX3Mfqxv0d2qq4WE-AV5DsesbL1wbr10DMztAdXgYRpxCwwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
پروژه استقرار PasarGuard Node روی بستر ابری Railway
پروژه
railway-pg-node
یک Wrapper مستقل برای بیلد و دیپلوی مستقیم نود پاسارگاد (
PasarGuard Node
) روی کلود Railway بدون نیاز به خرید سرور اختصاصی است.
⚙️
معماری و نکات کلیدی راه‌اندازی:
🔹
مدیریت پورت و لیسنر:
کانتینر یک لیسنر از نوع TLS اجرا می‌کند؛ متغیر پورت (
PORT
که معمولاً ۸۰۸۰ است) از سمت Railway تزریق شده و اسکریپت
start.sh
آن را به عنوان
SERVICE_PORT
ست می‌کند.
🔻
اتصال به پنل اصلی با TCP Proxy:
از آنجا که پنل مدیریت خارج از شبکه Railway قرار دارد، باید از
TCP Proxy
استفاده کنید:
🔹
پورت داخلی:
همان پورت داخل متغیر
PORT
یا لاگ سرویس (مثلاً ۸۰۸۰).
🔹
پورت عمومی:
پورت تخصیص‌یافته توسط Railway به همراه دامنه/Hostname عمومی.
⚠️
نکته مهم آدرس داخلی:
دامنه
railway-pg-node.railway.internal
تنها در شبکه داخلی Railway معتبر بوده و برای اتصال خارجی باید از آدرس TCP Proxy استفاده شود.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2918" target="_blank">📅 14:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2916">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teEWRoMl1joduwDC5l8Y-KukXcF7nK-fyU97sdbiCspvm7T6m2AThydEHFnK2UAunByqQ_rHdNqVqXoMSfgMITWdOG3TRSUnMT4S6Iitto_B9mYPyg1R9UzieKsCEfYi290CAATQ01oUOb8CcmRK6PkPFIPkYY7S__xI_mKSF6a37DNtfL6xI4nLRyQlIjrakUqTFz5NVPIrWsJyieBs_4peOTM540OH4Y-bgb94PU7xidP4yORtD2aPS4YYhXVHKutURw-LhTuZvXIC7PS-lh9F1M3ZN2g8wVrox8IRo757yWu5aIRv80oyf6jULJq6Ttbu8cHD_SUkT3Gp-TNRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی tproxy-server؛ نسل جدید پروکسی‌های وب برای تلگرام
این پروژه سمت سرور یک طرح اثبات مفهوم (PoC) از سوی تیم تلگرام دسکتاپ است که روشی کاملاً نوین برای عبور از فیلترینگ ترافیک MTProxy از طریق مرورگر داخلی (
WebView
) ارائه می‌دهد.
🔹
پنهان‌سازی در قالب ترافیک وب (HTTPS/WebSocket):
اپلیکیشن تلگرام فریم‌ها و رمزنگاری استاندارد MTProxy را حفظ می‌کند، اما تمام اتصالات TCP را از داخل یک لایه انتقال مبتنی بر WebView و در بستر امن HTTPS یا WebSocket عبور می‌دهد.
🔹
چندین اتصال در یک مسیر:
این سیستم چندین ارتباط لاجیکال را مالتی‌پلکس کرده و در سمت سرور، رله این جریان‌ها را مجدداً تفکیک نموده و به سرویس رسمی MTProxy متصل می‌کند.
🔹
استتار به عنوان یک سایت عادی:
دامنه سرور مانند یک وب‌سایت کاملاً معمولی و عادی HTTPS عمل می‌کند؛ تنها با داشتن Secret اختصاصی، صفحه پل ارتباطی پروکسی فعال شده و سایر درخواست‌های عمومی فقط وب‌سایت اصلی را می‌بینند.
🔸
سازگاری کراس‌پلتفرم:
این ساختار محدود به سیستم‌عامل خاصی نیست و هر کلاینت دارای WebView می‌تواند از آن استفاده کند.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/iaghapour/2916" target="_blank">📅 20:40 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2915">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv3cq6BtWU3j1iqtMoey25qydE9xm-PPL4_9Gg2JMLcb1jaTRWwmGF8s22ueJ-R2lk26XIU3Jgiaajm0VtnaSioYehpu20r6h6k9HbaYpWT2CuoTURI2RoUr6sXjzDOz_0F26Bb8OnMvaEPdTenwVNxYDZr2eRQ7-pKSGt8f6GIMJn31ire_qESqScquDEKpotHmJ5HV6dnh_FD-vTWh5XAHA_R1X1iAzjRuw9pisQhZTpGXOTBiaCnwLCP1N-kfyUqpAsU-uIfgwyLGsXNTSXaXhg9qmo1i-yy_eYWfMROnaD6Hiy5sHR3fLPAUpA0HtRUwTwK08KvcGvDrp0eboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
حدود ۴۰ درصد از آهنگ‌های جدید ماه ژوئیه با هوش مصنوعی ساخته شده‌اند
بر اساس گزارش تحلیلی پلتفرم
SubmitHub
و با بررسی بیش از ۱ میلیون قطعه موسیقی، نزدیک به
۳۸.۵ درصد
از کل آثار منتشرشده در ژوئیه ۲۰۲۶ با مداخله هوش مصنوعی تولید شده‌اند.
⚙️
آمار و نکات کلیدی این گزارش:
🔹
سهم آثار هوش مصنوعی:
۲۳.۲ درصد آثار کاملاً با AI ساخته شده‌اند و ۱۵.۳ درصد شامل قطعات تولیدشده با AI بوده که سپس توسط انسان‌ها ویرایش شده‌اند.
🔹
عدم توانایی تشخیص مخاطبان:
تحقیقات نشان می‌دهد ۹۷ درصد شنوندگان متوجه تفاوت میان موسیقی انسانی و تولیدشده توسط AI نمی‌شوند.
🔹
هجوم اسپم صوتی (AI Slop):
پلتفرم Deezer اعلام کرده بود بیش از نیمی از آپلودهای روزانه جدید آن به موسیقی‌های هوش مصنوعی اختصاص یافته است.
🔸
واکنش و مقابله پلتفرم‌های استریم:
🔹
پلتفرم
Bandcamp
انتشار هرگونه موسیقی هوش مصنوعی را کاملاً ممنوع و مشمول حذف اعلام کرده است.
🔹
پلتفرم
Spotify
از سپتامبر نشان اختصاصی «AI Persona» را به پروفایل‌ها اضافه می‌کند تا شنوندگان آثار ساخته‌شده با هوش مصنوعی را به‌راحتی تشخیص دهند.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/iaghapour/2915" target="_blank">📅 19:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-2912">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVlhkxjxKK3FwVp1iNSh2x27oiWpAV-ef8bBq5q3qlMydE3gi_7wmLMYkFeYNok4AtT5rN3Y77m1vopnYlJqXe_dhBngFNBB4osISdUTmZUQGGXlvPRlb1tKMXxrRBI3FzMww9Rm1uq5mg5bk_tH1ot_vcnq1hVwJevtf8VM7Giiima1mmysVZkXYGkb_xkg7cZ4az3dbHvwUWA-iTZ90BSBIJMjmQqkQ_KoBsJIzmZhSoc_DhSPHNLrC0iVRu91cshtGl9uq6gWfbHYUrwYrQkiWG9L9KCaJurKwcQp1p1OfyKTkyWLtuqg0YeBhKcZiprY_I8bomXvQnCt6pWO-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
دسترسی رایگان و آزمایشی به مدل‌های هوش مصنوعی Qwen در سرورهای Hetzner
هتزنر امکان استفاده رایگان و آزمایشی از دو مدل هوش مصنوعی
Qwen3.6-35B-A3B-FP8
و
Qwen3.8-27B
را برای کاربران خود فراهم کرده است که می‌توانید آن را به نرم‌افزارهایی مثل 9Router متصل کنید.
⚙️
مراحل فعال‌سازی و اتصال:
🔹
۱. دریافت توکن:
با اکانت خود وارد سایت شده و به آدرس زیر بروید تا یک توکن بسازید:
🔗
آدرس سایت هتزنر
🔹
۲. اضافه کردن به 9Router:
وارد برنامه شوید و یک پروایدر جدید از نوع
OpenAI Compatible
اضافه کنید.
🔹
۳. ثبت کلید:
روی گزینه
Add API Key
بزنید و توکن دریافتی از هتزنر را وارد کنید.
🔹
۴. ایمپورت مدل‌ها:
روی دکمه
Import from
کلیک کنید تا مدل‌ها به لیست شما اضافه شوند.
⚠️
وضعیت فعلی:
در حال حاضر مدل
Qwen3.6-35B-A3B-FP8
فعال و قابل استفاده است، اما مدل
Qwen3.8-27B
با خطا مواجه می‌شود.
©️
aleskxyz
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2912" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2911">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💡
راهنمای ساخت اینباند در پنل 3X-UI روی سرویس ابری Railway
نکات تگمیلی درباره
ویدیو بالا
☝🏻
با این ساختار می‌توانید بدون نیاز به خرید سرور (VPS)، پنل
3X-UI
را روی کلود
Railway
اجرا کنید.
🌐
مکانیزم عملکرد پورت‌ها:
پورت‌های ۸۰۰۱ تا ۸۰۵۰ (وب):
ترافیک از طریق Nginx روی پورت ۴۴۳ مدیریت می‌شود (مناسب برای WebSocket و HTTP Upgrade).
پورت ۸۰۸۰ (مستقیم):
از طریق
Railway TCP Proxy
مستقیماً هدایت می‌شود (مناسب برای Reality و gRPC).
🛠
روش اول: ساخت اینباند WebSocket / HTTP Upgrade (پورت ۸۰۰۱ تا ۸۰۵۰)
۱. در پنل وارد بخش
Inbounds
شده و روی
Add Inbound
کلیک کنید:
Remark:
نام دلخواه (مثلاً
WS-Inbound-1
)
Protocol:
انتخاب پروتکل (
VLESS
یا
VMess
یا
Trojan
)
Port:
یک پورت بین
8001
تا
8050
(مثلاً
8001
)
Network (Transport):
انتخاب حالت
ws
(WebSocket) یا
HTTPUpgrade
Path:
متناسب با شماره پورت (مثلاً برای پورت ۸۰۰۱:
/in1
، برای ۸۰۰۲:
/in2
و...)
Security:
تنظیم روی حالت
none
روی
Save
کلیک کنید.
۲.
تنظیم بخش Host (ضروری):
روی گزینه
Add Host
کنار همان اینباند کلیک کنید.
Address / Host:
دامنه اختصاصی پنل در Railway (مانند
your-app.up.railway.app
)
Port:
عدد
443
Security / TLS:
فعال‌سازی گزینه
TLS (Enabled)
⚡️
روش دوم: ساخت اینباند Reality یا gRPC (پورت ۸۰۸۰)
۱.
ایجاد پروکسی در Railway:
در داشبورد Railway به مسیر
Settings
⬅️
Networking
بروید، روی
Add TCP Proxy
کلیک کنید و پورت کانتینر را روی
8080
بگذارید. دامنه و پورت اختصاص‌یافته را کپی کنید (مانند
domain.proxy.rlwy.net:12345
).
۲.
ساخت اینباند در پنل 3X-UI:
روی
Add Inbound
کلیک کرده و
Port
را حتماً روی
8080
تنظیم کنید:
حالت Trojan gRPC Reality:
Protocol: Trojan
|
Network: gRPC (حالت Multi)
|
Security: Reality
حالت VLESS TCP Reality:
Protocol: VLESS
|
Network: tcp
|
Security: Reality
|
SNI: یک دامنه معتبر (مانند yahoo.com)
روی
Save
کلیک کنید.
۳.
تنظیم بخش Host در پنل:
روی
Add Host
کلیک کنید.
Address:
دامنه TCP Proxy دریافتی از Railway (مانند
domain.proxy.rlwy.net
)
Port:
پورت دریافتی از Railway (مانند
12345
)
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/iaghapour/2911" target="_blank">📅 20:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2910">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc58wZhVbb3MoK7rOQiD5LLsxX3owjVxRKpkhQISE9Iqfnyr3CvY46vMOgYlqHUibVTiHr07AHngHjr1zFYm5z1lBfoZk1iwhn23tILHM8qcR5W2erX_DNevCW7a7zAVbNeI_9QJtp_q7b67D0yDLsUmM0CssMgdirgM7tL5jCZntDpbwIxOhQLnNhdUfhXj1NonvKAk9DeYTM8SklW_QSo1RiiIxbsKGfs1ZjD-FZCRdJuy7oTnmr1K7dFCipR__7RnA4gEMekwAp4Ok0KA-obtKzs7GbOS14vaShcGKHAaXhhM4SmJHIJqHFfHRQVduMbLBOANjpGMB3YIMVzASA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بزرگ‌ترین آپدیت تاریخ CPU-Z منتشر شد؛ نسخه V3 با ۱۰۰ تست سلامت و سیستم اعتبارسنجی جدید
نرم‌افزار نام‌آشنای
CPU-Z
بزرگ‌ترین به‌روزرسانی تاریخ خود را از سال ۲۰۰۱ تا امروز تجربه کرد. نسخه جدید (V3) با بازطراحی کامل بخش اعتبارسنجی (Validation) و افزودن ابزارهای مانیتورینگ سلامت منتشر شده است.
⚙️
امکانات و تغییرات کلیدی نسخه V3:
🔹
اعتبارسنجی استاندارد:
بررسی سلامت کامل سیستم در کمتر از ۱۰ ثانیه با ارزیابی بیش از ۱۰۰ شاخص مختلف (درایورها، دمای CPU، برنامه‌های اضافی و...).
🔹
اعتبارسنجی پیشرفته:
تست استرس و خطایابی سنگین و دقیق روی CPU، رم و کارت گرافیک به همراه بنچمارک جامع سیستم و سنسورهای مانیتورینگ پیشرفته برگرفته از HWMonitor برای بررسی دما، سرعت فن‌ها و فرکانس.
🔹
حالت اختصاصی اورکلاک (XOC):
محاسبه فرکانس مؤثر پردازنده‌های مدرن و مدیریت صحیح اورکلاک رم جهت جلوگیری از رد شدن تصادفی تاییدیه‌ها و ثبت دقیق‌ترین رکوردهای فرکانسی.
📥
دسترسی:
فایل نصب نسخه جدید از وب‌سایت رسمی
cpuid.com
قابل دریافت است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/iaghapour/2910" target="_blank">📅 18:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2908">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=gr8QrwxG2Jk1JDm7wUaVTLjPcqQ0kKTHYnr1fZv633u_H-tTDXZJ7sOU3KsRsTaY0C6S4laZ0BLCjRr18GCIw0jTMq4cVLGBnmcfcPd4zgnCgSMxjsLErKwxSkdsE6cjxcuK4E6xuPqJLUa6gAwMrsFICkKT4PtXGtWIDyaQtbGUjgpT3akSBY6b2zbqHjylpjnMNKJSfdVGv7HAPk6EqSkZkZhvi5z3NKmUss4tl0cutkaBBRpYpymmvoDMutPjKvwRds5V_qJwis2IJQp5s3NJb606r00A-L62gkJb3BLEePGtzS4_RKuJPx4jXhSHDs9tA7A38YWSUSquK5JNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de89d4765.mp4?token=gr8QrwxG2Jk1JDm7wUaVTLjPcqQ0kKTHYnr1fZv633u_H-tTDXZJ7sOU3KsRsTaY0C6S4laZ0BLCjRr18GCIw0jTMq4cVLGBnmcfcPd4zgnCgSMxjsLErKwxSkdsE6cjxcuK4E6xuPqJLUa6gAwMrsFICkKT4PtXGtWIDyaQtbGUjgpT3akSBY6b2zbqHjylpjnMNKJSfdVGv7HAPk6EqSkZkZhvi5z3NKmUss4tl0cutkaBBRpYpymmvoDMutPjKvwRds5V_qJwis2IJQp5s3NJb606r00A-L62gkJb3BLEePGtzS4_RKuJPx4jXhSHDs9tA7A38YWSUSquK5JNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره پنجم و ششم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر مشخص شد:
👤
نیما عزیز با آیدی nimashokri5515، مبارکتون باشه!
✨
👤
حامد عزیز با آیدی hamedsalamati2286، مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسرهای عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/iaghapour/2908" target="_blank">📅 20:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2907">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey2_da9SR82BvRqRmS9FgD4S8cxFwrjyW_aIX9Qp0uD-C2FxvuMZaFJZwVNfGzObe6UbDfi8fLDXiEq_u1ENULxVA22wUx2h2AlpFAhUapPhkWIjBdex2-6urtqak_c_O9jpeRmpqUAlQOxOvo8b8ibwbxO_NK9CrqQI-xgo9FB_K0VdVPxX2_efIjKKd1P_40c2L7ZMeVinSxZtex4lViYWWGcQ7-3WRxyMEfMQ8IU5If_6h5n5cmOxaiYrUP8wiziuv02Pv1geYnpKH6yccT1gKG6dHlhnrnzlzX5dqCw8Yzkog7Et1lkQO5Q24XrtY522w11J6Kf9T7s3u8tOtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
تداوم ناپایداری‌ها؛ دیتاسنترها گرفتار فیلترینگ سخت‌گیرانه و سامانه «شاهکار»
بررسی‌ها و تایید مدیرعامل شرکت ارتباطات زیرساخت نشان می‌دهد وضعیت اینترنت در دیتاسنترها هنوز به روال عادی قبل از دی‌ماه ۱۴۰۴ بازنگشته است.
⚙️
چالش‌های کلیدی مراکز داده:
🚫
فیلترینگ شدیدتر:
دیتاسنترها با محدودیت‌هایی به‌مراتب سخت‌گیرانه‌تر و اختلالات فنی مرموزتری نسبت به اینترنت خانگی دست‌وپنج نرم می‌کنند.
🔻
بحران سامانه «شاهکار»:
بزرگ‌ترین مشکل فعلی، الزام به احراز هویت دستی کاربران در سامانه «شاهکار» پیش از اتصال است که این فرآیند را از ۲۴ ساعت تا
یک هفته
طولانی کرده است.
🌀
سردرگمی کسب‌وکارها:
تیم‌های فنی هنوز درگیر ترمیم زیرساخت‌های آسیب‌دیده از قطعی‌های طولانی هستند. فقدان تضمین برای عدم قطعی مجدد، شرکت‌ها را میان بازگشت به معماری استاندارد یا حفظ آمادگی برای بحران بعدی معلق نگه داشته است./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/iaghapour/2907" target="_blank">📅 19:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2906">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYP_J1wEfECSnlqkx6JlYW-Fu3mzxG8-rCrNqxoBrW_RNdNF39iyMkmOzkR9sWOiurBIFJkffK8YlotfNtyo6RRYnNH6Ias-KGM-RFJMTuw6SRX5CiJqxgfusKA8RT2myHbTQN4Oa11cSYMlLVpSwjvHw2lA1sJmnJdIyEyK5ANXNC9pvAxcr-UKjFHLtLMUVbZKkR28wceDLw-DeVCkXXZruMhDu_aMXEnaFVClsVlflF1F1-w3Ub-0kYZEB9u0z9bGv84920ayfRaWXCwahfHMurMb_Fp4xGtgS3Uw68S4riwjKqQwd4v6-wkParnxb9aEUTEjEZnmplPoRuarvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Tor Node Manager؛ اسکریپت ساخت و مدیریت خروجی‌های تور تفکیک‌شده بر اساس کشور
این پروژه یک ابزار تعاملی است که به شما امکان می‌دهد روی سرور خود نودهای مجزا و اختصاصی Tor را بر پایه کشورهای مختلف (مثل ترکیه، آلمان، هلند، فرانسه و...) به‌صورت پروکسی‌های لوکال SOCKS5 بسازید. این پورت‌های لوکال به‌راحتی می‌توانند به‌عنوان Outbound در پنل‌های
3X-UI
،
Xray
یا سایر برنامه‌ها استفاده شوند.
🌍
تفکیک نودها بر اساس کشور:
ساخت نمونه‌های مجزا از Tor با لوکیشن دلخواه و پورت SOCKS5 اختصاصی روی
127.0.0.1
.
🔄
سرویس‌های مستقل Systemd:
اجرای هر کشور به‌عنوان یک سرویس مجزا در سیستم‌عامل به همراه فایل کانفیگ، دایرکتوری داده و لاگ اختصاصی.
🔍
تأیید خودکار موقعیت جغرافیایی (Geo-Check):
بررسی زنده و چندمرحله‌ای اتصال و کشور خروجی Tor، همراه با سیستم تلاش و ری‌استارت مجدد خودکار تا زمان تایید قطعی لوکیشن انتخابی.
📋
کانفیگ آماده Xray Outbound:
تولید و نمایش خودکار قطعه‌کد آماده‌ی JSON برای اضافه کردن مستقیم به بخش Outbounds در Xray یا 3X-UI.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2906" target="_blank">📅 14:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2904">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmZGjnoX-zDpMq0CxURDqoq8THFuTCYJc0ZJMVLwAh6oBvgGrZJ-HSF0T7kcqIY6Fe5cgOOpUukgkFefwv6Q4uc2uMIhOOX75re7d9Wyn1P2hmaJiYKuhWu4Z5zz3nvIdQgXGNiVSBxZTqz1f9pqD9lKOdQ9A1nIaU3V-yOp6w8jKDdA0b1eypAqj3leFQQQsc1ksxmcK2Wdd2SnIvZN3zRjutUo987DpTLINSxuZobVvS-u9W0yYsyIFHuGvk88EuURE0P5n4lEXFhUSdhzNHrFOUhvm4C6_LVWy2y0BB-uA7QkhQYd2RazBRlE9yrsUHMhCAHgZIVmxKTCDVPlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش ساخت فیلترشکن شخصی بدون سرور و دامنه (کاملاً رایگان!)
🔹
اگه می‌خواید یک کانفیگ کاملاً شخصی برای خودتون داشته باشید، ساخت فیلترشکن شخصی بدون سرور و دامنه همون راهکاریه که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم که چطور بدون سرور یا دامنه، پنل X-UI رو راه‌اندازی کنید و برای خودتون کانفیگ شخصی بسازید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.(قرعه کشی این ویدیو با ویدیو قبلی باهم انجام میشه)
#آموزش
#فیلترشکن
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
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/iaghapour/2904" target="_blank">📅 17:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2903">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGNiuBmHL5_pDnha_MnWySPL0kiA0jwldjR4-GsFn8ksWULPmvjnh0rrXfizHxp5VC1eSe4disPIrrwoPQwZT90SoEKJ9w2bMDW76hWYPl5-PzplU8KhxsKM_Egw_Kz4O1wrkZFxc20Mw0B0pmhQ468ql2dDKj1cWK1eCYE08tGKRAHMwZOCadYGT1TmQNmsgZnmwpiFLKbPzD5bpwsG6zi4B7DpnIG2QTmwt_9EsEUdEGi5CgUIPG5_Jw7qf5Euu0giHxXZ22vBvnCeH8V0s9vO1fJsLut3FcRQKaOR2t-lQCTKNQHlDSMkInWWq6UJ0Cq64zC9fWpDThvNoCZIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش استعلام سیم‌کارت‌های فعال به نام شما با کد ملی
بی‌خبری از سیم‌کارت‌هایی که به نام شما ثبت شده‌اند می‌تواند باعث سوءاستفاده‌های حقوقی، امنیتی و جعل هویت شود. طبق قانون، هر فرد حداکثر می‌تواند
۱۰ سیم‌کارت فعال
در مجموع تمامی اپراتورها داشته باشد.
⚙️
روش‌های استعلام:
📩
۱. استعلام سریع از طریق پیامک:
— کد ملی ۱۰ رقمی خود را به سرشماره
۳۰۰۰۱۵۰
ارسال کنید.
— پیامکی از
CRA.ir
حاوی تعداد سیم‌کارت‌های فعال شما در هر اپراتور ارسال می‌شود.
🌐
۲. استعلام کامل از سامانه «دولت من:
— وارد سامانه
my.gov.ir
(یا اپلیکیشن دولت من) شوید.
— پس از ورود، از بخش
دسته‌بندی سازمان
⬅️
سازمان تنظیم مقررات و ارتباطات رادیویی
را انتخاب کنید.
— با انتخاب گزینه
«تعداد خطوط مشترکین تلفن ثابت و سیار»
، تمام شماره‌های فعال همراه اول، ایرانسل، رایتل، اپراتورهای مجازی و سیم‌کارت‌های TD-LTE را مشاهده کنید.
⚠️
اقدام فوری در صورت مشاهده سیم‌کارت ناشناس:
اگر خط ناشناسی به نام شما ثبت شده است، بلافاصله از طریق اپلیکیشن یا نمایندگی‌های اپراتور مربوطه نسبت به
سلب مالکیت یا سوزاندن سیم‌کارت
اقدام کنید./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2903" target="_blank">📅 16:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2901">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sg6mVquBZpHXGIKoZbySmrpFKbhcL9_UkMzpI6KKHEwmTgGtAGYEzcQiRY7g8zdRSsyRjd_GiRfOoaRvNaRFMpbJUHkvusFY81G81VbTKRchoDgexcjwOpyq4Rm5lyTEoWW4zfiBZFEVQxqqC5qvbssY2WqR85ukTI8L7AfYjXFozoWJE-5Lt3eXcuX8KloLi_dg0pxfP8xWh00srPxV32tnDVXGZmB0JlkL3x0u2Xp6btH-qz9bCfXZuFU1YQcnSOSGVghniFUR-Y8UV2UrkjeZw0LDPtjPzJo5mNn7SxGkvaG2KvfbSCsKpxb4TVNiybEyXktIrt9m7M7SEp4LsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فقط با یک سرور، 3 لوکیشن مختلف داشته باش! (با پنل 3X-UI)
🔹
اگه می‌خواید تو هزینه‌های خرید سرور صرفه‌جویی کنید ولی همزمان به آی‌پی‌ با لوکیشن‌های مختلف نیاز دارید، این آموزش دقیقاً همون چیزیه که دنبالشید. تو این ویدیو قدم‌به‌قدم بهتون یاد می‌دم که چطور فقط با یک سرور، 3 لوکیشن مختلف داشته باشید و این کار رو به سادگی روی پنل 3X-UI پیاده‌سازی کنید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.
#آموزش
#فیلترشکن
#ثنایی
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/iaghapour/2901" target="_blank">📅 18:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2900">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXBE3bjRviumSu6JeG8-EphKdddRToHp52yZFsOQTYxlN2IW3RSOVZD90RifBkih8nJlzsJHW7rKK67Jx_6phhTpdzcItErjDgTtntAXZFSpR1lKjs2mbAzSaN5bI7GhRlz9xdYV5QXxskdZtuM5knbQzILBDPjW6qgzPXglmsQD_cgEtnJLWm9jN3dvfBIOGrvsVItUK-DzKIRPR3av7KHOElGSoyTctffA-wquTVyFmsQ7BIosiRXVAJclgRNnxLETF9SRvRLsEI9oa1e__d8FYNNbWJIgGrFWDOXFpk8MLIX2njbUCV1y6wsmx0EewiNVrBLzyTQ761NzntiTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تلگرام به هر کاربر دامنه اختصاصی با پسوند gram. می‌دهد!
تلگرام رسماً درخواست ثبت دامنه سطح‌بالای اختصاصی (TLD) با عنوان
gram.
را به سازمان آیکان (ICANN) ارائه داده است تا کنترل کامل زیرساخت آدرس‌های خود را به دست بگیرد.
⚙️
جزئیات و امکانات این طرح:
🔹
دامنه اختصاصی برای هر کاربر:
در صورت موافقت آیکان، بیش از ۱ میلیارد کاربر تلگرام دامنه‌ای بر پایه نام کاربری خود دریافت می‌کنند (مثلاً
username.gram
).
🤖
ساخت وب‌سایت با هوش مصنوعی:
کاربران می‌توانند وب‌سایت‌های تعاملی خود را روی همین دامنه‌ها و با میزبانی مستقیم تلگرام، تنها با وارد کردن یک دستور متنی (پرامپت AI) بسازند.
🛡
استقلال از واسطه‌ها:
این اقدام پس از اختلال اخیر دامنه
t.me
توسط ثبت‌کننده پسوند
me.
انجام شد تا تلگرام از وابستگی به رجیسترارهای ثالث رها شود.
⏳
وضعیت تایید:
پذیرش این درخواست منوط به سپری شدن مراحل نظارتی، فنی و حقوقی در سازمان آیکان خواهد بود./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/iaghapour/2900" target="_blank">📅 17:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2899">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmDDy2zl0fE5Hfee0BkZOEhkLmzxYL21QwPhXdQWatFGo2HLkFe9ywDr7ztwt3eY-RLg3Ms5RT5bLq5pzTlayQBDReuCogyxPPEAkJGppoH0MiRxhrvsmWdgnxgQFx0WRPqOXv8p7HKUr179h3zzbnHO26SEIdwYkUMNKoI7VzCeduXO1nbM9RlHWbv0sXBFaONlzsaNUMJ168lSlYwUGC6ijLKpLMbd0_GElCFZEPrWz4-E7-tD5KrNu067fT5lR4dQubTdncgXWxAzVR7Q71ljw3o0GXASBtRFYVsXZmRQUL_Py7NtyZBrcP-cWSreZLzQ8ESLKznTEXhIWLbGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
نظرسنجی ایسپا: بیش از ۲۰ میلیون ایرانی خواهان استفاده از اینترنت استارلینک هستند
بر اساس نظرسنجی جدید مرکز افکارسنجی دانشجویان ایران (ایسپا) به سفارش وزارت ارتباطات، در صورت فراهم بودن شرایط، بالغ بر
۲۰.۵ میلیون نفر
از کاربران ایرانی تمایل دارند از اینترنت ماهواره‌ای استارلینک استفاده کنند.
⚙️
یافته‌های آماری و نکات کلیدی نظرسنجی:
📊
میزان آشنایی و تمایل:
۵۶.۶ درصد
کاربران هنوز شناختی از استارلینک ندارند.
در میان افراد آگاه،
حدود ۶۱ درصد
تمایل دارند این سرویس را تجربه کنند یا به صورت دائمی به آن متصل شوند.
🚫
مانع اصلی، قیمت و دسترسی است نه قانون!
برخلاف تصور، منع قانونی دلیل اصلی عدم اتصال اکثر افراد نیست؛ تنها
۳۸.۲ درصد
به دلیل غیرقانونی بودن سراغ آن نرفته‌اند.
نزدیک به
۶۰ درصد متقاضیان (حدود ۱۲ میلیون نفر)
اعلام کرده‌اند دلیل وصل نشدنشان،
قیمت بالای تجهیزات
و
عدم دسترسی به فروشنده مطمئن
است.
⚠️
پیام هشدارآمیز داده‌ها:
آمارها نشان می‌دهد در صورت کاهش هزینه‌های تجهیزات یا تسهیل مسیرهای ورود به کشور، تعداد کاربران استارلینک در ایران می‌تواند با جهشی میلیونی روبه‌رو شود./شبکه‌چی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/iaghapour/2899" target="_blank">📅 16:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVsXPwCr-2vxzlle_Qt3ZTwh8uLXqzHb_h5dRAhrrNbog4YyJVPcV5afmsW1qsPaQrYFrkDAYFqqtX1yR7CUWporn77nTFkIUsEtoNppdzS7kGeSMsqNg2qZfvpU8nmAlXNP3HV1dtri0Gl_Pom6vKoEoJZPnotAXOsRLT8j5wzdmvuy1R4ESDmTu-DBsWQomgLsqyd1oYROfwGJiRmwMJ3WVNBekij6KP9MHdmZYgv9h-_sXVj5oFZbsob_8ftAYyLyt9N2deEJW7TSLLA4xU4Kg2oTP0nn-N_hI7vaCzFQT_W16Yy788UyWtWpeUlHcX1lVrcz7rHDrswBOvksbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کدنویسی در سال ۲۰۲۶ :)</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/iaghapour/2897" target="_blank">📅 20:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2895">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joaD2buwmREODdQVv5klQwpXCJVRfzSUBfqFeWSiQEoD0Z8iaYfPtBaP8uLxe4lTLTfS1bl6amau8fuTaOUnVwfadezIp-zGm3kZdMRge-wU1hCF_-jVDc2QiHUNazagq7JPDNY8_yZvPRamA-PQnK2i498KcmiJs0EtnVrxorr9jC-KQo6Npy56kcsrh8XEi6YB-EPFctkZ9NnJThIyiQoLI2HuN6ZmAXoIBexUwcUqYIhDWBQR9iQbc0gCKApNbkcSk41BIMygkq33a0bBSHVnWgnxBg6lL7d_rO2CtzeazWstngX3t7mbaoJvj8eh-TQw1UeXLf4H9NTIPKkOaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpdQ_lTGCqP3AxlZuaaD3oJpzCj69i-_a7MOoTDlXzQj8yczYB_n6SZdkfDVPA0ox2UYuHBMZcJ1INrSrhnoHG-KbUXQwyEbQBu2imV8a7zXpOjid0KMc1J-ouqcMvdWRRb9HvoVRqKAIL_mtCXi1bYdgOr7zYz8kw2YXnrKLC3TB5F7_LsIDlLqnggmkw7dJ0YjTLmQ-hJDeKyEYGXYoOd9DKmxmcYAt1xmsdQFkEFI-Rsp2ln14LpQVurnSfsWI9u0-fiNpqRGlm3FZYzQsP_CWzOEw2MW3-Fyt-3zBwAgyfme7WRX9xYM2RcuGi_Vo1aiUJTaGSajyWaFL1-k1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
جایزه قرعه کشی تحویل 2 نفر از برنده ها شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.
👤
آقا mohamada8562 عزیز، مبارکتون باشه!
✨
👤
آقا birang_ali عزیز، مبارکتون باشه!
✨
🔻
متاسفانه یکی از دوستان دیگه با نام کاربردی پایین پاسخ ندادن:
👤
M4hdiGaming</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/iaghapour/2895" target="_blank">📅 20:18 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2894">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/atNcFE-573aYEn83GLi0_oG9SH517rREMyaHjDXJqDAPZKM5axf2gtn27ZIBP8-ubLS7pFGJSqS5rAVzRwQzqvPRtw-xxH0GsoBU93nlkDjC3TjBf1EhF1efEWqi7M1rprcdqYUSKcFSeMzQjqZcveUexoFaCkZCBqJSt-0U1aeYUOObQ5Fvvtk03OaEVbc3xXwebWOb9fMCgVziaBsjIiFKdw79BszauPTo8riELYwfkdj4dIyfwyYNEnD5mbzvSkYah9xXoMk__yVCdmY-tjNNPPWgFhvOxRIbTWCpeNvXKmIioxMD2eoYctk2DVwZpEGbll_4-rsHPvrFHsdDOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
امکان شناسایی افراد با سیگنال‌های وای‌فای!
پژوهشگران موسسه فناوری کارلسروهه (KIT) روشی نوین توسعه داده‌اند که با تحلیل امواج رادیویی روترهای استاندارد Wi-Fi، هویت افراد حاضر در محیط را با
دقتی نزدیک به ۱۰۰ درصد
و تنها ظرف چند ثانیه شناسایی می‌کند.
🔻
نحوه کارکرد و جزئیات فنی:
📡
این فناوری مانند یک دوربین نامرئی عمل می‌کند که به‌جای نور، از امواج رادیویی برای تصویرسازی محیط استفاده می‌کند. فرد حتی اگر گوشی خود را خاموش کرده باشد، صرفاً به دلیل بازتاب امواجِ دستگاه‌های فعال دیگر در محیط، قابل شناسایی است.
🔓
این سیستم داده‌های «اطلاعات بازخورد شکل‌دهی پرتو» (
BFI
) را که به‌صورت عادی و رمزنگاری‌نشده میان کلاینت و روتر ردوبدل می‌شود تحلیل کرده و تصاویر محیطی و هویتی می‌سازد.
🔬
در آزمایش با ۱۹۷ شرکت‌کننده، مدل یادگیری ماشین توانست افراد را با دقت نزدیک به ۱۰۰٪ شناسایی کند؛ به‌طوری که زاویه دید و نحوه راه رفتن افراد نیز مانع تشخیص نشد.
⚠️
به دلیل حضور گسترده مودم‌ها در کافه‌ها، خیابان‌ها و منازل، این فناوری می‌تواند به یک بستر نظارتی نامرئی تبدیل شود./تک‌ناک
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2894" target="_blank">📅 14:41 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnIrdrMddunbvNpYZ0hv6qkPs_4C_RJXL6j9BbnTSEkxA3ML1z79R1a6RkpgVej5rOayj2W_mI_H61WEt9Iyy1SiY2MeYXhPTN0BqYDW9LQYq-9WeeLSB3Sy_JTVxFMhxzXAgeVRHR7UmfPj3gzIqA5gPV1P8mVfXwI-E3hNRCDoTiB_m_2ZD2sJHMGLaeQl4XrNdtPHUv2T1L5PZBIeSe6ZG1zq-bhqgI-PTS2b3WgwuNTosftVvyPhbopNyqQh5s2qCqq7_0FMcQUaSwPZJDTvnFb3s7e-ESkqU8A58C-4q4Oh3nMzaVlF5YgrF8dvlvzOkcy8vmlKTTWKM5LXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش بهترین تانلینگ شخصی با Dragon Fruit Relay
🔹
تو این آموزش قدم‌به‌قدم و به ساده‌ترین شکل ممکن بهتون یاد می‌دم که چطور سرور خارج رو به سرور ایران به هم متصل کنید و یک تانل پایدار، شخصی و پرسرعت (به‌عنوان بهترین مکمل برای پنل 3x-ui) بسازید. البته میشه با کامپیوتر شخصی هم تانل کرد :)
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیو های قبلی قرعه‌کشی اکانت هوش مصنوعی داره، فقط تا فردا برای شرکت فرصت دارید.
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
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/iaghapour/2892" target="_blank">📅 18:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJfKgO4QiTuU0CkyWJOY3Baaj_Z2eDwjJijBjJGQhKAwOXOWd_oEGm8i1TjplC1jbAA-fMkPXsblbNRXhYwTCILBF9MYf4PNRt8N-wKsH5TGeamvGWSiEXsCB5EMXV_j8HYHpQ7E5AzLSaJEZpVUJDCfahPCSGI5UkLL46CG3WbHcK7gNQBR1LBmZGOQom8k_-VvfonBEwUQIQ2aO4pKJJ_bevhDQ33tlx5AyH91GZHoQUsscUcjlKMvwocqR9aE5Xw2A-JjuoEyrTexuYBVwv1kE2_fF9UeCFnMhP9UXt3r56-OOkfPCLjFNC-IeF0HnD-c0aAuBUl3xQId5pDTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✍🏻
یکسری نکات درباره تبلیغات تلگرام و تبلیغات خودمون رو قبلا هم گفته بودم و خالی از لطف نیست دوباره هم بگم.
⚠️
درباره تبلیغات تلگرام:
تبلیغاتی که در پایین کانال، زیر آخرین پست نمایش داده می‌شوند، توسط سیستم تبلیغاتی خود تلگرام قرار گرفته و هیچ ارتباطی با ما ندارند. معمولا این تبلیغات نشانه هایی خاص دارن مثل ارتفا کم کادر تبلیغ و یا قرار گرفتن علامت
ضربدر
و نوشته شدن کلمه
Ad
در کادر.
🔸
استفاده از آن تبلیغات کاملاً با مسئولیت شخصی خودتان است.
🔹
درباره تبلیغات پست‌شده توسط ما:
هر تبلیغی که در کانال منتشر می‌کنیم، فقط برای همان محصول یا خدمت خاص نوشته شده (مثلاً اگر "کانفیگ VPN" تبلیغ می‌کنیم، فقط کانفیگ بخرید نه دامنه یا سرور و یا خدمات دیگه).
⚠️
لطفاً فقط همان محصولی که در متن تبلیغ ذکر شده را از تبلیغ‌دهنده خریداری کنید.
✅
فقط از تبلیغاتی که ما به صورت مستقیم در کانال پست می‌کنیم، استفاده کنید و همان محصول مشخص شده را بخرید.
✍🏻
اگر تبلیغ‌دهنده محصول دیگری را به شما پیشنهاد کرد، این خرید ارتباطی به تبلیغ کانال ما ندارد و مسئولیتش با خودتان است.
ممنون از همراهی شما
🙏</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/iaghapour/2891" target="_blank">📅 16:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوستان عزیز، حتماً برای ارتباط با ما فقط از طریق ربات اقدام کنید.
به نظر می‌رسه یه سری از افراد دارن سعی می‌کنن با کپی کردن آیدی و عکس بچه‌های تیم ما، خودشون رو به عنوان پشتیبان کانال جا بزنن و سوءاستفاده کنن.
پس لطفاً برای ارتباط با پشتیبانی،
فقط و فقط
از طریق ربات رسمیِ
ارتباط با ما
پیام بدید تا مشکلی پیش نیاد.
🙏🏻</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/iaghapour/2890" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2888">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxJs9NtZSBkHR2KiMOuquR4pfkPOuY3yy63WpzHw-6uOf6GlSqeZn_t_TJZw5uVWVXjiAioS720vi4eDVskfvrogJzGe2psV_YVtv5c8DrhwEmLxz1OfWlFo9u-0UcfSHtCBQ0sW7zgX8BtaWpy5qFR-CRRuTZnALo8bdMPdeWUwaWRhIPnq_cj19eKIeylfYtNYvIb8lEziZWML8DWOk1UMnLkKJnECGT-Rd_PFR0m8ReRph9lrHLH-F_ISAkakaiSBSD_9Z2HEeWNngvE0_rylaAnSqhVOirmNCHBGs0Yio3N928_YUWSrg6br5YawMauwGQvKsHFxuvq25KLWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
خسارت ۶۷ همتی محدودیت‌های اینترنت به اقتصاد دیجیتال
ستار هاشمی، وزیر ارتباطات، در گفت‌وگو با روزنامه ایران اعلام کرد محدودیت‌های اینترنتی تا اواسط اردیبهشت، بیش از
۶۷ هزار میلیارد تومان (همت)
خسارت مستقیم و کاهش درآمد به حوزه فاوا و اقتصاد دیجیتال تحمیل کرده است.
🛑
فراتر از خسارت مالی:
این رقم تنها بخشی از آسیب‌هاست و مواردی چون از دست رفتن سرمایه‌گذاری‌ها، افت اعتماد عمومی، آسیب‌های علمی و مهاجرت نخبگان در آن محاسبه نشده است.
⚠️
محدودیت نباید فرسایشی می‌شد:
وزارت ارتباطات از ابتدا معتقد بود محدودیت‌ها باید کوتاه‌مدت و هدفمند باشند؛ چراکه قطع اینترنت، سلامت، آموزش، بانکداری و امنیت سایبری را مختل می‌کند.
💰
اختصاص ۷۰ همت بسته حمایتی:
اختصاص منابع حمایتی برای کسب‌وکارهای زیر ۵۰ نفر (تسهیلات تا ۲.۲ میلیارد تومان و ۴۴ میلیون تومان به‌ازای حفظ هر شغل)، هرچند هاشمی تأکید کرد که ریزش مشتریان و مهاجرت متخصصان با پول جبران نمی‌شود. (من نشنیدم به یه نفر داده باشن)
🤖
توسعه هوش مصنوعی تنها متکی به مراکز داده داخلی نیست و نیازمند ارتباط پایدار با جهان، مدل‌های متن‌باز و خدمات ابری است./زومیت
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/iaghapour/2888" target="_blank">📅 20:34 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2887">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWRl0wGkZLy-H6S7hVWi9LFKILanvXFYHQvdILq0QIr3q-cICiLYBWPHJbVJlG2ohI94p3IlsO4ltG2E5Z3mqpzw49DECT07Gw1IlwQ7cLJwYU4v5VW_umI5jLtDTC_QN1-aSyph0rl2jnsTOSHe9ljdeoOqF-9-yKbfdP2CKtx-rkQBYgJai4HooJiIng-tMR5PiOaQOVqIoQ6qavcmxnAz6owFeeXnFES75EKyclSxE3iX-lId5Gw_ldU9PcVE04Wt_md0QX2RCsoLcxnOJtyvNd4TNVFwLGgqkMxRWzoA3f1wdNOuBTPSnPA55NluxvtX9erzRpyvPeIVon-H9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
احتمال ۲۰ سال زندان برای دختر بیل گیتس؛ رسوایی تقلب مالی استارتاپ Phia
اسناد داخلی و بررسی کدهای نرم‌افزاری پلتفرم خرید آنلاین
Phia
فاش کرده که فیبی گیتس (دختر بیل گیتس) و سوفیا کیانی، هم‌بنیان‌گذاران این استارتاپ، ماه‌ها از ثبت ساختگی خریدها برای دریافت کمیسیون‌های غیرقانونی آگاه بوده و بر آن اصرار داشته‌اند.
🍪
روش تقلب:
افزونه مرورگر فیا به‌صورت پنهانی و بدون دخالت خریدار، کوکی‌های ردیابی را در صفحه تسویه‌حساب فروشگاه‌های بزرگی مثل نایک، گپ و نوردستروم تزریق می‌کرد تا کمیسیون خریدها به حساب فیا واریز شود.
📉
سقوط شدید درآمد:
با غیرفعال‌شدن این سیستم، درآمد روزانه استارتاپ از حدود
۸۰ هزار دلار
به
۱۰ تا ۲۸ هزار دلار
کاهش یافت؛ بیش از ۵۰ درصد درآمد ادعایی این شرکت از طریق همین روش‌های نامتعارف بوده است.
⚖️
خطر ۲۰ سال زندان:
اسناد نشان می‌دهد مدیران دست‌کم از ماه دسامبر از این تقلب آگاه بوده‌اند و حالا فیبی گیتس با خطر تا ۲۰ سال حبس روبه‌رو شده است.
🔄
واکنش سخنگوی فیا:
این شرکت اعلام کرده تمام کدهای مخرب را حذف کرده، در حال بازگرداندن مبالغ نادرست به شرکای تجاری است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/iaghapour/2887" target="_blank">📅 17:57 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2885">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/def52ea06b.mp4?token=oYQhsHqa48rYu2upOUylgnBEy08h3M89XG0ZYyYdGS_gzQ-tHIJHU_e8EMBggfwZQAuDxJQEZvXoGO5KXT7-yiOKkgBJDsuKqvjKa5CyCDD7Jn1Sr35tuoPDCnvlrl9miImblwBQ-N7IPtUF9sqPmknr12nJKtPjWfnVO8Iv3h-gHQAH76p_oLFLFhDvsBHx80xL7llh_v4p1hxJZi9OlDnyKRHOJnfpTLuw2z3ocdCDNN9VmNIXJAKP5-EfNspvd60EAQlmQ74tS1AA_akaKlegap6VjSvQrKjR7qlbLa2dyZMcjy17XsBKPijH2SPEm4lcVhmE08LEnwJsxtWETg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/def52ea06b.mp4?token=oYQhsHqa48rYu2upOUylgnBEy08h3M89XG0ZYyYdGS_gzQ-tHIJHU_e8EMBggfwZQAuDxJQEZvXoGO5KXT7-yiOKkgBJDsuKqvjKa5CyCDD7Jn1Sr35tuoPDCnvlrl9miImblwBQ-N7IPtUF9sqPmknr12nJKtPjWfnVO8Iv3h-gHQAH76p_oLFLFhDvsBHx80xL7llh_v4p1hxJZi9OlDnyKRHOJnfpTLuw2z3ocdCDNN9VmNIXJAKP5-EfNspvd60EAQlmQ74tS1AA_akaKlegap6VjSvQrKjR7qlbLa2dyZMcjy17XsBKPijH2SPEm4lcVhmE08LEnwJsxtWETg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برندگان عزیز قرعه‌کشی
(دوره سوم و چهارم)
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده 2 عدد اکانت هوش مصنوعی ۱ ماهه برای 2 نفر و یک اکانت Canva Pro Lifetime (مادام‌العمر) مشخص شد:
👤
آقا M4hdiGaming عزیز، مبارکتون باشه!
✨
👤
آقا mohamada8562 عزیز، مبارکتون باشه!
✨
👤
آقا birang_ali عزیز، مبارکتون باشه!
✨
✍🏻
با تشکر از اسپانسرهای عزیز این قرعه کشی.
لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/iaghapour/2885" target="_blank">📅 18:55 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2884">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TC4qoS-VZ32ZGkPdC58sjiYxXcePWfLMerUYbxcJF-mZElyhmjmhh8yq3AznG7t1SoZdrbqifSWT-T-ZxOPK6iX33dt7KeFInNvkI_vaomJ6v3Pp_qHdawNliOxnZyUAwyJGkT4JaqP9mC4T7r3xqpA8tottIenAr7BgWJskJilsnm4NWkPu3Ed4Rg__kJ488N5Kh39qcPSYCNHXdb4RKrmp4LGLpW1Xtju1noFHCcCVRVnrErx5mZL0SGguUG1QgT21KLLTObkhDRettEZUrA7AmuLnkaDkNiQ0hw6QUji7gfykpZSLy0Lqnz8lkyf_Ybop8zQYFsoGRkOpnxq7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رونمایی گوگل از هوش مصنوعی Gemini 3.7 Flash؛ جهش چشمگیر در کدنویسی
گوگل تنها سه هفته پس از نسخه قبلی، از مدل هوش مصنوعی
Gemini 3.7 Flash
رونمایی کرد که با پیشرفت‌های الگوریتمی بزرگ در مهندسی نرم‌افزار، توسعه وب و پردازش اسناد پیچیده همراه شده است.
💻
جهش بزرگ در برنامه‌نویسی:
افزایش چشمگیر دقت در رفع باگ و اشکال‌زدایی (ارتقای امتیاز DeepSWE V1.1 از ۴۹٪ به ۶۵.۳٪ و FrontierCode 1.1 به ۴۳.۶٪).
🎨
توسعه وب و طراحی UI:
ساخت وب‌اپلیکیشن‌های کامل‌تر با تعداد پرامپت کمتر و وفاداری فوق‌العاده در تبدیل اسکرین‌شات و طرح‌های گرافیکی به رابط‌های کاربری تمیز و منسجم.
📚
استدلال قوی در اسناد حجیم:
پردازش دقیق‌تر اسناد پیچیده حقوقی، مالی و علمی (رشد امتیاز بنچمارک GDP.pdf از ۲۲٪ به ۳۴٪ نسبت به نسخه ۳.۶ فلش).
💰
کاهش ۵۰ درصدی هزینه‌ها:
قیمت پایه به
۰.۷۵ دلار
برای هر ۱ میلیون توکن ورودی و
۳.۷۵ دلار
برای خروجی کاهش یافته که نصف قیمت نسخه قبل در زمان عرضه است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/iaghapour/2884" target="_blank">📅 17:31 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2883">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6vnYNqWu0Nyl8Rf-TI-qmikVRQeXYqsdyt0ho2q6HFt5GSoCQAl7MBC2fkEtI24v98PnssT6jDPit5MTskmZX7kFs-UjiKAkaNv5a9aMIsXlYehUGZO0mXQNerPxSGJBbzf-DrQeWMZxoS7hEOuKptvcutYDX5NeTerxgnCEipFIt-Qq0JccMhv-OUy6K6vzdwr39yWEL5j8oNzswQOhY_Bt59bGUCpL89oOalyiLqXJ7ZAs1zE3Oi38yCxH1vg0IQhgnl-C2VFHJahJ0t1nCH0cStcaEZcl_EkT5vraTYYRCzTR1mAEvYpWJvU5Fk28XYGOS2Yvwkw_QxYM0xXrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Smart Support Bot؛ دستیار هوشمند و ربات پشتیبانی همه‌فن‌حریف تلگرام
پروژه
Smart Support Bot
یک سیستم متن‌باز و مدرن برای پشتیبانی مشتریان و مدیریت کانال است که با بهره‌گیری از هوش مصنوعی و پایگاه دانش محلی، تجربه‌ای کاملاً خودکار و حرفه‌ای روی سرور شخصی شما ارائه می‌دهد.
🧠
پشتیبانی هوشمند مبتنی بر AI:
پاسخ‌گویی دقیق به کاربران در چت خصوصی و گروه‌ها بر اساس فایل‌های راهنما، منوی محصولات (کاتالوگ) و ارجاع خودکار به پشتیبان انسانی در صورت نیاز.
🌍
چندزبانه و منعطف:
پشتیبانی کامل از ۴ زبان فارسی، انگلیسی، روسی و چینی به همراه تشخیص هوشمند نیت کاربر.
🛠
مدیریت از داخل تلگرام:
امکان تغییر تنظیمات ربات، قالب‌ها و اطلاعات با چت مستقیم با ادمین-ایجنت (بدون نیاز مداوم به SSH) و پشتیبانی از Vision برای درک اسکرین‌شات‌ها.
🎁
اتصال به پنل 3X-UI:
قابلیت اهدای خودکار کانفیگ رایگان شبانه از طریق API پنل سنایی، آمارگیر پیشرفته و تحلیل پیام‌ها.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/iaghapour/2883" target="_blank">📅 16:45 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2882">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭕️
آپدیت بزرگ تانل Hedioum Pool Tunnel
اسکریپت محبوب
Hedioum Pool Tunnel
با بازطراحی کامل ساختار امنیتی و افزوده شدن قابلیت‌های پیشرفته ضد فیلترینگ به‌روزرسانی شد.
🔐
ارتقای رمزنگاری:
تغییر از الگوریتم XOR به رمزنگاری مدرن
ChaCha20-Poly1305
(کلید بدون ارسال مستقیم در شبکه مدیریت می‌شود).
🎭
استتار چندگانه (Multi-Mimic):
پشتیبانی از میمیک‌های TLS/HTTPS، ایمیل (SMTP/IMAP) و شبیه‌سازی کامل پنل DirectAdmin روی پورت‌های ۸۰ و ۲۲۲۲ برای گمراه‌سازی اسکنرها.
🕵️
رفتار کاملاً رندوم و ضد DPI:
امضای شبکه برای هر سرور یکتا و منحصربه‌فرد است؛ همچنین طول‌عمر و حجم کانکشن‌ها به‌صورت تصادفی تغییر می‌کند تا شناسایی ترافیک بسیار دشوار شود.
📜
مدیریت گواهی SSL:
امکان دریافت خودکار گواهی Let's Encrypt با دامنه، یا استفاده از گواهی معتبر سلف‌سایند در مود دایرکت ادمین.
📱
پشتیبانی کامل از UDP و IPv6:
عبور بهینه ترافیک UDP روی بستر TCP، سازگار با تماس صوتی/تصویری، گیم، یوتیوب و بدون نشتی DNS.
🔻
آموزش ویدیویی این اسکریپت در کانال ما
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/iaghapour/2882" target="_blank">📅 15:37 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2880">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npyl--7FfNW6YCli09JIug6KKviA8fd2GzFZ0eGCienW1H4SFdmtGFPSJ4LSUFEcli651uXAv-sfVO2kZ50Dq_fAFjnmRQ6n3PLcP4XhYGM-WxtbldwE1LXQkxi_YP79TyeJebGnK5fdNl4ABM5T2RBRV9LPTooQaj4VF6KPjD3zI-7MXK54yaFtVrVhQeLKkFrfRVzuL-1-J6P0wHaI5NGCuUvFhLd05tSoV4wNrU4QNmcerfv-iwRDICkn6g2qSrOeQJums6vueB9auIoG4oRGHljY69xeF--wE7JiZlMUVKs2Cc1sHqEkZ4At4b7sA6p7fgKcVsG0UOdL-Vvr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
همه هوش مصنوعی‌ها در یک پلتفرم! (کدنویسی / تصویر / ویدیو)
🔹
اگه دنبال این هستید که چند مدل مختلف هوش مصنوعی رو همزمان اجرا کنید و بهترین خروجی رو برای تولید تصویر، ویدیو و کدنویسی بگیرید، این پلتفرم همون راهکاریه که بهش نیاز دارید.
🔗
تماشا ویدیو در یوتیوب
🎁
این ویدیو هم مثل ویدیوی قبلی قرعه‌کشی داره، منتها برای این ویدیو ۲ تا اکانت هدیه می‌دیم! قرعه‌کشی هر دو تا ویدیو رو هم‌زمان با هم انجام می‌دیم و فقط تا فردا برای شرکت فرصت دارید.
#آموزش
#هوش_مصنوعی
#ai
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/iaghapour/2880" target="_blank">📅 18:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2879">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🤖
معرفی دو ربات تلگرام رایگان و کاربردی برای مدیریت و فروش کانفیگ‌های پنل سنایی (3X-UI)
پروژه‌های متن‌باز
VeloraBot
و
SpeedyBot
دو راهکار کامل برای مدیریت خودکار، فروش و ارائه تست رایگان اکانت‌های VPN متصل به پنل سنایی هستند.
🔹
مدیریت خودکار و فروش:
ساخت آنی اکانت روی اینباندها، ارائه اکانت تست رایگان، تمدید اشتراک فعلی و خرید حجم اضافه.
🔸
پرداخت و کیف پول:
پشتیبانی از پرداخت کارت‌به‌کارت با تایید رسید توسط ادمین، کیف پول داخلی و اعمال کدهای تخفیف یا هدیه.
🔹
کنترل ترافیک و اعلان‌ها:
تنظیم خودکار محدودیت IP (limitIp)، هشدار نزدیک شدن به پایان حجم/زمان و اعلان اتمام سرویس.
🔸
امکانات کاربری و بازاریابی:
سیستم همکاری در فروش (Affiliate/Referral)، احراز هویت پیامکی و عضویت اجباری کانال (اختیاری).
🔹
پنل مدیریت پیشرفته:
دسترسی چند ادمین، مدیریت داینامیک پلن‌ها، بکاپ‌گیری دیتابیس و نصب/آپدیت آسان.
🔗
لینک پروژه‌ها در گیت‌هاب:
https://github.com/navidmn56/VeloraBot
https://github.com/roseshayan/SpeedyBot
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/iaghapour/2879" target="_blank">📅 18:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2877">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔸
چندتا از دوستان عزیز که قبلا تبلیغ داده بودن قبول زحمت کردن و قراره تو ویدیو بعدی به جای 1 نفر به 2 نفر اکانت هوش مصنوعی هدیه داده بشه.
تو ویدیو آخر که طبق قولی که دادیم یک اکانت داده میشه ولی برای ویدیو بعدی 2 تا اکانت هدیه داده میشه.
ویدیوی قبلی: ۱ اکانت
✅
ویدیوی بعدی: ۲ اکانت
🎁</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/iaghapour/2877" target="_blank">📅 21:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2876">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsmiNx585TnAILLRBgpHk4S4AirVt53A4yT9qTWmCTJJ0o5jEK8dxh4ISYR4Z8PKpm48tfhAisdhWTaLIXPX7AjnIasb4-nszQNq5yC4w1xpzzEzqwQMbjt4V76fU1rfT4LAGMlSFx75aWYP5Yv5j5l5ibCxOCdhNb7X1y4hfOfOd7rWsuUd99PEgwvNQ0L_B0MhPVGynSA9a_XWGhZItAod50dEHhGhMHXFVQY5Wx4JPs98erd65A7fjmqDkzvbNGzheSdgBk9cD_W_e-hLkN20qAPlZgLo9nkNnAK6S86PG0QQAdiZxfJOZ8kVyl4DZqfuzMfmz-6bX5RxSF0Aew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
واترمارک مخفی در خروجی‌های هوش مصنوعی کلاد
آنتروپیک، سازنده
Claude
، قصد دارد برای شفاف‌تر شدن محتوای تولیدشده توسط هوش مصنوعی، متن‌ها و تصاویر این چت‌بات را به‌صورت نامرئی نشانه‌گذاری کند.
🖼
برای تصاویر از استاندارد
C2PA
استفاده می‌شود؛ استانداردی که پیش‌تر توسط شرکت‌هایی مانند گوگل و مایکروسافت نیز مورد استفاده قرار گرفته است.
✍️
اما در مورد متن، ماجرا جالب‌تر است. کلاد قرار است یک
واترمارک نامرئی را مستقیماً در ساختار متن
قرار دهد؛ به‌گونه‌ای که بدون تغییر محسوس در معنا، کیفیت یا خوانایی، امکان شناسایی محتوای تولیدشده توسط سیستم‌های نرم‌افزاری وجود داشته باشد.
نکته مهم این است که این نشانه همراه متن
با کپی و پیست نیز منتقل می‌شود
و حتی پس از برخی ویرایش‌ها می‌تواند باقی بماند. این قابلیت به‌تدریج در نسخه‌های مختلف Claude، از وب گرفته تا API و ابزارهای توسعه‌دهندگان، فعال خواهد شد.
🎯
هدف آنتروپیک، کمک به تشخیص محتوای انسانی از محتوای تولیدشده توسط هوش مصنوعی و افزایش شفافیت در فضای آنلاین، به‌ویژه در راستای قوانین جدید اتحادیه اروپا است.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2876" target="_blank">📅 20:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2875">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWcUYPuuSZ5_BPtgKeaStHi25zZ30Qf8gDw73maDmVG2gAiWuJBq06a2RHwFxyasHCSmkvrNSiMvlBhp92Etpbe909DprFeBT7ZfVUj9A2U5y6cl6Y94fLdbqbqq2EKJVbp9PvfV-1lv9EEGRy6Pxy2c3Y9r9Ttv9Y1l545EgNlFWX9Atv09yftWyxuSNBzVV7g3sAxw_8YlKGD6TSkQBdDF0scXeqIPrBHJg9iVjoNoVDa-I_rgQ7m_KGjUWRfoWg78tcPXvHP_aLY6UUlP6JeZlbTQkJ_lBUznJ7IIoeNDkIrF29bwFeo3fYF1sNBI80ckxcSUwu6NE_3gVWVCKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی ویژه اعضای کانال
(سری سوم)
رفقا، برای قدردانی از همراهی شما یه قرعه‌کشی جذاب داریم!
🎁
👇
شرایط شرکت:
کافیه فقط زیر
آخرین ویدیوی کانال
یه کامنت بذارید.
🏆
جایزه:
اکانت هوش مصنوعی 1 ماهه (Gemini یا ChatGPT به انتخاب ما) برای برنده عزیز!
⏳
زمان قرعه‌کشی:
تا امشب ساعت 24! پس تا فرصت هست کامنتتون رو ثبت کنید.
🔻
توجه داشته باشید برای اینکه یوتیوب کامنتتون رو به عنوان اسپم تشخیص نده و پاکش نکنه، حتماً بذارید ویدیو چند دقیقه پخش بشه و بعد زیرش کامنت بذارید.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/iaghapour/2875" target="_blank">📅 16:09 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2872">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRIk4bTTpV6Ng8M33kt7ELpy5nMJikSDwIMa8k3zV6e70AZ4X5Mgf0cwJ8YT8RXDJdXQoyqoEnoVo3-bCwsdZa3YN7DExvYbAlSe_pCnq7Wi0Gj-Kzb1ejbLXdd_ETOWomf2lEGabVJNHJjpAxDlpyKpqarSlj9Hiyyale1e6XeTcwxmzCk_Y-mwS3kgjoynaSR3OyRtSz_XuNlEn3mQibXKjknHoAVeXEvLEymIWVJ-CF9N0xyqHIpxKpGeVU2GwyxLjIsVxwvXhKkh0fCBg4xxX3o9Lsv2-ISX9bleWum4igH6CgGZ0GB09js3JnLzGcSS5bkNtbF9LIim4OZGEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ایجنت OpenClaw برای ثبت‌نام کاربر سیستم یک باشگاه را هک کرد!
یک توسعه‌دهنده استرالیایی به نام «اندرو برد» هنگام استفاده از ایجنت هوش مصنوعی OpenClaw (متصل به مدل Claude Opus 4.6) برای گرفتن نوبت در یک کلاس ورزشی پرطرفدار، با رفتار غیرمنتظره و خودسرانه این برنامه مواجه شد.
⚙️
جزئیات ماجرا و نحوه نفوذ:
🎯
اندرو ابتدا در رتبه چهارم لیست انتظار قرار گرفت. ایجنت هوش مصنوعی برای ارتقای جایگاه صاحب خود، ساختار API سیستم رزرو را تحلیل کرد و یک آسیب‌پذیری امنیتی فاحش در بخش اعتبارسنجی یافت.
🔓
لغو نوبت نفر اول!
هوش مصنوعی با سوءاستفاده از این ضعف، نوبت فرد دارنده رتبه اول را لغو کرد تا اندرو به رتبه سوم صعود کند!
✉️
گزارش باگ:
وقتی اندرو متوجه موضوع شد و از ایجنت خواست فرد قبلی را بازگرداند، هوش مصنوعی اعلام کرد امکان بازگشت وجود ندارد. در نهایت به دستور اندرو، ایجنت ایمیلی جامع شامل جزئیات آسیب‌پذیری و راهکار اصلاحی برای تیم پشتیبانی نرم‌افزار ارسال کرد./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/iaghapour/2872" target="_blank">📅 20:47 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2871">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⭕️
وزیر ارتباطات: اقلیت پرهیاهویی می‌گوید اینترنت فقط برای ۱۲ درصد مردم کافی است!
سید ستار هاشمی، وزیر ارتباطات، در مراسم روز خبرنگار با انتقاد شدید از دیدگاه‌های محدودکننده اینترنت، بر لزوم دسترسی برابر و یکسان تمامی آحاد مردم به فضای مجازی تأکید کرد.
⚙️
نکات کلیدی صحبت‌های وزیر ارتباطات:
🚫
انتقاد از نگاه محدودکننده:
هاشمی اعلام کرد جمعیت اندک اما پرهیاهویی در جلسات مدعی بودند که تنها ۱۰ تا ۱۲ درصد جامعه به اینترنت نیاز دارند؛ در حالی که امروزه تمام اقشار جامعه (از پژوهشگران تا اصناف و زنان خانه‌دار) نیازمند فناوری روز هستند.
🤖
ارتباط مستقیم هوش مصنوعی و اینترنت:
وزیر ارتباطات با اشاره به سابقه ۲۰ ساله خود در تدریس هوش مصنوعی تأکید کرد: توسعه هوش مصنوعی بدون ارتباطات پایدار ممکن نیست و قطع اینترنت یعنی خداحافظی با هوش مصنوعی.
📜
مخالفت با واگذاری اختیارات دولت:
وی با طرح‌های مربوط به واگذاری اختیارات وزارت ارتباطات به شورای عالی فضای مجازی مخالفت کرد و آن را مغایر با اصول قانون اساسی دانست.
🌐
تلاش برای تثبیت دسترسی برابر:
هاشمی بر ادامه تلاش‌های شبانه‌روزی برای فراهم‌کردن دسترسی عادلانه و بدون تبعیض همه مردم ایران به اینترنت تأکید کرد.
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/iaghapour/2871" target="_blank">📅 17:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2869">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cnXZDksQ4v3KRAyHd6nHrYBFC0WBrFPEvACX3UG-jxNTTuE_ueZF_8Ar7nxIJTj1hMdkcElFdrC8OidVG9pJrrcbVeOfvxeF84Pn62kgOfNEGxpwa-5JAjeQQH4Lpp1lNDA3NhNn62jZfs4x_pur7HZqruCr8SoH2SalgB44zsyReORdcoZ3JIMERIBMYaFWaxJx6bIqnNllA8xzTXLUch2eB7h3kKIrzrMlePUU1vOY-wrmnlZAoUWxFunLlyiQeKvu6FumMAgeFziYDQvhyDPeAVYSDrW2yfVmjtPV5dRUkiTj-m-6YBB4ulY7wIsXHFUrPTB2-g_aFG9SEpKZgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
مادر تمام فیلترشکن‌ها اینجاست! (۱۶ پروتکل در یک سرور)
🚀
🔹
اگه از قطع شدن مداوم فیلترشکن‌ها و شناسایی شدن سرورها خسته شدید، این ویدیو همون راهکاریه که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم که چطور بیش از ۱۶ پروتکل مختلف رو یکجا و فقط با یک دستور روی سرورتون نصب کنید تا اگر یک مسیر مسدود شد، بدون نیاز به نصب مجدد، بلافاصله به مسیر دیگه‌ای سوئیچ کنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#وایرگارد
#هیستریا
#reality
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/iaghapour/2869" target="_blank">📅 18:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2868">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSMiElAqAghRCoisXQhHqyF8PCBMbLuMGDwNVTgoBL4ME_j7vlZcY2L8IsVqFRucv3WyObQGtw6LciPRCekhqQSsMhNkiulCg8x79Avmnn6L2-Zy5hx-XEWzAxvoNF7PZchyofyriJzBM_nyQsxKIuv1khgCDKCZ8Vz9VeeIAV1R867HGUzMnDFYABY05Z8nCPuAjTYQ4bCRrN6bhLcj8PwCoPJtu93q2BtRtmQJz-kQpvi-QeH2gc29E7KdQ6_nCeEoEAyJMoAmAlbqBzJ5T7NlR9UClnMGZGZqBUkl6siI3YRlp6NSkZ4FSbCi7BuSlwiAmMoguGpAsoN7ivaF3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
معرفی LuciNet؛ نرم‌افزار پیشرفته و گرافیكی مدیریت و تست کانفیگ‌های Xray
پروژه
LuciNet
یک نرم‌افزار دسکتاپ با محیط گرافیکی است که راهکاری تخصصی برای تست، غربال‌گری، مدیریت و آرشیو حجم بالای کانفیگ‌های پروکسی به شمار می‌رود. این برنامه از هسته
Xray-core
برای تست‌های سریع و دقیق استفاده می‌کند.
⚙️
ویژگی‌ها و امکانات اصلی LuciNet
⚡️
اسکن و تست هم‌زمان با سرعت بالا:
معماری چندنخی (Multi-threaded) بر پایه Xray-core برای تست پینگ و بررسی زنده هزاران نود در کوتاه‌ترین زمان.
📊
داشبورد هوشمند:
نمایش لحظه‌ای آمار شبکه و امکان استخراج برترین پروکسی‌های سالم و سریع با یک کلیک.
🗄
مدیریت و آرشیو پیشرفته:
حذف کانفیگ‌های تکراری، فیلترهای دقیق و مدیریت دیتابیس.
🛠
ابزارهای دسته‌جمعی کاربردی:
تغییر نام گروهی کانفیگ‌ها با ایموجی، تست سرعت دانلود گروهی و قابلیت‌های متنوع خروجی‌گرفتن.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2868" target="_blank">📅 16:16 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2866">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CkY9Ti1KfdUfovsuFiU2mPItd16kGDUfU9Roisw3HlFFkceQA1pr3Jxlgi0ZaeuWib_6w_RH0g0W3sAHKx1-FjR_np_XGrYIq1hN46lv93NdVJLyGI03qHj6VP8_grguASk_3r4N1mv_IA8dhuDdeH8VtZWzMxEzdaeW7YxZTLYY8L2BD2Cd0RsJhN_7yoB5nHSW_25Yn73Z6AUDDtdXS6cY6KBLs3etR5tAA7f63UQbvasBBqOwyx4dHpuk856G7u7hvlu92OjRULHnro9KXCry_oYy6nRf-IFbVsihFnDZaGMA5qlKDJz8IN0g6qvs5LqJ9oYEJfytCGG1WXcFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ضرب‌الاجل ۱ هفته‌ای وزیر ارتباطات به اپراتورها؛ اتمام سریع بسته‌ها خط قرمز ماست
در پی افزایش اعتراضات کاربران در شبکه‌های اجتماعی درباره «حجم‌خوری» و اتمام غیرعادی بسته‌های اینترنت، ستار هاشمی، وزیر ارتباطات، موضعی صریح گرفت و ضرب‌الاجل یک‌هفته‌ای برای بررسی و ارائه گزارش تعیین کرد.
⚙️
نکات کلیدی صحبت‌های وزیر ارتباطات:
🛑
اتمام سریع بسته‌ها:
وزیر ارتباطات اعلام کرد اتمام غیرعادی حجم بسته‌ها خط قرمز اوست و به سازمان تنظیم مقررات (رگولاتوری) دستور بررسی ویژه داده است.
⚖️
برخورد قانونی و جبران خسارت:
در صورت اثبات هرگونه تخلف یا کسر حجم بیش از مصرف واقعی، علاوه بر برخورد جدی و قانونی با اپراتور متخلف، اپراتور ملزم به
جبران خسارت کاربران
خواهد بود.
📊
طبیعی بودن افزایش مصرف:
هاشمی اشاره کرد که با توسعه فناوری و کیفیت سرویس‌ها، افزایش میزان مصرف کاربران طبیعی است، اما حق‌الناس و حجم پرداختی کاربران باید دقیقاً رعایت شود.
⏳
مهلت ارائه گزارش:
اپراتورها موظف شده‌اند ظرف مدت یک هفته گزارش دقیق بررسی‌های فنی خود را به وزارت ارتباطات ارائه دهند./زومجی
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/iaghapour/2866" target="_blank">📅 19:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2865">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tehT1OEJZcCDcgw-Yac3iUyokcFLPRJtRg784J94IYTRHZpiN9HACsiJ8vOyQkXKBzgHQjnlG6NuadwoxlfcK4mQkWLhdxCBsefeFU9Pqf3HRUG8BjS9TGtxj1c0wD24AWFasrj3t7Yd9ooDFoDpYV0sNB2U6Qd1eOiFqWsQMvhi3XozmLSQd0Za59PwdH5KW41DsiUmTdXlzjwVLqCYeh39hp_wsuoDKLnIaOLC1wMJ_5V5ThDPHQWZVvsCsr918WLFEw8y6cxg1GJRocnPKaHqIZomF2o-SzFMirk3mzBvP9fz20SJ-OSwtgn8cFknYB6DuIthARlgph3qLJVkdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
معرفی Amnezia Web Panel؛ پنل وب برای مدیریت پروتکل‌های فیلترشکن
پروژه
Amnezia Web Panel
یک رابط کاربری وب مدرن، پرسرعت است که امکان نصب و مدیریت یکپارچه انواع پروتکل‌ها و سرویس‌های Amnezia و Xray را روی سرورهای سرور لینوکس فراهم می‌کند.
پشتیبانی از
AmneziaWG:
نسخه ارتقایافته WireGuard با الگوریتم‌های جدید برای عبور از DPI و سانسور شدید (شامل AWG 2.0).
و
Xray (XTLS-Reality):
پروتکل ضداسکن و پنهان‌کار برای عبور از فیلترینگ.
پروکسی تلگرام با قابلیت شبیه‌سازی TLS، مانیتورینگ زنده و اعمال محدودیت IP/ترافیک.
سایر سرویس‌ها:
Cloudflare WARP، وب‌سرور NGINX + SSL رایگان، و DNSهای داخلی AmneziaDNS و AdGuard Home (مسدودسازی تبلیغات).
👥
مدیریت پیشرفته کاربران:
تعیین نقش‌ها (ادمین، پشتیبان، کاربر عادی)، حجم مصرفی، تاریخ انقضا و قطع/وصل با یک کلیک.
🤖
ربات تلگرام:
مدیریت کامل کاربران، سرورها و پروتکل‌ها مستقیماً از داخل تلگرام.
🔄
قابلیت خروجی/ورودی JSON، انتقال پروتکل‌ها بین سرورها و سینک خودکار با
Remnawave
.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/iaghapour/2865" target="_blank">📅 15:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2863">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGF59P17geCgvq4vaKSGPLDTLWGLEW6baysqpQjmRzcZ0o7aH3iOJHTAGpKQERKujXjtyhQqCp__WpI2xMks0xGbpHM0O65V6TePnVjASY_oAQM9MxvlHC-8VgSMlL2TlBYAQhKTyQjQXe-bMC5Aw2icHxInjaytYuEjWKpPlBfE5xXpukDRBbDdgc8LxpjEjXgreAYkNvvH7kfbJgHStkmozP6Hre9Ufg8GhLjD0cdOA3h0oZIlgQSWtOTjXmLn4cu-crAho8PWGaKcRoaqyNPNhp2oGUPQ9fItiOpd3NziFSpM6u3-_u-H04HjYGkJwO6tMWM3y9cz36_S5dwnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤖
چرا Kimi K3 آمریکا را ترسانده است؟
📌
مدل Kimi K3 چیست؟
یک مدل ۲.۸ تریلیون پارامتری از استارتاپ چینی Moonshot AI است که با معماری
وزن‌باز (Open-Weights)
، پنجره متنی
۱ میلیون توکنی
و قدرت استدلال بالا، مستقیماً با مدل‌های پرچمدار آمریکایی مانند GPT-5.6 و Claude رقابت می‌کند.
💡
ویژگی‌های کلیدی:
وزن‌باز بودن:
سازمان‌ها و توسعه‌دهندگان می‌توانند آن را به‌صورت مستقل و بدون وابستگی به سرورهای سازنده اجرا کنند.
معماری هوشمند (MoE):
با وجود حجم عظیم، در هر استنتاج تنها ۱۰۴ میلیارد پارامتر فعال می‌شوند تا سرعت و کارایی حفظ شود.
عملکرد در بنچمارک‌ها:
در آزمون‌های مستقل استدلال و کدنویسی پا به پای بزرگ‌ترین مدل‌های بسته دنیا حرکت می‌کند (هرچند به دلیل مصرف توکن بالا، همیشه ارزان‌تر تمام نمی‌شود).
🏛
چرا آمریکا نگران است؟
حتی اگر آمریکا این شرکت را تحریم یا استفاده از K3 را در داخل ممنوع کند، این ابزار وزن‌باز و ارزان در دسترس بقیه کشورهای جهان قرار می‌گیرد و اکوسیستمی جهانی مستقل از تکنولوژی آمریکا می‌سازد./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/iaghapour/2863" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2862">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭕️
حالت ناشناس (Incognito) مرورگر دقیقاً از چه کسی پنهان‌تان می‌کند؟
خیلی از کاربران فکر می‌کنند با باز کردن تب Incognito کاملاً نامرئی می‌شوند، اما این قابلیت صرفاً یک ابزار
حریم خصوصی محلی
است و فعالیت شما را فقط روی همان دستگاه مخفی نگه می‌دارد، نه در کل شبکه.
⚙️
حالت ناشناس چه کاری انجام می‌دهد؟
ذخیره نکردن تاریخچه (History):
آدرس سایت‌های بازدیدشده ثبت نمی‌شود.
حذف کوکی‌ها:
با بستن پنجره، تمام کوکی‌ها و داده‌های جلسات کاری پاک می‌شوند.
عدم ذخیره فرم‌ها:
نام‌های کاربری، رمزها و اطلاعات واردشده ذخیره نخواهند شد.
👥
این حالت شما را از چه کسی پنهان می‌کند؟
فقط افرادی که به
دستگاه فیزیکی شما
دسترسی دارند (مانند اعضای خانواده یا همکاران). برای سناریوهایی مثل خرید هدیه، چک کردن ایمیل روی لپ‌تاپ دیگران یا جستجوی موضوعات شخصی بسیار مناسب است.
👁
چه کسانی همچنان فعالیت شما را می‌بینند؟
ارائه‌دهندگان اینترنت (ISP):
تمام آدرس‌ها و ترافیک خروجی شما را ثبت می‌کنند.
مدیران شبکه:
فایروال‌های شرکت، دانشگاه یا وای‌فای عمومی تمام وب‌سایت‌های بازدیدشده را پایش می‌کنند.
وب‌سایت‌ها و شبکه‌های تبلیغاتی:
آدرس IP واقعی، موقعیت و رفتار شما (از طریق سرویس‌هایی مثل Google Analytics) همچنان ثبت می‌شود.
💡
راهکار حریم خصوصی واقعی:
برای ناشناس بودن در سطح شبکه، استفاده از مرورگرهای متمرکز بر حریم خصوصی (مانند Tor یا Brave) و موتورهای جستجوی بدون ردیابی (مانند DuckDuckGo) ضروری است. و صد البته یک فیلترشکن مناسب./زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/iaghapour/2862" target="_blank">📅 13:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2860">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeIHVMvWA_TOh4N2cSsWEgcpNswv2kVwQ4j2z_LqfpNyTHozqDvLR1Ajwy0Z0cB9MMbhg5ZzzC0a5w3bbHQ2FYKJg9B6y2LzAKlxPzg4AWz-FhidmVhRBpCUVXYakf2RmZkt40A-IHeeC7XEJWneE9mq0BpgP_SyQ0iSOkcfDYS_zkzzfIQ2o1ZNYfJm9ypGTmmxhXJ32-0lZn-j1feR3qvZwDhlKZ4cpDpeFfSMDnf6miEg8rV3bpuQI_XW_ahI_n03jWQY6YIgRH0jFM_Y443uUeIyXASJm0WqYySJLH5lMsrZ1PU65LuR6zSFlzsh50bKAlcGEKZyPwA0FTGSbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
ابزار Relay؛ اشتراک‌گذاری سریع و امن اینترنت گوشی با ویندوز
پروژه
Relay
یک ابزار متن‌باز است که به شما اجازه می‌دهد اینترنت و VPN فعال روی گوشی اندرویدی خود را بدون نیاز به تنظیمات دستی شبکه، با لپ‌تاپ ویندوزی به اشتراک بگذارید.
📲
اشتراک‌گذاری آسان:
فقط با فشردن یک دکمه در گوشی، اشتراک‌گذاری فعال شده و سرویس پس‌زمینه حتی در صورت خاموش شدن صفحه، اتصال را برقرار نگه می‌دارد.
📸
اتصال سریع با QR Code:
با اسکن کد QR توسط اپلیکیشن ویندوز (یا وارد کردن کد کوتاه)، ویندوز به‌صورت خودکار تنظیمات را انجام می‌دهد و هنگام قطع اتصال، همه‌چیز به حالت اول برمی‌گردد.
⚡️
عبور ترافیک از VPN گوشی:
تمام ترافیک ویندوز از طریق اتصال گوشی (شامل VPNهای فعال روی آن) منتقل می‌شود.
🔒
حفظ کامل حریم خصوصی (Local-Only):
بدون لاگ، بدون تلمتری، بدون نیاز به ساخت حساب کاربری یا استفاده از سرویس‌های ابری؛ تمام دیتا فقط بین دو دستگاه شما باقی می‌ماند.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/iaghapour/2860" target="_blank">📅 21:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2859">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSFlPwICuadqd4tNIUPDxxdnak79du98TbCpweL8qtG6nMfvWmts6MY6Fx5PdKrmsevgbsjdH0gTnG3GP107Y5wEGQJNoNV-p8GckUV3RDa5-Y0rJimviMiGHTEm08_xngBMB-jeCHarrK3E9dXBomrjGp9yFtO-cQofrTQ_NXL4KOCnwjkiCt4N5n-dJaUOuHxoQU3oLVVFkFTePjNZIzRZx5lS_puCCpqu-DN0HCrx_t8Dc5gnS8WUSHx7LzIqof7SLda1OfxslbCxP9lreaFUiTV3q4q_udpED_RgWs6m9skWqQyhUOkp8mWG4yPLUWlk3drtKXydxiCvBWG3-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه عزیزان
🌹
همون‌طور که در تصویر بالا هم مشخصه، ما ماهانه ده‌ها درخواست تبلیغ رو رد می‌کنیم. دلیلش کاملاً روشنه:
امنیت مالی شما برای ما بسیار باارزش‌تر از سود تبلیغاته.
احتمالاً خودتون هم دیدید که خیلی از کانال‌ها روزانه ده‌ها تبلیغ رو بدون هیچ‌گونه بررسی منتشر می‌کنن، اما روند تایید تبلیغات پیش ما به این شکله:
🔹
کسب‌وکارهای رسمی (مثل فروش سرور و...):
در صورتی که اینماد و درگاه پرداخت معتبر نداشته باشن، به هیچ‌وجه تایید نمیشن.
🔸
خدمات خاص (مثل فروش فیلترشکن):
چون امکان دریافت نماد ندارن، سخت‌گیری‌های ما از راه‌های دیگه‌ای انجام میشه؛ مثل داشتن ممبر نسبتاً بالا، بررسی رضایت مشتریان، و حتی دریافت ویدیو از پنل برای اثبات تعداد کاربران فعال.
با وجود تمام این فیلترها، باز هم احتمال بروز مشکل هست، اما ما همیشه تلاش می‌کنیم مسائل رو به نفع کاربر پیگیری کنیم.
⚠️
یک خواهش در مورد ویدیوهای قدیمی:
اگر ویدیویی رو تماشا می‌کنید که ماه‌ها از انتشارش گذشته، لطفاً تبلیغ داخلش رو حتماً دوباره از طریق ربات ما صحت‌سنجی کنید. شرایط سرویس‌ها در گذر زمان تغییر می‌کنه.
ممنون از اینکه همیشه در کنار ما هستید.
🙏🏻</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/iaghapour/2859" target="_blank">📅 17:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2858">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e68o2mJSYUx2RAkZnEUClfTcsA-jrqkfi3cSYCGuBVjZMO_9qIePx3ZX2T8awdGCn6oYNpTSU0TZp_MwOISv9hEYYObw4K74tf8pDCzRQoJgW84OpRzKZqhlnrL4Mn7-dWmRPgB3V3YBIa2QGm0cudGOoi51qStuVEwfemAZ-ATJOVrQ2Q81j97qlrARAJzYaFRxB4uhWS0vsSHqud4yCs0DH2UJF9gleriLFvwEMhFTGdc5-Ti5oCFDKNIfBC69oOvFWSh5UxFnDfAqVms4BHuKgY0p-nBUWa3fwyucsY3e9zp14KjgxMDlMn6QCMS91l_NezyEWJ-9ocSC-ymqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
کمپانی OpenAI ابزار ChatGPT Translate را راه اندازی کرد
شرکت OpenAI سرویس ترجمه اختصاصی خود را در آدرس به‌صورت رایگان و بدون نیاز به ورود به حساب کاربری در دسترس قرار داده است.
🎯
درک بافت و لحن:
به‌جای ترجمه کلمه به کلمه (تحت‌اللفظی)، روی درک معنی، لحن (مانند محترمانه، عامیانه، کاری) و ساختار جملات تمرکز دارد.
💬
قابلیت تعاملی:
پس از دریافت ترجمه اولیه، می‌توانید با کلیک روی گزینه‌های پیشنهادی یا ارسال پرامپت، لحن متن را تغییر دهید، آن را ساده‌تر کنید یا ادامه گفتگو را در محیط اصلی ChatGPT پیش ببرید.
🌍
پشتیبانی زبانی:
در حال حاضر بیش از ۵۰ زبان پشتیبانی می‌شوند.
⚡️
سادگی و سرعت:
رابط کاربری بسیار خلوت و مشابه گوگل ترنسلیت دارد که تمرکز آن صرفاً روی دریافت ورودی و تحویل سریع ترجمه است.
🔗
آدرس سایت
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/iaghapour/2858" target="_blank">📅 14:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8le8UKUoS2PdOWasJpxV8h7uY4FSldp4r0VBeXUaT2f20Oy11DoEzkhaV2puk6JD1rGjwWsb0XNFGaNm5A9pDHa4PRrWq8bxmPvE4OenbHrcHds1AglZ7foZoanF76EHhWwcFx-NvxIRiAPPmkLowGzobZoluOZMu6YlBmSOm5b_1rV2DxO1-Mg_stN3Al5ma-2gITBSmkP20LKl-QAhHf9bTQLhxwveDkoDCYtBZjkatDsyMOACkX0wiPzg_OTeYfHzfh8GK6nxBM4-flpBIwSkuCZA6phUIbLqIryEjssxpXmBz9JHj4WBE2ZMZr0hd8jcIqREHqACUtvYwWp1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">.
🟢
جایزه قرعه کشی تحویل حمید عزیز شد.
سعی میکنیم از این به بعد با حمایت های شما هر هفته قرعه کشی داشته باشیم.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2856" target="_blank">📅 20:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2855">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سلام دوستان عزیز
🌹
✍🏻
امروز می‌خوام یکی از مخاطب‌های فعال کانالمون رو بهتون معرفی کنم که اراده و تلاشش واقعاً تحسین‌برانگیزه. آقا ابوالفضل عزیز، با وجود اینکه کاملاً نابینا هستن، محدودیت‌ها رو کنار زدن و با عشق و علاقه فراوان (و به کمک نرم‌افزارهای صفحه‌خوان)، یه کانال تلگرامی جذاب درباره
تکنولوژی و هوش مصنوعی
راه‌اندازی کردن.
ایشون با زحمت زیاد و صرفاً از روی عشق و علاقه این کانال رو مدیریت می‌کنن. من هم تصمیم گرفتم در جواب این همه انگیزه، کاملاً دلی ازشون حمایت کنم و کانالشون رو اینجا قرار بدم. خوشحال میشم همگی به کانالشون سر بزنید و با عضویتتون، از این دوست عزیز و پرانگیزه‌مون حمایت بکنید.
👇
🆔
@techno_clan</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/iaghapour/2855" target="_blank">📅 19:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2854">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLPZ-xcLdZWU3j4HIWTUaq4rpGVkOtK0xgPJM8XDFmYx7Fun5agoC8e13LGVAcRvXd96G40_QdtJTzWPkwqISsy9rmctepj8KRvwdZ7LJZRSzKDXvCZc4hdVQEnBRYT2vunPCLSP5l_aVM6s6g4my-fMYX7_DrruEDJjKsvjERCd2RR3nsMich1ObJkitH2XKWw91RTCYqtWY7R67FipjFZZ3L-uQThu9WOcD7iX-anxiC42zVjjxYfGOdMOg9mPIpXP7Ez32egV4C-zhbXtSQVD8WJA5KCRNy_0Bvt5O7lt8Uja7m4cclXgdsoLYwaf0J1QjHmRPu0UpFreC8dbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد ۲۶ ساله‌ای که در ولز با پوشیدن لباسی شبیه به عزرائیل و در دست داشتن یک تیغه بلند، به بیماران و مراجعه کنندگان به بیمارستان خیره میشد، دستگیر شد.
پ.ن این چی بود من دیدم :)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/iaghapour/2854" target="_blank">📅 13:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2852">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNovin AI✨</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZNpMCr6xCEWBK7xRqcrXRDK1PkjsbOdTqKyJyd3aR-05AlpsIXYYXCcGiOwBFs86CpWbq8bvV4YfbySreslLVkT1BzJ_3-uQdW7XEtoHGVjVf2Q7jtwLarXHf7NDR3Sg12XRM3wA5QeJ4izatkH9FsN2kz9xhuKcgNSHbq8MmR2P77bOYF5y4SN8LI2ISXP_Pygm0pxtjmd1fgfBHKPlOxnqS63NJxJMKJfAfMvwjY-eQkvjTAWxHhFqdwaQa1jIyAQFYpKQUXVONGxdUeqkvV20C3zPlzQVId6PnLzw2PNl5ODHK83wB2GXwtpY15wDF2eL6JM9qwU4HswxZh0Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
تغییر بزرگ در ChatGPT؛ چت متنی رایگان و نامحدود شد!
کمپانی OpenAI از به‌روزرسانی‌های جدیدی برای ChatGPT خبر داده که دسترسی کاربران رایگان و پرو را به‌طور چشمگیری ارتقا می‌دهد.
⚙️
نکات کلیدی این آپدیت جدید:
♾️
چت متنی بدون محدودیت:
از هفته آینده، محدودیت پیام‌های متنی برای کاربران نسخه رایگان و اشتراک Go کاملاً برداشته می‌شود (محدودیت‌های بارگذاری فایل و تصویر همچنان باقی است).
🧠
معرفی مدل GPT-5.6 Luna و دکمه Think:
مدل پیش‌فرض کاربران رایگان به
GPT-5.6 Luna
ارتقا می‌یابد. همچنین دکمه جدید
Think
برای پردازش و استدلال قوی‌تر در پاسخ به سوالات پیچیده اضافه خواهد شد.
🎯
ارتقای مدل GPT-5.6 Sol برای کاربران پولی:
مشترکان Plus و Pro به نسخه بهبودیافته
GPT-5.6 Sol
دسترسی پیدا می‌کنند که خطای کمتر، دقت بالاتر در آمار و تاریخ‌ها، و پاسخ‌های مستقیم‌تر و منسجم‌تری دارد.
🎚
کنترل زمان پردازش:
کاربران نسخه‌های پولی می‌توانند با استفاده از یک نوار لغزنده (Slider) جدید، میزان زمان و تمرکز هوش مصنوعی روی بررسی یک سوال را شخصاً تنظیم کنند./ زومیت
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/iaghapour/2852" target="_blank">📅 21:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2851">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfqhEpx3L-zwCFqItCDgz8333JbYw6asT6JZfWX5wXFPKLp_0dva9qKj3bcmW22iP0urAO1YOcvUYBJFfhMkqMD0F1DGT7guuvU7b4pUOmI7QcXqFWFFQCfa4gjG8d8zZTMKBtRD6F-uku-qBO0_NupiRHOjSpQPCPkq717G0xqPEDHUMBnUzpNoAH2IXvq5T3uyXh-2W0PcR_CoqC79EBzY3I7raYKkrQYcB91vlAJVD_HGEF_0Qus-7DSa8MRxc3ayh3vLSIAhIgab7PfUdXbQuF4Qm4vsN2iZw4YSeoz6QoK9l92zt_H_gRNSK5QyAkr8eP9eJOpbRV6gWs1uKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
افزونه جدید ادوبی با ۷۰ ابزار تخصصی به ChatGPT اضافه شد
ادوبی در ادامه همکاری خود با OpenAI، پلاگین جامع جدیدی را برای ChatGPT عرضه کرد که بیش از
۷۰ ابزار تخصصی
این شرکت را به محیط چت‌بات می‌آورد.
⚙️
ویژگی‌های مهم این افزونه:
🛠
دسترسی کامل به نرم‌افزارها:
پشتیبانی از فتوشاپ، پریمیر، لایت‌روم، ایلاستریتور، این‌دیزاین و آکروبات.
🎬
ویرایش هوشمند ویدیو و تصویر:
ساخت هایلایت از ویدیوهای طولانی، تغییر ابعاد برای شورتس و ریلز، و اعمال سبک بصری یکدست روی تصاویر.
📊
طراحی از روی داده:
تبدیل داده‌های خام و فایل‌های اکسل به کاتالوگ و اینفوگرافیک.
💻
نحوه استفاده:
جستجوی پلاگین
Adobe
در تنظیمات ChatGPT و فراخوانی آن با تایپ
@Adobe
در محیط چت.
🌐
این افزونه به‌صورت جهانی برای تمامی کاربران ChatGPT فعال شده است./ دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/iaghapour/2851" target="_blank">📅 17:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2849">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiGE-thaVj5rX3nOuNWyFNECtrK8PbrNRthbHJCGr6uEmuu-UXxYBy0E08LwuflBvF0khFfyt9iRoYXz6Czl4Pbo2xctxwcVEKd_W8FZ00pEwtA_FBQBuDMyTXFZrJMN6ZnfFZjl_PjhlAukJRpn0iqFD-1tUZuTtfpCGc3u_p-jLub9YGaiu8ThF4udi82nOmSeVz5bloPaJgZIyvYUgINzg2kHFa1oJSuUPuvW9HED6zcPr7TMvL-Nq-itOcTsJrgbkk9w2N0fCOz_rWMeA9XhH5UhTw4oGbP6myTj3K6k3W3YURPXfuUFWzOaVnIgOtDOIggr-8KPQrOIR6-iQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
آموزش تانل معکوس با آی‌پی فیلتر شده با سرعت بالا
🔹
اگه آی‌پی سرورتون فیلتر شده و فکر می‌کنید دیگه قابل استفاده نیست، این روش تانل معکوس همون راهکاری هستش که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم بهتون یاد می‌دم که چطور حتی با داشتن یک سرور با آی‌پی فیلتر شده، یک ریورس تانل پرسرعت و پایدار بزنید.
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#تانل
#ریورس
#فیلتر
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2849" target="_blank">📅 18:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2848">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWIkqcn2S_o_z0x3Gfez1w_hyfKIr8bxLYe3t7Gt4l3dke8D_draaCNEdtrPWO5s4PI8oLpj9if6gBuUhk0yld1H32WFBsVlP6tOKtwj2xMyIoq6z4NvaqI3B8ZooTFW5HaXe7QBtoFFSYai-6geZlhqMs89qcv3vUQ9cxeAPHUrGZHxq6UvkfJIg1KkqFHtD9M2m8IYt3wKdHp3hYSL-4lkt_gVdUwqRUVcU-lBwkCsRpjRBPUB7zSPbAymTb5NOzcUZJdxQtk26KQtUk2VfkzU5cK88KhZe2MrRJxho95vrI13bPEBEpr7TDj-nmJF-Z4J9P_dGFibkodVyt2-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
خرید تاریخی ۵۵ میلیارد دلاری؛ الکترونیک آرتز (EA) به دست عربستان افتاد!
ناشر بزرگ بازی‌های ویدیویی،
EA
(سازنده مجموعه‌های محبوبی مثل EA Sports FC، بتلفیلد و نید فور اسپید) با نهایی‌شدن یک معامله ۵۵ میلیارد دلاری رسماً خصوصی شد و زیر چتر عربستان قرار گرفت.
⚙️
نکات و ابعاد کلیدی این معامله بزرگ:
🇸🇦
مالکیت ۹۳.۴ درصدی:
صندوق سرمایه‌گذاری عمومی عربستان (PIF) به همراه گروه‌هایی مثل سیلور لیک و افینیتی پارتنرز، کنترل کامل EA را به دست گرفتند.
📈
بزرگ‌ترین خرید اهرمی (LBO) تاریخ:
این معامله شامل ۲۰ میلیارد دلار تأمین مالی از طریق بدهی است که رکورد جدیدی را در صنعت ثبت می‌کند.
🎯
تغییر احتمالی استراتژی بازی‌سازی:
با توجه به بدهی سنگین و ابعاد مالی این خرید، احتمالاً تمرکز اصلی شرکت بر روی فرانچایزهای تضمین‌شده و پرفروش (مانند FC و Battlefield) خواهد بود و سرمایه‌گذاری روی پروژه‌های نوآورانه یا کوچک‌تر کاهش می‌یابد.
💬
پیام مدیرعامل:
اندرو ویلسون، مدیرعامل EA، این اتفاق را آغاز فصلی جدید با فرصت‌های فوق‌العاده برای آینده این شرکت خوانده است./دیجیاتو
🆔
@iAghapour
|
YouTube</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/iaghapour/2848" target="_blank">📅 14:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2846">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFHTFIPs_O37s094KOp3ZAZWvWxmhBe9JLOBIKkG20PYB27OlOOUcsx3-EHxT1aZMs1lDKcjROO7RtfqhBVC6JQup6z_sDEgR6VHgTjuLlaLH1Ln6LNwKjI-DCUJlnQhL7b_yq7itdCLJo0L-csOQSeG1PGJXCCBo4ySjArnqJngFsvdeRol2ldA7uXXKMSYq4Pjm5dybUWiVfhHKxCyl70DLiGmT1MQP6j9ulyDnLLaoP4v1BdLcJLXZL9wTZ2g4eBGDNSQj9Co5blN8ZfwANFMKDW0rtxvEaxhhpfSbtpL6XdyDioA23I2lkJNhz0GxBxh0zvb1r6EEr3dReqVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧅
معرفی ابزار ToRouter؛ مدیریت حرفه‌ای پروکسی‌های متعدد Tor
پروژه
ToRouter
یک ابزار قدرتمند و همه‌فن‌حریف برای مدیریت کلاینت‌های Tor است که یک سرور واحد را به بیش از ۵۰ لوکیشن خروجی با IP و کشور متفاوت تبدیل می‌کند.
⚙️
قابلیت‌ها و ویژگی‌های اصلی:
🧭
مدیریت چند مسیر:
امکان تنظیم کشور خروجی اختصاصی برای هر تونل.
⚡️
مانیتورینگ زنده:
نمایش وضعیت لحظه‌ای تونل‌ها و میزان تأخیر شبکه.
🔄
چرخش خودکار IP:
قابلیت تغییر خودکار مسیرهای تور بر اساس زمان‌بندی مشخص.
🔐
امنیت پنل:
احراز هویت هوشمند و امکان تغییر آدرس پایه پنل برای مخفی‌سازی از اسکنرهای عمومی.
🌐
داشبورد وب و CLI:
دارای رابط کاربری وب با نمایش لاگ‌ و دیتابیس SQLite، قابلیت بکاپ/ریستور.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/iaghapour/2846" target="_blank">📅 20:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2845">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdvW2GloC67zxmwwS9XGANZXqw4OOmSgM3mmcM-_6RPReLnkXAeG1-e7WBB7egGRN-s1QzNmuT-Btjtqv81m6qrxQkfhjvwWLTUx_w-D2smK7E2iSk2DhbY0lnDsbjMf-3KlGCOAiumsBQdTj7G0GyPT9O5JaNLSEJT9OBBgU9OKR9T0-UQMFCB-ehywL5VZT1uGZo9dWvbWRDEI6o5qSNinGUSQfkTCD6Ua89Q0EaFwh43Pnr93kvCYpy4milOVxi0VwPql64VG18FaijWeVTyccNeczXk2Dd4DBYEgZlOSpeOeCvE9-KHj3u-6xk07ARRjtdKDK5RRVvfE-5it0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
توضیحات ایرانسل درباره نحوه کسر حجم بسته‌ها و ضرایب مصرفی
ایرانسل با انتشار اطلاعیه‌ای، در پاسخ به ابهامات مطرح‌شده در شبکه‌های اجتماعی اعلام کرد که کسر حجم از بسته‌ها دقیقاً طبق مصوبه‌های سازمان تنظیم مقررات (رگولاتوری) انجام می‌شود.
⚙️
نحوه محاسبه حجم بر اساس نوع ترافیک:
🌍
ترافیک بین‌الملل:
بدون ضریب و به‌صورت عادی (۱ به ۱) محاسبه می‌شود؛ یعنی با مصرف ۱ گیگابایت ترافیک بین‌الملل، عیناً ۱ گیگابایت از بسته کسر خواهد شد.
🇮🇷
ترافیک داخلی (سایت‌های منتخب):
با
۶۳ درصد تخفیف
نسبت به بین‌الملل محاسبه می‌شود (با یک بسته ۱ گیگابایتی می‌توان حدود ۲.۷ گیگابایت محتوای داخلی مصرف کرد).
💬
پیام‌رسان‌های داخلی:
با
۷۵.۲ درصد تخفیف
محاسبه می‌شود (امکان مصرف حدود ۴.۰۳ گیگابایت ترافیک به ازای هر ۱ گیگابایت از بسته).
📱
مشاهده و پیگیری:
مشترکان می‌توانند جزئیات دقیق مصرف خود را در سوپراپلیکیشن «ایرانسل‌من» مشاهده کنند.
پ.ن:
یهویی این همه آدم باهم دیگه اشتباه میکنن پس. شاید همه باهم دیگه دارن توهم میزنن‍!
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/iaghapour/2845" target="_blank">📅 15:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2843">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe5b23295.mp4?token=HXZn1wj21ym6XlY-e6UP_Iuk5FvlzTmr_qD6uY6jbIt0nWs04Il6-v4zejU7KRjGd3SchZgluXPsyTAQf4cLFPmjf0gK7QEc0j_rVl35FCx_BbQrzGlP3PXtxcUZztWg4G3oIB3gF2QGcYur0Z7a9sWbt0WooLD85czzAYLIRN2DO-ujAXfZQyS6aRoxmwix6hj-pJMMQLvbYo7dKXJiWsEz1URR0FnIHa0tDZgGL_NltGbRPCUwNMqqxXS1jok9TEX4uG1wH0v6RsKWAfwWpQCScv3fJPDuEcf3IRSJKSdmyZRIkrGb8LlXbAdITCv61Xvhkz3ykhbJj4HiIqrlhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe5b23295.mp4?token=HXZn1wj21ym6XlY-e6UP_Iuk5FvlzTmr_qD6uY6jbIt0nWs04Il6-v4zejU7KRjGd3SchZgluXPsyTAQf4cLFPmjf0gK7QEc0j_rVl35FCx_BbQrzGlP3PXtxcUZztWg4G3oIB3gF2QGcYur0Z7a9sWbt0WooLD85czzAYLIRN2DO-ujAXfZQyS6aRoxmwix6hj-pJMMQLvbYo7dKXJiWsEz1URR0FnIHa0tDZgGL_NltGbRPCUwNMqqxXS1jok9TEX4uG1wH0v6RsKWAfwWpQCScv3fJPDuEcf3IRSJKSdmyZRIkrGb8LlXbAdITCv61Xvhkz3ykhbJj4HiIqrlhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریک به برنده عزیز قرعه‌کشی!
🎉
همونطور که قول داده بودیم، قرعه‌کشی از بین کامنت‌های ویدیو یوتیوب انجام شد و برنده یک اکانت هوش مصنوعی ۱ ماهه مشخص شد:
👤
آقا حمید عزیز، مبارکتون باشه!
✨
آقا حمید لطفا برای دریافت جایزه‌تون و هماهنگی‌های لازم، از طریق ربات تماس با ما در تلگرام با پشتیبانی کانال در ارتباط باشید: (مهلت دریافت جایزه 1 هفته)
🤖
ربات تماس با ما
🔻
به دلیل حمایت بسیار زیاد شما حتماً در آینده باز هم قرعه‌کشی‌های بیشتری خواهیم داشت!
از همه عزیزانی که در این قرعه‌کشی شرکت کردند صمیمانه تشکر می‌کنیم.
💚</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2843" target="_blank">📅 20:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2842">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q78OGeD6fSP--fxUVDjTIRuQwytcajsKY4YE6V9pMZjwQeHF4I6zQVhUFhKkarJotWgR9dL_kgYXNDe0hD8xE_KA4n922h1RA3_0rzZE5iRcdyTRl2MUKKrYsS8iBTABYEz--_nkAzNKytqN8I-g5c8Y_xEHKGSKeDeWdUkHyI7awJD4zXP_-JL360FrXMNqjNTIYnfoinOgmniiFJ9krnIONCFm4lvuarV5ArTTey0gQaRyBXuxf8eBpEk5z8wZPvPsUwyofrIy2H3zqtzu1ta-iYJBHRAGr3_0cd6ON_m1f4PzgcDJyQ4KmySFkW3gUk29M3UhlzBcvzi4fbZdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دو ابزار برای مدیریت پروکسی‌های Psiphon و Tor روی سرور لینوکس
این دو اسکریپت ترمینالی، راهکاری عالی برای کسانی هستند که می‌خواهند چندین لوکیشن مختلف را به‌طور هم‌زمان و یکپارچه روی یک سرور مدیریت کنند:
🌍
۱. پنل مدیریت xPsiphon:
شما می‌توانید برای هر کشور یک تونل مجزا ایجاد کنید که همگی به‌طور هم‌زمان و هرکدام روی پورت اختصاصی خودشان فعال هستند.
🔹
نصب آن بسیار ساده و تنها با یک دستور انجام می‌شود.
🔹
تنظیمات برای استارت، توقف، مانیتورینگ و تست وضعیت اتصال‌.
🔗
مخزن پروژه در گیت‌هاب
🧅
۲. کلاینت‌منیجر xTor:
یک ابزار مدیریت برای شبکه Tor که امکان اجرای چندین لوکیشن را روی یک سرور لینوکسی فراهم می‌کند.
🔹
با جداسازی پردازش‌ها پایداری بسیار بالایی ارائه می‌دهد.
🔹
برای هر لوکیشن جغرافیایی، یک پورت دائمی و ثابت اختصاص می‌دهد تا مدیریت ترافیک راحت‌تر باشد.
🔗
مخزن پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/iaghapour/2842" target="_blank">📅 16:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2840">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">⚠️
دزدیِ آشکار و علنی یعنی همین! اپراتورها رسماً رو اینترنت بین‌الملل ضریب ۲.۷ می‌زنند؛ یعنی تا ۱۰۰ مگابایت دیتا مصرف می‌کنی، ۲۷۰ مگابایت از بسته‌ت می‌پره!
با کدوم متر و معیاری این ضریب‌های عجیب‌وغریب رو روی حجم مردم حساب می‌کنید؟ این پولایی که بابت جابه‌جاییِ چند برابرِ حجم از جیب ملت می‌کشید، از گوشت سگ هم حروم‌تره. بسته‌ها رو که نجومی گرون کردید، جاده‌یک‌طرفهٔ کیفیت رو هم بستید، حالا رسماً دارید با ضریب زدن، حجم باقی‌مونده رو هم غارت می‌کنید.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/iaghapour/2840" target="_blank">📅 20:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftXsnjCK62hb4pll3CSrloW8oNk28QJW0eAVeGH0kDLb1mccMqr3b9YcpkvDq1137WoLy6kewatF61Pyi7lFRA3ZrDZFqST2his58RZPTB9DxCa13pzZm-ABCLBvaQ_YJ1RMwyYQrUKUmm2Tqh-v1xpijxxPo5I7_h4bwH8oLxgh-q4aGpAHltwBZYy8rGnrfQQnWviNsDpsQ_0Gqqengo6QlDbdN0HLQpBbH5__BXEC_IuHm-LomUzLk1d90Vv96SoOe_VOsy6bK6XPfntnmTp9mN3A08yNput-ReHMOaJaW1ub74ORrbNOuOFUazjgMGIh5rStjeazHcw1oTYoeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎉
قرعه‌کشی ویژه اعضای کانال
(سری دوم)
رفقا، برای قدردانی از همراهی شما یه قرعه‌کشی جذاب داریم!
🎁
👇
شرایط شرکت:
کافیه فقط زیر
آخرین ویدیوی کانال
یه کامنت بذارید.
🏆
جایزه:
اکانت هوش مصنوعی 1 ماهه (Gemini یا ChatGPT به انتخاب ما) برای برنده عزیز!
⏳
زمان قرعه‌کشی:
تا امشب ساعت 24! پس تا فرصت هست کامنتتون رو ثبت کنید.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/iaghapour/2839" target="_blank">📅 18:18 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2838">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlImZNPGVWet4S5diBgau9T0Yo_e57G96AjdWkIo7rez4CdNu5UtXC8fAPX8bRnUAQ5qN-CzHg1SgKYuQRdTByK3ag21e2LPVWgpn2AcoNjRZzCY5urqYALqxw0hGpRod-fxM_Sl6uaAdIulngmGTSMhiNW7UQrt6SeuYEieDvWN4wTN-K_-9j_pUfY0_MSk0w6aRV5yj4vD13fOuXZ_9W3CCa_fHsz0UHX9tIi2zQuU1nZMPJXH1ES_AAoozY2LTQK4DTbRWlewHAF0aLeZh4K65Ze8iwChfNLh75WIKt40qSbImVEjn592FKaTOfxGZl6Vne0trwb8OolLTeK-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
معرفی کلاینت جدید Disruptor Proxy بر پایه Xray
یک کلاینت پروکسی جدید و بسیار سبک است که برای سیستم‌عامل‌های مختلف توسعه یافته، اما
در حال حاضر فقط نسخه‌های ویندوز و لینوکس و اندروید آن منتشر شده است.
⚙️
مشخصات فنی و ویژگی‌های کلیدی:
💠
حجم فوق‌العاده کم (Tauri 2):
استفاده از فریم‌ورک Tauri (مبتنی بر زبان Rust) به‌جای الکترون، باعث شده حجم این برنامه بین ۱۰ تا ۲۰ برابر کمتر از کلاینت‌های مشابه باشد.
⚡️
رابط کاربری سریع:
فرانت‌اند برنامه با استفاده از AzerothJS و Tailwind CSS طراحی شده است.
هسته قدرتمند: این کلاینت قدرت‌گرفته از
Xray-core
است و کانفیگ‌ها را به‌صورت خودکار (JSON) مدیریت می‌کند.
🗄
مدیریت آفلاین سرورها:
استفاده از IndexedDB برای ذخیره‌سازی، که امکان مدیریت هزاران کانفیگ را بدون نیاز به سرور بک‌اند فراهم می‌کند.
🔗
لینک پروژه در گیت‌هاب
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/iaghapour/2838" target="_blank">📅 16:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2837">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6lZlpcjMPXRoDyOGoH-81zlDjwG45pPetUn1lwP7ErjoBBM91_eMshYQyVBHb8iRpfSicZe8ffBMb0sHphp9WLBkvxMQZYazjw_fWJB4GJJPBuHivjuVkSDexsgqq7I7ZuzW9i4vdqHubZ4NgGrSCCLxlkeLwWY3aRVPtoJoCu80_bU0ebblMUzJvr3AqOrhUxjSBPxMhpF_YHNed_jxqECKSRb1-MpNSaZ12DewJCaXb2E2hSsl3XPA-ZlHvvJqziNV3cqnftdYYBSAYbWHpc4KwlanC3OaZNkcGlVJ3XXEuZWYKjai2kRYAeM8tFG4GcPP5xkbHhyXrzfb-FdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
معیشت بیش از ۵۰ درصد کاربران ایرانی به اینترنت وابسته است
یافته‌های جدیدترین نظرسنجی ملی مرکز افکارسنجی دانشجویان ایران (ایسپا) آمارهای قابل‌توجهی از ضریب نفوذ اینترنت و اهمیت اقتصادی آن در کشور ارائه می‌دهد:
⚙️
نکات کلیدی گزارش:
🌐
ضریب نفوذ ۸۹.۳ درصدی:
میزان استفاده از اینترنت در میان جامعه بالای ۱۵ سال کشور به
۸۹.۳ درصد
رسیده است.
💼
وابستگی معیشتی بالا:
درآمد و کسب‌وکار
بیش از نیمی از کاربران
به‌طور مستقیم به فضای مجازی و دسترسی به اینترنت وابسته است.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/iaghapour/2837" target="_blank">📅 13:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2835">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚠️
باز یه سری از بچه‌ها دارن می‌گن احتمال داره دوباره درگیری‌ها و جنگ شروع بشه. از اون طرفم خیلیا نگرانن که با بالا گرفتن اوضاع، دوباره با قطعی اینترنت یا حداقل اختلال‌های شدید و از کار افتادن خیلی از روش‌ها و تانل‌ها روبه‌رو بشیم.
واقعیت اینه که کار خاصی نمیشه کرد و کنترلش دست ما نیست، ولی تا اینترنت هست، فایل‌ها یا ابزارهای ضروری که روزمره لازم دارید رو دانلود کنید که اگه باز شرایط سخت شد، کمتر به مشکل بخورید.
در حال حاضر هیچ اختلالی روی شبکه و دیتاسنترها مشاهده نشده.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/iaghapour/2835" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2834">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1vp8kEti36kIZG_ZJmMAJ6yOMSimrZ3H_TuewWwI8zufx_4dDp_vXJAuj-4Zb-Vrz91qNPHwZb2nPvGMAJKfUPrwp6gaMmUjhQBgF-zT_ZAjreicdMgqu5RDcigZ2OJx-pttNR5YsX8sxBXraeAPfHi39y4uP1_2WWa-Mr0gxg06O3hTvFJP_QtSIn4AqVLBAsReio9CO28dsU4Jsl9n6m9x6f7aoRAnqFv1lL_xugQb5e_l3kH-dc2LwGnSZ7nWY0vtlcesWKOzJRazEvx9wLMYOth7qRirybYllMsT-S40OUUeT0PMb2_zBhlV8sSC4KDh54aCt8Xnm-TEPDnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گوگل محدودیت جدید نصب فایل‌های APK را برای کاربران ایرانی اعمال نمی‌کند
🔹
گوگل در آستانه اجرای طرح اجباری راستی‌آزمایی هویت توسعه‌دهندگان اندروید، استثنای ویژه‌ای را برای کشورهای تحت تحریم ایالات متحده آمریکا ازجمله ایران در نظر گرفته است. کاربران در این کشورها می‌توانند همچنان فایل‌های نصب مستقیم APK را بدون محدودیت‌های جدید روی گوشی‌های خود نصب کنند.
🔸
با وجود این موضوع، توسعه‌دهندگان ساکن این مناطق به‌دلیل عدم امکان احراز هویت، نمی‌توانند اپ‌های خود را در بازار بین‌المللی منتشر کنند. با اجرای این طرح، اپ‌های توسعه‌دهندگان ایرانی فقط روی گوشی‌های مستقر در مناطق تحریم‌شده به راحتی قابل نصب خواهند بود. اگر کاربری در اروپا یا آمریکا بخواهد برنامه‌ای از یک توسعه‌دهنده ایرانی تأییدنشده را نصب کند، با سد محکم سیستم‌عامل مواجه می‌شود./دیجیاتو
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/iaghapour/2834" target="_blank">📅 16:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2832">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqKxMOFZhEaMwxu0ZoEjWwFzmabdXV93fo88OR968DLppc26ow0LeHBDVKFIqQinufXdwcdEaTJICkG5WrXffEg6ZsD2Fu7W8A0C1I3JyGMDqn3NOS466678KMuCq9mx5K4yql9zpsaGDTLwNfB6YwisZywVRT7PGg2mvDSmqNbKyWJBcWSms3DG_TIRo9TTkCdleN9oa-yCLZTKge-1z3VkzBV1my6v5NGXK2WCrNzjvhGjqRvuyVuvq3oUrm24-T9RhDwzSYfXbKJ9yTmDCVNNQhvb0coP5_a1HYoVdes4uoS1eB4cIJAR3iNekizKjZpLqCf1flI4J5p0mCbl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
صفر تا صد تانل زدن و افزودن نود در پنل نوا سرور (Nova Server)
🔹
اگه می‌خواید محدودیت‌های شبکه رو راحت‌تر دور بزنید، اضافه کردن نود (Node) و تانل زدن بین سرورها همون راهکاریه که بهش نیاز دارید. تو این آموزش قدم‌به‌قدم و به ساده‌ترین شکل ممکن بهتون یاد می‌دم که چطور سرورهای مختلف رو به هم متصل کنید و یک تانل پایدار و حرفه‌ای روی پنل نوا بسازید.
🔗
تماشا ویدیو در یوتیوب
🔻
گرفتن سرتیفیکیت به صورت دستی:
sudo apt update
sudo apt install certbot
sudo certbot certonly --standalone -d YOURDOMAIN>COM --agree-tos --register-unsafely-without-email
#آموزش
#فیلترشکن
#تانل
#نوا
برای دور زدن
فیلترینگ
و آموزش
تکنولوژی
و
هوش مصنوعی
ما رو دنبال کنید
💚
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/iaghapour/2832" target="_blank">📅 18:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2831">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ottUk6bBfkc_esAWrZrjHbnG7hNBzb5mooLOmlfOqCuYIPj9lNtlGozw8WIE072L8ppDKm-ic-w4P6Syr26bZtKCpXZZbP0xKZTwl8xMNi4875uP-jc0pHVAgAgZayR0Kq8LtXOS4E_gDE1-4vFLg48wE098hKRsvC91iM39qGLF2C7PK8LDFohfTFdEZQlQX3rYE7lMUgYYma1i3FLVa0Fo3fvk8n9lH77Uku51clCi9s20ykg-8xjRVn6dqXB0xAvsyxYpxyU4AzZlCvLN9C6gg2mGlzNM3ybMXYZ5MgxrQyCUR-Oxubk1-O6wtFEJf5fYIkV5Qg3MJOazC3An-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
امنیت حساب اینستاگرام در صورت استفاده از VPN
تغییر مداوم موقعیت جغرافیایی (IP) هنگام اتصال به VPN، سیستم‌های امنیتی اینستاگرام را حساس می‌کند. اگر ورودها غیرعادی تشخیص داده شوند، احتمال قفل شدن یا محدودسازی موقت حساب وجود دارد.
⚙️
چرا فعال‌سازی احراز هویت دو مرحله‌ای (2FA) ضروری است؟
🔑
تأیید هویت معتبر:
با فعال بودن 2FA، اینستاگرام هنگام ورود از لوکیشن‌های جدید، هویت شما را از طریق کد ۶ رقمی تأیید می‌کند و آن را صرفاً یک «تغییر لوکیشن ساده» می‌داند، نه تلاش برای هک.
🛡
جلوگیری از قفل شدن ناگهانی:
احتمال محدودسازی یا Lock شدن حساب به دلیل شناسایی ورود مشکوک به شدت کاهش می‌یابد.
🔐
ارتقای امنیت:
در صورت لو رفتن رمز عبور، هیچ‌کس بدون داشتن کد 2FA امکان ورود به حساب شما را نخواهد داشت.
💡
پیشنهاد:
برای امنیت بیشتر و عدم وابستگی به پیامک (SMS)، حتماً از برنامه‌های Authenticator یا پروژه‌های امن کلاینت‌ساید برای تولید کدهای 2FA استفاده کنید.
©️
filterbaan
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/iaghapour/2831" target="_blank">📅 14:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2829">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mylUlcOK769yIG-MAMEJwcXq8ZIIm0f1b-ykUlGrqxa41hyfBbNttldfB7FeCtgZIryt5IXWrzR_huz0KUHg7kKKrGfiYbJ-I4bYfozin7vW8i6SUbP-FBpfb7gUFFrgBvp86qqlEzYuVwgPkLkEekqDX_q2JuGRZ7iXdpdus9r8bj4uLKqYrFIncip9g3LysVAeHG5zOZ5Efx19_5WJaZPIJZhYC0iZNxMwOoGeiueYif3KQhNVNzVVto1pbHpdYf7rQpHBQVL38EQc7Fzy2Dwy7X6gJ51ODqNrF_7vAv_1OQmlL8B4SDVizqE-6DoVidjM4fdfvoxLn-R8FTGfgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
فعال‌سازی رسمی اینترنت استارلینک در عراق
شرکت اسپیس‌ایکس از روز گذشته (۲۹ ژوئیه ۲۰۲۶)، ارائه خدمات اینترنت ماهواره‌ای استارلینک را به‌طور رسمی در کشور عراق آغاز کرد.
📊
جزئیات تعرفه‌ها و تجهیزات در عراق:
هزینه خرید کیت (دیش و روتر):
حدود
۳۵۰ دلار
(معادل ۵۲۵,۰۰۰ دینار عراق).
اشتراک پایه (سرعت ۱۰۰ مگابیت):
ماهانه حدود
۴۷ تا ۸۷ دلار
(حدود ۹ تا ۱۵ میلیون تومان با نرخ‌های تبادلی بازار).
اشتراک‌های پرسرعت‌تر (Residential Max / سرعت تا ۳۰۰+ مگابیت):
حدود
۹۸,۲۳۰ دینار
.
این سرویس امکان دسترسی به اینترنت پرسرعت و بدون محدودیت را به‌ویژه برای مناطق دورافتاده و کم‌برخوردار عراق فراهم می‌کند.
©️
Aliasghar Honarmand
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/iaghapour/2829" target="_blank">📅 21:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2828">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5ADFAF6X5-WXvmI8gTA2raM3otgaoCqrFfLf8cNpZEyHOxCItEcUtNmQePejXgZQN8wPaEtoapaovQaBr8G7BV0X6gPr4etq0NXlOgmtS-kAGBdrTiCzd9NcKTyA_YrMPoJbs-DBsTV3TJnpWE5zQsE11tv1cm0aDaFw8h9FFpd4s26HwMXfTtFTsQ5xCzfwelmNWhKI82VVRUn_GwWcFJZyYyA8dWQSsb8E7MdKUHgaHthV1IO0bI8K450hS7Nl3Wo1n-_ratQjrtPfmlJRUkoPNBaKZCc7SwGC0CEpWafgHLhsia7sACO6AtNwG9p0uxq4QTX69oCgKTmV_pk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رکوردشکنی هک‌های کریپتویی در نیمه اول ۲۰۲۶؛ سرقت بیش از ۱ میلیارد دلار
پروژه‌های رمزارز در ۶ ماه نخست سال ۲۰۲۶ با موج بی‌سابقه‌ای از حملات سایبری مواجه شدند و تعداد حملات تأییدشده در این دوره، از کل آمار سال گذشته (۲۰۲۵) فراتر رفت.
⚙️
آمار و نکات کلیدی گزارش:
💰
حجم خسارات:
مجموع دارایی‌های ربوده‌شده از مرز
۱ میلیارد دلار
گذشت (البته خسارات مالی نسبت به اوج سال ۲۰۲۲ کاهش ۷۴ درصدی داشته است).
🔻
نقش هکرهای کره شمالی:
بزرگ‌ترین سرقت‌ها از جمله حمله به
KelpDAO
(با خسارت ۲۹۲ میلیون دلار) و
دریفت
(با خسارت ۲۸۵ میلیون دلار) توسط گروه‌های وابسته به کره شمالی و با روش
مهندسی اجتماعی در لینکدین
و نفوذ به کیف‌پول‌های چندامضایی انجام شد.
🌐
آسیب‌پذیرترین شبکه‌ها:
•
اتریوم:
۳۳۲ میلیون دلار خسارت (تمرکز روی پروتکل‌های استیکینگ مجدد و استیبل‌کوین‌ها).
•
سولانا:
۳۲۶ میلیون دلار خسارت (هدف قرار دادن زیرساخت‌های امضا).
🤖
تهدید جدید؛ عامل‌های هوش مصنوعی:
کارشناسان از احتمال رشد حملات تزریق دستور (Prompt Injection) به ایجنت‌های هوش مصنوعی خبر می‌دهند که نمونه اولیه آن هک ۲۱۶ هزار دلاری پروژه بنکر بود.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/iaghapour/2828" target="_blank">📅 19:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2826">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIBhAENaUj3bU2NKDAlyHVXpKtU_ZbQ89rC1kB24VP1b2HlL4I4eimuYNB9VTKaRvoBOpl-Rne9gtbdJaO5NlPo959E1swYaMS78WGEhMEZLUW6awXnQDtUbNFVRWcDs5p6Ua3ohhV98cp252YWic4iK0H0H5Ucytdl3NP_2VjITr7MZuaG83rtbrz3co1ednYImzCVwko3yiDRO5E1IaJPZHkshW7FLY-hyILC1AAE6_mecSRkI7YCpBUOLkteVqgebkhxVERUyM2YOPWWoI19V2PJOKtaGA2tyUZIXE5O2cahU9Y4NhqTUbqXKpuglvnguvm7C3wIsLxBHluQPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تمام پروتکل‌ها در یک پنل (L2TP/PPTP, OpenVpn, WireGuard) در کنار Xray
🔹
پنلی که امروز بررسی می‌کنیم علاوه بر پشتیبانی کامل از Xray، یک پکیج کامل از تمام پروتکل‌های کلاسیک رو تو خودش جا داده. اگه نیاز به پروتکل‌هایی مثل سیسکو، OpenVPN، IKEv2، L2TP و PPTP یا حتی وایرگارد با AmneziaWG دارید، این پنل همه‌چیز رو خیلی راحت و تو یک محیط یکپارچه در اختیارتون می‌ذاره و دیگه نیازی به نصب جداگانه هیچکدوم نیست!
🔗
تماشا ویدیو در یوتیوب
#آموزش
#فیلترشکن
#سیسکو
#l2tp
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
@iAghapour</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/iaghapour/2826" target="_blank">📅 18:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2825">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye1RBhnUWYADoxUEL_1Ydf9vy1PuXvMQ-Rn2mvcB_bqurK_iwy-1nk9SYt3ai12W8XsWMXzD2zQsNboY33XiHTjKSVs1rAGwxzOFTCyMVzgZluXxTByB908ghZPMtjbl4VkS8D8AqX4mEDHGKfWy4AIGDOLMDpIyyWm6Z15qwaGYTj2tJ0Upyura3ZeL4ZRWYQE0k90vCsE1zpoQ7oM0ComPTRtOOs5ueRBZvsKGsG_8_MY3ATOPOgeGzQM50EOTm39TN5K-mLNAMXlv5ZXGTiPMopabAzlfARGU9pLf7Vm_iJq79VXxf8IuHCAdoWTUefl8rDhXRZc5JkP9h4T8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سرویس امنیت روسیه: پاول دورف تحت تعقیب بین‌المللی قرار گرفت
سرویس امنیت فدرال روسیه (FSB) «پاول دورف»، مدیرعامل تلگرام را به اتهام
تسهیل فعالیت‌های تروریستی
تحت پیگرد قرار داد و حکم بازداشت بین‌المللی او را صادر کرد.
🔻
خلاصه ادعاها و آخرین وضعیت:
🔍
اتهامات FSB:
ادعای عدم حذف کانال‌ها و ربات‌هایی که به گفته روسیه برای هماهنگی عملیات خرابکارانه، جذب نیرو و کلاهبرداری‌های سایبری استفاده می‌شوند.
💬
واکنش قبلی دورف:
دورف پرونده‌سازی‌های روسیه را بهانه‌ای برای سرکوب حریم خصوصی، آزادی بیان و فشار بر تلگرام دانسته بود.
⚖️
پرونده فرانسه:
هم‌زمان پرونده کیفری او در فرانسه نیز مفتوح است، هرچند محدودیت‌های مسافرتی وی در فرانسه اخیراً لغو شده بود.
🆔
@iAghapour</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/iaghapour/2825" target="_blank">📅 16:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-2823">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎬
فردا یه ویدیوی جدید داریم و دو روز بعدش هم یه ویدیوی جدید دیگه تو راهه!
توی یکی از این دو تا ویدیو قرعه‌کشی داریم که توی خود ویدیوها بهتون می‌گم.
طبق نتیجه‌ی نظرسنجی، قراره اکانت هوش مصنوعی به برنده‌ی عزیز هدیه داده بشه.
🎁
✨
شرایطش هم خیلی راحته؛ فقط کافیه زیر ویدیو کامنت بذارید!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/iaghapour/2823" target="_blank">📅 21:05 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
