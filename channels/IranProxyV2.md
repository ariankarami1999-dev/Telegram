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
<img src="https://cdn4.telesco.pe/file/VYC7yx3oO1b1S8ucAHBO7DTa6Qb8LroSwc2Kf0rBTtORlJHR2qMgvZubdNxY3-5uLKgYWWTSTq2P-wea5fKiIOSgufyrwdkOoHlQFrI-r87KnaADAx1a6xvNtd3p9EOapTLWDq7dh99X_xp0B1bx8dV4q5s9GT23O2Xt7SXga0l7g-qc6LFXmKu7gALnYlQ8HNxParpNBvaFzVWmNDrKbENxjUSTalySKkj3RUIPkHpR20IMcmdr0mHZo1T2JMkIW37TuzehzZF6Ypv-SGwNAgg0b8lcjBm5lpi98x1enuBYHb_i6XXGny9reKN2-X10JP_f_jGV1oj_qvjhOA98Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی | فیلترشکن | کانفیگ v2</h1>
<p>@IranProxyV2 • 👥 39.4K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارائه‌دهنده راهکارهای نوین شبکه، سرورهای مجازی پایدار و سرویس‌های مخصوص تلگرام  گیمرها و تریدرها.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 15:16:57</div>
<hr>

<div class="tg-post" id="msg-8480">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMJJzWtfcMy_g0M0EfpmfwNuxRZmfM4Swfn4qDv8c4j-UNHytrV8XZse9vIBm9vtgTHA80Ka37ltkc6um3RVZ-0p0u1vwHE4SIsApRo65flLZ_Xfyq9eh49h5zfQXSb7dgRoVPPGg3c6g-ksA79D50oOc_2wrBGmB9nW_MbbP6ZwD1OQDJVr5d5PeW1WM0Bt-VEzhApHYFEjuAkwBcBEhqB5cRzITfQzHG4f-P0aK-7q32993JVlcIo8bFx5fGjSjrCHuwcsQel9nqPlGo6RK8fzjkhS5AXN2ctwxBkUIynoQn7-lnQkSK45amykq3jmpO8nXhhU-YfMvbfEmXPGew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkd0qWTYJqEJnKoAw_ysnO8g50-pD4C4zeFWu1ZwKRAvxg9j5vueLmCHsrlFvEOuVfqwcp0A-XvNFiuwdE27HsJOcuMlEh-RUKyOJPIlFfpgAOV27BESrjI-zgENGDNRWHX4y7tzPgEWtrK4uY_vMKFmbSj1uUEJf12wNdqmYrkv-r5dLqWFQe7f1ZkBSh2Poi17XFfobq_vx8wfOCK3m0Rp-mINuRZr0Y1PT6EltxKeeCQDhdfsyihvmHhpO3yxnvZBmdU9kxs9kvhoFWigm2hyL-EXm6-SMNk-2UZx1CpX5YHJBOIcwZcbKXYyHWndM8JdP_3prbLxdqeohxSliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تنها چیزی که تو این جنگ نصیب ما شد چی بود ؟
قطعی اینترنت
نابودی میلیون ها کسب و کار
افزایش شدید تمامی کالا و اجناس
فروپاشی روانی ملت
اتلاف وقت با ارزش و هدر رفتن زندگی
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwyNoiPP4cLzs3KcNKvdP8_CrqvbKaY7ziJPgWSdjSW4Zl0H6OeNJKtQFJe5QcK0lYWWTT2kYz9Fes9uRvuVrAUK2GnvebgVdCyKBwA0EEw0KESy2VhK3Bo8rfxw0fGUJHRs9wCebVaR3pajYi6koXQNbWiGj1Wy-4g5LKLJlNEOpaKnT2qQk18IEAWE2CAEpbvEohcWc64YeEWrifgSLwISEZrBygf1_iN0Zqi-geAjpAIQKycpnlOFuuOozkvpcsNaVwJnKX8I1p6ZKWQwXzfW6NskyUtt8_Abtl8LHN_xoy6gWJ3cjvupdytZ8Z1TdU3h1MFbbF0JjqlZvdTpLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgTSrfQz1LT-VxIera-gSPxSWoTp9ywXhTGRmKqJR3ai-LI2eHGZA20RSEOMKnI_wmD2gyYEBAq2pKUn_-nqmGmKfm5KcL5A7HDj7E6HVRGx6kFgMW3IyOsS_VFcqStZgjp2m4uZ8Hw1A257CTW1DrPwcFd1sMytAg62Rc5AqaGRD4uzSnEX6JKwk54mY0BViRbJqcbtK2pRedMdvD5TZRXcULBJTMDD8odV96vXl7wC8qAu3Kf91bqWvE1PnIOAZMFt_PV1-8Nm9104sq13YBdcZNA2xJDI3Q4J9nuOqqe1JOZtxziFvYVCjkmFZVb_f93YIFxvcWu3eyvYss-yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
طبق تلاش و زحمات تیم russia proxy بر پایه اصول صدور ترافیک خالصی بدون پکت لاست
⬅️
آپتایم ۱٠٠ درصدی با سرعت +89 مگابیت و قیمت بسیار پایین
گیگی ۱۵٠
⚠️
🔡
براتون پخت و پز کردم، ۳ روزه نخوابیدم، سرورارو بهینه کردم با بالاترین سرعت و بهترین پینگ از الان میتونید باهاش حتی گیمم بزنید، اختلالات به طور کامل برطرف شد و هیچ قطعی نخواهیم داشت
❤️
🍸
➡️
@RUSSIAPROXYY_Bot
⚡️
آیدی ربات جهت ثبت سفارش
⬆️</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8473">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4A24P7dtSqJFWfUwp-uIlPn5VplBVyMKrHmYNOahHKIRwLI4sVgEstMcAS6ZzwzyOHss7OkjlyWFUkzWEQ9n4iGPqHBriEu9rurwD6defuPJwNVyc7s6qVdOK0D_0rWUBEiJJKK5_0AdJH_X5SxV4BeY3e08mMTsaFJcqjo8ilHxxIdkiVvy5y7fy_iM17CWbSJJf5U4cOW7HPGSvnbd60t83bRMYsphcVMBztaHXDiQ5LsF2yJDvXcP0s3b65FIFkSpAowX5Vp0b6p2__-ajNThfLlOsB6Ijb7i0Tpz-wklzCd1ghoETDB6_m5lYU7sWDzps8sBfwTRQeHRLSZAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8472">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez_Gk1polAyH4Dmk_qIHcMtY92B496-h9Bege0J6lfkgZw2-taMNARXo5Imf7QMgF44gydEXDZNGtq8xIH3DwVEsGxZEONS-Z9r2t44qMigeCcCI-I9qjeYV68Gf5oyAY5xwHfdzlmOE4sTGdQA_vB78QQq5fhEQjik1VBI2vzUQz0nUZoOWTIMKqArfaSJWoSsOyVxgUDS5dLnl0yQbgEVhKuOEXH8taLwXJMsok8W4yoONLwNkJ01gi55VQSsvOBvM1d50q62Jk2FTStlU3Q002y6q3MX9J5Tb4lPqthRSe5UfV3tVxsG_A0JxDR0XhiHodYN61YkXRLIkg3u8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZNnB10abtf_mjh78TsrYhtKCCDJJWeu5Ppj-V7Mw2o1anWJhdQzO2QpQqhi-FHbWVC6aizk5_ThZTSNAXFgKPsQrRzl9TuTGFXOz389nH0qg0jPYIrcoFwrugK-Xg6Y6PEjCIJ-d11Qu-ddZR9KUZIbCnKESag-ZCDJGZ1kdGm-PgBLjgowO4vVvhvlungYBElz9Adbpz5HSQG1ewa-v6Lzsywm3dQbTPU5fuzMnWOa5eGIycAMTPrcWKy7wjncVq-Q9DC1pCc8nmBW4gVgLFO6bFYBC4jbw08DEY64f7JVc42tRwE5JbA7btOuoA6iD0u-vNVhz79iV7GziW5prw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW1Dtd9QpJybSFXf6se99CwhVMoZu71iW2UBf4ui7KeWR7vK7vRTKAf6I6MI5YHlcdWFYL_qt2tjxA7C_szxihHh7Ca86oG538vnjZdM3qf-_KtbRlU_K_GJOQdAsF3QMIotTt60qogRMAAUnxh_c0lkr6vJgbObHxsqob25LBBKZTuZg2S_l0LZ2QzRowGPna9y-dIEFdYx6jgsnfclOHtZT87qG9wy7d-pASre2w7FkGgQvAyMj5QYp7xCei42Wz5DcrrA3mTrRKKIRncwC004rfaLAaCr9lqjBs8nGyF3wF1tj667k0zV-TS26BCtmc7A0pV6zhxOwRiJKbfL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnFF2F2TWm-ntKr6bmqJa_VYeCIg1ANtNAdJqyiJ-JRf-gfyMUM25KwEHX531sbYC9Ky2RQmRTuP_o52zDc5C3d2UgrOk1_jHsJVWxbmfihsGQP3R2FyFaetIoJDsY2BRjZFqrTxMGJzlvcsQJlYonVi2hUpsD9hbh3PmvQOLVDcKyr3q3Pm4NOeLQFgOSLWSAxQ0ugEW8Tztyrs2VB9PkGj9NDLmRP0sTNJWcBHndp8g6kZ2GgCJb6iVaQaXK1ygTFikF41GneBSNddXl-CE2Y9od8yCuel9Dw5MlDUN08ju6ka7NhB1BohMr_GaiNuoANWQByQqMLJgrGy9hjM2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xt35BKbd4hvyjKYWsUX3iv1b_kYdLGT53eDV7n8dxjFxe_PzEz1EDQ2lLUpin41z1sPK2s9rmZSK6-9yE4N6pIX1-j11hGaKPIuHjubhoxA3Y0Sie_mQ2yPdtcCCHBwsGx85Fp9tSDJHw9OFov38wMslecm-38YaYd_CgsSj4tgr-hdvNw-anJKpabwse2glr9-cMYEnhP3abxUi5IuI-vm6_gyqbqPB5PPqK_wWjBoa78XGnGAN1quzsKD-uBfu1s_JqxZqtZM3ydOXApO1GsWDvq3FBOF-ELsCucTL83ZdmO9UHNHy21v-96NXL4dGA3TeOu0L2JsuKREX1sG-AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار داده شده و حجم مصرفیتون، حجم باقی مونده، مقدار دانلود و اپلود و تاریخ انقضا کانفیگتون مشخصه
2⃣
پایینتر لینک ۲ تا سرور با لوکیشن های متفاوت قرار داده شده ، خواهشا لینک هارو از جایی که vless نوشته تا جایی که vless بعدی گذاشته تا قبلش، سرور اولی کپی کنید و وارد v2rayNG یا هربرنامه ای که دوست داشتین بکنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMDP_nemFIc5bLQToaFGoQqe_JOxaiP0lnp2nReCq_JrjykFGbx66vQyDbdSSJKQVX7oxIWXAWz9tVXxfzWUe2_T7kgtQiW5ZblTx8lclGaS5MdOJyGOa8vMXtmPjoViodLYcqbx5GUZnU9oIDZTRqBdRlJa0HF08KFAe9DjvH1AfSO3EyTVm1HZZ4OH5R-Hxcjjlgbffmj1vxDjD4PORd-XQXPNx7geuLeZtnzZ855ZoGhovd8luaxnD1DcVrjmPPl1Rb0SFG3qB0kC8_iTMmGuN68N78gbPX2xVMidllNz3tVWf9q-njLW54DJi65NeLBZUG2DN-mOmK_ILrc4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/IranProxyV2/8449" target="_blank">📅 08:24 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0UiGuvRH6EaRRKOan68qugXNSvj7ZZJLtiZQPvIjX4JaY5y45AlLE3bc8nIr2cfvkaqSqNF5CuVrA_-Xji3TaOd9kC1zws9-cl12YbRJTFI4_Av3R51ewUh_k7rAqZsv_BRM3bF9GftWms0Qh9AtOy_SciE_b-0JNdFewCalgmQ8jcrp34QNOql9Py2Cy8KvKtbYwV7P5d4Ntb9J1jfhzVcgGWTMiicq17fEVlnGlB50PjEAGbJph73yI94MeHxSJSeoBaOF_uHB7fiVG_Ao9_O4YaEYaVeVA7Csl7rm9Y81nXXXho7ucHzK-ob3lBFqxzqa_y_IKLQk55WPnjGyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8441">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://086ea932-23ce-402d-969c-8ac02325ce42@185.143.233.5:2083?path=%2F&security=tls&encryption=none&host=p1.sesrsa.com&fp=firefox&type=ws&sni=sub.sesrsa.com#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8440">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=mPCfyhTo6hEUPWRpl0CVQMzLvwQ5g-rUmrSmIXAXZl3Il5xE085wA00FEfGPiqeVmnYPMx0eId4n3AvqwmiX_r4KBtijwhlHx1SqJZqGlb4HgtfxEXon4OH80-uZYootfjUQJPR79KsezUxyT9apXckFBdzXE8VtFurI1eRmHEkUA1_3xUUJLfOsglOHMxZeaUM9_OnTbT7eztkF_jXjPKuSxPkokwgjODmt7BOs2E8nI_zEZ6VUjwCrIb66xSTXFGph_EiWSuUVYiUetqTRnLpcS7Oced8INMyZVUr2-awHX4jYOzO1nA0IBbnsWBHTePvkbamMDAe-dA_QmA264ZhZDzm4l5G8iG-XUOyBfjj9rpVmxKLy8kKpNUAlBNx5rLbEO6tvHkbvW55u4VdLXi5wmY0iMp1qhDOE6JxNPQkwqCcGk63DUezcC-6j4XNtujqjcM6oQIaPEqXi-kJE4t8RQcg3NQiZb1qnp8m6FT264dW6EcFvFNFDboihj9zCw8kcZVss8HxOfkHBT4AUlvMFyDlt0UR8-Zrs9AsR4bef1S8cOTVesmCXzFvhfxcxhcw2qE35sdPXpn3hGzGGWNZrc1O_Ok9702zS7A5BT9POPOTdIneBYu4sF1kjTKQZxrtJfLCBy1SpKQDUsmznJAr0AP1-HhehngTMF1fOVW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ca9375821.mp4?token=mPCfyhTo6hEUPWRpl0CVQMzLvwQ5g-rUmrSmIXAXZl3Il5xE085wA00FEfGPiqeVmnYPMx0eId4n3AvqwmiX_r4KBtijwhlHx1SqJZqGlb4HgtfxEXon4OH80-uZYootfjUQJPR79KsezUxyT9apXckFBdzXE8VtFurI1eRmHEkUA1_3xUUJLfOsglOHMxZeaUM9_OnTbT7eztkF_jXjPKuSxPkokwgjODmt7BOs2E8nI_zEZ6VUjwCrIb66xSTXFGph_EiWSuUVYiUetqTRnLpcS7Oced8INMyZVUr2-awHX4jYOzO1nA0IBbnsWBHTePvkbamMDAe-dA_QmA264ZhZDzm4l5G8iG-XUOyBfjj9rpVmxKLy8kKpNUAlBNx5rLbEO6tvHkbvW55u4VdLXi5wmY0iMp1qhDOE6JxNPQkwqCcGk63DUezcC-6j4XNtujqjcM6oQIaPEqXi-kJE4t8RQcg3NQiZb1qnp8m6FT264dW6EcFvFNFDboihj9zCw8kcZVss8HxOfkHBT4AUlvMFyDlt0UR8-Zrs9AsR4bef1S8cOTVesmCXzFvhfxcxhcw2qE35sdPXpn3hGzGGWNZrc1O_Ok9702zS7A5BT9POPOTdIneBYu4sF1kjTKQZxrtJfLCBy1SpKQDUsmznJAr0AP1-HhehngTMF1fOVW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورها همین الان هم اینستا هم یوتیوب
برای سفارش ربات زیر
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmsBdb4HnN5Xw4Fdo16EhI9jNQBsCnEsOW6z_m3NLDiCOuk4zucj4rcwkcYvoWmPFSVHqiHwQXSCCBvZyM-jIkF3lL3-P-1vp5BpNjLodk5ynUAL6l8xfXrPYZnXlVHTzM53MrdceHtTtNyHo6zM8rbAub4l_eZyBfPv8uz8WnPW7tqaE8iBOiChTdV3qvBQHDflaGRE3oZb9LA2Wkd7jvS5bUtBz6eAP71iKx83Z2Jg89EZrLeZGZsGju9COgILI9Lk876chtgOd6WJmDhEFWvigGU973T4b8QKOs_LgU4geuD7U53r37frfQuNlqE5AF471-Ieb5gYNokA0MBJKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8437">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2c72062a-a542-4b9b-97ac-0b636930d7c7@65.109.112.38:30366?security=none&allowInsecure=0&encryption=none&type=tcp&headerType=none#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8432">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U2bElJGcr7KgS7tYvZkH3laZixBnP60iHF9NhqjDlBc7XvqNF8Mc5fV3gbZuB8-uzjuKli9wfnp2lspjXeQv58f0CcpyfdY30dYLObA_M95ncCXSFGFT7nTZ35B88Qi2pdep48eK4fdQ1THSi55voPD9Oy9EEJOE0kODxgXHc7YGu6kZeo-nCnBmitKVrzrMsvCRtl4pv1wXkRJaZlVS14evjEtwFP92ES1hG5yUWH7kBP6aJi8Z6mG5_eFpiXT_HCb8OY1wQK4x5z4iKCgiMwT0F2BSstzeT16C62_PF7nx85YSzG4FPWUGIbLCwoU1tf9ITGYKWjJqbxZrqmwvCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8428">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ربات مجددا دردسترس قرار گرفت
میتونید ثبت سفارش انجام بدین
❤
✨
🔹
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/IranProxyV2/8428" target="_blank">📅 13:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8426">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiqME5qRNuqwpAqKb4sMUteqdJfJIlU35-8NgdPIFVzshk8LQ_qIsamnM7uGMbQTvXG41Ls-PEAdmIq2lqwJKE1S9K6Jcv_TcISHgS1Mea1SGpPOVdmHNsHmykdlF4l0erZ3IKnMcnXyczraKR_2lIQY1_UMibDkdStZtv5texyO1SOvWeqF3N04Q3t4HtT7ok52vE7CAvfWhP391cX-cYwHM9NhvppgFebDEvCuyXUAjYQ3AQMxXCho8aoCtFQ81U9MiATet6IOZoPlAwRWODDSBcdSn5DSHv-ROs_sGaJR3jJUVAnci9sdSE_YhP_f3voTJ3P37ctD2GMo_gIrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/IranProxyV2/8426" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8425">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=u_GJrp-GHDdG9hbMhRm_EVfUlvWVxiSSEUEwbLwwBh0Eir1JBbHzMW22S_XvVN8hMYRBjiGiO9vXnbvB9ZHuXEReinDIEfZzxgUOFq9cwNdkLA2J0p5zyrDQ8uIsTGATCTnBmBR_oB7drUUxJmpS6NDsAMR1nWcCGHq-r02Q_9sPqDGjEcmP95Dy8CWY_KRuuMFF_aCY5j_O5EEYkae8gN8uS26U3vR6nOYkP3CXCoJMbIf5ImHWO18o7FsS9paxxGbhnuFzbKgnHx7fi7IoUEmqNoae3JzQ-E9nD1upvCWOdMd78soqxPrsVVVDS_UZY4meN-6yO2KUKkjXmy9KereHRXsNh1Ed5cK60vu8yXhNvrDbmx_A2Mhs8pIt7jQVh7ewFuYeQ9GkKexkNxiZLYFsnsSHLXQ24Z6agGKqkxn7sCl2w8qygFsCl66fNu0Wk2QK2ouGb4ybOoJ2fQS-H8rcFxCEqXyf0Fx8QkenHqTeoUjJzWH72nVvyckUK2-74DArmcVSvxDoJzAXf1r7JvAKfk9QJV_sDe0tDYGwa5nwBPWI_ZPs27kcYiwT7oz4gEjie7_ZUww8fBe8Lz4YeBFjryuFeGyNObY8W5qadbYP5DlxDycD7CDEANmxpfwbm2SFIdkG-juDQxZRBmKUr0ezLUljxLXdy6osrIZSB2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=u_GJrp-GHDdG9hbMhRm_EVfUlvWVxiSSEUEwbLwwBh0Eir1JBbHzMW22S_XvVN8hMYRBjiGiO9vXnbvB9ZHuXEReinDIEfZzxgUOFq9cwNdkLA2J0p5zyrDQ8uIsTGATCTnBmBR_oB7drUUxJmpS6NDsAMR1nWcCGHq-r02Q_9sPqDGjEcmP95Dy8CWY_KRuuMFF_aCY5j_O5EEYkae8gN8uS26U3vR6nOYkP3CXCoJMbIf5ImHWO18o7FsS9paxxGbhnuFzbKgnHx7fi7IoUEmqNoae3JzQ-E9nD1upvCWOdMd78soqxPrsVVVDS_UZY4meN-6yO2KUKkjXmy9KereHRXsNh1Ed5cK60vu8yXhNvrDbmx_A2Mhs8pIt7jQVh7ewFuYeQ9GkKexkNxiZLYFsnsSHLXQ24Z6agGKqkxn7sCl2w8qygFsCl66fNu0Wk2QK2ouGb4ybOoJ2fQS-H8rcFxCEqXyf0Fx8QkenHqTeoUjJzWH72nVvyckUK2-74DArmcVSvxDoJzAXf1r7JvAKfk9QJV_sDe0tDYGwa5nwBPWI_ZPs27kcYiwT7oz4gEjie7_ZUww8fBe8Lz4YeBFjryuFeGyNObY8W5qadbYP5DlxDycD7CDEANmxpfwbm2SFIdkG-juDQxZRBmKUr0ezLUljxLXdy6osrIZSB2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از سرعت اینستا همین الان
برای خرید وارد ربات زیر بشید
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8425" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8424">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/IranProxyV2/8424" target="_blank">📅 12:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8423">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=nYvjLm7MkYq0RwB4g_N2LAV_xLpqpSilDXo2F3Hiefxt0jiDvE_1aUPiRwDAF9ljVcL7ZrdB8HlVGfMoiCs9diT6xbHoipLvsC3A5D2fhtgPKtD96XQmOeD4PdMuP60E7b9kjkEVMcYx4fn8rGxASnqdnShSs9S1xYjO90IKc7SCWcXG5PGBhrvAsUGfoA-zELd0ek3NwPcOSrjZId2hbco-LYKPHqxrCIJV_TEPbwcldznXhwzv9FcdJi3nY8-uLi2SlFCDlx_6ZLyK-sL_Pj_m2S57IbRBNv0YWt2N_uT0rQeiz3BXBJMUk9O8HtpYlSLwA0fSlKeRwrYYakf5tUP8hsk7iig4our9PjMzW73vMrTMzaBp8JnjxUPmN82aQU0lg55Usg6inaTX4jrEUiAKFSGIZxabe-U7nR-05XNiezoKwTALflw2JzTB00xm4dyk5gqv7qApZKDE4cXNG41DHtbyfeyiDDLJieN6hPS5p7JvidncGG9-hH6_egUfTPxzOP4WCMU8REL2MsAr00_xsIQrWouunUZe4q0VZRZBjyflNu1ER4jsROI3zuDNe7TcsD-iAy2vPHkRPLmYHu8IpIIeh0ueJ3VMQNQGk4ffe8AqUXQIqkkG5_m9KeO_ldAZ-dZ6k2ohgpSLle4rhFuvR25ZB04ZIkIqJooFQj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=nYvjLm7MkYq0RwB4g_N2LAV_xLpqpSilDXo2F3Hiefxt0jiDvE_1aUPiRwDAF9ljVcL7ZrdB8HlVGfMoiCs9diT6xbHoipLvsC3A5D2fhtgPKtD96XQmOeD4PdMuP60E7b9kjkEVMcYx4fn8rGxASnqdnShSs9S1xYjO90IKc7SCWcXG5PGBhrvAsUGfoA-zELd0ek3NwPcOSrjZId2hbco-LYKPHqxrCIJV_TEPbwcldznXhwzv9FcdJi3nY8-uLi2SlFCDlx_6ZLyK-sL_Pj_m2S57IbRBNv0YWt2N_uT0rQeiz3BXBJMUk9O8HtpYlSLwA0fSlKeRwrYYakf5tUP8hsk7iig4our9PjMzW73vMrTMzaBp8JnjxUPmN82aQU0lg55Usg6inaTX4jrEUiAKFSGIZxabe-U7nR-05XNiezoKwTALflw2JzTB00xm4dyk5gqv7qApZKDE4cXNG41DHtbyfeyiDDLJieN6hPS5p7JvidncGG9-hH6_egUfTPxzOP4WCMU8REL2MsAr00_xsIQrWouunUZe4q0VZRZBjyflNu1ER4jsROI3zuDNe7TcsD-iAy2vPHkRPLmYHu8IpIIeh0ueJ3VMQNQGk4ffe8AqUXQIqkkG5_m9KeO_ldAZ-dZ6k2ohgpSLle4rhFuvR25ZB04ZIkIqJooFQj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8420">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/IranProxyV2/8420" target="_blank">📅 10:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8419">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6Sr32H84wXmkt5bXr74-jIj-iNvkpgrWPZMjP_Dp1XtZAYQESCzeJ2vWyr9PoMmTk70vW179PLLr4u5L_bvGSn34M6APiCjASWVJXJM7ayXr32OiJbFoUDSCgMQQvVQuIBEVsOsertqze_zUHU8wUSJa60dvP4f-2jOkV7eNCYiuSYUuUl84RWztsuviat126u51oyZ73BQNkw-UDBNSZGQdFGe9c7n7u6sg0S0AD_hrDilUM_Z4UP70u3v0RyyLM4pYhU32NjFofvHjlmrS60EkNRnDM39t6zLRW9e1MRt9LwYtY5YCna3Iiw1jcFGRnLv0IZs9CPxTJ7h-a5BLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=150T
💥
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/IranProxyV2/8419" target="_blank">📅 03:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8418">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=nHiwnyCY0rdSPm_ANqdKH8_fo5nuKCMqAQmpAhU2axvaUzIiWbVt3XFE32GU_P2KEsTk7pP_FJRRk_Uz_tb39nL0RiaA6thHkKBgkZTUN1FoElJubP0IkpBgdihrysWZ_ZWqBEUL_TLCAP5r_dR5L8nR63wix06ZETpVCOQJIvXQ5nuoW_FEZNSebatRP1CNVoZzLqyfqm5PEsJlMrv9hG9xRFdJ8WvuiuPm5uQW8bRUBG4aYtIzek5-_tDoIYiTVVbAvGpX4u8NKTo_adnzHPrO7kx9iBBd0qyQ-QTvcF6E1Y-0jp6a7H2qaHByFBspdrT6ERXAttpTX76giLef8jvMHJbVW0DOnJSa9hL4L-n52kejMIusgrwjEV0_vA0YiCtTHpWQ_5X1es2Sw_Y6w1undss7wzkO5OXJ-ntfHgUuPDLBeqC2yJe8v8HHq_fZmWEHWAJmZU-vsbE6-DP5aL3kTyUcGrrp9lGOo8PJUBmNLnnGIC3GiXGfJj7vXcivNMui4F2i_jlH5iOZiVcn2LXiqD_fVXsSgA_clYH7PO16uPkAlvXvEl4rzJzryrRQpVzbrslL0CU2WpNZBf_fcaMIyPxq8PIo_x_Yk1uaNF48roUpURbC_N8Vn7asxLkfIMAVPScXTz3oAMACCWEkg18-Jh9GJW14qBl5nghXsmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de744c30fb.mp4?token=nHiwnyCY0rdSPm_ANqdKH8_fo5nuKCMqAQmpAhU2axvaUzIiWbVt3XFE32GU_P2KEsTk7pP_FJRRk_Uz_tb39nL0RiaA6thHkKBgkZTUN1FoElJubP0IkpBgdihrysWZ_ZWqBEUL_TLCAP5r_dR5L8nR63wix06ZETpVCOQJIvXQ5nuoW_FEZNSebatRP1CNVoZzLqyfqm5PEsJlMrv9hG9xRFdJ8WvuiuPm5uQW8bRUBG4aYtIzek5-_tDoIYiTVVbAvGpX4u8NKTo_adnzHPrO7kx9iBBd0qyQ-QTvcF6E1Y-0jp6a7H2qaHByFBspdrT6ERXAttpTX76giLef8jvMHJbVW0DOnJSa9hL4L-n52kejMIusgrwjEV0_vA0YiCtTHpWQ_5X1es2Sw_Y6w1undss7wzkO5OXJ-ntfHgUuPDLBeqC2yJe8v8HHq_fZmWEHWAJmZU-vsbE6-DP5aL3kTyUcGrrp9lGOo8PJUBmNLnnGIC3GiXGfJj7vXcivNMui4F2i_jlH5iOZiVcn2LXiqD_fVXsSgA_clYH7PO16uPkAlvXvEl4rzJzryrRQpVzbrslL0CU2WpNZBf_fcaMIyPxq8PIo_x_Yk1uaNF48roUpURbC_N8Vn7asxLkfIMAVPScXTz3oAMACCWEkg18-Jh9GJW14qBl5nghXsmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرعت سرور های همین الان
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ربات روشن شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/IranProxyV2/8416" target="_blank">📅 00:01 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8414">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUUK1snbwyMasz5gvECXXkNhClGYtJsCTdWcvPu9pcvbJ4BoidA3PTeHiQtBt8hmgiF7uvHdJeXzPfKScYWSr49q8C1qjK3Q--5f8wQXXTVdOnwsFFV_wfT-RDgeYCA5dzpIvc80NtZ1IvVuU2Mt5IR0554G3LIwqdl0QbyBa05Vg8vqrTjZD13Zb7sxVsm1aTmIYBYZucA84CEfbniO8V3QeYBEtGJlYZnH7mN39p-STKwlTVgREwuDu-vgs23ZQSKpsyBCKOdMseiw37TQYCY1ahu3ClEutG-RgEDauh5caa94IyWULattIYe-ECd0qu21mtwQ4H4rDc3VjucohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8412">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye0-9CzhAjFnqTzs8it7dTV78JGgtGtSoPzj9ppTw2Blc2KIy11P7hYxZXTxC7sxgeG6uYDuMuwSaWKZVFDLUtxh83A28U4j7wjSZrMCALbn-wkZZ4znLYYdf6bEsQZdS2Eh_davfR4uac3ZbXHYPC1TqldonO-XFL40OgZhDPjJZYVg0Vk-Raav28-g0gnI0CJ9ViIawcmkmLuKMYeP1XemmfFYCjG1E806ABrYrVVKDYJoW_vUaSSs0ImQXcwy7CIo5gLYXC-Y1xMeogMb8FbuKUO9VetskLgY4eIazxiUyAHl379AP_pLdRbV5200pWbQg2DJVc0pZTjuMDdj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/IranProxyV2/8412" target="_blank">📅 12:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8411">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=Pxa4B5JE9yOfNdU17zIc6WFlVGIZy_uzEsyMRF8AQcAcRc7wwVousuxVN3FePVO9q1d7o7-oZ9PBDqPYlMaMLTNzA15vn5qaPT7ig8BBfjHZOksMWg0WqLI3Ymy3FGv_Q6DamvIMvV2UMdNce69zKsmH0Ak2dUdfIoWhtjT2eF6Lq_CtOT98QMF42_EOZA9wOEDyyRdkyoV6_I__YJvMUgPCOOqbgUex3MiKvipwh_EgPLrpsg0Obfr7z0Z4VZ8KZ82ExTq1vYSYg7rTmCN2IpI1x8GhAQKA4JLAubmQhOoHW5dG2Wl8UJaxBYIhE_5kB0vg0rVschwp43cK9SuKrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=Pxa4B5JE9yOfNdU17zIc6WFlVGIZy_uzEsyMRF8AQcAcRc7wwVousuxVN3FePVO9q1d7o7-oZ9PBDqPYlMaMLTNzA15vn5qaPT7ig8BBfjHZOksMWg0WqLI3Ymy3FGv_Q6DamvIMvV2UMdNce69zKsmH0Ak2dUdfIoWhtjT2eF6Lq_CtOT98QMF42_EOZA9wOEDyyRdkyoV6_I__YJvMUgPCOOqbgUex3MiKvipwh_EgPLrpsg0Obfr7z0Z4VZ8KZ82ExTq1vYSYg7rTmCN2IpI1x8GhAQKA4JLAubmQhOoHW5dG2Wl8UJaxBYIhE_5kB0vg0rVschwp43cK9SuKrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمامی باگ ها و.. برطرف شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/IranProxyV2/8411" target="_blank">📅 12:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8410">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/IranProxyV2/8410" target="_blank">📅 10:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8409">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">درحال آپدیت دیتاسنتر هستم، اگه اختلالی بوجود امد احیانا صبور باشین
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8409" target="_blank">📅 10:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8407">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWJib9gB3Delb4P7c-eTJai-ngpUJlC_lI6GOLymUFD5-QRTZk0pc-5w6J7ws7qOidBWpiBeKZYlZX_UgAmD_gx6ZaGL-zaAsMwTpZOUrZnguQ7WO3rorJNy5ehmpXx15dr8VGggPoxiTeqHJSNEEp9RUBK7soaOulz1chg01Hoc2fPOuN7Q4rJO4jHtQw_mY5JmIN8s1PODUcliaZJZE_M_IagQBql4KiZ0xpMs_AG24-kdIfelvFd6Y2IWaQJLR-Cm_IbWdZys1kWZT5ke3IXLeq3OGLrPDujRCVpp7oi6wgVO-ErZ4IVuLO7_0W9t7hVjCsh_NXwxOzSFAYl-2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=180T
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با
تخفیفففف
🍸
💥
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8406">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://2261382e-40ad-4259-9564-33734d96cf5c@varzesh3.com:80?path=%2Fws&security=none&encryption=none&host=nobody.fasterspeed.ir&type=ws#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/IranProxyV2/8406" target="_blank">📅 20:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8405">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHa-y5uMif7nHH3QK-mj5nS_N-D8KsNeru-rGPIB8STa63TevxMWH4olOVFMQj_AcPZmaUYnAF6n_cuMiaNuSNJ_ms-aQZgVrHrGs4siYTgejntDBuBPHPo8Ya4TOWEVg3rrsbk9epVTyr1yvHgodnQYmYgIP9OIXSaYON-iFv3o6IwZfsa0DKJ8QZwO9nRjTC3cjk78wC41ZJi5SJkXIvtC-SlkDx0Vpmy3wpqhOndngF0A163boas9FIAE5Djp25kjwUUM9aAbjbL5I7U593ob2O8r-emGYY4XxwvRehgpQy4mCHBUIrU7TVQLIhjm_omUbWfo6n6oHtiBjUGyYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8403">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)  ‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)  ‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)  ‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)  ‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)  ‏
✅
…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏چالش دو گزینه ای با موضوع  اطلاعات عمومی
📚️
‏
🥇
🥷
Sara: ‏(۱۶۵
❣
)
‏
⚪
❌
⚪
⚪
✅
✅
❌
⚪
✅
✅
✅
✅
✅
✅
✅
❌
✅
✅
✅
⚪
‏
🥈
🥷
Freya: ‏(۱۳۸
❣
)
‏
⚪
⚪
✅
❌
✅
⚪
✅
⚪
⚪
✅
✅
✅
✅
✅
❌
✅
✅
❌
❌
⚪
‏
🥉
🥷
hossein: ‏(۱۳۶
❣
)
‏
⚪
❌
✅
✅
❌
✅
⚪
✅
⚪
✅
✅
✅
✅
✅
⚪
✅
✅
✅
⚪
❌
‏۴ )
🥷
Dystychiphobia: ‏(۱۳۴
❣
)
‏
✅
❌
❌
✅
✅
❌
✅
✅
❌
✅
✅
❌
❌
✅
❌
❌
✅
✅
❌
✅
‏۵ )
🥷
- Amin -: ‏(۱۲۹
❣
)
‏
✅
✅
❌
❌
✅
✅
❌
❌
❌
✅
❌
✅
❌
✅
❌
❌
❌
✅
✅
✅
‏۶ )
🥷
𝐑𝐚𝐝𝐢𝐧.𝐳𝟐𝟎𝟎𝟕: ‏(۱۲۳
❣
)
‏
✅
❌
✅
❌
❌
⚪
✅
✅
❌
❌
❌
✅
✅
✅
✅
✅
❌
⚪
✅
⚪
‏۷ )
🥷
Matin: ‏(۱۱۸
❣
)
‏
⚪
❌
⚪
✅
⚪
✅
⚪
✅
❌
✅
✅
✅
✅
✅
✅
❌
✅
❌
❌
❌
‏۸ )
🥷
𝘿 𝙀 𝙑 𝙄 𝙇: ‏(۱۱۵
❣
)
‏
⚪
❌
❌
❌
❌
❌
❌
✅
❌
✅
✅
✅
✅
❌
✅
✅
✅
⚪
✅
❌
‏۹ )
🥷
Paranoid: ‏(۱۰۸
❣
)
‏
✅
✅
✅
⚪
✅
⚪
❌
❌
❌
✅
❌
⚪
✅
❌
✅
✅
⚪
⚪
✅
⚪
‏۱۰ )
🥷
Robert: ‏(۱۰۲
❣
)
‏
⚪
⚪
✅
✅
⚪
✅
✅
⚪
❌
⚪
❌
❌
❌
❌
✅
✅
⚪
✅
❌
✅
‏۱۱ )
🥷
♧: ‏(۹۹
❣
)
‏
⚪
⚪
❌
✅
❌
⚪
❌
✅
✅
✅
❌
⚪
✅
✅
❌
❌
❌
❌
❌
✅
‏۱۲ )
🥷
Zaker: ‏(۹۷
❣
)
‏
✅
✅
✅
❌
⚪
✅
⚪
✅
⚪
✅
✅
❌
⚪
✅
⚪
❌
⚪
✅
⚪
❌
‏۱۳ )
🥷
✗ᏦℕiႺℍᎢ✗: ‏(۹۵
❣
)
‏
⚪
❌
✅
❌
⚪
✅
❌
❌
⚪
✅
❌
✅
✅
✅
✅
✅
❌
❌
❌
❌
‏۱۴ )
🥷
❥sheyda☙: ‏(۹۴
❣
)
‏
✅
⚪
❌
⚪
❌
⚪
❌
✅
⚪
⚪
✅
✅
⚪
✅
❌
✅
⚪
✅
⚪
✅
‏۱۵ )
🥷
Ахмед: ‏(۹۰
❣
)
‏
⚪
✅
❌
⚪
❌
✅
⚪
✅
❌
⚪
⚪
⚪
❌
✅
✅
✅
⚪
✅
✅
⚪
‏۱۶ )
🥷
Ali Moheb: ‏(۸۹
❣
)
‏
⚪
⚪
❌
✅
✅
❌
⚪
❌
❌
✅
✅
❌
❌
❌
❌
✅
✅
✅
⚪
❌
‏۱۷ )
🥷
Vista: ‏(۸۴
❣
)
‏
⚪
⚪
⚪
✅
⚪
⚪
✅
❌
⚪
❌
❌
✅
✅
❌
⚪
✅
⚪
✅
⚪
⚪
‏۱۸ )
🥷
ㅤ: ‏(۷۵
❣
)
‏
✅
⚪
✅
❌
❌
✅
❌
⚪
❌
⚪
✅
❌
⚪
❌
❌
❌
✅
❌
✅
⚪
‏۱۹ )
🥷
Mohammad: ‏(۷۴
❣
)
‏
⚪
⚪
⚪
❌
✅
⚪
✅
✅
⚪
✅
⚪
✅
⚪
✅
⚪
⚪
❌
⚪
✅
⚪
‏۲۰ )
🥷
✨
𝒫𝒶𝓇𝓂𝒾𝓈
✨
: ‏(۷۲
❣
)
‏
⚪
⚪
⚪
❌
⚪
✅
⚪
❌
❌
❌
⚪
❌
✅
⚪
✅
✅
⚪
✅
❌
⚪
‏
👥
و ۶۳ بازیکن دیگر با امتیاز (
❣
) کمتر از ۷۲
❤
خسته نباشید
❤
‏</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خب بالا باشین</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/IranProxyV2/8398" target="_blank">📅 20:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ساعت 20:00 امشب یه چالش سئوالی چهار گزینه ای برگزار میکنم، با جایزه یک گیگ کانفیگ برای نفر اول باز، امشب مجدد به غیر از این چالش برگزار خواهم کرد، زمانشم اعلام میکنم حتما
❤️
🍸</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8395">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2A_URXUIKu0lifoTk1PYXqA0hx-lhG81NzYNSJt7L86WGYf0WquyIeM0wZcBylP73fE2GrAc6NNPk4PLaXP5IEo37XZt7PWN-6w-PqXds1k3XZo5hXwqwu2S6dALF6Mz_drHyor-hwvKKKhSwWTqdL3xeu-8otuQxYEfQaen9OZ10eq8ytliY_2vaLL9NImjr0DrR-UlLo9_7uc8d2EP8Tzw5mqqk6zw3KGC3csE3SDqT_D5T2gn901-C6OkkwEevMlpD3m9ZTwaF49QmAe1v8y7XsWrTKRYIYzj3cyod4t9X4z8rnmoy61H9cZvNTiJQOGNyLNp4IlhJwzjCWbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن و بصورت آنی رسیداتون تایید میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8394">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/IranProxyV2/8394" target="_blank">📅 14:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8393">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">𝗩𝟮𝗿𝗮𝘆 + 𝗣𝘀𝗶𝗽𝗵𝗼𝗻
vless://36326231-3138-4166-b834-303439306131@185.143.234.96:80?encryption=none&security=none&type=ws&host=dl.tgmovie.bond&path=%2Fl%2Fw%2FaXD2QyDdS6vRQpxs%3Fed%3D2047#%40RUSSIAPROXYY%20%F0%9F%87%B7%F0%9F%87%BA
ℹ️
تعداد اتصالات بالا بره، برای وصل شدن به مشکل میخورین، این کانفیگ های رایگان فقط جهت اتصال دوستانی که نمیتونند هزینه ای بکنند و دنبال این هستن اخبار چک کنند خوبه
📌
آیدی ربات جهت خرید کانفیگ اختصاصی
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8392">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پسرا روزتون مبارک
♥️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/IranProxyV2/8392" target="_blank">📅 14:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8390">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=jHj6rphfJYrFsdXGRbho-NSv3P6_mdF_0wqRDwQrABKcGaCFcRu8T9-x7vuiEPhKU-tmznBo_ydRhwiqvki5DTOOrGYfTbbCruOyYdGIcl9nou3BRk4NnQJpij6H2eyNoq0dgmVk50Gouc7TecpdL3y3zyUY3CFhcddIX93RZs4SE2hadcNnJ0ADey9eDxApbNoFTsI7UqQzkKKz3W58RKB_vChNvJcv14qrNb-cl1Lbzg9UQr_wznzv7dZE-2LDmUxqlXQAGXiXQlDJNum8ct7cd7_r9nw_-Faze6seJEGOAQ9esX4LIkHKRe8NnfG_20miPUhMygYb165LZpc3-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=jHj6rphfJYrFsdXGRbho-NSv3P6_mdF_0wqRDwQrABKcGaCFcRu8T9-x7vuiEPhKU-tmznBo_ydRhwiqvki5DTOOrGYfTbbCruOyYdGIcl9nou3BRk4NnQJpij6H2eyNoq0dgmVk50Gouc7TecpdL3y3zyUY3CFhcddIX93RZs4SE2hadcNnJ0ADey9eDxApbNoFTsI7UqQzkKKz3W58RKB_vChNvJcv14qrNb-cl1Lbzg9UQr_wznzv7dZE-2LDmUxqlXQAGXiXQlDJNum8ct7cd7_r9nw_-Faze6seJEGOAQ9esX4LIkHKRe8NnfG_20miPUhMygYb165LZpc3-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=ckDuyNuUy3IX8sh97OoTThGba-8medpnw8qK_ZZZTszHISVzTmWJX34XMgO5skbTK223o3ojPQCzFu-71HPXqSELX0QUtBB1zwJFRlUH5OGRStie0PBjgmzyIVO0Fd0qqAIPGqZ9s0XZj1e5bCdHHSqxJQxESAvx67YQRXPRB7IL_6Vz7TOjLL0PqIaZZWZg-Het3SLre_awt-quyU2ULgn-6GjbWWkdkPnN1YLEcaj7klMOKFkycoNz964dO9ryHE4EriAIkHMQ-qYkZ_A_dTUWYp0x3SYM6agJzIJhxeN6RDblH5JIJSPwpYIPpNK-nQ5CNK48pBW7GWucGND1ipSJ5m2p8H8LvtyXQuGn2u1T_Otu5wDEN7Op9MLddle-c4uDv_W1kHge-t_jZkJRWo42RRpcSMm7imWbiLGxzAL7W7q7hIKJu2NprKPNMTfbYvWoqiGGq2K3UlAEVmnC9rlZSOX_CcNmYCS5ZlvQ0Y4BjGr5iJBGSycBbPVbMvJL69wBPVdQsq6HvnsMrcCTC_OTAlX7HjGPN66BgELpLyDfbZAzB5G7r1UqcpCQlVG_E8dGGM7RQpsrMxUgd-1avKr7_kCxh0jpxHUve9eqDjBqdto7_LtkV9Vg66avTQRAL-XubXaFITfkAcl0ckvBuGfeDYxld6ro9orFk4PIjgY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=ckDuyNuUy3IX8sh97OoTThGba-8medpnw8qK_ZZZTszHISVzTmWJX34XMgO5skbTK223o3ojPQCzFu-71HPXqSELX0QUtBB1zwJFRlUH5OGRStie0PBjgmzyIVO0Fd0qqAIPGqZ9s0XZj1e5bCdHHSqxJQxESAvx67YQRXPRB7IL_6Vz7TOjLL0PqIaZZWZg-Het3SLre_awt-quyU2ULgn-6GjbWWkdkPnN1YLEcaj7klMOKFkycoNz964dO9ryHE4EriAIkHMQ-qYkZ_A_dTUWYp0x3SYM6agJzIJhxeN6RDblH5JIJSPwpYIPpNK-nQ5CNK48pBW7GWucGND1ipSJ5m2p8H8LvtyXQuGn2u1T_Otu5wDEN7Op9MLddle-c4uDv_W1kHge-t_jZkJRWo42RRpcSMm7imWbiLGxzAL7W7q7hIKJu2NprKPNMTfbYvWoqiGGq2K3UlAEVmnC9rlZSOX_CcNmYCS5ZlvQ0Y4BjGr5iJBGSycBbPVbMvJL69wBPVdQsq6HvnsMrcCTC_OTAlX7HjGPN66BgELpLyDfbZAzB5G7r1UqcpCQlVG_E8dGGM7RQpsrMxUgd-1avKr7_kCxh0jpxHUve9eqDjBqdto7_LtkV9Vg66avTQRAL-XubXaFITfkAcl0ckvBuGfeDYxld6ro9orFk4PIjgY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور هامون همین الان در یوتیوب
برای خرید وارد ربات بشین
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/IranProxyV2/8389" target="_blank">📅 13:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8388">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امشب باز براتون چالش برگزار میکنم با جوایز کانفیگ بیشتر، این دفعه بصورت سئوال چهار گزینه ای هست چالشمون، ساعتشم اعلام میکنم بهتون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/IranProxyV2/8388" target="_blank">📅 12:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8386">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcQjIftWEWc-xck8yqPkS6ABgMnNtGeIDt3Wwm2rnwPn1o48BZSUbdpJy-0st6danmd5GyEkJui6K5xXZJkpwj59vzKBK1l432g4uqfq9HWsHp-j3NY9IgDvIQN_xX1Gmpv6tCKXGbIF5d9rPNdOaDRohJES0eHvtFGR8uJLoh05jzRuckvTpDu6gR-Gt9fAD7QYoquDSBxPKmyEsvgCsKFhd7Pe6vL84xUGASCkxwE0iKlpYQDhp7HWSYTjsyKBPCkmQg6fTPDvfDpjAAnwRuDWhIu963qk2awVem7H91X6wGeybI0bCmzfdn-twH_fW3cV_f_gBiVal9sM0edyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سرویس سرور v2ray برای همه پلتفورم ها و اپلیکیشن ها با بهترین سرعت و کیفیت
⚡️
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8386" target="_blank">📅 04:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8384">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHRgd-ku-a1NfRpwL05OfueeO6d2PMFKcebrh3pw8eu2n4VqahKK335CIc_AoBJFm0vw9wRZlKb28eAxv0y-DMHWONojalJt9FBvfRG8MERlgOgijpzAUlYfM5x365-xk4Ymvd_FlZ66JoeIo6uGh2yFg3kvVhuDeqP8Slp-C1EebrmwPDKf4fpkUhTTp0yvQ3kycl8jVDlPnCl-OaBy48UkWpCyVFg80Hz_JFzZb0ETL4GUMprTn3HxXhh33vYKn5hT-t9srwQscgOjVpq1yT1z3hBvGnu7FOUWk1V08i47dHL6tW3WXghkF91yrHhi2FNnYqjCJjyRrXPQfvaSXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
کد تخفیف حذف شد برای راحتی قیمت هارو آوردم پایین راحتر بتونید خرید بزنید
🆓
1 GB=190T
💳
توجه کنید پلن های 1 گیگ، 2 گیگ، 3 گیگ و 5 گیگ تو ربات موجوده با همین قیمت
🍸
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/csxi-iNsYakXEA0Dpo4R_Yfth6wZ9bZOJwB01BX1jGi63bqRhi11nSyDZo4hJQQIffgfDidsXW8sqqCbT90WcuOhkM38-6mMkNN04WQHRf7Nv7jyysNnm__PFHfR5jKHo1yOp-7taXvMKJ4TrAUy1my8oZ-VsyiID_UdfVF7yLKxHRiFyJkNzxpPOxTVoW0ItYnKY2xZ66iHghZ-NLVs3_xhh3TWzF9ieCz-uNZ1L56gIv2vSU66R_NbfLr737muVD-Hgww_5LIrvh3vaXmRprRODjSVazxMUtC4MATaSzoeSlBXSy3K4eu1kBsTzzk9HciTt0UsQeCFUQWP7oh7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8369">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/IranProxyV2/8369" target="_blank">📅 23:39 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8368">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/IranProxyV2/8368" target="_blank">📅 23:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8367">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=k6GMweJRpcTa9cVOEqiDz1y83-chJx12ZqvHqsu0QlY-GuNgBSkV-FB4anOkecguOSJWivmoJH-OBrmgGVt-WROqALmx9IObCloyqOc4TyaaORiO6F7f5iEKcR3oGnYVVrQ_e2kasQFCzrxv2TBca74H39_COV_ChvmWMMdp9mES3OaeWyxHwAr60oAMqa1wRbGaS87hL-e34PsmdNvllxjcsZPDRffWBD4jDiORjWwjEhSQA9ny4PIWk9K4sejukH7Ob2HFpPs-FvxS5kqiAFrXYi8G_rvODZAZkBV5P2d5yLWn7JEhybYiZO0jhe4XsFPpg1lVo7QaHXvaF6IQDHUluXDoyaobbjcJEGgdnggyAxBA8Hi5qwBmIxsc0Bh5VI8O3nH2JQz_Qiun9YZYtN-1z4bsxcC0JZyBhiDQF88KjmQPcTkBBFYdajZe-M9p2h2tefKoplzalCCfRfLUGIvZMm9UtZgwu7VprMeedIrNLwCsUKG-hD0_o10HwOAbOg1bmHyE_lYUyYf8CNya9CrYjz1DsLw7jQt5HBSFeKSEiaDW4mO_LqPLKWapywo6HtC6NPWmCXZ-3zlyyJFVnJLDYfDbujhZFz5rsfnnRBAdSoLTWaWzdi1y3TybQHPBrvQ996zwon6MYSu1Vsanpr1FRLhvMW019Udw-sqDhTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=k6GMweJRpcTa9cVOEqiDz1y83-chJx12ZqvHqsu0QlY-GuNgBSkV-FB4anOkecguOSJWivmoJH-OBrmgGVt-WROqALmx9IObCloyqOc4TyaaORiO6F7f5iEKcR3oGnYVVrQ_e2kasQFCzrxv2TBca74H39_COV_ChvmWMMdp9mES3OaeWyxHwAr60oAMqa1wRbGaS87hL-e34PsmdNvllxjcsZPDRffWBD4jDiORjWwjEhSQA9ny4PIWk9K4sejukH7Ob2HFpPs-FvxS5kqiAFrXYi8G_rvODZAZkBV5P2d5yLWn7JEhybYiZO0jhe4XsFPpg1lVo7QaHXvaF6IQDHUluXDoyaobbjcJEGgdnggyAxBA8Hi5qwBmIxsc0Bh5VI8O3nH2JQz_Qiun9YZYtN-1z4bsxcC0JZyBhiDQF88KjmQPcTkBBFYdajZe-M9p2h2tefKoplzalCCfRfLUGIvZMm9UtZgwu7VprMeedIrNLwCsUKG-hD0_o10HwOAbOg1bmHyE_lYUyYf8CNya9CrYjz1DsLw7jQt5HBSFeKSEiaDW4mO_LqPLKWapywo6HtC6NPWmCXZ-3zlyyJFVnJLDYfDbujhZFz5rsfnnRBAdSoLTWaWzdi1y3TybQHPBrvQ996zwon6MYSu1Vsanpr1FRLhvMW019Udw-sqDhTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8366">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔴
به درخواست شما دوستان مجدد از دیتاسنتر روسمون مجدد براتون، دیتاسنتر با تخفیف موجود کردم با پایینترین قیمت ممکن
◀️
تمامی پلن ها با 23% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=220T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن و با ساب ارائه میشن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/IranProxyV2/8366" target="_blank">📅 23:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8365">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrILzvDrEmi_nVHUbABAbvN4TIfsxiogA4pQQ3LDJmkbhOxc0EDtw2IzDjihda7YQ821qeeX7TKeGUqXTlzIKIPe3Fpz5t9KfDCYNVonHE8SIDsBJwGB3N28DWQ2Hy1VXVPGedhHUxE8HMibmER66Fm5y1s4W8-ugW91K-dDv97ZyqWtdAGehbP670IMrLKIQJ16MobfFCL_mLu_lJM3uClEPnSeVJ5puclCiEhYZG4Un4KAWzoHcHXedgpq91ORLKFGU0bfGSLqntZuHZmiBa8gjg5JRkhb4wAZ4VzZ7GLWL__t8UmyUFvDD0DBuo92OPebjCQ-tSN1MW_nVh3DCfM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=m-PI8gRfMNEfR0z0PJL9_S2_Mvz4m-veLxGLUz4zVVDax3vmy1BuH8oDCDauOwKQUelqrj6P7C6QfOKSafDfw151t9uBIquACNJMqH3Nnr0pLUt0ZvDFIfbgjw3zbM2b61NHlLHh8kfZfhTNBrp_ya3bV8-QKvWslxGuYYQucNdQw50D97aWMO_2z_GCHORS03O4oAjmWPRi2eq56oYKBWUIxEvMd36L12EXLrl9adZIJtFw2Rxl9bK_QLZZLIst8q-bcA_WNknzMkUfkCgPx-1z5wmxsTnhV28ITsPQhdQYJUbylBP1MxV52_H8JHhWYAHxsB2QKD3yKbsQ89ydBrILzvDrEmi_nVHUbABAbvN4TIfsxiogA4pQQ3LDJmkbhOxc0EDtw2IzDjihda7YQ821qeeX7TKeGUqXTlzIKIPe3Fpz5t9KfDCYNVonHE8SIDsBJwGB3N28DWQ2Hy1VXVPGedhHUxE8HMibmER66Fm5y1s4W8-ugW91K-dDv97ZyqWtdAGehbP670IMrLKIQJ16MobfFCL_mLu_lJM3uClEPnSeVJ5puclCiEhYZG4Un4KAWzoHcHXedgpq91ORLKFGU0bfGSLqntZuHZmiBa8gjg5JRkhb4wAZ4VzZ7GLWL__t8UmyUFvDD0DBuo92OPebjCQ-tSN1MW_nVh3DCfM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
وضعیت سرعت سرورها
@RUSSIAPROXYY
🇷🇺
📌
آیدی ربات جهت ثبت سفارش
👇🏻
✉
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/IranProxyV2/8364" target="_blank">📅 16:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8363">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان عزیزدل، یه تغییراتی رو پنل ایجاد کرده بودم، برای افزایش سرعت و رفع باگ ولی فراموش کرده بودم ذخیره کنم، به همین دلیل یه قطعی چنددقیقه ای داشتیم اوکی شد، پوزش
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/IranProxyV2/8363" target="_blank">📅 16:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8362">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏یادش بخیر یه زمانی اینترنت انقدر مفت بود که از ویدیوهای اینستا به عنوان چراغ‌قوه استفاده میکردم
😄
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/IranProxyV2/8362" target="_blank">📅 15:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8361">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uda3iHhZbp2KabZ25A8Rpky4GPGl6PltPCf4GuA_FyHHKZ0kChUaPZaxjIvBDS7AMzRj9z926wqiifn6Ec6lmNVAvFSbzp1QRu2s6AIBDIu2au1qOdWB-zoC2FjrCSQxJBKlAHrsFJ8zl2OrjGbYdo4ubV8jXZ7FUnsF8903LrVw8CmoC2fT_ct8v6B2_FiUX7O5IiPQWOZCTwMhOb8dDTYs8hA8996ruHmOn7U6GEi07se3dbAZexwmKLcjg-48yEipK0kaS02u2WPIHQgf9P0Lw9tfHOBkPykfzUZTZJVz8pbGHbXK7a6j7h6BV62q5jMuATpN5HGSfyBvHW3KeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهبازی،مجری صداوسیما: بهترین کاری که جمهوری اسلامی تو 47 سال گذشته انجام داد ملی کردن اینترنت و دادن اينترنت به اهلش بود نه يه مشت مزدور داخلی!
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/IranProxyV2/8361" target="_blank">📅 14:32 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8360">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/IranProxyV2/8360" target="_blank">📅 11:56 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8358">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8358" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8357">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 2.19K · <a href="https://t.me/IranProxyV2/8357" target="_blank">📅 04:09 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8354">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/IranProxyV2/8354" target="_blank">📅 01:53 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8353">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PA16IgKXagkMuqMrsV9PQ3I6I_fcm3vJtZxY7qBVtZpMDuo3GJXuNef2EFyuNJVeHxGEb-697SQs5mYmMi2Cbo-8KtoXiRSM7ok8EtIHKsQ8vbB5hGaeT0faXEBnPmemvlG3x3S7iEeRNPH_I3l3nV2LGz4c69yL_yTEP14cGkMuYmy9U6BQv_Bbn4wYJ_zw2s-Qfgb57_Nq0o_Bakv83zjsVijN8XC2Qqgh9N4B9S_fyu6O1mBx1xK57Y8LljwM5xosVjLpPv4ytdW-8V9VNOQu4YJKzH9ynE-4j2Yje81n8dzUBHvrPmzAhHMdlHm7enKig2Abtrafujz2hG-srA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بابا عجب
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/IranProxyV2/8353" target="_blank">📅 01:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8352">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف: freeiran
➡️
🆓
1 GB=250T…</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8352" target="_blank">📅 01:21 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8350">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
به درخواست شما دوستان تو این شرایط بد که کسب و کار ها خوابیده، تصمیم گرفتم که طی مدت کوتاهی کد تخفیفی قرار بدم که دوستانی که شرایط مالی جالبی ندارند هم امکان وصل شدن و خرید کانفیگ داشته باشن
◀️
تمامی پلن ها با 32% تخفیف
🎁
کد تخفیف:
freeiran
➡️
🆓
1 GB=
250
T / 170T
💳
دوستان دقت داشته باشین که سرویس هامون هیچ ضریبی ندارن
❤️
✔️
برای ثبت سفارش به ربات مراجعه کنید
🔻
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/IranProxyV2/8350" target="_blank">📅 23:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8349">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امشب یه سوپرایز دارم واستون
❤️
🍸</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/IranProxyV2/8349" target="_blank">📅 23:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8348">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">✈️
درود عزیزان، امروز یه مشکلی پیش اومده بود واسم یخورده سفارشات با تاخیر انجام شدند و اینکه دوستانی که امروز خرید کرده بودند، رباتو چک کنید حتما
🌟
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8348" target="_blank">📅 22:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8347">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
شهبازی، مجری صدا‌و‌سیما:
بهترین کار نظام تو ۴۷ سال گذشته، ملی کردن اینترنت بود.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/IranProxyV2/8347" target="_blank">📅 21:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8346">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">slipnet-enc://AQskvHpoSr0z/luIGDACbhKreNDTKyhhMA3DYlYmmHhr6T/THqqypSEZIR2ROKHLR6XP/iribGUsJGd/wwwh1ZLFTrR6kKY78tIX6XmbL6eLIwT2+Az997HmcivFgJpEtgDTqAQVkonbDemLykPWC/L86oUN+Bfoqg7S+FVTAWD2NIQa/11CwodDdSWh8KTKoVIV80wPNJXSS2qi4THuGu5jEoTVOenuOImriz65wsm4ASSgo750zT/dZvGGj0ynpjQVa+y9hxbby3u0Lu0qbp27pnXaUHzmoEh3jQVIQi5OAcX4VvcUetwhOtV6DXHU+vsZPWDcQUOpd/7/0wZW+EUN24SqPt9fGMIsFsKpHXPoJpUs2BB1PkC8TZymVkqwmjeO0Cey8oj1g+DCiR5r1jtWijUAv4yehzdzbDuU++T1J6Sj0nP7ADo9wGFllaneHyrpoGHXRSCiQtztJKw7qwEWTLBo0jLT1Lt76HyJ0xGn6lPM+evyYA4Pd3E1bwcaa9kh6kJ0BTIjfT2UBa+zd2L+UejzTjqrKrYW6whN792AmDFdS9CHY7Ho7F2PZf+wQx4E0BjdJ7MFpNfblxmmgD2SsxRqH/7IpWpb+mr48+kqlveInlB9RKTxdzdfufoY5s82opLQBhAsuyXEhcqMYgRLIUsUXiILutNRoc/vBq41mI4B02bmpcZR6JmcYTcU1pjWop1QQPNvo89WaaJWZxYBCjO+TtbhLFsN9VTXdVe6fMSNo524sRPA3Kk04YuQk3cugUbywKo/BUXCnss9G7ffIJgmxd6UK5GIunGf
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8346" target="_blank">📅 20:07 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8345">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=C4OP7EE6WsJSSPM362pzZdE7nVJa4CjKL_DWI0miYDyH1HCe-F-27UMzayD3wBDCAU_9AbkHe6pOI7IAmiZx3Jyp_LYHu_lA3PJQVwoHW1q3zyWeaU0PVTRt78EQjcfAAo3tc3yRZ33Aa4xPwDjkU2S64vj_tldtVc1V2EgcOaIuv2BrP28yU7BdJ7Q7vwXb8k5BzqLHc1kAAy8psGRq-j04mp2KjD6Wl0fFIlpT6fRmh3Ut-lHAfuG74ug9FZVv3ABddFPIAiBEQsUdpbk8LPNvXvJzFHezExCvblZ6dhe6tOm3P_jSAhLDxFdXRIR82QUthzxrsErKl5fI7QJvHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72f95f0235.mp4?token=C4OP7EE6WsJSSPM362pzZdE7nVJa4CjKL_DWI0miYDyH1HCe-F-27UMzayD3wBDCAU_9AbkHe6pOI7IAmiZx3Jyp_LYHu_lA3PJQVwoHW1q3zyWeaU0PVTRt78EQjcfAAo3tc3yRZ33Aa4xPwDjkU2S64vj_tldtVc1V2EgcOaIuv2BrP28yU7BdJ7Q7vwXb8k5BzqLHc1kAAy8psGRq-j04mp2KjD6Wl0fFIlpT6fRmh3Ut-lHAfuG74ug9FZVv3ABddFPIAiBEQsUdpbk8LPNvXvJzFHezExCvblZ6dhe6tOm3P_jSAhLDxFdXRIR82QUthzxrsErKl5fI7QJvHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینک از وضعیت سرعت کانفیگ ها که بخاین تبدیل کنید
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/IranProxyV2/8345" target="_blank">📅 19:46 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8344">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">چون پروکسی هارو از سمت سرور خارج بستن متاسفانه از سمت ما مشکلی نبود اگه از سرعت اینا ناراضی بودین میتونید برید پیوی ادمین لینک هاتونو بدین بهش تغیر بدین سرورتون رو با سرور های کانفیگ عادی با سرعت بالا یا هم صبر کنید سرور خارجی پروکسی ها درست بشن   ایدی ادمین…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/IranProxyV2/8344" target="_blank">📅 19:33 · 23 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
