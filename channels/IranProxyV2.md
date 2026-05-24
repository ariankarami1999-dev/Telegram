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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 11:48:48</div>
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
<div class="tg-footer">👁️ 919 · <a href="https://t.me/IranProxyV2/8480" target="_blank">📅 10:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkd0qWTYJqEJnKoAw_ysnO8g50-pD4C4zeFWu1ZwKRAvxg9j5vueLmCHsrlFvEOuVfqwcp0A-XvNFiuwdE27HsJOcuMlEh-RUKyOJPIlFfpgAOV27BESrjI-zgENGDNRWHX4y7tzPgEWtrK4uY_vMKFmbSj1uUEJf12wNdqmYrkv-r5dLqWFQe7f1ZkBSh2Poi17XFfobq_vx8wfOCK3m0Rp-mINuRZr0Y1PT6EltxKeeCQDhdfsyihvmHhpO3yxnvZBmdU9kxs9kvhoFWigm2hyL-EXm6-SMNk-2UZx1CpX5YHJBOIcwZcbKXYyHWndM8JdP_3prbLxdqeohxSliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی خواب بودین، آپدیتی رو سرور ها اعمال کردم، که هم بهینه شد و هم از همه نظر فیکس شده باگ هاش
🍸
❤️
➡️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 1.2K · <a href="https://t.me/IranProxyV2/8479" target="_blank">📅 09:25 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-8478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ولی من که فکر میکنم، همه اینا برای کنترل قیمت نفت و باز شدن تنگه هرمزه، که ترامپ بعد از جام جهانی تا اون موقع بتونه باز حمله کنه
🙁
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/IranProxyV2/8478" target="_blank">📅 09:17 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 1.33K · <a href="https://t.me/IranProxyV2/8477" target="_blank">📅 09:06 · 03 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/IranProxyV2/8476" target="_blank">📅 12:04 · 02 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/IranProxyV2/8475" target="_blank">📅 22:02 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/IranProxyV2/8473" target="_blank">📅 08:34 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/IranProxyV2/8472" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8471">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/IranProxyV2/8471" target="_blank">📅 22:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8470">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/IranProxyV2/8470" target="_blank">📅 21:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8469">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تعداد ۷ الی ۸ نفر از دوستان به علت اینکه ربات شارژ نشده رسیدشون تایید شده ولی کانفیگی دریافت نکردند، خواهشا فقط کسانی که این مشکل رو داشتند با شات از رسید واریزیشون تو ربات + شناسه پرداختی که ربات براشون ارسال کرده به پیوی زیر مراجعه کنید
❤️
✈️
@russiaproxyy_support</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/IranProxyV2/8469" target="_blank">📅 21:00 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/IranProxyV2/8468" target="_blank">📅 18:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوستان دارم سفارشاتونو انجام میدم، شرمنده اگه کمی طول کشید کار مهمی برام پیش امده بود الان هستم همرو دارم انجام میدم براتون نگران نباشید، پشتیبانی هم براتون فعال میکنم تا چنددقیقه دیگ
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/IranProxyV2/8467" target="_blank">📅 17:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8464">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📌
آموزش وارد کردن سرور v2rayNG
⚠️
دوستان عزیز دقت داشته باشین که حتما برای وارد شدن و برداشتن لینک های سرورتون حتما لینک سابی که ربات بهتون میده رو کپی کنید و در مرورگرتون وارد کنید، بدون هیچ فیلترشکنی
1⃣
تو عکس شماره یک وارد همچین صفحه ای میشید Qr کدتون قرار…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8464" target="_blank">📅 13:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8463">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/IranProxyV2/8463" target="_blank">📅 12:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8462">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هرکسی مشکلی داره نیاز به پشتیبانی داره، پشتیبانی رو ساعتشو امروز بهتون اطلاع میدم
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8462" target="_blank">📅 12:19 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/IranProxyV2/8461" target="_blank">📅 03:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پشتیبانی ربات غیرفعال شده، از فردا ادمین جدید میاد مشکلاتتون رو بررسی میکنه همینجا اطلاع میدم بهتون چه ساعتی پشتیبانی بازه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/IranProxyV2/8460" target="_blank">📅 02:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تمامی سفارشات انجام شدند، ربات مجددا روشن شد
❤️
👑
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/IranProxyV2/8459" target="_blank">📅 02:49 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/IranProxyV2/8456" target="_blank">📅 17:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mafI1O4zvwe_1YHmFpdwl_s3S2NtcYEqHtTKzvyalX5yJAdsx28tPffLR_UFTrWc6XhQoUN5KHQQsmI96xsOHIYmcKcKuVk_qml8XaSW0-KCujOWL05gUGRQphgZPuHuAFssLoAp1voVGBII-M95Y7fzZ3jLRn-roC_raa2qZ2YIXH_XRTz0FzbwliV_TNb8-SF3XCdElwbTVxso-heVS0w1CDKgOISuM99XiOWObmLGnvq4_HSF1DBD4ND97LOiJR1x_s0XK3COVqug5aZ_T5yjIJ1M1uQ99-ZcIoEHxdveIAcAv7_jeQav_GYwQcNTPpn0UMSm_hAbHj2XjmPJmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده امشب</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/IranProxyV2/8455" target="_blank">📅 17:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/IranProxyV2/8454" target="_blank">📅 16:04 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mq4CFgho5khrkqZMHezzJ6cDH5Y23MoL1ZMlUQJvUu2fbTU7S1ZSaPGHhhoCVGqrbCJz5ML0cNY3kgPXs6FBID2rsyFpENGWyRpt-dkp4Pe7MuNjAyEw6Rq2H0w3IbP6Lm1d3vi-J-jOCmXeNUPLGBRLKYgVh9Sj-ui3Jvy-ITepY1J8ojv3BImCrjq3tU25rc63LPaLtuLkPmekV-ez_JsBZgVtrwlPeBeAmONmF2vOG5Sg1Pi5f__Y5Xhgy8kjILpL04TXg7MtqyC4oaBe5D7iaR9moR2maFEoA9TZ_dD59n6FLT90eOsZL2-gGR2RUK4oJD5UiwHJ1JU1OTY3mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/IranProxyV2/8453" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8450">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">حجم سفارشات بالاست، درحال ثبت سفارشاتون هستم، مرسی از صبر و شکیبایی تون
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/IranProxyV2/8450" target="_blank">📅 12:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8449">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaJxx8bQF3ntV3D8lShjJYBl2pHM3ZOf9NlbxxYdny4UHJCDWZoPdF37OQz4gKyzgotsmk2O9ziH6UBPap3QvMPx5VotUyvrSo1vrjYlfA1P0ZgKJprGwDwydTVs3WJCVz0SSguMLHeP1S4zjqiICUMj6mj5PYui_0GkjDrWw_hHNt06riYv_EkVZBIY8QJNu0t6vHtbX0-q4bxE5yNyS7Yj72kBk_d4P3L4f797bGNfzEMH13x7nRf6iB74cthsSOH8gcDoZvg4I98ZwD6rDvY_53__RYT2Jji_HqJNExCW7lz7SJdFpAr6jXPagFjZVXkIoudmq0N5UAothQBiUw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/IranProxyV2/8447" target="_blank">📅 03:14 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8445">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_tk3d0B5HX8kAykJUBolLeH7JcrZJ-sRVwKnvGn42d_yvsnpKpJOm431aP4uliwgPm8cOzZFiGTiL7e2BMixVkMqa1CaJLRbA5nr6dpL8lkLr_biqIvCtGVBRkqxAsRTNLSDAB8mXKiT3RLuddywq9Lku9Mt3i8ZXcxYfzWhMICMyUqG9yEp2Pe1H4QoWplZ8JJdptDNya7re5Br6z0bNSasE4jXCMyzlHPElbED21iIzcJv0BNNcE47YhtCqUQpZ7EXWM5nYlx4FOhDqRxMi9UpI6118Kr9KRksZyxZEjs-wAaA59HvhKCXLLbOKebs7P3HuEem3Es38WGoNPfNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن  https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/IranProxyV2/8445" target="_blank">📅 23:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8444">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تا ساعت 23 هرکی با لینک زیر تو کانال جوین شه قرعه کشی میکنیم اونایی که جوین شدن
https://t.me/+TkcQjtWRitUzZjJk</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/IranProxyV2/8444" target="_blank">📅 22:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8443">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دوستان درحال اپدیت سرور هستم نگران نباشید مشکل از طرف خودم هستم سرورم رو نت های گوشیتون درحال بهینه سازی رو وایفا اوکیه تا دقایقی دیگه حل میشه رو نتای همراهتونم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/IranProxyV2/8443" target="_blank">📅 22:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8442">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب قرار بود چالش بزاریم این چالش به صورت قرعه کشیه بالا باشید</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/IranProxyV2/8442" target="_blank">📅 22:17 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8441" target="_blank">📅 21:01 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/IranProxyV2/8440" target="_blank">📅 19:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8439">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">امشب ساعت 22:00 چالش داریم با جوایز کانفیگ
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/IranProxyV2/8439" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8438">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپروکسی | فیلترشکن | کانفیگ v2</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1PFcRYam0B87rWNkKmnAQ8hJ-qqdjii2HvOYOif12iWe-NxkyZcVz6Uvt_m-Q51wmunnCSiSsBuIzYnz1KVkPV5cOcsSj_udxg2JOrcXpvmlRrXljs7haL6c48f43hchdTqQpXG8x-PQ-pRhVN8gwbiKSormEMMPRDJDvrJh4XO7u0_H5MnNjwJGohjdZy4JZqx1Q5H3-KxMbr2YffwX7MYuTYcmg9wT8RTvZZxjOw1g8HzCVZyNa3enKqEthEitHdxgKDhibpurbl2XBqS3V5zNrI0uRRC71ESP7O99jxAFoCzIojBhi4zrcf_ocjBiFrPAh2-OLnMFGvNNnLPfg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 2.72K · <a href="https://t.me/IranProxyV2/8438" target="_blank">📅 02:05 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/IranProxyV2/8437" target="_blank">📅 01:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8436">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ربات مجددا روشن شد برای ثبت سفارشاتون
❤️
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/IranProxyV2/8436" target="_blank">📅 01:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8435">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/IranProxyV2/8435" target="_blank">📅 01:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8434">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">دوستانی که سرور پروکسی داشتن اگه تعویض نکردن برن کانفیگ تو ربات زیر بفرستن کانفیگ تازه بگیرن
❤️
@editmylinkbot</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/IranProxyV2/8434" target="_blank">📅 01:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8433">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوستان ربات جهت آپدیت و اضافه کردن سرور تا ساعت ۲ شب خاموشه
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/IranProxyV2/8433" target="_blank">📅 22:47 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9K · <a href="https://t.me/IranProxyV2/8432" target="_blank">📅 21:07 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8431">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ربات آپدیت شد و روشن شد
🍸
❤️
✅
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/IranProxyV2/8431" target="_blank">📅 21:02 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8429">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ربات جهت آپدیت چند دقیقه ای خاموش شد
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/IranProxyV2/8429" target="_blank">📅 19:56 · 28 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=GKHz9RKPHG6U60TgJAF7kfPXupE0SsGRhRNGZtw2wTjTeEzbvpKDmhWcDjqItGiOzXy0eFDeTBGBxrGotgLw3oWgxhgqrt9Zdidx8WbL7vIPUP8bQDfb0hIAXbXBeo3LEgUokGewo0t5bUdJoOQgTcWWf0uPyy_BrQIJ_2b8ScsydSXQWEXIQ0G0eqmWqrw6UgJ0GtOiHW3SaGCRsfPQmE3mhLrMpdRh-iHV6_ASvfrR_NEqfoi2zZoeWmSQKMBwrs6RDVus6sBwJE2VnDkftybpP_7-I08c16hZAlSiGoZhgfYi9LCi-tCT7-ZKSh6UBvVOqC5jKY-B9isU8rZ9m6s9Z1BeGZSfIISa4u2_wTHYi31mQs7Es1Xt7YfqrD_Sb8na2_RPIoGzimSgU5U5g_iDNrkRFBjvjgzMwdW9l_blc53pvO8bJfqaPt9MqyYd1TFgY4VXgelT_R4JcZHCsxr1a_sn7Rq4LsNt1ss5loElTaY40U-QXP1P5fkhBRC--5nGmgyXX36wFejUCmFD30kjAUJTu4DnxQ09T4prHL45LaSRNsHPMGOEuYXIijhNTKElqOGZypLOu-5x4a-5dK73duTdVzBHY0JzULsd2fWHpyFo85ysohBHs4hnkB4pBwxn7oNpSLobKyPAOS9tF6Y--W5S7vmIL5nIYScw4dM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ebebfd753.mp4?token=GKHz9RKPHG6U60TgJAF7kfPXupE0SsGRhRNGZtw2wTjTeEzbvpKDmhWcDjqItGiOzXy0eFDeTBGBxrGotgLw3oWgxhgqrt9Zdidx8WbL7vIPUP8bQDfb0hIAXbXBeo3LEgUokGewo0t5bUdJoOQgTcWWf0uPyy_BrQIJ_2b8ScsydSXQWEXIQ0G0eqmWqrw6UgJ0GtOiHW3SaGCRsfPQmE3mhLrMpdRh-iHV6_ASvfrR_NEqfoi2zZoeWmSQKMBwrs6RDVus6sBwJE2VnDkftybpP_7-I08c16hZAlSiGoZhgfYi9LCi-tCT7-ZKSh6UBvVOqC5jKY-B9isU8rZ9m6s9Z1BeGZSfIISa4u2_wTHYi31mQs7Es1Xt7YfqrD_Sb8na2_RPIoGzimSgU5U5g_iDNrkRFBjvjgzMwdW9l_blc53pvO8bJfqaPt9MqyYd1TFgY4VXgelT_R4JcZHCsxr1a_sn7Rq4LsNt1ss5loElTaY40U-QXP1P5fkhBRC--5nGmgyXX36wFejUCmFD30kjAUJTu4DnxQ09T4prHL45LaSRNsHPMGOEuYXIijhNTKElqOGZypLOu-5x4a-5dK73duTdVzBHY0JzULsd2fWHpyFo85ysohBHs4hnkB4pBwxn7oNpSLobKyPAOS9tF6Y--W5S7vmIL5nIYScw4dM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=j470kpVWq6shYKtlfWv3s6E02a-yHwlE0gxMjiX96_WDtmmQeHGmVdcN7RPJVIHTQqLmJwqskqddXdPWQyfXXe8By2_ZaBlC4ickJGZow4-XRTSgqMf_KMyWyBfRHzHFt3hlhAqSFs9I70AYJ_8qTvng_gVn8BfyuImLjTAyUmvZCoJ8wO3PpzRt1AWYJo05Z8Xyl3gDFzI3aR_36ImIqaQt4me7TPhQN7FQi-Lq-sl5PuK-iIwxMqMaMf2AM3R37J5AbpigwHQ0dtZpKraaRvgCmtXfA0kSfOea4VNBOoho9vYbbWorXrJi_QakJiAX4AqgFqGWG7wu_E55UAo9vWuJSiMdhtP48KfbMvXtJytpLsZTWshYQNeb6stEKlfWuzlN22dslUJZn9CwxiCMI2QHYIV1nLxnN1-s0c5PWAUFgaFRWg0HIL5cfA6Axzqvx5yjhNIdoXcWdfKNmMw41d_g7gymtUra0XeP_Z08_odQ29wV93Nv-lnsm-SWcaE5vQgg9HWHxtAnVCkURoeZm6g8SIAZJK9YGYR5U9iGC1gwmYfM-dTV9Z1Z8pECIRGgzbLQ6VQF80auVUy1IEz7wobfRmNRqMaUFQB8vw7i--OMM1ls26osxNqctzGvFZQmFGcx3CdC6OPaswgI662K7QMA6dXOd0pBmGVxv7hYozI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a572e4966.mp4?token=j470kpVWq6shYKtlfWv3s6E02a-yHwlE0gxMjiX96_WDtmmQeHGmVdcN7RPJVIHTQqLmJwqskqddXdPWQyfXXe8By2_ZaBlC4ickJGZow4-XRTSgqMf_KMyWyBfRHzHFt3hlhAqSFs9I70AYJ_8qTvng_gVn8BfyuImLjTAyUmvZCoJ8wO3PpzRt1AWYJo05Z8Xyl3gDFzI3aR_36ImIqaQt4me7TPhQN7FQi-Lq-sl5PuK-iIwxMqMaMf2AM3R37J5AbpigwHQ0dtZpKraaRvgCmtXfA0kSfOea4VNBOoho9vYbbWorXrJi_QakJiAX4AqgFqGWG7wu_E55UAo9vWuJSiMdhtP48KfbMvXtJytpLsZTWshYQNeb6stEKlfWuzlN22dslUJZn9CwxiCMI2QHYIV1nLxnN1-s0c5PWAUFgaFRWg0HIL5cfA6Axzqvx5yjhNIdoXcWdfKNmMw41d_g7gymtUra0XeP_Z08_odQ29wV93Nv-lnsm-SWcaE5vQgg9HWHxtAnVCkURoeZm6g8SIAZJK9YGYR5U9iGC1gwmYfM-dTV9Z1Z8pECIRGgzbLQ6VQF80auVUy1IEz7wobfRmNRqMaUFQB8vw7i--OMM1ls26osxNqctzGvFZQmFGcx3CdC6OPaswgI662K7QMA6dXOd0pBmGVxv7hYozI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/IranProxyV2/8423" target="_blank">📅 11:49 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8422">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دوستان چند لحظه ای ربات خاموش میشه برای انجام سفارشات
❤
🙏🏻</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8422" target="_blank">📅 11:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8421">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">karing_1.2.15.1806_android_arm.apk</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/IranProxyV2/8421" target="_blank">📅 10:57 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuzsxfWWWHh-kV7Qy9rmaiMPtCZs2AcTItkVsVp9nd-QAyhrtz05Tjjsnsvid5rj-vMxXyS_Jrv4iYRwQbQqANeDkAucIoLf8jKXDdIzzHaEfVriFzknZD0UR9c00RV5zcSC7ENszlgV-jG2qXnjblyoLoUgS78ZfmDopy433Xygk7VJPl5NI0h8Bjx0xoUNIkDUssxbdKjhQB_lFUUawrVTi4ZzE0waThCet1Z0KAzu_c4wXNGjq_-czhmm2cHA1UEdbr3sPqEIBNokS0BKwsZPMzUb9HSYt7NuqQHpjbLYiXnycHZh7UbzlW4nijPro2RSYDQYZ94fzdj1h4adbA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/IranProxyV2/8418" target="_blank">📅 02:55 · 28 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Borrlq-Cgmcw2eo3jmaivwO-nu5C8CO7F2JXTdbP2l6PTkuy4tDYNIz7CPE72REyUdPstf1M2Ghtqr2QSIR8MWAPZa4h5WdC4tfFm19oEPr9onobU_cMj2fcLaMQYHbPGut9aGTB9rQ6O4nPeKmhgcmKz8x6erQR2G_uejVkDqfbliFQZCe4PSEEmWIJ6FV-c0m72eBqBDxqxwo9l20zKYQRvgyb__7MFpBSG8Liu1BVWIiFCIp1AStJjwaLX2uk8u4W5MW_wZ2ATkaPzGAA6d2s1iP7cwFfGnoqzDRZMOWnfkfPFLCfwZGPgQOSlJtsN5NtaQrwY4yIldxtyy7caA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همچی فیکس شد و با بهترین کیفیت
😯
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/IranProxyV2/8414" target="_blank">📅 19:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8413">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">حجم سفارشات بشدت بالاست، صبور باشین دارم یکی یکی صحت سنجی میکنم و تایید میکنم
❤
✨
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/IranProxyV2/8413" target="_blank">📅 18:32 · 27 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=LlVcZ1W2LRlD7JukqUBaD9KINLeKbZlJ7yLMCVzSOKLGYxSrjpnlWvR_6AvZm0lJJveq_57IENTMn74ijeKSNwUnexiODLlJG4NYiqgp-b1X2adEB3VdUJdY0WJxU6nGsNO0mrj2S1nUnMy0DvrB4Lrq9m-v_EekAXeQ_wGDXJ68eHU9qUqzMnihSGwkDrmqHmAwXy3OQqWzpgop3RIbqBG20CRMmpJO8rAaQS-Jt1cNVwqBkIMiKhb39pVxTSaD0EGuw9_IdQML8wvaoJhvYCJMxdA7G7yoWV4kNE2nLomFT0PFc4fjMo-xQtSQODX1Onug5YOzvA23vHhnQRsmyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5519cb51.mp4?token=LlVcZ1W2LRlD7JukqUBaD9KINLeKbZlJ7yLMCVzSOKLGYxSrjpnlWvR_6AvZm0lJJveq_57IENTMn74ijeKSNwUnexiODLlJG4NYiqgp-b1X2adEB3VdUJdY0WJxU6nGsNO0mrj2S1nUnMy0DvrB4Lrq9m-v_EekAXeQ_wGDXJ68eHU9qUqzMnihSGwkDrmqHmAwXy3OQqWzpgop3RIbqBG20CRMmpJO8rAaQS-Jt1cNVwqBkIMiKhb39pVxTSaD0EGuw9_IdQML8wvaoJhvYCJMxdA7G7yoWV4kNE2nLomFT0PFc4fjMo-xQtSQODX1Onug5YOzvA23vHhnQRsmyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmWDHpciJmSy-BoOuZJ48T0FO3heyjE2IcshzCiS3_2WJlBDXHxGJLjochH0DFN2mHnB-hqT1ZvpkxU69IDgCzNBT-bO9GF0OoaAL40fYYB32Ehc-7m8JGk9P96w_0K8NoFzti5ZA4qr1klCdo98mjNtx2X_ZkL__nfz64i2nFIW4HY6CsoWZLnskPowIRlTo6qkSRi29L88RUN8DS1WANU6EpSMSHOpmq01hSKDA407W-PIA2u-dWjyLtDxytZD9aPWu0CjOJrfDu-LHCxWhZZ5oTTDAnA-lLlhfp3ZUA53lKPGU8xW7OaDF4e8Ynrz0B8el3Icgj25BvjezbvSRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/IranProxyV2/8407" target="_blank">📅 20:50 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADX9E7kndOu6PJBtAbZuW5bjEqGnyo0miVLVR_ua1hc9lyl_tszg5q518UwNSFRWWr7cwfXrUhT51zo8_QNGxgT9MB4ECQT6y5xgj-ZYHRluem-6IYOwPCaifE3LOwP2fTWeVPJiH6dkYJUosZ2UwGS6RkAjI32an1AjaJqogywxVZvKAwZ4dWYwOOIALLA1WToR5PrqA5qPoltHuL0DtL8BAyENiTNULPEPMqFu1L5-sfkHJVDRmgjwD-7T3faSdL1hglY7N10qwp49D-6MoaSFtuzIXo-zm6F8RQLLlJrfVAH1uqqDlqtFJ5xZS6PlZZuH9fi1Q3erAiLilMH3Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب دوممون
❤️
🍸
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/IranProxyV2/8405" target="_blank">📅 20:36 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/IranProxyV2/8403" target="_blank">📅 20:22 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/IranProxyV2/8399" target="_blank">📅 20:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/IranProxyV2/8397" target="_blank">📅 19:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/IranProxyV2/8395" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/IranProxyV2/8393" target="_blank">📅 14:45 · 26 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=heu75u81txnRygvoEq0WQLdLthSa2DR7jy2G2M4yaxs2HZlxMXaTcicFzbhOMOA8p0TJxJSDAtS5o10DdnnD0cDEkkSxvO6s3Z7Lkr7ZILRvf2ZWQ7b7QO9Rd5JS_sA0uEfaXpHgmHaBZaQqj6BxlkWJn8AInncS-aFGHajqVzVJdcXy-3Qf0D11FBARlfqRofpzZ6-q6NNkwEz9x7mAOorR57v_m-jVrGPhkUpsV2bMwSxVaoAhdJgqKdzSGG0VoL8ZYZ6FBSCHtLCZBT46QZUy6G6pypHNCvv259ci9ZOL9CnbLGbboWnGg8gbE-imUp2hqFL7uhG4XWjzMQSI2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a909b2b06.mp4?token=heu75u81txnRygvoEq0WQLdLthSa2DR7jy2G2M4yaxs2HZlxMXaTcicFzbhOMOA8p0TJxJSDAtS5o10DdnnD0cDEkkSxvO6s3Z7Lkr7ZILRvf2ZWQ7b7QO9Rd5JS_sA0uEfaXpHgmHaBZaQqj6BxlkWJn8AInncS-aFGHajqVzVJdcXy-3Qf0D11FBARlfqRofpzZ6-q6NNkwEz9x7mAOorR57v_m-jVrGPhkUpsV2bMwSxVaoAhdJgqKdzSGG0VoL8ZYZ6FBSCHtLCZBT46QZUy6G6pypHNCvv259ci9ZOL9CnbLGbboWnGg8gbE-imUp2hqFL7uhG4XWjzMQSI2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از تست سرعت سرور اینستاگرام همین الان
@RUSSIAPROXYY_Bot</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/IranProxyV2/8390" target="_blank">📅 13:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8389">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=jsbiCOKW93yV00AKBEtZKTeHbWSQkTfVX8nhxPAyyVFVMVfqO-8JgTdfmThV11DhD0_SHDV8srtPnLa6qe0PcXKWa-R04ePXokdG5L-Bgh3zokH0lVRZoBSYO5ggQJ12bPDkuGF9j941gWyL23NvyVfirjL9i3XgVFtdcRxPVtDiNd1_chXRGtjo5QYuFsTUwtFFqdSeuKtXaTXrvM8C6qFGFVpRWmIv6G-zmF85cyuOMEbkF3Vhit9dUBUv41TQx-EFtt9x4nRu097MLCdgKlQIZRehCTVwy6H1sm8f5RKYoULjY2MpS3iqGaAWHMAJ0j9I2LALUIQtVJyyvvA8nDCqnpZYAGJoZoZ9U9g5yOJxdzAfiaF_RPkoww5skeQYzviZw1H8zPsA94zy32eBmkmuAEgXa_gwRukGC_Wm8cb3X7PQzRAB47ukMGvfPfrafdsyuR4bxBdY8yVtR7obxhBgDWMbCpi5u0yvgyA8y4qO4lGkfRyjxYkQMqHh2BafX7wVKYjyk_RTZP6joq0dyHMwQsYEdtIchR1KVt8jf_XLqafc-VEANy4m7AILajK89tAI4YLio6vTHfHLXZLGIWzbOeQhI3_Oze9hk0GYHk38QvbHTN2MhBeW-2We8IdwNkcDZh9zMJrlnBVv96TJI9xKS1RVA77VX82addnjEJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea2fe2cdfb.mp4?token=jsbiCOKW93yV00AKBEtZKTeHbWSQkTfVX8nhxPAyyVFVMVfqO-8JgTdfmThV11DhD0_SHDV8srtPnLa6qe0PcXKWa-R04ePXokdG5L-Bgh3zokH0lVRZoBSYO5ggQJ12bPDkuGF9j941gWyL23NvyVfirjL9i3XgVFtdcRxPVtDiNd1_chXRGtjo5QYuFsTUwtFFqdSeuKtXaTXrvM8C6qFGFVpRWmIv6G-zmF85cyuOMEbkF3Vhit9dUBUv41TQx-EFtt9x4nRu097MLCdgKlQIZRehCTVwy6H1sm8f5RKYoULjY2MpS3iqGaAWHMAJ0j9I2LALUIQtVJyyvvA8nDCqnpZYAGJoZoZ9U9g5yOJxdzAfiaF_RPkoww5skeQYzviZw1H8zPsA94zy32eBmkmuAEgXa_gwRukGC_Wm8cb3X7PQzRAB47ukMGvfPfrafdsyuR4bxBdY8yVtR7obxhBgDWMbCpi5u0yvgyA8y4qO4lGkfRyjxYkQMqHh2BafX7wVKYjyk_RTZP6joq0dyHMwQsYEdtIchR1KVt8jf_XLqafc-VEANy4m7AILajK89tAI4YLio6vTHfHLXZLGIWzbOeQhI3_Oze9hk0GYHk38QvbHTN2MhBeW-2We8IdwNkcDZh9zMJrlnBVv96TJI9xKS1RVA77VX82addnjEJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOBl7SIXCHcrox1TyiJ2x0ZeYN5cKqdfoMNV49WbOnrUIMRYexxkNn68UYUId53Rdrxxihxegr6d96RDhJed40W1VtCxX-QgMh5_ZEHu1OgLjEpaI9vGKtvtHoog_2QRGpevuKV07WH520QDcFxtA4sa04U7CgXHxKsisPlP2HY8YVwdqAEAuKBGvaPkBqMy2MQaiO9CKdxRxRjEJFN6ResR9NDhsqwxGrBLEqlBvPca5G6-KuE15jwyTTFeGXUh8mAg8xr-xG0FVSIG_h8llNvKZtUlxHgZ25EtvsW0GXtWjmeV0RevnteqHoCiqlS8iSuGNvNLXREmPghMzxVqFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6S9eEmlgdGx8OCZ0g5sdN-dE7kIHMzYwC89eK6fwU5kRFd4oz2hjDrcyiUJkcVbpuAuHRp64i_shf7hE4fvdtW7IqDaiWIsjPOXwBCSEBjMOq4RTPBzT0MqD7WBd1EXnZABE9R9-Yfz5nl5c9NZmqTowJSHsR98Aa_AohWpJ-IM60O-9FKAaXmIeurYjBmEwj_r--xpGDyTeLxdpYtBBeC5eZi7eQmhjYQh2pE140537gKNdwhAbZXbGUBYdtCRIxfFfDiFkEs9Y1lZCAq7ZWhe_RcMWDGf6O-YTrjWTWin_6di-j6xDeeOmCGgept5wtAFjwLDUSUGY4MmwyUWzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده چالش شب اولمون، از این به بعد هرشب سعی میکنم چالش با جوایز بیشتری بزارم براتون قلبا
🍸
❤️
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/IranProxyV2/8384" target="_blank">📅 03:03 · 26 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/IranProxyV2/8373" target="_blank">📅 17:43 · 25 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/IranProxyV2/8372" target="_blank">📅 11:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kKlFy80jog7Ckth89WD1I8EpFJEXVevhD6Ve3d0NggUW0QcW2KePdf85yaegSPbPmhoGiwyIOwruFYoQbwrQL5iCSEFFC31QBCPEI6whJkrrp6cUOYuhSVCREoioeVdPKIagw_YX82WVnnLWL5eggv9h-6cF3c0gXHYe-vL8xaCyxNaYdzI9edavk3sGm2teWGSBvOhfsEuhDbst59OphUNwSNFQ8Zevi9_roO1ufisESidn2PlKsqM92Cu1mr7FFRHb_QWvMwY0ygPCgyfsTKj40UyhKekQuQmXwx7rv0WnCP6foBDiI2jEjRzHUAyDEQoOiRJKfq6iA2ujY47I2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قیمت جهانی استارلینک مینی با تخفیف به زیر ۲۰۰دلار (۳۶میلیون تومن) رسیده و پایین‌تر هم میاد. سایز دیشش هم اندازه‌ی یه کاغذ A4 هس و براحتی همه جا مخفی میشه و با وضعیت ایران هیچ رقمه نمیشه جلوی موج قاچاقش رو گرفت
.
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/IranProxyV2/8371" target="_blank">📅 11:33 · 25 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=bXrmyTHK_z3sCWGfjidD6fAWl1Tns57_gmZqbj2Ic9NWH89yzkTKpNOi4k5mTGxQ1eKF9tPc5cu7IEBfMBLTaOkMIbCEFa6VLrbCHotxSbRsuu7o02GYPSqZBTSHVLWRWfYVvEQ0wa_VMRXlnLvAMpuJWkV1CkNCW4adeNSGMdU5TC4f-FPGh8pBClhkJzgzVdkFYZ_i4vWHt_MJFj92NX44cWKRWBZvcb-K5Qfpzg9XWfPnLwQSm4wnOQtvc4AzgZ03LO09giObSSyWaqycsuZkNZYugw-8sOD8i5Cpb4pGyVyeIDIfSsZY8aoI-ktrp3PUqPJKpQUYxZIpZYfTWKUAeL7dVnN8juLed7XR9E6drB5m8g2RwTfMHbO25C1bBI57ptJiwPsT-KHVL_f0no5rwb7FOUQHTHcemI7Yyc8BjeMuNL8fRPBXznajhOFY8oEjTTWMYpp417Sa0KDul_YiHcpbP_vFZWahuSFz-Z8nVqa5ctT1jXnuBaWhDZF4FyqYe5onPxS5A-A3sNYfkRLu8M0tChjIP4ouZMKRwqilGKDrpa2C2v3rCOlqAyRDmd_wcDoi3tRfR5jcnWWm-6R1oXr8nOVs6EEojP2mzi7Zy1KjVW7IiOY6HtLPkcJfgTWlICN_PRHi65FL0WaZLA2qw-ctDb_HCGy2M8SyySo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c04f638d20.mp4?token=bXrmyTHK_z3sCWGfjidD6fAWl1Tns57_gmZqbj2Ic9NWH89yzkTKpNOi4k5mTGxQ1eKF9tPc5cu7IEBfMBLTaOkMIbCEFa6VLrbCHotxSbRsuu7o02GYPSqZBTSHVLWRWfYVvEQ0wa_VMRXlnLvAMpuJWkV1CkNCW4adeNSGMdU5TC4f-FPGh8pBClhkJzgzVdkFYZ_i4vWHt_MJFj92NX44cWKRWBZvcb-K5Qfpzg9XWfPnLwQSm4wnOQtvc4AzgZ03LO09giObSSyWaqycsuZkNZYugw-8sOD8i5Cpb4pGyVyeIDIfSsZY8aoI-ktrp3PUqPJKpQUYxZIpZYfTWKUAeL7dVnN8juLed7XR9E6drB5m8g2RwTfMHbO25C1bBI57ptJiwPsT-KHVL_f0no5rwb7FOUQHTHcemI7Yyc8BjeMuNL8fRPBXznajhOFY8oEjTTWMYpp417Sa0KDul_YiHcpbP_vFZWahuSFz-Z8nVqa5ctT1jXnuBaWhDZF4FyqYe5onPxS5A-A3sNYfkRLu8M0tChjIP4ouZMKRwqilGKDrpa2C2v3rCOlqAyRDmd_wcDoi3tRfR5jcnWWm-6R1oXr8nOVs6EEojP2mzi7Zy1KjVW7IiOY6HtLPkcJfgTWlICN_PRHi65FL0WaZLA2qw-ctDb_HCGy2M8SyySo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت سرعت سرورامون همین الان
@RUSSIAPROXYY
🇷🇺</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/IranProxyV2/8367" target="_blank">📅 23:20 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/IranProxyV2/8365" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-8364">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=qPZxRaaP_QbdnfopYI8_HGg1tkJk8sxrRa484i_wVqVdD-fyR0GUPMOy_n434of2hxnX3bqfMVIjud99zGf4NdFkL5GJd1YgN_as2f4A4oZPN0DZENiFtYE57BGyjeEQNEGgDgoKT6xK0xHbKwj6oAmlhUkM2HuQoWC_Px1aTwaBB-1jNrM26w7eKzSgzmUVd7X5-RlhUpFnkeVLsRnrDtxcKckQpwcJx3DTZwPQl9A9x7Ti6kJ_uZX6plXrHfLE124PuvOpr80cEeHf97ZM-p3zhJDIVo-MWdUcYUjyxog5TndCIIt4tSCaQpeC4d-_WfPCM2TQIUlJDM1p_fAnmRy0G1gNziYyJ0c454699rcqxprvEzdXRZ_U5AEtRMGkTidQiUjCOhizxP9XCBmxzJ7BsRHVMWVG7kG_WR3-iHDxfCFu_8O4bhzPn5Hx2HV793vOkADl8xkoVkNYJFImQiwPMbdAfUqY9MISm-7eQ94yRsMrI8cfNuhkSsXGW_qcXYQDiNa99TcrP1J9ii7Ex5Y6oYWvV0ObI4g9sa1MJ4YYQyZWZ8_dHYIjr2Cg5cz8cuaYWMgVDZyxKDXrm8CT_HuaX8WqxNxMXhF1qng1Mz3bMP0DB3Z1zrfOqOAvM8BELQ6-1h0vtA5T1mVUyAFthNq8UPGhuOjUC3NN9RrIJUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01732adaf2.mp4?token=qPZxRaaP_QbdnfopYI8_HGg1tkJk8sxrRa484i_wVqVdD-fyR0GUPMOy_n434of2hxnX3bqfMVIjud99zGf4NdFkL5GJd1YgN_as2f4A4oZPN0DZENiFtYE57BGyjeEQNEGgDgoKT6xK0xHbKwj6oAmlhUkM2HuQoWC_Px1aTwaBB-1jNrM26w7eKzSgzmUVd7X5-RlhUpFnkeVLsRnrDtxcKckQpwcJx3DTZwPQl9A9x7Ti6kJ_uZX6plXrHfLE124PuvOpr80cEeHf97ZM-p3zhJDIVo-MWdUcYUjyxog5TndCIIt4tSCaQpeC4d-_WfPCM2TQIUlJDM1p_fAnmRy0G1gNziYyJ0c454699rcqxprvEzdXRZ_U5AEtRMGkTidQiUjCOhizxP9XCBmxzJ7BsRHVMWVG7kG_WR3-iHDxfCFu_8O4bhzPn5Hx2HV793vOkADl8xkoVkNYJFImQiwPMbdAfUqY9MISm-7eQ94yRsMrI8cfNuhkSsXGW_qcXYQDiNa99TcrP1J9ii7Ex5Y6oYWvV0ObI4g9sa1MJ4YYQyZWZ8_dHYIjr2Cg5cz8cuaYWMgVDZyxKDXrm8CT_HuaX8WqxNxMXhF1qng1Mz3bMP0DB3Z1zrfOqOAvM8BELQ6-1h0vtA5T1mVUyAFthNq8UPGhuOjUC3NN9RrIJUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF9dDNBlGP_H5Dn_NinR12Egz4CyK4gcvbOdT6bymC6JlkrH3G1pvAa9lD7GEjV2J9oXEUbpG9W6mWwLOets7KKDJklhEgUzoNPkRKqsieJ2LD26oVsXIz9ANk_4JMaHzBo5B4AAX72X6mDROgTRRMYYs8k994UiQaTwEdqlXXZatbgQ5E4lWPhb_RRLYPQJhSBKg-3hZzYA0viLX3Z5elbHp3gtkLR0Fu_n1gCIHUarxMIBxVh5W2rv1ZaoAdv9ZN__pftZAt1mbzfcTESWC0sAk-1Djbhvkx8nz1tCIGp2OQDfvmvQVwWsuPLO_pMOZR-oY-9gs49L1QdsHfx6Jg.jpg" alt="photo" loading="lazy"/></div>
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
