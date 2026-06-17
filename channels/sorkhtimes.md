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
<img src="https://cdn4.telesco.pe/file/Bi6SIu6nPB16H2vm_GTZT6hUZReecImamRTslMnGpQAFZFBmGbneHaaL4ePfqUKG6wWMSzFCnFOxjaPssqcwnWFuRRkm0G4VF6_ZrC5j7hOjU0xtxHqgfa9SMIKXE42JsF0ojDjeJOzl-AfOOJNZCQFMenCRYGpWK9ikiZcuCsaMT2rFcVYWBrQ28caRLqsgRULZdF-Ra3kMfOh0kQ1uQ7fpAWbZ8E0-AX8vwEeVY2pIdF_XEy2Nl55UYG9iuTs_2zD_ZWcSFa2p63dQhYHDAzq7A0SmrufpSHqZcihCt0mN5wRokAiOeHTqI1e7gzs4tE2xkdgVf6uWhTXQMIJE0Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 23:05:04</div>
<hr>

<div class="tg-post" id="msg-133764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن…</div>
<div class="tg-footer">👁️ 882 · <a href="https://t.me/SorkhTimes/133764" target="_blank">📅 22:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن…</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/133763" target="_blank">📅 22:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
دوستان به شایعاتی که توسط قدوسی در رابطه با اوسمار منتشر میشه توجهی نکنید،این عزیز دوست گرمابه گلستان ایجنت اوسمار هستن و تمامی مطالب شون خط دهی شدست تو هوادار رو به جون هم بندازن
🔻
اوسمار از ابتدا قراردادش ۱+۱ بوده و چیز تازه ای نیست اقایون احساس خطر کردن که نون دونی شون و دلالی هاشون به خطر بیوفته دارن یارکشی میکنن تا به هر ضرب زوری مربی که قراردادش بوده سال اول تو پرسپولیس ۲۰۰-۲۵۰ هزار دلار رو الان با ۱.۷ میلیون دلار حفظ بکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/SorkhTimes/133761" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwrfs4Nt-YVCc6C4cQhgNhpjnhoGogLqRoWYhHoyCkJPFnyxoRvf_qOuQxUBzAwJenEgDZFHLblWFmKvkmasdpblg0c1CHYZXq5C0c3yHe7naGYTZezxUWCOify3kGdqO-T8BEcvkRiLsifTVC3rYDw4twKa68GRRZOFNwobFHIKOs2Tylnl84DAZ-ZT_U6Zg7vD2lqAyItXbdkDh2pfGRNv1bILAUPoAeF1QY4dbLPyiEW1qkaSNjHYSian-tTMUuWeq3I0JM6amTyGW3sRSyqlKPgCrQpTK_yrEWyk-y3Vk1sVuzTvFHbDIbsiwnOW_TkEYQQqYQg7y5AWlnMNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شبکه خبر| انتشار متن تفاهم‌نامه ایران و آمریکا تا دقایقی دیگر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/SorkhTimes/133760" target="_blank">📅 22:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
😂
اولین گل تاریخ تیم ملی کنگو تو جام جهانی زده شد به پرتغال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/SorkhTimes/133759" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133757">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SorkhTimes/133757" target="_blank">📅 22:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133756">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🟨
پرسپولیس با چنتا از جوونای تاپ فوتبال ایران مذاکرات مثبتی داشته/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/SorkhTimes/133756" target="_blank">📅 22:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133755">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✅
ترامپ:
🔸
این یک یادداشت تفاهم است. اگر در ۶۰ روز انجام نشود، اشکالی ندارد، ما دوباره به بمباران بازمی‌گردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SorkhTimes/133755" target="_blank">📅 22:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133754">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/133754" target="_blank">📅 22:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133753">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
❌
گفته می شود په په لوسادا مربی اسپانیایی پرسپولیس اعلام کرده خانواده اش تا زمانی که جنگ در ایران تموم نشه اجازه نمیدن به ایران بیاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/SorkhTimes/133753" target="_blank">📅 21:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133752">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
بررسی داده‌های سامانه‌های پایش اینترنت از جمله رادار کلودفلر، نت بلاکس و رادار ابرآروان، نشان می‌دهد که اینترنت ایران در حال حاضر در وضعیت پایدار قرار دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/133752" target="_blank">📅 21:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133751">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
کریس رونالدو کاپیتان 41 ساله پرتغال : من میتوانم چهار سال‌ دیگر بازی کنم و در جام جهانی 2030 نیز حضور داشته‌ باشم. حالا حالا ها برنامه ای برای خداحافظی از دنیای فوتبال ندارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/133751" target="_blank">📅 21:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133750">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔸
🔸
🔸
🔸
ایران ورزشی طی یه خبری مدعی که شد مهدی ترابی و مهدی هاشم نژاد در استانه پیوستن به پرسپولیس قرار دارن
☝️
☝️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/133750" target="_blank">📅 21:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133749">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🟨
🟨
فوووووووووری
⬛️
اوسمار ویه را به زودی از پرسپولیس شکایت خواهد کرد/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/133749" target="_blank">📅 21:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133748">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: اسکوچیچ‌ ترکیه ست و به‌ زودی با امضا قرارداد میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/133748" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133747">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔻
🔻
🔻
فرشید حقیری :
⬜️
⬜️
بانک شهر تصمیم گرفته برای فصل بعد یه تیم قوی ببندد و امیدوارم در حد حرف نباشه. پیش قرارداد برای اسکوچیچ ارسال شده و تا شنبه نهایی میشه. خیلی ها از این موضوع ترسیدن که نتونن به پرسپولیس بیان یا نتونن تو تیم بمونن.
🔴
🔴
اوسمار برای فصل بعد…</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133747" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133746">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
فوووووووووووری
🔴
فرشید حقیری: قرارداد اسکوچیچ با بانک شهر شنبه امضا خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133746" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133745">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووووووووری
🔴
فرشید حقیری: پیش قرارداد برای اسکوچیچ فرستاده شده و به زودی امضا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/133745" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133744">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
❌
فرشید حقیری : بانک شهر تمام سهام سایپا رو خرید، از کارخونه بگیر تا تیم فوتبالش
✅
احتمالا با توجه به این موضوع پرسپولیس ب که سال بعد قراره تو لیگ یک شرکت کنه، جایگزین سایپا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SorkhTimes/133744" target="_blank">📅 21:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133743">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFtmegdvQCKEiFvRnyoAKnylLHCBRWT96xH8IzALublk4fCarizzXObHswVjR6K8cOR2StjMO8GR5TB3KydxYEkqJYh2X_HghT_Wkf_ObxjE1TE62-VsM-WfOCkYglvRUAUizQXPz0KtKH8rHzXoSIIzfl1DDf2km2XtTMghQwNtFedirWL-dWcgUbN4TxvcPD9O1vA8Aw3csYaGgo8a5pffZCXfSlQ9xOiDJ_0BvS6tHkLRIaR3XSjITP7FL-cpEqNUa7oHy9n1SvrYeg_FAKWlFJ-QeRnw1hp_HFqMQL2kDIcs4igQIn82m3_i_OTHIJ17ykTIdup6MmRQGG03fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🌍
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
🏆
گروه L جام‌جهانی ۲۰۲۶
[
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🆚
🇭🇷
کرواسی
]
⏰
چهارشنبه ساعت ۲۳:۳۰
🏟
استادیوم
دالاس
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
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/SorkhTimes/133743" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133742">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❗️
ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/SorkhTimes/133742" target="_blank">📅 20:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133741">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
#فوری | ترامپ:
🔻
توافق با ایران فردا یا پس فردا امضا می شود‌‌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/133741" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133740">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U3RIzRh8IvkmyTxribkzF8S1M1vsugegozsUWksEd17ZV_FFSEtoNQy1BzC-r37PW6yWok5HzYfMEGxrS9GiDpsMA6jTXagKFyONr19F5JdHgoCgkjDMRk7yWlGeVDbgxua1Ld4ntdZQuJFTrdM4-nHWZj9_mSaw0wnEAGzWhNta4B7tzwlv-JvRtMt5h0LfPVtO-OG-UqVyKbxt166okMo7kr0KHYM4y4pTZHoudcD99-Kiuq__-Yusn6NPYoXFDkuhURzJDZu0Jg-AoQ3Z3ZAcYvPk_Def5S-j3b4QfoazBIFltHef1_YlS5YJY8j23M4b8MYyOsm11GOBKjVNbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخلاف ادعای مدیرعامل گل گهر، انتقال مهدی تیکدری به پرسپولیس نهایی و قطعی شده است.
✅
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/133740" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133739">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇺🇸
ترامپ :
🔴
رهبرهای جدید ایران آدم‌های باهوشین، خیلی هم باهوشن؛
🔴
به اندازه قبلی‌ها تندرو و افراطی نیستن، فکر می‌کنم واقعاً کشورشون رو دوست دارن و آدم‌های خوبی هستن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/SorkhTimes/133739" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133738">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇺🇸
ترامپ: متن تفاهم‌نامه را نه تنها منتشر می‌کنم، بلکه احتمالاً یک نشست خبری برگزار می‌کنم و آن را کلمه‌به‌کلمه می‌خوانم تا رسانه‌ها آن را به‌درستی پوشش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/133738" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133737">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
قرارداد تیکدری بزودی امضا میشه/آنا   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/133737" target="_blank">📅 19:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133736">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
پیروز قربانی: من نیوزلند رو با فجر سپاسی شیراز می‌بردم مطمئن باشید نیوزلند اگه تو لیگ 16 تیمی ما بود، جزو چهار تیم آخر میشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/133736" target="_blank">📅 18:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133735">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❗️
نیوزیلند از دستمون فرار کرد و خوشحاله یک امتیاز و گرفته .چون واقعا زورش به ما نرسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133735" target="_blank">📅 18:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133734">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
❗️
خبرگزاری فارس هم اعلام کرد:
🔴
مهدی تیکدری پرسپولیسی شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/133734" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133733">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133733" target="_blank">📅 16:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133732">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
❗️
خبرگزاری فارس هم اعلام کرد:
🔴
مهدی تیکدری پرسپولیسی شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133732" target="_blank">📅 16:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133731">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🚨
‼️
مهدی لیموچی به پرسپولیس پیوست/ خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133731" target="_blank">📅 16:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133730">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❗️
❗️
با چهار بازی امشب و بامداد فردا دور اول بازی های تمام میشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133730" target="_blank">📅 16:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133729">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/133729" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133728">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
دنیل گرا: در ایران احساس امنیت می‌کنم
🌟
شب جنگ جولیانو (مربی بدنساز پرسپولیس) به هتل محل اقامت من آمد و گفت که پرسپولیس قرار است فردا اعضای خارجی تیم را با اتوبوس به مرز ترکیه ببرد. روز بعد ما 15 ساعت در راه بودیم و پس از رسیدن به ترکیه از آنجا با هواپیما…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/133728" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133727">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe69dca3f5.mp4?token=V2puGI60wd3kF2xD3frUJ0-HWeBo0PbapEmLvo5meDgi9y4LpogZR7lB9xArH0fJSvEyFTJ0e4caNdJl3Lkb2H4a7OaLzYB1xbOHfxiyxtQPM0QHnDGUee3pM8-65L0Lwv8mRBnmGtqk-GzKR4EtIekQ3ypxYHjhUEgJhH73ZXtZuqDp6gHSx41mD3XeW7uj7kTskthWk103sVTl5CPHhVYTSlpLqbg7KEEQjaUaUV9l3hO2xGts61svrgk1mVyjhTPk_EI36dk3OeRcgfo-6YfGVy78IJIkpFNNF4p21TbxP-5LbNQK75Jg4VnE5jJZaBI4pJt8LO8Nchq2RnikOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe69dca3f5.mp4?token=V2puGI60wd3kF2xD3frUJ0-HWeBo0PbapEmLvo5meDgi9y4LpogZR7lB9xArH0fJSvEyFTJ0e4caNdJl3Lkb2H4a7OaLzYB1xbOHfxiyxtQPM0QHnDGUee3pM8-65L0Lwv8mRBnmGtqk-GzKR4EtIekQ3ypxYHjhUEgJhH73ZXtZuqDp6gHSx41mD3XeW7uj7kTskthWk103sVTl5CPHhVYTSlpLqbg7KEEQjaUaUV9l3hO2xGts61svrgk1mVyjhTPk_EI36dk3OeRcgfo-6YfGVy78IJIkpFNNF4p21TbxP-5LbNQK75Jg4VnE5jJZaBI4pJt8LO8Nchq2RnikOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دنیل گرا: در ایران احساس امنیت می‌کنم
🌟
شب جنگ جولیانو (مربی بدنساز پرسپولیس) به هتل محل اقامت من آمد و گفت که پرسپولیس قرار است فردا اعضای خارجی تیم را با اتوبوس به مرز ترکیه ببرد. روز بعد ما 15 ساعت در راه بودیم و پس از رسیدن به ترکیه از آنجا با هواپیما راهی مجارستان شدم.
🌟
با اولین پروازی که می‌توانستم به ایران بازگشتم و به چیزی فکر نکردم چون من چنین شخصیتی دارم که اگر خانواده‌ام به من نیاز داشته باشند، من همیشه کنارشان هستم و اینکه ببینم چطور می‌توانم کمک‌شان کنم.
🌟
هر جایی که بوده‌ام و در هر تیمی که بازی کرده‌ام، تیم خانواده دوم من بوده است و حالا پرسپولیس خانواده دوم من است، به همین خاطر تردیدی به خودم راه ندادم و بازگشتم و حالا تمام توان‌مان را برای آنها به نمایش خواهم گذاشت. من در ایران احساس امنیت می‌کنم، عاشق این کشور هستم و خوشحالم که به اینجا بازگشته‌ام
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133727" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133726">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/133726" target="_blank">📅 14:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133725">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✅
جلسه آخره اوسمار با باشگاه زیاد خوب نبوده و گویا یه سری اختلافات وجود داره
🔴
به گفته منابع نزدیک اگر اوسمار با باشگاه به توافق نرسه مربی بعدی تارتار و گزینه های ایرانی نیستن ، از مربیان خارجی هم اسکوچیچ دراولویت باشگاه قرار داره.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133725" target="_blank">📅 14:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133724">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✅
❤️
حسین خبیری، گزینه باشگاه برای مدیریت ورزشی باشگاه است تا جانشین محسن خلیلی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133724" target="_blank">📅 14:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
جلسه اوسمار و حدادی پیرامون قرارداد و مباحث مالی سال دوم سرمربی فردا برگزار می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/133723" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133722">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDAbPGxHLwWnSc-sap0YoFoWXbYpr6HsXBxkjNctaAI0eVgHlyWmuHB2pHOlGKIaBJ56Ybam8GgrCD8vorDsfMWdnv5yd7lYKWjxJmRzusJRG-nYRtVcAyxs6nasz9I-wpdRa3tGYGtbqcD6Ezck06Wf7BfKhNZD_9CgOWTfXCLswejyjH-cIngYgtiMbaRnkyIwAwEJxGbUguvnIjSsXCfI5ImGRUBl202mPXLTeaJiGdK2seyyVQtNiSwbphVg5i_74z6VeHe4JanCzATVPX63jfrEbA-j5xc0LJrXkvdQ2xsfyG5B_goJcEDeoPJYD_HJgtUhVSdOj3ruv2zMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه K جام‌جهانی ۲۰۲۶
[
پرتغال
🇵🇹
🆚
🇨🇩
کنگو
]
⏰
چهارشنبه ساعت ۲۰:۳۰
🏟
استادیوم ان‌آرجی
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
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133722" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133721">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات…</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SorkhTimes/133721" target="_blank">📅 13:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133720">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
خداداد عزیزی : از طریق یکی از دوستان با پرسپولیس صحبت هایی شده، من اگه بسته بودم همینجا جلوی دوربین میگفتم بستم، هنوز قراردادی امضا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133720" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133719">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❗️
❗️
خبرگزاری فوتبالی :
🔴
🔴
اوسمار به مدیران پرسپولیس اعلام کرده برای شرکت در تورنمنت سه جانبه به ایران برگشته و برای ادامه‌ی همکاری در فصل بعد باید فکر کنه و از خانواده‌اش مشورت بگیره.
🔴
🔴
باشگاه هم به خاطر این که فصل بعد در صورت نیومدن اوسمار به مشکل نخورن؛…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133719" target="_blank">📅 12:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133718">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇷
❤️
رسانه‌های بلژیک نوشتند که تیم ملی ایران بخاطر سفر از مکزیک به آمریکا، دچار خستگی شده و این بهترین فرصت برای آن‌ها است تا پیروز شوند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133718" target="_blank">📅 12:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133717">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❌
❌
لوکاکو: بی صبرانه منتظر بازی با ایران هستم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/133717" target="_blank">📅 12:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/133716" target="_blank">📅 11:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#شفاف_سازی
‼️
تارتار هم محصول مشترک پژمان راهبر و فرزاد حبیب الهی هست و در کل ریدم تو دهن هرچی مربیه داخلیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/133715" target="_blank">📅 10:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133714">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_iIS0QfdbaJmF3g8Ks54XW6DBYdNZBd30Ue2QiHqpag0EP_r9YhVVAyRRXTxpLXXWUhbkIRBYHWT-vcSPAkvs0hjlpdzgWBA_n03cbjDvzDorjDRJWK7p3jxwvi_mn1mdWJ872hLoSMjtReaDvdIdA3KfU6I0BKSdAvykFzgbfVnLKAxeLFH-Au54fVZwF8Nx61DaASonCmsDfKDjsnK_RtVxbJl4Q4OxsbJsblJGzIcdwtmRXyJN6ndgG4L-kdR4ezbJjdKzRDJPuuJ7gH0Gvt4hOX_MaB7LeLOzXuHZ-nhnlZs2-RvEtxnp-lzKAxqrzrQ5FHhKl_qMUD0n9Lxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
اولین هت تریک جام جهانی 2026 توسط اسطوره لیونل مسی به ثمر رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/133714" target="_blank">📅 10:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh7gEQyJS8vlZKcRr8nFuRv6UYuelTcxP_Fi7I9SgSksBm8YgJgKB0CAx9rGZNTj54-IOaHOSZLK7XUs9HWD7bobJXXL3W6O-NvsAzDx6-ceG8CUrJOCKj5lL-L6PAW1l7mg5d6-PzfkT6fg9qV-WGjK93A12-w30rL8NMtPv36-zggep0lBtYs6doP0DIUGRTJ8LMS1rBXU63MbbZAiX19-uZgW9pwbMp3EEd-A3rQZtwxoD7AvNpflBW-TjW9PziG2VfPGQYGvatuqPfpTIURrS3xopI1CsU9JvnMRzu_jNaktUM_c_9VIhfxW-_EcY6rzhMLE3WM3DBCmq57rdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جدول گروه J در پایان هفته اول
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133713" target="_blank">📅 10:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
بانک شهر می‌خواد نقش اصلی رو تو اداره تیم و خرید و فروش بازیکنا داشته باشه، نه فقط حمایت مالی.
✍️
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SorkhTimes/133712" target="_blank">📅 09:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
گویا فقط ویزای مهدی ترابی باطل شده و شایع باطل شدن ویزای طارمی اشتباه رسانه فرانسوی بوده
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/133711" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133710">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efadb3452c.mp4?token=ffhytqyssrblzF3IMJEfqvNCAewj3vjHme6qQEp5Jkq9xULLAL3AO3PafwMjDZ0CZrtY2NDkpKJhaMir3SVFaFrIvbfUKbPdmrugXKUokRgZu7HfeEL5X5hzxXhdL10yjDbpMmk0r7nEZzDRuCwTQ_6FEcdecfUdRjNy270kIG_IdWysI5v1QvluSAtLEWxrdQ_UV8k1YHeqsiS_VUr8q4-xNHItKEHnL77w2UsoCXy1p7zrId_hYbJWkPVB7tqTK37B_mz8esMKA5N-Iqe1yhe2i4zUWk27mfa0bqZuBuiPHTH5K_4q1O61QIZTGfwZRDiZjVFgzQolnmTponnEQnBdjVh7U3-4B_UJGG5unmaftxD4fWhDbX5eQSYIRmsn9BcM8goUmEzHp71uwTY4vmqILPh9u6uC-hvrfP-51hT2pA8KisgAFvWUdMPtn-hA2pQ2eiwaw7XWCXmB2CSzU0fJUoSKEWFZTssPS1dov7bAWnFHsJcrcye0lk6Iz2LVE-jzcqNUR2UT1gfYaISaERd-lG9xhnMC_R393j6nbT2UW7UfzRwPo5ElBWNCkPWL75qUGbiTD7ec2yT3lYwHwmbMMO-PQynWEntVJK9848tchdcUWjwhNp55U4gpPHeRhNaFjFFZPb0cNVlTgjNHlt-5Fh2w4CrTxjfxSpJrMv0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efadb3452c.mp4?token=ffhytqyssrblzF3IMJEfqvNCAewj3vjHme6qQEp5Jkq9xULLAL3AO3PafwMjDZ0CZrtY2NDkpKJhaMir3SVFaFrIvbfUKbPdmrugXKUokRgZu7HfeEL5X5hzxXhdL10yjDbpMmk0r7nEZzDRuCwTQ_6FEcdecfUdRjNy270kIG_IdWysI5v1QvluSAtLEWxrdQ_UV8k1YHeqsiS_VUr8q4-xNHItKEHnL77w2UsoCXy1p7zrId_hYbJWkPVB7tqTK37B_mz8esMKA5N-Iqe1yhe2i4zUWk27mfa0bqZuBuiPHTH5K_4q1O61QIZTGfwZRDiZjVFgzQolnmTponnEQnBdjVh7U3-4B_UJGG5unmaftxD4fWhDbX5eQSYIRmsn9BcM8goUmEzHp71uwTY4vmqILPh9u6uC-hvrfP-51hT2pA8KisgAFvWUdMPtn-hA2pQ2eiwaw7XWCXmB2CSzU0fJUoSKEWFZTssPS1dov7bAWnFHsJcrcye0lk6Iz2LVE-jzcqNUR2UT1gfYaISaERd-lG9xhnMC_R393j6nbT2UW7UfzRwPo5ElBWNCkPWL75qUGbiTD7ec2yT3lYwHwmbMMO-PQynWEntVJK9848tchdcUWjwhNp55U4gpPHeRhNaFjFFZPb0cNVlTgjNHlt-5Fh2w4CrTxjfxSpJrMv0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رختکن تیم ملی پیش از دیدار با نیوزیلند و صحبت های زیبا و انگیزشی علیرضا جهانبخش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/133710" target="_blank">📅 09:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133709">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CldN1Odu30b8xP8qz_mEv5FjcgAjf1IXttCQ0fbzXQUkTb2bzSV8g4UfrpdC002cDoTEoTwY4Ii55LHIfsaDdkE3-nek9L9e_stOpwUDpC_ViyDpx5uCSLHbuNUQ1e-daQf3Mn0RqDnW3SDWAZKlpj1uHMcl1XbrAdWfDyylUdwsyTsBHzCDjuPYimeE_xWtXpQYd1p72EJIm5MV0g8mYWnT-erjkWWkS2Ajo_2BA9WJLCfpacDoM5xMaJwvpMRsqxDaagfXP9s580VSOYeytYfBhJ67IfPyCxeLMQ_XlHdRj8wxtgcFmlbRPnAiO8yLZMmbZ0CubHsXGhqx8mhdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🏆
گروه J جام‌جهانی ۲۰۲۶
[
آرژانتین
🇦🇷
🆚
🇩🇿
الجزایر
]
⏰
بامداد چهارشنبه ساعت ۰۴:۳۰
🏟
استادیوم اروهد
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
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133709" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133708">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
#فوری
| سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد
🔻
سنای آمریکا روز سه‌شنبه با اختلافی اندک، طرحی درباره محدودکردن اختیارات جنگی «دونالد ترامپ» را در قبال ایران رد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133708" target="_blank">📅 01:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133707">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLUCQNzzK-xtIvzHIoyxOU0RdJmqatRLtrz6V2g4jE3eClSXYyUAXMrYHrzbMQAz2JPcC7dUyDFqPnhKtTIn7CAh33Ube2IGoUmuQUrQT3avT14wagLNqqdO-1lhvbAhAHajBrszw0C0OJb_c11eHPYgT4eQHSKixCCqBTyG2xAwCJHjWqN9QOprurr4tRa5PIS3UeNnRc1HT0dxPyUyIuA5cQSQmzhLdoXTt0yD7aweIA1pqK5pbfmfrAM-yzcwGCxOqNyQ4Cklwl-Eh72Ey4uNdJ91ojiYpQUKWXYA6QoVMHY69wwUhRKO9WADDzGD_g3B-y2_z0C37P2r2ZO_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
پست اینستاگرامی اکبر عبدی با عکسی در کنار علی دایی در بیمارستان
🔴
علی دایی، اسطوره فوتبال ایران، با اکبر عبدی، بازیگر سینما و تلویزیون که در هفته‌های گذشته دچار حمله قلبی شده بود، دیدار کرده و جویای حال او شد.
🔴
اکبر عبدی با انتشار این تصویر در اینستاگرام، از علی دایی بابت پیگیری احوال خود، قدردانی کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/133707" target="_blank">📅 01:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133706">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=jwo28gfftulsYRLzfW7d_CgAJ88YZuWD2rJc-HcvAriFIL7MYSbzSAD7Du66t5AlSVVCWNW0rA7PBjHlKMRy3aW69fyAZuVgdHycPtdjBek_go_Udl6xwvBSqPIY_DHcsGDKhCbctnVJ7B6QKm7aKOCjzg0qIZVf15G9jRbLM8IyVYlzEskJhry8tzLsrzkb3ASZXGGRtKc5xOYM4wTL1yl3wC01UlhYncxspqbgfNGSU7Uy8TKJ712HH4uZr2PZbJkvvW2hmU3ifk7xQkOeDHafyJmSsCzhgGGZ6cFlLrs7ptq8xIEELKliUO4pNKOJinNUCJ4Ocev-Z_bxjNo0UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad4cd3bf3.webm?token=jwo28gfftulsYRLzfW7d_CgAJ88YZuWD2rJc-HcvAriFIL7MYSbzSAD7Du66t5AlSVVCWNW0rA7PBjHlKMRy3aW69fyAZuVgdHycPtdjBek_go_Udl6xwvBSqPIY_DHcsGDKhCbctnVJ7B6QKm7aKOCjzg0qIZVf15G9jRbLM8IyVYlzEskJhry8tzLsrzkb3ASZXGGRtKc5xOYM4wTL1yl3wC01UlhYncxspqbgfNGSU7Uy8TKJ712HH4uZr2PZbJkvvW2hmU3ifk7xQkOeDHafyJmSsCzhgGGZ6cFlLrs7ptq8xIEELKliUO4pNKOJinNUCJ4Ocev-Z_bxjNo0UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
شنیده ها
🚨
🔸
میگن فردا از کسری طاهری رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/133706" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133705">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/133705" target="_blank">📅 00:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133704">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fT16Qa_dl6E00CN3b5Oo0d6yhNwTT-PGaNbz98KlcuwSXYcTHEvVTfQXiiCLQXJkIy8oqYX1mwRe22TLchtFBraV7w0ZDjCJ4WbMkemMoMhFT9jo1H4HF_MWVrcH5yA2Wz1Sp4jgCv31gKIK1y-dX1WdW2n_fqzNaLAdzwEMuWLgIQWJoulmke1M-DU3LyMxLL8i49IPPWZ7-CxU4ut2ik_ofTrPqEHPD_Fy8qYYWjaoQ9zVQNz6OduJaXO9O2o9PIGmArNPOLqyZV5uCl1sO9Qmp851fqyL2MY4IZEWpGHSray0p5QAfSUdBPfFM-MwPHQGBL2hOuqmtvqplizdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سیدجلال: اوسمار پیشنهاد داد برگردم
❗️
صحبت‌هایی در این زمینه انجام شده و آقای اوسمار هم پیشنهاد هایی داده‌اند اما تصمیم‌ گیرنده نهایی من نیستم. این موضوع به نظر مدیران باشگاه و افرادی که درباره مسائل فنی تصمیم می‌گیرند بستگی دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/133704" target="_blank">📅 00:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133703">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=MmgBAMCu8dqbtaXDqZnQ_XC5wEAdI79fm0sRbJoL6gAWX4pRizih0l3-x9OluekFa_dhbNjQi5dgiF1uqkUCLHwTaMvv6QbJ1Wfm3Da_Zt6AaId_cl9jMDcHDjZBv7RFJVvVDGCSm9ZnIBFVxlLyjfZPQtTrjg9Qt46MegZLmyRbc-_q5PmcFU7RMkDH2DVFdNvsHdNxsg4Ev6DVsTyyvMcOWnlPkp562oSP4EW54g0jnzFjbQ4oyI3rCMOLn3TqepI25I4KEDvTQnevsHrqheoyncBm0p3G5jgqHnaOv0X1VtLf3sjQZ-nSJpP_jeTv_zqBq0clvN_4XO7y6Axoww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=MmgBAMCu8dqbtaXDqZnQ_XC5wEAdI79fm0sRbJoL6gAWX4pRizih0l3-x9OluekFa_dhbNjQi5dgiF1uqkUCLHwTaMvv6QbJ1Wfm3Da_Zt6AaId_cl9jMDcHDjZBv7RFJVvVDGCSm9ZnIBFVxlLyjfZPQtTrjg9Qt46MegZLmyRbc-_q5PmcFU7RMkDH2DVFdNvsHdNxsg4Ev6DVsTyyvMcOWnlPkp562oSP4EW54g0jnzFjbQ4oyI3rCMOLn3TqepI25I4KEDvTQnevsHrqheoyncBm0p3G5jgqHnaOv0X1VtLf3sjQZ-nSJpP_jeTv_zqBq0clvN_4XO7y6Axoww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
‏پیروز قربانی سرمربی فجر: با
بچه‌های شیراز نیوزلند رو میبردم!
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/133703" target="_blank">📅 23:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133702">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133702" target="_blank">📅 23:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133701">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0DWFpQonHYPaZ3QeiJeBoz5OTklea9EKWggYpE85wjcP_uI9yn2yo4tldKT_q4O-DGYbAQhj1SnXh9m1gkrrI0KcTpY0kpsfhaxqSKgCQPrnXP2e26Bl8dxiaeLhla5bbQ7MA1iwpm5SSXiGCHCpNYN-SIGbHA681klZVHfJBX3dSN6cMygMbu30jaqMR-0pu75Yuu-CQj3-A8tAtjRCIlN56hnNMvr1JRbUAEW9FQ0tlJopyNQ38QPL32Pnl-HOXPCRiwt3i2harspYhkvXadlX3H_VRUxjKum5dBQyBxtNMOSCfu2GA5YI-gCa6An-savfasI_Lw9a2_jNtBoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان در بین ملی پوشان: میخواهم تا چهل سالگی دربالاترین‌سطح خودم فوتبال بازی کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/133701" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133700">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133700" target="_blank">📅 22:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133699">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
برنامه بازی‌های روز پنجم جام جهانی
🙄
سه‌شنبه 26 خرداد
⏰
22:30 |
🇫🇷
فرانسه
🆚
🇸🇳
سنگال
👀
چهارشنبه 27 خرداد
⏰
1:30 بامداد |
🇮🇶
عراق
🆚
🇳🇴
نروژ
⏰
4:30 صبح |
🇦🇷
آرژانتین
🆚
🇩🇿
الجزایر
⏰
7:30 صبح |
🇦🇹
اتریش
🆚
🇯🇴
اردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/133699" target="_blank">📅 22:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133698">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPcQuCZ7YOocr_ovy-mfOLQrFDtliP8a3Nd7m_CTbMY7F3XQhydgSq4-_CQlxKMk-HziWXyZFQm077_0-2SsaE9ZxFqbKTkkvl-01Y9C8pvxCizbYxuCS5aKhQolEuump7b-E6cp5gpDFRtAtixjs8uqpmOxM1zsBK6S-u45S4onfYBNxd3czbUOFbAusn_9_GxBvTCE4n5VtmkCZIjlHGN68IzZV-v1EIbn1EaQ_gf_Cf1G4Hce1rcxBjPOOwXCe_w_IJO5rZXwUfEMLyU3krhJUQUI04iqYmOH-tyLvOXc7fSxS3hpODur_BIbR_irchenldINIIxKfDs_hTWCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رامین رضاییان: شادی گل من سیاسیه اما اینجا نمیخوام دربارش صحبت کنم. گلم رو به تموم مردم عزیز ایران تقدیم می کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/133698" target="_blank">📅 22:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133697">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133697" target="_blank">📅 21:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133696">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH_yBULggIcPzUsrCFa_3PWm1FnveucrQtThFCxrt3twAwunDtYKVzX3dBg1-nr30k9hXVx8ftf33XwxFa4JSjL8yV699l2ZVH9cRtNFFQ-bG69o1wtritNg-ntzinaUtW8E8riMlBBHTKsuZ3uiHxglIdMbNk_DLq8I5cmzV1UVzidUe9xRmaV6k80vWYMLTiw0FfM2HWphIfz6h_ynxrLYWH5XCtbp0p0xF33n3V1DNlrRB8tMzdagFnhAbJg-25DhCqCeVrYPGcCwPkj4MZeoHKhBmmj7U_eClDEMrP_lwvldiZ0XAclChhr1mmPcVXEOPydoc03kcIKmRvrBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
نشریه‌ معتبر ESPN: علیرضا فغانی که‌ داور دیدار امشب سنگال و فرانسه‌ است اصلی‌ترین گزینه فیفا برای سوت زدن دیدار فینال جام جهانی ست، و اگر اتفاق خاصی‌ رخ ندهد علیرضا فغانی فینال رو سوت خواهد زد
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133696" target="_blank">📅 21:25 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133695">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/133695" target="_blank">📅 21:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133694">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoTIbSEHMzhl3yFjHWDyeZqb2HwoHAOX_FKw57eaG76jH_ExotpA-gPj2DjWnIhC9sb_wxWXgZO31i4maBWlhQLjoOj7ANPqoLSaCZkAiSzLKWlVVpaPF0bClUxiK0cK9hl_cH8EXKfXpZPA0eU3i4mgWHqxrZkftNyBWgqhvx524HVCZxR4sL_TjllXtc2RSndeHbGzh8bVHACzW708LI_XjE2J9zPv4BZHGNUc7CCLJKQD_kJu2Vx8u_22a7m1tOV9L98ZP7-ebZDs91HS_KbQtd44lf_sBICuMC1z9733DOlfz8fceJ6jLjoOpkulc2JAleodOk46wSqr20mCOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🔵
FRANCE -
⚪️
SENEGAL
⚫️
جام‌جهانی گروه I
⏰
سه‌شنبه ساعت ۲۲:۳۰
🏟
استادیوم مت‌لایف
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/133694" target="_blank">📅 21:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133693">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
مهدی تیکدری نژاد مدافع راست گل گهر سیرجان با عقد قراردادی سه ساله به پرسپولیس پیوست/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/133693" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133692">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری :
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/133692" target="_blank">📅 21:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133691">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⁉️
⁉️
حضور عزیزی در پرسپولیس قطعی است؛ آغاز فعالیت‌های سرپرست جدید در امور نقل‌وانتقالاتی
🕯
حضور خداداد عزیزی در پرسپولیس قطعی شده است و حتی او پیگیر برخی امورات مربوط به تیم و نقل و انتقالات نیز است.
📊
📊
عزیزی خانه خود در تهران را حدود ۱۰ روز پیش در جلسه که…</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133691" target="_blank">📅 20:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133690">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmOgGpVDUbAKj_RRN-URd61uuKe98lSwR7ZJZpVigmTcCRa1lAIG-2YZwaPko8eeOlvg1quHtE4HckD2V5lfdTbbEVLMyShoVm33MD7nVso76_gyDYwrBGFcyjcRbb-4zQY4FmxVChjSJVE_umY4-Aa4zHqdcV6hWx4Ruj_gueFwJ4dr88rmXbbXULPDGDBObJGv_-3CsRbJzfB7UO5MxLTYfAicpT77lGOyL6uXGf0IzTTItEoV1SnWTptPG2HMo46A0rlL0b4vaMVXF16KlUFZlzwojif9t5nIn8pJS_OUgKJz52IMNNJXrX8AzA0s0dnGbLIufuJtDq9y2PfSUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
:
🔴
مهدی تیکدری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133690" target="_blank">📅 20:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133689">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/133689" target="_blank">📅 20:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133688">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90353b1248.mp4?token=PgiK-pdoH_lPrzQ1sTcHnsPr5pJcSYIW5vIGwQ3COY8BasXk7-YP0kn40CS2dTAaaIVJISIRiG69f8pmG-4Q5WFUFKALiJkGdqPWfJJlTrsRm05ABcY60bH5fuTaUHFFDvj9KCwqipYtF4bexTE9Ta8V_76FLO-jEIUtAHG3DiOiRKm3cJPOvqmYiLcvHqxV7SiNDqltxVBoghYZMoUTEKtbZ7U3duljCWN46pmGQRAfHfXamNYebNifzJHzGZpAhkTIfWpqx3bgj9gQ501WILgqSldnoglAxcKQ9B0cy_E6TKKfz2QAQG-yvkyJ5satOFmGJhtz1Ir6j3Zza02sBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90353b1248.mp4?token=PgiK-pdoH_lPrzQ1sTcHnsPr5pJcSYIW5vIGwQ3COY8BasXk7-YP0kn40CS2dTAaaIVJISIRiG69f8pmG-4Q5WFUFKALiJkGdqPWfJJlTrsRm05ABcY60bH5fuTaUHFFDvj9KCwqipYtF4bexTE9Ta8V_76FLO-jEIUtAHG3DiOiRKm3cJPOvqmYiLcvHqxV7SiNDqltxVBoghYZMoUTEKtbZ7U3duljCWN46pmGQRAfHfXamNYebNifzJHzGZpAhkTIfWpqx3bgj9gQ501WILgqSldnoglAxcKQ9B0cy_E6TKKfz2QAQG-yvkyJ5satOFmGJhtz1Ir6j3Zza02sBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرمربی پرسپولیس: خوشحالم که دوباره به ایران برگشتم. منتظر تصمیم فدراسیون برای برگزاری بازی‌ها هستیم. آماده‌ایم به هدف هوادارها در رسیدن به آسیا برسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133688" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133687">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56204fee3b.mp4?token=GjzP2wvReEcRCMJOJcTbjnegXOnrF_26EmMEeElqOFXFANmGLzobRiVwWZmn4-luAzavgLOeNn0NWpAf7Y8XV3YD-XafNhZaUUMFGcRTgjcHcCHQjCJ8VP7Nq1glZZ8m3Jz0aJgCGu3u2Z5A7dBmcvpPlJhG6Ui0sW-ZzepUBzPi2dfyQgqOkiVS7PUkjLrnlc0C_Opn5a8qjJdL8GQ74ylGMyCjuV3F_uL_rE3NXxbCIEM6a8pXIOqCzuavjTrqcBNh2NpvT91HaiEDeopilNnPqP5V7ZGX5SrPE3v-f_kC8_Xdpb-GnzmnQece6vhrtsjNVxKBCDdAVDYGfyny94f2AjuYrsDXwZC1rwCvwu35M9ek-FqPnFRahFN5IqwLzRAUyYz9tdJ5TdsB9MsML9yK9M0vKaaW_d0JVjYt0SAt4IZUB6091IXmUaCIe-NTFMLwefx5snlJazg7jCw_4onJOECIW8Vtn_FMds630fj4jGbUyeCBwwn0y5vyCwF8S4fRIAXolSaTe5Lx2ASLrnwFtJ5yM-oQktB0sj-2A47x3QdadPh_8oLjvqiOpz3FXcUcA1PdU1jIUt7JKPGqR0LQL2hOLAQZ_8OwrnGnu42Ah-OGgGZb8Dl7_FhD2JqWUSml7nczSLtlp8rp0GtRsKHvGfqkMg5ytfEhV3WPDmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56204fee3b.mp4?token=GjzP2wvReEcRCMJOJcTbjnegXOnrF_26EmMEeElqOFXFANmGLzobRiVwWZmn4-luAzavgLOeNn0NWpAf7Y8XV3YD-XafNhZaUUMFGcRTgjcHcCHQjCJ8VP7Nq1glZZ8m3Jz0aJgCGu3u2Z5A7dBmcvpPlJhG6Ui0sW-ZzepUBzPi2dfyQgqOkiVS7PUkjLrnlc0C_Opn5a8qjJdL8GQ74ylGMyCjuV3F_uL_rE3NXxbCIEM6a8pXIOqCzuavjTrqcBNh2NpvT91HaiEDeopilNnPqP5V7ZGX5SrPE3v-f_kC8_Xdpb-GnzmnQece6vhrtsjNVxKBCDdAVDYGfyny94f2AjuYrsDXwZC1rwCvwu35M9ek-FqPnFRahFN5IqwLzRAUyYz9tdJ5TdsB9MsML9yK9M0vKaaW_d0JVjYt0SAt4IZUB6091IXmUaCIe-NTFMLwefx5snlJazg7jCw_4onJOECIW8Vtn_FMds630fj4jGbUyeCBwwn0y5vyCwF8S4fRIAXolSaTe5Lx2ASLrnwFtJ5yM-oQktB0sj-2A47x3QdadPh_8oLjvqiOpz3FXcUcA1PdU1jIUt7JKPGqR0LQL2hOLAQZ_8OwrnGnu42Ah-OGgGZb8Dl7_FhD2JqWUSml7nczSLtlp8rp0GtRsKHvGfqkMg5ytfEhV3WPDmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: اگر تصمیم گرفته شود که بازی‌ها برگزار شود ما آماده هستیم/ اول باید تکلیف کادر فنی مشخص شود بعد سراغ لیست بازیکنانم خواهیم رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/SorkhTimes/133687" target="_blank">📅 19:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133686">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: بازی‌های لیگ می توانست برگزار شود/ تیم ملی ایران نیمه دوم بازی خوبی مقابل نیوزیلند انجام داد
🚨
بازی‌های بعدی تیم ملی می تواند عملکرد خوبی داشته باشد
🚨
بازیکنان خارجی تیم همراه ما هستند/ سروش رفیعی؟ تصمیم شخصی خودش بوده است که هراه تیم نباشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/133686" target="_blank">📅 19:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133685">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7b067e8b9.mp4?token=cBQ2vV3ks9p3UOGgRR8DlE_DNlmL5I70__8ny2IqS75GrLiuBGXPzPA7Z-KM-ZgcBjrx9hm1e1D-erSV3nf02HXIaPD2tbLPces6ClprZ1a2OaWs9U9x5uC6kLeShjxLi1RbzTJ8l3xhBh7_kFKgeDvsYJ1TiIlAhkX700Wui6kOEA0UXkje8HhQCR9jN8gUhIsqKpWX9xYbC_O3vruEPsmOaZ81yaPiwJl5zKupn8tC-ZIEEOvsNErD1E2JWYP9f2KZGfuKxhIlrQtVlTf3gfJqfa-41soA1GsE45FAXgSMrDGX5R0Hfsvf3vgM9lwBLH4oGDHZqvunmTI_Yri7JXgk60i0JVw9tG8G4ekqUBsKN62T70kdOdPS_DbJ7FBhm5Qy_Bw020B346Wgo67GmZ6y1Re54eZ9vAWS9YKlUSg5qfN4PI0igMmPyUlEHVCfwP7pWlnugtX7IKonW94dCuBqy92UH7StGc-RE1htBQ0KLfZveb63SPp768omkHsSCgjqYKkL2qjwYZbh0pOpAZvKczZvuJfaQT9odNNdyih6l5ymz0HjQ-hh3Q6u67woWgXvh-AIOPYsdVMTTI3Y_bAv4T7tzPfXLLMNESOQrWDojGDmT6gEOa1PCYv7EtKRpTLeEsbtJ8Xl9skQs9fQexAVzMznaU3j2-Y6_5zzh1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7b067e8b9.mp4?token=cBQ2vV3ks9p3UOGgRR8DlE_DNlmL5I70__8ny2IqS75GrLiuBGXPzPA7Z-KM-ZgcBjrx9hm1e1D-erSV3nf02HXIaPD2tbLPces6ClprZ1a2OaWs9U9x5uC6kLeShjxLi1RbzTJ8l3xhBh7_kFKgeDvsYJ1TiIlAhkX700Wui6kOEA0UXkje8HhQCR9jN8gUhIsqKpWX9xYbC_O3vruEPsmOaZ81yaPiwJl5zKupn8tC-ZIEEOvsNErD1E2JWYP9f2KZGfuKxhIlrQtVlTf3gfJqfa-41soA1GsE45FAXgSMrDGX5R0Hfsvf3vgM9lwBLH4oGDHZqvunmTI_Yri7JXgk60i0JVw9tG8G4ekqUBsKN62T70kdOdPS_DbJ7FBhm5Qy_Bw020B346Wgo67GmZ6y1Re54eZ9vAWS9YKlUSg5qfN4PI0igMmPyUlEHVCfwP7pWlnugtX7IKonW94dCuBqy92UH7StGc-RE1htBQ0KLfZveb63SPp768omkHsSCgjqYKkL2qjwYZbh0pOpAZvKczZvuJfaQT9odNNdyih6l5ymz0HjQ-hh3Q6u67woWgXvh-AIOPYsdVMTTI3Y_bAv4T7tzPfXLLMNESOQrWDojGDmT6gEOa1PCYv7EtKRpTLeEsbtJ8Xl9skQs9fQexAVzMznaU3j2-Y6_5zzh1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
اوسمار سرمربی پرسپولیس: مدیران پرسپولیس کارشان را به خوبی انجام می دهند و به ما کمک می کنند/  دعوت امیرحسین محمودی به تیم ملی؟ ج اگر چه در لیست نهایی تیم ملی قرار نگرفت اما حضور در کنار تیم هم تجربه خوبی برای اوست.
✅
مارکو باکیچ ، بیفوما و دنیل گرا نفرات خارجی پرسپولیس در تمرین امروز حضور داشتند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/133685" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133684">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00ec62d09.mp4?token=lddp4KzR6WqfoO46n1vZFT2Ng82cyqv4pjU3nkOMiLuIDP3ZuJ4-ZG6RNOSGun5p5V16EpKgmovYi0dAjJ-WBNrMj9w0d6ZLVo8nCOXxK3wX1NJKQEw1bFEKN1KEey1Z6ppNYOvN2r0TglADqZl4rEtji_nU0_f5p2I1SZ9Of8FnFhtag9NUWocOb_xmrnbExDQLNhg9ojVBCAPBjcOnxRwED4HEH1JWHHsHZmfOlyghHPFK0dOH4JsLye4_PWWxaCIrRg31a5_xiqXs0AQBtqYVDDsCf0lNe7Q8ClsyCAvE8Cfn9ao2v4dSrM-QEdRAH5YxeV5PPKXhluckXWta5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00ec62d09.mp4?token=lddp4KzR6WqfoO46n1vZFT2Ng82cyqv4pjU3nkOMiLuIDP3ZuJ4-ZG6RNOSGun5p5V16EpKgmovYi0dAjJ-WBNrMj9w0d6ZLVo8nCOXxK3wX1NJKQEw1bFEKN1KEey1Z6ppNYOvN2r0TglADqZl4rEtji_nU0_f5p2I1SZ9Of8FnFhtag9NUWocOb_xmrnbExDQLNhg9ojVBCAPBjcOnxRwED4HEH1JWHHsHZmfOlyghHPFK0dOH4JsLye4_PWWxaCIrRg31a5_xiqXs0AQBtqYVDDsCf0lNe7Q8ClsyCAvE8Cfn9ao2v4dSrM-QEdRAH5YxeV5PPKXhluckXWta5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اوسمار سرمربی پرسپولیس: تا وقتی این فصل تمام نشود لیستی اعلام نخواهد شد/ یاسین سلمانی؟  خودش فهمیده است که اشتباهاتی داشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133684" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133683">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
❗️
اوسمار:فدراسیون می توانست بازی های لیگ را برگزار کند.مدلهای دیگری هم برای انتخاب تیم ها برای آسیا بود
💬
به خاطر فشارهای غیر فوتبالی روی تیم تاثیر گذاشته بود اما در بازی های بعدی جبران می کنند
💬
وضعیت سروش رفیعی و تمرین امیری در کنار پرسپولیس؟ در مدتی…</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/133683" target="_blank">📅 19:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133682">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/133682" target="_blank">📅 19:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133681">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be8a9600b.mp4?token=hF48cwP1NIGVmRp-6nOOjCIMK1bAGtVZ-p2H020WTUaI7RlDuSJoLDjoZhyZ_EY0ClszG6EJLyEwDnzM9wTFPLPb6BPfOx74m_-BFBOsfAoArD6kS2IaFXMAF6_IsDpMzkQnxRPQchrLY4ct0R3x8-3_Fzdl7JYBV6_Md9aFRGucw9rWNiv2nwQEa8xbXb8ZcETF6NgQTgGFBaKu8eZfb8p3-ro3QrNRrI6A-eli4u2sOs5wNkfmOk2q1pOUstXOsqk7c0lJzSywjiNFquVh_NMsbIDxkaHWJx3lWXgbFRyg0-LkLiskbH2A0TlbaoORZmkaeAsBNERmmSZguurc3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be8a9600b.mp4?token=hF48cwP1NIGVmRp-6nOOjCIMK1bAGtVZ-p2H020WTUaI7RlDuSJoLDjoZhyZ_EY0ClszG6EJLyEwDnzM9wTFPLPb6BPfOx74m_-BFBOsfAoArD6kS2IaFXMAF6_IsDpMzkQnxRPQchrLY4ct0R3x8-3_Fzdl7JYBV6_Md9aFRGucw9rWNiv2nwQEa8xbXb8ZcETF6NgQTgGFBaKu8eZfb8p3-ro3QrNRrI6A-eli4u2sOs5wNkfmOk2q1pOUstXOsqk7c0lJzSywjiNFquVh_NMsbIDxkaHWJx3lWXgbFRyg0-LkLiskbH2A0TlbaoORZmkaeAsBNERmmSZguurc3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نمایی از تمرینات پرسپولیس در حضور وحید امیری و با اضافه شدن تیوی بیفوما، محمدحسین صادقی و فرزین معامله‌گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/133681" target="_blank">📅 19:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133680">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇺🇸
ترامپ: متن تفاهم‌نامه را نه تنها منتشر می‌کنم، بلکه احتمالاً یک نشست خبری برگزار می‌کنم و آن را کلمه‌به‌کلمه می‌خوانم تا رسانه‌ها آن را به‌درستی پوشش دهند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/133680" target="_blank">📅 18:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133679">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8eN_roTBQ6HIO4ewYMz5HUJ0PsD5QiUFRDGkQ-R6Qn-RGJd--X4yjfERioZie0UNFpE_cdozz_V6elmFCUCB7gaN8YI3XwSutPVZAA5FW4qQx41Kg0DB1G5e6tGCB2g1UIcvhq2j4maqZdZ2_xXOpRlPYnZRJYkORhlbwGT2JlBwemserz9AS2Doz05iRIMDY6dDjgxkm5oC6alegTcUq2jfGXCMh2dYfo_6INWb4a3ohNMJWm9RnbIrz4lC2oESF9jqcUJ6XauvaurLQ2z9jMukX6DTIsmaYFjQbkJsbFbMc4DJnWGqNmd1mmUHLhpU0AB44UKJ255O4OcDs_c4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
مثل اینکه قراره جمعه توافق اولیه تو همچین جایی امضا بشه
🇮🇷
❤️
روستای بورگنستوگ تو مرکز سوئیس که تا حالا میزبان کنفرانس‌های صلح زیادی بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133679" target="_blank">📅 18:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133678">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123eaa1e7a.mp4?token=HS8l2fuGvdlfic2uWMUU6aw7Vx9y9P11toyiOjVkLKXcDDCOZuufUQ-rSJRLR_L_PlUCGDSmMOYRtcSHhJi5T5sU4CzqTqD6VgFg1zX1XsigS_afBw3l6EqzUm9WlYEFG92A7LxHllilgt4gXvINIbkhxD5oUsSFedtJcuGiuMM5pdOozi9ifKht8Y7YlJXZPHigiOnJYiESmQ9KCy44R2Avm9QLsusVb5cJlJ5M0orxFZY_HhltIUWJH9OVqfXY4RiiWJEYSz0mlmaRh83-ZZYnZqexUMCQPtpMiW0X7XO4FEgTVrP6jzb8gS_TWosfLi33ZaDJx4aJws107Q8X2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123eaa1e7a.mp4?token=HS8l2fuGvdlfic2uWMUU6aw7Vx9y9P11toyiOjVkLKXcDDCOZuufUQ-rSJRLR_L_PlUCGDSmMOYRtcSHhJi5T5sU4CzqTqD6VgFg1zX1XsigS_afBw3l6EqzUm9WlYEFG92A7LxHllilgt4gXvINIbkhxD5oUsSFedtJcuGiuMM5pdOozi9ifKht8Y7YlJXZPHigiOnJYiESmQ9KCy44R2Avm9QLsusVb5cJlJ5M0orxFZY_HhltIUWJH9OVqfXY4RiiWJEYSz0mlmaRh83-ZZYnZqexUMCQPtpMiW0X7XO4FEgTVrP6jzb8gS_TWosfLi33ZaDJx4aJws107Q8X2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظاتی از تمرین امروز پرسپولیس باحضور کریم باقری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133678" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133677">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
ترامپ: چیزی که مرا به امضای این یادداشت تفاهم ترغیب کرد، اطمینان از این بود که ایران سلاح هسته‌ای نداشته باشد.
❗️
اگر ایران به دنبال دستیابی به سلاح هسته‌ای باشد، جهنمی به پا خواهد شد.
❗️
ترامپ: ایران طبق توافق هسته‌ای به سلاح هسته‌ای دست نخواهد یافت
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133677" target="_blank">📅 18:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133676">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❗️
❗️
خبر پیشنهاد به اسکوچیج دارد فراگیر و جدی می شود.
🔴
تکلیف کادر فنی را مشخص کنید بعد بازیکن بگیرید.اینکه فلانی خیلی خوبه و همه مربیان او را می خواهند استدلال زیبایی نیست.دو فصل اخیر هم با همین فرمول تیم بسته شد و یک سوم خریدها هم با نظر گاریدو و هاشمیان…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/133676" target="_blank">📅 16:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133675">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
انتقاد مهدی طارمی از ندادن ویزا به برخی از اعضای تیم ملی:
❗️
فیفا به ما گفته است که همین الان لس آنجلس را ترک کنید/ در صورتی که ما باید فردا صبح ریکاوری انجام می دادیم/ حقیقت را بگویم شرایط برای ما فاجعه است، هیچ ارتباطی با فیفا نداریم/ رییس فدراسیون و نایب…</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/133675" target="_blank">📅 16:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/133673" target="_blank">📅 16:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚠️
⚠️
فوووری از ورزش سه: کسری طاهری مهاجم روبین‌کازان با پرسپولیس به توافق نهایی رسیده و بزودی از او رونمایی می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/133672" target="_blank">📅 15:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
مهدی لیموچی در یکقدمی پرسپولیس/ایلنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/133671" target="_blank">📅 15:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✅
✅
با اوسمار هنوز تمدید نکردن ولی با بازیکنای مدنظرش مذاکره کردن و تهشم رفتن به یه مربی خارجی گفتن بیا تیم ما/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/133670" target="_blank">📅 14:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQAcEONx8-2gq9aq2OkiyeeNJIwfwmyPsN1uuD_2Ppqep8O24ZFT2u-ewZ3rTSc8W3NEHQleHKXn1sn9GsjAVux_N2WAnY-ST_dfT2AGU3LuAuqt1LdCI3ZOurZvVbLtcIsPhs5Od8X5eoM4rGaYnq7DEyGfJHuR3R6dn4wXCbKhXM1Vbcxq5dRNJvVHaA8O-8jOEWQ7X1wotmWvDJ5vJ6hBCkBAcPi8SzvF6CCvF2v2NjLFtVrjr7x5uGjJrl1fvHs_Ns1AzUY8avt3vWSDAfAQarWh-RX8a4NLv5nYrjEWa8gE_UO77wqevxo8cr30mRIFCyayKN-cpfbXofwAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امروز صبح در فرودگاه لس‌آنجلس، مهدی طارمی و سعید الهویی هنگام بازگشت به تیخوانا، چند ساعت توسط مأموران نگه داشته شدند و از آن‌ها بازجویی شد. در نهایت، پس از پیگیری‌های فیفا و فشارهای فدراسیون فوتبال، اجازه خروج برای آن‌ها صادر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133669" target="_blank">📅 14:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8JO71JxiirImbEXV52Y_fgcHM_FwF_d2s1fKsnu5d4f3olrYZoqbWMTgZvwDHRun0bbqs8eFs7yxSSX0AF41T5TN4ZWaxAEd1qX3ESG3TUyImPvi4F9msHS6znPZRlIRyFFHYoQy6nMOsCjZpydne9C8wFiyB5Ls-NVgRJmsHooDTzUkDUWLtO4vhKggKZVP9oLnyqd5s1DaXH2NGVT4kwL8N4HCxX1ioHq9xm0riEafPuHBbjraBUot1moO8_vQlMy0-dVFeljiwgNhXs3P4Z8jgmBVSfdFn1DifXh2VObhYQyCvh29YR3Oqm6zYrC6wpy7-mAA4Z45WMPAcWxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قلعه‌نویی همینو قاب می‌کنه میزنه دیوار منزل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/133668" target="_blank">📅 14:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
شادی گل محمد محبی که تو رسانه‌های خارجی جنجالی شده و میگن احتمال محرومیتش از رقابت های جام‌جهانی‌زیاد است! زلاتان ابراهیموویچ هم که کارشناس شبکه جام جهانیه ازش انتقاد کرده و گفته همینکه برای تیمت‌گل‌زدی کافیه دیگ این‌کارا چیه که تو خاک کشوری که رهبرت رو…</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/133667" target="_blank">📅 14:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IE_fUss-h_zHvPRrM5bIFuA1zTsmlI49aiGZUwmWpziDaVFHxk3hrgP9h3MMRaQgpdomtixbJ3Xw_65Zb5XWhUJ2nIrIwfEE9zG5QtTQ5MHW42oMwwdb5Wuxn1a7aV1grP3ZMuwtI5-zTDuJi8j3xA3J3D94YKvYKNjtfyC-h1lqV5AtsBw5fv7vwrdOodJXnO29mK7LQ8Wfdo6ZCiSdl6qFUXGAy70x-8mDzyQvHA_nLPlLt8X4Z2eEsWReFoCxYNOwhH1wJQUPRdNwPwahxPp6IhbAv0MtYkles58Cv23_WhzmMwlZBPEsFm9GBfb_99VM2AC0eTpZ--K2K82dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بونوس ویژه جام‌جهانی وینکوبت ادامه دارد!
🎁
۱۵٪ بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه فقط تا هفته آینده دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/133666" target="_blank">📅 14:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
❗️
فرهیختگان: لیست خرید پرسپولیس شامل طاهری، یوسفی، لیموچی، زارع، محبی، نوراللهی، مغانلو، ایری و اون یکی محبی هستش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/133665" target="_blank">📅 14:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5B2qpzSEjsyr3PEKKamIoxOg8D82P32-FME8sYDXO71Yz2HadATEZ4uV_NQtwXqV6ufrLUZmXutJlUYB5qUEgbzh8-iHgwtYpkOXzAG_ymwb1QPY7hQ7l4Q6kHybCTYIPdTjBvinIjj1k_oh1DFGE1ZouStXJCBcydFVRqkjToL0QNaMByyEuB-fZF8gMUXFljA93_5pbtK6PzbPwENEgaL3OOmFOcie-DWda_21xtjpKGpvs7pq0fIbJnFhC5VwfCJosTTzrVIBUQ_KdBNKZL4pe0nWZHTJsmPlwwEXVVZRf6TJebPkTdtaGGJF2x0njEeMTMMObrOXO-V3VDlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🫪
برگ ریزون
😳
🔽
دروازه بان کیپ ورد که جلوی اسپانیا کلین شیت کرد توی کمتر از ۱۲ ساعت فالوراش از ۵۰ کا شد ۶ میلیون
🔥
🔥
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133664" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
یکی از نزدیکان احمد نور به ما گفت؛ احمد تو ایران فقط و فقط لباس پرسپولیس رو بر تن می کنه
🔴
همه ما زیاد از این حرف ها شنیدیم اما تو این مورد، مادامی که پرسپولیس خواهان احمد نور باشه، این هافبک تو ایران انتخاب اول و آخرش مشخص است.///طاهرخانی
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133663" target="_blank">📅 14:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
ترامپ: من به تغییر رژیم اعتقاد ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133662" target="_blank">📅 13:45 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
