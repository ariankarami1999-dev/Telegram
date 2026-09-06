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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 02:04:26</div>
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
<div class="tg-footer">👁️ 901 · <a href="https://t.me/ArchiveTell/7662" target="_blank">📅 22:17 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/ArchiveTell/7661" target="_blank">📅 19:31 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.41K · <a href="https://t.me/ArchiveTell/7659" target="_blank">📅 17:38 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7658" target="_blank">📅 14:55 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/ArchiveTell/7657" target="_blank">📅 14:37 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is4lRS31TFv6ZsI0XxbT4p8GmP6yYH1kp-O0rbYxXHSa0rLHDvDF8UxqxTHIH35cEo-IHqEncTj5ItSAKyEqdzVRCswMPT0W1HfVY1vB2_E-maFaapYKlKbeSpOr7xD5rMn81etLkUNNyofpRFjnI9ZmYHyKXFXY2k12fmrs8W7pDVmliK5-EQ2dM9HqdQ2TeNXfjrs_Tz_Ti1huqU0B3lTojxumtlUz3cfguUUMAskL_Ef__s_JiqzBfO9h85v2FzpMXv_0DzAfOIq5SJiqK-36mxw9noyo6Wmm-tNKfzJwZL8Ji2CbtITbznlaXhrFcDvBWjlm-wHyril3TtvJ4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7656" target="_blank">📅 14:08 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfzEKEOMtVC0JqRIThOQjbRO-BJ31hozbtHxUhH-7YB6hsiD-z4vXxTkkOjhCe0V6Dv2K4wlnPpnWpb52yUPmPhxY3kMddioIk1VxwUG5TAsXAWHvOzgvzyfiLIG57-ZNzoOuFRptOFZz54gdFSpwZMyAV-MBgZw_VPYKJOKaywJV3UZ9ig0VbAvkB7tbAGl9Fu6c8bzK7WltPx1hkXjnXtc5iyaRmC1PPpOZAvplZPrDE5U_I-FWWPsmVYb35ZS3bmS6r8if-W9fQI4cqKNtxry3HY9VjgUACI-MPIqi9BWnQW0pXCbu_o6j3hVDFaJG_e_g7IPhfzFDCMFe6VZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن ایمیل دانشجویی رایگان
💥
🆓
کلی از سایتا همیشه به دانشجو ها تخفیف هایی قائل شدن یا چیزای رایگان دادن مثل گوگل که واسه وریفای یک ایمیل دانشجویی میخوان
✨
‏اینم لیست مزایایی که داره:  ‏• جمنای: ۱ سال رایگان  ‏• چت‌جی‌پی‌تی: ۴ ماه اشتراک ویژه  ‏• جت‌برینز:…</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/ArchiveTell/7655" target="_blank">📅 11:08 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.64K · <a href="https://t.me/ArchiveTell/7654" target="_blank">📅 10:38 · 15 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/ArchiveTell/7653" target="_blank">📅 23:46 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7652" target="_blank">📅 22:54 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/ArchiveTell/7651" target="_blank">📅 22:45 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.45K · <a href="https://t.me/ArchiveTell/7650" target="_blank">📅 22:05 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7649" target="_blank">📅 17:35 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7648" target="_blank">📅 17:21 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7647" target="_blank">📅 15:17 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7645" target="_blank">📅 14:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7644">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5JpVTrNmu9EBTDrhKkXP47zK0wCsbo4uZ-z6CRuV2lDntJExJxaAa_su49m3wNZ3kiRaD9p8MmdcYf0EWEGn0zHTriiDt2N4wBnAl-0QqiPa-4k6DHVyGDeTV_OAFhRf97YOpp-GVZHum_SXW4-ROQ5KjZFN-rvI5RSQo43LuGdKWTxOZhaThIaSH0kEAQRSHciNGrF-EysjMtpVisu3-qCYRupRJhEmVp69oySNq2YT-Dp4RmVDjWCMyq0zy0-KQ_vZVdVmeMvB8eHQYptxkUkKK79TXcIa_TNgKPTcMrANX8vjy6pUMjDUZICnHNHBHDbAWsXtNZsWYY_V5vtmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دسترسی به مدل‌های زیر در ترمینال به‌صورت رایگان
🚀
‌GLM 5.2⁩ | ‌Deepseek V4 Flash 0731⁩ | ‌Step 3.7 Flash⁩ | ‌Laguna S 2.1⁩  ‏وارد سایت ‌Cline⁩ بشید، با یک آیپی مناسب حساب بسازید؛ اگه شماره خواست، از سایت‌های شماره مجازی رایگان استفاده کنید. مانند این سایت…</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7644" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7643">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C87GmGCLe0Gl3euWN3yUvRcBm40X2EuAPvynMXSoBxolAaDBHCJZ7gXYBF3KHQIv_zXSk21HEfa0JjVlwl2Yz1GSxN9A2awprUcJkx-CB8etI2r9ldWlPTBJi0utFsQJcEVVB1UlTo3UPzavnFrg04x_0e-Gx2K1PXu2644uUUh3SLNS-K998mJt_nHgd8b_eiRuW4IrvtPTMhUTk1Ecyoyrv7Pky3yT-lXXtrjHB1ucH8MwWUeWF5q2DnkkZDzNPWMlfjd89QUqzLdRPGo46S5ZIwgk-pmwiiPClvXGrGQnAH0_DrgIedEOyr3ua8v49iwlAdTZk4SvICDfbRaI3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/ArchiveTell/7643" target="_blank">📅 11:59 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7642">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrZnZAaOaR40EiSkAnVw3F99AA-gm2JR2aS1_A4VWVgsB8jIrgtJ3unllC_7JbJ2O2wsc7k0I27tyXkksC5k7waLhTT8HPdcDCnxOqu7mal4laDIY3_UAl22qcuZYki5DhhKsctscbt7v52-cXZyoPkOWeTbbUvZ2dmeB8ikDna2G9P_s1DrNO_ic3gP-iFo01OkmsmfOxMUsKx1JBt8Yu3l8IcM1yBKpnlewvNRG3d8PKqYpREOfI4Nv8GMy9SlKqmBAqPObkIsvc4Kf4f5i0wfuAzJQtiHNPL86qa3lOL3wRN9N9VUip1zVJ1zGqVXs6_J16_QZQdECC0vsBLECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
Anthropic از Claude Fable 5 رونمایی کرد  شرکت Anthropic به‌تازگی مدل جدید Claude Fable 5 را معرفی کرده؛ اولین مدل عمومی از کلاس جدید Mythos که برای انجام وظایف پیچیده، پروژه‌های طولانی‌مدت و جریان‌های کاری خودکار طراحی شده است.
✨
مهم‌ترین ویژگی‌ها:  • عملکرد…</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7642" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/ArchiveTell/7639" target="_blank">📅 21:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjE9uh4BJ_uhm64B5tv-bdoUPdzAHDGQKfbQGUrWdum3NL-4bOrqbH035BS9hR6l76lRqMCnYTX-p8Zly9pWCoIKOl8dcwa7Nwyo27SSP4WWb-NLXnW_g1Mxrc-136xQ-BUK7NgNDGiQ8KFCIpMRsz1d1tITghtUwtSGVoq89CLe7Vic54TTZlKcp8_rsfKxpjd7jCxPssiJTjCLMrk2UNchccF2k0he4b8fgyB7ABenDheCbMdg0yJpdG0JViFan-9p3uG-7Ao17xb6qGv2okLQHez2pSTA-uC7y3FIDvvNzjL3ACXsCLerVBK_6Yc3F4mvV_sakbp_NYm_-4M2_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7637" target="_blank">📅 20:00 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.61K · <a href="https://t.me/ArchiveTell/7636" target="_blank">📅 19:00 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/ArchiveTell/7635" target="_blank">📅 18:11 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/ArchiveTell/7634" target="_blank">📅 17:03 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/ArchiveTell/7633" target="_blank">📅 16:00 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/ArchiveTell/7632" target="_blank">📅 15:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1ifJ8uBiyeCfBC69WijJs2J3Wt8bml8Yd8Bjgrj1_nEsp8GPyK3rCQNPUl1oPkjkAr7vNGrtY0JkY5bWGe4Hu-1g7wDtccGOx75c6_qDpqriFtCcNiDUBX0HmYwY0JK-vpnpIJCUp2OeZeju8JKnmzrcnltNUFIJXsjx-VJzghHrPzFgd6zvs2Ncyy2RHTUg4P80VSWGWpGEtsbN12R0-2dQKZwKMPrym7W_oI9J1xTgHIaPC6Nf4JsjZokEneN5ZOxjd9RNmkfCmv2ekll1JQPCe8ihpTsXB3IxGSVLgErPbyF37HYj_XDmOvVrrBsI2WwREn2mUp_zHanPmLZuA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/ArchiveTell/7631" target="_blank">📅 14:00 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7623">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=iJqjcCiKJn9y2hqPQZs6SMSl2RbnX_6AF3PZSjAExA-t2nMB-GG_NjjrQUErRIB-bvrZxlEDlIRaO3WRYos7n7GqjnBE69o8SrvIw8y8k4NXHqDH_oWrYphAVlytDHybr2Th1FfbY2ei9GjRYv4yVQjhZsj1IFDe2z9cLpsc908MKmZMLR-6ZXR_ZLx4cFtghybexFFxiNK6CQc32wVUyL3lgcnTA8FyaDHqI8A2C8RmS1MwNLENwjtH3gqUqYGp3tfQtrlOAPtzEk0hP7t_wbapOo0GOYuG2xFAk_uOGOYx1bMvkfG84ypukpWv7ZQlqcZ45HT1O6EVgEtbIotv2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d216f75e8.mp4?token=iJqjcCiKJn9y2hqPQZs6SMSl2RbnX_6AF3PZSjAExA-t2nMB-GG_NjjrQUErRIB-bvrZxlEDlIRaO3WRYos7n7GqjnBE69o8SrvIw8y8k4NXHqDH_oWrYphAVlytDHybr2Th1FfbY2ei9GjRYv4yVQjhZsj1IFDe2z9cLpsc908MKmZMLR-6ZXR_ZLx4cFtghybexFFxiNK6CQc32wVUyL3lgcnTA8FyaDHqI8A2C8RmS1MwNLENwjtH3gqUqYGp3tfQtrlOAPtzEk0hP7t_wbapOo0GOYuG2xFAk_uOGOYx1bMvkfG84ypukpWv7ZQlqcZ45HT1O6EVgEtbIotv2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/ArchiveTell/7623" target="_blank">📅 13:08 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/ArchiveTell/7621" target="_blank">📅 12:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7620">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/ArchiveTell/7620" target="_blank">📅 11:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7619">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/ArchiveTell/7619" target="_blank">📅 10:00 · 13 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.75K · <a href="https://t.me/ArchiveTell/7615" target="_blank">📅 19:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbSJHH1nvkv8UPTocDS28rgJcv8JbRg3fg66qpfTaF0-x-85Oj7MFaeqK3d3T2MUoqKlfjTWBy1hoDYt_6FY_6QHEEKhu9FarzkDyCeqR9XX-GQBwRUKIOgGFlxfwQJdPjhukDJb7UyvKR7fm4CVAKF7ez0Cl1bkyUf2CoT4KonRVMy1Rw47tgQHqxpz2q_nns0CaHk28OUh8F2FhoWhlWwJ5oaz3iKnnwxCLthgxuWRBLl1wy2Idv-hTvlHBn8vlWL6DrYM5_psDEkd3uylwQgi5RNe67FsOeakwSB-INgBrFmXqaUBK64-xq0nY9rGch6fu0ZqJybXfII2afUhpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/ArchiveTell/7614" target="_blank">📅 18:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7613">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔥
۱۰۰ مهارت برتر ایجنت‌های هوش مصنوعی — رتبه‌بندی روزانه  سرویس Linkly AI هزاران Skill رو از چند اکوسیستم (skills.sh، ClawHub، SkillHub چین) جمع و بر اساس نصب و رشد رتبه‌بندی می‌کنه.
📊
⚙️
بیشتر لیست رو ابزارهای توسعه‌دهنده پر کرده: مجموعه بزرگ Azure از مایکروسافت،…</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/ArchiveTell/7613" target="_blank">📅 17:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7612">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZly4g5ANUJvx1C-UI-qN4ti4L8evl--Z-uc_ilNmMQgea-vtUnHnL9Tr-wmHSWOak02I9BbIEtyvUmusXgnmiJMib7FeV29DT_EyUWu1ppO-Sjj0fSvABtBoztppZzF2iQ_d3XBc9iByQqkgz4yvZBI8jSGe29Ja46EsJEsMrmU-kKAQndGvuTm-vzRk1ZIGVdChTTSV652hH1LUYiYjmXPxpTvv2ywZUaJJNAxlAsQlUAoyKcwudGkMy-LAS3HJjLuP9_g-6awU8Ymhf0R0fM-jYBZf8nRqkUmjPpbBOUfMobVNuf2aqzT7Fi37Gr04VEPDM0r1_XTCD0-BiWCUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/ArchiveTell/7610" target="_blank">📅 13:41 · 12 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 1.94K · <a href="https://t.me/ArchiveTell/7608" target="_blank">📅 12:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIpPcWslzcIYtilsPya_yw8btC-SWINBQTCSJr3B75rwceAS5_xo9ftxI0Hka-Nk7pTbSkw2zQhnX-kcTpPUYG1ok2oJ5EiNBG9jfamrx2QDeTBZ6eKsiCrILVMQCoeBSvDL7Lt7aw2skjK7yDZ-_otSteS1B4yceUXgwPb_ydku0GsjhQWL8J-wUiebshhdX82lEXi2TgWPrx0oKak_hCJIosu7V6pEiqDge6f9MFTTIST5uJEcCjWSBTT3VSgf30eejIU_v7FmclzhhwdO3U33T2BpmTOjzY8Y1GM7ma2qCgSGCnUUkuAUuhnZw-s7V4DI8yeR84xILoXU4_B3Dg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/ArchiveTell/7605" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkxg_Em7mtzL931In0iRSkkVUomurKafNykMMo7GAmRGJpQsxSoesXoeCYE5kGSda_ymqJm6OjtYhNbPZc1r7wme4zEwEJflHa_qx9Tan-h1cpu7G8ps6-Eb_eqYTeWzvaCV_ofGEY_WQrZs-gfRZ5Tn8RtNM6SPsI5Ev5tL0PD3ldCG3ySW-SG3RkS-fTcy5YR70Nmenbhu8RHPB6LVuJZu8DW3amtAIKaUpAOaJ8_nr-RDVvGeKJAyww1NkekkoN8OB15OmjoE7n8-0FeW7Nzwg40P0il1N12bG1V9lXNmCsjJ10Rl4B9aHxYrawKv_o3coZCdJvc3nFSaqV_i4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل DeepSeek-v4-Flash را به صورت رایگان از طریق سایت Flatkey دریافت کنید.
🔗
https://flatkey.ai/
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/ArchiveTell/7602" target="_blank">📅 14:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">هواوی کد (Huawei CodeArts) به صورت روزانه 10 میلیون توکن رایگان ارائه میده که از مدل‌ GLM 5.3 Flash پشتیبانی میکنه و امکان نصب آن در VS Code وجود داره.
🔗
https://activity.huaweicloud.com/codearts_agent.html
✈️
@ArchiveTell</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/ArchiveTell/7601" target="_blank">📅 14:39 · 11 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/ArchiveTell/7599" target="_blank">📅 22:57 · 10 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/ArchiveTell/7598" target="_blank">📅 20:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3Wu-toxVmUUMSWV7FMrAGZY1tng6lrLe6JaNGMyLShVhKt8By_G3aFVwlfE2QEqboSIupDqqsK53YTmgjMxQj_GBxC7tsjPAWIj74_SsBcM6c3-YQxY-3hO6oTAp_60NjoVKRYyr2khDLSCxW5aB46CoOEFOaqqiav-9xQYq_SOJgKJtGhdNDbFVjeQjeN2KSO9_BbKyLx6qeFqwPhyi78jM124S5SZn29THlR4lmKZpkeJpvO2uC_doG-wiUcIZtjksLcv6Vlp_x2UdE8M0LrcZopcFP0184Ur-3ydzTzac3W_5Vb8MDuPIVHon4Kj1O5dpcsaY_ia9sGit518Yg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/ArchiveTell/7597" target="_blank">📅 19:33 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S07Tsib945474NQ_s4dCuEI_hOFbNN6qVJoU4lZsqaThr7dvreLkfW5pjWUEEtQNRGqh1d0HUkdfTtK5EM4p_ti4CAkdZ3FqewEatYoGTDZFbHHITQdzpDdUzwZ1704VMnii2CiVOq8faceI_79ED7d4Y594n22IXOMbnKiW_i99AZelpJFEzfWql_d7arG9_UOknPp1-v17AUW4wcig7KEtRqLU3YOUpnA4Q9RYZVBy7S06jD0ozfrlsY0no2Ik-wFRH7MXaTJTDlywRfomCenQ0lx9JIVgMoYOvgYjXXrvklFH4knhGkgI-MmtaX3ZCFhqGlRK7AYAgQuhnDOh4g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/ArchiveTell/7595" target="_blank">📅 16:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUw0YBw5NBZFyVxWMq5_299IqGkK4_hW6CSe--QL7sqXcD7A1cWPX1ABXZfPqPcCZVrDcOm2Ck9qiEBJ-QwcOGs-3v7S_eW52mx3_9aRsXDfbd_hIGF8iHgobMYgA7eC4AcydkgiFmzh42AHDXmwu9UJlzPvSyt0ZYf4at-64eMKhRyItB8j4SZ-ohtfkXVtoTMsNbpkIJgh4nOYHbCACCky3XfU51fb7eBWIJKgKv9dHhoPF6MO_JxHZ5LzCDWfT_GYbd2lN-bfeadVbJfIHOR__fK6xc0U5WpqE0SxrCSUh7wrkdXARbneCJ9I-p62YtQNbpVILlOOPxt6TNgJ0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/ArchiveTell/7594" target="_blank">📅 15:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auzCCmJex76WGoijJoqOSYSg2rOEECqKYQW7ZwMFAjvY_-e5l2CozHRiftrYUhnbnan9naKeU6bUu3XBJwtQyQ_MFWHgO09voHavZ7SJ0h_otoD_N0tmpXHuGfvF2pAwiRIUNo7x97CUI2LnFOc-6K0GorOfKktMyuyd48BjFDGFRGxGoISUFvXPpFRo6S3pXKo_nMAv9wtisy3b0tR6XMVDnXSGweLRVRhiRzA7vibTeqVe7f6xLNji5rdPKH7GiDDkeKtdh5GtNifYfqbJIm2JA0pXIH09SLYawCRhszOj6t8AJWi6KIuv1hSUigYlETeWj55GCV5M9316T4SKhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.07K · <a href="https://t.me/ArchiveTell/7593" target="_blank">📅 13:35 · 09 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fegL96YYCEHN5Z_PVatKsQZqJJtYmpCYb3wz1SgduoR2DVRaFhzPfUoDD_6FhN0q5aJRik4YdZs08nPX_vFJ5TXJTbozlAcCfIEwz4KB_WZs9F9nxGXR1FH6iHeTC9SlHaDDl0e-5RmcoTbGk9lFABVC2s5gnCt-7_o-Xu8NpHzSIGCqLxEVGnV2mCnTbRUICZKWJgrYSuKdmyX39pm3mT0jySUIVjGcejLEp-6V8yYbVr5ihB3JK3K761eo2MK987f6h4KVZWfxNRNjIm3NVTKH--m-7fonaydzR4rWEqfcareRE8W8R44u0QqF7xQ3nADJ_5YpR_SkJFUCe4u3GA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7590" target="_blank">📅 10:00 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAFbuqOT3U-t6xhCpzcuBbzwvH3au4qudS3tEPxv6YR7BwAKDreQijSM9mUNI7-6BLFnKXAFVexLqacDzobord_9ciTpVDeWGUYHk8oE58Me0vZS8lFX6CJqd35XY6ymPqkunMVz_3xfuyuzpaqbQjhEl0xIW1q4-8amGbWPGRAoeLeQ8YQ9JYNyU0-yfGLEfnr4dYkW_AaTNv9ob4IQk7NJPjVBrDheScYJoCilgETSa_kibh4eAQza1YHp058CzbgPlvKZZ5FaQ4DG554y1_9bs3Ot1yuALH7AbS8QT41AJR5nJkMwEGOzrH6CNennERIBSSBcJieX6_H8Hwjw_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/ArchiveTell/7585" target="_blank">📅 12:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN5_iFDv8OqWS_60c39A27hc6DcTLe6xMae5yoWyTNcjJwGoLJvw7zaiTMTrsRXJatn-T3jMyHDbtjsKd6gOXGKdsBIUhI5sn9pFPmrmVYQYPulqL6Z-B9WQ-2-Z6SMzk-zPM0SfXI6EvxvJc8iHnIJtbETGWZ4OiHXb5LnRpPPfDr7m3i8eM1P6_iFQgfSqJ16XdUSgc7Kx5QJZNW6XPEs9VyVxr45SnBe8tKDrjTF1sQae7bZ_u5zi525tvLJ5Qf6cMTeJVOx2yGAcgJgoqkNjdtAwAkXKRW7oqhGeJjmwdY7xO_cI0YQFQvly8q2eDrtCRdJkakuVSfa5QT6Apg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/ArchiveTell/7584" target="_blank">📅 18:11 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA3EaMFLlxRopkgQBz2LuxZtGD1cKf-57dB7JfFzQJiVJYgWkcCZHwF-PaG7b2Q5YVemb1IMLZn6CpEMB0Plis-CH0jKJITnkuEmPzosDepnJDJ4x9ZMtAN2a7Po15Qh0G-sm8oq60Q4-03oZxrLaiX6UgZVAa3aDsiT7kjBpu3woqW2eSaNNJ8dZ1f3YoPNc-P6xaxxBj99yEXFHcItAl_M2J7gm1x9BkqeVyQxF8nJwXSl8VQpaeGJ2v4nAxAkz3V-YMi3ommXVW41VnnXcf2TfoO9v1ZrQ80Px04v3plRh-G9Lrjz7PyrGORooVvfkuLwvFOjegUsxCVOVfPMrw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/ArchiveTell/7583" target="_blank">📅 18:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7581">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=Bi-a7AmXqtMnB-pLpUzvS99A6ig2x8j48RzTA2Arm649jNctoqYaVVVJ9W6QD9hBJgG4anevMK5OgaaHnZ2oymtpyc9RaOwuWrRL0PNQBQXs14pn_SG5ArEv9kaLOg-QOHb8tOyuZYdWXlFKFyllyjOH4K6v6i-DjsW_tpknvG8gDy831j1p7cQEgq0J05uxFIT267n62Q6Y3eaKM_sRqeIc4RCfLeX9NaVVNddhbd1RqnYq89ArNa4rjDRlqYRi-09AZdQFnj1t98loTqDkb0bwzghYUqitK-ems6e-fXLuRRTNcw3dDtFLbjtckMlw_rMSvqFdMc6_TCGUWxsutQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bf2a763b.mp4?token=Bi-a7AmXqtMnB-pLpUzvS99A6ig2x8j48RzTA2Arm649jNctoqYaVVVJ9W6QD9hBJgG4anevMK5OgaaHnZ2oymtpyc9RaOwuWrRL0PNQBQXs14pn_SG5ArEv9kaLOg-QOHb8tOyuZYdWXlFKFyllyjOH4K6v6i-DjsW_tpknvG8gDy831j1p7cQEgq0J05uxFIT267n62Q6Y3eaKM_sRqeIc4RCfLeX9NaVVNddhbd1RqnYq89ArNa4rjDRlqYRi-09AZdQFnj1t98loTqDkb0bwzghYUqitK-ems6e-fXLuRRTNcw3dDtFLbjtckMlw_rMSvqFdMc6_TCGUWxsutQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0UJOzbqt_KHXefgDxm8vC81QgWUMrQudJ5k6AWefSk1Z6NwDaCK2OA_DtW9_I0VVchYo0lNxITNttx6Bc2THos_P-NvUhDsuJliLIVmbYi-SvDf461wOiGuF6jAq5JKc-LpHerNRFnFlmPp8XP6ndFr68ax8q4DnBxqClQpAZZ_YwGG0osFPipqtZh8k3TI_5P1NkWofgVTj--ITPSghf9bDFNnRwgBjjQ1GwZ7Ha11YJ6piYULCSc9WzP3S2lJyk1WvZq_eeIfbAxYLgFXbjXI2_nzIUtwPf8nS6Gj1kMRSVzglRWRMiCi-8AWHLsUzLfoWrluB9WevM-xsnvnNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/ArchiveTell/7580" target="_blank">📅 15:31 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7579" target="_blank">📅 14:33 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/ArchiveTell/7578" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7577">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxN5_8iCu7IGGzFe9rMTAB_j7YI3BHYsPOtk_OddU15IhJEk4MNyJSNsvoEPTFVWI9OWC3Dm-i2UXvok4mXUAZdIYTk7PoGFhv4ESZ-RR5ZOP0ggfvg-8DbvqWg2Ybn3qMPXmfmG_yZs_jL85ChREydMKB6Ku22dTZpq-T8lqXFJjQxybt4us4iE7zazd_NFRllUBGTzmVGtYHLllmmKLehGr2RfTDkZcE0J1a_e73_OwnCTd3t1TOFetjpv636BvBA5pAuiorQPvwIGkO-2FZXdmI9rRxV_d7d_EEpUo2yc5zqu2R6hh2W3Vlmuy9b5Ffdp_sz0ILhWgbxI8Atuag.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/ArchiveTell/7577" target="_blank">📅 21:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdpYcO9tqkxL9IMBpUBdWCUDZzzHH3JnxWTz5c2QknRF9xMD-pCYigeuhRQgJrCN0ZOkThLE-yRHR6p7WIMSiFZb434InNk8QHqyXl38KZZqpI3wi5UnAzdgLS0nCW6LTQs_jeJ0Zk0Ojpa1fXInanUPVj3fbv5-mow8aAXT_4N75YjkDZc-LZxsp5P2R270eHnMui0hXtKHngvWjmGxbN4WlpZ_l5QNqyotzdsd3uR0B0zFGQ10bKO24twniHGo7P8ITJtnSaGY6xLHC3Hy1Lqr8danTeIlnBgU_gID-qr_gX5QCkz-mge7B3QHzGxPEnTP9G30LTa0X8diTjqgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sVLnGf2zPV3n9kmHpEZEz-GOdowMrossxyT4K-5qO10i3FwjrQxTC5m5HkHVWFNtXy7uujqpAi8Bh7YuoDcI6T4gTzQbY07Pewr4TH0n4pjml9ddysHygUSfSIlljdt5ag8o47aBfnI6XIBPdQlTrJ0M7IJNPb26Jpp2nv4vNB92yaxjxQ6mxUFLzue_oyfAXkXDk1M5hIJj7EYYDP-EZvyYNoPuJQZ74iRB3e_63dtQ_l5YzLvYDp1fAcTTxVL1JArsbJxxse9jFacDdOsefGZSfL9UThBwuscgsteFQ_qRKk6RGNGhBHhTdrHNHMJcjW2DYLQ5YUpDE0GPOjGy4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/ArchiveTell/7572" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏
🔥
سورپرایز دنیای هوش مصنوعی؛ قاتل جدید ‌Fable 5⁩ اومد!  ‏مدل مرموزی که با نام مستعار Ox Alpha همه رو شگفت‌زده کرده بود، همون ‌GLM-5.3 Flash⁩ محصول شرکت چینی ‌Z.ai⁩ از آب دراومد. کمپانی رسماً تأیید کرده و قول داده وزن‌های مدل رو همین امروز منتشر کنه
🚀
‏توی…</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/ArchiveTell/7571" target="_blank">📅 18:47 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/ArchiveTell/7568" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGK-uxIpeGygINwNm1HZ6sDwx-mGR5tj86gxGTwAX63lmRfOwD5N7KzXZ9e6MHXuXwvWDDqJ58-LcMDK8BW8MzgLI7aT0kJYD7yQHTFT-H80xdvRk7BeqSxY3DPzH5YCEgasiPNKCpjokutGkkL3cWsZWmLqHhqvitXdYzNsIq0lRF20od0Wzl9nzZDpSHFnrGVcKo23fCpHD5bE67dDMIr4sPH6QvAL10QmjSOrQl98ilhnRDSu7HtWAF5YACbVbniUXqGmKonp_5oBgNaC4bJKhoACKo5-LJ-mupsk4_dyMR8Ugh-TJImqz2DC5oiKechABnW1UGHLr7DJkV-wug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/ArchiveTell/7566" target="_blank">📅 12:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7565">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/ArchiveTell/7565" target="_blank">📅 10:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7564">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mxc6Qqb8uI1X3teUNB_KjBnAvE36hiN9h0rlgIkfdLITHhu9dJ5Rbgf-KX-CVrCIOnEzLQCv_jHOxRch6tmXtRAud3kc-N8QUEyEhBHHxwGq1OpDUDB9iw-tBmM0Ub-oQ4gnz0qXb2w0__1rZ_TknQ_xOOypH2j4U73le3eMVAvDD-z_4MMO0HqLuWNafgbndltANn4jMnJVK-bWx7S3zIMU_Dmvf53M5j_mE_jZVT1-WKwyuD6vgr_GmMUcOclTEd9kiK49v9u2518i5446PlcAhVqQPHS0n3Zn_7zD7o4nK6pV_CFeE7RLT50kIwdMfcPHpuadXgBbIdyxAylTYA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/ArchiveTell/7563" target="_blank">📅 13:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7560">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwXi_ZBf3Ci5m3Y1XS2ytsGTPO1IK1lgPJHxj_879GUNSivR_j6YsbeNVQFKbjFmZTML2T4CHwrvi7op0s5kRpz6cDAP3X7SOatcHsjOCh2bllZX66xKXII_NOQ7tK-x9E8qmWDdFTjTp2Yg3SEGmYwf3SSesvl3QiRI3Ue044BaHoUmAkXJ4eL-WVY9HTRoUo0xkTVIvZNAC85TIQV4BSf3sh-KGxC1glW6w6JkD4vhcLtB8jUaxu1BJjiFoAj-H7dbH-00nF_DOFqc8OOYVItQXwVka34UoBSeFcTjjZcyks4BHCwo0P-abKBQMVo0rGPbOerDg2tLse0M4Dnosg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DQ3cISAQd_QluluAWv1M_G-VIfVvmSuWI7l75OraSerTA9-HOqcra1icZEK4fpDE90Ub5ZE9JllDxrHMfVAPn-9KwNVPxmqxUBDc1gDjOhc3yccG3DbdKrzOwDsKEF15m6MEV8PLLdEEObjo4aUjhcrusDV-BxSZg2zIQxXeIJegqsPCwidvq6TOATWHlOfNa9wpqjC6-jIdf2f__KD5SbV1mE-6CjUgh1-89iktYW3QU7S36FsiVdWZ2MltfC3G1FYzz4ll1Bsx46V_H637UuKAY2Ea7sLp7QAhlVrofX2uvYM9MLw0WL6krZGPMfUkt_8AIQcczV5IHizn2PQRAA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/ArchiveTell/7559" target="_blank">📅 22:20 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/ArchiveTell/7558" target="_blank">📅 21:22 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONEvTMWt6aK3TgIc7g5cBQsgrnnR--NZFIsclnkm3uvenxVJYmzvTI4htGM-LS3VCQwxggF1uI7GUp_jZNETJeR0N_E4BKAAOL3uMSpT2seiDWJkchjBIdbQqRbQ9wl61tFBhnc03p6kdkyRcWvZ8bd_2I8LYY_7r5JTC0cGEgmoYhSAg0NBdUzvbyKjYB_UDZZYkNgD96brJDmKTH3tm0sK00mi5y-aWZr_KkUIJfa_kX9xL-pnm2S8zDtbx0oqAkGZG95UPUoOXZKsFWjCn5bewi7rmUa_GQP0ZiehRhE9U2XwFtDO64zgAlKhYgqhvjb-rPrHhJ2AaYefL-hCDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrSisFLv8FyP1_R6Rm66tJy9Fl28M9BeDZ_7LUVOh_8wQ6vbO10bJY5DE72LoGBr-sHhGjLXECI77Nligl-TfLB40pfufvB3qvh0ZFQZmeVRWN_8vqRjwMvH3QgfmqTVEmCrEMRH7eBiitOp8yTu_-YwdfLSeeVM63xYJN2mJk35NceBTFolR7qaxUV8O-Pc-K0u7K5reZvoAfDmUvZLwu2HCkb5srESq0ncdS45Lb6UqVPxtf-KoF7JGULGN6rIzxJQxt5Jx0enhfvFA8C0oMCRwyJkhgLTrAhlOA-rdG9I8tloWRzyWlkhdw27bkvoDp8kHtfYZr5SmSlTvSsVYQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/ArchiveTell/7554" target="_blank">📅 10:18 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7550">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=onAWN9Zbt-2APCxp5YquHDictk4-K9wJgj2CvhuqyNEI49UpB7y8RK37MjtdIMchhSgC1b3LiMBNp0ISJ_qO6fBgTOblVSK6UnCupv-YrRi9yIJbz5rafcRfBGQJY81hqSPXvJU-QLZRQa20s2tjATeqQKnSfPUwOw9doQA3y1-irCAVoFQGkUtyYz--LfrLtcsE1KFARQ1A89sqLmBHGCT4W5kmJpCDoryNq9X0B4n65dKQ4pTsg6APG7NL4cNrVRiG088QUmCzPcb4dMXIQGkTmqvJZyRJ_RWWEi2pNSyqsLPGCWXiwMl_x6gzDComLO5QAYSQLedPrY1UWYlpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bb09302e0.mp4?token=onAWN9Zbt-2APCxp5YquHDictk4-K9wJgj2CvhuqyNEI49UpB7y8RK37MjtdIMchhSgC1b3LiMBNp0ISJ_qO6fBgTOblVSK6UnCupv-YrRi9yIJbz5rafcRfBGQJY81hqSPXvJU-QLZRQa20s2tjATeqQKnSfPUwOw9doQA3y1-irCAVoFQGkUtyYz--LfrLtcsE1KFARQ1A89sqLmBHGCT4W5kmJpCDoryNq9X0B4n65dKQ4pTsg6APG7NL4cNrVRiG088QUmCzPcb4dMXIQGkTmqvJZyRJ_RWWEi2pNSyqsLPGCWXiwMl_x6gzDComLO5QAYSQLedPrY1UWYlpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/ArchiveTell/7550" target="_blank">📅 19:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-7549">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=EBVRnW0c-5Ch3XXFxjiGkgMKC0XgohXgTDzbBdlkE2jNAcYGRu_pfIgXKrVFqSY-j_-ceWlnp0hxcwhZLiPIFJZqtn0NYZyf323hF9y5bQ8p4Ew1p5iZ2G_xekOWI6UNvqEQzOZgYtPeOp5p6CIjNsRJuGRymWOuEaZBBzEpu67xjXhV7AxmAW2-rQTleCaYEf4cGKKLKZYUiSPXdBY382iptQFA7TpVa6Lwv27e-f8gtfGKNPxf60o4DTPLOYy354Husrm5HYOpsBoviK0J8XPgx3ZGavM460EUbxOv1QWeA2NODRU325TLKVDl-EoUYGd8XYorzd_f2g8fjgb95g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da15ea43b4.mp4?token=EBVRnW0c-5Ch3XXFxjiGkgMKC0XgohXgTDzbBdlkE2jNAcYGRu_pfIgXKrVFqSY-j_-ceWlnp0hxcwhZLiPIFJZqtn0NYZyf323hF9y5bQ8p4Ew1p5iZ2G_xekOWI6UNvqEQzOZgYtPeOp5p6CIjNsRJuGRymWOuEaZBBzEpu67xjXhV7AxmAW2-rQTleCaYEf4cGKKLKZYUiSPXdBY382iptQFA7TpVa6Lwv27e-f8gtfGKNPxf60o4DTPLOYy354Husrm5HYOpsBoviK0J8XPgx3ZGavM460EUbxOv1QWeA2NODRU325TLKVDl-EoUYGd8XYorzd_f2g8fjgb95g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-i0rNF33XB0AyT7DQRsZzmjUqmiDHv5EEjx5m-J_7s_2-k3iL_Iq20952yhV5KOuj3_MD-pZHXE7oBFtNbQoddl40lLUPtYtnM1k0btoURhgFWtm0okJTfT17Offn4bnoCLh4zjI__IkhrjnwX9Z55Zrx0chZmYaNDvI4fiTZIYLhOxXE-ybIGn_FCsELfoA9jACOdhIudYdyZi9krdpGZWIhrwhknDSSUYOT6n4D7Kv9ZeyoDo3pDMp5s8JIVUxZPKsqFAzU_ceGd6_X0n9FZ0s3m0NjdDsaRNIl-F6JJgt7fpXR0fhCuIJIVOxDtZssb2aD5E-EaUz-M6-c_vDQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJWaUrnwT5Y1nO-zoMBWAxcL2A6xDWE4SuOQNUPxWKpnBiQ1cgbOcZOPNJIgi-FTY4t2NFs_jgMrpXxeFE-YJXsc86mB-TSYdg-66J37_xo9viLnfL-BrVtcCcNVe5SZrkQN6xxhYC4IaECpeALgQF9Vw7V09gErQtoncDKaNHAi1riDVWJC9aFYZPNcnTGO2X_OUpkl2RGQFIJLBNDMENTM0v45rrGtcSw9cgXe5RIFe5Iz-j7uuCth5680iEJm9dpW6_iImZk6t5wjVa25JSZOgnZDy4w2j84ucIpTru5H-QeM0bmuo-fcvb44oZW3XxAjsLj9r2kB4P3QAxe5hg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSx21xIDnzEHbC-1rhdzYrCVqyUW5eQ7QCR4wAceA2qM8hz56CtVep2K4kvfFaxnLchKzj8dzr5ac5Kv7-aojSduBSX7QgrYeDZ5ICSbgpzET5n2qXlRbj-5SECoB_EboYc7Thp0FAtzxEc01ib3O3a5WvXC1dF6BS0RPLxT8BEp4Zwty6wEgs45m3X547zMmvHisfJAb4wkFjuRZ9t_CzS2ONf7WJC3kSzB16XW0pr2KbZN32hQtEYgkIO9gxDTVdFr0u0vqlTCRr59QhXdPu2Ey-vlXhXYYUxPQnlpJbXTJFN6Op-L2_-pcoq9HQwSPUixUzVp0ucNKVxIDNszrg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/ArchiveTell/7545" target="_blank">📅 23:01 · 31 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=IJpmb4HGNcM1sYEri0D9Ix_Tm6U6pY6JJKh1FeMmaRXUJzxel56vIdxu0hlst9ZMYbbzT7KQoltnLjuIQWh3NswsXif53pNgIRBdR8Ue-IeJSwwjFM9qzonoCvPs0Y6fMMUZKeF7e5pX7IXYDAfVffQXk3DH6UWbJa8SkA9KWfLaElddPQB0j9ihcNa4M8wFfjJysAqStNwP_YYLauFI_6F-LrTZjCDC81Aa4YrY-KBtI5FWZ8JnJYY-K3KP12ApCuEYwB5vUeNwaNukncSIhgxLT8HxEMq8ez53a-PDh69QDVXoVzSUsn5odh8OSgVeqTufPHiY2RczA5RtROxmPoL0yonLOa9m1I8ka14zRT7jw19gs96FnLI7quMmO3w0bBjt6on82hY_aa84jWU0I6BZWgCcW040LJncGZHmaRBTYMYXEBmoMc8qvQgPGUaSKDBT3M8wPXS65_n2lP99bDvwnxvaTG_FY-DPikGebBlnp1_f960Y68aTSYhgU77DhR4a-0cbKaoRdjcCn7A3Kax98JXt53ipn3cuYkF-kcPMOMrP0STD320OK0dr50RZjJaq6feX1kH-UpI9QxgT0OfKRSOEls3CchkABhlVbe0VYL6JASa8_8sYLk2tf5-P73X339lASyuZEIzeE20Ca0G8rCzZznJGxpF0jEqLjLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e6f8e92a.mp4?token=IJpmb4HGNcM1sYEri0D9Ix_Tm6U6pY6JJKh1FeMmaRXUJzxel56vIdxu0hlst9ZMYbbzT7KQoltnLjuIQWh3NswsXif53pNgIRBdR8Ue-IeJSwwjFM9qzonoCvPs0Y6fMMUZKeF7e5pX7IXYDAfVffQXk3DH6UWbJa8SkA9KWfLaElddPQB0j9ihcNa4M8wFfjJysAqStNwP_YYLauFI_6F-LrTZjCDC81Aa4YrY-KBtI5FWZ8JnJYY-K3KP12ApCuEYwB5vUeNwaNukncSIhgxLT8HxEMq8ez53a-PDh69QDVXoVzSUsn5odh8OSgVeqTufPHiY2RczA5RtROxmPoL0yonLOa9m1I8ka14zRT7jw19gs96FnLI7quMmO3w0bBjt6on82hY_aa84jWU0I6BZWgCcW040LJncGZHmaRBTYMYXEBmoMc8qvQgPGUaSKDBT3M8wPXS65_n2lP99bDvwnxvaTG_FY-DPikGebBlnp1_f960Y68aTSYhgU77DhR4a-0cbKaoRdjcCn7A3Kax98JXt53ipn3cuYkF-kcPMOMrP0STD320OK0dr50RZjJaq6feX1kH-UpI9QxgT0OfKRSOEls3CchkABhlVbe0VYL6JASa8_8sYLk2tf5-P73X339lASyuZEIzeE20Ca0G8rCzZznJGxpF0jEqLjLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keBPAPpn3H1KTPkyVtCaBsgpuDXYmEIcuguMBT5o9l6gkkqm_PkBIUrnlYxdyQ-Duv5YKULuMmZTMhGluwUyBcFVJbKbJ3KNsSkYJLFcV8Y6NGmmsryuX-mgdjrn6kqX--UoLgYi-KYH4fs1XCjg_aKJzF2XNXeLy6KFb1hl7caM87DZhClzH1jj7Abn7qxP9M2QaOjV768YJDcEukIfNED3iT5LOFzc8phGrIm3wEcX0piqCex172XaDhZQsYgys_vP4hu4NFIyztExOYS5lrZBdYuM-AydvlYCCQkG7JqvYyLNM7N904lAtbk25oj6NDiCLH5oZS083aC3RZa_aA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLyRqZTzOj6p6o8ORCdKyNvHvZ_wMc_xmZrlZnqzYuCcRYyN1UbcipovilNQc-STuPfc1UEbG3KS3l-Oly7ID5_qs08kpWzwAUxF7KBPVZx8wuY-L10psww2jXr5rlec1jI98BeAYWdpwgdC36Jbdk6fWRUX3eAs0IR1QHPudy_EH7KrUELqySvBbgB36-5NrXvcdMWCwMobuzPT6_1mKruxf69beI2VPa2EUO2pCQFn1n5lb38Bj4AYjDVWSp8JFuqliXnorfn7hLmBq7C52ApI8kZsC-bHpN19fF_rdtcWJ0ErX1GYmAlxqtt7zHfVC0twa_-nc-8n62LQ4vXzCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M75Zk5k5_41Imb-f9DI1MkpHKhgqijZXC_TkRS9pISkEfGCb6GwZk7YsbRbvOdIzktuXtGOr-j_wBn1I_-UUVBO59uAp7m1kTCFPmDNSAPK-3v4e-_AeDF4LplPZpk2FED21lwdPWZyJjfXT4gxegMrd4AT-D_2CAOsTFt3xEII0ZMcDCJU2u52YUOTQP5zsHa1Zli9sffOhcrJyIEjdCzSr42I0l4RDU49kcIDui7WeiEl76sXdcdMkStyr76_jXn9S5eitvmHhR6EJqJ2kcigbAgfJ9Fgoe7ngw5q7Zsl52tYgtLoco5zZU2W3Mqe5rd8FC16GlGxM86jRMxoXiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKU8k5daOBgMwGGxjBZT7a7AJqTc3PdBMlVQ9auGH0sSiCY5R3-04SFtueKLbf37Qz-bjRqpekWLxH_NEr1ixns20b4OaxoZAiuX7HZFegjfgSp2W1fhJue99pBlqBeP6Wak05sn3s9mnRx42macBep0ZAMGDZTSd8jbKU-cpnhXez5XbTVT0Rz87UFmpjoSC5lCqdalNO8gi2N6zC1MlH-y7JABdo2FCTNlsr9pYoGzXTC24lj0Xgb-KrtE6eszHoyAFAdFupdtQaQuzkgr5N6N84RJ2fvtPLG0DWkC2qEo1M0VA8qkZ5JwaDq-I2pLD87ki883V7YYhiVj5Fmx2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWaB4Lt-iN94b2o1kXmd1-avAN4gKfxQKjxyoadpTvFVttQNALKVxUKpHKrxnHQ5SZ1z_Q33qzLJmN6bIWJ630j7unWhnQ7VdEFGyxrCvRV4V5f8coE0b3utYuNVN1ibIzQ6J35R6EYQL8WGo2EemoCDU2yJs5vTTJBDfifG-5b9ApMjEBwkCogiK9l-oVC7rDrw83PjVMVKHDv6mb7k6wSXbRqp-drJo_K_oyXVcAKy_p2WY2AddYAzLjZWG-EU5urgWtmXTE3vD-pow3JWw7zDm5DiWae1VFTiY6qC1cXGVAJS-o7KE8MI8dunYJlyuiddt9eQ7pOudKEOFay0Pg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7nUURob0WGnqXp5D2HCyWaH8cWorNDrejRYehhbwVT3lRf0LMnL5cr798YlfS24SVi-vhuMpMrpnzRHVKL7AjVKaAaNN5Qq8-qtPsev9KTtmzl0phJP58cctUoGccAr-JovQV5hsRahIZiEhBlvLDlr4gNuVvP9sYvjEAs8-gvX_sAVSn0v87sTiebpD5G1C8zDgwoEfe1MVHU9EP_cUZ9dui-S9apSuHDsfcRFSzuDidivKDu85LkkCvIsWMNKVGxx6aDXDpE8WUMIM72NYCR4qbvVH8HsAJo7JfKD8_ITOkj9QqYlzfpmSuZvuRlmYjiOS8biixyckhWlg1_q5Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/ArchiveTell/7533" target="_blank">📅 22:02 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7532">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=DkWitYxOM7Tovl3ixMtFsZAN0FTfkh0Qv6ZfShygfk8ekOPEzoQ3uJvQ2fU_iP8yNJemz9YlFO_iDlFVznjb2rzGSZWYR1e_tXnREwjvYKxbORjU7YFMakX3N8euRk8o1k3InimInBqHbjNm1yT0aYeCTIF8yJ79SBfHM6gUlHvsxbVgRdcdj8moOdj9BykJOMd7EAfhz4OizV8HuEUZ8dfjZz0AnMgEuKS79swCt-AfwMAZYmxWVN4NR9jjeaIthoiyZptkRWi77kzBpzw38DivPF8iRzgsJkQFNbrspOI0Q8uo5pbBpjOsdhtxa5TaJ17GEVJOPrwHIp8N2X3zKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77f19a6e5c.mp4?token=DkWitYxOM7Tovl3ixMtFsZAN0FTfkh0Qv6ZfShygfk8ekOPEzoQ3uJvQ2fU_iP8yNJemz9YlFO_iDlFVznjb2rzGSZWYR1e_tXnREwjvYKxbORjU7YFMakX3N8euRk8o1k3InimInBqHbjNm1yT0aYeCTIF8yJ79SBfHM6gUlHvsxbVgRdcdj8moOdj9BykJOMd7EAfhz4OizV8HuEUZ8dfjZz0AnMgEuKS79swCt-AfwMAZYmxWVN4NR9jjeaIthoiyZptkRWi77kzBpzw38DivPF8iRzgsJkQFNbrspOI0Q8uo5pbBpjOsdhtxa5TaJ17GEVJOPrwHIp8N2X3zKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/ArchiveTell/7532" target="_blank">📅 19:14 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmM8sYpCybppesIROWcRUNfSS_rWKZXvCiEA8qKpz6tXoDCHAchkPuEyj1xJumSTYBDT0RgUjYydCPapJh8KypJa3VBEyyl1tffBo7QFhC46Qmcj_-pjgwkrWavMhw8HygNsglUQtKXo_LFtMt1fOm6vdf1nhWzn6lgePb2RmZqCvl8TARXEfbqilDBhPA2K_dziGOcfJBMc-LOdwo7dPb4GFAbDwvphsZagYOZTWWX1xosTt2gJIhMlBE-LCUhCoB42k8UTz1Q92zLCqDBXgUek0XtWBAqNu9p57W6HZ5kL09OpH8IxCd1u1nK8AD_2shVmaKmzb9_w-qP81pZRaw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9EX3Twk74mecQKbkMC-irQM0AJ0OOj-f3YXaP2pzka8HaQVsLfFjzkLYLVxvYZiXW3VtjbQbdtLyyCGdVvwjAdYVA7xA0c2hPaaTFM-u9vV5aIDA4JAbNLCBSPYPXaenLWpkwg-8bTlriu7UcGLsuHGvWMBb7hmsVjTaoOtseSUDbulzfCjQ7CJpEVCxmdRQQ2z4fLn74PpI7e6zFxDQfRwlF_GqVeSvnWUmD3kNEf7Xu6R4Pms4tG5u224f0gnQrVxZod4pRXmtOOjWh6aTiVrUsw5l1tEWP-EanHmEQ8tz2ToUWypokmClM9imarQB5OTk1hJuu1bEQQIU6GMbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/ArchiveTell/7528" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-7527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_3j6QhMT-IsMxmaTSA4G_DKYXpH_524cdFOuuipU7A5HyJWXucyKuog7cOQnI_FvOFbQC0NNbtP3wmgNClsiAJwMlyhX5OZtZ_fAypRVcrChUd-Czd5u6hfTn_IshRJZDEHe1vTcf6LyoTGt6FjWWVb2BGt9NZufvvkc8rjM_kQyn-oLOf6Aj6-exxwV7tesrA-kDddWX-YwSyPPTnTp4nubpfnDhHDTNQDynkzKUBsC12y5cQA9k1QZqhX90HNzzYHXu7KhfJ3E269Hz9Bu1NbekYTdDl1TIb4IyTtASIY94yS7ft4dIgjG7_BkOhxtC71we7kSSK0TzCXvPnvvw.jpg" alt="photo" loading="lazy"/></div>
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
