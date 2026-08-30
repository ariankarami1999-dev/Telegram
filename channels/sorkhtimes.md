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
<img src="https://cdn4.telesco.pe/file/ZA-Qf694SOL71xhk_OcjYJZDxwvrfzFkf0VGj-Xzxccw8ebj6h4XnmmAtUrq5WMgvDk7gWiJB6GJXWpzfAbxjokvz9NsJoxqKC1e3gy90Sy8kSgO_jrcWbQbC-opz9T9sB1uaWDjqPnhFssURsSjIpbK2Vg3OdNAlKRWC4Z6C--RyiBNH2_EnPfBqXHJlqm158q79YVez8NjHb5eznV6susQqgEP6kANq51mUUMQd2LqPXhasNcXjN4RSvhAEGtrsB6nztcnaG1h6KhuvfpPmwQM0CmB0CA0lF7Nnc47iJPbWLccVkimbQneAFFBarl_0l3uirqx7_t4wcIQ7q9i3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 17:38:01</div>
<hr>

<div class="tg-post" id="msg-139257">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
یک‌سایت خبری روزگذشته مدعی شده که مهدی‌ترابی در بازی با چادرملو دچار پارگی رباط صلیبی شده و فصل رو از دست داده! باید منتظر تایید یا تکذیب این خبر باشیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/139257" target="_blank">📅 17:18 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139256">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
عبدی : من زارع هم میخواستم، پرسپولیس گفت نمیدم. هاشم‌نژاد هم میخواستم که شکمش رو عمل کرد. کوشکی هم جواب تلفنم رو نداد. حسین‌نژاد هم بعید میدونم که تیم خارجی به ما بازیکن بده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/139256" target="_blank">📅 16:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139255">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✔️
✔️
با 5 بازیکن چگونه برویم تمرین کنیم/ می توانیم برویم گرگم به هوا بازی کنیم اما فوتبال نمی شود بازی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/139255" target="_blank">📅 16:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139254">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
حسین عبدی: 23 بازیکن دعوت کردم فقط سهیل صحرایی، مسعود محبی، پوریا شهرآبادی، پوریا لطیفی فر و دانیال ایری آمده اند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/SorkhTimes/139254" target="_blank">📅 16:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139253">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✔️
✔️
سه پرسپولیسی به اردوی تیم امید اضافه شدند
❌
❌
پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن تیم فوتبال پرسپولیس، به اردوی تیم ملی امید ایران اضافه شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/139253" target="_blank">📅 16:49 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139252">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
فوری/ با اعلام مهدی تارتار باشگاه تا 22 شهریور بازیکنی به تیم ملی امید نخواهد داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/SorkhTimes/139252" target="_blank">📅 16:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139251">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/139251" target="_blank">📅 15:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139250">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/139250" target="_blank">📅 15:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139249">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/139249" target="_blank">📅 15:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139248">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
تیکدری دفاع چپ پرسپولیس در دربی/خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139248" target="_blank">📅 13:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139247">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">❌
❌
❌
تیکدری: روز اولی که به پرسپولیس اومدم گفتم با تمام توان در هر پستی بازی میکنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/139247" target="_blank">📅 13:06 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139246">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">☑️
پرسپولیس برای دربی اردو زد!
🔻
با تصمیم کادرفنی پرسپولیس، اعضای این تیم بلافاصله پس از پیروزی برابر ملوان، راهی اردو در هتل المپیک شدند تا برای دربی ۱۰۷ آماده شوند؛ تارتار بعد از کسب این سه امتیاز به تیمش استراحت نداد و باتوجه به فشردگی رقابت‌های این فصل،…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/139246" target="_blank">📅 13:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139245">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/139245" target="_blank">📅 13:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrunHVUHnhkNF2NMzNVqVqEXA-FpW0nOCwfTk4NGzGd9uG8mouXdrqzTBCFDxICvTVvPBGCk1n1pud57o73Ikc52XLLdruvPLtaSu5wTw7j_aeFxCMWCfDuQ5H68f8Ly5Aj6r4OqSH_KfNFHbOmfjMFUsH9_31JTQfe4TGil2x0Dh2hrKpSlzRh1RyJBZYPzBQigc6zxjhSycpyq9HxX10af0__9aH2kIrXUi4o1Pjl0kgPsmnp60V7AQwLhdV5RLeetZ43Cxo4R1lXKIC0JRwr63uuRPZNjaPREzISLQEXhTDvdz2sCn9rDvhaz22bCi4u4yXfouf8sfz_pZF1GQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی علیپور با نمره 8.45 بهترین بازیکن بازی پرسپولیس و ملوان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139244" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🗣
🗣
با تلاش کادر پزشکی تراکتور؛ مهدی ترابی به دیدار با پرسپولیس رسید و از روی نیمکت بازی را آغاز خواهد کرد. هاشم‌نژاد غایب است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/139243" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mywPe144r2sG5f8IPj1CVmphPt2RGApa8AToPbYb-ASeisApuN4Q016gq3adGAHz6g3tkIDg_XAe03nC3MIlCgSqovBIiu4KNET0a5mi4eescDUfxDAAx2nAvMzCdfONECHCZLhyFnvjEpq3Wmzw3_bKY7GKUQxdBCqqNbq89U00vQtgfjZjbUVqpgfcTnU_HyDGcENQep1H33QcfAkPmlfb_iCkzFU7yS6qw6gHDLafA6_IV75-xo4LShHprLqTfeHYc0ZyXMAIXJlpPvuXLYpiNuATJmzxT1mQKWbGDPPbpSFUya9idNcMaDKPHkO6m6XyVV8v9D9Q2DSnxAS-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در آستانه ۱۰۰ تایی شدن ؛ علی علیپور به رکورد علی پروین در پرسـپولیس رسید و به دومین گلزن تاریخ پرسپولیس تبدیل شد
✔️
✔️
علی علیپور با گل‌زنی در مقابل ملوان، در کنار علی پروین با ۹۵ گل زده به دومین گلزن برتر تاریخ این باشگاه پس از فرشاد پیوس ۱۵۳ گله تبدیل شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139242" target="_blank">📅 10:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139241" target="_blank">📅 10:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1Vk-3CAFNv9tqIquyuN03L2zLT9m8UQDVITwnHQ9g9rh8dbWos15f8HSobDgWp2EyNN78eEYgHE0x2L3V9W5VNwKT84LTplm_Fr_n1Yx5YXWmPBdDTGdMTWLROCP2bVsGu2RAQ-vokrNnpmfUOqHuYEJZRrcBvWpKm3YTC0Os8ZgYuna_SsgBovgu1ky-nb3rzKN1VptPB1dBDSB6wr9jtMVvl9JUDU9eHkS6KBSC-Nktd8sHI77rcVVVr6lX55hJg8VuNF9FHycOEeSUN58kP592ohF1VlE5S0ownJcTM0dIDXbbwr50uvZOI18MQzx5dTMdw2k5kbW7sRw_N3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/139240" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
اردوی پرسپولیس برای دربی بعد از بازی با ملوان آغاز شد و بازیکنا به هتل المپیک رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139239" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139238" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139237" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139236" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139235" target="_blank">📅 08:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clB09SFqqre6oQ2O7ifCYQxaCnzhU4pkbPpPHg9HVlWIp_-Ng4FGXYVlzt9cHOnI4fUBJjwnzGeWEE5Zy6UEz-UX1WPEaRz6fYny-kQLB8NC733Ut2cmh6zzXOGNqM_JcPZdIU_rbCWKZShCYqeMs1IGdl33aMgkLP8b5cr5WOgW_iA5-QS2cOMRYdquH-qj07kLLL7D7BkQrblODWtAt05UmmUc3aMT0lcKv5om556jyvlM5O3RoRIkwMGT15rt-4ZnAW2sf90dYO9-pcGPQ0QiUZT6IZFjNYuUne_32ZfSVUvCsxqMJupyg8Wu2B-GAAVLZ8a2K2Ro9ogQ6bWoYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ورود به اسپورت‌نود؛ ساده‌تر از همیشه!
🔗
دنبال یه راه سریع و بدون دردسر برای ورود به اسپورت‌نود هستی؟
🔵
با مینی‌اپ ربات رسمی اسپورت‌نود، مسیر دسترسی ساده و یکپارچه شده؛ بدون لینک‌های متعدد و مراحل اضافی، مستقیماً وارد محیط کاربری شو و از امکانات سایت استفاده کن.
🔗
ربات رسمی اسپورت‌نود:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت‌نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139234" target="_blank">📅 01:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139233" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139232" target="_blank">📅 00:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✔️
✔️
دانیال ایری امشب به عنوان بازیکن ذخیره وارد زمین خواهد شد تا اتفاقات دیدار با تراکتور را فراموش کند.
✍️
ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139231" target="_blank">📅 00:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139230" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139229" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJOI96wM896Aeoye-a1mdMpl0Qg4hQ0iysITe_ApPpkPFkdsTSTgJF3JLPHagnmvdGqG233LMxVbjHx5MINafrO0rJdM_a_kJg1-WS7qWUBMnJHlMI6ndIeo-FFSnVyIdFCPkh0gXokLd5Iv9gL5FypvvgpODfYa0DNl8RdMBfYuTjOZyAKIdNVGbkhcx3MmxQ59ITIctxU_Zu69URZaL9UOUdiiU46UV7FQy8A-n-zEwd8IFhgQ2_Nsa3WjTzo7vHSVZZm3FaY7lAaue9HdakZFt2eOZoy0-x8yCw1OgkuXUvxguTdSsPNEZSakMHW3c3VCltsP5gslDDDkHmkeuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
✅
هفته‌پنجم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
طویله کیسه
🤩
🗓
تاریخ چهارشنبه ۱۱ شهریور
⏰
ساعت ۱۹:۳۰
🏟
میزبان نقش‌جهان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/139228" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139227" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
کریم باقری: پرسپولیس از هر بازیکنی بزرگتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139226" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
کریم باقری: نگران نباشید. پرسپولیس بهتر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139225" target="_blank">📅 00:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139224" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
❌
آمار برگ ریزان بازی
🔴
۱۶ شوت
🔴
۶ شوت در چارچوب
🔴
امید گل ۴
🔴
گل ۳
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139223" target="_blank">📅 23:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‼️
🔴
علیپور با ۲۵۷ بازی، از سید جلال حسینی با ۲۵۶ بازی عبور کرد و به رتبه دوم بیشترین تعداد دیدار رسمی با پیراهن پرسپولیس رسید.
🔴
علیپور در ۲۵۷ بازی خود با پیراهن پرسپولیس، ۹۰ گل زده و ۳۸ پاس گل ارسال کرده است. او با ۹۰ گل و پس از پیوس و پروین، سومین گلزن برتر…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/139222" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139221" target="_blank">📅 23:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KsVKCN6jJDFvnRPqa7nqKUz88dxQhewScdH2NeU58AbA3OH43MyB8xkGBcDSDIW1iW7FnhrsxyYDNLGo3ESNX9ffTO2sZd8wkrEwJO6phgCZnF6d_Mg8nNGeMSawghdGNI2E9ndUUhOTsIDrfvrNZ2GZRTesN2-lGnx-UfWraRh3C0X_tD8MeMfhgR8_CN6dYvx3Qdq1IdiYNGbUlk4AyLSWFdK_8jeGBZTDb2iCO2TswU2b_6XGv1NDcUWllO4_qn2K8MZkBDIBMeia3ngKxs3-2Ee1Nxwr4V-WyL18271uZodESP52BwZmU70MPAmVuyaryEIfakQYKLfxIWl7Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
ستاره این روز های پرسپولیس تارتار
📊
عملکرد بیفوما تو این فصل
🔄
4 بازی 1 گل 1 پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139220" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139219">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/139219" target="_blank">📅 22:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139218">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139218" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
کریم باقری:
🔹
به زارع دوست عزیزم تبریک می‌گویم؛تیم خوبی دارد و ضد فوتبال بازی نکردند.
🔻
خداراشکر برنده شدیم و توانستیم با روحیه خوب به پیشواز دربی برویم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0HEuRXh46g7xw9MTfY-UsiQbqmc3XL93bEBQWB4mQPSSdzuV5H7OS0ykdsMBN4anYRoQ2KuUEumq4WH3mNlLj0PvVNSgug1V3fmftQmjtJ4rhEm6dfZ9IYNWzq9jOoWte1vdoNLh636k876d2CJo5KJBny3BVfpAec9ZOk1EZVB_k2UjvN1THmsRlANDnfl7vCwhObkcQwhH-zGV3fykSM98MhsOIJUU6DKKotvYIv3T-EsxmjdGDhs3Pt40JfDPR9uVmfZjchf6K0efxZa19t400vHOhHwPSKt1CKN75CRpAQLqbJ_s-GN5glalvG1gYkeDKGUInSf8BnH0XZqKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
پیمان حدادی بار دیگر این استوری رو گذاشت/ حسبی الله : خدا برایم کافیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139214" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به دلیل افت فشار در نشست خبری بعد از بازی شرکت نکرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139213" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✔️
✔️
گفته می‌شود فردا نیز مهدی تارتار برای دفاع چپ پرسپولیس از علیرضا همائی‌فر استفاده نخواهد کرد و مهدی تیکدری در پست غیر تخصصی بازی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139212" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/139211" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139210">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=ldp6PZbVeXzLCDzjfHKZuCclcBpCq6t3EyTN5wWyk-Qdetl-kbL7El31C_fxV00kMzuVCZh56onzPrRwpYnF8KbO0wjUIB6Uy0F8jM4Y9zVEVoaYWMjGoup2zSFmJT6JlqMuIAwYBH8kyVpoCJNbeytRqKbMOoTLMZufxC6ywEJr2CqYIU_awn-wiihRyBcmp6q8k4mys64m2N_jclJTvDw3ezPjlrGxTqD9Hqzi87lGRPRJYI84u-4eUSQoYDp1LhzPBsC2qPEryW7GFpGbHy2eHAnz_cNgcaQFyiM98499unhynTu_a_5yDMf2-kg9-JcLi5C2d8Q6JXIKEizzUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=ldp6PZbVeXzLCDzjfHKZuCclcBpCq6t3EyTN5wWyk-Qdetl-kbL7El31C_fxV00kMzuVCZh56onzPrRwpYnF8KbO0wjUIB6Uy0F8jM4Y9zVEVoaYWMjGoup2zSFmJT6JlqMuIAwYBH8kyVpoCJNbeytRqKbMOoTLMZufxC6ywEJr2CqYIU_awn-wiihRyBcmp6q8k4mys64m2N_jclJTvDw3ezPjlrGxTqD9Hqzi87lGRPRJYI84u-4eUSQoYDp1LhzPBsC2qPEryW7GFpGbHy2eHAnz_cNgcaQFyiM98499unhynTu_a_5yDMf2-kg9-JcLi5C2d8Q6JXIKEizzUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139210" target="_blank">📅 22:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=rUz9Jn-AHA-I7yVXJu8Tb1d0y5fdETy1aZ-eEfSZMyEqQ1B4NFyr0H_bHJuy2jqRUnkedgEWtWCzwojxj81ruMEOxNQ8kiLH7G80qDvnFJotSvNTLXP6oIHzSFZ10-Um71YNkErm_Mk5BZOOk1gXy0qN2qybcDXsISy4K_5yikFTTaIkM_E0XXVKl1ue6eXTsH5clGPScUPL0HX4RB4HwnvLQvXIeM0IKkT8xGYOaL1GdToG_nqjPMADOf2CGesozfIJBs_Rp7hxIlkUnwiOa429OOJwV33hODZOxfnc8tmIt829ZFtSUWrZnb4_aDt3C6eWOHYtgUg8FKXiakEjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=rUz9Jn-AHA-I7yVXJu8Tb1d0y5fdETy1aZ-eEfSZMyEqQ1B4NFyr0H_bHJuy2jqRUnkedgEWtWCzwojxj81ruMEOxNQ8kiLH7G80qDvnFJotSvNTLXP6oIHzSFZ10-Um71YNkErm_Mk5BZOOk1gXy0qN2qybcDXsISy4K_5yikFTTaIkM_E0XXVKl1ue6eXTsH5clGPScUPL0HX4RB4HwnvLQvXIeM0IKkT8xGYOaL1GdToG_nqjPMADOf2CGesozfIJBs_Rp7hxIlkUnwiOa429OOJwV33hODZOxfnc8tmIt829ZFtSUWrZnb4_aDt3C6eWOHYtgUg8FKXiakEjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
👤
🎙
ابوالفضل جلالی:‌
🔻
حضورم در دربی؟!هنوز هیچ چیز مشخص نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/139209" target="_blank">📅 21:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxd10KrJOYDvTjgWRSgEeyXQhMR-W5cGKyCXOnZ5uaEn49EB6pbg98TWo_eyKlN3bpGeR30M6J3yu3E6f9Ov4Qi_bAgFOn0ocZIXAilf0kOm7kqgNzuCRvFYDPCvoN47q46KAJ8mupkrg0Mo2maaAUe-Jv6UnoNneV687rVaKS4Emf3Owm8UFpWhU9ldncjQKb_Y-f6lb1lTuAAyH631UpxwdVjvNOGe9un2gk1wsypr3AnjONMMdiJUvmKPdWY_mcnUHAN84eJ7L3mODgjbEAVSqKQ-55xgeRh9ETMVK_UNYEal2xUSKt_YNWPN-HbmU7zFMcObelsIiP8lK9fKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/139208" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Y1iorc8nYgasZdmAdlN8zNNbljXzjIUelkCZvAp3qaWl8Jp7oQ8CsVXqEC3Ir7MceMoYG1_28avTuEqd6AhoLmd3PnYJWejxP2EhPOBHj---GdZPdvhE6RWIadUDLZ3l_5k4UIee-gyZNa-X58IfZWojAlnipCoWlj8JEcMqm6IHJ-gZyLTm8Q1S2m9_bjLxQSZsNyKNraRt9iNIiolGTweahTpclCGjUtQLmUQ8mZRueV9GTv-O5ARXDUqHsmAEdjZ1laoeUfuHA-P57csXlUa5zu-Cn3ZA1yVocsE9Aiu4ABSZBA8Ki_AOivk6rywxnvSLNzq8hyK6LFD_bRjpBxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Y1iorc8nYgasZdmAdlN8zNNbljXzjIUelkCZvAp3qaWl8Jp7oQ8CsVXqEC3Ir7MceMoYG1_28avTuEqd6AhoLmd3PnYJWejxP2EhPOBHj---GdZPdvhE6RWIadUDLZ3l_5k4UIee-gyZNa-X58IfZWojAlnipCoWlj8JEcMqm6IHJ-gZyLTm8Q1S2m9_bjLxQSZsNyKNraRt9iNIiolGTweahTpclCGjUtQLmUQ8mZRueV9GTv-O5ARXDUqHsmAEdjZ1laoeUfuHA-P57csXlUa5zu-Cn3ZA1yVocsE9Aiu4ABSZBA8Ki_AOivk6rywxnvSLNzq8hyK6LFD_bRjpBxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
دانیال ایری، بازیکن جوان پرسپولیس به سمت هواداران ملوان رفت و به هواداران تیم سابقش ادای احترام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/139207" target="_blank">📅 21:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bxusjb-rKii8r2_6WeDmsscwCSI79ErNm5yPoa9eDvURhHf6SYkc_JxBc-SQmj7tyragpXFb-9H6otlDkI_7R-bIi4JrvRjEMXA1b6KWgM8oKzMB3wUBKyje9F8MIMCVAFP2BqMHHgOG4g4OTxzsxknlN7f375GYFLYOuuF86oCCLFPKbiPk0aIz0XsKhhnS8hordSquGYL2vNbvOkgxSyBIYde6qKXELYfuY2N_Iot0BzBEZ2C7K-XcwEPIvp0OKy7tQthx8RtzeXwvpu0huTdcsvKE5x3vW23gkuHQeAMGM6_swD4WWI5ost0nZi92lIZWx5TL1Ku2J7xsnZ405A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139206" target="_blank">📅 21:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=TWAXgmPctQJCA_cU0UuuKk1MOCxY3DeWDeyKiOrRP5jgK4KIyYxA92Mj4E40H_-_Avew0chpS_-DBndcSX0aRqLFpAbTCITDi7m3K8OJGP13Ie_mwKdCXf6lGIL0nc8Qg7CB4tjSwBQ9M7a5taGbBMygLH7gduWAROoCi2WrAhxFmbMFzd4W9UGXkQBxcVgfAWUkTrOLhPtsizitlSwSXFXWL-9JrBsWzp7NYghkrBuqvqaweWnWUZZTdvS7r9mWL_JgNXaKmJbOKp9PfJI88yq-xZ4PbXndQnPue5CYfUQbH3yLS5Z6mBvNreBGrf9sjyfTXCEZ92PTN8AyJImyJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=TWAXgmPctQJCA_cU0UuuKk1MOCxY3DeWDeyKiOrRP5jgK4KIyYxA92Mj4E40H_-_Avew0chpS_-DBndcSX0aRqLFpAbTCITDi7m3K8OJGP13Ie_mwKdCXf6lGIL0nc8Qg7CB4tjSwBQ9M7a5taGbBMygLH7gduWAROoCi2WrAhxFmbMFzd4W9UGXkQBxcVgfAWUkTrOLhPtsizitlSwSXFXWL-9JrBsWzp7NYghkrBuqvqaweWnWUZZTdvS7r9mWL_JgNXaKmJbOKp9PfJI88yq-xZ4PbXndQnPue5CYfUQbH3yLS5Z6mBvNreBGrf9sjyfTXCEZ92PTN8AyJImyJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تشکر اعضای پرسپولیس از هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/139205" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس ۳ - ملوان ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139204" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139203">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
به به چه فوتبالی .چه پرسپولیسی ...سه گل زدیم و شش گل نزدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/139203" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
تیم  دقیقه 98 هنوز تو حمله اس و تک به تک نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/SorkhTimes/139202" target="_blank">📅 21:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❌
❌
تیم سه گل زده هنوز سرتاسر حمله و تشنه گلزنیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139201" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
اورونوف هم تا اومد تو زمین ی پاس سکسی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/139200" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
✅
بازیکن ملوان اومد تو زمین سلام کرد و بلافاصله اخراج شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/139199" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚽
🤩
سیو تماشایی پیام نیازمند…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139198" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6343db8016.mp4?token=V8d_bkP5zrid59rlyFIm2UxTAJEhYirm4L2GKUYK1mo06EcMRhDlJW5wDzySO19hobeEYKAHQQIR2ikoZoosqYTwT8FjkSgXNZz5-VyMUQ5rTY7X6sk41YST0hOPbvAguvmNKE7k8U59uwN_Eee2XBMPl-CQaKfGQVKgVJDZmC-jS4NDySvYpI7MC2rd4oCXHVdVPTdQgDlL7FMwt9fCw-HMA_b2xEaDNCgCKN5qbl_lvGE4M9ENYw4aAhIEqjgsC0AkHGyWX9t1r5d9rikw8LtfXuSvDFEPCzMYZMwO8dqdIII2i8KMqPZKI8yYI7I4A7ulgWA6cOwbq5qpa0kgWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6343db8016.mp4?token=V8d_bkP5zrid59rlyFIm2UxTAJEhYirm4L2GKUYK1mo06EcMRhDlJW5wDzySO19hobeEYKAHQQIR2ikoZoosqYTwT8FjkSgXNZz5-VyMUQ5rTY7X6sk41YST0hOPbvAguvmNKE7k8U59uwN_Eee2XBMPl-CQaKfGQVKgVJDZmC-jS4NDySvYpI7MC2rd4oCXHVdVPTdQgDlL7FMwt9fCw-HMA_b2xEaDNCgCKN5qbl_lvGE4M9ENYw4aAhIEqjgsC0AkHGyWX9t1r5d9rikw8LtfXuSvDFEPCzMYZMwO8dqdIII2i8KMqPZKI8yYI7I4A7ulgWA6cOwbq5qpa0kgWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
سیو تماشایی
پیام
نیازمند
…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139196" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139194">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=uo2B9p-UWI0FlQ5-i5vm4CdnF_w5he6ntYqv9sSxk_3KBaByR7xOs9tZBubFN2TPeK5YoCJs9HfTABKwX6b4x2Wil2GflUnGHnfkq6WQhRnj0MPMF-kHs_Ag3o9zVNNBSMO7jUWvNL3FpmvItGbWXnKD34jAPQ72dzrR3WB6vkLzWjDwPHr4uKT0VhH0XtkXH5lmNdAkz1ZpaiQNL8v7MSm4urEEW7W2n9uud4hzCxyXDx11KuO9eQaCYhKNYp3EyOc-dEq2iA-JCSEwcJi9-Fyb2YDfNYnRngh4m4BvXrBE8lVsgAzedjdyzR7p88FC6tkILQKibsDpi01GrDgL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=uo2B9p-UWI0FlQ5-i5vm4CdnF_w5he6ntYqv9sSxk_3KBaByR7xOs9tZBubFN2TPeK5YoCJs9HfTABKwX6b4x2Wil2GflUnGHnfkq6WQhRnj0MPMF-kHs_Ag3o9zVNNBSMO7jUWvNL3FpmvItGbWXnKD34jAPQ72dzrR3WB6vkLzWjDwPHr4uKT0VhH0XtkXH5lmNdAkz1ZpaiQNL8v7MSm4urEEW7W2n9uud4hzCxyXDx11KuO9eQaCYhKNYp3EyOc-dEq2iA-JCSEwcJi9-Fyb2YDfNYnRngh4m4BvXrBE8lVsgAzedjdyzR7p88FC6tkILQKibsDpi01GrDgL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل سوم پرسپولیس توسط علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139194" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139193">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❌
❌
نیمه دوم نکشیم عقب پیروزی پرگلی قبل دربی خواهیم داشت‌.......
✔️
✔️
اقای تارتار یاد بگیر اینجور شجاعانه بازی کردن رو تو بازیا بزرگ نشون بدی
✔️
✔️
همینجوری جلو استقلال بازی کنیم بدون ترس پر گل میبریمشون
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139193" target="_blank">📅 20:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
بریم برای نیمه دوم ...بریم برای زدن گل های بیشتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139192" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=t7zW-j4T3z2PA263NzsWH39C9y8o8rT5WwjhfEUYf3wU2UUwFFFqWLijFLM-9etonWalyCLZTj2KpShwxyhKYrVA6nDeUYRA9_VvJMp-SMwyi5fQylAvDFj5jrqAZM6NUoblVzrifv-wKV5ArSp-FhttPWYt53ZkDBIFnoTSDay6fTs3nZ5jtESJ-iTOJ9k7s6cXuOHbX-cvg5r1xN6w-qCxptri2Xo02W3hYCghOvSdoSebX3Ib82fmRvM_zV9xwr1LIPyuvhEzs8qCwdSeHRNZ6STmZI18r6fZX96QWAoRy_rJKm3hjZmtuQF1NiTDCowa1xtefN_il26YhIwzdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=t7zW-j4T3z2PA263NzsWH39C9y8o8rT5WwjhfEUYf3wU2UUwFFFqWLijFLM-9etonWalyCLZTj2KpShwxyhKYrVA6nDeUYRA9_VvJMp-SMwyi5fQylAvDFj5jrqAZM6NUoblVzrifv-wKV5ArSp-FhttPWYt53ZkDBIFnoTSDay6fTs3nZ5jtESJ-iTOJ9k7s6cXuOHbX-cvg5r1xN6w-qCxptri2Xo02W3hYCghOvSdoSebX3Ib82fmRvM_zV9xwr1LIPyuvhEzs8qCwdSeHRNZ6STmZI18r6fZX96QWAoRy_rJKm3hjZmtuQF1NiTDCowa1xtefN_il26YhIwzdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
علی علیپور موقعیت خوب پرسپولیس رو به بیرون زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139191" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139190" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adad84121.mp4?token=eLSf8pGd3Zhd36g3aPORGgf0_JqIXv6KZnFMN5UOV_Yp45gfM4Y0kpBMSD61Riqmnt1Q7Wij1j6_4RnStk6c3cZ8wF025bVmxorHofw2ihD3eytXjPNRWeOHIjD3qxhU1F8uBsl_P3unBGCdGZXsw_QYoSqHntwGNtRQsvREOneUtGUK8MpWgrN4gsyqLoGVoWcmqG9xqB-QTiUL8cWHyPFOsQ-fFIq4KvqzDAhfjC3l--qFo6vdOZFGdUXeREvYAP2RIS-0L_KJChQW-ot1cNsR_bj0O13JZVkjqJb1yKRelFrrNBuDd76QMvvy4kVA9I7lShJsgH8F5putR4WiQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adad84121.mp4?token=eLSf8pGd3Zhd36g3aPORGgf0_JqIXv6KZnFMN5UOV_Yp45gfM4Y0kpBMSD61Riqmnt1Q7Wij1j6_4RnStk6c3cZ8wF025bVmxorHofw2ihD3eytXjPNRWeOHIjD3qxhU1F8uBsl_P3unBGCdGZXsw_QYoSqHntwGNtRQsvREOneUtGUK8MpWgrN4gsyqLoGVoWcmqG9xqB-QTiUL8cWHyPFOsQ-fFIq4KvqzDAhfjC3l--qFo6vdOZFGdUXeREvYAP2RIS-0L_KJChQW-ot1cNsR_bj0O13JZVkjqJb1yKRelFrrNBuDd76QMvvy4kVA9I7lShJsgH8F5putR4WiQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
در بین دو نیمه اورونوف از سوی طرفداران پرسپولیس به شدت تشویق شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/139189" target="_blank">📅 20:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/139187" target="_blank">📅 20:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SorkhTimes/139186" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139185" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=lyhNfqQvTfuDYcXQB5nkaWTmOT4wcEJDgdrvu4YfEX4uJwF9zpSwlcJIbgLe-fEw268376w5ngY1bEAUmADhstv_Gc189TKcXWXovk4A_ejaARqWksl-rTYKdR0gYwt4lxJjs7XSdtQVQjJHe_fc7Qz59q-ErO3ZqkT4SkDx1LnrldIKETJ7nSIaXAV6iH5mwa0ls0OEF5F5m7Sp2tltY_O9cwQClAmUnQsFmo-Z1_FORDIxxCz4-oBXtNN6sJowUepS52k8o446q7h-T8BvMdQeqCqlDlnb0q8P2crp-lkVgOuxvquE96BFpkIpM25gAooRLPmdfjVD1Qjl_SupNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=lyhNfqQvTfuDYcXQB5nkaWTmOT4wcEJDgdrvu4YfEX4uJwF9zpSwlcJIbgLe-fEw268376w5ngY1bEAUmADhstv_Gc189TKcXWXovk4A_ejaARqWksl-rTYKdR0gYwt4lxJjs7XSdtQVQjJHe_fc7Qz59q-ErO3ZqkT4SkDx1LnrldIKETJ7nSIaXAV6iH5mwa0ls0OEF5F5m7Sp2tltY_O9cwQClAmUnQsFmo-Z1_FORDIxxCz4-oBXtNN6sJowUepS52k8o446q7h-T8BvMdQeqCqlDlnb0q8P2crp-lkVgOuxvquE96BFpkIpM25gAooRLPmdfjVD1Qjl_SupNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
مهدی تارتار و کریم باقری از گل انفرادی بیفوما به وجد آمدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/139184" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙖𝙢𝙞𝙧</strong></div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/139183" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSana</strong></div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/139182" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahand</strong></div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139181" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139180" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139179" target="_blank">📅 20:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/139178" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dThV7NS-fU0IxTOi6mXWM6pbZ9lyU9jFfLdcaW2UcBE1eszuJaWWzMmtze-eMUdOb-6gtkDsf8kZkaZAKDtYgboPEPep30NlFnDTOoqZiPrhBvhE5Z5-7QlIFntPj3KCqX__w4Z7pjJn4cveTrzEcOTHzAOOdMu8hxXF2iTKM-6yZ0azGY0Rm_LVTp8vyS5zC5hBZncJDXar7yMh1TBmerOgYLaipcUQVPOOUdpqCmJ_iyLc7P29ax5jClpKb7Qd1SCVVX7jHsRyyo9evJXlvIOB40zNAKhXHCRtSpUfCbqLaRXSHeTk-6GTZQ9fEcQoIGOZGrJXoRWTby_KQIIrdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/139177" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkxRncxXzZCLpyjXf0Ia2j9OF0zdFjcWubwcki4i9g_6a4DrkW6YrkmojHHQS5rsVJJZvZ76G_T5PhPPyHRgZKwRYhcH9Fe3Me7K1wF4h-XkNr9M-Q8vOS96-DUcs_DwT9MV7lmbbVyRTxu0FyMdzmsT2ViUZnOyl_fTsS_-SqY1u8lfDsuvKDOWp6H2_dsu16iQt82NfqTKe7UIReZSpywE-tBNfEI5GkpYRnSM4WCfxKE41xpQnT4MLNgstn6YHaGABtmVWOZHo_kfe2sl1ooeTwoVk-BStFpdb7cmqAsYiEn5UOEBMLO2rGJkTyfqUNU16UDoTnDu0ktiG5nslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یووه در تورین دنبال دومین برد فصل؛ پارما هم برای جبران شکست هفته اول آمده!
برتری کیفیت و امتیاز میزبانی با یوونتوس است، اما غیبت ییلدیز می‌تواند کار را کمی سخت کند.
نبردی که بوی برد یووه می‌دهد؛ اما پارما می‌تواند برای مدعی دردسرساز شود
[
یوونتوس
⚽️
🆚
⚽️
پارما
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139176" target="_blank">📅 20:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">✔️
✔️
پایان بازی در نیمه نخست
⚪️
پرسپولیس دو - ملوان صفر
⚽️
گل‌ها: محمد پاپی(گل‌به‌خودی)، بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SorkhTimes/139175" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
❌
❌
خداییش دو تا زدیم سه تا نزدیم .عجب تیمی ..چه استارت هایی چه ضد حمله هایی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/139174" target="_blank">📅 20:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139173" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=lWfB0M1pBFF0qwhJURHw4p3-NTB_-CR0IFGySHC391I7ce83wz_cn05SrXhRKbrKOi0K7stZe4LlnI9lyUzo8MWxQ_pt4FS_dvJuiDI3GUDMo2eoHLxvnQBuFi4-Vx0qadGbuqgSfpww7rPeeI1-jpsiTyewmS04md9xLjCHt1e3CBzu3YW0z7gz2ySwBe-mfy4h9t1MKsYQLDz5NeEYOnF8Dot4dPHG0L3_r8o3Yzp_Q1Bt3SJY7Ft31y7egjXiQdUXxEHbXZiSbkQ9eg9-mf9hOoUE41pxYzdNFkk_YKJtfBcVpVbU365tp0r5RBu2EiTQPAnLYEMdO2YjDZkq6LlqbEhEFvvfjn4VooWxeKa2JqsObhmp7A7bk31ZdMMVhPBEP3ptLl5V_5n0ioEIODcS65n3AfQYzimk2wuWTwiXEW0XuwO9Hu-GNsCiOXPi3W_SIvtkGidmhKnzYJNiAdKQTzzWfMdkMLeLdMPG4CSPHhNaIslU-TWc69EUjoLED2-udO2WeP8K3-5errgAzJJfyfqx_DZf2V0l9rMEizBintDE1X3e7krJmcQalk40qVq22UsYzEiKL9c8odegx2vOQDFnJ53l1SWKuOAYU2JHlSCZfbIV5TaFy9T79-OroQ6XK9FFXPpmXorKBA4hdz6xx-VtHw_6tZtv7dWqTlM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=lWfB0M1pBFF0qwhJURHw4p3-NTB_-CR0IFGySHC391I7ce83wz_cn05SrXhRKbrKOi0K7stZe4LlnI9lyUzo8MWxQ_pt4FS_dvJuiDI3GUDMo2eoHLxvnQBuFi4-Vx0qadGbuqgSfpww7rPeeI1-jpsiTyewmS04md9xLjCHt1e3CBzu3YW0z7gz2ySwBe-mfy4h9t1MKsYQLDz5NeEYOnF8Dot4dPHG0L3_r8o3Yzp_Q1Bt3SJY7Ft31y7egjXiQdUXxEHbXZiSbkQ9eg9-mf9hOoUE41pxYzdNFkk_YKJtfBcVpVbU365tp0r5RBu2EiTQPAnLYEMdO2YjDZkq6LlqbEhEFvvfjn4VooWxeKa2JqsObhmp7A7bk31ZdMMVhPBEP3ptLl5V_5n0ioEIODcS65n3AfQYzimk2wuWTwiXEW0XuwO9Hu-GNsCiOXPi3W_SIvtkGidmhKnzYJNiAdKQTzzWfMdkMLeLdMPG4CSPHhNaIslU-TWc69EUjoLED2-udO2WeP8K3-5errgAzJJfyfqx_DZf2V0l9rMEizBintDE1X3e7krJmcQalk40qVq22UsYzEiKL9c8odegx2vOQDFnJ53l1SWKuOAYU2JHlSCZfbIV5TaFy9T79-OroQ6XK9FFXPpmXorKBA4hdz6xx-VtHw_6tZtv7dWqTlM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🎥
گل دوم پرسپولیس به ملوان ..استارت انفجاری و برق آسا از بیفوما
✔️
توسط بیفوما 33
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/139172" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/139171" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139170" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGSVpIysgmEoXy4E65FerEgE45ZuPsTl0XxonVt8CzYm-PIpAiDkU8DkUcu-kWiTr3kh887CPj_SVghQisNouFdDtHX4Q-hePX_gbak4rCkvPRWhIX4YJ4oIwDYDVKk1zucxMOR-xQf86EiRqc9mxSRdq_VFxe3nQYMds7YCmismyr_9DXNOssHQ0RCWUx9u0AYyu13q-kAQIJtAcKGRekUtqdRk7XG08e1TDEFnROGUm3_INWIFelic5GXucG5z2wAOEFm3FfuA7B9K3R0rIGupuhT_ZsN2-_KdDdGBKk9h8cbXgw5d8oaW1vqLaVQWEY-S287AYnU-yclJwsL16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139169" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=c6pa0PglvNA5iN0Dl-dskSH7JBZMvjd0hzkFxOML-Rqn_4vHP5fAfERdB6hACvziXkum4eXyc3jCZc6bijzh_LKnK11Envq4p2x-Auw7sIolMJ1LeNJpBtEjsVPdJyKGtNobY3GiwCxD2c7XYEjNW-Kb239KVGTejYsxAPJVL27FksVVUuZXHibOGAO9dY0KttZHHX-c-w6IPRqRaUJ5QGsGyyud53vZkVpDCMpr-6BocUv2Ro-tkVexbPK52pvHnwom1tjTcJBnPS8VCntbOCxCJiOq_tATenfk6filnICcefQXVDP6y9sUHjfD3NvEN5FCLHPD9xss816HqOYL_oAnNN0w1Qa4I9CoRbkY3WO6mcfKOeEQtKeaECHQxlyW_qO3V1rw9chuya3uSLmjDoIL97qySNX6Q_Kb9spqKwzD1cfHatb4qYjJqkgB0iKPBnEx6x74v9wTqro6MDKDgX-W5dde3NO2X9WUipsjX021Fbk2B2RjcI-7GkMFVlTZ_QPQUoSxgdVPezr3H-7qflJexC5a5GNlrYlNGYKmchDglG7vEdQ9GmbuBt1nXGv019ipmoTgpluzI30we325i5jp1HEsjsxZKS07svyEBr-5ZzALaABvAi18zXSUa7Jsi5P2j89rd-ohssWXkE9icFz2TNpfmr9Di1NjxZfVODk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=c6pa0PglvNA5iN0Dl-dskSH7JBZMvjd0hzkFxOML-Rqn_4vHP5fAfERdB6hACvziXkum4eXyc3jCZc6bijzh_LKnK11Envq4p2x-Auw7sIolMJ1LeNJpBtEjsVPdJyKGtNobY3GiwCxD2c7XYEjNW-Kb239KVGTejYsxAPJVL27FksVVUuZXHibOGAO9dY0KttZHHX-c-w6IPRqRaUJ5QGsGyyud53vZkVpDCMpr-6BocUv2Ro-tkVexbPK52pvHnwom1tjTcJBnPS8VCntbOCxCJiOq_tATenfk6filnICcefQXVDP6y9sUHjfD3NvEN5FCLHPD9xss816HqOYL_oAnNN0w1Qa4I9CoRbkY3WO6mcfKOeEQtKeaECHQxlyW_qO3V1rw9chuya3uSLmjDoIL97qySNX6Q_Kb9spqKwzD1cfHatb4qYjJqkgB0iKPBnEx6x74v9wTqro6MDKDgX-W5dde3NO2X9WUipsjX021Fbk2B2RjcI-7GkMFVlTZ_QPQUoSxgdVPezr3H-7qflJexC5a5GNlrYlNGYKmchDglG7vEdQ9GmbuBt1nXGv019ipmoTgpluzI30we325i5jp1HEsjsxZKS07svyEBr-5ZzALaABvAi18zXSUa7Jsi5P2j89rd-ohssWXkE9icFz2TNpfmr9Di1NjxZfVODk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139168" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=MkEmXGXoEg4IuK46IXDBHs5BNzewA56xHeXuayFdOMK0sgKfYOLL1ieCLd-R5UAuUHXz7hlCyoibSk0wZl6TPdUy7CFefPlgYX85e86TGRgTF-symmGi1BVX_GaKHZfjxJMCVXGciUGLkjembdVOK3FIZToz8h1nhYI82dhZszZg4WFZ-Cb3WyFYrBcMx17uEjMw5QSnSj58pSkC9UqOAWB3SIZyL05QQc1_2plSJHIugmGaTSDu-p2fwE_OujWELOGs8MNWrtzEVJCoqGCUGoKgsZq5LdkX2ywMxIvOqYJ9M8oft4eDz5Y8M7f-rxnluvpIRBd-sPLvsSmL2EsSPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=MkEmXGXoEg4IuK46IXDBHs5BNzewA56xHeXuayFdOMK0sgKfYOLL1ieCLd-R5UAuUHXz7hlCyoibSk0wZl6TPdUy7CFefPlgYX85e86TGRgTF-symmGi1BVX_GaKHZfjxJMCVXGciUGLkjembdVOK3FIZToz8h1nhYI82dhZszZg4WFZ-Cb3WyFYrBcMx17uEjMw5QSnSj58pSkC9UqOAWB3SIZyL05QQc1_2plSJHIugmGaTSDu-p2fwE_OujWELOGs8MNWrtzEVJCoqGCUGoKgsZq5LdkX2ywMxIvOqYJ9M8oft4eDz5Y8M7f-rxnluvpIRBd-sPLvsSmL2EsSPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کری سنگین هوادار پرسپولیس: آخرین باری که استقلال دربی رو برد دلار ٣۵٠٠ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139167" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=f4mbkmgOIrXLl0UyrvKElmXpxJdjvbBzQWQNCd4x26eiIJVg4AkHEkqzsZ_7RtY7RLCIy54h1G1iLhtjh0J_VvR4CDzese2x6Zt9KaVTx3v4HkdpjRg75RxO5et0fseH-LkpiFRuTT2YXXellK10mGjFhC7n8S6dgFFHYPZoBmRZ2iRpGnFgsUx4mQXENqxhCgiEle2LetHBUxBnW27ONz1h9x51-3RKzoTjJc9Rva3PHwbxBOx_0IUz-TP9YbE6xu5zss-LwJ5MjhX_NfYYt6E-ZMnOKASJpxSvHdBpyRDeGoGtY0VOTCBvFj-auOloTvhTwOMClK7ndJjNdvp_XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=f4mbkmgOIrXLl0UyrvKElmXpxJdjvbBzQWQNCd4x26eiIJVg4AkHEkqzsZ_7RtY7RLCIy54h1G1iLhtjh0J_VvR4CDzese2x6Zt9KaVTx3v4HkdpjRg75RxO5et0fseH-LkpiFRuTT2YXXellK10mGjFhC7n8S6dgFFHYPZoBmRZ2iRpGnFgsUx4mQXENqxhCgiEle2LetHBUxBnW27ONz1h9x51-3RKzoTjJc9Rva3PHwbxBOx_0IUz-TP9YbE6xu5zss-LwJ5MjhX_NfYYt6E-ZMnOKASJpxSvHdBpyRDeGoGtY0VOTCBvFj-auOloTvhTwOMClK7ndJjNdvp_XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
ورود طرفداران پرسپولیس به استادیوم شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139166" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76152fe425.mp4?token=CNbc6RfTClr75QesLfbS9Q-WvoaeTB9gLIOKkbqa5lpPMsKLJdKMNlYEtDB1O2I-DVcAhu1bRDX_i1Mv23XVc_F_8375TpMp7wB1Et2SXOJLb9dSuUDP79PlXMSrG7yI7AD11RfzwFLukh0jw-TveJdJHMaCBADehYHHe9IpP1q4_xZIVKmKWtYP1Gelx-ndpO9F4petKaPbi9dU9cUH4G-qN9DJkEzsjk05sLTeCXXNn5lVItVSqknOOmXJpPKRyxmse2lZW4JZRMiaUT9iTSSJzh2VNQZMrW5PJSBZFgQ5WWYfVKDF6gtj1qDCwiYoZ3q-wv0Jn5q77CerwZhUZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76152fe425.mp4?token=CNbc6RfTClr75QesLfbS9Q-WvoaeTB9gLIOKkbqa5lpPMsKLJdKMNlYEtDB1O2I-DVcAhu1bRDX_i1Mv23XVc_F_8375TpMp7wB1Et2SXOJLb9dSuUDP79PlXMSrG7yI7AD11RfzwFLukh0jw-TveJdJHMaCBADehYHHe9IpP1q4_xZIVKmKWtYP1Gelx-ndpO9F4petKaPbi9dU9cUH4G-qN9DJkEzsjk05sLTeCXXNn5lVItVSqknOOmXJpPKRyxmse2lZW4JZRMiaUT9iTSSJzh2VNQZMrW5PJSBZFgQ5WWYfVKDF6gtj1qDCwiYoZ3q-wv0Jn5q77CerwZhUZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
روش جدید ورود هواداران به ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139165" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=tlLTJL2OzJ0rDbwmQEdYVnb5nGAC_zLr6gv2hiS5PdkvWSKRArShIepXYLJOHh1Wpj0v1A6PAgXD2bc6_u6oBdziRLrd1MgpsbyG86LHf1V1HF06ASIS8nP7uDWpGZPT9P9dwnYrC94nRo-Kr-W6NnvbfLiY1-JSxFrrEVg2GkolbrAvr7ixsTKTqRMK81I8s6vWLrqq12d1JEZGz71sxGWFCyndd-9HRMHTjkz1VLBXcXn5SFzF09Zjpejrt8zzhk0yU_gTbrkRxJ22RifbiOABpP9JKlH9okrm_9bMW7tWuf8nR8cabQIX0QImCk5LZiAlYsHoRS_7-smRP-Y5gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=tlLTJL2OzJ0rDbwmQEdYVnb5nGAC_zLr6gv2hiS5PdkvWSKRArShIepXYLJOHh1Wpj0v1A6PAgXD2bc6_u6oBdziRLrd1MgpsbyG86LHf1V1HF06ASIS8nP7uDWpGZPT9P9dwnYrC94nRo-Kr-W6NnvbfLiY1-JSxFrrEVg2GkolbrAvr7ixsTKTqRMK81I8s6vWLrqq12d1JEZGz71sxGWFCyndd-9HRMHTjkz1VLBXcXn5SFzF09Zjpejrt8zzhk0yU_gTbrkRxJ22RifbiOABpP9JKlH9okrm_9bMW7tWuf8nR8cabQIX0QImCk5LZiAlYsHoRS_7-smRP-Y5gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چمن ورزشگاه قلعه‌حسن‌خان کوتاه و آماده میزبانی از دیدار پرسپولیس و ملوان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139164" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139163" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✔️
🎙
روشنک مسئول مسابقات لیگ برتر:
✔️
✔️
شاید جام حذفی را امسال نتوانیم برگزار کنیم، هدفمان این نیست ولی شما ببنید چقدر امسال برنامه‌ها فشرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139162" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=jZWqISDkrcESpJ71BQijohU7e9tysRZOOXQmfoUWfNnIU_AjWRPtlqOhB1Q0PgS3BxRzvGTc4GJNhMWlpanq8aKItb3z8Q1E2M-m_JXNHk0u3AtXzw1GcKhy54w7lLcU9ofBX2h1moHIX1Zeg9NI2qTtY9WZ6wa239e6GbqTY1ug5EvwIVCr8s7ePFR0cM12-iksz7jumKv9f-l0-Op927GEWaklFBSshOcWg2nCjKWv85qlWzHef4m11zlDOv8uOzX4vwsXsa9jyu0H0S-7kBde5cQJd3OpzlmUy4gzhrvLn5U9VR6Vd4eTVRB4gmweZmbCIYBoGq0qTZDatA2GHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=jZWqISDkrcESpJ71BQijohU7e9tysRZOOXQmfoUWfNnIU_AjWRPtlqOhB1Q0PgS3BxRzvGTc4GJNhMWlpanq8aKItb3z8Q1E2M-m_JXNHk0u3AtXzw1GcKhy54w7lLcU9ofBX2h1moHIX1Zeg9NI2qTtY9WZ6wa239e6GbqTY1ug5EvwIVCr8s7ePFR0cM12-iksz7jumKv9f-l0-Op927GEWaklFBSshOcWg2nCjKWv85qlWzHef4m11zlDOv8uOzX4vwsXsa9jyu0H0S-7kBde5cQJd3OpzlmUy4gzhrvLn5U9VR6Vd4eTVRB4gmweZmbCIYBoGq0qTZDatA2GHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
▶️
این وسط یهو یاد برد ۳بر۰ پرسپولیس جلوی نسف قارشی ازبکستان افتادم، جهنم آزادی، پرسپولیس مخوف و گادوین منشا ‌بی‌رحم
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139161" target="_blank">📅 15:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139160" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139159" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtrODtlCwTCDahmjK4nCMP09YnVOidvmMRb3Z9OGhzJhDy4q4OA9ivxfLswKuRsW528r0l3WWmxUjkXbNdmxOx3nXtP-1Bj3ejKdRcAaGCJD9H2zhik9yso9E6cjMIdx53LaobUeYGfZl5aUgQW_dJ6DugzqNo7v7y8ZQ7qSO93hwaatZ7Mh305keTaRCKWTodLo3G_r0UtXWQdlGV1jLP0y2Bwuphq_DUD7UpXtQXyn9Cw2m5aRpY9XSdAg5_ovjViSyfgLJI2aIcHXTevHaaYk6PljGsr7d6nnUhtaqcDFK22en-4vEM-Qambuty96B9nVYwayQ0sL8YaWy16f6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جریمه 50 میلیون تومانی باشگاه پرسپولیس بدلیل توهین علیه مقام رسمی مسابقه توسط تماشاگران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/139158" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139157">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=M585R_kNjx6OUtd-LWaRMXfLz8oPtHzMA7IWD2QBohVO0FlVIKn60hvTNleo8SAKtNUZ2FA8RZJ0hITVSDXJjyuQkKFFyz4YaOlePFUWO7nEe_vhfmiSZ4J0F4KG15z37uCMPggbVzeVwZpNm-1DuQ8l0BUuiE8IZsGyIkbS5gNDsT3N6PgRzrA_HVyD2hX9r3B3UBsCbxvKFlmfUvPdIhWw74rrhuYxCqAnwK_Tju183-uIh69peMU5HKQ_XWFvAQYaxyqlTyohwicLbhKGPG05uVcI5pJuDBiodEruiMQcrCBNAJsoZJJjsM72wF6hM_zQtZi8n3CMfH_hpsDuZYsTIJDFZPwUkSkQ6uRWjHNxfv2D_a48KVPWKTMTZYSDrjgruYYJ4EKntB4PUd7Hf45ywjhyHUF8jlIQAVnFzmfdnShC7waLPAqZOYvLKAwY0-O5Tief3GuDcAPjS5GALHVraYm7F2ckP_t_jClryT88UE8KIDm-SDcK6lpS5B9BGJQsXo6rJ7IhpjqLFUD8BNNveiRioTzA4o0K31mW9BZRoA2-EEZGv3A_nkjRqh-W-1w_LxAgE5PkiX_SeRAfZSzw5z95vFgUtDpwxIcK5s9N-xa9-oJBSyb2yaSbxWri8sqY9CeLcJk9p5vF70rBppDe8IN7PizJF_w6VFoc3CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=M585R_kNjx6OUtd-LWaRMXfLz8oPtHzMA7IWD2QBohVO0FlVIKn60hvTNleo8SAKtNUZ2FA8RZJ0hITVSDXJjyuQkKFFyz4YaOlePFUWO7nEe_vhfmiSZ4J0F4KG15z37uCMPggbVzeVwZpNm-1DuQ8l0BUuiE8IZsGyIkbS5gNDsT3N6PgRzrA_HVyD2hX9r3B3UBsCbxvKFlmfUvPdIhWw74rrhuYxCqAnwK_Tju183-uIh69peMU5HKQ_XWFvAQYaxyqlTyohwicLbhKGPG05uVcI5pJuDBiodEruiMQcrCBNAJsoZJJjsM72wF6hM_zQtZi8n3CMfH_hpsDuZYsTIJDFZPwUkSkQ6uRWjHNxfv2D_a48KVPWKTMTZYSDrjgruYYJ4EKntB4PUd7Hf45ywjhyHUF8jlIQAVnFzmfdnShC7waLPAqZOYvLKAwY0-O5Tief3GuDcAPjS5GALHVraYm7F2ckP_t_jClryT88UE8KIDm-SDcK6lpS5B9BGJQsXo6rJ7IhpjqLFUD8BNNveiRioTzA4o0K31mW9BZRoA2-EEZGv3A_nkjRqh-W-1w_LxAgE5PkiX_SeRAfZSzw5z95vFgUtDpwxIcK5s9N-xa9-oJBSyb2yaSbxWri8sqY9CeLcJk9p5vF70rBppDe8IN7PizJF_w6VFoc3CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139157" target="_blank">📅 15:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139150">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JlImzIaHVpAkVkwHcOPMtYBXbuceH4x6I2DssJLK0zzWrEhSuSuDhGd-SAfQfDEgpHmIjlRGRVXePBq0aCJlyy2Vbcuusy07YqgPK7-XgVd6QuXW99QvOqmOafdL8YnwFyhzflNqscUxCSEpcjb98NSd8VfHHVTkfIcFatGfd1P1VRdQjvAAFMb0Jx6o5dk40FrfPUYQDds8KUf6GqeI_GRfoZngQEAGEG-fOwCcV-x0_vbI_gZzJdUWgD4TqVS2Kpc13gEFx2hsCS1lN_f-bRVCIJ3zlX0pNNZPaf9HpEHteEmfPgr2t0ftuIhsRAyXuN4FV3TFt2hOe_cOXvr-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JyITaVm1-Jh3xRKXRrwj1Z_Q7CjZ0VqyVWDDhadak3Y3jCfdF3lypcckdaCnjsDtRP7PdeC0l6qUqmVGvaRpOYmnT6ApSFpyNpqVNZCtQGRadiL6_WbNYA_m9Hmg2HNWT7JpbuFYPt2b-Ygt-RlU8Ote7T14gguuHjy7wD_79lbSxqQ0xIyOdu6B0iHs-dCCqPCPocEDWtdUjcBg8dqqnhTJ3N_vNqcM7mzExUzpmgyCEsabdhJqvCs-lC0oJVuqt5VlCBdk4AjqrNsAsA9FkEWf_xeoTCh8FMp46EQcVnsAxIWKO08GjPi4MgSdh8oKHr0UjHqi1YrgQKKatgnLwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h1xfYqpASxQVCeFHp3l5lpROIoppUxCEeZ13iDcUKeY2x7360hfG3aNBDxO6NTJL5nAGpnqMqOLt_bN2c3nuF-ulvih337KaUYl51zCL96bNvoEpy4HzTHqNDYFwgIJFePXNrbfCuzUxYNTNDF3S32r-CFxneF2IZigBsqcnbji0TTFNMJXWDEHtaYNI7GhibXBvcivbu7xkJTpJyzRdcscOviCaXK5PCtefxD9KZ30LPXrcgcQF7eo4YaDVefIyeNLP9M7T3fbQ1fQfonyDYVflU5ffgmrMOpg4m_fEtEVzDgaGO4ehpQaSF1iP2AkVWd-2Tf_2LvXYvkfZpavJsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTYtQ-pCvLbEHwSrQKtR5Mfs5yun1vD0QSDKncfcJr_OAzvhdpRT78u851_rT8Bfs_XROCU1acw19t92KS78_YUSgb6MWoCG-WnxiUR1zqWokk1DXo0whiFawsuGdEQq6GdBbQHPmjV9mvB_WZT9z0u2K_hKN8fYGgWlTBFiIRkmKmuXmnTUasWTyikWuNWsESnC6eEmC4W6eIfXfP5OZfuVPqkQFZ05Inj5IXh-qzNPAQ5Mkg9OoiabyNKJZsMBXNM6WL3m_P-0bgorjgCNq4BiG4IkZQTwgaRVBDD8tyeY3CIfkfX6OKK7i8iTPSAdNfi8er659TxA7nkdV6DOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbFj7cKmhOt-o4mAXPzDQCnoVL2G8cdGcM802cSHi2CIId_4kTUH4-UKaQxnme9X1b9j8hJaNylfecS-JvT_Zm1YUY6iFwZzT7rd-KNiT4jdrVvcW4vq-9nP-GaHh7zKpuyy58VsGQlTp7go6f9oYTZVjdMLQl1cXVC2-2REOh-sNHE_as9whCY9jDloKFlPPVqxNhQ0Z6TGYwDYgJt5LqVQPStFDOLLbDusoN9kIbkqGHCxn7iqJyoGaZAfKYaKZcVC0rywQ_r78-ehUAhxngDFrOEE1OTJP_R26WlObaUHqfmNe500VN9BJt3T7rtPJF-UvYWwAE0OcVD9xTv4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M1-ynPec2SdpdIZ8S1XxnZKm9DOCkmiJp2dqZD3oNbFrX5R_eFwFjmtybn-dK9iQmmTLZzBntwXV6I13WkZDDtpuNN9jGpABZljMrk2UuLSVxZiS6ndA21_5Dq-zKtwjiCUKfo58heSSZmwelH2MOwQLQNyIJZym4q4gHBWpquwDx3lZ-fo0ZNd6a6EVYIvHqe7mGX9qI3QWGDPUz9-Oa-MiFVMGUUIHoK-mm6fpy0fCgJjRnrDDPIQ-MmClpkHPFCnMvEYCwX39Ms7wBQls3CHoHvAnkjfo--jf-uZkw26qjPjeSCVWVRRlELoeEgyCC7yzsO2Mw-Vw053pCHsb2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGkIl_atcDxObgb4MvxBbGbsg2z4k9X9a54ijjpNhUtmTPQoLERUSJzKc1AoxtQd0S_ZLhpiC_cP2Lfzvpl0X-AtAFWNwBY_eQy29cgtk5z2t3G5VOjUQvh3EF5RNYnCtTP4LrQZfRd7hjuYbPT_b1QMx_BrQMJdjcdTCvyY1tzTahbccYpeoMHDM5magidduDv7QQxOts0L3swogbJt26Vu72mLaxxWA6JjLldpekvDJUirm0Y2My6HKZCEG8p4m7UPVnKEHOkcSQEoLTW1GDjsvBZrPw-gaZVmI9TJ_xhcuz_p9RyemTubfK3uVAufGizntsmAD-zHLXTbF8AQ5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭕️
⛔️
حواشی نا تمام هوادار متمول؛گادفادر متوهم ول کن نیست
‼️
🔽
رشته استوری هارا بخوانید…رامین پوکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139150" target="_blank">📅 15:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q35lPDLVuw1rJJFda4q2mjgbLyTvV6w-hKdRAT7MxRRGa6zUXiyJm9zJ_xvOV_1AgGFsCO0qbslNdnsmGeAS3LbRItXGPpLVwzelIO2fREAlr0CJpKhfwq0scVqw-uNCeb64T-2-kcwvikjWfGrM9TYGfHDtJOu96nlj7qdCor6ngBnWYup_Ajk8dptAhFOsP3P_qpbeynmeCpxgo_WokN96HuoZGqPZKCiXJhS5hEiQnWN09Oleni6kvCpoJJZ5iLOJMVcWpRdq6PkqDiHNWmmQ-l5yGeMjaUOlKBHYqKbkXyx0TD0MhvCjqJRB1BiJHJoBd-09324UKDUNwdC1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پایتخت آماده یک شب داغ!
🔥
پرسپولیس دنبال شکار ملوان؛ قویِ انزلی برای غافلگیری به‌میدان میاد!
امشب نوبت کدوم تیمه که حرف آخر رو بزنه؟
[
پرسپولیس
⚽
🆚
⚽
ملوان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139149" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
