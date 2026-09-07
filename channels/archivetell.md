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
<img src="https://cdn4.telesco.pe/file/bsiMqcSWhuw4KzgpMtzIhun2E3Tc9QHykebYK2TPk9A4fcVDCVIheC2L57J2rpzTVkm4nWOUGDMCzm_j71qz1GeEdcLi88VpGfrB9Eqhqhk0db9QOl_VUY_-75poswxpwRb7N-mxsUM60rm_iPr9U0goWHKPn1Draiapw5elL2xqNr__95k0FgPYq-TuN-FQVT4Df2xpNRY42OQvLLk0K5YBjZuqqOS1B2uf6OQuEYw6ZdooPG16Ch89ECOTbpsBxSi2o0kUGlTqNuVd_oWDLzCXgEyuIeBzLbZFYvUl1Jp0oUvkIQjc-89xlQ7O7M45VCZss9EnTkDS4-OhxrBUbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 ArchiveTel</h1>
<p>@archivetell • 👥 10.1K عضو</p>
<a href="https://t.me/archivetell" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ‌‌‏🚀‏ آرشیوتل‌‏مرجع تخصصی معرفی، آرشیو و آموزش ابزارهای متن‌باز و پروکسی‌های مدرن.🛠بررسی روش‌های پایدار برای دور زدن فیلترینگ و اینترنت ملیآموزش‌های فنی به زبان ساده!🌐تبلیغات دایرکت کانالwww.youtube.com/@ArchiveTell</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 14:07:21</div>
<hr>

