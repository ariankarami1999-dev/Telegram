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
<img src="https://cdn4.telesco.pe/file/aOPv305zWY44xK-1CFCpqMVw2x5H_K6811fyCdn0xkptRT9FY-rEmcEmixJBBPT1uV2NoksL5q3Yix84M7cWpJC9qEG-XgpgWfZnQTIYBfR1NQtyjiBU0KNjTQa7gjZjsqKKQY4CADVHB1xrX1PsHEWjfaS-GlAM8IZvu8y88juDVvS-Y6hZBbGJqL0QMIQbUTTcCRlyMzjDufD-1Ab9S1o4vjSyWk0rxdUqoh_uObCZZwRjSawf_2mw7WALh93x7HKlPB7WpnGNKSENaLoBwXyrwND-QuMGZLE0kn8Vmhx-j72GSJmh613pn-WN0Sd2gc1hoJost9FTCCx9tJqxFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 02:28:56</div>
<hr>

<div class="tg-post" id="msg-132724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=h1kna5uHDnU_KO6CP5CTD_OCDyqxOPUbnkBCGRCgYZTvEn-Ep-k33qG8hQadBKvcuxlQ_tikKsyXlKyFaTTF9eFtuH1foRLCt_MFro4LdLi_1T3TNdj6858sdZO0RCNYThGm2Y8tJQ_6EB0LehF0ve3Fvx2CRh23au9btqyxiozrBmzkhMOLXySuDZocmKj2yoHmMiE3XTTebDp052xxcuZbwV3D7MeTgo0RoSFcg5NhfsfcjdV-vUVix_eIycIFQsOhHzTHe5q-UyWgWzh3jfrI1VSXdu1LGnVWc9vCmBoC7ZgeCN5-TmRyTuQKtAFYiESS_CiwOdQJSffCMvbv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=h1kna5uHDnU_KO6CP5CTD_OCDyqxOPUbnkBCGRCgYZTvEn-Ep-k33qG8hQadBKvcuxlQ_tikKsyXlKyFaTTF9eFtuH1foRLCt_MFro4LdLi_1T3TNdj6858sdZO0RCNYThGm2Y8tJQ_6EB0LehF0ve3Fvx2CRh23au9btqyxiozrBmzkhMOLXySuDZocmKj2yoHmMiE3XTTebDp052xxcuZbwV3D7MeTgo0RoSFcg5NhfsfcjdV-vUVix_eIycIFQsOhHzTHe5q-UyWgWzh3jfrI1VSXdu1LGnVWc9vCmBoC7ZgeCN5-TmRyTuQKtAFYiESS_CiwOdQJSffCMvbv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه رایگان وینکوبت رو از دست نده!
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
<div class="tg-footer">👁️ 759 · <a href="https://t.me/SorkhTimes/132724" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132723">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132723" target="_blank">📅 01:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132722">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
🚨
ترامپ:
🟢
نیازی به حمله زمینی به ایران نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.11K · <a href="https://t.me/SorkhTimes/132722" target="_blank">📅 00:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132721">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❗️
پاداش ویژه مدیرعامل باشگاه پرسپولیس به امیرحسین محمودی
🔴
دکتر پیمان حدادی به دلیل درخشش امیرحسین محمودی در اردوی پیش از جام جهانی تیم ملی و راهیابی او به عنوان جوان‌ترین بازیکن، یک پاداش ویژه برای وی در نظر گرفته است. این پاداش پس از بازگشت محمودی از اردو…</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/132721" target="_blank">📅 00:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132720">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_x8kPjWybBF9jHBOnjttMcSOg0aqmalJ8kudlumT_muLXdPEOtNGdPObWcWvJOGBxK9onbVZQu7H3RYFRTy31yAGgmkmO91WT18EVSaBByf7dKDK4xwhEZTnUAto9iBGJN0qoV-6GSJBbJ9jOCNjZIqUyBXTDM5X5zbh55ufCnnWwRuRLNcFUupPGce2lomqna5-OkprWKrJGk5NqjKcYV8o2vO86SwBsAHNuyYhOwfqOATBO1DQuEocDYUaC_QSzmYyQqfSHKbCxrJj9gl1AqYGZ2dDoDK2c3NS2v-rkKGP7fVPlmXWsQb73U1vyG1LgKKTsepIS5GyvUP5Pwj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قدوسی: باشگاه درحال مذاکره با اوسمار تا وضعیتش برای فصل آینده مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/SorkhTimes/132720" target="_blank">📅 00:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132719">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
طهماسبی، سرپرست هوادار: پرسپولیس مایل به خرید امتیاز هوادار است اما ما تمایلی نداریم
⚪️
خرید امتیاز هوادار توسط پرسپولیس؟ این موضوع به قبل از جنگ برمی‌گردد. پیش از آن، باشگاه پرسپولیس صحبت‌هایی انجام داده بود و جلساتی هم برگزار شد. آن‌ها تمایل زیادی داشتند…</div>
<div class="tg-footer">👁️ 2.41K · <a href="https://t.me/SorkhTimes/132719" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132718">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
🚨
🚨
عصر ایران نوشت: سفارت آمریکا به طارمی،شجاع خلیل زاده و احسان حاج صفی ویزا نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/132718" target="_blank">📅 23:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132717">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/SorkhTimes/132717" target="_blank">📅 22:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132716">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
فوری؛ سروش رفیعی از پرسپولیس جدا شد /فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/SorkhTimes/132716" target="_blank">📅 22:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132715">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/SorkhTimes/132715" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132714">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-B7f30L5NfzXPH-HDL9ra4skcNjpyVxNZk6DGlQ1zbnWOoJQdhtRpwLe9iCnYMrRHv9omBoYCYixUxlaXhFQUmVaopNAs2iLg7Ov9kO_01L6uVxoFbfoJpQRSCM3X2FE7OoZ3bt2OlwwAtx7YS3LVZKe3hRGOTFd2pSLicCTHyxkb2C4gqvLCZMVdESx-cZb9kjkrYakr9jJtAWiDvgMOaOucsDX5Ub3WfKxmTc7whOWUriO6r_WEZl3tl2-WX0Epa-Vb_yfMbnSpBLSsv_ytiJrg4KBVC1yQ0XmYQH5hRsrXXP1t_pY0-I1ip8c1cHr6RlqNvBRZm8R_vP-SVaGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آوا اسپرت کوردستان: یحیی گل‌محمدی اکنون در دهوک است و فصل آینده سرمربی تیم دهوک خواهد شد، قرارداد امروز امضا خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/SorkhTimes/132714" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132713">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❗️
فرهیختگان: باشگاه قصد داره اول با گرا و بیفوما برای فسخ توافق کنه و بعدش اسمشون رو در لیست مازاد اعلام کنه تا مثل اوریه بگا نره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/SorkhTimes/132713" target="_blank">📅 22:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132712">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300
30 گیگ 350
35 گیگ 400
55 گیگ 500T
100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/SorkhTimes/132712" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132711">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⁉️
⁉️
نت بلاکس: سه ماه پیش در چنین روزی Iran دسترسی به اینترنت جهانی را قطع کرد. در حالی که اتصال اکنون تا حد زیادی بازگشته است، شاخص‌ها نشان می‌دهند که کاربران هنوز با فیلترینگ شدید مواجه‌اند، مشابه دوره موقت بین اعتراضات ژانویه و آغاز جنگ.
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/SorkhTimes/132711" target="_blank">📅 20:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132710">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای (رهبر شهید )   ۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی  ۲۳ خرداد/ تشییع در تهران  ۲۴ خرداد/ تشییع در قم  ۲۵ خرداد/ تشییع در عراق  ۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد  پ.ن تخمین جمعیت حدود 25 تا…</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SorkhTimes/132710" target="_blank">📅 20:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132709">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❗️
رسما پایان جنگ اعلام شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/SorkhTimes/132709" target="_blank">📅 20:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132708">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚩
مارکو روبیو، وزیر خارجه آمریکا:
🟢
جنگ در ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132708" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132707">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
واکنش اسمار به  شایعه  اخبار جدایی او
📍
دلم برای انرژی آزادی تنگ شده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/SorkhTimes/132707" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132706">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
حسینی؛ سردبیر خط انرژی:  متاسفانه تابستان بسیار گرمی در پیش داریم و زمستون سرد ! توی جنگ اخیر به شدت بخش انرژی ما اسیب دیده و الان اگر چیزی حس نمیکنید بخاطر این هست که فصل گرما شروع نشده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SorkhTimes/132706" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132705">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
واکنش اسمار به  شایعه  اخبار جدایی او
📍
دلم برای انرژی آزادی تنگ شده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132705" target="_blank">📅 20:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132704">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
جزییات تاریخ برگزاری آئین خاکسپاری علی خامنه‌ای
(رهبر شهید )
۲۰، ۲۱، ۲۲ خرداد/ وداع در حرم امام‌ خمینی
۲۳ خرداد/ تشییع در تهران
۲۴ خرداد/ تشییع در قم
۲۵ خرداد/ تشییع در عراق
۲۶ خرداد (اول محرم)/ تشییع و خاکسپاری در مشهد
پ.ن تخمین جمعیت حدود 25 تا 30 میلیونی زده شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132704" target="_blank">📅 20:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132703">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❗️
🔴
آسیایی شدن پرسپولیس در گرو تصمیم cas
◻️
باشگاه پرسپولیس در تلاش است با استفاده از مسیرهای قانونی، شانس حضورش در رقابت‌های آسیایی را افزایش دهد. تعیین‌تکلیف شکایت این باشگاه از ملوان در دادگاه CAS زمان‌بر است، مگر اینکه درخواست رسیدگی فوری پرسپولیس پذیرفته…</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SorkhTimes/132703" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132702">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✅
با توجه به اینکه قرارداد سروش رفیعی تا پایان فصل به اتمام می‌رسد و باشگاه هم علاقه‌ای به ادامه همکاری با این بازیکن ندارد، احتمال تمدید قرارداد او حالا از بین رفته و با پایان نیمه‌کاره لیگ بیست‌وپنجم، به‌طور قطعی دیگر جایی در لیست پرسپولیسی‌ها در فصل آینده…</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/132702" target="_blank">📅 19:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132701">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
یه شایعاتی منتشر شده که اوسمار شاید برنگرده و جدا بشه که امیدوارم دروغ باشه وگرنه دوباره وارد دور باطل عوض کردن سرمربی می‌افتیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132701" target="_blank">📅 19:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132699">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
نتانیاهو: ترامپ معتقده که میتونه مشکل غنی‌سازی رو با مذاکرات حل کنه؛ من فکر میکنم باید بهش فرصت داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/132699" target="_blank">📅 18:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132698">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✅
یک بـازی بیشتر گـل‌گـهر و ابـهام در تصمیم‌گـیری سهمیه آسیـا
🔴
در حالی که پرسپولیس ، گل‌گهر و چادرملو مدعی کسب سهمیه آسیایی هستند ، فدراسیون فوتبال برای تعیین نماینده سوم ایران کارگروهی ویژه تشکیل داده است. نکته قابل توجه اینجاست که علیرضا اسفندیارپور، مدیرعامل…</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/SorkhTimes/132698" target="_blank">📅 18:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132697">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">✅
شجاع خلیل‌زاده، با ۳۷ سال سن، پیرترین بازیکن تاریخ ایران در کل ادوار جام جهانی فوتبال خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132697" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132696">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🔴
🇭🇺
❌
قرارداد دنیل گرا بزودی با پرسپولیس فسخ خواهد شد.  این تصمیم توسط اوسمار به هیئت مدیره باشگاه پرسپولیس گفته شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132696" target="_blank">📅 18:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132695">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
🚨
ترامپ:
🟢
نیازی به حمله زمینی به ایران نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/132695" target="_blank">📅 18:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132694">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
گل گهر، چادرملو و پرسپولیس به ترتیب به علت حضور در رتبه های چهارم، پنجم و ششم در صورت کسی مجوز حرفه‌ای جایگزین سپاهان در لیگ قهرمانان آسیا سطح دو خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132694" target="_blank">📅 18:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132693">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❗️
ترامپ   به نظر میرسد که ما با آیت‌ الله رابطه خوبی داریم دوست دارم او را ملاقات کنم. احتمالاً در مقطعی او را ملاقات خواهم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SorkhTimes/132693" target="_blank">📅 18:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132692">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06335497.mp4?token=aKoYRcsqRfpzyCDBrulirQ4eSbIxF3H5DVsd-oc7LZmCgDmVrzeIcfLvRaET-6N3CxWbnybo7CnyQwp5ENFd2sVVMVHvwsdTtLebdeicL1tdoYk0WRMH7bFGdFNtKBmrbBd5z1CPJvvwyjiSBxFGjifIn4akACxziStl9hes7yaZvFvTmG6wx5wQE2WezgUahSSN06pdicSJx-NdUhJvRBb6LldLi6KhylSVqgG5IUTN7EkDlwLcMjcCvy3k7fOet2IUQSMuxia-q65li0ESyvBd7f7utAG_TV9yOXdIM8kBRLgaRUiYPfVYcnikLD_5hJIHlCTJ0kij7vrUxRlc9SnaNjhx38HuHgZxyugCceaKZscMiBoODY1ozYv9jMffS4IFvqSJXslwt9dxgTeqV7O5iSX-OGti9PoH0Osy7gUgf35zk-pnX-ni-Xdkt4cxYtwBtoOiyb1R7gU9lkLpehC9SkqtYnjyX9FQhrT4xH16V8Ua0-ReXuAT2uv5MKZFKplbLiH4gd-JLlYph0Wx5-_ujQ_vJTZAtkBxxvvySRNWYlqUtFVAYmgSbS6Y2CW9LXHHdmc6-tzEVdC27X-zqvMgWfwvJjaahBLKQwOdJ7KvyZG2GB1gGxnBJb-PHrWDnvzuTRQ9uTxNVtLV4s0tjic4NwHLu4dQ-LEFKD7O3DM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06335497.mp4?token=aKoYRcsqRfpzyCDBrulirQ4eSbIxF3H5DVsd-oc7LZmCgDmVrzeIcfLvRaET-6N3CxWbnybo7CnyQwp5ENFd2sVVMVHvwsdTtLebdeicL1tdoYk0WRMH7bFGdFNtKBmrbBd5z1CPJvvwyjiSBxFGjifIn4akACxziStl9hes7yaZvFvTmG6wx5wQE2WezgUahSSN06pdicSJx-NdUhJvRBb6LldLi6KhylSVqgG5IUTN7EkDlwLcMjcCvy3k7fOet2IUQSMuxia-q65li0ESyvBd7f7utAG_TV9yOXdIM8kBRLgaRUiYPfVYcnikLD_5hJIHlCTJ0kij7vrUxRlc9SnaNjhx38HuHgZxyugCceaKZscMiBoODY1ozYv9jMffS4IFvqSJXslwt9dxgTeqV7O5iSX-OGti9PoH0Osy7gUgf35zk-pnX-ni-Xdkt4cxYtwBtoOiyb1R7gU9lkLpehC9SkqtYnjyX9FQhrT4xH16V8Ua0-ReXuAT2uv5MKZFKplbLiH4gd-JLlYph0Wx5-_ujQ_vJTZAtkBxxvvySRNWYlqUtFVAYmgSbS6Y2CW9LXHHdmc6-tzEVdC27X-zqvMgWfwvJjaahBLKQwOdJ7KvyZG2GB1gGxnBJb-PHrWDnvzuTRQ9uTxNVtLV4s0tjic4NwHLu4dQ-LEFKD7O3DM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویزای اعضای تیم ملی برای حضور در جام جهانی صادر شد
⚪️
سفیر ایران در ترکیه: ویزای اعضای تیم ملی برای حضور در مکزیک، امروز صادر و تحویل بازیکنان شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132692" target="_blank">📅 15:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132691">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🖍
دو باشگاه پرسپولیس و هوادار تهران برای واگذاری امتیاز این باشگاه لیگ یکی به باشگاه پرسپولیس به توافق رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/SorkhTimes/132691" target="_blank">📅 15:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132690">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❗️
تسنیم : یحیی گل‌محمدی به جز باشگاهای عراقی یه پیشنهاد مالی خوب هم از تراکتور داره و ممکنه بره تبریز!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/SorkhTimes/132690" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132689">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR6IAGs43A2aooBy8soRpWK1wFowUasx3Gwe21hOFwxeZ80Jxv2qnzHsiUKJ4PwZedoQt8-5PVqb-vk1UUeewsOY5Q5rFLORDKQrsH8HbosFEzUnbF6aZ0dvYRtTsW80h3wGq1rM543usqHuUqj8f8AmJxRcYKshdW23EmJQ5KHl-DqGDhWxYzIgomJ-DuKb9sQIoFmfxcCnuzNn2afdWQjgqpu6BovT9m7-4wt_XWwbUzVNeZBszCdFMn6tiPDyNijH31bmVua3YjaTJYgxa4lLEPj7e-3ab9xfD-Z-PjpikSz6dFSN9_kCUIFX74fYp65PNfGnD22bSBz2LiJvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
رقابت جذاب و حساس برای رسیدن به نیمه‌نهایی رولان‌گاروس، دیدارهای هیجان‌انگیز امروز تنیس رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132689" target="_blank">📅 14:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132688">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oThl3KHz3ZlH8uqmkX8CxeuxAh9pOTGCCJW22PJzLu0xmqn6G0AdHlOAMoZt8siyoWNDCsS7TL4rcqRQsXC-hJNE8jr8R2xbPxNh7NQd4NUAeesZBJBp_womVdtSOWBAJQ9OJDVqdPJkF4oqSgv7-BlYHQWDM76YrMfoK_MdYchk-PLLmRbnsVC2B1TQa_djgKLxjWJPNquDXo5St4ILNRcYUPZmreY2w5fXkDab4xKogM4Pfkp4Akf7jBmNTBlsgE88rF8KQZu788feCdFM9hFpn2KwlmnWmrVHk2H2zJxnbNk5fVWHlaHfdnAsTsEyl1GVT0q3ZYVA8Jei79BxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
روز کارگر که ترامپ گفت ممکن است محاصره دریایی ایران را لغو کند 4 مهرماه است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/SorkhTimes/132688" target="_blank">📅 14:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132687">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❗️
ترامپ   به نظر میرسد که ما با آیت‌ الله رابطه خوبی داریم دوست دارم او را ملاقات کنم. احتمالاً در مقطعی او را ملاقات خواهم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132687" target="_blank">📅 14:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132686">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
🚨
ادعای ترامپ:
🟢
شاید با مجتبی خامنه‌ای دیدار کنم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132686" target="_blank">📅 14:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132685">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
ترامپ برای هزارمین بار گفت؛
🟢
ایران موافقت کرده سلاح هسته‌ای نداشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132685" target="_blank">📅 14:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132684">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ برای هزارمین بار گفت؛
🟢
ایران موافقت کرده سلاح هسته‌ای نداشته باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132684" target="_blank">📅 14:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132683">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
‼️
چین از آمریکا و ایران خواست آتش‌بس را حفظ کنند.
پ.ن: آتش چه بسی هی همو انگول میکنید
🤣
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/SorkhTimes/132683" target="_blank">📅 13:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HOMyg1eWW3EQuJEnK32G4H_z1FPsugq9B2lggwXBe1cpe-LCLgq70DobkcaPRMX3EYzuClavdQm1aJkm9FVv3Nrluw12NdaYj2ykN1cpgKyswjrcMJCKFVI34Ma2bBbbW0LBQ33IWCw57whViK5za1_OvlD14oxy3N3qYtC0Lm2-pFtEJHr4Z-psR9Dn7AGt_KtQ-v13ubLwginOx3t_IRwYmebNNTcV2T1h0ej_SdK4LEMC3IsUKGR79H5jjV6JkgA7xUothvB1Ybst4FkvM-smXDFoVBe8rrS0LIPEgjN4My_zQSvu8roy7xr6ydI_pneIYgsjjHP_Sk9hOHZlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mflcbqo0HYFfWZny1jmRk2ynvOuvGppgciEZ2F4DUCkhYWo3tbH5x0XjK9kk_EpwcEkcxRMM2BC4xwDs4dKOXczI3CKYhyR6um4uOSkm3otVovDr09VCDSahaf5p4GoZfVDW6MXWFsjvuaO6hCuPQASBfdNEq96lknY4abbUspvs2N9wAFGSsCHGrun3YW5WU7Qzavu--X3MeydIeQgj98gh8bbJfzhzuBw01dhQcraQlS7kTkJ_EkuGM2JACoA3MMSgQnR7FJeSxMdfLarr15aTr4nn4evuOkQmDDlxvQdfssSgctTSJr24jLr7PhLLUhQvJFK8h2HyO2QABc97bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
وضعیت فرودگاه کویت بعد از حمله شب گذشته جمهوری اسلامی ایران
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132680" target="_blank">📅 11:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REkkoD49IHPGp_ULJnsN9GcOZLAyfVPbJpFZEGqgH_nPUcdzPgVXGGmXOj6wqnb82C_LDd1cRyakMG_9CQ5TfSm--GpuE-wo4pv_SGDXB7yhmsquPXROw5og_2byi0xhb1VHppvAaOVn6wXtgoFulS-zh63mAGWDguUASeXo8o_Eq_d2kPUaiHE_qJmXfDo9hujld2mya7hz2rJjCIg3AnS-2a1Fwp_whbFResE_b7Z1hya8k0ghVAOUw8_6E-stWDEeNLuOCPjbm0wSU6W_NU6HmwsdMpWtVffphX2n7aVBI61WCKCPf6yGxg1U75TLetthWBwq-N6OcGvBo-tiFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖍
دو باشگاه پرسپولیس و هوادار تهران برای واگذاری امتیاز این باشگاه لیگ یکی به باشگاه پرسپولیس به توافق رسیدند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132679" target="_blank">📅 10:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
توییت مهدی روزخوش، مدیر رسانه‌ای باشگاه پرسپولیس در واکنش به صحبت های زارعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132678" target="_blank">📅 10:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c58750c58.mp4?token=hShpwCIpm4r10VYkfCBY2U42LgC7a9Hp3rtV-LQAt3yBg8DExFryTqlsxfP_I6BJWvsUNGVtdgwBm_kkymnApcRv040NOKx_xIg4qSgTK_VtNoO_iJ2_a3AmGNeg8rduV62edIoMZ4BBTynZrjEfKtWluDvWHvk0omgfWlNWeOraGgMFRTNLNJsrBmC3EYsd9kjPq5quGIeFHhO_h9lYLDBsMaIth-4Jlaxk9LDZwOcLY4dP153gbThuYp5NPxjQ20kwsCHAWU-CWi-uJX6HjIWUHOVxiHFOE7a9iHJ9yTKrMj5hhLhikZ1VI_991xAW-vOtMaK1oHsUb-eqLMZKdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c58750c58.mp4?token=hShpwCIpm4r10VYkfCBY2U42LgC7a9Hp3rtV-LQAt3yBg8DExFryTqlsxfP_I6BJWvsUNGVtdgwBm_kkymnApcRv040NOKx_xIg4qSgTK_VtNoO_iJ2_a3AmGNeg8rduV62edIoMZ4BBTynZrjEfKtWluDvWHvk0omgfWlNWeOraGgMFRTNLNJsrBmC3EYsd9kjPq5quGIeFHhO_h9lYLDBsMaIth-4Jlaxk9LDZwOcLY4dP153gbThuYp5NPxjQ20kwsCHAWU-CWi-uJX6HjIWUHOVxiHFOE7a9iHJ9yTKrMj5hhLhikZ1VI_991xAW-vOtMaK1oHsUb-eqLMZKdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موضع باشگاه پرسپولیس نسبت به معرفی سهمیه های آسیایی؛ لیگ نخبگان یا لیگ قهرمانان 2؟ سخنگوی باشگاه: فرمول ها تعیین می کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132677" target="_blank">📅 10:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
صداوسیما تأیید کرد که نیروهوایی ارتش دقایقی پیش مقر تجزیه طلب های پانکرد در اربیل عراق را مورد هدف قرار داده اند
‼️
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132675" target="_blank">📅 08:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c3edbb36d.mp4?token=h4P6La33zm-RLtjCiFQY9is2wUkY7iPGTs1nGbmNy_cVzZC9AuCbCPGF99AKgw9kSaAxh8cMNTCSIfs9G-08XnTc9jmwuVHQzRSDwQutXYd2XgIYyQF1Vcpp4pkQBEoSXHyt3hLn8UmrxdKLiV5BiIXgewLXXC91dFAas73unhRtTd2ShM6bf9LbLQ3Vhkw5ft81p0y-LcBMcljRmBAR4dFVMJRcCmfiFF6_S4ppCF9tX3h_aVjfGV-7sdMqe0fpGq5vBGrYsTkMrxEQbjvx1roSLgUMa8VaB4xVajXZu9DOBpPOiFZRVaMETstrFgPyyxmQ8sLs-w9Qeam0EmEJ_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c3edbb36d.mp4?token=h4P6La33zm-RLtjCiFQY9is2wUkY7iPGTs1nGbmNy_cVzZC9AuCbCPGF99AKgw9kSaAxh8cMNTCSIfs9G-08XnTc9jmwuVHQzRSDwQutXYd2XgIYyQF1Vcpp4pkQBEoSXHyt3hLn8UmrxdKLiV5BiIXgewLXXC91dFAas73unhRtTd2ShM6bf9LbLQ3Vhkw5ft81p0y-LcBMcljRmBAR4dFVMJRcCmfiFF6_S4ppCF9tX3h_aVjfGV-7sdMqe0fpGq5vBGrYsTkMrxEQbjvx1roSLgUMa8VaB4xVajXZu9DOBpPOiFZRVaMETstrFgPyyxmQ8sLs-w9Qeam0EmEJ_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
انفجارات شب گذشته عنيفة تهز الكويت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/132674" target="_blank">📅 08:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله القاصم الجبارین
فَمَنِ اعْتَدَىٰ عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَىٰ عَلَيْكُمْ
🔺
در اواخر شب گذشته
ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگه هرمز مورد اصابت پرتابه هوایی قرار داد
که این نفتکش از محل موتورخانه دچار خسارت گردید.
🔺
در پاسخ به این تجاوز و نقض مقررات تنگه هرمز شناور متعلق به دشمن آمریکایی صهیونی به نام پانایا مورد هدف موشک های نیروی دریایی سپاه قرار گرفت.
🔺
دشمن آمریکایی در تجاوزی مجدد یک دکل مخابراتی سپاه در جنوب جزیره قشم را هدف پرتابه های هوایی خود قرار داد
🔺
در پاسخ به این تجاوز،
پایگاه هوایی و بالگردی آنان مستقر در یکی از کشورهای منطقه و همچنین مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفتند.
🔺
پیش از این
اخطار داده بودیم که در صورت تجاوز پاسخ متفاوت و سنگین تر خواهد بود و همینطور اقدام کردیم.
این پاسخ ها باید عبرت شده باشد.
🔺
تکرار می کنیم برهم زدن امنیت تنگه هرمز تاوان سختی برای ارتش متجاوز آمریکا خواهد داشت.
و ما النصر الا من عندالله العزیز الحکیم
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132673" target="_blank">📅 07:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132672">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm0oa-Jip_h-HRrlnMyqn1lAN2E5UY-s_F1Q1FugsTJ2yuL6G_cVWgC-GGMbmUvbgQiewedLjOBcc5-yKPQsGss401GwwlKAXMyEySvNT84COLu8O0H2qNujVCJFh0wtK81pQDzEc9skl2rZs_DHT45rE9eL8rRN9QHIFaQxsKuSikBitrIzN5myy0F83BqNdIcXTZZxEYZ8-liDKzeUXrHkM5PxVBungNvBwQ142SFv-tL-ZLide7YCg1QWX1O3J6QpXN4LaVKp1-F1f5cjXWtiGcOvVxovcDH3zMXfuDr8kxdY8ejFG9I9bzoSlJV48T8fC4bB1Ms3USZCP4Igtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
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
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132672" target="_blank">📅 01:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132671">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
با توجه به اینکه قرارداد سروش رفیعی تا پایان فصل به اتمام می‌رسد و باشگاه هم علاقه‌ای به ادامه همکاری با این بازیکن ندارد، احتمال تمدید قرارداد او حالا از بین رفته و با پایان نیمه‌کاره لیگ بیست‌وپنجم، به‌طور قطعی دیگر جایی در لیست پرسپولیسی‌ها در فصل آینده…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132671" target="_blank">📅 00:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132670">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حدادی: تمرکزمان این است از بازیکنان با استعداد خودمان استفاده کنیم. عنایت زاده، سهیل صحرایی، براجعه و صادقی و سایر جوانان ما با استعداد هستند.
🔺
یکی از سیاست های ما این است در ۲ یا ۳ پنجره نقل و انتقالاتی میانیگن سنی تیم را پایین بیاوریم و هم به سمت جوانگرایی…</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/132670" target="_blank">📅 00:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132669">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚩
مارکو روبیو، وزیر خارجه آمریکا:
🟢
جنگ در ایران به پایان رسیده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132669" target="_blank">📅 23:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132668">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗️
داستان سروش و پرسپولیس تمام شد؛ پایان زودیاک!
◻️
تمام شد؛ داستان سروش رفیعی و پرسپولیس به صفحه‌ پایانی‌اش رسید.
◻️
درحالی‌که در ماه‌های اخیر بارها درباره ازسرگیری رقابت‌های لیگ برتر اظهارات متناقضی مطرح شده و شب گذشته هم مهدی تاج، رئیس فدراسیون فوتبال اعلام…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132668" target="_blank">📅 23:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132667">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
یکی از دلیل اصلی که می‌تونه منجر به مازاد شدن کاظمیان و سروش رفیعی بشه درگیری وبی انضباطی این دوتا بازیکنه
🔴
اگه یادتون باشه این دونفر تورختکن باهم درگیری فیزیکی داشتن وبعد اون اوسمارهیچوقت مثل قبل توتمرینات راشون نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132667" target="_blank">📅 23:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132666">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e855e53fd2.mp4?token=ZffG_ncV2T7yqaoMZAcyThnIYPReiUxeGLXCIj34KagXq9AAY9svHgd8tLAyXxLJyICYAVXgJVtNrzw13Uzw5PrQvM88URYvSu6Lqs1UP1894Pem3ueNS5QbLK7qIwDN7dciTuWyxlneMixrzU2PAhVN8xl_L_u7dQSD21sCE9YIota5vgeYDiSmZXn3cm849Lle5z0y7rvew5C82slaZspk8PQZ8u0MC2E56oByDVdKhgaTGjFbONTsu2kaMfzuR064cy9JVA0IoTwFD5gYL6laYS-VX9C3HQdH1_BDzN0_D-uBrgh06PEqOOjE3kTxA3qMOpApQNK5U6Ui9JmMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e855e53fd2.mp4?token=ZffG_ncV2T7yqaoMZAcyThnIYPReiUxeGLXCIj34KagXq9AAY9svHgd8tLAyXxLJyICYAVXgJVtNrzw13Uzw5PrQvM88URYvSu6Lqs1UP1894Pem3ueNS5QbLK7qIwDN7dciTuWyxlneMixrzU2PAhVN8xl_L_u7dQSD21sCE9YIota5vgeYDiSmZXn3cm849Lle5z0y7rvew5C82slaZspk8PQZ8u0MC2E56oByDVdKhgaTGjFbONTsu2kaMfzuR064cy9JVA0IoTwFD5gYL6laYS-VX9C3HQdH1_BDzN0_D-uBrgh06PEqOOjE3kTxA3qMOpApQNK5U6Ui9JmMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
کفاشیانم آبشو داد میثاقی بخوره
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132666" target="_blank">📅 23:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132665">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
حسینی؛ سردبیر خط انرژی:  متاسفانه تابستان بسیار گرمی در پیش داریم و زمستون سرد ! توی جنگ اخیر به شدت بخش انرژی ما اسیب دیده و الان اگر چیزی حس نمیکنید بخاطر این هست که فصل گرما شروع نشده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132665" target="_blank">📅 23:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
ترامپ: اشکالی ندارد که ایران نمی‌خواهد صحبت کند؛ فکر می‌کنم ما زیادی حرف زده‌ایم!
🚨
این به معنی شروع جنگ نیست. ما فقط سکوت می‌کنیم. محاصره را حفظ می‌کنیم!
🚨
هر چقدر که آنها بخواهند می‌توانم صبر کنم. این آنها هستند دارند ثروت زیادی از دست می‌دهند!
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132663" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔰
سرویس اقتصادی
🔰
25 گیگ 300
30 گیگ 350
35 گیگ 400
55 گیگ 500T
100 گیگ 750T
🛜
مناسب برای تمام سایت ها و اپ ها ،ظرفیت اتصال و مدت زمان نامحدود
جهت خرید از پیوی =>
@Winstn_Churchill</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132662" target="_blank">📅 22:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
شرزود تمیروف مهاجم سابق پرسپولیس با ۲۸ گل در ۳۲ بازی، آقای گل لیگ عراق شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132661" target="_blank">📅 22:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132660">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
حدادی:
تمرکزمان این است از بازیکنان با استعداد خودمان استفاده کنیم. عنایت زاده، سهیل صحرایی، براجعه و صادقی و سایر جوانان ما با استعداد هستند.
🔺
یکی از سیاست های ما این است در ۲ یا ۳ پنجره نقل و انتقالاتی میانیگن سنی تیم را پایین بیاوریم و هم به سمت جوانگرایی از داخل آکادمی باشگاه برویم.
🔺
از فصل آینده لیگ یک، «تیم پرسپولیس ب» در این لیگ شروع به فعالیت می‌کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132660" target="_blank">📅 21:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132659">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🏆
رونمایی از قوانین جدید جام جهانی 2026
🔺
مهلت پرتاب اوت (پنج ثانیه): اگر بازیکنی عمداً شروع مجدد بازی را به تأخیر بیندازد، پرتاب اوت می‌تواند به تیم حریف داده شود.
🔺
ملهت زدن ضربه دروازه توسط دروازه‌بان (پنج ثانیه): در مورد تلاش‌های عمدی برای به تأخیر انداختن زمان بازی هم چنین چیزی اعمال می‌شود و این می‌تواند منجر به دادن امتیاز کرنر به تیم مقابل شود.
🔺
تعویض‌های محدود به زمان: بازیکنان تعویضی 10 ثانیه فرصت دارند تا از نزدیکترین نقطه زمین را ترک کنند. اگر این کار را نکنند، بازیکن تعویضی حداقل به مدت یک دقیقه نمی‌تواند وارد زمین شود و تیم باید با 10 بازیکن به بازی ادامه دهد.
🔺
درمان بازیکنان در خارج زمین (یک دقیقه): بازیکنانی که توسط فیزیوتراپیست تحت‌ درمان قرار می‌گیرند باید به مدت 60 ثانیه از زمین خارج شوند. البته استثنائاتی نیز وجود دارد، از جمله برای دروازه‌بانان، مصدومیت‌ها و اگر حریف کارت زرد یا قرمز بگیرد.
🔺
پوشاندن دهان توسط بازیکنان: هر بازیکنی که در موقعیت درگیری لفظی با حریف دهان خود را بپوشاند، ممکن است با کارت قرمز جریمه شود.
🔺
بررسی درستی ضربات کرنر: اگر VAR (کمک‌داور ویدئویی) مطمئن شود که کرنری که به یکی از تیم‌ها اعطا شده درست نیست، می‌تواند دخالت کند و آن را لغو کند، اما این کار باید سریع و قبل از شروع مجدد بازی انجام شود. این اما شامل برگرداندن ضربه دروازه‌ای که باید کرنر اعلام می‌شد، نمی‌شود.
🔺
بررسی درستی کارت زرد دوم: بازیکنانی که به دلیل دو اخطار از زمین اخراج می‌شوند، می‌توانند کارت زرد دوم‌شان مورد بررسی قرار بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132659" target="_blank">📅 21:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThdCCrfoJPoK2ALnIvEfAiguZMGAp8xB6BITGQrjoGNuISlkJm2oJHqKpKD3c-OSZ8YpAU_WsA7hy49N_ZMtoKAonsHsfOTEJGem8XLO7DfIA7MTPsiyxhjzk8HOucCeo7i15b-XwcbY2yBI8-1eg9IZN8QQH56tsJQ4Np_FFnZJoYbw_QKmTHDfQ_PoPlrN8MNtW4T_QAZDqBHYRyI6oXcjjND5l2POFozRzuTaL6Aj0NzdsXKPOgV3v9veWIiEAguwC8dpdKeNplZu3uqIN1ZEGS51UKdWeXL5mB1rTogccqMWOEMNuCdowC1EP_Zv2FRQv8_sKdkqj9wpa5pyvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⛔️
معمای بارگذاری مدارک استقلال برای آسیا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132657" target="_blank">📅 20:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">▪
︎با این وضعیت اینترنت،
ربات تلگرام وینکوبت
خیلی کاربردیه چون براحتی وارد سایت میشی.
▪
︎هم ثبت‌نامش سریع انجام میشه، هم کازینو رو داخل خود تلگرام میتونی بازی کنی و عملاً کل سایتو داخل ربات داری.
▪
︎پیش‌بینی، بازی، واریز، برداشت و همه‌چی همونجا انجام میشه و خیلی روون‌تره:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132656" target="_blank">📅 20:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a6eda933.mp4?token=fIdcrCxdXofKB0IkZ_RwjvxyqMMlZdPRUlP4I5LrObNiOL5BmkqLcGduj_iLIzS7KW4beZVxk2QEC4tZPSfqm2M9Bi40jjRoGHgvLg6qyZ9t8uvds9h7SV9H7hRtMZ9kGlqXuN5hwhIHUEe15F3wYnNIBFUx7X1vobfcCotyxG9jBqjGj49rcLX2IdFgDaglT6d-APvCu9HAmNKQeE-UHzU24SysufqkWgm9fBTQ_Fo6UUticBl_bpXpYLakiMa2N9pt0QJf-J582GQoF17ygtRVIDbML9j6Iwj1i-9RtTZnYjNG-uBqhyzo5aaCoE1fol8pwxDb3ZWr4_KN8T3lZbHk0k7cKNm3Fc-Lr2zRkmqsBoVDtXbe6j9Xp6PsG6z632gbmj1YON8i4xeycW5EurNEfT0o55zsEyRO3m6erZg6AcNg5-a0XrZfKOjLRxkp5kle9-R_xgERoo0FDViMMxeG29oaJcYAZ1m-Vd6mfYKNxg9zxIuYXB9jc8_2-hJMWoeI_IRzlh8gxoLMegpifj0mN7ShS-TQbLTGL_bHuVV3qFGj78zOv51yBefBNrSWoft4oIurDJBJ8vrlyaKcqChpPO8uTP3TQ030a2HiLNdW2wWNNxyYHx3E_G257COKAlj3Bh1RZ4TXhMVQUeOzL9yccDIAoZ2z_E08aw-iqE0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a6eda933.mp4?token=fIdcrCxdXofKB0IkZ_RwjvxyqMMlZdPRUlP4I5LrObNiOL5BmkqLcGduj_iLIzS7KW4beZVxk2QEC4tZPSfqm2M9Bi40jjRoGHgvLg6qyZ9t8uvds9h7SV9H7hRtMZ9kGlqXuN5hwhIHUEe15F3wYnNIBFUx7X1vobfcCotyxG9jBqjGj49rcLX2IdFgDaglT6d-APvCu9HAmNKQeE-UHzU24SysufqkWgm9fBTQ_Fo6UUticBl_bpXpYLakiMa2N9pt0QJf-J582GQoF17ygtRVIDbML9j6Iwj1i-9RtTZnYjNG-uBqhyzo5aaCoE1fol8pwxDb3ZWr4_KN8T3lZbHk0k7cKNm3Fc-Lr2zRkmqsBoVDtXbe6j9Xp6PsG6z632gbmj1YON8i4xeycW5EurNEfT0o55zsEyRO3m6erZg6AcNg5-a0XrZfKOjLRxkp5kle9-R_xgERoo0FDViMMxeG29oaJcYAZ1m-Vd6mfYKNxg9zxIuYXB9jc8_2-hJMWoeI_IRzlh8gxoLMegpifj0mN7ShS-TQbLTGL_bHuVV3qFGj78zOv51yBefBNrSWoft4oIurDJBJ8vrlyaKcqChpPO8uTP3TQ030a2HiLNdW2wWNNxyYHx3E_G257COKAlj3Bh1RZ4TXhMVQUeOzL9yccDIAoZ2z_E08aw-iqE0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیا پرسپولیس به دنبال جذب لیموچی، ایری و آریا یوسفی است؟
🔴
پیمان حدادی: با هیچ بازیکنی مذاکره نکردیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132655" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1124c640f.mp4?token=txOXQLkFglzFJpKbPUgsZwDhMdWtPRD7tavMtat4o4JcZXoSEgRu9FeEWNi1ZnwfY8B08PJc_ZPCSXIVW-oUHcPr8K_zJfTk1g2NDMj_fYaXFvU8YUUcLtE7RY-atS_lQbFVF3pmDUiaUFzf2U3AbXnDOFGSP01EdbebfTWqV6kMBI1bPwQhrLIitrKwYjUnbo_Qgs_TvqibUSpDJhEP8oWJ7bmKiJeAICyNao2wj_hdPxGrNAFXGpGB1E1oarP-fuDv07stan5BzaocTawglgLb2C7zFd6SO53ppwt4ABHdcLRj-E6FGsYj1QvEB9WFRaMgz9xeTYcY0gJtk4ByHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1124c640f.mp4?token=txOXQLkFglzFJpKbPUgsZwDhMdWtPRD7tavMtat4o4JcZXoSEgRu9FeEWNi1ZnwfY8B08PJc_ZPCSXIVW-oUHcPr8K_zJfTk1g2NDMj_fYaXFvU8YUUcLtE7RY-atS_lQbFVF3pmDUiaUFzf2U3AbXnDOFGSP01EdbebfTWqV6kMBI1bPwQhrLIitrKwYjUnbo_Qgs_TvqibUSpDJhEP8oWJ7bmKiJeAICyNao2wj_hdPxGrNAFXGpGB1E1oarP-fuDv07stan5BzaocTawglgLb2C7zFd6SO53ppwt4ABHdcLRj-E6FGsYj1QvEB9WFRaMgz9xeTYcY0gJtk4ByHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: از فصل آینده لیگ دسته اول تیم پرسپولیس ب در این لیگ شروع به فعالیت می کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132654" target="_blank">📅 20:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
پیمان حدادی
: با هیچ بازیکنی مذاکره نکردیم هنوز
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132653" target="_blank">📅 20:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132651">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی باشگاه:
🔺
ما باشگاهی هستیم که به خاطر سابقه، به خاطر حضور هوادار، به خاطر امکانات، به خاطر شرایط حرفه‌ای سازی و موارد دیگر حق خود می‌دانیم که در فصلی که نیمه‌کاره مانده بتوانیم در رقابت‌های آسیایی فصل بعد حضور پیدا کنیم و برای موفقیت کشور ایران در آسیا بجنگیم که نفعش به همه می‌رسد.
🔺
ما در این زمینه از حق هواداران پرسپولیس کوتاه نخواهیم آمد و تا آخرین لحظه از حق خودمان دفاع خواهیم کرد. خیال هواداران هم راحت باشد که ما اجازه نمی‌دهیم تصمیمات خارج از زمین گرفته شود. همانطور که بارها اشاره کرده‌ایم، از نظر ما پرسپولیس می‌توانست در هشت بازی باقی‌مانده شرایط جدول را تغییر بدهد و به یکی از تیم‌های بالای جدول برسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/132651" target="_blank">📅 20:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132649">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132649" target="_blank">📅 19:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132648">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWGAVJsRLDvt9_NQTlu3HYgxpxdNU_li_D6QocfCs9VA_9ymVpBOUi9Pdn0EBsqfOVv4_Rlt4yy8QI9S0wsjVoYp093izzQkq2j8EVeQq06bpT0RopUOok0XmX_R0d8HEuok29DWosCbuvfuTB9LyAYYhXyDCQLpZR2AxOnlY2QufYumWrtW4-wOEJInoPj9F364k5mRSl5hUkMOhaSm8P7nbzrtoYlb3XaTLqbMG5Mn-xs40ItTzaST19HJmBQ1wWWPiVSiZPOiBxEgzVbBzxkiFRKq-tAENOFhorxqoiOBCVZvcSlVWvZR6fBSFUSRHzYW6zAC7P2lhJBTY_RFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گل محمدی هنوز تصمیم قطعی خود را نگرفته و می خواهد پیشنهاد تیم دهوک  عراق و شرایط موجود را بررسی کند و بعد تصمیم بگیرد.اخباری از سفر او به عراق در پی پیشنهاد تیم دهوک منتشر شده است
/قرمزآنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132648" target="_blank">📅 18:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132647">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5uiSnJ6AsL3x5UAyzH1Q3fo3Pi1_JUo0vdbSPKBO4iz8VBHHpHD_N9ZHj_j-rzpC2P9mB6MvGmlq4ibnbZdoTpHpmrugDZfylk-9135oKU2tK43sKhwsEijoEJWsN6-xctfDLP_WU9kp3EmPrOYHHz2nve2gaSYEOAQAdO76rQZM31tNSodBbiEGzjDaFYizhnEdjj-UswgUPu2WHuJlh-Sjx9BqfWT8LqVscI92LBZOJA6_faFd1WtkfQMZStWdIaky9v_gpCJDw5gukxl2GGaVYH9yXOycrGAKUHScTEFSKpSCrF2W7cz5NvSx8UxWqCmck33_3vMyYkuVVe7TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏅
برگزاری مراسم تجلیل از مربیان بازیکن‌ساز آکادمی فوتبال پرسپولیس
⏺
باشگاه پرسپولیس برای نخستین بار، طی مراسمی از مربیان بازیکن‌ساز آکادمی فوتبال باشگاه تقدیر کرد. این مراسم با حضور مدیرعامل، معاون ورزشی و مدیر آکادمی برگزار شد و از مربیانی که در سال‌های اخیر نقش مؤثری در پرورش استعدادها و معرفی بازیکنان به تیم بزرگسالان و تیم‌های ملی داشته‌اند، تجلیل به عمل آمد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132647" target="_blank">📅 18:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132646">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
روبیو:
🔻
ایالات‌متحده همچنان در حال گفتگو با ایران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SorkhTimes/132646" target="_blank">📅 18:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132645">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
🚀
خبرگزاری فارس: مذاکرات با آمریکا به بن بست خورد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/132645" target="_blank">📅 18:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132644">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dj3pyxYlWfCEvhc-XPkwydpdG-lsi1YpBKyBGoHI-5vcXhlvJ9EmyqhWNgKVFm0dz6oSNEZFMgCNhuK58o9ijHcQaHuYSoWIpn1u-1aSdtlpHmqaGc5CvN-ivYBinblx27TEiXP8RB98kCc2wqDF0mLWS7WSwc5P5wwywq98oScKGP-tWglDmilZGNfOkD474Sdt5HkqxaK_g5LFtcKixZJQEqNt3KLiaZNzl2R4209QoihL-EyK200E4DlCZTw90TnpkaeZD1jO9GLrHKa5OB3UltgMN4Bdx8pyQxmkAs8Srv-X_4Q9Eq86LXRLB4F4rqj1XIezGVeiv22XQqlFRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت مهدی روزخوش، مدیر رسانه‌ای باشگاه پرسپولیس در واکنش به صحبت های زارعی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/SorkhTimes/132644" target="_blank">📅 18:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132643">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
🚀
خبرگزاری فارس: مذاکرات با آمریکا به بن بست خورد
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132643" target="_blank">📅 18:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132642">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHgllOS7g4ygwfyZ54r5SCXXotnj01gwiDlhLSPaj07M_CGzDg3cwQj6aH9aKQ3AUqV0giOzEYGX6P-9IUKlTiRN2MoKyxuKrYsBUTw7moA1NjZ7I-E6GUdrnFntgzopvSbM-e_eXNI51PxrhiHjAxuy5lpqeOVFqC39BBySyOYX0Jj3vYYMxstyytTdVBBuxgs94T0hrhBz0VeroV98Tdbcw7gy-8t62-c4gDSdjR52ZGh-fOZQU21r8gBxyEroKUYUn-wFh6_VY0Xmm8Wyx4c3ZwaaRSqpAiKo2G87AavsPgFj_POow8Nb2weItolwKL_-XfhpYhyYaoGdzlSAoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با مثبت شدن دوپینگ یک کشتی‌گیر روس در مسابقات جهانی 2015، ایران به عنوان قهرمانی رسید و قرار است جام در رقابت‌های مغولستان به ایران تحویل داده شود اما مسئله اصلی اینجاست که ایران باید کاپ سومی که تحویل گرفته بود رو پس بده اما کاپ سوم گم شده و کسی نمیدونه کجاست
😐
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SorkhTimes/132642" target="_blank">📅 18:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132641">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
🔴
امید عالیشاه، بازیکن تیم پرسپولیس: در روزهای اخیر خبرهایی درباره سهمیه‌های آسیایی شنیده‌ام که واقعاً ناراحت‌کننده است. از همان زمانی که آتش‌بس اعلام شد، ما خواستار آغاز دوباره لیگ بودیم و حرف‌مان هم روشن است؛ نمایندگان آسیایی باید در زمین مشخص شوند، نه پشت میز. فوتبال باید برگزار شود تا تیم‌ها بتوانند حق‌شان را در زمین بگیرند، نه اینکه بیرون زمین برایشان تصمیم‌گیری شود.
🔺
واقعاً تعجب می‌کنم چرا در اردیبهشت که فرصت کافی وجود داشت، لیگ را برگزار نکردند؛ در حالی که بارها نامه زدند که مسابقات شروع می‌شود و ما هم بر اساس همین نامه‌ها تمرینات‌مان را آغاز کردیم. کشورهای منطقه هم درگیر جنگ بودند، اما لیگ‌شان را برگزار کردند. چرا ما این کار را نکردیم؟
🔺
تا جایی که می‌دانم مصطفی زارعی مسئول صدور مجوز حرفه‌ای باشگاه‌هاست و نیازی نیست درباره پرسپولیس یا نحوه انتخاب نمایندگان ایران در آسیا اظهارنظر کند. تصمیم‌گیری درباره سهمیه‌ها باید بر اساس رقابت واقعی در زمین باشد، نه حرف و تصمیم‌های بیرونی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132641" target="_blank">📅 17:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132640">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
اولین بمب تابستانی پرسپولیس؟
🔴
ادعای سایت هفت ورزشی؛ اگر اتفاق خاصی نیفتد آریا یوسفی را باید اولین بمب تابستانی باشگاه پرسپولیس برای فصل آینده لقب داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132640" target="_blank">📅 15:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132639">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=YXtp7MYLOW3fuGkzMfQLcZvE0_gXKemelCgF9fSrT5diOIqpFjw8VOYBHMRbKVgstywbzUtw46ky_CoKWJQ3hxSj7vhy9-X-BfhcnjncfJ1xdrr4A-7day5bVeTaJFHVvXXVFyAWuJA0D9Vf-bxJFXtpumrJbmTr9M2wQHdsCCZ2OhBDr6Aj5UUMNAniSItO4Cd5CDoq5_8_TURh1MjxbZtC_9Ekg_gkWNi4YXBLjen7GqHmxqU1UBlFvAzAA4R1Zhj2x4Ut8Ubr6NpH_WabN-4lydljLt54jpZTNpIGz0VFEkP531qgnHIfKiMs8ASeDvROmuIUo3cbzOPRxN0l0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/552e7d620b.mp4?token=YXtp7MYLOW3fuGkzMfQLcZvE0_gXKemelCgF9fSrT5diOIqpFjw8VOYBHMRbKVgstywbzUtw46ky_CoKWJQ3hxSj7vhy9-X-BfhcnjncfJ1xdrr4A-7day5bVeTaJFHVvXXVFyAWuJA0D9Vf-bxJFXtpumrJbmTr9M2wQHdsCCZ2OhBDr6Aj5UUMNAniSItO4Cd5CDoq5_8_TURh1MjxbZtC_9Ekg_gkWNi4YXBLjen7GqHmxqU1UBlFvAzAA4R1Zhj2x4Ut8Ubr6NpH_WabN-4lydljLt54jpZTNpIGz0VFEkP531qgnHIfKiMs8ASeDvROmuIUo3cbzOPRxN0l0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
واکنش مجری تلویزیون به آسیایی نشدن پرسپولیس؛ آیا یزد و سیرجان هتل 5 ستاره دارد؟ باید میانگین امتیازی سه فصل اخیر حساب شود که پرسپولیس بالاتر است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132639" target="_blank">📅 14:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132638">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
الهویی، مربی تیم ملی: امیرحسین محمودی  به دلیل مسائل غیر فوتبالی و شرایط غیر  عادی کشور از لیست تیم ملی خط خورد!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SorkhTimes/132638" target="_blank">📅 13:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132637">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
مبارک اونایی که تن به ذلت "اینترنت پرو" ندادن. بنظرم کانفیگ فروشا باخت ندادن چون بازم برای اینستا و یوتیوبت بهشون نیاز داری و تا الانم حسابی فروختن.و اما تویی که فکر میکردی خونت رنگی تره برو با گیگی ۵۰ هزارتومنت حال کن نفس
👈
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132637" target="_blank">📅 13:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132635">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
باشگاه پرسپولیس از زارعی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132635" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132634">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=dgsBPeHC9luUWHXMSNEl99ZRIl1QivzmzsMQ3OQxALJ4F3vzFiKpk3d4h0INotGl1o69kiszJxc9tV59o6v93p5RZ_0zpjmZeXx6WkkVLh8lFsgRtdFZnglI1HLiI480DJkdNJmuCHP1sIJYPUluPK9tpeFQeiwh3ckCR5iSMHdTrREztP2Q3K7nQSQuqGwDolo3XEISuywMLl3vvOGX7wfN60pVrBAtsUVSmdyzBTlg2wbaPAnsizwd2BJo-kCczO9l0WcbHo1jXRDwaSNFQG6YiXbNV3gspApEO30L5aIv5mMdXUmLVWIAmGmIOAHgLneKm2bhB1EsnKLxyX3KGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=dgsBPeHC9luUWHXMSNEl99ZRIl1QivzmzsMQ3OQxALJ4F3vzFiKpk3d4h0INotGl1o69kiszJxc9tV59o6v93p5RZ_0zpjmZeXx6WkkVLh8lFsgRtdFZnglI1HLiI480DJkdNJmuCHP1sIJYPUluPK9tpeFQeiwh3ckCR5iSMHdTrREztP2Q3K7nQSQuqGwDolo3XEISuywMLl3vvOGX7wfN60pVrBAtsUVSmdyzBTlg2wbaPAnsizwd2BJo-kCczO9l0WcbHo1jXRDwaSNFQG6YiXbNV3gspApEO30L5aIv5mMdXUmLVWIAmGmIOAHgLneKm2bhB1EsnKLxyX3KGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- همه اون لحظه‌ای که سایت نصفه لود میشه و VPN قاطی میکنه رو تجربه کردیم، مخصوصاً وقتی وسط بازی یا ثبت پیش‌بینی باشی.
😑
- ربات رسمی تلگرام وینکوبت کارو راحت و ورود به سایت رو آسون کرده:
👇
-
🤖
@Wincobet_bot
-
🤖
@Wincobet_bot
- برای کسایی که بیشتر وقتشون توی تلگرامه، خیلی کاربردیه.</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/SorkhTimes/132634" target="_blank">📅 13:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132633">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
زارعی رئیس کمیته صدور مجوز حرفه ای :
🖍
پرسپولیس به هیچ عنوان نمی‌تواند آسیایی شود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132633" target="_blank">📅 12:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132632">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/132632" target="_blank">📅 12:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132631">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXmmUgRqfOXmiDkq25cmGEuFPDAZFcFR2NKq7-H0ShpeOM9oWpeiz94KHm5RPj490rWAP8evMrh4ymQbxIqOSShpsi8k9txe27eVJEm3BQG2xj4gk6Nv2BoH7vMTPibTU0itlPlLkdJjQP3o2M8Phgsjy9GZPEU7_J5lZilkeMLBujkNXl4tVUtXyqehz-EungU7O3pCLt6Vj_0EoerMHvLmkHwml0wvwvhHcfCroWhB5zAdEFE6BdyGpnq7HSTCDUI7QcVuqVcTvRKxymmG7W5STYllj3pkPNgUgKREPxL0d4w0T-ZUKVpU2FHGRN4RxuIY7-TKXjWixRqX1f9o5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه شایعاتی منتشر شده که اوسمار
شاید برنگرده و جدا بشه که امیدوارم دروغ باشه وگرنه دوباره وارد دور باطل عوض کردن سرمربی می‌افتیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/132631" target="_blank">📅 12:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132630">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkzXBDt3GXGSZXhIX5XAZtHJwaQS43Row2OqzSGDfe4feyBPyas2j5C8i4zgDDRQPyDuXdhuSD84J29ThG3lm_XVuar1CF60QYBvj3qlMplJUtpT4120x98cnQ9u9VOsgQHI69xlj03SKZxlgn2jRmcre0ixFOqZ0kc_u9J5DsUYkmBvtlN-SweHBFHv6Lq3wWf6VydwHnUaC9gwC1ymp5bL_ZXbhpkmuwQ0U1V-4fCr3dEnH_39-KmK6G10-JTqZ-AhvJ-FQkjLqK0wXUrqvUKv9_up1dWEHwmeBpENYAqsUL1JDd-Gv9BwmVhieL4fsPxhfmsA0a1xIj7FqX1eYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
مدرسه پیرمردها رو نوسازی کنید.
🔴
#فرهیختگان
: پرسپولیس با ۸ بازیکن بالای ۳۰ سال و میانکین سنی ۲۷/۶ پیرترین تیم لیگ برتر شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132630" target="_blank">📅 12:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132629">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
اوستون اورونوف و ایگور سرگیف در لیست نهایی ازبکستان برای جام‌جهانی قرار گرفتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132629" target="_blank">📅 12:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132627">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل   پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132627" target="_blank">📅 10:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132626">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ken6BiXnyjBLeWHYxXQQgTkj4wi9SPeRwHcXBSe0BZuMJ9W2zNDPJOryImJeUcgoA5sMpmTBZ0P1-H0RNjbKGvMJgTS2mHrMxUnzyfkDqj5bCQaZ4zMyLu8ijRsyLUpbD1WlN2xcIryUhcNnml929kXvaOXX5o5kp_n-v_cO1tWH50XU2pQcz4QZDNCQrSiwED5yfH5TM4TQ-bhVn84DOge4ve9JDFNLm0c0eOalPdLMygd5UEQgzH4S90gZ_N31QpBPE6jtSBq5Kt3jUgjRWk7vRg3i9Bt1dzCmTSKXBjNnAolQsKRtyh_SyfpXvnIP88lawP7Kq8iucT6A00A1mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سر تیتر روزنامه‌ گل
پ.ن پرسپولیس از خودت شاکی باش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SorkhTimes/132626" target="_blank">📅 10:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132625">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
تسنیم: مطابق جدول فعلی گل‌گهر، چادرملو و پرسپولیس در رده‌های چهارم تا ششم قرار دارند، تورنمنتی برگزار خواهد شد تا تکلیف سهمیه سوم و جایگزین سپاهان روشن بشود
🔴
مشابه این اتفاق در پایین جدول نیز اتفاق می‌افتد و قرار است تورنمنت چند جانبه‌ای برگزار شود تا دو…</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132625" target="_blank">📅 10:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132624">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132624" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=hqPcfuZpX11ieXjQDuJCdhyqSeptlkk2o2Rh4urYQq-tB8Et6XseaOdvhBUttcpS0_wYGBPXyvrOuy2o88ZaDnnslbzlqMAH4ivee_ZBgN6aEpfoVQu86eq_18e-__Uch4sX6KLxCyT5WBZzMKwwCgj_fq-tr0jZKZCxC4nzOl4ul74C3-P1bSwOWAtrk8CGbvCUpUJECGTqK0nBaEskHOWEmOPWIDCLJ5hOvxokbiInPqEOyaspuniPzrjVSzVWhCUYqxs0zPUNVVC5TOAVrO_yXRkBK_BrOjmKAp57zBl1UW_MCiIO69zwXQPhpHZVq15kCDG8brpUJh8fBXjcZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=hqPcfuZpX11ieXjQDuJCdhyqSeptlkk2o2Rh4urYQq-tB8Et6XseaOdvhBUttcpS0_wYGBPXyvrOuy2o88ZaDnnslbzlqMAH4ivee_ZBgN6aEpfoVQu86eq_18e-__Uch4sX6KLxCyT5WBZzMKwwCgj_fq-tr0jZKZCxC4nzOl4ul74C3-P1bSwOWAtrk8CGbvCUpUJECGTqK0nBaEskHOWEmOPWIDCLJ5hOvxokbiInPqEOyaspuniPzrjVSzVWhCUYqxs0zPUNVVC5TOAVrO_yXRkBK_BrOjmKAp57zBl1UW_MCiIO69zwXQPhpHZVq15kCDG8brpUJh8fBXjcZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
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
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132623" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت
بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132622" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
برنامه های تیم ملی تا شروع جام جهانی از زبان تاج
🔴
بخش دوم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132621" target="_blank">📅 00:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132620">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">✅
فدراسیون فوتبال: در صورت تمایل امیرحسین محمودی رو جهت حفظ روحیه بر خودمون میبریم مکزیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132620" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=pbFTxg547clMekLNmCfRP5GpmHOWQ6Vx3m8KZzuADg-_9at1xXmPwRxNcjq__9mrF6OmwhUy3TdzgXdolCfeh8stW0E1MMEBYdgYnNF8h2Sqo_EdmbpoL1vAz727ySgH9e46zEC-1LGXeK9XVJC83qhKL0tVqf5gVfRmIT1-FPbsaMYoV21aq4Ef0vCYnqAr50yjBzgE0TLxr2MpPxqg09jRJLt4MsA4UEbfQoMOfr4tlPG_Ne2JEy4u2ZOHk-v3lD-bYOlsTz_-Wz0Zz6FnbqiFqsZ_f6VkfUQ1SJqjZgPk5TiolF3nsE-eq5gf2ZZaQQ_-Ryhg0Hr9wi87peoxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=pbFTxg547clMekLNmCfRP5GpmHOWQ6Vx3m8KZzuADg-_9at1xXmPwRxNcjq__9mrF6OmwhUy3TdzgXdolCfeh8stW0E1MMEBYdgYnNF8h2Sqo_EdmbpoL1vAz727ySgH9e46zEC-1LGXeK9XVJC83qhKL0tVqf5gVfRmIT1-FPbsaMYoV21aq4Ef0vCYnqAr50yjBzgE0TLxr2MpPxqg09jRJLt4MsA4UEbfQoMOfr4tlPG_Ne2JEy4u2ZOHk-v3lD-bYOlsTz_-Wz0Zz6FnbqiFqsZ_f6VkfUQ1SJqjZgPk5TiolF3nsE-eq5gf2ZZaQQ_-Ryhg0Hr9wi87peoxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132619" target="_blank">📅 00:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132618">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=lH9e-CuHHh0i7Smo2JSinnSr-gxtSAi-X-mhd9jOpIH5Fw5B1nr2nt57pUN0byBAdg5JNELhb5qjbd5K-6_H31sS9Kp4qpFc9xPc38Yp0_G1uGnTMcvd3fcMK6XT6md4MVFM4IADmBSoxRM-NcUnr2CU4tjbsHi1NF5fltOn4lBrvpJs2_bAQi18-NA9_21W-xsuBrexTjWgqXwPBFScmxC_CxmXKMkcQuvPSGPcBnPZzT5g0JzwcsJAhufgHb6WvtlARONp0Yt7jeCbO2a8YfQpPtg-AOul4STJanZssn78Rvpwswjoc7rSB4TZZ9p8vwrDO5IXMkX3EFolvt2ulg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=lH9e-CuHHh0i7Smo2JSinnSr-gxtSAi-X-mhd9jOpIH5Fw5B1nr2nt57pUN0byBAdg5JNELhb5qjbd5K-6_H31sS9Kp4qpFc9xPc38Yp0_G1uGnTMcvd3fcMK6XT6md4MVFM4IADmBSoxRM-NcUnr2CU4tjbsHi1NF5fltOn4lBrvpJs2_bAQi18-NA9_21W-xsuBrexTjWgqXwPBFScmxC_CxmXKMkcQuvPSGPcBnPZzT5g0JzwcsJAhufgHb6WvtlARONp0Yt7jeCbO2a8YfQpPtg-AOul4STJanZssn78Rvpwswjoc7rSB4TZZ9p8vwrDO5IXMkX3EFolvt2ulg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
با اعلام تاج امیرحسین محمودی و مابقی خط خورده ها راهی جام جهانی میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132618" target="_blank">📅 00:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=ZnbQ6-3oXHX_ShfUhwNRGShXXXxWAcgfSG0QDqlLyHou6yQN5IRSODWyAI2AFEOtwYDMbWHFVYDuI5M1MYM9krkjGrkdQ-9kDAe5iXPnvsTeuJa7kVYpQ3F0eaCXDmiwY-PFIGJZMFOLS_S_X-AN_83FF4AXjLHnaTDyanTKayR84wUusp1sIoHVOPHy3wqz-kkbIvf-DC10de1dGnu_sdPLx_eCc-FL-FYRNutDsO4SnX-RPkazgpsvNyS78MmjZYd1hbD8-7B_-KiCc51qwHaUMjPfSNH8AYumK74kel6DFPKKouQSuxfAdtqFYClWZHEAQcQWau0yheBjxdHMvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=ZnbQ6-3oXHX_ShfUhwNRGShXXXxWAcgfSG0QDqlLyHou6yQN5IRSODWyAI2AFEOtwYDMbWHFVYDuI5M1MYM9krkjGrkdQ-9kDAe5iXPnvsTeuJa7kVYpQ3F0eaCXDmiwY-PFIGJZMFOLS_S_X-AN_83FF4AXjLHnaTDyanTKayR84wUusp1sIoHVOPHy3wqz-kkbIvf-DC10de1dGnu_sdPLx_eCc-FL-FYRNutDsO4SnX-RPkazgpsvNyS78MmjZYd1hbD8-7B_-KiCc51qwHaUMjPfSNH8AYumK74kel6DFPKKouQSuxfAdtqFYClWZHEAQcQWau0yheBjxdHMvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132616" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SorkhTimes/132615" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132614" target="_blank">📅 00:03 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
