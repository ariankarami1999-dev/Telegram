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
<img src="https://cdn4.telesco.pe/file/t0KcSQto0wd6VIETfBSci394CBkk6nabhXGRqwlh9amFdrLD1RNalRlLL8avjZzsxftQ7_m7_InDfoyTLThxc7EyTDMFy5HM8z_vASGN5iKyh6pVAcr4IEMaIt0p_lBnrbIRTrMThNB4l_4l-pddgBAV7-imVOCMpxGZh-RaBugwynhA7nMPDLAFbSMq6y0av9IAiQ5oGpwZFz48nMkpd5KDBU_4bVqPW14x6TR_CN4xB-PQwC5LQa2ccCXpHhxap1Vto5JeUImlYY5yhIj_9Jl15nDFGNJQxvqRFNj2ARlD0K0FEqKB-r7DuUnwsKWiImXQUjXsX2UmueUAyACOog.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 18:51:00</div>
<hr>

<div class="tg-post" id="msg-134025">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/134025" target="_blank">📅 18:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134021">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس مذاکرات با دراگان اسکوچیچ به سرانجام نرسید و اسکوچیچ منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/134021" target="_blank">📅 18:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134020">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/134020" target="_blank">📅 17:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134018">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
به گزارش خبرنگار قرمزآنلاین، مدیران باشگاه پرسپولیس تاکنون در دو دو نوبت با دراگان اسکوچیچ وارد مذاکره و بر سر کلیات قرارداد، تقریبا به توافق دست یافته اند. مانده جزئیات قرارداد بندهایی که هنوز به توافق نرسیده اند. دو طرف در حال صحبت هستند.
✅
البته برخی می…</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/134018" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134017">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❌
❌
قدوسی : با یه مقام ارشد باشگاه صحبت کردم، بند تمدید اوسمار فعال نشده و غرامتی قرار نیست بهش بدیم
❗️
حدادی و خلیلی در حال انعقاد قرارداد با اسکوچیچ هستن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SorkhTimes/134017" target="_blank">📅 16:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134016">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
🔴
قدوسی : پرسپولیس و اسکو به توافق کلی رسیدند و فقط دو بند جزئی مانده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/134016" target="_blank">📅 16:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134015">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
فوووووووووووووری
🔴
گفته میشه اسکوچیچ خواهان دو بند بسیار مهم شده
✅
1_ حق فسخ قرارداد در صورتیکه جنگ بشه!
✅
2_ اختیار تام در نقل و انتقالات و انتخاب تیم مدیریتی (سرپرست) و رسانه ای و کادرخدمات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SorkhTimes/134015" target="_blank">📅 16:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134014">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
آخرین خبر از روند مذاکرات پرسپولیس با اسکوچیچ
🔴
مذاکرات مدیران پرسپولیس با دراگان اسکوچیچ سرمربی سابق تراکتور، در ترکیه ادامه دارد. پیمان حدادی مدیرعامل پرسپولیس، محسن خلیلی و علی اینانلو در ترکیه حضور دارند و در حال مذاکرات با اسکوچیچ هستند.
🔴
برخلاف برخی…</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/SorkhTimes/134014" target="_blank">📅 15:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134013">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
خبرنگار الجزیره: ظهر امروز به وقت محلی قرار است مراسم نمادین امضا و مبادله متن توافق مرحله اول میان دو هیات ایران و آمریکا برگزار شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/134013" target="_blank">📅 15:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134012">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipE06O0XCJQMlgEz-V-XcIY1sFmoTf6m0wcHOIStQBNT5o-nGNJ6PMSAPIhjB-tQ5BIZs40uFsojtBeK0oQzfPDPErqh6zoT2UiM2ETZEsiCkQlHZV3S-4uR8fbJcNVi3bxnsLqTml0iWD2_RwCRlq3toDlcQf7pPWvzXj1cYMGxcGeNk4RjUyQtM-qZd7j6-hqPQUMe4MiyDP8KVEdXbxlK_OI1FQmM6KRqZ3CVO7e-JEcB40fP_WfGvBY1Mh0w4jfIHrwH-TFMaOuz-P8_kG4gv2GOXJfWbKNrscSDrj8juJsWXVhtInq1T9nqoQDPawWOcqlD9vdrU_jmpxbwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇧🇪
غیررسمی: تروسارد از ناحیه کتف مصدوم شده است و احتمالا به بازی مقابل ایران نخواهد رسید
❌
پ.ن فکر کنم تا شب که بازیه کل بلژیک نرسن به بازی
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/134012" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134011">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qb_38PEX_kGGQ7WT43X3pJXjIaL-AjgpcTGzUOjjEzRRDDgUAAxgG0SaWWM-Z95-T9_oDvHTKDMxdWDFuERlxchbGdKd1p_o_BF96tfAYAIMASeOUNfUlMf4ocUPh-4QaS1eCmUgRvAL47GNEsxC1vkJe2LXRKXeiwChIBKzbXPHCWn1JfV7Ii3E1jlgOvqqkX_b9NESd4ZkmSAc0s1aMaTKQMq1qSwfMNgc4bcoZsFdnlmxF0HZIgtVq_c3tSmCemwPkLy4Uj-NmGDMblcqFArO9J3krGFAU3XXTA41t_IAY_cIttVvkGSPbIK8VGfYd41N3nJze24Y6oH9DCU2wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووووووووری / آنا
✅
پرسپولیس با اسکوچیچ به توافق نرسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/134011" target="_blank">📅 15:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134010">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⚽️
خداداد: هنوز با پرسپولیس قرارداد امضا نکردم
💢
درمورد اسکوچیچ هم از نظر فنی و اخلاقی واقعا حرف ندارد؛ هم در تیم ملی و هم در تراکتور نشان داد مربی قابلی است. اگر پرسپولیس او را جذب کند برد کرده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/134010" target="_blank">📅 15:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134009">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5ynILuyA3ZD0Cbixt6WoyrabNk63TQtZWSRa2EFw9EJPRRGW5jE5AfE3lLhAkoU5I-BXFjamvZ9YBRIIRZI1173ZmsEI_GRP9wIIzWezkMWKJnaJ8OGvXVmE3HV584_XrmbKDy-yWzfKqK7IxateCr5EoBWlMhm63u0TSzk-VcAwvLpZZBRKlxZ5lpeTAr5HvXbE8rNzcmrxrBeAYjuGyCsRtaCDinbvLCuGrQ7B9dCFgZMVecwjE0umkXtwyGc-ofbk3poHanjq0sj57HLm_2IJlTnzxyAiUTsX5l8eINe_QdjD_eGL2h_mxYyGssGvOS1KXJ9xuF7o5GSeJttmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهراب بختیاری زاده با عقد قراردادی دو ساله برای بار nام سرمربی استقلال شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/134009" target="_blank">📅 15:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134008">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
🇮🇷
برگزاری تورنمنت سه جانبه برای مشخص شدن نماینده ایران قطعی شد
⬛️
طبق اعلام کارگروه متشکل از اعضای هیئت رئیسه فدراسیون فوتبال و مسئولان سازمان لیگ، در صورتی که کمیته استیناف اگر تا 31 خرداد (امروز) رأی کمیته انضباطی درباره 3 بر صفر شدن بازی گل‌گهر - چادرملو را تأیید می‌کرد، گل‌گهر به‌عنوان نماینده سوم ایران راهی لیگ قهرمانان آسیا 2 می‌شد و اگر تا این تاریخ رأی این پرونده صادر نشود، یا رأی به سود چادرملو باشد، برای معرفی نماینده سوم ایران تورنمنتی سه‌جانبه بین پرسپولیس، گل‌گهر و چادرملو برگزار خواهد شد.
⬛️
به این ترتیب و با صادر نشدن رأی دیدار گل‌گهر - چادرملو، برگزاری تورنمنت سه‌جانبه بین پرسپولیس، چادرملو و گل‌گهر قطعی است و تیم‌های پرسپولیس و چادرملو باید 5 تیرماه به مصاف هم بروند و برنده این دیدار 9 تیرماه رودرروی گل‌گهر قرار خواهد گرفت تا تکلیف نماینده سوم ایران در آسیا مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/134008" target="_blank">📅 14:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134007">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEodt0Kg5pdB2-UE_eeY8VA2nnXuQG-ypa6pgKI2Gseis-Bg9DcYvbCueuY3fzdz-fBQlRzpoC_xxrvnzjZWxwLxBmKritz5BERrUyAgMGXy2f7AAgGFW9dmjxv9Eh9qrIdAVE9Ssr6LrW1jUIuPwi5RVOcDaWPNCxNKRBHklWpU9eoV57aeMkpW2GlorEdgNdh_byo-GOX5jORRI9aIvyXcglLLUNVwM_NLqppTDzufnH0JAtO21Y6vlFlsFswrKfCwMMkwdFiusbNf8UXpunP73he6eXjdod3C7YC809Wxsa77Xfh_rkuzh22crcNNsCsbHzwNeDswmUEO2FSQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🔴
Belgium -
⚪️
Iran
⚫️
جام‌جهانی گروه G
⏰
یکشنبه ساعت ۲۲:۳
۰
🏟
استادیوم سوفای
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/134007" target="_blank">📅 14:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134006">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqX8k3l6ojpJp5f9hP-57rxW7B4bLDtPEyg9Vd6wIQrslKL4WQV2kL3ytr1k4lCzHtVcl6T2F_LiaE1myg4_ZctJheqAgNkcY1nS2JJT_uxrp2qHEl4v0fbNo1G-PAJXBUcs-abU4PBevpTo3T0p9KeB7lT6vI29rm3dall2KzteooezQknKLBuSNZ4y-UcbzOwvFyMmkp7ew61qbZAGGuR27H69pmsnZnSUa5hFCCAPedOrDiFN2mKeiYMJjJCbSiI1ZDISDIYeKyQA16tx502OibWBIMuuJarq5j5t3LiduOczO9oi794nYRG8U0Z3rzarTZs16cuAzOth0RLZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آخرین خبر از روند مذاکرات پرسپولیس با اسکوچیچ
🔴
مذاکرات مدیران پرسپولیس با دراگان اسکوچیچ سرمربی سابق تراکتور، در ترکیه ادامه دارد. پیمان حدادی مدیرعامل پرسپولیس، محسن خلیلی و علی اینانلو در ترکیه حضور دارند و در حال مذاکرات با اسکوچیچ هستند.
🔴
برخلاف برخی اخبار که حاکی از توقف مذاکرات اسکوچیچ و پرسپولیس است، این مذاکرات ادامه دارد و احتمال توافق نیز پائین نیست. همچنان مذاکرات در خصوص برخی بندها ادامه دارد و در صورتی که در برخی شروط به توافق برسند، احتمال توافق وجود دارد.
❌
همچنین در خصوص فعالسازی بند تمدید قرارداد اوسمار و احتمال شکایت او از پرسپولیس، مدیران پرسپولیس مدعی هستند مهلت فعالسازی بند تمدید قرارداد او دهم اردیبهشت‌ماه بوده که در آن تاریخ این بند فعال نشده و قرارداد اوسمار تمدید نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/134006" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134005">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
جنجال بالا گرفت؛
❌
پاسخ باشگاه پرسپولیس به صحبت‌های تاجرنیا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/134005" target="_blank">📅 13:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134004">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZYhMRJJnpVqsoCB_3DaaVmJ2WlGiZ_sLQyH09JkNtC1fOCLk0w9V-HqiVafNd8RzhB44MCX0FMLiEty7CxeNHnqEqaJ64Nq5q7QITaCoWep-YuK6aDKP802ZXRVjyTbJ5VPOlueAJ7sBZwjuj3o28xQbcKMY_ItnDCeUokc2sYfeHzqjtj6YEMT0H3fbDUzZR5xg2bsMxjyEGR1zUhWQahnCRIcAimg2Z_MSqQ9fqv9lj1cz3MRBmFWFAF0sSlrklFzAFedZycClZhicil9NQsvBhOhYwVa74VqQag6D6ccodROvEJ_8OMmBORIiapTXQU2acM7Npv2kDOTOF6ASg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تاجرنیا: جام قهرمانی رو بدید به استقلال دیگه  واسه سهمیه سوم هم جام حذفی برگزار کنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/134004" target="_blank">📅 13:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134003">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
مذاکرات پرسپولیس و اسکوچیچ بدون توافق به پایان رسید / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/134003" target="_blank">📅 12:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134002">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
فوووووووووووووری
🔴
گفته میشه اسکوچیچ خواهان دو بند بسیار مهم شده
✅
1_ حق فسخ قرارداد در صورتیکه جنگ بشه!
✅
2_ اختیار تام در نقل و انتقالات و انتخاب تیم مدیریتی (سرپرست) و رسانه ای و کادرخدمات تیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/134002" target="_blank">📅 12:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134001">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
با وجود توافق اولیه بر سر مبلغ قرارداد، طبق پیگیری خبرنگار تسنیم مذاکرات بر سر دو بند همچنان ادامه دارد و توافق در مورد آنها تا این لحظه حاصل نشده است. طرفین امروز بر سر این دو بند که مربوط به مسائل مالی نیست؛ مذاکره می‌کنند تا در صورت توافق، قرارداد رسمی…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/134001" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-134000">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">⚡️
جزئیات قرارداد دراگان اسکوچیچ با پرسپولیس:
⚡️
قرارداد دراگان اسکوچیچ با پرسپولیس برای دو فصل تنظیم شده است. اسکوچیچ فصل اول، یک میلیون و 200 هزار دلار خواهد گرفت و برای فصل بعد 10 درصد به آن اضافه می‌شود.
⚡️
در قرارداد اسکوچیچ، 500 هزار دلار به عنوان پاداش…</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/134000" target="_blank">📅 12:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133999">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
#فوووری
✅
ورزش سه طی خبری مدعی شد؛مذاکرات با اسکوچیچ بدون توافق به پایان رسیده و با توجه به تخفیف اوسمار ، احتمالا این سرمربی برزیلی در پرسپولیس موندگار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/133999" target="_blank">📅 12:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133998">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❗️
❗️
ورزش‌سه: پرسپولیس با اسکوچیچ به توافق نرسید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/133998" target="_blank">📅 12:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133997">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYPrHpntAvGf4H8Ck9XWNOiJeE9pkdZpvHKb18MslHWECxZgg_VPh2ufCZmtPov5dai0vXyBuR958sb-KMzy34E11SDG1riQhRNDXf0N-kWEQW--Ji4O-c4sEQitIG2gpAJgLGrdvJVzLk9YIsRcYST16zXVBXC9bQHWowMPxWaSNlTmXBZo6NRcCOnsnlkwtMT4mKPCt7Q8QmwG8h-9MP4ZEw1c0m3kxb0kTDVyOC1FsYkeR8BYXAICRVA38JA8IdXfQ16DM2ie7zlEyiI-J74Wtm9XeFdZaDePBciejCGBR0n7xDIPSONWYeZ_duWw9UmvtzshQP_v5DESPtkfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
🇮🇷
ورود تیم ملی فوتبال ایران به لس آنجلس برای انجام دومین دیدار خود در جام جهانی مقابل بلژیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/133997" target="_blank">📅 12:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133995">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
امروز آخرین روز مذاکره مدیران باشگاه پرسپولیس شامل پیمان حدادی، محسن خلیلی و امیرعلی حسینی (مسئول روابط بین الملل) و یکی از اعضای هیئت مدیره پرسپولیس با دراگان اسکوچیچ در ترکیه خواهد بود و انتظار می‌رود تا پایان امروز نتیجه نهایی این مذاکرات مشخص شود.//تسنیم…</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/133995" target="_blank">📅 12:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133994">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZl28iWabpAcEMwZBB4TGhx4KqSp2E_zDfBwrypsUSiKQ8otLvu8enq8n5m4FGjNkPPVmePw_IP0IPM2-58_9UATlJbMPTMlEi4N0vAlF1tG0eewxpOyURtAMEy7LPg5z0uoMlXVb9-FWh2hZ-cacRUV2OQfJ7bd4QYuAICvX1GsvPTyKEjodhn4v1ahnwT6I4fnyQ4hLrU6fe3YO4cr_05mYaKRumEwHtZ4_ZNwWw8BW5BVWlX3xcNOgGrNPDZPv4eYo86VyNj2M4QUSrxy-V9yXgVo4756PJ0Ci6ilwTZ69c_I-GlDD1R9rmQjTkoOojtVxJuDLYP6f62g4fprPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
جام جهانی جای عجیبیه!
🔴
🔴
توی یک شب میتونی راه ۱۰۰ساله رو طی کنی و این معمولا برای دروازه بان ها میوفته
🔴
🔴
مثلا همین ووزینیا دروازه‌بان ۴۰ساله کیپ ورد که تا ۲۵سالگی زباله بازیافتی جمع آوری میکرده اما با یک شب درخشش شگفت انگیز از ۵۰ هزار فالوئر به نزدیک ۱۵میلیون میرسه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/133994" target="_blank">📅 11:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133993">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmOJo4WkSI5yP05sVzLj3QA0PsNt2n622P-A-DjysaaxjGcFb0jlzUskPR_uxV7snQgBzRceCBoym0fbBrkezWCoOaW1LeaEVyp979FxHlbrFM7E8BNYc0UoyfWs3FytjJ9hJaV2fU-v9Mi9MfGVhjjP6hIW0cSz0rRJWfkWMYdODuw6d2gg19gVnHH3rDMYSpjaaQVBSI6dH3ZBrWUlXkZqFVNIECfRLRXkG1j2AGk2tAcG16z5qzijwLS1G7IUH-FCUEIEJBonOh2sPrXcp7F9NvruZU1ekw9qGqD2Yzr0lBKIrb0DymKb7GveB5F65yX0bXYRRlqz1Wt1Wlx8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
رومرو لوکاکو از لیست بلژیک برای بازی با ایران خط خورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/133993" target="_blank">📅 11:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133992">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
دانیال اسماعیلی فر ۱ ساله با تراکتور تمدید کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133992" target="_blank">📅 10:48 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133991">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
با وجود توافق اولیه بر سر مبلغ قرارداد، طبق پیگیری خبرنگار تسنیم مذاکرات بر سر دو بند همچنان ادامه دارد و توافق در مورد آنها تا این لحظه حاصل نشده است. طرفین امروز بر سر این دو بند که مربوط به مسائل مالی نیست؛ مذاکره می‌کنند تا در صورت توافق، قرارداد رسمی…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/133991" target="_blank">📅 10:12 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133990">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
ادامه مذاکره پرسپولیس با اسکوچیچ بر سر دو بند؛ امروز؛ صحبت نهایی
🔴
مدیران باشگاه پرسپولیس پس از انجام صحبت‌های اولیه با دراگان اسکوچیچ، بامداد روز گذشته (شنبه) برای مذاکره حضوری با این مربی راهی ترکیه شدند. روز گذشته  مذاکراتی جدی بین پیمان حدادی مدیرعامل…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/133990" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133989">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
مذاکرات میان اسکوچیچ و حدادی مدیر عامل پرسپولیس روند مثبتی داشته و اگر اتفاق غیرمنتظره‌ای رخ ندهد، اسکوچیچ به‌احتمال فراوان در روزهای آینده به‌عنوان سرمربی جدید معرفی خواهد شد./فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/133989" target="_blank">📅 10:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133988">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133988" target="_blank">📅 10:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133987">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
تاجرنیا: باید استقلال رو قهرمان لیگ معرفی کنند، ما حاضر بودیم لیگ برگزار بشه ...!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/133987" target="_blank">📅 10:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133986">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
✅
ورزش سه :  طبق تصمیم فدراسیون و سازمان لیگ، لیگ برتر فصل آینده با حضور 18 تیم برگزار می‌شود و از لیگ ناتمام امسال، هیچ تیمی سقوط نخواهد کرد و قهرمانی مشخص نخواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/133986" target="_blank">📅 10:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133985">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
🔻
پرسپولیس با اسکوچیچ تموم کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/133985" target="_blank">📅 09:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133984">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqqH6NRVntloq1w9bEgIW7l3n9vFM2_w0URqv-YlFgtKdHgb8jZ5NaZ7VVzeAZGzpmt4TKY4VfHE-LZyYR1O9dboTqbCgl7JGeSBtNABPvDq83uVv7yUwg6GMEHJSGj1QI6_9PhR5pEjYYvhdflajMXjdPY7k8GQhmSZBvRKKqSlqY0-I2TvcstWw8kJa1KPtbcJHLEJG8jqYop3IfPkPYqzxuzYaM6mwxbAv1TnkBSx6zSt8J6_AsB4pLZZZ0NtYfJXETQ91mQbPYEuhFNKcluFuYpXqy61s4BX3cmoNgd6SZ6d3ulRYBbh3Lys2hisTLt3FxU-lIgo9WDSguTmYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز 21 June، روزِ جهانی دلتنگ شدنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/133984" target="_blank">📅 09:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133983">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVJg76Ith26XAxUgQ47SCl6iosv_VE_zqHdaKWeEzKurLfkfkErNNVlXyFZieecDGOzW9ag0nAdE_YRKmmclZaeOSSLrgUxz4fFf333i2qp8mBhp8oM0-OTyhFpqskRBIq-MWl_uhOSXu94ZRPjIK2ZF0Q2_ASlihUk1YlhLOwizbX8eAWyVeG0LSFe6ZWhRDJWTIE4vlX2c-CZSbCQ56jOiZzDZra1mQtiAMJ6NOwQheFrwrlAhjSQjVGD-BxveHigS-Qy7s1Af5DWxHSOXtyXLm2L2VUvgme8Mne-qxPaFE8exUxZJ_FNo1tD2-aWlpGMb4jE9hy8j9AR8TR9oJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ویژه جام‌جهانی
6⃣
2⃣
0⃣
2⃣
همراه با وینکوبت ادامه دارد!
🔴
Tunisia -
🔵
Japan
⚫️
جام‌جهانی گروه F
⏰
بامداد یکشنبه ساعت ۰۷:۳
۰
🏟
استادیوم بی‌بی‌وی‌ای
🎁
🔣
5⃣
1⃣
بونوس ویژه به مدت محدود روی تمامی واریزها فقط با یک گردش روی حداقل ضریب ۱.۸ به موجودی خودت اضافه کن.
⏰
این بونوس ویژه وینکوبت فقط تا دوشنبه ۱ تیرماه ساعت ۲۱:۳۰ فعال است.
📌
همین حالا وارد ربات وینکوبت شو و ازین بونوس ویژه استفاده کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133983" target="_blank">📅 02:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133982">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAqVsVh-tDvD6wqHGbNl4O6dQAb1usnmKfy94xG_K0Gcs8GQAIKu9f1KRpZZRbTnMRQaDjENYKULtvPFuiE-VjoiWALUqhtCH4GJRyt28IWg_eR-Dg2BCsGF8Tt6vvDPj8IOnIKxyozZaLgpe64RJyQIhDSCdzZg_bsQLyyXzPXKEgzJh4pY8gD5GvwIbIMVXjUHbRBF2qSD12xCleIsHWH7yIkxKCrXZxTEHkXuC6SlF2DXeXZMx4zivbQZ8aIoPcMDYtauEI2dKdA2iUctNVWYJAkal4yiRUQ8OA6gb4H8BRxE75MC8204-DOccbNjLUkHct1owRI0GMoxO0LY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیش‌بینی اپتا از نتیجه بازی ایران و بلژیک
🔴
سایت اپتا براساس ۱۰۰۰۰ شبیه‌سازی نتیجه بازی ایران و بلژیک را پیش‌بینی کرده که در آن شانس برد تیم ملی ۱۵.۱ درصد است. در این پیش‌بینی شانس برد بلژیک ۶۶ درصد و تساوی ۱۸.۹ درصد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/133982" target="_blank">📅 01:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133981">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">⚡️
چه زجه ای میزنن ایجنت های اوسمار، بستون نبود هرچی نیم فصل خوردید؟!
🧐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133981" target="_blank">📅 00:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133980">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
|
#فوری
⁉️
🏅
به گزارش رسانه «سرخ تایمز» تاکنون قراردادی بین باشگاه پرسپولیس و دراگان اسکوچیچ امضاء نشده؛اما مذاکرات بین دو طرف در حال انجامه و اینکه آیا اسکوچیچ فصل آینده سرمربی پرسپولیس خواهد بود یا نه نهایتا روز دوشنبه مشخص میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133980" target="_blank">📅 00:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133979">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚡️
علیرضا نورمحمدی حماسه سازی کرده
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133979" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133978">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=fXd1Jp157oNBnlk_aGAkxORXCMO0A1TQUwOIQzzde4Yn5ZiAumHnTcpZ25amlg-czbGO3I5-wEgz3_AweQXu4CWS_TXsEZGKJgH1CBrLUkXm7WLxQav4kZVMVAfNoUufZyvwW2u8cikZqRvA-ox1vuBMP1g1MSjWRGV3pciRefrcgNNTTfRpV3VSC2WjLYgrr_-VjHlhQ9ZGqBCEubon7knLp-NvTCxfx8ihjoM4LMIS-G_21my4GBoShKsRHJOvRuP8GziHdZ_F0TAhRd7mze5t90rKgmgmyX9khyLTCayHzvdUvcO7TslYrm0PYFrmR-JIGjicwW0m2Kq1wJ74DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80ddf04f1.webm?token=fXd1Jp157oNBnlk_aGAkxORXCMO0A1TQUwOIQzzde4Yn5ZiAumHnTcpZ25amlg-czbGO3I5-wEgz3_AweQXu4CWS_TXsEZGKJgH1CBrLUkXm7WLxQav4kZVMVAfNoUufZyvwW2u8cikZqRvA-ox1vuBMP1g1MSjWRGV3pciRefrcgNNTTfRpV3VSC2WjLYgrr_-VjHlhQ9ZGqBCEubon7knLp-NvTCxfx8ihjoM4LMIS-G_21my4GBoShKsRHJOvRuP8GziHdZ_F0TAhRd7mze5t90rKgmgmyX9khyLTCayHzvdUvcO7TslYrm0PYFrmR-JIGjicwW0m2Kq1wJ74DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🆗
واکنش من به اخبار نقل و انتقالات این روز های باشگاه:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/133978" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133977">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🆗
واکنش من به اخبار نقل و انتقالات این روز های باشگاه:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/133977" target="_blank">📅 00:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133976">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
بقایی سخنگوی وزارت خارجه
🔴
مردم مطمئن باشند که ما با آمریکا تعهدی را امضا نکردیم که‌اجرا نشود/از همین‌رو هیئت‌میناب 168 تیم مذاکره‌کننده‌ی ما به ریاست آقایان قالیباف و عراقچی و همتی راهی سوئیس برای ادامه مذاکره با آمریکا شد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133976" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133975">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
جرمی‌ دوکو ستاره تیم‌ ملی بلژیک دیدار مقابل ایران را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133975" target="_blank">📅 00:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133974">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✅
بقایی سخنگوی وزارت خارجه
🔴
مردم مطمئن باشند که ما با آمریکا تعهدی را امضا نکردیم که‌اجرا نشود/از همین‌رو هیئت‌میناب 168 تیم مذاکره‌کننده‌ی ما به ریاست آقایان قالیباف و عراقچی و همتی راهی سوئیس برای ادامه مذاکره با آمریکا شد
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/133974" target="_blank">📅 00:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133972">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oce-2yy6Feg10c9cHr83_YU-nwA3KNxguEUm7sAJ-tf0SsBMoRvsSI4nfoqjYou-OnVOGEBltXua0FVSxEVsw6Pnq5WSbmzbSJz6UXHkJssomHxWn94YIbi3LNxNzXifuIPozYHgJ8-FZkRSV0M1X6LpEcWAlBo1RNTVZWJblRBHCn2Qdg_DHpZI4Q3d7f91aW26LnYjOIZvsuXzd_fVuTu9YcjlLooUdTWn9XOp26pugpB0TG3g7fxzg_V99k1SGFqlxcRI0Lr312XecCov49w2vAHcBkO2_MGNODjCVHgX2fPY_fSXjhGMz3hqWsa4t9-m_XhCrRHJpxALlfTA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133972" target="_blank">📅 23:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133971">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
تارتار: گل گهر سه ماه و نیم است تمرین نکرده، 4 بازیکن تاثیر گذار تیم هم بازیکن آزاد هستند، چطور من برای مسابقه آماده شوم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/133971" target="_blank">📅 23:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133970">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
تارتار: گل گهر سه ماه و نیم است تمرین نکرده، 4 بازیکن تاثیر گذار تیم هم بازیکن آزاد هستند، چطور من برای مسابقه آماده شوم؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/133970" target="_blank">📅 23:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133969">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
فوووووووری
🚨
مهدی گودرزی هافبک 22 ساله خیبر خرم آباد در لیست خرید تیم پرسپولیس قرار گرفته و مدیران باشگاه پرسپولیس قصد دارند این بازیکن را با پرداخت رضایت نامه جذب کنند/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133969" target="_blank">📅 23:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133968">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🔻
پرسپولیس با اسکوچیچ تموم کرد / قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/133968" target="_blank">📅 23:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133966">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/133966" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133965">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
فوووووووری
🚨
مهدی گودرزی هافبک 22 ساله خیبر خرم آباد در لیست خرید تیم پرسپولیس قرار گرفته و مدیران باشگاه پرسپولیس قصد دارند این بازیکن را با پرداخت رضایت نامه جذب کنند/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/133965" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133964">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
🚨
🚨
🚨
کسری طاهری، تیکدری و گودرزی خریدای پرسپولیسن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/133964" target="_blank">📅 23:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133963">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✅
هلند انتقام تونس رو از سوئد گرفت!
🇳🇱
5️⃣
➖
1️⃣
🇸🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133963" target="_blank">📅 22:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133962">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
جرمی‌ دوکو ستاره تیم‌ ملی بلژیک دیدار مقابل ایران را از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/133962" target="_blank">📅 22:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133961">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🟨
🟨
دوکو بخاطر زایمان همسرش اردو بلژیک رو ترک کرده و احتمالا بازی فردا شب مقابل تیم قلعه‌نویی رو از دست میده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/133961" target="_blank">📅 22:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133960">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anivyEZuLks4evTRenYA-AM7pzf75nHPUhst0UpyY-I_xEUA8iM08aLQghHwLGLkG2FO2RSm9eIfIrPEA1L-HJ95E3nCrjTcEBuvTOUbS1bI4Mmewxmp5UqHAxdB7eq5t765IIysX3Rwu14czNbyPEhlei1VU8TTgxz44moFMFx70JThiC0obXFAYJ5Jc_L62mpf06ShUFEEODY5S8Z0NNJHa_-bBK8CtMLRLTiHhcMVNPmwS9nkMXCNtobfkP1d4pa0fVhPJMa0IsUUOzbks1fuHPMoPlXHj-bigmsfcojbgnTv1lbZJhCD7rv6h5fDKJxn1SYM8pGUddZgPxnXAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
حضور مرتضی پورعلی گنجی با دست گچ گرفته در تمرین پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/133960" target="_blank">📅 22:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133959">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGB59ZbQDYcvYOPW_81mQ_j08SvrA8wo-b-xXY3lA-hYMAXjr4o3XgUPP8ZlNduYQbrE26VjUDEXgqpLyVfDlkTtdSEphJjLXvp-EbCWqsZgV0T93XuMjVf-IARTe1Bvl6K914Q1WkYtiPOwc-PplrIYcY6C36SC6VRDxoB5PAu89vkrpnBzL1qzsYz8aV6YB1-OR51LgsgId544jFzLSxoH4VIjsfjsdQNif1slJd7YIOclaFbigTzfrSdXM9nUHMV_jMazIPjrpsEmzYuKUlbomkRHQwzScS3u-VzQy2F-k5EZiAFH1dbAG8IAi5FWtZyOP7ruvo5qAABoFdkM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه F جام‌جهانی ۲۰۲۶
[
آلمان
🇩🇪
🆚
🇨🇮
ساحل‌عاج
]
⏰
شنبه ساعت ۲۳:۳۰
🏟
استادیوم
بی‌ام‌و
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
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/133959" target="_blank">📅 22:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133958">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
بعد از جام جهانی قرارداد امیرحسین محمودی هم از لحاظ مدت و هم از مبلغ افزایش خواهد یافت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/133958" target="_blank">📅 21:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133957">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
شنیده می‌شود قرارداد دو ساله اسکوچیچ با پرسپولیس امضا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/133957" target="_blank">📅 20:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133956">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96b9555f3f.mp4?token=aPYpxbhixVf2_VnY1bsvOEYeT8iTPTTJY0db9MxVVZ-8GCZA06AprULKfZkR7IOYPoli9Aq-AaxsnkyJiBcmKvE16wGe4DMl0vDPIDrA_3d6KTsS8wPLX_9Gkv8jABqzibnrQ9rrdhEHKmIuwaFkHVhHY4eYAygcPbMpPs3tbyIkidApUAyro5Ty85cLjAF-qNCvllAriMavzVU1QfKqhqG9uya9zHcY5eqqPd4h7eYaaEjkOy6GmMY57DX5KeBkaV_x05_RCzs6tMw7vpL6-kZEFKuzF0A0wgqVBE_l_tNuqyD-9eHda_Qzoq0Z8kQ-faLwPaLTZGC56JLlsbJF_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96b9555f3f.mp4?token=aPYpxbhixVf2_VnY1bsvOEYeT8iTPTTJY0db9MxVVZ-8GCZA06AprULKfZkR7IOYPoli9Aq-AaxsnkyJiBcmKvE16wGe4DMl0vDPIDrA_3d6KTsS8wPLX_9Gkv8jABqzibnrQ9rrdhEHKmIuwaFkHVhHY4eYAygcPbMpPs3tbyIkidApUAyro5Ty85cLjAF-qNCvllAriMavzVU1QfKqhqG9uya9zHcY5eqqPd4h7eYaaEjkOy6GmMY57DX5KeBkaV_x05_RCzs6tMw7vpL6-kZEFKuzF0A0wgqVBE_l_tNuqyD-9eHda_Qzoq0Z8kQ-faLwPaLTZGC56JLlsbJF_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دکتر عزیزی دست به کار شد
🔴
خداداد : میخوایم حسین نژاد رو بیاریم ایران!
پ.ن مبلغ فسخ و شنیدن شاخ درآوردن
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/133956" target="_blank">📅 20:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133955">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
مخالفت آمریکا با سفر ایران ۲ روز قبل بازی با بلژیک
🔴
🔴
در شرایطی که کادر فنی تیم ملی برنامه آماده‌سازی خود برای مسابقات را به فیفا اعلام کرده بود، محدودیت‌های اعمال‌شده از سوی برگزارکنندگان، روند اجرای این برنامه را با مشکلاتی مواجه کرده است. قرار بود تیم…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/133955" target="_blank">📅 19:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133954">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⚠️
⚠️
تنگه هرمز مجدد درش تخته شد
🔥
قرارگاه خاتم الانبیا:‌ تنگه هرمز به دلیل نقض مکرر اتش بس توسط اسرائیل تو جنوب لبنان و کشتار بی رحمانه‌ی مردم بسته شد
🚨
اگر عهدشکنی‌های آمریکا ادامه پیدا کنه پاسخ سنگین‌تری میدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/133954" target="_blank">📅 19:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133953">
<div class="tg-post-header">📌 پیام #35</div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/133953" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133952">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❗️
پاکستان: مذاکرات فنی ایران و آمریکا فردا در سوئیس برگزار میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/133952" target="_blank">📅 18:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
فووووووووووووری
🚨
قرارداد اسکوچیچ دوساله خواهد بود
‼️
سه دستیار نیز به همراه اسکوچیچ به تهران خواهند آمد. همچنین گفته میشود مربی دروازه‌بان‌های اسپانیایی پرسپولیس در کادرفنی اسکوچیچ باقی خواهد ماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/133951" target="_blank">📅 18:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
پیمان حدادی برای بستن قرارداد به ترکیه رفته و اگر اتفاق خاصی نیفتد، تا ۲۴ ساعت آینده اسکوچیچ رسماً معرفی می‌شود.
🔸
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/133950" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133949">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇵🇰
🇵🇰
🇵🇰
#فووووری شریف، نخست‌وزیر پاکستان:
🔸
خوشحالم که اعلام کنم توافق صلحی بین ایالات متحده آمریکا و جمهوری اسلامی ایران حاصل شد. جنگ در تمام جبهه ها پایان یافت. مراسم رسمی امضا روز جمعه، ۱۹ ژوئن، در سوئیس برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/133949" target="_blank">📅 18:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133948">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💢
💢
#فوری؛ ادعای #فرهیختگان:
▪
پیمان حدادی برای عقد قرارداد نهایی با اسکوچیچ به ترکیه رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/133948" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133947">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
🚨
❌
#فووووووووری از فرشید حقیری: حدادی صبح برای بستن قرارداد با اسکوچیچ به ترکیه رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/133947" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133946">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AiR0q5Jt0gejmy_c3kwTZls9rBpKd2SdvWRGojKodCKh3lKpDIbQWkeJYmvNpKcScnaQO6zdWBRGH_4wMe-zItkHTTgaNlcppN2c0I6IStvFhDU2Xim35n0z6sfNIOIfj447iJL8JFBlpa-wy-EGQlWcXdNC5dIRDY8zmsYd5vDAPwcXgj29GoX4YPA-i2zjqd3FBgrYDdv_oJGuTl6mxUTX4hS9JpxHczRi5Zv22poruZZyD6vmR9JApShw7NLMtKModGq9VVlmJivtniJcV65yMQEnS3iGVjE5k6Bg21Hohum2pjywPI0xL3-AXGcekHuo5OaAlcOslsvDX29T7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عجب بازی‌های آسونی دارن تیما آسیایی تو این هفته
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/133946" target="_blank">📅 17:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133945">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✅
قرمز آنلاین مدعی است دو تیم خواهان سروش رفیعی شده اند اما او دلش با پرسپولیس است اما به حدی از برخی واکنش ها و رویکردها ناراحت است که ترجیح داده سکوت کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/133945" target="_blank">📅 17:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133944">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
❗️
فرشید حقیری: اسکوچیچ‌ ترکیه ست و به‌ زودی با امضا قرارداد میاد پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/133944" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133943">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
سروش اگه پیشنهادی نداشته باشه خداحافظی میکنه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/133943" target="_blank">📅 16:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133942">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⚠️
⚠️
تنگه هرمز مجدد درش تخته شد
🔥
قرارگاه خاتم الانبیا:‌ تنگه هرمز به دلیل نقض مکرر اتش بس توسط اسرائیل تو جنوب لبنان و کشتار بی رحمانه‌ی مردم بسته شد
🚨
اگر عهدشکنی‌های آمریکا ادامه پیدا کنه پاسخ سنگین‌تری میدیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/133942" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133941">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
متن کامل پیام رهبر انقلاب اسلامی خطاب به ملت ایران درباره تفاهم‌نامه رئیس‌جمهوران ایران و امریکا :
🔸
بنده علی الاصول نظر دیگری داشتم ولی از باب تعهدی رئیس جمهور محترم به عنوان رئیس شورای عالی امنیت ملی به حقوق ملت ایران و محور مقاومت جلو اجازه آن را صادر…</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/133941" target="_blank">📅 15:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133940">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❗️
تیبو کورتوا:
✅
ایرانی‌ها یک مدافع راست به نام رامین رضاییان دارند که در حملات بسیار فعال است و ارسال‌های دقیقی دارد. باید مراقب او باشیم، او می‌تواند خطرناک باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/133940" target="_blank">📅 15:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133939">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇧🇪
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/133939" target="_blank">📅 15:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133938">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⚡️
⚡️
⚡️
گئورگی گولسیانی در لیست مازاد باشگاه سپاهان قرار گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/133938" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133937">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqmXYEA6HPiIv-atoZkRC-bRIX_fEtJx9rKMXLkj7XLDqV0XCQr9tUfpwtwzxCLU7qH7r2BysyHNka-v_uSeOdWHPWNNAcv8j3jh8kaxGNEtZI83T98HruRlRkj4fNuSigeEpRuQTdgGf1bzWuVJFGNZc78ldB21pm8m-gUWfRF7dtCCZFAFyX8qAMAx0CjFjHvc8KiTSelLuIaWB4vf8ABr56o0waiCdIEhu75v6AEoq07l15fIg11OtGhh9Qk5MmNAXZ2xjiXmxVXEkaiJiMx4R6kttytGs7jIx4crWl47PLPIrB9YZ-au8-299GiAgZUgSwls2Zh0OfsvNlVaog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
روزبه چشمی، سوگولی گروهبان قلعه‌نوعی که رفاقتی رفت جام‌جهانی بازی بلژیک رو هم به دلیل مصدومیت از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/133937" target="_blank">📅 14:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133936">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">❗️
تصمیم نهایی با بانک شهره و انتخاب اونا هم اسکوچیچه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/133936" target="_blank">📅 14:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133935">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
برگزاری لیگ بیست‌وششم در اواخر مرداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/133935" target="_blank">📅 14:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133934">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❗️
برگزاری لیگ بیست‌وششم در اواخر مرداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/133934" target="_blank">📅 13:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133933">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMPsoxjXPr9vxo157mkUgbTYLmaGnewMerZh5dDTj3FWi4qNSGxoAAjK9MopwTb91EuknD6Uk_qwuR192c-RauCGmBprRlTlgwuSF7-73C6yEd6qb6pAAEJB7td7ziAS0VpPss6Qu4tvVI7UxHliuOJ-E8YS580MYgItr5Q1MQWVP1jeE7qsp4nwapwtG9icrnZ5ClgHN85CakyUiFlPnKqxNH8qeDiZUQynNsHy7mBxGXc8UcivqUTS7OnBVaat4uHeXVDtBdmUsrR2MgpRjIQ3xo8ls2TY2-tdR-BnrZukyw32C6mZPQvuipom8Q3AYWKrvkfn0wLxxEzcarubqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نقل و انتقالات تابستانی لیگ برتر فصل 1405-1406 از 31 خرداد آغاز می شود و تا روز 4 شهریور ادامه خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/133933" target="_blank">📅 13:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133932">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
از دیگر نکات، این است که پیش‌تر باید حتما یک بازیکن آسیایی در بین نفرات خارجی می‌بود (1+7) اما در مصوبه جدید الزامی به آسیایی بودن یک بازیکن وجود ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133932" target="_blank">📅 13:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133931">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
این مصوبه البته یک استثنا دارد؛ اگر باشگاهی در فصل گذشته بیش از چهار بازیکن خارجی در اختیار داشته و این بازیکنان برای فصل آینده خود قرار دارند، استفاده از آنها بلامانع خواهد بود. در غیر اینصورت اگر قرارداد بازیکن خارجی تمام شده باشد، برای تمدید قرارداد تابع…</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/133931" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133930">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcphqym0G7RqJMYTwQy69seszZX159BCl58t1Us7H9dDu46c8Oj5l60zuQoVjsYLVWEJTDwYAwNdKxuJw1n1_e9OboAS8J0kR6N4DRcrOWoQO8AM8F12ME-QQnLsyl2oRiH3E9fHtaNuNwSR2cEW6BfJWhUdlJRZ86qG5iMX5tnLk8MAWmgT-dZGGXpNN67ywZsQlVbqltdUWmjHQMos4Z8jlhIwDtw3o3SWUlIE3E8T9yUp1jqREFvEc5ojupI8Q8lbJln1acx2kh1wfjQdGC9h8cI3WMBvXHFUvAd89lY6dQPUYy_NKsjMMBKTiuP9vPQG2zc7VhQxYvkzfmy0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚽️
اوج
هیجان مسابقات جام‌جهانی ۲۰۲۶ فقط با
اسپورت نود
⚽️
گروه F جام‌جهانی ۲۰۲۶
[
هلند
🇳🇱
🆚
🇸🇪
سوئد
]
⏰
شنبه ساعت ۲۰:۳
۰
🏟
استادیوم
ان‌آرجی
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
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/133930" target="_blank">📅 13:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133929">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">❗️
یکی از مصوبات دیگر و مهم جلسه امروز هیئت رئیسه فدراسیون فوتبال مربوط به بازیکنان خارجی بود. طبق پیگیری خبرنگار تسنیم بر این اساس سهمیه بازیکنان خارجی برای باشگاه‌ها که در فصل گذشته 1+7 بود، به 4 بازیکن کاهش یافت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/133929" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133928">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
✅
ورزش سه :  طبق تصمیم فدراسیون و سازمان لیگ، لیگ برتر فصل آینده با حضور 18 تیم برگزار می‌شود و از لیگ ناتمام امسال، هیچ تیمی سقوط نخواهد کرد و قهرمانی مشخص نخواهد شد .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/133928" target="_blank">📅 13:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133927">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🖍
فارس طی خبری مدعی شد باشگاه پرسپولیس با ارسال نامه ای به الوحده خواهان به خدمت گیری مبین دهقان شد
🔴
این بازیکن از الشارجه نیز پیشنهاد دارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/133927" target="_blank">📅 13:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133926">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
جدایی اوسمار از پرسپولیس قطعی هست/مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/133926" target="_blank">📅 12:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133925">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133925" target="_blank">📅 12:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133924">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
فووووووووری؛ تکلیف نیمکت پرسپولیس تا هفته آینده مشخص میشه. باشگاه از اوسمار تخفیف خواسته اونم موافقت کرده ولی میزان تخفیف رو اعلام نکرده/ فارس   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/133924" target="_blank">📅 11:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133923">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
اوسمار : امروز من سرمربی پرسپولیس هستم تا روزی که باشگاه تصمیم بگیره و بخواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/133923" target="_blank">📅 11:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133922">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/133922" target="_blank">📅 11:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133921">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❌
از باشگاه پرسپولیس خبر میرسد که با توجه به حضور مرتضی پور علی گنجی و حسین کنعانی زادگان در دفاع و همچنین احتمال جذب یک یا دو بازیکن جوان دیگر اگر اتفاق خاصی رخ ندهد مسئولان باشگاه قصد دارند نام ابرقویی رو در لیست مازاد قرار دهند
❌
البته مبلغ بالای دو مدافع…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/133921" target="_blank">📅 11:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133920">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
فووووووووری از ورزش 3: اعلام رای استیناف کنسل شده و تورنمنت قطعا برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/133920" target="_blank">📅 10:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-133919">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇧🇪
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/133919" target="_blank">📅 10:39 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