<div class="tg-post" id="msg-7662">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp_EWu7Ryzm1ZC4eDusIYYqqbvl1qRyx7odvtl7ZplGljMB1YEf0CcXiTMIp2jifkRIpgeXRAj5W3V0p6E33E0eEzYdZVgbCkKgZrymx-D2UhhIJXBsF9ZnJsHtOpPHRI8H67yqqbITPMBNrrEtZSQQT8SocUjfmJkdyomCUmxL-o-rSZU0xsbsYQrQA6LW13NC4CErHoNJb9QKCLho46M1y3RRU2KvNcXjZJarQEyQdCsFSG4i3_xjg9Cgn9ER80H3JtL7jCK_qp8_63IhB8OJlvNkp0HzhA4rOPFjGQJpP7wJh6xWndRiSmdFHdNCKHWVExh7CPjTL0z6oNfwfmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طراحی و ساخت اپلیکیشن با M3E Canvas
🛠
📱
پلتفرم
M3E Canvas
یه پلتفرم اوپن‌سورس و جدیده که بهتون اجازه می‌ده با درگ‌اند‌دراپ و کمک هوش مصنوعی، برای اندروید و وب رابط کاربری بسازید.
🔺
طراحی سریع:
المان‌های آماده رو می‌چینید، رنگ و فونت رو شخصی‌سازی می‌کنید و همونجا تو مرورگر تست می‌گیرید.
🔺
تولید پرامپت جادویی:
جذاب‌ترین ویژگیش اینه که در نهایت از طراحی شما، یه پرامپت دقیق می‌سازه که می‌تونید مستقیم بدید به ابزارهایی مثل Claude Code یا Codex تا براتون تمیز و بی‌نقص کدنویسیش کنن!
📌
لینک دانلود / گیت‌هاب پروژه
✈️
@ArchiveTell
| 𝔹𝕒𝕔𝕙𝕖𝕝𝕠𝕣
⚡️</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7661">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه ArchiveTel رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد این ربات رو استارت کنید…</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">قرعه کشی اکانت Gemini Pro 18 ماهه
💥
🆓
برای شرکت در این قرعه کشی کافیه کلمه
ArchiveTel
رو توی کامنت های همین پست ارسال کنید
✅
هرچقدر تعداد بیشتری از شما مراحل زیر رو انجام بده تعداد اکانت های بیشتری برای قرعه کشی جمع میشه
👇
1️⃣
وارد
این ربات
رو استارت کنید
2️⃣
در چنل ربات جوین بشید
3️⃣
با آیپی خوب ترجیحا آمریکا وارد دکمه بشید تا سایت باز بشه و دکمه وریفای رو بزنید
‼️
نکته :
در هر گوشی فقط 1 بار میشه اگه میخواید با یک گوشی تعداد بیشتری بزنید باید هربار کلون های تلگرام رو نصب کنید  ، هر 5 رفرال برابر با 1 اکانت هست ، تمامی کریدیت های جمع شده تبدیل به اکانت میشه و قرعه کشی میشه و لینک فعال‌سازی به شما داده میشه
‼️
شرایط : حتما باید در چنل آرشیوتل عضو باشید
تاریخ برگزاری ، فردا دوشنبه ساعت 20
🚀
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6yyijCPMJs43eijmZxgy7RBL3OO0LKgRE_RyVa12dkyZkYe6untbcTIFYpOYt2H2M_K6deSD_lmtI7bXCbmpp5AM97jHKmNlVUu-K4K1VJq5F9TbLuwtGNgYojhbAqdZpl7t1ZVvwQtoev3nQMkBmb9PLeXnsv4zIgWx0W4JAXAMI58z7aCmInhVuM75w7S-Bmzxd_e4-lfwFOVhA3KQYu386OfTXhAa1CufURGLBDg6-uOCYX-u94KGi1VbRkIyvdQnUVrHFS-v3p9uMhOdvjnct_5wmFk_7FpuKKvpRAOZMyagdYa2QarXnpXb0cbWiq0rx5Q0oepb0O-Vqyi5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API هوش مصنوعی ها
💥
🆓
DeepSeek-V4-Flash-Vision-Exp | DeepSeek-V4-Flash-0731 | Qwen3.8-Flash-Next
✅
این سایت ثبت نامش کمی آزاردهنده هست بخاطر UI بدی که داره ، باید با گیتهاب لاگین کنید بعدش میره تو داشبورد و به ایمیلتون کد میفرسته و اون کد رو توی مراحل وریفای وارد کنید ( شماره تلفن لازم نیست ) حالا بگردید عقب و از سایت API دریافت کنید
✅
هر روز این سایت 1 PTS بهتون میده که معادل 10 دلار هست و خیلی زیاده برای این مدل ها
🚀
محدودیت هم هست 20 درخواست در دقیقه
‼️
📌
Base URL :
https://developer.amd.com.cn/radeon/api/v1
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfIr4GdDFzZonsk3V8whrROBu98wYQPwi-5CHuWgfYVhUXMFR8lRxVaXykEndb-MuuGy4SrXT4z6lJZHgdq2GkVOqfCO-FH6p5BQjj6oOYgZbMmA_YVUeQUOvYQL1lw7C_K50dNqlhHzJM6HnfbuQCWYIVmP8jMANZJauEYOGgvUr-66Fqk0pnsR1wban2ccnmUK9ULXtNz6TyhlobiwufmP_xG9wG7V2REp_RsSLvlXJCatYd2q2y96YHcsgZCL86eEGzyfoiIlX_SnIyDLl1SADK3Xq4U8Fj0GRB7bktc0xwTXmIyQGvpP2QwXrydW3F4obUraFE1qFVosl-jbnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به هوش منصوعی های محبوب
💥
🆓
Opus 5 | GLM 5.3 Flash | Deepseek V4 Flash | GLM 5.3 Flash
✅
4 میلیون توکن میده که میتونید استفاده کنید از API هر روز هم ۱ میلیون توکن میده برای opus 5 ( حد مصرف روزانه هر مدل ۱ میلیون توکن هست )
📌
Base URL :
https://helyxai.space/v1
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMY1NKyKVS6DGpFifVDi6QAS5VejKanas-Bt1wuKHny75n-XICBN4DWCwhoyz_jSGKzUEeOZE7FqnjiYtVvTCC5noJF8xG8zSDui_Ems-VUaFJ2le5_7uG5RxojrL62jznxwFNju4lWkNXh0TsM60fok2mApFDC4wBhgnlaXSx1rDrvYGLoQ3NaoT4iy0k8vaSXRi2_SU1ZvlcsnMRm7trslPK5knLLV2gePgzgSsftELlW0ZzIIbWKH4pVZt53J6NXP9RY3uE_xUAQteLrFbgGLy5Z2Zqj9b31_Rg8kakgAKXks1eQBIG23zQqlmG400W0VGBnUM3G2bVhMhudaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏
اینم لیست مزایایی که داره:
‏• جمنای: ۱ سال رایگان
‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه
‏• جت‌برینز: ۵ سال استفاده از تمام ‌IDE⁩ها
‏• گیت‌هاب: پکیج کامل توسعه‌دهندگان
‏• آفیس ۳۶۵: نسخه کامل ورد، اکسل، پاورپوینت و تیمز
‏• فیگما: نسخه حرفه‌ای مادام‌العمر
‏• نوشن: اکانت پرمیوم مادام‌العمر
‏
برای دیدن آموزش کلیک کن
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBptPkCj13JumDoLw1a-RMISY8H7SuQZN1MNvU4LgMWD48HW0GKwX3cO9i72ftkLgRZvPkJLCEk5qxdKPh8ztQuAUxvrG9C-IZeOf2LR8rAFQYJ0EImv2pBwOqu1lvFe4hr4sZBazDEXX_hnsmrd-g4dCoq1itLxBOjnyzxJKpvZHgnKWycGxwIORpq4EkOgOAeleXxy-HOnd2gmiW06ZZMm0mXpxNXIg5PZ7LQHFY2OwmqwZOq4oFjNJxVMl30XA5UHC43MSko3lGoqzoSsRfoq8Iq8MQEsCFfydpVuAHk_nJ1Rt3eXPw8R8SA6l-4cMM4l7nfZRMP8BomL61PPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
داستان GPT-6 چیه؟ انقلاب هوش مصنوعی یا فقط شوآف تبلیغاتی؟
🤔
این روزها همه جا پر شده از اخبار رکوردشکنی GPT-6 Astra و نمره عجیب ۹۹.۹٪ در بنچمارک ARC-AGI-3.
طبق بررسی‌هایی که کردم، این نتیجه تو شرایط کاملاً ایزوله و خاص ثبت شده و توسط منابع مستقل تایید نشده.
قیمت‌گذاریش هم به شدت نجومیه؛ هر یک میلیون توکن ورودی ۱۰ دلار، و خروجی ۵۰ دلارِ ناقابل
😁
(مقایسه کنین با جمینای ۳.۸ که ۳.۷۵ دلاره)
در ازای این هزینه سرسام‌آور، وقتی در کل حساب کنید، برتری خاصی نسبت به رقبای خودش مثل Fable 5 نداره.
یکی از معدود بنچمارک‌هایی که هنوز اشباع نشده و به نظرم بهترین معیار برای ارزیابی مدل‌هاست، بنچمارک Humanity's Last Exam عه
تو این تست، عسترا نمره ۵۷٪ رو ثبت کرده؛ در حالی که Fable 5 با قیمتی مشابه و حتی پایین تر، نمره‌ش نزدیک به ۵۸٪ عه
🔥
با دیدن همین آمار میشه گفت OpenAI با این Gimmick های تبلیغاتی، رسماً داره به شعور کاربراش توهین می‌کنه
😐
من حتی کاربرشم نیستم ولی باز به شعورم توهین شد
#طهلیل_ai
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-wsrZHeec3hnIi-hdq6kvdRd7-nVBtA5dTL_spxHYOlrxVWUJWMhrQqQEmlqhC-KJYg_BYu_XwNCoOAWUtnnqRwPjTRXakhRpjDE7qQLlf3RQabxVZZvbZiuO6MQ57jjCT9jlgwYOQzo83PPlnt9xULOy1zxcPMKatWKXR1Xwc-Xuvn1vkVga3yx4B6hocnEaky6qRLhk2sg4j5fmzVqNIDcznDxVHORS1DHuBDgnzu0kwuHP8P6Am1XEDenlZbiSYPGFb33muKmPLaKdSApWSev4J87yDBKigVmhJMNdgYvlbclo6-V1NmjzIySSTk6hjCmzDqVgGP0dzaqEVTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Free 2k$ model GPT
💵
📌
Base URL:
https://vip.9aws.net/v1
📌
API KEY: sk-g926rIr0SG7pfoD4WextkZwRRAgFOwYZDsG5hnDr8mL2ZH9d
📌
Models:
gpt-5.5
gpt-5.6-sol
gpt-6-astra
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW5Twp-FUnETH9XVDWqj3_R8S1p80q72tCQQ9JmiZ8Woi74Zt1d1rAjqreAD5nomaa7A9Spn_f4-Dhuee-HZDhR5Aoi6XQdqnsRtp1rvBkiYN4Y0ftJ_8LsTOXnXkx8jzsV38FI2jDTR-chdD0LBgwu9wQhSzYBckr7BF90WBilMdJ2hJYoIXQHY260wuPyy1TAABZukvBOIQR32igOTIWXByTIgAlA-tsGKTHEvfx5GM0GXoPtq-Z9Ua38VFMQFY_PcU2L4dhWdMwCL5wqwxwvvYLZUP0OFdc1Gfr3xSc6rFfJGQPb2WGwbf_HPaDxrtoWPPcPs2Ixmtn28RnJGeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی آزمایشی رایگان به مدل‌های پیشرفته هوش مصنوعی
💥
🆓
Opus 5 | GPT 6 Astra
✅
سایت ClickUp فقط یک ابزار مدیریت پروژه نیست؛ ClickUp Brain حالا امکان استفاده از مدل‌های مختلف هوش مصنوعی را در محیط کاری ClickUp فراهم می‌کند. طبق مستندات رسمی، مدل‌های OpenAI، Claude و Gemini در Brain قابل انتخاب هستند و می‌توان بین مدل‌ها حتی در یک گفت‌وگو جابه‌جا شد.
🚀
🎁
سهمیه رایگان
در پلن Free Forever، نسخه آزمایشی Brain شامل ۲۵ استفاده برای هر Workspace تا ۱۰ نفر است. در Workspace های بیش از ۱۰ نفر، این مقدار ۵۰ استفاده است.
✨
⚠️
این سهمیه ریست نمی‌شود و پس از مصرف، برای استفاده گسترده‌تر باید پلن/افزونه پولی تهیه شود.
🤖
حالت Agent هم دارد؟ بله!
دارای دو نوع Agent است:
• Super Agents برای انجام کارهای چندمرحله‌ای، تحقیق، کار با اطلاعات
Workspace و اجرای workflow ها
• Autopilot Agents برای انجام خودکار اقدامات بر اساس trigger و شرایط مشخص
💡
علاوه بر چت معمولی، Brain می‌تواند روی فایل‌ها و اطلاعات Workspace کار کند، جست‌وجو و تحقیق انجام دهد و حتی Task، Doc، گزارش، اسلاید و موارد دیگر ایجاد کند.
🔗
لینک وب سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ds4lhrh9naExhnaFKU-tv6Ptx6Xr4gLpzBN06SNNNF_gg8MUmnbYxwbnVyyJFmLjAWqW6up3UH5Vg05060IU4hR9u4G1DP7O1qRXgx9s-lKQVbLA4oRQLeNCprpk_ZmUEGwFVOQ73KXo9h3339UIFiaH8Dllp90JcNOAcrD2tZJ2oc4u9dKajX52EoFUqOwniGohULBI2SuCeM65RFf-rVWQwczIUG8OdKk8j0YMGn0kzFqa5bFETPBlvXJNahM59CYWblZZR3NdcISZtkIi7Dxm3_us1-O8dygOg_zXCL8igkZDJ5kQmh46hd6r0QeCmc3FS9h5MhxVQ-OqhNnZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API مدل های هوش منصوعی
🚀
🆓
Opus 5 | Grok 4.6 | Deepseek V4 Flash
✅
برید تو سایت زیر ثبت نام کنید و موقع گرفتن api باید گروه Free رو انتخاب کنید از این گروه این سه مدل بالا رو تست کردم جواب دادن ، بقیه چیزای خوبش کار نکردن این مدل ها رایگان هستن و کریدیت نمی‌خوان
✅
📌
Base URL :
https://kiosapi.com/v1
اینم کلید خودمه اگه دوست داشتید میتونید تست کنید ریت لیمیتش رو نمیدونم
📌
Keys :
sk-ZoCd9hc91if9INutCoTC6zA0wJ2pbrd9a75GQJTyj5V4gIup
🔗
https://kiosapi.com
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpvRqzBGbTYn2Bco5BotVlxpeETGRcslrIbWCBVfGZOQJBxqvReNKBaZ0NPA7f4FhTp_NkqV_KRnuSRrbENRN47wqwXDqdW58YmNELvkASgk5nIiEFW6Go_FKUtwrkcxrkv9n3Y4bW7QDrNX7xznop4LysGEuY7vzT0qrMp5EexiRjEOCZhUdldHptJC3pRzBGCPeR0lK87qbpQDnjSg37swv7osJJbzOKSchdbAmozlpHabMEiVW-DWaTHivaazVPIeQ3neYRMBEo-iDTMcSIlhCzKenmuRaCJxG0BUuQ_5Kk7_2UMlex0VtojNGV3Kzot9gGEFU4vNNHEanoasUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5000
دلار
😎
📌
Base URL :
https://vip.9aws.net/v1
📌
Keys : sk-faNuu4uK9WqIYAiXjdmYxeX6PI1Z5wNLzCsIXKbKVQ67W1rG
📌
Model ID : claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMC-JoY8JCcPpnMPXpLoywL78KwR6-7eD_rVTfEEkZLgIAlA2yTIh7X8DQJBq6YJ9C9wYkeYSHgiWIwM5XoQRoKOmAMrx2_SZfa1exmsWsVlBdtjRXJnEgFwup6NE5MMSLcz6LzTBN7mN2Pp0_SX0o3bVAuE90B-ABeyMEBLzOTbT8PmsgAe_BXPcVX7uMIILtLH7_2w2sw8CJeMgj92OdcZSMpqV0YqsmUz_WGjg5_vVOtEXzQTeqE2OyMzhzmhB5OlgMMayc-PjQx6HvvSXMUwmxBKutsChZ5PAHbhLBEdKsVv8XuZyO97oS0S_NB-JpDuJwwsUWgOtJPaltvN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ساخت وبسایت ۱۰۰٪ رایگان، فقط با یک کلیک!
​سایت شخصی یا پورتفولیو می‌خوای اما حوصله خرید هاست و دردسر کانفیگ رو نداری؟ این پلتفرم اوپن‌سورس رو دقیقاً برای همین ساختم.
​
🔥
چرا ZeroWeb؟
​
💰
بدون هزینه هاست: کاملاً رایگان و مادام‌العمر روی سرورهای کلودفلر.
​
🤖
مدیریت با تلگرام: پیام‌های فرم تماس سایت مستقیم میاد تو تلگرامت و همونجا جواب میدی میاد تو سایت.
​
⚡️
نصب با یک کلیک: فقط روی deploy.bat دابل‌کلیک کن، تو ۱ دقیقه سایتت بالاست.
​کدها و آموزش کاملش رو تو گیت‌هاب گذاشتم. همین الان دانلود کن و سایتت رو بساز
👇
​
🔗
https://github.com/faithsaly5-stack/ZeroWeb
​
⭐️
خوشتون اومد استار بدین
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEn5M1L7UFjOYqsZT3278W-eWAbPj0N4FrrPxDNNiiRRAOAYk0hQ3KXpz0ycREJlOKm1PFHJQvDLE1KKNngeOuKXfi1dtdw0j9V0WBA5Nhu1CVRiOuWLjnnZWZDl3J7mflRvQSDAovFal-9D9FnlwlNkwoPK8FNOvj21XCBym3rPmh6kMI_jbPQOz3UvHGY5JALRfxw1bgcxQMsgwdUUoyMPpeyJbugfn27iOMnHM1oIrgIa1qoxW2rMDiry0pzsU9Gf6RuNbkARRvxQfWcvgcxpUj9hPr_xN8BUW7XxZz4PZziIb4pg2fjwxMWwD-VxKwLlpRxyDqT60XZpGfG1yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت z.ai کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه: ۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan: هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7645">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IW0cXenF4RGDdYuiLEEbylBNtTCh0TepKDiuOx5Slo4aljcbknjGphmFo8rHVbuLCePi503vdQBRxgRBV4PxeVymKg-3benci7nC3M4VinOJ1_ENA9_l3N2re4xYbX8H74GUlu_NQsyuwEYqr_VSgf3d2aCxN_BqvNCG55QPQMWEL_TFOJMgE3p-GGxycuVO_GMPKtWb_84tC2Y_QuLF3_f5jQTn4ABNcpyCoMbH99DxgYe-buZyykvcsLXKAqe_xjt4dZ5nnPk33EyHbiCp8mbr6HrpwqAXvSvWfUIc8TEY5lU2vviteh-mSfh7uIz4imyvEkoGePxVYF9XswDjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1,000 دلار
😎
💵
📌
Keys :
sk-ByTi6xCfB7Pt1N8Hp9z7VdsRwGIMM5pdnh4CsorUfflysvbq
📌
Base URL :
https://tabitoken.com/v1
📌
Model ID :
claude-opus-5
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yj4xWpcqweko8K-EmvNlynZwcmzrvuwFSj-TxarATVXLqss50ldTjG7Gpp8jnO_8UYc9vExHxXjVq2JF-CXqbfJx8lxvUPgkRurDVTqnRfQS_sfj-br6G7ws9nuQ1YRjzzmyfOsaW6335BG4tiKScR8-J_tvj5AgNI7O9CQuiGFiloGhCaha_K5MPxIwyfJZQXCG7A4WebQDOygITJmPdvHGXG99p24zxj1YvCFAGUzBHhXqY1x9rHN6UGK65Duai65Aj-0zo2CHACRDAl6C34jURryQ8s35O0qX2vXHzVCl0PiEBqV_x_O44IJ8y0q6M0dIW5xmWVjjG-Gv07qFHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZ1yRvXgSAdSLREc-_jy6af8HlcJRtVEPlR7Rkn_mo-cdTDrTnDOxcSImz4VlcMpWNdK_SOHQjsoGofYhbxb03jFgLecO1tZ7IoHJ_QEtsOFP3EBcUE3WItnCuOPUxG72OYe-2WbwtIW4MsEeSthtRdZaMBETuC6AatXRiDTsAKs-4YarLtGzoFnNylNfeLGK6EGUev352QFUP5G_OJgD_9yCnakd4BSMPnrvdZABin-w_BWxMKuyZANDymBfWciRLgB_JAjeNXvqZfYXzicn7akLBarPQxSqCA5eWW1U3XwAbS88Q9YCRW2RuC-XN9qqPawR51_6G5qrTck7HxnMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سایت هم به دلایل نامعلومی میاد API مدل های Fable 5.1 و GPT 6 Astra رو میده ایشالا که خیره
📌
Base URL :
https://api.experientiallabs.ai/v1
ماهانه 5 دلار میده و همچنین فکرکنم Fable و Astra کلا رایگانه
تست کردم اوکی بود
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGLo67Z_yzHuwSBJ0PDkTbaRlW3P6iyOZWcpviVbWHbW50zBrgg-xzNQOxFwlKUNLFmjh3SXWiZ_u9AV_bYk0GDR72_q8pWiDcNpYipWww6s2q1RA9Z8wrPRhcwBGVkMCyiEQ34VbnGKQ3UbJojKgJLiboO57Eg7RlHmCxecmfxzVajZSZin624DIjghRiWYDDQzeU08rwoLANJp6vO6d9fZmtygMFmtHNEIRfMVFBFYqxBs4xo1J_6LhSqGftmoCj8zkIry2n8uBzaa7a6FV9VbvMISCYFGT0n-dGe5dH3zM-qrAAttJQ-WLQpnjDthFAmgnn1eB6Gkiz46EAjuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=p78rHVmvHBzrp6P3ACdbuRYm2hrlpUpYB0q7fHOYRJcv9FgdXA3FMyUdSN-QwtVKkwVRH7dmDLe42OIpbTPWocKVH_gh4MS_wE_LbnggMiYVcTTDHndIGMrEejv_k4NDu8zP0uvl1gbq2-nWsYqI5anYAojoCA6nNtCAMPZ4Q98i9SYN7zXj17yb0WQe5coJ1UeTc9aNhIch3-JJBOUJzNTz1pM48rJOIVEmrIxWDZXGPiqvN2DJUshvDpH-Al4-XEVebnOM6SFV_acSHiqAdbUrzqmBsmkSXi8Tiyqk3CnwkHLrik4r2yWvU89v0-p3DowAmjSAg7hua0HQqQ_EOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39922c53.mp4?token=p78rHVmvHBzrp6P3ACdbuRYm2hrlpUpYB0q7fHOYRJcv9FgdXA3FMyUdSN-QwtVKkwVRH7dmDLe42OIpbTPWocKVH_gh4MS_wE_LbnggMiYVcTTDHndIGMrEejv_k4NDu8zP0uvl1gbq2-nWsYqI5anYAojoCA6nNtCAMPZ4Q98i9SYN7zXj17yb0WQe5coJ1UeTc9aNhIch3-JJBOUJzNTz1pM48rJOIVEmrIxWDZXGPiqvN2DJUshvDpH-Al4-XEVebnOM6SFV_acSHiqAdbUrzqmBsmkSXi8Tiyqk3CnwkHLrik4r2yWvU89v0-p3DowAmjSAg7hua0HQqQ_EOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هوش مصنوعی حالا می‌تونه با YouTube کار کنه!
یک قابلیت جدید به نام youtube-skills به ایجنت‌های هوش مصنوعی اجازه می‌ده فراتر از باز کردن ساده‌ی ویدیوها، مستقیماً با محتوای YouTube کار کنن.
🤖
🚀
قابلیت‌های اصلی:
🔺
استخراج ترنسکریپت کامل ویدیو همراه با تایم‌کدهای دقیق
🔺
جست‌وجوی ویدیو بر اساس موضوع و پیمایش کانال‌ها
🔺
دسترسی به ویدیوهای جدید و محتوای پلی‌لیست‌ها
🔺
دانلود زیرنویس‌ها
🔺
پردازش گسترده‌ی محتوا؛ از جمع‌آوری ترنسکریپت‌های یک کانال یا پلی‌لیست گرفته تا تحلیل چندین ویدیو
🔺
امکان انجام تحقیقات عمیق با بررسی هم‌زمان چند ویدیو درباره یک موضوع
📊
یعنی ایجنت می‌تونه ویدیوهای مختلف رو جمع‌آوری کنه، متن اون‌ها رو استخراج کنه و برای تحقیق و تحلیل از محتوای YouTube استفاده کنه.
⚡️
مناسب برای ساخت AI Agent، تحقیق، جمع‌آوری اطلاعات و تحلیل خودکار محتوای YouTube.
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMUJbI5wG9H8CZqk20rb_UK-Nat7QGNFiH6uVA0CQLFh6J3gVWMPbdcspPoJHwqbyC7583QCB2SWeXiPg-7zmuN5_HxyFFd6CtLkQliKImJCHoXlt_1FgaenLda4q6PXMiKNRtzHe2vj0YaXbAR1cOmmqoOVcxCFfJzyyOMspXHlz2ZDjdcgqFRudZm5BXtJ6PI6W7VUHNfOoBAI9SxKtFUwe9w8iUtsZwFevLdi1s6wBH3rxjg4vXsjQKuGbkAnJIpjjI0SibCJ6flLKRfoREhBzsKdj1YfJbjqHteB7dROXxo9tHdfaKCef0Sqf2iKRF9xHIR9E0s73zrYRTA1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">200 دلار برای دسترسی به مدل‌های هوش مصنوعی محبوب
💥
🆓
Kimi K3 | Deepseek V4 Pro | Deepseek V4 Flash | Sonnet 4.6 | Haiku 4.5 | GPT OSS 120B
✅
کافیه با جیمیل ثبت نام کنید و یک کلید API دریافت کنید تا 100 دلار دریافت کنید
✅
📌
Base URL :
https://api.you.com/v1
📌
Example Model ID :
kimi-k3
حالا برید بخش تکمیل پروفایل و یک ایمیل با دامنه ناشناخته وارد کنید
مثلا تمپ میل
سپس 100 دلار اضافه دریافت کنید
😎
🔗
لینک سایت
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎯
چالشی بزرگ برای وایب کدر ها به همراه جایزه
اون لحظه‌ای که به یه دایره چرخان خیره شدی و منتظر جواب هوش مصنوعی موندی؟ Commons میگه این وضعیت روزانه
۳۰ میلیون ساعت
از وقت آدم‌ها رو می‌بلعه و حالا با پول جدی می‌خواد حلش کنه.
😎
💵
🎮
چالش چیه؟
به‌جای یه پروژه‌ی کلی «چیزی با AI بساز»، این‌بار هدف مشخصه: زمان انتظار برای پاسخ هوش مصنوعی رو به یه تجربه‌ی سرگرم‌کننده تبدیل کن. یه بازی کوچیک، یه تجسم تعاملی، یا هر ایده‌ی تازه‌ای که به ذهنت می‌رسه.
🚀
⚖️
داوری روی زیبایی کد نیست؛ روی کیفیت خود تجربه‌ی انتظار، اصالت ایده، ارتباطش با AI، قابلیت استفاده‌ی دوباره و کیفیت اجرا تمرکز داره.
💰
جوایز:
🥇
نفر اول → 20000$
🥈
نفر دوم → 8000$
🥉
نفر سوم → 4000$
🏅
رتبه‌های ۴ تا ۱۹ → هرکدوم 500$
🔐
+ 20000$ جدا برای بخش ویژه
📌
مراحل شرکت:
ثبت‌نام تو
commonsmade.com
← بخش Hackathons ← Join the hackathon ← ساخت پروژه تو بخش Code ← وقتی آماده شد Publish کن و تو Hackathons ارسالش کن
✅
🗓
مهلت: ۱۷ سپتامبر | کاملا رایگان
اگه مدت‌هاست دنبال بهونه‌ای برای یه پروژه‌ی وایب کدینگ بودی، این هم خلاصه‌ی مشخص داره، هم جای خالی تو نمونه‌کارت رو پر می‌کنه، هم یه جایزه‌ی جدیه
✨
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVqAiMvhJyF6ymfrInNSIZYmc8dAVoK2Y16RFt09VfXKVCgFovvfBqNDBzDxgVsfyH-4al3BstrB0PxD05BxOhAfeW48fdjWh8Cvs4CbDn5bn-KsYS6cJEeh7-KVc9Jo3vEHAAvJAL7EIplRnrkZSh_EKMu6RLMXgUuE3mb9Ek6Kiu5eTOfSymsIqvoOGOdTbRmraJzbeBzTGO_7NUFUS_PjIRJBOygN8cvRfS-2wf1YbjIVKBO7MxwGu1HDjR_aOYl4nWFgwqvKtDrJmnO0Kg-Tjao0J2eqitQAFuWuXZatocWz7ckNlPlTQH_JTD2-OK7lSH0gR2hBw9n0hJPOzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM-5.3-Flash به صورت رایگان
💥
🆓
شرکت
z.ai
کمپین Global Build رو تو اپلیکیشن ZCode راه انداخته — از ۳ تا ۱۸ سپتامبر
🌎
⏰
دسترسی روزانه:
۱۰ ساعت ،  به وقت تهران: ۱۸:۳۰ تا ۰۴:۳۰
👑
کاربران Coding Plan:
هر روز، تمام ۱۵ روز، رایگان و کامل
🥚
کاربران جدید عادی
: یک‌بار ۱۰۰ میلیون توکن رایگان موقع ثبت‌نام (تا پایان کمپین باید مصرف بشه ، با اکانت جدید ثبت نام کنید )
⚠️
توکن‌های رایگان فقط داخل خود اپ ZCode کار می‌کنن، نه از طریق API.
🔗
لینک سایت
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17211673d.mp4?token=CzkXjuMgEzYB2AzL6sg8In6T1EYjpokIky6TW2oraTzpTIBwGrCs5sZ-pYaVpsu3pBjfnqHUZuRxGg6Dptl7N-qyoGbtqWPs49lcJdWhn3jL8AUx93HihOq8HaLyjkF4VGkQ7ul7SlHGdPOkFl_jVzSUs5pdhtM5-cBzER0GhJysYo87ZQIm8a3E2Mws4RhipCRFCJX3yOcIRW4ggdAT1umVJkjFjdYgqF1wf0Ahq2vcpyNEAg5L6100G-mF5hQwesBJ3pt7ph4VTFItxO0O4peaVhf1iNIVAhCIJQuDSmMdOdchDHGvYxTRN9MRwiBJhe1FjEbp52SNX8B5d6EjVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17211673d.mp4?token=CzkXjuMgEzYB2AzL6sg8In6T1EYjpokIky6TW2oraTzpTIBwGrCs5sZ-pYaVpsu3pBjfnqHUZuRxGg6Dptl7N-qyoGbtqWPs49lcJdWhn3jL8AUx93HihOq8HaLyjkF4VGkQ7ul7SlHGdPOkFl_jVzSUs5pdhtM5-cBzER0GhJysYo87ZQIm8a3E2Mws4RhipCRFCJX3yOcIRW4ggdAT1umVJkjFjdYgqF1wf0Ahq2vcpyNEAg5L6100G-mF5hQwesBJ3pt7ph4VTFItxO0O4peaVhf1iNIVAhCIJQuDSmMdOdchDHGvYxTRN9MRwiBJhe1FjEbp52SNX8B5d6EjVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌍
Pythia — رادار زنده جهان برای هوش مصنوعی
ابزاری متن‌باز که وضعیت لحظه‌ای کل دنیا رو جمع می‌کنه و بهت میگه احتمالاً چه اتفاقی قراره بیفته
🛰
🔺
بیش از ۴۰ منبع خبری و اطلاعاتی رو هم‌زمان رصد می‌کنه (اخبار، درگیری، بلایای طبیعی، هشدار آب‌وهوا و...)
🔺
پیش‌بینی از فردا تا یک سال آینده
🔺
کاملاً رایگان، روی سیستم خودت اجرا میشه — بدون اینترنت، بدون سرویس ابری
🔗
لینک گیت‌هاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.56K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=nHWavLCGGwy1-2eCNjgapXEK4mDpsYLO0S8Mu6JDHMlqFVUzQVbtY2kyUw2LQEIC6_sNIh9KMst3AE6O5zFUefmZK846iyG21HbDub-Xfjg7RatvqTDj83zUCZmHStaVY6hD3k6p3hbSScbiVfsjkje7MOD5ClIa3qbTFdo3qmpsjHErmjKzEh7wDYnP_1Pi1Vd4nirULbVoEsLpWVxQTNJ5oh1KihsKMOjWi-vzBghTfr1cxFMUVowJDtaFyIPjIY9YedkmgLIczDu60r9Xbq65SnOPzI9Mwo7LwZAkve1HfcLzgCh_vv4UacjUGlt7eUVEGHAeTcBZEnip1uKWzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0211ff0275.mp4?token=nHWavLCGGwy1-2eCNjgapXEK4mDpsYLO0S8Mu6JDHMlqFVUzQVbtY2kyUw2LQEIC6_sNIh9KMst3AE6O5zFUefmZK846iyG21HbDub-Xfjg7RatvqTDj83zUCZmHStaVY6hD3k6p3hbSScbiVfsjkje7MOD5ClIa3qbTFdo3qmpsjHErmjKzEh7wDYnP_1Pi1Vd4nirULbVoEsLpWVxQTNJ5oh1KihsKMOjWi-vzBghTfr1cxFMUVowJDtaFyIPjIY9YedkmgLIczDu60r9Xbq65SnOPzI9Mwo7LwZAkve1HfcLzgCh_vv4UacjUGlt7eUVEGHAeTcBZEnip1uKWzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔍
شرکت Anthropic ابزار رسمی بررسی محتوای Claude رو منتشر کرده
راهی برای فهمیدن اینکه یه فایل با Claude ساخته یا ویرایش شده — مستقیم تو مرورگر، بدون آپلود
🔒
📎
دنبال یه نشونه امضاشده (C2PA Content Credential) می‌گرده که Claude موقع تولید عکس، ویدیو یا صدا داخلش می‌ذاره.
🖼
فرمت‌ها: عکس، ویدیو و صدا (تا ۱۰۰ مگابایت)
⚠️
محدودیت‌ها:
🔺
فقط نشونه Claude رو تشخیص میده، نه هوش‌مصنوعی‌های دیگه
🔺
نتیجه «پیدا نشد» یعنی نامشخص، نه «قطعاً انسانی» — این نشونه با ادیت یا اسکرین‌شات پاک میشه
🔺
هیچ اطلاعاتی درباره سازنده فایل نشون نمیده
🔗
لینک ابزار
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=dC-MbcPtbwpUbsN7ZRUWyQwODbmefVpmCAR9sreXvPs5EfkqJkM92crAHavjhorErSjK3wj7-A4DKHCLNNLNFHcgcVAuiJUMN39-he2eqrUtNxHL1OQSnvc2KJ7LwgKDQ5TUXt0jJe0ubVBjxc4ffv4FfialpxgKTiXa_5QN6c279uUujn7NHWebYfA5HrVSNqmkzcJA_zHx9A91Fz_4_PssIPnIoqKyhBWUjLB6iqAvFt8zMO6Ya9sRQot0B2vly4RqKAZOKwEGhnjge5lav8DO9i5N5CZu7NvWf--dtyoGaojom2WdIExF7D0N2di_tp5Qy1zuxcoZ_qVr2EWvUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424c6d8acc.mp4?token=dC-MbcPtbwpUbsN7ZRUWyQwODbmefVpmCAR9sreXvPs5EfkqJkM92crAHavjhorErSjK3wj7-A4DKHCLNNLNFHcgcVAuiJUMN39-he2eqrUtNxHL1OQSnvc2KJ7LwgKDQ5TUXt0jJe0ubVBjxc4ffv4FfialpxgKTiXa_5QN6c279uUujn7NHWebYfA5HrVSNqmkzcJA_zHx9A91Fz_4_PssIPnIoqKyhBWUjLB6iqAvFt8zMO6Ya9sRQot0B2vly4RqKAZOKwEGhnjge5lav8DO9i5N5CZu7NvWf--dtyoGaojom2WdIExF7D0N2di_tp5Qy1zuxcoZ_qVr2EWvUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساخت رایگان ویدیو با مدل قدرتمند Seedance 2.5
🎬
🆓
خبر خوب برای علاقه‌مندان به هوش مصنوعی! سایت Dola مدل Seedance 2.5 رو به خودش اضافه کرده و حالا می‌تونید هر روز به‌صورت رایگان با این مدل ویدیوهای جذاب بسازید و لذت ببرید.
🍸
🎉
✨
ویژگی‌ها:
🔺
تولید ویدیو به صورت…</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDk0Z6-9WLKbr-fdVuG-A0-1NftBupZZByHB6Ouy0yw3vteRrlFLfZaaPfPAe5Hb0fTIIiKCSxwVTSNm3JbsRw_RwlZrY_b2pXfvdnBD68gD5bCW91uKQoGRkUnaTYE44C1HnxtPECenfRzMUU8VNhHc21lcIYBgr_JjmsSurv-3y7cb08ngPh6Zhztw16kXHp1iX_Pt_jqbCHO6-X70htP2fjK5ImjmvI7SOm_sv4AT7zeJR6gTXJln9iKoeGCosVqPy0ltCSoDgP3PxUfUoPlJNPuh2nxs6vz6cfzTgk9fG8Yfk6bVeu5VYhK8AxKXO53kxnfSa16DRzM12837Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرفتن API رایگان GLM-5.3 از طریق TokenRouter
💥
🆓
بدون کارت اعتباری، مستقیم قابل اتصال به اپ، چت‌بات، اسکریپت یا هر ابزار هوش مصنوعی دیگه‌ای
🤖
📌
راه‌اندازی:
1️⃣
ثبت‌نام یا ورود به حساب TokenRouter
2️⃣
ساخت API Key
3️⃣
تنظیم Base URL:
https://api.tokenrouter.com/v1
4️⃣
انتخاب مدل:
z-ai/glm-5.3-free
⚠️
نکته :
به دلیل رایگان بودن ، مدل کمی کند هست و باید در ساعات خلوت استفاده کنید ، محدودیت و ریت لیمیتی اعلام نشده ، این پیشنهاد به مدت محدود در دسترس هست
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=v2fekaYOQdLaYoijIeQEVHQYGYf3YG7NSWVdOblpFxO1jGtOoDMEioaSGrf2C-X92_MHYT2SftnuXI--z7c5w3s2XYFoeEy2Qm22J5ELzLK6MyOV5dUV7Vtgp88Qq8vPDuXrHgcMva-45EZGHFHdwKHPBn7yq-i9LpYX1c1dGUe4uBputYBOn9P1sUP5NRc6tPvAjcp70n7mP5gnBqKyduCY9XZzveFV5sXPsnu89Tv6okNYQ1dS5A38VJBJL7k6Deb0S8Yw0XQUBgQn-X2EN6p_lRJJp0os4OlUFrav279Vj7H1Bkkv8sXc8VPOL3PK-Y5tYHVDf7MXa1gEEtoVnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=v2fekaYOQdLaYoijIeQEVHQYGYf3YG7NSWVdOblpFxO1jGtOoDMEioaSGrf2C-X92_MHYT2SftnuXI--z7c5w3s2XYFoeEy2Qm22J5ELzLK6MyOV5dUV7Vtgp88Qq8vPDuXrHgcMva-45EZGHFHdwKHPBn7yq-i9LpYX1c1dGUe4uBputYBOn9P1sUP5NRc6tPvAjcp70n7mP5gnBqKyduCY9XZzveFV5sXPsnu89Tv6okNYQ1dS5A38VJBJL7k6Deb0S8Yw0XQUBgQn-X2EN6p_lRJJp0os4OlUFrav279Vj7H1Bkkv8sXc8VPOL3PK-Y5tYHVDf7MXa1gEEtoVnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اثر های شگفت انگیزی که تا الان توسط GPT 6 Astra خلق شدن
🚀
✨
🔗
منبع اول
🔗
منبع دوم
🔗
منبع سوم
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7622">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/ArchiveTell/7622" target="_blank">📅 13:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7621">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oynX9pi7PJaz0FveH3Jit1C09Dekxbm6pvD2TZoL41pikUzXD8QLzDo143A7SBSqmSS8natP8oh8IpfWtsUcs1LDIo0QaFtT_cUUmMdB2JkZQ6VVsR0eganHQ2oSZpg8KQLU-NP0_TLW_oTBX1lKWjX82XJLj7obgCqFsvFl8cqh0nDlWwtjMd7ELZtz1z9pqOeAV3jCyCl5Shzh_eYdv3P8Zvc5G3JLBY4X46LD5Pe4IcwWwDu3uwy-oJDjQT576lgrZuaUphVPudd9UTxx5D6Z0sTFVM5DD5ztsn3iTtb-hUprCevhc6rrYxVZdNhehHOoylhEIMPdCobIZPyigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
کتابخانه پرامپت YouMind
بیش از ۳۰٬۰۰۰ پرامپت آماده برای هوش مصنوعی
100% رایگان و هر روز آپدیت می‌شه
⏱
📦
چی توش هست؟
🖼
پرامپت تصویر (+۳۲ هزار)
🎬
پرامپت ویدیو (+۹ هزار)
🌐
پرامپت طراحی صفحه وب
⚡️
بر اساس مدل‌های داغ:
GPT Image 2 · Nano Banana Pro · Seedance · Gemini · Grok Imagine
🗂
دسته‌بندی حرفه‌ای بر اساس سبک، کاربرد و موضوع (پرتره، انیمه، سینمایی، سفر، اکشن و...)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkPtF_6q9lW3IbZPPL0Y61wwF39km2k-By-5Giz_JBSSH3LMDcyK8nAXT1Kj1GV_Gcha9Z8UAShlxJndDUItYPfB7h565wN8nmf3FA3B9V_-1jJ6Znva0vZMwp9rhUQ6E1UMMbWPYWWtsFk6Y59d7V33PWHOU9Cqc0qQJ9ADLUyBJDbqSeJks8n_-qfS6Fi3bHGnk9ILafLk0y1uF7X_TM-iwD8kwz_z8f3F5-i6WJ2Ol8YFdG2WuE605BpHkxjM3jVqnN7qB3L6_wQnn95-CvP2gGOCanfyxRta-UJr447pxjQFssecL6P_JJ5mAIA3650nWP5ICoFVofYMPJEGLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Fable 5.1 2 days Free
⚡️
⚡️
https://arena.ai/text/direct?model_a=claude-fable-5.1-high
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNyBW42Qdjj1YcSdOblE1aM-CpybSaPcpeRAcDMTRc1EiICAAnmGeaiBgFLokOQoYF72-CrzCGIcUqIV7FBJrydH-tbhZZxp2J5zTbbTF2VhGvdoqMV_Lc_WPyd6f0fcb6BwcfiXGrXmaa_VW5-MqWPpicBIdQpkmlqbnie7hUsH-swNoFm3sdaMAPU_zpetuIe23jOXxQ4ym5VD7HqVKFBdGd-H4yjhqUw0I-p1UJG2BRCDa9jMWbZZwokE2gLtyWTGbeXM7jnNSEg-InfjNyKoqxiTTXOXz4KLHH3KEGmJpuWCg1T-2I5Ew4Wb9alvWe4Qty96QCNFn3Cd4nwlHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
خبر خوب برای برنامه‌نویس‌ها و علاقه‌مندان به AI!
مدل‌های قدرتمند GLM 5.3 Flash و DeepSeek V4 Flash الان به‌صورت کاملاً رایگان
🎁
داخل IDE چندعامله‌ی Verdent در دسترس هستن — بدون نیاز به کلید API جداگانه یا اشتراک مدل!
❌
🛠
روش استفاده:
1️⃣
برو به سایت
Verdent.ai
2️⃣
نسخه IDE رو دانلود کن
3️⃣
وارد شو و از GLM 5.3 Flash یا DeepSeek V4 Flash به رایگان استفاده کن
⚠️
نکته مهم:
این دسترسی رایگان دائمی نیست! محدودیت مصرف ۵ ساعته و هفتگی داره پس قبل از شروع یه پروژه‌ی طولانی، حتماً سقف باقی‌مونده رو چک کن
📊
⏳
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5Kd7mZqemm3r93vlF6AR5ND9zqBuuLvJphLYD6rHMENy48xmc3Z61mXIJkKoK69b6GYQOt8VY9-Ar8qMkMJwhEY4bNenPWsCZlxxgvIrsJI3GIFbH6uX6EbjXYnowY77C1-s_CZr2PBtY4XS0kfD0j1xt9tSxXhwFcNF3hfipVQvii9xwxrs7GzZ_YVBYBfF3EIUDvXcu9XZcYBJg44oKBNIbOY4c9RwEF1z86H2s0k39Ze2tJEShIFisE2VvSx7DJb65ALwWxUjXShL7L5LiHpErmNWySRx3hGXtV3JMDgjOWfyzVClxVv4ur70eL_EMoedPi98YI-S2z2IAGUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه
سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت، Prisma، Supabase، و اتوماسیون‌های ClawHub (اسلک، دیسکورد، نوشن)
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/ArchiveTell/7612" target="_blank">📅 15:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7611">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL: https://syntro.up.railway.app/v1
🔺
Model ID: claude-fable-5.1
🔺
API Key: sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell | #API</div>
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7611" target="_blank">📅 14:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7610">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GW49nccgleFMVl06BTpFShedGIQGJ7062xTOQRt82slC7w-NXtIhl9Y4I3oJfxohEj53pm4LX0MMvl0FhSsMDCNL-eQ1OcbL2GHvssCA_9alXnBdeXYlvxmWr7ATQR4JIgz3FmjBEeFvrP1ekUaU4lHnCP6CYTtSgS72WuwsMKoT-JuzixRUlitHcQdpDl3KdWqVdp1fZMIYaFdBrtK4tuLeu1eI9vOo3mkVBM6iw2AhYiyRVy0ejkh4lD-wRf_DQBSqz9Z-7M_OsOx7zg6q6iVpWUFyWShqbbP2DCg3Tm3WZumCgMRqfBPBB5Ld0yVN-jZEhD3G96nKGENNoz1NOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">10000 دلار کریدیت رایگان Fable 5.1
💥
🆓
🔺
Base URL:
https://syntro.up.railway.app/v1
🔺
Model ID:
claude-fable-5.1
🔺
API Key:
sk-pHXhquluKg5xOejYuGxaFkrZbgArNB7kX9HtvekqCwA64pWc
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7609">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ری اکشن بالا باشه
😁
🔥</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7609" target="_blank">📅 13:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7608">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">Free Deepseek 2.5 Billion Tokens
🌊
Base URL:
api.pkay.fun/v1
Endpoint:
https://api.pkay.fun/v1/chat/completions
Key: pkay_f38d9bbbfdaea88a190f415eb007ef2ffb74bed33961c366
Model: deepseek-v4-flash
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6lVfvDdt6aVpv5O6FPYdP32FTBmpE1bZTVoG8NUIA1vHl_m7s3e1IC6xRefcKasr7KMXfllsYY9pE81gDacpDK5PTu1WfFlPuq6-xPqua7DqN3roVyDY1VwQLdu5qFHHivbW9U1h7nD9GG7l3XjJ-15cUydtNvDIaVgMK29TjzTmnoXX-v9lle5BHVc3U6hzaHNlpJvfgcf3kCTV2kl7xrxWtGU4YppywTusfkdEWzWFGJIqfEMvx809sMTus6Pm0ALqnuZSM2JFJ0i0CjshgdXAcfEkgMUtdYIscG95F09gCXM7LgmRzXFutDLeK6UesgtYj_VJbrNHXzKrgOBcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
مدل Gemini 3.8 Flash در برخی موارد از Opus 5 پیشی گرفت - با قیمت 0.75 دلار برای هر میلیون توکن
شرکت گوگل، سومین مدل Flash را در عرض شش هفته منتشر کرد. Gemini 3.8 Flash برای برنامه‌نویسی، کار با ابزارها و سیستم‌های عامل مستقل طراحی شده است.
بر اساس تست‌های گوگل، نتایج به این صورت است:
⚡️
Terminal-bench 2.1: 89.4%
در مقابل 89.1% برای Opus 5
⚡️
Finance Agent v2: 61.4%
در مقابل 58.6% برای Opus 5 و 53.8% برای GPT‑5.6 Sol
⚡️
HLE-Verified: 54.9%
در مقابل 54.4% برای Opus 5
⚡️
پردازش ویدیوهای طولانی: 87.8%
در مقابل 75.4% برای Opus 5
اما این مدل در همه زمینه‌ها از مدل‌های پیشرو پیشی نگرفته است:
⚡️
DeepSWE v1.1: 71%
در مقابل 74% برای Opus 5
⚡️
Terminal-bench 4.0: 19.1%
در مقابل 51.8%
⚡️
OSWorld 2.0: 59%
در مقابل 75.4%
به عبارت دیگر، این مدل "جایگزین Opus" نیست، بلکه یک مدل سریع و ارزان است که در برخی وظایف به مدل‌های پیشرو نزدیک شده است، اما در کارهای پیچیده و تست‌های جامع سیستم عامل، عملکرد ضعیف‌تری دارد.
قیمت این مدل تا پایان سال 2026 ثابت باقی می‌ماند: 0.75 دلار برای هر میلیون توکن ورودی و 3.75 دلار برای هر میلیون توکن خروجی. پس از آن، قیمت دو برابر خواهد شد.
همزمان، گوگل مدل Gemini 3.8 Flash Cyber را برای جستجو و رفع آسیب‌پذیری‌ها معرفی کرد. این مدل در CWE-Bench امتیاز 47.2% را کسب کرد، در حالی که مدل پیشرو امتیاز 47.8% را کسب کرده است. دسترسی عمومی به این مدل وجود ندارد: نسخه Cyber فقط به متخصصان امنیت تأیید شده از طریق برنامه Fairwind ارائه می‌شود.
در حال حاضر، این نتایج توسط خود گوگل ارائه شده است. هنوز هیچ تست مستقل از این مدل جدید انجام نشده است.
⚡️
جزئیات بیشتر:
Google
⚡️
بنچمارکش داخل سایت
https://artificialanalysis.ai/models
اومده
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Gemini 3.8 is out
💪
از اینجا رایگان تست کنین نظرتونو بگین:
Aistudio.google.com
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/ArchiveTell/7604" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7602">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A0BBTYKjiH4VMPZgXGy9zA-nbJDejb87YRmyWuTgfxHZ6--f3aGJcHjZh0L0drKxRcmGMpbVstxshAXznNLinre615uyxz3cdLhgYkwS95Ryb37_3e5Prh880qOzyAMtxNt8JkzAVhPP7qnyBFOvCVVyr2pmNoydKZZXKjhfvM-ceOE18Y9udRa8iMdfD5Y3CStzhx7vU5ej4dH0nBYnb4pKPBE2iUI2Z06ESlmtyie60ui5mbPHxhZQhQRKZ_UxR_lXxah_XlTtdPHiA_jOM8U_kyK7YxT7papEsOPSB_aUpC4ePazZiF93icQGEJr2o-QNq6mGE8nqcN5A22NpJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOJBOn1tJIEc3wgVR9jXVH-bOY-KFNKwRdMS9hOfguL6axy6ei0h7VPfzdoS4Y79t59T4Di1HIgOWIYnKPku-TOYdNpUpaXEW0fE8RNhMpH7kQ6DyCheFHaQCPiLhA3MZQPoDHcFWx56hfzSK1xOAZPlGgWPZQGWiRTMta9374Aa7wDDxA5k3IWlb1DCMAWPTEKrQ0-WK_LOKtsU6NHt3iWFGUE6M8zVn8a1U9QWjLB_38qx7sNl7RdbCiZIYBgR3XS8elkyLl9Ws5p1c9speYgP7yN-PEvVKEuR0bPlPyMtNkzOP9bkRs0zALext0nU-ooKg3B-dP1LT2hSfkSFGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلاد فابول ۵.۱
⚡️
😎
با تفاوت معنا دار antrophic هوشمند ترین مدل ai رو داره
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">GoRouter  Opus 5 $13000
🔑
کلید:
sk-vWZcSRFLAJF0Id4G9AQ1HUZ4CmpWGIish3QseC7fuxb7LmzF
🌐
آدرس پایه:
https://gorouter.app/v1
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUl3PJ9O-tkHrT-WpVSPcvOzEbmwpqlLOhaVJ1j9aJnaoDdltayB9Fj7103SW7cULWXiZxAEi3-VJS1F5_JeCMFUvElhAYKQJy7Ih_StDecZwDaaJX1Z9mqFRIJlbbLOFoFp0GNhXK16D8GpOQF_gAjVP3_uQq1SXRmZkjN10ofvfD6pOGuoC5BN8DXE5ZfKw6IA9md3JgexbsIZNtKpw8mH0LEX435ZNXT9wTHS6uOtDQoeKwtuJdGAeW5lEiLTwYPkMVRsD-dRbd0heikWvQNjT7EOVayjgqSvf5lvssSCSqrvTgqziELCUt4xdMDQj79PKKsMiQDumC9TF-OBYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
ریپوی ArasClient پابلیک شد!
بالاخره سورس کامل کلاینت روی گیت‌هاب عمومی شد
✅
🔗
گیت‌هاب:
github.com/ArasTey/ArasClient
📥
دانلود مستقیم:
github.com/ArasTey/ArasClient/releases
فایل arm64-v8a برای اکثر گوشی‌ها
✅
فایل universal برای بقیه دستگاه‌ها
⭐️
اگه خوشتون اومد یه Star یادتون نره — برای ادامه مسیر خیلی انگیزه میده
❤️
━━━━━━━━━━━━━━━
چرا ArasClient؟
چون کار چند تا اپ رو یکجا می‌کنه:
⚡️
اسمارت کانکت
یه دکمه: همه سرورها همزمان پینگ می‌گیرن و سریع‌ترین وصل می‌شه
🔃
سورت سراسری
بعد از هر تست، سریع‌ترین کانفیگ از هر سابی بالای لیست قرار می‌گیره
🔓
فرمت اختصاصی .arasc
ک
انفیگ‌هات رو تو یه فایل رمزنگاری‌شده امن ذخیره و به اشتراک بذار
حالت Protected: طرف فقط می‌تونه وصل شه و پینگ بگیره — نه آدرس، نه URI، نه اشتراک‌گذاری مجدد
📊
اطلاعات ساب
حجم مصرفی، حجم کل و زمان باقی‌مونده ساب مستقیم از لینک ساب خونده می‌شه و بالای کانفیگ‌ها نمایش داده می‌شه
📣
اعلانات ساب
پیام‌های سازنده ساب خودکار نمایش داده می‌شه
🏳️
پرچم کشور
کنار هر کانفیگ پرچم کشور سرورش (از روی IP واقعی سرور تشخیص داده می‌شه)
📊
آمار اتصال
تایم اتصال، آپلود و دانلود لحظه‌ای + آمار کلی در تنظیمات
🛡️
همه پروتکل‌ها
VLESS • VMess • Trojan • Shadowsocks • Hysteria2 • WireGuard و…
💎
پر-اپ پروکسی، روتینگ کامل، بکاپ و رستور، تم روشن و تاریک
━━━━━━━━━━━━━━━
🔒
ویژگی‌ای که هیچ کلاینتی نداره:
کانفیگ‌هات رو با پسورد به دوستات بده — اونا فقط می‌تونن وصل شن و پینگ بگیرن. نه می‌تونن آدرس سرور رو ببینن، نه کپی کنن، نه برای کسی بفرستن. مخصوص فروشنده‌ها و ادمین‌ها
🔥
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7596">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNVOx-VFA7DPVATmC40-EYvnTpz79LszcxDdb9wwMt_h662i5reP3Inp3zZVqLP3X30YlWiurTUTVJvDWbNQUrrO9Xn4F5xChCO08JqUXhO5JnOW74VGHPQQIf9MUo57R8ey_Pu7AVJyp6XNAHrWLbGYHWuibPj7Xuw6q7oB6PKRtY_fotfem5R1J8w1RR7J1bFRf2898yp0mJLeLZmKq887gUFkySWR9QaXbeBUmoX6VBP91bBwejXgKO0GZJhRv2ufbe7-3c_s2nFITEUxZmJ8M-9I4YT_wkrlGIzJPoBtOBm8BN6ync2SBs99IbUeOiZQ3yIetol9leCMT77cMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧑‍🎓
✨
OpenMAIC — کلاس درس تعاملی با هوش مصنوعی
هوش مصنوعی داره تبدیل به یه دانشگاه آنلاین کامل میشه!
OpenMAIC
یه پلتفرم متن‌باز برای ساخت دوره‌های آموزشی تعاملیه — شبیه NotebookLM، ولی با کلاس درس مجازی واقعی
📚
📤
چیکار کن؟
یه موضوع، فایل PDF، اسلاید، صوت یا ویدیو آپلود کن، سیستم خودکار می‌سازه:
✍️
ساختار منطقی دوره + اسلایدهای آماده
🔤
آزمون، تمرین و سیستم تصحیح خودکار
🔬
شبیه‌سازی، مینی‌گیم و مدل‌های سه‌بعدی
👨‍🏫
معلم‌ها و همکلاسی‌های هوش مصنوعی برای بحث گروهی
🎙
سخنرانی صداگذاری‌شده + تخته‌ی هوشمند با نمودار تعاملی
📦
خروجی:
فایل
.pptx
یا
.html
قابل ویرایش
🔌
سازگار با:
ChatGPT، Claude، Gemini، DeepSeek و مدل‌های محلی (لوکال) هم پشتیبانی میشه
⭐️
۲۰.۷ هزار ستاره روی گیت‌هاب
— پروژه‌ی فعال و پرطرفدار
🔗
لینک سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7596" target="_blank">📅 18:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7595">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksMuzkYBZj9OybqYW-VjXraIoWo4lNWypQfV2Oc5zC2LfdTOB0liZpQpvAEea-_lkt8JpSXZMTfjtCHg7sf77V6Yyc9rJlbJxarWEYQFzCdYwzOVYGs1f7gQPWt0FFnihol51NZuEljZbIWoAsDLkBp4jRgyZJtJTrnJDjjvvroOa72UKRVKPE_pO1bjUCACGNqMm0sOAIAiFl_4fFSPLn4PEhPIP_wYOLRTphTd5T1ZZhQgrN5GaDHplmf4NHiRyl4vH4_ZO5OjeLBxTl3bGHssg-MtQk7brtJepXv7S-h0l3Ej-fujX-ui7VwBNOPIPWU_uncbflILmIcqc0l19g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
✨
۵ ویدیوی رایگان روزانه با MiniMax H3 Max — بدون ثبت‌نام!
با این سایت میتونی این مدل ساخت ویدیو رو به صورت رایگان امتحان کنید
🔥
✨
ویژگی های کلیدی :
🔺
روزی ۵ بار تولید ویدیو، کاملاً رایگان
🔺
هر کلیپ ۵ ثانیه، کیفیت 768p
🔺
صدای طبیعی همزمان‌شده
🔺
متن و عکس به ویدیو
🔺
فریم اول و آخر بده، مدل حرکت وسطش رو بسازه
🔺
نسبت تصویر: 16:9 | 9:16 | 1:1 و...
بدون نیاز به اکانت برای ۵ تای رایگان روزانه — با لاگین هم ۵ تای دیگه اضافه می‌گیری (تا ۱۵ ثانیه‌ای)
💡
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zq4zJoBipWB8dwIJ36PT0sjlckDxC6bkiCxmc_Lw14kV9Lcp-rZpA_GDgQu2lZHVIQLtvrn1BzP7KHoltY0qhWEkazdA3dAE8rzBQtlGqJhGLq7uJWZfHe1AyrNpvtF037DK1EyniNhM-DlopWfNIPrJN6xOCuSI1b7uBcGmU4xlLoc3GImZwucH0pedfB2iMvkgG9ozecmh-k6lKw_x9vsFYMR2netZYqcD_btSvPOF10hfor-XXdqoEWtDc85MLK4FuvmiQs7QWDdxiXDIeHuJRwf5HCiLZENre1KABQ5j6p0Ky30dcKXHK5GuU5y6iZrGtLG2tqsu0w1XSl5QQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔧
✨
دانلود کامل گفتگوهای Claude با یک کلیک!
معرفی
Discussion Downloader
— یک اکستنشن ساده و سبک برای Chrome که گفتگوهاتو با
claude.ai
به فرمت
Markdown
ذخیره می‌کنه
📝
📥
چیکار می‌کنه؟
کل گفتگو رو استخراج می‌کنه — همراه با:
👤
مشخص بودن نویسنده هر پیام
🖥
بلوک‌های کد سالم و دست‌نخورده
✍️
لیست‌ها و جدول‌ها با فرمت درست
🏷
هدر YAML با متادیتا (عنوان، لینک، مدل، تاریخ)
⚙️
چطور کار می‌کنه؟
برخلاف روش‌های معمولی، داده‌ها رو مستقیم از API داخلی
claude.ai
می‌گیره، نه از روی صفحه! چون توی گفتگوهای طولانی پیام‌های قدیمی از DOM حذف میشن و روش‌های عادی نتیجه‌ی ناقص میدن
🎯
🔒
حریم خصوصی در اولویت:
✅
فقط دسترسی
activeTab
و
scripting
✅
بدون آنالیتیکس، بدون تله‌متری
✅
هیچ داده‌ای از مرورگرت خارج نمیشه
✅
رایگان و اوپن سورس
⚠️
محدودیت‌ها:
🔺
فقط شاخه‌ی فعال گفتگو صادر میشه
🔺
آرتیفکت‌ها و بخش thinking صادر نمیشن
🔺
رابط کاربری فقط روسیه
🔺
نصب دستی (unpacked) — توی Chrome Web Store نیست
🔗
لینک مخزن در گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3KgLHDnDTY8xe-OKFEw2FOOFZiDenVdTZXYVCDXhAvEvsB3AsrVyttJ_B-iFPCbZTjvFbEoD3pH41reAeHK4PdnNw9IVK5gdz2F8HoVnRsgtrUv_8jZcBCSZFFFrZ0B7T3ZWCGy3vynW1V8tzpgoYKEvy9PqNJnvfvteZNK3B7yFByoMtYNuUV8q6RqEvV14eVmWflOI3QvCmIkbVAWffad4PBjoLGJm_6D4UTsxXDlm8-GKA1mSdxpc8_VwgO2A1VGUa1IcibSgqGb0zzRhBPR5ryc0QaMUyQqCttUEcBzVzbh-Nqcm-Wk5IG1HbJpZhPbfNeqO7dYCV6AVqjbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦆
✨
حریم خصوصیتو با هوش مصنوعی معامله نکن!
با
Duck.ai
بدون ثبت‌نام، بدون اکانت، بدون هیچ دردسری به قدرتمندترین ابزارهای هوش مصنوعی دسترسی داری
💥
🆓
💬
چت و وب‌سرچ با GPT 5.6 Luna
🎨
ساخت عکس با GPT Image 2
🔊
ویس چت با هوش مصنوعی
سؤال بپرس، جستجو کن، تحقیق کن، عکس بساز —  همه‌چیز رایگان و خصوصی، بدون اینکه ردی از هویتت جایی بمونه
🥸
🔒
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7591">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_Oo0YMNlVZ0vJt62ZJceYnpgIH532zTidA0V6TXI4n0Uv92ykeNvP4ELg7TvK7SB4taXZ--WpUjYA-k9ACalGBywDATag7lD1nPDfv0T-Z4jBp_Icw6dCutwFiLy35abUiGWDQFtvOipkz2EbyEpMX9JHzLRmhd59u9IozY2djZNnS590inbD8FJxUleUtu-caRvO4N4uRbQOfSLv0HEjAyBkekmM3n5dl403cV681L7tgdXEo3QnAz3N5-3qZzigvSb4vrNzYn9uqT6ziN1uQr60mbeiOCGGDDrDiXpLb5H4yGzKLJvx5Acab2DuWZYmLsRykeMA1Y4xpTVcjfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معرفی Hy4 Preview: رقیب جدید GLM-5.3 و Kimi K3
شرکت تنسنت، مدل جدیدی از خانواده Hy را منتشر کرده است که قبلاً با نام Hunyuan شناخته می‌شد. این بار، برخلاف روال قبلی، مدل به صورت عمومی منتشر شده است، وزن‌های آن در دسترس قرار گرفته و به سرویس‌های محبوب اضافه شده است.
اطلاعات کلیدی:
🟢
770 میلیارد پارامتر، با 49 میلیارد پارامتر فعال به صورت همزمان
🟢
ظرفیت پردازش متن: 1 میلیون توکن
🟢
حداکثر طول پاسخ: 64 هزار توکن
تمرکز اصلی این مدل بر روی وظایف پیچیده و طولانی است: کار با کدهای بزرگ، تحلیل چندین سند، نمونه‌سازی بازی‌ها و تحقیقات علمی و غیره.
در یک آزمایش کور، شرکت تنسنت 203 وظیفه مهندسی را به 163 متخصص ارائه داد. نتایج به این صورت بود:
1. Hy4 Preview – 2.99 ( از 4 )
2. Kimi K3 – 2.94
3. GLM-5.3 – 2.92
این مدل در تست‌های منتشر شده نشان می‌دهد یکی از قوی‌ترین مدل‌های متن‌باز موجود است.
نکته جالب دیگر این است که این مدل به طور جزئی در فرآیند توسعه خود نیز نقش داشته است. این مدل نقاط ضعف در عملکرد خود را شناسایی کرده، پیشنهادهای بهینه‌سازی ارائه داده، آزمایش‌ها را انجام داده و به افزایش 31.8 درصدی سرعت پردازش کمک کرده است.
نحوه تست:
>
WorkBuddy
– به صورت رایگان در دو هفته اول پس از انتشار
>
CodeBuddy
– دوره رایگان دو هفته‌ای، با تمرکز بیشتر بر روی کد
>
OpenCode Go
– مدل به اشتراک اضافه شده است
>
Hugging Face
و
GitHub
– وزن‌های مدل برای اجرای محلی در دسترس هستند
برخی مشکلات شناخته شده وجود دارد: مدل گاهی اوقات بیش از حد طول می‌کشد و نتایج نهایی را دوباره بررسی می‌کند. به همین دلیل، این مدل در حال حاضر یک نسخه آزمایشی است و نه نسخه نهایی Hy4.
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/ArchiveTell/7591" target="_blank">📅 16:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7590">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCI1NFbCq0jk01UUKcrgl2b1RSd0uevOvlCXewPqhXFgp6h9W1i1Ff3zTvlVehX4PKf5ilNGlg9qfu0SeDQLB47Pt-hrsAaECbUwQvG2IK_i4qpqKtxQoMI9mSfEqpI5GvfBV1P3mQUPyUjmhQVJGxPx8x6C64SqSvXoB9dOAJbfRKZ2ZH8kB2znf_1IfGOcML8bPDGfxcYXoTxY9kqCjuGcuP7H_-yMCIxpet6BmOTrhNOWSTonfHYgPvUZm-xVHMxHZzXTMoo2yIMA2ebxan3SaF2T2FKs9HCNhGKgbKfg_8E16wynr6zpOallCC6wVmbj3jn4mMgxbnwoZQWvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تبدیل PDFهای قطور فارسی به متن تمیز برای هوش مصنوعی!
نرم‌افزار ویندوزی و رایگان
PDF2MD Studio
. با این ابزار، PDFهای ۱۰۰۰ صفحه‌ای رو به متن استاندارد مارک‌داون تبدیل کنید.
فقط در ۳ قدم ساده:
1️⃣
تبدیل هوشمند:
PDF رو بکشید تو برنامه تا به عکس‌های سبک و باکیفیت تبدیل بشه.
2️⃣
استخراج متن:
عکس‌ها رو تو Google Drive آپلود و با Google Docs باز کنید (بهترین OCR رایگان فارسی).
3️⃣
تمیزکاری نهایی:
متن خامِ گوگل رو دوباره بندازید تو برنامه. نرم‌افزار تمام خطوط و نیم‌فاصله‌ها رو مرتب می‌کنه و یک فایل فوق‌العاده تمیز میده!
حالا این متن رو بدید به AI تا براتون خلاصه کنه یا تست امتحانی بسازه!
😍
🤔
پردازش امن روی سیستم شما
🤔
بدون نیاز به اشتراک پولی
🤔
اصلاح خودکار باگ‌های تایپوگرافی
دانلود رایگان از گیت‌هاب
(ستاره
⭐️
یادتون نره):
🔗
دانلود نرم‌افزار PDF2MD Studio
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxYIDf2eBKCqwseoA_naw5YGtLnCM9-mwzzJmycs2SuWxLik1EK59buu6ajql5krz8AVhV-2uJZjTo4puF-BPRvk5pEC7m5pcTxbDvE92U8qaE-7eKPGSo3HnV4pvv7HkI4wLg9jWKvFldpXfYSFYx9Ma48Jf5X6PLLNLbqNeW8tfHTBqJmVPM2lxnUeMtqMVbQGSIgmKieLnG3Z9ZwnIGsgIzeQOk-e_4IqOdKha5GXw7fk8pyTuh_HDDrLmzSyTrzH50e2YJxM4jxB-UPLRQwivR6AFyKW8Bc1pWew0bqQrjvjoCfvarB6gEahq-nxkQiBld1_KcAnPP6d3rE_Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100
د
لار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
25 دلار
و شخص دریافت کننده
100
دلار
دریافت می‌کند!
همچنین 20 دلار پاداش روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IklmTwAkrjYFr6ShsEeGGMQCXu6JSVVxgr4ytAKISYcsiKNrh5_cuWuj0heLWuiuvCvoTmezr0SIoKK6eSyGm8FI5DcO1uhe8IwVXpqBsmr0w1qLNQ6lJJHhAD8fn6CopgO9T1s-3s4kzXnxEGdF0EmfooH-jpvbqqoU5Ieirqh5LUIauDK4AEyKVI9QAeZdBFFiguCHmi1BLf6SnVlCTnLZH7W_ODW2pA6AVDe02-YvRaTFEGoswTU7kR2uKUwBPOzDZhbTVC67UOWuvtZ4m8tvJPmdcohiq_WoLij4XhtDNtQY2x2ha51i133q4m13om0JZUYTo9byWIMLcF--Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت 10000 کریدیت رایگان سایت Genspark
💥
🆓
با این روش میتونید داخل این سایت برای مدل های زیر و دها مدل قدرتمند دیگر 10K کریدیت ۱ ماهه معادل ۲۵ دلار دریافت کنید
💵
😎
Opus 5 | Fable 5 | GPT 5.6 Sol | GLM 5.3 | Kimi k3 | Grok 4.6 | Deepseek V4 | Nano banana 2 | Seedance 2.5 | GPT image 2 | Gemini 3.1 flash TTS
✅
❗️
نکات مهم :
چت متنی در این سایت نامحدود هست ، محیط وب سایت یک محیط دارای Agent هست ، همچنین می‌توانید از این سایت API بگیرید ، همچنین این سایت یک نسخه cli هم داره
برای دیدن آموزش کلیک کنید
✅
✈️
@ArchiveTell
|
#METHOD</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhXlofTm9FTT8Tj475ZCKY85vQKV37cNnDkkLZON6sZqC3uFUN3wIeCUH-hWEl2YbEv1iqXnF8zPOrKFIYQ-9aDb6mAeGMfR7fNJhuE4sRDitNjzaYhuVthkkNqqzTkxqdZNgHbBenFknVN-v1m5SYIToj7Az7dCZ3t2WQptNzhxSigVN3jRqlCMf5JocYxV1f5xkx9jlQZUQ53a8JS-GqrwC6NRY2hyWg1AM5koSjsl0izfmRaVijpoqD0de44s4QWC1P3UvArEik85ljbGrTyHO8tq_JpauN-qz1MRFtCK5FkuT1ibl7yRGd_3ykU6Cv9bcOt75HoU8C2UVTHmiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
ساخت تصویر با هوش مصنوعی؛ رایگان و بدون ثبت‌نام!
🔺
بدونه اکانت و کارت بانکی
🔺
بدونه کردیت و واترمارک
🔺
بدونه هیچگونه سانسور
🔺
تا رزولوشن 1024×1024
🔺
چندین سایز تصویر
🚀
فقط وارد سایت شو، پرامپتت رو بنویس، فرمت رو انتخاب کن و تصویر رو دانلود کن
⚠️
مدل دقیق استفاده‌شده مشخص نیست و محدودیت رسمی روزانه هم اعلام نشده؛ ممکنه در ترافیک بالا با صف یا محدودیت مواجه بشی.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=prontMq9CpU08pYvHwECEZpqEMNK_GAxoD1EKo3_5Hnw3WiksQZuNEfphps2QnGojz5sF_xebL9WMbG-YIGVVrFO1BuXuTvCPo02K9rSVAQ6bLkb9CSosdy_4v7YhqVhQ6-wA0Ahyuvh6QJn0CUAAAAl_YjYJD0o6SaOXoGFrRF4Uhc8gO5QpTHIFH-Wl6noUA7wf7REBOQ0ZxY61cyP6fQpei_XqBHX8RK2jRZpqo3nrf96jNyKCWJzjZsHFGcc7BP4LeXOhtXLJdymv_zFGSA4t8DvcVZ4DiM1bl8yD0MIK0PgvZLYSkjN_XNIgLtkoF9Thkpb0oZgi-HOjpiL5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=prontMq9CpU08pYvHwECEZpqEMNK_GAxoD1EKo3_5Hnw3WiksQZuNEfphps2QnGojz5sF_xebL9WMbG-YIGVVrFO1BuXuTvCPo02K9rSVAQ6bLkb9CSosdy_4v7YhqVhQ6-wA0Ahyuvh6QJn0CUAAAAl_YjYJD0o6SaOXoGFrRF4Uhc8gO5QpTHIFH-Wl6noUA7wf7REBOQ0ZxY61cyP6fQpei_XqBHX8RK2jRZpqo3nrf96jNyKCWJzjZsHFGcc7BP4LeXOhtXLJdymv_zFGSA4t8DvcVZ4DiM1bl8yD0MIK0PgvZLYSkjN_XNIgLtkoF9Thkpb0oZgi-HOjpiL5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدها ابزار متن‌باز و رایگان، همه توی یه جا
💥
🆓
سرویس NoSignups یه دایرکتوریِ از جایگزین‌های متن‌باز و رایگان ابزارایی مثل فتوشاپ، کپ‌کات و فیگما رو جمع کرده — همشون هم به‌صورت آنلاین توی مرورگر کار می‌کنن.
✅
🔺
بدون ثبت‌نام، بدون نیاز به کارت بانکی
🔺
توی کاتالوگ، ابزار برای برنامه‌نویسی، کار با متن، عکس، ویدیو، موزیک و خیلی موارد دیگه هست
🔺
همه‌ی ابزارا کاملاً رایگانن
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/ArchiveTell/7581" target="_blank">📅 16:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7580">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd_lH9t7ZEqp9RjMP8sQDwnKxjmfod5pOE6Djs4QkWu6VqEpxG_NOsKbMY08RvyVzFX6f48nFkFlj5nDED88d8cnkscpnkUpakWbaWQYpVE_uAoF9fveQK2CWgn0K0Duk1PE9N8mqXsBWLwkYlSeQWfmAMjP6k6JMHejCSPQVuXzdFgQZT_n32Jim7APihvDKyc45kOpANdIXz8TODqGqlJzFFBoYUQC6VX0Mj2wyBJJg8i0k0h9iV8ClQhT16Dn-0NNpsnmtnY0AA7TALTVsG_BU7FNF91tF0HGMUoOlwPMjQe7T6p3S3k_Qw1CZ6KVwIFKV1s8sUG7geKrZk9Fbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجموعه رایگان ابزارهای تشخیص محتوای جعلی و تولیدشده با AI
🔍
سایت
forensics.media
یه سری ابزار مرورگرمحور برای بررسی عکس، صوت و فایله که کاملاً روی دستگاه خودت اجرا می‌شه — هیچی آپلود نمی‌شه
🛡
✨
چیزایی که می‌تونی باهاش چک کنی:
📷
تصویر:
تشخیص ادیت و اسپلایس (ELA)، متادیتای عکس (مکان، دستگاه، تاریخ)، تشخیص تولیدشده با GAN یا دیفیوژن (Midjourney، Stable Diffusion)، واترمارک نامرئی، SynthID گوگل، کلون/کپی‌-مووِ بخشی از عکس، و متن مخفی داخل پیکسل‌ها
🎧
صوت:
اسپکتروگرام، تشخیص موزیک ساخته‌شده با AI، فینگرپرینت صوتی، ENF (برای فهمیدن منطقه ضبط از روی هوم برق شهری)، و تاریخچه‌ی فشرده‌سازی
📁
فایل:
هش SHA-256 برای اثبات دست‌نخوردگی فایل
⚠️
نکته‌ی مهم:
هر کدوم از این ابزارا فقط یه سیگنال جدا رو می‌سنجن، پس هیچ‌کدوم به‌تنهایی حکم قطعی نیست. برای اطمینان واقعی باید چند سیگنال رو کنار هم دید
🔗
لینک وبسایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7579">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=LibSZhOjerv1QdpDRwSSN5KDmaxFXBY0NaGGyrB_eWTtU7-6_iOlYm8dJZTcm-ZDT3my0xQkSZ-t81uOMEpvgjIWkgb2mZze82RoYVPX_QPb_5poyAHeBOwkxTJMPXeWCAvLvpzo1R-fcimjePGb3U78Tp1Dx1RzCKREpEeGI9F4AzC2saxvpms5uVbHDL4FBF0cwzUge-eDv-yZAHYnWaMyDc71SDbj-G1ntGsH7yUzNjvDz-EmFXjKLudTOsfbAfJFTRip8TawFceL1Oa4ZHIcwN6WWFQa2T2hIDf1C0XFD-LDYqA4l9DqlgAzTZSCpWZJsXwlDf3YPli8Y2QEhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7791db8f9c.mp4?token=LibSZhOjerv1QdpDRwSSN5KDmaxFXBY0NaGGyrB_eWTtU7-6_iOlYm8dJZTcm-ZDT3my0xQkSZ-t81uOMEpvgjIWkgb2mZze82RoYVPX_QPb_5poyAHeBOwkxTJMPXeWCAvLvpzo1R-fcimjePGb3U78Tp1Dx1RzCKREpEeGI9F4AzC2saxvpms5uVbHDL4FBF0cwzUge-eDv-yZAHYnWaMyDc71SDbj-G1ntGsH7yUzNjvDz-EmFXjKLudTOsfbAfJFTRip8TawFceL1Oa4ZHIcwN6WWFQa2T2hIDf1C0XFD-LDYqA4l9DqlgAzTZSCpWZJsXwlDf3YPli8Y2QEhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوی ترین ابزار افزایش کیفیت ویدیو رایگان
💥
🆓
🎬
هیچی نصب نمی‌کنی — فقط فایلو بنداز توی مرورگر
✨
خروجی با کیفیت 2K یا 4K، هر کدوم بخوای
🔍
جزئیات ریز هم تمیز و شفاف پردازش می‌شن
🎁
کاملاً رایگان — نه واترمارک، نه حتی ثبت‌نام
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7578">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUXFA1rd8rM_sHwTIXzD8OS62a3U93wlYuGJcWqhkSuxm5u0UoT4D2h8rDyA0FjH7aqtCxt2WEc8iqKEy6arliddJpsMiNRh6ndsTvuHYuh9pffDwxZmc7H4VcBxMdE6_kRMJNLphWmrxFjwsm8H3eWY0wxwXpobotz3FarE0rE4HvHrjb8DBg_gZllCQZOR1ov0khEk1Fc51vTQwfUcknkVi5svn7oOL0Toh1E9sLqeYpyaKxQEUEacbgHA6ckT_hA7q9JvaU-T0YWXM71gTYQAWeAyySEUCLAN6GWA8jIBtAcjelAHD9W6cxAxj3ts5rN4ynRB_9uFPGDTe4TXqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی به API مدل های رایگان
💥
🆓
مدل MiniMax M3 و چند مدل دیگه از طریق Ollama Cloud به‌صورت رایگان قابل استفاده‌ان ( با محدودیت روزانه و هفتگی
⌛
)
1️⃣
وارد سایت
Ollama
بشو و اکانت کلود بساز
2️⃣
با گوگل یا جی‌سوییت لاگین کن
3️⃣
از داشبورد اکانتت یک API Key بساز
4️⃣
کلید رو به 9Router یا هر سرویس مشابه دیگه اضافه کن
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjQUWWG-w0IsN3cwfHLBVIs8_7sHD9eSFRBfVohyeuyK4AdBrVeX7_fbS7NKJ2vOO7aaOx8aOvAX7TWyvJOM58D0lL99Dcn_yol7GrGGS-DkAm3wcRUvLDcoqIPL-UaXD10gueTHXc2Q6xrwrhLGD3eLsP4by93duTyrmP81RHyj44X5apAiMk1VEFrPOcman2TrTCRyqd2qIxzTSFQ6vWN1g3fqBxthbpWAYlGvKZaWxeOplRXFbqDPSaCaVf2_Jojj1uaw-dsd_uiJ8PytCcHBQYcFth_L5T8yKpQgnYgJlcztPnfgmpk8dip-42bMmxHDEVGRFdAiwkAoe9-gJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
DeepSeek Harness Studio
رابط گرافیکی ویندوزی برای DeepSeek Harness
🤔
بدون نیاز به ترمینال یا Node.js!
🤔
نصب خودکار در اولین اجرا
🤔
وب UI رسمی داخل برنامه
🤔
پشتیبانی از پروکسی داخلی
💎
https://github.com/ScannerVpn/DeepSeekHarnessGui
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNO1anu6DtuDpS9dIas4ZsA6X-s_vzydpktABi0D9JNpd-pxC74aGgyE287GAJLZpnqEIo7A4efxIybRlzrxDX_HxfLRWjs7xMMVrvmFZxduRB48483R8ixG1FL_tzqyy4Fvn45IfleS5mrgNFAWwozRAfUmwHdilJy2PrDuD8QpjNCmyl8K1qXD2pBvQnqzk58NtlJ2QeIHIdAnwIc5Dhd1zS7muA05sE_nZgVj2HpMBxrCFkwidRo6v7iEOgtpTqJmJghDeAviouo2fSuOv9JnGPe-Ovm7eMOsY2k6sjo0reSN5RDNfZPic1x1ogEGt_M9twLeZCIPLHoNMziStg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/btunidV8cFRn4HKWHfQ-Q3pZXblctD4nzezgugPqysekpKulXqvWVaFAa2WlRyovcoObAEIF5VzLJzWI2PI_Do83Wd00BtohodJWvm3kmPy6YIw_EtW5-1zlZ1WKHeX20YBbNDn3zTE49syzQKM5eCMu030OBEvlA46hIpaArL6YVtq76_LjKiry3cMKbnhWyvK9gaiCzVboVLEsiIkQJrtpFaO3prgoKKyByvtSeEOdgcFSTUiUcmz4yE0D7MkJtHyerP0qdd969Bo9ZZp690KXHXNsakhEf1fxl7dz9AbFv4-OUxpfY27QVrtkj_FWXk7d_Tvo-idY2VECuIZUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAM2Ug94qjINbjck64YEBVOc2JeNd2gTnv3XH_wohqH9gFMkE_NI9V8HD08FYw1-zY7hFK9iW4ez7HVcQ5gAD8zByoCWDicXMBhPM2YQMHtpQdTHq8rRzGWaJPWAZ8g7ToX5oO_ck4fSRX27H_58kbPpMYPTFrChaPhN191pyxEla9Sb4p3zfQLImotXiM_quRM5AbWjVcjf1keXEuD6UyXMKN_9qEVQw4bFHQBE5KuKsJGDt0vuZ-4zK76kiG3QkVG_I_Q_pv6lz5Dj7oFQUl6dQPEIHNYwZ08wsYdw3R1ovddLY7r2WHuCFUKpEbRoCBy8LEDK442c4K0wSV3Crg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6lGfxn7vlWpWcxABTgUNMmHWv7kwQIquocvLmkiWHmtFM_eZ6NxFkE0Dq4VP9qDJ-ufAQQM9a9S5VvkCpm7N-g7fTrvqLkTRWgRcrWR_L_t0gU3S1JpldMNxNFpvphG8hSsP9eNyKpKZJBYl01H1hSD5ZEbHkP93Zfzu0oQ764p_q3RXbDZQf_i0lg0lTOITg0qg6JrSBw7SAjzfxtwQDNqCY8a-8R_aAJmDKKCEFl8zafUvv6iybAOR_1ECb2g5WhAd2leESkxEuRaVrhCcNBNMrEVAh-v8eIWitv8mUAOcM4ReCKzzHR0wwlY0e3_16qyMNqCMQy5HydLspdouQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🛍
خرید اکانت
Windscribe
با کریپتو از طریق
Build a Plan
اگر قصد دارید اشتراک
Windscribe
تهیه کنید، می‌توانید از بخش
Build a Plan
پلن دلخواه خودتان را بسازید
⚡️
کافی است مقدار دیتای موردنیاز و مدت اشتراک را انتخاب کنید، سپس در مرحله پرداخت گزینه
Crypto
را انتخاب کرده و پرداخت را با ارز دیجیتال انجام دهید
🪙
🔵
انعطاف‌پذیر و اقتصادی
🔵
امکان انتخاب لوکیشن‌های دلخواه
🔵
پرداخت با ارزهای دیجیتال
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7569">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DOzPfofJSqqahKXbGYerBAENyezMk3VLptkrJ-e3aFvsq9e2pQlQQ8aKiWDQ29DEQXlAzZs397c_PKq6n-lqecbbZvehr3z-sfDccfTC8WZtjqzlV3qDoCaVIA1lu6xkOwlLOP-93GEen4bCVWXSdUb5QYobDZCZaiWHpu0Ie97BA-zUzzXjDjwIC-DXD1yfUAjbfr7vR0vMExMQZWqMVZvHrRnbH0U76_i-5wxw_X7tttUZJhFxANDGNM_7_kNA-5w84CoHNuWkevHnHd0cVRgfcgnZ1w3VQCEHNyf12l95Aj5VjbQNIOIKuNVkn9qWT9-ltNcshzQ3qr1vdfYEVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!
‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون
‌GLM-5.3 Flash⁩
محصول شرکت چینی
‌Z.ai
⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی تست واقعی با ‌Cline⁩، هر دو مدل از پس باگ بر اومدن، اما Ox Alpha با مصرف یک سوم توکن و سرعتی خیره‌کننده‌، برنده بی‌‌چون ‌و چرای میدان شد
😎
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/ArchiveTell/7569" target="_blank">📅 17:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7568">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">عکس‌های داغونت رو تبدیل به شاهکار کن
✨
دیگه لازم نیست از عکس‌های بی‌کیفیت بگذری! نورون InvSR رو پیدا کردیم که هر پیکسل رو زنده می‌کنه، بهش عمق و جزئیات واقعی اضافه می‌کنه.
🔥
📦
نصب لوکال از
گیت‌هاب
🖥
آنلاین رو
Hugging Face
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7567">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">Avast SecureLine VPN
4KAX6F-Q7LM6J-5LCJ6E
3N7RAW-SG38HJ-5LCJ7W
BJS8N3-NNAVTJ-5LCJZJ
J3BSAR-XJZR32-5LCJME
VUYR9T-JZ5GBJ-5LCJVN
23RWWJ-SEAQGJ-5LCJTN
GFU46H-QA2CDJ-5LCJBE
7SKUU3-S97Y42-5LCJD6
UENGEB-Y9NGA2-5LCJEE
EBF8PY-8CPH82-5LCJ6J
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/ArchiveTell/7567" target="_blank">📅 14:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7566">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRS3wSlSgIFi2oiuQQOKXbGhcXhPDjBMCAeYSe387HArP3gc2_SvX3eEwGsaalXqzaNqBszkiTZT_1-jeHDmVI6qyTDQoytqAoY4uj6-UTQLBuMbeknNIaUxVc8VVprqfCYIo3lUZOTuPiO4WgpqW_h8xgF2jaSfgnUhiU4ke-9JZwbSyXH1tRci2pXAye6m8difnbkWkoYI2qhREqZjQq0v2Xyvc4_2F-ZH6BZKEJd_6SSVLe3wuc04qe4TcMR7-6wzuTnaTCbvvpMkBjgTVh5Ty8uzvCv-Fk2vywQfVWg7lWVXoP7oW1vZXxdck_6TS2B2jKuiZpqFvIDWkl6wNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">175 دلار برای دسترسی به بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | GPT 5.6 Sol | GLM 5.3 | Opus 4.8 | Deepseek V4 Flash
✅
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب
قدیمی داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
100 دلار
و شخص دریافت کننده
175 دلار
دریافت می‌کند!
فقط در کلاینت های گفته شده در Docs میتوان API را استفاده کرد
‼️
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlRYJEUI6tJksyGwkI22kIOSw_pQJUANAnjlLGxl3KY60LnM22kdYEyLihpN0hrk80HNnpxw7j030S37PjAfCoZjzNShTXDkWI0QLQecMfrrIpy2f0Let_J9gv3cx-8ifRGaLNyAjAQnAHa672GFF11x_TFvOEEiHph2EU94Z2dkXB9Wg3PIvtozLlc40_2LfcaafvHIQLLkFlurRR3ioq5Z9msl1K4x3gpTPR9SLHDhYPQdxrFdEbBXu0by3Sb6Xsz3ZqkA61V6jOD7IO__2fVcy0IqQ_9tG9ispCRvVC1GTm5NJ0IDYQ9O4AGsasZJQPHTxyQYkisE3QVnAggWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل‌های قدرتمند MiniMax M3 و M2.7 به مدت ۱۴ روز کاملاً رایگان و نامحدود روی GMI Cloud در دسترسه
⚠️
⚡️
📌
از
۲۴
اوت تا
۶
سپتامبر
🔥
همراه با
Speech 2.8
و
Music 3.0
🪧
دسترسی از طریق
API
خود
GMI
یا
OpenRouter
💎
بدون محدودیت استفاده
⛓
Link
🔝
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/ArchiveTell/7564" target="_blank">📅 18:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7563">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0KiuhSCmUnn9oKcTqvCZMTjWeLkUD3EQknIqQySmr_ZPF9sOy7xJ9aeKYJjBFTHMxqyzt3XoePMr0lsP2k-P0nwZnQt9B_14fbyq8hvm50oo9EcDbC5NYa9HsWkabbAD9VpbspQli82AakH2c54ZCCQN4Mm8fa3YZJl8tsHlmxWH86s9ftcYaJg0jIbFchrmv6LQorzbux8g8Gy19SA7phB2_iPiNBYmRY9vn57SYKq0W3dy3izcUTZ1Di_NnwgStpoXEAD1omjC52m4DbPv2Rb47HJ93GxP7HKimIKsj8WTtOVGWZ-XDoU-S2dpu-XWyOGKvznw3x4kt2DdXan6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به API بسیاری از مدل ها مانند
💥
🆓
:
Gemini 3.7 Flash | Gemini 3.5 | Flash-Lite | Gemini 3.6 Flash | GPT-OSS 20B | NVIDIA Nemotron | Nano 9B V2 | NVIDIA Nemotron | Nano 12B V2 VL | Ling 3.0 Flash | North Mini Code
✅
📌
Base URL :
http://aihubmix.com/v1
🔗
لینک ثبت نام در سایت
🔗
لیست مدل های رایگان
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7560" target="_blank">📅 23:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7559">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNC4F3bmeHLPMiZSh7xBjZxCJip12ISy4zPu3Yh1o1Ce-PYa5UhYkuzusLLT2n7AGZCGtkRNua2qloCJGadHquQx1ganoxriqAxSiOH8mDy2iVWup-8kCDHIgLI6IN9xKeMeLl-gbuigEcTDlvhPcx38Me4QhfJCIQV40TlZuuERGM1VJy5fitDjg22tNhtQlI-AHDWrqjHKWH9B2Lx538V_4DD6BzcRujvhOOr2mklXu5zm5Qo4GZYf9D3hwbGoYvP-FSH2roVXGeYIl0-Qgu85SLIgYx3_g8Xczxds28-Nk0vtIxBhHkhYsjPoJn8we2GWtKfWgTDOjhrrqJvvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی رایگان به برترین مدل های ساخت ویدیو
💥
🆓
Seedance 2.5 | Kling V3 | Minimax H3 | Seedance 2 | Seedance 2 fast | Happy Horser | Kling V3 Omni | Kling O1 | Q3 Pro Video | Q2 Pro Video
✅
با این سایت 1000 عدد کریدیت معادل 10 دلار برای دسترسی به مدل های بالا دریافت میکنید
🚀
✨
مراحل فعال‌سازی :
1️⃣
وارد
این سایت
بشید
2️⃣
پلن رایگان رو انتخاب کنید
3️⃣
با اکانت گیتهاب یا گوگل ثبت نام کنید
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دسترسی به Deepseek V4 Flash به صورت نامحدود و رایگان
💥
🆓
به مدت محدود در این سایت این مدل به صورت کاملا رایگان و بی محدودیت درخواست قابل استفاده هست
✅
📌
Base URL : https://api.b.ai/v1
📌
Model ID : deepseek-v4-flash
🔗
لینک ثبت نام
🔗
لینک بخش گرفتن کلید …</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCOahITcAWZfedoy2FKunpdkEIfyxJrPp3ES-lGxr1oST5cMp8cG32FIB2_eYmedJeV8-asgqQJKhRmI9Cm7qog7_Miw3nS8qHVJh76OOMeFNG83CSTaNtggKq7kWqpdp04eNyhbMp9Nc4JFu3XbkTfVoHZWsciRoN8X-9WRslq56DUqjRtrdD2UK8bBgwkzHUSFOYQYOBwmnTV2Mo14Key0aUQe8qGKfXFBpb1ibA-mznDmnfV21y-lJ3_WLDJqOoGAd_AC_bMDaR0wbFP-dbqsjJs-YdhJJOMvzWI1XQZHYvp5KaqXodEFJYwUw36HGilQjAS3l8-iRtTk9yr_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
دسترسی رایگان به GLM 5.3
شرکت
Z.ai
یک اپ دسکتاپ جدید به اسم AutoClaw معرفی کرده که یه دستیار هوش مصنوعی agentic است — یعنی می‌تونه به‌جای تو روی فایل‌ها، مرورگر، برنامه‌های آفیس و حتی پیام‌رسان‌هایی مثل تلگرام و واتساپ کار کنه.
😎
🎁
هدیه ثبت‌نام:
کاربران جدید ۲۶,۰۰۰ اعتبار (معادل تقریبی ۲۰ دلار) می‌گیرن که تا ۳۰ روز اعتبار داره و می‌تونی باهاش مدل پرچمدار جدید GLM-5.3 و همچنین DeepSeek رو امتحان کنی
✨
مراحل دریافت:
1️⃣
برو به
autoclaw.z.ai
2️⃣
نسخه دسکتاپ رو دانلود کن (macOS یا Windows، نصب کمتر از ۱ دقیقه)
3️⃣
با ایمیل ثبت‌نام و وارد شو
4️⃣
۲۶,۰۰۰ اعتباری که داخل پلتفرم منتظرته رو فعال کن
⌛
زمان محدوده، هر لحظه ممکنه تموم بشه — الان ثبت‌نام کن!
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7557" target="_blank">📅 20:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7556">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کانفیگ amneziavpn
[Interface]
PrivateKey = YM8CabYhib72x4z1G3Tv6YPTzkN1EgieYgzRAiEOXGA=
Address = 10.0.0.3/32
DNS = 1.1.1.1,8.8.8.8
MTU = 1280
Jc = 8
Jmin = 74
Jmax = 195
S1 = 115
S2 = 80
S3 = 44
S4 = 21
H1 = 220741314
H2 = 689752078
H3 = 1491205382
H4 = 2102461473
[Peer]
PublicKey = MF3gfbfjik3PoBeXrASElNP8OOXDlalC1ZCmLfqUuSo=
PresharedKey = 5AUecEnESNGx35D0nM1REFG1HAGtUuLTxlzhUHDhkSM=
AllowedIPs = 0.0.0.0/0
Endpoint = 65.109.215.18:51820
PersistentKeepalive = 15
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/ArchiveTell/7556" target="_blank">📅 16:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7555">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)   همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟  پروژه «روح‌گرام» یک یوزربات…</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7555" target="_blank">📅 12:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7554">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7t9IBAIhTKK7gtmUlS05-dI2ytf6BAoMyXTEiaMlHMBlS31CvVV89BFgwmtRyUTSY53W9WovffUCA6axewOWSXS9xQ3Ozx_ZvUVfZnKdask0Hc0PBQbgXF1jOnhqk0CJvXH7_tIg8O26v-AajQmnI-OBT3uBq3EyN2n21MlfAoNqMN9brgooeEhjgEbSVuKWt-_awWR5LtnukZudqxV2nB11nWx4ReFx3QwEgVc3rYfoANCTZv580x8n4nr1aEFSMWUu9cgXtW4pPcGpajW6-tD9SClDNCXhhGB1nw0NCr8g1OPFieLMwfoZih_APFLGES9xygZpzXv4Yw3bMYsXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
پروژه GhostGram (روح‌گرام)
همزاد هوش مصنوعی تلگرام شما که هیچ‌کس متوجه حضورش نمی‌شه!
🤖
تا حالا شده دلت بخواد اکانت تلگرامت اتوپایلوت بشه و درست مثل خودت (با لحن، شوخی‌ها و تیکه‌کلام‌های خودت) به پیوی‌ها و گروه‌ها جواب بده؟
پروژه «روح‌گرام» یک یوزربات فوق‌پیشرفته و اوپن‌سورس با اتصال به Google Gemini هست که مستقیماً روی اکانت تلگرام شخصی شما سوار میشه و رفتارهای یک انسان واقعی رو شبیه‌سازی می‌کنه!
🔥
قابلیت‌های خفن روح‌گرام:
⭐
کدهای رمزی و نامحسوس (Stealth):
با کدهای ۳ رقمی مثل 777 یا 666 کنترل میشه و دستورات بلافاصله بعد از ارسال پاک میشن تا هیچ‌کس نفهمه!
⚡
شبیه‌ساز واقعی تایپ و خوانش:
🌹
قبل از جواب دادن، اول به اندازه طول پیام «مکث خواندن» می‌کنه، بعد علامت ...typing رو فعال می‌کنه و با سرعت دست انسان تایپ می‌کنه!
🎭
تغییر آنی شخصیت
🎲
با یه دستور ساده لحنش رو عوض کنید.
دریافت و استفاده از پروژه از گیت هاب:
https://github.com/faithsaly5-stack/GhostGram
✈️
@ArchiveTell
| S</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=Wc6oinTzgnc1ZWLLaoJW5p-qulwhEdK2okZULkpemYb4KkE3o4YdG0YUd8jgMRarjEKnVNYo_j5Xg5085EQq1vnyo1EeNqlMfWNJaxx68wgJzmjSDp_e9IcwCyZ_yTN_jSmSxbZj3AyLlxky7vX7p7NweM8AUK6dH0V8Di1U-ihdRYzgEM6kn3TDF3P0arF32alp4ePD0QUxcXSoxSu8LdlgqESk4C7xmU_SqJL5zQgyZ_2NZZ20ofrtbCH8ZLLcmkBK-5KkYyTksNR3-w59VL6zfIAYVqHS4X6dscYd80QoRqGS3u5adXpmoLdXdi-MPm_tJRuB_-5Kc4-JoOGpUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=Wc6oinTzgnc1ZWLLaoJW5p-qulwhEdK2okZULkpemYb4KkE3o4YdG0YUd8jgMRarjEKnVNYo_j5Xg5085EQq1vnyo1EeNqlMfWNJaxx68wgJzmjSDp_e9IcwCyZ_yTN_jSmSxbZj3AyLlxky7vX7p7NweM8AUK6dH0V8Di1U-ihdRYzgEM6kn3TDF3P0arF32alp4ePD0QUxcXSoxSu8LdlgqESk4C7xmU_SqJL5zQgyZ_2NZZ20ofrtbCH8ZLLcmkBK-5KkYyTksNR3-w59VL6zfIAYVqHS4X6dscYd80QoRqGS3u5adXpmoLdXdi-MPm_tJRuB_-5Kc4-JoOGpUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚡
مدل‌های غول‌پیکر روی سیستم گیمینگ خودت!
محققان دانشگاه‌های UC Berkeley و MIT سورس‌کد سیستمی به نام FreeToken رو منتشر کردن که مدل‌های بزرگ MoE رو بدون کوانتیزاسیون شدید، روی سخت‌افزار معمولی اجرا می‌کنه. سیستم به‌صورت هوشمند محاسبات رو بین GPU، CPU و RAM توزیع می‌کنه.
💻
📊
نتایج کلیدی:
🔺
مدل Qwen3.6 35B روی لپ‌تاپ با RTX 4060 8GB تا ۳۹ توکن بر ثانیه
🔺
مدل DeepSeek-V4-Flash 284B روی RTX 5090: ۲۲ تا ۲۵ توکن بر ثانیه
🔺
حتی مدل ۷۵۳ میلیاردی GLM-5.2 روی یک GPU ورک‌استیشن قابل اجراست
✨
ویژگی‌های دیگه:
🔺
پشتیبانی از ۲۰+ مدل باز MoE با فرمت‌های مختلف کوانتیزاسیون
🔺
یک API سازگار با Anthropic/OpenAI برای اتصال به Claude Code، Codex و ابزارهای مشابه
🔺
نصب یک‌کلیکی با GUI برای ویندوز و لینوکس، بدون نیاز به تبدیل GGUF
🔺
متن‌باز و رایگان با لایسنس Apache 2.0
🔗
لینک مخزن گیتهاب
🔗
لینک وب‌سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=GhMHS663oeRqjtp4pGn0E1CPpZAvJtBkrEmOY9svDrnFK_SCAG_RtM8r-VhyTPXpxxaEuyZzKm5e4ITW74bymrOK5ofpfh407ngOinWjXmXeuKidJGlwdmM_EZKCq01KwjL3W-37FCA5TNfmIPD10t_N5yIoSoV8v0UYiZmXAW8jPewFEiHEMimbiiSHTxbHnbTeqIrx2AZx3Xba5k3F904mcoH3lc6KIw_bWQSeKwnLh4DFRq_uGJLe_GzWmWDsIIuFwJ4zWbyfniSJa2oQx3M3J4_51qK__KgyYKMVeAGvCaomZ_k5KB6mWWf_SlnCkWL-_GTZu4LmFyp5vwnp4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=GhMHS663oeRqjtp4pGn0E1CPpZAvJtBkrEmOY9svDrnFK_SCAG_RtM8r-VhyTPXpxxaEuyZzKm5e4ITW74bymrOK5ofpfh407ngOinWjXmXeuKidJGlwdmM_EZKCq01KwjL3W-37FCA5TNfmIPD10t_N5yIoSoV8v0UYiZmXAW8jPewFEiHEMimbiiSHTxbHnbTeqIrx2AZx3Xba5k3F904mcoH3lc6KIw_bWQSeKwnLh4DFRq_uGJLe_GzWmWDsIIuFwJ4zWbyfniSJa2oQx3M3J4_51qK__KgyYKMVeAGvCaomZ_k5KB6mWWf_SlnCkWL-_GTZu4LmFyp5vwnp4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاوت خروجی 0x Alpha و fable 5 در یک نگاه
👀
تو کل سطح اینترنت واقعا اتفاق های خیره کننده ای با این مدل رقم خورده
🔥
➡️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7549" target="_blank">📅 18:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7548">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrqnHh3gLVBQmJ9jTZzAAdY8d5GQMGdv4AQsIwoXXxVwdFs2uV9CSRdS4jABJC3cj1Xvbj4DcsMuZ3wCyVywOJgOemEFyXwZ4wdT8xUkvrpurtVXl1Ti2054UMH-3OLszPT2EFGsrtooXe1FkNWuo1YZXRLQz7C-tzJpPxxWp8aAim2gphOeOPlCCvvhVTfR7GRz5dcmW2mZalU1pR5C2lsms7LOV4nxoMwvzkT1H12Y3sSkN7WooOiATPfveBOThMjnCag60vHH9xvjfB4M8PVgn8HomsNKCBIvM4bFRQTg2klWmqPe5S5XBWlrF1jmw0reYtuqavOX7JD18v4qVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔬
دانشمند هوش مصنوعی که خودش مقاله می‌نویسه
یک پوشه از داده خام رو بهش می‌دی، یه جهت تحقیقاتی مشخص می‌کنی، و سیستم از فرضیه‌سازی تا مقاله‌ی نهایی PDF رو خودش انجام می‌ده.
🧪
✨
ویژگی‌ها:
🔺
کار با هر فرمتی: تصویر، صدا، ویدیو، اسکن سه‌بعدی، جدول، فرمول
🔺
درک مستقیم داده‌ی خام علمی، بدون تبدیل انسانی به جدول
🔺
سه مرحله: فرضیه‌سازی → آزمایش با کد واقعی → نگارش مقاله با DOI معتبر
🔺
اعتبارسنجی داخلی: هر عدد باید از خروجی واقعی کد تأیید بشه
🔺
سه روش اجرا: دسکتاپ، CLI، ماژول ادغام با ایجنت‌ها
🔺
پشتیبانی از Windows، macOS، Linux
🔗
لینک وب‌سایت
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7548" target="_blank">📅 17:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7547">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqRFgguNXbFCznAnPYMfMwz0-Lh9_Lw0S2mU_SxzQDuhhNdzdPHsBieOjD9iuwP6n4tu0HVG9UJ-7rlwb1ObQq45hBJHrJ4XFkOQPEUyss1fkZHbzU5L5dusV8IvdVmL22jKewyKqyyDdxGa6Nf2ARq-0ClR4ETR7jo_CdOujETPUSlb8YIfG5U5eh-144TdquK5aVByeqbjaMEaIXnOw69PyHOr56HqdtCT4SU4b5pMVdLaT3-2WqVXb6-gyYTmOMMsGn3Yr0PoL2_VuP9zSAMChztqaW8dLaBfYcCIswcAeIRYNSUrh5KWPs5_d69sZz1QqVME815gDCjQmIvsvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جدا کردن صدا و موسیقی با یک کلیک
یک ابزار آنلاین رایگان مبتنی بر هوش مصنوعی Demucs که صدای خواننده رو از موسیقی پس‌زمینه جدا می‌کنه. کافیه فایل صوتی رو آپلود کنی.
🎶
✨
ویژگی‌ها:
🔺
آپلود فایل محلی با فرمت‌های مختلف
🔺
جدا کردن خودکار صدای خواننده از موسیقی
🔺
پیش‌نمایش آنلاین قبل از دانلود
🔺
دانلود جداگانه‌ی تِرَک صدا و موسیقی
🔺
بدون نیاز به ثبت‌نام یا حساب کاربری
مناسب برای موزیسین‌ها، خواننده‌ها، تولیدکننده‌های محتوا و ادیتورهای صوتی که سریع نیاز به جدا کردن استم دارن.
✅
🔗
لینک ورود به سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/ArchiveTell/7547" target="_blank">📅 15:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7546">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOee-PyoKBqXUhPej7V4ZiFbr26tuA9UegsS1WVsbyMFerU8phXNg5azTOyxNyroqmfFW4gOwihamOeteCgDTOVJ_cCw9SXpvPaqsKt8-6nSxqE6btoumGFLiYupvkQZtIZ-cU_nyx0kUm0NawLbgh3sCO5JQkVtcU8TSw0xzWeOeB7jSU6ok_MvYJ7Mv2F6QGuYblaP-jmQM-cfGV6M88xqeqSmQaCm6Gpmb0wAeYg9AIQqBLwq8BBXbqiWCUHeteaQtJixUL-exyruRqd-coGTwPh-bpSAzemeHVZJz3TObeQcYvcjwrgYin1HREXIok7skFJZCE3mjGKv9oKNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">20 دلار برای استفاده از API مدل های هوش منصوعی زیر
😎
🆓
Opus 5 | GPT 5.6 Sol
✅
در سایت زیر با ایمیل یا اکانت گیتهاب ثبت نام کنید
( ابتدا کپچای سایت رو تکمیل کنید )
سپس کلید خود را بسازید
✅
📌
Base URL :
https://true-sota.com/v1
📌
Model ID :
claude-opus-5
|
gpt-5.6-sol
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/ArchiveTell/7546" target="_blank">📅 13:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7545">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7544">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">DeepSeek V4 Pro
| MiniMax M3
♾
♾
♾
♾
♾
ApiKey
—
sk-dc9d4b7df36ba555-rcaq9e-2790fa25
Model
—
am/deepseek-v4-pro
/
am/deepseek-v4-flash
/
am/minimax-m3
URL
:
https://anymodel.org
♾
♾
♾
♾
♾
Free
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7544" target="_blank">📅 21:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7543">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به هرمس اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7543" target="_blank">📅 20:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7542">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یه مدل اومده به صورت عجیب غریبی میگن خوبه به اسم : Ox Alpha
📔
حالا این مدل  به صورت رایگان به
هرمس
اضافه شده و هیچ محدودیتی هم در استفاده نداره
🆓
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.21K · <a href="https://t.me/ArchiveTell/7542" target="_blank">📅 20:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7541">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">5 میلیون توکن برای استفاده از GLM
💥
🆓
به مدت 5 روز هروز 3 میلیون توکن برای GLM 5.3 و 2 میلیون توکن برای GLM 5 Turbo برای کاربران جدید در اپیکیشن Zcode
✨
مراحل دریافت :
1️⃣
وارد سایت z.ai بشید و با اکانت جدید ثبت نام کنید
2️⃣
برنامه Zcode رو دانلود کنید…</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7541" target="_blank">📅 19:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7540">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=l0uOS6cjHfhlsyorAhBWbiBytqhY2dKlafODYxuoZ6qnBjOzwSMGuWgHUOd5zGx167XknK8vl1pYRKYm9CW3yLaejk-ikbBNJRIu3bPT6OHSJ6iU33EexpaUNp1KljhWwUti4N1EsxoyVW07b2eo1zoaaV_OG5flkBCiclRSakiXdUaBliGGz7gl24Ubjs5MJggpf9S3l7vYjra6F2ri-mjthySTVDA7h-mSIG16j0srWrT8WNCD_cCSdtLAj5TLIQVlYBaRPANXpCLsACyXLzFUW8AqEZQ_fom6Xf0LpF0h_x3Wzk3JcHdG3P8nrd_XxlAKoTwVHdNOlOXy1wLSaHs0toFKkZk2IShDiCzD-7nIHMPlU9GE5LSQreNZerw3qAKdp_EmLwTGCcFBpPTyNQ7-lxBgOhslcixOAD3OlkPg-ZacSkErD2vtEI_vLAWzhNEWC0ES8h2FMblltuaucOs4vN34UHuqEC2qFiekqhdhhmy8iEE4CdTun13wI0AV7l5ScuH5oTm5Q_CcHV6NwN9927pvsQTTJHNfx1G_GHY8nKY2CHr2M77jyCVay6DmMdO8KxABV57_Z6QJSHBNzsNk6x_2U6Hx7sKraEIepaizqHJYUcCh6qzBmkU05O0kjtasG9Vi6PwJY3T_LQunyARprFoZpYVtZZwFmnhBH-E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=l0uOS6cjHfhlsyorAhBWbiBytqhY2dKlafODYxuoZ6qnBjOzwSMGuWgHUOd5zGx167XknK8vl1pYRKYm9CW3yLaejk-ikbBNJRIu3bPT6OHSJ6iU33EexpaUNp1KljhWwUti4N1EsxoyVW07b2eo1zoaaV_OG5flkBCiclRSakiXdUaBliGGz7gl24Ubjs5MJggpf9S3l7vYjra6F2ri-mjthySTVDA7h-mSIG16j0srWrT8WNCD_cCSdtLAj5TLIQVlYBaRPANXpCLsACyXLzFUW8AqEZQ_fom6Xf0LpF0h_x3Wzk3JcHdG3P8nrd_XxlAKoTwVHdNOlOXy1wLSaHs0toFKkZk2IShDiCzD-7nIHMPlU9GE5LSQreNZerw3qAKdp_EmLwTGCcFBpPTyNQ7-lxBgOhslcixOAD3OlkPg-ZacSkErD2vtEI_vLAWzhNEWC0ES8h2FMblltuaucOs4vN34UHuqEC2qFiekqhdhhmy8iEE4CdTun13wI0AV7l5ScuH5oTm5Q_CcHV6NwN9927pvsQTTJHNfx1G_GHY8nKY2CHr2M77jyCVay6DmMdO8KxABV57_Z6QJSHBNzsNk6x_2U6Hx7sKraEIepaizqHJYUcCh6qzBmkU05O0kjtasG9Vi6PwJY3T_LQunyARprFoZpYVtZZwFmnhBH-E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎨
استودیوی هوش مصنوعی که خودش کارگردانی می‌کنه!
اپیکیشن MiniMax Design یک اپلیکیشن مستقل برای ویندوز و مک‌ هست . کافیه ایده‌ت رو توضیح بدی، هوش مصنوعی خودش برنامه‌ریزی، اجرا، کنترل کیفیت و نهایی‌سازی پروژه رو انجام می‌ده.
✅
✨
ویژگی‌ها:
🎬
ساخت تیزر تبلیغاتی، گرافیک، بنر، محتوای کاربرساخته (UGC) و انیمیشن
🧩
ادغام فیلم‌نامه، استوری‌بورد، ویدیو، تصویر، صدا و ادیتور در یک فضای کاری واحد
🔌
دسترسی به پلاگین‌ها و مهارت‌های تخصصی متعدد
📂
امکان وارد کردن فایل‌های محلی و اتصال به سرویس‌های خارجی از طریق API
💰
بعد از ثبت‌نام، ۳۰۰۰ کردیت رایگان اولیه به کاربر داده می‌شه
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/ArchiveTell/7540" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7539">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDRjVpYK3L1dEGlmNig3PasvUzrxURhbDIe5L9DXqTEuFcagrXT8m2RiOe9tWHffPrJVCHjg-jvBnSjWxZ_o5MsRkpCdj5_9CE0zCgw6uW8zyLIYL1Jed50fCkcoCIlx0JWrXqgFnlvTUHUrnf1A0GnW-h6hvKQ_iaMncBPDC85BqdM0k6o7hZAXg7nfY7L22UdaUOetdETw8vHf7iZobkReyBnbXN8lipFfhU4xS8qq86oYH-88MD1VexC7h42MLJatY9x70lf64AQ4X5eeqpSHmp9HNGh688E5gZN7c22pCTMjq-i5LKgfV2RzJX92kdM-xs8bUjRPewDzqR4IEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐳
۹۷ ابزار جادویی برای DeepSeek Harness — یک دستور، قدرت نامحدود!
یک لیست باز از افزونه‌ها برای DeepSeek Harness (dsh) — با یک دستور می‌تونی قابلیت جدید به ایجنت اضافه کنی.
🔌
✨
دسته‌بندی پلاگین‌ها:
💻
بهبود رابط کاربری — TUI، پنل‌های کناری، پالت دستورات
💬
نشست‌ها و پیام‌ها — شاخه‌بندی تاریخچه، اشتراک‌گذاری گفتگو، حافظه
🛠
ابزارها — اتصال به دیتابیس، CSV، JSON، regex، آمار
⚙
اتوماسیون — هماهنگی چند-ایجنت، زمان‌بند وظایف
🔔
اعلان‌ها — اتصال به تلگرام، هشدار دسکتاپ
🧩
توسعه/رانتایم — ممیزی امنیتی، sandbox، ابزارهای گیت
🎮
فقط برای سرگرمی — بازی‌های کوچک، استیکر، پت مجازی
🔗
لینک مخزن گیتهاب
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7539" target="_blank">📅 18:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7538">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7NPmYAwjCKPrb2Fx9V8PPnoL6UFEXQABD7uGMiuIR09DtYhRASMPM9MdDlhGKrh91mvPabT_hAzIK8fVtCRs3W_26zHlfC82ddkQRJNeELHRSjBStFrRvZT8scmal_3vNJeVenI1mW4b3-DnLTtnnkmYX4LNhOd06qdpxRhrf86BQoVgOV824Sb4GLDxQLjz6y_2EV_Q-z8WRGgL22zBtO8sjm_mvTf-dUMEWaITMgLtvqVLycGWQSs8FD6AltMwf2hSgdskyLTYwRTrbgzp4RwWM5qs4vn2rhI3VuBCXHMSzdTMRXMVFvqjWmIqFqI5Xdx3EOd9ZTvqq_lrn38iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
پروکسی وب جدید تلگرام — پنهان‌شدن پشت سایت‌های معمولی
تلگرام یک روش جدید برای دور زدن فیلترینگ آماده کرده که ترافیک پروکسی رو کاملاً شبیه ترافیک عادی وب می‌کنه.
🥸
⚙️
نحوه‌ی کار:
🖥
تلگرام دسکتاپ یک مرورگر کوچک داخلی باز می‌کنه و یک اتصال معمولی HTTPS/WebSocket با دامنه‌ای برقرار می‌کنه که ظاهرش شبیه یه سایت عادیه
📦
کل ترافیک MTProxy در یک جریان واحد بسته‌بندی و از طریق این کانال مبدل ارسال می‌شه
↔
روی سرور، یک نود واسط (relay) این جریان رو به اتصالات جدا تفکیک می‌کنه و بدون رمزگشایی، به MTProxy معمولی می‌فرسته
🌐
دامنه هم‌زمان یک سایت عادی نشون می‌ده، و صفحه‌ی «پل» فقط برای تلگرام و بعد از تأیید باز می‌شه
🎯
نتیجه:
کل ترافیک از دید ارائه‌دهنده‌ی اینترنت مثل بازدید از یه سایت معمولی به نظر می‌رسه — یعنی پنهان‌کاری تقریباً کامل در برابر فیلترینگ.
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/ArchiveTell/7538" target="_blank">📅 16:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7537">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nz-sqE_uepUkHMEzG_WE5LHqKsDD5IHle8sfdsw8RwnznbATrlriIzzO4vvksQL5hmhCrTL11Dp7RymX11l9wRV75LSGLgQV7SRt1V_7mUn5KBR0tt29ooeyz0T44sb9b71xXao-swsQA9aD11eu9rM_zSDvjYY-XaoFM0hhkp-EgexDnJh_qdcqbfcVG1ia6ts2jKI1-G8aStHS_eG_OyTFzPbEzcXszt2QNJc1mICUwOux3Vr-z995p0Mxqfme3WtELHGpi6FcIqJNwhDRmxbH5pF-cUP-wPIUsKmW2VztvIPmb4GcozEYnyyFSjDZ4MmUQfh_jZNA6mYtWxbBsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
زمین بازی هوش مصنوعی برای ساخت چهره و آثار هنری
سایت Artbreeder یک ابزار رایگان آنلاین برای ساخت تصاویر با هوش مصنوعیه که تو ساخت چهره، کاراکتر، منظره و هنر انتزاعی خیلی خوب عمل می‌کنه.
🖼
با کشیدن اسلایدرها می‌تونی ویژگی‌های چند تصویر مختلف رو با هم ترکیب کنی و یه تصویر کاملاً جدید بسازی.
⚡️
✨
ویژگی‌ها:
🧬
ترکیب و «تولیدمثل» تصاویر با تنظیم سن، جنسیت، حالت چهره و...
🖌
ابزارهای متنوع مثل Composer، Splicer و Collager
🤝
کامیونیتی فعال برای ریمیکس و اشتراک‌گذاری آثار
⚠️
نکته‌ی مهم:
تو پلن رایگان، تصاویری که می‌سازی
به‌صورت پیش‌فرض عمومی
هستن و همه می‌تونن ببیننشون.
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7537" target="_blank">📅 15:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7536">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnj3lKsjhxyRVyfwnHZamF16lzzFif-Agr-wqxMZIZCDJZmTF2YIHSIfbxMWAa2toOp06QauoCehhoi8fhh9jFTUZOUWmsqukGLI9shqyRe5Cz08kUSaTrtvX3YjzfrAoLB0ZVWfHTkfejSoQhxffwECDPBhzNRdTVmezOnK6jmBEgZ1sdlrNzvNTdPXcDUEFjUZG6sEL2nJdIK20XNxU86ub-OcismIRQrvvz4Ry71HHPRjyrFpWoPX13feJaeGuVEq23crpiQDnbh-o5LSo48_7_yX6HRjsLaV8T6qkg8Oi-0FUx3WueNXzA8hdjYi-dHsaydiFpbE0l_0PfJdCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📚
دروازه‌ی رایگان به میلیون‌ها مقاله علمی
سایت CORE یکی از بزرگ‌ترین موتورهای جست‌وجوی مقالات با دسترسی آزاد (Open Access) در دنیاست.
🌎
بیش از ۴۰۰ میلیون رکورد علمی رو ایندکس کرده و برای بیش از ۴۰ میلیون تاشون، دسترسی به متن کامل رایگانه — بدون نیاز به اشتراک یا پرداخت پول.
🆓
✨
ویژگی‌ها:
🔍
جست‌وجوی پیشرفته
📥
دانلود مستقیم PDF بدون پی‌وال
🎓
پوشش تقریباً همه‌ی رشته‌ها
اگه دانشجویی و داری پایان‌نامه، مقاله یا مرور ادبیات می‌نویسی، CORE می‌تونه یکی از منابع خیلی خوب برای پیدا کردن رفرنس‌های معتبر و رایگان باشه.
📝
🔗
لینک سایت
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/ArchiveTell/7536" target="_blank">📅 13:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7535">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vofJxgoalikw9FT5HQmcXuPXAj6xUJ0z8ecGQj_Kcy8QnC2ClyKCipdeqK3nOBs6VVcN2PPOs2ljLjfSD46VzCdFvR83YnW5EDGf6T0FOuCfrIy4gXz-zPldI57dkhE1xY9ak6tlpR2Bz0Sc2X0ZNoi0EBWsU139heD8izIyyOw7s1uKko-2jhZh0AL4JJoX8e2S0sErrs-PMrqI0D-hSLYlpgmTXtO_1e7vqCkVhIjzReWmnqXVoheef8ehpUurJvQ9H_Vahwp8cj4sXmP2PPfQXqGJ9jAlak_RDVTI70SCSZChYndIQ0MQS5HV5OX448tmZJ1HoU0XONkzXB5c3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتبار رایگان API تا ۳۰۰ دلار بدون نیاز به کارت بانکی
🆓
🧠
فقط با اکانت
گیت‌هاب
ثبت‌نام کن و بسته به سن
اکانتت
اعتبار رایگان بگیر
✅
با این اعتبار می‌تونی از
مدل‌های قوی
مثل
GPT
،
Qwen
،
DeepSeek
و بقیه استفاده کنی بدون اینکه هزینه‌ای
پرداخت
کنی
🟩
Link
🔗
💎
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/ArchiveTell/7535" target="_blank">📅 11:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7534">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVega Enter</strong></div>
<div class="tg-text">🚀
آپدیت جدید ربات وگا
🧠
حافظه هوشمند وگا
از این پس وگا اطلاعات مهم شما را به خاطر می‌سپارد تا گفتگوهای پیوی طبیعی‌تر و شخصی‌تری داشته باشید.
💬
حافظه در پیوی:
اسم، سن، دستورات و قوانین دلخواه شما ذخیره و در گفتگوهای بعدی استفاده می‌شود ( قابل حذف کردن هست )
👥
حافظه ماندگار در گروه:
دو نوع حافظه مجزا
• حافظه عمومی: قوانینی که برای همه اعضای گروه اعمال می‌شود
• حافظه فردی: اطلاعات هر کاربر به‌صورت جداگانه در همان گروه ذخیره می‌شود
از بخش «سرویس‌های هوشمند» گروه فعال می‌شود و قابلیت ریست نیز دارد
♻️
📊
حافظه کلی ربات نیز گسترش یافت. وگا اکنون پیام‌های بیشتری را در گروه‌ها و پیوی‌ها به خاطر می‌سپارد.
🧰
جعبه ابزار جدید در پیوی
پنج ابزار کاربردی اضافه شد:
💵
بررسی قیمت ارزها
📰
آخرین اخبار
🌐
تعامل با وب
🌎
مشخصات IP
💱
تبدیل ارز
🌐
تعامل با وب:
لینک هر سایتی را ارسال کنید تا وگا از آن اسکرین‌شات بگیرد، لینک‌های صفحه را استخراج کند، یا به HTML/JSON تبدیل کند
🌎
مشخصات IP:
آدرس IP یا دامنه را ارسال کنید تا لوکیشن، دیتاسنتر و سایر مشخصات آن نمایش داده شود
💱
تبدیل ارز:
به‌سرعت بفهمید هر مقدار از یک ارز معادل چقدر از ارز دیگر است
🛠️
بهبودهای فنی
✅
تمام باگ‌ها و مشکلات گزارش‌شده برطرف شد
⚡️
ریت لیمیت گفتگو از ۳۰ به ۴۰ افزایش یافت
🤖
مدل هوش مصنوعی جدید DeepSeek V4 Flash (0731) اضافه شد
✉️
هر مشکلی مشاهده کردید، به پشتیبانی ربات گزارش دهید
💡
ما همچنان در حال توسعه و بهبود ربات هستیم. منتظر قابلیت‌های جدید باشید!
🧠
Vega AI
| هوشمندتر از همیشه</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7534" target="_blank">📅 00:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7533">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqoU5iVUGgGuD9eemtDV2hUe5GYcvML9sVhGp0uOpi_B35CfhCM5rtTGKierB8g5yC7ZKZfWIu3VtbqmFTb6TdH9KX-0Sv-jkrRIyyvMH6wY72cPM3HNIj1c7ihPPegNzSu0oVMB7hEAiQx_y3paD-cnTPyaTQm69o6Woe5kXyrQ25TksFdE2JZu_BNcXUVkME0ZF5Y2ZsBXZ1QvGT6Y1nzrUPQrGQgJ7LHtbmwliEQzZNiYzO2-edsvknoMSYvzH7VwRuazl4qdioFeUoPDkFcT6Ssl8Yo9SjhhCmQidZrepqWYa-CR-O32J-AIxCy_hYWo5gM3s5E8thIbMXceUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسترسی کاملا رایگان به مدل های هوش منصوعی زیر
💥
🆓
Opus 4.8 | ox alpha | Kimi k3 | GLM 5.2 | Deepseek V4 Flash 0731 | muse spark 1.2 | Mimo 2.5 | GPT 5.4 | Grok 4.1 | Haiku 4.5
✅
📌
Base URL :
https://api.yjs.im/v1/
موقع ساخت کلید حتما گروه Free یا Free lite رو انتخاب کنید ، قبلش به بخش Playground برید تا بفهمید هر گروه چه مدل هایی رو پشتیبانی میکنه
✅
برای استفاده از مدل های رایگان داشتن کریدیت نیازی نیست
❗️
🔗
لینک ثبت نام
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=MIm-IBMm36YKdosVKskjOpP18xyyreLOkTamy-0n24cEbUjtBy8EpHXhmbwvCwtj1cHVYvhOftsFqTjbB2fwPWFgbBKByd-umCI0MN2ZsnnrxaTT4qy_MGzS5ebEsbVX-iviG8_8qoP6O3VP8xoufqEWk7dAigu2u4vKDODbbzeBv9rNN-WIK8brZBpMBVz1V3eF56ME6j1Ia_R9TCSlI5GVYUdvqq9MaBJG_PH7R-HpM58sTFqV7E5dS_5w6ObGdJqrHdEZ7bwZEUn92JrjQWgeoidL-twArsojrqWEf-ogk_YtlD28vBzGwONFxznZiYFuTOEzBveSfoghpZb3hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=MIm-IBMm36YKdosVKskjOpP18xyyreLOkTamy-0n24cEbUjtBy8EpHXhmbwvCwtj1cHVYvhOftsFqTjbB2fwPWFgbBKByd-umCI0MN2ZsnnrxaTT4qy_MGzS5ebEsbVX-iviG8_8qoP6O3VP8xoufqEWk7dAigu2u4vKDODbbzeBv9rNN-WIK8brZBpMBVz1V3eF56ME6j1Ia_R9TCSlI5GVYUdvqq9MaBJG_PH7R-HpM58sTFqV7E5dS_5w6ObGdJqrHdEZ7bwZEUn92JrjQWgeoidL-twArsojrqWEf-ogk_YtlD28vBzGwONFxznZiYFuTOEzBveSfoghpZb3hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بزرگ‌ترین نقشه جهان منتشر شد
دانشمندان بزرگ‌ترین و دقیق‌ترین نقشه‌ای که تا امروز از جهان ساخته شده رو منتشر کردن؛ حاصل ۱۳ سال رصد بی‌وقفه با ده‌ها تلسکوپ برتر دنیا.
📊
اعداد و ارقام قابل توجه:
🪐
۴ میلیارد جرم آسمانی
☀️
نزدیک به ۶ تریلیون پیکسل
📷
برگرفته از ۲۶۳ هزار عکس
این فقط یه تصویر ساده نیست؛ دقیق‌ترین و جزئی‌ترین تصویری‌ه که تا حالا از کیهان ثبت شده و بعید هست به این زودی‌ها دقیق‌تر از این ساخته بشه.
🔭
می‌تونید خودتون توی این نقشه کاوش کنید و گم بشید توی ابعاد کهکشان‌ها:
🔗
لینک سایت برای مشاهده
✈️
@ArchiveTell
|
#TOOLS</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrBki8ihLWAi9zTLQDrD21L8HU7IHsmuXxPGdtilWsQhS8UJ3dogqk93MYYtKys9jKvXavKYP-obx4st5PCWReZQLyc_AjJagzPOI2tBmLpvtpnJIQytB7knrGo3dFYX4XwaN7P8deL4aIYr2SsxhvMwYDpb8yo42KcgW-V1NR5ZcY0uMaVCf1kASz3FXLj_vH0VVcdMOmWvXi8bVka8OpHt-oS7T7EVDE3F7BdRwv60Ap1uPZvx67RLldzCUv7FLkPC0NmOuZLyAVew2R9aJVTk7-NmPO5k56HJuwCYAZjpJUrAK_nP8ixoswuVvnONOWh9Ld4b1nSyoVdjr3id-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل استلثِ ناشناس Ox Alpha رایگان شد
🥷
مدلی ناشناس با نام
Ox Alpha
، بدون هیچ اعلام رسمی از سمت سازنده‌اش، روی OpenRouter به صورت یک هفته رایگان و OpenCode منتشر شد
⚡
✍️
مشخصات فنی:
🔺
پنجره کانتکست: ۱ میلیون توکن
🔺
حداکثر خروجی: ۱۳۱ هزار توکن
🔺
ورودی مولتی‌مدال: متن، تصویر، ویدیو
🔺
قیمت: رایگان طی دوره پیش‌نمایش
🥸
سازنده مدل مشخص نیست. این یک انتشار «استلث» است — یک تأمین‌کننده ناشناس در حال آزمایش مدل است، و OpenRouter صرفاً درخواست‌ها را روتینگ می‌کند، نه توسعه‌دهنده یا مالک آن.
🇨🇳
❓
درباره منشأ مدل، برخی کاربران گزارش داده‌اند که در پاسخ به سؤالات حساس ژئوپلیتیکی (از جمله تایوان) رفتاری مشابه مدل‌های چینی نشان می‌دهد. این صرفاً یک گمانه‌زنی است و هویت سازنده رسماً تأیید نشده.
📈
طبق ادعای برخی کاربران، این مدل در تسک‌های کدنویسی agentic عملکرد قابل‌توجهی داشته، هرچند این ارزیابی‌ها فیدبک کاربری هستند، نه بنچمارک مستقل رسمی.
🔒
بر اساس توضیحات ارائه‌شده، داده‌های ارسالی طی دوره تست برای آموزش مدل استفاده نخواهد شد
🔗
لینک صفحه در OpenRouter
✈️
@ArchiveTell
|
#NEWS</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7530" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byhF-bt8kRv1sY4u3fVmkQDFlV4bOVkluXdZCi22is-ZBt52GxEkvaBBmk2x_Yge4lo8YcRrG5Em7SGYyK6YbRtYaJ1QBh4XWGHehFLEpTm5Z_V20ykPjreC3jF2yqkZ2lfGQhiRHyiAvZ5EfmIWM99ifVpc_JcUS8-_E7wze7ogXQKdRJpJamgvEYzGjSaiQ8s0kBKqKulMDL-obYy5fcJ2O2NoGzWRcMEikmXrEMEPLTsZl4MyxHu5Qsy5ih_3D1_VXDkyNBFTHzL1_e3caeTfcwOMJ4PqrVJC224rwElTKm50Pdbdu4jblgwiCuX7X662UZ5-VJJsWxodlsqKHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">70 دلار برای دسترسی به API بهترین مدل‌های هوش مصنوعی جهان
💥
🆓
Opus 5 | Opus 4.8
برای فعال‌سازی فقط کافیه یک اکانت
گیت‌هاب ( قدمت یکساله باشه )
داشته باشید و از طریق این
لینک
وارد شید
✅
🎁
با هر رفرال شما
40 دلار
و شخص دریافت کننده
70 دلار
دریافت می‌کند!
همچنین تا 25 دلار پاداش لاگین روزانه
🎉
✈️
@ArchiveTell
|
#API</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7529" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اگه حوصله خوندن توضیحات رو ندارید، فقط ساب زیر را وارد PattNG کرده و لذت ببرید !  https://raw.githubusercontent.com/patterniha/Free-Configs/main/configs.txt  ساب هر ۲۴ ساعت آپدیت میشود. /// توضیحات:  دو تا از پروژه های عالی که کانفیگهای رایگان را جمع‌آوری…</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHEEnYLuYZOU2D-WmnO7Xbeyr1vnDSsClx0v9WMqpE6AmcIeelId_bZeR3jJLZIPswh7ec6wUiYcWaeo8HwBrpQbeSvAEuuswkbSE4nRltOPOi4_qzLVvNS84Om_WAvEPHC9QNbmuye2W88LU5BulUxMHt1uES611iPSh7LaFrzL8K54Ii1tCr8r7hl5aqwh3sC0yAMciLkaKrNnK0L4puRA1oT8SliF23tleNCmOD_MUslBkKVvFOvZMORUUMXdMIXTw99B5PPXht9bwLA4mrBDWEads6ITMBOx11CVEMBaU0NN5cCV1RAlPT3FVP8C4uzCNYFdJegbKnsKiIqdbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان ظاهرا ی روش عجیب سامورایی پیدا شده
اکانت فریز میکنه
زیر سی ثانیه فریز میشه
لطفا پیوی کسی جوابی ندین یا پیام ندین (غیراعتماد)
برا بقیه هم بفرستین که مطلع شن
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/ArchiveTell/7527" target="_blank">📅 21:25 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
