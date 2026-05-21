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
<img src="https://cdn4.telesco.pe/file/aziROfLZfeX-RoXJqRolqZOoYeYQVUHx5pY0S8g7epBjBJ5WOZC-sFdm435qJvVzjihMOjy3RPWgQ4OBLxvu_PWoM2JM3xb_BIDV0H2XSJXjnlsiFLIc7rMWNd8NUPbO0JoOU1IJXIbirslyyPlehFy5ktCD0hpDbvtTlxHD9k6bWOnSPhfDhDEWbfDGe6Qd7x6_4LtGgGIKIFT19PgCCiVV76gehBs1bKC45ts8FWtxDJdtuLaVtnYmCvhjPiJTu9hw7aPzJusFR1UgDb1rNbiLKm8dBy5S49IsiHWYGoiboexMsnmmuS05UKevH3eAqbGuYUfcCmNB3hr0swiPIA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.8K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 14:03:13</div>
<hr>

<div class="tg-post" id="msg-131978">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcYtpprGjmC7ikYIPYkjos4uIDP5Wr8cEEQpTQlZOom-dPuKIvNvrynMKjIAxaLA0NPoktqekgTZHEFfyVK7XgblwQGWg8p1S_w68sPL_VBIOMltL6R32RoQAzt7yI-mMe48-3DokOaq8eJMSXXCOHNq3wxlYAecvIgijfobljAjZsEv4npxy65qwRZybuhceupNE46NryVZrUnCn0QApVbSGdsNx06m0mJoVbWshvJXbOVF21VyDPi_d27dxo5UOqPDY2DtHjBeovWYHaSmiR7dV9kT5wy245EmSJ0jNUhv9CEkGdXx3YOOt2sOG8elgURnTbo1LswUJ_Asm7pwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رفیعی دروازه بان پرسپولیس و همسرش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 363 · <a href="https://t.me/SorkhTimes/131978" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131977">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔵
سهراب بختیاری‌زاده: پرسپولیس عادت به فساد کرده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 365 · <a href="https://t.me/SorkhTimes/131977" target="_blank">📅 12:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131976">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 469 · <a href="https://t.me/SorkhTimes/131976" target="_blank">📅 11:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131975">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
رونمایی از لیست ۶۰ نفره قلعه‌نویی برای جام جهانی ۲۰۲۶؛ غیبت قطعی احمد نوراللهی
👀
امیر قلعه‌نویی در حالی لیست اولیه‌اش برای جام جهانی ۲۰۲۶ را تنظیم کرده که مشخصاً نام یک چهره در این فهرست به چشم نمی‌خورد؛ احمد نوراللهی!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 579 · <a href="https://t.me/SorkhTimes/131975" target="_blank">📅 10:56 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 569 · <a href="https://t.me/SorkhTimes/131974" target="_blank">📅 10:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏅
باشگاه پرسپولیس هزینه کامل دادرسی پرونده شکایت از بیرانوند را به CAS واریز کرد
⏺
باشگاه پرسپولیس که پیش از این بابت پرونده علیرضا بیرانوند دروازه‌بان تراکتور به دادگاه عالی ورزش شکایت کرده بود برای اینکه این دادگاه رای نهایی را صادر کند هزینه‌های دادرسی را…</div>
<div class="tg-footer">👁️ 601 · <a href="https://t.me/SorkhTimes/131973" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaswRZ6vUQaGyhH8ICzIvBAASninXNguoSK7GcVgUg4qjay8QK0JOBQDo41eiRDUY5pAtxqL212o8tWGyg5sOnZaBkpLzC4idlUQE3oz5_66Nurn_Q3kbykyH7EP5lVF4ulAbTOqJdH-QpHlw8vcFisVHJ9EdK_hJQHS6XBhmwCvpnJSe2w_mTgfnnehVmUyupihYs1OL-8dj2nmakSonGNk4ZRe6B8zceqE40-4vGXr4nEYCi7LtwU11lIdJoUXJO_EY75J5VBs-CJK61-_7RHC11ZfPPTXyhcX5H5yV9-Bv1xZKsrf4MoRsz2332ZApP2662QSPHJHJsC0Tf3VHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
واکنش باشگاه سپاهان به باشگاه هایی که با بازیکنان این تیم مذاکره کرده اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/SorkhTimes/131972" target="_blank">📅 10:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131971">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 581 · <a href="https://t.me/SorkhTimes/131971" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131970">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❗️
فوری/  عضو کمیسیون امنیت ملی مجلس:  عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 570 · <a href="https://t.me/SorkhTimes/131970" target="_blank">📅 10:37 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131969">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
| فرهیختگان:
✅
باشگاه پرسپولیس با باشگاه سپاهان سر مبلغ قرارداد مهدی لیموچی به توافق نرسیدند و خود مهدی  نیز دوست دارد فصل بعد در سپاهان توپ بزند چون احتمال آسیایی شدن این تیم بیشتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/131969" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131968">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131968" target="_blank">📅 00:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131967">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/SorkhTimes/131967" target="_blank">📅 00:04 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131966">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
#فوری | آکسیوس:
🔻
یک منبع آمریکایی گفت ترامپ به نتانیاهو گفته است که میانجی‌ها در حال کار بر روی یک «توافقنامه» هستند که هم ایالات متحده و هم ایران آن را امضا خواهند کرد تا رسماً به جنگ پایان دهند و یک دوره ۳۰ روزه مذاکره در مورد مسائلی مانند برنامه هسته‌ای…</div>
<div class="tg-footer">👁️ 979 · <a href="https://t.me/SorkhTimes/131966" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131965">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای…</div>
<div class="tg-footer">👁️ 972 · <a href="https://t.me/SorkhTimes/131965" target="_blank">📅 23:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131964">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">❗️
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
🔴
چند روزی منتظر پاسخ ایران خواهیم ماند.
🔴
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
🔴
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای…</div>
<div class="tg-footer">👁️ 944 · <a href="https://t.me/SorkhTimes/131964" target="_blank">📅 23:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
‏
ترامپ: اگر توافق امضا نشود، ایران این آخر هفته برق نخواهد داشت
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131963" target="_blank">📅 23:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131961">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
سرخپوشان نمی‌خواهند خسارت بدهند
✅
پرسپولیس به‌دنبال تنظیم دفاعیه برای شکایت اوریه
✅
فرهیختگان: سرژ اوریه یکی از خریدهای عجیب باشگاه پرسپولیس در بازار نقل و انتقالات تابستانی بود. در واقع همان مقطعی که رضا درویش بابت خرید اوریه در رسانه‌ها از بهترین خرید…</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/131961" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131960">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 911 · <a href="https://t.me/SorkhTimes/131960" target="_blank">📅 22:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131959">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
🚨
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه  علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه  احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی  سامان قدوس، روزبه…</div>
<div class="tg-footer">👁️ 879 · <a href="https://t.me/SorkhTimes/131959" target="_blank">📅 22:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131958">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تأیید محکومیت 15 میلیاردی شمس آذر در ماجرای فخریان
🔴
کمیته استیناف فدراسیون فوتبال رأی محکومیت باشگاه شمس آذر قزوین در پرونده انتقال مجتبی فخریان به پرسپولیس را تأیید کرد و به این ترتیب باشگاه قزوینی باید این مبلغ را به پرسپولیس بازگرداند.
🔴
باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 839 · <a href="https://t.me/SorkhTimes/131958" target="_blank">📅 22:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131957">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
🚨
🚨
#فوری | ترامپ:
🔻
همه چیز تمام شد. تنها سوال این است که آیا ما می رویم و آن را تمام می کنیم، یا آنها قرار است سندی را امضا کنند؟ ببینیم چه اتفاقی می افتد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/SorkhTimes/131957" target="_blank">📅 22:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131956">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عاصم منیر فردا به تهران می‌رود احتمالا خبر مهمی در راه است
🔴
روزنامه ابزرور پاکستان: فیلد مارشال سید عاصم منیر، رئیس ستاد ارتش، به عنوان چهره‌ای کلیدی در روند دیپلماتیک ایران و آمریکا، فردا به ایران می‌رود. در طول این سفر احتمالی، انتظار می‌رود اعلامیه‌ای مبنی بر تأیید تکمیل پیش‌نویس نهایی توافق منتشر شود.
🔴
این سفر می‌تواند به عنوان یک نقطه عطف دیپلماتیک سطح بالا باشد، جایی که تکمیل نسخه نهایی توافق ممکن است رسماً اعلام شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 866 · <a href="https://t.me/SorkhTimes/131956" target="_blank">📅 22:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131954">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
باشگاه پرسپولیس با مهدی لیموچی، بازیکن سپاهان وارد مذاکره شده و این بازیکن به همین علت درخواست جدایی از تیم سپاهان را ارائه کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 837 · <a href="https://t.me/SorkhTimes/131954" target="_blank">📅 22:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131953">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00eb689252.mp4?token=qo5ZKGudK-gWtxxJr9abgcZJCjf-w7EP5VgWj1lv6hQR7N9jvGv3WuQXGzu8nZ62e8dcSBrpnjWL4kFbohu0YUb2maxfCKbLMXXF8cl6OWYqOto3_C8dHsCWb6-WnlxVCIYZkTkYFMADKdf_EYEHQOAVvzT-tDkvCjVL55zOgCb0yBF8FsiKOANgPmMrOZT9Us6h9zZzLa6u1JYHLYTQ_tM2GWjxsDxx-A7-iv2DqKWBAS_c0vtUqf6giwMyT1U7kU4gXPiy22PvZyhOGX87NOgSHgkpid5U1OIJf5qwgopMtyCavnZlSuKPKImyTpU4qcvsqoOPsrI9193NiHGTWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00eb689252.mp4?token=qo5ZKGudK-gWtxxJr9abgcZJCjf-w7EP5VgWj1lv6hQR7N9jvGv3WuQXGzu8nZ62e8dcSBrpnjWL4kFbohu0YUb2maxfCKbLMXXF8cl6OWYqOto3_C8dHsCWb6-WnlxVCIYZkTkYFMADKdf_EYEHQOAVvzT-tDkvCjVL55zOgCb0yBF8FsiKOANgPmMrOZT9Us6h9zZzLa6u1JYHLYTQ_tM2GWjxsDxx-A7-iv2DqKWBAS_c0vtUqf6giwMyT1U7kU4gXPiy22PvZyhOGX87NOgSHgkpid5U1OIJf5qwgopMtyCavnZlSuKPKImyTpU4qcvsqoOPsrI9193NiHGTWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
قلعه‌نویی به نورافکن: آقای امیدخان نمیفهمی پای راسته؟ حتی اینم نمیفهمی
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 838 · <a href="https://t.me/SorkhTimes/131953" target="_blank">📅 22:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131952">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1098692638.mp4?token=UDgiXzQ2QyW4IUXyH3YIkCu1a2pN5NPNNTsmOitfEor7o53cNZxOkfk2oYYPJqLBxbz87UwlBRGYGOmceJStrDN8J0BResFgmiMAgviUyU0zNtdifbvLC138sNd7Qv0UQ4-wCRT0mJttwo88yK1DkCCkBc6lkddcA57SwpUeh5hMLo-6Umd1duv_Rjx1emRCePr2AeK8KequHrR9kr8GNEYkSOKSGLg4PLJoDPxfe5o8TQzzhFRvKe6MUQMbacAhRL6afzWwENpy-TwYXecHG8l--8oNsuEn1YD1SA61f265rHAaEy6Cbd-YTL4PNs2qQ6eyQsJO-xFae6qUEln19w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1098692638.mp4?token=UDgiXzQ2QyW4IUXyH3YIkCu1a2pN5NPNNTsmOitfEor7o53cNZxOkfk2oYYPJqLBxbz87UwlBRGYGOmceJStrDN8J0BResFgmiMAgviUyU0zNtdifbvLC138sNd7Qv0UQ4-wCRT0mJttwo88yK1DkCCkBc6lkddcA57SwpUeh5hMLo-6Umd1duv_Rjx1emRCePr2AeK8KequHrR9kr8GNEYkSOKSGLg4PLJoDPxfe5o8TQzzhFRvKe6MUQMbacAhRL6afzWwENpy-TwYXecHG8l--8oNsuEn1YD1SA61f265rHAaEy6Cbd-YTL4PNs2qQ6eyQsJO-xFae6qUEln19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
#فوری
| ادعای آکسیوس:
🔻
قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/SorkhTimes/131952" target="_blank">📅 22:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131951">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
ورزش سه: روزبه چشمی از ناحیه رباط صلیبی مصدوم شد و جام جهانی رو از دست داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 858 · <a href="https://t.me/SorkhTimes/131951" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131950">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsoiS7AlgWht_WA6KkjgzszLaF7sevmYK-JcleW679gULeis27t3wVkX7VC5ToU-hpSUppSz_sWgcM9E4VWSs8VBUZgn97kMHalK1uEd0B7-cR5zRvqr2uRs_ZizJsUEcqYLUPikoi7pt8z6WFPIQy-wI5hPYVRTJG_pG4CezUdw9m0bCkA5P1wL1ErcV6b42SNfnekSt_R_LNKIlkCCqsG2oJVIYyzYmBik2C-CagfobtG03HJuWX4paToN6uBLP1i7_vPRL3komv72DLEwkGhZagiXOdYvtThzdK2qd6UOfHnVIZieJABFUF5mk-ma3mlFT2epJ_gBgPutOWKHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
Final Europa League
⚫️
Freiburg -
🔵
AstonVilla
‼️
این روزا قبل از پیش‌بینی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
براحتی میتونید برای بازی فینال لیگ اروپا وارد سایت بشید و این دیدار رو پیش‌بینی کنید، واریز و برداشت هم بصورت آنی می‌باشد.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/SorkhTimes/131950" target="_blank">📅 21:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131949">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
5 گیگ 800T
10 گیگ 1.5T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 851 · <a href="https://t.me/SorkhTimes/131949" target="_blank">📅 21:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=AV-7kb7qpMla0MOe9Ope8BSyNhq3Gkf-gbza7Ed8EZkQyJsqDpdFsP9Xdh6JxLMugYfeS7-36e-vc3jmLu6JFFw7ZELRqcYn8Kf_OYSH8wQNLn_BCgo4tVV-8jEFZm8VpeveELtcZnj8jii0DZmIhqgCRAt2yJU_bCWlva3fdS0B5MiOLoCPCW43OPB0i-IHh5V3qYjF2ufUenUmUcS2qnoNX-n1pXekl3prkYoTIw9rbUIFB4NGC8n4ns8vMc9PPDQH48kEe4UO-8_P5U_OywritlgdYpbFVP6e17HfFZl3bnN0Z6oTDUbMAwTWbG2JeqPlxzW-2_lNcrzXwRrkKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/050c7fea46.mp4?token=AV-7kb7qpMla0MOe9Ope8BSyNhq3Gkf-gbza7Ed8EZkQyJsqDpdFsP9Xdh6JxLMugYfeS7-36e-vc3jmLu6JFFw7ZELRqcYn8Kf_OYSH8wQNLn_BCgo4tVV-8jEFZm8VpeveELtcZnj8jii0DZmIhqgCRAt2yJU_bCWlva3fdS0B5MiOLoCPCW43OPB0i-IHh5V3qYjF2ufUenUmUcS2qnoNX-n1pXekl3prkYoTIw9rbUIFB4NGC8n4ns8vMc9PPDQH48kEe4UO-8_P5U_OywritlgdYpbFVP6e17HfFZl3bnN0Z6oTDUbMAwTWbG2JeqPlxzW-2_lNcrzXwRrkKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
❤️
سردار دورسون: از ایران و ترکیه پیشنهاد دارم
🔴
امیدوارم صلح به ایران بازگردد
🔴
از روز اول رابطه خوبی با هاشمیان نداشتم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 976 · <a href="https://t.me/SorkhTimes/131946" target="_blank">📅 20:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1XmYDNyE4-Zxymst8hiMoDv5FYPmarL08drxkXsd50I8No5h0Gsiux8d5LtMvd8e9xfjsEKY8s9_sBqSuiAU2nG-1wsk1OY2fUW2Pjftj-PsWnoWQjYaZO4-3jq-HN38-3nupNk0qtOCpIR7vY-8sg1Vg9k6DuNUdigKn8uxPuajuldahf1j6BZkpmKI7N7azz9ykVTEJL2qF8LPvTKLew9bwiTl4JcdHQLOrJcxWzpJX7b0yVTqAqWXFJvr2LrAbgg7pHsnB0ITCEOwHcIXYC6CtfvB4-92kXEzW4DqMPqVviL2cqkdkf6SxDEei1bI3LmKBlirISusFfN6cJHgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوووووری
شبکه الحدث :
احتمالا طی ساعات آینده، متن توافق ایران و آمریکا نهایی میشه؛ دور بعدی مذاکرات هم باز تو پاکستانه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131945" target="_blank">📅 20:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔥
۲عدد سرور ۱۰ گیگ اف خورده ۱۹۰۰
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/SorkhTimes/131944" target="_blank">📅 19:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84765e9843.mp4?token=hzz2cXTIMssQsjElGZqeIBPOdJKSwbjjEd6tNA9uXbGNcxNnK7vkET6x1Z_tKfRSXcFe1dXRTq6o6H7Qs_bBuU7o4CCUV21jX7cvD0PYawg1Pug9QXHsLojVzbYngHW0qRG95D_H3uFHv9pKaMo3nXyhnuu1f9QqAqhQ_5EgJUobipjp1z1VxizF9IOH1UAwzEx3X1T2tIoHUumfnqfRp102VhrxZLNoEyAtbZFlRKedM70hrf2N6coGR8vwU-y9ClM6_-sYZdK7GZSTsNWdTfnfd6Yvt7yc07JprVCKZRi5-RNXJdr_Mek5LkYLhv2GtyNFkvDZmB3j0F-t6Y4OWDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84765e9843.mp4?token=hzz2cXTIMssQsjElGZqeIBPOdJKSwbjjEd6tNA9uXbGNcxNnK7vkET6x1Z_tKfRSXcFe1dXRTq6o6H7Qs_bBuU7o4CCUV21jX7cvD0PYawg1Pug9QXHsLojVzbYngHW0qRG95D_H3uFHv9pKaMo3nXyhnuu1f9QqAqhQ_5EgJUobipjp1z1VxizF9IOH1UAwzEx3X1T2tIoHUumfnqfRp102VhrxZLNoEyAtbZFlRKedM70hrf2N6coGR8vwU-y9ClM6_-sYZdK7GZSTsNWdTfnfd6Yvt7yc07JprVCKZRi5-RNXJdr_Mek5LkYLhv2GtyNFkvDZmB3j0F-t6Y4OWDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سردار دورسون‌ مهاجم سابق پرسپولیس مهمان امروز تمرین تیم ملی بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SorkhTimes/131943" target="_blank">📅 19:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
#تکمیلی | ترامپ:
🔻
یا با ایران به توافق می‌رسیم یا کارهای سختی انجام خواهیم داد و امیدواریم این اتفاق نیفتد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 982 · <a href="https://t.me/SorkhTimes/131942" target="_blank">📅 19:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SorkhTimes/131941" target="_blank">📅 19:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/SorkhTimes/131940" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❗️
🔻
ادعای العربیه: ممکن است طی ساعات آینده از نهایی شدن نسخه نهایی توافق بین آمریکا و ایران خبر داده شود  العربیه:
🔹
کار برای نهایی‌سازی متن توافق بین واشنگتن و تهران در حال انجام است. فرمانده ارتش پاکستان ممکن است فردا برای اعلام نسخه نهایی توافق از ایران…</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/SorkhTimes/131939" target="_blank">📅 19:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
🇺🇸
ترامپ: آمریکا در «مراحل نهایی» مذاکرات با ایرانه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 934 · <a href="https://t.me/SorkhTimes/131936" target="_blank">📅 19:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ترامپ درباره ایران: من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 869 · <a href="https://t.me/SorkhTimes/131935" target="_blank">📅 19:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWMqAVgHhBPUpM7vuFZjW8pTt6zGs_bD-vN80VNURtfWGchz-wwZpLJPInAenIXTcoxCErTKz9tOmBMz0Yymc-5SPA42wWqsSFKpctt1E6AvwPW-4_Zgd6p_czb7y827wTqdLWRouIP2kq0HEQYZlGmVZ9S8_xU5t3ukvvxhD0eDYV5PQZQ1pJN0GsVZksETWZ3yvmZqBGG6ste0932uG-9ozcwp3dNnfEO3VEmexE0s3g0MTdW2bq0sRvBhjh9sn4kkpJklAKg7fP9KngoEIn2TesGNhNn61ubrs1NscBeNlVJgyXHkJGdQEBWM5HzRzKgB_GrwMSwXQorRuqThgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
شکایت یک شرکت تبلیغاتی از باشگاه پرسپولیس در دادگاه تجدید نظر رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 902 · <a href="https://t.me/SorkhTimes/131934" target="_blank">📅 18:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJq23mlGVFw57Mn_qNkQe-Lg_h_797oNcbJ07j_JSI1GJSMGwd0kvRgAbtsJ-XplqgY083bzOCkaN7AO2HZE0NWAe6S5eNVei7MRGj3gKznMCOkLo0iBOq2nC6tixC6e4mwan5QKF3ZzjSvhg3fXQwiXLaCECK7hqLKtWZs6wKkdmpoGBxTPtt1clbrjYC15uX65AFFG3KyNs7bJ-5nG55hSd-WPZ-5nW8pJVqzLzgzr6bcsyb-UxjkCuVjmVNggWQsC76LRSyjM1G_XxdjGF3QViQ9Fk-6sISqWQWhSsLn9EaEK41WImCEOeefwZ5ETlJcDqZcCkU5mxuXzvMu4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
بازیکنان مطرح تیم ملی سعی میکنند سردار آزمون تو لحظات آخری برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 925 · <a href="https://t.me/SorkhTimes/131933" target="_blank">📅 18:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=IkiTGVXRm2w_3LB5lt9slgzPUaAMQcD10zhL0S6L7alS6q8wU0ZkBUNkMxJ2DjH3EBC9w3PSv5bnCk2bflaxWkYrCkHDPouZe-dJdbjpdJKH8qRE-_B4gXmqlY_14wIjtCkX9KOO4rDy7yeWofwDRtgoKIMcZDB7uy94tyj1GIaFdhkYuuGgmrJqCEkpb-MZc9h-sRbxI0x9r3iHBedOqVDJTTglrpW4rUj-qpwBKJslrkeyne63zFpD0IuRCcVkk8gTHbZw9NXgHz934MRi1KSIZXD4c211KGRS2XLVIvAbAyhvTIOyipW9k7L6y3HUM1HauEEUIC5YsNT8mbswnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ab8278f1.mp4?token=IkiTGVXRm2w_3LB5lt9slgzPUaAMQcD10zhL0S6L7alS6q8wU0ZkBUNkMxJ2DjH3EBC9w3PSv5bnCk2bflaxWkYrCkHDPouZe-dJdbjpdJKH8qRE-_B4gXmqlY_14wIjtCkX9KOO4rDy7yeWofwDRtgoKIMcZDB7uy94tyj1GIaFdhkYuuGgmrJqCEkpb-MZc9h-sRbxI0x9r3iHBedOqVDJTTglrpW4rUj-qpwBKJslrkeyne63zFpD0IuRCcVkk8gTHbZw9NXgHz934MRi1KSIZXD4c211KGRS2XLVIvAbAyhvTIOyipW9k7L6y3HUM1HauEEUIC5YsNT8mbswnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ورود کادرفنی تیم ملی به کمپ تمرینی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 847 · <a href="https://t.me/SorkhTimes/131932" target="_blank">📅 18:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=Fs79TCo52H6hcQdM9HJqCvHPzOElZd4FP_oXVd804avQMkqTaZjAhPtfqOOeczjGy3LWgu6eBF3DGD3XSYMjmrJhhJWgcPbr2AbOX-pjrM6xsu_yCOJdylMtYvYI8rp4kBcMTnp6lYb-OanR729MlQHnUQ8OHWz2s8cYemvj5_OtHnF6ubgycv2Egqj6sW2ilLk_S4emVWirnGhqEs04t8pvJr1rDPljE5ZDvkq20uAZ22JPqJd5nejs6QlvxSU_Rfq8ArQ0LGcnlstHMFl6hJPcWB9MRAqHbaMMDqXX-Ss2KHpeW-CWvB-xHLG_tRH8maKJJR9ZAfFfb_OSpAdmrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcc1b48df0.mp4?token=Fs79TCo52H6hcQdM9HJqCvHPzOElZd4FP_oXVd804avQMkqTaZjAhPtfqOOeczjGy3LWgu6eBF3DGD3XSYMjmrJhhJWgcPbr2AbOX-pjrM6xsu_yCOJdylMtYvYI8rp4kBcMTnp6lYb-OanR729MlQHnUQ8OHWz2s8cYemvj5_OtHnF6ubgycv2Egqj6sW2ilLk_S4emVWirnGhqEs04t8pvJr1rDPljE5ZDvkq20uAZ22JPqJd5nejs6QlvxSU_Rfq8ArQ0LGcnlstHMFl6hJPcWB9MRAqHbaMMDqXX-Ss2KHpeW-CWvB-xHLG_tRH8maKJJR9ZAfFfb_OSpAdmrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
زمین تمرینی شماره یک تایتانیک، محل تمرین امروز تیم ملی ایران
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 880 · <a href="https://t.me/SorkhTimes/131931" target="_blank">📅 18:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131930">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❗️
پاکستان متن توافقات اولیه را آماده کرده است و مذاکرات بعد از عید قربان در اسلام آباد انجام خواهد شد و تا ساعات آینده و نهایت تا فردا عاصم مونیر پایان جنگ را اعلام خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 907 · <a href="https://t.me/SorkhTimes/131930" target="_blank">📅 18:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 892 · <a href="https://t.me/SorkhTimes/131928" target="_blank">📅 18:23 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131926">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e0676b3f8e.mp4?token=BUox-Ia1Jr_zIM2Rr_HwSHbcFf45pl7B9fp8upn1ZFZsnQjCfJ4UpiwgALo7WtUghOBnieE5xoP-qn2inIMPnceX6-a9peDf3rx5Nu972wsX8g81jQXAUHd6QO_3K_HeOCQ92BCLNF1FgxcjWHVqw_i6CPCKmkrYLXtEh3X8_Opc7ysGYFsHltDz_sWOucc0XwN-zTo0ZuzefRW8iisDb-5ZTGunxL9TuqCNjb7snj_QEy9yyDRnCrwaXt1SW-Ra0ialDRe_73X8fTdUCJ5oTlI-2AvVjccLl9yLQ9yLtRBuKBv5lEOzqs2v3b9_7SzdgeaX374Rt1vDn1FNoV16Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e0676b3f8e.mp4?token=BUox-Ia1Jr_zIM2Rr_HwSHbcFf45pl7B9fp8upn1ZFZsnQjCfJ4UpiwgALo7WtUghOBnieE5xoP-qn2inIMPnceX6-a9peDf3rx5Nu972wsX8g81jQXAUHd6QO_3K_HeOCQ92BCLNF1FgxcjWHVqw_i6CPCKmkrYLXtEh3X8_Opc7ysGYFsHltDz_sWOucc0XwN-zTo0ZuzefRW8iisDb-5ZTGunxL9TuqCNjb7snj_QEy9yyDRnCrwaXt1SW-Ra0ialDRe_73X8fTdUCJ5oTlI-2AvVjccLl9yLQ9yLtRBuKBv5lEOzqs2v3b9_7SzdgeaX374Rt1vDn1FNoV16Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| رسانه‌های سعودی:
🔻
فرمانده ارتش پاکستان ممکن است فردا به ایران سفر کند تا نسخه نهایی توافق را اعلام کند. ممکن است طی ساعات آینده نسخه نهایی توافق بین آمریکا و ایران اعلام شود
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 975 · <a href="https://t.me/SorkhTimes/131926" target="_blank">📅 18:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131925">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
ترامپ درباره ایران:
من عجله‌ای ندارم، همه میگن انتخابات میان‌دوره‌ای و اینا، من برای جنگ اصلاً عجله ندارم.
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 963 · <a href="https://t.me/SorkhTimes/131925" target="_blank">📅 17:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
پژمان جمشیدی به ۹۹ ضربه شلاق محکوم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/SorkhTimes/131923" target="_blank">📅 16:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRBXm8jnraK6bOuhGddjyYWu5esb_CxjbSLjrl9ahl4Yz4W_C84Fpwq5a5VYwn_4K3X0xFu0IGP1xowUg9ygGQymzYpz7fYSjLOLR1uc6YVEC0YCZRoUupSC_42uVNqZrMsxRba4uC4fxzV-eqrqyhsDUSpRZ0b7ct-zkbqgD79TggkdD0yDriNFMAS_cfSZxajMzTNdkZz0cNwp1HiwKTlt0l5BRgpQegc43HcpvgXOZi_xu1K7KOJhZ-k2QUOUNarrV05CEHnikhNedMSpGv0jrWsCP9H0rnR8UN8_wQwD1wofFf6F3Awh9pnzYbdxtecddeYl9grOViPcjaMksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
احتمالا بخشی از اینترنت زیر ساخت ها در حال اتصال است!
❗️
بر اساس آماری که چارت های رادار کلادفلیر نمایش می دهند،
❗️
طی ساعات گذشته پهنای باند اینترنت کشور افزایش چشمگیری داشته و احتمالا این بدین معناست که اینترنت دیتا سنتر های ایرانی در حال اتصال است.
❗️
احتمالا تا ساعات آینده شاهد وصل شدن بخشی از فیلترشکن های قدیمی در داخل ایران خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131922" target="_blank">📅 16:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/SorkhTimes/131921" target="_blank">📅 15:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvpbT_TXDKNOhu2g_AV52_wcrrj4K3s4yaldGvxUl3nVQ9YMqzc4jnobjbhjo0JQIQ7-0-zTHJ4OduBgyXApFtRArqhINBDUINbWc1vw1sOKw4QMdsIUdOL2qp3-ELEP7CViH8pS7G0fytIIqHHVQ3mhMotarvTyu_uKH7RO-BAFTvYafPXswsgRRiN_OsU8pAzspM6s6MmWp_gK62F86KdI3OUBjqueLdTICXpK0LzHcuFixT6Q0CtXEx902hp07RLwgLK5Zko2kwJEXKVEHDb19ptGOD_zvjnc21OJugFBiHKSh_4jElECCf0s1Co4rFueAEI4zgMb_JDU4TL0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ادعای خبرگزاری فرهیختگان: آریا یوسفی و مهدی لیموچی در سبد خرید پرسپولیس قرار گرفته اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131920" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131919">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
فووری؛ اوستن اورنوف ستاره ازبک پرسپولیس در تمرینات تیم ملی این کشور مصدوم شده و وضعیتش برای جام جهانی نامشخص است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131919" target="_blank">📅 15:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بعد از ۷ بار تلاش سنای آمریکا، با رای ۵۰ به ۴۷ قطعنامه
اختیارات جنگ در ایران
رو تصویب کردن
این اختیارات ترامپ رو محدود میکنه البته احتمالا خود ترامپ اونو
وتو
کنه. مهم‌ترین تاثیرش اینه که دموکرات ها کم کم دارن قدرت بیشتری پیدا میکنن و برای
انتخابات
بعدی دست بالاتر رو پیدا میکنن
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 983 · <a href="https://t.me/SorkhTimes/131917" target="_blank">📅 15:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131915">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbB-wbcpJ0T7XYnpZ4La_4ZVGfRehsmW-81oNG8UPrMMIJ2oOtm14OBRkOVcsE6NauXFk_dKxsGHfN-Ki5x3J-WwY9TXZxFGYS6bKMMC3UJI6h3K0l8f4mvFd1qplnV0Vo3rz_y0TTiOF2R_DxgE8szkq_RP4q17660O0Jg7wzOUO6P3eDdNyjasY0jGt6ib17Jon67GxwLebrXdtPj5anR36RXqRdrEStnC5Y_2KM5DEUU3vtqGETMGPama8tP9Xid4rIIdPQ1QfgicO9kAoKLKqpBNaVErt60HVOnAlMxdmDt0imfJTWtFMHQLHEEud75O2DDpAGxXWDRzqnsmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش مدیر رسانه ای باشگاه
😂
👌
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 960 · <a href="https://t.me/SorkhTimes/131915" target="_blank">📅 12:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131914">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5EmXBs3gl_K7-zpca-cfHD2jhkeL4BuepHV2fPFwSCVu570Vppz7PJcBIT17PpViTQtMX2WOyykxdSSX2iawl9mUdUu_-mCIbRYjSehHNsbQh12S9b39aGbhu9jBLjEpoobIlCCJo6uBUt2_o3Vo_SzqtdEcMiww7L_Orf1EXeyJUSonJ-91STMmMxLGo8odrKARs6EgPzXPgSu42ahWgp2k_G-YL-tSx8-qSLwuSeJ27DHx3z1r0R7VYCFjcijZeyOmYgKuMpHZalvRLjPdi174uQk4g0xmPMvz9XOSKOvt4tkMfgQJWpfzJOImvPUxoY-3bmGLLmiMP_vIG0VmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این روزا قبل از شرط‌بندی بیشتر از خود بازی باید نگران این باشی که VPN وصل میشه یا نه.
😀
ربات تلگرام وینکوبت دقیقاً برای همین شرایط خوبه چون کل سایت داخل خود تلگرام اجرا میشه و دیگه لازم نیست هی بین سایت و VPN درگیرشی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
میتونی مستقیم وارد بازی‌ها و کازینو شی، پیش‌بینی ثبت کنی، واریز و برداشت انجام بدی و همه‌چی خیلی سریع‌تر و راحت‌تر انجام میشه.
🟣
آدرس دائمی سایت:
wincobet.com
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 998 · <a href="https://t.me/SorkhTimes/131914" target="_blank">📅 12:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131913">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131913" target="_blank">📅 12:08 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131912">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">محمد پروین، فرزند علی پروین:   پدرم به دلیل زخم پا (به علت دیابت) در بیمارستان بستری شده است، اما مشکل خاصی ندارد و به زودی مرخص می‌شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 959 · <a href="https://t.me/SorkhTimes/131912" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131911">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRFcDmtKP-bC7jGMM9suFWgv9u0XXMd9PrnzJZgjBVHKy4cPKrpw6OdO-MPUduMAYjpkssXaITOt1ivMPXPgwmJ3zlxxxoA1gxq7THj-2xQee6TK238Qh3omfNiq11Zod2_QBNED3mMogkZwNNKswmyP938LvFnNRs3oEE_8Pz82GT_KRymfO7EJWnmRngOxsSN3Rq6O88raK62vKPHZs5Lpk5JTaWatiHM7Lk79sZwZPw36Feqhvlsv4FOmJkZhDPp-HImprlBDn-p7afMQNpVv_wWm_1hW-GXGK9bIoK4-OlUG2VKxsZTLRdE7DC21QV_EPQiSkDIYO_-jcjroPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک تایمز :
🔴
فیفا قصد دارد دوباره ورود پرچم «شیر و خورشید» ایران پیش از انقلاب و لباس‌های مرتبط با آن را به ورزشگاه‌های جام جهانی ۲۰۲۶ ممنوع کند. این پرچم در جام جهانی ۲۰۲۲ قطر هم محدود شده بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 931 · <a href="https://t.me/SorkhTimes/131911" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131910">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
شایعه حضور تارتار روی نیمکت پرسپولیس از کجا آب می‌خورد؟
💸
یک دلال با سوءاستفاده از شرایط جنگی و شایعات درباره بازنگشتن خارجی‌ها ، پیشنهاد داد در صورت نیامدن اوسمار ، تارتار سرمربی پرسپولیس شود.
⛔️
این پیشنهاد جدی گرفته نشد و مدیران پرسپولیس قصد دارند همکاری…</div>
<div class="tg-footer">👁️ 989 · <a href="https://t.me/SorkhTimes/131910" target="_blank">📅 10:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
ونس معاون اول رئیس‌ جمهور در مصاحبه جديد خود اعلام کرد اصلا متوجه نمیشم مقامات رژیم ایران چه میگویند یا چه چیز میخواهند فهمیدن حرف هایشان واقعا سخت است و مدام حرف ها و خواسته هایشان تغییر میکند و نميتوانند به یك تصمیم واحد برسند ، اون 440 کیلو اورانیوم باید…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SorkhTimes/131909" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
قاتل الهه حسین زاده با اذان صبح فردا اعدام می‌شود.
❗️
استوری خواهر الهه: امشب، قصاص مرهم داغ خواهرم نمی شود... اما شاید کمی از بی عدالتی این دنیا کم کند. الهه جانم...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131908" target="_blank">📅 10:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">●
بدترین حس وقتیه که میخوای سریع وارد سایت شی، بازی شروع شده، ولی VPN وصل نمیشه یا سایت نصفه لود میشه.
😑
● برای همین
ربات تلگرام وینکوبت
این روزا خیلی کاربردیه چون کل فضای سایتو داخل خود تلگرام میاره و عملاً بدون دردسر میتونی مستقیم وارد بازی‌ها و کازینو شی:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131906" target="_blank">📅 00:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131904">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
#فارس مدعی شد ؛ مدیرای پرسپولیس اصراری به موندن علیپور ندارن و اگر اوسمار هم بگه نمیخوام قرارداد علیپور تمدید نمیشه.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131904" target="_blank">📅 23:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131903">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⚪️
مهدی تاج: اگر پرچمی به جز پرچم جمهوری اسلامی وارد استادیوم شود به آمریکا نخواهیم رفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.13K · <a href="https://t.me/SorkhTimes/131903" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131902">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
⭕️
🔴
حضور حسین کنعانی زادگان و رضا درویش در منزل خانواده زنده یاد الهه حسین‌نژاد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131902" target="_blank">📅 23:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131901">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚖
پژمان جمشیدی تو جلسه دادگاهی امروزش: «من قسم میخورم که هیچکاری نکردم و این اتهام درست نیست. من با این دختر کاری نکردم و اصلا بهش دست هم نزدم. به روح مادرم قسم میخورم که من کاری باهاش نکردم.»
◽️
وکیلش هم گفت ادله و مستنداتی به دادگاه ارائه دادیم که بی‌گناهی…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131901" target="_blank">📅 23:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131900">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.05K · <a href="https://t.me/SorkhTimes/131900" target="_blank">📅 22:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131899">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 951 · <a href="https://t.me/SorkhTimes/131899" target="_blank">📅 22:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131898">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=aXmJlb-9z_SebO5K6EvSjszjOwU9a1T8LYNBH-ELWNtcBnQNh_owozPgnjge0XzmTZZ3chCbwDzAPJN7Hnt7VnEppi8tVb47tfHQKOzN_UMlXJUdbBFxVmEK2Rw3hRxZ359M-BVy__n8aZzDCkklG8Hnnx7-E-Zh2fSD0m1qEnQZB-uU_SnPxp9P_kyQaMf930gOUO55pWqXYeyd-_lJkcta93kgrS7w2qicRkmxjii4k7Ak5Se2Y4M3kSViG81qwRzZuIWDs4Q_8NL2RddQH7s76RRDtAPYl-PXnj8Y0jK5LOkXWbwTBAxKN5RTzNEO8umgQv-YHY_e6VxLiqFTkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=aXmJlb-9z_SebO5K6EvSjszjOwU9a1T8LYNBH-ELWNtcBnQNh_owozPgnjge0XzmTZZ3chCbwDzAPJN7Hnt7VnEppi8tVb47tfHQKOzN_UMlXJUdbBFxVmEK2Rw3hRxZ359M-BVy__n8aZzDCkklG8Hnnx7-E-Zh2fSD0m1qEnQZB-uU_SnPxp9P_kyQaMf930gOUO55pWqXYeyd-_lJkcta93kgrS7w2qicRkmxjii4k7Ak5Se2Y4M3kSViG81qwRzZuIWDs4Q_8NL2RddQH7s76RRDtAPYl-PXnj8Y0jK5LOkXWbwTBAxKN5RTzNEO8umgQv-YHY_e6VxLiqFTkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
مزخرفات خنده دار سهراب بختیاری زاده سرمربی کیسه: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 981 · <a href="https://t.me/SorkhTimes/131898" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131897">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
باشگاه پرسپولیس: ما میگیم لیگ برگزار بشه ولی ما رو نادیده میگیرن، اونوقت تیم‌هایی که میگن لیگ کنسل بشه، معرفی میشن واسه آسیا. نمایندگان ایران تو آسیا باید با عدالت و در زمین فوتبال معلوم بشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 940 · <a href="https://t.me/SorkhTimes/131897" target="_blank">📅 22:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131896">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
💢
بیرانوند از جام جهانی محروم نمی‌شود
💢
رسول باختر، حقوقدان ورزشی در گفت‌وگو با ایسنا: در رای استیناف آمده بود که محرومیت بیرانوند شامل مرحله نهایی مسابقات بین المللی در تیم ملی نیست.
💢
با توجه به این موضوع، حتی در صورت صدور رای CAS پیش از جام جهانی، بیرانوند…</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/SorkhTimes/131896" target="_blank">📅 22:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131895">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
نصیرزاده، وکیل علیرضا بیرانوند: در صورتی که حتی رای محرومیت ۴ ماهه این دروازه‌بان توسط دادگاه CAS تایید شود، محرومیت وی شامل جام جهانی نخواهد شد.
⏺
به محض اینکه هزینه دادرسی واریز شود، رای صادر نمی‌شود. تا بخواهند رای را صادر کنند جام جهانی تمام شده است.…</div>
<div class="tg-footer">👁️ 917 · <a href="https://t.me/SorkhTimes/131895" target="_blank">📅 22:03 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131894">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❗️
پرسپولیس شاکی از بمب درویش/ حدادی: اجازه دهید دلایل را نگویم!
🔴
مناقشه باشگاه پرسپولیس با سرژ اوریه، مدافع سابق این تیم، وارد مرحله جدیدی شده و این باشگاه رسماً علیه بازیکن ساحل عاجی خود شکایت کرده است. پیمان حدادی، مدیرعامل پرسپولیس، با اعلام این خبر، ابراز…</div>
<div class="tg-footer">👁️ 984 · <a href="https://t.me/SorkhTimes/131894" target="_blank">📅 22:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131893">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/131893" target="_blank">📅 21:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131892">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=Tk84K3XAswzZbmGBkfFkp3tOseCrup_isI_-Sy49uL8MbE38e0F2pbCCRyMSI18XNMIQhQJLw4KFr25CVFUXDZx57VoaZSymFNjYXltYIdrCBH0uDKhnVAfqncceJQJI8g5NEiFvDgZZyWUBMqNBv9uQNoUAXTyU5Nw3Ik6kfR3ux58ZwMKJpwOryN2PGr0mdBRovmL_Umte0NV5QGxMcsgh0q_MmOy8rG1ZQJC-Mqcgo7e2fkeXE6jzPTQ9FLR4ANVVgvKSjSZU01eKsIL4c4I-drv5MfmHmkcUFWUxLYnABpHgNWS0hRdwpLSls0AF9p31jdFsQ7Bnt1P-ICn3rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773afe10e.mp4?token=Tk84K3XAswzZbmGBkfFkp3tOseCrup_isI_-Sy49uL8MbE38e0F2pbCCRyMSI18XNMIQhQJLw4KFr25CVFUXDZx57VoaZSymFNjYXltYIdrCBH0uDKhnVAfqncceJQJI8g5NEiFvDgZZyWUBMqNBv9uQNoUAXTyU5Nw3Ik6kfR3ux58ZwMKJpwOryN2PGr0mdBRovmL_Umte0NV5QGxMcsgh0q_MmOy8rG1ZQJC-Mqcgo7e2fkeXE6jzPTQ9FLR4ANVVgvKSjSZU01eKsIL4c4I-drv5MfmHmkcUFWUxLYnABpHgNWS0hRdwpLSls0AF9p31jdFsQ7Bnt1P-ICn3rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ممکن است مجبور شویم ضربه بزرگی دیگر به آنها وارد کنیم. هنوز مطمئن نیستم
🔹
خیلی زود خواهید فهمید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131892" target="_blank">📅 19:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131891">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
🔴
اگر وحید هاشمیان و پرسپولیس توافق نکنند، تکلیف صدور کارت مربیگری اوسمار چه می شود؟ هوشنگ نصیرزاده پاسخ می دهد
‼️
‼️
نصیرزاده: برای فسخ قرارداد یا برکناری سرمربی هیچ محرومیتی تعیین نشده است و فقط باید غرامت پرداخت شود. اگر در قرارداد وحید هاشمیان مبلغی برای…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131891" target="_blank">📅 18:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131890">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
باشگاه پرسپولیس با ارسال نامه‌ای به مسعود پزشکیان خواستار جلوگیری از بی عدالتی در اعلام نمایندگان ایران برای فصل بعد رقابت‌های فوتبال آسیا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131890" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131889">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131889" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131887">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
با اعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131887" target="_blank">📅 15:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131886">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚡️
حکم جلب رشید مظاهری گلر سابق کیسه به خاطر بدهی ۴ میلیاردی صادر شد، میگن متواری شده!
⚡️
عجیبه با این قرارداد های میلیاردی که داشتن ۴ میلیارد بدهکار باشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/SorkhTimes/131886" target="_blank">📅 15:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131885">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
یکی از گزینه‌های اصلی باشگاه ، برای گلر ذخیره جایگزین امیررضا رفیعی آرمین عباسی گلر جوان پیکان تهران است   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131885" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131884">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7h8JLP2MNI-E8xF-OOCUYSSZfqebVp3x_in09HaZWTZCqCIjIu4Ha_GyXTsVuP_KqHX2C8qvylwS5FcHYNWkONt6VwrW7xKYbK6kFK2Xk3CAvH4CdMJBjEhmwALBzhOlP4iESbeufAHXNPUqSqB8OBv2I8iE5ms2CVLysFYgVyTIvHLWkdMq7tVjqjrfaLX9Ao18yQxXFJoBdCSLukaWDcCoWWFBdMijg--CZiztKcGkFT5Apip1r9cRu0V2cOmsM-cxBc25SwvsvuUlWDPIKZZP2pSNw9ZHRHNWkE3Vcw_kN1QrFSCIDu9BWkVSZShIOJYjtk7iHJMoJcraRIewg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعتراض کنایه‌آمیز باشگاه پرسپولیس: نماینده ایران در آسیا نباید با تصمیمات سلیقه‌ای و خارج از زمین فوتبال مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131884" target="_blank">📅 15:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131883">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131883" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SorkhTimes/131882" target="_blank">📅 12:53 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1vzDxtYYx-6QO2uLCH4O_sspcPDUP_Omsx1ycVas4JEHE1RUFIwFBe-N0h9fODJnbzuzlVImwJhGStNeMUe7mvjwjy2_cORhAx5RD55CtRs_PA29P_byBvB1fqCm6EEHY3WIjKqBDwbvN9a5s6hHuhMyfmo-6Oup9aJfk_SWL1q-F3sGjyCiqeQqePq7tvyWj0Su5Dk3HX5xzXtpJvaX55kElfjA18Ug8dVtxIhSOMY0BQEsn85u8gSLBRHXi3Dw6LjkszQ8mD59pUBArUr6Hdz0qD9ZLlGsjyYEk7dUixOUEu_znduOr9J090jLX0Ph5LSrspiA9BopP7fHCi_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یک تراکتوری در رادار پرسپولیس
◽️
با توجه به نیمکت نشینی صادق محرمی در این فصل در تیم تراکتور به نظر می‌رسد در انتهای فصل از این تیم جدا شود و با توجه به تمدید احتمالی اسماعیلی‌فر و حضور مهدی شیری در پست دفاع راست تراکتور صادق جایی در ترکیب تراکتور نخواهد داشت و از پرسپولیس به عنوان متحمل ترین گزینه وی یاد میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131881" target="_blank">📅 12:52 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
تغییر بزرگ در نقل‌وانتقالات؛ لیگ برتر ایرانی‌تر می‌شود
❗️
فوتبال باشگاهی ایران در آستانه فصل جدید رقابت‌های لیگ برتر با شرایطی متفاوت نسبت به سال‌های گذشته روبه‌رو شده و به نظر می‌رسد سیاست اکثر باشگاه‌ها در نقل‌وانتقالات تابستانی به سمت کاهش هزینه‌ها و استفاده بیشتر از بازیکنان داخلی تغییر کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131880" target="_blank">📅 12:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131879">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131879" target="_blank">📅 11:04 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🛜
سرور نامحدود 1 ماهه
Anyconnect
سرعت عالی،یوتیوب رو هم ساپورت میکنه
فقط و فقط 4.5T
🔥
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131878" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131877">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-wI-JlYoYAVlMI2FhHJCBFYs_tIjG_ehc7jjnNUdoQpcp6oKZK3N_bdC9NWBsfFQgTJiyV8l-Dhqh718rd7Y4uixNDPG77fepidn3gelnf82B83UHWqCOs5gh1R87FIrjAFC-oKXqzFbJASL6PbTOYinKGsrsZgBemdm1loEcFwZUheSrjCQJypjQIv6RF9o8Ccd2ZqlvVovBX9oqIQ8fODjk2UBy6xo1Gq9DP9wy9QfgU7zgGPGOW6vMjyUtILftgdgtGqTD_Kn6PXIolL250VzILDRSl_bH2H0H6Mm_ma10t-B5QGbFcvIy9BBBmv8GDQ8IOGRyBV4cztSj2lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
دسترسی سریع و مستقیم به
وینکوبت
📌
دیگه لازم نیست بین لینک‌های مختلف بگردی یا وقتت تلف بشه.
📌
فقط با یک ورود ساده به ربات رسمی، مستقیم وارد سایت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
⚡️
ورود سریع و بدون معطلی
⚡️
بدون لینک‌های اضافی و گیج‌کننده
⚡️
دسترسی مستقیم از داخل تلگرام
😀
همه چیز برای راحتی کاربران داخل ربات فراهم و قرار داده شده.
🔵
برای تحلیل‌ها و اخبار سایت وارد کانال سایت شوید:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/131877" target="_blank">📅 02:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131876">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=MMduAbfvZI8-jJf5wj3SXxM7ritjhabC26R-Ba1g_5MuQmVBL0-T11oWM-6vHwEFqS9tuUM2dPcRknvPgynybC6zRnd6FqPKarkExv-tV7FYFcvIBl0BZKOpBxPEzbk-RY5RX9X48S9_bYjBVwwwziTHnlI-hV4mFpi5BiF1WzTKs8PBk5k8ML3-aV5xRIwqEq4C2nmrexb5lGzmEoUeN5zb3DTzIa80bClF0xvSBDgRNUd04DOnQ0VRplZAQbRmZQz7dHOtR5l8JXouuSV66k6xc1B6FyZW-RThDZBm3KEQnz4HR4C6b4RKLc8lA2KYMkwxL7-oPMKZTXTusN89oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe16cfa21f.mp4?token=MMduAbfvZI8-jJf5wj3SXxM7ritjhabC26R-Ba1g_5MuQmVBL0-T11oWM-6vHwEFqS9tuUM2dPcRknvPgynybC6zRnd6FqPKarkExv-tV7FYFcvIBl0BZKOpBxPEzbk-RY5RX9X48S9_bYjBVwwwziTHnlI-hV4mFpi5BiF1WzTKs8PBk5k8ML3-aV5xRIwqEq4C2nmrexb5lGzmEoUeN5zb3DTzIa80bClF0xvSBDgRNUd04DOnQ0VRplZAQbRmZQz7dHOtR5l8JXouuSV66k6xc1B6FyZW-RThDZBm3KEQnz4HR4C6b4RKLc8lA2KYMkwxL7-oPMKZTXTusN89oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری فوتبال برتر: فردا قرار است جلسه‌ای برگزار شود تا چمن استادیوم آزادی را به بهانه ویروسی شدن جمع کنند و سپس طرح هیبریدی اجرا شود.
🔹
ما چمن هیبریدی را در تبریز دیدیم. نکند چمن آزادی هم به همین سرنوشت دچار شود. چمن در فوتبال ایران مافیا دارد. مراقب باشید کاسبی اتفاق نیافتد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.19K · <a href="https://t.me/SorkhTimes/131876" target="_blank">📅 01:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131875">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
ترامپ درباره ایران : من فعلاً عقب انداختمش، امیدوارم شاید برای همیشه، ولی شاید هم فقط برای یه مدت کوتاه
🔴
چون با ایران مذاکرات خیلی مهمی داشتیم و باید ببینیم چی ازش درمیاد  -
🔴
از من خواستن عربستان، قطر، امارات و چند کشور دیگه که اگه میشه این رو دو سه روز…</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/SorkhTimes/131875" target="_blank">📅 01:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/131874" target="_blank">📅 01:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26879febf9.mp4?token=IKRVLIuC8-rtXIhMCAshSAHLXcW2Duyjh3f-xoDVgoMPpfjQTTVJQTN3mZUdp1XO8e5g79FR3k-dCG2h_0IdLX3zLkMvyUj3GowBLeRU07pPZ8ifPGzl90HsWzUhA5VSPz6KBv8luPxSwMyXTuEQ7RzvlZFwVqPnFkELfCO5ifMX2Tyb2GDpb-tkOS6DP3D-MLw8tXQ4yN0kfXmJ2o5eIa38yXYIqpjYYKKqU007ATKM-zG4JImm7LwoexkiRNfhS6Prs2fxcxulQ_nMBPf3RAhb26rBlO51Kk-Drt3MAib5HzRsOKJfMqVorv6RCxcZ5wmA7uoLEA2DlQCWNLja0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26879febf9.mp4?token=IKRVLIuC8-rtXIhMCAshSAHLXcW2Duyjh3f-xoDVgoMPpfjQTTVJQTN3mZUdp1XO8e5g79FR3k-dCG2h_0IdLX3zLkMvyUj3GowBLeRU07pPZ8ifPGzl90HsWzUhA5VSPz6KBv8luPxSwMyXTuEQ7RzvlZFwVqPnFkELfCO5ifMX2Tyb2GDpb-tkOS6DP3D-MLw8tXQ4yN0kfXmJ2o5eIa38yXYIqpjYYKKqU007ATKM-zG4JImm7LwoexkiRNfhS6Prs2fxcxulQ_nMBPf3RAhb26rBlO51Kk-Drt3MAib5HzRsOKJfMqVorv6RCxcZ5wmA7uoLEA2DlQCWNLja0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما داشتیم آماده می‌شدیم که فردا یه حمله خیلی بزرگ و جدی انجام بدیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131873" target="_blank">📅 01:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=CGQJpelulUren4ZvboGd8ORsOnHD0bHd2H7I4XtY8OTe3zHNId2WtI6Dae03C-Tk_x-9XUWzYmw3g-bCNwWmoTP4dRE2tj6310SQAS9KSMYN2aDiGe0IQr7fltSmNBm9e4rSC88s9NiFWXWfQce4kbIASH0DARq7KKjLhFIThzvsfzKKQRSHcmtVsvZgLouvsLiooTr3rh173X3-1ryQDggxuPs4I39a-RKn8kerqtQggolI07UsXvPwaE_-18edeuiGTiALWYcW9VZ0Nz3f2j0pyDjDKijImB1UqTlvfcNkq0pvpmsRp3PbRO5jxZbAdx-AJM0riZuLquDwEXJfmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0edd05b28.mp4?token=CGQJpelulUren4ZvboGd8ORsOnHD0bHd2H7I4XtY8OTe3zHNId2WtI6Dae03C-Tk_x-9XUWzYmw3g-bCNwWmoTP4dRE2tj6310SQAS9KSMYN2aDiGe0IQr7fltSmNBm9e4rSC88s9NiFWXWfQce4kbIASH0DARq7KKjLhFIThzvsfzKKQRSHcmtVsvZgLouvsLiooTr3rh173X3-1ryQDggxuPs4I39a-RKn8kerqtQggolI07UsXvPwaE_-18edeuiGTiALWYcW9VZ0Nz3f2j0pyDjDKijImB1UqTlvfcNkq0pvpmsRp3PbRO5jxZbAdx-AJM0riZuLquDwEXJfmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جمله عجیب سخنگوی فدارسیون خطاب به تیم‌هایی که هفته اول خرداد تمرینات‌شان شروع می‌شود
◻️
علوی: شاید آنها خبری دارند که ما نداریم؛ ورزش کردن اتفاق خوبی است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.1K · <a href="https://t.me/SorkhTimes/131872" target="_blank">📅 01:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=rwM4tQDl8CnIkgQPPUVq0jcO5XOz4UdEd_Z_PLDWbpSZBY_QUG9H7nl3ly3Nx5p-SbMUleGpRmZLlLBXdgW9bB07BsIMvPsIbw2hCdWSvdQbh24t8YvHyBvlSyCL76_RdjPTbLv61cP0QRgqsC1VdKtciyX8UTPOq6rqo6l9iJnIMvqRVtCqg9h5ZirH6x5UPCWyT_QldCLqqusf9AX90_aF46R9fgsX6hflgz5RS0CqAaa4C7KV8hId7dCRTkGdY_JZV4Fm4TlV8Z0xECMLM3y2UmxN01Ui2dvCanEBn4Stkz0LtdaRgMVxTklgSklFefAUyIlxo2iSU1mqSGi50g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db79861a4e.mp4?token=rwM4tQDl8CnIkgQPPUVq0jcO5XOz4UdEd_Z_PLDWbpSZBY_QUG9H7nl3ly3Nx5p-SbMUleGpRmZLlLBXdgW9bB07BsIMvPsIbw2hCdWSvdQbh24t8YvHyBvlSyCL76_RdjPTbLv61cP0QRgqsC1VdKtciyX8UTPOq6rqo6l9iJnIMvqRVtCqg9h5ZirH6x5UPCWyT_QldCLqqusf9AX90_aF46R9fgsX6hflgz5RS0CqAaa4C7KV8hId7dCRTkGdY_JZV4Fm4TlV8Z0xECMLM3y2UmxN01Ui2dvCanEBn4Stkz0LtdaRgMVxTklgSklFefAUyIlxo2iSU1mqSGi50g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
علوی، سخنگوی فدراسیون فوتبال: دو هفته بعد از 10 خرداد و به طور کلی قبل از جام جهانی باید سهمیه‌ها را به AFC اعلام کنیم/ استقلال، تراکتور و سپاهان الان هستند ولی قطعی نیست؛ باید مجوز حرفه‌ای آنها صادر شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.01K · <a href="https://t.me/SorkhTimes/131871" target="_blank">📅 01:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=A5CSd3GlbeUt725Oess5_lYahIrYNSapb6Q4SNjZjVHdjyRKuINVgJI6Idl3O0HBCB5evLEpLm9Mdguc265gB1Ds2X1LMx2ykRrg2ARNXRwGTHI6WElnOIm4EJC2zeXWF4OzOR9XHj4iZ7DvFkVCAFN8XhzTBmMjAStBggekzNAAGcFGEyHPGMamyWYSAGM7ugGLLiV-D8imrmirAhmzW2f7FktK__QYD1E1GCHlgiIQPYghwmplw27cM1n8_C9S0zxNNWKekhDS-BAAjzqXxVcKhkvC-Iy5RgXx4ogUr6MwfQF370SAzUhRg3RydmbTnf3c8HvaBiFYgiP70bqCuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7d54cae7.mp4?token=A5CSd3GlbeUt725Oess5_lYahIrYNSapb6Q4SNjZjVHdjyRKuINVgJI6Idl3O0HBCB5evLEpLm9Mdguc265gB1Ds2X1LMx2ykRrg2ARNXRwGTHI6WElnOIm4EJC2zeXWF4OzOR9XHj4iZ7DvFkVCAFN8XhzTBmMjAStBggekzNAAGcFGEyHPGMamyWYSAGM7ugGLLiV-D8imrmirAhmzW2f7FktK__QYD1E1GCHlgiIQPYghwmplw27cM1n8_C9S0zxNNWKekhDS-BAAjzqXxVcKhkvC-Iy5RgXx4ogUr6MwfQF370SAzUhRg3RydmbTnf3c8HvaBiFYgiP70bqCuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
علوی، سخنگوی فدراسیون فوتبال: در حال پیگیری هستیم که باشگاه‌ها از تاریخ 9 اسفند به بعد درپی شرایط اضطراری به خارجی‌هایشان حقوق ندهند؛
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 994 · <a href="https://t.me/SorkhTimes/131870" target="_blank">📅 01:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔰
سرویس VIP
🔰
1 گیگ 250T
2 گیگ 500T
3 گیگ 750T
5 گیگ 1.2T
10 گیگ 2T
20 گیگ 3.5T
40 گیگ 5.6T
🛜
مناسب برای تمام سایت ها اپ ها
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 997 · <a href="https://t.me/SorkhTimes/131869" target="_blank">📅 00:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سه ماه تعطیلی؛
🚨
🔴
وظیفه اصلی که هیئت مدیره پرسپولیس فراموش کرده
🔺
هیئت مدیره باشگاه پرسپولیس که طبق قانون موظف است به صورت هفتهگی جلسه برگزار کند (و عادت داشت این جلسات را دوشنبه‌ها برگزار کند)، اما بعد از آتش بس چرا نزدیک به سه ماه است حتی یک جلسه رسمی نداشته؟
🔺
در این مدت، اعضای محترم هیئت مدیره همگی در تهران حضور داشته‌اند. در بازی خیرخواهانه حاضر شدند، مصاحبه کردند، واکنش نشان دادند، ابراز نگرانی و همراهی کردند؛ اما وظیفه اصلی خود را زمین گذاشته‌اند.
🔺
مدیرعامل باشگاه بدون پشت گرمی مصوبات هیئت مدیره، عملاً دست و بال بسته است. هر حرکت اجرایی نیاز به تأیید و چارچوب دارد؛ وقتی جلسه‌ای تشکیل نشود، خبری از مصوبه نیست و مدیریت قادر به گره‌گشایی از کارهای روزمره و بلندمدت نخواهد بود. نتیجه؟ باشگاه لنگ می‌زند. قراردادها روی زمین می‌ماند، برنامه‌ریزی مالی بلاتکلیف است و تیم در آستانه فصل حساس، سردرگم اداره می‌شود.
🔺
هیئت مدیره نباید تنها به حضور نمادین در رویدادهای عمومی و مصاحبه‌های احساسی اکتفا کند.
فریاد هواداران را بشنوید: «هیئت مدیره، به وظیفه قانونی‌ات عمل کن، وگرنه باشگاه را بیشتر از این به زمین نزن.»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/SorkhTimes/131868" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
#فوری | ترامپ:
🔴
امیر قطر، تمیم بن حمد آل ثانی، ولیعهد عربستان سعودی، محمد بن سلمان آل سعود، و رئیس‌جمهور امارات متحده عربی، محمد بن زاید آل نهیان، از من خواستند که حمله نظامی برنامه‌ریزی‌شده‌مان علیه ایران را که برای فردا تعیین شده بود، به تعویق بیندازیم
‼️
…</div>
<div class="tg-footer">👁️ 1.14K · <a href="https://t.me/SorkhTimes/131866" target="_blank">📅 22:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131865">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
#فوری | ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/SorkhTimes/131865" target="_blank">📅 22:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-131864">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=PvFavj95dllM65kr541wg7iGa9A-2R-nZU5ErKWyejwRir6aRAGjo3WFjYQeAipR4yaeYkEPC9VhgblGi7HI5OrJ5VN2-OSOlHRM9p2DfmfM6WK80x1tCxNRP_2tT-HU7ZRr10Ii29Kv5B6dK_S28mOQFoF2BRUDvrHxfh00wouHPmWXVMubF4UHHuc2nMTDn_wUiygh_Wi56RTNUZjKWi-dgyVAif3JOgiQ9K8QM3xXLN-pXBi_IwaKgFsGPHeFYY0142jMRTzqkPEShEQg8TkL00iLfV4bxYobGFFekP8oxM5VtKSgrlKMylWOeQhUjqQoAccZMmjSbCrvR0kbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/372dcfefd5.mp4?token=PvFavj95dllM65kr541wg7iGa9A-2R-nZU5ErKWyejwRir6aRAGjo3WFjYQeAipR4yaeYkEPC9VhgblGi7HI5OrJ5VN2-OSOlHRM9p2DfmfM6WK80x1tCxNRP_2tT-HU7ZRr10Ii29Kv5B6dK_S28mOQFoF2BRUDvrHxfh00wouHPmWXVMubF4UHHuc2nMTDn_wUiygh_Wi56RTNUZjKWi-dgyVAif3JOgiQ9K8QM3xXLN-pXBi_IwaKgFsGPHeFYY0142jMRTzqkPEShEQg8TkL00iLfV4bxYobGFFekP8oxM5VtKSgrlKMylWOeQhUjqQoAccZMmjSbCrvR0kbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
#فوری
| ادعای ترامپ:
🔻
حمله به ایران را که قرار بود فردا انجام دهم به تعویق انداختم
‼️
‼️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.12K · <a href="https://t.me/SorkhTimes/131864" target="_blank">📅 22:44 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
