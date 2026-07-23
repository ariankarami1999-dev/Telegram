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
<img src="https://cdn4.telesco.pe/file/drVgZTvAC9RJxc242KpFiBczDNIezyEaUb7Vlum5STS5orbOJcm8Q0f-laJij_rgSXad3eOcJn18v5xoIa8P6iIcVkpqsb334QEb3Q5-iAxWo6Ae7e0kPqtMW5_E6XN0jKh9WHjeCaoDdgkZgRRy-CRkcAydTYApZ4SdfUkEk5yhhckHALsuy1LShWHObaTDqs69LZdu0_nmMOSWjGETADIjSR5EPZKvxiBwrQ4KjZna44JjIQskbnAFlP8wpR1UQOId_q9OFdwEZKy8hchMpOXIcmFWn6DGdxFz6d6RUuQhasGZGNZnyWog5im2WjvmvTLnGyDfmUMibz1zSfrDdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 22:30:52</div>
<hr>

<div class="tg-post" id="msg-136560">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
رفیعی خودش قراردادش رو با پرسپولیس فسخ کرده و حالا دستش بازه هر تیمی خواست بره. احتمالاً هم راهی گل‌گهر یا شمس‌آذر می‌شه و اخباری جاش به پرسپولیس میاد.
✅
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 215 · <a href="https://t.me/SorkhTimes/136560" target="_blank">📅 22:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136559">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">❌
❌
#فوری |ترامپ به شبکه 12 اسرائیل: من در حال بررسی امکان انجام حمله‌ای بزرگ‌تر از هر چیزی که در گذشته شاهد بوده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.16K · <a href="https://t.me/SorkhTimes/136559" target="_blank">📅 22:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136558">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 1.28K · <a href="https://t.me/SorkhTimes/136558" target="_blank">📅 22:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136557">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/SorkhTimes/136557" target="_blank">📅 22:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136556">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA-KnQTwQ-FW45qnbRjZGa_aucW-bWfmbubjwmDm7Qut_AQXGoKegYfqtYMS0dhJaQV4sRqnF4a3kt8RHqbd_q9zqBd_M3bHzwafD4L0f40odHMEzk0J0kHsufTNNtDcN2hl5mKwNy_eqDA9yYXxRUdPkLXWdoJy6LbMLBWDB17SWui7VLF1u8jaSGofSFjnA586tyK8B0i96W-1-i0B7ONlzE650V2mS08vTxI7UbGqhobH42VqtyqeRFiiUmZvV3t5Hmqz_MlZkYidgLTUXj10QGtBgtJ2-kVoIMIHkghw0gPBLiCYtOSRQJubYMyKoZBEPb_uFYmvW1eUvXwuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کاروان پرسپولیس دقایقی قبل وارد ارزروم ترکیه شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/SorkhTimes/136556" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136555">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❗️
قاب ماندگار بازی پرتغال - اسپانیا؛ دلجویی یامال از رونالدو پس از سوت پایان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/136555" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136554">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
مرتضی و کاظمیان با تیم به ترکیه نرفتن و جداییشون تقریباً قطعیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SorkhTimes/136554" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136553">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/136553" target="_blank">📅 20:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136552">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet.apk</div>
  <div class="tg-doc-extra">54.1 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136552" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🤖
