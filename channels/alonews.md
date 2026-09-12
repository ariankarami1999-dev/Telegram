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
<img src="https://cdn4.telesco.pe/file/qugs9vHqmldfcp9S95cqbvorrRk4umsmAm_OzXz444eBmQ-LWpEM2J54kyPZnniTfb84CN5mbw1Vd9QuZNcUV-IkwIpvQlatKJXAmrTEL_L6h4tyqRQZvinchGJNk9ZQ0h3AprpyKPACcJeOKdQhC5RDlJPSfggPkAEy4MBSUDMgFheCzAr_z9d6x5L4E91YjRu1D8VqfwmL9pIHGHc2I7QyK4nXCvQEvll8qpGQfmVr_8jHsrEgrLWKkp4UbZFSewyeO-tbVbTdDbc0PmyWBeUf4LIKDOpbSSE-4iXNGsSQTKgoZx1cMfr1S7bSQfeeDiCp2HKe287XC6X_g-TelQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 919K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 03:06:01</div>
<hr>

<div class="tg-post" id="msg-147135">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLIT فیلترشکن هوشمند</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-NYZ-T-Ugdz79Kg_bNB-8B5pF4ZluZRUgJVjaSOrHAuMuhN0FpyX5JIs2GHqfbLErNxL5jn5vWjjS0kOT-zT4NCYdIiXSOCLtvBxZcCbJmjvJailol4Juj07wnPDVi0By_CNuMEzKJ2yhTBjiqPfottqoG4s-CMirJMXPgh2mSuMIVy5hB2VNEDHOoqWqdsGgEKBsNTKa9NpHfswibEgfrenvn6HBs419LOkx4KDI1nmXNr_Np-VeG-XNcT_9r6CVMmBA6vNKTa_CYbWbo3q2Nk2fZusDJhEsOhc2kIf-QCUnzaeTPWJ5bQFCdlsIKxr9Dr0qB53M6PIrSU49svrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
قیمتارو شکوندیم!
ورود به ربات و دریافت ۲۰ هزار تومن هدیه
مولتی هوشمند
لیت
|
۳۰٪ تخفیف
۳۵+ لوکیشن • ۱۳۰+ لینک پرسرعت • IP ثابت
▶️
یوتوب
و
ساندکلاد
بدون تبلیغات
🔥
فیلیمو، فیلم‌نت و نماوا رایگان
🔥
آی‌پی ثابت برای ترید و اینستا و یوتوب
🎮
سرور
گیمینگ
پینگ بسیار پایین
🎁
کد تخفیف
:
LIT200K
اول رایگان تست کن، بعد انتخاب کن.
🔥
ربات تست رایگان و کانفیگ:
@
litvpn_bot
❤️
ربات مخصوص
همکاران
:
@litpanel_bot
❤️
پشتیبانی
۲۴ ساعته:
@mahan_lit
.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/alonews/147135" target="_blank">📅 01:32 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147134">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
گزارشات تأیید نشده از شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/alonews/147134" target="_blank">📅 01:22 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147133">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
مصاحبه جدید هادی چوپان: هانی رامبد بهم خنجر زد. بهم گفت پشت ایران نباید باشی( منظورش جمهوری اسلامی و حکومته) ولی من قبول نکردم و اونم همکاریشو کامل باهام قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/147133" target="_blank">📅 01:16 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147132">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شاید باورتون نشه ولی تورم یمن تنها ۳درصد هست و تورم ایران ۱۵۰درصد
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/147132" target="_blank">📅 01:03 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‏
👈
علی قلهکی: طبق توافق احتمالی ایران و عمان بر سر تنگه هرمز، «مسیر ورودی به تنگه ۱۰۰ درصد در اختیار ایران» (مسیر شمالی) و «مسیر خروجی نیز ۲۵ درصد در آب ایران» است.  ‏
🔴
۷ شرط ایران برای بازکردن تنگه هرمز شامل «اتمام جنگ در همه جبهه‌ها» _غزه، لبنان و ایران_ ،…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/alonews/147131" target="_blank">📅 00:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7nc06m6Rj0BlP78N0kFQ6mTsi36K_i4aoxz00MyCXpNYRH8G8chcJ922uZWZGVDBnWS_nnvdrMsbCAwbcRAdTcuAtynvcpPRBeIS5GUJQsrJqSCJESQEG3HoizXlcMlgTrtO-FE9Rj6IAntSVnahHLvnq9_Geb7d_ZnGwj1XVaKy9R767q4l1J4UDXOczCmDS9-j5BBF_kH0UDegRDVxtMpsMk13JEDyxKJ42xueRfyaPttm72TncvdlgzYjCZ5YnLMJ4iF5Bg2iFDhLETVC_7DJh6YRZbunSTidaLGEMbx1tEF3sSuzyWfagg95JeDkT_ltbebzjqH9fruVMI-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
علی قلهکی: طبق توافق احتمالی ایران و عمان بر سر تنگه هرمز، «مسیر ورودی به تنگه ۱۰۰ درصد در اختیار ایران» (مسیر شمالی) و «مسیر خروجی نیز ۲۵ درصد در آب ایران» است.
‏
🔴
۷ شرط ایران برای بازکردن تنگه هرمز شامل «اتمام جنگ در همه جبهه‌ها» _غزه، لبنان و ایران_ ، «رفع محاصره»، «آزادسازی بخش قابل توجهی از اموال بلوکه شده»، «لغو تحریم‌ها»، «مسیر ایرانی تنگه»، «قبول حقوق هسته‌ای ایران» (حقِ غنی‌سازی و عدم خروج ۴۰۰ کیلو اورانیوم۶۰٪) و ... است.
‏
🔴
«مذاکره ایران با آمریکا» کاملا متوقف شده و «توافق ایران و عمان بر سر تنگه»، مساله‌ای میان «تهران_مسقط» و کشورهای حوزه خلیج فارس است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147130" target="_blank">📅 00:39 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsuVO-rexqAQZXnnM9xcsmqEVLU8M5bn0PD2yxXiAm1rvjbxyXG5LddFoqJ9cxLABGR7dO9zZbbZEkCExd9lZGXBeLGW9PnyVu9sok_UWOFBrEFgBhnCH8rfkMafu4ENo8OlW8Ch_DYEA5q31Wq1hHdYN9bDlhfmGc74AgrVxgT4PsEqDimFEzHO6oSPOtC7rAVj98BE3PTqBq-KOELuK8BnWE2CChtdas9T1SIQTgI0hErGEqNwEXc3qM2gzjyoSI3NeFucnuRbZ0AqC5Ve7mnbQDWp0_aroSq8leRrcHW-y-0u62Xd7CMO85Ut_UUG1g9L9HyHqjv7qcoHU6ldNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیمتی:
گرونیا بخاطر جنگه دیگه! طبیعیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/147129" target="_blank">📅 00:25 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1-l1DSS7ArpWFW73P6Es2BJQgiBwqAk87Ik4cYhdwucriS3RqlvJwFaB-ImxeSXxw1N_rOFgaJiEhMYDAkieL7i0FvcJIICZ1yQxj6NQThH83uYO9Dow9xrR_DWQahPqyMAgzCqgNuDF5uouMsa69IfrpdGP2IDGyEBU-dh9x7n1T9spX_-wolysXhyqW7vzW2wFXR14LuGWGbI82SMaTdghgHhGSs3nvNLZ5BkQVc9J5TE9r2XeJByPGPYhpdDn3eJrKAGGYTJYqiySnWsO5qaev6jd9JKNqFlGRt1l1CiHa-8EcSQkWTcjLFGkE7JrL9z1J-cAZvoFjKhwhizFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فووووووووری
/
کانال ۱۴ اسرائیل:
ایران برای خروج از npt و آزمایش بمب هسته‌ای آماده می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147128" target="_blank">📅 00:12 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/147127" target="_blank">📅 00:06 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PL8fo-GQUk6pvaCFLyCRsp-9b2lpmFFruQmwzdjWpI5doDOPi06SiCjR2La4QDVX2JnXNC4z5rxA-3ldQOyVECvm1fn0ZD1O3FzGYbpm2ayYQdBz4azVwAWT_b1S8ppF4YPx8jvM7j3NufAlxS4iR6tI90rFE0stAkOToawqza71yzj4VQnvpgCGxMDFkgoeL3hHkUX7psq10sAsncpEpMdH67Lsg8oGoUUlrYIpWCknCAqo50ih7otZz1XDXevndNjXrrk5z_STgls5jGLFLeJ1wregfHCGkog1ILXwZoEMfL-FqOgW0cSxlPY8_JLzZW5mnHL6e1XcwDdBm-VuvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط زن سابق سپهر حیدری وارد اونلی فنز شد تا عکس و ویدیو اشتراکی بفروشه
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147126" target="_blank">📅 23:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147125">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزیر خزانه‌داری ترکیه به شرکت‌ها درباره معامله با ایران هشدار داد
🔴
وزیر خزانه‌داری و دارایی ترکیه به شرکت‌ها و مؤسسات مالی این کشور درباره معاملاتی که ممکن است مشمول تحریم شوند هشدار داده است؛ موضعی که چند روز پس از تحریم یک بانک ترکیه و دو شرکت زیرمجموعه آن به دلیل ارتباط مالی با ایران اعلام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147125" target="_blank">📅 23:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147124">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
چهار مورد از حملات توپخانه‌ای اسرائیل، منطقه "سربین" در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/147124" target="_blank">📅 23:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147123">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ارتش عراق: اجازه نمی‌دهیم از خاک کشور برای حمله به کشورهای همسایه استفاده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/147123" target="_blank">📅 23:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147122">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / گزارش شلیک موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/147122" target="_blank">📅 23:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147121">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
سردار وحیدی: اسرائیل اگه جرات داره بدون اربابش وارد درگیری بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/147121" target="_blank">📅 23:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147120">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
آنتروپیک: هوش مصنوعی می‌تواند تا ۲۰۳۰ هم به رشد اقتصادی و هم بیکاری گسترده منجر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/147120" target="_blank">📅 23:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147119">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e73c3932.mp4?token=epUGLg97a3KFMQP5IOf-LHrDu8QuzfL9IhGt1A2b9X7FIAiP6WCIaje3EnAStY8xMPjVkZlEz3N_Wt2AeGPRKkPLSp8LCqdAokeJb2WTWORSLaA3w6VjGC71yzDG6b_FYYIG-ZKc8R4Il1HX25wZE5WB9i8z4Y2bLpF-fmDaIq2IR4baP2e0oXaeRjgWnqY29mlkTWN_vCmEW6NhzJA5w4fNsikwbkhnf2dqI88dWrEIytJn67EmG_HPexcsIeyqD5fLOERHZFk5Er5wMKkYhPitJunQ6gT_tRJ8-dNXekCo_vfW9sls3t-2AUgEdyeO-t18gEoDB5wGj4PO4p7OaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e73c3932.mp4?token=epUGLg97a3KFMQP5IOf-LHrDu8QuzfL9IhGt1A2b9X7FIAiP6WCIaje3EnAStY8xMPjVkZlEz3N_Wt2AeGPRKkPLSp8LCqdAokeJb2WTWORSLaA3w6VjGC71yzDG6b_FYYIG-ZKc8R4Il1HX25wZE5WB9i8z4Y2bLpF-fmDaIq2IR4baP2e0oXaeRjgWnqY29mlkTWN_vCmEW6NhzJA5w4fNsikwbkhnf2dqI88dWrEIytJn67EmG_HPexcsIeyqD5fLOERHZFk5Er5wMKkYhPitJunQ6gT_tRJ8-dNXekCo_vfW9sls3t-2AUgEdyeO-t18gEoDB5wGj4PO4p7OaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله اسرائیل به قنطره در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/147119" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147118">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
برخی منابع خبری گزارش دادند ‌ داعش به یک مقر ارتش عراق در استان کرکوک حمله کردند
🔴
هنوز ارتش عراق به صورت رسمی این حمله را تأیید نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/147118" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147117">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سقوط یک موشک در شهرستان الطوال، واقع در منطقه جازان، که منجر به زخمی شدن دو نفر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/147117" target="_blank">📅 22:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147116">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
وزیر دارایی ترکیه: ترکیه به دلیل تحریم های جدید آمریکا پول واردات گاز از ایران را نمیتواند پرداخت کند، ایران تنها از این پول می‌تواند دارو بخرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/147116" target="_blank">📅 22:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147115">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
معاون سیاسی و امنیتی استانداری خوزستان از بازگشایی موقت و محدود مرزهای شلمچه و چذابه تا ساعت ۲۴ امشب برای عبور مسافرانی که در پشت مرزها باقی مانده‌اند، خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/147115" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e8bb997.mp4?token=Q_pXX6b7VrHcqXJNnDKnB8C52iYC73sSyEbyeqUYYd1z3fHZEYOO0q7zD1-dQPoCo1kqsDnBckyfe58CT_DuJJuppcMcky0ohTQD6pYXwyJ67p8MmbFfh9FL4QDCbL4ToCNwNTu58XQdmAyonPQr5mzpNmpH8QqbKHlr7htXIHfYRb-sz4a2gdqN2YRmc9DXLA0Uk7JCbsFtW1SGlllSQZR0XEnQrCpKqrK7gDl7VWfuk_yma9F5bKRM360ULX1AZ1n1WuQH1tAkJxyI4YdQZK_MZSecRtALJPJn53Y91L4S7PAQPkDFJsNBzU8w6H7_JrcumfDbRI7iKUYx-4ge0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e8bb997.mp4?token=Q_pXX6b7VrHcqXJNnDKnB8C52iYC73sSyEbyeqUYYd1z3fHZEYOO0q7zD1-dQPoCo1kqsDnBckyfe58CT_DuJJuppcMcky0ohTQD6pYXwyJ67p8MmbFfh9FL4QDCbL4ToCNwNTu58XQdmAyonPQr5mzpNmpH8QqbKHlr7htXIHfYRb-sz4a2gdqN2YRmc9DXLA0Uk7JCbsFtW1SGlllSQZR0XEnQrCpKqrK7gDl7VWfuk_yma9F5bKRM360ULX1AZ1n1WuQH1tAkJxyI4YdQZK_MZSecRtALJPJn53Y91L4S7PAQPkDFJsNBzU8w6H7_JrcumfDbRI7iKUYx-4ge0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو مشهد یه کارگاه آموزشی گذاشتن واسه افراد بالای ۶۰ سال و کارش اینه به این افراد یاد میده چطور اسنپ بگیرن و بابت هر جلسه ۵۰۰ هزار تومن ازشون میگیرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/147114" target="_blank">📅 22:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
مقام ارشد ایرانی: دیدار رئیس‌جمهور با ولیعهد ابوظبی در فضایی آرام و سازنده برگزار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/147113" target="_blank">📅 22:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
بمباران توپخانه‌ای ارتش اسرائیل مناطق نباتیه الفوقا و الرشیدیه در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/147112" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=rzCH-kxVSLmwFGuLtNlINF-1zQVdyatvV6enuNDuAs44PlVP9vn0xyAoZyLn2VcHrhVyPq6OGPs-WOaULifdqkqjqTsbG7fMN9vh6c_lNdD_xYQ3BveBRkNxxqaU9tmVVt4z5MeLgr94_4_vDh3hNWCxbcNQjf_HBCnO_wpge10YClFidTAGlpsG0VPlpHfi9KLVGxVXnmd7K_t5vqwbR__YxYjZjjciI9zatqxXJhthYuHh04extKL4xw6e5PooRpnG8iE54tY366d30bKny5UFJSDzYmK6Ro2B14ZoDL19M3pWO7cNd-BAbRrFzjG0W6bLIIeYkZNgI4mWfYNr6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb519e251e.mp4?token=rzCH-kxVSLmwFGuLtNlINF-1zQVdyatvV6enuNDuAs44PlVP9vn0xyAoZyLn2VcHrhVyPq6OGPs-WOaULifdqkqjqTsbG7fMN9vh6c_lNdD_xYQ3BveBRkNxxqaU9tmVVt4z5MeLgr94_4_vDh3hNWCxbcNQjf_HBCnO_wpge10YClFidTAGlpsG0VPlpHfi9KLVGxVXnmd7K_t5vqwbR__YxYjZjjciI9zatqxXJhthYuHh04extKL4xw6e5PooRpnG8iE54tY366d30bKny5UFJSDzYmK6Ro2B14ZoDL19M3pWO7cNd-BAbRrFzjG0W6bLIIeYkZNgI4mWfYNr6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: آقا مجتبی دستور بده توی 24 ساعت سلاح هسته‌ای میسازیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/147111" target="_blank">📅 21:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
عراق از کشف 47 پهپاد و 46 موشک و تجهیزات مرتبط در یک مکان متروکه در نزدیکی مرز با ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/147110" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
فوری / هشدارهای صوتی در شهر ابها و استان خمیس مشیت، واقع در جنوب عربستان سعودی
✅
@AloNewd</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/147109" target="_blank">📅 21:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / هشدارهای صوتی در شهر ابها و استان خمیس مشیت، واقع در جنوب عربستان سعودی
✅
@AloNewd</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/147108" target="_blank">📅 21:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6A0E0ALRChb6Z5uDOgILdHejHF14S8KzAOKJcflAsFTfgfOnkPyu-y4mSIkiEfSYiJ6agsg_UoNosB4zABrrD46-mNvoLbTdhrFsgrBc3I6Tav-3ef9bbeWADtcP5S9u-f9JJ-NhEwjxRvCIZZhEhQM81THVuqd8cAICS2jVzgdn62NnSUofcI4hA6oiAWVZuwUcKiy1dTrn3xKFX2UPOJqJapOPHQvNtu4epYcSTodHvH9lA0T8nGcIW3n-blxMisrLkCkk_7dedE9cCnxtNz8s8Hw5T1I-ond9JqJeDlkgE5tUWyF0givrIE3X1f6QuCs1TekWeesM4JvHAMUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایلان ماسک با دارینو آمودی، مدیرعامل آنتروپیک، موافق است که توسعه صنعت هوش مصنوعی باید کندتر شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/147107" target="_blank">📅 21:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6B3gEuBN32teMbrya2moLeF3DjeLy7BjsFvqZLG4H-SR9wTScQDJyjl2rwwlRZddF2u1uoNrPduWMI26PE0LYXZqgw2c1jUkQC46R7TgrcED690W1ehSh5zPNEa41qedVNeZMS2T59ewvc3Ip_cp3jBDR4HfuEHgfv1B1McQo05OTj42u58G9Ki6toVht0I7y4Z6Yk9HpDrtAfg-QKLeGtDRnAkaWtMYkw76k-_er16A2K9Bd3lzrhtxwFT8AnfWHONDriRgyLg1rDAVJOS41hHVm1dfjuA5nXv78AM_j148a9ZxNJQcqxtkoDKp4Ir28SXheEtWovASAifYHZi9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عبری: بن سلمان به ایران پیغام داده که جلوی پیشروی یمنی‌ها را بگیرد و در عوض امتیازاتی به ایران خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/147106" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
صمصامی، نماینده مجلس: بیش از 86 میلیون بشکه نفت کشور بدون اخذ تضمین و به صورت اعتباری به یک شخص واگذار شده و تنها 30 میلیون بشکه به خریدار نهایی منتقل و سرنوشت بیش از 56 میلیون بشکه نفت نامشخص است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/147105" target="_blank">📅 21:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یحیی فست: جنگنده‌های سعودی در ۴۸ ساعت گذشته ۱۲۹ حمله هوایی انجام دادند / این حملات بدون پاسخ نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/147104" target="_blank">📅 21:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vL5-QviGswh2tbUEV1G_oh7rHaIIrWCyO54PhYL1n9hPm_RjD2GSKwh9jNlR1tY4GeCG4zBw0wuRyDZFcmYVGdyJfQ8eS0OPZjMycNmzUH7pATfjAjnVvMBDXJyl_M0pD3NBYji6Cr6QHpjU6vpd_mU3cnXJJVX1yhojWdVkkOwqwdGzeS_y4dgBBLiSgtG8C9MH7GvfidMt2RZf-pJm6BL8f26FwH-_Pgjd_QfLjnnQdh2BMCNMEwg4bRmoaxT_vfZeA3k8Nmba-zqaePBTnuFN41i9Pb_mg-fg3Gm38tdVrmcXwN98Ek2oNjzzY4K8J-XLhb5NyaWX442RtpVLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داماد روحانی:
پایداری‌ها تخم حسن رو هم نمیتونن بخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/147103" target="_blank">📅 21:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
رئیس کمیته نظامی نیروهای مسلح یمن، (حوثی ها): اگر عربستان به سمت صلح شرافتمندانه حرکت و توافق تبادل اسرا را اجرا نکند، سرنوشتش تسلیم خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/147102" target="_blank">📅 21:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
کرملین: نگران وخامت اوضاع در خلیج فارس هستیم
🔴
به نظر می‌رسد که اوضاع به هیچ وجه تحت کنترل نیست
🔴
همچنین نگران وضعیت تنگه باب‌المندب هستیم؛ این وضعیت خطر تشدید تنش‌های عمده را به همراه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/147101" target="_blank">📅 20:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / منابع عربی: شلیک موشک به سوی تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/147100" target="_blank">📅 20:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
یک منبع وابسته به دولت صنعا: ۷۳ کشتی طی ۲ روز از باب‌المندب عبور کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/147099" target="_blank">📅 20:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
تسنیم: مسیر جنوبی که واشنگتن قصد دارد آن را باز کند، مسدود خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/147098" target="_blank">📅 20:33 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
انصارالله (حوثی‌ها) اعلام می‌کند ائتلاف سعودی‌رأس در ۴۸ ساعت گذشته ۱۲۹ حمله هوایی در سراسر یمن انجام داده است که هدف آن‌ها استان‌های تعز، مأرب، حدهیده، الجوف، صعدة، عمران و حجه بوده است.
🔴
آن‌ها میگویند این حملات توسط جنگنده‌های اف-۱۵ و تایفون که از پایگاه‌های ائتلاف در خمیس مشیت و طائف عملیات می‌کردند، انجام شده است.
🔴
این گروه هشدار داد که این حملات «بی‌مجازات نخواهد ماند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/147097" target="_blank">📅 20:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7775db9344.mp4?token=eLAEHiF4un0i9gDOph8KkpDIR4c7RvMKM0K1f48CvaiRrNAp_L2DtJA_rfCtBxt8Yxk_ckHBJgMuI55oShaLBnvPJ8ZQiUgovyk27WVMXgpW3bNBs1BrPGZi7HvYdn1yJxysMkn4-MFDCW2VYf9x56OpXhEADZv8IMKSRHlUNxS-VbJ4E11dNeg4We4Hx3OZzxvszhWVohwBMf_eqIK0FAepKTAQQsJlyVHe4iK77Td9_pqRZsSgePsfnMQyxFwfqcX-wagnXKxjZyoPXa-gDD3Zj7-B0hR4y8AG3zkLZCg8-xuPBIXZFLhxIduXPqPBIYJx8oi7RzVzelvvcm6bZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7775db9344.mp4?token=eLAEHiF4un0i9gDOph8KkpDIR4c7RvMKM0K1f48CvaiRrNAp_L2DtJA_rfCtBxt8Yxk_ckHBJgMuI55oShaLBnvPJ8ZQiUgovyk27WVMXgpW3bNBs1BrPGZi7HvYdn1yJxysMkn4-MFDCW2VYf9x56OpXhEADZv8IMKSRHlUNxS-VbJ4E11dNeg4We4Hx3OZzxvszhWVohwBMf_eqIK0FAepKTAQQsJlyVHe4iK77Td9_pqRZsSgePsfnMQyxFwfqcX-wagnXKxjZyoPXa-gDD3Zj7-B0hR4y8AG3zkLZCg8-xuPBIXZFLhxIduXPqPBIYJx8oi7RzVzelvvcm6bZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای دیروز نشان‌دهنده آسیب گسترده به پلنت عمده‌فروشی ابها آرامکو پس از حملات حوثی (انصارالله) است، به طوری که حداقل شش مخزن ذخیره نفت به طور کامل تخریب شده و هشت مخزن دیگر نیز آسیب‌های خفیف‌تری دیده‌اند.
🔴
احتمالاً این تأسیسات از کار افتاده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/147096" target="_blank">📅 20:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3V6srY_9R2wh5I-qXoyhfMrMjJSx3Lb_3ZmppuhWSdTjLlG8Gqww_TwbeEqg1O6n_m7HdCwenWVlFLaTJ8EHk-RumaKkeR2aHPLRp5c8QeNI6B6eUTXg-51rqYCs3M6IEziPe478-UuEcbi22F2Pkhn_vd3TGKk25afNe0DON-WsyGw82z8Qbe6m7D5Mt6KBIBDBmZwCkwm4tpJkNV61sOGw4vmYBfRBiAc9gw8SFNFBH9fOCiG1UdUCb-kpTr06T0cB9vknYFIFB7cDR7jzhZXwh_PfEShuxgqtXnTlYfCUg41QNrFe3Nr4TPRiv5YsJzh6DR-U0tFekstnuaBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کنسول بازی ps5 pro به قیمت تقریبا ۳۰۰ میلیون تومن رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/147095" target="_blank">📅 20:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvC2v34xUR2sPqoFm87EV1NudbFLkwvYcMPg_qjVyZNK5lkYVKcT10K31dzSij-6uIT6Cv67S3Or9b_hP7QT3mFg96NGPslL0FOPMVfYYKaHLchBiAKegTD-xsUA64Z_BbobBhZhNXxf6AclBPRRsG3cQHkey34lmDZpTYO7CwwZOyuDmZr_g-CO8uHC1RQxEFW-R6PT6BDjgyzOkUuLwTBkaO3VpUVEieQlCEumdviyB7ecaKI3sZR0oDb5cFGpwx0wwgx6t2KUWeW2GdFUgAVLlhjCyPl3gMkhriHM_11YaUcCwZq-VDgC8ImhiVdNUsTAfKitQZmVBR-QqNeXCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: مذاکره متوقف شده است چیزی وجود ندارد که میانجیگر داشته باشد.
🔴
عاصم منیر هم جمع بندی ندارد که اگر وارد جنگ یمن شد، بتواند پیروز شود و پرتابه‌ای سمت تاسیسات حیاتی پاکستان نرود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/147094" target="_blank">📅 20:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147093">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsOheG_CH0cx1cQOA9fF7cjyUN3kAdieyBbKZ6Bf7WVSnY7Bf_zf7UrQUIooNxXfGHHTwrNMGiHbzyR_QlZiSP913iqibqMyz8Jt-3JJ1ww9P2STprO5xauRBiQ2297D0KYZ4w8fhMDdJXiR4eqcnm3e86le032Ia9ZVyMa2loID7cm8e4W57QtKFZPEoDtHLbGjDa4r7NvTtir2y3g-V9HmOO6f0270M2Y13AvI0P8EparmfBIXaRfWjLzW6Y6a3KfaoCz1203IdRZs1lJBaMzkPsBRMntN2eaFpmACRdyG8oZWh4AsmiH0AVghe9ufGSph44zn_tWsLCnoGqkhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی: ماهی ۱۵ میلیارد حقوق میخوام
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/147093" target="_blank">📅 19:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJC2doB6dlZuVORM6iFtVh7RT6Ni28Ij9QJW7vSxzogohSwQxcGsOJBH0yloOxaOZq5Gy-4PD8wnT-YC55B_Ba0Jh80Mr8hChOWI_YoUnSJ0lgRWsMM3e24Xhbs9R1IazQ1jNNOZKdk4JhjTpcuW3xTdXy4wEImkyHxV7slYDu3gPmOIh4hpk4ATq1SshDpiBm5NsAARTUE3tD89seOABEjDy5Py3YVdsH1eyxdo4PZHbg6O27VxHJRzqydzWFIwQ8rgunMcM466wah-SicJJzYUDuT-EhmLgh_r0ZRF1fAmTvWLZjKAj_000aAYJG6dwIQRE9u5IrWuAZHaEDK-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لباس‌ های نظامی و تصاویر به‌ دست‌آمده نشان می‌دهد که نیروهای ارتش عربستان سعودی حضور مستقیم و سازمان‌ یافته‌ای در بندر المخا یمن داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147092" target="_blank">📅 19:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
مهر به نقل از منبع آگاه: براساس گفت و گوهای فشرده فنی و دیپلماتیک میان ایران و عمان که در نهایت در اوایل شهریور ماه توافق نهایی حاصل شد، قرار است به زودی تفاهم میان تهران و مسقط با حضور وزرای خارجه کشورهای حاشیه خلیج منطقه اعلام شود.
🔴
این تفاهم صرفا میان ایران و عمان است و سایر کشورها فقط به این خاطر که در جریان جزئیات مسیر و ترتیبات تردد قرار گیرند در جلسه حضور خواهند داشت تا بصورت تلویحی عدم مخالفت آن‌ها نیز برای جامعه جهانی مشخص شود
🔴
در این تفاهم درباره جزئیات و مشخصات مسیرهای جدید ورود و خروج از تنگه میان ایران و عمان توافق انجام شده است. براساس این تفاهم، مسیر ورودی به خلیج فارس به صورت کامل در آب های سرزمینی ایران قرار دارد و بخشی از مسیر خروج از خلیج فارس نیز در آب های سرزمینی ایران قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/147091" target="_blank">📅 19:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiXqkkahq8ARme9bU02FTwBm3MkYbP2gjZhs6H1Y0kreJy8ZAV9Vc07XeIRS36QqEoF6thBPFFYK8BqhiiIN5D8x1XgWMv36RGQxkHcsw_SPoRvYWs1JmtgYGhGJRrM5YUjO6s2NIIsyoLYmBIWt5IHcVJnlt_Z8c7VWO5SbOVwIMpXhHmjIQxxCBXZUdKBeOkUblPwM2_MX4MTEJyWLX2yItSVoui7M99LXJfPCDp8GbNVR-zfhE2w1wfl8S44pVDXGXmrCGXACCLBSmPYtWW8oyOrwEuJ9aEImmUU-WtXoiB4CnXGhBK2qTNTDJ79BNmvOQ3_3Fs2IcR-cur3NsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترکیه شدیدا حملات پهپادی که از خاک عراق علیه عربستان سعودی انجام شد، محکوم کرد و حمایت خود را از حاکمیت و یکپارچگی قلمرو عربستان سعودی مجدداً تأیید نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/147090" target="_blank">📅 19:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/خبری مهم
👇
https://t.me/+4tCwpwOgY3gyNzU0
https://t.me/+4tCwpwOgY3gyNzU0</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/147089" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/756c9e4032.mp4?token=oLyuCxXTnXSiQB67i6HZl7uEHCf_n4Un7uVwRoLpE1ypwx9QwBZyocNrDlMPO9rAnu6o6AQMs62pdkOd5XOXqSZ7NvVpPKNF43lzvH04UYrhvvX-8MhcbpuYmy3BfjVp2jXQrITxUWWZAs0SYXNUJHLdmAsErRIenFDIhDNgJFmTUqyCUZ9UtfvlSHPDw2EmgT3Hb3LyzRbjD1sPChJaYhlrDYvoZ7Zyb2ozHfg9AvmVSXmX_XMqV2qi-_uGMRgEzF_Em1iTalhkzKBcuyHsMuZKL26jeEn7fcKIYdjdZ2_wvQrYdCGz02vuyfHU_Bw2tQXeIlFmDvIy9NlBtwt9Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/756c9e4032.mp4?token=oLyuCxXTnXSiQB67i6HZl7uEHCf_n4Un7uVwRoLpE1ypwx9QwBZyocNrDlMPO9rAnu6o6AQMs62pdkOd5XOXqSZ7NvVpPKNF43lzvH04UYrhvvX-8MhcbpuYmy3BfjVp2jXQrITxUWWZAs0SYXNUJHLdmAsErRIenFDIhDNgJFmTUqyCUZ9UtfvlSHPDw2EmgT3Hb3LyzRbjD1sPChJaYhlrDYvoZ7Zyb2ozHfg9AvmVSXmX_XMqV2qi-_uGMRgEzF_Em1iTalhkzKBcuyHsMuZKL26jeEn7fcKIYdjdZ2_wvQrYdCGz02vuyfHU_Bw2tQXeIlFmDvIy9NlBtwt9Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر امور مالی اسرائیل، بزیل سموتریچ:
امروز، فلسطینیان در غزه هنوز به امید چسبیده‌اند که به‌نحوی همه‌چیز بازسازی خواهد شد و آن‌ها بازخواهند گشت.
🔴
آن‌ها باید درک کنند که چیزی برای جستجو در آنجا باقی نمانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/147088" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ثبت احوال : همه کارت های ملی که تاریخ انقضای آنها رسیده تا پایان سال ۱۴۰۵ اعتبار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/147087" target="_blank">📅 19:26 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
هواشناسی: درپی فعالیت سامانهٔ بارشی در بخش‌هایی از شمال‌غرب، سواحل دریای خزر و دامنه‌های البرز، امروز و فردا در این مناطق رگبار باران، رعدوبرق و وزش باد شدید موقت پیش‌بینی می‌شود.
🔴
همچنین در ۵ روز آینده، جنوب کرمان، جنوب سیستان‌وبلوچستان و ارتفاعات هرمزگان با رگبار، رعدوبرق و وزش باد شدید موقت مواجه خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147086" target="_blank">📅 19:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام ایرانی: ایران به دنبال وضع عوارض بر کشتی‌های عبوری از تنگه هرمز است و سلطان‌نشین عمان این درخواست را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/147085" target="_blank">📅 19:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏
👈
الجزیره:
یک منبع امریکایی گفت هرگونه توافقی که بین ایران و پادشاهی عمان امضا شود، از نظر ما هیچ اهمیتی ندارد.
‎
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/147084" target="_blank">📅 19:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/o1OdiR840Foxpkh8wdNbmzQVt39hPfaQGfVAnJBGqGOMkBJ5rFkPCEYg4oL7-CBLt97x328lLd5Q51-3lLbt1MEc9Dzne9neYXmNxdW-FGEbeto7ox-2gWEkNznrGpz0cecBnxcROh_7uNu3-cBeM1S6MKfR2VaKZHSaY-h16ag7bSLfvPN0HPLHjdZ_GO4svr9mmCVe3pLalCyrxepd5niAMklRQXnizbbBfaC_vaPncaEVr73AhxyX4VPkV4qUoEhGEvfMkdGa765fx9BPosKKW199TeYhiMNe5kSc0nQwAoGvU2GICSIFByV2stkWDb5ESmnzu6E3XT8hum3Iyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده آمریکا (سنتکام) اعلام کرد که در ۶۰ روز گذشته، ۱۰۰ کشتی تجاری را به عنوان بخشی از محاصره خود علیه بنادر ایران تغییر مسیر داده است. سنتکام همچنین اعلام کرد که هیچ کشتی‌ای از محاصره آن‌ها عبور نکرده است.
افزایش ۱ کشتی تغییرمسیرشده نسبت به به‌روزرسانی دیروز.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147083" target="_blank">📅 19:02 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147080">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ffVp37na_IhGnXchl6VAN80agciMWtbU0bDoBXguTnTQh10jkUnoyNmZPGlrPfQlY98mTPoNDdVq1muuHy6E6_6kZhobuDiWkqUsdjmvBaAxa_G1dM_mh2hUN1bnBNv0pTHBt_BgxGSDfyJ_ta_7xscP8HtYnV47i_AfydKokSN74H8clyysQxymx7MN21OnxttN7gOR8TUe-pIJv22ChmLvAPcF3EJjBZRH-a1q_2o6rMNmZqzg_dkm_XGaNGZuzQrc7iW81FLzRkrAkj6tRiuv9le727sdhDOjfUzWa0pPvsHIdjjSAEIDRwZmP4TWwKs7e8JddQa-WoAYIF2l0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_JzrkljWqocBXz9tvN_1zABhcO06UeB2OQjYCRUob5aKt51ZzLF_UMisOLc4We5sQvZyA1c7jSMtQp-yhiFRn3iBczOJlTZ8mXD06xkUvGNnybT7O3TFa5ill1C6XQmiDgcV3_rgqcXEgLv7rw6VspjAy13e6c3wAKwDZnoe7OK5mlcYyt7LJc602wcXUIfN5trvvh-1HFuP9zKeu37yYH0ozaKLcMAdnpIcRfuoX2k9qzWbV-nXKcXJkpHYptt3R9BHI6-O2IWuxXKq7fs5Q5dZuU_0xQYDxKQqHrOYKAaL7sMMObLZ1N42p4QPkZYtJJJpifIURuY1qKxgYHZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CS9-ex7SB280bZpH3mQAR8XN2VPj9NkpLqc-ep6Db_THNLS0PVUuEXP7mJkVoC4hDZnacnZhXz34yNXgDhkLjQFsg2KumI2qFCMKBcjTRtmlf94p7JQOR2QuLXFrXrykQoRB7LF-uGf0KsJhYD5qvkC_fqMUELS5d67WriCQ7CL4Ls_KVYiejZBIJfTWAWAy-Uh_9d47S9ir9IA-fRBJm2yGo_5iw1UASpqNOV6nKvggJu623Hg9ox4WgabvapsTxf4AAOFgogK5QircqM9Q0GcobMZQWpGVRytr2qT3N_kH8NIe3GdWKp-5Tg78KPS1r6aHZd3cj0kFcYVOxWfcqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کشتی‌ها و نفتکش‌های آسیب‌دیده ایران در خلیج فارس
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147080" target="_blank">📅 18:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Re3JJBrXffJs8ljrJR7y0b6prrpaveLNhS8LSbo5m5qNNfWO4Ew7udbxNLQu4AD1psf_I8UXsVO9fH2z0z2PNjU-9LB-CSSztkCr4kdTQCB9D8gRni9CUdYCq-wvn5P29QXIrTFCqiGs7qsVvcIJEuqh9PjIkQAYCTbiOXJtVeY_KBarqFf1hVBGzEvFYvEka195ttAeQOTDegtqOoCQdbvCsTpuzMtOgZgxQ5cDTqKqf1ZVUWdDzZ5p8LynkzV5CZj_f236u8j4ObHUKU5eFEWpwvkLWf9JgAxBNfOj2plG8OqGyG9GV5gpkhZQClCTjJ5gJCQbz73ginJG9TLC1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
نفت برنت در پایان این هفته ۱۰۴ دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/147079" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRgdZAdBV6-AHi2yvR1WmU_pgFxMsr-OX9f0kVBShMDdT3sU2mD8xhXc7YwLIU8_b-3mXna7sxYfP5Ow2ktnRJ96Zq8fn9QVakH9wDAqbS3WXBQ3qvQ25Tx-NQUB_fHhOR0hfGnpW3H6OO2Cb0g0WPEOszldblWKOhImpDdEh9mBDqeO_2UjP5VDf9Z5ZKJ-DhmfZm_71ke9rQJpr92_9S1WcJczJgQcFs8mPAmMkr-yom0rBLfp9RHj780McRBkT-ZeaQA3wesVybgaxwMJGtlYWgXOpnSFkASqMDNFxC_1ETmOyosgNLYi-yjlPHV9VB64gAVtxjdmhH-TmLfovQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لاوروف: روسیه آماده مذاکره با اوکراین است
🔴
وزیر خارجه روسیه گفت مسکو برای مذاکره جهت حل مناقشه کی‌یف آماده است اما عملیات ویژه نظامی را در طول این فرآیند متوقف نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/147078" target="_blank">📅 18:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147077">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6346739a2f.mp4?token=tEh5l8UztR-IovyOg9FXOez0GOM3ZCYn2H-PVRdRLxmU7GQ2hWPsc6k5kD5DbsGF00pCh9DbqgJ_uT-mUy4y6FDQ44nkIqsy5VQgcZ6roi1rAT4p8AGQdv3a21a8kOFg0KgWDWrS64NRZ1018agy-xjpLAZZdD05BY29kblAQ1br0CLfCYu4Tb8ua1SWotA2gKceZvXwiGuvwsLWxgjiMh0A63fVCwnfQOUITqN4ZZJsRGz29NCtpBKtBXQawP84bjemu-Sgnn6AdjUr0MO-WxCkq8BHY_gfpBhCpdrfHNRUaik2EPxkxmNH1ZcUAu_l8puJpQONFWjWJRmuNWSQAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6346739a2f.mp4?token=tEh5l8UztR-IovyOg9FXOez0GOM3ZCYn2H-PVRdRLxmU7GQ2hWPsc6k5kD5DbsGF00pCh9DbqgJ_uT-mUy4y6FDQ44nkIqsy5VQgcZ6roi1rAT4p8AGQdv3a21a8kOFg0KgWDWrS64NRZ1018agy-xjpLAZZdD05BY29kblAQ1br0CLfCYu4Tb8ua1SWotA2gKceZvXwiGuvwsLWxgjiMh0A63fVCwnfQOUITqN4ZZJsRGz29NCtpBKtBXQawP84bjemu-Sgnn6AdjUr0MO-WxCkq8BHY_gfpBhCpdrfHNRUaik2EPxkxmNH1ZcUAu_l8puJpQONFWjWJRmuNWSQAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری‌هایی بین نیروهای حوثی و نیروهای وفادار به عربستان سعودی در غرب شهر تعز رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147077" target="_blank">📅 18:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFiNW5Vs3p7K4IHi5u_0ycVvNGdwoK1eEGDIP_Wv-KtXIGC45-N7lpIB_cJnsWRwyonY_ToOONsWbQ339CzFpMgjYJeMH6ehAyfvfHCOzoHwQlEOLyD2NaIfq0j_7-XvA8qg2PCnsAVxN0kxpihA1QDH-JCi3jRTg4XsMyc5g1VfOS1HilJXBmn8KG_M0KI2UjmmxU8yz8V_9OtkDUI6D4Yq7t4FT3ThruQWaA9sLPOZWQcFsjXbodjouQeiASUrcTW636xtLL4mS9O2u99Vf77Vl9gt0dkm8FlDbs24RIRAw5VAoU-BnIc7w5qocgrg7d9pQR32EqQMxR9fTWHTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طائب، رئیس بسیج: اسرائیل رو نابود میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/147076" target="_blank">📅 18:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLNEJJmcJqXHN5ENUBYjlcJCL6G2PVVzlHUQPfy0z6ECA8Fet3yB5O47jY4jRqXkuGDx_unEHWugD_Qz04vFPo_voTOlpVAOuO1KTMLzpvwiPlexb58E7ZkaX6jxoN-PRPZZoq18scs4BCL4IzKHH1UQFRurvWICEVuq_OpjUzd11niN-_eekWMGnE-_bYCBgh_7HWyKb6lcO-qnNu-ng9CNgpZwOdhislbk-xI3XnlWonFs79g3nqKXaFuE-fXRhW5K_U-vTrug-o52kLzxkXAWCbvrwUz3UX9ggXZx1zKFyno_ZoQRdyEfOKRbU3xEekjxvl1IbaGSVyIvj55O_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام ارشد ایرانی به رویترز:
جلسه‌ای که قرار بود روز دوشنبه برگزار شود، به درخواست عمان ترتیب داده شد. انتظار نمی‌رود که در این جلسه به توافقی برای باز کردن تنگه هرمز دست یابند. ایران به توافقی نیاز دارد که به آن اجازه دهد از کشتی‌های عبوری در این تنگه عوارض دریافت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/147075" target="_blank">📅 17:53 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
سفارت ایالات متحده در امارات متحده عربی آمریکایی‌ها را به اعمال «احتیاط بیشتر» در اطراف اماکن یهودی و مرتبط با اسرائیل، از جمله اماکن عبادت، هشدار داد.
امارات متحده عربی همچنان در سطح ۳ «بازنگری در سفر» به دلیل تروریسم و تعارض مسلح قرار دارد.
این یک تهدید خاص و جدید نیست، بلکه یادآوری‌ای در میان ریسک‌های افزایش‌یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147074" target="_blank">📅 17:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147073">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بحرین اعلام کرد
تا زمانی که روابط دیپلماتیک با
تهران
برقرار نشود، از شرکت در هرگونه نشست با این کشور خودداری می‌کند و پیشنهاد عمان برای برگزاری نشست وزرای خلیج فارس و تهران در مورد تنگه هرمز را رد کرده است.
بحرین چهار شرط تعیین کرد: توقف حملات، پرداخت خسارت‌ها، احترام به حاکمیت و حل اختلافات از طریق قانون.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147073" target="_blank">📅 17:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147072">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-hethfFMwjswzMUWF5IjC2vnU28D6RNp77Elyq0N57LCWrnFWJDjBCEkOdy5pWzFuQGX920rNAx9E3yipTRfUMj5NHFpG3JMhzhtW7SVSIRkVv5jtUqVS7uqdKUHYtCQ6KaSy1jZXe9VzIn4pp7hUlOjfOYfGyyh82jCakRPVTBgIn6yjAZEgrZ0Y9v4f5sLm7_LjPIce47-PUx0RJ3T8YGKY1XbNpsbOmBW_7NPz35aZv863qM_m5kQhz4C2WNj8LOBOCjFcUsawDP9hAq32fAL2WG2HXePqqDcTfQExeUS7q3Vf0rnWoX8rYXgOuTWRf8teWbbhobQvViZ6KI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای خرید آیفون ۱۸ پرو در هر کشور باید چند روز کار کرد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/147072" target="_blank">📅 17:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147071">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
رئیس‌جمهور چین، شی جین‌پینگ، پیشنهاد ایفای نقش در مذاکرات صلح میان آمریکا و ایران را مطرح کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/147071" target="_blank">📅 17:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea0cc24d7.mp4?token=TN0-wECzswp1BsNBfntli7cZQ4v3OYh9b-_wGVwN5FMDOGwfHMJfKqpDXN0qFsEh8lCE-i64lzRsUpUVRFPOlBxEjop1hXX_K6WskFs9S2fmQxjr4_PTmGdzu4E19UB_wS2dH1fsh21wFSPb8j4S8luxAdv74JQ7wnMb4P7WuGLbgzqHD-pOb6aGMKCtQzEg_Rx1D_lVEflr0JLkouGo5LzM_yM929810hSlnIFqmC5Lm4YGEDyYqGaqJagd6NUCIfowOXeDqY1d3CmNLeYC6m5qG-U_dbLwCHqg6wZmDciZD2nWBmjKOJ3JJSEuAtFDAULzxzH94hCUZYL1tA1PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea0cc24d7.mp4?token=TN0-wECzswp1BsNBfntli7cZQ4v3OYh9b-_wGVwN5FMDOGwfHMJfKqpDXN0qFsEh8lCE-i64lzRsUpUVRFPOlBxEjop1hXX_K6WskFs9S2fmQxjr4_PTmGdzu4E19UB_wS2dH1fsh21wFSPb8j4S8luxAdv74JQ7wnMb4P7WuGLbgzqHD-pOb6aGMKCtQzEg_Rx1D_lVEflr0JLkouGo5LzM_yM929810hSlnIFqmC5Lm4YGEDyYqGaqJagd6NUCIfowOXeDqY1d3CmNLeYC6m5qG-U_dbLwCHqg6wZmDciZD2nWBmjKOJ3JJSEuAtFDAULzxzH94hCUZYL1tA1PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته، دبیرکل ناتو: روسیه متحمل تلفات بسیار سنگینی شده است که اکنون تخمین زده می‌شود بیش از ۴۰ هزار نفر در هر ماه یا به قتل برسند یا به شدت مجروح شوند.
🔴
لحظه‌ای در این مورد فکر کنید. بیش از ۴۰ هزار نفر. در هر ماه
🔴
با وجود این تلفات سنگین، پوتین هیچ تمایلی برای پایان دادن به جنگ نشان نمی‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/147070" target="_blank">📅 17:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwcfwBvG01lWq918J8Nh6Un8B0LL0EpAM43rJSMq1nrQwqmBNGZT-_FCBX0SRZoqppNDYBO8ookmfXt7YDojSsYS5eUZ2DE7xH-b_LV-3dsSJZ1mmQmVtoXqZ1U0rWYST9WpZ3Gv6MKq8MAjDM01PJ671ltioVXQSbKWR0AzZ-A0nkj3veUmHwoxgZXANBSocipYd0ASPHK4uoDuaHNk_YiXyk-SBzxHOw_mUmmFXEl4B23YczbCJgQqRdnjYzDcpHNwrWpEN1Vtiz5_iXj1eD82epyuQhhTDOg3d09syBZTfwdk6r0XsfynPpXCYjYFrjGOcx_x8ONqbJ7TsfEQvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: ایالات متحده با یک چالش جدید مواجه است: اگر حوثی‌ها تنگه باب المندب را مسدود کنند، ضربه دیگری به اقتصاد جهانی وارد خواهد شد و 7 درصد دیگر از عرضه نفت جهانی و حدود 12 درصد از تجارت جهانی را محدود خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/147069" target="_blank">📅 17:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / بحرین اعلام کرد که در نشست ایران درباره تنگه هرمز شرکت نخواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/147068" target="_blank">📅 16:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147067">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دولت عراق: نخست‌وزیر با درخواست ایران برای انجام تحقیقات مشترک درباره کشف سکوهای پرتاب پهپاد در مناطق مرزی موافقت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/147067" target="_blank">📅 16:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147066">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c66927e311.mp4?token=UG2Lf6H7u4gadW4ZVh1cy-0FYG2MTUOFK9HHxOid3PvxGLWhB3ND62rd184qM9m1xx-fH7JS3s12nhB5u34VJ8DsHHof_Tkil1fB5v9VX6ZcbKhJXur23Fe_5sVqi1FaLT1cxGIvYwlEeQ7BDDXWOj7AuLrSEHE-tdLmIfAqIlulGLi1Qgef2ezSLu2jF3Pkv2HMZrl2lH-vF9PDoCiiAm87N8_vZveVOggdMXe8v-CsWpKthJiQsASJmlvYeog-QgALYtg-BNVRYh5OtCYBAvsDXoy2thr3YX775Mj6BL9ilPEc3D9Fpr2cGL0Viud9xWTZmPSn5clyseTxIyM2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c66927e311.mp4?token=UG2Lf6H7u4gadW4ZVh1cy-0FYG2MTUOFK9HHxOid3PvxGLWhB3ND62rd184qM9m1xx-fH7JS3s12nhB5u34VJ8DsHHof_Tkil1fB5v9VX6ZcbKhJXur23Fe_5sVqi1FaLT1cxGIvYwlEeQ7BDDXWOj7AuLrSEHE-tdLmIfAqIlulGLi1Qgef2ezSLu2jF3Pkv2HMZrl2lH-vF9PDoCiiAm87N8_vZveVOggdMXe8v-CsWpKthJiQsASJmlvYeog-QgALYtg-BNVRYh5OtCYBAvsDXoy2thr3YX775Mj6BL9ilPEc3D9Fpr2cGL0Viud9xWTZmPSn5clyseTxIyM2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خودروهای زرهی متعلق به امارات تحت کنترل نیروهای حوثی یمنی قرار دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/147066" target="_blank">📅 16:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147065">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsTaPeYCGYPCTT6iNkGbUkxw7BHeHT72c0UeuKq4fBvMfYFh6AMFEQqil6H85dX9uk3wm_pnGfnYUriHS3ETH1r4t-EKCdPd8jRJPSQF9JgI3X8KkW7-EZdJykk5RplL9B3Uq3gNeANOoQT8WUY94e5KCAMGONiRnozrpLGI1RZJUa7uc1-fk92Q6GWGiG528SjtubkQsCoY5ohflRyer0JHA80yeyToPizqQakKvrvPhRW712RK0TNKvsZ9VVN1HYNWxIbZVoY6tFeZqlCKImWXgAkDxbpxKqMl7jKLVgOLohaLiFLWUdUorlABaydBFV7PW34cscT555KwwLkqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارسال مقالات علمی هم تحریم شد
🔴
معاون تحقیقات و فناوری وزیر بهداشت، با انتشار تصویری از صفحه محدودیت دسترسی شرکت Salesforce به دلیل قوانین تحریم‌های آمریکا، از ممانعت کاربران ایرانی از ارسال مقاله به یک مجله علمی خبر داد
🔴
در تصویر منتشرشده، نوشته شده که این شرکت برای رعایت قوانین و مقررات کنترل صادرات و تحریم‌های اقتصادی آمریکا، دسترسی کاربران از ایران و چند منطقه و کشور دیگر را به برخی خدمات خود پشتیبانی نمی‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147065" target="_blank">📅 16:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147064">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
ترامپ: ناتو و اروپا در قبال ایران «بسیار ناامیدکننده» بوده‌اند!
🔴
ناتو نمی‌خواست در تنگه [هرمز] به ما کمک کند، با اینکه ما هیچ نفتی از این تنگه دریافت نمی‌کنیم
🔴
ما همه مین‌ها را از بین بردیم؛ دیگر هیچ مینی آنجا وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/147064" target="_blank">📅 16:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147063">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=Wq_cz9UwAzF27urSAqbu11BT7iZ4zfq5dVjU40_cTZRToP2n37yylwPV7DEcZPmwvXpQZ268CBd8usbwWd0VpX5A038GVv0_Vpv0HMTd_YtR9gBuJxGeR9YIokIxkHePj1TO-zc8sA_Ac9ArLr0itE3tnrWPJ3ighO3pOHUtm-YD8-TTG472tU1sEWto3wfAFIc25AFmdPGFcZl68T9zn27_OMV1r_GH0UWWPD3Osc9mgnAj75GpBRecoDIX9dFA3huRo7YFslqV_urrJ6byfggWQabEbP6Bq5I_17NyAKiGunfeL4irCVz2agXJi42wpSc3mI6g1ijYwgSiNsuH2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4d0c57f91.mp4?token=Wq_cz9UwAzF27urSAqbu11BT7iZ4zfq5dVjU40_cTZRToP2n37yylwPV7DEcZPmwvXpQZ268CBd8usbwWd0VpX5A038GVv0_Vpv0HMTd_YtR9gBuJxGeR9YIokIxkHePj1TO-zc8sA_Ac9ArLr0itE3tnrWPJ3ighO3pOHUtm-YD8-TTG472tU1sEWto3wfAFIc25AFmdPGFcZl68T9zn27_OMV1r_GH0UWWPD3Osc9mgnAj75GpBRecoDIX9dFA3huRo7YFslqV_urrJ6byfggWQabEbP6Bq5I_17NyAKiGunfeL4irCVz2agXJi42wpSc3mI6g1ijYwgSiNsuH2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: تاسیسات هسته‌ای صلح‌آمیز باید از حمله و تهدید مصون بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/147063" target="_blank">📅 16:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147062">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
آرش اعلایی، خبرنگار اسبق اینترنشنال: عربستان تا ۱هفته دیگه شورتش پرچم میشه و آمریکا هم کلا منطقه رو بیخیال شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/147062" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147061">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کاخ کرملین: هنوز مشخص نیست که آیا پوتین در اجلاس سران گروه ۲۰ در میامی شرکت خواهد کرد یا خیر.
🔴
اگر زلنسکی واقعاً تمایل به ملاقات با پوتین دارد، می‌تواند به مسکو بیاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/147061" target="_blank">📅 16:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147060">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
دلار بزودی 300هزار میشه
⁉️
🔴
تحلیل ترسناک نوستراداموس ایرانی
👇
https://t.me/+WZbLEaPPJQUwZDU0
https://t.me/+WZbLEaPPJQUwZDU0</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/147060" target="_blank">📅 16:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147059">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
حاجی دلیگانی، نماینده مجلس: طرح سه‌فوریتی خروج ایران از NPT آماده شده است
🔴
بهتر است هر چه زودتر آزمایش‌های لازم را برای سلاح هسته‌ای انجام دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/147059" target="_blank">📅 16:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8i-yTixrY4CUB2hf4ZJGD6DohJ5nITV23s1g1_kpoGCNuNmVP4qE5YwLM2c6uVbDHu3nwn6e8inDLkAd9gRafuqLjdhe-HfMYufAYfKDeWgfyk6CJBh_MAB7y0ts4MSqeAJfGQ0yOmrf1nE6k6eHly2N3nhKCQlzLDrWEYqAYAZSES-DtL5DNJjqy3CrhF3SxGfRl1zBXTvI63jV7JAnyOxBrMPNWq744zi0hzeBoY1kBQdcJhddO0SAd1gqpedGCMBQvMqK9V68rsk959IwXbxOWiiQuymXzPCy1G0J6eUTqG2-x45qZSIPiTMVnn-c1Y6RdMQ64orly_yEQHhhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلقک بازی امت معکوس در شب نشینی‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147058" target="_blank">📅 15:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c3694001e.mp4?token=vAmVIcrFnJeLgRq9U_1S1ej9ojs4F44KlRsIyphBg8dZ8KzemIY008YXQENZESOBOMm8fld7TAEfeXfWoS6KsW7qHuoaKbsvqDbKUbuYy5zz7newPkQwaLP6IuZ-yAgl5PAbvoR36c708uZeEgRLQE6Kg4yt-V03xbIbSL2fZS2wZFf2Uey3g2WcmbkdO7GiUQqclonkOFl2_TweLFmaDpd6d1z5Zh7qwDEJo65hDHWSgxOdSkvcCKtJM3KLWU8pk30eTg5qBJ7g3Kal5al_zVVV0yV65ix4AcxGw_g6gZH-_1rKf4wB9anm525eNMwOntIfKgrHKAwX--DyM3n0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c3694001e.mp4?token=vAmVIcrFnJeLgRq9U_1S1ej9ojs4F44KlRsIyphBg8dZ8KzemIY008YXQENZESOBOMm8fld7TAEfeXfWoS6KsW7qHuoaKbsvqDbKUbuYy5zz7newPkQwaLP6IuZ-yAgl5PAbvoR36c708uZeEgRLQE6Kg4yt-V03xbIbSL2fZS2wZFf2Uey3g2WcmbkdO7GiUQqclonkOFl2_TweLFmaDpd6d1z5Zh7qwDEJo65hDHWSgxOdSkvcCKtJM3KLWU8pk30eTg5qBJ7g3Kal5al_zVVV0yV65ix4AcxGw_g6gZH-_1rKf4wB9anm525eNMwOntIfKgrHKAwX--DyM3n0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کانادا
:
به احتمال زیاد، به زودی شاهد توافقی با کانادا خواهید بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/147057" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147055">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHDrrQ2xXQ444wtBfL5WcEW0OLIvt09RepgmbOVeaiEuxk4nKUOmnPHClWBJ7vvX6xcO9xxq8R6qxX_Lq8MbSjUbxQcoT_T5e_krhAEjFTgaU6xfKl40-BO8afj7jnCaf9UJ2NH35dOedQfNshmKSnz_LPK428RH5u0-bBuoqRv_mFh8g2S_Bkg9bcPTziOnEtPnNE8HWMAotC3JLkXIlEWVxTPtvc13AhLh8unMjQm3IX8ZZAEKsbDe_N1n810U1IXtMZQlvraNTKlHZcxC0EfYREkLn8OibabgaGqa-pWxMckL47JCnWI8PoXJBVLEeCZa2IhQ5fGD9G9-2IqEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e8deb1520.mp4?token=smXOk4vojlev-i9bCo_n8Upp9T1shn-UhnHv3ngLt2wxXiLjBA_IQRJQtgGpbeVJhjxhz2ERRjCWnB73rjn8Hyur2fYPhwhv4QdJD488J9m8GeYPOlsbmy3lJdFBWJFlJnyg0VRUQwgMTQjGLSuAtFrVyixoSk91TJgXuLemr5MFJ6nQKRwGpTpBPrRUL_ewe0AmLM3tSpLN3LkMFwbU7eVvo7M6jIUQHJxu2AN31uwZqGICg2JXXxaMrYm0yhuc4ka_fOMXg7M2a_Jhz3flR-StHBRTl33fNBJ4E4J9SuPj5Lg6foKCtshDll7xZSOH-DjUHjRS3zvnAPBV_rNm3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e8deb1520.mp4?token=smXOk4vojlev-i9bCo_n8Upp9T1shn-UhnHv3ngLt2wxXiLjBA_IQRJQtgGpbeVJhjxhz2ERRjCWnB73rjn8Hyur2fYPhwhv4QdJD488J9m8GeYPOlsbmy3lJdFBWJFlJnyg0VRUQwgMTQjGLSuAtFrVyixoSk91TJgXuLemr5MFJ6nQKRwGpTpBPrRUL_ewe0AmLM3tSpLN3LkMFwbU7eVvo7M6jIUQHJxu2AN31uwZqGICg2JXXxaMrYm0yhuc4ka_fOMXg7M2a_Jhz3flR-StHBRTl33fNBJ4E4J9SuPj5Lg6foKCtshDll7xZSOH-DjUHjRS3zvnAPBV_rNm3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو تهران (ونک) یه غذاخوری افتتاح شده به اسم کتلت بی بی که فقط تخصصش  کتلت درست کردنه
🔴
حالا قراره به دلایل نامعلوم پلمپ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/147055" target="_blank">📅 15:41 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147054">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">💵
ماهانه بالای صد میلیون تومان تو خونه خودتون با ارز دیجیتال پول دربیارید !
💰
🟢
‌‌‌‌‌‌‌دیگه مجبور نیستید برای دیگران کار کنید!
🟢
‌‌‌‌فقط با یه گوشی!
🟢
‌‌‌‌‌‌‌بدون نیاز به تجربه!
✅
‌‌‌‌‌ آموزش ۱٠٠٪ رایگـــــــــــــــــــــــــان
جا نمونین ازش لینکش
👇
👇
https://t.me/+fDXpi2Dbi185ZjRk
https://t.me/+fDXpi2Dbi185ZjRk</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/147054" target="_blank">📅 15:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147053">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40b6de5cd2.mp4?token=eEJyAyiJOZ-df-0TxCJVuQdJbNFEm_MnHBhKZ4jipfwGDP8xNzuVygBczSsLtNqi7Oo1rw9eDjamjK9H0ZVXJMajPaKA4hHkHeAwfpPzmHfH2JvmaZdqI7M1P4ZFqOJYMOCiAcm0_e8cyjBAK7LlVBAOtzkzlLT7Q7U2At4QYcGOH9NNqrkZgbE8X40aOkUCEtJU0xFDrPSO2q5TDuVtISBF0KNRljo4L7VqcePuGERjioFcmkkKvvpqGOBh3Yjh1vtGVfwHKsbTl6KmgG0M7fMoWMySn_mja8twZZh3SQva6pNBA9Vw3hB1S6gpb2qD51IuW_hHGJaEqDfSoobG2Ah8VdvGtK34RrcUvsNI4cqRz_d_a2FHHiA4Cg9ew88tQWaFR4irfyXkFm4Rzh8jfetZfP3EeZ_uAYYSC0NAjP3QiZfwjkK-THrFt6jRL7oT24GAWu7LUp92f_wf57cgw8xiJDsPAx3FD-Ky1xs213BhbJO9jR5WJw_Pqvb36a6WCgYpvLl8dw6_VxiJQ6KTdy18ckZsjWfUhWAoo3RQBTWEi0xnw9Z9mOe5QsAKWDyWuSyE9KxLo7UvsITt1nYez4GGMZnJBS25-EYI0TXHl7NsxwDNQybQz0SuT9g5XvtZha5bZKBloHc0ppYgibOxuuyzSTrXjEDInTcuuUl8-7M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40b6de5cd2.mp4?token=eEJyAyiJOZ-df-0TxCJVuQdJbNFEm_MnHBhKZ4jipfwGDP8xNzuVygBczSsLtNqi7Oo1rw9eDjamjK9H0ZVXJMajPaKA4hHkHeAwfpPzmHfH2JvmaZdqI7M1P4ZFqOJYMOCiAcm0_e8cyjBAK7LlVBAOtzkzlLT7Q7U2At4QYcGOH9NNqrkZgbE8X40aOkUCEtJU0xFDrPSO2q5TDuVtISBF0KNRljo4L7VqcePuGERjioFcmkkKvvpqGOBh3Yjh1vtGVfwHKsbTl6KmgG0M7fMoWMySn_mja8twZZh3SQva6pNBA9Vw3hB1S6gpb2qD51IuW_hHGJaEqDfSoobG2Ah8VdvGtK34RrcUvsNI4cqRz_d_a2FHHiA4Cg9ew88tQWaFR4irfyXkFm4Rzh8jfetZfP3EeZ_uAYYSC0NAjP3QiZfwjkK-THrFt6jRL7oT24GAWu7LUp92f_wf57cgw8xiJDsPAx3FD-Ky1xs213BhbJO9jR5WJw_Pqvb36a6WCgYpvLl8dw6_VxiJQ6KTdy18ckZsjWfUhWAoo3RQBTWEi0xnw9Z9mOe5QsAKWDyWuSyE9KxLo7UvsITt1nYez4GGMZnJBS25-EYI0TXHl7NsxwDNQybQz0SuT9g5XvtZha5bZKBloHc0ppYgibOxuuyzSTrXjEDInTcuuUl8-7M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جزایر فالکلند:
من نمی‌دانم که آیا بریتانیایی‌ها مایل به سفر به آنجا هستند یا خیر. این مکان بسیار دور است؛ صحبت از هفته‌ها سفر با کشتی است.
🔴
من مطمئنم که در این بحران احتمالی فراخوانده خواهم شد
🔴
احتمالاً من می‌توانم این موضوع را حل کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147053" target="_blank">📅 15:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147052">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f83c0d55.mp4?token=cS7mnCMQ2MqNL4xa9VSbyfXzo1Jt1v19fYXeM0g3u9VuVBJk_IwyYfEkrSgErpveIfmnrGGx5YuVpYssyGqDpBmySihdiPhVRik5X9ohc8faOEtxYSViBuKrVz1xtXziMNETJ49jKCn1_Cq8y3reaw156TfJtKt9d37EWyRPObYknTd2DGOS1-5qwmSCSTmfY7jSDlIXqjdczz2cwE4LvOgqo32dw2Q4TgU8XUspXvF2Iu-xls9Mvf06GKbTY0YEEg-Ne73zlXslLeCQBz9EW8mN45JeXXtmoAclfB8DlEBeYqNlkkQ6zgOpXGSMVBSlg55zKf2h3JYhTEwQ7tOVWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f83c0d55.mp4?token=cS7mnCMQ2MqNL4xa9VSbyfXzo1Jt1v19fYXeM0g3u9VuVBJk_IwyYfEkrSgErpveIfmnrGGx5YuVpYssyGqDpBmySihdiPhVRik5X9ohc8faOEtxYSViBuKrVz1xtXziMNETJ49jKCn1_Cq8y3reaw156TfJtKt9d37EWyRPObYknTd2DGOS1-5qwmSCSTmfY7jSDlIXqjdczz2cwE4LvOgqo32dw2Q4TgU8XUspXvF2Iu-xls9Mvf06GKbTY0YEEg-Ne73zlXslLeCQBz9EW8mN45JeXXtmoAclfB8DlEBeYqNlkkQ6zgOpXGSMVBSlg55zKf2h3JYhTEwQ7tOVWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره شی جین‌پینگ و چین:
مردم می‌گویند او از ما جاسوسی می‌کند، اما ما هم از او جاسوسی می‌کنیم. ما هم در این کار خوب هستیم. با یکدیگر کنار می‌آییم.
​
🔴
اینکه روابط خوبی با هم داریم، اتفاق خوبی است. اکنون روابط ما با چین خوب پیش می‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/147052" target="_blank">📅 15:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147051">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ea108cac.mp4?token=a407JuPRk_E1hTUHubxO50xhj_fhiZo8bhIxpOIagCm661q4jgvLrZqFnLaEazixyZ9z1mQqYgOi95sKdXQYH7rJXVuWQ_D9ZGlTbhNEWqqZE1rM8wWA300JrfB3lFl7YzeVFReik0OOjsoRhQNGbsnrVfee28Yf9SYkQxKuk4n1XRp6dlWB7D7HFLUHD-GtLKh7oSrcLtqFCag5ZzHsF_L-D-uhRFPNVf0I2UoK1ZQHmIJxOwHoUQx9SrNu_p7-n9U0GVQ3WHD7rG7Fiy5UVmFozSbm_21xBEzu9NiIS_0LCDMeRDWGOga_OeoW2I2ieBjogWw-CIFHMwhcv4n5XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ea108cac.mp4?token=a407JuPRk_E1hTUHubxO50xhj_fhiZo8bhIxpOIagCm661q4jgvLrZqFnLaEazixyZ9z1mQqYgOi95sKdXQYH7rJXVuWQ_D9ZGlTbhNEWqqZE1rM8wWA300JrfB3lFl7YzeVFReik0OOjsoRhQNGbsnrVfee28Yf9SYkQxKuk4n1XRp6dlWB7D7HFLUHD-GtLKh7oSrcLtqFCag5ZzHsF_L-D-uhRFPNVf0I2UoK1ZQHmIJxOwHoUQx9SrNu_p7-n9U0GVQ3WHD7rG7Fiy5UVmFozSbm_21xBEzu9NiIS_0LCDMeRDWGOga_OeoW2I2ieBjogWw-CIFHMwhcv4n5XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط هواپیما در حیاط یک خانه در روسیه
🔴
در پی سقوط یک هواپیمای کوچک در حیاط یک خانه شخصی در روسیه دو نفر جان باختند
🔴
با آغاز تحقیقات کیفری، بازرسان احتمال خطای خلبان و نقص فنی را بررسی می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/147051" target="_blank">📅 15:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147050">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=Yx0lYsgwf4K5CQeJLbSZUqY-KcQP8JNla3RfX3NC3ZubVKizebKSPwITbWhzd5NNJD_jgUJ4tmacnjIqsawmiDQ_4qUQ4jB1gK8AGVVKQNS9HXroNnehCYt21HDh4AgeWIMEWXbLJI9Pno99uAz3PDYV3ayODujtoILSuMYlDuhNOkUfT_EfMPzJomPmTeG8ZlAnDvKiDXm3gxILYjpsmaLNUETl3-HeLQq86RKNMD1_RytUEDbBGnTLecHtWq3oWNNc_EfkhHMPy56Zkfs1PNluxRQQZWPFK65ttYlrSIShZlxnzj_gGFXA8IurD8sqPLNF-Gpg986Dx1Wd_Wtx8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a405ba0f.mp4?token=Yx0lYsgwf4K5CQeJLbSZUqY-KcQP8JNla3RfX3NC3ZubVKizebKSPwITbWhzd5NNJD_jgUJ4tmacnjIqsawmiDQ_4qUQ4jB1gK8AGVVKQNS9HXroNnehCYt21HDh4AgeWIMEWXbLJI9Pno99uAz3PDYV3ayODujtoILSuMYlDuhNOkUfT_EfMPzJomPmTeG8ZlAnDvKiDXm3gxILYjpsmaLNUETl3-HeLQq86RKNMD1_RytUEDbBGnTLecHtWq3oWNNc_EfkhHMPy56Zkfs1PNluxRQQZWPFK65ttYlrSIShZlxnzj_gGFXA8IurD8sqPLNF-Gpg986Dx1Wd_Wtx8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما: مرزهای بسته‌شده توسط عراق در چه وضعیتی هستند
🔴
ساعتی پیش مرز چذابه برای اتباع عراقی بازگشایی شده، اما هنوز خبری از بازگشایی پایانهٔ عراق به‌سمت ایران اعلام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/147050" target="_blank">📅 15:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147049">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba6f72c328.mp4?token=FnUNGHOcmtGyzl1JAXVIFPYG7KEG866hbCCjcwUd21-uFWjp3aGDd3It_pc4q3Ixfswjl190MENIcCDjd4tNBYv8c7RuIok0lf1Qdrl6KL-iAXAkG65D0_l23ueY9W4GhGjiyAg-krfdic0QdXfnH8OlqwFjNPIr_IQdlPoOwSvLl2VxqMqFHot1sjUHA7Hmd064ir8mxGly1m2SHlX2mz_ALBySH9YEMk9_oe8OBlFGHbQj0QZY8fNnx4-sbZTrm8YPbufMolS8qcsX9J_mP2g6fsaRQjyzoEKXyG_nwbBTpIn38E9_GZyGdfSioMUjeRG82VumzNkAcXG457zxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba6f72c328.mp4?token=FnUNGHOcmtGyzl1JAXVIFPYG7KEG866hbCCjcwUd21-uFWjp3aGDd3It_pc4q3Ixfswjl190MENIcCDjd4tNBYv8c7RuIok0lf1Qdrl6KL-iAXAkG65D0_l23ueY9W4GhGjiyAg-krfdic0QdXfnH8OlqwFjNPIr_IQdlPoOwSvLl2VxqMqFHot1sjUHA7Hmd064ir8mxGly1m2SHlX2mz_ALBySH9YEMk9_oe8OBlFGHbQj0QZY8fNnx4-sbZTrm8YPbufMolS8qcsX9J_mP2g6fsaRQjyzoEKXyG_nwbBTpIn38E9_GZyGdfSioMUjeRG82VumzNkAcXG457zxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ درباره ناتو: اصلاً چرا داریم به آن‌ها کمک می‌کنیم؟
🔴
بعداً در این‌باره بیشتر خواهید شنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/147049" target="_blank">📅 15:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147048">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731f902b63.mp4?token=hJtEUwF3YKKTc1dplQvAbfdpzrN-_xnMZ3GntvzxiiI9FqCHltH2wqLANa5bEnybNQ2Pc3QkiSF4AJcaHYllikZ2FxGL80KgEynvEDK0a9M9jlHmYa5NaN_gqKZ6xf5BTwesCOoo21YwhqDLsMKtygA2SufdoGgphCsNf6jpUrQqf-IzakLXifMNuzIc17DOnyjvGpSZ9KKhgYyaXrLM0ObOD65icykASk3Bfuo8Sl-nisPj9sAmIyobWA7eaH4W31IEmlGesO7sjxxX4n2Y0n3yksHC5l9NZoUeDuigidmdYRmCHee8WzRAAPw2MLXayCjr9AO90cpdDbxdYbKE34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731f902b63.mp4?token=hJtEUwF3YKKTc1dplQvAbfdpzrN-_xnMZ3GntvzxiiI9FqCHltH2wqLANa5bEnybNQ2Pc3QkiSF4AJcaHYllikZ2FxGL80KgEynvEDK0a9M9jlHmYa5NaN_gqKZ6xf5BTwesCOoo21YwhqDLsMKtygA2SufdoGgphCsNf6jpUrQqf-IzakLXifMNuzIc17DOnyjvGpSZ9KKhgYyaXrLM0ObOD65icykASk3Bfuo8Sl-nisPj9sAmIyobWA7eaH4W31IEmlGesO7sjxxX4n2Y0n3yksHC5l9NZoUeDuigidmdYRmCHee8WzRAAPw2MLXayCjr9AO90cpdDbxdYbKE34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ما یک درگیری نظامی کوتاه داشتیم. آن‌ها می‌گویند: «آیا ممکن است از کلمه «جنگ» استفاده نکنید؟ چون وقتی از کلمه «جنگ» استفاده می‌کنید، موضوع کمی متفاوت می‌شود.»
🔴
به نظر من، این یک درگیری نظامی است. ما آن‌ها را به شدت تحت فشار قرار داده‌ایم.
🔴
در مورد ونزوئلا، ما آنجا را تحت کنترل خود درآوردیم. ما در آن جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147048" target="_blank">📅 15:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147047">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
بیانیه مشترک گروه بریکس: بار دیگر بر تعهد خود به حل‌وفصل مسالمت‌آمیز مناقشات بین‌المللی از طریق گفت‌وگو، رایزنی و دیپلماسی تأکید می‌کنیم.
🔴
خواستار اتخاذ رویکردی چندجانبه هستیم که دیدگاه‌ها و مواضع ملی متنوع درباره مسائل مهم و حیاتی جهانی را محترم بشمارد.
🔴
بر ضرورت همکاری برای حفظ جریان روان تجارت جهانی، زنجیره‌های تأمین و جریان انرژی تأکید می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/147047" target="_blank">📅 15:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147046">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb1aee77d.mp4?token=C4oDfPBb6kFhpIcUXG4Q7sOko5o6BNCOTviuKeQbJSlNmExgiH7WS6P_71066xnvUs5g9e4dJu_g9aVY7skdZGidc_En797jYDDuwlk0qJMxld40Ek-p_TtuSpXRwsMsqQHB_khz4KrGdfQbYHaWFdhg8wFOiywvTx_lru5ujz9XIC0Oc0eIQShg-ls0MTv4ZTs98q9S1AKS0UTnwP2d8Ph8HLzNSRQC_XGJ4kxTmMzm4pH32zrUICO9wvD7H26-6NyRldbub7KO_u46Olu9JwZj2FTzqHCI39VTYofUopRSlA1UEYtTUzMY1kNxS_P_BfajWZmt3cOujzda-sowXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb1aee77d.mp4?token=C4oDfPBb6kFhpIcUXG4Q7sOko5o6BNCOTviuKeQbJSlNmExgiH7WS6P_71066xnvUs5g9e4dJu_g9aVY7skdZGidc_En797jYDDuwlk0qJMxld40Ek-p_TtuSpXRwsMsqQHB_khz4KrGdfQbYHaWFdhg8wFOiywvTx_lru5ujz9XIC0Oc0eIQShg-ls0MTv4ZTs98q9S1AKS0UTnwP2d8Ph8HLzNSRQC_XGJ4kxTmMzm4pH32zrUICO9wvD7H26-6NyRldbub7KO_u46Olu9JwZj2FTzqHCI39VTYofUopRSlA1UEYtTUzMY1kNxS_P_BfajWZmt3cOujzda-sowXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ونزوئلا، ما آنجا را تصرف کردیم. ما در این جنگ پیروز شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/147046" target="_blank">📅 14:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147045">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3c10d8e3.mp4?token=sOQAOUY9iLCpLEIDhS218OJ_XQy8MWLsEqi6JuYTMGENLHtSpxTFM10oPJ9WrFlSBgltPjim1-ekwcr5Ct9ercZcwIx14P8CIB5H2mAe0z49hqExAaEihu03oiLvxg4uZX_FdXuWrvhYdOZSBQQ4KejotXHa5uXfLGA2h-_t0hAc38Jab-5D_XySO_b-xipW12rucNUmk2zq0mwvXwb9pegUIgvUOOnjBwWSPmgFMwv0Jcy0AG9zQ8cv7W1WYD0-IkoY3asXS2oU7dBzNyKpPrTZOEqlhUsT0ClFA4u0O7RzWYJausP_Dt_J4I9GCw9ANGhP77J_wfNmONBj84LC7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3c10d8e3.mp4?token=sOQAOUY9iLCpLEIDhS218OJ_XQy8MWLsEqi6JuYTMGENLHtSpxTFM10oPJ9WrFlSBgltPjim1-ekwcr5Ct9ercZcwIx14P8CIB5H2mAe0z49hqExAaEihu03oiLvxg4uZX_FdXuWrvhYdOZSBQQ4KejotXHa5uXfLGA2h-_t0hAc38Jab-5D_XySO_b-xipW12rucNUmk2zq0mwvXwb9pegUIgvUOOnjBwWSPmgFMwv0Jcy0AG9zQ8cv7W1WYD0-IkoY3asXS2oU7dBzNyKpPrTZOEqlhUsT0ClFA4u0O7RzWYJausP_Dt_J4I9GCw9ANGhP77J_wfNmONBj84LC7TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: از من پرسیدند: «نظر شما درباره اتحاد ایرلند و ایرلند شمالی چیست؟»
🔴
به نظر من، من پاسخ خوبی دادم
🔴
این یکی از آن سوالاتی است که در آن، مهم نیست چه بگویید، هیچ پاسخ درستی وجود ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/147045" target="_blank">📅 14:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147044">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
صداوسیما: پس از بسته شدن دو پایانه مرزی شلمچه و چذابه به شکل یک طرفه از سوی عراق؛ از ساعاتی پیش مرز چذابه برای اتباع عراقی که قصد بازگشت دارند؛بازگشایی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/147044" target="_blank">📅 14:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147043">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56e22cc60c.mp4?token=DChll-LMaV9e95bVn6g-0o2AcJyjPAWPUYnV4L8DgF-myo2cEVbI26qGoQoFO3drrWKvqb8TLbGeJyLzow0BQdOmYbml7PBeN60zW-8RVOlPahkjL21r0mQdJbiPF2ZINBNenR35o_fjiAFJ-YaALdOi8rMTf8p2jJ3GqompRIyJgxCGEPkrqd1GIvxp-k4toO_E9-OZBO07OcllfPEQ7mN7rkfEh_mqMRA4zQpEaa66pWTidCG6E3bHEFTvCLMI7X1yoiyayYoEyLVhm0zdHzgDCiMsaeFynF-fVE83c-WeBQSNZ6hFS-CUwZq9ZAmwes51C32cFZVpIjK0nAsH7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56e22cc60c.mp4?token=DChll-LMaV9e95bVn6g-0o2AcJyjPAWPUYnV4L8DgF-myo2cEVbI26qGoQoFO3drrWKvqb8TLbGeJyLzow0BQdOmYbml7PBeN60zW-8RVOlPahkjL21r0mQdJbiPF2ZINBNenR35o_fjiAFJ-YaALdOi8rMTf8p2jJ3GqompRIyJgxCGEPkrqd1GIvxp-k4toO_E9-OZBO07OcllfPEQ7mN7rkfEh_mqMRA4zQpEaa66pWTidCG6E3bHEFTvCLMI7X1yoiyayYoEyLVhm0zdHzgDCiMsaeFynF-fVE83c-WeBQSNZ6hFS-CUwZq9ZAmwes51C32cFZVpIjK0nAsH7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: خبرنگاران به قصد ضربه زدن به من سوال می‌پرسند
🔴
دونالد ترامپ: هر سوالی که می‌پرسند، قصدشان ضربه زدن است؛ آن‌ها همیشه به دنبال ضربه زدن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147043" target="_blank">📅 14:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147042">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
وای نت عبری : کشورهای خاورمیانه، سقوط جمهوری اسلامی را به نفع منطقه می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/147042" target="_blank">📅 14:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147041">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
معاون امنیتی و انتظامی استانداری خوزستان اعلام کرد: نخست‌وزیر عراق دستور داد به مسافران معطل‌مانده در دو سوی مرزهای چذابه و شلمچه، اجازه ورود داده شود.
🔴
آقای حیاتی گفت: مسافران ۲ ساعت فرصت دارند از این دو مرز عبور کنند و پس از حوالی ساعت ۱۴:۳۰، مرز دوباره بسته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/147041" target="_blank">📅 14:39 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147040">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-Y7z_6zNioq2ADD1j76_YGu0L_RpowNgE4OZSf3bhGmKiMNj39zO4pHGOoL0JbfleGG5Y0MYdhbp-PGPe3h5a-FivGNzLbly99JIdNitQisofsZvsxcbbGiNWgnl2AQfWxlLgfBZyZ7fjBESk2VAa7UZKILGDrbAU5wEoMJYZpVps2rx1kEU32LUtMRtQFMHe8tiAf5Vtt8DdRkS7SGOoHeAaCGh7_Vm2Jj70mWHnQxfzCiqYqd7G6IcxBzc6Npz223i-ThzWQsTL_4Etjzywwtdh33ll4kdG_nksr6dmRdiz6hOCyRUSeSTKp-9GXmUwhJkBrICurmqTMgkIPSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور در جریان حضور در اجلاس سران بریکس با محمد بن زاید آل نهیان، رئیس‌ امارات دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147040" target="_blank">📅 14:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147039">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
پزشکیان: برای ارتقای کارآمدی و سرعت بخشیدن به اجرای تصمیمات بریکس، تدابیری همچون مقاومت در برابر تحریم‌های یک‌جانبه، تبدیل رقابت‌ها به همکاری و استقرار دبیرخانه دائمی ضروری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/147039" target="_blank">📅 14:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147038">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/culG8yCxn-UhUongQwTFH0zctysexizJjo97uZVQcfWljEq4aML6h8Ae9DoM5Sf4Xwj48OE9A3ZnyRsYQVGmbIZzKosReQw9ckizhN5a9VSY6dagYLtKWf6QddGP0_-gZFVXdH0v5vT8sRim66Tsda6vR4BWlmM1IJXimbNMr7y2HkAPcajoVl0ogYWzgeH7zEPrCUdK__K8DqgsxI-DtDqolWPJ6y6yaeD1kltzKdDeMvIfbJiLf3xrYF7mjT87JgKLWd0zTLOkmpfBO8hS1HepFdYi8grVd84temcjQsOBP_yL0lSCUG8QzT4tXprFlhya59s1nV7KN7Lbh-9L-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این سوپر النینویی که الان شاهديم و البته هنوز به اوج خود نرسیده تا بحال رخ نداده بود و البته شاید تا صدها سال دیگه هم به این حد نرسه، شاید باورتون نشه تو ۷۵ سال گذشته فقط سه بار سوپر النينو رخ داده که هر سه تاشونم در برابر این سوپر النينو عددی نیستن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/147038" target="_blank">📅 14:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147037">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=BGnnBQ7wwJrd21A7TmsuFSwCNH3Hco3qAwyeMfKiu01QZLpPvRQqAPOBiW_ctFIXCAeJICH8S1nI-OduTvkWyG29Xk6B3mOw7mEBHqNGAM8nD-p3vZiUQBjXGxRW7dAP2xG3_8AD7g2hMXmT_lkAvXYzjIRZadi7bo4f6VLpcRXyrGFVil6QGwMMAmFQ3AV0OHiXMTvUGH_-UeCK4HWegtm0mJcthoDtF_870ri8D_U5lhQxSgrUncEeYHez_KDKnuqIC0MN6EejehoERjdkEWUMp9mdDG8-5jH156_wtiGjgXxmo3Zz81f2OPs-9ZLFtYvZr8cEUOfcjQthoCP_DLcBVumVikdekRjfkS-sYpEUHKt3Um4ykjZTLvkEylFbM2-AilDdiRkH0CPcO04ERnn5RUs2qU4Nn9JTtYKgL68wDb5cAQTyx9WIOsmf0JLr0P33udj2EvDhJ3_2YVx91bCITmFEYUIPnjDz4iH7Q5umAKAsACTvD1f-pUTXf2_nA0fgC12FEBVQkPtsYeHzKDkb1_ddjqZ2Dlo36KCrlHz1bQLApvPwDrojRaOFyxZFYzt3-30LjSlsaHLIsNallUWMHyXseGW5yNqaw5nj1Ud2kTo2-TP7sQOqatHCXs5s9U8W2KZbxAi2GyvKvqyWX0-gULaGIUpAkgmYAl-AE-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64984e2da7.mp4?token=BGnnBQ7wwJrd21A7TmsuFSwCNH3Hco3qAwyeMfKiu01QZLpPvRQqAPOBiW_ctFIXCAeJICH8S1nI-OduTvkWyG29Xk6B3mOw7mEBHqNGAM8nD-p3vZiUQBjXGxRW7dAP2xG3_8AD7g2hMXmT_lkAvXYzjIRZadi7bo4f6VLpcRXyrGFVil6QGwMMAmFQ3AV0OHiXMTvUGH_-UeCK4HWegtm0mJcthoDtF_870ri8D_U5lhQxSgrUncEeYHez_KDKnuqIC0MN6EejehoERjdkEWUMp9mdDG8-5jH156_wtiGjgXxmo3Zz81f2OPs-9ZLFtYvZr8cEUOfcjQthoCP_DLcBVumVikdekRjfkS-sYpEUHKt3Um4ykjZTLvkEylFbM2-AilDdiRkH0CPcO04ERnn5RUs2qU4Nn9JTtYKgL68wDb5cAQTyx9WIOsmf0JLr0P33udj2EvDhJ3_2YVx91bCITmFEYUIPnjDz4iH7Q5umAKAsACTvD1f-pUTXf2_nA0fgC12FEBVQkPtsYeHzKDkb1_ddjqZ2Dlo36KCrlHz1bQLApvPwDrojRaOFyxZFYzt3-30LjSlsaHLIsNallUWMHyXseGW5yNqaw5nj1Ud2kTo2-TP7sQOqatHCXs5s9U8W2KZbxAi2GyvKvqyWX0-gULaGIUpAkgmYAl-AE-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما کنترل بسیار قوی‌ای بر تنگه هرمز داریم. هیچ‌کس فکر نمی‌کرد که این اتفاق بیفتد.
🔴
به طور متوسط، ما روزانه حدود 25 شناور را توقیف می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/147037" target="_blank">📅 14:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147036">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
گزارشگر: اگر بخواهید به مردم ایرلند که امروز در حال اعتراض هستند، چه بگویید؟ آن‌ها معترض هستند زیرا نمی‌خواهند شما به ایرلند بیایید.
🔴
ترامپ: من نمی‌دانستم که اعتراضی وجود دارد. من هیچ اعتراضی ندیده‌ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/147036" target="_blank">📅 14:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147035">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
چین ریاست سال ۲۰۲۷ بریکس را بر عهده می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/147035" target="_blank">📅 14:14 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147034">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ : حوثی‌ها «نمی‌خواهند با ما بجنگند» و افزود که آنها با آمریکا تماس گرفته و خواستار آن شده‌اند که واشنگتن در این درگیری مداخله نکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/147034" target="_blank">📅 14:07 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147033">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ترامپ: فکر می‌کنم ایران موشک‌هایی دارد که می‌تواند شهرهای اروپایی را هدف قرار دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147033" target="_blank">📅 14:06 · 21 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
