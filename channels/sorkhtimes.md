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
<img src="https://cdn4.telesco.pe/file/Nlow3DJBzAnCN2fYYYyGBrtG_6vKUm5RbQ7eY9v5zcUnJdcdma3s8i41u56CSKu4vemHr_rpM_k6H-hIICyMxuaaAj1cbq9kIBBlx8R_XtFPW4e5A6imieOFFJaau3Yx5ctFSYyOXlUDGL0_SPYZn5ArpD70Msd8VUzLfm3VgVQPGD9ZAWGEIapgdyopOAaf0WNFroJDjObQkgr7pYFtKxH1wMc2swZX0j2dspU8_ObKSqjhzP1-r5OJ4XT_3Kb5_TP-ZmanE2y0R9CocqmbfxE0j_myAeIijyGO9YQ1rJPoDQgr-nbVnGTMCrwdItFV_C-rtlrSBTKbC2Y2ECYZEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 03:25:16</div>
<hr>

<div class="tg-post" id="msg-134626">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">من عضو کانالشونم، تحلیل‌هاشون نسبت به بقیه واقعاً منطقی‌تره. پیشنهاد میکنم حداقل یه نگاه بندازین.»</div>
<div class="tg-footer">👁️ 1.44K · <a href="https://t.me/SorkhTimes/134626" target="_blank">📅 01:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134625">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksN5jmttbFhhahDcL1LhJ7MJs3wiU49NFfJLUzI2oLrbLHLp7uOh44iM_XVTMHftkNR024iOJ8XdkmH6eiQwzM36enqXXV0gJQe5OpEq6AmBUwuehhlXLa2fzldUcxY0JIf1LMjIdSBQFv56e1jqxzyzPfWjBAnxf8SK4lP_NkwJJ-gKMWJAzq6nD3j4SHIXS0ShKggEwNvSQU_ZmRV07sh_CiDgsq8Eq6b8wWQDGfl04gZXOJau7hPpUDuYbkJ4HYOq_H-HfvYUz1jUTd7w6CqE5WAbNXMl4AKF5bir-puW0kiBJFgXEXdAvMUJ5jJvSX3sC0DgDkF3A-7s0l9PJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
?
💡
کافیه یه کانال معتبر پیدا کنی که کارش تحلیل فوتبال باشه و دارای چند سال سابقه کاری باشه کانال پیشبینی تیپستر پرشین همونیه که دنبالشی چکش کن
👇
https://t.me/+LTqi6B-mG8kxMzU0
https://t.me/+LTqi6B-mG8kxMzU0</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/134625" target="_blank">📅 01:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134624">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فوووووری
گلر ملی‌پوش به پرسپولیس خواهد پیوست
⁉️
👀
تا دقایقی دیگر
⚪️</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/SorkhTimes/134624" target="_blank">📅 00:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134623">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
پایان نیمه اول | سامورایی ها در نیمه نخست برزیلی ها را شوکه کردند
‼️
🇧🇷
برزیل 0
😎
1ژاپن
🇯🇵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/134623" target="_blank">📅 00:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134622">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
فووووووووری از تسنیم
🔴
اسمار با دریافت 250 تا 300 هزار دلار از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/134622" target="_blank">📅 00:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134621">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🔴
فرهیختگان : باشگاه پرسپولیس بعد از برگزاری نشست‌های طولانی با ایجنت اوسمار ویرا در نهایت با او در مورد مسائل مالی به توافق رسید.
🔴
🔴
توجه به این قضیه باشگاه پرسپولیس فقط قرار شد طلب مربوط به قرارداد این فصل اوسمار را که حدود ۳۰۰ هزار دلار است را به وی بپردازد.…</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/134621" target="_blank">📅 23:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134620">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
استوری جدید فرشید حقیری : امید عالیشاه از پرسپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/134620" target="_blank">📅 23:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134619">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/134619" target="_blank">📅 23:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134618">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
کریم باقری: ما بد بازی کردیم و باختیم/ بازیکنان مقصر شکست هستند؟ در این یکی دوسال پرسپولیس شرایط خوبی نداشت آن هم به دلیل تغییرات زیاد است
❌
آمدن اسکوچیچ به پرسپولیس؟  تیم ما مربی داشت که بحث اسکوچیچ شد/ این موضوعات فقط حاشیه سازی  است
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/134618" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134617">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/134617" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134616">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fbbo1UQmFML_LDzgofY3tzcMilHRhAX8dDf0vTgaojU00J1d8iKdEsPIejMvDHmNNA8yhlLGwu5fkbZ83m0QCcgrdK2Q7fizh71vvzjOdPUmraAtv1NcYDu5NLVY0Glni80WhMVaT3bnB3oIttFkRfIndBbbjr_gRdnLh9WfXOAyVYI7bOFnV7FcCtH-N1vgq7KDtWMhwgmZU9qsaE0tnLwnVZRqh1JHjbEmV3Xl9Sz9TUQO9GES2-HOYgH-5KzLAhTjVw76_cigNR0sIW7cchB7oZcA63Xka0gabLFP6g5Xn4HGkTMvnMrHD2V6OJ_B4u21TBV3rm53oRxuWO3gyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
میکس VIP  از بازیهای جام جهانی
🏆
🇧🇷
برزیل
🆚
ژاپن
❤️
🇩🇪
آلمان
🆚
پاراگوئه
🇵🇾
باضریب
⬅️
4.08
📊
گذاشتم
اینجا
حتما استفاده کنید
💎
شروع فرم ساعت
🔢
🔢
⬇️
👇
⬇️
⚽️
برای دریافت کلیک کنید
🤩
🤩
🤩
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+Bt80HN28Ils5YWE0
◀️
https://t.me/+Bt80HN28Ils5YWE0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/SorkhTimes/134616" target="_blank">📅 22:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134615">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
ضربات پنالتی دیدار چادرملو و گل‌گهر (۲۲ ضربه)!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/134615" target="_blank">📅 22:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134614">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/134614" target="_blank">📅 22:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134613">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
پایان نیمه اول | سامورایی ها در نیمه نخست برزیلی ها را شوکه کردند
‼️
🇧🇷
برزیل 0
😎
1ژاپن
🇯🇵
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/134613" target="_blank">📅 22:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134612">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
نیمکت نشینی عالیشاه مقابل چادرملو فنی بود؟
🔻
🔻
گفته می شود نیمکت نشینی عالیشاه مقابل چادرملو ریشه در دخالت مدیران داشته است.
🔻
🔻
برخلاف اخبار منتشره امید عالیشاه، در لیست مازاد اوسمار ویرا نبوده و عدم حضورش در ترکیب اصلی و بازی گرفتن از او در دقیقه ۸۰ ، عجیب…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/134612" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134611">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
چادرملو اردکان با برتری مقابل گل‌گهر سیرجان در ضربات پنالتی، راهی لیگ قهرمانان 2 آسیا شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/134611" target="_blank">📅 22:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
خدا لعنت کنه بازیکنان بی غیرت مارو که حذف شدن وگرنه امشب قهرمانی سه جانبه ما بود و رفتن به سطح دو آسیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/134610" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
پایان 90 دقیقه بازی چادرملو 0 _ 0 گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/134609" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bw-6Yh7twmQn_nT7fJKH08hxJ7ZOJsMGKHOpaxjL4qRXoBFGh9vCbbpBzNGtqj4UjKkAhsGUC9rOoiVu8uSiMjz4AsR9ydHYI8n1qNuOw2GXS25mHn-XABB__7T_yNCU-xZnUMQBZhubIhXbeJ_Kb1jZ8i64VMtotCFjzUAyB-mfccL5x9l0sbLNxecjqMt24gQCg_Z3PtNA9gnECm7RL0-Pks6rPzw1LgDIk4II9FaqJD-pmhbKWNj5eE6CwzBcEdwrost519rIZJU7kBPDTI2N5o0gaqSsL1TUBXCYpL8S7HmqfPrt2orzbMR5QQ870ZsCHfGm6W95juSC5mGNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل قاسمی دومین گلزن و بهترین پاسور امیدهای کشور و ذوب‌آهن به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/134608" target="_blank">📅 21:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔖
🔖
تیم‌های چادرملو و گل‌گهر سیرجان امروز ساعت ۱۹ به مصاف یکدیگر می‌روند تا سهمیه سوم فوتبال ایران در لیگ آسیایی مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134607" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
پدر کسری طاهری: کسری فصل بعد پرسپولیسی ست و قرارداد داخلی امضا شده
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/134606" target="_blank">📅 21:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
آقای قلعه نوعی .یاد بگیر از ژاپن ...بدون اما و اگر صعود کرد و نیمه اولم از برزیل برده بازی و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/134605" target="_blank">📅 21:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/134604" target="_blank">📅 21:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134603">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/134603" target="_blank">📅 20:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134602">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
زیبا‌ترین گل‌های جام‌جهانی 2026 تا پایان مرحله گروهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134602" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134601">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
بازی های امروز و بامداد فردا جام جهانی
🇧🇷
برزیل - ژاپن
🇯🇵
20:30
🇩🇪
آلمان - پاراگوئه
🇵🇾
00:00
🇲🇦
مراکش - هلند
🇳🇱
04:30
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134601" target="_blank">📅 18:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134600">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🤩
🤩
🤩
گفته می‌شود مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کند تا طرفین برای جدایی به توافق برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134600" target="_blank">📅 18:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQhWoXUBvcBeSXK3Ab_g6tirFVpkYMSyvnco5NcMqJ-bynKGQSN_FKfAFoSJZR2JocZqeWxuE1ruwRqkzwolF83h--OZtBY5V2uJfOLWI63eAodK6rvdvtg-JD0c6f-dRrBEqe1Ys6wYM4IN6O84FaxkkkqP8lSSDqPZTYVscDQxcUIw24Ov6JkQSeLopnNXrfyjnnB_AyjshkzTDrQ3gNANAJHZRoICagkBExIhVxgvL1JR8lqsSVaTqXN_x8gJbzK8Lgdo_lAX5CuTybSvbrvQdBXkG0BWlZsr6fSX0ZUirsSuP3xn_nRaZz35pgNhByTZQzfcfiFXq7iVeajrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته فرهیختگان، باشگاه برنامه ای برای تمدید قرارداد علیرضا رفیعی نداره و این بازیکن بزودی از پرسپولیس جدا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/134598" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134597" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/134596" target="_blank">📅 16:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❗️
میلاد محمدی ظاهراً دوست داره برگرده یونان. از اون طرف، مدیران باشگاه هم خیلی تمایلی به تمدید ندارن و دنبال جذب رزاق‌پور هستن اما اسکوچیچ به سبک بازی محمدی علاقه دارد و شاید با توجه به پافشاری سرمربی مدیران باشگاه راه چاره‌ای جز مصالحه با میلاد نداشته…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134595" target="_blank">📅 15:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/134594" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
غیر رسمی: اسکوچیچ فردا بعنوان سرمربی پرسپولیس رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134593" target="_blank">📅 15:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE38-8kKVL9xZ4tXNGe7sIREcNqpkj4vSUQ9bOdC9ncpn5bNRr5koFToq-rEiEzmVVr9NE5fa28DHykH3wqTTxSkPSZgrwXmMwX6ac-VzXQODuJ1f-KWvBTCAHZN8wKCHJhAU6LiqptB66z0d-HF8l_Rq10w44KqiWp6WwXVrpkLlc3Zem1adbn0edNa6CyF_66XifaqhwKS3eesMAUgl5_w95fpu59OO7HtKfFvpqk3Ab6qQg-40qpYEO7JBJu40XMDjF0iqisFK6os4F3GniaNFADttp-MYE36P54lPL32SqOKQRHUXbZV7Z7UdrSvSOYmXxwlC8kqnid6_KBFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عینک مخصوص حذف از جام جهانی ۴۸ تیمه فقط ۱۳۴ هزار تومن :)))
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/134592" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134591" target="_blank">📅 15:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134589">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
تراکتور بعد از دانشگر و محمد مهدی محبی اینبار رضا غندی پور هم جذب کرد ..امیدوارم باشگاه برای جذب بازیکن دیر اقدام نکنه ...چون بازیکن خوب روی زمین نمی‌مونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/134589" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134588">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
🔴
محمد مهدی محبی با قراردادی ۳ ساله رفت ترتر و بعد از ممد دانشگر دومین خرید ترتره .
🔴
مدیران ما هم هنوز تو خواب زمستانی هستن .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134588" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134587">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
نیمکت نشینی عالیشاه مقابل چادرملو فنی بود؟
🔻
🔻
گفته می شود نیمکت نشینی عالیشاه مقابل چادرملو ریشه در دخالت مدیران داشته است.
🔻
🔻
برخلاف اخبار منتشره امید عالیشاه، در لیست مازاد اوسمار ویرا نبوده و عدم حضورش در ترکیب اصلی و بازی گرفتن از او در دقیقه ۸۰ ، عجیب…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/134587" target="_blank">📅 14:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134586">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134586" target="_blank">📅 14:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/134585" target="_blank">📅 13:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
با اعلام مسعود پزشکیان، 6 میلیارد دلار از دارایی های ایران در قطر آزاد و به ایران تحویل داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/134584" target="_blank">📅 13:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134583">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✅
✅
استقلال رسما با ارسال نامه ای به وکیل بیرانوند پیشنهاد دو ساله به ارزش ۲۰۰ میلیارد داد./ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134583" target="_blank">📅 13:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134582">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
🔴
🔴
چرخ گردون، گاهی با توپِ گل می‌چرخه، گاهی هم با پرچمِ آفسایدِ کمک‌داور!
🚨
همون حسی که اون روز به ما دادی، امروز با یه آفسایدِ شیرین برگشت پیش خودت دیدنش واقعاً تماشایی بود
🚨
اسمش کارماس شلیل زاده
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134582" target="_blank">📅 11:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134581">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHM_aIWtd3zdjaPwNOv1wnUhZ0SzWv_sObeFD6D00BvOsaSznyzjZoXrCi6s2uB7j3MMc5B7q8PjsaKoXNTCm3HAPHTn8AZZx5biPktzOYP0h-__FH1zFNnqI7bDufOuY9R1gZd0NXYwuuGViUFSqHkh2gZQD83ywTJMn8HsEJYiK0aI3XudOLYVOMnyL8VUNR2M1YZKDXsrk_TMba_fqSs_aIbdvBTa3oi5c2hAu0OfDnbz48lu3zpEUGukddsMqq499x74yIxkRhkaG-PT9emMCISLd9F9RZ7Jc_sjxeeJobSVLUfeVBqa-Qs57fJlVDnbL7_4Q4GZkEQlykXZ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🔴
چرخ گردون، گاهی با توپِ گل می‌چرخه، گاهی هم با پرچمِ آفسایدِ کمک‌داور!
🚨
همون حسی که اون روز به ما دادی، امروز با یه آفسایدِ شیرین برگشت پیش خودت دیدنش واقعاً تماشایی بود
🚨
اسمش کارماس شلیل زاده
🙂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/134581" target="_blank">📅 11:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134580">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/134580" target="_blank">📅 11:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134579">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
🔺
اعلام زمان مسابقه دوم پلی آف آسیا
🔸
مسابقه دو تیم چادرملو اردکان – گل گهرسیرجان  ساعت ۱۹ روز دوشنبه ۸ تیر ساعت ۱۹ در ورزشگاه پاس تهران  و بدون حضور تماشاگر آغاز می شود.
🔸
برنده این مسابقه به عنوان نماینده فوتبال کشورمان در لیگ قهرمانان سطح دو آسیا به کنفدراسیون…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134579" target="_blank">📅 11:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134578">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134578" target="_blank">📅 11:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134577">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
عراقچی: موضوع هسته‌ای، رفع تحریم‌ها، بازسازی و پول‌های بلوکه شده در یادداشت تفاهم آمده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134577" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134576">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
🔴
قرارداد اوسمار دیشب با پرسپولیس فسخ شد و این سرمربی برزیلی از پرسپولیس جدا شد.
✅
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134576" target="_blank">📅 11:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134575">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134575" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134574">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d0b066411.mp4?token=nkgbZqEAjahiwxUXOLJAVOH3m0M6PDVS-n__S5okhNhopAc0RqMroolLsO0SEOI7tA9ciy8ev9TO9-jrmLcXXuiFA40Hn16XSol52WpLLpVxbYELiB6NdKrOzFArR0leceJckECmJweWy4W7aR-WiZiEtGYEyRnindE3NUsMJ5Sq9ov1BfB_Yc37Krv2EZ-UakFQDGYstlayA2Vbtx1c-uSHZQJOtYfb9CWHPVvGnaOiaS4k6cvO57SOBe_gXjh4R-PUK7pMF-FBNcMAEAC1AC1Z1TfEe4XuJwPtpzSICetgZQVThFiqWquUFHpsDKWILJ20_FAOxvpUNJFjl7h1Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d0b066411.mp4?token=nkgbZqEAjahiwxUXOLJAVOH3m0M6PDVS-n__S5okhNhopAc0RqMroolLsO0SEOI7tA9ciy8ev9TO9-jrmLcXXuiFA40Hn16XSol52WpLLpVxbYELiB6NdKrOzFArR0leceJckECmJweWy4W7aR-WiZiEtGYEyRnindE3NUsMJ5Sq9ov1BfB_Yc37Krv2EZ-UakFQDGYstlayA2Vbtx1c-uSHZQJOtYfb9CWHPVvGnaOiaS4k6cvO57SOBe_gXjh4R-PUK7pMF-FBNcMAEAC1AC1Z1TfEe4XuJwPtpzSICetgZQVThFiqWquUFHpsDKWILJ20_FAOxvpUNJFjl7h1Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خیابانی در مورد اسکوچیچ
✅
رنگ رخساره خبر می‌دهد از سر درون؛ فدراسیون فوتبال ایران یک عذرخواهی به تو بدهکار است.
🔴
وقتی فساد هست وضعیت همین است، نباید اون اتفاقات قبل از جام جهانی 2022 میفتاد‌، به بازیکن چه سرمربی عوض کند، هیچ ایرانی نپذیرفت آن زمان سرمربی ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134574" target="_blank">📅 08:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134573">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134573" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134572">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✅
✅
امیر قلعه نویی بعد از تساوی ایران و مصر:
🔴
🔴
شاید خدا هم با ما سر ناسازگاری دارد. با یک موقعیت گل نزدیم. می گویند گل ما هم با 5 سانت آفساید گرفته شد. تیم مصر تیم بسیار بزرگی است ولی عدالت فوتبال با همه مشکلات ما رعایت نشد. شاید این آزمایش خداوند از من است…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134572" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134571">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga_ql2GKWKcJIXUP_kRXtHrdXVNy0J2jhZ2uQXKqN83CiGMqV2iE6bcNfpSXJP4mp2F9WqI_pmFa7kdZXd2pkOG93stNPpJ-luPmaB2m7H-5BKzeFF3NpqIUL2D5L0y8WGtDm3fPO2fOStD4XXwySe6iyFSPWngUSi3CK9hImhVaw_Um-m236IEQj8cNbMv9LNXnG8kBW7IxYC_gylcO86gBanK7_9VCAEdc4BXJDCj-XPMdEXeRMhytdH6LxJkUYZ3YOzY-URZhAfFNRKt_4tnKhmAc9-EXluRwx63nrN2L-5--KSXEYFyGubpbF5HwMEVPfz5ueyYqi17-VUd3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت رو از دست نده، همین الان وارد سایت شو و گردونه رو بچرخون!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134571" target="_blank">📅 01:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134569">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">#فوری
⁉️
👎
خبر منتشر شده مبنی بر مذاکره حسین خبیری با بانک شهر کذب است،و نقل قول منتسب به خبیری صحت نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/134569" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134568">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: مدیران باشگاه قرارداد رو برای اسکوچیچ ارسال کردن…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/134568" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134567">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
حدادی  : خداداد عزیزی و خلیلی گزینه های سرپرستی تیمن  / هیچ فشاری از بانک شهر برای اومدن خداداد نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134567" target="_blank">📅 00:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134566">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
🏆
برنامه کامل بازی‌های ۱/۱۶ نهایی جام جهانی
🇿🇦
آفریقا جنوبی - کانادا
🇨🇦
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
🇺🇸
آمریکا - بوسنی
🇧🇦
🇳🇴
نروژ - ساحل عاج
🇮🇪
🇫🇷
فرانسه - سوئد
🇸🇪
🇩🇪
آلمان - پاراگوئه
🇵🇾
🇲🇽
مکزیک - اکوادور
🇪🇨
🇧🇪
بلژیک - سنگال
🇸🇳
🇪🇸
اسپانیا - اتریش…</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/134566" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134565">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
پنجره کیسه بسته است بابت بدهی خارجی .ولی اونوقت مجوز حرفه ای گرفتن.عجب داره واقعا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/134565" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134564">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/134564" target="_blank">📅 23:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134563">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❗️
دانشخر به سوراختور پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/134563" target="_blank">📅 23:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134562">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iuB5eA7ox4_fSRmNIEHZ_HGi4pzOK_cRd7PIzwDRlOn9dMmPLNVfjd9niDToVS-D27DB_jCKGMwg9vN3guSs2Kwiv5eWEdY3djKxO34CWV3jWStveigzo5r53TVEZ6iXwP_xc5wYS7BCqFaXRqBgfFs8n1m40UALac7nVoCJHuWAfLfU5ByvfEy-lIZJCmlomBvN-5ZIaVbefmIqSevlrmR-_Hhyq2lc0Rm2Vm1iqYlzb7wfthy5_nb7x-4UPYN4TaZLzD4IfVDspDeobCFpN6iuA-pysY4SXCFBsVcB3LCdZ7cemEA6zNRBEwkzc2OybD3tzvU4CcPL-KIrh1UZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
فقط ۴۰ روز تا آغاز لیگ برتر خلیج‌فارس باقی مانده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134562" target="_blank">📅 23:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134561">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59577ce95d.mp4?token=f31WkpG9QSpheSn7S8_BvGF7V7mfp6ikAxW_iltBG0ca_pacuCBU51-q4gY2kaEuEBPysOQozwCZk1xpBxU7BVz9F6f21sI_ZV61Zk1S6qqzBSIek2CTW-O3ARQ4KkoPcq8EyIyZovJggNE2IM6lP_l3R5EDmbVSDQgVROZrdBij4UTNVY_u0Z3FKNzvhEjEUz_wc75FYRo9rsN3gzfHMfioPr9BqTS7eW669iSKLvAS_hiNLlFLSrnvACutkvy3bS0oe1aDdpXegnWnKv3E_iEeOqGku4XW7be_ucwxqq_3Z7-YeRyrFaH5Qzx88OGIDsPxB5am5RyIFQn6sRKHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59577ce95d.mp4?token=f31WkpG9QSpheSn7S8_BvGF7V7mfp6ikAxW_iltBG0ca_pacuCBU51-q4gY2kaEuEBPysOQozwCZk1xpBxU7BVz9F6f21sI_ZV61Zk1S6qqzBSIek2CTW-O3ARQ4KkoPcq8EyIyZovJggNE2IM6lP_l3R5EDmbVSDQgVROZrdBij4UTNVY_u0Z3FKNzvhEjEUz_wc75FYRo9rsN3gzfHMfioPr9BqTS7eW669iSKLvAS_hiNLlFLSrnvACutkvy3bS0oe1aDdpXegnWnKv3E_iEeOqGku4XW7be_ucwxqq_3Z7-YeRyrFaH5Qzx88OGIDsPxB5am5RyIFQn6sRKHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی: اونور یک دقیقه ای بازیکن اتریش اومد گل زد، چطوریه که طارمی سه بازی گل نزد؟ طارمی خیلی پولدارم هست و مقصر صعود نکردن ایران هم خودشه باید پول بلیت برگشت کادر و بازیکنان رو بده
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/134561" target="_blank">📅 22:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134560">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
عادل فردوسی پور: مدیران‌تیم پرسپولیس باخودِ مهدی لیموچی برای قرارداد به توافق شخصی رسیده‌اند و درصورت توافق با مدیران سپاهان این انتقال انجام میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/134560" target="_blank">📅 22:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134559">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/134559" target="_blank">📅 22:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134558">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده اوسمار رو پرداخت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/SorkhTimes/134558" target="_blank">📅 22:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134555">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/134555" target="_blank">📅 22:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134554">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXCrjfL1mBym7q9Am5uXK-YrFdNhsO3gZM7KhN6x8vCxdEWWUfeVr851mKwP7cUj90C8LOYjpX_0YRhuDM9A2t_7a2xPsZvmZH-x1e3Hsoswd5HodYTt281RnobvlMLXCVypqnGkjyi9xT40Wv-3CDFZfQh7IlHLjzta_Epc11egyOXo0RvR5dai2doRl8OB9aW0vPlV_Rq_aLuEU_GrZCJAYntAlS8fCht3u4UqTUO9Fa2CIhGwrwHYM2RgoyIrsxEyeRXI3nqoKue82-AXbGmCIojiQOKCaqMuIfmuaJ5xBHRj7ISM6ymsxIK1VLwE3aRWkm6-GGxYspcA5a2iqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
مرحله یک‌شانزدهم نهایی رقابت‌های جام‌جهانی
6⃣
2⃣
0⃣
2⃣
از راه رسید!
🔵
اوج هیجان فقط با وینکوبت،
دیدار جذاب امشب کانادا
🔴
-
🟡
آفریقای‌جنوبی رو با
🔣
0⃣
1⃣
بونوس اولین واریز پیش‌بینی کنید!
🔴
جام جهانی ۲۰۲۶ رو با وینکوبت پیش‌بینی کن و ۱۰ درصد بونوس اولین واریز بگیر.
🟢
چرخش رایگان گردونه، شانس روزانه تا سقف ۱ میلیون تومان.
🔗
برای پیش‌بینی بازی‌های جام‌جهانی با بیشترین آپشن ممکن همین حالا وارد ربات مینی‌اپ وینکوبت بشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🔗
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/134554" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134553">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❗️
❗️
اسکوچیچ خواهان جذب دروژدک مهاجم اسبق خود در تراکتورسازی، برای پرسپولیس شد.
🎙
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/134553" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134552">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فرشید حقیری :
⛔️
اسکوچیچ سرمربی پرسپولیس شد تمام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/134552" target="_blank">📅 20:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134551">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
سفیر آمریکا در سازمان ملل: صبر ترامپ نسبت به ایران در حال تمام شدن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/134551" target="_blank">📅 20:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134550">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
عضو کمیسیون امنیت ملی مجلس:
✅
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/134550" target="_blank">📅 19:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134549">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها: پاتریس کارترون گزینه پرسپولیس در صورت عدم توافق نهایی با اسکوچیچ!!!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/134549" target="_blank">📅 18:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134548">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Debl0xvSDv_ChJmx4XQW0VrY1M4uUW19eGMDCJUTr2N4j41feIWsoc0GCKj9njITKiUAsp_giIRPlShU8JJdBr42XdtyIPu9wrv0Cr8awGOCFxrFd8UT8jVHkUg9GDRra6qTYlj5_ab6uTSM9UxJDn8kVOM7rrXmj72hYcUycBmJRcoebh9pxeZ7exXVY5oruzVGOlRDKTa8P3XhrJjyL3pyZuCJMiXwIULD9t2xZVf2YZ3ODgJ5EorPr-8a39vrZ-PnOZRa0dufbR1S3jbMxbQ_WMI-B7tUTTS3vDZfPE9g9U11Qs57ABKhLxaKervNLlL1faKnwbAzqZviyS7wfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
نتایج تیم ملی والیبال ایران در هفته دوم لیگ ملت‌های والیبال ۲۰۲۶
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/134548" target="_blank">📅 18:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134547">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134547" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134546">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf61xJOxcv5LrQn3UDjqSLceXM_Hh1CTsRcuFcClYWMl3AricRCG89O6Dd05f_vw_IvPK17JPc6WhhFf9yuBvx3D5Up64QwNnGGxHR3yILY-ryubv4XPCE2z7279pTw1yDb5K0P_8uDnxQQqhVVRRCqbLIU8-yfCuJCr57vZDqcvzBQaYkm9zzusPB-KTzhDqBx_iycG0P6YbZT8gRHGqL02ATsUCZMSEj_kgwkvhSvBHZJ3QUN62Wl-gilAHHZtHCkf8_EvxMEB0u5kcbHSh3BqTU3kLylQ1YeBg5xiikXEM_Iko3_Y8zB5VJ0dWp5tcITxEQGuODUe8byLReCCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فوری از قدوسی: علاوه بر اسکوچیچ، باشگاه پرسپولیس در حال مذاکره با یک سرمربی نام آشنای دیگر نیز می باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/134546" target="_blank">📅 18:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134544">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
قدوسی: اوسمار ویه را از سال گذشته 400 هزار دلار طلب داره و تنها در صورت دریافت طلبش فسخ می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134544" target="_blank">📅 18:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134543">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134543" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134542">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMobin</strong></div>
<div class="tg-text">این خبرها همه سفارشی از عالیشاه باندشه که حدادی کله پا کنند ح رومزاده ها فکر کردند این باشگاه ماله باباشونه که بخوان تا زمان فسیل شدنشون تو اینجا باشند واسه این همه هوادار تصمیم گیری کنند</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134542" target="_blank">📅 18:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134541">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
قرار است امروز (یکشنبه) جلسه هیئت‌مدیره انجام شود که دور از انتظار نیست خروجی این جلسه، برکناری اوسمار، انتخاب اسکوچیچ و البته پذیرش استعفای حدادی با انتخاب سرپرست مدیرعامل جدید باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/134541" target="_blank">📅 17:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134540">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
#مهم | لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134540" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134539">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
#فوری
🚨
هیات مدیره پرسپولیس برای فردا صبح جلسه فوق العاده گذاشته و درباره آینده پرسپولیس تصمیم گیری خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/134539" target="_blank">📅 17:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134538">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
به گزارش خبرنگار قرمزآنلاین، طبق اخباری که قبلاً منتشر کردیم، باشگاه پرسپولیس و دراگان اسکوچیچ بر سر دو موضوع با هم اختلاف نظر داشتند که یکی مدت قرارداد بود و دیگری درج بند فسخ در قرارداد در صورت تکرار جنگ که اکنون خبر می رسد دو طرف، توافق کرده اند مدت قرارداد…</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134538" target="_blank">📅 17:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
دیدید حالا نمیشه
✌🏻
🔴
تا وقتی به مردمت پشت کنی و دل مردمت باهات صاف نباشه احتمال ۹۲ درصدی صعودت هم به صفر تبدیل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134537" target="_blank">📅 17:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134536">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134536" target="_blank">📅 15:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134535">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🏐
برنامه کامل مسابقات تیم ملی والیبال ایران در هفته دوم لیگ‌ ملت‌های‌ جهان؛
❌
از فردا شب شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/134535" target="_blank">📅 15:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134534">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/134534" target="_blank">📅 15:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134533">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
تمرینات پرسپولیس به مدت شش روز تعطیل شد و قرار است از شنبه هفته آینده تمرینات پرسپولیس برای فصل جدید در تهران آغاز شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134533" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⚡️
2- آلویس نانگ (Aloys Nong)
⚡️
آلویس نانگ نامی آشنا برای فوتبال‌دوستان ایرانی است زیرا عملکرد خوبی را در لیگ برتر ایران با تیم‌های فولاد خوزستان، نفت تهران، تراکتور، استقلال خوزستان، پارس جنوبی جم و سایپای تهران داشت. او که با سابقه بازی در باشگاه‌هایی مثل…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/134532" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚡️
⚡️
- سانل کونیویچ (Sanel Konjevic)
⚡️
این مربی اهل اسلوونی دارای مدرک یوفا پرولایسنس بوده و در زمان بازی، حضور در تیم‌های اسووبودا و اینتربلاک از اسلوونی و فرلاخ و استراسبورگ از اتریش را تجربه کرده است. او به عنوان سرمربی در باشگاه‌های اینتربلاک، برینیه و…</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/134531" target="_blank">📅 14:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134530">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❗️
آشنایی با کادر احتمالی اسکوچیچ در پرسپولیس؛ از مهاجم و مربی سابق تراکتور تا دروازه‌بان سابق دینامو زاگرب
👇
👇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/134530" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134529">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
سایت اسپورت نت کرواسی مدعی شد؛اسکوچیچ و سه مربی از کرواسی، اسلوونی و کامرون در پرسپولیس
🔴
- آلویس نانگ بازیکن سابق فولاد و تراکتور
🔴
- سانل کونیویچ دستیار سابقش در تراکتور
🔴
- ماریو یوزیچ مربی دروازه‌بانان سابق رییکا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/134529" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134528">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZMUOt3oD5TQURccLAOWFiR9r2jsWU1tLzrAGRmDzNPOsaNvxX-jUf3Chli44ib7fVGAwUT4S0FDjQAwjfQD8cApg21uLkzQ_vfKmDnIUIiYdwFBs-DxTYTd4PPrfVuA2C-uBH-AVfWlXJe3vV3vuiaH_fWaBiQTID6HGaKkRHKXSgZqtainNmAz3B_-WRAnGyhQgB4N-aajlRPrjQky4J70QKYB9tPWNx7Gp4kMDI3nNxCB30xceCom6CxIRQwAn-dN9qpa-TYCZMNl7U9lQnvsnZp1e0rBCNHlPIeR36bWKFDisqGMlRrfTSCeYjTtKaJoG9U36G7eGE1bqe1YBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویری پربازدید از اقامه نماز در رختکن تیم ملی فرانسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134528" target="_blank">📅 14:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134527">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
اخباری: گل لحظه آخر را بازیکنی زد که تازه داماد شده و دیشب به تیم اضافه شد. او گفته بود روی من حساب نکنید ولی گفتم کنارمان باشد تا روحیه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/134527" target="_blank">📅 14:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134526">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/134526" target="_blank">📅 14:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134525">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM7oUfohUHBqe0HVGaLjvOPArXtU3tP5osseBrAsHZFVqcKvbNN8O4U58JyDDHYiulLCrjXu91egsC01rs8zFpqhMxFIc68ZY2Yx8xy5_8i7ANp9HTbGwNHB1l0m1kD6d-OOsVSMEtt9SFR0KAUpjy1cRf7NFItXlRzggw-b72MPe29IvYnEy2Oy6Shsjv2qTel1OKJGoG0SJ4yKhTI0Vmcqmai5mV7RAlTTXcMCb-UjmxjdUtXuFvN-Q0_Rgu39TR6jjjGQHl20Uv8r9ZCE4RrtZDYqX7VUwaXpdf-N0ZRvKrkHf4OJOIr9Zl433pbaYSEsq2zPjvvsmLQXmiMD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/134525" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134524">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
⚡️
تیوی بیفوما و دنیل گرا برای فسخ قرارداد به باشگاه دعوت شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/134524" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134523">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d69fbc8a47.mp4?token=jHHG-CWErB-UkI2XVvRj9Aqg3m7DXht2eScNvkwzWBKWHoiZ4D9Tk3nRGEJhmGLkecsFN0f-1gdcs3yVqlIkeGCCdf3qC7YnoS-lZ6PboGRf-YxaoHfEpHbGimiXQouYTg_u58UPi8j1X6_lUM4Oi64Dsdaiy7AaZw-i557f_sOJgpwLERyVvC6WYNer9cqqwiEdFQTMoEF-ABOAOq54RkBoZwTTQVbt0L3UgdYs8uEbT7lFIn7uvn-W3GCIZXbhAc8N9MG3CtxY6e9q5V0YKZ62y3vf9TH5KyFl7wH7IscLGNfGHYMQzgHjOENzpkhpakOCWycJYz0xhkF3VoVW7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d69fbc8a47.mp4?token=jHHG-CWErB-UkI2XVvRj9Aqg3m7DXht2eScNvkwzWBKWHoiZ4D9Tk3nRGEJhmGLkecsFN0f-1gdcs3yVqlIkeGCCdf3qC7YnoS-lZ6PboGRf-YxaoHfEpHbGimiXQouYTg_u58UPi8j1X6_lUM4Oi64Dsdaiy7AaZw-i557f_sOJgpwLERyVvC6WYNer9cqqwiEdFQTMoEF-ABOAOq54RkBoZwTTQVbt0L3UgdYs8uEbT7lFIn7uvn-W3GCIZXbhAc8N9MG3CtxY6e9q5V0YKZ62y3vf9TH5KyFl7wH7IscLGNfGHYMQzgHjOENzpkhpakOCWycJYz0xhkF3VoVW7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مصاحبه قلعه نویی بعد حذف از جام جهانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/134523" target="_blank">📅 13:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134522">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTwHSCKG2TOD5_YtP_ZlOix8ayeD7TTdlH5LxHvyMPhLQztXzDf1kESHQFfD7ihh7emYfyiUyOzIj57glhOFiXRwHs-JVCv0dVqriomrxtkKYfqVd16tvhp2MPjgKu38ey7U6qTfR58YsJkEVgCZLdIU85zOAr_Ne82Jl5Df2LjaI11wUxVqp0m4AJA3R36nhIbrPTmpXLmBMCBxe_Qxc4nwn0j6yGSGkUA72Wq3RTDNy_AYx0q4HK3sbz9IN7qOORb6ckTnJ2lQdu3jnmlSPmhJk0JWPo5mMN7-UR1f39nqMthiZqrVm1_bhRsHEU6Q7WqDbNRKLerkfKsi50huCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
یک‌شانزدهم نهایی جام‌جهانی ۲۰۲۶
[
آفریقای‌جنوبی
🇿🇦
🆚
🇨🇦
کانادا
]
⏰
یکشنبه ساعت ۲۲:۳
۰
🏟
استادیوم
سوفای
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134522" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134521">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
قرارداد گولسیانی با سپاهان 700 هزار دلار بوده و او برای فسخ قرارداد، کل این پول را خواسته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/134521" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
