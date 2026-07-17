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
<img src="https://cdn4.telesco.pe/file/e8zjN7w8JGJmu-poBtrnMpWKpmwWog1meAAtnsUL6k1IMeQ0Cu3hUnYPL9n9b5sICKrH45WZZtowkTJ9aK03Aw3MNyNv43NRcIojLHQnRip_Qea52HdDg6E190xB4JHxhS4dohhosyv7-B3V_-Xcq2ATnjDMxarkmYCi-bMBFJneu6J0J5ONZk9p_9KEPtgXJYMWHG5E3fe2JmXIw6Hm6g_zd_ck6w2s7gVGJLWt28k8dMTcqMZM25p6MdfzzP0VWsLk1KyTs24TsngWq5uSNJveD_MBvqO-lX0JTqDpmGEbB5T3_Qxb9zc31gphFDKfid_PjoZCcWmCrd6kLVEwlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 14:08:44</div>
<hr>

<div class="tg-post" id="msg-136015">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
با جدایی سرلک، محمودی خواهان شماره ۱۰ برای فصل بعد شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/SorkhTimes/136015" target="_blank">📅 13:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136014">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/SorkhTimes/136014" target="_blank">📅 13:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136013">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
❌
چهارشنبه هم گذشت و اورونوف برنگشت !
❗️
روزهای پایانی هفته گذشته اعلام شد اوستون اورونوف ۲۴ تیر ماه به تهران برمی‌گردد اما هنوز خبری از این بازیکن ازبک نشده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/136013" target="_blank">📅 13:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136012">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/136012" target="_blank">📅 13:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136011">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❗️
یا تمدید یا خداحافظی!!!  فرهیختگان: میلاد محمدی باید سریعاً تصمیم بگیره قراردادش رو تمدید کنه یا بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/SorkhTimes/136011" target="_blank">📅 13:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136010">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❌
❌
تیم پرسپولیس که قصد داشت فردا برای اردوی اماده‌سازی راهی شهر ارزروم ترکیه شود، با یک هفته تاخیر اردوی خارجی خود را برگزار خواهد کرد.
🔴
🔴
پرسپولیس روز ۳۱ تیر ماه برای این اردو تهران را به مقصد ارزروم ترک خواهد کرد و احتمالا دو هفته‌ای در این اردوی خارجی حضور…</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/SorkhTimes/136010" target="_blank">📅 13:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136009">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136009" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">💛
آپدیت جدید اپلیکیشن اندروید MelBet
❗️
🎁
کد هدیه 100 دلاری:
giftcodeir
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
آموزش ثبت نام و واریز
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را فارسی کنید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/136009" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136008">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💛
چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت
💰
هنگام ثبت‌نام با وارد کردن کد هدیه giftcodeir بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SorkhTimes/136008" target="_blank">📅 13:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136007">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djP-ubPkVyE_qHxpq-iGqd6xgHp2IYVCsoNJPqB4oDxesqn7j5LhDYigyWTRC7tTxALNdipSUcyX_QGZtFEIekMIBOR4XVZd7TEhd43FI_0lEG0rgnJ8_OZodOaeVknOi9TAJoNXUPZ0tTh76VCRx3B76wGAACAqaCKVCYhvQ5MTG05YK-4PPEKpHCWIxwOZY3Y_Jowf5AcIaGaOQi06Q414HRdML-Kz35FipvdL8idv-5XFbT8i6WqPgNd8eD60dqfanAnvQ5_Pz8VWhsGaLSZFRqvjHBfDu0K9y-ha_XUvh2sfYK0n-cmUQxqoiYnx3smyYSvYIMb-8Cd2Yp0gRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
چرا هیچ خبری از این بنده خدا نمیاد؟
❗️
حتی باشگاه پوستر خداحافظیم نزد براش
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/136007" target="_blank">📅 12:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136006">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7N44HXqF-ajL0GSSD5HBW3Y1a0ufa4d3mhk5_cjIk9e2HavhkZMvRnoxw1Em59cOosrzb2SB5qXCq54NZylqDBIeYRTC10SuzswSnSGOgtdZo3wwtLVu2Y-Svdfr0ffDvFZFiSJocQSms5MOALN2je9KmffCqHuEZUDy2d9eI3YfwMQCLGR8LQVbmHJTEqhxTeg5O1zzcrVymIi_rjmzeuYHk4jVPrWr38LlU-xJnXaetSLf1xmw9GmZvus_ZTooGYXKkD1S3z0viADOxbehqnIGzAg7Q9PEna-bbmE8H9-GzCQHh1VPsNCqwUZOAlQ0U4-KRYEIRr8EcYcVyrz5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووری
/ فرهیختگان
🔴
با توجه به بندی که در قرارداد آسانی با استقلال وجود داره پرونده حضور این بازیکن در تیم های دیگر در لیگ ایران منتفی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/136006" target="_blank">📅 12:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136005">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/136005" target="_blank">📅 12:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVvYS_f_tznA3I1LhX5GuVp61JIhWIobVei4J6E_wNC9dKhhcI2CwInx_VF4lnCnBXzop1eVNP0dcZXqvPdU88Q7UgoIlFU6D8JWT6opm6t7a-hBJRUTV71c4h5bq9mdH38jvWkq6LBcAjK3naplLayqDhIA_nE0s8kr5_w3HamH0x0M28KKlOslqwq3n1QLxhhl--mPonWwYCURwsYEzt2pxkyOj1qS453p9JHUQzmSAZmt0HV0yS8APmJ9hdwyrSFk7DTU6qg-S1E0-U-WpHNkvothqMXS7SwNCkcFJ_aILcJtz4LmzKjuy0LH0Nn2HxQzgDwZCAAnkza8cAU1ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ابوالفضل قاسمی به پرسپولیس پیوست
❌
#پسر_پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/136004" target="_blank">📅 11:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/136003" target="_blank">📅 11:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
برای این نتایج ۱۴۰ میلیارد پاداش گرفت؛ واکاوی پاداش تعیین‌شده برای اعضای تیم ملی بابت راه‌یابی به جام جهانی؛ رقم قلعه‌نویی، ۴/۵ برابر قراردادش!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/136002" target="_blank">📅 11:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
✅
فوری از سپهر خرمی: پوریا لطیفی فر به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/136001" target="_blank">📅 11:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
❌
فوووووووووووری
😀
کانال 14 اسراییل: پل و راه اهن و فرودگاه و پادگان ها در جنوب ایران بمباران میشوند تا جنوب تسخیر شود. بزودی نیروهای امریکا وارد ایران میشوند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/136000" target="_blank">📅 10:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
✅
باشگاه همچنان موفق به فسخ توافقی با بیفوما و گرا نشده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/135999" target="_blank">📅 10:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✅
فوری از سپهر خرمی: دنیل گرا به طور قطع از پرسپولیس جدا میشه مگر اینکه به لحاظ مالی به توافق نرسن چون سلطان یه فصل دیگه قرارداد داره!
🔴
🔴
البته به نفعشه یه پولی بگیره و بره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/135998" target="_blank">📅 10:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135996">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">📌
۴۰۰ هزار دلار کمتر از ایری برامون تموم‌ شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/135996" target="_blank">📅 10:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135995">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">❌
❌
احتمال خیلی زیاد امیر رضا رفیعی به علاوه 60 میلیارد با لطیفی فر معاوضه میشه و توافقات انجام شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/135995" target="_blank">📅 09:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135994">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXu0zze-hcq5P74IwKe4cE4U-X6lFrPiV1nJwEJx6Ns0-edfGVSOyACIS7-u2Bz3DRplYWw3YMv3NR23stjz2OJIxvl-q8nrXQtmvL27Cnt5gk0ivyOjKS4A2h79taG3SzVvbSdd56KDb_RboqiNNF8lKashbpHaDVVrhw2gBLTWz5v8cAehiGn2qzbI5d7SWUEIo9FFYMmXIABXrnxrWibtO8xKdy5CMeEHhSbr7KKVW09J3Q1xP9BJOUwzS-M0POri6wxSZ48rJ0YFZbkXb8Qfs3ABpXUMoY2nZ2bpepzVK1sxl299XRXisgZhVzyyz_RCpb5h6FkItmGB6suAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برج ۸۰ متری کنترل دریایی چابهار در طی حملات آمریکا بطور کامل نابود شد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135994" target="_blank">📅 09:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135993">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/135993" target="_blank">📅 09:14 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135992">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
داورهای بازی فینال و رده‌بندی جام جهانی مشخص شدند و علیرضا فغانی در هیچکدام از این دو دیدار حضور ندارد.
❌
بر اساس اعلام فیفا، اسلاوکو وینچیچ از اسلوونی دیدار فینال جام جهانی بین اسپانیا و آرژانتین را قضاوت خواهد کرد.
✅
همچنین ژسوس والنزوئلا از ونزوئلا،…</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/135992" target="_blank">📅 08:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135991">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/135991" target="_blank">📅 08:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135990">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCcIPbr-5fg63neHXWqp3wT2NZVGI78RaYFrPlqhYclUbwIzLU8kl_wu96B3e8Vm_2OJ-JGo2Av9F-pHdJWrswTgufdela3KCC5U1QKbB844bLDnKFcuW3YBqcESXg6XXz7ZjticQQbaV6fSnYUI6aep9ABuxShonu3Ie7Adn2Uo_YfFYpd7rC_BNPPAHduvMbC-0ceNlhznZKcJw2eLn4IwgwXEkNI7n6RKHhRvhGzpDYKyqLEUuJpgZSU9NJUGzRPRxfgAh9bJQSy-8r6wovPvWvcBlO5WY2eiEU9UbZ_LDKF1-pXIRfRsb4tvv0bWDu6FP3uVwYO3ptzhObequg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پرسپولیس ممکنه زندگی نده، ولی
شادی میده
عشق میده
اینه داستان سرخ...
❤️
‌
سلام صبح بخیر پرسپولیسیها؛
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/135990" target="_blank">📅 08:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135989">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/135989" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🪙
اپلیشیکن اندروید سایت جهانی لاین بت
💳
واریز و برداشت ریالی
🎁
هر دوشنبه تا سقف ۱۳ ملیون تومان بونوس ورزشی
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
https://telegram.me/+dukgrB6-zGsyNGM8</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135989" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135988">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGhNcUId5ZBBqexty8ohXSu3lJzkntAzFLSZIm4BK9rFDWR0Dkr0Z_yue0gPNzaq7Wq_CYW1JGGJyUfLkhMamkkUR1m2HBGPUP9l2n8lUexbbT6pt6Gt7CzFTno3qBQfIPbxVlt39E2Jkp-Dq9fMU6du8IH7dURmVl0ek247Y98n9tmNPwQQ74ODimjtgIbB59NTyqG3wI41XhynZIKnV7brwiUr-jnES7LZy75tVcvO8fffx4bPVRCfmOZTr2DMI5metv_OGbXIjdARI7TzCAsrlwlTU5ZRLmnbUy7j1B6Psica5i3th_74OwmuL_-njrFIsfHPU2MwGi16A120Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
به دنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
🌍
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://telegram.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
Ⓜ️
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/135988" target="_blank">📅 01:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135987">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/135987" target="_blank">📅 00:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135986">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❌
❌
تمام راه‌های ارتباطی به جنوب، فرودگاه، پل‌ها، راه آهن و... دارن دونه دونه نابود میشن! آمریکا بدون هدف کاریو نمی کنه. یه سناریو بزرگ و احتمالا حمله زمینی پشتشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135986" target="_blank">📅 00:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135985">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135985" target="_blank">📅 00:42 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135984">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
دقایقی پیش ایستگاه انشعاب راه آهن بندرعباس از سوی دشمن آمریکایی هدف قرار گرفته شده و ۲ هموطن مصدوم شدند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/135984" target="_blank">📅 00:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135983">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
یه خبر نصف شبی فوری، شنیده ها:
🔴
برخی از کارشناسان حقوقی معتبر به باشگاه اطلاع دادن کسری طاهری میتونه برای پرسپولیس بازی کنه و باشگاه داره مجدد واسه جذبش تلاش میکنه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/135983" target="_blank">📅 00:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135982">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135982" target="_blank">📅 00:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135981">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135981" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135980">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
آمریکا پل کهورستان بندر عباس را هدف قرار داد.
🔴
این پل، بندرعباس رو به شهرستان بندر خمیر و سپس به بندرلنگه و سایر شهرهای غرب استان متصل میکرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135980" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135979">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">❌
آمریکا پل ارتباطی بندرعباس و شیراز در جنوب ایران را هدف قرار داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135979" target="_blank">📅 00:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135978">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✅
✅
خبرگزاری تسنیم : آمریکا رسما حمله به زیرساخت‌های ایرانو آغاز کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/135978" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135977">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
فووووووووووووووووری
⏺
ارتش اسراییل: آمریکا در حال نابودی زیرساخت های جنوب ایران است تا به راحتی به آنها حمله زمینی کند و سپس به مرکز ایران برسد
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135977" target="_blank">📅 00:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135976">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
🚨
حملات در جنوب کشور شروع شده...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135976" target="_blank">📅 00:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135975">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🔴
موج جدید حملات سنگین آمریکا به جنوب کشور آغاز شده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135975" target="_blank">📅 23:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135974">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmAlTus75WOFwjwKC3ePAxQ94igaPTJBHZShox072lop2Rq3oW0moN4ETH9sSsbtdZfS7gXK2KvmF8iMvNBlaRJe4ypYbunV5XDas2ys5Mz6oLxf0vjtJS8KxhNVSGbYMy5C1vVoxFoyynlaboNmp7AQPYeGMpkgnEmvcDegtqagEnTT5VwvZUAVetr_p3bFREMWiLjSTC30xv3tqb7XDc5dl3t0DYP3pZjJgUPjJENwYfmFRLfyOMR_jWkUI_y1BiNaZmYCc4IDy-nW-Z0s-QoZHiCqsSOf6hNMs8emG5QEw9dhYg8bMHRainPsKORx7-svbxK7hOE1JavCtVrgHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حضور رضا جباری در تمرین امروز پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135974" target="_blank">📅 23:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135973">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTFwfa1i9IDryaJfE03IjcGgI3leV5ICBpEVq2F-4-FfjFCchfM-BKf4c8dDimcl1hvSUi6gk64JjqI6DGhOmMycjg88s1ug9Y_483-3JrS-Ct9GQPXaoaBExm-AQQpZN6WX6P1wIhMZx6lFdF6g80MtZqbeyCSa5U2UhEY61VkV4BFvUKSe43FpME_HeWXbuOslRe4PLGu2eq0g6dPdxJH1IW_sgXqyf4XisA7o38kEA8YDcSZH6MFwifDK8Rf7vG2CwLlBKoEz4BnrLXsHedHEhCfpqmzjf8leKWqUm9a0QwyVhrUyH8VIHg2etSF2yobrAYwMNzytD4y-uZcLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش تصویری از تمرین امروز پرسپولیس
با حضور علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135973" target="_blank">📅 22:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135972">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/135972" target="_blank">📅 22:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135971">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBMJYUCoB008B2j_lHaplfv9iih5zVVrpU-4bOC3Ex-VsbDwD7glcmt8ZPqKyb4laQ1yYJ92vFyAbjuhiFgIZ8a_uPrm5oBjgaDz1ax4QMLiDe_glCS6xbpJ0CFWooB-xKgmJWabJgwPvDj_mEcaAqYpiOmRJoYjH5IaJFISXDO1XfG8Wjc9PYHANr5BXtrUZ2YKgQA03suHaT9NOygFdxnDlrvWO6UVvYkSIxpdvgJmyLv6_aZIEH9MjCxePwSksEMkHVeyYQxALtKxaIytCMyYKJjq628py5Wppjx6rZ_5riG9ghiye-ohVdseG3vqi0lisYpERuauNpbCv5pw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان:
✅
وحید امیری 38 ساله به پرسپولیس پیوست و کاپیتان اول پرسپولیس شد!
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135971" target="_blank">📅 22:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135970">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
صنعت نفت آبادان با برتری 2 بر 0 برابر نیروی زمینی در رده سوم جدول رده بندی ایستاد و حریف مس رفسنجان در دیدار پلی آف لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/135970" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135969">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135969" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135968">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#شفاف_سازی
🫦
📌
ببینید دوستان لطفا به مطالب جهت دهی شده توجهی نکنید این مطالب رو رفقای اقای زندی میدن بیرون که باشگاه رو تحت فشار بزارن، همونطور که چند روز پیش گفتم و امروز هم اشاره کردم باشگاه خوب نساجی نقدا پول رضایت نامه ایری و طاهری رو پرداخت کرده که بتونن با دو سه برابر پرداختی شون به تیم های دیگه بفروشن این دوتا بازیکن رو…الان که باشگاه با علیپور تمدید کرده و زارع رو جذب کرده،مدیران نساجی الان زیرش زاییدن چون سپاهان سقف قراردادش ۴۵ میلیارد هست، استقلال بخره هم الان به کارش نمیاد، فولاد هم بودجش در حد سپاهانه… جز ما و استقلال کسی دنبال ایری و طاهری نبود که بخاد پول خوب بده الان به گوه خوردن افتادن مدیران شون ولی با این تفاوت که الان افتادن تو فضای مجازی و دارن کصشر تلاوت میکنن تا هجمه وارد کنن، بگن ما موز میدادیم کیلویی ۳۰۰ حدادی خیار خرید کیلویی ۲۰۰ اقایون جای این لاشی بازی ها بازیکن رو به قیمت بفروشید که اینجوری قهوه ای نشید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/135968" target="_blank">📅 22:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135967">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❗️
قرارداد علی علیپور تمدید شد
❌
قرارداد علی علیپور، مهاجم باسابقه و ملی‌پوش پرسپولیس، پس از توافق با دکتر پیمان حدادی، مدیرعامل باشگاه، به مدت یک فصل دیگر تمدید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/135967" target="_blank">📅 20:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKEF5gFyolum1JOP3Ub-2UoH6Htw6zUC97EpIOEVoJffuAC8SsYvcGHLn5HEzDjcsTAfE-kEBpjAfRnKSv3HTZexMQUjvUopMLty_cQGSRZgVW_dxtvTmE1ttzPirtW_VTfxGG1Ek43-BJ01N_OHd7szYxpfOv5BGp245TPu5N0kDyjfTgPZ5pOE5u7aOSj5SJ0j1DXj9NRpYIsONC5b0bVLoTMMgXjwDWGccFTxHCJJKSykgbazLqnlCMluhgFCr67PEIBhNxidzuIz0CPV7N9GZRxasJXc8Z7UBRLr7japEU2mdS_aAJfHk-v13K-UuPkNW8nvmKzoGuV9M7G5CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه پاکستانی
😀
اکسپرس‌تریبیون:
❌
بعد از از بین رفتن تفاهم‌نامه بین آمریکا و ایران، پاکستان تلاش‌های خودشو برای کاهش تنش‌ها و ایجاد صلح بین این دو کشور متوقف کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/135966" target="_blank">📅 20:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/135965" target="_blank">📅 20:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانالی که همیشه در مسیر ورشکست کردن سایت های شرطبندی حرکت کرده!
😈
آمار ثابت 90 درصد برد
✅
فقط کافیه چند روز فرم هاش رو دنبال کنید...
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135964" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIYxujD51Os8alk_CLkAuctfq9FBeG_MHqU_3iX7M780FpaVqKCsSbkte23plDIe4gm1AS14guk70WZCoyCmAgWTAGoCWVLTf-DK4L29_ktNNksT99vmVK2o71fwlzOQK8I1qepSDlhj8QDAW96Fbr29i0nwLkUCel8q_yf-bvm2Jlh1YqDJPxWWvKyXIi3L2bGByGJ8ae-wi2YDlQc6mbPD-0zj9cHUcawF4XXgnYqdcce21y-tfDDkhGtbhhQ07TKiNWrapjOu8wldsbBgUyB9BkdTJ8WuuuK3laROeYMsqnNAL6EE5h-1rBn8Lb7lBOWHaQgEV5wSJW9TZyD88w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip
@aron_tip</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135963" target="_blank">📅 20:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ0dRNmoY-cCQaJ56QzYr_DYgpZHU6k3zxj_jp7fglR65lMAO1IxZzr34hprXxk5Ly9TXk2FKw_ue-MchmaBszemQMPbGFSfW1fvIFFCo7ulgy156AVxxyhkU0VFkPnaJdFISZYHpRZQA4TxNn7XkDDAefbRfaB9BRDjLSeb3MeYOW2JSsApViLavqj3hawGp4_0Gh8hcWiNZnwglwpGp4xr_7GWg2zcpGLf3bxTnS1p8NckZfwSc2CuZEJTwG9-aVxYZQjpG8TmUPVsLnuqG1qLgCVEMokok2Gk9EZ30RRRszYI6y03weEV0_shs_JJ7wCwhIg6OjwXjBewsGCLGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم ملی والیبال امروز تو یه بازی جذاب 3-2 مقابل آلمان پیروز شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135962" target="_blank">📅 20:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/135961" target="_blank">📅 20:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YljUqQr6u2JAAY6dBU2maJIs4BZ27NTbYfdI2YOSd9jh5IT-KjlmwXar-Gmg8IbHVzuZU3-FznTlcb8wOvrhLzWiAbgAz5LeY0FXyf7gECM5ihIlOGUTXRCtEhVAmYUuz-KfEGkAIn2CMgM9DqoTYnTcKGjN6iPPZKLDYUsjWJKmBF00HnqGt8IiRL1878SLf6oHHuzOK6qI4AyD339mEG_ZzTKiY_o-3SFcKCsnK6WWjWr1fHdYJ0pjUa3DJu_2NdmbjkQsXElVFNRpAEStOsycGReQo0ORg5xMLQwkSAi_daI_JSfqqUEGZZZw_bmjj3MBW3PSfpUVMozgLCqbGeEM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e071e1ff46.mp4?token=B8eG4mhb300iXezVwD1eURbMZQsoH2wYnXiezzNAJQS9rm7RVwYqzS0jTmoOXMfzgIce_WBTLjc60NhucVHyO81sUwnp7xl4guArF1Zp9SqXn7NvwBOABqMr9kpi04cRGpVVEqQYnENKXpeFcjmkbmSmQc5VetkGZOmSEqfUVskwXae2wyRU09qxsDOJtl2BXvOcp0rse0h95M0XaIuUeY3xwBDo-8asaYzHmT1bBbXZaD5NvY85gdVri42zBp8HY-pnJCGAEpsrlXo3d_lqMGdGLV2CbVyqQNLfnFOAPTGu9TBHM-Gky6nUWDz_pngWNSg5DSbOmg_Lvig5WN5YljUqQr6u2JAAY6dBU2maJIs4BZ27NTbYfdI2YOSd9jh5IT-KjlmwXar-Gmg8IbHVzuZU3-FznTlcb8wOvrhLzWiAbgAz5LeY0FXyf7gECM5ihIlOGUTXRCtEhVAmYUuz-KfEGkAIn2CMgM9DqoTYnTcKGjN6iPPZKLDYUsjWJKmBF00HnqGt8IiRL1878SLf6oHHuzOK6qI4AyD339mEG_ZzTKiY_o-3SFcKCsnK6WWjWr1fHdYJ0pjUa3DJu_2NdmbjkQsXElVFNRpAEStOsycGReQo0ORg5xMLQwkSAi_daI_JSfqqUEGZZZw_bmjj3MBW3PSfpUVMozgLCqbGeEM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل چند ماه قبل پویا پورعلی به پرسپولیس با پیراهن گل‌گهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/135960" target="_blank">📅 19:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=NIYJL1Ty1q48y_N4UYfDJRa7KRp_w4hUdYf6MqXem_Y7miAA68f80_-GdBBAPUHWUqVyPbzc-pP5xSNs1UpDZqVgRmTfLGcVhRsd20hxaStSf3aKtkWQPT1QUNn9szZVrfo3kUfDwVK2_AiapZGYDIHbxxrvdDiFmwOTlRlPDf1y8dpduUgS5lQ70iPG8-R5kXyH5fVXPK6yjfo0NUSHSBSs5XKb4q6GtCmAWo-R_vQCaAYrzymBzF3znnPmzUNGXP09U7xCBcpyhGbs_xnsc9-tXvPVUk6DYMQ4NxdLhURjotqU003gfkfOaDcun1r6Ko89H_nbd0zYA09Kni6jXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/664e6b20c6.mp4?token=NIYJL1Ty1q48y_N4UYfDJRa7KRp_w4hUdYf6MqXem_Y7miAA68f80_-GdBBAPUHWUqVyPbzc-pP5xSNs1UpDZqVgRmTfLGcVhRsd20hxaStSf3aKtkWQPT1QUNn9szZVrfo3kUfDwVK2_AiapZGYDIHbxxrvdDiFmwOTlRlPDf1y8dpduUgS5lQ70iPG8-R5kXyH5fVXPK6yjfo0NUSHSBSs5XKb4q6GtCmAWo-R_vQCaAYrzymBzF3znnPmzUNGXP09U7xCBcpyhGbs_xnsc9-tXvPVUk6DYMQ4NxdLhURjotqU003gfkfOaDcun1r6Ko89H_nbd0zYA09Kni6jXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب علیرضا، پسر نابینای ایرانی اينجوری با گل آرژانتین ذوق کرد
❤️
🔴
گزارشگر اختصاصی هم داره که پدرشه...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/135959" target="_blank">📅 19:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135958" target="_blank">📅 19:17 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">✅
اردوی خارجی پرسپولیس در آستانه لغو
❗️
❗️
در حالی که تیم فوتبال پرسپولیس قصد دارد روز جمعه تهران را به مقصد ارزروم ترک کند تا یک اردوی دو هفته‌ای را در مسیر آماده‌سازی خود داشته باشد، هنوز شورای برونمرزی وزارت ورزش مجوزهای لازم برای برگزاری این اردو را صادر…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135957" target="_blank">📅 18:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
ورزش سه: تارتار به وحید امیری پیشنهاد داده به عنوان دستیار و مربی به کادرفنی پرسپولیس اضافه بشه؛ اما امیری فعلا دلش میخواد بازی کنه و دیروزم داخل ترکیب پرسپولیس قرار گرفت تا خودشو به تارتار ثابت کنه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/135956" target="_blank">📅 18:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1eda321934.mp4?token=buoiHGUQNbLJSgu2kKMDDm5_05vN4fldYMriVsiDFDQ-h0sMAkld7dzkH-2JHGhE7p_FujoQTiezIOoe3d_dsDT_kF3KUtQEbCVSW22msnepZoTCiC6n77LB-TN26sldR834MpXjN70q_59eZCcdpd-ljS_w3FrCt1kxgE3tCdEmIgNBNQO4HHrB-zbimOzL_ADihGHXHDX2llzThj18aNA_OCVEGzwG9Hsl7pUMTQOeq3P2HyxMaNRH35YCKy6UVITzI3I0rvkLsqaL_DZuQUSIx3uYiVa50Ax2eK5d0tkSRum7iID4JGuoGbbiCGCreZNLYDxX_AC-IlM_WYPMGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1eda321934.mp4?token=buoiHGUQNbLJSgu2kKMDDm5_05vN4fldYMriVsiDFDQ-h0sMAkld7dzkH-2JHGhE7p_FujoQTiezIOoe3d_dsDT_kF3KUtQEbCVSW22msnepZoTCiC6n77LB-TN26sldR834MpXjN70q_59eZCcdpd-ljS_w3FrCt1kxgE3tCdEmIgNBNQO4HHrB-zbimOzL_ADihGHXHDX2llzThj18aNA_OCVEGzwG9Hsl7pUMTQOeq3P2HyxMaNRH35YCKy6UVITzI3I0rvkLsqaL_DZuQUSIx3uYiVa50Ax2eK5d0tkSRum7iID4JGuoGbbiCGCreZNLYDxX_AC-IlM_WYPMGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فوووووووری
:
🔴
ماشاریپوف و نازون از استقلال جدا شدن :)
🔴
پ.ن فقط از استقلال ی سهراب مونده همه رفتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/SorkhTimes/135955" target="_blank">📅 18:19 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
✅
اورونوف چهارشنبه‌ وارد ایران خواهد شد.
🔴
پیشنهاد ۳/۵میلیون یورویی الشمال قطر صحت ندارد.پیشنهادی باشد هم با میلغ بسیار کمتری است و از قرارداد مالی او یک میلیون و ۴۰۰ هزار دلاری با پرسپولیس بیشتر نیست/قرمزانلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/135954" target="_blank">📅 17:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135953">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
قدوسی در خبری فوری
❌
احمد نور میخواد برگرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/135953" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135952">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDUbeCV5eXojyyVDftf9O3D1cxtI7fHRAiU9AchRy1ft8XOMIxpvpk6yL1ESUJL1U8JKNIT5VclsN1yiroy8iyojO72vacLXQzP_2N5KpkkwCoLHZDBWZiEkyk9tAbi1K2iRrzw-WUsaN8czOGxG1p8cLTvKAYbodOL_NXtaEPliyGiSs5m1ql7pl70zQgxW92O_DwTcgyWeRvrVVfjGqAWXA5JZzih4SUB4f41H31hHgr_vUQxLc6-qFk4gTcI3fmjCRMg3rXdqmrO16LYLixHXvF9gN6UNfcLvmNReleyOmZOc1u66QXgZV-8Pr0N8-_gGkQ1pmTpJ8gL0JUdWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ابوالفضل جلالی بعد از پیوستن به پرسپولیس یه میلیونی شد
🎉
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/SorkhTimes/135952" target="_blank">📅 17:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135951">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✅
✅
سامان قدوس در فهرست نقل‌وانتقالات باشگاه پرسپولیس قرار دارد و سرخپوشان به دنبال جذب او برای پست شماره ۱۰ و جایگزینی با رضا شکاری
هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135951" target="_blank">📅 17:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135950">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
شایعات؛ محمدحسین اسلامی در حال مذاکره با پرسپولیس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/SorkhTimes/135950" target="_blank">📅 16:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135949">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
کوشکی و اسلامی توسط ترنسفرمارکت بازیکن آزاد اعلام شدند
🔴
از طرفی ایجنت هر ۲ بازیکن با ایجنت جلالی یکیه
👀
نظرتونه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/SorkhTimes/135949" target="_blank">📅 16:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135948">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/SorkhTimes/135948" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135947">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/135947" target="_blank">📅 16:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135946">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVYch2lIQ10BeF_JTg5KYVeOsiIqC3IBTTpTYVvpme9BFa0LTHbDv7dw_JJlNwL5WuQvuCl8SCLYEnn4ro-Sf0B2TK2eXxwHAV2u1pOkUGNp6if8-2QYfIvFB4WpaKi-mtPTmCcG54LBix62I3rGMWnqhwax4yX4tEFZejQMw_aKKGvbwkSg-tuzHBLettFXlr0iVZNjELgB4H9jIDriqSvvG1OXNLVPvyprEu4uQOpYNQtRU5EFT3lQl-s3eyqg2Oi8VmVLxA9KCJVbmIx8_Ip-leT96lR4f2jW4tqWoQcoY9AmmrKmPVTseyqYvmWP41Gh7-T9pQvTrDxaECItSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ایجنت مرتضی اومده مرتضی رو دوباره به لیست پرسپولیس اضافه کرده ؛ باشگاهم هنوز برای مرتضی پوستر خداحافظی نزده
😑
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/SorkhTimes/135946" target="_blank">📅 15:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj2VLl3glEhawEWtaFD4Fhw2DYiUD0I3rrbkSEKUXeTRuQSwFxtntaFQ2V-X3xzyFIqdyH9kfcep68VoqrD5alQh5hjkiCrSfIwdQ_GtuoklI_UmUeBOCxHY9yEEcffrs3J6QQKkh2KsmPjqD86bten_t0-gyj9YAjjGl-EjfEGrzP_Yx5ARKmcU37tk40qI9fpMzLlXmMYVs4CKof5MZhIrFxo6hom6UHbEfo-XtOMPqhFkn81agys8to1opdBf59iHX4zEHkc0GjszgC3SvQaQwvPm9crbtSnNW7EiYhWTJMlmSzl6x_BRoe9zlUcPc5GltIZqmFUAs64tGpJDlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سامان قدوس؛ بمب بعدی پرسپولیس؟
🔴
🔴
ورزش سه: پرسپولیس برای جذب سامان قدوس هافبک ایرانی اتحاد کلباء امارات درخواست داده و این بازیکن در لیست خرید سرخپوشان قرار گرفته است.
🔴
🔴
قدوس که سابقه بازی در لیگ برتر انگلیس با برنتفورد و تیم ملی ایران را دارد، یکی از گزینه‌های جذاب پرسپولیس برای تقویت خط میانی محسوب می‌شود.
🔴
❌
باید دید مذاکرات پرسپولیس با ستاره کلباء به کجا می‌رسد و آیا شاهد یک انتقال بزرگ دیگر به جمع سرخ‌ها خواهیم بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135944" target="_blank">📅 15:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
✅
عملکرد پویا پورعلی هافبک دفاعی جدید 30 ساله پرسپولیس در فصل گذشته لیگ برتر :
🔆
21 بازی ، 1 گل / نمره متریکا : 7/03
🔴
سابقه حضور در گل گهر، تراکتور، ملوان، ذوب آهن، فجر سپاسی، خونه به خونه، بادران، شهرداری جویبار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/135943" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135941">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abNRloxGndf_snvasInb6FDNVnx2d8QPyK6pxg_xaK2YqsuHKk3q7uVX-IDtapt_8g8cHAOzz4zLOgKmHtOlLp_G1Tfr2-szqw7ns9sJ1fGseWzaJP11PvuS7HTKnY6HPxkAweLxibb5qhEarG3gvFtcLfQba5Gfq7VrlsyoxCB82Kk5v2EzesvGh9qdWoEiuzCloWPjQItPv5E4eaev6SQ1VUDdcN29VTdLF3MlaTJC4ciuYI9MafLVEdh0kbLiIdE7h0elSJLk5MkuwlwAwUZnzfCA8SCHBPBZXa0hSH86QENoWWz9IwpRDtrE9lsZyoUz7PENbgxL6t3NO4KoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
فیفا قضاوت دیدار فینال جام جهانی ۲۰۲۶ میان تیم‌های ملی اسپانیا و آرژانتین را به علیرضا فغانی سپرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/SorkhTimes/135941" target="_blank">📅 15:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135940">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4v0Rt4KXLYk0FBYpZ1ItfWY-j6sJIHkH4DJ17eDpLOCshO75U8xzSsRcHH-yyZZRrKxLzi15DFiUwOTnfELiZnnA9CNMQ4MDIfaZfEgHkVSqZA7HnyhECwNtzXcXvHjFc8NEeDDVqFpf_mklUzcy1rYQuEmdN12QCZOD03NfRRnxO89IjTFSRnpUr48xevid3iRSeF8NK0JK0arrW7u_ge2jtZFyvrcsXte2h-8RqLrAZ6n0UEtcp9qdUdmTK6zXZoKO82ZOYT7TOsM2R0qnRR1erUuSHg9IePdNycms2TuLP2TQyA7heBcAI4ETAN20xzlUuNeLfu5afgXEMD_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خریدهای لیگ‌برتری پرسپولیس تا به امروز:
مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/135940" target="_blank">📅 15:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135939">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝙷𝚊𝚓𝙼𝙰𝚑𝚍𝚒</strong></div>
<div class="tg-text">تو دور زمونه ای که فساد حرف اولو میزنه کسی که وظیفشو انجام میده باید قدردان خودشو پدر و مادرش بود...</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/135939" target="_blank">📅 15:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135938">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frompourya</strong></div>
<div class="tg-text">دیگه نمیتونی زحمات یکی رو بگا بدی خیلیا به وضیفشون عمل نمیکنن</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/135938" target="_blank">📅 14:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135937">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وظیفه اشه  دیگه دمت گرم نداره  مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/SorkhTimes/135937" target="_blank">📅 14:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135936">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVahidreza. Sadeghpour</strong></div>
<div class="tg-text">وظیفه اشه
دیگه دمت گرم نداره
مثه اینه مادر به بچه اش شیر بده بگیم دمت گرم مادر که به بچه تازه بدنیا اومده شیر میدی
😂</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/135936" target="_blank">📅 14:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135935">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/135935" target="_blank">📅 14:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135934">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دمت حدادی گرم که باج به شغال نمیدد</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/135934" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135933">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHamed 65442</strong></div>
<div class="tg-text">دم بانک شهر گرم</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135933" target="_blank">📅 14:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135932">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
#تایید_خبراختصاصی | #اولین_رسانه
🚨
❤️
پوریا پورعلی با عقد قرارداد دو ساله به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/135932" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135931">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
🚨
شنیده ها: امروز احتمالا ۲ رونمایی خواهیم داشت
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/135931" target="_blank">📅 14:42 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135930">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/135930" target="_blank">📅 14:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135929">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxZMh2wAup1U_3IlTLJGvRd5MtSsFR1ccnhjdHD_VOJ08brgxM4fm1r6In-81pf4EZ0WDvnl3EL6iiMKfvxT3Bt0p01jxg3ldfsnTTRJ--GmR4nquLNb8wPMczjADvsmGXceFcU17qCRgcLza_ZGcVjroQWf3Odr48iaDkZ97k1GKISWu1QB2HY0cNRo4itPQntmfTHkx_LkOtDvI6DfhoUn9KNlNLa9tJnOsSymui_CLKiYbuwoY5ED0TIfHWxV7RsMjOa7fo7_MC7reghAN3WJVB1UcAU5HtNPebOsybKchVfCNA2ifOUGlrqdQm6ZjJZCbCc7ejlP0vlkig3M2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام سایت ترانسفر مارکت؛ باشگاه پرسپولیس بابت رضایت‌نامه محمد مهدی زارع 800 هزار دلار به باشگاه اخمت گروژنی روسیه پرداخت کرده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/135929" target="_blank">📅 14:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135928">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LemY_JhWt7xsVUyd4Af1ssLKLibYoOaqbsfzyb8IlZRZMj3H--8zr_Nn-jUcCQcFq6YCDBJ4THl3NFBp2m0j5GQmssoWAxwcSuRLedloLCHzlQ7kze5Oy6K6IKSlI2s_aFaHwT-ilpaYNjQV38fceNd7Py50PtVjqxrsWRoOLDcWujyO30OFZFtcpMzmEwGv4p1AR59Mamf5buH4VNtgc9DfH_70fqS9pQa-F1K3cn6DKOvEV4vcIc-_hDk5LtbXBU_kTnYtx_fQP9P-Cy19RxTIowJo-LSJvB770Tn1YafxoayNSRT76lHYGgoqVyrIMgYuZ86atGJRWclaINbCmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135928" target="_blank">📅 14:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135925">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
فوری از فارس:
🔴
انتقال پوریا پورعلی هافبک گل‌گهر به پرسپولیس تا چند ساعت آینده امضا میشه و به زودی رونمایی خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/135925" target="_blank">📅 14:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135924">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">✅
✅
شماره پیراهن خریدهای جدید پرسپولیس
🔴
مهدی تیکدری: شماره 11
🔴
مجید عیدی: شماره 20
🔴
ابوالفضل جلالی: شماره 33
🔴
پوریا شهرآبادی: شماره 21
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/135924" target="_blank">📅 14:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
تمرین امروز سرخپوشان در سالن وزنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/135923" target="_blank">📅 14:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#تایمز_توئیت
⚠️
تو این مملکت دستت رو عسل بکنی بزاری دهن طرف دستت رو گاز میگیرن، همین زارع رو نمیگرفتن به خدای احد واحد خار مادر باشگاه رو یکی میکردید وسط فصل….
‼️
نساجی برای ایری ۱.۲ میلیون دلار و برای طاهری ۱.۳ میلیون دلار میخاست
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/SorkhTimes/135922" target="_blank">📅 14:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
❤️
رسمی؛ محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/135921" target="_blank">📅 14:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135919">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb8cg3xE3_IkdkhSiEf-3XvkRjJuENOOVuFyrPctMawqHT-a2F9dYsJj7OzMIKRDJBTJ4VgC5XjTON8_-A81vMUGofXExI5J5N2kf7ry2B3iV-HCDNpdgkShXqdHY6CiCQeoFQ07wJfle_zfUPZexByUHNB0c-hk7Edqa4VxoN7oRnqQXSntB4keIWEuEoo78588P8een7cBY3Z0UxXNTVirqCxy4ISKJX0OmkgmOs16w9-T_AHEXvWOnQSRQfzfCmNneSCK2KB6eIgO_3OnUsiixRGmzMFwlpu0CSyY-SHqD9qDxI52GppVLFMunAczGap2cyllqpwmiXbIlg2iRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
❤️
رسمی؛
محمدمهدی زارع به پرسپولیس پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/135919" target="_blank">📅 14:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135918" target="_blank">📅 14:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">#تایمز_توئیت
⛔️
❌
با یه مشت دیونه زنجیری طرفیم، باشگاه هرکسی رو میخره یه عده هستن فقط بلندن گوه بخورن
‼️
قبلا میگفتن بانک شهر گداست پول نمیده الان رفتیم یکی از بهترین دفاع وسط های ایران رو خریدیم (زارع) یه عده دهنشون رو باز میکنن که با این پول میشد ایری و طاهری رو خرید یکی نیست اخه کون گلابی اگر میشد مغز خر خوردن برن زارع رو بگیرن ؟! اصلا میشد تو بلدی بیا بکن یه عده فواره گوزو پر مدعا نشستن بیرون میگن لنگش کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/135917" target="_blank">📅 13:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
❗️
فرهیختگان : قرار بر این شده است که  باشگاه پرسپولیس قرارداد هافبک مورد علاقه تارتار پوریا پور علی را امشب نهایی کرده تا این بازیکن بتواند از فردا در کنار سرخپوشان تمرین کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/135916" target="_blank">📅 13:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135915">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❗️
فارس؛ پویا لطیفی‌فر هافبک گل‌گهر در لیست خرید تارتار قرار گرفت
😐
❌
پ.ن از گل گهر بکشید بیرون ناموسا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/135915" target="_blank">📅 13:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135914">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
محمدمهدی زارع در آستانه پرسپولیسی شدن!
⌛
انتقال محمدمهدی زارع ۹۹ درصد نهایی شده و فقط واریز مبلغ باقی مانده است؛ پس از انجام پرداخت، از این خرید به‌صورت رسمی رونمایی خواهد شد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/135914" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135913">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❗️
مهدی تارتار از مدیران پرسپولیس درخواست کرده با توجه به شانس کم پرسپولیس برای جذب ایری و زارع،اقدام به بازگرداندن مرتضی پورعلی‌گنجی به تمرینات تیم کنند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/135913" target="_blank">📅 12:23 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135912">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❗️
تارتار شخصاً با زارع تماس گرفته و خواهان اومدنش شده؛ باشگاه هم میخواد از اخمت‌گروژنی تخفیف بگیره/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/SorkhTimes/135912" target="_blank">📅 12:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❗️
❗️
فووووووووری
❌
فرهیختگان : اگر میلاد محمدی با باشگاه تمدید نکنه ، مدیران باشگاه از مدافع چپ جوونی که با اون به توافق نهایی رسیده‌اند ، رونمایی خواهند کرد
🔴
گفته می‌شود تمام اقدامات نهایی خرید جدید تیم انجام شده و این انتقال برای نهایی شدن تنها به یک امضا…</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/SorkhTimes/135911" target="_blank">📅 10:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-135910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
❌
میلاد محمدی همچنان تمدید نکرده و اخبار قطعی شدنش کذبه اما توافق داشته/ایرنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/SorkhTimes/135910" target="_blank">📅 10:53 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
