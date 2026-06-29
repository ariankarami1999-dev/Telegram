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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-134603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
تاج: برنامه‌های مرتبط با حمایت از همجنس‌گرایان در بازی با مصر لغو شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/134603" target="_blank">📅 20:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
زیبا‌ترین گل‌های جام‌جهانی 2026 تا پایان مرحله گروهی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SorkhTimes/134602" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134601">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/134601" target="_blank">📅 18:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤩
🤩
🤩
گفته می‌شود مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کند تا طرفین برای جدایی به توافق برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/SorkhTimes/134600" target="_blank">📅 18:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134598">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQhWoXUBvcBeSXK3Ab_g6tirFVpkYMSyvnco5NcMqJ-bynKGQSN_FKfAFoSJZR2JocZqeWxuE1ruwRqkzwolF83h--OZtBY5V2uJfOLWI63eAodK6rvdvtg-JD0c6f-dRrBEqe1Ys6wYM4IN6O84FaxkkkqP8lSSDqPZTYVscDQxcUIw24Ov6JkQSeLopnNXrfyjnnB_AyjshkzTDrQ3gNANAJHZRoICagkBExIhVxgvL1JR8lqsSVaTqXN_x8gJbzK8Lgdo_lAX5CuTybSvbrvQdBXkG0BWlZsr6fSX0ZUirsSuP3xn_nRaZz35pgNhByTZQzfcfiFXq7iVeajrgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته فرهیختگان، باشگاه برنامه ای برای تمدید قرارداد علیرضا رفیعی نداره و این بازیکن بزودی از پرسپولیس جدا میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/SorkhTimes/134598" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134597">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/134597" target="_blank">📅 18:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134596">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/134596" target="_blank">📅 16:24 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134595">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❗️
❗️
میلاد محمدی ظاهراً دوست داره برگرده یونان. از اون طرف، مدیران باشگاه هم خیلی تمایلی به تمدید ندارن و دنبال جذب رزاق‌پور هستن اما اسکوچیچ به سبک بازی محمدی علاقه دارد و شاید با توجه به پافشاری سرمربی مدیران باشگاه راه چاره‌ای جز مصالحه با میلاد نداشته…</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/134595" target="_blank">📅 15:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134594">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
باشگاه تراکتور با رضا غندی‌پور مهاجم تیم شباب الاهلی امارات به توافق رسید و فصل آینده این بازیکن جوان پیراهن تی تی ها را به تن می‌کند.
✍️
مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/134594" target="_blank">📅 15:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134593">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
غیر رسمی: اسکوچیچ فردا بعنوان سرمربی پرسپولیس رونمایی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/134593" target="_blank">📅 15:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134592">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sE38-8kKVL9xZ4tXNGe7sIREcNqpkj4vSUQ9bOdC9ncpn5bNRr5koFToq-rEiEzmVVr9NE5fa28DHykH3wqTTxSkPSZgrwXmMwX6ac-VzXQODuJ1f-KWvBTCAHZN8wKCHJhAU6LiqptB66z0d-HF8l_Rq10w44KqiWp6WwXVrpkLlc3Zem1adbn0edNa6CyF_66XifaqhwKS3eesMAUgl5_w95fpu59OO7HtKfFvpqk3Ab6qQg-40qpYEO7JBJu40XMDjF0iqisFK6os4F3GniaNFADttp-MYE36P54lPL32SqOKQRHUXbZV7Z7UdrSvSOYmXxwlC8kqnid6_KBFIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
عینک مخصوص حذف از جام جهانی ۴۸ تیمه فقط ۱۳۴ هزار تومن :)))
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/134592" target="_blank">📅 15:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134591">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/134591" target="_blank">📅 15:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">❌
تراکتور بعد از دانشگر و محمد مهدی محبی اینبار رضا غندی پور هم جذب کرد ..امیدوارم باشگاه برای جذب بازیکن دیر اقدام نکنه ...چون بازیکن خوب روی زمین نمی‌مونه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134589" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
🔴
محمد مهدی محبی با قراردادی ۳ ساله رفت ترتر و بعد از ممد دانشگر دومین خرید ترتره .
🔴
مدیران ما هم هنوز تو خواب زمستانی هستن .
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/134588" target="_blank">📅 14:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
نیمکت نشینی عالیشاه مقابل چادرملو فنی بود؟
🔻
🔻
گفته می شود نیمکت نشینی عالیشاه مقابل چادرملو ریشه در دخالت مدیران داشته است.
🔻
🔻
برخلاف اخبار منتشره امید عالیشاه، در لیست مازاد اوسمار ویرا نبوده و عدم حضورش در ترکیب اصلی و بازی گرفتن از او در دقیقه ۸۰ ، عجیب…</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/134587" target="_blank">📅 14:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
✅
فرهیختگان: برنامه باشگاه پرسپولیس برای مرتضی پورعلی گنجی و امید عالیشاه، فسخ توافقی هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134586" target="_blank">📅 14:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/134585" target="_blank">📅 13:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
با اعلام مسعود پزشکیان، 6 میلیارد دلار از دارایی های ایران در قطر آزاد و به ایران تحویل داده شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/134584" target="_blank">📅 13:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✅
✅
استقلال رسما با ارسال نامه ای به وکیل بیرانوند پیشنهاد دو ساله به ارزش ۲۰۰ میلیارد داد./ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/134583" target="_blank">📅 13:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134582">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/134582" target="_blank">📅 11:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134581">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/134581" target="_blank">📅 11:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» حدادی شخصا میخاد با امید عالیشا،میلاد سراک،رضا شکاری،مرتضی پورعلی گنجی،دنیل گرا و تیوی بیفوما فسخ کنه.
❌
حالا باید ببینیم بانک شهر برای فسخ و آوردن بازیکن جایگزین بودجه میده یا نه
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/134580" target="_blank">📅 11:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
🔺
اعلام زمان مسابقه دوم پلی آف آسیا
🔸
مسابقه دو تیم چادرملو اردکان – گل گهرسیرجان  ساعت ۱۹ روز دوشنبه ۸ تیر ساعت ۱۹ در ورزشگاه پاس تهران  و بدون حضور تماشاگر آغاز می شود.
🔸
برنده این مسابقه به عنوان نماینده فوتبال کشورمان در لیگ قهرمانان سطح دو آسیا به کنفدراسیون…</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/134579" target="_blank">📅 11:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❌
❌
به نظر می‌رسد یک تابستان پُرخبر در انتظار سرخ‌پوشان خواهد بود.
🔴
مدیران باشگاه نه‌تنها به دنبال قطع همکاری با اوسمار ویرا هستند و براساس آخرین خبرها، مذاکرات با دراگان اسکوچیچ به مرحله پایانی رسیده و قرار او به‌زودی با سرخ‌پوشان نهایی خواهد شد بلکه فهرست…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/134578" target="_blank">📅 11:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134577">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
عراقچی: موضوع هسته‌ای، رفع تحریم‌ها، بازسازی و پول‌های بلوکه شده در یادداشت تفاهم آمده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134577" target="_blank">📅 11:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134576">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
🔴
قرارداد اوسمار دیشب با پرسپولیس فسخ شد و این سرمربی برزیلی از پرسپولیس جدا شد.
✅
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/134576" target="_blank">📅 11:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134575">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز | #فوری
🤫
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس توافق نامه دو جانبه توسط اوسمار ویرا امضاء شد و رسما اوسمار ویرا از پرسپولیس جدا شد!
❌
مفاد توافق نامه بدین شرح است: باشگاه پرسپولیس باید ظرف ۲ هفته مطالبات باقی مانده…</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/134575" target="_blank">📅 11:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134574">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134574" target="_blank">📅 08:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134573">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❗️
قلعه نویی: استعفا نمیدم و آماده میشیم برای جام‌ملت‌ها
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134573" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134572">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">✅
✅
امیر قلعه نویی بعد از تساوی ایران و مصر:
🔴
🔴
شاید خدا هم با ما سر ناسازگاری دارد. با یک موقعیت گل نزدیم. می گویند گل ما هم با 5 سانت آفساید گرفته شد. تیم مصر تیم بسیار بزرگی است ولی عدالت فوتبال با همه مشکلات ما رعایت نشد. شاید این آزمایش خداوند از من است…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134572" target="_blank">📅 08:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134571">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmV-Gliy59pszj9rj2F9mvfsLOnyhBTCoYc9e6cRXlBGr_1FiplAk6TWgoFD-DdP2G2sQGKWXIujtagngJnRJqwPrhKokpi4G9F8Z1_h-GsCjBAovV6W7SUfkEA6AddAX1JxZvNDyLrHJf4Ihpne72u5iECdxVh3k3Sv-uyh80jXWcVQheQpJlNIjRq3eXHHTVMQzibb-9Yrl2CK4zGwOT0uypUFiQpWVTxaVKho6Zh1GHbtN_e41z8A67CUMAdZUlOyOSsI4QcLuyY0tkUkXoTRuGtLeQUFBpNE_s7HSfmuOldfWxs8rFVlYwMKvjWVAizuJHYkKcqkFcg_QAaf2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134571" target="_blank">📅 01:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134569">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">#فوری
⁉️
👎
خبر منتشر شده مبنی بر مذاکره حسین خبیری با بانک شهر کذب است،و نقل قول منتسب به خبیری صحت نداره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/134569" target="_blank">📅 00:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134568">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
🔴
فرشید حقیری: مدیران باشگاه قرارداد رو برای اسکوچیچ ارسال کردن…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/134568" target="_blank">📅 00:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134567">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✅
✅
حدادی  : خداداد عزیزی و خلیلی گزینه های سرپرستی تیمن  / هیچ فشاری از بانک شهر برای اومدن خداداد نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/134567" target="_blank">📅 00:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134566">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134566" target="_blank">📅 00:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134565">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
پنجره کیسه بسته است بابت بدهی خارجی .ولی اونوقت مجوز حرفه ای گرفتن.عجب داره واقعا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134565" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134564">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/134564" target="_blank">📅 23:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134563">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
دانشخر به سوراختور پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/134563" target="_blank">📅 23:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134562">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaDNOe5hWWDLYGl28EBahpuyKr6VNXXfXk-dc9fdEeKLxEQ_N9Mn0-VANwqyJh5ynzbhdZWw9KCWE9ojc1OkGf14mToCJHebBsnBT_Xd0NSBcIQi_kyyD3EvJ3RxO4enUalS-HsVdDGnzlB8TmMm5MXZ8Os32RQMqUdpvvyKleyj2GKLoLcRT4dnKabddKjVwJRkzHpwMNSg7ug0sfBg7C4K8WZOxYT0Irzn-ZHm32L8574l4A3WHcXrJU2gkB9nKRNrKwt3JB3sRzuOQw9XNH6JG38Jy28DCWPdrEuKV916N_cnb9rG5PcF3G_9RLT6gMLRSs6McR-MTsEGNEoZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚩
فقط ۴۰ روز تا آغاز لیگ برتر خلیج‌فارس باقی مانده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/134562" target="_blank">📅 23:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134561">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59577ce95d.mp4?token=FaNs5NGMYM36s6HPR2tAJ7Tp9mmiRFU7ItB2tQW50jApcoBKXRTnNhLMRUQhiAlxhmg1oskl5Z1DLb9IAwHj1tBAe15kU2aMbb_VJI0NGxNYHGh571zV51_nlZpOKH4rXWHFLd3ae8xQynIv5EZqzP70Hy-ea7ksR9pjBvdhkdb9Pfpzsf1Q-f3kGo8zgYoF526PQb2JNHJC8Hyn00uUe8djNLevAIbriRrQ47a7WFdkwT1uurzFrBL-Ked7C9f_4a_yVUriSoXt2hYg9gpn6Qlhcw5wtwa3YIXIomtNcVIpydgxK2VTR_H9pvHNJ9ipIqLkytmuJuUAYdTDNC6Ahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59577ce95d.mp4?token=FaNs5NGMYM36s6HPR2tAJ7Tp9mmiRFU7ItB2tQW50jApcoBKXRTnNhLMRUQhiAlxhmg1oskl5Z1DLb9IAwHj1tBAe15kU2aMbb_VJI0NGxNYHGh571zV51_nlZpOKH4rXWHFLd3ae8xQynIv5EZqzP70Hy-ea7ksR9pjBvdhkdb9Pfpzsf1Q-f3kGo8zgYoF526PQb2JNHJC8Hyn00uUe8djNLevAIbriRrQ47a7WFdkwT1uurzFrBL-Ked7C9f_4a_yVUriSoXt2hYg9gpn6Qlhcw5wtwa3YIXIomtNcVIpydgxK2VTR_H9pvHNJ9ipIqLkytmuJuUAYdTDNC6Ahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی: اونور یک دقیقه ای بازیکن اتریش اومد گل زد، چطوریه که طارمی سه بازی گل نزد؟ طارمی خیلی پولدارم هست و مقصر صعود نکردن ایران هم خودشه باید پول بلیت برگشت کادر و بازیکنان رو بده
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134561" target="_blank">📅 22:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134560">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❗️
عادل فردوسی پور: مدیران‌تیم پرسپولیس باخودِ مهدی لیموچی برای قرارداد به توافق شخصی رسیده‌اند و درصورت توافق با مدیران سپاهان این انتقال انجام میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/134560" target="_blank">📅 22:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134559">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/134559" target="_blank">📅 22:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134558">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/134558" target="_blank">📅 22:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134555" target="_blank">📅 22:00 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134554">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/134554" target="_blank">📅 20:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">❗️
❗️
اسکوچیچ خواهان جذب دروژدک مهاجم اسبق خود در تراکتورسازی، برای پرسپولیس شد.
🎙
خبرگزاری تسنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/134553" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134552">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/134552" target="_blank">📅 20:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134551">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
سفیر آمریکا در سازمان ملل: صبر ترامپ نسبت به ایران در حال تمام شدن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/134551" target="_blank">📅 20:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134550">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❗️
عضو کمیسیون امنیت ملی مجلس:
✅
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/134550" target="_blank">📅 19:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134549">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
شنیده ها: پاتریس کارترون گزینه پرسپولیس در صورت عدم توافق نهایی با اسکوچیچ!!!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/134549" target="_blank">📅 18:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134548">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Debl0xvSDv_ChJmx4XQW0VrY1M4uUW19eGMDCJUTr2N4j41feIWsoc0GCKj9njITKiUAsp_giIRPlShU8JJdBr42XdtyIPu9wrv0Cr8awGOCFxrFd8UT8jVHkUg9GDRra6qTYlj5_ab6uTSM9UxJDn8kVOM7rrXmj72hYcUycBmJRcoebh9pxeZ7exXVY5oruzVGOlRDKTa8P3XhrJjyL3pyZuCJMiXwIULD9t2xZVf2YZ3ODgJ5EorPr-8a39vrZ-PnOZRa0dufbR1S3jbMxbQ_WMI-B7tUTTS3vDZfPE9g9U11Qs57ABKhLxaKervNLlL1faKnwbAzqZviyS7wfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏐
نتایج تیم ملی والیبال ایران در هفته دوم لیگ ملت‌های والیبال ۲۰۲۶
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/134548" target="_blank">📅 18:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134547">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
زنوزی، مالک باشگاه تراکتور به صورت شخصی با مرتضی پورعلی گنجی، مدافع پرسپولیس وارد مذاکره شده تا این بازیکن راهی تبریز شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/134547" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134546">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bf61xJOxcv5LrQn3UDjqSLceXM_Hh1CTsRcuFcClYWMl3AricRCG89O6Dd05f_vw_IvPK17JPc6WhhFf9yuBvx3D5Up64QwNnGGxHR3yILY-ryubv4XPCE2z7279pTw1yDb5K0P_8uDnxQQqhVVRRCqbLIU8-yfCuJCr57vZDqcvzBQaYkm9zzusPB-KTzhDqBx_iycG0P6YbZT8gRHGqL02ATsUCZMSEj_kgwkvhSvBHZJ3QUN62Wl-gilAHHZtHCkf8_EvxMEB0u5kcbHSh3BqTU3kLylQ1YeBg5xiikXEM_Iko3_Y8zB5VJ0dWp5tcITxEQGuODUe8byLReCCuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
فوری از قدوسی: علاوه بر اسکوچیچ، باشگاه پرسپولیس در حال مذاکره با یک سرمربی نام آشنای دیگر نیز می باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134546" target="_blank">📅 18:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134544">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
قدوسی: اوسمار ویه را از سال گذشته 400 هزار دلار طلب داره و تنها در صورت دریافت طلبش فسخ می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/134544" target="_blank">📅 18:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134543">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⚽️
پیمان حدادی مدیرعامل باشگاه پرسپولیس در گفت و گو با نزدیکانش خبر استعفای خود از مدیرعاملی پرسپولیس را شایعه دانسته و تکذیب کرده است  بازگشا سخنگوی باشگاه هم در گفت و گویی که داشتیم استعفای حدادی را شایعه دانست و تکذیب کرد/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/134543" target="_blank">📅 18:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134542">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMobin</strong></div>
<div class="tg-text">این خبرها همه سفارشی از عالیشاه باندشه که حدادی کله پا کنند ح رومزاده ها فکر کردند این باشگاه ماله باباشونه که بخوان تا زمان فسیل شدنشون تو اینجا باشند واسه این همه هوادار تصمیم گیری کنند</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/134542" target="_blank">📅 18:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134541">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
قرار است امروز (یکشنبه) جلسه هیئت‌مدیره انجام شود که دور از انتظار نیست خروجی این جلسه، برکناری اوسمار، انتخاب اسکوچیچ و البته پذیرش استعفای حدادی با انتخاب سرپرست مدیرعامل جدید باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/134541" target="_blank">📅 17:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134540">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
#مهم | لحظه امضای نسخه فارسی یادداشت تفاهم ایران و آمریکا توسط دونالد ترامپ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134540" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134539">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
#فوری
🚨
هیات مدیره پرسپولیس برای فردا صبح جلسه فوق العاده گذاشته و درباره آینده پرسپولیس تصمیم گیری خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134539" target="_blank">📅 17:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
به گزارش خبرنگار قرمزآنلاین، طبق اخباری که قبلاً منتشر کردیم، باشگاه پرسپولیس و دراگان اسکوچیچ بر سر دو موضوع با هم اختلاف نظر داشتند که یکی مدت قرارداد بود و دیگری درج بند فسخ در قرارداد در صورت تکرار جنگ که اکنون خبر می رسد دو طرف، توافق کرده اند مدت قرارداد…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/134538" target="_blank">📅 17:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔴
دیدید حالا نمیشه
✌🏻
🔴
تا وقتی به مردمت پشت کنی و دل مردمت باهات صاف نباشه احتمال ۹۲ درصدی صعودت هم به صفر تبدیل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/134537" target="_blank">📅 17:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/134536" target="_blank">📅 15:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏐
برنامه کامل مسابقات تیم ملی والیبال ایران در هفته دوم لیگ‌ ملت‌های‌ جهان؛
❌
از فردا شب شروع میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/134535" target="_blank">📅 15:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134534" target="_blank">📅 15:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✅
تمرینات پرسپولیس به مدت شش روز تعطیل شد و قرار است از شنبه هفته آینده تمرینات پرسپولیس برای فصل جدید در تهران آغاز شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134533" target="_blank">📅 15:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134532">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">⚡️
2- آلویس نانگ (Aloys Nong)
⚡️
آلویس نانگ نامی آشنا برای فوتبال‌دوستان ایرانی است زیرا عملکرد خوبی را در لیگ برتر ایران با تیم‌های فولاد خوزستان، نفت تهران، تراکتور، استقلال خوزستان، پارس جنوبی جم و سایپای تهران داشت. او که با سابقه بازی در باشگاه‌هایی مثل…</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/134532" target="_blank">📅 14:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134531">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚡️
⚡️
- سانل کونیویچ (Sanel Konjevic)
⚡️
این مربی اهل اسلوونی دارای مدرک یوفا پرولایسنس بوده و در زمان بازی، حضور در تیم‌های اسووبودا و اینتربلاک از اسلوونی و فرلاخ و استراسبورگ از اتریش را تجربه کرده است. او به عنوان سرمربی در باشگاه‌های اینتربلاک، برینیه و…</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/134531" target="_blank">📅 14:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134530">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❗️
آشنایی با کادر احتمالی اسکوچیچ در پرسپولیس؛ از مهاجم و مربی سابق تراکتور تا دروازه‌بان سابق دینامو زاگرب
👇
👇
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134530" target="_blank">📅 14:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134529">
<div class="tg-post-header">📌 پیام #32</div>
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
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/134529" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134528">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZMUOt3oD5TQURccLAOWFiR9r2jsWU1tLzrAGRmDzNPOsaNvxX-jUf3Chli44ib7fVGAwUT4S0FDjQAwjfQD8cApg21uLkzQ_vfKmDnIUIiYdwFBs-DxTYTd4PPrfVuA2C-uBH-AVfWlXJe3vV3vuiaH_fWaBiQTID6HGaKkRHKXSgZqtainNmAz3B_-WRAnGyhQgB4N-aajlRPrjQky4J70QKYB9tPWNx7Gp4kMDI3nNxCB30xceCom6CxIRQwAn-dN9qpa-TYCZMNl7U9lQnvsnZp1e0rBCNHlPIeR36bWKFDisqGMlRrfTSCeYjTtKaJoG9U36G7eGE1bqe1YBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویری پربازدید از اقامه نماز در رختکن تیم ملی فرانسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/134528" target="_blank">📅 14:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134527">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❗️
اخباری: گل لحظه آخر را بازیکنی زد که تازه داماد شده و دیشب به تیم اضافه شد. او گفته بود روی من حساب نکنید ولی گفتم کنارمان باشد تا روحیه بدهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/134527" target="_blank">📅 14:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134526">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/134526" target="_blank">📅 14:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134525">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM7oUfohUHBqe0HVGaLjvOPArXtU3tP5osseBrAsHZFVqcKvbNN8O4U58JyDDHYiulLCrjXu91egsC01rs8zFpqhMxFIc68ZY2Yx8xy5_8i7ANp9HTbGwNHB1l0m1kD6d-OOsVSMEtt9SFR0KAUpjy1cRf7NFItXlRzggw-b72MPe29IvYnEy2Oy6Shsjv2qTel1OKJGoG0SJ4yKhTI0Vmcqmai5mV7RAlTTXcMCb-UjmxjdUtXuFvN-Q0_Rgu39TR6jjjGQHl20Uv8r9ZCE4RrtZDYqX7VUwaXpdf-N0ZRvKrkHf4OJOIr9Zl433pbaYSEsq2zPjvvsmLQXmiMD6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فووری از فارس: مدیران باشگاه پرسپولیس خواسته دراگان اسکوچیچ را پذیرفتند و این مربی با عقد قراردادی دوساله (مشروط) سرمربی پرسپولیس شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/134525" target="_blank">📅 14:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134524">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
⚡️
تیوی بیفوما و دنیل گرا برای فسخ قرارداد به باشگاه دعوت شدن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/134524" target="_blank">📅 13:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134523">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/134523" target="_blank">📅 13:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134522">
<div class="tg-post-header">📌 پیام #25</div>
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
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134522" target="_blank">📅 13:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134521">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
قرارداد گولسیانی با سپاهان 700 هزار دلار بوده و او برای فسخ قرارداد، کل این پول را خواسته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/134521" target="_blank">📅 12:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134520">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
ابراهیم اسدی: شأن پرسپولیس حفظ نشد
🔴
🔴
پرسپولیس در حد و اندازه‌های همیشگی خود ظاهر نشد و این حذف برای هواداران قابل قبول نیست. ای کاش تصمیمات مدیریتی و فنی با دقت بیشتری اتخاذ می‌شد و تیم در مسیر بهتری قرار می‌گرفت. این سبک آسیایی شدن در شأن تیم بزرگ و پرهواداری…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/134520" target="_blank">📅 12:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134519">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgKJzVX2LMEkNeBtUkcxVAeH9TA84tsbCnbp0nYrVVyctYN0W_KEf9V2Qu8Z9jRwAyezzx6V7yinZejSRzgW0ih0lXUqcz6b8cOAoqcFWEGtqCBJbgFzrc-65gQ1n9aGJSeggDDVyauWkcT43B_lpjeGVEWB1M_D35jtXt41h3iHT0ZSkvcDODaf_w46tsj31c-nMmZbKHDDN8fdQ4JD3LmGXQhkXBmw_Wx_wTV9chsOKO3UUGhXa_kmn11QX8tpdDWdJZ3qEt9wbCepOYOj_5fpPLgLmk8e7AHvQLZ_ngU5jktovMbuelzduJ5WG1Qvra9VO-rqNgXJX-0WsmxtXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعد گل سوم الجزایر اینجا بازیکنشون میگه اگه ببریم میخوریم به اسپانیا و ریاض محرز تازه میفهمه چه غلطی کرده بخاطر همین شل میکنن تا گل سومم بخورن.
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/134519" target="_blank">📅 11:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134518">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/134518" target="_blank">📅 10:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134517">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
دیدید حالا نمیشه
✌🏻
🔴
تا وقتی به مردمت پشت کنی و دل مردمت باهات صاف نباشه احتمال ۹۲ درصدی صعودت هم به صفر تبدیل میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/134517" target="_blank">📅 10:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134515">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">😂
😂
اتریش دوباره زد و ایران حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134515" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134514">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134514" target="_blank">📅 10:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134513">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
بجا مانده از امروز صبح
😐
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/134513" target="_blank">📅 10:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134512">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnzIZ1kwoELtfeXVrkrF21ERADAB8oMQX2BIXVWaCvKIn6smgNKYSC7SkL_LfrzIcFvRzEcAWF-wJIamSjNHvleUhHws9beV2RUKnOw6vhMAKjTFvrLCOlcKPu25VyuBtAu9yB5gxuB5kNhyXgrIKpOVnjJ8xIHx1HpE37HRB_cz0NuTZAGiJMvC4ryixNEIpQyR5IdeJGmRFcBvkAI1IrBwj3FsHr4z-i8nLmCvDg6wfE3yNaVT0A9gxcQDQ85nQHWiFNcPgLKkTr_oeRq1JsDCcJ78-MV-3FZQ47SBDnoBYp1RI0piIBtKE9J2zIkeDd9pnyHCuIZBf0BnbOZGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/134512" target="_blank">📅 10:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134511">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
یادتونه ژنرال قبل از مسابقات میگفت تیم ملی یه کاری میکنه تو جام جهانی ایران یه هفته تعطیل بشه؟؟
🔴
هفته بعد تقریبا ایران تعطیله کلا ؛ ژنرال صعود نکرد ولی قولش رو عملی کرد
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/134511" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134510">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYQiKO1cCp-sSiP3Pkc74yaeLGRHSpv9TBgf2Ly8S9rRwkEU_vD7y5zpW_ErJuGnk4dz5ss5cDxpxEMyCjt_0dRYZUQdncYVBSCVUrtWZMPg1tjRHTnMaGjuQiEKupYYZgzp2rsZ5IGEgEjD1h4yBrvLw7adlQyR9T55Z807lup1ih80PIA2wh63cKth72Og8aZhQWwLouY_fly5VCmlxaWOg2EUj6b4VbRy2S-_yAgrEjdz6J8_28-wH7YZuAWGysvl6bANv61bIBkTS9t8-aGQB3DNyd752iOyZSUx9j1llVxAQlClnU8pDJthutt68iZp87gb7d_uihWv6pO51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یادتونه ژنرال قبل از مسابقات میگفت تیم ملی یه کاری میکنه تو جام جهانی ایران یه هفته تعطیل بشه؟؟
🔴
هفته بعد تقریبا ایران تعطیله کلا ؛ ژنرال صعود نکرد ولی قولش رو عملی کرد
🙃
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/134510" target="_blank">📅 10:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134509">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❗️
❗️
تسنیم : قرار است به زودی در وهله اول باشگاه پرسپولیس مراحل اداری قطع همکاری با اوسمار را انجام دهد و سپس به طور رسمی جدایی این مربی برزیلی اعلام شود.
🔴
🔴
پرسپولیسی ها که با اسکوچیچ برای جانشینی اوسمار مذاکره و توافق کرده اند، هنوز هیچ قراردادی با این مربی…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/134509" target="_blank">📅 09:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134508">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❌
دقیقه 92 الجزایر گل زد
گزارشگر: ۷ تیر رو یادتون باشه؛ یه تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد.
😂
🔴
دو دقیقه بعدش اتریش گل زد
😆
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/134508" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134507">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/134507" target="_blank">📅 09:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134506">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b235a5b41.mp4?token=J2XAS12v3kq8NKD3JQdKaWXP3cPnX3vv0XB0z3lqPAOCiVgfDdIj6g-JgvFaYqls8Bj2vBALSNzYC90mmDP5P_gp7MJ5YbSMxPEbKN9zD9HODX-ZMtV-QAcvsm0hee8CGd4SxhxTaD9Z-Ju_7QedZj7wYklMqgRyeHhbRpsi1lXWL5i8ki7-OKG9Vl_6T6FdMOdGrXi08rEh_E_hhEQYgJGVLXMLVtR8ZSN_WN9qe6rUvo8bzlW8abs3St9ul7XheSO17FbegmG9t_fChBslICKBdZE50RPYlCSMR3NOk9NizINgAIPTzgY6GzWR2ubBUbPL_IkKwnyZdU80noxEW2YpyOds5WkEdlyqwEjIqwft-U086sHRB-ks1CiQUD7vHLy3X-pmo5vLBmfRgayg46K4zRbgO2vmamUE9jhcshQMaeJRjHNtXJo9-2YEIwC6Bg-PICbRwQQl1NMCM8XQDj4cyjrpdpBZRfZ6d2dXEdq5snz0h2OHyn6D9FlZiGruV2zLNYs2-k05peQWtkv_e0QX8JUx1mQWfYW-wuqUIyP8iOGTAS7gAGRieySKx9aPuK_rqJ_IapWozUKLflNWleSSh3Es9hVL9-K0mvG-Aaa8ZBNV90FJlYepqRDRhHMXuRAUaVb2V3sUvqyKyG-woi1mHx8De-zWrKC3AEKPTwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b235a5b41.mp4?token=J2XAS12v3kq8NKD3JQdKaWXP3cPnX3vv0XB0z3lqPAOCiVgfDdIj6g-JgvFaYqls8Bj2vBALSNzYC90mmDP5P_gp7MJ5YbSMxPEbKN9zD9HODX-ZMtV-QAcvsm0hee8CGd4SxhxTaD9Z-Ju_7QedZj7wYklMqgRyeHhbRpsi1lXWL5i8ki7-OKG9Vl_6T6FdMOdGrXi08rEh_E_hhEQYgJGVLXMLVtR8ZSN_WN9qe6rUvo8bzlW8abs3St9ul7XheSO17FbegmG9t_fChBslICKBdZE50RPYlCSMR3NOk9NizINgAIPTzgY6GzWR2ubBUbPL_IkKwnyZdU80noxEW2YpyOds5WkEdlyqwEjIqwft-U086sHRB-ks1CiQUD7vHLy3X-pmo5vLBmfRgayg46K4zRbgO2vmamUE9jhcshQMaeJRjHNtXJo9-2YEIwC6Bg-PICbRwQQl1NMCM8XQDj4cyjrpdpBZRfZ6d2dXEdq5snz0h2OHyn6D9FlZiGruV2zLNYs2-k05peQWtkv_e0QX8JUx1mQWfYW-wuqUIyP8iOGTAS7gAGRieySKx9aPuK_rqJ_IapWozUKLflNWleSSh3Es9hVL9-K0mvG-Aaa8ZBNV90FJlYepqRDRhHMXuRAUaVb2V3sUvqyKyG-woi1mHx8De-zWrKC3AEKPTwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش میثاقی به تساوی باورنکردنی بازی اتریش - الجزایر: این بازی اصلا عادی نبود
😆
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/134506" target="_blank">📅 08:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134505">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">😂
😂
اتریش دوباره زد و ایران حذف شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/134505" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134504">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❗️
❗️
یا حسین ....الجزایر دقیقه نود و چهار گل و زد و ایران صعود کرد ...عجیبا غرببا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/134504" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134503">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
قشنگ دارن دو تیم اتریش و الجزایر تو زمین راه میرن که مساوی تموم بشه ....و ایران عملا حذف بشه ..چوب و ضربه بازی نیوزیلند و خوردیم ..و خداحافظ  ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/134503" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134502">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
ده دقیقه تا حذف ایران از جام جهانی ...هیچ حالتی اتفاق نیفتاد ...غنا باخت .ازبکستان باخت ..اتریش و الجزایر با تبانی و هماهنگی فعلا تا دقیقه 80 مساوی هستند و میل بردن ندارن چون هر دو تیم صعود میکنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/134502" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134501">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
صعود ایران چگونه محقق خواهد شد؟
🔴
تیم ملی ایران فقط به یکی از اتفاقات زیر نیاز دارد تا به عنوان یکی از تیم های سوم صعود کند
🔴
شکست کرواسی برابر غنا
🔴
شکست نخوردن ازبکستان برابر کنگو.
🔴
عدم تساوی در دیدار اتریش و الجزایر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/134501" target="_blank">📅 07:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134500">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
مثل دیشب
🇺🇸
🇮🇷
فوری از باراک راوید، خبرنگار نزدیک به ترامپ: مقامات آمریکایی حمله به تنگه هرمز رو تایید کردن و آمریکا رسما مسئولیت حمله رو به عهده گرفته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/134500" target="_blank">📅 01:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134499">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
خبرنگار فاکس‌نیوز به‌نقل از مقامات ارشد دفاعی بیان می‌کند حملات هوایی آمریکا همچنان در جریان است که باتوجه به حجم تحرکات هوایی در جنوب کشور ادامه‌دار بودن آن قابل انتظار است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/134499" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
برای اولین حالت باید ساعت 12/30 منتظر بازی غنا و کرواسی باشیم .که غنا ببره صعود میکنیم ..نشد باید ساعت 3 منتظر نباختن ازبک باشیم .....نشد باید ساعت 5/30 الجزایر و اتریش مساوی نشه .....
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/134498" target="_blank">📅 01:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJFI1el_iT1D-MBdh12J6GBpbEewrgF7Cc4tNY_HtfygY_bYODh4lwCsuPuXiqlpRWnxw80jhy7YIkQP_UMCd26XE-IAhe94qhwH7HUmOwOvIsTTI0iND7_diQPqRdf4FDWftpeJKmueWFGkk2amqkgIj_pnhT8Dm0j4qhD9lJBjT_1UKAkuzSTmDDDUxaKC1D1yC9I5auyGh5GzFdzwqWEgT9TF03MgRhvK9Y1o33Ic4mdbVontL9EUdBcwghfH7Dlt4omcVwBz305Z9_wq58QTZYuMoDqUcWdbbssMeNzvua4RPb2ZPHIETgfJtN4XawigC8RTL9gzQj3YcwoVGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جان سینا : ظرف روزهای آینده برای امضای یک قرارداد اسپانسرینگ مهم با همسرم به ایران و شهر زیبای شیراز سفر می‌کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/134497" target="_blank">📅 00:21 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
