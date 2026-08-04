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
<img src="https://cdn4.telesco.pe/file/bEKebfLH_7V01P_vfjHsq8LZ9BJq1x4NSFbg8nZV_PziNV3Q85TRgoOSgK5lixHR3UAjxo2-xN9pAgfda6UYIP2Zg5YXUidGAq73CR06497hMzqu-gzDxDuANHBT9FQP39ZlfB-TY9ZXd6uAWpdG6qZinnYyZUhQYHarg9S59-mVQ2p5vw8mfUzvMtdrFKbTXHOrWKqQJvs91ax6BiHQ7g74P1IQyfEI5e75Slx2lWQWgFSbMKZECzRLr8EnDI52xs47kYnCWXwST9aDL7ub7LL0hsfzeugfviHjAX6R_YZ_zYJCO5nD6L_HCMMh1-Dk5p7S-4mMxqTomzxOpU78SA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 21:39:20</div>
<hr>

<div class="tg-post" id="msg-137339">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
رضایتنامه حسین نژاد از 6 میلیون یورو به 1 میلیون و 500 هزار یورو کاهش پیدا کرده، حسین‌نژاد جز استقلال و پرسپولیس از ریو آوه پرتغال هم پیشنهاد جدی دارد‌ ولی اطرافیان حسین‌نژاد می‌گویند اولویت  وی همچنان ادامه مسیر در فوتبال اروپا میباشد
✍
ورزش سه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/137339" target="_blank">📅 21:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137338">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/SorkhTimes/137338" target="_blank">📅 20:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137337">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⚫️
⚫️
⚫️
سرمربی باشگاه پرسپولیس به الن هالیلوویچ هافبک کروات پاسخ منفی داد و حضور وی منتفی شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/137337" target="_blank">📅 20:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137336">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
فوری از ورزش‌سه:
⬆
مذاکرات مخفیانه استقلال با رامین به نتیجه رسید و در صورت حل آخرین جزئیات مورد اختلاف رامین به استقلال برمیگرده و در ایران میمونه!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/SorkhTimes/137336" target="_blank">📅 20:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137335">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoG5ovxBeAFtL61YSYmByL0jlBuQ94wVdgDAD7zzjpJgHUSq9U9lJ8v1skTrjFI5zBHJ1aqESGQButgVhBueMnVf_1wntFs0CIRlIHgYKyjgvFh8R3clYTCR8o4WQgz-RNWz44WzG10S8br_fZcXU68YHRleg2bGFit6GP5V7PDwHn0prRsCswX8Qa7qurC-m2m1cZ0CiyHv6Vk-1mErUlqdGuQN_HTw0duItlchwcJhvQ9feny3Icj86qLtpmZultt4BUkrhf-dMKPtgNNx9avWPLFbOMDApgDs4ys39CnRABADkLsxKdPUvQdlRVWTBiEjbT6HYu0B0wBv_ro_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7️⃣
بونوس اختصاصی ۱۵ چرخش رایگان بازی Egypt Power
💰
فقط تا پایان ۱۷ مرداد، با حداقل ۱ میلیون تومان شارژ، ۱۵ فری اسپین رایگان
Egypt Power
دریافت کن و بدون پرداخت اضافه، شانس خودت را برای شکار جوایز بزرگ نقدی امتحان کن.
⚡️
پس از شارژ حساب کاربری و فعال شدن فری‌اسپین‌ خود، وارد بخش بونوس‌ها شوید و ازین فرصت چرخش رایگان نهایت استفاده رو ببر!
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/137335" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137334">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
فوووری؛ باشگاه فجر سپاسی شیراز بازی مقابل پرسپولیس در ۱۶ مرداد انصراف داد.
❌
❌
احتمالا نساجی جایگزین این تیم برای بازی دوستانه ‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/137334" target="_blank">📅 19:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137333">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Idsq2uoBQgVI2mD1JZYmezgZBNmrWOFL1ou2pSinNexkYtD_HgdTjOmabIBnedMBRzl8wvWQFXApFj4blJpAOQBT2DEHUuh-hxvW8F_8irJohwK9J4rpe-4J4nID7gD27ekGpoXLsgfYtTQ-Eiw21S1XEvKmwVmG1j_wXNoMJeUMx45_VKV4VUMDrf17CAHg3Ct-oo5URZrcCbpUYOhjH9o_Yk5R-4WIJg1mk2-g4gfXJwmfO72MbzAsL2vt1muAEDE_UUqsdV8wQ8N3HTaD8XnAD0qWSJZmbjKeI5nJ8pV9L3zWPt5UaWQqI_mxOy8JyE4PFfWiYH_bStveL7Tn_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
#
رسمی
؛ علی نعمتی مدافع‌ سابق پرسپولیس و فولاد با عقد قراردادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/137333" target="_blank">📅 19:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137332">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
❌
فولاد قیمت رضایت‌نامه رزاق‌پور را برای پرسپولیس ۲۰۰ میلیارد تومان اعلام کرد!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SorkhTimes/137332" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137331">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyOv-1LgLu98hH_409NvsGBWDqUp5o1j5R8x4A8wSc5TFdqCThrXYwux9w7x78j4LRmni3_kFFqwurGp36FoVulZOr1E15MqLbtqhUiuwpiT6G9B1oKe4S_IgQM-BSbmlOs90J5ho322eIyCXGuZgc6StfI9YG1LbG21iEuKMAU9rWcKftAun_D8XnSqt_FMuULqw8xHAaGmW1aWcYickz3r5gj8QBwUXvc1A7gH3oMnPIVPE1iLs370PNcPAweouzoX0C4rKEIyEeo936CiWoXF4FMBKOQDhzedzo-qq7ymbB-7HNo-dTrcbNMCyj2TiNABkhT-xA0fVbvdLU_RiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تارتار نه از جلالی و نه از عیدی راضی نیست و دفاع چپ و راست میخواد
☹️
☹️
☹️
///فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/137331" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137330">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
15 روز تا اولین بازی پرسپولیس ورژن تارتار در لیگ برتر مونده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SorkhTimes/137330" target="_blank">📅 18:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137329">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
🔴
🔴
🔴
مهدی تارتار تأکید ویژه‌ای روی جذب محمد قربانی دارد و نام این بازیکن را در صدر فهرست نفرات مدنظر خود قرار داده
🔄
🔄
باشگاه پرسپولیس همچنان در حال چانه زنی برای کم کردن مبلغ رضایتنامه است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/137329" target="_blank">📅 18:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137328">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
❌
امید عالیشاه بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/137328" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137327">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🗣
باشگاه عصر دیروز به جمع بندی رسید که باید برای جذب قربانی اقدام کنه
👀
مذاکره با قربانی و ایجنتش که رابطه خوبی با مدیران الوحده دارد شروع شده و امروز با جدیت بیشتر پیگیری شده است.
🎤
حسین قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SorkhTimes/137327" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137326">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
محمد انصاری که در تیم جوانان ایران به عنوان یکی از دستیاران حسین عبدی فعالیت می‌کرد هم اکنون یکی از گزینه‌های جانشینی او در این تیم هست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/137326" target="_blank">📅 17:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137325">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس به فولاد پیشنهاد بیفوما + ۸۰ میلیارد برای رزاق‌پور رو داده که مطهری گفته اگه یکی از بین علیپور، سرگیف یا شهرابادی رو بدید میزارم جدا بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/137325" target="_blank">📅 17:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137324">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gusKX8SB60Vs_gbTASm5B3WQIImRtLuliasnZ-YXsxyWyDVZZ-WIQdhhLau2vJNIUoGuT3ncWJum1bqZij9jug3zhSh5vvzLv4KN-27uhshfC14XLIZZIq3_fGLyu0uTGXSEQDF4WOdY10gFtLMX22if1i7VEaxqCzFmchGuGKsOOUlSDWj3vvnjZ5p_j_b93ThonwxRs-5qRSOxAth6p-BCRLkVYv9Gg7uRXNxzxE1WU2jbA-BK45v7mOM9lPjr_gDzb5miMq3xWaXYccnbIlFLTOApRDw0ENirHK9gsPvKNvSU2oozWwdbE7j0WN4uf_1RjZlcBD0oZMqKmsVZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
🔻
پرسپولیس تنها تیم در جمع تمام تیم‌های لیگ برتر بود که اردوی خارج کشور داشت و بیش از ۸ خرید جدید هم به صورت رسمی ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/137324" target="_blank">📅 16:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137323">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">❌
❌
❌
❌
کسری طاهری: وظیفه‌ی من بازی کردن برای نساجیه و درباره بقیه مسائل باید مدیریت پاسخگو باشه/الان زمان صحبت کردن درباره‌ی اون داستانا نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/137323" target="_blank">📅 16:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137322">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
🚨
🚨
فووووری 360: رضاییان از کیسه جدا شد
🚨
🚨
با توجه به حضور صالح حردانی و سامان تورانیان، سهراب بختیاری زاده با برگشت رضاییان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/137322" target="_blank">📅 15:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137321">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔄
🔄
🔄
پرسپولیس به فولاد پیشنهاد بیفوما + ۸۰ میلیارد برای رزاق‌پور رو داده که مطهری گفته اگه یکی از بین علیپور، سرگیف یا شهرابادی رو بدید میزارم جدا بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/137321" target="_blank">📅 15:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137320">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
با اعلام ایجنت رامین رضاییان، این بازیکن از استقلال جدا شد
🚬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/137320" target="_blank">📅 15:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137319">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🗣
🗣
🗣
عبدالله ویسی سرمربی ذوب آهن: با یک بازیکن ( امید عالیشاه ) وارد مذاکره شدیم برای یک فصل از ما 130 میلیارد خواست و من جلوی این انتقال رو گرفتم. ما تیم جوان هستیم و نمی‌توانیم چنین هزینه های بکنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/137319" target="_blank">📅 15:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137318">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
❌
طبق شنیده‌ها: سید مهدی رحمتی سرمربی گل گهر سیرجان موافقت خود را با فروش امیر جعفری مدافع چپ 24 ساله این باشگاه به‌پرسپولیس اعلام‌کرده‌است. رحمتی در این پست قنبری شاگرد سابق خود در خیبر رو میخواهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/137318" target="_blank">📅 14:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137317">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
❌
❌
ترامپ: در حال حاضر درباره بازگشایی کامل تنگه هرمز تا فردا با ایران صحبت می‌کنیم. این آخرین فرصت ایران برای دستیابی به توافقی خوب است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/137317" target="_blank">📅 14:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137316">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_E7scgOt6DknGfyBtoh_-5DbGGzbHpMBd-0LJZRcMPxDOrfyAuIMkj8BAk8SpbQkMp_o3iK823z1tFwg3TCybAoUhKKLzsNEIsC_BSOiTZqOzK0y59xm4BNMAWOfLhH42HJnI1EVDvVQ595jcy_CwWaKuZnRvkFWKoruG__eXy3GvRzWMWXh0OaTMfMCtX6zkUytAJ3s2LISEqPcG_2peD-MHC1xhO-1YrAYruZ4pvsoRa4cIfKqodXZHsPH8tzkg3TF0JQxsnn79TM-Rj1Eb4-63KnOzeAKYg8KkP5Z8KpCdv9aiQVPHhMYEC8uwST1H2rdg7zV7TkLs64qYGZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد برای صعود؛ شبی سرنوشت‌ساز در لیگ قهرمانان اروپا
⚽️
دیدارهای امشب مرحله مقدماتی لیگ قهرمانان اروپا با رقابت نزدیک مدعیان برای رسیدن به پلی‌آف دنبال می‌شود. تیم‌ها در تلاش‌اند با کسب نتیجه‌ای مطلوب، شانس خود را برای حضور در مرحله اصلی افزایش دهند و همین موضوع می‌تواند بازی‌هایی تاکتیکی و پرتنش را رقم بزند. انتظار می‌رود جزئیات کوچک و عملکرد ستاره‌ها، نقش تعیین‌کننده‌ای در سرنوشت این مسابقات داشته باشد.
⚽️
بازی‌های امشب رو در
ربات وینکوبت
با ضرایبی شگفت‌انگیز همراه با ۵٪ شارژ بیشتر از طریق کریپتو پیش‌بینی کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/137316" target="_blank">📅 14:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137315">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❌
10 باشگاه لیگ برتری صبح امروز با ارسال نامه ای به سازمان لیگ خواهان تعویق 10 روزه لیگ شدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/137315" target="_blank">📅 14:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
🔴
🔴
ایمن حسین مهاجم ۳۰ ساله تیم ملی عراق، در انتقالی آزاد با قراردادی یکساله به پاختاکور ازبکستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137314" target="_blank">📅 12:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‼️
آخرین وضعیت ایمن حسین ستاره تیم ملی عراق در ترانسفر مارکت که درحال‌حاضر بازیکن آزاد است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/137313" target="_blank">📅 12:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
تندیسی زیبا که باشگاه پرسپولیس برای امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک ساخته بود و‌ این بازیکنان برای دریافت این تندیس حضور پیدا نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/137312" target="_blank">📅 12:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
❌
علیرضا بیرانوند این فصل سرباز هست./ ایران ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/137311" target="_blank">📅 12:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137310">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX7m54mfhzutW5iSX6hvUFYzpnCP_2cNhjGMEEB5hjP7W9X9wZhwqzGtnmj4FamnFhuO_NDRbIguNLjjXxlXLXXB46DwfDYveY8nKhY0P0r8AzKqzOz7vdqrgWpnRI0mywQnI0hKvEQZkIXdUyZ3YiL_IBYj0WAttKrDGNFdAHXTme2NDREPu7t-_Q6QfxWKZ8McDKJMA2maQ_fdsCSDP4k9zdk4VZfbayLn1zxjpNTKVy7vS1Yz4qhy7D5TVmui7lq_EDem1YR_a3NZtCH9mwskZe_3loZRXOdgcO_-t0rtjZT5VQV9HLvf5HDuOGdrcjUtOa2CnNdzQgj86BpwJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
تندیسی زیبا که باشگاه پرسپولیس برای امید عالیشاه، مرتضی پورعلی گنجی و میلاد سرلک ساخته بود و‌ این بازیکنان برای دریافت این تندیس حضور پیدا نکردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/137310" target="_blank">📅 11:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137309">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">⚠️
⚠️
⚠️
مدیرعامل باشگاه گل گهر سیرجان :
⚠️
⚠️
امیر جعفری مدافع چپ مدنظر باشگاه پرسپولیس قرار دارد اما تا این ثانیه به صورت رسمی با ما مکاتبات نشده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/137309" target="_blank">📅 11:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137308">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
✔️
گفته میشه که تارتار بعد چند سال بالاخره جاسوس تمرینات پرسپولیس و پیدا کرده و بدون رودروایسی کنارش گذاشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/137308" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137307">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووری
📊
📊
خبرگزاری RB اسپورت روسیه : مذاکرات پرسپولیس و دیناموماخاچ قلعه برای حسین نژاد جدی شده است و امکان توافق طرفین بالاست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/137307" target="_blank">📅 10:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137306">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❤️
📸
تصاویری از شادی بعد از گل علیرضا همائیفرد پس از باز کردن دروازه حریف
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/137306" target="_blank">📅 08:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137305">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
🔻
🔻
ترکیب پرسپولیس دوباره لو رفت؛ تارتار هم دنبال جاسوس می‌گردد
➡️
➡️
➡️
فرهیختگان: سرخپوشان روز گذشته به مصاف تیم پیرامیدز مصر رفتند. اما جدا از مسائل فنی، موردی که ذهن مهدی تارتار و دستیارانش را به خود مشغول کرده است، بحث لو رفتن ترکیب تیمش یک روز قبل از مسابقه…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/137305" target="_blank">📅 08:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137304">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74903f0977.mp4?token=l-Uyx1-4ACh_-FlmfrSW1uJnaOvsO1Q7XcghDaaiy19kzQGD9Y9_Dzi_V8ZuSkKo256daFUQNbxl8XfO_NbrUoQwKfbjT3KfgvwBvV2gd34ueT3JLP6ct3s7COgeuEQAfYtXKRcAIkxKCIr6akDbguXbXz_kfoEwF7TGl1BrdYAT6ch3sBpD98-V3ApEqTQEKWndbPC00nATAVqXeS1TqdieDdvNc4lN86361mZcwfITXtkDHB5tWwM54QnTb8WkZ-ajoao6blgtjF3G9-dpy-FYDR4MQTWvjcvU9VD4CEJTkA_lJLxEVjIUUATUd1uKHKWdvT4NdXoDnC3tKzj6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74903f0977.mp4?token=l-Uyx1-4ACh_-FlmfrSW1uJnaOvsO1Q7XcghDaaiy19kzQGD9Y9_Dzi_V8ZuSkKo256daFUQNbxl8XfO_NbrUoQwKfbjT3KfgvwBvV2gd34ueT3JLP6ct3s7COgeuEQAfYtXKRcAIkxKCIr6akDbguXbXz_kfoEwF7TGl1BrdYAT6ch3sBpD98-V3ApEqTQEKWndbPC00nATAVqXeS1TqdieDdvNc4lN86361mZcwfITXtkDHB5tWwM54QnTb8WkZ-ajoao6blgtjF3G9-dpy-FYDR4MQTWvjcvU9VD4CEJTkA_lJLxEVjIUUATUd1uKHKWdvT4NdXoDnC3tKzj6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔴
فرا رسیدن اربعین حسینی بر شما عزیزان تسلیت باد
🏴
⚡️
الهی به حرمت این روز همگی حاجت روا  و عاقبت بخیر باشید
🙏
الهی آمین
🙏
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137304" target="_blank">📅 08:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137303">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3J67Qh4ZarltHTQCBENHTjSgHcKRghI2CjMG8sbrBnG5RHiO1dDACNNDGcIv0sygZGjVPLDYGCJFUQyJb73QPEP_MqdjX4Kx62eLESDXZbuSWWQPqpSroPgChokGdgrWhIffY63cOp7MIe4DeJOn66SQr8_NhoP8QgE46DAJvqR2t7MgcQD_fGgLW7VUwPW39_hTSAwzwh8D1AGrkRs4a7H7qdry7YMQhGthhRIR4e1DSuUTXm9bxTFn4DWhD84GuL2z4DxeLDP9b1U4Opqbkchk0gsZ8zc0B1Q5UvSocF7_vdLRd85b1mId2VLjfyW5x_EwNmUWvt2SGcUxf0MZG8Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a058da26.mp4?token=Dyi8y1BsSixeOBZsgbWxFkieoM7XSc3lTO4u5t3qIHef7rZWMpxV09VHbsvUoDW5toxnoKi583s1fw_4LKbYxWpht0LGIRYNTc-yk6feOqG8NfNWsEg_28BNGiZOvWO5uPwXmQ-olyJwRurwDBHNZo_nRKLjOdcIFWYTHiD4SU-f0r4-EuFiTVW5fnTwMtXchNRN4_kb9kdh8EUx1ZVcjAWrZMLyYbXu1477-MUHYHLvnIJBgsErqQAAq35n7qrLnneCaMqyZwkykLDEfBB1qTpY-RqCTAgfmFVKVaYwu2OK3k7SmWztMVrg8ozESyo5DvTRw7VtHPKMuudQg6re3J67Qh4ZarltHTQCBENHTjSgHcKRghI2CjMG8sbrBnG5RHiO1dDACNNDGcIv0sygZGjVPLDYGCJFUQyJb73QPEP_MqdjX4Kx62eLESDXZbuSWWQPqpSroPgChokGdgrWhIffY63cOp7MIe4DeJOn66SQr8_NhoP8QgE46DAJvqR2t7MgcQD_fGgLW7VUwPW39_hTSAwzwh8D1AGrkRs4a7H7qdry7YMQhGthhRIR4e1DSuUTXm9bxTFn4DWhD84GuL2z4DxeLDP9b1U4Opqbkchk0gsZ8zc0B1Q5UvSocF7_vdLRd85b1mId2VLjfyW5x_EwNmUWvt2SGcUxf0MZG8Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
تجربه‌ای متفاوت از هنر روپایی و تصمیم‌گیری با Crash Kick؛ جاییکه مهارت با هیجان گره می‌خورد!
⚽️
در کراش کیک، هر روپایی موفق ضریب برد را افزایش می‌دهد و هر لحظه وسوسه ادامه دادن بیشتر می‌شود. هنر اصلی بازی، انتخاب بهترین زمان برای برداشت جایزه قبل از پایان روند صعودی است. این بازی با ترکیب هیجان، تصمیم‌گیری لحظه‌ای و مدیریت ریسک، تجربه‌ای متفاوت و نفس‌گیر را برای علاقه‌مندان به بازی‌های سریع و پرهیجان رقم می‌زند.
✅
جسارت ادامه دادن یا هوشمندی در برداشت؟ تصمیم تو، سرنوشت جایزه را مشخص می‌کند.
📌
همین حالا وارد ربات وینکوبت شو و هیجان واقعی رو لمس کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137303" target="_blank">📅 01:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137302">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/SorkhTimes/137302" target="_blank">📅 00:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137301">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
گزارش تصویری / پایان اردوی سرخ‌پوشان در ترکیه!
❤️
تصاویر منتخب از آخرین جلسه تمرینی  ارتش سرخ در اردوی آماده‌سازی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137301" target="_blank">📅 00:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137300">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUEwEhXYrbKcFfJ5weZWNdAqngwsCyYonPl3PllB4DGQM1b2SASwSD3OhmFn9OCW7E9LzIjHSUpWSZ8HaLtknflwT2cHz8D8kYpfHQKomdVO6y6ggB3hv33lvIycSejUSXdpc4SesqAQyxQKZRNlQ9hOrA0xB1vAyZwKbSJIRCe5zwYdocCR12K4kKdlymP-O5gwY52MydsAlMfna8wfPj0D2RRvTWWdn-YpHLsVyyBknKoggOhQLAUllfq80N6fq4h7ZhgQdaZITnzSwz6ysKxjIhGlZpffc5WVuJKBAe4I_f1aGIx6p573C_wcKkRyGyYx85T6AnXF-6YGXM-DKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
با تصمیم مدیریت باشگاه پرسپولیس زمین شماره ۲ مجموعه ورزشی درفشی‌فر به نام شهید ماکان نصیری نامگذاری شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/137300" target="_blank">📅 00:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137299">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCxH5tnOtq27gQ8HulGX0Plh_BSTX7xI0gwKDVBHR3i8WduOtP2fC5hWLLYE4LBjG908kOKA_nqGyy29R5G-1x1Jvd348bESZQp_tKv6_4u2STcCnylO-1yH07Bx3QEp3Jt6R6Ej-j1l__996nYRNFiuy7PsFvep_4qUzl3nFoqf7XHOjeCopOY0HLYpyvlbJVY0K3Q2nSkXTwVYxum0IEXNxXFYuEdgTfgdLk6r0gYdJzXebFe699c0jH3ElCTc_RBGmqZ7ddFyBLdtkc8BepkZhWmycNAOCNqD21l6P8wJ4LMkVeigAQNx947wI2lcbstYJRjXhlrTCkYEkibu5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فووووووووووووری
🚨
با اعلام ایجنت رامین رضاییان، این بازیکن از استقلال جدا شد
🚬
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/SorkhTimes/137299" target="_blank">📅 23:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137298">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
احتمال تعویق یک هفته‌ای لیگ برتر به دلیل درخواست برخی باشگاه‌ها افزایش یافته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/SorkhTimes/137298" target="_blank">📅 23:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137297">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
❌
خب ظاهرا پیشنهاد استقلال بهتر شد و پستای استقلال برگشت
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/SorkhTimes/137297" target="_blank">📅 23:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137296">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⚠️
⚠️
امید عالیشاه به ذوب‌آهن پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137296" target="_blank">📅 23:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137295">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNzq9WUK2kIMW8CGku3Z0dWptSp-4njcO01HEXFIwsrmiBMaBg5agoU20BNDcLfIKEPE_rxNm5Ooz9R2Dbetzum9mJ5kDa9Hn8FalQvD9yARtVeSloDxY3XUt-MqtjCNWRBS6hnfvbl2dTDA8l2sSAnSEUVlGCzcJmBAmNQmuukLfbaFEzloXnoAuqivgaG6Ncnsrw66hSQnbu67aBHsHoIG0Zjjt4DD04m2AyHBFYvs1ae3RR7q-r82IIIESoI8PWRzG5XYsAzzx4UL0GewwolnXKmCqQ0QPUXXCAqV0P6aE6EZHhoPqmyHyDBh4KxLzxandKQOHG8vbzNbS9V81w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
احتمال تعویق یک هفته‌ای لیگ برتر به دلیل درخواست برخی باشگاه‌ها افزایش یافته است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137295" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137294">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
🚨
📊
فووووووووووووری
🗣
باشگاه عصر دیروز به جمع بندی رسید که باید برای جذب قربانی اقدام کنه
👀
مذاکره با قربانی و ایجنتش که رابطه خوبی با مدیران الوحده دارد شروع شده و امروز با جدیت بیشتر پیگیری شده است.
🎤
حسین قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/SorkhTimes/137294" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137293">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
✔️
شرایط ایری از نظر حقوقی متفاوت با کسری طاهری است.
✔️
اینکه پرسپولیس همچنان دنبال کسری هم هست یا خیر و اینکه نساجی حاضر به انتقال فقط ایری می شود یا خیر نمی دانیم
✔️
تارتار بشدت دنبال جذب مدافع میانی و چپ است و ظاهرا گزینه ای جز ایری و رزاق پور ندارد.…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137293" target="_blank">📅 23:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137291">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
فوری/ ترامپ: به درخواست ایران و کشورهای منطقه، حمله رو برای فراهم شدن زمینه توافق، متوقف کردم. ما کاملا آماده حمله بودیم اما حالا مذاکره می‌کنیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137291" target="_blank">📅 21:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137290">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
قرمزآنلاین: دانیال ایری، رزاق‌پور و محمد قربانی سه خرید پایانی پرسپولیس
🚨
🚨
باشگاه همچنان برای جذب ایری و رزاق‌پور تلاش می‌کند، هرچند فولاد فعلاً با جدایی رزاق‌پور مخالفت کرده است. همچنین با درخواست دوباره تارتار، مذاکرات برای جذب محمد قربانی پس از کاهش…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/SorkhTimes/137290" target="_blank">📅 21:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137289">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a103c22f7.mp4?token=YEFTg6W-I-uCuW5b6oLqG0kvUyfw-kUti6491ypKGUNq_JhIXc-nIlBvCKYaZ-K76y7Vr4oEe6SCqCXdD2KyEdGbfx7EJTP12BJOZ4WjaMehVtzlc66QC2wmh3G7NevHQDTCJdMUr4OhbbZ3c-LRzc8GRFH_BO4Wd0nkK-G16Z9r2ue1nfnZ8QoElCchD7JV8A8EvL1jrdMJsTBK87TvRdwl5rO9TQZqDp7BV9f5GzpPvB2j5hr-jT5LIj9oYNYcllWfSw7-2sx_8qvJabqsBtXVsjcAo4DcHDl7mICrNZ19d6eSDFFYgVT3qcDcwqbtFhIPnrSdjZyx06NDasRVkRCfC01P-KbOw3IfLFW__Jq8DcbN63DXmv7XD0cP4_4bY72EXPqYoYGY5KslHro0MN2tK965FUq0g9ftiRTRHEf9r3SsAi8-wv92qI6yGMDMG0TB-wBqD30omvudcifhtdOl1-deNQzzlbb4bDWRdHXAIV23H_C0BCj-05mpwmxARFM6xIMgR4AnLLGBk4nfsRECWCBLLW0ejGYPYguf6IuL3tnHFRe9SPZVFoSBPOce6Kd9wu34cRKxQ0YuTdtQRgJadiueNu-owtzRfqUwocUXgqFClYHEJ7UrZv4LrPLx-kZa9hRrKI62sLXDUKyPIyDhVRZjAlaESxGYsvqOAHk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a103c22f7.mp4?token=YEFTg6W-I-uCuW5b6oLqG0kvUyfw-kUti6491ypKGUNq_JhIXc-nIlBvCKYaZ-K76y7Vr4oEe6SCqCXdD2KyEdGbfx7EJTP12BJOZ4WjaMehVtzlc66QC2wmh3G7NevHQDTCJdMUr4OhbbZ3c-LRzc8GRFH_BO4Wd0nkK-G16Z9r2ue1nfnZ8QoElCchD7JV8A8EvL1jrdMJsTBK87TvRdwl5rO9TQZqDp7BV9f5GzpPvB2j5hr-jT5LIj9oYNYcllWfSw7-2sx_8qvJabqsBtXVsjcAo4DcHDl7mICrNZ19d6eSDFFYgVT3qcDcwqbtFhIPnrSdjZyx06NDasRVkRCfC01P-KbOw3IfLFW__Jq8DcbN63DXmv7XD0cP4_4bY72EXPqYoYGY5KslHro0MN2tK965FUq0g9ftiRTRHEf9r3SsAi8-wv92qI6yGMDMG0TB-wBqD30omvudcifhtdOl1-deNQzzlbb4bDWRdHXAIV23H_C0BCj-05mpwmxARFM6xIMgR4AnLLGBk4nfsRECWCBLLW0ejGYPYguf6IuL3tnHFRe9SPZVFoSBPOce6Kd9wu34cRKxQ0YuTdtQRgJadiueNu-owtzRfqUwocUXgqFClYHEJ7UrZv4LrPLx-kZa9hRrKI62sLXDUKyPIyDhVRZjAlaESxGYsvqOAHk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حمایت تمام قد حسین خبیری از حدادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/SorkhTimes/137289" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137288">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHAQK5v9v1mnWT30IY_uyHx45frKEsNKqnx0tSAKkwnkqM_mKw8hOQWEf6y9INiP-0GyLKICbVg0B7XjM8tDfIUABdN2IiZpo12W_8xDS09vscfS7ev5WR7n1hFG-XqIqrKMvHvypSCDPgo--JYjkwzi2N2qspxnbeX4lqHaLIG5RbqYIl0Kh0a65_gS-XliT0S2fE1yO_OWbPA7XXKM6565jbnz8zVLnrBg8XWSra_pHmSlNV3P60d27WeNgJqpKY_uDEv4snQDzvdNBBIAgOj8xYrgswxynLaR4husBxrEuNHUfG5MSOmTAK9RTuZf9TilaWrr4tMN8qy9fP6JpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
فریتز در مسیر قهرمانی؛ جودار به دنبال شگفتی در فینال!
🎾
Rafael Jodar -
🎾
Taylor Fritz
🎾
تیلور فریتز با اتکا به سرویس‌های قدرتمند، ضربات فورهند سنگین و تجربه بیشتر در دیدارهای بزرگ، شانس اصلی کسب عنوان قهرمانی محسوب می‌شود. در مقابل، رافائل جودار با نمایش‌های کم‌اشتباه و روحیه جنگندگی خود نشان داده که توانایی به چالش کشیدن هر حریفی را دارد. اگر جودار بتواند ریتم بازی را برهم بزند و رالی‌ها را طولانی کند، این فینال می‌تواند بسیار نزدیک‌تر از حد انتظار دنبال شود.
📌
مسابقه را فقط تماشا نکن؛ از هر امتیازش فرصت بساز و پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137288" target="_blank">📅 20:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137287">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIk6GeMjVZLxP3HTFQqugqlTho8bsyrSjeXXBbycxXWq_-V93TBigfO7D_GN7A0z2QuLBJVgQd2SLG1ViMFjZPJbxZLSYgmghVfcq9BkOKDfd8P6uL4O6LZpBAik7Bt766qmXywooypiK8ScAtpqcBlg9ygPM2MdIQgysn7j56IuBYR8dJGcVyonYJQ-396ioy1jubyTcG_7oist_TkhICd0wbfexEYZ8CWnopy6kLOW0ZP-e2x8eqmWf-t7HGsWnmwLL6fQq0mhnKp93WFw8bDpcwBYq2fh9dLWjfaHURNYoDnPHD7t5dkXysoq7kFh2VRrPS8X7bku8V8QMxvQag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری / پایان اردوی سرخ‌پوشان در ترکیه!
❤️
تصاویر منتخب از آخرین جلسه تمرینی  ارتش سرخ در اردوی آماده‌سازی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137287" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137286">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔽
🔽
ویدیو 6 تایی شدن ارزروم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/SorkhTimes/137286" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137285">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
❌
دو باشگاه تراکتور و پرسپولیس به دنبال جذب محمد قربانی هستند، باشگاه می‌تواند این بازیکن را جذب کند که با الوحده امارات به توافق برسد.
✍️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137285" target="_blank">📅 20:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137284">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/SorkhTimes/137284" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137283">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SL9nkdd0PjYEyt4OqR9D1-l-1OzI_g0WJUkZKfYJDVajzy4vskGOTXkvYZxr-rtG2EyijU5FjpbHN9tj6D8r0o4YMKbltjtcwDYenvmN5aIX8NYfAiOK3LGQB-HlOhwYaxW7zxOYs2nYrteqtiRJhjNTmkVyfEAuzj5fb6yp1iHeH_8YyUrsz4jFMnKXpH4VCw5Lu73FJllIx6wkHF25-1t_yuNJKB6RJJuqjaQG3Mos3-dxGilwAOCGTJ3Pt-jykNFRPEF4iNrWFTjOMkApOv3GbpIZAt6mvjQFpnJffqOqrNSf3Rzi-1s19v7Ek9yVrYWIMmsg-f0QtPR5Xo8ZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاروان تیم  درحال آماده شدن برای بازگشت به ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137283" target="_blank">📅 18:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137282">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
مجتبی حسینی: پرسپولیس هیچ مذاکره‌ای با من نداشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/137282" target="_blank">📅 18:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137281">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
❌
حسین خبیری بزودی بعنوان معاون باشگاه پرسپولیس انتخاب خواهد شد
🔄
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/137281" target="_blank">📅 16:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137280">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس امروز بار دیگر در نامه ای به ملوان خواهد جذب فرهان جعفری شده است
🔴
🔴
در تماسی که خلیلی با مازیار زارع و ایجنت این بازیکن داشته تعلل در بستن قرارداد و فروش این بازیکن رو مشکلات مدیریتی ملوان و مشخص نبودن وضعیت مدیریتی برای مذاکره اعلام کردند…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/SorkhTimes/137280" target="_blank">📅 16:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137279">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
❌
حسین خبیری بزودی بعنوان معاون باشگاه پرسپولیس انتخاب خواهد شد
🔄
ایسنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/SorkhTimes/137279" target="_blank">📅 16:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137278">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🤩
🥇
تسنیم: صنعت نفت مشتری جدید امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/SorkhTimes/137278" target="_blank">📅 16:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137277">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🌹
گودرزی بعد از پیوستن به گل گهر: پنجره استقلال بسته بود؛ شرایط پرسپولیس مهیا نبود.
⏺
از استقلال و پرسپولیس پیشنهاد داشتم اما استقلال پنجره نقل‌وانتقالاتی‌اش بسته بود و پرسپولیس هم شرایطی که مدنظر بود را نداشت. در نهایت گل‌گهر را انتخاب کردم چرا که هم با مهدی رحمتی کار کرده‌ام و هم گل‌گهر تیمی بسیار خوب، ریشه‌دار و آسیایی است.
⏺
یکی از دلایلی که واقعاً گل‌گهر را انتخاب کردم، حضور مهدی رحمتی بود. خیلی دوست داشتم دوباره با او کار کنم و او هم شناخت خیلی خوبی از من دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/SorkhTimes/137277" target="_blank">📅 16:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137276">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔹
🔹
🔹
نتایج پرسپولیس زیرنظر تارتار
👀
13 گل زده و 0 گل خورده
🔥
🔴
پرسپولیس 3-0 شهدای رزکان
🔴
پرسپولیس 2-0 خیبر خرم‌آباد
🔴
پرسپولیس 1-0 آلانیا اسپور
🔴
پرسپولیس 1-0 پیرامیدز مصر
🔴
پرسپولیس 6-0 ارزروم اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/137276" target="_blank">📅 15:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137275">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
❌
دو باشگاه تراکتور و پرسپولیس به دنبال جذب محمد قربانی هستند، باشگاه می‌تواند این بازیکن را جذب کند که با الوحده امارات به توافق برسد.
✍️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/137275" target="_blank">📅 15:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137274">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
🔴
شنبه بازی دوستانه داریم،پرسپولیس و آلومینیوم
قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/137274" target="_blank">📅 15:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137273">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری؛ رامین رضاییان چند پست خود با پیراهن پرسپولیس را از آرشیو پیچ اینستاگرامش خارج کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/SorkhTimes/137273" target="_blank">📅 15:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137272">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtrtXl6n24uWOQS17jZvWQVfmsnHDXWgauzTKjvqX34XTzbVj-Lr3VOBe2TgmoRNjepF6olTpcRB_Xor53fdnj9I62MqcYhwp46RzegSQvPJt39_lmshDBxJyJoHVgpw5ZntvIy5ZrVNIX72HQByaG8XPjeawms6k3GgJKu8ip3Glfxu3bLwQXMr7bUmUyn8YB84VVOKE7bW0p-o8VOVweyRC1PsH2OVKIXe0XaBb2uuCVT7Bqotgt0eTBVhy-V4XjfuisyUrkQqEYzoQYtEdC3cH12pxnBCCX263cCSx5hssRaNKSWrfwpmbWHcIWuNX-Pl5sAfqkBIkvZFz7HQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
👀
بازگشا سخنگوی باشگاه پرسپولیس: در حال حاضر باشگاه پرسپولیس برنامه ای برای تغییرات احتمالی در کادر مدیریتی خود ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/137272" target="_blank">📅 15:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137271">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
محسن خلیلی از سمت خودش در معاونت ورزشی باشگاه کنار گذاشته شد و به زودی جانشین او مشخص خواهد شد //فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/137271" target="_blank">📅 15:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137269">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
فوری؛ رامین رضاییان چند پست خود با پیراهن پرسپولیس را از آرشیو پیچ اینستاگرامش خارج کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137269" target="_blank">📅 15:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137268">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/137268" target="_blank">📅 15:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137267">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
باشگاه پرسپولیس با وجود باکیچ ، خدابنده لو و پویا پورعلی گفته نیازی به جذب هافبک شماره 10 یا شماره 8 نداره و بدین ترتیب حضور محمد جواد حسین نژاد در پرسپولیس منتفی شد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes…</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/SorkhTimes/137267" target="_blank">📅 15:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137266">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
فووووری 360: رضاییان از کیسه جدا شد
🚨
🚨
با توجه به حضور صالح حردانی و سامان تورانیان، سهراب بختیاری زاده با برگشت رضاییان مخالفت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137266" target="_blank">📅 13:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137264">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
قربانی چند تا استوری بچهای پرسپولیسی که تگش کرده بودن و درخواست کرده بودن بیاد پرسپولیس رو لایک کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137264" target="_blank">📅 13:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137262">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4uGF70YF9Oecv0EpZdJp1tuIxxvS-8pJ8Gv0pFGOMU0SpcWtbTR_fmFcpDz6lZgpiqwGMZAo31xYmQJ_fXlkACu1rK1LuDfirbAgjbbIUkJMEfdqAo0I6JjvEi1Clh4InrqWv_RN2vUJF07YEHtw2edrOl524UVPjRT_b4ZqRhSqADvTLzBZChhRlIzrP6SsRQCDaxAXTLgEIeEhW642cLq1z4WFvFipBqRMYHEoQ-9uZ_DvZslrHz7enI6OjNltG7MRNYJOtI9TU-xOOS7G92c6NJawSSsv-JJju84ULiQmBEoreCbAgYhdSj12ewUKSu7KMUvwvgzSE78EwP03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➕
دسترسی سریع و مستقیم به اسپورت‌نود
🔗
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
🔗
این دسترسی از طریق ربات رسمی اسپورت‌نود انجام می‌شود:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
-
مزیت روش ورود از طریق ربات:
👇
• ورود مستقیم به سایت
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/SorkhTimes/137262" target="_blank">📅 13:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137261">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚡️
⚡️
⚡️
مهدی گودرزی، هافبک ۲۲ ساله خیبر، با گل‌گهر به توافق نهایی رسیده. این در حالی است که چند روزی شایعه حضورش در پرسپولیس مطرح شده بود.
🔻
🔻
آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/137261" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137260">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✅
✅
✅
پرسپولیس برای پرس و جو از مبلغ رضایت نامه محمد قربانی از باشگاه اماراتی داشته اما مشخص نیست جذب میشه یا ن/ قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/SorkhTimes/137260" target="_blank">📅 10:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137259">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
🔴
کادرفنی خواهان جذب یه هافبک بازیسازه درحالی که هوادارا برای جذب محمد قربانی فشار میارن
🗣
🗣
باشگاه هنوز روی جذبش به نتیجه گیری نرسیده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/SorkhTimes/137259" target="_blank">📅 10:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137258">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
پوریا لطیفی فر با بیش از ده درگیری موفق در وسط زمین و هیچ پاس اشتباهی حضور مثبت و قانع کننده ای از خودش نشون داد همینجور ادامه بده پسر
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/SorkhTimes/137258" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
🔴
🔴
🔴
پلن های پرسپولیس برای گلر دوم:
🔴
موندن امیررضا رفیعی
🔴
جذب احمد گوهری(سهمیه لیگ برتری )
🔴
جذب امیر عابدزاده
🔴
گندمی گلر دوم فصل بعد باشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/137257" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❌
❌
فوری
✔️
فرهان جعفری نتونست کسری خدمت بگیره و تا بهمن ماه یعنی پایان نیم فصل در ملوان موندنی شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137256" target="_blank">📅 09:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137255">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
به‌به بازوبند‌ کاپیتانی‌ رو ببین چه بهش میاد
©
🕶
🔥
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137255" target="_blank">📅 08:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137254">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5n3DeEk7vJBaEKIHg0Kkq_BKu7F30UjOQgSkuhumbuBW_kx4PLPNwhPFaYAGSFvgrdymzi5aqFSUZc2J7iy9hWcsJMUrnHXuuu4SCY6K5N63RMAwVySBTyJp6kMcDJXacbR67AOXYnsHAHVqxplU56I6wOviFvpFWloX803kAyfqD3P2FkTDpL9lbE-G-Av83etcZdIV05zGmE9fa0K5ZzssEgtcUFOOJWvN2hOGI92pRf-webPt7CGfOVZOl_FWkX64rElZ5ofEXzdnmlav-LdBl8Y-dBTkuUv7ThbQwgTEfilQ-DD4Zz1rok2Fja9y41HuuXgx-2solq9sx6MzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137254" target="_blank">📅 08:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137253">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDYI7aquUDqUntaspa3twKoQBRIjeDBtILU3ER7LSFvvccHGFPXBPftG7tj0MbMtJ0wmjWetUztumuH-4q-THF4XQGMC4PUcEcXFBPDNDqiN6Fb0KL9XCUNAcLKNjTHt_qmk3G_Ku37zQZ1IiQExYFD26xzcBcT2cvglXU9XTD1ddh2ShHJ2pcsZSGh52zFGfxfG0nBjsxQPDn7-ya4kr6sCs8ifU7ucLuw5U-rI9wa38KlzFhQs9maV-2RQ4_PAVXwN2Fi70Jc9el72V7Twootx22veqyt_ANZl7nJOxxUk9TpnO51X56sdxYCMMSc6NLfW7z521mxC8NbEZTAg4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
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
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/SorkhTimes/137253" target="_blank">📅 01:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137252">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
🚨
طبق گزارشات اکثر سرورا و vpn های رایگان از کار افتادن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137252" target="_blank">📅 01:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137251">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
تکمیلی :قدوسی : تارتار گفته بیفوما و گرا برن و سرگیف بمونه اما خلیلی میخواد سرگیف ملی پوش رو رد کنه تا گرا و بیفوما بمونن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137251" target="_blank">📅 01:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137250">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
طبق گزارشات، اینترنت ایران امشب خیلی ضعیف بوده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/SorkhTimes/137250" target="_blank">📅 00:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137249">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
فوری به نقل از منابع داخلی ؛  اینترنت بین الملل به شدت ضعیف شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/SorkhTimes/137249" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137248">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
پرسپولیس دو دیدار دوستانه دیگر را تا 24 مرداد خواهد داشت. در اردوی ترکیه برابر ارزروم اسپور و در ایران مقابل فجرسپاسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137248" target="_blank">📅 00:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137247">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔽
🔽
🔽
ایری یک قدم دیگر به پرسپولیس نزدیک شد/مذاکره نساجی با جرجانی
🔽
🔽
نساجی با درخواست مجتبی حسینی مذاکراتش را با یاسین جرجانی آغاز کرده
🔽
🔽
بنظر میرسه کار انتقال ایری به پرسپولیس در آستانه نهایی شدن چون نساجی علاوه بر جذب جرجانی چهار دفاع وسط دیگر هم داره
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/SorkhTimes/137247" target="_blank">📅 00:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137246">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⚪️
⚪️
⚪️
⚪️
شنیده ها: استعلام اولیه باشگاه پرسپولیس از فیفا درباره جذب دانیال ایری مثبت بوده و مانعی برای انتقال نیست اما پرسپولیس برای اطمینان بیشتر، یک استعلام دیگر هم گرفته تا تکلیف نهایی مشخص شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/SorkhTimes/137246" target="_blank">📅 23:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137245">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
ورزش سه: دانیال ایری درخواست جدایی از نساجی رو داده و باشگاه نساجی هم قصد فروش این بازیکن رو داره و اگه اتفاق خاصی رخ نده ایری پس از کش و قوس های فراوان پرسپولیسی میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/137245" target="_blank">📅 23:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137244">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
🔴
کادرفنی خواهان جذب یه هافبک بازیسازه درحالی که هوادارا برای جذب محمد قربانی فشار میارن
🗣
🗣
باشگاه هنوز روی جذبش به نتیجه گیری نرسیده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/137244" target="_blank">📅 23:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137243">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
✅
✅
فوووووووووری
🚨
انتقال ابوالفضل رزاق پور به پرسپولیس به طور کامل کنسل شد/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/137243" target="_blank">📅 23:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137242">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‼️
‼️
نمودار ترسناک و فوق العاده غم انگیز... کمترین میزان ازدواج در ۳۰سال اخیر  و کمترین میزان زاد و ولد در ۷۰سال اخیر! سلامی تلخ به پیری جمعیت باید کرد... از هرایرانی بپرسید علت این فاجعه را چشم بسته عاملش را "اقتصاد فاجعه بار" خواهند نامید.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/137242" target="_blank">📅 23:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137241">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
❌
❌
رزاق‌پور رسماً و شرعاً منتفی شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/137241" target="_blank">📅 23:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137240">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔹
🔹
🔹
نتایج پرسپولیس زیرنظر تارتار
👀
13 گل زده و 0 گل خورده
🔥
🔴
پرسپولیس 3-0 شهدای رزکان
🔴
پرسپولیس 2-0 خیبر خرم‌آباد
🔴
پرسپولیس 1-0 آلانیا اسپور
🔴
پرسپولیس 1-0 پیرامیدز مصر
🔴
پرسپولیس 6-0 ارزروم اسپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/137240" target="_blank">📅 23:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137239">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyTL8i4fkudgC9o-D32YdN_fX8Wb4QhErg7u7iTmtqSA6g0AZlXMt-7zAieqMwz-hdr30oPqsrUrhLDGjoU2hHZqtr8fSy4gn97l3V4z2gW3mk9ObmZtIEh90mfSeRWZzGlHDXzaBY0TRciyKfeG9J3X6SRaYPSRg_n8UG33yfwZqYxYTZFCEcCWcf7A1YHxQDkwjscLEcm1OEY0pZlLJBya_JQIyeOsnLfXvFi_HZ4HEMVpdNIii6q1xjXxvttRbowz9cJ1maWvTP7aIdhbDsZ3boIZs3KyQ61BMuSQTkde2P777BXWMaJjmJELP2WR27f3EpM488UFK7CzxmvlQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
منهای ورزش
❌
بعد از هشت ماه نرفتن بچه ها به مدرسه
❌
فوری : مدارس امسال از مهر باز نمیشن!
❌
+ عمران عباسی، عضو کمیسیون آموزش مجلس:
❌
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
❌
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/SorkhTimes/137239" target="_blank">📅 23:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137238">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBJkb8HaHtOEe3JbTDFZzrcbvv321LkZ1qW_nPpn_ioRsDNWsnFfuK32EIM-cTF-8cY_0rIkeK9-LBV_F35-Tufkw0PDN0bKQihkQ0YI8VUN16J-J9GyM1c68P0tWDckYJ2hcRNJtVr6FEM2EG2DjRd2ql302PPtkw3_u8-CTc8XqJZSC5GvnwgDdS3VtzdLXGcZzmd_t6StHHlCwqXa8k66GhdgXXhkqWUpCAWPPE9LvkEbEzl7ZInpPbp5VcFIMJfy74PnOoFdB7DU9vL2TQ9Q2yyi17G2kOPBlceU-jhLaE6W_XPDtckYBTmuP2G1NXT517vreL0nb2v34bZLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
لهستان قهرمان لیگ ملتهای والیبال شد
🔴
لهستان  مقابل آمریکا 3 بر2  به پیروزی رسید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/137238" target="_blank">📅 22:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137237">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIF6qxPCrwY1bLs4Me6YYSEh1ck7ll9NUcp4IwcDdaoxPI17GiE_-KS13ypRKjtT7bsky7YLBFHo70YVWCJmcwqvbeSVLZbo0DAZVKkpuEADyRNoNHSGIYcgd0c6KFAwXSsSdlSVzRrPn6xbRmz1rkMEGurvwlh5bWJ3X3urJKW4Xif1Hgy_RtwldXabXk7L2DQqSzNJNx0ebJXFrwHIFAamqXcZC1r3FX4Y2SwW8Htkq7T8LCaYhEzrY1PklsbfBRwqnhMzrZ8jLjfQGc9CQ2FVmDagqiukl3bImQWODZXCnsOm1yDkeM7LYXaatu2FFXCZGHSjVRvHQ51BRCA6Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎾
فینالِ نسل‌ها؛ فریتز در اندیشه جام، جودار در سودای تاریخ‌سازی،
فریتز و جودار برای فتح جام مقابل هم می‌جنگند!
🎾
رقابت رافائل جودار
🇪🇸
-
🎾
تیلور فریتز رو با آپشن‌های مختلف و بدون خارج شدن از تلگرام همراه با
ربات اسپورت‌نود
پیش‌بینی کنید.
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
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/SorkhTimes/137237" target="_blank">📅 22:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137236">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
❌
رزاق‌پور رسماً و شرعاً منتفی شد/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/137236" target="_blank">📅 21:45 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
