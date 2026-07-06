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
<img src="https://cdn4.telesco.pe/file/WP7q3qOW_6IhDGi8lJX5mF9GmYLgj0OYRwt6QRaFZyqZuIu4SJ2lXKkdGqsepIs_5-l_0TmbeVQxG76oFGYeAiAZCdm_D3pKIg4zZSLG8YOxKgneHhMXidHqt-N3QFU_fyKKEwjujTRTneVX3ZegopHdI-OOEqAosWvSfany3Nps9MiCEe12AFBJkGrABFYTQy67YMbRjf4skgAO8GekbwsLYW0GrfDOOZ66OXD8yt4Z4E3anuIjMe40T61SnvSakAaEDFGea8TYuLsw6aud_SP9wM6-t_1myQl5F3SDRutt2D32zfDhr_YhQVB2AJWYuSMvKqD952q2K_yhl3D_bQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 21:40:27</div>
<hr>

<div class="tg-post" id="msg-135127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx51o-9HBdmFpAdWljVcEQ_D5RyyJxPOMvQMMcoWSpyhxN44dQcxxtoPwywjC8f2DDUMIttNCiKgTrqn3o4XkJ1F61pG5AOsD9oDpUVHVLX7QO8Hfh81Ll9fYkjay4HmY2unhoAArHwo7BYz0m3HW-7Of13cFjI4HAHYGx-hf4WdSDlE5QEQ1C6pmBccEwSzcj2dM_X5_tQK7o8x8Dbd5zqkvE8I_CeTZwx30ZguAw__ja8j_cF26F1vjXNtzdEOzvS0vldczUGHXZOowjWtWs4dAPKIECH59E_TZpQuhUd63tq2eGPdDyoWZLrAt1iOnWGu6NorNR6_6CDO7IST5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فوری از ایرنا:
🔴
هایجک مدافع تیم ملی از سپاهان؛ ایری به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/135127" target="_blank">📅 21:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/135126" target="_blank">📅 21:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❗️
اگه اوسمار بمونه فصل بعد وحید امیری به عنوان بازیکن یا مربی تو پرسپولیسه / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/135125" target="_blank">📅 21:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135124">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
کلیپ باشگاه پرسپولیس به بهانه حضور مهدی تارتار در این باشگاه به عنوان سرمربی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/135124" target="_blank">📅 21:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135123">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
رفقا این فرمو میتونید سنگین بزنید
🔥
🔥
تخصصی ترین چنل شرطبندی تلگرام
‼️
#VIP
#رایگان</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/135123" target="_blank">📅 21:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135122">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/imQ3miE3Bi-L8bwYv5K9NsU8HETeEBGz3x3DqWky-2pqMWb8aY2p8gDaBG0IqfVe7gh8mwNbXgfsjGGq_pzt6yFm0XG770G0G2ZFckKDbxQXiaf2fl9ZPgL2HjQHnOOvNccPYHVP269Dat3baUbamIBjuP15-A-GxzSaBDFxuIapNW8CY-TgUC_tfjFns3vwysIeHf8tNlbKHkCZXQxDwgNBSfIFLJMszAxfVTClsK9cdpYfVr9egaDzC9s0cqoj_dttAJvIzsawPixCVWCJ3MN67kPI_5IJoGhf530krIrR3Zd7m12yy3rJJm7D3XIdNAH11hxPL5kIYdMqrC_-eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😀
فرم VIP از جام جهانی
🏆
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
باضریب
⬅️
3.24
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
💀
رفقااینجا عضو بشین تا شما هم سود کردنو یاد بگیرین
👇
https://t.me/+nA_vmf86vLBjNGU0
◀️
https://t.me/+nA_vmf86vLBjNGU0
◀️
💎
💯
100درصد وینه
💯
💎</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/135122" target="_blank">📅 21:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135121">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/SorkhTimes/135121" target="_blank">📅 20:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135120">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
کریم باقری:
❗️
من با باشگاه قرارداد دارم. سرمربی محترم هم با من حرف زده و خواسته که با او همکاری کنم. مشکل خاصی برای ادامه دادن ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/135120" target="_blank">📅 20:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135119">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGfzVyoR12pYxmRzr1USfgRY0-hFLrnUCN0NrmOX7cQC1MLNvyD29q_acBpekUaU-HlczKjOskH5YgSiYUltC3-xqimETjekbulyKDrlRE74pHHUOdYrQFjSzI2Esyw25g88eAWTP9OUV4Me6jLTg99cuNtqEb_ky_rArGHK6UN7s5E7_fcR0gOwL4eWCZBnExTKWW5CpDxk44cxatItTskqhS0jl2GHM7L3guQeyvFbmr76tW3oNBpuHPz2Pu11eQVNfnxYDcGFZzt4D5mVBrS-g96axeLTLuEop1FoSU99fnED11jK6O9dLrfgP0QuJ6l00soDl0mcgbSBg-BbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
کریم باقری:
❗️
من با باشگاه قرارداد دارم. سرمربی محترم هم با من حرف زده و خواسته که با او همکاری کنم. مشکل خاصی برای ادامه دادن ندارم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/135119" target="_blank">📅 20:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135118">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/135118" target="_blank">📅 18:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135117">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
✅
#فووووووووووری
🔴
تارتار علاوه بر پورعلی‌گنجی، برای حسین ابرقویی نیز اعلام عدم نیاز کرده و‌ معتقد است این بازیکن در ضد حملات حریف کند عمل می‌کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/135117" target="_blank">📅 18:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135116">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/135116" target="_blank">📅 18:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135115">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» مدیران باشگاه پرسپولیس با نظر مهدی تارتار با این چهار بازیکن وارد مذاکره شدند.
⬅️
مجید عیدی
⬅️
محمد قیرشی
⬅️
پوریا پورعلی
⬅️
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/135115" target="_blank">📅 17:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135114">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
بعد از منتفی شدن حضور خداداد عزیزی، احتمالاً محسن خلیلی سرپرست تیم برای فصل جدید هست. باشگاه هم می‌خواد یه معاون ورزشی جدید به‌جای خلیلی بیاره
❌
✍️
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/135114" target="_blank">📅 17:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135113">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
❌
فووووووووووری از فوتبال 360
🔴
لیست خرید تارتار برای پرسپولیس
🔴
مجید عیدی
🔴
مسعود محبی
🔴
علی نعمتی
🔴
دانیال ایری / محمد مهدی زارع
🔴
پویا پورعلی
🔴
کسری طاهری
🔴
پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/135113" target="_blank">📅 17:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135112">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
با اعلام ترانسفر مارکت محمد قربانی بازیکن آزاد اعلام‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/135112" target="_blank">📅 17:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135111">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/135111" target="_blank">📅 16:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135110">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❗️
ورزش سه :تارتار لیست مازادش را به باشگاه تحویل داد
❌
امید عالیشاه
❌
سروش رفیعی
❌
مرتضی پورعلی‌گنجی
❌
میلاد سرلک
✅
✅
مدیران باشگاه این تصمیم را به بازیکنان اطلاع داده‌اند و این چهار نفر اجازه حضور در تمرینات را ندارند.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/135110" target="_blank">📅 16:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135109">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❗️
مهدی تارتار: می دانستم حضور من در پرسپولیس دیر و زود دارد اما سوخت و سوز ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/135109" target="_blank">📅 16:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135108">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
مهدی تارتار مخالفتی با حضور کریم باقری در کادرفنی پرسپولیس ندارد، اما وضعیت همکاری باقری با سرخ‌پوشان هنوز مشخص نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135108" target="_blank">📅 16:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135107">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135107" target="_blank">📅 15:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135106">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
رونمایی از لیست ورود و خروج مهدی تارتار در پرسپولیس
🔴
🔴
امید عالیشاه، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا نفراتی هستند که مدنظر سرمربی جدید پرسپولیس قرار ندارند. سروش رفیعی که قراردادش با پرسپولیس به پایان رسیده نیز جایی در تفکرات تارتار…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135106" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135105">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135105" target="_blank">📅 13:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135104">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135104" target="_blank">📅 13:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135103">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
رونمایی از لیست ورود و خروج مهدی تارتار در پرسپولیس
🔴
🔴
امید عالیشاه، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا نفراتی هستند که مدنظر سرمربی جدید پرسپولیس قرار ندارند. سروش رفیعی که قراردادش با پرسپولیس به پایان رسیده نیز جایی در تفکرات تارتار…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135103" target="_blank">📅 13:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135102">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
رونمایی از لیست ورود و خروج مهدی تارتار در پرسپولیس
🔴
🔴
امید عالیشاه، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا نفراتی هستند که مدنظر سرمربی جدید پرسپولیس قرار ندارند. سروش رفیعی که قراردادش با پرسپولیس به پایان رسیده نیز جایی در تفکرات تارتار…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135102" target="_blank">📅 13:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135101">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
🔴
به امید عالیشاه، میلاد سرلک و مرتضی پورعلی‌گنجی اعلام شده در تمرینات حاضر نشوند و در لیست مازاد قرار گرفتند.
🔴
🔴
باشگاه همچنین به سروش رفیعی اطلاع داده قصد تمدید قراردادش را ندارد.
🔴
🔴
تارتار هم گفته هفته آینده درباره ادامه همکاری با بیفوما تصمیم نهایی…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135101" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135100">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
🔴
خبرگزاری فارس مدعی شده محسن خلیلی میخواد احسان محروقی مهاجم فولاد رو بجای علیپور بیاره پرسپولیس‌
😐
😐
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/135100" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135099">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #افشاگری
⚠️
🔴
به گزارش رسانه «سرخ تایمز» محسن خلیلی معاونت ورزشی باشگاه پرسپولیس در ۲۴ ساعت گذشته سخت به تکاپو افتاده و دنبال آوردن یحیی گل محمدی به پرسپولیسه؛تنها شخصی که تو باشگاه خیلی سفت سخت داره تمام زورشو میزنه تا مربی ایرانی بیاد…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135099" target="_blank">📅 12:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135098">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5Ep5DKbz7brGwndSk57tYn_tUkoanUC-dd6rt2ZziqjstdGpSqeLRn3zGT7_oH_g5SzpciWIzM8xYi3dXT1FaJCUDosMx9eYbSm3yGYgEr3m0awClyC_fBi8colY35Z9yoxG3O6qafAkCijIsTUY0InoU6XwvEVwduOvBrDBQHoiI3Ft5p8qm7uSbgLlSe7Fz8N9a4zAA5jA8Y7pXl738CxZy41U4TB9dDac2tEwJWuRvPZ7a6UMStg3fP0psjsAgX2IQ2wydPsCzG_MZzDkaYXmDuMGGFXADumq-R0mCTe05DsmwYsqiMM9k1UacB7iVaTZgCpui0tpCfWOSqXXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
برگی از تاریخ‌‌‌‌ ایران...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135098" target="_blank">📅 12:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135097">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
طبق آمار ترانسفرمارکت، تیکدری در دوران فوتبالش در لیگ برتر در پست‌های مختلف به میدان رفته است:
🔴
دفاع راست: 72 بازی
🔴
وینگر راست: 52 بازی
🔴
هافبک راست: 18 بازی
🔴
مهاجم نوک: 15 بازی
🔴
وینگر چپ: 10 بازی
🔴
دفاع چپ: 4 بازی
🔴
هافبک هجومی: 2 بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/135097" target="_blank">📅 12:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXCZEN7HJa-4p5C1Opn24h3mODyLL4BsBQYMYg2lMHNI_Kwci5a2uQv9_Hw8rRF8bgukMJJ-f1g84xlTgTmAfzbVvMN01FMqcakIxZ0mwptCA5yoBm55IJAxhzFTQhkdrzrfixbpddK11Y6kdC1BPYaIsRi5KgZ0OWnoAFBsC2MBZcAIStP4FlZsz88GOhh_SswkxcgA6FcsEfYgzygCE82VhOl0OWyvLswEyNanQD2y5ETCWTyKObbTV0SlJFTJp84oPgxS9yotEDkjeogRZSctXqC4PaT77Z4KWKv3TkL47If-H6sJkusC47QO3VsW68Lo3oJpWxJZyUu21WaPzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
برنامه بازی‌های روز نهم مرحله حذفی جام جهانی
پ.ن چه فوتبالیه امشب ساعت ۲۲٫۳۰ ..اسپانیا و پرتغال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/135096" target="_blank">📅 12:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
#فارس؛ کریم باقری تمایلی برای حضور در کادرفنی تارتار ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135095" target="_blank">📅 11:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135094">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135094" target="_blank">📅 11:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135093">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
علی نعمتی گفته 48 ساعت وقت میخوام اگه با باشگاه خارجی نبستم، میام پرسپولیس ///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135093" target="_blank">📅 10:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135092">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
اولین خواسته‌ی کادرفنی جدید تمدید قرارداد کریم خان باقری بوده و گفتن حتما باید بمونه /طاهرخانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135092" target="_blank">📅 10:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135091">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
خط و نشان مهدی تارتار برای بازیکنان پرسپولیس
🔴
تارتار:در پرسپولیس تغییر داریم چون من بازیکن جنگجو می خواهم، بازیکن باید اول جنگجو باشد بعد فوتبالیست، وگرنه فوتبالیست زیاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135091" target="_blank">📅 10:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135090">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇳🇴
نروژی ها بعد از بازی دیشب شادی وایکینگی رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135090" target="_blank">📅 10:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135089">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdbe3de490.mp4?token=taCqOv-zyAuWFkmJLGW4Cl6KN9BopmKBXhomql8RkF8IRndQAKcS4FVwnp-wExL9-3ottZKYBUcw8GrvMA0ZiJ5jyOYPZXxR5u1_94DtpsyL_wnQVKAtj0jxQ_KdccDyc3k6gvQzluVO_Bp92_ZC3PLmNIpEDpfzUDzrQYCzs5SKUrUtZb3oyF_-DzR6fumGk3nnMMHvzDiYRtM1CZ_Z7SoSuu3zG7oTsqxdo48u1kKJ00zHnTPtxxiyzUSL4946CYhzawS1yHppCqqkaZvlBshyzj03KAdVvMDqQr68b35NlUXSp9Jc1PLF3NyXlFhGJWVB5_fFbuia2hd4AxF0JqfObajZkUIMyNh6tzddmXiaAaoMrzBcFQuFk9WjaaRkFz91PHntj4OVbC6pStsnz0-Zb_HIbLL3iZ8EisB4lI5Whqzlsh5GL__oH1NJ8uGJ-iaQXXKUdc0OTun_Vu-f0QW3lLwZJo6T_AxhO0XjZ4DXGK92zWc7S31pP1tdSOZurWpnAwiou5y0cAs2C1VWws650ozZ8xlOXUiRptlfb6jypXAIsLiBItpxkALUPhmwMOws9y-BPpr7GnXAKv2LM7-0kNxH27-39aIO_VrQhEnL_MQwSAd1RAiBY4I7chBIwQ-DlkDzKKw5W7IU0XqVBBagJYFzcVKwOFd6Cnx2yLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdbe3de490.mp4?token=taCqOv-zyAuWFkmJLGW4Cl6KN9BopmKBXhomql8RkF8IRndQAKcS4FVwnp-wExL9-3ottZKYBUcw8GrvMA0ZiJ5jyOYPZXxR5u1_94DtpsyL_wnQVKAtj0jxQ_KdccDyc3k6gvQzluVO_Bp92_ZC3PLmNIpEDpfzUDzrQYCzs5SKUrUtZb3oyF_-DzR6fumGk3nnMMHvzDiYRtM1CZ_Z7SoSuu3zG7oTsqxdo48u1kKJ00zHnTPtxxiyzUSL4946CYhzawS1yHppCqqkaZvlBshyzj03KAdVvMDqQr68b35NlUXSp9Jc1PLF3NyXlFhGJWVB5_fFbuia2hd4AxF0JqfObajZkUIMyNh6tzddmXiaAaoMrzBcFQuFk9WjaaRkFz91PHntj4OVbC6pStsnz0-Zb_HIbLL3iZ8EisB4lI5Whqzlsh5GL__oH1NJ8uGJ-iaQXXKUdc0OTun_Vu-f0QW3lLwZJo6T_AxhO0XjZ4DXGK92zWc7S31pP1tdSOZurWpnAwiou5y0cAs2C1VWws650ozZ8xlOXUiRptlfb6jypXAIsLiBItpxkALUPhmwMOws9y-BPpr7GnXAKv2LM7-0kNxH27-39aIO_VrQhEnL_MQwSAd1RAiBY4I7chBIwQ-DlkDzKKw5W7IU0XqVBBagJYFzcVKwOFd6Cnx2yLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔖
منهای ورزش
🔴
جمعیتی عجیب و غریب در تهران که انتها ندارد؛ تصاویر هوایی از حضور حماسی مردم در مسیر تشییع
پیکر رهبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135089" target="_blank">📅 09:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135088">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
پرسپولیس حاضره تا ۲ برابر سقف قراردادش به احمد نوراللهی پیشنهاد بده/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/135088" target="_blank">📅 09:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135087">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4ydAv_h8aKoFf2SQUEg0MrrRpMGTcVtuDU8XMfwkBcQNkrn7J9w1zHUJWmNhfXR03fkXD8HPDfYxgyXeqMlCmGkAPkVNIVTm0eGArGaIRJg1Octe5ycWmeH_XlMTbjWTwqF0GxR26uI51kzdRAQVHehMb6Re2tN-8k-r88iV2T8uvtWllJHjhPz1xoACYzyq2socD8O1id2ra31EPrRkhxVS3RSTQAk8s4O42u1SrJFe6TFW8ArYyA4nheO6ItepzEx_lay1lgosZsi0f5gfF56cu9Z-af6dwmnFx0dhBDqYGIxbOPI_XnYh7YOOzTmhHlDOuGexh1EnMNh1_mq9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
قلعه نویی اول صبح مهمون داره
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135087" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135086">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/045d65d9fc.mp4?token=gWTiL-XrFL0NmByh-V1TaFmgOHbckJ0vIxXF1CrpPO_Ac792PztZCwlOh99ka0ACtXrN-WYbUDEU-4Sfelwe-oucxaY6GfFS_AZpqcfh3RNZaW2DKpC-h0b2H5bpzdeHEN_JLF9aBPOrcHWzJJyjIIBUBNlKDVe8LMhFlJRWQsvUSeQWiyvyz0pUAGj5NlsmUpki6YwoTVCJPt_sxGs-QmHPgkXDWv0GOriS4f1ux7IJ-rOktJUQXFP-l_08LhQej27ccUFvJETlFKA8g0u4017gX65AekbL5z3vu5jBML4J39F34RLLGchQFStiFM36KcgK2TKZamDbRnlYzhjT9hTC-DyrOcwhon8kgBtZjCe3n5PkExPtBwUzSvgrlAru7oppbFAIZIHeX5Mq4sPTNNrCxPxyEHv4zLIOK0AsyYOwhjSkVrQNqFWcCyB81_d7dXEiw-Ps42hmDLVwDexwEWtYoQbHjyOKZvljCgvZP7vd3dB-cscgtTa2tSIX_3RVsrRvjoEfLqydgz3DuBuV2BFk7nlmN4j5jAAB0gVGGtkM69A52PixIakzJbvTMYaIuv8JHYsNW7U8i_Vw33oZv9Z_5pbiFz_SG6WI__Ot_GzEHK1OYBXoPhCyfL4Zj56nbLaidCWIc7Fdn0O74ZG0VRMI8QO640EkNpDTJwloRJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/045d65d9fc.mp4?token=gWTiL-XrFL0NmByh-V1TaFmgOHbckJ0vIxXF1CrpPO_Ac792PztZCwlOh99ka0ACtXrN-WYbUDEU-4Sfelwe-oucxaY6GfFS_AZpqcfh3RNZaW2DKpC-h0b2H5bpzdeHEN_JLF9aBPOrcHWzJJyjIIBUBNlKDVe8LMhFlJRWQsvUSeQWiyvyz0pUAGj5NlsmUpki6YwoTVCJPt_sxGs-QmHPgkXDWv0GOriS4f1ux7IJ-rOktJUQXFP-l_08LhQej27ccUFvJETlFKA8g0u4017gX65AekbL5z3vu5jBML4J39F34RLLGchQFStiFM36KcgK2TKZamDbRnlYzhjT9hTC-DyrOcwhon8kgBtZjCe3n5PkExPtBwUzSvgrlAru7oppbFAIZIHeX5Mq4sPTNNrCxPxyEHv4zLIOK0AsyYOwhjSkVrQNqFWcCyB81_d7dXEiw-Ps42hmDLVwDexwEWtYoQbHjyOKZvljCgvZP7vd3dB-cscgtTa2tSIX_3RVsrRvjoEfLqydgz3DuBuV2BFk7nlmN4j5jAAB0gVGGtkM69A52PixIakzJbvTMYaIuv8JHYsNW7U8i_Vw33oZv9Z_5pbiFz_SG6WI__Ot_GzEHK1OYBXoPhCyfL4Zj56nbLaidCWIc7Fdn0O74ZG0VRMI8QO640EkNpDTJwloRJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
خلاصه بازی جذاب دیشب انگلیس و مکزیک که با ۳-۲ انگلیس برد و تو مرحله ¼ به نروژ خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135086" target="_blank">📅 09:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135085">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135085" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر پنجشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
🔗
بدون نیاز ب فیلترشکن
🤩
آموزش کامل استفاده از اپ
🔜
💰
💰
💰
💰
💰
📱
Telegram Channel
👇
https://t.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/135085" target="_blank">📅 01:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135084">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNc-D1Fa9bYffREA8Ibu0qBmpCkQ2cuQj-nQhtPvgo4OgmF7RAPz0_ml_f6UaZfujN7CkdL2RPcDL9N7lCbg9l6U8ZcThYDxFGLDYmfh_GlE6zBTXd9BqR0C0LRHVK1Z4aPjrhetQYfJ9mpj_GNFrzzORNOCv-Rv_JiR8wcRZJCLabZQV1ztslbAm55mwJG0Pc6VFQzYqlpXHv3yVrY5betS-cCkf_F0jSNwrqh853AumoEegOfJLfrnUHueQKwNU5MRHZtfrWWZlZtVseug23J0bBjR8x3qJJrS8av4Zx_udPRcN8vtXpgjnsYmgYv5FjH8PQd5uzFj1bKcIHqTug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اولین سایت جهانی برای کاربران ایران با واریز برداشت مستقیم
⬇️
🪙
سایت بین المللی و معتبر لاین
بت
❤️‍🔥
اسپانسر لیگ  فرانسه
💳
واریز و برداشت ریالی
👀
بازگشت باخت ب صورت هفتگی
📣
دارای پشتیبانی فارسی فعال
🎁
بونوس
💯
روز های دوشنبه
🎡
کدهدیه ثبت نام
➡️
L5670
🔗
《 لینک سایت برای کاربران ایرانی》
👍
《 دانلود اپلیکیشن اندروید》
❤️
https://t.me/+dukgrB6-zGsyNGM8
🔻
جهت استفاده از وبسایت از آی پی کشورهای آسیایی
🇷🇺
یا کانادا
🇨🇦
، استفاده کنید
Ⓜ️
✔️
آموزش کامل و جامع شرطبندی
👉</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135084" target="_blank">📅 01:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135083">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43875d53c9.mp4?token=FcBcBHkBS10QeCJiMompaY4gh3bGokdUlxfdsDVYNP0SCVuA_sXQRgTjVoV1-w7y5dA7EIifFiOuTmdiZnRi8od_qTTIM7DMVqTmyufX-0M_KP5Vai0TnFJZH0DQAICDQO1o-KhtTMqV9Hiz2dxxbcQLOufu2EnLE789OtkgOBGaEDdhDsd8i4R0kHAXQ36Wi-h58RdoJaUQXyrrGzzvuXk6bdzLVGjuJ8ciTo_kvePUbKrX7j7tvBCVyhb9NXbQMQLV4sWd370yEOI9XF5fE9vNYi6BcwPSWb3MIiRnyYEY5zeByqcT3hkn7PG59jeHsvTatT24hRJWFMw6x487Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43875d53c9.mp4?token=FcBcBHkBS10QeCJiMompaY4gh3bGokdUlxfdsDVYNP0SCVuA_sXQRgTjVoV1-w7y5dA7EIifFiOuTmdiZnRi8od_qTTIM7DMVqTmyufX-0M_KP5Vai0TnFJZH0DQAICDQO1o-KhtTMqV9Hiz2dxxbcQLOufu2EnLE789OtkgOBGaEDdhDsd8i4R0kHAXQ36Wi-h58RdoJaUQXyrrGzzvuXk6bdzLVGjuJ8ciTo_kvePUbKrX7j7tvBCVyhb9NXbQMQLV4sWd370yEOI9XF5fE9vNYi6BcwPSWb3MIiRnyYEY5zeByqcT3hkn7PG59jeHsvTatT24hRJWFMw6x487Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
گریه‌های شدید نیمار پس از پایان بازی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/135083" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135082">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwrFALkJdfEe8PX0zz9SEemUIvKroxraQOeu256JisyFnc60nFHcIOimWyY11QElYifGQkM_S0clxlyrHcRwRzeaHuvvp8NRDJGWZf1JjoASplrrgc0MxtZpwxbAcv5BN9WLowTf7YtdBds-dQ6K-jGNpHwHIBy9UYlU6QxtuAw3FEXaoTC5gSaEoaXkKIm_mCHmtriCzSaq82G_hwLEh4zhfyyMYwjNtZw8i29aqEn_d8TARtwvlE65_WU7GKxIuudKdlm0Q63ANhIoTLIZRxdb4jD8U_YKzhuxeQlTbJdqWlpTgG6KbC1YK53m9ByPm-mZI7z2fJYrS--jSnrefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇸🇦
پایان بازی | 1/8 نهایی جام جهانی 2026
🇧🇷
برزیل
😃
-
😄
نروژ
🇳🇴
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135082" target="_blank">📅 01:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135081">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba6a7f41c4.mp4?token=YGkD1OyQaR_pWxSlA6-UxVLcm-fjp_kOM_InFHuM27np55-eQLKg88yinTNl2FSvnK7FWND93OA-fzAwgmuBOGmVzpqBuU4qD3sYYwsiORIIxiQsBIPKKfLyZqKSTH82-FcJCRuProlEQYzmKRPYxIFggKfvd0x-RIZa4D16f-GKPYIMN2Xc5r6CzWKWUwk6hIoOxLEJtRAqUo4fvmNAjh880OgSDmBBnjRy43uV7cA6sMlQ-N0s67pZU7De_eRfHQDpWlPut6d4rhgJ64K3AKb3O59KJtVZFd_g7JEgNJuuGqrt7if3cENKz2map7oj30DDvyKYJMJdbVAEZXK-PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba6a7f41c4.mp4?token=YGkD1OyQaR_pWxSlA6-UxVLcm-fjp_kOM_InFHuM27np55-eQLKg88yinTNl2FSvnK7FWND93OA-fzAwgmuBOGmVzpqBuU4qD3sYYwsiORIIxiQsBIPKKfLyZqKSTH82-FcJCRuProlEQYzmKRPYxIFggKfvd0x-RIZa4D16f-GKPYIMN2Xc5r6CzWKWUwk6hIoOxLEJtRAqUo4fvmNAjh880OgSDmBBnjRy43uV7cA6sMlQ-N0s67pZU7De_eRfHQDpWlPut6d4rhgJ64K3AKb3O59KJtVZFd_g7JEgNJuuGqrt7if3cENKz2map7oj30DDvyKYJMJdbVAEZXK-PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
خط و نشان مهدی تارتار برای بازیکنان پرسپولیس
🔴
تارتار:در پرسپولیس تغییر داریم چون من بازیکن جنگجو می خواهم، بازیکن باید اول جنگجو باشد بعد فوتبالیست، وگرنه فوتبالیست زیاد است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135081" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135080">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
نروژ دقیقه ۸۰ گل زد به برزیل و یک بر صفر. جلو افتاده ...ده دقیقه تا حذف برزیل از جام جهانی
🤩
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/135080" target="_blank">📅 01:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135079">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
تارتار : ما تو دنیا هم نشون دادیم با کادر ایرانی میتونیم مقابل بلژیک و مصر بایستیم و به اینا نباختیم، شاید یه مقدار مقابل مصر شجاع تر بودیم صعود کرده بودیم، کادر ایرانی نشون داد چیزی از مربی خارجی کم نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135079" target="_blank">📅 01:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135078">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
مهدی تارتار: من می‌خوام یه پرسپولیس جنگجو بسازم و اسم ها برام مهم نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/135078" target="_blank">📅 00:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135077">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">✅
✅
علی نعمتی گفته 48 ساعت وقت میخوام اگه با باشگاه خارجی نبستم، میام پرسپولیس ///خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135077" target="_blank">📅 00:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135076">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
مهدی تیکدری: وقتی رفتم با استقلال قرارداد بستم هم پرسپولیسی بودم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/135076" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135075">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
تارتار : تو نفت مسجدسلیمان، پارس جنوبی جم، ملوان بندرانزلی، گل گهر سیرجان بهترین نتایج تاریخشون رو رقم زدم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135075" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135074">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
تارتار: از انتقادای منتقدین که خواهر برادرای من هستن حتما استفاده میکنم. من ۱۹ سال تجربه دارم فکر میکنم شرایط اینکه به تیم محبوبم کمک کنم رو دارم. از پیشکسوتا هم رخصت میگیرم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135074" target="_blank">📅 23:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135073">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f1df6e4b.mp4?token=adDNrBz8dc4Job2bRHS4zaftdlXLiLjCasMs06_hzigxIYm3CvvNWbCMm0YxyU1y_GzEbgpu4bsGFiyc2QqAWXpxKmvuzrHwtaq0dcQdUS7bQcZ-GOqAG0uiuPJbKJjun-gPvinwzSm0IitkIfq6r4mMFT6GSzJRD-UcCAsO8pegyihlvgaly8mnesZf42t_BAnTSOaAAw-JoJQDfyzWnqk8VGmvRz7XIl4-MKAQ7H0SN8cmKQ8pc0k9FZRD8WbSWaZTDLkYEtZmrID_KQxlcnzFReuWrj3F52a0C-zOeq-lAgfJptv2l-0LUvK6Ccws9DbQ_VIRyGtxT1tyDFUcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f1df6e4b.mp4?token=adDNrBz8dc4Job2bRHS4zaftdlXLiLjCasMs06_hzigxIYm3CvvNWbCMm0YxyU1y_GzEbgpu4bsGFiyc2QqAWXpxKmvuzrHwtaq0dcQdUS7bQcZ-GOqAG0uiuPJbKJjun-gPvinwzSm0IitkIfq6r4mMFT6GSzJRD-UcCAsO8pegyihlvgaly8mnesZf42t_BAnTSOaAAw-JoJQDfyzWnqk8VGmvRz7XIl4-MKAQ7H0SN8cmKQ8pc0k9FZRD8WbSWaZTDLkYEtZmrID_KQxlcnzFReuWrj3F52a0C-zOeq-lAgfJptv2l-0LUvK6Ccws9DbQ_VIRyGtxT1tyDFUcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
واکنش مهدی تارتار به حضور کوتاه مدت وحید هاشمیان در پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135073" target="_blank">📅 23:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135072">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e534deb415.mp4?token=RWYTfLfqHbEKLvqbIN33LZnNtU67bV-B8kv6YW2O0uPBjfrxwtzpuJAVhQL_-ucZ1q2fLln-p10VY7dD35RCqiRWN2gVhE2qWjBoyg_kKU7UXKu-3Gnqyhb4Rt_3lUKpMUM5rXCmRd1YHUscYWD0lHMWZy4M4ciaFbFukdXNRNMmhn2e4HmEtUJMknT-5nz-Fd7VVYCMy4smMPVG4XcUkPpC1WtdhmMV6DnTOiuaoQYLy2Sr0v6NfXvXZsXBOtbM67drL8ucY_dhZPQI3pw2_tuMW0s3nRFR0XNn4zB7mbsp7fK1167PAscNTi8m0MgQK47wMI814eSAFD5ZWLpEtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e534deb415.mp4?token=RWYTfLfqHbEKLvqbIN33LZnNtU67bV-B8kv6YW2O0uPBjfrxwtzpuJAVhQL_-ucZ1q2fLln-p10VY7dD35RCqiRWN2gVhE2qWjBoyg_kKU7UXKu-3Gnqyhb4Rt_3lUKpMUM5rXCmRd1YHUscYWD0lHMWZy4M4ciaFbFukdXNRNMmhn2e4HmEtUJMknT-5nz-Fd7VVYCMy4smMPVG4XcUkPpC1WtdhmMV6DnTOiuaoQYLy2Sr0v6NfXvXZsXBOtbM67drL8ucY_dhZPQI3pw2_tuMW0s3nRFR0XNn4zB7mbsp7fK1167PAscNTi8m0MgQK47wMI814eSAFD5ZWLpEtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
مهدی تارتار: می دانستم حضور من در پرسپولیس دیر و زود دارد اما سوخت و سوز ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/135072" target="_blank">📅 23:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135071">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
تارتار: ما برای اینکه یه تیم جنگجو و دونده داشته باشیم نیاز به تغییرات داریم.. یه بازیکن اول باید جنگجو باشه بعد فوتبالیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135071" target="_blank">📅 23:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135070">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
تارتار: خیلی خوشحالم شرایط طوریه که مربیای داخلی هم میتونن به تیمای بزرگ برن. از هوادارای پرسپولیس میخوام بهم اعتماد کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/135070" target="_blank">📅 23:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135069">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
اولین واکنش تارتار به سرمربیگری پرسپولیس: 18 سال تجربه دارم و می‌توانم به پرسپولیس کمک کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/135069" target="_blank">📅 23:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135068">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
🔴
رسمی؛ مهدی تیکدری، مدافع راست ۲۹ ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/135068" target="_blank">📅 23:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135067">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
مهدی تارتار: فکر می کنم بتوانم به عنوان یک سرباز به پرسپولیس کمک کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/135067" target="_blank">📅 23:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
مهدی تارتار: فکر می کنم بتوانم به عنوان یک سرباز به پرسپولیس کمک کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/135066" target="_blank">📅 23:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135065">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HjC0I-db5-28YoFaYWM_2U_xIPWnv1uXagVyfHKy-qe9bQWCtLIO9lKR3RCJS9lZusK0-EM4t281VqgHvE6ZtT5sb671LoyWmHOiQRdDNBlRH8YmQNqXcK24qYv_V3PgxMmo2Bqpw_RILvqNuRvaIWVU4eJmtYtq26fA1WRndoayb4lmBFb5ESaWML5LGohLMa6Wq1oRC-xrD6lWe4_BZW6cmJ26eRfA5OvJvMDhMegRIsY1LEInx4adYy3k-fl68iZ1qgmT8gbPTbcxzzgJ5iDvQ8_JGqKcSAjyE57idUC6qULkQVFLt6fgxSy1a-dWqEoWYgdzkM8l_E4tRYBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
باشگاه گل‌گهر از سیدمهدی رحمتی و جانشین تارتار رونمایی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/135065" target="_blank">📅 23:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4dD-A9WJunNJuyLZYc2KZLjFQDTFh_VWfrOE-zHYfOsLHpzCU7FTScOfnIeS8AfGTaDt138WDPqrDcSFrwQigWjNRwDmezNuQotY2Oz5kRMNJ99VdiD4-AeY88a_9NlwEF19OW0rQpMdH1psKYbfQFWT6_Jr5QIEjTpXegkG_aAGPecsqCIbFIM8gdu63lzHsPvLcn7RjGXbfgRHA97Go7xWLLF7gQVCOhY2YyuJayqwtbWALOJYXeMPVj1iTSIZGzAsce8fugCyVtq04cFCMajx-5bpUbMBgIkt-8LHwQsnnX6ymBaxeimcrgYBGUkM5BMWFbb1EBq4iERN09riA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
اینانلو عضو هئیت مدیره پرسپولیس در گفتگو با فوتبالی : از اول هم سرمربی داخلی می‌خواستیم
📚
به دلیل شرایط باشگاه از جمله آسیایی نبودن تیم به این جمع بندی رسیدیم که سرمربی داخلی انتخاب شود. چند گزینه داخلی داشتیم و مهدی مهدوی‌کیا جزء گزینه‌های ما نبوده است</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135064" target="_blank">📅 22:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135063">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
رامین رضاییان بعد از وینیسیوس جونیور بیشترین جایزه‌ (بهترین بازیکن زمین) در این جام‌ جهانی را گرفته است. همچنین رامین رضاییان با گلی که امروز زد، به کافو اسطوره برزیل رسید و با 3 گل، گلزن ترین دفاع راست تاریخ جام جهانی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135063" target="_blank">📅 22:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135062">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
پروژه جوان گرایی تارتار تو پرسپولیس
✅
پوریا پورعلی 30 ساله
❗️
جایگزین میلاد سرلک 31 ساله میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135062" target="_blank">📅 22:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135061">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
پروژه معمولی سازی پرسپولیس آغاز شد
❗️
پویا پورعلی هافبک دفاعی گل گهر سیرجان به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135061" target="_blank">📅 21:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f006bce86a.mp4?token=WmkzJHiCubPB6ImRveIz06g-_96XxScAcIaVY8HNWUCDWf3StVCZcpkx2vjcMuWQtoIOaAqrzx_eNIDD6SBnLCZyJ0RRg2R1X33YSf314g1GKCyY8CxCsqe5BEX0qShmYFckm4WRcM8ykeX7YZO97in9eEgYM24UQ-lpGUPwoma3B-0UiAfFc-51PosXTWaEqKfiyfokDbTfssjVlmcIlqpzoRGhK0-jP4ndTQRfAieOib2NzjMBDv-chMRd4kLh7HBuQ-goJur33-ANedbQbZjCmclUUj6HvtS6bNQs1eT50MyjXGnrpGPjtXhce2HJ1GoEWqQ_DYHZ16BkEPKpaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f006bce86a.mp4?token=WmkzJHiCubPB6ImRveIz06g-_96XxScAcIaVY8HNWUCDWf3StVCZcpkx2vjcMuWQtoIOaAqrzx_eNIDD6SBnLCZyJ0RRg2R1X33YSf314g1GKCyY8CxCsqe5BEX0qShmYFckm4WRcM8ykeX7YZO97in9eEgYM24UQ-lpGUPwoma3B-0UiAfFc-51PosXTWaEqKfiyfokDbTfssjVlmcIlqpzoRGhK0-jP4ndTQRfAieOib2NzjMBDv-chMRd4kLh7HBuQ-goJur33-ANedbQbZjCmclUUj6HvtS6bNQs1eT50MyjXGnrpGPjtXhce2HJ1GoEWqQ_DYHZ16BkEPKpaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پروژه معمولی سازی پرسپولیس آغاز شد
❗️
پویا پورعلی هافبک دفاعی گل گهر سیرجان به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/135060" target="_blank">📅 21:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135059">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
میلاد محمدی تا این لحظه به پیشنهاد تمدید قرارداد باشگاه پرسپولیس جوابی نداده است و اولویت او لژیونر شدن است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135059" target="_blank">📅 21:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🟥
علی نعمتی در آستانه بازگشت به پرسپولیس////خرمی   پ.ن فقط این و کم داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135058" target="_blank">📅 21:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhl8lmVwCsOK3op0GU4PKijXD3DkBngFJJuR1dwhAdrNa_yo1kPr50dijlZz2mKr9u1xJOleDn_QbKODpnRnugBRQbfAv2_cGrg9WD4ogl62ai5HBdW9UQoLghEyKT8maqF_FuWj4PZlyNTE6Jik2Xcm2NaENncZzdN33T-X9d9xcxcIkdORXqLF8Fm-1S0YqRxx1voyk00oivS-kE0HHMa_kxVgibfmOlvPSyyC-rmyuFLTy8fCJ00hIcXeI2wDrwV-9iWXPZggaAprdjV1wV05Y4O4vEJon6DxxypS14jGn1aScK42PbL0EPSa-sze7Ls3i2Q5vDlO7m_x9uYO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
علی نعمتی در آستانه بازگشت به پرسپولیس
////خرمی
پ.ن فقط این و کم داشتیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135057" target="_blank">📅 21:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135056">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXhZMi-J4XO2RclODlW6OoCeoONRT5EmHCN_zB_wWiVjbWcOmFejCbsys2qog3Z73scrJBnFcxOWK0jdybYsennf4qyXZfkOs9q8X5kgjO8kXQDRUDyTzD47LmlL_is0JcZRTA9QYdfki-rvTMbzuwrntc7PZq0vKfWnluiEc5xwMj9CrPjy0f9FuA6QtJYYCEW9b8RZ1ivj0u3fYHhG2YMNwvBTHavhy58z7OmnBzl8MbCKYwybvVYF1Jcu4kt7B3CrSUTn50v0gbF25PcsfgZsZGyi0jGVumilzDoQ_xrQff_sYqDnNV5oXZo3x6Fn1QsHhOIdDoL8NAE0HrU4RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا، داخل بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه!!
❗️
پ.ن سیاست آوردن تو فوتبال و ترس از آمریکا و ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/135056" target="_blank">📅 21:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
پورعلی‌گنجی، عالیشاه، بیفوما و گرا تا حد زیادی جدایی‌شان از جمع سرخوشان قطعی است.
🔴
کاظمیان، شکاری و سرلک نیز مهدی تارتار بعد از بررسی وضعیت آنها تصمیم گیری خواهد کرد. / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135055" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135053">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافقات با مهدی تارتار انجام شده است و باید تارتار رو رسمأ سرمربی بعدی پرسپولیس بدونیم!
📚
مهدی تارتار یک دستیار اسپانیایی انتخاب کرده و با خودش به پرسپولیس میاره؛…</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/135053" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135052">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135052" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135051">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6-IQfatHb7R15L4q9bJTOp4IEpIuGrlLVDC48IaqN8jpc2jT-_6yosBqE-TWlS0MoyUcPfLD1WaoXR5-7Za-YvPfJdsCXt5JYmAbDNGBzRvOHrFEkenzW4YLenjY7CRIh-a6DhVEFqlGqJ8klFjF7yWodFQonyDUgSWE7_O6B61lu6nl9s3ElXaiGhBI6VzKsm-5nFQyji9N0Y7KkpveuTE3dAfsoeiyAxxBqiwJS7QueBo-JFhERz5JIXgTS0HFt4u3FRdkKhIgwP1lF3TGMUjG6lA88NNF-ruBTnB07a73Pk045Gki9_EApb4dUm1FkL3tagopZiRM1bZooS6LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135051" target="_blank">📅 20:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135049">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join
Join Join Join</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/135049" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135048">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rHkrRIBh-ozmU_x_HdyruoIUevEiYohFy-V3ExMl1738ZDBEe1J9o-xE3OFVBS1hkJL1kLhhoS7vYtuFxZhlqkffWoe9ImhF7o_OJ5UsaqcYgYsNKUTAj1QsnRjBve_qb97L2oZPEylypVe05r2VqIkzdLN6CDlQIw6bohKU2x2BpQcnP880Vu1gtzXqQj7Bq0Ri7Kh5eG9ZIOCpk_tMlZF6a1xYbMiayQfjMsmioFL6mqgo4fUWr2RjTdUMCYnXjH7qV1Hc5nHZm-KIx2BKMZGvtVQ4X422P0_Qvzm8XwblREUa-NL9qLnNSmzFL7avmGtJI-fYbsWs44oZpO2Mrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکس عالی برد شد
❤️
☑️
✔️
@HaJFixed</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135048" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135047">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/135047" target="_blank">📅 20:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135046">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5iB2egiRYw7rfIDKF0mhknRH4qcuCUpKp-m_KohzcXs_BZTyE2j0o5ZQB77z5U9HVYex1ui4X515-AsOvm032bvKvtgxHYJTaPx0IcFzHT7ExUsC1k3Nt-5Z8uXCOZJB00tv8OWU2Y--mvFmu4IT_wRi6WULF0eTs_uS3atzkyaSP6Kep1hQcqL-EiKY3hm-drfnhiOFdLi4AFncxUbMWVrbJoUw-2i72aotf9yK1Kbiedn-0Mdcfunxo4hfL_P--peXG_AUuz9dPdiI_vhrVLfOPEBSycDl8PztmWy4WlayJBVTNGbu0ECiAyIn3zxS7yp972wBLXbS5um6hmU_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جواد نکونام با گل‌گهر به توافق رسید و جای تارتار و میگیره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135046" target="_blank">📅 20:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135045">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135045" target="_blank">📅 20:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135044">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❗️
کسری طاهری و پوریا شهرآبادی به ترتیب دومین و سومین خرید باشگاه پرسپولیس خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135044" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135043">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135043" target="_blank">📅 20:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135042">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✅
✅
سه دستیار تارتار معرفی شدند
🔴
حسین اینانلو به عنوان مربی دروازه‌بان‌های پرسپولیس فعالیت خواهد کرد. اینانلو با ۱۸ سال سابقه مربیگری و دارا بودن مدرک مربیگری A آسیا، یکی از مربیان باتجربه فوتبال ایران به شمار می‌رود.
❗️
وحید فاضلی، که سابقه سرمربیگری نساجی…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/135042" target="_blank">📅 20:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135041">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
اولین بار گفتیم تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135041" target="_blank">📅 20:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135040">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/135040" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135039">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKDXLX1HUN4ydN4pFFduu0ecJDYzTGvWsdS1L1RV2yi9b6vBDuuB1GdGG_3mTvwUMxQXQWW3wwho6sMNwRS1rmH5N-yzJEFVbF9I8eRR5_5yT9nTy1zYYgofIuxXIEObjQjQaagOrUBfw8D1wNs0_BxCph09Ub47LYVWUCZSj2MXydnATQxGFu6nmy3rUps_ac9f5A2_SJV6G1tRvaXkKq0EqrNY8PkD4kOC8YY47VHScZe1PezaCj7k6qgKmi_Epbn0f-ZFDnJgRsh6S8czvQzFm4X5NmaL6BoGJ80xZX9ryKuqNT0URaiWuQvJbFtlH4lzNbw28xQKBKaKIqEPqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یاگو به عنوان مربی بدنساز فصل آینده پرسپولیس انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135039" target="_blank">📅 20:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135038" target="_blank">📅 20:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
🔴
رسمی؛ مهدی تیکدری، مدافع راست ۲۹ ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/135037" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVYwLUw4njX46_6de5lz2KCOlhrC4AdSTDcUUPKboYBw6y1AQQvfUm3xH0_Wx6nw3l61T062VoXsjrjLZcKFoMIVDHw0g1wDVhneX1XbkaM-sueM3Ii7y2M97ykw5Pe9wnAFQt8eulSrPbi6MdJAw0niGFjBbEbKy_hmLGORxy7kp7_3Q8eyD3e2AdIZrYjuoHg1c6Xd0_1avyQZvBN3jSkkL7PwNqumdS6GAsw-_7N4tdjPZ9ODbj7yUFuVmBKD01coVEQrCO5UxMN4eno2MwT7okBhy2s59FM8koNY6GPSNiMwsvbPVtmTemhhofMwne665kdeCcOfUqswzPV4BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اولین بار گفتیم تمومه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135036" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔖
🔖
مهدی تیکدری بزودی رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135035" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❗️
❗️
فوووووووری
🔴
علیرضا محمد مدافع سابق پرسپولیس به عنوان دستیار مهدی تارتار انتخاب شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/135034" target="_blank">📅 19:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135033">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🔴
یک سرباز واقعی، ستاره متعصب و جنگنده پرسپولیس؛ بازیکنی که برای لباس پرسپولیس، سر خود را جلوی توپ می‌گذاشت.
❗️
❗️
مدافع محبوب هواداران پرسپولیس، امروز ۴۹ ساله شد. تولدت در قلب آسمان مبارک، "داش علی انصاریان".
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135033" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135032">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: تارتار از هفته ها قبل سرمربی پرسپولیس شده. حتی تارتار دو روز پیش زنگ زده به آریا یوسفی و گفته پاشو بیا پرسپولیس
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135032" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
❗️
حقیری :علت جدایی خداداد عزیزی از پرسپولیس مشکلات مالی شدید باشگاه اعلام شده است!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/135031" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
مهدی تارتار سرمربی جدید پرسپولیس خواهان حضور پویا پورعلی و پوریا شهرآبادی در پرسپولیس شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/135030" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✅
✅
مهدی تارتار تصمیم دارد چند بازیکن از گل‌گهر را با خود به پرسپولیس بیاورد. در حال حاضر تنها انتقال مهدی تیکدری به پرسپولیس نهایی شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/135029" target="_blank">📅 17:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔖
🔖
مهدی تیکدری بزودی رونمایی خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/135028" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135027">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🏅
مهدی تارتار سرمربی پرسپولیس شد!
🤫
دیشب به نقل از مدیران باشگاه اعلام کردیم تمام شده و ته دیگش رو هم خوردن…دیدید که امروز رفت باشگاه و بست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135027" target="_blank">📅 17:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135026" target="_blank">📅 16:54 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
