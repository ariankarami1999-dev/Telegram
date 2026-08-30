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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 12:13:41</div>
<hr>

<div class="tg-post" id="msg-139244">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrunHVUHnhkNF2NMzNVqVqEXA-FpW0nOCwfTk4NGzGd9uG8mouXdrqzTBCFDxICvTVvPBGCk1n1pud57o73Ikc52XLLdruvPLtaSu5wTw7j_aeFxCMWCfDuQ5H68f8Ly5Aj6r4OqSH_KfNFHbOmfjMFUsH9_31JTQfe4TGil2x0Dh2hrKpSlzRh1RyJBZYPzBQigc6zxjhSycpyq9HxX10af0__9aH2kIrXUi4o1Pjl0kgPsmnp60V7AQwLhdV5RLeetZ43Cxo4R1lXKIC0JRwr63uuRPZNjaPREzISLQEXhTDvdz2sCn9rDvhaz22bCi4u4yXfouf8sfz_pZF1GQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی علیپور با نمره 8.45 بهترین بازیکن بازی پرسپولیس و ملوان شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/SorkhTimes/139244" target="_blank">📅 11:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139243">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🗣
🗣
با تلاش کادر پزشکی تراکتور؛ مهدی ترابی به دیدار با پرسپولیس رسید و از روی نیمکت بازی را آغاز خواهد کرد. هاشم‌نژاد غایب است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/SorkhTimes/139243" target="_blank">📅 11:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139242">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/SorkhTimes/139242" target="_blank">📅 10:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139241">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/SorkhTimes/139241" target="_blank">📅 10:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139240">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1Vk-3CAFNv9tqIquyuN03L2zLT9m8UQDVITwnHQ9g9rh8dbWos15f8HSobDgWp2EyNN78eEYgHE0x2L3V9W5VNwKT84LTplm_Fr_n1Yx5YXWmPBdDTGdMTWLROCP2bVsGu2RAQ-vokrNnpmfUOqHuYEJZRrcBvWpKm3YTC0Os8ZgYuna_SsgBovgu1ky-nb3rzKN1VptPB1dBDSB6wr9jtMVvl9JUDU9eHkS6KBSC-Nktd8sHI77rcVVVr6lX55hJg8VuNF9FHycOEeSUN58kP592ohF1VlE5S0ownJcTM0dIDXbbwr50uvZOI18MQzx5dTMdw2k5kbW7sRw_N3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📸
صادقیان دیشب تو ورزشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SorkhTimes/139240" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139239">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✔️
✔️
اردوی پرسپولیس برای دربی بعد از بازی با ملوان آغاز شد و بازیکنا به هتل المپیک رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/139239" target="_blank">📅 10:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139238">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/139238" target="_blank">📅 09:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139237">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
✔️
‌ تیکی‌تاکای تارتار؛ ۱۸ پاس و گُلی که نشد
❌
پرسپولیس با ۱۸ پاس متوالی روی زمین یکی از زیباترین حملاتش را ساخت و تا آستانه یک گل تماشایی پیش رفت، اما ضربه سر ایگور سرگیف از بالای دروازه بیرون رفت؛ با ورود اورونوف، سمت چپ سرخ‌ها هم فعال‌تر شد و ترکیب‌های…</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/SorkhTimes/139237" target="_blank">📅 09:04 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">✔️
✔️
پرسپولیس با 9 گل زده تا هفته چهارم بهترین خط حمله لیگ داشته و امشب با ثبت امید گل 4 بالاترین امید گل رو 4 هفته ابتدایی ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/139236" target="_blank">📅 09:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✅
صبحی که تیم محبوبمون توی ی بازی جذاب و دیدنی بازی و برده بخیر.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/139235" target="_blank">📅 08:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139234">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/139234" target="_blank">📅 01:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139233">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139233" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139232">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139232" target="_blank">📅 00:23 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139231">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
دانیال ایری امشب به عنوان بازیکن ذخیره وارد زمین خواهد شد تا اتفاقات دیدار با تراکتور را فراموش کند.
✍️
ورزش‌سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139231" target="_blank">📅 00:20 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139230">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❌
حسین کنعانی ، دانیال ایری ، مجید عیدی ، پویا پورعلی و محمد عمری پنج بازیکن تیم پرسپولیس که سابقه پوشیدن پیراهن تیم ملوان دارن
✔️
فرزین معامله‌گری هم که برای سربازی منتقل شده به ملوان تنها بازیکنی که سابقه پوشیدن لباس پرسپولیس داره
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139230" target="_blank">📅 00:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139229">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139229" target="_blank">📅 00:10 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139228">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrnBKoE40XQDXXJfQUI_qO3LZRza4EWzFovzk0W_o5E1BtQY9K_jMQNH2PP8aKimPU8WPt1ONKYq-Ib3i1w0SL7I5NSRO5_FcNAD-ESNzIGWEVP1sh5CtCWtBeiJQ083-Oer5plqrkeETdNKcNhF1JXsoSnKMQiWbQVtIxkHfyjYiW1RIBLXdlEQp8V-gk1ukgYnESCIWub-C25TSWo3V0RgZKKMMqy_UHxuiXgZSYUbTtGsfXdQEBHkm-QxUs5qSzaf2Pj7UlSJRWj3p2D5FrubPTvlQVusZw0KYhf98eE7GuuMx8l2hVSNQtd0yRciL6urmk5xR7Xs3UTAwn3DRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139228" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139227">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
مهدی تیکدری: بعد بازی قبل همقسم شدیم که این بازی رو ببریم/بزرگترای تیم خیلی بهمون کمک کردن/روی یه اتفاق به تراکتور باختیم/هجمه‌ها بعد از باخت طبیعیه/ترافیک در خط حمله زیاده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139227" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139226">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
کریم باقری: پرسپولیس از هر بازیکنی بزرگتره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139226" target="_blank">📅 00:07 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139225">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
کریم باقری: نگران نباشید. پرسپولیس بهتر میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139225" target="_blank">📅 00:05 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139224">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/139224" target="_blank">📅 00:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139223">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139223" target="_blank">📅 23:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139222">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
🔴
علیپور با ۲۵۷ بازی، از سید جلال حسینی با ۲۵۶ بازی عبور کرد و به رتبه دوم بیشترین تعداد دیدار رسمی با پیراهن پرسپولیس رسید.
🔴
علیپور در ۲۵۷ بازی خود با پیراهن پرسپولیس، ۹۰ گل زده و ۳۸ پاس گل ارسال کرده است. او با ۹۰ گل و پس از پیوس و پروین، سومین گلزن برتر…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139222" target="_blank">📅 23:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139221">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">✔️
خلیلی: امروز فقط بهای جوانگرایی را دادیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139221" target="_blank">📅 23:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139220">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7NFMb68WZAoxNv--p8ngFLovy81lbbPYxw2KpMrtFVUCFaQBtrTyANtJD03seSE5KzKLpU6dPM8dq5pmK478MZfYAXeCDOzDaDvyKDH_bG21Foh_Zj86jFkjyGZj_X4k1R-SbvdX6tPryazH_be7bWFMSwhbNOYgA8CQRctyoACkV6W5Y_gF5p4XPXAp-s78ejCd2K_x7xR4cFjzjPsMJAc9h6la2RICf-2y-U5Ix0ZOdGph3O2Ap-soM6ISVfddS6QUeL0S9SmMDdoAW4BZB0cSd53ZCnPXTHZPHGcnVtg-YQSc2tPG3w91fakFnOq02DFHReY4D5njzumUmBXPA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139220" target="_blank">📅 22:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139219">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/139219" target="_blank">📅 22:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139218">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139218" target="_blank">📅 22:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139217">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
باقری: کادرفنی زمان می‌خواهد که میان بازیکنان هماهنگی ایجاد کند
❌
تیم پرسپولیس به نفرات توجه نمی‌کند، همه بازیکنان جمع شدند زیر سقف پرسپولیس
❌
تماشاگران پرسپولیس را تشویق کنند، نفر را تشویق نکنند!
❌
اورونوف دیر به تمرینات اضافه شده و کادرفنی تلاش می‌کند…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/139217" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139216">
<div class="tg-post-header">📌 پیام #72</div>
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
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/139216" target="_blank">📅 22:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139215">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139215" target="_blank">📅 22:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139214">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCs1ssIQYfMrAaw42oIEXTyexYDzaF7BgsmuwOBdkVpdSYnmHxDzto_bT_PkPRKrizAxj5I-t0gs5HDkgZxxkJNukRXFsHJDSzXASd6x24Lpfw7h4wuvv8IoiX9O0dsVAX5ZFvjiBPfi_SmDekr1nJVPiLp9FRYoJxnocMpKdKRP2IN6MiyNNV9OAEY2IDkWzeRca4NOx7I_O2CR8gtY8oq9iYn3NWLxAOt_PkfJuSIhaxDiXSMKWv4I8qQRVFEeV7sD19lQjYMg3y_eTbmo36k8g6tPKGmsfl1UkA2vGwQnj1-KfC2lNvlhOSCptzawlPnY3KJlRJ0xAzVtkGubUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
پیمان حدادی بار دیگر این استوری رو گذاشت/ حسبی الله : خدا برایم کافیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139214" target="_blank">📅 22:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139213">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
مهدی تارتار به دلیل افت فشار در نشست خبری بعد از بازی شرکت نکرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/139213" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139212">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
گفته می‌شود فردا نیز مهدی تارتار برای دفاع چپ پرسپولیس از علیرضا همائی‌فر استفاده نخواهد کرد و مهدی تیکدری در پست غیر تخصصی بازی خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/139212" target="_blank">📅 22:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139211">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/139211" target="_blank">📅 22:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139210">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=hjAcmVQSRhjUChNsuepmt7zYpJj0M9wMJb2U8_9gzo2_IPyF0D6LK6LTamgdpC_sSlTERWtOSP9R7Vc-E3jiY2kw-7K3YJx9drT4MoEL8ldR6Ni_KsW0JFd3KzWlgjL9fjSmBJ5C5Z8Q3-YlMwU0EloCLQur7hC8kGlWdO7KcDEw6m_-n6CXeUUnGUEiKhM-EODx0ImNC1r2Vc-LT7JOkED-BWibJUnPSDvdD0gdvhUQirLZQ9uV5BrE-kcZ_i-Exwq6tBc-SlYcPGtZY9M3dwCYcbFijBWIyjH_MnnaF1fNKUYGGWlRdg2k9jvdwSBp0_cNG4cGinbq9yqeKfBR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=hjAcmVQSRhjUChNsuepmt7zYpJj0M9wMJb2U8_9gzo2_IPyF0D6LK6LTamgdpC_sSlTERWtOSP9R7Vc-E3jiY2kw-7K3YJx9drT4MoEL8ldR6Ni_KsW0JFd3KzWlgjL9fjSmBJ5C5Z8Q3-YlMwU0EloCLQur7hC8kGlWdO7KcDEw6m_-n6CXeUUnGUEiKhM-EODx0ImNC1r2Vc-LT7JOkED-BWibJUnPSDvdD0gdvhUQirLZQ9uV5BrE-kcZ_i-Exwq6tBc-SlYcPGtZY9M3dwCYcbFijBWIyjH_MnnaF1fNKUYGGWlRdg2k9jvdwSBp0_cNG4cGinbq9yqeKfBR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
کنایه مازیار زارع به برنامه فوتبال برتر: دوست ندارم تصویر من را در برنامه تان پخش کنید. شما اینجا باشید من مصاحبه نمی کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139210" target="_blank">📅 22:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139209">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=q7eRFlbbAoWX9JeodHcDbDDI3W1UkqjXhDwz0IRtn7IItBodIV-MGBjQ1tRx7-VXYYls4PrvMqqD57GMOx4CLz0VHg8lsz-asHROfD9m_YgV8j3d7u0MxEQE4bErx5wSSGFS3CZjk3u9IbHFfIUc8njguAXT6n1AVDPbzvzhyjXAKMghfdF9z3ALgTkXfV1mpXdnOOfz6IqeSrqehC8pSQy8WpRrDSqpvwfpkwjmJ28utF8QTPhIktoaSZGg1_Vabe3lH-v9HZVidl6_65cBE0tyiRVSw1PUs6Xt8fGtgMXG-KUTMbxZNdlGIGtTb8o-xw4M--Zz4WjZ5xHJPM3AXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e73d84229.mp4?token=q7eRFlbbAoWX9JeodHcDbDDI3W1UkqjXhDwz0IRtn7IItBodIV-MGBjQ1tRx7-VXYYls4PrvMqqD57GMOx4CLz0VHg8lsz-asHROfD9m_YgV8j3d7u0MxEQE4bErx5wSSGFS3CZjk3u9IbHFfIUc8njguAXT6n1AVDPbzvzhyjXAKMghfdF9z3ALgTkXfV1mpXdnOOfz6IqeSrqehC8pSQy8WpRrDSqpvwfpkwjmJ28utF8QTPhIktoaSZGg1_Vabe3lH-v9HZVidl6_65cBE0tyiRVSw1PUs6Xt8fGtgMXG-KUTMbxZNdlGIGtTb8o-xw4M--Zz4WjZ5xHJPM3AXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139209" target="_blank">📅 21:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139208">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBRf5UdtjyaEZ1T2J9t_QTDt7r6qBrrEdgbCk0falRL8pfUVuTxqF28bgqMTahP_27bOU0n1TQloU-mUJEF_czhrWJe5mkQQ9ym0fkB2BrbQny9PF7bZb51naBnhAmUs0FtJY7sOE28k9gorZecZlYZ5Kaue_6CdZBRW1syyiwA2wSpchpvzL5mmo60J8MJBUlrEOwJ7YPYNU1PtoJZ4z9KASFuA5vYG6CE0QL1LC4fkB18PUAYGEzYqavMhPZCSfTBOaBYTOPHWQv1yB5RhCIkAU6EkMAqxxS0Vbtu3JQAUOHtcFFtjNEO8XW_QG2OEupi4Y7cEPnoTC2zjFsRdqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
هوادار همین سبکو میخواد آقا تارتار تیمی بدون ترس و سراسر هجومی تیمی که می‌تونست امشب خیلی راحت بالا 5 تا هم گل بزنه
⏺
خداشکر با روحیه بالا سراغ دربی رفتیم و امیدوارم تو دربی هم همینطور و همین سبک رو ارائه بدیم
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚨
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/139208" target="_blank">📅 21:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139207">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Yxbdjixcr49N4gA3v1n0bOeGVjhYMDthrzVqo0L8FrfHiHTwJ_8UTsSX-8n8v9AEr_o2ntWnQsd6lcoh3o8ydOemF6gSZPIwoGs5_8kwD6n40aPGTrS8h0uC3KldLe54vxCk71q_w0rRsaxZI5p87kJ_wlYCJUCCvbeL_A3DAYwZQzhcwCoYhli6HtlhWVKqNbLLAHKlkxh22qx6fkZ4AEdpdsQBkGRyD9jiEvgdQOSM5BYOHIhMQWpEmrxgn_RFmYwXybYUN7s0SSAIvrJpjlndwJUxRBz6v_ZlFjMjz3L_B4d3khSFnAAS5-lonedDuvd5KOHgFHNt3ibwIWgB33s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a052a7430c.mp4?token=MTX7P1x-z0QxMQNjyCenJJDgAder_epD8xXaMO9iJUHqdu668g-qWqbeBh8aypqGVMytABayqgvO8LbeTmsg4V-qMI1HzrJFzYV4XgakyHdBzuTWP2mtG4n9u4N7cobKpABBewA1XI0jZc4pfnzEZu-8G69hh8nQY7OT2UYuc7EoE4cjVquehjMW8QcWH0me4fv0i4VeZLFbmdzbbz3w5KuYOfD_mRr-W9iEYsHTWg4t4AFn2DUp6xhO9y6hE4gV9nGN3f1lehxXSrYbeXFtYtnUDcqIoLmb9dynErNeLI4u-FnGVf8IDKqo0ex6Zup0v8ReUK0oA35CIHVhnN83Yxbdjixcr49N4gA3v1n0bOeGVjhYMDthrzVqo0L8FrfHiHTwJ_8UTsSX-8n8v9AEr_o2ntWnQsd6lcoh3o8ydOemF6gSZPIwoGs5_8kwD6n40aPGTrS8h0uC3KldLe54vxCk71q_w0rRsaxZI5p87kJ_wlYCJUCCvbeL_A3DAYwZQzhcwCoYhli6HtlhWVKqNbLLAHKlkxh22qx6fkZ4AEdpdsQBkGRyD9jiEvgdQOSM5BYOHIhMQWpEmrxgn_RFmYwXybYUN7s0SSAIvrJpjlndwJUxRBz6v_ZlFjMjz3L_B4d3khSFnAAS5-lonedDuvd5KOHgFHNt3ibwIWgB33s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
دانیال ایری، بازیکن جوان پرسپولیس به سمت هواداران ملوان رفت و به هواداران تیم سابقش ادای احترام کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139207" target="_blank">📅 21:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139206">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKEC3EirWSVN0tqvCPY9f3mHrEljrzcFCTn4Wey_IFeML78ovQiIczAjlEiLh65EemxtfggQZe9EFZFrS2lg7E7520u7d8_mR2M0K3slL58tHP8O0LwFYJL2taiDt4GEBCPitCX-w_thtfrFzvSsXbjp8bq830XskYGmBgCQekO7NoPOS1BBJcPHf3LZNV0vDalo-e9nz1hJ3OB8Ki2SA7c8wsfUJpVFkM70uLUJSU58CY0--P2g7jOwvjzB6oSrnwUaEH6TAEOlSxPaSgHOmzMcIOI5NT3PZE32HmjqYv_y_segp3YWTch_1PsoAi70NKkc4AtVmMwejcTb0rabEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
جدول رده‌بندی لیگ برتر پس از پایان هفته چهارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/139206" target="_blank">📅 21:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139205">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=q4pRapYc3Ayb0ZlEvWd-KvhOEPxbh29W0ClenPU7B3q-NY_OkIO1MxoGtFMeE14xm_eSVeGl-rVrAGpLz9OXlpr3IEKliQafnzFN4TB8eXrd9qOqGW0ZHYbER1JfHNutDIR68TGqGOe7gg5Wx5P5Hy4dh5ORBv9x4t3y493fSFXanMCMS93nE-XKnwIpaHrKCSe0M2dQT8XNXc2VLdQVZ-_LoAzt5w8F5YN1fDsktAaKjycohu9l5EvU2X_ebqZjxO78ABLzLO3dhxiUP3z4Y9WMTNYIE6RPLV4hm-0xf13sAzXk-g8SeKKuWb41uet2E0p0G4gU5eghg-2yIhMxLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37d6965b1.mp4?token=q4pRapYc3Ayb0ZlEvWd-KvhOEPxbh29W0ClenPU7B3q-NY_OkIO1MxoGtFMeE14xm_eSVeGl-rVrAGpLz9OXlpr3IEKliQafnzFN4TB8eXrd9qOqGW0ZHYbER1JfHNutDIR68TGqGOe7gg5Wx5P5Hy4dh5ORBv9x4t3y493fSFXanMCMS93nE-XKnwIpaHrKCSe0M2dQT8XNXc2VLdQVZ-_LoAzt5w8F5YN1fDsktAaKjycohu9l5EvU2X_ebqZjxO78ABLzLO3dhxiUP3z4Y9WMTNYIE6RPLV4hm-0xf13sAzXk-g8SeKKuWb41uet2E0p0G4gU5eghg-2yIhMxLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تشکر اعضای پرسپولیس از هواداران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/139205" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139204">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
🔴
💢
خلاصه بازی پرسپولیس ۳ - ملوان ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/139204" target="_blank">📅 21:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139203">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
به به چه فوتبالی .چه پرسپولیسی ...سه گل زدیم و شش گل نزدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/139203" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139202">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
تیم  دقیقه 98 هنوز تو حمله اس و تک به تک نمیزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/139202" target="_blank">📅 21:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139201">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
تیم سه گل زده هنوز سرتاسر حمله و تشنه گلزنیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139201" target="_blank">📅 21:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139200">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
اورونوف هم تا اومد تو زمین ی پاس سکسی داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/139200" target="_blank">📅 20:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139199">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
✅
بازیکن ملوان اومد تو زمین سلام کرد و بلافاصله اخراج شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/139199" target="_blank">📅 20:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139198">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚽
🤩
سیو تماشایی پیام نیازمند…
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/139198" target="_blank">📅 20:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139196">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6343db8016.mp4?token=ZUivyJwPMOC5S8p0fAfpcpY3GRJyU8-BHV_C8OdW-gXPRmVIEik2A1KN4bCdIzHukIHd6YMrV7x7Urp9Nj3wzoNxq4kHcudBcGPVwKh-xRz4laV9YFKDJwepsJcefjwYnbp1t3IelIo3AskNg8xI0r7ZNQ9OJEBGlRemHdItTMsF9VK1C0xTrj440Nos0WlbQN_EEoLBSeEW1ula0YcSNynVwTRMMR-7i5BnvTlId3ymrsyK1nhvt0bY769uGBnT0DvMzuPIU3dFAGP4amqzrJDy1grGz6MGxGOMeSet3Qo4MU2e-pci9XeZ53bHkuGZfO49DPKexnd35I_dUQMruA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6343db8016.mp4?token=ZUivyJwPMOC5S8p0fAfpcpY3GRJyU8-BHV_C8OdW-gXPRmVIEik2A1KN4bCdIzHukIHd6YMrV7x7Urp9Nj3wzoNxq4kHcudBcGPVwKh-xRz4laV9YFKDJwepsJcefjwYnbp1t3IelIo3AskNg8xI0r7ZNQ9OJEBGlRemHdItTMsF9VK1C0xTrj440Nos0WlbQN_EEoLBSeEW1ula0YcSNynVwTRMMR-7i5BnvTlId3ymrsyK1nhvt0bY769uGBnT0DvMzuPIU3dFAGP4amqzrJDy1grGz6MGxGOMeSet3Qo4MU2e-pci9XeZ53bHkuGZfO49DPKexnd35I_dUQMruA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139196" target="_blank">📅 20:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139194">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=LdP0rNn28EDfmViuSWYQ4qLoXAHWKUbQU1L4jdNTv45g4-ly9hv1sUPS_Qoe63oGIuxkwCMF86KswGAs2Cs-qlY91zgcRyBxng7gl3eoMGC7axg2A99SDiyL7ydUlXlQW4l2H_N32BLEXGiiDSe4qYLaa-MCEDNs0TZqWOvvSJQjK6CyF5qXU6NdVm4lojzPSMukWZDUtNURFHU6WyS29zEueQUW1iTcFrri-pz6YKUI56dB88w0B7ssVDMdK86hzAX_Kx-vBbVoDlP7UcusBkGiR0tViFGx8jid5QQHXX87ofwUKI-ySEXFeTt7jv-qOyoUbqjvx4E2db4UqL3bXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df197fe84.mp4?token=LdP0rNn28EDfmViuSWYQ4qLoXAHWKUbQU1L4jdNTv45g4-ly9hv1sUPS_Qoe63oGIuxkwCMF86KswGAs2Cs-qlY91zgcRyBxng7gl3eoMGC7axg2A99SDiyL7ydUlXlQW4l2H_N32BLEXGiiDSe4qYLaa-MCEDNs0TZqWOvvSJQjK6CyF5qXU6NdVm4lojzPSMukWZDUtNURFHU6WyS29zEueQUW1iTcFrri-pz6YKUI56dB88w0B7ssVDMdK86hzAX_Kx-vBbVoDlP7UcusBkGiR0tViFGx8jid5QQHXX87ofwUKI-ySEXFeTt7jv-qOyoUbqjvx4E2db4UqL3bXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
🤩
گل سوم پرسپولیس توسط علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139194" target="_blank">📅 20:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139193">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139193" target="_blank">📅 20:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139192">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❌
❌
بریم برای نیمه دوم ...بریم برای زدن گل های بیشتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139192" target="_blank">📅 20:35 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139191">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=kPH8PdmlwB9oBf5Jipsw5ObmSaOKHRA_5Jqe7HsQq8FU8B-QTvxcqei7KyaFpGp6Gvt3uD4sN65vRL3u1q9lksI466Nv33GsV1u6KegNVEIKBCTm1E9UzZlho1QLCwz9e3Rg5I_ydVrHiVERIHwa5JEZTBdB2X6SXIsmGovX4dyP8OtuXSp7OIS1ug6ExuzCvCJOVgloQazPNNwhZ0pSGOaa6g7MweVPlqEMu1pPEFd2YREgYqFY_Qf9qMQUGe26t_Dm5gsUd6M9p6K2ShGbv9SszJXrcJDqB4MTr-BKqwQSm3OfvFlhakeLl8r41bXzYAO7JFUO18wjTq6vjp-PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9742c8c7.mp4?token=kPH8PdmlwB9oBf5Jipsw5ObmSaOKHRA_5Jqe7HsQq8FU8B-QTvxcqei7KyaFpGp6Gvt3uD4sN65vRL3u1q9lksI466Nv33GsV1u6KegNVEIKBCTm1E9UzZlho1QLCwz9e3Rg5I_ydVrHiVERIHwa5JEZTBdB2X6SXIsmGovX4dyP8OtuXSp7OIS1ug6ExuzCvCJOVgloQazPNNwhZ0pSGOaa6g7MweVPlqEMu1pPEFd2YREgYqFY_Qf9qMQUGe26t_Dm5gsUd6M9p6K2ShGbv9SszJXrcJDqB4MTr-BKqwQSm3OfvFlhakeLl8r41bXzYAO7JFUO18wjTq6vjp-PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
علی علیپور موقعیت خوب پرسپولیس رو به بیرون زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/139191" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139190">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139190" target="_blank">📅 20:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139189">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adad84121.mp4?token=sBl7XSivG3V5Gdia5FsiMrtgnlI7AbYQspm4coUIu08jgx084PBQMVMhaQvlupUPXoaufGZPxti4N0I-NCm6WdcKBFqW57k-NgQ8jb09KXzHCFmBO52iHfv5cm1LldJSr0RBEWpU7T7-OY8hMREVCipPtqKojYPEaxk0RIpTy9pncWT4fUFSt0XQIk9fUxIyJz6sHe9HCmEjn1T41I6Ho-ww3fo5ZFmxoXObQWC8lXNiApLSI6wrtTC4pm-OQIEKPtq0RK1IlS-64w7O1eo6Dehgw8n_KB2Gch63BVV6_dlhEm1JQ7A5URi4cLxncIsc4J8F6EW4Es8lWarL2M4_gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adad84121.mp4?token=sBl7XSivG3V5Gdia5FsiMrtgnlI7AbYQspm4coUIu08jgx084PBQMVMhaQvlupUPXoaufGZPxti4N0I-NCm6WdcKBFqW57k-NgQ8jb09KXzHCFmBO52iHfv5cm1LldJSr0RBEWpU7T7-OY8hMREVCipPtqKojYPEaxk0RIpTy9pncWT4fUFSt0XQIk9fUxIyJz6sHe9HCmEjn1T41I6Ho-ww3fo5ZFmxoXObQWC8lXNiApLSI6wrtTC4pm-OQIEKPtq0RK1IlS-64w7O1eo6Dehgw8n_KB2Gch63BVV6_dlhEm1JQ7A5URi4cLxncIsc4J8F6EW4Es8lWarL2M4_gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
در بین دو نیمه اورونوف از سوی طرفداران پرسپولیس به شدت تشویق شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/139189" target="_blank">📅 20:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139187">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/139187" target="_blank">📅 20:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139186">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139186" target="_blank">📅 20:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139185">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139185" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139184">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=Q5G2bszyyLPQ2-ilFJ_tB2cVvJpU59LxddmC51yVfB4frV45D3-zR5pAqbuILXS4WAQOQNiJoTUsmskMcFza-E4lYXDZpa3ZLO3hvJhGXTHw-BTmh9ElhOqWT7jNrp_pcjHvVtGmnccySs0b5mhcLwLp8_zBueuWJwN3ER9IP1bu_0QWcjc1kG1v7PPVZjBtypET8ltR5eef-f1x9DRmobu6O60j1CM13UiA2iVyC_qhbZRN_PqFpdAweJup7AxZr7k-UrG-8xKU9gS9-tf4a0Q2QvsFFk6hUFB-5wusbhdIf5DX5NBjTqaFuGS9J2CiPGnrsyVw7wokQaq4NjrbJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b85faf30c.mp4?token=Q5G2bszyyLPQ2-ilFJ_tB2cVvJpU59LxddmC51yVfB4frV45D3-zR5pAqbuILXS4WAQOQNiJoTUsmskMcFza-E4lYXDZpa3ZLO3hvJhGXTHw-BTmh9ElhOqWT7jNrp_pcjHvVtGmnccySs0b5mhcLwLp8_zBueuWJwN3ER9IP1bu_0QWcjc1kG1v7PPVZjBtypET8ltR5eef-f1x9DRmobu6O60j1CM13UiA2iVyC_qhbZRN_PqFpdAweJup7AxZr7k-UrG-8xKU9gS9-tf4a0Q2QvsFFk6hUFB-5wusbhdIf5DX5NBjTqaFuGS9J2CiPGnrsyVw7wokQaq4NjrbJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
مهدی تارتار و کریم باقری از گل انفرادی بیفوما به وجد آمدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139184" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139183">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙖𝙢𝙞𝙧</strong></div>
<div class="tg-text">چرا باکیچ رو بازی نمیده حرومزاده کعیر تو گلگهر با بازیکناش</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/139183" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139182">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSana</strong></div>
<div class="tg-text">پورعلی کلا وله بخدا باکیچ توانایی جمع کردن وسط زمینو دارت</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SorkhTimes/139182" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139181">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSahand</strong></div>
<div class="tg-text">نظری ندارین که چرا از باکیچ بازی نمیگیره؟</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/139181" target="_blank">📅 20:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139180">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SorkhTimes/139180" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139179">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">📌
وسط وله…
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SorkhTimes/139179" target="_blank">📅 20:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139178">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/139178" target="_blank">📅 20:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139177">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpWTQ3ovJtuZxXgXINboH1Ls0VB7LnCgD5kVN9MSYdrWCxG2mvwTV6j8aPHXAi-EeJALznw9QhjBbtCSMNNWgYlpMmBp2zIRRTAGKj00rxtiYLoX8ndDjVpsNpnpri57bRDNAmt_zOFAku6QE-Ma6phuSswcgGv8pTMNOiPSwS4SW9PRf1O44qNoq4YLUtUtj-9MGJJia95ghVWG9vOyH9AVdXn30kgz1ibRXNaAwdvA4kkZdmimDHGVHN3vEks8j5VcN0Us00H3AI4SI8qqGtnZ-w9b-U7B-Fm_cFSqeytSC6BqWvkw8QWNckBMyp_4QAmBH9JcGtgMmla2egtssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
دیدی خوب بازی کنی نتیجشو میبینی؟
✔️
کاش جلو ترتر اینجوری بازی میکردی آقای تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/SorkhTimes/139177" target="_blank">📅 20:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139176">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ-9JY_SbrA5zagzU7MDFoLuR9NdaQMFHk7TyiIf8x83lWVRk8zfkFIqaUzJCn5cubHosoN0VSLUwHWfLJAENVN06AgHIEqFYVLzHOO4k5iGbDey7s2IgDm_3YvVGpG0Sal35tqyTCEQpIu48rr-MPUyBDIQ1CGKDXpLJKwofWPQuzg9nzt1jLLmIZCv4RvolisEyTKckkJqLEUBgfxQfSKsBQ5OKj9YZrmDbpKeGBD9oKqp7OFJ59sDbPO6tc5Wsm1yJP2mVe6ozR06NB8vDYOYL4_A4CIOvBtVItG2mttJFHSMIgbeR9lJa35oMZXOBCHM-thzOkDyDetCJTeWgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/139176" target="_blank">📅 20:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139175">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SorkhTimes/139175" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139174">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
خداییش دو تا زدیم سه تا نزدیم .عجب تیمی ..چه استارت هایی چه ضد حمله هایی ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/139174" target="_blank">📅 20:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139173">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/139173" target="_blank">📅 20:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139172">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=HpVkUYg0mjH2w_vOC7aOY2BmE9xqXWOL5C1PO8XwpvAjIFJ33XF_IDQRYK291WyAl-tWYyypgwR_jqDBh8R_XtfdjCh3j1KlJxqWgZFHczouWyvSx3qATrbSBwaCY2mhYNFU_R-7E6v0VKeoC7kuFVb9YBlqIITK2csA9OhhU0VfxHVRZgK6q0mOITDMswTRUbKrsawiByrpHADhgcNeqbtsiXVCbmKTAtEqGITSYNCntYL5PMkDDuw5SssX7Wf_kEYYf-cGRQXwaOwRaFeZ54zsIEtsqHN5x75yFTmaM0YmM5y4fiCvDKL9CSwEPclXKLpe3d5KctQ3B8-wM5cBrkxUPAR89LAkspnlRZYGlJOUGZHvvdeuhDbu8r0Q9cf1cl8EQn-R_DMxEsI8T0qWiF5YEQm8Rvb7i5-W9ZH64jjyaz7g7Qyl581avkf73CkatFHi6z67ZGYf8-jzV4zQDktrDIicnwd_YsBTPWp1TC1DD184jHKQKgCWyUne97GofPSUDdeulF0tIpQMIW9M_HAnJx_HNcw4TJzHmG7UAQQqWDtLROQMQLd35Uque2dMJUoO5Jkfw-hnUdIKbV2yGu-c9A5ZaLmjM23j4fFWeIRyc53fTY6am3GwF2PcdOi8ot0syPpCu1ucZrMR8Y422LCOM_qJ9eTHlbVDje4v1h4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63de6c0cf7.mp4?token=HpVkUYg0mjH2w_vOC7aOY2BmE9xqXWOL5C1PO8XwpvAjIFJ33XF_IDQRYK291WyAl-tWYyypgwR_jqDBh8R_XtfdjCh3j1KlJxqWgZFHczouWyvSx3qATrbSBwaCY2mhYNFU_R-7E6v0VKeoC7kuFVb9YBlqIITK2csA9OhhU0VfxHVRZgK6q0mOITDMswTRUbKrsawiByrpHADhgcNeqbtsiXVCbmKTAtEqGITSYNCntYL5PMkDDuw5SssX7Wf_kEYYf-cGRQXwaOwRaFeZ54zsIEtsqHN5x75yFTmaM0YmM5y4fiCvDKL9CSwEPclXKLpe3d5KctQ3B8-wM5cBrkxUPAR89LAkspnlRZYGlJOUGZHvvdeuhDbu8r0Q9cf1cl8EQn-R_DMxEsI8T0qWiF5YEQm8Rvb7i5-W9ZH64jjyaz7g7Qyl581avkf73CkatFHi6z67ZGYf8-jzV4zQDktrDIicnwd_YsBTPWp1TC1DD184jHKQKgCWyUne97GofPSUDdeulF0tIpQMIW9M_HAnJx_HNcw4TJzHmG7UAQQqWDtLROQMQLd35Uque2dMJUoO5Jkfw-hnUdIKbV2yGu-c9A5ZaLmjM23j4fFWeIRyc53fTY6am3GwF2PcdOi8ot0syPpCu1ucZrMR8Y422LCOM_qJ9eTHlbVDje4v1h4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139172" target="_blank">📅 19:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139171">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
همچنان معتقدم برای این تیم باید کلاه از روی سر برداشت و با این پرسپولیس باید با احترام حرف زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/139171" target="_blank">📅 19:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139170">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
همگی باید کلاه از روی سر برداریم و ایستاده این تیم و تشویق کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139170" target="_blank">📅 19:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139169">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9EIwda1u5K_UecyMcuek8axSighIiyB9nytF7ZQtd1Jo6vz6HYHRCPEjzrEAAPzejMM8JVJOv6UjoMUW85V7UEQZU-vaiUy8H7GJHfAhXZnQObTSCBugqdo8DbvFh5Qwn5LOZx60zk7nbTVlHYhmaEE9kKFalm94ZjYHi-8E6HH6NNnl8Devbiu4BgKaEdgnTByFaEv4PJe5U7HC3Omq3lR5C-frzHa7EUmTWWGAt8H4boxsjttUv4H9iff_HJLU87ln9emP0X5R0rafhDBPJsFyZj9-FX9RT6WB9p42yVpF71jeTOJ2kI9KiXyhmr8M0KNydaDELhnqt4mKJSbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/139169" target="_blank">📅 18:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139168">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJrx2VpV8HKuwMImita3gtrZKZYjXTi2SgLGmNojY165q7LgkIhgsNRxYs_pKfDE20L55TAFtmFg6EqzmGQJYKhUNAjGK1VEb9tF46rKaqbfuDrI3by3oeeBfmeM3v16CrswwjJJgqqxGu-DexAxevAtjpbXpcbHm0Z-GvIE9FG9CODt8PjvkY9-ynlKZWpWd5WPLt_zNjO-1DbqJsBXN0UNNwBa9ZyySbr0wn31l9PEhOeJdFo32Z7sfz1dhZNu9R1i9Gjrp1zUVJG7oFFrwh6BqMN4uJwoDDcZ8J6L4RgD3jqBhJVVAjk5q7kQqDDlmWLAZLx7KTWbcw6z3SqiMIpB8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78df0f8e05.mp4?token=XRmiRO2sbB7bqPKLlc4fjUJst0iaC-Xhvry7HO3681-NLigmGGBpGNLiB18KaRHjqTy8-1BlsEq2lJ5DeJ_WS3ziWnn8BVZnuJNz-dd16F2JgMH-mJoYT7G-jxPO2KdrZ8FC-BLCsa9m4hpyOfp7onN0lun49IsU-ehijWJ2U4uC-Yg0JXmKgfh36CX23W7PCYUEo5L3ubZGZMYtOMKMHl4xZLbc4EtXdoGxFAsFF_3yjnQWp3phpHOqNSmMp1ogOhVJJxjn4E07cGvwzfpZijbJpiwFJtMZLwrwSc1H75tjWC_zWHQUJARJuw3rsbNTFsdUpcwW2zY3mNNxG6PJrx2VpV8HKuwMImita3gtrZKZYjXTi2SgLGmNojY165q7LgkIhgsNRxYs_pKfDE20L55TAFtmFg6EqzmGQJYKhUNAjGK1VEb9tF46rKaqbfuDrI3by3oeeBfmeM3v16CrswwjJJgqqxGu-DexAxevAtjpbXpcbHm0Z-GvIE9FG9CODt8PjvkY9-ynlKZWpWd5WPLt_zNjO-1DbqJsBXN0UNNwBa9ZyySbr0wn31l9PEhOeJdFo32Z7sfz1dhZNu9R1i9Gjrp1zUVJG7oFFrwh6BqMN4uJwoDDcZ8J6L4RgD3jqBhJVVAjk5q7kQqDDlmWLAZLx7KTWbcw6z3SqiMIpB8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
ورود کاروان پرسپولیس به ورزشگاه شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139168" target="_blank">📅 18:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139167">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=OPc8-zBEvdpo5h6ulG9fy01kq_hvx-mRWQfA_fOtv2uShZgfgwiWxMf8aQJjSa35Xakow6DT6dXAK7kYwouEu4N2r3TSwP_76QwsHteq_qhGldkNF-bVMi3ml6biAEtY7jGDc7Ymyx7hoA1pwKZBy-C9Wpe4IVjDwWybFZ-8oza8-tEBC7LoZRrKmiSfO96D9GJSwMu0bZR1nQSFOpL5_ddWTtnw1Mfao6NnFWXQYNaQaG52JGXFux-Gq7IAM0Pn3njtZFpOXhDXtvhpTOl6MjJ-29QBbWXas9Wh0mwxhhnlDWdh5tUtsV32b8I3HSyv3KILvIWj0bxTVyiwJj9CGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153ca3a7ea.mp4?token=OPc8-zBEvdpo5h6ulG9fy01kq_hvx-mRWQfA_fOtv2uShZgfgwiWxMf8aQJjSa35Xakow6DT6dXAK7kYwouEu4N2r3TSwP_76QwsHteq_qhGldkNF-bVMi3ml6biAEtY7jGDc7Ymyx7hoA1pwKZBy-C9Wpe4IVjDwWybFZ-8oza8-tEBC7LoZRrKmiSfO96D9GJSwMu0bZR1nQSFOpL5_ddWTtnw1Mfao6NnFWXQYNaQaG52JGXFux-Gq7IAM0Pn3njtZFpOXhDXtvhpTOl6MjJ-29QBbWXas9Wh0mwxhhnlDWdh5tUtsV32b8I3HSyv3KILvIWj0bxTVyiwJj9CGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کری سنگین هوادار پرسپولیس: آخرین باری که استقلال دربی رو برد دلار ٣۵٠٠ بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139167" target="_blank">📅 18:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139166">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=rvCFozWiXII7rQXbD4VKWjq4H0cSzKe_r_FaUsEQwytwvwzu3qWfX0FpGetPP5bbR3o9RqzsM-zQMUYK6QteK_6j1K6V0KaocmIXtMhb2Rq2xKfGtVtV7KdiSVHNnQorfQyFJpkQ2Eh_h6wLmmmScFciCh23ukheCjkNHPzq71K0uBj-5uRDx4570UjShTvXtxLff1aXSehDy91RcqKGQ1WmCkJNXgaFgO7_pPJrVRvIjvKdd-gAyrWqNHzZCyoxkTwSy6lX6Rn7kjFsLY69vhdy1IA9TDNp2m4nRFFp5Yc-YsqVs03MmtM1krDTeDNBtkbSIoS_D8ovzrInePi2Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76c3af39e.mp4?token=rvCFozWiXII7rQXbD4VKWjq4H0cSzKe_r_FaUsEQwytwvwzu3qWfX0FpGetPP5bbR3o9RqzsM-zQMUYK6QteK_6j1K6V0KaocmIXtMhb2Rq2xKfGtVtV7KdiSVHNnQorfQyFJpkQ2Eh_h6wLmmmScFciCh23ukheCjkNHPzq71K0uBj-5uRDx4570UjShTvXtxLff1aXSehDy91RcqKGQ1WmCkJNXgaFgO7_pPJrVRvIjvKdd-gAyrWqNHzZCyoxkTwSy6lX6Rn7kjFsLY69vhdy1IA9TDNp2m4nRFFp5Yc-YsqVs03MmtM1krDTeDNBtkbSIoS_D8ovzrInePi2Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽
⚽
ورود طرفداران پرسپولیس به استادیوم شهدای شهر قدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/139166" target="_blank">📅 18:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139165">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76152fe425.mp4?token=FWEqiDP6Zy0V4NhZms19g2WzQ-fhd4ezbnMVVcDUN77Ul4lxRJ7irONfQ4cNKAA4iCuoj1lAdpptSeNlFf4lHakoy1U_duLYoum1tHx9rGFmr4WDV2w2Gcr-RgDJtZC3xMTcAjA9OAMrc4-KPGL3VvL6tb0cGJK2UpXP0Y5CPObmr51IRZiivpye65GRB7T6h-dP95uXTgpL9_xvIOf3PRBzFFvwt0ZP4H4LM8MCVigj5eo9sAxptYRO3CDZxgxyMQFi_ADjcdk7TeiGt5A34Z93o1s4ZvWv7FBfiQmfxmOo980Kdpj7Ro_UqW7EqCtEQrYy5pVyPDU7_1Dnvuyvmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76152fe425.mp4?token=FWEqiDP6Zy0V4NhZms19g2WzQ-fhd4ezbnMVVcDUN77Ul4lxRJ7irONfQ4cNKAA4iCuoj1lAdpptSeNlFf4lHakoy1U_duLYoum1tHx9rGFmr4WDV2w2Gcr-RgDJtZC3xMTcAjA9OAMrc4-KPGL3VvL6tb0cGJK2UpXP0Y5CPObmr51IRZiivpye65GRB7T6h-dP95uXTgpL9_xvIOf3PRBzFFvwt0ZP4H4LM8MCVigj5eo9sAxptYRO3CDZxgxyMQFi_ADjcdk7TeiGt5A34Z93o1s4ZvWv7FBfiQmfxmOo980Kdpj7Ro_UqW7EqCtEQrYy5pVyPDU7_1Dnvuyvmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
روش جدید ورود هواداران به ورزشگاه شهرقدس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SorkhTimes/139165" target="_blank">📅 18:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139164">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=C7d7t1aoHi-NuDsefn5drliLVuaMt9k3tDaGEn3Nkh008GPX4AMEcHHUPPnQ0GzizFGrEP1Q7hllg33smg7pu-xgVracfIUZ4LvVM9Gr6qtMOTXClXEVVPPxxLbF1eVGAY6UYPhzFqiwIyIk4fJFdtJAtFqp5JMbGONqiZa_Nx8T6Ox9T5FeArs3ADFIsZ85mWCghye6u6GWNnwbuoVaoPMAWQD0lfr94cG_tnIyIlwG3MsjHCy2lwPTSHH_OPNYEtDwhNW6TvuRN3g8pOLOSJSicp8NbF_dYAOhgNoik0pvdze6CppSYuRFHSEBve2gyY_ilRwPU_Fp0HhlvOUVTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95e62021f.mp4?token=C7d7t1aoHi-NuDsefn5drliLVuaMt9k3tDaGEn3Nkh008GPX4AMEcHHUPPnQ0GzizFGrEP1Q7hllg33smg7pu-xgVracfIUZ4LvVM9Gr6qtMOTXClXEVVPPxxLbF1eVGAY6UYPhzFqiwIyIk4fJFdtJAtFqp5JMbGONqiZa_Nx8T6Ox9T5FeArs3ADFIsZ85mWCghye6u6GWNnwbuoVaoPMAWQD0lfr94cG_tnIyIlwG3MsjHCy2lwPTSHH_OPNYEtDwhNW6TvuRN3g8pOLOSJSicp8NbF_dYAOhgNoik0pvdze6CppSYuRFHSEBve2gyY_ilRwPU_Fp0HhlvOUVTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چمن ورزشگاه قلعه‌حسن‌خان کوتاه و آماده میزبانی از دیدار پرسپولیس و ملوان است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/139164" target="_blank">📅 17:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139163">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/139163" target="_blank">📅 17:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139162">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/139162" target="_blank">📅 16:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139161">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=J5mHgKBK9jLjYtfHwHVElg8dff2Yc8JmbM_74U9l5ozqa2T9BQv-NMRJ5Tfe0pNQ5mK0rFHjsj-aKYueigfzt6EXjE8JpnoazyN6CFNzeFKN9CColtH8bNCw4o1USXoEUNjzcTXw72MQrPObS0-Kv72Ggx11iwtqO-anwo98D-Rcz-JPVBx3Sp_Z3PXF6AxFQcv1qrVX430Q3mB0-6eZfPCfXC3fF1Ix4VU897jKiz7S9Q1oFvxmvekjx85c8tqJpCiVLREKPdOJb4VfiWqM8-uGFENnG_R2kzBfjVWnJrU6cPbwKJ0ws3JYN8TyIYpefnNaw56n5Xw1928zJKEIEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5fbb7cadc.mp4?token=J5mHgKBK9jLjYtfHwHVElg8dff2Yc8JmbM_74U9l5ozqa2T9BQv-NMRJ5Tfe0pNQ5mK0rFHjsj-aKYueigfzt6EXjE8JpnoazyN6CFNzeFKN9CColtH8bNCw4o1USXoEUNjzcTXw72MQrPObS0-Kv72Ggx11iwtqO-anwo98D-Rcz-JPVBx3Sp_Z3PXF6AxFQcv1qrVX430Q3mB0-6eZfPCfXC3fF1Ix4VU897jKiz7S9Q1oFvxmvekjx85c8tqJpCiVLREKPdOJb4VfiWqM8-uGFENnG_R2kzBfjVWnJrU6cPbwKJ0ws3JYN8TyIYpefnNaw56n5Xw1928zJKEIEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
▶️
این وسط یهو یاد برد ۳بر۰ پرسپولیس جلوی نسف قارشی ازبکستان افتادم، جهنم آزادی، پرسپولیس مخوف و گادوین منشا ‌بی‌رحم
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139161" target="_blank">📅 15:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139160">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
باشگاه فولاد امروز بار دیگر تمام پیشنهادات پرسپولیس برای جذب رزاق پور را رد کرد و این بازیکن در فولاد ماندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139160" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139159">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
خبرگزاری فارس: تارتار دلش می‌خواست سرکیف رو جلوی تراکتور بفرسته داخل ولی تو ذهنش یه تصمیم تاکتیکی گرفت و فکر می‌کرد شهرآبادی می‌تونه بازی رو دربیاره
🚨
تارتار همچنین علاقه‌مند به سبک بازی سرگیف هست اما تعدد بازیکن تو تیم‌ باعث شده به همه بازی نرسه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139159" target="_blank">📅 15:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139158">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5rhOwcnYBy03bzl0MrntAwf8xHb6oEy-Zd7zgfnD6JpUdz5CPZDsOBN96612lIJOqh5r641Ev2ExiK3R8s-KmZoCnm_h0TIA6gm0QRL_ttKoYbM34IEgnOhIzIQhQe-Sq8Gi7UQoq39cHdJ8Vlz3zp07PtoNvn6YOduY99CEUbJfgGQVdsfgpUayN2bzYrN38ZdLuCxPxHJ3i7Qdq7Gfe8ftp0Rp3yX1E8YQq4IUi_KukAFdcLredSjhGeLu-LDzATrNexZWwNrcBusSJ0pZlt1Bmg-x2byN4wauzbQx6ouois8UBc8Hp12B6W8DPAVn9r1SLygjAQE6IufESmDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
جریمه 50 میلیون تومانی باشگاه پرسپولیس بدلیل توهین علیه مقام رسمی مسابقه توسط تماشاگران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139158" target="_blank">📅 15:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139157">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=M585R_kNjx6OUtd-LWaRMXfLz8oPtHzMA7IWD2QBohVO0FlVIKn60hvTNleo8SAKtNUZ2FA8RZJ0hITVSDXJjyuQkKFFyz4YaOlePFUWO7nEe_vhfmiSZ4J0F4KG15z37uCMPggbVzeVwZpNm-1DuQ8l0BUuiE8IZsGyIkbS5gNDsT3N6PgRzrA_HVyD2hX9r3B3UBsCbxvKFlmfUvPdIhWw74rrhuYxCqAnwK_Tju183-uIh69peMU5HKQ_XWFvAQYaxyqlTyohwicLbhKGPG05uVcI5pJuDBiodEruiMQcrCBNAJsoZJJjsM72wF6hM_zQtZi8n3CMfH_hpsDuZaLzxWHtf2dt0STAV4jCA86JL_LIGd7yyCDEbFcYvXBoN2cheZXFN8gmq5m2zkzjvUQ9MveLEPkZ-kyslqlXkIO1sfoImsmJL46z3ilCuYm6HT_0ccXAHCr4d5bZOYTES1H2fPWG7KkiEMFxo6I1QkZfEKduj3CeM_jffoO7N4yVYQhJvLtukDgtyCDeDfXVbLLxKk91IzoLIcK39qEYiGGa-1tlhZLKudunFIQCzNNj9S6_LptLvn2sWyiiQ4yG4CUD7CqqgOo-GvJYtR0MtRHYQcGFpKuWm6HBd5vbZfHiBGDsJRXahVWECeAeWiA9DwcNX9FqVodItJ6WbXT7q_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5667f8b6b4.mp4?token=M585R_kNjx6OUtd-LWaRMXfLz8oPtHzMA7IWD2QBohVO0FlVIKn60hvTNleo8SAKtNUZ2FA8RZJ0hITVSDXJjyuQkKFFyz4YaOlePFUWO7nEe_vhfmiSZ4J0F4KG15z37uCMPggbVzeVwZpNm-1DuQ8l0BUuiE8IZsGyIkbS5gNDsT3N6PgRzrA_HVyD2hX9r3B3UBsCbxvKFlmfUvPdIhWw74rrhuYxCqAnwK_Tju183-uIh69peMU5HKQ_XWFvAQYaxyqlTyohwicLbhKGPG05uVcI5pJuDBiodEruiMQcrCBNAJsoZJJjsM72wF6hM_zQtZi8n3CMfH_hpsDuZaLzxWHtf2dt0STAV4jCA86JL_LIGd7yyCDEbFcYvXBoN2cheZXFN8gmq5m2zkzjvUQ9MveLEPkZ-kyslqlXkIO1sfoImsmJL46z3ilCuYm6HT_0ccXAHCr4d5bZOYTES1H2fPWG7KkiEMFxo6I1QkZfEKduj3CeM_jffoO7N4yVYQhJvLtukDgtyCDeDfXVbLLxKk91IzoLIcK39qEYiGGa-1tlhZLKudunFIQCzNNj9S6_LptLvn2sWyiiQ4yG4CUD7CqqgOo-GvJYtR0MtRHYQcGFpKuWm6HBd5vbZfHiBGDsJRXahVWECeAeWiA9DwcNX9FqVodItJ6WbXT7q_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
کلیپ باشگاه برای بازی امروز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139157" target="_blank">📅 15:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139150">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c9BNXDd6CnklaOqfWblBeInIfy5zaXi3p7iuMnih1iNsrLy1AblPmpvlPw41J4nlVN3ZgeEIz3XUi1zGur2iu02ILGy18TprtwhGF0u4kK0OtOpld1PKKHFrhoEGLbIS4MtRdiK7_6gfTWjxIjPrrJMkmEKQPANLyZx3N4IiBtXWGVrCRdlWegz2jXRWtiajsGI3Aer4VDFXau6PvG867emyuhS0Em7fuc4fXoo6bzzgn0Dv3zUVqi533BuZVih6ooqsdN4avQVtdG7Jzsr6BY5YMG6qieoUi5ZjajHDjo2hrhyKfvb77sK3MNKUxvHLSe8_2-JH9Lcidc_Dwws8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ozlAblJ-97zV1tUrTFZIait4cx1jH-hBZPhcmkTyZkas6rVeDaYoZEaVjscf_Otv7nhvxZ9yCtr4gLsFBuMUK64T82aiPCPY1tYw_V__-AeKW6C5w2pnjP8ILTx6sma8W_yFmi5bhIBqQUoaTXHpUkVpA8MEC5YavmKE2bUtOnhwJJYL5hqU1FCtlnGHsIhz12qlfh7WJXKnNdyB_3XweZk9gGSNLnqPLylvlf_YTFsw94PYuJsutYkeihhkPhUxTGqimVf94iftZGDJNVF6cE-LLLCnlfMKF4RhtENKxYWzGZEjCDXwobbbO3GNErdB_5wcbQvYX7gzVmk2WhEwxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHFEqPI4AEGubFUAaiBn2zDvO9SW1D_BXX1WXI9vLwiA6XO0Z8m798fj6jiJUbeQlyBp9___pzwS9pDL2_SFN0hFyJpHtVUWIReDrGMYEk-UPzjA5Ubh87Uhl5tu-VIdAtoTDdPQXebTGaNLP1H0EfR0Cs1XamAaL4iPFhPnLq3pnbrbUA2oipY1g5l-A-23gZCsOj6WJdR_ARHA0vZj8n9OzX1eHwxiXcLkNmuISvWLDBrMbXCwxPWPecYgHGJn5jEivkm890ErRBJtHeVNx-peRgeZrKPaWPUsarTGyfFHCZWPKlUnA5H8Ocg3uZa_sjkHq-t6DiNBvwB1TpKDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRUaJJ-_No67j8xiVNbdtu4tZFwiqgEGgc_gKT1jNPzU6zIH0pcb9Xj9w5oF4kVTWWwGjMLCqfQGEIY4jL-Skw0ew5kE0MTr7PYT0aWhBCg8VgOJCuF6jZhjR3q9kaiJ5dtsFsNGFxYlzUbdGlrtyT88xRD_gndPfgSFFZ7VSs-9_ytWTDS8eVfgoHzIGYGbQ88aMC27cuEoUIViS1wWLxxRU0HLCN-T8Huq9efMigRwJMmloBIoMtXGT7pTmQ2LajnW-tmHYBBH5TxH-B78SRk2oVVrReV2IM0w5xOmqx1bcYrusbRn6exMnILRBu5cwop9X6R0KjnjFfhvz2iX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JCz_MG0ba7IwfvKg2MF61VlFckiualeDcF-oSi6ECKlf1RzDtOybIimrTVk9wmdD71JCZz3qmVKHI6MD5HTX38P5TU-izb1vWvscS6TqdkBDfTmxYLRVAKVRyaYZvspE-N-MI0AK5CftqdReN1n3igD2HqswdnJq1cl8ZfOgEMrjdeU_kCpVEE7P1S3R5rv_Hfn4fMOS11S5HQzotBTBs5RID-V1eyiVdSO5M0mwlVrj1I6lVecwaJcEVbaJ3GfR4marviq-EbKBg0Nug-AtfZgYoBJURsCxe89vCUUB9hjtwDGdl_cod2eh8oVyoJdP91xcMuB1lhNe6001NDFZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j49qWd4uAYxpupH5a4hjF70mRYUqrZOxyYePXCgUBwVyA4myHPidZRnaYivVsV7zRIj2877aoEGOrpHmD8zzWWXz5ATNPBMAfaEWCCWw0rNTwlz148aqhsiyEk-5zK2x5yNoYd6GXSggLpyDO9Fdu15CSFCkiiv2PwvSjkkbHWdDQzXHcJqR4AkJ5Gflza0LQa-4bjvOtXVim9ZAOvtgIWVYLRlX-s5EzszpN338HFHC6wE60Kg_4lTBU6uaNEBPoqD8MT9_loeI7HjwL-5o0yu1hOHi8BXn6vjxTE-M8IgNsurlqQzrc6pW_teEyWed0Zn6XjtTib8GmSAPre5GNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JnF1Fm3fg2Oo7M2UMXpVZ4RHk2hU8-A0yS79jQODKU83EeQ9a_eAPf88TiYl-0HITlGnhiPwUyLRq2sTVfsxF7VEomy3qsjTXPfRuggxsX4PcmVeglPJgjz7GB8LXEGXAJQOSjZWWfQoSMrNufQ2X9iBb40IOf9kPvN_qNADWCnTlXiz3AYzpijmug59S6brouHJRUWoO2fPDYc5WFqPdplKHl95tCWfe2ujs3GVClbrcm4j1ieg6KHqaAHCkUH9KR_LV8BiEu_5RFnAjWdgiI5uIlKuhx-aAI0zsXpRpN5qIhJfGl3Y-eeztBHXfIR5qDFHHlsNFvfE3N5Tb1Ntzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/139150" target="_blank">📅 15:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139149">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S14CDFoYxTsV7fZYzEQ_RizquEU3OhXIWDo6GKpk5W-SGt5FEm-aR8CMOGd_GCJxOn1tWcqLnEUmVm6XfTUUNEM113FNabTWH0ifbdZFmB3UGCr3qqJp7_ZbZ7GstR9M7u9_Fa4hiSaW6nuVZa1LWV9to_qVrl_g9zEfXBxv-vA5eSCnkCB3tenKmoza2mEXIUvByL9WsrAik-X1YRkhzLzqgaYj05cPomAu-Pi_8y27mx5GDg80iVDgX-z0GTrh2TetnMstfZoURIbTx_iiTSN6LYkesGtSJ6kn0PmIj89XfySbVtkDxjiocjcr4cvASLK6O5J4PBLwwQNKw5KJFg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139149" target="_blank">📅 14:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139148">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nTiXSKeGCd3muMTbL_MK43eDOb-OuW6WUrlNAMA9dKnRAWBhf1OtK8mSxetUnnH_ooFhq-mYfwtTvnT-nmBlTy3NvIb1YjxwDCmKkMQRMi7Bp0hxrB-Kwgx_DRNp5joBzX8pi8ZmtG9biEie2Nr-uIXz8iskKoDQ5XONWv1_ZniFXOed5a9oJJN0iPDrHuddT6osRnTA-fsPzrmvmYLNy-EfAJZgJ6S3g2tdW6Ga-a-M47Vkb0_WoJF1UAP2Ilt1c7oHf6Whl3xf-8eWgQQ7A_CW4aOfssdnduSMKO1xrawe_clEogs7AUVTM3G_pAY8PKQAbP47g3uCmAmkcuZX7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
رضاییان در توجیه رفتنش به استقلال میگفت هواداران استقلال جنتلمن و با فرهنگ هستند اما دیروز هرچی فحش توهین بود بارش کردند وسط بازی هم کلی بطری سنگ و ... سمتش پرتاپ شد !
🔻
🔻
بله آقای رضاییان اینا همون هواداران جنتلمن و بزرگ استقلال هستند که به مادربزرگ مرحوم جلالی هم رحم نکردن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/139148" target="_blank">📅 13:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139147">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139147" target="_blank">📅 13:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139146">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
✔️
دنیل گرا مصدومیتش برطرف شده اما تارتار بهش اجازه شرکت در تمرینات رو نمی‌ده و باشگاه هم گرا رو نمی‌خواد ولی تا پایان قراردادش در پرسپولیس میمونه/ فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/139146" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139145">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG8FT715h5sKB7OERV0SD9pk8-u0Ll7ZfzDbuRsDNLNk9zeRm4Qj55F--RJQnf_pFmx7E4xpPifZYDM3wfXKMTtzBffEN-zSCx_aqcoVZneGaKKWE7D2L8nVdI2A_n9PmDp2S3N6gbs7ZreIcC_Ga1RAkcXlssJsBgBZjTRL5mAqMN7Y0Dus0fFqRNRfrH9_iaZDvnPFYJACVY4KljWEDuzsjpXTp81BCzQsH2AT1RZgRABrD9DWu_YEd5c39gFHkK1Zv0xlalWNr2dOdIkJfW3lKXSAchT7BLHtlKn-1c1bW-VVUyJFp53i8lYiyrIpt_USqEy06nXAuPu83TU8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اتفاق عجیب در لیگ عربستان؛ از هوش رفتن ۵۰ تماشاگر!
🔻
در دیدار الهلال و الخلیج بیش از ۵۰ تماشاگر به دلیل گرما و رطوبت شدید هوا بیهوش شدند.‌ بسیاری از هواداران نیز پیش از پایان نیمه اول ورزشگاه را ترک کردند. الهلال این دیدار را با نتیجه ۵-۱ به سود خود به پایان رساند.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139145" target="_blank">📅 13:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139144">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">✔️
✔️
گفته میشه مدیران باشگاه گل گهر برای شکایت از باشگاه سپاهان بخاطر بازی دادن به کسری طاهری از تیم حقوقی پرسپولیس قبل از شروع مسابقه مشورت گرفتن!   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/139144" target="_blank">📅 11:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139143">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
فووووووووووری
❌
❌
یک سری شایعات پخش شده امسال بخاطر فشردگی تقویم لیگ خبری از جام حذفی نیست و قراره سهیمه آسیایی جام حذفی به چادرملو داده بشه
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/139143" target="_blank">📅 09:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139142">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌬
پایان بازی  نساجی
0⃣
-
2⃣
شمس آذر
🔴
👔
اولین حیا کن، رها کن فصل در قائمشهر؛ روزهای سخت در انتظار مجتبی حسینی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/139142" target="_blank">📅 09:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139141">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✔️
✔️
✔️
حجت کریمی مدیرعامل تراکتورسازی: چون دلار شده ۲۰۰ هزار تومان کسی نباید در مورد بیرانوند صحبت کنه. مردم به فکر مشکلات اقتصادی باشند نه بیرانوند
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/139141" target="_blank">📅 08:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139140">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
صبحی که ی بازی سخت و حساسی  داریم بخیر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/139140" target="_blank">📅 08:56 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139139">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9pbSxfk8AgW_pWaPLpMmZJlIPDyHd7oekDZEwnIcF5xy_W6HrWxw0hxgZe6x-PhB7VvJx5Gc0rzQFViXXd_Vve9AzLQX0PXZYWfHjcSnC-dgI1RhiLExj35IgGmKUl33JpHd8uMlKKMCa7N4XUKpZS6blG6LN8iY_tZy_I9aCTL9w3LbJ5NmLF3ak3ALecH9oaw-6sl7CeUSSi67PerN47maN087Yr1W0rONI3XZObZ5Pz273RdgKr7ypCn0B-naanXa56X14PcQ2_qTlvPDb9V2DzcY-tHxxVfSr8d6Z97CiOhloRCkkBPyftahr_GNqX8ZA5mNyg_qsdiUHJehA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/139139" target="_blank">📅 02:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139138">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQF6MjR1qFBzjAMp1KnGDXB_0SAUtVgKOgyQ5dTx8nAp7Eu-3ktsuPlDwlYJhFHq0gBk7beWP-Jc9gC2e6HDhOQUorS5k3_w9BfbYhrkvdhRfC09VQrJdOPQJcv7UuSbL19t7hhISG9QtfkwkekrjrK3p1yDAgQY6RJppVL1MxUxQpRYUsYUdJY7TBe63-R6Lt0uKfZSZHjNtO97EtpHPLzV-AxFxatl9s5W5Mh0nuHDsrV8ePURKgQ8JqRwAP6_4vK1pnfFLIUQsNnqbVwwFs9pCVFCKjPsqQ6wqjBUw7Qz_PmJLFW-ZlyrnFNPNY6N5txC6fSivo8KtDk9iwBWbtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/241731bcb2.mp4?token=qmPsaYKMYhZ8jDHIkHfP-AWQYqM4vBBCZnnveEWOwmjfa0XSvSqK1OGy8p4ntxZOPJ9BFG9-ZzMi3zs4bGdUwvuMv2tj7tBaaombnivPJYZ01aaJYeAoBv8zkLwq4N-2VX2FdH3bjSOvgsl6alTe6mYRtmxtDuc3PZgWhOSZaba_Bo8DGutRhqydSRydGdYyrMvpwRktC25Z16cKJxPWwKIC-ZHmvhBKrEvrWVX4OJ3wXRLO3c4qckAt-zjpPmJHLLm3E4oZwjuEse16EEplwfk3gluq-XbbO4sNzbaRKfZnb0Rl7HvsTV23xWmNFjv7pPIfeuXNM7b-YW7LAAHnQF6MjR1qFBzjAMp1KnGDXB_0SAUtVgKOgyQ5dTx8nAp7Eu-3ktsuPlDwlYJhFHq0gBk7beWP-Jc9gC2e6HDhOQUorS5k3_w9BfbYhrkvdhRfC09VQrJdOPQJcv7UuSbL19t7hhISG9QtfkwkekrjrK3p1yDAgQY6RJppVL1MxUxQpRYUsYUdJY7TBe63-R6Lt0uKfZSZHjNtO97EtpHPLzV-AxFxatl9s5W5Mh0nuHDsrV8ePURKgQ8JqRwAP6_4vK1pnfFLIUQsNnqbVwwFs9pCVFCKjPsqQ6wqjBUw7Qz_PmJLFW-ZlyrnFNPNY6N5txC6fSivo8KtDk9iwBWbtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#منهای_پرسپولیس
👤
فراز فاطمی سرپرست چادرملو:
❌
آقای حیدری فکر کرده ما خریم. قشنگ بگید میخواید یه تیم ببازه دیگه اینجور قضاوت کردن بخاطر چیه. امیرحسین حسین‌زاده با تکلی که زد دوبار باید اخراج میشد ولی حتی صحنه به وار
هم نرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/139138" target="_blank">📅 01:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139137">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">✔️
✔️
براساس‌صحبت‌های‌مهدی‌تارتار؛ سرگیف از بازی فردا مقابل ملوان به ترکیب سرخ‌ها برمیگرده و تارتار میخواد زوج علیپور - سرگیف استفاده کنه اما اوستون اورونوف همچنان نیمکت نشین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139137" target="_blank">📅 00:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139136">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
استقلال فولاد مساوی تموم شد.کیسه خیلی خسته و کوفته شد و واسه دربی قانونا خسته میاد تیمش امیدوارم استفاده کنیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/139136" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