جدیدترین آپدیت اندروید اپلیکیشن 1XBET
🍏
برای آموزش ثبت نام مخصوص کاربران ios اینجا را بخوانید.
✅
ورود / ثبت نام از اپلیکیشن
🎖
بزرگترین اسپانسر رسمی لالیگا
🔵
بدون فیلترشکن
از اپلیکیشن استفاده کنید</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/136552" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136551">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCJ9h8otFpJfFGNZuhnw_AR-svOaTDAuOqT15OtGgCHfyHAYVKtwTHEnoC5s5-9GyJbT2YfymQ9hymujbhQnaBh_qGxeo4m5yQZ_nUp87zP9dLUMrSYOJ0Yo33n2wWM6BJnSo0Ao9zQkKyTX6gJSmW8dlijf3_4UeKcb3cXj4jWp_rJPtPIBWlTQ4dxwIpSKjqH-xZ_qGcrbPIIAnUJEr9-evyR__U5FxSNRdWMcY670yJTBQOvp4hwn7bEH0-yTwr--fXawM8De2VyRPRJfVR2wU0isUCZ-RJAPiw9Xfd5UbNNpBFKsMQJPtOaBAcU3PTkuJRBPZOl3JsxhsLUxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">1️⃣
شما هم به خانواده
1XBET
بپیوندید
1️⃣
🏁
جام جهانی تمام شد... اما هیجان فوتبال ادامه دارد!
⚽️
🔥
🎁
پلیر ها پس از 5، 10، 15، 20، 25 و 30 روز متوالی، پروموکد Freebet دریافت خواهند کرد که تا 7 روز اعتبار دارد
🔔
آموزش ثبت نام و واریز
🟦
آدرس وان‌ایکس‌بت:
🌐
Link :
1XBET.COM
🌐
Link :
1XBET.COM
🛑
برای ورود به سایت از وی پی ان (فیلترشکن) کشور های آسیایی یا کانادا یا ترکیه استفاده کنید.
➖
➖
➖
➖
➖
➖
➖
➖
🌐
Channel :
@iran1xbet_official</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/136551" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136550">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/136550" target="_blank">📅 20:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136549">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/136549" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136548">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1w0NSHRza-53HRMHMIIJcmR3sb2UWVLLJaqIMDdNTNy4kPhS8wQrePd33O65HuiFZxML4EM6TZulW-eygZUiHIW2Rt0TaC3avngOWa1dVFGXs4o7NldElxWU0Nc7gv9t-7dG3Ui9j_tiO54g9FG9P9R1eisA6YO7KeDGx9ja6vrtDZRUvMRr2zpSKzxhkQTe8rNQeaxqqh7Q2i1NYMtrMqv6eF3Q630E25_bsA4fyPn84DqVK-2SDQLpw-UsYwT7s5Rnrz3aR1bY-1xKAbTz7D6MUziCjyht_lYNETxq1zdMCzhTmoctQN-8pb9m8DasStsyyx4U3feDrOefR3rpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
🚨
🚨
مذاکرات نهایی بین مدیران پرسپولیس و نساجی بر سر انتقال کسری طاهری و دانیال ایری به جمع سرخپوشان روز شنبه برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/136548" target="_blank">📅 19:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136547">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">❗️
❗️
هنوز قرارداد اخباری، ایری و طاهری امضا نشده/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/136547" target="_blank">📅 19:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136546">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SorkhTimes/136546" target="_blank">📅 19:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136545">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/np_C1r2cRguRy-pXzbUu9Z9WsRckZl_GflSNO5N-0C7vUa8cfm09kZ-PGYirfI9qJm2U2ZcSTVwT4DYPw0Bzw4YvG9WxmUurm6DuqI_umDTo_9eXrtGazYtBY1HRCzQ6lM-8lZhYAH0qYsIQNswKT9gAJGu7TvXdjSNZcaosiVJxxOTj5OzzpQEPXZXRXvzDmwTU7PtUIV2wB6tYjgIwTRewxt4f3xvOiUV9iW0q61F6kr1U5D9FTit6d0NEnPta4fANyN6EuWXbStyyTJt2NT2AJC9wZWcqdfQJ5mTOvdyxDejkGEE-lWFSwR5LGojJSulbMFBBdTRiRp3KHw4Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علیپور تنها بازمانده نسل طلایی برانکو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/136545" target="_blank">📅 19:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136544">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=Y11cOZXbEpkiuntUla8lffCiOP-YGKX8pIziYD505AN4e3nvIstZKpJlM3rrXaJNdjDBOIESufb811VJAxrFSt7PsGTbvlBYWXZ-5vCrNojYpXcNaDjziBgKIGZzFfTnuCSHtDpUN22RXDtBcV3PRTfhVe8iXIK-N6prZT1k8cpVHdHnM40zQsTRlJoWZqSJN-hTCzqJ1fhMkoj1JNgfCoGJV-GBoXt9bDMzVxYHUi7fwMfUKRsPFDXJbfWgxp7ruohuTN3GkrPanAtzsWSrWdzxUrIDg2B6tBH9lzZPn3-yqRwC-0Nn5xTWknqsfqyoE72DPsIHFq2N2jh9M2g8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feaf2d5596.mp4?token=Y11cOZXbEpkiuntUla8lffCiOP-YGKX8pIziYD505AN4e3nvIstZKpJlM3rrXaJNdjDBOIESufb811VJAxrFSt7PsGTbvlBYWXZ-5vCrNojYpXcNaDjziBgKIGZzFfTnuCSHtDpUN22RXDtBcV3PRTfhVe8iXIK-N6prZT1k8cpVHdHnM40zQsTRlJoWZqSJN-hTCzqJ1fhMkoj1JNgfCoGJV-GBoXt9bDMzVxYHUi7fwMfUKRsPFDXJbfWgxp7ruohuTN3GkrPanAtzsWSrWdzxUrIDg2B6tBH9lzZPn3-yqRwC-0Nn5xTWknqsfqyoE72DPsIHFq2N2jh9M2g8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
استوک صورتی با کیسه فسخ کرد
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/136544" target="_blank">📅 18:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136543">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_aFjZBo5ow1d4T4-Umj7RB4zOHKLHeH9kVYxmIZk1TsMR-nBnqOIq1Zf03pvOX1UcK1_GfMujRQvGtYJbVu9vBW7AFIibfKZJlJL4apIg76fF0G3lIOuMY27kOlL7JzRkBAawGOi4M1T7VyJQaYigJaisNOuXwr5putPsUIOpnwWaCXUb5suv_3kle83xfCqZtRA_uFiDaOqFZkoCeqAkA9JFMranl61ymszF3ZN6jHbFxZz8hvZvUXXfrMYHPgb6rjY1i7aTnZXH0UnpASiPZWAfBiteYEyU7gx_PG-6W8LbSLt04EGG4JDya7tqMlb-cu3eBlggAO4nGTlF8nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از تمرینات خبر رسیده پویا اسمی کاپیتان ۱۶ ساله تیم نوجوانان یکی از خوب های پرسپولیس بوده
🚨
این بازیکن در این سن با این فیزیک و قد مناسب شدیدا آینده داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/136543" target="_blank">📅 17:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136542">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPwTDtBCdzV4wuBbkYBThoV0fjdNB7hAEtEJ8JmSkVyB6ZrkWlRmnU1C2V9l3Jve7WYZaP1Mr-7FdlkVLfNjafKubJgWmkoD95DL8GrzPAqUyx6tFU1PsLsm2I69k06DGGlTUoEPv3PIWo2kCP-rjUJ7sHRQbXacGtmB0KGhGHDvYO_HRoTHmi4I-L5WvGIPbVdevHWFmhuwgyzQpkOSUosxmGQuK_nA2diITinsgmw51Z1z_bDgS25e8d3mApqrX_J6bkMmyCInipxjJ21_MFrqlF0uhX1RrAfSlFFOzqaNd4tcym-CkjPIxdeBoiTytJj0m2U7yMgEcmjm3TS8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
🇹🇷
تیم فوتبال پرسپولیس برای برپایی اردویی ۱۲ روزه تهران را به مقصد ترکیه ترک کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/136542" target="_blank">📅 17:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136541">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/136541" target="_blank">📅 17:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136540">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvHm2pmun6aKEgoY9u5r2QKamn3Tc_90uZ7MmIL5AwYri3fzFs-K9po6jqgGuwLYp5Kc88onRS1LtFBzRQDjVwjFhvsloNCBvOVpc3zZTV4ZyVoFd7KagKErmtcg-nBueBM4yhcpntQR-q0IBbIvonKv88_FPZdyjxkzKNKdZepUAs4wIrupRgEXyBLFLfUuGEaFdJUEj6oeav8Zvldoh9l_VckhaKqDtYzChZiLoDHcW7EZ_LeL4rGGHQq117-blKtXmRG1youUgr0MbyBLEiiYj5xSZ--J7RNIlFOURWiIZU3eUwYwSA5wCOr14pSM-Vq-KSQQzE9dIpTpf3RDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تیم رفت ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/136540" target="_blank">📅 17:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136539">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=D7P2wP8WtwNPI7M7YQQcsuCl7jLKO5nwiTDmpgwrzxtzJ9ROj3Hq-RDXl9FPTbP2FKk4AE35qnZwHYjfyg7_lxA2e2LgtZbGuGX8ubrTJcKDji2UGSVVjUxvqalhAg7S6nASPuvk-6M9o_aMdA3pRIvm924ma2qZSqqGMsS6Kd1EInzEb7l9ckrutHkm9fQw4US022j5nOxF1iSWRhdx10elEZf7HelXGkoSVIqe6lY4sOlrgCJ4zMLWbCw0xgRDRwE1Ie9C7aeZp4naUei9WwpXvsXNjAtE67SSPzkOlzLgX9FLzUsw3DOpQyJtLzj_qgYV27ocKa8n3f1BdNr3WD9iwhSCXwjofI-wunip5v0lOF0TK-YfZMPG6JCUUDfU7cXb4d2N4ASoEy-XMkf-LGR7vUIAYo00ikdQxSULuvy-qIoh7Tznw2_8SC3OinsbZRHhBChGGjSEd79tzeSqQ-H-DW65BC_8QxobmWXcmCkBRFzDc_NdF_8V2EGZjmP9BpUeieH3C1nAaKpSghANXyJB5l8OZqeRw1rRLPS1GsVBxJDfuFD0my0tNPBzxzBAE8XlP54b6Ha1iZ_vqo4ZYsWhhqzopaRdC9ic34mvQ6_ehFj_4GRG1-Zc9af4VBMDThJke_rn2IW9S1DR8xiORD2-qD0uAX3zhaJVAjCWiJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/875cf546b8.mp4?token=D7P2wP8WtwNPI7M7YQQcsuCl7jLKO5nwiTDmpgwrzxtzJ9ROj3Hq-RDXl9FPTbP2FKk4AE35qnZwHYjfyg7_lxA2e2LgtZbGuGX8ubrTJcKDji2UGSVVjUxvqalhAg7S6nASPuvk-6M9o_aMdA3pRIvm924ma2qZSqqGMsS6Kd1EInzEb7l9ckrutHkm9fQw4US022j5nOxF1iSWRhdx10elEZf7HelXGkoSVIqe6lY4sOlrgCJ4zMLWbCw0xgRDRwE1Ie9C7aeZp4naUei9WwpXvsXNjAtE67SSPzkOlzLgX9FLzUsw3DOpQyJtLzj_qgYV27ocKa8n3f1BdNr3WD9iwhSCXwjofI-wunip5v0lOF0TK-YfZMPG6JCUUDfU7cXb4d2N4ASoEy-XMkf-LGR7vUIAYo00ikdQxSULuvy-qIoh7Tznw2_8SC3OinsbZRHhBChGGjSEd79tzeSqQ-H-DW65BC_8QxobmWXcmCkBRFzDc_NdF_8V2EGZjmP9BpUeieH3C1nAaKpSghANXyJB5l8OZqeRw1rRLPS1GsVBxJDfuFD0my0tNPBzxzBAE8XlP54b6Ha1iZ_vqo4ZYsWhhqzopaRdC9ic34mvQ6_ehFj_4GRG1-Zc9af4VBMDThJke_rn2IW9S1DR8xiORD2-qD0uAX3zhaJVAjCWiJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علی علیپور: از آقای قلعه‌نویی تشکر می‌کنم که شانس حضور در جام‌جهانی را به من داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136539" target="_blank">📅 15:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136538">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136538" target="_blank">📅 14:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136537">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwOpuxnpNMRduNcp6dRk6jUWiX_dZqJpDyFGIzm0JuN-83xgJfqGlTrA2QKLNhpA9w9L-61ficOtRb3G426PBAD0zsI0guGMa6IcbgLEWuqJbBHqQWItnxu1faAadeHSG915OyBLY-8BDGiG20EZck0DPWa_WFp3A-8ZV-rv7tgikqMvSx1GtgVxqjXVaN-hBlAuf6BXmPnVIgkJKTljItJPtJukxf4zMoNsF7b8hN7vrtKUVvyMLuRKvNN37-bDXXnwp9oFa3uYnleCDLJkbDrteYI9xi-b-WKmY7d2XMAgHNo9JzAmQWiMXWvsx7wL1G8dj7014J1uQS-CGn0UFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پرسپولیس امروز برای برگزاری تو این کمپ زیبا و
اردوی ۱۲ روزه راهی ترکیه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136537" target="_blank">📅 14:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136536">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
میلاد زکی پور، مدافع چپ سپاهان پس از قرار گرفتن در لیست خروج محرم نویدکیا، به پرسپولیس معرفی شده تا جانشین میلاد محمدی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136536" target="_blank">📅 14:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136535">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
فوووووووووری از ورزش سه:  دانیال ایری و کسری طاهری از نساجی به پرسپولیس پیوستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136535" target="_blank">📅 13:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
فوری، حمید مطهری با جدایی ابوالفضل رزاق پور، مدافع چپ فولاد خوزستان و پیوستن این بازیکن به پرسپولیس مخالفت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/SorkhTimes/136534" target="_blank">📅 13:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136533">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
شنیده ها: محسن خلیلی ساعتی پیش با حمیدرضا گرشاسبی برای انتقال ابوالفضل رزاق پور دیدار کرد و قرار است در صورت توافق شخصی با بازیکن و واریز مبلغ رضایت نامه این بازیکن راهی پرسپولیس شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136533" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136532">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
با نظر مهدی تارتار ، محمدحسین کنعانی زادگان به عنوان کاپیتان اول پرسپولیس انتخاب شد / فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136532" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136531">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
مخالفت AFC با درخواست فدراسیون فوتبال ایران؛ گل گهر نماینده ایران در آسیا شد!
🚨
🚨
کنفدراسیون فوتبال آسیا با ارسال نامه‌ای به فدراسیون فوتبال ایران اعلام کرد گل گهر نماینده کشورمان در لیگ قهرمانان آسیا ٢ خواهد بود و در خواست فدراسیون برای حضور چادرملو را نپذیرفت.…</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136531" target="_blank">📅 11:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136530">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
✅
پرسپولیس انتخاب کاپیتان را به تارتار سپرده؛ احتمالاً رقابت بین علیپور و کنعانی است.
🔴
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136530" target="_blank">📅 11:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136529">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
طبق شنیده ها   احتمالا فردا باشگاه از سه تا بازیکن رونمایی خواهند کرد .که شامل محمدرضا اخباری و کسری طاهری و دانیال ایری هست.
🔴
باید دید چه اتفاقی خواهد افتاد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136529" target="_blank">📅 10:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136528">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5HFBUvkRbPOjjO9prVsdbbj8OpNSnTKYgLd6-NOCIeS_8AHVC0Y2Si2JexmKM8pLT6c_ZjtBt6q25UzQ6oHRyiijPCANDnmBev9ShQJcnqQuKbTBPRyxKaNBpFE2wRPjYxoTeB-EMiHn4nejk9QOQ-qKowu-i5rQi3jrMatBhvacJPOba7U4JVLM-Ybk8LVrU6nhKDig5_eHK9Zn5Qhr53GVTV5vkRHmUOnwXPHxONSS4wz-pR6MxOz0b81Q_-V-VXH_ySfSJ_-aNT4SupwRgqLCfEjaS_1dEyq4bzATmT0MYP4MC3vg7Lenb3DR12wSSuI7WHlX0YCBUfVL2m0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
خط دفاعو ببین پسرر
...شیر پسر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/SorkhTimes/136528" target="_blank">📅 10:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136527">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oeq_LPoBpWyp7pp7SbW5G_n7rDbRerkOmDRYlWoUc1ku2He1EnkW57xmDTS2nqsgRM1UNk9sdopl8A5fJC6LgBSOvDTgdsqp0FxRXNfkh7IPzOVjxX6Qqm98Wmmq3xZlpHy4cAcABH8jgGSjVeDfSWeXWdcJLcgTMg6LqzDGOYCktZVJCdW-7z5WARVVBeqdcSmBQSuaH57GyfobQOdo-7-m1UCp1gqknYmfB8EcZyeM1j8y3nvojyVUej81KWjkgr0G1OM5wZhrfXtvEaHQQ3GKtavwbbAULtzoY4CUy9eFE4Tw5kLwN5a6vji9BbpJo1KO5UT61K5JKeJUnj7qsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باراک راوید خبرنگار آکسیوس: یک فروند از بمب‌افکن‌های استراتژیک B-1B Lancer نیروی هوایی ایالات متحده، شب گذشته به ایران حمله کرد
❗️
پ.ن بیچاره مردم که دودش فقط تو چشم مردم می‌ره این جنگ ها و حملات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136527" target="_blank">📅 10:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136526">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ArTIUJW35ZDqxDCXlxgrIGZMKpIQaIJGSrHQZJ22ICWNZOR9NYPCeY7jVu_c7IoQBuZW7xUcYgatoVpl3DiEIsM2kfN52uHcKAR_Y3aRVvSPMIYrD8VaNjI34NlhcxVFdqCrbAxtLZBCrhCHJujkgYtyUtaxvKsen1V6pqqpQCoFvJqUru-mqdQyMqwcEXacsEUwTRn5roAbBc5zUk0uXvHgY_fh4PwB9hE6IHi2lgYvHMyHi4zMt8uLw97nJHPWv6iNebmxqn71R1r73cxyfonnicQRtve5UKUKxgE46CAMR2VQgUiannCpZ-1L2Lj3xWA7VZ7yEaIqHQPbj7tnXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرهیختگان: محمد‌مهدی محبی در لیست مازاد اتحاد الکلبا قرار گرفته و باشگاه اماراتی پولی بابت رضایت نامه محبی نمیخواد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136526" target="_blank">📅 09:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136525">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✅
کسری طاهری و دانیال ایری طی 48 ساعت آینده قراردادشان را با پرسپولیس امضا خواهد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136525" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136524">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136524" target="_blank">📅 08:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136523">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔹
فوووووووووری
😐
🔹
ترامپ: دستور دادم در های جهنم به روی ایران باز شود  ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136523" target="_blank">📅 08:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkDF-14XI-DYSyQsK-XEt-PsF3r6dZG9f17ibA1iEfxHY6Qm5cB5qGLuML_GmwAxT9LMPBvGEUJL7O66WJJdg6hKfFDzBRDJqyzq40NeMwFzGtJe2lm8gVBgJWwBcBa78SsZ6AJqw3dcEgZplG2tlwrNdoD9UoBzhGsS-mT5KEpAVSY0iEy0qGZt9aenE3K4Nm4O2bae6XLmtieohe6IMxmD7nQa1IkVEcGMEejf8S9T36xPsMjP5pFoE7kHcMYpNqBzL28xJiW_Ixe46qxrUVCtQkJ_iknVEfbhk251RLL8LQnK-LiL-IdkqNTbLFbPQjTXU40ipF-YcQ0CNWIwuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136522" target="_blank">📅 08:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136521">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">linebet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136521" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136521" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136520">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA_p4M4lu8AIqfpPyixC_VbU7qZJy5SYwL8t0n81e4FxI4tXL0xnOy_MjTgK7H3GvpCtPy5zwTS8WsIizjy6DLz3h0kqWb2PPibZ2FtMNuKxKuDC69dviD61BTVCKf6NAGd1lSAAyGzuQEpKvF6IZGJSA5TcNTozLbaVFPgpfV3CIQMyLAfNNGQhFmz-v1xDK86vt_oOPNP-VHG_cv1lOp0sf6tLM9S46sjH0i_DOkrR-6A89zJgTZHxMfBeYpeUY1OXdUCLzmgLMBi-6Rqsld676ubC6MFpqvnAgkocFG7yNorzW2lu8PEGGO9aJjbb86mhI-EITmF1JJ-1cYnbvA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136520" target="_blank">📅 01:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136519">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3zTcCbhxQpsTztkWnPFgvNWsXIGbMasQyXbWPsSFS-I8NJm6QpwDXKsQIoEwzDHyTBqo2h7qDdx8XCjU1l548JiaDWDf3U1M8jADyXAOtOZE-vIC_y95zj_NCb99bpHi-c2V1kzdRzfx07cJhn6tuj6TH4nldfoWpB1RYVR5kQxcEhSeQuhotHJcBtEcjhkkgU6M96oBY47i6Tmfl58O1_CyUte2rwQToF5-oHbtY6v4JUPmmwt_djYkWRgkUnL-WZnTBB7khGUqaJ2z2vat3Sbrszz9uU65lbOQZnjycFX-L6YKzTJsgK6uMIUJmf8-zeHiKQGZ0Cm_gt9ppKz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
درگذشت قهرمان جوان ژیمناستیک‌ تهران
🔻
محمدصدرا رحیم‌زاده ورزشکار ۱۸ ساله و از قهرمانان ژیمناستیک استان تهران که هفته گذشته در حین تمرین دچار سانحه شده بود، دار فانی را وداع گفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/SorkhTimes/136519" target="_blank">📅 01:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136518">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/SorkhTimes/136518" target="_blank">📅 00:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136517">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/SorkhTimes/136517" target="_blank">📅 00:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136516">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
❌
حملات امشب شروع شد و فعلا چندتا شهر خوزستان صدای انفجار داشتن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/SorkhTimes/136516" target="_blank">📅 00:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136515">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">✅
فوری/ سنت‌کام:
❌
دور جدید حملات از الان شروع شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/SorkhTimes/136515" target="_blank">📅 00:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136514">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
محمدرضا اخباری دقایقی پیش با حضور در باشگاه پرسپولیس قرارداد‌ دو ساله شو با پرسپولیس امضا کرد / ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/SorkhTimes/136514" target="_blank">📅 00:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136513">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/SorkhTimes/136513" target="_blank">📅 00:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136512">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
✅
دیروز در بازی با خیبر، جلالی مصدوم شد و از بی دفاع چپی جای خودشو به دنیل گرا داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/SorkhTimes/136512" target="_blank">📅 23:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136511">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
یک مقام رسمی باشگاه پرسپولیس خبر امضای قرارداد دو ساله با اخباری که وایرال هم شده را تایید نکرد.
🔴
وی در گفت و گو با قرمزانلاین درباره اینکه گفته می شود مذاکرات امیدوار کننده بوده و توافق اولیه حاصل شده گفت؛قراردادی امضا نشده است.بیشتر نمی توانم فعلا توضیح…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/136511" target="_blank">📅 23:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136510">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
فوری از سپهر خرمی:
🚨
بعد از کنسل شدن تمام گزینه های پرسپولیس در پست هافبک دفاعی، مسئولان این تیم دوباره سراغ محمد قربانی رفته‌اند اما اینبار با پیشنهاد بهتر!
🚨
قربانی از تراکتور هم پیشنهاد خوبی دریافت کرده اما تمایل داره به پرسپولیس بیاد!
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/136510" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">✅
✅
پرسپولیس با محمدرضا اخباری به توافق رسیده و اگه اتفاق خاصی نیفته، امروز رسماً ازش به‌عنوان دروازه‌بان جدید تیم رونمایی می‌کنه.///فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/136509" target="_blank">📅 23:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
🔴
باشگاه پرسپولیس در آستانه توافق نهایی برای جذب دانیال ایری و کسری طاهری است.
✍️
قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/136508" target="_blank">📅 23:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/SorkhTimes/136507" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/SorkhTimes/136506" target="_blank">📅 21:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8WDyFkLTGN-mgJUghk4n-rKozEyvYGyHz_rzjCL9a-wgkfY0L2perIWvoEi0t9cie8yX9JNWZz51EQwLTXH0wicZmPGOV97Ftiau-uq8Jyw2euBTHRWKyR6L4s1hl-L2TchCasW1ChnZXcLOvuXQf0J2k0OrecqQkTWe0smTTqFJaQxorUo44zHd9laufZAPxx3y3HbDyGPc-N4uLjAXZp-kN8fwscJ9mQhF8NwwZtPisSKDkiZHJ3E8ddIlIjuEptDhi7xC7uN-9XfoRhzz7w6mYbVrhv3SBTbaa-sD0UaRuSSCGQsP8PfVnMkWITOIelhYFu0samHEZM3NzFFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
فوری/ کان نیوز: اسرائیل از سوی ایالات متحده آمریکا مطلع شده است که این کشور قصد دارد حملات خود به ایران را تشدید کند و در روزهای آینده، و برای اولین بار در این تشدید، حملاتی را با استفاده از بمب‌افکن‌های سنگین علیه ایران انجام دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/SorkhTimes/136505" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
✅
امیرحسین محمودی در فصل آینده با شماره 10 برای پرسپولیس به میدون خواهد رفت. شماره ای که سالها بر تن بزرگی همچون علی آقا دایی بوده
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136504" target="_blank">📅 20:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❗️
پورعلی گنجی هنوز با پرسپولیس برای جدایی به توافق نرسیده است
🔹
گفته میشه این بازیکن زیر بار کم کردن قراردادش نمیره و کل پولش می خواد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/136503" target="_blank">📅 20:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗️
رسانه‌های مملکت: نساجی با انتقال طاهری و ایری مشکلی نداره و اونا در اردوی ترکیه به سرخپوشان اضافه میشن و حتی ممکنه کاظمیان هم در ازای رضایتنامه‌ی یکیشون راهی قائمشهر بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/SorkhTimes/136502" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗️
تکمیلی :فرهیختگان: استعلام از فیفا اومده و مشکلی برای انتقال نیست و احتمالاً هردو قرضی رایگان تا نیم فصل + بند خرید با تیم راهی ترکیه میشن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136501" target="_blank">📅 20:37 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYz002rw6u5xMeIkuBLauuBFf_EtN5WXgWEoFUCd_b47EEpeq5vT70MmRYOZYd-SgzuLCI1d5xpF2drhDkQrB9wbh06U1CRm9BpxxEUgblmo7BXLmtiUiAjW1kYGVMJkIi90UOs9ufFy0qaWrIxDATG3k75w9qGaHgBlBdhFQC2DR8OXCa2LSFDCflPbCRuAPAoRZIS25y1QamfcR4VFQnbNtQvpFMU0AvA1e88CBYeo4roHcE5BbxM6f671_NpIGE7K0E-QG97qm9XzfS7xl84TzuvZvSKLLT2WCq9gSSTqW0wM_N3hhE1pDO9VaGktV0eBKy7ASA62gTAMPTO18Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طاهرخانی:
❌
میلاد زکی‌پور با ارسال پیغام‌هایی به بعضی از افراد خواهان پیوستن به پرسپولیس شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136500" target="_blank">📅 20:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جالب اینه تموم فرم ها رایگانه، حتما عضو شین و‌ چک کنید چقد راحت سود میشه کرد
😉
✅
JOIN JOIN JOIN
JOIN JOIN JOIN</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136499" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyHxUKkzpnTbHT6JodBFh89ozul5Xl8k7alaxvW2P0ydzi_dpUKM-_L1X3olOsWeN7vLZuYEtpVbgW7I90Fb5TLdiZL3OTQyJKok4zp5UNKbBYQsnNZMz8Vd8j7o2tjVp2nGSvxu278O4S98xxuAhEU_lmfZX6pk-kaF9T9oTrdZbsz33uaTyDonYD0sv0sVvvTTPSUNqb7iX81owwN5h_Gc7GdQncPumEYQ9GVCowX1FchBfpkfRTbcjEsnUVpJc3F0R0Hq_KMJSQsjFdbXWMhONWk0npv9ViPAKYRPSeZyvtvUgyK919qjeqs_jzegEDeLjF2lzuih69fp-hKSpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
Ⓜ️
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@ARON_TIP @ARON_TIP
@ARON_TIP
@ARON_TIP</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136498" target="_blank">📅 20:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❗️
❗️
به این ترتیب با وجود رد شکایت باشگاه پرسپولیس، همچنان موضوع اصلی پرونده محرومیت 4 ماهه بیرانوند به قوت خود باقی است و این دروازه‌بان در شکایت به دادگاه CAS خواستار لغو محرومیت و جریمه مالی خود شده است.
🔴
🔴
شنیده می‌شود هنوز علیرضا بیرانوند در موضوع شکایت…</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136497" target="_blank">📅 19:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❗️
🚨
خبرگزاری تسنیم: عادل فردوسی‌پور نباید از علیرضا فغانی که از رضا پهلوی حمایت کرده، تو برنامه خودش دعوت می‌کرد و همین باعث قطع برنامه‌اش شده!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/SorkhTimes/136496" target="_blank">📅 19:11 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/136495" target="_blank">📅 19:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
پرسپولیس فعلا با احتیاط داره از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نمیده، چون دیرتر از بقیه بازیکنان به تمرینات اضافه شده
❌
❌
کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدومیت های پی در پی نداشته باشه
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136494" target="_blank">📅 18:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=h8_4caikYpgW_J6VN3Iq1Gvg0rov5tQBJR1qXrKcLZbQgizzvJq21eauD_SyaODeRdfnHN2LOOw8iBHV1qH-1g10kVkY-raaFzXcUAbIyFkGseKHYNrNJZ9vceB-bYFygRg-ff3IxdkNxsl-jPo3A3QUYBCNDdkZoxIcYsSxTiIK-N93Paee3H_zpxusN1N0SYgWDei3pzGCo92NxncjBHQlEM9CTmhJcyFp1CctKY4TwiyQEJdEeeegOdGZ8Fd8JOgSNme6vNH3i8Mog2PtJJZHXi6brvQepMbv8T2xAtC4lsdtHu7FM04acxUeETZoFMbwER5MHAAo6S5RRK1-Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27b7114b3.mp4?token=h8_4caikYpgW_J6VN3Iq1Gvg0rov5tQBJR1qXrKcLZbQgizzvJq21eauD_SyaODeRdfnHN2LOOw8iBHV1qH-1g10kVkY-raaFzXcUAbIyFkGseKHYNrNJZ9vceB-bYFygRg-ff3IxdkNxsl-jPo3A3QUYBCNDdkZoxIcYsSxTiIK-N93Paee3H_zpxusN1N0SYgWDei3pzGCo92NxncjBHQlEM9CTmhJcyFp1CctKY4TwiyQEJdEeeegOdGZ8Fd8JOgSNme6vNH3i8Mog2PtJJZHXi6brvQepMbv8T2xAtC4lsdtHu7FM04acxUeETZoFMbwER5MHAAo6S5RRK1-Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
در شرایطی که قرار بود امروز بازی پلی اف لیگ برتر بین مس رفسنجان و صنعت نفت برگزار بشه.. تیم مس تو زمین حاضر نشده و آبادانیا جشن صعود به لیگ برتر گرفتن
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136493" target="_blank">📅 18:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
#فووووووووووری
🔴
پرسپولیس در آستانه جذب دانیال ایری و کسری طاهری
🚨
پرسپولیس از فیفا استعلام گرفت و فیفا اعلام کرد مشکلی برای عقد قرارداد وجود ندارد
📰
فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136492" target="_blank">📅 18:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">❗️
باشگاه پرسپولیس برای جذب کسری طاهری از فیفا استعلام گرفته و منتظر جواب فیفا ست تا برای جذبش اقدام کنه/آنا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136491" target="_blank">📅 18:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🔴
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136490" target="_blank">📅 18:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136489">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
ویدیو باشگاه پرسپولیس برای خداحافظی و تشکر از کمال کامیابی نیا
❤️
🎗
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🚩
⭐️
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136489" target="_blank">📅 18:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136488">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
زارع و شهرآبادی دوباره در ترکیه؛ استراحت دو روزه برای سرخپوشان
⏺
مهدی تارتار امروز را به شاگردانش استراحت داده و فردا نیز سرخپوشان خود را برای سفر به ارزروم ترکیه آماده خواهند کرد. در واقع فردا عصر کاروان پرسپولیس عازم این سفر خواهد شد و 10 روزی را در آنجا…</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136488" target="_blank">📅 17:51 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136487">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
🔴
تیم فوتبال پرسپولیس فردا برای برپایی اردوی تدارکاتی ارزوم ترکیه عازم خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136487" target="_blank">📅 17:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136486">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فووری/منابع عبری: ایالات متحده امشب با بمب اتم تاکتیکی تاسیسات کوه کلنگ ایران را منهدم خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/136486" target="_blank">📅 17:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136484">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
ترامپ:ما اصلاً کارمان با ایران تمام نشده است
🔻
ما در حال حاضر قصد ترک خاورمیانه را نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/SorkhTimes/136484" target="_blank">📅 16:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136483">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/136483" target="_blank">📅 16:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136482">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❗️
دیدار تدارکاتی پرسپولیس با نتیجه دو بر صفر به پایان رسید و پرسپولیسی ها با پیروزی به ترکیه خواهند رفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/136482" target="_blank">📅 16:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136481">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
پرونده شکایت پرسپولیس از بیرانوند و تراکتور که دوساله طول کشیده به علت عدم پرداخت هزینه دادرسی توسط cas مختومه اعلام شد!
🔴
🔴
مدیریت درویش و حدادی:)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/136481" target="_blank">📅 16:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136480">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">❗️
فووووووری؛ با اعلام کاس، شکایت پرسپولیس از علیرضا بیرانوند رد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136480" target="_blank">📅 15:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136479">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❌
شکایت پرسپولیس از بیرانوند و تراکتور رد شد
⏺
دادگاه عالی ورزش (CAS) اعلام کرد شکایت پرسپولیس علیه علیرضا بیرانوند و تراکتور به‌دلیل عدم پرداخت به‌موقع هزینه دادرسی رد شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SorkhTimes/136479" target="_blank">📅 15:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136478">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
ارونوف تحت شدیدترین محافظت پزشکی
🔴
🔴
پرسپولیس فعلاً خیلی با احتیاط از اورونوف مراقبت می‌کنه و تو بازی دوستانه بهش بازی نداد. چون دیرتر از بقیه به تمرینات اضافه شده، کادر فنی می‌خواد با برنامه ریکاوری و بدنسازی مخصوص، کم‌کم آماده‌اش کنه تا دوباره مصدوم نشه.…</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/SorkhTimes/136478" target="_blank">📅 15:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136477">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
بی تفاوتی علی دایی درباره استوری بیرانوند؛ فقط سکوت
🔴
🔴
علی دایی صراحتا به دوستان نزدیکان خود گفته است که قصد ندارد جواب علیرضا بیرانوند را بدهد چرا که اصلا او را در حد خود نمی‌داند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136477" target="_blank">📅 15:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136476">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❗️
❗️
قلی زاده: فکر نمیکنم تو ایران برای تیمی جز پرسپولیس بازی کنم ؛ چون قلبا پرسپولیسیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136476" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136475">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136475" target="_blank">📅 14:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136474">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
امروز ساعت 18:45 دیدار پلی‌آف مابین صنعت نفت و مس رفسنجان برگذار خواهد شد تا هجدهمین نماینده لیگ برتر در فصل آینده مشخص شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136474" target="_blank">📅 14:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136473">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=TvPofrmhi1jXzaCZHkKxIXcja-bEKl9qLFQiUZLOzg6xiheXTYAMyN-IRlIjFT-V_MmIzysxQ-ypwNYm00VKmB7LR9tkwXIeXQSpSt8qFjIz-FJQKCMBmMYchnNLxgtRhZbssx030S8nXo1EbdomRfLdB9UHQIVaAX-guIFYE1kkNB9AxDP4LCnezKaWMckNtCq6dVyx4Lsb7zXtczKsM_vkKvDy-IZAASyR1_fPkis3nHb5d4lkZEZgar4CZvcZj9FPbKB4FCaqArJkDkha65sIIbDHXaU4fnQoNRYBM7lOZ6LUK59-nOOD-jZb29v_JA_jGFlxkcBxJ7t53xRE5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352f2979cb.mp4?token=TvPofrmhi1jXzaCZHkKxIXcja-bEKl9qLFQiUZLOzg6xiheXTYAMyN-IRlIjFT-V_MmIzysxQ-ypwNYm00VKmB7LR9tkwXIeXQSpSt8qFjIz-FJQKCMBmMYchnNLxgtRhZbssx030S8nXo1EbdomRfLdB9UHQIVaAX-guIFYE1kkNB9AxDP4LCnezKaWMckNtCq6dVyx4Lsb7zXtczKsM_vkKvDy-IZAASyR1_fPkis3nHb5d4lkZEZgar4CZvcZj9FPbKB4FCaqArJkDkha65sIIbDHXaU4fnQoNRYBM7lOZ6LUK59-nOOD-jZb29v_JA_jGFlxkcBxJ7t53xRE5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
📝
سیدجلال حسینی:
🎙
آقای کارتال خیلی ادعا داشت و نمی‌شد با او کار کرد. کارتال باشگاه پرسپولیس را خیلی کوچک می‌دید و نمی‌دانست به یک باشگاه بزرگ آمده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136473" target="_blank">📅 14:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136472">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
تیکدری امروز بازم مثل بازی قبلی یک گل و یک پاس‌گل به نام خودش ثبت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136472" target="_blank">📅 14:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136471">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">❗️
با پنجره بسته، دفاع چپ جوون هم گرفتن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136471" target="_blank">📅 14:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136470">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/SorkhTimes/136470" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/SorkhTimes/136470" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136469">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.Melbet.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
giftcodeir
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136469" target="_blank">📅 14:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136468">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e636d7ab2.mp4?token=jwMHx-jTp1aQhxXprIt1TitpQc8CcSA8LjfxRcx1ALicKy-BjgL1gfGjPoCqst9NZfBn2PNwhUph_mYDtZ6gCqAOSCN_LZBGED0AcN1p9DHjq9PCS4npNjeVNrIoXqeUdJk2YDpdmZUy6siUw_n7XlW80YVpmd2-FLbYVh-LzCB2cqjMGSkbGPNMvnubdF49yYAksn2D4dXfQx3FSUTyJUrqWnZ6HUiHqdxT1gbdBSqzbDnhO43zc3D5NrPXOlUo2n8mRfI6rtxpKSVWUE8PIXm_7D0JHgci9URod6tL-OGpF0pISDeyLAXCoNzTOx67tN7KQ95WWgLmWGVhw8_vsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e636d7ab2.mp4?token=jwMHx-jTp1aQhxXprIt1TitpQc8CcSA8LjfxRcx1ALicKy-BjgL1gfGjPoCqst9NZfBn2PNwhUph_mYDtZ6gCqAOSCN_LZBGED0AcN1p9DHjq9PCS4npNjeVNrIoXqeUdJk2YDpdmZUy6siUw_n7XlW80YVpmd2-FLbYVh-LzCB2cqjMGSkbGPNMvnubdF49yYAksn2D4dXfQx3FSUTyJUrqWnZ6HUiHqdxT1gbdBSqzbDnhO43zc3D5NrPXOlUo2n8mRfI6rtxpKSVWUE8PIXm_7D0JHgci9URod6tL-OGpF0pISDeyLAXCoNzTOx67tN7KQ95WWgLmWGVhw8_vsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فنرباغچه اسماعیل کارتال با این گل زیبای تالیسکا بازی رفت پلی آف لیگ قهرمانان اروپا رو برد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/136468" target="_blank">📅 13:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136467">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚩
🚩
قلعه نویی منتقدان تیم‌ ملی را بی وطن و وطن فروش خطاب میکنه...
❗️
❗️
❗️
🔖
🔖
خاک بر سر فوتبال این مملکت، که سرمربیش قندلی است...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136467" target="_blank">📅 13:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136466">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❌
❌
در ابتدا مدیرای باشگاه قصد فروش اورونوف رو داشتن تا فصل بعد ازاد جدا نشه ولی تارتار خواهان ادامه‌ی حضورش شده و جداییش کنسله/فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/SorkhTimes/136466" target="_blank">📅 13:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136465">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⌛️
⌛️
فووووووووووووری
🚨
لیگ برتر به صورت رسمی از 23 مرداد آغاز خواهد شد.
🚨
همچنین جمعه 2 مرداد مراسم قرعه کشی لیگ برتر برگزار خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136465" target="_blank">📅 11:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/641375cfeb.mp4?token=lPa5Jvs3GzMKkOXbwm0yYMrZeI1F_C8kcPozr9It5TKgz4bNVVeRp2CQzLNll8GdxmsIINkKxDD8EKby8iYtagGPH8aWmhFcvvYtrAiKEHMtnSB44ykYvZcciQXZJRSu03xeYHi1KgsRw4D78ozuF_tXU_OEYq1G0Zi3Pe_zsGMi5lnSwmpxcqdsp5CeiaZcW68qBEl9rh4VTjvKMHMsfnQpc-8rLXH12aZT95_J7X0ZWcJ_-JFi4EtdcgC1U2ChYIYA3EjPrjPcgAp3pWbGYqkgYQnc829xNnFJcagK7zXnEojHOa1aOVH23um2alx1WC_U8Sg2alg4zHejIrZ6xkGLZYVzz13vGOGunvCb9H1NLFDQgHQbY6JAYkDb38yxQ8TdIMsm6fxozDi8kVxuV9wIl1hUvWeOxAsN1URobIAT4cPn2mCqfDQ8zzEPOYDcDKKhjPRGNKP3ymJ24D5NEvUf90DKnbV0-RABd9k9H1ELg8rdjZ1joANfSJlYzIFHbjJS54-7Lq6ZkN9ZarUgX6dnutv-49j5cCJlfgDAv-FTt6aZRVRSHK83DdAq1AQjA9qRB8cNqydyNFWn3RXb2FdQc72xQyPjDwD6YuvxPhnc417npDf4ctEtLeqU_H6y5vx0iwEVe8dhfXkXq0lbBnLd0Eerz-mc1b9j5jhHuNk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/641375cfeb.mp4?token=lPa5Jvs3GzMKkOXbwm0yYMrZeI1F_C8kcPozr9It5TKgz4bNVVeRp2CQzLNll8GdxmsIINkKxDD8EKby8iYtagGPH8aWmhFcvvYtrAiKEHMtnSB44ykYvZcciQXZJRSu03xeYHi1KgsRw4D78ozuF_tXU_OEYq1G0Zi3Pe_zsGMi5lnSwmpxcqdsp5CeiaZcW68qBEl9rh4VTjvKMHMsfnQpc-8rLXH12aZT95_J7X0ZWcJ_-JFi4EtdcgC1U2ChYIYA3EjPrjPcgAp3pWbGYqkgYQnc829xNnFJcagK7zXnEojHOa1aOVH23um2alx1WC_U8Sg2alg4zHejIrZ6xkGLZYVzz13vGOGunvCb9H1NLFDQgHQbY6JAYkDb38yxQ8TdIMsm6fxozDi8kVxuV9wIl1hUvWeOxAsN1URobIAT4cPn2mCqfDQ8zzEPOYDcDKKhjPRGNKP3ymJ24D5NEvUf90DKnbV0-RABd9k9H1ELg8rdjZ1joANfSJlYzIFHbjJS54-7Lq6ZkN9ZarUgX6dnutv-49j5cCJlfgDAv-FTt6aZRVRSHK83DdAq1AQjA9qRB8cNqydyNFWn3RXb2FdQc72xQyPjDwD6YuvxPhnc417npDf4ctEtLeqU_H6y5vx0iwEVe8dhfXkXq0lbBnLd0Eerz-mc1b9j5jhHuNk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
در اتفاقی عجیب، محمد خلیفه به سبک رضا درویش بر روی خودش کت انداخت تا دیده نشه و از ساختمان باشگاه استقلال خارج شد
😂
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136464" target="_blank">📅 10:49 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4Kt8zW0h4Xr3Hq08MqL87JIC9bU_zNNE0yn-DfC-MLKvMj4BGdiVY6Uz9PosUDnS4rH94nlXKegds8g7Al3ThhQCo8O6rPsnhyYXVy7peQWyBDOgchsWBpJ79CTNj4VkzL8HiPG-IBrzsrcRwlSpeQHyCtdyI49QOibeotlVKcH2xUklTqq6STZriggaIoIo920QSx-WLWfBz9RdWshbdveTd13-_cWyEAXlBl7oV3L-fL-cbRUdjfQyqSq-JYeSVcmemPAjjFuai4Y6iKwUfFh5TwE8WDlIP1BQlUNGMsQ5j2QJ4MdtNiI3bQD5fLgV1WiauOTSaKk03X6S7FV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
شرط پرسپولیس برای جذب کسری طاهری مشخص شد
🔴
🔴
پرسپولیس به نساجی پیشنهاد داده طاهری را تا نیم‌فصل به‌صورت قرضی جذب کند و سپس با همان مبلغ پرداختی نساجی به روبین‌کازان، قرارداد دائمی او را نهایی کند. حالا تصمیم نهایی در انتظار پاسخ مدیران نساجی است.
🖍
✍️
خبرگزاری…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/136463" target="_blank">📅 10:47 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136460">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">❤️
🟢
مروری بر مهم‌ترین لحظات دومین مسابقه تدارکاتی سرخپوشان؛ دیداری که با پیروزی ۲ بر صفر پرسپولیس برابر خیبر خرم‌آباد به پایان رسید
.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/136460" target="_blank">📅 10:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136459">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">❌
❌
سید جلال
:
❗️
هیچوقت به رفتن به استقلال فکر نکردم و نمیکنم به بقیه بازیکناام میگم اینکارو نکنن.
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/SorkhTimes/136459" target="_blank">📅 10:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-136457">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
تصاویری از بازی دوستانه امروز پرسپولیس و خیبر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/SorkhTimes/136457" target="_blank">📅 10:23 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
